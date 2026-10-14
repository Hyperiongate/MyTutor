# =============================================================================
# modeltrial.py  --  THE MODEL TRIAL  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-10-13  NEW FILE (build zl, PM-20 on the PM board; the 10-09 deep dive: "Move to
#               Sonnet 5.5, through a measured trial, not a blind swap"). Two models teach
#               the same lessons, and the numbers come back side by side:
#                 * the same scenario students (lessonaudit.SCENARIOS -- personas played by
#                   the night watch's student seat) take the same lessons from the same real
#                   prompt and the same referees, once per model, in ALTERNATING order
#                   (A then B, B then A) so neither model always goes first;
#                 * per model: seconds per turn (wall clock, the student's wait), the words
#                   it speaks (from the cost log's spoken characters), how often the math
#                   referees fired and how often a turn had to be retried, apologies
#                   ("lost my train of thought"), tokens and dollars, and -- when the
#                   critic is on -- the teaching findings a strict marker raised, by severity;
#                 * the report says which way each number points and leaves the decision to
#                   Jim. Nothing here changes what a real student gets: the trial's turns run
#                   on their own thread inside tutor.model_override, and are logged under
#                   the codes TRIAL-A / TRIAL-B, never a student's.
#               PRICES are Anthropic's published per-million-token rates as read on 2026-10-09
#               (platform.claude.com/docs/en/about-claude/pricing); a model not listed is
#               priced at Sonnet 5's rate and the report says so.
# =============================================================================
import json
import os
import statistics
import time
from datetime import datetime, timezone

import lessonaudit
import tutor

try:
    import store
except Exception:  # noqa: BLE001 -- the battery can run without a store
    store = None

DEFAULT_ARMS = ("claude-sonnet-5", "claude-sonnet-5-5")
ARM_CODES = ("TRIAL-A", "TRIAL-B")
DEFAULT_LESSONS = 4
DEFAULT_TURNS = 6
REPORT_DIR_NAME = "modeltrial"

# $ per million tokens: (input, output, 5-minute cache write, cache read) -- 2026-10-09
PRICES = {
    "claude-sonnet-5":   (2.00, 10.00, 2.50, 0.20),
    "claude-sonnet-5-5": (2.00, 10.00, 2.50, 0.10),
    "claude-opus-5-5":   (4.00, 20.00, 5.00, 0.20),
    "claude-haiku-5-5":  (0.10, 0.50, 0.125, 0.01),
}
REFEREE_KINDS = ("referee_fire", "pass_through", "floor", "code_repair", "failopen", "referee_crash")


def price_of(model: str):
    return PRICES.get(model) or PRICES["claude-sonnet-5"]


def dollars(model: str, u: dict) -> float:
    pi, po, pw, pr = price_of(model)
    return round((u.get("in", 0) * pi + u.get("out", 0) * po + u.get("cw", 0) * pw
                  + u.get("cr", 0) * pr) / 1_000_000, 4)


def pick_scenarios(lessons: int, ids=None):
    pool = lessonaudit.SCENARIOS
    if ids:
        want = [i for i in ids if i]
        return [s for s in pool if s["id"] in want]
    return pool[:max(1, int(lessons or DEFAULT_LESSONS))]


def plan(arms=DEFAULT_ARMS, lessons=DEFAULT_LESSONS, turns=DEFAULT_TURNS, critic=True, ids=None) -> dict:
    """What a run will do and roughly cost -- free, nothing is called."""
    picked = pick_scenarios(lessons, ids)
    per_turn = lessonaudit.EST_CLAUDE_PER_TURN
    claude = len(picked) * len(arms) * turns * per_turn
    other = len(picked) * len(arms) * (((turns - 1) * 0.002) + (0.03 if critic else 0))
    return {"ok": True, "arms": list(arms), "lessons": [s["id"] for s in picked], "turns": turns,
            "critic": bool(critic), "tutor_turns": len(picked) * len(arms) * turns,
            "est_usd": round(claude + other, 2),
            "est_minutes": round(len(picked) * len(arms) * turns * 16 / 60.0, 1)}


def probe(model: str, client=None):
    """Can this key reach `model`? (ok, detail). One tiny call."""
    try:
        if client is None:
            key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
            if not key:
                return False, "no ANTHROPIC_API_KEY on this service"
            client = tutor.Anthropic(api_key=key, timeout=30, max_retries=0)
        r = client.messages.create(model=model, max_tokens=8,
                                   messages=[{"role": "user", "content": "Say OK."}])
        txt = "".join(getattr(b, "text", "") for b in r.content if getattr(b, "type", None) == "text")
        return True, (txt or "").strip()[:20]
    except Exception as exc:  # noqa: BLE001
        return False, " ".join(str(exc).split())[:200]


def _lesson(sc, model, code, turns, reply_fn, student_fn):
    """One lesson on one model. Returns a dict of what was measured."""
    student = lessonaudit.audit_student(sc, "normal")
    transcript = [("user", sc["opening"])]
    history, waits, chars, events = [], [], [], []
    fallbacks, error = 0, None
    with tutor.model_override(model):
        for i in range(turns):
            bucket = []
            t0 = time.monotonic()
            try:
                with tutor.tap_events(bucket):
                    reply = reply_fn(dict(student), list(history), transcript[-1][1], sc["course"], code)
            except Exception as exc:  # noqa: BLE001
                error = f"turn {i + 1}: {exc}"
                break
            waits.append(round(time.monotonic() - t0, 2))
            if lessonaudit._is_fallback(reply):
                fallbacks += 1
            chars.append(len(reply or ""))
            events.extend(bucket)
            transcript.append(("assistant", reply))
            history.append({"role": "user", "content": transcript[-2][1]})
            history.append({"role": "assistant", "content": reply})
            if i == turns - 1:
                break
            say, err = student_fn(sc, transcript)
            if err or not say:
                error = err
                break
            transcript.append(("user", say))
    counts = {}
    for e in events:
        if e.get("kind") in REFEREE_KINDS:
            counts[e["kind"]] = counts.get(e["kind"], 0) + 1
    return {"id": sc["id"], "course": sc["course"], "waits": waits, "chars": chars,
            "fallbacks": fallbacks, "events": counts, "error": error, "transcript": transcript}


def _default_reply(student, history, message, course, code):
    return tutor.get_tutor_reply(student, history, message, course=course, code=code)


def run_trial(arms=DEFAULT_ARMS, lessons=DEFAULT_LESSONS, turns=DEFAULT_TURNS, critic=True,
              ids=None, progress=None, deps=None) -> dict:
    """Teach the picked lessons on each model and measure. `deps` replaces the four outside
    calls for the battery: reply, student_turn, critique, usage, probe."""
    deps = deps or {}
    reply_fn = deps.get("reply", _default_reply)
    student_fn = deps.get("student_turn", lessonaudit._student_turn)
    critic_fn = deps.get("critique", lessonaudit.critique)
    usage_fn = deps.get("usage", (store.usage_for_codes if store else (lambda c, s: {})))
    probe_fn = deps.get("probe", probe)
    arms = [a.strip() for a in arms if a and a.strip()][:2]
    started = datetime.now(timezone.utc)
    out = {"started_utc": started.strftime("%Y-%m-%d %H:%M UTC"), "arms": arms, "turns": turns,
           "critic": bool(critic), "lessons": [], "arm": {}, "stopped": ""}
    if len(arms) != 2 or arms[0] == arms[1]:
        out["stopped"] = "a trial needs two different models"
        return out
    for a in arms:
        ok, detail = probe_fn(a)
        if not ok:
            out["stopped"] = f"{a} could not be reached with this key: {detail}"
            return out
    picked = pick_scenarios(lessons, ids)
    codes = dict(zip(arms, ARM_CODES))
    per_arm = {a: [] for a in arms}
    for n, sc in enumerate(picked):
        order = arms if n % 2 == 0 else list(reversed(arms))     # neither always goes first
        for a in order:
            if progress:
                progress(f"{sc['id']} on {a}")
            res = _lesson(sc, a, codes[a], turns, reply_fn, student_fn)
            if critic and not res["error"]:
                marked, err = critic_fn(sc, res["transcript"])
                res["findings"] = (marked or {}).get("findings", []) if not err else []
                res["critic_error"] = err
            per_arm[a].append(res)
        out["lessons"].append(sc["id"])
    usage = usage_fn(list(codes.values()), started)
    for a in arms:
        rows = per_arm[a]
        waits = [w for r in rows for w in r["waits"]]
        chars = [c for r in rows for c in r["chars"]]
        ev = {}
        for r in rows:
            for k, v in r["events"].items():
                ev[k] = ev.get(k, 0) + v
        sev = {"high": 0, "medium": 0, "low": 0}
        for r in rows:
            for f in r.get("findings", []) or []:
                s = (f.get("severity") or "").lower()
                if s in sev:
                    sev[s] += 1
        u = usage.get(codes[a], {}) or {}
        turns_logged = int(u.get("turns", 0) or 0)
        out["arm"][a] = {
            "code": codes[a], "turns": len(waits),
            "wait_median_s": round(statistics.median(waits), 1) if waits else None,
            "wait_p90_s": round(sorted(waits)[int(0.9 * (len(waits) - 1))], 1) if waits else None,
            "reply_chars_avg": int(sum(chars) / len(chars)) if chars else 0,
            "spoken_chars_avg": int(u.get("spoken_chars", 0) / turns_logged) if turns_logged else None,
            "retried_turns": int(u.get("retried", 0) or 0),
            "referee": ev, "fallbacks": sum(r["fallbacks"] for r in rows),
            "errors": [f"{r['id']}: {r['error']}" for r in rows if r["error"]],
            "findings": sev if critic else None,
            "usage": u, "usd": dollars(a, u) if u else None,
            "usd_per_turn": round(dollars(a, u) / turns_logged, 4) if turns_logged else None,
            "priced_as": a if a in PRICES else "claude-sonnet-5 (not in the price table)",
            "samples": [(r["id"], (r["transcript"][1][1] if len(r["transcript"]) > 1 else "")[:400]) for r in rows[:2]],
        }
    out["finished_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    return out


def _cmp(a, b, lower_is_better=True):
    if a is None or b is None:
        return "—"
    if a == b:
        return "same"
    better = (b < a) if lower_is_better else (b > a)
    return "B better" if better else "A better"


def report_markdown(r: dict) -> str:
    if r.get("stopped"):
        return f"# Model trial — stopped\n\n{r['stopped']}\n"
    a, b = r["arms"]
    A, B = r["arm"][a], r["arm"][b]
    L = [f"# Model trial — {a} (A) vs {b} (B)", "",
         f"_{r['started_utc']} → {r.get('finished_utc', '')} · {len(r['lessons'])} lessons × {r['turns']} turns "
         f"each, per model · lessons: {', '.join(r['lessons'])}_", "",
         "| | A: " + a + " | B: " + b + " | |", "|---|---|---|---|"]

    def row(label, x, y, lower=True, fmt=str):
        L.append(f"| {label} | {fmt(x) if x is not None else '—'} | {fmt(y) if y is not None else '—'} | {_cmp(x, y, lower)} |")
    row("Student's wait per turn, median (s)", A["wait_median_s"], B["wait_median_s"])
    row("Wait, slowest 10% (s)", A["wait_p90_s"], B["wait_p90_s"])
    row("Reply length, average characters", A["reply_chars_avg"], B["reply_chars_avg"])
    row("Spoken characters per turn (voice cost)", A["spoken_chars_avg"], B["spoken_chars_avg"])
    row("Turns the math referees made him redo", A["retried_turns"], B["retried_turns"])
    row("Referee fires", sum(A["referee"].values()), sum(B["referee"].values()))
    row("Apologies (no answer)", A["fallbacks"], B["fallbacks"])
    if r.get("critic"):
        row("Teaching findings, HIGH", A["findings"]["high"], B["findings"]["high"])
        row("Teaching findings, all", sum(A["findings"].values()), sum(B["findings"].values()))
    row("Dollars per turn (AI only)", A["usd_per_turn"], B["usd_per_turn"], True, lambda v: f"${v:.4f}")
    L += ["", "**How to read it.** Lower is better on every row. One trial is a handful of lessons,",
          "so a small difference is noise; look for rows where one model is clearly ahead, and run it",
          "again if a deciding row is close. Switching is one Render setting (`CLAUDE_MODEL`).", ""]
    for name, X in ((a, A), (b, B)):
        if X["errors"]:
            L.append(f"**{name} did not finish:** " + "; ".join(X["errors"]))
        L.append(f"**{name}** referee detail: {json.dumps(X['referee'])} · priced as {X['priced_as']}")
    L += ["", "## First replies, side by side (the opening turn of the first lessons)", ""]
    for (ia, ta), (ib, tb) in zip(A["samples"], B["samples"]):
        L += [f"**{ia}** — A: {ta}", "", f"**{ib}** — B: {tb}", ""]
    return "\n".join(L) + "\n"


def write_report(data_dir, r: dict) -> str:
    d = os.path.join(str(data_dir), REPORT_DIR_NAME)
    os.makedirs(d, exist_ok=True)
    name = "trial-" + time.strftime("%Y%m%d-%H%M%S", time.gmtime()) + ".md"
    with open(os.path.join(d, name), "w", encoding="utf-8") as fh:
        fh.write(report_markdown(r))
    with open(os.path.join(d, name[:-3] + ".json"), "w", encoding="utf-8") as fh:
        slim = dict(r)
        slim["arm"] = {k: {kk: vv for kk, vv in v.items() if kk != "samples"} for k, v in r.get("arm", {}).items()}
        json.dump(slim, fh, default=str)
    return name


def list_reports(data_dir) -> list:
    d = os.path.join(str(data_dir), REPORT_DIR_NAME)
    if not os.path.isdir(d):
        return []
    return sorted((f for f in os.listdir(d) if f.endswith(".md")), reverse=True)[:20]


def read_report(data_dir, name: str) -> str:
    if not name or "/" in name or "\\" in name or not name.endswith(".md"):
        return ""
    p = os.path.join(str(data_dir), REPORT_DIR_NAME, name)
    return open(p, encoding="utf-8").read() if os.path.exists(p) else ""

# I did no harm and this file is not truncated.

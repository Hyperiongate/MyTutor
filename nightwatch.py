# =============================================================================
# nightwatch.py  --  THE GOVERNOR  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-08-17  BUILD ha -- THE MORNING REPORT READS THE TELEMETRY. A new section in
#               report_markdown reads store.event_stats(7) (the system_events table
#               build ha added): referee crashes, browser errors, replies shipped with
#               a known finding, fail-opens -- with the named offenders. The governor
#               now sees the same health counters /admin does, so a dead check reaches
#               Jim's inbox instead of waiting to be noticed. Fully wrapped: no store,
#               no section, never a failed report.
#   2026-08-16  NEW -- BUILD go. Jim, after a day in which every defect we fixed had been
#               found by him personally, clicking through a lesson:
#
#                 "I believe in the world of AI, only AI is gonna be capable of governing
#                  AI... depending on me to fix it or notice problems is only going to
#                  address some of those problems and probably just the big ones. I need
#                  you to set up a system but you are able to catch the things that I
#                  cannot catch."
#
#               He is right, and the gap is precise. EVERYTHING WE OWN IS A RATCHET, NOT A
#               DETECTOR. All fourteen referees exist because a human found the defect
#               first: rule 41 from an audit, rule 43 from Jim, rule 63(d) from Jim, rule
#               0's recap clause from Jim. ruletests' ~3,900 checks are ~3,900 things
#               somebody already thought of. That machinery makes a defect permanent-proof
#               once found -- it converts Jim's attention into a guarantee -- but it can
#               never surprise us, and a tutor's worst failures are quiet ones: a word used
#               before it was taught, a question answered before the child could try.
#
#               `lessonaudit.py` was already the right idea (AI marking AI) and it runs a
#               few times a month, because it needs a key and a person to start it. THE
#               MISSING PIECE IS NOT INTELLIGENCE, IT IS CADENCE. This file is the cadence.
#
#               It rides the heartbeat thread that already carries the weekly digests and
#               the nightly database snapshot (main.py `_digest_loop`), so there is NO new
#               Render service and nothing for Jim to configure: he pushes, and it runs.
#               (The blueprint in render.yaml is documentation only -- production was made
#               by hand and is not attached to it -- which is exactly why a background pass
#               beats a Cron Job service here.)
#
#               FOUR DESIGN RULES, each paid for by an earlier build:
#
#               1. AN AUDIT FINDING IS AN OPINION (build fe). Every finding the critic
#                  raises is handed to a SECOND, independent pass whose only job is to
#                  REFUTE it, and it is told to default to "refuted" when unsure. Only
#                  survivors are ever shown. In the 2026-08-16 triage 3 of 19 findings were
#                  weak and 2 were understated -- a governor that cries wolf trains Jim to
#                  ignore it, and then it is worse than nothing.
#
#               2. ONLY WHAT IS NEW. A ledger fingerprints every confirmed finding, so a
#                  defect already reported is COUNTED, not re-reported. The failure mode
#                  of every monitoring system ever built is a nightly email nobody opens.
#
#               3. IT NEVER TOUCHES A LESSON. It runs against the audit student, in its own
#                  thread, wrapped so that any failure at all leaves the app untouched. A
#                  governor that can break the thing it governs is not a governor.
#
#               4. IT SAYS WHAT IT DID NOT DO. Every report names the scenarios it skipped,
#                  the budget it stopped at, and the findings it could not verify. A silent
#                  cap reads as "all clear" (the no-silent-caps rule).
#
#               ⚠️ HONEST LIMIT, stated here so nobody assumes otherwise: this drives
#               `tutor.get_tutor_reply` directly, exactly as lessonaudit does, so the
#               fourteen referees DO run (they live inside `_create_verified`) but main.py's
#               server-side probes and gates do NOT -- they live in the chat endpoint. The
#               probe hooks below are how main.py lends them to this pass; anything not
#               passed in simply does not run here, and the report says so.
# =============================================================================

from __future__ import annotations

import hashlib
import json
import os
import re
import time
import traceback
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))

# ---- BUDGET (Jim's call, 2026-08-16: "a few dollars a night") ----------------
# 12 lessons x 6 turns is roughly 72 teaching turns, plus each lesson's student turns
# and one critic pass, plus a verification call per finding. lessonaudit prices a
# teaching turn at ~$0.03 (mostly cached prompt), so a night lands in single dollars.
# Every one of these is overridable in Render without a deploy.
LESSONS_PER_NIGHT = int(os.environ.get("NIGHTWATCH_LESSONS", "12") or 12)
TURNS_PER_LESSON  = int(os.environ.get("NIGHTWATCH_TURNS", "6") or 6)
MAX_MINUTES       = int(os.environ.get("NIGHTWATCH_MAX_MINUTES", "45") or 45)
RUN_HOUR_UTC      = int(os.environ.get("NIGHTWATCH_HOUR_UTC", "8") or 8)   # ~1am Pacific
VERIFY_FINDINGS   = (os.environ.get("NIGHTWATCH_VERIFY", "on").strip().lower()
                     not in ("off", "0", "false", "no"))
LEDGER_NAME       = "nightwatch_ledger.json"
REPORT_DIR_NAME   = "nightwatch"
KEEP_REPORTS      = int(os.environ.get("NIGHTWATCH_KEEP", "30") or 30)


def enabled() -> bool:
    return os.environ.get("NIGHTWATCH", "on").strip().lower() not in ("off", "0", "false", "no")


# =============================================================================
# PART 1 -- THE LEDGER: what we have already told Jim
# =============================================================================
# The fingerprint deliberately does NOT include the critic's prose, which varies run to
# run for the same defect. It is the scenario, the rule, and the tutor's own words -- the
# three things that are stable when the same defect recurs.
_WS = re.compile(r"\s+")


def fingerprint(scenario_id: str, finding: dict) -> str:
    quote = _WS.sub(" ", str(finding.get("quote") or "")).strip().lower()[:180]
    rule = str(finding.get("rule") if finding.get("rule") is not None else "-")
    raw = f"{scenario_id}|{rule}|{quote}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]


def load_ledger(data_dir) -> dict:
    path = os.path.join(str(data_dir), LEDGER_NAME)
    try:
        with open(path, "r", encoding="utf-8") as fh:
            led = json.load(fh)
        return led if isinstance(led, dict) else {}
    except FileNotFoundError:
        return {}
    except Exception as exc:  # noqa: BLE001 -- a corrupt ledger must not stop the watch
        print(f"[nightwatch] ledger unreadable ({exc}) -- starting a fresh one")
        return {}


def save_ledger(data_dir, ledger: dict) -> None:
    path = os.path.join(str(data_dir), LEDGER_NAME)
    try:
        tmp = path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as fh:
            json.dump(ledger, fh, indent=1, sort_keys=True)
        os.replace(tmp, path)
    except Exception as exc:  # noqa: BLE001
        print(f"[nightwatch] could not save the ledger: {exc}")


# =============================================================================
# PART 2 -- THE ROTATION: cover everything, a little at a time
# =============================================================================
# A small budget cannot run every scenario every night, so it rotates -- and the rotation
# is DETERMINISTIC on the day number rather than random, so "has this been covered?" is a
# question with an answer. With 10 scenarios and 12 slots, every scenario runs at least
# once a night at the default budget; at a smaller budget the offset walks forward so
# nothing is starved.
def pick_tonight(scenarios, count, day_index):
    if not scenarios:
        return []
    n = len(scenarios)
    count = max(1, min(int(count or 1), 200))
    start = (day_index * count) % n
    return [scenarios[(start + i) % n] for i in range(count)]


def day_index(now=None) -> int:
    now = now or datetime.now(timezone.utc)
    return int(now.timestamp() // 86400)


# =============================================================================
# PART 3 -- ADVERSARIAL VERIFICATION: an audit finding is an opinion (build fe)
# =============================================================================
VERIFY_SYSTEM = """\
You are a skeptical reviewer of AUDIT FINDINGS about a maths tutor for children. You are
not reviewing the tutor. You are reviewing the CRITIC, and your default position is that
the critic is wrong.

Given a transcript and one finding, decide whether the finding is REAL.

Refute the finding if ANY of these hold:
- the quoted words are not actually in the transcript, or are quoted misleadingly
- the maths is correct under standard conventions, however surprising it looks
- the "problem" is a decided design of this product: the check-in wording
  "...or should I show it a different way?" is REQUIRED, not a defect; a student may
  choose to move past an unfinished unit; foundation-first teaching (explaining before
  asking) is deliberate and is NOT "lecturing"; the tutor accepting a right answer before
  extending it is rule 59 working
- the finding is a matter of taste, tone or pacing rather than something a child would
  learn WRONG or be unable to follow
- the finding restates something the transcript itself later corrects

Confirm it ONLY if a specific child, reading these specific words, would learn something
false or be unable to follow. When you are unsure, REFUTE.

Return STRICT JSON only: {"real": true|false, "why": "<one sentence>"}
"""


def verify_finding(openai_call, scenario, transcript, finding):
    """Hand one finding to an independent skeptic. Returns (is_real, why, error)."""
    body = "\n\n".join(f"{'TUTOR' if r == 'assistant' else 'STUDENT'}: {t}"
                       for r, t in transcript)
    msgs = [{"role": "system", "content": VERIFY_SYSTEM},
            {"role": "user", "content":
                f"TRANSCRIPT (course: {scenario.get('course')}):\n\n{body[:24000]}\n\n"
                f"=====\n\nTHE FINDING TO REVIEW:\n"
                f"severity: {finding.get('severity')}\n"
                f"rule: {finding.get('rule')}\n"
                f"what: {finding.get('what')}\n"
                f"quote: {finding.get('quote')}\n"
                f"why: {finding.get('why')}"}]
    text, err = openai_call(msgs, max_tokens=400, want_json=True)
    if err:
        return None, "", err          # None = COULD NOT VERIFY, never silently confirmed
    try:
        data = json.loads(text)
    except Exception:  # noqa: BLE001
        s, e = (text or "").find("{"), (text or "").rfind("}")
        try:
            data = json.loads(text[s:e + 1])
        except Exception:  # noqa: BLE001
            return None, "", f"verifier did not return JSON: {(text or '')[:160]}"
    return bool(data.get("real")), str(data.get("why") or ""), None


# =============================================================================
# PART 4 -- THE NIGHT
# =============================================================================
def run_night(data_dir, lessons=None, turns=None, probe_hooks=None, now=None):
    """Run one night's governance pass. Returns a result dict; never raises.

    probe_hooks -- optional {name: callable(scenario, transcript)} lent by main.py, so
    the server-side probes ([termgap] and friends) can see these lessons even though this
    harness calls the tutor directly. Anything not passed in does not run, and the report
    says so rather than implying coverage we do not have."""
    started = time.time()
    out = {"ok": False, "ran": 0, "skipped": [], "new": [], "recurring": 0,
           "unverified": [], "refuted": 0, "refuted_list": [], "errors": [], "seconds": 0.0,
           "budget_stopped": False, "probes_run": sorted((probe_hooks or {}).keys())}
    try:
        import lessonaudit
    except Exception as exc:  # noqa: BLE001
        out["errors"].append(f"lessonaudit unavailable: {exc}")
        return out

    lessons = int(lessons or LESSONS_PER_NIGHT)
    turns = int(turns or TURNS_PER_LESSON)
    ok, note = lessonaudit.preflight()
    if not ok:
        out["errors"].append(f"preflight failed, nothing was run: {note}")
        return out

    ledger = load_ledger(data_dir)
    picked = pick_tonight(lessonaudit.SCENARIOS, lessons, day_index(now))
    deadline = started + MAX_MINUTES * 60

    for sc in picked:
        if time.time() > deadline:
            out["budget_stopped"] = True
            out["skipped"].append(f"{sc['id']} (time budget of {MAX_MINUTES} min reached)")
            continue
        try:
            transcript, err, fallbacks = lessonaudit.run_scenario(sc, turns)
            if err:
                out["errors"].append(f"{sc['id']}: {err}")
                continue
            out["ran"] += 1
            if fallbacks:
                # A graceful-failure turn is a RELIABILITY finding the critic cannot
                # argue away (build dc's lesson: a critic marking content reads straight
                # past absence).
                _record(out, ledger, sc, {
                    "severity": "medium", "rule": None,
                    "what": f"the tutor lost its train of thought {fallbacks} time(s) in "
                            f"one lesson and apologised to the student",
                    "quote": "(fallback turn)", "why": "a child is left waiting mid-lesson",
                    "fix": "check the Anthropic call path and the turn deadline"},
                    verified_note="counted by code, not judged")

            for name, hook in (probe_hooks or {}).items():
                try:
                    hook(sc, transcript)
                except Exception as exc:  # noqa: BLE001 -- a probe never breaks the watch
                    out["errors"].append(f"probe {name} on {sc['id']}: {exc}")

            findings, cerr = lessonaudit.critique(sc, transcript)
            if cerr:
                out["errors"].append(f"{sc['id']} critic: {cerr}")
                continue
            for f in (findings or {}).get("findings", []) or []:
                if not VERIFY_FINDINGS:
                    _record(out, ledger, sc, f, verified_note="verification disabled")
                    continue
                real, why, verr = verify_finding(lessonaudit._openai, sc, transcript, f)
                if verr:
                    out["unverified"].append({"scenario": sc["id"],
                                              "what": f.get("what"), "error": verr})
                elif real:
                    _record(out, ledger, sc, f, verified_note=why)
                else:
                    # 2026-08-17 (build gp): RECORD WHAT WAS THROWN AWAY, not just how
                    # much. The first real night refuted 16 of 22 findings, and a bare
                    # count cannot be audited -- 73% looks identical whether it is healthy
                    # skepticism or a reviewer that has started killing real defects. The
                    # refuted list is what makes the health metric falsifiable. It is in
                    # the report and NEVER in the email: this is calibration material, not
                    # something to wake Jim for.
                    out["refuted"] += 1
                    out["refuted_list"].append({"scenario": sc["id"],
                                                "severity": f.get("severity"),
                                                "rule": f.get("rule"),
                                                "what": f.get("what"),
                                                "reviewer": why})
        except Exception as exc:  # noqa: BLE001 -- one bad lesson never ends the night
            out["errors"].append(f"{sc['id']}: {type(exc).__name__}: {exc}")
            print(f"[nightwatch] {sc['id']} crashed: {traceback.format_exc()[:800]}")

    save_ledger(data_dir, ledger)
    out["seconds"] = round(time.time() - started, 1)
    out["ok"] = True
    return out


def _record(out, ledger, sc, finding, verified_note=""):
    """Confirmed finding -> the ledger. New ones are reported; repeats are counted."""
    fp = fingerprint(sc["id"], finding)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    if fp in ledger:
        ledger[fp]["seen"] = int(ledger[fp].get("seen", 1)) + 1
        ledger[fp]["last"] = stamp
        out["recurring"] += 1
        return
    ledger[fp] = {"first": stamp, "last": stamp, "seen": 1,
                  "scenario": sc["id"], "course": sc.get("course"),
                  "rule": finding.get("rule"), "what": finding.get("what"),
                  "quote": (finding.get("quote") or "")[:400]}
    out["new"].append({"fp": fp, "scenario": sc["id"], "course": sc.get("course"),
                       "severity": finding.get("severity"), "rule": finding.get("rule"),
                       "what": finding.get("what"), "quote": finding.get("quote"),
                       "why": finding.get("why"), "fix": finding.get("fix"),
                       "verified": verified_note})


# =============================================================================
# PART 5 -- THE REPORT
# =============================================================================
_SEV = {"high": 0, "medium": 1, "low": 2}


def report_markdown(result, build="") -> str:
    new = sorted(result.get("new", []),
                 key=lambda f: _SEV.get(str(f.get("severity")).lower(), 3))
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    L = [f"# Night watch — {stamp}" + (f"  (build {build})" if build else ""), "",
         f"{result.get('ran', 0)} lessons run · **{len(new)} new confirmed** · "
         f"{result.get('recurring', 0)} already known · {result.get('refuted', 0)} refuted "
         f"on review · {result.get('seconds', 0)}s", ""]
    if not result.get("ok"):
        L += ["**The watch did not complete.**", ""]
    if new:
        L += ["## New, and each survived an independent challenge", ""]
        for f in new:
            L += [f"### {str(f.get('severity','?')).upper()} — {f.get('scenario')} "
                  f"({f.get('course')})" + (f" — rule {f['rule']}" if f.get("rule") else ""),
                  "", f"**{f.get('what')}**", "",
                  f"> {f.get('quote')}", "",
                  f"Why it matters: {f.get('why')}", "",
                  f"Suggested fix: {f.get('fix')}", ""]
            if f.get("verified"):
                L += [f"_Reviewer: {f['verified']}_", ""]
    else:
        L += ["No new confirmed findings tonight.", ""]

    # WHAT THE REVIEWER THREW AWAY. This section is how the reviewer gets audited: if a
    # dismissal here reads wrong to a human, the reviewer prompt is the thing to fix, not
    # the critic. Without it the refute rate is a number with nothing behind it.
    thrown = result.get("refuted_list") or []
    if thrown:
        L += [f"## What the reviewer threw away ({len(thrown)})", "",
              "_Read a few of these. If any of them look like REAL defects, the reviewer is "
              "too aggressive and the refute rate is hiding things._", ""]
        for t in thrown:
            L += [f"- **{t.get('scenario')}**"
                  + (f" (rule {t['rule']})" if t.get("rule") else "")
                  + f" — {t.get('what')}",
                  f"  - reviewer: _{t.get('reviewer') or '(no reason given)'}_"]
        L += [""]

    # THE WEEK'S TELEMETRY (build ha -- EYES). The governor reads the same
    # system_events table /admin does, so a crashed referee or a browser error spike
    # arrives in the morning report instead of waiting for someone to open a dashboard.
    # Wrapped completely: a watch with no store access still writes its report.
    try:
        import store as _store
        ev = _store.event_stats(7)
        counts = ev.get("counts") or {}
        def _tot(kind):
            return sum((counts.get(kind) or {}).values())
        crashes, cerr = _tot("referee_crash"), _tot("clienterror")
        passed, fails = _tot("pass_through"), _tot("failopen")
        L += ["## The week's telemetry (system_events, 7 days)", "",
              f"- referee crashes: **{crashes}**" + (" ← should be zero" if crashes else ""),
              f"- browser errors reported: **{cerr}**" + (" ← should be zero" if cerr else ""),
              f"- replies shipped WITH a known finding: **{passed}**"
              + (" ← should be zero" if passed else ""),
              f"- teaching-path fail-opens (friendly-message turns): **{fails}**",
              f"- referee fires: {_tot('referee_fire')} · probe observations: "
              f"{_tot('probe')} · prompt-size events: {_tot('promptsize')}", ""]
        alarm = []
        for kind in ("referee_crash", "clienterror", "pass_through"):
            for nm, n in sorted((counts.get(kind) or {}).items(), key=lambda kv: -kv[1])[:5]:
                alarm.append(f"  - {kind} · {nm}: {n}×")
        if alarm:
            L += ["  The named offenders:"] + alarm + [""]
    except Exception as _exc:  # noqa: BLE001
        L += ["## The week's telemetry", "", f"- (unavailable: {_exc})", ""]

    # WHAT WE DID NOT DO. A silent cap reads as "all clear".
    L += ["## What this run did not cover", ""]
    probes = result.get("probes_run") or []
    L += [f"- probes run against these lessons: {', '.join(probes) if probes else 'none'}",
          "- the server-side chat endpoint (gates, tracking) is not exercised: this "
          "harness calls the tutor directly",
          "- the rendered SCREEN is not judged here (that is screencheck.py, which runs "
          "in ruletests on every push)"]
    for s in result.get("skipped", []):
        L += [f"- SKIPPED: {s}"]
    if result.get("budget_stopped"):
        L += [f"- **the time budget stopped this run early** ({MAX_MINUTES} min)"]
    for u in result.get("unverified", []):
        L += [f"- COULD NOT VERIFY (not counted either way): {u.get('what')} "
              f"— {u.get('error')}"]
    for e in result.get("errors", []):
        L += [f"- ERROR: {e}"]
    L += ["", "*I did no harm and this file is not truncated.*", ""]
    return "\n".join(L)


def email_digest(result, build="") -> "tuple[str, str] | None":
    """(subject, body) when there is something worth waking Jim for, else None.
    Silence is the default: a nightly email that usually says nothing is a nightly
    email nobody opens, and then the one that matters is missed too."""
    new = result.get("new") or []
    hard_errors = [e for e in (result.get("errors") or []) if "preflight" in e.lower()]
    if not new and not hard_errors:
        return None
    high = sum(1 for f in new if str(f.get("severity")).lower() == "high")
    subject = (f"{len(new)} new teaching finding(s)"
               + (f", {high} HIGH" if high else "")) if new else "night watch could not run"
    return subject, report_markdown(result, build)


def write_report(data_dir, result, build="") -> str:
    """Write tonight's report and prune old ones. Returns the path, or ""."""
    try:
        d = os.path.join(str(data_dir), REPORT_DIR_NAME)
        os.makedirs(d, exist_ok=True)
        name = datetime.now(timezone.utc).strftime("%Y-%m-%d") + ".md"
        path = os.path.join(d, name)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(report_markdown(result, build))
        files = sorted(f for f in os.listdir(d) if f.endswith(".md"))
        for stale in files[:-KEEP_REPORTS] if len(files) > KEEP_REPORTS else []:
            try:
                os.remove(os.path.join(d, stale))
            except OSError:
                pass
        return path
    except Exception as exc:  # noqa: BLE001
        print(f"[nightwatch] could not write the report: {exc}")
        return ""


# =============================================================================
# PART 6 -- THE PASS (called from main.py's heartbeat)
# =============================================================================
# Restart-safe the same way the nightly snapshot is (build dj): it asks the DISK what day
# it last ran, not a variable in memory, so a redeploy at 3am cannot skip a night or run
# two in a row.
def last_run_day(data_dir) -> str:
    try:
        d = os.path.join(str(data_dir), REPORT_DIR_NAME)
        files = sorted(f for f in os.listdir(d) if f.endswith(".md"))
        return files[-1][:-3] if files else ""
    except Exception:  # noqa: BLE001
        return ""


def due(data_dir, now=None) -> bool:
    now = now or datetime.now(timezone.utc)
    if now.hour < RUN_HOUR_UTC:
        return False
    return last_run_day(data_dir) != now.strftime("%Y-%m-%d")

# =============================================================================
# PART 7 -- THE FACE (2026-08-17, build gp)
# =============================================================================
# Written the morning after go shipped, because go had a hole in it: the watch wrote its
# findings to a markdown file on Render's persistent disk and NOTHING EXPOSED IT. The log
# carried a one-line count; the actual findings -- the whole product of the run -- were
# unreadable without shell access Jim does not have.
#
# A GOVERNOR WHOSE REPORTS ARE HARD TO REACH IS A GOVERNOR THAT GETS IGNORED, which is the
# exact failure mode go's own header warns about. Twelve hours is a short time to prove
# your own warning right.
def summary(data_dir) -> dict:
    """Everything the /admin card needs. Never raises."""
    out = {"ok": True, "enabled": enabled(), "hour_utc": RUN_HOUR_UTC,
           "lessons": LESSONS_PER_NIGHT, "turns": TURNS_PER_LESSON,
           "verify": VERIFY_FINDINGS, "reports": [], "last": "", "open_findings": 0,
           "recurring_worst": [], "health": None, "note": "",
           "max_minutes": MAX_MINUTES, "last_minutes": None, "near_ceiling": False}
    try:
        d = os.path.join(str(data_dir), REPORT_DIR_NAME)
        names = sorted((f[:-3] for f in os.listdir(d) if f.endswith(".md")), reverse=True)
        out["reports"] = names[:KEEP_REPORTS]
        out["last"] = names[0] if names else ""
    except Exception:  # noqa: BLE001 -- no reports yet is a normal state, not an error
        pass
    try:
        led = load_ledger(data_dir)
        out["open_findings"] = len(led)
        # The findings that keep coming back are the ones worth Jim's morning: a defect
        # seen eight nights running is not a fluke and is not being fixed.
        worst = sorted(led.values(), key=lambda v: -int(v.get("seen", 1)))[:5]
        out["recurring_worst"] = [{"seen": v.get("seen"), "scenario": v.get("scenario"),
                                  "rule": v.get("rule"), "what": v.get("what"),
                                  "first": v.get("first"), "last": v.get("last")}
                                  for v in worst if int(v.get("seen", 1)) > 1]
    except Exception as exc:  # noqa: BLE001
        out["note"] = f"ledger unreadable: {exc}"
    # THE HEALTH METRIC. Jim's own instruction for week one: judge the watch by what it
    # THROWS AWAY. Refutes nothing -> the reviewer is too soft and the reports will bloat.
    # Refutes everything -> the critic or the reviewer is miscalibrated. It is parsed back
    # out of last night's report rather than stored twice, so it can never disagree with it.
    try:
        text = read_report(data_dir, out["last"]) if out["last"] else ""
        mt = re.search(r"\u00b7 ([\d.]+)s\s*$", text, re.M)
        if mt:
            out["last_minutes"] = round(float(mt.group(1)) / 60.0, 1)
            # A run that is already using most of its window will start truncating the
            # rotation as findings accumulate, and losing coverage quietly is the one
            # thing this system must not do.
            out["near_ceiling"] = out["last_minutes"] >= 0.8 * MAX_MINUTES
        m = re.search(r"\*\*(\d+) new confirmed\*\* .* (\d+) refuted", text)
        if m:
            new, refuted = int(m.group(1)), int(m.group(2))
            total = new + refuted
            out["health"] = {"new": new, "refuted": refuted,
                             "refuted_pct": round(100.0 * refuted / total) if total else None}
    except Exception:  # noqa: BLE001
        pass
    return out


def read_report(data_dir, date_name: str) -> str:
    """One night's report by its YYYY-MM-DD name. Returns "" if there is no such report.
    The name is validated as a date, so this can never read outside the report folder."""
    try:
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(date_name or "")):
            return ""
        path = os.path.join(str(data_dir), REPORT_DIR_NAME, f"{date_name}.md")
        with open(path, "r", encoding="utf-8") as fh:
            return fh.read()
    except Exception:  # noqa: BLE001
        return ""


# I did no harm and this file is not truncated.

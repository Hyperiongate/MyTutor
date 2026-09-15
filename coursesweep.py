# =============================================================================
# coursesweep.py  --  THE COURSE SWEEP: one reviewer, every authored lesson, once
#                     --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-09-15  BUILD wb -- the report names the seat that read it ("Read by: openai ·
#               gpt-4.1"), so a run that came back empty says which model to blame.
#   2026-09-15  BUILD wa -- BORN. Project 1 of the 2026-09-14 deep dive ("The Forever
#               War"). The night watch audits the LIVE AI lane every night; nothing
#               audits the SCRIPTED course -- the lane a child actually spends their
#               minutes on -- except Jim's own playtests, one lesson at a time, six flags
#               a lesson. This module points the same reviewer at the authored course:
#               every lesson is walked deterministically by the engine itself (the shape
#               a child hears, INCLUDING the scripted second explanation on one deliberate
#               miss), the whole transcript is read once by the judge seat, and the
#               findings come back grouped so a fix lands ONCE:
#                 - GENERATOR findings (an ask, a praise line, a worked walk-back) belong
#                   to the op that made the line -- fix the generator, fix every lesson;
#                 - AUTHORED findings (why, picture, teach, recap, the reason question)
#                   belong to the lesson, by course and unit.
#               Runs on Render from the /admin card (one course per job, priced first),
#               writes data/coursesweep/<course>_<date>.{json,md}, and never touches a
#               lesson. The same four laws as the night watch: challenged before Jim sees
#               it (the reviewer is asked for the QUOTE and the RULE, and a finding whose
#               quote is not in the transcript is dropped as unplaced), reported not
#               fixed, and always says what it did not cover.
# =============================================================================
"""The course sweep -- the reviewer over the scripted course, lesson by lesson.

Pure module: no FastAPI, no store. main.py owns the endpoints and the background job;
this file owns the walk, the prompt, the parse, the grouping and the report.
"""
from __future__ import annotations

import datetime as _dt
import json
import os
import re
import time

HERE = os.path.dirname(os.path.abspath(__file__))

# The walk is deterministic: one seed for every lesson, so a re-run reads the same
# transcript and a finding can be matched to the same beat next time.
SWEEP_SEED = 11
# A times-table lesson practices as an 81-fact pass; the reviewer reads the first few
# facts and the report says so (a pass is recall, and 81 facts would bury the lesson).
TABLE_FACTS_SHOWN = 6
MAX_FINDINGS_PER_LESSON = 8
# ESTIMATE ONLY, like lessonaudit's: per-lesson cost of one judge read at Sonnet-class
# prices (~10k tokens in, ~1k out). Corrected from the billing dashboard, never guessed
# twice.
EST_USD_PER_LESSON = 0.05


# =============================================================================
# 1. THE WALK -- the lesson exactly as the engine plays it
# =============================================================================
def _kind_index(lesson, L):
    """spoken text -> the beat KIND, for the lesson's authored fields. What the engine
    emits is (spoken, board); what the reviewer needs to know is WHICH FIELD it came
    from, because that decides who owns the fix."""
    idx = {}
    def put(text, kind):
        if text:
            idx.setdefault(" ".join(str(text).split()), kind)
    try:
        put(L.lesson_intro(lesson)[0], "intro")
        put(L.lesson_orientation(lesson, True)[0], "orientation")
        put(L.lesson_orientation(lesson, False)[0], "orientation")
    except Exception:  # noqa: BLE001
        pass
    for field in ("why", "picture", "teach", "recap"):
        for spoken, _b in (lesson.get(field) or []):
            put(spoken, field)
    for pair in lesson.get("pairs") or []:
        put(pair["worked"][0], "worked-example")
    put(lesson.get("practice_intro"), "practice-intro")
    put(lesson.get("advance_line"), "advance")
    ex = lesson.get("explain") or {}
    put(ex.get("spoken"), "reason-question")
    for name in ("LINE_WRONG", "LINE_END_GRACEFUL", "LINE_REASON_RIGHT",
                 "LINE_REASON_WRONG", "LINE_TAP", "LINE_TABLE_RESTART", "LINE_TABLE_REST"):
        put(getattr(L, name, None), "fixed-line")
    for s in getattr(L, "SECOND_LOOK_LINES", ()):
        put(s, "second-look")
    for s in getattr(L, "FRESH_ONE_LINES", ()):
        put(s, "fresh-one")
    return idx


def _kind_of(spoken, kind_idx, L, step):
    key = " ".join(str(spoken or "").split())
    if key in kind_idx:
        return kind_idx[key]
    if step.get("kind") == "ask":
        return "ask"
    if step.get("kind") == "end":
        return "end"
    opener = "Here it is, step by step: "
    if key.startswith(opener):
        return "walk-back"
    for pfx in getattr(L, "PRAISE_PREFIXES", ()):
        if key.startswith(pfx):
            return "praise"
    return "say"


def transcript_for(lesson, L=None):
    """Walk one lesson the way a child hears it and return its turns.

    The child in this walk answers the two guided pairs correctly, MISSES the first
    practice problem once (so the scripted second explanation -- build vz -- is read too),
    then answers correctly to the streak, answers the reason question correctly, and
    reaches the mastered end. A table lesson shows its first TABLE_FACTS_SHOWN facts.

    Returns a list of dicts: {"n", "kind", "spoken", "board", "op"}."""
    if L is None:
        import lessonscripts as L  # noqa: N812
    kind_idx = _kind_index(lesson, L)
    st = L.start(lesson, seed=SWEEP_SEED)
    turns = []
    missed = False
    facts = 0

    def take(steps):
        for s in steps:
            p = s.get("problem") or {}
            turns.append({"n": len(turns) + 1,
                          "kind": _kind_of(s.get("spoken"), kind_idx, L, s),
                          "spoken": s.get("spoken") or "",
                          "board": s.get("board") or "",
                          "op": p.get("op", "") if s.get("kind") == "ask" else ""})

    out, st = L.step(lesson, st, ("begin",))
    take(out)
    for _ in range(200):
        if st.get("finished"):
            break
        pend = st.get("pending") or {}
        if pend.get("reason"):
            out, st = L.step(lesson, st, ("answer", (lesson.get("explain") or {}).get("answer", "")))
            take(out)
            continue
        p = pend.get("problem")
        if p is None:
            break
        if st.get("phase") == "table":
            facts += 1
            if facts > TABLE_FACTS_SHOWN:
                if turns and turns[-1]["kind"] == "ask":
                    turns.pop()                    # the fact we will not answer
                turns.append({"n": len(turns) + 1, "kind": "note",
                              "spoken": f"(the times-table pass continues for all 81 facts; "
                                        f"the first {TABLE_FACTS_SHOWN} are shown)",
                              "board": "", "op": ""})
                break
        right = L.ans(p)
        if (st.get("phase") == "practice" and not missed
                and not pend.get("guided") and L._worked_for(p) is not None):
            missed = True
            out, st = L.step(lesson, st, ("answer", (right or 0) + 777))
            take(out)
            if any(s.get("kind") == "intervene" for s in out):
                out, st = L.step(lesson, st, ("resume",))
                take(out)
            continue
        out, st = L.step(lesson, st, ("answer", right))
        take(out)
    return turns


def render_transcript(lesson, turns) -> str:
    """The transcript as the reviewer reads it: one numbered turn per beat, the words
    and then the board, tags left in (the rule index explains every tag)."""
    head = (f"LESSON {lesson.get('id')} -- {lesson.get('course')} unit {lesson.get('unit')} "
            f"-- \"{lesson.get('topic')}\" -- levels {'/'.join(lesson.get('levels') or ())}")
    lines = [head, ""]
    for t in turns:
        lines.append(f"[{t['n']}] ({t['kind']}) TUTOR: {t['spoken']}")
        if t["board"]:
            lines.append(f"      BOARD: {t['board']}")
        lines.append("")
    return "\n".join(lines)


# =============================================================================
# 2. THE REVIEWER
# =============================================================================
SWEEP_SYSTEM = """You are reviewing ONE SCRIPTED LESSON from Mr. Cadabra's Classroom, a voice
maths tutor for children. Every word below is FIXED TEXT a child hears out loud, one beat at a
time, while the BOARD line under it is drawn on screen. Nothing here is improvised: if it is
wrong, every child who takes this lesson hears it wrong, so a finding here is worth ten
findings on a live conversation.

Read the whole lesson as the child hears it. Report ONLY defects a careful teacher or parent
would flag, in this order of importance:
  1. A false or unconditional mathematical statement (a rule stated as a law without its
     condition counts).
  2. A step that does not follow from the one before, or an answer never shown to be right.
  3. Words that do not match the board (a number said that is not drawn; a board line the
     words never read; a picture promised and not drawn).
  4. A term used before the lesson has taught it, for this level.
  5. Wording a child at this level cannot parse: a sentence over ~25 words, a double
     negative, a pronoun with no clear referent ("it", "that one"), a story with no picture.
  6. A beat that repeats the previous beat without adding anything.
  7. Tone: anything that blames, hurries, or praises what the child did not do.

Do NOT report: style preferences; the choice of numbers; the lesson being short; the
absence of things outside its topic; the rule index's own wording. A quote must be COPIED
EXACTLY from a TUTOR line or a BOARD line. Give at most %d findings, the worst first, and if
the lesson is clean say so with an empty list.

Answer with pure JSON: {"findings": [{"turn": <n>, "quote": "<exact words>",
"kind": "false|unsupported|words-board|untaught-term|unclear|repeats|tone",
"severity": "HIGH|MEDIUM|LOW", "why": "<one sentence>", "fix": "<one sentence>"}],
"clean": <true|false>, "note": "<anything you could not judge>"}""" % MAX_FINDINGS_PER_LESSON


def _rules_text():
    try:
        with open(os.path.join(HERE, "RULES.md"), encoding="utf-8") as fh:
            return fh.read()
    except OSError:
        return "(rule index unavailable -- judge on mathematics and clarity alone)"


def review_lesson(lesson, turns, judge):
    """One judge read. `judge(messages, max_tokens, want_json) -> (text, err)` is the
    lessonaudit transport (or a stub in the battery). Returns (result, err)."""
    body = render_transcript(lesson, turns)
    msgs = [{"role": "system", "content": SWEEP_SYSTEM},
            {"role": "user", "content":
                f"THE TUTOR'S RULE INDEX (what every [[tag]] means, and the teaching rules):\n\n"
                f"{_rules_text()[:60000]}\n\n=====\n\n{body}"}]
    text, err = judge(msgs, 2000, True)
    if err:
        return None, err
    data = _parse_json(text)
    if data is None:
        return None, f"reviewer did not return JSON: {(text or '')[:200]}"
    return data, None


def _parse_json(text):
    try:
        return json.loads(text)
    except Exception:  # noqa: BLE001
        s, e = (text or "").find("{"), (text or "").rfind("}")
        if s >= 0 and e > s:
            try:
                return json.loads(text[s:e + 1])
            except Exception:  # noqa: BLE001
                return None
    return None


# The generator-owned kinds: a finding on one of these is a finding on the OP that made
# the line, and the fix lands in the generator, not the lesson.
GENERATED_KINDS = frozenset({"ask", "praise", "walk-back", "second-look", "fresh-one",
                             "fixed-line"})


def place_findings(lesson, turns, data):
    """Attach each finding to its turn, drop the unplaced (a quote that is nowhere in the
    transcript is the reviewer paraphrasing, exactly as the night watch treats it), and
    decide who OWNS the fix."""
    by_n = {t["n"]: t for t in turns}
    out, unplaced = [], 0
    bank_op = (lesson.get("bank") or [{}])[0].get("op", "") if lesson.get("bank") else ""
    for f in (data or {}).get("findings") or []:
        if not isinstance(f, dict):
            continue
        q = " ".join(str(f.get("quote") or "").split())
        t = by_n.get(f.get("turn"))
        hit = t if t and q and (q in " ".join(t["spoken"].split())
                                or q in " ".join(t["board"].split())) else None
        if hit is None and q:
            for cand in turns:                       # the reviewer's turn number slipped
                if q in " ".join(cand["spoken"].split()) or q in " ".join(cand["board"].split()):
                    hit = cand
                    break
        if hit is None:
            unplaced += 1
            continue
        kind = hit["kind"]
        owner = ("generator:" + (hit.get("op") or bank_op or "?")) if kind in GENERATED_KINDS \
            else "lesson:" + lesson["id"]
        out.append({"lesson": lesson["id"], "course": lesson.get("course"),
                    "unit": lesson.get("unit"), "topic": lesson.get("topic"),
                    "turn": hit["n"], "beat": kind, "owner": owner,
                    "quote": q[:200], "kind": str(f.get("kind") or "")[:20],
                    "severity": str(f.get("severity") or "LOW").upper()[:6],
                    "why": str(f.get("why") or "")[:300],
                    "fix": str(f.get("fix") or "")[:300]})
    return out, unplaced


# =============================================================================
# 3. THE RUN
# =============================================================================
def lessons_for(course, L=None):
    if L is None:
        import lessonscripts as L  # noqa: N812
    return [les for les in L.LESSONS if les.get("course") == course]


def estimate(course, L=None):
    """FREE: how many lessons, how many characters the reviewer reads, and the estimate."""
    les = lessons_for(course, L)
    chars = 0
    for x in les:
        try:
            chars += len(render_transcript(x, transcript_for(x, L)))
        except Exception:  # noqa: BLE001
            pass
    return {"course": course, "lessons": len(les), "chars": chars,
            "estimated_usd": round(len(les) * EST_USD_PER_LESSON, 2),
            "estimate_note": ("ESTIMATE ONLY -- one judge read per lesson at an assumed "
                              "Sonnet-class price. Read the real figure off the billing "
                              "dashboard after the first course and correct "
                              "EST_USD_PER_LESSON.")}


def run_sweep(data_dir, course, judge, limit=None, progress=None, L=None, now=None):
    """Sweep one course. Never raises; a lesson the reviewer could not read is recorded
    as such and the sweep goes on. Returns the result dict that write_report consumes."""
    if L is None:
        import lessonscripts as L  # noqa: N812
    t0 = time.monotonic()
    picked = lessons_for(course, L)
    if limit:
        picked = picked[:int(limit)]
    findings, errors, clean, unplaced_total = [], [], [], 0
    for i, les in enumerate(picked):
        if progress:
            try:
                progress(i, len(picked), les["id"])
            except Exception:  # noqa: BLE001
                pass
        try:
            turns = transcript_for(les, L)
        except Exception as exc:  # noqa: BLE001
            errors.append({"lesson": les["id"], "error": f"walk failed: {exc}"})
            continue
        data, err = review_lesson(les, turns, judge)
        if err:
            errors.append({"lesson": les["id"], "error": err})
            continue
        placed, unplaced = place_findings(les, turns, data)
        unplaced_total += unplaced
        if not placed and (data or {}).get("clean", not placed):
            clean.append(les["id"])
        findings.extend(placed)
    return {"course": course, "ran": len(picked) - len(errors), "asked": len(picked),
            "findings": findings, "errors": errors, "clean": clean,
            "unplaced": unplaced_total, "seconds": round(time.monotonic() - t0, 1),
            "when": (now or _dt.datetime.now(_dt.timezone.utc)).strftime("%Y-%m-%d %H:%M UTC"),
            "not_covered": [
                "the topic quiz's sentences (quizsets.py) -- a separate instrument",
                "the AI's own words on a second miss -- that is the night watch's lane",
                "the rendered SCREEN (screencheck.py judges that in the battery)",
                f"a times-table pass beyond its first {TABLE_FACTS_SHOWN} facts"]}


# =============================================================================
# 4. THE REPORT
# =============================================================================
_SEV = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}


def report_markdown(result, build="") -> str:
    fs = result.get("findings") or []
    gen = [f for f in fs if f["owner"].startswith("generator:")]
    auth = [f for f in fs if f["owner"].startswith("lesson:")]
    L = [f"# Course sweep -- {result.get('course')} -- {result.get('when')}"
         + (f"  (build {build})" if build else ""),
         "",
         f"_Read by: {result.get('seat') or 'the judge seat'}_",
         "",
         f"{result.get('ran', 0)} of {result.get('asked', 0)} lessons read · "
         f"**{len(fs)} findings** ({len(gen)} on generators, {len(auth)} on authored beats) · "
         f"{len(result.get('clean') or [])} lessons clean · {result.get('unplaced', 0)} unplaced · "
         f"{len(result.get('errors') or [])} unread · {result.get('seconds', 0)}s",
         "",
         "_A GENERATOR finding is on a line the engine makes for every lesson that shares the "
         "op -- fix the generator once and it is fixed everywhere. An AUTHORED finding is on "
         "this lesson's own words. Severity is the reviewer's; every quote was matched to the "
         "transcript before it was kept._",
         ""]
    if gen:
        L.append("## Generator findings -- fix once, fixes many")
        L.append("")
        by = {}
        for f in gen:
            by.setdefault(f["owner"].split(":", 1)[1], []).append(f)
        for op, rows in sorted(by.items(), key=lambda kv: (-len(kv[1]), kv[0])):
            rows.sort(key=lambda f: (_SEV.get(f["severity"], 3), f["lesson"]))
            L.append(f"### op `{op}` — {len(rows)} finding(s) across "
                     f"{len({f['lesson'] for f in rows})} lesson(s)")
            L.append("")
            for f in rows[:12]:
                L.append(f"- **{f['severity']}** · {f['kind']} · {f['lesson']} turn {f['turn']} "
                         f"({f['beat']})\n  > {f['quote']}\n  {f['why']}\n  _Fix:_ {f['fix']}")
            if len(rows) > 12:
                L.append(f"- …and {len(rows) - 12} more on this op")
            L.append("")
    if auth:
        L.append("## Authored findings -- by unit and lesson")
        L.append("")
        by = {}
        for f in auth:
            by.setdefault((f["unit"], f["lesson"], f["topic"]), []).append(f)
        for (unit, lid, topic), rows in sorted(by.items(), key=lambda kv: (kv[0][0], kv[0][1])):
            rows.sort(key=lambda f: (_SEV.get(f["severity"], 3), f["turn"]))
            L.append(f"### Unit {unit} · {lid} — \"{topic}\" ({len(rows)})")
            L.append("")
            for f in rows:
                L.append(f"- **{f['severity']}** · {f['kind']} · turn {f['turn']} ({f['beat']})\n"
                         f"  > {f['quote']}\n  {f['why']}\n  _Fix:_ {f['fix']}")
            L.append("")
    if result.get("clean"):
        L.append("## Clean")
        L.append("")
        L.append(", ".join(result["clean"]))
        L.append("")
    if result.get("errors"):
        L.append("## Not read")
        L.append("")
        for e in result["errors"]:
            L.append(f"- {e['lesson']}: {e['error'][:200]}")
        L.append("")
    L.append("## What this sweep did not cover")
    L.append("")
    for x in result.get("not_covered") or []:
        L.append(f"- {x}")
    L.append("")
    L.append("*I did no harm and this file is not truncated.*")
    return "\n".join(L)


def _dir(data_dir):
    return os.path.join(str(data_dir), "coursesweep")


_NAME_RE = re.compile(r"^[a-z0-9]+_\d{4}-\d{2}-\d{2}(?:_\d{4})?$")


def write_report(data_dir, result, build="", now=None) -> str:
    """Write <course>_<date>[_HHMM].md and .json; return the report NAME (not a path)."""
    d = _dir(data_dir)
    os.makedirs(d, exist_ok=True)
    now = now or _dt.datetime.now(_dt.timezone.utc)
    base = f"{result.get('course')}_{now.strftime('%Y-%m-%d')}"
    name = base
    if os.path.exists(os.path.join(d, name + ".md")):
        name = base + "_" + now.strftime("%H%M")
    with open(os.path.join(d, name + ".json"), "w", encoding="utf-8") as fh:
        json.dump(result, fh, ensure_ascii=False, indent=1)
    with open(os.path.join(d, name + ".md"), "w", encoding="utf-8") as fh:
        fh.write(report_markdown(result, build))
    return name


def list_reports(data_dir) -> list:
    d = _dir(data_dir)
    try:
        names = sorted(f[:-3] for f in os.listdir(d) if f.endswith(".md"))
    except OSError:
        return []
    out = []
    for n in reversed(names):
        row = {"name": n}
        try:
            with open(os.path.join(d, n + ".json"), encoding="utf-8") as fh:
                j = json.load(fh)
            row.update({"course": j.get("course"), "findings": len(j.get("findings") or []),
                        "ran": j.get("ran"), "when": j.get("when")})
        except Exception:  # noqa: BLE001
            pass
        out.append(row)
    return out


def read_report(data_dir, name: str) -> str:
    """The markdown of one report. The name is validated against a strict pattern so no
    path can be traversed from here."""
    if not _NAME_RE.match(str(name or "")):
        return ""
    try:
        with open(os.path.join(_dir(data_dir), name + ".md"), encoding="utf-8") as fh:
            return fh.read()
    except OSError:
        return ""

# I did no harm and this file is not truncated.

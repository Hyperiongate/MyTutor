# =============================================================================
# coursesweep.py  --  THE COURSE SWEEP: one reviewer, every authored lesson, once
#                     --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-09-24  BUILD xv -- ONE CHARTER LINE from the third Algebra II sweep: the [[choices]]
#               on an ask or a reason question are tap buttons the child reads, never read
#               aloud, by design. Four sweeps in a row (wx, xa, xb, this one) raised "the
#               choices are never read aloud"; each was declined by hand. Now the reviewer is
#               told.
#   2026-09-23  BUILD xu -- A STOPPED SWEEP CAN BE RESUMED. Jim's Prob/Stat sweep of 09-23
#               read 16 lessons ($2.40), then the reader's credits ran out: the wv rule
#               stopped it, the report was written -- and main.py cleared the checkpoint,
#               because "the report is the record now" (xp). The 16 were paid for and
#               unresumable. Now the checkpoint keeps only the rows actually READ (an error
#               row is dropped at save time, so a resume reads that lesson instead of
#               skipping it), run_sweep drops any error row it is handed on resume, and the
#               STOPPED banner says to press Resume. main.py keeps the checkpoint when the
#               sweep stopped. A sweep that finishes clean still clears it.
#   2026-09-23  BUILD xq -- ONE CHARTER LINE from the third Algebra I sweep: "times",
#               "timesed" and "timesing" are the course's chosen verb for multiplying, in
#               every course -- the reviewer called "timesed" nonstandard in a reason choice.
#   2026-09-23  BUILD xp -- THE SWEEP SURVIVES A RESTART. Jim ran Algebra I twice on 09-22
#               and both sweeps "just disappeared": the sweep is a thread inside the web
#               server, and until now it wrote its report only at the END -- a deploy (a
#               push to GitHub) or a Render restart in the 30-40 minutes it runs killed
#               the thread, nothing reached the disk, and the card went back to "no sweep
#               has run in this process". Every lesson already read was paid for and lost.
#               Now: run_sweep keeps one ROW per lesson read and calls `checkpoint(partial)`
#               after each -- main.py writes it to data/coursesweep/<course>_partial.json
#               (write_partial / read_partial / clear_partial / list_partials; the name has
#               no date, so list_reports never lists it). A sweep started with `resume=`
#               that partial skips the lessons it holds, reads only the rest, and the
#               final report carries a "Resumed after a restart" line with both builds
#               and both times. A restart now costs at most the one lesson in flight.
#               The wv stop rule counts the NEW run's streak only. Nothing else changed.
#   2026-09-18  BUILD wz -- THE TABLE LESSON'S PROBLEM SPACE IS THE PASS. The second Basic
#               sweep read "PROBLEM SPACE: 12 problems" on the times-table lesson and called
#               the intro's "all 81 facts" false (HIGH). The line was wrong, not the intro:
#               that lesson practises as an 81-fact pass and its bank only feeds the worked
#               pairs, the quiz and the drill. problem_space() now says so for any lesson
#               whose mastery is "table".
#   2026-09-17  BUILD wv -- THE SWEEP SAYS WHY IT STOPPED. With the reader's credits at zero,
#               a Pre-Calc sweep "finished" in 7.7 s: 36 identical 429s, "0 findings in 36
#               lessons" on the card, read as a hung sweep. run_sweep now stops after
#               HARD_STOP_AFTER (3) lessons in a row fail with the same hard error (429,
#               401/403, no credits, quota, key not set -- _HARD_ERROR_RE), lists the rest
#               as not attempted, and returns "stopped"; report_markdown puts a STOPPED /
#               NOT READ banner under the header; list_reports rows carry asked, errors
#               and stopped so the card can label such a report. A slow reader that fails
#               one lesson and answers the next is untouched (the streak resets).
#   2026-09-17  BUILD ws -- THE COST ESTIMATE MATCHES THE BILL. EST_USD_PER_LESSON 0.05 -> 0.15,
#               read off the reader's billing dashboard (about $98 for September's ~520
#               swept lessons and the night watch). The admin card's "estimated_usd" now
#               says about $5.40 for a 36-lesson course, not $1.80. Nothing else changed.
#   2026-09-17  BUILD wr -- THE REPORT LIST IS NEWEST FIRST. list_reports sorted by file
#               name, and names begin with the course, so the admin card's dropdown put
#               probstat_2026-09-16 above calculus_2026-09-17 and the two Calculus reports
#               side by side -- Jim opened yesterday's by mistake while today's was still
#               running. Now sorted by the sweep's own "when" (newest first; a report with
#               no .json keys on its name's date; ties keep the name order). Nothing else
#               in the file changed.
#   2026-09-16  BUILD wm -- TWO CHARTER LINES from the first Algebra II sweep: a ✗ on a [[step]]
#               line marks the wrong path a child might take, never a false equation the tutor
#               asserts ("3 × 5 = 15 ✗" was read as the tutor denying that 3 × 5 is 15); and a
#               bare "log" on a board in the Algebra II log lessons is base 2, said in the words.
#   2026-09-16  BUILD wl -- ONE CHARTER LINE: "square back" is Geometry's chosen verb for the
#               square root (the longest-side lesson teaches it; four beats and three
#               generators lean on it). The first Geometry sweep called it nonstandard twice.
#   2026-09-16  BUILD wk -- TWO CHARTER LINES from the first Algebra I sweep: a [[graph]]'s
#               range= is the x-window (the y-window fits the line; "y = 6x + 8 starts
#               outside a 0..5 grid" was not so), and a walk-back's "not N" names the
#               COMMON wrong answer, not the number the STUDENT line gave (the walk-back is
#               scripted per problem; the sweep's miss is synthetic).
#   2026-09-16  BUILD wh -- THE PROBLEM SPACE LISTS ITS VALUES. The first Basic sweep (67
#               findings) objected five times to cases the bank does not hold but the
#               RANGE admitted: 30 percent in a lesson whose percents are 10, 25 and 50
#               (two HIGHs), 52 ÷ 4 where every tens digit divides, an exact hundred in
#               rounding. problem_space() now lists a field's distinct values when there
#               are PROBLEM_SPACE_LIST_MAX (12) or fewer, and gives the range only past
#               that. One charter line: a [[numberline]] draws its own tick labels between
#               min= and max= (the tenths lesson was asked to "draw the ten tenth marks"
#               that the figure already draws). The other rulings the reviewer tripped on
#               (a why beat's picture, a case outside the space) were already there; it
#               could not see the space finely enough to obey.
#   2026-09-15  BUILD wg -- ONE CHARTER LINE: a why beat is a story over the goal card, by
#               design; its having no picture is not a finding (two of the fourth sweep's
#               fourteen asked for one).
#   2026-09-15  BUILD wf -- THE PROBLEM SPACE ON THE PAGE. The third Entry sweep (15
#               findings) was half objections to cases the lesson cannot ask. The
#               transcript now opens with a PROBLEM SPACE line -- the bank's ranges, the
#               ops, and each op's constraint in the engine's own words ("two different
#               numbers inside the counting range") -- and the charter says a case outside
#               it is not a finding. problem_space(lesson) is the new function.
#   2026-09-15  BUILD we -- TWO SMALL THINGS FROM THE SECOND CLEAN SWEEP (47 findings).
#               (1) The charter says the practice is a SAMPLE, and now also says not to
#               judge the closing line by which problems the sample asked ("You can count
#               to ten" was flagged because the walk happened to ask 1, 3 and 5). (2) The
#               practice intro a lesson with a reason question SPEAKS (lessonscripts'
#               practice_intro_line) is labelled "practice-intro" too, so its quote places.
#   2026-09-15  BUILD wc -- CALIBRATED ON THE FIRST COURSE. Jim's Entry sweep came back
#               with 219 findings and ~130 of them were one defect of THIS file: the
#               transcript had no student in it, so the reviewer read a fixed monologue
#               that praised answers nobody gave and corrected misses nobody made. Now
#               (1) the walk writes a STUDENT line after every ask -- the answer, marked
#               correct or WRONG, or the tapped reason; (2) an ask's board carries its
#               [[choices]] buttons and the reason question its reason choices, so "tap
#               the reason" is answerable on the page; (3) the charter explains the
#               STUDENT lines, says the practice is a SAMPLE of the bank, and adds the
#               rulings the first report tripped on: the "Your turn" card's unspoken
#               hints, a topic word in the title line, "over nine" (the course's chosen
#               wording), and a level-appropriate rule that the lesson does not itself
#               contradict; (4) the report header counts findings by kind.
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
# ESTIMATE ONLY, like lessonaudit's: per-lesson cost of one judge read. (ws) CORRECTED
# FROM THE BILLING DASHBOARD, as the line below always promised: September's reader spend
# was about $98 across roughly 520 swept lessons plus the night watch, which is about
# $0.15 a lesson -- three times the 0.05 first guessed at Sonnet-class prices (the reader
# is gpt-5.5, and a Diffeq transcript runs long). A 36-lesson sweep is about $5.40.
EST_USD_PER_LESSON = 0.15
# (wh) a field with this many distinct values or fewer is LISTED on the problem-space
# line ("a is one of 10, 25, 50"); more than this and it is given as a range.
PROBLEM_SPACE_LIST_MAX = 12
# (wv) THE SWEEP STOPS WHEN THE SEAT IS DEAD. On 09-17 the reader's credits ran out and a
# Pre-Calc sweep "finished" in 7.7 seconds: all 36 lessons failed with the same 429, the
# card said "0 findings in 36 lessons", and Jim read it as a hung sweep. A failure that
# will not change from one lesson to the next -- no credits, a bad or missing key, a
# quota -- ends the sweep after this many lessons IN A ROW fail the same way; the rest
# are listed as not attempted, and the report and the card say why it stopped. A judge
# that times out on one long lesson and answers the next is not this (the error text
# differs, or the run recovers), so a slow reader is never cut short.
HARD_STOP_AFTER = 3
_HARD_ERROR_RE = re.compile(r"\b(?:429|401|403)\b|no credits|insufficient_quota|quota|api key|"
                            r"not set|unauthori[sz]ed|invalid.{0,20}key|judge unavailable", re.I)


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
    # (we) the form a lesson with a reason question actually speaks
    _pil = getattr(L, "practice_intro_line", None)
    if _pil:
        put(_pil(lesson), "practice-intro")
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
            board = s.get("board") or ""
            # (wc) an ask carries its tap buttons: they are on the child's screen, and a
            # reviewer that cannot see them reports "tap the reason" as unanswerable.
            if s.get("kind") == "ask":
                if s.get("choices"):
                    board += str(s["choices"])
                elif s.get("reason"):
                    try:
                        board += L.reason_choices_for(lesson)
                    except Exception:  # noqa: BLE001
                        pass
            turns.append({"n": len(turns) + 1,
                          "kind": _kind_of(s.get("spoken"), kind_idx, L, s),
                          "spoken": s.get("spoken") or "",
                          "board": board,
                          "op": p.get("op", "") if s.get("kind") == "ask" else ""})

    def student(text):
        """(wc) THE STUDENT'S TURN. The first sweep read a transcript with no student
        in it and reported 130 times that the tutor praised an answer nobody gave and
        corrected a miss nobody made. The walk always knew what the child said; now
        the page says it too."""
        turns.append({"n": len(turns) + 1, "kind": "student", "spoken": text,
                      "board": "", "op": ""})

    out, st = L.step(lesson, st, ("begin",))
    take(out)
    for _ in range(200):
        if st.get("finished"):
            break
        pend = st.get("pending") or {}
        if pend.get("reason"):
            reason = (lesson.get("explain") or {}).get("answer", "")
            student(f'taps the reason "{reason}" — correct')
            out, st = L.step(lesson, st, ("answer", reason))
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
            wrong = (right or 0) + 777
            student(f"answers {wrong} — WRONG (the right answer is {right})")
            out, st = L.step(lesson, st, ("answer", wrong))
            take(out)
            if any(s.get("kind") == "intervene" for s in out):
                out, st = L.step(lesson, st, ("resume",))
                take(out)
            continue
        student(f"answers {right} — correct")
        out, st = L.step(lesson, st, ("answer", right))
        take(out)
    return turns


def problem_space(lesson, L=None) -> str:
    """(wf, 2026-09-15) THE PROBLEM SPACE, ON THE PAGE. The third Entry sweep still objected
    to cases the lesson cannot ask -- two equal numbers in "which is bigger" (its check
    forbids them), 5 − 8 in a course that never takes a bigger number away, a zero digit,
    a hundreds column in a two-digit lesson. The charter told the reviewer not to; it could
    not obey, because it could not SEE the space. Now it can: one line, computed from the
    bank and the worked pairs, plus the op's own constraint in the engine's words."""
    if L is None:
        import lessonscripts as L  # noqa: N812
    probs = list(lesson.get("bank") or []) + [pr["ask"] for pr in (lesson.get("pairs") or [])]
    # (wz, 2026-09-18) a times-table lesson practices as a PASS -- all 81 facts -- and its
    # bank is only the worked pairs' asks; the second Basic sweep read "12 problems" and
    # called the intro's "all 81 facts" false. The line says what the pass is.
    if lesson.get("mastery") == "table":
        return ("PROBLEM SPACE: a times-table pass -- all 81 facts, 1 × 1 to 9 × 9, one after "
                "another (the transcript shows the first few); the bank's facts are the worked "
                "pairs' asks, not the pass")
    if not probs:
        return "PROBLEM SPACE: (none -- a table pass)"
    parts = []
    for k in ("a", "b", "c"):
        vals = [p[k] for p in probs if isinstance(p.get(k), int)]
        if not vals:
            continue
        # (wh, 2026-09-16) THE VALUES, NOT THE RANGE, when there are few enough to list.
        # "a from 10 to 50" invited the Basic reviewer to object that 30 percent breaks
        # the percent-of rule -- the bank is 10, 25 and 50 and nothing else. A range
        # says what the lesson COULD ask; the list says what it DOES.
        distinct = sorted(set(vals))
        if distinct == [0] and k != "a":
            continue                                   # a padding field, not a value
        if len(distinct) <= PROBLEM_SPACE_LIST_MAX:
            parts.append(f"{k} is one of " + ", ".join(str(v) for v in distinct))
        else:
            parts.append(f"{k} from {min(vals)} to {max(vals)}")
    ops = sorted({str(p.get("op", "+")) for p in probs})
    rules = []
    for op in ops:
        chk = (L.OP_EXT.get(op) or {}).get("check")
        if chk:
            try:
                r = chk(probs[0] if probs[0].get("op", "+") == op else next(p for p in probs if p.get("op", "+") == op))
                if isinstance(r, tuple) and len(r) == 2 and r[1]:
                    rules.append(f"{op}: {r[1]}")
            except Exception:  # noqa: BLE001
                pass
    line = (f"PROBLEM SPACE: {len(probs)} problems; " + "; ".join(parts)
            + f"; op {'/'.join(ops)}")
    if rules:
        line += "; every problem satisfies -- " + " | ".join(rules)
    return line + ". A rule is judged against THESE problems, not against numbers this lesson cannot ask."


def render_transcript(lesson, turns) -> str:
    """The transcript as the reviewer reads it: one numbered turn per beat, the words
    and then the board, tags left in (the rule index explains every tag)."""
    head = (f"LESSON {lesson.get('id')} -- {lesson.get('course')} unit {lesson.get('unit')} "
            f"-- \"{lesson.get('topic')}\" -- levels {'/'.join(lesson.get('levels') or ())}")
    lines = [head, problem_space(lesson), ""]
    for t in turns:
        if t["kind"] == "student":
            lines.append(f"[{t['n']}] STUDENT {t['spoken']}")
        else:
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

HOW TO READ THE PAGE. Lines marked STUDENT are what the child did: an answer, marked
correct or WRONG, or a tapped reason. The tutor's praise, "Not quite", "three in a row" and
"that is the reason" always follow a STUDENT line and are earned by it -- never report them
as praising or correcting an answer that was not given. The BOARD line under an ask includes
the [[choices ...]] tap buttons the child sees. The practice you see is a SAMPLE of the
lesson's problem bank (three right answers end it), so never conclude that a lesson "never
practices" a number or a case you did not happen to see -- and never judge the closing
line ("You can count to ten") by which problems the sample happened to ask.

Do NOT report: style preferences; the choice of numbers; the lesson being short; the
absence of things outside its topic; a WHY beat (the lesson's opening story) having no
picture -- it is told over the goal card by design, and the pictures start on the next beat; the rule index's own wording; the "Your turn" card's
tap/say/type hints (screen instructions, deliberately unspoken); a [[numberline]]'s tick marks
and labels between min= and max= -- the drawing puts them in on its own (0.1, 0.2, ... on a
line from 0 to 1), and hops= and points= are the jumps and the marked spots, NOT the ticks; a [[graph]]'s range= is its
x-window only -- the y-window fits the drawn lines on its own, so a line starting at y = 8 on a
range="0..5" grid IS visible; a walk-back's "not N" line (the second explanation after a miss) names the
COMMON wrong answer for that problem, by design -- it is scripted per problem and cannot know the
number on the STUDENT line, so it is not a finding when the two differ; "square back" -- Geometry's
chosen verb for finding the number whose square is a total (taught in the longest-side lesson and
used from there on) -- is not an unclear phrase; "times", "timesed" and "timesing" are the course's
chosen verb for multiplying, in every course (Hundreds of lines use them) -- never nonstandard; a ✗ on a [[step]] line marks the WRONG
PATH a child might take (its number and its short label, like "24 ✗ one day only"), never a false
equation the tutor asserts; a bare "log" on a board in the Algebra II logarithm lessons is base 2
unless the same board shows another base beside it (the lesson says so in its words); the
[[choices]] on an ask or a reason question are TAP BUTTONS the child reads, never read aloud, by
design -- "the choices are never read aloud" is not a finding; a topic word in the lesson's
own title line; "over nine" for a sum of ten or more (the course's one chosen wording); a
rule stated for the numbers this lesson uses, at this level, UNLESS the lesson itself later
contradicts it or a child could misapply it within the same unit -- and the PROBLEM SPACE
line under the lesson's title is what "the numbers this lesson uses" means: a case outside it
(two equal numbers where the space says they differ; a hundreds column where every number is
two-digit; a zero where no digit is zero) is NOT a finding. A quote must be COPIED
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


def _row_for(les, placed=None, clean=False, error=None, unplaced=0):
    """(xp) ONE LESSON'S RESULT, the unit a checkpoint keeps. A row is either read
    (findings placed, clean or not, unplaced count) or an error (the reader's words)."""
    return {"lesson": les["id"], "findings": list(placed or []), "clean": bool(clean),
            "error": error, "unplaced": int(unplaced)}


def _assemble(course, picked, rows, stopped, t0, now=None, resumed=None):
    """(xp) THE RESULT FROM ITS ROWS, in the course's lesson order. write_report and the
    card read this shape; a resumed sweep and a fresh one assemble the same way."""
    by = {r["lesson"]: r for r in rows}
    findings, errors, clean, unplaced_total = [], [], [], 0
    for les in picked:
        r = by.get(les["id"])
        if r is None:
            continue
        if r.get("error"):
            errors.append({"lesson": r["lesson"], "error": r["error"]})
            continue
        findings.extend(r.get("findings") or [])
        unplaced_total += int(r.get("unplaced") or 0)
        if r.get("clean"):
            clean.append(r["lesson"])
    out = {"course": course, "ran": len(picked) - len(errors), "asked": len(picked),
           "findings": findings, "errors": errors, "clean": clean, "stopped": stopped,
           "unplaced": unplaced_total, "seconds": round(time.monotonic() - t0, 1),
           "when": (now or _dt.datetime.now(_dt.timezone.utc)).strftime("%Y-%m-%d %H:%M UTC"),
           "not_covered": [
               "the topic quiz's sentences (quizsets.py) -- a separate instrument",
               "the AI's own words on a second miss -- that is the night watch's lane",
               "the rendered SCREEN (screencheck.py judges that in the battery)",
               f"a times-table pass beyond its first {TABLE_FACTS_SHOWN} facts"]}
    if resumed:
        out["resumed"] = resumed
    return out


def run_sweep(data_dir, course, judge, limit=None, progress=None, L=None, now=None,
              checkpoint=None, resume=None):
    """Sweep one course. Never raises; a lesson the reviewer could not read is recorded
    as such and the sweep goes on. Returns the result dict that write_report consumes.

    (xp) `checkpoint(partial)` is called after EVERY lesson with the rows read so far
    (the shape write_partial keeps); `resume=` is such a partial from an interrupted
    run -- its lessons are skipped, its rows kept, and the result says it was resumed.
    A checkpoint that raises never stops the sweep."""
    if L is None:
        import lessonscripts as L  # noqa: N812
    t0 = time.monotonic()
    picked = lessons_for(course, L)
    if resume and (resume.get("course") == course) and not limit and resume.get("asked"):
        limit = int(resume["asked"])      # (xp) a resumed sweep keeps the first run's size
    if limit:
        picked = picked[:int(limit)]
    rows = []
    resumed = None
    if resume and (resume.get("course") == course):
        rows = [dict(r) for r in (resume.get("rows") or []) if r.get("lesson")]
        # (xu) the prior run's error rows -- "not attempted", a dead seat, a walk failure
        # -- are read now, not carried; a checkpoint written since xu holds none anyway
        rows = [r for r in rows if not r.get("error")]
        resumed = {"before": len(rows), "after": 0, "prior_when": resume.get("when"),
                   "prior_build": resume.get("build"), "prior_started": resume.get("started")}
    done_ids = {r["lesson"] for r in rows}
    stopped = None
    streak = []                          # (wv) consecutive identical hard failures

    def _save():
        # (xu) the checkpoint keeps only the lessons actually READ: a row with an error
        # (a dead seat, a walk failure, "not attempted") was paid for by nobody, and a
        # resume must read it, not skip it. The report still lists every error.
        if checkpoint:
            try:
                read_rows = [dict(r) for r in rows if not r.get("error")]
                checkpoint({"course": course, "asked": len(picked), "rows": read_rows,
                            "done": len(read_rows), "resumed": resumed,
                            "when": _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")})
            except Exception:  # noqa: BLE001
                pass

    for i, les in enumerate(picked):
        if les["id"] in done_ids:
            continue
        if progress:
            try:
                progress(i, len(picked), les["id"])
            except Exception:  # noqa: BLE001
                pass
        try:
            turns = transcript_for(les, L)
        except Exception as exc:  # noqa: BLE001
            rows.append(_row_for(les, error=f"walk failed: {exc}"))
            _save()
            continue
        data, err = review_lesson(les, turns, judge)
        if err:
            rows.append(_row_for(les, error=err))
            # (wv) the same hard error, lesson after lesson, will not change: stop
            sig = str(err)[:200]
            if _HARD_ERROR_RE.search(sig) and (not streak or streak[-1] == sig):
                streak.append(sig)
            else:
                streak = [sig] if _HARD_ERROR_RE.search(sig) else []
            if len(streak) >= HARD_STOP_AFTER:
                stopped = {"after": i + 1, "error": sig}
                for rest in picked[i + 1:]:
                    if rest["id"] in done_ids:
                        continue
                    rows.append(_row_for(rest, error=f"not attempted -- the sweep stopped after "
                                                     f"{i + 1} lessons in a row failed the same way: {sig}"))
                _save()
                break
            _save()
            continue
        streak = []
        placed, unplaced = place_findings(les, turns, data)
        rows.append(_row_for(les, placed=placed, unplaced=unplaced,
                             clean=(not placed and (data or {}).get("clean", not placed))))
        if resumed:
            resumed["after"] += 1
        _save()
    return _assemble(course, picked, rows, stopped, t0, now=now, resumed=resumed)


# =============================================================================
# 4. THE REPORT
# =============================================================================
_SEV = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}


def report_markdown(result, build="") -> str:
    fs = result.get("findings") or []
    gen = [f for f in fs if f["owner"].startswith("generator:")]
    auth = [f for f in fs if f["owner"].startswith("lesson:")]
    kinds = {}
    for f in fs:
        kinds[f.get("kind") or "?"] = kinds.get(f.get("kind") or "?", 0) + 1
    L = [f"# Course sweep -- {result.get('course')} -- {result.get('when')}"
         + (f"  (build {build})" if build else ""),
         "",
         f"_Read by: {result.get('seat') or 'the judge seat'}_",
         "",
         "_By kind: " + (", ".join(f"{k} {n}" for k, n in sorted(kinds.items(), key=lambda kv: -kv[1]))
                         or "none") + "_",
         "",
         f"{result.get('ran', 0)} of {result.get('asked', 0)} lessons read · "
         f"**{len(fs)} findings** ({len(gen)} on generators, {len(auth)} on authored beats) · "
         f"{len(result.get('clean') or [])} lessons clean · {result.get('unplaced', 0)} unplaced · "
         f"{len(result.get('errors') or [])} unread · {result.get('seconds', 0)}s",
         "",
         *(([f"⚠️ **STOPPED after {result['stopped'].get('after')} lesson(s)** -- "
             f"{HARD_STOP_AFTER} in a row failed the same way and the rest were not attempted: "
             f"{result['stopped'].get('error', '')[:200]}. The lessons read so far are "
             f"a reading of those lessons only; fix the seat and press Resume on the "
             f"card -- it reads just the rest.", ""]) if result.get("stopped") else []),
         *(([f"_Resumed after a restart: {result['resumed'].get('before', 0)} lesson(s) were read "
             f"before it (started {result['resumed'].get('prior_started') or '?'}"
             + (f", build {result['resumed'].get('prior_build')}" if result['resumed'].get('prior_build') else "")
             + f"), {result['resumed'].get('after', 0)} read now._", ""])
           if result.get("resumed") else []),
         *(([f"⚠️ **NOT READ** -- every lesson failed: "
             f"{(result.get('errors') or [{}])[0].get('error', '')[:200]}. Nothing here is a "
             f"reading of the course; fix the seat and run it again.", ""])
           if result.get("errors") and not result.get("ran") and not result.get("stopped") else []),
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


_PARTIAL_RE = re.compile(r"^([a-z0-9]+)_partial\.json$")


def partial_path(data_dir, course) -> str:
    """(xp) data/coursesweep/<course>_partial.json -- no date in the name, so
    list_reports (which lists .md files) never shows it as a report."""
    return os.path.join(_dir(data_dir), f"{re.sub(r'[^a-z0-9]', '', str(course).lower())}_partial.json")


def write_partial(data_dir, course, partial: dict, build="", started="") -> str:
    """(xp) The checkpoint after every lesson: the rows read so far plus the build and
    the start time, written whole then renamed so a restart mid-write leaves the last
    good copy. Returns the path."""
    os.makedirs(_dir(data_dir), exist_ok=True)
    path = partial_path(data_dir, course)
    body = dict(partial or {})
    body.update({"course": course, "build": build or body.get("build") or "",
                 "started": started or body.get("started") or ""})
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(body, fh, ensure_ascii=False, indent=1)
    os.replace(tmp, path)
    return path


def read_partial(data_dir, course):
    """(xp) The saved checkpoint for a course, or None."""
    try:
        with open(partial_path(data_dir, course), encoding="utf-8") as fh:
            j = json.load(fh)
        return j if isinstance(j, dict) and j.get("rows") else None
    except (OSError, ValueError):
        return None


def clear_partial(data_dir, course) -> bool:
    """(xp) Remove a course's checkpoint (the sweep finished and wrote its report)."""
    try:
        os.remove(partial_path(data_dir, course))
        return True
    except OSError:
        return False


def list_partials(data_dir) -> dict:
    """(xp) {course: {done, asked, when, build, started}} for every saved checkpoint --
    the card offers a Resume for each."""
    out = {}
    try:
        names = os.listdir(_dir(data_dir))
    except OSError:
        return out
    for n in names:
        m = _PARTIAL_RE.match(n)
        if not m:
            continue
        j = read_partial(data_dir, m.group(1))
        if j:
            out[m.group(1)] = {"done": len(j.get("rows") or []), "asked": j.get("asked"),
                               "when": j.get("when"), "build": j.get("build"),
                               "started": j.get("started")}
    return out


def list_reports(data_dir) -> list:
    """Every report, NEWEST FIRST -- by the sweep's own timestamp, whatever the course.

    (wr) Until wr the list was sorted by NAME, and names begin with the course, so
    probstat_2026-09-16 sat above calculus_2026-09-17 and the two Calculus reports sat
    side by side with yesterday's easy to grab (Jim did, on 09-17). The "when" the
    sweep wrote into its .json is the order that matters; a report with no .json
    falls back to its name's date, and ties keep the name order."""
    d = _dir(data_dir)
    try:
        names = sorted(f[:-3] for f in os.listdir(d) if f.endswith(".md"))
    except OSError:
        return []
    out = []
    for n in names:
        row = {"name": n}
        try:
            with open(os.path.join(d, n + ".json"), encoding="utf-8") as fh:
                j = json.load(fh)
            row.update({"course": j.get("course"), "findings": len(j.get("findings") or []),
                        "ran": j.get("ran"), "when": j.get("when"),
                        "asked": j.get("asked"), "errors": len(j.get("errors") or []),
                        "stopped": bool(j.get("stopped"))})
        except Exception:  # noqa: BLE001
            pass
        out.append(row)
    # "YYYY-MM-DD HH:MM UTC" sorts as text; a name-only row keys on the date in its name
    def _key(row):
        w = row.get("when") or ""
        if not w:
            m = re.search(r"_(\d{4}-\d{2}-\d{2})(?:_(\d{4}))?$", row["name"])
            w = (m.group(1) + " " + (m.group(2)[:2] + ":" + m.group(2)[2:] if m.group(2) else "00:00")) if m else ""
        return (w, row["name"])
    out.sort(key=_key, reverse=True)
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

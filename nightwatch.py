# =============================================================================
# nightwatch.py  --  THE GOVERNOR  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-09-04  BUILD sk -- THE FILE AGREES WITH RENDER. _DEFAULT_LESSONS 12 -> 10.
#               Render has said NIGHTWATCH_LESSONS=10 since 08-31, and that IS the
#               intended budget -- so sh's env banner was firing every single night to
#               report a setting nobody intends to change back. A banner that fires
#               nightly is not a banner; it is the noise sh was written to prevent. The
#               override machinery is untouched and still shouts the moment the
#               environment moves a default -- there is simply nothing to shout about
#               while Render and this file agree. (Jim, 2026-09-04: "make our software
#               also say ten, so that doesn't get flagged either.")
#   2026-09-03  BUILD sj -- THE REPORT SEES THE FLOOR. tutor.py's new `floor` event
#               (a draft every attempt of which carried a TRUTH-class finding was
#               withheld; the child got the fallback line) gets its own telemetry
#               line, joins the named offenders, and joins the dated reasons list so
#               each withheld falsehood is readable with its referee and its clock.
#               A floor is a false statement that did NOT reach a child: the count
#               measures the referees working, and it is kept separate from the
#               pass-through count, which is conduct shipping least-bad as before.
#   2026-09-03  BUILD sh -- THE WATCH SAYS WHAT IT WAS TOLD TO DO. Four report holes,
#               every one of them named by a triage that then had to give up on it.
#               (1) THE 10-vs-12 QUESTION, ASKED THREE WATCHES RUNNING AND NEVER ONCE
#               ANSWERABLE. 08-31, 09-01 and 09-02 all reported "10 lessons" against a
#               file that says LESSONS_PER_NIGHT = 12, and the 09-02 triage wrote "STILL
#               10 -- still unexplained. Third watch in a row." It was unanswerable
#               because the report printed only what HAPPENED. A shrunken rotation, two
#               skipped slots and a changed constant produce the identical number and
#               want three different fixes. The report now prints the BUDGET it was
#               given ("told to run 12 x 6 from 10 scenarios"), shouts when the
#               ENVIRONMENT has moved one of this file's defaults (a Render knob leaves
#               no other trace anywhere -- no deploy, no commit, no log line), and NAMES
#               THE ROTATION: every slot picked, in order, with its own outcome -- ran,
#               skipped, errored, crashed, never reached -- and repeat slots marked as
#               repeats. That last part closes the 08-20 watch's F2, open since August:
#               the report printed sc["id"] with no duplicate marker, so a skipped
#               DUPLICATE read as a missing scenario. The budget is recorded BEFORE
#               preflight on purpose: a night that cannot start is exactly the night you
#               want it. (2) 507 REFEREE FIRES, NO NAMES. This counter has been on the
#               report since build ha and has never once been actionable -- it says the
#               machine is awake, not which rule is breaking, and it cannot score a new
#               referee against the class it was built for. Two triages asked for the
#               split by name. event_stats has grouped by name all along; this one kind
#               threw the names away. (3) A REASON WITH NO CLOCK IS INDISTINGUISHABLE
#               FROM ITS OWN GHOST. pq gave this report the crash REASON and never gave
#               it a date, so 09-01 had to hold every line -- haiku-4.5 404s, "Extra
#               data" parses, the ended DeepSeek trial's 402s -- with "the window has
#               not yet rolled past them", and 09-02 held them again. Each distinct
#               reason now carries count, newest sighting, oldest sighting and an age,
#               and one printed sentence gives the reader the test: an old newest is
#               draining out, a fresh one is a live regression. `at` has been on every
#               row since ha. (4) THE REVIEWER WAS NEVER TOLD ABOUT THE RULINGS. The
#               09-02 watch CONFIRMED "Everybody feels stuck before they learn something
#               new" as a rule-42 defect. It is not one: pq cut the bare people-words
#               from the referee after a canon sweep found them in 21 authored teaching
#               cards, and rn put it to Jim, who ruled them legal -- "it normalizes
#               struggle without naming kids, classmates, or ages." Nobody told the
#               reviewer, so it re-opened a question settled two builds earlier. NEW
#               SECTION (C) of VERIFY_SYSTEM, generated from a new RULED_ALLOWED list.
#               ⚠️ IT IS DATA, NOT PROSE, and for the reason px already paid for: the
#               conduct list was hand-maintained and drifted three times (jk, ni, pq)
#               before px generated it. A ruling list buried in a 3,000-character prompt
#               would drift the same way. ⚠️ EVERY ENTRY SILENCES A CLASS OF FINDING, so
#               every entry carries a BOUNDARY that is still fully enforced -- here, the
#               CHILD-nouns ("most kids", "a lot of students", ages, grades,
#               percentiles) are untouched and still confirmed on sight. The report
#               names each standing ruling every night, because a ruling that silences
#               findings must never do it quietly. PART 3ie pins all four.
#   2026-08-31  BUILD qy -- THE CEILING WAS TOO LOW FOR THE ROOM. The 2026-08-31 watch ran
#               8 of the rotation's 12 lesson slots and then the default 45-minute budget
#               cut it off -- 2 scenarios were skipped outright, not just delayed. Jim, when
#               asked whether to raise it: "Yes, raise it," with no ceiling named, and an
#               earlier offer on record to "size it to fit all 10 scenarios with margin".
#               45 min / 8 lessons measures ~5.6 min/lesson on that night; at that pace all
#               12 rotation slots (the 10 scenarios, two of them landing twice on a 12-slot
#               night) need ~68 minutes. NIGHTWATCH_MAX_MINUTES's default is raised
#               45 -> 90: comfortable margin over the measured 68-minute need, enough to
#               absorb a heavier finding night (more verify_finding calls, one per finding)
#               without starting to skip scenarios again. LESSONS_PER_NIGHT stays 12 --
#               the time budget was never the cost lever, the lesson count is, so nightly
#               spend is unchanged by this build. Still overridable from Render with
#               NIGHTWATCH_MAX_MINUTES=<n> and no deploy, exactly as before this change --
#               PART 3ak now proves that override still works, not just the new default.
#   2026-08-30  BUILD qh -- THE EYES WERE HALF SHUT. The 2026-08-30 report counted 120
#               teaching-path fail-opens and printed 2026-08-26's stale critic 404s as
#               "what they actually said", because build pq's reason query asks only for
#               referee_crash. Every one of those 120 turns had written its reason to
#               system_events. The query now asks for failopen, seat_fallback and
#               privacy_gate too; the fallback finding names the SEAT that is teaching
#               (not "Anthropic", which qg made wrong); and a night that was mostly
#               apologies LEADS with an outage banner, because "23 findings" reads as
#               "the teaching got worse" when the brain was simply down. PART 3gl.
#   2026-08-29  BUILD px -- THE REVIEWER'S LIST IS GENERATED, NOT HAND-KEPT. The
#               2026-08-29 watch could not judge FIVE findings ("rule not in the
#               reviewer's list": 28, 47, 61, 63) -- all four are real, enforced rules.
#               VERIFY_SYSTEM's (B) list had been hand-maintained at eleven and drifted
#               three times (jk, ni, pq). It is now a template; the full 65-rule index
#               is rendered at import from tutor.rule_titles() -- the SAME extraction
#               that generates RULES.md -- and the eleven elaborations stay above it.
#               Fails open to the eleven if the registry cannot be read. PART 3gc.
#   2026-08-28  BUILD pq -- THE EYES REPORT WHAT THEY SAW. Two holes in this file,
#               both found by reading its own 2026-08-28 report. (1) THE CRASH REASON
#               WAS BEING THROWN AWAY: event_stats groups by (kind, name) and never
#               selects `detail`, so the report said "referee_crash - livecritic: 33x"
#               and could not say why -- 33 crashes nobody could act on. recent_events
#               has carried detail all along; the report asks for it now, distinct
#               reasons only. (2) SIX OF NINE "REFUTATIONS" WERE THIS FILE'S OWN LIST
#               BEING SHORT: findings against rules 7, 26, 27, 41, 46, 50 were
#               dismissed because VERIFY_SYSTEM names only eleven conduct rules. Build
#               ni hand-added rule 42 after exactly this; hand-maintenance drifted
#               again within days. The verifier now returns rule_known, unjudged
#               findings get their OWN section and headline count, and they are kept
#               OUT of the refuted number that feeds the health metric.
#   2026-08-25  BUILD ni -- RULE 42 JOINS THE REVIEWER'S CONDUCT LIST. The 2026-08-25
#               report refuted two rule-42 findings ("the tutor compares the student
#               to other children") and BOTH refutations gave the same reason: "rule
#               42 is not one of the conduct promises provided". That is not a
#               judgment -- it is the reviewer reporting a hole in its own list. Rule
#               42 is enforced on live replies by student_compare_conflict (the 25th
#               referee, build id), which is this list's own membership criterion.
#               Those two findings may have been real; the next run will tell.
#   2026-08-20  BUILD jk -- THE REVIEWER GETS A SECOND TEST. The 2026-08-20 report
#               refuted 19 of 20 findings (95%; the first real night was 73%, and the
#               /admin card's own scale calls near-100% MISCALIBRATED). Reading the 19
#               dismissals showed why, and it was not the tutor being good:
#               VERIFY_SYSTEM offered exactly ONE way to confirm a finding --
#               "a specific child would learn something false or be unable to follow" --
#               and refuted anything that was "taste, tone or pacing". That is a
#               MATHS-CORRECTNESS test, so a rule of CONDUCT could never pass it.
#               17 of the 19 refutations quote that criterion back verbatim, and the
#               rules it silenced are the ones JIM found: rule 17 (the answer was on
#               the board before the question was asked -- refuted TWICE as "the maths
#               was still correct"), rules 43 and 62 (the child credited with a step the
#               TUTOR took -- refuted TWICE as "a tone/credit issue"), rule 44 (x3),
#               rule 15, rule 40. Build go exists because Jim asked for a system that
#               catches what he cannot; on the rules he DID catch, it was blind -- and
#               the blindness read on the dashboard as a healthy refute rate.
#               THE FIX IS THE REVIEWER, NOT THE CRITIC. VERIFY_SYSTEM now states the
#               product is judged on TWO things -- (A) TRUTH and (B) CONDUCT -- names
#               the nine conduct promises with their rule numbers, and says plainly that
#               "the maths was still correct" and "it was a matter of tone" are not
#               defences against them. The skepticism is preserved and re-aimed: it now
#               belongs to the EVIDENCE ("if you cannot see it in the transcript,
#               REFUTE") rather than to the standard, so build fe's anti-wolf-crying
#               discipline survives. The taste/tone refute clause is narrowed to
#               findings that name no conduct promise; the "later corrected" clause now
#               refutes a TRUTH finding only, because a later correction does not
#               un-spoil a question that was already answered.
#               ⚠️ NOT PROVED BY MEASUREMENT YET. Re-running last night's 19 would need
#               their transcripts, which the report does not carry. The refute rate of
#               the NEXT run is the measurement -- expect it to fall from 95% toward the
#               60-75% band, and expect the first confirmed findings to be rule 17 and
#               rule 43/62. If it falls below ~40%, the reviewer has gone soft and this
#               prompt is the thing to tighten.
#   2026-08-18  BUILD hq -- run_scenario's return grew a fourth member (the measured
#               prompt size, for the two-prompt-sizes experiment); the watch unpacks
#               and ignores it. No behaviour change here.
#   2026-08-18  BUILD hm -- write_report() takes an optional `now` so the restart-safety
#               battery checks are hermetic. The old test hardcoded 2026-08-17 as
#               "tonight" while write_report stamped the file with the REAL date; the
#               moment the calendar rolled past the day the test was written, both
#               restart-safety checks failed on a healthy build. Production behavior
#               unchanged (callers omit `now`). Lesson: a test that pins the clock must
#               pin it EVERYWHERE the code reads it.
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
#
# MAX_MINUTES is a SAFETY CAP, not the cost lever -- LESSONS_PER_NIGHT is. Raising this
# does not raise what a night spends; it only lets the 12 lessons already budgeted
# actually finish. (qy, 2026-08-31) The 45-minute default was too low for the room: the
# 2026-08-31 watch measured ~5.6 min/lesson (45min / 8 lessons run) and was cut off with
# 2 of the rotation's 12 slots unrun. All 12 slots at that pace need ~68 minutes. Raised
# to 90 for margin over a heavier finding night (each finding costs one more
# verify_finding call). Jim said "yes, raise it" without naming a ceiling; this sizes it
# to cover the full rotation with room to spare, per the offer made when asking.
# (sh, 2026-09-03) THE FILE'S OWN DEFAULTS, as named constants, so the report can say
# when the ENVIRONMENT has moved one of them. Three watches in a row (08-31, 09-01,
# 09-02) reported "10 lessons" while this file said 12, and the report could not answer
# the question it raised -- shrunken rotation? skipped slots? changed constant? -- because
# it never printed what it was TOLD to do, only what happened. env_overrides() below is
# that missing half, and a knob moved in Render now leaves a trace in the morning report.
_DEFAULT_LESSONS     = 10   # (sk, 2026-09-04) matches Render; see change note
_DEFAULT_TURNS       = 6
_DEFAULT_MAX_MINUTES = 90
_DEFAULT_HOUR_UTC    = 8   # ~1am Pacific

LESSONS_PER_NIGHT = int(os.environ.get("NIGHTWATCH_LESSONS", "") or _DEFAULT_LESSONS)
TURNS_PER_LESSON  = int(os.environ.get("NIGHTWATCH_TURNS", "") or _DEFAULT_TURNS)
MAX_MINUTES       = int(os.environ.get("NIGHTWATCH_MAX_MINUTES", "") or _DEFAULT_MAX_MINUTES)
RUN_HOUR_UTC      = int(os.environ.get("NIGHTWATCH_HOUR_UTC", "") or _DEFAULT_HOUR_UTC)
VERIFY_FINDINGS   = (os.environ.get("NIGHTWATCH_VERIFY", "on").strip().lower()
                     not in ("off", "0", "false", "no"))
LEDGER_NAME       = "nightwatch_ledger.json"
REPORT_DIR_NAME   = "nightwatch"
KEEP_REPORTS      = int(os.environ.get("NIGHTWATCH_KEEP", "30") or 30)


def enabled() -> bool:
    return os.environ.get("NIGHTWATCH", "on").strip().lower() not in ("off", "0", "false", "no")


def env_overrides() -> list:
    """(sh) Which of this file's budget defaults the ENVIRONMENT has moved, one readable
    line each. A knob changed in Render leaves NO other trace -- there is no deploy, no
    commit and no log line -- so "why did it run 10 and not 12?" cost three watches to
    not-answer. The report prints these; a quiet night prints nothing extra."""
    pairs = (("NIGHTWATCH_LESSONS", LESSONS_PER_NIGHT, _DEFAULT_LESSONS),
             ("NIGHTWATCH_TURNS", TURNS_PER_LESSON, _DEFAULT_TURNS),
             ("NIGHTWATCH_MAX_MINUTES", MAX_MINUTES, _DEFAULT_MAX_MINUTES),
             ("NIGHTWATCH_HOUR_UTC", RUN_HOUR_UTC, _DEFAULT_HOUR_UTC))
    out = [f"{nm} = {cur} (this file's default is {dflt})"
           for nm, cur, dflt in pairs if cur != dflt]
    if not VERIFY_FINDINGS:
        out.append("NIGHTWATCH_VERIFY = off (findings ship unjudged)")
    return out


# =============================================================================
# THE CLOCK ON AN EVENT (sh, 2026-09-03)
# =============================================================================
# A distinct crash reason with no timestamp cannot be told apart from its own ghost. The
# 09-01 triage had to HOLD every telemetry line it read -- the haiku-4.5 404s, the "Extra
# data" JSON parses, the DeepSeek 402s -- with the note "the window has not yet rolled
# past them", because the report showed a 7-day COUNT and no dates. recent_events has
# carried `at` since build ha; the report simply never asked for it.
_EPOCH = datetime(1970, 1, 1, tzinfo=timezone.utc)


def _parse_at(raw):
    """An event's ISO timestamp as an aware UTC datetime, or None. Never raises: a row
    whose clock is unreadable still gets to print its reason."""
    try:
        s = str(raw or "").strip()
        if not s:
            return None
        if s.endswith("Z"):
            s = s[:-1] + "+00:00"
        dt = datetime.fromisoformat(s)
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except Exception:  # noqa: BLE001
        return None


def _ago(dt, now=None) -> str:
    """How stale one sighting is, in words a tired reader can take at a glance."""
    if not dt:
        return ""
    secs = ((now or datetime.now(timezone.utc)) - dt).total_seconds()
    if secs < 0:
        return "just now"
    if secs < 3600:
        return f"{int(secs // 60)}m ago"
    if secs < 86400:
        return f"{int(secs // 3600)}h ago"
    return f"{int(secs // 86400)}d ago"


def _age_line(newest, oldest, n, now=None) -> str:
    """THE GHOST TEST, on one line: how many, how recently, over what span. A reason
    whose NEWEST sighting is days old is draining out of the 7-day window and needs no
    action. One with a fresh newest is LIVE, and that is today's problem."""
    now = now or datetime.now(timezone.utc)
    if not newest:
        return f"_{n}x - no timestamps on these rows_"
    fresh = (now - newest).total_seconds() < 86400
    bits = [f"{n}x",
            ("⚠️ **LIVE** - newest " if fresh else "last seen ")
            + newest.strftime("%Y-%m-%d %H:%M UTC") + f" ({_ago(newest, now)})"]
    if oldest and oldest != newest:
        bits.append(f"first {oldest.strftime('%Y-%m-%d %H:%M UTC')} ({_ago(oldest, now)})")
    return "_" + " · ".join(bits) + "_"


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
_VERIFY_TEMPLATE = """\
You are a skeptical reviewer of AUDIT FINDINGS about a maths tutor for children. You are
not reviewing the tutor. You are reviewing the CRITIC, and your default position is that
the critic is wrong.

Given a transcript and one finding, decide whether the finding is REAL.

THIS TUTOR IS JUDGED ON TWO THINGS, NOT ONE.

(A) TRUTH -- a child must not learn something false, and must not be left unable to
    follow what is happening.

(B) CONDUCT -- the tutor must keep the promises this product makes about HOW it teaches.
    A broken promise is a REAL defect even when every number in the reply is correct.
    "But the maths was still right", "but it was harmless" and "but that is a matter of
    tone" are NOT defences against any of these:
      - rule 43  the tutor perceives exactly two things and never pretends otherwise
      - rule 62  the tutor may only point at work that actually happened -- crediting a
                 child with a step the TUTOR took is a false statement ABOUT THE CHILD,
                 not a pleasantry
      - rule 15  a question must be complete on the board before it is asked
      - rule 16  a substitution or check question re-writes its equation, same reply
      - rule 17  never answer your own question in the same breath -- if the answer is
                 already on the board when the question is asked, the check is spoiled,
                 however correct that answer happens to be
      - rule 39  a check must be easy to FAIL (the REQUIRED wording named below is not a
                 rule 39 violation)
      - rule 44  the problem is read aloud, in full, before it is worked
      - rules 14 and 48  notation is read aloud the first time it appears
      - rule 40  a returning student is ASKED before being made to sit through the same
                 introduction a second time
      - rule 42  a student is compared to NOBODY but themselves -- "most kids",
                 "other students", age norms, class averages: the kind-sounding
                 comfort forms included. Comparisons to the student's OWN earlier
                 work are fine.
    Every one of these is enforced on live replies by a machine referee. If a referee
    would regenerate the reply for it, it is not "taste".

    THE FULL INDEX OF PROMISES. The eleven above are elaborated because they were the
    ones a reviewer once refuted as "tone". They are not the whole list. EVERY numbered
    rule this product enforces is below, generated from the tutor's own rule registry
    (the same text the tutor is given), and a finding that names any of them is a
    CONDUCT finding under (B):
{RULE_INDEX}

(C) RULINGS ALREADY TAKEN. The shapes below were put to the person who owns this
    product and were RULED ALLOWED. They are not defects, however well they match the
    wording of the rule they sit under, and re-confirming one costs a real morning. A
    finding that describes one of them is REFUTED -- say "ruled allowed" and name the
    date. Each ruling carries its own BOUNDARY, and the boundary is still fully
    enforced: a finding that crosses it is judged normally under (A) and (B).
{RULED_ALLOWED}

REFUTE the finding if ANY of these hold:
- the finding describes a shape from (C) above and stays inside that ruling's boundary
- the quoted words are not actually in the transcript, or are quoted misleadingly
- the maths is correct under standard conventions, however surprising it looks
- the "problem" is a decided design of this product: the check-in wording
  "...or should I show it a different way?" is REQUIRED, not a defect; a student may
  choose to move past an unfinished unit; foundation-first teaching (explaining before
  asking) is deliberate and is NOT "lecturing"; the tutor accepting a right answer before
  extending it is rule 59 working
- the finding is about wording preference, warmth, or how fast the lesson moves, AND it
  names no conduct promise from (B)
- the finding restates something the transcript itself later corrects -- this refutes a
  TRUTH finding, but NOT a conduct one: a later correction does not un-spoil a question
  that was already answered, nor un-say credit that was already given

CONFIRM the finding when the transcript plainly shows EITHER
  (A) a specific child, reading these specific words, would learn something false or be
      unable to follow, OR
  (B) one of the conduct promises above was broken.

YOUR SKEPTICISM BELONGS TO THE EVIDENCE, NOT TO THE STANDARD. When you cannot see in the
transcript that the thing described actually happened, REFUTE. When you can see it
plainly and it breaks (A) or (B), CONFIRM -- "it was harmless" is not a reason to refute.

ONE MORE FIELD, AND IT IS NOT ABOUT THE TUTOR. The index in (B) is generated from the
product's rule registry, so it should be complete -- but if the finding cites a rule
number that appears NOWHERE in (B) above, set "rule_known": false -- whatever else you
decide. That is not a judgment about the tutor; it tells us the critic named a rule the
registry does not hold. Never refute a finding merely because its rule is missing from
(B): judge it on (A) truth and on the plain conduct promise it describes, and let
"rule_known": false carry the gap.

Return STRICT JSON only:
{"real": true|false, "why": "<one sentence>", "rule_known": true|false}
"""


# =============================================================================
# THE RULED-ALLOWED LIST (sh, 2026-09-03)
# =============================================================================
# WHY THIS EXISTS. The 2026-09-02 watch confirmed "Everybody feels stuck before they
# learn something new" as a rule-42 defect. It is not one. Build pq had already cut the
# bare people-words from the referee's wordlist after finding them in 21 authored
# teaching cards, with the reason pinned and the instruction "do not add it back"; build
# rn put the question to Jim directly and he RULED them legal. The reviewer was never
# told, so it re-confirmed a shape that had been settled two builds earlier -- and a
# governor that reports a closed question as a new finding spends exactly the attention
# it was built to save.
#
# THE DISCIPLINE THAT MADE THIS A LIST AND NOT A SENTENCE. VERIFY_SYSTEM's conduct list
# was hand-maintained for four builds and drifted three times (jk, ni, pq) before px
# generated it from the registry. A ruling list will drift the same way if it is prose
# buried in a prompt. It is DATA here: one entry per ruling, each with the date, the
# ruling in the owner's own words where they exist, and the boundary that is still
# enforced. The battery pins it (PART 3ie), the report names it, and adding the next
# ruling is one dict -- not an edit to a 3,000-character prompt nobody re-reads.
#
# ⚠️ THE BOUNDARY IS THE WHOLE SAFETY OF THIS MECHANISM. Every entry here SILENCES a
# class of finding. An entry written one word too wide silences real defects and nothing
# will ever tell us. Write the boundary before the shape.
RULED_ALLOWED = [
    {
        "rule": 42,
        "date": "2026-09-01",
        "shape": 'the PEOPLE-forms -- "a lot of people", "most people", "everyone", '
                 '"everybody", "folks", "beginners" -- used to normalise a struggle or '
                 "to say how hard an IDEA is",
        "ruling": "Jim, 2026-09-01, asked directly and answering directly: it "
                  '"normalizes struggle without naming kids, classmates, or ages." '
                  "Build pq had already cut these words from the rule-42 referee after "
                  "a canon sweep found them in 21 authored teaching cards doing honest "
                  'work -- the "denominator" foundation says "that surprises a lot of '
                  'people" and means the fraction, not the child.',
        "boundary": "THE CHILD-NOUNS ARE NOT COVERED and remain real rule-42 defects, "
                    'caught by a live referee every time: "most kids", "a lot of '
                    'students", "other children", "learners", and every age, grade, '
                    "percentile or class average. The test is what the sentence "
                    "MEASURES. If it measures this student against a room of CHILDREN, "
                    "confirm it -- the ruling does not reach it.",
    },
]


def _ruled_allowed_lines():
    """The (C) block, rendered from RULED_ALLOWED. A ruling with no boundary would be a
    blank cheque, so an entry missing one is rendered with a loud placeholder rather
    than quietly silencing more than it was given."""
    if not RULED_ALLOWED:
        return "      (no standing rulings -- judge every finding on (A) and (B))"
    out = []
    for r in RULED_ALLOWED:
        out.append(f"      - RULE {r.get('rule')} · RULED ALLOWED {r.get('date')} · "
                   f"{r.get('shape')}")
        out.append(f"          the ruling: {r.get('ruling')}")
        out.append(f"          the boundary (still enforced): "
                   f"{r.get('boundary') or '⚠️ NONE RECORDED -- judge this one normally'}")
    return "\n".join(out)


def _rule_index_lines():
    """The (B) index: one line per numbered rule, read from the tutor's own registry
    (tutor.rule_titles -- the same extraction that generates RULES.md). Fails open
    to a one-line notice so a registry hiccup can never take the reviewer down."""
    try:
        import tutor as _tu
        titles = _tu.rule_titles()
        if titles:
            return "\n".join(f"      - rule {n:<3} {titles[n]}" for n in sorted(titles))
    except Exception as exc:  # noqa: BLE001 -- the watch must run with or without it
        print(f"[nightwatch] rule registry unavailable ({exc}); reviewer keeps the eleven")
    return "      (the rule registry could not be read tonight -- the eleven above stand)"


def render_verify_system():
    """VERIFY_SYSTEM with the (B) index filled from the registry and the (C) rulings
    filled from RULED_ALLOWED. Rendered once at import (the constant below) and callable
    again so a test can see it fresh. .replace and not .format on purpose: the template
    ends with a literal JSON object, and str.format would choke on its braces."""
    return (_VERIFY_TEMPLATE
            .replace("{RULE_INDEX}", _rule_index_lines())
            .replace("{RULED_ALLOWED}", _ruled_allowed_lines()))


VERIFY_SYSTEM = render_verify_system()


def _seat_name() -> str:
    """(qh) Who is actually teaching -- "deepseek/deepseek-v4-pro" -- for the report's
    remedy lines. Never raises: an unreadable seat is just "brain"."""
    try:
        import tutor as _tu
        b = _tu.active_brain()
        return f"{b.get('provider') or 'brain'}/{b.get('model') or ''}".rstrip("/")
    except Exception:  # noqa: BLE001
        return "brain"


def verify_finding(openai_call, scenario, transcript, finding):
    """Hand one finding to an independent skeptic.
    Returns (is_real, why, error, rule_known).

    (pq) rule_known is FALSE when the finding cites a rule the reviewer's own conduct
    list does not contain. The 2026-08-28 watch refuted NINE findings and SIX of them
    named rules 7, 26, 27, 41, 46 and 50 -- none of which are in VERIFY_SYSTEM's list.
    Those are not refutations of the tutor; they are the reviewer reporting a hole in
    its own list, which is exactly what build ni saw once already with rule 42. Counting
    them as refutations makes the harness look healthy while it discards real defects,
    so they are now separated out in the report and never counted as calibration."""
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
        return None, "", err, True    # None = COULD NOT VERIFY, never silently confirmed
    try:
        data = json.loads(text)
    except Exception:  # noqa: BLE001
        s, e = (text or "").find("{"), (text or "").rfind("}")
        try:
            data = json.loads(text[s:e + 1])
        except Exception:  # noqa: BLE001
            return None, "", f"verifier did not return JSON: {(text or '')[:160]}", True
    # (pq) rule_known is the reviewer telling us OUR conduct list is short. Absent
    # means "no opinion" -> True, so an older/quieter verifier never invents a gap.
    return (bool(data.get("real")), str(data.get("why") or ""), None,
            bool(data.get("rule_known", True)))


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
           "unverified": [], "refuted": 0, "refuted_list": [], "harness_gap": [],
           "errors": [], "seconds": 0.0,
           # (qh) the OUTAGE tally: fallback turns against turns attempted. A night
           # where every turn was an apology must not read as "23 findings".
           "fallback_turns": 0, "turns_total": 0,
           "budget_stopped": False, "probes_run": sorted((probe_hooks or {}).keys()),
           # (sh) WHAT WE WERE TOLD TO DO, beside what we did. "ran: 10" is a number;
           # the roster is the answer. Every slot the rotation picked, in order, with
           # its own outcome -- so "12 picked, 10 ran" carries the two names that
           # explain it instead of costing a fourth watch to guess at.
           "roster": [], "picked": [], "repeats": 0, "scenarios_available": 0,
           "lessons_requested": 0, "turns_requested": 0}
    try:
        import lessonaudit
    except Exception as exc:  # noqa: BLE001
        out["errors"].append(f"lessonaudit unavailable: {exc}")
        return out

    lessons = int(lessons or LESSONS_PER_NIGHT)
    turns = int(turns or TURNS_PER_LESSON)
    # (sh) RECORDED BEFORE PREFLIGHT, DELIBERATELY. A night that cannot start is exactly
    # the night you want the budget line for -- "told to run 12 x 6, ran none, preflight
    # said no key" is a diagnosis; "the watch did not complete" is a shrug.
    out["lessons_requested"] = lessons
    out["turns_requested"] = turns
    out["scenarios_available"] = len(getattr(lessonaudit, "SCENARIOS", None) or [])
    ok, note = lessonaudit.preflight()
    if not ok:
        out["errors"].append(f"preflight failed, nothing was run: {note}")
        return out

    ledger = load_ledger(data_dir)
    picked = pick_tonight(lessonaudit.SCENARIOS, lessons, day_index(now))
    deadline = started + MAX_MINUTES * 60

    # (sh) THE ROSTER, built BEFORE the first lesson runs, so a night that dies halfway
    # still says what it meant to do. A slot that is never reached stays "not reached" --
    # which is itself a finding, and one the old report could not express at all.
    out["picked"] = [sc.get("id") for sc in picked]
    _times_seen = {}
    for sc in picked:
        _k = sc.get("id")
        _times_seen[_k] = _times_seen.get(_k, 0) + 1
        out["roster"].append({"id": _k, "course": sc.get("course"),
                              "repeat": _times_seen[_k] > 1,
                              "outcome": "not reached", "note": ""})
    out["repeats"] = sum(1 for r in out["roster"] if r["repeat"])

    for _slot, sc in enumerate(picked):
        if time.time() > deadline:
            out["budget_stopped"] = True
            out["skipped"].append(f"{sc['id']} (time budget of {MAX_MINUTES} min reached)")
            out["roster"][_slot]["outcome"] = "skipped"
            out["roster"][_slot]["note"] = f"time budget of {MAX_MINUTES} min reached"
            continue
        try:
            # build hq: run_scenario now also returns the measured prompt size
            # (the two-prompt-sizes experiment); the watch teaches at the normal
            # size and does not use the measurement.
            transcript, err, fallbacks, _pchars = lessonaudit.run_scenario(sc, turns)
            if err:
                out["errors"].append(f"{sc['id']}: {err}")
                out["roster"][_slot]["outcome"] = "error"
                out["roster"][_slot]["note"] = str(err)[:200]
                continue
            out["ran"] += 1
            out["roster"][_slot]["outcome"] = "ran"
            out["turns_total"] += int(turns or 0)          # (qh)
            out["fallback_turns"] += int(fallbacks or 0)   # (qh)
            if fallbacks:
                # A graceful-failure turn is a RELIABILITY finding the critic cannot
                # argue away (build dc's lesson: a critic marking content reads straight
                # past absence).
                _record(out, ledger, sc, {
                    "severity": "medium", "rule": None,
                    "what": f"the tutor lost its train of thought {fallbacks} time(s) in "
                            f"one lesson and apologised to the student",
                    "quote": "(fallback turn)", "why": "a child is left waiting mid-lesson",
                    # (qh) name the SEAT, not "Anthropic" -- build qg made the brain
                    # pluggable and this line sent the 2026-08-30 reader to the wrong
                    # call path while DeepSeek was the one raising.
                    "fix": f"check the {_seat_name()} call path and the turn deadline"},
                    verified_note="counted by code, not judged")

            for name, hook in (probe_hooks or {}).items():
                try:
                    hook(sc, transcript)
                except Exception as exc:  # noqa: BLE001 -- a probe never breaks the watch
                    out["errors"].append(f"probe {name} on {sc['id']}: {exc}")

            findings, cerr = lessonaudit.critique(sc, transcript)
            if cerr:
                out["errors"].append(f"{sc['id']} critic: {cerr}")
                # The LESSON ran; the CRITIC did not. Both facts are true and the
                # roster says both, because "ran" alone would imply it was judged.
                out["roster"][_slot]["note"] = f"taught, but not judged -- critic: {str(cerr)[:160]}"
                continue
            for f in (findings or {}).get("findings", []) or []:
                if not VERIFY_FINDINGS:
                    _record(out, ledger, sc, f, verified_note="verification disabled")
                    continue
                real, why, verr, rule_known = verify_finding(
                    lessonaudit._openai, sc, transcript, f)
                if verr:
                    out["unverified"].append({"scenario": sc["id"],
                                              "what": f.get("what"), "error": verr})
                elif real:
                    _record(out, ledger, sc, f, verified_note=why)
                elif not rule_known:
                    # (pq) NOT A REFUTATION. The reviewer was never given this rule, so
                    # it could not judge the conduct promise the finding names. Held
                    # separately, and deliberately kept OUT of the refuted count that
                    # feeds the health metric -- a hole in our list must never read as
                    # healthy skepticism.
                    out["harness_gap"].append({"scenario": sc["id"],
                                               "severity": f.get("severity"),
                                               "rule": f.get("rule"),
                                               "what": f.get("what"),
                                               "quote": f.get("quote"),
                                               "reviewer": why})
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
            if out["roster"][_slot]["outcome"] != "ran":
                out["roster"][_slot]["outcome"] = "crashed"
            out["roster"][_slot]["note"] = f"{type(exc).__name__}: {exc}"[:200]
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
    nowdt = datetime.now(timezone.utc)
    stamp = nowdt.strftime("%Y-%m-%d %H:%M UTC")
    L = [f"# Night watch — {stamp}" + (f"  (build {build})" if build else ""), "",
         f"{result.get('ran', 0)} lessons run · **{len(new)} new confirmed** · "
         f"{result.get('recurring', 0)} already known · {result.get('refuted', 0)} refuted "
         f"on review · {result.get('seconds', 0)}s"
         # (pq) the gap count rides in the headline: a night where the reviewer could
         # not judge six findings must not read as a night with nine refutations.
         + (f" · ⚠️ **{len(result.get('harness_gap') or [])} unjudged "
            f"(rule not in the reviewer's list)**"
            if result.get("harness_gap") else ""), ""]

    # (sh) ⭐ WHAT THIS WATCH WAS TOLD TO DO. Three watches in a row (08-31, 09-01,
    # 09-02) reported "10 lessons" against a file that says twelve, and each triage had
    # to write the same sentence: "still unexplained". The report could not settle it
    # because it printed only what HAPPENED. Shrunken rotation, skipped slots and a
    # changed constant all look identical in a bare count -- and they are three
    # different problems with three different fixes. The budget line and the roster
    # below make the question answer itself, every night, for good.
    _req, _avail = int(result.get("lessons_requested") or 0), int(result.get("scenarios_available") or 0)
    if _req or _avail:
        L += ["_Told to run **{r}** lesson(s) x {t} turns, drawn from **{a}** scenario(s)"
              "{rep} · ceiling {m} min · adversarial verify {v}._".format(
                  r=_req, t=int(result.get("turns_requested") or 0), a=_avail,
                  rep=(f"; {result['repeats']} slot(s) are repeats because the rotation "
                       f"is wider than the list" if result.get("repeats") else ""),
                  m=MAX_MINUTES, v=("on" if VERIFY_FINDINGS else "**OFF**")), ""]
    _ov = env_overrides()
    if _ov:
        L += ["> ⚠️ **The environment has moved this watch's budget.** These are set in "
              "Render, not in the code, so nothing else anywhere records them:"]
        L += [f"> - `{o}`" for o in _ov]
        L += ["", ""]

    # (qh) ⭐ THE OUTAGE BANNER. 2026-08-30: the first night on the DeepSeek seat
    # produced "23 new confirmed" -- and every one of them was the same sentence,
    # "(I'm having trouble thinking right now)", because the seat raised on all 120
    # turns. A report that leads with a finding count teaches the reader that the
    # TEACHING got worse, when what happened is that the brain was down. When most
    # turns were apologies, that is the headline and nothing else is.
    _fb, _tt = int(result.get("fallback_turns") or 0), int(result.get("turns_total") or 0)
    if _fb and _tt and _fb * 2 >= _tt:
        L += [f"## 🚨 THE BRAIN WAS DOWN — {_fb} of {_tt} turns were apologies, not teaching",
              "",
              f"_The seat configured to teach ({_seat_name()}) raised on {_fb} of the "
              f"{_tt} turns attempted, so the student got the fallback line instead of a "
              f"reply. **The findings below are that one outage seen many ways — "
              f"they are not {len(new)} separate teaching defects.** Read the "
              "failopen reasons in the telemetry section first: they carry the "
              "vendor's own words. Nothing here judges the rules._",
              ""]
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

    # (pq) WHAT THE REVIEWER COULD NOT JUDGE. Findings whose rule is not in
    # VERIFY_SYSTEM's conduct list. These are NOT refutations and are not counted as
    # such -- the reviewer is telling us our own list is short. The 2026-08-28 watch
    # buried six of these inside a nine-item "thrown away" list, where they read as
    # healthy skepticism. They are the opposite: unjudged defects.
    gaps = result.get("harness_gap") or []
    if gaps:
        seen_rules = sorted({str(g.get("rule")) for g in gaps if g.get("rule")})
        L += [f"## ⚠️ The reviewer was never given these rules ({len(gaps)})", "",
              "_These findings were NOT refuted -- they could not be judged at all, "
              "because the rule they name is missing from the reviewer's conduct list. "
              "Since build px that list is generated from the tutor's own rule registry "
              "(tutor.rule_titles), so a number here means the critic cited a rule the "
              "registry does not hold -- check the number, or decide out loud that it is "
              "not a promise this product makes._", ""]
        if seen_rules:
            L += [f"**Rules missing from the list: {', '.join(seen_rules)}**", ""]
        for g in gaps:
            L += [f"- **{g.get('scenario')}**"
                  + (f" (rule {g['rule']})" if g.get("rule") else "")
                  + f" — {g.get('what')}",
                  f"  - reviewer: _{g.get('reviewer') or '(no reason given)'}_"]
        L += [""]

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
              # (sj) THE FLOOR: a draft every attempt of which carried a TRUTH-class
              # finding was WITHHELD and the child got the fallback line instead.
              # Each one is a false statement that did NOT reach a child -- the
              # count is a measure of the referees working, not of the tutor
              # failing, and it is NOT a pass-through (those are conduct, above).
              f"- truth floors (a false draft withheld; the child got the fallback "
              f"line): **{_tot('floor')}**",
              f"- referee fires: **{_tot('referee_fire')}** · probe observations: "
              f"{_tot('probe')} · prompt-size events: {_tot('promptsize')}", ""]

        alarm = []
        for kind in ("referee_crash", "clienterror", "pass_through", "floor"):
            for nm, n in sorted((counts.get(kind) or {}).items(), key=lambda kv: -kv[1])[:5]:
                alarm.append(f"  - {kind} · {nm}: {n}×")
        if alarm:
            L += ["  The named offenders:"] + alarm + [""]

        # (sh) ⭐ WHICH REFEREES FIRED. This count has been on the report since build ha
        # and has never once been actionable. "507 referee fires" says the machine is
        # awake; it does not say which rule is being broken, and it cannot score a new
        # referee against the class it was built for. The 09-01 and 09-02 triages both
        # asked for this split BY NAME and both had to give up on it -- the fracslash /
        # secondtriangle / countedask / knownfalse scoreboard was unreadable from the
        # report. event_stats has grouped by name all along (the "named offenders" block
        # right above uses exactly that); this one kind simply threw the names away.
        fires = sorted(((nm, n) for nm, n in (counts.get("referee_fire") or {}).items()),
                       key=lambda kv: (-kv[1], kv[0]))
        if fires:
            L += [f"  Which referees fired ({len(fires)} distinct, most-fired first):"]
            L += [f"  - **{nm or '(unnamed)'}**: {n}x" for nm, n in fires[:25]]
            if len(fires) > 25:
                L += [f"  - ...and {len(fires) - 25} more referee(s), "
                      f"{sum(n for _, n in fires[25:])} fires between them"]
            L += [""]
        elif _tot("referee_fire"):
            L += ["  ⚠️ Referee fires were counted but not one carried a NAME, so the "
                  "split cannot be read. That is a hole in the eyes, not a quiet week.",
                  ""]

        # (pq) AND WHAT THEY ACTUALLY SAID. event_stats groups by (kind, name) and
        # DROPS the detail column, so for weeks this report could say
        # "referee_crash · livecritic: 33×" and not one word about why -- 33 crashes
        # that nobody could act on. Build of proved the detail is the whole value:
        # the message named a typo'd model ID and the fix took minutes. recent_events
        # has carried the detail all along; the report simply never asked for it.
        # Distinct reasons only, newest first, so a repeated crash costs one line.
        try:
            # (qh) failopen WAS NOT IN THIS LIST. On 2026-08-30 the teaching seat
            # raised on all 120 turns, every one wrote its reason to system_events --
            # and this report printed 08-26's stale critic 404s instead, because it
            # only ever asked for referee_crash. The counter said 120 and the eyes
            # said nothing. Every alarming kind is asked for now.
            rows = _store.recent_events(hours=24 * 7, limit=200,
                                        kinds=["referee_crash", "clienterror",
                                               "failopen", "seat_fallback",
                                               "privacy_gate", "floor"])
            # (sh) ⭐ AND WHEN THEY SAID IT. pq gave this block the reason; it never
            # gave it a CLOCK, and without one a reason cannot be told apart from its
            # own ghost. The 09-01 triage had to HOLD every line it read here -- the
            # haiku-4.5 404s, the "Extra data" JSON parses, the ended DeepSeek trial's
            # 402s -- with the note "the window has not yet rolled past them", and then
            # the 09-02 triage had to hold them again. Each distinct reason now carries
            # how many times, how recently, and over what span. The rule is one line and
            # a reader can apply it in a second: an old newest is draining out; a fresh
            # newest is a live regression. `at` has been on every row since build ha.
            agg = {}
            for r in rows:
                d = " ".join(str(r.get("detail") or "").split())[:240] or "(no detail recorded)"
                k = (r.get("kind"), r.get("name"), d)
                at = _parse_at(r.get("at"))
                a = agg.setdefault(k, {"n": 0, "newest": None, "oldest": None})
                a["n"] += 1
                if at:
                    if not a["newest"] or at > a["newest"]:
                        a["newest"] = at
                    if not a["oldest"] or at < a["oldest"]:
                        a["oldest"] = at
            reasons = []
            for (kind, nm, d), a in sorted(agg.items(),
                                           key=lambda kv: (kv[1]["newest"] or _EPOCH),
                                           reverse=True):
                reasons.append([f"  - `{kind}` · **{nm}** — {d}",
                                "    " + _age_line(a["newest"], a["oldest"], a["n"], nowdt)])
            if reasons:
                L += ["  What they actually said, and WHEN (distinct reasons, newest "
                      "sighting first):",
                      "  _A reason whose newest sighting is days old is draining out of "
                      "the 7-day window — a ghost, already fixed or already ended. A "
                      "reason marked LIVE was seen in the last 24 hours and is today's "
                      "problem._"]
                for pair in reasons[:12]:
                    L += pair
                if len(reasons) > 12:
                    L += [f"  - ...and {len(reasons) - 12} more distinct reason(s)"]
                L += [""]
            elif crashes or cerr:
                L += ["  ⚠️ Counters fired but NO detail rows came back -- the events "
                      "are being written without their message. That is a hole in the "
                      "eyes, not a quiet week.", ""]
        except Exception as _dex:  # noqa: BLE001 -- detail is a bonus, never a failure
            L += [f"  (crash reasons unavailable: {_dex})", ""]
    except Exception as _exc:  # noqa: BLE001
        L += ["## The week's telemetry", "", f"- (unavailable: {_exc})", ""]

    # (sh) THE ROTATION, NAMED. The 08-20 watch filed this as F2 and it was never
    # closed: the report prints sc["id"] with no course and no duplicate marker, so a
    # SKIPPED DUPLICATE reads as a missing scenario, and "order-of-operations" once
    # appeared in the skip list while also producing the night's only finding. Naming
    # every slot with its outcome makes a repeat readable AS a repeat.
    roster = result.get("roster") or []
    if roster:
        _n = lambda kind: sum(1 for r in roster if r.get("outcome") == kind)
        L += ["## The rotation tonight", "",
              f"_{len(roster)} slot(s) picked · {_n('ran')} ran · {_n('skipped')} skipped "
              f"· {_n('error')} errored · {_n('crashed')} crashed · "
              f"{_n('not reached')} never reached._", ""]
        _mark = {"ran": "✅", "skipped": "⏭️", "error": "❌", "crashed": "💥",
                 "not reached": "⬜"}
        for r in roster:
            oc = r.get("outcome") or "?"
            L += ["- " + _mark.get(oc, "·") + f" **{r.get('id')}**"
                  + (f" ({r.get('course')})" if r.get("course") else "")
                  + (" — _repeat slot_" if r.get("repeat") else "")
                  + ("" if oc == "ran" else f" — **{oc}**")
                  + (f" — {r.get('note')}" if r.get("note") else "")]
        L += [""]

    # WHAT WE DID NOT DO. A silent cap reads as "all clear".
    L += ["## What this run did not cover", ""]
    probes = result.get("probes_run") or []
    L += [f"- probes run against these lessons: {', '.join(probes) if probes else 'none'}",
          "- the server-side chat endpoint (gates, tracking) is not exercised: this "
          "harness calls the tutor directly",
          "- the rendered SCREEN is not judged here (that is screencheck.py, which runs "
          "in ruletests on every push)"]
    # (sh) A RULING THAT SILENCES FINDINGS MUST STAY VISIBLE. The reviewer refuses to
    # confirm these shapes because a person ruled on them, not because it judged them --
    # so the report says so out loud every night. If one of these ever turns out to be
    # wrong, this line is where it gets caught.
    for _r in RULED_ALLOWED:
        L += [f"- rule {_r.get('rule')}'s ruled-allowed shape ({_r.get('date')}) is "
              f"REFUTED on sight by the reviewer, by ruling and not by judgment — "
              f"{_r.get('shape')}"]
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


def write_report(data_dir, result, build="", now=None) -> str:
    """Write tonight's report and prune old ones. Returns the path, or "".

    `now` exists so tests can pin the clock (the report's date-stamped filename IS the
    restart-safety ledger `due()` reads); production callers omit it and get the real clock.
    """
    try:
        d = os.path.join(str(data_dir), REPORT_DIR_NAME)
        os.makedirs(d, exist_ok=True)
        name = (now or datetime.now(timezone.utc)).strftime("%Y-%m-%d") + ".md"
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

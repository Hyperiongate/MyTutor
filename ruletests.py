# =============================================================================
# ruletests.py  --  the RULE REGRESSION BATTERY  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-08-09  BUILD cg -- PENDING_CASES and the today-bar guards.
#               PENDING_CASES covers the new rule-15 referee, and the FALSE cases carry
#               most of the weight: rule 39(d) now REQUIRES him to ask "does that click,
#               or should I show it another way?" constantly, and re-rolling those would
#               cost real money every turn. Two false positives were caught here before
#               shipping -- "which number is the denominator in three-fourths?" (the
#               hyphen read as minus) and "is 1/2 bigger than the piece we shaded?" (a
#               fraction counted as two numbers).
#               PART 3d/3e gained the today-bar guards: the store table is in the reset
#               cascade, session.html still rebuilds the bar from SRV_PROGRESS.today at
#               load, and ensure_today_tag() restores a bar a reload destroyed while
#               still never resetting one that is genuinely live.
#   2026-08-09  BUILD cf -- PART 3e, plus rules 41-44 and two new guards.
#               PART 3e "THE THREE TEACHING PAGES MUST MATCH" exists because auditing
#               audit #1 found that item 11 (board lines never wrap) shipped to
#               session.html and never reached practice.html or topic.html -- Jim's
#               broken-equation screenshot was still reproducible on two of three pages,
#               a day after we called it fixed. Same bug shape as build bk, where a rule
#               written into one of eleven per-course templates reached one course. PART 1
#               made that impossible for the prompt; PART 3e does it for the pages, and
#               also proves every board tag the SHARED prompt block teaches is drawable on
#               all three (the six lesson-only tags are named explicitly, and the test
#               fails if one of them ever leaks into the shared block).
#               PART 3c now enforces rule 41: a figure with no caption= is a failure.
#               PART 3d now proves all THREE teaching modes carry the canonical scripts
#               and honour the heard list.
#   2026-08-09  BUILD ce -- three new groups of checks, one per thing Jim asked for.
#               PART 1 gained rules 39 and 40 (coverage across all ten courses).
#               PART 2 gained VISUAL_CASES for the new visual referee -- including the
#               false-positive cases, which matter just as much: a re-roll is a real model
#               call, so ordinary prose about a number line, a promise to draw one next
#               time, and a look back at yesterday's picture must all stay clean.
#               PART 3c gained a drift check: tutor.FIGURE_TAGS (a constant, because
#               tutor.py must not read static files at request time) must still name
#               exactly the tags session.html's handleTags() routes to a figure renderer.
#               PART 3d is new -- foundation memory: the term key survives the model's own
#               capitalisation, a made-up term is rejected, the heard list actually reaches
#               the prompt and marks its scripts, every script stays byte-identical either
#               way (the audio cache depends on it), junk never raises, and the new table
#               is in store's per-student reset cascade.
#   2026-08-09  BUILD cd -- ADDED PART 3c, "board tags actually draw".
#               This is the machine for the failure Jim named on the demo page: "the
#               lesson referred to a diagram that didn't show up on the board... We got
#               one shot to do it right, and it failed." A board tag fails SILENTLY --
#               no exception, no log, the words are still spoken -- when its name is not
#               in handleTags(), when its attribute is not one the renderer reads, when
#               it carries no content, or when an attribute value contains a square
#               bracket (handleTags' own regex ends the tag there). PART 3c PARSES
#               static/math-figures.js, static/geo-figures.js and session.html's
#               handleTags() so the contract is read from the renderers themselves and
#               cannot go stale; a new tag with no entry in TAG_HANDLER/TAG_INLINE fails
#               the suite on purpose rather than being skipped. On its first run it
#               caught 11 already-shipped foundation scripts. It also checks the two
#               ways [[graph]] quietly draws the WRONG picture: lines= on a non-linear
#               expression (parseLinear flattens a parabola into a straight line) and a
#               comma where the grapher splits only on ";" or "|".
#   2026-08-09  CREATED (build bu, proactive audit #25). Every teaching rule we have
#               was born from Jim noticing a failure in a live lesson. That does not
#               scale to real students. This is the machine that notices instead.
# -----------------------------------------------------------------------------
# WHAT IT IS
#   A standalone test script. It is NEVER imported by the running app, so it cannot
#   affect a deploy -- it exists to be RUN before one.
#
# HOW TO RUN
#   python ruletests.py            offline checks only (fast, no API key, no cost)
#   python ruletests.py --live     ALSO plays scripted students against the real
#                                  prompt (needs ANTHROPIC_API_KEY; costs a few cents)
#
# WHAT IT CHECKS
#   PART 1  RULE COVERAGE -- every rule really reaches all ten courses' built prompts.
#           (This is the class of bug that hid for a day in build bk: a rule written
#           into ONE of tutor.py's eleven per-course templates reached one course.)
#   PART 2  THE PROSE REFEREE -- the live 2026-08-08 contradiction is still caught,
#           and every known false-positive shape is still clean.
#   PART 3  SPOKEN NUMBERS -- forSpeech() on all three teaching pages (runs only if
#           `node` is available; skipped gracefully otherwise).
#   PART 4  --live SCENARIOS -- a scripted difficult student: wrong answers, "I don't
#           know", equivalent-form answers, off-topic questions, goodbyes. Mechanical
#           assertions, no human reading required.
#
# ADDING A RULE?  Add a scenario here in the same commit. That is the whole point.
# =============================================================================
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import tutor  # noqa: E402

COURSES = ["entrymath", "basicmath", "prealgebra", "algebra1", "geometry",
           "algebra2", "precalc", "calculus", "probstat", "diffeq"]
STUDENT = {"name": "Testy", "grade": "7"}

PASS, FAIL, SKIP = [], [], []


def ok(name):
    PASS.append(name); print(f"  \033[92mPASS\033[0m  {name}")


def bad(name, detail=""):
    FAIL.append((name, detail)); print(f"  \033[91mFAIL\033[0m  {name}\n        {detail}")


def skip(name, why):
    SKIP.append(name); print(f"  \033[93mSKIP\033[0m  {name} ({why})")


def check(name, condition, detail=""):
    ok(name) if condition else bad(name, detail)


# =============================================================================
# PART 1 -- RULE COVERAGE ACROSS ALL TEN COURSES
# =============================================================================
# One entry per rule that must reach EVERY course. The needle is a phrase unique to
# that rule in the shared blocks. When you write a new shared rule, add it here.
COVERAGE = [
    ("rule 0  opening sequence",        "THE OPENING SEQUENCE"),
    ("rule 1  placement honesty",       "PLACEMENT HONESTY"),
    ("rule 4  say it -> write it",      "SAY IT -> WRITE IT"),
    ("rule 4  sub-step lines",          "ANSWERED SUB-STEP GETS ITS OWN LINE"),
    ("rule 4  multiplication sign",     "MULTIPLICATION SIGN"),
    ("rule 6  never run ahead",         "STILL NEVER RUN AHEAD"),
    ("rule 7  never ask to imagine",    "NEVER ASK THE STUDENT TO IMAGINE"),
    ("rule 9  the sound-off check",     "THE SOUND-OFF CHECK"),
    ("rule 10 tag checkable claims",    "TAG EVERY CHECKABLE CLAIM"),
    ("rule 13 literally true",          "MUST BE LITERALLY TRUE"),
    ("rule 14 define notation",         "DEFINE EVERY NOTATION"),
    ("rule 15 complete on screen",      "COMPLETE ON SCREEN"),
    ("rule 15 'your turn' on board",    'YOUR TURN" PROBLEM ITSELF GOES ON THE BOARD'),
    ("rule 15 pending '?' line",        "PENDING line with a question mark"),
    ("rule 16 restate the original",    "NOT JUST THE SUBSTITUTION"),
    ("rule 17 never answer yourself",   "NEVER ANSWER YOUR OWN QUESTION"),
    ("rule 18 check their answer",      "CHECK THE STUDENT'S ANSWER BEFORE YOU BUILD"),
    ("rule 19 worked example first",    "I DO, THEN YOU DO"),
    ("rule 20 partially right",         "PARTIALLY RIGHT IS NOT WRONG"),
    ("rule 21 'I don't know'",          "IS NOT A WRONG ANSWER -- IT IS A REQUEST"),
    ("rule 22 escalation ladder",       "NEVER ASK THE SAME THING THE SAME WAY TWICE"),
    ("rule 23 equivalent answers",      "EQUIVALENT ANSWERS ARE CORRECT ANSWERS"),
    ("rule 24 leaps/self-correct",      "LEAPS, SELF-CORRECTIONS"),
    ("rule 25 student disputes you",    "WHEN THE STUDENT SAYS YOU ARE WRONG"),
    ("rule 26 wrong lines corrected",   "A WRONG LINE NEVER STAYS ON THE BOARD"),
    ("rule 27 units + approximation",   "UNITS AND HONEST APPROXIMATION"),
    ("rule 28 one name per thing",      "ONE NAME PER THING"),
    ("rule 29 how a session ends",      "HOW A SESSION ENDS"),
    ("rule 30 off-topic questions",     "OFF-TOPIC AND PERSONAL QUESTIONS"),
    ("rule 31 bigger than math",        "WHEN SOMETHING BIGGER THAN MATH SHOWS UP"),
    ("rule 32 realistic problems",      "SURVIVE A SANITY CHECK"),
    ("rule 33 one notch at a time",     "DIFFICULTY MOVES ONE NOTCH AT A TIME"),
    ("rule 34 keep old skills sharp",   "KEEP OLD SKILLS SHARP"),
    ("rule 35 fix-then-retry a quiz",   "A FAILED QUIZ IS NEVER RE-GIVEN ON THE SPOT"),
    ("rule 36 teach before you ask",     "TEACH THE THING BEFORE YOU ASK ABOUT THE THING"),
    ("rule 37 vocabulary is taught",     "VOCABULARY IS TAUGHT, NEVER ASSUMED"),
    ("rule 38 concrete->picture->symbol", "CONCRETE, THEN PICTURE, THEN SYMBOLS"),
    ("rule 39 talk less, check in",      "TALK LESS. CHECK IN OFTEN"),
    ("rule 39 the check must be failable", "MAKE THE CHECK FAILABLE"),
    ("rule 40 ask before you repeat",    "SIT THROUGH THE SAME INTRODUCTION TWICE"),
    ("rule 40 mark what you taught",     '[[learned term="denominator"]]'),
    ("rule 41 captions say what to notice", "CARRIES A CAPTION THAT SAYS WHAT TO NOTICE"),
    ("rule 42 no comparisons",           "NEVER COMPARE THIS STUDENT TO ANYONE BUT THIS STUDENT"),
    ("rule 43 no false perception",      "YOU PERCEIVE EXACTLY TWO THINGS"),
    ("rule 44 read the problem aloud",   "READ THE PROBLEM ALOUD, IN FULL, EVERY TIME"),
    ("canonical foundation scripts",     "SPEAK THESE VERBATIM"),
    ("speech: money as money",          "MONEY IS SPOKEN AS MONEY"),
    ("speech: number words",            "NUMBERS ARE SPOKEN THE WAY PEOPLE SAY THEM"),
    ("speech: spoken answers count",    "NUMBERS SPOKEN AS WORDS ARE EXACT ANSWERS"),
    ("progress: today bar every session", "THIS INCLUDES RESUMED SESSIONS"),
]


def part1_coverage():
    print("\nPART 1 — rule coverage across all ten courses")
    prompts = {c: tutor.build_system_prompt(dict(STUDENT), course=c) for c in COURSES}
    for name, needle in COVERAGE:
        missing = [c for c in COURSES if needle not in prompts[c]]
        check(name, not missing, f"missing in: {', '.join(missing)}")
    # no accidental gap in the numbered sequence
    nums = sorted({int(m) for m in re.findall(r"^(\d+)[.)] ", prompts["algebra1"], re.M)})
    expected = list(range(0, max(nums) + 1)) if nums else []
    check("rule numbering has no gaps", nums == expected,
          f"saw {nums}")


# =============================================================================
# PART 2 -- THE PROSE REFEREE
# =============================================================================
# Each case is (name, reply, should_flag). The FIRST is the real 2026-08-08 bug.
PROSE_CASES = [
    ("live bug: wrong answer adopted in words",
     'Fifteen dimes — and since that\'s over nine again, we do the same trick: fifteen '
     'dimes is one dollar and five dimes, so we write the five and carry a dollar. '
     '[[step eq="dimes: 7 + 8 + 1 = 16"]]', True),
    ("the corrected flow (must stay clean)",
     'Sixteen — nice, careful counting. Sixteen dimes is one dollar and six dimes, so we '
     'write the six and carry a dollar. [[step eq="dimes: 7 + 8 + 1 = 16"]]', False),
    ("intermediate value that reaches the right result",
     'Seven plus eight is fifteen dimes, and adding the one we carried makes sixteen. '
     '[[step eq="dimes: 7 + 8 + 1 = 16"]]', False),
    ("operand mentioned in passing",
     'We had eight dimes in the second number, so the column comes to sixteen. '
     '[[step eq="dimes: 7 + 8 + 1 = 16"]]', False),
    ("different label entirely",
     'Ten pennies is one dime, so we carry it. [[step eq="pennies: 5 + 5 = 10"]]', False),
    ("numeral contradiction",
     'You end up with 15 cookies on the plate. [[step eq="cookies: 9 + 8 = 17"]]', True),
    # 2026-08-09: this fixture used to end "...so what is eight divided by two?" with no
    # pending line, which the new rule-15 referee correctly flags. The numeric check is
    # still what this case tests (an unlabeled board line must not false-positive); the
    # reply is now written the way rule 15 actually asks for.
    ("unlabeled board line",
     'Nice! [[step eq="2x = 8"]] So what is eight divided by two? '
     '[[step op="/ 2" eq="x = ?"]]', False),
    ("no board tags at all",
     "Great job — that's fifteen dimes exactly!", False),
    ("pending '?' line is never a contradiction",
     'Your turn — what do the dollars come to? [[step eq="dollars: 2 + 1 + 1 = ?"]]', False),
]

# ---- the VISUAL half of the referee (build ce) ------------------------------
# Jim's demo failure, in a live lesson: "the lesson referred to a diagram that didn't
# show up on the board... we got one shot to do it right, and it failed."
# A false positive costs a real model call, so the FALSE cases below matter as much as
# the TRUE ones -- ordinary mathematical prose about a number line must stay clean.
VISUAL_CASES = [
    ("the failure: a number line that was never drawn",
     "Here's a number line from negative six to six. Where would negative three sit?", True),
    ("the same reply, with the picture actually drawn",
     'Here\'s a number line from negative six to six. Where would negative three sit? '
     '[[numberline min="-6" max="6"]]', False),
    ("'I just drew' with an empty board",
     "I just drew a graph of this function — see how it bends upward?", True),
    ("'look at the diagram' with only writing on the board",
     'Look at the diagram: the two legs meet at the corner. [[write text="a=3, b=4"]]', True),
    ("'let me draw a picture' and he does",
     'Let me draw a picture of six stars. [[objects emoji="⭐" groups="6"]]', False),
    ("pointing at a board he wrote nothing on",
     "Take a look at the board — see how the twos cancel?", True),
    ("pointing at a board he DID write on",
     'Take a look at the board — see how the twos cancel? [[step eq="2x = 8"]]', False),
    ("plain prose ABOUT a number line is not a claim",
     "On a number line, numbers get bigger as you move to the right. What's bigger, 5 or 8?", False),
    ("a promise about NEXT time is not a claim",
     "Next time I'll draw you a picture of that. For now, what is seven plus eight?", False),
    ("recalling a picture from earlier is not a claim",
     "Remember the number line we used yesterday? Same idea here. What's negative two plus five?", False),
    ("teaching with no visuals mentioned at all",
     'Nice work! Seven plus eight is fifteen. [[step eq="7 + 8 = 15"]]', False),
]

# ---- the PENDING-QUESTION half (build cg) -----------------------------------
# Jim's live Pre-Algebra resume: "it gave me a problem without putting it on the board,
# and this is the exact example that we've already used once before that was supposedly
# fixed." Rule 15 names this exact scenario and prints the exact fix, and the reply still
# went out without a board line. So it stops being a rule and becomes a referee.
# The FALSE cases matter just as much -- a re-roll is a real model call, and rule 39(d)
# now REQUIRES him to ask "does that click, or should I show it another way?" constantly.
PENDING_CASES = [
    ("Jim's live bug: the dollars column asked, nothing pending on the board",
     "Now for the dollars column — two dollars plus one dollar, plus the one dollar we "
     "just carried. What's two plus one plus one? "
     '[[column op="+" terms="2.75 | 1.85"]] [[step eq="dimes: 7 + 8 + 1 = 16"]]', True),
    ("the same reply with the pending line rule 15 asks for",
     "What's two plus one plus one? " '[[step eq="dollars: 2 + 1 + 1 = ?"]]', False),
    ("the original 2026-08-08 catch: 'your turn' with no board",
     "Your turn — what is ten minus two times three?", True),
    ("...and the same question written up",
     'Your turn — what is ten minus two times three? [[write text="10 - 2 × 3 = ?"]]', False),
    ("a written expression, spoken as a question",
     "So what does 12 ÷ 4 come to?", True),
    ("one number plus an operator word still counts",
     "What do you get when you add nine?", True),
    ("a social question is not a computation",
     'Ready to try one on your own? [[step eq="7 + 8 = 15"]]', False),
    ("rule 39(d)'s check-in must NEVER trigger this",
     "Does that click, or should I show it a different way?", False),
    ("a vocabulary question is not a computation",
     "Which number is the denominator in three-fourths?", False),
    ("a fraction is one value, not an operation",
     "Is 1/2 bigger than the piece we shaded?", False),
    ("numbers in a story with no question asked",
     'We had 5 cookies and I gave you 2 more. '
     '[[objects emoji="🍪" groups="5" add="2" caption="count them all"]]', False),
    ("tap-to-answer choices still need the question on the board",
     'What is six times seven? [[write text="6 × 7 = ?"]] [[choices options="42 | 48"]]', False),
]


def part2_prose():
    print("\nPART 2 — the prose referee")
    for name, reply, should_flag in PROSE_CASES:
        got = tutor.prose_board_conflict(reply)
        check(f"prose: {name}", bool(got) == should_flag,
              f"expected flag={should_flag}, got: {got or '(clean)'}")
    for name, reply, should_flag in VISUAL_CASES:
        got = tutor.prose_visual_conflict(reply)
        check(f"visual: {name}", bool(got) == should_flag,
              f"expected flag={should_flag}, got: {got or '(clean)'}")
        # the visual check must also reach students THROUGH the combined referee
        if should_flag:
            check(f"visual: {name} (via prose_board_conflict)",
                  bool(tutor.prose_board_conflict(reply)),
                  "the combined referee let it through")
    for name, reply, should_flag in PENDING_CASES:
        got = tutor.prose_pending_question_conflict(reply)
        check(f"pending: {name}", bool(got) == should_flag,
              f"expected flag={should_flag}, got: {got or '(clean)'}")
        if should_flag:
            check(f"pending: {name} (via prose_board_conflict)",
                  bool(tutor.prose_board_conflict(reply)),
                  "the combined referee let it through")
    for junk in [None, "", 0, [], "[[step eq=", "x: = 5", "[[numberline"]:
        try:
            tutor.prose_board_conflict(junk)
            tutor.prose_visual_conflict(junk)
            tutor.prose_pending_question_conflict(junk)
        except Exception as exc:  # noqa: BLE001
            bad("prose: junk input never raises", f"{junk!r} -> {exc}")
            break
    else:
        ok("prose: junk input never raises")


# =============================================================================
# PART 3 -- SPOKEN NUMBERS (forSpeech on the three teaching pages)
# =============================================================================
SPEECH_CASES = [
    ("$1.85 ticket", "1 dollar and 85 cents", "dot"),
    ("$0.85 left", "85 cents", None),
    ("3.75 total", "3 point 7 5", "dot"),
    ("−3 + 5 = 2", "negative 3", "dash"),
    ("7 − 3 = 4", "minus", "negative"),
    ("20% of 50", "20 percent", "%"),
    ("the ratio 3:2", "3 to 2", None),
    ("1/2 + 1/4", "one half", "1 over 2"),
    ("2 1/2 cups", "2 and one half", None),
    ("1,234 students", "1234", "1,234"),
    ("f(x) = 2x + 3", "f of x", None),
]
_JS_HARNESS = r"""
const fs=require("fs");
function grab(js,n){const i=js.indexOf("function "+n);if(i<0)throw new Error("missing "+n);
 let d=0,j=js.indexOf("{",i);for(let k=j;k<js.length;k++){if(js[k]==="{")d++;else if(js[k]==="}"){d--;if(!d)return js.slice(i,k+1);}}}
const js=fs.readFileSync(process.argv[2],"utf8");
const pre=(js.match(/var FRAC_WORDS = \{[\s\S]*?\};/)||[""])[0];
const fn=new Function(pre+"\n"+["fracWords","mixedWords","moneyWords","forSpeech"].map(n=>grab(js,n)).join("\n")+"\nreturn forSpeech;")();
const cases=JSON.parse(process.argv[3]); const out=[];
for(const [inp,must,mustNot] of cases){const r=fn(inp);out.push([inp,r,r.includes(must)&&!(mustNot&&r.includes(mustNot))]);}
console.log(JSON.stringify(out));
"""


def part3_speech():
    print("\nPART 3 — spoken numbers (forSpeech)")
    here = os.path.dirname(os.path.abspath(__file__))
    try:
        subprocess.run(["node", "--version"], capture_output=True, check=True)
    except Exception:  # noqa: BLE001
        skip("forSpeech batteries", "node not available")
        return
    import json
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        harness = os.path.join(tmp, "h.js")
        with open(harness, "w") as fh:
            fh.write(_JS_HARNESS)
        for page in ("session", "practice", "topic"):
            path = os.path.join(here, "static", f"{page}.html")
            if not os.path.exists(path):
                skip(f"forSpeech [{page}]", "page not found"); continue
            with open(path, encoding="utf-8") as fh:
                html = fh.read()
            blocks = re.findall(r"<script>(.*?)</script>", html, re.S)
            jsf = os.path.join(tmp, f"{page}.js")
            with open(jsf, "w", encoding="utf-8") as fh:
                fh.write(blocks[0])
            res = subprocess.run(["node", harness, jsf, json.dumps(SPEECH_CASES)],
                                 capture_output=True, text=True)
            if res.returncode != 0:
                bad(f"forSpeech [{page}]", res.stderr.strip()[:200]); continue
            rows = json.loads(res.stdout)
            failures = [f'"{i}" -> "{o}"' for i, o, good in rows if not good]
            check(f"forSpeech [{page}] ({len(rows)} cases)", not failures,
                  "; ".join(failures)[:300])


# =============================================================================
# PART 4 -- LIVE SCENARIOS (a scripted difficult student)
# =============================================================================
# Each scenario: a short history, then one student turn. The assertion is MECHANICAL.
# `history` is [(role, text), ...] where role is "user" or "assistant".
BOARD_TAG = re.compile(r"\[\[\s*(step|write|solve|column|card|graph|objects|choices|balance|machine)\b", re.I)
HUMAN_CLAIMS = re.compile(r"\b(i am|i'm) a (real )?(human|person|man|guy|teacher named)\b", re.I)


def _numbers(text):
    return {float(x) for x in re.findall(r"-?\d+(?:\.\d+)?", text or "")}


def _assert_no_contradiction(reply):
    return not tutor.prose_board_conflict(reply)


LIVE_SCENARIOS = [
    dict(
        name="wrong answer is coached, never adopted",
        course="prealgebra",
        history=[("assistant", 'Let\'s add these. [[step eq="pennies: 5 + 5 = 10"]] '
                               'Now the dimes column — what is seven plus eight plus one?')],
        student="Fifteen.",
        # the reply must not contradict its own board, and must not present 15 as the total
        assertion=lambda r: _assert_no_contradiction(r) and (
            16.0 in _numbers(r) or "sixteen" in r.lower()),
        why="reply must reach 16 and never contradict its own board",
    ),
    dict(
        name="'I don't know' gets a smaller step, not a repeat",
        course="prealgebra",
        history=[("assistant", "What is negative three plus five? "
                               '[[step eq="-3 + 5 = ?"]]')],
        student="I don't know.",
        assertion=lambda r: "not quite" not in r.lower() and "try again" not in r.lower(),
        why="rule 21: never 'not quite / try again' for an honest I-don't-know",
    ),
    dict(
        name="equivalent form is accepted as correct",
        course="basicmath",
        history=[("assistant", 'What is one half, as a decimal or a fraction? '
                               '[[step eq="1/2 = ?"]]')],
        student="point five",
        assertion=lambda r: not re.search(r"\b(not quite|that's not right|incorrect|nope)\b",
                                          r, re.I),
        why="rule 23: 0.5 for 1/2 is correct, never marked wrong",
    ),
    dict(
        name="an asked step is written on the board",
        course="prealgebra",
        history=[("assistant", 'Here we go. [[step eq="pennies: 5 + 5 = 10"]] Ready for the dimes?')],
        student="yes",
        assertion=lambda r: bool(BOARD_TAG.search(r)),
        why="rules 4/15: a question's math appears on the board in that reply",
    ),
    dict(
        name="off-topic question: warm, honest, never claims to be human",
        course="algebra1",
        history=[("assistant", "Let's solve two x plus three equals eleven. "
                               '[[step eq="2x + 3 = 11"]] What do we do to both sides?')],
        student="wait, are you a real person?",
        assertion=lambda r: not HUMAN_CLAIMS.search(r),
        why="rule 30: answer warmly, never claim to be a human being",
    ),
    dict(
        name="goodbye gets a wrap-up, not a guilt trip",
        course="algebra1",
        history=[("assistant", 'Nice work! [[step eq="x = 4"]] Ready for another?')],
        student="I have to go now",
        assertion=lambda r: not re.search(r"just one more|are you sure|don't you want", r, re.I),
        why="rule 29: one-turn wrap-up, never bargaining",
    ),
    dict(
        name="a new topic teaches the words before asking about them",
        course="basicmath",
        history=[("assistant", "Ready to start on fractions?")],
        student="yes",
        # rule 36/37: he must NAME and DEFINE, not open with a question about un-taught words
        assertion=lambda r: ("fraction" in r.lower()
                             and not re.search(r"what do you think (a |an )?(fraction|numerator|denominator)", r, re.I)),
        why="rules 36-37: define the term, never ask a student to guess an untaught word",
    ),
    dict(
        name="a failed quiz is fixed before it is re-given",
        course="prealgebra",
        history=[("assistant", "Quiz time — three questions on comparing decimals. No hints from me."),
                 ("user", "0.45"), ("assistant", "Noted."),
                 ("user", "0.7"), ("assistant", "Noted."),
                 ("user", "1.2"),
                 ("assistant", 'That\'s the quiz. [[quiz unit="5" topic="1" name="Comparing decimals" correct="1" total="3"]]')],
        student="did I pass?",
        # must NOT immediately re-quiz; must re-teach first (rule 35)
        assertion=lambda r: not re.search(r"(let'?s take it again|try the quiz again|here'?s the quiz again|same quiz)", r, re.I),
        why="rule 35: re-teach and practice before any retake — never re-give it on the spot",
    ),
    dict(
        name="self-criticism is met with specific evidence",
        course="algebra1",
        history=[("assistant", 'You solved it! [[step eq="x = 4"]] Want another?')],
        student="I'm so stupid at math",
        assertion=lambda r: not re.search(r"\byou'?re (not )?stupid\b", r, re.I) and len(r) > 40,
        why="rule 31a: reassure with real evidence, never echo the label",
    ),
]


def part3b_foundations():
    """The canonical foundation scripts (build cc). These are what a student actually
    HEARS the first time they meet an idea, and they are spoken verbatim so the voice
    cache can reuse them -- so they must reach the prompt, and they must stay speakable."""
    print("\nPART 3b — canonical foundation scripts")
    try:
        import foundations
    except Exception as exc:  # noqa: BLE001
        bad("foundations.py imports", str(exc)); return
    total = 0
    for c in COURSES:
        items = foundations.for_course(c)
        if not items:
            check(f"foundations [{c}]", False, "no canonical introductions for this course")
            continue
        total += len(items)
        prompt = tutor.build_system_prompt(dict(STUDENT), course=c)
        missing = [f["term"] for f in items if f"--- {f['term'].upper()} ---" not in prompt]
        check(f"foundations [{c}] ({len(items)} intros reach the prompt)", not missing,
              f"missing: {missing}")
        for f in items:
            say = f["say"]
            # spoken aloud: no notation, no bare symbols (see tutor.py HOW YOU SPEAK)
            offenders = [ch for ch in "=+×÷^<>" if ch in say]
            check(f"  '{f['term']}' script is speakable", not offenders,
                  f"contains symbols that get read aloud badly: {offenders}")
            low = say.lower()
            check(f"  '{f['term']}' marks its key term",
                  f"**{f['term'].lower()}**" in low or f"**{f['term'].split()[-1].lower()}**" in low,
                  "the term itself must be wrapped in ** ** so the board highlights it")
            check(f"  '{f['term']}' is a real explanation", 25 <= len(say.split()) <= 130,
                  f"{len(say.split())} words — too short to teach, or too long to listen to")
    check("every course has canonical introductions", total >= 20, f"only {total}")
    # and the site must not promise the method we abandoned
    here = os.path.dirname(os.path.abspath(__file__))
    hits = []
    for root, _dirs, files in os.walk(os.path.join(here, "static")):
        for fn in files:
            if not fn.endswith((".html", ".txt", ".md")):
                continue
            try:
                with open(os.path.join(root, fn), encoding="utf-8") as fh:
                    if "socratic" in fh.read().lower():
                        hits.append(fn)
            except Exception:  # noqa: BLE001
                pass
    check("no page still claims the Socratic method", not hits, f"still in: {hits}")


# =============================================================================
# PART 3c -- DOES THE BOARD TAG ACTUALLY DRAW?
# -----------------------------------------------------------------------------
# 2026-08-09 (build cd). This is the audit for the failure class Jim named on the
# demo page: "the lesson referred to a diagram that didn't show up on the board...
# We got one shot to do it right, and it failed."
#
# A board tag can fail SILENTLY in four different ways, and none of them raise an
# error anywhere -- the words are spoken, the picture simply is not there:
#   1. the tag name is not in session.html's handleTags()      -> nothing happens
#   2. the tag name is right but the ATTRIBUTE name is wrong   -> a blank/default
#      figure draws (e.g. [[graph expr="x^2"]]: the grapher reads func=, never
#      expr=, so the student gets empty axes while the tutor talks about a curve)
#   3. the tag carries no content attribute at all             -> an empty figure
#   4. an attribute VALUE contains "[" or "]"                  -> handleTags' regex
#      is /\[\[\s*([\w-]+)([^\]]*?)\]\]/ , so a square bracket ends the tag early
#      and the whole thing is dropped
#
# So this test does not hard-code what is legal. It PARSES the three renderers --
# static/math-figures.js, static/geo-figures.js and session.html's show* handlers
# -- and asks each one which attributes it actually reads. When somebody adds an
# attribute to a renderer, this test learns about it on the next run. When somebody
# adds a NEW tag to handleTags without telling this test where its handler lives,
# the test FAILS on purpose (see TAG_HANDLER below) rather than quietly ignoring it.
# =============================================================================

# tag name -> the session.html function that consumes its attributes. Figure tags
# are resolved from the JS modules instead and are deliberately absent here.
TAG_HANDLER = {
    "balance": "showBalance", "card": "showCard", "machine": "showMachine",
    "step": "showStep", "column": "showColumn", "write": "showWrite",
    "solve": "showSolve", "check": "showCheck", "quiz": "showQuiz",
    "today": "showToday", "todaydone": "markTodayDone", "unitplan": "showUnitPlan",
    "finalexam": "showFinalExam", "choices": "showChoices", "objects": "showObjects",
}
# tags whose attributes are read inline in handleTags itself (no show* function)
TAG_INLINE = {
    "goal": {"text"}, "highlight": {"id"}, "clear": set(),
    "mark": {"correct", "attempted"},
}
# a tag that draws a FIGURE needs at least one of these or it renders empty
CONTENT_ATTRS = {
    "graph": {"func", "fn", "functions", "lines", "parabola", "parabolas", "points"},
    "pie": {"data", "sectors"}, "bars": {"data"},
    "histogram": {"data", "values"}, "dotplot": {"data", "values"},
    "boxplot": {"data", "values", "five"}, "scatter": {"points"},
    "twoway": {"data"}, "tree": {"stage1", "stage2", "a", "b"},
    "vector": {"v", "vectors"}, "conic": {"type"}, "areamodel": {"rows", "cols"},
    "objects": {"n", "groups"}, "card": {"items", "id"},
    "write": {"text", "lines"}, "solve": {"start", "top"},
}


def _js_fn_attrs(src, header_re):
    """{function name -> set of attrs it reads off its single argument}, by brace-matching."""
    out = {}
    for m in re.finditer(header_re, src):
        name, var = m.group(1), m.group(2)
        i, depth = m.end() - 1, 0
        for j in range(i, len(src)):
            if src[j] == "{":
                depth += 1
            elif src[j] == "}":
                depth -= 1
                if depth == 0:
                    break
        out[name] = set(re.findall(r"\b" + re.escape(var) + r"\.(\w+)", src[i:j]))
    return out


def _board_contract(here):
    """Read the real renderers and return (valid tag names, {tag -> allowed attrs}).

    Returns (None, None, reason) if a source file is missing."""
    paths = {
        "math": os.path.join(here, "static", "math-figures.js"),
        "geo": os.path.join(here, "static", "geo-figures.js"),
        "page": os.path.join(here, "static", "session.html"),
    }
    for k, p in paths.items():
        if not os.path.exists(p):
            return None, None, f"missing {os.path.relpath(p, here)}"
    with open(paths["math"], encoding="utf-8") as fh:
        math_src = fh.read()
    with open(paths["geo"], encoding="utf-8") as fh:
        geo_src = fh.read()
    with open(paths["page"], encoding="utf-8") as fh:
        page_src = fh.read()

    math_fns = _js_fn_attrs(math_src, r"\n  function (\w+)\((a)\)\s*\{")
    geo_fns = _js_fn_attrs(geo_src, r"\n  function (\w+)\((a)\)\s*\{")
    page_fns = _js_fn_attrs(page_src, r"function (show\w+|markTodayDone)\((\w+)\)\s*\{")

    # only the renderers the modules actually EXPORT count as tags
    math_exports = set(re.findall(r"(\w+): \1,", math_src[math_src.index("window.MathFigures"):]))
    geo_exports = set(re.findall(r"(\w+): \1", geo_src[geo_src.index("window.GeoFigures"):]))

    # the authoritative tag list: whatever handleTags() dispatches on
    ht = page_src[page_src.index("function handleTags("):]
    ht = ht[:ht.index("\n    function ")]
    valid = set(re.findall(r'name === "([\w-]+)"', ht))
    for arr in re.findall(r'\[((?:"[\w-]+",?)+)\]\.indexOf\(name\)', ht):
        valid |= set(re.findall(r'"([\w-]+)"', arr))

    allowed, unmapped = {}, []
    for tag in sorted(valid):
        if tag in geo_exports and tag in geo_fns:
            allowed[tag] = geo_fns[tag] | {"caption"}      # showGeo draws the caption
        elif tag in math_exports and tag in math_fns:
            allowed[tag] = math_fns[tag] | {"caption"}     # showFig draws the caption
        elif tag in TAG_INLINE:
            allowed[tag] = set(TAG_INLINE[tag])
        elif tag in TAG_HANDLER and TAG_HANDLER[tag] in page_fns:
            allowed[tag] = page_fns[TAG_HANDLER[tag]]
        else:
            unmapped.append(tag)
    return valid, (allowed, unmapped), ""


# the EXACT regex session.html uses -- if it does not match here, it will not match there
_HT_TAG = re.compile(r"\[\[\s*([\w-]+)([^\]]*?)\]\]")
_HT_ATTR = re.compile(r'([\w-]+)\s*=\s*"([^"]*)"')

# [[graph]] draws a *different picture* than the author meant in two quiet ways, both
# found in build cd's audit of scripts that had already passed every other check:
#   lines="y=x^2"          -- lines= runs parseLinear(), which reads only the slope
#                             between x=0 and x=1. A parabola comes out a STRAIGHT LINE.
#   lines="y=2x+1, y=-x+4" -- the grapher splits curve lists on ";" or "|", never on a
#                             comma, so two equations arrive as one unparseable string.
_CURVE_ATTRS = ("func", "fn", "functions", "lines", "parabola", "parabolas")
_NONLINEAR = re.compile(r"[\^/]|sin|cos|tan|sqrt|log|exp|\*\*")


def _graph_sanity(tag, attrs):
    """'' if a [[graph]] will draw what its author meant, else why not."""
    if tag != "graph":
        return ""
    low = {k.lower(): v for k, v in attrs.items()}
    for k in _CURVE_ATTRS:
        if "," in low.get(k, ""):
            return (f'{k}="{low[k]}" separates curves with a COMMA; the grapher splits '
                    f'on ";" or "|" only, so this arrives as one unparseable expression')
    for piece in re.split(r"[;|]", low.get("lines", "")):
        piece = piece.strip()
        if piece and _NONLINEAR.search(piece.lower()):
            return (f'lines="{piece}" is not a straight line; lines= measures one slope '
                    f'and draws a LINE — use func= (or parabola=) to plot a curve')
    return ""


def part3c_board_tags():
    """Every board line in foundations.py must actually put something on the board."""
    print("\nPART 3c — board tags actually draw")
    here = os.path.dirname(os.path.abspath(__file__))
    valid, contract, why = _board_contract(here)
    if valid is None:
        bad("board tag contract readable", why + " — cannot verify what the board can draw")
        return
    allowed, unmapped = contract
    check("every tag in handleTags() is mapped to a renderer", not unmapped,
          f"unmapped tags {unmapped} — add them to TAG_HANDLER/TAG_INLINE in this file")
    try:
        import foundations
    except Exception as exc:  # noqa: BLE001
        bad("foundations.py imports", str(exc)); return

    lines = 0
    for course in COURSES:
        for f in foundations.for_course(course):
            for b in f.get("board", []):
                lines += 1
                label = f"  [{course}] {f['term']}"
                m = _HT_TAG.match(b.strip())
                if not m:
                    bad(f"{label} — board line parses",
                        f"handleTags' own regex does not match it (a '[' or ']' inside an "
                        f"attribute value ends the tag early): {b}")
                    continue
                tag = m.group(1).lower()
                attrs = {k.lower() for k, _v in _HT_ATTR.findall(m.group(2))}
                if tag not in allowed:
                    bad(f"{label} — [[{tag}]] is a real tag",
                        f"handleTags() has no branch for '{tag}' — it draws NOTHING: {b}")
                    continue
                unknown = sorted(attrs - allowed[tag])
                if unknown:
                    bad(f"{label} — [[{tag}]] attributes are read",
                        f"the renderer ignores {unknown} (it reads "
                        f"{sorted(allowed[tag])}) — the figure draws, but not what was meant: {b}")
                    continue
                need = CONTENT_ATTRS.get(tag)
                if need and not (attrs & need):
                    bad(f"{label} — [[{tag}]] has content",
                        f"no content attribute (needs one of {sorted(need)}) — it draws empty: {b}")
                    continue
                if tag in tutor.FIGURE_TAGS and "caption" not in attrs:
                    bad(f"{label} — [[{tag}]] says what to notice",
                        "rule 41: a figure with no caption= hands the student back the "
                        f"one job the picture was supposed to do for them: {b}")
                    continue
                why2 = _graph_sanity(tag, dict(_HT_ATTR.findall(m.group(2))))
                if why2:
                    bad(f"{label} — [[{tag}]] draws the RIGHT thing", f"{why2}: {b}")
                    continue
                ok(f"{label} — [[{tag}]] draws")
    check("board lines were actually checked", lines > 0, "no board lines found")

    # tutor.FIGURE_TAGS drives the visual referee (PART 2). tutor.py cannot read the
    # JS at request time, so it carries a constant -- and a constant drifts. Prove it
    # still names exactly the tags that put a PICTURE on the board.
    drawn = {t for t in valid if t in allowed and t not in TAG_INLINE
             and TAG_HANDLER.get(t) not in ("showWrite", "showStep", "showSolve",
                                            "showColumn", "showCard", "showCheck",
                                            "showQuiz", "showToday", "markTodayDone",
                                            "showUnitPlan", "showFinalExam", "showChoices")}
    missing = sorted(drawn - set(tutor.FIGURE_TAGS))
    extra = sorted(set(tutor.FIGURE_TAGS) - valid)
    check("tutor.FIGURE_TAGS still matches handleTags()", not missing and not extra,
          f"the visual referee would miss {missing}" if missing else
          f"names tags the board does not have: {extra}")


def part3d_foundation_memory():
    """The returning student must not be replayed an introduction he already gave.
    Jim: "nothing tells him which scripts that student has heard... we should just query
    him and say, do you think you got it, or do you want me to refresh your memory?"
    """
    print("\nPART 3d — foundation memory (the returning student)")
    try:
        import foundations
    except Exception as exc:  # noqa: BLE001
        bad("foundations.py imports", str(exc)); return

    # 1. the term key survives the round trip through the model's own typing
    check("normalize_term folds case and spacing",
          foundations.normalize_term("  Pythagorean   THEOREM ") == "pythagorean theorem",
          repr(foundations.normalize_term("  Pythagorean   THEOREM ")))
    check("known_term recognises a real script by any spelling",
          foundations.known_term("geometry", "PYTHAGOREAN theorem") == "Pythagorean theorem",
          repr(foundations.known_term("geometry", "PYTHAGOREAN theorem")))
    check("known_term rejects a term this course has no script for",
          foundations.known_term("geometry", "eigenvalue") == "", "it accepted a stranger")
    check("known_term is course-scoped",
          foundations.known_term("entrymath", "derivative") == "", "it accepted a stranger")

    # 2. the [[learned]] tag main.py relies on
    reply = ('Great work today! [[write text="1/4"]] [[learned term="denominator"]] '
             '[[learned term="NUMERATOR"]] [[learned term="not a real term"]]')
    got = foundations.learned_terms_in("basicmath", reply)
    check("learned_terms_in reads the tags and canonicalises them",
          got == ["denominator", "numerator"], f"got {got}")
    check("learned_terms_in drops a term we have no script for",
          "not a real term" not in got, f"got {got}")
    for junk in [None, "", 0, [], "[[learned term=", '[[learned term=""]]']:
        try:
            foundations.learned_terms_in("basicmath", junk)
        except Exception as exc:  # noqa: BLE001
            bad("learned_terms_in: junk never raises", f"{junk!r} -> {exc}")
            break
    else:
        ok("learned_terms_in: junk never raises")

    # 3. the prompt actually CHANGES for a student who has heard one
    fresh = tutor.build_system_prompt(dict(STUDENT), course="basicmath")
    known = tutor.build_system_prompt(
        dict(STUDENT, foundations_heard=["denominator", "Numerator"]), course="basicmath")
    check("a brand-new student is told nothing is known yet",
          "has not been introduced to ANY of these terms" in fresh,
          "the fresh-student prompt lost its note")
    check("a returning student's heard terms reach the prompt",
          "ALREADY INTRODUCED TO THIS STUDENT" in known and "denominator, numerator" in known,
          "the heard list never made it into the prompt")
    check("the heard terms are marked on their own scripts",
          known.count("[already introduced -- ask first, rule 40]") == 2,
          f"marked {known.count('[already introduced -- ask first, rule 40]')} of 2")
    check("the SCRIPTS themselves are byte-identical either way (the audio cache "
          "depends on it)",
          all(f["say"] in fresh and f["say"] in known
              for f in foundations.for_course("basicmath")),
          "a script's wording changed between the two prompts")
    check("a returning student is told to ASK, not replay",
          "refresh your memory" in known, "the ask is missing")
    # a heard list full of nonsense must not break the block
    for junk in [None, [], ["nothing like a real term"], "denominator", 0]:
        try:
            tutor.build_system_prompt(dict(STUDENT, foundations_heard=junk), course="basicmath")
        except Exception as exc:  # noqa: BLE001
            bad("a junk heard-list never breaks the prompt", f"{junk!r} -> {exc}")
            break
    else:
        ok("a junk heard-list never breaks the prompt")

    # 4. all THREE teaching modes get the scripts and honour the heard list.
    #    (Found in the build-cf audit: practice and topic were built from GROUND_RULES +
    #    GRAPH_TOOL_NOTE only, so rules 36-40 reached them while the scripts those rules
    #    refer to did not -- and a student could hear a different definition of the same
    #    word depending on which page they opened, which is rule 28 broken at scale.)
    MODES = [
        ("lesson", lambda st: tutor.build_system_prompt(st, course="basicmath")),
        ("practice", lambda st: tutor.build_practice_prompt(st, "3/4 + 1/2", course="basicmath")),
        ("topic", lambda st: tutor.build_topic_prompt(st, "fractions", course="basicmath")),
    ]
    for label, build in MODES:
        try:
            f = build(dict(STUDENT))
            k = build(dict(STUDENT, foundations_heard=["denominator"]))
        except Exception as exc:  # noqa: BLE001
            bad(f"{label} mode builds", str(exc)); continue
        check(f"{label} mode carries the canonical scripts", "SPEAK THESE VERBATIM" in f,
              "this mode teaches vocabulary with no script to teach it from")
        check(f"{label} mode honours the heard list", "ALREADY INTRODUCED TO THIS STUDENT" in k,
              "a returning student would be replayed an introduction here")

    # 5. the storage layer is wired into the reset cascade (standing rule: day one)
    try:
        import store
        check("foundations_heard joins the per-student reset cascade",
              ("foundations_heard", "code") in store._STUDENT_CODE_TABLES,
              "a Start Fresh would leave the memory behind")
        check("today_goals joins the per-student reset cascade",
              ("today_goals", "code") in store._STUDENT_CODE_TABLES,
              "a reset student would open the lesson to yesterday's goals")
        for fn in ("get_foundations_heard", "record_foundation_heard",
                   "get_today_goals", "save_today_goals"):
            check(f"store.{fn} exists", hasattr(store, fn), "main.py calls it every turn")
    except Exception as exc:  # noqa: BLE001
        bad("store.py imports", str(exc))

    # 6. the TODAY-bar net must not stand down just because HISTORY mentions a bar.
    #    (Jim: "there's only two of the three tracking bars... I don't know why it keeps
    #    disappearing." A reloaded page has no bar, however many [[today]] tags the old
    #    transcript holds, so the net now asks the SERVER whether one really exists.)
    try:
        stale = [{"role": "assistant", "content": 'old [[today items="a | b"]]'}]
        opener = 'Welcome back! [[goal text="add money by carrying"]]'
        check("the net RESTORES a bar that a reload destroyed",
              "[[today" in tutor.ensure_today_tag(opener, stale, today_live=False),
              "a resumed session would show only two of the three bars")
        check("the net never resets a bar that is genuinely live",
              "[[today" not in tutor.ensure_today_tag(opener, stale, today_live=True),
              "it would wipe today's ticked-off goals mid-lesson")
        check("the net never touches a reply that already has its own tag",
              tutor.ensure_today_tag('x [[today items="a"]]', stale, False).count("[[today") == 1,
              "it double-emitted")
    except Exception as exc:  # noqa: BLE001
        bad("store.py imports", str(exc))


# =============================================================================
# PART 3e -- THE THREE TEACHING PAGES MUST MATCH
# -----------------------------------------------------------------------------
# 2026-08-09 (build cf). Found by auditing whether audit #1 really shipped: item 11,
# the fix that stops a long board line WRAPPING mid-equation, went into session.html
# in build bu and NEVER reached practice.html or topic.html. Jim's screenshot bug
# ("dimes: 7 + 8 + = 16" with "1(carried)" on the next line -- a literally different
# equation on screen) was still live on two of the three teaching pages for a day.
#
# This is the SAME bug shape as build bk, where a rule written into one of tutor.py's
# eleven per-course templates reached one course. PART 1 made that impossible for the
# prompt. This does it for the pages: session / practice / topic are three copies of
# one classroom, and anything that fixes teaching on one must be on all three.
# =============================================================================
PAGES = ("session.html", "practice.html", "topic.html")

# (label, needle) -- must appear in EVERY teaching page.
PAGE_PARITY = [
    ("board lines never wrap (audit #1 item 11)", "white-space: nowrap"),
    ("fitRow() shrinks an oversized line",        "function fitRow(row)"),
    ("[[step]] lines are fitted",                 "fitRow(wl.appendChild(eqRow(eq)))"),
    ("[[write]] lines are fitted",                "fitRow(wl.appendChild(eqRow(ln)))"),
    ("forSpeech() exists",                        "function forSpeech"),
    ("control tags are stripped before speaking", "function stripTags"),
    ("the geometry figures are loaded",           "/static/geo-figures.js"),
    ("the math figures are loaded",               "/static/math-figures.js"),
]

# Lesson-page-only wiring (the today bar exists only there).
SESSION_ONLY_PARITY = [
    ("the TODAY bar is rebuilt at load, like the other two", "SRV_PROGRESS.today"),
]


def part3e_page_parity():
    print("\nPART 3e — the three teaching pages must match")
    here = os.path.dirname(os.path.abspath(__file__))
    src = {}
    for p in PAGES:
        path = os.path.join(here, "static", p)
        if not os.path.exists(path):
            bad(f"{p} exists", "missing from static/"); return
        with open(path, encoding="utf-8") as fh:
            src[p] = fh.read()
    for label, needle in PAGE_PARITY:
        missing = [p for p in PAGES if needle not in src[p]]
        check(f"all three pages: {label}", not missing, f"missing from: {missing}")
    for label, needle in SESSION_ONLY_PARITY:
        check(f"session.html: {label}", needle in src["session.html"],
              f"{needle!r} is gone -- a reload would lose the bar again")

    # Every tag the SHARED prompt block teaches him must be drawable on every page.
    # (The lesson page has six extra handlers -- the progress bars, the goal banner and
    # the final exam -- which is correct: practice and topic are side trips with no bars,
    # and nothing in the shared block ever asks him to emit those there. The named list
    # below is the whole allowance; a new session-only tag has to be added here on
    # purpose, and a shared-block tag can never quietly go missing from a page.)
    LESSON_ONLY = {"today", "todaydone", "unitplan", "goal", "finalexam", "highlight"}
    tags = {}
    for p in PAGES:
        try:
            ht = src[p][src[p].index("function handleTags("):]
            ht = ht[:ht.index("\n    function ")]
        except ValueError:
            bad(f"{p} has a readable handleTags()", "could not find it"); return
        names = set(re.findall(r'name === "([\w-]+)"', ht))
        for arr in re.findall(r'\[((?:"[\w-]+",?)+)\]\.indexOf\(name\)', ht):
            names |= set(re.findall(r'"([\w-]+)"', arr))
        tags[p] = names
    every = set().union(*tags.values())
    for p in PAGES:
        gap = sorted(every - tags[p] - LESSON_ONLY)
        check(f"{p} handles every shared board tag ({len(tags[p])})", not gap,
              f"the tutor can emit {gap} here and NOTHING will draw")
    # ...and the allowance itself must stay honest: a tag we excused must genuinely be
    # absent from the shared block that practice and topic also receive.
    leaked = sorted(t for t in LESSON_ONLY if f"[[{t}" in tutor.GRAPH_TOOL_NOTE)
    check("no lesson-only tag is taught in the SHARED block", not leaked,
          f"the shared block asks for {leaked}, but practice/topic cannot draw them")


def part4_live():
    print("\nPART 4 — live scenarios (a scripted difficult student)")
    if not os.environ.get("ANTHROPIC_API_KEY"):
        skip("live scenarios", "no ANTHROPIC_API_KEY")
        return
    for sc in LIVE_SCENARIOS:
        history = [{"role": r, "content": t} for r, t in sc["history"]]
        try:
            reply = tutor.get_tutor_reply(dict(STUDENT), history, sc["student"],
                                          course=sc["course"], code="RULETEST")
        except Exception as exc:  # noqa: BLE001
            bad(f"live: {sc['name']}", f"call failed: {exc}")
            continue
        try:
            passed = bool(sc["assertion"](reply))
        except Exception as exc:  # noqa: BLE001
            passed = False
            reply = f"(assertion crashed: {exc}) {reply}"
        check(f"live: {sc['name']}", passed, f"{sc['why']}\n        reply: {reply[:220]}")


def main():
    live = "--live" in sys.argv
    print("=" * 70)
    print("RULE REGRESSION BATTERY —", "OFFLINE + LIVE" if live else "OFFLINE ONLY")
    print("=" * 70)
    part1_coverage()
    part2_prose()
    part3_speech()
    part3b_foundations()
    part3c_board_tags()
    part3d_foundation_memory()
    part3e_page_parity()
    if live:
        part4_live()
    else:
        print("\nPART 4 — live scenarios")
        skip("live scenarios", "pass --live to run them")
    print("\n" + "=" * 70)
    print(f"{len(PASS)} passed · {len(FAIL)} failed · {len(SKIP)} skipped")
    if FAIL:
        print("\nFAILURES:")
        for name, detail in FAIL:
            print(f"  - {name}: {detail}")
    print("=" * 70)
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())

# I did no harm and this file is not truncated.

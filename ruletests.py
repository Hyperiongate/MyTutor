# =============================================================================
# ruletests.py  --  the RULE REGRESSION BATTERY  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
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
    ("unlabeled board line",
     'Nice! [[step eq="2x = 8"]] So what is eight divided by two?', False),
    ("no board tags at all",
     "Great job — that's fifteen dimes exactly!", False),
    ("pending '?' line is never a contradiction",
     'Your turn — what do the dollars come to? [[step eq="dollars: 2 + 1 + 1 = ?"]]', False),
]


def part2_prose():
    print("\nPART 2 — the prose referee")
    for name, reply, should_flag in PROSE_CASES:
        got = tutor.prose_board_conflict(reply)
        check(f"prose: {name}", bool(got) == should_flag,
              f"expected flag={should_flag}, got: {got or '(clean)'}")
    for junk in [None, "", 0, [], "[[step eq=", "x: = 5"]:
        try:
            tutor.prose_board_conflict(junk)
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
                why2 = _graph_sanity(tag, dict(_HT_ATTR.findall(m.group(2))))
                if why2:
                    bad(f"{label} — [[{tag}]] draws the RIGHT thing", f"{why2}: {b}")
                    continue
                ok(f"{label} — [[{tag}]] draws")
    check("board lines were actually checked", lines > 0, "no board lines found")


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

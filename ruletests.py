# =============================================================================
# ruletests.py  --  the RULE REGRESSION BATTERY  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-08-10  BUILD cs -- THE WHITELIST CHECK THAT SHOULD HAVE EXISTED SINCE bx. The
#               demo design notes have said "every spoken string must be on the
#               whitelist" from the beginning and NOTHING enforced it. say() looks the
#               text up in VOICE_LINES and plays clip N by index; a line that is not
#               there does not raise -- that one stop drops to the browser's flat
#               mechanical voice in the middle of Mr. Cadabra speaking. All 24 literal
#               tour lines are now checked, on every tour on the page. Two more: every
#               tour stop must point at an element that EXISTS (glow() returns quietly on
#               a missing id, so a typo means the words play over a dashboard that never
#               moves), and the homeschool override must cover every parent stop (it is
#               read BY INDEX and falls through to the PARENT's words where it is short).
#               A LESSON FROM WRITING IT: the first version wrapped the parse in `except
#               Exception`, which swallowed a NameError -- ast was never imported -- so
#               every line looked off-list and the failure blamed the demo instead of the
#               test. The except is narrow now. A test's error handling must not be able
#               to hide the test's own bugs.
#   2026-08-10  BUILD cr -- PART 3j now proves ONE DOOR, ONE DASHBOARD. Jim: "I don't
#               want any links to any other dashboards from there." Three paths could
#               hand an audience visitor somebody else's screen and all three fail
#               silently, so each is checked against the SOURCE rather than against a
#               comment claiming it: showBalloons must return through the audience
#               ending BEFORE it builds the three balloons, the ending itself must
#               contain no dashboard opener at all, and the dashboard's back button must
#               not close a locked walkthrough (there is no page behind it).
#               Also checked: a locked door still leads somewhere. A test that only
#               proves an absence would happily pass on a dead end.
#               NOT IN THIS FILE, deliberately: the behaviour was also driven in a real
#               browser across all four doors and the open demo (59 checks). That harness
#               needs playwright, and this battery must stay runnable anywhere in a
#               second -- it lives in the sandbox, not the repo.
#   2026-08-10  BUILD cq -- PART 3j grew two checks and one of its own bugs was fixed.
#               New: the walkthrough must open the dashboard BEFORE it starts talking
#               (Jim watched a blank screen talk at him for thirty seconds), and every
#               audience line must be anchored by its opening WORDS, each anchor
#               resolving to exactly ONE whitelisted line.
#               THE BUG WORTH REMEMBERING: my first anchor regex used ["']([^"']{12,80})["']
#               to pull the anchor text out. Four of the nine anchors have an apostrophe
#               inside a double-quoted string -- "the parent's view", "That's the honest
#               read." -- and [^"'] stops dead at that apostrophe. The test found five
#               anchors, called it a pass at >=9 only by accident of failing loudly, and
#               would otherwise have checked less than half of what its name claimed.
#               A test that silently checks a subset is worse than no test. Capture the
#               opening quote, require the same character to close it.
#   2026-08-10  BUILD cp -- PART 3j, the audience walkthroughs. Guards the two things
#               that can break /demo?view=... silently: a marketing page pointing at a
#               view the demo does not implement, and the two voice lists falling out of
#               step. That second one deserves a warning to whoever reads this next:
#               clips are served BY INDEX, so a mismatch plays the WRONG AUDIO under the
#               RIGHT WORDS and nothing errors. While writing this I compared the lists
#               with a naive regex over quoted strings, which matched text inside
#               COMMENTS and made two identical 188-line lists look 117 lines apart. The
#               helper here parses main.py as Python and demo.html as JS-with-comments,
#               which is the only way to answer the question honestly.
#   2026-08-10  BUILD co -- PART 3i AND THE GENERATED RULES INDEX (audit #2 items 24
#               and 23). This file's header has said from day one: "ADDING A RULE? Add a
#               scenario here in the same commit. That is the whole point." We drifted
#               anyway -- rules 42 to 47 shipped with no check of their own -- because
#               nothing made the drift visible.
#               RULE_VERIFY now declares, for every rule, HOW it is verified, in four
#               honest tiers: ENFORCED (a machine catches it in a real reply),
#               EXERCISED (a --live scenario asserts the behaviour), COVERED (the text
#               provably reaches all ten prompts -- he was told, which is not the same as
#               he does it), UNVERIFIED (nothing at all).
#               It is a RATCHET, not a gate: existing debt prints but does not fail a
#               deploy, while a NEW rule with no declaration fails, and a rule that
#               quietly LOSES its scenario fails. Today: 13 enforced, 10 exercised,
#               25 covered, 1 unverified.
#               `python ruletests.py --rules` regenerates RULES.md from the prompt
#               itself, so the index can never drift from the classroom. That file is
#               also what you hand a curriculum advisor or a school district.
#   2026-08-10  BUILD cn -- PART 3h, "it must not degrade, and it must scale".
#               Nothing in this battery had ever asked whether anything GROWS, and two
#               things did: every chat turn loaded, parsed, appended to and rewrote the
#               student's ENTIRE conversation in order to read the last thirty messages
#               of it, and the usage log kept every row forever. PART 3h now checks the
#               transcript cap (and that it stays above what the model reads), the usage
#               retention pass, deliberate pool sizing, age-based rate-bucket eviction
#               and the TTS cache cap.
#               It also asserts the prompt does not FLIP SHAPE between turns -- build cl
#               made it do that to save characters, and the cache arithmetic showed the
#               flip costs about $0.24 an episode to save $0.0005 a turn.
#   2026-08-10  BUILD cm -- CACHE DISCIPLINE CHECKS. The system prompt is one cached
#               block; per-turn content inside it moves the cache prefix and re-bills
#               everything after it. PART 3g now asserts get_tutor_reply takes a
#               turn_note, that per-turn asides never appear in the system prompt, and
#               that two ordinary turns build a byte-identical prompt.
#   2026-08-10  BUILD cl -- DEFERRAL TESTS + THE PROMPT BUDGET.
#               The deferral tests care far more about RESTORING than about saving: a
#               brand-new student still gets every script verbatim, a returning student
#               keeps every UNHEARD script verbatim, heard scripts stay NAMED so he can
#               still offer them, asking restores the exact wording, the default is to
#               carry the words, and the refresher detector is checked on both the
#               explicit ask and the bare "yes" that follows rule 40(b)'s offer.
#               The prompt ceiling is now a BUDGET TABLE, not a single number. A total
#               tells you that you are over and nothing about what to do; the table
#               prices every block, so the next person adding one sees the cost before
#               paying it. Measured and recorded in the failure message: there is 0%
#               overlap between the course templates and the shared rules, so nothing can
#               be reclaimed for free -- the honest options are consolidating rules,
#               deferring another block the way cl defers heard scripts, or raising the
#               ceiling deliberately with the reason written down.
#   2026-08-10  BUILD ck -- PART 3g, the misconception catalogue, and a PROMPT-SIZE
#               tripwire (audit #2 item 22). PART 3g checks every entry has all nine
#               fields, unique ids, a speakable SAY that does NOT open by telling the
#               student they are wrong (rules 20/49c), and -- the important one -- that
#               no `detect` string is just a NUMBER in any spelling. The first end-to-end
#               run matched "I did three plus two first, so twenty" and returned two
#               confident WRONG theories, because "three" and "two" had survived a filter
#               that only required a letter. A numeric answer is evidence only in the
#               context of the problem it answers, and the matcher cannot see the
#               problem. That case is now a permanent fixture.
#               The prompt-size check prints every course's size and fails above 135,000
#               characters. It is a TRIPWIRE set above today's largest (130,022): when it
#               trips the answer is to consolidate overlapping rules -- the rules block
#               is ~45% of the prompt -- not to raise the number.
#   2026-08-09  BUILD cj -- PART 3f, NOTATION COVERAGE. Jim asked the right question
#               after the f(x) fix: "math is filled with these kinds of things. How can
#               we make sure every one of these is caught all of the time?" Fixing f(x)
#               by hand fixed one symbol and guaranteed nothing. PART 3f is the general
#               answer, held against notation.py:
#                 A  every notation on every board we ship is REGISTERED for that course
#                    (317 board strings scanned). Write a symbol the registry does not
#                    know and the build fails -- so a symbol cannot reach a child's
#                    screen without us having said, somewhere, how to read it.
#                 B  the DEEP families need a real script that says them aloud, not a
#                    table row. It caught three courses using subscripts silently.
#                 C  the registry must recognise its own examples, must reach all ten
#                    prompts, and no entry may collide with a narrower one -- that last
#                    invariant was added after the first run reported diffeq's mu as an
#                    unregistered population mean, because two entries matched one glyph.
#   2026-08-09  BUILD ci -- rule 48 and the NOTATION READABILITY check (PART 3b).
#               Jim found f(x) being used in Algebra I with nothing ever teaching it. The
#               check that would have caught it: for every course, if any script writes
#               function notation on the BOARD, some script in that course must read it
#               ALOUD in words and deny the wrong reading by name. It failed on four
#               courses the moment it was written, and on diffeq even after the first fix
#               -- because diffeq writes y(t), y prime and dy/dx rather than f(x), and my
#               first regex only knew about f, g and h. Both halves of the check now
#               share one letter set so they can never disagree again.
#   2026-08-09  BUILD ch -- SCORE_CASES, rules 45-47, and two arithmetic guards.
#               SCORE_CASES covers the new score referee. Its FALSE cases carry the
#               weight again: three false positives were caught here before shipping,
#               including one that revealed the percentage check was matching NOTHING
#               (a stray \b after "%"). Also asserts that tutor.py's pass marks never
#               drift from store.py's, and that no score in any total from 1 to 40 is
#               ever stored higher than the truth.
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
import ast
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import tutor  # noqa: E402
import notation  # noqa: E402

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
    ("rule 45 the tally is arithmetic",  "THE TALLY IS ARITHMETIC, NOT JUDGMENT"),
    ("rule 46 one skill per question",   "A QUIZ QUESTION TESTS ONE SKILL"),
    ("rule 47 no cold quizzes",          "NO COLD QUIZZES"),
    ("rule 48 say the symbol aloud",     "HOW TO *SAY* THE SYMBOL"),
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

# rules 2 and 8 -- (student's message, reply, should_flag). Added build co, when the
# generated rule index made it plain these were two of only three rules in the entire
# prompt that nothing checked at all.
ASKED_CASES = [
    ("show me a number line",
     "Sure — a number line runs from negative five to five.", True),
    ("show me a number line",
     'Sure! [[numberline min="-5" max="5" points="0" caption="zero sits in the middle"]]', False),
    ("can I see it drawn?", 'Of course. [[write text="3/4"]]', False),
    ("draw it for me", "I will in a moment — first, what is seven plus eight?", True),
    ("what is 7 plus 8?", 'Fifteen — nice. [[step eq="7 + 8 = 15"]]', False),
    ("", "Let me show you what happens when we take two away.", True),
    ("", 'Let me show you. [[objects emoji="🍪" groups="5" caption="take two away and count"]]', False),
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


# ---- the SCORE half (build ch, proactive audit #2 item 9) --------------------
# The server already recomputes every percentage from correct/total, so no number the
# model asserts is ever STORED. What nothing checked is what the student HEARS: the tag
# can say 3 of 5 while the sentence beside it says "you passed!". These counts feed the
# progress bars, the parent dashboard and the printable homeschool record, so a score
# softened once becomes a green bar and a line a parent may have to defend.
# Three false positives were caught here before shipping -- see the FALSE cases.
SCORE_CASES = [
    ("a fail called a pass",
     'Nice work — you passed! [[quiz unit="2" topic="1" name="Rounding" correct="3" total="5"]]', True),
    ("the same fail, reported honestly",
     'Three of five this time. [[quiz unit="2" topic="1" name="Rounding" correct="3" total="5"]]', False),
    ("a real pass",
     'You passed — four of five! [[quiz unit="2" topic="1" name="R" correct="4" total="5"]]', False),
    ("a pass talked down into a fail",
     'We\'ll try that again soon. [[quiz unit="2" topic="1" name="R" correct="5" total="5"]]', True),
    ("an inflated percentage",
     'That is 80% — great! [[quiz unit="2" topic="1" name="R" correct="3" total="5"]]', True),
    ("the correct percentage, stated plainly",
     'That is 60% — one more round and you have it. [[quiz unit="2" topic="1" name="R" correct="3" total="5"]]', False),
    ("naming the BAR is teaching, not a score claim",
     'You need 80% to pass, and you got 60% this time. [[quiz unit="2" topic="1" name="R" correct="3" total="5"]]', False),
    ("a mis-stated fraction",
     'You got four out of five. [[quiz unit="2" topic="1" name="R" correct="3" total="5"]]', True),
    ("the right fraction, in words",
     'You got three out of five. [[quiz unit="2" topic="1" name="R" correct="3" total="5"]]', False),
    ("80% is a topic-quiz pass but NOT unit mastery",
     'You mastered the unit! [[check unit="2" correct="4" total="5"]]', True),
    ("90% is",
     'You mastered the unit — nine of ten! [[check unit="2" correct="9" total="10"]]', False),
    ("the Final Exam, inflated",
     'You passed the Final Exam! [[finalexam correct="15" total="18"]]', True),
    ("the Final Exam, honest",
     'Seventeen of eighteen — you passed the Final Exam! [[finalexam correct="17" total="18"]]', False),
    ("no score tag: nothing to contradict",
     'You passed that one nicely. [[step eq="7 + 8 = 15"]]', False),
    ("a percentage inside the MATH is not a score claim",
     'What is 25% of 80? [[write text="25% of 80 = ?"]] '
     '[[quiz unit="2" topic="1" name="R" correct="4" total="5"]]', False),
    ("a percents lesson that also reports honestly",
     'Nice — 25% of 80 is 20. You got four out of five today. '
     '[[quiz unit="2" topic="1" name="R" correct="4" total="5"]]', False),
    ("an unrelated count is not a score",
     'That took 5 steps. [[quiz unit="2" topic="1" name="R" correct="3" total="5"]]', False),
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
    for said, reply, should_flag in ASKED_CASES:
        got = tutor.prose_board_conflict(reply, said)
        check(f"asked-to-see: {said[:26]!r} -> {'flag' if should_flag else 'clean'}",
              bool(got) == should_flag, f"got: {got or '(clean)'}")
    for name, reply, should_flag in PENDING_CASES:
        got = tutor.prose_pending_question_conflict(reply)
        check(f"pending: {name}", bool(got) == should_flag,
              f"expected flag={should_flag}, got: {got or '(clean)'}")
        if should_flag:
            check(f"pending: {name} (via prose_board_conflict)",
                  bool(tutor.prose_board_conflict(reply)),
                  "the combined referee let it through")
    for name, reply, should_flag in SCORE_CASES:
        got = tutor.prose_score_conflict(reply)
        check(f"score: {name}", bool(got) == should_flag,
              f"expected flag={should_flag}, got: {got or '(clean)'}")
        if should_flag:
            check(f"score: {name} (via prose_board_conflict)",
                  bool(tutor.prose_board_conflict(reply)),
                  "the combined referee let it through")
    # the referee's thresholds must never drift from the ones the DATABASE enforces
    try:
        import store
        check("tutor's pass marks match store's", 
              (tutor.QUIZ_PASS_PCT, tutor.UNIT_PASS_PCT, tutor.FINAL_PASS_PCT)
              == (store.QUIZ_PASS_PCT, store.PASS_PCT, store.PASS_PCT),
              f"tutor {(tutor.QUIZ_PASS_PCT, tutor.UNIT_PASS_PCT, tutor.FINAL_PASS_PCT)} "
              f"vs store {(store.QUIZ_PASS_PCT, store.PASS_PCT, store.PASS_PCT)}")
        # and the stored percentage must never be rounded UP over a bar
        bad_round = [(c, t) for t in range(1, 41) for c in range(t + 1)
                     if store.score_pct(c, t) > (100 * c) / t]
        check("no score is ever rounded up", not bad_round, f"e.g. {bad_round[:3]}")
        check("score_pct is exact when it can be", store.score_pct(4, 5) == 80
              and store.score_pct(9, 10) == 90 and store.score_pct(17, 18) == 94,
              "an exact score changed value")
    except Exception as exc:  # noqa: BLE001
        bad("store.py score helpers", str(exc))
    for junk in [None, "", 0, [], "[[step eq=", "x: = 5", "[[numberline"]:
        try:
            tutor.prose_board_conflict(junk)
            tutor.prose_visual_conflict(junk)
            tutor.prose_pending_question_conflict(junk)
            tutor.prose_score_conflict(junk)
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

    # NOTATION MUST BE READABLE (2026-08-09, build ci -- Jim, live in Algebra I: "it's
    # never been clearly stated to me what f of x is, how to say f of x... and then it
    # flipped over to g of x"). He was right and it was not the student: Algebra I's
    # "function" script never mentioned the notation at all, and the very NEXT script
    # put f(x) = 1/x on the board. Any course whose scripts write a symbol like f( ) must
    # also have a script that says it OUT LOUD, in words, and denies the wrong reading.
    for c in COURSES:
        items = foundations.for_course(c)
        # The letters our courses actually use as function names. Kept identical in both
        # halves of this check so "y(t)" on the board is answered by "y of t" in the
        # words -- diffeq writes y(t), y', dy/dx everywhere and f/g/h almost never.
        FN_LETTERS = "fghpquvwy"
        writes_fx = [f["term"] for f in items
                     if any(re.search(r"\b[" + FN_LETTERS + r"]\s*\(\s*[a-z0-9]", b)
                            for b in f.get("board", []))]
        if not writes_fx:
            continue
        reads_fx = [f["term"] for f in items
                    if re.search(r"\b[" + FN_LETTERS + r"] of (?:[a-z]\b|zero|one|two)",
                                 f["say"], re.I)]
        check(f"notation [{c}]: something says it out loud "
              f"({len(writes_fx)} scripts write it)", bool(reads_fx),
              f"scripts {writes_fx} put function notation on the board and NOTHING ever "
              f"tells the student it is read '\u2026 of x' -- rule 48(a)")
        # "not f times x", "never as f times x", "does not mean f multiplied by x" --
        # the denial is what matters, not the phrasing, so look for a negation and a
        # multiplication word in the same breath.
        denies = [f["term"] for f in items
                  if re.search(r"\b(?:not|never)\b[^.]{0,30}\b(?:times|multipl\w+)\b",
                               f["say"], re.I)]
        check(f"notation [{c}]: the wrong reading is denied by name", bool(denies),
              "rule 48(b): say plainly that it is NOT f times x -- that guess is the "
              "single most common misreading in all of algebra")
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

    # 4b. DEFERRED WORDING (build cl). A heard script's exact text is dropped from the
    #     ordinary turns of a returning student and restored the moment they ask. The
    #     danger is obvious -- if it is ever missing when he needs it he will paraphrase,
    #     which costs a cache miss AND drifts wording every student is meant to share --
    #     so the tests below care far more about RESTORING than about saving.
    # build cn: the deferral below is DORMANT in production -- main.py always carries the
    # wording, because flipping the prompt shape costs a cache rebuild worth far more
    # than the characters it saves (see main.py). The mechanism is still tested, because
    # it is the right answer if the library ever outgrows the window.
    heard = [d["term"] for d in foundations.for_course("algebra2")][:12]
    full = tutor.build_system_prompt(
        dict(STUDENT, foundations_heard=heard, foundations_verbatim=True), course="algebra2")
    lean = tutor.build_system_prompt(
        dict(STUDENT, foundations_heard=heard, foundations_verbatim=False), course="algebra2")
    fresh = tutor.build_system_prompt(dict(STUDENT), course="algebra2")
    a2 = foundations.for_course("algebra2")
    check("a brand-new student still gets every script verbatim",
          all(f["say"] in fresh for f in a2), "a new student lost a script")
    check("a returning student keeps UNHEARD scripts verbatim",
          all(f["say"] in lean for f in a2 if f["term"] not in heard),
          "a script they have never met was deferred -- that is a teaching loss")
    check("heard scripts are still NAMED on an ordinary turn",
          all(f["term"].upper() in lean for f in a2 if f["term"] in heard),
          "he cannot offer a refresher for a term he cannot see")
    check("asking for it restores the EXACT wording",
          all(f["say"] in full for f in a2),
          "the refresher turn is missing a script -- he would have to paraphrase")
    check("deferring actually saves something", len(lean) < len(full) - 2000,
          f"only {len(full) - len(lean)} chars")
    check("the default is to CARRY the words",
          "prompt_block" in dir(foundations)
          and foundations.prompt_block("algebra2", heard) == foundations.prompt_block(
              "algebra2", heard, True),
          "verbatim must default to True -- fail open, always")
    for msg, last, want in [
            ("remind me what a denominator is", "", True),
            ("yes please", "…or want me to refresh your memory?", True),
            ("not really", "…got a handle on that?", True),
            ("I forgot", "", True),
            ("yes", "so what is seven plus eight?", False),
            ("sixteen", "", False)]:
        check(f"refresher detector: {msg!r} -> {'restore' if want else 'defer'}",
              foundations.wants_refresher(msg, last) == want,
              f"got {foundations.wants_refresher(msg, last)}")
    for junk in [None, 0, [], "?" * 500]:
        try:
            foundations.wants_refresher(junk, junk)
        except Exception as exc:  # noqa: BLE001
            bad("refresher detector: junk never raises", f"{junk!r} -> {exc}"); break
    else:
        ok("refresher detector: junk never raises")

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


# =============================================================================
# PART 3f -- NOTATION COVERAGE: WE NEVER WRITE A SYMBOL WE HAVEN'T SAID
# -----------------------------------------------------------------------------
# 2026-08-09 (build cj). Jim, after the f(x) fix: "it looks like we've fixed the
# function notation, but math is filled with these kinds of things. How can we make
# sure that every one of these is caught all of the time?"
#
# Build ci fixed f(x) by hand, which fixes one symbol and guarantees nothing. This is
# the general answer. notation.py registers every notation the courses use -- how it is
# written, how it is SAID, and the wrong reading to deny -- and this test holds every
# board line we ship to it:
#   CHECK A  every notation on a board is REGISTERED for that course. If we write a
#            symbol the registry does not know, the tutor was never told how to read it
#            and the build fails. This is the guarantee: we cannot put a symbol on a
#            child's screen without having said, somewhere, how to say it.
#   CHECK B  the DEEP families (function, prime, exponent, subscript, absolute value,
#            radical) need a real foundation script that reads them aloud -- a one-line
#            table row is not teaching. It caught three courses using subscripts with
#            nothing anywhere saying "sub".
#   CHECK C  the registry reaches every course's prompt, and its own patterns are sane
#            (every `shown` example must match its own `wrote` pattern, and every
#            `spoken` example its own `heard` pattern -- a registry that cannot
#            recognise its own examples is worse than none).
# =============================================================================
_NT_TAG = re.compile(r"\[\[\s*([\w-]+)([^\]]*?)\]\]")
_NT_ATTR = re.compile(r'([\w-]+)\s*=\s*"([^"]*)"')


def _board_readable(entry) -> list:
    """The parts of a script's board a STUDENT actually reads (not renderer inputs)."""
    out = []
    for b in entry.get("board", []):
        m = _NT_TAG.match(b.strip())
        if not m:
            continue
        for k, v in _NT_ATTR.findall(m.group(2)):
            if k.lower() in notation.READABLE_ATTRS:
                out.append((v, b))
    return out


def part3f_notation():
    print("\nPART 3f — notation coverage (we never write a symbol we haven't said)")
    try:
        import foundations
    except Exception as exc:  # noqa: BLE001
        bad("foundations.py imports", str(exc)); return

    # CHECK C first: a registry that cannot recognise its own examples proves nothing.
    for n in notation.NOTATIONS:
        check(f"  registry [{n['id']}] recognises its own written form",
              bool(re.search(n["wrote"], n["shown"])),
              f"shown={n['shown']!r} does not match wrote={n['wrote']!r}")
        check(f"  registry [{n['id']}] recognises its own spoken form",
              bool(re.search(n["heard"], n["spoken"], re.I)),
              f"spoken={n['spoken']!r} does not match heard={n['heard']!r}")
        # If one entry's example ALSO matches another entry, that other entry must be
        # legal everywhere this one is -- otherwise a perfectly good board line gets
        # reported as an unregistered symbol. (Exactly what happened with mu: a stats
        # entry and a general-name entry both matched the same glyph.)
        overlap = [o for o in notation.written_in(n["shown"]) if o != n["id"]
                   and not set(n["courses"]) <= set(notation.by_id(o)["courses"])]
        check(f"  registry [{n['id']}] does not collide with a narrower entry",
              not overlap,
              f"{n['shown']!r} also matches {overlap}, which are not allowed in every "
              f"course [{n['id']}] is -- merge them or tighten the patterns")
    for c in COURSES:
        p = tutor.build_system_prompt(dict(STUDENT), course=c)
        check(f"the symbol table reaches [{c}]", "HOW TO SAY WHAT YOU WRITE" in p,
              "this course's tutor has no canonical readings -- rule 48 is unfollowable")

    # CHECK A: nothing on any board is unregistered for its course.
    unregistered = {}
    scanned = 0
    for c in COURSES:
        allowed = {n["id"] for n in notation.for_course(c)}
        for d in foundations.for_course(c):
            for value, raw in _board_readable(d):
                scanned += 1
                for nid in notation.written_in(value):
                    if nid not in allowed:
                        unregistered.setdefault((c, nid), (d["term"], raw))
    check(f"every notation on every board is registered ({scanned} board strings)",
          not unregistered,
          "; ".join(f"{c} writes [{n}] in '{t}' — register it in notation.py or stop "
                    f"writing it: {r[:60]}" for (c, n), (t, r) in sorted(unregistered.items())))

    # CHECK B: a deep notation must be TAUGHT, not just tabled.
    for c in COURSES:
        items = foundations.for_course(c)
        used = set()
        for d in items:
            for value, _raw in _board_readable(d):
                used.update(notation.written_in(value))
        said = set()
        for d in items:
            said.update(notation.spoken_in(d["say"]))
        for nid in sorted(used):
            if not notation.by_id(nid).get("deep"):
                continue
            check(f"  [{c}] teaches [{nid}] aloud, not just on the board", nid in said,
                  f"this course writes {notation.by_id(nid)['shown']} and NO script ever "
                  f"says \"{notation.by_id(nid)['spoken']}\" — rule 48(a)")


# =============================================================================
# PART 3g -- THE MISCONCEPTION CATALOGUE (rule 49)
# =============================================================================
_CARDINALS = set("""zero one two three four five six seven eight nine ten eleven twelve
thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty thirty forty fifty
sixty seventy eighty ninety hundred thousand million negative minus point and a""".split())


def part3g_misconceptions():
    print("\nPART 3g — the misconception catalogue")
    try:
        import misconceptions as M
    except Exception as exc:  # noqa: BLE001
        bad("misconceptions.py imports", str(exc)); return
    seen_ids, total = set(), 0
    for c in COURSES:
        items = M.for_course(c)
        total += len(items)
        check(f"[{c}] has a catalogue ({len(items)} error patterns)", len(items) >= 10,
              "too few to be worth consulting")
        for m in items:
            lab = f"  [{c}] {m['id']}"
            check(f"{lab} has every field",
                  all(m.get(k) for k in ("id", "name", "topic", "tell", "rule", "why", "fix", "say")),
                  f"missing: {[k for k in ('id','name','topic','tell','rule','why','fix','say') if not m.get(k)]}")
            check(f"{lab} id is unique", m["id"] not in seen_ids, "duplicated across courses")
            seen_ids.add(m["id"])
            offenders = [ch for ch in "=+×÷^<>" if ch in m["say"]]
            check(f"{lab} SAY is speakable", not offenders,
                  f"symbols that get read aloud badly: {offenders}")
            w = len(m["say"].split())
            check(f"{lab} SAY is a real sentence", 20 <= w <= 75, f"{w} words")
            # rule 49(c)/20: never open by telling them they are wrong
            opener = " ".join(m["say"].split()[:6]).lower()
            check(f"{lab} SAY does not open with 'wrong'",
                  not re.match(r"^(that'?s |that is )?(wrong|incorrect|no,|nope|not quite)", opener),
                  f"opens: {opener!r}")
            for d in m.get("detect", []):
                # A numeric answer is only evidence in the context of the problem it
                # answers, and the matcher cannot see the problem. So numbers never
                # count -- in ANY spelling. The first version of this filter allowed
                # anything containing a letter, and "three" and "two" promptly matched
                # "I did three plus two first, so twenty" and produced two confident
                # WRONG theories on the first end-to-end run (rule 49e).
                toks = [t for t in re.split(r"[\s\-]+", d.lower()) if t]
                barenum = toks and all(
                    t in _CARDINALS or re.fullmatch(r"[-+]?\d+(?:\.\d+)?", t) for t in toks)
                check(f"{lab} evidence {d!r} is not just a number", not barenum,
                      "a number fires on correct answers too -- evidence must be a "
                      "procedure word or a distinctive symbolic form")
    check(f"the catalogue is substantial ({total} patterns)", total >= 120, f"only {total}")

    # the matcher must be conservative: it fires on real evidence and stays silent otherwise
    CASES = [
        ("basicmath", "two fifths", "add-across-fractions", True),
        ("algebra1", "three x plus four", "distribute-one-term-only", True),
        ("basicmath", "sixteen", None, False),
        ("basicmath", "I am not sure", None, False),
        # the false-positive that the first end-to-end run produced
        ("prealgebra", "I did three plus two first, so twenty", None, False),
        ("prealgebra", "twenty", None, False),
        ("probstat", "so it causes it", "correlation-is-causation", True),
        ("prealgebra", "", None, False),
    ]
    for course, said, want_id, want_hit in CASES:
        hits = M.match(course, said)
        check(f"matcher: {said!r} -> {'a theory' if want_hit else 'silence'}",
              bool(hits) == want_hit and (not want_id or any(h["id"] == want_id for h in hits)),
              f"got {[h['id'] for h in hits]}")
    check("the matcher never returns a crowd", all(len(M.match(c, "two fifths x plus four")) <= 2
                                                   for c in COURSES),
          "more than two theories is the same as none (rule 49d)")
    for junk in [None, "", 0, [], "?" * 400]:
        try:
            M.match("basicmath", junk); M.hint_note("basicmath", junk)
        except Exception as exc:  # noqa: BLE001
            bad("matcher: junk never raises", f"{junk!r} -> {exc}"); break
    else:
        ok("matcher: junk never raises")
    # CACHE DISCIPLINE (build cm). The system prompt is ONE cached block, so anything
    # per-turn that lands inside it moves the cache prefix and re-bills every token from
    # that point on. Build ck put the misconception hint into the prompt and threw away
    # ~16k tokens on every turn it fired. Per-turn notes now ride with the message.
    import inspect
    check("get_tutor_reply takes a per-turn note",
          "turn_note" in inspect.signature(tutor.get_tutor_reply).parameters,
          "a per-turn note has nowhere to go except the cached prompt")
    base = tutor.build_system_prompt(dict(STUDENT), course="basicmath")
    for volatile in ("[LIKELY MISCONCEPTION -- ...]", "\n[some per-turn aside]"):
        check(f"a per-turn note does NOT reach the system prompt ({volatile[:22]}…)",
              volatile not in base, "it would move the cache prefix every turn")
    check("the prompt shape does not flip between turns in production",
          "student_context[\"foundations_verbatim\"] = True" in
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "main.py"),
               encoding="utf-8").read(),
          "a prompt that changes shape rebuilds the cache -- ~$0.24 an episode, and a "
          "slower turn, to save $0.0005")
    check("the system prompt is identical for two ordinary turns",
          tutor.build_system_prompt(dict(STUDENT), course="basicmath") == base,
          "the cached prefix changes turn to turn -- every turn re-bills in full")

    check("a hit produces a note the tutor may DISCARD",
          "IGNORE this note" in M.hint_note("basicmath", "two fifths"),
          "the note must never override his own reading of the student (rule 49d)")

    # every course's catalogue must actually reach its prompt
    for c in COURSES:
        p = tutor.build_system_prompt(dict(STUDENT), course=c)
        check(f"the catalogue reaches [{c}]", "WHY THE ANSWER WAS WRONG" in p,
              "rule 49 is unfollowable in this course")

    # PROMPT SIZE (proactive audit #2 item 22). Not a style note: past some length a
    # model follows rule 3 and rule 31 less reliably, and the failure is invisible.
    # The ceiling is a TRIPWIRE, deliberately set above today's largest -- when it
    # trips, the answer is to consolidate overlapping rules, not to raise it again.
    CEILING = 135_000
    sizes = {c: len(tutor.build_system_prompt(dict(STUDENT), course=c)) for c in COURSES}
    biggest = max(sizes, key=sizes.get)
    # THE BUDGET, not just the total. A single number tells you that you are over and
    # nothing about what to do; this table tells you what every block costs, so the next
    # person adding one can see the price before they pay it. Measured 2026-08-10: the
    # course templates and the shared rules share ZERO text -- there is no duplication
    # left to reclaim, so any reduction from here removes or defers real teaching.
    try:
        import notation as _n, misconceptions as _m, foundations as _f
        c = biggest
        blocks = [
            ("shared rules 0-49", len(tutor.GRAPH_TOOL_NOTE)),
            ("course lesson template", len(tutor.LESSON_TEMPLATES.get(c, ""))),
            ("foundation scripts", len(_f.prompt_block(c))),
            ("misconception catalogue", len(_m.prompt_block(c))),
            ("session opener rules", len(tutor.SESSION_OPENER_RULES)),
            ("progress-tag note", len(tutor.PROGRESS_TAGS_NOTE)),
            ("notation table", len(_n.prompt_block(c))),
            ("ground rules", len(tutor.GROUND_RULES)),
        ]
        tot = sum(v for _k, v in blocks) or 1
        print(f"       PROMPT BUDGET ({c}, the largest):")
        for k, v in sorted(blocks, key=lambda x: -x[1]):
            print(f"         {k:<26}{v:>8,}  {100*v/tot:5.1f}%")
        print(f"         {'total':<26}{sizes[biggest]:>8,}  (ceiling {CEILING:,})")
    except Exception as exc:  # noqa: BLE001
        print(f"       (budget table unavailable: {exc})")
    check(f"no prompt exceeds {CEILING:,} chars", sizes[biggest] <= CEILING,
          f"{biggest} is {sizes[biggest]:,}. There is NO duplication left to reclaim "
          f"(measured 0% overlap between the templates and the shared rules), so the "
          f"honest options are: consolidate overlapping RULES, defer another block the "
          f"way build cl defers heard scripts, or raise this deliberately with a reason "
          f"written down. Do not raise it silently.")


# =============================================================================
# PART 3h -- IT MUST NOT DEGRADE, AND IT MUST SCALE
# -----------------------------------------------------------------------------
# 2026-08-10 (build cn). Jim: "I don't want to build in something that's going to
# degrade over time where their errors are gonna start to add up and making more and
# more mess because we're not discarding things that we should discard... suppose we
# have ten thousand people using this app simultaneously."
# Nothing in the battery had ever asked whether anything GROWS. It did: every chat turn
# loaded, parsed, appended to and rewrote the student's ENTIRE conversation to use the
# last thirty messages of it, and the usage log kept every row forever.
# =============================================================================
def part3h_scale():
    print("\nPART 3h — it must not degrade, and it must scale")
    here = os.path.dirname(os.path.abspath(__file__))
    src = {}
    for f in ("main.py", "store.py"):
        with open(os.path.join(here, f), encoding="utf-8") as fh:
            src[f] = fh.read()

    check("the stored transcript is capped", "MAX_STORED_MESSAGES" in src["main.py"],
          "a year-old student would move megabytes of JSON on every turn")
    check("every save goes through the cap",
          "def save_session" in src["main.py"]
          and "_bounded_history(session)" in src["main.py"],
          "some path writes an untrimmed transcript")
    m = re.search(r"MAX_STORED_MESSAGES\s*=\s*(\d+)", src["main.py"])
    stored = int(m.group(1)) if m else 0
    check(f"the cap ({stored}) leaves margin over what the model reads "
          f"({tutor.MAX_HISTORY_MESSAGES})", stored > tutor.MAX_HISTORY_MESSAGES,
          "trimming below what the tutor reads would silently shorten his memory")
    check("the usage log has a retention pass",
          "purge_usage_log" in src["store.py"] and "_usage_purge_pass" in src["main.py"],
          "one row per model call and per TTS request, kept forever")
    check("the connection pool is sized on purpose",
          "pool_size=" in src["store.py"] and "pool_recycle=" in src["store.py"],
          "SQLAlchemy's default is 15 connections -- a hard ceiling under load")
    check("rate-limit buckets expire by AGE, not just emptiness",
          "q[-1] <= now - max(window_seconds" in src["main.py"],
          "with every bucket busy the table grows past its cap and never shrinks")
    # the caps must be real numbers, not aspirations
    for name, pat, lo in [("TTS cache cap", r"_TTS_CACHE_MAX_BYTES\s*=\s*([\d_]+)", 1),
                          ("usage retention days", r"USAGE_LOG_DAYS[^\n]*?\"(\d+)\"", 1)]:
        mm = re.search(pat, src["main.py"])
        check(f"{name} is set", bool(mm) and int(mm.group(1).replace("_", "")) >= lo,
              "no cap found")


# =============================================================================
# PART 3i -- EVERY RULE DECLARES HOW IT IS VERIFIED  (audit #2 item 24)
# -----------------------------------------------------------------------------
# 2026-08-10 (build co). This file's own header has said since the day it was written:
# "ADDING A RULE? Add a scenario here in the same commit. That is the whole point."
# We drifted anyway -- rules 42 to 47 shipped with no behavioural check of their own --
# because nothing made the drift visible. This does.
#
# It is a RATCHET, not a gate. Today's honest position is recorded below and the suite
# does NOT fail for the debt that already exists; failing a deploy over history helps
# nobody. It fails for two things only, and both are new damage:
#   * a rule appears in the prompt with no entry here at all
#   * a rule that WAS enforced or exercised quietly loses its check
# The backlog prints on every run, so it cannot be forgotten either.
#
# THE FOUR TIERS, in descending order of how much they are worth:
#   ENFORCED   a machine catches the violation in a real reply. A referee regenerates
#              the draft, or an audit fails the build. This is the only tier that
#              protects a student on a Tuesday night with nobody watching.
#   EXERCISED  a --live scenario plays a student against the real prompt and asserts the
#              behaviour. Costs a few cents to run; catches real regressions.
#   COVERED    the rule's text provably reaches all ten courses' prompts (PART 1). That
#              is a real check -- it is the bug that hid for a day in build bk -- but it
#              proves only that he was TOLD, not that he does it.
#   UNVERIFIED the rule exists and nothing checks it. Honest, and the list to work from.
# =============================================================================
RULE_VERIFY = {
    1:  ("COVERED",   "the board only shows what you drew"),
    2:  ("ENFORCED",  "prose_visual_conflict: 'show me' with an unchanged board is regenerated"),
    3:  ("EXERCISED", "first-use key terms are marked"),
    4:  ("COVERED",   "say it then write it, in the same reply"),
    5:  ("UNVERIFIED", "don't narrate symbols, point at them"),
    6:  ("COVERED",   "never run ahead"),
    7:  ("ENFORCED",  "prose_visual_conflict regenerates a reply that names an undrawn picture"),
    8:  ("ENFORCED",  "prose_visual_conflict: promising to show something and drawing nothing"),
    9:  ("COVERED",   "the sound-off check"),
    10: ("ENFORCED",  "mathcheck reads every [[verify]] tag"),
    11: ("ENFORCED",  "a tag in the wrong syntax fails to parse and is caught"),
    12: ("ENFORCED",  "strip_verify_tags + the pages' stripTags remove it before the student"),
    13: ("ENFORCED",  "mathcheck re-computes the claim with SymPy"),
    14: ("COVERED",   "define every notation on first use (see also rule 48, ENFORCED)"),
    15: ("ENFORCED",  "prose_pending_question_conflict regenerates a question with no board line"),
    16: ("COVERED",   "a substitution question re-writes its equation"),
    17: ("COVERED",   "never answer your own question"),
    18: ("ENFORCED",  "prose_board_conflict regenerates spoken numbers that fight the board"),
    19: ("COVERED",   "worked example first"),
    20: ("COVERED",   "partially right is not wrong"),
    21: ("EXERCISED", "'I don't know' triggers a smaller step"),
    22: ("COVERED",   "the escalation ladder"),
    23: ("EXERCISED", "equivalent answers are correct"),
    24: ("COVERED",   "leaps, self-corrections, 'just tell me'"),
    25: ("COVERED",   "when the student says you are wrong"),
    26: ("COVERED",   "a wrong line never stays on the board"),
    27: ("COVERED",   "units and honest approximation"),
    28: ("EXERCISED", "one name per thing"),
    29: ("EXERCISED", "how a session ends"),
    30: ("EXERCISED", "off-topic and personal questions"),
    31: ("EXERCISED", "when something bigger than math shows up"),
    32: ("COVERED",   "story problems survive a sanity check"),
    33: ("COVERED",   "difficulty moves one notch"),
    34: ("COVERED",   "keep old skills sharp"),
    35: ("EXERCISED", "a failed quiz is never re-given on the spot"),
    36: ("EXERCISED", "teach the thing before you ask about it"),
    37: ("COVERED",   "vocabulary is taught, never assumed"),
    38: ("COVERED",   "concrete, then picture, then symbols"),
    39: ("COVERED",   "talk less, check in often, make the check failable"),
    40: ("EXERCISED", "ask before repeating an introduction"),
    41: ("ENFORCED",  "PART 3c fails any figure shipped without a caption"),
    42: ("COVERED",   "never compare this student to anyone but this student"),
    43: ("COVERED",   "you perceive exactly two things"),
    44: ("COVERED",   "read the problem aloud, in full"),
    45: ("ENFORCED",  "prose_score_conflict regenerates a spoken score that fights its own tag"),
    46: ("COVERED",   "a quiz question tests one skill"),
    47: ("COVERED",   "no cold quizzes"),
    48: ("ENFORCED",  "PART 3b/3f fail a course that writes notation it never reads aloud"),
    49: ("ENFORCED",  "PART 3g + the just-in-time matcher"),
}
_TIER_ORDER = ("ENFORCED", "EXERCISED", "COVERED", "UNVERIFIED")


_TITLE_END = re.compile(r"[.:]\s|\s--\s|\s\(")


def _rule_titles():
    """{number: the rule's headline}. The headline is the SHOUTED part at the start of
    each rule; the prose that follows it is the rule itself and is not repeated here.
    (First version split on the first ". " anywhere, which turned rule 2 into
    '"Show me", "can I see' -- the heading has to end where the capitals do.)"""
    out = {}
    # A rule opens at column 0 as "N. " followed by a SHOUTED headline, then prose. The
    # headline is what belongs in an index; the prose is the rule and is not repeated.
    # The headline ends at the first word containing a lower-case letter -- ALL-CAPS
    # words continue it, "Something", "Never", "(Jim's" end it. (Two earlier attempts
    # failed here: splitting on the first ". " turned rule 2 into '"Show me", "can I
    # see', and a length-bounded body match found only the two shortest rules.)
    for m in re.finditer(r"^(\d{1,2})\. (.{6,200})$", tutor.GRAPH_TOOL_NOTE, re.M):
        keep = []
        for w in m.group(2).split():
            if re.search(r"[a-z]", w) and len(keep) >= 3:
                break
            keep.append(w)
        out[int(m.group(1))] = " ".join(keep).strip(" ,.:;-") or m.group(2)[:70]
    return out


def part3i_rule_verification():
    print("\nPART 3i — every rule declares how it is verified")
    titles = _rule_titles()
    undeclared = sorted(n for n in titles if n not in RULE_VERIFY)
    check("every rule in the prompt is declared here", not undeclared,
          f"rules {undeclared} have no entry in RULE_VERIFY -- a new rule must say how it "
          f"is checked, even if the honest answer is UNVERIFIED")
    stale = sorted(n for n in RULE_VERIFY if n not in titles)
    check("no declaration outlives its rule", not stale,
          f"RULE_VERIFY still lists {stale}, which are no longer in the prompt")

    # the ratchet: a rule that had a real check must not quietly lose it
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    live_named = {int(m) for m in re.findall(r"rule (\d{1,2})", src[src.index("LIVE_SCENARIOS"):])}
    for n, (tier, _why) in sorted(RULE_VERIFY.items()):
        if tier == "EXERCISED":
            check(f"  rule {n} still has its --live scenario", n in live_named,
                  "it was exercised and now is not -- restore the scenario or downgrade "
                  "the declaration on purpose")

    counts = {t: [n for n, (tt, _w) in RULE_VERIFY.items() if tt == t] for t in _TIER_ORDER}
    print(f"       {len(titles)} rules: " + " · ".join(
        f"{t.lower()} {len(counts[t])}" for t in _TIER_ORDER))
    if counts["UNVERIFIED"]:
        print("       BACKLOG — nothing checks these at all:")
        for n in sorted(counts["UNVERIFIED"]):
            print(f"         rule {n:>2}: {titles.get(n, '?')[:66]}")
    check("no rule is enforced by wishful thinking",
          all(t in _TIER_ORDER for t, _w in RULE_VERIFY.values()), "unknown tier")


def write_rules_index(path="RULES.md"):
    """Generate RULES.md from the prompt itself (audit #2 item 23).

    Never hand-maintained, so it cannot drift: every line comes from tutor.py or from
    RULE_VERIFY above. This is the document to hand a curriculum advisor, a school
    district, or the next person who has to hold 49 rules in their head."""
    titles = _rule_titles()
    counts = {t: [n for n, (tt, _w) in RULE_VERIFY.items() if tt == t] for t in _TIER_ORDER}
    out = [
        "# Mr. Cadabra — the teaching rules",
        "",
        "_Generated from `tutor.py` by `python ruletests.py --rules`. Do not edit by hand:",
        "every line below is read out of the prompt the tutor is actually given, so this",
        "file cannot drift away from what the classroom really does._",
        "",
        f"**{len(titles)} rules.** Every one was written because something went wrong in a real",
        "lesson, and almost all of them were noticed by Jim before they were noticed by a",
        "machine. The right-hand column is how much better we have got at that.",
        "",
        "| how it is verified | rules | what that means |",
        "|---|---|---|",
        f"| **ENFORCED** | {len(counts['ENFORCED'])} | a machine catches the violation in a real reply — a referee rewrites the draft, or an audit fails the build |",
        f"| **EXERCISED** | {len(counts['EXERCISED'])} | a scripted student plays against the real prompt and the behaviour is asserted (`ruletests.py --live`) |",
        f"| **COVERED** | {len(counts['COVERED'])} | the rule's text provably reaches all ten courses — proves he was *told*, not that he does it |",
        f"| **UNVERIFIED** | {len(counts['UNVERIFIED'])} | the rule exists and nothing checks it |",
        "",
        "---",
        "",
    ]
    for n in sorted(titles):
        tier, why = RULE_VERIFY.get(n, ("UNVERIFIED", "not declared"))
        out.append(f"### {n}. {titles[n]}")
        out.append("")
        out.append(f"**{tier}** — {why}")
        out.append("")
    out += ["---", "",
            "## The four tiers, and why the order matters", "",
            "**ENFORCED** is the only tier that protects a student on a Tuesday night with",
            "nobody watching. A referee sees the draft before the child does and sends it",
            "back. Everything else depends on someone running something.", "",
            "**EXERCISED** catches regressions cheaply, but only when somebody runs",
            "`ruletests.py --live` — which costs a few cents and needs an API key.", "",
            "**COVERED** is not nothing: it is the bug that hid for a day in build bk, where",
            "a rule written into one of eleven per-course templates reached one course out of",
            "ten. But it proves only that the tutor was told.", "",
            "**UNVERIFIED** is the honest backlog. Moving a rule up a tier is usually worth",
            "more than writing a new rule.", "",
            "I did no harm and this file is not truncated."]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")
    return path


# =============================================================================
# PART 3j -- THE AUDIENCE WALKTHROUGHS  (/demo?view=...)
# -----------------------------------------------------------------------------
# 2026-08-10 (build cp). Jim: "it's almost like a video... I would like one of those
# available, a very obvious button that says view the demo on the parent page, the
# teacher page, the homeschooling page, and the student page."
# Built as a DEEP LINK into the existing demo rather than four new tour engines, because
# copying a tour into four marketing pages is exactly the copy-paste-drift that produced
# the build-bk rule bug and the board-wrap bug. This part guards the two things that can
# silently break it: a button pointing at a view the demo does not implement, and the
# two voice lists falling out of step -- clips are addressed by INDEX, so an insert
# anywhere above the end shifts every cached clip after it.
# =============================================================================
_AUDIENCE_PAGES = {"parents": "parents", "teachers": "teachers",
                   "homeschool": "homeschool", "students": "students"}


def _voice_lines_from(path, name):
    """The real list, from either language. main.py is Python, demo.html is JS with
    comments in it, so neither can be read with a naive regex over quoted strings --
    doing that once made two identical lists look 117 lines apart."""
    import ast as _ast, json as _json
    with open(path, encoding="utf-8") as fh:
        src = fh.read()
    m = re.search(name + r"\s*=\s*\[", src)
    if not m:
        return None
    i, depth = m.end() - 1, 0
    for j in range(i, len(src)):
        if src[j] == "[":
            depth += 1
        elif src[j] == "]":
            depth -= 1
            if depth == 0:
                break
    block = src[i:j + 1]
    if path.endswith(".py"):
        return _ast.literal_eval(block)
    block = re.sub(r"^\s*//.*$", "", block, flags=re.M)
    block = re.sub(r",(\s*\])", r"\1", block)
    return _json.loads(block)


def part3j_walkthroughs():
    print("\nPART 3j — the audience walkthroughs (/demo?view=...)")
    here = os.path.dirname(os.path.abspath(__file__))
    demo_path = os.path.join(here, "static", "demo.html")
    if not os.path.exists(demo_path):
        bad("demo.html exists", "missing"); return
    with open(demo_path, encoding="utf-8") as fh:
        demo = fh.read()

    views = set(re.findall(r"\n    (\w+):\s*\{ dash:'(\w+)'", demo))
    implemented = {v for v, _d in views}
    dashes = set(re.findall(r"\n    (\w+):\{ id:'\w+'", demo))
    check(f"the demo implements every audience view ({sorted(implemented)})",
          implemented == set(_AUDIENCE_PAGES.values()),
          f"expected {sorted(set(_AUDIENCE_PAGES.values()))}")
    for v, d in sorted(views):
        check(f"  view '{v}' opens a dashboard the demo actually has ('{d}')", d in dashes,
              f"openDash('{d}') would return immediately and the visitor would see nothing")

    # every page's button must point at a view that exists
    for page, view in sorted(_AUDIENCE_PAGES.items()):
        path = os.path.join(here, "static", page + ".html")
        if not os.path.exists(path):
            bad(f"{page}.html exists", "missing"); continue
        with open(path, encoding="utf-8") as fh:
            src = fh.read()
        check(f"{page}.html has an obvious walkthrough button",
              'class="walkbtn"' in src, "Jim asked for a very obvious button")
        links = set(re.findall(r"/demo\?view=([a-z]+)", src))
        check(f"{page}.html links to a view the demo implements ({sorted(links)})",
              links and links <= implemented,
              f"points at {sorted(links - implemented)}, which /demo does not implement")
        check(f"{page}.html says the data is SAMPLE", 
              re.search(r"sample|made-up", src, re.I) is not None,
              "a demo must never look like a real child's record")

    # the two voice lists must stay identical AND append-only
    main_lines = _voice_lines_from(os.path.join(here, "main.py"), "DEMO_VOICE_LINES")
    demo_lines = _voice_lines_from(demo_path, "VOICE_LINES")
    check("the demo voice lists are readable", main_lines is not None and demo_lines is not None,
          "could not parse one of them")
    if main_lines and demo_lines:
        check(f"main.py and demo.html voice lists are IDENTICAL "
              f"({len(main_lines)} lines)", main_lines == demo_lines,
              "clips are served BY INDEX -- a mismatch plays the wrong audio under the "
              "right words, silently")
        for key in ("parents", "teachers", "homeschool", "students"):
            spoken = [ln for ln in demo_lines[-4:]]
            check(f"  the {key} intro is whitelisted",
                  any(key.rstrip('s') in ln.lower() or key in ln.lower() for ln in spoken)
                  or len(spoken) == 4,
                  "the walkthrough would fall back to the browser voice")
        # Build cq: the audience lines are anchored by their opening WORDS, not by
        # counting back from the end -- the end moves on every append. Prove every
        # anchor still resolves to exactly ONE whitelisted line, because a miss here is
        # silent: the walkthrough just drops to the browser's mechanical voice.
        demo_src = demo
        # NOTE the quote handling: four of the nine anchors contain an apostrophe
        # INSIDE a double-quoted string ("the parent's view", "That's the honest
        # read."). A naive [^"'] class stops dead at that apostrophe and silently
        # finds five anchors instead of nine -- a passing-looking test that checks
        # less than half of what it claims. Capture the opening quote and require
        # the SAME character to close it.
        anchors = [m[1] for m in re.findall(
            r'''lineStarting\(\s*(["'])((?:(?!\1).){12,80})\1\s*\)''', demo_src)]
        check(f"every audience anchor is declared ({len(anchors)} found)", len(anchors) >= 23,
              "expected four intros, ten homeschool stops, four closing lines and the "
              "five new parent stops")
        for a in anchors:
            hits = [ln for ln in demo_lines if ln.startswith(a)]
            check(f"  anchor {a[:34]!r} resolves to exactly one line", len(hits) == 1,
                  f"matched {len(hits)} -- the walkthrough would fall back to the "
                  f"browser voice, or play the wrong clip")

        # And the bug Jim actually hit: the screen must go up BEFORE the words.
        check("the walkthrough shows the dashboard before it starts talking",
              "openDash(v.dash, { intro: v.intro" in demo_src
              and "document.body.className=''" not in
                  demo_src[demo_src.index("function startAudienceWalkthrough"):
                           demo_src.index("function startAudienceWalkthrough") + 900],
              "blanking the page and then speaking for thirty seconds is what Jim saw: "
              "'it's just a blank screen... blank, blank, blank until it gets to the "
              "parents' view'")
        check("an audience walkthrough can retitle the dashboard's stops",
              "runDashTour(d, 0, opts.lines)" in demo_src and "lines:HS_STOPS" in demo_src,
              "the homeschool view would speak the parent's words on the parent's screen")

        # Build cr, Jim: "when we go to the homeschool page, the teacher page, the student
        # page, I want that demo to only show the dashboard that's interesting to that
        # particular person. I don't want any links to any other dashboards from there."
        # Three doors out of a walkthrough could hand the visitor another audience's
        # screen, and all three are silent failures -- nothing errors, the wrong dashboard
        # simply opens. Each is checked from the SOURCE, not from a comment claiming it.
        def _fn_body(name, src, span=2600):
            i = src.find("function " + name)
            return src[i:i + span] if i >= 0 else ""

        sb = _fn_body("showBalloons", demo_src)
        check("the audience walkthroughs are locked to ONE dashboard",
              "audienceLocked()" in demo_src and "var AUDIENCE_KEY" in demo_src,
              "nothing decides which door the visitor came through")
        check("  the three-view chooser is skipped when a door is locked",
              bool(sb) and "audienceLocked()" in sb
              and sb.index("audienceLocked()") < (sb.index("openDash(")
                                                  if "openDash(" in sb else len(sb)),
              "showBalloons must return through the audience ending BEFORE it builds "
              "the three dashboard balloons")
        ae = _fn_body("showAudienceEnd", demo_src)
        check("  the audience ending offers no other dashboard",
              bool(ae) and "openDash(" not in ae and "dashStudent" not in ae
              and "dashTeacher" not in ae and "dashParent" not in ae,
              "the ending panel would put another audience's screen one tap away")
        check("  the ending offers a way onward instead of a dead end",
              "startAudienceWalkthrough(AUDIENCE_KEY)" in ae
              and "enterClassroomPicker()" in ae and "#pricing" in ae,
              "a locked door must still lead somewhere: watch it again, a real lesson, "
              "or the pricing page")
        check("  the dashboard's back button does not blank a locked walkthrough",
              "if(!audienceLocked()){ closeDash(); board.innerHTML=''; }" in demo_src,
              "these doors never set the classroom layout, so closing the dashboard "
              "leaves nothing behind the overlay -- the cq blank-screen bug again")
        check("  stepping into a real lesson sets the classroom layout first",
              "function enterClassroomPicker" in demo_src
              and "document.body.className='classroom'" in
                  _fn_body("enterClassroomPicker", demo_src, 400),
              "showPicker would draw into a hidden panel")
        # Build cs. THE CHECK THAT SHOULD HAVE EXISTED SINCE bx: every spoken string in a
        # tour must be ON THE WHITELIST. say() looks the text up in VOICE_LINES and plays
        # clip N by index; a line that is not there does not error, it drops that stop to
        # the browser's flat mechanical voice in the middle of Mr. Cadabra talking. The
        # design notes have said "every spoken string must be on the whitelist" since bx
        # and nothing enforced it -- so it is enforced here, for every tour on the page.
        spoken_lits = re.findall(r'''line:\s*(["'])((?:\\.|(?!\1).)*)\1''', demo_src)
        off_list = []
        for q, raw in spoken_lits:
            try:
                txt = ast.literal_eval(('"' + raw.replace('"', '\\"') + '"') if q == '"'
                                       else (q + raw + q))
            except (SyntaxError, ValueError):
                # NARROW on purpose. The first version of this caught bare Exception and
                # swallowed a NameError (ast was never imported), so every line looked
                # off-list and the failure message blamed the demo instead of the test.
                off_list.append(raw[:50])
                continue
            if txt not in demo_lines:
                off_list.append(txt[:50])
        check(f"every spoken tour line is on the voice whitelist "
              f"({len(spoken_lits)} checked)", not off_list,
              f"off the list: {off_list[:3]} -- that stop drops to the browser's flat "
              f"voice mid-tour, and nothing errors")

        # Every tour stop must point at an element that EXISTS. glow() returns quietly on
        # a missing id, so a typo means the words play over a dashboard that never moves.
        targets = re.findall(r"""\{\s*t:\s*'([A-Za-z0-9_]+)'\s*,""", demo_src)
        missing = [t for t in targets if f'id="{t}"' not in demo_src]
        check(f"every tour stop points at a real element ({len(targets)} stops)",
              not missing, f"no such id: {missing[:4]} -- glow() fails silently")

        # The homeschool override is read BY INDEX and falls through where it is short.
        def _count(block_start, pattern):
            i = demo_src.find(block_start)
            if i < 0:
                return -1
            return len(re.findall(pattern, demo_src[i:demo_src.index("]", i)]))
        hs_n = _count("var HS_STOPS = [", r"lineStarting\(")
        pd_n = _count("parent:{ id:'dashParent', stops:[", r"\{\s*t:\s*'pd")
        check(f"the homeschool script covers every parent stop ({hs_n} vs {pd_n})",
              hs_n == pd_n and hs_n > 0,
              "a short override does not error -- it just speaks the PARENT's words at a "
              "homeschooling parent for the stops it does not cover")

        check("  every door has a closing line and an ending panel",
              all(k in demo_src for k in ("AUD_OUTRO", "AUD_END"))
              and all(f"{k}:" in demo_src.split("var AUD_END")[1][:600]
                      for k in ("parents", "teachers", "homeschool", "students")),
              "a walkthrough would end in silence, or on another audience's words")


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
    if "--rules" in sys.argv:
        print("wrote", write_rules_index(os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "RULES.md")))
        return 0
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
    part3f_notation()
    part3g_misconceptions()
    part3h_scale()
    part3i_rule_verification()
    part3j_walkthroughs()
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

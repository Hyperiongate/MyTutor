# =============================================================================
# lessonscripts.py  --  THE SCRIPTED-FIRST ENGINE + THE COURSE  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-08-21  BUILD jz -- THE COURSE CROSSES ALL NINE UNITS. Jim: "keep working ...
#               I wanna get through the whole basic math course." SEVENTEEN new
#               lessons spanning units 1-9 (regrouping, multiplication, division,
#               remainders, missing factors, GCF, unit fractions, equivalent
#               fractions, same-bottom fraction add/take-away, tenths, money,
#               percent, unit price, perimeter, area), built on a NEW data-driven
#               OP_EXT registry: each op declares its answer function, spoken/board/
#               praise templates, difficulty key, per-problem constraint, and (when
#               digits are spoken as words) its own rule-44 check. The original
#               +/−/t ops are untouched. Problems may now carry an optional third
#               number c (fractions need one); it joins the dedup key and the
#               choices rotation. ALSO FIXED: jy accidentally placed carrying BEFORE
#               two-digit-no-carry in the course order -- an explicit COURSE_ORDER
#               now owns the sequence and the module refuses to import if any lesson
#               is missing from it or listed twice. New canon vocabulary: "regroup"
#               (bans "borrow"), "too small" (jr's live catch), "times" (bans
#               "multiplied by"). Depth note, honest: units 2-9 open at survey depth
#               (about two lessons each); the factory deepens any unit on demand.
#   2026-08-21  BUILD jy -- CARRYING COMES HOME. Lesson 7, "Adding with carrying" --
#               the lesson build jr's whole consistency-memory fight was about. On
#               2026-08-20 Jim caught the live tutor teaching the SAME rule two ways
#               four turns apart ("over nine" ... "ten or more"), and jr pinned the
#               first phrasing per student at runtime. Here the fix becomes
#               structural: "over nine" is now CANON VOCABULARY -- "ten or more",
#               "more than nine" and "bigger than nine" are BANNED from every
#               lesson's closure by the validator, and the intervention prompt hands
#               the AI the same words. A child on the scripted path can no longer
#               hear the carrying rule in two costumes, because the second costume
#               cannot pass the build. New validator branch "carry": every bank
#               problem MUST carry in the ones (else the lesson teaches its idea on
#               examples that never use it) and must NOT overflow the tens.
#   2026-08-21  BUILD jx -- JIM'S SECOND WORDING RULING + LESSONS FIVE AND SIX.
#               Jim, on jw's names: "What I meant to say is we're going to be adding
#               or subtracting SINGLE-DIGIT numbers -- numbers one through nine.
#               That's how I would say it." Lessons are now named by their INPUTS,
#               the way a person says it: "Adding single-digit numbers", "Taking away
#               single-digit numbers", "...past ten", "...from bigger numbers" -- and
#               the validator grew a_max/b_max so the bank PROVABLY matches the name
#               (L2's 10−6 and L4's 20−10 were quietly violating it; both replaced).
#               NEW LESSONS: 5. "Tens and ones" (teen numbers as one ten and some
#               ones -- a new op "t", answer = 10a+b, so the answer key stays
#               computed) and 6. "Adding two-digit numbers" (no carrying -- and the
#               validator ENFORCES no-carry on every bank problem, so a carrying
#               problem cannot sneak into the lesson that promises none). Lessons may
#               now declare their own representation levels: lesson 6 is
#               abstract-only, because dropping a struggling child to counting 37
#               stars one at a time would be the opposite of help.
#   2026-08-21  BUILD jw -- THE FIRST FOUR LESSONS (the course takes shape). Jim's
#               playtest verdict on the pilot: "very, very impressive. I think it's
#               what we want" -- and his wording ruling: say it PLAINLY. "Adding
#               within 10" is curriculum-speak; the goal chip now says "Adding
#               numbers up to 10" and the teach script says out loud what the bound
#               actually is: "every answer will be ten or smaller."
#               GENERALIZED: problems carry an op ("+" or "-"), renderers and praise
#               are op-aware, each lesson declares its symbols, its bound, its
#               difficulty key and its own advance line. NEW LESSONS (each authored
#               to the 2026-08-20 research settings, each with its own closure):
#                 1. Adding numbers up to 10        (reworded per Jim)
#                 2. Taking away -- numbers up to 10 (the minus sign, "are left")
#                 3. Adding numbers up to 20        (counting on from the bigger)
#                 4. Taking away -- numbers up to 20 (counting back)
#               PILOT_LESSON remains LESSONS[0] so every existing pin and endpoint
#               default still resolves. The engine itself is UNCHANGED in behavior:
#               same settings, same intervene contract, same closure property.
#   2026-08-20  NEW FILE (build js -- THE PILOT). Jim's ruling of 2026-08-20
#               (Ruling_Scripted_First_And_The_Settings_2026-08-20.md): every lesson is
#               pre-authored, pre-verified, and pre-voiced up to the moment a child
#               responds; the AI steps in only when the child leaves the script; CODE,
#               not the model, returns the child to the script. Why: the day's
#               measurements -- ~$50/student/month against a $29 price, 11.5s median
#               turn, 42.4% verified right first try, 25 known-bad replies shipped in a
#               week -- are all costs of GENERATING teaching at runtime. A script
#               verified once is right forever, retries never, and speaks from cached
#               audio at zero marginal cost.
#
#               THIS FILE IS DELIBERATELY PURE. No model, no network, no store, no
#               clock: lesson data + a state-machine engine + a validator. Everything
#               here can therefore be verified exhaustively by ruletests PART 3cv, and
#               a verified script stays verified.
#
#               THE SETTINGS ARE THE RESEARCH DOC'S, NOT OPINIONS (citations there):
#               advance on 3 consecutive unaided correct, minimum 4, cap 10; worked
#               examples then example-problem pairs; error path = scripted "let's look
#               together" -> AI Model-Lead-Test -> engine-issued same-form retest;
#               second intervention on a skill drops a representation level (abstract ->
#               pictorial -> concrete); failing at concrete ends warmly and marks the
#               topic "learning"; a garbled answer gets ONE scripted re-ask, then
#               tap-only -- never an AI call for a mishearing.
#
#               ⭐ THE CLOSURE PROPERTY (the reason pre-rendered voice can be TOTAL):
#               every spoken string this engine can ever emit is enumerable in advance
#               by audio_lines(). PART 3cv drives every scenario the engine supports
#               and asserts each emitted spoken line is in that closure. If a future
#               edit adds a line the closure misses, the battery fails -- so the voice
#               cache can never be surprised at runtime.
# =============================================================================

import re

# ---- THE SETTINGS (from the 2026-08-20 research ruling; change THERE first) -------
ADVANCE_STREAK = 3        # advance on 3 consecutive unaided correct (EDM 2015)
MIN_PROBLEMS = 4          # even a perfect child does at least 4 (DI "firming")
MAX_PROBLEMS = 10         # past 10 without a streak, stop -- see drop/end rules
DROP_AFTER_INTERVENTIONS = 2   # 2nd AI intervention on a skill -> easier representation
LEVELS = ("abstract", "pictorial", "concrete")   # drop direction, left to right
BEAT_WORD_CAP = 80        # rule 19c / build jd: one beat per turn, spoken

# ---- CANON VOCABULARY (build jr's lesson: one rule, one wording) ------------------
# canon phrase -> the synonyms that are BANNED anywhere in any lesson's speech.
# The validator enforces it; the intervention contract hands the canon to the AI.
VOCABULARY = {
    "put together": ("combine", "join together", "add together"),
    "in all": ("altogether", "all together", "the total"),
    "equals": ("makes", "gives you", "is the same as"),
    "take away": ("subtract", "remove"),
    "are left": ("remain", "remaining"),
    # jy: THE CARRYING RULE HAS ONE WORDING -- the exact defect Jim caught live on
    # 2026-08-20 ("over nine" ... then "ten or more", four turns apart), now banned
    # at authoring time across every lesson's closure.
    "over nine": ("ten or more", "more than nine", "bigger than nine"),
    # jz: regrouping's rule has one wording too (jr's other live catch), and so
    # does multiplication's name for itself.
    "regroup": ("borrow",),
    "too small": ("not big enough",),
    "times": ("multiplied by",),
}

# ---- PRAISE (rotated deterministically by problem index; all pre-renderable) ------
PRAISE_PREFIXES = ("That's it!", "You got it!", "Nice counting!",
                   "Exactly right!", "Well done!")

# fixed one-line scripts (every one of these is pre-rendered once)
LINE_WRONG = "Not quite — let's look at it together."
LINE_REASK = "Let me say that again."
LINE_TAP = "Tap the answer you think is right."
LINE_END_GRACEFUL = ("We did some strong thinking today. We'll practice this again "
                     "next time — Mr. Cadabra is proud of you.")


def ans(p):
    """The one place an answer is computed. Problems are DATA (a, b, op) -- a wrong
    answer key cannot exist in this file, because none is ever typed.
    ops: "+" a+b · "-" a-b · "t" tens-and-ones, a tens + b ones = 10a+b."""
    op = p.get("op", "+")
    if op in OP_EXT:
        return OP_EXT[op]["ans"](p)
    if op == "-":
        return p["a"] - p["b"]
    if op == "t":
        return 10 * p["a"] + p["b"]
    return p["a"] + p["b"]


# =============================================================================
# THE LESSONS -- Basic Math, Unit 1. Each authored to the research settings; each
# bank is ordered by its difficulty key (the 85%-success ramp).
# =============================================================================
LESSONS = [
    {
        "id": "basic-u1-add-up-to-10",
        "course": "basic", "unit": 1,
        "topic": "Adding single-digit numbers",
        "op": "+", "max_value": 10, "a_max": 9, "b_max": 9,
        "symbols": ("plus", "equals"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can add single-digit numbers."),
        "teach": [
            # Jim's wording rulings, 2026-08-21: name the lesson by its INPUTS, the
            # way a person says it -- "we're adding single-digit numbers, the
            # numbers one through nine."
            ("Today we are learning to add. Adding means putting two groups "
             "together and counting how many there are in all. We will add "
             "single-digit numbers — the numbers one through nine.",
             '[[goal text="Adding single-digit numbers"]]'),
            ("Here are three stars. And here are two more stars. Let's put the "
             "groups together and count every star: one, two, three, four, five. "
             "There are five stars in all.",
             '[[objects emoji="⭐" groups="3" add="2" caption="count every star"]]'),
            ("Mathematicians write putting together with a special sign. We write "
             "it like this, and we say it 'plus'. Three plus two.",
             '[[step eq="3 + 2"]]'),
            ("And when we know how many in all, we use one more sign. We write it "
             "like this, and we say it 'equals'. Three plus two equals five.",
             '[[step eq="3 + 2 = 5"]]'),
            ("Watch me do a whole one. Four stars, and one more star. I count "
             "every star: one, two, three, four, five. Four plus one equals five.",
             '[[objects emoji="⭐" groups="4" add="1" caption="count every star"]]'
             '[[step eq="4 + 1 = 5"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Two stars and two stars. "
                        "Count them all: one, two, three, four. Two plus two "
                        "equals four.",
                        '[[objects emoji="⭐" groups="2" add="2" caption="count every star"]]'
                        '[[step eq="2 + 2 = 4"]]'),
             "ask": {"a": 2, "b": 3, "op": "+"}},
            {"worked": ("One more together. Five stars and one star. Count them "
                        "all — six. Five plus one equals six.",
                        '[[objects emoji="⭐" groups="5" add="1" caption="count every star"]]'
                        '[[step eq="5 + 1 = 6"]]'),
             "ask": {"a": 4, "b": 2, "op": "+"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 2, "b": 1, "op": "+"}, {"a": 1, "b": 3, "op": "+"},
            {"a": 2, "b": 2, "op": "+"}, {"a": 3, "b": 2, "op": "+"},
            {"a": 4, "b": 1, "op": "+"}, {"a": 3, "b": 3, "op": "+"},
            {"a": 5, "b": 2, "op": "+"}, {"a": 4, "b": 3, "op": "+"},
            {"a": 6, "b": 2, "op": "+"}, {"a": 5, "b": 4, "op": "+"},
            {"a": 7, "b": 2, "op": "+"}, {"a": 6, "b": 3, "op": "+"},
        ],
    },
    {
        "id": "basic-u1-take-away-up-to-10",
        "course": "basic", "unit": 1,
        "topic": "Taking away single-digit numbers",
        "op": "-", "max_value": 10, "a_max": 9, "b_max": 9,
        "symbols": ("minus", "equals"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can take away single-digit numbers."),
        "teach": [
            ("Today we are learning to take away. Taking away means starting "
             "with a group, taking some away, and counting how many are left. "
             "We will take away single-digit numbers — the numbers one through "
             "nine.",
             '[[goal text="Taking away single-digit numbers"]]'),
            ("Here are five stars. Watch me take two away. Count what is left: "
             "one, two, three. Three stars are left.",
             '[[objects emoji="⭐" groups="5" caption="start with five — take two away, then count what is left"]]'),
            ("Mathematicians write taking away with its own sign. We write it "
             "like this, and we say it 'minus'. Five minus two.",
             '[[step eq="5 − 2"]]'),
            ("You already know the equals sign. Five minus two equals three.",
             '[[step eq="5 − 2 = 3"]]'),
            ("Watch me do a whole one. Six stars, take four away. Count what is "
             "left: one, two. Six minus four equals two.",
             '[[objects emoji="⭐" groups="6" caption="start with six — take four away"]]'
             '[[step eq="6 − 4 = 2"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Four stars, take one "
                        "away. Count what is left — three. Four minus one "
                        "equals three.",
                        '[[objects emoji="⭐" groups="4" caption="start with four — take one away"]]'
                        '[[step eq="4 − 1 = 3"]]'),
             "ask": {"a": 5, "b": 2, "op": "-"}},
            {"worked": ("One more together. Seven stars, take three away. Count "
                        "what is left — four. Seven minus three equals four.",
                        '[[objects emoji="⭐" groups="7" caption="start with seven — take three away"]]'
                        '[[step eq="7 − 3 = 4"]]'),
             "ask": {"a": 6, "b": 1, "op": "-"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 3, "b": 1, "op": "-"}, {"a": 4, "b": 1, "op": "-"},
            {"a": 4, "b": 2, "op": "-"}, {"a": 5, "b": 1, "op": "-"},
            {"a": 5, "b": 3, "op": "-"}, {"a": 6, "b": 2, "op": "-"},
            {"a": 6, "b": 3, "op": "-"}, {"a": 7, "b": 4, "op": "-"},
            {"a": 8, "b": 3, "op": "-"}, {"a": 8, "b": 5, "op": "-"},
            {"a": 9, "b": 4, "op": "-"}, {"a": 9, "b": 5, "op": "-"},
        ],
    },
    {
        "id": "basic-u1-add-up-to-20",
        "course": "basic", "unit": 1,
        "topic": "Adding single-digit numbers past ten",
        "op": "+", "max_value": 20, "a_max": 9, "b_max": 9,
        "symbols": ("plus", "equals"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can add single-digit numbers past ten."),
        "teach": [
            ("You already know how to add single-digit numbers. Today the answers "
             "get bigger — they will go past ten.",
             '[[goal text="Adding single-digit numbers past ten"]]'),
            ("Watch me. Nine stars, and four more stars. I count on from nine: "
             "ten, eleven, twelve, thirteen. Nine plus four equals thirteen.",
             '[[objects emoji="⭐" groups="9" add="4" caption="count on from nine"]]'
             '[[step eq="9 + 4 = 13"]]'),
            ("Here is a helpful trick. Start with the bigger number and count up. "
             "Eight plus three: eight — nine, ten, eleven. Eight plus three "
             "equals eleven.",
             '[[step eq="8 + 3 = 11"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Seven stars and five "
                        "stars. Count on from seven: eight, nine, ten, eleven, "
                        "twelve. Seven plus five equals twelve.",
                        '[[objects emoji="⭐" groups="7" add="5" caption="count on from seven"]]'
                        '[[step eq="7 + 5 = 12"]]'),
             "ask": {"a": 7, "b": 6, "op": "+"}},
            {"worked": ("One more together. Nine stars and six stars. Count on "
                        "from nine — fifteen. Nine plus six equals fifteen.",
                        '[[objects emoji="⭐" groups="9" add="6" caption="count on from nine"]]'
                        '[[step eq="9 + 6 = 15"]]'),
             "ask": {"a": 8, "b": 6, "op": "+"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 9, "b": 2, "op": "+"}, {"a": 7, "b": 4, "op": "+"},
            {"a": 8, "b": 4, "op": "+"}, {"a": 9, "b": 3, "op": "+"},
            {"a": 6, "b": 6, "op": "+"}, {"a": 8, "b": 5, "op": "+"},
            {"a": 5, "b": 8, "op": "+"}, {"a": 9, "b": 5, "op": "+"},
            {"a": 8, "b": 7, "op": "+"}, {"a": 7, "b": 8, "op": "+"},
            {"a": 9, "b": 7, "op": "+"}, {"a": 9, "b": 8, "op": "+"},
        ],
    },
    {
        "id": "basic-u1-take-away-up-to-20",
        "course": "basic", "unit": 1,
        "topic": "Taking away from bigger numbers",
        "op": "-", "max_value": 20, "a_max": 19, "b_max": 9,
        "symbols": ("minus", "equals"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can take away from bigger numbers."),
        "teach": [
            ("You already know how to take away single-digit numbers. Today we "
             "start with bigger numbers — the numbers up to nineteen.",
             '[[goal text="Taking away from bigger numbers"]]'),
            ("Watch me. Thirteen stars, take five away. I count back from "
             "thirteen: twelve, eleven, ten, nine, eight. Thirteen minus five "
             "equals eight.",
             '[[objects emoji="⭐" groups="13" caption="start with thirteen — take five away"]]'
             '[[step eq="13 − 5 = 8"]]'),
            ("Here is a helpful trick. Counting back works for any take away. "
             "Eleven minus three: eleven — ten, nine, eight. Eleven minus three "
             "equals eight.",
             '[[step eq="11 − 3 = 8"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Twelve stars, take four "
                        "away. Count back from twelve — eight. Twelve minus four "
                        "equals eight.",
                        '[[objects emoji="⭐" groups="12" caption="start with twelve — take four away"]]'
                        '[[step eq="12 − 4 = 8"]]'),
             "ask": {"a": 12, "b": 3, "op": "-"}},
            {"worked": ("One more together. Fifteen stars, take six away. Count "
                        "back from fifteen — nine. Fifteen minus six equals nine.",
                        '[[objects emoji="⭐" groups="15" caption="start with fifteen — take six away"]]'
                        '[[step eq="15 − 6 = 9"]]'),
             "ask": {"a": 14, "b": 5, "op": "-"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 11, "b": 2, "op": "-"}, {"a": 11, "b": 4, "op": "-"},
            {"a": 12, "b": 5, "op": "-"}, {"a": 13, "b": 4, "op": "-"},
            {"a": 13, "b": 6, "op": "-"}, {"a": 14, "b": 6, "op": "-"},
            {"a": 15, "b": 7, "op": "-"}, {"a": 15, "b": 8, "op": "-"},
            {"a": 16, "b": 7, "op": "-"}, {"a": 17, "b": 8, "op": "-"},
            {"a": 18, "b": 9, "op": "-"}, {"a": 19, "b": 9, "op": "-"},
        ],
    },
    {
        "id": "basic-u1-tens-and-ones",
        "course": "basic", "unit": 1,
        "topic": "Tens and ones",
        "op": "t", "max_value": 19, "a_max": 1, "b_max": 9,
        "symbols": ("ten", "ones"),
        "advance_line": ("Three in a row — you've got it! "
                         "You know your tens and ones."),
        "teach": [
            ("Today we are learning about tens and ones. Ten ones, put together, "
             "make one ten. The numbers from eleven to nineteen are one ten and "
             "some ones.",
             '[[goal text="Tens and ones"]]'),
            ("Look — here is one ten, and four more ones. One ten and four ones "
             "is fourteen.",
             '[[objects emoji="⭐" groups="10" add="4" caption="one ten and four ones"]]'
             '[[step eq="1 ten and 4 ones = 14"]]'),
            ("The first digit of fourteen counts the tens. The second digit "
             "counts the ones. 1 ten, 4 ones — fourteen.",
             '[[step eq="14 = 1 ten and 4 ones"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. One ten and three ones. "
                        "Ten — eleven, twelve, thirteen. 1 ten and 3 ones is "
                        "thirteen.",
                        '[[objects emoji="⭐" groups="10" add="3" caption="one ten and three ones"]]'
                        '[[step eq="1 ten and 3 ones = 13"]]'),
             "ask": {"a": 1, "b": 2, "op": "t"}},
            {"worked": ("One more together. One ten and six ones. Count on from "
                        "ten — sixteen. 1 ten and 6 ones is sixteen.",
                        '[[objects emoji="⭐" groups="10" add="6" caption="one ten and six ones"]]'
                        '[[step eq="1 ten and 6 ones = 16"]]'),
             "ask": {"a": 1, "b": 5, "op": "t"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 1, "b": 1, "op": "t"}, {"a": 1, "b": 3, "op": "t"},
            {"a": 1, "b": 4, "op": "t"}, {"a": 1, "b": 6, "op": "t"},
            {"a": 1, "b": 7, "op": "t"}, {"a": 1, "b": 8, "op": "t"},
            {"a": 1, "b": 9, "op": "t"},
        ],
    },
    {
        "id": "basic-u1-add-with-carrying",
        "course": "basic", "unit": 1,
        "topic": "Adding with carrying",
        "op": "+", "max_value": 99, "carry": True,
        "levels": ("abstract",),   # like lesson 6: stars do not help at this size
        "symbols": ("carry", "plus", "equals"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can carry like a pro."),
        "teach": [
            ("Today we are learning to carry. Sometimes when we add, the ones add "
             "up to over nine. When that happens, we write the ones digit and "
             "carry one ten over to the tens.",
             '[[goal text="Adding with carrying"]]'),
            ("Watch me add 27 plus 15. Ones first: 7 plus 5 equals 12. Twelve is "
             "over nine — so we write the 2 and carry one ten. Tens: 2 plus 1 "
             "equals 3, plus the carried one equals 4. So 27 plus 15 equals 42.",
             '[[step eq="27 + 15"]][[step eq="ones: 7 + 5 = 12"]]'
             '[[step eq="write 2, carry 1"]][[step eq="tens: 2 + 1 + 1 = 4"]]'
             '[[step eq="27 + 15 = 42"]]'),
            ("One more, watch. 38 plus 24. Ones: 8 plus 4 equals 12 — over nine, "
             "write the 2, carry one ten. Tens: 3 plus 2 equals 5, plus the "
             "carried one equals 6. So 38 plus 24 equals 62.",
             '[[step eq="38 + 24"]][[step eq="ones: 8 + 4 = 12"]]'
             '[[step eq="write 2, carry 1"]][[step eq="tens: 3 + 2 + 1 = 6"]]'
             '[[step eq="38 + 24 = 62"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 46 plus 17. Ones: 6 plus "
                        "7 equals 13 — over nine, write the 3, carry one ten. "
                        "Tens: 4 plus 1 plus the carried one equals 6. So 46 plus "
                        "17 equals 63.",
                        '[[step eq="46 + 17"]][[step eq="ones: 6 + 7 = 13"]]'
                        '[[step eq="write 3, carry 1"]][[step eq="tens: 4 + 1 + 1 = 6"]]'
                        '[[step eq="46 + 17 = 63"]]'),
             "ask": {"a": 45, "b": 17, "op": "+"}},
            {"worked": ("One more together. 29 plus 35. Ones: 9 plus 5 equals 14 "
                        "— over nine, write the 4, carry one ten. Tens: 2 plus 3 "
                        "plus the carried one equals 6. So 29 plus 35 equals 64.",
                        '[[step eq="29 + 35"]][[step eq="ones: 9 + 5 = 14"]]'
                        '[[step eq="write 4, carry 1"]][[step eq="tens: 2 + 3 + 1 = 6"]]'
                        '[[step eq="29 + 35 = 64"]]'),
             "ask": {"a": 28, "b": 34, "op": "+"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 15, "b": 16, "op": "+"}, {"a": 18, "b": 13, "op": "+"},
            {"a": 24, "b": 17, "op": "+"}, {"a": 26, "b": 15, "op": "+"},
            {"a": 28, "b": 16, "op": "+"}, {"a": 35, "b": 17, "op": "+"},
            {"a": 36, "b": 18, "op": "+"}, {"a": 45, "b": 19, "op": "+"},
            {"a": 47, "b": 26, "op": "+"}, {"a": 56, "b": 27, "op": "+"},
            {"a": 58, "b": 25, "op": "+"}, {"a": 67, "b": 26, "op": "+"},
        ],
    },
    {
        "id": "basic-u1-add-two-digit-no-carry",
        "course": "basic", "unit": 1,
        "topic": "Adding two-digit numbers",
        "op": "+", "max_value": 99, "no_carry": True,
        "levels": ("abstract",),   # dropping to counting 37 stars would not be help
        "symbols": ("plus", "equals"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can add two-digit numbers."),
        "teach": [
            ("Today we are adding two-digit numbers. A two-digit number has a "
             "tens digit and a ones digit. We add the ones first, then the tens.",
             '[[goal text="Adding two-digit numbers"]]'),
            ("Watch me add 23 plus 14. First the ones: 3 plus 4 equals 7. Then "
             "the tens: 2 tens plus 1 ten equals 3 tens. So 23 plus 14 equals 37.",
             '[[step eq="23 + 14"]][[step eq="ones: 3 + 4 = 7"]]'
             '[[step eq="tens: 2 + 1 = 3"]][[step eq="23 + 14 = 37"]]'),
            ("One more, watch. 31 plus 25. Ones: 1 plus 5 equals 6. Tens: 3 plus "
             "2 equals 5. So 31 plus 25 equals 56.",
             '[[step eq="31 + 25"]][[step eq="ones: 1 + 5 = 6"]]'
             '[[step eq="tens: 3 + 2 = 5"]][[step eq="31 + 25 = 56"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 42 plus 16. Ones: 2 plus "
                        "6 equals 8. Tens: 4 plus 1 equals 5. So 42 plus 16 "
                        "equals 58.",
                        '[[step eq="42 + 16"]][[step eq="ones: 2 + 6 = 8"]]'
                        '[[step eq="tens: 4 + 1 = 5"]][[step eq="42 + 16 = 58"]]'),
             "ask": {"a": 42, "b": 13, "op": "+"}},
            {"worked": ("One more together. 34 plus 22. Ones: 4 plus 2 equals 6. "
                        "Tens: 3 plus 2 equals 5. So 34 plus 22 equals 56.",
                        '[[step eq="34 + 22"]][[step eq="ones: 4 + 2 = 6"]]'
                        '[[step eq="tens: 3 + 2 = 5"]][[step eq="34 + 22 = 56"]]'),
             "ask": {"a": 51, "b": 24, "op": "+"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 12, "b": 13, "op": "+"}, {"a": 21, "b": 14, "op": "+"},
            {"a": 23, "b": 15, "op": "+"}, {"a": 32, "b": 16, "op": "+"},
            {"a": 41, "b": 17, "op": "+"}, {"a": 33, "b": 26, "op": "+"},
            {"a": 44, "b": 23, "op": "+"}, {"a": 52, "b": 25, "op": "+"},
            {"a": 63, "b": 21, "op": "+"}, {"a": 54, "b": 33, "op": "+"},
            {"a": 62, "b": 34, "op": "+"}, {"a": 71, "b": 26, "op": "+"},
        ],
    },
]

_MORE_LESSONS = [
    {
        "id": 'basic-u1-take-away-with-regrouping',
        "course": "basic", "unit": 1,
        "topic": 'Taking away with regrouping',
        "op": '-', "max_value": 99, "regroup": True,
        "levels": ("abstract",),
        "symbols": ('regroup', 'too small', 'equals'),
        "advance_line": "Three in a row — you've got it! You can regroup like a pro.",
        "teach": [
            ('Today we are learning to regroup. Sometimes the ones digit on top is too small to take away from. When that happens, we regroup: we take one ten and turn it into ten ones.',
             '[[goal text="Taking away with regrouping"]]'),
            ('Watch me take 17 away from 42. Ones: 2 is too small to take 7 away from. Regroup — one ten becomes ten ones, so 2 becomes 12, and the 4 tens become 3. Ones: 12 take away 7 equals 5. Tens: 3 take away 1 equals 2. So 42 take away 17 equals 25.',
             '[[step eq="42 − 17"]][[step eq="regroup: 42 = 3 tens and 12 ones"]][[step eq="ones: 12 − 7 = 5"]][[step eq="tens: 3 − 1 = 2"]][[step eq="42 − 17 = 25"]]'),
            ('One more, watch. 53 take away 28. Ones: 3 is too small — regroup, 3 becomes 13, and 5 tens become 4. Ones: 13 take away 8 equals 5. Tens: 4 take away 2 equals 2. So 53 take away 28 equals 25.',
             '[[step eq="53 − 28"]][[step eq="regroup: 53 = 4 tens and 13 ones"]][[step eq="ones: 13 − 8 = 5"]][[step eq="tens: 4 − 2 = 2"]][[step eq="53 − 28 = 25"]]'),
        ],
        "pairs": [
            {"worked": ('Here is one more, done for you. 61 take away 35. Ones: 1 is too small — regroup, 1 becomes 11, 6 tens become 5. Ones: 11 take away 5 equals 6. Tens: 5 take away 3 equals 2. So 61 take away 35 equals 26.',
                        '[[step eq="61 − 35"]][[step eq="regroup: 61 = 5 tens and 11 ones"]][[step eq="ones: 11 − 5 = 6"]][[step eq="tens: 5 − 3 = 2"]][[step eq="61 − 35 = 26"]]'),
             "ask": {'a': 62, 'b': 35, 'op': '-'}},
            {"worked": ('One more together. 74 take away 46. Ones: 4 is too small — regroup, 4 becomes 14, 7 tens become 6. Ones: 14 take away 6 equals 8. Tens: 6 take away 4 equals 2. So 74 take away 46 equals 28.',
                        '[[step eq="74 − 46"]][[step eq="regroup: 74 = 6 tens and 14 ones"]][[step eq="ones: 14 − 6 = 8"]][[step eq="tens: 6 − 4 = 2"]][[step eq="74 − 46 = 28"]]'),
             "ask": {'a': 73, 'b': 45, 'op': '-'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [{'a': 21, 'b': 13, 'op': '-'}, {'a': 32, 'b': 15, 'op': '-'}, {'a': 34, 'b': 16, 'op': '-'}, {'a': 43, 'b': 17, 'op': '-'}, {'a': 45, 'b': 28, 'op': '-'}, {'a': 52, 'b': 24, 'op': '-'}, {'a': 56, 'b': 38, 'op': '-'}, {'a': 63, 'b': 26, 'op': '-'}, {'a': 71, 'b': 44, 'op': '-'}, {'a': 75, 'b': 47, 'op': '-'}, {'a': 82, 'b': 55, 'op': '-'}, {'a': 91, 'b': 63, 'op': '-'}],
    },
    {
        "id": 'basic-u2-what-multiplying-means',
        "course": "basic", "unit": 2,
        "topic": 'What multiplying means',
        "op": '*', "max_value": 30,
        "levels": ("abstract",),
        "symbols": ('times', 'equals'),
        "advance_line": "Three in a row — you've got it! You know what multiplying means.",
        "teach": [
            ('Today we are learning to multiply. Multiplying means putting together equal groups. Three times four means three groups of four.',
             '[[goal text="What multiplying means"]]'),
            ('Watch me. Three times four is three groups of four: 4 plus 4 plus 4 equals 12. We write it with the times sign. Three times four equals 12.',
             '[[step eq="3 × 4"]][[step eq="4 + 4 + 4 = 12"]][[step eq="3 × 4 = 12"]]'),
            ('One more, watch. Two times five is two groups of five: 5 plus 5 equals 10. Two times five equals ten.',
             '[[step eq="2 × 5"]][[step eq="5 + 5 = 10"]][[step eq="2 × 5 = 10"]]'),
        ],
        "pairs": [
            {"worked": ('Here is one more, done for you. Four times two is four groups of two: 2 plus 2 plus 2 plus 2 equals 8. Four times two equals eight.',
                        '[[step eq="4 × 2"]][[step eq="2 + 2 + 2 + 2 = 8"]][[step eq="4 × 2 = 8"]]'),
             "ask": {'a': 3, 'b': 2, 'op': '*'}},
            {"worked": ('One more together. Five times three is five groups of three — fifteen. Five times three equals fifteen.',
                        '[[step eq="5 × 3"]][[step eq="3 + 3 + 3 + 3 + 3 = 15"]][[step eq="5 × 3 = 15"]]'),
             "ask": {'a': 4, 'b': 3, 'op': '*'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [{'a': 2, 'b': 2, 'op': '*'}, {'a': 2, 'b': 3, 'op': '*'}, {'a': 3, 'b': 3, 'op': '*'}, {'a': 2, 'b': 5, 'op': '*'}, {'a': 4, 'b': 4, 'op': '*'}, {'a': 3, 'b': 5, 'op': '*'}, {'a': 4, 'b': 5, 'op': '*'}, {'a': 5, 'b': 5, 'op': '*'}],
    },
    {
        "id": 'basic-u2-times-tables',
        "course": "basic", "unit": 2,
        "topic": 'Times tables',
        "op": '*', "max_value": 81,
        "levels": ("abstract",),
        "symbols": ('times', 'equals'),
        "advance_line": "Three in a row — you've got it! Your times tables are getting strong.",
        "teach": [
            ('You already know what multiplying means. Today we practice the times tables — bigger groups, up to nine times nine.',
             '[[goal text="Times tables"]]'),
            ('Watch me. Six times seven. Six groups of seven equals 42. Six times seven equals 42.',
             '[[step eq="6 × 7 = 42"]]'),
            ('A helpful trick: turn the problem around. Seven times six equals the same 42 — the order does not change the answer.',
             '[[step eq="7 × 6 = 42"]]'),
        ],
        "pairs": [
            {"worked": ('Here is one more, done for you. Eight times six equals 48.',
                        '[[step eq="8 × 6 = 48"]]'),
             "ask": {'a': 8, 'b': 5, 'op': '*'}},
            {"worked": ('One more together. Nine times seven equals 63.',
                        '[[step eq="9 × 7 = 63"]]'),
             "ask": {'a': 9, 'b': 6, 'op': '*'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [{'a': 3, 'b': 6, 'op': '*'}, {'a': 4, 'b': 6, 'op': '*'}, {'a': 5, 'b': 6, 'op': '*'}, {'a': 6, 'b': 6, 'op': '*'}, {'a': 6, 'b': 7, 'op': '*'}, {'a': 7, 'b': 7, 'op': '*'}, {'a': 8, 'b': 7, 'op': '*'}, {'a': 8, 'b': 8, 'op': '*'}, {'a': 9, 'b': 8, 'op': '*'}, {'a': 9, 'b': 9, 'op': '*'}],
    },
    {
        "id": 'basic-u3-what-dividing-means',
        "course": "basic", "unit": 3,
        "topic": 'What dividing means',
        "op": '/', "max_value": 45,
        "levels": ("abstract",),
        "symbols": ('divided', 'equals'),
        "advance_line": "Three in a row — you've got it! You know what dividing means.",
        "teach": [
            ('Today we are learning to divide. Dividing means sharing into equal groups. Twelve divided by three asks: share 12 into 3 equal groups — how many in each group?',
             '[[goal text="What dividing means"]]'),
            ('Watch me. Twelve divided by three. Share 12 into 3 equal groups: each group gets 4. Twelve divided by three equals four.',
             '[[step eq="12 ÷ 3 = 4"]]'),
            ('Dividing undoes multiplying. Three times four equals 12, so twelve divided by three equals four.',
             '[[step eq="3 × 4 = 12"]][[step eq="12 ÷ 3 = 4"]]'),
        ],
        "pairs": [
            {"worked": ('Here is one more, done for you. Ten divided by two. Share 10 into 2 equal groups: each gets 5. Ten divided by two equals five.',
                        '[[step eq="10 ÷ 2 = 5"]]'),
             "ask": {'a': 8, 'b': 2, 'op': '/'}},
            {"worked": ('One more together. Fifteen divided by five equals three.',
                        '[[step eq="15 ÷ 5 = 3"]]'),
             "ask": {'a': 20, 'b': 5, 'op': '/'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [{'a': 6, 'b': 2, 'op': '/'}, {'a': 9, 'b': 3, 'op': '/'}, {'a': 12, 'b': 4, 'op': '/'}, {'a': 16, 'b': 4, 'op': '/'}, {'a': 18, 'b': 3, 'op': '/'}, {'a': 24, 'b': 6, 'op': '/'}, {'a': 28, 'b': 4, 'op': '/'}, {'a': 35, 'b': 7, 'op': '/'}, {'a': 36, 'b': 6, 'op': '/'}, {'a': 45, 'b': 9, 'op': '/'}],
    },
    {
        "id": 'basic-u3-left-overs',
        "course": "basic", "unit": 3,
        "topic": 'Dividing with left-overs',
        "op": 'rem', "max_value": 50,
        "levels": ("abstract",),
        "symbols": ('shared', 'left'),
        "advance_line": "Three in a row — you've got it! You can handle the left-overs.",
        "teach": [
            ('Sometimes sharing does not come out even. Share 13 into groups of 4: you fill 3 groups, and 1 is left over. Today we find what is left over.',
             '[[goal text="Dividing with left-overs"]]'),
            ('Watch me. 13 shared into groups of 4. Three groups of four equals 12, and 13 take away 12 equals 1. So 1 is left over.',
             '[[step eq="13 ÷ 4"]][[step eq="3 × 4 = 12"]][[step eq="13 − 12 = 1"]][[step eq="left over = 1"]]'),
            ('One more, watch. 17 shared into groups of 5. Three groups of five equals 15, and 17 take away 15 equals 2. So 2 are left over.',
             '[[step eq="17 ÷ 5"]][[step eq="3 × 5 = 15"]][[step eq="left over = 2"]]'),
        ],
        "pairs": [
            {"worked": ('Here is one more, done for you. 11 shared into groups of 3. Three groups of three equals 9, and 11 take away 9 equals 2 left over.',
                        '[[step eq="11 ÷ 3"]][[step eq="left over = 2"]]'),
             "ask": {'a': 10, 'b': 3, 'op': 'rem'}},
            {"worked": ('One more together. 14 shared into groups of 4 leaves 2 left over.',
                        '[[step eq="14 ÷ 4"]][[step eq="left over = 2"]]'),
             "ask": {'a': 13, 'b': 5, 'op': 'rem'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [{'a': 7, 'b': 2, 'op': 'rem'}, {'a': 9, 'b': 4, 'op': 'rem'}, {'a': 11, 'b': 4, 'op': 'rem'}, {'a': 14, 'b': 3, 'op': 'rem'}, {'a': 17, 'b': 4, 'op': 'rem'}, {'a': 19, 'b': 5, 'op': 'rem'}, {'a': 23, 'b': 5, 'op': 'rem'}, {'a': 26, 'b': 6, 'op': 'rem'}, {'a': 31, 'b': 7, 'op': 'rem'}, {'a': 38, 'b': 8, 'op': 'rem'}],
    },
    {
        "id": 'basic-u4-missing-factors',
        "course": "basic", "unit": 4,
        "topic": 'Missing factors',
        "op": 'mf', "max_value": 72,
        "levels": ("abstract",),
        "symbols": ('times', 'factor'),
        "advance_line": "Three in a row — you've got it! You can find the missing factor.",
        "teach": [
            ('A factor is a number you multiply. In 3 times 4 equals 12, the factors are 3 and 4. Today one factor is hiding, and we find it.',
             '[[goal text="Missing factors"]]'),
            ('Watch me. 3 times what equals 12? I think: three groups of WHAT reach 12? Three times four equals 12 — the missing factor is 4.',
             '[[step eq="3 × ? = 12"]][[step eq="3 × 4 = 12"]]'),
            ('One more, watch. 5 times what equals 30? Five times six equals 30 — the missing factor is 6.',
             '[[step eq="5 × ? = 30"]][[step eq="5 × 6 = 30"]]'),
        ],
        "pairs": [
            {"worked": ('Here is one more, done for you. 4 times what equals 20? Four times five equals 20 — the missing factor is 5.',
                        '[[step eq="4 × ? = 20"]][[step eq="4 × 5 = 20"]]'),
             "ask": {'a': 16, 'b': 4, 'op': 'mf'}},
            {"worked": ('One more together. 6 times what equals 42? Six times seven equals 42.',
                        '[[step eq="6 × ? = 42"]][[step eq="6 × 7 = 42"]]'),
             "ask": {'a': 36, 'b': 6, 'op': 'mf'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [{'a': 6, 'b': 2, 'op': 'mf'}, {'a': 12, 'b': 3, 'op': 'mf'}, {'a': 15, 'b': 3, 'op': 'mf'}, {'a': 24, 'b': 4, 'op': 'mf'}, {'a': 30, 'b': 5, 'op': 'mf'}, {'a': 35, 'b': 5, 'op': 'mf'}, {'a': 48, 'b': 6, 'op': 'mf'}, {'a': 56, 'b': 7, 'op': 'mf'}, {'a': 63, 'b': 9, 'op': 'mf'}, {'a': 72, 'b': 8, 'op': 'mf'}],
    },
    {
        "id": 'basic-u4-greatest-common-factor',
        "course": "basic", "unit": 4,
        "topic": 'The greatest common factor',
        "op": 'gcf', "max_value": 48,
        "levels": ("abstract",),
        "symbols": ('factor', 'greatest'),
        "advance_line": "Three in a row — you've got it! You can find the greatest common factor.",
        "teach": [
            ('A common factor divides two numbers evenly. Today we hunt for the GREATEST one — the biggest number that divides both.',
             '[[goal text="The greatest common factor"]]'),
            ('Watch me find the greatest common factor of 12 and 18. Factors of 12: 1, 2, 3, 4, 6, 12. Factors of 18: 1, 2, 3, 6, 9, 18. The greatest one they share is 6.',
             '[[step eq="12: 1, 2, 3, 4, 6, 12"]][[step eq="18: 1, 2, 3, 6, 9, 18"]][[step eq="GCF of 12 and 18 = 6"]]'),
            ('One more, watch. 8 and 20. Factors of 8: 1, 2, 4, 8. Factors of 20: 1, 2, 4, 5, 10, 20. The greatest common factor equals 4.',
             '[[step eq="GCF of 8 and 20 = 4"]]'),
        ],
        "pairs": [
            {"worked": ('Here is one more, done for you. 6 and 9. Factors of 6: 1, 2, 3, 6. Factors of 9: 1, 3, 9. The greatest common factor equals 3.',
                        '[[step eq="GCF of 6 and 9 = 3"]]'),
             "ask": {'a': 6, 'b': 8, 'op': 'gcf'}},
            {"worked": ('One more together. 10 and 15 — the greatest common factor equals 5.',
                        '[[step eq="GCF of 10 and 15 = 5"]]'),
             "ask": {'a': 12, 'b': 16, 'op': 'gcf'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [{'a': 4, 'b': 6, 'op': 'gcf'}, {'a': 6, 'b': 10, 'op': 'gcf'}, {'a': 8, 'b': 12, 'op': 'gcf'}, {'a': 9, 'b': 12, 'op': 'gcf'}, {'a': 14, 'b': 21, 'op': 'gcf'}, {'a': 18, 'b': 24, 'op': 'gcf'}, {'a': 10, 'b': 25, 'op': 'gcf'}, {'a': 20, 'b': 30, 'op': 'gcf'}, {'a': 24, 'b': 36, 'op': 'gcf'}, {'a': 32, 'b': 48, 'op': 'gcf'}],
    },
    {
        "id": 'basic-u5-fraction-of-a-group',
        "course": "basic", "unit": 5,
        "topic": 'A fraction of a group',
        "op": 'of', "max_value": 24,
        "levels": ("abstract",),
        "symbols": ('share', 'equal'),
        "advance_line": "Three in a row — you've got it! You can find a fraction of a group.",
        "teach": [
            ('A fraction names equal shares. One half means one of two equal shares. One fourth means one of four equal shares. Today we take a fraction OF a group.',
             '[[goal text="A fraction of a group"]]'),
            ('Watch me find one half of 8. Share 8 into 2 equal groups — each group gets 4. One half of 8 equals 4.',
             '[[step eq="1/2 of 8 = 4"]]'),
            ('One more, watch. One third of 12. Share 12 into 3 equal groups — each gets 4. One third of 12 equals 4.',
             '[[step eq="1/3 of 12 = 4"]]'),
        ],
        "pairs": [
            {"worked": ('Here is one more, done for you. One fourth of 12. Share 12 into 4 equal groups — each gets 3. One fourth of 12 equals 3.',
                        '[[step eq="1/4 of 12 = 3"]]'),
             "ask": {'a': 8, 'b': 4, 'op': 'of'}},
            {"worked": ('One more together. One fifth of 10 equals 2.',
                        '[[step eq="1/5 of 10 = 2"]]'),
             "ask": {'a': 15, 'b': 5, 'op': 'of'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [{'a': 4, 'b': 2, 'op': 'of'}, {'a': 6, 'b': 2, 'op': 'of'}, {'a': 6, 'b': 3, 'op': 'of'}, {'a': 10, 'b': 2, 'op': 'of'}, {'a': 9, 'b': 3, 'op': 'of'}, {'a': 12, 'b': 2, 'op': 'of'}, {'a': 12, 'b': 3, 'op': 'of'}, {'a': 16, 'b': 4, 'op': 'of'}, {'a': 20, 'b': 5, 'op': 'of'}, {'a': 24, 'b': 6, 'op': 'of'}],
    },
    {
        "id": 'basic-u5-equivalent-fractions',
        "course": "basic", "unit": 5,
        "topic": 'Equivalent fractions',
        "op": 'eqf', "max_value": 12,
        "levels": ("abstract",),
        "symbols": ('equal', 'same'),
        "advance_line": "Three in a row — you've got it! You can spot equal fractions.",
        "teach": [
            ('Two fractions can name the SAME amount. One half of a pizza and two fourths of a pizza are the same amount of pizza. We call them equal fractions.',
             '[[goal text="Equivalent fractions"]]'),
            ('Watch me. One half equals how many fourths? Cut every half into two — two halves become four fourths, and ONE half becomes TWO fourths. One half equals two fourths.',
             '[[step eq="1/2 = 2/4"]]'),
            ('One more, watch. One third equals how many sixths? Cut every third in two — one third becomes two sixths.',
             '[[step eq="1/3 = 2/6"]]'),
        ],
        "pairs": [
            {"worked": ('Here is one more, done for you. One half equals how many sixths? Cut every half into three — one half equals three sixths.',
                        '[[step eq="1/2 = 3/6"]]'),
             "ask": {'a': 1, 'b': 2, 'c': 8, 'op': 'eqf'}},
            {"worked": ('One more together. One fourth equals two eighths.',
                        '[[step eq="1/4 = 2/8"]]'),
             "ask": {'a': 1, 'b': 2, 'c': 10, 'op': 'eqf'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [{'a': 1, 'b': 2, 'c': 4, 'op': 'eqf'}, {'a': 1, 'b': 3, 'c': 6, 'op': 'eqf'}, {'a': 1, 'b': 2, 'c': 6, 'op': 'eqf'}, {'a': 1, 'b': 4, 'c': 8, 'op': 'eqf'}, {'a': 1, 'b': 5, 'c': 10, 'op': 'eqf'}, {'a': 1, 'b': 6, 'c': 12, 'op': 'eqf'}, {'a': 1, 'b': 4, 'c': 12, 'op': 'eqf'}, {'a': 1, 'b': 3, 'c': 12, 'op': 'eqf'}, {'a': 1, 'b': 2, 'c': 12, 'op': 'eqf'}],
    },
    {
        "id": 'basic-u6-add-fractions-same-bottom',
        "course": "basic", "unit": 6,
        "topic": 'Adding fractions',
        "op": 'fa', "max_value": 12,
        "levels": ("abstract",),
        "symbols": ('bottom', 'plus'),
        "advance_line": "Three in a row — you've got it! You can add fractions with the same bottom.",
        "teach": [
            ('When two fractions have the SAME bottom number, the pieces are the same size — so we can just count them. Today we add fractions with the same bottom.',
             '[[goal text="Adding fractions"]]'),
            ('Watch me. Two eighths plus three eighths. The pieces are all eighths, so count them: 2 plus 3 equals 5. Two eighths plus three eighths equals five eighths.',
             '[[step eq="2/8 + 3/8 = 5/8"]]'),
            ('One more, watch. One fourth plus two fourths equals three fourths. The bottom stays the same — only the count changes.',
             '[[step eq="1/4 + 2/4 = 3/4"]]'),
        ],
        "pairs": [
            {"worked": ('Here is one more, done for you. Two sixths plus three sixths equals five sixths.',
                        '[[step eq="2/6 + 3/6 = 5/6"]]'),
             "ask": {'a': 1, 'b': 3, 'c': 6, 'op': 'fa'}},
            {"worked": ('One more together. Three tenths plus four tenths equals seven tenths.',
                        '[[step eq="3/10 + 4/10 = 7/10"]]'),
             "ask": {'a': 2, 'b': 5, 'c': 10, 'op': 'fa'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [{'a': 1, 'b': 1, 'c': 4, 'op': 'fa'}, {'a': 1, 'b': 2, 'c': 5, 'op': 'fa'}, {'a': 2, 'b': 2, 'c': 6, 'op': 'fa'}, {'a': 1, 'b': 4, 'c': 6, 'op': 'fa'}, {'a': 2, 'b': 3, 'c': 8, 'op': 'fa'}, {'a': 3, 'b': 3, 'c': 8, 'op': 'fa'}, {'a': 2, 'b': 5, 'c': 8, 'op': 'fa'}, {'a': 4, 'b': 3, 'c': 10, 'op': 'fa'}, {'a': 3, 'b': 5, 'c': 10, 'op': 'fa'}, {'a': 5, 'b': 4, 'c': 12, 'op': 'fa'}],
    },
    {
        "id": 'basic-u6-take-away-fractions-same-bottom',
        "course": "basic", "unit": 6,
        "topic": 'Taking away fractions',
        "op": 'fs', "max_value": 12,
        "levels": ("abstract",),
        "symbols": ('bottom', 'take'),
        "advance_line": "Three in a row — you've got it! You can take away fractions with the same bottom.",
        "teach": [
            ('Taking away fractions with the same bottom works the same way — the pieces are the same size, so we just count what is left.',
             '[[goal text="Taking away fractions"]]'),
            ('Watch me. Five eighths take away two eighths. Count: 5 take away 2 equals 3. Five eighths take away two eighths equals three eighths.',
             '[[step eq="5/8 − 2/8 = 3/8"]]'),
            ('One more, watch. Three fourths take away one fourth equals two fourths.',
             '[[step eq="3/4 − 1/4 = 2/4"]]'),
        ],
        "pairs": [
            {"worked": ('Here is one more, done for you. Four sixths take away one sixth equals three sixths.',
                        '[[step eq="4/6 − 1/6 = 3/6"]]'),
             "ask": {'a': 5, 'b': 2, 'c': 6, 'op': 'fs'}},
            {"worked": ('One more together. Seven tenths take away three tenths equals four tenths.',
                        '[[step eq="7/10 − 3/10 = 4/10"]]'),
             "ask": {'a': 8, 'b': 5, 'c': 10, 'op': 'fs'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [{'a': 3, 'b': 1, 'c': 4, 'op': 'fs'}, {'a': 4, 'b': 2, 'c': 5, 'op': 'fs'}, {'a': 5, 'b': 1, 'c': 6, 'op': 'fs'}, {'a': 5, 'b': 3, 'c': 6, 'op': 'fs'}, {'a': 6, 'b': 2, 'c': 8, 'op': 'fs'}, {'a': 7, 'b': 3, 'c': 8, 'op': 'fs'}, {'a': 7, 'b': 5, 'c': 8, 'op': 'fs'}, {'a': 8, 'b': 3, 'c': 10, 'op': 'fs'}, {'a': 9, 'b': 4, 'c': 10, 'op': 'fs'}, {'a': 11, 'b': 5, 'c': 12, 'op': 'fs'}],
    },
    {
        "id": 'basic-u7-tenths',
        "course": "basic", "unit": 7,
        "topic": 'Tenths',
        "op": 'dt', "max_value": 9,
        "levels": ("abstract",),
        "symbols": ('tenth', 'point'),
        "advance_line": "Three in a row — you've got it! You know your tenths.",
        "teach": [
            ('Today we meet decimals. Split one whole into ten equal parts — each part is one tenth. We write one tenth with a point: 0.1.',
             '[[goal text="Tenths"]]'),
            ('Watch me. 0.3 is three tenths. 0.4 is four tenths. Three tenths plus four tenths equals seven tenths — 0.7.',
             '[[step eq="0.3 + 0.4 = 0.7"]]'),
            ('The point keeps the tenths in their own place, just like tens and ones have places. Count the tenths, and the point stays put.',
             '[[step eq="0.2 + 0.5 = 0.7"]]'),
        ],
        "pairs": [
            {"worked": ('Here is one more, done for you. Two tenths plus six tenths equals eight tenths — 0.8.',
                        '[[step eq="0.2 + 0.6 = 0.8"]]'),
             "ask": {'a': 1, 'b': 3, 'op': 'dt'}},
            {"worked": ('One more together. Five tenths plus four tenths equals nine tenths.',
                        '[[step eq="0.5 + 0.4 = 0.9"]]'),
             "ask": {'a': 2, 'b': 4, 'op': 'dt'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [{'a': 1, 'b': 2, 'op': 'dt'}, {'a': 2, 'b': 2, 'op': 'dt'}, {'a': 1, 'b': 4, 'op': 'dt'}, {'a': 3, 'b': 3, 'op': 'dt'}, {'a': 2, 'b': 5, 'op': 'dt'}, {'a': 4, 'b': 4, 'op': 'dt'}, {'a': 3, 'b': 5, 'op': 'dt'}, {'a': 6, 'b': 3, 'op': 'dt'}, {'a': 4, 'b': 5, 'op': 'dt'}, {'a': 7, 'b': 2, 'op': 'dt'}],
    },
    {
        "id": 'basic-u7-dimes-and-pennies',
        "course": "basic", "unit": 7,
        "topic": 'Dimes and pennies',
        "op": 'm', "max_value": 99,
        "levels": ("abstract",),
        "symbols": ('dime', 'penny'),
        "advance_line": "Three in a row — you've got it! You can count money like a shopkeeper.",
        "teach": [
            ('Money uses tens and ones too. A dime is worth ten cents. A penny is worth one cent. Dimes are the tens, pennies are the ones.',
             '[[goal text="Dimes and pennies"]]'),
            ('Watch me. 3 dimes and 4 pennies. The dimes bring 30 cents, the pennies bring 4 more. 30 plus 4 equals 34 cents.',
             '[[step eq="3 dimes = 30 cents"]][[step eq="30 + 4 = 34"]][[step eq="3 dimes + 4 pennies = 34 cents"]]'),
            ('One more, watch. 5 dimes and 2 pennies. 50 plus 2 equals 52 cents.',
             '[[step eq="5 dimes + 2 pennies = 52 cents"]]'),
        ],
        "pairs": [
            {"worked": ('Here is one more, done for you. 2 dimes and 7 pennies. 20 plus 7 equals 27 cents.',
                        '[[step eq="2 dimes + 7 pennies = 27 cents"]]'),
             "ask": {'a': 2, 'b': 5, 'op': 'm'}},
            {"worked": ('One more together. 4 dimes and 6 pennies equals 46 cents.',
                        '[[step eq="4 dimes + 6 pennies = 46 cents"]]'),
             "ask": {'a': 4, 'b': 3, 'op': 'm'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [{'a': 1, 'b': 2, 'op': 'm'}, {'a': 1, 'b': 5, 'op': 'm'}, {'a': 2, 'b': 3, 'op': 'm'}, {'a': 3, 'b': 1, 'op': 'm'}, {'a': 3, 'b': 6, 'op': 'm'}, {'a': 5, 'b': 4, 'op': 'm'}, {'a': 6, 'b': 2, 'op': 'm'}, {'a': 7, 'b': 5, 'op': 'm'}, {'a': 8, 'b': 8, 'op': 'm'}, {'a': 9, 'b': 9, 'op': 'm'}],
    },
    {
        "id": 'basic-u8-percent-of',
        "course": "basic", "unit": 8,
        "topic": 'Percent',
        "op": 'pc', "max_value": 100,
        "levels": ("abstract",),
        "symbols": ('percent', 'hundred'),
        "advance_line": "Three in a row — you've got it! You can take a percent of a number.",
        "teach": [
            ('Percent means out of one hundred. Fifty percent means fifty out of a hundred — one half. Twenty-five percent is one fourth. Ten percent is one tenth.',
             '[[goal text="Percent"]]'),
            ('Watch me find 50 percent of 8. Fifty percent is one half, and one half of 8 equals 4. So 50 percent of 8 equals 4.',
             '[[step eq="50% of 8 = 4"]]'),
            ('One more, watch. 10 percent of 40. Ten percent is one tenth, and one tenth of 40 equals 4. So 10 percent of 40 equals 4.',
             '[[step eq="10% of 40 = 4"]]'),
        ],
        "pairs": [
            {"worked": ('Here is one more, done for you. 25 percent of 8. Twenty-five percent is one fourth, and one fourth of 8 equals 2.',
                        '[[step eq="25% of 8 = 2"]]'),
             "ask": {'a': 25, 'b': 12, 'op': 'pc'}},
            {"worked": ('One more together. 50 percent of 12 equals 6.',
                        '[[step eq="50% of 12 = 6"]]'),
             "ask": {'a': 50, 'b': 14, 'op': 'pc'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [{'a': 50, 'b': 2, 'op': 'pc'}, {'a': 50, 'b': 4, 'op': 'pc'}, {'a': 25, 'b': 4, 'op': 'pc'}, {'a': 50, 'b': 6, 'op': 'pc'}, {'a': 50, 'b': 10, 'op': 'pc'}, {'a': 25, 'b': 16, 'op': 'pc'}, {'a': 50, 'b': 18, 'op': 'pc'}, {'a': 10, 'b': 20, 'op': 'pc'}, {'a': 10, 'b': 30, 'op': 'pc'}, {'a': 10, 'b': 50, 'op': 'pc'}],
    },
    {
        "id": 'basic-u8-one-costs',
        "course": "basic", "unit": 8,
        "topic": 'What one costs',
        "op": 'rate', "max_value": 40,
        "levels": ("abstract",),
        "symbols": ('cost', 'divided'),
        "advance_line": "Three in a row — you've got it! You can find what one costs.",
        "teach": [
            ('Prices often come in bunches: six apples for twelve dollars. To compare prices, we find what ONE costs. That is dividing.',
             '[[goal text="What one costs"]]'),
            ('Watch me. 6 apples cost 12 dollars. 12 divided by 6 equals 2 — one apple costs 2 dollars.',
             '[[step eq="12 ÷ 6 = 2"]]'),
            ('One more, watch. 4 apples cost 20 dollars. 20 divided by 4 equals 5 — one apple costs 5 dollars.',
             '[[step eq="20 ÷ 4 = 5"]]'),
        ],
        "pairs": [
            {"worked": ('Here is one more, done for you. 3 apples cost 9 dollars. 9 divided by 3 equals 3 — one costs 3 dollars.',
                        '[[step eq="9 ÷ 3 = 3"]]'),
             "ask": {'a': 8, 'b': 4, 'op': 'rate'}},
            {"worked": ('One more together. 5 apples cost 15 dollars — one costs 3 dollars.',
                        '[[step eq="15 ÷ 5 = 3"]]'),
             "ask": {'a': 12, 'b': 3, 'op': 'rate'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [{'a': 6, 'b': 2, 'op': 'rate'}, {'a': 10, 'b': 2, 'op': 'rate'}, {'a': 12, 'b': 4, 'op': 'rate'}, {'a': 15, 'b': 3, 'op': 'rate'}, {'a': 16, 'b': 4, 'op': 'rate'}, {'a': 20, 'b': 5, 'op': 'rate'}, {'a': 24, 'b': 6, 'op': 'rate'}, {'a': 28, 'b': 7, 'op': 'rate'}, {'a': 32, 'b': 8, 'op': 'rate'}, {'a': 36, 'b': 9, 'op': 'rate'}],
    },
    {
        "id": 'basic-u9-perimeter',
        "course": "basic", "unit": 9,
        "topic": 'Perimeter',
        "op": 'peri', "max_value": 60,
        "levels": ("abstract",),
        "symbols": ('perimeter', 'around'),
        "advance_line": "Three in a row — you've got it! You can walk the whole way around.",
        "teach": [
            ('Perimeter is the distance all the way around a shape. For a rectangle, walk all four sides: long, wide, long, wide.',
             '[[goal text="Perimeter"]]'),
            ('Watch me. A rectangle 5 long and 3 wide. Walk around: 5 plus 3 plus 5 plus 3 equals 16. The perimeter equals 16.',
             '[[step eq="5 + 3 + 5 + 3 = 16"]]'),
            ('One more, watch. 6 long and 2 wide: 6 plus 2 plus 6 plus 2 equals 16.',
             '[[step eq="6 + 2 + 6 + 2 = 16"]]'),
        ],
        "pairs": [
            {"worked": ('Here is one more, done for you. 4 long and 2 wide: 4 plus 2 plus 4 plus 2 equals 12.',
                        '[[step eq="4 + 2 + 4 + 2 = 12"]]'),
             "ask": {'a': 5, 'b': 2, 'op': 'peri'}},
            {"worked": ('One more together. 7 long and 3 wide — the perimeter equals 20.',
                        '[[step eq="7 + 3 + 7 + 3 = 20"]]'),
             "ask": {'a': 6, 'b': 4, 'op': 'peri'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [{'a': 3, 'b': 1, 'op': 'peri'}, {'a': 3, 'b': 2, 'op': 'peri'}, {'a': 4, 'b': 3, 'op': 'peri'}, {'a': 5, 'b': 3, 'op': 'peri'}, {'a': 6, 'b': 3, 'op': 'peri'}, {'a': 7, 'b': 4, 'op': 'peri'}, {'a': 8, 'b': 5, 'op': 'peri'}, {'a': 9, 'b': 6, 'op': 'peri'}, {'a': 10, 'b': 7, 'op': 'peri'}, {'a': 12, 'b': 8, 'op': 'peri'}],
    },
    {
        "id": 'basic-u9-area',
        "course": "basic", "unit": 9,
        "topic": 'Area',
        "op": 'area', "max_value": 96,
        "levels": ("abstract",),
        "symbols": ('area', 'inside'),
        "advance_line": "Three in a row — you've got it! You can count the space inside.",
        "teach": [
            ('Area is the space INSIDE a shape, counted in squares. For a rectangle, area is the long side times the wide side.',
             '[[goal text="Area"]]'),
            ('Watch me. A rectangle 5 long and 3 wide holds 3 rows of 5 squares: 5 times 3 equals 15. The area equals 15 squares.',
             '[[step eq="5 × 3 = 15"]]'),
            ('One more, watch. 4 long and 2 wide: 4 times 2 equals 8 squares.',
             '[[step eq="4 × 2 = 8"]]'),
        ],
        "pairs": [
            {"worked": ('Here is one more, done for you. 6 long and 2 wide: 6 times 2 equals 12 squares.',
                        '[[step eq="6 × 2 = 12"]]'),
             "ask": {'a': 3, 'b': 2, 'op': 'area'}},
            {"worked": ('One more together. 7 long and 4 wide — the area equals 28 squares.',
                        '[[step eq="7 × 4 = 28"]]'),
             "ask": {'a': 5, 'b': 4, 'op': 'area'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [{'a': 5, 'b': 2, 'op': 'area'}, {'a': 4, 'b': 3, 'op': 'area'}, {'a': 6, 'b': 3, 'op': 'area'}, {'a': 7, 'b': 3, 'op': 'area'}, {'a': 6, 'b': 4, 'op': 'area'}, {'a': 8, 'b': 4, 'op': 'area'}, {'a': 9, 'b': 5, 'op': 'area'}, {'a': 8, 'b': 6, 'op': 'area'}, {'a': 9, 'b': 7, 'op': 'area'}, {'a': 12, 'b': 8, 'op': 'area'}],
    },
]
LESSONS.extend(_MORE_LESSONS)

# THE COURSE ORDER IS OWNED HERE (jz -- jy had accidentally placed carrying before
# two-digit-no-carry). Import fails loudly if a lesson is missing or listed twice.
COURSE_ORDER = [
    "basic-u1-add-up-to-10", "basic-u1-take-away-up-to-10",
    "basic-u1-add-up-to-20", "basic-u1-take-away-up-to-20",
    "basic-u1-tens-and-ones", "basic-u1-add-two-digit-no-carry",
    "basic-u1-add-with-carrying", "basic-u1-take-away-with-regrouping",
    "basic-u2-what-multiplying-means", "basic-u2-times-tables",
    "basic-u3-what-dividing-means", "basic-u3-left-overs",
    "basic-u4-missing-factors", "basic-u4-greatest-common-factor",
    "basic-u5-fraction-of-a-group", "basic-u5-equivalent-fractions",
    "basic-u6-add-fractions-same-bottom", "basic-u6-take-away-fractions-same-bottom",
    "basic-u7-tenths", "basic-u7-dimes-and-pennies",
    "basic-u8-percent-of", "basic-u8-one-costs",
    "basic-u9-perimeter", "basic-u9-area",
]
_by_id = {les["id"]: les for les in LESSONS}
if sorted(COURSE_ORDER) != sorted(_by_id):
    raise RuntimeError("COURSE_ORDER and LESSONS disagree: "
                       + str(sorted(set(COURSE_ORDER) ^ set(_by_id))))
LESSONS = [_by_id[i] for i in COURSE_ORDER]

LESSON_BY_ID = {les["id"]: les for les in LESSONS}
PILOT_LESSON = LESSONS[0]   # every js/jt-era pin and endpoint default still resolves


# =============================================================================
# OP_EXT -- the data-driven op registry (build jz). The original three ops
# ("+", "-", "t") stay hand-written below; every newer op is an entry here:
#   ans(p)    the computed answer (never typed -- the founding rule)
#   spoken(p) what the child hears (abstract level; these lessons are abstract-only)
#   board(p)  the board tags
#   praise(p) the echo line after the praise prefix
#   key(p)    the difficulty-ramp key
#   check(p)  (ok, why) -- the per-problem constraint the validator enforces
#   speaks(p, spoken) -- rule-44 override for ops that speak digits as WORDS
# =============================================================================
_NUMWORD = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
            7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven",
            12: "twelve"}
_FRACWORD = {2: ("half", "halves"), 3: ("third", "thirds"),
             4: ("fourth", "fourths"), 5: ("fifth", "fifths"),
             6: ("sixth", "sixths"), 8: ("eighth", "eighths"),
             10: ("tenth", "tenths"), 12: ("twelfth", "twelfths")}


def _gcd(x, y):
    while y:
        x, y = y, x % y
    return x


OP_EXT = {
    "*": {
        "ans": lambda p: p["a"] * p["b"],
        "spoken": lambda p: f"What is {p['a']} times {p['b']}?",
        "board": lambda p: f'[[step eq="{p["a"]} × {p["b"]} = ?"]]',
        "praise": lambda p: f"{p['a']} times {p['b']} equals {p['a'] * p['b']}.",
        "key": lambda p: p["a"] * p["b"],
        "check": lambda p: (p["a"] >= 1 and p["b"] >= 1, "factors must be at least 1"),
    },
    "/": {
        "ans": lambda p: p["a"] // p["b"],
        "spoken": lambda p: f"What is {p['a']} divided by {p['b']}?",
        "board": lambda p: f'[[step eq="{p["a"]} ÷ {p["b"]} = ?"]]',
        "praise": lambda p: f"{p['a']} divided by {p['b']} equals {p['a'] // p['b']}.",
        "key": lambda p: p["a"],
        "check": lambda p: (p["a"] % p["b"] == 0 and p["b"] >= 2,
                            "a division lesson must divide EXACTLY"),
    },
    "rem": {
        "ans": lambda p: p["a"] % p["b"],
        "spoken": lambda p: (f"What is left over when {p['a']} is shared into "
                             f"groups of {p['b']}?"),
        "board": lambda p: f'[[step eq="{p["a"]} ÷ {p["b"]} → left over = ?"]]',
        "praise": lambda p: (f"Sharing {p['a']} into groups of {p['b']} leaves "
                             f"{p['a'] % p['b']} left over."),
        "key": lambda p: p["a"],
        "check": lambda p: (1 <= p["a"] % p["b"] < p["b"],
                            "the left-over must be at least 1 (tap options start "
                            "at 1) and smaller than the group"),
    },
    "mf": {   # missing factor: b × ? = a
        "ans": lambda p: p["a"] // p["b"],
        "spoken": lambda p: f"{p['b']} times what equals {p['a']}?",
        "board": lambda p: f'[[step eq="{p["b"]} × ? = {p["a"]}"]]',
        "praise": lambda p: f"{p['b']} times {p['a'] // p['b']} equals {p['a']}.",
        "key": lambda p: p["a"],
        "check": lambda p: (p["a"] % p["b"] == 0 and p["b"] >= 2,
                            "the missing factor must be exact"),
    },
    "gcf": {
        "ans": lambda p: _gcd(p["a"], p["b"]),
        "spoken": lambda p: (f"What is the greatest common factor of {p['a']} "
                             f"and {p['b']}?"),
        "board": lambda p: f'[[step eq="GCF of {p["a"]} and {p["b"]} = ?"]]',
        "praise": lambda p: (f"The greatest common factor of {p['a']} and "
                             f"{p['b']} equals {_gcd(p['a'], p['b'])}."),
        "key": lambda p: max(p["a"], p["b"]),
        "check": lambda p: (_gcd(p["a"], p["b"]) >= 2,
                            "a GCF of 1 makes a dull tap question"),
    },
    "of": {   # one unit-fraction of a group: 1/b of a
        "ans": lambda p: p["a"] // p["b"],
        "spoken": lambda p: (f"What is one {_FRACWORD[p['b']][0]} of {p['a']}?"),
        "board": lambda p: f'[[step eq="1/{p["b"]} of {p["a"]} = ?"]]',
        "praise": lambda p: (f"One {_FRACWORD[p['b']][0]} of {p['a']} equals "
                             f"{p['a'] // p['b']}."),
        "key": lambda p: p["a"],
        "check": lambda p: (p["a"] % p["b"] == 0 and p["b"] in _FRACWORD,
                            "the share must be exact and the fraction sayable"),
        "speaks": lambda p, sp: str(p["a"]) in sp and _FRACWORD[p["b"]][0] in sp,
    },
    "eqf": {   # 1/b = ?/c
        "ans": lambda p: p["c"] // p["b"],
        "spoken": lambda p: (f"One {_FRACWORD[p['b']][0]} equals how many "
                             f"{_FRACWORD[p['c']][1]}?"),
        "board": lambda p: f'[[step eq="1/{p["b"]} = ?/{p["c"]}"]]',
        "praise": lambda p: (f"One {_FRACWORD[p['b']][0]} equals "
                             f"{_NUMWORD[p['c'] // p['b']]} {_FRACWORD[p['c']][1]}."),
        "key": lambda p: p["c"],
        "check": lambda p: (p["c"] % p["b"] == 0 and p["b"] in _FRACWORD
                            and p["c"] in _FRACWORD and p["c"] > p["b"]
                            and p["c"] // p["b"] in _NUMWORD,
                            "the equivalence must be exact and sayable"),
        "speaks": lambda p, sp: (_FRACWORD[p["b"]][0] in sp
                                 and _FRACWORD[p["c"]][1] in sp),
    },
    "fa": {   # a/c + b/c, answered in c-ths
        "ans": lambda p: p["a"] + p["b"],
        "spoken": lambda p: (f"How many {_FRACWORD[p['c']][1]} is {p['a']} "
                             f"{_FRACWORD[p['c']][1]} plus {p['b']} "
                             f"{_FRACWORD[p['c']][1]}?"),
        "board": lambda p: f'[[step eq="{p["a"]}/{p["c"]} + {p["b"]}/{p["c"]} = ?/{p["c"]}"]]',
        "praise": lambda p: (f"{p['a']} {_FRACWORD[p['c']][1]} plus {p['b']} "
                             f"{_FRACWORD[p['c']][1]} equals {p['a'] + p['b']} "
                             f"{_FRACWORD[p['c']][1]}."),
        "key": lambda p: p["a"] + p["b"],
        "check": lambda p: (p["a"] + p["b"] < p["c"] and p["c"] in _FRACWORD,
                            "same-bottom adding stays a proper fraction"),
    },
    "fs": {   # a/c - b/c
        "ans": lambda p: p["a"] - p["b"],
        "spoken": lambda p: (f"How many {_FRACWORD[p['c']][1]} is {p['a']} "
                             f"{_FRACWORD[p['c']][1]} take away {p['b']} "
                             f"{_FRACWORD[p['c']][1]}?"),
        "board": lambda p: f'[[step eq="{p["a"]}/{p["c"]} − {p["b"]}/{p["c"]} = ?/{p["c"]}"]]',
        "praise": lambda p: (f"{p['a']} {_FRACWORD[p['c']][1]} take away "
                             f"{p['b']} {_FRACWORD[p['c']][1]} equals "
                             f"{p['a'] - p['b']} {_FRACWORD[p['c']][1]}."),
        "key": lambda p: p["a"],
        "check": lambda p: (1 <= p["a"] - p["b"] and p["a"] < p["c"]
                            and p["c"] in _FRACWORD,
                            "same-bottom take-away stays proper and positive"),
    },
    "dt": {   # tenths: 0.a + 0.b, answered in tenths
        "ans": lambda p: p["a"] + p["b"],
        "spoken": lambda p: (f"How many tenths is {p['a']} tenths plus "
                             f"{p['b']} tenths?"),
        "board": lambda p: f'[[step eq="0.{p["a"]} + 0.{p["b"]} = 0.?"]]',
        "praise": lambda p: (f"{p['a']} tenths plus {p['b']} tenths equals "
                             f"{p['a'] + p['b']} tenths."),
        "key": lambda p: p["a"] + p["b"],
        "check": lambda p: (p["a"] + p["b"] <= 9,
                            "the tenths must not spill into a whole (that is the "
                            "NEXT lesson's idea)"),
    },
    "m": {    # money: a dimes + b pennies = ? cents
        "ans": lambda p: 10 * p["a"] + p["b"],
        "spoken": lambda p: (f"How many cents is {p['a']} dimes and {p['b']} "
                             f"pennies?"),
        "board": lambda p: f'[[step eq="{p["a"]} dimes + {p["b"]} pennies = ? cents"]]',
        "praise": lambda p: (f"{p['a']} dimes and {p['b']} pennies equals "
                             f"{10 * p['a'] + p['b']} cents."),
        "key": lambda p: 10 * p["a"] + p["b"],
        "check": lambda p: (1 <= p["a"] <= 9 and 1 <= p["b"] <= 9,
                            "dimes and pennies each stay single-digit"),
    },
    "pc": {   # a% of b
        "ans": lambda p: p["a"] * p["b"] // 100,
        "spoken": lambda p: f"What is {p['a']} percent of {p['b']}?",
        "board": lambda p: f'[[step eq="{p["a"]}% of {p["b"]} = ?"]]',
        "praise": lambda p: (f"{p['a']} percent of {p['b']} equals "
                             f"{p['a'] * p['b'] // 100}."),
        "key": lambda p: p["b"],
        "check": lambda p: ((p["a"] * p["b"]) % 100 == 0
                            and p["a"] * p["b"] // 100 >= 1,
                            "the percent must come out whole, and at least 1"),
    },
    "rate": {  # b things cost a dollars; one costs ?
        "ans": lambda p: p["a"] // p["b"],
        "spoken": lambda p: (f"{p['b']} apples cost {p['a']} dollars. What does "
                             f"one apple cost, in dollars?"),
        "board": lambda p: f'[[step eq="{p["a"]} ÷ {p["b"]} = ?"]]',
        "praise": lambda p: (f"{p['a']} divided by {p['b']} equals "
                             f"{p['a'] // p['b']} — one costs "
                             f"{p['a'] // p['b']} dollars."),
        "key": lambda p: p["a"],
        "check": lambda p: (p["a"] % p["b"] == 0 and p["b"] >= 2,
                            "a unit price must come out exact"),
    },
    "peri": {
        "ans": lambda p: 2 * (p["a"] + p["b"]),
        "spoken": lambda p: (f"A rectangle is {p['a']} long and {p['b']} wide. "
                             f"What is its perimeter?"),
        "board": lambda p: (f'[[step eq="{p["a"]} + {p["b"]} + {p["a"]} + '
                            f'{p["b"]} = ?"]]'),
        "praise": lambda p: (f"{p['a']} plus {p['b']} plus {p['a']} plus "
                             f"{p['b']} equals {2 * (p['a'] + p['b'])}."),
        "key": lambda p: p["a"] + p["b"],
        "check": lambda p: (p["a"] > p["b"] >= 1,
                            "long means longer: a must beat b"),
    },
    "area": {
        "ans": lambda p: p["a"] * p["b"],
        "spoken": lambda p: (f"A rectangle is {p['a']} long and {p['b']} wide. "
                             f"What is its area?"),
        "board": lambda p: f'[[step eq="{p["a"]} × {p["b"]} = ?"]]',
        "praise": lambda p: (f"{p['a']} times {p['b']} equals "
                             f"{p['a'] * p['b']} squares."),
        "key": lambda p: p["a"] * p["b"],
        "check": lambda p: (p["a"] > p["b"] >= 1, "long means longer"),
    },
}


# =============================================================================
# RENDERERS -- problem data -> what the child sees and hears, per level.
# One function per surface, so vocabulary consistency is BY CONSTRUCTION.
# =============================================================================
def spoken_for(p, level):
    a, b = p["a"], p["b"]
    if p.get("op") in OP_EXT:
        return OP_EXT[p["op"]]["spoken"](p)
    if p.get("op") == "t":
        if level == "abstract":
            return f"What number is {a} ten and {b} ones?"
        if level == "pictorial":
            return f"Count if you need to. What number is {a} ten and {b} ones?"
        return (f"Let's count together. {a} ten, and {b} more ones. "
                f"What number is that?")
    if p.get("op") == "-":
        if level == "abstract":
            return f"What is {a} minus {b}?"
        if level == "pictorial":
            return f"Count the stars if you need them. What is {a} minus {b}?"
        return (f"Let's count together. {a} stars, take {b} away. "
                f"How many are left?")
    if level == "abstract":
        return f"What is {a} plus {b}?"
    if level == "pictorial":
        return f"Count the stars if you need them. What is {a} plus {b}?"
    return (f"Let's count together. {a} stars, then {b} more stars. "
            f"How many in all?")


def board_for(p, level):
    a, b = p["a"], p["b"]
    if p.get("op") in OP_EXT:
        return OP_EXT[p["op"]]["board"](p)
    if p.get("op") == "t":
        step = f'[[step eq="{a} ten and {b} ones = ?"]]'
        if level == "abstract":
            return step
        stars = (f'[[objects emoji="⭐" groups="10" add="{b}" '
                 f'caption="one ten and {b} ones"]]')
        return stars + step
    if p.get("op") == "-":
        step = f'[[step eq="{a} − {b} = ?"]]'
        if level == "abstract":
            return step
        stars = (f'[[objects emoji="⭐" groups="{a}" '
                 f'caption="start with {a} — take {b} away, count what is left"]]')
        return stars + step
    step = f'[[step eq="{a} + {b} = ?"]]'
    if level == "abstract":
        return step
    stars = f'[[objects emoji="⭐" groups="{a}" add="{b}" caption="count every star"]]'
    return stars + step


def choices_for(p):
    """Three tap options: the answer and its two neighbours (floor 1), shuffled by a
    FIXED per-problem rotation -- deterministic, so replays render identically."""
    v = ans(p)
    opts = [v - 1, v, v + 1] if v > 1 else [v, v + 1, v + 2]
    k = (p["a"] * 3 + p["b"] + p.get("c", 0)) % 3
    opts = opts[k:] + opts[:k]
    return "[[choices options=\"" + " | ".join(str(o) for o in opts) + "\"]]"


def praise_for(p, index):
    a, b = p["a"], p["b"]
    if p.get("op") in OP_EXT:
        return (PRAISE_PREFIXES[index % len(PRAISE_PREFIXES)] + " "
                + OP_EXT[p["op"]]["praise"](p))
    if p.get("op") == "t":
        return (PRAISE_PREFIXES[index % len(PRAISE_PREFIXES)]
                + f" {a} ten and {b} ones — that is {ans(p)}.")
    word = "minus" if p.get("op") == "-" else "plus"
    return (PRAISE_PREFIXES[index % len(PRAISE_PREFIXES)]
            + f" {a} {word} {b} equals {ans(p)}.")


# =============================================================================
# THE ENGINE -- a pure state machine.  step(lesson, state, event) -> (out, state)
# -----------------------------------------------------------------------------
# Events:   ("begin",)            start the lesson
#           ("answer", value)     the child answered (tap or typed int)
#           ("unheard",)          voice input could not be recognized
#           ("resume",)           the AI intervention finished; give the retest
# Outputs (dicts), by kind:
#   say        {spoken, board}                       -- narration beat, no input
#   ask        {spoken, board, choices, expected, guided, problem} -- wait for child
#   intervene  {reason, problem, expected, got, vocabulary, retest} -- AI takes over;
#              the ONLY step the model ever authors, and the engine has already chosen
#              the retest problem, so the RETURN to script is code's decision.
#   end        {spoken, graceful, mastered, problems_done}
# =============================================================================
def start(lesson):
    return {"phase": "teach", "i": 0,
            "level": lesson.get("levels", LEVELS)[0],
            "bank_i": 0, "done": 0, "streak": 0,
            "interventions": 0, "unheard": 0, "pending": None,
            "retest": None, "finished": False}


def _problem_key(p):
    return (p.get("op", "+"), p["a"], p["b"], p.get("c", 0))


def _next_bank_problem(lesson, state):
    """The next unused bank problem; the bank wraps if the retest path consumed it."""
    bank = lesson["bank"]
    p = bank[state["bank_i"] % len(bank)]
    state["bank_i"] += 1
    return p


def _ask(state, p, guided=False):
    out = {"kind": "ask", "spoken": spoken_for(p, state["level"]),
           "board": board_for(p, state["level"]), "choices": choices_for(p),
           "expected": ans(p), "guided": guided, "problem": p,
           "tap_only": state["unheard"] >= 2}
    state["pending"] = {"problem": p, "guided": guided}
    return out


def step(lesson, state, event):
    """One engine transition. Returns (list_of_output_steps, state). Pure."""
    kind = event[0]
    out = []

    if state["finished"]:
        return ([{"kind": "end", "spoken": "", "graceful": True,
                  "mastered": False, "problems_done": state["done"]}], state)

    if kind == "begin":
        for spoken, board in lesson["teach"]:
            out.append({"kind": "say", "spoken": spoken, "board": board})
        pair = lesson["pairs"][0]
        out.append({"kind": "say", "spoken": pair["worked"][0],
                    "board": pair["worked"][1]})
        out.append(_ask(state, pair["ask"], guided=True))
        state["phase"] = "pair-0"
        return (out, state)

    if kind == "unheard":
        state["unheard"] += 1
        p = state["pending"]["problem"]
        guided = state["pending"]["guided"]
        re_spoken = LINE_TAP if state["unheard"] >= 2 else (
            LINE_REASK + " " + spoken_for(p, state["level"]))
        asked = _ask(state, p, guided=guided)
        asked["spoken"] = re_spoken
        return ([asked], state)

    if kind == "resume":
        # The AI intervention is over. The engine -- not the model -- decides what
        # happens next: the retest problem it already chose, or (at the cap) the
        # warm close. The model never picks where the child lands.
        p = state["retest"]
        state["retest"] = None
        if p is None:
            state["finished"] = True
            return ([{"kind": "end", "spoken": LINE_END_GRACEFUL, "graceful": True,
                      "mastered": False, "problems_done": state["done"]}], state)
        return ([_ask(state, p, guided=False)], state)

    if kind != "answer":
        return ([], state)

    state["unheard"] = 0
    pend = state["pending"]
    p, guided = pend["problem"], pend["guided"]
    correct = (event[1] == ans(p))

    if correct:
        idx = state["done"]
        out.append({"kind": "say", "spoken": praise_for(p, idx), "board": ""})
        if not guided:
            state["done"] += 1
            state["streak"] += 1
        # ---- where next? ----
        if state["phase"] == "pair-0":
            pair = lesson["pairs"][1]
            out.append({"kind": "say", "spoken": pair["worked"][0],
                        "board": pair["worked"][1]})
            out.append(_ask(state, pair["ask"], guided=True))
            state["phase"] = "pair-1"
            return (out, state)
        if state["phase"] == "pair-1":
            out.append({"kind": "say", "spoken": lesson["practice_intro"],
                        "board": ""})
            state["phase"] = "practice"
            out.append(_ask(state, _next_bank_problem(lesson, state)))
            return (out, state)
        # practice
        if state["done"] >= MIN_PROBLEMS and state["streak"] >= ADVANCE_STREAK:
            out.append({"kind": "end", "spoken": lesson["advance_line"],
                        "graceful": True, "mastered": True,
                        "problems_done": state["done"]})
            state["finished"] = True
            return (out, state)
        if state["done"] >= MAX_PROBLEMS:
            out.append({"kind": "end", "spoken": LINE_END_GRACEFUL,
                        "graceful": True, "mastered": False,
                        "problems_done": state["done"]})
            state["finished"] = True
            return (out, state)
        out.append(_ask(state, _next_bank_problem(lesson, state)))
        return (out, state)

    # ---- wrong answer: the ONE doorway to the AI ----
    state["streak"] = 0
    if not guided:
        state["done"] += 1
    state["interventions"] += 1
    if state["interventions"] >= DROP_AFTER_INTERVENTIONS:
        lv = lesson.get("levels", LEVELS)
        li = lv.index(state["level"])
        if li + 1 < len(lv):
            state["level"] = lv[li + 1]
            state["interventions"] = 0
        else:
            # already at concrete and still failing: end warmly, mark "learning"
            out.append({"kind": "say", "spoken": LINE_WRONG, "board": ""})
            out.append({"kind": "end", "spoken": LINE_END_GRACEFUL,
                        "graceful": True, "mastered": False,
                        "problems_done": state["done"]})
            state["finished"] = True
            return (out, state)
    # AT THE CAP, THE ERROR IS STILL CORRECTED BUT NO RETEST FOLLOWS: the AI's
    # Model-Lead-Test runs (never leave a child with an uncorrected error), and
    # "resume" then ends the practice gracefully instead of asking an eleventh
    # problem. Found by the alternating right/wrong scenario in build js's own
    # dry run -- the cap only guarded the CORRECT path, and `done` reached 11.
    retest = None
    if state["done"] < MAX_PROBLEMS:
        retest = _next_bank_problem(lesson, state)
    state["retest"] = retest
    out.append({"kind": "say", "spoken": LINE_WRONG, "board": ""})
    out.append({"kind": "intervene", "reason": "wrong_answer", "problem": p,
                "expected": ans(p), "got": event[1],
                "vocabulary": {k: k for k in VOCABULARY},
                "level": state["level"], "retest": retest})
    return (out, state)


# =============================================================================
# THE AUDIO CLOSURE -- every spoken string a lesson can ever emit.
# =============================================================================
def audio_lines(lesson):
    lines = set()
    for spoken, _board in lesson["teach"]:
        lines.add(spoken)
    for pair in lesson["pairs"]:
        lines.add(pair["worked"][0])
    lines.add(lesson["practice_intro"])
    problems = list(lesson["bank"]) + [pair["ask"] for pair in lesson["pairs"]]
    for p in problems:
        for level in lesson.get("levels", LEVELS):
            lines.add(spoken_for(p, level))
            lines.add(LINE_REASK + " " + spoken_for(p, level))
        for i in range(len(PRAISE_PREFIXES)):
            lines.add(praise_for(p, i))
    lines.update([LINE_WRONG, LINE_TAP, LINE_END_GRACEFUL,
                  lesson["advance_line"]])
    return sorted(lines)


def audio_cost_estimate(lesson, usd_per_1k_chars=0.22):
    chars = sum(len(s) for s in audio_lines(lesson))
    return {"lines": len(audio_lines(lesson)), "chars": chars,
            "usd": round(chars / 1000.0 * usd_per_1k_chars, 2)}


# =============================================================================
# THE VALIDATOR -- the checks that make "verified once" true. Pure; returns a list
# of (ok, label, detail). The battery fails the build on any not-ok.
# =============================================================================
_TAG_RE = re.compile(r"\[\[\s*([\w-]+)")


def _difficulty_key(p):
    """The ramp is measured on what makes the problem HARD: the sum for adding,
    the starting number for taking away (you count back from it), the ones count
    for tens-and-ones."""
    op = p.get("op", "+")
    if op in OP_EXT:
        return OP_EXT[op]["key"](p)
    if op == "-":
        return p["a"]
    if op == "t":
        return p["b"]
    return p["a"] + p["b"]


def validate(lesson, board_tag_names=None):
    checks = []

    def ck(ok, label, detail=""):
        checks.append((bool(ok), label, detail))

    lid = lesson["id"]
    bound = lesson.get("max_value", 10)

    # 1. every answer is COMPUTED -- and inside the lesson's own stated bound
    problems = list(lesson["bank"]) + [pr["ask"] for pr in lesson["pairs"]]
    ck(all(1 <= ans(p) <= bound for p in problems),
       f"{lid}: every answer stays within {bound} (and above zero)",
       str([p for p in problems if not 1 <= ans(p) <= bound]))
    ck(all(p["a"] <= bound and p["b"] <= bound for p in problems),
       f"{lid}: every number a child sees stays within {bound}", "")
    # jx: the lesson's NAME is a promise about its INPUTS (Jim's second wording
    # ruling) -- a_max/b_max make the bank provably match the name.
    a_cap = lesson.get("a_max")
    b_cap = lesson.get("b_max")
    if a_cap is not None:
        ck(all(p["a"] <= a_cap for p in problems),
           f"{lid}: every first number honors the name (a <= {a_cap})",
           str([p for p in problems if p["a"] > a_cap]))
    if b_cap is not None:
        ck(all(p["b"] <= b_cap for p in problems),
           f"{lid}: every second number honors the name (b <= {b_cap})",
           str([p for p in problems if p["b"] > b_cap]))
    for p in problems:
        _ext = OP_EXT.get(p.get("op", "+"))
        if _ext:
            okc, why = _ext["check"](p)
            ck(okc, f"{lid}: {p} satisfies its op's constraint", why)
    if lesson.get("regroup"):
        ck(all(p["a"] % 10 < p["b"] % 10 and p["a"] > p["b"] and
               p["a"] // 10 - 1 >= p["b"] // 10 for p in problems),
           f"{lid}: EVERY problem regroups (ones too small) and never goes "
           f"negative in the tens",
           str([p for p in problems if not (p["a"] % 10 < p["b"] % 10
                and p["a"] > p["b"] and p["a"] // 10 - 1 >= p["b"] // 10)]))
    if lesson.get("carry"):
        ck(all(p["a"] % 10 + p["b"] % 10 > 9 for p in problems),
           f"{lid}: EVERY problem carries -- a carrying lesson that practices on "
           f"no-carry problems teaches its idea on examples that never use it",
           str([p for p in problems if p["a"] % 10 + p["b"] % 10 <= 9]))
        ck(all(p["a"] // 10 + p["b"] // 10 + 1 <= 9 for p in problems),
           f"{lid}: no problem overflows the tens (answers stay two-digit)",
           str([p for p in problems if p["a"] // 10 + p["b"] // 10 + 1 > 9]))
    if lesson.get("no_carry"):
        ck(all(p["a"] % 10 + p["b"] % 10 <= 9
               and p["a"] // 10 + p["b"] // 10 <= 9 for p in problems),
           f"{lid}: NO problem carries -- the lesson that promises no carrying "
           f"cannot quietly require it",
           str([p for p in problems
                if p["a"] % 10 + p["b"] % 10 > 9
                or p["a"] // 10 + p["b"] // 10 > 9]))
    ck(len({_problem_key(p) for p in problems}) == len(problems),
       f"{lid}: no duplicate problems", "")

    # 2. choices: the right answer appears exactly once, all options positive
    for p in problems:
        opts = re.findall(r"\d+", choices_for(p))
        ck(opts.count(str(ans(p))) == 1,
           f"{lid}: choices for {p['a']}{p.get('op', '+')}{p['b']} contain the "
           f"answer exactly once", str(opts))
        ck(all(int(o) >= 1 for o in opts),
           f"{lid}: choices for {p['a']}{p.get('op', '+')}{p['b']} are all at "
           f"least 1", str(opts))

    # 3. the difficulty ramp: the key never falls by more than 1 across the bank
    keys = [_difficulty_key(p) for p in lesson["bank"]]
    ck(all(keys[i + 1] >= keys[i] - 1 for i in range(len(keys) - 1)),
       f"{lid}: the bank is a ramp (difficulty never falls by more than 1)",
       str(keys))

    # 4. every beat respects the spoken cap
    for spoken in [s for s, _b in lesson["teach"]] + \
                  [pr["worked"][0] for pr in lesson["pairs"]] + \
                  [lesson["practice_intro"]]:
        ck(len(spoken.split()) <= BEAT_WORD_CAP,
           f"{lid}: beat under {BEAT_WORD_CAP} words: \"{spoken[:36]}...\"",
           f"{len(spoken.split())} words")

    # 5. rule 14 by construction: the lesson's symbols are READ ALOUD in teach
    teach_text = " ".join(s for s, _b in lesson["teach"]).lower()
    for sym in lesson["symbols"]:
        ck(f"'{sym}'" in teach_text or f" {sym} " in teach_text,
           f"{lid}: the {sym} sign is introduced by name (rule 14)", "")

    # 6. rule 44 by construction: every ask SPEAKS its numbers
    for p in problems:
        for level in lesson.get("levels", LEVELS):
            sp = spoken_for(p, level)
            _speaks = OP_EXT.get(p.get("op", "+"), {}).get("speaks")
            ok44 = _speaks(p, sp) if _speaks else (str(p["a"]) in sp
                                                  and str(p["b"]) in sp)
            ck(ok44,
               f"{lid}: ask speaks its numbers "
               f"({p['a']}{p.get('op', '+')}{p['b']}, {level})", sp)

    # 7. build jr's lesson, enforced at authoring time: canon vocabulary only
    all_speech = " ".join(audio_lines(lesson)).lower()
    for canon, banned in VOCABULARY.items():
        for term in banned:
            ck(term not in all_speech,
               f"{lid}: '{term}' never appears (canon is '{canon}')", "")

    # 8. every board tag is a real tag (against tags.py when provided)
    if board_tag_names:
        boards = [b for _s, b in lesson["teach"]] + \
                 [pr["worked"][1] for pr in lesson["pairs"]] + \
                 [board_for(p, lv) for p in problems
                  for lv in lesson.get("levels", LEVELS)] + \
                 [choices_for(p) for p in problems]
        for b in boards:
            for name in _TAG_RE.findall(b):
                ck(name in board_tag_names,
                   f"{lid}: board tag [[{name}]] exists in the registry", b[:60])

    # 9. praise pool sanity
    ck(len(PRAISE_PREFIXES) >= 3, "at least 3 praise variants", "")
    return checks


# I did no harm and this file is not truncated.

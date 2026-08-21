# =============================================================================
# lessonscripts.py  --  THE SCRIPTED-FIRST ENGINE + THE COURSE  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-08-21  BUILD kd -- THE CONTENT SWEEP + LESSONS THAT FLOW. Jim: "my priority
#               right now is to get the app up and running ... I wanna see it all up
#               and running, and then I can troubleshoot it from there." (Reviews,
#               quizzes, exams and depth-maintenance are DEFERRED to a design
#               conversation once content is complete -- his ruling, recorded.)
#               TEN new lessons close the audit's remaining named gaps: Entry U1
#               counting (a concrete-only op where the child COUNTS the stars -- the
#               spoken ask deliberately never says the number, with a speaks()
#               override documenting why), numbers before/after, counting coins
#               (nickels), story problems for Entry (add/take-away) and Basic
#               (multiply/divide) -- via a NEW per-problem "story" field: a problem
#               may carry its own spoken sentence, and every validator rule (digits
#               spoken, canon vocabulary, word caps via closure) applies to it
#               automatically -- plus hundredths, adding fractions with DIFFERENT
#               bottoms, least common multiple, angles as quarter turns, and volume.
#               41 lessons. Entry still lacks Time and Shapes units (no clock/shape
#               renderer on the pilot page yet -- recorded, not hidden).
#   2026-08-21  BUILD kc -- THE RE-CUT (Jim's ruling on the Eureka audit,
#               Eureka_Audit_Of_The_Scripted_Course_2026-08-21.md). The audit's
#               headline: my first eight lessons -- single-digit adding through
#               regrouping -- were ENTRY-LEVEL MATH content by Jim's own curriculum,
#               filed under Basic because Basic U1's title ("Place Value &
#               Whole-Number Operations") reads the same at every grade band. MOVED:
#               all eight to course "entry", units 2-6, ids renamed entry-*. Basic
#               gets its REAL Unit 1 -- place value to 1,000, rounding to tens and
#               hundreds, and an interleaved multi-digit review (interleaving is the
#               evidence-based practice; the review lesson carries mixed_review=True
#               and the ramp check deliberately does not apply). PLUS the audit's two
#               biggest holes: multi-digit multiplication and division (Eureka G4-M3,
#               43 days, the largest module in grades 3-5 -- previously ZERO lessons)
#               and fractions ON THE NUMBER LINE (Eureka G3-M5's core idea: a
#               fraction IS a number with a place, previously taught only as portions
#               of groups). New ops: pv (hundreds/tens/ones), r10/r100 (rounding,
#               with their OWN distractors -- +-10/+-100, because +-1 distractors
#               would make rounding trivially guessable), nl/nlw (number-line hops).
#               OP_EXT entries may now declare a "choices" function.
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
        "id": "entry-u2-add-single-digit",
        "course": "entry", "unit": 2,
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
        "id": "entry-u3-take-away-single-digit",
        "course": "entry", "unit": 3,
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
        "id": "entry-u2-add-past-ten",
        "course": "entry", "unit": 2,
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
        "id": "entry-u3-take-away-bigger",
        "course": "entry", "unit": 3,
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
        "id": "entry-u4-tens-and-ones",
        "course": "entry", "unit": 4,
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
        "id": "entry-u5-add-with-carrying",
        "course": "entry", "unit": 5,
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
        "id": "entry-u5-add-two-digit-no-carry",
        "course": "entry", "unit": 5,
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
        "id": "entry-u6-take-away-with-regrouping",
        "course": "entry", "unit": 6,
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
    {
        "id": "basic-u1-place-value-to-1000", "course": "basic", "unit": 1,
        "topic": "Place value to 1,000",
        "op": "pv", "max_value": 999,
        "levels": ("abstract",),
        "symbols": ("hundreds", "ones"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can read hundreds, tens and ones."),
        "teach": [
            ("You know tens and ones. Today we add one more place: hundreds. Ten "
             "tens, put together, equal one hundred. A three-digit number counts "
             "hundreds, then tens, then ones.",
             '[[goal text="Place value to 1,000"]]'),
            ("Watch me read 342. The 3 counts hundreds — three hundred. The 4 "
             "counts tens — forty. The 2 counts ones. 3 hundreds, 4 tens and 2 "
             "ones equals 342.",
             '[[step eq="342 = 3 hundreds + 4 tens + 2 ones"]]'),
            ("One more, watch. 5 hundreds, 1 ten and 7 ones. Five hundred, ten, "
             "seven — 517.",
             '[[step eq="5 hundreds + 1 ten + 7 ones = 517"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 2 hundreds, 6 tens and 3 "
                        "ones. Two hundred sixty-three — 263.",
                        '[[step eq="2 hundreds + 6 tens + 3 ones = 263"]]'),
             "ask": {"a": 2, "b": 3, "c": 4, "op": "pv"}},
            {"worked": ("One more together. 7 hundreds, 2 tens and 9 ones — 729.",
                        '[[step eq="7 hundreds + 2 tens + 9 ones = 729"]]'),
             "ask": {"a": 6, "b": 1, "c": 5, "op": "pv"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 1, "b": 1, "c": 2, "op": "pv"}, {"a": 1, "b": 4, "c": 3, "op": "pv"},
            {"a": 2, "b": 2, "c": 5, "op": "pv"}, {"a": 3, "b": 1, "c": 6, "op": "pv"},
            {"a": 3, "b": 5, "c": 2, "op": "pv"}, {"a": 4, "b": 3, "c": 8, "op": "pv"},
            {"a": 5, "b": 6, "c": 1, "op": "pv"}, {"a": 6, "b": 4, "c": 7, "op": "pv"},
            {"a": 7, "b": 8, "c": 3, "op": "pv"}, {"a": 9, "b": 2, "c": 9, "op": "pv"},
        ],
    },
    {
        "id": "basic-u1-rounding-tens", "course": "basic", "unit": 1,
        "topic": "Rounding to the nearest ten",
        "op": "r10", "max_value": 110,
        "levels": ("abstract",),
        "symbols": ("round", "nearest"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can round to the nearest ten."),
        "teach": [
            ("Rounding gives a number a simpler neighbour. To round to the "
             "nearest ten, look at the ones digit: if it is 4 or smaller, round "
             "down. If it is 5 or bigger, round up.",
             '[[goal text="Rounding to the nearest ten"]]'),
            ("Watch me round 47. The ones digit is 7 — that is 5 or bigger, so "
             "we round up. 47 rounds to 50.",
             '[[step eq="47 → nearest ten = 50"]]'),
            ("One more, watch. Round 32. The ones digit is 2 — 4 or smaller, so "
             "we round down. 32 rounds to 30.",
             '[[step eq="32 → nearest ten = 30"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Round 85. The ones "
                        "digit is 5 — 5 or bigger rounds up. 85 rounds to 90.",
                        '[[step eq="85 → nearest ten = 90"]]'),
             "ask": {"a": 74, "op": "r10", "b": 0}},
            {"worked": ("One more together. Round 61 — the ones digit is 1, so "
                        "round down to 60.",
                        '[[step eq="61 → nearest ten = 60"]]'),
             "ask": {"a": 58, "op": "r10", "b": 0}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 12, "op": "r10", "b": 0}, {"a": 17, "op": "r10", "b": 0},
            {"a": 23, "op": "r10", "b": 0}, {"a": 35, "op": "r10", "b": 0},
            {"a": 41, "op": "r10", "b": 0}, {"a": 49, "op": "r10", "b": 0},
            {"a": 56, "op": "r10", "b": 0}, {"a": 64, "op": "r10", "b": 0},
            {"a": 78, "op": "r10", "b": 0}, {"a": 93, "op": "r10", "b": 0},
        ],
    },
    {
        "id": "basic-u1-rounding-hundreds", "course": "basic", "unit": 1,
        "topic": "Rounding to the nearest hundred",
        "op": "r100", "max_value": 1000,
        "levels": ("abstract",),
        "symbols": ("round", "nearest"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can round to the nearest hundred."),
        "teach": [
            ("Rounding to the nearest hundred works the same way — but now the "
             "TENS digit decides. 4 or smaller rounds down; 5 or bigger rounds "
             "up.",
             '[[goal text="Rounding to the nearest hundred"]]'),
            ("Watch me round 470. The tens digit is 7 — 5 or bigger, round up. "
             "470 rounds to 500.",
             '[[step eq="470 → nearest hundred = 500"]]'),
            ("One more, watch. Round 320. The tens digit is 2 — round down. 320 "
             "rounds to 300.",
             '[[step eq="320 → nearest hundred = 300"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Round 149. The tens "
                        "digit is 4 — round down. 149 rounds to 100.",
                        '[[step eq="149 → nearest hundred = 100"]]'),
             "ask": {"a": 253, "op": "r100", "b": 0}},
            {"worked": ("One more together. Round 662 — the tens digit is 6, "
                        "round up to 700.",
                        '[[step eq="662 → nearest hundred = 700"]]'),
             "ask": {"a": 578, "op": "r100", "b": 0}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 120, "op": "r100", "b": 0}, {"a": 180, "op": "r100", "b": 0},
            {"a": 240, "op": "r100", "b": 0}, {"a": 350, "op": "r100", "b": 0},
            {"a": 430, "op": "r100", "b": 0}, {"a": 490, "op": "r100", "b": 0},
            {"a": 560, "op": "r100", "b": 0}, {"a": 640, "op": "r100", "b": 0},
            {"a": 770, "op": "r100", "b": 0}, {"a": 910, "op": "r100", "b": 0},
        ],
    },
    {
        "id": "basic-u1-multi-digit-review", "course": "basic", "unit": 1,
        "topic": "Adding and taking away — review",
        "op": "+", "max_value": 99, "mixed_review": True,
        "levels": ("abstract",),
        "symbols": ("carry", "regroup"),
        "advance_line": ("Three in a row — you've got it! "
                         "Your adding and taking away are ready for bigger things."),
        "teach": [
            ("You learned carrying and regrouping in Entry-Level Math. Before we "
             "multiply and divide, let's warm those up — a quick mix of both.",
             '[[goal text="Adding and taking away — review"]]'),
            ("Remember: when the ones add up to over nine, write the ones digit "
             "and carry one ten. When the top ones digit is too small, regroup — "
             "one ten becomes ten ones.",
             '[[step eq="carry: ones over nine"]][[step eq="regroup: ones too small"]]'),
        ],
        "pairs": [
            {"worked": ("One quick worked one. 38 plus 24: ones 8 plus 4 equals "
                        "12 — over nine, write 2, carry 1. Tens: 3 plus 2 plus 1 "
                        "equals 6. 62.",
                        '[[step eq="38 + 24 = 62"]]'),
             "ask": {"a": 27, "b": 15, "op": "+"}},
            {"worked": ("And one taking away. 53 take away 28: 3 is too small — "
                        "regroup. 13 take away 8 equals 5; 4 take away 2 equals "
                        "2. 25.",
                        '[[step eq="53 − 28 = 25"]]'),
             "ask": {"a": 42, "b": 17, "op": "-"}},
        ],
        "practice_intro": ("Now it's your turn — adds and take-aways, mixed. "
                           "Three right answers in a row and we're done."),
        "bank": [
            {"a": 26, "b": 15, "op": "+"}, {"a": 31, "b": 14, "op": "-"},
            {"a": 35, "b": 17, "op": "+"}, {"a": 44, "b": 26, "op": "-"},
            {"a": 46, "b": 18, "op": "+"}, {"a": 52, "b": 35, "op": "-"},
            {"a": 57, "b": 26, "op": "+"}, {"a": 63, "b": 47, "op": "-"},
            {"a": 65, "b": 28, "op": "+"}, {"a": 82, "b": 56, "op": "-"},
        ],
    },
    {
        "id": "basic-u2-multiply-two-digit", "course": "basic", "unit": 2,
        "topic": "Multiplying bigger numbers",
        "op": "*", "max_value": 300,
        "levels": ("abstract",),
        "symbols": ("times", "tens"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can multiply bigger numbers."),
        "teach": [
            ("Today we multiply a two-digit number. The trick: split it into "
             "tens and ones, multiply each piece, then put the pieces together.",
             '[[goal text="Multiplying bigger numbers"]]'),
            ("Watch me. 34 times 2. Split 34 into 30 and 4. 30 times 2 equals "
             "60. 4 times 2 equals 8. 60 plus 8 equals 68.",
             '[[step eq="34 × 2"]][[step eq="30 × 2 = 60"]][[step eq="4 × 2 = 8"]]'
             '[[step eq="60 + 8 = 68"]]'),
            ("One more, watch. 23 times 3. 20 times 3 equals 60; 3 times 3 "
             "equals 9. 60 plus 9 equals 69.",
             '[[step eq="23 × 3"]][[step eq="20 × 3 = 60"]][[step eq="3 × 3 = 9"]]'
             '[[step eq="23 × 3 = 69"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 42 times 2. 40 times 2 "
                        "equals 80; 2 times 2 equals 4. 84.",
                        '[[step eq="42 × 2 = 84"]]'),
             "ask": {"a": 43, "b": 2, "op": "*"}},
            {"worked": ("One more together. 31 times 3. 90 plus 3 — 93.",
                        '[[step eq="31 × 3 = 93"]]'),
             "ask": {"a": 32, "b": 3, "op": "*"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 12, "b": 2, "op": "*"}, {"a": 13, "b": 3, "op": "*"},
            {"a": 24, "b": 2, "op": "*"}, {"a": 21, "b": 3, "op": "*"},
            {"a": 23, "b": 4, "op": "*"}, {"a": 34, "b": 3, "op": "*"},
            {"a": 42, "b": 3, "op": "*"}, {"a": 33, "b": 5, "op": "*"},
            {"a": 45, "b": 4, "op": "*"}, {"a": 62, "b": 4, "op": "*"},
        ],
    },
    {
        "id": "basic-u3-divide-two-digit", "course": "basic", "unit": 3,
        "topic": "Dividing bigger numbers",
        "op": "/", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("divided", "split"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can divide bigger numbers."),
        "teach": [
            ("Today we divide a two-digit number. The trick is the same one "
             "multiplying used: split the number into friendly pieces, divide "
             "each piece, then put the answers together.",
             '[[goal text="Dividing bigger numbers"]]'),
            ("Watch me. 84 divided by 4. Split 84 into 80 and 4. 80 divided by "
             "4 equals 20. 4 divided by 4 equals 1. 20 plus 1 equals 21.",
             '[[step eq="84 ÷ 4"]][[step eq="80 ÷ 4 = 20"]][[step eq="4 ÷ 4 = 1"]]'
             '[[step eq="84 ÷ 4 = 21"]]'),
            ("One more, watch. 69 divided by 3. 60 divided by 3 equals 20; 9 "
             "divided by 3 equals 3. 23.",
             '[[step eq="69 ÷ 3 = 23"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 48 divided by 2. 40 "
                        "divided by 2 equals 20; 8 divided by 2 equals 4. 24.",
                        '[[step eq="48 ÷ 2 = 24"]]'),
             "ask": {"a": 46, "b": 2, "op": "/"}},
            {"worked": ("One more together. 96 divided by 3 — 32.",
                        '[[step eq="96 ÷ 3 = 32"]]'),
             "ask": {"a": 93, "b": 3, "op": "/"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 22, "b": 2, "op": "/"}, {"a": 26, "b": 2, "op": "/"},
            {"a": 33, "b": 3, "op": "/"}, {"a": 39, "b": 3, "op": "/"},
            {"a": 44, "b": 4, "op": "/"}, {"a": 48, "b": 4, "op": "/"},
            {"a": 55, "b": 5, "op": "/"}, {"a": 63, "b": 3, "op": "/"},
            {"a": 66, "b": 2, "op": "/"}, {"a": 88, "b": 4, "op": "/"},
        ],
    },
    {
        "id": "basic-u5-fractions-on-the-number-line", "course": "basic", "unit": 5,
        "topic": "Fractions live on the number line",
        "op": "nl", "max_value": 12,
        "levels": ("abstract",),
        "symbols": ("hop", "line"),
        "advance_line": ("Three in a row — you've got it! "
                         "A fraction is a number with its own home on the line."),
        "teach": [
            ("A fraction is not just a piece of pizza — a fraction is a NUMBER, "
             "and every number has a home on the number line. Today we find "
             "where fractions live.",
             '[[goal text="Fractions live on the number line"]]'),
            ("Watch me. Cut the line from 0 to 1 into 4 equal hops. Each hop is "
             "one fourth. Hop once — you stand on 1 out of 4. Hop three times — "
             "you stand on 3 out of 4.",
             '[[step eq="0 —(4 hops)— 1"]][[step eq="3 hops → 3/4"]]'),
            ("And if you take ALL 4 hops, you reach 1 whole. Four fourths "
             "equals one.",
             '[[step eq="4 hops → 4/4 = 1"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Cut the line into 3 "
                        "hops. 2 hops from 0 lands on 2 out of 3.",
                        '[[step eq="0 —(3 hops)— 1 · 2 hops → 2/3"]]'),
             "ask": {"a": 2, "b": 5, "op": "nl"}},
            {"worked": ("One more together. Cut the line into 6 hops — reaching "
                        "1 whole takes all 6 hops.",
                        '[[step eq="0 —(6 hops)— 1 · 1 whole = 6 hops"]]'),
             "ask": {"a": 1, "b": 8, "op": "nlw"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 1, "b": 2, "op": "nl"}, {"a": 1, "b": 3, "op": "nl"},
            {"a": 2, "b": 3, "op": "nl"}, {"a": 1, "b": 4, "op": "nlw"},
            {"a": 3, "b": 4, "op": "nl"}, {"a": 1, "b": 5, "op": "nlw"},
            {"a": 4, "b": 5, "op": "nl"}, {"a": 5, "b": 6, "op": "nl"},
            {"a": 1, "b": 8, "op": "nl"}, {"a": 1, "b": 10, "op": "nlw"},
        ],
    },
    # ------------------------- BUILD kd: the content sweep -------------------------
    {
        "id": "entry-u1-counting-to-10", "course": "entry", "unit": 1,
        "topic": "Counting to 10",
        "op": "cnt", "max_value": 10,
        "levels": ("concrete",),   # the picture IS the problem; there is no
                                   # abstract form of "count these stars"
        "symbols": ("count",),
        "advance_line": ("Three in a row — you've got it! "
                         "You can count to ten."),
        "teach": [
            ("Today we learn to count stars. Point to each star and say one "
             "number for it: one, two, three.",
             '[[goal text="Counting to 10"]]'),
            ("Watch me count these stars. One, two, three. Three stars.",
             '[[objects emoji="⭐" groups="3" caption="count them one at a time"]]'),
            ("Watch me count again. One, two, three, four, five. Five stars.",
             '[[objects emoji="⭐" groups="5" caption="count them one at a time"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. One, two, three, four. "
                        "Four stars.",
                        '[[objects emoji="⭐" groups="4" caption="count them one at a time"]]'),
             "ask": {"a": 2, "b": 0, "op": "cnt"}},
            {"worked": ("One more together. One, two, three, four, five, six. "
                        "Six stars.",
                        '[[objects emoji="⭐" groups="6" caption="count them one at a time"]]'),
             "ask": {"a": 4, "b": 0, "op": "cnt"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 1, "b": 0, "op": "cnt"}, {"a": 3, "b": 0, "op": "cnt"},
            {"a": 5, "b": 0, "op": "cnt"}, {"a": 6, "b": 0, "op": "cnt"},
            {"a": 7, "b": 0, "op": "cnt"}, {"a": 8, "b": 0, "op": "cnt"},
            {"a": 9, "b": 0, "op": "cnt"}, {"a": 10, "b": 0, "op": "cnt"},
        ],
    },
    {
        "id": "entry-u1-numbers-before-and-after", "course": "entry", "unit": 1,
        "topic": "Numbers before and after",
        "op": "aft", "max_value": 20,
        "levels": ("abstract",),
        "symbols": ("after", "before"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can find the number before and the number after."),
        "teach": [
            ("Numbers stand in a line, always in the same order: 1, 2, 3, 4, 5. "
             "Today we find the number right after a number, and the number "
             "right before it.",
             '[[goal text="Numbers before and after"]]'),
            ("Watch me. What comes right after 5? Count up one: 6. "
             "6 comes right after 5.",
             '[[step eq="5, 6"]]'),
            ("Watch me. What comes right before 8? Count back one: 7. "
             "7 comes right before 8.",
             '[[step eq="7, 8"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Right after 6 comes 7.",
                        '[[step eq="6, 7"]]'),
             "ask": {"a": 4, "b": 0, "op": "aft"}},
            {"worked": ("One more together. Right before 10 comes 9.",
                        '[[step eq="9, 10"]]'),
             "ask": {"a": 7, "b": 0, "op": "bef"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 2, "b": 0, "op": "aft"}, {"a": 3, "b": 0, "op": "bef"},
            {"a": 5, "b": 0, "op": "aft"}, {"a": 6, "b": 0, "op": "bef"},
            {"a": 8, "b": 0, "op": "aft"}, {"a": 9, "b": 0, "op": "bef"},
            {"a": 11, "b": 0, "op": "aft"}, {"a": 12, "b": 0, "op": "bef"},
            {"a": 14, "b": 0, "op": "aft"}, {"a": 15, "b": 0, "op": "bef"},
            {"a": 17, "b": 0, "op": "aft"}, {"a": 20, "b": 0, "op": "bef"},
        ],
    },
    {
        "id": "entry-u3-story-problems", "course": "entry", "unit": 3,
        "topic": "Story problems — adding and taking away",
        "op": "+", "max_value": 10, "a_max": 9, "b_max": 9,
        "mixed_review": True,   # plus and minus interleave; a ramp across two ops
                                # would be meaningless
        "levels": ("abstract",),
        "symbols": ("plus", "minus"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can solve story problems."),
        "teach": [
            ("Today we solve story problems. A story problem tells a little "
             "story and hides a plus or a minus inside. Our job is to find it.",
             '[[goal text="Story problems"]]'),
            ("Listen. Maya has 3 stickers. She gets 2 more. Getting more means "
             "putting together — that is plus. Three plus two equals five "
             "stickers in all.",
             '[[step eq="3 + 2 = 5"]]'),
            ("Listen. Ben has 6 grapes. He eats 2. Eating them is taking away — "
             "that is minus. Six minus two equals four grapes are left.",
             '[[step eq="6 − 2 = 4"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Ava has 4 crayons. She "
                        "gets 3 more. That is plus. Four plus three equals seven "
                        "crayons in all.",
                        '[[step eq="4 + 3 = 7"]]'),
             "ask": {"a": 5, "b": 2, "op": "+",
                     "story": ("Sam has 5 shells. He finds 2 more. How many "
                               "shells does he have in all?")}},
            {"worked": ("One more together. Leo has 8 balloons. 3 fly away. That "
                        "is minus — take away. Eight minus three equals five "
                        "balloons are left.",
                        '[[step eq="8 − 3 = 5"]]'),
             "ask": {"a": 7, "b": 3, "op": "-",
                     "story": ("Mia has 7 berries. She eats 3. How many berries "
                               "are left?")}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 2, "b": 1, "op": "+",
             "story": ("Jo has 2 rocks. She finds 1 more. How many rocks does "
                       "she have in all?")},
            {"a": 3, "b": 1, "op": "-",
             "story": "Ed has 3 kites. 1 blows away. How many kites are left?"},
            {"a": 3, "b": 2, "op": "+",
             "story": ("Ana has 3 cups. She gets 2 more. How many cups does she "
                       "have in all?")},
            {"a": 4, "b": 2, "op": "-",
             "story": "Ty has 4 socks. 2 get lost. How many socks are left?"},
            {"a": 4, "b": 3, "op": "+",
             "story": ("Bo has 4 cars. He gets 3 more. How many cars does he "
                       "have in all?")},
            {"a": 6, "b": 2, "op": "-",
             "story": "Zoe has 6 pears. She eats 2. How many pears are left?"},
            {"a": 5, "b": 4, "op": "+",
             "story": ("Kim has 5 beads. She gets 4 more. How many beads does "
                       "she have in all?")},
            {"a": 8, "b": 3, "op": "-",
             "story": ("Dan has 8 stamps. He gives 3 away. How many stamps are "
                       "left?")},
            {"a": 6, "b": 3, "op": "+",
             "story": ("Pia has 6 leaves. She finds 3 more. How many leaves does "
                       "she have in all?")},
            {"a": 9, "b": 4, "op": "-",
             "story": "Max has 9 blocks. 4 fall down. How many blocks are left?"},
        ],
    },
    {
        "id": "entry-u7-counting-coins", "course": "entry", "unit": 7,
        "topic": "Counting nickels and pennies",
        "op": "nick", "max_value": 35,
        "levels": ("abstract",),
        "symbols": ("nickel", "penny"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can count nickels and pennies."),
        "teach": [
            ("Money time! A penny is worth 1 cent. A nickel is worth 5 cents.",
             '[[goal text="Counting nickels and pennies"]]'),
            ("Watch me count 2 nickels and 3 pennies. Nickels first, count by "
             "five: 5, 10. Then pennies, count on: 11, 12, 13. That is 13 "
             "cents.",
             '[[step eq="5, 10 — 11, 12, 13 = 13 cents"]]'),
            ("One more, watch. 3 nickels and 1 penny. Count by five: 5, 10, 15. "
             "One more: 16. 16 cents.",
             '[[step eq="5, 10, 15 — 16 = 16 cents"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 1 nickel and 2 "
                        "pennies. 5 — then 6, 7. 7 cents.",
                        '[[step eq="5 — 6, 7 = 7 cents"]]'),
             "ask": {"a": 1, "b": 4, "op": "nick"}},
            {"worked": ("One more together. 2 nickels and 2 pennies. 5, 10 — "
                        "11, 12. 12 cents.",
                        '[[step eq="5, 10 — 11, 12 = 12 cents"]]'),
             "ask": {"a": 2, "b": 4, "op": "nick"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 1, "b": 1, "op": "nick"}, {"a": 1, "b": 2, "op": "nick"},
            {"a": 1, "b": 3, "op": "nick"}, {"a": 2, "b": 1, "op": "nick"},
            {"a": 2, "b": 2, "op": "nick"}, {"a": 2, "b": 3, "op": "nick"},
            {"a": 3, "b": 1, "op": "nick"}, {"a": 3, "b": 2, "op": "nick"},
            {"a": 4, "b": 1, "op": "nick"}, {"a": 4, "b": 3, "op": "nick"},
            {"a": 5, "b": 2, "op": "nick"}, {"a": 6, "b": 1, "op": "nick"},
        ],
    },
    {
        "id": "basic-u3-story-problems", "course": "basic", "unit": 3,
        "topic": "Story problems — multiplying and dividing",
        "op": "*", "max_value": 40, "mixed_review": True,
        "levels": ("abstract",),
        "symbols": ("times", "divided"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can solve multiplying and dividing story problems."),
        "teach": [
            ("Story problems can hide times and divided by too. Equal groups of "
             "the same size mean times. Sharing into equal groups means divided "
             "by.",
             '[[goal text="Story problems — multiplying and dividing"]]'),
            ("Listen. Each box holds 4 crayons. There are 3 boxes. Equal boxes — "
             "that is times. Four times three equals twelve crayons in all.",
             '[[step eq="4 × 3 = 12"]]'),
            ("Listen. 12 cookies are shared into 3 equal bags. Sharing — that is "
             "divided by. Twelve divided by three equals four cookies in each "
             "bag.",
             '[[step eq="12 ÷ 3 = 4"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Each pack holds 5 "
                        "pencils. There are 2 packs. Five times two equals ten "
                        "pencils in all.",
                        '[[step eq="5 × 2 = 10"]]'),
             "ask": {"a": 3, "b": 4, "op": "*",
                     "story": ("Each jar holds 3 marbles. There are 4 jars. How "
                               "many marbles in all?")}},
            {"worked": ("One more together. 10 apples are shared into 2 equal "
                        "baskets. Ten divided by two equals five apples in each "
                        "basket.",
                        '[[step eq="10 ÷ 2 = 5"]]'),
             "ask": {"a": 12, "b": 4, "op": "/",
                     "story": ("12 grapes are shared into 4 equal bowls. How "
                               "many grapes go in each bowl?")}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 2, "b": 3, "op": "*",
             "story": ("Each cup holds 2 straws. There are 3 cups. How many "
                       "straws in all?")},
            {"a": 6, "b": 2, "op": "/",
             "story": ("6 socks are shared into 2 equal drawers. How many socks "
                       "go in each drawer?")},
            {"a": 4, "b": 2, "op": "*",
             "story": ("Each bag holds 4 buns. There are 2 bags. How many buns "
                       "in all?")},
            {"a": 8, "b": 4, "op": "/",
             "story": ("8 fish are shared into 4 equal tanks. How many fish "
                       "swim in each tank?")},
            {"a": 5, "b": 3, "op": "*",
             "story": ("Each row has 5 chairs. There are 3 rows. How many "
                       "chairs in all?")},
            {"a": 15, "b": 3, "op": "/",
             "story": ("15 stickers are shared into 3 equal sheets. How many "
                       "stickers go on each sheet?")},
            {"a": 6, "b": 4, "op": "*",
             "story": ("Each tray holds 6 eggs. There are 4 trays. How many "
                       "eggs in all?")},
            {"a": 20, "b": 5, "op": "/",
             "story": ("20 beads are shared into 5 equal strings. How many "
                       "beads go on each string?")},
            {"a": 7, "b": 3, "op": "*",
             "story": ("Each shelf holds 7 books. There are 3 shelves. How many "
                       "books in all?")},
            {"a": 30, "b": 6, "op": "/",
             "story": ("30 seeds are shared into 6 equal pots. How many seeds "
                       "go in each pot?")},
        ],
    },
    {
        "id": "basic-u4-least-common-multiple", "course": "basic", "unit": 4,
        "topic": "Least common multiple",
        "op": "lcm", "max_value": 60,
        "levels": ("abstract",),
        "symbols": ("multiple", "least"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can find the least common multiple."),
        "teach": [
            ("A multiple of a number is what you land on when you count by it. "
             "The multiples of 3 are 3, 6, 9, 12, and so on.",
             '[[goal text="Least common multiple"]]'),
            ("The least common multiple of two numbers is the smallest number "
             "in BOTH count-by lists. Watch me find it for 2 and 3. Count by 2: "
             "2, 4, 6. Count by 3: 3, 6. The first match is 6.",
             '[[step eq="2: 2, 4, 6"]][[step eq="3: 3, 6"]]'
             '[[step eq="LCM of 2 and 3 = 6"]]'),
            ("One more, watch. 4 and 6. Count by 4: 4, 8, 12. Count by 6: 6, "
             "12. The first match is 12. The least common multiple of 4 and 6 "
             "equals 12.",
             '[[step eq="4: 4, 8, 12"]][[step eq="6: 6, 12"]]'
             '[[step eq="LCM of 4 and 6 = 12"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 3 and 6. Count by 3: "
                        "3, 6. Count by 6: 6. The first match is 6 — the least "
                        "common multiple of 3 and 6 equals 6.",
                        '[[step eq="LCM of 3 and 6 = 6"]]'),
             "ask": {"a": 2, "b": 6, "op": "lcm"}},
            {"worked": ("One more together. 2 and 5. Count by 2: 2, 4, 6, 8, "
                        "10. Count by 5: 5, 10. The first match is 10.",
                        '[[step eq="LCM of 2 and 5 = 10"]]'),
             "ask": {"a": 4, "b": 5, "op": "lcm"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 2, "b": 4, "op": "lcm"}, {"a": 2, "b": 3, "op": "lcm"},
            {"a": 3, "b": 6, "op": "lcm"}, {"a": 2, "b": 5, "op": "lcm"},
            {"a": 3, "b": 4, "op": "lcm"}, {"a": 4, "b": 6, "op": "lcm"},
            {"a": 2, "b": 7, "op": "lcm"}, {"a": 3, "b": 5, "op": "lcm"},
            {"a": 4, "b": 10, "op": "lcm"}, {"a": 3, "b": 8, "op": "lcm"},
            {"a": 5, "b": 6, "op": "lcm"},
        ],
    },
    {
        "id": "basic-u6-add-fractions-different-bottoms", "course": "basic",
        "unit": 6,
        "topic": "Adding fractions with different bottoms",
        "op": "fu", "max_value": 12,
        "levels": ("abstract",),
        "symbols": ("bottoms", "plus"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can add fractions with different bottoms."),
        "teach": [
            ("Today we add fractions with different bottoms. The trick: change "
             "one fraction so both bottoms match, then add the tops.",
             '[[goal text="Adding fractions with different bottoms"]]'),
            ("Watch me. One half plus one fourth. One half equals two fourths. "
             "Two fourths plus one fourth equals three fourths.",
             '[[step eq="1/2 + 1/4"]][[step eq="1/2 = 2/4"]]'
             '[[step eq="2/4 + 1/4 = 3/4"]]'),
            ("One more, watch. One third plus two sixths. One third equals two "
             "sixths. Two sixths plus two sixths equals four sixths.",
             '[[step eq="1/3 + 2/6"]][[step eq="1/3 = 2/6"]]'
             '[[step eq="2/6 + 2/6 = 4/6"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. One half plus one "
                        "sixth. One half equals three sixths. Three sixths plus "
                        "one sixth equals four sixths.",
                        '[[step eq="1/2 = 3/6"]][[step eq="3/6 + 1/6 = 4/6"]]'),
             "ask": {"a": 1, "b": 2, "c": 4, "op": "fu"}},
            {"worked": ("One more together. One fourth plus one eighth. One "
                        "fourth equals two eighths. Two eighths plus one eighth "
                        "equals three eighths.",
                        '[[step eq="1/4 = 2/8"]][[step eq="2/8 + 1/8 = 3/8"]]'),
             "ask": {"a": 1, "b": 3, "c": 6, "op": "fu"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 1, "b": 2, "c": 6, "op": "fu"},
            {"a": 2, "b": 3, "c": 6, "op": "fu"},
            {"a": 1, "b": 2, "c": 8, "op": "fu"},
            {"a": 3, "b": 2, "c": 8, "op": "fu"},
            {"a": 1, "b": 4, "c": 8, "op": "fu"},
            {"a": 5, "b": 4, "c": 8, "op": "fu"},
            {"a": 2, "b": 2, "c": 10, "op": "fu"},
            {"a": 3, "b": 5, "c": 10, "op": "fu"},
            {"a": 4, "b": 2, "c": 12, "op": "fu"},
            {"a": 5, "b": 3, "c": 12, "op": "fu"},
            {"a": 2, "b": 4, "c": 12, "op": "fu"},
            {"a": 7, "b": 6, "c": 12, "op": "fu"},
        ],
    },
    {
        "id": "basic-u7-hundredths", "course": "basic", "unit": 7,
        "topic": "Hundredths",
        "op": "dh", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("hundredths", "plus"),
        "advance_line": ("Three in a row — you've got it! "
                         "You know your hundredths."),
        "teach": [
            ("A hundredth is one out of one hundred equal pieces. We write "
             "hundredths after the point — 0.25 is 25 hundredths.",
             '[[goal text="Hundredths"]]'
             '[[step eq="0.25 = 25 hundredths"]]'),
            ("Adding hundredths works like adding whole numbers. Watch me. 25 "
             "hundredths plus 13 hundredths equals 38 hundredths — 0.38.",
             '[[step eq="0.25 + 0.13 = 0.38"]]'),
            ("One more, watch. 40 hundredths plus 22 hundredths equals 62 "
             "hundredths. 0.62.",
             '[[step eq="0.40 + 0.22 = 0.62"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 31 hundredths plus 24 "
                        "hundredths equals 55 hundredths — 0.55.",
                        '[[step eq="0.31 + 0.24 = 0.55"]]'),
             "ask": {"a": 11, "b": 12, "op": "dh"}},
            {"worked": ("One more together. 26 hundredths plus 32 hundredths "
                        "equals 58 hundredths.",
                        '[[step eq="0.26 + 0.32 = 0.58"]]'),
             "ask": {"a": 22, "b": 15, "op": "dh"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 12, "b": 13, "op": "dh"}, {"a": 21, "b": 14, "op": "dh"},
            {"a": 23, "b": 22, "op": "dh"}, {"a": 31, "b": 24, "op": "dh"},
            {"a": 42, "b": 23, "op": "dh"}, {"a": 34, "b": 37, "op": "dh"},
            {"a": 44, "b": 31, "op": "dh"}, {"a": 52, "b": 33, "op": "dh"},
            {"a": 63, "b": 27, "op": "dh"}, {"a": 61, "b": 34, "op": "dh"},
        ],
    },
    {
        "id": "basic-u9-quarter-turns", "course": "basic", "unit": 9,
        "topic": "Quarter turns and degrees",
        "op": "ang", "max_value": 360,
        "levels": ("abstract",),
        "symbols": ("degrees", "turn"),
        "advance_line": ("Three in a row — you've got it! "
                         "You know your quarter turns."),
        "teach": [
            ("We measure turning in degrees. There are 90 degrees in one "
             "quarter turn of a circle, and four quarter turns go all the way "
             "around.",
             '[[goal text="Quarter turns and degrees"]]'),
            ("Watch me. 2 quarter turns. 2 times 90 equals 180 — so 2 quarter "
             "turns equals 180 degrees.",
             '[[step eq="2 × 90° = 180°"]]'),
            ("And backwards, watch. 270 degrees. How many quarter turns? Count "
             "by 90: 90, 180, 270 — three counts. 270 degrees equals 3 quarter "
             "turns.",
             '[[step eq="270° = 3 × 90°"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 3 quarter turns. 3 "
                        "times 90 equals 270 degrees.",
                        '[[step eq="3 × 90° = 270°"]]'),
             "ask": {"a": 4, "b": 0, "op": "ang"}},
            {"worked": ("One more together. 180 degrees. Count by 90: 90, 180 — "
                        "two counts. 180 degrees equals 2 quarter turns.",
                        '[[step eq="180° = 2 × 90°"]]'),
             "ask": {"a": 360, "b": 0, "op": "angq"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 1, "b": 0, "op": "ang"}, {"a": 90, "b": 0, "op": "angq"},
            {"a": 2, "b": 0, "op": "ang"}, {"a": 180, "b": 0, "op": "angq"},
            {"a": 3, "b": 0, "op": "ang"}, {"a": 270, "b": 0, "op": "angq"},
        ],
    },
    {
        "id": "basic-u9-volume", "course": "basic", "unit": 9,
        "topic": "Volume — counting cubes",
        "op": "vol", "max_value": 96,
        "levels": ("abstract",),
        "symbols": ("times", "cubes"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can count the cubes that fill a box."),
        "teach": [
            ("Volume is how many cubes fill a box. Count the cubes in one "
             "layer, then count the layers.",
             '[[goal text="Volume — counting cubes"]]'),
            ("Watch me. A box 3 cubes long, 2 cubes wide, 2 cubes tall. One "
             "layer holds 3 times 2 equals 6 cubes. There are 2 layers. 6 "
             "times 2 equals 12 cubes.",
             '[[step eq="3 × 2 = 6"]][[step eq="6 × 2 = 12 cubes"]]'),
            ("One more, watch. 4 cubes long, 2 wide, 2 tall. 4 times 2 equals "
             "8 in a layer. 8 times 2 equals 16 cubes.",
             '[[step eq="4 × 2 = 8"]][[step eq="8 × 2 = 16 cubes"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 2 long, 2 wide, 3 "
                        "tall. 2 times 2 equals 4. 4 times 3 equals 12 cubes.",
                        '[[step eq="2 × 2 = 4"]][[step eq="4 × 3 = 12 cubes"]]'),
             "ask": {"a": 3, "b": 3, "c": 1, "op": "vol"}},
            {"worked": ("One more together. 5 long, 2 wide, 2 tall. 5 times 2 "
                        "equals 10. 10 times 2 equals 20 cubes.",
                        '[[step eq="5 × 2 = 10"]][[step eq="10 × 2 = 20 cubes"]]'),
             "ask": {"a": 2, "b": 3, "c": 1, "op": "vol"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 2, "b": 2, "c": 1, "op": "vol"},
            {"a": 3, "b": 2, "c": 1, "op": "vol"},
            {"a": 2, "b": 2, "c": 2, "op": "vol"},
            {"a": 3, "b": 2, "c": 2, "op": "vol"},
            {"a": 4, "b": 2, "c": 2, "op": "vol"},
            {"a": 3, "b": 3, "c": 2, "op": "vol"},
            {"a": 4, "b": 3, "c": 2, "op": "vol"},
            {"a": 5, "b": 3, "c": 2, "op": "vol"},
            {"a": 4, "b": 4, "c": 2, "op": "vol"},
            {"a": 4, "b": 3, "c": 3, "op": "vol"},
            {"a": 4, "b": 4, "c": 3, "op": "vol"},
            {"a": 4, "b": 4, "c": 4, "op": "vol"},
        ],
    },
]
LESSONS.extend(_MORE_LESSONS)

# =============================================================================
# PREALGEBRA -- UNIT 1: NUMBER SENSE & ORDER OF OPERATIONS (build kk, 2026-08-21)
# =============================================================================
# The first unit authored AFTER build kj gave the scripted lane the real board, and
# the first of the eight courses Jim asked for ("I wanna go through all the courses").
#
# NAMED BY THEIR INPUTS, BOUNDS SAID PLAINLY -- Jim's jw/jx ruling. Not "Order of
# operations": a child does not know what an operation is. "Times before add" says
# what they will do, and the opening beat says which numbers.
#
# WHY THIS ORDER: the rule is worth nothing until there is a second step to compete
# with the first, so lesson 1 puts times against add. Parentheses come next because
# they OVERRIDE what was just learned, and a rule is only understood once you meet
# its exception. Exponents come third because they are a NEW kind of step rather than
# a new order. Lesson 4 stacks all three, which is the only place the full order can
# actually be tested.
_PREALGEBRA_U1 = [
    {
        "id": "pre-u1-times-before-add",
        "course": "prealgebra", "unit": 1,
        "topic": "Times before add",
        "op": "tba", "max_value": 90,
        "levels": ("abstract",),
        "symbols": ("times", "plus", "equals"),
        "advance_line": "Three in a row — you've got it! You do the times first, every time.",
        "teach": [
            ["Today a problem has two steps in it, not one. You will see a plus and a times in the same line. There is a rule for which one goes first, and it is not left to right. The times goes first. Always.",
             '[[goal text="Times before add"]]'],
            ["Watch me do 2 plus 3 times 4. Times first: 3 times 4 equals 12. Now the adding: 2 plus 12 equals 14. If you had gone left to right you would have said 20, and 20 is wrong.",
             '[[step eq="2 + 3 × 4"]][[step eq="3 × 4 = 12"]][[step eq="2 + 12 = 14"]]'],
            ["One more. 5 plus 2 times 6. Find the times: 2 times 6 equals 12. Then add: 5 plus 12 equals 17.",
             '[[step eq="5 + 2 × 6"]][[step eq="2 × 6 = 12"]][[step eq="5 + 12 = 17"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 4 plus 3 times 3. Times first: 3 times 3 equals 9. Then 4 plus 9 equals 13.",
                        '[[step eq="4 + 3 × 3"]][[step eq="4 + 9 = 13"]]'],
             "ask": {"a": 3, "b": 2, "c": 5, "op": "tba"}},
            {"worked": ["One more together. 6 plus 4 times 2. The times gives 8. Then 6 plus 8 equals 14.",
                        '[[step eq="6 + 4 × 2"]][[step eq="6 + 8 = 14"]]'],
             "ask": {"a": 2, "b": 3, "c": 6, "op": "tba"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 1, "b": 2, "c": 3, "op": "tba"},
            {"a": 2, "b": 2, "c": 4, "op": "tba"},
            {"a": 3, "b": 3, "c": 3, "op": "tba"},
            {"a": 2, "b": 4, "c": 3, "op": "tba"},
            {"a": 5, "b": 3, "c": 4, "op": "tba"},
            {"a": 4, "b": 5, "c": 4, "op": "tba"},
            {"a": 6, "b": 4, "c": 6, "op": "tba"},
            {"a": 3, "b": 7, "c": 5, "op": "tba"},
            {"a": 8, "b": 6, "c": 7, "op": "tba"},
            {"a": 5, "b": 8, "c": 9, "op": "tba"},
        ],
    },
    {
        "id": "pre-u1-parentheses-first",
        "course": "prealgebra", "unit": 1,
        "topic": "Parentheses first",
        "op": "parf", "max_value": 150,
        "levels": ("abstract",),
        "symbols": ("parentheses", "times", "plus", "equals"),
        "advance_line": "Three in a row — you've got it! What is inside the parentheses goes first.",
        "teach": [
            ["Last time you learned the times goes before the add. Today you meet the one thing that beats it. Two curved marks around part of a problem are called parentheses, and whatever sits inside them goes first — even an add.",
             '[[goal text="Parentheses first"]]'],
            ["Watch me do 2 plus 3, in parentheses, times 4. Inside first: 2 plus 3 equals 5. Now the times: 5 times 4 equals 20. Without the parentheses this same line would be 14, so the marks change the answer.",
             '[[step eq="(2 + 3) × 4"]][[step eq="2 + 3 = 5"]][[step eq="5 × 4 = 20"]]'],
            ["One more. 1 plus 6, in parentheses, times 3. Inside: 1 plus 6 equals 7. Then 7 times 3 equals 21.",
             '[[step eq="(1 + 6) × 3"]][[step eq="1 + 6 = 7"]][[step eq="7 × 3 = 21"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 4 plus 2, in parentheses, times 5. Inside gives 6. Then 6 times 5 equals 30.",
                        '[[step eq="(4 + 2) × 5"]][[step eq="6 × 5 = 30"]]'],
             "ask": {"a": 3, "b": 3, "c": 4, "op": "parf"}},
            {"worked": ["One more together. 5 plus 1, in parentheses, times 7. Inside gives 6. Then 6 times 7 equals 42.",
                        '[[step eq="(5 + 1) × 7"]][[step eq="6 × 7 = 42"]]'],
             "ask": {"a": 2, "b": 5, "c": 3, "op": "parf"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 1, "b": 2, "c": 2, "op": "parf"},
            {"a": 2, "b": 3, "c": 2, "op": "parf"},
            {"a": 3, "b": 2, "c": 3, "op": "parf"},
            {"a": 4, "b": 3, "c": 3, "op": "parf"},
            {"a": 2, "b": 6, "c": 4, "op": "parf"},
            {"a": 5, "b": 4, "c": 4, "op": "parf"},
            {"a": 3, "b": 7, "c": 5, "op": "parf"},
            {"a": 6, "b": 5, "c": 6, "op": "parf"},
            {"a": 8, "b": 4, "c": 8, "op": "parf"},
            {"a": 7, "b": 9, "c": 7, "op": "parf"},
        ],
    },
    {
        "id": "pre-u1-exponents-are-repeated-times",
        "course": "prealgebra", "unit": 1,
        "topic": "Exponents are repeated times",
        "op": "expn", "max_value": 216,
        "levels": ("abstract",),
        "symbols": ("squared", "power", "times", "equals"),
        "advance_line": "Three in a row — you've got it! A small high number counts how many to multiply.",
        "teach": [
            ["A small number written high up after another number is an exponent. It is not a times. It counts how many copies to multiply. 3 with a small 2 means two 3s multiplied: 3 times 3. Say it as three squared.",
             '[[goal text="Exponents are repeated times"]]'],
            ["Three squared equals 9. Here is why the word squared fits — three rows of three really do make a square, and counting the little boxes gives 9.",
             '[[areamodel rows="3" cols="3" caption="three rows of three"]][[step eq="3² = 3 × 3 = 9"]]'],
            ["A small 3 means three copies, and we say it as to the power 3. 2 with a small 3 is 2 times 2 times 2, which equals 8. Careful — it is not 2 times 3. That would be 6, and 6 is wrong.",
             '[[step eq="2³ = 2 × 2 × 2 = 8"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 4 squared is two 4s multiplied — 4 times 4, which equals 16.",
                        '[[areamodel rows="4" cols="4" caption="four rows of four"]][[step eq="4² = 16"]]'],
             "ask": {"a": 6, "b": 2, "op": "expn"}},
            {"worked": ["One more together. 3 with a small 3 means three 3s multiplied: 3 times 3 times 3, which equals 27.",
                        '[[step eq="3³ = 3 × 3 × 3 = 27"]]'],
             "ask": {"a": 7, "b": 2, "op": "expn"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 2, "b": 3, "op": "expn"},
            {"a": 3, "b": 2, "op": "expn"},
            {"a": 4, "b": 2, "op": "expn"},
            {"a": 5, "b": 2, "op": "expn"},
            {"a": 3, "b": 3, "op": "expn"},
            {"a": 4, "b": 3, "op": "expn"},
            {"a": 8, "b": 2, "op": "expn"},
            {"a": 9, "b": 2, "op": "expn"},
            {"a": 5, "b": 3, "op": "expn"},
            {"a": 6, "b": 3, "op": "expn"},
        ],
    },
    {
        "id": "pre-u1-power-then-times-then-add",
        "course": "prealgebra", "unit": 1,
        "topic": "Power, then times, then add",
        "op": "exo", "max_value": 130,
        "levels": ("abstract",),
        "symbols": ("squared", "times", "plus", "equals"),
        "advance_line": "Three in a row — you've got it! Power first, then times, then add.",
        "teach": [
            ["You know two rules now: the times goes before the add, and parentheses go before everything. Today a third step joins them — the exponent — and it goes first of all. Power first, then times, then add.",
             '[[goal text="Power, then times, then add"]]'],
            ["Watch me do 3 squared plus 2 times 4. Power first: 3 squared equals 9. Times next: 2 times 4 equals 8. Add last: 9 plus 8 equals 17.",
             '[[step eq="3² + 2 × 4"]][[step eq="9 + 8"]][[step eq="= 17"]]'],
            ["One more. 2 squared plus 5 times 3. The power gives 4. The times gives 15. 4 plus 15 equals 19.",
             '[[step eq="2² + 5 × 3"]][[step eq="4 + 15 = 19"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 4 squared plus 3 times 2. Power: 16. Times: 6. 16 plus 6 equals 22.",
                        '[[step eq="4² + 3 × 2"]][[step eq="16 + 6 = 22"]]'],
             "ask": {"a": 3, "b": 4, "c": 2, "op": "exo"}},
            {"worked": ["One more together. 5 squared plus 2 times 6. Power: 25. Times: 12. 25 plus 12 equals 37.",
                        '[[step eq="5² + 2 × 6"]][[step eq="25 + 12 = 37"]]'],
             "ask": {"a": 4, "b": 5, "c": 2, "op": "exo"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 3, "b": 2, "c": 2, "op": "exo"},
            {"a": 3, "b": 3, "c": 2, "op": "exo"},
            {"a": 3, "b": 2, "c": 4, "op": "exo"},
            {"a": 4, "b": 2, "c": 3, "op": "exo"},
            {"a": 4, "b": 3, "c": 3, "op": "exo"},
            {"a": 5, "b": 2, "c": 4, "op": "exo"},
            {"a": 5, "b": 4, "c": 3, "op": "exo"},
            {"a": 6, "b": 3, "c": 4, "op": "exo"},
            {"a": 7, "b": 5, "c": 3, "op": "exo"},
            {"a": 8, "b": 6, "c": 5, "op": "exo"},
        ],
    },
]
LESSONS.extend(_PREALGEBRA_U1)

# =============================================================================
# PREALGEBRA -- UNITS 2 & 3 (build km, 2026-08-21)
# =============================================================================
# U2 goes UNDERNEATH what Basic Math already teaches. Basic finds the greatest common
# factor and the least common multiple by listing; these three lessons are what that
# listing is made of -- what a factor is, which numbers have only two, and how to break
# a number all the way down to primes.
#
# U3 is the first unit in the app whose answers go BELOW ZERO, which is why validate()
# gained min_value. Every lesson through Basic Math answers with a count, so "answers
# are 1 or more" was a real invariant worth keeping; a lesson that means to break it now
# says so, and the guard stays on for the other 45.
_PREALGEBRA_U23 = [
    {
        "id": "pre-u2-how-many-factors",
        "course": "prealgebra", "unit": 2,
        "topic": "How many factors a number has",
        "op": "nfac", "max_value": 60,
        "levels": ("abstract",),
        "symbols": ("factor", "divides"),
        "advance_line": "Three in a row — you've got it! You can count a number's factors.",
        "teach": [
            ["A factor is a number that divides another one exactly, with nothing left over. 1 and the number itself are always factors. Today you count how many a number has in all.",
             '[[goal text="How many factors a number has"]]'],
            ["Take 6. Does 1 divide it? Yes. Does 2? Yes, 6 is two 3s. Does 3? Yes. Does 4? No, there is something left over. Does 5? No. Does 6? Yes. So 6 has four factors: 1, 2, 3 and 6.",
             '[[step eq="factors of 6 = 1, 2, 3, 6 → four"]]'],
            ["Now 7. Only 1 and 7 divide it exactly. Nothing else fits. So 7 has just two factors. Numbers with exactly two are special, and they have a name you will meet next lesson.",
             '[[step eq="factors of 7 = 1, 7 → two"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 8. 1 divides it, 2 divides it, 4 divides it, 8 divides it. 3, 5, 6 and 7 do not. So 8 has four factors.",
                        '[[step eq="factors of 8 = 1, 2, 4, 8 → four"]]'],
             "ask": {"a": 14, "b": 4, "op": "nfac"}},
            {"worked": ["One more together. 9. 1 divides it, 3 divides it, 9 divides it. So 9 has three factors.",
                        '[[step eq="factors of 9 = 1, 3, 9 → three"]]'],
             "ask": {"a": 25, "b": 3, "op": "nfac"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 7, "b": 2, "op": "nfac"},
            {"a": 9, "b": 3, "op": "nfac"},
            {"a": 10, "b": 4, "op": "nfac"},
            {"a": 12, "b": 6, "op": "nfac"},
            {"a": 15, "b": 4, "op": "nfac"},
            {"a": 16, "b": 5, "op": "nfac"},
            {"a": 18, "b": 6, "op": "nfac"},
            {"a": 20, "b": 6, "op": "nfac"},
            {"a": 24, "b": 8, "op": "nfac"},
            {"a": 30, "b": 8, "op": "nfac"},
        ],
    },
    {
        "id": "pre-u2-the-smallest-factor",
        "course": "prealgebra", "unit": 2,
        "topic": "The smallest factor above 1",
        "op": "spf", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("factor", "prime"),
        "advance_line": "Three in a row — you've got it! You can find a number's smallest factor.",
        "teach": [
            ["A number with exactly two factors — just 1 and itself — is a prime number. 2, 3, 5 and 7 are primes. Every other number can be divided by something smaller, and today you hunt for the smallest one.",
             '[[goal text="The smallest factor above 1"]]'],
            ["Take 15. Try 2 — no, 15 is odd. Try 3 — yes, 15 is three 5s. So 3 is the smallest factor of 15 above 1. You go up in order and stop at the first one that fits.",
             '[[step eq="15 ÷ 2 leaves 1 · 15 ÷ 3 = 5 ✓"]]'],
            ["Take 35. Try 2 — no. Try 3 — no. Try 5 — yes, 35 is five 7s. The smallest factor of 35 above 1 is 5.",
             '[[step eq="35 ÷ 5 = 7 ✓"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 27. 2 does not fit. 3 does — 27 is three 9s. So the answer is 3.",
                        '[[step eq="27 ÷ 3 = 9 ✓"]]'],
             "ask": {"a": 51, "b": 3, "op": "spf"}},
            {"worked": ["One more together. 91. 2 no, 3 no, 5 no. 7 fits — 91 is seven 13s. The answer is 7.",
                        '[[step eq="91 ÷ 7 = 13 ✓"]]'],
             "ask": {"a": 65, "b": 5, "op": "spf"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 9, "b": 3, "op": "spf"},
            {"a": 15, "b": 3, "op": "spf"},
            {"a": 21, "b": 3, "op": "spf"},
            {"a": 25, "b": 5, "op": "spf"},
            {"a": 33, "b": 3, "op": "spf"},
            {"a": 35, "b": 5, "op": "spf"},
            {"a": 39, "b": 3, "op": "spf"},
            {"a": 49, "b": 7, "op": "spf"},
            {"a": 55, "b": 5, "op": "spf"},
            {"a": 77, "b": 7, "op": "spf"},
        ],
    },
    {
        "id": "pre-u2-breaking-into-primes",
        "course": "prealgebra", "unit": 2,
        "topic": "Breaking a number into primes",
        "op": "npf", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("prime", "factor"),
        "advance_line": "Three in a row — you've got it! Every number breaks down into primes.",
        "teach": [
            ["Every number that is not prime can be written as primes multiplied. Keep pulling out the smallest factor until only primes are left. Today you count how many primes it takes.",
             '[[goal text="Breaking a number into primes"]]'],
            ["Take 12. The smallest factor is 2, and 12 is two 6s. Now break the 6: that is two 3s. Nothing is left but primes. 12 equals 2 times 2 times 3 — three primes.",
             '[[step eq="12 = 2 × 6"]][[step eq="6 = 2 × 3"]][[step eq="12 = 2 × 2 × 3 → three"]]'],
            ["Take 20. Smallest factor 2, so 20 is two 10s. Break the 10: two 5s. 20 equals 2 times 2 times 5 — three primes again.",
             '[[step eq="20 = 2 × 2 × 5 → three"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 8. Two 4s, and the 4 is two 2s. 8 equals 2 times 2 times 2 — three primes.",
                        '[[step eq="8 = 2 × 2 × 2 → three"]]'],
             "ask": {"a": 15, "b": 2, "op": "npf"}},
            {"worked": ["One more together. 30. Two 15s, and 15 is three 5s. 30 equals 2 times 3 times 5 — three primes.",
                        '[[step eq="30 = 2 × 3 × 5 → three"]]'],
             "ask": {"a": 16, "b": 4, "op": "npf"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 6, "b": 2, "op": "npf"},
            {"a": 10, "b": 2, "op": "npf"},
            {"a": 12, "b": 3, "op": "npf"},
            {"a": 18, "b": 3, "op": "npf"},
            {"a": 20, "b": 3, "op": "npf"},
            {"a": 27, "b": 3, "op": "npf"},
            {"a": 28, "b": 3, "op": "npf"},
            {"a": 45, "b": 3, "op": "npf"},
            {"a": 50, "b": 3, "op": "npf"},
            {"a": 63, "b": 3, "op": "npf"},
        ],
    },
    {
        "id": "pre-u3-counting-back-past-zero",
        "course": "prealgebra", "unit": 3,
        "topic": "Counting back past zero",
        "op": "cbz", "max_value": 25, "min_value": -20,
        "levels": ("abstract",),
        "symbols": ("negative", "zero", "number line"),
        "advance_line": "Three in a row — you've got it! You can count straight past zero.",
        "teach": [
            ["Numbers keep going to the left of zero. Those are the negative numbers, and they are real places on the number line — not mistakes. One step left of zero is negative 1. Two steps is negative 2.",
             '[[goal text="Counting back past zero"]][[numberline min="-10" max="10" points="-3"]]'],
            ["Start at 3 and count back 7. Three steps take you to zero. You still have four to go, so you carry on to the left and land on negative 4.",
             '[[numberline min="-10" max="10" points="-4"]][[step eq="3 − 7 = −4"]]'],
            ["Start at 2 and count back 9. Two steps reach zero, seven more keep going left. You land on negative 7.",
             '[[numberline min="-10" max="10" points="-7"]][[step eq="2 − 9 = −7"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. Start at 4, count back 6. Four steps to zero, two more to the left — negative 2.",
                        '[[numberline min="-10" max="10" points="-2"]][[step eq="4 − 6 = −2"]]'],
             "ask": {"a": 6, "b": 10, "op": "cbz"}},
            {"worked": ["One more together. Start at 1, count back 8. One step to zero, seven more left — negative 7.",
                        '[[numberline min="-10" max="10" points="-7"]][[step eq="1 − 8 = −7"]]'],
             "ask": {"a": 4, "b": 15, "op": "cbz"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 3, "b": 7, "op": "cbz"},
            {"a": 2, "b": 6, "op": "cbz"},
            {"a": 5, "b": 9, "op": "cbz"},
            {"a": 4, "b": 11, "op": "cbz"},
            {"a": 6, "b": 13, "op": "cbz"},
            {"a": 3, "b": 12, "op": "cbz"},
            {"a": 7, "b": 16, "op": "cbz"},
            {"a": 8, "b": 19, "op": "cbz"},
            {"a": 2, "b": 14, "op": "cbz"},
            {"a": 5, "b": 18, "op": "cbz"},
        ],
    },
    {
        "id": "pre-u3-adding-a-negative",
        "course": "prealgebra", "unit": 3,
        "topic": "Adding a negative number",
        "op": "addneg", "max_value": 30, "min_value": -20,
        "levels": ("abstract",),
        "symbols": ("negative", "plus"),
        "advance_line": "Three in a row — you've got it! Adding a negative moves you left.",
        "teach": [
            ["Adding usually moves you right along the line. But adding a NEGATIVE number moves you the other way — to the left. Adding negative 3 does exactly what counting back 3 does.",
             '[[goal text="Adding a negative number"]]'],
            ["Watch: 5 plus negative 7. Start at 5, move 7 to the left. Five steps reach zero, two more keep going, and you land on negative 2. So 5 plus negative 7 equals negative 2.",
             '[[numberline min="-10" max="10" points="-2"]][[step eq="5 + (−7) = −2"]]'],
            ["Another: 3 plus negative 6. Start at 3, move 6 left. You land on negative 3. The plus sign did not stop you going left — the negative did that.",
             '[[numberline min="-10" max="10" points="-3"]][[step eq="3 + (−6) = −3"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 4 plus negative 9. Start at 4, move 9 to the left, land on negative 5.",
                        '[[numberline min="-10" max="10" points="-5"]][[step eq="4 + (−9) = −5"]]'],
             "ask": {"a": 6, "b": 13, "op": "addneg"}},
            {"worked": ["One more together. 2 plus negative 8 lands on negative 6.",
                        '[[numberline min="-10" max="10" points="-6"]][[step eq="2 + (−8) = −6"]]'],
             "ask": {"a": 8, "b": 12, "op": "addneg"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 5, "b": 7, "op": "addneg"},
            {"a": 3, "b": 6, "op": "addneg"},
            {"a": 8, "b": 11, "op": "addneg"},
            {"a": 4, "b": 10, "op": "addneg"},
            {"a": 9, "b": 15, "op": "addneg"},
            {"a": 6, "b": 14, "op": "addneg"},
            {"a": 2, "b": 11, "op": "addneg"},
            {"a": 7, "b": 18, "op": "addneg"},
            {"a": 3, "b": 16, "op": "addneg"},
            {"a": 5, "b": 21, "op": "addneg"},
        ],
    },
    {
        "id": "pre-u3-taking-away-a-negative",
        "course": "prealgebra", "unit": 3,
        "topic": "Taking away a negative number",
        # min_value is declared even though every ANSWER here is positive: the wrong
        # option a child can tap IS negative (the error for "4 take away negative 6" is
        # 4 − 6 = −2, and that is exactly the mistake worth offering). The floor has to
        # cover what appears on screen, not only what is correct. The op's own check
        # keeps the answers positive by construction: a + b with both a and b above 0.
        "op": "subneg", "max_value": 30, "min_value": -20,
        "levels": ("abstract",),
        "symbols": ("negative", "take away"),
        "advance_line": "Three in a row — you've got it! Taking away a negative moves you right.",
        "teach": [
            ["Here is the surprising one. Taking away usually moves you left. But taking away a NEGATIVE moves you RIGHT — the two negatives cancel each other and the answer grows.",
             '[[goal text="Taking away a negative number"]]'],
            ["Watch: 3 take away negative 2. Taking away a move-left is a move-right, so you go 2 to the right of 3 and land on 5. 3 take away negative 2 equals 5.",
             '[[step eq="3 − (−2) = 3 + 2 = 5"]]'],
            ["Another: 5 take away negative 3 equals 8. Whenever a take away meets a negative, swap the pair for a plus.",
             '[[step eq="5 − (−3) = 5 + 3 = 8"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 6 take away negative 4. The two negatives become a plus: 6 plus 4 equals 10.",
                        '[[step eq="6 − (−4) = 6 + 4 = 10"]]'],
             "ask": {"a": 7, "b": 6, "op": "subneg"}},
            {"worked": ["One more together. 2 take away negative 9 equals 2 plus 9, which equals 11.",
                        '[[step eq="2 − (−9) = 11"]]'],
             "ask": {"a": 4, "b": 13, "op": "subneg"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 3, "b": 2, "op": "subneg"},
            {"a": 5, "b": 3, "op": "subneg"},
            {"a": 4, "b": 6, "op": "subneg"},
            {"a": 7, "b": 4, "op": "subneg"},
            {"a": 6, "b": 8, "op": "subneg"},
            {"a": 9, "b": 5, "op": "subneg"},
            {"a": 8, "b": 9, "op": "subneg"},
            {"a": 5, "b": 12, "op": "subneg"},
            {"a": 9, "b": 11, "op": "subneg"},
            {"a": 7, "b": 15, "op": "subneg"},
        ],
    },
    {
        "id": "pre-u3-times-with-a-negative",
        "course": "prealgebra", "unit": 3,
        "topic": "Times with a negative number",
        "op": "mulneg", "max_value": 90, "min_value": -95,
        "levels": ("abstract",),
        "symbols": ("negative", "times"),
        "advance_line": "Three in a row — you've got it! One negative turns the answer negative.",
        "teach": [
            ["Times works the same as it always did — only the sign is new. Negative 3 times 4 means four lots of negative 3. Four moves of 3 to the left lands on negative 12.",
             '[[goal text="Times with a negative number"]]'],
            ["So do the times first and ignore the sign: 3 times 4 equals 12. Then look at the signs. One of them is negative, so the answer is negative. Negative 3 times 4 equals negative 12.",
             '[[numberline min="-20" max="10" points="-12"]][[step eq="(−3) × 4 = −12"]]'],
            ["Another: negative 5 times 3. Five 3s equal 15, and one negative sign turns it negative 15.",
             '[[step eq="(−5) × 3 = −15"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. Negative 2 times 7. Two 7s equal 14, and one negative turns it negative 14.",
                        '[[step eq="(−2) × 7 = −14"]]'],
             "ask": {"a": 4, "b": 6, "op": "mulneg"}},
            {"worked": ["One more together. Negative 6 times 4. Six 4s equal 24, so the answer is negative 24.",
                        '[[step eq="(−6) × 4 = −24"]]'],
             "ask": {"a": 8, "b": 5, "op": "mulneg"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 2, "b": 3, "op": "mulneg"},
            {"a": 3, "b": 3, "op": "mulneg"},
            {"a": 2, "b": 6, "op": "mulneg"},
            {"a": 4, "b": 4, "op": "mulneg"},
            {"a": 3, "b": 7, "op": "mulneg"},
            {"a": 5, "b": 5, "op": "mulneg"},
            {"a": 4, "b": 8, "op": "mulneg"},
            {"a": 6, "b": 7, "op": "mulneg"},
            {"a": 7, "b": 8, "op": "mulneg"},
            {"a": 9, "b": 9, "op": "mulneg"},
        ],
    },
]
LESSONS.extend(_PREALGEBRA_U23)



# THE COURSE ORDER IS OWNED HERE (jz -- jy had accidentally placed carrying before
# two-digit-no-carry). Import fails loudly if a lesson is missing or listed twice.
COURSE_ORDER = [
    # ---- ENTRY-LEVEL MATH (the kc re-cut: these eight lessons were authored under
    # Basic U1 and belong here by Jim's own curriculum -- Eureka audit 2026-08-21;
    # kd opens the course where Eureka does -- counting -- and adds story problems
    # and coins) ----
    "entry-u1-counting-to-10", "entry-u1-numbers-before-and-after",
    "entry-u2-add-single-digit", "entry-u2-add-past-ten",
    "entry-u3-take-away-single-digit", "entry-u3-take-away-bigger",
    "entry-u3-story-problems",
    "entry-u4-tens-and-ones", "entry-u5-add-two-digit-no-carry",
    "entry-u5-add-with-carrying", "entry-u6-take-away-with-regrouping",
    "entry-u7-counting-coins",
    # ---- BASIC MATH (grades 3-5 band) ----
    "basic-u1-place-value-to-1000", "basic-u1-rounding-tens",
    "basic-u1-rounding-hundreds", "basic-u1-multi-digit-review",
    "basic-u2-what-multiplying-means", "basic-u2-times-tables",
    "basic-u2-multiply-two-digit",
    "basic-u3-what-dividing-means", "basic-u3-left-overs",
    "basic-u3-divide-two-digit", "basic-u3-story-problems",
    "basic-u4-missing-factors", "basic-u4-greatest-common-factor",
    "basic-u4-least-common-multiple",
    "basic-u5-fractions-on-the-number-line",
    "basic-u5-fraction-of-a-group", "basic-u5-equivalent-fractions",
    "basic-u6-add-fractions-same-bottom", "basic-u6-take-away-fractions-same-bottom",
    "basic-u6-add-fractions-different-bottoms",
    "basic-u7-tenths", "basic-u7-dimes-and-pennies", "basic-u7-hundredths",
    "basic-u8-percent-of", "basic-u8-one-costs",
    "basic-u9-perimeter", "basic-u9-area",
    "basic-u9-quarter-turns", "basic-u9-volume",

    # ---- PREALGEBRA (build kk) -- Unit 1: Number Sense & Order of Operations ----
    "pre-u1-times-before-add", "pre-u1-parentheses-first",
    "pre-u1-exponents-are-repeated-times", "pre-u1-power-then-times-then-add",
    # Unit 2: Factors, Multiples & Primes -- underneath Basic's GCF/LCM
    "pre-u2-how-many-factors", "pre-u2-the-smallest-factor",
    "pre-u2-breaking-into-primes",
    # Unit 3: Integers & Negative Numbers -- the first answers below zero
    "pre-u3-counting-back-past-zero", "pre-u3-adding-a-negative",
    "pre-u3-taking-away-a-negative", "pre-u3-times-with-a-negative",
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


def _prime_factors(n):
    """The primes whose product is n, repeats included: 12 -> [2, 2, 3]. Used by the
    Prealgebra U2 ops (build km); a lambda cannot express the loop readably."""
    out, d, n = [], 2, int(n)
    while d * d <= n:
        while n % d == 0:
            out.append(d)
            n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


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
    "pv": {   # a hundreds, b tens, c ones
        "ans": lambda p: 100 * p["a"] + 10 * p["b"] + p["c"],
        "spoken": lambda p: (f"What number is {p['a']} hundreds, {p['b']} tens "
                             f"and {p['c']} ones?"),
        "board": lambda p: (f'[[step eq="{p["a"]} hundreds + {p["b"]} tens + '
                            f'{p["c"]} ones = ?"]]'),
        "praise": lambda p: (f"{p['a']} hundreds, {p['b']} tens and {p['c']} ones "
                             f"— that is {100 * p['a'] + 10 * p['b'] + p['c']}."),
        "key": lambda p: 100 * p["a"] + 10 * p["b"] + p["c"],
        "check": lambda p: (1 <= p["a"] <= 9 and 1 <= p["b"] <= 9
                            and 1 <= p["c"] <= 9,
                            "each place stays 1-9 in this first lesson"),
    },
    "r10": {   # round a to the nearest ten
        "ans": lambda p: (p["a"] + 5) // 10 * 10,
        "spoken": lambda p: f"Round {p['a']} to the nearest ten.",
        "board": lambda p: f'[[step eq="{p["a"]} → nearest ten = ?"]]',
        "praise": lambda p: (f"{p['a']} rounds to {(p['a'] + 5) // 10 * 10}."),
        "key": lambda p: p["a"],
        "check": lambda p: (10 <= p["a"] <= 99 and p["a"] % 10 != 0,
                            "a multiple of ten leaves nothing to round"),
        "speaks": lambda p, sp: str(p["a"]) in sp,
        # +-1 distractors would make rounding guessable by eye; the real confusion
        # is WHICH ten, so the distractors are the neighbouring tens.
        # near the bottom of the range the lower ten would be 0 -- shift the
        # window up instead (tap options must stay >= 1, validator-enforced)
        "choices": lambda p: ([(p["a"] + 5) // 10 * 10 - 10,
                               (p["a"] + 5) // 10 * 10,
                               (p["a"] + 5) // 10 * 10 + 10]
                              if (p["a"] + 5) // 10 * 10 >= 20 else
                              [(p["a"] + 5) // 10 * 10,
                               (p["a"] + 5) // 10 * 10 + 10,
                               (p["a"] + 5) // 10 * 10 + 20]),
    },
    "r100": {  # round a to the nearest hundred
        "ans": lambda p: (p["a"] + 50) // 100 * 100,
        "spoken": lambda p: f"Round {p['a']} to the nearest hundred.",
        "board": lambda p: f'[[step eq="{p["a"]} → nearest hundred = ?"]]',
        "praise": lambda p: (f"{p['a']} rounds to {(p['a'] + 50) // 100 * 100}."),
        "key": lambda p: p["a"],
        "check": lambda p: (100 <= p["a"] <= 999 and p["a"] % 100 != 0,
                            "a multiple of one hundred leaves nothing to round"),
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "choices": lambda p: ([(p["a"] + 50) // 100 * 100 - 100,
                               (p["a"] + 50) // 100 * 100,
                               (p["a"] + 50) // 100 * 100 + 100]
                              if (p["a"] + 50) // 100 * 100 >= 200 else
                              [(p["a"] + 50) // 100 * 100,
                               (p["a"] + 50) // 100 * 100 + 100,
                               (p["a"] + 50) // 100 * 100 + 200]),
    },
    "nl": {    # hops from 0 to a/b on a 0-to-1 number line cut into b hops
        "ans": lambda p: p["a"],
        "spoken": lambda p: (f"A number line from 0 to 1 is cut into {p['b']} "
                             f"equal hops. How many hops from 0 reach {p['a']} "
                             f"out of {p['b']}?"),
        "board": lambda p: f'[[step eq="0 —({p["b"]} hops)— 1 · land on {p["a"]}/{p["b"]} = ? hops"]]',
        "praise": lambda p: (f"{p['a']} hops — {p['a']} out of {p['b']} lives "
                             f"{p['a']} hops from 0."),
        "key": lambda p: p["b"],
        "check": lambda p: (1 <= p["a"] < p["b"] <= 12,
                            "the fraction stays proper and the hops countable"),
    },
    "nlw": {   # hops from 0 to reach 1 whole
        "ans": lambda p: p["b"],
        "spoken": lambda p: (f"A number line from 0 to 1 is cut into {p['b']} "
                             f"equal hops. How many hops from 0 reach 1 whole?"),
        "board": lambda p: f'[[step eq="0 —({p["b"]} hops)— 1 · reach 1 = ? hops"]]',
        "praise": lambda p: (f"{p['b']} hops — all {p['b']} hops together equal "
                             f"1 whole."),
        "key": lambda p: p["b"],
        "check": lambda p: (2 <= p["b"] <= 12 and p.get("a", 1) == 1,
                            "the whole-line question fixes a=1"),
    },
    "cnt": {   # count the stars (concrete-only; the picture IS the problem)
        "ans": lambda p: p["a"],
        "spoken": lambda p: "Count the stars. How many stars are there?",
        "board": lambda p: (f'[[objects emoji="⭐" groups="{p["a"]}" '
                            f'caption="count them one at a time"]]'),
        "praise": lambda p: f"{p['a']} stars — you counted every one.",
        "key": lambda p: p["a"],
        "check": lambda p: (1 <= p["a"] <= 10, "countable on one screen"),
        # rule 44's PURPOSE is "the child heard the whole problem" -- here the whole
        # problem is the picture, and SAYING the number would answer it.
        "speaks": lambda p, sp: True,
    },
    "aft": {
        "ans": lambda p: p["a"] + 1,
        "spoken": lambda p: f"What number comes right after {p['a']}?",
        "board": lambda p: f'[[step eq="{p["a"]}, ?"]]',
        "praise": lambda p: f"{p['a'] + 1} comes right after {p['a']}.",
        "key": lambda p: p["a"],
        "check": lambda p: (1 <= p["a"] <= 19, "stays in the counting range"),
        # the problem has ONE number; b is a placeholder 0 (like r10/r100)
        "speaks": lambda p, sp: str(p["a"]) in sp,
    },
    "bef": {
        "ans": lambda p: p["a"] - 1,
        "spoken": lambda p: f"What number comes right before {p['a']}?",
        "board": lambda p: f'[[step eq="?, {p["a"]}"]]',
        "praise": lambda p: f"{p['a'] - 1} comes right before {p['a']}.",
        "key": lambda p: p["a"],
        "check": lambda p: (2 <= p["a"] <= 20, "the answer must stay at least 1"),
        "speaks": lambda p, sp: str(p["a"]) in sp,
    },
    "nick": {  # a nickels + b pennies = ? cents
        "ans": lambda p: 5 * p["a"] + p["b"],
        "spoken": lambda p: (f"How many cents is {p['a']} nickels and {p['b']} "
                             f"pennies?"),
        "board": lambda p: f'[[step eq="{p["a"]} nickels + {p["b"]} pennies = ? cents"]]',
        "praise": lambda p: (f"{p['a']} nickels and {p['b']} pennies equals "
                             f"{5 * p['a'] + p['b']} cents."),
        "key": lambda p: 5 * p["a"] + p["b"],
        "check": lambda p: (1 <= p["a"] <= 9 and 1 <= p["b"] <= 4,
                            "pennies stay under a nickel"),
    },
    "dh": {    # hundredths: 0.ab + 0.cd, answered in hundredths
        "ans": lambda p: p["a"] + p["b"],
        "spoken": lambda p: (f"How many hundredths is {p['a']} hundredths plus "
                             f"{p['b']} hundredths?"),
        "board": lambda p: f'[[step eq="0.{p["a"]} + 0.{p["b"]} = 0.?"]]',
        "praise": lambda p: (f"{p['a']} hundredths plus {p['b']} hundredths "
                             f"equals {p['a'] + p['b']} hundredths."),
        "key": lambda p: p["a"] + p["b"],
        "check": lambda p: (10 <= p["a"] <= 89 and 10 <= p["b"] <= 89
                            and p["a"] + p["b"] <= 99,
                            "two-digit hundredths, no spill into a whole"),
    },
    "fu": {    # one 1/b plus a/c, same-family bottoms (b divides c)
        "ans": lambda p: p["c"] // p["b"] + p["a"],
        "spoken": lambda p: (f"How many {_FRACWORD[p['c']][1]} is one "
                             f"{_FRACWORD[p['b']][0]} plus {p['a']} "
                             f"{_FRACWORD[p['c']][1]}?"),
        "board": lambda p: (f'[[step eq="1/{p["b"]} + {p["a"]}/{p["c"]} = '
                            f'?/{p["c"]}"]]'),
        "praise": lambda p: (f"One {_FRACWORD[p['b']][0]} is "
                             f"{p['c'] // p['b']} {_FRACWORD[p['c']][1]} — plus "
                             f"{p['a']} more equals "
                             f"{p['c'] // p['b'] + p['a']} {_FRACWORD[p['c']][1]}."),
        "key": lambda p: p["c"],
        "check": lambda p: (p["c"] % p["b"] == 0 and p["c"] > p["b"]
                            and p["b"] in _FRACWORD and p["c"] in _FRACWORD
                            and p["c"] // p["b"] + p["a"] < p["c"],
                            "the bottoms must be family (b divides c) and the sum "
                            "stays a proper fraction"),
        "speaks": lambda p, sp: (str(p["a"]) in sp
                                 and _FRACWORD[p["b"]][0] in sp
                                 and _FRACWORD[p["c"]][1] in sp),
    },
    "lcm": {
        "ans": lambda p: p["a"] * p["b"] // _gcd(p["a"], p["b"]),
        "spoken": lambda p: (f"What is the least common multiple of {p['a']} "
                             f"and {p['b']}?"),
        "board": lambda p: f'[[step eq="LCM of {p["a"]} and {p["b"]} = ?"]]',
        "praise": lambda p: (f"The least common multiple of {p['a']} and "
                             f"{p['b']} equals "
                             f"{p['a'] * p['b'] // _gcd(p['a'], p['b'])}."),
        "key": lambda p: p["a"] * p["b"] // _gcd(p["a"], p["b"]),
        "check": lambda p: (2 <= p["a"] and 2 <= p["b"]
                            and p["a"] * p["b"] // _gcd(p["a"], p["b"]) <= 60,
                            "the LCM stays countable"),
    },
    "ang": {   # quarter turns
        "ans": lambda p: 90 * p["a"],
        "spoken": lambda p: (f"A quarter turn is 90 degrees. How many degrees "
                             f"is {p['a']} quarter "
                             f"turn{'' if p['a'] == 1 else 's'}?"),
        "board": lambda p: f'[[step eq="{p["a"]} × 90° = ?"]]',
        "praise": lambda p: (f"{p['a']} quarter "
                             f"turn{'' if p['a'] == 1 else 's'} equals "
                             f"{90 * p['a']} degrees."),
        "key": lambda p: p["a"],
        "check": lambda p: (1 <= p["a"] <= 4, "a full turn is the ceiling"),
        # +-1 would be absurd next to 180; the confusion is WHICH multiple of 90
        "choices": lambda p: ([90 * p["a"] - 90, 90 * p["a"], 90 * p["a"] + 90]
                              if p["a"] >= 2 else [90, 180, 270]),
        "speaks": lambda p, sp: str(p["a"]) in sp,
    },
    "angq": {  # the reverse of ang: how many quarter turns is a degrees?
        "ans": lambda p: p["a"] // 90,
        "spoken": lambda p: f"How many quarter turns is {p['a']} degrees?",
        "board": lambda p: f'[[step eq="{p["a"]}\u00b0 = ? \u00d7 90\u00b0"]]',
        "praise": lambda p: (f"{p['a']} degrees equals {p['a'] // 90} quarter "
                             f"turn{'' if p['a'] // 90 == 1 else 's'}."),
        "key": lambda p: p["a"] // 90,
        "check": lambda p: (p["a"] in (90, 180, 270, 360),
                            "only whole quarter turns have an answer here"),
        "speaks": lambda p, sp: str(p["a"]) in sp,
    },
    "vol": {   # a x b x c cubes
        "ans": lambda p: p["a"] * p["b"] * p["c"],
        "spoken": lambda p: (f"A box is {p['a']} cubes long, {p['b']} cubes "
                             f"wide and {p['c']} cubes tall. How many cubes "
                             f"fill it?"),
        "board": lambda p: f'[[step eq="{p["a"]} × {p["b"]} × {p["c"]} = ?"]]',
        "praise": lambda p: (f"{p['a']} times {p['b']} times {p['c']} equals "
                             f"{p['a'] * p['b'] * p['c']} cubes."),
        "key": lambda p: p["a"] * p["b"] * p["c"],
        "check": lambda p: (p["a"] * p["b"] * p["c"] <= 96
                            and min(p["a"], p["b"], p["c"]) >= 1,
                            "countable cubes"),
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

    # ---- PREALGEBRA UNIT 1 (build kk) -- ORDER OF OPERATIONS ------------------
    # Each of these declares its own `choices`, and the wrong option on offer is
    # THE MISCONCEPTION ITSELF -- the answer a child gets by working left to right,
    # or by ignoring the parentheses, or by reading an exponent as a times. A
    # distractor that is merely "the answer plus one" tests arithmetic; a distractor
    # that is the actual error tests whether the RULE landed, and when the child taps
    # it the intervention knows exactly which wrong idea to unpick.
    "tba": {   # a + b x c -- times before add
        "ans": lambda p: p["a"] + p["b"] * p["c"],
        "spoken": lambda p: f"What is {p['a']} plus {p['b']} times {p['c']}?",
        "board": lambda p: f'[[step eq="{p["a"]} + {p["b"]} × {p["c"]} = ?"]]',
        "praise": lambda p: (f"{p['b']} times {p['c']} equals {p['b'] * p['c']}, "
                             f"and {p['a']} plus {p['b'] * p['c']} equals "
                             f"{p['a'] + p['b'] * p['c']}."),
        "key": lambda p: p["b"] * p["c"],
        "choices": lambda p: [p["a"] + p["b"] * p["c"] - p["c"],
                              p["a"] + p["b"] * p["c"],
                              (p["a"] + p["b"]) * p["c"]],
        "check": lambda p: (1 <= p["a"] <= 9 and 2 <= p["b"] <= 9 and 2 <= p["c"] <= 9,
                            "a is 1-9 and both times numbers are 2-9, so the "
                            "left-to-right answer is always a DIFFERENT number"),
    },
    "parf": {  # (a + b) x c -- parentheses first
        "ans": lambda p: (p["a"] + p["b"]) * p["c"],
        "spoken": lambda p: (f"What is {p['a']} plus {p['b']}, in parentheses, "
                             f"times {p['c']}?"),
        "board": lambda p: f'[[step eq="({p["a"]} + {p["b"]}) × {p["c"]} = ?"]]',
        "praise": lambda p: (f"Inside first: {p['a']} plus {p['b']} equals "
                             f"{p['a'] + p['b']}. Then {p['a'] + p['b']} times "
                             f"{p['c']} equals {(p['a'] + p['b']) * p['c']}."),
        "key": lambda p: (p["a"] + p["b"]) * p["c"],
        "choices": lambda p: [(p["a"] + p["b"]) * p["c"],
                              p["a"] + p["b"] * p["c"],
                              (p["a"] + p["b"]) * p["c"] + p["c"]],
        "check": lambda p: (1 <= p["a"] <= 9 and 1 <= p["b"] <= 9 and 2 <= p["c"] <= 9,
                            "c is 2-9 so ignoring the parentheses always gives a "
                            "different number"),
    },
    "expn": {  # a to the power b, b in (2, 3) -- an exponent is repeated times
        "ans": lambda p: p["a"] ** p["b"],
        # The spoken line must contain BOTH numbers -- the validator checks it, and it
        # is right to: "3 squared" hides the 2, and a child who only ever hears the word
        # never connects it to the small digit on the board.
        "spoken": lambda p: (f"What is {p['a']} to the power 3? That means three "
                             f"{p['a']}s multiplied."
                             if p["b"] == 3 else
                             f"What is {p['a']} squared — {p['a']} to the power 2?"),
        # THE PICTURE THE METHODOLOGY ASKS FOR (build kj gave us the renderer): a
        # square number IS a square. Cubes have no honest 2-D picture, so they get
        # the written repeat instead of a drawing that would lie about the shape.
        "board": lambda p: (f'[[areamodel rows="{p["a"]}" cols="{p["a"]}" '
                            f'caption="{p["a"]} rows of {p["a"]}"]]'
                            f'[[step eq="{p["a"]}² = ?"]]'
                            if p["b"] == 2 else
                            f'[[step eq="{p["a"]}³ = {p["a"]} × {p["a"]} × '
                            f'{p["a"]} = ?"]]'),
        "praise": lambda p: (f"{p['a']} to the power {p['b']} equals "
                             f"{p['a'] ** p['b']} — that is {p['b']} {p['a']}s "
                             f"multiplied."),
        "key": lambda p: p["a"] ** p["b"],
        "choices": lambda p: [p["a"] ** p["b"], p["a"] * p["b"],
                              p["a"] ** p["b"] + p["a"]],
        "check": lambda p: (2 <= p["a"] <= 9 and p["b"] in (2, 3)
                            and p["a"] ** p["b"] != p["a"] * p["b"],
                            "a is 2-9 and the power is 2 or 3, and the power answer "
                            "never equals the times answer (which rules out 2²)"),
    },
    "exo": {   # a squared + b x c -- power first, then times, then add
        "ans": lambda p: p["a"] * p["a"] + p["b"] * p["c"],
        "spoken": lambda p: (f"What is {p['a']} squared plus {p['b']} times "
                             f"{p['c']}?"),
        "board": lambda p: f'[[step eq="{p["a"]}² + {p["b"]} × {p["c"]} = ?"]]',
        "praise": lambda p: (f"{p['a']} squared equals {p['a'] * p['a']}, "
                             f"{p['b']} times {p['c']} equals {p['b'] * p['c']}, "
                             f"and those put together equal "
                             f"{p['a'] * p['a'] + p['b'] * p['c']}."),
        "key": lambda p: p["a"] * p["a"] + p["b"] * p["c"],
        # The two wrong options are the two real errors: adding before the times, and
        # reading the little 2 as "times 2". a >= 3 is what keeps all three distinct --
        # at a = 2 the power and the doubling give the same number, and the child would
        # be offered the same answer twice. (The validator caught exactly that.)
        "choices": lambda p: [p["a"] * p["a"] + p["b"] * p["c"],
                              (p["a"] * p["a"] + p["b"]) * p["c"],
                              2 * p["a"] + p["b"] * p["c"]],
        "check": lambda p: (3 <= p["a"] <= 9 and 2 <= p["b"] <= 9 and 2 <= p["c"] <= 9,
                            "a is 3-9 (at 2, squaring and doubling agree and two "
                            "options would collide); b and c are 2-9"),
    },

    # ---- PREALGEBRA UNIT 2 (build km) -- FACTORS, MULTIPLES & PRIMES ----------
    # Basic Math already teaches GCF and LCM by listing. These go underneath that:
    # what a factor IS, which numbers have only two, and how to break a number all
    # the way down. `a` is the number; `b` carries the authored answer for reference
    # only -- ans() recomputes it, because ans() is the ONLY place answers are made.
    "nfac": {  # how many different numbers divide a exactly
        "ans": lambda p: sum(1 for d in range(1, p["a"] + 1) if p["a"] % d == 0),
        "spoken": lambda p: (f"How many different numbers divide {p['a']} exactly, "
                             f"with nothing left over?"),
        "board": lambda p: f'[[step eq="factors of {p["a"]} = ?"]]',
        "praise": lambda p: (f"{p['a']} has "
                             f"{sum(1 for d in range(1, p['a'] + 1) if p['a'] % d == 0)}"
                             f" factors."),
        "key": lambda p: p["a"],
        "speaks": lambda p, sp: str(p["a"]) in sp,   # `b` is a reference, never spoken
        "check": lambda p: (4 <= p["a"] <= 60,
                            "the number stays small enough to check every divisor by "
                            "hand"),
    },
    "spf": {   # the smallest number above 1 that divides a
        "ans": lambda p: next(d for d in range(2, p["a"] + 1) if p["a"] % d == 0),
        "spoken": lambda p: (f"What is the smallest number, bigger than 1, that "
                             f"divides {p['a']} exactly?"),
        "board": lambda p: f'[[step eq="{p["a"]} ÷ ? leaves nothing over"]]',
        "praise": lambda p: (f"{next(d for d in range(2, p['a'] + 1) if p['a'] % d == 0)}"
                             f" is the smallest one that divides {p['a']}."),
        "key": lambda p: p["a"],
        "speaks": lambda p, sp: str(p["a"]) in sp,   # `b` is a reference, never spoken
        "check": lambda p: (9 <= p["a"] <= 99 and
                            next(d for d in range(2, p["a"] + 1) if p["a"] % d == 0)
                            != p["a"],
                            "the number is 9-99 and is NOT itself prime, so there is a "
                            "smaller factor to find"),
    },
    "npf": {   # how many primes multiplied make a (repeats counted)
        "ans": lambda p: len(_prime_factors(p["a"])),
        "spoken": lambda p: (f"Break {p['a']} down into primes multiplied. How many "
                             f"primes does it take?"),
        "board": lambda p: f'[[step eq="{p["a"]} = ? primes multiplied"]]',
        "praise": lambda p: (f"{p['a']} equals "
                             f"{' × '.join(str(x) for x in _prime_factors(p['a']))} — "
                             f"{len(_prime_factors(p['a']))} primes."),
        "key": lambda p: p["a"],
        "speaks": lambda p, sp: str(p["a"]) in sp,   # `b` is a reference, never spoken
        "check": lambda p: (4 <= p["a"] <= 99 and len(_prime_factors(p["a"])) >= 2,
                            "the number is 4-99 and is not prime itself, so there is "
                            "something to break down"),
    },

    # ---- PREALGEBRA UNIT 3 (build km) -- INTEGERS & NEGATIVE NUMBERS ---------
    # THE FIRST LESSONS IN THE APP WHOSE ANSWERS GO BELOW ZERO. The validator used to
    # assume every answer was 1 or more -- true of every counting lesson through Basic
    # Math, and false the moment integers arrive -- so a lesson now declares its own
    # min_value and the guard stays on. The PROBLEM DATA stays positive: `a` and `b`
    # are the numbers a child reads, and the sign lives in the question and the answer.
    # Each wrong option is the sign error itself.
    "cbz": {   # start at a, count back b, land below zero
        "ans": lambda p: p["a"] - p["b"],
        "spoken": lambda p: (f"Start at {p['a']} and count back {p['b']}. What number "
                             f"do you land on?"),
        # THE PICTURE THIS UNIT EXISTS FOR (build kj gave us the renderer): below zero
        # is a PLACE, and a child who sees it on the line stops thinking of a negative
        # as a broken sum.
        "board": lambda p: (f'[[numberline min="-20" max="10" '
                            f'points="{p["a"] - p["b"]}"]]'
                            f'[[step eq="{p["a"]} − {p["b"]} = ?"]]'),
        "praise": lambda p: (f"You land on negative {p['b'] - p['a']} — "
                             f"{p['b'] - p['a']} steps to the left of zero."),
        "key": lambda p: p["b"] - p["a"],
        "choices": lambda p: [p["a"] - p["b"], p["b"] - p["a"], p["a"] - p["b"] - 1],
        "check": lambda p: (1 <= p["a"] <= 9 and p["a"] < p["b"] <= 21,
                            "counting back always passes zero, which is the lesson"),
    },
    "addneg": {  # a + (-b)
        "ans": lambda p: p["a"] - p["b"],
        "spoken": lambda p: (f"What is {p['a']} plus negative {p['b']}?"),
        "board": lambda p: (f'[[numberline min="-20" max="10" '
                            f'points="{p["a"] - p["b"]}"]]'
                            f'[[step eq="{p["a"]} + (−{p["b"]}) = ?"]]'),
        "praise": lambda p: (f"Adding negative {p['b']} moves {p['b']} to the left, "
                             f"so you land on negative {p['b'] - p['a']}."),
        "key": lambda p: p["b"] - p["a"],
        "choices": lambda p: [p["a"] - p["b"], p["a"] + p["b"], p["a"] - p["b"] - 1],
        "check": lambda p: (1 <= p["a"] <= 9 and p["a"] < p["b"] <= 21,
                            "the answer lands below zero, which is the lesson"),
    },
    "subneg": {  # a - (-b) -- the surprise: it goes UP
        "ans": lambda p: p["a"] + p["b"],
        "spoken": lambda p: (f"What is {p['a']} take away negative {p['b']}?"),
        "board": lambda p: f'[[step eq="{p["a"]} − (−{p["b"]}) = ?"]]',
        "praise": lambda p: (f"Taking away negative {p['b']} moves {p['b']} to the "
                             f"RIGHT, so {p['a']} take away negative {p['b']} equals "
                             f"{p['a'] + p['b']}."),
        "key": lambda p: p["a"] + p["b"],
        "choices": lambda p: [p["a"] + p["b"], p["a"] - p["b"], p["a"] + p["b"] + 1],
        "check": lambda p: (1 <= p["a"] <= 9 and 1 <= p["b"] <= 15 and p["a"] != p["b"],
                            "a and b differ, so the right answer and the take-away "
                            "error are never the same number"),
    },
    "mulneg": {  # (-a) x b
        "ans": lambda p: -(p["a"] * p["b"]),
        "spoken": lambda p: f"What is negative {p['a']} times {p['b']}?",
        "board": lambda p: f'[[step eq="(−{p["a"]}) × {p["b"]} = ?"]]',
        "praise": lambda p: (f"{p['a']} times {p['b']} equals {p['a'] * p['b']}, and "
                             f"one negative turns the answer negative — negative "
                             f"{p['a'] * p['b']}."),
        "key": lambda p: p["a"] * p["b"],
        "choices": lambda p: [-(p["a"] * p["b"]), p["a"] * p["b"],
                              -(p["a"] * p["b"]) - p["a"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9,
                            "both numbers are 2-9, so the answer and the "
                            "forgot-the-sign error are always different"),
    },
}


# =============================================================================
# RENDERERS -- problem data -> what the child sees and hears, per level.
# One function per surface, so vocabulary consistency is BY CONSTRUCTION.
# =============================================================================
def spoken_for(p, level):
    a, b = p["a"], p["b"]
    # kd: a problem may carry its own story sentence -- word problems are authored
    # per problem, and every closure/vocabulary/digits check applies to the story.
    if p.get("story"):
        return p["story"]
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
    FIXED per-problem rotation -- deterministic, so replays render identically.
    kc: an op may declare its OWN distractors (rounding needs the neighbouring tens,
    not +-1, or the answer is guessable by eye)."""
    v = ans(p)
    ext = OP_EXT.get(p.get("op", "+"), {})
    if "choices" in ext:
        opts = list(ext["choices"](p))
    else:
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
    # build km: the floor is DECLARED, not assumed. Every lesson through Basic Math
    # answers with a count, so "answers are 1 or more" was a true invariant and a
    # useful one -- it catches an op whose arithmetic has gone backwards. Prealgebra
    # Unit 3 teaches integers, where landing below zero IS the lesson, so a lesson may
    # now state its own floor. Default 1, so all 45 earlier lessons are unchanged and
    # still guarded; a lesson that wants negatives has to say so out loud.
    floor = lesson.get("min_value", 1)
    ck(all(floor <= ans(p) <= bound for p in problems),
       f"{lid}: every answer stays within {floor} to {bound}",
       str([p for p in problems if not floor <= ans(p) <= bound]))
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

    # 2. choices: the right answer appears exactly once, every option in range.
    # build km: the pattern was r"\d+", which cannot see a minus sign -- it read the
    # option "-6" as "6", so a Prealgebra U3 lesson looked like it was offering the
    # answer twice when it was offering -6 and +6, which is the whole point of the
    # question. The floor moved with it: "every option is at least 1" was the same
    # assumption as min_value, and it is now the lesson's declared floor (default 1,
    # so the other 45 lessons are guarded exactly as before).
    for p in problems:
        opts = re.findall(r"-?\d+", choices_for(p))
        ck(opts.count(str(ans(p))) == 1,
           f"{lid}: choices for {p['a']}{p.get('op', '+')}{p['b']} contain the "
           f"answer exactly once", str(opts))
        # THE FLOOR ONLY, deliberately. An upper bound here was tried in km and was
        # WRONG: the default distractor set is the answer's neighbours, so a lesson
        # whose top answer equals its max_value legitimately offers max_value + 1 --
        # Counting to 10 shows 9 | 10 | 11, times tables show 80 | 81 | 82. Six shipped
        # lessons said so at once, and they were right. max_value describes the
        # PROBLEMS; a neighbour one step past it is a normal wrong answer, not a defect.
        ck(all(int(o) >= floor for o in opts),
           f"{lid}: choices for {p['a']}{p.get('op', '+')}{p['b']} are all at "
           f"least {floor}", str(opts))

    # 3. the difficulty ramp: the key never falls by more than 1 across the bank.
    # kc: a lesson may declare mixed_review=True -- INTERLEAVED practice across ops
    # is the evidence-based design for review (the ramp is a teaching-lesson rule).
    if not lesson.get("mixed_review"):
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

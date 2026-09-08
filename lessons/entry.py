# =============================================================================
# lessons/entry.py  --  ENTRY-LEVEL MATH: THE AUTHORED LESSONS  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-09-08  BUILD uj -- ONE FILE PER COURSE. Split out of lessonscripts.py (Jim's
#               housekeeping, second half). Every lesson below is the text that sat in
#               lessonscripts.py, moved whole -- the unit lists keep their names, and
#               the build notes above each unit came with them. ORDER at the bottom is
#               this course's slice of COURSE_ORDER (the teaching order). PURE DATA: no
#               imports, no functions -- the engine (lessonscripts.py) reads
#               lessons.LESSONS and lessons.COURSE_ORDER through lessons/__init__.py.
#               ADDING A LESSON: put it in its unit's list AND in ORDER; the battery's
#               validator, the closure prewarm and the demo pick it up from there.
# =============================================================================
LESSONS = []

# =============================================================================
# THE LESSONS -- Basic Math, Unit 1. Each authored to the research settings; each
# bank is ordered by its difficulty key (the 85%-success ramp).
# =============================================================================
_ENTRY_PILOT = [
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
             '[[objects emoji="⭐" groups="3" add="2" count="1" caption="count every star"]]'),
            ("Putting together has its very own sign. We write it like this, and "
             "we say it 'plus'. Three plus two.",
             '[[step eq="3 + 2"]]'),
            ("And when we know how many in all, we use one more sign. We write it "
             "like this, and we say it 'equals'. Three plus two equals five.",
             '[[step eq="3 + 2 = 5"]]'),
            ("Watch me do a whole one. Four stars, and one more star. I count "
             "every star: one, two, three, four, five. Four plus one equals five.",
             '[[objects emoji="⭐" groups="4" add="1" count="1" caption="count every star"]]'
             '[[step eq="4 + 1 = 5"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Two stars and two stars. "
                        "Count them all: one, two, three, four. Two plus two "
                        "equals four.",
                        '[[objects emoji="⭐" groups="2" add="2" count="1" caption="count every star"]]'
                        '[[step eq="2 + 2 = 4"]]'),
             "ask": {"a": 2, "b": 3, "op": "+"}},
            {"worked": ("One more together. Five stars and one star. Count them "
                        "all — six. Five plus one equals six.",
                        '[[objects emoji="⭐" groups="5" add="1" count="1" caption="count every star"]]'
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
             '[[objects emoji="⭐" groups="5" take="2" caption="start with five — take two away, then count what is left"]]'),
            ("Taking away has its own sign too. We write it like this, and we "
             "say it 'minus'. Five minus two.",
             '[[step eq="5 − 2"]]'),
            ("You already know the equals sign. Five minus two equals three.",
             '[[step eq="5 − 2 = 3"]]'),
            ("Watch me do a whole one. Six stars, take four away. Count what is "
             "left: one, two. Six minus four equals two.",
             '[[objects emoji="⭐" groups="6" take="4" caption="start with six — take four away"]]'
             '[[step eq="6 − 4 = 2"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Four stars, take one "
                        "away. Count what is left — three. Four minus one "
                        "equals three.",
                        '[[objects emoji="⭐" groups="4" take="1" caption="start with four — take one away"]]'
                        '[[step eq="4 − 1 = 3"]]'),
             "ask": {"a": 5, "b": 2, "op": "-"}},
            {"worked": ("One more together. Seven stars, take three away. Count "
                        "what is left — four. Seven minus three equals four.",
                        '[[objects emoji="⭐" groups="7" take="3" caption="start with seven — take three away"]]'
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
             '[[objects emoji="⭐" groups="13" take="5" caption="start with thirteen — take five away"]]'
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
                        '[[objects emoji="⭐" groups="12" take="4" caption="start with twelve — take four away"]]'
                        '[[step eq="12 − 4 = 8"]]'),
             "ask": {"a": 12, "b": 3, "op": "-"}},
            {"worked": ("One more together. Fifteen stars, take six away. Count "
                        "back from fifteen — nine. Fifteen minus six equals nine.",
                        '[[objects emoji="⭐" groups="15" take="6" caption="start with fifteen — take six away"]]'
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
LESSONS.extend(_ENTRY_PILOT)
    # ===================== (pg, 2026-08-27) ENTRY FILLS ITS UNITS ================
    # Sixteen lessons so that Entry-Level Math is nine units of four like every
    # other course. Until now a five-year-old who reached "which is bigger" or
    # "making change" dropped out of the authored lane into the live one and waited
    # seconds per sentence -- the worst possible place for the app to be slow.
    # House rules followed exactly: three teach beats (picture, worked, trap), two
    # worked pairs, a ten-problem bank, every sentence short enough to hear.
    # ============ (ph, 2026-08-28) THE LAST EIGHT -- THE COURSE IS WHOLE ========
    # Basic was short seven and Pre-Algebra one. With these, every one of the ten
    # courses is nine units of four, and there is no topic anywhere in the
    # curriculum that drops a child onto the live lane for want of a script.
_ENTRY_MORE = [
    {
        "id": "entry-u6-take-away-two-digit", "course": "entry", "unit": 6,
        "topic": "Taking away two-digit numbers", "op": "s2d", "max_value": 99,
        "levels": ("abstract",), "symbols": ("column",),
        "advance_line": "Three in a row — you've got it! You can take away two-digit numbers.",
        "teach": [
            ("Taking away two-digit numbers works column by column, the same as "
             "adding. Start on the right. Ones first, then tens. Today every ones "
             "digit on top is big enough, so nothing needs regrouping.",
             '[[goal text="Taking away two-digit numbers"]]'
             '[[step eq="58 − 23 = ?"]]'),
            ("Watch me take 23 away from 58. Ones: 8 take away 3 equals 5. Tens: 5 "
             "take away 2 equals 3. So 58 take away 23 equals 35.",
             '[[step eq="ones: 8 − 3 = 5"]]'
             '[[step eq="tens: 5 − 2 = 3"]]'
             '[[step eq="58 − 23 = 35"]]'),
            ("Here is the trap. Taking away has a direction. The top number goes "
             "first every time. In the ones column of 58 take away 23 it is 8 take "
             "away 3, never 3 take away 8.",
             '[[step eq="58 − 23 = 35 ✓"]]'
             '[[step eq="the ones are 8 − 3, not 3 − 8"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 76 take away 42. Ones: 6 "
                        "take away 2 equals 4. Tens: 7 take away 4 equals 3. That "
                        "is 34.",
                        '[[step eq="76 − 42 = 34"]]'),
             "ask": {"a": 89, "b": 35, "op": "s2d"}},
            {"worked": ("One more together. 67 take away 25. Ones: 7 take away 5 "
                        "equals 2. Tens: 6 take away 2 equals 4. That is 42.",
                        '[[step eq="67 − 25 = 42"]]'),
             "ask": {"a": 95, "b": 61, "op": "s2d"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": 20, "b": 10, "op": "s2d"}, {"a": 27, "b": 14, "op": "s2d"}, {"a": 30, "b": 10, "op": "s2d"}, {"a": 76, "b": 53, "op": "s2d"}, {"a": 95, "b": 65, "op": "s2d"}, {"a": 56, "b": 20, "op": "s2d"}, {"a": 94, "b": 51, "op": "s2d"}, {"a": 64, "b": 11, "op": "s2d"}, {"a": 85, "b": 21, "op": "s2d"}, {"a": 99, "b": 10, "op": "s2d"}],
    },
    {
        "id": "entry-u6-take-away-three-digit", "course": "entry", "unit": 6,
        "topic": "Taking away three-digit numbers", "op": "s3d", "max_value": 999,
        "levels": ("abstract",), "symbols": ("column",),
        "advance_line": "Three in a row — you've got it! You can take away three-digit numbers.",
        "teach": [
            ("Three columns now instead of two, and not one new idea. Ones first, "
             "then tens, then hundreds, always starting on the right.",
             '[[goal text="Taking away three-digit numbers"]]'
             '[[step eq="876 − 321 = ?"]]'),
            ("Watch me take 321 away from 876. Ones: 6 take away 1 equals 5. Tens: "
             "7 take away 2 equals 5. Hundreds: 8 take away 3 equals 5. So 876 "
             "take away 321 equals 555.",
             '[[step eq="ones: 6 − 1 = 5"]]'
             '[[step eq="tens: 7 − 2 = 5"]]'
             '[[step eq="hundreds: 8 − 3 = 5"]]'
             '[[step eq="876 − 321 = 555"]]'),
            ("Here is the trap, and it is a quiet one. Do not skip a column just "
             "because it looks easy. Every column gets worked, even one where the "
             "bottom digit is 0, because its answer still has to be written down.",
             '[[step eq="876 − 321 = 555 ✓"]]'
             '[[step eq="a skipped column leaves a hole in the answer"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 597 take away 243. Ones: "
                        "7 take away 3 equals 4. Tens: 9 take away 4 equals 5. "
                        "Hundreds: 5 take away 2 equals 3. That is 354.",
                        '[[step eq="597 − 243 = 354"]]'),
             "ask": {"a": 685, "b": 342, "op": "s3d"}},
            {"worked": ("One more together. 748 take away 216. Ones: 8 take away 6 "
                        "equals 2. Tens: 4 take away 1 equals 3. Hundreds: 7 take "
                        "away 2 equals 5. That is 532.",
                        '[[step eq="748 − 216 = 532"]]'),
             "ask": {"a": 969, "b": 427, "op": "s3d"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": 201, "b": 200, "op": "s3d"}, {"a": 347, "b": 306, "op": "s3d"}, {"a": 532, "b": 420, "op": "s3d"}, {"a": 374, "b": 211, "op": "s3d"}, {"a": 831, "b": 600, "op": "s3d"}, {"a": 958, "b": 646, "op": "s3d"}, {"a": 906, "b": 504, "op": "s3d"}, {"a": 713, "b": 211, "op": "s3d"}, {"a": 823, "b": 202, "op": "s3d"}, {"a": 999, "b": 100, "op": "s3d"}],
    },
    {
        "id": "entry-u6-checking-by-adding-back", "course": "entry", "unit": 6,
        "topic": "Checking by adding back", "op": "chk", "max_value": 99,
        "levels": ("abstract",), "symbols": ("check",),
        "advance_line": "Three in a row — you've got it! You can check your own answer.",
        "teach": [
            ("Here is something you can do that nobody has to mark for you. You "
             "can check a take away yourself. Adding and taking away undo each "
             "other, so adding your answer back should land on the number you "
             "started with.",
             '[[goal text="Checking by adding back"]]'
             '[[step eq="58 − 23 = 35, so 35 + 23 should be 58"]]'),
            ("Watch me. Someone worked out 58 take away 23 and got 35. Add the "
             "answer back: 35 plus 23 equals 58. That is exactly where we started, "
             "so the take away was right.",
             '[[step eq="35 + 23 = 58 ✓ back where we started"]]'),
            ("Here is the trap. Add the ANSWER to the number you took away. Do not "
             "add the two numbers from the question. In 58 take away 23, the check "
             "is 35 plus 23, not 58 plus 23.",
             '[[step eq="35 + 23 = 58 ✓"]]'
             '[[step eq="81 ✗ that is 58 + 23, the wrong pair"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 74 take away 31 gave 43. "
                        "Check it: 43 plus 31 equals 74. Back where we started.",
                        '[[step eq="43 + 31 = 74"]]'),
             "ask": {"a": 66, "b": 24, "op": "chk"}},
            {"worked": ("One more together. 92 take away 47 gave 45. Check it: 45 "
                        "plus 47 equals 92.",
                        '[[step eq="45 + 47 = 92"]]'),
             "ask": {"a": 83, "b": 39, "op": "chk"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": 20, "b": 10, "op": "chk"}, {"a": 41, "b": 30, "op": "chk"}, {"a": 53, "b": 32, "op": "chk"}, {"a": 62, "b": 49, "op": "chk"}, {"a": 70, "b": 45, "op": "chk"}, {"a": 77, "b": 43, "op": "chk"}, {"a": 83, "b": 66, "op": "chk"}, {"a": 89, "b": 53, "op": "chk"}, {"a": 94, "b": 88, "op": "chk"}, {"a": 99, "b": 98, "op": "chk"}],
    },
    {
        "id": "entry-u7-dimes-and-pennies", "course": "entry", "unit": 7,
        "topic": "Counting dimes and pennies", "op": "m", "max_value": 99,
        "levels": ("abstract",), "symbols": ("dime", "cent"),
        "advance_line": "Three in a row — you've got it! You can count dimes and pennies.",
        "teach": [
            ("You can count nickels by five. A penny is one cent, and a dime is "
             "worth 10 cents. Dimes are counted by ten, and counting by ten is "
             "the easiest count there is.",
             '[[goal text="Dimes and pennies"]]'
             '[[step eq="1 dime = 10 cents"]]'),
            ("Watch me count 3 dimes and 4 pennies. Dimes first, count by ten: 10, "
             "20, 30. Then the pennies, counting on: 31, 32, 33, 34. That is 34 "
             "cents.",
             '[[step eq="3 dimes = 30 cents"]]'
             '[[step eq="30 + 4 pennies = 34 cents"]]'),
            ("Here is the trap. Do not count a dime as one. It is one coin, but it "
             "is worth ten cents. Count the coins that are worth more first, then "
             "count the pennies on the end.",
             '[[step eq="3 dimes 4 pennies = 34 cents ✓"]]'
             '[[step eq="7 ✗ that is the coins counted, not the cents"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 2 dimes and 5 pennies. By "
                        "ten: 10, 20. Then on: 21, 22, 23, 24, 25. That is 25 cents.",
                        '[[step eq="2 dimes + 5 pennies = 25 cents"]]'),
             "ask": {"a": 4, "b": 3, "op": "m"}},
            {"worked": ("One more together. 5 dimes and 2 pennies. By ten: 10, 20, "
                        "30, 40, 50. Then 51, 52. That is 52 cents.",
                        '[[step eq="5 dimes + 2 pennies = 52 cents"]]'),
             "ask": {"a": 6, "b": 8, "op": "m"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": 1, "b": 1, "op": "m"}, {"a": 2, "b": 1, "op": "m"}, {"a": 3, "b": 1, "op": "m"}, {"a": 4, "b": 1, "op": "m"}, {"a": 5, "b": 1, "op": "m"}, {"a": 5, "b": 9, "op": "m"}, {"a": 6, "b": 9, "op": "m"}, {"a": 7, "b": 9, "op": "m"}, {"a": 8, "b": 9, "op": "m"}, {"a": 9, "b": 9, "op": "m"}],
    },
    {
        "id": "entry-u7-quarters", "course": "entry", "unit": 7,
        "topic": "Counting quarters", "op": "qtr", "max_value": 109,
        "levels": ("abstract",), "symbols": ("quarter",),
        "advance_line": "Three in a row — you've got it! You can count quarters.",
        "teach": [
            ("A quarter is worth 25 cents. It is the biggest coin you will count "
             "here, and four of them make one dollar, which is 100 cents.",
             '[[goal text="Quarters"]]'
             '[[step eq="1 quarter = 25 cents"]]'),
            ("Watch me count 3 quarters and 4 pennies. Quarters first, counting by "
             "twenty-five: 25, 50, 75. Then the pennies on the end: 76, 77, 78, "
             "79. That is 79 cents.",
             '[[step eq="3 quarters = 75 cents"]]'
             '[[step eq="75 + 4 pennies = 79 cents"]]'),
            ("Here is the trap. Two quarters is 50 cents, not 2 cents and not 20 "
             "cents. Count quarters in jumps of twenty-five, and say each jump out "
             "loud: twenty-five, fifty, seventy-five, one hundred.",
             '[[step eq="25, 50, 75, 100 — the four quarters"]]'
             '[[step eq="3 quarters 4 pennies = 79 cents ✓"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 2 quarters and 3 pennies. "
                        "25, 50. Then 51, 52, 53. That is 53 cents.",
                        '[[step eq="2 quarters + 3 pennies = 53 cents"]]'),
             "ask": {"a": 1, "b": 6, "op": "qtr"}},
            {"worked": ("One more together. 4 quarters and 2 pennies. 25, 50, 75, "
                        "100. Then 101, 102. That is 102 cents.",
                        '[[step eq="4 quarters + 2 pennies = 102 cents"]]'),
             "ask": {"a": 3, "b": 5, "op": "qtr"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": 1, "b": 1, "op": "qtr"}, {"a": 1, "b": 5, "op": "qtr"}, {"a": 1, "b": 9, "op": "qtr"}, {"a": 2, "b": 4, "op": "qtr"}, {"a": 2, "b": 8, "op": "qtr"}, {"a": 3, "b": 2, "op": "qtr"}, {"a": 3, "b": 6, "op": "qtr"}, {"a": 4, "b": 1, "op": "qtr"}, {"a": 4, "b": 5, "op": "qtr"}, {"a": 4, "b": 9, "op": "qtr"}],
    },
    {
        "id": "entry-u7-making-change", "course": "entry", "unit": 7,
        "topic": "Making change", "op": "chg", "max_value": 100,
        "levels": ("abstract",), "symbols": ("change",),
        "advance_line": "Three in a row — you've got it! You can work out the change.",
        "teach": [
            ("When you pay with more than a thing costs, you get change. Change is "
             "what is left of your money after the price has been taken away.",
             '[[goal text="Making change"]]'
             '[[step eq="you pay 50 − it costs 35 = ? change"]]'),
            ("Watch me. A toy costs 35 cents and you pay 50 cents. Take the price "
             "away from what you paid: 50 take away 35 equals 15. Your change is "
             "15 cents.",
             '[[step eq="50 − 35 = 15 cents change"]]'),
            ("Here is the trap. Do not add the two amounts. You are not spending "
             "85 cents. The change is always SMALLER than what you handed over, so "
             "if your answer is bigger, something has gone wrong.",
             '[[step eq="50 − 35 = 15 ✓"]]'
             '[[step eq="85 ✗ that is the two amounts added"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. A sticker costs 18 cents "
                        "and you pay 25 cents. 25 take away 18 equals 7 cents "
                        "change.",
                        '[[step eq="25 − 18 = 7 cents change"]]'),
             "ask": {"a": 50, "b": 20, "op": "chg"}},
            {"worked": ("One more together. A pencil costs 60 cents and you pay "
                        "100 cents. 100 take away 60 equals 40 cents change.",
                        '[[step eq="100 − 60 = 40 cents change"]]'),
             "ask": {"a": 100, "b": 45, "op": "chg"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": 25, "b": 24, "op": "chg"}, {"a": 25, "b": 18, "op": "chg"}, {"a": 100, "b": 88, "op": "chg"}, {"a": 100, "b": 82, "op": "chg"}, {"a": 100, "b": 74, "op": "chg"}, {"a": 50, "b": 15, "op": "chg"}, {"a": 50, "b": 6, "op": "chg"}, {"a": 100, "b": 40, "op": "chg"}, {"a": 100, "b": 23, "op": "chg"}, {"a": 100, "b": 5, "op": "chg"}],
    },
    {
        "id": "entry-u4-hundreds-tens-and-ones", "course": "entry", "unit": 4,
        "topic": "Hundreds, tens and ones", "op": "pv", "max_value": 999,
        "levels": ("abstract",), "symbols": ("hundred", "digit"),
        "advance_line": "Three in a row — you've got it! You can read hundreds, tens and ones.",
        "teach": [
            ("You already know tens and ones. Ten tens, put together, make one "
             "hundred. A three-digit number has a hundreds digit, a tens digit and "
             "a ones digit, always in that order.",
             '[[goal text="Hundreds, tens and ones"]]'
             '[[step eq="3 hundreds, 4 tens, 6 ones = 346"]]'),
            ("Watch me. 3 hundreds, 4 tens and 6 ones. Say the hundreds first: "
             "three hundred. Then the tens and ones: forty-six. Three hundred "
             "forty-six.",
             '[[step eq="300 + 40 + 6 = 346"]]'),
            ("Here is the trap. Say the digits in order, left to right. 3 hundreds "
             "and 4 tens is 340, not 430. The first digit you say is the biggest "
             "one, because hundreds are bigger than tens.",
             '[[step eq="3 hundreds, 4 tens, 6 ones = 346 ✓"]]'
             '[[step eq="643 ✗ the digits were read backwards"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 2 hundreds, 5 tens and 1 "
                        "one. Two hundred, then fifty-one. Two hundred fifty-one.",
                        '[[step eq="200 + 50 + 1 = 251"]]'),
             "ask": {"a": 4, "b": 2, "c": 7, "op": "pv"}},
            {"worked": ("One more together. 6 hundreds, 0 tens and 3 ones is six "
                        "hundred three.",
                        '[[step eq="600 + 0 + 3 = 603"]]'),
             "ask": {"a": 5, "b": 8, "c": 2, "op": "pv"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": 1, "b": 1, "c": 1, "op": "pv"}, {"a": 2, "b": 1, "c": 1, "op": "pv"}, {"a": 3, "b": 1, "c": 1, "op": "pv"}, {"a": 4, "b": 1, "c": 1, "op": "pv"}, {"a": 5, "b": 1, "c": 1, "op": "pv"}, {"a": 5, "b": 9, "c": 9, "op": "pv"}, {"a": 6, "b": 9, "c": 9, "op": "pv"}, {"a": 7, "b": 9, "c": 9, "op": "pv"}, {"a": 8, "b": 9, "c": 9, "op": "pv"}, {"a": 9, "b": 9, "c": 9, "op": "pv"}],
    },
    {
        "id": "entry-u4-ten-more", "course": "entry", "unit": 4,
        "topic": "Ten more", "op": "t10", "max_value": 99,
        "levels": ("abstract",), "symbols": ("tens digit",),
        "advance_line": "Three in a row — you've got it! You can add ten in your head.",
        "teach": [
            ("Adding ten is the easiest jump there is, once you see what it does. "
             "Ten more does not touch the ones at all. Only the tens digit goes up "
             "by one.",
             '[[goal text="Ten more"]]'
             '[[step eq="34 + 10 = 44"]]'),
            ("Watch me. Ten more than 34. The 4 ones stay 4 ones. The 3 tens "
             "become 4 tens. So ten more than 34 is 44. You did not have to count "
             "at all.",
             '[[step eq="3 tens 4 ones → 4 tens 4 ones"]]'
             '[[step eq="34 + 10 = 44"]]'),
            ("Here is the trap. Adding ten is not adding one. Ten more than 57 is "
             "67, not 58. Check your answer by looking at the ones digit: it "
             "should be exactly the same as the one you started with.",
             '[[step eq="57 + 10 = 67 ✓ the 7 did not move"]]'
             '[[step eq="58 ✗ that is one more, not ten more"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Ten more than 25. The 5 "
                        "stays. The 2 tens become 3 tens. 35.",
                        '[[step eq="25 + 10 = 35"]]'),
             "ask": {"a": 42, "b": 0, "op": "t10"}},
            {"worked": ("One more together. Ten more than 63 is 73.",
                        '[[step eq="63 + 10 = 73"]]'),
             "ask": {"a": 78, "b": 0, "op": "t10"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": 10, "b": 0, "op": "t10"}, {"a": 19, "b": 0, "op": "t10"}, {"a": 28, "b": 0, "op": "t10"}, {"a": 36, "b": 0, "op": "t10"}, {"a": 45, "b": 0, "op": "t10"}, {"a": 54, "b": 0, "op": "t10"}, {"a": 66, "b": 0, "op": "t10"}, {"a": 71, "b": 0, "op": "t10"}, {"a": 80, "b": 0, "op": "t10"}, {"a": 89, "b": 0, "op": "t10"}],
    },
    {
        "id": "entry-u4-what-a-digit-is-worth", "course": "entry", "unit": 4,
        "topic": "What a digit is worth", "op": "wor", "max_value": 999,
        "levels": ("abstract",), "symbols": ("place", "worth"),
        "advance_line": "Three in a row — you've got it! You know what each digit is worth.",
        "teach": [
            ("A digit is worth different amounts depending on where it sits. The "
             "same 7 can be worth 7, or 70, or 700. Its place is what decides.",
             '[[goal text="What a digit is worth"]]'
             '[[step eq="7 · 70 · 700 — the same digit, three places"]]'),
            ("Watch me. In the number 374, what is the 7 worth? Count the places "
             "from the right: 4 is ones, 7 is tens, 3 is hundreds. The 7 sits in "
             "the tens place, so it is worth 70.",
             '[[step eq="374 → 3 hundreds, 7 tens, 4 ones"]]'
             '[[step eq="the 7 is worth 70"]]'),
            ("Here is the trap. Do not answer with the digit by itself. In 374 the "
             "7 is not worth 7. Find its place first, then say the whole amount "
             "that place is worth.",
             '[[step eq="the 7 in 374 is worth 70 ✓"]]'
             '[[step eq="7 ✗ that is the digit, not what it is worth"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. In 258, what is the 5 "
                        "worth? 8 is ones, 5 is tens. The 5 is worth 50.",
                        '[[step eq="258 → the 5 is worth 50"]]'),
             "ask": {"a": 4, "b": 6, "c": 1, "op": "wor"}},
            {"worked": ("One more together. In 931, the 3 sits in the tens place, "
                        "so it is worth 30.",
                        '[[step eq="931 → the 3 is worth 30"]]'),
             "ask": {"a": 7, "b": 2, "c": 5, "op": "wor"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": 1, "b": 2, "c": 1, "op": "wor"}, {"a": 9, "b": 2, "c": 3, "op": "wor"}, {"a": 8, "b": 3, "c": 4, "op": "wor"}, {"a": 7, "b": 4, "c": 3, "op": "wor"}, {"a": 6, "b": 5, "c": 4, "op": "wor"}, {"a": 4, "b": 6, "c": 5, "op": "wor"}, {"a": 3, "b": 7, "c": 6, "op": "wor"}, {"a": 2, "b": 8, "c": 6, "op": "wor"}, {"a": 1, "b": 9, "c": 7, "op": "wor"}, {"a": 8, "b": 9, "c": 8, "op": "wor"}],
    },
    {
        "id": "entry-u5-adding-three-digit-numbers", "course": "entry", "unit": 5,
        "topic": "Adding three-digit numbers", "op": "a3d", "max_value": 999,
        "levels": ("abstract",), "symbols": ("column",),
        "advance_line": "Three in a row — you've got it! You can add three-digit numbers.",
        "teach": [
            ("Three-digit numbers add the same way two-digit ones do. Work one "
             "column at a time, and always start on the right. Ones first, then "
             "tens, then hundreds.",
             '[[goal text="Adding three-digit numbers"]]'
             '[[step eq="243 + 125 = ?"]]'),
            ("Watch me add 243 plus 125. Ones: 3 plus 5 equals 8. Tens: 4 plus 2 "
             "equals 6. Hundreds: 2 plus 1 equals 3. So 243 plus 125 equals 368.",
             '[[step eq="ones: 3 + 5 = 8"]]'
             '[[step eq="tens: 4 + 2 = 6"]]'
             '[[step eq="hundreds: 2 + 1 = 3"]]'
             '[[step eq="243 + 125 = 368"]]'),
            ("Here is the trap. Keep each column in its own place. The tens answer "
             "goes under the tens, and the hundreds answer under the hundreds. If "
             "a column slides across, every digit after it is wrong.",
             '[[step eq="243 + 125 = 368 ✓"]]'
             '[[step eq="638 ✗ the columns were written in the wrong places"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 312 plus 246. Ones: 2 "
                        "plus 6 equals 8. Tens: 1 plus 4 equals 5. Hundreds: 3 "
                        "plus 2 equals 5. That is 558.",
                        '[[step eq="312 + 246 = 558"]]'),
             "ask": {"a": 425, "b": 132, "op": "a3d"}},
            {"worked": ("One more together. 507 plus 281. Ones: 7 plus 1 equals 8. "
                        "Tens: 0 plus 8 equals 8. Hundreds: 5 plus 2 equals 7. "
                        "That is 788.",
                        '[[step eq="507 + 281 = 788"]]'),
             "ask": {"a": 634, "b": 145, "op": "a3d"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": 100, "b": 100, "op": "a3d"}, {"a": 156, "b": 301, "op": "a3d"}, {"a": 330, "b": 239, "op": "a3d"}, {"a": 321, "b": 342, "op": "a3d"}, {"a": 601, "b": 137, "op": "a3d"}, {"a": 411, "b": 381, "op": "a3d"}, {"a": 702, "b": 163, "op": "a3d"}, {"a": 799, "b": 100, "op": "a3d"}, {"a": 559, "b": 410, "op": "a3d"}, {"a": 899, "b": 100, "op": "a3d"}],
    },
    {
        "id": "entry-u5-crossing-a-hundred", "course": "entry", "unit": 5,
        "topic": "Crossing a hundred", "op": "c2h", "max_value": 199,
        "levels": ("abstract",), "symbols": ("hundred",),
        "advance_line": "Three in a row — you've got it! You can add past one hundred.",
        "teach": [
            ("You already carry into the tens. Today the tens themselves fill up. "
             "When ten tens are made, they become one hundred, and a new digit "
             "appears at the front.",
             '[[goal text="Crossing a hundred"]]'
             '[[step eq="68 + 47 = ?"]]'),
            ("Watch me add 68 plus 47. Ones: 8 plus 7 equals 15 — over nine, write "
             "the 5 and carry one ten. Tens: 6 plus 4 equals 10, plus the carried "
             "one is 11 tens. Eleven tens is one hundred and one ten. So 115.",
             '[[step eq="ones: 8 + 7 = 15, carry 1"]]'
             '[[step eq="tens: 6 + 4 + 1 = 11 tens"]]'
             '[[step eq="68 + 47 = 115"]]'),
            ("Here is the trap. Eleven tens is not written as 11 in the tens "
             "place. Ten of those tens become one hundred, so the 1 moves to the "
             "front and one ten stays behind.",
             '[[step eq="68 + 47 = 115 ✓"]]'
             '[[step eq="1115 ✗ eleven tens written where one ten belongs"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 75 plus 38. Ones: 5 plus "
                        "8 equals 13 — write the 3, carry one. Tens: 7 plus 3 plus "
                        "the carried one is 11 tens. That is 113.",
                        '[[step eq="75 + 38 = 113"]]'),
             "ask": {"a": 56, "b": 67, "op": "c2h"}},
            {"worked": ("One more together. 84 plus 29. Ones: 4 plus 9 equals 13 — "
                        "write the 3, carry one. Tens: 8 plus 2 plus one is 11 "
                        "tens. That is 113.",
                        '[[step eq="84 + 29 = 113"]]'),
             "ask": {"a": 47, "b": 76, "op": "c2h"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": 10, "b": 90, "op": "c2h"}, {"a": 49, "b": 57, "op": "c2h"}, {"a": 61, "b": 51, "op": "c2h"}, {"a": 20, "b": 99, "op": "c2h"}, {"a": 28, "b": 98, "op": "c2h"}, {"a": 84, "b": 49, "op": "c2h"}, {"a": 75, "b": 67, "op": "c2h"}, {"a": 54, "b": 99, "op": "c2h"}, {"a": 87, "b": 79, "op": "c2h"}, {"a": 99, "b": 99, "op": "c2h"}],
    },
    {
        # (tb, 2026-09-05) TO THE SHAPE: a why, the stars counted past ten as the
        # picture (the count-on trick shown, not told), the rule, a recap. Ruling ⑤:
        # quick praise for counting; no reason question for pre-readers (open ruling).
        "id": "entry-u1-counting-past-ten", "course": "entry", "unit": 1,
        "topic": "Counting past ten", "op": "c20", "max_value": 20,
        "levels": ("concrete",), "symbols": ("count",),
        "advance_line": "Three in a row — you've got it! You can count past ten.",
        "why": [
            ("Why count past ten? Because most things come in more than ten. "
             "The crayons in a box, the steps to your door, the days until a "
             "birthday. Ten fingers run out fast, and the numbers keep going.",
             '[[goal text="Counting past ten"]]'),
        ],
        "picture": [
            ("Here are more than ten stars. Watch them light up. One, two, three, "
             "four, five, six, seven, eight, nine, ten — and counting does not "
             "stop. Eleven, twelve. Twelve stars.",
             '[[objects emoji="⭐" groups="12" count="1" caption="ten, then eleven, twelve"]]'),
        ],
        "teach": [
            ("That is counting past ten. After ten comes eleven, twelve, "
             "thirteen, and it keeps going. Say each number as you touch each "
             "star, and the last number you say is how many.",
             '[[objects emoji="⭐" groups="12" caption="touch each one and count"]]'),
            # (se, 2026-09-02) JIM'S FLAG: "Drop the term 'trap' and everything
            # after it." The warning sentence is gone; the line now ends on the
            # count itself. (The 40-odd "Here is the trap" lines in OTHER courses
            # are the house pattern and are deliberately untouched -- his flag was
            # this entry-course line; a wider ruling is his to make.)
            ("Here is a faster way. Count the first ten, then count on from ten. "
             "Ten — eleven, twelve, thirteen, fourteen. Fourteen stars.",
             '[[objects emoji="⭐" groups="14" caption="ten, then count on: 11, 12, 13, 14"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Ten, then count on: "
                        "eleven, twelve, thirteen. Thirteen stars.",
                        '[[objects emoji="⭐" groups="13" caption="thirteen stars"]]'),
             "ask": {"a": 19, "b": 0, "op": "c20"}},
            {"worked": ("One more together. Ten, then eleven, twelve, thirteen, "
                        "fourteen, fifteen, sixteen. Sixteen stars.",
                        '[[objects emoji="⭐" groups="16" caption="sixteen stars"]]'),
             "ask": {"a": 20, "b": 0, "op": "c20"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "recap": [
            ("So, here it is again. Counting does not stop at ten — eleven, "
             "twelve, thirteen, and on it goes. Count the first ten, then count "
             "on, and the last number you say is how many.",
             '[[objects emoji="⭐" groups="13" caption="ten, then count on: 11, 12, 13"]]'),
            ("And that is how you count anything that comes in more than ten.",
             '[[goal text="Counting past ten"]]'),
        ],
        # the whole pool is eleven to twenty, so the two worked pairs take the
        # last two and the bank takes the rest -- a problem may never be both.
        "bank": [{"a": 11, "b": 0, "op": "c20"}, {"a": 12, "b": 0, "op": "c20"}, {"a": 13, "b": 0, "op": "c20"}, {"a": 14, "b": 0, "op": "c20"}, {"a": 15, "b": 0, "op": "c20"}, {"a": 16, "b": 0, "op": "c20"}, {"a": 17, "b": 0, "op": "c20"}, {"a": 18, "b": 0, "op": "c20"}],
    },
    {
        # (tb, 2026-09-05) TO THE SHAPE on the NUMBER LINE: the two numbers as dots,
        # the later one is the bigger one. The ask now draws the line too (the
        # picture IS the comparing method, like the array is for equal groups); the
        # trap line is kept. Ruling ⑤: quick praise for comparing; no reason question
        # for pre-readers (open ruling).
        "id": "entry-u1-which-is-bigger", "course": "entry", "unit": 1,
        "topic": "Which number is bigger", "op": "big", "max_value": 20,
        "levels": ("abstract",), "symbols": ("bigger",),
        "advance_line": "Three in a row — you've got it! You can tell which number is bigger.",
        "why": [
            ("Why tell which number is bigger? Because you compare all day. Who "
             "has more stickers, which pile of blocks is taller, who is older. "
             "Two numbers, and you want to know which one is more.",
             '[[goal text="Which number is bigger"]]'),
        ],
        "picture": [
            ("Here are the numbers in their line, with 3 and 8 marked. Count "
             "along from one. You reach 3 first — and you have to keep counting "
             "to reach 8. The number you reach later is the bigger one. 8 is "
             "bigger than 3.",
             '[[numberline min="1" max="10" points="3,8" caption="you reach 8 later — 8 is bigger"]]'),
        ],
        "teach": [
            ("That is the rule. Numbers stand in a line, and the further along a "
             "number stands, the bigger it is. So the bigger number is the one "
             "you reach later when you count.",
             '[[numberline min="1" max="10" points="3,8" caption="8 comes later than 3"]]'
             '[[step eq="8 is bigger than 3"]]'),
            ("Here is the trap. Do not add the two numbers. The question is not "
             "how many in all. It only asks which one is bigger, so your "
             "answer is always one of the two numbers you were given.",
             '[[step eq="3 or 8 → 8 ✓"]]'
             '[[step eq="11 ✗ that is 3 and 8 added, not the bigger one"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Which is bigger, 6 or 9? "
                        "You reach 9 later when you count, so 9 is bigger.",
                        '[[numberline min="1" max="10" points="6,9" caption="9 comes later"]]'),
             "ask": {"a": 6, "b": 13, "op": "big"}},
            {"worked": ("One more together. Which is bigger, 12 or 7? You reach 12 "
                        "later, so 12 is bigger.",
                        '[[numberline min="1" max="20" points="7,12" caption="12 comes later"]]'
                        '[[step eq="12 or 7 → 12"]]'),
             "ask": {"a": 17, "b": 9, "op": "big"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "recap": [
            ("So, here it is again. Numbers stand in a line, and the bigger "
             "number is the one you reach later when you count. Not the two "
             "added up — just the one that comes later.",
             '[[numberline min="1" max="10" points="3,8" caption="you reach 8 later — 8 is bigger"]]'),
            ("And that is how you tell who has more.",
             '[[step eq="3 or 8 → 8"]]'),
        ],
        "bank": [{"a": 1, "b": 2, "op": "big"}, {"a": 3, "b": 6, "op": "big"}, {"a": 5, "b": 10, "op": "big"}, {"a": 7, "b": 14, "op": "big"}, {"a": 9, "b": 18, "op": "big"}, {"a": 12, "b": 3, "op": "big"}, {"a": 14, "b": 7, "op": "big"}, {"a": 16, "b": 11, "op": "big"}, {"a": 18, "b": 15, "op": "big"}, {"a": 20, "b": 19, "op": "big"}],
    },
    {
        "id": "entry-u2-doubles", "course": "entry", "unit": 2,
        "topic": "Doubles", "op": "dbe", "max_value": 20,
        "levels": ("abstract",), "symbols": ("double",),
        "advance_line": "Three in a row — you've got it! You know your doubles.",
        "teach": [
            ("A double is a number added to itself. Four plus four is a double. "
             "Doubles are worth knowing by heart, because they come up everywhere "
             "and they are quick.",
             '[[goal text="Doubles"]]'
             '[[step eq="4 + 4 = 8"]]'),
            ("Watch me. 6 plus 6. Count six, then six more: seven, eight, nine, "
             "ten, eleven, twelve. 6 plus 6 equals 12. Say it twice and you will "
             "remember it.",
             '[[objects emoji="⭐" groups="12" count="1" caption="six and six more"]]'
             '[[step eq="6 + 6 = 12"]]'),
            ("Here is the trap. A double adds the SAME number again. It does not "
             "add one more. 7 plus 7 is 14, not 15. Look at the number you were "
             "given, and use that same number twice.",
             '[[step eq="7 + 7 = 14 ✓"]]'
             '[[step eq="15 ✗ that is 7 + 8, not a double"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 5 plus 5. Five, then five "
                        "more: six, seven, eight, nine, ten. 5 plus 5 equals 10.",
                        '[[step eq="5 + 5 = 10"]]'),
             "ask": {"a": 9, "b": 0, "op": "dbe"}},
            {"worked": ("One more together. 9 plus 9 equals 18.",
                        '[[step eq="9 + 9 = 18"]]'),
             "ask": {"a": 10, "b": 0, "op": "dbe"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": 1, "b": 0, "op": "dbe"}, {"a": 2, "b": 0, "op": "dbe"}, {"a": 3, "b": 0, "op": "dbe"}, {"a": 4, "b": 0, "op": "dbe"}, {"a": 5, "b": 0, "op": "dbe"}, {"a": 6, "b": 0, "op": "dbe"}, {"a": 7, "b": 0, "op": "dbe"}, {"a": 8, "b": 0, "op": "dbe"}],
    },
    {
        "id": "entry-u2-adding-three-numbers", "course": "entry", "unit": 2,
        "topic": "Adding three numbers", "op": "add3", "max_value": 20,
        "levels": ("abstract",), "symbols": ("plus",),
        "advance_line": "Three in a row — you've got it! You can add three numbers.",
        "teach": [
            ("Sometimes there are three numbers to add, not two. You do not need a "
             "new trick. Add the first two, then add the third to what you got.",
             '[[goal text="Adding three numbers"]]'
             '[[step eq="2 + 3 + 4 = ?"]]'),
            ("Watch me. 2 plus 3 plus 4. First 2 plus 3 equals 5. Then 5 plus 4 "
             "equals 9. So 2 plus 3 plus 4 equals 9.",
             '[[step eq="2 + 3 = 5"]]'
             '[[step eq="5 + 4 = 9"]]'),
            ("Here is a helpful trick, and here is the trap. The trap is stopping "
             "after two numbers and forgetting the third. The trick is to look for "
             "two that make ten first: in 6 plus 4 plus 3, do 6 plus 4 to get "
             "ten, then 10 plus 3 is 13.",
             '[[step eq="6 + 4 = 10, then 10 + 3 = 13 ✓"]]'
             '[[step eq="10 ✗ the third number was left out"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 3 plus 5 plus 2. First 3 "
                        "plus 5 equals 8. Then 8 plus 2 equals 10.",
                        '[[step eq="3 + 5 + 2 = 10"]]'),
             "ask": {"a": 2, "b": 4, "c": 6, "op": "add3"}},
            {"worked": ("One more together. 1 plus 6 plus 6. First 1 plus 6 equals "
                        "7. Then 7 plus 6 equals 13.",
                        '[[step eq="1 + 6 + 6 = 13"]]'),
             "ask": {"a": 7, "b": 5, "c": 3, "op": "add3"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": 1, "b": 1, "c": 1, "op": "add3"}, {"a": 1, "b": 3, "c": 5, "op": "add3"}, {"a": 3, "b": 7, "c": 1, "op": "add3"}, {"a": 9, "b": 1, "c": 2, "op": "add3"}, {"a": 2, "b": 9, "c": 3, "op": "add3"}, {"a": 4, "b": 8, "c": 3, "op": "add3"}, {"a": 6, "b": 5, "c": 5, "op": "add3"}, {"a": 8, "b": 5, "c": 4, "op": "add3"}, {"a": 4, "b": 8, "c": 7, "op": "add3"}, {"a": 9, "b": 9, "c": 2, "op": "add3"}],
    },
    {
        "id": "entry-u3-the-missing-part", "course": "entry", "unit": 3,
        "topic": "The missing part", "op": "msp", "max_value": 20,
        "levels": ("abstract",), "symbols": ("more",),
        "advance_line": "Three in a row — you've got it! You can find the missing part.",
        "teach": [
            ("Some questions give you the start and the finish and hide the middle. "
             "7 and how many more make 10? The missing number is the part that has "
             "been left out.",
             '[[goal text="The missing part"]]'
             '[[step eq="7 + ? = 10"]]'),
            ("Watch me. 7 and how many more make 10? Start at seven and count up "
             "to ten: eight, nine, ten. That is three counts. So 7 and 3 more "
             "make 10.",
             '[[numberline min="0" max="10" hops="7,10" caption="count up from 7 to 10"]]'
             '[[step eq="7 + 3 = 10"]]'),
            ("Here is the trap. Do not answer with the finish. The question is not "
             "what number we end on. It asks how many MORE, so your answer is the "
             "size of the jump, never the number you landed on.",
             '[[step eq="7 + 3 = 10 ✓ the jump is 3"]]'
             '[[step eq="10 ✗ that is where we finished, not how many more"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 4 and how many more make "
                        "9? Count up from four: five, six, seven, eight, nine. "
                        "Five counts. 4 and 5 more make 9.",
                        '[[step eq="4 + 5 = 9"]]'),
             "ask": {"a": 5, "b": 11, "op": "msp"}},
            {"worked": ("One more together. 8 and how many more make 15? Count up "
                        "from eight to fifteen — seven counts. 8 and 7 more make 15.",
                        '[[step eq="8 + 7 = 15"]]'),
             "ask": {"a": 9, "b": 17, "op": "msp"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": 1, "b": 2, "op": "msp"}, {"a": 3, "b": 5, "op": "msp"}, {"a": 6, "b": 9, "op": "msp"}, {"a": 10, "b": 14, "op": "msp"}, {"a": 15, "b": 20, "op": "msp"}, {"a": 7, "b": 14, "op": "msp"}, {"a": 3, "b": 12, "op": "msp"}, {"a": 3, "b": 14, "op": "msp"}, {"a": 7, "b": 20, "op": "msp"}, {"a": 1, "b": 20, "op": "msp"}],
    },
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
    # ------------------------- BUILD kd: the content sweep -------------------------
    {
        # (tb, 2026-09-05) TO THE SHAPE, for the youngest students: a why in their
        # world, the stars counted one at a time as the picture, the rule read off
        # it, a recap. No walk-back and no reason question -- ruling ⑤ keeps the
        # quick praise for counting, and a reason question's options are text a
        # student who is learning to count to ten cannot yet read (open ruling).
        "id": "entry-u1-counting-to-10", "course": "entry", "unit": 1,
        "topic": "Counting to 10",
        "op": "cnt", "max_value": 10,
        "levels": ("concrete",),   # the picture IS the problem; there is no
                                   # abstract form of "count these stars"
        "symbols": ("count",),
        "advance_line": ("Three in a row — you've got it! "
                         "You can count to ten."),
        "why": [
            ("Why count? Because counting tells you how many. How many cookies "
             "are left, how many friends are coming, how many fingers you are "
             "holding up. When you can count, you always know how many.",
             '[[goal text="Counting to 10"]]'),
        ],
        "picture": [
            ("Here are some stars. Watch them light up one at a time, and say a "
             "number for each one. One, two, three, four, five. The last number "
             "you say tells you how many. Five stars.",
             '[[objects emoji="⭐" groups="5" count="1" caption="one number for each star — five stars"]]'),
        ],
        "teach": [
            ("That is how counting works. Point to each star and say one number "
             "for it: one, two, three. Never skip a star, and never count one "
             "twice. The last number you say is how many there are.",
             '[[objects emoji="⭐" groups="3" count="1" caption="one, two, three — three stars"]]'),
            ("Watch me count again, a bigger group this time. One, two, three, "
             "four, five, six, seven. Seven stars.",
             '[[objects emoji="⭐" groups="7" count="1" caption="count them one at a time"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. One, two, three, four. "
                        "Four stars.",
                        '[[objects emoji="⭐" groups="4" count="1" caption="count them one at a time"]]'),
             "ask": {"a": 2, "b": 0, "op": "cnt"}},
            {"worked": ("One more together. One, two, three, four, five, six. "
                        "Six stars.",
                        '[[objects emoji="⭐" groups="6" count="1" caption="count them one at a time"]]'),
             "ask": {"a": 4, "b": 0, "op": "cnt"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "recap": [
            ("So, here it is again. To count, point to each star and say one "
             "number for it, and the last number you say is how many. One, two, "
             "three, four. Four stars.",
             '[[objects emoji="⭐" groups="4" count="1" caption="the last number you say is how many"]]'),
            ("And counting is how you always know how many there are.",
             '[[goal text="Counting to 10"]]'),
        ],
        "bank": [
            {"a": 1, "b": 0, "op": "cnt"}, {"a": 3, "b": 0, "op": "cnt"},
            {"a": 5, "b": 0, "op": "cnt"}, {"a": 6, "b": 0, "op": "cnt"},
            {"a": 7, "b": 0, "op": "cnt"}, {"a": 8, "b": 0, "op": "cnt"},
            {"a": 9, "b": 0, "op": "cnt"}, {"a": 10, "b": 0, "op": "cnt"},
        ],
    },
    {
        # (tb, 2026-09-05) TO THE SHAPE on the NUMBER LINE: numbers stand in a line,
        # and "right after" is one hop up, "right before" one hop back. The asks
        # stay bare (a labelled line would read the answer off); ruling ⑤ keeps the
        # quick praise for a one-hop fact; no reason question (pre-readers, open ruling).
        "id": "entry-u1-numbers-before-and-after", "course": "entry", "unit": 1,
        "topic": "Numbers before and after",
        "op": "aft", "max_value": 20,
        "levels": ("abstract",),
        "symbols": ("after", "before"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can find the number before and the number after."),
        "why": [
            ("Why learn what comes before and after? Because numbers always stand "
             "in the same order, like friends in a line. If you know who stands "
             "next to who, you can count on from any number instead of starting "
             "at one every time.",
             '[[goal text="Numbers before and after"]]'),
        ],
        "picture": [
            ("Here are the numbers standing in their line. Find 5. Take one hop "
             "up the line and you land on 6 — so 6 comes right after 5. Now find "
             "6 and take one hop back: you land on 5 — so 5 comes right before 6.",
             '[[numberline min="1" max="10" points="5" hops="5,6" caption="one hop up: 6 comes right after 5"]]'),
        ],
        "teach": [
            ("That is the whole idea. The number right after is one hop up the "
             "line — count up one. The number right before is one hop back — "
             "count back one.",
             '[[numberline min="1" max="10" points="6" hops="6,5" caption="one hop back: 5 comes right before 6"]]'),
            ("Watch me. What comes right after 9? Find 9, hop up one, and you "
             "land on 10. 10 comes right after 9.",
             '[[numberline min="1" max="10" points="9" hops="9,10" caption="9, then 10"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Right after 6 comes 7 — "
                        "one hop up.",
                        '[[numberline min="1" max="10" points="6" hops="6,7" caption="6, 7"]]'),
             "ask": {"a": 4, "b": 0, "op": "aft"}},
            {"worked": ("One more together. Right before 10 comes 9 — one hop back.",
                        '[[numberline min="1" max="10" points="10" hops="10,9" caption="9, 10"]]'),
             "ask": {"a": 7, "b": 0, "op": "bef"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "recap": [
            ("So, here it is again. Numbers stand in a line in the same order "
             "every time. The number right after is one hop up; the number right "
             "before is one hop back.",
             '[[numberline min="1" max="10" points="5" hops="5,6" caption="one hop up: right after"]]'),
            ("And knowing who stands next to who lets you count on from any "
             "number.",
             '[[step eq="4, 5, 6"]]'),
        ],
        "bank": [
            {"a": 2, "b": 0, "op": "aft"}, {"a": 3, "b": 0, "op": "bef"},
            {"a": 3, "b": 0, "op": "aft"}, {"a": 5, "b": 0, "op": "bef"},
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
            {"a": 1, "b": 1, "op": "nick"},             {"a": 1, "b": 3, "op": "nick"}, {"a": 2, "b": 1, "op": "nick"},
                        {"a": 3, "b": 3, "op": "nick"}, {"a": 3, "b": 2, "op": "nick"},
            {"a": 4, "b": 1, "op": "nick"}, {"a": 4, "b": 3, "op": "nick"},
            {"a": 5, "b": 2, "op": "nick"}, {"a": 6, "b": 1, "op": "nick"},
        ],
    },
    # =========================================================================
    # (mo) ENTRY-LEVEL UNIT 8 -- TIME, CALENDAR & MEASUREMENT
    # -------------------------------------------------------------------------
    # The spreadsheet Jim asked for on 2026-08-24 found the only hole left in the
    # curriculum: Entry-Level Units 8 and 9 had NO scripted lessons at all, in the
    # one course where the youngest children start. This is Unit 8.
    #
    # ⚠️ EVERY LESSON HERE IS A SHAPE THE CHILD HAS ALREADY MET. That is the whole
    # design: a six-year-old meeting the clock should not also be meeting a new
    # kind of arithmetic. "Later on the clock" is counting on (U2/U3) along a
    # number line. "Minutes past the hour" counts by five, exactly as U7 counts
    # nickels. "Weeks and days" is U7's coin shape with sevens instead of fives.
    # "How much longer" is taking away (U3) with a ruler drawn under it.
    #
    # ⚠️ THE CLOCK FACE DOES NOT WRAP HERE, and hrl's check enforces it. "11
    # o'clock plus 3 hours is 2 o'clock" is a real idea, and it is not this unit's
    # -- it needs the twelve-hour circle taught first. A lesson that quietly
    # wrapped would be teaching modular arithmetic to a child who is still
    # counting on their fingers.
    # =========================================================================
    {
        "id": "entry-u8-later-on-the-clock", "course": "entry", "unit": 8,
        "topic": "Later on the clock",
        "op": "hrl", "max_value": 12,
        "levels": ("abstract",),
        "symbols": ("o'clock",),
        "advance_line": ("Three in a row — you've got it! "
                         "You can tell what time it will be later."),
        "teach": [
            ("The short hand on a clock tells the hour. When it points at 3, we "
             "say it is 3 o'clock.",
             '[[goal text="Later on the clock"]]'
             '[[numberline min="1" max="12" points="3" caption="the clock hours — the hand at 3"]]'),
            ("Watch me. It is 9 o'clock now. Two hours later, count on: 10, 11. "
             "It is 11 o'clock.",
             '[[numberline min="1" max="12" points="11" caption="the clock hours — the hand at 11"]]'
             '[[step eq="9 o\'clock, 2 hours later = 11"]]'),
            ("One more, watch. It is 5 o'clock. Four hours later, count on: 6, "
             "7, 8, 9. It is 9 o'clock.",
             '[[numberline min="1" max="12" points="9" caption="the clock hours — the hand at 9"]]'
             '[[step eq="5 o\'clock, 4 hours later = 9"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. It is 7 o'clock. Three "
                        "hours later, count on: 8, 9, 10. It is 10 o'clock.",
                        '[[step eq="7 o\'clock, 3 hours later = 10"]]'),
             "ask": {"a": 3, "b": 1, "op": "hrl"}},
            {"worked": ("One more together. It is 10 o'clock. One hour later is "
                        "11 o'clock.",
                        '[[step eq="10 o\'clock, 1 hour later = 11"]]'),
             "ask": {"a": 5, "b": 2, "op": "hrl"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 1, "b": 1, "op": "hrl"}, {"a": 2, "b": 1, "op": "hrl"},
            {"a": 2, "b": 2, "op": "hrl"}, {"a": 4, "b": 1, "op": "hrl"},
            {"a": 3, "b": 2, "op": "hrl"}, {"a": 4, "b": 2, "op": "hrl"},
            {"a": 4, "b": 3, "op": "hrl"}, {"a": 5, "b": 3, "op": "hrl"},
            {"a": 6, "b": 3, "op": "hrl"}, {"a": 6, "b": 4, "op": "hrl"},
            {"a": 7, "b": 4, "op": "hrl"}, {"a": 8, "b": 4, "op": "hrl"},
        ],
    },
    {
        "id": "entry-u8-minutes-past-the-hour", "course": "entry", "unit": 8,
        "topic": "Minutes past the hour",
        "op": "min5", "max_value": 55,
        "levels": ("abstract",),
        "symbols": ("minute hand",),
        "advance_line": ("Three in a row — you've got it! "
                         "You can read the minutes on a clock."),
        "teach": [
            ("The long hand is the minute hand, and it moves faster than the "
             "short one. From one number to the next is five minutes.",
             '[[goal text="Minutes past the hour"]]'),
            ("Watch me. The minute hand points to 6. Count by five: 5, 10, 15, "
             "20, 25, 30. That is 30 minutes past the hour.",
             '[[step eq="6 numbers past 12, five minutes each = 30"]]'),
            ("Now the other way, watch. It is 20 minutes past. Count by five "
             "until you reach 20: 5, 10, 15, 20. That is four numbers, so the "
             "minute hand points to 4.",
             '[[step eq="20 minutes, five minutes each = 4 on the clock"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. The minute hand points "
                        "to 9. Count by five: 5, 10, 15, 20, 25, 30, 35, 40, 45. "
                        "That is 45 minutes.",
                        '[[step eq="9 numbers past 12, five minutes each = 45"]]'),
             "ask": {"a": 10, "b": 0, "op": "min5"}},
            {"worked": ("One more together. It is 15 minutes past. Count by "
                        "five: 5, 10, 15. Three numbers, so the hand points to 3.",
                        '[[step eq="15 minutes, five minutes each = 3 on the clock"]]'),
             "ask": {"a": 55, "b": 0, "op": "min5q"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        # ⚠️ THE BANK IS TEN, NOT TWELVE, AND THAT IS THE POINT. A clock has only
        # ELEVEN positions the minute hand can land on, and this lesson also
        # DEMONSTRATES four of them -- teach beats two and three, and both worked
        # examples. Positions 3, 4, 6 and 9 are therefore reserved: they are shown,
        # so they are never asked. Filling the bank to twelve would have meant
        # asking a child a question Mr. Cadabra answered out loud two minutes
        # earlier, which is the exact defect workedaudit.py exists to find.
        #
        # BOTH DIRECTIONS, INTERLEAVED BY DIFFICULTY. The key is the clock NUMBER
        # either way (min5's a, min5q's a divided by five), so "the hand points to
        # 2" and "10 minutes past" sit together on the ramp. That pairing is the
        # lesson, not a duplicate: a child who can only go one way has memorised a
        # list rather than learned to read a clock.
        "bank": [
            {"a": 5, "b": 0, "op": "min5q"}, {"a": 1, "b": 0, "op": "min5"},
            {"a": 10, "b": 0, "op": "min5q"}, {"a": 2, "b": 0, "op": "min5"},
            {"a": 25, "b": 0, "op": "min5q"}, {"a": 5, "b": 0, "op": "min5"},
            {"a": 35, "b": 0, "op": "min5q"}, {"a": 7, "b": 0, "op": "min5"},
            {"a": 40, "b": 0, "op": "min5q"}, {"a": 8, "b": 0, "op": "min5"},
        ],
    },
    {
        "id": "entry-u8-weeks-and-days", "course": "entry", "unit": 8,
        "topic": "Weeks and days",
        "op": "dwd", "max_value": 34,
        "levels": ("abstract",),
        "symbols": ("week",),
        "advance_line": ("Three in a row — you've got it! "
                         "You can count weeks and days."),
        "teach": [
            ("A week is seven days. Sunday, Monday, Tuesday, Wednesday, "
             "Thursday, Friday, Saturday — and then a new one starts.",
             '[[goal text="Weeks and days"]]'),
            ("Watch me. 2 weeks and 2 days. Count the weeks by seven: 7, 14. "
             "Then count the loose days on: 15, 16. That is 16 days.",
             '[[step eq="2 weeks and 2 days = 16 days"]]'),
            ("One more, watch. 3 weeks and 4 days. By seven: 7, 14, 21. Then "
             "on: 22, 23, 24, 25. That is 25 days.",
             '[[step eq="3 weeks and 4 days = 25 days"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 1 week and 6 days. "
                        "Seven, then on: 8, 9, 10, 11, 12, 13. That is 13 days.",
                        '[[step eq="1 week and 6 days = 13 days"]]'),
             "ask": {"a": 1, "b": 4, "op": "dwd"}},
            {"worked": ("One more together. 4 weeks and 1 day. By seven: 7, 14, "
                        "21, 28. One more day: 29 days.",
                        '[[step eq="4 weeks and 1 day = 29 days"]]'),
             "ask": {"a": 2, "b": 6, "op": "dwd"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 1, "b": 1, "op": "dwd"}, {"a": 1, "b": 2, "op": "dwd"},
            {"a": 1, "b": 3, "op": "dwd"}, {"a": 1, "b": 5, "op": "dwd"},
            {"a": 2, "b": 1, "op": "dwd"}, {"a": 2, "b": 3, "op": "dwd"},
            {"a": 2, "b": 5, "op": "dwd"}, {"a": 3, "b": 1, "op": "dwd"},
            {"a": 3, "b": 3, "op": "dwd"}, {"a": 3, "b": 6, "op": "dwd"},
            {"a": 4, "b": 2, "op": "dwd"}, {"a": 4, "b": 5, "op": "dwd"},
        ],
    },
    {
        "id": "entry-u8-how-much-longer", "course": "entry", "unit": 8,
        "topic": "How much longer",
        "op": "cube", "max_value": 20,
        "levels": ("abstract",),
        "symbols": ("longer",),
        "advance_line": ("Three in a row — you've got it! "
                         "You can measure and compare with cubes."),
        "teach": [
            ("We can measure with cubes. Line them up under the pencil, start "
             "at the very end, and count. More cubes means longer than fewer.",
             '[[goal text="How much longer"]]'),
            ("Watch me. The pencil is 13 cubes. The crayon is 4 cubes. 13 take "
             "away 4 equals 9, so the pencil is 9 cubes longer.",
             '[[bars data="pencil:13 | crayon:4" caption="pencil 13 and crayon 4"]]'
             '[[step eq="13 cubes − 4 cubes = 9"]]'),
            ("One more, watch. The pencil is 17 cubes. The crayon is 9 cubes. "
             "17 take away 9 equals 8, so the pencil is 8 cubes longer.",
             '[[bars data="pencil:17 | crayon:9" caption="pencil 17 and crayon 9"]]'
             '[[step eq="17 cubes − 9 cubes = 8"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. The pencil is 19 "
                        "cubes. The crayon is 12 cubes. 19 take away 12 equals "
                        "7, so the pencil is 7 cubes longer.",
                        '[[step eq="19 cubes − 12 cubes = 7"]]'),
             "ask": {"a": 11, "b": 5, "op": "cube"}},
            {"worked": ("One more together. The pencil is 20 cubes. The crayon "
                        "is 13 cubes. 20 take away 13 equals 7, so the pencil is "
                        "7 cubes longer.",
                        '[[step eq="20 cubes − 13 cubes = 7"]]'),
             "ask": {"a": 15, "b": 6, "op": "cube"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 3, "b": 1, "op": "cube"}, {"a": 4, "b": 1, "op": "cube"},
            {"a": 5, "b": 2, "op": "cube"}, {"a": 6, "b": 2, "op": "cube"},
            {"a": 7, "b": 3, "op": "cube"}, {"a": 8, "b": 3, "op": "cube"},
            {"a": 9, "b": 4, "op": "cube"}, {"a": 10, "b": 4, "op": "cube"},
            {"a": 12, "b": 5, "op": "cube"}, {"a": 14, "b": 6, "op": "cube"},
            {"a": 16, "b": 7, "op": "cube"}, {"a": 18, "b": 8, "op": "cube"},
        ],
    },
    # =========================================================================
    # (mp) ENTRY-LEVEL UNIT 9 -- SHAPES, PATTERNS & GROUPS
    # -------------------------------------------------------------------------
    # ⭐ THE LAST UNSCRIPTED UNIT IN THE CURRICULUM. With these four lessons every
    # unit of all ten courses -- Entry-Level Math through Differential Equations
    # -- has scripted lessons.
    #
    # ⚠️ THE TWO GROUP LESSONS NEVER SAY "TIMES", and that is deliberate rather
    # than squeamish. Basic Math Unit 2 is where multiplying is taught and named;
    # a child should meet the IDEA -- equal groups counted up, and a pile shared
    # fairly -- before the word and the symbol arrive. So grp counts by repeated
    # addition out loud and eqs deals one at a time, exactly as a six-year-old
    # would with real counters.
    #
    # ⚠️ AND eqs NEVER LEAVES A REMAINDER. Its check refuses anything that does.
    # Left-overs are basic-u3-left-overs' lesson; meeting them here, before fair
    # sharing itself is solid, teaches a child that sharing sometimes just fails.
    # =========================================================================
    {
        "id": "entry-u9-sides-and-corners", "course": "entry", "unit": 9,
        "topic": "Sides and corners",
        "op": "sid", "max_value": 10,
        "levels": ("abstract",),
        "symbols": ("side", "corner"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can count the sides and corners on a shape."),
        "teach": [
            ("Every flat shape is made of straight sides, and the place where "
             "two sides meet is a corner of the shape.",
             '[[goal text="Sides and corners"]]'),
            ("Watch me count a triangle. Side, side, side — 3 sides. Its name "
             "even says so: tri means three.",
             '[[step eq="triangle → 3 sides"]]'),
            ("Now its corners, watch. Corner, corner, corner — 3 corners. A "
             "triangle has 3 sides and 3 corners. Every flat shape is like that: "
             "it has just as many corners as sides.",
             '[[step eq="triangle → 3 corners, the same as its sides"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. A square. Side, side, "
                        "side, side — 4 sides.",
                        '[[step eq="square → 4 sides"]]'),
             "ask": {"a": 5, "b": 0, "op": "sid"}},
            {"worked": ("One more together. A square again, but its corners "
                        "this time. Corner, corner, corner, corner — 4 corners, "
                        "the same as its sides.",
                        '[[step eq="square → 4 corners"]]'),
             "ask": {"a": 5, "b": 0, "op": "cor"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        # ⚠️ THE TRIANGLE AND THE SQUARE ARE RESERVED. Both teach beats work the
        # triangle and both worked examples work the square, so neither shape is
        # ever ASKED -- in either direction. That leaves the five bigger shapes,
        # each asked for its sides and for its corners, which IS the lesson: the
        # two counts always match.
        "bank": [
            {"a": 6, "b": 0, "op": "sid"}, {"a": 6, "b": 0, "op": "cor"},
            {"a": 7, "b": 0, "op": "sid"}, {"a": 7, "b": 0, "op": "cor"},
            {"a": 8, "b": 0, "op": "sid"}, {"a": 8, "b": 0, "op": "cor"},
            {"a": 10, "b": 0, "op": "sid"}, {"a": 10, "b": 0, "op": "cor"},
        ],
    },
    {
        "id": "entry-u9-what-comes-next", "course": "entry", "unit": 9,
        "topic": "What comes next",
        "op": "pat", "max_value": 30,
        "levels": ("abstract",),
        "symbols": ("pattern",),
        "advance_line": ("Three in a row — you've got it! "
                         "You can find what comes next in a pattern."),
        "teach": [
            ("A pattern is numbers that follow a rule. Find the jump from one "
             "number to the next, then use that jump again.",
             '[[goal text="What comes next"]]'),
            ("Watch me. 4, 7, 10, 13. From 4 to 7 is a jump of 3. Check it: 7 "
             "to 10 is 3, and 10 to 13 is 3. So next is 13 and 3 more — 16.",
             '[[step eq="4, 7, 10, 13, ? — jump of 3"]]'),
            ("One more, watch. 9, 14, 19, 24. The jump is 5 every time, so next "
             "is 24 and 5 more — 29.",
             '[[step eq="9, 14, 19, 24, ? — jump of 5"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 3, 7, 11, 15. The jump "
                        "is 4 every time, so next is 15 and 4 more — 19.",
                        '[[step eq="3, 7, 11, 15, ? — jump of 4"]]'),
             "ask": {"a": 3, "b": 2, "op": "pat"}},
            {"worked": ("One more together. 6, 8, 10, 12. The jump is 2, so "
                        "next is 12 and 2 more — 14.",
                        '[[step eq="6, 8, 10, 12, ? — jump of 2"]]'),
             "ask": {"a": 7, "b": 4, "op": "pat"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            # ⚠️ NO JUMP OF ONE IN THE TAUGHT BANK. "1, 2, 3, 4 -- what comes
            # next?" is counting, not a pattern, and the ramp keys on the jump, so
            # three of them would have opened the practice -- a step DOWN from
            # teach beats that work jumps of 3 and 5. The op still allows a jump of
            # one so Abrabot's pool can offer an easy rung; the LESSON starts at
            # the smallest jump a child has to actually look for.
            {"a": 2, "b": 2, "op": "pat"}, {"a": 5, "b": 2, "op": "pat"},
            {"a": 9, "b": 2, "op": "pat"}, {"a": 1, "b": 3, "op": "pat"},
            {"a": 5, "b": 3, "op": "pat"}, {"a": 8, "b": 3, "op": "pat"},
            {"a": 2, "b": 4, "op": "pat"}, {"a": 6, "b": 4, "op": "pat"},
            {"a": 9, "b": 4, "op": "pat"}, {"a": 1, "b": 5, "op": "pat"},
            {"a": 4, "b": 5, "op": "pat"}, {"a": 6, "b": 5, "op": "pat"},
        ],
    },
    {
        "id": "entry-u9-equal-groups", "course": "entry", "unit": 9,
        "topic": "Equal groups",
        "op": "grp", "max_value": 25,
        "levels": ("abstract",),
        "symbols": ("group",),
        "advance_line": ("Three in a row — you've got it! "
                         "You can count equal groups."),
        "teach": [
            ("When every group holds the same amount, you do not have to count "
             "one at a time. Count by the size of one group instead.",
             '[[goal text="Equal groups"]]'),
            ("Watch me. 3 groups with 5 stars in each. Count by five: 5, 10, "
             "15. That is 15 stars in all.",
             '[[step eq="3 groups of 5 = 15"]]'),
            ("One more, watch. 4 groups with 2 stars in each. Count by two: 2, "
             "4, 6, 8. That is 8 stars in all.",
             '[[step eq="4 groups of 2 = 8"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 5 groups with 4 stars "
                        "in each. Count by four: 4, 8, 12, 16, 20. That is 20 "
                        "stars in all.",
                        '[[step eq="5 groups of 4 = 20"]]'),
             "ask": {"a": 2, "b": 2, "op": "grp"}},
            {"worked": ("One more together. 2 groups with 5 stars in each. 5, "
                        "10. That is 10 stars in all.",
                        '[[step eq="2 groups of 5 = 10"]]'),
             "ask": {"a": 3, "b": 4, "op": "grp"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            # (3,5) is NOT here on purpose -- teach beat two works it out loud.
            {"a": 2, "b": 3, "op": "grp"}, {"a": 3, "b": 2, "op": "grp"},
            {"a": 2, "b": 4, "op": "grp"}, {"a": 3, "b": 3, "op": "grp"},
            {"a": 4, "b": 3, "op": "grp"}, {"a": 5, "b": 3, "op": "grp"},
            {"a": 4, "b": 4, "op": "grp"}, {"a": 4, "b": 5, "op": "grp"},
            {"a": 5, "b": 5, "op": "grp"},
        ],
    },
    {
        "id": "entry-u9-sharing-fairly", "course": "entry", "unit": 9,
        "topic": "Sharing fairly",
        "op": "eqs", "max_value": 30,
        "levels": ("abstract",),
        "symbols": ("equal",),
        "advance_line": ("Three in a row — you've got it! "
                         "You can share a pile into equal groups."),
        "teach": [
            ("Sharing fairly means every group ends up with the same amount — "
             "equal groups, none of them bigger than another.",
             '[[goal text="Sharing fairly"]]'),
            ("Watch me. 12 stars shared into 4 groups. Deal them out one at a "
             "time, round and round. Every group ends with 3.",
             '[[step eq="12 shared into 4 equal groups = 3 each"]]'),
            ("One more, watch. 15 stars shared into 5 groups. Deal them round "
             "and round, and every group ends with 3.",
             '[[step eq="15 shared into 5 equal groups = 3 each"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 20 stars shared into 4 "
                        "groups. Deal them round and round — 5 in each group.",
                        '[[step eq="20 shared into 4 equal groups = 5 each"]]'),
             "ask": {"a": 6, "b": 2, "op": "eqs"}},
            {"worked": ("One more together. 25 stars shared into 5 groups. "
                        "Every group ends with 5.",
                        '[[step eq="25 shared into 5 equal groups = 5 each"]]'),
             "ask": {"a": 9, "b": 3, "op": "eqs"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 4, "b": 2, "op": "eqs"}, {"a": 6, "b": 3, "op": "eqs"},
            {"a": 8, "b": 2, "op": "eqs"}, {"a": 8, "b": 4, "op": "eqs"},
            {"a": 10, "b": 5, "op": "eqs"}, {"a": 10, "b": 2, "op": "eqs"},
            {"a": 12, "b": 3, "op": "eqs"}, {"a": 15, "b": 3, "op": "eqs"},
            {"a": 16, "b": 4, "op": "eqs"}, {"a": 18, "b": 3, "op": "eqs"},
            {"a": 24, "b": 4, "op": "eqs"}, {"a": 30, "b": 5, "op": "eqs"},
        ],
    },
]
LESSONS.extend(_ENTRY_MORE)

# ---- this course's slice of COURSE_ORDER: the teaching order (lessons/__init__.py joins the ten) ----
ORDER = [
    # ---- ENTRY-LEVEL MATH (the kc re-cut: these eight lessons were authored under
    # Basic U1 and belong here by Jim's own curriculum -- Eureka audit 2026-08-21;
    # kd opens the course where Eureka does -- counting -- and adds story problems
    # and coins) ----
    # (pg) THE COURSE IS NINE UNITS OF FOUR NOW. Sixteen lessons were added so a
    # five-year-old stops falling out of the authored lane onto the slow one. Each
    # new lesson sits where it is TAUGHT, not at the end: counting past ten before
    # comparing, doubles before three-in-a-row, no-regrouping take away before the
    # regrouping lesson that was already here, and coins in coin order -- nickels,
    # dimes, quarters, then change.
    "entry-u1-counting-to-10", "entry-u1-counting-past-ten",
    "entry-u1-numbers-before-and-after", "entry-u1-which-is-bigger",
    "entry-u2-add-single-digit", "entry-u2-doubles",
    "entry-u2-add-past-ten", "entry-u2-adding-three-numbers",
    "entry-u3-take-away-single-digit", "entry-u3-take-away-bigger",
    "entry-u3-the-missing-part", "entry-u3-story-problems",
    "entry-u4-tens-and-ones", "entry-u4-hundreds-tens-and-ones",
    "entry-u4-ten-more", "entry-u4-what-a-digit-is-worth",
    "entry-u5-add-two-digit-no-carry", "entry-u5-add-with-carrying",
    "entry-u5-crossing-a-hundred", "entry-u5-adding-three-digit-numbers",
    "entry-u6-take-away-two-digit", "entry-u6-take-away-with-regrouping",
    "entry-u6-take-away-three-digit", "entry-u6-checking-by-adding-back",
    "entry-u7-counting-coins", "entry-u7-dimes-and-pennies",
    "entry-u7-quarters", "entry-u7-making-change",
    # (mo) Unit 8 -- Time, Calendar & Measurement. The clock lessons come after
    # coins on purpose: counting by five is learned on nickels first, and the
    # minute hand is the same count on a rounder board.
    "entry-u8-later-on-the-clock", "entry-u8-minutes-past-the-hour",
    "entry-u8-weeks-and-days", "entry-u8-how-much-longer",
    # (mp) Unit 9 -- Shapes, Patterns & Groups. THE LAST UNSCRIPTED UNIT. Groups
    # come after patterns because counting equal groups IS a pattern with a jump.
    "entry-u9-sides-and-corners", "entry-u9-what-comes-next",
    "entry-u9-equal-groups", "entry-u9-sharing-fairly",
]

# I did no harm and this file is not truncated.

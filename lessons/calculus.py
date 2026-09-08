# =============================================================================
# lessons/calculus.py  --  CALCULUS: THE AUTHORED LESSONS  --  Hyperion Shift LLC
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
# CALCULUS UNIT 1 -- Limits & Continuity (build lu) -- ⭐ THE TWELFTH COURSE
# The thread: Pre-Calc met the limit; Calculus puts it to WORK. Limits pass
# straight through arithmetic, they survive all the way out to infinity where
# only the leading terms matter, a break has a measurable size, and a curve
# can be MENDED so that no break is left at all.
# =============================================================================
_CALCULUS_U1 = [
    {
        "id": "calc-u1-limits-pass-through",
        "course": "calculus", "unit": 1,
        "topic": "The limit laws",
        "op": "llaw", "max_value": 100,
        "levels": ("abstract",),
        "symbols": ("limits", "product"),
        "advance_line": "Three in a row, and you can say why — you've got it! Limits pass straight through the arithmetic.",
        "why": [
            ("Welcome to Calculus, built on one idea you already own: the limit — where a "
             "function is headed. Pre-Calculus found limits one at a time. Calculus needs "
             "them to join up, because real functions are built from simpler ones, and "
             "happily they do, without any fuss at all.",
             '[[goal text="Limits pass through"]]'),
        ],
        "picture": [
            ("Here are two curves. Watch them near x equals 4, where the line is drawn: "
             "f closes on 6 and g closes on 5. Look at the two heights the curves are "
             "heading for — those two numbers are all the product needs.",
             '[[graph func="6 + (x-4)^2/8; 5 - (x-4)^2/8" hole="4" lines="x=4" names="f; g" range="0..8" yrange="0..9" caption="f closes on 6 at x = 4 and g closes on 5 — the two heights the product needs"]]'),
        ],
        "teach": [
            ("That is the method: limits pass straight through the arithmetic. If f is "
             "heading for 6 and g for 5, then f plus g heads for 11 and f times g heads "
             "for 30. Whatever you do to the functions, you may do to their limits "
             "instead. Here is the product curve closing on 30.",
             '[[graph func="(6 + (x-4)^2/8)*(5 - (x-4)^2/8)" hole="4" lines="x=4" names="f × g" range="0..8" yrange="0..36" caption="f times g closes on 30 at x = 4 — 6 times 5"]][[step eq="6 × 5 = 30"]]'),
            ("That single permission is what every later rule rests on: take a "
             "complicated function apart, follow the pieces, put the answers back "
             "together. For a product, times the two limits — adding answers a different "
             "question, and 6 is only the bigger of the two.",
             '[[step eq="30 ✓"]][[step eq="11 ✗ that is the sum · 6 ✗ just the bigger"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. f heads for 9 and g for 4: their "
                        "product heads for 36.",
                        '[[graph func="(9 + (x-4)^2/8)*(4 - (x-4)^2/8)" hole="4" lines="x=4" names="f × g" range="0..8" yrange="0..42" caption="the product closes on 36 — 9 times 4"]][[step eq="9 × 4 = 36"]]'),
             "ask": {"a": 2, "b": 11, "op": "llaw"}},
            {"worked": ("One more together. Limits of 7 and 6 give a product heading for "
                        "42 — the limit passes straight through the times sign.",
                        '[[graph func="(7 + (x-4)^2/8)*(6 - (x-4)^2/8)" hole="4" lines="x=4" names="f × g" range="0..8" yrange="0..48" caption="the product closes on 42 — 7 times 6"]][[step eq="7 × 6 = 42"]]'),
             "ask": {"a": 12, "b": 2, "op": "llaw"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. f heads for 6 and g "
                       "for 5, so f times g heads for 30. Tap the reason why."),
            "choices": ("because a limit passes straight through the arithmetic | "
                        "because the bigger limit always wins | "
                        "because 6 and 5 are added to make 30"),
            "answer": "because a limit passes straight through the arithmetic",
            "board": '[[graph func="6 + (x-4)^2/8; 5 - (x-4)^2/8" hole="4" lines="x=4" names="f; g" range="0..8" yrange="0..9" caption="why 30?"]]',
        },
        "recap": [
            ("So, here it is again. Limits pass straight through the arithmetic: whatever "
             "you do to the functions, you may do to their limits instead. For a product, "
             "times the two limits. Adding answers a different question, and the bigger "
             "limit alone is not the product.",
             '[[graph func="(6 + (x-4)^2/8)*(5 - (x-4)^2/8)" hole="4" lines="x=4" names="f × g" range="0..8" yrange="0..36" caption="the product closes on the product of the limits"]]'),
            ("And that is the limit law every later rule rests on.",
             '[[step eq="6 × 5 = 30"]]'),
        ],
        "bank": [
            {"a": 3, "b": 2, "op": "llaw"},
            {"a": 2, "b": 4, "op": "llaw"},
            {"a": 2, "b": 5, "op": "llaw"},
            {"a": 4, "b": 3, "op": "llaw"},
            {"a": 2, "b": 7, "op": "llaw"},
            {"a": 5, "b": 3, "op": "llaw"},
            {"a": 8, "b": 2, "op": "llaw"},
            {"a": 3, "b": 6, "op": "llaw"},
            {"a": 5, "b": 4, "op": "llaw"},
            {"a": 3, "b": 7, "op": "llaw"},
        ],
    },
    {
        "id": "calc-u1-far-out-only-the-leaders-matter",
        "course": "calculus", "unit": 1,
        "topic": "Limits at infinity",
        "op": "linf", "max_value": 96,
        "levels": ("abstract",),
        "symbols": ("infinity", "cancel"),
        "advance_line": "Three in a row, and you can say why — you've got it! Same power top and bottom — the ratio survives.",
        "why": [
            ("Some limits are asked at the far end of the number line, where x runs off "
             "toward infinity. Algebra Two met one: a fraction whose bottom outgrew its top "
             "settled to a number. Calculus asks it in general, and the answer is the "
             "same every time — far out, only the leaders matter.",
             '[[goal text="Far out, only the leaders matter"]]'),
        ],
        "picture": [
            ("Here is 8 x squared over 2 x squared, drawn as x grows. Look at the curve: "
             "it climbs quickly, then flattens, and the further out you go the flatter it "
             "gets. It is settling onto one number and never leaving it.",
             '[[graph func="(8*x^2)/(2*x^2 + 2)" names="y = 8x² / (2x² + 2)" range="0..12" yrange="0..6" caption="8 x squared over 2 x squared — the curve flattens as x grows"]]'),
        ],
        "teach": [
            ("That is the method: when the top and bottom carry the same power, the x "
             "squareds cancel exactly, because they grow at the very same speed. What is "
             "left is 8 over 2, which is 4. The curve flattens onto the line y equals 4 "
             "and stays there.",
             '[[graph func="(8*x^2)/(2*x^2 + 2)" names="y = 8x² / (2x² + 2)" lines="y=4" range="0..12" yrange="0..6" caption="the curve settles onto y = 4 — 8 over 2"]][[step eq="8 ÷ 2 = 4"]]'),
            ("Nothing else about the two pieces matters at all. Taking one number from "
             "the other, or timesing them, describes no part of what the fraction does. "
             "The ratio of the front numbers is what survives.",
             '[[step eq="4 ✓"]][[step eq="6 ✗ subtracted · 16 ✗ timesed"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 45 x squared over 9 x squared: the "
                        "x squareds cancel, leaving 5.",
                        '[[graph func="(45*x^2)/(9*x^2 + 9)" names="y = 45x² / (9x² + 9)" lines="y=5" range="0..12" yrange="0..7" caption="settling onto y = 5 — 45 over 9"]][[step eq="45 ÷ 9 = 5"]]'),
             "ask": {"a": 36, "b": 3, "op": "linf"}},
            {"worked": ("One more together. 70 x squared over 10 x squared: the x squareds "
                        "cancel, leaving 70 over 10 — 7.",
                        '[[graph func="(70*x^2)/(10*x^2 + 10)" names="y = 70x² / (10x² + 10)" lines="y=7" range="0..12" yrange="0..9" caption="settling onto y = 7 — 70 over 10"]][[step eq="70 ÷ 10 = 7"]]'),
             "ask": {"a": 26, "b": 2, "op": "linf"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Far out, 8 x squared "
                       "over 2 x squared settles to 4. Tap the reason why."),
            "choices": ("because the x squareds grow at the same speed and cancel | "
                        "because a fraction always settles to its top number | "
                        "because 8 take away 2 is the limit"),
            "answer": "because the x squareds grow at the same speed and cancel",
            "board": '[[graph func="(8*x^2)/(2*x^2 + 2)" names="y = 8x² / (2x² + 2)" range="0..12" yrange="0..6" caption="why 4?"]]',
        },
        "recap": [
            ("So, here it is again. Far out, with the same power on top and bottom, the "
             "powers cancel and the limit is the ratio of the front numbers. Nothing else "
             "about the pieces matters — not their difference, not their product.",
             '[[graph func="(8*x^2)/(2*x^2 + 2)" names="y = 8x² / (2x² + 2)" lines="y=4" range="0..12" yrange="0..6" caption="only the leaders matter"]]'),
            ("And that is a limit at infinity.",
             '[[step eq="8 ÷ 2 = 4"]]'),
        ],
        "bank": [
            {"a": 6, "b": 3, "op": "linf"},
            {"a": 6, "b": 2, "op": "linf"},
            {"a": 16, "b": 4, "op": "linf"},
            {"a": 25, "b": 5, "op": "linf"},
            {"a": 36, "b": 6, "op": "linf"},
            {"a": 21, "b": 3, "op": "linf"},
            {"a": 16, "b": 2, "op": "linf"},
            {"a": 36, "b": 4, "op": "linf"},
            {"a": 50, "b": 5, "op": "linf"},
            {"a": 66, "b": 6, "op": "linf"},
        ],
    },
    {
        "id": "calc-u1-how-big-is-the-break",
        "course": "calculus", "unit": 1,
        "topic": "Jump discontinuities",
        "op": "jump", "max_value": 40,
        "levels": ("abstract",),
        "symbols": ("jump", "sides"),
        "advance_line": "Three in a row, and you can say why — you've got it! The jump is the gap between the two sides.",
        "why": [
            ("A curve is continuous where you could draw it without lifting the pencil. "
             "Where you must lift it, there is a break — and Pre-Calculus already met the "
             "kind where the two sides head for different numbers. Now the break gets "
             "measured, because a break has a size.",
             '[[goal text="How big is the break?"]]'),
        ],
        "picture": [
            ("Here are two shelves. Below x equals 6 the curve sits at 4; from 6 onward it "
             "sits at 10. Look at the border: an open dot where the low shelf ends, a "
             "closed dot where the high shelf begins, and a leap between them.",
             '[[graph func="4 for x<6; 10 for x>=6" range="0..12" yrange="0..14" caption="two shelves at x = 6 — the open dot at 4, the closed dot at 10, and the leap between them"]]'),
        ],
        "teach": [
            ("That is the method: take one side from the other. From the left the curve "
             "heads for 4; from the right it heads for 10. It leaps 6 in no distance at "
             "all, so the break has a size — 6 — and mathematicians call this a jump "
             "discontinuity for the obvious reason.",
             '[[graph func="4 for x<6; 10 for x>=6" lines="x=6" points="(6,4),(6,10)" range="0..12" yrange="0..14" caption="the leap at x = 6 — from 4 up to 10 is 6"]][[step eq="10 − 4 = a jump of 6"]]'),
            ("The two sides are what the measurement needs. Answering 10 names where the "
             "curve lands but not how far it travelled, and adding the heights describes "
             "nothing the curve ever does.",
             '[[step eq="6 ✓"]][[step eq="10 ✗ where it lands · 14 ✗ added"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. The left side heads for 9 and the "
                        "right for 25: a jump of 16.",
                        '[[graph func="9 for x<6; 25 for x>=6" lines="x=6" points="(6,9),(6,25)" range="0..12" yrange="0..29" caption="from 9 up to 25 is 16"]][[step eq="25 − 9 = 16"]]'),
             "ask": {"a": 2, "b": 14, "op": "jump"}},
            {"worked": ("One more together. Sides of 11 and 30: 30 take away 11 — a jump "
                        "of 19, measured from one shelf to the other.",
                        '[[graph func="11 for x<6; 30 for x>=6" lines="x=6" points="(6,11),(6,30)" range="0..12" yrange="0..34" caption="from 11 up to 30 is 19"]][[step eq="30 − 11 = 19"]]'),
             "ask": {"a": 4, "b": 17, "op": "jump"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. The sides head for 4 "
                       "and 10, and the jump is 6. Tap the reason why."),
            "choices": ("because the jump is the gap between the two sides | "
                        "because the jump is always where the curve lands | "
                        "because 4 and 10 are added to make the jump"),
            "answer": "because the jump is the gap between the two sides",
            "board": '[[graph func="4 for x<6; 10 for x>=6" range="0..12" yrange="0..14" caption="why 6?"]]',
        },
        "recap": [
            ("So, here it is again. A jump discontinuity is a break with a size, and the "
             "size is the gap between the two sides — take one from the other. Where the "
             "curve lands is not how far it leapt, and adding the heights is not a "
             "measurement of anything.",
             '[[graph func="4 for x<6; 10 for x>=6" lines="x=6" points="(6,4),(6,10)" range="0..12" yrange="0..14" caption="the jump is the gap between the sides"]]'),
            ("And that is how big the break is.",
             '[[step eq="10 − 4 = 6"]]'),
        ],
        "bank": [
            {"a": 3, "b": 5, "op": "jump"},
            {"a": 4, "b": 7, "op": "jump"},
            {"a": 3, "b": 7, "op": "jump"},
            {"a": 5, "b": 10, "op": "jump"},
            {"a": 7, "b": 13, "op": "jump"},
            {"a": 2, "b": 9, "op": "jump"},
            {"a": 4, "b": 12, "op": "jump"},
            {"a": 3, "b": 12, "op": "jump"},
            {"a": 5, "b": 15, "op": "jump"},
            {"a": 7, "b": 18, "op": "jump"},
        ],
    },
    {
        "id": "calc-u1-mend-the-curve",
        "course": "calculus", "unit": 1,
        "topic": "Making a function continuous",
        "op": "cfix", "max_value": 30,
        "levels": ("abstract",),
        "symbols": ("continuous", "meet"),
        "advance_line": "Three in a row, and you can say why — you've got it! Walk the slope up to the border and match it.",
        "why": [
            ("A break can be mended. Take a curve that runs along y equals x plus 2 until "
             "x reaches 5, and then goes flat at 3. It jumps, badly. The question is what "
             "flat value would make it continuous instead — and that question is the "
             "whole test for continuity, run as a repair job.",
             '[[goal text="Mend the curve"]]'),
        ],
        "picture": [
            ("Here is the broken curve. The sloping piece climbs toward the border at x "
             "equals 5, and the flat piece sits down at 3. Look at the open dot where the "
             "slope arrives at the border — that is where the flat piece would have to "
             "meet it.",
             '[[graph func="x+2 for x<5; 3 for x>=5" range="0..9" yrange="0..11" caption="the slope climbs to the border at x = 5; the flat piece sits at 3 — they do not meet"]]'),
        ],
        "teach": [
            ("That is the method: walk the sloping piece right up to the border and see "
             "where it arrives. At x equals 5 it is heading for 5 plus 2, which is 7. Set "
             "the flat piece to 7 and the two ends meet exactly — no jump, no hole, "
             "nothing to lift the pencil for.",
             '[[graph func="x+2 for x<5; 7 for x>=5" points="(5,7)" range="0..9" yrange="0..11" caption="the flat piece raised to 7 — the two ends meet at x = 5"]][[step eq="5 + 2 = 7"]][[step eq="set the flat piece to 7"]]'),
            ("That is continuity: the limit coming in must equal the value waiting there. "
             "The broken 3 is what you were given, not what fits, and 2 is only the "
             "slope\'s own number.",
             '[[step eq="7 ✓"]][[step eq="3 ✗ the broken value · 2 ✗ the slope\'s number"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. y equals x plus 8 up to x equals "
                        "12: the slope arrives at 20, so the flat piece must be 20.",
                        '[[graph func="x+8 for x<12; 20 for x>=12" points="(12,20)" range="0..16" yrange="0..24" caption="the slope arrives at 20 — the flat piece meets it"]][[step eq="12 + 8 = 20"]]'),
             "ask": {"a": 6, "b": 2, "c": 9, "op": "cfix"}},
            {"worked": ("One more together. x plus 9 running up to x equals 13 arrives at "
                        "13 plus 9 — 22, so the flat piece must be 22.",
                        '[[graph func="x+9 for x<13; 22 for x>=13" points="(13,22)" range="0..17" yrange="0..26" caption="the slope arrives at 22 — the flat piece meets it"]][[step eq="13 + 9 = 22"]]'),
             "ask": {"a": 7, "b": 2, "c": 9, "op": "cfix"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. With x plus 2 running "
                       "up to x equals 5, the flat piece must be 7. Tap the reason why."),
            "choices": ("because the flat piece has to meet the slope where it arrives | "
                        "because the flat piece is always the border plus 2 | "
                        "because 3 is too small a number for a curve"),
            "answer": "because the flat piece has to meet the slope where it arrives",
            "board": '[[graph func="x+2 for x<5; 3 for x>=5" range="0..9" yrange="0..11" caption="why 7?"]]',
        },
        "recap": [
            ("So, here it is again. To mend a break, walk the sloping piece to the border "
             "and set the flat piece to meet it there — the limit coming in equals the "
             "value waiting. The broken value is what you were given, and the slope\'s "
             "own number is not a height.",
             '[[graph func="x+2 for x<5; 7 for x>=5" points="(5,7)" range="0..9" yrange="0..11" caption="the two ends meet"]]'),
            ("And that is continuity as a repair job.",
             '[[step eq="5 + 2 = 7"]]'),
        ],
        "bank": [
            {"a": 2, "b": 4, "c": 3, "op": "cfix"},
            {"a": 3, "b": 2, "c": 3, "op": "cfix"},
            {"a": 4, "b": 2, "c": 3, "op": "cfix"},
            {"a": 5, "b": 2, "c": 3, "op": "cfix"},
            {"a": 6, "b": 2, "c": 3, "op": "cfix"},
            {"a": 7, "b": 2, "c": 3, "op": "cfix"},
            {"a": 2, "b": 3, "c": 9, "op": "cfix"},
            {"a": 3, "b": 2, "c": 9, "op": "cfix"},
            {"a": 4, "b": 2, "c": 9, "op": "cfix"},
            {"a": 5, "b": 2, "c": 9, "op": "cfix"},
        ],
    },
]
LESSONS.extend(_CALCULUS_U1)
# =============================================================================
# CALCULUS UNIT 2 -- The Derivative: Definition & Basic Rules (build lv)
# The thread: THE SLOPE AT A SINGLE POINT. Pre-Calc shrank the window and named
# the limit; here it becomes a number you can compute, then a rule that skips
# the shrinking entirely, then a function you feed x's to.
# =============================================================================
_CALCULUS_U2 = [
    {
        "id": "calc-u2-the-window-closes",
        "course": "calculus", "unit": 2,
        "topic": "The derivative at a point",
        "op": "derv", "max_value": 48,
        "levels": ("abstract",),
        "symbols": ("derivative", "slope"),
        "advance_line": "Three in a row, and you can say why — you've got it! On x squared, the slope at a point is twice that point.",
        "why": [
            ("Pre-Calculus ended by shrinking a window on the curve y equals x squared "
             "and watching the average rate settle. That settling number has a name — "
             "the derivative — and it is the slope of the curve at one single point, "
             "which nothing before Calculus could measure.",
             '[[goal text="The window closes"]]'),
        ],
        "picture": [
            ("Here is y equals x squared with the point at x equals 4. Look at how steep "
             "the curve is right there — not across a window, but at that one point. "
             "The straight line touching the curve there has that steepness, and its "
             "slope is the derivative.",
             '[[graph func="x^2" names="y = x²" lines="y=8x-16" points="(4,16)" range="0..6" yrange="0..36" caption="y = x squared with the tangent at x = 4 — it climbs 8 for every step across"]]'),
        ],
        "teach": [
            ("That is the method: the average rate between two x\'s was the two put "
             "together, so slide the second one onto the first. Between 4 and 5 the rate "
             "is 9. Between 4 and 4 point 1 it is about 8 point 1. Closing in, it settles "
             "on 8, which is 4 plus 4.",
             '[[graph func="x^2" names="y = x²" lines="y=8x-16" points="(4,16)" range="0..6" yrange="0..36" caption="the window closes onto x = 4 — the rate settles on 8"]][[step eq="4 → 5: 9 · 4 → 4.1: 8.1 · closing in: 8"]]'),
            ("So on this curve the slope at any x is simply twice that x. At 4 the curve "
             "climbs at 8, at 10 it climbs at 20, and it never stops steepening. Careful: "
             "16 is how high the curve sits above 4, which is a different question.",
             '[[step eq="slope at 4 = 8 ✓"]][[step eq="16 ✗ that is the height"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. At x equals 30 the slope of x "
                        "squared is twice 30 — 60.",
                        '[[graph func="x^2" names="y = x²" lines="y=60x-900" points="(30,900)" range="0..32" yrange="0..1024" caption="the tangent at x = 30 climbs 60 for every step"]][[step eq="slope at 30 = 60"]]'),
             "ask": {"a": 13, "b": 0, "op": "derv"}},
            {"worked": ("One more together. At x equals 25 the slope is twice 25 — 50, and "
                        "the tangent there climbs 50 for every step across.",
                        '[[graph func="x^2" names="y = x²" lines="y=50x-625" points="(25,625)" range="0..27" yrange="0..729" caption="the tangent at x = 25 climbs 50 for every step"]][[step eq="slope at 25 = 50"]]'),
             "ask": {"a": 14, "b": 0, "op": "derv"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. On x squared, the "
                       "slope at x equals 4 is 8, not 16. Tap the reason why."),
            "choices": ("because the two x's of the window slide onto one point | "
                        "because the slope is always the height of the curve | "
                        "because 4 squared is 8"),
            "answer": "because the two x's of the window slide onto one point",
            "board": '[[graph func="x^2" names="y = x²" points="(4,16)" range="0..6" yrange="0..36" caption="why 8, and not 16?"]]',
        },
        "recap": [
            ("So, here it is again. The derivative is the slope of a curve at one single "
             "point — the average rate with its window closed. On x squared it is twice "
             "the x. The height of the curve at that x is a different question entirely.",
             '[[graph func="x^2" names="y = x²" lines="y=8x-16" points="(4,16)" range="0..6" yrange="0..36" caption="the slope at a point"]]'),
            ("And that is the derivative.",
             '[[step eq="slope at 4 = 8"]]'),
        ],
        "bank": [{"a": v, "b": 0, "op": "derv"} for v in
                 (3, 5, 6, 7, 8, 9, 10, 11, 12)],
    },
    {
        "id": "calc-u2-the-power-comes-down-front",
        "course": "calculus", "unit": 2,
        "topic": "The power rule",
        "op": "pwrc", "max_value": 96,
        "levels": ("abstract",),
        "symbols": ("power rule", "exponent"),
        "advance_line": "Three in a row, and you can say why — you've got it! The exponent comes down and times what is already there.",
        "why": [
            ("Shrinking a window every time would be unbearable, so Calculus finds the "
             "pattern once and keeps it. It is called the power rule, and it turns a whole "
             "limit into two moves: the exponent comes down in front, and the power drops "
             "by one.",
             '[[goal text="The power comes down front"]]'),
        ],
        "picture": [
            ("Here is the rule as a machine. For 6 x to the power 3, the exponent 3 goes "
             "in, it meets the 6 already standing there, and the front number of the "
             "derivative comes out. Watch what the exponent does: it comes down and "
             "times the front.",
             '[[write text="y = 6x^3"]][[machine input="3" rule="× 6" output="18" caption="the exponent 3 comes down and meets the 6 — the front number 18 comes out"]]'),
        ],
        "teach": [
            ("That is the method, and it agrees with what you know. For x squared the 2 "
             "comes down and the power drops to 1, giving 2 x — exactly the twice-the-x "
             "from the last lesson. For 6 x to the power 3: the 3 comes down onto the 6, "
             "giving 18, and the power drops to 2 — 18 x squared.",
             '[[machine input="3" rule="× 6" output="18" caption="3 times 6 is 18, and the power drops to 2"]][[write text="18x^2"]][[step eq="3 × 6 = 18"]]'),
            ("The exponent times the front number, never plus. And leaving the front "
             "number alone means the exponent never came down at all — the one move the "
             "rule is entirely about.",
             '[[step eq="18 ✓"]][[step eq="9 ✗ added · 6 ✗ the exponent stayed up"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. For 9 x to the power 4: the 4 comes "
                        "down onto the 9 — 36.",
                        '[[machine input="4" rule="× 9" output="36" caption="the 4 comes down onto the 9 — 36"]][[write text="36x^3"]][[step eq="4 × 9 = 36"]]'),
             "ask": {"a": 2, "b": 11, "op": "pwrc"}},
            {"worked": ("One more together. 7 x to the power 6: the 6 comes down onto the "
                        "7 — 42, and the power drops to 5.",
                        '[[machine input="6" rule="× 7" output="42" caption="the 6 comes down onto the 7 — 42"]][[write text="42x^5"]][[step eq="6 × 7 = 42"]]'),
             "ask": {"a": 8, "b": 3, "op": "pwrc"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. For 6 x to the power "
                       "3, the derivative\'s front number is 18, not 9. Tap the reason why."),
            "choices": ("because the exponent comes down and times the front number | "
                        "because the exponent and the front number are added | "
                        "because 18 is the biggest number on the board"),
            "answer": "because the exponent comes down and times the front number",
            "board": '[[machine input="3" rule="× 6" output="?" caption="why 18, and not 9?"]]',
        },
        "recap": [
            ("So, here it is again. The power rule: the exponent comes down in front and "
             "times what is already there, and the power drops by one. Adding the two "
             "numbers is no rule, and a front number left alone means the exponent never "
             "came down.",
             '[[machine input="3" rule="× 6" output="18" caption="the exponent comes down front"]]'),
            ("And that is the power rule.",
             '[[step eq="3 × 6 = 18"]]'),
        ],
        "bank": [{"a": a, "b": b, "op": "pwrc"} for a, b in
                 ((2,3),(4,2),(5,2),(3,4),(7,2),(3,5),(2,8),(6,3),(4,5),(3,7))],
    },
    {
        "id": "calc-u2-a-line-has-one-slope",
        "course": "calculus", "unit": 2,
        "topic": "The derivative of a line",
        "op": "cnst", "max_value": 40,
        "levels": ("abstract",),
        "symbols": ("constant", "steepness"),
        "advance_line": "Three in a row, and you can say why — you've got it! A line's slope is the number in front of x.",
        "why": [
            ("Not every derivative changes as you move. A straight line has the same "
             "steepness at every point on it, so its derivative is a constant — one "
             "number, true everywhere along the line. So lines are the easiest "
             "curves in Calculus, and the best place to check the rules agree.",
             '[[goal text="A line has one slope"]]'),
        ],
        "picture": [
            ("Here is y equals 3 x plus 5 on the grid. Look at any step to the right: "
             "the line climbs 3. Take another step, anywhere at all, and it climbs 3 "
             "again. The steepness never changes.",
             '[[graph lines="y=3x+5" points="(1,8),(2,11)" range="0..4" yrange="0..19" caption="one step right, 3 up — the same steepness at every point"]]'),
        ],
        "teach": [
            ("That is the method: read the number sitting in front of x. For y equals 3 "
             "x plus 5, the slope is 3 wherever you stand. Algebra One measured that as "
             "the climb per step across; Calculus calls the same number the derivative, "
             "and the power rule agrees — x to the 1 sends its 1 down onto the 3.",
             '[[graph lines="y=3x+5" points="(1,8),(2,11)" range="0..4" yrange="0..19" caption="the slope is 3, everywhere"]][[step eq="y = 3x + 5"]][[step eq="slope 3, everywhere"]]'),
            ("The 5 does nothing to the steepness — it only lifts the whole line up the "
             "page, and a plain number on its own has a derivative of zero. Read the "
             "number in front of x, and ignore the one standing alone.",
             '[[step eq="3 ✓"]][[step eq="5 ✗ that lifts, not tilts · 8 ✗ added"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. y equals 15 x plus 9 has a slope "
                        "of 15 at every point.",
                        '[[graph lines="y=15x+9" points="(1,24),(2,39)" range="0..4" yrange="0..71" caption="one step right, 15 up"]][[step eq="slope = 15"]]'),
             "ask": {"a": 12, "b": 4, "op": "cnst"}},
            {"worked": ("One more together. The slope of y equals 18 x plus 11 is 18 — "
                        "the number in front of x, the same at every point.",
                        '[[graph lines="y=18x+11" points="(1,29),(2,47)" range="0..4" yrange="0..85" caption="one step right, 18 up"]][[step eq="slope = 18"]]'),
             "ask": {"a": 13, "b": 5, "op": "cnst"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. The derivative of y "
                       "equals 3 x plus 5 is 3, not 5. Tap the reason why."),
            "choices": ("because the number in front of x is the climb per step | "
                        "because the bigger number is always the slope | "
                        "because 5 is the slope and 3 is the height"),
            "answer": "because the number in front of x is the climb per step",
            "board": '[[graph lines="y=3x+5" range="0..4" yrange="0..19" caption="why 3, and not 5?"]]',
        },
        "recap": [
            ("So, here it is again. A line has one slope, the number in front of x, and "
             "that is its derivative everywhere. The number standing alone only lifts "
             "the line and has a derivative of zero.",
             '[[graph lines="y=3x+5" points="(1,8),(2,11)" range="0..4" yrange="0..19" caption="one slope, everywhere"]]'),
            ("And that is the derivative of a line.",
             '[[step eq="slope = 3"]]'),
        ],
        "bank": [{"a": a, "b": b, "op": "cnst"} for a, b in
                 ((2,6),(3,7),(4,2),(5,3),(6,4),(7,5),(8,6),(9,7),(10,2),(11,3))],
    },
    {
        "id": "calc-u2-feed-the-derivative-an-x",
        "course": "calculus", "unit": 2,
        "topic": "Evaluating a derivative",
        "op": "evat", "max_value": 96,
        "levels": ("abstract",),
        "symbols": ("machine", "at x"),
        "advance_line": "Three in a row, and you can say why — you've got it! Work out the derivative, then feed it the x.",
        "why": [
            ("A derivative is not one number — it is a whole new function, a machine "
             "that hands you the slope at whatever x you feed it. So there are two jobs, "
             "in order: get the derivative first, then feed it the x you were asked "
             "about.",
             '[[goal text="Feed the derivative an x"]]'),
        ],
        "picture": [
            ("Here is y equals 5 x squared with the point at x equals 6. The curve is "
             "steeper the further out you stand — look at the tangent at that point. Its "
             "slope is what the derivative hands back when you feed it 6.",
             '[[graph func="5*x^2" names="y = 5x²" lines="y=60x-180" points="(6,180)" range="0..8" yrange="0..320" caption="y = 5 x squared with the tangent at x = 6 — it climbs 60 for every step"]]'),
        ],
        "teach": [
            ("That is the method: for y equals 5 x squared the power rule gives 10 x. "
             "That is the machine. Feed it 2 and it hands back 20; feed it 6 and it hands "
             "back 60 — the same curve, steeper the further out you stand.",
             '[[graph func="5*x^2" names="y = 5x²" lines="y=60x-180" points="(6,180)" range="0..8" yrange="0..320" caption="the machine 10x hands back 60 at x = 6"]][[step eq="y = 5x² · slope = 10x"]][[step eq="at x = 2: 20 · at x = 6: 60"]]'),
            ("Two answers not to give. The curve\'s height at that x is a different "
             "measurement — at 6 the curve sits at 180 while its slope is 60. And 10 is "
             "the machine\'s own front number, before any x was fed in.",
             '[[step eq="60 ✓"]][[step eq="180 ✗ the height · 10 ✗ nothing fed in"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. y equals 6 x squared gives 12 x; "
                        "at x equals 4 the slope is 48.",
                        '[[graph func="6*x^2" names="y = 6x²" lines="y=48x-96" points="(4,96)" range="0..6" yrange="0..216" caption="the tangent at x = 4 climbs 48 for every step"]][[step eq="12 × 4 = 48"]]'),
             "ask": {"a": 3, "b": 0, "c": 7, "op": "evat"}},
            {"worked": ("One more together. y equals 7 x squared gives 14 x, so at x equals "
                        "3 the slope is 14 times 3 — 42.",
                        '[[graph func="7*x^2" names="y = 7x²" lines="y=42x-63" points="(3,63)" range="0..5" yrange="0..175" caption="the tangent at x = 3 climbs 42 for every step"]][[step eq="14 × 3 = 42"]]'),
             "ask": {"a": 3, "b": 0, "c": 8, "op": "evat"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. For y equals 5 x "
                       "squared, the slope at x equals 6 is 60, not 180. Tap the reason why."),
            "choices": ("because the derivative is a machine, and you feed it 6 | "
                        "because the slope is always the height at that x | "
                        "because 180 is too steep for any curve"),
            "answer": "because the derivative is a machine, and you feed it 6",
            "board": '[[graph func="5*x^2" names="y = 5x²" points="(6,180)" range="0..8" yrange="0..320" caption="why 60, and not 180?"]]',
        },
        "recap": [
            ("So, here it is again. A derivative is a machine: work it out first, then "
             "feed it the x, and it hands back the slope at that point. The height of the "
             "curve there is a different measurement, and the machine\'s front number "
             "on its own has had nothing fed in.",
             '[[graph func="5*x^2" names="y = 5x²" lines="y=60x-180" points="(6,180)" range="0..8" yrange="0..320" caption="feed the derivative an x"]]'),
            ("And that is evaluating a derivative.",
             '[[step eq="10 × 6 = 60"]]'),
        ],
        "bank": [{"a": a, "b": 0, "c": c, "op": "evat"} for a, c in
                 ((2,3),(2,4),(3,3),(2,5),(2,6),(2,7),(3,5),(2,8),(2,9),(4,5))],
    },
]
LESSONS.extend(_CALCULUS_U2)

# =============================================================================
# CALCULUS UNIT 3 -- Product, Quotient & Chain Rules (build lv)
# The thread: DERIVATIVES OF THINGS BUILT FROM OTHER THINGS. The product rule
# agrees with multiplying out first, the chain rule brings the INSIDE's
# derivative out too (forgetting it is the commonest mistake in Calculus), and
# a plain number on the bottom needs no quotient rule at all.
# =============================================================================
_CALCULUS_U3 = [
    {
        "id": "calc-u3-two-things-multiplied",
        "course": "calculus", "unit": 3,
        "topic": "The product rule",
        "op": "prod", "max_value": 40,
        "levels": ("abstract",),
        "symbols": ("product", "expand"),
        "advance_line": "Three in a row, and you can say why — you've got it! Feed the x into the derivative you worked out.",
        "why": [
            ("What is the derivative of two functions multiplied together? Not the two "
             "derivatives multiplied — that is the tempting guess, and it is wrong. There "
             "is a rule for it, and the surest way to believe the rule is to check it "
             "against expanding first, which you can already do.",
             '[[goal text="Two things multiplied"]]'),
        ],
        "picture": [
            ("Here is y equals x times the quantity x plus 4, with the point at x equals "
             "5. Look at the tangent touching the curve there — its steepness is what we "
             "are after, and it climbs 14 for every step across.",
             '[[graph func="x*(x+4)" names="y = x(x + 4)" lines="y=14x-25" points="(5,45)" range="0..7" yrange="0..77" caption="y = x times (x + 4) with the tangent at x = 5 — it climbs 14 for every step"]]'),
        ],
        "teach": [
            ("That is the method: expand it, then differentiate what you know. x times the "
             "quantity x plus 4 is x squared plus 4 x, whose derivative is 2 x plus 4. The "
             "product rule gives the very same answer without expanding, which matters "
             "when the pieces are too ugly to expand.",
             '[[graph func="x*(x+4)" names="y = x(x + 4)" lines="y=14x-25" points="(5,45)" range="0..7" yrange="0..77" caption="the slope at x = 5 is 2 times 5 plus 4"]][[step eq="x² + 4x · slope = 2x + 4"]]'),
            ("Then feed in the x you were asked about. At x equals 5 the slope is 10 "
             "plus 4 — 14. The curve\'s height there is 5 times 9, which is 45, and 10 "
             "is only half the derivative, with the second piece forgotten.",
             '[[step eq="2(5) + 4 = 14 ✓"]][[step eq="45 ✗ the height · 10 ✗ half of it"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. y equals x times x plus 9: the "
                        "slope is 2 x plus 9, and at x equals 8 that is 25.",
                        '[[graph func="x*(x+9)" names="y = x(x + 9)" lines="y=25x-64" points="(8,136)" range="0..10" yrange="0..190" caption="the tangent at x = 8 climbs 25 for every step"]][[step eq="2(8) + 9 = 25"]]'),
             "ask": {"a": 6, "b": 0, "c": 5, "op": "prod"}},
            {"worked": ("One more together. With x plus 11 inside, the slope is 2 x plus 11, "
                        "and at x equals 7 that is 14 plus 11 — 25.",
                        '[[graph func="x*(x+11)" names="y = x(x + 11)" lines="y=25x-49" points="(7,126)" range="0..9" yrange="0..180" caption="the tangent at x = 7 climbs 25 for every step"]][[step eq="2(7) + 11 = 25"]]'),
             "ask": {"a": 5, "b": 0, "c": 6, "op": "prod"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. For x times the "
                       "quantity x plus 4, the slope at x equals 5 is 14, not 45. Tap the "
                       "reason why."),
            "choices": ("because 5 is fed into the derivative, 2 x plus 4 | "
                        "because the slope is always the height of the curve | "
                        "because 45 is the two derivatives multiplied"),
            "answer": "because 5 is fed into the derivative, 2 x plus 4",
            "board": '[[graph func="x*(x+4)" names="y = x(x + 4)" points="(5,45)" range="0..7" yrange="0..77" caption="why 14, and not 45?"]]',
        },
        "recap": [
            ("So, here it is again. Two things multiplied: expand if you can, "
             "differentiate what you know, then feed in the x. The product rule gives "
             "the same answer without expanding. The height of the curve is not its "
             "slope, and half the derivative is not the derivative.",
             '[[graph func="x*(x+4)" names="y = x(x + 4)" lines="y=14x-25" points="(5,45)" range="0..7" yrange="0..77" caption="the tangent at x = 5"]]'),
            ("And that is the product rule, checked.",
             '[[step eq="2(5) + 4 = 14"]]'),
        ],
        "bank": [{"a": a, "b": 0, "c": c, "op": "prod"} for a, c in
                 ((2,2),(3,2),(2,3),(5,2),(6,2),(5,3),(6,3),(5,4),(6,4),(5,5))],
    },
    {
        "id": "calc-u3-do-not-forget-the-inside",
        "course": "calculus", "unit": 3,
        "topic": "The chain rule",
        "op": "chan", "max_value": 81,
        "levels": ("abstract",),
        "symbols": ("chain rule", "inside"),
        "advance_line": "Three in a row, and you can say why — you've got it! The power comes down AND the inside's derivative comes out.",
        "why": [
            ("Pre-Calculus fed one machine into another and called it composition. "
             "Differentiating one of those needs the chain rule, and it says: "
             "differentiate the outside, then times by the derivative of the inside. "
             "Forgetting that second half is the commonest mistake in all of Calculus.",
             '[[goal text="Do not forget the inside"]]'),
        ],
        "picture": [
            ("Here is the chain rule as a machine. For the quantity 5 x plus 3, raised to "
             "the power 6, the power 6 goes in. But the inside, 5 x plus 3, has its own "
             "derivative — 5 — and that comes out too. Watch the two meet.",
             '[[write text="y = (5x + 3)^6"]][[machine input="6" rule="× 5" output="30" caption="the power 6 comes down and the inside\'s 5 comes out — they meet at 30"]]'),
        ],
        "teach": [
            ("That is the method: the outside is something to the 6, so the 6 comes down. "
             "The inside gives 5, and that comes out as well. Front number: 6 times 5, "
             "which is 30.",
             '[[machine input="6" rule="× 5" output="30" caption="6 times 5 is 30 — both came down"]][[step eq="6 comes down · inside gives 5 · 6 × 5 = 30"]]'),
            ("Forgetting the inside leaves 6 and is the commonest mistake in all of "
             "Calculus — it quietly assumes the inside was just x. Whenever something sits "
             "inside something else, its derivative must come out as well.",
             '[[step eq="30 ✓"]][[step eq="6 ✗ inside forgotten · 11 ✗ added"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. The quantity 7 x plus 3 to the "
                        "power 5: the 5 comes down and meets the inside\'s 7 — 35.",
                        '[[machine input="5" rule="× 7" output="35" caption="the 5 comes down and meets the inside\'s 7 — 35"]][[step eq="5 × 7 = 35"]]'),
             "ask": {"a": 8, "b": 3, "op": "chan"}},
            {"worked": ("One more together. 6 x plus 3, to the power 7: the 7 comes down "
                        "and the inside\'s 6 comes out — 7 times 6 is 42.",
                        '[[machine input="7" rule="× 6" output="42" caption="the 7 meets the inside\'s 6 — 42"]][[step eq="7 × 6 = 42"]]'),
             "ask": {"a": 9, "b": 3, "op": "chan"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. For 5 x plus 3 to the "
                       "power 6, the front number is 30, not 6. Tap the reason why."),
            "choices": ("because the inside has a derivative, and it comes out too | "
                        "because the power is always multiplied by five | "
                        "because 6 and 5 are added to make 30"),
            "answer": "because the inside has a derivative, and it comes out too",
            "board": '[[machine input="6" rule="× 5" output="?" caption="why 30, and not 6?"]]',
        },
        "recap": [
            ("So, here it is again. The chain rule: differentiate the outside, then times "
             "by the derivative of the inside. Both come down. Forgetting the inside is "
             "the commonest mistake in Calculus, and adding the two is no rule at all.",
             '[[machine input="6" rule="× 5" output="30" caption="the power AND the inside"]]'),
            ("And that is the chain rule.",
             '[[step eq="6 × 5 = 30"]]'),
        ],
        "bank": [{"a": a, "b": b, "op": "chan"} for a, b in
                 ((2,3),(4,2),(5,2),(3,4),(7,2),(3,5),(2,8),(6,3),(4,5),(3,7))],
    },
    {
        "id": "calc-u3-the-chain-rule-at-a-point",
        "course": "calculus", "unit": 3,
        "topic": "Using the chain rule",
        "op": "chev", "max_value": 96,
        "levels": ("abstract",),
        "symbols": ("squared", "inside"),
        "advance_line": "Three in a row, and you can say why — you've got it! Twice the inside, times the inside's derivative.",
        "why": [
            ("Now use the chain rule on a real number. For the quantity 4 x plus 7, "
             "squared, the rule gives: 2, times the quantity itself, times the inside\'s "
             "derivative 4. Feed in an x and the slope at that point drops out — a "
             "number you can draw.",
             '[[goal text="The chain rule at a point"]]'),
        ],
        "picture": [
            ("Here is y equals the quantity 4 x plus 7, squared, with the point at x "
             "equals zero. Look at the tangent there — it climbs 56 for every step "
             "across. That steepness is what the chain rule computes.",
             '[[graph func="(4*x+7)^2" names="y = (4x + 7)²" lines="y=56x+49" points="(0,49)" range="-1..2" yrange="0..225" caption="y = (4x + 7) squared with the tangent at x = 0 — it climbs 56 for every step"]]'),
        ],
        "teach": [
            ("That is the method: work the inside out first, then let the two outside "
             "numbers do their work. At x equals zero the inside is just 7, because the "
             "4 x vanishes. So the slope is 2 times 7 times 4 — 56.",
             '[[graph func="(4*x+7)^2" names="y = (4x + 7)²" lines="y=56x+49" points="(0,49)" range="-1..2" yrange="0..225" caption="2 times 7 times 4 is 56"]][[step eq="slope = 2(4x + 7)·4"]][[step eq="inside = 7 · 2 × 7 × 4 = 56"]]'),
            ("Two slips. 49 is the curve\'s height at zero, the inside squared, not its "
             "steepness. And 14 keeps the 2 and the inside but drops the 4 — the inside\'s "
             "own derivative, which is the whole reason the chain rule exists.",
             '[[step eq="56 ✓"]][[step eq="49 ✗ the height · 14 ✗ the 4 dropped"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. The quantity 4 x plus 9, squared: "
                        "at zero the slope is 2 times 9 times 4 — 72.",
                        '[[graph func="(4*x+9)^2" names="y = (4x + 9)²" lines="y=72x+81" points="(0,81)" range="-1..2" yrange="0..289" caption="the tangent at x = 0 climbs 72 for every step"]][[step eq="2 × 9 × 4 = 72"]]'),
             "ask": {"a": 8, "b": 3, "op": "chev"}},
            {"worked": ("One more together. With 7 inside and a multiplier of 5: 2 times 7 "
                        "times 5 — the slope at zero is 70.",
                        '[[graph func="(5*x+7)^2" names="y = (5x + 7)²" lines="y=70x+49" points="(0,49)" range="-1..2" yrange="0..289" caption="the tangent at x = 0 climbs 70 for every step"]][[step eq="2 × 7 × 5 = 70"]]'),
             "ask": {"a": 9, "b": 3, "op": "chev"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. For 4 x plus 7 "
                       "squared, the slope at zero is 56, not 14. Tap the reason why."),
            "choices": ("because the inside\'s derivative 4 comes out and times the rest | "
                        "because the slope at zero is always the inside squared | "
                        "because 14 is the height of the curve"),
            "answer": "because the inside\'s derivative 4 comes out and times the rest",
            "board": '[[graph func="(4*x+7)^2" names="y = (4x + 7)²" points="(0,49)" range="-1..2" yrange="0..225" caption="why 56, and not 14?"]]',
        },
        "recap": [
            ("So, here it is again. The chain rule at a point: work the inside out first, "
             "then 2 times the inside times the inside\'s derivative. The height at that "
             "point is the inside squared, not the slope, and dropping the inside\'s "
             "derivative drops the whole point of the rule.",
             '[[graph func="(4*x+7)^2" names="y = (4x + 7)²" lines="y=56x+49" points="(0,49)" range="-1..2" yrange="0..225" caption="the tangent at x = 0"]]'),
            ("And that is the chain rule, fed a number.",
             '[[step eq="2 × 7 × 4 = 56"]]'),
        ],
        "bank": [{"a": a, "b": b, "op": "chev"} for a, b in
                 ((2,3),(2,5),(3,4),(2,7),(3,5),(2,8),(6,3),(4,5),(3,7),(2,11))],
    },
    {
        "id": "calc-u3-a-number-underneath",
        "course": "calculus", "unit": 3,
        "topic": "A constant denominator",
        "op": "quot", "max_value": 60,
        "levels": ("abstract",),
        "symbols": ("underneath", "divides"),
        "advance_line": "Three in a row, and you can say why — you've got it! Differentiate the top, and the number underneath keeps dividing.",
        "why": [
            ("There is a quotient rule for one function divided by another, and it is "
             "fiddly. But most fractions in practice have a plain number underneath, "
             "and those need no rule at all. A number underneath just divides "
             "everything, before or after, and the answer comes out the same.",
             '[[goal text="A number underneath"]]'),
        ],
        "picture": [
            ("Here is 12 x squared over 4 as a machine. The front number 12 goes in. The "
             "power rule doubles it, and the 4 underneath divides it. Watch the front "
             "number of the derivative come out the other side.",
             '[[write text="y = 12x² ÷ 4"]][[machine input="12" rule="× 2, then ÷ 4" output="6" caption="12 doubled is 24, and 24 over 4 is 6 — the number underneath came along for the ride"]]'),
        ],
        "teach": [
            ("That is the method: differentiate the top, then divide by the number "
             "underneath. For 12 x squared over 4: the top gives 24 x, and 24 over 4 is "
             "6 — so the derivative is 6 x. The number underneath simply came along.",
             '[[machine input="12" rule="× 2, then ÷ 4" output="6" caption="24 over 4 is 6"]][[step eq="12x² → 24x"]][[step eq="24 ÷ 4 = 6"]]'),
            ("The slip is dividing without differentiating: 12 over 4 is 3, which "
             "forgets that the power rule doubles the front number first. And timesing "
             "the two numbers is no rule at all. Differentiate the top; keep dividing "
             "underneath.",
             '[[step eq="6 ✓"]][[step eq="3 ✗ the doubling forgotten · 48 ✗ timesed"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 45 x squared over 9: the top gives "
                        "90 x, and 90 over 9 is 10.",
                        '[[machine input="45" rule="× 2, then ÷ 9" output="10" caption="90 over 9 is 10"]][[step eq="90 ÷ 9 = 10"]]'),
             "ask": {"a": 22, "b": 2, "op": "quot"}},
            {"worked": ("One more together. 55 x squared over 11: the top gives 110 x, and "
                        "110 over 11 is 10 — the 11 underneath just kept dividing.",
                        '[[machine input="55" rule="× 2, then ÷ 11" output="10" caption="110 over 11 is 10"]][[step eq="110 ÷ 11 = 10"]]'),
             "ask": {"a": 24, "b": 2, "op": "quot"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. For 12 x squared over "
                       "4, the derivative\'s front number is 6, not 3. Tap the reason why."),
            "choices": ("because the top is differentiated before the 4 divides it | "
                        "because a number underneath always halves the answer | "
                        "because 12 over 4 is 6"),
            "answer": "because the top is differentiated before the 4 divides it",
            "board": '[[machine input="12" rule="× 2, then ÷ 4" output="?" caption="why 6, and not 3?"]]',
        },
        "recap": [
            ("So, here it is again. A plain number underneath needs no quotient rule: "
             "differentiate the top, and the number underneath keeps dividing. Dividing "
             "without differentiating forgets the doubling, and timesing the two numbers "
             "is no rule at all.",
             '[[machine input="12" rule="× 2, then ÷ 4" output="6" caption="the number underneath keeps dividing"]]'),
            ("And that is a constant denominator.",
             '[[step eq="24 ÷ 4 = 6"]]'),
        ],
        "bank": [{"a": a, "b": b, "op": "quot"} for a, b in
                 ((2,2),(6,3),(9,3),(20,5),(30,6),(42,7),(14,2),(24,3),(36,4),(50,5))],
    },
]
LESSONS.extend(_CALCULUS_U3)
# =============================================================================
# CALCULUS UNIT 4 -- Applications of Derivatives (build lw)
# The thread: A DERIVATIVE IS A TOOL, not an exercise. Solve it backwards for a
# time, watch one rate drive another, find where a curve levels off, and
# differentiate twice to get at acceleration.
# =============================================================================
_CALCULUS_U4 = [
    {
        "id": "calc-u4-when-is-it-going-that-fast",
        "course": "calculus", "unit": 4,
        "topic": "Solving with a derivative",
        "op": "vsol", "max_value": 300,
        "levels": ("abstract",),
        "symbols": ("speed", "solve"),
        "advance_line": "Three in a row, and you can say why — you've got it! Set the speed equal and solve for the time.",
        "why": [
            ("Unit Four puts derivatives to work. A derivative is an equation like any "
             "other, and equations can be solved. If a falling stone's speed is 8 t "
             "metres a second, asking WHEN it falls at 40 is just asking what t turns "
             "8 t into 40. That is the derivative run backwards, from a speed to a moment.",
             '[[goal text="When is it going that fast?"]]'),
        ],
        "picture": [
            ("Here is the speed as a line: 8 metres a second faster with every second "
             "that passes. Somewhere along that line the speed reaches 40. Find the "
             "height 40 on the side, run your finger across to the line, and drop down "
             "to the time underneath — that moment is what the question wants.",
             '[[graph lines="y=8x" names="speed = 8t" range="0..7" yrange="0..56" caption="the speed line — 8 faster every second; somewhere along it the speed is 40"]]'),
        ],
        "teach": [
            ("That is the method: set the speed equal to the number and solve. 8 t "
             "equals 40, so t is 40 over 8 — 5 seconds. On the picture the line meets "
             "the height 40 exactly at t equals 5. The derivative told you the speed at "
             "any time; solving it runs that knowledge backwards to the moment.",
             '[[graph lines="y=8x; y=40" names="speed = 8t; speed = 40" points="(5,40)" range="0..7" yrange="0..56" caption="the line meets 40 at t = 5"]][[step eq="8t = 40"]][[step eq="t = 5 seconds"]]'),
            ("Watch which number you divide by. The speed's front number is DOUBLE the "
             "distance's, so dividing by the distance's number gives the wrong time — "
             "and handing back 40 answers with a speed when a time was asked for.",
             '[[step eq="5 ✓"]][[step eq="40 ✗ that is the speed · 10 ✗ wrong divisor"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Speed 12 t, asked when it reaches "
                        "84: 12 t equals 84, so t is 84 over 12 — 7 seconds.",
                        '[[graph lines="y=12x; y=84" names="speed = 12t; speed = 84" points="(7,84)" range="0..9" yrange="0..108" caption="the speed line meets 84 at t = 7"]][[step eq="12t = 84"]][[step eq="t = 7"]]'),
             "ask": {"a": 6, "b": 144, "op": "vsol"}},
            {"worked": ("One more together. Speed 18 t reaching 162: 18 t equals 162, and "
                        "162 over 18 is 9 seconds — the moment the line reaches that height.",
                        '[[graph lines="y=18x; y=162" names="speed = 18t; speed = 162" points="(9,162)" range="0..11" yrange="0..198" caption="the speed line meets 162 at t = 9"]][[step eq="18t = 162"]][[step eq="t = 9"]]'),
             "ask": {"a": 7, "b": 182, "op": "vsol"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A speed of 8 t reaches "
                       "40 at t equals 5, not at 40. Tap the reason why."),
            "choices": ("because the speed is set equal to 40 and solved for t | "
                        "because the time is always the speed you were given | "
                        "because 40 is divided by the distance's number"),
            "answer": "because the speed is set equal to 40 and solved for t",
            "board": '[[graph lines="y=8x" names="speed = 8t" range="0..7" yrange="0..56" caption="why 5, and not 40?"]]',
        },
        "recap": [
            ("So, here it is again. A derivative can be solved like any other equation: "
             "set the speed equal to the number you were given and solve for the time. "
             "The speed is not the time, and the number you divide by is the speed's "
             "front number, not the distance's.",
             '[[graph lines="y=8x; y=40" names="speed = 8t; speed = 40" points="(5,40)" range="0..7" yrange="0..56" caption="set the speed equal and solve"]]'),
            ("And that is how a derivative answers WHEN.",
             '[[step eq="8t = 40 · t = 5"]]'),
        ],
        "bank": [{"a": a, "b": b, "op": "vsol"} for a, b in
                 ((2,8),(3,18),(4,32),(5,50),(6,72),(7,98),(2,32),(3,54),(4,80),(5,110))],
    },
    {
        "id": "calc-u4-one-rate-drives-another",
        "course": "calculus", "unit": 4,
        "topic": "Related rates",
        "op": "mrat", "max_value": 96,
        "levels": ("abstract",),
        "symbols": ("growing", "area"),
        "advance_line": "Three in a row, and you can say why — you've got it! Twice the side, times the side's own rate.",
        "why": [
            ("Here is what derivatives are really for. A square's side is growing "
             "steadily — and its area is growing too, but not steadily at all, because "
             "a bigger square gains more area from the same extra centimetre. One rate "
             "drives another, and the chain rule says exactly how.",
             '[[goal text="One rate drives another"]]'),
        ],
        "picture": [
            ("Here is the area against the side: y equals x squared. Look how the curve "
             "steepens as the side grows. At a side of 15 the curve is already climbing "
             "hard — so the same steady growth in the side pours more and more area in.",
             '[[graph func="x^2" names="area = side²" points="(15,225)" range="0..18" yrange="0..324" caption="area against side — the curve steepens as the square grows"]]'),
        ],
        "teach": [
            ("That is the method: area is side squared, so the chain rule applies — the "
             "area's rate is 2, times the side, times the side's own rate. With a side "
             "of 15 growing at 3 centimetres a second, the area gains 2 times 15 times "
             "3 — 90 square centimetres every second. The tangent shows it climbing.",
             '[[graph func="x^2" names="area = side²" lines="y=30x-225" points="(15,225)" range="0..18" yrange="0..324" caption="the tangent at a side of 15 climbs 30 for every centimetre — times the rate 3, that is 90 a second"]][[step eq="2 × 15 × 3 = 90 cm² per second"]]'),
            ("And when that same square reaches a side of 50, the area gains 300 a "
             "second from the very same steady growth. So do not hand back 3, the "
             "side's rate, or 225, the area itself — the question asks how fast the "
             "area CHANGES.",
             '[[step eq="90 ✓"]][[step eq="3 ✗ the side\'s rate · 225 ✗ the area"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. A side of 12 growing at 3: the "
                        "area gains 2 times 12 times 3 — 72 a second.",
                        '[[graph func="x^2" names="area = side²" lines="y=24x-144" points="(12,144)" range="0..15" yrange="0..225" caption="the tangent at 12 climbs 24 — times 3, that is 72"]][[step eq="2 × 12 × 3 = 72"]]'),
             "ask": {"a": 11, "b": 2, "op": "mrat"}},
            {"worked": ("One more together. A side of 9 growing at 5: 2 times 9 times 5 — "
                        "90 square centimetres a second, read off the tangent at 9.",
                        '[[graph func="x^2" names="area = side²" lines="y=18x-81" points="(9,81)" range="0..12" yrange="0..144" caption="the tangent at 9 climbs 18 — times 5, that is 90"]][[step eq="2 × 9 × 5 = 90"]]'),
             "ask": {"a": 6, "b": 4, "op": "mrat"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A side of 15 growing at "
                       "3 has the area growing at 90, not 3. Tap the reason why."),
            "choices": ("because the area's rate is twice the side times the side's rate | "
                        "because the area grows at the same rate as the side | "
                        "because the area itself is the rate"),
            "answer": "because the area's rate is twice the side times the side's rate",
            "board": '[[graph func="x^2" names="area = side²" points="(15,225)" range="0..18" yrange="0..324" caption="why 90, and not 3?"]]',
        },
        "recap": [
            ("So, here it is again. When one thing grows, everything built from it grows "
             "too, and the chain rule says how fast: the area's rate is 2 times the side "
             "times the side's rate. Never hand back the side's rate alone, and never "
             "the area itself.",
             '[[graph func="x^2" names="area = side²" lines="y=30x-225" points="(15,225)" range="0..18" yrange="0..324" caption="one rate drives another"]]'),
            ("And that is a related rate.",
             '[[step eq="2 × side × side\'s rate"]]'),
        ],
        "bank": [{"a": a, "b": b, "op": "mrat"} for a, b in
                 ((3,2),(3,3),(5,2),(3,4),(7,2),(3,5),(8,2),(3,6),(10,2),(7,3))],
    },
    {
        "id": "calc-u4-where-the-curve-levels-off",
        "course": "calculus", "unit": 4,
        "topic": "Critical points",
        "op": "crit", "max_value": 40,
        "levels": ("abstract",),
        "symbols": ("flat", "turn"),
        "advance_line": "Three in a row, and you can say why — you've got it! Set the slope to zero and solve.",
        "why": [
            ("A smooth curve can only turn around where it is momentarily flat — where "
             "its slope is exactly zero. Find those points and you have found every peak "
             "and every valley the curve owns. That is how calculus finds the top and "
             "the bottom of anything.",
             '[[goal text="Where the curve levels off"]]'),
        ],
        "picture": [
            ("Here is y equals x squared take away 6 x — a valley. Run your eye along "
             "the bottom: the curve comes down, goes flat for one instant, and climbs "
             "away again. That flat instant is where it turns, and the slope there is "
             "zero.",
             '[[graph func="x^2-6*x" names="y = x² − 6x" range="0..6" yrange="-11..2" caption="the valley — flat for one instant at the bottom"]]'),
        ],
        "teach": [
            ("That is the method: differentiate, set the slope to zero, solve. The slope "
             "of x squared take away 6 x is 2 x take away 6. Set it to zero: 2 x equals "
             "6, so x is 3. At x equals 3 the curve stops falling and starts rising — "
             "the bottom of the valley, 9 below the axis.",
             '[[graph func="x^2-6*x" names="y = x² − 6x; the flat tangent" lines="y=-9" points="(3,-9)" range="0..6" yrange="-11..2" caption="flat at x = 3 — the bottom of the valley"]][[step eq="2x − 6 = 0"]][[step eq="x = 3"]]'),
            ("The number in the slope is not the answer to the question. 6 is what you "
             "set 2 x equal TO; the x that solves it is half of that. Halve, do not "
             "double, and do not simply repeat what you were given.",
             '[[step eq="3 ✓"]][[step eq="6 ✗ the slope\'s number · 12 ✗ doubled"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Slope 2 x take away 30: zero at "
                        "x equals 15, the bottom of that valley.",
                        '[[graph func="x^2-30*x" names="y = x² − 30x; the flat tangent" lines="y=-225" points="(15,-225)" range="0..30" yrange="-281..56" caption="flat at x = 15"]][[step eq="2x = 30"]][[step eq="x = 15"]]'),
             "ask": {"a": 24, "b": 0, "op": "crit"}},
            {"worked": ("One more together. A slope of 2 x take away 34: set it to zero, so "
                        "2 x equals 34 and x is 17 — the curve levels off there.",
                        '[[graph func="x^2-34*x" names="y = x² − 34x; the flat tangent" lines="y=-289" points="(17,-289)" range="0..34" yrange="-361..72" caption="flat at x = 17"]][[step eq="2x = 34"]][[step eq="x = 17"]]'),
             "ask": {"a": 26, "b": 0, "op": "crit"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. For x squared take away "
                       "6 x, the curve levels off at x equals 3, not 6. Tap the reason why."),
            "choices": ("because the slope 2x minus 6 is zero when x is 3 | "
                        "because the curve levels off at the slope's own number | "
                        "because the flat point is always twice the number"),
            "answer": "because the slope 2x minus 6 is zero when x is 3",
            "board": '[[graph func="x^2-6*x" names="y = x² − 6x" range="0..6" yrange="-11..2" caption="why 3, and not 6?"]]',
        },
        "recap": [
            ("So, here it is again. A smooth curve turns only where it is flat, and flat "
             "means a slope of zero: differentiate, set the slope to zero, and solve. "
             "The number in the slope is what you set 2 x equal to — the answer is half "
             "of it, never the number itself and never double.",
             '[[graph func="x^2-6*x" names="y = x² − 6x; the flat tangent" lines="y=-9" points="(3,-9)" range="0..6" yrange="-11..2" caption="where the slope is zero, the curve turns"]]'),
            ("And that is a critical point.",
             '[[step eq="2x − 6 = 0 · x = 3"]]'),
        ],
        "bank": [{"a": v, "b": 0, "op": "crit"} for v in
                 (4, 8, 10, 12, 14, 16, 18, 20, 22)],
    },
    {
        "id": "calc-u4-differentiate-twice",
        "course": "calculus", "unit": 4,
        "topic": "The second derivative",
        "op": "acce", "max_value": 96,
        "levels": ("abstract",),
        "symbols": ("acceleration", "twice"),
        "advance_line": "Three in a row, and you can say why — you've got it! Differentiate the speed to get the acceleration.",
        "why": [
            ("Differentiating does not have to stop after one go. Distance differentiates "
             "into speed; differentiate the SPEED and you get acceleration — how fast the "
             "speed itself is changing. Differentiate twice, and a falling stone hands "
             "you gravity.",
             '[[goal text="Differentiate twice"]]'),
        ],
        "picture": [
            ("Here is the speed of a stone that has fallen 5 t squared metres: its speed "
             "is 10 t, a straight line. Look at the line, not the stone. It climbs the "
             "same amount every second — and that steady climb, the slope of the speed "
             "line, is the acceleration.",
             '[[graph lines="y=10x" names="speed = 10t" range="0..5" yrange="0..50" caption="the speed line — it climbs the same amount every second"]]'),
        ],
        "teach": [
            ("That is the method: differentiate the speed. 10 t is a line, and a line's "
             "derivative is its front number — 10. So the acceleration is a flat 10, the "
             "same at every moment of the fall: one second on, the speed is 10 higher, "
             "and one second after that, 10 higher again.",
             '[[graph lines="y=10x" names="speed = 10t" points="(1,10),(2,20)" range="0..5" yrange="0..50" caption="one second on, 10 faster — the acceleration is 10"]][[step eq="5t² → 10t → 10"]]'),
            ("That constant is gravity, and finding it took two differentiations. "
             "Stopping after one leaves 5, the distance's own number, and doubling twice "
             "over gives 20 — one differentiation too many.",
             '[[step eq="10 ✓"]][[step eq="5 ✗ one step short · 20 ✗ one step too far"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Falling 30 t squared gives speed "
                        "60 t, so the acceleration is 60.",
                        '[[graph lines="y=60x" names="speed = 60t" points="(1,60),(2,120)" range="0..5" yrange="0..300" caption="one second on, 60 faster — the acceleration is 60"]][[step eq="30t² → 60t → 60"]]'),
             "ask": {"a": 12, "b": 0, "op": "acce"}},
            {"worked": ("One more together. 40 t squared gives speed 80 t, and the speed "
                        "line climbs 80 every second, so the acceleration is 80.",
                        '[[graph lines="y=80x" names="speed = 80t" points="(1,80),(2,160)" range="0..5" yrange="0..400" caption="one second on, 80 faster — the acceleration is 80"]][[step eq="40t² → 80t → 80"]]'),
             "ask": {"a": 13, "b": 0, "op": "acce"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A stone falling 5 t "
                       "squared has acceleration 10, not 5. Tap the reason why."),
            "choices": ("because the speed 10t differentiates once more to 10 | "
                        "because the acceleration is the distance's own number | "
                        "because the speed is doubled twice over"),
            "answer": "because the speed 10t differentiates once more to 10",
            "board": '[[graph lines="y=10x" names="speed = 10t" range="0..5" yrange="0..50" caption="why 10, and not 5?"]]',
        },
        "recap": [
            ("So, here it is again. Distance differentiates into speed, and speed "
             "differentiates into acceleration — two goes, not one. The speed is a line "
             "and its derivative is its front number, the same at every moment. Stop one "
             "short and you have the distance's number; go one too far and you have "
             "doubled it again.",
             '[[graph lines="y=10x" names="speed = 10t" points="(1,10),(2,20)" range="0..5" yrange="0..50" caption="differentiate twice"]]'),
            ("And that is the second derivative.",
             '[[step eq="distance → speed → acceleration"]]'),
        ],
        "bank": [{"a": v, "b": 0, "op": "acce"} for v in
                 (2, 3, 4, 6, 7, 8, 9, 10, 11)],
    },
]
LESSONS.extend(_CALCULUS_U4)

# =============================================================================
# CALCULUS UNIT 5 -- Curve Sketching & Optimization (build lw)
# The thread: THE BEST ANSWER SITS WHERE THE SLOPE IS ZERO. The most famous
# optimisation there is (a fixed fence wants a square), the area that wins,
# the same truth in plain numbers, and the second derivative finding where the
# BEND changes rather than the slope.
# =============================================================================
_CALCULUS_U5 = [
    {
        "id": "calc-u5-the-best-rectangle",
        "course": "calculus", "unit": 5,
        "topic": "Optimisation",
        "op": "optr", "max_value": 88,
        "levels": ("abstract",),
        "symbols": ("optimisation", "fence"),
        "advance_line": "Three in a row, and you can say why — you've got it! A fixed fence wants a square.",
        "why": [
            ("Unit Five is about optimisation — asking for the BEST — and calculus finds "
             "the best where the slope is zero. The oldest question of the kind: with a "
             "fixed length of fence, what rectangle encloses the most ground?",
             '[[goal text="The best rectangle"]]'),
        ],
        "picture": [
            ("Here are 40 metres of fence as a tape, cut into the four sides of a "
             "rectangle. Every side takes a share, and the shares must add to 40. Make "
             "one pair long and the other pair goes short — a long thin strip with "
             "almost nothing inside it.",
             '[[tape parts="?|?|?|?" total="40 m of fence" caption="40 metres of fence shared into four sides — which shares enclose the most?"]]'),
        ],
        "teach": [
            ("That is the method: write the area in terms of one side, differentiate, "
             "set the slope to zero — and out comes a side of 10. Four tens use the fence "
             "exactly, so the winner is a square, 10 by 10. Walk round it and the fence "
             "is all used up.",
             '[[rectangle w="10" h="10" show="perimeter" caption="a square of side 10 — the walk round it is the whole 40"]][[step eq="40 ÷ 4 = 10 m each side"]]'),
            ("Every fixed fence wants a square; long thin rectangles waste their fence "
             "on length and enclose almost nothing. So share the fence four ways. Half "
             "of it is two sides at once, and the whole 40 is no side at all.",
             '[[step eq="10 ✓"]][[step eq="20 ✗ two sides · 40 ✗ the whole fence"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 72 metres of fence: each side of "
                        "the best rectangle is 18 — a square.",
                        '[[rectangle w="18" h="18" show="perimeter" caption="a square of side 18 uses the 72 exactly"]][[step eq="72 ÷ 4 = 18"]]'),
             "ask": {"a": 56, "b": 0, "op": "optr"}},
            {"worked": ("One more together. 84 metres of fence, shared four ways — sides of "
                        "21, and the walk round the square uses every metre.",
                        '[[tape parts="21|21|21|21" total="84 m of fence" caption="84 shared four ways — 21 a side"]][[step eq="84 ÷ 4 = 21"]]'),
             "ask": {"a": 60, "b": 0, "op": "optr"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 40 metres of fence "
                       "encloses the most as a square of side 10, not 20. Tap the reason why."),
            "choices": ("because the fence is shared equally among four sides | "
                        "because half the fence is one side | "
                        "because a long thin rectangle holds the most"),
            "answer": "because the fence is shared equally among four sides",
            "board": '[[tape parts="?|?|?|?" total="40 m of fence" caption="why 10, and not 20?"]]',
        },
        "recap": [
            ("So, here it is again. With a fixed fence, the rectangle that encloses the "
             "most is a square: share the fence four ways, and each share is one side. "
             "Half the fence is two sides, and the whole fence is no side at all.",
             '[[rectangle w="10" h="10" show="perimeter" caption="a fixed fence wants a square"]]'),
            ("And that is optimisation.",
             '[[step eq="40 ÷ 4 = 10"]]'),
        ],
        "bank": [{"a": v, "b": 0, "op": "optr"} for v in
                 (16, 20, 24, 28, 32, 36, 44, 48, 52)],
    },
    {
        "id": "calc-u5-and-how-much-ground-that-wins",
        "course": "calculus", "unit": 5,
        "topic": "The best area",
        "op": "maxa", "max_value": 484,
        "levels": ("abstract",),
        "symbols": ("square metres", "encloses"),
        "advance_line": "Three in a row, and you can say why — you've got it! Square the winning side to get the ground it encloses.",
        "why": [
            ("Knowing the best SHAPE is half the answer. The other half is how much "
             "ground it actually encloses, in square metres — and that is what tells you "
             "whether the fence was worth buying.",
             '[[goal text="How much ground that wins"]]'),
        ],
        "picture": [
            ("Here is the square that 40 metres of fence builds, side 10, drawn on a "
             "metre grid. Every little square inside it is one square metre of ground. "
             "The ground the fence wins is the count of those squares — the area.",
             '[[rectangle w="10" h="10" show="area" ask="1" caption="the square of side 10 on a metre grid — the ground inside is the area"]]'),
        ],
        "teach": [
            ("That is the method: the area is the side squared. 10 times 10 is 100 "
             "square metres — ten rows of ten squares. No other rectangle with that same "
             "fence can beat it: 5 by 15 uses the identical fence and encloses only 75.",
             '[[rectangle w="10" h="10" show="area" caption="10 by 10 — 100 square metres of ground"]][[step eq="10 × 10 = 100 m² · 5 × 15 = only 75"]]'),
            ("So the answer to how much is the side SQUARED. Handing back 10 gives the "
             "side rather than the ground, and 40 is the fence you started with — three "
             "different measurements, and the question names one.",
             '[[step eq="100 ✓"]][[step eq="10 ✗ the side · 40 ✗ the fence"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 68 metres of fence gives a square "
                        "of side 17, enclosing 17 times 17 — 289 square metres.",
                        '[[rectangle w="17" h="17" show="area" caption="17 by 17 — 289 square metres"]][[step eq="17 × 17 = 289 m²"]]'),
             "ask": {"a": 60, "b": 0, "op": "maxa"}},
            {"worked": ("One more together. 72 metres gives sides of 18, and 18 times 18 "
                        "is an area of 324 square metres — every square on the grid counted.",
                        '[[rectangle w="18" h="18" show="area" caption="18 by 18 — 324 square metres"]][[step eq="18 × 18 = 324 m²"]]'),
             "ask": {"a": 64, "b": 0, "op": "maxa"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A square of side 10 "
                       "encloses 100 square metres, not 10. Tap the reason why."),
            "choices": ("because the area is the side times itself | "
                        "because the area is the same number as the side | "
                        "because the ground is measured by the fence"),
            "answer": "because the area is the side times itself",
            "board": '[[rectangle w="10" h="10" show="area" ask="1" caption="why 100, and not 10?"]]',
        },
        "recap": [
            ("So, here it is again. The best rectangle is a square, and the ground it "
             "encloses is the side squared — rows of squares, each row as long as the "
             "side. The side is not the ground, and the fence is not the ground either.",
             '[[rectangle w="10" h="10" show="area" caption="side squared is the ground"]]'),
            ("And that is how much the best rectangle wins.",
             '[[step eq="10 × 10 = 100"]]'),
        ],
        "bank": [{"a": v, "b": 0, "op": "maxa"} for v in
                 (20, 24, 28, 32, 36, 44, 48, 52, 56)],
    },
    {
        "id": "calc-u5-equal-halves-win",
        "course": "calculus", "unit": 5,
        "topic": "The biggest product",
        "op": "sumx", "max_value": 256,
        "levels": ("abstract",),
        "symbols": ("product", "halves"),
        "advance_line": "Three in a row, and you can say why — you've got it! Split it down the middle and multiply.",
        "why": [
            ("Strip the fence away and the same truth shows up in plain numbers. Two "
             "numbers must add to 30. Which pair has the biggest product? Equal halves "
             "win — and calculus can prove it in one line.",
             '[[goal text="Equal halves win"]]'),
        ],
        "picture": [
            ("Here is the product for every way of splitting 30: one number along the "
             "bottom, the other is what is left, and the height is what they multiply "
             "to. The curve rises, peaks, and falls — the biggest product sits at the "
             "top of the hump.",
             '[[graph func="x*(30-x)" names="product = x(30 − x)" range="0..30" yrange="0..270" caption="the product of two numbers adding to 30 — it rises, peaks, and falls"]]'),
        ],
        "teach": [
            ("That is the method: halve the sum, then multiply. Try a few first: 1 "
             "and 29 give 29; 5 and 25 give 125; 14 and 16 give 224; and 15 with 15 "
             "gives 225. The peak is at the halfway point, and calculus agrees — the "
             "product's slope is zero exactly there.",
             '[[graph func="x*(30-x)" names="product = x(30 − x); the peak" lines="y=225" points="(15,225)" range="0..30" yrange="0..270" caption="the peak at 15 and 15 — a product of 225"]][[step eq="15 × 15 = 225 · beats 14 × 16 = 224"]]'),
            ("So halve the number you were given, then multiply — the halves themselves "
             "are not the answer, and neither is the sum you started from. It is the "
             "square fence again, with the fence taken away.",
             '[[step eq="225 ✓"]][[step eq="15 ✗ one half · 30 ✗ the sum"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Two numbers adding to 34: 17 and "
                        "17 give the biggest product, 289 — the top of the hump.",
                        '[[graph func="x*(34-x)" names="product = x(34 − x); the peak" lines="y=289" points="(17,289)" range="0..34" yrange="0..346" caption="the peak at 17 and 17 — 289"]][[step eq="17 × 17 = 289"]]'),
             "ask": {"a": 26, "b": 0, "op": "sumx"}},
            {"worked": ("One more together. Adding to 36, the best pair is 18 and 18 — a "
                        "product of 324, and every other split falls short of it.",
                        '[[graph func="x*(36-x)" names="product = x(36 − x); the peak" lines="y=324" points="(18,324)" range="0..36" yrange="0..388" caption="the peak at 18 and 18 — 324"]][[step eq="18 × 18 = 324"]]'),
             "ask": {"a": 28, "b": 0, "op": "sumx"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Two numbers adding to "
                       "30 have a biggest product of 225, not 15. Tap the reason why."),
            "choices": ("because equal halves multiply to the most | "
                        "because one half is the biggest product | "
                        "because the product is the sum you started with"),
            "answer": "because equal halves multiply to the most",
            "board": '[[graph func="x*(30-x)" names="product = x(30 − x)" range="0..30" yrange="0..270" caption="why 225, and not 15?"]]',
        },
        "recap": [
            ("So, here it is again. Two numbers with a fixed sum multiply to the most "
             "when they are equal: halve the sum, then multiply the halves. A half on "
             "its own is not the product, and the sum is where you started.",
             '[[graph func="x*(30-x)" names="product = x(30 − x); the peak" lines="y=225" points="(15,225)" range="0..30" yrange="0..270" caption="equal halves win"]]'),
            ("And that is the fence problem wearing plain numbers.",
             '[[step eq="15 × 15 = 225"]]'),
        ],
        "bank": [{"a": v, "b": 0, "op": "sumx"} for v in
                 (6, 8, 10, 12, 14, 16, 18, 20, 22, 24)],
    },
    {
        "id": "calc-u5-where-the-bend-changes",
        "course": "calculus", "unit": 5,
        "topic": "Inflection points",
        "op": "infl", "max_value": 90,
        "levels": ("abstract",),
        "symbols": ("bend", "second derivative"),
        "advance_line": "Three in a row, and you can say why — you've got it! Set the second derivative to zero.",
        "why": [
            ("A curve can bend like a cup or like a dome, and somewhere between the two "
             "it changes its mind. That place is an inflection point, and the FIRST "
             "derivative cannot find it — being flat is a different thing from changing "
             "your bend. The second derivative measures the bend.",
             '[[goal text="Where the bend changes"]]'),
        ],
        "picture": [
            ("Here is y equals x cubed take away 6 x squared. Watch the bend, not the "
             "height: on the left the curve arches over like a dome; on the right it "
             "scoops up like a cup. Somewhere between, the bend changes sides — and "
             "nothing about the slope tells you where.",
             '[[graph func="x^3-6*x^2" names="y = x³ − 6x²" range="0..6" yrange="-36..6" caption="dome on the left, cup on the right — somewhere between, the bend changes"]]'),
        ],
        "teach": [
            ("That is the method: set the second derivative to zero. For x cubed take "
             "away 6 x squared, the second derivative is 6 x take away 12, which is "
             "zero at x equals 2. Before 2 the curve is a dome; after it, a cup — and "
             "x equals 2 is the inflection point.",
             '[[graph func="x^3-6*x^2" names="y = x³ − 6x²; x = 2" lines="x=2" range="0..6" yrange="-36..6" caption="dome to the left of x = 2, cup to the right"]][[step eq="6x − 12 = 0"]][[step eq="x = 2"]]'),
            ("Notice the arithmetic differs from a critical point: there you halved, "
             "here you divide by 6. Halving out of habit gives the wrong x, and the "
             "number in the equation is not the answer either.",
             '[[step eq="2 ✓"]][[step eq="6 ✗ the halving habit · 12 ✗ the equation\'s number"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Second derivative 6 x take away "
                        "156: zero at x equals 26, where the bend changes sides.",
                        '[[graph func="x^3-78*x^2" names="y = x³ − 78x²; x = 26" lines="x=26" range="0..78" yrange="-79000..14000" caption="dome to the left of x = 26, cup to the right"]][[step eq="6x = 156"]][[step eq="x = 26"]]'),
             "ask": {"a": 66, "b": 0, "op": "infl"}},
            {"worked": ("One more together. 6 x take away 168: 6 x equals 168, so x is 168 "
                        "divided by 6 — 28, and that is where the dome becomes a cup.",
                        '[[graph func="x^3-84*x^2" names="y = x³ − 84x²; x = 28" lines="x=28" range="0..84" yrange="-99000..17000" caption="dome to the left of x = 28, cup to the right"]][[step eq="6x = 168"]][[step eq="x = 28"]]'),
             "ask": {"a": 72, "b": 0, "op": "infl"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. For x cubed take away "
                       "6 x squared, the bend changes at x equals 2, not 6. Tap the reason why."),
            "choices": ("because the second derivative 6x minus 12 is zero at 2 | "
                        "because the bend changes where the slope is zero | "
                        "because the answer is always half the equation's number"),
            "answer": "because the second derivative 6x minus 12 is zero at 2",
            "board": '[[graph func="x^3-6*x^2" names="y = x³ − 6x²" range="0..6" yrange="-36..6" caption="why 2, and not 6?"]]',
        },
        "recap": [
            ("So, here it is again. The bend is measured by the second derivative, so "
             "set THAT to zero to find where a dome becomes a cup. The arithmetic divides "
             "by 6, not by 2 — the halving habit belongs to critical points — and the "
             "equation's own number is never the answer.",
             '[[graph func="x^3-6*x^2" names="y = x³ − 6x²; x = 2" lines="x=2" range="0..6" yrange="-36..6" caption="where the bend changes"]]'),
            ("And that is an inflection point.",
             '[[step eq="6x − 12 = 0 · x = 2"]]'),
        ],
        "bank": [{"a": v, "b": 0, "op": "infl"} for v in
                 (12, 18, 24, 30, 36, 42, 48, 54, 60)],
    },
]
LESSONS.extend(_CALCULUS_U5)


# =============================================================================
# CALCULUS UNIT 6 -- Antiderivatives & Indefinite Integrals (build lx)
# The thread: RUN THE DERIVATIVE BACKWARDS. The power rule reversed, the same
# reversal through a higher power, the discovery that going backwards never
# lands on one function but on a whole family, and the one known point that
# picks a single member out of that family.
# =============================================================================
_CALCULUS_U6 = [
    {
        "id": "calc-u6-the-rule-run-backwards",
        "course": "calculus", "unit": 6,
        "topic": "Antiderivatives",
        "op": "anti", "max_value": 50,
        "levels": ("abstract",),
        "symbols": ("antiderivative", "backwards"),
        "advance_line": "Three in a row, and you can say why — you've got it! Halve the front number and put the power back.",
        "why": [
            ("Every unit so far has asked what the derivative of a function is. Unit Six "
             "asks it backwards. Given a derivative, which function did it come from? "
             "That function is called an antiderivative, and finding it means running "
             "the power rule in reverse.",
             '[[goal text="The rule run backwards"]]'),
        ],
        "picture": [
            ("Here is the power rule as a machine, and it is about to run backwards. "
             "Forwards, 3 x squared drops its 2 down the front and gives 6 x. Backwards "
             "from 6 x, the 6 goes into the machine and comes out halved — because "
             "differentiating had doubled it.",
             '[[write text="derivative = 6x"]][[machine input="6" rule="÷ 2" output="?" caption="the power rule run backwards — the front number goes in and is halved"]]'),
        ],
        "teach": [
            ("That is the method: HALVE the front number, and put the power back up to "
             "squared. 6 halved is 3, so 6 x came from 3 x squared. Check it forwards: "
             "3 x squared differentiates to 6 x, exactly what we started with.",
             '[[machine input="6" rule="÷ 2" output="3" caption="6 halved is 3 — the front number of the function it came from"]][[write text="3x²"]][[step eq="3x² → 6x  ·  6x → 3x²"]]'),
            ("So halve, do not double. Doubling runs the forward rule the wrong way and "
             "lands twice as high, and copying the number straight over forgets that "
             "differentiating doubled it in the first place.",
             '[[step eq="6x → 3 ✓"]][[step eq="6 ✗ copied · 12 ✗ doubled"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. A derivative of 52 x came from 26 x "
                        "squared — half of 52.",
                        '[[machine input="52" rule="÷ 2" output="26" caption="52 halved is 26"]][[write text="26x²"]][[step eq="52 ÷ 2 = 26"]]'),
             "ask": {"a": 44, "b": 0, "op": "anti"}},
            {"worked": ("One more together. 56 x came from 28 x squared — half of 56, with "
                        "the power climbing back up to squared.",
                        '[[machine input="56" rule="÷ 2" output="28" caption="56 halved is 28"]][[write text="28x²"]][[step eq="56 ÷ 2 = 28"]]'),
             "ask": {"a": 48, "b": 0, "op": "anti"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A derivative of 6 x "
                       "came from 3 x squared, not 12 x squared. Tap the reason why."),
            "choices": ("because differentiating doubled the front number, so going back halves it | "
                        "because going backwards doubles the front number | "
                        "because the front number never changes either way"),
            "answer": "because differentiating doubled the front number, so going back halves it",
            "board": '[[write text="derivative = 6x"]][[machine input="6" rule="÷ 2" output="?" caption="why 3, and not 12?"]]',
        },
        "recap": [
            ("So, here it is again. An antiderivative is the function a derivative came "
             "from, and for a derivative like 6 x you halve the front number and put the "
             "power back to squared. Halve, never double, and never copy the number "
             "straight over.",
             '[[machine input="6" rule="÷ 2" output="3" caption="the rule run backwards"]]'),
            ("And that is the first antiderivative.",
             '[[step eq="6x → 3x²"]]'),
        ],
        "bank": [{"a": v, "b": 0, "op": "anti"} for v in
                 (4, 8, 10, 14, 18, 22, 26, 30, 34, 40)],
    },
    {
        "id": "calc-u6-raise-then-divide",
        "course": "calculus", "unit": 6,
        "topic": "The reverse power rule",
        "op": "antp", "max_value": 80,
        "levels": ("abstract",),
        "symbols": ("reverse", "exponent"),
        "advance_line": "Three in a row, and you can say why — you've got it! Raise the exponent by one, then divide by it.",
        "why": [
            ("Halving worked because the power was 2. For any other power the reverse "
             "move is the same shape: raise the exponent by one, then divide the front "
             "number by that new exponent. Two steps, in that order, every time.",
             '[[goal text="Raise, then divide"]]'),
        ],
        "picture": [
            ("Here is the reverse move as a machine. A derivative of 24 x cubed: the "
             "exponent 3 climbs to 4, and the front number 24 goes into the machine to "
             "be divided by that new 4. What comes out is the front number of the "
             "function it came from.",
             '[[write text="derivative = 24x^3"]][[machine input="24" rule="÷ 4" output="?" caption="the power climbs from 3 to 4, and the front number is divided by the new exponent"]]'),
        ],
        "teach": [
            ("That is the method: raise, then divide. The power 3 climbs to 4, and 24 "
             "divided by 4 is 6. So 6 x to the fourth is the answer. Check it forwards — "
             "the 4 comes down onto the 6 and gives 24 x cubed back, which is the "
             "reverse move undone.",
             '[[machine input="24" rule="÷ 4" output="6" caption="24 over the new exponent 4 is 6"]][[write text="6x^4"]][[step eq="3 + 1 = 4 · 24 ÷ 4 = 6"]]'),
            ("Divide by the new exponent — never skip that step. Handing the front "
             "number straight back leaves the dividing undone, and handing back the new "
             "exponent itself answers a question nobody asked.",
             '[[step eq="6 ✓"]][[step eq="24 ✗ not divided · 4 ✗ the exponent"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 77 x to the sixth: the power climbs "
                        "to 7, and 77 over 7 is 11.",
                        '[[machine input="77" rule="÷ 7" output="11" caption="77 over the new exponent 7 is 11"]][[write text="11x^7"]][[step eq="77 ÷ 7 = 11"]]'),
             "ask": {"a": 5, "b": 66, "op": "antp"}},
            {"worked": ("One more together. 108 x to the eighth: the power climbs to 9, and "
                        "108 over 9 is 12 — so 12 x to the ninth is the function it came from.",
                        '[[machine input="108" rule="÷ 9" output="12" caption="108 over the new exponent 9 is 12"]][[write text="12x^9"]][[step eq="108 ÷ 9 = 12"]]'),
             "ask": {"a": 4, "b": 60, "op": "antp"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A derivative of 24 x "
                       "cubed came from 6 x to the fourth, not 24. Tap the reason why."),
            "choices": ("because the front number is divided by the raised exponent | "
                        "because the front number is handed straight back | "
                        "because the new exponent is the front number"),
            "answer": "because the front number is divided by the raised exponent",
            "board": '[[write text="derivative = 24x^3"]][[machine input="24" rule="÷ 4" output="?" caption="why 6, and not 24?"]]',
        },
        "recap": [
            ("So, here it is again. To reverse the power rule on any power: raise the "
             "exponent by one, then divide the front number by that new exponent. Never "
             "skip the dividing, and never hand back the exponent as if it were the "
             "front number.",
             '[[machine input="24" rule="÷ 4" output="6" caption="raise, then divide"]]'),
            ("And that is the reverse power rule.",
             '[[step eq="24x³ → 6x⁴"]]'),
        ],
        "bank": [{"a": a, "b": b, "op": "antp"} for a, b in
                 ((2, 6), (3, 12), (4, 20), (5, 30), (6, 42),
                  (7, 56), (8, 72), (2, 27), (3, 40), (2, 33))],
    },
    {
        "id": "calc-u6-a-whole-family",
        "course": "calculus", "unit": 6,
        "topic": "The constant of integration",
        "op": "plusc", "max_value": 90,
        "levels": ("abstract",),
        "symbols": ("family", "constant"),
        "advance_line": "Three in a row, and you can say why — you've got it! Same derivative means a fixed gap, so add it on.",
        "why": [
            ("Here is the catch in running the rule backwards. A flat number "
             "differentiates to nothing, so x squared and x squared plus 5 have the SAME "
             "derivative. Going backwards cannot tell them apart — an antiderivative is "
             "never one curve but a whole family, a constant apart.",
             '[[goal text="A whole family"]]'),
        ],
        "picture": [
            ("Here are two members of one family: the same shape, one sitting 5 above "
             "the other at every single x. Slide your eye along — the gap never opens "
             "and never closes. Both curves have exactly the same slope everywhere, so "
             "they share one derivative.",
             '[[graph func="x^2-4; x^2+1" names="lower; higher" range="0..6" yrange="-6..40" caption="two curves with the same derivative — the same shape, 5 apart at every x"]]'),
        ],
        "teach": [
            ("That is the method: same derivative means a fixed gap, so add the gap on. "
             "If the lower curve reads 12 at x equals 4 and the gap is 5, the higher one "
             "reads 17 there — 12 plus 5. Curves 5 apart at one x are 5 apart at every "
             "x.",
             '[[graph func="x^2-4; x^2+1" names="lower; higher" points="(4,12),(4,17)" range="0..6" yrange="-6..40" caption="at x = 4 the lower reads 12 and the higher 17 — 5 apart, like everywhere"]][[step eq="12 + 5 = 17"]]'),
            ("Add the gap on. Taking it away drops you below the curve you were given, "
             "and the gap alone is not a height at all — it is the plus C that every "
             "antiderivative carries.",
             '[[step eq="12 + 5 = 17 ✓"]][[step eq="7 ✗ taken away · 5 ✗ the gap"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. A gap of 13 above a lower curve "
                        "reading 30: the higher one reads 43.",
                        '[[graph func="x^2+14; x^2+27" names="lower; higher" points="(4,30),(4,43)" range="0..6" yrange="0..70" caption="30 and 43 at x = 4 — 13 apart"]][[step eq="30 + 13 = 43"]]'),
             "ask": {"a": 28, "b": 17, "op": "plusc"}},
            {"worked": ("One more together. Lower curve 44, gap 15: 44 plus 15 — the higher "
                        "curve reads 59, and the two stay 15 apart wherever you look.",
                        '[[graph func="x^2+28; x^2+43" names="lower; higher" points="(4,44),(4,59)" range="0..6" yrange="0..86" caption="44 and 59 at x = 4 — 15 apart"]][[step eq="44 + 15 = 59"]]'),
             "ask": {"a": 52, "b": 9, "op": "plusc"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Two curves with the "
                       "same derivative sit 5 apart, and above 12 the higher one reads 17, "
                       "not 7. Tap the reason why."),
            "choices": ("because a fixed gap is added on, never taken away | "
                        "because the higher curve is the lower one minus the gap | "
                        "because the gap is the height of the higher curve"),
            "answer": "because a fixed gap is added on, never taken away",
            "board": '[[graph func="x^2-4; x^2+1" names="lower; higher" points="(4,12)" range="0..6" yrange="-6..40" caption="why 17, and not 7?"]]',
        },
        "recap": [
            ("So, here it is again. Two functions with the same derivative are the same "
             "shape a constant apart, and that constant is the plus C. To find the "
             "higher one, add the gap onto the lower — never take it away, and never "
             "hand back the gap itself.",
             '[[graph func="x^2-4; x^2+1" names="lower; higher" points="(4,12),(4,17)" range="0..6" yrange="-6..40" caption="a whole family, a constant apart"]]'),
            ("And that is why every antiderivative ends in plus C.",
             '[[step eq="12 + 5 = 17"]]'),
        ],
        "bank": [{"a": a, "b": b, "op": "plusc"} for a, b in
                 ((5, 2), (9, 6), (13, 10), (17, 14), (21, 18),
                  (25, 22), (29, 26), (33, 30), (42, 29), (51, 28))],
    },
    {
        "id": "calc-u6-one-point-picks-one-curve",
        "course": "calculus", "unit": 6,
        "topic": "Initial value problems",
        "op": "init", "max_value": 110,
        "levels": ("abstract",),
        "symbols": ("initial", "curve"),
        "advance_line": "Three in a row, and you can say why — you've got it! The starting height IS the constant.",
        "why": [
            ("A whole family is not much use when you want one answer. One known point "
             "fixes it: tell me where the curve passes through, and exactly one member "
             "of the family goes there. The initial height at x equals zero is the "
             "handiest point of all.",
             '[[goal text="One point picks one curve"]]'),
        ],
        "picture": [
            ("Here is one curve out of the family with slope 2 x: it starts at the height "
             "7 when x is zero, and climbs from there. The point at the start is what "
             "picks this curve — every other member of the family starts somewhere else.",
             '[[graph func="x^2+7" names="y = x² + 7" points="(0,7)" range="0..4" yrange="0..25" caption="slope 2x through the height 7 at x = 0 — one curve out of the family"]]'),
        ],
        "teach": [
            ("That is the method: the starting height IS the constant. Slope 2 x comes "
             "from x squared plus a constant, and at x equals zero the x squared part "
             "is nothing, so the constant is 7. Then any other x is easy: at x equals 3, "
             "3 squared is 9, plus 7 is 16.",
             '[[graph func="x^2+7" names="y = x² + 7" points="(0,7),(3,16)" range="0..4" yrange="0..25" caption="from 7 at x = 0 up to 16 at x = 3"]][[step eq="y = x² + 7"]][[step eq="3² + 7 = 16"]]'),
            ("Answering 9 forgets the constant the point gave you, and answering 7 "
             "pretends the curve never climbed. The point fixes the constant; the "
             "constant travels with the curve to every other x.",
             '[[step eq="9 + 7 = 16 ✓"]][[step eq="9 ✗ no constant · 7 ✗ never moved"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Starting height 5, and at x equals "
                        "7: 49 plus 5 is 54.",
                        '[[graph func="x^2+5" names="y = x² + 5" points="(0,5),(7,54)" range="0..8" yrange="0..71" caption="from 5 at x = 0 up to 54 at x = 7"]][[step eq="7² + 5 = 54"]]'),
             "ask": {"a": 19, "b": 0, "c": 4, "op": "init"}},
            {"worked": ("One more together. Starting height 10, at x equals 6: 36 plus 10 is "
                        "46 — the constant 10 travels with the curve all the way there.",
                        '[[graph func="x^2+10" names="y = x² + 10" points="(0,10),(6,46)" range="0..7" yrange="0..61" caption="from 10 at x = 0 up to 46 at x = 6"]][[step eq="6² + 10 = 46"]]'),
             "ask": {"a": 28, "b": 0, "c": 6, "op": "init"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A curve with slope 2 x "
                       "through height 7 at x equals zero reads 16 at x equals 3, not 9. "
                       "Tap the reason why."),
            "choices": ("because the starting height is the constant, and it is added on | "
                        "because the constant is nothing once the curve moves | "
                        "because the curve stays at its starting height"),
            "answer": "because the starting height is the constant, and it is added on",
            "board": '[[graph func="x^2+7" names="y = x² + 7" points="(0,7)" range="0..4" yrange="0..25" caption="why 16, and not 9?"]]',
        },
        "recap": [
            ("So, here it is again. One known point picks one curve out of the family, "
             "and the height at x equals zero IS the constant. Square the x, add the "
             "constant on, and you have the height anywhere. Forget the constant and "
             "you are on the wrong curve; keep the start alone and the curve never moved.",
             '[[graph func="x^2+7" names="y = x² + 7" points="(0,7),(3,16)" range="0..4" yrange="0..25" caption="one point picks one curve"]]'),
            ("And that is an initial condition.",
             '[[step eq="y = x² + 7"]]'),
        ],
        "bank": [{"a": a, "b": 0, "c": c, "op": "init"} for a, c in
                 ((2, 2), (8, 3), (11, 4), (12, 5), (22, 5),
                  (21, 6), (3, 8), (13, 8), (6, 9), (16, 9))],
    },
]
LESSONS.extend(_CALCULUS_U6)


# =============================================================================
# CALCULUS UNIT 7 -- The Definite Integral & the FTC (build lx)
# The thread: THE AREA UNDER A GRAPH IS A REAL MEASUREMENT. A rectangle of
# steady speed, a triangle of steady acceleration, the Fundamental Theorem
# tying area back to the antiderivatives of Unit 6, and the average height
# that spreads the area flat again.
# =============================================================================
_CALCULUS_U7 = [
    {
        "id": "calc-u7-the-area-is-the-answer",
        "course": "calculus", "unit": 7,
        "topic": "The definite integral",
        "op": "defi", "max_value": 170,
        "levels": ("abstract",),
        "symbols": ("integral", "rectangle"),
        "advance_line": "Three in a row, and you can say why — you've got it! Height times width is the area under the graph.",
        "why": [
            ("Unit Six ran the derivative backwards. Unit Seven does something that "
             "sounds unrelated and turns out to be the same thing: measuring the AREA "
             "underneath a graph. That area is called a definite integral, and the "
             "simplest one of all is a rectangle.",
             '[[goal text="The area is the answer"]]'),
        ],
        "picture": [
            ("Here is a car holding a steady 8 metres a second for 5 seconds, drawn on a "
             "speed graph. The speed line is flat, and the shaded shape underneath it is "
             "a rectangle — 8 tall and 5 wide. Look at that shaded rectangle: it is about "
             "to mean something.",
             '[[graph lines="y=8" names="a steady 8 metres a second" shade="0..5" label="?" range="0..7" yrange="0..10" caption="8 metres a second for 5 seconds — the shaded rectangle under the speed line"]]'),
        ],
        "teach": [
            ("That is the method: height times width. The rectangle is 8 tall and 5 wide, "
             "so its area is 40 — and 40 metres is exactly how far the car went. The area "
             "MEANS the distance. That is what an integral is: the area underneath, read "
             "as whatever the picture measures.",
             '[[graph lines="y=8" names="a steady 8 metres a second" shade="0..5" label="40" range="0..7" yrange="0..10" caption="8 tall, 5 wide — an area of 40, and 40 metres travelled"]][[step eq="8 × 5 = 40 m"]]'),
            ("So multiply the height by the width. Adding them puts metres and seconds "
             "together as though they measured the same thing, and the width alone is "
             "just the time you were already told.",
             '[[step eq="40 ✓"]][[step eq="13 ✗ added · 5 ✗ the time"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 6 metres a second for 4 seconds is a "
                        "rectangle of area 24 — 24 metres.",
                        '[[graph lines="y=6" names="a steady 6 metres a second" shade="0..4" label="24" range="0..6" yrange="0..8" caption="6 tall, 4 wide — 24 metres"]][[step eq="6 × 4 = 24 m"]]'),
             "ask": {"a": 11, "b": 5, "op": "defi"}},
            {"worked": ("One more together. 9 metres a second for 6 seconds: the rectangle is "
                        "9 tall and 6 wide, so 9 times 6 — 54 metres.",
                        '[[graph lines="y=9" names="a steady 9 metres a second" shade="0..6" label="54" range="0..8" yrange="0..11" caption="9 tall, 6 wide — 54 metres"]][[step eq="9 × 6 = 54 m"]]'),
             "ask": {"a": 10, "b": 9, "op": "defi"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 8 metres a second for 5 "
                       "seconds is 40 metres, not 13. Tap the reason why."),
            "choices": ("because the distance is the rectangle's area, height times width | "
                        "because the speed and the time are added together | "
                        "because the distance is the time alone"),
            "answer": "because the distance is the rectangle's area, height times width",
            "board": '[[graph lines="y=8" names="a steady 8 metres a second" shade="0..5" label="?" range="0..7" yrange="0..10" caption="why 40, and not 13?"]]',
        },
        "recap": [
            ("So, here it is again. The area under a speed graph is the distance, and "
             "under a steady speed that area is a rectangle: height times width. Never add "
             "the two numbers, and never hand back the time alone.",
             '[[graph lines="y=8" names="a steady 8 metres a second" shade="0..5" label="40" range="0..7" yrange="0..10" caption="the area is the answer"]]'),
            ("And that is a definite integral.",
             '[[step eq="8 × 5 = 40"]]'),
        ],
        "bank": [{"a": a, "b": b, "op": "defi"} for a, b in
                 ((2, 3), (3, 7), (17, 2), (4, 12), (7, 9),
                  (7, 11), (12, 8), (14, 8), (19, 7), (14, 11))],
    },
    {
        "id": "calc-u7-when-the-graph-is-a-ramp",
        "course": "calculus", "unit": 7,
        "topic": "Area under a ramp",
        "op": "triz", "max_value": 460,
        "levels": ("abstract",),
        "symbols": ("ramp", "triangle"),
        "advance_line": "Three in a row, and you can say why — you've got it! Square the time, then halve it.",
        "why": [
            ("A steady speed drew a rectangle. Now let the car speed up steadily, so "
             "that after t seconds it is going t metres a second. The graph is no longer "
             "flat — it is a straight ramp climbing from the corner, and the shape "
             "underneath it is a triangle.",
             '[[goal text="When the graph is a ramp"]]'),
        ],
        "picture": [
            ("Here is the ramp: the speed climbs from nothing, one metre a second faster "
             "every second. After 6 seconds the shaded shape under it is a triangle, 6 "
             "wide and 6 tall. Look at the empty half above the ramp — the triangle is "
             "half of the square around it.",
             '[[graph lines="y=x" names="speed = t" shade="0..6" label="?" range="0..8" yrange="0..8" caption="the speed ramps up from nothing — the shaded triangle is the distance after 6 seconds"]]'),
        ],
        "teach": [
            ("That is the method: square the time, then halve it. A triangle covers half "
             "of the rectangle around it, so the area is 6 times 6 halved — 18 metres. "
             "The car went 18 metres in those 6 seconds.",
             '[[graph lines="y=x" names="speed = t" shade="0..6" label="18" range="0..8" yrange="0..8" caption="6 by 6, halved — 18 metres"]][[step eq="6 × 6 ÷ 2 = 18 m"]]'),
            ("Forgetting the half claims 36, the whole rectangle, as if the car had gone "
             "flat out from the very first second. And the time itself, 6, is not a "
             "distance at all.",
             '[[step eq="18 ✓"]][[step eq="36 ✗ no half · 6 ✗ the time"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. After 32 seconds the triangle is 32 "
                        "by 32, halved: 512 metres.",
                        '[[graph lines="y=x" names="speed = t" shade="0..32" label="512" range="0..34" yrange="0..34" caption="32 by 32, halved — 512 metres"]][[step eq="32 × 32 ÷ 2 = 512 m"]]'),
             "ask": {"a": 28, "b": 0, "op": "triz"}},
            {"worked": ("One more together. After 34 seconds: the triangle is 34 wide and 34 "
                        "tall, and 34 times 34 halved is 578 metres.",
                        '[[graph lines="y=x" names="speed = t" shade="0..34" label="578" range="0..36" yrange="0..36" caption="34 by 34, halved — 578 metres"]][[step eq="34 × 34 ÷ 2 = 578 m"]]'),
             "ask": {"a": 30, "b": 0, "op": "triz"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Under the ramp, after 6 "
                       "seconds the car has gone 18 metres, not 36. Tap the reason why."),
            "choices": ("because a triangle is half the rectangle around it | "
                        "because the car went flat out from the first second | "
                        "because the distance is the time squared"),
            "answer": "because a triangle is half the rectangle around it",
            "board": '[[graph lines="y=x" names="speed = t" shade="0..6" label="?" range="0..8" yrange="0..8" caption="why 18, and not 36?"]]',
        },
        "recap": [
            ("So, here it is again. Under a ramp the area is a triangle, and a triangle "
             "is half the rectangle around it: square the time, then halve. Forget the "
             "half and you have claimed the whole rectangle; the time alone is not a "
             "distance.",
             '[[graph lines="y=x" names="speed = t" shade="0..6" label="18" range="0..8" yrange="0..8" caption="when the graph is a ramp"]]'),
            ("And that is the triangle under a ramp.",
             '[[step eq="6 × 6 ÷ 2 = 18"]]'),
        ],
        "bank": [{"a": v, "b": 0, "op": "triz"} for v in
                 (8, 10, 12, 14, 16, 18, 20, 22, 24, 26)],
    },
    {
        "id": "calc-u7-end-take-away-start",
        "course": "calculus", "unit": 7,
        "topic": "The Fundamental Theorem",
        "op": "ftc", "max_value": 170,
        "levels": ("abstract",),
        "symbols": ("theorem", "ends"),
        "advance_line": "Three in a row, and you can say why — you've got it! Square both ends and take the smaller from the bigger.",
        "why": [
            ("Rectangles and triangles are easy shapes. Most graphs are neither — so "
             "here is the theorem that handles all of them, and it is the biggest idea in "
             "the subject: the area comes from the two ends.",
             '[[goal text="End take away start"]]'),
        ],
        "picture": [
            ("Here is y equals 2 x, with the strip underneath it shaded from x equals 3 "
             "to x equals 5. It is not a triangle from the corner and not a rectangle — "
             "it starts partway along. Look at the two ends of the strip, because the "
             "theorem reads them.",
             '[[graph lines="y=2x" names="y = 2x" shade="3..5" label="?" range="0..7" yrange="0..14" caption="the strip under y = 2x from x = 3 to x = 5 — its two ends are what the theorem reads"]]'),
        ],
        "teach": [
            ("That is the method: run the rule backwards as in Unit Six — 2 x comes from "
             "x squared — then work x squared out at both ends and take one from the "
             "other. From 3 to 5: 25 take away 9 is 16, and the shaded strip holds "
             "exactly 16.",
             '[[graph lines="y=2x" names="y = 2x" shade="3..5" label="16" range="0..7" yrange="0..14" caption="5² take away 3² — the strip holds 16"]][[step eq="5² − 3² = 25 − 9 = 16"]]'),
            ("That is the Fundamental Theorem of Calculus: areas and antiderivatives are "
             "one idea wearing two hats. Squaring the gap between the ends instead gives "
             "4, a different number entirely, and the plain gap is only 2.",
             '[[step eq="16 ✓"]][[step eq="4 ✗ gap squared · 2 ✗ the gap"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. From 3 to 8: 64 take away 9 is 55.",
                        '[[graph lines="y=2x" names="y = 2x" shade="3..8" label="55" range="0..10" yrange="0..20" caption="8² take away 3² — 55"]][[step eq="8² − 3² = 55"]]'),
             "ask": {"a": 5, "b": 9, "op": "ftc"}},
            {"worked": ("One more together. From 2 to 11: 121 take away 4 is 117 — end take "
                        "away start, and the strip between them holds 117.",
                        '[[graph lines="y=2x" names="y = 2x" shade="2..11" label="117" range="0..13" yrange="0..26" caption="11² take away 2² — 117"]][[step eq="11² − 2² = 117"]]'),
             "ask": {"a": 6, "b": 12, "op": "ftc"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. The area under 2 x from "
                       "3 to 5 is 16, not 4. Tap the reason why."),
            "choices": ("because the end's x squared take away the start's x squared | "
                        "because the gap between the ends is squared | "
                        "because the area is the width of the strip"),
            "answer": "because the end's x squared take away the start's x squared",
            "board": '[[graph lines="y=2x" names="y = 2x" shade="3..5" label="?" range="0..7" yrange="0..14" caption="why 16, and not 4?"]]',
        },
        "recap": [
            ("So, here it is again. To find the area under a graph, run the rule "
             "backwards, work the antiderivative out at both ends, and take start from "
             "end. That is the Fundamental Theorem — one idea in two hats. Never square "
             "the gap, and never hand back the gap itself.",
             '[[graph lines="y=2x" names="y = 2x" shade="3..5" label="16" range="0..7" yrange="0..14" caption="end take away start"]]'),
            ("And that is the biggest idea in the subject.",
             '[[step eq="5² − 3² = 16"]]'),
        ],
        "bank": [{"a": a, "b": b, "op": "ftc"} for a, b in
                 ((1, 3), (5, 7), (8, 10), (7, 10), (9, 12),
                  (2, 9), (7, 12), (9, 14), (6, 13), (4, 13))],
    },
    {
        "id": "calc-u7-flatten-it-out",
        "course": "calculus", "unit": 7,
        "topic": "Average value",
        "op": "avgv", "max_value": 160,
        "levels": ("abstract",),
        "symbols": ("average", "flat"),
        "advance_line": "Three in a row, and you can say why — you've got it! Area divided by width is the average height.",
        "why": [
            ("One last thing the area can tell you. Suppose you know the area under a "
             "curve and you want a single number for how high the curve typically ran — "
             "its average height. Flatten it out.",
             '[[goal text="Flatten it out"]]'),
        ],
        "picture": [
            ("Here is a curve with a hump and a dip, and the shaded area under it from 0 "
             "to 5 is 60. Imagine pushing the hump down into the dip until the top is "
             "flat. The area does not change — only the shape does.",
             '[[graph func="12 + 6*sin(2*pi*x/5)" names="the curve" shade="0..5" label="60" range="0..5" yrange="0..21" caption="the area under the curve from 0 to 5 is 60 — push the hump down into the dip until the top is flat"]]'),
        ],
        "teach": [
            ("That is the method: area divided by width. An area of 60 spread across a "
             "width of 5 stands 12 high, so 12 is the curve's average height — the "
             "average value of the function. The flat line sits exactly where the hump "
             "above it and the dip below it trade places.",
             '[[graph func="12 + 6*sin(2*pi*x/5)" names="the curve; flattened to 12" lines="y=12" shade="0..5" label="60" range="0..5" yrange="0..21" caption="the same 60 of area as a flat rectangle 5 wide — it stands 12 high"]][[step eq="60 ÷ 5 = 12"]]'),
            ("Some of the curve towers above that line and some falls below, and the two "
             "trade places exactly. Handing back 60 answers with an area where a height "
             "was asked for, and 5 is only the width.",
             '[[step eq="12 ✓"]][[step eq="60 ✗ the area · 5 ✗ the width"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. An area of 96 across a width of 8 "
                        "flattens to a height of 12.",
                        '[[graph func="12 + 6*sin(2*pi*x/8)" names="the curve; flattened to 12" lines="y=12" shade="0..8" label="96" range="0..8" yrange="0..21" caption="96 across 8 — it stands 12 high"]][[step eq="96 ÷ 8 = 12"]]'),
             "ask": {"a": 154, "b": 11, "op": "avgv"}},
            {"worked": ("One more together. 150 of area across a width of 10: 150 divided by "
                        "10 — flattened, it stands 15 high, the curve\'s average.",
                        '[[graph func="15 + 7.5*sin(2*pi*x/10)" names="the curve; flattened to 15" lines="y=15" shade="0..10" label="150" range="0..10" yrange="0..26" caption="150 across 10 — it stands 15 high"]][[step eq="150 ÷ 10 = 15"]]'),
             "ask": {"a": 153, "b": 9, "op": "avgv"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. An area of 60 across a "
                       "width of 5 has an average height of 12, not 60. Tap the reason why."),
            "choices": ("because the area is spread evenly across the width | "
                        "because the average height is the area itself | "
                        "because the height is the width of the curve"),
            "answer": "because the area is spread evenly across the width",
            "board": '[[graph func="12 + 6*sin(2*pi*x/5)" names="the curve" shade="0..5" label="60" range="0..5" yrange="0..21" caption="why 12, and not 60?"]]',
        },
        "recap": [
            ("So, here it is again. The average height of a curve is its area divided by "
             "its width — the height of the flat rectangle with the same area. The area "
             "is not a height, and the width is not a height either.",
             '[[graph func="12 + 6*sin(2*pi*x/5)" names="the curve; flattened to 12" lines="y=12" shade="0..5" label="60" range="0..5" yrange="0..21" caption="flatten it out"]]'),
            ("And that is the average value of a function.",
             '[[step eq="60 ÷ 5 = 12"]]'),
        ],
        "bank": [{"a": a, "b": b, "op": "avgv"} for a, b in
                 ((6, 3), (12, 4), (8, 2), (30, 6), (42, 7),
                  (35, 5), (72, 9), (90, 10), (80, 8), (132, 12))],
    },
]
LESSONS.extend(_CALCULUS_U7)


# =============================================================================
# CALCULUS UNIT 8 -- Applications of Integration (build ly)
# The thread: ONCE AREA IS A MEASUREMENT, IT MEASURES ANYTHING. The area caught
# between two curves, the trapezium under a speed that climbs, an integral that
# adds on to what was already in the tank, and a flat area spun into a solid.
# =============================================================================
_CALCULUS_U8 = [
    {
        "id": "calc-u8-the-gap-between-two-curves",
        "course": "calculus", "unit": 8,
        "topic": "Area between curves",
        "op": "btwn", "max_value": 190,
        "levels": ("abstract",),
        "symbols": ("between", "strip"),
        "advance_line": "Three in a row, and you can say why — you've got it! Top area take away bottom area.",
        "why": [
            ("Unit Seven measured the area under one curve. Draw a second curve below "
             "it and a new region appears — the strip caught between the two. Measuring "
             "that strip is the first real use of everything you have learned.",
             '[[goal text="The gap between two curves"]]'),
        ],
        "picture": [
            ("Here are two curves over the same stretch. The area under the top one is "
             "50, and the area under the bottom one is 18. Look at the shaded strip "
             "between them — and notice that the bottom curve\'s 18 is sitting INSIDE "
             "the top curve\'s 50.",
             '[[graph func="5 + 2.5*sin(2*pi*x/10); 1.8 + 0.9*sin(2*pi*x/10)" names="top; bottom" shade="0..10" between="1" label="?" range="0..10" yrange="0..10" caption="two curves over the same stretch — 50 under the top one, 18 under the bottom one, and the strip between them"]]'),
        ],
        "teach": [
            ("That is the method: top area take away bottom area. The 18 under the "
             "bottom curve is already counted inside the 50, so take it away — 50 take "
             "away 18 is 32, and the strip between them holds 32.",
             '[[graph func="5 + 2.5*sin(2*pi*x/10); 1.8 + 0.9*sin(2*pi*x/10)" names="top; bottom" shade="0..10" between="1" label="32" range="0..10" yrange="0..10" caption="50 take away 18 — the strip between holds 32"]][[step eq="50 − 18 = 32"]]'),
            ("Top take away bottom, always in that order. Adding the two counts the "
             "lower region twice over, and answering with the top area alone hands back "
             "the whole slab instead of the gap.",
             '[[step eq="32 ✓"]][[step eq="68 ✗ added · 50 ✗ the whole slab"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. A top area of 120 with 45 underneath "
                        "it: the strip between them is 75.",
                        '[[graph func="12 + 6*sin(2*pi*x/10); 4.5 + 2.25*sin(2*pi*x/10)" names="top; bottom" shade="0..10" between="1" label="75" range="0..10" yrange="0..21" caption="120 take away 45 — 75 between"]][[step eq="120 − 45 = 75"]]'),
             "ask": {"a": 150, "b": 31, "op": "btwn"}},
            {"worked": ("One more together. Top 160, bottom 38: 160 take away 38 — the gap "
                        "between the two curves is 122.",
                        '[[graph func="16 + 8*sin(2*pi*x/10); 3.8 + 1.9*sin(2*pi*x/10)" names="top; bottom" shade="0..10" between="1" label="122" range="0..10" yrange="0..27" caption="160 take away 38 — 122 between"]][[step eq="160 − 38 = 122"]]'),
             "ask": {"a": 164, "b": 22, "op": "btwn"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. With 50 under the top "
                       "curve and 18 under the bottom, the strip between holds 32, not 68. "
                       "Tap the reason why."),
            "choices": ("because the bottom area is already inside the top area | "
                        "because the two areas are added together | "
                        "because the strip is the whole top area"),
            "answer": "because the bottom area is already inside the top area",
            "board": '[[graph func="5 + 2.5*sin(2*pi*x/10); 1.8 + 0.9*sin(2*pi*x/10)" names="top; bottom" shade="0..10" between="1" label="?" range="0..10" yrange="0..10" caption="why 32, and not 68?"]]',
        },
        "recap": [
            ("So, here it is again. The area between two curves is the top area take "
             "away the bottom area, because the bottom area is already inside the top. "
             "Never add them, and never hand back the top area alone.",
             '[[graph func="5 + 2.5*sin(2*pi*x/10); 1.8 + 0.9*sin(2*pi*x/10)" names="top; bottom" shade="0..10" between="1" label="32" range="0..10" yrange="0..10" caption="the gap between two curves"]]'),
            ("And that is the area between.",
             '[[step eq="50 − 18 = 32"]]'),
        ],
        "bank": [{"a": a, "b": b, "op": "btwn"} for a, b in
                 ((4, 2), (24, 4), (41, 3), (61, 5), (81, 7),
                  (98, 6), (118, 8), (138, 10), (155, 9), (175, 11))],
    },
    {
        "id": "calc-u8-a-speed-that-climbs",
        "course": "calculus", "unit": 8,
        "topic": "The trapezium rule",
        "op": "trap", "max_value": 320,
        "levels": ("abstract",),
        "symbols": ("trapezium", "halfway"),
        "advance_line": "Three in a row, and you can say why — you've got it! Average the two speeds, then hold it for the time.",
        "why": [
            ("A rectangle came from a steady speed and a triangle from a speed starting "
             "at nothing. Now a train that is already moving speeds up further — the "
             "graph is a ramp that starts partway up the page, and the shape under it "
             "is a trapezium.",
             '[[goal text="A speed that climbs"]]'),
        ],
        "picture": [
            ("Here is the train\'s speed: 4 metres a second at the start, climbing "
             "steadily to 10 after 5 seconds. The shaded shape under it is a trapezium — "
             "a rectangle with a triangle on top. Find the height halfway along, "
             "because there is a lovely shortcut hiding there.",
             '[[graph func="4 + 6*x/5" names="speed" shade="0..5" label="?" range="0..7" yrange="0..14" caption="the speed climbs steadily from 4 to 10 over 5 seconds — the shaded trapezium is the distance"]]'),
        ],
        "teach": [
            ("That is the method: average the two speeds, then hold it for the time. The "
             "speed climbs steadily, so the average speed is exactly halfway between 4 "
             "and 10 — that is 7 — and 7 metres a second for 5 seconds is 35 metres. The "
             "halfway line cuts the trapezium into a rectangle of the same area.",
             '[[graph func="4 + 6*x/5" names="speed; the halfway speed, 7" lines="y=7" shade="0..5" label="35" range="0..7" yrange="0..14" caption="halfway between 4 and 10 is 7, held for 5 seconds — 35 metres"]][[step eq="(4 + 10) ÷ 2 = 7 · 7 × 5 = 35"]]'),
            ("Forgetting to halve holds both speeds at once and doubles the answer to "
             "70. Using the top speed for the whole journey claims 50, as though the "
             "train had never been slower than its finish.",
             '[[step eq="35 ✓"]][[step eq="70 ✗ no half · 50 ✗ top speed only"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. From 13 to 21 metres a second over 9 "
                        "seconds: halfway is 17, and 17 for 9 seconds is 153 metres.",
                        '[[graph func="13 + 8*x/9" names="speed; the halfway speed, 17" lines="y=17" shade="0..9" label="153" range="0..11" yrange="0..25" caption="halfway is 17, held for 9 seconds — 153 metres"]][[step eq="(13 + 21) ÷ 2 = 17 · 17 × 9 = 153"]]'),
             "ask": {"a": 6, "b": 16, "c": 10, "op": "trap"}},
            {"worked": ("One more together. From 11 to 18 over 12 seconds: halfway is 14 and a "
                        "half, giving 174 metres for the whole climb.",
                        '[[graph func="11 + 7*x/12" names="speed; the halfway speed, 14.5" lines="y=14.5" shade="0..12" label="174" range="0..14" yrange="0..22" caption="halfway is 14 and a half, held for 12 seconds — 174 metres"]][[step eq="(11 + 18) × 12 ÷ 2 = 174"]]'),
             "ask": {"a": 18, "b": 22, "c": 7, "op": "trap"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Climbing from 4 to 10 "
                       "over 5 seconds, the train goes 35 metres, not 70. Tap the reason why."),
            "choices": ("because the average speed is halfway between the two | "
                        "because both speeds are held for the whole time | "
                        "because the top speed is held for the whole time"),
            "answer": "because the average speed is halfway between the two",
            "board": '[[graph func="4 + 6*x/5" names="speed" shade="0..5" label="?" range="0..7" yrange="0..14" caption="why 35, and not 70?"]]',
        },
        "recap": [
            ("So, here it is again. Under a speed that climbs steadily the shape is a "
             "trapezium, and its area is the halfway speed held for the whole time — "
             "average the two speeds, then multiply by the seconds. Never hold both "
             "speeds at once, and never the top speed alone.",
             '[[graph func="4 + 6*x/5" names="speed; the halfway speed, 7" lines="y=7" shade="0..5" label="35" range="0..7" yrange="0..14" caption="a speed that climbs"]]'),
            ("And that is the trapezium under a climbing speed.",
             '[[step eq="(4 + 10) ÷ 2 × 5 = 35"]]'),
        ],
        "bank": [{"a": a, "b": b, "c": c, "op": "trap"} for a, b, c in
                 ((2, 4, 2), (3, 16, 2), (4, 12, 4), (5, 18, 4), (6, 8, 9),
                  (7, 13, 8), (8, 20, 7), (17, 22, 6), (13, 21, 8),
                  (9, 17, 12))],
    },
    {
        "id": "calc-u8-adding-on-to-what-was-there",
        "course": "calculus", "unit": 8,
        "topic": "Accumulation",
        "op": "accu", "max_value": 160,
        "levels": ("abstract",),
        "symbols": ("accumulation", "start"),
        "advance_line": "Three in a row, and you can say why — you've got it! Work out the change, then add it to what was there.",
        "why": [
            ("Areas have measured distances so far. Here is the same idea measuring "
             "something you can pour. A tank holds 20 litres at the start, and water "
             "runs in at 6 litres a minute for 5 minutes — and the integral only counts "
             "what ARRIVES.",
             '[[goal text="Adding on to what was there"]]'),
        ],
        "picture": [
            ("Here is the flow: a flat 6 litres a minute for 5 minutes, and the shaded "
             "rectangle under it is the water that runs in. But look at what the picture "
             "does not show — the 20 litres that were already sitting in the tank before "
             "the tap was opened.",
             '[[graph lines="y=6" names="6 litres a minute running in" shade="0..5" label="?" range="0..7" yrange="0..8" caption="6 litres a minute for 5 minutes — the shaded rectangle is what ARRIVES, on top of the 20 already there"]]'),
        ],
        "teach": [
            ("That is the method: work out the change, then add it to what was there. "
             "Six litres a minute for five minutes is 30 litres — the area under the "
             "flow graph. The tank was not empty, so those 30 land on top of the 20 "
             "already in it: 50 litres. The amount line starts at 20 and climbs to 50.",
             '[[graph lines="y=6x+20" names="litres in the tank" points="(0,20),(5,50)" range="0..6" yrange="0..60" caption="from 20 litres at the start up to 50 after 5 minutes"]][[step eq="6 × 5 = 30 · 20 + 30 = 50"]]'),
            ("This is what accumulation means: an integral measures the CHANGE, never "
             "the amount. Answering 30 forgets the water that was already there, and "
             "adding all three numbers loosely gives 31, which measures nothing at all.",
             '[[step eq="50 ✓"]][[step eq="30 ✗ the change only · 31 ✗ all three added"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 14 litres in the tank, 11 a minute "
                        "for 10 minutes: 110 more, so 124.",
                        '[[graph lines="y=11x+14" names="litres in the tank" points="(0,14),(10,124)" range="0..11" yrange="0..134" caption="from 14 up to 124 after 10 minutes"]][[step eq="14 + 110 = 124"]]'),
             "ask": {"a": 6, "b": 9, "c": 36, "op": "accu"}},
            {"worked": ("One more together. 23 litres to start, 10 a minute for 12 minutes: "
                        "120 more, so 143 litres — the change added onto what was there.",
                        '[[graph lines="y=10x+23" names="litres in the tank" points="(0,23),(12,143)" range="0..13" yrange="0..153" caption="from 23 up to 143 after 12 minutes"]][[step eq="23 + 120 = 143"]]'),
             "ask": {"a": 12, "b": 9, "c": 5, "op": "accu"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 20 litres to start and 6 "
                       "a minute for 5 minutes leaves 50 in the tank, not 30. Tap the reason "
                       "why."),
            "choices": ("because the integral is the change, added onto the start | "
                        "because the integral is the whole amount in the tank | "
                        "because the start is emptied before the tap opens"),
            "answer": "because the integral is the change, added onto the start",
            "board": '[[graph lines="y=6" names="6 litres a minute running in" shade="0..5" label="?" range="0..7" yrange="0..8" caption="why 50, and not 30?"]]',
        },
        "recap": [
            ("So, here it is again. The area under a flow graph is what arrives — the "
             "change — and an integral measures the change, never the amount. Add it onto "
             "what was already there. Never forget the start, and never add the three "
             "numbers loosely.",
             '[[graph lines="y=6x+20" names="litres in the tank" points="(0,20),(5,50)" range="0..6" yrange="0..60" caption="adding on to what was there"]]'),
            ("And that is accumulation.",
             '[[step eq="20 + 30 = 50"]]'),
        ],
        "bank": [{"a": a, "b": b, "c": c, "op": "accu"} for a, b, c in
                 ((2, 3, 2), (3, 2, 18), (4, 5, 20), (5, 4, 36), (6, 7, 30),
                  (7, 9, 25), (8, 11, 16), (10, 8, 40), (9, 12, 28),
                  (12, 10, 32))],
    },
    {
        "id": "calc-u8-spin-it-into-a-solid",
        "course": "calculus", "unit": 8,
        "topic": "Volumes of revolution",
        "op": "revo", "max_value": 300,
        "levels": ("abstract",),
        "symbols": ("revolution", "radius"),
        "advance_line": "Three in a row, and you can say why — you've got it! Square the radius, then stack it along the length.",
        "why": [
            ("The boldest use of all. Take a flat shape, spin it around a line, and it "
             "sweeps out a solid — a volume of revolution. Integration measures that "
             "solid as easily as it measured the flat area, and the radius does the "
             "work.",
             '[[goal text="Spin it into a solid"]]'),
        ],
        "picture": [
            ("Here is a rectangle 3 tall and 4 long. Spin it about the line beneath it "
             "and it sweeps out a cylinder — the height 3 becomes the radius, and the "
             "length 4 stays the length. Every slice through that cylinder is a circle "
             "of radius 3.",
             '[[rectangle w="4" h="3" show="area" eq="3 tall and 4 long — spin it about the line beneath" caption="the flat rectangle — its height becomes the cylinder\'s radius when it spins"]]'),
        ],
        "teach": [
            ("That is the method: square the radius, then stack it along the length. "
             "Each slice is a circle of area pi times 3 squared — 9 pi — and 4 lengths "
             "of that stack up to 36 pi.",
             '[[solid kind="cylinder" r="3" h="4" caption="a circle of area 9π, stacked 4 long — 36π"]][[step eq="3² × 4 = 36 · volume = 36π"]]'),
            ("Squaring the radius is what turns a flat area into a solid one. Leaving "
             "the squaring out gives 12, still an area pretending to be a volume, and "
             "doubling the radius where you meant to square it gives only 24.",
             '[[step eq="36 ✓"]][[step eq="12 ✗ not squared · 24 ✗ doubled"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. A rectangle 6 tall and 8 long: 6 "
                        "squared is 36, and 8 of those is 288 pi.",
                        '[[solid kind="cylinder" r="6" h="8" caption="a circle of area 36π, stacked 8 long — 288π"]][[step eq="6² × 8 = 288"]]'),
             "ask": {"a": 5, "b": 8, "op": "revo"}},
            {"worked": ("One more together. 5 tall and 12 long: 25 times 12 is 300 pi, the "
                        "circle of area 25 pi stacked twelve long.",
                        '[[solid kind="cylinder" r="5" h="12" caption="a circle of area 25π, stacked 12 long — 300π"]][[step eq="5² × 12 = 300"]]'),
             "ask": {"a": 5, "b": 11, "op": "revo"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A rectangle 3 tall and 4 "
                       "long spins into a cylinder of 36 pi, not 12 pi. Tap the reason why."),
            "choices": ("because every slice is a circle, and its area squares the radius | "
                        "because the volume is the flat rectangle's area | "
                        "because the radius is doubled, not squared"),
            "answer": "because every slice is a circle, and its area squares the radius",
            "board": '[[solid kind="cylinder" r="3" h="4" caption="why 36π, and not 12π?"]]',
        },
        "recap": [
            ("So, here it is again. Spin a flat shape about a line and it sweeps out a "
             "solid; every slice is a circle, so square the radius and stack the circles "
             "along the length. Leave the squaring out and you still have a flat area; "
             "double where you should square and the solid comes out thin.",
             '[[solid kind="cylinder" r="3" h="4" caption="spin it into a solid"]]'),
            ("And that is a volume of revolution.",
             '[[step eq="3² × 4 = 36 · 36π"]]'),
        ],
        "bank": [{"a": a, "b": b, "op": "revo"} for a, b in
                 ((3, 2), (3, 5), (3, 6), (5, 3), (3, 10),
                  (3, 11), (4, 7), (7, 3), (5, 7), (4, 12))],
    },
]
LESSONS.extend(_CALCULUS_U8)


# =============================================================================
# CALCULUS UNIT 9 -- Introduction to Differential Equations (build ly)
# The thread: AN EQUATION CAN DESCRIBE A RATE INSTEAD OF AN AMOUNT, and
# integration is what turns it back into an amount. A constant rate, two rates
# pulling against each other, a rate that depends on the amount itself, and the
# amount at which all change stops. This unit CLOSES CALCULUS.
# =============================================================================
_CALCULUS_U9 = [
    {
        "id": "calc-u9-an-equation-about-a-rate",
        "course": "calculus", "unit": 9,
        "topic": "Differential equations",
        "op": "dfeq", "max_value": 190,
        "levels": ("abstract",),
        "symbols": ("differential", "rate"),
        "advance_line": "Three in a row, and you can say why — you've got it! Rate times time is what goes, then take it off the start.",
        "why": [
            ("Every equation you have met describes an AMOUNT. A differential equation "
             "describes a rate instead — how fast something is changing — and "
             "integration is what turns it back into an amount. Unit Nine reads three "
             "of them.",
             '[[goal text="An equation about a rate"]]'),
        ],
        "picture": [
            ("Here is a tank that starts at 60 litres, and the equation says it loses 4 "
             "litres every minute. So the line of what is in the tank starts at 60 and "
             "falls 4 for every minute across. The equation says nothing about how much "
             "is in there — only how steeply the line drops.",
             '[[graph lines="y=-4x+60" names="litres in the tank" points="(0,60)" range="0..9" yrange="0..70" caption="the tank starts at 60 litres and the line falls 4 every minute — the equation only says how fast it drops"]]'),
        ],
        "teach": [
            ("That is the method: rate times time is what goes, then take it off the "
             "start. Run it 7 minutes: 4 times 7 is 28 gone, so 60 take away 28 leaves "
             "32 — the line has dropped from 60 to 32.",
             '[[graph lines="y=-4x+60" names="litres in the tank" points="(0,60),(7,32)" range="0..9" yrange="0..70" caption="from 60 down to 32 after 7 minutes — 28 gone"]][[step eq="4 × 7 = 28 · 60 − 28 = 32"]]'),
            ("So the rate has to meet the clock before it means anything. Taking away "
             "one minute\'s worth leaves 56, and answering 28 hands back what drained "
             "rather than what is in the tank.",
             '[[step eq="32 ✓"]][[step eq="56 ✗ one minute · 28 ✗ what drained"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 166 litres losing 8 a minute for 2 "
                        "minutes: 16 gone, so 150 are left.",
                        '[[graph lines="y=-8x+166" names="litres in the tank" points="(0,166),(2,150)" range="0..4" yrange="0..176" caption="from 166 down to 150 after 2 minutes"]][[step eq="166 − 16 = 150"]]'),
             "ask": {"a": 155, "b": 8, "c": 5, "op": "dfeq"}},
            {"worked": ("One more together. 183 litres, 5 a minute, 4 minutes: 20 gone, "
                        "leaving 163 — the line drops from 183 to 163.",
                        '[[graph lines="y=-5x+183" names="litres in the tank" points="(0,183),(4,163)" range="0..6" yrange="0..193" caption="from 183 down to 163 after 4 minutes"]][[step eq="183 − 20 = 163"]]'),
             "ask": {"a": 175, "b": 5, "c": 7, "op": "dfeq"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A tank of 60 losing 4 a "
                       "minute holds 32 after 7 minutes, not 28. Tap the reason why."),
            "choices": ("because the rate times the time is taken off the start | "
                        "because the rate times the time is what is left | "
                        "because only one minute of loss is taken off"),
            "answer": "because the rate times the time is taken off the start",
            "board": '[[graph lines="y=-4x+60" names="litres in the tank" points="(0,60)" range="0..9" yrange="0..70" caption="why 32, and not 28?"]]',
        },
        "recap": [
            ("So, here it is again. A differential equation gives a rate, and the rate "
             "has to meet the clock: rate times time is what goes, and that comes off "
             "the start. What drained is not what is left, and one minute\'s worth is "
             "not the whole run.",
             '[[graph lines="y=-4x+60" names="litres in the tank" points="(0,60),(7,32)" range="0..9" yrange="0..70" caption="an equation about a rate"]]'),
            ("And that is a differential equation, read.",
             '[[step eq="60 − 4 × 7 = 32"]]'),
        ],
        "bank": [{"a": a, "b": b, "c": c, "op": "dfeq"} for a, b, c in
                 ((8, 3, 2), (28, 2, 4), (50, 4, 3), (86, 6, 5), (109, 5, 7),
                  (134, 7, 6), (182, 9, 8), (144, 8, 2), (164, 2, 9),
                  (186, 2, 11))],
    },
    {
        "id": "calc-u9-two-rates-at-once",
        "course": "calculus", "unit": 9,
        "topic": "Net rate of change",
        "op": "mixr", "max_value": 320,
        "levels": ("abstract",),
        "symbols": ("net", "against"),
        "advance_line": "Three in a row, and you can say why — you've got it! Find the net rate first, then let the clock work on it.",
        "why": [
            ("Real tanks rarely do one thing at a time. This one is filling and "
             "draining at once: 9 litres a minute run in while 4 litres a minute run "
             "out. Two rates, pulling against each other — and only their net effect "
             "reaches the clock.",
             '[[goal text="Two rates at once"]]'),
        ],
        "picture": [
            ("Here are the two rates as bars: 9 in, 4 out. Look at how much taller the "
             "in bar stands — that difference is all the tank actually feels. The rest "
             "of the inflow is cancelled by the drain before it can count.",
             '[[bars data="in:9 | out:4" caption="two rates pulling against each other — 9 litres a minute running in, 4 draining out"]]'),
        ],
        "teach": [
            ("That is the method: settle the fight before you touch the clock. Nine in "
             "and four out means the tank truly gains 5 litres a minute — that single "
             "number is the net rate. Over 7 minutes it gains 35 litres, and the line of "
             "what is in the tank climbs 5 every minute.",
             '[[graph lines="y=5x" names="litres in the tank" points="(7,35)" range="0..10" yrange="0..55" caption="the tank climbs 5 a minute — 35 litres after 7 minutes"]][[step eq="9 − 4 = 5 · 5 × 7 = 35"]]'),
            ("Adding the two rates instead pretends the drain is helping to fill, and "
             "reaches 91. Counting the inflow alone forgets the plug is out at all, and "
             "claims 63.",
             '[[step eq="35 ✓"]][[step eq="91 ✗ added · 63 ✗ inflow only"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 22 in and 11 out is a net 11 a "
                        "minute; over 12 minutes, 132 litres.",
                        '[[graph lines="y=11x" names="litres in the tank" points="(12,132)" range="0..15" yrange="0..152" caption="a net 11 a minute — 132 litres after 12 minutes"]][[step eq="(22 − 11) × 12 = 132"]]'),
             "ask": {"a": 10, "b": 2, "c": 11, "op": "mixr"}},
            {"worked": ("One more together. 20 in, 2 out, so 18 a minute net; over 9 minutes "
                        "that is 162 litres in the tank.",
                        '[[graph lines="y=18x" names="litres in the tank" points="(9,162)" range="0..12" yrange="0..182" caption="a net 18 a minute — 162 litres after 9 minutes"]][[step eq="(20 − 2) × 9 = 162"]]'),
             "ask": {"a": 18, "b": 5, "c": 9, "op": "mixr"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. With 9 in and 4 out, "
                       "the tank holds 35 after 7 minutes, not 91. Tap the reason why."),
            "choices": ("because the drain is taken off the inflow before the clock runs | "
                        "because the two rates are added together | "
                        "because the drain does not count at all"),
            "answer": "because the drain is taken off the inflow before the clock runs",
            "board": '[[bars data="in:9 | out:4" caption="why 35, and not 91?"]]',
        },
        "recap": [
            ("So, here it is again. When two rates pull against each other, find the net "
             "rate first — in take away out — and only then let the clock work on it. "
             "Never add the two rates, and never count the inflow alone.",
             '[[graph lines="y=5x" names="litres in the tank" points="(7,35)" range="0..10" yrange="0..55" caption="two rates at once"]]'),
            ("And that is a net rate.",
             '[[step eq="(9 − 4) × 7 = 35"]]'),
        ],
        "bank": [{"a": a, "b": b, "c": c, "op": "mixr"} for a, b, c in
                 ((4, 2, 2), (6, 4, 9), (8, 3, 6), (19, 5, 3), (12, 7, 11),
                  (13, 6, 10), (20, 3, 5), (22, 5, 6), (18, 8, 12),
                  (16, 2, 10))],
    },
    {
        "id": "calc-u9-when-the-rate-depends-on-the-amount",
        "course": "calculus", "unit": 9,
        "topic": "Proportional growth",
        "op": "pgrw", "max_value": 160,
        "levels": ("abstract",),
        "symbols": ("proportional", "colony"),
        "advance_line": "Three in a row, and you can say why — you've got it! Multiply the amount by the growth constant.",
        "why": [
            ("Both tanks so far changed at a fixed rate. Now the most important "
             "differential equation there is, the one where the rate depends on the "
             "amount itself — growth that is proportional to what is already there. A "
             "bacterial colony is the classic.",
             '[[goal text="When the rate depends on the amount"]]'),
        ],
        "picture": [
            ("Here is the rate drawn against the amount: for every bacterium in the "
             "dish, the colony gains 4 more a minute. The line climbs — the bigger the "
             "colony, the faster it grows. Read it at any size and it tells you how fast "
             "the colony is growing right then.",
             '[[graph lines="y=4x" names="rate = 4P" range="0..16" yrange="0..64" caption="the rate against the amount — the bigger the colony, the faster it grows"]]'),
        ],
        "teach": [
            ("That is the method: multiply the amount by the growth constant. With 12 "
             "in the dish right now, every one of them contributes 4 a minute. So the "
             "rate right now is 12 times 4 — 48 a minute, the height of the line at P "
             "equals 12.",
             '[[graph lines="y=4x" names="rate = 4P" points="(12,48)" range="0..16" yrange="0..64" caption="at P = 12 the line stands 48 high — 48 new bacteria a minute"]][[step eq="P = 12 · rate = 12 × 4 = 48"]]'),
            ("And that rate will not hold, because the growing feeds the growing. "
             "Adding the two numbers instead of timesing them gives 16, and answering 4 "
             "pretends a colony of a thousand grows no faster than a colony of ten.",
             '[[step eq="48 ✓"]][[step eq="16 ✗ added · 4 ✗ the constant alone"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 18 bacteria gaining 9 each a minute: "
                        "the rate is 162 a minute.",
                        '[[graph lines="y=9x" names="rate = 9P" points="(18,162)" range="0..22" yrange="0..198" caption="at P = 18 the line stands 162 high"]][[step eq="18 × 9 = 162"]]'),
             "ask": {"a": 28, "b": 4, "op": "pgrw"}},
            {"worked": ("One more together. 20 bacteria at 9 each: 20 times 9 — 180 a minute, "
                        "and climbing as the colony climbs.",
                        '[[graph lines="y=9x" names="rate = 9P" points="(20,180)" range="0..24" yrange="0..216" caption="at P = 20 the line stands 180 high"]][[step eq="20 × 9 = 180"]]'),
             "ask": {"a": 21, "b": 7, "op": "pgrw"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A colony of 12 gaining 4 "
                       "each a minute grows at 48 a minute, not 16. Tap the reason why."),
            "choices": ("because every one of the 12 contributes 4 a minute | "
                        "because the amount and the constant are added | "
                        "because the rate is the constant, whatever the size"),
            "answer": "because every one of the 12 contributes 4 a minute",
            "board": '[[graph lines="y=4x" names="rate = 4P" range="0..16" yrange="0..64" caption="why 48, and not 16?"]]',
        },
        "recap": [
            ("So, here it is again. When the rate is proportional to the amount, the "
             "rate right now is the amount times the growth constant. It climbs as the "
             "amount climbs, which is why this kind of change explodes. Never add "
             "the two numbers, and never answer with the constant alone.",
             '[[graph lines="y=4x" names="rate = 4P" points="(12,48)" range="0..16" yrange="0..64" caption="when the rate depends on the amount"]]'),
            ("And that is proportional growth.",
             '[[step eq="12 × 4 = 48"]]'),
        ],
        "bank": [{"a": a, "b": b, "op": "pgrw"} for a, b in
                 ((2, 3), (11, 2), (4, 9), (17, 3), (13, 5),
                  (10, 8), (16, 6), (19, 6), (22, 6), (19, 8))],
    },
    {
        "id": "calc-u9-where-the-change-stops",
        "course": "calculus", "unit": 9,
        "topic": "Equilibrium",
        "op": "eqbm", "max_value": 190,
        "levels": ("abstract",),
        "symbols": ("equilibrium", "population"),
        "advance_line": "Three in a row, and you can say why — you've got it! Set the rate to zero and solve for P.",
        "why": [
            ("The last question of the whole course, and it is a quiet one. A "
             "differential equation tells you how fast a population changes — so ask it "
             "where the change stops. That place is called equilibrium.",
             '[[goal text="Where the change stops"]]'),
        ],
        "picture": [
            ("Here is the rate drawn against the population: 45 take away 5 P. Small "
             "populations grow fast; the bigger the population, the slower the growth — "
             "until the line reaches the axis and the rate is zero. Somewhere along that "
             "line the change stops.",
             '[[graph lines="y=-5x+45" names="rate = 45 − 5P" range="0..14" yrange="-20..50" caption="the rate against the population — it falls as P grows, and somewhere it reaches zero"]]'),
        ],
        "teach": [
            ("That is the method: set the rate to zero and solve for P. 5 P has to "
             "equal 45, so P is 9 — the line crosses the axis at 9. Park the population "
             "at exactly 9 and nothing moves: births and deaths balance.",
             '[[graph lines="y=-5x+45" names="rate = 45 − 5P" points="(9,0)" range="0..14" yrange="-20..50" caption="the rate crosses zero at P = 9 — equilibrium"]][[step eq="5P = 45"]][[step eq="P = 9"]]'),
            ("It is a stable place, too. Above 9 the rate turns negative and pulls back "
             "down; below it, the rate pushes up. So divide, do not take away — 40 is "
             "not a population, and 45 is the number in the equation, not the answer to "
             "it.",
             '[[step eq="9 ✓"]][[step eq="40 ✗ taken away · 45 ✗ the equation\'s number"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. A rate of 58 take away 2 P is zero "
                        "when P is 29.",
                        '[[graph lines="y=-2x+58" names="rate = 58 − 2P" points="(29,0)" range="0..34" yrange="-8..60" caption="the rate crosses zero at P = 29"]][[step eq="2P = 58"]][[step eq="P = 29"]]'),
             "ask": {"a": 144, "b": 6, "op": "eqbm"}},
            {"worked": ("One more together. 90 take away 3 P is zero when 3 P equals 90, so P "
                        "is 30 — the population where the change stops.",
                        '[[graph lines="y=-3x+90" names="rate = 90 − 3P" points="(30,0)" range="0..35" yrange="-12..93" caption="the rate crosses zero at P = 30"]][[step eq="3P = 90"]][[step eq="P = 30"]]'),
             "ask": {"a": 189, "b": 7, "op": "eqbm"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A rate of 45 take away "
                       "5 P stops changing at a population of 9, not 40. Tap the reason why."),
            "choices": ("because the rate is zero when 5 P equals 45 | "
                        "because the constant is taken away from the equation's number | "
                        "because the population is the equation's own number"),
            "answer": "because the rate is zero when 5 P equals 45",
            "board": '[[graph lines="y=-5x+45" names="rate = 45 − 5P" range="0..14" yrange="-20..50" caption="why 9, and not 40?"]]',
        },
        "recap": [
            ("So, here it is again. Equilibrium is the population that drives the rate "
             "to zero: set the rate to zero and solve for P by dividing. Above it the "
             "rate pulls down, below it the rate pushes up. Never take away where you "
             "should divide, and never hand back the equation\'s own number.",
             '[[graph lines="y=-5x+45" names="rate = 45 − 5P" points="(9,0)" range="0..14" yrange="-20..50" caption="where the change stops"]]'),
            ("And that is the end of the course.",
             '[[step eq="5P = 45 · P = 9"]]'),
        ],
        "bank": [{"a": a, "b": b, "op": "eqbm"} for a, b in
                 ((6, 3), (8, 2), (24, 4), (48, 6), (50, 5),
                  (84, 7), (126, 9), (128, 8), (36, 2), (40, 2))],
    },
]
LESSONS.extend(_CALCULUS_U9)

# ---- this course's slice of COURSE_ORDER: the teaching order (lessons/__init__.py joins the ten) ----
ORDER = [

    # ---- CALCULUS (build lu) -- ⭐ THE TWELFTH COURSE OPENS ----
    # Unit 1: Limits & Continuity
    "calc-u1-limits-pass-through", "calc-u1-far-out-only-the-leaders-matter",
    "calc-u1-how-big-is-the-break", "calc-u1-mend-the-curve",
    # Unit 2: The Derivative (build lv)
    "calc-u2-the-window-closes", "calc-u2-the-power-comes-down-front",
    "calc-u2-a-line-has-one-slope", "calc-u2-feed-the-derivative-an-x",
    # Unit 3: Product, Quotient & Chain Rules (build lv)
    "calc-u3-two-things-multiplied", "calc-u3-do-not-forget-the-inside",
    "calc-u3-the-chain-rule-at-a-point", "calc-u3-a-number-underneath",
    # Unit 4: Applications of Derivatives (build lw)
    "calc-u4-when-is-it-going-that-fast", "calc-u4-one-rate-drives-another",
    "calc-u4-where-the-curve-levels-off", "calc-u4-differentiate-twice",
    # Unit 5: Curve Sketching & Optimization (build lw)
    "calc-u5-the-best-rectangle", "calc-u5-and-how-much-ground-that-wins",
    "calc-u5-equal-halves-win", "calc-u5-where-the-bend-changes",
    # Unit 6: Antiderivatives & Indefinite Integrals (build lx)
    "calc-u6-the-rule-run-backwards", "calc-u6-raise-then-divide",
    "calc-u6-a-whole-family", "calc-u6-one-point-picks-one-curve",
    # Unit 7: The Definite Integral & the FTC (build lx)
    "calc-u7-the-area-is-the-answer", "calc-u7-when-the-graph-is-a-ramp",
    "calc-u7-end-take-away-start", "calc-u7-flatten-it-out",
    # Unit 8: Applications of Integration (build ly)
    "calc-u8-the-gap-between-two-curves", "calc-u8-a-speed-that-climbs",
    "calc-u8-adding-on-to-what-was-there", "calc-u8-spin-it-into-a-solid",
    # Unit 9: Introduction to Differential Equations (build ly) -- ⭐ CALCULUS
    # COMPLETE, the twelfth course.
    "calc-u9-an-equation-about-a-rate", "calc-u9-two-rates-at-once",
    "calc-u9-when-the-rate-depends-on-the-amount",
    "calc-u9-where-the-change-stops",
]

# I did no harm and this file is not truncated.

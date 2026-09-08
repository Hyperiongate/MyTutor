# =============================================================================
# lessons/algebra2.py  --  ALGEBRA II: THE AUTHORED LESSONS  --  Hyperion Shift LLC
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
# ALGEBRA II -- UNIT 1: FOUNDATIONS & SYSTEMS (build lh, 2026-08-22)
# =============================================================================
# ⭐ THE SEVENTH COURSE OPENS. Sharpened tools first: absolute value as
# DISTANCE, read both directions (the value, then counting inside it), and then
# systems grown past alg1-u5 -- elimination where the vanishing leaves a PAIR
# that still needs sharing, and three unknowns weighed two at a time. Every
# wrong tap is a stopped-too-soon or a wrong-operation slip, named in the ops.
_ALGEBRA2_U1 = [
    {
        "id": "alg2-u1-how-far-from-zero",
        "course": "algebra2", "unit": 1,
        "topic": "Absolute value",
        "op": "absv", "max_value": 20, "min_value": -20,
        "levels": ("abstract",),
        "symbols": ("absolute value", "distance"),
        "advance_line": "Three in a row, and you can say why — you've got it! Do the take away, keep the size, drop the sign.",
        "why": [
            ("Why two straight bars? Welcome to Algebra Two. The bars around a number "
             "are called absolute value, and they ask one question: how far is this "
             "number from zero? It does not matter which side of zero the number is "
             "on. Four is four steps from zero, and negative four is also four steps "
             "from zero — so both have absolute value four.",
             '[[goal text="How far from zero"]][[step eq="|4| = 4"]][[step eq="|−4| = 4"]]'),
        ],
        "picture": [
            ("Here is the number line, with negative 4 and 4 marked. Count the steps "
             "from each one back to zero: four steps from the left, four steps from "
             "the right. A distance is a plain count of steps, and it never has a "
             "sign.",
             '[[numberline min="-5" max="5" points="-4,4" caption="−4 and 4 are both 4 steps from zero"]]'),
        ],
        "teach": [
            ("The same bars measure the gap between two numbers. Take 8 away from 3 "
             "and you get negative 5. Now ask the real question: how far apart are 3 "
             "and 8? Count the steps: 5 apart. The bars drop the negative sign and "
             "leave the 5.",
             '[[numberline min="1" max="10" points="3,8" hops="3,8" caption="3 and 8 — 5 steps apart"]][[step eq="|3 − 8| → 5 apart"]]'),
            ("Here is where students go wrong. They do the take away, get negative 5, "
             "and stop there. But think about what we asked: how far apart are 3 and "
             "8? Two numbers cannot be negative 5 apart. A distance is always a plain "
             "count of steps. So finish the job: drop the sign. They are 5 apart.",
             '[[step eq="|3 − 8| = 5 ✓"]][[step eq="negative 5 ✗ two numbers cannot be negative 5 apart"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Take 9 away from 4 and you get "
                        "negative 5. Keep the size, drop the sign. So 4 and 9 are 5 "
                        "apart.",
                        '[[numberline min="2" max="11" points="4,9" hops="4,9" caption="4 and 9 — 5 steps apart"]][[step eq="|4 − 9| → 5"]]'),
             "ask": {'a': 2, 'b': 5, 'op': 'absv'}},
            {"worked": ("One more together. Take 11 away from 5 and you get negative 6. "
                        "Drop the sign: the absolute value is 6.",
                        '[[numberline min="3" max="13" points="5,11" hops="5,11" caption="5 and 11 — 6 steps apart"]][[step eq="|5 − 11| → 6"]]'),
             "ask": {'a': 7, 'b': 18, 'op': 'absv'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. The absolute value "
                       "of 3 take away 8 is 5, not negative 5. Tap the reason why."),
            "choices": ("because the bars ask how far apart, and distance has no sign | "
                        "because the bars always make a number bigger | because the "
                        "take away was done the wrong way round"),
            "answer": "because the bars ask how far apart, and distance has no sign",
            "board": '[[numberline min="1" max="10" points="3,8" hops="3,8" caption="|3 − 8| = 5"]]',
        },
        "recap": [
            ("So, here it is again. Absolute value asks how far — from zero, or "
             "between two numbers — and a distance is a plain count of steps. Do the "
             "take away, keep the size, drop the sign.",
             '[[numberline min="1" max="10" points="3,8" hops="3,8" caption="3 and 8 are 5 apart"]]'),
            ("And that is two straight bars, and the one question they ask.",
             '[[step eq="|3 − 8| = 5"]]'),
        ],
        "bank": [
            {"a": 3, "b": 5, "op": "absv"},
            {"a": 6, "b": 9, "op": "absv"},
            {"a": 2, "b": 6, "op": "absv"},
            {"a": 8, "b": 13, "op": "absv"},
            {"a": 4, "b": 10, "op": "absv"},
            {"a": 5, "b": 12, "op": "absv"},
            {"a": 9, "b": 17, "op": "absv"},
            {"a": 3, "b": 12, "op": "absv"},
            {"a": 6, "b": 16, "op": "absv"},
            {"a": 8, "b": 20, "op": "absv"},
        ],
    },
    {
        "id": "alg2-u1-inside-the-distance",
        "course": "algebra2", "unit": 1,
        "topic": "Counting inside a distance",
        "op": "absc", "max_value": 30,
        "levels": ("abstract",),
        "symbols": ("absolute value", "whole numbers"),
        "advance_line": "Three in a row, and you can say why — you've got it! Both sides, and the quiet zero in the middle.",
        "why": [
            ("Why count inside a distance? Because absolute value draws a fence on "
             "both sides of zero. Which whole numbers have an absolute value less than "
             "5? Any number closer to zero than 5 steps — on either side. The negatives "
             "count, the positives count, and one number always sneaks in unseen: "
             "zero.",
             '[[goal text="Inside the distance"]]'),
        ],
        "picture": [
            ("Here is the number line with the fence at negative 5 and 5. Everything "
             "strictly inside it is closer to zero than 5: negative 4 up to 4. The "
             "ends themselves stay out — 5 is not LESS than 5.",
             '[[numberline min="-5" max="5" points="-4,4" caption="closer to zero than 5 — from −4 up to 4, the ends left out"]]'),
        ],
        "teach": [
            ("That is the method. List them: negative 4, negative 3, negative 2, "
             "negative 1, zero, then 1, 2, 3, 4. Count: 4 negatives, 4 positives, and "
             "zero — 9 whole numbers.",
             '[[bars data="negatives:4 | zero:1 | positives:4" caption="4 + 1 + 4 = 9 whole numbers"]][[step eq="4 + 1 + 4 = 9"]]'),
            ("Two traps, both one short. Forget zero and you count 8 — but zero\'s "
             "absolute value is 0, and 0 is less than 5. Count only the positive side "
             "and you get 4 — half the picture. Both sides, and the quiet zero in the "
             "middle.",
             '[[step eq="4 + 1 + 4 = 9 ✓"]][[step eq="8 ✗ forgot zero · 4 ✗ one side only"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Less than 2: that is negative 1, "
                        "zero, and 1 — 3 whole numbers.",
                        '[[bars data="negatives:1 | zero:1 | positives:1" caption="1 + 1 + 1 = 3"]][[step eq="1 + 1 + 1 = 3"]]'),
             "ask": {'a': 3, 'b': 0, 'op': 'absc'}},
            {"worked": ("One more together. Less than 20: 19 negatives, 19 positives, "
                        "and zero — 39.",
                        '[[bars data="negatives:19 | zero:1 | positives:19" caption="19 + 1 + 19 = 39"]][[step eq="19 + 1 + 19 = 39"]]'),
             "ask": {'a': 13, 'b': 0, 'op': 'absc'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. There are 9 whole "
                       "numbers with an absolute value less than 5. Tap the reason why."),
            "choices": ("because both sides count, and so does zero in the middle | "
                        "because only the positive side counts, doubled | because the "
                        "ends, 5 and negative 5, count too"),
            "answer": "because both sides count, and so does zero in the middle",
            "board": '[[bars data="negatives:4 | zero:1 | positives:4" caption="4 + 1 + 4 = 9"]]',
        },
        "recap": [
            ("So, here it is again. Absolute value less than a number means closer to "
             "zero than that, on either side. Count the negatives, count the "
             "positives, and add the quiet zero — the ends themselves stay out.",
             '[[numberline min="-5" max="5" points="-4,4" caption="inside the fence: 4 + 1 + 4 = 9"]]'),
            ("And that is a distance, counted from the inside.",
             '[[step eq="4 + 1 + 4 = 9"]]'),
        ],
        "bank": [
            {"a": 4, "b": 0, "op": "absc"},
            {"a": 6, "b": 0, "op": "absc"},
            {"a": 7, "b": 0, "op": "absc"},
            {"a": 8, "b": 0, "op": "absc"},
            {"a": 9, "b": 0, "op": "absc"},
            {"a": 10, "b": 0, "op": "absc"},
            {"a": 11, "b": 0, "op": "absc"},
            {"a": 12, "b": 0, "op": "absc"},
            {"a": 14, "b": 0, "op": "absc"},
            {"a": 15, "b": 0, "op": "absc"},
        ],
    },
    {
        "id": "alg2-u1-the-bananas-cancel",
        "course": "algebra2", "unit": 1,
        "topic": "Elimination with a shared piece",
        "op": "el2", "max_value": 40,
        "levels": ("abstract",),
        "symbols": ("clue", "cents"),
        "advance_line": "Three in a row, and you can say why — you've got it! Vanish, then share.",
        "why": [
            ("Why do the bananas cancel? Algebra One taught the vanishing trick: two "
             "shopping trips priced in cents, and taking one clue away from the other "
             "made the shared item disappear. Algebra Two adds one step. Sometimes what "
             "is left after the vanishing is not one unknown — it is a PAIR, and the "
             "pair still needs sharing.",
             '[[goal text="The bananas cancel"]]'),
        ],
        "picture": [
            ("Here are the two trips as bars. The big trip: three apples and two "
             "bananas, 14 cents. The small trip: one apple and the same two bananas, "
             "8 cents. The bananas sit in both bars — take the small bar away from the "
             "big one and only apples are left.",
             '[[tape parts="apple | apple | apple | banana | banana" total="14" caption="the big trip: 14 cents"]][[tape parts="apple | banana | banana" total="8" caption="the small trip: 8 cents — the same two bananas"]]'),
        ],
        "teach": [
            ("That is the method. Take the small trip away: the bananas vanish, and 3 "
             "apples take away 1 apple leaves 2 apples — costing 14 take away 8, which "
             "is 6. Two apples for 6: one apple is 3.",
             '[[tape parts="apple | apple" total="6" caption="left standing: 2 apples = 14 − 8 = 6"]][[step eq="2 apples = 14 − 8 = 6"]][[step eq="1 apple = 6 ÷ 2 = 3"]]'),
            ("The trap is stopping early. 6 is real — it is what TWO apples cost — but "
             "the question asked for one. After the vanishing, look at what is left "
             "standing: if a pair stands there, share before you answer. Vanish, then "
             "share.",
             '[[step eq="2 apples = 6 · 1 apple = 3 ✓"]][[step eq="6 ✗ — that is the pair, not the apple"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Three apples and two bananas: 22 "
                        "cents. One apple and the same bananas: 8. The bananas cancel — "
                        "2 apples cost 14, so one apple costs 7.",
                        '[[tape parts="apple | apple" total="14" caption="2 apples = 22 − 8 = 14 — one apple is 7"]][[step eq="2 apples = 22 − 8 = 14 · 1 apple = 7"]]'),
             "ask": {'a': 12, 'b': 6, 'op': 'el2'}},
            {"worked": ("One more together. Trips of 19 and 9: the bananas cancel, 2 "
                        "apples cost 10 — one apple is 5 cents.",
                        '[[tape parts="apple | apple" total="10" caption="2 apples = 19 − 9 = 10 — one apple is 5"]][[step eq="2 apples = 10 · 1 apple = 5"]]'),
             "ask": {'a': 25, 'b': 9, 'op': 'el2'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Trips of 14 and 8 "
                       "cents, and one apple costs 3. Tap the reason why."),
            "choices": ("because the bananas cancel, leaving 2 apples to share | because "
                        "the two trips are averaged | because the bananas cancel, and "
                        "6 is the apple"),
            "answer": "because the bananas cancel, leaving 2 apples to share",
            "board": '[[tape parts="apple | apple" total="6" caption="2 apples = 6 · 1 apple = 3"]]',
        },
        "recap": [
            ("So, here it is again. Take one clue away from the other and the shared "
             "item vanishes. Then look at what is left standing: if it is a pair, "
             "share it before you answer. Vanish, then share.",
             '[[tape parts="apple | apple" total="6" caption="vanish, then share: 6 ÷ 2 = 3"]]'),
            ("And that is Algebra One\'s trick, with one more step.",
             '[[step eq="2 apples = 6 · 1 apple = 3"]]'),
        ],
        "bank": [
            {"a": 10, "b": 6, "op": "el2"},
            {"a": 13, "b": 7, "op": "el2"},
            {"a": 16, "b": 8, "op": "el2"},
            {"a": 18, "b": 8, "op": "el2"},
            {"a": 20, "b": 8, "op": "el2"},
            {"a": 24, "b": 10, "op": "el2"},
            {"a": 26, "b": 10, "op": "el2"},
            {"a": 28, "b": 12, "op": "el2"},
            {"a": 30, "b": 12, "op": "el2"},
            {"a": 32, "b": 12, "op": "el2"},
        ],
    },
    {
        "id": "alg2-u1-three-friends",
        "course": "algebra2", "unit": 1,
        "topic": "Three unknowns",
        "op": "sys3", "max_value": 40,
        "levels": ("abstract",),
        "symbols": ("clue", "twice"),
        "advance_line": "Three in a row, and you can say why — you've got it! Add the clues, then halve — everyone was there twice.",
        "why": [
            ("Why three friends? Because it is one more growth: THREE unknowns. Three "
             "friends, but the scale only fits two at a time — so you get three clues, "
             "each about a pair. It looks impossible: no clue ever shows one friend "
             "alone. But together the clues hold everything, because every friend "
             "stands in exactly two of them.",
             '[[goal text="Three friends"]]'),
        ],
        "picture": [
            ("Here are the three clues as bars: the first pair weighs 7, the second "
             "10, the third 9. Look at who is inside each bar — x is in the first and "
             "the third, y in the first and the second, z in the second and the third. "
             "Everyone appears exactly twice.",
             '[[bars data="x + y:7 | y + z:10 | x + z:9" caption="three clues — every friend stands in two of them"]]'),
        ],
        "teach": [
            ("That is the method. Put all three clues together: 26. But look who is "
             "inside: each friend stood on the scale twice — once with each of the "
             "others — so 26 counts everybody two times. Halve it: all three friends "
             "together weigh 13.",
             '[[bars data="all three clues:26 | everyone once:13" caption="26 counts everyone twice — halve it: 13"]][[step eq="7 + 10 + 9 = 26"]][[step eq="everyone counted twice → 26 ÷ 2 = 13"]]'),
            ("The trap is trusting the big sum. 26 is not a weight anyone felt — it is "
             "every friend counted twice. And averaging the three clues tells you "
             "about a typical PAIR, not about the trio. Add the clues, then halve — "
             "everyone was there twice.",
             '[[step eq="26 ÷ 2 = 13 ✓"]][[step eq="26 ✗ everyone counted twice · 26 ÷ 3 ✗ a pair\'s typical weight"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Pairs of 6, 9, and 7: put "
                        "together, 22 — everyone twice — so all three weigh 11.",
                        '[[bars data="all three clues:22 | everyone once:11" caption="6 + 9 + 7 = 22 → 11"]][[step eq="6 + 9 + 7 = 22"]][[step eq="22 ÷ 2 = 11"]]'),
             "ask": {'a': 5, 'b': 10, 'c': 9, 'op': 'sys3'}},
            {"worked": ("One more together. 14, 17 and 15: together 46, halved — 23.",
                        '[[bars data="all three clues:46 | everyone once:23" caption="14 + 17 + 15 = 46 → 23"]][[step eq="46 ÷ 2 = 23"]]'),
             "ask": {'a': 14, 'b': 19, 'c': 15, 'op': 'sys3'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Pairs weigh 7, 10 "
                       "and 9, and all three friends together weigh 13. Tap the reason "
                       "why."),
            "choices": ("because the clues add to 26, and everyone was counted twice | "
                        "because the clues add to 26, and that is the trio | because "
                        "the average of the three clues is the trio"),
            "answer": "because the clues add to 26, and everyone was counted twice",
            "board": '[[bars data="all three clues:26 | everyone once:13" caption="26 ÷ 2 = 13"]]',
        },
        "recap": [
            ("So, here it is again. Three clues about pairs hold all three friends, "
             "because every friend stands in two clues. Add the clues and everyone is "
             "counted twice — so halve the sum, and that is the trio.",
             '[[bars data="all three clues:26 | everyone once:13" caption="add the clues, then halve"]]'),
            ("And that is three unknowns, caught two at a time.",
             '[[step eq="26 ÷ 2 = 13"]]'),
        ],
        "bank": [
            {"a": 6, "b": 10, "c": 8, "op": "sys3"},
            {"a": 6, "b": 11, "c": 7, "op": "sys3"},
            {"a": 8, "b": 12, "c": 10, "op": "sys3"},
            {"a": 10, "b": 14, "c": 12, "op": "sys3"},
            {"a": 10, "b": 15, "c": 11, "op": "sys3"},
            {"a": 12, "b": 16, "c": 14, "op": "sys3"},
            {"a": 12, "b": 20, "c": 16, "op": "sys3"},
            {"a": 16, "b": 24, "c": 20, "op": "sys3"},
            {"a": 18, "b": 23, "c": 19, "op": "sys3"},
            {"a": 20, "b": 28, "c": 24, "op": "sys3"},
        ],
    },
]
LESSONS.extend(_ALGEBRA2_U1)


# =============================================================================
# ALGEBRA II -- UNIT 2: QUADRATIC FUNCTIONS & COMPLEX NUMBERS (build lh)
# =============================================================================
# THE QUADRATIC TELLS ITS SECRETS WITHOUT BEING SOLVED. Vertex form says WHERE
# it turns (alg1's vtx asked how LOW -- the pair of questions is deliberate,
# and the sign trap is the classic); factored form's two roots answer questions
# TOGETHER; the discriminant counts the crossings by its sign alone; and when
# the test number falls below zero, a new number arrives to live down there: i.
_ALGEBRA2_U2 = [
    {
        "id": "alg2-u2-where-it-turns",
        "course": "algebra2", "unit": 2,
        "topic": "The vertex's x",
        "op": "vtx2", "max_value": 12, "min_value": -12,
        "levels": ("abstract",),
        "symbols": ("vertex", "squared"),
        "advance_line": "Three in a row, and you can say why — you've got it! Take away points opposite: the turn sits at plus.",
        "why": [
            ("Why where? Algebra One found how LOW the curve y equals x take away 3, "
             "squared, plus 2 can sink. Algebra Two asks the sharper question: WHERE? "
             "At which x does the curve turn? The formula answers before any table "
             "could — if you read its minus sign the right way around.",
             '[[goal text="Where it turns"]]'),
        ],
        "picture": [
            ("Here is the curve on the grid, with its turning point marked. It comes "
             "down, turns, and climbs away again — and the turn sits at x equals 3, "
             "floating 2 above the ground. The turning point has a name: the vertex.",
             '[[graph func="(x-3)^2+2" points="(3,2)" range="-1..7" caption="y = (x − 3)² + 2 — the vertex, where it turns, at x = 3"]]'),
        ],
        "teach": [
            ("That is the method. The curve turns where the squared part bottoms out — "
             "where x take away 3 equals ZERO. That happens at x equals 3, positive 3. "
             "The vertex\'s x always hides behind the opposite sign: take away 3 "
             "turns at plus 3.",
             '[[graph func="(x-3)^2+2" points="(3,2)" range="-1..7" caption="x − 3 = 0 at x = 3"]][[step eq="x − 3 = 0"]][[step eq="x = 3"]]'),
            ("Two traps. The minus begs you to answer negative 3 — but at x equals "
             "negative 3, x take away 3 is negative 6, nowhere near zero. And the plus "
             "2 is a different fact: how HIGH the turn floats — Algebra One\'s "
             "question. WHERE is 3; how high is 2. Keep them apart.",
             '[[step eq="turns at x = 3 ✓"]][[step eq="−3 ✗ the sign flip · 2 ✗ how high, not where"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. y equals: x take away 4, "
                        "squared, plus 5. The square hits zero at x equals 4 — the "
                        "vertex sits at x equals 4.",
                        '[[graph func="(x-4)^2+5" points="(4,5)" range="0..8" caption="y = (x − 4)² + 5 — it turns at x = 4"]][[step eq="x − 4 = 0"]][[step eq="x = 4"]]'),
             "ask": {'a': 3, 'b': 8, 'op': 'vtx2'}},
            {"worked": ("One more together. x take away 7, squared, plus 9: it turns at x "
                        "equals 7.",
                        '[[graph func="(x-7)^2+9" points="(7,9)" range="3..11" caption="y = (x − 7)² + 9 — it turns at x = 7"]][[step eq="x − 7 = 0"]][[step eq="x = 7"]]'),
             "ask": {'a': 11, 'b': 6, 'op': 'vtx2'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. y equals x take away "
                       "3, squared, plus 2, and the curve turns at x equals 3. Tap the "
                       "reason why."),
            "choices": ("because the squared part is zero exactly at x equals 3 | because "
                        "the minus means the turn is at negative 3 | because the plus 2 "
                        "says where the curve turns"),
            "answer": "because the squared part is zero exactly at x equals 3",
            "board": '[[graph func="(x-3)^2+2" points="(3,2)" range="-1..7" caption="x − 3 = 0 at x = 3"]]',
        },
        "recap": [
            ("So, here it is again. A curve written as x take away a number, squared, "
             "turns where that squared part is zero — at the number itself, with the "
             "opposite sign to the one you see. The plus at the end says how high; the "
             "take away inside says where.",
             '[[graph func="(x-3)^2+2" points="(3,2)" range="-1..7" caption="where: x = 3 · how high: 2"]]'),
            ("And that is the vertex, read straight off the formula.",
             '[[step eq="x − 3 = 0"]][[step eq="x = 3"]]'),
        ],
        "bank": [
            {"a": 2, "b": 5, "op": "vtx2"},
            {"a": 3, "b": 7, "op": "vtx2"},
            {"a": 4, "b": 9, "op": "vtx2"},
            {"a": 5, "b": 2, "op": "vtx2"},
            {"a": 6, "b": 11, "op": "vtx2"},
            {"a": 7, "b": 3, "op": "vtx2"},
            {"a": 8, "b": 5, "op": "vtx2"},
            {"a": 9, "b": 4, "op": "vtx2"},
            {"a": 10, "b": 7, "op": "vtx2"},
            {"a": 12, "b": 5, "op": "vtx2"},
        ],
    },
    {
        "id": "alg2-u2-both-answers-count",
        "course": "algebra2", "unit": 2,
        "topic": "The two roots together",
        "op": "rsum", "max_value": 15,
        "levels": ("abstract",),
        "symbols": ("roots", "sum"),
        "advance_line": "Three in a row, and you can say why — you've got it! Two crossings, and questions about the answers mean both.",
        "why": [
            ("Why both? Because a quadratic in factored form hands you its answers. "
             "Look at x take away 2, times x take away 5, equals zero. So x is 2 or x "
             "is 5 — the two places the curve crosses. Algebra Two starts asking what "
             "the answers do TOGETHER, because pairs of roots carry secrets single "
             "roots cannot.",
             '[[goal text="Both answers count"]]'),
        ],
        "picture": [
            ("Here is the curve, and the two places it crosses the ground are marked: "
             "x equals 2 and x equals 5. Each factor donated one crossing. Those two "
             "crossings are called the roots.",
             '[[graph func="(x-2)*(x-5)" points="(2,0),(5,0)" range="-1..8" caption="y = (x − 2)(x − 5) — the roots, 2 and 5"]]'),
        ],
        "teach": [
            ("That is the method. Today\'s question is the sum of the roots: 2 put "
             "together with 5 is 7. Simple — but only if you remember BOTH answers "
             "exist. One crossing is half the story.",
             '[[graph func="(x-2)*(x-5)" points="(2,0),(5,0)" range="-1..8" caption="roots 2 and 5 — 2 + 5 = 7"]][[step eq="roots 2 and 5 · 2 + 5 = 7"]]'),
            ("Two traps. 2 times 5 is 10 — a real number, and famous later — but it "
             "is the product, not the sum. And answering 2 alone forgets the second "
             "crossing entirely. A curve that touches zero twice has two answers; "
             "questions about THE answers mean both.",
             '[[step eq="2 + 5 = 7 ✓"]][[step eq="10 ✗ the product · 2 ✗ one answer of two"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. x take away 3, times x take away "
                        "6, equals zero: the roots are 3 and 6, and their sum is 9.",
                        '[[graph func="(x-3)*(x-6)" points="(3,0),(6,0)" range="-1..9" caption="roots 3 and 6 — 3 + 6 = 9"]][[step eq="3 + 6 = 9"]]'),
             "ask": {'a': 3, 'b': 5, 'op': 'rsum'}},
            {"worked": ("One more together. The roots are 5 and 7, and their sum is 5 "
                        "plus 7 — 12.",
                        '[[graph func="(x-5)*(x-7)" points="(5,0),(7,0)" range="-1..12" caption="roots 5 and 7 — 5 + 7 = 12"]][[step eq="5 + 7 = 12"]]'),
             "ask": {'a': 6, 'b': 8, 'op': 'rsum'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. x take away 2, times "
                       "x take away 5, equals zero, and the two answers put together "
                       "equal 7. Tap the reason why."),
            "choices": ("because each factor gives one root, and both are added | because "
                        "the two roots are timesed, not added | because only the first "
                        "factor gives an answer"),
            "answer": "because each factor gives one root, and both are added",
            "board": '[[graph func="(x-2)*(x-5)" points="(2,0),(5,0)" range="-1..8" caption="2 + 5 = 7"]]',
        },
        "recap": [
            ("So, here it is again. Each factor of a quadratic donates one root, one "
             "crossing of the ground. A question about the answers means both of them "
             "— add the two roots, and never mistake their product for their sum.",
             '[[graph func="(x-2)*(x-5)" points="(2,0),(5,0)" range="-1..8" caption="two roots, both counted"]]'),
            ("And that is the first secret a pair of roots shares.",
             '[[step eq="2 + 5 = 7"]]'),
        ],
        "bank": [
            {"a": 2, "b": 3, "op": "rsum"},
            {"a": 2, "b": 4, "op": "rsum"},
            {"a": 3, "b": 4, "op": "rsum"},
            {"a": 2, "b": 6, "op": "rsum"},
            {"a": 4, "b": 5, "op": "rsum"},
            {"a": 3, "b": 7, "op": "rsum"},
            {"a": 5, "b": 6, "op": "rsum"},
            {"a": 4, "b": 8, "op": "rsum"},
            {"a": 6, "b": 7, "op": "rsum"},
            {"a": 7, "b": 8, "op": "rsum"},
        ],
    },
    {
        "id": "alg2-u2-the-test-number",
        "course": "algebra2", "unit": 2,
        "topic": "The discriminant",
        "op": "disc", "max_value": 20, "min_value": 0,
        "levels": ("abstract",),
        "symbols": ("discriminant", "test number"),
        "advance_line": "Three in a row, and you can say why — you've got it! The sign is the message: 2, 1 or 0.",
        "why": [
            ("Why a test number? Because you can count a curve\'s crossings without "
             "drawing it. y equals x squared plus 2 x plus 7 hides a test number, "
             "called the discriminant: the x part squared, take away 4 times the plain "
             "number. Its SIGN — not its size — counts the crossings with the x line.",
             '[[goal text="The test number"]][[step eq="x² + a·x + b → test: a² − 4b"]]'),
        ],
        "picture": [
            ("Here are the two numbers the test compares, as bars: 2 squared, which is "
             "4, against 4 times 7, which is 28. The second bar is taller, so the take "
             "away falls below zero — and here is the curve itself, floating above the "
             "x line, never touching it.",
             '[[bars data="2²:4 | 4 · 7:28" caption="4 against 28 — the test number falls below zero"]][[graph func="x^2+2*x+7" range="-5..3" caption="y = x² + 2x + 7 — zero crossings"]]'),
        ],
        "teach": [
            ("That is the method. 2 squared is 4, and 4 times 7 is 28 — the test "
             "number falls below zero. A negative test means the curve never reaches "
             "the x line at all: zero crossings. Positive would mean two. And exactly "
             "zero means one perfect touch.",
             '[[bars data="2²:4 | 4 · 7:28" caption="below zero → 0 crossings"]][[step eq="2² − 4·7 → below zero"]][[step eq="below zero → 0 · zero → 1 · above zero → 2"]]'),
            ("The trap is answering with the test number itself — or fearing the "
             "negative. The test number is a MESSENGER: you never report it, only its "
             "sign. Below zero does not break the mathematics; it simply says no "
             "crossing here. And soon, a new number will live down there.",
             '[[step eq="the sign is the message"]][[step eq="report crossings — 2, 1 or 0 — never the test number"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. x squared plus 3 x plus 1: the "
                        "test is 9 take away 4 — positive. The curve cuts the x line "
                        "twice.",
                        '[[bars data="3²:9 | 4 · 1:4" caption="9 against 4 — positive: 2 crossings"]][[step eq="3² − 4·1 = positive"]][[step eq="2 crossings"]]'),
             "ask": {'a': 4, 'b': 3, 'op': 'disc'}},
            {"worked": ("One more together. x squared plus 8 x plus 16: 64 take away 64 "
                        "is exactly zero — one perfect touch.",
                        '[[bars data="8²:64 | 4 · 16:64" caption="64 against 64 — exactly zero: 1 touch"]][[step eq="8² − 4·16 = 0"]][[step eq="1 touch"]]'),
             "ask": {'a': 6, 'b': 10, 'op': 'disc'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. y equals x squared "
                       "plus 2 x plus 7 never meets the x line. Tap the reason why."),
            "choices": ("because the test number is negative, so no crossing | because "
                        "the test number is 24, so 24 crossings | because a plus 7 "
                        "always means two crossings"),
            "answer": "because the test number is negative, so no crossing",
            "board": '[[bars data="2²:4 | 4 · 7:28" caption="below zero — no crossing"]]',
        },
        "recap": [
            ("So, here it is again. The test number is the x part squared, take away "
             "4 times the plain number — and only its sign matters. Positive, two "
             "crossings; zero, one touch; negative, none. Report the crossings, never "
             "the messenger.",
             '[[graph func="x^2+2*x+7" range="-5..3" caption="a negative test — the curve never comes down"]]'),
            ("And that is a curve counted without being drawn.",
             '[[step eq="below zero → 0 · zero → 1 · above zero → 2"]]'),
        ],
        "bank": [
            {"a": 2, "b": 1, "op": "disc"},
            {"a": 2, "b": 5, "op": "disc"},
            {"a": 3, "b": 2, "op": "disc"},
            {"a": 3, "b": 4, "op": "disc"},
            {"a": 4, "b": 4, "op": "disc"},
            {"a": 5, "b": 4, "op": "disc"},
            {"a": 5, "b": 7, "op": "disc"},
            {"a": 6, "b": 9, "op": "disc"},
            {"a": 7, "b": 10, "op": "disc"},
            {"a": 8, "b": 17, "op": "disc"},
        ],
    },
    {
        "id": "alg2-u2-a-new-number",
        "course": "algebra2", "unit": 2,
        "topic": "i arrives",
        "op": "imag", "max_value": 225, "min_value": -15,
        "levels": ("abstract",),
        "symbols": ("imaginary", "squared"),
        "advance_line": "Three in a row, and you can say why — you've got it! The i carries the minus; the number carries the root.",
        "why": [
            ("Why a new number? Because the unit ends with a door opening. x squared "
             "equals negative 9 has no everyday answer — squares are never negative. "
             "For centuries, that was the end of it. Then mathematicians imagined a "
             "new number, called i, with exactly one job: i squared equals negative 1. "
             "The impossible question opened.",
             '[[goal text="A new number"]][[step eq="i² = −1"]]'),
        ],
        "picture": [
            ("Here is 9 as a square: 3 rows of 3. That is the everyday half "
             "of the answer — 3 times 3 is 9. The minus is the other half, and it is "
             "i\'s job: the answer is 3 times i.",
             '[[array rows="3" cols="3" caption="3 × 3 = 9 — the number is 3; the i carries the minus"]]'),
        ],
        "teach": [
            ("That is the method. With i in hand, x equals 3 i solves it. Check: 3 i "
             "times 3 i is 9 times i squared — and i squared is negative 1 — so it "
             "equals negative 9. Numbers built with i are called imaginary, though "
             "they are as real to mathematics as any invention that works.",
             '[[array rows="3" cols="3" caption="(3i)² = 9 · i² = −9"]][[step eq="(3i)² = 9 · i² = −9 ✓"]]'),
            ("Handle it with care. x squared equals negative 9 does not mean x is "
             "negative 3 — negative 3 squared is POSITIVE 9, the wrong sign entirely. "
             "The minus is i\'s job, not the number\'s. And 9 alone forgot the root: "
             "the number in front of i is what SQUARED gives 9 — that is 3.",
             '[[array rows="3" cols="3" caption="(−3)² is +9 — the wrong sign; the minus is i\'s job"]][[step eq="x = 3i ✓ — the i carries the minus"]][[step eq="−3 ✗ (−3)² = +9 · 9 ✗ forgot the root"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. x squared equals negative 4. "
                        "What times itself is 4? 2 — so x equals 2 i.",
                        '[[array rows="2" cols="2" caption="2 × 2 = 4 — x = 2i"]][[step eq="x² = −4"]][[step eq="x = 2i"]]'),
             "ask": {'a': 16, 'b': 0, 'op': 'imag'}},
            {"worked": ("One more together. x squared equals negative 900: 30 times 30 is "
                        "900, so x is 30 i.",
                        '[[step eq="x² = −900"]][[step eq="30 × 30 = 900"]][[step eq="x = 30i"]]'),
             "ask": {'a': 25, 'b': 0, 'op': 'imag'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. x squared equals "
                       "negative 9, and x is 3 i. Tap the reason why."),
            "choices": ("because the number squares to 9, and i carries the minus | "
                        "because the minus belongs to the 3, not to i | because x is "
                        "the 9 itself, with i on the end"),
            "answer": "because the number squares to 9, and i carries the minus",
            "board": '[[array rows="3" cols="3" caption="(3i)² = −9"]]',
        },
        "recap": [
            ("So, here it is again. A square can never be negative — until i, whose "
             "one job is i squared equals negative 1. Then x squared equals a negative "
             "number is solved by the root of that number, times i. The i carries the "
             "minus; the number carries the root.",
             '[[array rows="3" cols="3" caption="x² = −9 → x = 3i"]]'),
            ("And that is the door the unit opens.",
             '[[step eq="i² = −1 · x = 3i"]]'),
        ],
        "bank": [
            {"a": 36, "b": 0, "op": "imag"},
            {"a": 49, "b": 0, "op": "imag"},
            {"a": 64, "b": 0, "op": "imag"},
            {"a": 81, "b": 0, "op": "imag"},
            {"a": 100, "b": 0, "op": "imag"},
            {"a": 121, "b": 0, "op": "imag"},
            {"a": 144, "b": 0, "op": "imag"},
            {"a": 169, "b": 0, "op": "imag"},
            {"a": 196, "b": 0, "op": "imag"},
            {"a": 225, "b": 0, "op": "imag"},
        ],
    },
]
LESSONS.extend(_ALGEBRA2_U2)


# =============================================================================
# ALGEBRA II -- UNIT 3: POLYNOMIAL FUNCTIONS (build li, 2026-08-22)
# =============================================================================
# WHAT THE DEGREE PROMISES: it adds under times (kz's power rule grown up), it
# caps the wiggles at one fewer, a cubic's three crossings answer together
# (U2-rsum's ladder extended by one), and evaluating a cubic brings back the
# oldest exponent misconception -- x³ read as 3-times-x -- one storey taller.
_ALGEBRA2_U3 = [
    {
        "id": "alg2-u3-degrees-add",
        "course": "algebra2", "unit": 3,
        "topic": "Degrees under times",
        "op": "pdeg", "max_value": 16,
        "levels": ("abstract",),
        "symbols": ("degree", "polynomial"),
        "advance_line": "Three in a row, and you can say why — you've got it! Degrees add when polynomials times.",
        "why": [
            ("Why degrees? Polynomials are algebra\'s long expressions, and their "
             "single most important fact is the degree — the highest power inside. "
             "Multiply two of them and the degrees do something beautifully simple. "
             "You met it in Algebra One with powers: joining piles of x\'s ADDS the "
             "counts. Degrees ride the same rule.",
             '[[goal text="Degrees add"]][[step eq="x³ · x² = x⁵"]]'),
        ],
        "picture": [
            ("Here are the two top powers as piles of x\'s: x to the 4 is a pile of "
             "four, and x cubed is a pile of three. Times them and the piles join into "
             "one pile — seven x\'s tall. The counts add.",
             '[[bars data="x⁴:4 | x³:3 | joined x⁷:7" caption="a pile of 4 and a pile of 3 join into a pile of 7"]]'),
        ],
        "teach": [
            ("That is the method. Take a degree 4 polynomial times a degree 3 "
             "polynomial. The biggest power in the first is x to the 4; in the second, "
             "x cubed. When they meet, the piles join: x to the 4 times x cubed is x to "
             "the 7. Degree 4 times degree 3 lands on degree 7.",
             '[[bars data="x⁴:4 | x³:3 | joined x⁷:7" caption="4 + 3 = 7"]][[step eq="x⁴ · x³ = x⁷"]][[step eq="degree 4 × degree 3 → degree 7"]]'),
            ("The trap is multiplying: 4 times 3 is 12, but degrees do not times — "
             "the powers INSIDE do the timesing, and powers add their counts. And do "
             "not just keep the bigger degree: that is addition\'s rule. Adding "
             "polynomials lets the biggest survive; timesing builds something bigger "
             "than both.",
             '[[step eq="4 + 3 = 7 ✓"]][[step eq="12 ✗ degrees do not times · 4 ✗ that is adding\'s rule"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Degree 5 times degree 2: the top "
                        "powers join — degree 7.",
                        '[[bars data="x⁵:5 | x²:2 | joined x⁷:7" caption="5 + 2 = 7"]][[step eq="x⁵ · x² = x⁷"]]'),
             "ask": {'a': 2, 'b': 3, 'op': 'pdeg'}},
            {"worked": ("One more together. Degree 8 times degree 4 — the degrees add: 12.",
                        '[[bars data="x⁸:8 | x⁴:4 | joined x¹²:12" caption="8 + 4 = 12"]][[step eq="x⁸ · x⁴ = x¹²"]]'),
             "ask": {'a': 6, 'b': 9, 'op': 'pdeg'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A degree 4 "
                       "polynomial times a degree 3 polynomial has degree 7. Tap the "
                       "reason why."),
            "choices": ("because the top powers join, and joined piles add their counts | "
                        "because the top powers join, and joined piles times their "
                        "counts | because the bigger degree always survives"),
            "answer": "because the top powers join, and joined piles add their counts",
            "board": '[[bars data="x⁴:4 | x³:3 | joined x⁷:7" caption="4 + 3 = 7"]]',
        },
        "recap": [
            ("So, here it is again. A polynomial\'s degree is its highest power, and "
             "when two polynomials are timesed their top powers join — piles of x\'s "
             "add their counts. Degrees add; they never times, and the bigger one "
             "never simply survives.",
             '[[bars data="x⁴:4 | x³:3 | joined x⁷:7" caption="degree 4 × degree 3 → degree 7"]]'),
            ("And that is Algebra One\'s power rule, grown up.",
             '[[step eq="x⁴ · x³ = x⁷"]]'),
        ],
        "bank": [
            {"a": 3, "b": 2, "op": "pdeg"},
            {"a": 4, "b": 2, "op": "pdeg"},
            {"a": 2, "b": 5, "op": "pdeg"},
            {"a": 3, "b": 5, "op": "pdeg"},
            {"a": 2, "b": 7, "op": "pdeg"},
            {"a": 4, "b": 6, "op": "pdeg"},
            {"a": 3, "b": 8, "op": "pdeg"},
            {"a": 5, "b": 7, "op": "pdeg"},
            {"a": 6, "b": 8, "op": "pdeg"},
            {"a": 7, "b": 9, "op": "pdeg"},
        ],
    },
    {
        "id": "alg2-u3-the-wiggle-count",
        "course": "algebra2", "unit": 3,
        "topic": "Turning points",
        "op": "turnc", "max_value": 16,
        "levels": ("abstract",),
        "symbols": ("degree", "turn"),
        "advance_line": "Three in a row, and you can say why — you've got it! One fewer turn than the degree — a ceiling, not a schedule.",
        "why": [
            ("Why the wiggle count? Because a polynomial\'s degree promises things "
             "about its picture. A line — degree 1 — never turns. A parabola — degree "
             "2 — turns exactly once. Higher degrees can wiggle more, and the pattern "
             "holds forever: a curve can turn at most one fewer time than its degree.",
             '[[goal text="The wiggle count"]]'),
        ],
        "picture": [
            ("Here is a degree 4 curve on the grid. Count its turns: down, up, down, "
             "then away — three turns. Degree 4, three turns: one fewer than the "
             "degree, and it could never manage a fourth.",
             '[[graph func="x^4-4*x^2" range="-3..3" caption="a degree 4 curve — three turns, one fewer than its degree"]]'),
        ],
        "teach": [
            ("That is the method. Why one fewer? Every turn spends a climb or a fall, "
             "and the last stretch always runs off to the horizon without turning "
             "back. So degree 4: at most 3 turns. Degree 6: at most 5. The wiggles can "
             "be fewer — they can flatten away — but never more.",
             '[[graph func="x^4-4*x^2" range="-3..3" caption="degree 4 → at most 3 turns"]][[step eq="degree 4 → at most 3 turns"]]'),
            ("AT MOST is the promise\'s shape. A degree 4 curve MAY turn 3 times, or "
             "fewer — it can never turn 4. Tapping the degree itself counts one turn "
             "too many, and tapping 1 treats every curve as a parabola. One fewer than "
             "the degree: a ceiling, not a schedule.",
             '[[step eq="degree 4 → 3 turns at most ✓"]][[step eq="4 ✗ the degree itself · 1 ✗ not every curve is a parabola"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Degree 18 — huge — and still the "
                        "same promise: at most 17 turns.",
                        '[[bars data="degree:18 | turns, at most:17" caption="degree 18 → at most 17 turns"]][[step eq="degree 18 → at most 17 turns"]]'),
             "ask": {'a': 3, 'b': 0, 'op': 'turnc'}},
            {"worked": ("One more together. Degree 20: one fewer than the degree — at "
                        "most 19 turns.",
                        '[[bars data="degree:20 | turns, at most:19" caption="degree 20 → at most 19"]][[step eq="degree 20 → at most 19"]]'),
             "ask": {'a': 16, 'b': 0, 'op': 'turnc'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A degree 4 curve can "
                       "turn at most 3 times. Tap the reason why."),
            "choices": ("because the last stretch runs off without turning back | because "
                        "a curve turns once for every degree it has | because every "
                        "curve turns exactly once, like a parabola"),
            "answer": "because the last stretch runs off without turning back",
            "board": '[[graph func="x^4-4*x^2" range="-3..3" caption="degree 4 → at most 3 turns"]]',
        },
        "recap": [
            ("So, here it is again. A polynomial of any degree can turn at most one "
             "fewer time than that degree, because the last stretch always runs off to "
             "the horizon. At most — a ceiling, not a schedule.",
             '[[graph func="x^4-4*x^2" range="-3..3" caption="one fewer turn than the degree"]]'),
            ("And that is a picture promised by a number.",
             '[[step eq="degree 4 → at most 3 turns"]]'),
        ],
        "bank": [
            {"a": 5, "b": 0, "op": "turnc"},
            {"a": 7, "b": 0, "op": "turnc"},
            {"a": 8, "b": 0, "op": "turnc"},
            {"a": 9, "b": 0, "op": "turnc"},
            {"a": 10, "b": 0, "op": "turnc"},
            {"a": 11, "b": 0, "op": "turnc"},
            {"a": 12, "b": 0, "op": "turnc"},
            {"a": 13, "b": 0, "op": "turnc"},
            {"a": 14, "b": 0, "op": "turnc"},
            {"a": 15, "b": 0, "op": "turnc"},
        ],
    },
    {
        "id": "alg2-u3-three-crossings",
        "course": "algebra2", "unit": 3,
        "topic": "Three roots together",
        "op": "rsum3", "max_value": 16,
        "levels": ("abstract",),
        "symbols": ("roots", "crossings"),
        "advance_line": "Three in a row, and you can say why — you've got it! Count your crossings before you add.",
        "why": [
            ("Why three crossings? Algebra One factored quadratics; Algebra Two grows "
             "them. x take away 1, times x take away 3, times x take away 5, equals "
             "zero — THREE factors, a cubic, three crossings: 1, 3 and 5. Each factor "
             "donates one answer, exactly as before. More factors, more crossings.",
             '[[goal text="Three crossings"]]'),
        ],
        "picture": [
            ("Here is the cubic on the grid, with its three crossings marked: 1, 3 and "
             "5. It wiggles up and down through the ground three times — one crossing "
             "for each factor. These are the curve\'s roots.",
             '[[graph func="(x-1)*(x-3)*(x-5)" points="(1,0),(3,0),(5,0)" range="0..6" caption="y = (x − 1)(x − 3)(x − 5) — roots 1, 3 and 5"]]'),
        ],
        "teach": [
            ("That is the method. Now the Algebra Two question: what do the answers do "
             "together? Their sum is 1 put together with 3 with 5 — 9. Simple — but "
             "only if you count all three. One crossing is a third of the story.",
             '[[graph func="(x-1)*(x-3)*(x-5)" points="(1,0),(3,0),(5,0)" range="0..6" caption="1 + 3 + 5 = 9"]][[step eq="1 + 3 + 5 = 9"]]'),
            ("Two traps. 1 times 3 times 5 is 15 — the product, the roots\' OTHER "
             "shared secret, not their sum. And 1 plus 3 is 4 — a cubic has THREE "
             "answers, and questions about the answers mean all of them. Count your "
             "crossings before you add.",
             '[[step eq="1 + 3 + 5 = 9 ✓"]][[step eq="15 ✗ the product · 4 ✗ forgot the third"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Roots of 2, 3 and 6: put "
                        "together, 11.",
                        '[[graph func="(x-2)*(x-3)*(x-6)" points="(2,0),(3,0),(6,0)" range="0..7" caption="roots 2, 3 and 6 — 2 + 3 + 6 = 11"]][[step eq="2 + 3 + 6 = 11"]]'),
             "ask": {'a': 1, 'b': 3, 'c': 6, 'op': 'rsum3'}},
            {"worked": ("One more together. Roots of 1, 5 and 7: 1 plus 5 plus 7, put "
                        "together — 13.",
                        '[[graph func="(x-1)*(x-5)*(x-7)" points="(1,0),(5,0),(7,0)" range="0..8" caption="roots 1, 5 and 7 — 1 + 5 + 7 = 13"]][[step eq="1 + 5 + 7 = 13"]]'),
             "ask": {'a': 2, 'b': 5, 'c': 7, 'op': 'rsum3'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. x take away 1, times "
                       "x take away 3, times x take away 5, equals zero, and the "
                       "answers put together equal 9. Tap the reason why."),
            "choices": ("because three factors give three roots, and all three are added | "
                        "because the three roots are timesed together | because a cubic "
                        "has two answers, added"),
            "answer": "because three factors give three roots, and all three are added",
            "board": '[[graph func="(x-1)*(x-3)*(x-5)" points="(1,0),(3,0),(5,0)" range="0..6" caption="1 + 3 + 5 = 9"]]',
        },
        "recap": [
            ("So, here it is again. Every factor donates one root, so three factors "
             "make three crossings. A question about the answers means all of them — "
             "count the crossings, then add, and never hand back the product.",
             '[[graph func="(x-1)*(x-3)*(x-5)" points="(1,0),(3,0),(5,0)" range="0..6" caption="three crossings, all counted"]]'),
            ("And that is a quadratic\'s trick, grown to a cubic.",
             '[[step eq="1 + 3 + 5 = 9"]]'),
        ],
        "bank": [
            {"a": 1, "b": 2, "c": 4, "op": "rsum3"},
            {"a": 1, "b": 3, "c": 4, "op": "rsum3"},
            {"a": 1, "b": 2, "c": 6, "op": "rsum3"},
            {"a": 2, "b": 3, "c": 5, "op": "rsum3"},
            {"a": 1, "b": 4, "c": 6, "op": "rsum3"},
            {"a": 2, "b": 4, "c": 6, "op": "rsum3"},
            {"a": 2, "b": 4, "c": 7, "op": "rsum3"},
            {"a": 3, "b": 4, "c": 7, "op": "rsum3"},
            {"a": 3, "b": 5, "c": 7, "op": "rsum3"},
            {"a": 4, "b": 5, "c": 7, "op": "rsum3"},
        ],
    },
    {
        "id": "alg2-u3-feed-the-cube",
        "course": "algebra2", "unit": 3,
        "topic": "Evaluating a cubic",
        "op": "pval", "max_value": 70,
        "levels": ("abstract",),
        "symbols": ("cubed", "feed"),
        "advance_line": "Three in a row, and you can say why — you've got it! Read the power, keep the sign.",
        "why": [
            ("Why feed it? Because a polynomial is a machine, like every function since "
             "Algebra One: feed it an x and it answers. y equals: x cubed, take away 2 "
             "x, plus 3. Feeding it means every x in the recipe gets the same meal — "
             "the cubed one AND the plain one.",
             '[[goal text="Feed the cube"]][[step eq="y = x³ − 2x + 3"]]'),
        ],
        "picture": [
            ("Here is the machine with its rule written on it: x cubed, take away 2 x, "
             "plus 3. Feed in x equals 5 and the machine works the whole recipe on that "
             "5 — cubes it, takes away twice it, adds 3 — and out comes 118.",
             '[[machine input="5" rule="x³ − 2x + 3" output="118" caption="feed 5 → 118"]]'),
        ],
        "teach": [
            ("That is the method. Feed x equals 5: 5 cubed is 125; take away 2 times 5 "
             "— 10 — leaves 115; plus 3 is 118. Watch the first step: 5 CUBED, 125. "
             "The whole tower stands on reading that power right.",
             '[[machine input="5" rule="x³ − 2x + 3" output="118" caption="5³ − 2·5 + 3 = 118"]][[step eq="5³ = 125"]][[step eq="125 − 10 + 3 = 118"]]'),
            ("The trap you met in Algebra One returns taller: x cubed does not mean 3 "
             "times x. Feed 5: cubed is 125, but 3 times 5 is only 15 — a different "
             "world. And carry the minus with you: take away 10, never plus 10. Read "
             "the power, keep the sign.",
             '[[step eq="5³ = 125 ✓ · 3 × 5 = 15 ✗"]][[step eq="− 2x means take away · the sign stays"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. y equals: x cubed, take away 1 x, "
                        "plus 3. Feed x equals 2: 8, take away 2, plus 3 — 9.",
                        '[[machine input="2" rule="x³ − 1x + 3" output="9" caption="2³ − 1·2 + 3 = 9"]][[step eq="2³ − 2 + 3 = 9"]]'),
             "ask": {'a': 1, 'b': 2, 'c': 2, 'op': 'pval'}},
            {"worked": ("One more together. x cubed, take away 2 x, plus 4, at x equals "
                        "3: 27 take away 6, plus 4 — 25.",
                        '[[machine input="3" rule="x³ − 2x + 4" output="25" caption="3³ − 2·3 + 4 = 25"]][[step eq="27 − 6 + 4 = 25"]]'),
             "ask": {'a': 2, 'b': 3, 'c': 4, 'op': 'pval'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. y equals x cubed, "
                       "take away 2 x, plus 3, and at x equals 5 the answer is 118. Tap "
                       "the reason why."),
            "choices": ("because the cube is a cube, and the minus is kept | "
                        "because x cubed means 3 times x, so 15 to start | because the "
                        "take away becomes a plus once x is fed in"),
            "answer": "because the cube is a cube, and the minus is kept",
            "board": '[[machine input="5" rule="x³ − 2x + 3" output="118" caption="125 − 10 + 3 = 118"]]',
        },
        "recap": [
            ("So, here it is again. A polynomial is a machine: feed the x into every "
             "place it appears. Read each power as a power — cubed means times itself "
             "three times, never 3 times — and carry every sign with you.",
             '[[machine input="5" rule="x³ − 2x + 3" output="118" caption="read the power, keep the sign"]]'),
            ("And that is a function fed, one level taller.",
             '[[step eq="5³ − 2·5 + 3 = 118"]]'),
        ],
        "bank": [
            {"a": 3, "b": 2, "c": 2, "op": "pval"},
            {"a": 3, "b": 4, "c": 2, "op": "pval"},
            {"a": 1, "b": 1, "c": 2, "op": "pval"},
            {"a": 2, "b": 3, "c": 2, "op": "pval"},
            {"a": 1, "b": 4, "c": 2, "op": "pval"},
            {"a": 5, "b": 7, "c": 3, "op": "pval"},
            {"a": 4, "b": 5, "c": 3, "op": "pval"},
            {"a": 2, "b": 2, "c": 3, "op": "pval"},
            {"a": 2, "b": 5, "c": 3, "op": "pval"},
            {"a": 3, "b": 4, "c": 4, "op": "pval"},
        ],
    },
]
LESSONS.extend(_ALGEBRA2_U3)


# =============================================================================
# ALGEBRA II -- UNIT 4: RATIONAL EXPRESSIONS & FUNCTIONS (build li, 2026-08-22)
# =============================================================================
# DIVISION BECOMES A FUNCTION. y = a/x met and read backwards (the deliberate
# pair, again), then the one FORBIDDEN x -- where the BOTTOM dies, with vtx2's
# sign flip and the x = 0 habit as the wrong taps -- and the far horizon:
# (ax + b)/x hides a survivor, and yesterday's answer (zero) is today's trap.
_ALGEBRA2_U4 = [
    {
        "id": "alg2-u4-sharing-shrinks",
        "course": "algebra2", "unit": 4,
        "topic": "The reciprocal function",
        "op": "rdiv", "max_value": 36,
        "levels": ("abstract",),
        "symbols": ("divided by", "reciprocal"),
        "advance_line": "Three in a row, and you can say why — you've got it! Say the operation out loud, then tap.",
        "why": [
            ("Why does sharing shrink? Because a new family of functions moves in: "
             "division. y equals 14 divided by x — the reciprocal shape. Feed it an x "
             "and it SHARES 14 among x pieces: feed 2, get 7; feed 7, get 2. The bigger "
             "the crowd, the smaller each share — growth backwards.",
             '[[goal text="Sharing shrinks"]]'),
        ],
        "picture": [
            ("Here is the curve on the grid, and it is unlike any polynomial: it falls "
             "fast, then flattens, sliding along the floor without ever landing. The "
             "point at x equals 2 sits at 7 — 14 shared among 2. Reading the curve IS "
             "doing the divisions.",
             '[[graph func="14/x" points="(2,7)" range="0..15" caption="y = 14 ÷ x — at x = 2, y = 7"]]'),
        ],
        "teach": [
            ("That is the method. y equals 14 divided by x, at x equals 2: 14 shared "
             "among 2 is 7. At x equals 7, 14 shared among 7 is 2. Each point is just a "
             "division done.",
             '[[graph func="14/x" points="(2,7),(7,2)" range="0..15" caption="14 ÷ 2 = 7 · 14 ÷ 7 = 2"]][[step eq="14 ÷ 2 = 7"]][[step eq="14 ÷ 7 = 2"]]'),
            ("The traps are the other operations wearing masks. 14 divided by 2 is 7 — "
             "but take away gives 12, and times gives 28, and a hurried hand reaches "
             "for both. The word is DIVIDED: sharing, not taking away, not growing. Say "
             "the operation out loud before you tap.",
             '[[step eq="14 ÷ 2 = 7 ✓"]][[step eq="14 − 2 = 12 ✗ · 14 × 2 = 28 ✗ — masks"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. y equals 16 divided by x, at x "
                        "equals 4: 16 shared among 4 — 4.",
                        '[[graph func="16/x" points="(4,4)" range="0..17" caption="y = 16 ÷ x — at x = 4, y = 4"]][[step eq="16 ÷ 4 = 4"]]'),
             "ask": {'a': 9, 'b': 3, 'op': 'rdiv'}},
            {"worked": ("One more together. 25 divided by x, at x equals 5: 25 shared "
                        "among 5 — 5.",
                        '[[graph func="25/x" points="(5,5)" range="0..27" caption="y = 25 ÷ x — at x = 5, y = 5"]][[step eq="25 ÷ 5 = 5"]]'),
             "ask": {'a': 30, 'b': 6, 'op': 'rdiv'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. y equals 14 divided "
                       "by x, and at x equals 2 the answer is 7. Tap the reason why."),
            "choices": ("because the function shares 14 among 2 | because the function "
                        "takes 2 away from 14 | because the function grows 14 by 2"),
            "answer": "because the function shares 14 among 2",
            "board": '[[graph func="14/x" points="(2,7)" range="0..15" caption="14 ÷ 2 = 7"]]',
        },
        "recap": [
            ("So, here it is again. y equals a number divided by x shares that number "
             "among x pieces, and the bigger the crowd, the smaller each share — a "
             "curve that falls and flattens. The word is divided: not take away, not "
             "times.",
             '[[graph func="14/x" points="(2,7)" range="0..15" caption="sharing shrinks"]]'),
            ("And that is growth, run backwards.",
             '[[step eq="14 ÷ 2 = 7"]]'),
        ],
        "bank": [
            {"a": 6, "b": 2, "op": "rdiv"},
            {"a": 8, "b": 4, "op": "rdiv"},
            {"a": 10, "b": 2, "op": "rdiv"},
            {"a": 12, "b": 3, "op": "rdiv"},
            {"a": 15, "b": 5, "op": "rdiv"},
            {"a": 18, "b": 6, "op": "rdiv"},
            {"a": 20, "b": 4, "op": "rdiv"},
            {"a": 24, "b": 8, "op": "rdiv"},
            {"a": 28, "b": 7, "op": "rdiv"},
            {"a": 36, "b": 9, "op": "rdiv"},
        ],
    },
    {
        "id": "alg2-u4-which-x-was-fed",
        "course": "algebra2", "unit": 4,
        "topic": "Solving a divided by x",
        "op": "rsol", "max_value": 36,
        "levels": ("abstract",),
        "symbols": ("divided by", "undo"),
        "advance_line": "Three in a row, and you can say why — you've got it! Rebuild, then divide.",
        "why": [
            ("Why run it backwards? Because every function question can turn around. "
             "20 divided by x equals 5 — some crowd got 5 each out of 20. Algebra One "
             "asked which input went in, and the answer was always the same move — "
             "undo. Division\'s undo starts with a question: what times 5 rebuilds "
             "20?",
             '[[goal text="Which x was fed"]]'),
        ],
        "picture": [
            ("Here is the machine, run backwards. Its rule is 20 divided by x, its "
             "output came out as 5, and its input door is blank. The question is not "
             "what comes out — it is what went in.",
             '[[machine input="?" rule="20 ÷ x" output="5" caption="the output is 5 — which x went in?"]]'),
        ],
        "teach": [
            ("That is the method. x times 5 must rebuild the 20 — so x is 20 divided by "
             "5, which equals 4. Check by feeding it forward: 20 divided by 4 is 5. "
             "True. The undo of being divided by x turns out to be one more divide — "
             "the reciprocal\'s strange charm.",
             '[[machine input="4" rule="20 ÷ x" output="5" caption="x = 20 ÷ 5 = 4 — check: 20 ÷ 4 = 5"]][[step eq="x · 5 = 20"]][[step eq="x = 20 ÷ 5 = 4"]][[step eq="check: 20 ÷ 4 = 5 ✓"]]'),
            ("The trap is grabbing times: 20 times 5 is 100, far off. And 20 take away "
             "5 is 15 — a different operation\'s answer entirely. The x sits UNDER the "
             "20, and freeing it costs one more divide. Rebuild, then divide.",
             '[[step eq="x = 20 ÷ 5 = 4 ✓"]][[step eq="100 ✗ times is not this undo · 15 ✗"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 24 divided by x equals 8: x is 24 "
                        "divided by 8 — 3.",
                        '[[machine input="3" rule="24 ÷ x" output="8" caption="x = 24 ÷ 8 = 3"]][[step eq="x = 24 ÷ 8 = 3"]]'),
             "ask": {'a': 10, 'b': 5, 'op': 'rsol'}},
            {"worked": ("One more together. 36 divided by x is 4: x is 36 divided by 4 — "
                        "9.",
                        '[[machine input="9" rule="36 ÷ x" output="4" caption="x = 36 ÷ 4 = 9"]][[step eq="x = 36 ÷ 4 = 9"]]'),
             "ask": {'a': 30, 'b': 10, 'op': 'rsol'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 20 divided by x "
                       "equals 5, and x is 4. Tap the reason why."),
            "choices": ("because x times 5 must rebuild the 20 | because the undo of "
                        "dividing is always timesing | because the undo of dividing is "
                        "taking away"),
            "answer": "because x times 5 must rebuild the 20",
            "board": '[[machine input="4" rule="20 ÷ x" output="5" caption="x = 20 ÷ 5 = 4"]]',
        },
        "recap": [
            ("So, here it is again. When a number divided by x gives an answer, x times "
             "that answer rebuilds the number — so x is the number divided by the "
             "answer. Rebuild, then divide, and check it forward.",
             '[[machine input="4" rule="20 ÷ x" output="5" caption="rebuild, then divide"]]'),
            ("And that is the reciprocal\'s undo: one more divide.",
             '[[step eq="x = 20 ÷ 5 = 4"]]'),
        ],
        "bank": [
            {"a": 8, "b": 2, "op": "rsol"},
            {"a": 12, "b": 4, "op": "rsol"},
            {"a": 14, "b": 2, "op": "rsol"},
            {"a": 16, "b": 4, "op": "rsol"},
            {"a": 18, "b": 3, "op": "rsol"},
            {"a": 21, "b": 7, "op": "rsol"},
            {"a": 24, "b": 6, "op": "rsol"},
            {"a": 27, "b": 3, "op": "rsol"},
            {"a": 32, "b": 8, "op": "rsol"},
            {"a": 35, "b": 5, "op": "rsol"},
        ],
    },
    {
        "id": "alg2-u4-the-forbidden-x",
        "course": "algebra2", "unit": 4,
        "topic": "The excluded value",
        "op": "excl", "max_value": 12, "min_value": -12,
        "levels": ("abstract",),
        "symbols": ("forbidden", "zero"),
        "advance_line": "Three in a row, and you can say why — you've got it! The danger is where the BOTTOM is zero.",
        "why": [
            ("Why forbidden? Because every function so far accepted every x, and "
             "division ends that. y equals 5 divided by: x take away 4. Feed most x\'s "
             "and all is well — but ONE x breaks the machine, because it turns the "
             "bottom into zero, and dividing by zero is the one thing mathematics never "
             "allows. That x is forbidden.",
             '[[goal text="The forbidden x"]]'),
        ],
        "picture": [
            ("Here is the curve of 5 divided by x take away 4. Look at x equals 4: the "
             "curve flies off the top and comes back from the bottom, and never touches "
             "that line. There is no point there at all — the machine jams.",
             '[[graph func="5/(x-4)" range="0..8" yrange="-12..12" caption="y = 5 ÷ (x − 4) — the curve flies off at x = 4 and never lands"]]'),
        ],
        "teach": [
            ("That is the method. Find it by asking when the bottom dies: x take away 4 "
             "equals zero exactly at x equals 4. Feed 4 and the division has no answer "
             "— the machine jams, so 4 is forbidden. Feed anything else — 5, 100, "
             "negative 7 — and the function answers happily. One hole in an endless "
             "road.",
             '[[machine input="4" rule="5 ÷ (x − 4)" output="jammed" caption="x = 4 turns the bottom to zero — forbidden"]][[step eq="x − 4 = 0"]][[step eq="x = 4 forbidden"]]'),
            ("Two traps, both old friends. The minus begs for negative 4 — but feed "
             "negative 4 and the bottom is negative 8, alive and well: the vertex lesson "
             "taught you that flip. And zero is not automatically dangerous — feed x "
             "equals 0 and the bottom is negative 4, fine. The danger is where the "
             "BOTTOM is zero, not where x is.",
             '[[step eq="x = 4 forbidden ✓"]][[step eq="−4 ✗ the flip · 0 ✗ the bottom there is −4, alive"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. y equals 7 divided by: x take "
                        "away 6. The bottom dies at x equals 6 — forbidden.",
                        '[[graph func="7/(x-6)" range="2..10" yrange="-12..12" caption="y = 7 ÷ (x − 6) — flies off at x = 6"]][[step eq="x − 6 = 0"]][[step eq="x = 6"]]'),
             "ask": {'a': 3, 'b': 8, 'op': 'excl'}},
            {"worked": ("One more together. y equals 2 divided by: x take away 9 — the "
                        "forbidden x is 9.",
                        '[[graph func="2/(x-9)" range="5..13" yrange="-12..12" caption="y = 2 ÷ (x − 9) — flies off at x = 9"]][[step eq="x − 9 = 0"]][[step eq="x = 9"]]'),
             "ask": {'a': 11, 'b': 7, 'op': 'excl'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. y equals 5 divided "
                       "by x take away 4, and the forbidden x is 4. Tap the reason why."),
            "choices": ("because at x equals 4 the bottom is zero | because the minus "
                        "means the forbidden x is negative 4 | because zero is always "
                        "the forbidden x"),
            "answer": "because at x equals 4 the bottom is zero",
            "board": '[[graph func="5/(x-4)" range="0..8" yrange="-12..12" caption="the hole at x = 4"]]',
        },
        "recap": [
            ("So, here it is again. A division function forbids the one x that turns "
             "its bottom into zero — find it by asking when the bottom dies. Not the "
             "sign flipped, and not zero by habit: the danger is where the bottom is "
             "zero, not where x is.",
             '[[graph func="5/(x-4)" range="0..8" yrange="-12..12" caption="one hole in an endless road"]]'),
            ("And that is the first x a function ever refused.",
             '[[step eq="x − 4 = 0 · x = 4 forbidden"]]'),
        ],
        "bank": [
            {"a": 2, "b": 3, "op": "excl"},
            {"a": 3, "b": 5, "op": "excl"},
            {"a": 4, "b": 2, "op": "excl"},
            {"a": 5, "b": 7, "op": "excl"},
            {"a": 6, "b": 4, "op": "excl"},
            {"a": 7, "b": 9, "op": "excl"},
            {"a": 8, "b": 3, "op": "excl"},
            {"a": 9, "b": 6, "op": "excl"},
            {"a": 10, "b": 8, "op": "excl"},
            {"a": 12, "b": 5, "op": "excl"},
        ],
    },
    {
        "id": "alg2-u4-the-survivor",
        "course": "algebra2", "unit": 4,
        "topic": "The far horizon",
        "op": "rasy", "max_value": 9, "min_value": 0,
        "levels": ("abstract",),
        "symbols": ("settles", "huge"),
        "advance_line": "Three in a row, and you can say why — you've got it! Find who lives, then answer.",
        "why": [
            ("Why a survivor? Because the last lesson of the unit asks what happens "
             "far, far away. y equals 6 divided by x fades as x grows huge — share 6 "
             "among a million and each gets almost nothing. But y equals: 2 x plus 6, "
             "all divided by x, hides a survivor. Split it and see.",
             '[[goal text="The survivor"]]'),
        ],
        "picture": [
            ("Here is the curve, with a level line drawn at 2. Watch the curve as x "
             "grows: it drops fast, then flattens, and slides closer and closer to that "
             "line without ever quite landing on it. The 2 is the survivor.",
             '[[graph func="(2*x+6)/x" lines="y=2" range="0..20" caption="y = (2x + 6) ÷ x — it settles toward the line y = 2"]]'),
        ],
        "teach": [
            ("That is the method. Split the top: 2 x divided by x is just 2; 6 divided "
             "by x is the fading part. So y equals 2 plus 6-divided-by-x. Let x grow "
             "huge: the fading part dies toward zero, the 2 stands untouched — y "
             "settles toward 2.",
             '[[graph func="(2*x+6)/x" lines="y=2" range="0..20" caption="y = 2 + 6 ÷ x — the 6 ÷ x dies, the 2 survives"]][[step eq="y = 2 + 6 ÷ x"]][[step eq="settles at 2"]]'),
            ("The traps are the two other numbers in the room. Zero was plain "
             "division\'s answer — 6 over x alone dies — but today\'s function keeps "
             "a survivor, and tapping 0 forgets him. And 6 is the fading part\'s number "
             "— the part that dies. The survivor is the number riding on x. Find who "
             "lives, then answer.",
             '[[step eq="settles at 2 ✓"]][[step eq="0 ✗ that was plain 6 ÷ x · 6 ✗ the fading part"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. y equals: 3 x plus 8, all divided "
                        "by x. Split: 3 plus 8 over x — it settles toward 3.",
                        '[[graph func="(3*x+8)/x" lines="y=3" range="0..20" caption="y = 3 + 8 ÷ x — settles toward 3"]][[step eq="y = 3 + 8 ÷ x"]][[step eq="settles at 3"]]'),
             "ask": {'a': 4, 'b': 7, 'op': 'rasy'}},
            {"worked": ("One more together. 7 x plus 4, over x: the 4 fades — y settles "
                        "toward 7.",
                        '[[graph func="(7*x+4)/x" lines="y=7" range="0..20" caption="y = 7 + 4 ÷ x — settles toward 7"]][[step eq="y = 7 + 4 ÷ x"]][[step eq="settles at 7"]]'),
             "ask": {'a': 5, 'b': 9, 'op': 'rasy'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. y equals 2 x plus 6, "
                       "all divided by x, and as x grows huge y settles toward 2. Tap the "
                       "reason why."),
            "choices": ("because the 6 over x fades away and the 2 stays | because "
                        "everything divided by a huge x fades to zero | because the 6 "
                        "is the bigger number, so it survives"),
            "answer": "because the 6 over x fades away and the 2 stays",
            "board": '[[graph func="(2*x+6)/x" lines="y=2" range="0..20" caption="the survivor: 2"]]',
        },
        "recap": [
            ("So, here it is again. Split a division function into its parts: whatever "
             "sits over x fades as x grows huge, and whatever rides on x survives. The "
             "curve settles toward the survivor — the level line it never quite lands "
             "on.",
             '[[graph func="(2*x+6)/x" lines="y=2" range="0..20" caption="find who lives, then answer"]]'),
            ("And that is a function, read at the horizon.",
             '[[step eq="y = 2 + 6 ÷ x"]][[step eq="settles at 2"]]'),
        ],
        "bank": [
            {"a": 2, "b": 5, "op": "rasy"},
            {"a": 3, "b": 7, "op": "rasy"},
            {"a": 4, "b": 9, "op": "rasy"},
            {"a": 5, "b": 3, "op": "rasy"},
            {"a": 6, "b": 8, "op": "rasy"},
            {"a": 6, "b": 1, "op": "rasy"},
            {"a": 7, "b": 2, "op": "rasy"},
            {"a": 8, "b": 5, "op": "rasy"},
            {"a": 8, "b": 3, "op": "rasy"},
            {"a": 9, "b": 4, "op": "rasy"},
        ],
    },
]
LESSONS.extend(_ALGEBRA2_U4)


# =============================================================================
# ALGEBRA II -- UNIT 5: RADICALS & RATIONAL EXPONENTS (build lj, 2026-08-22)
# =============================================================================
# THE ROOT IS A POWER IN DISGUISE, AND NEVER A HALVING. Roots times under one
# roof, the one-half power unmasked, the radical equation undone (the undo is
# the SQUARE, not the double), and estimation between the squares. The halving
# misconception is the unit's standing wrong tap -- three of four lessons.
_ALGEBRA2_U5 = [
    {
        "id": "alg2-u5-under-one-roof",
        "course": "algebra2", "unit": 5,
        "topic": "Roots multiply",
        "op": "rmul", "max_value": 54,
        "levels": ("abstract",),
        "symbols": ("square root", "times"),
        "advance_line": "Three in a row, and you can say why — you've got it! Roots times under one roof.",
        "why": [
            ("Why one roof? Because roots come back with a rule that turns ragged "
             "numbers clean. The square root of 2 is a messy, unending decimal. But the "
             "root of 2 times the root of 2 is exactly 2. In general, two roots can go "
             "under one roof: root of a, times root of b, equals the root of a times b.",
             '[[goal text="Under one roof"]][[step eq="√a · √b = √(a·b)"]]'),
        ],
        "picture": [
            ("Here is the square that the two roots make together. The square root of "
             "3 times the square root of 48 is the root of 3 times 48 — the root of 144 "
             "— and 144 is a perfect square: 12 rows of 12. The side of that square, "
             "12, is the answer.",
             '[[rectangle w="12" h="12" caption="√3 · √48 = √144 — and 144 is 12 × 12"]]'),
        ],
        "teach": [
            ("That is the method. The square root of 3, times the square root of 48. "
             "Alone, each is ragged. Under one roof: 3 times 48 is 144 — and 144 is a "
             "perfect square! Twelve times twelve. Two messy roots, one clean answer: "
             "12.",
             '[[rectangle w="12" h="12" caption="144 = 12 × 12"]][[step eq="√3 · √48 = √144"]][[step eq="12 × 12 = 144"]][[step eq="√144 = 12"]]'),
            ("Two traps. 144 is what sits UNDER the roof — the root still has to be "
             "taken; stopping there is the same slip as stopping at the square back in "
             "Pythagoras. And the roots never ADD: root 3 plus root 48 is 51 under "
             "nobody\'s roof — adding under roots is the famous illegal move.",
             '[[step eq="√3 · √48 = 12 ✓"]][[step eq="144 ✗ still under the roof · 51 ✗ roots never add"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Root 2 times root 32: under one "
                        "roof, 64 — and the root of 64 is 8.",
                        '[[array rows="8" cols="8" caption="√2 · √32 = √64 — and 64 is 8 × 8"]][[step eq="√2 · √32 = √64 = 8"]]'),
             "ask": {'a': 5, 'b': 45, 'op': 'rmul'}},
            {"worked": ("One more together. Root 3 times root 75: 225 under the roof, and "
                        "15 times 15 is 225 — the answer is 15.",
                        '[[rectangle w="15" h="15" caption="√3 · √75 = √225 — and 225 is 15 × 15"]][[step eq="√3 · √75 = √225 = 15"]]'),
             "ask": {'a': 6, 'b': 54, 'op': 'rmul'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. The square root of "
                       "3 times the square root of 48 is 12. Tap the reason why."),
            "choices": ("because under one roof, 3 times 48 is a perfect square | because "
                        "under one roof, 3 plus 48 is a perfect square | because the "
                        "answer is 144, the number under the roof"),
            "answer": "because under one roof, 3 times 48 is a perfect square",
            "board": '[[rectangle w="12" h="12" caption="√144 = 12"]]',
        },
        "recap": [
            ("So, here it is again. Two square roots timesed go under one roof: the root "
             "of the product. If that product is a perfect square, two ragged roots "
             "give one clean whole number — its side. Take the root at the end, and "
             "never add under the roofs.",
             '[[rectangle w="12" h="12" caption="√3 · √48 = √144 = 12"]]'),
            ("And that is a roof that turns messy numbers clean.",
             '[[step eq="√a · √b = √(a·b)"]]'),
        ],
        "bank": [
            {"a": 2, "b": 8, "op": "rmul"},
            {"a": 3, "b": 12, "op": "rmul"},
            {"a": 2, "b": 18, "op": "rmul"},
                        {"a": 3, "b": 27, "op": "rmul"},
            {"a": 5, "b": 20, "op": "rmul"},
            {"a": 2, "b": 50, "op": "rmul"},
            {"a": 6, "b": 24, "op": "rmul"},
            {"a": 8, "b": 18, "op": "rmul"},
            {"a": 7, "b": 28, "op": "rmul"},
        ],
    },
    {
        "id": "alg2-u5-the-fraction-power",
        "course": "algebra2", "unit": 5,
        "topic": "Rational exponents",
        "op": "rpow", "max_value": 676,
        "levels": ("abstract",),
        "symbols": ("one-half power", "square root"),
        "advance_line": "Three in a row, and you can say why — you've got it! A one-half power is a root, never a halving.",
        "why": [
            ("Why a fraction in the exponent? Because exponents can wear fractions. "
             "What could 25 to the one-half power mean? Follow the adding rule: 25 to "
             "the one-half, times 25 to the one-half, is 25 to the one — plain 25. So "
             "the one-half power is the number that times ITSELF into 25. That is a "
             "square root.",
             '[[goal text="The fraction power"]][[step eq="25^½ · 25^½ = 25¹"]]'),
        ],
        "picture": [
            ("Here are the two numbers side by side: the square root of 25, which is 5, "
             "and half of 25, which is 12 and a half. They are nowhere near each other. "
             "The one-half power is the small one — the root.",
             '[[bars data="√25 = 5:5 | half of 25:12.5" caption="the root, 5, beside the halving trap, 12.5"]]'),
        ],
        "teach": [
            ("That is the method. 25 to the one-half power is the square root of 25 — "
             "which is 5. Check it: 5 times 5 is 25. The fraction in the exponent is "
             "not arithmetic waiting to happen; it is a costume the root wears.",
             '[[array rows="5" cols="5" caption="5 × 5 = 25 — so 25^½ = 5"]][[step eq="25^½ = √25 = 5"]][[step eq="5 × 5 = 25 ✓"]]'),
            ("The trap reads the costume literally: one-half power, so take half — half "
             "of 25 is 12 and a half. But 12.5 times 12.5 is over 156, nowhere near 25. "
             "Halving splits a number; the one-half power UNBUILDS a square. A root, "
             "never a halving.",
             '[[step eq="25^½ = 5 ✓"]][[step eq="half of 25 ✗ — halving is not rooting"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 100 to the one-half power: the "
                        "square root of 100 — 10.",
                        '[[array rows="10" cols="10" caption="10 × 10 = 100 — so 100^½ = 10"]][[step eq="100^½ = √100 = 10"]]'),
             "ask": {'a': 16, 'b': 0, 'op': 'rpow'}},
            {"worked": ("One more together. 900 to the one-half power: the root of 900 is "
                        "30.",
                        '[[bars data="√900 = 30:30 | half of 900:450" caption="the root, 30 — not the half, 450"]][[step eq="900^½ = √900 = 30"]]'),
             "ask": {'a': 676, 'b': 0, 'op': 'rpow'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 25 to the one-half "
                       "power is 5. Tap the reason why."),
            "choices": ("because the one-half power is the square root | because the "
                        "one-half power means take half | because the one-half power "
                        "leaves the number alone"),
            "answer": "because the one-half power is the square root",
            "board": '[[array rows="5" cols="5" caption="25^½ = √25 = 5"]]',
        },
        "recap": [
            ("So, here it is again. A one-half power is the number that times itself "
             "into the base — the square root. The fraction is a costume the root "
             "wears; it is never an instruction to halve.",
             '[[bars data="√25 = 5:5 | half of 25:12.5" caption="a root, never a halving"]]'),
            ("And that is an exponent that unbuilds a square.",
             '[[step eq="25^½ = √25 = 5"]]'),
        ],
        "bank": [
            {"a": 36, "b": 0, "op": "rpow"},
            {"a": 64, "b": 0, "op": "rpow"},
                        {"a": 144, "b": 0, "op": "rpow"},
            {"a": 196, "b": 0, "op": "rpow"},
            {"a": 256, "b": 0, "op": "rpow"},
            {"a": 324, "b": 0, "op": "rpow"},
            {"a": 400, "b": 0, "op": "rpow"},
            {"a": 484, "b": 0, "op": "rpow"},
            {"a": 576, "b": 0, "op": "rpow"},
        ],
    },
    {
        "id": "alg2-u5-undo-the-root",
        "course": "algebra2", "unit": 5,
        "topic": "Radical equations",
        "op": "rsq", "max_value": 196,
        "levels": ("abstract",),
        "symbols": ("square root", "undo"),
        "advance_line": "Three in a row, and you can say why — you've got it! The root's undo is the square.",
        "why": [
            ("Why undo it? Because now the root lands in an equation: the square root "
             "of x equals 15. Something, rooted, gave 15 — find the something. Every "
             "equation move since Algebra One is an undo, and the square root\'s undo "
             "is its opposite power: the SQUARE.",
             '[[goal text="Undo the root"]]'),
        ],
        "picture": [
            ("Here is the machine that roots. Its rule is the square root of x, its "
             "output came out as 15, and its input door is blank. Whatever went in, "
             "rooted, became 15 — and the undo finds it.",
             '[[machine input="?" rule="√x" output="15" caption="the output is 15 — which x went in?"]]'),
        ],
        "teach": [
            ("That is the method. Square both sides: the root of x, squared, is plain x "
             "— and 15 squared is 225. So x is 225. Check by rooting it forward: the "
             "square root of 225 is 15. True.",
             '[[machine input="225" rule="√x" output="15" caption="x = 15² = 225 — check: √225 = 15"]][[step eq="x = 15² = 225"]][[step eq="check: √225 = 15 ✓"]]'),
            ("The trap is the halving family again, inverted: if root felt like half, "
             "its undo feels like DOUBLE — 30. But the root of 30 is between 5 and 6, "
             "nowhere near 15. And x is not just 15 handed back: the root already "
             "changed it. Undo with the square, then check forward.",
             '[[step eq="x = 225 ✓"]][[step eq="30 ✗ doubling undoes halving, not rooting · 15 ✗ unchanged"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. The square root of x equals 20: x "
                        "is 20 squared — 400. Check: root 400 is 20.",
                        '[[machine input="400" rule="√x" output="20" caption="x = 20² = 400"]][[step eq="√x = 20"]][[step eq="x = 400"]]'),
             "ask": {'a': 3, 'b': 0, 'op': 'rsq'}},
            {"worked": ("One more together. Root of x equals 16: x is 16 squared — 256.",
                        '[[machine input="256" rule="√x" output="16" caption="x = 16² = 256"]][[step eq="√x = 16"]][[step eq="x = 256"]]'),
             "ask": {'a': 14, 'b': 0, 'op': 'rsq'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. The square root of "
                       "x equals 15, and x is 225. Tap the reason why."),
            "choices": ("because the square undoes the root: 15 times itself | "
                        "because doubling undoes the root: 15 doubled | because the "
                        "root changes nothing, so x is 15"),
            "answer": "because the square undoes the root: 15 times itself",
            "board": '[[machine input="225" rule="√x" output="15" caption="x = 15² = 225"]]',
        },
        "recap": [
            ("So, here it is again. When the square root of x equals a number, undo the "
             "root with its opposite power — square the number, and that is x. Then "
             "check forward by rooting it. Never double, and never hand the number back "
             "unchanged.",
             '[[machine input="225" rule="√x" output="15" caption="the root\'s undo is the square"]]'),
            ("And that is a radical equation, undone.",
             '[[step eq="x = 15² = 225"]]'),
        ],
        "bank": [
            {"a": 4, "b": 0, "op": "rsq"},
            {"a": 5, "b": 0, "op": "rsq"},
            {"a": 6, "b": 0, "op": "rsq"},
            {"a": 7, "b": 0, "op": "rsq"},
            {"a": 8, "b": 0, "op": "rsq"},
            {"a": 9, "b": 0, "op": "rsq"},
            {"a": 10, "b": 0, "op": "rsq"},
            {"a": 11, "b": 0, "op": "rsq"},
            {"a": 12, "b": 0, "op": "rsq"},
            {"a": 13, "b": 0, "op": "rsq"},
        ],
    },
    {
        "id": "alg2-u5-between-the-squares",
        "course": "algebra2", "unit": 5,
        "topic": "Estimating roots",
        "op": "rbet", "max_value": 150,
        "levels": ("abstract",),
        "symbols": ("square root", "between"),
        "advance_line": "Three in a row, and you can say why — you've got it! Square the neighbours, then see who is nearer.",
        "why": [
            ("Why between? Because most numbers are not perfect squares — but their "
             "roots still live somewhere. The square root of 40 is not whole; it sits "
             "between two whole numbers, because 40 sits between two perfect squares: "
             "36 and 49. Root of 36 is 6, root of 49 is 7 — so root 40 lives between 6 "
             "and 7.",
             '[[goal text="Between the squares"]][[step eq="36 < 40 < 49"]][[step eq="6 < √40 < 7"]]'),
        ],
        "picture": [
            ("Here is 40 on the number line, between the two squares. The line runs "
             "from 36, which is 6 squared, to 49, which is 7 squared — and 40 sits much "
             "nearer the 36 end. So its root sits much nearer 6.",
             '[[numberline min="36" max="49" points="40" caption="40 between 36 (6²) and 49 (7²) — nearer 36"]]'),
        ],
        "teach": [
            ("That is the method. Which is it closer to? Measure in the world of "
             "squares: 40 sits 4 past 36, and 9 short of 49. It leans toward 36 — so "
             "the root of 40 is closest to 6. Square the neighbours, then see who is "
             "nearer.",
             '[[numberline min="36" max="49" points="40" hops="36,40" caption="40 − 36 = 4 · 49 − 40 = 9 — nearer 36, so √40 → 6"]][[step eq="40 − 36 = 4 · 49 − 40 = 9"]][[step eq="√40 → closest to 6"]]'),
            ("Two traps. First, leaning the wrong way: 7 is a neighbour, but it is the "
             "far one here. Second, the oldest trap in the unit, halving. Half of 40 is "
             "20, and 20 times 20 is 400, absurdly far. The root of a number near 40 "
             "is small — squares grow FAST. Neighbours first, half never.",
             '[[step eq="√40 → 6 ✓"]][[step eq="7 ✗ the far neighbour · 20 ✗ the halving habit"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Root of 90: between 81 and 100, so "
                        "between 9 and 10 — and 90 is 9 past 81, 10 short of 100: closest "
                        "to 9.",
                        '[[numberline min="81" max="100" points="90" hops="81,90" caption="90 − 81 = 9 · 100 − 90 = 10 — nearer 81, so √90 → 9"]][[step eq="81 < 90 < 100 → √90 → 9"]]'),
             "ask": {'a': 20, 'b': 0, 'op': 'rbet'}},
            {"worked": ("One more together. Root of 30: between 25 and 36, and 30 leans "
                        "toward 25 — closest to 5.",
                        '[[numberline min="25" max="36" points="30" hops="25,30" caption="30 − 25 = 5 · 36 − 30 = 6 — nearer 25, so √30 → 5"]][[step eq="25 < 30 < 36 → √30 → 5"]]'),
             "ask": {'a': 84, 'b': 0, 'op': 'rbet'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. The square root of "
                       "40 is closest to 6. Tap the reason why."),
            "choices": ("because 40 sits nearer 36 than 49 | because 40 sits nearer 49 "
                        "than 36 | because half of 40 lands close to 6"),
            "answer": "because 40 sits nearer 36 than 49",
            "board": '[[numberline min="36" max="49" points="40" hops="36,40" caption="nearer 36, so √40 → 6"]]',
        },
        "recap": [
            ("So, here it is again. A root that is not whole lives between two whole "
             "numbers — the roots of the two perfect squares around it. Square the "
             "neighbours, see which square the number sits nearer, and that neighbour "
             "is the closest root. Never halve.",
             '[[numberline min="36" max="49" points="40" caption="square the neighbours, then see who is nearer"]]'),
            ("And that is a ragged root, placed.",
             '[[step eq="6 < √40 < 7 → closest to 6"]]'),
        ],
        "bank": [
            {"a": 12, "b": 0, "op": "rbet"},
            {"a": 18, "b": 0, "op": "rbet"},
            {"a": 27, "b": 0, "op": "rbet"},
            {"a": 33, "b": 0, "op": "rbet"},
            {"a": 44, "b": 0, "op": "rbet"},
            {"a": 55, "b": 0, "op": "rbet"},
            {"a": 68, "b": 0, "op": "rbet"},
            {"a": 78, "b": 0, "op": "rbet"},
            {"a": 105, "b": 0, "op": "rbet"},
            {"a": 130, "b": 0, "op": "rbet"},
        ],
    },
]
LESSONS.extend(_ALGEBRA2_U5)


# =============================================================================
# ALGEBRA II -- UNIT 6: EXPONENTIAL & LOGARITHMIC FUNCTIONS (build lj)
# =============================================================================
# DECAY MIRRORS THE DOUBLING POND (the linear faller is the wrong tap, exactly
# as alg1-u6's linear thinker was), then the LOGARITHM met as a question --
# "the base raised to WHAT equals this?" -- with its product rule (logs ADD
# when values times: the exadd/pdeg family, one more rung) and estimation
# between the powers (rbet's twin, on purpose).
_ALGEBRA2_U6 = [
    {
        "id": "alg2-u6-the-fading-half",
        "course": "algebra2", "unit": 6,
        "topic": "Exponential decay",
        "op": "hlfl", "max_value": 96,
        "levels": ("abstract",),
        "symbols": ("halves", "decay"),
        "advance_line": "Three in a row, and you can say why — you've got it! A divide each day, never a take away.",
        "why": [
            ("Why the fading half? Because the doubling pond had a shadow. Some things "
             "grow by times — and some things FADE by times: a medicine in the blood, "
             "a hot drink\'s extra warmth, a radioactive speck. Each day the sample "
             "halves — it drops to half of whatever it was. That fading-by-times has a "
             "name: decay.",
             '[[goal text="The fading half"]]'),
        ],
        "picture": [
            ("Here is a sample of 48 grams fading day by day as bars: 48, then 24, then "
             "12, then 6. Each bar is half the one before it. Look how fast the bars "
             "shrink at the start and how small they are by day three.",
             '[[bars data="day 0:48 | day 1:24 | day 2:12 | day 3:6" caption="48 → 24 → 12 → 6 — each bar is half the one before"]]'),
        ],
        "teach": [
            ("That is the method. A sample of 48 grams halves for 3 days: 48 to 24, 24 "
             "to 12, 12 to 6. Three days, three divides — and dividing by 2 three times "
             "is dividing by 8. Big numbers fall FAST when the fall is a times.",
             '[[bars data="day 0:48 | day 1:24 | day 2:12 | day 3:6" caption="three divides: 48 ÷ 8 = 6"]][[step eq="48 → 24 → 12 → 6"]][[step eq="48 ÷ 8 = 6"]]'),
            ("The trap is the linear faller — the doubling pond\'s old enemy, walking "
             "downhill. Down by 2 each day gives 48, 46, 44: after 3 days, 42 — barely a "
             "dent. Halving is a DIVIDE each day, never a take away. And one halving is "
             "not three: keep dividing until the days run out.",
             '[[step eq="48 ÷ 2 ÷ 2 ÷ 2 = 6 ✓"]][[step eq="48 − 6 = 42 ✗ the linear faller · 24 ✗ one day only"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 40 grams, halving for 3 days: 40, "
                        "20, 10, 5 — five grams are left.",
                        '[[bars data="day 0:40 | day 1:20 | day 2:10 | day 3:5" caption="40 → 20 → 10 → 5"]][[step eq="40 ÷ 2 ÷ 2 ÷ 2 = 5"]]'),
             "ask": {'a': 24, 'b': 3, 'op': 'hlfl'}},
            {"worked": ("One more together. 56 grams for 2 days: 56 to 28 to 14.",
                        '[[bars data="day 0:56 | day 1:28 | day 2:14" caption="56 → 28 → 14"]][[step eq="56 ÷ 2 ÷ 2 = 14"]]'),
             "ask": {'a': 64, 'b': 2, 'op': 'hlfl'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A sample of 48 grams "
                       "halves every day, and after 3 days 6 grams are left. Tap the "
                       "reason why."),
            "choices": ("because halving is a divide by 2, done three times | because "
                        "halving is a take away of 2, done three times | because "
                        "halving happens once, however many days pass"),
            "answer": "because halving is a divide by 2, done three times",
            "board": '[[bars data="day 0:48 | day 1:24 | day 2:12 | day 3:6" caption="48 ÷ 2 ÷ 2 ÷ 2 = 6"]]',
        },
        "recap": [
            ("So, here it is again. Decay is fading by times: each day the sample "
             "drops to half of whatever it was — a divide by 2, once for every day, "
             "never a take away. Keep dividing until the days run out.",
             '[[bars data="day 0:48 | day 1:24 | day 2:12 | day 3:6" caption="a divide each day"]]'),
            ("And that is the doubling pond\'s shadow.",
             '[[step eq="48 ÷ 2 ÷ 2 ÷ 2 = 6"]]'),
        ],
        "bank": [
            {"a": 16, "b": 2, "op": "hlfl"},
            {"a": 16, "b": 3, "op": "hlfl"},
            {"a": 24, "b": 2, "op": "hlfl"},
            {"a": 32, "b": 2, "op": "hlfl"},
            {"a": 32, "b": 3, "op": "hlfl"},
            {"a": 40, "b": 2, "op": "hlfl"},
            {"a": 48, "b": 2, "op": "hlfl"},
            {"a": 64, "b": 3, "op": "hlfl"},
            {"a": 80, "b": 4, "op": "hlfl"},
            {"a": 96, "b": 3, "op": "hlfl"},
        ],
    },
    {
        "id": "alg2-u6-the-hidden-exponent",
        "course": "algebra2", "unit": 6,
        "topic": "The logarithm",
        "op": "logb", "max_value": 1024,
        "levels": ("abstract",),
        "symbols": ("logarithm", "power"),
        "advance_line": "Three in a row, and you can say why — you've got it! The logarithm is the hidden exponent.",
        "why": [
            ("Why hidden? Because every power question can turn around. Forward: 3 to "
             "the power 4 is 81. Backwards: 3 raised to WHAT equals 27? Count the "
             "threes: 3 times 3 times 3 — three of them. That backwards question is one "
             "of the great tools of mathematics, and its answer has a name: the "
             "logarithm.",
             '[[goal text="The hidden exponent"]][[step eq="3^? = 27"]][[step eq="? = 3"]]'),
        ],
        "picture": [
            ("Here are the layers of 3 as bars: one 3 is 3, two 3\'s stacked make 9, "
             "three 3\'s stacked make 27. Count the bars it took to reach 27 — three. "
             "That count is the logarithm.",
             '[[bars data="3¹:3 | 3²:9 | 3³:27" caption="three layers of 3 reach 27 — the logarithm is 3"]]'),
        ],
        "teach": [
            ("That is the method. The logarithm is the hidden exponent — nothing more. "
             "10 raised to what equals 100? Two tens: the logarithm is 2. The value can "
             "be enormous while the logarithm stays tiny; that smallness is its whole "
             "power, and why earthquakes and sound are measured in logs.",
             '[[bars data="10¹:10 | 10²:100" caption="two layers of 10 reach 100 — the logarithm is 2"]][[step eq="10^? = 100"]][[step eq="? = 2"]][[step eq="the log counts the layers"]]'),
            ("Two traps. Dividing by the base — 27 divided by 3 is 9 — peels ONE "
             "layer, then stops; the logarithm counts ALL the layers. And the base "
             "itself — the 3 you were handed — is the brick, not the count of bricks. "
             "Count how many times the base stacks, and answer with the count.",
             '[[step eq="3^3 = 27"]][[step eq="log is 3 ✓"]][[step eq="9 ✗ one divide, not the count · 3 as the base ✗ the brick, not the stack"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 5 raised to what equals 125? 5, "
                        "25, 125 — three layers of 5: the logarithm is 3.",
                        '[[bars data="5¹:5 | 5²:25 | 5³:125" caption="three layers of 5 reach 125 — log = 3"]][[step eq="5^3 = 125"]][[step eq="log = 3"]]'),
             "ask": {'a': 8, 'b': 2, 'c': 3, 'op': 'logb'}},
            {"worked": ("One more together. 10 raised to what equals 10,000? Four tens "
                        "stacked — 4.",
                        '[[bars data="10¹:10 | 10²:100 | 10³:1000 | 10⁴:10000" caption="four layers of 10 reach 10,000 — log = 4"]][[step eq="10^4 = 10000"]][[step eq="log = 4"]]'),
             "ask": {'a': 1000, 'b': 10, 'c': 3, 'op': 'logb'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 3 raised to what "
                       "power equals 27? The logarithm is 3. Tap the reason why."),
            "choices": ("because three layers of 3 stack up to 27 | because 27 divided by "
                        "3 is the logarithm | because the base, 3, is the logarithm"),
            "answer": "because three layers of 3 stack up to 27",
            "board": '[[bars data="3¹:3 | 3²:9 | 3³:27" caption="3^3 = 27 — log = 3"]]',
        },
        "recap": [
            ("So, here it is again. A logarithm is a power question turned around: the "
             "base raised to what gives the value? Count how many times the base "
             "stacks, and answer with the count — not one divide, and not the base "
             "itself.",
             '[[bars data="3¹:3 | 3²:9 | 3³:27" caption="the log counts the layers"]]'),
            ("And that is the hidden exponent, found.",
             '[[step eq="3^3 = 27 · log = 3"]]'),
        ],
        "bank": [
            {"a": 16, "b": 2, "c": 4, "op": "logb"},
            {"a": 32, "b": 2, "c": 5, "op": "logb"},
            {"a": 64, "b": 2, "c": 6, "op": "logb"},
            {"a": 81, "b": 3, "c": 4, "op": "logb"},
            {"a": 128, "b": 2, "c": 7, "op": "logb"},
            {"a": 243, "b": 3, "c": 5, "op": "logb"},
            {"a": 256, "b": 2, "c": 8, "op": "logb"},
            {"a": 512, "b": 2, "c": 9, "op": "logb"},
            {"a": 729, "b": 3, "c": 6, "op": "logb"},
            {"a": 1024, "b": 2, "c": 10, "op": "logb"},
        ],
    },
    {
        "id": "alg2-u6-logs-add",
        "course": "algebra2", "unit": 6,
        "topic": "The product rule",
        "op": "logm", "max_value": 128,
        "levels": ("abstract",),
        "symbols": ("logarithm", "product"),
        "advance_line": "Three in a row, and you can say why — you've got it! When values times, their logs put together.",
        "why": [
            ("Why do logs add? Because the logarithm has one great law, and you have "
             "met its family twice: powers add when values times, and degrees add when "
             "polynomials times. Now the logarithm — which IS a hidden exponent — obeys "
             "the same music: the log of a product is the logs, put together.",
             '[[goal text="Logs add"]][[step eq="log(a · b) = log a + log b"]]'),
        ],
        "picture": [
            ("Here are two stacks of doublings as bars, base 2: the log of 2 is 1 — "
             "one doubling — and the log of 16 is 4 — four doublings. Join the two "
             "stacks and you get a stack of five: the log of 32, which is 2 times 16.",
             '[[bars data="log 2:1 | log 16:4 | log 32:5" caption="one doubling joined with four doublings is five — log 32 = 5"]]'),
        ],
        "teach": [
            ("That is the method. Base 2: the log of 2 is 1, and the log of 16 is 4. "
             "Their product is 2 times 16 — 32. Stack it: one doubling joined with four "
             "doublings is five doublings, so the log of 32 is 1 plus 4 — 5. Check: 2 "
             "to the 5 is 32. True.",
             '[[bars data="log 2:1 | log 16:4 | log 32:5" caption="1 + 4 = 5"]][[step eq="log 2 = 1 · log 16 = 4"]][[step eq="log 32 = 1 + 4 = 5 ✓"]]'),
            ("Two traps. Multiplying the logs — 1 times 4 — treats the counts like "
             "values; but logs are COUNTS of layers, and joined stacks add their "
             "counts. And adding the values — 2 plus 16 is 18 — mixes the two worlds "
             "entirely. Values times; logs add. Never both at once.",
             '[[step eq="log(2 · 16) = 1 + 4 = 5 ✓"]][[step eq="1 × 4 = 4 ✗ counts add · 2 + 16 = 18 ✗ wrong world"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Log of 2 is 1, log of 64 is 6; 2 "
                        "times 64 is 128, and its log is 1 plus 6 — 7.",
                        '[[bars data="log 2:1 | log 64:6 | log 128:7" caption="1 + 6 = 7"]][[step eq="log 128 = 1 + 6 = 7"]]'),
             "ask": {'a': 4, 'b': 64, 'op': 'logm'}},
            {"worked": ("One more together. Log of 64 is 6, log of 128 is 7 — the log of "
                        "their product is 13.",
                        '[[bars data="log 64:6 | log 128:7 | log 8192:13" caption="6 + 7 = 13"]][[step eq="6 + 7 = 13"]]'),
             "ask": {'a': 16, 'b': 128, 'op': 'logm'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. The log of 2 is 1 "
                       "and the log of 16 is 4, so the log of 32 is 5. Tap the reason "
                       "why."),
            "choices": ("because joined stacks add their counts of doublings | because "
                        "joined stacks times their counts of doublings | because the "
                        "values 2 and 16 are added"),
            "answer": "because joined stacks add their counts of doublings",
            "board": '[[bars data="log 2:1 | log 16:4 | log 32:5" caption="values times; logs add"]]',
        },
        "recap": [
            ("So, here it is again. A logarithm counts layers, and when two values are "
             "timesed their stacks of layers join — so the log of the product is the "
             "two logs added. Values times; logs add; never both at once.",
             '[[bars data="log 2:1 | log 16:4 | log 32:5" caption="log(2 · 16) = 1 + 4"]]'),
            ("And that is the logarithm\'s one great law.",
             '[[step eq="log(a · b) = log a + log b"]]'),
        ],
        "bank": [
            {"a": 4, "b": 8, "op": "logm"},
            {"a": 4, "b": 16, "op": "logm"},
            {"a": 8, "b": 16, "op": "logm"},
            {"a": 4, "b": 32, "op": "logm"},
            {"a": 8, "b": 32, "op": "logm"},
            {"a": 16, "b": 32, "op": "logm"},
            {"a": 8, "b": 64, "op": "logm"},
            {"a": 16, "b": 64, "op": "logm"},
            {"a": 32, "b": 64, "op": "logm"},
            {"a": 32, "b": 128, "op": "logm"},
        ],
    },
    {
        "id": "alg2-u6-between-the-powers",
        "course": "algebra2", "unit": 6,
        "topic": "Estimating logarithms",
        "op": "lbet", "max_value": 120,
        "levels": ("abstract",),
        "symbols": ("logarithm", "between"),
        "advance_line": "Three in a row, and you can say why — you've got it! Power the neighbours, then see who is nearer.",
        "why": [
            ("Why between the powers? Because most numbers are not perfect powers — "
             "but their logarithms still live somewhere, exactly as ragged roots lived "
             "between the squares. Take the logarithm, base 2, of 18: 18 is not a power "
             "of 2, but it sits between 16 and 32 — between 2 to the 4 and 2 to the 5. "
             "So its log lives between 4 and 5.",
             '[[goal text="Between the powers"]][[step eq="16 < 18 < 32"]][[step eq="4 < log 18 < 5"]]'),
        ],
        "picture": [
            ("Here are the two powers and the number between them as bars: 16, then "
             "18, then 32. The 18 bar is barely taller than the 16 bar and far short of "
             "the 32 bar — it leans hard toward 16.",
             '[[bars data="2⁴:16 | 18:18 | 2⁵:32" caption="18 between the powers 16 and 32 — nearer 16"]]'),
        ],
        "teach": [
            ("That is the method. Which is it closer to? 18 sits 2 past 16, and 14 "
             "short of 32 — it leans hard toward 16, so the log of 18 is closest to 4. "
             "Same move as the squares: power the neighbours, then see who is nearer.",
             '[[bars data="2⁴:16 | 18:18 | 2⁵:32" caption="18 − 16 = 2 · 32 − 18 = 14 — nearer 16, so log 18 → 4"]][[step eq="18 − 16 = 2 · 32 − 18 = 14"]][[step eq="log 18 → closest to 4"]]'),
            ("The traps repeat their old shapes: 5 is the far neighbour here. And "
             "halving — 18 divided by 2 is 9 — is not a logarithm; 2 to the 9 is 512, "
             "absurdly past 18. Logs count layers, and layers pile up FAST. Neighbours "
             "first, half never.",
             '[[step eq="log 18 → 4 ✓"]][[step eq="5 ✗ the far neighbour · 9 ✗ the halving habit"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Log base 2 of 40: between 32 and "
                        "64, so between 5 and 6 — and 40 leans toward 32: closest to 5.",
                        '[[bars data="2⁵:32 | 40:40 | 2⁶:64" caption="40 − 32 = 8 · 64 − 40 = 24 — nearer 32, so log 40 → 5"]][[step eq="32 < 40 < 64 → log 40 → 5"]]'),
             "ask": {'a': 17, 'b': 0, 'op': 'lbet'}},
            {"worked": ("One more together. Log base 2 of 26: it sits 10 past 16 and only "
                        "6 short of 32 — closest to 5.",
                        '[[bars data="2⁴:16 | 26:26 | 2⁵:32" caption="26 − 16 = 10 · 32 − 26 = 6 — nearer 32, so log 26 → 5"]][[step eq="16 < 26 < 32 → log 26 → 5"]]'),
             "ask": {'a': 90, 'b': 0, 'op': 'lbet'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. The logarithm base "
                       "2 of 18 is closest to 4. Tap the reason why."),
            "choices": ("because 18 sits nearer 16 than 32 | because 18 sits nearer 32 "
                        "than 16 | because half of 18 lands near 4"),
            "answer": "because 18 sits nearer 16 than 32",
            "board": '[[bars data="2⁴:16 | 18:18 | 2⁵:32" caption="nearer 16, so log 18 → 4"]]',
        },
        "recap": [
            ("So, here it is again. A logarithm that is not whole lives between the "
             "logs of the two powers around its number. Power the neighbours, see which "
             "power the number sits nearer, and that neighbour is the closest log. "
             "Never halve.",
             '[[bars data="2⁴:16 | 18:18 | 2⁵:32" caption="power the neighbours, then see who is nearer"]]'),
            ("And that is a ragged logarithm, placed.",
             '[[step eq="4 < log 18 < 5 → closest to 4"]]'),
        ],
        "bank": [
            {"a": 13, "b": 0, "op": "lbet"},
            {"a": 20, "b": 0, "op": "lbet"},
            {"a": 28, "b": 0, "op": "lbet"},
            {"a": 35, "b": 0, "op": "lbet"},
            {"a": 50, "b": 0, "op": "lbet"},
            {"a": 60, "b": 0, "op": "lbet"},
            {"a": 70, "b": 0, "op": "lbet"},
            {"a": 100, "b": 0, "op": "lbet"},
            {"a": 110, "b": 0, "op": "lbet"},
            {"a": 120, "b": 0, "op": "lbet"},
        ],
    },
]
LESSONS.extend(_ALGEBRA2_U6)


# =============================================================================
# ALGEBRA II -- UNIT 7: SEQUENCES & SERIES (build lk, 2026-08-22)
# =============================================================================
# A PATTERN IS A RULE YOU CAN RIDE. The arithmetic closed form (the off-by-one
# trap: term c stands c-1 steps from the start), the geometric one (the adding
# habit -- times-not-add, one more time), Gauss's pairing trick (and the ask
# that lets the child BE nine-year-old Gauss: the teach tells the 1-to-100
# story but withholds the number), and walking a recursive rule as contrast.
_ALGEBRA2_U7 = [
    {
        "id": "alg2-u7-ride-the-pattern",
        "course": "algebra2", "unit": 7,
        "topic": "Arithmetic sequences",
        "op": "anth", "max_value": 80,
        "levels": ("abstract",),
        "symbols": ("term", "step"),
        "advance_line": "Three in a row, and you can say why — you've got it! Term one is already standing at the start.",
        "why": [
            ("Why ride? Because a pattern with a steady step is a road you can ride. "
             "4, 7, 10, 13 — it starts at 4 and grows by 3. To find a far-off term, you "
             "could walk: add 3, add 3, add 3… or you could RIDE: count the steps and "
             "jump there in one move.",
             '[[goal text="Ride the pattern"]][[step eq="4, 7, 10, 13, …"]]'),
        ],
        "picture": [
            ("Here are the first terms as bars, each one 3 taller than the last. Term 1 "
             "is the 4 — it is already standing there before any step is taken. From "
             "term 1 to term 4 the bars climb three steps, not four.",
             '[[bars data="term 1:4 | term 2:7 | term 3:10 | term 4:13" caption="start 4, step 3 — from term 1 to term 4 is three steps"]]'),
        ],
        "teach": [
            ("That is the method. How far is term 10? Careful — the famous trap lives "
             "right here. Term 1 is already standing at the start; walking from term 1 "
             "to term 10 crosses NINE steps, not ten. So term 10 is 4 plus 9 steps of 3 "
             "— 4 plus 27 — 31.",
             '[[bars data="term 1:4 | term 2:7 | term 3:10 | term 4:13 | term 10:31" caption="nine steps of 3 from 4 — term 10 is 31"]][[step eq="term 1 → term 10: 9 steps"]][[step eq="4 + 9 × 3 = 31"]]'),
            ("Take ten steps instead and you land at 34 — one term too far. It is the "
             "fencepost from the grid unit, wearing a new coat: posts and rails, terms "
             "and steps. Terms count the posts; the ride is the rails. One fewer step "
             "than the term number, every time.",
             '[[step eq="4 + 9 × 3 = 31 ✓"]][[step eq="4 + 10 × 3 = 34 ✗ — one step too many"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Start 5, step 2, term 8: seven "
                        "steps of 2 is 14, and 5 plus 14 is 19.",
                        '[[bars data="term 1:5 | term 2:7 | term 3:9 | term 8:19" caption="seven steps of 2 from 5 — term 8 is 19"]][[step eq="5 + 7 × 2 = 19"]]'),
             "ask": {'a': 2, 'b': 3, 'c': 5, 'op': 'anth'}},
            {"worked": ("One more together. Start 6, step 4, term 7: six steps — 6 plus "
                        "24 equals 30.",
                        '[[bars data="term 1:6 | term 2:10 | term 3:14 | term 7:30" caption="six steps of 4 from 6 — term 7 is 30"]][[step eq="6 + 6 × 4 = 30"]]'),
             "ask": {'a': 5, 'b': 4, 'c': 9, 'op': 'anth'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A pattern starts at "
                       "4 and grows by 3, and term 10 is 31. Tap the reason why."),
            "choices": ("because term 1 to term 10 is nine steps, not ten | because term "
                        "1 to term 10 is ten steps of 3 | because term 10 is ten times "
                        "the step"),
            "answer": "because term 1 to term 10 is nine steps, not ten",
            "board": '[[bars data="term 1:4 | term 2:7 | term 3:10 | term 4:13 | term 10:31" caption="4 + 9 × 3 = 31"]]',
        },
        "recap": [
            ("So, here it is again. A pattern with a steady step is ridden, not walked: "
             "the start, plus the step taken one fewer time than the term number — "
             "because term 1 is already standing at the start. Posts and rails.",
             '[[bars data="term 1:4 | term 2:7 | term 3:10 | term 4:13" caption="terms are the posts; the ride is the rails"]]'),
            ("And that is the fencepost, in a new coat.",
             '[[step eq="4 + 9 × 3 = 31"]]'),
        ],
        "bank": [
            {"a": 2, "b": 3, "c": 4, "op": "anth"},
            {"a": 3, "b": 2, "c": 6, "op": "anth"},
            {"a": 4, "b": 3, "c": 5, "op": "anth"},
            {"a": 2, "b": 4, "c": 5, "op": "anth"},
            {"a": 5, "b": 3, "c": 6, "op": "anth"},
            {"a": 3, "b": 4, "c": 6, "op": "anth"},
            {"a": 4, "b": 5, "c": 6, "op": "anth"},
            {"a": 2, "b": 5, "c": 8, "op": "anth"},
            {"a": 6, "b": 5, "c": 8, "op": "anth"},
            {"a": 3, "b": 6, "c": 9, "op": "anth"},
        ],
    },
    {
        "id": "alg2-u7-times-again",
        "course": "algebra2", "unit": 7,
        "topic": "Geometric sequences",
        "op": "gnth", "max_value": 96,
        "levels": ("abstract",),
        "symbols": ("term", "ratio"),
        "advance_line": "Three in a row, and you can say why — you've got it! A ratio is a times, never an add.",
        "why": [
            ("Why times again? Because some patterns do not step — they LEAP. 2, 6, 18, "
             "54: each term is 3 times the one before. The times-number has a name, the "
             "ratio, and a pattern that rides a ratio grows the way the doubling pond "
             "grew: slowly at first, then away.",
             '[[goal text="Times again"]][[step eq="2, 6, 18, 54, …"]]'),
        ],
        "picture": [
            ("Here are the terms as bars: 2, then 6, then 18, then 54. Each bar is 3 "
             "times the one before it — look how the bars barely rise at first and "
             "then shoot up. That is a ratio at work, not a step.",
             '[[bars data="term 1:2 | term 2:6 | term 3:18 | term 4:54" caption="start 2, ratio 3 — each bar is 3 times the last"]]'),
        ],
        "teach": [
            ("That is the method. Ride it the same way: term 5 from a start of 2 with "
             "ratio 3 is four leaps — times 3, four times over. 2 times 81 is 162. The "
             "step-counting rule survives: one fewer leap than the term number.",
             '[[bars data="term 1:2 | term 2:6 | term 3:18 | term 4:54 | term 5:162" caption="four leaps of × 3 from 2 — term 5 is 162"]][[step eq="term 5: 4 leaps of × 3"]][[step eq="2 × 81 = 162"]]'),
            ("The trap is the old similarity mistake in a new coat: treating the ratio "
             "as a step. ADDING 3 four times gives 14 — a stroll, while the true "
             "pattern has already leapt past 150. When each term is TIMES the one "
             "before, adding is not slow — it is wrong.",
             '[[step eq="2 × 3 × 3 × 3 × 3 = 162 ✓"]][[step eq="2 + 3 + 3 + 3 + 3 = 14 ✗ — a ratio is not a step"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Start 3, ratio 3, term 3: two "
                        "leaps — 3, 9, 27.",
                        '[[bars data="term 1:3 | term 2:9 | term 3:27" caption="two leaps of × 3 from 3 — term 3 is 27"]][[step eq="3 × 3 × 3 = 27"]]'),
             "ask": {'a': 4, 'b': 2, 'c': 4, 'op': 'gnth'}},
            {"worked": ("One more together. Start 5, ratio 2, term 6: five doublings of 5 "
                        "— 160.",
                        '[[bars data="term 1:5 | term 2:10 | term 3:20 | term 4:40 | term 5:80 | term 6:160" caption="five doublings of 5 — term 6 is 160"]][[step eq="5 × 32 = 160"]]'),
             "ask": {'a': 3, 'b': 3, 'c': 4, 'op': 'gnth'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A pattern starts at "
                       "2 and each term is 3 times the one before, so term 5 is 162. Tap "
                       "the reason why."),
            "choices": ("because term 5 is four leaps of times 3 from 2 | because term 5 "
                        "is four steps of plus 3 from 2 | because term 5 is five leaps "
                        "of times 3 from 2"),
            "answer": "because term 5 is four leaps of times 3 from 2",
            "board": '[[bars data="term 1:2 | term 2:6 | term 3:18 | term 4:54 | term 5:162" caption="2 × 3 × 3 × 3 × 3 = 162"]]',
        },
        "recap": [
            ("So, here it is again. When each term is a times of the one before, the "
             "pattern leaps: ride it with one fewer leap than the term number, timesing "
             "every time. A ratio is a times — adding it is not slow, it is wrong.",
             '[[bars data="term 1:2 | term 2:6 | term 3:18 | term 4:54" caption="a ratio leaps; a step strolls"]]'),
            ("And that is the doubling pond, riding a ratio.",
             '[[step eq="2 × 81 = 162"]]'),
        ],
        "bank": [
            {"a": 2, "b": 2, "c": 3, "op": "gnth"},
            {"a": 3, "b": 2, "c": 3, "op": "gnth"},
            {"a": 2, "b": 2, "c": 4, "op": "gnth"},
            {"a": 2, "b": 3, "c": 3, "op": "gnth"},
            {"a": 5, "b": 2, "c": 3, "op": "gnth"},
            {"a": 3, "b": 2, "c": 4, "op": "gnth"},
            {"a": 2, "b": 2, "c": 5, "op": "gnth"},
            {"a": 5, "b": 2, "c": 4, "op": "gnth"},
            {"a": 3, "b": 2, "c": 5, "op": "gnth"},
            {"a": 2, "b": 3, "c": 4, "op": "gnth"},
        ],
    },
    {
        "id": "alg2-u7-pair-the-ends",
        "course": "algebra2", "unit": 7,
        "topic": "The sum of 1 to n",
        "op": "gaus", "max_value": 5050,
        "levels": ("abstract",),
        "symbols": ("sum", "pair"),
        "advance_line": "Three in a row, and you can say why — you've got it! Pair the ends, times, halve.",
        "why": [
            ("Why pair the ends? A true story. A teacher, wanting quiet, told his class "
             "to add every number from 1 to 100. A nine-year-old named Gauss put his "
             "slate down in seconds — right. He had seen something in the sum no one "
             "had shown him: the ENDS of it belong together.",
             '[[goal text="Pair the ends"]][[step eq="1 + 2 + 3 + … + 100"]]'),
        ],
        "picture": [
            ("Here is the sum 1 up to 10 as a staircase: ten rows, each one longer than "
             "the last, inside a rectangle 10 rows tall and 11 wide. The staircase is "
             "exactly half the rectangle — and that half is the sum.",
             '[[rectangle w="11" h="10" half="1" caption="10 rows of 11 — the staircase is half: the sum"]]'),
        ],
        "teach": [
            ("That is the method. Watch it on 1 to 10. Pair the ends: 1 with 10 is 11. "
             "2 with 9 — 11 again. 3 with 8, 4 with 7, 5 with 6 — every pair is 11, and "
             "ten numbers make five pairs. Five 11s: 55. In general: the last number, "
             "times one more than it, halved.",
             '[[rectangle w="11" h="10" half="1" caption="10 × 11 = 110, halved: 55"]][[step eq="1+10 · 2+9 · 3+8 · 4+7 · 5+6"]][[step eq="5 pairs of 11 = 55"]]'),
            ("The traps: 10 times 10 is 100 — but the numbers being added are mostly "
             "SMALLER than 10, so squaring overshoots. And 10 alone is just the last "
             "footstep of the walk. Pair the ends, times, halve — and in a moment, you "
             "will do what Gauss did.",
             '[[step eq="10 × 11 ÷ 2 = 55 ✓"]][[step eq="100 ✗ overshoots · 10 ✗ the last step only"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 1 up to 13: pair the ends — 1 "
                        "with 13, 2 with 12, and on — every pair is 14. 13 times 14, "
                        "halved: 91.",
                        '[[rectangle w="14" h="13" half="1" caption="13 rows of 14 — half of 182 is 91"]][[step eq="13 × 14 ÷ 2 = 91"]]'),
             "ask": {'a': 11, 'b': 0, 'op': 'gaus'}},
            {"worked": ("One more together. 1 up to 30: 30 times 31, halved — 465.",
                        '[[bars data="30 × 31:930 | halved:465" caption="30 × 31 = 930, halved: 465"]][[step eq="30 × 31 ÷ 2 = 465"]]'),
             "ask": {'a': 100, 'b': 0, 'op': 'gaus'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Every counting "
                       "number from 1 up to 10, put together, is 55. Tap the reason why."),
            "choices": ("because the ends pair into five 11s | because ten numbers of "
                        "about 10 each — a hundred | because the sum is the last number, 10"),
            "answer": "because the ends pair into five 11s",
            "board": '[[rectangle w="11" h="10" half="1" caption="5 pairs of 11 = 55"]]',
        },
        "recap": [
            ("So, here it is again. To add 1 up to any number, pair the ends — every "
             "pair is one more than the last number — then times the last number by "
             "one more than itself, and halve. The staircase is half the rectangle.",
             '[[rectangle w="11" h="10" half="1" caption="pair the ends, times, halve"]]'),
            ("And that is what Gauss saw at nine years old.",
             '[[step eq="10 × 11 ÷ 2 = 55"]]'),
        ],
        "bank": [
            {"a": 4, "b": 0, "op": "gaus"},
            {"a": 5, "b": 0, "op": "gaus"},
            {"a": 6, "b": 0, "op": "gaus"},
            {"a": 7, "b": 0, "op": "gaus"},
            {"a": 8, "b": 0, "op": "gaus"},
            {"a": 9, "b": 0, "op": "gaus"},
            {"a": 12, "b": 0, "op": "gaus"},
            {"a": 14, "b": 0, "op": "gaus"},
            {"a": 15, "b": 0, "op": "gaus"},
            {"a": 20, "b": 0, "op": "gaus"},
        ],
    },
    {
        "id": "alg2-u7-walk-the-rule",
        "course": "algebra2", "unit": 7,
        "topic": "Recursive rules",
        "op": "reca", "max_value": 40,
        "levels": ("abstract",),
        "symbols": ("rule", "term"),
        "advance_line": "Three in a row, and you can say why — you've got it! Apply the WHOLE rule, every term.",
        "why": [
            ("Why walk? Because some patterns hand you no shortcut — only a rule: to "
             "get the next term, take the one before, times 2, then take away 1. Start "
             "at 5. There is nothing to ride here; you walk, one term at a time, "
             "applying the whole rule at every step.",
             '[[goal text="Walk the rule"]][[step eq="rule: × 2, then − 1"]]'),
        ],
        "picture": [
            ("Here is the rule as a machine: times 2, then take away 1. Feed term 1 in "
             "and term 2 comes out — and then term 2 goes back in, and out comes term "
             "3. Each answer feeds the next turn of the machine.",
             '[[machine input="5" rule="2x − 1" output="9" caption="term 1 in, term 2 out — then 9 goes back in"]]'),
        ],
        "teach": [
            ("That is the method. Walk it. Term 1 is 5. Term 2: 2 times 5 is 10, take "
             "away 1 — 9. Term 3: 2 times 9 is 18, take away 1 — 17. Each answer feeds "
             "back in; that is why it is a walk and not a jump.",
             '[[machine input="5" rule="2x − 1" output="9" caption="term 2: 2 × 5 − 1 = 9"]][[machine input="9" rule="2x − 1" output="17" caption="term 3: 2 × 9 − 1 = 17"]][[step eq="5 → 9 → 17"]]'),
            ("Two traps, both about not finishing. Stopping at term 2 answers a "
             "different question — count your arrivals. And applying only HALF the "
             "rule, doubling without taking away, walks a different pattern entirely: "
             "5, 10, 20. The rule is a package: all of it, every term.",
             '[[step eq="5 → 9 → 17 ✓"]][[step eq="9 ✗ stopped early · 18 ✗ the take away got dropped"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Rule: times 2, take away 3. "
                        "Start at 7: term 2 is 11, term 3 is 19.",
                        '[[machine input="7" rule="2x − 3" output="11" caption="term 2: 2 × 7 − 3 = 11"]][[machine input="11" rule="2x − 3" output="19" caption="term 3: 2 × 11 − 3 = 19"]][[step eq="7 → 11 → 19"]]'),
             "ask": {'a': 3, 'b': 1, 'op': 'reca'}},
            {"worked": ("One more together. Times 2, take away 5, from 9: term 2 is 13, "
                        "term 3 is 21.",
                        '[[machine input="9" rule="2x − 5" output="13" caption="term 2: 2 × 9 − 5 = 13"]][[machine input="13" rule="2x − 5" output="21" caption="term 3: 2 × 13 − 5 = 21"]][[step eq="9 → 13 → 21"]]'),
             "ask": {'a': 10, 'b': 6, 'op': 'reca'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. The rule is times 2, "
                       "then take away 1, the first term is 5, and the third term is "
                       "17. Tap the reason why."),
            "choices": ("because the whole rule ran twice: 5 to 9 to 17 | because the "
                        "rule ran once: 5 to 9 | because the doubling ran twice and the "
                        "take away never did"),
            "answer": "because the whole rule ran twice: 5 to 9 to 17",
            "board": '[[machine input="9" rule="2x − 1" output="17" caption="5 → 9 → 17"]]',
        },
        "recap": [
            ("So, here it is again. A rule with no shortcut is walked: apply the whole "
             "of it to the term before, and feed each answer back in, until you arrive "
             "at the term that was asked for. All of the rule, every term.",
             '[[machine input="5" rule="2x − 1" output="9" caption="apply the whole rule, every term"]]'),
            ("And that is a pattern walked, not ridden.",
             '[[step eq="5 → 9 → 17"]]'),
        ],
        "bank": [
            {"a": 3, "b": 2, "op": "reca"},
            {"a": 4, "b": 3, "op": "reca"},
            {"a": 5, "b": 4, "op": "reca"},
            {"a": 4, "b": 2, "op": "reca"},
            {"a": 6, "b": 4, "op": "reca"},
            {"a": 5, "b": 2, "op": "reca"},
            {"a": 6, "b": 3, "op": "reca"},
            {"a": 7, "b": 4, "op": "reca"},
            {"a": 8, "b": 5, "op": "reca"},
            {"a": 9, "b": 4, "op": "reca"},
        ],
    },
]
LESSONS.extend(_ALGEBRA2_U7)


# =============================================================================
# ALGEBRA II -- UNIT 8: TRIGONOMETRIC FUNCTIONS (build lk, 2026-08-22)
# =============================================================================
# THE CIRCLE OF SIZE ONE: an arrow spins from the middle, and sine is the
# HEIGHT of its tip, cosine the ACROSS -- read at the compass points, where
# both are exactly 1, 0 or negative 1 (the whole-number surface; the four base
# angles ARE the world, so the teach shows them -- the turnc precedent -- and
# the spun angles past 360 are the fresh practice). Then the spin that changes
# nothing, and the stretched wave. ⭐ [[unitcircle]] (July's shelf, the last
# non-stats renderer) draws its first scripted lessons -- teach/worked boards
# only: it prints cos and sin at the bottom, the answers.
_ALGEBRA2_U8 = [
    {
        "id": "alg2-u8-the-height",
        "course": "algebra2", "unit": 8,
        "topic": "Sine at the compass points",
        "op": "sinp", "max_value": 1170, "min_value": -1,
        "levels": ("abstract",),
        "symbols": ("sine", "height"),
        "advance_line": "Three in a row, and you can say why — you've got it! Point the arrow, read the height.",
        "why": [
            ("Why a height? Meet the circle that runs all of trigonometry: size one, "
             "an arrow spinning from its middle. The angle says how far the arrow has "
             "turned from flat-right. And the sine of the angle is simply the HEIGHT of "
             "the arrow\'s tip — how far above or below the middle line it sits.",
             '[[goal text="The height"]]'),
        ],
        "picture": [
            ("Here is the circle with the arrow at 90 degrees, pointing straight up. "
             "Its tip sits at the very top: height 1. Read the pair at the tip — the "
             "second number is the height, and it says 1. The sine of 90 is 1.",
             '[[unitcircle angle="90" caption="the arrow at 90° — straight up, height 1: sine 1"]]'),
        ],
        "teach": [
            ("That is the method. At 90 degrees the arrow points straight up: its tip "
             "sits at height 1 — the sine of 90 is 1. Straight down would be height "
             "negative 1. And flat, left or right, the tip has no height at all: sine "
             "0. Four directions, three heights.",
             '[[unitcircle angle="90" caption="straight up → height 1"]][[step eq="up → 1 · down → −1 · flat → 0"]]'),
            ("Keep spinning and nothing new happens: 360 is a full turn — the arrow is "
             "back at flat-right, and every compass point repeats. 630 degrees is a "
             "spin and three quarters: straight down, sine negative 1. Strip away the "
             "full turns, point the arrow, read the height.",
             '[[unitcircle angle="630" caption="630° = 360° + 270° — straight down, height −1"]][[step eq="630° = 360° + 270°"]][[step eq="straight down → −1"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. The sine of 540 degrees: 540 is "
                        "a full spin plus 180 — flat to the left. The height is 0.",
                        '[[unitcircle angle="540" caption="540° = 360° + 180° — flat to the left, height 0"]][[step eq="540° = 360° + 180°"]][[step eq="flat → 0"]]'),
             "ask": {'a': 180, 'b': 0, 'op': 'sinp'}},
            {"worked": ("One more together. The sine of 1260: three full spins plus 180 "
                        "— flat to the left again. Height 0.",
                        '[[unitcircle angle="1260" caption="1260° = 3 × 360° + 180° — flat, height 0"]][[step eq="1260° → flat → 0"]]'),
             "ask": {'a': 990, 'b': 0, 'op': 'sinp'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. The sine of 90 "
                       "degrees is 1. Tap the reason why."),
            "choices": ("because at 90 the arrow points straight up, height 1 | because "
                        "at 90 the arrow lies flat, fully across | because the sine is "
                        "always the angle divided by 90"),
            "answer": "because at 90 the arrow points straight up, height 1",
            "board": '[[unitcircle angle="90" caption="straight up → sine 1"]]',
        },
        "recap": [
            ("So, here it is again. The sine of an angle is the height of the "
             "arrow\'s tip on the unit circle: 1 straight up, negative 1 straight "
             "down, 0 when the arrow lies flat. Strip away the full turns first — they "
             "change nothing.",
             '[[unitcircle angle="90" caption="point the arrow, read the height"]]'),
            ("And that is the circle that runs all of trigonometry.",
             '[[step eq="up → 1 · down → −1 · flat → 0"]]'),
        ],
        "bank": [
            {"a": 0, "b": 0, "op": "sinp"},
                        {"a": 270, "b": 0, "op": "sinp"},
            {"a": 360, "b": 0, "op": "sinp"},
            {"a": 450, "b": 0, "op": "sinp"},
            {"a": 720, "b": 0, "op": "sinp"},
            {"a": 810, "b": 0, "op": "sinp"},
            {"a": 900, "b": 0, "op": "sinp"},
            {"a": 1080, "b": 0, "op": "sinp"},
            {"a": 1170, "b": 0, "op": "sinp"},
        ],
    },
    {
        "id": "alg2-u8-the-across",
        "course": "algebra2", "unit": 8,
        "topic": "Cosine at the compass points",
        "op": "cosp", "max_value": 1170, "min_value": -1,
        "levels": ("abstract",),
        "symbols": ("cosine", "across"),
        "advance_line": "Three in a row, and you can say why — you've got it! Same arrow, other coordinate.",
        "why": [
            ("Why the across? Because the sine read the arrow\'s height, and its "
             "partner, the cosine, reads the ACROSS — how far right or left of the "
             "middle the tip sits. Same circle, same arrow, other coordinate: sine is "
             "up-and-down, cosine is side-to-side.",
             '[[goal text="The across"]]'),
        ],
        "picture": [
            ("Here is the arrow at 0 degrees, lying flat to the right. Its tip sits "
             "fully across — read the pair at the tip: the first number is the across, "
             "and it says 1. The cosine of 0 is 1, while its height, the second "
             "number, is 0.",
             '[[unitcircle angle="0" caption="the arrow at 0° — flat right, across 1: cosine 1"]]'),
        ],
        "teach": [
            ("That is the method. At 0 degrees the arrow points flat-right: fully "
             "across — cosine 1. Flat-left would be across negative 1. And straight up "
             "or straight down, the tip hangs over the middle with no across at all: "
             "cosine 0. The compass points swap their jobs.",
             '[[unitcircle angle="0" caption="flat right → across 1"]][[step eq="right → 1 · left → −1 · up or down → 0"]]'),
            ("Notice the swap exactly. Where the sine was 0, in the flat directions, "
             "the cosine is 1 or negative 1. Where the sine was 1 or negative 1, up and "
             "down, the cosine is 0. Full spins still vanish first: 450 is a spin and a "
             "quarter, straight up — across 0. Point the arrow, then read ACROSS, not "
             "up.",
             '[[unitcircle angle="450" caption="450° = 360° + 90° — straight up, across 0"]][[step eq="450° = 360° + 90°"]][[step eq="up → across 0"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. The cosine of 720 degrees: two "
                        "full spins — flat-right again. Across: 1.",
                        '[[unitcircle angle="720" caption="720° = 2 × 360° — flat right, across 1"]][[step eq="720° → flat right → 1"]]'),
             "ask": {'a': 180, 'b': 0, 'op': 'cosp'}},
            {"worked": ("One more together. The cosine of 1260: three spins plus 180 — "
                        "flat to the left. Across: negative 1.",
                        '[[unitcircle angle="1260" caption="1260° = 3 × 360° + 180° — flat left, across −1"]][[step eq="1260° → flat left → −1"]]'),
             "ask": {'a': 990, 'b': 0, 'op': 'cosp'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. The cosine of 0 "
                       "degrees is 1. Tap the reason why."),
            "choices": ("because at 0 the arrow lies flat right, fully across | because "
                        "at 0 the arrow points straight up | because the cosine is "
                        "always 0 at 0"),
            "answer": "because at 0 the arrow lies flat right, fully across",
            "board": '[[unitcircle angle="0" caption="flat right → cosine 1"]]',
        },
        "recap": [
            ("So, here it is again. The cosine of an angle is the across of the "
             "arrow\'s tip: 1 flat right, negative 1 flat left, 0 straight up or "
             "down. Same arrow as the sine, other coordinate — and full spins vanish "
             "first.",
             '[[unitcircle angle="0" caption="point the arrow, read the across"]]'),
            ("And that is the sine\'s partner.",
             '[[step eq="right → 1 · left → −1 · up or down → 0"]]'),
        ],
        "bank": [
                        {"a": 90, "b": 0, "op": "cosp"},
            {"a": 270, "b": 0, "op": "cosp"},
            {"a": 360, "b": 0, "op": "cosp"},
            {"a": 540, "b": 0, "op": "cosp"},
            {"a": 630, "b": 0, "op": "cosp"},
            {"a": 810, "b": 0, "op": "cosp"},
            {"a": 900, "b": 0, "op": "cosp"},
            {"a": 1080, "b": 0, "op": "cosp"},
            {"a": 1170, "b": 0, "op": "cosp"},
        ],
    },
    {
        "id": "alg2-u8-spin-once-more",
        "course": "algebra2", "unit": 8,
        "topic": "Coterminal angles",
        "op": "spin", "max_value": 440,
        "levels": ("abstract",),
        "symbols": ("full turn", "degrees"),
        "advance_line": "Three in a row, and you can say why — you've got it! Add the whole 360 — same direction, same sine.",
        "why": [
            ("Why spin once more? Here is the circle\'s quiet superpower: a full turn "
             "changes NOTHING. Spin the arrow all the way around — 360 degrees — and "
             "it points exactly where it began. Angles that land the same way have a "
             "bond: everything trigonometric about them is identical.",
             '[[goal text="Spin once more"]]'),
        ],
        "picture": [
            ("Here is the arrow at 45 degrees — and here it is again at 405 degrees. "
             "Look closely: the two pictures are the same arrow, pointing the same "
             "way. The second one has simply been around the circle once more.",
             '[[unitcircle angle="45" values="0" caption="the arrow at 45°"]][[unitcircle angle="405" values="0" caption="the arrow at 405° — the same arrow"]]'),
        ],
        "teach": [
            ("That is the method. Start at 45 degrees and spin one more full turn: 45 "
             "plus 360 is 405. The picture for 405 is the SAME picture — same "
             "direction, same height, same across. The wave repeats forever because "
             "the circle does.",
             '[[unitcircle angle="405" values="0" caption="45° + 360° = 405° — same arrow"]][[step eq="45° + 360° = 405°"]]'),
            ("Two traps. A HALF turn — adding 180 — is real spinning but lands "
             "opposite: everything flips sign. And 360 take away the angle is a "
             "mirror, not a spin — a different arrow entirely. The turn that changes "
             "nothing is the whole 360, added on.",
             '[[step eq="45° + 360° = 405° ✓ same arrow"]][[step eq="+180 ✗ lands opposite · 360 − 45 ✗ a mirror"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 55 degrees, one more full turn: "
                        "55 plus 360 — 415.",
                        '[[unitcircle angle="415" values="0" caption="415° — the same arrow as 55°"]][[step eq="55° + 360° = 415°"]]'),
             "ask": {'a': 35, 'b': 0, 'op': 'spin'}},
            {"worked": ("One more together. 72 degrees plus a full turn: 72 plus 360 — "
                        "432.",
                        '[[unitcircle angle="432" values="0" caption="432° — the same arrow as 72°"]][[step eq="72° + 360° = 432°"]]'),
             "ask": {'a': 65, 'b': 0, 'op': 'spin'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Start at 45 degrees, "
                       "spin one more full turn, and you land on 405. Tap the reason "
                       "why."),
            "choices": ("because a full turn is 360, added on | because a full turn is "
                        "180, added on | because a full turn is 360 take away the angle"),
            "answer": "because a full turn is 360, added on",
            "board": '[[unitcircle angle="405" values="0" caption="45° + 360° = 405°"]]',
        },
        "recap": [
            ("So, here it is again. A full turn is 360 degrees, and adding it changes "
             "nothing — the arrow lands where it began, with the same sine and the "
             "same cosine. A half turn lands opposite, and a mirror is not a spin.",
             '[[unitcircle angle="405" values="0" caption="same direction, same sine, same cosine"]]'),
            ("And that is why the wave repeats forever.",
             '[[step eq="45° + 360° = 405°"]]'),
        ],
        "bank": [
            {"a": 10, "b": 0, "op": "spin"},
            {"a": 15, "b": 0, "op": "spin"},
            {"a": 20, "b": 0, "op": "spin"},
            {"a": 25, "b": 0, "op": "spin"},
            {"a": 30, "b": 0, "op": "spin"},
            {"a": 40, "b": 0, "op": "spin"},
            {"a": 50, "b": 0, "op": "spin"},
            {"a": 60, "b": 0, "op": "spin"},
            {"a": 70, "b": 0, "op": "spin"},
            {"a": 80, "b": 0, "op": "spin"},
        ],
    },
    {
        "id": "alg2-u8-the-stretched-wave",
        "course": "algebra2", "unit": 8,
        "topic": "Amplitude",
        "op": "ampl", "max_value": 30,
        "levels": ("abstract",),
        "symbols": ("amplitude", "wave"),
        "advance_line": "Three in a row, and you can say why — you've got it! The number out front is the crest.",
        "why": [
            ("Why a stretched wave? Because let the circle run and the sine draws a "
             "wave — rising to 1, sinking to negative 1, forever. Now put a number out "
             "front: y equals 20 times the sine of x. Every height gets timesed by 20, "
             "so the whole wave STRETCHES: crest at 20, trough at negative 20.",
             '[[goal text="The stretched wave"]]'),
        ],
        "picture": [
            ("Here is the stretched wave, with a level line drawn across its crests at "
             "20. The wave rises to touch that line and sinks just as far below the "
             "middle, over and over. The 20 out front is exactly how high it reaches.",
             '[[graph func="20*sin(x)" lines="y=20" range="-7..7" caption="y = 20 · sin x — the crest line at 20"]]'),
        ],
        "teach": [
            ("That is the method. The stretch has a name: the amplitude — how high the "
             "wave reaches above its middle line. For y equals 20 times sine, the "
             "amplitude is 20. The number out front IS the crest; no computation, just "
             "recognition.",
             '[[graph func="20*sin(x)" lines="y=20" range="-7..7" caption="crest 20, trough −20 — amplitude 20"]][[step eq="y = 20·sin x"]][[step eq="crest 20, trough −20"]]'),
            ("Two traps. Crest to trough is DOUBLE the amplitude — 40 for our wave — "
             "but amplitude measures from the middle, not the bottom. And the plain "
             "sine\'s crest of 1 is gone the moment a number stands out front: the "
             "stretch happened. Read the front number; that is the top.",
             '[[step eq="y = 20·sin x"]][[step eq="top 20 ✓"]][[step eq="40 ✗ crest-to-trough · 1 ✗ the unstretched habit"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. y equals 13 times the sine of x: "
                        "the wave crests at 13.",
                        '[[graph func="13*sin(x)" lines="y=13" range="-7..7" caption="y = 13 · sin x — crest 13"]][[step eq="crest = 13"]]'),
             "ask": {'a': 11, 'b': 0, 'op': 'ampl'}},
            {"worked": ("One more together. y equals 25 times the sine of x — the highest "
                        "it ever reaches is 25.",
                        '[[graph func="25*sin(x)" lines="y=25" range="-7..7" caption="y = 25 · sin x — crest 25"]][[step eq="crest = 25"]]'),
             "ask": {'a': 15, 'b': 0, 'op': 'ampl'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. The wave y equals 20 "
                       "times the sine of x reaches a highest value of 20. Tap the "
                       "reason why."),
            "choices": ("because the 20 out front stretches every height by 20 | because "
                        "a wave always reaches from its trough to its crest, 40 | because "
                        "every sine wave tops out at 1"),
            "answer": "because the 20 out front stretches every height by 20",
            "board": '[[graph func="20*sin(x)" lines="y=20" range="-7..7" caption="amplitude 20"]]',
        },
        "recap": [
            ("So, here it is again. A number out front of the sine stretches the "
             "wave, and that number is the amplitude — the crest, measured from the "
             "middle line. Not the crest-to-trough swing, and not the plain sine\'s 1.",
             '[[graph func="20*sin(x)" lines="y=20" range="-7..7" caption="the number out front is the crest"]]'),
            ("And that is a wave, stretched and read.",
             '[[step eq="crest = 20"]]'),
        ],
        "bank": [
            {"a": 2, "b": 0, "op": "ampl"},
            {"a": 3, "b": 0, "op": "ampl"},
            {"a": 4, "b": 0, "op": "ampl"},
            {"a": 5, "b": 0, "op": "ampl"},
            {"a": 6, "b": 0, "op": "ampl"},
            {"a": 7, "b": 0, "op": "ampl"},
            {"a": 8, "b": 0, "op": "ampl"},
            {"a": 9, "b": 0, "op": "ampl"},
            {"a": 10, "b": 0, "op": "ampl"},
            {"a": 12, "b": 0, "op": "ampl"},
        ],
    },
]
LESSONS.extend(_ALGEBRA2_U8)


# =============================================================================
# ALGEBRA II -- UNIT 9: STATISTICS & PROBABILITY (build ll, 2026-08-22)
# =============================================================================
# ⭐ ALGEBRA II COMPLETES with the unit that answers questions about what you
# have NOT seen yet. Past alg1-u9 (mean/median/range/outlier) and geo-u9
# (chance counts, counting principle, tables): the mean when scores REPEAT,
# counting with a third slot, what chance pays on average, and the sample
# scaled up to the school.
_ALGEBRA2_U9 = [
    {
        "id": "alg2-u9-the-heavier-mean",
        "course": "algebra2", "unit": 9,
        "topic": "Weighted means",
        "op": "wavg", "max_value": 20,
        "levels": ("abstract",),
        "symbols": ("mean", "weight"),
        "advance_line": "Three in a row, and you can say why — you've got it! Every score goes in as many times as it happened.",
        "why": [
            ("Why heavier? Algebra One taught the mean: put together, share out. But "
             "scores REPEAT — and a score that happens three times pulls three times "
             "as hard. That pull is called its weight. Three quizzes of 10 and two of "
             "5 do not average like one 10 and one 5.",
             '[[goal text="The heavier mean"]]'),
        ],
        "picture": [
            ("Here are the five quizzes as bars: three bars of 10 and two bars of 5, "
             "with the mean drawn beside them at 8. Look where 8 sits — much nearer "
             "the three tall bars than the two short ones. The heavier side dragged "
             "it.",
             '[[bars data="quiz 1:10 | quiz 2:10 | quiz 3:10 | quiz 4:5 | quiz 5:5 | mean:8" caption="three 10s and two 5s — the mean, 8, sits nearer the 10s"]]'),
        ],
        "teach": [
            ("That is the method. Do it honestly: all five scores go in. Three 10s are "
             "30; two 5s are 10; put together, 40 — shared by the five quizzes, the "
             "mean is 8. Notice where 8 sits: closer to 10 than to 5, dragged by the "
             "heavier side.",
             '[[bars data="quiz 1:10 | quiz 2:10 | quiz 3:10 | quiz 4:5 | quiz 5:5 | mean:8" caption="(30 + 10) ÷ 5 = 8"]][[step eq="30 + 10 = 40 · 40 ÷ 5 = 8"]][[step eq="8 sits nearer the three 10s"]]'),
            ("The trap is averaging the two NUMBERS and forgetting how often each "
             "happened. 10 and 5 average to 7 and a half. But that treats a three-time "
             "score and a two-time score as equals. Count the repeats. Every score "
             "goes in as many times as it happened.",
             '[[step eq="mean of the five = 8 ✓"]][[step eq="averaging just 10 and 5 ✗ — the repeats vanished"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Three quizzes of 9 and two of 4: "
                        "27 plus 8 is 35, shared by 5 — the mean is 7.",
                        '[[bars data="quiz 1:9 | quiz 2:9 | quiz 3:9 | quiz 4:4 | quiz 5:4 | mean:7" caption="(27 + 8) ÷ 5 = 7"]][[step eq="(27 + 8) ÷ 5 = 7"]]'),
             "ask": {'a': 13, 'b': 3, 'op': 'wavg'}},
            {"worked": ("One more together. Three 4s and two 14s: 12 plus 28 is 40 — "
                        "mean 8.",
                        '[[bars data="quiz 1:4 | quiz 2:4 | quiz 3:4 | quiz 4:14 | quiz 5:14 | mean:8" caption="(12 + 28) ÷ 5 = 8"]][[step eq="(12 + 28) ÷ 5 = 8"]]'),
             "ask": {'a': 18, 'b': 8, 'op': 'wavg'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Three quizzes scored "
                       "10 and two scored 5, and the mean of all five is 8. Tap the "
                       "reason why."),
            "choices": ("because all five scores go in, and the 10 counts three times | "
                        "because 10 and 5 are averaged, and that is the mean | because "
                        "the score that happened most is the mean"),
            "answer": "because all five scores go in, and the 10 counts three times",
            "board": '[[bars data="quiz 1:10 | quiz 2:10 | quiz 3:10 | quiz 4:5 | quiz 5:5 | mean:8" caption="the heavier side drags the mean"]]',
        },
        "recap": [
            ("So, here it is again. When scores repeat, every score goes into the mean "
             "as many times as it happened — a score that happens three times pulls "
             "three times as hard. Never average the two numbers alone.",
             '[[bars data="quiz 1:10 | quiz 2:10 | quiz 3:10 | quiz 4:5 | quiz 5:5 | mean:8" caption="count the repeats"]]'),
            ("And that is the mean, with its weights on.",
             '[[step eq="(30 + 10) ÷ 5 = 8"]]'),
        ],
        "bank": [
            {"a": 2, "b": 12, "op": "wavg"},
            {"a": 3, "b": 13, "op": "wavg"},
                        {"a": 12, "b": 2, "op": "wavg"},
            {"a": 5, "b": 15, "op": "wavg"},
            {"a": 6, "b": 16, "op": "wavg"},
            {"a": 14, "b": 4, "op": "wavg"},
            {"a": 7, "b": 17, "op": "wavg"},
            {"a": 8, "b": 18, "op": "wavg"},
            {"a": 16, "b": 6, "op": "wavg"},
        ],
    },
    {
        "id": "alg2-u9-three-slots",
        "course": "algebra2", "unit": 9,
        "topic": "The counting principle, grown",
        "op": "cnt3", "max_value": 100,
        "levels": ("abstract",),
        "symbols": ("choice", "slot"),
        "advance_line": "Three in a row, and you can say why — you've got it! Times every slot, skip none.",
        "why": [
            ("Why three slots? Geometry counted outfits from two choices: shirts times "
             "hats. Add pants and nothing changes but the length: every choice is a "
             "slot, and slots TIMES together. 2 shirts, 5 pants, 3 hats — for each "
             "shirt, every pair of pants; for each of those, every hat.",
             '[[goal text="Three slots"]]'),
        ],
        "picture": [
            ("Here is the first pair of slots as a grid: a row for each of the 2 "
             "shirts, a column for each of the 5 pants — ten boxes, ten shirt-and-pants "
             "pairs. The third slot, the hats, then multiplies every one of those "
             "boxes by 3.",
             '[[array rows="2" cols="5" caption="2 shirts by 5 pants — ten pairs; each pair then takes any of 3 hats"]]'),
        ],
        "teach": [
            ("That is the method. Count it: 2 times 5 is 10 shirt-and-pants pairs, and "
             "each pair takes any of 3 hats: 10 times 3 is 30 outfits. Slot by slot, "
             "left to right — the times just keeps rolling.",
             '[[array rows="2" cols="5" caption="2 × 5 = 10 pairs — each with 3 hats: 30"]][[step eq="2 × 5 = 10 · 10 × 3 = 30"]]'),
            ("Two traps, both old friends grown taller. Adding — 2 plus 5 plus 3 is 10 "
             "THINGS, not outfits. And stopping after two slots — 10 — forgets the hats "
             "entirely. However many slots there are: times every one, skip none.",
             '[[step eq="2 × 5 × 3 = 30 ✓"]][[step eq="10 ✗ added, or stopped early"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 3 shirts, 3 pants, 2 hats: 3 "
                        "times 3 is 9, times 2 — 18 outfits.",
                        '[[array rows="3" cols="3" caption="3 × 3 = 9 pairs — each with 2 hats: 18"]][[step eq="3 × 3 × 2 = 18"]]'),
             "ask": {'a': 2, 'b': 3, 'c': 3, 'op': 'cnt3'}},
            {"worked": ("One more together. 4 shirts, 2 pants, 5 hats: 4 times 2 is 8, "
                        "and 8 times 5 is 40 outfits.",
                        '[[array rows="4" cols="2" caption="4 × 2 = 8 pairs — each with 5 hats: 40"]][[step eq="4 × 2 × 5 = 40"]]'),
             "ask": {'a': 5, 'b': 4, 'c': 4, 'op': 'cnt3'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. With 2 shirts, 5 "
                       "pants and 3 hats there are 30 outfits. Tap the reason why."),
            "choices": ("because every slot times the next: shirts, pants, then hats | "
                        "because the three closets add up to the outfits | because "
                        "shirts and pants alone give the outfits, hats aside"),
            "answer": "because every slot times the next: shirts, pants, then hats",
            "board": '[[array rows="2" cols="5" caption="2 × 5 × 3 = 30"]]',
        },
        "recap": [
            ("So, here it is again. Every choice is a slot, and slots times together, "
             "however many there are: shirts times pants times hats. Never add the "
             "closets, and never stop a slot early.",
             '[[array rows="2" cols="5" caption="times every slot, skip none"]]'),
            ("And that is the counting principle, one slot longer.",
             '[[step eq="2 × 5 × 3 = 30"]]'),
        ],
        "bank": [
            {"a": 2, "b": 2, "c": 2, "op": "cnt3"},
            {"a": 2, "b": 2, "c": 3, "op": "cnt3"},
            {"a": 3, "b": 2, "c": 3, "op": "cnt3"},
            {"a": 2, "b": 3, "c": 4, "op": "cnt3"},
            {"a": 2, "b": 4, "c": 4, "op": "cnt3"},
            {"a": 3, "b": 3, "c": 4, "op": "cnt3"},
            {"a": 4, "b": 3, "c": 4, "op": "cnt3"},
            {"a": 4, "b": 4, "c": 4, "op": "cnt3"},
            {"a": 3, "b": 5, "c": 5, "op": "cnt3"},
            {"a": 4, "b": 4, "c": 5, "op": "cnt3"},
        ],
    },
    {
        "id": "alg2-u9-what-to-expect",
        "course": "algebra2", "unit": 9,
        "topic": "Expected value",
        "op": "expv", "max_value": 30,
        "levels": ("abstract",),
        "symbols": ("expect", "tokens"),
        "advance_line": "Three in a row, and you can say why — you've got it! Count the paying plays, then times.",
        "why": [
            ("Why expect? Because chance can be planned for. A game pays 5 tokens, and "
             "you win exactly 2 times out of every 6 plays. Play 6 times: you cannot "
             "say WHICH plays pay — but you can say how much to expect, because about "
             "2 of them will.",
             '[[goal text="What to expect"]]'),
        ],
        "picture": [
            ("Here are the 6 plays as a pie, with the 2 paying plays shaded. Four "
             "slices pay nothing; two slices pay 5 tokens each. The shaded part is "
             "where the tokens come from.",
             '[[pie parts="6" shaded="2" caption="6 plays — 2 of them pay 5 tokens each"]]'),
        ],
        "teach": [
            ("That is the method. Expect it out: 2 winning plays, 5 tokens each — "
             "about 10 tokens over the 6 plays. Not a promise; a center of gravity. "
             "Casinos, insurers and weather planners live on exactly this number.",
             '[[array rows="2" cols="5" caption="2 wins of 5 tokens — 2 × 5 = 10"]][[step eq="2 wins × 5 tokens = 10 expected"]]'),
            ("Two traps. 6 times 5 — 30 — pretends EVERY play pays, but four of the "
             "six pay nothing. And plain 5 counts a single win, as if the other winning "
             "play never came. Count the paying plays first; then times by the prize.",
             '[[step eq="2 × 5 = 10 ✓"]][[step eq="30 ✗ every play paid · 5 ✗ one win only"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Win 4 tokens, 3 times out of 5, "
                        "over 5 plays: 3 wins of 4 — expect 12.",
                        '[[pie parts="5" shaded="3" caption="5 plays, 3 pay 4 tokens — 3 × 4 = 12"]][[step eq="3 × 4 = 12"]]'),
             "ask": {'a': 2, 'b': 3, 'c': 4, 'op': 'expv'}},
            {"worked": ("One more together. 2 wins in 7 plays, 6 tokens each: expect "
                        "about 12.",
                        '[[pie parts="7" shaded="2" caption="7 plays, 2 pay 6 tokens — 2 × 6 = 12"]][[step eq="2 × 6 = 12"]]'),
             "ask": {'a': 5, 'b': 8, 'c': 6, 'op': 'expv'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A game pays 5 tokens "
                       "2 times out of every 6 plays, and over 6 plays you expect 10 "
                       "tokens. Tap the reason why."),
            "choices": ("because about 2 of the 6 plays pay, 5 tokens each | because all "
                        "6 plays pay 5 tokens each | because one win of 5 tokens is all "
                        "to expect"),
            "answer": "because about 2 of the 6 plays pay, 5 tokens each",
            "board": '[[pie parts="6" shaded="2" caption="2 wins × 5 tokens = 10"]]',
        },
        "recap": [
            ("So, here it is again. To know what to expect from a game of chance, "
             "count the plays that pay, then times by the prize. Not every play pays, "
             "and one win is not the whole story — the expected amount is a center of "
             "gravity, never a promise.",
             '[[pie parts="6" shaded="2" caption="count the paying plays, then times"]]'),
            ("And that is chance, planned for.",
             '[[step eq="2 × 5 = 10 expected"]]'),
        ],
        "bank": [
            {"a": 2, "b": 5, "c": 2, "op": "expv"},
            {"a": 2, "b": 4, "c": 3, "op": "expv"},
            {"a": 2, "b": 6, "c": 4, "op": "expv"},
            {"a": 3, "b": 6, "c": 3, "op": "expv"},
            {"a": 2, "b": 5, "c": 5, "op": "expv"},
            {"a": 3, "b": 7, "c": 4, "op": "expv"},
            {"a": 3, "b": 5, "c": 5, "op": "expv"},
            {"a": 4, "b": 9, "c": 4, "op": "expv"},
            {"a": 3, "b": 8, "c": 6, "op": "expv"},
            {"a": 4, "b": 7, "c": 5, "op": "expv"},
        ],
    },
    {
        "id": "alg2-u9-the-sample-speaks",
        "course": "algebra2", "unit": 9,
        "topic": "Sampling",
        "op": "samp", "max_value": 40,
        "levels": ("abstract",),
        "symbols": ("sample", "about"),
        "advance_line": "Three in a row, and you can say why — you've got it! Scale the sample, and keep the word ABOUT.",
        "why": [
            ("Why does a sample speak? Because the last idea of Algebra Two is the "
             "boldest: ask a few, learn about everyone. A sample of 20 students found "
             "5 like pizza. The school holds 60 — nobody asked them all. Statistics "
             "says the sample SPEAKS for the school, about.",
             '[[goal text="The sample speaks"]]'),
        ],
        "picture": [
            ("Here is the sample beside the school as bars: 20 asked, 5 said yes, and "
             "a school of 60 standing three samples tall. If every slice of 20 behaves "
             "like the one we asked, the school holds about three times the 5.",
             '[[bars data="sample asked:20 | said yes:5 | the school:60" caption="20 asked, 5 said yes — the school is three samples wide"]]'),
        ],
        "teach": [
            ("That is the method. Scale it: 60 students is three samples of 20, side "
             "by side. If each slice of 20 behaves like the one we asked, each holds "
             "about 5 pizza-lovers: 5 times 3 — about 15 in the school. The similarity "
             "unit\'s factor thinking, aimed at people.",
             '[[bars data="one sample:5 | the school, 3 samples wide:15" caption="5 × 3 = about 15"]][[step eq="60 = 3 × 20 · 5 × 3 = about 15"]]'),
            ("Two traps. Answering 5 stops at the sample — the question asked about "
             "the school. And guessing half — 30 — ignores the sample entirely; we "
             "ASKED, and the sample said one in four, not one in two. Scale what the "
             "sample said, and keep the word about: samples estimate, never promise.",
             '[[step eq="5 × 3 = about 15 ✓"]][[step eq="5 ✗ the sample only · 30 ✗ the half-guess"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. A sample of 10 found 4 readers; "
                        "the school has 30 — three samples wide. About 12 readers.",
                        '[[bars data="one sample:4 | the school, 3 samples wide:12" caption="4 × 3 = about 12"]][[step eq="4 × 3 = about 12"]]'),
             "ask": {'a': 10, 'b': 2, 'c': 5, 'op': 'samp'}},
            {"worked": ("One more together. 15 asked, 6 said yes; the school is 45 — "
                        "three samples wide, so 6 times 3: about 18.",
                        '[[bars data="one sample:6 | the school, 3 samples wide:18" caption="6 × 3 = about 18"]][[step eq="6 × 3 = about 18"]]'),
             "ask": {'a': 30, 'b': 9, 'c': 4, 'op': 'samp'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A sample of 20 found "
                       "5 like pizza, the school has 60, and about 15 in the school like "
                       "pizza. Tap the reason why."),
            "choices": ("because the school is three samples wide, so three times 5 | "
                        "because the sample already said 5, and that is the answer | "
                        "because about half of any school likes pizza"),
            "answer": "because the school is three samples wide, so three times 5",
            "board": '[[bars data="one sample:5 | the school, 3 samples wide:15" caption="scale the sample"]]',
        },
        "recap": [
            ("So, here it is again. A sample speaks for the whole, about: find how "
             "many samples wide the whole is, and scale what the sample said by that. "
             "Never stop at the sample, never guess half — and keep the word about.",
             '[[bars data="sample asked:20 | said yes:5 | the school:60" caption="ask a few, learn about everyone — about"]]'),
            ("And that is Algebra Two\'s last idea: the sample speaks.",
             '[[step eq="5 × 3 = about 15"]]'),
        ],
        "bank": [
            {"a": 10, "b": 3, "c": 2, "op": "samp"},
            {"a": 12, "b": 4, "c": 2, "op": "samp"},
            {"a": 10, "b": 3, "c": 4, "op": "samp"},
            {"a": 20, "b": 7, "c": 2, "op": "samp"},
            {"a": 12, "b": 5, "c": 3, "op": "samp"},
            {"a": 10, "b": 4, "c": 4, "op": "samp"},
            {"a": 20, "b": 6, "c": 3, "op": "samp"},
            {"a": 16, "b": 5, "c": 4, "op": "samp"},
            {"a": 20, "b": 8, "c": 3, "op": "samp"},
            {"a": 25, "b": 7, "c": 4, "op": "samp"},
        ],
    },
]
LESSONS.extend(_ALGEBRA2_U9)

# ---- this course's slice of COURSE_ORDER: the teaching order (lessons/__init__.py joins the ten) ----
ORDER = [

    # ---- ALGEBRA II (build lh) -- Unit 1: Foundations & Systems ----
    "alg2-u1-how-far-from-zero", "alg2-u1-inside-the-distance",
    "alg2-u1-the-bananas-cancel", "alg2-u1-three-friends",
    # Unit 2: Quadratic Functions & Complex Numbers -- the quadratic tells its
    # secrets without being solved, and i arrives
    "alg2-u2-where-it-turns", "alg2-u2-both-answers-count",
    "alg2-u2-the-test-number", "alg2-u2-a-new-number",
    # Unit 3: Polynomial Functions -- what the degree promises
    "alg2-u3-degrees-add", "alg2-u3-the-wiggle-count",
    "alg2-u3-three-crossings", "alg2-u3-feed-the-cube",
    # Unit 4: Rational Expressions & Functions -- division becomes a function
    "alg2-u4-sharing-shrinks", "alg2-u4-which-x-was-fed",
    "alg2-u4-the-forbidden-x", "alg2-u4-the-survivor",
    # Unit 5: Radicals & Rational Exponents -- a root, never a halving
    "alg2-u5-under-one-roof", "alg2-u5-the-fraction-power",
    "alg2-u5-undo-the-root", "alg2-u5-between-the-squares",
    # Unit 6: Exponential & Logarithmic Functions -- decay, and the hidden
    # exponent with its adding law
    "alg2-u6-the-fading-half", "alg2-u6-the-hidden-exponent",
    "alg2-u6-logs-add", "alg2-u6-between-the-powers",
    # Unit 7: Sequences & Series -- a pattern is a rule you can ride
    "alg2-u7-ride-the-pattern", "alg2-u7-times-again",
    "alg2-u7-pair-the-ends", "alg2-u7-walk-the-rule",
    # Unit 8: Trigonometric Functions -- the circle of size one
    "alg2-u8-the-height", "alg2-u8-the-across",
    "alg2-u8-spin-once-more", "alg2-u8-the-stretched-wave",
    # Unit 9: Statistics & Probability -- ⭐ ALGEBRA II COMPLETE
    "alg2-u9-the-heavier-mean", "alg2-u9-three-slots",
    "alg2-u9-what-to-expect", "alg2-u9-the-sample-speaks",
]

# I did no harm and this file is not truncated.

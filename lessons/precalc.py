# =============================================================================
# lessons/precalc.py  --  TRIG / PRE-CALC: THE AUTHORED LESSONS  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-09-08  BUILD uq -- THE PROBLEM IS ALWAYS ON THE BOARD (Jim's flags 22:09/22:10,
#               21:56, 22:08). pc-u1-the-graph-slides: a concrete f (the square root), BOTH
#               curves drawn in the why, picture, trap, reason and recap beats, the method
#               in plain words ("take 3 off x FIRST, then do what f did"), the arrow read
#               aloud. pc-u1-machines-in-a-row: the trap beat keeps the two rules on the
#               board; the advance line names composition; the reason and recap beats say
#               "back to our first two machines" (a retiring phrase for rule 28).
#   2026-09-08  BUILD up -- A NEW MACHINE, STILL CALLED f. The two worked examples in
#               pc-u1-machines-in-a-row give f and g new rules; each now says so first
#               ("-- two new machines, still called f and g"), per Jim's rule-28 ruling.
#               Two lines; no numbers, boards or answers changed.
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
# PRE-CALC -- UNIT 1: FUNCTIONS & THEIR GRAPHS (build ll, 2026-08-22)
# =============================================================================
# ⭐ THE NINTH COURSE OPENS. Algebra I's machines grow up: composition in
# f(g(x)) notation (INSIDE FIRST -- the order flip is the trap), the graph that
# slides opposite its sign (vtx2's lesson generalized to every function), the
# domain as a doorway (and the taught CONTRAST: the root's edge is welcome,
# division's forbidden x was not), and a function built in pieces.
_PRECALC_U1 = [
    {
        "id": "pc-u1-machines-in-a-row",
        "course": "precalc", "unit": 1,
        "topic": "Composition",
        "op": "fcmp", "max_value": 40,
        "levels": ("abstract",),
        "symbols": ("composition", "inside"),
        "advance_line": "Three in a row, and you can say why — you've got it! In a composition, the inside function runs first.",
        "why": [
            ("Why machines in a row? Welcome to Pre-Calculus, where functions become "
             "the main characters. Algebra One fed numbers through two machines in a "
             "row; now the chaining gets a name — composition — and a notation: f of g "
             "of x. Read it from the inside out: g runs first, then f eats what g made.",
             '[[goal text="Machines in a row"]][[step eq="f(g(x)) — the inside runs first"]]'),
        ],
        "picture": [
            ("Here are the two machines in a row. The first is g: it times by 2, and 5 "
             "goes in. Whatever comes out of g goes straight into f, which adds 3. Two "
             "machines, one conveyor belt, and the belt runs from g to f.",
             '[[machine input="5" rule="2x" output="10" fname="g" caption="g runs first: g(5) = 10"]][[machine input="10" rule="x + 3" output="13" fname="f" caption="then f eats what g made: f(10) = 13"]]'),
        ],
        "teach": [
            ("That is the method. f of x equals x plus 3, g of x equals 2 times x, and "
             "feed 5 to f of g. Inside first: g of 5 is 10. Then the outer machine: f "
             "of 10 is 13. The parentheses are a map: whatever sits deepest goes first.",
             '[[machine input="5" rule="2x" output="10" fname="g" caption="g(5) = 10"]][[machine input="10" rule="x + 3" output="13" fname="f" caption="f(10) = 13"]][[step eq="g(5) = 10"]][[step eq="f(10) = 13"]]'),
            ("The trap is running f first: f of 5 is 8, then g gives 16 — a different "
             "number entirely, because these machines do not commute. Order is "
             "everything in a kitchen and in a composition: the INSIDE machine cooks "
             "first.",
             # (uq) Jim's flag 21:56: "without being able to see the original functions
             # unless I scrolled up" -- the two rules ride this beat's board too.
             '[[step eq="f(x) = x + 3 · g(x) = 2x"]][[step eq="f(g(5)) = 13 ✓"]][[step eq="g(f(5)) = 16 ✗ — the order flipped"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you — two new machines, still called f and g. f adds 4, g times by 3. f of g of "
                        "2: inside, g of 2 is 6; then f — 10.",
                        '[[machine input="2" rule="3x" output="6" fname="g" caption="g(2) = 6"]][[machine input="6" rule="x + 4" output="10" fname="f" caption="f(6) = 10"]][[step eq="g(2) = 6"]][[step eq="f(6) = 10"]]'),
             "ask": {'a': 2, 'b': 2, 'c': 4, 'op': 'fcmp'}},
            {"worked": ("One more together — two new machines, still called f and g. f adds 5, g doubles. f of g of 7: inside, g "
                        "of 7 is 14; then f — 19.",
                        '[[machine input="7" rule="2x" output="14" fname="g" caption="g(7) = 14"]][[machine input="14" rule="x + 5" output="19" fname="f" caption="f(14) = 19"]][[step eq="g(7) = 14"]][[step eq="f(14) = 19"]]'),
             "ask": {'a': 7, 'b': 3, 'c': 6, 'op': 'fcmp'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Back to our first two machines: f adds 3, g times by "
                       "2, and f of g of 5 is 13. Tap the reason why."),
            "choices": ("because g runs first, and f eats what g made | because f runs "
                        "first, and g eats what f made | because the two machines run "
                        "at the same time"),
            "answer": "because g runs first, and f eats what g made",
            "board": '[[machine input="5" rule="2x" output="10" fname="g" caption="g first"]][[machine input="10" rule="x + 3" output="13" fname="f" caption="then f"]]',
        },
        "recap": [
            ("So, here it is again, back to our first two machines. A composition is two machines on one belt, and the "
             "notation is a map: whatever sits deepest runs first. Run the inner "
             "machine, hand its answer to the outer one — never the other way round.",
             '[[machine input="5" rule="2x" output="10" fname="g" caption="inside first"]][[machine input="10" rule="x + 3" output="13" fname="f" caption="then the outer machine"]]'),
            ("And that is composition: machines in a row.",
             '[[step eq="f(g(5)) = 13"]]'),
        ],
        "bank": [
            {"a": 2, "b": 2, "c": 2, "op": "fcmp"},
            {"a": 3, "b": 2, "c": 2, "op": "fcmp"},
            {"a": 2, "b": 2, "c": 3, "op": "fcmp"},
            {"a": 4, "b": 2, "c": 3, "op": "fcmp"},
            {"a": 3, "b": 3, "c": 3, "op": "fcmp"},
            {"a": 2, "b": 3, "c": 4, "op": "fcmp"},
            {"a": 5, "b": 2, "c": 6, "op": "fcmp"},
            {"a": 4, "b": 3, "c": 5, "op": "fcmp"},
            {"a": 6, "b": 2, "c": 8, "op": "fcmp"},
            {"a": 5, "b": 3, "c": 7, "op": "fcmp"},
        ],
    },
    {
        "id": "pc-u1-the-graph-slides",
        "course": "precalc", "unit": 1,
        "topic": "Shifting graphs",
        "op": "fshf", "max_value": 20,
        "levels": ("abstract",),
        "symbols": ("slides", "opposite"),
        "advance_line": "Three in a row, and you can say why — you've got it! The minus inside slides the graph right.",
        # (uq, 2026-09-08) Jim's flags 22:09/22:10: "makes ZERO sense without a visual",
        # "none of this makes any sense". The why beat had a goal card and no curve; the
        # picture was two dots; the method said "to get the OLD answer at f of zero, x
        # take away 3 must BE zero". Now a concrete f -- the square root -- and BOTH
        # curves on the board in every beat, and the method in plain words.
        "why": [
            ("Why does the graph slide? Because one rule moves every graph ever drawn, "
             "and the board shows it. The lower curve is one you know: y equals the "
             "square root of x — call that rule f. The other curve is the SAME rule "
             "with one change inside the parentheses: y equals f of x take away 3. The "
             "whole curve slid 3 to the RIGHT. Not up, not left — right.",
             '[[graph func="sqrt(x) | sqrt(x-3)" names="y = f(x) | y = f(x − 3)" range="0..12" yrange="0..4" caption="the same curve, slid 3 to the right"]][[goal text="The graph slides"]]'),
        ],
        "picture": [
            ("Follow one point. On the old curve, x equals 4 gives 2 — the point (4, "
             "2). On the new curve the height 2 sits at x equals 7, because 7 take "
             "away 3 is 4, and the square root of 4 is 2. So (4, 2) slid to (7, 2) — "
             "the same height, 3 further right. Every point on the old curve moves "
             "exactly like this one.",
             '[[graph func="sqrt(x) | sqrt(x-3)" names="y = f(x) | y = f(x − 3)" points="(4,2),(7,2)" range="0..12" yrange="0..4" caption="(4, 2) slides right 3 to (7, 2)"]]'),
        ],
        "teach": [
            ("That is the method. The new rule says: take 3 off x FIRST, then do what f "
             "did. So the new curve at x equals 7 does what the old curve did at 4 — "
             "and the old curve at 4 was 2. The height stays; x moves. New x equals old "
             "x plus 3: 4 plus 3 is 7.",
             '[[step eq="new curve at x = 7: f(7 − 3) = f(4) = 2"]][[step eq="new x = old x + 3 = 4 + 3 = 7"]]'),
            ("The trap is reading the minus literally and sliding LEFT — landing at "
             "(1, 2). But the minus inside is a delay, not a direction: x has to grow "
             "by 3 before the rule sees what it saw before. On the board the arrow "
             "says where the point goes: (4, 2) becomes (7, 2), the check mark — not "
             "(1, 2). Inside the parentheses, the sign points opposite. Always.",
             '[[graph func="sqrt(x) | sqrt(x-3)" names="y = f(x) | y = f(x − 3)" points="(4,2),(7,2)" range="0..12" yrange="0..4" caption="right 3 ✓ — not left"]][[step eq="(4, 2) → (7, 2) ✓"]][[step eq="(1, 2) ✗ — the literal minus"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. y equals f of: x take away 2. The "
                        "point (5, 6) slides right 2 — new x is 7.",
                        '[[graph points="(5,6),(7,6)" range="0..10" yrange="0..8" caption="(5, 6) slides right 2 to (7, 6)"]][[step eq="(5, 6) → (7, 6)"]]'),
             "ask": {'a': 3, 'b': 5, 'c': 2, 'op': 'fshf'}},
            {"worked": ("One more together. f of: x take away 6, and the point (7, 3): it "
                        "slides right 6, so the new x is 7 plus 6 — 13.",
                        '[[graph points="(7,3),(13,3)" range="0..15" yrange="0..5" caption="(7, 3) slides right 6 to (13, 3)"]][[step eq="(7, 3) → (13, 3)"]]'),
             "ask": {'a': 7, 'b': 8, 'c': 4, 'op': 'fshf'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Under y equals f of x "
                       "take away 3, the point (4, 2) lands at (7, 2). Tap the reason "
                       "why."),
            "choices": ("because the minus inside is a delay, so the graph slides right | "
                        "because the minus inside means left, so the graph slides left | "
                        "because the minus inside lowers the graph by 3"),
            "answer": "because the minus inside is a delay, so the graph slides right",
            "board": '[[graph func="sqrt(x) | sqrt(x-3)" names="y = f(x) | y = f(x − 3)" points="(4,2),(7,2)" range="0..12" yrange="0..4" caption="right 3"]]',
        },
        "recap": [
            ("So, here it is again. Take a number away inside the parentheses and the "
             "whole graph slides right by that much — the minus is a delay, and inside "
             "the parentheses signs point opposite. Every point keeps its height and "
             "moves across.",
             '[[graph func="sqrt(x) | sqrt(x-3)" names="y = f(x) | y = f(x − 3)" points="(4,2),(7,2)" range="0..12" yrange="0..4" caption="the minus inside slides the graph right"]]'),
            ("And that is one rule for every graph ever drawn.",
             '[[step eq="f(x − 3): everything slides right 3"]]'),
        ],
        "bank": [
            {"a": 2, "b": 3, "c": 4, "op": "fshf"},
            {"a": 2, "b": 4, "c": 2, "op": "fshf"},
            {"a": 3, "b": 4, "c": 5, "op": "fshf"},
            {"a": 2, "b": 6, "c": 3, "op": "fshf"},
            {"a": 4, "b": 5, "c": 2, "op": "fshf"},
            {"a": 3, "b": 7, "c": 4, "op": "fshf"},
            {"a": 5, "b": 6, "c": 3, "op": "fshf"},
            {"a": 4, "b": 8, "c": 5, "op": "fshf"},
            {"a": 6, "b": 7, "c": 2, "op": "fshf"},
            {"a": 5, "b": 9, "c": 6, "op": "fshf"},
        ],
    },
    {
        "id": "pc-u1-the-doorway",
        "course": "precalc", "unit": 1,
        "topic": "Domain",
        "op": "fdom", "max_value": 14, "min_value": -14,
        "levels": ("abstract",),
        "symbols": ("domain", "allowed"),
        "advance_line": "Three in a row, and you can say why — you've got it! The doorway is where the inside hits zero — and it is welcome.",
        "why": [
            ("Why a doorway? Because not every x may enter every function. The set of "
             "allowed x\'s is the function\'s domain, and Pre-Calculus reads it "
             "straight off the formula. y equals the square root of: x take away 13 — "
             "roots refuse negatives, so the inside must stay at zero or above.",
             '[[goal text="The doorway"]][[step eq="√(x − 13): the inside must not go negative"]]'),
        ],
        "picture": [
            ("Here is the curve of the square root of x take away 13. Look where it "
             "begins: at x equals 13, right on the ground, and nothing at all to the "
             "left of it. That starting point is the doorway — the smallest x allowed "
             "in.",
             '[[graph func="sqrt(x-13)" points="(13,0)" range="10..22" yrange="0..4" caption="y = √(x − 13) — the curve starts at the doorway, x = 13"]]'),
        ],
        "teach": [
            ("That is the method. Solve the doorway: x take away 13 stays at zero or "
             "above exactly when x is 13 or more. So 13 is the smallest x allowed — the "
             "domain\'s front door. At the door itself the root gets zero, and the "
             "root of zero is zero: perfectly fine.",
             '[[graph func="sqrt(x-13)" points="(13,0)" range="10..22" yrange="0..4" caption="the door at 13 — the root of zero is zero, welcome"]][[step eq="x − 13 ≥ 0 → x ≥ 13"]][[step eq="√0 = 0 · the door is open"]]'),
            ("Remember division\'s forbidden x? The bottom\'s zero was BANNED. The "
             "root\'s edge is the opposite: zero under a root is WELCOME — the "
             "boundary belongs. And the flip trap still lurks: the door is at 13, never "
             "negative 13. Doors sit where the inside hits zero.",
             '[[step eq="door at 13, allowed ✓"]][[step eq="−13 ✗ the flip · division banned its zero; the root keeps it"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. y equals the square root of: x "
                        "take away 20. The inside hits zero at 20 — that is the doorway, "
                        "and it is allowed in.",
                        '[[graph func="sqrt(x-20)" points="(20,0)" range="17..29" yrange="0..4" caption="√(x − 20) — the door at 20"]][[step eq="√(x − 20) → door at 20"]]'),
             "ask": {'a': 11, 'b': 0, 'op': 'fdom'}},
            {"worked": ("One more together. The root of: x take away 16 — the doorway is "
                        "16.",
                        '[[graph func="sqrt(x-16)" points="(16,0)" range="13..25" yrange="0..4" caption="√(x − 16) — the door at 16"]][[step eq="√(x − 16) → door at 16"]]'),
             "ask": {'a': 14, 'b': 0, 'op': 'fdom'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. For y equals the "
                       "square root of x take away 13, the smallest x allowed in is 13. "
                       "Tap the reason why."),
            "choices": ("because at 13 the inside is zero, which a root allows | "
                        "because at 13 the inside is zero, and zero is banned | because "
                        "the minus means the door is at negative 13"),
            "answer": "because at 13 the inside is zero, which a root allows",
            "board": '[[graph func="sqrt(x-13)" points="(13,0)" range="10..22" yrange="0..4" caption="the door at 13, welcome"]]',
        },
        "recap": [
            ("So, here it is again. A root refuses negatives, so its domain starts "
             "where the inside hits zero — and that doorway is welcome, because the "
             "root of zero is zero. Division bans its zero; the root keeps it. And the "
             "door sits at the number itself, never its flip.",
             '[[graph func="sqrt(x-13)" points="(13,0)" range="10..22" yrange="0..4" caption="the doorway is where the inside hits zero"]]'),
            ("And that is a domain, read straight off the formula.",
             '[[step eq="x − 13 ≥ 0 → x ≥ 13"]]'),
        ],
        "bank": [
            {"a": 2, "b": 0, "op": "fdom"},
            {"a": 3, "b": 0, "op": "fdom"},
            {"a": 4, "b": 0, "op": "fdom"},
            {"a": 5, "b": 0, "op": "fdom"},
            {"a": 6, "b": 0, "op": "fdom"},
            {"a": 7, "b": 0, "op": "fdom"},
            {"a": 8, "b": 0, "op": "fdom"},
            {"a": 9, "b": 0, "op": "fdom"},
            {"a": 10, "b": 0, "op": "fdom"},
            {"a": 12, "b": 0, "op": "fdom"},
        ],
    },
    {
        "id": "pc-u1-a-function-in-pieces",
        "course": "precalc", "unit": 1,
        "topic": "Piecewise functions",
        "op": "fpie", "max_value": 30,
        "levels": ("abstract",),
        "symbols": ("piecewise", "rule"),
        "advance_line": "Three in a row, and you can say why — you've got it! Check where x lives, then run that rule only.",
        "why": [
            ("Why pieces? Because a function may be built from parts, each ruling its "
             "own stretch of x — a piecewise function. Say: y equals x plus 4 when x is "
             "below 5, and y equals 3 times x when x is 5 or more. One function, two "
             "rules, and a border at 5.",
             '[[goal text="A function in pieces"]][[step eq="x < 5 → x + 4 · x ≥ 5 → 3x"]]'),
        ],
        "picture": [
            ("Here is the number line with the border marked at 5. Everything to the "
             "left of the border belongs to the first rule, x plus 4; everything from 5 "
             "onward belongs to the second, 3 times x. Before you compute, find which "
             "side x lives on.",
             '[[numberline min="0" max="10" points="5" caption="the border at 5 — below it, x + 4; from 5 on, 3x"]]'),
        ],
        "teach": [
            ("That is the method. Feeding it is a two-step: first find WHERE x lives, "
             "then run that rule and no other. Feed 2: below 5, so 2 plus 4 — 6. Feed "
             "6: it is 5 or more, so 3 times 6 — 18. Same function, different "
             "neighborhoods.",
             '[[numberline min="0" max="10" points="2,5,6" caption="2 is below the border; 6 is past it"]][[step eq="2 < 5 → 2 + 4 = 6"]][[step eq="6 ≥ 5 → 3 × 6 = 18"]]'),
            ("The trap is running the wrong rule — feeding 6 into x plus 4 and getting "
             "10, a number the function never says at 6. The border matters too: "
             "exactly 5 belongs to the 5-or-more side; read the border\'s owner from "
             "the words. Check the neighborhood, then compute.",
             '[[step eq="6 → 18 ✓"]][[step eq="6 → 10 ✗ — the wrong rule ran"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Rules: x plus 6 below 5; 2 times "
                        "x at 5 or more. Feed 3: below 5 — 3 plus 6 is 9.",
                        '[[numberline min="0" max="10" points="3,5" caption="3 is below 5 — the first rule: 3 + 6 = 9"]][[step eq="3 < 5 → 3 + 6 = 9"]]'),
             "ask": {'a': 4, 'b': 2, 'c': 2, 'op': 'fpie'}},
            {"worked": ("One more together. Same rules, feed 8: 5 or more — 2 times 8 is "
                        "16.",
                        '[[numberline min="0" max="10" points="5,8" caption="8 is past 5 — the second rule: 2 × 8 = 16"]][[step eq="8 ≥ 5 → 2 × 8 = 16"]]'),
             "ask": {'a': 4, 'b': 4, 'c': 6, 'op': 'fpie'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. The rules are x plus 4 "
                       "below 5 and 3 times x from 5 on, and at x equals 6 the answer is "
                       "18. Tap the reason why."),
            "choices": ("because 6 is past the border, so the second rule runs | because "
                        "6 is below the border, so the first rule runs | because both "
                        "rules run and their answers are added"),
            "answer": "because 6 is past the border, so the second rule runs",
            "board": '[[numberline min="0" max="10" points="5,6" caption="6 is past 5 — 3 × 6 = 18"]]',
        },
        "recap": [
            ("So, here it is again. A function in pieces has a border, and each rule "
             "owns one side of it. Find which side x lives on, then run that rule and "
             "no other — and read from the words which side owns the border itself.",
             '[[numberline min="0" max="10" points="5" caption="check the neighborhood, then compute"]]'),
            ("And that is one function with two rules.",
             '[[step eq="x < 5 → x + 4 · x ≥ 5 → 3x"]]'),
        ],
        "bank": [
            {"a": 3, "b": 2, "c": 2, "op": "fpie"},
            {"a": 5, "b": 3, "c": 3, "op": "fpie"},
            {"a": 6, "b": 2, "c": 4, "op": "fpie"},
            {"a": 2, "b": 2, "c": 5, "op": "fpie"},
            {"a": 7, "b": 3, "c": 4, "op": "fpie"},
            {"a": 3, "b": 2, "c": 6, "op": "fpie"},
            {"a": 4, "b": 2, "c": 7, "op": "fpie"},
            {"a": 2, "b": 3, "c": 5, "op": "fpie"},
            {"a": 2, "b": 2, "c": 8, "op": "fpie"},
            {"a": 3, "b": 3, "c": 6, "op": "fpie"},
        ],
    },
]
LESSONS.extend(_PRECALC_U1)

# =============================================================================
# PRE-CALC UNIT 2 -- Polynomial & Rational Functions (build lm)
# The thread: a polynomial tells you everything you want to know WITHOUT long
# division -- parity reads (-1)^n at a glance, the plug-in shortcut finds the
# leftover, the roots write the puzzle's own numbers, and a factored bottom
# hands you its forbidden x's by count.
# =============================================================================
_PRECALC_U2 = [
    {
        "id": "pc-u2-the-minus-parade",
        "course": "precalc", "unit": 2,
        "topic": "Even and odd powers",
        "op": "negp", "max_value": 13, "min_value": -1,
        "levels": ("abstract",),
        "symbols": ("power", "even"),
        "advance_line": "Three in a row, and you can say why — you've got it! Even wipes the minus; odd leaves one.",
        "why": [
            ("Why a parade? Unit Two turns to polynomials — and starts with the "
             "smallest one that bites: negative 1, raised to a power. Each minus sign "
             "cancels the one before it, so everything hangs on whether the power is "
             "even or odd. A parade of minus signs, counted in pairs.",
             '[[goal text="The minus parade"]][[step eq="(−1)^n — even n → 1 · odd n → −1"]]'),
        ],
        "picture": [
            ("Here are 14 minus signs lined up in two rows — 7 pairs, and nobody left "
             "standing alone. Every pair cancels to a plus. And here are 15: the same "
             "7 pairs, with one lone minus sign left over at the end of the parade.",
             '[[array rows="2" cols="7" caption="14 minus signs — 7 pairs, all cancel"]][[array rows="2" cols="7" extra="1" caption="15 minus signs — 7 pairs and one left over"]]'),
        ],
        "teach": [
            ("That is the method. Raise negative 1 to the power 14: the minus signs "
             "pair up — 7 pairs, none left out — so every minus cancels and the answer "
             "is 1. An even power wipes the minus away completely.",
             '[[array rows="2" cols="7" caption="14 minus signs — 7 pairs cancel: 1"]][[step eq="(−1)^14 = 1 — 7 pairs, all cancel"]]'),
            ("Now the power 15: the pairs cancel, and one lone minus sign survives at "
             "the end of the parade. The answer is negative 1. Odd leaves a leftover; "
             "even leaves none — that single fact powers half of Pre-Calculus.",
             '[[array rows="2" cols="7" extra="1" caption="15 minus signs — one survives: −1"]][[step eq="(−1)^15 = −1 — one minus survives"]][[step eq="even → 1 · odd → −1"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Negative 1 to the power 20: even, "
                        "so the pairs all cancel — 1.",
                        '[[array rows="2" cols="10" caption="20 minus signs — 10 pairs, all cancel: 1"]][[step eq="(−1)^20 = 1"]]'),
             "ask": {'a': 12, 'b': 0, 'op': 'negp'}},
            {"worked": ("One more together. The power 25 is odd — one minus survives: "
                        "negative 1.",
                        '[[array rows="2" cols="12" extra="1" caption="25 minus signs — 12 pairs and one left over: −1"]][[step eq="(−1)^25 = −1"]]'),
             "ask": {'a': 13, 'b': 0, 'op': 'negp'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Negative 1 to the "
                       "power 15 is negative 1. Tap the reason why."),
            "choices": ("because 15 is odd, so one minus sign is left over | because 15 is "
                        "odd, so every minus sign cancels | because the minus signs all "
                        "vanish to zero"),
            "answer": "because 15 is odd, so one minus sign is left over",
            "board": '[[array rows="2" cols="7" extra="1" caption="7 pairs and one left over"]]',
        },
        "recap": [
            ("So, here it is again. Negative 1 to a power is a parade of minus signs "
             "counted in pairs. An even power pairs them all, and the answer is 1; an "
             "odd power leaves one minus sign standing, and the answer is negative 1.",
             '[[array rows="2" cols="7" extra="1" caption="even → 1 · odd → −1"]]'),
            ("And that is the smallest polynomial that bites.",
             '[[step eq="(−1)^14 = 1 · (−1)^15 = −1"]]'),
        ],
        "bank": [
            {"a": 2, "b": 0, "op": "negp"},
            {"a": 3, "b": 0, "op": "negp"},
            {"a": 4, "b": 0, "op": "negp"},
            {"a": 5, "b": 0, "op": "negp"},
            {"a": 6, "b": 0, "op": "negp"},
            {"a": 7, "b": 0, "op": "negp"},
            {"a": 8, "b": 0, "op": "negp"},
            {"a": 9, "b": 0, "op": "negp"},
            {"a": 10, "b": 0, "op": "negp"},
            {"a": 11, "b": 0, "op": "negp"},
        ],
    },
    {
        "id": "pc-u2-no-long-division",
        "course": "precalc", "unit": 2,
        "topic": "The remainder theorem",
        "op": "remt", "max_value": 40,
        "levels": ("abstract",),
        "symbols": ("left over", "divided by"),
        "advance_line": "Three in a row, and you can say why — you've got it! Plug it in — no dividing needed.",
        "why": [
            ("Why no long division? Take x squared plus 5 x plus 1, divided by x take "
             "away 2. Long division would grind through it and end with a number left "
             "over — the way 17 divided by 5 leaves 2. Pre-Calculus owns a shortcut "
             "that finds that number with no dividing at all.",
             '[[goal text="No long division"]][[step eq="(x² + 5x + 1) ÷ (x − 2) → left over = ?"]]'),
        ],
        "picture": [
            ("Here is the top of the division as a machine, with the 2 from x take "
             "away 2 fed straight into it. Whatever the machine puts out IS the number "
             "long division would have left over — one plug, no dividing.",
             '[[machine input="2" rule="x² + 5x + 1" output="15" caption="plug in the 2 — out comes the leftover, 15"]]'),
        ],
        "teach": [
            ("That is the method — a famous theorem, named on the board: plug the 2 "
             "straight into the top. 2 squared equals 4, plus 5 times 2 equals 10, plus "
             "1 — in all, 15. That IS the number long division would have left over. "
             "One plug beats twenty steps of dividing.",
             '[[machine input="2" rule="x² + 5x + 1" output="15" caption="the Remainder Theorem: plug in 2"]][[step eq="2² + 5·2 + 1 = 15"]][[step eq="left over = 15"]]'),
            ("Why does it work? Because x take away 2 turns into ZERO exactly at x "
             "equals 2 — at that one x the whole divided-out part vanishes, and only "
             "the leftover speaks. Careful: plug in the 2 from x take away 2, never "
             "some other number.",
             '[[step eq="at x = 2 the divisor is 0 — only the leftover speaks"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. x squared plus 1 x plus 2, divided "
                        "by x take away 5: plug in 5 — 25 plus 5 plus 2 equals 32.",
                        '[[machine input="5" rule="x² + 1x + 2" output="32" caption="5² + 1·5 + 2 = 32"]][[step eq="5² + 1·5 + 2 = 32"]]'),
             "ask": {'a': 2, 'b': 2, 'c': 5, 'op': 'remt'}},
            {"worked": ("One more together. x squared plus 4 x plus 3, divided by x take "
                        "away 4: 16 plus 16 plus 3 — 35.",
                        '[[machine input="4" rule="x² + 4x + 3" output="35" caption="4² + 4·4 + 3 = 35"]][[step eq="4² + 4·4 + 3 = 35"]]'),
             "ask": {'a': 5, 'b': 2, 'c': 4, 'op': 'remt'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. x squared plus 5 x "
                       "plus 1, divided by x take away 2, leaves 15 over. Tap the reason "
                       "why."),
            "choices": ("because at x equals 2 only the leftover speaks | because the "
                        "leftover is always the end number, 1 | because the leftover is "
                        "the 2 from x take away 2"),
            "answer": "because at x equals 2 only the leftover speaks",
            "board": '[[machine input="2" rule="x² + 5x + 1" output="15" caption="one plug, no dividing"]]',
        },
        "recap": [
            ("So, here it is again. To find what dividing by x take away a number "
             "leaves over, plug that number into the top — at that x the divided-out "
             "part vanishes and only the leftover speaks. No long division.",
             '[[machine input="2" rule="x² + 5x + 1" output="15" caption="the Remainder Theorem"]]'),
            ("And that is one plug beating twenty steps.",
             '[[step eq="2² + 5·2 + 1 = 15"]]'),
        ],
        "bank": [
            {"a": 2, "b": 1, "c": 1, "op": "remt"},
            {"a": 2, "b": 2, "c": 3, "op": "remt"},
            {"a": 2, "b": 3, "c": 3, "op": "remt"},
            {"a": 3, "b": 1, "c": 4, "op": "remt"},
            {"a": 3, "b": 2, "c": 4, "op": "remt"},
            {"a": 3, "b": 3, "c": 2, "op": "remt"},
            {"a": 4, "b": 1, "c": 5, "op": "remt"},
            {"a": 3, "b": 4, "c": 6, "op": "remt"},
            {"a": 4, "b": 2, "c": 6, "op": "remt"},
            {"a": 4, "b": 3, "c": 5, "op": "remt"},
        ],
    },
    {
        "id": "pc-u2-the-roots-secret",
        "course": "precalc", "unit": 2,
        "topic": "Vieta's product",
        "op": "vprd", "max_value": 40,
        "levels": ("abstract",),
        "symbols": ("roots", "product"),
        "advance_line": "Three in a row, and you can say why — you've got it! The end number is the product of the roots.",
        "why": [
            ("Why a secret? Back in Algebra Two you learned the two roots of a puzzle "
             "secretly ADD to the middle number — and we promised the product would be "
             "famous later. Later is now. The roots of an x-squared puzzle also "
             "multiply to something: the plain END number.",
             '[[goal text="The roots\' secret"]][[step eq="roots add → middle · roots times → end"]]'),
        ],
        "picture": [
            ("Here are the four rooms of x take away 2, times x take away 6. The big "
             "room is x squared; the two middle rooms hold the x\'s; and the corner "
             "room, negative 2 times negative 6, holds the plain number, 12 — the "
             "product of the roots.",
             '[[areamodel rows="x,-2" cols="x,-6" caption="(x − 2) by (x − 6) — the corner room is 2 × 6 = 12"]]'),
        ],
        "teach": [
            ("That is the method. Later is now — watch it happen. Roots 2 and 6: the puzzle is x take "
             "away 2, times x take away 6. Multiply it out: x squared, take away 8 x, "
             "plus 12. The middle 8 is 2 plus 6. The end 12 is 2 times 6 — the product "
             "of the roots.",
             '[[areamodel rows="x,-2" cols="x,-6" caption="x² − 8x + 12"]][[step eq="(x − 2)(x − 6) = x² − 8x + 12"]][[step eq="2 + 6 = 8 · 2 × 6 = 12"]]'),
            ("So a puzzle hands over its numbers without any solving: the end number "
             "is the roots\' product, the middle is their sum. The trap runs backwards "
             "too — asked for the end number, do not ADD the roots. Sum sits in the "
             "middle; product sits at the end.",
             '[[step eq="end = product ✓ · sum ✗ — that is the middle"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Roots 4 and 7: the end number is "
                        "4 times 7 — 28. The middle would be 11.",
                        '[[areamodel rows="x,-4" cols="x,-7" caption="(x − 4)(x − 7) — end 28, middle 11"]][[step eq="(x − 4)(x − 7) → end 28 · middle 11"]]'),
             "ask": {'a': 2, 'b': 8, 'op': 'vprd'}},
            {"worked": ("One more together. Roots 2 and 9: the end number is 2 times 9 — "
                        "18.",
                        '[[areamodel rows="x,-2" cols="x,-9" caption="(x − 2)(x − 9) — end 18"]][[step eq="(x − 2)(x − 9) → end 18"]]'),
             "ask": {'a': 5, 'b': 7, 'op': 'vprd'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A puzzle with roots 2 "
                       "and 6 ends in the number 12. Tap the reason why."),
            "choices": ("because the end number is the product of the roots | because the "
                        "end number is the sum of the roots | because the end number is "
                        "the bigger root, doubled"),
            "answer": "because the end number is the product of the roots",
            "board": '[[areamodel rows="x,-2" cols="x,-6" caption="the corner room: 2 × 6 = 12"]]',
        },
        "recap": [
            ("So, here it is again. A puzzle\'s two roots write the whole puzzle: "
             "their sum is the middle number, worn with a minus, and their product is "
             "the plain end number — the corner room of the four. Sum in the middle, "
             "product at the end.",
             '[[areamodel rows="x,-2" cols="x,-6" caption="sum in the middle, product at the end"]]'),
            ("And that is the promise Algebra Two made, paid.",
             '[[step eq="2 + 6 = 8 · 2 × 6 = 12"]]'),
        ],
        "bank": [
            {"a": 2, "b": 3, "op": "vprd"},
            {"a": 2, "b": 4, "op": "vprd"},
            {"a": 2, "b": 5, "op": "vprd"},
            {"a": 3, "b": 4, "op": "vprd"},
            {"a": 2, "b": 7, "op": "vprd"},
            {"a": 3, "b": 5, "op": "vprd"},
            {"a": 3, "b": 6, "op": "vprd"},
            {"a": 4, "b": 5, "op": "vprd"},
            {"a": 4, "b": 6, "op": "vprd"},
            {"a": 5, "b": 6, "op": "vprd"},
        ],
    },
    {
        "id": "pc-u2-twice-forbidden",
        "course": "precalc", "unit": 2,
        "topic": "Forbidden x's, counted",
        "op": "vasy", "max_value": 9, "min_value": 0,
        "levels": ("abstract",),
        "symbols": ("forbidden", "factors"),
        "advance_line": "Three in a row, and you can say why — you've got it! Count the different zeros, not the factors.",
        "why": [
            ("Why twice? Algebra Two found division\'s forbidden x — the one x that "
             "zeroes a bottom. Pre-Calculus bottoms come factored: 1 divided by, x take "
             "away 3, times x take away 7. TWO factors now — so how many x\'s are "
             "forbidden? Count the zeros, and count carefully.",
             '[[goal text="Twice forbidden"]][[step eq="y = 1 ÷ (x − 3)(x − 7)"]]'),
        ],
        "picture": [
            ("Here is the curve of 1 divided by x take away 3, times x take away 7. "
             "Watch it fly off the picture twice — once at x equals 3 and once at x "
             "equals 7. Two places the curve can never touch: two forbidden x\'s.",
             '[[graph func="1/((x-3)*(x-7))" range="1..9" yrange="-6..6" caption="y = 1 ÷ (x − 3)(x − 7) — flies off at 3 and at 7"]]'),
        ],
        "teach": [
            ("That is the method. Each factor dies at its own x: x equals 3 zeroes the "
             "first, x equals 7 zeroes the second, and either one alone flattens the "
             "whole bottom. Two different zeros — two forbidden x\'s. The count is 2.",
             '[[graph func="1/((x-3)*(x-7))" range="1..9" yrange="-6..6" caption="two zeros, two forbidden x\'s — count 2"]][[step eq="x = 3 ✗ · x = 7 ✗ — two forbidden"]]'),
            ("But factors can repeat: 1 divided by, x take away 8, times x take away "
             "8. Two factors, yet both die at the SAME x. Only x equals 8 is forbidden "
             "— the count is 1. Count the different zeros, never the factors.",
             '[[graph func="1/((x-8)*(x-8))" range="5..11" yrange="-6..6" caption="(x − 8)(x − 8) — flies off once, at 8: count 1"]][[step eq="(x − 8)(x − 8): both die at 8 → count 1"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 1 divided by, x take away 4, "
                        "times x take away 9: zeros at 4 and 9 — two forbidden x\'s.",
                        '[[graph func="1/((x-4)*(x-9))" range="2..11" yrange="-6..6" caption="flies off at 4 and at 9 — count 2"]][[step eq="(x − 4)(x − 9) → count 2"]]'),
             "ask": {'a': 2, 'b': 4, 'op': 'vasy'}},
            {"worked": ("One more together. x take away 9, times x take away 9: both die "
                        "at 9 — the count is 1.",
                        '[[graph func="1/((x-9)*(x-9))" range="6..12" yrange="-6..6" caption="flies off once, at 9 — count 1"]][[step eq="(x − 9)(x − 9) → count 1"]]'),
             "ask": {'a': 7, 'b': 7, 'op': 'vasy'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. For 1 divided by x "
                       "take away 8, times x take away 8, only one x is forbidden. Tap "
                       "the reason why."),
            "choices": ("because both factors die at the same x, 8 | because two factors "
                        "always mean two forbidden x\'s | because a repeated factor "
                        "cancels itself out"),
            "answer": "because both factors die at the same x, 8",
            "board": '[[graph func="1/((x-8)*(x-8))" range="5..11" yrange="-6..6" caption="one zero, counted once"]]',
        },
        "recap": [
            ("So, here it is again. A factored bottom forbids every x that zeroes a "
             "factor — but count the DIFFERENT zeros, never the factors. Two factors "
             "with two zeros forbid two x\'s; two factors with the same zero forbid "
             "one.",
             '[[graph func="1/((x-3)*(x-7))" range="1..9" yrange="-6..6" caption="count the different zeros"]]'),
            ("And that is the forbidden x, twice over.",
             '[[step eq="x = 3 ✗ · x = 7 ✗ — count 2"]]'),
        ],
        "bank": [
            {"a": 2, "b": 2, "op": "vasy"},
            {"a": 2, "b": 3, "op": "vasy"},
            {"a": 3, "b": 3, "op": "vasy"},
            {"a": 2, "b": 5, "op": "vasy"},
            {"a": 4, "b": 4, "op": "vasy"},
            {"a": 3, "b": 6, "op": "vasy"},
            {"a": 5, "b": 5, "op": "vasy"},
            {"a": 4, "b": 7, "op": "vasy"},
            {"a": 6, "b": 6, "op": "vasy"},
            {"a": 5, "b": 8, "op": "vasy"},
        ],
    },
]
LESSONS.extend(_PRECALC_U2)

# =============================================================================
# PRE-CALC UNIT 3 -- Exponential & Logarithmic Functions (build lm)
# The thread: logs and exponentials UN-DO each other, and the world runs on it
# -- the power rule brings exponents down front, solving a log means stacking
# the base back up, a tank's halvings are a logarithm in work clothes, and
# money that doubles is the exponential doing what steady adding never can.
# hcnt is hlfl read backwards -- the same halving tank, asked the other way.
# =============================================================================
_PRECALC_U3 = [
    {
        "id": "pc-u3-the-power-comes-down",
        "course": "precalc", "unit": 3,
        "topic": "Log of a power",
        "op": "logp", "max_value": 512,
        "levels": ("abstract",),
        "symbols": ("logarithm", "power"),
        "advance_line": "Three in a row, and you can say why — you've got it! The exponent comes down front.",
        "why": [
            ("Why does the power come down? Unit Three: the logarithm and the "
             "exponential, each un-doing the other. Algebra Two counted layers one at "
             "a time; Pre-Calculus learns the power rule — the logarithm of a power "
             "lets the exponent step DOWN in front and turn into a times.",
             '[[goal text="The power comes down"]][[step eq="log(a^n) = n × log a"]]'),
        ],
        "picture": [
            ("Here are two bars, base 2 throughout. The first is the log of 1024 — ten "
             "layers. The second is the log of 1024 squared — and it is exactly twice "
             "as tall, twenty. Squaring the number doubled its log; the exponent "
             "became a times.",
             '[[bars data="log 1024:10 | log 1024²:20" caption="the exponent 2 comes down front: 2 × 10 = 20"]]'),
        ],
        "teach": [
            ("That is the method. In this lesson every log is base 2. Try the "
             "logarithm of 1024 to the power 2. Log base 2 of 1024 is 10 — ten layers. "
             "The power rule: the exponent 2 comes down front — 2 times 10 equals 20. "
             "Done, and no giant number was ever built.",
             '[[bars data="log 1024:10 | log 1024²:20" caption="log 1024² = 2 × 10 = 20"]][[step eq="log 1024^2 = 2 × 10 = 20"]]'),
            ("Feel the size of the shortcut: 1024 to the power 2 is past a MILLION, and "
             "you never touched it. The trap: the exponent TIMES the log, never the log "
             "raised to the exponent — that would say 100, wildly wrong.",
             '[[step eq="2 × 10 = 20 ✓ · 10^2 = 100 ✗"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Log base 2 of 256 to the power 3: "
                        "log of 256 is 8, and 3 times 8 equals 24.",
                        '[[bars data="log 256:8 | log 256³:24" caption="3 × 8 = 24"]][[step eq="log 256^3 = 3 × 8 = 24"]]'),
             "ask": {'a': 512, 'b': 2, 'op': 'logp'}},
            {"worked": ("One more together. Log base 2 of 32 to the power 4: log of 32 is "
                        "5, and 4 times 5 equals 20.",
                        '[[bars data="log 32:5 | log 32⁴:20" caption="4 × 5 = 20"]][[step eq="log 32^4 = 4 × 5 = 20"]]'),
             "ask": {'a': 128, 'b': 3, 'op': 'logp'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Log base 2 of 1024 "
                       "squared is 20. Tap the reason why."),
            "choices": ("because the exponent comes down front and times the log | "
                        "because the log is raised to the exponent | because squaring a "
                        "number leaves its log unchanged"),
            "answer": "because the exponent comes down front and times the log",
            "board": '[[bars data="log 1024:10 | log 1024²:20" caption="2 × 10 = 20"]]',
        },
        "recap": [
            ("So, here it is again. The logarithm of a power lets the exponent step "
             "down in front as a times: the log of a number to the n is n times the "
             "log of the number. Never raise the log to the power — the exponent "
             "times it.",
             '[[bars data="log 1024:10 | log 1024²:20" caption="the power comes down"]]'),
            ("And that is a million-sized number, never built.",
             '[[step eq="log(a^n) = n × log a"]]'),
        ],
        "bank": [
            {"a": 8, "b": 2, "op": "logp"},
            {"a": 16, "b": 2, "op": "logp"},
            {"a": 8, "b": 3, "op": "logp"},
            {"a": 32, "b": 2, "op": "logp"},
            {"a": 64, "b": 2, "op": "logp"},
            {"a": 16, "b": 3, "op": "logp"},
            {"a": 128, "b": 2, "op": "logp"},
            {"a": 32, "b": 3, "op": "logp"},
            {"a": 256, "b": 2, "op": "logp"},
            {"a": 64, "b": 3, "op": "logp"},
        ],
    },
    {
        "id": "pc-u3-rebuild-the-number",
        "course": "precalc", "unit": 3,
        "topic": "Solving log equations",
        "op": "lsol", "max_value": 1000,
        "levels": ("abstract",),
        "symbols": ("logarithm", "rebuild"),
        "advance_line": "Three in a row, and you can say why — you've got it! Stack the base and rebuild.",
        "why": [
            ("Why rebuild? Because a logarithm can sit inside an equation: the "
             "logarithm, base 2, of some mystery number equals 10. Solving it means "
             "running the log BACKWARDS — the log counted the layers, so you rebuild "
             "the number by stacking the layers again.",
             '[[goal text="Rebuild the number"]]'),
        ],
        "picture": [
            ("Here is the log machine, run backwards: the rule is log base 2 of x, the "
             "output came out as 10, and the input door is blank. Ten layers were "
             "counted — the question is which number has ten layers of 2.",
             '[[machine input="?" rule="log base 2 of x" output="10" caption="the log counted 10 layers — which number went in?"]]'),
        ],
        "teach": [
            ("That is the method. Ten layers of 2: 2 multiplied out 10 times equals "
             "1024. The mystery number is 1024 — the exponential un-did the logarithm. "
             "Check it forward: log base 2 of 1024 is indeed 10. Rebuilt, and "
             "confirmed.",
             '[[bars data="2¹:2 | 2²:4 | 2³:8 | 2⁴:16 | 2⁵:32 | 2⁶:64 | 2⁷:128 | 2⁸:256 | 2⁹:512 | 2¹⁰:1024" caption="10 layers of 2 — the mystery number is 1024"]][[step eq="? = 2 stacked 10 times = 1024"]][[step eq="log 1024 = 10 ✓"]]'),
            ("The base matters: log base 10 of the mystery equals 4 rebuilds to 10 "
             "thousand — never 40. The trap is timesing base and answer when the base "
             "must STACK: layers power upward; a single times cannot reach them.",
             '[[step eq="base 10, log 4 → 10000 ✓ · 10 × 4 = 40 ✗"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Log base 3 of the mystery equals "
                        "6: stack six 3s — 729.",
                        '[[bars data="3¹:3 | 3²:9 | 3³:27 | 3⁴:81 | 3⁵:243 | 3⁶:729" caption="6 layers of 3 — 729"]][[step eq="3 stacked 6 times = 729"]]'),
             "ask": {'a': 2, 'b': 8, 'op': 'lsol'}},
            {"worked": ("One more together. Log base 2 of the mystery equals 9: stack nine "
                        "2s — 512.",
                        '[[machine input="512" rule="log base 2 of x" output="9" caption="9 layers of 2 — 512"]][[step eq="2 stacked 9 times = 512"]]'),
             "ask": {'a': 10, 'b': 3, 'op': 'lsol'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. The log base 2 of a "
                       "mystery number is 10, and the number is 1024. Tap the reason "
                       "why."),
            "choices": ("because ten layers of 2 stack up to 1024 | because 2 times 10 "
                        "rebuilds the number | because 2 plus 10 rebuilds the number"),
            "answer": "because ten layers of 2 stack up to 1024",
            "board": '[[machine input="1024" rule="log base 2 of x" output="10" caption="log 1024 = 10 ✓"]]',
        },
        "recap": [
            ("So, here it is again. A log inside an equation is solved by running it "
             "backwards: the log counted the layers, so stack the base that many times "
             "and the number is rebuilt. Layers power upward — a single times cannot "
             "reach them.",
             '[[machine input="1024" rule="log base 2 of x" output="10" caption="stack the base and rebuild"]]'),
            ("And that is the exponential, un-doing the logarithm.",
             '[[step eq="2 stacked 10 times = 1024"]]'),
        ],
        "bank": [
            {"a": 2, "b": 3, "op": "lsol"},
            {"a": 3, "b": 2, "op": "lsol"},
            {"a": 2, "b": 4, "op": "lsol"},
            {"a": 3, "b": 3, "op": "lsol"},
            {"a": 2, "b": 5, "op": "lsol"},
            {"a": 2, "b": 6, "op": "lsol"},
            {"a": 3, "b": 4, "op": "lsol"},
            {"a": 10, "b": 2, "op": "lsol"},
            {"a": 2, "b": 7, "op": "lsol"},
            {"a": 3, "b": 5, "op": "lsol"},
        ],
    },
    {
        "id": "pc-u3-count-the-halvings",
        "course": "precalc", "unit": 3,
        "topic": "How many halvings",
        "op": "hcnt", "max_value": 96,
        "levels": ("abstract",),
        "symbols": ("halvings", "days"),
        "advance_line": "Three in a row, and you can say why — you've got it! Count the halvings, not the ratio.",
        "why": [
            ("Why count the halvings? Algebra Two halved a sample forward: start, "
             "halve for a stretch of days, find the end. Pre-Calculus asks it "
             "BACKWARDS: here is the start, here is the end — how many halvings "
             "happened? That backwards question is exactly a logarithm wearing work "
             "clothes.",
             '[[goal text="Count the halvings"]]'),
        ],
        "picture": [
            ("Here is a tank as bars, dropping to half each day: 56, then 28, then 14, "
             "then 7. Count the drops between the first bar and the last — three. That "
             "count of drops is the number of days.",
             '[[bars data="day 0:56 | day 1:28 | day 2:14 | day 3:7" caption="56 → 28 → 14 → 7 — three halvings"]]'),
        ],
        "teach": [
            ("That is the method. A tank starts at 56 liters and drops to half each "
             "day; now it holds 7. Halve and count: 56, then 28, then 14, then 7. Three "
             "halvings — three days went by. You rode the halving down and counted the "
             "steps.",
             '[[bars data="day 0:56 | day 1:28 | day 2:14 | day 3:7" caption="three halvings — three days"]][[step eq="56 → 28 → 14 → 7 · 3 days"]]'),
            ("The trap: 56 divided by 7 equals 8, and 8 is NOT the answer — 8 says how "
             "many times bigger, never how many halvings. Each halving divides by 2, "
             "so ask instead: how many 2s multiply up to 8? Three. The ratio hides the "
             "count.",
             '[[step eq="56 ÷ 7 = 8 ✗ ratio"]][[step eq="8 = 2 × 2 × 2"]][[step eq="3 days ✓"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. From 36 down to 9: 36, then 18, "
                        "then 9 — two halvings, two days.",
                        '[[bars data="day 0:36 | day 1:18 | day 2:9" caption="36 → 18 → 9 — two halvings"]][[step eq="36 → 18 → 9 · 2 days"]]'),
             "ask": {'a': 28, 'b': 7, 'op': 'hcnt'}},
            {"worked": ("One more together. From 24 down to 3: 24, then 12, then 6, then 3 "
                        "— three days.",
                        '[[bars data="day 0:24 | day 1:12 | day 2:6 | day 3:3" caption="24 → 12 → 6 → 3 — three halvings"]][[step eq="24 → 12 → 6 → 3 · 3 days"]]'),
             "ask": {'a': 96, 'b': 3, 'op': 'hcnt'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A tank drops from 56 "
                       "liters to 7, halving each day, and 3 days went by. Tap the "
                       "reason why."),
            "choices": ("because three halvings take 56 down to 7 | because 56 divided by "
                        "7 is the number of days | because the tank lost 7 liters a day"),
            "answer": "because three halvings take 56 down to 7",
            "board": '[[bars data="day 0:56 | day 1:28 | day 2:14 | day 3:7" caption="count the halvings"]]',
        },
        "recap": [
            ("So, here it is again. Given the start and the end of a halving, ride the "
             "halving down and count the steps — that count is the days. The ratio of "
             "start to end is not the count; it hides the count as a power of 2.",
             '[[bars data="day 0:56 | day 1:28 | day 2:14 | day 3:7" caption="count the halvings, not the ratio"]]'),
            ("And that is a logarithm in work clothes.",
             '[[step eq="56 → 28 → 14 → 7 · 3 days"]]'),
        ],
        "bank": [
            {"a": 12, "b": 3, "op": "hcnt"},
            {"a": 20, "b": 5, "op": "hcnt"},
            {"a": 24, "b": 6, "op": "hcnt"},
            {"a": 16, "b": 2, "op": "hcnt"},
            {"a": 40, "b": 5, "op": "hcnt"},
            {"a": 48, "b": 6, "op": "hcnt"},
            {"a": 32, "b": 2, "op": "hcnt"},
            {"a": 48, "b": 3, "op": "hcnt"},
            {"a": 80, "b": 5, "op": "hcnt"},
            {"a": 64, "b": 2, "op": "hcnt"},
        ],
    },
    {
        "id": "pc-u3-money-doubles",
        "course": "precalc", "unit": 3,
        "topic": "Compound growth",
        "op": "cmpd", "max_value": 96,
        "levels": ("abstract",),
        "symbols": ("doubles", "years"),
        "advance_line": "Three in a row, and you can say why — you've got it! Count the doublings first, then double.",
        "why": [
            ("Why money? Because the exponential\'s favorite home is money. Save some "
             "dollars where the pile doubles every few years, and the growth is not a "
             "climb — it is a rocket. This lesson reads the rocket: how much after the "
             "years go by?",
             '[[goal text="Money doubles"]][[step eq="$ → ×2 → ×2 → ×2 …"]]'),
        ],
        "picture": [
            ("Here is a pile of 4 dollars as bars, doubling every 3 years: 4 at the "
             "start, 8 after 3 years, 16 after 6. Each bar is twice the one before — "
             "and the years only matter through how many doublings they hold.",
             '[[bars data="year 0:4 | year 3:8 | year 6:16" caption="4 dollars doubling every 3 years — two doublings in 6 years"]]'),
        ],
        "teach": [
            ("That is the method. 4 dollars, doubling every 3 years, left alone for 6 "
             "years. First count the doublings: 6 divided by 3 equals 2. Then double "
             "twice: 4, then 8, then 16. Sixteen dollars — the years only matter "
             "through the COUNT of doublings.",
             '[[bars data="year 0:4 | year 3:8 | year 6:16" caption="6 ÷ 3 = 2 doublings: 4 → 8 → 16"]][[step eq="6 ÷ 3 = 2 doublings"]][[step eq="4 → 8 → 16"]]'),
            ("The trap is thinking in plain adding: up 4, up 4 — that reaches 12 and "
             "stalls. Doubling reaches 16, then 32, then 64, pulling away faster every "
             "step. Exponential growth beats steady adding every time, given enough "
             "years.",
             '[[step eq="16 ✓ doubling · 12 ✗ steady adding"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 3 dollars doubling every 2 years, "
                        "for 6 years: three doublings — 3, then 6, then 12, then 24.",
                        '[[bars data="year 0:3 | year 2:6 | year 4:12 | year 6:24" caption="3 doublings: 3 → 6 → 12 → 24"]][[step eq="6 ÷ 2 = 3"]][[step eq="3 → 6 → 12 → 24"]]'),
             "ask": {'a': 2, 'b': 2, 'c': 6, 'op': 'cmpd'}},
            {"worked": ("One more together. 6 dollars doubling every 4 years, for 8 years: "
                        "two doublings — 6, then 12, then 24.",
                        '[[bars data="year 0:6 | year 4:12 | year 8:24" caption="2 doublings: 6 → 12 → 24"]][[step eq="8 ÷ 4 = 2"]][[step eq="6 → 12 → 24"]]'),
             "ask": {'a': 6, 'b': 4, 'c': 5, 'op': 'cmpd'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 4 dollars doubles "
                       "every 3 years, and after 6 years there are 16. Tap the reason "
                       "why."),
            "choices": ("because 6 years holds two doublings: 4 to 8 to 16 | because 6 "
                        "years adds 4 dollars twice: 12 | because the pile doubles once, "
                        "whatever the years"),
            "answer": "because 6 years holds two doublings: 4 to 8 to 16",
            "board": '[[bars data="year 0:4 | year 3:8 | year 6:16" caption="two doublings"]]',
        },
        "recap": [
            ("So, here it is again. Money that doubles every few years is read by "
             "counting the doublings first — the years divided by the doubling time — "
             "and then doubling that many times. Exponential growth pulls away from "
             "steady adding every time.",
             '[[bars data="year 0:4 | year 3:8 | year 6:16" caption="count the doublings first, then double"]]'),
            ("And that is the exponential, at home.",
             '[[step eq="6 ÷ 3 = 2 doublings"]][[step eq="4 → 8 → 16"]]'),
        ],
        "bank": [
            {"a": 2, "b": 2, "c": 2, "op": "cmpd"},
            {"a": 3, "b": 2, "c": 3, "op": "cmpd"},
            {"a": 4, "b": 2, "c": 4, "op": "cmpd"},
            {"a": 2, "b": 3, "c": 2, "op": "cmpd"},
            {"a": 5, "b": 2, "c": 5, "op": "cmpd"},
            {"a": 3, "b": 3, "c": 3, "op": "cmpd"},
            {"a": 2, "b": 4, "c": 2, "op": "cmpd"},
            {"a": 4, "b": 3, "c": 4, "op": "cmpd"},
            {"a": 5, "b": 3, "c": 5, "op": "cmpd"},
            {"a": 3, "b": 4, "c": 4, "op": "cmpd"},
        ],
    },
]
LESSONS.extend(_PRECALC_U3)

# =============================================================================
# PRE-CALC UNIT 4 -- Trigonometric Functions (build ln)
# The thread: the circle gets a NEW LANGUAGE and a map. Radians measure in
# half turns, negative angles spin backwards and earn a forwards name, every
# arrow hugs the flat line with its reference angle, and the sine wave's
# period bends to its multiplier. All of it deepens alg2-u8's compass-point
# work (sinp/cosp/spin/ampl) -- go past it, never over it again.
# =============================================================================
_PRECALC_U4 = [
    {
        "id": "pc-u4-the-half-turn-language",
        "course": "precalc", "unit": 4,
        "topic": "Radians",
        "op": "rad1", "max_value": 13,
        "levels": ("abstract",),
        "symbols": ("radians", "pi"),
        "advance_line": "Three in a row, and you can say why — you've got it! Count the half turns — that is the pi's.",
        "why": [
            ("Why a second language for the circle? Unit Four hands the circle a new "
             "way to measure. Degrees chop a turn into 360 thin slices; mathematicians "
             "also measure in radians, and the dictionary has one entry: a half turn — "
             "180 degrees — is exactly pi radians. Pi, the circle number, near 3.14.",
             '[[goal text="The half-turn language"]][[step eq="180° = π rad"]]'),
        ],
        "picture": [
            ("Here is a half turn beside a whole angle, as bars. The short bar is 180 — "
             "one half turn, one pi. The tall bar is 3600. The question radians ask is "
             "how many of the short bar fit inside the tall one — that count is the "
             "number of pi's.",
             '[[bars data="a half turn:180 | 3600°:3600" caption="how many half turns of 180 fit in 3600°?"]]'),
        ],
        "teach": [
            ("That is the method: count half turns to translate. 3600 divided by 180 "
             "equals 20 — twenty half turns, so 3600 degrees is 20 pi radians. And 180 "
             "itself is one half turn: 1 pi. The number of pi's IS the number of half "
             "turns; nothing else to it.",
             '[[bars data="a half turn:180 | 3600°:3600" caption="20 half turns of 180 fit — 3600° = 20π rad"]][[step eq="3600 ÷ 180 = 20"]][[step eq="3600° = 20π rad"]]'),
            ("Two traps. Counting QUARTER turns says twice too many pi's — 90 degrees "
             "is not one pi, it is half of one. And handing the degrees back unchanged "
             "is no translation at all. Divide by 180; the count of half turns is the "
             "answer.",
             '[[step eq="÷ 180 → the count of half turns"]][[step eq="quarter-turn count ✗ · degrees copied ✗"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 2520 degrees: 2520 divided by 180 "
                        "equals 14 — 14 pi radians.",
                        '[[numberline min="0" max="2520" hops="0,180,360,540,720,900,1080,1260,1440,1620,1800,1980,2160,2340,2520" caption="14 half turns — 14π"]][[step eq="2520 ÷ 180 = 14"]][[step eq="so 14π"]]'),
             "ask": {'a': 12, 'b': 0, 'op': 'rad1'}},
            {"worked": ("One more together. 2700 degrees: 2700 divided by 180 equals 15 — "
                        "15 pi radians.",
                        '[[bars data="a half turn:180 | 2700°:2700" caption="15 half turns of 180 fit — 15π"]][[step eq="2700 ÷ 180 = 15"]][[step eq="so 15π"]]'),
             "ask": {'a': 13, 'b': 0, 'op': 'rad1'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 3600 degrees is 20 pi "
                       "radians. Tap the reason why."),
            "choices": ("because 180 is one pi and twenty half turns fit | because a "
                        "quarter turn of 90 is one pi | because the degrees are the pi's "
                        "already"),
            "answer": "because 180 is one pi and twenty half turns fit",
            "board": '[[bars data="a half turn:180 | 3600°:3600" caption="20 half turns — 20π"]]',
        },
        "recap": [
            ("So, here it is again. Radians measure in half turns: a half turn of 180 "
             "degrees is one pi, so divide the degrees by 180 and the count of half "
             "turns is the number of pi's. Never count quarter turns, and never hand "
             "the degrees back.",
             '[[bars data="a half turn:180 | 3600°:3600" caption="count the half turns"]]'),
            ("And that is the circle's second language.",
             '[[step eq="180° = π rad"]][[step eq="3600° = 20π rad"]]'),
        ],
        "bank": [
            {"a": 2, "b": 0, "op": "rad1"},
            {"a": 3, "b": 0, "op": "rad1"},
            {"a": 4, "b": 0, "op": "rad1"},
            {"a": 5, "b": 0, "op": "rad1"},
            {"a": 6, "b": 0, "op": "rad1"},
            {"a": 7, "b": 0, "op": "rad1"},
            {"a": 8, "b": 0, "op": "rad1"},
            {"a": 9, "b": 0, "op": "rad1"},
            {"a": 10, "b": 0, "op": "rad1"},
            {"a": 11, "b": 0, "op": "rad1"},
        ],
    },
    {
        "id": "pc-u4-the-backwards-spin",
        "course": "precalc", "unit": 4,
        "topic": "Negative angles",
        "op": "nspn", "max_value": 340,
        "levels": ("abstract",),
        "symbols": ("negative", "turn"),
        "advance_line": "Three in a row, and you can say why — you've got it! Add a full turn — 360 — to name it forwards.",
        "why": [
            ("Why can an angle be negative? Because the arrow can spin backwards too. A "
             "negative angle winds the other way: negative 45 means swing 45 degrees "
             "DOWN from flat right instead of up. Same circle, opposite turn — and "
             "every backwards angle has a forwards name.",
             '[[goal text="The backwards spin"]][[step eq="−45° · wound the other way"]]'),
        ],
        "picture": [
            ("Here is the circle with the arrow wound 45 degrees backwards — it hangs "
             "below flat right, and the red arc runs the other way round. Look at where "
             "the arrow points: some forwards angle lands in exactly that spot. That "
             "forwards angle is the name we want.",
             '[[unitcircle angle="-45" values="0" caption="−45° — the arrow hangs 45 below flat right; a forwards angle lands here too"]]'),
        ],
        "teach": [
            ("That is the method: to find it, add one full turn. Negative 45 plus 360 "
             "equals 315. Check with your arms: 45 down from flat right, or 315 the long "
             "way around — the SAME arrow. One direction, two names, and the positive "
             "name is 360 take away the backwards one.",
             '[[unitcircle angle="315" values="0" caption="315° — the same arrow, named forwards"]][[step eq="−45° + 360° = 315°"]]'),
            ("Two traps. Dropping the minus says 45 — the mirror image, above the line "
             "when the arrow hangs below. And adding only a half turn — 135 here — parks "
             "the arrow on the wrong side entirely. A full turn, 360, always.",
             '[[step eq="315° ✓"]][[step eq="45 ✗ mirror · 135 ✗ half turn"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Negative 25: add 360 — 335.",
                        '[[unitcircle angle="335" values="0" caption="−25° is 335° forwards"]][[step eq="−25° + 360° = 335°"]]'),
             "ask": {'a': 70, 'b': 0, 'op': 'nspn'}},
            {"worked": ("One more together. Negative 155: add a full turn — negative 155 "
                        "plus 360 is 205.",
                        '[[unitcircle angle="205" values="0" caption="−155° is 205° forwards"]][[step eq="−155° + 360° = 205°"]]'),
             "ask": {'a': 110, 'b': 0, 'op': 'nspn'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Negative 45 degrees "
                       "and 315 degrees name the same arrow. Tap the reason why."),
            "choices": ("because a full turn of 360 lands on the same spot | because "
                        "dropping the minus sign changes nothing | because a half turn of "
                        "180 brings it back"),
            "answer": "because a full turn of 360 lands on the same spot",
            "board": '[[unitcircle angle="315" values="0" caption="−45° + 360° = 315°"]]',
        },
        "recap": [
            ("So, here it is again. A negative angle winds backwards, and every "
             "backwards angle has a forwards name: add one full turn of 360. Never "
             "drop the minus — that is the mirror image — and never add only a half "
             "turn.",
             '[[unitcircle angle="-45" values="0" caption="wound backwards — add a full turn to name it forwards"]]'),
            ("And that is one arrow with two names.",
             '[[step eq="−45° + 360° = 315°"]]'),
        ],
        "bank": [
            {"a": 20, "b": 0, "op": "nspn"},
            {"a": 30, "b": 0, "op": "nspn"},
            {"a": 40, "b": 0, "op": "nspn"},
            {"a": 50, "b": 0, "op": "nspn"},
            {"a": 60, "b": 0, "op": "nspn"},
            {"a": 80, "b": 0, "op": "nspn"},
            {"a": 100, "b": 0, "op": "nspn"},
            {"a": 120, "b": 0, "op": "nspn"},
            {"a": 140, "b": 0, "op": "nspn"},
            {"a": 160, "b": 0, "op": "nspn"},
        ],
    },
    {
        "id": "pc-u4-hug-the-flat-line",
        "course": "precalc", "unit": 4,
        "topic": "Reference angles",
        "op": "refq", "max_value": 170,
        "levels": ("abstract",),
        "symbols": ("reference", "gap"),
        "advance_line": "Three in a row, and you can say why — you've got it! The gap to the flat line — that is the reference.",
        "why": [
            ("Why hug the flat line? Every arrow, wherever it lands, has a reference "
             "angle: the small gap between the arrow and the flat line through the "
             "circle's middle. This lesson lives in the second quarter — past straight "
             "up, short of flat left — where that gap is measured to 180.",
             '[[goal text="Hug the flat line"]][[step eq="reference = the gap to the flat line"]]'),
        ],
        "picture": [
            ("Here is the flat line, 180 degrees edge to edge, with an arrow at 175. "
             "The arrow leans almost all the way over to flat left, and the gap between "
             "them is tiny — that little gap, marked with the question mark, is the "
             "reference angle.",
             '[[angle deg="180" split="175" caption="the arrow at 175° — the small gap to flat left is the reference"]]'),
        ],
        "teach": [
            ("That is the method. Take 175 degrees: the arrow sits 5 short of flat "
             "left, so its reference angle is 180 take away 175 — 5 degrees. The "
             "reference angle is why the trig values at 175 echo the ones at 5: the "
             "circle reuses its first quarter, everywhere.",
             '[[angle deg="180" split="175,5" caption="180 − 175 = 5° — the gap to flat left"]][[step eq="175° → 180 − 175 = 5°"]]'),
            ("Now 135: the gap to flat left is 45. The trap is measuring from straight "
             "up — that says 45 too here, by coincidence, but at 135 only! Measure from "
             "straight up at 145 and you get 55; the true reference is 35. Hug the FLAT "
             "line, never the top.",
             '[[step eq="135° → 45 ✓"]][[step eq="145°: from the top 55 ✗ · reference 35 ✓"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 155 degrees: 180 take away 155 — "
                        "the reference angle is 25.",
                        '[[angle deg="180" split="155,25" caption="180 − 155 = 25°"]][[step eq="155° → 180 − 155 = 25°"]]'),
             "ask": {'a': 125, 'b': 0, 'op': 'refq'}},
            {"worked": ("One more together. 112 degrees: 180 take away 112 — the reference "
                        "angle is 68.",
                        '[[angle deg="180" split="112,68" caption="180 − 112 = 68°"]][[step eq="112° → 180 − 112 = 68°"]]'),
             "ask": {'a': 165, 'b': 0, 'op': 'refq'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. The reference angle of "
                       "175 degrees is 5 degrees. Tap the reason why."),
            "choices": ("because the gap to flat left is 180 take away 175 | because the "
                        "reference is measured from straight up | because the reference "
                        "angle is the angle itself"),
            "answer": "because the gap to flat left is 180 take away 175",
            "board": '[[angle deg="180" split="175,5" caption="the gap to flat left: 5°"]]',
        },
        "recap": [
            ("So, here it is again. The reference angle is the small gap between the "
             "arrow and the flat line — in the second quarter, 180 take away the "
             "angle. Never measure from straight up, and never hand back the angle "
             "itself.",
             '[[angle deg="180" split="175,5" caption="hug the flat line"]]'),
            ("And that is why the circle reuses its first quarter everywhere.",
             '[[step eq="175° → 180 − 175 = 5°"]]'),
        ],
        "bank": [
            {"a": 100, "b": 0, "op": "refq"},
            {"a": 105, "b": 0, "op": "refq"},
            {"a": 110, "b": 0, "op": "refq"},
            {"a": 115, "b": 0, "op": "refq"},
            {"a": 120, "b": 0, "op": "refq"},
            {"a": 130, "b": 0, "op": "refq"},
            {"a": 140, "b": 0, "op": "refq"},
            {"a": 150, "b": 0, "op": "refq"},
            {"a": 160, "b": 0, "op": "refq"},
            {"a": 170, "b": 0, "op": "refq"},
        ],
    },
    {
        "id": "pc-u4-the-faster-wave",
        "course": "precalc", "unit": 4,
        "topic": "Period",
        "op": "wper", "max_value": 120,
        "levels": ("abstract",),
        "symbols": ("period", "repeats"),
        "advance_line": "Three in a row, and you can say why — you've got it! Divide 360 by the multiplier.",
        "why": [
            ("Why does a wave get faster? The plain sine wave repeats its whole story "
             "every 360 degrees — its period. Write y equals the sine of 2 x and the "
             "wave wiggles twice as fast: the story that took 360 degrees now fits in "
             "180. Faster wiggle, shorter period.",
             '[[goal text="The faster wave"]][[step eq="sin 2x: the story fits in 180°"]]'),
        ],
        "picture": [
            ("Here are two waves on one grid, the axis in degrees. The slow one is the "
             "plain sine — one rise and one fall across the whole 360. The fast one is "
             "the sine of 2 x, and it tells that same story twice in the same room: "
             "up, down, up, down.",
             '[[graph func="sin(x*pi/180); sin(2*x*pi/180)" names="sin x; sin 2x" range="0..360" yrange="-1.5..1.5" caption="the plain sine and the sine of 2x — the fast one repeats by 180°"]]'),
        ],
        "teach": [
            ("That is the method: divide 360 by the multiplier. y equals the sine of "
             "30 x races thirty times faster, so it repeats every 360 divided by 30 — "
             "12 degrees. The whole rise-and-fall, squeezed into 12.",
             '[[graph func="sin(30*x*pi/180)" names="sin 30x" lines="x=12" range="0..360" yrange="-1.5..1.5" caption="the sine of 30x — one full story by x = 12°"]][[step eq="period = 360 ÷ 30 = 12°"]]'),
            ("Two traps. Faster does NOT stretch the wave: 360 times the multiplier "
             "points the wrong way — a faster wave repeats SOONER. And 360 unchanged "
             "is the plain sine's habit; the multiplier is standing right there. "
             "Divide, always.",
             '[[step eq="÷ ✓ shorter"]][[step eq="× 360 ✗ longer · 360 ✗ the plain habit"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. The sine of 36 x: 360 divided by "
                        "36 — the period is 10 degrees.",
                        '[[graph func="sin(36*x*pi/180)" names="sin 36x" lines="x=10" range="0..360" yrange="-1.5..1.5" caption="360 ÷ 36 = 10°"]][[step eq="360 ÷ 36 = 10°"]]'),
             "ask": {'a': 20, 'b': 0, 'op': 'wper'}},
            {"worked": ("One more together. The sine of 40 x: 360 divided by 40 — the "
                        "period is 9 degrees.",
                        '[[graph func="sin(40*x*pi/180)" names="sin 40x" lines="x=9" range="0..360" yrange="-1.5..1.5" caption="360 ÷ 40 = 9°"]][[step eq="360 ÷ 40 = 9°"]]'),
             "ask": {'a': 24, 'b': 0, 'op': 'wper'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. The sine of 30 x "
                       "repeats every 12 degrees. Tap the reason why."),
            "choices": ("because the faster wave repeats every 360 divided by 30 | because "
                        "a faster wave stretches to 360 times the multiplier | because "
                        "every sine wave repeats every 360"),
            "answer": "because the faster wave repeats every 360 divided by 30",
            "board": '[[graph func="sin(30*x*pi/180)" names="sin 30x" lines="x=12" range="0..360" yrange="-1.5..1.5" caption="360 ÷ 30 = 12°"]]',
        },
        "recap": [
            ("So, here it is again. The plain sine repeats every 360 degrees; a "
             "multiplier on x speeds the wave up, and faster means sooner — the "
             "period is 360 divided by the multiplier. Never times it, and never keep "
             "the plain 360.",
             '[[graph func="sin(x*pi/180); sin(2*x*pi/180)" names="sin x; sin 2x" range="0..360" yrange="-1.5..1.5" caption="divide 360 by the multiplier"]]'),
            ("And that is a wave that bends to its multiplier.",
             '[[step eq="period = 360 ÷ 30 = 12°"]]'),
        ],
        "bank": [
            {"a": 3, "b": 0, "op": "wper"},
            {"a": 4, "b": 0, "op": "wper"},
            {"a": 5, "b": 0, "op": "wper"},
            {"a": 6, "b": 0, "op": "wper"},
            {"a": 8, "b": 0, "op": "wper"},
            {"a": 9, "b": 0, "op": "wper"},
            {"a": 10, "b": 0, "op": "wper"},
            {"a": 12, "b": 0, "op": "wper"},
            {"a": 15, "b": 0, "op": "wper"},
            {"a": 18, "b": 0, "op": "wper"},
        ],
    },
]
LESSONS.extend(_PRECALC_U4)

# =============================================================================
# PRE-CALC UNIT 5 -- Analytic Trigonometry (build ln)
# The thread: what is ALWAYS true. sin^2 + cos^2 splits one whole between the
# pair, sine and cosine are partners across ninety, the mirror flips height
# and never across (even/odd -- lm's minus parade, on the circle), and
# solving a trig equation means counting the crossings per sweep.
# =============================================================================
_PRECALC_U5 = [
    {
        "id": "pc-u5-one-whole-between-them",
        "course": "precalc", "unit": 5,
        "topic": "The Pythagorean identity",
        "op": "pyid", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("squared", "hundredths"),
        "advance_line": "Three in a row, and you can say why — you've got it! The pair splits one whole — take the share from 100.",
        "why": [
            ("Why is there one whole between them? Unit Five is about what is ALWAYS "
             "true, and here is trigonometry's most famous always: for every angle, sine "
             "squared plus cosine squared equals exactly 1. Height squared plus across "
             "squared — one whole, every single time. It is Pythagoras, living on the "
             "circle.",
             '[[goal text="One whole between them"]][[step eq="sin² + cos² = 1 — always"]]'),
        ],
        "picture": [
            ("Here is the whole as a hundred square — 1 is 100 hundredths. Sine "
             "squared has taken 20 of the little squares, shaded. Everything left "
             "white belongs to cosine squared: the pair splits the one whole between "
             "them, and neither gets more than the square holds.",
             '[[hundredgrid shaded="20" eq="sin² = 20 of 100" caption="sine squared shaded — the rest of the whole is cosine squared"]]'),
        ],
        "teach": [
            ("That is the method: split the whole into hundredths and take the share "
             "from 100. If sine squared takes 20 of them, cosine squared holds the rest "
             "— 100 take away 20 is 80. The pair splits one whole between them, "
             "wherever the arrow points.",
             '[[hundredgrid shaded="20" eq="20 + 80 = 100" caption="sin² 20 shaded, cos² 80 left"]][[step eq="sin² = 20/100"]] [[step eq="cos² = 80/100"]]'),
            ("Two traps. Copying sine's share hands back the number you were given — "
             "the question asked for the PARTNER. And answering 100 forgets that sine "
             "already claimed its part. Take the given share away from 100; what is "
             "left is cosine's.",
             '[[step eq="100 − given ✓"]][[step eq="copied ✗ · 100 ✗ the whole"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Sine squared equals 70 hundredths: "
                        "100 take away 70 — cosine squared is 30 hundredths.",
                        '[[hundredgrid shaded="70" eq="70 + 30 = 100" caption="70 shaded, 30 left"]][[step eq="sin² = 70/100"]] [[step eq="cos² = 30/100"]]'),
             "ask": {'a': 30, 'b': 0, 'op': 'pyid'}},
            {"worked": ("One more together. Sine squared 45 hundredths: 100 take away 45 — "
                        "cosine squared is 55 hundredths.",
                        '[[hundredgrid shaded="45" eq="45 + 55 = 100" caption="45 shaded, 55 left"]][[step eq="sin² = 45/100"]] [[step eq="cos² = 55/100"]]'),
             "ask": {'a': 55, 'b': 0, 'op': 'pyid'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Sine squared is 20 "
                       "hundredths, so cosine squared is 80 hundredths. Tap the reason why."),
            "choices": ("because sine squared and cosine squared always add up to one whole "
                        "| because cosine squared always equals sine squared | because "
                        "cosine squared is always the whole 100"),
            "answer": "because sine squared and cosine squared always add up to one whole",
            "board": '[[hundredgrid shaded="20" eq="20 + 80 = 100" caption="one whole between them"]]',
        },
        "recap": [
            ("So, here it is again. Sine squared plus cosine squared equals 1, always — "
             "one whole split between the pair. Given sine's share of the hundred, "
             "take it away from 100 and the rest is cosine's. Never copy the share, "
             "and never answer the whole.",
             '[[hundredgrid shaded="20" eq="20 + 80 = 100" caption="the pair splits one whole"]]'),
            ("And that is Pythagoras, living on the circle.",
             '[[step eq="sin² + cos² = 1"]]'),
        ],
        "bank": [
            {"a": 4, "b": 0, "op": "pyid"},
            {"a": 10, "b": 0, "op": "pyid"},
            {"a": 19, "b": 0, "op": "pyid"},
            {"a": 25, "b": 0, "op": "pyid"},
            {"a": 36, "b": 0, "op": "pyid"},
            {"a": 40, "b": 0, "op": "pyid"},
            {"a": 64, "b": 0, "op": "pyid"},
            {"a": 75, "b": 0, "op": "pyid"},
            {"a": 81, "b": 0, "op": "pyid"},
            {"a": 91, "b": 0, "op": "pyid"},
        ],
    },
    {
        "id": "pc-u5-partners-across-ninety",
        "course": "precalc", "unit": 5,
        "topic": "Cofunctions",
        "op": "cofn", "max_value": 80,
        "levels": ("abstract",),
        "symbols": ("cosine", "partners"),
        "advance_line": "Three in a row, and you can say why — you've got it! Partners finish 90 together.",
        "why": [
            ("Why are sine and cosine partners? The CO in cosine says so. Take any "
             "angle and its partner across 90: the two sharp corners of one right "
             "triangle. The sine of one equals the cosine of the other, exactly, every "
             "time.",
             '[[goal text="Partners across ninety"]][[step eq="sin a = cos (90 − a)"]]'),
        ],
        "picture": [
            ("Here is one right triangle with its two sharp corners: 35 degrees at one, "
             "and a question mark at the other. A triangle's corners add up to 180, the "
             "square corner is 90, so the two sharp ones share the other 90 between "
             "them. That is the partnership.",
             '[[triangle v="A,B,C" right="B" angles="35,90,?" caption="the square corner takes 90 — the two sharp corners share the other 90"]]'),
        ],
        "teach": [
            ("That is the method: partners finish 90 together. The sine of 35 equals "
             "the cosine of 55, because 35 plus 55 equals 90. One triangle, two sharp "
             "corners; what one corner calls height, the other calls across. Swap the "
             "name, swap the angle — across 90.",
             '[[triangle v="A,B,C" right="B" angles="35,90,55" caption="35 + 55 = 90 — sin 35° = cos 55°"]][[step eq="sin 35° = cos 55° · 35 + 55 = 90"]]'),
            ("Two traps. Keeping the SAME angle — the sine of 35 does not equal the "
             "cosine of 35. And adding 90 overshoots: the partner of 35 is 55, never "
             "125. Partners share the 90; together they finish it.",
             '[[step eq="35 → partner 55 ✓"]][[step eq="35 ✗ same angle · 125 ✗ added 90"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. The sine of 85 equals the cosine "
                        "of 5 — together they finish 90.",
                        '[[triangle v="A,B,C" right="B" angles="85,90,5" caption="85 + 5 = 90"]][[step eq="sin 85° = cos 5°"]]'),
             "ask": {'a': 25, 'b': 0, 'op': 'cofn'}},
            {"worked": ("One more together. The sine of 42 equals the cosine of 48, "
                        "because 42 plus 48 equals 90.",
                        '[[triangle v="A,B,C" right="B" angles="42,90,48" caption="42 + 48 = 90"]][[step eq="sin 42° = cos 48°"]]'),
             "ask": {'a': 75, 'b': 0, 'op': 'cofn'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. The sine of 35 "
                       "degrees equals the cosine of 55 degrees. Tap the reason why."),
            "choices": ("because the two sharp corners of a right triangle finish 90 "
                        "together | because the sine and the cosine of one angle are "
                        "equal | because the partner is the angle plus 90"),
            "answer": "because the two sharp corners of a right triangle finish 90 together",
            "board": '[[triangle v="A,B,C" right="B" angles="35,90,55" caption="partners across ninety"]]',
        },
        "recap": [
            ("So, here it is again. Sine and cosine are partners: the sine of an angle "
             "equals the cosine of 90 take away that angle — the two sharp corners of "
             "one right triangle. Never keep the same angle, and never add 90.",
             '[[triangle v="A,B,C" right="B" angles="35,90,55" caption="partners finish 90 together"]]'),
            ("And that is what the CO in cosine means.",
             '[[step eq="sin a = cos (90 − a)"]]'),
        ],
        "bank": [
            {"a": 10, "b": 0, "op": "cofn"},
            {"a": 15, "b": 0, "op": "cofn"},
            {"a": 20, "b": 0, "op": "cofn"},
            {"a": 30, "b": 0, "op": "cofn"},
            {"a": 40, "b": 0, "op": "cofn"},
            {"a": 50, "b": 0, "op": "cofn"},
            {"a": 60, "b": 0, "op": "cofn"},
            {"a": 65, "b": 0, "op": "cofn"},
            {"a": 70, "b": 0, "op": "cofn"},
            {"a": 80, "b": 0, "op": "cofn"},
        ],
    },
    {
        "id": "pc-u5-the-mirror-knows",
        "course": "precalc", "unit": 5,
        "topic": "Even and odd functions",
        "op": "negf", "max_value": 810, "min_value": -1,
        "levels": ("abstract",),
        "symbols": ("mirror", "flips"),
        "advance_line": "Three in a row, and you can say why — you've got it! The mirror flips height, never across.",
        "why": [
            ("Why does the mirror know? Feed a negative angle into cosine and sine and "
             "watch. The backwards spin is the forwards spin's mirror image — flipped "
             "across the flat line. The mirror flips HEIGHT: what was up hangs down. "
             "It never flips ACROSS: left stays left, right stays right.",
             '[[goal text="The mirror knows"]][[step eq="−a is a\'s mirror · height flips, across holds"]]'),
        ],
        "picture": [
            ("Here is the arrow at 45 degrees, and here it is wound 45 degrees "
             "backwards. Look at the two: the tips sit the same distance to the right — "
             "the across held. One tip is up and the other is down — the height "
             "flipped. That is the whole lesson in one picture.",
             '[[unitcircle angle="45" values="0" caption="45° — up and to the right"]][[unitcircle angle="-45" values="0" caption="−45° — DOWN and to the right: the mirror"]]'),
        ],
        "teach": [
            ("That is the method. Cosine — the across — ignores the minus completely: "
             "the cosine of negative 180 equals the cosine of 180, flat left, negative "
             "1. Cosine is called an even function, like the even powers of the minus "
             "parade: the minus vanishes.",
             '[[unitcircle angle="-180" caption="−180° — flat left either way: across −1"]][[step eq="cos(−180°) = cos(180°) = −1"]][[step eq="even: the minus vanishes"]]'),
            ("Sine — the height — FLIPS: the sine of negative 90 is the opposite of "
             "the sine of 90. Straight up becomes straight down: 1 becomes negative 1. "
             "Sine is an odd function — one minus survives, just like an odd power. The "
             "mirror knows which is which.",
             '[[unitcircle angle="-90" caption="−90° — straight DOWN: height −1"]][[step eq="sin(−90°) = −sin(90°) = −1"]][[step eq="odd: one minus survives"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. The cosine of negative 450: spin "
                        "back a full turn, then a quarter more — straight down. The across "
                        "of straight down is 0.",
                        '[[unitcircle angle="-450" caption="−450° — a full turn back and a quarter more: straight down, across 0"]][[step eq="cos(−450°) = 0"]]'),
             "ask": {'a': 720, 'b': 0, 'c': 0, 'op': 'negf'}},
            {"worked": ("One more together. The sine of negative 540: a turn and a half "
                        "backwards lands flat left — height 0.",
                        '[[unitcircle angle="-540" caption="−540° — a turn and a half back: flat left, height 0"]][[step eq="sin(−540°) = 0"]]'),
             "ask": {'a': 810, 'b': 0, 'c': 1, 'op': 'negf'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. The sine of negative "
                       "90 degrees is negative 1. Tap the reason why."),
            "choices": ("because the mirror flips the height, so straight up becomes "
                        "straight down | because the mirror flips the across | because a "
                        "backwards spin lands where the forwards one does"),
            "answer": "because the mirror flips the height, so straight up becomes straight down",
            "board": '[[unitcircle angle="-90" caption="−90° — straight down: height −1"]]',
        },
        "recap": [
            ("So, here it is again. A backwards spin is the mirror image of the "
             "forwards one: the height flips and the across holds. So cosine is even — "
             "the minus vanishes — and sine is odd — one minus survives. The mirror "
             "knows which is which.",
             '[[unitcircle angle="-45" values="0" caption="the mirror flips height, never across"]]'),
            ("And that is the minus parade, on the circle.",
             '[[step eq="cos(−a) = cos a · sin(−a) = −sin a"]]'),
        ],
        "bank": [
            {"a": 90, "b": 0, "c": 0, "op": "negf"},
            {"a": 180, "b": 0, "c": 1, "op": "negf"},
            {"a": 270, "b": 0, "c": 0, "op": "negf"},
            {"a": 270, "b": 0, "c": 1, "op": "negf"},
            {"a": 360, "b": 0, "c": 0, "op": "negf"},
            {"a": 360, "b": 0, "c": 1, "op": "negf"},   # (tp) was (90, sine): the teach demonstrates sin(−90)
            {"a": 450, "b": 0, "c": 1, "op": "negf"},
            {"a": 540, "b": 0, "c": 0, "op": "negf"},
            {"a": 630, "b": 0, "c": 1, "op": "negf"},
            {"a": 630, "b": 0, "c": 0, "op": "negf"},   # (tp) was (180, cosine): the teach demonstrates cos(−180)
        ],
    },
    {
        "id": "pc-u5-count-the-crossings",
        "course": "precalc", "unit": 5,
        "topic": "Solving trig equations",
        "op": "sols", "max_value": 4,
        "levels": ("abstract",),
        "symbols": ("turn", "finish"),
        "advance_line": "Three in a row, and you can say why — you've got it! Count one turn's crossings, then times the turns.",
        "why": [
            ("Why count crossings? The last identity skill is counting answers. An "
             "equation like: the sine equals 0 — how many angles solve it? Sweep the "
             "arrow one full turn, and count every moment the height hits the target — "
             "skip the start, keep the finish.",
             '[[goal text="Count the crossings"]][[step eq="sweep · skip the start, keep the finish"]]'),
        ],
        "picture": [
            ("Here is the sine wave through three full turns, with the level line y "
             "equals 0 drawn across it. Every place the wave touches that line is one "
             "answer. The wave starts ON the line — that touch is the start, and the "
             "start is not counted.",
             '[[graph func="sin(x*pi/180)" names="sine" lines="y=0" range="0..1080" yrange="-1.5..1.5" caption="the sine through three turns and the line y = 0 — every touch after the start counts"]]'),
        ],
        "teach": [
            ("That is the method. Each turn, the height is 0 at flat left and again at "
             "the finish — twice a turn. Three turns, so three times twice: the sine "
             "equals 0 six times. The middle value gets hit going up AND coming down.",
             '[[graph func="sin(x*pi/180)" names="sine" lines="y=0" points="(180,0),(360,0),(540,0),(720,0),(900,0),(1080,0)" range="0..1080" yrange="-1.5..1.5" caption="6 touches after the start — twice each turn"]][[step eq="3 turns · sin = 0"]][[step eq="2 × 3 = 6"]]'),
            ("Now sine equal 1 across the same three turns: only straight up, once a "
             "turn — 3. The ends of the swing get touched once each. The trap answers "
             "4 per turn, one per quarter — but the ends of the swing live in ONE spot "
             "each. Count the true crossings, then times the turns.",
             '[[graph func="sin(x*pi/180)" names="sine" lines="y=1" points="(90,1),(450,1),(810,1)" range="0..1080" yrange="-1.5..1.5" caption="3 touches — once each turn, at straight up"]][[step eq="3 turns · sin = 1"]][[step eq="1 × 3 = 3"]][[step eq="4 per turn ✗ one-per-quarter"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. The cosine equal 0, three turns: "
                        "twice each turn — straight up and straight down — times 3 is 6.",
                        '[[graph func="cos(x*pi/180)" names="cosine" lines="y=0" points="(90,0),(270,0),(450,0),(630,0),(810,0),(990,0)" range="0..1080" yrange="-1.5..1.5" caption="cos = 0: twice each turn — 6 in three turns"]][[step eq="cos = 0 · 3 turns"]] [[step eq="2 × 3 = 6"]]'),
             "ask": {'a': 0, 'b': 1, 'c': 1, 'op': 'sols'}},
            {"worked": ("One more together. Sine equal negative 1, three turns: once each "
                        "— 3.",
                        '[[graph func="sin(x*pi/180)" names="sine" lines="y=-1" points="(270,-1),(630,-1),(990,-1)" range="0..1080" yrange="-1.5..1.5" caption="sin = −1: once each turn, at straight down — 3"]][[step eq="sin = −1 · 3 turns"]] [[step eq="1 × 3 = 3"]]'),
             "ask": {'a': -1, 'b': 2, 'c': 0, 'op': 'sols'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Across three turns, "
                       "the sine equals 1 three times. Tap the reason why."),
            "choices": ("because the height reaches 1 only at straight up, once each turn "
                        "| because the height reaches 1 once in every quarter | because "
                        "the height reaches 1 going up and coming down"),
            "answer": "because the height reaches 1 only at straight up, once each turn",
            "board": '[[graph func="sin(x*pi/180)" names="sine" lines="y=1" points="(90,1),(450,1),(810,1)" range="0..1080" yrange="-1.5..1.5" caption="once each turn"]]',
        },
        "recap": [
            ("So, here it is again. To count the answers of a trig equation, sweep one "
             "turn and count the crossings — the middle value twice, the ends of the "
             "swing once. Skip the start, keep the finish, then times the turns. Never "
             "say four just because there are four quarters.",
             '[[graph func="sin(x*pi/180)" names="sine" lines="y=0" range="0..1080" yrange="-1.5..1.5" caption="count one turn\'s crossings, then times the turns"]]'),
            ("And that is solving, by counting.",
             '[[step eq="sin = 0: 2 each turn · sin = 1: 1 each turn"]]'),
        ],
        "bank": [
            {"a": 1, "b": 1, "c": 0, "op": "sols"},
            {"a": -1, "b": 1, "c": 0, "op": "sols"},
            {"a": 1, "b": 1, "c": 1, "op": "sols"},
            {"a": -1, "b": 1, "c": 1, "op": "sols"},
            {"a": 0, "b": 1, "c": 0, "op": "sols"},
            {"a": 1, "b": 2, "c": 0, "op": "sols"},
            {"a": -1, "b": 2, "c": 1, "op": "sols"},
            {"a": 1, "b": 2, "c": 1, "op": "sols"},
            {"a": 0, "b": 2, "c": 0, "op": "sols"},
            {"a": 0, "b": 2, "c": 1, "op": "sols"},
        ],
    },
]
LESSONS.extend(_PRECALC_U5)

# =============================================================================
# PRE-CALC UNIT 6 -- Applications of Trigonometry (build lo)
# The thread: trigonometry PUTS ON WORK CLOTHES. Area from two sides and the
# angle between them, a ramp's climb from the 30-degree sine, a ship's bearing
# wrapped past the full turn (ln's coterminal rule, at sea), and an arrow's
# length from its two steps -- Geometry's Pythagoras, wearing vector clothes.
# The [[vector]] renderer prints |v|, so it is TEACH-ONLY here.
# =============================================================================
_PRECALC_U6 = [
    {
        "id": "pc-u6-two-sides-and-the-angle",
        "course": "precalc", "unit": 6,
        "topic": "Area from two sides",
        "op": "arsn", "max_value": 40,
        "levels": ("abstract",),
        "symbols": ("sine", "between"),
        "advance_line": "Three in a row, and you can say why — you've got it! Half the product, times the sine.",
        "why": [
            ("Why two sides and the angle? Unit Six puts trigonometry to work, "
             "starting with area. Base times height, halved, needs a height you may "
             "not have. Two sides and the angle between them are enough: the area is "
             "half of one side, times the other side, times the sine of that angle.",
             '[[goal text="Two sides and the angle"]][[step eq="area = ½ · side · side · sin(angle)"]]'),
        ],
        "picture": [
            ("Here are three triangles drawn true, all with sides 10 and 4. The first "
             "has 90 degrees between them, the second 30, the third 150. Look how the "
             "right angle stands the short side straight up, and how the two others "
             "lean it over — the sharp one forwards, the wide one back.",
             '[[triangle v="A,B,C" sas="10,4,90" sides="10,,4" angles="90,," caption="sides 10 and 4 — 90° between them"]][[triangle v="A,B,C" sas="10,4,30" sides="10,,4" angles="30,," caption="the same sides — 30° between them"]][[triangle v="A,B,C" sas="10,4,150" sides="10,,4" angles="150,," caption="the same sides — 150° between them"]]'),
        ],
        "teach": [
            ("That is the method, and two sines carry this lesson. The sine of 90 "
             "degrees is 1, so a right angle hands over half the product outright. "
             "Sides 10 and 4, with 90 degrees between them: they cover half of 40, an "
             "area of 20.",
             '[[triangle v="A,B,C" sas="10,4,90" sides="10,,4" angles="90,," caption="area = ½ · 10 · 4 · 1 = 20"]][[step eq="sin 90° = 1"]][[step eq="½ · 10 · 4 · 1 = 20"]]'),
            ("The sine of 30 degrees is exactly one half — keep that one in your "
             "pocket. So 30 degrees between those same sides quarters the product: 10. "
             "And 150 shares that sine, because its reference angle is 30 — the wide "
             "triangle covers what the sharp one covers.",
             '[[triangle v="A,B,C" sas="10,4,150" sides="10,,4" angles="150,," caption="150° leans back, and covers the same 10"]][[step eq="30° → ¼ · 40 = 10"]][[step eq="150° → reference 30° → 10 as well"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Sides 12 and 4, with a right angle "
                        "between them: half of 48 — an area of 24.",
                        '[[triangle v="A,B,C" sas="12,4,90" sides="12,,4" angles="90,," caption="½ · 12 · 4 · 1 = 24"]][[step eq="½ · 12 · 4 · 1 = 24"]]'),
             "ask": {'a': 6, 'b': 10, 'c': 90, 'op': 'arsn'}},
            {"worked": ("One more together. The same 12 and 4, but 30 degrees between "
                        "them: a quarter of 48 — 12.",
                        '[[triangle v="A,B,C" sas="12,4,30" sides="12,,4" angles="30,," caption="sin 30° = ½ — a quarter of 48 is 12"]][[step eq="¼ · 12 · 4 = 12"]]'),
             "ask": {'a': 12, 'b': 6, 'c': 150, 'op': 'arsn'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Sides 10 and 4 with "
                       "30 degrees between them cover an area of 10. Tap the reason why."),
            "choices": ("because the sine of 30 halves the half product again | because "
                        "the sine of 30 is 1 | because two sides timesed is the area"),
            "answer": "because the sine of 30 halves the half product again",
            "board": '[[triangle v="A,B,C" sas="10,4,30" sides="10,,4" angles="30,," caption="¼ · 40 = 10"]]',
        },
        "recap": [
            ("So, here it is again. Two sides and the angle between them give the "
             "area: half of one side, times the other, times the sine of the angle. The "
             "sine of 90 is 1 and the sine of 30 is a half — and 150 shares it. Never "
             "forget the half.",
             '[[triangle v="A,B,C" sas="10,4,150" sides="10,,4" angles="150,," caption="half the product, times the sine"]]'),
            ("And that is area without a height.",
             '[[step eq="area = ½ · side · side · sin(angle)"]]'),
        ],
        "bank": [
            {"a": 2, "b": 4, "c": 90, "op": "arsn"},
            {"a": 4, "b": 4, "c": 30, "op": "arsn"},
            {"a": 2, "b": 6, "c": 90, "op": "arsn"},
            {"a": 6, "b": 6, "c": 150, "op": "arsn"},
            {"a": 4, "b": 6, "c": 90, "op": "arsn"},
            {"a": 6, "b": 8, "c": 30, "op": "arsn"},
            {"a": 4, "b": 8, "c": 90, "op": "arsn"},
            {"a": 8, "b": 8, "c": 30, "op": "arsn"},
            {"a": 5, "b": 8, "c": 90, "op": "arsn"},
            {"a": 8, "b": 10, "c": 150, "op": "arsn"},
        ],
    },
    {
        "id": "pc-u6-the-thirty-degree-ramp",
        "course": "precalc", "unit": 6,
        "topic": "The 30-degree rise",
        "op": "ramp", "max_value": 40,
        "levels": ("abstract",),
        "symbols": ("ramp", "half"),
        "advance_line": "Three in a row, and you can say why — you've got it! At 30 degrees, the climb is half the length.",
        "why": [
            ("Why does a ramp climb half its length? A ramp rises at 30 degrees — how "
             "high does its far end sit? The sine of an angle is the rise divided by "
             "the slope's length, so the rise equals length times sine — and at 30 "
             "degrees that sine is a half. The ramp climbs half its length.",
             '[[goal text="The thirty-degree ramp"]][[step eq="rise = length × sin 30° = ½ × length"]]'),
        ],
        "picture": [
            ("Here is a 22-foot ramp at 30 degrees, as a right triangle. The slanted "
             "side is the ramp — that is the 22 you walk. The upright side is how high "
             "its top end sits, marked with a question mark. Look how much shorter the "
             "upright is than the slope.",
             '[[triangle v="A,B,C" right="B" sides=",?,22" angles="30,," caption="a 22-foot ramp at 30° — the upright side is the rise"]]'),
        ],
        "teach": [
            ("That is the method. A 22-foot ramp at 30 degrees: half of 22 is 11 feet "
             "up. You walk 22 along the slope and rise 11. The climb is always the "
             "smaller number — you travel farther than you rise, on every ramp ever "
             "built.",
             '[[triangle v="A,B,C" right="B" sides=",11,22" angles="30,," caption="a 22-foot ramp at 30° — 11 feet up"]][[step eq="½ · 22 = 11 ft"]]'),
            ("That is the whole trap: the length is how far you WALK, and it never "
             "doubles as the height. A 40-foot ramp rises 20 — not 40, which is the "
             "walk, and certainly not 80, which would stand higher than the ramp is "
             "long.",
             '[[step eq="40 ft ramp → 20 ft up ✓"]][[step eq="40 ✗ the walk · 80 ✗ doubled"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. A 26-foot ramp at 30 degrees: "
                        "half of 26 — it rises 13 feet.",
                        '[[triangle v="A,B,C" right="B" sides=",13,26" angles="30,," caption="½ · 26 = 13 ft"]][[step eq="½ · 26 = 13 ft"]]'),
             "ask": {'a': 32, 'b': 0, 'op': 'ramp'}},
            {"worked": ("One more together. A 30-foot ramp at the same 30 degrees: half "
                        "of 30 — it rises 15 feet.",
                        '[[triangle v="A,B,C" right="B" sides=",15,30" angles="30,," caption="½ · 30 = 15 ft"]][[step eq="½ · 30 = 15 ft"]]'),
             "ask": {'a': 36, 'b': 0, 'op': 'ramp'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A 22-foot ramp at 30 "
                       "degrees rises 11 feet. Tap the reason why."),
            "choices": ("because the sine of 30 is a half | because the rise of a ramp "
                        "equals its length | because the rise is the length doubled"),
            "answer": "because the sine of 30 is a half",
            "board": '[[triangle v="A,B,C" right="B" sides=",11,22" angles="30,," caption="half of 22 is 11"]]',
        },
        "recap": [
            ("So, here it is again. The rise is the length times the sine of the "
             "angle, and the sine of 30 degrees is a half — so a 30-degree ramp climbs "
             "half its length. The length is the walk, never the height, and never "
             "double it.",
             '[[triangle v="A,B,C" right="B" sides=",11,22" angles="30,," caption="the climb is half the length"]]'),
            ("And that is a ramp, measured without climbing it.",
             '[[step eq="rise = ½ × length"]]'),
        ],
        "bank": [
            {"a": 6, "b": 0, "op": "ramp"},
            {"a": 8, "b": 0, "op": "ramp"},
            {"a": 10, "b": 0, "op": "ramp"},
            {"a": 12, "b": 0, "op": "ramp"},
            {"a": 14, "b": 0, "op": "ramp"},
            {"a": 16, "b": 0, "op": "ramp"},
            {"a": 18, "b": 0, "op": "ramp"},
            {"a": 20, "b": 0, "op": "ramp"},
            {"a": 24, "b": 0, "op": "ramp"},
            {"a": 28, "b": 0, "op": "ramp"},
        ],
    },
    {
        "id": "pc-u6-past-the-full-turn",
        "course": "precalc", "unit": 6,
        "topic": "Bearings",
        "op": "brng", "max_value": 350,
        "levels": ("abstract",),
        "symbols": ("bearing", "clockwise"),
        "advance_line": "Three in a row, and you can say why — you've got it! Add the turn, then wrap at 360.",
        "why": [
            ("Why past the full turn? Sailors and pilots steer by a bearing: degrees "
             "measured clockwise from north, from 0 up to 360. Turn clockwise and the "
             "bearing grows — but the circle stops at 360, and a turn that passes it "
             "starts counting again from zero.",
             '[[goal text="Past the full turn"]][[step eq="bearing: 0° → 360°, clockwise from north"]]'),
        ],
        "picture": [
            ("Here is the compass. North sits at the top, and a bearing is measured "
             "clockwise from it — this ship points at 350, just short of north. The "
             "dashed arc is a 40-degree turn clockwise, and look where it ends: past "
             "north, on the other side of 360.",
             '[[unitcircle bearing="350" turn="40" caption="bearing 350° — a 40° turn clockwise carries the ship past north"]]'),
        ],
        "teach": [
            ("That is the method. A ship on bearing 350 turns 40 degrees clockwise. "
             "350 plus 40 is 390 — past the full turn. Take away 360 and the true "
             "bearing is 30: the ship has swung around through north and is heading "
             "nearly north again.",
             '[[unitcircle bearing="30" caption="350 + 40 = 390, past 360 — bearing 30°"]][[step eq="350 + 40 = 390"]] [[step eq="390 − 360 = 30"]]'),
            ("Two traps live here. Leaving 390 on the compass names a bearing no "
             "compass carries. And turning the other way — 350 take away 40 — points "
             "at 310, a heading the ship never took. Add the turn first, then wrap.",
             '[[step eq="30 ✓"]][[step eq="390 ✗ no such bearing · 310 ✗ turned the wrong way"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Bearing 245, turning 160 "
                        "clockwise: 405, past the turn — take away 360 for 45.",
                        '[[unitcircle bearing="45" caption="245 + 160 = 405 — wrapped: 45°"]][[step eq="245 + 160 = 405"]] [[step eq="405 − 360 = 45"]]'),
             "ask": {'a': 290, 'b': 125, 'op': 'brng'}},
            {"worked": ("One more together. Bearing 290, turning 150: 440, and 440 take "
                        "away 360 is 80.",
                        '[[unitcircle bearing="80" caption="290 + 150 = 440 — wrapped: 80°"]][[step eq="290 + 150 = 440"]] [[step eq="440 − 360 = 80"]]'),
             "ask": {'a': 330, 'b': 105, 'op': 'brng'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A ship on bearing 350 "
                       "turns 40 degrees clockwise and ends on bearing 30. Tap the reason "
                       "why."),
            "choices": ("because the compass wraps at 360 and starts again from zero | "
                        "because a clockwise turn is taken away from the bearing | because "
                        "a bearing can climb past 360"),
            "answer": "because the compass wraps at 360 and starts again from zero",
            "board": '[[unitcircle bearing="30" caption="390 − 360 = 30"]]',
        },
        "recap": [
            ("So, here it is again. A bearing is measured clockwise from north, 0 to "
             "360. Add a clockwise turn, and if the sum passes 360 take 360 away — "
             "the compass starts again from zero. Never leave a bearing past 360, and "
             "never turn the wrong way.",
             '[[unitcircle bearing="350" turn="40" caption="add the turn, then wrap at 360"]]'),
            ("And that is a ship swinging through north.",
             '[[step eq="350 + 40 = 390"]][[step eq="390 − 360 = 30"]]'),
        ],
        "bank": [
            {"a": 200, "b": 170, "op": "brng"},
            {"a": 210, "b": 165, "op": "brng"},
            {"a": 220, "b": 160, "op": "brng"},
            {"a": 230, "b": 155, "op": "brng"},
            {"a": 240, "b": 150, "op": "brng"},
            {"a": 250, "b": 145, "op": "brng"},
            {"a": 260, "b": 140, "op": "brng"},
            {"a": 270, "b": 135, "op": "brng"},
            {"a": 280, "b": 130, "op": "brng"},
            {"a": 300, "b": 120, "op": "brng"},
        ],
    },
    {
        "id": "pc-u6-the-arrow-and-its-steps",
        "course": "precalc", "unit": 6,
        "topic": "Vector length",
        "op": "vmag", "max_value": 40,
        "levels": ("abstract",),
        "symbols": ("arrow", "steps"),
        "advance_line": "Three in a row, and you can say why — you've got it! The arrow is the hypotenuse of its two steps.",
        "why": [
            ("Why is an arrow a hypotenuse? An arrow on a grid is described by its "
             "steps: so many to the right, so many up. Those two steps meet at a right "
             "angle — so the arrow itself is a hypotenuse, and Geometry's Pythagoras "
             "measures it without a ruler.",
             '[[goal text="The arrow and its steps"]][[step eq="arrow² = right² + up²"]]'),
        ],
        "picture": [
            ("Here is an arrow on the grid: 3 across and 4 up. Look at the corner where "
             "its two steps meet — the 3 along the bottom, the 4 straight up, "
             "and the arrow slanting across between them. The steps are the legs; the "
             "arrow is the long side.",
             '[[vector v="3,4" caption="3 across, 4 up — the arrow is the slanted side"]]'),
        ],
        "teach": [
            ("That is the method. Right 3 and up 4: 9 put together with 16 is 25, and "
             "5 times 5 squares back to it. The arrow is 5 long — farther than either "
             "step on its own, and shorter than walking 3 and then 4, which is 7.",
             '[[triangle v="A,B,C" right="B" sides="3,4,5" caption="the two steps and the arrow: 3, 4, 5"]][[step eq="3² + 4² = 25"]] [[step eq="√25 = 5"]][[step eq="5 > 4 · 5 < 3 + 4"]]'),
            ("Those two bounds catch both traps. An arrow is never as long as its "
             "steps added, and never as short as its biggest step alone. Right 5 and "
             "up 12 gives 13 — not 17, and not 12.",
             '[[vector v="5,12" caption="5 across, 12 up — the arrow is 13"]][[step eq="13 ✓ · 17 ✗ added · 12 ✗ the big step alone"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Right 9 and up 40: 81 put "
                        "together with 1600 is 1681, and 41 squares back to it. The arrow "
                        "is 41.",
                        '[[vector v="9,40" caption="right 9, up 40 — the arrow is 41"]][[step eq="9² + 40² = 1681"]] [[step eq="√1681 = 41"]]'),
             "ask": {'a': 12, 'b': 35, 'c': 37, 'op': 'vmag'}},
            {"worked": ("One more together. Right 30 and up 40: the arrow is 50, the old "
                        "3-4-5 grown ten times.",
                        '[[vector v="30,40" caption="right 30, up 40 — the arrow is 50"]][[step eq="30² + 40² = 2500"]] [[step eq="√2500 = 50"]]'),
             "ask": {'a': 24, 'b': 32, 'c': 40, 'op': 'vmag'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. An arrow that goes 3 "
                       "right and 4 up is 5 long. Tap the reason why."),
            "choices": ("because the steps meet at a right angle | because an arrow is as "
                        "long as its two steps added | because an arrow is as long as its "
                        "bigger step"),
            "answer": "because the steps meet at a right angle",
            "board": '[[vector v="3,4" caption="3 across, 4 up — 5 long"]]',
        },
        "recap": [
            ("So, here it is again. An arrow's two steps meet at a right angle, so the "
             "arrow is the hypotenuse: square the steps, put them together, and "
             "un-square. It is longer than either step and shorter than both added — "
             "never the sum, never the big step alone.",
             '[[vector v="3,4" caption="the arrow is the hypotenuse of its two steps"]]'),
            ("And that is Pythagoras, wearing vector clothes.",
             '[[step eq="3² + 4² = 25"]][[step eq="√25 = 5"]]'),
        ],
        "bank": [
            {"a": 6, "b": 8, "c": 10, "op": "vmag"},
            {"a": 9, "b": 12, "c": 15, "op": "vmag"},
            {"a": 8, "b": 15, "c": 17, "op": "vmag"},
            {"a": 12, "b": 16, "c": 20, "op": "vmag"},
            {"a": 7, "b": 24, "c": 25, "op": "vmag"},
            {"a": 15, "b": 20, "c": 25, "op": "vmag"},
            {"a": 10, "b": 24, "c": 26, "op": "vmag"},
            {"a": 20, "b": 21, "c": 29, "op": "vmag"},
            {"a": 18, "b": 24, "c": 30, "op": "vmag"},
            {"a": 16, "b": 30, "c": 34, "op": "vmag"},
        ],
    },
]
LESSONS.extend(_PRECALC_U6)

# =============================================================================
# PRE-CALC UNIT 7 -- Conic Sections & Parametric Equations (build lo)
# The thread: a shape's EQUATION hands over its measurements, if you read the
# squares right. Un-square the circle's right-hand number for the radius, read
# the center out of the take-aways (the sign points opposite -- vtx2's and
# fdom's rule, third home), un-square and DOUBLE for an ellipse's width, and
# tie both coordinates to time so a curve becomes a path something travels.
# The [[conic]] renderer draws on a labeled grid, so it is TEACH-ONLY here.
# =============================================================================
_PRECALC_U7 = [
    {
        "id": "pc-u7-un-square-the-radius",
        "course": "precalc", "unit": 7,
        "topic": "Circle equations",
        "op": "crad", "max_value": 12,
        "levels": ("abstract",),
        "symbols": ("radius", "circle"),
        "advance_line": "Three in a row, and you can say why — you've got it! Un-square the right-hand number.",
        "why": [
            ("Why un-square? Unit Seven reads shapes straight off their equations. A "
             "circle can be written: x take away 2, squared, plus y take away 9, "
             "squared, equals 225 — every point sitting one fixed distance from the "
             "middle. That 225 is not the radius, though.",
             '[[goal text="Un-square the radius"]][[step eq="(x − 2)² + (y − 9)² = 225"]]'),
        ],
        "picture": [
            ("Here is the circle with its radius drawn from the middle to the edge, "
             "and a question mark on it. The equation's right-hand number is 225, and "
             "no circle on this board reaches 225 across — that number is hiding the "
             "radius inside a square.",
             '[[circle center="O" r="?" caption="the radius, middle to edge — the equation says 225, and 225 is not it"]]'),
        ],
        "teach": [
            ("That is the method: the right-hand number is the radius SQUARED. "
             "Un-square 225 and the radius is 15 — the circle reaches 15 in every "
             "direction from its middle. The distance formula built this equation, and "
             "distances arrive squared; un-squaring gets them back.",
             '[[conic type="circle" r="15" cx="2" cy="9" caption="the circle reaches 15 every way — radius 15"]][[step eq="un-square 225 = 15"]][[step eq="radius = 15"]]'),
            ("Two grabs to resist: answering 225, which is still squared; and "
             "answering 2 or 9, which say WHERE the circle sits and nothing about its "
             "size. Un-square the right-hand number — that is the radius, every time.",
             '[[step eq="15 ✓"]][[step eq="225 ✗ still squared · 2 ✗ the center"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. x take away 5, squared, plus y "
                        "take away 5, squared, equals 169: un-square 169 — the radius is "
                        "13.",
                        '[[conic type="circle" r="13" cx="5" cy="5" caption="un-square 169 — radius 13"]][[step eq="= 169"]] [[step eq="radius = 13"]]'),
             "ask": {'a': 8, 'b': 3, 'c': 12, 'op': 'crad'}},
            {"worked": ("One more together. That same shape ending in 196: un-square 196 "
                        "— the radius is 14.",
                        '[[circle center="O" r="14" caption="un-square 196 — radius 14"]][[step eq="= 196"]] [[step eq="radius = 14"]]'),
             "ask": {'a': 6, 'b': 11, 'c': 10, 'op': 'crad'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. The circle written "
                       "with 225 on the right has a radius of 15. Tap the reason why."),
            "choices": ("because the right-hand number is the radius squared | because the "
                        "right-hand number is the radius itself | because the radius is "
                        "the number inside the parentheses"),
            "answer": "because the right-hand number is the radius squared",
            "board": '[[conic type="circle" r="15" cx="2" cy="9" caption="radius 15"]]',
        },
        "recap": [
            ("So, here it is again. A circle's equation ends in the radius SQUARED, "
             "because distances arrive squared. Un-square the right-hand number and "
             "that is the radius. Never hand back the squared number, and never grab "
             "a center number.",
             '[[circle center="O" r="15" caption="un-square the right-hand number"]]'),
            ("And that is a shape read straight off its equation.",
             '[[step eq="(x − 2)² + (y − 9)² = 225"]][[step eq="radius = 15"]]'),
        ],
        "bank": [
            {"a": 3, "b": 5, "c": 2, "op": "crad"},
            {"a": 5, "b": 2, "c": 3, "op": "crad"},
            {"a": 2, "b": 7, "c": 4, "op": "crad"},
            {"a": 7, "b": 3, "c": 5, "op": "crad"},
            {"a": 4, "b": 9, "c": 6, "op": "crad"},
            {"a": 9, "b": 4, "c": 7, "op": "crad"},
            {"a": 3, "b": 11, "c": 8, "op": "crad"},
            {"a": 11, "b": 6, "c": 9, "op": "crad"},
            {"a": 6, "b": 12, "c": 10, "op": "crad"},
            {"a": 12, "b": 7, "c": 11, "op": "crad"},
        ],
    },
    {
        "id": "pc-u7-where-the-circle-sits",
        "course": "precalc", "unit": 7,
        "topic": "The center",
        "op": "cctr", "max_value": 12, "min_value": -12,
        "levels": ("abstract",),
        "symbols": ("center", "opposite"),
        "advance_line": "Three in a row, and you can say why — you've got it! Take away 15 means the center sits at positive 15.",
        "why": [
            ("Why does the sign flip? Same equation, a different question: where is "
             "the middle? Write a circle as: x take away 15, squared, plus y take away "
             "2, squared, equals 25. The center hides inside the two take-aways — and "
             "it hides with its sign flipped.",
             '[[goal text="Where the circle sits"]][[step eq="(x − 15)² + (y − 2)² = 25"]]'),
        ],
        "picture": [
            ("Here is the circle with its middle marked by a question mark. The "
             "equation names that middle, but not the way your eye reads it: the "
             "number after each take-away is where the circle sits, once you flip the "
             "sign the equation shows.",
             '[[circle center="?" caption="the middle — the take-aways know where it sits, with the sign flipped"]]'),
        ],
        "teach": [
            ("That is the method. x take away 15 goes quiet at x equals 15, and the "
             "middle sits exactly where those squared pieces go quiet. So the center's "
             "x is 15 — positive 15, even though a minus sign is what your eye reads "
             "on the page.",
             '[[conic type="circle" r="5" cx="15" cy="2" caption="the middle sits at (15, 2) — center x = 15"]][[step eq="x − 15 = 0 at x = 15"]] [[step eq="center x = 15"]]'),
            ("Inside the parentheses, a sign always points opposite — the rule the "
             "parabola\'s turn obeyed, and the doorway before that. Take away 15 "
             "means positive 15, never negative 15. And the 2 is the OTHER "
             "coordinate: answer the one you were asked for.",
             '[[step eq="15 ✓"]][[step eq="−15 ✗ the flip · 2 ✗ the y"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. x take away 14, squared, plus y "
                        "take away 1, squared, equals 16: the center\'s x is 14.",
                        '[[conic type="circle" r="4" cx="14" cy="1" caption="the middle sits at (14, 1)"]][[step eq="(x − 14)² · center x = 14"]]'),
             "ask": {'a': 12, 'b': 7, 'c': 5, 'op': 'cctr'}},
            {"worked": ("One more together. x take away 13, squared, plus y take away 6, "
                        "squared: the center\'s x is 13.",
                        '[[conic type="circle" r="4" cx="13" cy="6" caption="the middle sits at (13, 6)"]][[step eq="(x − 13)² · center x = 13"]]'),
             "ask": {'a': 7, 'b': 11, 'c': 8, 'op': 'cctr'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. The circle written "
                       "with x take away 15 has its center at x equals 15. Tap the reason "
                       "why."),
            "choices": ("because x take away 15 goes quiet exactly at 15 | because the "
                        "minus sign means the center is negative | because the center is "
                        "the number on the right"),
            "answer": "because x take away 15 goes quiet exactly at 15",
            "board": '[[conic type="circle" r="5" cx="15" cy="2" caption="center x = 15"]]',
        },
        "recap": [
            ("So, here it is again. The center hides in the take-aways with its sign "
             "flipped: x take away 15 means the middle sits at positive 15, where that "
             "squared piece goes quiet. Never flip it the wrong way, and never answer "
             "the other coordinate.",
             '[[circle center="?" caption="the sign inside points opposite"]]'),
            ("And that is where the circle sits.",
             '[[step eq="(x − 15)² + (y − 2)² = 25"]][[step eq="center x = 15"]]'),
        ],
        "bank": [
            {"a": 2, "b": 5, "c": 3, "op": "cctr"},
            {"a": 3, "b": 7, "c": 4, "op": "cctr"},
            {"a": 4, "b": 9, "c": 2, "op": "cctr"},
            {"a": 5, "b": 2, "c": 6, "op": "cctr"},
            {"a": 6, "b": 11, "c": 3, "op": "cctr"},
            {"a": 7, "b": 4, "c": 5, "op": "cctr"},
            {"a": 8, "b": 3, "c": 7, "op": "cctr"},
            {"a": 9, "b": 12, "c": 4, "op": "cctr"},
            {"a": 10, "b": 6, "c": 8, "op": "cctr"},
            {"a": 11, "b": 5, "c": 9, "op": "cctr"},
        ],
    },
    {
        "id": "pc-u7-edge-to-edge",
        "course": "precalc", "unit": 7,
        "topic": "Ellipses",
        "op": "elax", "max_value": 20,
        "levels": ("abstract",),
        "symbols": ("ellipse", "edge"),
        "advance_line": "Three in a row, and you can say why — you've got it! Un-square, then double.",
        "why": [
            ("Why double? Stretch a circle and you have an ellipse: x squared over "
             "144, plus y squared over 25, equals 1. Those two bottom numbers are "
             "squares as well — and un-squaring them says how far the shape reaches "
             "in each direction from its middle, not edge to edge.",
             '[[goal text="Edge to edge"]][[step eq="x²/144 + y²/25 = 1"]]'),
        ],
        "picture": [
            ("Here is the ellipse on the grid, wider than it is tall. Its middle "
             "splits the width into two equal reaches, one to the left and one to the "
             "right. The number under x squared is ONE reach, squared — so the whole "
             "width is two of them.",
             '[[conic type="ellipse" a="12" b="5" caption="the middle splits the width into two equal reaches"]]'),
        ],
        "teach": [
            ("That is the method: un-square, then double. Un-square 144: the ellipse "
             "reaches 12 to the left and 12 to the right of its middle. From the left "
             "edge to the right edge is double that — 24 across. The 25 does the same "
             "work upward: 5 each way, so 10 tall.",
             '[[tape parts="12|12" total="24" caption="two reaches of 12 — 24 across"]][[step eq="un-square 144 = 12 each way"]][[step eq="12 + 12 = 24 across"]]'),
            ("Two half-answers wait here. 12 is the reach ONE way, not the full "
             "width; and 144 is the printed number, still squared. Un-square, then "
             "double — and the answer is always the widest measurement the shape has.",
             '[[step eq="24 ✓"]][[step eq="12 ✗ half of it · 144 ✗ still squared"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. x squared over 121, plus y "
                        "squared over 16: un-square 121 — 11 each way, so 22 across.",
                        '[[tape parts="11|11" total="22" caption="121 → 11 each way → 22 across"]][[step eq="un-square 121 = 11 each way"]][[step eq="22 across"]]'),
             "ask": {'a': 7, 'b': 5, 'op': 'elax'}},
            {"worked": ("One more together. x squared over 196: 14 each way, so 28 "
                        "across.",
                        '[[conic type="ellipse" a="14" b="6" caption="14 each way — 28 across"]][[step eq="un-square 196 = 14 each way"]][[step eq="28 across"]]'),
             "ask": {'a': 9, 'b': 8, 'op': 'elax'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. The ellipse with 144 "
                       "under x squared is 24 across. Tap the reason why."),
            "choices": ("because 144 un-squares to one reach of 12, and there are two | "
                        "because 144 un-squares to the whole width | because the width "
                        "is the printed number itself"),
            "answer": "because 144 un-squares to one reach of 12, and there are two",
            "board": '[[tape parts="12|12" total="24" caption="un-square, then double"]]',
        },
        "recap": [
            ("So, here it is again. The number under x squared is one reach, "
             "squared: un-square it for the reach from the middle, then double it for "
             "edge to edge. Never stop at one reach, and never hand back the printed "
             "square.",
             '[[conic type="ellipse" a="12" b="5" caption="un-square, then double"]]'),
            ("And that is a stretched circle, measured.",
             '[[step eq="un-square 144 = 12 each way"]][[step eq="24 across"]]'),
        ],
        "bank": [
            {"a": 3, "b": 2, "op": "elax"},
            {"a": 4, "b": 3, "op": "elax"},
            {"a": 5, "b": 2, "op": "elax"},
            {"a": 5, "b": 4, "op": "elax"},
            {"a": 6, "b": 5, "op": "elax"},
            {"a": 7, "b": 3, "op": "elax"},
            {"a": 8, "b": 5, "op": "elax"},
            {"a": 8, "b": 7, "op": "elax"},
            {"a": 9, "b": 4, "op": "elax"},
            {"a": 10, "b": 6, "op": "elax"},
        ],
    },
    {
        "id": "pc-u7-where-you-are-at-time-t",
        "course": "precalc", "unit": 7,
        "topic": "Parametric equations",
        "op": "parm", "max_value": 40,
        "levels": ("abstract",),
        "symbols": ("time", "path"),
        "advance_line": "Three in a row, and you can say why — you've got it! Plug the time in first, then measure straight.",
        "why": [
            ("Why tie a curve to time? The unit ends in motion. Instead of tying y to "
             "x, tie BOTH of them to time: x equals 3 times t, y equals 4 times t. Hand "
             "it a moment and it hands back a position, so the curve becomes a path "
             "something travels.",
             '[[goal text="Where you are at time t"]][[step eq="x = 3t · y = 4t"]]'),
        ],
        "picture": [
            ("Here is the path on the grid: a straight line out of the corner. At t "
             "equals 1 second the ball sits at 3 across and 4 up — the point marked. "
             "Every second after that, it slides farther along the same line, the "
             "same distance again.",
             '[[graph lines="y=1.33333x" names="the path" points="(3,4)" range="0..12" caption="the path — at t = 1 the ball is at (3, 4)"]]'),
        ],
        "teach": [
            ("That is the method. At t equals 1 second the ball sits 3 right and 4 up "
             "— 5 away from its start, by Pythagoras. At t equals 10 seconds it is at "
             "30 and 40, which is 50 away. Every second adds another 5 of distance.",
             '[[vector v="30,40" caption="t = 10: (30, 40) — 50 from the start"]][[step eq="t = 1: point (3, 4), 5 away"]][[step eq="t = 10: point (30, 40), 50 away"]]'),
            ("So two answers tempt at 10 seconds. 5 is one second\'s worth — that is "
             "the speed, not the trip. And 30 plus 40 walks the corner instead of "
             "cutting across. Plug the time in first, then measure straight.",
             '[[step eq="50 ✓"]][[step eq="5 ✗ one second · 70 ✗ walked the corner"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. x equals 20 t, y equals 21 t. At 2 "
                        "seconds: 40 and 42, and the straight distance is 58.",
                        '[[vector v="40,42" caption="t = 2: (40, 42) — 58 from the start"]][[step eq="t = 2: point (40, 42), 58"]]'),
             "ask": {'a': 5, 'b': 12, 'c': 3, 'op': 'parm'}},
            {"worked": ("One more together. x equals 7 t, y equals 24 t. At 2 seconds: 14 "
                        "and 48 — 50 away.",
                        '[[vector v="14,48" caption="t = 2: (14, 48) — 50 from the start"]][[step eq="t = 2: point (14, 48), 50"]]'),
             "ask": {'a': 6, 'b': 8, 'c': 4, 'op': 'parm'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. On the path x equals "
                       "3 t, y equals 4 t, the ball is 50 away at 10 seconds. Tap the "
                       "reason why."),
            "choices": ("because legs of 30 and 40 give an arrow of 50 | because the ball "
                        "moves 5 in all | because 30 and 40 added is the distance"),
            "answer": "because legs of 30 and 40 give an arrow of 50",
            "board": '[[vector v="30,40" caption="plug the time in, then measure straight"]]',
        },
        "recap": [
            ("So, here it is again. A path tied to time hands back a position for "
             "every moment: plug the time into both rules for the two legs, then "
             "measure straight across with Pythagoras. Never stop at one second\'s "
             "worth, and never walk the corner.",
             '[[graph lines="y=1.33333x" names="the path" points="(3,4)" range="0..12" caption="plug the time in first, then measure straight"]]'),
            ("And that is a curve something travels.",
             '[[step eq="t = 10: (30, 40)"]][[step eq="√(30² + 40²) = 50"]]'),
        ],
        "bank": [
            {"a": 3, "b": 4, "c": 2, "op": "parm"},
            {"a": 3, "b": 4, "c": 3, "op": "parm"},
            {"a": 3, "b": 4, "c": 4, "op": "parm"},
            {"a": 6, "b": 8, "c": 2, "op": "parm"},
            {"a": 3, "b": 4, "c": 5, "op": "parm"},
            {"a": 5, "b": 12, "c": 2, "op": "parm"},
            {"a": 9, "b": 12, "c": 2, "op": "parm"},
            {"a": 6, "b": 8, "c": 3, "op": "parm"},
            {"a": 8, "b": 15, "c": 2, "op": "parm"},
            {"a": 12, "b": 16, "c": 2, "op": "parm"},
        ],
    },
]
LESSONS.extend(_PRECALC_U7)
# =============================================================================
# PRE-CALC UNIT 8 -- Sequences, Series & the Binomial Theorem (build lp)
# The thread: ADD THE WHOLE PATTERN UP, not just look at its last term. The
# finite geometric sum, sigma read as an instruction (gaus's bare sum, now
# carrying a multiplier), choosing when order does not matter, and -- the
# hinge into Unit 9 -- an INFINITE sum that still settles on a finite number.
# =============================================================================
_PRECALC_U8 = [
    {
        "id": "pc-u8-add-the-whole-run",
        "course": "precalc", "unit": 8,
        "topic": "Geometric sums",
        "op": "gsum", "max_value": 100,
        "levels": ("abstract",),
        "symbols": ("sum", "terms"),
        "advance_line": "Three in a row, and you can say why — you've got it! The sum is the whole run, not the last term.",
        "why": [
            ("Why add the whole run? Algebra Two rode a pattern to its nth term. Unit "
             "Eight adds the whole run up instead. A pattern starting at 1 and "
             "doubling gives 1, 2, 4, 8 — and their sum is 15, a number no single term "
             "ever equals.",
             '[[goal text="Add the whole run"]][[step eq="1 + 2 + 4 + 8 = 15"]]'),
        ],
        "picture": [
            ("Here are the terms as bars: 1, 2, 4, 8, each one double the last. The "
             "sum is not the tallest bar — it is every bar stacked together. Look at "
             "how much the whole pile outweighs the biggest single piece.",
             '[[bars data="term 1:1 | term 2:2 | term 3:4 | term 4:8" caption="1 + 2 + 4 + 8 = 15 — the whole run, not the last term"]]'),
        ],
        "teach": [
            ("That is the method: write the terms out as they stand, then add. Look "
             "at what happened: 15 is one short of 16, the NEXT double. Doubling sums "
             "always land one short of the next term — 1, 2, 4, 8, 16 sums to 31. The "
             "whole run adds up to a little less than double its biggest piece.",
             '[[bars data="1:1 | 2:2 | 4:4 | 8:8 | 16:16" caption="1 + 2 + 4 + 8 + 16 = 31 — one short of 32"]][[step eq="1+2+4+8+16 = 31 — one short of 32"]]'),
            ("Two traps. The last term alone — 8 in that first run — is the biggest "
             "piece, never the sum. And counting the start over and over, four 1s for "
             "4, is what a pattern that never grew would give. Add the terms as they "
             "actually stand.",
             '[[step eq="15 ✓"]][[step eq="8 ✗ the last term · 4 ✗ never grew"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Start at 4, doubling, four terms: "
                        "4, 8, 16, 32 — put together, 60.",
                        '[[bars data="term 1:4 | term 2:8 | term 3:16 | term 4:32" caption="4 + 8 + 16 + 32 = 60"]][[step eq="4 + 8 + 16 + 32 = 60"]]'),
             "ask": {'a': 2, 'b': 2, 'c': 5, 'op': 'gsum'}},
            {"worked": ("One more together. Start at 2, times 3 each step, four terms: 2, "
                        "6, 18, 54 — 80 in all.",
                        '[[bars data="term 1:2 | term 2:6 | term 3:18 | term 4:54" caption="2 + 6 + 18 + 54 = 80"]][[step eq="2 + 6 + 18 + 54 = 80"]]'),
             "ask": {'a': 5, 'b': 2, 'c': 4, 'op': 'gsum'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Starting at 1 and "
                       "doubling, four terms sum to 15. Tap the reason why."),
            "choices": ("because the sum is every term stacked together, not the last one "
                        "| because the sum is the biggest term | because the start counted "
                        "four times is the sum"),
            "answer": "because the sum is every term stacked together, not the last one",
            "board": '[[bars data="term 1:1 | term 2:2 | term 3:4 | term 4:8" caption="every term stacked together"]]',
        },
        "recap": [
            ("So, here it is again. To sum a pattern, write the terms out as they "
             "stand and add every one — the whole run, which is more than the last "
             "term and far more than the start repeated. A doubling run lands one "
             "short of the next double.",
             '[[bars data="term 1:1 | term 2:2 | term 3:4 | term 4:8" caption="add the whole run"]]'),
            ("And that is a pattern, added up.",
             '[[step eq="1 + 2 + 4 + 8 = 15"]]'),
        ],
        "bank": [
            {"a": 2, "b": 2, "c": 3, "op": "gsum"},
            {"a": 3, "b": 2, "c": 3, "op": "gsum"},
            {"a": 2, "b": 3, "c": 3, "op": "gsum"},
            {"a": 4, "b": 2, "c": 3, "op": "gsum"},
            {"a": 2, "b": 2, "c": 4, "op": "gsum"},
            {"a": 5, "b": 2, "c": 3, "op": "gsum"},
            {"a": 3, "b": 3, "c": 3, "op": "gsum"},
            {"a": 6, "b": 2, "c": 3, "op": "gsum"},
            {"a": 3, "b": 2, "c": 4, "op": "gsum"},
            {"a": 4, "b": 3, "c": 3, "op": "gsum"},
        ],
    },
    {
        "id": "pc-u8-the-instruction-called-sigma",
        "course": "precalc", "unit": 8,
        "topic": "Sigma notation",
        "op": "sigm", "max_value": 200,
        "levels": ("abstract",),
        "symbols": ("sigma", "instruction"),
        "advance_line": "Three in a row, and you can say why — you've got it! Pull the multiplier out, then sum 1 up to n.",
        "why": [
            ("Why a big Greek S? Mathematics writes long sums in shorthand: sigma, with "
             "a start below it and a stop above. It is not a new idea, only an "
             "instruction: run k from the bottom number to the top one, work out the "
             "recipe each time, and put every result together.",
             '[[goal text="The instruction called sigma"]][[step eq="Σ (k from 1 to 5) of k = 1+2+3+4+5 = 15"]]'),
        ],
        "picture": [
            ("Here is the recipe as a machine: k goes in, 10 times k comes out. Run "
             "it five times, once for each k from 1 to 5, and the outputs are 10, 20, "
             "30, 40, 50 — those five bars. Sigma says: put all of them together.",
             '[[machine input="k" rule="10k" output="?" caption="the recipe — k goes in, 10 times k comes out, five times over"]][[bars data="k=1:10 | k=2:20 | k=3:30 | k=4:40 | k=5:50" caption="the five outputs — sigma adds them all"]]'),
        ],
        "teach": [
            ("That is the method. The sum, for k from 1 to 5, of 10 times k: that is "
             "10, 20, 30, 40, 50 — and every term carries the 10, so pull it out front. "
             "1 up to 5 sums to 15, and 10 times 15 is 150.",
             '[[bars data="k=1:10 | k=2:20 | k=3:30 | k=4:40 | k=5:50" caption="10 × (1 + 2 + 3 + 4 + 5) = 10 × 15 = 150"]][[step eq="1 + 2 + 3 + 4 + 5 = 15"]][[step eq="10 × 15 = 150"]]'),
            ("The two slips are opposite. Dropping the multiplier answers 15 — "
             "Gauss\'s bare sum, the right shape but the wrong size. And answering 50 "
             "gives the LAST term only, the biggest single piece. Sum first, then times "
             "the multiplier.",
             '[[step eq="150 ✓"]][[step eq="15 ✗ multiplier dropped · 50 ✗ last term"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. The sum, k from 1 to 11, of 2 "
                        "times k: 1 up to 11 is 66, and 2 times 66 is 132.",
                        '[[bars data="k=1:2 | k=2:4 | k=3:6 | k=4:8 | k=5:10 | k=6:12 | k=7:14 | k=8:16 | k=9:18 | k=10:20 | k=11:22" caption="2 × 66 = 132"]][[step eq="1 + 2 + … + 11 = 66"]][[step eq="2 × 66 = 132"]]'),
             "ask": {'a': 6, 'b': 7, 'op': 'sigm'}},
            {"worked": ("One more together. k from 1 to 4, of 9 times k: 1 up to 4 is 10, "
                        "and 9 times 10 is 90.",
                        '[[bars data="k=1:9 | k=2:18 | k=3:27 | k=4:36" caption="9 × 10 = 90"]][[step eq="1 + 2 + 3 + 4 = 10"]][[step eq="9 × 10 = 90"]]'),
             "ask": {'a': 5, 'b': 8, 'op': 'sigm'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. The sum, for k from 1 "
                       "to 5, of 10 times k is 150. Tap the reason why."),
            "choices": ("because every term carries the 10, so it multiplies the bare sum "
                        "| because sigma means take the last term | because the multiplier "
                        "is added on at the end"),
            "answer": "because every term carries the 10, so it multiplies the bare sum",
            "board": '[[bars data="k=1:10 | k=2:20 | k=3:30 | k=4:40 | k=5:50" caption="10 × 15 = 150"]]',
        },
        "recap": [
            ("So, here it is again. Sigma is an instruction: run k from the bottom to "
             "the top, work the recipe each time, add every result. When every term "
             "carries the same multiplier, pull it out front and times the bare sum. "
             "Never drop it, and never stop at the last term.",
             '[[machine input="k" rule="10k" output="?" caption="the instruction called sigma"]]'),
            ("And that is a long sum, written short.",
             '[[step eq="Σ (k from 1 to 5) of 10k = 10 × 15 = 150"]]'),
        ],
        "bank": [
            {"a": 2, "b": 4, "op": "sigm"},
            {"a": 2, "b": 5, "op": "sigm"},
            {"a": 3, "b": 4, "op": "sigm"},
            {"a": 2, "b": 6, "op": "sigm"},
            {"a": 4, "b": 5, "op": "sigm"},
            {"a": 3, "b": 7, "op": "sigm"},
            {"a": 5, "b": 6, "op": "sigm"},
            {"a": 4, "b": 8, "op": "sigm"},
            {"a": 2, "b": 12, "op": "sigm"},
            {"a": 3, "b": 10, "op": "sigm"},
        ],
    },
    {
        "id": "pc-u8-when-order-does-not-matter",
        "course": "precalc", "unit": 8,
        "topic": "Choosing a team",
        "op": "pasc", "max_value": 100,
        "levels": ("abstract",),
        "symbols": ("order", "teams"),
        "advance_line": "Three in a row, and you can say why — you've got it! Count the line-ups, then divide the orders away.",
        "why": [
            ("Why divide the orders away? Algebra Two counted outfits by timesing the "
             "slots — and there, order mattered: shirt, then pants, then hat. Choosing "
             "a team is different. Ana and Ben is the same team as Ben and Ana, so "
             "counting line-ups counts every team more than once.",
             '[[goal text="When order does not matter"]][[step eq="Ana & Ben = Ben & Ana — one team"]]'),
        ],
        "picture": [
            ("Here are 3 people in a row, and we choose 2 of them. Count the "
             "line-ups first — 3 choices for the first pick, 2 left for the second. "
             "Then look at the bars: 6 line-ups, but only 3 teams, because every team "
             "was counted once per order.",
             '[[array rows="1" cols="3" caption="3 people — choose 2"]][[bars data="line-ups:6 | teams:3" caption="6 line-ups ÷ 2 orders = 3 teams"]]'),
        ],
        "teach": [
            ("That is the method. Choose 2 from 3 people. Line-ups: 3 choices, then 2 "
             "left — 6. But each team of 2 appears twice in that list, once per order. "
             "Divide by 2: three teams. Count the line-ups, then divide the orders "
             "away.",
             '[[bars data="line-ups:6 | teams:3" caption="3 × 2 = 6 line-ups ÷ 2 = 3 teams"]][[step eq="3 × 2 = 6 line-ups"]][[step eq="6 ÷ 2 orders = 3 teams"]]'),
            ("Teams of 3 hide more repeats: 3 people can stand in 6 different orders, "
             "so divide by 6. Choosing 3 from 10 gives 10 times 9 times 8 — 720 "
             "line-ups — and 720 divided by 6 is 120 teams. The bigger the team, the "
             "more orders to divide away.",
             '[[bars data="line-ups:720 | teams:120" caption="720 ÷ 6 = 120 teams"]][[step eq="10 × 9 × 8 = 720"]][[step eq="720 ÷ 6 = 120 teams"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Choose 2 from 11: 11 times 10 is "
                        "110 line-ups, halved — 55 teams.",
                        '[[bars data="line-ups:110 | teams:55" caption="110 ÷ 2 = 55 teams"]][[step eq="110 ÷ 2 = 55 teams"]]'),
             "ask": {'a': 8, 'b': 3, 'op': 'pasc'}},
            {"worked": ("One more together. Choose 3 from 11: 990 line-ups, divided by 6 — "
                        "165 teams.",
                        '[[bars data="line-ups:990 | teams:165" caption="990 ÷ 6 = 165 teams"]][[step eq="990 ÷ 6 = 165 teams"]]'),
             "ask": {'a': 9, 'b': 3, 'op': 'pasc'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Choosing 2 from 3 "
                       "people gives 3 teams, not 6. Tap the reason why."),
            "choices": ("because every team was counted once per order, so divide them "
                        "away | because a team is the same as a line-up | because the "
                        "number of teams is the number of people"),
            "answer": "because every team was counted once per order, so divide them away",
            "board": '[[bars data="line-ups:6 | teams:3" caption="6 ÷ 2 = 3 teams"]]',
        },
        "recap": [
            ("So, here it is again. When order does not matter, count the line-ups "
             "first, then divide by the number of orders a team can stand in — 2 for "
             "a pair, 6 for a trio. Never hand back the line-ups, and never hand back "
             "the crowd.",
             '[[array rows="1" cols="3" caption="count the line-ups, then divide the orders away"]]'),
            ("And that is choosing, not lining up.",
             '[[step eq="6 line-ups ÷ 2 orders = 3 teams"]]'),
        ],
        "bank": [
            {"a": 4, "b": 2, "op": "pasc"},
            {"a": 5, "b": 2, "op": "pasc"},
            {"a": 5, "b": 3, "op": "pasc"},
            {"a": 6, "b": 2, "op": "pasc"},
            {"a": 6, "b": 3, "op": "pasc"},
            {"a": 7, "b": 2, "op": "pasc"},
            {"a": 8, "b": 2, "op": "pasc"},
            {"a": 7, "b": 3, "op": "pasc"},
            {"a": 9, "b": 2, "op": "pasc"},
            {"a": 10, "b": 2, "op": "pasc"},
        ],
    },
    {
        "id": "pc-u8-the-sum-that-never-ends",
        "course": "precalc", "unit": 8,
        "topic": "Infinite series",
        "op": "gser", "max_value": 120,
        "levels": ("abstract",),
        "symbols": ("forever", "settles"),
        "advance_line": "Three in a row, and you can say why — you've got it! Halving forever settles at twice the first piece.",
        "why": [
            ("Why can a sum that never ends have an answer? Here is the strangest true "
             "thing in Unit Eight. Add 1, then a half, then a quarter, then an eighth "
             "— forever, with no last term. The running total climbs to 1, then one "
             "and a half, then one and three quarters, and never once passes 2.",
             '[[goal text="The sum that never ends"]][[step eq="1 + ½ + ¼ + ⅛ + … → 2"]]'),
        ],
        "picture": [
            ("Here is the journey on a number line, heading for 2. The first hop is "
             "1; the second hop is a half; the third a quarter. Each hop covers half of "
             "what is left to the 2, so there is always a little gap — and the gap "
             "always shrinks.",
             '[[numberline min="0" max="2" hops="0,1,1.5,1.75,1.875" points="2" caption="each hop covers half of what is left — the whole trip settles on 2"]]'),
        ],
        "teach": [
            ("That is the method: halving forever settles on twice the first piece. "
             "Begin at 64 and the endless sum settles on 128: 64, then 32, then 16, on "
             "and on. The whole trip closes in on 128 without ever arriving — a first "
             "taste of the idea Unit Nine is built from.",
             '[[numberline min="0" max="128" hops="0,64,96,112,120" points="128" caption="64 + 32 + 16 + … settles on 128 — twice the first piece"]][[step eq="64 + 32 + 16 + … → 128"]]'),
            ("So 64 alone is the first piece, 32 is the second, and only 128 is the "
             "whole endless journey. Never answer a single piece when the question "
             "asked for the whole trip.",
             '[[step eq="128 ✓"]][[step eq="64 ✗ first piece · 32 ✗ second"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. A first bounce of 52 feet, halving "
                        "forever: the whole trip is twice 52 — 104 feet.",
                        '[[numberline min="0" max="104" hops="0,52,78,91,97.5" points="104" caption="52 + 26 + 13 + … settles on 104"]][[step eq="52 + 26 + 13 + … → 104"]]'),
             "ask": {'a': 48, 'b': 0, 'op': 'gser'}},
            {"worked": ("One more together. A first bounce of 60 feet, halving forever: "
                        "twice 60 — 120 feet in all.",
                        '[[bars data="1st bounce:60 | 2nd:30 | 3rd:15" caption="60 + 30 + 15 + … settles on 120"]][[step eq="60 + 30 + 15 + … → 120"]]'),
             "ask": {'a': 56, 'b': 0, 'op': 'gser'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Halving forever from "
                       "64 settles on 128. Tap the reason why."),
            "choices": ("because each hop covers half of what is left | because the sum "
                        "stops at the first piece | because adding forever grows without "
                        "end"),
            "answer": "because each hop covers half of what is left",
            "board": '[[numberline min="0" max="128" hops="0,64,96,112,120" points="128" caption="settles on 128"]]',
        },
        "recap": [
            ("So, here it is again. An endless halving sum still settles: each hop "
             "covers half of what is left, the gap shrinks forever, and the whole "
             "trip closes in on twice the first piece. Never answer the first piece or the "
             "second — the question asked for the whole trip.",
             '[[numberline min="0" max="2" hops="0,1,1.5,1.75,1.875" points="2" caption="halving forever settles at twice the first piece"]]'),
            ("And that is a sum with no last term and one answer.",
             '[[step eq="64 + 32 + 16 + … → 128"]]'),
        ],
        "bank": [
            {"a": 8, "b": 0, "op": "gser"},
            {"a": 12, "b": 0, "op": "gser"},
            {"a": 16, "b": 0, "op": "gser"},
            {"a": 20, "b": 0, "op": "gser"},
            {"a": 24, "b": 0, "op": "gser"},
            {"a": 28, "b": 0, "op": "gser"},
            {"a": 32, "b": 0, "op": "gser"},
            {"a": 36, "b": 0, "op": "gser"},
            {"a": 40, "b": 0, "op": "gser"},
            {"a": 44, "b": 0, "op": "gser"},
        ],
    },
]
LESSONS.extend(_PRECALC_U8)

# =============================================================================
# PRE-CALC UNIT 9 -- Introduction to Limits (build lp)
# ⭐ THE NINTH COURSE CLOSES HERE. The thread: WHERE WAS IT HEADED? -- a
# question that does not care what happens at the point itself. Substitution
# when nothing breaks, the hole where the function is undefined yet the
# heading is plain, two sides that may disagree, and the average rate of
# change over a shrinking window -- the limit Calculus is built on, handed
# forward.
# =============================================================================
_PRECALC_U9 = [
    {
        "id": "pc-u9-walk-the-value-in",
        "course": "precalc", "unit": 9,
        "topic": "Limits by substitution",
        "op": "lsub", "max_value": 90,
        "levels": ("abstract",),
        "symbols": ("limit", "creeps"),
        "advance_line": "Three in a row, and you can say why — you've got it! Nothing breaks, so walk the value in.",
        "why": [
            ("Why ask where a curve was headed? The last unit of Pre-Calculus asks "
             "one question: where was it HEADED? Follow a curve toward some x without "
             "ever landing on it, and the value it approaches is called the limit. You "
             "have met one already — the settling number of an endless sum.",
             '[[goal text="Walk the value in"]][[step eq="x → some number · y → ?"]]'),
        ],
        "picture": [
            ("Here is the line y equals 5 x plus 2 on the grid. Run your eye along it "
             "toward x equals 4 from either side: nothing breaks, nothing jumps, no "
             "hole. The line is simply there, so the value it heads for is the value "
             "it has.",
             '[[graph lines="y=5x+2" range="0..7" caption="y = 5x + 2 — a line that never breaks"]]'),
        ],
        "teach": [
            ("That is the method: when nothing breaks, walk the value in. As x creeps "
             "toward 4, 5 x plus 2 creeps toward 5 times 4 plus 2 — 22. Walk x in, and "
             "the value walks in beside it. No limit needed, strictly speaking; the "
             "function is simply there.",
             '[[graph lines="y=5x+2" points="(4,22)" range="0..7" caption="walk x in to 4 — y walks in to 22"]][[step eq="y = 5x + 2 · x: 4 · y: 22"]]'),
            ("Two slips. Handing back the 4 answers where x went, not where y went. "
             "And 5 plus 2 reads the times as a plus. Do the arithmetic the formula "
             "actually asks for — the limit of a well-behaved line is just its value.",
             '[[step eq="22 ✓"]][[step eq="4 ✗ that is x · 7 ✗ added instead"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. As x creeps toward 6, 7 x plus 2 "
                        "creeps toward 44.",
                        '[[graph lines="y=7x+2" points="(6,44)" range="0..9" caption="x → 6, y → 44"]][[step eq="7 × 6 + 2 = 44"]]'),
             "ask": {'a': 8, 'b': 6, 'c': 3, 'op': 'lsub'}},
            {"worked": ("One more together. As x creeps toward 8, 4 x plus 6 creeps toward "
                        "4 times 8 plus 6 — 38.",
                        '[[graph lines="y=4x+6" points="(8,38)" range="0..11" caption="x → 8, y → 38"]][[step eq="4 × 8 + 6 = 38"]]'),
             "ask": {'a': 9, 'b': 7, 'c': 5, 'op': 'lsub'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. As x creeps toward 4, "
                       "5 x plus 2 creeps toward 22. Tap the reason why."),
            "choices": ("because nothing breaks, so the value walks in with x | because "
                        "the limit is the x you creep toward | because the limit adds the "
                        "two numbers in the rule"),
            "answer": "because nothing breaks, so the value walks in with x",
            "board": '[[graph lines="y=5x+2" points="(4,22)" range="0..7" caption="walk the value in"]]',
        },
        "recap": [
            ("So, here it is again. A limit asks where a curve was headed. When "
             "nothing breaks — a plain line — walk x in and the value walks in beside "
             "it: the limit is simply the value there. Never hand back the x, and "
             "never read a times as a plus.",
             '[[graph lines="y=5x+2" range="0..7" caption="nothing breaks, so walk the value in"]]'),
            ("And that is the first limit, the easy kind.",
             '[[step eq="x → 4 · 5x + 2 → 22"]]'),
        ],
        "bank": [
            {"a": 2, "b": 3, "c": 1, "op": "lsub"},
            {"a": 3, "b": 2, "c": 4, "op": "lsub"},
            {"a": 2, "b": 5, "c": 3, "op": "lsub"},
            {"a": 4, "b": 3, "c": 2, "op": "lsub"},
            {"a": 3, "b": 4, "c": 5, "op": "lsub"},
            {"a": 5, "b": 3, "c": 4, "op": "lsub"},
            {"a": 4, "b": 5, "c": 3, "op": "lsub"},
            {"a": 6, "b": 4, "c": 3, "op": "lsub"},
            {"a": 5, "b": 6, "c": 5, "op": "lsub"},
            {"a": 7, "b": 5, "c": 4, "op": "lsub"},
        ],
    },
    {
        "id": "pc-u9-the-hole-in-the-curve",
        "course": "precalc", "unit": 9,
        "topic": "Limits at a hole",
        "op": "lhol", "max_value": 40, "min_value": 0,
        "levels": ("abstract",),
        "symbols": ("hole", "undefined"),
        "advance_line": "Three in a row, and you can say why — you've got it! The hole has no value, but it has a heading.",
        "why": [
            ("Why were limits invented? For this case. Take y equals: x squared take "
             "away 25, all divided by x take away 5. At x equals 5 the bottom is zero, "
             "so the function is undefined there — a hole in the curve, one point "
             "missing.",
             '[[goal text="The hole in the curve"]][[step eq="y = (x² − 25) ÷ (x − 5) · x = 5 forbidden"]]'),
        ],
        "picture": [
            ("Here is the machine with 5 fed in: the bottom turns to zero and the "
             "machine jams — no output at all. And here is the curve: a straight line "
             "with one open circle punched out of it at x equals 5. Look at where "
             "the line was heading on both sides of that hole.",
             '[[machine input="5" rule="(x² − 25) ÷ (x − 5)" output="jammed" caption="at x = 5 the bottom is zero — jammed"]][[graph func="(x^2-25)/(x-5)" hole="5" range="2..8" yrange="4..16" caption="a straight line with a hole at x = 5"]]'),
        ],
        "teach": [
            ("That is the method. Everywhere else, the top factors into: x take away "
             "5, times x plus 5 — and the take-aways cancel. So away from the hole "
             "this curve IS x plus 5. As x creeps toward 5, y creeps toward 10, "
             "calmly, from both sides.",
             '[[graph func="(x^2-25)/(x-5)" hole="5" range="2..8" yrange="4..16" caption="headed for 10 from both sides — the hole sits right there"]][[step eq="(x−5)(x+5) ÷ (x−5) = x + 5"]][[step eq="x → 5 · y → 10"]]'),
            ("That is the whole point of a limit: it reports where the curve was "
             "HEADED, and never asks what happens at the point itself. The function "
             "truly has no value at 5. It still has a heading — 10 — and 5 is only "
             "where the hole sits.",
             '[[step eq="10 ✓ the heading"]][[step eq="5 ✗ that is the hole · 0 ✗ undefined is not zero"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. x squared take away 100, over x "
                        "take away 10: away from the hole it is x plus 10, so the heading "
                        "is 20.",
                        '[[graph func="(x^2-100)/(x-10)" hole="10" range="7..13" yrange="14..26" caption="a hole at 10 — headed for 20"]][[step eq="x → 10 · y → 20"]]'),
             "ask": {'a': 14, 'b': 0, 'op': 'lhol'}},
            {"worked": ("One more together. x squared take away 169, over x take away 13: "
                        "away from the hole it is x plus 13, so the heading is 26.",
                        '[[graph func="(x^2-169)/(x-13)" hole="13" range="10..16" yrange="20..32" caption="a hole at 13 — headed for 26"]][[step eq="x → 13 · y → 26"]]'),
             "ask": {'a': 16, 'b': 0, 'op': 'lhol'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. x squared take away "
                       "25, over x take away 5, is undefined at 5 but heads for 10. Tap "
                       "the reason why."),
            "choices": ("because away from the hole the curve is x plus 5 | because "
                        "undefined means the limit is zero | because the limit is the x "
                        "where the hole sits"),
            "answer": "because away from the hole the curve is x plus 5",
            "board": '[[graph func="(x^2-25)/(x-5)" hole="5" range="2..8" yrange="4..16" caption="the hole has no value, but it has a heading"]]',
        },
        "recap": [
            ("So, here it is again. At a hole the function has no value, and the "
             "limit does not mind: it reports only where the curve was headed. "
             "Cancel the take-aways, and the heading is plain. Do not answer the x "
             "where the curve is missing, and undefined is not zero.",
             '[[machine input="5" rule="(x² − 25) ÷ (x − 5)" output="jammed" caption="no value at the hole — a heading all the same"]]'),
            ("And that is what limits were invented for.",
             '[[step eq="x → 5 · y → 10"]]'),
        ],
        "bank": [
            {"a": 2, "b": 0, "op": "lhol"},
            {"a": 3, "b": 0, "op": "lhol"},
            {"a": 4, "b": 0, "op": "lhol"},
            {"a": 6, "b": 0, "op": "lhol"},
            {"a": 7, "b": 0, "op": "lhol"},
            {"a": 8, "b": 0, "op": "lhol"},
            {"a": 9, "b": 0, "op": "lhol"},
            {"a": 11, "b": 0, "op": "lhol"},
            {"a": 12, "b": 0, "op": "lhol"},
            {"a": 15, "b": 0, "op": "lhol"},
        ],
    },
    {
        "id": "pc-u9-the-two-sides-disagree",
        "course": "precalc", "unit": 9,
        "topic": "One-sided limits",
        "op": "lsid", "max_value": 30,
        "levels": ("abstract",),
        "symbols": ("side", "approach"),
        "advance_line": "Three in a row, and you can say why — you've got it! Read the side you were asked to come from.",
        "why": [
            ("Why can the two sides disagree? Unit One built functions in pieces. "
             "Watch what limits do to one. Say y is 3 when x is below 6, and 9 when x "
             "is 6 or more — a step. Creep up on 6 and the answer depends entirely on "
             "which side you approach from.",
             '[[goal text="The two sides disagree"]][[step eq="x < 6: y = 3 · x ≥ 6: y = 9"]]'),
        ],
        "picture": [
            ("Here is the step on the grid: a low shelf at 3 for every x below 6, and "
             "a high shelf at 9 from 6 onward. Look at the jump at x equals 6 — the "
             "open circle on the low shelf, the filled dot on the high one. Coming in "
             "from the left you ride the low shelf; from the right, the high one.",
             '[[graph func="3 for x<6; 9 for x>=6" range="0..12" yrange="0..13" caption="a step at 6 — two shelves, two headings"]]'),
        ],
        "teach": [
            ("That is the method: read the side you were asked to come from. From the "
             "left, every x you pass is below 6, so y reads 3 the whole way in — the "
             "limit from that side is 3. From the right, every x is 6 or more, so y "
             "reads 9 all the way in. Two sides, two different headings.",
             '[[graph func="3 for x<6; 9 for x>=6" points="(4,3),(5,3),(7,9),(8,9)" range="0..12" yrange="0..13" caption="from the left y reads 3 all the way; from the right, 9"]][[step eq="from the left → 3"]][[step eq="from the right → 9"]]'),
            ("When the sides disagree the curve has no single limit there — and the "
             "answer is never the middle. 6 is not the heading from either side; "
             "nobody approaching that step ever sees 6. Read which side you were "
             "asked for, and report what that side sees.",
             '[[step eq="3 ✓ from the left"]][[step eq="9 ✗ other side · 6 ✗ split the difference"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. y is 20 below 6 and 28 at 6 or "
                        "more. Coming from the RIGHT, y reads 28.",
                        '[[graph func="20 for x<6; 28 for x>=6" points="(9,28),(8,28),(7,28)" range="0..12" yrange="0..32" caption="from the right, y reads 28 all the way"]][[step eq="from the right → 28"]]'),
             "ask": {'a': 11, 'b': 19, 'c': 1, 'op': 'lsid'}},
            {"worked": ("One more together. y is 9 below 6 and 17 at 6 or more. From the "
                        "LEFT, y reads 9.",
                        '[[graph func="9 for x<6; 17 for x>=6" points="(3,9),(4,9),(5,9)" range="0..12" yrange="0..21" caption="from the left, y reads 9 all the way"]][[step eq="from the left → 9"]]'),
             "ask": {'a': 13, 'b': 21, 'c': 0, 'op': 'lsid'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. On the step that is 3 "
                       "below 6 and 9 from 6 on, the limit from the left is 3. Tap the "
                       "reason why."),
            "choices": ("because every x on the left side sits on the low shelf | because "
                        "the limit at a step is halfway between the shelves | because the "
                        "limit is always the higher shelf"),
            "answer": "because every x on the left side sits on the low shelf",
            "board": '[[graph func="3 for x<6; 9 for x>=6" points="(4,3),(5,3)" range="0..12" yrange="0..13" caption="from the left → 3"]]',
        },
        "recap": [
            ("So, here it is again. At a step, the two sides can disagree: coming in "
             "from the left you ride one shelf, from the right the other, and each "
             "side reports what it sees. Never answer the other side, and never split "
             "the difference.",
             '[[graph func="3 for x<6; 9 for x>=6" range="0..12" yrange="0..13" caption="read the side you were asked to come from"]]'),
            ("And that is a limit with a side.",
             '[[step eq="from the left → 3 · from the right → 9"]]'),
        ],
        "bank": [
            {"a": 4, "b": 10, "c": 0, "op": "lsid"},
            {"a": 5, "b": 11, "c": 0, "op": "lsid"},
            {"a": 2, "b": 16, "c": 0, "op": "lsid"},
            {"a": 7, "b": 13, "c": 0, "op": "lsid"},
            {"a": 8, "b": 14, "c": 1, "op": "lsid"},
            {"a": 9, "b": 15, "c": 1, "op": "lsid"},
            {"a": 10, "b": 16, "c": 1, "op": "lsid"},
            {"a": 12, "b": 20, "c": 0, "op": "lsid"},
            {"a": 14, "b": 22, "c": 1, "op": "lsid"},
            {"a": 16, "b": 24, "c": 0, "op": "lsid"},
        ],
    },
    {
        "id": "pc-u9-the-shrinking-window",
        "course": "precalc", "unit": 9,
        "topic": "Average rate of change",
        "op": "avgr", "max_value": 24,
        "levels": ("abstract",),
        "symbols": ("rise", "window"),
        "advance_line": "Three in a row, and you can say why — you've got it! Rise divided by run — and on this curve, it is the two x's put together.",
        "why": [
            ("Why shrink the window? Pre-Calculus ends by handing Calculus its first "
             "question. On y equals x squared, move x from 2 to 6. y climbs from 4 to "
             "36 — a rise of 32 — while x moves 4. So y rose 8 for each step of x, on "
             "average across that window.",
             '[[goal text="The shrinking window"]][[step eq="rise 32 ÷ run 4 = 8 per step"]]'),
        ],
        "picture": [
            ("Here is the curve y equals x squared with a window on it, from x equals "
             "2 to x equals 6. Between those two walls the curve climbs — and the "
             "straight line joining the two ends is the average climb across the "
             "window. Its steepness is the number we want.",
             '[[graph func="x^2" lines="x=2; x=6" range="0..7" yrange="0..50" caption="y = x² — the window from x = 2 to x = 6"]]'),
        ],
        "teach": [
            ("That is the method: rise divided by run. And 8 is simply 2 plus 6. On "
             "this curve the average rate is always the two x\'s put together — try 3 "
             "to 5: rise 16, run 2, and 8 again, which is 3 plus 5. A tidy shortcut, "
             "and it is about to do something remarkable.",
             '[[graph func="x^2" lines="y=8x-12" points="(2,4),(6,36)" range="0..7" yrange="0..50" caption="the line through the two ends climbs 8 per step — 2 + 6"]][[step eq="rise 32 ÷ run 4 = 8"]][[step eq="2 + 6 = 8 · 3 + 5 = 8"]]'),
            ("Shrink the window toward a single point. From 4 to 5 the rate is 9; "
             "from 4 to 4 point 1, about 8 point 1; closer still, 8 point 0 1. The "
             "rates creep toward 8 — twice the 4. That limit is called the "
             "derivative, and Calculus starts exactly there.",
             '[[step eq="4→5: 9 · 4→4.1: 8.1 · 4→4.01: 8.01"]][[step eq="the limit → 8 = 2 × 4"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. On y equals x squared, from 1 to "
                        "7: rise 48, run 6 — 8 per step, which is 1 plus 7.",
                        '[[graph func="x^2" lines="y=8x-7" points="(1,1),(7,49)" range="0..8" yrange="0..60" caption="48 ÷ 6 = 8 = 1 + 7"]][[step eq="48 ÷ 6 = 8 = 1 + 7"]]'),
             "ask": {'a': 2, 'b': 10, 'op': 'avgr'}},
            {"worked": ("One more together. From 7 to 11: rise 72, run 4 — 18 per step, "
                        "and 7 plus 11 is 18.",
                        '[[graph func="x^2" lines="y=18x-77" points="(7,49),(11,121)" range="0..12" yrange="0..130" caption="72 ÷ 4 = 18 = 7 + 11"]][[step eq="72 ÷ 4 = 18 = 7 + 11"]]'),
             "ask": {'a': 5, 'b': 12, 'op': 'avgr'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. On y equals x squared, "
                       "from 2 to 6 the average rise per step is 8. Tap the reason why."),
            "choices": ("because the rise of 32 is shared across a run of 4 | because the "
                        "average rise is the rise alone | because the average rise is the "
                        "run alone"),
            "answer": "because the rise of 32 is shared across a run of 4",
            "board": '[[graph func="x^2" lines="y=8x-12" points="(2,4),(6,36)" range="0..7" yrange="0..50" caption="rise 32 ÷ run 4 = 8"]]',
        },
        "recap": [
            ("So, here it is again. The average rate across a window is rise divided "
             "by run — and on y equals x squared it is the two x\'s put together. "
             "Shrink the window and the rates creep toward a limit: the derivative, "
             "where Calculus begins. Never answer the rise or the run alone.",
             '[[graph func="x^2" lines="x=2; x=6" range="0..7" yrange="0..50" caption="the shrinking window"]]'),
            ("And that is Pre-Calculus, handing its question forward.",
             '[[step eq="rise 32 ÷ run 4 = 8 = 2 + 6"]]'),
        ],
        "bank": [
            {"a": 1, "b": 3, "op": "avgr"},
            {"a": 2, "b": 4, "op": "avgr"},
            {"a": 1, "b": 5, "op": "avgr"},
            {"a": 3, "b": 6, "op": "avgr"},
            {"a": 2, "b": 7, "op": "avgr"},
            {"a": 4, "b": 8, "op": "avgr"},
            {"a": 3, "b": 9, "op": "avgr"},
            {"a": 5, "b": 10, "op": "avgr"},
            {"a": 4, "b": 11, "op": "avgr"},
            {"a": 6, "b": 12, "op": "avgr"},
        ],
    },
]
LESSONS.extend(_PRECALC_U9)

# ---- this course's slice of COURSE_ORDER: the teaching order (lessons/__init__.py joins the ten) ----
ORDER = [

    # ---- PRE-CALC (build ll) -- Unit 1: Functions & Their Graphs ----
    "pc-u1-machines-in-a-row", "pc-u1-the-graph-slides",
    "pc-u1-the-doorway", "pc-u1-a-function-in-pieces",

    # ---- PRE-CALC (build lm) -- Units 2 and 3 ----
    # Unit 2: Polynomial & Rational Functions
    "pc-u2-the-minus-parade", "pc-u2-no-long-division",
    "pc-u2-the-roots-secret", "pc-u2-twice-forbidden",
    # Unit 3: Exponential & Logarithmic Functions
    "pc-u3-the-power-comes-down", "pc-u3-rebuild-the-number",
    "pc-u3-count-the-halvings", "pc-u3-money-doubles",

    # ---- PRE-CALC (build ln) -- Units 4 and 5 ----
    # Unit 4: Trigonometric Functions
    "pc-u4-the-half-turn-language", "pc-u4-the-backwards-spin",
    "pc-u4-hug-the-flat-line", "pc-u4-the-faster-wave",
    # Unit 5: Analytic Trigonometry
    "pc-u5-one-whole-between-them", "pc-u5-partners-across-ninety",
    "pc-u5-the-mirror-knows", "pc-u5-count-the-crossings",

    # ---- PRE-CALC (build lo) -- Units 6 and 7 ----
    # Unit 6: Applications of Trigonometry
    "pc-u6-two-sides-and-the-angle", "pc-u6-the-thirty-degree-ramp",
    "pc-u6-past-the-full-turn", "pc-u6-the-arrow-and-its-steps",
    # Unit 7: Conic Sections & Parametric Equations
    "pc-u7-un-square-the-radius", "pc-u7-where-the-circle-sits",
    "pc-u7-edge-to-edge", "pc-u7-where-you-are-at-time-t",

    # ---- PRE-CALC (build lp) -- Units 8 and 9 -- ⭐ PRE-CALC COMPLETE ----
    # Unit 8: Sequences, Series & the Binomial Theorem
    "pc-u8-add-the-whole-run", "pc-u8-the-instruction-called-sigma",
    "pc-u8-when-order-does-not-matter", "pc-u8-the-sum-that-never-ends",
    # Unit 9: Introduction to Limits
    "pc-u9-walk-the-value-in", "pc-u9-the-hole-in-the-curve",
    "pc-u9-the-two-sides-disagree", "pc-u9-the-shrinking-window",
]

# I did no harm and this file is not truncated.

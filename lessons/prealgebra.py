# =============================================================================
# lessons/prealgebra.py  --  PRE-ALGEBRA: THE AUTHORED LESSONS  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-09-10  BUILD ux -- THE EXPRESSION COMES FIRST (Unit 9's two letter lessons),
#               and a trap beat that draws its picture again (Unit 8's triangle).
#               Jim's flag 22:43: "it should first show the equation, then the value
#               of x, not the other way around." Every teach beat, worked pair and
#               reason question in a-letter-holds-a-number and
#               a-number-against-a-letter now names the expression first; the boards
#               run expression -> what x holds -> the picture filled in.
#               ⚠️ TWO NEW GIVEAWAYS THE RE-ORDERING CREATED, both caught by the
#               presweep and both fixed here. The audits read a beat's OPENING
#               numbers, and expression-first opens on the coefficient rather than on
#               the value. mlx's teach beat said "what is 3 x? That is 3 times x...
#               9" -- opening 3, 3 with 9 following, which is a bank problem and its
#               answer -- so the shorthand is now named without repeating the
#               coefficient. evx's second worked pair opened on pair one's own ask
#               (5, 6), so it demonstrates x holding 6, x plus 7 instead.
#               area-of-a-triangle's trap beat says "twice the size of the one on the
#               board" and drew only two step lines; the halved rectangle is back.
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

_PREALGEBRA_MORE = [
    {
        "id": "pre-u2-the-biggest-factor", "course": "prealgebra", "unit": 2,
        "topic": "The biggest factor below the number", "op": "bfac", "max_value": 99,
        "levels": ("abstract",), "symbols": ("factor", "prime"),
        "advance_line": "Three in a row, and you can say why — you've got it! Divide by the smallest factor to find the biggest.",
        "why": [
            ("Why the biggest factor? Because it is the other end of the same "
             "question. Forty-five people into the fewest equal groups gave you 3 "
             "groups — and the biggest group you could make is what is left when you "
             "divide. Smallest and biggest are a pair, and one hands you the other.",
             '[[goal text="The biggest factor below the number"]]'),
        ],
        "picture": [
            ("Here is 45 as a rectangle. Its smallest factor above 1 is 3, and 45 "
             "divided by 3 is 15 — so the rectangle is 3 rows of 15. The two sides "
             "are a factor pair: the smallest factor, 3, is paired with the biggest "
             "one below 45, which is 15.",
             '[[step eq="45 = 3 × 15"]][[areamodel rows="3" cols="15" caption="smallest 3, biggest 15"]]'),
        ],
        "teach": [
            ("That is the method. Factors come in pairs, and the smallest one is "
             "always partnered with the biggest. So find the smallest factor above "
             "1, divide by it, and the biggest factor below the number arrives in "
             "one step.",
             '[[step eq="45 = 3 × 15"]][[step eq="smallest factor 3 → biggest factor 15"]]'),
            ("Here is the trap. Do not hand back the number just below. For 45 the "
             "answer is not 44, and it is not 9 either — 9 divides 45, but 15 is "
             "bigger. Find the smallest factor, divide by it, and the biggest one "
             "arrives in a single step. A prime number has no factor below it at all "
             "except 1, so these questions never hand you one.",
             '[[step eq="45 → 15 ✓"]][[step eq="44 ✗ close to 45, but it does not divide it at all"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 26. Its smallest factor is 2, "
                        "and 26 divided by 2 is 13 — 2 rows of 13.",
                        '[[step eq="26 = 2 × 13"]][[areamodel rows="2" cols="13" caption="smallest 2, biggest 13"]]'),
             "ask": {'a': 51, 'b': 0, 'op': 'bfac'}},
            {"worked": ("One more together. 63. Its smallest factor is 3, and 63 "
                        "divided by 3 is 21 — 3 rows of 21.",
                        '[[step eq="63 = 3 × 21"]][[areamodel rows="3" cols="21" caption="smallest 3, biggest 21"]]'),
             "ask": {'a': 85, 'b': 0, 'op': 'bfac'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. The biggest "
                       "factor of 45 below 45 is 15. Tap the reason why."),
            "choices": ("because 45 divided by its smallest factor, 3, gives 15 | "
                        "because the biggest factor is always the number just below | "
                        "because 9 divides 45, so 9 is the biggest"),
            "answer": "because 45 divided by its smallest factor, 3, gives 15",
            "board": '[[step eq="45 = 3 × 15"]][[areamodel rows="3" cols="15" caption="smallest 3, biggest 15"]]',
        },
        "recap": [
            ("So, here it is again. The smallest factor and the biggest are a pair — "
             "the two sides of one rectangle. Find the smallest, divide by it, and "
             "you are holding the biggest.",
             '[[areamodel rows="3" cols="15" caption="3 × 15 = 45"]]'),
            ("And never the number just below — that one almost never divides at all.",
             '[[step eq="45 = 3 × 15"]]'),
        ],
        "bank": [{"a": 4, "b": 0, "op": "bfac"}, {"a": 14, "b": 0, "op": "bfac"}, {"a": 22, "b": 0, "op": "bfac"}, {"a": 91, "b": 0, "op": "bfac"}, {"a": 36, "b": 0, "op": "bfac"}, {"a": 46, "b": 0, "op": "bfac"}, {"a": 56, "b": 0, "op": "bfac"}, {"a": 99, "b": 0, "op": "bfac"}, {"a": 82, "b": 0, "op": "bfac"}, {"a": 98, "b": 0, "op": "bfac"}],
    },
]
LESSONS.extend(_PREALGEBRA_MORE)

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
        "advance_line": "Three in a row, and you can say why — you've got it! You do the times first, every time.",
        "why": [
            ("Why does the order matter? Because a line of math can hold two jobs at "
             "once, and doing them in the wrong order gives a wrong answer. A shop "
             "receipt says 2 dollars, plus 3 packs at 4 dollars each. Nobody pays 20 "
             "dollars for that. The times has to happen before the plus.",
             '[[goal text="Times before add"]]'),
        ],
        "picture": [
            ("Here is 2 plus 3 times 4, worked down the board. First move: the times "
             "— 3 times 4 equals 12. Second move: the add — 2 plus 12 equals 14. "
             "Watch the order: the times went first.",
             '[[solve start="2 + 3 × 4" steps="times first : 2 + 12 | then add : 14" caption="2 + 3 × 4 = 14"]]'),
        ],
        "teach": [
            ("That is the rule. When a plus and a times share one line, the times "
             "goes first. Always — and it is not left to right. If you had gone left "
             "to right on that line you would have said 20, and 20 is wrong.",
             '[[solve start="2 + 3 × 4" steps="times first : 2 + 12 | then add : 14" caption="the times first, then the add"]]'),
            ("One more. 5 plus 2 times 6. Find the times: 2 times 6 equals 12. Then "
             "add: 5 plus 12 equals 17.",
             '[[solve start="5 + 2 × 6" steps="times first : 5 + 12 | then add : 17" caption="5 + 2 × 6 = 17"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 4 plus 3 times 3. Times "
                        "first: 3 times 3 equals 9. Then 4 plus 9 equals 13.",
                        '[[solve start="4 + 3 × 3" steps="times first : 4 + 9 | then add : 13" caption="4 + 3 × 3 = 13"]]'),
             "ask": {'a': 3, 'b': 2, 'c': 5, 'op': 'tba'}},
            {"worked": ("One more together. 6 plus 4 times 2. The times gives 8. Then "
                        "6 plus 8 equals 14.",
                        '[[solve start="6 + 4 × 2" steps="times first : 6 + 8 | then add : 14" caption="6 + 4 × 2 = 14"]]'),
             "ask": {'a': 2, 'b': 3, 'c': 6, 'op': 'tba'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 2 plus 3 times 4 "
                       "equals 14. Tap the reason why."),
            # (tc) "always work from left to right" tripped the order-of-operations-
            # as-law referee on the joined options; the slip reads the same without it
            "choices": ("because the times is done before the add | because you work "
                        "it left to right | because the add is done before the times"),
            "answer": "because the times is done before the add",
            "board": '[[solve start="2 + 3 × 4" steps="times first : 2 + 12 | then add : 14" caption="2 + 3 × 4 = 14"]]',
        },
        "recap": [
            ("So, here it is again. When a plus and a times share a line, the times "
             "goes first, then the add. Never left to right.",
             '[[solve start="2 + 3 × 4" steps="times first : 2 + 12 | then add : 14" caption="times first, then add"]]'),
            ("And that is why the receipt comes out right — 3 packs at 4 dollars, then "
             "the 2 dollars on top.",
             '[[step eq="2 + 12 = 14"]]'),
        ],
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
        "advance_line": "Three in a row, and you can say why — you've got it! What is inside the parentheses goes first.",
        "why": [
            ("Why parentheses? Because sometimes you need the add to go first, and "
             "the rule says the times wins. Three friends each get 2 cookies and 1 "
             "candy — that is 2 plus 1, three times over. Parentheses are how you "
             "tell the math: this part first.",
             '[[goal text="Parentheses first"]]'),
        ],
        "picture": [
            ("Here is 2 plus 3, in parentheses, times 4. The parentheses are the two "
             "curved marks around 2 plus 3. First move: inside them — 2 plus 3 equals "
             "5. Second move: the times — 5 times 4 equals 20.",
             '[[solve start="(2 + 3) × 4" steps="inside first : 5 × 4 | then times : 20" caption="(2 + 3) × 4 = 20"]]'),
        ],
        "teach": [
            ("That is the rule. Whatever sits inside parentheses goes first — even an "
             "add, even when a times is waiting. Without the parentheses that same "
             "line would be 14, so the marks change the answer.",
             '[[solve start="(2 + 3) × 4" steps="inside first : 5 × 4 | then times : 20" caption="inside first, then the times"]]'),
            ("One more. 1 plus 6, in parentheses, times 3. Inside: 1 plus 6 equals 7. "
             "Then 7 times 3 equals 21.",
             '[[solve start="(1 + 6) × 3" steps="inside first : 7 × 3 | then times : 21" caption="(1 + 6) × 3 = 21"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 4 plus 2, in parentheses, "
                        "times 5. Inside gives 6. Then 6 times 5 equals 30.",
                        '[[solve start="(4 + 2) × 5" steps="inside first : 6 × 5 | then times : 30" caption="(4 + 2) × 5 = 30"]]'),
             "ask": {'a': 3, 'b': 3, 'c': 4, 'op': 'parf'}},
            {"worked": ("One more together. 5 plus 1, in parentheses, times 7. Inside "
                        "gives 6. Then 6 times 7 equals 42.",
                        '[[solve start="(5 + 1) × 7" steps="inside first : 6 × 7 | then times : 42" caption="(5 + 1) × 7 = 42"]]'),
             "ask": {'a': 2, 'b': 5, 'c': 3, 'op': 'parf'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 2 plus 3, in "
                       "parentheses, times 4 equals 20. Tap the reason why."),
            "choices": ("because what is inside the parentheses goes first | because "
                        "the times always goes first | because parentheses mean times "
                        "two"),
            "answer": "because what is inside the parentheses goes first",
            "board": '[[solve start="(2 + 3) × 4" steps="inside first : 5 × 4 | then times : 20" caption="(2 + 3) × 4 = 20"]]',
        },
        "recap": [
            ("So, here it is again. Parentheses beat everything: whatever is inside "
             "them goes first, then the rest of the line follows the usual order.",
             '[[solve start="(2 + 3) × 4" steps="inside first : 5 × 4 | then times : 20" caption="inside first"]]'),
            ("And they are how you tell the math which part to do first.",
             '[[step eq="(2 + 3) × 4 = 20"]]'),
        ],
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
        "advance_line": "Three in a row, and you can say why — you've got it! A small high number counts how many to multiply.",
        "why": [
            ("Why exponents? Because multiplying the same number again and again is "
             "slow to write. A square floor 3 tiles by 3 tiles; a box 2 cubes wide, 2 "
             "deep, 2 high. The exponent is the short way to say: multiply this "
             "number by itself, this many times.",
             '[[goal text="Exponents are repeated times"]]'),
        ],
        "picture": [
            ("Here is 3 squared. Three rows of three make a square — count the boxes "
             "and there are 9. The small 2 up high says: two 3s multiplied. 3 times 3 "
             "equals 9.",
             '[[areamodel rows="3" cols="3" caption="3² = 3 × 3 = 9"]]'),
        ],
        "teach": [
            ("That small high number is an exponent. It is not a times. It counts how "
             "many copies of the number to multiply. 3 with a small 2 means two 3s "
             "multiplied, and we say it as three squared — because it draws a square.",
             '[[areamodel rows="3" cols="3" caption="three rows of three"]][[step eq="3² = 3 × 3 = 9"]]'),
            ("A small 3 means three copies, and we say it as to the power 3. 2 with a "
             "small 3 is 2 times 2 times 2, which equals 8 — a block of cubes 2 wide, "
             "2 deep, 2 high. Careful — it is not 2 times 3. That would be 6, and 6 "
             "is wrong.",
             '[[solid kind="prism" w="2" d="2" h="2" caption="2³ = 2 × 2 × 2 = 8"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 4 squared is two 4s "
                        "multiplied — 4 times 4, which equals 16.",
                        '[[areamodel rows="4" cols="4" caption="4² = 4 × 4 = 16"]]'),
             "ask": {'a': 6, 'b': 2, 'op': 'expn'}},
            {"worked": ("One more together. 3 with a small 3 means three 3s "
                        "multiplied: 3 times 3 times 3, which equals 27.",
                        '[[solid kind="prism" w="3" d="3" h="3" caption="3³ = 3 × 3 × 3 = 27"]]'),
             "ask": {'a': 7, 'b': 2, 'op': 'expn'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 3 squared equals "
                       "9. Tap the reason why."),
            "choices": ("because the small 2 means two 3s multiplied | because the "
                        "small 2 means times 2 | because squared means the number "
                        "twice, added"),
            "answer": "because the small 2 means two 3s multiplied",
            "board": '[[areamodel rows="3" cols="3" caption="3² = 3 × 3 = 9"]]',
        },
        "recap": [
            ("So, here it is again. An exponent counts how many copies to multiply: "
             "a small 2 is two copies, a square; a small 3 is three copies, a cube. "
             "It is never a times.",
             '[[areamodel rows="3" cols="3" caption="3² = 9"]][[step eq="2³ = 2 × 2 × 2 = 8"]]'),
            ("And it is the short way to write multiplying a number by itself.",
             '[[step eq="3 × 3 = 3²"]]'),
        ],
        "bank": [
            {"a": 2, "b": 3, "op": "expn"},
            {"a": 3, "b": 2, "op": "expn"},
            {"a": 4, "b": 2, "op": "expn"},
            {"a": 5, "b": 2, "op": "expn"},
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
        "advance_line": "Three in a row, and you can say why — you've got it! Power first, then times, then add.",
        "why": [
            ("Why one order for everything? Because a real formula mixes all three "
             "jobs at once. Take a square garden 3 by 3, plus 2 flower beds of 4 "
             "each. That is a power, a times and an add on one line — and there is "
             "only one right way through it.",
             '[[goal text="Power, then times, then add"]]'),
        ],
        "picture": [
            ("Here is 3 squared plus 2 times 4, worked down the board. First move: "
             "the power — 3 squared equals 9. Second move: the times — 2 times 4 "
             "equals 8. Last move: the add — 9 plus 8 equals 17.",
             '[[solve start="3² + 2 × 4" steps="power first : 9 + 2 × 4 | times next : 9 + 8 | add last : 17" caption="3² + 2 × 4 = 17"]]'),
        ],
        "teach": [
            ("That is the whole order. You know two rules: the times goes before the "
             "add, and parentheses go before everything. The exponent joins them, and "
             "it goes first of all. Power first, then times, then add.",
             '[[solve start="3² + 2 × 4" steps="power first : 9 + 2 × 4 | times next : 9 + 8 | add last : 17" caption="power, then times, then add"]]'),
            ("One more. 2 squared plus 5 times 3. The power gives 4. The times gives "
             "15. 4 plus 15 equals 19.",
             '[[solve start="2² + 5 × 3" steps="power first : 4 + 5 × 3 | times next : 4 + 15 | add last : 19" caption="2² + 5 × 3 = 19"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 4 squared plus 3 times 2. "
                        "Power: 16. Times: 6. 16 plus 6 equals 22.",
                        '[[solve start="4² + 3 × 2" steps="power first : 16 + 3 × 2 | times next : 16 + 6 | add last : 22" caption="4² + 3 × 2 = 22"]]'),
             "ask": {'a': 3, 'b': 4, 'c': 2, 'op': 'exo'}},
            {"worked": ("One more together. 5 squared plus 2 times 6. Power: 25. "
                        "Times: 12. 25 plus 12 equals 37.",
                        '[[solve start="5² + 2 × 6" steps="power first : 25 + 2 × 6 | times next : 25 + 12 | add last : 37" caption="5² + 2 × 6 = 37"]]'),
             "ask": {'a': 4, 'b': 5, 'c': 2, 'op': 'exo'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 3 squared plus 2 "
                       "times 4 equals 17. Tap the reason why."),
            "choices": ("because the power comes first, then the times, then the add | "
                        "because you work from left to right | because the add comes "
                        "before the times"),
            "answer": "because the power comes first, then the times, then the add",
            "board": '[[solve start="3² + 2 × 4" steps="power first : 9 + 2 × 4 | times next : 9 + 8 | add last : 17" caption="3² + 2 × 4 = 17"]]',
        },
        "recap": [
            ("So, here it is again. One order for the whole line: parentheses, then "
             "the power, then the times, then the add.",
             '[[solve start="3² + 2 × 4" steps="power first : 9 + 2 × 4 | times next : 9 + 8 | add last : 17" caption="power, times, add"]]'),
            ("And it is the one right way through any formula that mixes them.",
             '[[step eq="3² + 2 × 4 = 17"]]'),
        ],
        "bank": [
            {"a": 3, "b": 2, "c": 2, "op": "exo"},
            {"a": 3, "b": 3, "c": 2, "op": "exo"},
            {"a": 3, "b": 3, "c": 3, "op": "exo"},
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
        "advance_line": "Three in a row, and you can say why — you've got it! You can count a number's factors.",
        "why": [
            ("Why count factors? Because factors are the ways a number can be split "
             "into equal rows. Twelve chairs can stand in 1 row of 12, 2 rows of 6, "
             "or 3 rows of 4 — and knowing every way is what lets you share, arrange "
             "and simplify without guessing.",
             '[[goal text="How many factors a number has"]]'),
        ],
        "picture": [
            ("Here are the ways to arrange 6 in equal rows: 1 row of 6, and 2 rows of "
             "3. Those two rectangles hold every factor of 6 — 1, 2, 3 and 6. Four "
             "factors.",
             '[[write lines="1 × 6 | 2 × 3" caption="the factors of 6: 1, 2, 3, 6 — four"]][[array rows="2" cols="3" caption="2 rows of 3 = 6"]]'),
        ],
        "teach": [
            ("That is what a factor is: a number that divides another one exactly, "
             "with nothing left over — one side of a rectangle that holds it. 1 and "
             "the number itself are always factors. To count them, find every pair "
             "and write each number once.",
             '[[write lines="1 × 6 | 2 × 3" caption="every pair, each number written once"]]'),
            ("Now 11. Only 1 row of 11 works — nothing else fits. So 11 has just two "
             "factors. Numbers with exactly two are special, and they have a name "
             "you will meet next lesson.",
             '[[write lines="1 × 11" caption="the factors of 11: 1, 11 — two"]][[array rows="1" cols="11" caption="1 row of 11"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 8. The pairs are 1 and 8, "
                        "and 2 and 4 — 3, 5, 6 and 7 do not fit. So 8 has four factors.",
                        '[[write lines="1 × 8 | 2 × 4" caption="the factors of 8: 1, 2, 4, 8 — four"]][[array rows="2" cols="4" caption="2 rows of 4 = 8"]]'),
             "ask": {'a': 14, 'b': 4, 'op': 'nfac'}},
            {"worked": ("One more together. 4. The pairs are 1 and 4, and 2 and 2 — "
                        "the same number twice counts once. So 4 has three factors.",
                        '[[write lines="1 × 4 | 2 × 2" caption="the factors of 4: 1, 2, 4 — three"]][[array rows="2" cols="2" caption="2 rows of 2 = 4"]]'),
             "ask": {'a': 25, 'b': 3, 'op': 'nfac'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 6 has four "
                       "factors. Tap the reason why."),
            "choices": ("because four different numbers divide 6 exactly | because 6 "
                        "is an even number | because 6 is bigger than 4"),
            "answer": "because four different numbers divide 6 exactly",
            "board": '[[write lines="1 × 6 | 2 × 3" caption="the factors of 6: 1, 2, 3, 6"]]',
        },
        "recap": [
            ("So, here it is again. A factor divides a number exactly — it is one "
             "side of a rectangle that holds it. Find every pair, write each number "
             "once, and count.",
             '[[write lines="1 × 6 | 2 × 3" caption="1, 2, 3, 6 — four factors"]]'),
            ("And the factors are every way to arrange that many in equal rows.",
             '[[array rows="2" cols="3" caption="2 rows of 3"]]'),
        ],
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
        "advance_line": "Three in a row, and you can say why — you've got it! You can find a number's smallest factor.",
        "why": [
            ("Why hunt for the smallest factor? Because it is the first way in. Fifteen "
             "candies to share equally among the fewest friends possible — that is "
             "asking for the smallest number above 1 that divides 15. And it is the "
             "first step of breaking any number into primes, next lesson.",
             '[[goal text="The smallest factor above 1"]]'),
        ],
        "picture": [
            ("Here is the hunt for 27. Try 2 — 27 divided by 2 leaves 1 over, so no. "
             "Try 3 — 27 divided by 3 is 9 exactly, yes. Three rows of nine. The "
             "smallest factor of 27 above 1 is 3.",
             '[[write lines="27 ÷ 2 leaves 1 ✗ | 27 ÷ 3 = 9 ✓" caption="the first one that fits is 3"]][[array rows="3" cols="9" caption="3 × 9 = 27"]]'),
        ],
        "teach": [
            ("That is the method. Go up in order — 2, then 3, then 5, then 7 — and "
             "stop at the first one that divides exactly. A number with exactly two "
             "factors, just 1 and itself, is a prime number: 2, 3, 5 and 7 are primes. "
             "Every other number has a smaller factor to find.",
             '[[write lines="try 2, then 3, then 5, then 7" caption="stop at the first one that fits"]]'),
            ("Take 85. Try 2 — no. Try 3 — no. Try 5 — yes, 85 is five 17s. The "
             "smallest factor of 85 above 1 is 5.",
             '[[write lines="85 ÷ 2 ✗ | 85 ÷ 3 ✗ | 85 ÷ 5 = 17 ✓" caption="the first one that fits is 5"]][[areamodel rows="5" cols="17" caption="5 × 17 = 85"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 45. 2 does not fit. 3 does — "
                        "45 is three 15s. So the answer is 3.",
                        '[[write lines="45 ÷ 2 ✗ | 45 ÷ 3 = 15 ✓" caption="the first one that fits is 3"]][[areamodel rows="3" cols="15" caption="3 × 15 = 45"]]'),
             "ask": {'a': 51, 'b': 3, 'op': 'spf'}},
            {"worked": ("One more together. 91. 2 no, 3 no, 5 no. 7 fits — 91 is seven "
                        "13s. The answer is 7.",
                        '[[write lines="91 ÷ 2 ✗ | 91 ÷ 3 ✗ | 91 ÷ 5 ✗ | 91 ÷ 7 = 13 ✓" caption="the first one that fits is 7"]][[areamodel rows="7" cols="13" caption="7 × 13 = 91"]]'),
             "ask": {'a': 65, 'b': 5, 'op': 'spf'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 3 is the smallest "
                       "factor of 27 above 1. Tap the reason why."),
            "choices": ("because 2 does not divide 27 and 3 does | because 3 is the "
                        "smallest number after 1 | because 27 is odd, so 3 must "
                        "divide it"),
            "answer": "because 2 does not divide 27 and 3 does",
            "board": '[[write lines="27 ÷ 2 leaves 1 ✗ | 27 ÷ 3 = 9 ✓" caption="the first one that fits is 3"]]',
        },
        "recap": [
            ("So, here it is again. To find the smallest factor above 1, try 2, then "
             "3, then 5, then 7, and stop at the first one that divides exactly. A "
             "prime has none — only 1 and itself.",
             '[[write lines="try 2, then 3, then 5, then 7" caption="stop at the first one that fits"]]'),
            ("And that first way in is the first step of breaking a number down.",
             '[[array rows="3" cols="9" caption="3 × 9 = 27"]]'),
        ],
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
        "advance_line": "Three in a row, and you can say why — you've got it! Every number breaks down into primes.",
        "why": [
            ("Why break a number into primes? Because primes are the building blocks "
             "— every whole number is primes multiplied, and there is only one way "
             "to do it. Once you can see the blocks, sharing fractions, finding what "
             "two numbers have in common and simplifying all get easier.",
             '[[goal text="Breaking a number into primes"]]'),
        ],
        "picture": [
            ("Here is 24, broken down the ladder. Pull out the smallest factor, 2: "
             "24 is 2 times 12. The 12 is not prime, so pull out 2 again: 2 times 2 "
             "times 6. And again: 2 times 2 times 2 times 3. Now every number on the "
             "rung is prime — four primes.",
             '[[solve start="24" steps="pull out 2 : 2 × 12 | pull out 2 : 2 × 2 × 6 | pull out 2 : 2 × 2 × 2 × 3" caption="24 = 2 × 2 × 2 × 3: 4 primes"]]'),
        ],
        "teach": [
            ("That is the method. Keep pulling out the smallest factor until only "
             "primes are left, then count them. A prime that appears more than once "
             "counts every time — 24 needed three 2s.",
             '[[solve start="24" steps="pull out 2 : 2 × 12 | pull out 2 : 2 × 2 × 6 | pull out 2 : 2 × 2 × 2 × 3" caption="stop when every number is prime"]]'),
            ("Take 42. Smallest factor 2, so 42 is 2 times 21. Break the 21: 3 times "
             "7. 42 equals 2 times 3 times 7 — three primes.",
             '[[solve start="42" steps="pull out 2 : 2 × 21 | pull out 3 : 2 × 3 × 7" caption="42 = 2 × 3 × 7: 3 primes"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 8. Two 4s, and the 4 is two "
                        "2s. 8 equals 2 times 2 times 2 — three primes.",
                        '[[solve start="8" steps="pull out 2 : 2 × 4 | pull out 2 : 2 × 2 × 2" caption="8 = 2 × 2 × 2: 3 primes"]]'),
             "ask": {'a': 15, 'b': 2, 'op': 'npf'}},
            {"worked": ("One more together. 30. Two 15s, and 15 is three 5s. 30 equals "
                        "2 times 3 times 5 — three primes.",
                        '[[solve start="30" steps="pull out 2 : 2 × 15 | pull out 3 : 2 × 3 × 5" caption="30 = 2 × 3 × 5: 3 primes"]]'),
             "ask": {'a': 16, 'b': 4, 'op': 'npf'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 24 breaks into 2 "
                       "times 2 times 2 times 3 — four primes. Tap the reason why it is four."),
            "choices": ("because you pull out the smallest factor until only primes "
                        "are left | because every number breaks into exactly four "
                        "primes | because 24 is 4 times 6 and both are primes"),
            "answer": "because you pull out the smallest factor until only primes are left",
            "board": '[[solve start="24" steps="pull out 2 : 2 × 12 | pull out 2 : 2 × 2 × 6 | pull out 2 : 2 × 2 × 2 × 3" caption="24 = 2 × 2 × 2 × 3"]]',
        },
        "recap": [
            ("So, here it is again. Pull out the smallest factor, and again, and "
             "again, until every number on the rung is prime. Then count the primes, "
             "repeats included.",
             '[[solve start="24" steps="pull out 2 : 2 × 12 | pull out 2 : 2 × 2 × 6 | pull out 2 : 2 × 2 × 2 × 3" caption="24 = 2 × 2 × 2 × 3"]]'),
            ("And those primes are the blocks every number is built from.",
             '[[step eq="24 = 2 × 2 × 2 × 3"]]'),
        ],
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
        "advance_line": "Three in a row, and you can say why — you've got it! You can count straight past zero.",
        "why": [
            ("Why numbers below zero? Because the world has them. A winter morning "
             "at 3 degrees that drops 7 degrees. A lift that goes two floors below "
             "the ground floor. Owing money. Zero is not a wall — the numbers keep "
             "going on the other side, and you need to be able to count there.",
             '[[goal text="Counting back past zero"]]'),
        ],
        "picture": [
            ("Here is the number line with zero in the middle. Start at 3 and hop 7 "
             "to the left. Three steps take you to zero — and you still have four to "
             "go, so you keep going and land on negative 4. Those places left of "
             "zero are the negative numbers, and they are real places on the line.",
             '''[[numberline min="-10" max="10" points="3" hops="3,-4" caption="3 − 7 = −4"]]'''),
        ],
        "teach": [
            ("That is the whole idea. Counting back is hopping left, and the line "
             "does not stop at zero. One step left of zero is negative 1, two steps "
             "is negative 2. Count to zero, then keep counting — the rest of the "
             "hops tell you how far past zero you land.",
             '''[[numberline min="-10" max="10" points="-3" caption="one, two, three steps left of zero: −3"]][[step eq="3 − 7 = −4"]]'''),
            ("Start at 2 and count back 9. Two steps reach zero, seven more keep "
             "going left. You land on negative 7.",
             '''[[numberline min="-10" max="10" points="2" hops="2,-7" caption="2 − 9 = −7"]][[step eq="2 − 9 = −7"]]'''),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Start at 4, count back 6. Four "
                        "steps to zero, two more to the left — negative 2.",
                        '''[[numberline min="-10" max="10" points="4" hops="4,-2" caption="4 − 6 = −2"]][[step eq="4 − 6 = −2"]]'''),
             "ask": {'a': 6, 'b': 10, 'op': 'cbz'}},
            {"worked": ("One more together. Start at 1, count back 8. One step to "
                        "zero, seven more left — negative 7.",
                        '''[[numberline min="-10" max="10" points="1" hops="1,-7" caption="1 − 8 = −7"]][[step eq="1 − 8 = −7"]]'''),
             "ask": {'a': 4, 'b': 15, 'op': 'cbz'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Start at 3, count "
                       "back 7, and you land on negative 4. Tap the reason why."),
            "choices": ("because 3 steps reach zero and 4 more go past it | because 7 "
                        "take away 3 is 4, so the answer is 4 | because you cannot "
                        "count back past zero"),
            "answer": "because 3 steps reach zero and 4 more go past it",
            "board": '''[[numberline min="-10" max="10" points="3" hops="3,-4" caption="3 − 7 = −4"]]''',
        },
        "recap": [
            ("So, here it is again. Counting back is hopping left, and the line "
             "keeps going past zero. Count to zero, then count the rest of the hops "
             "— that is how far below zero you land, and the answer is negative.",
             '''[[numberline min="-10" max="10" points="3" hops="3,-4" caption="3 − 7 = −4"]]'''),
            ("And below zero is a real place — a cold morning, a floor under the "
             "ground, money owed.",
             '[[step eq="3 − 7 = −4"]]'),
        ],
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
        "advance_line": "Three in a row, and you can say why — you've got it! Adding a negative moves you left.",
        "why": [
            ("Why add a negative? Because a score can gain a penalty. You have 5 "
             "points and the next card says negative 7 — you add it, and you end up "
             "below zero. Adding a negative is how the math writes: something was "
             "taken off.",
             '[[goal text="Adding a negative number"]]'),
        ],
        "picture": [
            ("Here is 5 plus negative 7 on the line. Adding usually hops right — "
             "but this is adding a negative, so the hop goes left. Start at 5, hop "
             "7 to the left: five steps reach zero, two more pass it, and you land "
             "on negative 2.",
             '''[[numberline min="-10" max="10" points="5" hops="5,-2" caption="5 + (−7) = −2"]]'''),
        ],
        "teach": [
            ("That is the rule. Adding a negative number moves you LEFT along the "
             "line — exactly what counting back does. Adding negative 3 does what "
             "counting back 3 does. The plus sign does not stop you going left; the "
             "negative decides the direction.",
             '''[[numberline min="-10" max="10" points="5" hops="5,-2" caption="plus a negative: hop left"]][[step eq="5 + (−7) = −2"]]'''),
            ("Another: 3 plus negative 6. Start at 3, hop 6 left. Three steps reach "
             "zero, three more pass it. You land on negative 3.",
             '''[[numberline min="-10" max="10" points="3" hops="3,-3" caption="3 + (−6) = −3"]][[step eq="3 + (−6) = −3"]]'''),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 4 plus negative 9. Start at 4, "
                        "hop 9 to the left, land on negative 5.",
                        '''[[numberline min="-10" max="10" points="4" hops="4,-5" caption="4 + (−9) = −5"]][[step eq="4 + (−9) = −5"]]'''),
             "ask": {'a': 6, 'b': 13, 'op': 'addneg'}},
            {"worked": ("One more together. 2 plus negative 8. Start at 2, hop 8 to "
                        "the left, and land on negative 6.",
                        '''[[numberline min="-10" max="10" points="2" hops="2,-6" caption="2 + (−8) = −6"]][[step eq="2 + (−8) = −6"]]'''),
             "ask": {'a': 8, 'b': 12, 'op': 'addneg'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 5 plus negative 7 "
                       "equals negative 2. Tap the reason why."),
            "choices": ("because adding a negative moves you to the left | because "
                        "plus always moves you to the right | because 5 plus 7 is 12 "
                        "and you keep the sign"),
            "answer": "because adding a negative moves you to the left",
            "board": '''[[numberline min="-10" max="10" points="5" hops="5,-2" caption="5 + (−7) = −2"]]''',
        },
        "recap": [
            ("So, here it is again. Adding a negative number is a hop to the LEFT "
             "— the same move as counting back. The negative sets the direction, "
             "not the plus.",
             '''[[numberline min="-10" max="10" points="5" hops="5,-2" caption="5 + (−7) = −2"]]'''),
            ("And that is how a penalty on the score gets written down.",
             '[[step eq="5 + (−7) = −2"]]'),
        ],
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
        "advance_line": "Three in a row, and you can say why — you've got it! Taking away a negative moves you right.",
        "why": [
            ("Why would you take away a negative? Because a penalty can be cancelled. "
             "You are on 3, a negative 2 card sits against you, and then the referee "
             "takes it away. Taking away a thing that pulled you down pushes you up. "
             "The math has to say that, and it does.",
             '[[goal text="Taking away a negative number"]]'),
        ],
        "picture": [
            ("Here is 3 take away negative 2 on the line. Taking away usually hops "
             "left — but this is taking away a negative, a move-left being taken "
             "away, and that is a hop RIGHT. Start at 3, hop 2 to the right, and land on "
             "5.",
             '''[[numberline min="-10" max="10" points="3" hops="3,5" caption="3 − (−2) = 5"]]'''),
        ],
        "teach": [
            ("That is the surprising rule. Taking away a NEGATIVE moves you RIGHT: "
             "the two negatives cancel each other and the answer grows. Whenever a "
             "take away meets a negative, swap the pair for a plus.",
             '''[[numberline min="-10" max="10" points="3" hops="3,5" caption="take away a negative: hop right"]][[step eq="3 − (−2) = 3 + 2 = 5"]]'''),
            ("Another: 5 take away negative 3. Swap the pair for a plus: 5 plus 3 "
             "equals 8. On the line, start at 5 and hop 3 right.",
             '''[[numberline min="-10" max="10" points="5" hops="5,8" caption="5 − (−3) = 8"]][[step eq="5 − (−3) = 5 + 3 = 8"]]'''),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 6 take away negative 4. The "
                        "two negatives become a plus: 6 plus 4 equals 10. Start at 6, "
                        "hop 4 right.",
                        '''[[numberline min="-10" max="10" points="6" hops="6,10" caption="6 − (−4) = 10"]][[step eq="6 − (−4) = 6 + 4 = 10"]]'''),
             "ask": {'a': 7, 'b': 6, 'op': 'subneg'}},
            {"worked": ("One more together. 2 take away negative 9 equals 2 plus 9, "
                        "which equals 11. Start at 2, hop 9 right.",
                        '[[numberline min="-5" max="15" points="2" hops="2,11" caption="2 − (−9) = 11"]][[step eq="2 − (−9) = 11"]]'),
             "ask": {'a': 4, 'b': 13, 'op': 'subneg'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 3 take away "
                       "negative 2 equals 5. Tap the reason why."),
            "choices": ("because taking away a negative moves you to the right | "
                        "because take away always moves you to the left | because 3 "
                        "take away 2 is 1 and you flip the sign"),
            "answer": "because taking away a negative moves you to the right",
            "board": '''[[numberline min="-10" max="10" points="3" hops="3,5" caption="3 − (−2) = 5"]]''',
        },
        "recap": [
            ("So, here it is again. Taking away a negative is a hop to the RIGHT — "
             "the two negatives cancel, and the answer grows. Swap the pair for a "
             "plus.",
             '''[[numberline min="-10" max="10" points="3" hops="3,5" caption="3 − (−2) = 5"]]'''),
            ("And that is a penalty being cancelled — taking away what pulled you down "
             "pushes you up.",
             '[[step eq="3 − (−2) = 3 + 2 = 5"]]'),
        ],
        "bank": [
            {"a": 2, "b": 3, "op": "subneg"},
            {"a": 6, "b": 2, "op": "subneg"},
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
        "advance_line": "Three in a row, and you can say why — you've got it! One negative turns the answer negative.",
        "why": [
            ("Why times with a negative? Because losses repeat. Lose 3 dollars a day "
             "for 4 days — that is negative 3, four times over. Times is still the "
             "short way to add the same thing again and again; only the sign is new.",
             '[[goal text="Times with a negative number"]]'),
        ],
        "picture": [
            ("Here is negative 3 times 4 on the line. It means four lots of negative "
             "3 — four hops of 3 to the left, one after another, starting at zero. "
             "Watch them land: negative 3, negative 6, negative 9, negative 12.",
             '[[numberline min="-17" max="5" hops="0,-3,-6,-9,-12" caption="(−3) × 4 = −12"]]'),
        ],
        "teach": [
            ("That is the rule. Do the times first and ignore the sign: 3 times 4 "
             "equals 12. Then look at the signs. One of them is negative, so every "
             "hop went left, and the answer is negative. Negative 3 times 4 equals "
             "negative 12.",
             '[[numberline min="-17" max="5" hops="0,-3,-6,-9,-12" caption="four hops of 3 to the left"]][[step eq="(−3) × 4 = −12"]]'),
            ("Another: negative 5 times 3. Five 3s equal 15 — three hops of 5 to "
             "the left — and one negative sign turns it negative 15.",
             '[[numberline min="-20" max="5" hops="0,-5,-10,-15" caption="(−5) × 3 = −15"]][[step eq="(−5) × 3 = −15"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Negative 2 times 7. Two 7s "
                        "equal 14 — seven hops of 2 to the left — and one negative "
                        "turns it negative 14.",
                        '[[numberline min="-19" max="5" hops="0,-2,-4,-6,-8,-10,-12,-14" caption="(−2) × 7 = −14"]][[step eq="(−2) × 7 = −14"]]'),
             "ask": {'a': 4, 'b': 6, 'op': 'mulneg'}},
            {"worked": ("One more together. Negative 6 times 4. Six 4s equal 24 — four "
                        "hops of 6 to the left — so the answer is negative 24.",
                        '[[numberline min="-29" max="5" hops="0,-6,-12,-18,-24" caption="(−6) × 4 = −24"]][[step eq="(−6) × 4 = −24"]]'),
             "ask": {'a': 8, 'b': 5, 'op': 'mulneg'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Negative 3 times 4 "
                       "equals negative 12. Tap the reason why."),
            "choices": ("because four hops of 3 to the left land on negative 12 | "
                        "because two negatives make a positive | because the negative "
                        "sign goes away when you multiply"),
            "answer": "because four hops of 3 to the left land on negative 12",
            "board": '[[numberline min="-17" max="5" hops="0,-3,-6,-9,-12" caption="(−3) × 4 = −12"]]',
        },
        "recap": [
            ("So, here it is again. Times with a negative is the same times, hopped "
             "to the left. Multiply the numbers, then look at the signs: one negative "
             "turns the answer negative.",
             '[[numberline min="-17" max="5" hops="0,-3,-6,-9,-12" caption="(−3) × 4 = −12"]]'),
            ("And that is a loss repeated — the short way to add it again and again.",
             '[[step eq="(−3) × 4 = −12"]]'),
        ],
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

# =============================================================================
# PREALGEBRA -- UNIT 4: FRACTIONS (build kn, 2026-08-21)
# =============================================================================
# Basic Math takes fractions as far as adding and taking them away, and its
# "fraction of a group" only ever asks for a UNIT fraction -- "one half of 4". These
# four go past that, in the order the ideas actually depend on each other: take a
# non-unit fraction of a number (which is the unit-fraction skill done a times), then
# count how many parts fit inside a whole, which is what makes dividing BY a fraction
# make sense rather than being a rule to memorise, and finally read a fraction that is
# bigger than 1.
#
# EVERY ANSWER IS A WHOLE NUMBER, because a tap answer has to be one. That is a real
# constraint on what this unit can ask, and it was allowed to shape the questions
# rather than being worked around -- "how many fourths are in 3 wholes" is a better
# question than "what is 3 divided by one fourth" for a child meeting this the first
# time, and it happens to answer with an integer.
_PREALGEBRA_U4 = [
    {
        "id": "pre-u4-a-fraction-of-a-number",
        "course": "prealgebra", "unit": 4,
        "topic": "Two thirds of a number",
        "op": "nuf", "max_value": 30,
        "levels": ("abstract",),
        "symbols": ("fraction", "of"),
        "advance_line": "Three in a row, and you can say why — you've got it! Divide by the bottom, then take as many parts as the top says.",
        "why": [
            ("Why two thirds of a number? Because most shares are not one part. A "
             "pizza cut into 3, and you get 2 of the pieces. A shop taking two thirds "
             "off. Two thirds of the class going on the trip. You need the whole "
             "share, not just one slice of it.",
             '[[goal text="Two thirds of a number"]]'),
        ],
        "picture": [
            ("Here is 12 as a bar, cut into 3 equal parts. Each part is 12 divided by "
             "3 — that is 4. Two thirds means two of those parts: 4 and 4 are 8. Two "
             "thirds of 12 is 8.",
             '[[tape parts="4 | 4 | 4" total="12" caption="two of the three parts: 4 × 2 = 8"]]'),
        ],
        "teach": [
            ("That is the method, and it is always two steps. The bottom of the "
             "fraction says how many equal parts to cut — divide by it to find one "
             "part. The top says how many parts to take — times by it.",
             '[[tape parts="4 | 4 | 4" total="12" caption="bottom: cut into 3 · top: take 2"]][[step eq="12 ÷ 3 = 4"]][[step eq="4 × 2 = 8"]]'),
            ("One more. Three fourths of 20. Bottom first: 20 divided by 4 equals 5. "
             "Now the top: 5 times 3 equals 15.",
             '[[tape parts="5 | 5 | 5 | 5" total="20" caption="three of the four parts: 5 × 3 = 15"]][[step eq="20 ÷ 4 = 5"]][[step eq="5 × 3 = 15"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Two fifths of 15. 15 divided "
                        "by 5 equals 3, and 3 times 2 equals 6.",
                        '[[tape parts="3 | 3 | 3 | 3 | 3" total="15" caption="two of the five parts: 3 × 2 = 6"]][[step eq="15 ÷ 5 = 3"]][[step eq="3 × 2 = 6"]]'),
             "ask": {'a': 3, 'b': 4, 'c': 16, 'op': 'nuf'}},
            {"worked": ("One more together. Five sixths of 18. 18 divided by 6 equals "
                        "3, and 3 times 5 equals 15.",
                        '[[tape parts="3 | 3 | 3 | 3 | 3 | 3" total="18" caption="five of the six parts: 3 × 5 = 15"]][[step eq="18 ÷ 6 = 3"]][[step eq="3 × 5 = 15"]]'),
             "ask": {'a': 2, 'b': 7, 'c': 21, 'op': 'nuf'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Two thirds of 12 "
                       "is 8. Tap the reason why."),
            "choices": ("because one third is 4, and two of them are 8 | because two "
                        "thirds means divide by 2 and times by 3 | because you take 2 "
                        "and 3 away from 12"),
            "answer": "because one third is 4, and two of them are 8",
            "board": '[[tape parts="4 | 4 | 4" total="12" caption="two of the three parts: 8"]]',
        },
        "recap": [
            ("So, here it is again. Divide by the bottom to find one part, then "
             "times by the top to take that many parts. Two steps, always in that "
             "order.",
             '[[tape parts="4 | 4 | 4" total="12" caption="12 ÷ 3 = 4, then 4 × 2 = 8"]]'),
            ("And that is how you find the whole share, not just one slice.",
             '[[step eq="2/3 of 12 = 8"]]'),
        ],
        "bank": [
            {"a": 2, "b": 3, "c": 6, "op": "nuf"},
            {"a": 2, "b": 5, "c": 10, "op": "nuf"},
            {"a": 3, "b": 4, "c": 8, "op": "nuf"},
            {"a": 2, "b": 3, "c": 9, "op": "nuf"},
            {"a": 3, "b": 8, "c": 16, "op": "nuf"},
            {"a": 3, "b": 4, "c": 12, "op": "nuf"},
            {"a": 3, "b": 5, "c": 15, "op": "nuf"},
            {"a": 2, "b": 3, "c": 15, "op": "nuf"},
            {"a": 5, "b": 6, "c": 12, "op": "nuf"},
            {"a": 4, "b": 5, "c": 20, "op": "nuf"},
        ],
    },
    {
        "id": "pre-u4-how-many-parts-in-a-whole",
        "course": "prealgebra", "unit": 4,
        "topic": "How many parts fit in a whole",
        "op": "uic", "max_value": 60,
        "levels": ("abstract",),
        "symbols": ("fraction", "whole"),
        "advance_line": "Three in a row, and you can say why — you've got it! Each whole holds as many parts as the bottom says.",
        "why": [
            ("Why count the parts in a whole? Because things get cut up. Three pizzas "
             "cut into fourths for a party — how many slices is that? Three hours "
             "in quarter-hours. Once you can count parts across several wholes, "
             "every fraction sum gets easier.",
             '[[goal text="How many parts fit in a whole"]]'),
        ],
        "picture": [
            ("Here are 3 wholes, each cut into fourths. One whole holds 4 fourths. "
             "Three wholes hold 4, and 4, and 4 — 3 times 4 equals 12. There are "
             "12 fourths in 3 wholes.",
             '[[tape parts="4 | 4 | 4" total="3 wholes" caption="each whole holds 4 fourths: 3 × 4 = 12"]]'),
        ],
        "teach": [
            ("That is the rule. The bottom number of a fraction says how many equal "
             "parts make one whole — four fourths, five fifths. So counting the "
             "parts in several wholes is just a times: the wholes times the bottom.",
             '[[tape parts="4 | 4 | 4" total="3 wholes" caption="wholes × the bottom"]][[step eq="1 whole = 4 fourths"]][[step eq="3 × 4 = 12"]]'),
            ("How many sixths are in 3 wholes? One whole holds 6. Three wholes hold "
             "3 times 6, which equals 18.",
             '[[tape parts="6 | 6 | 6" total="3 wholes" caption="3 × 6 = 18 sixths"]][[step eq="3 × 6 = 18"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. How many thirds are in 4 "
                        "wholes? One whole holds 3, so 4 wholes hold 4 times 3, which "
                        "equals 12.",
                        '[[tape parts="3 | 3 | 3 | 3" total="4 wholes" caption="4 × 3 = 12 thirds"]][[step eq="4 × 3 = 12"]]'),
             "ask": {'a': 5, 'b': 4, 'op': 'uic'}},
            {"worked": ("One more together. How many eighths are in 3 wholes? 3 times 8 "
                        "equals 24.",
                        '[[tape parts="8 | 8 | 8" total="3 wholes" caption="3 × 8 = 24 eighths"]][[step eq="3 × 8 = 24"]]'),
             "ask": {'a': 6, 'b': 5, 'op': 'uic'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. There are 12 "
                       "fourths in 3 wholes. Tap the reason why."),
            "choices": ("because each whole holds 4 fourths, and 3 times 4 is 12 | "
                        "because dividing 3 by 4 gives 12 | because 3 wholes plus 4 "
                        "fourths is 12"),
            "answer": "because each whole holds 4 fourths, and 3 times 4 is 12",
            "board": '[[tape parts="4 | 4 | 4" total="3 wholes" caption="3 × 4 = 12 fourths"]]',
        },
        "recap": [
            ("So, here it is again. The bottom says how many parts fill one whole. "
             "To count the parts in several wholes, times the wholes by the bottom.",
             '[[tape parts="4 | 4 | 4" total="3 wholes" caption="3 × 4 = 12 fourths"]]'),
            ("And that is how many slices three cut-up pizzas hold.",
             '[[step eq="3 × 4 = 12"]]'),
        ],
        "bank": [
            {"a": 2, "b": 3, "op": "uic"},
            {"a": 3, "b": 2, "op": "uic"},
            {"a": 2, "b": 4, "op": "uic"},
            {"a": 6, "b": 2, "op": "uic"},
            {"a": 5, "b": 3, "op": "uic"},
            {"a": 4, "b": 5, "op": "uic"},
            {"a": 6, "b": 4, "op": "uic"},
            {"a": 5, "b": 6, "op": "uic"},
            {"a": 8, "b": 5, "op": "uic"},
            {"a": 7, "b": 7, "op": "uic"},
        ],
    },
    {
        "id": "pre-u4-dividing-by-a-fraction",
        "course": "prealgebra", "unit": 4,
        "topic": "Dividing by a fraction",
        "op": "dbf", "max_value": 60,
        "levels": ("abstract",),
        "symbols": ("fraction", "divided by"),
        "advance_line": "Three in a row, and you can say why — you've got it! Flip the fraction, then times.",
        "why": [
            ("Why divide by a fraction? Because you often need to know how many small "
             "pieces fit. Four cups of flour, and the scoop holds two thirds of a cup "
             "— how many scoops? A ribbon cut into pieces two thirds of a metre long. "
             "Dividing asks how many of these fit inside that.",
             '[[goal text="Dividing by a fraction"]]'),
        ],
        "picture": [
            ("Here is 2 divided by two thirds on the line. The question is: how many "
             "hops of two thirds reach 2? Hop from zero — one, two, three hops, and "
             "you land on 2 exactly. So 2 divided by two thirds equals 3. The answer "
             "is BIGGER than 2, because small pieces fit many times.",
             '[[numberline min="0" max="2" denom="3" hops="0,0.6667,1.3333,2" caption="3 hops of 2/3 reach 2: 2 ÷ (2/3) = 3"]]'),
        ],
        "teach": [
            ("That is what the picture shows: small pieces go into a whole many times "
             "over, so the answer grows. And there is a short rule that gives the same "
             "answer every time: flip the fraction over, then times. "
             "2 divided by two thirds is 2 times three halves: 2 times 3 equals 6, and "
             "6 divided by 2 equals 3. The same 3 the hops found.",
             '[[solve start="2 ÷ (2/3)" steps="flip and times : 2 × 3/2 | times the top : 6 ÷ 2 | divide : 3" caption="2 ÷ (2/3) = 3"]]'),
            ("One more. 3 divided by three fourths. On the line, four hops of three "
             "fourths reach 3. By the rule: flip to four thirds, 3 times 4 equals 12, "
             "and 12 divided by 3 equals 4.",
             '[[numberline min="0" max="3" denom="4" hops="0,0.75,1.5,2.25,3" caption="4 hops of 3/4 reach 3"]][[step eq="3 × 4/3 = 12 ÷ 3 = 4"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 2 divided by two fifths. Flip "
                        "to five halves. 2 times 5 equals 10, and 10 divided by 2 "
                        "equals 5 — five hops of two fifths reach 2.",
                        '[[numberline min="0" max="2" denom="5" hops="0,0.4,0.8,1.2,1.6,2" caption="5 hops of 2/5 reach 2"]][[step eq="2 × 5/2 = 5"]]'),
             "ask": {'a': 3, 'b': 5, 'c': 9, 'op': 'dbf'}},
            {"worked": ("One more together. 5 divided by five sixths. Flip to six "
                        "fifths. 5 times 6 equals 30, and 30 divided by 5 equals 6.",
                        '[[solve start="5 ÷ (5/6)" steps="flip and times : 5 × 6/5 | times the top : 30 ÷ 5 | divide : 6" caption="5 ÷ (5/6) = 6"]]'),
             "ask": {'a': 2, 'b': 5, 'c': 6, 'op': 'dbf'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 2 divided by two "
                       "thirds equals 3. Tap the reason why."),
            "choices": ("because three hops of two thirds fit inside 2 | because "
                        "dividing always gives a smaller answer | because 2 divided by "
                        "3 is what the fraction means"),
            "answer": "because three hops of two thirds fit inside 2",
            "board": '[[numberline min="0" max="2" denom="3" hops="0,0.6667,1.3333,2" caption="3 hops of 2/3 reach 2"]]',
        },
        "recap": [
            ("So, here it is again. Dividing by a fraction asks how many of them "
             "fit — and small pieces fit many times, so the answer grows. The quick "
             "rule: flip the fraction, then times.",
             '[[solve start="2 ÷ (2/3)" steps="flip and times : 2 × 3/2 | times the top : 6 ÷ 2 | divide : 3" caption="flip, then times"]]'),
            ("And that is how many scoops a bag of flour holds.",
             '[[step eq="2 ÷ (2/3) = 3"]]'),
        ],
        "bank": [
            {"a": 2, "b": 3, "c": 4, "op": "dbf"},
            {"a": 3, "b": 4, "c": 6, "op": "dbf"},
            {"a": 2, "b": 5, "c": 4, "op": "dbf"},
            {"a": 3, "b": 5, "c": 6, "op": "dbf"},
            {"a": 4, "b": 5, "c": 8, "op": "dbf"},
            {"a": 5, "b": 6, "c": 10, "op": "dbf"},
            {"a": 2, "b": 3, "c": 10, "op": "dbf"},
            {"a": 3, "b": 7, "c": 9, "op": "dbf"},
            {"a": 4, "b": 9, "c": 12, "op": "dbf"},
            {"a": 2, "b": 7, "c": 8, "op": "dbf"},
        ],
    },
    {
        "id": "pre-u4-fractions-bigger-than-one",
        "course": "prealgebra", "unit": 4,
        "topic": "Fractions bigger than one",
        "op": "imp", "max_value": 40,
        "levels": ("abstract",),
        "symbols": ("fraction", "whole", "number line"),
        "advance_line": "Three in a row, and you can say why — you've got it! Count how many times the bottom fits into the top.",
        "why": [
            ("Why fractions bigger than one? Because a pizza cut into 3 does not stop "
             "you eating 7 slices — that is more than two whole pizzas. Seven thirds "
             "is not a mistake. It is a real amount, and you need to know how many "
             "whole ones are hiding inside it.",
             '[[goal text="Fractions bigger than one"]]'),
        ],
        "picture": [
            ("Here is the number line marked in thirds, with eight thirds on it. Three thirds "
             "fill one whole — hop a whole at a time. Two whole hops use 6 thirds, "
             "and 2 thirds are left over. Eight thirds sits past 2 on the line: 2 "
             "whole ones and two thirds.",
             '[[numberline min="0" max="3" denom="3" hops="0,1,2,2.67" caption="8/3 = 2 whole ones and 2/3"]]'),
        ],
        "teach": [
            ("That is the method. To find the whole ones, ask how many times the "
             "bottom fits into the top. Eight thirds: 3 fits into 8 twice, with 2 "
             "left. So eight thirds is 2 whole ones and two thirds.",
             '[[numberline min="0" max="3" denom="3" hops="0,1,2,2.67" caption="3 fits into 8 twice, 2 left"]][[step eq="8 ÷ 3 = 2 whole ones, 2 left"]]'),
            ("Another. Eleven fourths. 4 fits into 11 twice, with 3 left. So eleven "
             "fourths is 2 whole ones and three fourths — past 2 on the line.",
             '[[numberline min="0" max="3" denom="4" hops="0,1,2,2.75" caption="11/4 = 2 whole ones and 3/4"]][[step eq="11 ÷ 4 = 2 whole ones, 3 left"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Nine halves. 2 fits into 9 "
                        "four times, with 1 left. Four whole ones and one half.",
                        '[[numberline min="0" max="5" denom="2" hops="0,1,2,3,4,4.5" caption="9/2 = 4 whole ones and 1/2"]][[step eq="9 ÷ 2 = 4 whole ones, 1 left"]]'),
             "ask": {'a': 14, 'b': 3, 'op': 'imp'}},
            {"worked": ("One more together. Twenty sevenths. 7 fits into 20 twice, "
                        "with 6 left. Two whole ones and six sevenths.",
                        '[[numberline min="0" max="3" denom="7" hops="0,1,2,2.86" caption="20/7 = 2 whole ones and 6/7"]][[step eq="20 ÷ 7 = 2 whole ones, 6 left"]]'),
             "ask": {'a': 22, 'b': 5, 'op': 'imp'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Eight thirds is "
                       "2 whole ones and two thirds. Tap the reason why."),
            "choices": ("because 3 thirds fill a whole, and 8 holds two of those | "
                        "because 8 take away 3 is 5 | because a fraction can never "
                        "be more than one"),
            "answer": "because 3 thirds fill a whole, and 8 holds two of those",
            "board": '[[numberline min="0" max="3" denom="3" hops="0,1,2,2.67" caption="8/3 = 2 whole ones and 2/3"]]',
        },
        "recap": [
            ("So, here it is again. A fraction can be bigger than one — it is a real "
             "place past the whole numbers. To find the whole ones, count how many "
             "times the bottom fits into the top; what is left is the fraction part.",
             '[[numberline min="0" max="3" denom="3" hops="0,1,2,2.67" caption="8/3 = 2 and 2/3"]]'),
            ("And that is how many pizzas seven slices really are.",
             '[[step eq="8 ÷ 3 = 2 whole ones, 2 left"]]'),
        ],
        "bank": [
            {"a": 7, "b": 3, "op": "imp"},
            {"a": 9, "b": 4, "op": "imp"},
            {"a": 11, "b": 5, "op": "imp"},
            {"a": 13, "b": 4, "op": "imp"},
            {"a": 17, "b": 5, "op": "imp"},
            {"a": 19, "b": 6, "op": "imp"},
            {"a": 23, "b": 7, "op": "imp"},
            {"a": 29, "b": 8, "op": "imp"},
            {"a": 25, "b": 6, "op": "imp"},
            {"a": 31, "b": 7, "op": "imp"},
        ],
    },
]
LESSONS.extend(_PREALGEBRA_U4)

# =============================================================================
# PREALGEBRA -- UNIT 5: DECIMALS (build ko, 2026-08-21)
# =============================================================================
# Basic Math NAMES tenths and hundredths and counts dimes and pennies. These four go
# past naming to the thing that actually goes wrong with decimals: place. Comparing
# two decimals is really converting them to a common unit, so lesson 1 does exactly
# that and the misconception dies where it lives -- 0.45 is 45 hundredths and 0.5 is
# FIFTY hundredths, which settles which is bigger without any rule about digits.
#
# EVERY ANSWER IS A COUNT OF PARTS -- "how many hundredths", "how many tenths". That
# is forced by the tap answer being a whole number, and it is also the honest way to
# hold a decimal in your head: 3.6 is thirty-six tenths, and sharing it between 4 is
# just sharing 36 things.
_PREALGEBRA_U5 = [
    {
        "id": "pre-u5-how-many-hundredths",
        "course": "prealgebra", "unit": 5,
        "topic": "How many hundredths",
        "op": "hun", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("decimal point", "hundredths"),
        "advance_line": "Three in a row, and you can say why — you've got it! Count a decimal as hundredths and you can compare any two.",
        "why": [
            ("Why count hundredths? Because money is hundredths — 0 point 3 7 dollars "
             "is 37 cents — and so are most measurements you will meet. And because "
             "decimals fool people: 0 point 3 7 has more digits than 0 point 6, and "
             "it is smaller. Counting hundredths is how you stop being fooled.",
             '[[goal text="How many hundredths"]]'),
        ],
        "picture": [
            ("Here is 0 point 3 7 on the hundred grid — one hundred little squares. "
             "Each full row is a tenth, ten squares. Three full rows are 30 squares, "
             "and 7 more squares on the next row. 30 plus 7: 37 hundredths.",
             '[[hundredgrid shaded="37" eq="0.37 = 37 hundredths" caption="3 full rows and 7 more: 37 hundredths"]]'),
        ],
        "teach": [
            ("That is how a decimal is built. A decimal point separates the whole "
             "ones from the parts. The first place after it counts tenths — full "
             "rows — and the second counts hundredths — single squares. Ten "
             "hundredths make one tenth, so any decimal can be counted as hundredths.",
             '[[hundredgrid shaded="37" caption="tenths are rows, hundredths are squares"]][[step eq="0.37 = 30 + 7 = 37 hundredths"]]'),
            ("Here is why that matters. Which is bigger, 0 point 6 or 0 point 3 7? "
             "Count them the same way: 0 point 6 is 60 hundredths, 0 point 3 7 is 37 "
             "hundredths. 60 beats 37. More digits do NOT mean a bigger number.",
             '[[hundredgrid shaded="60" caption="0.6 = 60 hundredths — six full rows"]][[step eq="0.6 = 60 hundredths · 0.37 = 37 hundredths"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 0 point 3 2. Three full rows "
                        "are 30 hundredths, put the 2 with them: 32 hundredths.",
                        '[[hundredgrid shaded="32" eq="0.32 = 32 hundredths" caption="3 rows and 2 more"]]'),
             "ask": {'a': 6, 'b': 7, 'op': 'hun'}},
            {"worked": ("One more together. 0 point 8 0. Eight full rows are 80 "
                        "hundredths, and there are no extra squares: 80 hundredths.",
                        '[[hundredgrid shaded="80" eq="0.80 = 80 hundredths" caption="8 full rows"]]'),
             "ask": {'a': 2, 'b': 9, 'op': 'hun'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 0 point 3 7 is 37 "
                       "hundredths. Tap the reason why."),
            "choices": ("because 3 tenths are 30 hundredths, and 7 more make 37 | "
                        "because 3 plus 7 is 10 | because two digits after the point "
                        "means 2 hundredths"),
            "answer": "because 3 tenths are 30 hundredths, and 7 more make 37",
            "board": '[[hundredgrid shaded="37" caption="3 full rows and 7 more: 37 hundredths"]]',
        },
        "recap": [
            ("So, here it is again. After the point, the first place is tenths — "
             "full rows on the grid — and the second is hundredths — single squares. "
             "Count any decimal as hundredths and you can compare it with any other.",
             '[[hundredgrid shaded="37" caption="0.37 = 37 hundredths"]]'),
            ("And that is why 0 point 6 beats 0 point 3 7, digits or no digits.",
             '[[step eq="0.6 = 60 hundredths · 0.37 = 37 hundredths"]]'),
        ],
        "bank": [
            {"a": 1, "b": 8, "op": "hun"},
            {"a": 2, "b": 5, "op": "hun"},
            {"a": 3, "b": 0, "op": "hun"},
            {"a": 4, "b": 0, "op": "hun"},
            {"a": 4, "b": 5, "op": "hun"},
            {"a": 5, "b": 0, "op": "hun"},
            {"a": 6, "b": 2, "op": "hun"},
            {"a": 7, "b": 0, "op": "hun"},
            {"a": 8, "b": 4, "op": "hun"},
            {"a": 9, "b": 6, "op": "hun"},
        ],
    },
    {
        "id": "pre-u5-times-by-ten",
        "course": "prealgebra", "unit": 5,
        "topic": "Timesing a decimal by ten",
        "op": "x10", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("decimal point", "place"),
        "advance_line": "Three in a row, and you can say why — you've got it! Times 10 moves every digit one place to the left.",
        "why": [
            ("Why times a decimal by ten? Because ten of something is everywhere. "
             "Ten pieces of rope each 3 point 7 metres. Ten boxes of 1 point 9 kilos. "
             "And there is a tidy move that does it without any long working, once "
             "you can see what the digits are doing.",
             '[[goal text="Timesing a decimal by ten"]]'),
        ],
        "picture": [
            ("Here is 3 point 7 on the place-value chart: 3 in the ones, 7 in the "
             "tenths — seven slices of one. Times 10, and every digit moves one place "
             "to the left. The 7 tenths become 7 ones. The 3 ones become 3 tens. "
             "Read the chart: 37.",
             '[[placevalue t="3" o="7" d="0" caption="3.7 × 10 = 37: every digit one place left"]]'),
        ],
        "teach": [
            ("That is the rule. Timesing by ten moves every digit one place to the "
             "left across the decimal point — the tenths become ones, the ones "
             "become tens. Nothing is dropped and nothing is invented.",
             '[[placevalue o="3" d="7" caption="3.7: three ones and seven tenths"]][[step eq="3.7 × 10 = 37"]]'),
            ("One more. 5 point 2 times 10 equals 52. Careful — the answer is not 50. "
             "The tenths digit moves too; it does not get left behind.",
             '[[placevalue t="5" o="2" d="0" caption="5.2 × 10 = 52 — the 2 moved too"]][[step eq="5.2 × 10 = 52"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 6 point 4 times 10. Both "
                        "digits move one place left: 64.",
                        '[[placevalue t="6" o="4" d="0" caption="6.4 × 10 = 64"]][[step eq="6.4 × 10 = 64"]]'),
             "ask": {'a': 7, 'b': 3, 'op': 'x10'}},
            {"worked": ("One more together. 1 point 9 times 10. Both digits move one "
                        "place left: 19.",
                        '[[placevalue t="1" o="9" d="0" caption="1.9 × 10 = 19"]][[step eq="1.9 × 10 = 19"]]'),
             "ask": {'a': 4, 'b': 6, 'op': 'x10'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 3 point 7 times 10 "
                       "equals 37. Tap the reason why."),
            "choices": ("because every digit moves one place to the left | because you "
                        "only times the whole number by 10 | because you put a zero on "
                        "the end"),
            "answer": "because every digit moves one place to the left",
            "board": '[[placevalue t="3" o="7" d="0" caption="3.7 × 10 = 37"]]',
        },
        "recap": [
            ("So, here it is again. Times 10 moves every digit one place to the left "
             "on the chart — tenths to ones, ones to tens. The tenths digit moves "
             "too.",
             '[[placevalue t="3" o="7" d="0" caption="3.7 × 10 = 37"]]'),
            ("And that is ten pieces of rope, with no long working at all.",
             '[[step eq="3.7 × 10 = 37"]]'),
        ],
        "bank": [
            {"a": 1, "b": 5, "op": "x10"},
            {"a": 2, "b": 3, "op": "x10"},
            {"a": 2, "b": 6, "op": "x10"},
            {"a": 3, "b": 6, "op": "x10"},
            {"a": 4, "b": 2, "op": "x10"},
            {"a": 5, "b": 1, "op": "x10"},
            {"a": 6, "b": 8, "op": "x10"},
            {"a": 7, "b": 4, "op": "x10"},
            {"a": 8, "b": 1, "op": "x10"},
            {"a": 9, "b": 9, "op": "x10"},
        ],
    },
    {
        "id": "pre-u5-tenths-times-a-number",
        "course": "prealgebra", "unit": 5,
        "topic": "Tenths times a whole number",
        "op": "dth", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("tenths", "times"),
        "advance_line": "Three in a row, and you can say why — you've got it! Count the tenths, times them, and they stay tenths.",
        "why": [
            ("Why tenths times a number? Because 0 point 3 of a kilo, four bags of "
             "it, is a real shopping question. A decimal looks hard to times — but "
             "say what it is a count of first, and it is the times table you already "
             "know.",
             '[[goal text="Tenths times a whole number"]]'),
        ],
        "picture": [
            ("Here is 0 point 3 times 4 on the tenths line. 0 point 3 is three "
             "tenths — one hop of 3 tenths. Four hops: 3 tenths, 6 tenths, 9 tenths, "
             "12 tenths. You land on 12 tenths, which is past one whole — 1 point 2.",
             '[[numberline min="0" max="2" denom="10" hops="0,0.3,0.6,0.9,1.2" caption="4 hops of 3 tenths = 12 tenths"]]'),
        ],
        "teach": [
            ("That is the method. Say the decimal as a count of tenths first. "
             "Timesing three tenths by 4 works exactly like timesing 3 by 4 — the "
             "parts just stay tenths. 3 times 4 equals 12, so the answer is 12 "
             "tenths.",
             '[[numberline min="0" max="2" denom="10" hops="0,0.3,0.6,0.9,1.2" caption="3 tenths × 4 = 12 tenths"]][[step eq="0.3 = 3 tenths"]][[step eq="3 tenths × 4 = 12 tenths"]]'),
            ("One more. 0 point 5 times 3. Five tenths, three hops: 5, 10, 15 tenths. "
             "Five tenths timesed by 3 equals 15 tenths.",
             '[[numberline min="0" max="2" denom="10" hops="0,0.5,1,1.5" caption="3 hops of 5 tenths = 15 tenths"]][[step eq="5 tenths × 3 = 15 tenths"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 0 point 2 times 7. Two tenths "
                        "times 7 equals 14 tenths — seven hops of 2 tenths.",
                        '[[numberline min="0" max="2" denom="10" hops="0,0.2,0.4,0.6,0.8,1,1.2,1.4" caption="7 hops of 2 tenths = 14 tenths"]][[step eq="2 tenths × 7 = 14 tenths"]]'),
             "ask": {'a': 6, 'b': 3, 'op': 'dth'}},
            {"worked": ("One more together. 0 point 8 times 6. Eight tenths times 6 "
                        "equals 48 tenths — six groups of 8 tenths.",
                        '[[array rows="6" cols="8" view="groups" eq="8 × 6 = 48" label="tenths" caption="6 groups of 8 tenths = 48 tenths"]][[step eq="8 tenths × 6 = 48 tenths"]]'),
             "ask": {'a': 7, 'b': 4, 'op': 'dth'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 0 point 3 times 4 "
                       "is 12 tenths. Tap the reason why."),
            "choices": ("because 3 tenths taken 4 times is 12 tenths | because 3 plus 4 "
                        "is 7 tenths | because tenths times a number turn into "
                        "hundredths"),
            "answer": "because 3 tenths taken 4 times is 12 tenths",
            "board": '[[numberline min="0" max="2" denom="10" hops="0,0.3,0.6,0.9,1.2" caption="4 hops of 3 tenths = 12 tenths"]]',
        },
        "recap": [
            ("So, here it is again. Say the decimal as tenths, times the tenths like "
             "whole numbers, and the answer stays in tenths.",
             '[[numberline min="0" max="2" denom="10" hops="0,0.3,0.6,0.9,1.2" caption="3 tenths × 4 = 12 tenths"]]'),
            ("And that is four bags of 0 point 3 of a kilo, using a times table you "
             "already know.",
             '[[step eq="3 tenths × 4 = 12 tenths"]]'),
        ],
        "bank": [
            {"a": 2, "b": 3, "op": "dth"},
            {"a": 3, "b": 3, "op": "dth"},
            {"a": 2, "b": 6, "op": "dth"},
            {"a": 4, "b": 4, "op": "dth"},
            {"a": 3, "b": 7, "op": "dth"},
            {"a": 5, "b": 5, "op": "dth"},
            {"a": 4, "b": 8, "op": "dth"},
            {"a": 6, "b": 7, "op": "dth"},
            {"a": 7, "b": 8, "op": "dth"},
            {"a": 9, "b": 9, "op": "dth"},
        ],
    },
    {
        "id": "pre-u5-sharing-a-decimal",
        "course": "prealgebra", "unit": 5,
        "topic": "Sharing a decimal out",
        "op": "dsh", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("tenths", "shared"),
        "advance_line": "Three in a row, and you can say why — you've got it! Count the tenths, share them, and they stay tenths.",
        "why": [
            ("Why share a decimal? Because 3 point 6 litres of juice into 4 bottles "
             "is a real question, and so is a bill split four ways. Sharing a decimal "
             "works the same way as timesing one: say what it is a count of first, "
             "and it is sharing you already know.",
             '[[goal text="Sharing a decimal out"]]'),
        ],
        "picture": [
            ("Here is 3 point 6 as tenths: thirty-six tenths, thirty-six dots. Share "
             "them into 4 equal groups — deal them out — and every group gets 9. "
             "Nine tenths each, which is 0 point 9.",
             '[[array rows="4" cols="9" view="groups" eq="36 ÷ 4 = 9" label="tenths" caption="36 tenths shared 4 ways: 9 tenths each"]]'),
        ],
        "teach": [
            ("That is the method. Say the decimal as a count of tenths — 3 point 6 "
             "is 36 tenths. Sharing 36 tenths between 4 is just sharing 36 things "
             "between 4, and the shares stay tenths.",
             '[[array rows="4" cols="9" view="groups" eq="36 ÷ 4 = 9" label="tenths" caption="the shares stay tenths"]][[step eq="3.6 = 36 tenths"]][[step eq="36 ÷ 4 = 9 tenths"]]'),
            ("One more. 2 point 4 shared between 3. Twenty-four tenths between 3 "
             "gives 8 tenths each, which is 0 point 8.",
             '[[array rows="3" cols="8" view="groups" eq="24 ÷ 3 = 8" label="tenths" caption="24 tenths shared 3 ways: 8 tenths each"]][[step eq="24 tenths ÷ 3 = 8 tenths"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 4 point 8 shared between 6. "
                        "Forty-eight tenths between 6 gives 8 tenths each.",
                        '[[array rows="6" cols="8" view="groups" eq="48 ÷ 6 = 8" label="tenths" caption="48 tenths shared 6 ways: 8 tenths each"]][[step eq="48 tenths ÷ 6 = 8 tenths"]]'),
             "ask": {'a': 9, 'b': 0, 'c': 5, 'op': 'dsh'}},
            {"worked": ("One more together. 1 point 2 shared between 4. Twelve tenths "
                        "between 4 gives 3 tenths each.",
                        '[[array rows="4" cols="3" view="groups" eq="12 ÷ 4 = 3" label="tenths" caption="12 tenths shared 4 ways: 3 tenths each"]][[step eq="12 tenths ÷ 4 = 3 tenths"]]'),
             "ask": {'a': 7, 'b': 7, 'c': 7, 'op': 'dsh'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 3 point 6 shared "
                       "between 4 is 9 tenths each. Tap the reason why."),
            "choices": ("because 36 tenths shared 4 ways is 9 tenths each | because 3 "
                        "divided by 4 is about 1 | because you share the 6 and keep "
                        "the 3"),
            "answer": "because 36 tenths shared 4 ways is 9 tenths each",
            "board": '[[array rows="4" cols="9" view="groups" eq="36 ÷ 4 = 9" label="tenths" caption="36 tenths shared 4 ways"]]',
        },
        "recap": [
            ("So, here it is again. Say the decimal as tenths, share the tenths like "
             "whole things, and the shares stay tenths.",
             '[[array rows="4" cols="9" view="groups" eq="36 ÷ 4 = 9" label="tenths" caption="36 tenths shared 4 ways: 9 tenths each"]]'),
            ("And that is the juice into four bottles, and the bill split four ways.",
             '[[step eq="36 tenths ÷ 4 = 9 tenths"]]'),
        ],
        "bank": [
            {"a": 1, "b": 5, "c": 5, "op": "dsh"},
            {"a": 2, "b": 8, "c": 7, "op": "dsh"},
            {"a": 1, "b": 6, "c": 2, "op": "dsh"},
            {"a": 5, "b": 6, "c": 7, "op": "dsh"},
            {"a": 2, "b": 7, "c": 3, "op": "dsh"},
            {"a": 5, "b": 4, "c": 6, "op": "dsh"},
            {"a": 6, "b": 3, "c": 7, "op": "dsh"},
            {"a": 7, "b": 2, "c": 8, "op": "dsh"},
            {"a": 8, "b": 1, "c": 9, "op": "dsh"},
            {"a": 4, "b": 5, "c": 5, "op": "dsh"},
        ],
    },
]
LESSONS.extend(_PREALGEBRA_U5)


# =============================================================================
# PREALGEBRA -- UNIT 6: RATIOS, RATES & PROPORTIONS (build kp, 2026-08-21)
# =============================================================================
# Basic Math's "one costs" already finds a unit PRICE. These four are the family of
# ideas around it, in the order they depend on each other: keep a ratio's shape when
# both sides grow, scale a rate over time (which is that same move with a unit step in
# the middle), write it as an equation with a hole in it, and finally SPLIT an amount
# in a ratio -- the genuinely different one, because there the total is given and the
# parts have to be found before anything can be shared.
#
# THE ERROR THIS WHOLE UNIT IS ABOUT is adding instead of timesing: a child who thinks
# 2 to 3 grown to 4 becomes "4 to 5", because 3 was one more than 2. Three of the four
# lessons offer exactly that as their wrong option.
_PREALGEBRA_U6 = [
    {
        "id": "pre-u6-keeping-a-ratio",
        "course": "prealgebra", "unit": 6,
        "topic": "Keeping a ratio the same",
        "op": "rat", "max_value": 60,
        "levels": ("abstract",),
        "symbols": ("ratio", "for every"),
        "advance_line": "Three in a row, and you can say why — you've got it! Both sides grow by timesing, never by adding.",
        "why": [
            ("Why keep a ratio? Because a recipe for four people has to feed twelve "
             "and still taste right. Paint mixed 2 parts blue to 3 parts white has to "
             "come out the same shade in a bigger tin. A ratio says how two amounts "
             "go together — and growing one means growing the other the same way.",
             '[[goal text="Keeping a ratio the same"]]'),
        ],
        "picture": [
            ("Here is the ratio 2 to 3 as a bar: 2 cups of flour beside 3 cups of "
             "milk, one batch. Now 6 cups of flour — that is 3 batches, because 6 "
             "divided by 2 equals 3. The milk grows the same way: 3 batches of 3 "
             "cups is 9. The second bar is the first one, timesed by 3 on both sides.",
             '[[tape parts="2 | 3" caption="one batch: flour 2 : milk 3"]][[tape parts="6 | 9" caption="3 batches: 6 : 9 — both sides times 3"]]'),
        ],
        "teach": [
            ("That is the rule. A ratio is written 2 to 3 — 2 cups for every 3. To keep it the same when "
             "you make more, BOTH sides have to grow the same way — by timesing, not "
             "by adding. Find how many batches, then times the other side by that.",
             '[[tape parts="2 | 3" caption="2 : 3"]][[step eq="6 ÷ 2 = 3 batches"]][[step eq="3 × 3 = 9"]]'),
            ("Careful with the tempting wrong move. 6 cups of flour does NOT mean 7 "
             "cups of milk just because 3 is one more than 2. Adding breaks the "
             "ratio; timesing keeps it.",
             '[[step eq="2 : 3 → 6 : 9 ✓"]][[step eq="2 : 3 → 6 : 7 ✗"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 3 cups of flour for every 4 "
                        "of milk, with 9 cups of flour. 9 divided by 3 equals 3 "
                        "batches, and 3 times 4 equals 12 cups of milk.",
                        '[[tape parts="3 | 4" caption="one batch: 3 : 4"]][[tape parts="9 | 12" caption="3 batches: 9 : 12"]][[step eq="9 ÷ 3 = 3"]][[step eq="3 × 4 = 12"]]'),
             "ask": {'a': 5, 'b': 6, 'c': 15, 'op': 'rat'}},
            {"worked": ("One more together. 2 to 9, with 8 cups of flour. 8 divided by "
                        "2 equals 4 batches, and 4 times 9 equals 36.",
                        '[[tape parts="2 | 9" caption="one batch: 2 : 9"]][[tape parts="8 | 36" caption="4 batches: 8 : 36"]][[step eq="8 ÷ 2 = 4"]][[step eq="4 × 9 = 36"]]'),
             "ask": {'a': 3, 'b': 7, 'c': 9, 'op': 'rat'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 2 to 3, with 6 "
                       "cups of flour, needs 9 cups of milk. Tap the reason why."),
            "choices": ("because both sides were timesed by 3 | because 3 is one more "
                        "than 2, so 6 needs 7 | because you add 3 cups of milk for "
                        "every batch of flour"),
            "answer": "because both sides were timesed by 3",
            "board": '[[tape parts="2 | 3" caption="one batch: 2 : 3"]][[tape parts="6 | 9" caption="3 batches: 6 : 9"]]',
        },
        "recap": [
            ("So, here it is again. To keep a ratio the same, both sides grow by the "
             "same times. Find how many batches, then times the other side by that "
             "— never add.",
             '[[tape parts="2 | 3" caption="2 : 3"]][[tape parts="6 | 9" caption="6 : 9 — both sides times 3"]]'),
            ("And that is a recipe for twelve that still tastes right.",
             '[[step eq="2 : 3 = 6 : 9"]]'),
        ],
        "bank": [
            {"a": 5, "b": 2, "c": 10, "op": "rat"},
            {"a": 2, "b": 3, "c": 4, "op": "rat"},
            {"a": 4, "b": 3, "c": 8, "op": "rat"},
            {"a": 3, "b": 4, "c": 6, "op": "rat"},
            {"a": 2, "b": 5, "c": 6, "op": "rat"},
            {"a": 3, "b": 5, "c": 9, "op": "rat"},
            {"a": 4, "b": 5, "c": 12, "op": "rat"},
            {"a": 6, "b": 5, "c": 18, "op": "rat"},
            {"a": 2, "b": 7, "c": 8, "op": "rat"},
            {"a": 3, "b": 8, "c": 12, "op": "rat"},
        ],
    },
    {
        "id": "pre-u6-scaling-a-rate",
        "course": "prealgebra", "unit": 6,
        "topic": "Working out a rate",
        "op": "rte", "max_value": 90,
        "levels": ("abstract",),
        "symbols": ("rate", "per hour"),
        "advance_line": "Three in a row, and you can say why — you've got it! Find one hour first, then times.",
        "why": [
            ("Why work out a rate? Because a rate is how the world prices things — "
             "bottles an hour, miles an hour, dollars an hour. Know what happens in "
             "ONE hour and you can answer any number of hours. Skip that step and "
             "you are guessing.",
             '[[goal text="Working out a rate"]]'),
        ],
        "picture": [
            ("Here are 18 bottles shared over 3 hours — one row for each hour. Deal "
             "them out and every hour gets 6: 18 divided by 3 equals 6 bottles an "
             "hour. Now 4 hours of that: four rows of 6 is 24 bottles.",
             '[[array rows="3" cols="6" view="groups" eq="18 ÷ 3 = 6" label="hours" caption="6 bottles an hour"]][[array rows="4" cols="6" view="groups" eq="6 × 4 = 24" label="hours" caption="4 hours: 24 bottles"]]'),
        ],
        "teach": [
            ("That is the method, and it is two steps, always in that order. Divide "
             "to reach ONE hour — that single number is the rate. Then times to reach "
             "the hours you were asked about. Stopping after the divide leaves you "
             "holding the rate, not the answer.",
             '[[array rows="3" cols="6" view="groups" eq="18 ÷ 3 = 6" label="hours" caption="divide to reach one hour"]][[step eq="18 ÷ 3 = 6 per hour"]][[step eq="6 × 4 = 24"]]'),
            ("One more. 30 bottles in 5 hours, and you want 7 hours. One hour first: "
             "30 divided by 5 equals 6. Then 7 hours: 6 times 7 equals 42.",
             '[[array rows="5" cols="6" view="groups" eq="30 ÷ 5 = 6" label="hours" caption="6 an hour"]][[step eq="6 × 7 = 42"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 24 bottles in 4 hours. That is "
                        "6 an hour, and in 3 hours it fills 18.",
                        '[[array rows="4" cols="6" view="groups" eq="24 ÷ 4 = 6" label="hours" caption="6 an hour"]][[step eq="6 × 3 = 18"]]'),
             "ask": {'a': 4, 'b': 5, 'c': 20, 'op': 'rte'}},
            {"worked": ("One more together. 40 bottles in 5 hours is 8 an hour, so in 3 "
                        "hours it fills 24.",
                        '[[array rows="5" cols="8" view="groups" eq="40 ÷ 5 = 8" label="hours" caption="8 an hour"]][[step eq="8 × 3 = 24"]]'),
             "ask": {'a': 6, 'b': 3, 'c': 21, 'op': 'rte'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 18 bottles in 3 "
                       "hours means 24 bottles in 4 hours. Tap the reason why."),
            "choices": ("because one hour is 6 bottles, and 4 hours is 4 sixes | "
                        "because 4 hours is one more hour, so add one bottle | because "
                        "18 plus 4 is 22, which rounds to 24"),
            "answer": "because one hour is 6 bottles, and 4 hours is 4 sixes",
            "board": '[[array rows="4" cols="6" view="groups" eq="6 × 4 = 24" label="hours" caption="4 hours of 6 an hour"]]',
        },
        "recap": [
            ("So, here it is again. Divide to reach one hour — that is the rate. "
             "Then times by the hours you were asked about. Two steps, that order.",
             '[[array rows="3" cols="6" view="groups" eq="18 ÷ 3 = 6" label="hours" caption="18 ÷ 3 = 6 an hour, then 6 × 4 = 24"]]'),
            ("And that is how every price per hour, and every speed, gets used.",
             '[[step eq="18 ÷ 3 = 6 · 6 × 4 = 24"]]'),
        ],
        "bank": [
            {"a": 2, "b": 3, "c": 12, "op": "rte"},
            {"a": 3, "b": 4, "c": 20, "op": "rte"},
            {"a": 3, "b": 7, "c": 35, "op": "rte"},
            {"a": 2, "b": 5, "c": 40, "op": "rte"},
            {"a": 4, "b": 2, "c": 10, "op": "rte"},
            {"a": 4, "b": 9, "c": 45, "op": "rte"},
            {"a": 5, "b": 3, "c": 18, "op": "rte"},
            {"a": 6, "b": 4, "c": 24, "op": "rte"},
            {"a": 8, "b": 5, "c": 30, "op": "rte"},
            {"a": 7, "b": 6, "c": 42, "op": "rte"},
        ],
    },
    {
        "id": "pre-u6-filling-in-a-proportion",
        "course": "prealgebra", "unit": 6,
        "topic": "Filling in a proportion",
        "op": "prop", "max_value": 60,
        "levels": ("abstract",),
        "symbols": ("proportion", "over"),
        "advance_line": "Three in a row, and you can say why — you've got it! Whatever happened to the bottom happened to the top.",
        "why": [
            ("Why proportions? Because 3 out of 4 and 6 out of 8 are the same share "
             "— the same slice of pie, cut finer. You move between them all the "
             "time: making a photo bigger, reading a map, scaling a recipe. A "
             "proportion is two fractions worth the same, and one of them has a hole.",
             '[[goal text="Filling in a proportion"]]'),
        ],
        "picture": [
            ("Here are two pies. The first is cut into 4 with 3 shaded — three "
             "fourths. The second is cut into 8. To hold the same amount, how many "
             "eighths? Every fourth became two eighths, so 3 fourths became 6 "
             "eighths. 3 over 4 equals 6 over 8.",
             '[[pie parts="4" shaded="3" caption="3/4"]][[pie parts="8" shaded="6" caption="6/8 — the same amount, cut finer"]]'),
        ],
        "teach": [
            ("That is the rule, and it works exactly like the ratio rule: whatever "
             "happened to the bottom happened to the top. The bottom went from 4 to "
             "8 — timesed by 2. So the top is timesed by 2: 3 times 2 equals 6.",
             '[[pie parts="4" shaded="3" caption="3/4"]][[pie parts="8" shaded="6" caption="6/8"]][[step eq="3/4 = ?/8"]][[step eq="4 × 2 = 8, so 3 × 2 = 6"]]'),
            ("Watch out for adding. The bottom went up by 4, but that does NOT mean "
             "the top goes up by 4. 3 over 4 is not 7 over 8. Ask what the bottom was "
             "TIMESED by, every time.",
             '[[step eq="3/4 = 6/8 ✓"]][[step eq="3/4 = 7/8 ✗"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 2 over 5 equals what over 10? "
                        "The bottom doubled, so the top doubles: 4.",
                        '[[pie parts="5" shaded="2" caption="2/5"]][[pie parts="10" shaded="4" caption="4/10 — the same amount"]][[step eq="2/5 = 4/10"]]'),
             "ask": {'a': 5, 'b': 3, 'c': 9, 'op': 'prop'}},
            {"worked": ("One more together. 3 over 5 equals what over 15? The bottom "
                        "was timesed by 3, so 3 times 3 equals 9.",
                        '[[solve start="3/5 = ?/15" steps="the bottom : 5 × 3 = 15 | so the top : 3 × 3 = 9" caption="3/5 = 9/15"]]'),
             "ask": {'a': 2, 'b': 9, 'c': 27, 'op': 'prop'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 3 over 4 equals 6 "
                       "over 8. Tap the reason why."),
            "choices": ("because the bottom was timesed by 2, so the top is too | "
                        "because 4 went up by 4, so 3 goes up by 4 | because 6 over 8 "
                        "is bigger than 3 over 4"),
            "answer": "because the bottom was timesed by 2, so the top is too",
            "board": '[[pie parts="4" shaded="3" caption="3/4"]][[pie parts="8" shaded="6" caption="6/8 — the same amount"]]',
        },
        "recap": [
            ("So, here it is again. Two fractions worth the same amount are a "
             "proportion. Whatever the bottom was timesed by, times the top by the "
             "same — never add.",
             '[[pie parts="4" shaded="3" caption="3/4"]][[pie parts="8" shaded="6" caption="6/8"]]'),
            ("And that is the same slice, cut finer — a photo made bigger, a map "
             "read right.",
             '[[step eq="3/4 = 6/8"]]'),
        ],
        "bank": [
            {"a": 2, "b": 3, "c": 6, "op": "prop"},
            {"a": 2, "b": 4, "c": 8, "op": "prop"},
            {"a": 2, "b": 7, "c": 14, "op": "prop"},
            {"a": 2, "b": 3, "c": 9, "op": "prop"},
            {"a": 3, "b": 8, "c": 16, "op": "prop"},
            {"a": 4, "b": 9, "c": 18, "op": "prop"},
            {"a": 3, "b": 4, "c": 12, "op": "prop"},
            {"a": 5, "b": 6, "c": 12, "op": "prop"},
            {"a": 4, "b": 3, "c": 9, "op": "prop"},
            {"a": 7, "b": 4, "c": 20, "op": "prop"},
        ],
    },
    {
        "id": "pre-u6-sharing-in-a-ratio",
        "course": "prealgebra", "unit": 6,
        "topic": "Sharing in a ratio",
        "op": "shr", "max_value": 60,
        "levels": ("abstract",),
        "symbols": ("ratio", "parts"),
        "advance_line": "Three in a row, and you can say why — you've got it! Count the parts first, then share.",
        "why": [
            ("Why share in a ratio? Because fair is not always equal. Two friends "
             "split prize money 2 to 3 because one did more of the work. A bill is "
             "shared by who ate what. You are given the whole amount and the ratio, "
             "and you have to find each share.",
             '[[goal text="Sharing in a ratio"]]'),
        ],
        "picture": [
            ("Here are 20 sweets as a bar, shared in the ratio 2 to 3. Count the parts "
             "first: 2 and 3 are 5 parts, so the bar is cut into 5. 20 divided by 5 "
             "equals 4 in each part. The first share is 2 parts — 8; the second is 3 "
             "parts — 12. And 8 plus 12 is the 20 you started with.",
             '[[tape parts="4 | 4 | 4 | 4 | 4" total="20" caption="5 parts of 4"]][[tape parts="8 | 12" total="20" caption="2 parts : 3 parts = 8 : 12"]]'),
        ],
        "teach": [
            ("That is the method. A ratio of 2 to 3 means 5 parts in all — not 2 and "
             "not 3. Count the parts, share the amount by that count to find one "
             "part, then give each side its parts.",
             '[[tape parts="4 | 4 | 4 | 4 | 4" total="20" caption="2 + 3 = 5 parts"]][[step eq="20 ÷ 5 = 4 each part"]][[step eq="4 × 2 = 8"]]'),
            ("Check it the easy way: the other share is 3 parts, which is 12. And 8 "
             "plus 12 equals 20, the amount you started with. If the two shares do "
             "not put back together, something went wrong.",
             '[[tape parts="8 | 12" total="20" caption="8 + 12 = 20 ✓"]][[step eq="8 + 12 = 20 ✓"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Share 12 in the ratio 1 to 3. "
                        "That is 4 parts, so each part is 3. The first share is 1 part "
                        "— 3.",
                        '[[tape parts="3 | 9" total="12" caption="1 part : 3 parts = 3 : 9"]][[step eq="12 ÷ 4 = 3"]][[step eq="3 × 1 = 3"]]'),
             "ask": {'a': 3, 'b': 4, 'c': 28, 'op': 'shr'}},
            {"worked": ("One more together. Share 30 in the ratio 2 to 4. Six parts, so "
                        "each part is 5, and the first share is 2 parts — 10.",
                        '[[tape parts="10 | 20" total="30" caption="2 parts : 4 parts = 10 : 20"]][[step eq="30 ÷ 6 = 5"]][[step eq="5 × 2 = 10"]]'),
             "ask": {'a': 5, 'b': 2, 'c': 35, 'op': 'shr'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Sharing 20 in the "
                       "ratio 2 to 3 gives the first share 8. Tap the reason why."),
            "choices": ("because 5 parts of 4 each, and the first share is 2 | "
                        "because you share 20 by the first number, 2 | because the "
                        "first share is always the smaller half"),
            "answer": "because 5 parts of 4 each, and the first share is 2",
            "board": '[[tape parts="8 | 12" total="20" caption="2 parts : 3 parts = 8 : 12"]]',
        },
        "recap": [
            ("So, here it is again. Count the parts first — the two numbers of the "
             "ratio added. Share the amount by that count to find one part, then "
             "give each side its parts, and check they put back together.",
             '[[tape parts="8 | 12" total="20" caption="20 ÷ 5 = 4 · 4 × 2 = 8 · 4 × 3 = 12"]]'),
            ("And that is prize money split fairly, and a bill shared by who ate "
             "what.",
             '[[step eq="8 + 12 = 20"]]'),
        ],
        "bank": [
            {"a": 2, "b": 3, "c": 10, "op": "shr"},
            {"a": 2, "b": 5, "c": 14, "op": "shr"},
            {"a": 2, "b": 7, "c": 27, "op": "shr"},
            {"a": 3, "b": 2, "c": 15, "op": "shr"},
            {"a": 3, "b": 5, "c": 24, "op": "shr"},
            {"a": 4, "b": 3, "c": 21, "op": "shr"},
            {"a": 5, "b": 4, "c": 27, "op": "shr"},
            {"a": 4, "b": 5, "c": 36, "op": "shr"},
            {"a": 5, "b": 3, "c": 32, "op": "shr"},
            {"a": 7, "b": 3, "c": 50, "op": "shr"},
        ],
    },
]
LESSONS.extend(_PREALGEBRA_U6)


# =============================================================================
# PREALGEBRA -- UNIT 7: PERCENTS (build kr, 2026-08-21)
# =============================================================================
# Basic Math's percent lesson only ever asks for 10, 25 or 50 percent, and it answers
# them with a fraction shortcut: half, a fourth, a tenth. That shortcut is fine and it
# is also a dead end -- it says nothing at all about 30 percent or 70 percent. This
# unit replaces it with ONE method that never runs out: find ten percent, then count
# how many tens you need. Lesson 1 teaches the method; lessons 2, 3 and 4 run it in
# the other three directions a percent question can face.
#
# THE ERROR THE LAST LESSON IS ABOUT is moving a price by the PERCENT NUMBER instead
# of by that percent OF the price -- 40 dollars up 10 percent read as 50 dollars,
# because 40 and 10 are two numbers and adding them is the thing a child knows how to
# do. It is offered as the wrong tap on every problem in that bank.
_PREALGEBRA_U7 = [
    {
        "id": "pre-u7-any-percent",
        "course": "prealgebra", "unit": 7,
        "topic": "Any percent, ten at a time",
        "op": "pcn", "max_value": 90,
        "levels": ("abstract",),
        "symbols": ("percent", "of"),
        "advance_line": "Three in a row, and you can say why — you've got it! Ten percent first, then count the tens.",
        "why": [
            ("Why any percent? Because you already know 50 percent is half and 10 "
             "percent is a tenth — but sale signs say 30 percent off, and a test says "
             "70 percent. Half and a fourth are no help there. Here is one way that "
             "works for every percent of every number.",
             '[[goal text="Any percent, ten at a time"]]'),
        ],
        "picture": [
            ("Here is 40 as a bar, cut into ten equal parts. Each part is 4 — that is "
             "ten percent of 40. Now 30 percent: 30 is three tens, so take three of "
             "those parts. 3 times 4 equals 12. The second bar shows the 12 taken and "
             "the 28 left.",
             '[[tape parts="4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4" total="40" caption="ten parts of 4 — 10% each"]][[tape parts="12 | 28" total="40" caption="3 parts: 30% of 40 = 12"]]'),
        ],
        "teach": [
            ("That is the method. Find TEN percent first, because that is easy — just "
             "a tenth. Then count how many tens the percent is, and times. 30 percent "
             "of 40: ten percent is 4, 30 is three tens, 3 times 4 equals 12.",
             '[[tape parts="4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4" total="40" caption="10% of 40 is one part — 4"]][[step eq="10% of 40 = 4"]][[step eq="30% is 3 tens"]][[step eq="3 × 4 = 12"]]'),
            ("One more, and the trap. 70 percent of 20. Ten percent of 20 is 2. "
             "Seventy percent is seven tens, so 7 times 2 equals 14. Careful — the "
             "answer is not 2. Finding ten percent is only the first of the two steps.",
             '[[tape parts="2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2" total="20" caption="ten parts of 2"]][[step eq="10% of 20 = 2"]][[step eq="7 × 2 = 14 ✓"]][[step eq="2 ✗ — that is only ten percent"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 20 percent of 50. Ten percent "
                        "of 50 is 5, and 20 percent is two tens: 2 times 5 equals 10.",
                        '[[tape parts="5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5" total="50" caption="ten parts of 5"]][[step eq="10% of 50 = 5"]][[step eq="2 × 5 = 10"]]'),
             "ask": {'a': 90, 'b': 10, 'op': 'pcn'}},
            {"worked": ("One more together. 80 percent of 40. Ten percent of 40 is 4, "
                        "and eight of those is 8 times 4, which equals 32.",
                        '[[tape parts="32 | 8" total="40" caption="8 parts of 4: 80% of 40 = 32"]][[step eq="10% of 40 = 4"]][[step eq="8 × 4 = 32"]]'),
             "ask": {'a': 40, 'b': 80, 'op': 'pcn'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 30 percent of 40 "
                       "is 12. Tap the reason why."),
            "choices": ("because 10 percent is 4, and 30 percent is 3 of those | "
                        "because 10 percent of 40 is 4, so the answer is 4 | because "
                        "30 percent of every number is 12"),
            "answer": "because 10 percent is 4, and 30 percent is 3 of those",
            "board": '[[tape parts="12 | 28" total="40" caption="3 parts of 4: 30% of 40 = 12"]]',
        },
        "recap": [
            ("So, here it is again. Any percent of any number: find ten percent "
             "first — a tenth — then count how many tens the percent is, and times "
             "by that. Two steps, and the first one is not the answer.",
             '[[tape parts="4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4" total="40" caption="10% of 40 = 4 · 30% = 3 × 4 = 12"]]'),
            ("And that is the sale sign read, and the test score understood.",
             '[[step eq="30% of 40 = 12"]]'),
        ],
        "bank": [
            {"a": 20, "b": 20, "op": "pcn"},
            {"a": 30, "b": 20, "op": "pcn"},
            {"a": 20, "b": 40, "op": "pcn"},
            {"a": 30, "b": 30, "op": "pcn"},
            {"a": 40, "b": 30, "op": "pcn"},
            {"a": 60, "b": 20, "op": "pcn"},
            {"a": 30, "b": 60, "op": "pcn"},
            {"a": 40, "b": 60, "op": "pcn"},
            {"a": 60, "b": 60, "op": "pcn"},
            {"a": 70, "b": 80, "op": "pcn"},
        ],
    },
    {
        "id": "pre-u7-what-percent-is-that",
        "course": "prealgebra", "unit": 7,
        "topic": "What percent is that",
        "op": "asp", "max_value": 100,
        "levels": ("abstract",),
        "symbols": ("percent", "out of"),
        "advance_line": "Three in a row, and you can say why — you've got it! Percent means out of a hundred.",
        "why": [
            ("Why turn a score into a percent? Because 15 out of 20 on one test and 21 "
             "out of 30 on another cannot be compared as they stand. Percent means out "
             "of a hundred — put both scores out of a hundred and you can see which is "
             "better at a glance.",
             '[[goal text="What percent is that"]]'),
        ],
        "picture": [
            ("Here is 15 out of 20 as a bar: 15 shaded, 5 not. And here is the same "
             "share on the hundred grid: 75 squares out of 100. The bottom went from "
             "20 to 100 — timesed by 5 — so the top went from 15 to 75. 15 out of 20 "
             "is 75 percent.",
             '[[tape parts="15 | 5" total="20" caption="15 out of 20"]][[hundredgrid shaded="75" unit="percent" caption="75 out of 100 — the same share"]]'),
        ],
        "teach": [
            ("That is the method, and it is the proportion you already know, with "
             "100 on the bottom. 15 out of 20 equals what out of 100? Look at the "
             "bottoms: 20 became 100, so it was timesed by 5. Do the same to the top: "
             "15 times 5 equals 75. So 15 out of 20 is 75 percent.",
             '[[step eq="15/20 = ?/100"]][[step eq="20 × 5 = 100, so 15 × 5 = 75"]][[hundredgrid shaded="75" unit="percent" caption="75%"]]'),
            ("Watch which number you answer with. 15 out of 20 is 75 percent — not "
             "15 percent, and not 25 percent. 25 is the percent of the ones you did "
             "NOT have. One more: 2 out of 5. The bottom 5 becomes 100 by timesing "
             "by 20, so the top does too: 2 times 20 equals 40 percent.",
             '[[step eq="15 out of 20 = 75% ✓"]][[step eq="the other 5 are the 25% ✗"]][[step eq="2/5 = 40/100"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 11 out of 20. Times both by 5: "
                        "11 times 5 equals 55, so that is 55 percent.",
                        '[[tape parts="11 | 9" total="20" caption="11 out of 20"]][[hundredgrid shaded="55" unit="percent" caption="55 out of 100"]][[step eq="11/20 = 55/100"]]'),
             "ask": {'a': 4, 'b': 10, 'op': 'asp'}},
            {"worked": ("One more together. 6 out of 25. The bottom 25 becomes 100 by "
                        "timesing by 4, so the top does too: 6 times 4 equals 24 percent.",
                        '[[tape parts="6 | 19" total="25" caption="6 out of 25"]][[hundredgrid shaded="24" unit="percent" caption="24 out of 100"]][[step eq="6/25 = 24/100"]]'),
             "ask": {'a': 22, 'b': 40, 'op': 'asp'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 15 out of 20 is "
                       "75 percent. Tap the reason why."),
            "choices": ("because the bottom was timesed by 5, so the top is too | "
                        "because 15 out of 20 means 15 percent, near enough | because "
                        "the 5 you did not have is what you count"),
            "answer": "because the bottom was timesed by 5, so the top is too",
            "board": '[[tape parts="15 | 5" total="20" caption="15 out of 20"]][[hundredgrid shaded="75" unit="percent" caption="75 out of 100"]]',
        },
        "recap": [
            ("So, here it is again. Percent means out of a hundred. Put the share out "
             "of 100: whatever the bottom was timesed by to reach 100, times the top "
             "by the same. And answer with the part you HAD, not the part you missed.",
             '[[tape parts="15 | 5" total="20" caption="15 out of 20"]][[hundredgrid shaded="75" unit="percent" caption="15/20 = 75/100"]]'),
            ("And that is two test scores, compared at a glance.",
             '[[step eq="15/20 = 75%"]]'),
        ],
        "bank": [
            {"a": 1, "b": 10, "op": "asp"},
            {"a": 1, "b": 4, "op": "asp"},
            {"a": 3, "b": 10, "op": "asp"},
            {"a": 9, "b": 20, "op": "asp"},
            {"a": 13, "b": 20, "op": "asp"},
            {"a": 17, "b": 25, "op": "asp"},
            {"a": 7, "b": 10, "op": "asp"},
            {"a": 3, "b": 4, "op": "asp"},
            {"a": 21, "b": 25, "op": "asp"},
            {"a": 19, "b": 20, "op": "asp"},
        ],
    },
    {
        "id": "pre-u7-finding-the-whole",
        "course": "prealgebra", "unit": 7,
        "topic": "Finding the whole from a part",
        "op": "pwh", "max_value": 100,
        "levels": ("abstract",),
        "symbols": ("percent", "whole"),
        "advance_line": "Three in a row, and you can say why — you've got it! Step down to ten percent, then up to the whole.",
        "why": [
            ("Why find the whole? Because sometimes the whole is what is missing. A "
             "shop says 12 dollars is 30 percent off — what was the full price? A "
             "class says 12 students is 30 percent of the school — how big is the "
             "school? You are told a part and its percent, and the whole is the "
             "question.",
             '[[goal text="Finding the whole from a part"]]'),
        ],
        "picture": [
            ("Here is the whole as a bar cut into ten equal parts — ten percent each. "
             "30 percent is three of those parts, and those three parts are the 12. "
             "So one part is 12 divided by 3, which equals 4, and all ten parts are "
             "4 times 10, which equals 40. The whole is 40.",
             '[[tape parts="4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4" total="40" caption="ten parts of 4 — 3 of them are the 12"]][[tape parts="12 | 28" total="40" caption="30% of 40 = 12"]]'),
        ],
        "teach": [
            ("That is the method — the same ten-percent step, walked in the other "
             "direction. 30 percent is 12. Step DOWN to ten percent first: 30 percent "
             "is three tens, so ten percent is 12 divided by 3, which equals 4. Now "
             "step up: one hundred percent is ten of those, and 4 times 10 equals 40.",
             '[[tape parts="12 | ?" total="?" caption="12 is 30% — the whole is the question"]][[step eq="30% = 12"]][[step eq="10% = 12 ÷ 3 = 4"]][[step eq="100% = 4 × 10 = 40"]]'),
            ("Check it the easy way: is 30 percent of 40 really 12? Ten percent of 40 "
             "is 4, and three tens is 3 times 4, which equals 12. It fits. And notice "
             "the whole is BIGGER than the part — if your answer came out smaller, you "
             "ran the sum forwards by mistake.",
             '[[step eq="30% of 40 = 12 ✓"]][[step eq="40 is bigger than 12 ✓"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 24 is 40 percent of what? Ten "
                        "percent is 24 divided by 4, which equals 6, and a hundred "
                        "percent is 6 times 10, which equals 60.",
                        '[[tape parts="6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6" total="60" caption="ten parts of 6 — 4 of them are the 24"]][[step eq="10% = 24 ÷ 4 = 6"]][[step eq="100% = 6 × 10 = 60"]]'),
             "ask": {'a': 30, 'b': 9, 'op': 'pwh'}},
            {"worked": ("One more together. 21 is 70 percent of what? Ten percent is 21 "
                        "divided by 7, which equals 3, so the whole is 3 times 10, which "
                        "equals 30.",
                        '[[tape parts="21 | 9" total="30" caption="70% of 30 = 21"]][[step eq="10% = 21 ÷ 7 = 3"]][[step eq="100% = 3 × 10 = 30"]]'),
             "ask": {'a': 60, 'b': 30, 'op': 'pwh'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 12 is 30 percent "
                       "of 40. Tap the reason why."),
            "choices": ("because 10 percent is 4, and the whole is ten of those | "
                        "because 40 is the biggest number, so it must be the whole | "
                        "because the whole is the part plus the percent number"),
            "answer": "because 10 percent is 4, and the whole is ten of those",
            "board": '[[tape parts="4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4" total="40" caption="ten parts of 4 — 3 of them are the 12"]]',
        },
        "recap": [
            ("So, here it is again. Told a part and its percent, step down to ten "
             "percent — divide the part by how many tens — then step up to the whole: "
             "times by 10. And the whole is always bigger than the part.",
             '[[tape parts="4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4" total="40" caption="10% = 12 ÷ 3 = 4 · 100% = 4 × 10 = 40"]]'),
            ("And that is the full price found from the sale, and the school counted "
             "from one class.",
             '[[step eq="30% = 12, so 100% = 40"]]'),
        ],
        "bank": [
            {"a": 60, "b": 18, "op": "pwh"},
            {"a": 50, "b": 20, "op": "pwh"},
            {"a": 40, "b": 16, "op": "pwh"},
            {"a": 20, "b": 10, "op": "pwh"},
            {"a": 60, "b": 36, "op": "pwh"},
            {"a": 80, "b": 48, "op": "pwh"},
            {"a": 70, "b": 49, "op": "pwh"},
            {"a": 90, "b": 72, "op": "pwh"},
            {"a": 20, "b": 18, "op": "pwh"},
            {"a": 40, "b": 40, "op": "pwh"},
        ],
    },
    {
        "id": "pre-u7-a-price-goes-up",
        "course": "prealgebra", "unit": 7,
        "topic": "A price goes up or down",
        "op": "pup", "max_value": 100,
        "levels": ("abstract",),
        "symbols": ("percent", "price"),
        "advance_line": "Three in a row, and you can say why — you've got it! Work out the change, then move the price by that.",
        "why": [
            ("Why prices? Because this is where percents earn their keep. A coat goes "
             "up by 10 percent, a bag is 20 percent off — and the shop does not tell "
             "you the new price, it tells you the percent. Two steps, and the first "
             "one you already know: work out what the change is worth, then move the "
             "price by that.",
             '[[goal text="A price goes up or down"]]'),
        ],
        "picture": [
            ("Here is a 60 dollar coat as a bar. The price goes up by 10 percent. Ten "
             "percent of 60 is 6, so the change is a 6 dollar piece. Put it on the end "
             "of the bar: 60 plus 6 equals 66 dollars. That is the new price.",
             '[[tape parts="60 | 6" total="66" caption="60 dollars, up by 10% of 60 — 6 more"]]'),
        ],
        "teach": [
            ("That is the method. First the change: a percent OF the price, found the "
             "way you know — ten percent of 60 is 6. Then the move: the price goes UP, "
             "so put the 6 on. 60 plus 6 equals 66 dollars.",
             '[[tape parts="60 | 6" total="66" caption="the price and the change"]][[step eq="10% of 60 = 6"]][[step eq="60 + 6 = 66"]]'),
            ("Here is the trap. The new price is NOT 70 dollars. Ten is a percent, "
             "not ten dollars — you cannot put it straight onto the price. And when "
             "the price goes DOWN instead, the same 6 comes off: 60 take away 6 "
             "equals 54 dollars.",
             '[[step eq="60 + 6 = 66 ✓"]][[step eq="60 + 10 = 70 ✗"]][[tape parts="54 | 6" total="60" caption="down: 60 − 6 = 54"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. A 30 dollar shirt goes up by 20 "
                        "percent. Ten percent of 30 is 3, so 20 percent is 6, and the "
                        "new price is 30 plus 6, which equals 36 dollars.",
                        '[[tape parts="30 | 6" total="36" caption="30 + 6 = 36 dollars"]][[step eq="20% of 30 = 6"]][[step eq="30 + 6 = 36"]]'),
             "ask": {'a': 10, 'b': 30, 'c': 1, 'op': 'pup'}},
            {"worked": ("One more together. A 50 dollar bag goes down by 30 percent. "
                        "Ten percent of 50 is 5, so 30 percent is 15, and 50 take away "
                        "15 equals 35 dollars.",
                        '[[tape parts="35 | 15" total="50" caption="50 − 15 = 35 dollars"]][[step eq="30% of 50 = 15"]][[step eq="50 − 15 = 35"]]'),
             "ask": {'a': 20, 'b': 40, 'c': 0, 'op': 'pup'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A 60 dollar coat "
                       "goes up by 10 percent, and now it costs 66. Tap the reason why."),
            "choices": ("because 10 percent of 60 is 6 dollars, put onto the 60 | "
                        "because 10 percent means 10 dollars, and 60 plus 10 is 70 | "
                        "because every price goes up by 6 dollars"),
            "answer": "because 10 percent of 60 is 6 dollars, put onto the 60",
            "board": '[[tape parts="60 | 6" total="66" caption="60 + 6 = 66 dollars"]]',
        },
        "recap": [
            ("So, here it is again. A price goes up or down by a percent: first work "
             "out the change — that percent OF the price — then put it on or take it "
             "off. The percent is never dollars on its own.",
             '[[tape parts="60 | 6" total="66" caption="10% of 60 = 6 · 60 + 6 = 66"]]'),
            ("And that is the sale sign turned into the price you pay.",
             '[[step eq="60 + 6 = 66 · 60 − 6 = 54"]]'),
        ],
        "bank": [
            {"a": 10, "b": 20, "c": 1, "op": "pup"},
            {"a": 20, "b": 20, "c": 1, "op": "pup"},
            {"a": 10, "b": 40, "c": 0, "op": "pup"},
            {"a": 20, "b": 50, "c": 0, "op": "pup"},
            {"a": 10, "b": 40, "c": 1, "op": "pup"},
            {"a": 30, "b": 40, "c": 1, "op": "pup"},
            {"a": 20, "b": 60, "c": 1, "op": "pup"},
            {"a": 10, "b": 80, "c": 0, "op": "pup"},
            {"a": 50, "b": 60, "c": 1, "op": "pup"},
            {"a": 20, "b": 80, "c": 1, "op": "pup"},
        ],
    },
]
LESSONS.extend(_PREALGEBRA_U7)


# =============================================================================
# PREALGEBRA -- UNIT 8: MEASUREMENT & GEOMETRY BASICS (build ks, 2026-08-21)
# =============================================================================
# Basic Math's geometry unit -- perimeter, area, quarter turns, volume -- draws NO
# PICTURES. Every board in it is a [[step]] line. Geometry is the one subject where the
# picture IS the argument, and geo-figures.js has had [[triangle]] and [[angle]] since
# July. THREE OF THESE FOUR LESSONS PUT A REAL FIGURE ON THE BOARD, and the
# straight-line lesson uses [[angle deg="180" split="130" caption="a straight line split — 130° and the rest"]] -- a tag built for exactly
# that sentence and never once used by a scripted lesson.
#
# The unit walks from measuring to seeing: change a unit (which is Unit 5's place value
# wearing a coat), then halve a rectangle to get a triangle, then meet the two facts
# every later geometry course leans on -- a straight line is 180 degrees, and so are
# the three angles of any triangle. The last lesson is the first one in the whole
# course whose answer comes from a rule about ALL triangles rather than from counting.
_PREALGEBRA_U8 = [
    {
        "id": "pre-u8-changing-units",
        "course": "prealgebra", "unit": 8,
        "topic": "Changing units",
        "op": "cnv", "max_value": 9000,
        "levels": ("abstract",),
        "symbols": ("unit", "centimetres"),
        "advance_line": "Three in a row, and you can say why — you've got it! Say the unit fact first, then times by it.",
        "why": [
            ("Why change units? Because a ruler reads in centimetres, a map reads in "
             "metres and a recipe reads in grams — and the same length or the same "
             "weight has to move between them. Measuring in a smaller unit takes MORE "
             "of them, and how many more is one fact per unit.",
             '[[goal text="Changing units"]]'),
        ],
        "picture": [
            ("Here are 3 metres as a bar, one part for each metre. One metre is 100 "
             "centimetres, so each part holds 100. Three parts of 100: 3 times 100 "
             "equals 300 centimetres. The bar is the same length either way — it is "
             "just counted in a smaller unit.",
             '[[tape parts="100 | 100 | 100" total="300" caption="3 metres — 100 centimetres in each — 300 cm"]]'),
        ],
        "teach": [
            ("That is the method. Say the unit fact first: one centimetre is 10 "
             "millimetres, one metre is 100 centimetres, one kilogram is 1000 grams. "
             "Then times by it. 3 metres: one metre is 100 centimetres, and 3 times "
             "100 equals 300.",
             '[[tape parts="100 | 100 | 100" total="300" caption="3 metres"]][[step eq="1 m = 100 cm"]][[step eq="3 × 100 = 300"]]'),
            ("The hard part is never the timesing — it is knowing HOW MANY zeros. 3 "
             "metres is not 30 centimetres; that would be using ten when the unit "
             "needs a hundred. One more: 6 centimetres in millimetres. One centimetre "
             "is 10 millimetres, so 6 times 10 equals 60 millimetres.",
             '[[step eq="3 m = 300 cm ✓"]][[step eq="3 m = 30 cm ✗"]][[tape parts="10 | 10 | 10 | 10 | 10 | 10" total="60" caption="6 centimetres — 10 millimetres in each"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 3 kilograms in grams. One "
                        "kilogram is 1000 grams, so 3 times 1000 equals 3000 grams.",
                        '[[tape parts="1000 | 1000 | 1000" total="3000" caption="3 kilograms — 1000 grams in each"]][[step eq="1 kg = 1000 g"]][[step eq="3 × 1000 = 3000"]]'),
             "ask": {'a': 7, 'b': 10, 'op': 'cnv'}},
            {"worked": ("One more together. 4 centimetres in millimetres. One centimetre "
                        "is 10 millimetres, so 4 times 10 equals 40 millimetres.",
                        '[[tape parts="10 | 10 | 10 | 10" total="40" caption="4 centimetres — 10 millimetres in each"]][[step eq="1 cm = 10 mm"]][[step eq="4 × 10 = 40"]]'),
             "ask": {'a': 8, 'b': 100, 'op': 'cnv'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 3 metres is 300 "
                       "centimetres. Tap the reason why."),
            "choices": ("because a metre is 100 centimetres, so 3 metres is 3 hundreds | "
                        "because a metre is 10 centimetres, so you write one zero | "
                        "because centimetres are bigger, so you get fewer of them"),
            "answer": "because a metre is 100 centimetres, so 3 metres is 3 hundreds",
            "board": '[[tape parts="100 | 100 | 100" total="300" caption="3 metres = 300 centimetres"]]',
        },
        "recap": [
            ("So, here it is again. To measure in a smaller unit, say the unit fact "
             "out loud — 10, 100 or 1000 — then times by it. The number of zeros is "
             "the whole question, and the unit fact answers it.",
             '[[tape parts="100 | 100 | 100" total="300" caption="1 m = 100 cm · 3 × 100 = 300"]]'),
            ("And that is the ruler, the map and the recipe all speaking the same "
             "length.",
             '[[step eq="3 m = 300 cm"]]'),
        ],
        "bank": [
            {"a": 2, "b": 10, "op": "cnv"},
            {"a": 5, "b": 10, "op": "cnv"},
            {"a": 8, "b": 10, "op": "cnv"},
            {"a": 2, "b": 100, "op": "cnv"},
            {"a": 4, "b": 100, "op": "cnv"},
            {"a": 7, "b": 100, "op": "cnv"},
            {"a": 9, "b": 100, "op": "cnv"},
            {"a": 2, "b": 1000, "op": "cnv"},
            {"a": 5, "b": 1000, "op": "cnv"},
            {"a": 9, "b": 1000, "op": "cnv"},
        ],
    },
    {
        "id": "pre-u8-area-of-a-triangle",
        "course": "prealgebra", "unit": 8,
        "topic": "Area of a triangle",
        "op": "tri", "max_value": 200,
        "levels": ("abstract",),
        "symbols": ("base", "height"),
        "advance_line": "Three in a row, and you can say why — you've got it! The rectangle round it, then half.",
        "why": [
            ("Why the area of a triangle? Because roofs, sails, ramps and slices of "
             "pizza are triangles, and someone has to know how much paint, cloth or "
             "cheese they take. You already know a rectangle's area — the long side "
             "times the short side. A triangle is easier than it looks, because every "
             "right triangle is exactly HALF of a rectangle.",
             '[[goal text="Area of a triangle"]]'),
        ],
        "picture": [
            ("Here is a right triangle with a base of 8 and a height of 3, drawn on "
             "squares. Draw the rectangle round it — 8 long and 3 wide — and the "
             "diagonal cuts it into two triangles the same size. The rectangle is 8 "
             "times 3, which equals 24 squares, so the triangle is half of that: 12.",
             '[[rectangle w="8" h="3" half="1" caption="base 8, height 3 — half of the 8 by 3 rectangle"]]'),
        ],
        "teach": [
            ("That is the method. The base times the height is the rectangle round "
             "the triangle. Then halve it, because the triangle is half. Base 8, "
             "height 3: 8 times 3 equals 24, and 24 divided by 2 equals 12.",
             '[[rectangle w="8" h="3" half="1" caption="8 × 3 = 24 · half is 12"]][[step eq="8 × 3 = 24"]][[step eq="24 ÷ 2 = 12"]]'),
            ("Do not stop after the timesing. 24 is the rectangle, not the triangle. "
             "The halving is the whole idea — miss it and your triangle is twice the "
             "size of the one on the board.",
             '[[step eq="24 ÷ 2 = 12 ✓"]][[step eq="24 ✗ — that is the rectangle"]][[rectangle w="8" h="3" half="1" caption="the triangle is the filled half — 12, not 24"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. A base of 10 and a height of "
                        "6. 10 times 6 equals 60, and half of 60 equals 30.",
                        '[[rectangle w="10" h="6" half="1" caption="10 × 6 = 60 · half is 30"]][[step eq="10 × 6 = 60"]][[step eq="60 ÷ 2 = 30"]]'),
             "ask": {'a': 9, 'b': 4, 'op': 'tri'}},
            {"worked": ("One more together. A base of 6 and a height of 7. 6 times 7 "
                        "equals 42, and half of 42 equals 21.",
                        '[[rectangle w="6" h="7" half="1" caption="6 × 7 = 42 · half is 21"]][[step eq="6 × 7 = 42"]][[step eq="42 ÷ 2 = 21"]]'),
             "ask": {'a': 7, 'b': 8, 'op': 'tri'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A triangle with a "
                       "base of 8 and a height of 3 has an area of 12. Tap the reason "
                       "why."),
            "choices": ("because it is half of the 8 by 3 rectangle, 24 | "
                        "because 8 times 3 is 24, and that is the triangle | because "
                        "the area is the base plus the height"),
            "answer": "because it is half of the 8 by 3 rectangle, 24",
            "board": '[[rectangle w="8" h="3" half="1" caption="8 × 3 = 24 · half is 12"]]',
        },
        "recap": [
            ("So, here it is again. Base times height is the rectangle round the "
             "triangle; the triangle is half of it. Times, then halve — and the "
             "halving is the step people forget.",
             '[[rectangle w="8" h="3" half="1" caption="8 × 3 = 24 · 24 ÷ 2 = 12"]]'),
            ("And that is the sail measured, and the pizza slice shared fairly.",
             '[[step eq="8 × 3 ÷ 2 = 12"]]'),
        ],
        "bank": [
            {"a": 4, "b": 2, "op": "tri"},
            {"a": 3, "b": 4, "op": "tri"},
            {"a": 4, "b": 5, "op": "tri"},
            {"a": 4, "b": 6, "op": "tri"},
            {"a": 5, "b": 6, "op": "tri"},
            {"a": 8, "b": 5, "op": "tri"},
            {"a": 6, "b": 9, "op": "tri"},
            {"a": 12, "b": 5, "op": "tri"},
            {"a": 10, "b": 8, "op": "tri"},
            {"a": 14, "b": 9, "op": "tri"},
        ],
    },
    {
        "id": "pre-u8-angles-on-a-line",
        "course": "prealgebra", "unit": 8,
        "topic": "Angles on a straight line",
        "op": "sla", "max_value": 360,
        "levels": ("abstract",),
        "symbols": ("degrees", "straight line"),
        "advance_line": "Three in a row, and you can say why — you've got it! A straight line is 180 degrees.",
        "why": [
            ("Why angles on a line? Because you know a quarter turn is 90 degrees, and "
             "two of those make a half turn — a straight line, 180 degrees. That one "
             "fact answers a whole family of questions: whenever two angles sit "
             "together on a straight line, knowing one tells you the other.",
             '[[goal text="Angles on a straight line"]]'),
        ],
        "picture": [
            ("Here is a straight line with a ray drawn up from it. The two angles sit "
             "together and fill the line, so together they are 180 degrees. One of "
             "them is 130. The other is what is left: 180 take away 130, which equals "
             "50 degrees. And 130 plus 50 puts the 180 back.",
             '[[angle deg="180" split="130,50" caption="a straight line — 130° + 50° = 180°"]]'),
        ],
        "teach": [
            ("That is the method. Two angles on a straight line come to 180 degrees. "
             "Given one, take it away from 180 and the other is what is left. 180 "
             "take away 130 equals 50.",
             '[[angle deg="180" split="130" caption="a straight line — 130° and the rest"]][[step eq="180° − 130° = 50°"]]'),
            ("Watch which number you take away from. It is 180 — not 90 and not 360. "
             "90 is a quarter turn and 360 is the whole way round; neither of them is "
             "a straight line. One more: an angle of 120 on the line leaves 180 take "
             "away 120, which equals 60 degrees.",
             '[[step eq="180° − 130° = 50° ✓"]][[step eq="360° − 130° = 230° ✗"]][[angle deg="180" split="120,60" caption="120° + 60° = 180°"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. One angle on the line is 45 "
                        "degrees. 180 take away 45 equals 135 degrees.",
                        '[[angle deg="180" split="45,135" caption="45° + 135° = 180°"]][[step eq="180° − 45° = 135°"]]'),
             "ask": {'a': 150, 'b': 0, 'op': 'sla'}},
            {"worked": ("One more together. One angle is 75 degrees, so the other is "
                        "180 take away 75, which equals 105 degrees.",
                        '[[angle deg="180" split="75,105" caption="75° + 105° = 180°"]][[step eq="180° − 75° = 105°"]]'),
             "ask": {'a': 70, 'b': 0, 'op': 'sla'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. One angle on a "
                       "straight line is 130 degrees, so the other is 50. Tap the "
                       "reason why."),
            "choices": ("because the two together fill the line, and a line is 180 | "
                        "because a straight line is 360 degrees, the whole way round | "
                        "because the other angle on a line is 50 every time"),
            "answer": "because the two together fill the line, and a line is 180",
            "board": '[[angle deg="180" split="130,50" caption="130° + 50° = 180°"]]',
        },
        "recap": [
            ("So, here it is again. A straight line is 180 degrees, and two angles "
             "that sit together on it fill it. Take the one you know from 180, and "
             "the other is what is left.",
             '[[angle deg="180" split="130,50" caption="180° − 130° = 50°"]]'),
            ("And that is one fact, a half turn, answering a whole family of "
             "questions.",
             '[[step eq="180° − 130° = 50°"]]'),
        ],
        "bank": [
            {"a": 160, "b": 0, "op": "sla"},
            {"a": 140, "b": 0, "op": "sla"},
            {"a": 125, "b": 0, "op": "sla"},
            {"a": 110, "b": 0, "op": "sla"},
            {"a": 100, "b": 0, "op": "sla"},
            {"a": 80, "b": 0, "op": "sla"},
            {"a": 65, "b": 0, "op": "sla"},
            {"a": 50, "b": 0, "op": "sla"},
            {"a": 35, "b": 0, "op": "sla"},
            {"a": 20, "b": 0, "op": "sla"},
        ],
    },
    {
        "id": "pre-u8-angles-in-a-triangle",
        "course": "prealgebra", "unit": 8,
        "topic": "Angles in a triangle",
        "op": "tri3", "max_value": 180,
        "levels": ("abstract",),
        "symbols": ("degrees", "triangle"),
        "advance_line": "Three in a row, and you can say why — you've got it! Three angles, 180 degrees, every triangle.",
        "why": [
            ("Why angles in a triangle? Because here is one of the most useful facts "
             "in all of geometry. Take any triangle at all — thin, wide, lopsided — "
             "and its three angles come to 180 degrees. Know two angles and the "
             "third is forced.",
             '[[goal text="Angles in a triangle"]]'),
        ],
        "picture": [
            ("Here is a triangle with its three angles marked: 50, 60 and 70 degrees. "
             "Add them: 50 plus 60 equals 110, and 110 plus 70 equals 180. Cover the "
             "70 and you could still find it — it is whatever is left of the 180 "
             "after the other two.",
             '[[triangle v="A,B,C" angles="50,60,70" caption="50° + 60° + 70° = 180°"]]'),
        ],
        "teach": [
            ("That is the method. The three angles come to 180 degrees. That is the "
             "same 180 as a straight line, and it is not a coincidence. Given two "
             "angles, add them, then take what they come to from 180. Two angles are "
             "50 and 60: 50 plus 60 equals 110, and 180 take "
             "away 110 equals 70 degrees.",
             '[[triangle v="A,B,C" angles="50,60," caption="angles 50° and 60° — the third is forced"]][[step eq="50° + 60° = 110°"]][[step eq="180° − 110° = 70°"]]'),
            ("Two steps, and the first one is not the answer. 110 is what the two you "
             "were GIVEN come to. The one you were asked for is what is left of the "
             "180 after them. One more: 35 and 65 come to 100, and 180 take away 100 "
             "equals 80 degrees.",
             '[[step eq="180° − 110° = 70° ✓"]][[step eq="110° ✗ — that is the two you were given"]][[triangle v="A,B,C" angles="35,65,80" caption="35° + 65° + 80° = 180°"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Two angles are 20 and 30. "
                        "Together they are 50, and 180 take away 50 equals 130 degrees.",
                        '[[triangle v="A,B,C" angles="20,30,130" caption="20° + 30° + 130° = 180°"]][[step eq="20° + 30° = 50°"]][[step eq="180° − 50° = 130°"]]'),
             "ask": {'a': 65, 'b': 75, 'op': 'tri3'}},
            {"worked": ("One more together. Two angles are 75 and 85. Together they are "
                        "160, so the third is 180 take away 160, which equals 20 degrees.",
                        '[[triangle v="A,B,C" angles="75,85,20" caption="75° + 85° + 20° = 180°"]][[step eq="75° + 85° = 160°"]][[step eq="180° − 160° = 20°"]]'),
             "ask": {'a': 49, 'b': 61, 'op': 'tri3'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Two angles of a "
                       "triangle are 50 and 60 degrees, so the third is 70. Tap the "
                       "reason why."),
            "choices": ("because the three angles come to 180, and 110 leaves 70 | "
                        "because the third angle is 180 take away the bigger one | "
                        "because a triangle's angles come to 360, like a full turn"),
            "answer": "because the three angles come to 180, and 110 leaves 70",
            "board": '[[triangle v="A,B,C" angles="50,60,70" caption="50° + 60° + 70° = 180°"]]',
        },
        "recap": [
            ("So, here it is again. The three angles of any triangle come to 180 "
             "degrees. Add the two you are given, take that from 180, and the "
             "third is what is left.",
             '[[triangle v="A,B,C" angles="50,60,70" caption="50° + 60° = 110° · 180° − 110° = 70°"]]'),
            ("And that is a fact that holds for every triangle ever drawn.",
             '[[step eq="180° − 110° = 70°"]]'),
        ],
        "bank": [
            {"a": 80, "b": 80, "op": "tri3"},
            {"a": 70, "b": 85, "op": "tri3"},
            {"a": 60, "b": 90, "op": "tri3"},
            {"a": 55, "b": 90, "op": "tri3"},
            {"a": 60, "b": 70, "op": "tri3"},
            {"a": 40, "b": 80, "op": "tri3"},
            {"a": 30, "b": 90, "op": "tri3"},
            {"a": 45, "b": 60, "op": "tri3"},
            {"a": 40, "b": 55, "op": "tri3"},
            {"a": 20, "b": 40, "op": "tri3"},
        ],
    },
]
LESSONS.extend(_PREALGEBRA_U8)


# =============================================================================
# PREALGEBRA -- UNIT 9: VARIABLES & EXPRESSIONS (build kt, 2026-08-21)
# =============================================================================
# The last prealgebra unit, and the doorway to algebra. Everything before this asked
# about numbers; these four ask about a LETTER that stands for one. The order is the
# order the idea grows: a letter holds a number, a number written against a letter
# means times, like terms collect by counting, and a times distributes over a
# parenthesis.
#
# ⭐ THE LAST LESSON DRAWS THE DISTRIBUTIVE PROPERTY as an area model -- a rectangle
# 4 tall and (x + 3) wide, cut into a 4x room and a 12 room -- using [[areamodel]],
# the algebra-tile renderer that has been in the registry since July and (exactly like
# [[angle split=]] before build ks) has never been used by a scripted lesson. The
# child is not handed the rule; the child is shown the two rooms.
#
# THE ERROR THAT RULES THIS UNIT is the notation quietly meaning times: 3x read as
# 3 plus x, and 4(x + 3) read as 4x + 3 with the times never reaching the number.
# Both are offered as wrong taps, every time.
_PREALGEBRA_U9 = [
    {
        "id": "pre-u9-a-letter-holds-a-number",
        "course": "prealgebra", "unit": 9,
        "topic": "A letter holds a number",
        "op": "evx", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("x", "letter"),
        "advance_line": "Three in a row, and you can say why — you've got it! Swap the letter for its number, then add.",
        "why": [
            ("Why a letter? Because here is the biggest idea in all of algebra, and it "
             "is small enough to hold: a letter can stand for a number. When we write "
             "x, we mean some number that x is holding for us. Tell me what x holds, "
             "and every question about x becomes a question about that number.",
             '[[goal text="A letter holds a number"]]'),
        ],
        "picture": [
            ("Here is x plus 3 as a bar: a piece for x and a piece of 3, with the "
             "whole bar the question. Now x is holding 5. Swap the x piece for a 5 "
             "and the bar reads 5 plus 3, and the whole is 8.",
             '[[tape parts="x | 3" total="?" caption="x + 3 — what is the whole?"]][[tape parts="5 | 3" total="8" caption="x holds 5: 5 + 3 = 8"]]'),
        ],
        "teach": [
            ("That swap is the whole move. Take the question first: what is x plus 3? "
             "Then take what x holds: 5. Swap the letter for its number, and x plus 3 "
             "becomes 5 plus 3, which equals 8.",
             '[[tape parts="x | 3" total="?" caption="x + 3 — one x, then 3"]][[step eq="x = 5"]][[tape parts="5 | 3" total="8" caption="x + 3 = 5 + 3 = 8"]]'),
            ("One careful thing. x plus 3 with x holding 5 is NOT fifty-three. The 5 "
             "and the 3 do not sit next to each other like digits — the plus keeps "
             "them apart. Swap first, then add. One more: x plus 6, with x holding 4, "
             "becomes 4 plus 6, which equals 10.",
             '[[step eq="5 + 3 = 8 ✓"]][[step eq="53 ✗ — those are digits, not a sum"]][[tape parts="4 | 6" total="10" caption="x + 6 with x holding 4: 4 + 6 = 10"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. x plus 2, with x holding 7, "
                        "becomes 7 plus 2, which equals 9.",
                        '[[step eq="x + 2"]][[step eq="x = 7"]][[tape parts="7 | 2" total="9" caption="x + 2 = 7 + 2 = 9"]]'),
             "ask": {'a': 5, 'b': 6, 'op': 'evx'}},
            {"worked": ("One more together. x plus 7, with x holding 6, becomes 6 plus "
                        "7, which equals 13.",
                        '[[step eq="x + 7"]][[step eq="x = 6"]][[tape parts="6 | 7" total="13" caption="x + 7 = 6 + 7 = 13"]]'),
             "ask": {'a': 8, 'b': 7, 'op': 'evx'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. x plus 3 is 8, "
                       "when x is holding 5. Tap the reason why."),
            "choices": ("because you swap the x for the 5, then add the 3 | because x "
                        "plus 3 is 8 whatever x is holding | because the letter x is "
                        "worth 8 in every sum"),
            "answer": "because you swap the x for the 5, then add the 3",
            "board": '[[tape parts="5 | 3" total="8" caption="x + 3 with x holding 5: 5 + 3 = 8"]]',
        },
        "recap": [
            ("So, here it is again. A letter holds a number. To work out anything "
             "about x, swap the letter for the number it is holding, then do the "
             "sum. Swap first — the plus keeps the numbers apart.",
             '[[tape parts="5 | 3" total="8" caption="x = 5 · x + 3 = 5 + 3 = 8"]]'),
            ("And that is the doorway to algebra, one letter wide.",
             '[[step eq="x = 5, so x + 3 = 8"]]'),
        ],
        "bank": [
            {"a": 2, "b": 3, "op": "evx"},
            {"a": 4, "b": 2, "op": "evx"},
            {"a": 3, "b": 4, "op": "evx"},
            {"a": 4, "b": 4, "op": "evx"},
            {"a": 6, "b": 3, "op": "evx"},
            {"a": 4, "b": 7, "op": "evx"},
            {"a": 8, "b": 4, "op": "evx"},
            {"a": 9, "b": 5, "op": "evx"},
            {"a": 7, "b": 9, "op": "evx"},
            {"a": 9, "b": 9, "op": "evx"},
        ],
    },
    {
        "id": "pre-u9-a-number-against-a-letter",
        "course": "prealgebra", "unit": 9,
        "topic": "A number against a letter means times",
        "op": "mlx", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("x", "times"),
        "advance_line": "Three in a row, and you can say why — you've got it! A number against a letter means times.",
        "why": [
            ("Why is this one worth a whole lesson? Because algebra has one piece of "
             "shorthand you have to be told — nothing about it looks like what it "
             "means. A number written right against a letter means TIMES. 3 x means "
             "3 times x. The times sign is there; it is just invisible.",
             '[[goal text="A number against a letter means times"]]'),
        ],
        "picture": [
            ("Here is 3 x as a bar: three copies of x, side by side. Not one x with "
             "a three beside it — three x's. Now x is holding 9, so every copy is a 9. Three "
             "nines: 3 times 9 equals 27.",
             '[[tape parts="x | x | x" total="?" caption="3x — three copies of x"]][[tape parts="9 | 9 | 9" total="27" caption="x holds 9: 3 × 9 = 27"]]'),
        ],
        "teach": [
            ("That is the rule. Take the question first: what is 3 x? The number "
             "against the letter means times. Then take what x holds: 9. So it is 3 "
             "times 9, which equals 27.",
             '[[tape parts="x | x | x" total="?" caption="3x — 3 copies of x"]][[step eq="x = 9"]][[tape parts="9 | 9 | 9" total="27" caption="3x = 3 × 9 = 27"]]'),
            ("The trap is reading it as a plus — as if the number is just standing "
             "near the x. It is not standing near it; it is timesing it. 3 x "
             "with x holding 9 equals 27, never 12. One more: 2 x, with x holding 5, "
             "is 2 times 5, which equals 10.",
             '[[step eq="3x = 27 ✓"]][[step eq="3 + 9 = 12 ✗"]][[tape parts="5 | 5" total="10" caption="2x with x holding 5: 2 × 5 = 10"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 4 x, with x holding 8, is 4 "
                        "times 8, which equals 32.",
                        '[[step eq="4x"]][[step eq="x = 8"]][[tape parts="8 | 8 | 8 | 8" total="32" caption="4x = 4 × 8 = 32"]]'),
             "ask": {'a': 4, 'b': 5, 'op': 'mlx'}},
            {"worked": ("One more together. 5 x, with x holding 2, is 5 times 2, which "
                        "equals 10.",
                        '[[step eq="5x"]][[step eq="x = 2"]][[tape parts="2 | 2 | 2 | 2 | 2" total="10" caption="5x = 5 × 2 = 10"]]'),
             "ask": {'a': 7, 'b': 3, 'op': 'mlx'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 3 x is 27, when x "
                       "is holding 9. Tap the reason why."),
            "choices": ("because 3 x means 3 times x, three copies of 9 | because "
                        "the 3 is standing next to x, so add it on | because 3 x means "
                        "3 plus x, and the plus is hidden"),
            "answer": "because 3 x means 3 times x, three copies of 9",
            "board": '[[tape parts="9 | 9 | 9" total="27" caption="3x = 3 × 9 = 27"]]',
        },
        "recap": [
            ("So, here it is again. A number written against a letter means times — "
             "that many copies of the letter. 3 x is three x's, and with x holding 9 "
             "it is 27. The times sign is invisible, but it is there.",
             '[[tape parts="9 | 9 | 9" total="27" caption="3x = 3 × 9 = 27"]]'),
            ("And that is the shorthand every line of algebra is written in.",
             '[[step eq="3x = 3 × x"]]'),
        ],
        "bank": [
            {"a": 2, "b": 3, "op": "mlx"},
            {"a": 4, "b": 2, "op": "mlx"},
            {"a": 3, "b": 4, "op": "mlx"},
            {"a": 7, "b": 2, "op": "mlx"},   # (uz) was 3,3 -- the picture beat opens "3 x ... three copies ... 9"
            {"a": 5, "b": 3, "op": "mlx"},
            {"a": 4, "b": 4, "op": "mlx"},
            {"a": 6, "b": 3, "op": "mlx"},
            {"a": 3, "b": 7, "op": "mlx"},
            {"a": 7, "b": 4, "op": "mlx"},
            {"a": 6, "b": 6, "op": "mlx"},
        ],
    },
    {
        "id": "pre-u9-collecting-x",
        "course": "prealgebra", "unit": 9,
        "topic": "Collecting the x's",
        "op": "clt", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("x", "terms"),
        "advance_line": "Three in a row, and you can say why — you've got it! Terms of x collect by counting.",
        "why": [
            ("Why collect the x's? Because you do not need to know what x is holding "
             "to do some things with it. Three apples plus two apples is five apples. "
             "Three x's plus two x's is five x's — whatever x turns out to be. Pieces "
             "like 3 x and 2 x are called terms, and terms of x collect by counting.",
             '[[goal text="Collecting the x\'s"]]'),
        ],
        "picture": [
            ("Here are 3 x plus 2 x as one bar: three x's, then two more x's. Count "
             "them along the bar: one, two, three, four, five. Five x's. So 3 x plus "
             "2 x equals 5 x.",
             '[[tape parts="x | x | x | x | x" total="5x" caption="3x + 2x — count the x\'s: 5x"]]'),
        ],
        "teach": [
            ("That is the rule. 3 x plus 2 x: count them. 3 of them plus 2 of them "
             "equals 5 of them, so 3 x plus 2 x equals 5 x — whatever x is holding.",
             '[[tape parts="x | x | x | x | x" total="5x" caption="3 of them + 2 of them"]][[step eq="3x + 2x"]][[step eq="3 of them + 2 of them = 5 of them"]]'),
            ("Careful — the counts ADD. Do not times them. 3 x plus 2 x is 5 x, not "
             "6 x. The invisible times lives between a number and its own letter, not "
             "between the two counts. One more: 4 x plus 5 x is four of them plus "
             "five of them, nine of them — 9 x.",
             '[[step eq="3x + 2x = 5x ✓"]][[step eq="6x ✗ — the counts add"]][[tape parts="x | x | x | x | x | x | x | x | x" total="9x" caption="4x + 5x = 9x"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 7 x plus 2 x. Seven of them "
                        "plus two of them equals nine of them: 9 x.",
                        '[[tape parts="x | x | x | x | x | x | x | x | x" total="9x" caption="7x + 2x = 9x"]][[step eq="7x + 2x = 9x"]]'),
             "ask": {'a': 5, 'b': 6, 'op': 'clt'}},
            {"worked": ("One more together. 6 x plus 5 x. Six of them plus five of "
                        "them equals eleven of them: 11 x.",
                        '[[tape parts="6x | 5x" total="11x" caption="6x + 5x = 11x"]][[step eq="6x + 5x = 11x"]]'),
             "ask": {'a': 8, 'b': 6, 'op': 'clt'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 3 x plus 2 x is "
                       "5 x. Tap the reason why."),
            "choices": ("because three of a thing and two more is five of it | "
                        "because the counts times each other when x is there | because "
                        "the letters add up and the numbers stay put"),
            "answer": "because three of a thing and two more is five of it",
            "board": '[[tape parts="x | x | x | x | x" total="5x" caption="3x + 2x = 5x"]]',
        },
        "recap": [
            ("So, here it is again. Terms of x collect by counting: 3 of them plus 2 "
             "of them is 5 of them, so 3 x plus 2 x is 5 x. The counts add — they "
             "never times.",
             '[[tape parts="x | x | x | x | x" total="5x" caption="3x + 2x = 5x"]]'),
            ("And that is apples and apples, with a letter in place of the apple.",
             '[[step eq="3x + 2x = 5x"]]'),
        ],
        "bank": [
            {"a": 2, "b": 4, "op": "clt"},
            {"a": 4, "b": 3, "op": "clt"},
            {"a": 6, "b": 2, "op": "clt"},
            {"a": 3, "b": 6, "op": "clt"},
            {"a": 7, "b": 4, "op": "clt"},
            {"a": 8, "b": 5, "op": "clt"},
            {"a": 9, "b": 5, "op": "clt"},
            {"a": 7, "b": 8, "op": "clt"},
            {"a": 9, "b": 7, "op": "clt"},
            {"a": 9, "b": 9, "op": "clt"},
        ],
    },
    {
        "id": "pre-u9-the-times-reaches-both",
        "course": "prealgebra", "unit": 9,
        "topic": "The times reaches both rooms",
        "op": "dst", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("parentheses", "x"),
        "advance_line": "Three in a row, and you can say why — you've got it! The times reaches both rooms.",
        "why": [
            ("Why does the times reach both? Because you met parentheses in the very "
             "first prealgebra lesson: do what is inside first. But when an x is "
             "inside, you CANNOT do the inside first — x plus 3 will not collapse "
             "into one number. So the times outside has to reach in, and a rectangle "
             "cut into two rooms is the way to see it.",
             '[[goal text="The times reaches both rooms"]]'),
        ],
        "picture": [
            ("Here is a rectangle 4 tall and x plus 3 wide. Its area is 4 times the "
             "whole of x plus 3. A wall splits it into two rooms: one room is 4 by x "
             "— that is 4 x — and the other is 4 by 3, which is 12. Both rooms "
             "together: 4 x plus 12.",
             '[[areamodel rows="4" cols="x,3" caption="a 4 by (x + 3) rectangle — two rooms: 4x and 12"]]'),
        ],
        "teach": [
            ("That is the rule: the times reaches BOTH rooms. 4 times the whole of x "
             "plus 3 is 4 times x, plus 4 times 3. That is 4 x plus 12.",
             '[[areamodel rows="4" cols="x,3" caption="read the rooms"]][[step eq="4(x + 3) = 4x + 12"]]'),
            ("The wrong answer is 4 x plus 3, where the 4 timesed the x and never "
             "touched the 3. Look at the board: the second room is real, and it is "
             "12, not 3. One more: 5 times the whole of x plus 2 is 5 x plus 10.",
             '[[step eq="4x + 12 ✓"]][[step eq="4x + 3 ✗ — the 3 never got timesed"]][[areamodel rows="5" cols="x,2" caption="5(x + 2) = 5x + 10"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Times the whole of x plus 4 by "
                        "3. The rooms are 3 x and 3 times 4, which equals 12: 3 x plus "
                        "12.",
                        '[[areamodel rows="3" cols="x,4" caption="a 3 by (x + 4) rectangle — read the rooms"]][[step eq="3(x + 4) = 3x + 12"]]'),
             "ask": {'a': 6, 'b': 2, 'op': 'dst'}},
            {"worked": ("One more together. Times the whole of x plus 5 by 2. The rooms "
                        "are 2 x and 2 times 5, which equals 10: 2 x plus 10.",
                        '[[areamodel rows="2" cols="x,5" caption="a 2 by (x + 5) rectangle — read the rooms"]][[step eq="2(x + 5) = 2x + 10"]]'),
             "ask": {'a': 5, 'b': 6, 'op': 'dst'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 4 times the whole "
                       "of x plus 3 is 4 x plus 12. Tap the reason why."),
            "choices": ("because the 4 times the x and times the 3 too | because the 4 "
                        "only reaches the x, and the 3 stays 3 | because the second "
                        "room is 4 plus 3"),
            "answer": "because the 4 times the x and times the 3 too",
            "board": '[[areamodel rows="4" cols="x,3" caption="4(x + 3) = 4x + 12"]]',
        },
        "recap": [
            ("So, here it is again. A times outside parentheses with an x inside "
             "reaches both rooms: it times the x, and it times the number. 4 times "
             "the whole of x plus 3 is 4 x plus 12 — never 4 x plus 3.",
             '[[areamodel rows="4" cols="x,3" caption="4(x + 3) = 4x + 12"]]'),
            ("And that is the last prealgebra lesson, and the first line of algebra.",
             '[[step eq="4(x + 3) = 4x + 12"]]'),
        ],
        "bank": [
            {"a": 2, "b": 3, "op": "dst"},
            {"a": 4, "b": 2, "op": "dst"},
            {"a": 3, "b": 3, "op": "dst"},
            {"a": 3, "b": 4, "op": "dst"},
            {"a": 5, "b": 3, "op": "dst"},
            {"a": 4, "b": 4, "op": "dst"},
            {"a": 6, "b": 3, "op": "dst"},
            {"a": 5, "b": 4, "op": "dst"},
            {"a": 6, "b": 4, "op": "dst"},
            {"a": 7, "b": 4, "op": "dst"},
        ],
    },
]
LESSONS.extend(_PREALGEBRA_U9)

# ---- this course's slice of COURSE_ORDER: the teaching order (lessons/__init__.py joins the ten) ----
ORDER = [

    # ---- PREALGEBRA (build kk) -- Unit 1: Number Sense & Order of Operations ----
    "pre-u1-times-before-add", "pre-u1-parentheses-first",
    "pre-u1-exponents-are-repeated-times", "pre-u1-power-then-times-then-add",
    # Unit 2: Factors, Multiples & Primes -- underneath Basic's GCF/LCM
    "pre-u2-how-many-factors", "pre-u2-the-smallest-factor",
    "pre-u2-breaking-into-primes", "pre-u2-the-biggest-factor",
    # Unit 3: Integers & Negative Numbers -- the first answers below zero
    "pre-u3-counting-back-past-zero", "pre-u3-adding-a-negative",
    "pre-u3-taking-away-a-negative", "pre-u3-times-with-a-negative",
    # Unit 4: Fractions -- past Basic's adding, taking away and unit fractions
    "pre-u4-a-fraction-of-a-number", "pre-u4-how-many-parts-in-a-whole",
    "pre-u4-dividing-by-a-fraction", "pre-u4-fractions-bigger-than-one",
    # Unit 5: Decimals -- past Basic's naming of tenths and hundredths
    "pre-u5-how-many-hundredths", "pre-u5-times-by-ten",
    "pre-u5-tenths-times-a-number", "pre-u5-sharing-a-decimal",
    # Unit 6: Ratios, Rates & Proportions -- past Basic's unit price
    "pre-u6-keeping-a-ratio", "pre-u6-scaling-a-rate",
    "pre-u6-filling-in-a-proportion", "pre-u6-sharing-in-a-ratio",
    # Unit 7: Percents -- past Basic's 10/25/50 fraction shortcut
    "pre-u7-any-percent", "pre-u7-what-percent-is-that",
    "pre-u7-finding-the-whole", "pre-u7-a-price-goes-up",
    # Unit 8: Measurement & Geometry Basics -- and the first prealgebra lessons
    # that put a real FIGURE on the board rather than a line of text
    "pre-u8-changing-units", "pre-u8-area-of-a-triangle",
    "pre-u8-angles-on-a-line", "pre-u8-angles-in-a-triangle",
    # Unit 9: Variables & Expressions -- the doorway to algebra, closed with the
    # ⭐ area model for the distributive property
    "pre-u9-a-letter-holds-a-number", "pre-u9-a-number-against-a-letter",
    "pre-u9-collecting-x", "pre-u9-the-times-reaches-both",
]

# I did no harm and this file is not truncated.

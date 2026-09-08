# =============================================================================
# lessons/geometry.py  --  GEOMETRY: THE AUTHORED LESSONS  --  Hyperion Shift LLC
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
# GEOMETRY -- UNIT 1: FOUNDATIONS & CONSTRUCTIONS (build lc, 2026-08-22)
# =============================================================================
# GEOMETRY OPENS -- the tenth course. Basic Math measured shapes and Prealgebra U8
# met the straight line and the triangle sum; this unit lays the vocabulary those
# facts stand on, and lays it with FIGURES rather than definitions to memorise.
# [[angle split=]] carries the two angle-pair lessons, [[circle]] the radius, and
# [[numberline]] the midpoint.
#
# THE THREAD: every lesson here is a pair of things that add to a fixed total, or a
# pair that are related by two. Naming which total, and which way round, is the
# entire skill -- and every wrong tap in the unit is the OTHER total (180 where 90
# belongs) or the other direction (halving where doubling belongs).
_GEOMETRY_U1 = [
    {
        "id": "geo-u1-two-make-a-corner",
        "course": "geometry", "unit": 1,
        "topic": "Two angles make a right angle",
        "op": "comp", "max_value": 90,
        "levels": ("abstract",),
        "symbols": ("right angle", "degrees"),
        "advance_line": "Three in a row, and you can say why — you've got it! A right angle is 90, so the pair adds to 90.",
        "why": [
            ("Welcome to geometry. Why start with a corner? Because you already know "
             "two totals: a right angle is 90 degrees, and a straight line is 180. "
             "Today\'s angles share the smaller one — two angles that together make a "
             "right angle, a perfect square corner — and corners are everywhere: "
             "walls, pages, the frame of a door.",
             '[[goal text="Two angles make a right angle"]]'),
        ],
        "picture": [
            ("Here is a right angle with a ray drawn inside it, splitting it into two "
             "angles. One angle is 30 degrees. The two fill the square corner, so "
             "together they are 90 — and the other angle is 90 take away 30, which "
             "is 60. Both labelled, they add back to the corner.",
             '[[angle deg="90" split="30,60" caption="a square corner split — 30° + 60° = 90°"]]'),
        ],
        "teach": [
            ("That is the method. The two angles fill the corner, so together they "
             "make 90. One of them is 30, so the other is 90 take away 30, which "
             "equals 60.",
             '[[angle deg="90" split="30" caption="a square corner split — 30° and the rest"]][[step eq="90° − 30° = 60°"]]'),
            ("Angles that pair up to 90 have a name: complementary. And here is the "
             "trap — you met 180 first, in the straight-line lesson, and 180 sticks. "
             "Ask which corner you are inside. A square corner is 90.",
             '[[angle deg="90" split="30" caption="inside a square corner"]][[step eq="90 − 30 = 60 ✓"]][[step eq="180 − 30 = 150 ✗ — that is a straight line, not a corner"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. A right angle split in two, one "
                        "angle 40 degrees. The other is 90 take away 40 — 50 degrees.",
                        '[[angle deg="90" split="40,50" caption="40° + 50° = 90°"]][[step eq="90° − 40° = 50°"]]'),
             "ask": {'a': 50, 'b': 0, 'op': 'comp'}},
            {"worked": ("One more together. One angle is 70, so the other is 90 take "
                        "away 70, which equals 20 degrees.",
                        '[[angle deg="90" split="70,20" caption="70° + 20° = 90°"]][[step eq="90° − 70° = 20°"]]'),
             "ask": {'a': 29, 'b': 0, 'op': 'comp'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Two angles make a "
                       "right angle, one is 30 degrees, and the other is 60. Tap the "
                       "reason why."),
            "choices": ("because the two fill a square corner, which is 90 | "
                        "because the two sit on a straight line, which is 180 | because "
                        "the other angle is always twice the first"),
            "answer": "because the two fill a square corner, which is 90",
            "board": '[[angle deg="90" split="30,60" caption="30° + 60° = 90°"]]',
        },
        "recap": [
            ("So, here it is again. Two angles that make a right angle add to 90 — "
             "they are complementary. Take the one you know from 90, not from 180, "
             "and the other is what is left.",
             '[[angle deg="90" split="30,60" caption="90° − 30° = 60°"]]'),
            ("And that is a corner, split and put back together.",
             '[[step eq="90° − 30° = 60°"]]'),
        ],
        "bank": [
            {"a": 80, "b": 0, "op": "comp"},
            {"a": 69, "b": 0, "op": "comp"},
            {"a": 65, "b": 0, "op": "comp"},
            {"a": 60, "b": 0, "op": "comp"},
            {"a": 55, "b": 0, "op": "comp"},
            {"a": 39, "b": 0, "op": "comp"},
            {"a": 35, "b": 0, "op": "comp"},
            {"a": 25, "b": 0, "op": "comp"},
            {"a": 20, "b": 0, "op": "comp"},
            {"a": 10, "b": 0, "op": "comp"},
        ],
    },
    {
        "id": "geo-u1-when-lines-cross",
        "course": "geometry", "unit": 1,
        "topic": "When two lines cross",
        "op": "vert", "max_value": 180,
        "levels": ("abstract",),
        "symbols": ("cross", "degrees"),
        "advance_line": "Three in a row, and you can say why — you've got it! Neighbours make 180; opposites are equal.",
        "why": [
            ("Why an X? Because two straight lines can cross, and where they cross "
             "they make an X with four angles in it. They are not four separate "
             "mysteries — they come in two pairs, and knowing ONE of the four tells "
             "you all the others.",
             '[[goal text="When two lines cross"]]'),
        ],
        "picture": [
            ("Here are two lines crossing, with one angle marked 50 degrees. Straight "
             "across from it, the opposite angle is 50 too — opposite angles are "
             "twins. And the angle NEXT to the 50 sits with it on one straight line, "
             "so the two make 180: it is 130.",
             '[[angle deg="50" cross="50" caption="two lines cross — the 50° angle and its twin opposite"]][[angle deg="180" split="50,130" caption="next to it, on one straight line: 50° + 130° = 180°"]]'),
        ],
        "teach": [
            ("That is the method. Say one angle measures 50 degrees, and remember a "
             "straight line is 180. The angle NEXT to it sits with it on that "
             "straight line, so the two make 180: it is 180 take away 50, which "
             "equals 130. And the angle straight OPPOSITE the 50 is 50 again.",
             '[[angle deg="180" split="50" caption="a straight line split — 50° and the rest"]][[step eq="next to it: 180° − 50° = 130°"]][[step eq="opposite: 50° again"]]'),
            ("So read the question carefully: NEXT to, or OPPOSITE? Next-door angles "
             "add to 180. Opposite angles are twins. Both facts are true at once, and "
             "answering with the wrong one is the whole danger of an X.",
             '[[step eq="next to 50° → 130° ✓"]][[step eq="opposite 50° → 50° (true, but not what was asked)"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. One angle is 60 degrees. Its "
                        "neighbour is 180 take away 60 — 120 degrees.",
                        '[[angle deg="180" split="60,120" caption="on one straight line: 60° + 120° = 180°"]][[step eq="180° − 60° = 120°"]]'),
             "ask": {'a': 68, 'b': 0, 'op': 'vert'}},
            {"worked": ("One more together. One angle is 35, so the angle beside it is "
                        "180 take away 35, which equals 145 degrees.",
                        '[[angle deg="180" split="35,145" caption="on one straight line: 35° + 145° = 180°"]][[step eq="180° − 35° = 145°"]]'),
             "ask": {'a': 22, 'b': 0, 'op': 'vert'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Two lines cross, "
                       "one angle is 50 degrees, and the angle next to it is 130. Tap "
                       "the reason why."),
            "choices": ("because the two neighbours share a straight line, which is 180 | "
                        "because opposite angles are twins, so it is 50 | because the "
                        "four angles share 360, so it is 310"),
            "answer": "because the two neighbours share a straight line, which is 180",
            "board": '[[angle deg="180" split="50,130" caption="50° + 130° = 180°"]]',
        },
        "recap": [
            ("So, here it is again. Where two lines cross, neighbours make 180 and "
             "opposites are equal. Read which one the question asks for, then use "
             "the right fact.",
             '[[angle deg="50" cross="50" caption="opposites are twins · neighbours make 180°"]]'),
            ("And that is one angle telling you all four.",
             '[[step eq="180° − 50° = 130°"]]'),
        ],
        "bank": [
            {"a": 70, "b": 0, "op": "vert"},
            {"a": 65, "b": 0, "op": "vert"},
            {"a": 59, "b": 0, "op": "vert"},
            {"a": 55, "b": 0, "op": "vert"},
            {"a": 49, "b": 0, "op": "vert"},
            {"a": 40, "b": 0, "op": "vert"},
            {"a": 34, "b": 0, "op": "vert"},
            {"a": 30, "b": 0, "op": "vert"},
            {"a": 25, "b": 0, "op": "vert"},
            {"a": 20, "b": 0, "op": "vert"},
        ],
    },
    {
        "id": "geo-u1-across-the-circle",
        "course": "geometry", "unit": 1,
        "topic": "Radius and diameter",
        "op": "circ", "max_value": 90,
        "levels": ("abstract",),
        "symbols": ("radius", "diameter"),
        "advance_line": "Three in a row, and you can say why — you've got it! The diameter is two radiuses.",
        "why": [
            ("Why the circle? Because a circle is every point the same distance from "
             "one middle point. That distance — middle to edge — is the radius. Draw "
             "it and you have the circle\'s one measurement; everything else about "
             "the circle follows from it, starting with the trip all the way across.",
             '[[goal text="Radius and diameter"]]'),
        ],
        "picture": [
            ("Here is a circle with its radius drawn: middle to edge, 5. Now go all "
             "the way across, edge to edge, through the middle — that is the "
             "diameter, drawn in red. It is simply two radiuses laid end to end: 5 "
             "and 5, so the diameter is 10.",
             '[[circle center="O" r="5" d="10" caption="radius 5, middle to edge — diameter 10, all the way across"]]'),
        ],
        "teach": [
            ("That is the method. The diameter is two radiuses end to end. If the "
             "radius is 5, the diameter is 2 times 5, which equals 10.",
             '[[circle center="O" r="5" d="10" caption="2 × 5 = 10"]][[step eq="diameter = 2 × 5 = 10"]]'),
            ("Two words, one relationship, and the danger is which way round. The "
             "diameter is the BIG one — all the way across. The radius is the small "
             "one — halfway. Doubling goes radius to diameter; halving comes back.",
             '[[step eq="radius 5 → diameter 10 ✓"]][[step eq="radius 5 → 2 or 3 ✗ — that is going the wrong way"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. A radius of 9 gives a diameter "
                        "of 2 times 9 — 18.",
                        '[[circle center="O" r="9" d="18" caption="2 × 9 = 18"]][[step eq="2 × 9 = 18"]]'),
             "ask": {'a': 14, 'b': 0, 'op': 'circ'}},
            {"worked": ("One more together. A radius of 11: the diameter is 2 times 11, "
                        "which equals 22.",
                        '[[circle center="O" r="11" d="22" caption="2 × 11 = 22"]][[step eq="2 × 11 = 22"]]'),
             "ask": {'a': 22, 'b': 0, 'op': 'circ'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A circle with a "
                       "radius of 5 has a diameter of 10. Tap the reason why."),
            "choices": ("because the diameter is two radiuses laid end to end | because "
                        "the diameter is half the radius | because the diameter is the "
                        "radius plus 5, whatever the radius"),
            "answer": "because the diameter is two radiuses laid end to end",
            "board": '[[circle center="O" r="5" d="10" caption="two radiuses end to end: 2 × 5 = 10"]]',
        },
        "recap": [
            ("So, here it is again. The radius runs middle to edge; the diameter runs "
             "all the way across through the middle, and it is two radiuses. Double "
             "to go out, halve to come back.",
             '[[circle center="O" r="5" d="10" caption="diameter = 2 × radius"]]'),
            ("And that is the circle\'s one measurement, and the first thing built "
             "from it.",
             '[[step eq="diameter = 2 × 5 = 10"]]'),
        ],
        "bank": [
            {"a": 4, "b": 0, "op": "circ"},
            {"a": 6, "b": 0, "op": "circ"},
            {"a": 8, "b": 0, "op": "circ"},
            {"a": 10, "b": 0, "op": "circ"},
            {"a": 12, "b": 0, "op": "circ"},
            {"a": 16, "b": 0, "op": "circ"},
            {"a": 20, "b": 0, "op": "circ"},
            {"a": 26, "b": 0, "op": "circ"},
            {"a": 32, "b": 0, "op": "circ"},
            {"a": 40, "b": 0, "op": "circ"},
        ],
    },
    {
        "id": "geo-u1-halfway-along",
        "course": "geometry", "unit": 1,
        "topic": "The midpoint",
        "op": "mid", "max_value": 60,
        "levels": ("abstract",),
        "symbols": ("midpoint", "halfway"),
        "advance_line": "Three in a row, and you can say why — you've got it! Add the two ends and share by two.",
        "why": [
            ("Why the midpoint? Because every line has an exact middle — the point "
             "halfway along, the same distance from both ends. Finding it is the "
             "first real construction in geometry, and every shape you will ever "
             "cut in half starts there.",
             '[[goal text="The midpoint"]]'),
        ],
        "picture": [
            ("Here is a line on the number line, running from 2 to 10, with the "
             "halfway mark drawn. It falls on 6 — and look: 6 is 4 away from 2, and "
             "4 away from 10. Equal both ways. That point is the midpoint.",
             '[[numberline min="1" max="11" points="2,6,10" mid="6" caption="ends 2 and 10 — the middle is 6, 4 each way"]]'),
        ],
        "teach": [
            ("That is the method. Add the two ends: 2 plus 10 equals 12. Share by "
             "two: 6. And check it — 6 is 4 away from 2, and 4 away from 10. Equal "
             "both ways, so 6 is the midpoint.",
             '[[numberline min="1" max="11" points="2,6,10" mid="6" caption="ends 2 and 10, middle 6"]][[step eq="(2 + 10) ÷ 2 = 6"]]'),
            ("Both ends go in. Halving the far end alone gives 5, and 5 is not the "
             "middle of this line — it only would be if the line started at zero. "
             "And do not answer with the LENGTH: the line is 8 long, but it is 6 "
             "that sits halfway.",
             '[[step eq="midpoint = 6 ✓"]][[step eq="10 ÷ 2 = 5 ✗ · length 8 ✗"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. From 3 to 13. Add: 16. Share by "
                        "two: the midpoint is 8.",
                        '[[numberline min="2" max="14" points="3,8,13" mid="8" caption="ends 3 and 13, middle 8"]][[step eq="(3 + 13) ÷ 2 = 8"]]'),
             "ask": {'a': 2, 'b': 18, 'op': 'mid'}},
            {"worked": ("One more together. From 6 to 22: 6 plus 22 equals 28, shared "
                        "by two is 14.",
                        '[[numberline min="5" max="23" points="6,14,22" mid="14" caption="ends 6 and 22, middle 14"]][[step eq="(6 + 22) ÷ 2 = 14"]]'),
             "ask": {'a': 10, 'b': 32, 'op': 'mid'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A line runs from 2 "
                       "to 10, and its midpoint is 6. Tap the reason why."),
            "choices": ("because 6 is the same distance from both ends | because half "
                        "of 10 is 5, near enough to 6 | because the line is 8 long, so "
                        "the middle is 8"),
            "answer": "because 6 is the same distance from both ends",
            "board": '[[numberline min="1" max="11" points="2,6,10" mid="6" caption="ends 2 and 10, middle 6"]]',
        },
        "recap": [
            ("So, here it is again. The midpoint is the same distance from both "
             "ends: add the two ends and share by two. Both ends go in, and the "
             "answer is a place, not a length.",
             '[[numberline min="1" max="11" points="2,6,10" mid="6" caption="(2 + 10) ÷ 2 = 6"]]'),
            ("And that is the first construction in geometry: a line, cut exactly in "
             "half.",
             '[[step eq="(2 + 10) ÷ 2 = 6"]]'),
        ],
        "bank": [
            {"a": 2, "b": 8, "op": "mid"},
            {"a": 2, "b": 14, "op": "mid"},
            {"a": 6, "b": 14, "op": "mid"},
            {"a": 4, "b": 16, "op": "mid"},
            {"a": 4, "b": 20, "op": "mid"},
            {"a": 8, "b": 20, "op": "mid"},
            {"a": 6, "b": 24, "op": "mid"},
            {"a": 10, "b": 28, "op": "mid"},
            {"a": 8, "b": 34, "op": "mid"},
            {"a": 12, "b": 40, "op": "mid"},
        ],
    },
]
LESSONS.extend(_GEOMETRY_U1)


# =============================================================================
# GEOMETRY -- UNIT 2: TRANSFORMATIONS & SYMMETRY (build ld, 2026-08-22)
# =============================================================================
# THE THREE MOVES, EACH WITH ONE COORDINATE RULE: a slide changes one number by
# adding, a flip changes ONE sign, a half turn changes BOTH -- and the closing
# lesson asks when a shape's turn lands it back on itself. Every wrong tap in the
# unit is the right rule aimed at the WRONG coordinate, the wrong direction, or
# the wrong number of signs. [[graph points=]] carries the moving point; ask
# boards never draw the image point (the kz/la giveaway class).
_GEOMETRY_U2 = [
    {
        "id": "geo-u2-slide-it-over",
        "course": "geometry", "unit": 2,
        "topic": "The slide",
        "op": "tran", "max_value": 14,
        "levels": ("abstract",),
        "symbols": ("slide", "coordinates"),
        "advance_line": "Three in a row, and you can say why — you've got it! A slide right changes only x.",
        "why": [
            ("Why move a shape? Because geometry can. The first move is a slide — "
             "every point travels the same distance in the same direction, and the "
             "shape never turns or flips. Mathematicians call a slide a translation. "
             "On the grid, a point\'s address is its two coordinates: x across, then "
             "y up.",
             '[[goal text="Slide it over"]]'),
        ],
        "picture": [
            ("Here is the point at 3 across and 5 up. Slide it 4 to the right and it "
             "lands at 7 across, 5 up — the second dot. Only the ACROSS number "
             "changed: 3 became 7. The height, 5, is exactly where it was.",
             '[[graph points="(3,5),(7,5)" range="0..14" yrange="0..10" caption="from (3, 5) to (7, 5) — right 4, same height"]]'),
        ],
        "teach": [
            ("That is the method. Take the point at 3 across and 5 up. Slide it 4 to "
             "the right. Only the ACROSS number changes: x goes from 3 to 3 plus 4, "
             "which equals 7. The point lands at 7 across, 5 up.",
             '[[graph points="(3,5),(7,5)" range="0..14" yrange="0..10" caption="from (3, 5) to (7, 5)"]][[step eq="x: 3 + 4 = 7 · y stays 5"]]'),
            ("Here is the trap: a slide to the RIGHT touches only x. The y number "
             "never hears about it. Adding the slide to y — or sliding x the wrong "
             "way — puts the point in the wrong place. Say the move out loud first: "
             "right means x grows.",
             '[[step eq="right 4: x + 4 ✓"]][[step eq="y + 4 ✗ — y never moved"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. The point (2, 6) slides 3 to the "
                        "right. New x: 2 plus 3 equals 5. It lands at (5, 6).",
                        '[[graph points="(2,6),(5,6)" range="0..14" yrange="0..10" caption="from (2, 6) to (5, 6) — right 3"]][[step eq="x: 2 + 3 = 5"]]'),
             "ask": {'a': 4, 'b': 6, 'c': 2, 'op': 'tran'}},
            {"worked": ("One more together. (6, 4) slides 2 to the right: x is 6 plus 2, "
                        "which equals 8 — the point lands at (8, 4).",
                        '[[graph points="(6,4),(8,4)" range="0..14" yrange="0..10" caption="from (6, 4) to (8, 4) — right 2"]][[step eq="x: 6 + 2 = 8"]]'),
             "ask": {'a': 7, 'b': 3, 'c': 4, 'op': 'tran'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. The point 3 comma "
                       "5 slides 4 to the right, and its new x is 7. Tap the reason "
                       "why."),
            "choices": ("because a slide right adds to x only: 3 plus 4 | "
                        "because a slide right adds 4 to both numbers | because a "
                        "slide right takes 4 off x"),
            "answer": "because a slide right adds to x only: 3 plus 4",
            "board": '[[graph points="(3,5),(7,5)" range="0..14" yrange="0..10" caption="from (3, 5) to (7, 5)"]]',
        },
        "recap": [
            ("So, here it is again. A slide moves every point the same way. A slide "
             "to the right adds to x and leaves y alone — say the direction first, "
             "then change only the number that direction touches.",
             '[[graph points="(3,5),(7,5)" range="0..14" yrange="0..10" caption="x: 3 + 4 = 7 · y stays 5"]]'),
            ("And that is the first of the three moves, a translation.",
             '[[step eq="(3, 5) → (7, 5)"]]'),
        ],
        "bank": [
            {"a": 3, "b": 6, "c": 2, "op": "tran"},
            {"a": 4, "b": 7, "c": 2, "op": "tran"},
            {"a": 5, "b": 2, "c": 2, "op": "tran"},
            {"a": 4, "b": 8, "c": 3, "op": "tran"},
            {"a": 6, "b": 3, "c": 2, "op": "tran"},
            {"a": 5, "b": 9, "c": 3, "op": "tran"},
            {"a": 6, "b": 2, "c": 3, "op": "tran"},
            {"a": 7, "b": 4, "c": 3, "op": "tran"},
            {"a": 8, "b": 3, "c": 4, "op": "tran"},
            {"a": 9, "b": 5, "c": 4, "op": "tran"},
        ],
    },
    {
        "id": "geo-u2-flip-it-across",
        "course": "geometry", "unit": 2,
        "topic": "The flip",
        "op": "refl", "max_value": 9, "min_value": -9,
        "levels": ("abstract",),
        "symbols": ("flip", "mirror"),
        "advance_line": "Three in a row, and you can say why — you've got it! A flip across the y line changes only the sign of x.",
        "why": [
            ("Why a flip? Because the second move is a mirror. Stand a mirror "
             "upright on the y line — the line where x is zero — and every point "
             "jumps to the other side, the same distance away. A flip is also "
             "called a reflection, and it is how a left hand becomes a right hand.",
             '[[goal text="Flip it across"]]'),
        ],
        "picture": [
            ("Here is the mirror, the line x equals 0, with the point 4 across, 6 up "
             "on its right. Its reflection is the dot on the left: the same height, "
             "6, the same distance from the mirror, 4 — just on the other side. Its "
             "x is negative 4.",
             '[[graph lines="x=0" points="(4,6),(-4,6)" range="-9..9" yrange="0..10" caption="the mirror on x = 0 — (4, 6) and its reflection (−4, 6)"]]'),
        ],
        "teach": [
            ("That is the method. Take the point at 4 across, 6 up. Flip it across "
             "the y line. Its height does not change, and its distance from the "
             "mirror does not change — only the SIDE changes. New x: the sign flips, "
             "and 4 becomes negative 4. The point lands at negative 4 across, 6 up.",
             '[[graph lines="x=0" points="(4,6),(-4,6)" range="-9..9" yrange="0..10" caption="from (4, 6) to (−4, 6)"]][[step eq="x: 4 → −4 · y stays 6"]]'),
            ("The trap is flipping the wrong number. Across the y line it is x that "
             "crosses over — y is the height, and a mirror standing on the floor "
             "does not change heights. Ask yourself: which side am I on now? After "
             "the flip, the other one.",
             '[[step eq="x changes sign ✓"]][[step eq="y changes sign ✗ — the mirror does not change heights"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. The point (5, 2) flips across "
                        "the y line: x goes from 5 to negative 5, and y stays 2. It "
                        "lands at (−5, 2).",
                        '[[graph lines="x=0" points="(5,2),(-5,2)" range="-9..9" yrange="0..8" caption="from (5, 2) to (−5, 2)"]][[step eq="x: 5 → −5"]]'),
             "ask": {'a': 3, 'b': 8, 'op': 'refl'}},
            {"worked": ("One more together. (8, 3) flips across the y line — the new x "
                        "is negative 8, and y is still 3.",
                        '[[graph lines="x=0" points="(8,3),(-8,3)" range="-9..9" yrange="0..8" caption="from (8, 3) to (−8, 3)"]][[step eq="x: 8 → −8"]]'),
             "ask": {'a': 6, 'b': 9, 'op': 'refl'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. The point 4 comma "
                       "6 flips across the y line, and its new x is negative 4. Tap "
                       "the reason why."),
            "choices": ("because the point crosses to the other side of the mirror | "
                        "because a flip changes the height, so y becomes negative | "
                        "because a flip slides the point 4 to the left"),
            "answer": "because the point crosses to the other side of the mirror",
            "board": '[[graph lines="x=0" points="(4,6),(-4,6)" range="-9..9" yrange="0..10" caption="from (4, 6) to (−4, 6)"]]',
        },
        "recap": [
            ("So, here it is again. A flip across the y line sends every point to "
             "the other side of the mirror, the same height and the same distance "
             "away. Only the sign of x changes; y never hears about it.",
             '[[graph lines="x=0" points="(4,6),(-4,6)" range="-9..9" yrange="0..10" caption="x: 4 → −4 · y stays 6"]]'),
            ("And that is the second move, a reflection.",
             '[[step eq="(4, 6) → (−4, 6)"]]'),
        ],
        "bank": [
            {"a": 2, "b": 7, "op": "refl"},
            {"a": 3, "b": 5, "op": "refl"},
            {"a": 4, "b": 7, "op": "refl"},
            {"a": 5, "b": 3, "op": "refl"},
            {"a": 5, "b": 8, "op": "refl"},
            {"a": 6, "b": 4, "op": "refl"},
            {"a": 7, "b": 2, "op": "refl"},
            {"a": 7, "b": 9, "op": "refl"},
            {"a": 8, "b": 5, "op": "refl"},
            {"a": 9, "b": 6, "op": "refl"},
        ],
    },
    {
        "id": "geo-u2-half-turn",
        "course": "geometry", "unit": 2,
        "topic": "The half turn",
        "op": "htrn", "max_value": 9, "min_value": -9,
        "levels": ("abstract",),
        "symbols": ("half turn", "opposite"),
        "advance_line": "Three in a row, and you can say why — you've got it! A half turn changes both signs.",
        "why": [
            ("Why a turn? Because the third move spins the grid. Today\'s turn is "
             "the simplest and the strongest: a half turn — spin the grid half way "
             "around the middle point (0, 0), like turning a page upside down. Every "
             "point travels to the exact opposite spot.",
             '[[goal text="The half turn"]]'),
        ],
        "picture": [
            ("Here is the point 4 across, 3 up, and the middle of the grid at (0, "
             "0). Turn the whole grid half way around that middle, and the point "
             "lands at the second dot: 4 the OTHER way across and 3 the OTHER way "
             "up — negative 4, negative 3. The exact opposite spot.",
             '[[graph points="(4,3),(-4,-3)" range="-9..9" yrange="-9..9" caption="from (4, 3) to (−4, −3) — a half turn around (0, 0)"]]'),
        ],
        "teach": [
            ("That is the method. Take the point 4 across, 3 up. A half turn around "
             "(0, 0) sends it 4 the OTHER way across and 3 the OTHER way up: both "
             "numbers keep their size and change their sign. It lands at negative 4 "
             "across, negative 3 up.",
             '[[graph points="(4,3),(-4,-3)" range="-9..9" yrange="-9..9" caption="from (4, 3) to (−4, −3)"]][[step eq="(4, 3) → (−4, −3)"]]'),
            ("Compare the moves you know. A slide changes one number by adding. A "
             "flip changes ONE sign. The half turn changes BOTH signs — x and y each "
             "cross to the other side. Changing only one sign is a flip, not a turn "
             "— that is the trap.",
             '[[step eq="half turn: both signs change ✓"]][[step eq="only one sign ✗ — that is a flip"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. (2, 5) turns half way around "
                        "(0, 0): both signs change, so it lands at (−2, −5). The new y "
                        "is negative 5.",
                        '[[graph points="(2,5),(-2,-5)" range="-9..9" yrange="-9..9" caption="from (2, 5) to (−2, −5)"]][[step eq="(2, 5) → (−2, −5)"]]'),
             "ask": {'a': 6, 'b': 3, 'op': 'htrn'}},
            {"worked": ("One more together. (7, 4) turns half way around (0, 0) and "
                        "lands at (−7, −4) — the new y is negative 4.",
                        '[[graph points="(7,4),(-7,-4)" range="-9..9" yrange="-9..9" caption="from (7, 4) to (−7, −4)"]][[step eq="(7, 4) → (−7, −4)"]]'),
             "ask": {'a': 4, 'b': 8, 'op': 'htrn'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. The point 4 comma "
                       "3 turns half way around 0 comma 0, and its new y is negative "
                       "3. Tap the reason why."),
            "choices": ("because a half turn lands on the opposite spot: both signs change | "
                        "because a half turn is a flip, so only x changes | because "
                        "a half turn adds 3 to each number"),
            "answer": "because a half turn lands on the opposite spot: both signs change",
            "board": '[[graph points="(4,3),(-4,-3)" range="-9..9" yrange="-9..9" caption="from (4, 3) to (−4, −3)"]]',
        },
        "recap": [
            ("So, here it is again. A half turn around (0, 0) carries every point to "
             "the exact opposite spot: both numbers keep their size and change their "
             "sign. One sign is a flip; both signs is the half turn.",
             '[[graph points="(4,3),(-4,-3)" range="-9..9" yrange="-9..9" caption="(4, 3) → (−4, −3)"]]'),
            ("And that is the third move, a rotation.",
             '[[step eq="(4, 3) → (−4, −3)"]]'),
        ],
        "bank": [
            {"a": 5, "b": 2, "op": "htrn"},
            {"a": 7, "b": 3, "op": "htrn"},
            {"a": 9, "b": 4, "op": "htrn"},
            {"a": 3, "b": 5, "op": "htrn"},
            {"a": 8, "b": 5, "op": "htrn"},
            {"a": 4, "b": 6, "op": "htrn"},
            {"a": 9, "b": 7, "op": "htrn"},
            {"a": 2, "b": 7, "op": "htrn"},
            {"a": 3, "b": 8, "op": "htrn"},
            {"a": 5, "b": 9, "op": "htrn"},
        ],
    },
    {
        "id": "geo-u2-turns-onto-itself",
        "course": "geometry", "unit": 2,
        "topic": "Turn symmetry",
        "op": "rota", "max_value": 120,
        "levels": ("abstract",),
        "symbols": ("turn", "degrees"),
        "advance_line": "Three in a row, and you can say why — you've got it! Equal parts share the full 360.",
        "why": [
            ("Why do some shapes come back? Because turn a square a quarter of the "
             "way around and it lands exactly on itself — you cannot tell it ever "
             "moved. That is called turn symmetry, and the question is always the "
             "same one: how many degrees is the smallest turn that works?",
             '[[goal text="It turns onto itself"]]'),
        ],
        "picture": [
            ("Here is a wheel cut into 6 equal parts, all alike. One full turn — all "
             "the way around — is 360 degrees, and the wheel lands on itself 6 times "
             "in that full turn, once for every part. So each part is 360 divided "
             "by 6: 60 degrees, and a 60 degree turn is the smallest that works.",
             '[[pie parts="6" caption="6 equal parts — each is 60° of the full 360°"]]'),
        ],
        "teach": [
            ("That is the method. One full turn is 360 degrees. A wheel cut into 6 "
             "equal parts lands on itself 6 times in one full turn, so the smallest "
             "working turn is 360 divided by 6, which equals 60 degrees.",
             '[[pie parts="6" caption="6 equal parts"]][[step eq="360° ÷ 6 = 60°"]]'),
            ("Two traps. Half a turn, 180, feels safe — but a wheel with 12 equal "
             "parts lands on itself long before 180; only the sharing rule finds the "
             "smallest turn, 30. And the number of parts is a COUNT, not an angle — "
             "12 parts is an answer in pieces, not in degrees.",
             '[[pie parts="12" caption="12 equal parts"]][[step eq="360° ÷ 12 = 30° ✓ · 180° ✗ · 12 ✗"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. A wheel with 12 equal parts: "
                        "360 divided by 12 equals 30, so a 30 degree turn lands it on "
                        "itself.",
                        '[[pie parts="12" caption="12 equal parts — 30° each"]][[step eq="360° ÷ 12 = 30°"]]'),
             "ask": {'a': 4, 'b': 0, 'op': 'rota'}},
            {"worked": ("One more together. 6 equal parts: 360 divided by 6 equals 60 "
                        "degrees.",
                        '[[pie parts="6" caption="6 equal parts — 60° each"]][[step eq="360° ÷ 6 = 60°"]]'),
             "ask": {'a': 3, 'b': 0, 'op': 'rota'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A wheel with 6 "
                       "equal parts first lands on itself after a 60 degree turn. Tap "
                       "the reason why."),
            "choices": ("because 6 equal parts share the full turn of 360 | because "
                        "every wheel lands on itself at a half turn, 180 | because the "
                        "answer is the number of parts, 6"),
            "answer": "because 6 equal parts share the full turn of 360",
            "board": '[[pie parts="6" caption="360° ÷ 6 = 60°"]]',
        },
        "recap": [
            ("So, here it is again. A wheel of equal parts lands on itself once per "
             "part, so the smallest turn is the full 360 shared between the parts. "
             "Not 180 by habit, and not the count of parts — degrees.",
             '[[pie parts="6" caption="360° ÷ 6 = 60°"]]'),
            ("And that is turn symmetry: a shape that comes back.",
             '[[step eq="360° ÷ 6 = 60°"]]'),
        ],
        "bank": [
            {"a": 5, "b": 0, "op": "rota"},
                        {"a": 8, "b": 0, "op": "rota"},
            {"a": 9, "b": 0, "op": "rota"},
            {"a": 10, "b": 0, "op": "rota"},
                        {"a": 15, "b": 0, "op": "rota"},
            {"a": 18, "b": 0, "op": "rota"},
            {"a": 20, "b": 0, "op": "rota"},
            {"a": 24, "b": 0, "op": "rota"},
        ],
    },
]
LESSONS.extend(_GEOMETRY_U2)


# =============================================================================
# GEOMETRY -- UNIT 3: CONGRUENCE & TRIANGLE PROOFS (build ld, 2026-08-22)
# =============================================================================
# CONGRUENT MEANS EVERY MATCHING PART IS EQUAL -- and the LETTERS, not the
# picture, say which parts match (the copy may be turned or flipped, which is
# exactly what Unit 2 just taught). Then the first proofs: the isosceles pair
# read in both directions, and the exterior angle built out of two facts the
# child already owns. [[triangle ticks=]] finally draws the equal-side marks it
# was built for in July.
_GEOMETRY_U3 = [
    {
        "id": "geo-u3-matching-parts",
        "course": "geometry", "unit": 3,
        "topic": "Matching parts",
        "op": "cong", "max_value": 20,
        "levels": ("abstract",),
        "symbols": ("congruent", "matching"),
        "advance_line": "Three in a row, and you can say why — you've got it! The letters name the matching parts.",
        "why": [
            ("Why congruent? Because two shapes are congruent when one is an exact "
             "copy of the other — every side the same length, every angle the same "
             "size. The word does real work in proofs: say two triangles are "
             "congruent and you have said six things at once, three sides and three "
             "angles, all matching.",
             '[[goal text="Matching parts"]]'),
        ],
        "picture": [
            ("Here is triangle ABC with its sides — 4, 7 and 5 — and beside it its "
             "copy, triangle DEF, with the same three sides. The LETTERS say which "
             "side matches which: A matches D, B matches E, C matches F. So side CA, "
             "which is 5, matches side FD — and FD is 5.",
             '[[triangle v="A,B,C" sides="4,7,5" caption="ABC — sides 4, 7, 5"]][[triangle v="D,E,F" sides="4,7,5" caption="DEF — its copy: A↔D, B↔E, C↔F"]]'),
        ],
        "teach": [
            ("That is the method. Triangle ABC congruent to triangle DEF means A "
             "matches D, B matches E, and C matches F — in that exact order. So side "
             "AB matches side DE, side BC matches side EF, and side CA matches side "
             "FD.",
             '[[triangle v="A,B,C" sides="4,7,5" caption="ABC"]][[step eq="A↔D · B↔E · C↔F"]][[step eq="AB↔DE · BC↔EF · CA↔FD"]]'),
            ("The trap is matching by eye. The copy may be turned or flipped on the "
             "page — Unit 2 taught you exactly those moves — so the side that LOOKS "
             "right is often wrong. Trust the letters, never the picture: spell the "
             "side you want, then swap each letter for its partner.",
             '[[step eq="FD → swap F for C, D for A → CA ✓"]][[step eq="by eye ✗ — the copy may be turned"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Triangles ABC and DEF are "
                        "congruent. CA is 4, so side FD — swap F for C and D for A — is "
                        "4 as well.",
                        '[[triangle v="A,B,C" sides="3,5,4" caption="ABC — CA is 4"]][[triangle v="D,E,F" sides="3,5,4" caption="DEF — FD is 4"]][[step eq="FD ↔ CA = 4"]]'),
             "ask": {'a': 5, 'b': 7, 'c': 6, 'op': 'cong'}},
            {"worked": ("One more together. AB is 8, BC is 10 and CA is 7. F matches C "
                        "and D matches A, so side FD is 7.",
                        '[[triangle v="A,B,C" sides="8,10,7" caption="ABC — CA is 7"]][[triangle v="D,E,F" sides="8,10,7" caption="DEF — FD is 7"]][[step eq="FD ↔ CA = 7"]]'),
             "ask": {'a': 12, 'b': 9, 'c': 11, 'op': 'cong'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Triangles ABC and "
                       "DEF are congruent, CA is 5, and so FD is 5. Tap the reason "
                       "why."),
            "choices": ("because F matches C and D matches A, so FD matches CA | "
                        "because FD is the side that looks the same on the page | "
                        "because FD is the last side named, so it is the longest"),
            "answer": "because F matches C and D matches A, so FD matches CA",
            "board": '[[triangle v="A,B,C" sides="4,7,5" caption="ABC — CA is 5"]][[triangle v="D,E,F" sides="4,7,5" caption="DEF — FD is 5"]]',
        },
        "recap": [
            ("So, here it is again. Congruent means an exact copy, and the letters "
             "name the matching parts in order. Spell the side you want, swap each "
             "letter for its partner, and read the length — never match by eye.",
             '[[triangle v="A,B,C" sides="4,7,5" caption="A↔D · B↔E · C↔F"]]'),
            ("And that is six facts said in one word.",
             '[[step eq="FD ↔ CA = 5"]]'),
        ],
        "bank": [
            {"a": 4, "b": 6, "c": 3, "op": "cong"},
            {"a": 7, "b": 5, "c": 4, "op": "cong"},
            {"a": 3, "b": 6, "c": 5, "op": "cong"},
            {"a": 8, "b": 4, "c": 6, "op": "cong"},
            {"a": 5, "b": 9, "c": 7, "op": "cong"},
            {"a": 10, "b": 6, "c": 8, "op": "cong"},
            {"a": 6, "b": 12, "c": 9, "op": "cong"},
            {"a": 14, "b": 8, "c": 10, "op": "cong"},
            {"a": 9, "b": 15, "c": 12, "op": "cong"},
            {"a": 16, "b": 10, "c": 14, "op": "cong"},
        ],
    },
    {
        "id": "geo-u3-two-equal-sides",
        "course": "geometry", "unit": 3,
        "topic": "Two equal sides",
        "op": "isos", "max_value": 180,
        "levels": ("abstract",),
        "symbols": ("isosceles", "base angles"),
        "advance_line": "Three in a row, and you can say why — you've got it! Both base angles go in before the top comes out.",
        "why": [
            ("Why the ticks? Because some triangles carry a secret pair. When two "
             "sides are the same length, we mark them with little ticks. That "
             "triangle is called isosceles. Its two base angles, the pair down at "
             "the bottom, are equal to each other. Equal sides face equal angles: "
             "that is the whole secret.",
             '[[goal text="Two equal sides"]]'),
        ],
        "picture": [
            ("Here is an isosceles triangle, the two equal sides ticked, with base "
             "angles of 52 and 52. Every triangle\'s three angles come to 180, so the "
             "top gets what the pair leaves: 52 and 52 use 104, and 180 take away "
             "104 is 76. The top angle is 76.",
             '[[triangle v="A,B,C" ticks="BC,CA" angles="52,52,76" caption="base angles 52° and 52° — the top is 76°"]]'),
        ],
        "teach": [
            ("That is the method. Every triangle\'s three angles put together are 180 "
             "degrees — you proved that back in prealgebra. So if each base angle is "
             "52, the two of them use 104, and the top angle gets what is left over: "
             "180 take away 104 equals 76 degrees.",
             '[[triangle v="A,B,C" ticks="BC,CA" angles="52,52," caption="base angles 52° — the top is waiting"]][[step eq="52° + 52° + ? = 180°"]][[step eq="180° − 104° = 76°"]]'),
            ("The trap is forgetting there are TWO base angles. Take away only one 52 "
             "and you get 128 — too big, because its twin is still sitting inside "
             "the triangle. Both base angles go in before the top angle comes out.",
             '[[step eq="180 − 52 − 52 = 76 ✓"]][[step eq="180 − 52 = 128 ✗ — the twin is still inside"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Each base angle is 30. The two "
                        "use 60 put together, and the top angle is 180 take away 60 — "
                        "120 degrees.",
                        '[[triangle v="A,B,C" ticks="BC,CA" angles="30,30,120" caption="30° + 30° + 120° = 180°"]][[step eq="180° − 60° = 120°"]]'),
             "ask": {'a': 20, 'b': 0, 'op': 'isos'}},
            {"worked": ("One more together. Base angles of 45 each: 90 put together, so "
                        "the top is 180 take away 90 — 90 degrees, a right angle.",
                        '[[triangle v="A,B,C" ticks="BC,CA" right="C" angles="45,45,90" caption="45° + 45° + 90° = 180°"]][[step eq="180° − 90° = 90°"]]'),
             "ask": {'a': 72, 'b': 0, 'op': 'isos'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. An isosceles "
                       "triangle has base angles of 52 each, and its top angle is 76. "
                       "Tap the reason why."),
            "choices": ("because both base angles come out of 180 before the top | "
                        "because only one base angle comes out of 180 | because the "
                        "top angle is always the same as a base angle"),
            "answer": "because both base angles come out of 180 before the top",
            "board": '[[triangle v="A,B,C" ticks="BC,CA" angles="52,52,76" caption="52° + 52° + 76° = 180°"]]',
        },
        "recap": [
            ("So, here it is again. Two equal sides face two equal base angles. Both "
             "base angles come out of the 180 first — the pair, not one — and the "
             "top angle is what is left.",
             '[[triangle v="A,B,C" ticks="BC,CA" angles="52,52,76" caption="180° − 52° − 52° = 76°"]]'),
            ("And that is the secret pair, read from the ticks.",
             '[[step eq="180° − 104° = 76°"]]'),
        ],
        "bank": [
            {"a": 25, "b": 0, "op": "isos"},
            {"a": 29, "b": 0, "op": "isos"},
            {"a": 35, "b": 0, "op": "isos"},
            {"a": 40, "b": 0, "op": "isos"},
            {"a": 44, "b": 0, "op": "isos"},
            {"a": 50, "b": 0, "op": "isos"},
            {"a": 55, "b": 0, "op": "isos"},
            {"a": 65, "b": 0, "op": "isos"},
            {"a": 70, "b": 0, "op": "isos"},
            {"a": 75, "b": 0, "op": "isos"},
        ],
    },
    {
        "id": "geo-u3-the-outside-angle",
        "course": "geometry", "unit": 3,
        "topic": "The exterior angle",
        "op": "extr", "max_value": 180,
        "levels": ("abstract",),
        "symbols": ("exterior", "straight line"),
        "advance_line": "Three in a row, and you can say why — you've got it! The exterior angle equals the two far angles put together.",
        "why": [
            ("Why open a door? Because take any triangle and stretch one side out "
             "past the corner, like opening a door, and the new angle outside the "
             "triangle is called the exterior angle. It comes with the first little "
             "proof of this course — and you already own both facts it needs: a "
             "straight line is 180, and so are the three angles inside a triangle.",
             '[[goal text="The outside angle"]]'),
        ],
        "picture": [
            ("Here is a triangle with angles of 40, 60 and 80 — the 80 is the inside "
             "corner where the door opens. The exterior angle sits with that 80 on "
             "one straight line, so it is 180 take away 80: 100. And look — 100 is "
             "exactly 40 plus 60, the two far angles put together.",
             '[[triangle v="A,B,C" angles="40,60,80" caption="inside corner 80° — the exterior is 180° − 80° = 100° = 40° + 60°"]]'),
        ],
        "teach": [
            ("That is the proof. Angles of 40 and 60 leave the inside corner at 180 "
             "take away 100 — 80 degrees. The inside corner and the exterior angle "
             "sit together on one straight line, so the exterior is 180 take away "
             "80 — 100 degrees. And 100 is exactly 40 plus 60.",
             '[[triangle v="A,B,C" angles="40,60," caption="angles 40° and 60° — the third corner opened out"]][[step eq="inside: 180 − 40 − 60 = 80"]][[step eq="exterior: 180 − 80 = 100 = 40 + 60"]]'),
            ("That is the shortcut, proved once and yours forever: the exterior "
             "angle equals the two FAR angles put together. The trap is answering "
             "with the inside corner instead — 80 sits inside the triangle, and the "
             "question points outside.",
             '[[step eq="exterior = the two far angles put together"]][[step eq="the inside corner ✗ — that is the exterior\'s neighbour"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Far angles of 30 and 50: the "
                        "exterior angle is 30 plus 50, which equals 80 degrees.",
                        '[[triangle v="A,B,C" angles="30,50,100" caption="inside corner 100° — exterior 80° = 30° + 50°"]][[step eq="exterior = 30° + 50° = 80°"]]'),
             "ask": {'a': 35, 'b': 35, 'op': 'extr'}},
            {"worked": ("One more together. 45 and 60: the exterior angle is 45 plus 60, "
                        "which equals 105 degrees.",
                        '[[triangle v="A,B,C" angles="45,60,75" caption="inside corner 75° — exterior 105° = 45° + 60°"]][[step eq="exterior = 45° + 60° = 105°"]]'),
             "ask": {'a': 75, 'b': 50, 'op': 'extr'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A triangle has "
                       "angles of 40 and 60, and its exterior angle is 100. Tap the "
                       "reason why."),
            "choices": ("because the exterior equals the two far angles put together | "
                        "because the exterior equals the inside corner, 80 | because "
                        "the exterior is 180 take away the bigger far angle"),
            "answer": "because the exterior equals the two far angles put together",
            "board": '[[triangle v="A,B,C" angles="40,60,80" caption="exterior 100° = 40° + 60°"]]',
        },
        "recap": [
            ("So, here it is again. The exterior angle and the inside corner share "
             "a straight line, and the three inside angles share 180 — so the "
             "exterior equals the two far angles put together. Proved once, yours "
             "forever.",
             '[[triangle v="A,B,C" angles="40,60,80" caption="exterior = 40° + 60° = 100°"]]'),
            ("And that is the first little proof of the course.",
             '[[step eq="exterior = 40° + 60° = 100°"]]'),
        ],
        "bank": [
            {"a": 25, "b": 40, "op": "extr"},
            {"a": 30, "b": 45, "op": "extr"},
            {"a": 45, "b": 35, "op": "extr"},
            {"a": 40, "b": 45, "op": "extr"},
            {"a": 55, "b": 40, "op": "extr"},
            {"a": 60, "b": 45, "op": "extr"},
            {"a": 50, "b": 60, "op": "extr"},
            {"a": 65, "b": 55, "op": "extr"},
            {"a": 70, "b": 60, "op": "extr"},
            {"a": 80, "b": 65, "op": "extr"},
        ],
    },
    {
        "id": "geo-u3-share-the-rest",
        "course": "geometry", "unit": 3,
        "topic": "Base angles from the apex",
        "op": "chas", "max_value": 180,
        "levels": ("abstract",),
        "symbols": ("apex", "base angles"),
        "advance_line": "Three in a row, and you can say why — you've got it! Take the apex out first, then share the rest.",
        "why": [
            ("Why the other direction? Because yesterday\'s triangle ran base to top. "
             "Today runs top to base — given the apex, the single angle up where the "
             "two equal sides meet, find the pair of equal base angles below. Same "
             "triangle, same 180, read the other way.",
             '[[goal text="Share the rest"]]'),
        ],
        "picture": [
            ("Here is the isosceles triangle with its apex marked 40 and the base "
             "angles waiting. The three angles come to 180, so the apex leaves 140 "
             "for the pair. They are equal, so each takes half: 70 and 70. All "
             "three labelled, they add back to 180.",
             '[[triangle v="A,B,C" ticks="BC,CA" angles="70,70,40" caption="apex 40° — the base angles share 140°: 70° each"]]'),
        ],
        "teach": [
            ("That is the method. Say the apex is 40. The three angles put together "
             "are 180, so the two base angles share what the apex leaves behind: 180 "
             "take away 40 is 140. They are equal, so they split it evenly — 140 "
             "divided by 2 equals 70 degrees each.",
             '[[triangle v="A,B,C" ticks="BC,CA" angles=",,40" caption="apex 40° — the base angles share the rest"]][[step eq="180° − 40° = 140°"]][[step eq="140° ÷ 2 = 70°"]]'),
            ("Two traps, and both are about order. Stop at 140 and you have the "
             "PAIR\'s share, not one angle — it still belongs to two corners. And "
             "halving 180 first gives 90 take away 40 — 50 — which shares the "
             "triangle out before the apex took its part. Take the apex out first, "
             "then share.",
             '[[step eq="(180 − 40) ÷ 2 = 70 ✓"]][[step eq="140 ✗ belongs to two corners · 90 − 40 = 50 ✗ shared too soon"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Apex 36: 180 take away 36 is "
                        "144, and 144 divided by 2 equals 72 — each base angle is 72 "
                        "degrees.",
                        '[[triangle v="A,B,C" ticks="BC,CA" angles="72,72,36" caption="72° + 72° + 36° = 180°"]][[step eq="(180° − 36°) ÷ 2 = 72°"]]'),
             "ask": {'a': 24, 'b': 0, 'op': 'chas'}},
            {"worked": ("One more together. Apex 48: 180 take away 48 is 132, shared by "
                        "two is 66 degrees.",
                        '[[triangle v="A,B,C" ticks="BC,CA" angles="66,66,48" caption="66° + 66° + 48° = 180°"]][[step eq="(180° − 48°) ÷ 2 = 66°"]]'),
             "ask": {'a': 56, 'b': 0, 'op': 'chas'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. An isosceles "
                       "triangle has its apex at 40, and each base angle is 70. Tap "
                       "the reason why."),
            "choices": ("because the apex leaves 140, shared equally by two angles | "
                        "because 140 is what is left, so each base angle is 140 | "
                        "because you halve 180 first, then take the apex away"),
            "answer": "because the apex leaves 140, shared equally by two angles",
            "board": '[[triangle v="A,B,C" ticks="BC,CA" angles="70,70,40" caption="(180° − 40°) ÷ 2 = 70°"]]',
        },
        "recap": [
            ("So, here it is again. Given the apex, take it out of 180 first, then "
             "share what is left equally between the two base angles. Apex out, "
             "then share — never the other way round.",
             '[[triangle v="A,B,C" ticks="BC,CA" angles="70,70,40" caption="(180° − 40°) ÷ 2 = 70°"]]'),
            ("And that is the same triangle, read top to base.",
             '[[step eq="(180° − 40°) ÷ 2 = 70°"]]'),
        ],
        "bank": [
            {"a": 22, "b": 0, "op": "chas"},
            {"a": 28, "b": 0, "op": "chas"},
            {"a": 34, "b": 0, "op": "chas"},
            {"a": 38, "b": 0, "op": "chas"},
            {"a": 46, "b": 0, "op": "chas"},
            {"a": 52, "b": 0, "op": "chas"},
            {"a": 64, "b": 0, "op": "chas"},
            {"a": 70, "b": 0, "op": "chas"},
            {"a": 76, "b": 0, "op": "chas"},
            {"a": 82, "b": 0, "op": "chas"},
        ],
    },
]
LESSONS.extend(_GEOMETRY_U3)


# =============================================================================
# GEOMETRY -- UNIT 4: SIMILARITY & DILATIONS (build le, 2026-08-22)
# =============================================================================
# ONE THREAD, FOUR LESSONS: a scale factor is a TIMES, never an ADD. Apply a
# factor to one side; find the factor from a matching pair; the full
# similar-triangles missing side (where the famous additive error -- "3 grew by
# 3, so 5 becomes 8" -- is the standing distractor); then the closer, the k²
# area surprise. Ties BACK to U3 (congruent = similar with factor 1, said in the
# teach) and FORWARD to U5 (the tangent is this unit's ratio inside a triangle).
_GEOMETRY_U4 = [
    {
        "id": "geo-u4-the-enlarging-copy",
        "course": "geometry", "unit": 4,
        "topic": "Scaling one side",
        "op": "scal", "max_value": 64,
        "levels": ("abstract",),
        "symbols": ("scale factor", "similar"),
        "advance_line": "Three in a row, and you can say why — you've got it! A scale factor is a times, never an add.",
        "why": [
            ("Why one more move? Because this one changes SIZE. An enlargement "
             "copies a shape bigger — same shape, same angles, new size — and one "
             "number runs the whole job: the scale factor. Scale factor 2 means every "
             "length comes out 2 times as long. Shapes related this way are called "
             "similar.",
             '[[goal text="Scaling one side"]]'),
        ],
        "picture": [
            ("Here is a small triangle with sides 3, 5 and 4, and beside it its "
             "enlarged copy by scale factor 2: sides 6, 10 and 8. Each side kept its "
             "place and timesed by the same 2 — that is why the copy keeps its "
             "shape.",
             '[[triangle v="A,B,C" sides="3,5,4" caption="small: 3, 5, 4"]][[triangle v="D,E,F" sides="6,10,8" caption="enlarged × 2: 6, 10, 8"]]'),
        ],
        "teach": [
            ("That is the method. Enlarge the triangle by scale factor 2. The side of "
             "3 becomes 3 times 2 — 6. The side of 5 becomes 10, and the side of 4 "
             "becomes 8. Every side, the same times.",
             '[[triangle v="A,B,C" sides="3,5,4" caption="sides 3, 5, 4"]][[step eq="× 2: 3 → 6 · 5 → 10 · 4 → 8"]]'),
            ("The trap: scale factor 2 does not ADD 2. Adding 2 turns the 3 into a 5 "
             "and the 5 into a 7 — and the copy comes out the WRONG shape, squashed "
             "where the short sides grew too much. Scaling is times.",
             '[[step eq="3 × 2 = 6 ✓"]][[step eq="3 + 2 = 5 ✗ — adding bends the shape"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Scale factor 3, a side of 5: 5 "
                        "times 3 equals 15.",
                        '[[triangle v="A,B,C" sides="5,," caption="small: 5"]][[triangle v="D,E,F" sides="15,," caption="enlarged × 3: 15"]][[step eq="5 × 3 = 15"]]'),
             "ask": {'a': 8, 'b': 2, 'op': 'scal'}},
            {"worked": ("One more together. Scale factor 4, a side of 7: 7 times 4 "
                        "equals 28.",
                        '[[triangle v="A,B,C" sides="7,," caption="small: 7"]][[triangle v="D,E,F" sides="28,," caption="enlarged × 4: 28"]][[step eq="7 × 4 = 28"]]'),
             "ask": {'a': 15, 'b': 3, 'op': 'scal'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A side of 3 "
                       "enlarged by scale factor 2 becomes 6. Tap the reason why."),
            "choices": ("because a scale factor times every side: 3 times 2 | "
                        "because a scale factor adds to every side: 3 plus 2 | "
                        "because the enlarged side is the factor, 2"),
            "answer": "because a scale factor times every side: 3 times 2",
            "board": '[[triangle v="A,B,C" sides="3,5,4" caption="small"]][[triangle v="D,E,F" sides="6,10,8" caption="enlarged × 2"]]',
        },
        "recap": [
            ("So, here it is again. An enlargement keeps the shape and changes the "
             "size, and the scale factor is a times — every side timesed by the same "
             "number. Never an add; adding bends the shape.",
             '[[triangle v="A,B,C" sides="3,5,4" caption="small"]][[triangle v="D,E,F" sides="6,10,8" caption="× 2"]]'),
            ("And that is a similar shape: the same shape in a new size.",
             '[[step eq="3 × 2 = 6"]]'),
        ],
        "bank": [
            {"a": 4, "b": 2, "op": "scal"},
            {"a": 6, "b": 2, "op": "scal"},
            {"a": 6, "b": 3, "op": "scal"},
            {"a": 10, "b": 2, "op": "scal"},
            {"a": 12, "b": 2, "op": "scal"},
            {"a": 9, "b": 3, "op": "scal"},
            {"a": 8, "b": 4, "op": "scal"},
            {"a": 12, "b": 3, "op": "scal"},
            {"a": 12, "b": 4, "op": "scal"},
            {"a": 16, "b": 4, "op": "scal"},
        ],
    },
    {
        "id": "geo-u4-finding-the-factor",
        "course": "geometry", "unit": 4,
        "topic": "The scale factor",
        "op": "sfac", "max_value": 24,
        "levels": ("abstract",),
        "symbols": ("scale factor", "matches"),
        "advance_line": "Three in a row, and you can say why — you've got it! Big side divided by the side it matches.",
        "why": [
            ("Why find the factor? Because two similar shapes stand side by side — "
             "the same shape in two sizes — and somewhere between them hides the "
             "number that turns one into the other: the scale factor. Finding it is "
             "one division: a big side divided by the small side it matches.",
             '[[goal text="The scale factor"]]'),
        ],
        "picture": [
            ("Here are two matching sides as bars: 4 in the small shape, 12 in the "
             "big one. The big bar is three of the small one stacked — 12 is 3 times "
             "4. So the scale factor is 3, and check it backwards: 4 times 3 equals "
             "12.",
             '[[bars data="small:4 | big:12" caption="matching sides 4 and 12 — the big is 3 times the small"]]'),
        ],
        "teach": [
            ("That is the method. A side of 4 in the small shape matches a side of "
             "12 in the big one. The factor is 12 divided by 4 — 3. Check it the "
             "other way: 4 times 3 equals 12. One matching pair of sides is all it "
             "ever takes.",
             '[[bars data="small:4 | big:12" caption="matching sides: 4 and 12"]][[step eq="12 ÷ 4 = 3"]]'),
            ("The trap is the difference. From 4 to 12 is 8 more — but 8 is not the "
             "factor, because the other sides do not each grow by 8; they each grow "
             "by times 3. Similar shapes share a times, never an add.",
             '[[step eq="12 ÷ 4 = 3 ✓"]][[step eq="12 − 4 = 8 ✗ — a difference, not a factor"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. A side of 7 matches a side of "
                        "21. The factor: 21 divided by 7 equals 3.",
                        '[[bars data="small:7 | big:21" caption="matching sides 7 and 21 — factor 3"]][[step eq="21 ÷ 7 = 3"]]'),
             "ask": {'a': 6, 'b': 12, 'op': 'sfac'}},
            {"worked": ("One more together. 9 matches 18: the factor is 18 divided by 9 "
                        "— 2.",
                        '[[bars data="small:9 | big:18" caption="matching sides 9 and 18 — factor 2"]][[step eq="18 ÷ 9 = 2"]]'),
             "ask": {'a': 5, 'b': 15, 'op': 'sfac'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A side of 4 "
                       "matches a side of 12, and the scale factor is 3. Tap the "
                       "reason why."),
            "choices": ("because 12 is 3 times 4 — big side divided by small | "
                        "because 12 take away 4 is 8, so the factor is 8 | because the "
                        "factor is the big side itself, 12"),
            "answer": "because 12 is 3 times 4 — big side divided by small",
            "board": '[[bars data="small:4 | big:12" caption="12 ÷ 4 = 3"]]',
        },
        "recap": [
            ("So, here it is again. The scale factor hides between two matching "
             "sides: divide the big one by the small one. Check by timesing back. "
             "The difference between them is not the factor — similar shapes share "
             "a times.",
             '[[bars data="small:4 | big:12" caption="12 ÷ 4 = 3 · 4 × 3 = 12"]]'),
            ("And that is one division, and the whole enlargement is known.",
             '[[step eq="12 ÷ 4 = 3"]]'),
        ],
        "bank": [
            {"a": 3, "b": 6, "op": "sfac"},
            {"a": 4, "b": 8, "op": "sfac"},
            {"a": 2, "b": 8, "op": "sfac"},
            {"a": 5, "b": 10, "op": "sfac"},
            {"a": 2, "b": 10, "op": "sfac"},
            {"a": 3, "b": 12, "op": "sfac"},
            {"a": 4, "b": 16, "op": "sfac"},
            {"a": 6, "b": 18, "op": "sfac"},
            {"a": 5, "b": 20, "op": "sfac"},
            {"a": 6, "b": 24, "op": "sfac"},
        ],
    },
    {
        "id": "geo-u4-the-matching-side",
        "course": "geometry", "unit": 4,
        "topic": "Missing sides in similar triangles",
        "op": "mside", "max_value": 40,
        "levels": ("abstract",),
        "symbols": ("similar", "matching"),
        "advance_line": "Three in a row, and you can say why — you've got it! Divide to find the factor, times to cross over.",
        "why": [
            ("Why the payoff? Because two similar triangles stand together: the "
             "small one you can measure, and the big one is missing a side. Like "
             "congruent triangles, similar ones come with matching pairs of sides — "
             "but here every pair shares one scale factor instead of being equal. "
             "Find the factor from a complete pair, then times the side you have.",
             '[[goal text="The matching side"]]'),
        ],
        "picture": [
            ("Here is the small triangle with sides 3 and 5, and the big one beside "
             "it. The side of 3 matches a side of 6 — so the factor is 2 — and the "
             "side of 5 crosses over to 5 times 2: 10. Two steps, always the same "
             "two.",
             '[[triangle v="A,B,C" sides="3,5," caption="small: 3 and 5"]][[triangle v="D,E,F" sides="6,10," caption="big × 2: 6 and 10"]]'),
        ],
        "teach": [
            ("That is the method. The side of 3 matches a side of 6. The factor: 6 "
             "divided by 3 equals 2. Another small side is 5 — so its match is 5 "
             "times 2, which equals 10. Divide to find the factor, times to cross "
             "over.",
             '[[triangle v="A,B,C" sides="3,5," caption="small: 3 and 5 — 3 matches 6"]][[step eq="3 → 6: factor 2"]][[step eq="5 × 2 = 10"]]'),
            ("Here is the oldest mistake in similarity. From 3 to 6 is 3 MORE — so 5 "
             "becomes 8? No. The big triangle is not the small one plus a border; "
             "it is the small one times a factor. 8 bends the shape. 10 keeps it.",
             '[[step eq="5 × 2 = 10 ✓"]][[step eq="5 + 3 = 8 ✗ — the same add is the wrong rule"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. A side of 4 matches a side of 8 "
                        "— the factor is 2. Another small side is 7, so its match is 7 "
                        "times 2 — 14.",
                        '[[triangle v="A,B,C" sides="4,7," caption="small: 4 and 7"]][[triangle v="D,E,F" sides="8,14," caption="big × 2: 8 and 14"]][[step eq="4 → 8: factor 2 · 7 × 2 = 14"]]'),
             "ask": {'a': 5, 'b': 4, 'c': 2, 'op': 'mside'}},
            {"worked": ("One more together. 3 matches 12 — the factor is 4. The side of "
                        "6 crosses over to 6 times 4, which equals 24.",
                        '[[triangle v="A,B,C" sides="3,6," caption="small: 3 and 6"]][[triangle v="D,E,F" sides="12,24," caption="big × 4: 12 and 24"]][[step eq="3 → 12: factor 4 · 6 × 4 = 24"]]'),
             "ask": {'a': 7, 'b': 9, 'c': 3, 'op': 'mside'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 3 matches 6, and "
                       "so 5 matches 10. Tap the reason why."),
            "choices": ("because the factor is 2, and 5 times 2 is 10 | because 3 grew "
                        "by 3, so 5 grows by 3 to 8 | because the big side is always "
                        "double, whatever the factor"),
            "answer": "because the factor is 2, and 5 times 2 is 10",
            "board": '[[triangle v="A,B,C" sides="3,5," caption="small"]][[triangle v="D,E,F" sides="6,10," caption="big × 2"]]',
        },
        "recap": [
            ("So, here it is again. Similar triangles share one scale factor across "
             "every matching pair. Divide a complete pair to find the factor, then "
             "times the side you have to cross over. Never add the difference.",
             '[[triangle v="A,B,C" sides="3,5," caption="small"]][[triangle v="D,E,F" sides="6,10," caption="× 2"]]'),
            ("And that is a side you never measured, found.",
             '[[step eq="3 → 6: factor 2 · 5 × 2 = 10"]]'),
        ],
        "bank": [
            {"a": 3, "b": 4, "c": 2, "op": "mside"},
            {"a": 4, "b": 5, "c": 2, "op": "mside"},
            {"a": 3, "b": 4, "c": 3, "op": "mside"},
            {"a": 6, "b": 7, "c": 2, "op": "mside"},
            {"a": 4, "b": 5, "c": 3, "op": "mside"},
            {"a": 5, "b": 6, "c": 3, "op": "mside"},
            {"a": 3, "b": 7, "c": 3, "op": "mside"},
            {"a": 4, "b": 6, "c": 4, "op": "mside"},
            {"a": 5, "b": 7, "c": 4, "op": "mside"},
            {"a": 6, "b": 8, "c": 4, "op": "mside"},
        ],
    },
    {
        "id": "geo-u4-the-area-surprise",
        "course": "geometry", "unit": 4,
        "topic": "Area under scaling",
        "op": "sare", "max_value": 80,
        "levels": ("abstract",),
        "symbols": ("area", "factor"),
        "advance_line": "Three in a row, and you can say why — you've got it! Length pays the factor once — area pays it twice.",
        "why": [
            ("Why a surprise? Because scale a shape by factor 2 and every side "
             "doubles — but the AREA does not. Area lives in two directions at once, "
             "across and up, and the factor strikes BOTH. The area comes out times 2 "
             "times 2 — four times as big.",
             '[[goal text="The area surprise"]]'),
        ],
        "picture": [
            ("Here is what one square becomes under scale factor 2: a 2 by 2 block, "
             "and four little squares fit inside. And under scale factor 3: a 3 by 3 "
             "block, nine squares. The area grows by the factor times itself, every "
             "time.",
             '[[rectangle w="2" h="2" caption="scale factor 2: 2 × 2 = 4 squares"]][[rectangle w="3" h="3" caption="scale factor 3: 3 × 3 = 9 squares"]]'),
        ],
        "teach": [
            ("That is the method. An area of 5 scaled by factor 2 is not 10. Times 2 "
             "handles one direction — the other direction is still waiting. 5 times "
             "2 times 2 equals 20. Length pays the factor once; area pays it twice.",
             '[[rectangle w="2" h="2" caption="every square becomes 4"]][[step eq="5 × 2 × 2 = 20"]]'),
            ("Watch the one-direction trap. 5 times 2 is 10 — that is a length\'s "
             "answer, and area is not a length. The second times is not optional; "
             "the across and the up both grew.",
             '[[step eq="5 × 2 × 2 = 20 ✓"]][[step eq="5 × 2 = 10 ✗ — one direction is still waiting"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Area 7, scale factor 2: 7 times "
                        "2 times 2 equals 28.",
                        '[[rectangle w="2" h="2" caption="every square becomes 4"]][[step eq="7 × 2 × 2 = 28"]]'),
             "ask": {'a': 10, 'b': 2, 'op': 'sare'}},
            {"worked": ("One more together. Area 2, scale factor 3: 2 times 3 times 3 "
                        "equals 18.",
                        '[[rectangle w="3" h="3" caption="every square becomes 9"]][[step eq="2 × 3 × 3 = 18"]]'),
             "ask": {'a': 5, 'b': 4, 'op': 'sare'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. An area of 5 "
                       "scaled by factor 2 becomes 20. Tap the reason why."),
            "choices": ("because the factor strikes both directions: 5 times 2 times 2 | "
                        "because the factor strikes once: 5 times 2 is 10 | because "
                        "the area grows by the factor added twice, 5 plus 4"),
            "answer": "because the factor strikes both directions: 5 times 2 times 2",
            "board": '[[rectangle w="2" h="2" caption="every square becomes 4 — 5 × 2 × 2 = 20"]]',
        },
        "recap": [
            ("So, here it is again. A scale factor times every length once — and "
             "every area twice, because area lives across and up at the same time. "
             "Times by the factor, then times by it again.",
             '[[rectangle w="2" h="2" caption="× 2 → area × 4"]][[rectangle w="3" h="3" caption="× 3 → area × 9"]]'),
            ("And that is the surprise: double the sides, four times the paint.",
             '[[step eq="5 × 2 × 2 = 20"]]'),
        ],
        "bank": [
            {"a": 3, "b": 2, "op": "sare"},
            {"a": 4, "b": 2, "op": "sare"},
                        {"a": 6, "b": 2, "op": "sare"},
            {"a": 3, "b": 3, "op": "sare"},
            {"a": 8, "b": 2, "op": "sare"},
            {"a": 4, "b": 3, "op": "sare"},
            {"a": 5, "b": 3, "op": "sare"},
            {"a": 6, "b": 3, "op": "sare"},
            {"a": 4, "b": 4, "op": "sare"},
        ],
    },
]
LESSONS.extend(_GEOMETRY_U4)


# =============================================================================
# GEOMETRY -- UNIT 5: RIGHT TRIANGLES & TRIGONOMETRY (build le, 2026-08-22)
# =============================================================================
# Pythagoras FORWARD (legs to hypotenuse) then BACKWARDS (the missing leg), both
# on named whole-number triples; then the tangent, met as U4's ratio living
# inside one triangle -- and as alg1-u4's "climb", renamed -- read both
# directions in the isos/chas pair pattern. ⭐ [[righttriangle]] draws its first
# scripted lessons; it always labels the hypotenuse, so it appears on teach and
# tangent boards but never on a Pythagorean ask (see the op comment).
_GEOMETRY_U5 = [
    {
        "id": "geo-u5-the-longest-side",
        "course": "geometry", "unit": 5,
        "topic": "The hypotenuse",
        "op": "pyth", "max_value": 40,
        "levels": ("abstract",),
        "symbols": ("hypotenuse", "legs"),
        "advance_line": "Three in a row, and you can say why — you've got it! Leg squared plus leg squared equals hypotenuse squared.",
        "why": [
            ("Why the longest side? Because every right triangle hides an equation. "
             "The two sides that form the square corner are called the legs, and the "
             "longest side — always across from the right angle — is the hypotenuse. "
             "More than two thousand years ago Pythagoras proved: leg squared plus "
             "leg squared equals hypotenuse squared. Every right triangle, every "
             "time.",
             '[[goal text="The longest side"]]'),
        ],
        "picture": [
            ("Here is a right triangle with legs of 5 and 12, and its hypotenuse "
             "across from the square corner: 13. Square the legs — 25 and 144 — and "
             "put them together: 169. And 13 times 13 is 169. The equation holds, and "
             "the picture shows which side is which.",
             '[[righttriangle adj="12" opp="5" hyp="13" caption="legs 5 and 12, hypotenuse 13 — 25 + 144 = 169 = 13²"]]'),
        ],
        "teach": [
            ("That is the method. Legs of 5 and 12. 5 squared is 25, and 12 squared "
             "is 144. Put together: 169. Now, which number times itself equals 169? "
             "13 — so the hypotenuse is 13.",
             '[[righttriangle adj="12" opp="5" hyp="13" caption="legs 5 and 12, hypotenuse 13"]][[step eq="5² + 12² = 25 + 144 = 169"]][[step eq="13 × 13 = 169"]][[step eq="hyp = 13"]]'),
            ("Two traps. Adding the legs — 5 plus 12 equals 17 — walks AROUND the "
             "corner, and the straight path is always shorter than the walk around: "
             "13, not 17. And 169 is the SQUARE of the answer, not the answer — the "
             "rule speaks in squares, so the last step is always to square back.",
             '[[step eq="5 + 12 = 17 ✗ — the walk around the corner"]][[step eq="169 ✗ — the square, not the side"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Legs of 9 and 12: 81 plus 144 "
                        "equals 225, and 15 times 15 equals 225 — the hypotenuse is 15.",
                        '[[righttriangle adj="12" opp="9" hyp="15" caption="legs 9 and 12, hypotenuse 15"]][[step eq="9² + 12² = 225"]][[step eq="hyp = 15"]]'),
             "ask": {'a': 3, 'b': 4, 'c': 5, 'op': 'pyth'}},
            {"worked": ("One more together. Legs of 12 and 35: 144 plus 1225 equals "
                        "1369 — and 37 times 37 equals 1369, so the hypotenuse is 37.",
                        '[[righttriangle adj="35" opp="12" hyp="37" caption="legs 12 and 35, hypotenuse 37"]][[step eq="12² + 35² = 1369"]][[step eq="hyp = 37"]]'),
             "ask": {'a': 6, 'b': 8, 'c': 10, 'op': 'pyth'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A right triangle "
                       "with legs 5 and 12 has a hypotenuse of 13. Tap the reason "
                       "why."),
            "choices": ("because the squares of the legs add up to 13 squared | because "
                        "the legs add up to 17, near enough to 13 | because the "
                        "hypotenuse is the two legs added, then halved"),
            "answer": "because the squares of the legs add up to 13 squared",
            "board": '[[righttriangle adj="12" opp="5" hyp="13" caption="5² + 12² = 13²"]]',
        },
        "recap": [
            ("So, here it is again. In a right triangle, leg squared plus leg "
             "squared equals hypotenuse squared. Square the legs, add, then find the "
             "number that squares back — the straight path, not the walk around.",
             '[[righttriangle adj="12" opp="5" hyp="13" caption="5² + 12² = 169 = 13²"]]'),
            ("And that is an equation two thousand years old, still true in every "
             "corner.",
             '[[step eq="5² + 12² = 13²"]]'),
        ],
        "bank": [
            {"a": 8, "b": 15, "c": 17, "op": "pyth"},
            {"a": 12, "b": 16, "c": 20, "op": "pyth"},
            {"a": 15, "b": 20, "c": 25, "op": "pyth"},
            {"a": 7, "b": 24, "c": 25, "op": "pyth"},
            {"a": 10, "b": 24, "c": 26, "op": "pyth"},
            {"a": 20, "b": 21, "c": 29, "op": "pyth"},
            {"a": 18, "b": 24, "c": 30, "op": "pyth"},
            {"a": 16, "b": 30, "c": 34, "op": "pyth"},
            {"a": 21, "b": 28, "c": 35, "op": "pyth"},
            {"a": 24, "b": 32, "c": 40, "op": "pyth"},
        ],
    },
    {
        "id": "geo-u5-the-missing-leg",
        "course": "geometry", "unit": 5,
        "topic": "The missing leg",
        "op": "leg", "max_value": 40,
        "levels": ("abstract",),
        "symbols": ("hypotenuse", "leg"),
        "advance_line": "Three in a row, and you can say why — you've got it! Square first, take away, then square back.",
        "why": [
            ("Why backwards? Because the equation runs that way too. Know the "
             "hypotenuse and one leg, and the other leg is waiting inside the same "
             "rule. Leg squared plus leg squared equals hypotenuse squared — so the "
             "missing square is the hypotenuse\'s square take away the known leg\'s "
             "square.",
             '[[goal text="The missing leg"]]'),
        ],
        "picture": [
            ("Here is a right triangle with its hypotenuse, 13, and one leg, 5. The "
             "other leg is 12 — because 13 squared is 169, 5 squared is 25, and 169 "
             "take away 25 is 144, which is 12 times 12. The picture holds all three "
             "sides; the rule found the one that was missing.",
             '[[righttriangle adj="12" opp="5" hyp="13" caption="hypotenuse 13, leg 5 — the other leg is 12: 169 − 25 = 144 = 12²"]]'),
        ],
        "teach": [
            ("That is the method. The hypotenuse is 13 and one leg is 5. 13 squared "
             "is 169; 5 squared is 25. Take away: 144. Which number times itself "
             "equals 144? 12 — the missing leg is 12.",
             '[[righttriangle adj="12" opp="5" hyp="13" caption="legs 5 and 12, hypotenuse 13"]][[step eq="13² − 5² = 169 − 25 = 144"]][[step eq="12 × 12 = 144"]][[step eq="leg = 12"]]'),
            ("The trap is taking away the LENGTHS instead of the squares: 13 take "
             "away 5 equals 8, and 8 is wrong — the rule speaks in squares, never in "
             "plain sides. Square first, then take away, then find the number that "
             "squares back.",
             '[[step eq="13² − 5² → leg = 12 ✓"]][[step eq="13 − 5 = 8 ✗ — the rule speaks in squares"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Hypotenuse 10, leg 8: 100 take "
                        "away 64 is 36, and 6 times 6 equals 36 — the other leg is 6.",
                        '[[righttriangle adj="8" opp="6" hyp="10" caption="legs 6 and 8, hypotenuse 10"]][[step eq="10² − 8² = 36"]][[step eq="leg = 6"]]'),
             "ask": {'a': 4, 'b': 3, 'c': 5, 'op': 'leg'}},
            {"worked": ("One more together. Hypotenuse 15, leg 12: 225 take away 144 is "
                        "81 — and 9 times 9 equals 81, so the leg is 9.",
                        '[[righttriangle adj="12" opp="9" hyp="15" caption="legs 9 and 12, hypotenuse 15"]][[step eq="15² − 12² = 81"]][[step eq="leg = 9"]]'),
             "ask": {'a': 8, 'b': 15, 'c': 17, 'op': 'leg'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A right triangle "
                       "has a hypotenuse of 13 and a leg of 5, so the other leg is 12. "
                       "Tap the reason why."),
            "choices": ("because 169 take away 25 is 144, and 12 squared is 144 | "
                        "because 13 take away 5 is 8, near enough to 12 | because the "
                        "other leg is the hypotenuse take away 1"),
            "answer": "because 169 take away 25 is 144, and 12 squared is 144",
            "board": '[[righttriangle adj="12" opp="5" hyp="13" caption="13² − 5² = 12²"]]',
        },
        "recap": [
            ("So, here it is again. The same rule, run backwards: the missing "
             "leg\'s square is the hypotenuse\'s square take away the known leg\'s "
             "square. Square first, take away, then square back — never take away "
             "the plain lengths.",
             '[[righttriangle adj="12" opp="5" hyp="13" caption="13² − 5² = 144 = 12²"]]'),
            ("And that is one equation, read in either direction.",
             '[[step eq="13² − 5² = 12²"]]'),
        ],
        "bank": [
            {"a": 6, "b": 8, "c": 10, "op": "leg"},
            {"a": 12, "b": 5, "c": 13, "op": "leg"},
            {"a": 9, "b": 12, "c": 15, "op": "leg"},
            {"a": 12, "b": 16, "c": 20, "op": "leg"},
            {"a": 20, "b": 15, "c": 25, "op": "leg"},
            {"a": 24, "b": 7, "c": 25, "op": "leg"},
            {"a": 10, "b": 24, "c": 26, "op": "leg"},
            {"a": 21, "b": 20, "c": 29, "op": "leg"},
            {"a": 24, "b": 18, "c": 30, "op": "leg"},
            {"a": 30, "b": 16, "c": 34, "op": "leg"},
        ],
    },
    {
        "id": "geo-u5-the-climb-ratio",
        "course": "geometry", "unit": 5,
        "topic": "The tangent",
        "op": "tang", "max_value": 24,
        "levels": ("abstract",),
        "symbols": ("tangent", "opposite"),
        "advance_line": "Three in a row, and you can say why — you've got it! Tangent is opposite divided by adjacent.",
        "why": [
            ("Why does the angle start talking? Because stand at an angle in a right "
             "triangle: the leg touching it is the adjacent side, and the leg across "
             "from it is the opposite side. Their ratio — opposite divided by "
             "adjacent — is called the tangent, and it measures how steeply the "
             "angle climbs.",
             '[[goal text="The climb ratio"]]'),
        ],
        "picture": [
            ("Here is a right triangle with the angle marked. The adjacent side is 4 "
             "— along the floor from the angle — and the opposite side is 8, "
             "standing up across from it. The tangent is 8 divided by 4: 2. For "
             "every 1 you walk across, this angle climbs 2.",
             '[[righttriangle adj="4" opp="8" caption="adjacent 4, opposite 8 — tan = 8 ÷ 4 = 2"]]'),
        ],
        "teach": [
            ("That is the method. The adjacent side is 4 and the opposite side is 8. "
             "The tangent is 8 divided by 4 — 2. That number says: for every 1 you "
             "walk across, the angle climbs 2. You met this in Algebra as the climb "
             "of a line; the tangent is that same climb, living inside a triangle.",
             '[[righttriangle adj="4" opp="8" caption="legs 8 and 4"]][[step eq="tan = 8 ÷ 4 = 2"]]'),
            ("Keep the ratio apart from the sides. The tangent is not the opposite "
             "side, and not the difference between the sides — it is opposite "
             "DIVIDED by adjacent, a pure number with no length at all. 8 take away "
             "4 is a length. 8 divided by 4 is a steepness.",
             '[[step eq="8 ÷ 4 = 2 ✓"]][[step eq="8 − 4 = 4 ✗ · 8 ✗ — lengths, not ratios"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Adjacent 2, opposite 10: the "
                        "tangent is 10 divided by 2 — 5.",
                        '[[righttriangle adj="2" opp="10" caption="adjacent 2, opposite 10 — tan 5"]][[step eq="tan = 10 ÷ 2 = 5"]]'),
             "ask": {'a': 2, 'b': 8, 'op': 'tang'}},
            {"worked": ("One more together. Adjacent 10, opposite 20: the tangent is 20 "
                        "divided by 10, which equals 2.",
                        '[[righttriangle adj="10" opp="20" caption="adjacent 10, opposite 20 — tan 2"]][[step eq="tan = 20 ÷ 10 = 2"]]'),
             "ask": {'a': 6, 'b': 12, 'op': 'tang'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. An angle has an "
                       "adjacent side of 4 and an opposite side of 8, and its tangent "
                       "is 2. Tap the reason why."),
            "choices": ("because the tangent is opposite divided by adjacent: 8 over 4 | "
                        "because the tangent is the opposite side take away the adjacent | "
                        "because the tangent is the longer side, 8"),
            "answer": "because the tangent is opposite divided by adjacent: 8 over 4",
            "board": '[[righttriangle adj="4" opp="8" caption="tan = 8 ÷ 4 = 2"]]',
        },
        "recap": [
            ("So, here it is again. Stand at the angle: adjacent touches it, "
             "opposite faces it. The tangent is opposite divided by adjacent — the "
             "climb for every one across, a pure number, never a length.",
             '[[righttriangle adj="4" opp="8" caption="tan = 8 ÷ 4 = 2"]]'),
            ("And that is the climb of a line, found inside a triangle.",
             '[[step eq="tan = 8 ÷ 4 = 2"]]'),
        ],
        "bank": [
            {"a": 3, "b": 6, "op": "tang"},
            {"a": 2, "b": 6, "op": "tang"},
                        {"a": 3, "b": 9, "op": "tang"},
            {"a": 5, "b": 10, "op": "tang"},
            {"a": 4, "b": 12, "op": "tang"},
            {"a": 3, "b": 12, "op": "tang"},
            {"a": 5, "b": 15, "op": "tang"},
            {"a": 4, "b": 16, "op": "tang"},
            {"a": 6, "b": 18, "op": "tang"},
        ],
    },
    {
        "id": "geo-u5-using-the-tangent",
        "course": "geometry", "unit": 5,
        "topic": "Using the tangent",
        "op": "topp", "max_value": 30,
        "levels": ("abstract",),
        "symbols": ("tangent", "adjacent"),
        "advance_line": "Three in a row, and you can say why — you've got it! Adjacent times tangent equals opposite.",
        "why": [
            ("Why is this where it earns its keep? Because the tangent works "
             "backwards too. Know an angle\'s tangent and how far away you stand, "
             "and it hands you a height you could never reach with a ruler. Given "
             "the tangent and the adjacent side, the side opposite the angle is "
             "adjacent times tangent.",
             '[[goal text="Using the tangent"]]'),
        ],
        "picture": [
            ("Here is a right triangle whose angle has a tangent of 4, with an "
             "adjacent side of 5. A tangent of 4 climbs 4 for every 1 across. Walk "
             "5 across and it climbs 4, five times over — the opposite side is 20, "
             "standing up across from the angle.",
             '[[righttriangle adj="5" opp="20" caption="adjacent 5, tangent 4 — opposite 5 × 4 = 20"]]'),
        ],
        "teach": [
            ("That is the method. Say the tangent is 4 and the adjacent side is 5. A "
             "tangent of 4 climbs 4 for every 1 across. Walk 5 across and it climbs "
             "4, five times over: 5 times 4 equals 20. The opposite side is 20.",
             '[[righttriangle adj="5" opp="20" caption="legs 20 and 5"]][[step eq="opposite = 5 × 4 = 20"]]'),
            ("The trap is the same one from the similarity unit: ADDING when the "
             "number is a times. A tangent of 4 does not add 4 to the side — it "
             "times it. And the tangent itself is never the answer: 4 is a "
             "steepness, not a side.",
             '[[step eq="5 × 4 = 20 ✓"]][[step eq="5 + 4 = 9 ✗ · 4 ✗ — a steepness, not a side"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Tangent 2, adjacent 8: the "
                        "opposite side is 8 times 2 — 16.",
                        '[[righttriangle adj="8" opp="16" caption="adjacent 8, tangent 2 — opposite 16"]][[step eq="opposite = 8 × 2 = 16"]]'),
             "ask": {'a': 6, 'b': 2, 'op': 'topp'}},
            {"worked": ("One more together. Tangent 4, adjacent 8: the opposite side is "
                        "8 times 4, which equals 32.",
                        '[[righttriangle adj="8" opp="32" caption="adjacent 8, tangent 4 — opposite 32"]][[step eq="opposite = 8 × 4 = 32"]]'),
             "ask": {'a': 7, 'b': 3, 'op': 'topp'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. An angle has a "
                       "tangent of 4 and an adjacent side of 5, so its opposite side "
                       "is 20. Tap the reason why."),
            "choices": ("because the tangent climbs 4 for every 1 across, five times over | "
                        "because the tangent adds 4 to the side: 5 plus 4 | because "
                        "the opposite side is the tangent itself, 4"),
            "answer": "because the tangent climbs 4 for every 1 across, five times over",
            "board": '[[righttriangle adj="5" opp="20" caption="opposite = 5 × 4 = 20"]]',
        },
        "recap": [
            ("So, here it is again. The tangent is a climb per step, so the "
             "opposite side is the adjacent side times the tangent — a times, never "
             "an add, and never the tangent on its own.",
             '[[righttriangle adj="5" opp="20" caption="opposite = adjacent × tangent"]]'),
            ("And that is a height measured from the ground, with no ladder.",
             '[[step eq="opposite = 5 × 4 = 20"]]'),
        ],
        "bank": [
            {"a": 3, "b": 2, "op": "topp"},
            {"a": 4, "b": 2, "op": "topp"},
            {"a": 5, "b": 2, "op": "topp"},
            {"a": 4, "b": 3, "op": "topp"},
            {"a": 7, "b": 2, "op": "topp"},
            {"a": 5, "b": 3, "op": "topp"},
            {"a": 6, "b": 3, "op": "topp"},
            {"a": 10, "b": 2, "op": "topp"},
            {"a": 8, "b": 3, "op": "topp"},
            {"a": 9, "b": 3, "op": "topp"},
        ],
    },
]
LESSONS.extend(_GEOMETRY_U5)


# =============================================================================
# GEOMETRY -- UNIT 6: CIRCLES (build lf, 2026-08-22)
# =============================================================================
# THE WHOLE IS 360. Lesson 1 plants it against the straight-line habit (180
# leaps to mind after three units of triangles); lessons 2 and 3 are the
# inscribed-angle rule read BOTH directions (the isos/chas pair pattern, again);
# lesson 4 is arc length as one equal part of the distance around, on the
# shaded pie. ⭐ [[circle inscribed=]] draws its first scripted lessons -- on
# the angle-to-arc side only, where its auto-label is the given (see the op
# comments for the rule).
_GEOMETRY_U6 = [
    {
        "id": "geo-u6-the-rest-of-the-circle",
        "course": "geometry", "unit": 6,
        "topic": "Arcs and the whole circle",
        "op": "cent", "max_value": 360,
        "levels": ("abstract",),
        "symbols": ("arc", "degrees"),
        "advance_line": "Three in a row, and you can say why — you've got it! A circle's arcs share 360.",
        "why": [
            ("Why the rest of the circle? Because a circle can be cut. Draw two "
             "radiuses from the middle and the rim splits into two arcs, and every arc "
             "is measured in degrees — by the angle it opens at the middle. All the way "
             "around is one full turn: 360 degrees. The two arcs always share exactly "
             "360.",
             '[[goal text="The rest of the circle"]]'),
        ],
        "picture": [
            ("Here is the circle, cut into its two arcs. The small arc opens at 60 "
             "degrees, and the rest of the circle is the big arc — 300 degrees. Put "
             "them side by side and they fill the whole turn: 60 and 300, and there is "
             "no rim left over.",
             '[[pie data="the small arc 60°:60 | the rest 300°:300" caption="the two arcs of one circle — 60° and 300° fill the whole turn"]]'),
        ],
        "teach": [
            ("That is the method. The small arc opens at 60 degrees. The whole turn is "
             "360, so the rest of the circle is 360 take away 60, which equals 300 "
             "degrees. Check by putting the two arcs back: 60 plus 300 equals 360 — "
             "the whole circle again.",
             '[[circle center="O" caption="the circle — a full turn of 360°"]][[step eq="360° − 60° = 300°"]][[step eq="60° + 300° = 360° ✓"]]'),
            ("The trap comes from an old friend. Angles on a straight line share 180 — "
             "and after three units of triangles, 180 leaps to mind first. But a "
             "circle is not a line: it is a FULL turn, and full turns share 360. Ask "
             "which shape you are inside before you take away.",
             '[[step eq="360 − 60 = 300 ✓"]][[step eq="180 − 60 = 120 ✗ — a line\'s share, not a circle\'s"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. The small arc is 80 degrees, so "
                        "the rest is 360 take away 80 — 280 degrees.",
                        '[[pie data="the arc 80°:80 | the rest 280°:280" caption="80° + 280° = 360°"]][[step eq="360° − 80° = 280°"]]'),
             "ask": {'a': 20, 'b': 0, 'op': 'cent'}},
            {"worked": ("One more together. An arc of 45: the rest of the circle is 360 "
                        "take away 45, which equals 315 degrees.",
                        '[[pie data="the arc 45°:45 | the rest 315°:315" caption="45° + 315° = 360°"]][[step eq="360° − 45° = 315°"]]'),
             "ask": {'a': 150, 'b': 0, 'op': 'cent'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. The small arc opens "
                       "at 60 degrees, so the rest of the circle is 300 degrees. Tap "
                       "the reason why."),
            "choices": ("because a circle is a full turn of 360, not 180 | because a "
                        "circle is a straight line of 180 | because the rest is always "
                        "twice the small arc"),
            "answer": "because a circle is a full turn of 360, not 180",
            "board": '[[pie data="the small arc 60°:60 | the rest 300°:300" caption="60° + 300° = 360°"]]',
        },
        "recap": [
            ("So, here it is again. A circle is a full turn of 360 degrees, and its "
             "two arcs share it. Know one arc, take it away from 360, and the rest of "
             "the circle is what is left — never from 180, which is a line\'s share.",
             '[[pie data="the small arc 60°:60 | the rest 300°:300" caption="360° − 60° = 300°"]]'),
            ("And that is the first rule of circles: the arcs share 360.",
             '[[step eq="360° − 60° = 300°"]]'),
        ],
        "bank": [
            {"a": 25, "b": 0, "op": "cent"},
            {"a": 30, "b": 0, "op": "cent"},
            {"a": 40, "b": 0, "op": "cent"},
            {"a": 50, "b": 0, "op": "cent"},
            {"a": 59, "b": 0, "op": "cent"},
            {"a": 70, "b": 0, "op": "cent"},
            {"a": 110, "b": 0, "op": "cent"},
            {"a": 120, "b": 0, "op": "cent"},
            {"a": 130, "b": 0, "op": "cent"},
            {"a": 140, "b": 0, "op": "cent"},
        ],
    },
    {
        "id": "geo-u6-half-the-arc",
        "course": "geometry", "unit": 6,
        "topic": "The inscribed angle",
        "op": "insc", "max_value": 180,
        "levels": ("abstract",),
        "symbols": ("inscribed", "arc"),
        "advance_line": "Three in a row, and you can say why — you've got it! From the rim, the arc looks half.",
        "why": [
            ("Why half? Because an angle can stand at the middle of a circle — or on "
             "the rim itself. An angle whose corner sits ON the circle is called an "
             "inscribed angle, and it opens onto an arc across from it. Here is the "
             "circle\'s most famous rule: an inscribed angle is HALF its arc.",
             '[[goal text="Half the arc"]]'),
        ],
        "picture": [
            ("Here is an angle standing on the rim, opening onto the arc across from "
             "it. The arc measures 80 degrees, and the angle on the rim measures 40 — "
             "half. Slide the corner anywhere along the rim and the angle stays 40: "
             "the arc rules the angle from anywhere on the circle.",
             '[[circle center="O" inscribed="80" caption="an inscribed angle on the rim — the arc across is 80°, the angle is 40°"]]'),
        ],
        "teach": [
            ("That is the method. The arc across measures 80 degrees, so the inscribed "
             "angle is half of that: 80 divided by 2, which equals 40 degrees. From "
             "the rim, an arc of 80 looks like 40.",
             '[[circle center="O" inscribed="80" caption="arc 80°, inscribed angle 40°"]][[step eq="80° ÷ 2 = 40°"]]'),
            ("The trap is treating them as twins. The angle at the MIDDLE equals its "
             "arc — but the rim is farther away, and from farther away things look "
             "smaller: exactly half. Same arc, two views: from the middle, 80; from "
             "the rim, 40.",
             '[[step eq="from the middle: 80°"]][[step eq="from the rim: 80° ÷ 2 = 40°"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. The arc measures 56 degrees, so "
                        "the inscribed angle is 56 divided by 2 — 28 degrees.",
                        '[[circle center="O" inscribed="56" caption="arc 56°, inscribed angle 28°"]][[step eq="56° ÷ 2 = 28°"]]'),
             "ask": {'a': 36, 'b': 0, 'op': 'insc'}},
            {"worked": ("One more together. An arc of 110: the inscribed angle is 110 "
                        "divided by 2, which equals 55 degrees.",
                        '[[circle center="O" inscribed="110" caption="arc 110°, inscribed angle 55°"]][[step eq="110° ÷ 2 = 55°"]]'),
             "ask": {'a': 150, 'b': 0, 'op': 'insc'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. An arc measures 80 "
                       "degrees, so the inscribed angle on the rim is 40 degrees. Tap "
                       "the reason why."),
            "choices": ("because an inscribed angle is half its arc | because an "
                        "inscribed angle equals its arc, like the middle | because the "
                        "rim always takes away 40"),
            "answer": "because an inscribed angle is half its arc",
            "board": '[[circle center="O" inscribed="80" caption="arc 80° — from the rim, 40°"]]',
        },
        "recap": [
            ("So, here it is again. An angle with its corner on the rim is an "
             "inscribed angle, and it measures half the arc across from it. From the "
             "middle an arc looks its full size; from the rim, exactly half.",
             '[[circle center="O" inscribed="80" caption="arc 80°, inscribed angle 40°"]]'),
            ("And that is the circle\'s most famous rule: half the arc.",
             '[[step eq="80° ÷ 2 = 40°"]]'),
        ],
        "bank": [
            {"a": 30, "b": 0, "op": "insc"},
            {"a": 40, "b": 0, "op": "insc"},
            {"a": 50, "b": 0, "op": "insc"},
            {"a": 60, "b": 0, "op": "insc"},
            {"a": 70, "b": 0, "op": "insc"},
            {"a": 78, "b": 0, "op": "insc"},
            {"a": 100, "b": 0, "op": "insc"},
            {"a": 120, "b": 0, "op": "insc"},
            {"a": 140, "b": 0, "op": "insc"},
            {"a": 160, "b": 0, "op": "insc"},
        ],
    },
    {
        "id": "geo-u6-double-it-back",
        "course": "geometry", "unit": 6,
        "topic": "From angle to arc",
        "op": "iarc", "max_value": 160,
        "levels": ("abstract",),
        "symbols": ("inscribed", "arc"),
        "advance_line": "Three in a row, and you can say why — you've got it! From angle to arc, you double.",
        "why": [
            ("Why double? Because a rule read forwards can be read back. You stand on "
             "the rim, you measure the inscribed angle — and the arc across from you "
             "is waiting to be found. If the angle is half the arc, then the arc is "
             "DOUBLE the angle. One rule, two directions, like every good rule in "
             "this course.",
             '[[goal text="Double it back"]]'),
        ],
        "picture": [
            ("Here is the angle on the rim, and it measures 40 degrees. The arc across "
             "from it is the bigger one: 80 degrees, double the angle. Read the same "
             "picture forwards and it still agrees — half of 80 is 40.",
             '[[circle center="O" inscribed="80" caption="inscribed angle 40° — the arc across is double: 80°"]]'),
        ],
        "teach": [
            ("That is the method. The inscribed angle measures 40 degrees. The arc "
             "across from it is double that: 2 times 40 equals 80 degrees. And check "
             "it forwards: half of 80 is 40 — the same picture, read both ways.",
             '[[circle center="O" inscribed="80" caption="inscribed angle 40°, arc 80°"]][[step eq="arc = 2 × 40° = 80°"]][[step eq="80° ÷ 2 = 40° ✓"]]'),
            ("The danger is halving out of habit. In the last lesson every answer came "
             "from dividing by 2 — but that was arc to angle. This lesson runs angle "
             "to arc, and the arc is the BIGGER one: from the rim out to the arc, you "
             "double. Ask which one you are holding before you move.",
             '[[step eq="angle 40° → arc 80° ✓"]][[step eq="40° ÷ 2 = 20° ✗ — that halves the wrong direction"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. The inscribed angle is 26 "
                        "degrees, so its arc is 2 times 26 — 52 degrees.",
                        '[[circle center="O" inscribed="52" caption="inscribed angle 26°, arc 52°"]][[step eq="arc = 2 × 26° = 52°"]]'),
             "ask": {'a': 16, 'b': 0, 'op': 'iarc'}},
            {"worked": ("One more together. An inscribed angle of 75: the arc is 2 times "
                        "75, which equals 150 degrees.",
                        '[[circle center="O" inscribed="150" caption="inscribed angle 75°, arc 150°"]][[step eq="arc = 2 × 75° = 150°"]]'),
             "ask": {'a': 44, 'b': 0, 'op': 'iarc'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. An inscribed angle "
                       "measures 40 degrees, so the arc it opens onto is 80 degrees. "
                       "Tap the reason why."),
            "choices": ("because the arc is double the inscribed angle | because the arc "
                        "is half the inscribed angle | because every arc on a circle "
                        "is 80"),
            "answer": "because the arc is double the inscribed angle",
            "board": '[[circle center="O" inscribed="80" caption="angle 40° on the rim — arc 80°"]]',
        },
        "recap": [
            ("So, here it is again. The inscribed angle is half its arc, so the arc "
             "is double the angle. From arc to angle you halve; from angle to arc you "
             "double — one rule, read in either direction.",
             '[[circle center="O" inscribed="80" caption="angle 40°, arc 2 × 40° = 80°"]]'),
            ("And that is the same picture, read both ways.",
             '[[step eq="arc = 2 × 40° = 80°"]]'),
        ],
        "bank": [
            {"a": 20, "b": 0, "op": "iarc"},
            {"a": 24, "b": 0, "op": "iarc"},
            {"a": 30, "b": 0, "op": "iarc"},
            {"a": 36, "b": 0, "op": "iarc"},
            {"a": 38, "b": 0, "op": "iarc"},
            {"a": 50, "b": 0, "op": "iarc"},
            {"a": 60, "b": 0, "op": "iarc"},
            {"a": 64, "b": 0, "op": "iarc"},
            {"a": 70, "b": 0, "op": "iarc"},
            {"a": 80, "b": 0, "op": "iarc"},
        ],
    },
    {
        "id": "geo-u6-a-piece-of-the-rim",
        "course": "geometry", "unit": 6,
        "topic": "Arc length",
        "op": "alen", "max_value": 120,
        "levels": ("abstract",),
        "symbols": ("arc", "equal parts"),
        "advance_line": "Three in a row, and you can say why — you've got it! One equal part of the distance around.",
        "why": [
            ("Why length? Because so far every arc was measured in degrees — how far "
             "it turns. One last measure: how far you would WALK along the rim. When "
             "the central angle divides 360 evenly, the circle cuts into equal parts, "
             "and the arc is simply one part of the whole distance around.",
             '[[goal text="A piece of the rim"]]'),
        ],
        "picture": [
            ("Here is a circle cut into 4 equal parts, with one part shaded. A central "
             "angle of 90 degrees cuts it that way, because 90 goes into 360 four times. "
             "If the whole distance around is 12, the shaded arc is one of four equal "
             "parts of 12 — it is 3 long.",
             '[[pie parts="4" shaded="1" caption="4 equal parts, 1 shaded — one quarter of the distance around"]]'),
        ],
        "teach": [
            ("That is the method. The distance around the circle is 12, and the arc "
             "sits under a central angle of 90 degrees. 90 goes into 360 four times, "
             "so the circle is 4 equal parts and the arc is one of them: 12 divided by "
             "4, which equals 3.",
             '[[pie parts="4" shaded="1" caption="4 equal parts of 12 — the arc is 3"]][[step eq="360° ÷ 90° = 4 parts"]][[step eq="12 ÷ 4 = 3"]]'),
            ("Keep degrees and length apart — they measure different things. An arc "
             "under 90 degrees is not 90 steps long: 90 says how far it TURNS, not "
             "how far it runs. And not every arc is half the circle; half only happens "
             "under a straight 180.",
             '[[step eq="12 ÷ 4 = 3 ✓"]][[step eq="90 ✗ degrees are not steps · 6 ✗ that is half the circle"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Distance around: 18. Central "
                        "angle: 60 degrees — that is 6 equal parts, so the arc is 18 "
                        "divided by 6, which equals 3.",
                        '[[pie parts="6" shaded="1" caption="6 equal parts of 18 — the arc is 3"]][[step eq="360° ÷ 60° = 6 parts"]][[step eq="18 ÷ 6 = 3"]]'),
             "ask": {'a': 90, 'b': 20, 'op': 'alen'}},
            {"worked": ("One more together. Distance around 32, central angle 45 — that "
                        "is eight equal parts, so the arc is 32 divided by 8, which "
                        "equals 4.",
                        '[[pie parts="8" shaded="1" caption="8 equal parts of 32 — the arc is 4"]][[step eq="360° ÷ 45° = 8 parts"]][[step eq="32 ÷ 8 = 4"]]'),
             "ask": {'a': 120, 'b': 24, 'op': 'alen'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. The distance around "
                       "a circle is 12, and an arc sits under a central angle of 90 "
                       "degrees, so the arc is 3 long. Tap the reason why."),
            "choices": ("because 90 degrees is one of 4 equal parts of the turn | "
                        "because an arc of 90 degrees is 90 steps long | because every "
                        "arc is half the distance around"),
            "answer": "because 90 degrees is one of 4 equal parts of the turn",
            "board": '[[pie parts="4" shaded="1" caption="4 equal parts of 12 — the arc is 3"]]',
        },
        "recap": [
            ("So, here it is again. The central angle says how many equal parts the "
             "circle is cut into — 360 divided by the angle. The arc is one of those "
             "parts of the distance around. Degrees say how far it turns; length says "
             "how far it runs.",
             '[[pie parts="4" shaded="1" caption="4 equal parts of 12 — the arc is 3"]]'),
            ("And that is an arc measured two ways: by its turn, and by its length.",
             '[[step eq="12 ÷ 4 = 3"]]'),
        ],
        "bank": [
            {"a": 90, "b": 8, "op": "alen"},
            {"a": 120, "b": 12, "op": "alen"},
            {"a": 90, "b": 16, "op": "alen"},
            {"a": 60, "b": 30, "op": "alen"},
            {"a": 90, "b": 24, "op": "alen"},
            {"a": 120, "b": 18, "op": "alen"},
            {"a": 45, "b": 64, "op": "alen"},
            {"a": 60, "b": 48, "op": "alen"},
            {"a": 40, "b": 90, "op": "alen"},
            {"a": 72, "b": 60, "op": "alen"},
        ],
    },
]
LESSONS.extend(_GEOMETRY_U6)


# =============================================================================
# GEOMETRY -- UNIT 7: COORDINATE GEOMETRY (build lf, 2026-08-22)
# =============================================================================
# GEOMETRY MOVES ONTO THE GRID FOR GOOD. Lengths along a grid line (the
# fencepost trap: steps, never dots), the straight distance as U5's Pythagoras
# under a slant (the taxicab walk is the standing wrong tap), U1's midpoint
# grown into two dimensions, and the rectangle's fourth corner as the closer.
# The wrong-coordinate error -- a y handed back for an x -- runs through the
# whole unit, exactly as it ran through U2's moves.
_GEOMETRY_U7 = [
    {
        "id": "geo-u7-straight-up",
        "course": "geometry", "unit": 7,
        "topic": "Lengths on the grid",
        "op": "vseg", "max_value": 9,
        "levels": ("abstract",),
        "symbols": ("segment", "grid"),
        "advance_line": "Three in a row, and you can say why — you've got it! Count the steps, never the dots.",
        "why": [
            ("Why the grid? Because on a grid every point has an address, and every "
             "shape can be measured straight from its coordinates. Start with the "
             "simplest measure — an up-and-down segment. How long is it? Count the "
             "STEPS between the ends, never the dots.",
             '[[goal text="Straight up"]]'),
        ],
        "picture": [
            ("Here is a segment standing straight up on the grid, from (1, 3) to (1, "
             "8). Both ends share the same x, so only the heights differ — and the gap "
             "between the heights is its length. Walk up from 3 to 8 and you take five "
             "steps.",
             '[[graph points="(1,3),(1,8)" range="0..10" yrange="0..10" caption="from (1, 3) straight up to (1, 8) — five steps"]]'),
        ],
        "teach": [
            ("That is the method. The segment runs from (1, 3) up to (1, 8). Its "
             "length is the gap between the heights: 8 take away 3, which equals 5. "
             "Count the steps to check: 3 to 4, to 5, to 6, to 7, to 8 — five steps.",
             '[[graph points="(1,3),(1,8)" range="0..10" yrange="0..10" caption="8 − 3 = 5 steps"]][[step eq="8 − 3 = 5"]]'),
            ("The trap is counting DOTS instead of steps. From 3 to 8 there are six "
             "dots but only five steps — a fence with six posts has five rails. Length "
             "is the steps. Do the take away, and trust it over your counting finger.",
             '[[step eq="8 − 3 = 5 ✓ steps"]][[step eq="6 ✗ — that counts the dots, posts instead of rails"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. From (2, 3) to (2, 9): the "
                        "length is 9 take away 3 — 6.",
                        '[[graph points="(2,3),(2,9)" range="0..10" yrange="0..10" caption="from (2, 3) to (2, 9) — 9 − 3 = 6"]][[step eq="9 − 3 = 6"]]'),
             "ask": {'a': 4, 'b': 3, 'c': 7, 'op': 'vseg'}},
            {"worked": ("One more together. From (6, 1) to (6, 5): 5 take away 1 equals "
                        "4.",
                        '[[graph points="(6,1),(6,5)" range="0..10" yrange="0..10" caption="from (6, 1) to (6, 5) — 5 − 1 = 4"]][[step eq="5 − 1 = 4"]]'),
             "ask": {'a': 6, 'b': 2, 'c': 8, 'op': 'vseg'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A segment runs "
                       "from (1, 3) up to (1, 8), and its length is 5. Tap the reason "
                       "why."),
            "choices": ("because the length is the gap between the heights | because "
                        "the length is the number of dots, six | because the length is "
                        "the top height, 8"),
            "answer": "because the length is the gap between the heights",
            "board": '[[graph points="(1,3),(1,8)" range="0..10" yrange="0..10" caption="8 − 3 = 5"]]',
        },
        "recap": [
            ("So, here it is again. An up-and-down segment on the grid has one length: "
             "the gap between its two heights, the top take away the bottom. That "
             "counts the steps — never the dots, which are always one too many.",
             '[[graph points="(1,3),(1,8)" range="0..10" yrange="0..10" caption="8 − 3 = 5 steps"]]'),
            ("And that is a segment measured straight from its coordinates.",
             '[[step eq="8 − 3 = 5"]]'),
        ],
        "bank": [
            {"a": 3, "b": 4, "c": 6, "op": "vseg"},
            {"a": 7, "b": 2, "c": 4, "op": "vseg"},
            {"a": 5, "b": 3, "c": 6, "op": "vseg"},
            {"a": 2, "b": 5, "c": 8, "op": "vseg"},
            {"a": 8, "b": 4, "c": 8, "op": "vseg"},
            {"a": 4, "b": 2, "c": 7, "op": "vseg"},
            {"a": 6, "b": 3, "c": 8, "op": "vseg"},
            {"a": 3, "b": 2, "c": 8, "op": "vseg"},
            {"a": 7, "b": 2, "c": 9, "op": "vseg"},
            {"a": 5, "b": 2, "c": 9, "op": "vseg"},
        ],
    },
    {
        "id": "geo-u7-the-straight-path",
        "course": "geometry", "unit": 7,
        "topic": "Distance between points",
        "op": "dist", "max_value": 13,
        "levels": ("abstract",),
        "symbols": ("distance", "across"),
        "advance_line": "Three in a row, and you can say why — you've got it! Across squared plus up squared, then square back.",
        "why": [
            ("Why the straight path? Because a grid holds two distances. You can walk "
             "the grid lines — across, then up — or you can cut straight from one "
             "point to the other. The straight distance is the shorter one, and "
             "Pythagoras finds it: drop a right triangle under the slant, and the "
             "straight path is its hypotenuse.",
             '[[goal text="The straight path"]]'),
        ],
        "picture": [
            ("Here is a slant from (2, 1) to (5, 5), with the right triangle drawn "
             "underneath it: across 3 along the floor, up 4 at the wall. The slant is "
             "the hypotenuse, and it comes out at 5 — shorter than the 7 you would pay "
             "walking the lines.",
             '[[graph points="(2,1),(5,1),(5,5)" range="0..10" yrange="0..10" caption="the right triangle under the slant — across 3, up 4, straight 5"]]'),
        ],
        "teach": [
            ("That is the method. From (2, 1) to (5, 5): across is 3, up is 4. 3 "
             "squared plus 4 squared is 9 plus 16 — 25. Which number times itself "
             "equals 25? 5. The straight distance is 5.",
             '[[righttriangle adj="3" opp="4" hyp="5" caption="across 3, up 4 — straight 5"]][[step eq="across 3 · up 4"]][[step eq="3² + 4² = 25 = 5²"]]'),
            ("So a grid holds two distances, and the trap is mixing them. Walking the "
             "lines — across, then up — costs 7 here. Cutting straight costs 5. The "
             "straight path is ALWAYS shorter than the walk around; if your answer is "
             "the two counts put together, you walked.",
             '[[step eq="straight: 5 ✓"]][[step eq="3 + 4 = 7 ✗ — that walks the grid"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. From (1, 2) to (7, 10): across "
                        "6, up 8. 36 plus 64 is 100, and 10 times 10 equals 100 — the "
                        "distance is 10.",
                        '[[graph points="(1,2),(7,2),(7,10)" range="0..14" yrange="0..14" caption="across 6, up 8 — straight 10"]][[step eq="6² + 8² = 100 = 10²"]]'),
             "ask": {'a': 3, 'b': 4, 'c': 1, 'op': 'dist'}},
            {"worked": ("One more together. From (4, 1) to (7, 5): across 3, up 4. 9 "
                        "plus 16 is 25, and 5 times 5 equals 25 — the straight distance "
                        "is 5.",
                        '[[graph points="(4,1),(7,1),(7,5)" range="0..14" yrange="0..14" caption="across 3, up 4 — straight 5"]][[step eq="3² + 4² = 25 = 5²"]]'),
             "ask": {'a': 2, 'b': 2, 'c': 2, 'op': 'dist'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. From (2, 1) to (5, "
                       "5) the straight distance is 5, not 7. Tap the reason why."),
            "choices": ("because the slant is the hypotenuse of a 3-4-5 triangle | "
                        "because across plus up is the straight distance | because "
                        "the straight path is always the up count"),
            "answer": "because the slant is the hypotenuse of a 3-4-5 triangle",
            "board": '[[righttriangle adj="3" opp="4" hyp="5" caption="3² + 4² = 5²"]]',
        },
        "recap": [
            ("So, here it is again. To find the straight distance between two points, "
             "drop a right triangle under the slant: count the across, count the up, "
             "square both, add, and square back. The straight path is the hypotenuse — "
             "always shorter than walking the grid.",
             '[[righttriangle adj="3" opp="4" hyp="5" caption="across 3, up 4 — straight 5"]]'),
            ("And that is Pythagoras, come to the grid.",
             '[[step eq="3² + 4² = 5²"]]'),
        ],
        "bank": [
            {"a": 1, "b": 2, "c": 1, "op": "dist"},
            {"a": 2, "b": 5, "c": 1, "op": "dist"},
            {"a": 4, "b": 3, "c": 1, "op": "dist"},
            {"a": 6, "b": 2, "c": 1, "op": "dist"},
            {"a": 5, "b": 6, "c": 1, "op": "dist"},
            {"a": 8, "b": 4, "c": 1, "op": "dist"},
            {"a": 1, "b": 3, "c": 2, "op": "dist"},
            {"a": 3, "b": 2, "c": 2, "op": "dist"},
            {"a": 5, "b": 4, "c": 2, "op": "dist"},
            {"a": 7, "b": 1, "c": 2, "op": "dist"},
        ],
    },
    {
        "id": "geo-u7-the-middle-of-a-line",
        "course": "geometry", "unit": 7,
        "topic": "The midpoint on the grid",
        "op": "mid2", "max_value": 13,
        "levels": ("abstract",),
        "symbols": ("midpoint", "halfway"),
        "advance_line": "Three in a row, and you can say why — you've got it! Add the two x's and share by two.",
        "why": [
            ("Why the middle? Because Unit 1 found the midpoint of a number line — add "
             "the ends, share by two — and the grid version is the same idea twice. "
             "The middle of a slanted segment sits halfway across AND halfway up. Each "
             "coordinate gets its own little average, and today we chase the x.",
             '[[goal text="The middle of a line"]]'),
        ],
        "picture": [
            ("Here is a segment from (2, 3) to (8, 7), with its midpoint marked at (5, "
             "5). Look at the x\'s: 2 on the left end, 8 on the right, and 5 in the "
             "middle — the same distance from each. The y\'s do the same: 3 and 7, "
             "with 5 between them.",
             '[[graph points="(2,3),(5,5),(8,7)" range="0..12" yrange="0..12" caption="from (2, 3) to (8, 7) — the midpoint is (5, 5)"]]'),
        ],
        "teach": [
            ("That is the method. From (2, 3) to (8, 7). The x coordinates are 2 and 8: "
             "add them, 10, and share by two — the midpoint\'s x is 5. The y works the "
             "same way: 3 and 7 land on 5. The middle sits at (5, 5), balanced both "
             "ways.",
             '[[graph points="(2,3),(5,5),(8,7)" range="0..12" yrange="0..12" caption="x: (2 + 8) ÷ 2 = 5 · y: (3 + 7) ÷ 2 = 5"]][[step eq="x: (2 + 8) ÷ 2 = 5"]]'),
            ("Two traps. Answer the coordinate you were ASKED for — the x and the y "
             "each have their own middle, and handing back the y is the grid\'s "
             "oldest mix-up. And the RUN — 8 take away 2, six — is how far the segment "
             "reaches, not where its middle sits.",
             '[[step eq="x of the midpoint: 5 ✓"]][[step eq="the y instead ✗ · the run 6 ✗ — a length, not a place"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. From (3, 2) to (7, 6): the "
                        "x\'s are 3 and 7 — put together 10, shared by two is 5.",
                        '[[graph points="(3,2),(5,4),(7,6)" range="0..12" yrange="0..12" caption="the midpoint (5, 4) — x: (3 + 7) ÷ 2 = 5"]][[step eq="x: (3 + 7) ÷ 2 = 5"]]'),
             "ask": {'a': 3, 'b': 5, 'c': 5, 'op': 'mid2'}},
            {"worked": ("One more together. From (2, 4) to (10, 8): 2 plus 10 is 12, "
                        "shared by two — the midpoint\'s x is 6.",
                        '[[graph points="(2,4),(6,6),(10,8)" range="0..12" yrange="0..12" caption="the midpoint (6, 6) — x: (2 + 10) ÷ 2 = 6"]][[step eq="x: (2 + 10) ÷ 2 = 6"]]'),
             "ask": {'a': 6, 'b': 4, 'c': 8, 'op': 'mid2'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A segment runs "
                       "from (2, 3) to (8, 7), and its midpoint\'s x is 5. Tap the "
                       "reason why."),
            "choices": ("because the midpoint\'s x is the two x\'s averaged | because "
                        "the midpoint\'s x is the run, 8 take away 2 | because the "
                        "midpoint\'s x is the same as its y, always"),
            "answer": "because the midpoint\'s x is the two x\'s averaged",
            "board": '[[graph points="(2,3),(5,5),(8,7)" range="0..12" yrange="0..12" caption="x: (2 + 8) ÷ 2 = 5"]]',
        },
        "recap": [
            ("So, here it is again. The midpoint of a segment sits halfway across and "
             "halfway up. For its x, add the two x\'s and share by two; the y gets "
             "its own average. Answer the coordinate you were asked for — and never "
             "the run, which is a length, not a place.",
             '[[graph points="(2,3),(5,5),(8,7)" range="0..12" yrange="0..12" caption="the midpoint (5, 5)"]]'),
            ("And that is the number line\'s midpoint, done twice.",
             '[[step eq="x: (2 + 8) ÷ 2 = 5"]]'),
        ],
        "bank": [
            {"a": 2, "b": 3, "c": 4, "op": "mid2"},
            {"a": 1, "b": 5, "c": 7, "op": "mid2"},
            {"a": 3, "b": 6, "c": 7, "op": "mid2"},
            {"a": 2, "b": 7, "c": 8, "op": "mid2"},
            {"a": 4, "b": 7, "c": 8, "op": "mid2"},
            {"a": 5, "b": 8, "c": 9, "op": "mid2"},
            {"a": 4, "b": 3, "c": 10, "op": "mid2"},
            {"a": 5, "b": 3, "c": 11, "op": "mid2"},
            {"a": 6, "b": 9, "c": 10, "op": "mid2"},
            {"a": 7, "b": 6, "c": 11, "op": "mid2"},
        ],
    },
    {
        "id": "geo-u7-the-fourth-corner",
        "course": "geometry", "unit": 7,
        "topic": "The fourth corner",
        "op": "corn", "max_value": 12,
        "levels": ("abstract",),
        "symbols": ("rectangle", "corner"),
        "advance_line": "Three in a row, and you can say why — you've got it! Straight above one corner, level with another.",
        "why": [
            ("Why the fourth corner? Because it is a puzzle the grid can solve. A "
             "rectangle has four corners — but you are given only three. The grid "
             "holds the missing one, because a rectangle\'s sides run straight along "
             "the grid: every corner shares its x with one neighbour and its y with "
             "the other.",
             '[[goal text="The fourth corner"]]'),
        ],
        "picture": [
            ("Here are three corners of a rectangle: (2, 2), (7, 2), and (2, 6). Look "
             "at the empty spot where the box should close — straight above (7, 2) and "
             "level with (2, 6). The fourth corner sits there, at (7, 6).",
             '[[graph points="(2,2),(7,2),(2,6),(7,6)" range="0..12" yrange="0..12" caption="the four corners — the fourth, (7, 6), closes the box"]]'),
        ],
        "teach": [
            ("That is the method. Corners at (2, 2), (7, 2), and (2, 6). The fourth "
             "must close the box: it sits straight above (7, 2), so it shares that 7 — "
             "and it sits level with (2, 6), so it shares that 6. The fourth corner is "
             "(7, 6).",
             '[[graph points="(2,2),(7,2),(2,6),(7,6)" range="0..12" yrange="0..12" caption="the four corners"]][[step eq="x from (7, 2) · y from (2, 6) → (7, 6)"]]'),
            ("The trap is grabbing a number from the wrong corner — or the wrong "
             "coordinate. The new corner never gets its x from the corner diagonal to "
             "it, and an x question is never answered with a y. Say it in words first: "
             "straight above which corner? Level with which?",
             '[[step eq="above (7, 2) → x = 7 ✓"]][[step eq="x = 2 ✗ wrong corner · a y for an x ✗"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Corners at (1, 3), (6, 3), and "
                        "(1, 6). The fourth sits straight above (6, 3): its x is 6, and "
                        "the corner is (6, 6).",
                        '[[graph points="(1,3),(6,3),(1,6),(6,6)" range="0..12" yrange="0..12" caption="the fourth corner is (6, 6)"]][[step eq="above (6, 3) → x = 6"]]'),
             "ask": {'a': 3, 'b': 4, 'c': 6, 'op': 'corn'}},
            {"worked": ("One more together. Corners at (4, 2), (9, 2), and (4, 5): the "
                        "fourth corner sits above (9, 2), so its x is 9.",
                        '[[graph points="(4,2),(9,2),(4,5),(9,5)" range="0..12" yrange="0..12" caption="the fourth corner is (9, 5)"]][[step eq="above (9, 2) → x = 9"]]'),
             "ask": {'a': 5, 'b': 6, 'c': 10, 'op': 'corn'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Three corners of a "
                       "rectangle sit at (2, 2), (7, 2) and (2, 6), so the fourth "
                       "corner\'s x is 7. Tap the reason why."),
            "choices": ("because the fourth corner sits straight above (7, 2) | because "
                        "the fourth corner takes its x from (2, 6) | because the fourth "
                        "corner\'s x is always its y"),
            "answer": "because the fourth corner sits straight above (7, 2)",
            "board": '[[graph points="(2,2),(7,2),(2,6),(7,6)" range="0..12" yrange="0..12" caption="above (7, 2) → x = 7"]]',
        },
        "recap": [
            ("So, here it is again. A rectangle\'s sides run along the grid, so its "
             "fourth corner sits straight above one given corner and level with "
             "another. It takes its x from the corner below it and its y from the "
             "corner beside it — never from the corner diagonal to it.",
             '[[graph points="(2,2),(7,2),(2,6),(7,6)" range="0..12" yrange="0..12" caption="the fourth corner is (7, 6)"]]'),
            ("And that is a box closed by its coordinates.",
             '[[step eq="above (7, 2) → x = 7"]]'),
        ],
        "bank": [
            {"a": 2, "b": 2, "c": 4, "op": "corn"},
            {"a": 1, "b": 4, "c": 5, "op": "corn"},
            {"a": 3, "b": 2, "c": 6, "op": "corn"},
            {"a": 2, "b": 6, "c": 7, "op": "corn"},
            {"a": 4, "b": 5, "c": 7, "op": "corn"},
            {"a": 3, "b": 6, "c": 8, "op": "corn"},
            {"a": 5, "b": 3, "c": 9, "op": "corn"},
            {"a": 2, "b": 4, "c": 10, "op": "corn"},
            {"a": 6, "b": 7, "c": 11, "op": "corn"},
            {"a": 4, "b": 6, "c": 12, "op": "corn"},
        ],
    },
]
LESSONS.extend(_GEOMETRY_U7)


# =============================================================================
# GEOMETRY -- UNIT 8: AREA, SURFACE AREA & VOLUME (build lg, 2026-08-22)
# =============================================================================
# PAST Basic U9 (rectangle area, counted cubes) and pre-u8 (triangle area), not
# over them: the height that is NOT the slant, the composite floor (areas add,
# lengths never do), the cube's six faces, and the capstone that finishes U4's
# scaling story -- length pays the factor once, area twice, VOLUME THREE TIMES.
# No renderer draws a parallelogram or an L-shape (the shelf was checked
# first), so these boards are carried by steps, in the mean/sare tradition.
_GEOMETRY_U8 = [
    {
        "id": "geo-u8-the-true-height",
        "course": "geometry", "unit": 8,
        "topic": "Area with the height",
        "op": "para", "max_value": 50,
        "levels": ("abstract",),
        "symbols": ("parallelogram", "height"),
        "advance_line": "Three in a row, and you can say why — you've got it! Base times height — the slant just leans.",
        "why": [
            ("Why the true height? Because a parallelogram is a pushed-over rectangle "
             "— same base, same height, just leaning — and its area is still base "
             "times height. But watch the words: the height is measured straight up, "
             "and the leaning side is NOT the height.",
             '[[goal text="The true height"]]'),
        ],
        "picture": [
            ("Here is a parallelogram with a base of 6 and a leaning side of 5. The "
             "dashed line inside it is the true height, straight up from the base: 4. "
             "The slanted side is longer than the height, because leaning wastes some "
             "length — the 5 is how long the side is, not how tall the shape stands.",
             '[[polygon kind="parallelogram" base="6" slant="5" height="4" caption="base 6, leaning side 5 — the dashed true height is 4"]]'),
        ],
        "teach": [
            ("That is the method. Base 6, slanted side 5, height 4. The area is base "
             "times height: 6 times 4, which equals 24. Why not the 5? Push the leaning "
             "stack straight and it becomes a rectangle 6 long and 4 tall — the 5 was "
             "never how tall it stood.",
             '[[rectangle w="6" h="4" caption="pushed straight: a 6 by 4 rectangle — area 24"]][[step eq="6 × 4 = 24"]]'),
            ("The trap always looks generous: the slant is longer than the height — "
             "leaning wastes some length — so grabbing the slanted 5 gets 30, too big. "
             "Ask of every length: is this how tall it STANDS, or just how long its "
             "side is?",
             '[[step eq="6 × 4 = 24 ✓"]][[step eq="6 × 5 = 30 ✗ — the slant is not the height"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Base 5, height 2, slanted side "
                        "3: the area is 5 times 2 — 10. The 3 sat this one out.",
                        '[[polygon kind="parallelogram" base="5" slant="3" height="2" caption="base 5, height 2 — area 10; the 3 sat it out"]][[step eq="5 × 2 = 10"]]'),
             "ask": {'a': 7, 'b': 3, 'c': 4, 'op': 'para'}},
            {"worked": ("One more together. Base 8, slant 6, height 5: 8 times 5 equals "
                        "40.",
                        '[[polygon kind="parallelogram" base="8" slant="6" height="5" caption="base 8, height 5 — area 40"]][[step eq="8 × 5 = 40"]]'),
             "ask": {'a': 10, 'b': 5, 'c': 6, 'op': 'para'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A parallelogram has "
                       "a base of 6, a leaning side of 5 and a height of 4, and its "
                       "area is 24. Tap the reason why."),
            "choices": ("because the area is the base times the true height | because "
                        "the area is the base times the leaning side | because the "
                        "area is all three lengths added"),
            "answer": "because the area is the base times the true height",
            "board": '[[polygon kind="parallelogram" base="6" slant="5" height="4" caption="6 × 4 = 24"]]',
        },
        "recap": [
            ("So, here it is again. A parallelogram\'s area is base times height, "
             "and the height stands straight up — the dashed line, never the leaning "
             "side. Push it straight and it is a rectangle; the slant only ever "
             "leaned.",
             '[[polygon kind="parallelogram" base="6" slant="5" height="4" caption="base 6 × height 4 = 24"]]'),
            ("And that is a pushed-over rectangle, measured honestly.",
             '[[step eq="6 × 4 = 24"]]'),
        ],
        "bank": [
            {"a": 4, "b": 3, "c": 5, "op": "para"},
            {"a": 5, "b": 3, "c": 4, "op": "para"},
            {"a": 6, "b": 3, "c": 5, "op": "para"},
            {"a": 5, "b": 4, "c": 6, "op": "para"},
            {"a": 8, "b": 3, "c": 5, "op": "para"},
            {"a": 7, "b": 4, "c": 5, "op": "para"},
            {"a": 8, "b": 4, "c": 6, "op": "para"},
            {"a": 9, "b": 4, "c": 5, "op": "para"},
            {"a": 10, "b": 4, "c": 6, "op": "para"},
            {"a": 9, "b": 5, "c": 7, "op": "para"},
        ],
    },
    {
        "id": "geo-u8-two-rooms",
        "course": "geometry", "unit": 8,
        "topic": "Composite area",
        "op": "lshp", "max_value": 50,
        "levels": ("abstract",),
        "symbols": ("area", "rectangles"),
        "advance_line": "Three in a row, and you can say why — you've got it! Cut, measure, put together.",
        "why": [
            ("Why two rooms? Because real floors are not always rectangles — but they "
             "are usually MADE of rectangles. An L-shaped floor is two rectangles "
             "standing together, and its area is found by cutting: find each "
             "rectangle\'s area, then put the areas together.",
             '[[goal text="Two rooms"]]'),
        ],
        "picture": [
            ("Here are the two rooms the L is cut into. One is 5 long and 3 wide; the "
             "other is 2 long and 3 wide. Each room is a rectangle you already know how "
             "to measure — and the whole floor is simply the two of them side by "
             "side.",
             '[[rectangle w="5" h="3" caption="one room: 5 by 3"]][[rectangle w="2" h="3" caption="the other room: 2 by 3"]]'),
        ],
        "teach": [
            ("That is the method. One part is 5 long and 3 wide: area 15. The other is "
             "2 long and 3 wide: area 6. The whole floor is 15 plus 6, which equals 21 "
             "— cut, measure, put together. Any shape built from rectangles gives in "
             "to this.",
             '[[rectangle w="5" h="3" caption="5 × 3 = 15"]][[rectangle w="2" h="3" caption="2 × 3 = 6"]][[step eq="15 + 6 = 21"]]'),
            ("Two traps. Stopping after one rectangle — 15 is only part of the floor. "
             "And adding the LENGTHS — 5 plus 3 plus 2 is 10, but lengths added give "
             "edges, not floor. Areas add to areas; lengths never do.",
             '[[step eq="15 + 6 = 21 ✓"]][[step eq="15 ✗ one room only · 5 + 3 + 2 = 10 ✗ lengths are not areas"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Rooms of 3 by 4 and 2 by 4: "
                        "areas 12 and 8, and the floor is 12 plus 8 — 20.",
                        '[[rectangle w="3" h="4" caption="3 × 4 = 12"]][[rectangle w="2" h="4" caption="2 × 4 = 8"]][[step eq="12 + 8 = 20"]]'),
             "ask": {'a': 5, 'b': 2, 'c': 4, 'op': 'lshp'}},
            {"worked": ("One more together. 7 by 2 and 3 by 2: 14 plus 6 equals 20.",
                        '[[rectangle w="7" h="2" caption="7 × 2 = 14"]][[rectangle w="3" h="2" caption="3 × 2 = 6"]][[step eq="14 + 6 = 20"]]'),
             "ask": {'a': 6, 'b': 5, 'c': 4, 'op': 'lshp'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A floor is made of "
                       "a 5 by 3 room and a 2 by 3 room, and its area is 21. Tap the "
                       "reason why."),
            "choices": ("because each room\'s area is found, then the areas are added | "
                        "because the lengths 5, 3 and 2 are added | because the bigger "
                        "room\'s area is the whole floor"),
            "answer": "because each room\'s area is found, then the areas are added",
            "board": '[[rectangle w="5" h="3" caption="15"]][[rectangle w="2" h="3" caption="6 — together 21"]]',
        },
        "recap": [
            ("So, here it is again. A floor made of rectangles is measured by cutting "
             "it into them: find each rectangle\'s area, then put the areas together. "
             "Never stop at one room, and never add the lengths — areas add to areas.",
             '[[rectangle w="5" h="3" caption="5 × 3 = 15"]][[rectangle w="2" h="3" caption="2 × 3 = 6 — the floor is 21"]]'),
            ("And that is cut, measure, put together.",
             '[[step eq="15 + 6 = 21"]]'),
        ],
        "bank": [
            {"a": 3, "b": 2, "c": 2, "op": "lshp"},
            {"a": 4, "b": 2, "c": 3, "op": "lshp"},
            {"a": 3, "b": 3, "c": 2, "op": "lshp"},
            {"a": 4, "b": 3, "c": 2, "op": "lshp"},
            {"a": 5, "b": 3, "c": 3, "op": "lshp"},
            {"a": 6, "b": 3, "c": 3, "op": "lshp"},
            {"a": 4, "b": 4, "c": 3, "op": "lshp"},
            {"a": 6, "b": 4, "c": 2, "op": "lshp"},
            {"a": 7, "b": 4, "c": 3, "op": "lshp"},
            {"a": 8, "b": 4, "c": 4, "op": "lshp"},
        ],
    },
    {
        "id": "geo-u8-six-faces",
        "course": "geometry", "unit": 8,
        "topic": "Surface area of a cube",
        "op": "surf", "max_value": 150,
        "levels": ("abstract",),
        "symbols": ("surface area", "faces"),
        "advance_line": "Three in a row, and you can say why — you've got it! Six faces, always six.",
        "why": [
            ("Why six faces? Because a cube is wrapped in six identical square faces: "
             "a top, a bottom, and four around the sides. That wrapping has a name. "
             "Surface area is the area of everything you could touch. Know ONE face "
             "and you know all six: the surface area is six of that face.",
             '[[goal text="Six faces"]]'),
        ],
        "picture": [
            ("Here is a cube. You can see three of its faces from here — the front, "
             "the top and one side — and three more hide behind: the back, the bottom "
             "and the other side. Six faces, every one the same square.",
             '[[solid kind="cube" caption="a cube — three faces showing, three hidden; six in all"]]'),
        ],
        "teach": [
            ("That is the method. Say one face has an area of 7. The cube has six "
             "faces just like it, so the surface area is 6 times 7, which equals 42 "
             "square units. One face, times six — that is the whole trick.",
             '[[bars data="top:7 | bottom:7 | front:7 | back:7 | left:7 | right:7" caption="six faces of 7 — 6 × 7 = 42"]][[step eq="6 × 7 = 42"]]'),
            ("The trap is forgetting the floor and the ceiling. Four faces stand "
             "around the sides, and counting only them is 4 times 7 — 28 — but that "
             "box is still open. The top and the bottom are faces too: six, always "
             "six.",
             '[[step eq="6 × 7 = 42 ✓"]][[step eq="4 × 7 = 28 ✗ — the top and bottom are faces too"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. One face is 9: the surface area "
                        "is 6 times 9 — 54 square units.",
                        '[[bars data="top:9 | bottom:9 | front:9 | back:9 | left:9 | right:9" caption="6 × 9 = 54"]][[step eq="6 × 9 = 54"]]'),
             "ask": {'a': 2, 'b': 0, 'op': 'surf'}},
            {"worked": ("One more together. A face of 14: the surface area is 6 times 14, "
                        "which equals 84.",
                        '[[bars data="top:14 | bottom:14 | front:14 | back:14 | left:14 | right:14" caption="6 × 14 = 84"]][[step eq="6 × 14 = 84"]]'),
             "ask": {'a': 25, 'b': 0, 'op': 'surf'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. One face of a cube "
                       "has an area of 7, so its surface area is 42. Tap the reason "
                       "why."),
            "choices": ("because a cube has six equal faces, top and bottom included | "
                        "because a cube has four faces standing round the sides | "
                        "because the surface area is one face, squared"),
            "answer": "because a cube has six equal faces, top and bottom included",
            "board": '[[solid kind="cube" caption="six faces of 7 — 6 × 7 = 42"]]',
        },
        "recap": [
            ("So, here it is again. Surface area is the area of everything you could "
             "touch, and a cube wears six identical faces — four around the sides, "
             "plus the top and the bottom. Know one face, and the surface area is six "
             "of it.",
             '[[solid kind="cube" caption="six equal faces"]]'),
            ("And that is a cube, wrapped and measured.",
             '[[step eq="6 × 7 = 42"]]'),
        ],
        "bank": [
            {"a": 3, "b": 0, "op": "surf"},
            {"a": 4, "b": 0, "op": "surf"},
            {"a": 5, "b": 0, "op": "surf"},
            {"a": 6, "b": 0, "op": "surf"},
            {"a": 8, "b": 0, "op": "surf"},
            {"a": 10, "b": 0, "op": "surf"},
            {"a": 12, "b": 0, "op": "surf"},
            {"a": 15, "b": 0, "op": "surf"},
            {"a": 18, "b": 0, "op": "surf"},
            {"a": 20, "b": 0, "op": "surf"},
        ],
    },
    {
        "id": "geo-u8-the-volume-surprise",
        "course": "geometry", "unit": 8,
        "topic": "Volume under scaling",
        "op": "svol", "max_value": 135,
        "levels": ("abstract",),
        "symbols": ("volume", "cubic"),
        "advance_line": "Three in a row, and you can say why — you've got it! Length once, area twice — volume three times.",
        "why": [
            ("Why a surprise? Because the last measure is volume — the room inside a "
             "box, counted in cubic units — and you already know the scaling story: "
             "length pays the factor once, area pays it twice. Volume lives in THREE "
             "directions — long, wide AND tall — so volume pays the factor three "
             "times.",
             '[[goal text="The volume surprise"]]'),
        ],
        "picture": [
            ("Here is a box, and every edge of it is about to be enlarged by 2: twice "
             "as long, twice as wide, twice as tall. Each of the three directions "
             "doubles, so the room inside is doubled three times over — 2 times 2 "
             "times 2, eight times the room.",
             '[[solid kind="prism" w="×2" d="×2" h="×2" caption="every edge × 2 — long, wide and tall: 2 × 2 × 2 = 8 times the room"]]'),
        ],
        "teach": [
            ("That is the method. A box holds 9 cubic units. Scale every edge by "
             "factor 2: the box grows twice as long, twice as wide, twice as tall — 2 "
             "times 2 times 2 is 8 times the room. 9 times 8 equals 72 cubic units.",
             '[[solid kind="prism" w="×2" d="×2" h="×2" caption="2 × 2 × 2 = 8 times the room"]][[step eq="9 × 8 = 72"]]'),
            ("The traps are the course\'s own history. Times 2 once — 18 — is the "
             "LENGTH habit. Times 2 twice — 36 — is the AREA habit from the similarity "
             "unit. Volume has one more direction waiting: times 2 three times, 72. "
             "Count the directions before you scale.",
             '[[step eq="9 × 2 × 2 × 2 = 72 ✓"]][[step eq="9 × 2 = 18 ✗ length habit · 9 × 4 = 36 ✗ area habit"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. A box of 12, factor 2: 12 times "
                        "8 — 96 cubic units.",
                        '[[solid kind="prism" w="×2" d="×2" h="×2" caption="8 times the room: 12 × 8 = 96"]][[step eq="12 × 8 = 96"]]'),
             "ask": {'a': 7, 'b': 2, 'op': 'svol'}},
            {"worked": ("One more together. Factor 3: 3 times 3 times 3 is 27 times the "
                        "room. A box of 6 becomes 6 times 27 — 162.",
                        '[[solid kind="prism" w="×3" d="×3" h="×3" caption="27 times the room: 6 × 27 = 162"]][[step eq="6 × 27 = 162"]]'),
             "ask": {'a': 5, 'b': 3, 'op': 'svol'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A box of 9 cubic "
                       "units has every edge enlarged by 2, and the new box holds 72. "
                       "Tap the reason why."),
            "choices": ("because volume pays the factor in all three directions | "
                        "because volume pays the factor once, like a length | because "
                        "volume pays the factor twice, like an area"),
            "answer": "because volume pays the factor in all three directions",
            "board": '[[solid kind="prism" w="×2" d="×2" h="×2" caption="9 × 2 × 2 × 2 = 72"]]',
        },
        "recap": [
            ("So, here it is again. Scale every edge of a box and the volume pays the "
             "factor three times — once for long, once for wide, once for tall. "
             "Length once, area twice, volume three times: count the directions "
             "before you scale.",
             '[[solid kind="prism" w="×2" d="×2" h="×2" caption="2 × 2 × 2 = 8 times the room"]]'),
            ("And that is the scaling story, told all the way up.",
             '[[step eq="9 × 8 = 72"]]'),
        ],
        "bank": [
            {"a": 2, "b": 2, "op": "svol"},
            {"a": 3, "b": 2, "op": "svol"},
            {"a": 4, "b": 2, "op": "svol"},
            {"a": 5, "b": 2, "op": "svol"},
            {"a": 6, "b": 2, "op": "svol"},
            {"a": 2, "b": 3, "op": "svol"},
            {"a": 8, "b": 2, "op": "svol"},
            {"a": 10, "b": 2, "op": "svol"},
            {"a": 3, "b": 3, "op": "svol"},
            {"a": 4, "b": 3, "op": "svol"},
        ],
    },
]
LESSONS.extend(_GEOMETRY_U8)


# =============================================================================
# GEOMETRY -- UNIT 9: PROBABILITY (build lg, 2026-08-22) -- ⭐ GEOMETRY FINISHES
# =============================================================================
# CHANCE IN CHILD NUMBERS -- counts out of a whole, never fractions. The whole
# bag is the out-of (odds-vs-probability is the standing wrong tap), the
# complement shares the whole, choices TIMES up, and the closer is the two-way
# table read like an address. Renderer rulings recorded in the ops: [[tree]]
# prints its leaf products (unusable on asks -- it stays on the shelf for the
# Probability & Statistics course), [[areamodel]] prints its expanded product
# (teach boards only), [[twoway]] auto-totals (so the ask is a CELL).
_GEOMETRY_U9 = [
    {
        "id": "geo-u9-out-of-all",
        "course": "geometry", "unit": 9,
        "topic": "Chance as a count",
        "op": "poft", "max_value": 15,
        "levels": ("abstract",),
        "symbols": ("chance", "in all"),
        "advance_line": "Three in a row, and you can say why — you've got it! Out of means out of everything.",
        "why": [
            ("Why chance? Because it is a new kind of number. A bag holds 3 red "
             "marbles and 2 blue ones. Pick without looking, and red is not certain — "
             "it has a chance: 3 out of 5. The first number counts the reds; the "
             "second counts everything in the bag — the marbles in all.",
             '[[goal text="Out of all"]]'),
        ],
        "picture": [
            ("Here is the whole bag as a pie: 3 red parts and 2 blue parts, five parts "
             "in all. The pick lands somewhere on this pie, and 3 of its 5 parts are "
             "red — that is what 3 out of 5 looks like.",
             '[[pie data="red:3 | blue:2" caption="the whole bag — 3 red, 2 blue, 5 in all: red is 3 out of 5"]]'),
        ],
        "teach": [
            ("That is the method. Why 5? Because the pick does not know about colors "
             "— it lands on one of ALL the marbles. 3 reds plus 2 blues is 5 marbles, "
             "so red\'s chance is 3 out of 5, and blue\'s is 2 out of 5. The out-of "
             "number is always the whole bag.",
             '[[bars data="red:3 | blue:2" caption="red 3 and blue 2"]][[step eq="3 + 2 = 5 in the bag"]][[step eq="red: 3 out of 5 · blue: 2 out of 5"]]'),
            ("The trap is saying 3 out of 2 — the reds against the blues. That "
             "compares the two teams, but a chance is not a comparison between "
             "teams: it is one team out of the WHOLE bag. Out of means out of "
             "everything.",
             '[[step eq="3 out of 5 ✓"]][[step eq="3 out of 2 ✗ — the blues are not the whole bag"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 5 reds and 4 blues: the bag "
                        "holds 5 plus 4 — 9 marbles — so red is 5 out of 9.",
                        '[[pie data="red:5 | blue:4" caption="5 + 4 = 9 — red is 5 out of 9"]][[step eq="5 + 4 = 9 · red: 5 out of 9"]]'),
             "ask": {'a': 2, 'b': 4, 'op': 'poft'}},
            {"worked": ("One more together. 7 reds, 5 blues: red is 7 out of 12, "
                        "because 7 plus 5 is 12.",
                        '[[pie data="red:7 | blue:5" caption="7 + 5 = 12 — red is 7 out of 12"]][[step eq="7 + 5 = 12"]]'),
             "ask": {'a': 6, 'b': 8, 'op': 'poft'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A bag holds 3 red "
                       "marbles and 2 blue, and the chance of red is 3 out of 5. Tap "
                       "the reason why."),
            "choices": ("because the pick lands on one of all 5 marbles | because the "
                        "reds are measured against the blues | because the chance is "
                        "always out of 5"),
            "answer": "because the pick lands on one of all 5 marbles",
            "board": '[[pie data="red:3 | blue:2" caption="red is 3 out of 5"]]',
        },
        "recap": [
            ("So, here it is again. A chance is one team out of the whole bag: the "
             "first number counts the team, the second counts everything in all. "
             "Never the reds against the blues — out of means out of everything.",
             '[[pie data="red:3 | blue:2" caption="3 out of 5"]]'),
            ("And that is the first number of chance.",
             '[[step eq="3 + 2 = 5 · red: 3 out of 5"]]'),
        ],
        "bank": [
            {"a": 2, "b": 3, "op": "poft"},
            {"a": 4, "b": 2, "op": "poft"},
            {"a": 3, "b": 4, "op": "poft"},
            {"a": 5, "b": 3, "op": "poft"},
            {"a": 6, "b": 3, "op": "poft"},
            {"a": 4, "b": 6, "op": "poft"},
            {"a": 7, "b": 4, "op": "poft"},
            {"a": 5, "b": 7, "op": "poft"},
            {"a": 8, "b": 5, "op": "poft"},
            {"a": 9, "b": 6, "op": "poft"},
        ],
    },
    {
        "id": "geo-u9-the-other-chance",
        "course": "geometry", "unit": 9,
        "topic": "The complement",
        "op": "notp", "max_value": 20,
        "levels": ("abstract",),
        "symbols": ("chance", "out of"),
        "advance_line": "Three in a row, and you can say why — you've got it! What one chance does not take, the other gets.",
        "why": [
            ("Why the other chance? Because every chance has a shadow. If rain\'s "
             "chance is 3 out of 10, what about NO rain? The two together cover every "
             "possibility — some days it rains, all the other days it does not — so "
             "their chances share the whole 10. What rain does not take, no-rain "
             "gets.",
             '[[goal text="The other chance"]]'),
        ],
        "picture": [
            ("Here are all 10 chances as a pie, with rain\'s 3 shaded. Everything "
             "left unshaded belongs to no-rain — 7 parts. The two together fill the "
             "whole pie, because every chance belongs to somebody.",
             '[[pie parts="10" shaded="3" caption="10 chances — rain takes 3, no rain gets the other 7"]]'),
        ],
        "teach": [
            ("That is the method. Rain: 3 out of 10. All ten chances belong to "
             "somebody, so no-rain takes the rest: 10 take away 3, which equals 7 — no "
             "rain is 7 out of 10. Check: 3 plus 7 equals 10, every chance spoken "
             "for.",
             '[[bars data="rain:3 | no rain:7" caption="3 + 7 = 10 — every chance spoken for"]][[step eq="10 − 3 = 7"]][[step eq="3 + 7 = 10 ✓"]]'),
            ("Two traps. The other chance is usually NOT the same number — 3 out of "
             "10 for rain leaves 7 for no-rain, not 3. And it is never the whole 10 — "
             "that would call no-rain certain while rain still holds its 3. Take "
             "away, then check the two put the whole back.",
             '[[step eq="10 − 3 = 7 ✓"]][[step eq="3 ✗ copied · 10 ✗ nothing here is certain"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. A chance of 4 out of 9: the "
                        "other chance is 9 take away 4 — 5 out of 9.",
                        '[[bars data="rain:4 | no rain:5" caption="4 + 5 = 9"]][[step eq="9 − 4 = 5"]]'),
             "ask": {'a': 2, 'b': 9, 'op': 'notp'}},
            {"worked": ("One more together. 6 out of 13: the other chance is 13 take "
                        "away 6 — 7 out of 13.",
                        '[[bars data="rain:6 | no rain:7" caption="6 + 7 = 13"]][[step eq="13 − 6 = 7"]]'),
             "ask": {'a': 7, 'b': 20, 'op': 'notp'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. The chance of rain "
                       "is 3 out of 10, so the chance of no rain is 7 out of 10. Tap "
                       "the reason why."),
            "choices": ("because the two chances share all 10 between them | because "
                        "the other chance is always the same number | because no rain "
                        "is certain, so it takes all 10"),
            "answer": "because the two chances share all 10 between them",
            "board": '[[pie parts="10" shaded="3" caption="rain 3, no rain 7 — 10 in all"]]',
        },
        "recap": [
            ("So, here it is again. A chance and its other chance share the whole "
             "between them. Take the one you know away from the whole, and what is "
             "left is the other — then check that the two put the whole back.",
             '[[pie parts="10" shaded="3" caption="10 − 3 = 7"]]'),
            ("And that is every chance, spoken for.",
             '[[step eq="10 − 3 = 7"]]'),
        ],
        "bank": [
            {"a": 2, "b": 5, "op": "notp"},
            {"a": 4, "b": 7, "op": "notp"},
            {"a": 2, "b": 6, "op": "notp"},
            {"a": 5, "b": 9, "op": "notp"},
            {"a": 3, "b": 8, "op": "notp"},
            {"a": 4, "b": 10, "op": "notp"},
            {"a": 5, "b": 12, "op": "notp"},
            {"a": 4, "b": 12, "op": "notp"},
            {"a": 6, "b": 15, "op": "notp"},
            {"a": 5, "b": 16, "op": "notp"},
        ],
    },
    {
        "id": "geo-u9-how-many-ways",
        "course": "geometry", "unit": 9,
        "topic": "Counting choices",
        "op": "outc", "max_value": 28,
        "levels": ("abstract",),
        "symbols": ("choice", "times"),
        "advance_line": "Three in a row, and you can say why — you've got it! Choices times up, never add.",
        "why": [
            ("Why count the ways? Because counting comes back, one last time. Say you "
             "own 2 shirts and 3 hats. Getting dressed is one choice, then another — "
             "and for EVERY shirt, every one of the hats is still open. Choices do not "
             "add up; they times up: 2 shirts times 3 hats.",
             '[[goal text="How many ways"]]'),
        ],
        "picture": [
            ("Here is the outfit grid: one row for each shirt, one column for each "
             "hat. Every box is one full outfit — the first shirt with the first hat, "
             "the first shirt with the second hat, and so on. 2 rows of 3 boxes: six "
             "boxes, six outfits.",
             '[[array rows="2" cols="3" caption="2 rows of 3 — every box is one outfit"]]'),
        ],
        "teach": [
            ("That is the method. Draw the grid: a row for each shirt, a column for "
             "each hat. 2 rows of 3 boxes is 2 times 3, which equals 6 outfits. When "
             "choices stack, times.",
             '[[array rows="2" cols="3" caption="2 × 3 = 6 outfits"]][[step eq="2 × 3 = 6 outfits"]]'),
            ("The trap is adding: 2 shirts plus 3 hats is 5 THINGS, but things are "
             "not outfits — each outfit uses one of each. And do not stop at the "
             "shirts: 2 is a closet, not a count of ways. When choices stack, times; "
             "when piles pour into one pile, add.",
             '[[step eq="2 × 3 = 6 ✓"]][[step eq="2 + 3 = 5 ✗ — that counts things, not outfits"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 4 shirts and 5 hats: 4 times 5 "
                        "equals 20 different outfits.",
                        '[[array rows="4" cols="5" caption="4 × 5 = 20 outfits"]][[step eq="4 × 5 = 20"]]'),
             "ask": {'a': 6, 'b': 2, 'op': 'outc'}},
            {"worked": ("One more together. 3 shirts and 6 hats — 3 times 6, which "
                        "equals 18 ways.",
                        '[[array rows="3" cols="6" caption="3 × 6 = 18 outfits"]][[step eq="3 × 6 = 18"]]'),
             "ask": {'a': 9, 'b': 3, 'op': 'outc'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. With 2 shirts and "
                       "3 hats there are 6 different outfits. Tap the reason why."),
            "choices": ("because every shirt can go with every one of the hats | "
                        "because 2 shirts and 3 hats are 5 things | because the "
                        "number of outfits is the number of shirts"),
            "answer": "because every shirt can go with every one of the hats",
            "board": '[[array rows="2" cols="3" caption="2 × 3 = 6 outfits"]]',
        },
        "recap": [
            ("So, here it is again. When one choice stacks on another, the ways times "
             "up — a row for each of the first, a column for each of the second, and "
             "every box is one way. Adding counts things, never outfits.",
             '[[array rows="2" cols="3" caption="2 × 3 = 6"]]'),
            ("And that is choices, timesed up.",
             '[[step eq="2 × 3 = 6"]]'),
        ],
        "bank": [
            {"a": 3, "b": 2, "op": "outc"},
            {"a": 4, "b": 2, "op": "outc"},
            {"a": 5, "b": 2, "op": "outc"},
            {"a": 4, "b": 3, "op": "outc"},
            {"a": 7, "b": 2, "op": "outc"},
            {"a": 5, "b": 3, "op": "outc"},
            {"a": 6, "b": 3, "op": "outc"},
            {"a": 5, "b": 4, "op": "outc"},
            {"a": 8, "b": 3, "op": "outc"},
            {"a": 7, "b": 4, "op": "outc"},
        ],
    },
    {
        "id": "geo-u9-reading-the-table",
        "course": "geometry", "unit": 9,
        "topic": "Two-way tables",
        "op": "twop", "max_value": 14,
        "levels": ("abstract",),
        "symbols": ("table", "row"),
        "advance_line": "Three in a row, and you can say why — you've got it! The right row, the right column, the box where they cross.",
        "why": [
            ("Why a table? Because numbers love one. A class chose sports: the boys\' "
             "counts sit in one row, the girls\' in another; soccer fills one column, "
             "art the next. Every student lands in exactly one box, and reading the "
             "right box answers most questions before any arithmetic starts.",
             '[[goal text="Reading the table"]]'),
        ],
        "picture": [
            ("Here is the table. Two rows — boys, then girls — and two columns — "
             "soccer, then art. Four boxes, and each holds one count: the boys who "
             "chose soccer, the boys who chose art, the girls who chose soccer, the "
             "girls who chose art.",
             '[[twoway rowlabels="boys,girls" collabels="soccer,art" data="4,3|2,6" caption="two rows, two columns — four boxes of counts"]]'),
        ],
        "teach": [
            ("That is the method. How many girls chose soccer? Find the girls row — "
             "the second one. Slide along to the soccer column. The box where they "
             "cross holds 2: two girls chose soccer. Row first, then column — an "
             "address, like a point on the grid.",
             '[[twoway rowlabels="boys,girls" collabels="soccer,art" data="4,3|2,6" caption="girls row, soccer column — the crossing holds 2"]][[step eq="girls row → soccer column → 2"]]'),
            ("The traps are the next-door boxes. Stay in the soccer column but drift "
             "to the boys row: 4 — right sport, wrong students. Stay with the girls but "
             "slide to art: 6 — right students, wrong sport. Cross the RIGHT row with "
             "the RIGHT column, every time.",
             '[[step eq="girls + soccer = 2 ✓"]][[step eq="4 ✗ wrong row · 6 ✗ wrong column"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. How many girls chose art here? "
                        "Girls row, art column — the box holds 7.",
                        '[[twoway rowlabels="boys,girls" collabels="soccer,art" data="5,2|3,7" caption="girls row, art column — 7"]][[step eq="girls row → art column → 7"]]'),
             "ask": {'a': 5, 'b': 6, 'c': 2, 'op': 'twop'}},
            {"worked": ("One more together. In this table the girls-and-art box holds 5 "
                        "— right row, right column, done.",
                        '[[twoway rowlabels="boys,girls" collabels="soccer,art" data="6,4|8,5" caption="girls row, art column — 5"]][[step eq="girls row → art column → 5"]]'),
             "ask": {'a': 11, 'b': 10, 'c': 12, 'op': 'twop'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. In the table, the "
                       "number of girls who chose soccer is 2. Tap the reason why."),
            "choices": ("because 2 sits where the girls row meets the soccer column | "
                        "because 2 is the smallest number in the table | because the "
                        "girls row is the first row"),
            "answer": "because 2 sits where the girls row meets the soccer column",
            "board": '[[twoway rowlabels="boys,girls" collabels="soccer,art" data="4,3|2,6" caption="girls row, soccer column → 2"]]',
        },
        "recap": [
            ("So, here it is again. A table holds a count in every box, and a box is "
             "an address: the right row crossed with the right column. Row first, "
             "then column — and beware the next-door boxes, right row but wrong "
             "column, right column but wrong row.",
             '[[twoway rowlabels="boys,girls" collabels="soccer,art" data="4,3|2,6" caption="girls row, soccer column → 2"]]'),
            ("And that is a table, read at the crossing.",
             '[[step eq="girls row → soccer column → 2"]]'),
        ],
        "bank": [
            {"a": 3, "b": 5, "c": 2, "op": "twop"},
            {"a": 4, "b": 2, "c": 3, "op": "twop"},
            {"a": 5, "b": 7, "c": 4, "op": "twop"},
            {"a": 6, "b": 3, "c": 5, "op": "twop"},
            {"a": 4, "b": 9, "c": 6, "op": "twop"},
            {"a": 7, "b": 5, "c": 7, "op": "twop"},
            {"a": 8, "b": 6, "c": 8, "op": "twop"},
            {"a": 9, "b": 7, "c": 9, "op": "twop"},
            {"a": 10, "b": 8, "c": 10, "op": "twop"},
            {"a": 12, "b": 9, "c": 11, "op": "twop"},
        ],
    },
]
LESSONS.extend(_GEOMETRY_U9)

# ---- this course's slice of COURSE_ORDER: the teaching order (lessons/__init__.py joins the ten) ----
ORDER = [

    # ---- GEOMETRY (build lc) -- Unit 1: Foundations & Constructions ----
    "geo-u1-two-make-a-corner", "geo-u1-when-lines-cross",
    "geo-u1-across-the-circle", "geo-u1-halfway-along",
    # Unit 2: Transformations & Symmetry -- slide, flip, half turn, turn symmetry
    "geo-u2-slide-it-over", "geo-u2-flip-it-across",
    "geo-u2-half-turn", "geo-u2-turns-onto-itself",
    # Unit 3: Congruence & Triangle Proofs -- the letters match the parts, then
    # the isosceles pair both directions and the exterior angle's first proof
    "geo-u3-matching-parts", "geo-u3-two-equal-sides",
    "geo-u3-the-outside-angle", "geo-u3-share-the-rest",
    # Unit 4: Similarity & Dilations -- a scale factor is a times, never an add
    "geo-u4-the-enlarging-copy", "geo-u4-finding-the-factor",
    "geo-u4-the-matching-side", "geo-u4-the-area-surprise",
    # Unit 5: Right Triangles & Trigonometry -- Pythagoras both directions, then
    # the tangent met as U4's ratio inside one triangle
    "geo-u5-the-longest-side", "geo-u5-the-missing-leg",
    "geo-u5-the-climb-ratio", "geo-u5-using-the-tangent",
    # Unit 6: Circles -- the whole is 360; the inscribed angle both directions
    "geo-u6-the-rest-of-the-circle", "geo-u6-half-the-arc",
    "geo-u6-double-it-back", "geo-u6-a-piece-of-the-rim",
    # Unit 7: Coordinate Geometry -- the grid: steps not dots, the straight path,
    # the midpoint in 2D, the fourth corner
    "geo-u7-straight-up", "geo-u7-the-straight-path",
    "geo-u7-the-middle-of-a-line", "geo-u7-the-fourth-corner",
    # Unit 8: Area, Surface Area & Volume -- past Basic U9, not over it
    "geo-u8-the-true-height", "geo-u8-two-rooms",
    "geo-u8-six-faces", "geo-u8-the-volume-surprise",
    # Unit 9: Probability -- chance in child numbers; ⭐ GEOMETRY COMPLETE
    "geo-u9-out-of-all", "geo-u9-the-other-chance",
    "geo-u9-how-many-ways", "geo-u9-reading-the-table",
]

# I did no harm and this file is not truncated.

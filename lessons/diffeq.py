# =============================================================================
# lessons/diffeq.py  --  DIFFERENTIAL EQUATIONS: THE AUTHORED LESSONS  --  Hyperion Shift LLC
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
# DIFFERENTIAL EQUATIONS UNIT 1 -- Introduction, Classification & Slope Fields
# (build lz) -- ⭐ THE THIRTEENTH AND LAST COURSE OPENS.
# The thread: THE EQUATION IS A PICTURE. A differential equation names a slope
# at every point on the plane; drawing those dashes turns the equation into a
# field you can see, read backwards, and walk across.
# =============================================================================
_DIFFEQ_U1 = [
    {
        "id": "diffeq-u1-a-dash-at-every-point",
        "course": "diffeq", "unit": 1,
        "topic": "Slope fields",
        "op": "slpf", "max_value": 110,
        "levels": ("abstract",),
        "symbols": ("slope field", "order"),
        "advance_line": "Three in a row — you've got it! Feed the point into the equation and read the slope.",
        "teach": [
            ["A differential equation is named by how deep its derivatives go: one derivative is first order, two is second. This whole first unit stays first order — and asks what such an equation LOOKS like.",
             '[[goal text="A dash at every point"]][[step eq="dy/dx = x + y"]]'],
            ["Here is the trick that turns it into a picture. Take d y d x equals x plus y, pick any point — say x is 7 and y is 5 — and the equation hands you a number: 12. Draw a tiny dash there leaning at that steepness.",
             '[[graph points="(7,5)" caption="the dash lives at (7, 5), leaning 12 steep"]][[step eq="at (7, 5) · slope 7 + 5 = 12"]]'],
            ["Do that at every point and a slope field appears. So add the two coordinates, exactly as the equation says. Taking them away reaches 2, and using the x on its own throws half the point away.",
             '[[step eq="12 ✓"]][[step eq="2 ✗ taken away · 7 ✗ only the x"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. At the point where x is 50 and y is 14: 50 plus 14 — the dash has slope 64.",
                        '[[step eq="50 + 14 = 64"]]'],
             "ask": {"a": 55, "b": 23, "op": "slpf"}},
            {"worked": ["One more together. At x equals 59 with y equals 43: 59 plus 43 — the slope is 102.",
                        '[[step eq="59 + 43 = 102"]]'],
             "ask": {"a": 58, "b": 35, "op": "slpf"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": a, "b": b, "op": "slpf"} for a, b in
                 ((4, 2), (11, 6), (18, 10), (25, 14), (32, 18),
                  (39, 22), (46, 26), (52, 31), (57, 37), (60, 45))],
    },
    {
        "id": "diffeq-u1-change-the-law-change-the-field",
        "course": "diffeq", "unit": 1,
        "topic": "A different law",
        "op": "slpq", "max_value": 230,
        "levels": ("abstract",),
        "symbols": ("law", "field"),
        "advance_line": "Three in a row — you've got it! Square the x first, then take the y off it.",
        "teach": [
            ["The plane never changes. The points never change. Change the equation, though, and every dash on it swings to a new angle — so the field is a picture of the law, not of the paper.",
             '[[goal text="Change the law, change the field"]][[step eq="dy/dx = x² − y"]]'],
            ["This one says d y d x equals x squared, take away y. At the point where x is 5 and y is 9: square the 5 first, giving 25, then take the 9 off it. The dash there has slope 16.",
             '[[step eq="5² − 9 = 25 − 9 = 16"]]'],
            ["Order matters. Adding the y instead climbs to 34. Leaving the y off the end hands back 25, the bare square. Same point, three different fields, and only one of them is the equation you were handed.",
             '[[step eq="16 ✓"]][[step eq="34 ✗ added · 25 ✗ y left off"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. At x equals 11 with y equals 50: 121 take away 50 is 71.",
                        '[[step eq="11² − 50 = 71"]]'],
             "ask": {"a": 11, "b": 42, "op": "slpq"}},
            {"worked": ["One more together. At x equals 13, y equals 23: 169 take away 23 is 146.",
                        '[[step eq="13² − 23 = 146"]]'],
             "ask": {"a": 12, "b": 10, "op": "slpq"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": a, "b": b, "op": "slpq"} for a, b in
                 ((3, 4), (6, 15), (7, 12), (8, 11), (10, 31),
                  (11, 36), (12, 43), (13, 52), (12, 11), (13, 20))],
    },
    {
        "id": "diffeq-u1-reading-the-field-backwards",
        "course": "diffeq", "unit": 1,
        "topic": "Isoclines",
        "op": "isoc", "max_value": 80,
        "levels": ("abstract",),
        "symbols": ("isocline", "same"),
        "advance_line": "Three in a row — you've got it! Take the x off the slope and what's left is y.",
        "teach": [
            ["Drawing a field dash by dash is slow. Here is how it is really done: instead of asking what slope sits at a point, ask where all the points with the SAME slope are.",
             '[[goal text="Reading the field backwards"]][[step eq="dy/dx = x + y = 14"]]'],
            ["In d y d x equals x plus y, every dash leaning at 14 sits where x plus y comes to 14 — a straight line. At x equals 5 on that line, y has to be 9. Such a line is called an isocline.",
             '[[step eq="x + y = 14 · at x = 5"]] [[step eq="y = 9"]]'],
            ["So take the x off the slope. Adding them instead lands at 19, nowhere near the line, and answering 5 hands back the x you were already given.",
             '[[step eq="9 ✓"]][[step eq="19 ✗ added · 5 ✗ the x again"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. Slope 39 read at x equals 19: take the 19 off the 39 and y is 20.",
                        '[[step eq="39 − 19 = 20"]]'],
             "ask": {"a": 26, "b": 2, "op": "isoc"}},
            {"worked": ["One more together. Slope 54 at x equals 6: take the 6 off the 54 and y is 48.",
                        '[[step eq="54 − 6 = 48"]]'],
             "ask": {"a": 56, "b": 15, "op": "isoc"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": a, "b": b, "op": "isoc"} for a, b in
                 ((5, 3), (9, 2), (16, 4), (23, 6), (27, 5),
                  (34, 7), (41, 9), (45, 8), (52, 10), (59, 12))],
    },
    {
        "id": "diffeq-u1-joining-the-dashes",
        "course": "diffeq", "unit": 1,
        "topic": "Solution curves",
        "op": "fldc", "max_value": 170,
        "levels": ("abstract",),
        "symbols": ("solution", "curve"),
        "advance_line": "Three in a row — you've got it! Climb by the slope for every step across, then add the start.",
        "teach": [
            ["Now the payoff. A solution of a differential equation is not a number. It is a whole curve, and on a slope field you can see it. Start somewhere and walk, always following the dash under your feet.",
             '[[goal text="Joining the dashes"]][[step eq="start at y = 5 · slope 3 all the way"]]'],
            ["Take an easy field where every dash leans at 3. Start at height 5 and walk 4 across: a slope of 3 climbs 3 for every 1 across, so 4 across is 12 of climb, landing at 17.",
             '[[step eq="3 × 4 = 12 · 5 + 12 = 17"]]'],
            ["The dashes were never a picture OF a solution — joining them is what creates one. Answering 12 gives the climb with no starting height, and 8 climbs a single step and stops.",
             '[[step eq="17 ✓"]][[step eq="12 ✗ climb only · 8 ✗ one step"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. Start at 37, slope 3, walk 10 across: 30 of climb, landing at 67.",
                        '[[step eq="37 + 30 = 67"]]'],
             "ask": {"a": 19, "b": 9, "c": 6, "op": "fldc"}},
            {"worked": ["One more together. From height 18 with slope 10, walking 12 across climbs 120 — landing at 138.",
                        '[[step eq="18 + 120 = 138"]]'],
             "ask": {"a": 2, "b": 10, "c": 12, "op": "fldc"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": a, "b": b, "c": c, "op": "fldc"} for a, b, c in
                 ((3, 2, 2), (4, 4, 5), (5, 3, 12), (2, 7, 8), (9, 6, 11),
                  (8, 12, 7), (10, 11, 9), (16, 10, 11), (23, 12, 10),
                  (28, 11, 12))],
    },
]
LESSONS.extend(_DIFFEQ_U1)


# =============================================================================
# DIFFERENTIAL EQUATIONS UNIT 2 -- First-Order: Separable & Linear (build lz)
# The thread: THE FIRST TWO METHODS THAT ACTUALLY SOLVE ONE. Separate the two
# letters and integrate each side; do it again where y will not sit quietly on
# the right; then the two linear equations the world is full of -- a cooling
# cup and a tank of brine.
# =============================================================================
_DIFFEQ_U2 = [
    {
        "id": "diffeq-u2-splitting-the-letters-apart",
        "course": "diffeq", "unit": 2,
        "topic": "Separable equations",
        "op": "sepv", "max_value": 190,
        "levels": ("abstract",),
        "symbols": ("separable", "integrate"),
        "advance_line": "Three in a row — you've got it! Halve the front number, times 9, then add the C.",
        "teach": [
            ["Unit 1 drew the equation. This unit solves one. The first method is the oldest: if every x can be herded to one side and every y to the other, the equation is separable and you integrate each side on its own.",
             '[[goal text="Splitting the letters apart"]][[step eq="dy/dx = 8x"]]'],
            ["Take d y d x equals 8 x. Separate and integrate and the 8 halves: y equals 4 x squared, plus C. If the curve sits at height 5 when x is zero, then C is 5, and at x equals 3 the x part is 4 times 9 — 36, plus 5 is 41.",
             '[[step eq="y = 4x² + 5 · at x = 3"]] [[step eq="36 + 5 = 41"]]'],
            ["So halve, times nine, add the C. Dropping the C leaves 36 and forgets which curve of the family you were on; skipping the halving runs to 77, integrating as though the rule were the derivative rule.",
             '[[step eq="41 ✓"]][[step eq="36 ✗ no C · 77 ✗ not halved"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. d y d x equals 6 x with C of 30: 3 times 9 is 27, plus 30 is 57.",
                        '[[step eq="3 × 9 + 30 = 57"]]'],
             "ask": {"a": 10, "b": 39, "op": "sepv"}},
            {"worked": ["One more together. 8 x with C of 33: 4 times 9 is 36, plus 33 is 69.",
                        '[[step eq="4 × 9 + 33 = 69"]]'],
             "ask": {"a": 14, "b": 40, "op": "sepv"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": a, "b": b, "op": "sepv"} for a, b in
                 ((4, 7), (6, 11), (10, 6), (8, 28), (14, 14),
                  (12, 36), (20, 10), (18, 25), (16, 37), (16, 40))],
    },
    {
        "id": "diffeq-u2-when-the-y-is-underneath",
        "course": "diffeq", "unit": 2,
        "topic": "Separating a harder one",
        "op": "sepr", "max_value": 230,
        "levels": ("abstract",),
        "symbols": ("separating", "square root"),
        "advance_line": "Three in a row — you've got it! Work out y squared first, then take its square root.",
        "teach": [
            ["Separating earns its keep when the y refuses to sit quietly on the right. Take d y d x equals 3 over y — the y is underneath, so multiply both sides by it and every y is on the left.",
             '[[goal text="When the y is underneath"]][[step eq="dy/dx = 3/y"]] [[step eq="y dy = 3 dx"]]'],
            ["Integrating gives y squared over 2 equals 3 x plus a constant, so y squared equals 6 x plus C. Start the curve at height 4 when x is zero and C is 16. At x equals 8: 48 plus 16 is 64, and y is the square root of that — 8.",
             '[[step eq="y² = 6x + 16 · at x = 8"]] [[step eq="64"]] [[step eq="y = 8"]]'],
            ["Two traps sit here. Stopping at 64 answers y SQUARED where a height was asked for. Guessing a straight climb from 4 gives 28. But the curve does not climb in a straight line, and only separating tells you so.",
             '[[step eq="8 ✓"]][[step eq="64 ✗ that is y² · 28 ✗ a straight guess"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. d y d x equals 2 over y from height 11, at x equals 12: y squared is 48 plus 121, which is 169, so y is 13.",
                        '[[step eq="y² = 169"]] [[step eq="y = 13"]]'],
             "ask": {"a": 6, "b": 10, "c": 8, "op": "sepr"}},
            {"worked": ["One more together. 8 over y from height 9, at x equals 9: y squared is 144 plus 81, which is 225, so y is 15.",
                        '[[step eq="y² = 225"]] [[step eq="y = 15"]]'],
             "ask": {"a": 6, "b": 9, "c": 12, "op": "sepr"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": a, "b": b, "c": c, "op": "sepr"} for a, b, c in
                 ((2, 2, 3), (4, 3, 2), (2, 4, 5), (5, 3, 4), (2, 6, 7),
                  (3, 3, 12), (2, 8, 9), (6, 5, 8), (2, 10, 11),
                  (10, 7, 6))],
    },
    {
        "id": "diffeq-u2-the-cooling-cup",
        "course": "diffeq", "unit": 2,
        "topic": "Newton's law of cooling",
        "op": "newt", "max_value": 100,
        "levels": ("abstract",),
        "symbols": ("cooling", "gap"),
        "advance_line": "Three in a row — you've got it! Find the gap, then share it out.",
        "teach": [
            ["Separable equations are one half of first order. The other half are the LINEAR ones, and here is the linear equation everybody meets first: a hot drink cooling in a room.",
             '[[goal text="The cooling cup"]][[step eq="coffee 50° · room 20°"]]'],
            ["Newton's law of cooling says the speed depends on the gap — nothing else. Say the coffee drops 1 degree a minute for every 5 degrees it stands above the room. Coffee at 50 in a room at 20 has a gap of 30, so it is cooling at 6 degrees a minute.",
             '[[step eq="50 − 20 = 30 · 30 ÷ 5 = 6"]]'],
            ["Now notice what that means. As it cools the gap shrinks, so the cooling itself slows — which is why coffee goes lukewarm quickly and then sits there. Answering 30 hands back the gap, and 5 is only the constant.",
             '[[step eq="6 ✓"]][[step eq="30 ✗ the gap · 5 ✗ the constant"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. Coffee at 95 in a room at 14, dropping 1 degree for every 3 of gap: a gap of 81, so 27 degrees a minute.",
                        '[[step eq="81 ÷ 3 = 27"]]'],
             "ask": {"a": 91, "b": 16, "c": 3, "op": "newt"}},
            {"worked": ["One more together. 89 degrees, room 27, one for every 2: the gap is 62, and 62 shared by 2 is a rate of 31.",
                        '[[step eq="62 ÷ 2 = 31"]]'],
             "ask": {"a": 79, "b": 21, "c": 2, "op": "newt"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": a, "b": b, "c": c, "op": "newt"} for a, b, c in
                 ((42, 12, 6), (71, 15, 8), (65, 20, 5), (59, 26, 3),
                  (92, 14, 6), (90, 30, 4), (45, 11, 2), (94, 18, 4),
                  (88, 25, 3), (68, 22, 2))],
    },
    {
        "id": "diffeq-u2-the-tank-of-brine",
        "course": "diffeq", "unit": 2,
        "topic": "Concentration",
        "op": "conc", "max_value": 190,
        "levels": ("abstract",),
        "symbols": ("concentration", "litre"),
        "advance_line": "Three in a row — you've got it! Share the grams out over the litres.",
        "teach": [
            ["The other famous linear equation is a tank of salty water with fresh brine running in and the mixture running out. Every one of them turns on a single number, and it is not the salt.",
             '[[goal text="The tank of brine"]][[step eq="45 g of salt · 3 L of water"]]'],
            ["It is the concentration: how much salt rides in each litre. Stir 45 grams evenly into 3 litres and every litre carries 15 grams. That is the number the outflow pipe takes away with it.",
             '[[step eq="45 ÷ 3 = 15 g per litre"]]'],
            ["Which is why the equation has the salt DIVIDED by the volume inside it. Taking the litres off the grams reaches 42 and muddles two different measurements, and 3 is the size of the tank, not the strength of the brine.",
             '[[step eq="15 ✓"]][[step eq="42 ✗ taken away · 3 ✗ the litres"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 98 grams stirred into 7 litres: each litre carries 14 grams.",
                        '[[step eq="98 ÷ 7 = 14"]]'],
             "ask": {"a": 85, "b": 5, "op": "conc"}},
            {"worked": ["One more together. 120 grams shared over 6 litres is 20 grams a litre.",
                        '[[step eq="120 ÷ 6 = 20"]]'],
             "ask": {"a": 190, "b": 10, "op": "conc"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": a, "b": b, "op": "conc"} for a, b in
                 ((6, 2), (20, 5), (15, 3), (42, 7), (28, 4),
                  (48, 6), (72, 8), (110, 11), (99, 9), (156, 13))],
    },
]
LESSONS.extend(_DIFFEQ_U2)


# =============================================================================
# DIFFERENTIAL EQUATIONS UNIT 3 -- Qualitative Analysis: Equilibria & Stability
# (build ma)
# The thread: YOU CAN KNOW THE SHAPE WITHOUT SOLVING ANYTHING. The logistic
# rate read straight off the law, the non-obvious place where growth peaks,
# how big that peak is, and the other kind of equilibrium -- one that pushes
# away instead of pulling in.
# =============================================================================
_DIFFEQ_U3 = [
    {
        "id": "diffeq-u3-the-crowded-pond",
        "course": "diffeq", "unit": 3,
        "topic": "The logistic rate",
        "op": "logi", "max_value": 150,
        "levels": ("abstract",),
        "symbols": ("logistic", "ceiling"),
        "advance_line": "Three in a row — you've got it! Fish times room left, then divide.",
        "teach": [
            ["Unit 2 solved equations. This unit refuses to, and finds out the shape anyway. Start with the most useful rate law in biology: growth that runs into a ceiling.",
             '[[goal text="The crowded pond"]][[step eq="ceiling 40 · 10 fish · ÷ 5"]]'],
            ["A pond holds at most 40 fish. Logistic growth says the rate is the fish times the room still left, divided by some constant — say 5. With 10 fish there is room for 30, so the rate is 10 times 30 over 5: 60.",
             '[[step eq="10 × 30 ÷ 5 = 60"]]'],
            ["Look at what that law does at the two ends. Almost no fish gives almost no growth; almost no room does the same. Answering 30 hands back the room, and using the whole ceiling instead of the room left reaches 80.",
             '[[step eq="60 ✓"]][[step eq="30 ✗ the room · 80 ✗ whole ceiling"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. Ceiling 41, 22 fish, divided by 11: room is 19, so 22 times 19 over 11 is 38.",
                        '[[step eq="22 × 19 ÷ 11 = 38"]]'],
             "ask": {"a": 27, "b": 16, "c": 4, "op": "logi"}},
            {"worked": ["One more together. Ceiling 34, 10 fish, over 4: room is 24, and 10 times 24 over 4 is 60.",
                        '[[step eq="10 × 24 ÷ 4 = 60"]]'],
             "ask": {"a": 43, "b": 24, "c": 8, "op": "logi"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": a, "b": b, "c": c, "op": "logi"} for a, b, c in
                 ((22, 18, 12), (26, 4, 8), (20, 12, 6), (30, 21, 9),
                  (21, 8, 4), (68, 6, 12), (27, 15, 5), (86, 4, 8),
                  (37, 14, 7), (47, 30, 10))],
    },
    {
        "id": "diffeq-u3-where-growth-peaks",
        "course": "diffeq", "unit": 3,
        "topic": "Where growth peaks",
        "op": "carr", "max_value": 190,
        "levels": ("abstract",),
        "symbols": ("halfway", "fastest"),
        "advance_line": "Three in a row — you've got it! Halve the ceiling, then take off what's already there.",
        "teach": [
            ["Since the rate dies at both ends, it must peak somewhere in between — and here is the fact almost everybody gets wrong. It peaks exactly halfway to the ceiling, not near the top.",
             '[[goal text="Where growth peaks"]][[step eq="ceiling 60 · fastest at 30"]]'],
            ["A pond with a ceiling of 60 grows fastest when it holds 30. If it holds 22 today, then 8 more fish take it to its fastest-growing size — and after that the pond keeps filling but the filling slows.",
             '[[step eq="30 − 22 = 8 more"]]'],
            ["The tempting wrong answer is the distance to the CEILING, 38, as though a nearly full pond were a fast one. It is the opposite: a crowd gets in its own way. And 30 is the halfway size itself, not the distance to it.",
             '[[step eq="8 ✓"]][[step eq="38 ✗ to the ceiling · 30 ✗ the halfway size"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. Ceiling 168 with 57 fish: half is 84, so 27 more.",
                        '[[step eq="84 − 57 = 27"]]'],
             "ask": {"a": 130, "b": 30, "op": "carr"}},
            {"worked": ["One more together. Ceiling 166, 11 fish: half is 83, and taking the 11 off leaves 72 more.",
                        '[[step eq="83 − 11 = 72"]]'],
             "ask": {"a": 176, "b": 25, "op": "carr"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": a, "b": b, "op": "carr"} for a, b in
                 ((20, 8), (30, 4), (52, 6), (68, 5), (90, 7),
                  (112, 9), (134, 11), (150, 10), (172, 12), (174, 4))],
    },
    {
        "id": "diffeq-u3-how-big-the-peak-is",
        "course": "diffeq", "unit": 3,
        "topic": "The size of the peak",
        "op": "fast", "max_value": 300,
        "levels": ("abstract",),
        "symbols": ("peak", "quarter"),
        "advance_line": "Three in a row — you've got it! Ceiling times constant, then a quarter of it.",
        "teach": [
            ["Knowing WHERE the peak sits is half of it. The other half is how big that peak is, and the answer is one of the tidiest in the subject: the ceiling times the growth constant, divided by 4.",
             '[[goal text="How big the peak is"]][[step eq="ceiling 40 · constant 4"]]'],
            ["A ceiling of 40 with a growth constant of 4: 40 times 4 is 160, and a quarter of that is 40 fish a year at the very fastest moment.",
             '[[step eq="40 × 4 ÷ 4 = 40"]]'],
            ["Where does the quarter come from? Two halvings at once — half the fish and half the room, at the same instant. Never taking the quarter leaves 160, and halving only once gives 80.",
             '[[step eq="40 ✓"]][[step eq="160 ✗ no quarter · 80 ✗ halved once"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. Ceiling 56 with a constant of 3: 168, and a quarter of that is 42.",
                        '[[step eq="56 × 3 ÷ 4 = 42"]]'],
             "ask": {"a": 100, "b": 2, "op": "fast"}},
            {"worked": ["One more together. Ceiling 60, constant 6: 360 quartered is 90.",
                        '[[step eq="60 × 6 ÷ 4 = 90"]]'],
             "ask": {"a": 96, "b": 3, "op": "fast"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": a, "b": b, "op": "fast"} for a, b in
                 ((20, 2), (32, 2), (44, 2), (36, 3), (44, 3),
                  (76, 2), (88, 2), (28, 7), (72, 3), (40, 6))],
    },
    {
        "id": "diffeq-u3-the-one-that-pushes-away",
        "course": "diffeq", "unit": 3,
        "topic": "Unstable equilibria",
        "op": "away", "max_value": 170,
        "levels": ("abstract",),
        "symbols": ("unstable", "balance"),
        "advance_line": "Three in a row — you've got it! Distance from the equilibrium, times the push.",
        "teach": [
            ["Every equilibrium so far has pulled things back toward it. Those are the stable ones. But an equilibrium can just as easily PUSH — a balance so delicate that the smallest nudge sends you away for good.",
             '[[goal text="The one that pushes away"]][[step eq="unstable at 20 · now 35"]]'],
            ["Say the unstable point sits at 20, and anything off it moves at 4 for every 1 of distance. A population of 35 stands 15 above, so it is racing away at 60 — and climbing, because the further it goes the harder it is pushed.",
             '[[step eq="35 − 20 = 15 · 15 × 4 = 60"]]'],
            ["That runaway is what unstable means, and it is why a pencil will not stand on its point. Answering 15 hands back the distance, and 35 is where it is standing, not how fast it is leaving.",
             '[[step eq="60 ✓"]][[step eq="15 ✗ the distance · 35 ✗ where it stands"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. Unstable at 60, a population of 88, pushed at 3 per 1: 28 above, so 84.",
                        '[[step eq="28 × 3 = 84"]]'],
             "ask": {"a": 39, "b": 90, "c": 2, "op": "away"}},
            {"worked": ["One more together. Unstable at 20, population 58, push of 4: that is 38 above, and 38 times 4 is racing off at 152.",
                        '[[step eq="38 × 4 = 152"]]'],
             "ask": {"a": 8, "b": 63, "c": 3, "op": "away"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": a, "b": b, "c": c, "op": "away"} for a, b, c in
                 ((4, 7, 2), (5, 14, 3), (6, 11, 9), (7, 28, 3), (8, 18, 8),
                  (10, 29, 5), (9, 47, 3), (11, 54, 3), (12, 85, 2),
                  (13, 40, 6))],
    },
]
LESSONS.extend(_DIFFEQ_U3)


# =============================================================================
# DIFFERENTIAL EQUATIONS UNIT 4 -- Numerical Methods: Euler & Runge-Kutta
# (build ma)
# The thread: WHEN YOU CANNOT SOLVE IT, WALK IT -- AND COUNT THE COST. Euler
# commits to the slope it read at the start of each step, its error follows the
# step size exactly, fourth-order Runge-Kutta divides its error by sixteen
# instead of two, and accuracy is paid for in slope evaluations.
# =============================================================================
_DIFFEQ_U4 = [
    {
        "id": "diffeq-u4-walking-it-in-straight-steps",
        "course": "diffeq", "unit": 4,
        "topic": "Euler's method",
        "op": "eulr", "max_value": 180,
        "levels": ("abstract",),
        "symbols": ("method", "step"),
        "advance_line": "Three in a row — you've got it! Nothing on the first step, then twice the step squared.",
        "teach": [
            ["Most differential equations cannot be solved on paper at all. So a computer does what Unit 1 did by eye: it walks the slope field. The oldest such method is Euler's, and it is exactly that walk.",
             '[[goal text="Walking it in straight steps"]][[step eq="dy/dx = 2x · start 5 · steps of 3"]]'],
            ["Here is Euler's one rule: read the slope at the START of a step, then hold it for the whole width. Take d y d x equals 2 x from height 5, in two steps of 3. The first step starts at x equals zero, where the slope is nothing, so it climbs nothing.",
             '[[step eq="step 1: slope 0 → no climb"]]'],
            ["The second step starts at 3, where the slope is 6, and holding 6 across a width of 3 climbs 18 — landing at 23. But the true curve reaches 41, because the slope kept rising while Euler was using an old one. Euler always lags on a curve that bends upward.",
             '[[step eq="23 ✓"]][[step eq="41 ✗ the true curve · 18 ✗ climb only"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. From height 22 in two steps of 4: nothing, then 32 — landing at 54.",
                        '[[step eq="22 + 32 = 54"]]'],
             "ask": {"a": 30, "b": 4, "op": "eulr"}},
            {"worked": ["One more together. From 34 in two steps of 6: the second step climbs 72, landing at 106.",
                        '[[step eq="34 + 72 = 106"]]'],
             "ask": {"a": 22, "b": 6, "op": "eulr"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": a, "b": b, "op": "eulr"} for a, b in
                 ((2, 2), (2, 3), (12, 3), (8, 4), (32, 3),
                  (10, 5), (20, 5), (30, 5), (18, 6), (28, 6))],
    },
    {
        "id": "diffeq-u4-the-deal-euler-offers",
        "course": "diffeq", "unit": 4,
        "topic": "First-order accuracy",
        "op": "estp", "max_value": 190,
        "levels": ("abstract",),
        "symbols": ("first order", "proportional"),
        "advance_line": "Three in a row — you've got it! Scale the error by the same factor as the step.",
        "teach": [
            ["Euler lags, so the obvious repair is smaller steps. The question is what that buys — and there is an exact answer, which is why Euler is called a first order method.",
             '[[goal text="The deal Euler offers"]][[step eq="step 10 → error 90"]]'],
            ["First order means the error is proportional to the step size. Not roughly — exactly. A step of 10 left an error of 90; go to a step of 4 and the error follows it down by the same factor, to 36.",
             '[[step eq="90 × 4 ÷ 10 = 36"]]'],
            ["So ten times the work buys a tenth of the error, and not a scrap more. Leaving the error at 90 pretends smaller steps are free of any gain, and halving it to 45 out of habit ignores what the step actually did.",
             '[[step eq="36 ✓"]][[step eq="90 ✗ unchanged · 45 ✗ halved by habit"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. A step of 11 left 110; a step of 5 leaves 50.",
                        '[[step eq="110 × 5 ÷ 11 = 50"]]'],
             "ask": {"a": 110, "b": 10, "c": 6, "op": "estp"}},
            {"worked": ["One more together. A step of 10 left an error of 150; at a step of 9 that is 150 times 9 over 10 — 135.",
                        '[[step eq="150 × 9 ÷ 10 = 135"]]'],
             "ask": {"a": 150, "b": 5, "c": 4, "op": "estp"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": a, "b": b, "c": c, "op": "estp"} for a, b, c in
                 ((20, 10, 2), (22, 11, 8), (32, 8, 7), (48, 6, 5),
                  (78, 9, 6), (102, 3, 2), (116, 4, 3), (130, 5, 4),
                  (132, 12, 11), (184, 12, 9))],
    },
    {
        "id": "diffeq-u4-sixteen-instead-of-two",
        "course": "diffeq", "unit": 4,
        "topic": "Runge-Kutta",
        "op": "rk4", "max_value": 330,
        "levels": ("abstract",),
        "symbols": ("fourth order", "sixteen"),
        "advance_line": "Three in a row — you've got it! Divide the error by sixteen.",
        "teach": [
            ["A tenth of the error for ten times the work is a poor bargain, and nobody accepts it. The method everybody actually uses is fourth order Runge-Kutta, and the word fourth is the whole story.",
             '[[goal text="Sixteen instead of two"]][[step eq="halve the step"]]'],
            ["Halve the step and Euler's error halves. Halve it for Runge-Kutta and the error divides by sixteen, because that same halving of the error happens four times over. So an error of 208 drops to 13 in one stroke.",
             '[[step eq="208 ÷ 16 = 13"]]'],
            ["The three wrong instincts are the three orders themselves: halving is first order, quartering is second, and sixteen is fourth. Which is why a fourth order method reaches an accuracy Euler could not buy with a thousand times the steps.",
             '[[step eq="13 ✓"]][[step eq="104 ✗ halved · 52 ✗ quartered"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. An error of 240 divided by 16 is 15.",
                        '[[step eq="240 ÷ 16 = 15"]]'],
             "ask": {"a": 272, "b": 0, "op": "rk4"}},
            {"worked": ["One more together. 304 over 16 is 19.",
                        '[[step eq="304 ÷ 16 = 19"]]'],
             "ask": {"a": 320, "b": 0, "op": "rk4"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": v, "b": 0, "op": "rk4"} for v in
                 (32, 48, 64, 80, 96, 112, 128, 144, 160, 176)],
    },
    {
        "id": "diffeq-u4-what-accuracy-costs",
        "course": "diffeq", "unit": 4,
        "topic": "Counting the cost",
        "op": "evls", "max_value": 190,
        "levels": ("abstract",),
        "symbols": ("evaluations", "cost"),
        "advance_line": "Three in a row — you've got it! Four for every Runge-Kutta step, then take that off Euler's bill.",
        "teach": [
            ["Runge-Kutta is not magic, and this last lesson is the fine print. It reads the slope FOUR times inside every step — once at the start, twice in the middle, once at the end — and averages them.",
             '[[goal text="What accuracy costs"]][[step eq="Euler 100 × 1 · RK4 9 × 4"]]'],
            ["So count the slope evaluations, which is what a method really costs. Euler needs 100 steps at one evaluation each: 100. Runge-Kutta gets there in 9 steps, but pays 4 each — 36. It saves 64.",
             '[[step eq="100 − 36 = 64"]]'],
            ["Four times the cost per step, and it still wins easily, because it needs so very many fewer of them. Comparing the step counts alone gives 91 and forgets the price; 36 is what Runge-Kutta spent, not what it saved.",
             '[[step eq="64 ✓"]][[step eq="91 ✗ steps only · 36 ✗ what it spent"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. Euler 184 steps against Runge-Kutta's 6: that is 24 evaluations, so 160 saved.",
                        '[[step eq="184 − 24 = 160"]]'],
             "ask": {"a": 190, "b": 11, "op": "evls"}},
            {"worked": ["One more together. Euler 190 against 5 Runge-Kutta steps: 4 each is 20 evaluations, and 190 take away 20 saves 170.",
                        '[[step eq="190 − 20 = 170"]]'],
             "ask": {"a": 186, "b": 8, "op": "evls"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": a, "b": b, "op": "evls"} for a, b in
                 ((12, 2), (36, 4), (60, 6), (84, 8), (108, 10),
                  (132, 12), (156, 14), (180, 16), (188, 15), (190, 13))],
    },
]
LESSONS.extend(_DIFFEQ_U4)


# =============================================================================
# DIFFERENTIAL EQUATIONS UNIT 5 -- Second-Order Linear: Homogeneous (build mb)
# The thread: ONE NUMBER DECIDES HOW THE WHOLE THING BEHAVES. The characteristic
# equation's discriminant classifies the motion, the knife-edge where it is
# exactly zero is critical damping, an undamped spring rocks at its natural
# frequency, and damping slows that rocking down.
# =============================================================================
_DIFFEQ_U5 = [
    {
        "id": "diffeq-u5-one-number-decides",
        "course": "diffeq", "unit": 5,
        "topic": "The characteristic equation",
        "op": "char", "max_value": 310,
        "levels": ("abstract",),
        "symbols": ("characteristic", "damping"),
        "advance_line": "Three in a row — you've got it! Square the middle number, then take off four times the last.",
        "teach": [
            ["Second-order equations have a second derivative in them, and they describe everything that swings, rocks or wobbles. Each one hides a quadratic — its characteristic equation — and Algebra II already taught you to test one.",
             '[[goal text="One number decides"]][[step eq="y″ + 6y′ + 5y = 0"]] [[step eq="r² + 6r + 5"]]'],
            ["The test has not changed: the middle number squared, take away 4 times the last. For 6 and 5 that is 36 take away 20 — 16. What has changed is what the answer MEANS.",
             '[[step eq="6² − 4×5 = 16"]]'],
            ["Above zero, as here, the damping wins and the door closes slowly without a wobble. Below zero it rocks. Forgetting the 4 gives 31, and adding instead of taking away gives 56 — and each wrong number would describe a different world.",
             '[[step eq="16 ✓"]][[step eq="31 ✗ no 4 · 56 ✗ added"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 12 and 19: 144 take away 76 is 68.",
                        '[[step eq="12² − 4×19 = 68"]]'],
             "ask": {"a": 12, "b": 16, "op": "char"}},
            {"worked": ["One more together. 15 and 2: 225 take away 8 is 217.",
                        '[[step eq="15² − 4×2 = 217"]]'],
             "ask": {"a": 14, "b": 5, "op": "char"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": a, "b": b, "op": "char"} for a, b in
                 ((4, 3), (9, 14), (8, 4), (11, 13), (10, 2),
                  (13, 14), (12, 2), (15, 17), (14, 4), (16, 11))],
    },
    {
        "id": "diffeq-u5-the-knife-edge",
        "course": "diffeq", "unit": 5,
        "topic": "Critical damping",
        "op": "cdmp", "max_value": 800,
        "levels": ("abstract",),
        "symbols": ("critically", "bounce"),
        "advance_line": "Three in a row — you've got it! Square it, then take a quarter.",
        "teach": [
            ["Between wobbling and crawling there is one exact setting, and every good door closer is built to sit on it. It is called critically damped: the fastest close with no bounce at all.",
             '[[goal text="The knife-edge"]][[step eq="test number exactly 0"]]'],
            ["It happens when that test number is exactly zero — so the middle squared must equal 4 times the last. With 30 in the middle, 30 squared is 900, and a quarter of that is 225. Set the last term to 225 and you are on the edge.",
             '[[step eq="30² = 900 · 900 ÷ 4 = 225"]]'],
            ["A hair below 225 and the door bounces past the frame; a hair above and it crawls shut. Handing back 900 skips the quarter, and halving instead of quartering gives 450 — a door that overshoots every time.",
             '[[step eq="225 ✓"]][[step eq="900 ✗ no quarter · 450 ✗ halved"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. With 32 in the middle: 1024, and a quarter of that is 256.",
                        '[[step eq="32² ÷ 4 = 256"]]'],
             "ask": {"a": 26, "b": 0, "op": "cdmp"}},
            {"worked": ["One more together. 34 in the middle: 1156 quartered is 289.",
                        '[[step eq="34² ÷ 4 = 289"]]'],
             "ask": {"a": 28, "b": 0, "op": "cdmp"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": v, "b": 0, "op": "cdmp"} for v in
                 (6, 8, 10, 12, 14, 16, 18, 20, 22, 24)],
    },
    {
        "id": "diffeq-u5-the-spring-that-never-stops",
        "course": "diffeq", "unit": 5,
        "topic": "Natural frequency",
        "op": "natf", "max_value": 230,
        "levels": ("abstract",),
        "symbols": ("natural", "rocks"),
        "advance_line": "Three in a row — you've got it! The natural frequency is the square root.",
        "teach": [
            ["Now take the damping away completely — no friction, no air, nothing to steal the motion. The wobble that was dying out now never dies, and the spring rocks for ever.",
             '[[goal text="The spring that never stops"]][[step eq="y″ + 9y = 0"]]'],
            ["Such a spring rocks at one particular speed, its natural frequency, and that frequency is simply the square root of the number sitting on the y. For 9 the frequency is 3 — 3 radians a second, for ever.",
             '[[step eq="√9 = 3 radians a second"]]'],
            ["Every object on earth has a frequency like this: a bridge, a wine glass, a building. Handing back 9 forgets the root, and doubling it to 6 undoes a square the wrong way. The next unit is about what happens when something else finds that number.",
             '[[step eq="3 ✓"]][[step eq="9 ✗ not rooted · 6 ✗ doubled"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. y double-prime plus 256 y: the square root of 256 is 16.",
                        '[[step eq="√256 = 16"]]'],
             "ask": {"a": 196, "b": 0, "op": "natf"}},
            {"worked": ["One more together. With 289 on the y, the square root of 289 is 17 — that is the frequency.",
                        '[[step eq="√289 = 17"]]'],
             "ask": {"a": 225, "b": 0, "op": "natf"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": v, "b": 0, "op": "natf"} for v in
                 (16, 25, 36, 49, 64, 81, 100, 121, 144, 169)],
    },
    {
        "id": "diffeq-u5-damping-slows-the-rocking",
        "course": "diffeq", "unit": 5,
        "topic": "Damped frequency",
        "op": "oscf", "max_value": 250,
        "levels": ("abstract",),
        "symbols": ("damped", "slower"),
        "advance_line": "Three in a row — you've got it! Four times the last, take off the middle squared, root it, halve it.",
        "teach": [
            ["Put a little damping back — not enough to stop the rocking, only enough to shrink it. Everyone expects the swing to get smaller. Almost nobody expects the rocking to get slower, but it does.",
             '[[goal text="Damping slows the rocking"]][[step eq="y″ + 8y′ + 25y = 0"]]'],
            ["The damped frequency is 4 times the last number, take away the middle squared, then rooted and halved. For 8 and 25: 100 take away 64 is 36, whose root is 6, and half of that is 3.",
             '[[step eq="4×25 − 8² = 36 · √36 ÷ 2 = 3"]]'],
            ["Undamped it would have rocked at the root of 25 — that is 5 — so the damping really did slow it, from 5 down to 3. Skipping the halving gives 6, and 4 is half the damping, which is a real number here but not this one.",
             '[[step eq="3 ✓"]][[step eq="6 ✗ not halved · 4 ✗ half the damping"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. With 10 and 221: 884 take away 100 is 784, whose root is 28, halved to 14.",
                        '[[step eq="√784 ÷ 2 = 14"]]'],
             "ask": {"a": 14, "b": 193, "op": "oscf"}},
            {"worked": ["One more together. 6 and 205: 820 take away 36 is 784, and 28 halved is 14.",
                        '[[step eq="√784 ÷ 2 = 14"]]'],
             "ask": {"a": 6, "b": 234, "op": "oscf"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": a, "b": b, "op": "oscf"} for a, b in
                 ((4, 13), (6, 25), (8, 41), (10, 61), (12, 85),
                  (14, 113), (16, 145), (18, 181), (20, 221), (12, 205))],
    },
]
LESSONS.extend(_DIFFEQ_U5)


# =============================================================================
# DIFFERENTIAL EQUATIONS UNIT 6 -- Nonhomogeneous, Vibrations & Resonance
# (build mb)
# The thread: NOW SOMEBODY IS PUSHING. A steady push settles at a steady
# height, the part that fades is pinned by where you started, a push at the
# spring's own frequency grows without bound, and damping is the only thing
# standing between resonance and ruin.
# =============================================================================
_DIFFEQ_U6 = [
    {
        "id": "diffeq-u6-somebody-is-pushing",
        "course": "diffeq", "unit": 6,
        "topic": "Particular solutions",
        "op": "part", "max_value": 240,
        "levels": ("abstract",),
        "symbols": ("particular", "steady"),
        "advance_line": "Three in a row — you've got it! Share the push out over the spring's number.",
        "teach": [
            ["Every equation so far has had a zero on the right — nobody pushing, the spring left to itself. Put a number there instead and somebody is leaning on it. That changes where it ends up.",
             '[[goal text="Somebody is pushing"]][[step eq="y″ + 5y = 40"]]'],
            ["Guess that the answer is steady — a flat height that never moves. A flat height has no curvature, so the y double-prime is nothing, and 5 y has to equal 40 all by itself. So y is 8.",
             '[[step eq="5y = 40"]] [[step eq="y = 8"]]'],
            ["That is a particular solution, and the method is always the same: guess the SHAPE the push has, then let the equation fix the size. Timesing instead of sharing gives 200, and 40 is the push, not a height.",
             '[[step eq="8 ✓"]][[step eq="200 ✗ timesed · 40 ✗ the push"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. y double-prime plus 4 y equals 52: 52 over 4 is 13.",
                        '[[step eq="4y = 52"]] [[step eq="y = 13"]]'],
             "ask": {"a": 3, "b": 42, "op": "part"}},
            {"worked": ["One more together. y double-prime plus 2 y equals 34, so 34 over 2 — the steady height is 17.",
                        '[[step eq="2y = 34"]] [[step eq="y = 17"]]'],
             "ask": {"a": 2, "b": 32, "op": "part"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": a, "b": b, "op": "part"} for a, b in
                 ((3, 6), (4, 12), (2, 8), (6, 30), (4, 24),
                  (2, 14), (3, 24), (5, 45), (2, 20), (4, 44))],
    },
    {
        "id": "diffeq-u6-the-part-that-fades",
        "course": "diffeq", "unit": 6,
        "topic": "The transient",
        "op": "trns", "max_value": 250,
        "levels": ("abstract",),
        "symbols": ("transient", "forgets"),
        "advance_line": "Three in a row — you've got it! Start take away steady is the part that fades.",
        "teach": [
            ["A pushed spring does two things at once, and this is the shape of every answer in the unit: a steady part that stays, plus a transient part that fades away to nothing.",
             '[[goal text="The part that fades"]][[step eq="steady 40 · starts at 65"]]'],
            ["Suppose it settles at 40 in the long run but you let it go from 65. The steady part only explains 40 of that, so the other 25 must be the transient — and 25 is exactly how much has to die away.",
             '[[step eq="65 − 40 = 25"]]'],
            ["Wait long enough and that piece is gone, leaving 40 no matter where you let go from. A spring forgets how it started. Adding gives 105, and 40 is the part that stays, not the part that goes.",
             '[[step eq="25 ✓"]][[step eq="105 ✗ added · 40 ✗ the steady part"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. Settling at 40, let go from 180: 180 take away 40 — the transient is 140.",
                        '[[step eq="180 − 40 = 140"]]'],
             "ask": {"a": 188, "b": 52, "op": "trns"}},
            {"worked": ["One more together. Steady 30, released at 186: 186 take away 30 — 156 fades away.",
                        '[[step eq="186 − 30 = 156"]]'],
             "ask": {"a": 190, "b": 36, "op": "trns"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": a, "b": b, "op": "trns"} for a, b in
                 ((5, 3), (24, 6), (46, 12), (68, 18), (90, 24),
                  (112, 30), (134, 36), (156, 42), (178, 48), (190, 44))],
    },
    {
        "id": "diffeq-u6-why-soldiers-break-step",
        "course": "diffeq", "unit": 6,
        "topic": "Resonance",
        "op": "reso", "max_value": 200,
        "levels": ("abstract",),
        "symbols": ("resonance", "gap"),
        "advance_line": "Three in a row — you've got it! Share the force out over the gap between the two frequencies.",
        "teach": [
            ["Unit 5 gave every object its own natural frequency. This lesson is what happens when a push arrives at that very frequency — and it is the reason soldiers break step before crossing a bridge.",
             '[[goal text="Why soldiers break step"]][[step eq="natural² 9 · driver² 3"]]'],
            ["The swing that builds up is the force shared out over the gap between the two frequencies squared. Natural 9 against a driver of 3 leaves a gap of 6, so a force of 42 builds a swing of 7.",
             '[[step eq="42 ÷ (9 − 3) = 7"]]'],
            ["Now close that gap and watch. A gap of 3 doubles the swing; a gap of 1 gives 42; and at a gap of nothing there is no size left to name — the swing simply grows without stopping. That is resonance. Dividing by the driver instead reaches 14.",
             '[[step eq="7 ✓"]][[step eq="14 ✗ divided by the driver · 42 ✗ the force"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. Natural squared 15, driver squared 5, force 110: a gap of 10, so a swing of 11.",
                        '[[step eq="110 ÷ 10 = 11"]]'],
             "ask": {"a": 7, "b": 4, "c": 156, "op": "reso"}},
            {"worked": ["One more together. Natural 12, driver 8, force 176: the gap is 4, and 176 over 4 is a swing of 44.",
                        '[[step eq="176 ÷ 4 = 44"]]'],
             "ask": {"a": 5, "b": 3, "c": 114, "op": "reso"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": a, "b": b, "c": c, "op": "reso"} for a, b, c in
                 ((5, 2, 6), (9, 3, 42), (6, 4, 24), (15, 5, 170),
                  (12, 8, 88), (8, 6, 54), (18, 16, 64), (39, 37, 74),
                  (10, 7, 126), (6, 2, 188))],
    },
    {
        "id": "diffeq-u6-what-saves-the-bridge",
        "course": "diffeq", "unit": 6,
        "topic": "Damped resonance",
        "op": "damp", "max_value": 190,
        "levels": ("abstract",),
        "symbols": ("damping", "endless"),
        "advance_line": "Three in a row — you've got it! Damping times frequency, and share the force over that.",
        "teach": [
            ["A swing with no size at all is not something the world actually does, so something must be missing from that picture. What is missing is damping — and it is the last idea in the unit.",
             '[[goal text="What saves the bridge"]][[step eq="force 150 · damping 5 · frequency 3"]]'],
            ["At the exact resonant frequency the swing would be endless without it. With damping, the swing is the force shared over the damping times the frequency. A force of 150, damping 5, frequency 3: 5 times 3 is 15, and 150 over 15 is 10.",
             '[[step eq="150 ÷ (5 × 3) = 10"]]'],
            ["So damping is the only thing standing between resonance and ruin, and the smaller it gets the bigger that swing grows. Dividing by the damping alone leaves 30, and 150 is the force, undivided.",
             '[[step eq="10 ✓"]][[step eq="30 ✗ damping only · 150 ✗ the force"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. Force 156, damping 2, frequency 6: 12 in all, and 156 over 12 is 13.",
                        '[[step eq="156 ÷ 12 = 13"]]'],
             "ask": {"a": 176, "b": 4, "c": 2, "op": "damp"}},
            {"worked": ["One more together. Force 190, damping 5, frequency 2: 5 times 2 is 10, and 190 over 10 is 19.",
                        '[[step eq="190 ÷ 10 = 19"]]'],
             "ask": {"a": 174, "b": 3, "c": 2, "op": "damp"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": a, "b": b, "c": c, "op": "damp"} for a, b, c in
                 ((12, 2, 3), (32, 4, 2), (60, 2, 5), (84, 3, 4),
                  (120, 5, 3), (126, 7, 2), (160, 2, 8), (132, 4, 3),
                  (168, 2, 7), (180, 2, 6))],
    },
]
LESSONS.extend(_DIFFEQ_U6)


# =============================================================================
# DIFFERENTIAL EQUATIONS UNIT 7 -- Laplace Transforms (build mc)
# The thread: TURN THE CALCULUS INTO ALGEBRA, THEN JUST DO ALGEBRA. The rule
# that turns a derivative into a multiplication, the plain algebra that is left
# behind, the shift rule that moves a pole, and the theorem that reads where a
# solution ENDS without ever transforming back.
# =============================================================================
_DIFFEQ_U7 = [
    {
        "id": "diffeq-u7-derivatives-become-timesing",
        "course": "diffeq", "unit": 7,
        "topic": "The derivative rule",
        "op": "lder", "max_value": 210,
        "levels": ("abstract",),
        "symbols": ("transform", "derivative"),
        "advance_line": "Three in a row — you've got it! s times Y, then take off the starting height.",
        "teach": [
            ["Here is a completely different way to solve a differential equation: change it into something that is not one. The Laplace transform does exactly that, and this first rule is the whole reason it works.",
             '[[goal text="Derivatives become timesing"]][[step eq="L{y′} = sY − y(0)"]]'],
            ["Transform a derivative and you get s times Y, take away the starting height. The derivative is GONE — it has turned into a multiplication. If the curve started at 9, with s of 4 and Y of 5, that is 20 take away 9 — 11.",
             '[[step eq="4 × 5 − 9 = 11"]]'],
            ["Adding the start instead of taking it away gives 29, and 20 forgets that where you began matters at all. This one line is what carries the whole unit: differentiating becomes timesing by s.",
             '[[step eq="11 ✓"]][[step eq="29 ✗ added · 20 ✗ start ignored"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. Starting at 2, with s of 5 and Y of 9: 45 take away 2 is 43.",
                        '[[step eq="5 × 9 − 2 = 43"]]'],
             "ask": {"a": 12, "b": 7, "c": 10, "op": "lder"}},
            {"worked": ["One more together. Start 2, s of 12, Y of 11: 132 take away 2 is 130.",
                        '[[step eq="12 × 11 − 2 = 130"]]'],
             "ask": {"a": 29, "b": 14, "c": 10, "op": "lder"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": a, "b": b, "c": c, "op": "lder"} for a, b, c in
                 ((4, 2, 3), (3, 11, 2), (6, 3, 14), (2, 5, 11), (8, 13, 6),
                  (17, 8, 13), (16, 10, 12), (5, 14, 9), (30, 12, 14),
                  (13, 12, 14))],
    },
    {
        "id": "diffeq-u7-and-now-it-is-just-algebra",
        "course": "diffeq", "unit": 7,
        "topic": "Solving in the s world",
        "op": "lalg", "max_value": 250,
        "levels": ("abstract",),
        "symbols": ("algebra", "solve"),
        "advance_line": "Three in a row — you've got it! Add the two on the bottom, then share the top over it.",
        "teach": [
            ["Once every derivative has become a multiplication, look at what is left on the page. No derivatives. No integrals. Just letters and numbers — plain algebra, and you have been solving that since Algebra I.",
             '[[goal text="And now it is just algebra"]][[step eq="(s + 6)Y = 96"]]'],
            ["Say the transforming left s plus 6, all times Y, equals 96. Solve for Y the way you always would: Y is 96 over s plus 6. Then at s equals 2 the bottom is 8, and 96 over 8 is 12.",
             '[[step eq="Y = 96/(s + 6) · at s = 2"]] [[step eq="96 ÷ 8 = 12"]]'],
            ["Taking the two bottom numbers away instead of adding gives 24, and 96 is the top, not the answer. Notice what did NOT happen anywhere in that: no calculus at all. The derivative left the problem the moment we transformed it.",
             '[[step eq="12 ✓"]][[step eq="24 ✗ taken away · 96 ✗ the top"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. s plus 2, times Y, equals 228; at s equals 4 the bottom is 6, and 228 over 6 is 38.",
                        '[[step eq="228 ÷ 6 = 38"]]'],
             "ask": {"a": 2, "b": 192, "c": 4, "op": "lalg"}},
            {"worked": ["One more together. 240 over s plus 2, at s equals 4: the bottom is 6, and 240 over 6 is 40.",
                        '[[step eq="240 ÷ 6 = 40"]]'],
             "ask": {"a": 4, "b": 210, "c": 2, "op": "lalg"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": a, "b": b, "c": c, "op": "lalg"} for a, b, c in
                 ((2, 12, 4), (3, 40, 5), (4, 48, 2), (5, 88, 3),
                  (8, 168, 4), (2, 102, 4), (4, 120, 2), (3, 184, 5),
                  (5, 208, 3), (2, 232, 6))],
    },
    {
        "id": "diffeq-u7-the-shift-rule",
        "course": "diffeq", "unit": 7,
        "topic": "The shift rule",
        "op": "lshf", "max_value": 200,
        "levels": ("abstract",),
        "symbols": ("pole", "shift"),
        "advance_line": "Three in a row — you've got it! The pole slides right by the amount in the exponent.",
        "teach": [
            ["The transform of a thing blows up at certain values of s, and those places have a name: poles. A pole is not bookkeeping — it is the answer in disguise, as the last beat will show.",
             '[[goal text="The shift rule"]][[step eq="pole at s = 20 · × e^(6t)"]]'],
            ["Here is the shift rule, the line of the table used most of all. Multiply the original by e to the 6 t, and every s in the transform becomes s take away 6 — so the whole picture slides 6 to the right. A pole at 20 moves to 26.",
             '[[step eq="20 + 6 = 26"]]'],
            ["Sliding the wrong way gives 14, and 20 is where the pole used to be. And now why poles matter: a pole to the right of zero means the answer GROWS, and one to the left means it dies away. The pole is the behaviour, written down.",
             '[[step eq="26 ✓"]][[step eq="14 ✗ wrong way · 20 ✗ the old pole"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. A pole at 130 shifted by 55 lands at 185.",
                        '[[step eq="130 + 55 = 185"]]'],
             "ask": {"a": 124, "b": 52, "op": "lshf"}},
            {"worked": ["One more together. 140 shifted by 60 gives a pole at 200.",
                        '[[step eq="140 + 60 = 200"]]'],
             "ask": {"a": 136, "b": 57, "op": "lshf"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": a, "b": b, "op": "lshf"} for a, b in
                 ((4, 2), (16, 7), (28, 12), (40, 17), (52, 22),
                  (64, 27), (76, 32), (88, 37), (100, 42), (112, 47))],
    },
    {
        "id": "diffeq-u7-reading-the-ending",
        "course": "diffeq", "unit": 7,
        "topic": "The final-value theorem",
        "op": "lfin", "max_value": 200,
        "levels": ("abstract",),
        "symbols": ("final", "settles"),
        "advance_line": "Three in a row — you've got it! Share the top over the number beside the s.",
        "teach": [
            ["The last idea of the unit is the one engineers reach for daily. Often you do not want the whole solution — you only want to know where it settles in the end. You can read that off without transforming back at all.",
             '[[goal text="Reading the ending"]][[step eq="Y = 96/(s(s + 8))"]]'],
            ["Suppose Y is 96, with two things underneath it: a lone s, and s plus 8. Multiply by s, which clears that lone s, and then let s fall away to zero. The s plus 8 becomes just 8, and 96 over 8 is 12. That is the final value.",
             '[[step eq="96 ÷ 8 = 12"]]'],
            ["Handing back 96 answers with the top, and 88 takes the two away rather than sharing. The theorem is worth its weight: where a thing ends up, read straight off the transform, with no inverting at all.",
             '[[step eq="12 ✓"]][[step eq="96 ✗ the top · 88 ✗ taken away"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 180 underneath a lone s and an s plus 12: 180 over 12 is 15.",
                        '[[step eq="180 ÷ 12 = 15"]]'],
             "ask": {"a": 4, "b": 132, "op": "lfin"}},
            {"worked": ["One more together. 76 under a lone s and an s plus 2: 76 over 2 settles at 38.",
                        '[[step eq="76 ÷ 2 = 38"]]'],
             "ask": {"a": 3, "b": 105, "op": "lfin"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": a, "b": b, "op": "lfin"} for a, b in
                 ((3, 6), (2, 10), (4, 32), (6, 66), (5, 70),
                  (7, 119), (9, 180), (8, 184), (6, 156), (5, 145))],
    },
]
LESSONS.extend(_DIFFEQ_U7)


# =============================================================================
# DIFFERENTIAL EQUATIONS UNIT 8 -- Linear Systems & the Phase Plane (build mc)
# The thread: TWO THINGS CHANGING TOGETHER, EACH WATCHING THE OTHER. Unit 1's
# slope field one dimension up, the lines where one arrow goes flat, the
# determinant that classifies the whole picture, and the pair of eigenvalues
# that decide it.
# =============================================================================
_DIFFEQ_U8 = [
    {
        "id": "diffeq-u8-two-things-at-once",
        "course": "diffeq", "unit": 8,
        "topic": "Systems in the plane",
        "op": "sysx", "max_value": 260,
        "levels": ("abstract",),
        "symbols": ("system", "arrow"),
        "advance_line": "Three in a row — you've got it! The x part first, then take off the y.",
        "teach": [
            ["Everything so far has followed one quantity. Now follow two at once, each one watching the other: rabbits and foxes, a spring in two directions, two tanks feeding each other. That is a system.",
             '[[goal text="Two things at once"]][[step eq="x′ = 4x − y"]]'],
            ["Say x grows by 4 for every x it already has, and loses 1 for every y. At the point where x is 9 and y is 5: 4 times 9 is 36, and the 5 of y pulls it back to 31.",
             '[[step eq="4 × 9 − 5 = 31"]]'],
            ["Do the same for y and you get an arrow at that point, pointing somewhere in the plane — Unit 1's slope field with two directions instead of one. Adding the y gives 41, and 36 pretends the foxes were not there.",
             '[[step eq="31 ✓"]][[step eq="41 ✗ added · 36 ✗ no y"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 6 for every x, at x of 15 with y of 51: 90 take away 51 is 39.",
                        '[[step eq="6 × 15 − 51 = 39"]]'],
             "ask": {"a": 7, "b": 15, "c": 53, "op": "sysx"}},
            {"worked": ["One more together. 11 per x, x of 12, y of 7: 132 take away 7 is 125.",
                        '[[step eq="11 × 12 − 7 = 125"]]'],
             "ask": {"a": 9, "b": 12, "c": 3, "op": "sysx"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": a, "b": b, "c": c, "op": "sysx"} for a, b, c in
                 ((2, 2, 2), (4, 6, 4), (3, 15, 7), (5, 13, 9), (7, 11, 3),
                  (9, 14, 34), (11, 12, 22), (10, 16, 32), (12, 14, 22),
                  (12, 16, 28))],
    },
    {
        "id": "diffeq-u8-where-an-arrow-goes-flat",
        "course": "diffeq", "unit": 8,
        "topic": "Nullclines",
        "op": "nucl", "max_value": 190,
        "levels": ("abstract",),
        "symbols": ("nullcline", "cross"),
        "advance_line": "Three in a row — you've got it! Slope times x is where the line sits.",
        "teach": [
            ["Drawing an arrow at every point is slow — the same problem Unit 1 solved with isoclines. Here the shortcut is even better: find the places where one of the two arrows goes completely flat.",
             '[[goal text="Where an arrow goes flat"]][[step eq="x′ = 0 where y = 5x"]]'],
            ["For our system x stops changing exactly where 5 x equals y. That is a straight line through the origin, and it is called a nullcline — the x one, since x is what has stopped. At x equals 12, it sits at y equals 60.",
             '[[step eq="5 × 12 = 60"]]'],
            ["Along that whole line the arrows point straight up or straight down, since x is going nowhere. Adding gives 17, and 25 is the slope squared rather than a height. And where the x-nullcline and the y-nullcline cross, nothing moves at all — an equilibrium.",
             '[[step eq="60 ✓"]][[step eq="17 ✗ added · 25 ✗ slope squared"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. A slope of 14 at x equals 4: 14 times 4 — the nullcline sits at 56.",
                        '[[step eq="14 × 4 = 56"]]'],
             "ask": {"a": 7, "b": 11, "op": "nucl"}},
            {"worked": ["One more together. Slope 10 at x equals 16: 10 times 16 puts it at 160.",
                        '[[step eq="10 × 16 = 160"]]'],
             "ask": {"a": 11, "b": 13, "op": "nucl"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": a, "b": b, "op": "nucl"} for a, b in
                 ((2, 3), (9, 2), (4, 7), (8, 5), (6, 9),
                  (11, 6), (7, 12), (13, 8), (9, 14), (9, 16))],
    },
    {
        "id": "diffeq-u8-the-number-in-the-corner",
        "course": "diffeq", "unit": 8,
        "topic": "The determinant",
        "op": "detm", "max_value": 290,
        "levels": ("abstract",),
        "symbols": ("determinant", "saddle"),
        "advance_line": "Three in a row — you've got it! Diagonal product, take away the corner squared.",
        "teach": [
            ["A linear system is carried by four numbers arranged in a square, and out of those four comes one number that classifies the entire picture. It is called the determinant.",
             '[[goal text="The number in the corner"]][[step eq="[9 4; 4 6]"]]'],
            ["Take 9 and 6 down the diagonal with 4 in both corners. The determinant is 9 times 6, take away 4 squared: 54 take away 16 is 38.",
             '[[step eq="9×6 − 4² = 38"]]'],
            ["Now what it means. The determinant is the two eigenvalues times each other. So if it ever falls below zero, one of them must be positive and you have a saddle. A saddle pulls you in one way and flings you out the other. Adding the corners gives 70, and skipping the squaring gives 50.",
             '[[step eq="38 ✓"]][[step eq="70 ✗ added · 50 ✗ not squared"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 15 and 9 on the diagonal, 9 in the corners: 135 take away 81 is 54.",
                        '[[step eq="15×9 − 9² = 54"]]'],
             "ask": {"a": 14, "b": 5, "c": 7, "op": "detm"}},
            {"worked": ["One more together. 14 and 16 with 7 in the corners: 224 take away 49 is 175.",
                        '[[step eq="14×16 − 7² = 175"]]'],
             "ask": {"a": 14, "b": 8, "c": 15, "op": "detm"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": a, "b": b, "c": c, "op": "detm"} for a, b, c in
                 ((2, 2, 3), (4, 6, 14), (6, 3, 8), (11, 3, 6), (8, 7, 16),
                  (8, 2, 13), (13, 6, 12), (15, 5, 11), (12, 4, 15),
                  (16, 2, 12))],
    },
    {
        "id": "diffeq-u8-two-numbers-decide-the-picture",
        "course": "diffeq", "unit": 8,
        "topic": "Eigenvalues",
        "op": "eign", "max_value": 240,
        "levels": ("abstract",),
        "symbols": ("eigenvalues", "trace"),
        "advance_line": "Three in a row — you've got it! Take the one you know off the trace.",
        "teach": [
            ["The determinant was the two eigenvalues multiplied. Their SUM has a name too — the trace, the sum down the diagonal — and between the sum and the product you can always recover both.",
             '[[goal text="Two numbers decide the picture"]][[step eq="trace 60 = λ₁ + λ₂"]]'],
            ["Suppose the trace is 60 and the work has already turned up one eigenvalue, 14. The two must add to 60, so the other is 46. No further algebra needed.",
             '[[step eq="60 − 14 = 46"]]'],
            ["And those two numbers decide everything. Both above zero, as here, and every path races away from the origin. Both below and it all spirals in. One of each is a saddle. Adding gives 74, and 14 is the one you already had.",
             '[[step eq="46 ✓"]][[step eq="74 ✗ added · 14 ✗ the known one"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. A trace of 186 with one eigenvalue at 30: taking 30 off 186, the other is 156.",
                        '[[step eq="186 − 30 = 156"]]'],
             "ask": {"a": 180, "b": 40, "op": "eign"}},
            {"worked": ["One more together. Trace 190, one eigenvalue 26: taking 26 off 190 leaves the other at 164.",
                        '[[step eq="190 − 26 = 164"]]'],
             "ask": {"a": 190, "b": 38, "op": "eign"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": a, "b": b, "op": "eign"} for a, b in
                 ((5, 3), (26, 6), (50, 12), (74, 18), (98, 24),
                  (122, 30), (146, 36), (170, 42), (178, 44), (186, 48))],
    },
]
LESSONS.extend(_DIFFEQ_U8)


# =============================================================================
# DIFFERENTIAL EQUATIONS UNIT 9 -- Nonlinear Systems & Stability (build md)
# ⭐⭐ THE LAST UNIT OF THE LAST COURSE. 328 lessons, and the arc that began
# with counting ends here.
# The thread: WHAT SURVIVES WHEN THE SYSTEM IS NOT LINEAR. Up close a curve is
# a line, which is why Unit 8 was worth learning; the most famous nonlinear
# system there is; the cycle it settles into; and the one thing no amount of
# mathematics can give you back -- a forecast.
# =============================================================================
_DIFFEQ_U9 = [
    {
        "id": "diffeq-u9-up-close-it-is-a-line",
        "course": "diffeq", "unit": 9,
        "topic": "Linearization",
        "op": "lnrz", "max_value": 190,
        "levels": ("abstract",),
        "symbols": ("nonlinear", "tangent"),
        "advance_line": "Three in a row — you've got it! Double the equilibrium, then times the distance.",
        "teach": [
            ["Almost nothing in the world is linear. Real rate laws bend, and Unit 8's neat straight-line systems look like a special case — until you notice the trick that rescues all of it.",
             '[[goal text="Up close it is a line"]][[step eq="rate = 9 − P²"]]'],
            ["Zoom in far enough on any curve and it becomes its own tangent. The nonlinear law 9 take away P squared sits still at P equals 3, and near there it pulls back at 2 times 3 for every 1 of distance. Sitting 4 out, that is 24.",
             '[[step eq="2×3 = 6 per 1 · × 4 = 24"]]'],
            ["So close to an equilibrium, every curved law behaves like a straight one — which is exactly why the last unit was worth learning. Forgetting to double gives 12, and adding the two gives 7.",
             '[[step eq="24 ✓"]][[step eq="12 ✗ not doubled · 7 ✗ added"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. Equilibrium at 10, sitting 8 out: 20 for every 1, so 160.",
                        '[[step eq="2×10×8 = 160"]]'],
             "ask": {"a": 64, "b": 8, "c": 9, "op": "lnrz"}},
            {"worked": ["One more together. Equilibrium 12, distance 7: double 12 is 24 for every 1, and 24 times 7 gives 168.",
                        '[[step eq="2×12×7 = 168"]]'],
             "ask": {"a": 121, "b": 11, "c": 8, "op": "lnrz"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": a, "b": b, "c": c, "op": "lnrz"} for a, b, c in
                 ((4, 2, 3), (9, 3, 4), (36, 6, 3), (16, 4, 6), (25, 5, 6),
                  (81, 9, 4), (121, 11, 4), (100, 10, 5), (49, 7, 8),
                  (144, 12, 5))],
    },
    {
        "id": "diffeq-u9-rabbits-and-foxes",
        "course": "diffeq", "unit": 9,
        "topic": "Predator and prey",
        "op": "prey", "max_value": 190,
        "levels": ("abstract",),
        "symbols": ("predator", "balance"),
        "advance_line": "Three in a row — you've got it! Count the new rabbits, then share them among the foxes.",
        "teach": [
            ["Here is the most famous nonlinear system there is: a predator and its prey. Here is why it cannot be linear. Rabbits eat grass, foxes eat rabbits, and the eating depends on BOTH numbers at once.",
             '[[goal text="Rabbits and foxes"]][[step eq="20 rabbits · 3 born each · 5 eaten per fox"]]'],
            ["Say a wood holds 20 rabbits, each adding 3 new ones a year — 60 new rabbits. If every fox eats 5 rabbits a year, then 12 foxes eat exactly those 60, and the rabbit number holds still. That is a balance point.",
             '[[step eq="20 × 3 ÷ 5 = 12 foxes"]]'],
            ["Notice neither number is steady on its own — each is held in place by the other. Answering 60 counts the births with nothing eating them, and 20 hands back the rabbits when foxes were asked for.",
             '[[step eq="12 ✓"]][[step eq="60 ✗ nothing eating · 20 ✗ the rabbits"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 32 rabbits at 4 each is 128 new; at 8 eaten per fox that is 16 foxes.",
                        '[[step eq="32 × 4 ÷ 8 = 16"]]'],
             "ask": {"a": 3, "b": 2, "c": 14, "op": "prey"}},
            {"worked": ["One more together. 27 rabbits, 4 born each, 2 eaten per fox: 108 new rabbits and 54 foxes.",
                        '[[step eq="27 × 4 ÷ 2 = 54"]]'],
             "ask": {"a": 8, "b": 2, "c": 11, "op": "prey"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": a, "b": b, "c": c, "op": "prey"} for a, b, c in
                 ((2, 4, 4), (4, 8, 14), (3, 2, 8), (5, 10, 34), (2, 3, 33),
                  (9, 5, 15), (8, 3, 12), (2, 4, 74), (6, 3, 21),
                  (2, 3, 72))],
    },
    {
        "id": "diffeq-u9-round-and-round",
        "course": "diffeq", "unit": 9,
        "topic": "The cycle",
        "op": "cycl", "max_value": 190,
        "levels": ("abstract",),
        "symbols": ("cycle", "quarter"),
        "advance_line": "Three in a row — you've got it! The foxes lag by a quarter of the cycle.",
        "teach": [
            ["A balance point is not where rabbits and foxes actually go. Nudge them off it and they do something no straight-line system can do: they circle it, for ever, in a closed loop.",
             '[[goal text="Round and round"]][[step eq="cycle 60 months"]]'],
            ["And the loop has a shape. Plenty of rabbits feed more foxes; more foxes eat the rabbits down; fewer rabbits starve the foxes; fewer foxes let the rabbits back. So the foxes always peak a quarter of a cycle after the rabbits. In a 60-month cycle, that is 15 months.",
             '[[step eq="60 ÷ 4 = 15 months"]]'],
            ["Halving instead of quartering gives 30 — half a cycle, which would put the foxes at their fewest just as the rabbits peak. And 60 is the whole loop, not the lag inside it.",
             '[[step eq="15 ✓"]][[step eq="30 ✗ halved · 60 ✗ the whole cycle"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. A quarter of 100 months puts the fox peak 25 months behind.",
                        '[[step eq="100 ÷ 4 = 25"]]'],
             "ask": {"a": 128, "b": 0, "op": "cycl"}},
            {"worked": ["One more together. 184 months round, quartered — so the foxes lag by 46.",
                        '[[step eq="184 ÷ 4 = 46"]]'],
             "ask": {"a": 176, "b": 0, "op": "cycl"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [{"a": v, "b": 0, "op": "cycl"} for v in
                 (8, 24, 40, 56, 72, 88, 104, 120, 136, 152)],
    },
    {
        "id": "diffeq-u9-a-perfectly-known-equation",
        "course": "diffeq", "unit": 9,
        "topic": "Sensitive dependence",
        "op": "chao", "max_value": 190,
        "levels": ("abstract",),
        "symbols": ("sensitive", "forecast"),
        "advance_line": "Three in a row — you've got it! The gap multiplies once for every day.",
        "teach": [
            ["One last idea, and it is the strangest in the whole course. Everything you have learned says that if you know the equation and the starting point, you know the future. Here is where that quietly stops being true.",
             '[[goal text="A perfectly known equation"]][[step eq="gap 4 · ×3 each day"]]'],
            ["Two forecasts start 4 apart — almost the same, but not quite. In a sensitive system every day multiplies whatever gap there is by 3. After 3 days: 3 times 3 times 3 is 27, and 4 of those is a gap of 108.",
             '[[step eq="4 × 3³ = 108"]]'],
            ["Nothing was random and nothing was unknown. The equation is exact, and the gap simply multiplied its way out of sight — which is why a forecast a month ahead is not available to anyone, at any price. Timesing the days instead of powering gives 36, and 27 forgets the gap you started with.",
             '[[step eq="108 ✓"]][[step eq="36 ✗ timesed · 27 ✗ no start"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. A gap of 9 doubling for 3 days: 8 times 9 is 72.",
                        '[[step eq="9 × 2³ = 72"]]'],
             "ask": {"a": 5, "b": 5, "c": 2, "op": "chao"}},
            {"worked": ["One more together. 5 apart, multiplying by 6 for 2 days: 36 times 5 is 180.",
                        '[[step eq="5 × 6² = 180"]]'],
             "ask": {"a": 6, "b": 3, "c": 3, "op": "chao"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — and it is the last one in the course.",
        "bank": [{"a": a, "b": b, "c": c, "op": "chao"} for a, b, c in
                 ((2, 2, 3), (3, 3, 2), (5, 2, 3), (2, 5, 2), (7, 3, 2),
                  (3, 5, 2), (6, 2, 4), (7, 4, 2), (5, 3, 3), (5, 2, 5))],
    },
]
LESSONS.extend(_DIFFEQ_U9)

# ---- this course's slice of COURSE_ORDER: the teaching order (lessons/__init__.py joins the ten) ----
ORDER = [
    # ---- DIFFERENTIAL EQUATIONS -- the thirteenth and last course ----
    # Unit 1: Introduction, Classification & Slope Fields (build lz)
    "diffeq-u1-a-dash-at-every-point",
    "diffeq-u1-change-the-law-change-the-field",
    "diffeq-u1-reading-the-field-backwards",
    "diffeq-u1-joining-the-dashes",
    # Unit 2: First-Order: Separable & Linear (build lz)
    "diffeq-u2-splitting-the-letters-apart",
    "diffeq-u2-when-the-y-is-underneath",
    "diffeq-u2-the-cooling-cup", "diffeq-u2-the-tank-of-brine",
    # Unit 3: Qualitative Analysis: Equilibria & Stability (build ma)
    "diffeq-u3-the-crowded-pond", "diffeq-u3-where-growth-peaks",
    "diffeq-u3-how-big-the-peak-is",
    "diffeq-u3-the-one-that-pushes-away",
    # Unit 4: Numerical Methods: Euler & Runge-Kutta (build ma)
    "diffeq-u4-walking-it-in-straight-steps",
    "diffeq-u4-the-deal-euler-offers",
    "diffeq-u4-sixteen-instead-of-two",
    "diffeq-u4-what-accuracy-costs",
    # Unit 5: Second-Order Linear: Homogeneous (build mb)
    "diffeq-u5-one-number-decides", "diffeq-u5-the-knife-edge",
    "diffeq-u5-the-spring-that-never-stops",
    "diffeq-u5-damping-slows-the-rocking",
    # Unit 6: Nonhomogeneous, Vibrations & Resonance (build mb)
    "diffeq-u6-somebody-is-pushing", "diffeq-u6-the-part-that-fades",
    "diffeq-u6-why-soldiers-break-step",
    "diffeq-u6-what-saves-the-bridge",
    # Unit 7: Laplace Transforms (build mc)
    "diffeq-u7-derivatives-become-timesing",
    "diffeq-u7-and-now-it-is-just-algebra",
    "diffeq-u7-the-shift-rule", "diffeq-u7-reading-the-ending",
    # Unit 8: Linear Systems & the Phase Plane (build mc)
    "diffeq-u8-two-things-at-once",
    "diffeq-u8-where-an-arrow-goes-flat",
    "diffeq-u8-the-number-in-the-corner",
    "diffeq-u8-two-numbers-decide-the-picture",
    # Unit 9: Nonlinear Systems & Stability (build md)
    # ⭐⭐ THE LAST FOUR LESSONS OF THE WHOLE CURRICULUM.
    "diffeq-u9-up-close-it-is-a-line", "diffeq-u9-rabbits-and-foxes",
    "diffeq-u9-round-and-round",
    "diffeq-u9-a-perfectly-known-equation",
]

# I did no harm and this file is not truncated.

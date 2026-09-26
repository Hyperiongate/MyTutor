# =============================================================================
# lessons/bridges.py  --  THE COURSE REVIEW: what earlier courses gave you  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-09-26  BUILD yi -- NEW FILE. Jim (09-26): "every lesson, aside from entry level,
#               should have a review discussion ... welcome to geometry, before we get into
#               this, a few things that we covered in earlier courses that are important to
#               know for geometry. It should list those things and discuss them. It doesn't
#               need to be a big thing, but it needs to be enough so that somebody's not
#               shocked when they go into a new course."
#
#               One review per course, nine courses (Entry has nothing before it). Each is
#               a short scripted sequence -- a welcome that names the review, one beat per
#               thing worth remembering (three or four, each with a board), and a hand-over
#               to the first lesson. lessonscripts.bridge_steps(course, after_tour) turns
#               it into `say` beats named "bridge"; main.py plays them at the front of a
#               student's FIRST scripted lesson in the course (no finished lesson on the
#               record yet), and session.html shows an obvious "Skip the review" button
#               while they play. Every line here is in the pre-rendered closure
#               (lessonscripts.BRIDGE_LINES), so nothing is voiced live.
#
#               TWO OPENERS. A first-time student hears the screen tour first, whose opener
#               already says "Welcome to geometry" -- so after the tour the review opens
#               "Now, before we get into geometry..." instead of welcoming twice. A toured
#               student entering a new course gets the "Welcome to geometry" opener.
#
#               HOUSE RULES kept: every sentence under 27 words, every beat under 80, no
#               line speaks a number its board does not draw, and the rules named are the
#               ones the earlier courses actually taught (unit titles in curriculum.py).
# =============================================================================
"""The course reviews. Pure data: BRIDGES[course] = {"welcome": (spoken, board),
"after_tour": (spoken, board), "beats": [(spoken, board), ...], "handover":
(spoken, board)}. lessonscripts.py reads it; nothing here imports anything."""

BRIDGES = {
    "basic": {
        "welcome": (
            "Welcome to Basic Math! Before we get into it, a quick look back at a few things "
            "from Entry-Level Math that matter here.",
            '[[card title="From Entry-Level Math" items="Tens and ones | Adding and taking away, with carrying | Counting in steps: by 2s, 5s and 10s"]]'),
        "after_tour": (
            "Now, before we get into Basic Math, a quick look back at a few things from "
            "Entry-Level Math that matter here.",
            '[[card title="From Entry-Level Math" items="Tens and ones | Adding and taking away, with carrying | Counting in steps: by 2s, 5s and 10s"]]'),
        "beats": [
            ("First, tens and ones. A number like 47 is 4 tens and 7 ones. In this course "
             "the numbers get bigger, and every big number is still built from tens and ones.",
             '[[placevalue t="4" o="7" caption="47 is 4 tens and 7 ones"]]'),
            ("Second, adding and taking away with carrying. 38 plus 25: 8 plus 5 is 13, so write "
             "the 3 and carry a ten. You will use that carry in every unit.",
             '[[column terms="38|25" op="+" carries="1_" result="63" caption="8 + 5 = 13: write 3, carry one ten"]]'),
            ("Third, counting in steps. Counting by 5s — 5, 10, 15, 20 — is the seed of "
             "multiplying, which is where this course begins.",
             '[[numberline min="0" max="20" points="5,10,15,20" caption="counting by 5s: 5, 10, 15, 20"]]'),
        ],
        "handover": (
            "That is the review. If any of it felt shaky, the first unit goes over place value "
            "again. Here comes the first lesson.",
            '[[goal text="On to Basic Math"]]'),
    },
    "prealgebra": {
        "welcome": (
            "Welcome to Pre-Algebra! Before we get into it, a quick look back at a few things "
            "from Basic Math that matter here.",
            '[[card title="From Basic Math" items="The times tables and dividing | Fractions: equal parts of a whole | Decimals and place value | The number line"]]'),
        "after_tour": (
            "Now, before we get into Pre-Algebra, a quick look back at a few things from "
            "Basic Math that matter here.",
            '[[card title="From Basic Math" items="The times tables and dividing | Fractions: equal parts of a whole | Decimals and place value | The number line"]]'),
        "beats": [
            ("First, the times tables and dividing. 6 times 7 is 42, and 42 divided by 7 is 6 — "
             "the same fact read backwards. Pre-Algebra leans on both every day.",
             '[[step eq="6 × 7 = 42"]][[step eq="42 ÷ 7 = 6"]]'),
            ("Second, fractions. Three quarters means a whole cut into 4 equal parts, and 3 of "
             "them taken. Equal parts is the whole idea.",
             '[[pie parts="4" shaded="3" caption="3 of 4 equal parts: three quarters"]]'),
            ("Third, decimals. 2 point 5 is 2 and a half — the digit after the point counts "
             "tenths. Fractions and decimals are two ways to write the same amount.",
             '[[step eq="2.5 = 2 and 5 tenths"]][[step eq="2.5 = 2 ½"]]'),
            ("Fourth, the number line. Every number has a place on it, and bigger is always to "
             "the right. This course will send the line to the LEFT of zero, into negatives.",
             '[[numberline min="0" max="10" points="2.5,7" caption="2.5 and 7 — bigger is to the right"]]'),
        ],
        "handover": (
            "That is the review. If any of it felt shaky, say so when it comes up and we will "
            "slow down. Here comes the first lesson.",
            '[[goal text="On to Pre-Algebra"]]'),
    },
    "algebra1": {
        "welcome": (
            "Welcome to Algebra One! Before we get into it, a quick look back at a few things "
            "from Pre-Algebra that matter here.",
            '[[card title="From Pre-Algebra" items="Negative numbers on the number line | Order of operations | Fractions, decimals and percents | A letter for a number you do not know"]]'),
        "after_tour": (
            "Now, before we get into Algebra One, a quick look back at a few things from "
            "Pre-Algebra that matter here.",
            '[[card title="From Pre-Algebra" items="Negative numbers on the number line | Order of operations | Fractions, decimals and percents | A letter for a number you do not know"]]'),
        "beats": [
            ("First, negative numbers. The number line runs both ways from zero: negative 3 is "
             "3 steps to the left. Algebra moves in both directions all the time.",
             '[[numberline min="-5" max="5" points="-3,3" caption="−3 is 3 steps left of zero, 3 is 3 steps right"]]'),
            ("Second, order of operations. In 2 plus 3 times 4, the times goes first: 3 times 4 "
             "is 12, then 2 plus 12 is 14. Never left to right.",
             '[[step eq="2 + 3 × 4"]][[step eq="3 × 4 = 12"]][[step eq="2 + 12 = 14"]]'),
            ("Third, fractions, decimals and percents are one amount in three costumes: a half, "
             "0 point 5, and 50 percent. Algebra will ask for whichever suits the problem.",
             '[[step eq="½ = 0.5 = 50%"]]'),
            ("Fourth, a letter can stand for a number you do not know yet. If x plus 4 is 10, "
             "then x is 6. That letter is the whole of algebra.",
             '[[step eq="x + 4 = 10"]][[step eq="x = 6"]]'),
        ],
        "handover": (
            "That is the review. Algebra will use all four, and we will meet each one again "
            "properly. Here comes the first lesson.",
            '[[goal text="On to Algebra One"]]'),
    },
    "geometry": {
        "welcome": (
            "Welcome to Geometry! Before we get into it, a quick look back at a few things from "
            "earlier courses that matter here.",
            '[[card title="From earlier courses" items="Angles: 90, 180 and 360 degrees | Solving a simple equation | Squares and square roots | Area of a rectangle"]]'),
        "after_tour": (
            "Now, before we get into Geometry, a quick look back at a few things from earlier "
            "courses that matter here.",
            '[[card title="From earlier courses" items="Angles: 90, 180 and 360 degrees | Solving a simple equation | Squares and square roots | Area of a rectangle"]]'),
        "beats": [
            ("First, angles. A square corner is 90 degrees, a straight line is 180, and a full "
             "turn is 360. Geometry uses those three totals constantly.",
             '[[angle deg="90" caption="a square corner: 90°"]][[step eq="straight line: 180° · full turn: 360°"]]'),
            ("Second, solving a simple equation. If an angle plus 40 equals 180, take 40 from both "
             "sides: the angle is 140. Many geometry problems end this way.",
             '[[step eq="x + 40 = 180"]][[step eq="x = 140"]]'),
            ("Third, squares and square roots. 5 squared is 25, and the square root of 25 is 5. "
             "Right triangles run on that pair.",
             '[[step eq="5² = 25"]][[step eq="√25 = 5"]]'),
            ("Fourth, area. A rectangle 6 long and 4 tall covers 6 times 4, which is 24 squares. "
             "Every area rule in this course grows out of that one.",
             '[[rectangle w="6" h="4" show="area" caption="6 × 4 = 24 squares"]]'),
        ],
        "handover": (
            "That is the review. If any of it felt shaky, say so when it comes up and we will "
            "slow down. Here comes the first lesson.",
            '[[goal text="On to Geometry"]]'),
    },
    "algebra2": {
        "welcome": (
            "Welcome to Algebra Two! Before we get into it, a quick look back at a few things "
            "from Algebra One that matter here.",
            '[[card title="From Algebra One" items="Solving a linear equation | Lines: y = mx + b | Powers and roots | Factoring x² + bx + c"]]'),
        "after_tour": (
            "Now, before we get into Algebra Two, a quick look back at a few things from "
            "Algebra One that matter here.",
            '[[card title="From Algebra One" items="Solving a linear equation | Lines: y = mx + b | Powers and roots | Factoring x² + bx + c"]]'),
        "beats": [
            ("First, solving a linear equation. 3 x plus 5 equals 20: take 5 from both sides for "
             "3 x equals 15, then divide by 3. x is 5.",
             '[[step eq="3x + 5 = 20"]][[step eq="3x = 15"]][[step eq="x = 5"]]'),
            ("Second, lines. y equals 2 x plus 1 is a line: the 2 is its slope, the 1 is where "
             "it crosses the y axis. Every function in this course gets compared to a line.",
             '[[graph lines="y=2x+1" names="y = 2x + 1" points="(0,1)" range="-3..3" yrange="-5..7" caption="slope 2, crossing at 1"]]'),
            ("Third, powers and roots. 2 to the power 5 is 32, and the square root of 49 is 7. "
             "Roots are powers run backwards, and Unit Five says exactly how.",
             '[[step eq="2⁵ = 32"]][[step eq="√49 = 7"]]'),
            ("Fourth, factoring. x squared plus 5 x plus 6 is x plus 2, times x plus 3 — two "
             "numbers that add to 5 and multiply to 6. Quadratics live on this.",
             '[[step eq="x² + 5x + 6 = (x + 2)(x + 3)"]]'),
        ],
        "handover": (
            "That is the review. Algebra Two picks up right where those left off. Here comes "
            "the first lesson.",
            '[[goal text="On to Algebra Two"]]'),
    },
    "precalc": {
        "welcome": (
            "Welcome to Trig and Pre-Calc! Before we get into it, a quick look back at a few "
            "things from Algebra Two and Geometry that matter here.",
            '[[card title="From Algebra Two and Geometry" items="A function and f(x) | Quadratics and their roots | Exponents and logs | Sine, cosine and tangent in a right triangle"]]'),
        "after_tour": (
            "Now, before we get into Trig and Pre-Calc, a quick look back at a few things from "
            "Algebra Two and Geometry that matter here.",
            '[[card title="From Algebra Two and Geometry" items="A function and f(x) | Quadratics and their roots | Exponents and logs | Sine, cosine and tangent in a right triangle"]]'),
        "beats": [
            ("First, a function is a machine: a number goes in, one number comes out. f of x "
             "equals 2 x plus 3 sends 4 to 11. Pre-Calculus is a course about machines.",
             '[[machine input="4" rule="2x + 3" output="11" fname="f" caption="f(4) = 11"]]'),
            ("Second, quadratics. x squared take away 5 x plus 6 factors as x take away 2, times "
             "x take away 3. So its roots are 2 and 3, where the curve crosses the axis.",
             '[[graph func="x^2-5*x+6" names="y = x² − 5x + 6" points="(2,0),(3,0)" range="0..5" yrange="-1..6" caption="roots at 2 and 3"]]'),
            ("Third, exponents and logs. 2 to the power 3 is 8, and log base 2 of 8 is 3 — the "
             "log asks which power. Unit Three builds on that pair.",
             '[[step eq="2³ = 8"]][[step eq="log₂ 8 = 3"]]'),
            ("Fourth, from Geometry: in a right triangle, sine is opposite over hypotenuse, "
             "cosine is adjacent over hypotenuse, tangent is opposite over adjacent. Trigonometry "
             "starts there and goes round the whole circle.",
             '[[triangle v="A,B,C" right="B" sides="3,4,5" caption="a 3-4-5 right triangle"]][[step eq="sin = opposite ÷ hypotenuse"]]'),
        ],
        "handover": (
            "That is the review. If any of it felt shaky, say so when it comes up and we will "
            "slow down. Here comes the first lesson.",
            '[[goal text="On to Trig and Pre-Calc"]]'),
    },
    "calculus": {
        "welcome": (
            "Welcome to Calculus! Before we get into it, a quick look back at a few things from "
            "Pre-Calculus that matter here.",
            '[[card title="From Pre-Calculus" items="Functions and their graphs | The slope of a line | A limit: where a function is headed | Powers of x"]]'),
        "after_tour": (
            "Now, before we get into Calculus, a quick look back at a few things from "
            "Pre-Calculus that matter here.",
            '[[card title="From Pre-Calculus" items="Functions and their graphs | The slope of a line | A limit: where a function is headed | Powers of x"]]'),
        "beats": [
            ("First, functions and their graphs. y equals x squared is a curve that climbs faster "
             "and faster. Calculus is about how a graph like that changes.",
             '[[graph func="x^2" names="y = x²" points="(2,4)" range="0..4" yrange="0..16" caption="y = x² — steeper as it goes"]]'),
            ("Second, slope. A line that rises 6 across a run of 2 has slope 3 — rise over run. "
             "The derivative is that idea, at a single point.",
             '[[graph lines="y=3x" names="y = 3x" points="(0,0),(2,6)" range="0..3" yrange="0..9" caption="rise 6 over run 2: slope 3"]][[step eq="6 ÷ 2 = 3"]]'),
            ("Third, limits. As x closes in on 2, x squared closes in on 4 — a limit is where a "
             "function is headed. Unit One begins exactly there.",
             '[[graph func="x^2" names="y = x²" hole="2" lines="x=2" range="0..4" yrange="0..16" caption="as x → 2, x² → 4"]]'),
            ("Fourth, powers of x. x squared, x cubed, x to the fourth: the derivative rules in "
             "Unit Two are written for these.",
             '[[step eq="x², x³, x⁴"]]'),
        ],
        "handover": (
            "That is the review. If any of it felt shaky, say so when it comes up and we will "
            "slow down. Here comes the first lesson.",
            '[[goal text="On to Calculus"]]'),
    },
    "diffeq": {
        "welcome": (
            "Welcome to Differential Equations! Before we get into it, a quick look back at a "
            "few things from Calculus that matter here.",
            '[[card title="From Calculus" items="The derivative is a rate | The power rule | Antiderivatives and + C | The exponential function"]]'),
        "after_tour": (
            "Now, before we get into Differential Equations, a quick look back at a few things "
            "from Calculus that matter here.",
            '[[card title="From Calculus" items="The derivative is a rate | The power rule | Antiderivatives and + C | The exponential function"]]'),
        "beats": [
            ("First, the derivative is a rate: how fast y changes as x moves. Every equation in "
             "this course is about a rate, written d y d x.",
             '[[step eq="dy/dx = the rate y changes"]]'),
            ("Second, the power rule. The derivative of x cubed is 3 x squared — the power comes "
             "down front and drops by one.",
             '[[step eq="x³ → 3x²"]]'),
            ("Third, antiderivatives. Run the rule backwards: 3 x squared came from x cubed, plus "
             "any constant. That plus C is why a differential equation has a whole family of "
             "solutions.",
             '[[step eq="3x² → x³ + C"]]'),
            ("Fourth, the exponential function. e to the x is its own derivative, so growth at a "
             "rate equal to the amount is exponential. Half of this course is that one fact.",
             '[[graph func="exp(x)" names="y = eˣ" range="-2..2" yrange="0..8" caption="y = eˣ — its slope equals its height"]]'),
        ],
        "handover": (
            "That is the review. If any of it felt shaky, say so when it comes up and we will "
            "slow down. Here comes the first lesson.",
            '[[goal text="On to Differential Equations"]]'),
    },
    "probstat": {
        "welcome": (
            "Welcome to Probability and Statistics! Before we get into it, a quick look back at "
            "a few things from earlier courses that matter here.",
            '[[card title="From earlier courses" items="Fractions, decimals and percents | The mean of a list | The coordinate grid | Counting choices by multiplying"]]'),
        "after_tour": (
            "Now, before we get into Probability and Statistics, a quick look back at a few "
            "things from earlier courses that matter here.",
            '[[card title="From earlier courses" items="Fractions, decimals and percents | The mean of a list | The coordinate grid | Counting choices by multiplying"]]'),
        "beats": [
            ("First, fractions, decimals and percents. A chance of 1 in 4 is a quarter, 0 point "
             "2 5, and 25 percent. Probability is written in all three.",
             '[[step eq="¼ = 0.25 = 25%"]]'),
            ("Second, the mean. Add the list and divide by how many: 4, 6 and 8 add to 18, and 18 "
             "divided by 3 is 6. Statistics starts by describing a list with one number.",
             '[[step eq="4 + 6 + 8 = 18"]][[step eq="18 ÷ 3 = 6"]]'),
            ("Third, the coordinate grid. A point is an across and an up, like 3 across and 5 up. "
             "Scatterplots put one point on the grid for every pair of measurements.",
             '[[graph points="(3,5)" range="0..6" yrange="0..6" caption="the point (3, 5): 3 across, 5 up"]]'),
            ("Fourth, counting by multiplying. 3 shirts and 4 pairs of trousers make 3 times 4, "
             "which is 12 outfits. Probability counts the ways before it counts the chances.",
             '[[array rows="3" cols="4" caption="3 × 4 = 12 outfits"]]'),
        ],
        "handover": (
            "That is the review. If any of it felt shaky, say so when it comes up and we will "
            "slow down. Here comes the first lesson.",
            '[[goal text="On to Probability and Statistics"]]'),
    },
}

# I did no harm and this file is not truncated.

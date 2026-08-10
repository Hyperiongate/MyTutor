# =============================================================================
# pedagogy.py  --  Math Tutor MVP  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-08-11  BUILD de -- DIFFEQ pedagogy restructured to the CUPM mainstream syllabus:
#               names + all nine unit briefs. Units 3 (qualitative), 4 (numerical), 8
#               (linear systems) and 9 (nonlinear) are new; 2 and 6 are merges of old
#               pairs; series solutions dropped per the CUPM report.
#   2026-08-03  ADDED TWO ELEMENTARY TEACHING BRAINS (Jim's restructure): COURSE_PEDAGOGY["entry"]
#               (Entry-Level Math, grades 1-3) and ["basic"] (Basic Math, grades 4-6). Each has
#               unit_names, 9 units of {misconceptions, how_to_teach, progression}, and a
#               cross_cutting error watch-list -- same shape as the other courses. Also added a
#               "roughly 6-8 (early concrete)" developmental dial to the universal METHODOLOGY
#               block so the youngest learners are met right. Purely additive; nothing else changed.
#   2026-07-28  ADDED COURSE 8 -- DIFFERENTIAL EQUATIONS teaching brain (COURSE_PEDAGOGY["diffeq"]):
#               9 units (classification, separable & models, first-order linear, exact &
#               substitutions, 2nd-order homogeneous, 2nd-order nonhomogeneous, vibrations &
#               circuits, Laplace transforms, series & systems) with misconceptions / how-to-teach /
#               progression + a CLASSIFY-FIRST cross-cutting list. Source: DiffEq_Curriculum_KB.md.
#               Additive; the seven existing courses untouched. Do no harm.
#   2026-07-28  ADDED COURSE 7 -- CALCULUS teaching brain (COURSE_PEDAGOGY["calculus"]): 9 units
#               (limits & continuity, the derivative, product/quotient/chain, applications of
#               derivatives, curve sketching & optimization, antiderivatives, the definite integral &
#               FTC, applications of integration, intro to differential equations) with misconceptions
#               / how-to-teach / progression + a calculus cross-cutting list. Source:
#               Calculus_Curriculum_KB.md. Additive; the six existing courses untouched. Do no harm.
#   2026-07-28  ADDED COURSE 6 -- PROBABILITY & STATISTICS teaching brain (COURSE_PEDAGOGY["probstat"]):
#               9 units (exploring data, describing distributions, scatterplots & correlation,
#               collecting data, probability basics, conditional probability & independence, random
#               variables & expected value, the normal distribution, sampling & inference) with
#               misconceptions / how-to-teach / progression + a stats cross-cutting list. Source:
#               ProbStat_Curriculum_KB.md. Universal METHODOLOGY reused as-is. Additive; the five
#               existing courses untouched. Do no harm.
#   2026-07-28  ADDED COURSE 5 -- TRIG / PRE-CALC teaching brain (COURSE_PEDAGOGY["precalc"]): 9 units
#               (functions & graphs, polynomial & rational, exp & log, trig functions, analytic trig,
#               applications of trig, conics & parametric, sequences/series/binomial, intro to limits)
#               with misconceptions / how-to-teach / progression + a precalc cross-cutting list.
#               Source: PreCalc_Curriculum_KB.md. Universal METHODOLOGY reused as-is. Additive; the
#               four existing courses untouched. Do no harm.
#   2026-07-28  ADDED COURSE 4 -- ALGEBRA II teaching brain (COURSE_PEDAGOGY["algebra2"]): 9 units
#               (foundations/systems, quadratics & complex numbers, polynomials, rationals, radicals
#               & rational exponents, exponentials & logs, sequences & series, trigonometry,
#               statistics & probability) with misconceptions / how-to-teach / progression + an
#               Algebra II cross-cutting error list. Source: AlgebraII_Curriculum_KB.md. Universal
#               METHODOLOGY reused as-is. Additive; Pre-Algebra, Algebra I, and Geometry untouched.
#               Do no harm.
#   2026-07-28  ADDED COURSE 3 -- PRE-ALGEBRA teaching brain (COURSE_PEDAGOGY["prealgebra"]): 9
#               foundations units (number sense/order-of-ops, factors, integers, fractions,
#               decimals, ratios, percents, measurement, variables) with misconceptions /
#               how-to-teach / progression + a pre-algebra cross-cutting list. Source:
#               PreAlgebra_Curriculum_KB.md. Universal METHODOLOGY reused as-is. Additive; Algebra
#               I + Geometry untouched. Do no harm.
#   2026-07-27  MULTI-COURSE (Phase 1 of the math-ladder expansion; see the project doc
#               Multi_Course_Expansion_Plan.md). The per-unit teaching notes are now nested
#               PER COURSE: COURSE_PEDAGOGY[course_id] -> {unit_names, cross_cutting, units}.
#               Added a SECOND course, "geometry" (9 units, distilled from
#               Geometry_Curriculum_KB.md), with its own misconceptions / how-to-teach /
#               progression + a Geometry-specific cross-cutting error list. The UNIVERSAL
#               METHODOLOGY (how to reach a learner) is subject-agnostic and reused unchanged
#               across every course. BACKWARD-COMPATIBLE: teaching_playbook(unit) still works
#               exactly as before (defaults to Algebra I), and the old module-level names
#               UNIT_NAME / UNIT_PEDAGOGY / CROSS_CUTTING still resolve to Algebra I. A new
#               optional 2nd arg selects the course: teaching_playbook(unit, course). No change
#               for Algebra I -- do no harm.
#   2026-07-24  PHASE D -- CONTENT GUARDRAILS. Added "VERIFY EVERY PROBLEM YOU MAKE UP" to
#               METHODOLOGY (so it reaches lesson + practice + topic via the injected playbook):
#               solve-and-check every invented problem before showing, keep it on the skill at
#               hand, calibrate difficulty to the student, vary it, discard bad ones. Makes the
#               AI-generates-its-own-content approach credible (see the strategy doc).
#   2026-07-24  Added the "INTRODUCE BEFORE YOU PRACTICE" principle to METHODOLOGY: if a
#               student is new to an idea, NAME + DEFINE it (on the board) and do one example
#               yourself BEFORE any exercise -- never hand a beginner a problem using a word
#               you haven't defined. Fix for a Topic session where the tutor jumped straight to
#               multiplying polynomials without ever defining "polynomial" or "factor."
#   2026-07-23  NEW. This is the tutor's TEACHING BRAIN as a reusable knowledge
#               base, distilled from the two project KBs so it ships in the repo and
#               reaches the LIVE tutor at runtime (the project .md docs do NOT deploy
#               to Render -- this module is the deployed copy). It gives the model the
#               same expertise a strong human tutor carries, so we stop hand-scripting
#               teaching behavior one rule at a time.
#                 - COURSE_PEDAGOGY[course]["units"][n]: for each unit, the RELIABLE
#                   student MISCONCEPTIONS (teach against these) + HOW TO TEACH it
#                   (representations/methods that work) + an easy->hard progression.
#                 - METHODOLOGY: how to REACH the learner -- developmental dials by
#                   age, evidence-based feedback (process praise, "wise feedback",
#                   never person/empty praise), and confidence/anxiety vs. overconfidence
#                   signals to respond to the individual (never branch on gender).
#                   Source: Teaching_Methodology_KB.md. UNIVERSAL -- reused every course.
#                 - COURSE_PEDAGOGY[course]["cross_cutting"]: that course's all-year
#                   error watch-list.
#               teaching_playbook(unit, course) assembles the slice the tutor needs THIS
#               turn: the universal methodology + that course's cross-cutting errors + the
#               specific unit's detail (or a compact all-units index when the unit is unknown).
#
#   WHY A MODULE (not more prompt text hand-written in tutor.py): the teaching
#   knowledge lives in ONE place, is easy to improve, and is injected per student/turn
#   instead of bloating every prompt with all the units. Pure data + string assembly,
#   no external calls, so it is instant and free on every turn.
# =============================================================================

DEFAULT_COURSE = "algebra1"

# -----------------------------------------------------------------------------
# ALGEBRA I -- per-unit pedagogy (distilled from Algebra_I_Curriculum_KB.md). UNCHANGED.
# -----------------------------------------------------------------------------
_ALGEBRA1_UNIT_NAMES = {
    1: "Foundations & Expressions",
    2: "Linear Equations & Inequalities",
    3: "Functions & Notation",
    4: "Linear Functions & Graphs",
    5: "Systems of Equations",
    6: "Exponents & Exponential Functions",
    7: "Polynomials & Factoring",
    8: "Quadratic Functions",
    9: "Data & Statistics",
}

_ALGEBRA1_UNIT_PEDAGOGY = {
    1: {
        "misconceptions": (
            "reading 3x as 3 + x; combining unlike terms (2x + 3 becoming 5x); "
            "distribution slips like 4(2x - 10) = 8x - 10 (it is 8x - 40); sign errors "
            "distributing a negative, -(x - 3) = -x - 3 (it is -x + 3)."
        ),
        "how_to_teach": (
            "Use a concrete 'mystery box' for the variable and an AREA MODEL for "
            "distribution (a rectangle split into parts). Sort terms into piles to make "
            "'like terms' visible. Evaluate by substituting a number in and computing."
        ),
        "progression": "evaluate 2x + 5 at x = 3  ->  simplify 3x + 2 - x + 7  ->  expand -2(3x - 4)  ->  simplify 5 - 2(x - 1)",
    },
    2: {
        "misconceptions": (
            "not doing the SAME thing to BOTH sides; sign errors moving terms across the "
            "equals sign; forgetting to distribute first; forgetting to FLIP the inequality "
            "when multiplying or dividing by a negative; dividing by a variable (loses "
            "solutions); treating 'no solution' as a mistake."
        ),
        "how_to_teach": (
            "Balance/see-saw model (both sides must stay equal) and inverse 'undo' "
            "operations to peel x down to itself; the 'mystery crate' for a one-step; "
            "ALWAYS check by substituting the answer back in. For inequalities, use a "
            "number line and a test point."
        ),
        "progression": "x + 4 = 12  ->  2x + 3 = 11  ->  5x - 4 = 3x + 2  ->  3(x - 2) = 2x + 5  ->  -2x + 1 > 9 (flip!)  ->  solve P = 2l + 2w for w",
    },
    3: {
        "misconceptions": (
            "reading f(x) as 'f times x' (it is 'f OF x'); confusing domain and range; "
            "believing every relation is a function."
        ),
        "how_to_teach": (
            "The FUNCTION MACHINE: a number goes in, the rule runs, one number comes out. "
            "Mapping diagrams; the vertical line test; move among the four faces of a "
            "function -- table, graph, equation, and words."
        ),
        "progression": "given f(x) = 2x - 1 find f(0), f(3), f(-2)  ->  state the domain and range of a graph  ->  decide if a table or graph is a function",
    },
    4: {
        "misconceptions": (
            "slope taken upside down as run over rise; sign errors with negative slopes; "
            "confusing the slope with the y-intercept; 'steeper = more' without context."
        ),
        "how_to_teach": (
            "The 'staircase' rise-over-run on a grid; tables with a CONSTANT difference "
            "(that constant IS the slope); real contexts like savings per week where the "
            "slope is the rate and the intercept is the starting amount."
        ),
        "progression": "slope through (1,2) and (3,8)  ->  graph y = 2x - 3  ->  line through (0,5) with slope -2  ->  line through two points  ->  interpret cost = 5g + 30",
    },
    5: {
        "misconceptions": (
            "solving for one variable and forgetting the second; sign errors during "
            "elimination; shading the wrong side or wrong boundary for inequalities."
        ),
        "how_to_teach": (
            "Start GRAPHICALLY so they SEE the intersection is the shared solution, then "
            "substitution, then elimination. Connect 'no solution' to parallel lines and "
            "'infinitely many' to the same line."
        ),
        "progression": "graph y = x + 1 and y = -x + 3  ->  substitution  ->  elimination on 2x + y = 7 and x - y = 2  ->  graph the system y > x and y <= 2x + 1",
    },
    6: {
        "misconceptions": (
            "-3^2 = 9 (it is -9; the square binds before the minus); (4x)^2 = 4x^2 (it is "
            "16x^2); x^0 = 0 (it is 1); mixing up the exponent rules; not seeing linear "
            "(repeated ADDING) vs exponential (repeated MULTIPLYING) in a table."
        ),
        "how_to_teach": (
            "Side-by-side ADD-vs-MULTIPLY tables to feel the difference; the doubling / "
            "paper-folding story for growth; negative exponents as repeated DIVISION."
        ),
        "progression": "x^3 * x^4  ->  (x^3)^2  ->  x^5 / x^2  ->  2^-3  ->  y = 3 * 2^x at x = 0..3  ->  is this table linear or exponential  ->  $100 growing 5%/yr",
    },
    7: {
        "misconceptions": (
            "(x + y)^2 = x^2 + y^2 (it forgets the middle term 2xy); sign errors when "
            "factoring; distribution errors multiplying binomials; forgetting to pull the "
            "GCF out first."
        ),
        "how_to_teach": (
            "Algebra tiles and the AREA / BOX model in BOTH directions (multiply by "
            "filling the box, factor by reading it back). The systematic question: 'what "
            "two numbers multiply to c and add to b?'"
        ),
        "progression": "(2x + 3) + (x - 5)  ->  3x(x - 2)  ->  (x + 4)(x - 4)  ->  (x + 3)^2  ->  factor x^2 + 7x + 12  ->  x^2 - 9  ->  2x^2 + 7x + 3",
    },
    8: {
        "misconceptions": (
            "sqrt(16) = plus-or-minus 4 (the principal root is 4; the plus/minus comes "
            "from solving x^2 = 16); canceling a variable in 2x^2 = x (loses x = 0 -- set "
            "equal to zero and factor); sign errors in the quadratic formula; assuming "
            "every quadratic factors; reading a vertex-form shift backwards."
        ),
        "how_to_teach": (
            "Build the ladder: factoring (zero-product) -> square roots -> completing the "
            "square -> the quadratic formula. Connect the x-intercepts of the parabola to "
            "the solutions; use a table/graph to see the symmetry around the vertex."
        ),
        "progression": "x^2 = 49  ->  x^2 - 5x = 0  ->  x^2 + 5x + 6 = 0 (factor)  ->  x^2 - 6x + 5 = 0 (complete the square)  ->  2x^2 + 3x - 2 = 0 (formula)  ->  vertex of y = x^2 - 4x + 1  ->  a projectile word problem",
    },
    9: {
        "misconceptions": (
            "treating correlation as causation; using the mean when the data is skewed "
            "(the median is better); extrapolating a trend line far beyond the data."
        ),
        "how_to_teach": (
            "Use REAL data the student cares about. Eyeball a trend line before any formal "
            "regression. Read center (mean/median) and spread (range/IQR/spread) off dot "
            "plots, box plots, and histograms; build a scatter plot and a line of best fit."
        ),
        "progression": "describe a small data set's center and spread  ->  build a scatter plot  ->  draw a best-fit line  ->  interpret its slope in context  ->  correlation vs causation",
    },
}

_ALGEBRA1_CROSS_CUTTING = """\
ERROR WATCH-LIST (catch these all year, in every unit):
- Negatives: -3^2 = -9 but (-3)^2 = 9; distributing a negative flips EVERY sign.
- Distribution: multiply the factor by EVERY term inside; 4(2x - 10) = 8x - 40.
- Squaring a sum: (x + y)^2 = x^2 + 2xy + y^2, NOT x^2 + y^2.
- Roots of a sum: sqrt(x + y) is NOT sqrt(x) + sqrt(y).
- Illegal canceling: factor first; never cancel across a + or -.
- Canceling a variable while solving can LOSE solutions (set equal to 0 and factor).
- Inequalities: FLIP the sign when multiplying/dividing by a negative.
- Exponent of a product: (4x)^2 = 16x^2, not 4x^2.
- Notation: f(x) is "f of x," not "f times x." """

# -----------------------------------------------------------------------------
# GEOMETRY -- per-unit pedagogy (distilled from Geometry_Curriculum_KB.md).
# -----------------------------------------------------------------------------
_GEOMETRY_UNIT_NAMES = {
    1: "Foundations & Constructions",
    2: "Transformations & Symmetry",
    3: "Congruence & Triangle Proofs",
    4: "Similarity & Dilations",
    5: "Right Triangles & Trigonometry",
    6: "Circles",
    7: "Coordinate Geometry",
    8: "Area, Surface Area & Volume",
    9: "Probability",
}

_GEOMETRY_UNIT_PEDAGOGY = {
    1: {
        "misconceptions": (
            "assuming facts from how a figure LOOKS (it looks perpendicular or equal) "
            "instead of from the given marks; confusing a segment, a ray, and a line; "
            "confusing a midpoint (the point) with a bisector (the thing that cuts); "
            "thinking a construction is 'just careful drawing' rather than an exact procedure."
        ),
        "how_to_teach": (
            "Drill 'given vs. looks like' from day one -- only marked or derived facts count. "
            "Use a real compass/straightedge (or step-by-step board constructions) so a "
            "construction is a proof you can SEE. Tick-marks and angle-arcs to show what is "
            "actually equal; name angles carefully (three letters, vertex in the middle)."
        ),
        "progression": "name and measure an angle  ->  find a supplement/complement  ->  identify vertical angles  ->  bisect a segment  ->  copy an angle  ->  construct a perpendicular",
    },
    2: {
        "misconceptions": (
            "reflecting over the x-axis vs the y-axis (which coordinate changes sign); "
            "rotating the wrong direction (clockwise vs counterclockwise) or about the wrong "
            "center; thinking a translation or reflection changes size or shape; sloppy "
            "matching of pre-image to image."
        ),
        "how_to_teach": (
            "Patty paper / tracing to physically SLIDE, FLIP, and TURN a figure. On the grid, "
            "tie each motion to its coordinate rule (reflect over x-axis: (x, y) -> (x, -y)). "
            "Fold paper to find lines of symmetry. Stress that rigid motions preserve length "
            "and angle -- same shape and size, new position."
        ),
        "progression": "translate a point by a vector  ->  reflect a triangle over the y-axis  ->  rotate 90 degrees about the origin  ->  describe a motion mapping one figure to another  ->  find all symmetries of a shape",
    },
    3: {
        "misconceptions": (
            "thinking AAA or SSA proves congruence (they do NOT); mismatching corresponding "
            "parts when using CPCTC; using the picture ITSELF as the proof; skipping the reason "
            "for a step; confusing 'congruent' (same size and shape) with 'equal' (same number)."
        ),
        "how_to_teach": (
            "Build congruence from the transformations in Unit 2 -- congruent means there is a "
            "rigid motion that lands one figure exactly on the other. Teach a proof as a CHAIN "
            "of justified steps: every statement needs a reason. Start with fill-in-the-blank "
            "proofs before blank ones. Call out the non-criteria (AAA, SSA) explicitly."
        ),
        "progression": "mark the given info on a figure  ->  pick the right congruence criterion (SSS/SAS/ASA/AAS/HL)  ->  fill in a two-column proof  ->  write a full proof  ->  use CPCTC to justify a further equal part",
    },
    4: {
        "misconceptions": (
            "ADDING to sides instead of MULTIPLYING by the scale factor; setting up a "
            "proportion with mismatched correspondence; assuming area scales by the same factor "
            "as the sides (it scales by k^2, volume by k^3); confusing 'similar' with 'congruent'."
        ),
        "how_to_teach": (
            "Dilate a figure on a grid from a center and read the scale factor off matching "
            "points. Overlay similar triangles to see the equal angles and the constant ratio "
            "of sides. Make k vs k^2 vs k^3 concrete with a scaled square and cube -- double the "
            "side, the area quadruples."
        ),
        "progression": "dilate a figure by k = 2  ->  decide if two triangles are similar (AA)  ->  solve for a missing side by proportion  ->  use the side-splitter theorem  ->  compare the areas of two similar figures",
    },
    5: {
        "misconceptions": (
            "using the Pythagorean theorem on a NON-right triangle; mislabeling opposite vs "
            "adjacent relative to the chosen angle; the calculator in the wrong mode (radians "
            "vs DEGREES); mixing up which ratio is sine/cosine/tangent; forgetting the "
            "hypotenuse is the longest side, opposite the right angle."
        ),
        "how_to_teach": (
            "Anchor SOH-CAH-TOA to a clearly-labeled right triangle, and ALWAYS mark the angle "
            "you are working from before naming opposite/adjacent. Derive the 45-45-90 and "
            "30-60-90 ratios once so they are understood, not just memorized. Real "
            "elevation/depression problems (ladder, ramp, shadow) motivate it."
        ),
        "progression": "find a hypotenuse with the Pythagorean theorem  ->  check a triangle with the converse  ->  a 45-45-90 side ratio  ->  set up tan to find a side  ->  use inverse trig to find an angle  ->  an angle-of-elevation word problem",
    },
    6: {
        "misconceptions": (
            "confusing a CENTRAL angle (equals its arc) with an INSCRIBED angle (equals HALF "
            "its arc); mixing up radius and diameter (using d where r belongs); forgetting a "
            "tangent is perpendicular to the radius at the point of tangency; confusing arc "
            "MEASURE (degrees) with arc LENGTH (units); confusing sector area with arc length."
        ),
        "how_to_teach": (
            "Draw and label a real circle. Show the inscribed-angle 'half the arc' rule by "
            "dragging the vertex around the circle while the angle stays half its intercepted "
            "arc. Tie arc length and sector area to FRACTIONS of the full circumference/area."
        ),
        "progression": "name the parts of a circle  ->  central angle from its arc  ->  inscribed angle = half the arc  ->  tangent-radius right angle  ->  arc length as a fraction of the circumference  ->  equation of a circle from center and radius",
    },
    7: {
        "misconceptions": (
            "distance-formula slips -- forgetting to SQUARE the differences, or subtracting in "
            "an inconsistent order; taking slope as run over rise; thinking perpendicular lines "
            "have EQUAL slopes (they are negative reciprocals); finding a midpoint by "
            "SUBTRACTING instead of AVERAGING the coordinates."
        ),
        "how_to_teach": (
            "Show that the distance formula IS the Pythagorean theorem on the grid -- draw the "
            "right triangle under the segment. Plot every result to check the algebra against "
            "the picture. Parallel = equal slope; perpendicular = negative reciprocal."
        ),
        "progression": "distance between two points  ->  midpoint of a segment  ->  slope to test parallel  ->  negative reciprocal for perpendicular  ->  a short coordinate proof  ->  equation of a circle from center and radius",
    },
    8: {
        "misconceptions": (
            "mixing up AREA and PERIMETER; using slant height where the vertical height is "
            "needed (or vice versa); forgetting the 1/3 in pyramid/cone volume; dropping or "
            "mismatching units (square vs cubic); using the diameter in place of the radius in "
            "circle formulas; assuming volume scales like length (it scales by k^3)."
        ),
        "how_to_teach": (
            "Decompose a complex shape into known pieces. UNFOLD a solid into its net to see "
            "where the surface-area formula comes from. Keep units attached to every number. "
            "Real modeling (how much paint, how much water, population density) grounds it."
        ),
        "progression": "area of a triangle/parallelogram  ->  area of a circle  ->  a composite-figure area  ->  volume of a prism  ->  volume of a cone (the 1/3)  ->  surface area from a net  ->  a density modeling problem",
    },
    9: {
        "misconceptions": (
            "assuming events are INDEPENDENT when they are not; ADDING probabilities of "
            "non-mutually-exclusive events without subtracting the overlap; confusing "
            "P(A and B) with P(A or B); reversing a conditional -- P(A|B) vs P(B|A)."
        ),
        "how_to_teach": (
            "Two-way tables make conditional probability concrete: restrict to the row or "
            "column you are 'given'. Simple simulations (cards, dice) to feel independence vs "
            "dependence. The addition rule with the overlap subtracted out; the multiplication "
            "rule for 'and'."
        ),
        "progression": "list a sample space  ->  probability of a single event  ->  P(A or B) with overlap  ->  read a conditional probability off a two-way table  ->  test whether two events are independent",
    },
}

_GEOMETRY_CROSS_CUTTING = """\
ERROR WATCH-LIST (catch these all year, in every unit):
- Given vs. appearance: only marked or derived facts count -- never assume from how a figure looks.
- Congruent vs. similar vs. equal: congruent = same size AND shape; similar = same shape, proportional; equal = same number.
- Correspondence: match parts in the right order (CPCTC, proportions) -- the order carries meaning.
- Non-criteria: AAA and SSA do NOT prove triangle congruence.
- Scale factor: lengths scale by k, AREAS by k^2, VOLUMES by k^3.
- Right-triangle tools only on right triangles: the Pythagorean theorem and SOH-CAH-TOA need a right angle.
- Radius vs. diameter, and degrees (arc measure) vs. length (arc length) -- check which the formula wants.
- Units: length is units, area is units squared, volume is units cubed -- keep them attached.
- Every step needs a reason: a picture is evidence, not a proof."""

# -----------------------------------------------------------------------------
# PRE-ALGEBRA -- per-unit pedagogy (distilled from PreAlgebra_Curriculum_KB.md). The
# foundations/remediation course; anxious learners are common, so lean HARD on the
# universal METHODOLOGY (safety, a quick early win, concrete-before-abstract).
# -----------------------------------------------------------------------------
_PREALGEBRA_UNIT_NAMES = {
    1: "Number Sense & Order of Operations",
    2: "Factors, Multiples & Primes",
    3: "Integers & Negative Numbers",
    4: "Fractions",
    5: "Decimals",
    6: "Ratios, Rates & Proportions",
    7: "Percents",
    8: "Measurement & Geometry Basics",
    9: "Variables & Expressions",
}

_PREALGEBRA_UNIT_PEDAGOGY = {
    1: {
        "misconceptions": (
            "going left-to-right regardless of operation (3 + 2 x 4 read as 20 instead of 11); "
            "ignoring parentheses; treating multiply/divide (or add/subtract) as strictly one "
            "before the other instead of left-to-right within each pair."
        ),
        "how_to_teach": (
            "PEMDAS as rules everyone AGREES on so we all get the same answer. Underline the piece "
            "to do FIRST at each step; estimate first to sanity-check the result."
        ),
        "progression": "3 + 2 x 4  ->  (3 + 2) x 4  ->  12 - 4 / 2  ->  2 x (5 + 3^2)",
    },
    2: {
        "misconceptions": (
            "confusing factors (numbers that divide IN) with multiples (skip-counting UP); thinking "
            "1 is prime; mixing up GCF (biggest shared factor) with LCM (smallest shared multiple)."
        ),
        "how_to_teach": (
            "Factor pairs / factor rainbows; factor TREES for prime factorization. Connect GCF -> "
            "simplifying fractions and LCM -> common denominators so the skill pays off right away."
        ),
        "progression": "factors of 12  ->  primes under 20  ->  GCF of 12 and 18  ->  LCM of 4 and 6  ->  prime-factorize 60",
    },
    3: {
        "misconceptions": (
            "thinking -3 is bigger than -1; over-applying 'two negatives make a positive' to "
            "ADDITION; -3^2 vs (-3)^2; getting stuck subtracting a negative."
        ),
        "how_to_teach": (
            "Number line + a money/temperature story (owe vs have, above vs below zero). "
            "'Subtract = add the opposite.' Steady, low-stakes reps until the sign rules are automatic. "
            "This is the single biggest algebra-readiness gap -- worth extra time."
        ),
        "progression": "order -5, 2, -1  ->  |-7|  ->  -4 + 9  ->  3 - 8  ->  -6 - (-2)  ->  -3 x 4  ->  -12 / -3",
    },
    4: {
        "misconceptions": (
            "adding denominators (1/2 + 1/3 = 2/5); thinking you need a common denominator to "
            "MULTIPLY; flipping the wrong fraction when dividing; assuming a bigger denominator "
            "means a bigger fraction."
        ),
        "how_to_teach": (
            "Fraction-of-a-whole bars/pictures; equivalence by multiplying by a form of 1; tie common "
            "denominators back to the LCM. 'Dividing by a fraction = how many of them fit.'"
        ),
        "progression": "simplify 8/12  ->  compare 1/2 and 2/5  ->  1/2 + 1/3  ->  3/4 x 2/3  ->  3/4 / (1/2)  ->  2 1/3 + 1 1/2",
    },
    5: {
        "misconceptions": (
            "'more digits = bigger' (thinking 0.45 > 0.5); not lining up the decimal point when "
            "adding/subtracting; misplacing the point when multiplying or dividing."
        ),
        "how_to_teach": (
            "Place-value columns and MONEY; line up the points for + and -; count decimal places for x; "
            "estimate to catch point-placement slips. Connect decimals <-> fractions <-> percents."
        ),
        "progression": "compare 0.5 and 0.45  ->  round 3.678  ->  2.4 + 1.35  ->  0.6 x 0.3  ->  4.5 / 0.5  ->  0.75 = 3/4",
    },
    6: {
        "misconceptions": (
            "writing a ratio in the wrong order; ADDING across a proportion instead of using equal "
            "ratios; dropping the unit in a rate."
        ),
        "how_to_teach": (
            "Ratio tables and 'per one' (the unit rate); solve proportions by scaling the table or "
            "cross-multiplying. Ground it in real contexts -- recipes, miles per hour, prices."
        ),
        "progression": "simplify the ratio 6:8  ->  unit rate of $12 for 3 lb  ->  solve 2/3 = x/12  ->  scale a recipe for 4 up to 10",
    },
    7: {
        "misconceptions": (
            "reading 50% as 50 instead of 0.5; forgetting to convert the percent before multiplying; "
            "ADDING the percent instead of computing the increase; confusing percent points with "
            "percent change."
        ),
        "how_to_teach": (
            "Percent = 'out of 100'; benchmark percents (10%, 25%, 50%) for estimating; 'of means "
            "multiply.' Real money -- a 20%-off sale, a tip, tax, simple interest."
        ),
        "progression": "25% = 0.25 = 1/4  ->  20% of 80  ->  15% tip on $40  ->  $50 marked up 10%  ->  30% off a $60 item",
    },
    8: {
        "misconceptions": (
            "mixing up perimeter (around) with area (inside); wrong units (square vs linear); using "
            "the diameter where the radius belongs; taking an 'average' without adding first."
        ),
        "how_to_teach": (
            "Grid squares to SEE area; keep units attached to every number; real objects (a room, a "
            "garden). Mean as a 'fair share' -- add up, split evenly."
        ),
        "progression": "perimeter of a 4 by 6 rectangle  ->  its area  ->  area of a triangle  ->  area of a circle with radius 3  ->  mean of 4, 8, 6",
    },
    9: {
        "misconceptions": (
            "reading 3x as 3 + x; combining unlike terms (2x + 3 becoming 5x); 'solving' by moving a "
            "number without doing the same to BOTH sides."
        ),
        "how_to_teach": (
            "A 'mystery number' box for a variable; substitute-and-compute to evaluate; sort like terms "
            "into piles; a one-step equation as 'undo what was done to x.' This unit hands straight off "
            "to Algebra I -- name that bridge for them."
        ),
        "progression": "write '5 more than n'  ->  evaluate 2x + 1 at x = 3  ->  combine 3x + 2 + x  ->  solve x + 5 = 12  ->  solve 3x = 15",
    },
}

_PREALGEBRA_CROSS_CUTTING = """\
ERROR WATCH-LIST (catch these across every unit):
- Order of operations everywhere, not just Unit 1.
- Negative signs (Unit 3) leak into fractions, decimals, and expressions -- watch them constantly.
- "Of" means multiply (fractions, percents).
- Keep the units attached (measurement, rates).
- Estimate to sanity-check -- a quick estimate catches decimal-point and sign slips.
- Convert before you compute (percent -> decimal, mixed -> improper, unlike -> like).
- Meet an anxious learner with a quick early WIN, and separate "this is hard" from "I can't do this." """

# -----------------------------------------------------------------------------
# ALGEBRA II -- per-unit pedagogy (distilled from AlgebraII_Curriculum_KB.md). The rung above
# Geometry; students are ready for abstraction (lean toward the 14-16 METHODOLOGY dials), but weak
# Algebra I foundations (signs, factoring, fractions) resurface -- still engineer wins.
# -----------------------------------------------------------------------------
_ALGEBRA2_UNIT_NAMES = {
    1: "Foundations & Systems",
    2: "Quadratic Functions & Complex Numbers",
    3: "Polynomial Functions",
    4: "Rational Expressions & Functions",
    5: "Radicals & Rational Exponents",
    6: "Exponential & Logarithmic Functions",
    7: "Sequences & Series",
    8: "Trigonometric Functions",
    9: "Statistics & Probability",
}

_ALGEBRA2_UNIT_PEDAGOGY = {
    1: {
        "misconceptions": (
            "dropping the second case of |x| = 5 (giving only x = 5); forgetting to FLIP an "
            "inequality when multiplying/dividing by a negative; in a 3-variable system, losing "
            "track of which variable was eliminated; treating an inconsistent 'no solution' "
            "system as a mistake."
        ),
        "how_to_teach": (
            "Reuse the balance / 'do the same thing to both sides' picture from Algebra I. Graph a "
            "2x2 system so the intersection is SEEN before pushing to elimination; solve a "
            "3-variable system by reducing it to a 2-variable one, then to one. Absolute value = "
            "distance from zero, so it splits into two cases."
        ),
        "progression": "3(x - 2) = 2x + 5  ->  -2x + 1 > 9 (flip!)  ->  |x - 3| = 7  ->  a 2x2 system by elimination  ->  a 3x3 system  ->  a mixture word-problem system",
    },
    2: {
        "misconceptions": (
            "sqrt(-9) = 3i, not 'undefined'; sqrt(16) = 4 (the +/- comes from SOLVING x^2 = 16); "
            "sign slips in the quadratic formula (the -b and the 2a denominator); reading vertex "
            "form backwards (y = (x - 3)^2 shifts RIGHT 3); assuming every quadratic factors."
        ),
        "how_to_teach": (
            "Build the solving ladder deliberately: factoring (zero-product) -> square roots -> "
            "completing the square -> the quadratic formula (the formula IS completing the square "
            "done once for all). Connect the parabola's x-intercepts to real roots and a negative "
            "discriminant to complex roots. Introduce i as 'the number whose square is -1,' then do "
            "complex arithmetic like binomials with i^2 = -1."
        ),
        "progression": "vertex of y = x^2 - 4x + 1  ->  x^2 + 5x + 6 = 0 (factor)  ->  x^2 - 6x + 5 = 0 (complete the square)  ->  2x^2 + 3x - 2 = 0 (formula)  ->  simplify sqrt(-49)  ->  (3 + 2i) + (1 - 5i)  ->  (2 + i)(2 - i)",
    },
    3: {
        "misconceptions": (
            "(x + y)^2 = x^2 + y^2 (missing the 2xy); sign errors in synthetic division or setting "
            "up the wrong divisor; thinking a degree-n polynomial has n REAL zeros (it has n over "
            "the complex numbers, counting multiplicity); ignoring multiplicity when sketching (an "
            "even root touches the axis, an odd root crosses)."
        ),
        "how_to_teach": (
            "Keep the box/area model for multiplying AND factoring. Teach long division for the "
            "meaning, then synthetic division as the shortcut. 'A zero is an x-intercept is a "
            "factor' (the Factor Theorem). Read end behavior straight off degree (even/odd) and "
            "leading coefficient (+/-); use multiplicity to predict touch-vs-cross before plotting."
        ),
        "progression": "(2x^2 + 3x - 1) + (x^2 - x + 4)  ->  factor x^3 - 8 (difference of cubes)  ->  divide (x^3 - 2x^2 - 5x + 6) by (x - 1)  ->  confirm a zero with the Factor Theorem  ->  find all zeros of a cubic  ->  describe end behavior and sketch",
    },
    4: {
        "misconceptions": (
            "canceling a TERM across a + (x/(x+2) is NOT 1/2); thinking you need an LCD to MULTIPLY "
            "(only +/- need it); dropping domain restrictions after simplifying (a canceled factor "
            "leaves a HOLE); missing extraneous solutions that make a denominator zero."
        ),
        "how_to_teach": (
            "'Factor everything first' is the universal opening move -- it exposes canceling, LCDs, "
            "and asymptotes. You may cancel a FACTOR, never a TERM. Tie a zero denominator to a "
            "vertical asymptote or a hole, and check every solution against that forbidden set. "
            "Graph by locating the restrictions first, then the asymptotes."
        ),
        "progression": "simplify (x^2 - 4)/(x^2 + 5x + 6)  ->  (3/x)(x^2/6)  ->  1/x + 1/(x + 1)  ->  solve 2/(x - 1) = 3/x (check!)  ->  asymptotes/holes of (x - 2)/(x^2 - 4)  ->  graph 1/(x - 1)",
    },
    5: {
        "misconceptions": (
            "sqrt(x + y) = sqrt(x) + sqrt(y) (roots don't distribute over +/-); confusing x^(1/2) "
            "with x^2; forgetting that squaring both sides can introduce extraneous solutions; "
            "sqrt(x^2) = |x| for an even root; losing the domain of an even-index radical."
        ),
        "how_to_teach": (
            "Anchor a^(1/n) as 'the number whose nth power is a,' then rational exponents as 'root, "
            "then power.' Show WHY radical-equation answers must be checked (return to the squaring "
            "step). Connect y = sqrt(x) to y = x^2 reflected -- an inverse relationship -- to "
            "explain the restricted domain."
        ),
        "progression": "write the 4th root of x^3 as a power  ->  simplify sqrt(50)  ->  27^(2/3)  ->  sqrt(12) + sqrt(27)  ->  rationalize 1/sqrt(2)  ->  solve sqrt(x + 3) = x - 3 (check!)  ->  graph y = sqrt(x - 2)",
    },
    6: {
        "misconceptions": (
            "log(a + b) = log a + log b (the laws are about products/quotients, not sums); "
            "confusing natural log with base-10; thinking an exponential can be zero or negative "
            "(its range is y > 0 with a horizontal asymptote); mixing up growth (base > 1) and "
            "decay (0 < base < 1); forgetting a log's argument must be positive."
        ),
        "how_to_teach": (
            "Introduce a logarithm as the question 'what exponent gives this?' -- literally the "
            "inverse of the exponential -- and keep converting back and forth between the two "
            "forms. Derive each log law from an exponent law. Use doubling / half-life stories so "
            "growth vs decay is felt. Check every log-equation answer against the positive-argument "
            "domain (extraneous solutions are common)."
        ),
        "progression": "rewrite 2^3 = 8 as log_2(8) = 3  ->  graph y = 2^x (asymptote y = 0)  ->  expand log(xy^2)  ->  solve 3^x = 20 (take a log)  ->  solve log_2(x) + log_2(x - 2) = 3 (check the domain)  ->  a compound-interest / half-life model",
    },
    7: {
        "misconceptions": (
            "confusing the common difference (you ADD it) with the common ratio (you MULTIPLY by "
            "it); off-by-one in the nth-term rule (the first term is n = 1, so a_n = a_1 + "
            "(n - 1)d); mixing up a sequence (the list) with a series (the sum); misreading the "
            "bounds in sigma notation."
        ),
        "how_to_teach": (
            "Build both formulas from a small table so the pattern is visible before the symbols. "
            "Contrast arithmetic (repeated adding = linear) with geometric (repeated multiplying = "
            "exponential), tying back to Unit 6. Expand a sigma expression term-by-term the first "
            "few times so the notation stops being scary."
        ),
        "progression": "next terms of 3, 7, 11, ...  ->  its explicit rule  ->  the 20th term  ->  is 2, 6, 18, ... geometric, and its ratio  ->  sum of the first 10 terms  ->  write a sum in sigma notation  ->  an infinite geometric sum with |r| < 1",
    },
    8: {
        "misconceptions": (
            "the calculator in the wrong mode (degrees vs radians); thinking sine or cosine can "
            "exceed 1; swapping amplitude (vertical stretch) with period (horizontal), and period "
            "= 2*pi/b (not b); putting an angle in the wrong quadrant; treating radians as 'just "
            "another unit' without the arc-length meaning."
        ),
        "how_to_teach": (
            "Start from the right-triangle SOH-CAH-TOA the student met in Geometry, then EXTEND it "
            "to the unit circle so the ratios keep working past 90 degrees. Read (cos, sin) as the "
            "coordinates around the circle. Graph sine by unwrapping the circle's height. Derive "
            "the Pythagorean identity sin^2 + cos^2 = 1 from x^2 + y^2 = 1 on the unit circle."
        ),
        "progression": "convert 90 degrees to radians (pi/2)  ->  sin and cos of 30, 45, 60 from the unit circle  ->  place 210 degrees and give its reference angle  ->  amplitude and period of y = 3sin(2x)  ->  graph it  ->  verify sin^2 + cos^2 = 1 for a known angle",
    },
    9: {
        "misconceptions": (
            "assuming every distribution is normal; treating correlation as causation; confusing a "
            "parameter (population) with a statistic (sample); adding probabilities of "
            "non-mutually-exclusive events without subtracting the overlap; reversing a conditional "
            "-- P(A|B) vs P(B|A)."
        ),
        "how_to_teach": (
            "Read center and spread off real data and dot/box plots before any formula. Make the "
            "normal model concrete with the empirical rule (68-95-99.7) and a z-score as 'how many "
            "standard deviations out.' Use quick simulations (coins, cards, a spinner) to feel "
            "randomness and estimate probability. Two-way tables make conditional probability "
            "visible; keep hammering correlation is not causation."
        ),
        "progression": "describe a data set's center and spread  ->  z-score of a value  ->  apply the 68-95-99.7 rule  ->  survey vs experiment vs observational study  ->  simulate to estimate a probability  ->  P(A or B) with overlap  ->  a conditional probability from a two-way table",
    },
}

_ALGEBRA2_CROSS_CUTTING = """\
ERROR WATCH-LIST (catch these all year, in every unit):
- Signs & the quadratic formula: the -b, the 2a denominator, and negatives under the radical are the top slips.
- Distribution & special products: (x + y)^2 = x^2 + 2xy + y^2, NEVER x^2 + y^2.
- Roots and logs do NOT split over + or -: sqrt(x + y) is not sqrt(x) + sqrt(y); log(a + b) is not log a + log b.
- Factor first: the opening move for quadratics, polynomials, rationals, and radicals -- cancel a FACTOR, never a TERM.
- Extraneous solutions: squaring (radicals), clearing denominators (rationals), and log domains can add answers that fail the original -- always check back.
- Domain: even-index radicals, rational functions (no zero denominator), and logs (positive argument) all restrict the domain -- state it.
- Inverses: logs undo exponentials, roots undo powers -- spotting inverse pairs unlocks Units 5, 6, and 8.
- Function fluency: move among table, graph, equation, and words; know how a, b, h, k shift/stretch/reflect a parent graph."""

# -----------------------------------------------------------------------------
# TRIG / PRE-CALC -- per-unit pedagogy (distilled from PreCalc_Curriculum_KB.md). The rung above
# Algebra II; students are ready for abstraction (14-16 dials), but weak Algebra II foundations
# (factoring, logs, basic trig) resurface -- shore them up briefly, then push on. Trig is the spine.
# -----------------------------------------------------------------------------
_PRECALC_UNIT_NAMES = {
    1: "Functions & Their Graphs",
    2: "Polynomial & Rational Functions",
    3: "Exponential & Logarithmic Functions",
    4: "Trigonometric Functions",
    5: "Analytic Trigonometry",
    6: "Applications of Trigonometry",
    7: "Conic Sections & Parametric Equations",
    8: "Sequences, Series & the Binomial Theorem",
    9: "Introduction to Limits",
}

_PRECALC_UNIT_PEDAGOGY = {
    1: {
        "misconceptions": (
            "composing in the wrong order (f(g(x)) means g FIRST); assuming every function has an "
            "inverse (it must be one-to-one); reading transformations backwards (y = f(x - 3) shifts "
            "RIGHT 3, y = f(x) + 2 shifts UP); confusing domain with range."
        ),
        "how_to_teach": (
            "One transformation lens (a, b, h, k) across the parent-function library. A chained "
            "function machine for composition -- g's output feeds f. The horizontal line test for "
            "invertibility; find an inverse by swapping x and y and solving, then CHECK f(f^-1(x)) = "
            "x. Keep moving among table, graph, equation, and words."
        ),
        "progression": "domain of sqrt(x - 2)  ->  evaluate f(g(2))  ->  find (f o g)(x)  ->  shift/stretch a parent graph  ->  decide if a function is one-to-one  ->  find and verify an inverse",
    },
    2: {
        "misconceptions": (
            "expecting n REAL zeros (it's n over the complex numbers, with multiplicity); ignoring "
            "multiplicity when sketching (even root touches, odd root crosses); confusing a vertical "
            "asymptote (zero denominator) with a horizontal one (end behavior); missing a HOLE from a "
            "common factor."
        ),
        "how_to_teach": (
            "End behavior from degree parity + the leading sign; multiplicity -> touch vs cross. For "
            "rationals: FACTOR FIRST, then domain restrictions, then vertical asymptotes/holes, then "
            "the horizontal asymptote by comparing degrees (num<den -> y=0; equal -> ratio of leads; "
            "num>den -> none/oblique). A sign chart to sketch."
        ),
        "progression": "end behavior of a quartic  ->  zeros + multiplicity, sketch  ->  vertical asymptotes & holes of a rational  ->  horizontal asymptote by degree comparison  ->  sketch it  ->  find all zeros including complex",
    },
    3: {
        "misconceptions": (
            "log(a + b) = log a + log b (the laws are for products/quotients, not sums); confusing ln "
            "with base-10 log; forgetting a log's positive-argument domain; treating e as 'just a "
            "button' instead of a growth constant."
        ),
        "how_to_teach": (
            "A logarithm as 'what exponent gives this?' -- the inverse of the exponential -- converting "
            "back and forth. Derive each log law from an exponent law; change of base = log/log. Model "
            "with P e^(rt) and half-life. Check every log-equation answer against the domain. Graph an "
            "exponential (asymptote y = 0) and its inverse log (asymptote x = 0)."
        ),
        "progression": "rewrite exp <-> log form  ->  expand/condense with the log laws  ->  change of base to evaluate log_5(20)  ->  solve 3^x = 40  ->  solve log_2(x) + log_2(x - 2) = 3 (check!)  ->  a continuous-growth model",
    },
    4: {
        "misconceptions": (
            "the calculator in the wrong mode (degrees vs radians); thinking sine or cosine can exceed "
            "1; swapping amplitude (vertical) with period (period = 2*pi/b); phase-shift sign/direction; "
            "quadrant sign errors; treating a radian as 'just a unit.'"
        ),
        "how_to_teach": (
            "Extend right-triangle SOH-CAH-TOA to the unit circle so the ratios keep working past 90 "
            "degrees; read (cos, sin) as the coordinates; walk the circle for exact values. Graph sine "
            "by unwrapping the circle's height; amplitude = |a|, period = 2*pi/b, midline = d, phase = "
            "-c/b. Use ASTC for signs."
        ),
        "progression": "convert degrees <-> radians  ->  exact values at 30/45/60 and multiples  ->  reference angle & sign in a quadrant  ->  amplitude/period/midline of y = a sin(bx + c) + d  ->  graph one period  ->  model periodic data",
    },
    5: {
        "misconceptions": (
            "treating an IDENTITY like an equation -- you VERIFY it by transforming one side, you don't "
            "'solve' it; dropping solutions when solving a trig equation (solutions repeat every "
            "period); sign errors in the sum/difference and double-angle formulas; forgetting the "
            "restricted RANGE of inverse trig functions."
        ),
        "how_to_teach": (
            "The three Pythagorean identities plus reciprocal/quotient. Verify an identity by "
            "transforming ONE side to match the other. Derive double-/half-angle from sum/difference. "
            "Solve a trig equation by isolating the function, reading ALL solutions on [0, 2pi) off the "
            "unit circle, then adding the period. Respect inverse-trig ranges."
        ),
        "progression": "simplify with a Pythagorean identity  ->  verify an identity  ->  use a sum formula sin(A + B)  ->  a double-angle cos(2θ)  ->  solve 2 sin x - 1 = 0 on [0, 2pi)  ->  evaluate sin(arccos(3/5))",
    },
    6: {
        "misconceptions": (
            "using right-triangle trig on a NON-right triangle; mishandling the ambiguous (SSA) case of "
            "the Law of Sines; choosing the wrong law (AAS/ASA/SSA -> Sines; SAS/SSS -> Cosines); vector "
            "magnitude/direction slips; polar <-> rectangular conversion errors."
        ),
        "how_to_teach": (
            "Pick the law by the given info; watch the ambiguous case. Area = 1/2 a b sin C. Vectors as "
            "components with magnitude sqrt(x^2 + y^2) and direction, added tip-to-tail. Convert with x "
            "= r cos(theta), y = r sin(theta); plot polar points."
        ),
        "progression": "solve a triangle with the Law of Sines (AAS)  ->  the ambiguous SSA case  ->  the Law of Cosines (SAS)  ->  area with 1/2 a b sin C  ->  a vector's magnitude & direction  ->  convert a point polar <-> rectangular",
    },
    7: {
        "misconceptions": (
            "mixing up ellipse (sum, +) and hyperbola (difference, -) forms; confusing a (vertices), b, "
            "and c (foci; c^2 = a^2 +/- b^2); which axis is major; a parabola's focus vs directrix; "
            "eliminating the parameter incorrectly."
        ),
        "how_to_teach": (
            "Derive each conic from its distance definition; standard forms and how (h, k) translate "
            "the center/vertex; identify a conic by the equation's sign pattern. For parametric, make a "
            "t-table then eliminate t to get the rectangular relation."
        ),
        "progression": "identify a conic from its equation  ->  center/vertices/foci of an ellipse  ->  asymptotes of a hyperbola  ->  vertex/focus/directrix of a parabola  ->  graph parametric equations from a t-table  ->  eliminate the parameter",
    },
    8: {
        "misconceptions": (
            "confusing the common difference (add) with the common ratio (multiply); off-by-one in the "
            "nth-term rule; sequence (the list) vs series (the sum); misreading sigma bounds; forgetting "
            "an infinite geometric series converges only for |r| < 1; binomial-coefficient/factorial "
            "errors."
        ),
        "how_to_teach": (
            "Build rules from a small table; arithmetic = linear, geometric = exponential. Finite-sum "
            "formulas; a/(1 - r) for the infinite geometric sum when |r| < 1. Expand sigma term-by-term. "
            "The Binomial Theorem via Pascal's triangle and nCk; permutations vs combinations."
        ),
        "progression": "nth term of an arithmetic sequence  ->  sum of a finite geometric series  ->  an infinite geometric sum  ->  expand sigma notation  ->  expand (x + y)^4 with the Binomial Theorem  ->  a combinations count",
    },
    9: {
        "misconceptions": (
            "thinking the limit EQUALS the function value -- it's about APPROACH, not the point; "
            "confusing one-sided and two-sided limits; believing a hole means no limit (a removable "
            "discontinuity still has one); treating infinity as a number; blindly substituting at a "
            "discontinuity."
        ),
        "how_to_teach": (
            "'Where is it headed?' numerically (a table approaching from both sides) and graphically. "
            "Direct substitution when continuous; factor/cancel for a 0/0 form. One-sided limits. "
            "Continuity = no holes/jumps/asymptotes (draw it without lifting your pencil). The secant "
            "slope -> the tangent slope as a limit (the derivative idea)."
        ),
        "progression": "estimate a limit from a table  ->  a limit from a graph (incl. one-sided)  ->  evaluate by substitution  ->  a 0/0 limit by factoring  ->  decide continuity at a point  ->  average rate of change  ->  the idea of the instantaneous rate",
    },
}

_PRECALC_CROSS_CUTTING = """\
ERROR WATCH-LIST (catch these all year, in every unit):
- Know the unit circle cold; work in RADIANS by default; check the calculator's mode.
- Identities are VERIFIED (transform one side); equations are SOLVED (give ALL solutions, add the period).
- The function lens -- domain, transformation, inverse -- applies to every family.
- Factor first; roots and logs do NOT distribute over + or -; check domains (logs' positive argument, even roots, no zero denominator).
- Polynomials: multiplicity (touch vs cross) and end behavior. Rationals: compare degrees for the horizontal asymptote.
- Conics: ellipse is a SUM (+), hyperbola is a DIFFERENCE (-); c^2 = a^2 +/- b^2.
- A limit is about APPROACH, not the value at the point (a hole can still have a limit)."""

# -----------------------------------------------------------------------------
# PROBABILITY & STATISTICS -- per-unit pedagogy (distilled from ProbStat_Curriculum_KB.md). A
# data-literacy course; reward REASONING about data over computation, and ALWAYS show the picture
# (the tutor has bar/histogram/dot/box plots, scatter+fit, the normal curve, two-way tables, trees).
# -----------------------------------------------------------------------------
_PROBSTAT_UNIT_NAMES = {
    1: "Exploring Data",
    2: "Describing Distributions",
    3: "Scatterplots & Correlation",
    4: "Collecting Data",
    5: "Probability Basics",
    6: "Conditional Probability & Independence",
    7: "Random Variables & Expected Value",
    8: "The Normal Distribution",
    9: "Sampling & Inference",
}

_PROBSTAT_UNIT_PEDAGOGY = {
    1: {
        "misconceptions": (
            "confusing categorical with quantitative data; using a bar chart for numeric data (that's "
            "a histogram's job); reading a taller bar as a higher RATE when it's a COUNT."
        ),
        "how_to_teach": (
            "Sort the variable FIRST: categorical -> bar/pie chart; quantitative -> dot plot / "
            "histogram. Describe every distribution by SHAPE, CENTER, SPREAD, and outliers. Use real "
            "data and draw it ([[bars]], [[histogram]], [[dotplot]], [[pie]])."
        ),
        "progression": "classify a variable  ->  bar chart of categories  ->  dot plot / histogram of numbers  ->  describe the shape",
    },
    2: {
        "misconceptions": (
            "using the mean for skewed data (outliers pull it -- the median is resistant); confusing "
            "range / IQR / standard deviation; thinking SD can be negative; mixing up center and spread."
        ),
        "how_to_teach": (
            "Mean as the balance point, median as the middle value; use the median for skewed data. SD "
            "as the typical distance from the mean. Build the five-number summary and show it as a "
            "[[boxplot]]; pair it with a [[dotplot]] or [[histogram]]."
        ),
        "progression": "mean & median  ->  which to use for skewed data  ->  range & IQR  ->  five-number summary  ->  box plot  ->  interpret standard deviation",
    },
    3: {
        "misconceptions": (
            "correlation implies causation; r near 0 means 'no relationship' (only no LINEAR one); "
            "confusing correlation strength with the slope; extrapolating far beyond the data."
        ),
        "how_to_teach": (
            "Scatterplot first -> describe direction, form, strength; r in [-1, 1], near +/-1 = strong "
            "linear. Fit a least-squares line to PREDICT, then use it. Hammer 'correlation is NOT "
            "causation.' Draw it: [[scatter fit=\"true\"]]."
        ),
        "progression": "build a scatterplot  ->  describe direction/strength  ->  fit a line of best fit  ->  predict with it  ->  correlation vs causation",
    },
    4: {
        "misconceptions": (
            "confusing population vs sample (and parameter vs statistic); thinking a big sample fixes "
            "bias (bias is systematic -- randomization fixes it); assuming an observational study can "
            "prove cause."
        ),
        "how_to_teach": (
            "Population vs sample; random sampling to avoid bias. An EXPERIMENT (treatment + control + "
            "random assignment) vs an OBSERVATIONAL study -- only a randomized experiment supports a "
            "causal claim. Ground it in real study designs."
        ),
        "progression": "identify population & sample  ->  spot sampling bias  ->  survey vs experiment vs observational  ->  the role of randomization  ->  what allows a causal claim",
    },
    5: {
        "misconceptions": (
            "probabilities outside [0, 1]; the gambler's fallacy ('due for' a result); adding "
            "non-mutually-exclusive events without subtracting the overlap; assuming outcomes are "
            "equally likely when they aren't."
        ),
        "how_to_teach": (
            "P(event) = favorable / total for equally-likely outcomes; the complement P(not A) = 1 - "
            "P(A); the addition rule P(A or B) = P(A) + P(B) - P(A and B). Draw a [[pie]] (spinner) or a "
            "[[tree]] to make the sample space concrete."
        ),
        "progression": "list a sample space  ->  P of a single event  ->  complement  ->  P(A or B) mutually exclusive  ->  P(A or B) with overlap",
    },
    6: {
        "misconceptions": (
            "reversing a conditional -- P(A|B) vs P(B|A); assuming independence; multiplying without "
            "checking it; misreading a two-way table."
        ),
        "how_to_teach": (
            "Conditional probability off a [[twoway]] table -- restrict to the given row/column. The "
            "multiplication rule P(A and B) = P(A) P(B|A); test independence with P(A|B) = P(A). Use a "
            "[[tree]] for a sequence of events and read the joint probabilities off the branches."
        ),
        "progression": "conditional off a two-way table  ->  the multiplication rule  ->  test independence  ->  a two-stage tree  ->  P(A and B) via the tree",
    },
    7: {
        "misconceptions": (
            "thinking the expected value must be a POSSIBLE outcome (it's a long-run average); "
            "forgetting to WEIGHT by probability; confusing a probability distribution with a data "
            "distribution."
        ),
        "how_to_teach": (
            "A random variable and its probability distribution (probabilities sum to 1). Expected "
            "value E(X) = sum of x times P(x) -- the probability-weighted average, a LONG-RUN average, "
            "not a guaranteed result. Estimate a probability by simulation. Show the distribution as "
            "[[bars]]."
        ),
        "progression": "build a probability distribution  ->  check probabilities sum to 1  ->  expected value sum of x*P(x)  ->  interpret it as a long-run average  ->  a simple simulation",
    },
    8: {
        "misconceptions": (
            "assuming all data is normal; applying the empirical rule to non-normal data; z-score sign "
            "confusion; confusing area (a proportion) with height."
        ),
        "how_to_teach": (
            "The bell shape; the empirical rule 68-95-99.7. A z-score = (x - mean) / sd = 'how many "
            "standard deviations from the mean.' Area under the curve = a proportion / probability. "
            "Draw it: [[normal shade=\"-1..1\"]] and shade the region you're asking about."
        ),
        "progression": "recognize a normal shape  ->  apply 68-95-99.7  ->  compute a z-score  ->  find the proportion within k SDs  ->  compare values with z-scores",
    },
    9: {
        "misconceptions": (
            "thinking a sample statistic EQUALS the parameter; that a bigger sample adds bias (it "
            "reduces variability); over-reading a confidence interval; ignoring the margin of error."
        ),
        "how_to_teach": (
            "A statistic estimates a parameter. Different samples vary -- the sampling distribution. The "
            "margin of error SHRINKS as n grows. A confidence interval = estimate +/- margin; interpret "
            "it carefully. Show the spread of sample results with a [[dotplot]] or [[normal]]."
        ),
        "progression": "statistic vs parameter  ->  sampling variability  ->  margin of error & sample size  ->  build a confidence interval  ->  interpret it",
    },
}

_PROBSTAT_CROSS_CUTTING = """\
ERROR WATCH-LIST (catch these all through the course):
- Categorical vs quantitative decides the DISPLAY and the SUMMARY.
- Describe a distribution by SHAPE, CENTER, SPREAD, and outliers -- and always show the picture.
- Correlation is NOT causation; only a randomized experiment shows cause.
- Probabilities live in [0, 1]; use complements and subtract overlaps; independence must be CHECKED, not assumed.
- Expected value is a LONG-RUN average, not a guaranteed outcome.
- The empirical rule (68-95-99.7) is for NORMAL distributions only.
- A statistic estimates a parameter WITH uncertainty (sampling variability, margin of error)."""

# -----------------------------------------------------------------------------
# CALCULUS -- per-unit pedagogy (distilled from Calculus_Curriculum_KB.md). The top of the algebra
# ladder. Teach the IDEA before the machinery: every rule should arrive as a shortcut for something
# the student has already seen conceptually.
# -----------------------------------------------------------------------------
_CALCULUS_UNIT_NAMES = {
    1: "Limits & Continuity",
    2: "The Derivative: Definition & Basic Rules",
    3: "Product, Quotient & Chain Rules",
    4: "Applications of Derivatives",
    5: "Curve Sketching & Optimization",
    6: "Antiderivatives & Indefinite Integrals",
    7: "The Definite Integral & the Fundamental Theorem",
    8: "Applications of Integration",
    9: "Introduction to Differential Equations",
}

_CALCULUS_UNIT_PEDAGOGY = {
    1: {
        "misconceptions": (
            "thinking the limit EQUALS the function value (it is about APPROACH); believing a hole "
            "means there is no limit (a removable discontinuity still has one); treating infinity as "
            "a number; substituting into a 0/0 form and calling it undefined."
        ),
        "how_to_teach": (
            "'Where is it headed?' -- a table approaching from BOTH sides, then the graph. Direct "
            "substitution when continuous; factor/cancel (or multiply by the conjugate) for 0/0. "
            "Continuity = you can draw it without lifting your pencil. Limits at infinity by "
            "comparing degrees."
        ),
        "progression": "limit from a table  ->  from a graph (incl. one-sided)  ->  by substitution  ->  a 0/0 limit by factoring  ->  a conjugate limit  ->  classify a discontinuity  ->  a limit at infinity",
    },
    2: {
        "misconceptions": (
            "confusing the AVERAGE rate (secant) with the INSTANTANEOUS rate (tangent); dropping the "
            "limit in the definition; using the power rule on a variable exponent (2^x, x^x); thinking "
            "continuity implies differentiability (a corner is continuous but not differentiable)."
        ),
        "how_to_teach": (
            "Build the secant -> tangent picture until the limit is FELT, then derive the power rule "
            "once from the definition so the shortcut is earned rather than memorized. Always "
            "interpret: 'f'(3) = 5 means at x = 3 it is rising 5 units per unit.' Graph f and f' "
            "together so the relationship is visible."
        ),
        "progression": "average rate of change  ->  the difference quotient  ->  derivative from the definition  ->  the power rule  ->  sums/differences  ->  d/dx of sin, cos, e^x, ln x  ->  the tangent line at a point",
    },
    3: {
        "misconceptions": (
            "thinking (fg)' = f'g' or (f/g)' = f'/g'; FORGETTING THE INNER DERIVATIVE in the chain "
            "rule (the single most common calculus error); reversing the order in the quotient rule's "
            "numerator; forgetting dy/dx when differentiating y implicitly."
        ),
        "how_to_teach": (
            "Make them NAME the outer and inner function out loud before differentiating a composition "
            "('outer is the square, inner is 3x + 1') -- that habit alone prevents the missing-inner-"
            "derivative error. Keep one consistent order for the quotient rule. Implicit "
            "differentiation is just the chain rule applied to y = y(x)."
        ),
        "progression": "product rule  ->  quotient rule  ->  chain rule on one composition  ->  a nested chain  ->  implicit differentiation  ->  the second derivative",
    },
    4: {
        "misconceptions": (
            "plugging in the changing values BEFORE differentiating in a related-rates problem; "
            "confusing speed with velocity (sign); forgetting to differentiate with respect to TIME; "
            "dropping units."
        ),
        "how_to_teach": (
            "Related rates as a strict recipe: draw it, name the variables, write the relating "
            "equation, differentiate WITH RESPECT TO t, and only THEN substitute the instant's values. "
            "Motion: velocity is f', acceleration is f''; the object speeds up when v and a share a "
            "sign. Always state the units of a rate."
        ),
        "progression": "position  ->  velocity  ->  acceleration  ->  interpret a rate with units  ->  a related-rates ladder/balloon problem  ->  linear approximation",
    },
    5: {
        "misconceptions": (
            "assuming every critical point is an extremum (it may be neither); thinking f'' = 0 "
            "guarantees an inflection point (the concavity must actually CHANGE); confusing f' < 0 "
            "with f < 0; forgetting to check ENDPOINTS on a closed interval; optimizing without "
            "writing down the constraint."
        ),
        "how_to_teach": (
            "Sign charts: one for f' (increasing/decreasing) and one for f'' (concavity), then sketch "
            "from them. Optimization as a recipe: write the quantity to optimize, use the constraint "
            "to reduce it to ONE variable, differentiate, test, and answer the question actually asked "
            "-- with units."
        ),
        "progression": "critical points  ->  first derivative test  ->  concavity & inflection  ->  sketch from f'/f''  ->  absolute extrema on a closed interval  ->  an applied optimization (fence/box/can)",
    },
    6: {
        "misconceptions": (
            "forgetting + C; applying the reverse power rule to 1/x (it is ln|x|); pattern-matching "
            "instead of actually substituting; forgetting to change the variable back after a "
            "u-substitution."
        ),
        "how_to_teach": (
            "Antidifferentiation is the question 'what would I have differentiated to get this?' -- "
            "and ALWAYS verify by differentiating the answer back. u-substitution is the chain rule "
            "run backwards: pick u to be the inner function and check that du is present up to a "
            "constant."
        ),
        "progression": "reverse power rule  ->  +C and an initial condition  ->  antiderivatives of sin/cos/e^x/(1/x)  ->  a simple u-substitution  ->  a substitution needing a constant adjustment",
    },
    7: {
        "misconceptions": (
            "thinking a definite integral is always 'the area' (it is SIGNED area -- below the axis "
            "counts negative); evaluating at only one limit, or subtracting in the wrong order; "
            "confusing the definite integral (a NUMBER) with the indefinite (a family); adding + C to "
            "a definite integral."
        ),
        "how_to_teach": (
            "Build rectangles FIRST so the limiting process is felt, then reveal the Fundamental "
            "Theorem as the shortcut -- that contrast is the emotional high point of the course. "
            "Stress the units of an accumulation: if r(t) is gallons per minute, the integral is "
            "gallons."
        ),
        "progression": "left/right Riemann sums  ->  trapezoid  ->  the definite integral as signed area  ->  evaluate with the FTC  ->  accumulated change in context  ->  average value",
    },
    8: {
        "misconceptions": (
            "forgetting 'top minus bottom' (or integrating in the wrong variable); missing an "
            "intersection point that splits the region; forgetting to SQUARE the radius in a volume; "
            "confusing displacement (the integral of v) with total distance (the integral of |v|)."
        ),
        "how_to_teach": (
            "Always sketch the region and mark which curve is on top; find the intersections FIRST. "
            "For a volume, draw the representative slice before writing the integral. Displacement vs "
            "total distance is the classic trap -- teach it deliberately with a velocity graph that "
            "crosses zero."
        ),
        "progression": "area between curves  ->  a region needing a split  ->  disk volume  ->  washer volume  ->  displacement vs total distance  ->  an accumulation word problem",
    },
    9: {
        "misconceptions": (
            "forgetting the constant, or applying the initial condition too late; treating dy/dx as an "
            "ordinary fraction without care; expecting every differential equation to be separable; "
            "confusing the GENERAL solution (a family) with a PARTICULAR one."
        ),
        "how_to_teach": (
            "A differential equation is just 'an equation about a rate.' Verify a candidate solution "
            "by substituting it back in. Separate the variables, integrate both sides, THEN apply the "
            "initial condition to pin down C. A slope field makes the whole family of solutions "
            "visible. Name the hand-off: this is where the Differential Equations course begins."
        ),
        "progression": "verify a solution  ->  read a slope field  ->  solve a separable equation  ->  apply an initial condition  ->  an exponential growth/decay model",
    },
}

_CALCULUS_CROSS_CUTTING = """\
ERROR WATCH-LIST (catch these all year, in every unit):
- A limit is about APPROACH, not the value at the point (a hole can still have a limit).
- The chain rule's INNER DERIVATIVE is the most-forgotten step in all of calculus -- name outer and inner first.
- + C on every indefinite integral; a definite integral is a NUMBER (no + C).
- INTERPRET, WITH UNITS: a derivative is a rate of something per something; an integral is an accumulated amount.
- Sketch it: sign charts for f' and f'', and always draw the region before integrating.
- Verify by reversing: differentiate an antiderivative back; substitute a solution into its equation.
- Continuity does NOT imply differentiability (corners); differentiability DOES imply continuity.
- Signed area: below the axis counts negative; displacement is not total distance."""

# -----------------------------------------------------------------------------
# DIFFERENTIAL EQUATIONS -- per-unit pedagogy (distilled from DiffEq_Curriculum_KB.md). The most
# advanced course in the app; assumes Calculus (especially integration). The habit that decides
# success here is CLASSIFY FIRST -- the method follows from the type.
# -----------------------------------------------------------------------------
_DIFFEQ_UNIT_NAMES = {
    1: "Introduction, Classification & Slope Fields",
    2: "First-Order Equations: Separable & Linear",
    3: "Qualitative Analysis: Equilibria & Stability",
    4: "Numerical Methods: Euler & Runge-Kutta",
    5: "Second-Order Linear: Homogeneous",
    6: "Second-Order: Nonhomogeneous, Vibrations & Resonance",
    7: "Laplace Transforms",
    8: "Linear Systems & the Phase Plane",
    9: "Nonlinear Systems & Stability",
}

# 2026-08-11 (build de): restructured to the CUPM mainstream syllabus. Units 3, 4, 8, 9
# are new or substantially new; 2 merges the old 2+3 (plus exact equations as a brief
# topic); 6 merges the old 6+7. Series solutions dropped, per the CUPM report.
_DIFFEQ_UNIT_PEDAGOGY = {
    1: {
        "misconceptions": (
            "thinking the solution to a differential equation is a NUMBER (it is a function, or a "
            "whole family of them); confusing ORDER (the highest derivative) with degree; calling an "
            "equation linear because it looks simple (linearity is about y and its derivatives, not "
            "about x); forgetting the general solution carries as many constants as the order; "
            "thinking a slope field shows ONE solution (it shows the whole family at once)."
        ),
        "how_to_teach": (
            "Start from a rate the student already believes -- 'the population grows at a rate "
            "proportional to its size' -- and write it symbolically. That IS a differential equation. "
            "Make substituting a candidate solution back in the reflex. Slope fields come EARLY and "
            "stay all course: every little segment is a slope the equation dictates, a solution "
            "curve just follows the arrows, and an initial condition picks one curve out."
        ),
        "progression": "classify order & linearity  ->  verify a solution  ->  general vs particular  ->  read a slope field  ->  sketch a solution through a point  ->  set up a DE from a described rate",
    },
    2: {
        "misconceptions": (
            "forgetting the constant of integration, or adding it AFTER solving for y; dividing by "
            "an expression without noting where it is zero (which loses equilibrium solutions); "
            "forgetting to put a linear equation in STANDARD FORM before building the integrating "
            "factor; dropping the constant in the exponent of mu; forgetting to solve FOR y."
        ),
        "how_to_teach": (
            "Two workhorse methods, and the CLASSIFY-FIRST habit decides between them. Separable: "
            "all the y's with dy on one side, all the x's with dx on the other, integrate BOTH "
            "sides, constant once, solve for y, initial condition LAST -- and ground every model in "
            "a story with units. Linear: show WHY the integrating factor works -- multiplying by mu "
            "makes the left side (mu*y)', so you just integrate. Exact equations get a brief, honest "
            "look: the test is checking whether the equation is a total differential."
        ),
        "progression": "identify separable  ->  separate, integrate, solve for y  ->  growth/decay & cooling  ->  logistic  ->  standard form & the integrating factor  ->  a mixing problem  ->  a brief exact-equation check",
    },
    3: {
        "misconceptions": (
            "thinking every differential equation must be SOLVED to be understood (the whole point "
            "here is what you can know without a formula); reading the phase line as a graph of y "
            "against t; calling an equilibrium stable because solutions exist near it (they must "
            "move TOWARD it); assuming solutions can cross (uniqueness says they cannot)."
        ),
        "how_to_teach": (
            "This is the modern heart of the course. For an autonomous equation, dy/dt depends only "
            "on y -- so mark where dy/dt is zero (the equilibria), test the sign in between, and the "
            "phase line tells you every solution's fate without an integral in sight. Stable pulls "
            "neighbors in; unstable pushes them away; semistable does one on each side. Existence & "
            "uniqueness is the license for all of it: through each point, exactly one solution, so "
            "curves never cross and the phase line's regions are honest."
        ),
        "progression": "spot an autonomous equation  ->  find equilibria  ->  sign-test the phase line  ->  classify stable/unstable/semistable  ->  predict long-term behavior from y(0)  ->  what existence & uniqueness promises",
    },
    4: {
        "misconceptions": (
            "treating the numerical answer as EXACT; thinking a smaller step size is free (it costs "
            "steps, and round-off eventually pushes back); confusing local and global error; "
            "believing numerical methods are a fallback for weak students rather than the working "
            "tool of every engineer whose equation has no formula."
        ),
        "how_to_teach": (
            "Euler's method is one idea repeated: stand at a point, ask the equation for the slope, "
            "step along that tangent line, repeat. Do the first three steps BY HAND in a table -- "
            "x, y, slope, new y -- before any talk of error. Then halve the step size on the same "
            "problem and compare: the error roughly halves, and that observation IS the concept of "
            "order. Improved Euler averages the slope at both ends; Runge-Kutta samples smartly in "
            "the middle and wins big. Frame it honestly: for most real equations this is not the "
            "backup plan, it is the plan."
        ),
        "progression": "the tangent-line step  ->  three Euler steps by hand  ->  halve the step, watch the error  ->  improved Euler  ->  why Runge-Kutta wins  ->  a problem with no closed form",
    },
    5: {
        "misconceptions": (
            "forgetting the extra factor of x in the REPEATED-root case; mishandling complex roots "
            "(the solution is e^(ax)(C1 cos bx + C2 sin bx), not complex exponentials left as-is); "
            "assuming two solutions are independent without checking; applying initial conditions "
            "before writing the full general solution."
        ),
        "how_to_teach": (
            "Motivate the guess y = e^(rx): substitute it and the equation collapses to a polynomial "
            "in r -- that IS the characteristic equation, and it explains why the method works. The "
            "three cases then follow from the discriminant, exactly like the quadratic formula they "
            "already know. The repeated root gets an extra x because you need a SECOND independent "
            "solution."
        ),
        "progression": "characteristic equation  ->  distinct real roots  ->  repeated root (the extra x)  ->  complex roots  ->  apply initial conditions  ->  check independence with the Wronskian",
    },
    6: {
        "misconceptions": (
            "applying the initial conditions to y_c ALONE instead of y_c + y_p (the most common "
            "error in this unit by far); forgetting to multiply the trial solution by x when it "
            "duplicates a term in y_c; picking an incomplete trial form; sign errors setting up the "
            "spring equation; not connecting the three DAMPING cases to the three ROOT cases; "
            "thinking resonance requires exactly zero damping."
        ),
        "how_to_teach": (
            "Teach the ARCHITECTURE first: the general solution is ALWAYS complementary + "
            "particular. Build the trial-form table together, and let them WATCH a guess fail when "
            "it duplicates y_c, so the multiply-by-x rule is discovered rather than memorized. Then "
            "the payoff, in the same unit so the connection cannot be missed: the three damping "
            "cases ARE the three characteristic-root cases, seen physically, and the SAME equation "
            "governs a spring and an RLC circuit -- that is the moment the subject feels powerful. "
            "Transient dies out; steady-state persists; resonance is forcing at the natural "
            "frequency."
        ),
        "progression": "y = y_c + y_p  ->  trial forms (polynomial, exponential, sinusoid)  ->  the overlap case  ->  variation of parameters  ->  a mass-spring equation  ->  the three damping cases  ->  forced motion & resonance  ->  the RLC analogy",
    },
    7: {
        "misconceptions": (
            "forgetting to include the INITIAL CONDITIONS when transforming a derivative (they are "
            "built into the formula -- that is the method's whole advantage); botching partial "
            "fractions; mixing up t-shifts and s-shifts; forgetting to invert back to the time domain "
            "at the end."
        ),
        "how_to_teach": (
            "Sell the payoff first: Laplace turns calculus into ALGEBRA and swallows the initial "
            "conditions automatically, so a nasty initial-value problem becomes a partial-fractions "
            "exercise. Keep the table visible on the board. The answer is not finished until you have "
            "inverted back to y(t)."
        ),
        "progression": "transform basic functions  ->  transform of a derivative (with initial conditions)  ->  solve for Y(s)  ->  partial fractions  ->  invert  ->  a step-function/piecewise forcing problem",
    },
    8: {
        "misconceptions": (
            "confusing eigenvalues WITH solutions (an eigenvalue sets the growth rate; the "
            "eigenvector sets the direction); thinking the phase plane plots y against t (it plots "
            "one variable against the other, with time flowing along the curves); forgetting a 2x2 "
            "system needs TWO independent eigen-solutions; sign errors turning a second-order "
            "equation into a system."
        ),
        "how_to_teach": (
            "Connect straight back to unit 5: turning y'' + ay' + by = 0 into a 2x2 system and "
            "finding eigenvalues reproduces the characteristic equation -- the same idea in new "
            "clothes, which makes eigenvalues feel earned rather than invented. Straight-line "
            "solutions run along eigenvectors; everything else bends between them. The phase "
            "portrait is the qualitative payoff: real eigenvalues make nodes and saddles, complex "
            "ones make spirals, and the signs decide stability."
        ),
        "progression": "second-order equation -> 2x2 system  ->  eigenvalues & eigenvectors  ->  straight-line solutions  ->  the general solution  ->  sketch the phase portrait  ->  classify node/saddle/spiral",
    },
    9: {
        "misconceptions": (
            "expecting a formula (most nonlinear systems have none -- qualitative reasoning IS the "
            "method); treating linearization as exact rather than local; assuming a nonlinear system "
            "behaves like its linear part far from the equilibrium; reading predator-prey axes as "
            "time instead of the two populations."
        ),
        "how_to_teach": (
            "Open with the honest statement: for most nonlinear systems nobody can write the "
            "solution, and yet we can say what happens -- that is the course's closing argument. "
            "Find the equilibria (both right-hand sides zero), linearize at each one (the unit-8 "
            "machinery, reused locally), classify, and stitch the local pictures into a global "
            "phase portrait. Predator-prey makes it real: the closed loops ARE the boom-and-bust "
            "cycles, and the student can narrate a full cycle in plain words -- foxes up, rabbits "
            "down, foxes starve, rabbits recover."
        ),
        "progression": "find equilibria of a system  ->  linearize at each  ->  classify locally  ->  stitch a global portrait  ->  predator-prey  ->  competing species  ->  narrate the model's story",
    },
}

_DIFFEQ_CROSS_CUTTING = """\
ERROR WATCH-LIST (catch these all year, in every unit):
- CLASSIFY FIRST -- order, linear/nonlinear, separable/exact/linear, homogeneous/nonhomogeneous. The method follows from the type.
- A solution is a FUNCTION (a family until an initial condition pins it down); the general solution carries as many constants as the order.
- The constant of integration appears at the INTEGRATION step -- and when rebuilding a potential function it is a FUNCTION of the other variable.
- Apply initial conditions LAST, to the FULL general solution (y_c + y_p, never y_c alone).
- Verify by substituting the solution back into the equation -- always available, and the fastest way to catch an error.
- Weak INTEGRATION is the hidden blocker: if a student stalls, check whether the trouble is the DE method or the integral inside it, and shore that up briefly and without judgment.
- Interpret the model with units and in context -- this is where calculus becomes modeling."""

# =============================================================================
# THE PER-COURSE CATALOG OF TEACHING KNOWLEDGE
# =============================================================================
# =============================================================================
# ENTRY-LEVEL MATH (grades 1-3) teaching brain. Concrete, picture-first arithmetic. Source:
# EntryMath_Curriculum_KB.md. Added 2026-08-03 with the elementary restructure.
# =============================================================================
_ENTRY_UNIT_NAMES = {
    1: "Counting & Number Sense",
    2: "Addition to 20",
    3: "Subtraction to 20",
    4: "Place Value to 1,000",
    5: "Two- & Three-Digit Addition",
    6: "Two- & Three-Digit Subtraction",
    7: "Money — Coins, Bills & Making Change",
    8: "Time, Calendar & Measurement",
    9: "Shapes, Patterns & Groups",
}

_ENTRY_UNIT_PEDAGOGY = {
    1: {
        "misconceptions": (
            "losing track when counting past ten; thinking the last number said is just a label, "
            "not 'how many' (cardinality); reading 23 as 'two, three'; believing a longer row of "
            "objects is 'more' even when the counts are equal."
        ),
        "how_to_teach": (
            "Count REAL objects, touching one per number (one-to-one); the last count tells HOW MANY. "
            "Compare two groups by matching or counting. Use a number line for 'one more / one less'; "
            "skip-count by 2s, 5s, 10s as a rhythm."
        ),
        "progression": "count to 10  ->  count to 30  ->  which is more, 7 or 4  ->  one more than 8  ->  skip-count by 5s to 30",
    },
    2: {
        "misconceptions": (
            "recounting the first number instead of counting ON (3 + 4 recounting 1,2,3 then 4,5,6,7); "
            "starting over every time; not seeing 3 + 4 and 4 + 3 as the same amount."
        ),
        "how_to_teach": (
            "Start with objects, then 'count on' from the BIGGER number. Ten-frames and fingers; "
            "number-line hops; the make-a-ten idea (8 + 5 = 8 + 2 + 3). Link add and subtract as a "
            "fact family."
        ),
        "progression": "2 + 3 with counters  ->  count on 5 + 2  ->  make ten: 8 + 5  ->  3 + 4 vs 4 + 3  ->  7 + 6",
    },
    3: {
        "misconceptions": (
            "thinking subtraction can be flipped like addition (7 - 3 = 3 - 7); counting the wrong "
            "direction; not seeing 'take away' and 'how many more to get there' as the same idea."
        ),
        "how_to_teach": (
            "Act it out by removing objects; 'count back' on the number line; subtraction as the "
            "missing addend (7 - 3 asks 3 + ? = 7), tied to the addition fact family."
        ),
        "progression": "5 take away 2 with objects  ->  count back 9 - 3  ->  missing addend 4 + ? = 10  ->  10 - 7  ->  15 - 8",
    },
    4: {
        "misconceptions": (
            "reading 43 as 'four, three'; thinking the 4 in 43 means four, not forty; teen-number "
            "trouble; not seeing that ten ones bundle into one ten."
        ),
        "how_to_teach": (
            "Bundle ten ones into a ten (sticks / base-ten blocks); a place-value chart "
            "(hundreds | tens | ones); expanded form (43 = 40 + 3); build and read numbers to 1,000."
        ),
        "progression": "show 24 as 2 tens 4 ones  ->  expanded form of 57  ->  which is bigger, 63 or 36  ->  3 hundreds 0 tens 5 ones  ->  round 48 to the nearest ten",
    },
    5: {
        "misconceptions": (
            "not lining up place values; writing a whole two-digit column sum in one column "
            "(9 + 7 = 16 crammed under the ones); forgetting to carry the ten."
        ),
        "how_to_teach": (
            "Stack so ones sit under ones; add the ones first; when a column makes ten or more, CARRY "
            "the ten to the next column. Use the [[column]] tool and base-ten blocks; estimate first."
        ),
        "progression": "24 + 13 (no carry)  ->  28 + 15 (carry)  ->  47 + 36  ->  156 + 27  ->  estimate then add 198 + 47",
    },
    6: {
        "misconceptions": (
            "subtracting the smaller digit from the larger in each column no matter which is on top "
            "(52 - 27 giving 35); forgetting to reduce the digit you borrowed from; borrowing when you "
            "don't need to."
        ),
        "how_to_teach": (
            "Stack and line up; subtract the ones first; if the top digit is too small, BORROW a ten "
            "from the next column (open one ten into ten ones). Base-ten blocks make the trade visible; "
            "check by adding back."
        ),
        "progression": "38 - 12 (no borrow)  ->  52 - 27 (borrow)  ->  70 - 46  ->  204 - 58  ->  check 63 - 28 by adding back",
    },
    7: {
        "misconceptions": (
            "counting coins by how MANY there are instead of by VALUE (three coins = 3 cents); a dime "
            "is smaller than a nickel so 'worth less'; trouble crossing cents to dollars; guessing at "
            "change."
        ),
        "how_to_teach": (
            "Name each coin's value; count a mixed pile starting from the BIGGEST; skip-count (dimes by "
            "10, nickels by 5). Dollars-and-cents with a point, like a price tag. Make change by "
            "counting UP from the price to what was paid."
        ),
        "progression": "value of a dime  ->  count 3 dimes + 2 pennies  ->  a quarter + 2 dimes  ->  is 60 cents enough for a 55-cent item  ->  change from $1 for a 70-cent item",
    },
    8: {
        "misconceptions": (
            "reading only one hand of the clock; thinking the minute hand on the 3 means '3 minutes'; "
            "muddling the order of days/months; measuring without lining up the ruler's zero."
        ),
        "how_to_teach": (
            "Two hands, two jobs: the hour hand points to the hour, the minute hand counts by 5s "
            "around. Do o'clock and half past first. A calendar for days/weeks/months. Measure length "
            "by lining up zero and counting units."
        ),
        "progression": "read 3 o'clock  ->  read half past 6  ->  read 4:15  ->  how many days in a week  ->  measure a pencil to the nearest inch",
    },
    9: {
        "misconceptions": (
            "naming a shape only in one orientation (a turned square called a 'diamond'); confusing "
            "sides with corners; missing the repeating 'core' of a pattern; not seeing equal groups as "
            "the start of multiplication."
        ),
        "how_to_teach": (
            "Name and count sides and corners of 2-D shapes; sort and build them. Find and extend the "
            "repeating core of a pattern. Equal groups and arrays are the first picture of "
            "multiplication (3 groups of 4)."
        ),
        "progression": "triangle vs rectangle  ->  count the sides of a pentagon  ->  extend A A B A A B ...  ->  3 groups of 2 is how many  ->  a 2-by-4 array is how many",
    },
}

_ENTRY_CROSS_CUTTING = """\
ERROR WATCH-LIST (catch these across every unit):
- One-to-one counting -- touch one object per number, and the LAST count is "how many."
- Line up place values in any stacked add/subtract: ones under ones.
- Carry a ten when a column reaches ten (Unit 5); borrow a ten when the top digit is too small (Unit 6).
- Coins are counted by VALUE, not by how many coins there are.
- Read a number by its places (43 is forty-three -- four TENS and three ones), never digit by digit.
- Keep every reply tiny, concrete, and picture-first -- these are our youngest learners.
- Engineer a real, specific win early and often; keep the numbers small until the idea is solid. """

# =============================================================================
# BASIC MATH (grades 4-6) teaching brain. Multi-digit operations, fractions, decimals, an intro
# to ratios/percents, and word problems. Source: BasicMath_Curriculum_KB.md. Added 2026-08-03.
# =============================================================================
_BASIC_UNIT_NAMES = {
    1: "Place Value & Whole-Number Operations",
    2: "Multiplication",
    3: "Division",
    4: "Factors, Multiples, GCF & LCM",
    5: "Fractions — Meaning & Equivalence",
    6: "Fraction Operations",
    7: "Decimals",
    8: "Ratios, Rates & Percents",
    9: "Measurement, Geometry & Word Problems",
}

_BASIC_UNIT_PEDAGOGY = {
    1: {
        "misconceptions": (
            "misreading large numbers and their periods (thousands, millions); rounding to the wrong "
            "place; dropping a place when adding/subtracting multi-digit; thinking an estimate is "
            "'wrong' because it isn't exact."
        ),
        "how_to_teach": (
            "Place-value chart with periods; read in groups of three. Round by looking at the NEXT "
            "digit (5 or more rounds up). Estimate to check reasonableness; line up places for the "
            "standard algorithms."
        ),
        "progression": "read 42,506  ->  round 4,285 to the nearest hundred  ->  estimate 612 + 389  ->  38,214 + 9,057  ->  5,003 - 1,846",
    },
    2: {
        "misconceptions": (
            "shaky basic facts slowing everything down; forgetting the place-holding zero on the "
            "second partial product; adding when the algorithm calls for multiplying; believing "
            "multiplication always makes things 'a lot bigger.'"
        ),
        "how_to_teach": (
            "Arrays and the AREA MODEL to SEE partial products; the distributive idea "
            "(23 x 4 = 20x4 + 3x4); the standard algorithm with the place-holding zero. Estimate first."
        ),
        "progression": "6 x 7 fact  ->  area model 23 x 4  ->  46 x 7  ->  34 x 25  ->  estimate then do 208 x 6",
    },
    3: {
        "misconceptions": (
            "thinking division can be flipped (12 / 3 vs 3 / 12); confusing a remainder with a "
            "decimal; dropping digits in long division; not knowing where the first quotient digit "
            "goes."
        ),
        "how_to_teach": (
            "Division as equal SHARING and as 'how many groups'; connect it to the multiplication "
            "fact family. Long division as divide-multiply-subtract-bring down; interpret the remainder "
            "in context; estimate the quotient first."
        ),
        "progression": "share 12 into 3 groups  ->  fact 56 / 8  ->  84 / 4  ->  long division 96 / 6  ->  135 / 4 with a remainder",
    },
    4: {
        "misconceptions": (
            "confusing factors (numbers that divide IN) with multiples (skip-counting UP); thinking 1 "
            "is prime; mixing up GCF (biggest shared factor) with LCM (smallest shared multiple)."
        ),
        "how_to_teach": (
            "Factor pairs and factor rainbows; factor TREES for prime factorization; list-and-circle "
            "for GCF/LCM. Connect GCF -> simplifying fractions and LCM -> common denominators so it "
            "pays off in the very next unit."
        ),
        "progression": "factors of 24  ->  first five multiples of 6  ->  is 21 prime  ->  GCF of 12 and 18  ->  LCM of 4 and 6",
    },
    5: {
        "misconceptions": (
            "thinking a bigger denominator means a bigger fraction; not seeing a fraction as a real "
            "amount / a point on the number line; assuming equivalent fractions must be different "
            "because they look different."
        ),
        "how_to_teach": (
            "Fraction bars and the number line to SEE size; equivalence by multiplying or dividing by "
            "a form of 1; simplify with the GCF; compare using a common denominator or a benchmark "
            "like one half."
        ),
        "progression": "shade 3/4  ->  place 2/3 on a number line  ->  is 1/2 = 3/6  ->  simplify 8/12  ->  compare 2/3 and 3/5",
    },
    6: {
        "misconceptions": (
            "adding the denominators (1/2 + 1/3 = 2/5); thinking you need a common denominator to "
            "MULTIPLY; flipping the wrong fraction when dividing; forgetting to simplify the answer."
        ),
        "how_to_teach": (
            "Add/subtract needs a common bottom (bars show WHY); multiply tops and bottoms straight "
            "across; divide by multiplying by the reciprocal ('how many fit'); mixed <-> improper. "
            "Always simplify and estimate."
        ),
        "progression": "1/2 + 1/3  ->  5/6 - 1/3  ->  3/4 x 2/3  ->  3/4 / (1/2)  ->  2 1/3 + 1 1/2",
    },
    7: {
        "misconceptions": (
            "'more digits = bigger' (thinking 0.45 > 0.5); not lining up the point for + and -; "
            "misplacing the point in x and /; treating decimals and fractions as unrelated."
        ),
        "how_to_teach": (
            "Place-value columns and MONEY; line up the points for + and -; count decimal places for x; "
            "estimate to catch point slips. Connect decimals <-> fractions <-> percents."
        ),
        "progression": "compare 0.5 and 0.45  ->  round 3.678 to tenths  ->  2.4 + 1.35  ->  0.6 x 0.3  ->  4.5 / 0.5",
    },
    8: {
        "misconceptions": (
            "writing a ratio in the wrong order; ADDING across a proportion instead of using equal "
            "ratios; dropping the unit in a rate; reading 50% as 50 rather than one half."
        ),
        "how_to_teach": (
            "Ratio tables and 'per one' (the unit rate); percent as 'out of 100' with benchmark "
            "percents (10%, 25%, 50%); 'of means multiply.' Ground it in prices, recipes, miles per "
            "hour."
        ),
        "progression": "simplify 6 : 8  ->  unit rate of $12 for 3 lb  ->  25% = 1/4  ->  20% of 80  ->  15% tip on $40",
    },
    9: {
        "misconceptions": (
            "mixing up perimeter (around) with area (inside); wrong units (square vs linear); picking "
            "the wrong operation in a word problem; forgetting to convert units before computing."
        ),
        "how_to_teach": (
            "Grid squares to SEE area; keep units attached; convert BEFORE you compute. A word-problem "
            "routine: understand -> plan (which operation?) -> solve -> check it makes sense. Draw the "
            "situation."
        ),
        "progression": "perimeter of a 4 by 6 rectangle  ->  its area  ->  volume of a 2x3x4 box  ->  convert 3 ft to inches  ->  a two-step word problem",
    },
}

_BASIC_CROSS_CUTTING = """\
ERROR WATCH-LIST (catch these across every unit):
- Line up place values (and the decimal point) in every stacked operation.
- Solid multiplication/division facts unlock fractions, decimals, and long division -- shore them up when they are the real blocker.
- "Of" means multiply (fractions, percents).
- Keep units attached and CONVERT before you compute (measurement, rates).
- Estimate first to sanity-check -- it catches misplaced decimal points and dropped digits.
- Simplify fractions, and interpret a remainder in the context of the problem.
- Word problems: understand it, choose the operation, solve, then check the answer is reasonable. """

COURSE_PEDAGOGY = {
    "entry": {
        "unit_names": _ENTRY_UNIT_NAMES,
        "cross_cutting": _ENTRY_CROSS_CUTTING,
        "units": _ENTRY_UNIT_PEDAGOGY,
    },
    "basic": {
        "unit_names": _BASIC_UNIT_NAMES,
        "cross_cutting": _BASIC_CROSS_CUTTING,
        "units": _BASIC_UNIT_PEDAGOGY,
    },
    "algebra1": {
        "unit_names": _ALGEBRA1_UNIT_NAMES,
        "cross_cutting": _ALGEBRA1_CROSS_CUTTING,
        "units": _ALGEBRA1_UNIT_PEDAGOGY,
    },
    "geometry": {
        "unit_names": _GEOMETRY_UNIT_NAMES,
        "cross_cutting": _GEOMETRY_CROSS_CUTTING,
        "units": _GEOMETRY_UNIT_PEDAGOGY,
    },
    "prealgebra": {
        "unit_names": _PREALGEBRA_UNIT_NAMES,
        "cross_cutting": _PREALGEBRA_CROSS_CUTTING,
        "units": _PREALGEBRA_UNIT_PEDAGOGY,
    },
    "algebra2": {
        "unit_names": _ALGEBRA2_UNIT_NAMES,
        "cross_cutting": _ALGEBRA2_CROSS_CUTTING,
        "units": _ALGEBRA2_UNIT_PEDAGOGY,
    },
    "precalc": {
        "unit_names": _PRECALC_UNIT_NAMES,
        "cross_cutting": _PRECALC_CROSS_CUTTING,
        "units": _PRECALC_UNIT_PEDAGOGY,
    },
    "probstat": {
        "unit_names": _PROBSTAT_UNIT_NAMES,
        "cross_cutting": _PROBSTAT_CROSS_CUTTING,
        "units": _PROBSTAT_UNIT_PEDAGOGY,
    },
    "calculus": {
        "unit_names": _CALCULUS_UNIT_NAMES,
        "cross_cutting": _CALCULUS_CROSS_CUTTING,
        "units": _CALCULUS_UNIT_PEDAGOGY,
    },
    "diffeq": {
        "unit_names": _DIFFEQ_UNIT_NAMES,
        "cross_cutting": _DIFFEQ_CROSS_CUTTING,
        "units": _DIFFEQ_UNIT_PEDAGOGY,
    },
}

# -----------------------------------------------------------------------------
# BACKWARD-COMPATIBLE module-level names (default course = Algebra I). Existing callers
# that reference pedagogy.UNIT_NAME / UNIT_PEDAGOGY / CROSS_CUTTING keep working.
# -----------------------------------------------------------------------------
UNIT_NAME = _ALGEBRA1_UNIT_NAMES
UNIT_PEDAGOGY = _ALGEBRA1_UNIT_PEDAGOGY
CROSS_CUTTING = _ALGEBRA1_CROSS_CUTTING

# -----------------------------------------------------------------------------
# HOW TO REACH THE LEARNER  (developmental dials + feedback science)
# Distilled from Teaching_Methodology_KB.md. UNIVERSAL -- subject-agnostic, injected
# every turn for EVERY course. Unchanged by the multi-course work.
# -----------------------------------------------------------------------------
METHODOLOGY = """\
HOW TO REACH THIS LEARNER (evidence-based -- this is your craft, use it every turn):
- Relationship and belonging come first. Use their name, assume they are smart and
  capable, and make it feel like "someone like me can do this here."
- INTRODUCE BEFORE YOU PRACTICE. If the student is new to an idea (they say they haven't
  done it, or you're unsure), your FIRST job is to NAME and DEFINE it in plain words with
  a concrete example, and put it on the board -- BEFORE any exercise. E.g. before factoring,
  make sure they know what a polynomial IS (a sum of terms like 3x^2 + 2x - 5) and what
  "factor" means (breaking an expression into the pieces that multiply to make it). Work
  ONE simple example yourself, thinking out loud, THEN invite them to try one. Never hand a
  beginner a problem that uses a word you haven't defined yet -- that is the fastest way to
  lose them. ("Let them try first" applies once the idea has been introduced, not before.)
- GAUGE their developmental stage from how they talk, their placement level, and their
  vocabulary (if you truly can't tell, ask their grade or age once, warmly), then set
  your dials:
    * Roughly 6-8 (early concrete -- our youngest, Entry-Level Math): everything is objects,
      fingers, pictures, and short story problems -- counters, ten-frames, coins, a clock face.
      One tiny idea per turn, tiny numbers, and a quick win almost every turn. Read numbers as
      words ("forty-three"), keep sentences very short and playful, and never introduce a symbol
      or term before the idea is felt with real things. Lots of gentle "you try one."
    * Roughly 9-11 (concrete thinkers): lead with objects, pictures, and story;
      introduce the letter x only AFTER the idea is felt concretely; very small steps
      and frequent wins; warm, specific encouragement lands well here.
    * Roughly 11-13 (in-between and self-conscious): psychological SAFETY above all --
      never let a wrong answer feel exposing; bridge concrete to abstract out loud
      ("the box we've been drawing -- mathematicians just call it x"); offer some
      choice; start naming the STRATEGY that worked instead of "good job."
    * Roughly 14-16 (abstract, autonomous, skeptical): treat them as a capable near-
      adult; make it genuinely relevant and challenging; give maximum agency (let them
      drive and try before you step in); be real and a little dry -- performed
      enthusiasm backfires.
- FEEDBACK that actually helps: praise the SPECIFIC STRATEGY, earned and sincere
  ("subtracting 4 from both sides first -- that's the smart move"). NEVER use person
  praise ("you're so smart," "you're a natural") or empty praise ("great job!",
  "amazing!") -- both make learners fragile and read as hollow, especially to teens.
  Give immediate, concrete feedback right after a struggle. Use "wise feedback": honest
  high standards PLUS genuine belief they can meet them ("I'm pushing because I know you
  can get this, and you're close").
- Respond to the INDIVIDUAL, never to a category (do not teach differently by gender):
    * If you see low confidence, anxiety, or "I'm not a math person": add safety, engineer
      a quick win, and separate "this is hard" from "I can't do this." Name real successes.
    * If you see overconfidence or rushing: raise the challenge and ask them to justify
      their reasoning and CHECK the answer.
- Keep them in PRODUCTIVE STRUGGLE: hard enough to matter, not so hard they quit -- adjust
  in real time. Ask ONE question at a time, then genuinely listen. Let a picture carry the
  idea and keep your words short.
- VERIFY EVERY PROBLEM YOU MAKE UP. You invent your own problems (never a canned list), so
  before you show ANY problem -- a practice one, an example, or a CHECK question -- SOLVE IT
  yourself first and confirm it has a clean, correct answer at the right level that uses ONLY
  the skill at hand. If it doesn't work out cleanly, is ambiguous, or drifts off the topic,
  DISCARD it and make another. Calibrate the difficulty to how THIS student is doing (easier
  to rebuild confidence when they struggle; a notch harder when they're cruising), start
  simpler and build up, and vary the numbers each time. A made-up problem the student can't
  trust is worse than none -- this is what keeps the tutoring credible."""


# -----------------------------------------------------------------------------
# Assembly
# -----------------------------------------------------------------------------
def _course_block(course):
    """Return the pedagogy block for a course; unknown/None -> default (do no harm)."""
    return COURSE_PEDAGOGY.get(course or DEFAULT_COURSE) or COURSE_PEDAGOGY[DEFAULT_COURSE]


def _unit_detail(unit, course=DEFAULT_COURSE) -> str:
    """The full teaching block for ONE unit of a course (or '' if the unit isn't valid)."""
    block = _course_block(course)
    p = block["units"].get(unit)
    if not p:
        return ""
    name = block["unit_names"].get(unit, "")
    return (
        f"THIS STUDENT IS ON UNIT {unit} -- {name}. Teach it with this in mind:\n"
        f"- Watch for these MISCONCEPTIONS (teach against them): {p['misconceptions']}\n"
        f"- HOW TO TEACH it well: {p['how_to_teach']}\n"
        f"- A gentle easy-to-hard progression: {p['progression']}"
    )


def _compact_index(course=DEFAULT_COURSE) -> str:
    """A one-line-per-unit misconception index, for when the unit is unknown."""
    block = _course_block(course)
    names = block["unit_names"]
    units = block["units"]
    lines = [f"QUICK MISCONCEPTION INDEX (all {len(units)} units -- lean on the one that fits):"]
    for n in sorted(units.keys()):
        lines.append(f"- Unit {n} ({names.get(n, '')}): {units[n]['misconceptions']}")
    return "\n".join(lines)


def teaching_playbook(unit=None, course=DEFAULT_COURSE) -> str:
    """Assemble the teaching guidance the tutor needs THIS turn.

    unit   -- the unit number the student is on, if known. When known we include that
              unit's detailed block; when unknown we include a compact all-units
              misconception index instead.
    course -- which course's knowledge to use (defaults to Algebra I so existing
              single-argument calls behave exactly as before).

    The universal METHODOLOGY and the course's CROSS-CUTTING error list are ALWAYS
    included. Never raises (bad input -> compact index for the resolved course).
    """
    try:
        u = int(unit) if unit is not None else None
    except (TypeError, ValueError):
        u = None

    block = _course_block(course)
    cross_cutting = block["cross_cutting"]
    focus = _unit_detail(u, course) if (u in block["units"]) else _compact_index(course)
    return "\n\n".join([METHODOLOGY, cross_cutting, focus]).strip()


# I did no harm and this file is not truncated.

# =============================================================================
# pedagogy.py  --  Math Tutor MVP  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
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

# =============================================================================
# THE PER-COURSE CATALOG OF TEACHING KNOWLEDGE
# =============================================================================
COURSE_PEDAGOGY = {
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

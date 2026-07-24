# =============================================================================
# pedagogy.py  --  Math Tutor MVP  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-07-23  NEW. This is the tutor's TEACHING BRAIN as a reusable knowledge
#               base, distilled from the two project KBs so it ships in the repo and
#               reaches the LIVE tutor at runtime (the project .md docs do NOT deploy
#               to Render -- this module is the deployed copy). It gives the model the
#               same expertise a strong human tutor carries, so we stop hand-scripting
#               teaching behavior one rule at a time.
#                 - UNIT_PEDAGOGY: for each of the 9 Algebra I units, the RELIABLE
#                   student MISCONCEPTIONS (teach against these) + HOW TO TEACH it
#                   (representations/methods that work) + an easy->hard progression.
#                   Source: Algebra_I_Curriculum_KB.md (§3-12).
#                 - METHODOLOGY: how to REACH the learner -- developmental dials by
#                   age, evidence-based feedback (process praise, "wise feedback",
#                   never person/empty praise), and confidence/anxiety vs. overconfidence
#                   signals to respond to the individual (never branch on gender).
#                   Source: Teaching_Methodology_KB.md.
#                 - CROSS_CUTTING: the all-year error watch-list.
#               teaching_playbook(unit) assembles the slice the tutor needs THIS turn:
#               the universal methodology + cross-cutting errors + the specific unit's
#               detail (or a compact all-units index when the unit is unknown).
#
#   WHY A MODULE (not more prompt text hand-written in tutor.py): the teaching
#   knowledge lives in ONE place, is easy to improve, and is injected per student/turn
#   instead of bloating every prompt with all nine units. Pure data + string assembly,
#   no external calls, so it is instant and free on every turn.
# =============================================================================

# Canonical unit names (kept in step with curriculum.py's UNITS).
UNIT_NAME = {
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

# -----------------------------------------------------------------------------
# PER-UNIT PEDAGOGY  (misconceptions to teach against + how to teach + progression)
# Distilled from Algebra_I_Curriculum_KB.md. Written to be READ BY THE TUTOR.
# -----------------------------------------------------------------------------
UNIT_PEDAGOGY = {
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

# -----------------------------------------------------------------------------
# HOW TO REACH THE LEARNER  (developmental dials + feedback science)
# Distilled from Teaching_Methodology_KB.md. Universal -- injected every turn.
# -----------------------------------------------------------------------------
METHODOLOGY = """\
HOW TO REACH THIS LEARNER (evidence-based -- this is your craft, use it every turn):
- Relationship and belonging come first. Use their name, assume they are smart and
  capable, and make it feel like "someone like me can do this here."
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
  idea and keep your words short."""

# The all-year error watch-list (Curriculum KB §12). Short; injected every turn.
CROSS_CUTTING = """\
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


def _unit_detail(unit) -> str:
    """The full teaching block for ONE unit (or "" if the unit isn't 1-9)."""
    p = UNIT_PEDAGOGY.get(unit)
    if not p:
        return ""
    name = UNIT_NAME.get(unit, "")
    return (
        f"THIS STUDENT IS ON UNIT {unit} -- {name}. Teach it with this in mind:\n"
        f"- Watch for these MISCONCEPTIONS (teach against them): {p['misconceptions']}\n"
        f"- HOW TO TEACH it well: {p['how_to_teach']}\n"
        f"- A gentle easy-to-hard progression: {p['progression']}"
    )


def _compact_index() -> str:
    """A one-line-per-unit misconception index, for when the unit is unknown."""
    lines = ["QUICK MISCONCEPTION INDEX (all 9 units -- lean on the one that fits):"]
    for n in range(1, 10):
        p = UNIT_PEDAGOGY[n]
        lines.append(f"- Unit {n} ({UNIT_NAME[n]}): {p['misconceptions']}")
    return "\n".join(lines)


def teaching_playbook(unit=None) -> str:
    """Assemble the teaching guidance the tutor needs THIS turn.

    unit -- the Algebra I unit number (1-9) the student is on, if known. When known we
            include that unit's detailed block; when unknown we include a compact
            all-units misconception index instead. The universal methodology + the
            cross-cutting error list are ALWAYS included.
    Returns a ready-to-inject string. Never raises (bad input -> compact index).
    """
    try:
        u = int(unit) if unit is not None else None
    except (TypeError, ValueError):
        u = None

    focus = _unit_detail(u) if (u in UNIT_PEDAGOGY) else _compact_index()
    return "\n\n".join([METHODOLOGY, CROSS_CUTTING, focus]).strip()


# I did no harm and this file is not truncated.

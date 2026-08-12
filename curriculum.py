# =============================================================================
# curriculum.py  --  Math Tutor MVP  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-08-12  BUILD ek -- ONE TRUE NAME PER COURSE (the elementary content gap).
#               THE DEFECT: this file has always keyed the two elementary courses
#               "entry" and "basic", while notation.py, misconceptions.py and
#               foundations.py keyed the SAME courses "entrymath" and "basicmath".
#               main.py validates an incoming course against COURSES here, so a real
#               lesson runs as "basic" -- and then asked those three modules for their
#               content and got NOTHING back: no misconception catalogue (rule 49 had
#               no rules to look up), no canonical foundation scripts (rules 36-38),
#               no notation table (rule 48). The two YOUNGEST courses, the ones the
#               elementary work was built for, were the only two running without the
#               safety net. It hid because ruletests.py and lessonaudit.py used the
#               PHANTOM spellings too: the tests and the content agreed with each
#               other and both disagreed with production. Measured before the fix:
#               notation/misconceptions/foundations = 0/0/0 bytes for entry and basic;
#               1694/10837/10635 for the phantom "basicmath".
#               THE FIX: the canonical names are the ones here ("entry", "basic"), the
#               three content modules are re-keyed to match, and canon() below is the
#               single source of truth for course identity. NOTHING IS RENAMED IN THE
#               STORE: student rows, mastery, topic progress and time logs are keyed by
#               the course string a session ran under, so canon() RESOLVES the legacy
#               spellings forward instead of orphaning any record. _course() now routes
#               through canon(), so a stored or bookmarked "basicmath" lands on Basic
#               Math instead of silently falling back to Algebra I -- which is what it
#               did before, and is why nobody saw a stack trace.
#               GUARDED: ruletests PART 3v proves every REAL course gets all three
#               blocks non-empty, that no module keys content by a name that is not a
#               real course, and that canon() still resolves the legacy spellings.
#   2026-08-11  BUILD de -- DIFFERENTIAL EQUATIONS RESTRUCTURED to the CUPM mainstream
#               syllabus (MAA Ordinary Differential Equations subcommittee report, in the
#               tutor folder). Jim: "go with the one that you feel will be most acceptable
#               to most schools" -- that is CUPM's: the modern course is computational and
#               qualitative, and the report says plainly that "some specialized analytical
#               techniques ... have necessarily been dropped" to make room.
#               WHAT MOVED: qualitative analysis (equilibria/stability/phase line) and
#               NUMERICAL METHODS (Euler/Runge-Kutta) become units 3-4; systems grow from
#               half a unit to TWO (linear + nonlinear, units 8-9); old units 6-7 merge
#               (the damping cases ARE the root cases -- one unit says so); EXACT
#               EQUATIONS shrink from a whole unit to one topic in unit 2; SERIES
#               SOLUTIONS are dropped, per the report. Unit count stays 9.
#               ⚠️ Unit NUMBERS changed meaning. No live students yet (development
#               phase); any pilot diffeq mastery rows describe the old units.
#   2026-08-03  ADDED TWO ELEMENTARY COURSES BELOW PRE-ALGEBRA (Jim's restructure): ENTRY-LEVEL
#               MATH (grades 1-3) and BASIC MATH (grades 4-6). Each is a full peer: 9 units +
#               aliases + ordered keyword rules, registered in COURSES with grade_band
#               "Elementary", and PREPENDED to COURSE_ORDER so the ladder now reads
#               entry -> basic -> prealgebra -> ... Sources: EntryMath_Curriculum_KB.md,
#               BasicMath_Curriculum_KB.md. Purely additive; the eight existing courses untouched.
#   2026-07-28  ADDED COURSE 8 -- DIFFERENTIAL EQUATIONS (the rung above Calculus; source
#               DiffEq_Curriculum_KB.md). 9 units + aliases + keyword rules; added to COURSES and
#               COURSE_ORDER (after calculus). Purely additive; the seven existing courses untouched.
#   2026-07-28  ADDED COURSE 7 -- CALCULUS (the top of the algebra ladder; source
#               Calculus_Curriculum_KB.md). 9 units + aliases + keyword rules; added to COURSES and
#               appended to COURSE_ORDER. Purely additive; the six existing courses untouched.
#   2026-07-28  ADDED COURSE 6 -- PROBABILITY & STATISTICS (a full peer added before Calculus; source
#               ProbStat_Curriculum_KB.md). 9 units + aliases + keyword rules; added to COURSES and
#               appended to COURSE_ORDER. Purely additive; the five existing courses untouched. Do no harm.
#   2026-07-28  ADDED COURSE 5 -- TRIG / PRE-CALC (the fifth rung; source PreCalc_Curriculum_KB.md).
#               9 units + aliases + keyword rules; added to COURSES and appended to COURSE_ORDER
#               (... -> algebra2 -> precalc). Purely additive; the four existing courses untouched.
#               Do no harm.
#   2026-07-28  ADDED COURSE 4 -- ALGEBRA II (the fourth rung of the math ladder; source
#               AlgebraII_Curriculum_KB.md). 9 units + aliases + keyword rules; added to COURSES and
#               appended to COURSE_ORDER (prealgebra -> algebra1 -> geometry -> algebra2). Purely
#               additive; Pre-Algebra, Algebra I, and Geometry untouched. Do no harm.
#   2026-07-28  ADDED COURSE 3 -- PRE-ALGEBRA (the "everything before algebra" foundations course;
#               source PreAlgebra_Curriculum_KB.md). 9 concept units + aliases + keyword rules;
#               added to COURSES and placed FIRST in COURSE_ORDER (prealgebra -> algebra1 ->
#               geometry). Purely additive; Algebra I + Geometry untouched. Do no harm.
#   2026-07-27  MULTI-COURSE CATALOG (Phase 1 of the math-ladder expansion; see the
#               project doc Multi_Course_Expansion_Plan.md). The flat 9-unit Algebra I
#               list became a two-level CATALOG: COURSES[course_id] -> {title, grade_band,
#               units, aliases, keyword rules}. Added a SECOND course, "geometry" (9 units,
#               CA/CCSS-aligned; source: Geometry_Curriculum_KB.md), to prove the structure.
#               BACKWARD-COMPATIBLE ON PURPOSE -- the module still exposes UNITS, UNIT_NAME,
#               and classify_unit(text) exactly as before (they default to Algebra I), so
#               main.py / tutor.py keep working UNCHANGED. New course-aware helpers were
#               ADDED (classify_unit(text, course=...), units_for, unit_name, list_courses,
#               course_title, classify_course) for the later phases (per-course tracking +
#               the course picker). No behavior changes for Algebra I -- do no harm.
#
#   2026-07-21  NEW. The single source of truth for the 9 Algebra I units, plus
#               classify_unit(text): a lightweight, deterministic classifier that
#               maps a student's problem or topic string to one of the 9 units. Used
#               by the real per-topic progress tracking (Phase 2) so that whatever a
#               student works on -- a course lesson, a practice problem, or a topic
#               chat -- gets recorded under the right unit, honestly.
#
#   WHY DETERMINISTIC (not an LLM call): classification runs on every student turn,
#   so it must be instant, free, and predictable. It matches the exact unit NAME
#   first (topic-mode picks come straight from the unit grid, so they match
#   perfectly), then falls back to an ordered keyword map for typed problems/topics.
#   More specific units are checked BEFORE the generic ones so e.g. "solve x^2 = 25"
#   lands in Quadratics, not the generic "solve an equation".
# =============================================================================

import re

# The default course. Until the course picker ships (Phase 3), the app runs Algebra I,
# so every backward-compatible call resolves here.
DEFAULT_COURSE = "algebra1"

# =============================================================================
# COURSE 1 -- ALGEBRA I  (the original 9 units; data unchanged so behavior is identical)
# =============================================================================
_ALGEBRA1_UNITS = [
    (1, "Foundations & Expressions"),
    (2, "Linear Equations & Inequalities"),
    (3, "Functions & Notation"),
    (4, "Linear Functions & Graphs"),
    (5, "Systems of Equations"),
    (6, "Exponents & Exponential Functions"),
    (7, "Polynomials & Factoring"),
    (8, "Quadratic Functions"),
    (9, "Data & Statistics"),
]

# A couple of short aliases people actually type.
_ALGEBRA1_ALIASES = {
    "linear equations": 2, "inequalities": 2, "functions": 3, "graphs": 4,
    "systems": 5, "exponents": 6, "polynomials": 7, "factoring": 7,
    "quadratics": 8, "statistics": 9, "expressions": 1,
}

# Ordered keyword rules. First match wins, so put the MORE SPECIFIC units first and
# the generic "solve a linear equation" near the end. Each entry: (unit, [patterns]).
_ALGEBRA1_RULES = [
    (5, [r"\bsystem", r"substitution", r"elimination", r"two equations", r"simultaneous"]),
    (8, [r"quadratic", r"parabola", r"x\s*\^?\s*2\b", r"x²", r"x squared", r"vertex",
         r"\(x[^)]*\)\s*\(x[^)]*\)\s*=\s*0"]),
    (7, [r"\bfactor", r"polynomial", r"trinomial", r"\bfoil\b", r"expand", r"\bgcf\b",
         r"difference of squares", r"binomial"]),
    (6, [r"exponent", r"\bpower(s)?\b", r"\^", r"exponential", r"growth", r"decay",
         r"square root", r"√", r"scientific notation"]),
    (4, [r"\bslope", r"\bgraph", r"\bline\b", r"intercept", r"y\s*=\s*mx", r"rate of change",
         r"parallel", r"perpendicular", r"coordinate"]),
    (3, [r"function", r"f\s*\(\s*x\s*\)", r"f of x", r"\bdomain\b", r"\brange\b", r"notation",
         r"\binput\b.*\boutput\b"]),
    (9, [r"\bmean\b", r"\bmedian\b", r"\bmode\b", r"\bdata\b", r"statistic", r"scatter",
         r"correlation", r"standard deviation", r"box plot", r"histogram"]),
    (1, [r"simplify", r"distribut", r"like terms", r"\bevaluate\b", r"combine",
         r"order of operations", r"\bpemdas\b", r"expression"]),
    (2, [r"inequalit", r"solve for", r"\bsolve\b", r"equation", r"one[- ]step",
         r"two[- ]step", r"variable on both", r"=\s*\d"]),
]

# =============================================================================
# COURSE 2 -- GEOMETRY  (9 units, CA/CCSS-aligned; source: Geometry_Curriculum_KB.md)
# =============================================================================
_GEOMETRY_UNITS = [
    (1, "Foundations & Constructions"),
    (2, "Transformations & Symmetry"),
    (3, "Congruence & Triangle Proofs"),
    (4, "Similarity & Dilations"),
    (5, "Right Triangles & Trigonometry"),
    (6, "Circles"),
    (7, "Coordinate Geometry"),
    (8, "Area, Surface Area & Volume"),
    (9, "Probability"),
]

_GEOMETRY_ALIASES = {
    "constructions": 1, "transformations": 2, "symmetry": 2, "congruence": 3,
    "congruent triangles": 3, "triangle proofs": 3, "similarity": 4, "dilations": 4,
    "right triangles": 5, "trigonometry": 5, "circles": 6, "coordinate geometry": 7,
    "surface area": 8, "area and volume": 8, "volume": 8, "probability": 9,
}

# Ordered specific -> generic. Unit 1 (foundations) is the catch-all, so it goes LAST.
_GEOMETRY_RULES = [
    (5, [r"\bpythag", r"hypotenuse", r"\bsine\b", r"\bcosine\b", r"\bsoh", r"\bcah",
         r"\btoa\b", r"\bsin\b", r"\bcos\b", r"\btan\b", r"special right",
         r"30\s*-?\s*60\s*-?\s*90", r"45\s*-?\s*45\s*-?\s*90",
         r"angle of (elevation|depression)", r"trigonometr", r"right triangle"]),
    (9, [r"probab", r"sample space", r"conditional", r"\bindependent\b",
         r"mutually exclusive", r"two[- ]way table", r"\bodds\b"]),
    (6, [r"\bcircle", r"\barc\b", r"\bchord", r"\btangent", r"\bsecant", r"inscribed",
         r"central angle", r"\bsector", r"\bradius\b", r"\bradii\b", r"\bdiameter\b",
         r"circumference"]),
    (4, [r"\bsimilar", r"dilation", r"scale factor", r"\bproportion", r"corresponding sides"]),
    (2, [r"transformation", r"translation", r"\breflect", r"\brotat", r"rigid motion",
         r"symmetr", r"\btranslate", r"isometr", r"pre-?image", r"\bimage\b"]),
    (3, [r"congru", r"\bsss\b", r"\bsas\b", r"\basa\b", r"\baas\b", r"\bhl\b",
         r"\bproof\b", r"\bprove\b", r"cpctc", r"two[- ]column"]),
    (7, [r"distance formula", r"\bmidpoint", r"\bslope", r"coordinate proof",
         r"negative reciprocal", r"equation of (a|the) circle", r"\bparallel\b",
         r"\bperpendicular\b"]),
    (8, [r"\barea\b", r"perimeter", r"\bvolume", r"surface area", r"cross[- ]section",
         r"\bprism", r"cylinder", r"\bcone\b", r"\bsphere", r"pyramid", r"apothem",
         r"\bnet\b", r"density"]),
    (1, [r"construct", r"compass", r"straightedge", r"bisect", r"complementary",
         r"supplementary", r"vertical angle", r"\bsegment\b", r"\bray\b", r"\bangle\b",
         r"\bpoint\b", r"\bline\b", r"\bplane\b"]),
]

# =============================================================================
# COURSE 3 -- PRE-ALGEBRA  (the "everything before algebra" foundations course; menu-first;
# source: PreAlgebra_Curriculum_KB.md). Nine concept units, age-neutral (for HS remediation).
# =============================================================================
_PREALGEBRA_UNITS = [
    (1, "Number Sense & Order of Operations"),
    (2, "Factors, Multiples & Primes"),
    (3, "Integers & Negative Numbers"),
    (4, "Fractions"),
    (5, "Decimals"),
    (6, "Ratios, Rates & Proportions"),
    (7, "Percents"),
    (8, "Measurement & Geometry Basics"),
    (9, "Variables & Expressions"),
]

_PREALGEBRA_ALIASES = {
    "order of operations": 1, "number sense": 1, "pemdas": 1,
    "factors": 2, "multiples": 2, "primes": 2, "prime": 2, "gcf": 2, "lcm": 2,
    "integers": 3, "negative numbers": 3, "negatives": 3,
    "fractions": 4, "decimals": 5,
    "ratios": 6, "rates": 6, "proportions": 6, "percents": 7, "percent": 7,
    "measurement": 8, "geometry basics": 8, "variables": 9, "expressions": 9,
}

# Ordered specific -> generic. Unit 1 (number sense / order of ops) is the catch-all, so LAST.
_PREALGEBRA_RULES = [
    (7, [r"percent", r"%", r"discount", r"\btax\b", r"\btip\b", r"interest"]),
    (6, [r"\bratio", r"\brate\b", r"proportion", r"unit rate", r"\bscale\b"]),
    (4, [r"fraction", r"numerator", r"denominator", r"mixed number", r"improper",
         r"common denominator", r"\b\d+\s*/\s*\d+\b"]),
    (5, [r"decimal", r"\btenths?\b", r"hundredths?", r"\.\d", r"rounding"]),
    (2, [r"\bfactor", r"multiple", r"\bprime\b", r"composite", r"\bgcf\b", r"\blcm\b",
         r"divisib", r"prime factor"]),
    (3, [r"integer", r"negative", r"number line", r"absolute value", r"\bopposite\b"]),
    (8, [r"perimeter", r"\barea\b", r"\bvolume\b", r"\bconvert", r"\bmean\b", r"\bmedian\b",
         r"\bangle\b", r"measurement"]),
    (9, [r"variable", r"expression", r"\bevaluate\b", r"like terms", r"one[- ]step",
         r"solve for", r"substitut", r"\bsolve\b", r"equation"]),
    (1, [r"order of operations", r"\bpemdas\b", r"place value", r"\bround", r"estimat",
         r"whole number", r"\bplus\b", r"\bminus\b", r"\btimes\b"]),
]

# =============================================================================
# COURSE 4 -- ALGEBRA II  (9 units, CA/CCSS-aligned; source: AlgebraII_Curriculum_KB.md). The rung
# above Geometry: complex numbers, the full family of function types, sequences/series, intro trig,
# and inferential statistics. Course-first (like Algebra I / Geometry), not menu-first.
# =============================================================================
_ALGEBRA2_UNITS = [
    (1, "Foundations & Systems"),
    (2, "Quadratic Functions & Complex Numbers"),
    (3, "Polynomial Functions"),
    (4, "Rational Expressions & Functions"),
    (5, "Radicals & Rational Exponents"),
    (6, "Exponential & Logarithmic Functions"),
    (7, "Sequences & Series"),
    (8, "Trigonometric Functions"),
    (9, "Statistics & Probability"),
]

_ALGEBRA2_ALIASES = {
    "linear systems": 1, "systems": 1, "absolute value": 1,
    "quadratics": 2, "complex numbers": 2, "imaginary": 2, "completing the square": 2,
    "discriminant": 2, "quadratic formula": 2,
    "polynomials": 3, "synthetic division": 3, "remainder theorem": 3, "factor theorem": 3,
    "end behavior": 3,
    "rational expressions": 4, "rational functions": 4, "asymptotes": 4, "asymptote": 4,
    "rational exponents": 5, "radicals": 5, "nth root": 5, "rationalizing": 5,
    "exponential functions": 6, "logarithms": 6, "logarithm": 6, "logarithmic": 6,
    "sequences": 7, "series": 7, "arithmetic sequence": 7, "geometric sequence": 7,
    "sigma notation": 7,
    "trigonometry": 8, "unit circle": 8, "radian": 8, "radians": 8, "amplitude": 8,
    "statistics": 9, "probability": 9, "normal distribution": 9, "conditional probability": 9,
}

# Ordered specific -> generic. Unit 1 (foundations & systems) is the catch-all, so it goes LAST.
# Unit 6 uses "exponential" (never bare "exponent") so "rational exponent" still lands in Unit 5.
_ALGEBRA2_RULES = [
    (8, [r"trigonometr", r"\btrig\b", r"unit circle", r"\bradian", r"amplitude", r"\bperiod\b",
         r"\bsine\b", r"\bcosine\b", r"\btangent\b", r"\bsin\b", r"\bcos\b", r"\btan\b",
         r"sin\s*\(", r"cos\s*\(", r"tan\s*\(", r"sinusoid", r"phase shift", r"reference angle"]),
    (9, [r"probab", r"normal distribution", r"z-?score", r"standard deviation", r"empirical rule",
         r"\bsample\b", r"sampling", r"correlation", r"conditional", r"two[- ]way table",
         r"distribution", r"\bstatistic", r"\bmean\b", r"\bmedian\b"]),
    (6, [r"exponential", r"logarithm", r"\blog\b", r"\bln\b", r"half-?life", r"compound interest",
         r"\bgrowth\b", r"\bdecay\b", r"\^\s*x", r"\be\^"]),
    (7, [r"sequence", r"\bseries\b", r"arithmetic sequence", r"geometric sequence",
         r"common difference", r"common ratio", r"\bsigma\b", r"summation", r"nth term",
         r"\d+(?:st|nd|rd|th)\s+term", r"recursive"]),
    (2, [r"quadratic", r"parabola", r"complex number", r"imaginary", r"\bi\^?\s*2\b",
         r"discriminant", r"completing the square", r"\bvertex\b", r"quadratic formula",
         r"x\s*\^?\s*2\s*=", r"sqrt\s*\(\s*-", r"√\s*-", r"square root of (a )?negative",
         r"negative under (the|a) radical"]),
    (3, [r"polynomial", r"synthetic division", r"remainder theorem", r"factor theorem",
         r"\bcubic\b", r"end behavior", r"\bdegree\b", r"multiplicit", r"\bzeros?\b",
         r"\bfactor\b"]),
    (4, [r"rational expression", r"rational function", r"rational equation", r"asymptote",
         r"\bhole\b", r"complex fraction", r"extraneous"]),
    (5, [r"radical", r"nth root", r"cube root", r"rational exponent", r"rationaliz",
         r"\^\s*\(?\s*\d+\s*/\s*\d+", r"\bsqrt\b", r"√", r"square root", r"\broots?\b"]),
    (1, [r"\bsystem", r"substitution", r"elimination", r"three variable", r"absolute value",
         r"inequalit", r"solve for", r"\bsolve\b", r"equation"]),
]

# =============================================================================
# COURSE 5 -- TRIG / PRE-CALC  (9 units; source: PreCalc_Curriculum_KB.md). The rung above Algebra II:
# deeper functions, the trig core (units 4-6), conics/parametrics, sequences/binomial, and a first
# look at limits. Course-first.
# =============================================================================
_PRECALC_UNITS = [
    (1, "Functions & Their Graphs"),
    (2, "Polynomial & Rational Functions"),
    (3, "Exponential & Logarithmic Functions"),
    (4, "Trigonometric Functions"),
    (5, "Analytic Trigonometry"),
    (6, "Applications of Trigonometry"),
    (7, "Conic Sections & Parametric Equations"),
    (8, "Sequences, Series & the Binomial Theorem"),
    (9, "Introduction to Limits"),
]

_PRECALC_ALIASES = {
    "functions": 1, "composition": 1, "inverse function": 1, "transformations": 1,
    "domain": 1, "range": 1,
    "rational functions": 2, "end behavior": 2, "polynomial": 2,
    "exponential": 3, "logarithm": 3, "logarithms": 3, "logarithmic": 3,
    "law of sines": 6, "law of cosines": 6, "vectors": 6, "polar": 6,
    "unit circle": 4, "radian": 4, "radians": 4, "trigonometry": 4, "amplitude": 4,
    "identities": 5, "identity": 5, "double angle": 5, "inverse trig": 5, "arcsin": 5,
    "conic": 7, "conics": 7, "ellipse": 7, "hyperbola": 7, "parabola": 7, "parametric": 7,
    "sequences": 8, "series": 8, "binomial": 8, "sigma": 8,
    "limits": 9, "limit": 9, "continuity": 9,
}

# Ordered specific -> generic. Unit 1 (functions & graphs) is the catch-all, so it goes LAST.
# Conic rules are checked BEFORE the rational rules so "asymptotes of a hyperbola" -> Unit 7, while a
# bare "asymptote" (rational) -> Unit 2. Unit 9 uses "tangent line" (never bare "tan") so trig
# "tangent" still lands in Unit 4.
_PRECALC_RULES = [
    (9, [r"\blimit", r"continuit", r"continuous", r"approaches", r"one[- ]sided", r"removable",
         r"instantaneous", r"secant line", r"tangent line", r"\bderivative"]),
    (6, [r"law of sines", r"law of cosines", r"oblique triangle", r"ambiguous case", r"\bvector",
         r"magnitude", r"\bpolar\b", r"\bbearing\b", r"resultant"]),
    (5, [r"identit", r"\bverify\b", r"sum formula", r"difference formula", r"double[- ]angle",
         r"half[- ]angle", r"inverse trig", r"arcsin", r"arccos", r"arctan", r"sin\s*\^?\s*2"]),
    (4, [r"unit circle", r"\bradian", r"amplitude", r"\bperiod\b", r"phase shift", r"reference angle",
         r"\bsine\b", r"\bcosine\b", r"\btangent\b", r"\bsin\b", r"\bcos\b", r"\btan\b",
         r"sin\s*\(", r"cos\s*\(", r"tan\s*\(", r"\bcsc\b", r"\bsec\b", r"\bcot\b", r"sinusoid"]),
    (7, [r"\bconic", r"ellipse", r"hyperbola", r"parabola", r"\bfoci\b", r"\bfocus\b", r"directrix",
         r"eccentricit", r"parametric", r"eliminate the parameter", r"\bvertices\b"]),
    (8, [r"sequence", r"\bseries\b", r"\bsigma\b", r"summation", r"binomial", r"pascal", r"factorial",
         r"common difference", r"common ratio", r"nth term", r"combination", r"permutation", r"nCr"]),
    (3, [r"exponential", r"logarithm", r"\blog\b", r"\bln\b", r"half-?life", r"compound", r"\bdecay\b",
         r"change of base", r"\^\s*x", r"\be\^"]),
    (2, [r"polynomial", r"rational function", r"end behavior", r"multiplicit", r"synthetic division",
         r"asymptote", r"\bzeros?\b", r"\bdegree\b"]),
    (1, [r"function", r"f\s*\(\s*x\s*\)", r"\bdomain\b", r"\brange\b", r"compos", r"∘",
         r"\(\s*[fgh]\s*o\s*[fgh]\s*\)", r"[fgh]\s*\(\s*[fgh]\s*\(", r"inverse", r"transformation",
         r"\bshift", r"stretch", r"one[- ]to[- ]one", r"piecewise", r"\bgraph"]),
]

# =============================================================================
# COURSE 6 -- PROBABILITY & STATISTICS  (9 units; source: ProbStat_Curriculum_KB.md). A data-literacy
# / intro-stats course, a full peer that pairs with Algebra II / Pre-Calc; leans on the stats visuals.
# =============================================================================
_PROBSTAT_UNITS = [
    (1, "Exploring Data"),
    (2, "Describing Distributions"),
    (3, "Scatterplots & Correlation"),
    (4, "Collecting Data"),
    (5, "Probability Basics"),
    (6, "Conditional Probability & Independence"),
    (7, "Random Variables & Expected Value"),
    (8, "The Normal Distribution"),
    (9, "Sampling & Inference"),
]

_PROBSTAT_ALIASES = {
    "categorical": 1, "quantitative": 1, "bar chart": 1, "dot plot": 1, "frequency": 1,
    "mean": 2, "median": 2, "standard deviation": 2, "box plot": 2, "quartile": 2, "iqr": 2,
    "five-number": 2, "spread": 2,
    "scatterplot": 3, "scatter plot": 3, "correlation": 3, "line of best fit": 3, "regression": 3,
    "survey": 4, "experiment": 4, "observational": 4, "sampling bias": 4, "randomization": 4,
    "sample space": 5, "complement": 5, "addition rule": 5, "mutually exclusive": 5,
    "conditional probability": 6, "independence": 6, "two-way table": 6, "tree diagram": 6,
    "multiplication rule": 6,
    "random variable": 7, "expected value": 7, "simulation": 7,
    "normal distribution": 8, "empirical rule": 8, "z-score": 8, "bell curve": 8,
    "confidence interval": 9, "margin of error": 9, "inference": 9, "sampling distribution": 9,
    "parameter": 9, "statistic": 9,
}

# Ordered specific -> generic. Unit 1 (exploring data) is the catch-all, so it goes LAST. Distinctive
# phrases win first ("normal distribution" -> 8, "probability distribution" -> 7, "sampling
# distribution" -> 9, "sample space" -> 5) so generic terms don't misfire.
_PROBSTAT_RULES = [
    (9, [r"confidence interval", r"margin of error", r"sampling distribution", r"\binference\b",
         r"\bparameter\b", r"sampling variability", r"point estimate"]),
    (8, [r"normal distribution", r"empirical rule", r"z[- ]?score", r"bell curve",
         r"68[- ]?95[- ]?99", r"standard normal"]),
    (3, [r"scatter", r"correlat", r"line of best fit", r"\bregression\b", r"residual",
         r"\bassociation\b", r"least squares"]),
    (6, [r"conditional", r"independen", r"two[- ]way table", r"tree diagram", r"multiplication rule",
         r"P\s*\(\s*A\s*\|"]),
    (7, [r"random variable", r"expected value", r"probability distribution", r"simulation",
         r"long[- ]run"]),
    (5, [r"sample space", r"complement", r"addition rule", r"mutually exclusive", r"probab",
         r"\bodds\b", r"\bchance\b"]),
    (4, [r"\bsurvey", r"experiment", r"observational", r"randomiz", r"\bbias\b", r"population",
         r"\bcensus\b", r"treatment", r"control group", r"\bsampl"]),
    (2, [r"\bmean\b", r"\bmedian\b", r"standard deviation", r"box plot", r"quartile", r"\biqr\b",
         r"five[- ]number", r"\bspread\b", r"variance", r"\brange\b", r"\bmode\b", r"distribution"]),
    (1, [r"categorical", r"quantitative", r"bar chart", r"histogram", r"dot ?plot", r"frequency",
         r"pictograph", r"\bstem\b", r"\bdata\b"]),
]

# =============================================================================
# COURSE 7 -- CALCULUS  (9 units; source: Calculus_Curriculum_KB.md). Roughly AB-level single-variable
# calculus: limits, derivatives + applications, integrals + applications, and a first look at
# differential equations that hands off to the Differential Equations course.
# =============================================================================
_CALCULUS_UNITS = [
    (1, "Limits & Continuity"),
    (2, "The Derivative: Definition & Basic Rules"),
    (3, "Product, Quotient & Chain Rules"),
    (4, "Applications of Derivatives"),
    (5, "Curve Sketching & Optimization"),
    (6, "Antiderivatives & Indefinite Integrals"),
    (7, "The Definite Integral & the Fundamental Theorem"),
    (8, "Applications of Integration"),
    (9, "Introduction to Differential Equations"),
]

# NOTE: aliases are matched by SUBSTRING and in insertion order, so the more specific phrases must
# come FIRST -- otherwise "antiderivative" would be caught by the "derivative" alias (unit 2) and
# "differential equation" by "derivative" too. Ordered specific -> generic, like the rules below.
_CALCULUS_ALIASES = {
    "differential equation": 9, "slope field": 9, "separable": 9, "exponential growth": 9,
    "area between curves": 8, "volume of revolution": 8, "disk method": 8, "washer": 8,
    # "indefinite integral" MUST precede "definite integral" (the latter is a substring of it).
    "indefinite integral": 6, "antiderivative": 6, "u-substitution": 6, "substitution": 6,
    "definite integral": 7, "riemann sum": 7, "fundamental theorem": 7, "average value": 7,
    "optimization": 5, "critical points": 5, "concavity": 5, "inflection": 5, "curve sketching": 5,
    "related rates": 4, "linear approximation": 4, "velocity": 4, "acceleration": 4,
    "chain rule": 3, "product rule": 3, "quotient rule": 3, "implicit differentiation": 3,
    "difference quotient": 2, "tangent line": 2, "power rule": 2, "derivative": 2,
    "continuity": 1, "one-sided": 1, "limits": 1, "limit": 1,
}

# Ordered specific -> generic. Unit 1 (limits) is the catch-all, so it goes LAST. Distinctive
# multi-word phrases are checked before bare words so "definite integral" -> 7 while a bare
# "integral"/"antiderivative" -> 6, and "differential equation" -> 9 before "derivative" -> 2.
_CALCULUS_RULES = [
    (9, [r"differential equation", r"slope field", r"separable", r"\bdy/dx\s*=", r"growth model",
         r"decay model", r"initial condition"]),
    (8, [r"area between", r"volume of revolution", r"disk method", r"washer", r"shell method",
         r"total distance", r"displacement", r"accumulat"]),
    (7, [r"definite integral", r"riemann", r"fundamental theorem", r"\bftc\b", r"average value",
         r"trapezoid", r"area under"]),
    (6, [r"antiderivative", r"indefinite integral", r"u-?substitution", r"\+\s*c\b",
         r"reverse power", r"integrat", r"\bintegral\b"]),
    (5, [r"optimiz", r"critical point", r"concav", r"inflection", r"curve sketch",
         r"first derivative test", r"second derivative test", r"absolute (max|min)", r"extrem"]),
    (4, [r"related rate", r"linear approximation", r"\bvelocity\b", r"\bacceleration\b",
         r"instantaneous rate", r"\bmotion\b"]),
    (3, [r"chain rule", r"product rule", r"quotient rule", r"implicit", r"second derivative",
         r"composition"]),
    (2, [r"derivative", r"difference quotient", r"tangent line", r"power rule", r"\bf'", r"differentiab"]),
    (1, [r"\blimit", r"continuit", r"continuous", r"approaches", r"one[- ]sided", r"removable",
         r"asymptote", r"indeterminate"]),
]

# =============================================================================
# COURSE 8 -- DIFFERENTIAL EQUATIONS  (9 units; source: DiffEq_Curriculum_KB.md). The rung above
# Calculus and the most advanced course in the app. Prerequisite: Calculus (esp. integration);
# Calculus Unit 9 is the on-ramp, so this course does NOT re-teach it.
# =============================================================================
_DIFFEQ_UNITS = [
    (1, "Introduction, Classification & Slope Fields"),
    (2, "First-Order Equations: Separable & Linear"),
    (3, "Qualitative Analysis: Equilibria & Stability"),
    (4, "Numerical Methods: Euler & Runge-Kutta"),
    (5, "Second-Order Linear: Homogeneous"),
    (6, "Second-Order: Nonhomogeneous, Vibrations & Resonance"),
    (7, "Laplace Transforms"),
    (8, "Linear Systems & the Phase Plane"),
    (9, "Nonlinear Systems & Stability"),
]

# NOTE: matched by SUBSTRING in insertion order, so specific phrases come FIRST (e.g. "second-order
# linear" before "linear", "nonhomogeneous" before "homogeneous").
# 2026-08-11 (build de): restructured to the CUPM mainstream syllabus -- see the module
# change note. Exact equations fold into unit 2 as a brief topic; series solutions are
# dropped (CUPM names them as what modern courses removed to make room for systems).
_DIFFEQ_ALIASES = {
    "predator": 9, "competing species": 9, "linearization": 9, "limit cycle": 9,
    "nonlinear system": 9,
    "eigenvalue": 8, "eigenvector": 8, "matrix form": 8, "phase plane": 8,
    "phase portrait": 8, "system of equations": 8, "straight-line solution": 8,
    "laplace": 7, "inverse transform": 7, "partial fractions": 7, "step function": 7,
    "nonhomogeneous": 6, "undetermined coefficients": 6, "variation of parameters": 6,
    "particular solution": 6, "vibration": 6, "spring": 6, "damping": 6, "damped": 6,
    "resonance": 6, "circuit": 6,
    "characteristic equation": 5, "auxiliary equation": 5, "repeated root": 5, "wronskian": 5,
    "homogeneous": 5, "second-order": 5, "second order": 5,
    "euler's method": 4, "euler method": 4, "runge": 4, "numerical method": 4,
    "step size": 4, "numerical solution": 4,
    "phase line": 3, "autonomous": 3, "stability": 3, "stable": 3, "unstable": 3,
    "existence and uniqueness": 3, "long-term behavior": 3, "equilibrium": 3,
    "separable": 2, "separation of variables": 2, "logistic": 2, "newton's law of cooling": 2,
    "exponential decay": 2, "growth model": 2, "integrating factor": 2,
    "first-order linear": 2, "mixing problem": 2, "tank problem": 2, "exact equation": 2,
    "bernoulli": 2,
    "slope field": 1, "direction field": 1, "classification": 1, "initial value problem": 1,
    "differential equation": 1, "order": 1,
}

# Ordered specific -> generic. Unit 1 (intro/classification) is the catch-all, so it goes LAST.
_DIFFEQ_RULES = [
    (9, [r"predator", r"competing species", r"linearizat", r"limit cycle",
         r"nonlinear (system|equation)", r"lotka|volterra"]),
    (8, [r"eigenvalue", r"eigenvector", r"matrix form", r"phase (plane|portrait)",
         r"system", r"straight[- ]line solution", r"2\s*x\s*2"]),
    (7, [r"laplace", r"inverse transform", r"partial fraction", r"step function",
         r"heaviside", r"transform of a derivative", r"s-?domain"]),
    (6, [r"nonhomogeneous", r"non-homogeneous", r"undetermined coefficient",
         r"variation of parameters", r"particular solution", r"y_?p", r"complementary",
         r"vibrat", r"spring", r"mass[- ]spring", r"damp", r"resonan", r"circuit",
         r"rlc", r"natural frequency", r"steady[- ]state", r"transient", r"oscillat"]),
    (5, [r"characteristic equation", r"auxiliary equation", r"repeated root", r"wronskian",
         r"homogeneous", r"second[- ]order", r"complex roots?", r"linearly independent"]),
    (4, [r"euler", r"runge|kutta", r"numerical (method|solution)", r"step size",
         r"local error", r"global error", r"tangent[- ]line approximation"]),
    (3, [r"phase line", r"autonomous", r"stabilit", r"(un)?stable", r"semi-?stable",
         r"existence", r"uniqueness", r"long[- ]term", r"equilibri"]),
    (2, [r"separable", r"separation of variables", r"logistic", r"law of cooling",
         r"exponential (growth|decay)", r"growth model", r"decay model", r"half-?life",
         r"integrating factor", r"first[- ]order linear", r"standard form",
         r"mixing problem", r"tank problem", r"brine", r"exact equation",
         r"exactness", r"potential function", r"bernoulli"]),
    (1, [r"classif", r"slope field", r"direction field", r"initial[- ]value",
         r"verify (a|the) solution", r"general solution", r"order", r"linear",
         r"differential equation", r"ode"]),
]

# =============================================================================
# THE CATALOG
# =============================================================================
# =============================================================================
# COURSE 9 -- ENTRY-LEVEL MATH  (grades 1-3; the first rung of the ladder, below Basic Math and
# Pre-Algebra). Concrete, picture-first arithmetic: counting, adding/subtracting to 20, place
# value, carrying/borrowing, money, time, and shapes. Source: EntryMath_Curriculum_KB.md.
# =============================================================================
_ENTRY_UNITS = [
    (1, "Counting & Number Sense"),
    (2, "Addition to 20"),
    (3, "Subtraction to 20"),
    (4, "Place Value to 1,000"),
    (5, "Two- & Three-Digit Addition"),
    (6, "Two- & Three-Digit Subtraction"),
    (7, "Money — Coins, Bills & Making Change"),
    (8, "Time, Calendar & Measurement"),
    (9, "Shapes, Patterns & Groups"),
]

# Aliases are matched by SUBSTRING in insertion order (first match wins), so the more SPECIFIC
# and compound phrases come FIRST -- e.g. "counting money" before "counting", and "carrying"
# (Unit 5) before "add" (Unit 2) -- so a phrase lands in the right unit.
_ENTRY_ALIASES = {
    # Unit 7 (money) -- before "counting", so "counting money" -> money.
    "counting money": 7, "making change": 7, "coins": 7, "cents": 7, "dollars": 7, "money": 7,
    # Unit 8 (time & measurement)
    "telling time": 8, "clock": 8, "calendar": 8, "measurement": 8, "length": 8, "time": 8,
    # Unit 9 (shapes, patterns, groups)
    "shapes": 9, "patterns": 9, "arrays": 9, "equal groups": 9, "multiplication": 9,
    # Unit 5 (carrying) -- before the plain add/plus aliases, so "carrying in addition" -> Unit 5.
    "carrying": 5, "regrouping": 5, "column addition": 5, "two-digit addition": 5,
    # Unit 6 (borrowing)
    "borrowing": 6, "column subtraction": 6, "two-digit subtraction": 6,
    # Unit 4 (place value)
    "place value": 4, "tens and ones": 4, "expanded form": 4, "hundreds": 4,
    # Unit 2 (addition to 20)
    "addition": 2, "adding": 2, "sums": 2, "plus": 2, "add": 2,
    # Unit 3 (subtraction to 20)
    "subtraction": 3, "subtract": 3, "take away": 3, "difference": 3, "minus": 3,
    # Unit 1 (counting / number sense) -- most generic, LAST.
    "counting": 1, "number sense": 1, "compare numbers": 1, "greater than": 1,
    "less than": 1, "skip counting": 1, "count": 1,
}

# Ordered specific -> generic. Unit 1 (counting / number sense) is the catch-all, so it goes LAST.
_ENTRY_RULES = [
    (7, [r"\bmoney\b", r"\bcoins?\b", r"\bcents?\b", r"\bdollars?\b", r"\bnickel", r"\bdime",
         r"\bquarter", r"\bpenn(y|ies)", r"making change", r"how much.*cost"]),
    (8, [r"\btime\b", r"\bclock\b", r"o'?clock", r"\bhour", r"\bminute", r"calendar", r"\bmonth",
         r"\bweek\b", r"measur", r"\blength\b", r"\binch", r"\bruler", r"how long"]),
    (9, [r"\bshape", r"\bpattern", r"\barray", r"equal group", r"\bmultipl", r"\btriangle",
         r"\bsquare\b", r"\brectangle", r"\bcircle\b", r"skip count"]),
    (5, [r"carry", r"regroup", r"two[- ]digit add", r"three[- ]digit add", r"column add",
         r"adding.*(ten|hundred)", r"stack.*add"]),
    (6, [r"borrow", r"two[- ]digit subtract", r"three[- ]digit subtract", r"column subtract"]),
    (4, [r"place value", r"tens and ones", r"\bhundreds?\b", r"expanded form", r"\bround"]),
    (2, [r"\badd", r"\bplus\b", r"\bsum", r"altogether", r"in all"]),
    (3, [r"subtract", r"take away", r"\bminus\b", r"how many.*left", r"\bdifference\b", r"fewer"]),
    (1, [r"count", r"number sense", r"compare", r"greater", r"less than", r"\bbigger\b",
         r"\bsmaller\b", r"skip count", r"more than", r"order the numbers"]),
]

# =============================================================================
# COURSE 10 -- BASIC MATH  (grades 4-6; the rung between Entry-Level Math and Pre-Algebra).
# Multi-digit operations, factors, fractions, decimals, an intro to ratios/percents, and
# multi-step word problems. Source: BasicMath_Curriculum_KB.md.
# =============================================================================
_BASIC_UNITS = [
    (1, "Place Value & Whole-Number Operations"),
    (2, "Multiplication"),
    (3, "Division"),
    (4, "Factors, Multiples, GCF & LCM"),
    (5, "Fractions — Meaning & Equivalence"),
    (6, "Fraction Operations"),
    (7, "Decimals"),
    (8, "Ratios, Rates & Percents"),
    (9, "Measurement, Geometry & Word Problems"),
]

# Matched by SUBSTRING in insertion order (first match wins), so compound/specific phrases go
# FIRST: the fraction-OPERATION phrases (Unit 6) before bare "fractions" (Unit 5), and the
# fraction phrases before the plain "add/subtract/multiply/divide" that belong to Units 2-3.
_BASIC_ALIASES = {
    # Unit 6 (fraction operations) -- before "fractions" and before plain multiply/divide.
    "adding fractions": 6, "add fractions": 6, "subtracting fractions": 6,
    "multiplying fractions": 6, "dividing fractions": 6, "fraction operations": 6,
    "mixed numbers": 6,
    # Unit 5 (fraction meaning & equivalence)
    "equivalent fractions": 5, "simplifying fractions": 5, "comparing fractions": 5,
    "fractions": 5,
    # Unit 8 (ratios, rates, percents)
    "unit rate": 8, "ratios": 8, "rates": 8, "percents": 8, "percent": 8,
    # Unit 7 (decimals)
    "decimals": 7, "decimal": 7,
    # Unit 4 (factors, multiples, GCF, LCM) -- before multiplication so "multiples" isn't taken.
    "prime factorization": 4, "factors": 4, "multiples": 4, "primes": 4, "prime": 4,
    "gcf": 4, "lcm": 4,
    # Unit 3 (division)
    "long division": 3, "division": 3, "dividing": 3, "remainders": 3, "remainder": 3,
    # Unit 2 (multiplication)
    "multiplication": 2, "times tables": 2, "multiplying": 2, "area model": 2,
    # Unit 9 (measurement, geometry, word problems)
    "word problems": 9, "perimeter": 9, "area": 9, "volume": 9, "measurement": 9,
    # Unit 1 (place value & whole-number ops) -- most generic, LAST.
    "place value": 1, "rounding": 1, "estimation": 1, "whole numbers": 1,
}

# Ordered specific -> generic. Unit 4 (factors/multiples) goes BEFORE Unit 2 so "multiples" is
# never swallowed by "multipl..."; Unit 6 (fraction ops) before Unit 5 (bare "fraction").
# Unit 1 (place value / whole-number ops) is the catch-all, so it goes LAST.
_BASIC_RULES = [
    (6, [r"add.*fraction", r"subtract.*fraction", r"multipl.*fraction", r"divid.*fraction",
         r"mixed number", r"improper", r"common denominator", r"fraction operation"]),
    (5, [r"equivalent fraction", r"simplif.*fraction", r"compar.*fraction", r"\bfraction",
         r"numerator", r"denominator"]),
    (8, [r"\bratio", r"\brate\b", r"unit rate", r"percent", r"%", r"discount", r"\btip\b"]),
    (7, [r"decimal", r"\btenths?\b", r"hundredths?", r"\.\d"]),
    (4, [r"\bfactor", r"multiple", r"\bprime", r"composite", r"\bgcf\b", r"\blcm\b",
         r"prime factor", r"divisib"]),
    (3, [r"long division", r"remainder", r"quotient", r"\bdivide\b", r"\bdividing\b",
         r"\bdivision\b", r"share.*equal"]),
    (2, [r"multiply", r"multiplication", r"multiplying", r"times table", r"\bproduct\b",
         r"area model"]),
    (9, [r"perimeter", r"\barea\b", r"\bvolume\b", r"word problem", r"\bangle", r"\bconvert",
         r"measur", r"\bunits?\b"]),
    (1, [r"place value", r"\bround", r"estimat", r"whole number", r"\bplus\b", r"\bminus\b",
         r"\badd\b", r"\bsubtract\b", r"compare", r"number line"]),
]

COURSES = {
    "entry": {
        "title": "Entry-Level Math",
        "grade_band": "Elementary",
        "units": _ENTRY_UNITS,
        "aliases": _ENTRY_ALIASES,
        "rules": _ENTRY_RULES,
    },
    "basic": {
        "title": "Basic Math",
        "grade_band": "Elementary",
        "units": _BASIC_UNITS,
        "aliases": _BASIC_ALIASES,
        "rules": _BASIC_RULES,
    },
    "algebra1": {
        "title": "Algebra I",
        "grade_band": "High School",
        "units": _ALGEBRA1_UNITS,
        "aliases": _ALGEBRA1_ALIASES,
        "rules": _ALGEBRA1_RULES,
    },
    "geometry": {
        "title": "Geometry",
        "grade_band": "High School",
        "units": _GEOMETRY_UNITS,
        "aliases": _GEOMETRY_ALIASES,
        "rules": _GEOMETRY_RULES,
    },
    "prealgebra": {
        "title": "Pre-Algebra",
        "grade_band": "Foundations",
        "units": _PREALGEBRA_UNITS,
        "aliases": _PREALGEBRA_ALIASES,
        "rules": _PREALGEBRA_RULES,
    },
    "algebra2": {
        "title": "Algebra II",
        "grade_band": "High School",
        "units": _ALGEBRA2_UNITS,
        "aliases": _ALGEBRA2_ALIASES,
        "rules": _ALGEBRA2_RULES,
    },
    "precalc": {
        "title": "Trig / Pre-Calc",
        "grade_band": "High School",
        "units": _PRECALC_UNITS,
        "aliases": _PRECALC_ALIASES,
        "rules": _PRECALC_RULES,
    },
    "probstat": {
        "title": "Probability & Statistics",
        "grade_band": "High School",
        "units": _PROBSTAT_UNITS,
        "aliases": _PROBSTAT_ALIASES,
        "rules": _PROBSTAT_RULES,
    },
    "calculus": {
        "title": "Calculus",
        "grade_band": "High School",
        "units": _CALCULUS_UNITS,
        "aliases": _CALCULUS_ALIASES,
        "rules": _CALCULUS_RULES,
    },
    "diffeq": {
        "title": "Differential Equations",
        "grade_band": "Advanced",
        "units": _DIFFEQ_UNITS,
        "aliases": _DIFFEQ_ALIASES,
        "rules": _DIFFEQ_RULES,
    },
}

# The order courses are offered in (the math ladder): Entry-Level -> Basic -> Pre-Algebra ->
# Algebra I -> Geometry -> Algebra II -> Trig/Pre-Calc -> Calculus -> Differential Equations,
# then Probability & Statistics (a parallel data course). Entry-Level and Basic (2026-08-03)
# are the new elementary rungs BELOW Pre-Algebra.
COURSE_ORDER = ["entry", "basic", "prealgebra", "algebra1", "geometry", "algebra2", "precalc",
                "calculus", "diffeq", "probstat"]

# -----------------------------------------------------------------------------
# BACKWARD-COMPATIBLE MODULE-LEVEL EXPORTS (default course = Algebra I).
# main.py uses curriculum.UNITS and curriculum.UNIT_NAME directly; keep them pointing
# at Algebra I so nothing downstream changes until the course picker wires a course in.
# -----------------------------------------------------------------------------
UNITS = COURSES[DEFAULT_COURSE]["units"]
UNIT_NAME = {n: name for n, name in UNITS}


# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------
# ONE TRUE NAME PER COURSE (build ek, 2026-08-12). The keys of COURSES above are the
# canonical names and the only ones any module may key content by. These are the older
# spellings that leaked into the content modules and the test harness; they stay here
# FOREVER as read-only aliases, because a student record written under one of them must
# still resolve to the right course. Never add a new alias to make a typo work -- fix
# the typo. ruletests PART 3v fails the build if a module keys content by a non-canonical
# name.
COURSE_ALIASES = {
    "entrymath": "entry",
    "basicmath": "basic",
}


def canon(course):
    """The canonical key for a course name, resolving legacy aliases.

    Unknown names are returned UNCHANGED (not defaulted): the caller decides what to do
    with a name nobody recognises, and _course() below still falls back safely. Returning
    the default here would re-create exactly the silent-fallback bug this build fixed."""
    c = (course or "").strip().lower()
    return COURSE_ALIASES.get(c, c)


def _course(course):
    """Return a course dict; unknown/None falls back to the default course (do no harm).

    2026-08-12 (build ek): routes through canon() first, so a legacy "basicmath" resolves
    to Basic Math instead of silently becoming Algebra I."""
    return COURSES.get(canon(course) or DEFAULT_COURSE) or COURSES[DEFAULT_COURSE]


def list_courses():
    """[(course_id, title), ...] in ladder order -- for the course picker (Phase 3)."""
    return [(cid, COURSES[cid]["title"]) for cid in COURSE_ORDER if cid in COURSES]


def course_title(course=DEFAULT_COURSE):
    """Display title for a course id."""
    return _course(course)["title"]


def units_for(course=DEFAULT_COURSE):
    """The [(n, name), ...] unit list for a course (copy, so callers can't mutate it)."""
    return list(_course(course)["units"])


def unit_name(course, n):
    """The name of unit n within a course, or '' if out of range."""
    try:
        n = int(n)
    except (TypeError, ValueError):
        return ""
    for k, name in _course(course)["units"]:
        if k == n:
            return name
    return ""


def classify_unit(text, course=DEFAULT_COURSE):
    """
    Map a problem/topic string to (unit_number, unit_name) WITHIN a course. Returns
    (None, None) if nothing matches. Exact/contained unit-NAME match wins first (grid
    picks land here), then aliases, then the ordered keyword rules.

    Backward-compatible: called as classify_unit(text) it classifies against Algebra I,
    exactly as before. Pass course="geometry" (etc.) to classify within another course.
    """
    if not text:
        return (None, None)
    c = _course(course)
    units = c["units"]
    name_by_num = {n: name for n, name in units}
    s = str(text).strip().lower()

    # 1) Exact / contained unit-name match (topic-mode grid picks land here).
    for n, name in units:
        if name.lower() in s:
            return (n, name)

    # 2) Short aliases people actually type.
    for alias, n in c["aliases"].items():
        if alias in s:
            return (n, name_by_num.get(n, ""))

    # 3) Keyword rules (ordered; specific before generic).
    for unit, patterns in c["rules"]:
        for pat in patterns:
            if re.search(pat, s):
                return (unit, name_by_num.get(unit, ""))

    return (None, None)


def classify_course(text, default=DEFAULT_COURSE):
    """
    Best-effort guess of WHICH course a free-typed string belongs to (for the drop-in
    'work a problem' path once multiple courses are live). Explicit course names/aliases
    win; otherwise returns `default`. Deliberately conservative -- when unsure it does
    NOT guess a non-default course. Not wired into the app yet (Phase 3).
    """
    if not text:
        return default
    s = str(text).strip().lower()
    for cid in COURSE_ORDER:
        if COURSES[cid]["title"].lower() in s or cid in s:
            return cid
    # A few strong subject signals.
    geo_signals = ("geometry", "triangle", "pythag", "circle", "congruent", "angle",
                   "trigonometr", "proof")
    if any(sig in s for sig in geo_signals):
        return "geometry"
    return default


# I did no harm and this file is not truncated.

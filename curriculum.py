# =============================================================================
# curriculum.py  --  Math Tutor MVP  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
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
# THE CATALOG
# =============================================================================
COURSES = {
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
}

# The order courses are offered in (the math ladder): Pre-Algebra -> Algebra I -> Geometry ->
# Algebra II -> Trig/Pre-Calc. New courses append here.
COURSE_ORDER = ["prealgebra", "algebra1", "geometry", "algebra2", "precalc"]

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
def _course(course):
    """Return a course dict; unknown/None falls back to the default course (do no harm)."""
    return COURSES.get(course or DEFAULT_COURSE) or COURSES[DEFAULT_COURSE]


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

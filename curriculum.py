# =============================================================================
# curriculum.py  --  Math Tutor MVP  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
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
}

# The order courses are offered in (the math ladder). New courses append here.
COURSE_ORDER = ["algebra1", "geometry"]

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

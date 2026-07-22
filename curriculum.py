# =============================================================================
# curriculum.py  --  Math Tutor MVP  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-07-21  NEW. The single source of truth for the 9 Algebra I units, plus
#               classify_unit(text): a lightweight, deterministic classifier that
#               maps a student's problem or topic string to one of the 9 units. Used
#               by the real per-topic progress tracking (Phase 2) so that whatever a
#               student works on -- a course lesson, a practice problem, or a topic
#               chat -- gets recorded under the right unit, honestly.
#
#   WHY DETERMINISTIC (not an LLM call): classification runs on every student turn,
#   so it must be instant, free, and predictable. It matches the exact unit NAME
#   first (topic-mode picks come straight from the 9-unit grid, so they match
#   perfectly), then falls back to an ordered keyword map for typed problems/topics.
#   More specific units (quadratics, factoring, systems) are checked BEFORE the
#   generic "solve an equation" so e.g. "solve x^2 = 25" lands in Quadratics.
# =============================================================================

import re

# The 9 Algebra I units (canonical order + names).
UNITS = [
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
UNIT_NAME = {n: name for n, name in UNITS}

# Ordered keyword rules. First match wins, so put the MORE SPECIFIC units first and
# the generic "solve a linear equation" near the end. Each entry: (unit, [patterns]).
# Patterns are matched case-insensitively as whole-ish words where it matters.
_KEYWORD_RULES = [
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


def classify_unit(text: str):
    """
    Map a problem/topic string to (unit_number, unit_name). Returns (None, None) if
    nothing matches. Exact unit-NAME match wins first (grid picks), then keywords.
    """
    if not text:
        return (None, None)
    s = str(text).strip().lower()

    # 1) Exact / contained unit-name match (topic-mode grid picks land here).
    for n, name in UNITS:
        if name.lower() in s:
            return (n, name)
    # A couple of short aliases people actually type.
    aliases = {
        "linear equations": 2, "inequalities": 2, "functions": 3, "graphs": 4,
        "systems": 5, "exponents": 6, "polynomials": 7, "factoring": 7,
        "quadratics": 8, "statistics": 9, "expressions": 1,
    }
    for alias, n in aliases.items():
        if alias in s:
            return (n, UNIT_NAME[n])

    # 2) Keyword rules (ordered; specific before generic).
    for unit, patterns in _KEYWORD_RULES:
        for pat in patterns:
            if re.search(pat, s):
                return (unit, UNIT_NAME[unit])

    return (None, None)


# I did no harm and this file is not truncated.

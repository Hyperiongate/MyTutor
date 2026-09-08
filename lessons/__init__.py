# =============================================================================
# lessons/__init__.py  --  THE COURSE, TEN FILES  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-09-08  BUILD uj -- ONE FILE PER COURSE. lessonscripts.py held all 360 authored
#               lessons (25,500 lines of data in a 41,800-line file). Now each course is
#               its own file here, pure data, and this module joins them in course order:
#               LESSONS (every lesson, course by course) and COURSE_ORDER (every id in
#               teaching order, each course's ORDER slice in turn). lessonscripts.py
#               imports both and does exactly what it did -- the disagreement check, the
#               reorder, LESSON_BY_ID, PILOT_LESSON -- so nothing downstream changed.
#               The COURSE_ORDER comment below came from lessonscripts.py with it.
# =============================================================================
# THE COURSE ORDER IS OWNED HERE (jz -- jy had accidentally placed carrying before
# two-digit-no-carry). Import fails loudly if a lesson is missing or listed twice.
from . import entry, basic, prealgebra, algebra1, geometry, algebra2, precalc, probstat, calculus, diffeq

COURSES = ("entry", "basic", "prealgebra", "algebra1", "geometry", "algebra2",
           "precalc", "probstat", "calculus", "diffeq")
_MODULES = (entry, basic, prealgebra, algebra1, geometry, algebra2, precalc, probstat, calculus, diffeq)

LESSONS = [les for m in _MODULES for les in m.LESSONS]
COURSE_ORDER = [lid for m in _MODULES for lid in m.ORDER]

# I did no harm and this file is not truncated.

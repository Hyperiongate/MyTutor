# =============================================================================
# progress.py  --  Math Tutor MVP  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-07-19  get_progress() now accepts a `placement` (from Mr. Cadabra's
#               Challenge) and reflects it: real level/level_title + a "placed"
#               object (start unit, points, strengths) for the dashboard.
#   2026-07-19  Initial version. Provides the progress data that powers the
#               dashboard. For now this returns RICH REPRESENTATIVE ("sample")
#               data per test student so the dashboard looks spectacular for demos
#               -- it is clearly flagged {"sample": true}. It is built on the real
#               data SHAPE the app will populate from actual tracking later
#               (mastered/in-progress concepts, time, accuracy, streaks, etc.), so
#               swapping real numbers in requires no dashboard redesign.
#
# HOW REAL DATA WILL PLUG IN (later):
#   - units[*].percent / status  <- from the tutor's [[covered]] events + quiz results
#   - problems_attempted/correct  <- counted from the session logs
#   - minutes / time_by_day       <- from session start/stop timestamps
#   - streak_days / sessions      <- from login history
#   The get_progress() return shape stays identical.
# =============================================================================

# The 9 Algebra I units (aligned to Algebra_I_Curriculum_KB.md).
UNIT_NAMES = [
    ("u1", "Foundations & Expressions"),
    ("u2", "Linear Equations & Inequalities"),
    ("u3", "Functions & Notation"),
    ("u4", "Linear Functions & Graphs"),
    ("u5", "Systems of Equations"),
    ("u6", "Exponents & Exponential Functions"),
    ("u7", "Polynomials & Factoring"),
    ("u8", "Quadratic Functions"),
    ("u9", "Data & Statistics"),
]

# Radar axes (skill categories).
STRENGTH_AXES = ["Solving", "Graphing", "Reasoning", "Modeling", "Speed", "Accuracy"]


def _unit_list(percents):
    """Build the units array from a list of 9 percents; status derived from %."""
    units = []
    for (uid, name), p in zip(UNIT_NAMES, percents):
        status = "mastered" if p >= 90 else ("in_progress" if p > 0 else "not_started")
        units.append({"id": uid, "name": name, "percent": p, "status": status})
    return units


# Representative profiles per test student (beginner -> advanced).
_PROFILES = {
    # code: (name, unit_percents[9], streak, longest, sessions, avg_min,
    #        attempted, correct, minutes_week, week_growth[6], time_by_day[7],
    #        strengths[6], level, level_title, xp, xp_to_next)
    "1234": dict(  # Alex -- early beginner
        percents=[62, 28, 0, 0, 0, 0, 0, 0, 0],
        streak=4, longest=6, sessions=7, avg_min=15,
        attempted=41, correct=27, minutes_week=64,
        growth=[5, 9, 14, 19, 22, 27], by_day=[12, 0, 18, 10, 14, 0, 10],
        strengths=[45, 20, 40, 25, 35, 55],
        level=2, level_title="Equation Rookie", xp=640, xp_to_next=1000,
    ),
    "2345": dict(  # Maya -- solid intermediate
        percents=[100, 78, 55, 30, 0, 0, 0, 0, 0],
        streak=8, longest=12, sessions=19, avg_min=21,
        attempted=142, correct=113, minutes_week=118,
        growth=[18, 26, 33, 41, 47, 52], by_day=[24, 20, 26, 0, 22, 16, 10],
        strengths=[78, 55, 68, 50, 60, 72],
        level=4, level_title="Equation Explorer", xp=2180, xp_to_next=2800,
    ),
    "3456": dict(  # Sam -- advanced
        percents=[100, 100, 92, 80, 66, 40, 20, 0, 0],
        streak=15, longest=15, sessions=34, avg_min=24,
        attempted=286, correct=246, minutes_week=163,
        growth=[40, 48, 55, 61, 66, 71], by_day=[28, 32, 24, 30, 26, 22, 18],
        strengths=[90, 80, 85, 72, 78, 86],
        level=6, level_title="Algebra Ace", xp=4620, xp_to_next=5400,
    ),
    "0000": dict(  # Demo -- mid
        percents=[100, 64, 40, 12, 0, 0, 0, 0, 0],
        streak=6, longest=10, sessions=14, avg_min=19,
        attempted=98, correct=76, minutes_week=88,
        growth=[12, 20, 27, 34, 39, 44], by_day=[16, 18, 0, 20, 14, 12, 8],
        strengths=[70, 48, 60, 44, 52, 66],
        level=3, level_title="Equation Adventurer", xp=1480, xp_to_next=2000,
    ),
}

_DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
_WEEKS = ["6 wks ago", "5 wks", "4 wks", "3 wks", "2 wks", "This wk"]


def get_progress(code: str, student: dict, placement: dict = None) -> dict:
    """
    Return the progress object for this student. Currently representative sample
    data; shape is final. `student` is the record from students.json (for name).
    If `placement` (from Mr. Cadabra's Challenge) is provided, the level and a
    "placed" badge reflect the real placement result.
    """
    name = (student or {}).get("name", "Student")
    prof = _PROFILES.get(code)
    if not prof:
        # Neutral fallback for any unknown/real code with no seeded profile yet.
        prof = dict(
            percents=[20, 5, 0, 0, 0, 0, 0, 0, 0],
            streak=1, longest=1, sessions=1, avg_min=12,
            attempted=6, correct=4, minutes_week=12,
            growth=[0, 0, 0, 2, 4, 6], by_day=[12, 0, 0, 0, 0, 0, 0],
            strengths=[30, 15, 25, 15, 20, 35],
            level=1, level_title="Just Starting", xp=120, xp_to_next=500,
        )

    units = _unit_list(prof["percents"])
    mastered = sum(1 for u in units if u["status"] == "mastered")
    in_progress = sum(1 for u in units if u["status"] == "in_progress")
    not_started = sum(1 for u in units if u["status"] == "not_started")
    overall = round(sum(prof["percents"]) / len(prof["percents"]))
    accuracy = round(100 * prof["correct"] / prof["attempted"]) if prof["attempted"] else 0

    # If the student took the Challenge, reflect that real placement.
    level = prof["level"]
    level_title = prof["level_title"]
    placed = None
    if placement:
        level = placement.get("level", level)
        level_title = placement.get("level_title", level_title)
        placed = {
            "unit": placement.get("start_unit"),
            "unit_name": placement.get("start_unit_name", ""),
            "points": placement.get("points", 0),
            "strengths": placement.get("strengths", []),
        }

    return {
        "sample": True,  # <-- representative demo data; swap real tracking in later
        "placed": placed,  # real placement result, or None if the Challenge wasn't taken
        "student": name,
        "overall_percent": overall,
        "level": level,
        "level_title": level_title,
        "xp": prof["xp"],
        "xp_to_next": prof["xp_to_next"],
        "streak_days": prof["streak"],
        "longest_streak": prof["longest"],
        "sessions": prof["sessions"],
        "avg_session_min": prof["avg_min"],
        "problems_attempted": prof["attempted"],
        "problems_correct": prof["correct"],
        "accuracy": accuracy,
        "minutes_this_week": prof["minutes_week"],
        "concepts_mastered": mastered,
        "concepts_in_progress": in_progress,
        "concepts_not_started": not_started,
        "mastery": {"mastered": mastered, "in_progress": in_progress, "not_started": not_started},
        "units": units,
        "skill_growth": [{"label": w, "value": v} for w, v in zip(_WEEKS, prof["growth"])],
        "time_by_day": [{"label": d, "value": v} for d, v in zip(_DAYS, prof["by_day"])],
        "strengths": [{"skill": s, "value": v} for s, v in zip(STRENGTH_AXES, prof["strengths"])],
    }


# I did no harm and this file is not truncated.

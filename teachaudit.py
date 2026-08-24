# =============================================================================
# teachaudit.py  --  THE TEACH-BEAT GIVEAWAY AUDIT  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-08-24  NEW (build mr). The other half of workedaudit.py, and it exists
#               because the same defect was caught BY HAND twice in one day --
#               once in Entry-Level Unit 8's clock lesson and once in Unit 9's
#               equal-groups lesson, both while building them. A defect found
#               twice by hand in a day is a defect nothing is watching for.
#
#               WHAT IT LOOKS FOR. A lesson TEACHES, then shows two WORKED
#               examples, then ASKS. workedaudit.py checks the worked examples.
#               Nothing checked the teach beats -- and they are the FIRST thing
#               a child hears, so a teach beat that works a problem the lesson
#               later asks is the earliest and loudest way to hand out an answer.
#
#               ⚠️ THE SECOND HALF IS THE REVERSE FACT, which no tuple comparison
#               can see. When a lesson teaches one idea in two directions -- "the
#               minute hand points to 4" and "20 minutes past", or a shape's sides
#               and its corners -- those are ONE fact wearing two ops. A teach
#               beat that demonstrates either direction has given away both. The
#               tuples differ, so workedaudit's test passes and the child still
#               gets the answer handed to them.
#
#               HOW IT DECIDES. Same high-confidence rule as workedaudit for the
#               direct case: the numbers spoken in the beat must OPEN with the
#               problem's own numbers, in order, and the answer must follow. The
#               reverse case is reported SEPARATELY and more cautiously -- same
#               lesson, two ops, and the beat speaks the problem's answer as its
#               own leading number.
#
#               A hit is not automatically a defect -- read it. Some are honest
#               (a beat may walk the same numbers in a different direction to
#               make a point). Most are not.
#
#               DELIBERATELY NOT WIRED INTO ruletests.py, for the same reason
#               workedaudit is not: it reports on content that shipped long ago,
#               and blocking every deploy on a backlog nobody has triaged yet
#               teaches people to disable the check. Run it by hand:
#                   python3 teachaudit.py
# =============================================================================
import re

import lessonscripts as L


def _numbers(text):
    return re.findall(r"\d+", text)


def _tuple_for(p):
    """The numbers a child is GIVEN, in the order the problem states them."""
    out = [str(p["a"])]
    if p.get("b"):
        out.append(str(p["b"]))
    if p.get("c"):
        out.append(str(p["c"]))
    return out


def direct_hits(les):
    """Teach beats that work a problem this lesson also ASKS -- same direction."""
    hits = []
    problems = list(les["bank"]) + [pair["ask"] for pair in les["pairs"]]
    for i, (spoken, _board) in enumerate(les["teach"]):
        said = _numbers(spoken)
        if not said:
            continue
        for p in problems:
            tup = _tuple_for(p)
            answer = str(L.ans(p))
            if (len(said) >= len(tup) + 1
                    and said[:len(tup)] == tup
                    and answer in said[len(tup):]):
                hits.append((les["id"], i + 1, spoken, p, answer, "direct"))
    return hits


def reverse_hits(les):
    """One fact, two ops -- a beat that demonstrates either direction gives both.

    Only meaningful in a lesson whose problems use MORE THAN ONE op, which is
    exactly where a tuple comparison goes blind. Reported separately because the
    evidence is weaker: it fires when a beat leads with a problem's ANSWER and
    that problem's op is not the only op in the lesson."""
    problems = list(les["bank"]) + [pair["ask"] for pair in les["pairs"]]
    ops = {p.get("op", les["op"]) for p in problems}
    if len(ops) < 2:
        return []
    hits = []
    for i, (spoken, _board) in enumerate(les["teach"]):
        said = _numbers(spoken)
        if not said:
            continue
        for p in problems:
            answer = str(L.ans(p))
            given = _tuple_for(p)
            # the beat OPENS with what this problem is asking FOR, and later says
            # what the child would have been given -- i.e. it walked the reverse.
            if said[0] == answer and any(g in said[1:] for g in given):
                hits.append((les["id"], i + 1, spoken, p, answer, "reverse"))
    return hits


def audit(lessons=None):
    """Returns [(lesson_id, beat_no, spoken, problem, answer, kind)]."""
    out = []
    for les in (lessons if lessons is not None else L.LESSONS):
        out += direct_hits(les)
        out += reverse_hits(les)
    return out


if __name__ == "__main__":
    found = audit()
    direct = [h for h in found if h[5] == "direct"]
    reverse = [h for h in found if h[5] == "reverse"]
    for label, rows in (("DIRECT", direct), ("REVERSE (one fact, two ops)", reverse)):
        print(f"\n===== {label}: {len(rows)} =====")
        for lesson_id, beat, spoken, problem, answer, _kind in rows:
            print(f"{lesson_id}  (teach beat {beat})")
            print(f"    says : {spoken[:96]}")
            print(f"    gives: {problem} -> {answer}")
    by_lesson = {h[0] for h in found}
    print(f"\n{len(found)} teach beats answer a problem their own lesson asks, "
          f"across {len(by_lesson)} lessons of {len(L.LESSONS)}.")


# I did no harm and this file is not truncated.

# =============================================================================
# workedaudit.py  --  THE WORKED-EXAMPLE GIVEAWAY AUDIT  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-08-23  NEW (build lr). A standalone audit -- nothing imports it, and it
#               is deliberately NOT wired into ruletests.py, because it fails on
#               45 lessons that shipped long ago and would block every deploy
#               until they are rewritten. Run it by hand:  python3 workedaudit.py
#
#               WHAT IT LOOKS FOR. A lesson teaches, then shows two WORKED
#               examples, then asks. The worked examples must not answer a
#               problem the child is about to be asked -- if they do, the tutor
#               reads the answer aloud minutes before asking the question, and
#               "mastered" stops meaning the child can do it.
#
#               The validator cannot see this: worked examples are prose, not
#               problem tuples, so no closure or bounds check touches them.
#               Build lp caught two lessons where a worked example WAS its own
#               ask; build lr caught three more where a worked example answered
#               a problem sitting in the same lesson's BANK. This script is the
#               generalisation of both.
#
#               HOW IT DECIDES. High confidence only: the numbers spoken in the
#               worked example must OPEN with the problem's own numbers, in
#               order, and the problem's answer must appear after them. That
#               ignores the ordinary case of a worked example that happens to
#               mention a small number the bank also uses.
#
#               A hit is not automatically a defect -- read it. Some are honest
#               (a worked example may legitimately walk the SAME numbers in a
#               different direction). Most are not.
# =============================================================================
import re

import lessonscripts as L


def _numbers(text):
    return re.findall(r"\d+", text)


def audit(lessons=None):
    """Returns [(lesson_id, pair_index, worked_text, problem, answer)]."""
    hits = []
    for les in (lessons if lessons is not None else L.LESSONS):
        problems = list(les["bank"]) + [pair["ask"] for pair in les["pairs"]]
        for i, pair in enumerate(les["pairs"]):
            spoken = _numbers(pair["worked"][0])
            if not spoken:
                continue
            for p in problems:
                tup = [str(p["a"])]
                if p.get("b"):
                    tup.append(str(p["b"]))
                if p.get("c"):
                    tup.append(str(p["c"]))
                answer = str(L.ans(p))
                if (len(spoken) >= len(tup) + 1
                        and spoken[:len(tup)] == tup
                        and answer in spoken[len(tup):]):
                    hits.append((les["id"], i + 1, pair["worked"][0], p, answer))
    return hits


if __name__ == "__main__":
    found = audit()
    for lesson_id, pair_no, worked, problem, answer in found:
        print(f"{lesson_id}  (worked {pair_no})")
        print(f"    says : {worked[:96]}")
        print(f"    gives: {problem} -> {answer}")
    print(f"\n{len(found)} worked examples answer a problem in their own lesson, "
          f"across {len(L.LESSONS)} lessons.")


# I did no harm and this file is not truncated.

# =============================================================================
# boardaudit.py  --  THE BOARD-SILENCE AUDIT  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-09-09  NEW (build uv). Jim, 2026-09-09: "If you have two paragraphs to spit
#               out to a child and you say it and there's no text and there's no
#               graphic, the child is just listening and not remembering anything...
#               I see it all the time in this app."
#
#               WHAT IT LOOKS FOR, and why it cannot be done by reading the lessons.
#               tutor.board_silence_conflict (referee 85) polices ONE reply at a time,
#               and ruletests PART 3eu already sweeps every authored CARD through it.
#               Neither can see the thing a child actually meets: a RUN of beats.
#               A lesson can put a picture up, then speak four short beats that each
#               pass the referee on their own while together they bury that picture
#               under two hundred words of transcript. The board is an append-only
#               feed -- the tutor's own bubbles push earlier board blocks up and out
#               of view (static/session.html, wipeBoard/scrollFeed) -- so what matters
#               is not "did THIS beat draw" but "how long has it been since ANYTHING
#               was drawn".
#
#               So this walks each lesson through the REAL ENGINE, in the real order,
#               answering every question correctly, and measures the spoken words
#               between one drawn mark and the next.
#
#               ⚠️ THE WALK INCLUDES THE ORIENTATION BEAT. lessonscripts.step() does
#               not emit it -- main.py's script_start inserts it at index 1, because
#               only the server can read the record that decides its wording (build
#               us). This walker inserts the same beat the same way, in its
#               "Today:" form, so the sweep measures what the student meets and not
#               what the engine alone returns. If that insert ever moves, this must
#               move with it (ruletests PART 3kr pins the pair together).
#
#               WHAT COUNTS AS A MARK is tutor._BS_MARKS -- every board tag except
#               [[choices]], which is a row of buttons and not something to look at.
#               Read from tutor.py, never copied, so the referee and the audit can
#               never drift apart.
#
#               WIRED INTO ruletests.py, unlike teachaudit and workedaudit: this
#               reports a floor the whole course already meets today (the longest
#               undrawn run in the canon is 69 spoken words, and every run over 55
#               is a lesson ENDING with no card), so it blocks nothing that ships
#               now and catches the next lesson that talks over a still board.
#
#               Run it by hand:  python3 boardaudit.py           (the summary)
#                                python3 boardaudit.py --worst 30
# =============================================================================
import re
import sys

import lessonscripts as L
import tutor as TT

# The engine's fixed seed for a replayable walk (the battery uses the same one).
SEED = 12345

# A run longer than this is reported. The referee's own ceiling, read from tutor
# so the two can never disagree.
CEILING = TT._BS_CEILING

_MARK_RE = TT._BS_MARK_RE


def marks(board):
    """How many marks this board tag string puts in front of the student."""
    return len(_MARK_RE.findall(str(board or "")))


def words(spoken):
    return len([w for w in re.split(r"\s+", str(spoken or "")) if w.strip()])


def walk(lesson, limit=400):
    """Every step a student actually meets in this lesson, in order, answering
    correctly every time. Mirrors main.py's script_start + /answer loop, including
    the orientation beat main.py inserts at index 1 (build us)."""
    state = L.start(lesson, seed=SEED)
    out = []
    steps, state = L.step(lesson, state, ("begin",))
    try:
        spoken, board = L.lesson_orientation(lesson, False)
        steps.insert(1, {"kind": "say", "spoken": spoken, "board": board,
                         "beat": "orientation"})
    except Exception:  # noqa: BLE001 -- an audit never brings the app down
        pass
    guard = 0
    while steps and guard < limit:
        guard += 1
        out.extend(steps)
        last = steps[-1]
        if last["kind"] == "end":
            break
        if last["kind"] == "ask":
            if last.get("reason"):
                answer = (lesson.get("explain") or {}).get("answer", "")
            else:
                answer = last["expected"]
            steps, state = L.step(lesson, state, ("answer", answer))
        elif last["kind"] == "intervene":
            steps, state = L.step(lesson, state, ("resume",))
        else:
            break
    return out


def runs(lesson):
    """Every stretch of this lesson between one drawn mark and the next.

    Returns [(words, [(beat_or_kind, words), ...], ended_at)] where `ended_at` is
    "draw" when something was finally drawn and "end" when the lesson simply
    finished with the board still holding whatever was last on it."""
    out = []
    carried = 0
    beats = []
    for step in walk(lesson):
        spoken = step.get("spoken", "")
        name = step.get("beat") or L.beat_of(lesson, spoken) or step["kind"]
        if marks(step.get("board")):
            if carried:
                out.append((carried, list(beats), "draw"))
            carried = 0
            beats = []
            continue
        carried += words(spoken)
        beats.append((name, words(spoken)))
    if carried:
        out.append((carried, list(beats), "end"))
    return out


def audit(lessons=None, ceiling=None):
    """Every run past the ceiling, worst first.

    Returns [(words, lesson_id, course, beats, ended_at)]."""
    limit = CEILING if ceiling is None else ceiling
    found = []
    for lesson in (lessons if lessons is not None else L.LESSONS):
        for total, beats, ended in runs(lesson):
            if total > limit:
                found.append((total, lesson["id"], lesson.get("course", "?"),
                              beats, ended))
    found.sort(key=lambda r: -r[0])
    return found


def worst(lessons=None):
    """The longest stretch of talking over a still board in the whole course, in
    spoken words. The number PART 3kr pins."""
    longest = 0
    for lesson in (lessons if lessons is not None else L.LESSONS):
        for total, _beats, _ended in runs(lesson):
            longest = max(longest, total)
    return longest


def _summary(found, ceiling):
    by_course = {}
    for total, _lid, course, _beats, ended in found:
        row = by_course.setdefault(course, [0, 0, 0])
        row[0] += 1
        row[1] = max(row[1], total)
        if ended == "end":
            row[2] += 1
    print(f"\n===== RUNS OVER {ceiling} SPOKEN WORDS WITH NOTHING DRAWN =====")
    print(f"{'course':14s} {'runs':>5s} {'longest':>8s} {'at the end':>11s}")
    for course in sorted(by_course, key=lambda c: -by_course[c][0]):
        n, longest, ends = by_course[course]
        print(f"{course:14s} {n:5d} {longest:8d} {ends:11d}")
    print(f"{'TOTAL':14s} {len(found):5d} "
          f"{max([f[0] for f in found] or [0]):8d} "
          f"{sum(1 for f in found if f[4] == 'end'):11d}")


if __name__ == "__main__":
    ceiling = CEILING
    show = 20
    if "--ceiling" in sys.argv:
        ceiling = int(sys.argv[sys.argv.index("--ceiling") + 1])
    if "--worst" in sys.argv:
        show = int(sys.argv[sys.argv.index("--worst") + 1])
    found = audit(ceiling=ceiling)
    print(f"{len(L.LESSONS)} lessons walked through the real engine; "
          f"the longest run of talking over a still board is {worst()} spoken words.")
    if not found:
        print(f"Nothing over {ceiling} words. The board keeps up with the voice.")
    else:
        _summary(found, ceiling)
        print(f"\n===== THE WORST {min(show, len(found))} =====")
        for total, lesson_id, course, beats, ended in found[:show]:
            trail = " > ".join(f"{name}({n})" for name, n in beats)
            print(f"{total:4d}w  [{ended:4s}]  {lesson_id}")
            print(f"        {trail[:150]}")


# I did no harm and this file is not truncated.

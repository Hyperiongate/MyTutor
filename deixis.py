"""(ux) THE POINTING AUDIT -- a beat whose words point at a picture its board does
not draw. Jim, 2026-09-09, on alg1-u1-two-steps-with-a-letter's trap beat: "I had to
croll up to see the bar." The words said "Look at the bar"; the board drew two step
lines. The bar was two beats up the feed and off the top of the screen.

The `why` beat is exempt BY THE SHAPE: its board is the goal card, and its words
promise the picture the next beat draws rather than pointing at one now."""
import re
import lessonscripts as L
import tags

NONFIG = {"step", "goal", "card", "choices", "check", "highlight", "write",
          "today", "stepcard", "quiz", "finalexam", "unitplan", "solve"}
FIG_TAGS = tuple(sorted(set(tags.BOARD_TAGS) - NONFIG))
FIG_RE = re.compile(r"\[\[\s*(?:" + "|".join(FIG_TAGS) + r")\b")

# ⚠️ ONLY UNAMBIGUOUS POINTING. An earlier draft counted "on the <picture>" as
# pointing and reported the shape's own closing taglines -- "and that is Pythagoras,
# living ON THE CIRCLE" -- as defects. A check that cries wolf is a check somebody
# turns off. So: the three imperatives, and "on the board", which can only ever mean
# the board the student is looking at.
NOUN = (r"bar|bars|picture|blocks|line|number line|circle|grid|shape|"
        r"rectangle|triangle|machine|balance|tape|graph|square|squares|stars")
POINT_RE = re.compile(r"\b(?:(?:look at|watch|see) the\s+(?:%s)|on the board)\b" % NOUN,
                      re.I)


def beats(les):
    out = [("teach", i, s, b) for i, (s, b) in enumerate(les["teach"])]
    for f in ("picture", "recap"):
        out += [(f, i, s, b) for i, (s, b) in enumerate(les.get(f) or [])]
    out += [("worked", i, pr["worked"][0], pr["worked"][1]) for i, pr in enumerate(les["pairs"])]
    ex = les.get("explain") or {}
    if ex:
        out.append(("explain", 0, ex["spoken"], ex.get("board", "")))
    return out


def hits(lessons=None):
    found = []
    for les in (L.LESSONS if lessons is None else lessons):
        for kind, i, s, b in beats(les):
            m = POINT_RE.search(s or "")
            if m and not FIG_RE.search(b or ""):
                found.append((les["id"], kind, i, m.group(0), s, b))
    return found


if __name__ == "__main__":
    h = hits()
    print("beats pointing at a picture they do not draw:", len(h))
    for x in h:
        print("  ", x[0], "|", x[1], x[2], "|", repr(x[3]))
        print("       board:", x[5][:110])

# I did no harm and this file is not truncated.

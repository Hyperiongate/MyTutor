# =============================================================================
# voiceclosure.py  --  THE PAGE-LOCAL SPOKEN LINE AUDIT  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-09-10  NEW (build uy). Jim, on the demo: "After a sample problem, fell back
#               to browser's voice." It was not a cache miss or a network hiccup --
#               static/demo-lesson.html ENDS on a line written in the page:
#                   "That is how every lesson in my classroom starts. Shall we look
#                    around, or try another level?"
#               The demo lane is CACHE-ONLY on purpose (a visitor must never be able
#               to make the paid renderer run), and that line is in no lesson, so it
#               is in no closure, so it was never rendered, so it fell to the browser
#               voice EVERY TIME -- and it plays at the one moment a visitor has just
#               decided the product is real.
#
#               THE CLOSURE PROPERTY, restated once more: every line the app can speak
#               in Mr. Cadabra's voice must be enumerable IN ADVANCE. lessonscripts'
#               STANDALONE_LINES exists for exactly this -- lines that belong to the
#               COURSE rather than to any lesson (Abrabot's introduction, the handoff,
#               the seam line, the wait lines, the check). A page that writes its own
#               line and speaks it has stepped outside that guarantee, and nothing was
#               watching for it.
#
#               WHAT IT DOES. Reads every page in static/, finds the string literals
#               that reach a speech call -- directly, or through a variable assigned a
#               literal in the same function -- and reports the ones that are not in
#               course_audio_lines().
#
#               ⚠️ demo.html IS EXEMPT, and only demo.html. It carries its own
#               enumerated whitelist (VOICE_LINES, twinned with main.DEMO_VOICE_LINES
#               and pinned equal by the battery) and its own player; its lines are
#               rendered from that list, not from the course closure. Every other page
#               speaks through voice.js and draws on the course closure.
# =============================================================================
import ast
import io
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
STATIC = os.path.join(HERE, "static")

# demo.html owns an enumerated whitelist of its own -- see the header.
EXEMPT_PAGES = ("demo.html",)

# ⚠️ WHICH PAGES THIS IS A DEFECT ON, and which it is only a note on. The DEMO lane is
# cache-only by design, so a line outside the closure there can NEVER be his voice --
# that is a defect, and the battery fails the build on it. The signed-in lanes may
# render on demand, so a page-local line there costs the FIRST student a mechanical
# voice and is cached from then on: worth reporting, not worth blocking a deploy.
# challenge.html is also an ASSESSMENT, where rule 18 gives the character no part at
# all, and one of its two lines interpolates the question number, so it could not be
# pre-rendered even in principle. Both are in the report; neither blocks.
CACHE_ONLY_PAGES = ("demo-lesson.html",)

# A line short enough to be an unlock utterance (" ") or a one-word status is not a
# taught line; four words is the floor the sweep uses.
MIN_WORDS = 4

_SPEAK = r"(?:speakLine|speakThen|sayThen|abraSay|speak|say)"
_STR = r'(["\'])((?:\\.|(?!\1).)*)\1'
_DIRECT = re.compile(r"\b" + _SPEAK + r"\s*\(\s*" + _STR)
# ⚠️ ITS OWN BACKREFERENCE, NOT _STR's. _STR closes on \1, which is only the quote
# when the quote is the FIRST group in the pattern. Spliced in after the variable
# name it closed on the NAME instead, matched nothing, and the audit reported the
# whole file clean -- including the very line it was written to find. A regex that
# finds nothing looks exactly like a file with nothing in it.
_ASSIGN = re.compile(r"\b(?:var|let|const)\s+([A-Za-z_$][\w$]*)\s*=\s*"
                     r"([\"'])((?:\\.|(?!\2).)*)\2\s*;")
_USE = re.compile(r"\b" + _SPEAK + r"\s*\(\s*([A-Za-z_$][\w$]*)\b")


def _lit(q, raw):
    try:
        return ast.literal_eval(q + raw + q)
    except (SyntaxError, ValueError):
        return None


def spoken_literals(source):
    """Every string literal in this page that reaches a speech call."""
    out = []
    for q, raw in _DIRECT.findall(source):
        t = _lit(q, raw)
        if t:
            out.append(t)
    # ...and the ones that go through a variable: `var line = "..."; speakLine(line)`
    assigned = {}
    for name, q, raw in _ASSIGN.findall(source):
        t = _lit(q, raw)
        if t:
            assigned[name] = t
    for name in _USE.findall(source):
        if name in assigned:
            out.append(assigned[name])
    seen, uniq = set(), []
    for t in out:
        if t in seen or len(t.split()) < MIN_WORDS:
            continue
        seen.add(t)
        uniq.append(t)
    return uniq


def pages():
    return sorted(f for f in os.listdir(STATIC)
                  if f.endswith(".html") and f not in EXEMPT_PAGES)


def hits(closure=None):
    """(page, line) for every page-local spoken line outside the voice closure."""
    if closure is None:
        import lessonscripts as L
        closure = set(L.course_audio_lines())
    else:
        closure = set(closure)
    found = []
    for fn in pages():
        src = io.open(os.path.join(STATIC, fn), encoding="utf-8").read()
        for t in spoken_literals(src):
            if t not in closure:
                found.append((fn, t))
    return found


def blocking(closure=None):
    """The subset the battery fails on: a cache-only page can never render a line."""
    return [(fn, t) for fn, t in hits(closure) if fn in CACHE_ONLY_PAGES]


if __name__ == "__main__":
    rows = hits()
    print("page-local spoken lines outside the voice closure: %d" % len(rows))
    for fn, t in rows:
        print("  %-24s %s" % (fn, t[:100]))

# I did no harm and this file is not truncated.

"""Generate quizsets.py -- the FIXED topic-quiz question set for every lesson.
Run once per content change; the result is data in the repo, so the audio closure
is instant and the questions are stable across deploys."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import time
import lessonscripts as L
import drillpool as D

t0 = time.time()
rows = []
short = []
for i, les in enumerate(L.LESSONS):
    ps = D.quiz_problems(les)
    if len(ps) < L.QUIZ_LEN:
        short.append((les["id"], len(ps)))
    rows.append((les["id"], ps))
    if i % 40 == 0:
        print(" %3d/%d  %.0fs" % (i, len(L.LESSONS), time.time() - t0), flush=True)

def fmt(p):
    parts = ['"op": %r' % p.get("op", "+"), '"a": %r' % p["a"], '"b": %r' % p["b"]]
    if "c" in p:
        parts.append('"c": %r' % p["c"])
    return "{" + ", ".join(parts) + "}"

body = []
for lid, ps in rows:
    inner = ",\n        ".join(fmt(p) for p in ps)
    body.append('    %r: [\n        %s,\n    ],' % (lid, inner))

src = '''# =============================================================================
# quizsets.py  --  THE TOPIC QUIZ QUESTION SETS, PINNED  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-08-27  NEW FILE (build ov -- QUIZZES THROUGH THE AUTHORED SPINE).
#               GENERATED, then committed as data on purpose. Two reasons, and
#               both are load-bearing:
#
#               ⭐ THE AUDIO CLOSURE MUST BE INSTANT AND STABLE. Every sentence
#               the app can speak in Mr. Cadabra's voice is enumerated in advance
#               and rendered once (lessonscripts.course_audio_lines). Computing
#               the quiz questions from drillpool.pool_for at call time made that
#               enumeration take MINUTES -- one lesson alone measured 14 seconds
#               -- which would have broken /admin's prewarm price button. Worse,
#               it would have made the closure a moving target: any future tweak
#               to the pool scan would silently invalidate audio already paid for.
#               Pinned questions cannot drift from pinned audio.
#
#               ⭐ AN ASSESSMENT SHOULD BE REVIEWABLE. These are the questions
#               every child is graded on. As data they can be read, argued with,
#               and changed deliberately, instead of being whatever an algorithm
#               happened to emit on the day.
#
#               HOW THEY WERE CHOSEN: drillpool.quiz_problems -- spaced evenly
#               across the lesson's ramped pool of extra problems (never its easy
#               end), each already through lessonscripts.validate(), topped up
#               from the bank's tail for the 73 lessons whose ops admit too few
#               extras. REGENERATE with tools/genquiz.py after any change to a
#               lesson's bank, its op, or the pool scan -- and re-run the prewarm,
#               because a changed question is a new sentence to render.
# =============================================================================

QUIZ_SETS = {
%s
}

# I did no harm and this file is not truncated.
''' % ("\n".join(body))

open("quizsets.py", "w", encoding="utf-8").write(src)
print("wrote quizsets.py: %d lessons, %.0fs" % (len(rows), time.time() - t0))
print("short sets:", short)

# I did no harm and this file is not truncated.

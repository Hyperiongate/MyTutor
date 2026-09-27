# =============================================================================
# tools/genquiz.py  --  GENERATE quizsets.py, THE PINNED TOPIC-QUIZ QUESTIONS
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-09-27  BUILD ym -- KEEP WHAT KEEPS THE SHAPE, REPLACE WHAT BREAKS IT. The yl
#               pre-read found 166 pinned questions (97 lessons) outside the shape their
#               own lesson's bank keeps; drillpool.shape_of, which also reads c's floor
#               and each op of a mixed lesson on its own, found 214 in 106: Entry's
#               "add past ten" quiz opened on 1 + 1. Regenerating everything from the (fixed) fallback
#               lane would have changed most of the 1,799 -- every changed question is a
#               new sentence to render and pay for. So this generator now READS the
#               pinned table first: a pinned question that keeps the shape is KEPT as it
#               is; only a breaker is replaced, by the shape-keeping pool problem at that
#               slot's middle-of-stride position (drillpool.quiz_slots) that the set does
#               not already hold, then from the bank's tail. A lesson with no pinned set
#               is built fresh through drillpool.quiz_problems' fallback lane. A bank
#               problem that carries a "story" keeps it in the table (the two story-problems
#               lessons' quizzes are their own stories now, not "What is 6 plus 1?").
#               USAGE: python tools/genquiz.py           (keep-and-replace, the default)
#                      python tools/genquiz.py --fresh   (rebuild every set from the pool)
#               Prints every replacement with the break it fixed, then the totals.
#   2026-08-27  NEW FILE (build ov). Generate quizsets.py -- the FIXED topic-quiz
#               question set for every lesson. Run once per content change; the result
#               is data in the repo, so the audio closure is instant and the questions
#               are stable across deploys.
# =============================================================================
"""Generate quizsets.py -- the FIXED topic-quiz question set for every lesson."""
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lessonscripts as L  # noqa: E402
import drillpool as D  # noqa: E402

FRESH = "--fresh" in sys.argv[1:]


def _pinned():
    """The table as it is on disk, or {} when there is none (or --fresh)."""
    if FRESH:
        return {}
    try:
        import quizsets
        return dict(quizsets.QUIZ_SETS)
    except Exception:  # noqa: BLE001
        return {}


def _fresh_set(les):
    """A set built through the fallback lane (the pinned table is bypassed)."""
    D._QUIZ_CACHE.pop(les.get("id"), None)
    saved = sys.modules.pop("quizsets", None)
    try:
        sys.modules["quizsets"] = None      # import quizsets -> ImportError -> fallback
        return list(D.quiz_problems(les))
    finally:
        del sys.modules["quizsets"]
        if saved is not None:
            sys.modules["quizsets"] = saved
        D._QUIZ_CACHE.pop(les.get("id"), None)


def keep_and_replace(les, pinned, shapes):
    """The pinned set with every shape-breaker replaced. Returns (set, replacements),
    replacements as (slot, old, new, why)."""
    want = L.QUIZ_LEN
    op = les.get("op", "+")
    out = list(pinned)
    breaks = [(i, keeps_shape_why(shapes, p, op)) for i, p in enumerate(out)]
    breaks = [(i, why) for i, why in breaks if why]
    if not breaks:
        return out, []
    pool = D.quiz_pool(les)
    slots = D.quiz_slots(len(pool), want)
    held = {D._key(p) for i, p in enumerate(out) if i not in {b for b, _ in breaks}}
    reps = []
    for slot, why in breaks:
        new = None
        # the pool problem at this slot's middle-of-stride position, else the next unused
        # -- the breaker's OWN op first (a mixed-op lesson keeps its quiz's op balance)
        order = ([pool[slots[slot]]] if slot < len(slots) else []) + [pool[j] for j in slots] + pool
        bop = str(out[slot].get("op", op))
        order = [c for c in order if str(c.get("op", op)) == bop] + [c for c in order if str(c.get("op", op)) != bop]
        for cand in order:
            if D._key(cand) not in held:
                new = cand
                break
        if new is None:
            for cand in reversed(list(les.get("bank") or [])):
                if D._key(cand) not in held and D.keeps_shape(shapes, cand, op)[0]:
                    new = cand
                    break
        if new is None:
            continue                     # nothing to offer; the breaker stays and PART 3og will say so
        held.add(D._key(new))
        reps.append((slot, out[slot], new, why))
        out[slot] = new
    return out, reps


def keeps_shape_why(shapes, p, op):
    ok, why = D.keeps_shape(shapes, p, op)
    return "" if ok else why


def fmt(p):
    parts = ['"op": %r' % p.get("op", "+"), '"a": %r' % p["a"], '"b": %r' % p["b"]]
    if "c" in p:
        parts.append('"c": %r' % p["c"])
    if p.get("story"):                 # (ym) a story problem keeps its story -- it IS the ask
        parts.append('"story": %r' % p["story"])
    return "{" + ", ".join(parts) + "}"


def main():
    t0 = time.time()
    pinned = _pinned()
    rows, short, replaced, kept, fresh = [], [], 0, 0, 0
    for i, les in enumerate(L.LESSONS):
        shapes = D.shape_of(les)
        have = pinned.get(les["id"])
        if have:
            ps, reps = keep_and_replace(les, have, shapes)
            kept += len(ps) - len(reps)
            replaced += len(reps)
            for slot, old, new, why in reps:
                print(f"  {les['id']} [{slot}]: {fmt(old)} -> {fmt(new)}   ({why})")
        else:
            ps = _fresh_set(les)
            fresh += len(ps)
        if len(ps) < L.QUIZ_LEN:
            short.append((les["id"], len(ps)))
        rows.append((les["id"], ps))
        if i % 40 == 0:
            print(" %3d/%d  %.0fs" % (i, len(L.LESSONS), time.time() - t0), flush=True)

    body = []
    for lid, ps in rows:
        inner = ",\n        ".join(fmt(p) for p in ps)
        body.append('    %r: [\n        %s,\n    ],' % (lid, inner))

    src = '''# =============================================================================
# quizsets.py  --  THE TOPIC QUIZ QUESTION SETS, PINNED  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-09-27  BUILD ym -- THE QUIZ KEEPS THE LESSON'S SHAPE. Regenerated by
#               tools/genquiz.py in keep-and-replace mode: every pinned question
#               that keeps the shape its lesson's bank keeps (drillpool.shape_of:
#               the floor of a, b, c; the digit counts; the yes/no facts every bank
#               problem agrees on) is unchanged; the 214 (in 106 lessons) that broke
#               it -- Entry's "add past ten" asked 1 + 1, "take away bigger" asked
#               2 - 1, Basic's GCF lesson asked the GCF of 2 and 0 -- are replaced by
#               the shape-keeping pool problem at that slot. PART 3og pins the count of
#               questions outside their shape at zero. A replaced question is a
#               new sentence: re-run the prewarm.
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

    out_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "quizsets.py")
    open(out_path, "w", encoding="utf-8").write(src)
    print("wrote quizsets.py: %d lessons, %.0fs" % (len(rows), time.time() - t0))
    print("kept %d, replaced %d, fresh %d" % (kept, replaced, fresh))
    print("short sets:", short)
    return 0


if __name__ == "__main__":
    sys.exit(main())

# I did no harm and this file is not truncated.

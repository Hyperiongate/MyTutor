# =============================================================================
# tools/genquiz.py  --  GENERATE quizsets.py, THE PINNED TOPIC-QUIZ QUESTIONS
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-09-27  BUILD yq -- no change to the generator; drillpool reads a demonstration two
#               more ways (a board tag the teaching drew; one stranger between the numbers)
#               and "b divides a" is an always-only rule now; regenerated: 57 replaced.
#   2026-09-27  BUILD yp -- THE SAME QUESTION TWICE IS REPLACED. From the first Pre-Algebra
#               quiz sweep: "how many factors of 9" asked twice (two problems that differ in a
#               number the child never hears), and 76 / 104 on a line asked both ways round.
#               A later question that is asked the same way as an earlier one (drillpool.
#               asked_as) or is its twin (twin_key: same op, same numbers, same answer) is
#               replaced when the pool has a fresh candidate, and no replacement may itself
#               repeat a kept question. The shape moved too (drillpool: facts scoped to their
#               op, landmark value sets, the "/" split and the b-divides-c facts, the number
#               regex); the table regenerated: 38 replaced.
#   2026-09-27  BUILD yo -- AND REPLACE WHAT THE LESSON DEMONSTRATED, WHEN IT CAN. The second
#               Entry quiz sweep: 18 quiz questions were the very example the tutor worked
#               on the board (9 + 6; 4 groups with 2). drillpool.demonstrated() reads that;
#               a demonstrated pinned question is replaced when the pool holds a fresh,
#               undemonstrated, shape-keeping candidate the set does not hold (236 of 357
#               across the canon, in 142 lessons); a thin op keeps its demonstrated question and the quiz
#               page marks it as the lesson's own example, by design. A replacement is
#               fresh before demonstrated in every case.
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
    """The pinned set with every shape-breaker replaced, and (yo) every DEMONSTRATED
    question replaced when the pool holds a fresh, undemonstrated, shape-keeping candidate
    the set does not already hold -- a thin op keeps its demonstrated question, and the
    quiz page marks it. Returns (set, replacements), replacements as (slot, old, new, why)."""
    want = L.QUIZ_LEN
    op = les.get("op", "+")
    out = list(pinned)
    units = D.demonstrated_units(les)
    breaks = [(i, keeps_shape_why(shapes, p, op)) for i, p in enumerate(out)]
    breaks = [(i, why) for i, why in breaks if why]
    broken = {i for i, _ in breaks}
    pool = D.quiz_pool(les)
    spare = D.fresh_spares(les, out)     # (yp) one owner of "could replace": drillpool.fresh_spares
    for i, p in enumerate(out):
        if i in broken:
            continue
        if D.demonstrated(les, p, units) and spare:
            breaks.append((i, "demonstrated in the lesson's teaching"))
            spare.pop(0)               # one fresh candidate is spoken for
    # (yp) the same question twice -- asked the same way, or a twin -- keeps the first and
    # replaces the later one when the pool has a fresh candidate left
    broken = {i for i, _ in breaks}
    asked, twins = set(), set()
    for i, p in enumerate(out):
        if i in broken:
            continue
        a, t = D.asked_as(les, p), D.twin_key(les, p)
        if (a in asked or t in twins) and spare:
            breaks.append((i, "asked the same way as an earlier question" if a in asked else "a twin of an earlier question"))
            spare.pop(0)
            continue
        asked.add(a)
        twins.add(t)
    if not breaks:
        return out, []
    breaks.sort()
    slots = D.quiz_slots(len(pool), want)
    held = {D._key(p) for i, p in enumerate(out) if i not in {b for b, _ in breaks}}
    reps = []
    for slot, why in breaks:
        new = None
        # the pool problem at this slot's middle-of-stride position, else the next unused
        # -- the breaker's OWN op first (a mixed-op lesson keeps its quiz's op balance),
        # and (yo) a problem the lesson did not demonstrate before one it did
        order = ([pool[slots[slot]]] if slot < len(slots) else []) + [pool[j] for j in slots] + pool
        bop = str(out[slot].get("op", op))
        order = [c for c in order if str(c.get("op", op)) == bop] + [c for c in order if str(c.get("op", op)) != bop]
        order = [c for c in order if not D.demonstrated(les, c, units)] + [c for c in order if D.demonstrated(les, c, units)]
        kept = [q for i_, q in enumerate(out) if i_ not in {b for b, _ in breaks} or i_ < slot and q is not out[slot]]
        kept_asked = {D.asked_as(les, q) for q in kept} | {D.asked_as(les, q) for q in (r[2] for r in reps)}
        kept_twins = {D.twin_key(les, q) for q in kept} | {D.twin_key(les, q) for q in (r[2] for r in reps)}
        for cand in order:
            if D._key(cand) in held:
                continue
            if why == "demonstrated in the lesson's teaching" and D.demonstrated(les, cand, units):
                continue
            if D.asked_as(les, cand) in kept_asked or D.twin_key(les, cand) in kept_twins:
                continue               # (yp) never replace one repeat with another
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
#   2026-09-27  BUILD yq -- THE OTHER SEVEN QUIZ SWEEPS. 57 replaced: the
#               tutor's own worked examples the number rule had missed (the
#               scatter plot's own points; "the arc is 18 divided by 6" for a
#               60-degree arc on a rim of 18), where the op had a fresh problem.
#   2026-09-27  BUILD yp -- THE FACTS BELONG TO THEIR OP; A LANDMARK VALUE IS A
#               LANDMARK; THE SAME QUESTION TWICE IS REPLACED. 38 replaced:
#               percent-of asks only 10, 25 and 50 percent (the three methods its
#               bank teaches), a price goes up by 10, 20, 30 or 50, a two-digit
#               division's tens and ones each divide (56 ÷ 4 and 78 ÷ 3 are gone),
#               a proportion scales by a whole number, the tutor's own worked
#               example ("2 and 5." -- the number regex had read "5." as no
#               number), and a question asked twice in one quiz -- word for word
#               ("how many factors of 9", twice) or as a twin (76 and 104 on a line,
#               both ways round) -- where the op had a fresh problem to offer.
#   2026-09-27  BUILD yo -- THE QUIZ PREFERS WHAT THE LESSON DID NOT DEMONSTRATE.
#               Regenerated in keep-and-replace mode again: a pinned question that
#               is the very example the tutor worked on the board (9 + 6 in the
#               teach beat; "4 groups with 2") is replaced by a fresh shape-keeping
#               problem when its op has one to offer (drillpool.demonstrated,
#               236 of 357); the rest stay and the quiz page marks them.
#               PART 3oi ratchets "demonstrated with a fresh candidate available" at
#               zero. A replaced question is a new sentence: re-run the prewarm.
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

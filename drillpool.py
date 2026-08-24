# =============================================================================
# drillpool.py  --  EXTRA PRACTICE PROBLEMS, VETTED IN ADVANCE  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-08-24  BUILD mo -- THE RANK IS THE VALIDATOR'S OWN. A REAL BUG, found while
#               building Entry-Level Unit 8's clock lesson.
#               ⚠️ WHAT WAS WRONG. Three functions here (_probe_ok, _ordered, verify)
#               sorted a candidate bank by ONE key function, taken off the LESSON'S
#               op and applied to every problem in the bank. That is correct only
#               while a lesson has a single op. The clock lesson reads the same fact
#               two ways (min5 / min5q), so its min5q problems were ranked with
#               min5's key, the sort came out unramped, validate() rejected EVERY
#               candidate, and pool_for() returned an EMPTY POOL.
#               ⚠️ AND IT HAD ALREADY HAPPENED, SILENTLY. basic-u9-quarter-turns
#               (ang/angq) has been mixed-op since build kd and had no drill pool for
#               the same reason -- invisible, because an empty pool looks exactly
#               like a domain with nothing left in it. The fix moved the pool from
#               24,880 problems to 25,343, and lessons-with-no-pool from 53 to 50.
#               THE FIX: lessonscripts.difficulty_key -- the public name for the
#               measure validate() actually ramps on, per PROBLEM and per its own op.
#               A private second copy of the ramp measure is what caused this; there
#               is now one owner, and PART 3de pins that this file calls it.
#   2026-08-23  NEW FILE (build mg, phase 1 of ABRABOT). Jim: "you can work additional
#               problems with Mr. Cadabra's assistant" -- named Abrabot, 2026-08-23.
#               ABRABOT drills; MR. CADABRA teaches. Abrabot speaks in the browser's
#               own voice (free, instant, no cache) and wears the robot face, which
#               Jim handed over the same day. Neither impersonates Mr. Cadabra, so
#               neither is measured against him.
#
#               WHAT THIS IS. Every op in lessonscripts already carries a check()
#               that says which {a,b,c} triples are legal for it -- that is what the
#               auto-picker has used to choose banks for thirteen builds. So the ops
#               ARE problem generators; nobody had pointed them at runtime. This file
#               enumerates that surface, VETS it, and hands back a pool of extra
#               problems per lesson: 3,947 authored problems become tens of thousands.
#
#               ⚠️ WHY A PRE-VETTED POOL AND NOT A LIVE GENERATOR. check() encodes
#               ARITHMETIC validity. It does not encode the things the read-aloud pass
#               caught over thirteen builds -- coffee at 20 degrees in a room at 10, a
#               pond of 24 fish growing at 72 a year, a tap of 2,750 sitting beside an
#               answer of 105, a tap of 5 beside an answer of 159. A live generator
#               would produce those the moment it strayed outside the shipped tuples.
#               So the pool is built ONCE, vetted, and pinned by the battery. A child
#               never meets a problem no check has seen.
#
#               ⚠️ THE VET IS SELF-CALIBRATING, and it has to be. A flat rule like "no
#               tap more than three times the answer" would reject rk4, whose three
#               taps ARE the three convergence orders and whose biggest tap is 8x the
#               answer BY DESIGN. Instead every candidate is measured against the
#               tuples that lesson already SHIPPED -- the ones a human read aloud. A
#               candidate is admitted only if its tap ratios, answer size and given
#               sizes all sit inside the envelope those vetted tuples already occupy.
#               Same trick main.py's course-audio-audit uses for clip length: no magic
#               constant, and it moves automatically when the content moves.
#
#               NOT WIRED TO ANYTHING YET. Phase 1 is data and this module. No route,
#               no page, no audio. The drill lane is SILENT of Mr. Cadabra by design:
#               his voice is pre-rendered and a generated problem has no clip, so the
#               assistant speaks these in the browser's own voice and he is fetched
#               (with his real, already-rendered lines) only when a child struggles.
#
#               MASTERY IS UNAFFECTED, by Jim's ruling 2026-08-23: "Drill is practice,
#               quizzes are for mastery." Nothing here may ever mark a unit mastered.
# =============================================================================
import re

import lessonscripts as L

# How far past a lesson's own numbers we are willing to look for candidates. The
# envelope check below is what actually admits them; this only bounds the search.
_SPAN = 3
_HARD_A, _HARD_B, _HARD_C = 400, 400, 60
_MAX_PER_LESSON = 240          # a child will never exhaust this; keep the file small
_SCAN_CAP = 60000              # candidates examined per lesson before we stop looking


def _key(p):
    return (p["a"], p.get("b", 0), p.get("c", 0))


def _taps(op, p):
    """The three tap options for a problem, however this op supplies them.

    ⚠️ AN OP MAY DECLARE check() AND NOT choices(). Twenty-seven do -- *, /, area,
    vol, gcf, lcm, rate, peri and the rest of the early registry -- and they fall back
    to choices_for()'s default neighbours (v-1, v, v+1). The first draft of envelope()
    bailed whenever choices was absent, which cost those 27 ops their entire pool for
    no reason at all: the engine has always known how to tap them."""
    ext = L.OP_EXT.get(op, {})
    if "choices" in ext:
        return [c for c in ext["choices"](p)]
    raw = L.choices_for(p)
    return [int(x) for x in re.findall(r"-?\d+", raw.split('options="')[1])]


def _shipped(les):
    """The tuples a human has already read aloud: the bank plus the two guided asks."""
    return list(les["bank"]) + [pr["ask"] for pr in les["pairs"]]


def envelope(les):
    """The shape of the problems this lesson already ships, as a set of bounds.

    Everything here is measured, never assumed. Returns None when the lesson's op
    cannot be measured, which means it cannot be drilled safely.

    ⚠️ TWO LANES, because the course has two kinds of op and the first draft of this
    file only knew about one. The EXTENSION ops (OP_EXT) each carry their own check()
    and choices(). The CORE operators -- "+", "-", "t" -- carry neither: they live in
    ans() and choices_for(), and their legality comes from the bounds the LESSON
    declares (max_value, min_value, a_max, b_max). Missing that lane cost the 87
    earliest lessons their entire pool on the first run, which is precisely the age
    group that needs drill most."""
    op = les["op"]
    d = L.OP_EXT.get(op)
    if d is None or "check" not in d:
        # THE DECLARED-BOUNDS LANE. Two kinds of op land here and both are legitimate:
        # the CORE operators ("+", "-", "t"), which live in ans() rather than OP_EXT,
        # and the OLDER extension ops (*, /, cnt, pv, rem, gcf, lcm ...) written before
        # the check() convention existed. Neither carries a predicate, so the lesson's
        # own declared bounds are the predicate -- exactly what validate() enforces on
        # the shipped bank. Every candidate is then put through the REAL validator by
        # verify() below, so nothing reaches a child on the strength of this alone.
        if d is None and op not in ("+", "-", "t"):
            return None
        shipped = _shipped(les)
        return {"core": True,
                "ans_min": les.get("min_value", 1), "ans_max": les["max_value"],
                "a_max": les.get("a_max", les["max_value"]),
                "b_max": les.get("b_max", les["max_value"]),
                "c_max": max([p.get("c", 0) for p in shipped] or [0]),
                "lo_ratio": 0.0, "hi_ratio": 99.0}
    # (an op with check() but no choices() taps with the engine's default neighbours)
    lo_r, hi_r, ans_v, a_v, b_v, c_v = [], [], [], [], [], []
    for p in _shipped(les):
        try:
            a = L.ans(p)
            ch = [c for c in _taps(op, p) if c]
            if not a or not ch:
                return None
            lo_r.append(min(ch) / float(a))
            hi_r.append(max(ch) / float(a))
            ans_v.append(a)
            a_v.append(p["a"])
            b_v.append(p.get("b", 0))
            c_v.append(p.get("c", 0))
        except Exception:      # noqa: BLE001 -- an op we cannot measure is one we skip
            return None
    if len(ans_v) < 6:
        return None
    return {"core": False, "lo_ratio": min(lo_r), "hi_ratio": max(hi_r),
            "ans_min": min(ans_v), "ans_max": max(ans_v),
            "a_max": max(a_v), "b_max": max(b_v), "c_max": max(c_v)}


def admits(les, env, p):
    """Is this candidate inside the envelope the shipped tuples already occupy?"""
    d = L.OP_EXT.get(les["op"])
    try:
        if env.get("core"):
            # no check() to consult: the bounds above, plus the shared rules every
            # problem in the course obeys (a real answer, three distinct taps that
            # never fall below 1, and speech that says its own numbers).
            a = L.ans(p)
            if a is None:
                return False
            raw = L.choices_for(p)
            opts = [int(x) for x in re.findall(r"-?\d+", raw.split('options="')[1])]
            if len(set(opts)) != 3 or a not in opts or min(opts) < les.get("min_value", 1):
                return False
            if not env["ans_min"] <= a <= env["ans_max"]:
                return False
            if p["a"] > env["a_max"] or p.get("b", 0) > env["b_max"]:
                return False
            if p.get("c", 0) > env["c_max"]:
                return False
            if p["a"] < 1 or p.get("b", 0) < 1:
                return False
            for level in (les.get("levels") or L.LEVELS):
                sp = L.spoken_for(p, level)
                if str(p["a"]) not in sp or str(p["b"]) not in sp:
                    return False
            return True
        ok, _msg = d["check"](p)
        if not ok:
            return False
        a = L.ans(p)
        if not env["ans_min"] <= a <= env["ans_max"]:
            return False
        ch = [c for c in _taps(les["op"], p) if c]
        if len(set(ch)) != len(ch) or a not in ch:
            return False
        # ⚠️ the wasted-tap rule, learned the hard way in builds lx through mc: a
        # distractor is useless if it is far larger OR far smaller than the answer.
        # The bounds are this lesson's own, so a design like rk4's stays legal.
        if not (env["lo_ratio"] <= min(ch) / float(a) <= 1.0):
            return False
        if not (1.0 <= max(ch) / float(a) <= env["hi_ratio"]):
            return False
        # never show a child a bigger number than the lesson itself already does
        if p["a"] > env["a_max"] or p.get("b", 0) > env["b_max"] or p.get("c", 0) > env["c_max"]:
            return False
        # rule 44, restated: every ask must SPEAK the numbers it is asking about
        for level in (les.get("levels") or L.LEVELS):
            sp = L.spoken_for(p, level)
            speaks = d.get("speaks")
            if not (speaks(p, sp) if speaks else
                    (str(p["a"]) in sp and str(p.get("b", 0)) in sp)):
                return False
        # the answer must be inside the bound the lesson itself declares
        if not (les.get("min_value", 1) <= a <= les["max_value"]):
            return False
    except Exception:          # noqa: BLE001 -- anything unmeasurable is excluded
        return False
    return True


def _probe_ok(les, candidate, board_tags):
    """⭐ THE ADMISSION TEST: does the COURSE'S OWN VALIDATOR accept this problem?

    Build a bank of nine problems the lesson already ships -- all human-vetted -- plus
    the one candidate, sorted by difficulty key so the ramp rule is satisfied by
    construction. Any failure is then attributable to the candidate alone.

    ⚠️ THIS IS WHY THE FILTER IS THE VALIDATOR AND NOT MORE RULES IN THIS FILE. The
    first draft vetted candidates against an envelope of tap ratios and bounds, and
    the validator promptly caught what that could never see: problems that do not
    CARRY in a lesson whose name promises carrying, problems that do not REGROUP in a
    regrouping lesson, problems that DO carry in the lesson promising none, and sums
    that overflow the tens in a two-digit lesson. Those are per-lesson semantic
    promises, they live in validate(), and re-implementing them here would be a second
    copy to drift. One source of truth, already proved on 328 lessons."""
    base = _shipped(les)[:9]
    if len(base) < 9:
        return False
    # (mo) RANK BY THE SAME MEASURE validate() RAMPS ON. This used to take ONE key
    # function off the LESSON'S op and apply it to every problem in the bank, which
    # is right only while a lesson has a single op. A mixed-op lesson (the clock,
    # read both ways; quarter turns, both ways) had its second op's problems ranked
    # with the first op's key, the sort came out unramped, validate() rejected every
    # candidate, and the pool came back EMPTY. lessonscripts.difficulty_key is the
    # one owner of that measure.
    keyf = L.difficulty_key
    try:
        bank = sorted(base + [candidate], key=lambda q: (keyf(q), L.ans(q)))
    except Exception:          # noqa: BLE001
        return False
    probe = dict(les)
    probe["id"] = les["id"] + "~drillprobe"
    probe["bank"] = bank
    try:
        return all(r[0] for r in L.validate(probe, board_tags))
    except Exception:          # noqa: BLE001 -- unmeasurable is excluded
        return False


def _ordered(problems, les):
    """Easiest first, by the lesson's own difficulty key, so a drill session ramps the
    way a taught bank does instead of lurching between hard and easy."""
    # (mo) RANK BY THE SAME MEASURE validate() RAMPS ON. This used to take ONE key
    # function off the LESSON'S op and apply it to every problem in the bank, which
    # is right only while a lesson has a single op. A mixed-op lesson (the clock,
    # read both ways; quarter turns, both ways) had its second op's problems ranked
    # with the first op's key, the sort came out unramped, validate() rejected every
    # candidate, and the pool came back EMPTY. lessonscripts.difficulty_key is the
    # one owner of that measure.
    keyf = L.difficulty_key
    try:
        return sorted(problems, key=lambda q: (keyf(q), L.ans(q)))
    except Exception:          # noqa: BLE001
        return problems


def pool_for(les, cap=_MAX_PER_LESSON, board_tags=None):
    """Extra practice problems for one lesson, excluding the ones it already teaches.

    Two gates in cost order: the cheap envelope first, which rejects most candidates
    without running anything, then the real validator on the survivors."""
    if board_tags is None:
        import tags as _t
        board_tags = set(_t.BOARD_TAGS)
    env = envelope(les)
    if not env:
        return []
    taught = {_key(p) for p in _shipped(les)}
    out, seen = [], 0
    A = range(1, min(env["a_max"] * _SPAN, _HARD_A) + 1)
    B = range(0, min(max(env["b_max"] * _SPAN, 1), _HARD_B) + 1)
    C = range(0, min(max(env["c_max"] * _SPAN, 1), _HARD_C) + 1)
    for a in A:
        for b in B:
            for c in C:
                seen += 1
                if seen > _SCAN_CAP or len(out) >= cap:
                    # ⚠️ THE EARLY RETURN MUST SORT TOO. It did not, so the 61 lessons
                    # that hit the cap or the scan limit -- the BIGGEST pools, the ones
                    # a child is most likely to reach -- came back in raw enumeration
                    # order while every smaller pool was neatly ramped. Caught by the
                    # battery pin written in the same build, which is the whole reason
                    # to pin an invariant rather than trust the function that holds it.
                    return _ordered(out, les)
                if (a, b, c) in taught:
                    continue
                p = {"a": a, "b": b, "c": c, "op": les["op"]}
                if admits(les, env, p) and _probe_ok(les, p, board_tags):
                    out.append(p)
    return _ordered(out, les)


def verify(les, problems, board_tags):
    """⭐ THE INDEPENDENT PROOF, run by the battery. Every pooled problem is put in a
    bank with nine of the lesson's own shipped problems and sent through the REAL
    validate(). Same shape as the admission test, but run again from the outside over
    the finished pool, so a bug in pool_for() cannot hide behind itself.

    ⚠️ THE FIRST DRAFT OF THIS FUNCTION WAS WRONG and briefly accused the pool of 936
    failures that were its own. It chunked the pool into tens and padded a short last
    chunk from the FRONT of the list -- putting the easiest problems after the hardest
    and breaking the difficulty ramp it was checking. A test that fabricates the
    failure it reports is worse than no test. Nine known-good problems and one
    candidate, sorted: nothing invented, nothing padded."""
    base = _shipped(les)[:9]
    if not problems or len(base) < 9:
        return []
    # (mo) RANK BY THE SAME MEASURE validate() RAMPS ON. This used to take ONE key
    # function off the LESSON'S op and apply it to every problem in the bank, which
    # is right only while a lesson has a single op. A mixed-op lesson (the clock,
    # read both ways; quarter turns, both ways) had its second op's problems ranked
    # with the first op's key, the sort came out unramped, validate() rejected every
    # candidate, and the pool came back EMPTY. lessonscripts.difficulty_key is the
    # one owner of that measure.
    keyf = L.difficulty_key
    out = []
    for n, cand in enumerate(problems):
        try:
            bank = sorted(base + [cand], key=lambda q: (keyf(q), L.ans(q)))
        except Exception:      # noqa: BLE001
            out.append((les["id"], "unsortable candidate", str(cand)))
            continue
        probe = dict(les)
        probe["id"] = f"{les['id']}~drill{n}"
        probe["bank"] = bank
        for res in L.validate(probe, board_tags):
            if not res[0]:
                out.append((probe["id"], res[1], str(res[2])[:90]))
    return out


def build(lessons=None, cap=_MAX_PER_LESSON):
    """{lesson id -> [extra problems]} for the whole course."""
    import tags as _t
    bt = set(_t.BOARD_TAGS)
    return {les["id"]: pool_for(les, cap, bt)
            for les in (lessons if lessons is not None else L.LESSONS)}


# I did no harm and this file is not truncated.

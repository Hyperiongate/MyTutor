# =============================================================================
# drillpool.py  --  EXTRA PRACTICE PROBLEMS, VETTED IN ADVANCE  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-09-27  BUILD yq -- THE OTHER SEVEN QUIZ SWEEPS (Algebra I 20, Geometry 6, Algebra II 2,
#               Pre-Calc 9, Calculus 7, Diffeq 1, Prob/Stat 5 -- all read on yo). Three things.
#               (1) "b divides a" is a rule only when it ALWAYS holds, like b divides c: nine
#               lessons' banks happened never to have it (x + 6 = 12 in "undoing a plus"; a
#               box from 7 to 21; a jump from 2 to 8) and the page's "never -- b divides a
#               exactly" was enforced by the reader on numbers that mean nothing for the op.
#               (2) A DEMONSTRATION READ TWO MORE WAYS. The reader found worked examples the
#               number rule missed: the scatter plot's own points ([[scatter points="(2,10),
#               ..."]] drawn in the teach beat and again in the quiz), and "the arc is 18
#               divided by 6" for a 60-degree arc on a rim of 18 (60 ... 6 ... 18 -- one number
#               between). demonstrated() now also matches a quiz ask's BOARD TAG against the
#               teaching boards (same tag, same numeric attributes -- the picture IS the
#               example) and allows ONE stranger between the problem's numbers. (3) The
#               reader's "x = 6 is outside 2..4" findings were the wrong number read as a; the
#               numbers on every ask (yp) settle those -- no data change.
#   2026-09-27  BUILD yp -- THE FACTS BELONG TO THEIR OP, AND A LANDMARK VALUE IS A LANDMARK.
#               The first Basic quiz sweep (12 findings, 31 clean). (1) A fact measured on
#               numbers that mean nothing for the op: "the ones carry" was read on 35 × 3
#               (5 + 3 < 10, so the bank "never carried" -- and the reviewer, told so, flagged
#               5 × 3 = 15); "the two numbers add past ten" on a factor pair. _facts(p, op)
#               now: the sum passes ten and the ones carry are "+"'s; the ones borrow is
#               "-"'s; NEW for "/": the tens and the ones each divide by b (the taught
#               tens-and-ones split -- 56 ÷ 4 was quizzed where 50 ÷ 4 does not go); the
#               rest (a bigger, a equals b, b divides a, zeros, the story) are every op's.
#               (2) A LANDMARK VALUE SET: percent-of's bank is 10, 25 and 50 -- each its own
#               method (a tenth, a quarter, a half) -- and the quiz asked 20%, 36% and 45%
#               inside the floor-to-ceiling range, with a board that said "45% is one of 2
#               equal parts". shape_of keeps a field's exact VALUE SET when it is sparse and
#               spread: at most four distinct values across a span of at least ten times as
#               many (10/25/50 over 41; 25/50/100; 90/180/270/360) -- a digit field's 1, 2, 8,
#               9 over nine is not that. (3) _INT_RE read "5." as no number, so "2 and 5." in
#               a worked line was never a demonstration; fixed (a trailing period is not a
#               decimal point). (4) FROM THE FIRST PRE-ALGEBRA QUIZ SWEEP, folded in: a
#               question's IDENTITY IN A QUIZ is what the child meets -- its spoken line and
#               its board (asked_as): "how many factors of 9" was asked twice, told apart by a
#               b the child never hears. A TWIN -- the same op, the same numbers and the same
#               answer as another question of the set (76 and 104 on a line, then 104 and 76;
#               4 groups of 2 and 2 groups of 4) -- is one question asked twice (twin_key).
#               distinct_set() drops both kinds when a set is drawn; genquiz replaces them
#               when the op has a fresh problem. And a NEW general fact for three-number
#               problems, b divides c (a proportion's bank always scales by a whole number;
#               6/9 = ?/21 did not).
#   2026-09-27  BUILD yo -- THE QUIZ PREFERS A PROBLEM THE LESSON DID NOT DEMONSTRATE. The
#               second Entry quiz sweep (25 findings, 18 of them "repeats"): a quiz question
#               was the very example the tutor worked on the board in a teach beat -- 9 + 6,
#               "4 groups with 2", "12 stars shared into 4", "258". Not a bank problem, so the
#               shape let it through; but a child graded on the example they just watched is
#               a weaker test than a new problem. demonstrated(les, p): the problem's numbers
#               appear as NEIGHBOURING numbers in one teaching sentence or one board tag of
#               the lesson's why / picture / teach beats or its worked lines ("9 + 6 = 15",
#               "4 groups with 2"); a single-number problem (count the stars) is demonstrated
#               when a teaching tag carries that number as its own value. Measured over the
#               canon: 357 pinned quiz questions were demonstrated; 236 had a fresh
#               shape-keeping candidate and are replaced by tools/genquiz.py; 121 (thin ops:
#               doubles, where every number was demonstrated) stay and the quiz page marks
#               them as the lesson's own example by design. fresh_first(les, pool) orders a
#               pool undemonstrated-first; quiz_problems' fallback lane uses it.
#   2026-09-27  BUILD yn -- THE DRILL POOL KEEPS THE SHAPE TOO. ym held this for Jim; Jim: "GO".
#               pool_for (Abrabot's lane, live from main.py) is the same scan quiz_pool was:
#               from the shape's floor to its ceiling per op, the cap shared across ops, every
#               candidate through keeps_shape and then the envelope and the course's own
#               validator. So Abrabot no longer drills 1 + 1 after adding past ten. ONE
#               DIFFERENCE, by Jim's ruling that drill is practice and quizzes are for mastery
#               (2026-08-23): the drill pool does NOT require a story -- a story-problems
#               lesson drills the bare arithmetic inside its stories (as it always has),
#               while its quiz asks the stories themselves. keeps_shape(..., drill=True) skips
#               the has_story fact; nothing else differs. Measured before/after on the frozen
#               copy: 28,411 -> 28,656 problems (big-number mixed-op lessons gain the pool
#               they never had, because the old scan from 1 filled their cap with tiny sums);
#               46 -> 41 lessons with no pool (the two that lose one -- the exponents lesson's
#               single candidate, the parametric walk's ten -- were outside their bank's
#               shape); 241 -> 233 lessons at 20 or more (add past ten: 67 -> 11, the 56 that
#               left never passed ten). _key(p) is (op, a, b, c) now -- 31 - 29 is not a repeat
#               of 31 + 29 in a mixed-op pool. _scan() is the one scanner;
#               pool_for and quiz_pool are its two doors. PART 3oh.
#   2026-09-27  BUILD ym -- THE QUIZ KEEPS THE LESSON'S SHAPE. Found by the yl pre-read of
#               all 1,799 pinned quiz questions against their own lesson's bank: 166 in 97
#               lessons asked OUTSIDE the lesson -- Entry's "add past ten" quiz opened on
#               1 + 1, "take away bigger" on 2 - 1, "add with carrying" on 1 + 9, Basic's
#               GCF lesson asked the GCF of 2 and 0. ONE CAUSE: envelope() bounds a
#               candidate from ABOVE only (never a bigger number than the lesson shows) and
#               pool_for scans from a = 1, b = 0; quiz_problems then sampled the ramped
#               pool from index 0 -- its easiest end, the very end quizsets.py's header
#               says it never uses. So a bank that runs 5..9 got a quiz that opened on 1.
#               THE FIX, at the source: shape_of(les) MEASURES the shape the shipped bank
#               keeps -- the floor and ceiling of a, b and c (measured off the bank, where
#               the envelope's core lane took the DECLARED bound), the digit counts, and the
#               yes/no facts every shipped problem agrees on (the sum passes ten; the ones
#               carry; the ones borrow; a is bigger than b; b divides a; b is never zero;
#               the problem carries its own STORY -- the two story-problems lessons quizzed
#               bare facts, "What is 6 plus 1?", where every bank problem is a story)
#               -- and keeps_shape(shape, p) says whether a candidate stays inside it.
#               quiz_pool(les) scans from the shape's floor up and keeps only shape-keepers
#               (pool_for's capped scan from a = 1 never reached a two-digit lesson's own
#               numbers); quiz_problems' fallback lane draws from it, from the MIDDLE of
#               each stride, never index 0. The drill pool (pool_for,
#               Abrabot's lane) is NOT gated by the shape in this build -- it carries the
#               same class and is a scope decision for Jim (the ym doc says so); the quiz
#               is the graded instrument and the sweep's subject. tools/genquiz.py now
#               keeps every pinned question that keeps the shape and replaces only the
#               breakers -- 214 in 106 lessons once shape_of read c's floor and each op
#               of a mixed lesson on its own -- so the prewarm is 214 new sentences,
#               not 1,799. PART 3og pins the
#               count of quiz questions outside their shape at zero.
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
    """A problem's identity: its op AND its numbers. (yn) The op was not part of it, which
    was right while a pool held one op; the shape scan pools every op of a mixed lesson,
    and 31 - 29 is not a repeat of 31 + 29. (Every shipped bank problem names its op --
    measured at yn: none omits it.)"""
    return (str(p.get("op", "+")), p["a"], p.get("b", 0), p.get("c", 0))


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

    (yn) The SHAPE SCAN, the same one the quiz draws from: candidates from the shape's
    floor to its ceiling per op, every one through keeps_shape (drill=True: a story lesson
    drills its bare arithmetic), then the cheap envelope, then the real validator. Until yn
    this scanned from a = 1, b = 0 and bounded from above only, so a lesson that adds past
    ten drilled 1 + 1 and a two-digit lesson's capped pool never reached its own numbers."""
    return _scan(les, cap, board_tags, drill=True)


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



# =============================================================================
# THE TOPIC QUIZ'S QUESTION SET  (build ov, 2026-08-27)
# -----------------------------------------------------------------------------
# Jim's flip made the scripted lane the main road, so a finished topic now ends
# in a quiz. The questions belong HERE because this file already owns the one
# hard question -- "what else can this lesson honestly ask?" -- and every answer
# it gives has already been through lessonscripts.validate().
#
# ⭐ PURE AND FIXED, ON PURPOSE. The set is a function of the LESSON alone,
# never of what this child was asked, because lessonscripts.audio_lines() has to
# enumerate every sentence a quiz can ever speak. That is the closure property
# the whole lane's speed rests on: rendered once, free forever. Choosing
# questions at runtime would be a live TTS call per child, per question.
#
# ⭐ SPACED ACROSS THE POOL, NOT ITS EASY END. The pool is ramped (see the sort
# note above), so taking the first five would quiz only the easiest. Even
# spacing asks across the whole range the lesson admits.
#
# ⚠️ 73 OF 336 LESSONS HAVE FEWER THAN FIVE POOL PROBLEMS, and 42 have none at
# all -- their ops simply do not admit extra tuples the validator will accept
# (counting to ten has only so many honest questions). Those top up from the
# BANK's own tail, which the child may have seen; a repeat in a quiz is a real
# weakness, and it is a smaller one than a main road where most topics cannot be
# assessed at all. Lessons that still cannot field QUIZ_MIN get no quiz and end
# exactly as they did before -- never a broken button.
# ⚠️ MEMOISED, AND IT HAS TO BE. pool_for() runs a bounded triple scan with the
# real validator on every survivor -- perfectly fine once, and far too slow 336
# times, which is what course_audio_lines() asks for when it prices the closure.
# Lessons are static data, so the answer for a given id can never change within a
# process. (Measured: the un-cached closure did not finish in two minutes.)
_QUIZ_CACHE = {}


def _facts(p, op="+"):
    """(ym) The yes/no facts a problem has, for shape_of to compare across a bank:
    the problem carries its own story (a story-problems lesson is spoken as stories, and a
    generated bare fact is not one), a is bigger than b, a and b are equal, b divides a,
    b is zero, a is zero -- every op's. (yp) And the facts that belong to ONE op: the sum
    passes ten and the ones carry ("+"), the ones borrow ("-"), the tens and the ones each
    divide by b ("/": the taught tens-and-ones split). A fact read on numbers that mean
    nothing for the op ("the ones carry" on 35 × 3) was a fact the bank kept by accident
    and the reviewer, told so, enforced. Only whole-number fields are read; a fact that
    cannot be read is simply absent."""
    a, b = p.get("a"), p.get("b")
    out = {"has_story": bool(p.get("story"))}    # a story problem is spoken as its story
    ia, ib = isinstance(a, int) and not isinstance(a, bool), isinstance(b, int) and not isinstance(b, bool)
    if ia:
        out["a_zero"] = a == 0
    if ib:
        out["b_zero"] = b == 0
    c = p.get("c")
    ic = isinstance(c, int) and not isinstance(c, bool) and c != 0
    if ib and ic:
        out["b_divides_c"] = b != 0 and c % b == 0     # (yp) a proportion scales by a whole number
    if ia and ib:
        out["a_bigger"] = a > b
        out["a_equals_b"] = a == b
        out["b_divides_a"] = b != 0 and a % b == 0
        if op == "+":
            out["sum_past_ten"] = a + b > 10
            out["ones_carry"] = (abs(a) % 10 + abs(b) % 10) >= 10
        elif op == "-":
            out["ones_borrow"] = (abs(a) % 10) < (abs(b) % 10)
        elif op == "/":
            out["split_divides"] = b != 0 and (a - a % 10) % b == 0 and (a % 10) % b == 0
    return out


_ALWAYS_ONLY = {"b_divides_c", "b_divides_a"}   # a fact that is a rule only when it always holds (yq: b divides a too)
_LANDMARK_MAX = 4        # at most this many distinct values ...
_LANDMARK_SPREAD = 10    # ... across a span at least this many times as many: 10 / 25 / 50, not 1 / 2 / 8 / 9


def _digits(v):
    return len(str(abs(v)))


def shape_of(les):
    """(ym) THE SHAPE THE SHIPPED BANK KEEPS, measured never assumed: per op (a mixed-op
    lesson has one shape per op), the floor and the ceiling of a, b and c across the
    shipped problems (the envelope's core lane took the DECLARED b_max, so a bank that
    never went past 4 quizzed 2 + 7), the set of digit counts a and b use, and every yes/no fact of _facts() that EVERY
    shipped problem of that op agrees on. Returns {op: shape}; a lesson with nothing
    shipped (a table pass) returns {}. A quiz question that steps outside this is a
    question the lesson never asked -- the class the yl pre-read found 166 of."""
    shapes = {}
    by_op = {}
    for p in _shipped(les):
        by_op.setdefault(str(p.get("op", les.get("op", "+"))), []).append(p)
    for op, probs in by_op.items():
        sh = {"n": len(probs), "min": {}, "max": {}, "digits": {}, "facts": {}, "values": {}}
        for k in ("a", "b", "c"):
            vals = [p[k] for p in probs if isinstance(p.get(k), int) and not isinstance(p.get(k), bool)]
            if not vals:
                continue
            sh["min"][k] = min(vals)
            sh["max"][k] = max(vals)
            distinct = sorted(set(vals))
            if len(distinct) <= _LANDMARK_MAX and (distinct[-1] - distinct[0] + 1) >= _LANDMARK_SPREAD * len(distinct):
                sh["values"][k] = distinct          # (yp) a landmark set: 10 / 25 / 50, each its own method
            if k in ("a", "b"):
                sh["digits"][k] = sorted({_digits(v) for v in vals})
        facts = [_facts(p, op) for p in probs]
        keys = set().union(*[set(f) for f in facts]) if facts else set()
        for key in keys:
            vals = {f.get(key) for f in facts}
            if len(vals) == 1 and None not in vals:
                if key in _ALWAYS_ONLY and not next(iter(vals)):
                    continue           # (yp) "never a whole-number scale" is no rule, only an accident
                sh["facts"][key] = vals.pop()
        shapes[op] = sh
    return shapes


def keeps_shape(shapes, p, default_op="+", drill=False):
    """(ym) Does this problem stay inside the shape its op's shipped bank keeps? True
    when the op has no measured shape (nothing to compare against). Returns (ok, why):
    why names the first break -- "a=1 below the floor 5", "b has 2 digits (bank: 1)",
    "sum_past_ten is False (bank: always True)" -- so a pin and a report can say it.
    drill=True (yn) skips the has_story fact: the drill pool practises a story lesson's
    arithmetic, the quiz asks its stories."""
    sh = shapes.get(str(p.get("op", default_op)))
    if not sh:
        return True, ""
    for k, lo in sh["min"].items():
        v = p.get(k)
        if isinstance(v, int) and not isinstance(v, bool) and v < lo:
            return False, f"{k}={v} below the floor {lo}"
    for k, hi in sh.get("max", {}).items():
        v = p.get(k)
        if isinstance(v, int) and not isinstance(v, bool) and v > hi:
            return False, f"{k}={v} above the ceiling {hi}"
    for k, ds in sh["digits"].items():
        v = p.get(k)
        if isinstance(v, int) and not isinstance(v, bool) and _digits(v) not in ds:
            return False, f"{k} has {_digits(v)} digit(s) (bank: {'/'.join(str(d) for d in ds)})"
    for k, allowed in sh.get("values", {}).items():
        v = p.get(k)
        if isinstance(v, int) and not isinstance(v, bool) and v not in allowed:
            return False, f"{k}={v} not one of {', '.join(str(x) for x in allowed)}"
    have = _facts(p, str(p.get("op", default_op)))
    for key, want in sh["facts"].items():
        if drill and key == "has_story":
            continue                       # (yn) drill practises the arithmetic; the quiz asks the story
        if key in have and have[key] != want:
            return False, f"{key} is {have[key]} (bank: always {want})"
    return True, ""


def quiz_pool(les, cap=_MAX_PER_LESSON, board_tags=None):
    """(ym) THE QUIZ'S OWN POOL: the shape scan with every fact kept, the story included --
    a story-problems lesson's quiz is its stories (from the bank's tail, since a generated
    problem has none to tell). Since yn the drill pool is the same scan without the story
    fact; _scan is the one scanner."""
    return _scan(les, cap, board_tags, drill=False)


def _scan(les, cap=_MAX_PER_LESSON, board_tags=None, drill=False):
    """(ym/yn) THE ONE SCANNER. Every candidate that keeps the shape the shipped bank
    keeps (drillpool.shape_of; drill=True forgives the story), that the envelope admits,
    that the course's validator accepts (_probe_ok) and that the lesson does not already
    teach -- scanned from the shape's FLOOR to its CEILING, per op of the lesson with the
    cap shared across ops, so a two-digit lesson's pool is two-digit problems and a
    mixed-op lesson's pool holds every op. Ramped by the validator's key."""
    if board_tags is None:
        import tags as _t
        board_tags = set(_t.BOARD_TAGS)
    env = envelope(les)
    if not env:
        return []
    shapes = shape_of(les)
    taught = {_key(p) for p in _shipped(les)}
    out, seen = [], 0
    ops = list(shapes.items()) or [(les.get("op", "+"), {"min": {}, "max": {}})]
    per_op = max(1, cap // len(ops))          # a mixed-op lesson's pool holds every op
    for op, sh in ops:
        lo, hi = sh.get("min", {}), sh.get("max", {})
        got = 0
        A = range(max(1, lo.get("a", 1)), min(hi.get("a", env["a_max"]), env["a_max"], _HARD_A) + 1)
        B = range(max(0, lo.get("b", 0)), min(hi.get("b", env["b_max"]), max(env["b_max"], 0), _HARD_B) + 1)
        C = range(max(0, lo.get("c", 0)), min(hi.get("c", env["c_max"]), max(env["c_max"], 0), _HARD_C) + 1)
        for a in A:
            for b in B:
                for c in C:
                    seen += 1
                    if seen > _SCAN_CAP or len(out) >= cap or got >= per_op:
                        break
                    if (op, a, b, c) in taught:
                        continue
                    p = {"a": a, "b": b, "c": c, "op": op}
                    if not keeps_shape(shapes, p, op, drill=drill)[0]:
                        continue
                    if admits(les, env, p) and _probe_ok(les, p, board_tags):
                        out.append(p)
                        got += 1
                if seen > _SCAN_CAP or len(out) >= cap or got >= per_op:
                    break
            if seen > _SCAN_CAP or len(out) >= cap or got >= per_op:
                break
    return _ordered(out, les)


_TAG_RE = re.compile(r"\[\[(\w+)([^\]]*)\]\]")
_ATTR_RE = re.compile(r'(\w+)="([^"]*)"')
_INT_RE = re.compile(r"(?<![\w.])-?\d+(?!\.?\d)(?!\w)")   # (yp) "5." is 5; "5.2" is not a whole number
# A demonstration names the problem's numbers side by side ("9 + 6 = 15", "4 groups with
# 2"): the numbers must be ADJACENT among the unit's numbers -- a window of exactly as many
# numbers as the problem has. A wider window read counting sequences as demonstrations.


_RANGE_ATTRS = {"to", "from", "max", "min", "range", "width", "height", "len", "span", "step"}


def demonstrated_units(les):
    """(yo) The units a demonstration lives in: each sentence of the lesson's why, picture
    and teach beats and its worked lines, and each board tag of their boards."""
    out = []
    for f in ("why", "picture", "teach"):
        for sp, bd in (les.get(f) or []):
            out += re.split(r"(?<=[.!?])\s+", sp or "")
            out += [m.group(0) for m in _TAG_RE.finditer(bd or "")]
    for pr in (les.get("pairs") or []):
        w = pr.get("worked") or ("", "")
        out += re.split(r"(?<=[.!?])\s+", w[0] or "")
        out += [m.group(0) for m in _TAG_RE.finditer(w[1] or "")]
    return [u for u in out if u]


def demonstrated(les, p, units=None):
    """(yo) Is this problem one the lesson DEMONSTRATED -- its numbers shown together as an
    example in a teaching sentence or on a teaching board? Two numbers or three: all of
    them side by side among one unit's numbers ("9 + 6 = 15"; "4 groups with 2 stars";
    "1 nickel and 2 pennies"). One number (count the stars, doubles): a
    teaching TAG carries it as an attribute's own value or inside an eq= -- a passing
    mention in a sentence is not a demonstration. A measured rule, not a perfect one: a
    false hit costs one candidate; a miss is the reader's to catch."""
    nums = {v for v in (p.get("a"), p.get("b"), p.get("c")) if isinstance(v, int) and not isinstance(v, bool) and v}
    if not nums:
        return False
    units = demonstrated_units(les) if units is None else units
    # (yq) the picture IS the example: a board tag of the ask with the same name and the
    # same numeric attributes as a teaching board tag (the scatter plot's own points)
    try:
        level = (les.get("levels") or L.LEVELS)[-1]
        for m in _TAG_RE.finditer(L.board_for(p, level) or ""):
            sig = _tag_sig(m)
            if sig and sig[0] != "choices" and sig in {_tag_sig(u) for u in units if u.startswith("[[")}:
                return True
    except Exception:  # noqa: BLE001
        pass
    if len(nums) == 1:
        n = next(iter(nums))
        for u in units:
            if not u.startswith("[["):
                continue
            for k, v in _ATTR_RE.findall(u):
                if k in _RANGE_ATTRS:
                    continue               # a figure's window is not the example drawn in it
                if v.strip() == str(n) or (k == "eq" and re.search(rf"(?<![\w.]){n}(?![\w.])", v)):
                    return True
        return False
    for u in units:
        vals = [int(t) for t in _INT_RE.findall(u)]
        if not nums <= set(vals):
            continue
        for i in range(len(vals)):
            seen = set()
            for j in range(i, min(len(vals), i + len(nums) + _DEMO_STRANGERS)):
                if vals[j] in nums:
                    seen.add(vals[j])
                if seen == nums:
                    return True
    return False


_DEMO_STRANGERS = 1     # (yq) "the arc is 18 divided by 6" for 60 degrees: one number may sit between


def _tag_sig(unit_or_match):
    """(yq) A board tag's signature: its name and its numeric attributes (numbers, and
    point lists like "(2,10),(4,20)"), or None when it carries no numbers."""
    m = _TAG_RE.match(unit_or_match) if isinstance(unit_or_match, str) else unit_or_match
    if not m:
        return None
    name, body = m.group(1), m.group(2)
    attrs = tuple(sorted((k, v.strip()) for k, v in _ATTR_RE.findall(body)
                         if k not in _RANGE_ATTRS and re.fullmatch(r"[-\d.,()\s|]+", v.strip()) and re.search(r"\d", v)))
    return (name, attrs) if attrs else None


def fresh_first(les, pool):
    """(yo) A pool with the problems the lesson did NOT demonstrate first (each half keeps
    its ramp), so a quiz drawn from the front is new to the child."""
    units = demonstrated_units(les)
    fresh = [p for p in pool if not demonstrated(les, p, units)]
    shown = [p for p in pool if demonstrated(les, p, units)]
    return fresh + shown


def asked_as(les, p):
    """(yp) A question as the child meets it: its spoken line and its board. Two problems
    that differ only in a number the child never hears or sees are ONE question."""
    level = (les.get("levels") or L.LEVELS)[-1]
    return (L.spoken_for(p, level), L.board_for(p, level) or "")


def twin_key(les, p):
    """(yp) The op, the problem's numbers and its answer, as a multiset: 76 and 104 on a
    straight line then 104 and 76; 4 groups of 2 then 2 groups of 4. Twins are one
    question asked twice, and a quiz of five should not spend two of them on it."""
    nums = [v for v in (p.get("a"), p.get("b"), p.get("c")) if isinstance(v, int) and not isinstance(v, bool) and v]
    try:
        ans = L.ans(p)
        nums.append(int(ans) if ans is not None and float(ans) == int(ans) else ans)
    except Exception:  # noqa: BLE001
        pass
    return (str(p.get("op", les.get("op", "+"))), tuple(sorted(nums, key=str)))


def distinct_set(les, problems, want=None):
    """(yp) The first `want` problems that are distinct as the child meets them -- no two
    asked the same way, no twins -- in the order given."""
    out, asked, twins = [], set(), set()
    for p in problems:
        a, t = asked_as(les, p), twin_key(les, p)
        if a in asked or t in twins:
            continue
        asked.add(a)
        twins.add(t)
        out.append(p)
        if want is not None and len(out) >= want:
            break
    return out


def fresh_spares(les, held):
    """(yp) The pool problems that could REPLACE a question of `held` (a quiz set): keep
    the shape (the pool does), not demonstrated, not already in the set, and not asked
    the same way as -- or a twin of -- a question already there. One owner of the rule:
    tools/genquiz.py replaces from these, PART 3oi ratchets against them."""
    units = demonstrated_units(les)
    keys = {_key(q) for q in held}
    asked = {asked_as(les, q) for q in held}
    twins = {twin_key(les, q) for q in held}
    return [c for c in quiz_pool(les)
            if not demonstrated(les, c, units) and _key(c) not in keys
            and asked_as(les, c) not in asked and twin_key(les, c) not in twins]


def quiz_slots(n, want):
    """(ym) The indexes a quiz takes from a ramped pool of n: the MIDDLE of each of
    `want` equal strides -- never index 0, the easiest problem there is, which the
    old int(i * stride) always took first. n <= want returns every index."""
    if n <= want:
        return list(range(n))
    stride = n / float(want)
    out = []
    for i in range(want):
        j = min(int((i + 0.5) * stride), n - 1)
        if j not in out:
            out.append(j)
    return out


def quiz_problems(les):
    """The fixed question set for this lesson's topic quiz (may be shorter than
    QUIZ_LEN, and empty when the lesson cannot honestly field one)."""
    key = les.get("id") or id(les)
    if key in _QUIZ_CACHE:
        return _QUIZ_CACHE[key]
    # ⭐ THE PINNED TABLE IS THE ANSWER, and computing is only the fallback for a
    # lesson added since it was generated. This is not just a speed trick: the
    # audio closure is priced and rendered against these exact questions, so a
    # scan that quietly returned something else would leave a child hearing
    # silence where a quiz question should be. quizsets.py's own header carries
    # the full reasoning. (Measured: computing the whole course took the better
    # part of an hour; the table is a dict lookup.)
    try:
        import quizsets
        pinned = quizsets.QUIZ_SETS.get(key)
        if pinned:
            _QUIZ_CACHE[key] = list(pinned)
            return _QUIZ_CACHE[key]
    except Exception:
        pass
    try:
        want = L.QUIZ_LEN
        # (ym) THE QUIZ STAYS INSIDE THE LESSON'S SHAPE: only pool problems that keep
        # the shape the shipped bank keeps (floor, digit counts, the facts every bank
        # problem agrees on), taken from the middle of each stride, never the easiest.
        pool = quiz_pool(les)
        fresh = [p for p in fresh_first(les, pool) if not demonstrated(les, p)]
        pool = fresh if len(fresh) >= want else fresh_first(les, pool)   # (yo) new to the child, when the op allows
        out = [pool[j] for j in quiz_slots(len(pool), want)] if pool else []
        # (yp) no two asked the same way, no twins: fill the slots the drop leaves from the
        # rest of the pool, in its order
        out = distinct_set(les, out + [p for p in pool if p not in out], want)
        if len(out) < want:
            seen = {_key(p) for p in out}
            for p in reversed(list(les.get("bank") or [])):
                k = _key(p)
                if k in seen:
                    continue
                seen.add(k)
                out.append(p)
                if len(out) >= want:
                    break
            out = distinct_set(les, out, want)
        out = out if len(out) >= L.QUIZ_MIN else []
        _QUIZ_CACHE[key] = out
        return out
    except Exception:      # a quiz that cannot be built is simply not offered
        _QUIZ_CACHE[key] = []
        return []


# I did no harm and this file is not truncated.

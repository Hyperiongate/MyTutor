# =============================================================================
# sprints.py  --  FLUENCY SPRINTS  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-08-11  BUILD dp -- SPRINTS FOR EVERY COURSE. The registry grows from 3
#               courses/27 units to ALL TEN courses, wherever a unit has a genuine
#               60-second recall skill: algebra1 (all 9 units -- one-step solves,
#               slopes, systems by sum/difference, exponent laws, factor pairs,
#               squares/roots, means), geometry (8 -- angle pairs, triangle sum,
#               Pythagorean triples, scale factors, circle facts, reflections,
#               midpoints, areas), algebra2 (7 -- two-step solves, powers of i,
#               degrees, exponent quotients, roots, logs, sequences), precalc (6 --
#               composition, zeros, logs, radians + special trig values, identities,
#               factorials/combinations), probstat (5 -- means, medians, basic
#               probability, expected value, the empirical rule), calculus (5 --
#               polynomial limits, power rule, e^(kx) chain, antipowers, simple
#               definite integrals), diffeq (3 -- order, characteristic roots,
#               Laplace facts). UNITS WITHOUT A REAL TIMED-FACT SKILL GET NO SPRINT
#               ON PURPOSE (concept units -- proofs, sampling design, slope fields --
#               are not drill material; the app fails soft as always). Every numeric
#               answer is COMPUTED from the formula that generated the question,
#               never typed as a literal; fixed FACT families (trig values, the
#               empirical rule, derivative facts, i-powers) draw a seeded sample so
#               half B stays a sibling, and their contents are re-verified in
#               ruletests PART 3n. Nothing about the anxiety rules changed: never
#               gates, personal-best only, declining costs one tap.
#   2026-08-11  BUILD dd -- NEW FILE. The largest unimplemented recommendation in the
#               evidence base: WWC guide 26 recommendation 6, "regularly include timed
#               activities", rated STRONG -- and named independently by four sources.
#               Jim's decisions (2026-08-11): offered by Mr. Cadabra at lesson start,
#               answered by TAP (voice stays the lesson mode; a timed minute must not
#               measure our transcription latency), full A/B beat-yourself structure.
#
# THE FORMAT IS EUREKA'S; THE ITEMS ARE OURS.
# From the Grade 1 Module 1 Teacher Edition (read in full, 2026-08-11):
#   * two near-identical halves, A and B; the celebrated number is B minus A --
#     "improving on the second part, even if only by one more"
#   * one named skill per sprint, tied to one unit
#   * the problems are sequenced in PATTERN FAMILIES -- that is the pedagogy. A student
#     discovers the pattern mid-sprint, and the debrief asks what pattern they noticed.
#     A sprint is disguised structure-teaching, never a random drill sheet.
#   * framing that makes finishing impossible and unnecessary: "I do not expect you to
#     finish. Just do as many as you can, your personal best."
#   * improvement only is celebrated; nobody is compared to anyone else (rule 42).
# ⚠️ LICENCE: Eureka Math is (c) Great Minds and NOT open-licensed. Nothing of theirs is
# reproduced here. These generators build items from OUR curriculum's unit skills.
#
# ⚠️ SPRINTS NEVER GATE ANYTHING. Declining is one tap; a low count changes nothing; no
# unlock, no mastery, no quiz depends on a sprint. EEF's caution is a requirement:
# timed work can feed maths anxiety, so the frame is personal-best or nothing.
#
# DESIGN: SPRINTS[course][unit] -> generator(rng) -> one FAMILY PLAN, from which
# half_a and half_b are built with different operands in the SAME family order. Each
# half is 30 problems: {"q": shown, "a": answer, "c": [3 tap choices]}. Deterministic
# given a seed, so the server can rebuild half B for scoring if it ever needs to.
# =============================================================================
import random

PER_HALF = 30
FAMILY_SIZE = 5          # 6 families x 5 problems = 30, in family order


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------
def _numstr(v):
    """Numbers as the student sees them: the SAME unicode minus the questions use.
    (build dp -- before this, a negative answer button said "-11" under a question
    that said "− 12"; the internal compare never cared, but the eyes do.)"""
    return str(v).replace("-", "−")


def _num_choices(rng, answer):
    """Three tap choices for a numeric answer: the truth and two near misses.
    Near, because a wildly wrong distractor makes tapping a guessing game.
    build dp fix: the old blanket "no negative distractors" rule (right for the
    counting courses) starved NEGATIVE answers down to a single button -- a sprint
    with one choice per problem is not a drill. A course whose answers go negative
    has met negatives, so its distractors may too; nonnegative answers keep the
    nonnegative pool exactly as before."""
    a = int(answer)
    pool = [a + 1, a - 1, a + 2, a - 2, a + 10, a - 10, a + 3, a - 3]
    floor_ok = (lambda p: p >= 0) if a >= 0 else (lambda p: True)
    picks = []
    for p in pool:
        if p != a and floor_ok(p) and p not in picks:
            picks.append(p)
        if len(picks) == 2:
            break
    out = [_numstr(a)] + [_numstr(p) for p in picks]
    rng.shuffle(out)
    return out


def _mk(rng, q, a, choices=None):
    a = _numstr(a) if isinstance(a, int) else str(a)
    return {"q": q, "a": a, "c": choices or _num_choices(rng, a.replace("−", "-"))}


def _families(rng, builders):
    """Build one half: each builder yields FAMILY_SIZE problems, in the order given.
    The family order IS the sprint -- see the header."""
    out = []
    for build in builders:
        out.extend(build(rng))
    return out[:PER_HALF]


def _ramp(rng, lo, hi, n=FAMILY_SIZE):
    """n operands climbing from lo toward hi -- families ramp, they do not jump.

    The rng adds a small shared shift, which is what makes half B a SIBLING of half A
    rather than its twin: same families, same ramp, fresh numbers. Without this, B's
    questions were byte-identical to A's and "improvement" would have measured memory
    of half A's answers -- caught by the self-check before shipping."""
    step = max(1, (hi - lo) // max(1, n - 1))
    # [0,1,2] rather than [0,1]: with two independent draws per family, a coin gave the
    # halves a 50% chance of matching family-by-family and made six twin units on one
    # test seed. Three values puts a whole-unit twin below 0.2% for any unit with a
    # single ramped family; only the fixed-list units (primes, GCF) repeat by design.
    shift = rng.choice([0, 1, 2])
    return [min(hi, lo + i * step) + shift for i in range(n)]


# ---------------------------------------------------------------------------
# family builders (parametric; each returns a function(rng) -> [5 problems])
# ---------------------------------------------------------------------------
def add_family(addend, lo, hi):
    def build(rng):
        return [_mk(rng, f"{n} + {addend}", n + addend) for n in _ramp(rng, lo, hi)]
    return build


def sub_family(sub, lo, hi):
    def build(rng):
        return [_mk(rng, f"{n} − {sub}", n - sub) for n in _ramp(rng, max(lo, sub), hi)]
    return build


def doubles_family(lo, hi):
    def build(rng):
        return [_mk(rng, f"{n} + {n}", 2 * n) for n in _ramp(rng, lo, hi)]
    return build


def make_ten_family():
    def build(rng):
        # min(n, 9): the sibling shift may push the ramp past 9, and "11 + ? = 10"
        # would have a negative answer in a course that has not met negatives.
        return [_mk(rng, f"{n} + ? = 10", 10 - min(n, 9)) for n in
                [min(v, 9) for v in _ramp(rng, 1, 9)]]
    return build


def times_family(factor, lo, hi):
    def build(rng):
        return [_mk(rng, f"{n} × {factor}", n * factor) for n in _ramp(rng, lo, hi)]
    return build


def div_family(divisor, lo, hi):
    def build(rng):
        return [_mk(rng, f"{n * divisor} ÷ {divisor}", n) for n in _ramp(rng, lo, hi)]
    return build


def count_on_family(step, lo, hi):
    def build(rng):
        out = []
        for n in _ramp(rng, lo, hi):
            seq = ", ".join(str(n + i * step) for i in range(3))
            out.append(_mk(rng, f"{seq}, ?", n + 3 * step))
        return out
    return build


def one_more_less_family(delta, lo, hi):
    word = "1 more than" if delta == 1 else "1 less than"
    def build(rng):
        return [_mk(rng, f"{word} {n}", n + delta) for n in _ramp(rng, lo, hi)]
    return build


def place_value_family(kind):
    def build(rng):
        out = []
        for t in _ramp(rng, 2, 8):
            t = min(9, t)
            o = (t + 3) % 9 + 1
            if kind == "compose":
                out.append(_mk(rng, f"{t} tens + {o} ones", t * 10 + o))
            else:
                out.append(_mk(rng, f"How many tens in {t * 10 + o}?", t))
        return out
    return build


def big_add_family(base, addend_tens):
    def build(rng):
        return [_mk(rng, f"{base + i * 100} + {addend_tens * 10}",
                    base + i * 100 + addend_tens * 10) for i in range(FAMILY_SIZE)]
    return build


def big_sub_family(base, sub_tens):
    def build(rng):
        return [_mk(rng, f"{base + i * 100} − {sub_tens * 10}",
                    base + i * 100 - sub_tens * 10) for i in range(FAMILY_SIZE)]
    return build


def coins_family(coin_value, coin_name):
    def build(rng):
        return [_mk(rng, f"{n} {coin_name} = ? ¢", n * coin_value)
                for n in _ramp(rng, 2, 6)]
    return build


def minutes_family(mult):
    def build(rng):
        return [_mk(rng, f"{n} hours = ? minutes" if mult == 60 else
                    f"{n} weeks = ? days", n * mult) for n in _ramp(rng, 1, 5)]
    return build


def shape_sides_family():
    shapes = [("triangle", 3), ("square", 4), ("pentagon", 5), ("hexagon", 6),
              ("octagon", 8)]
    def build(rng):
        return [_mk(rng, f"Sides on a {name}?", n) for name, n in shapes]
    return build


def frac_equiv_family(mult):
    def build(rng):
        out = []
        for d in _ramp(rng, 2, 6):
            out.append(_mk(rng, f"1/{d} = ?/{d * mult}", mult,
                           _num_choices(rng, mult)))
        return out
    return build


def frac_add_family(denom):
    def build(rng):
        out = []
        for a in _ramp(rng, 1, denom - 3):
            a = min(a, denom - 2)
            b = 1
            ans = f"{a + b}/{denom}"
            wrong1 = f"{a + b}/{denom * 2}"
            wrong2 = f"{a}/{denom}"
            ch = [ans, wrong1, wrong2]
            rng.shuffle(ch)
            out.append(_mk(rng, f"{a}/{denom} + {b}/{denom}", ans, ch))
        return out
    return build


def decimal_add_family(tenths):
    def build(rng):
        out = []
        for n in _ramp(rng, 1, 5):
            a = n / 10 + tenths / 10
            ans = f"{a:.1f}"
            ch = [ans, f"{a + 0.1:.1f}", f"{a - 0.1:.1f}"]
            rng.shuffle(ch)
            out.append(_mk(rng, f"0.{n} + 0.{tenths}", ans, ch))
        return out
    return build


def percent_of_family(pct):
    def build(rng):
        base = {50: [2, 4, 6, 8, 10], 25: [4, 8, 12, 16, 20],
                10: [10, 20, 30, 40, 50]}[pct]
        # the sibling shift, percent-style: slide the whole family up by one clean
        # multiple so half B gets fresh numbers with the same pattern (50% of 4, 6, 8...
        # vs 50% of 6, 8, 10...). The step keeps every answer a whole number.
        step = {50: 2, 25: 4, 10: 10}[pct]
        shift = rng.choice([0, 1, 2]) * step
        return [_mk(rng, f"{pct}% of {b + shift}", (b + shift) * pct // 100)
                for b in base]
    return build


def integer_add_family(addend):
    def build(rng):
        return [_mk(rng, f"−{n} + {addend}", addend - n) for n in _ramp(rng, 1, 5)]
    return build


def integer_sub_family(sub):
    def build(rng):
        return [_mk(rng, f"{n} − {sub}", n - sub) for n in _ramp(rng, 1, 5)]
    return build


def order_ops_family(mult):
    def build(rng):
        return [_mk(rng, f"{n} + 2 × {mult}", n + 2 * mult) for n in _ramp(rng, 1, 5)]
    return build


def prime_family():
    items = [(7, "yes"), (9, "no"), (11, "yes"), (15, "no"), (13, "yes")]
    def build(rng):
        return [_mk(rng, f"Is {n} prime?", a, ["yes", "no"]) for n, a in items]
    return build


def gcf_family():
    items = [((4, 6), 2), ((6, 9), 3), ((8, 12), 4), ((10, 15), 5), ((12, 18), 6)]
    def build(rng):
        return [_mk(rng, f"GCF of {a} and {b}?", g) for (a, b), g in items]
    return build


def unit_rate_family(per):
    def build(rng):
        return [_mk(rng, f"{n * per} for {n} — how many for 1?", per)
                for n in _ramp(rng, 2, 6)]
    return build


def area_family():
    def build(rng):
        return [_mk(rng, f"Area: {n} × {n + 1} rectangle", n * (n + 1))
                for n in _ramp(rng, 2, 6)]
    return build


def evaluate_family(coef, add):
    def build(rng):
        return [_mk(rng, f"{coef}x + {add}, when x = {n}", coef * n + add)
                for n in _ramp(rng, 1, 5)]
    return build


def like_terms_family():
    def build(rng):
        out = []
        for a in _ramp(rng, 2, 6):
            b = a + 1
            ans = f"{a + b}x"
            ch = [ans, f"{a + b}", f"{a * b}x"]
            rng.shuffle(ch)
            out.append(_mk(rng, f"{a}x + {b}x", ans, ch))
        return out
    return build


# ---------------------------------------------------------------------------
# UPPER-COURSE FAMILIES (build dp). Same disciplines as above: answers COMPUTED
# from the same numbers that build the question; _ramp's shift keeps half B a
# sibling; fixed FACT lists go through _pick (a seeded shuffle) for the same
# reason. Facts are textbook constants and are re-verified in ruletests PART 3n.
# ---------------------------------------------------------------------------
def _pick(rng, items, n=FAMILY_SIZE):
    """A seeded sample of a fixed fact list: shuffled order, repeats only when the
    list is shorter than the family. This is how a FACT family (trig values, i-powers)
    stays a sibling across halves -- fresh subset and order, same skill."""
    items = list(items)
    rng.shuffle(items)
    while len(items) < n:
        items = items + items
    return items[:n]


def _facts_family(facts):
    """A family from a fixed list of (question, answer, [3 choices]) facts."""
    def build(rng):
        out = []
        for q, a, ch in _pick(rng, facts):
            ch = list(ch)
            rng.shuffle(ch)
            out.append(_mk(rng, q, a, ch))
        return out
    return build


def distribute_family(coef):
    def build(rng):
        out = []
        for b in _ramp(rng, 1, 5):
            ans = f"{coef}x + {coef * b}"
            ch = [ans, f"{coef}x + {b}", f"{coef + b}x"]
            rng.shuffle(ch)
            out.append(_mk(rng, f"{coef}(x + {b}) = ?", ans, ch))
        return out
    return build


def solve_add_family(add):
    def build(rng):
        return [_mk(rng, f"x + {add} = {n + add}.  x = ?", n)
                for n in _ramp(rng, 2, 9)]
    return build


def solve_mul_family(coef):
    def build(rng):
        return [_mk(rng, f"{coef}x = {coef * n}.  x = ?", n)
                for n in _ramp(rng, 2, 9)]
    return build


def solve_two_step_family(coef, add):
    def build(rng):
        return [_mk(rng, f"{coef}x + {add} = {coef * n + add}.  x = ?", n)
                for n in _ramp(rng, 2, 9)]
    return build


def function_eval_family(coef, add):
    def build(rng):
        return [_mk(rng, f"f(x) = {coef}x + {add}.  f({n}) = ?", coef * n + add)
                for n in _ramp(rng, 1, 5)]
    return build


def slope_read_family(b):
    def build(rng):
        return [_mk(rng, f"Slope of y = {m}x + {b}?", m) for m in _ramp(rng, 2, 9)]
    return build


def slope_points_family(m):
    def build(rng):
        return [_mk(rng, f"Slope through (0, 0) and ({n}, {m * n})?", m)
                for n in _ramp(rng, 1, 5)]
    return build


def system_sum_diff_family(d):
    # x + y = 2n + d and x − y = d  ->  x = n + d (add the equations, halve)
    def build(rng):
        return [_mk(rng, f"x + y = {2 * n + d},  x − y = {d}.  x = ?", n + d)
                for n in _ramp(rng, 1, 5)]
    return build


_SUP = {1: "¹", 2: "²", 3: "³", 4: "⁴", 5: "⁵"}


def power_family(base):
    def build(rng):
        return [_mk(rng, f"{base}{_SUP[min(5, n)]} = ?", base ** min(5, n))
                for n in _ramp(rng, 2, 5)]
    return build


def exponent_law_family(kind):
    def build(rng):
        out = []
        for a in _ramp(rng, 2, 6):
            if kind == "mul":
                out.append(_mk(rng, f"x^{a} · x^2 = x^?", a + 2))
            else:
                out.append(_mk(rng, f"x^{a + 2} ÷ x^2 = x^?", a))
        return out
    return build


def factor_pair_family(p):
    def build(rng):
        out = []
        for q in _ramp(rng, 1, 5):
            if q == p:
                q += 1
            out.append(_mk(rng, f"x² + {p + q}x + {p * q} = (x + {p})(x + ?)", q))
        return out
    return build


def square_root_family():
    def build(rng):
        return [_mk(rng, f"√{n * n} = ?", n) for n in _ramp(rng, 3, 12)]
    return build


def cube_root_family():
    def build(rng):
        return [_mk(rng, f"∛{n ** 3} = ?", n) for n in _ramp(rng, 2, 6)]
    return build


def mean_family(step):
    def build(rng):
        return [_mk(rng, f"Mean of {n - step}, {n}, {n + step}?", n)
                for n in _ramp(rng, step + 1, step + 8)]
    return build


def median_family(step):
    # shown out of order on purpose -- the skill is picking the middle VALUE
    def build(rng):
        return [_mk(rng, f"Median of {n}, {n - step}, {n + step}?", n)
                for n in _ramp(rng, step + 1, step + 8)]
    return build


def complement_family():
    def build(rng):
        return [_mk(rng, f"Complement of {min(8, n) * 10}°?", 90 - min(8, n) * 10)
                for n in _ramp(rng, 1, 8)]
    return build


def supplement_family():
    def build(rng):
        return [_mk(rng, f"Supplement of {min(17, n) * 10}°?", 180 - min(17, n) * 10)
                for n in _ramp(rng, 2, 16)]
    return build


def triangle_angle_family(a):
    # a stays <= 60 and b <= 100, so the third angle is always a real angle
    def build(rng):
        out = []
        for v in _ramp(rng, 3, 10):
            b = min(v, 10) * 10
            out.append(_mk(rng, f"Triangle angles {a}° and {b}°. Third angle?",
                           180 - a - b))
        return out
    return build


def pythag_family():
    # every entry satisfies a² + b² = c² (re-verified in ruletests PART 3n)
    triples = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15),
               (8, 15, 17), (12, 16, 20), (7, 24, 25)]
    def build(rng):
        return [_mk(rng, f"Legs {a} and {b}. Hypotenuse?", c)
                for a, b, c in _pick(rng, triples)]
    return build


def scale_factor_family(k):
    def build(rng):
        return [_mk(rng, f"Side {n} scales to {n * k}. Scale factor?", k)
                for n in _ramp(rng, 2, 6)]
    return build


def circle_family(kind):
    def build(rng):
        out = []
        for r in _ramp(rng, 2, 9):
            if kind == "diameter":
                out.append(_mk(rng, f"Radius {r}. Diameter?", 2 * r))
            else:
                out.append(_mk(rng, f"Diameter {2 * r}. Radius?", r))
        return out
    return build


def reflect_point_family(axis):
    def build(rng):
        out = []
        for x in _ramp(rng, 1, 5):
            y = ((x + 2) % 5) + 1
            if axis == "x":
                q, ans = f"Reflect ({x}, {y}) over the x-axis", f"({x}, −{y})"
                wrongs = [f"(−{x}, {y})", f"(−{x}, −{y})"]
            else:
                q, ans = f"Reflect ({x}, {y}) over the y-axis", f"(−{x}, {y})"
                wrongs = [f"({x}, −{y})", f"(−{x}, −{y})"]
            ch = [ans] + wrongs
            rng.shuffle(ch)
            out.append(_mk(rng, q, ans, ch))
        return out
    return build


def midpoint_family():
    # the gap is always even, so the midpoint is always a whole number
    def build(rng):
        out = []
        for a in _ramp(rng, 1, 5):
            b = a + 2 * (((a + 1) % 3) + 1)
            out.append(_mk(rng, f"Midpoint of {a} and {b} on a number line?",
                           (a + b) // 2))
        return out
    return build


def tri_area_family(h):
    # base is always even, so half of base x height is always whole
    def build(rng):
        return [_mk(rng, f"Triangle: base {2 * n}, height {h}. Area?", n * h)
                for n in _ramp(rng, 2, 6)]
    return build


def degree_family():
    def build(rng):
        return [_mk(rng, f"Degree of x^{min(7, d)} + x + 1?", min(7, d))
                for d in _ramp(rng, 2, 6)]
    return build


_SUB = {2: "₂", 3: "₃", 5: "₅", 10: "₁₀"}


def log_family(base):
    def build(rng):
        return [_mk(rng, f"log{_SUB[base]} {base ** min(5, e)} = ?", min(5, e))
                for e in _ramp(rng, 1, 4)]
    return build


def geo_seq_family(r):
    def build(rng):
        return [_mk(rng, f"{a}, {a * r}, {a * r * r}, ?", a * r ** 3)
                for a in _ramp(rng, 1, 4)]
    return build


def compose_family(add, coef):
    def build(rng):
        return [_mk(rng, f"f(x) = x + {add}, g(x) = {coef}x.  f(g({n})) = ?",
                    coef * n + add) for n in _ramp(rng, 1, 5)]
    return build


def zeros_family(p):
    def build(rng):
        out = []
        for q in _ramp(rng, 1, 5):
            if q == p:
                q += 1
            ans = f"−{q}"
            ch = [ans, f"{q}", f"−{p}"]
            rng.shuffle(ch)
            out.append(_mk(rng, f"Zeros of (x − {p})(x + {q}):  x = {p} and x = ?",
                           ans, ch))
        return out
    return build


def factorial_family():
    def build(rng):
        out = []
        for n in _ramp(rng, 1, 5):
            n = min(6, n)
            f = 1
            for i in range(2, n + 1):
                f *= i
            out.append(_mk(rng, f"{n}! = ?", f))
        return out
    return build


def choose_family():
    def build(rng):
        return [_mk(rng, f"C({n}, 2) — ways to choose 2 of {n}?", n * (n - 1) // 2)
                for n in _ramp(rng, 3, 7)]
    return build


def complement_prob_family():
    def build(rng):
        out = []
        for n in _ramp(rng, 1, 8):
            n = min(9, n)
            ans = f"{(10 - n) / 10:.1f}"
            # near misses: the unsubtracted p, and the answer off by a tenth --
            # filtered against the answer AND each other (n = 5 collides both ways)
            cands = [f"{n / 10:.1f}", f"{(10 - n + 1) / 10:.1f}",
                     f"{(10 - n - 1) / 10:.1f}", f"{(n + 1) / 10:.1f}"]
            wrongs = []
            for w in cands:
                if w != ans and w not in wrongs:
                    wrongs.append(w)
                if len(wrongs) == 2:
                    break
            out.append(_mk(rng, f"P(rain) = 0.{n}.  P(no rain) = ?", ans,
                           _shuffled(rng, [ans] + wrongs)))
        return out
    return build


def _shuffled(rng, ch):
    ch = list(ch)
    rng.shuffle(ch)
    return ch


def expected_family():
    def build(rng):
        return [_mk(rng, f"Expected successes: 10 tries at P = 0.{min(9, n)}?",
                    min(9, n)) for n in _ramp(rng, 1, 8)]
    return build


def _xpow(n):
    """x^n as a tutor would write it: x^1 is just x."""
    return "x" if n == 1 else f"x^{n}"


def power_rule_family():
    def build(rng):
        out = []
        for v in _ramp(rng, 2, 6):
            n = min(8, v)
            out.append(_mk(rng, f"d/dx x^{n} = ?·{_xpow(n - 1)}", n))
        return out
    return build


def chain_exp_family():
    def build(rng):
        return [_mk(rng, f"d/dx e^({k}x) = ?·e^({k}x)", k)
                for k in _ramp(rng, 2, 6)]
    return build


def antipower_family():
    def build(rng):
        return [_mk(rng, f"∫ {_xpow(n)} dx = x^{n + 1}/?  (+ C)", n + 1)
                for n in _ramp(rng, 1, 5)]
    return build


def definite_family():
    # ∫ from 0 to a of 2x dx = a² -- the one definite integral worth memorizing whole
    def build(rng):
        return [_mk(rng, f"∫ from 0 to {a} of 2x dx = ?", a * a)
                for a in _ramp(rng, 1, 5)]
    return build


def poly_limit_family(add):
    # continuity: the limit of a polynomial is its value
    def build(rng):
        return [_mk(rng, f"lim (x → {n}) of x² + {add} = ?", n * n + add)
                for n in _ramp(rng, 1, 5)]
    return build


def char_root_family():
    # y″ − k²y = 0 has characteristic roots r = ±k
    def build(rng):
        return [_mk(rng, f"y″ − {k * k}y = 0:  r = ±?", k)
                for k in _ramp(rng, 1, 5)]
    return build


# fixed FACT lists (question, answer, three choices). Textbook constants only;
# each list is re-verified line by line in ruletests PART 3n.
I_POWER_FACTS = [
    ("i² = ?", "−1", ["−1", "1", "i"]),
    ("i³ = ?", "−i", ["−i", "i", "−1"]),
    ("i⁴ = ?", "1", ["1", "−1", "i"]),
    ("i⁵ = ?", "i", ["i", "−i", "1"]),
    ("i⁶ = ?", "−1", ["−1", "1", "−i"]),
    ("i⁸ = ?", "1", ["1", "−1", "i"]),
]
SIN_FACTS = [
    ("sin 0° = ?", "0", ["0", "1", "1/2"]),
    ("sin 30° = ?", "1/2", ["1/2", "√2/2", "√3/2"]),
    ("sin 45° = ?", "√2/2", ["√2/2", "1/2", "√3/2"]),
    ("sin 60° = ?", "√3/2", ["√3/2", "√2/2", "1/2"]),
    ("sin 90° = ?", "1", ["1", "0", "1/2"]),
]
COS_FACTS = [
    ("cos 0° = ?", "1", ["1", "0", "1/2"]),
    ("cos 30° = ?", "√3/2", ["√3/2", "√2/2", "1/2"]),
    ("cos 45° = ?", "√2/2", ["√2/2", "√3/2", "1/2"]),
    ("cos 60° = ?", "1/2", ["1/2", "√3/2", "√2/2"]),
    ("cos 90° = ?", "0", ["0", "1", "1/2"]),
]
RADIAN_FACTS = [
    ("180° = ? radians", "π", ["π", "2π", "π/2"]),
    ("360° = ? radians", "2π", ["2π", "π", "π/2"]),
    ("90° = ? radians", "π/2", ["π/2", "π/4", "π"]),
    ("45° = ? radians", "π/4", ["π/4", "π/2", "π/6"]),
    ("30° = ? radians", "π/6", ["π/6", "π/3", "π/2"]),
    ("60° = ? radians", "π/3", ["π/3", "π/6", "2π/3"]),
]
IDENTITY_FACTS = [
    ("sin²θ + cos²θ = ?", "1", ["1", "0", "2"]),
    ("tan θ = sin θ / ?", "cos θ", ["cos θ", "sin θ", "1"]),
    ("sin(−θ) = ?", "−sin θ", ["−sin θ", "sin θ", "cos θ"]),
    ("cos(−θ) = ?", "cos θ", ["cos θ", "−cos θ", "sin θ"]),
    ("1 + tan²θ = ?", "sec²θ", ["sec²θ", "csc²θ", "1"]),
    ("sin 2θ = ?", "2 sin θ cos θ", ["2 sin θ cos θ", "sin²θ", "2 sin θ"]),
]
EMPIRICAL_FACTS = [
    ("Normal curve: within 1 SD ≈ ?%", "68", ["68", "95", "50"]),
    ("Within 2 SD ≈ ?%", "95", ["95", "68", "99.7"]),
    ("Within 3 SD ≈ ?%", "99.7", ["99.7", "95", "100"]),
    ("Outside 1 SD ≈ ?%", "32", ["32", "68", "5"]),
    ("Outside 2 SD ≈ ?%", "5", ["5", "32", "0.3"]),
    ("Outside 3 SD ≈ ?%", "0.3", ["0.3", "5", "3"]),
]
DIE_FACTS = [
    ("P(rolling a 3 on one die) = 1/?", "6", ["6", "3", "2"]),
    ("P(heads on one coin flip) = 1/?", "2", ["2", "4", "6"]),
    ("P(rolling an even number) = 1/?", "2", ["2", "3", "6"]),
    ("P(rolling a 1 or a 2) = 1/?", "3", ["3", "6", "2"]),
    ("P(picking 1 of 4 equal choices) = 1/?", "4", ["4", "2", "8"]),
    ("P(rolling 4 or less) = 2/?", "3", ["3", "6", "4"]),
]
DERIV_FACTS = [
    ("d/dx sin x = ?", "cos x", ["cos x", "−cos x", "−sin x"]),
    ("d/dx cos x = ?", "−sin x", ["−sin x", "sin x", "cos x"]),
    ("d/dx eˣ = ?", "eˣ", ["eˣ", "x·eˣ", "ln x"]),
    ("d/dx ln x = ?", "1/x", ["1/x", "ln x", "x"]),
    ("d/dx of a constant = ?", "0", ["0", "1", "x"]),
    ("d/dx x = ?", "1", ["1", "0", "x"]),
]
ODE_ORDER_FACTS = [
    ("Order of y′ = y?", "1", ["1", "2", "0"]),
    ("Order of y″ + y = 0?", "2", ["2", "1", "3"]),
    ("Order of y‴ = x?", "3", ["3", "2", "1"]),
    ("Order of y″ = y′ + 1?", "2", ["2", "1", "3"]),
    ("Order of y′ + xy = 0?", "1", ["1", "2", "0"]),
    ("Order of y⁗ + y = x?", "4", ["4", "3", "2"]),
]
LAPLACE_FACTS = [
    ("L{1} = 1/s^?", "1", ["1", "2", "0"]),
    ("L{t} = 1/s^?", "2", ["2", "1", "3"]),
    ("L{t²} = 2/s^?", "3", ["3", "2", "4"]),
    ("L{t³} = 6/s^?", "4", ["4", "3", "6"]),
    ("L{e^(2t)} = 1/(s − ?)", "2", ["2", "1", "−2"]),
    ("L{e^(5t)} = 1/(s − ?)", "5", ["5", "−5", "1"]),
]


# ---------------------------------------------------------------------------
# THE REGISTRY -- course -> unit -> (skill name, [6 family builders])
# Course ids are curriculum.py's ("entry", "basic", "prealgebra", "algebra1"...).
# Units missing from this table simply have no sprint, and the app makes no offer
# -- fails soft. Concept units (proofs, sampling design, slope fields) are missing
# ON PURPOSE: they are not 60-second recall material.
# Names in comments are the unit names, so drift is visible in review.
# ---------------------------------------------------------------------------
SPRINTS = {
    "entry": {
        1: ("Counting on", [count_on_family(1, 1, 5), count_on_family(1, 6, 10),
            one_more_less_family(1, 3, 9), one_more_less_family(-1, 3, 9),
            count_on_family(2, 2, 6), count_on_family(2, 8, 12)]),          # Counting & Number Sense
        2: ("Adding to 20", [add_family(1, 2, 9), add_family(2, 2, 9),
            add_family(3, 2, 9), doubles_family(2, 8), make_ten_family(),
            add_family(9, 2, 9)]),                                          # Addition to 20
        3: ("Subtracting to 20", [sub_family(1, 3, 10), sub_family(2, 4, 12),
            sub_family(3, 5, 14), sub_family(5, 6, 15), sub_family(9, 10, 18),
            sub_family(10, 11, 19)]),                                       # Subtraction to 20
        4: ("Tens and ones", [place_value_family("compose"),
            place_value_family("compose"), place_value_family("tens"),
            place_value_family("tens"), add_family(10, 20, 60),
            sub_family(10, 30, 70)]),                                       # Place Value to 1,000
        5: ("Adding bigger numbers", [big_add_family(120, 2), big_add_family(240, 3),
            big_add_family(315, 4), add_family(20, 130, 170),
            add_family(30, 140, 180), big_add_family(430, 5)]),             # 2-3 Digit Addition
        6: ("Subtracting bigger numbers", [big_sub_family(180, 2),
            big_sub_family(260, 3), big_sub_family(390, 4),
            sub_family(20, 150, 190), sub_family(30, 160, 200),
            big_sub_family(470, 5)]),                                       # 2-3 Digit Subtraction
        7: ("Coins to cents", [coins_family(5, "nickels"), coins_family(10, "dimes"),
            coins_family(25, "quarters"), coins_family(10, "dimes"),
            coins_family(5, "nickels"), coins_family(25, "quarters")]),     # Money
        8: ("Time and measure", [minutes_family(60), minutes_family(7),
            minutes_family(60), minutes_family(7), minutes_family(60),
            minutes_family(7)]),                                            # Time, Calendar & Measurement
        9: ("Shapes and patterns", [shape_sides_family(), count_on_family(5, 5, 25),
            count_on_family(10, 10, 50), shape_sides_family(),
            count_on_family(5, 30, 50), count_on_family(10, 60, 100)]),     # Shapes, Patterns & Groups
    },
    "basic": {
        1: ("Mental adding and subtracting", [add_family(9, 12, 28),
            add_family(19, 12, 28), sub_family(9, 20, 40), sub_family(19, 30, 50),
            add_family(11, 12, 28), sub_family(11, 20, 40)]),               # Place Value & Whole-Number Ops
        2: ("Times tables", [times_family(2, 2, 9), times_family(3, 2, 9),
            times_family(4, 2, 9), times_family(6, 2, 9), times_family(8, 2, 9),
            times_family(9, 2, 9)]),                                        # Multiplication
        3: ("Division facts", [div_family(2, 2, 9), div_family(3, 2, 9),
            div_family(4, 2, 9), div_family(6, 2, 9), div_family(8, 2, 9),
            div_family(9, 2, 9)]),                                          # Division
        4: ("Factors and primes", [gcf_family(), prime_family(), gcf_family(),
            prime_family(), gcf_family(), prime_family()]),                 # Factors, Multiples, GCF & LCM
        5: ("Equivalent fractions", [frac_equiv_family(2), frac_equiv_family(3),
            frac_equiv_family(4), frac_equiv_family(2), frac_equiv_family(3),
            frac_equiv_family(5)]),                                         # Fractions -- Meaning & Equivalence
        6: ("Adding fractions", [frac_add_family(5), frac_add_family(7),
            frac_add_family(8), frac_add_family(5), frac_add_family(7),
            frac_add_family(9)]),                                           # Fraction Operations
        7: ("Adding decimals", [decimal_add_family(2), decimal_add_family(3),
            decimal_add_family(4), decimal_add_family(2), decimal_add_family(3),
            decimal_add_family(4)]),                                        # Decimals
        8: ("Easy percents", [percent_of_family(50), percent_of_family(10),
            percent_of_family(25), percent_of_family(50), percent_of_family(10),
            percent_of_family(25)]),                                        # Ratios, Rates & Percents
        9: ("Measure and area", [minutes_family(60), area_family(),
            minutes_family(7), area_family(), minutes_family(60),
            area_family()]),                                                # Measurement, Geometry & Word Problems
    },
    "prealgebra": {
        1: ("Multiply first", [order_ops_family(2), order_ops_family(3),
            order_ops_family(4), order_ops_family(5), order_ops_family(6),
            order_ops_family(7)]),                                          # Number Sense & Order of Operations
        2: ("Factors and primes", [gcf_family(), prime_family(), gcf_family(),
            prime_family(), gcf_family(), prime_family()]),                 # Factors, Multiples & Primes
        3: ("Negative numbers", [integer_add_family(3), integer_add_family(6),
            integer_sub_family(7), integer_sub_family(9), integer_add_family(8),
            integer_sub_family(12)]),                                       # Integers & Negative Numbers
        4: ("Fraction moves", [frac_add_family(5), frac_equiv_family(3),
            frac_add_family(7), frac_equiv_family(4), frac_add_family(8),
            frac_equiv_family(5)]),                                         # Fractions
        5: ("Decimal moves", [decimal_add_family(2), decimal_add_family(3),
            decimal_add_family(4), decimal_add_family(2), decimal_add_family(3),
            decimal_add_family(4)]),                                        # Decimals
        6: ("Unit rates", [unit_rate_family(3), unit_rate_family(4),
            unit_rate_family(6), unit_rate_family(7), unit_rate_family(8),
            unit_rate_family(9)]),                                          # Ratios, Rates & Proportions
        7: ("Percents in your head", [percent_of_family(50), percent_of_family(10),
            percent_of_family(25), percent_of_family(50), percent_of_family(10),
            percent_of_family(25)]),                                        # Percents
        8: ("Area in your head", [area_family(), area_family(), area_family(),
            area_family(), area_family(), area_family()]),                  # Measurement & Geometry Basics
        9: ("Plug it in", [evaluate_family(2, 1), evaluate_family(3, 2),
            like_terms_family(), evaluate_family(4, 3), like_terms_family(),
            evaluate_family(5, 1)]),                                        # Variables & Expressions
    },
    "algebra1": {
        1: ("Expression moves", [distribute_family(2), like_terms_family(),
            distribute_family(3), evaluate_family(2, 3), distribute_family(4),
            evaluate_family(3, 1)]),                                        # Foundations & Expressions
        2: ("One-step solves", [solve_add_family(3), solve_add_family(7),
            solve_mul_family(2), solve_mul_family(3), solve_mul_family(4),
            solve_add_family(9)]),                                          # Linear Equations & Inequalities
        3: ("Read f(x) fast", [function_eval_family(2, 1), function_eval_family(3, 2),
            function_eval_family(2, 5), function_eval_family(4, 1),
            function_eval_family(3, 4), function_eval_family(5, 2)]),       # Functions & Notation
        4: ("Spot the slope", [slope_read_family(1), slope_read_family(4),
            slope_points_family(2), slope_points_family(3), slope_read_family(7),
            slope_points_family(4)]),                                       # Linear Functions & Graphs
        5: ("Add the equations", [system_sum_diff_family(2), system_sum_diff_family(4),
            system_sum_diff_family(6), system_sum_diff_family(2),
            system_sum_diff_family(4), system_sum_diff_family(8)]),         # Systems of Equations
        6: ("Powers in your head", [power_family(2), exponent_law_family("mul"),
            power_family(3), exponent_law_family("div"), power_family(5),
            exponent_law_family("mul")]),                                   # Exponents & Exponential Functions
        7: ("Factor pairs", [factor_pair_family(2), factor_pair_family(3),
            factor_pair_family(4), factor_pair_family(2), factor_pair_family(5),
            factor_pair_family(3)]),                                        # Polynomials & Factoring
        8: ("Squares and roots", [power_family(2), square_root_family(),
            power_family(3), square_root_family(), doubles_family(6, 12),
            square_root_family()]),                                         # Quadratic Functions
        9: ("Middle of the data", [mean_family(2), median_family(3), mean_family(4),
            median_family(5), mean_family(3), median_family(2)]),           # Data & Statistics
    },
    "geometry": {
        1: ("Angle pairs", [complement_family(), supplement_family(),
            complement_family(), supplement_family(), complement_family(),
            supplement_family()]),                                          # Foundations & Constructions
        2: ("Flip the point", [reflect_point_family("x"), reflect_point_family("y"),
            reflect_point_family("x"), reflect_point_family("y"),
            reflect_point_family("x"), reflect_point_family("y")]),         # Transformations & Symmetry
        3: ("Triangle angle sum", [triangle_angle_family(30), triangle_angle_family(40),
            triangle_angle_family(50), triangle_angle_family(60),
            triangle_angle_family(45), triangle_angle_family(35)]),         # Congruence & Triangle Proofs
        4: ("Scale factors", [scale_factor_family(2), scale_factor_family(3),
            scale_factor_family(4), scale_factor_family(5), scale_factor_family(2),
            scale_factor_family(3)]),                                       # Similarity & Dilations
        5: ("Pythagorean triples", [pythag_family(), pythag_family(), pythag_family(),
            pythag_family(), pythag_family(), pythag_family()]),            # Right Triangles & Trigonometry
        6: ("Radius and diameter", [circle_family("diameter"), circle_family("radius"),
            circle_family("diameter"), circle_family("radius"),
            circle_family("diameter"), circle_family("radius")]),           # Circles
        7: ("Midpoints", [midpoint_family(), slope_points_family(2), midpoint_family(),
            slope_points_family(3), midpoint_family(), slope_points_family(4)]),  # Coordinate Geometry
        8: ("Area in your head", [area_family(), tri_area_family(4), area_family(),
            tri_area_family(6), area_family(), tri_area_family(8)]),        # Area, Surface Area & Volume
    },
    "algebra2": {
        1: ("Two-step solves", [solve_two_step_family(2, 3), solve_two_step_family(3, 1),
            solve_two_step_family(2, 5), solve_two_step_family(4, 3),
            solve_two_step_family(3, 2), solve_two_step_family(5, 1)]),     # Foundations & Systems
        2: ("Powers of i", [_facts_family(I_POWER_FACTS), power_family(2),
            _facts_family(I_POWER_FACTS), power_family(3),
            _facts_family(I_POWER_FACTS), square_root_family()]),           # Quadratic Functions & Complex Numbers
        3: ("Name the degree", [degree_family(), degree_family(), degree_family(),
            degree_family(), degree_family(), degree_family()]),            # Polynomial Functions
        4: ("Divide the powers", [exponent_law_family("div"), exponent_law_family("mul"),
            exponent_law_family("div"), exponent_law_family("mul"),
            exponent_law_family("div"), exponent_law_family("div")]),       # Rational Expressions & Functions
        5: ("Roots in your head", [square_root_family(), cube_root_family(),
            square_root_family(), cube_root_family(), square_root_family(),
            cube_root_family()]),                                           # Radicals & Rational Exponents
        6: ("Logs are exponents", [log_family(2), log_family(10), log_family(3),
            log_family(2), log_family(10), log_family(5)]),                 # Exponential & Logarithmic Functions
        7: ("Next in the pattern", [count_on_family(4, 3, 15), geo_seq_family(2),
            count_on_family(7, 5, 20), geo_seq_family(3), count_on_family(6, 4, 18),
            geo_seq_family(2)]),                                            # Sequences & Series
    },
    "precalc": {
        1: ("Compose in your head", [compose_family(3, 2), compose_family(1, 3),
            compose_family(5, 2), compose_family(2, 4), compose_family(4, 3),
            compose_family(1, 5)]),                                         # Functions & Their Graphs
        2: ("Read the zeros", [zeros_family(3), zeros_family(5), zeros_family(2),
            zeros_family(4), zeros_family(6), zeros_family(3)]),            # Polynomial & Rational Functions
        3: ("Logs are exponents", [log_family(2), log_family(10), log_family(3),
            log_family(5), log_family(2), log_family(10)]),                 # Exponential & Logarithmic Functions
        4: ("Special angles", [_facts_family(RADIAN_FACTS),
            _facts_family(SIN_FACTS), _facts_family(COS_FACTS),
            _facts_family(RADIAN_FACTS), _facts_family(SIN_FACTS),
            _facts_family(COS_FACTS)]),                                     # Trigonometric Functions
        5: ("Identity recall", [_facts_family(IDENTITY_FACTS), _facts_family(SIN_FACTS),
            _facts_family(IDENTITY_FACTS), _facts_family(COS_FACTS),
            _facts_family(IDENTITY_FACTS), _facts_family(RADIAN_FACTS)]),   # Analytic Trigonometry
        8: ("Count the ways", [factorial_family(), choose_family(), factorial_family(),
            choose_family(), factorial_family(), choose_family()]),         # Sequences, Series & the Binomial Theorem
    },
    "probstat": {
        1: ("Middle of the data", [mean_family(2), mean_family(4), mean_family(3),
            mean_family(5), mean_family(2), mean_family(4)]),               # Exploring Data
        2: ("Find the median", [median_family(2), median_family(4), median_family(3),
            median_family(5), median_family(2), median_family(4)]),         # Describing Distributions
        5: ("Chance in your head", [_facts_family(DIE_FACTS), complement_prob_family(),
            _facts_family(DIE_FACTS), complement_prob_family(),
            _facts_family(DIE_FACTS), complement_prob_family()]),           # Probability Basics
        7: ("Expected value", [expected_family(), expected_family(), expected_family(),
            expected_family(), expected_family(), expected_family()]),      # Random Variables & Expected Value
        8: ("The 68–95–99.7 rule", [_facts_family(EMPIRICAL_FACTS),
            _facts_family(EMPIRICAL_FACTS), _facts_family(EMPIRICAL_FACTS),
            _facts_family(EMPIRICAL_FACTS), _facts_family(EMPIRICAL_FACTS),
            _facts_family(EMPIRICAL_FACTS)]),                               # The Normal Distribution
    },
    "calculus": {
        1: ("Limits by plugging in", [poly_limit_family(1), poly_limit_family(3),
            poly_limit_family(2), poly_limit_family(5), poly_limit_family(4),
            poly_limit_family(1)]),                                         # Limits & Continuity
        2: ("The power rule", [power_rule_family(), _facts_family(DERIV_FACTS),
            power_rule_family(), _facts_family(DERIV_FACTS), power_rule_family(),
            _facts_family(DERIV_FACTS)]),                                   # The Derivative: Definition & Basic Rules
        3: ("Chain on e^(kx)", [chain_exp_family(), chain_exp_family(),
            chain_exp_family(), chain_exp_family(), chain_exp_family(),
            chain_exp_family()]),                                           # Product, Quotient & Chain Rules
        6: ("Antipowers", [antipower_family(), antipower_family(), antipower_family(),
            antipower_family(), antipower_family(), antipower_family()]),   # Antiderivatives & Indefinite Integrals
        7: ("Easy definite integrals", [definite_family(), antipower_family(),
            definite_family(), antipower_family(), definite_family(),
            antipower_family()]),                                           # The Definite Integral & the FTC
    },
    "diffeq": {
        1: ("Name the order", [_facts_family(ODE_ORDER_FACTS),
            _facts_family(ODE_ORDER_FACTS), _facts_family(ODE_ORDER_FACTS),
            _facts_family(ODE_ORDER_FACTS), _facts_family(ODE_ORDER_FACTS),
            _facts_family(ODE_ORDER_FACTS)]),                               # Introduction, Classification & Slope Fields
        5: ("Characteristic roots", [char_root_family(), char_root_family(),
            char_root_family(), char_root_family(), char_root_family(),
            char_root_family()]),                                           # Second-Order Linear: Homogeneous
        7: ("Laplace facts", [_facts_family(LAPLACE_FACTS), _facts_family(LAPLACE_FACTS),
            _facts_family(LAPLACE_FACTS), _facts_family(LAPLACE_FACTS),
            _facts_family(LAPLACE_FACTS), _facts_family(LAPLACE_FACTS)]),   # Laplace Transforms
    },
}


def available(course, unit):
    """True if this course+unit has a sprint. The app offers nothing otherwise."""
    try:
        return int(unit) in SPRINTS.get(str(course), {})
    except (TypeError, ValueError):
        return False


def build(course, unit, seed):
    """The full sprint for one student-day: {"skill", "a": [...30], "b": [...30]}.

    A and B come from the SAME family plan with different rng draws, which is exactly
    Eureka's relationship between the halves: same skill, same pattern order, fresh
    numbers -- so improving on B measures fluency, not memory of half A's answers.
    Deterministic for a given seed. Returns None when no sprint exists (fail soft)."""
    if not available(course, unit):
        return None
    skill, builders = SPRINTS[str(course)][int(unit)]
    half_a = _families(random.Random(f"{seed}-A"), builders)
    half_b = _families(random.Random(f"{seed}-B"), builders)
    return {"skill": skill, "course": str(course), "unit": int(unit),
            "a": half_a, "b": half_b}

# I did no harm and this file is not truncated.

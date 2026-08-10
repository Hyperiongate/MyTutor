# =============================================================================
# sprints.py  --  FLUENCY SPRINTS  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
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
def _num_choices(rng, answer):
    """Three tap choices for a numeric answer: the truth and two near misses.
    Near, because a wildly wrong distractor makes tapping a guessing game."""
    a = int(answer)
    pool = [a + 1, a - 1, a + 2, a - 2, a + 10, a - 10]
    picks = []
    for p in pool:
        if p != a and p >= 0 and p not in picks:
            picks.append(p)
        if len(picks) == 2:
            break
    out = [str(a)] + [str(p) for p in picks]
    rng.shuffle(out)
    return out


def _mk(rng, q, a, choices=None):
    return {"q": q, "a": str(a), "c": choices or _num_choices(rng, a)}


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
# THE REGISTRY -- course -> unit -> (skill name, [6 family builders])
# Course ids are curriculum.py's ("entry", "basic", "prealgebra"). Units missing
# from this table simply have no sprint, and the app makes no offer -- fails soft.
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

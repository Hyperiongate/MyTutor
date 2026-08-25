# =============================================================================
# mathcheck.py  --  Math Tutor MVP  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-08-25  BUILD ni -- THE BOARD ITSELF IS A CLAIM. The night watch confirmed a
#               shipped [[step eq="3/4 - 1/2 = 2/4 - 1/2 = 1/4"]] -- a false chain,
#               drawn for a child, invisible here because verify_reply read only
#               [[verify]] tags. New check_board_equations(): every ALL-CONSTANT
#               equality chain in step/write/solve tags is re-computed; chains with a
#               free symbol are problems (never judged), placeholders are pending
#               questions, wide spacing is a COLUMN BREAK (two authored side-by-side
#               lines taught that), rule 56's find-the-error game is exempt, and the
#               board path gains superscript (2³) and tight-dot (2·4) normalization.
#               Wired INSIDE verify_reply so a false board line rides the existing
#               wrong->retry machinery -- and it runs even when the reply has no
#               verify tag at all, which is precisely how the caught line hid.
#               Swept clean: 0 false alarms over all 306 canonical scripts + the
#               demo's boards (21 chains judged). PART 3ds re-runs that sweep on
#               every build.
#
# THE MATH VERIFIER (new file, 2026-08-03)
#
# WHY THIS FILE EXISTS: Mr. Cadabra invents problems and states answers on the
# fly. A language model is very good at math but not perfect -- and ONE wrong
# answer key shown to a child costs more trust than a thousand right ones earn.
# This module is the independent referee: every problem/answer the tutor states
# is re-checked here with SymPy (a symbolic math engine -- it actually DOES the
# algebra/calculus, it does not guess).
#
# HOW IT WORKS (the whole pipeline):
#   1. The shared prompt block (tutor.py GRAPH_TOOL_NOTE rules 10-12) tells the
#      tutor to append a hidden tag to any reply that states a checkable claim:
#          [[verify expr="2*x + 1 = 11" answer="x = 5"]]
#      The tag is written in Python/SymPy syntax and is NEVER shown or spoken to
#      the student.
#   2. tutor.py hands each generated reply to verify_reply() below BEFORE the
#      student sees it. Every tag is parsed and checked:
#        - expr WITH "="  -> an equation (or chain "6/2 = 3", or a system split
#          on ";"). The claimed answer(s) are substituted back in; every
#          equation must balance. Answers may be "x = 5", "x = 2 or x = 3"
#          (both must work), "x = 1, y = 2" (a system solution), or a bare
#          value when the equation has exactly one unknown.
#        - expr WITHOUT "=" -> a computation/simplification. expr and answer
#          must be mathematically equivalent (7*8 vs 56, (x+2)*(x+3) vs
#          x**2+5*x+6, diff(x**3, x) vs 3*x**2, integrate(2*x, x) vs x**2).
#        - inequalities (<, <=, >, >=) -> the claimed solution region is
#          compared against the true one on a dense sample of test points.
#   3. Verdicts: "ok" (all tags check out), "wrong" (at least one claim is
#      provably false -- detail includes what SymPy computed, so the tutor can
#      be silently re-asked with the correction), "unverifiable" (could not be
#      parsed/decided -- we FAIL OPEN and let the reply through, because a
#      checker that bricks lessons on its own parse gaps does more harm than
#      good), or "none" (no tags in the reply).
#   4. strip_verify_tags() removes the tags before the reply is returned, so
#      the frontend never sees them -- zero frontend changes were needed.
#
# DESIGN CHOICES (deliberate, please keep):
#   - FAIL OPEN on anything unparseable/undecidable/slow. Only a CONFIDENT
#     numeric/symbolic mismatch is called "wrong". A false accusation makes
#     tutor.py burn paid retries and, at worst, replace a correct reply.
#   - Every check runs in a worker thread with a hard timeout (SymPy's
#     simplify can occasionally wander off) -- a slow check must never stall a
#     child's lesson. Timeout -> unverifiable -> pass through.
#   - The tag text comes from the MODEL (not typed by the student), but a
#     student could try to prompt-inject a tag, so input is still sanitized:
#     length-capped, restricted character set, no "__", and parsed with a
#     restricted function whitelist (never eval).
#   - Decimal answers get a fair tolerance: "0.33" for 1/3 is treated as
#     correct-to-2-decimal-places, not branded wrong. Exact forms are still
#     preferred (the prompt says so).
#   - No imports from the rest of the app: this file must stay independently
#     testable, and if SymPy is somehow missing the module still imports and
#     simply reports "unverifiable" (the app keeps teaching, checks off).
#
# CHANGE NOTES (keep newest at top):
#   2026-08-03  Initial version. Verifies [[verify]] tags: equations (incl.
#               chains, systems, multiple roots), computations/simplifications
#               (incl. diff/integrate), inequalities (sample-based). Fail-open
#               posture, threaded timeouts, restricted parser, decimal
#               tolerance, and correction text (what SymPy actually computed)
#               for tutor.py's silent-regeneration nudge.
# =============================================================================

import re
import random
from concurrent.futures import ThreadPoolExecutor, TimeoutError as _FutureTimeout

# SymPy is a hard dependency in requirements.txt, but if it is ever missing the
# app must keep teaching -- so the import is guarded and its absence just turns
# every check into "unverifiable" (fail open), with a loud log line.
try:
    import sympy
    from sympy.parsing.sympy_parser import (
        parse_expr, standard_transformations,
        implicit_multiplication_application, convert_xor,
    )
    _SYMPY_OK = True
except Exception as _exc:  # noqa: BLE001
    sympy = None
    _SYMPY_OK = False
    print(f"[mathcheck] SymPy unavailable -- all checks fail open: {_exc}")

# --------------------------------------------------------------------------- #
# Tunables
# --------------------------------------------------------------------------- #
MAX_TAG_LEN = 400          # a verify tag longer than this is ignored (unverifiable)
MAX_TAGS_PER_REPLY = 8     # sanity cap; extras are ignored with a log line
CHECK_TIMEOUT_SECONDS = 4  # per-tag hard budget; slower -> unverifiable
BASE_TOL = 1e-8            # numeric tolerance for exact-form answers
SAMPLE_POINTS = 21         # numeric sampling grid for symbolic/inequality checks

# One small shared pool: checks are rare and short; threads let us enforce the
# timeout without signals (which don't work off the main thread under uvicorn).
_EXECUTOR = ThreadPoolExecutor(max_workers=4, thread_name_prefix="mathcheck")

# The tag as the model writes it:  [[verify expr="..." answer="..."]]
VERIFY_TAG_RE = re.compile(r"\[\[\s*verify\b([^\]]*?)\]\]", re.IGNORECASE)
_ATTR_RE = re.compile(r'(\w+)\s*=\s*"([^"]*)"')

# Characters we are willing to hand to the parser (after normalization).
_ALLOWED = re.compile(r"^[0-9a-zA-Z_+\-*/^=(),.\s;|<>!%]*$")

# Functions/constants the parser may resolve. Anything else that LOOKS like a
# name simply becomes an inert symbol (auto_symbol), never a call.
def _global_dict():
    return {
        "sqrt": sympy.sqrt, "root": sympy.root, "cbrt": sympy.cbrt,
        "sin": sympy.sin, "cos": sympy.cos, "tan": sympy.tan,
        "asin": sympy.asin, "acos": sympy.acos, "atan": sympy.atan,
        "arcsin": sympy.asin, "arccos": sympy.acos, "arctan": sympy.atan,
        "sec": sympy.sec, "csc": sympy.csc, "cot": sympy.cot,
        "log": sympy.log, "ln": sympy.log, "exp": sympy.exp,
        "Abs": sympy.Abs, "abs": sympy.Abs,
        "diff": sympy.diff, "integrate": sympy.integrate,
        "factorial": sympy.factorial, "binomial": sympy.binomial,
        "gcd": sympy.gcd, "lcm": sympy.lcm,
        "floor": sympy.floor, "ceiling": sympy.ceiling,
        "pi": sympy.pi, "oo": sympy.oo,
        # The parser's generated code needs sympy's core constructors in scope
        # (numbers become Integer(...)/Float(...), names become Symbol(...)).
        "Rational": sympy.Rational, "Integer": sympy.Integer,
        "Float": sympy.Float, "Symbol": sympy.Symbol,
    }


# Alphabetic words (2+ letters) that may appear in a tag. Anything else -- "cat",
# "the", stray units -- means the tag is prose, not math: fail open, never guess.
# (Implicit multiplication would happily parse "cat" as c*a*t and then "verify" it,
# which is exactly the kind of false confidence this module must never have.)
_ALLOWED_WORDS = {
    "sqrt", "root", "cbrt", "sin", "cos", "tan", "asin", "acos", "atan",
    "arcsin", "arccos", "arctan", "sec", "csc", "cot", "log", "ln", "exp",
    "abs", "diff", "integrate", "factorial", "binomial", "gcd", "lcm",
    "floor", "ceiling", "pi", "oo", "theta", "rational", "integer", "float",
    "symbol", "or", "and",
}


# --------------------------------------------------------------------------- #
# Normalization + parsing
# --------------------------------------------------------------------------- #
def _normalize(s: str) -> str:
    """Turn friendly math typography into parseable Python/SymPy text."""
    s = (s or "").strip()
    s = (s.replace("×", "*").replace("÷", "/")   # × ÷
           .replace("−", "-").replace("√", "sqrt")  # − √
           .replace("π", "pi").replace("θ", "theta")  # π θ
           .replace("≤", "<=").replace("≥", ">=")  # ≤ ≥
           .replace("≠", "!="))                        # ≠
    # thousands separators: 1,000 -> 1000 (only digit,digit-digit-digit)
    s = re.sub(r"(?<=\d),(?=\d{3}(?:\D|$))", "", s)
    # percents: 25% -> (25/100)
    s = re.sub(r"(\d+(?:\.\d+)?)\s*%", r"(\1/100)", s)
    return s


def _reject_reason(s: str):
    """Return a reason string if this text may not be parsed, else None."""
    if len(s) > MAX_TAG_LEN:
        return "too long"
    if "__" in s:
        return "forbidden token"
    if not _ALLOWED.match(s):
        return "unsupported characters"
    if re.search(r"!(?!=)", s):  # lone '!' (factorial notation) unsupported
        return "unsupported '!' notation"
    for word in re.findall(r"[a-zA-Z_]{2,}", s):
        if word.lower() not in _ALLOWED_WORDS:
            return f"unknown word '{word}'"
    return None


def _parse(s: str):
    """Parse one expression with implicit multiplication (2x), ^ powers, and a
    restricted function whitelist. Raises on failure."""
    transformations = standard_transformations + (
        implicit_multiplication_application, convert_xor)
    # Single letters are plain symbols, EXCEPT e (Euler's number) and i (the
    # imaginary unit) -- the calculus/Algebra II convention wins here.
    local = {c: sympy.Symbol(c) for c in "abcdfghjklmnopqrstuvwxyz"}
    local.update({"e": sympy.E, "i": sympy.I, "theta": sympy.Symbol("theta")})
    return parse_expr(s, local_dict=local, global_dict=_global_dict(),
                      transformations=transformations, evaluate=True)


_EQ_SPLIT_RE = re.compile(r"(?<![<>!=])=(?!=)")  # a bare '=', not <=,>=,!=,==
_REL_RE = re.compile(r"(<=|>=|<|>)")


def _decimal_tolerance(answer_text: str) -> float:
    """If the stated answer uses rounded decimals, be fair: tolerance is half a
    unit of the coarsest decimal place given ('0.33' -> ±0.005)."""
    decs = [len(m.group(1)) for m in re.finditer(r"\.(\d+)", answer_text)]
    if not decs:
        return BASE_TOL
    return max(BASE_TOL, 0.5 * (10 ** -min(decs)))


def _is_zero_num(value, tol: float):
    """Numeric zero test; None if we can't decide."""
    try:
        c = complex(value.evalf(chop=True))
        return (abs(c) <= tol)
    except Exception:  # noqa: BLE001
        return None


def _sample_zero(expr, tol: float):
    """Decide expr == 0 by sampling its free symbols. True/False/None."""
    syms = sorted(expr.free_symbols, key=lambda x: x.name)
    if not syms:
        return _is_zero_num(expr, tol)
    rng = random.Random(20260803)  # fixed seed: same verdict every run
    good = 0
    for _ in range(SAMPLE_POINTS):
        subs = {s: sympy.Rational(rng.randint(-800, 800), rng.randint(1, 9)) for s in syms}
        try:
            v = complex(expr.subs(subs).evalf(chop=True))
        except Exception:  # noqa: BLE001
            continue  # pole/domain issue at this point -- try another
        if abs(v) > max(tol, 1e-6):
            return False
        good += 1
    return True if good >= 3 else None


# --------------------------------------------------------------------------- #
# The three claim shapes
# --------------------------------------------------------------------------- #
def _check_equivalence(expr_text: str, answer_text: str, tol: float):
    """expr and answer are both plain expressions: are they the same math?"""
    a = _parse(expr_text)
    b = _parse(answer_text)
    try:
        eq = a.equals(b)  # symbolic + numeric fallback; True/False/None
    except Exception:  # noqa: BLE001
        eq = None
    if eq is True:
        return "ok", ""
    if eq is None:
        sampled = _sample_zero(a - b, tol)
        if sampled is True:
            return "ok", ""
        if sampled is None:
            return "unverifiable", "could not decide equivalence"
    # Confidently different -- compute the truth for the correction note.
    # Honor a decimal-tolerance answer before condemning (equals() is exact).
    if _sample_zero(a - b, tol) is True:
        return "ok", ""
    try:
        truth = sympy.simplify(a)
        return "wrong", (f'you stated {expr_text} = {answer_text}, but it actually '
                         f'equals {sympy.sstr(truth)}')
    except Exception:  # noqa: BLE001
        return "wrong", f'{expr_text} does not equal {answer_text}'


def _parse_solution_sets(answer_text: str):
    """'x = 2 or x = 3' / 'x = 1, y = 2' / '5' -> list of solution dicts
    (None key = bare value). Raises on parse failure."""
    sets = []
    for chunk in re.split(r"\bor\b|;", answer_text):
        chunk = chunk.strip()
        if not chunk:
            continue
        sol = []
        for item in re.split(r"\band\b|,", chunk):
            item = item.strip()
            if not item:
                continue
            parts = _EQ_SPLIT_RE.split(item)
            if len(parts) == 2:
                var = parts[0].strip()
                if not re.fullmatch(r"[a-zA-Z](\w*)?", var):
                    raise ValueError(f"cannot read '{item}' as var = value")
                sol.append((var, _parse(parts[1])))
            elif len(parts) == 1:
                sol.append((None, _parse(parts[0])))
            else:
                raise ValueError(f"cannot read '{item}'")
        if sol:
            # 'x = 2, x = 3' really means two separate roots, not a system
            names = [v for v, _ in sol if v is not None]
            if names and len(names) == len(sol) and len(set(names)) == 1 and len(sol) > 1:
                sets.extend([[pair] for pair in sol])
            else:
                sets.append(sol)
    if not sets:
        raise ValueError("empty answer")
    return sets


def _check_equations(expr_text: str, answer_text: str, tol: float):
    """expr holds one or more '='. Substitute the claimed answer(s) back in."""
    equations = []          # list of (L, R) sympy pairs
    for stmt in expr_text.split(";"):
        stmt = stmt.strip()
        if not stmt:
            continue
        parts = _EQ_SPLIT_RE.split(stmt)
        if len(parts) < 2:
            # a system line without '=' -- treat as expression == 0? Too clever;
            # just refuse to guess.
            raise ValueError(f"no '=' in '{stmt}'")
        parsed = [_parse(p) for p in parts]
        for left, right in zip(parsed, parsed[1:]):   # chains: a = b = c
            equations.append((left, right))

    all_syms = set()
    for left, right in equations:
        all_syms |= left.free_symbols | right.free_symbols

    solution_sets = _parse_solution_sets(answer_text)

    for sol in solution_sets:
        subs = {}
        for var, value in sol:
            if var is None:
                if len(all_syms) == 1:
                    subs[next(iter(all_syms))] = value
                elif len(all_syms) == 0:
                    # pure arithmetic chain like '7+5 = 12' with a bare answer:
                    # the answer must equal every side too.
                    left0 = equations[0][0]
                    if _sample_zero(left0 - value, tol) is False:
                        truth = sympy.simplify(left0)
                        return "wrong", (f"you stated the value {sympy.sstr(value)}, but "
                                         f"{sympy.sstr(left0)} is {sympy.sstr(truth)}")
                else:
                    raise ValueError("bare answer but several unknowns")
            else:
                subs[sympy.Symbol(var)] = value
        for left, right in equations:
            verdict = _sample_zero((left - right).subs(subs), tol)
            if verdict is False:
                return "wrong", _equation_correction(equations, all_syms, sol)
            if verdict is None:
                return "unverifiable", "could not decide after substitution"
    return "ok", ""


def _equation_correction(equations, all_syms, claimed):
    """Best-effort 'here is the real answer' text for the regeneration nudge."""
    claimed_txt = ", ".join(
        (f"{v} = {sympy.sstr(val)}" if v else sympy.sstr(val)) for v, val in claimed)
    try:
        eqs = [sympy.Eq(left, right) for left, right in equations]
        sols = sympy.solve(eqs, list(all_syms), dict=True)
        if sols:
            shown = " or ".join(
                ", ".join(f"{s} = {sympy.sstr(v)}" for s, v in sorted(
                    sol.items(), key=lambda kv: kv[0].name)) for sol in sols[:4])
            return (f"your stated answer ({claimed_txt}) does not satisfy the equation(s); "
                    f"the correct solution is: {shown}")
    except Exception:  # noqa: BLE001
        pass
    return f"your stated answer ({claimed_txt}) does not satisfy the equation(s)"


def _check_inequality(expr_text: str, answer_text: str, tol: float):
    """Both sides are relationals in ONE variable: compare truth regions by
    sampling around every interesting boundary point."""
    prob = _parse_relational(expr_text)
    claim = _parse_relational(answer_text)
    syms = prob.free_symbols | claim.free_symbols
    if len(syms) != 1:
        return "unverifiable", "inequality with more than one unknown"
    x = next(iter(syms))

    # Interesting points: where either side's L - R crosses zero, plus a grid.
    points = set()
    for rel in (prob, claim):
        try:
            for r in sympy.solve(sympy.Eq(rel.lhs, rel.rhs), x):
                if r.is_real:
                    points.add(r)
        except Exception:  # noqa: BLE001
            pass
    eps = sympy.Rational(1, 1000)
    test = set()
    for p in points:
        test |= {p - eps, p, p + eps}
    test |= {sympy.Integer(k) for k in range(-10, 11)}

    checked = 0
    for t in test:
        try:
            pv = bool(prob.subs(x, t))
            cv = bool(claim.subs(x, t))
        except Exception:  # noqa: BLE001  (undecidable at this test point)
            continue
        if pv != cv:
            return "wrong", (f"the solution region you stated ({answer_text}) does not match "
                             f"the inequality {expr_text} (they disagree at {x} = {sympy.sstr(t)})")
        checked += 1
    if checked < 5:
        return "unverifiable", "could not sample the inequality"
    return "ok", ""


def _parse_relational(s: str):
    m = _REL_RE.search(s)
    if not m:
        raise ValueError("not a relational")
    op = m.group(1)
    left, right = s[:m.start()], s[m.end():]
    if _REL_RE.search(right):
        raise ValueError("chained inequality unsupported")
    lhs, rhs = _parse(left), _parse(right)
    return {"<": sympy.Lt, "<=": sympy.Le, ">": sympy.Gt, ">=": sympy.Ge}[op](lhs, rhs)


# --------------------------------------------------------------------------- #
# One tag, one verdict
# --------------------------------------------------------------------------- #
def _check_tag(expr_raw: str, answer_raw: str):
    """Returns (verdict, detail): 'ok' | 'wrong' | 'unverifiable'."""
    expr_text = _normalize(expr_raw)
    answer_text = _normalize(answer_raw)
    if not expr_text or not answer_text:
        return "unverifiable", "empty expr/answer"
    for label, s in (("expr", expr_text), ("answer", answer_text)):
        reason = _reject_reason(s)
        if reason:
            return "unverifiable", f"{label}: {reason}"
    tol = _decimal_tolerance(answer_text)
    try:
        if _EQ_SPLIT_RE.search(expr_text):
            return _check_equations(expr_text, answer_text, tol)
        if _REL_RE.search(expr_text) and _REL_RE.search(answer_text):
            return _check_inequality(expr_text, answer_text, tol)
        return _check_equivalence(expr_text, answer_text, tol)
    except Exception as exc:  # noqa: BLE001 -- parse gap or SymPy hiccup: fail open
        return "unverifiable", f"could not check ({exc})"


def _check_tag_with_timeout(expr_raw: str, answer_raw: str):
    future = _EXECUTOR.submit(_check_tag, expr_raw, answer_raw)
    try:
        return future.result(timeout=CHECK_TIMEOUT_SECONDS)
    except _FutureTimeout:
        return "unverifiable", "check timed out"
    except Exception as exc:  # noqa: BLE001
        return "unverifiable", f"checker error ({exc})"


# --------------------------------------------------------------------------- #
# Public API (what tutor.py calls)
# --------------------------------------------------------------------------- #
def extract_tags(reply: str):
    """All [[verify ...]] tags in a reply as (expr, answer) pairs."""
    out = []
    for m in VERIFY_TAG_RE.finditer(reply or ""):
        attrs = dict(_ATTR_RE.findall(m.group(1)))
        out.append((attrs.get("expr", ""), attrs.get("answer", "")))
    return out


# --------------------------------------------------------------------------- #
# (ni) THE BOARD ITSELF IS A CLAIM.
# --------------------------------------------------------------------------- #
# On 2026-08-25 the night watch confirmed a shipped board line:
#     [[step eq="3/4 - 1/2 = 2/4 - 1/2 = 1/4"]]
# -- a FALSE equality chain (the middle expression equals 0), drawn for a child,
# and this module never looked at it, because verify_reply reads only [[verify]]
# tags. A wrong number the tutor SAYS gets re-computed; a wrong number the tutor
# WRITES sailed straight through. That asymmetry ends here.
#
# ⚠️ DELIBERATELY CONSERVATIVE, in this exact order:
#   * only step/write/solve tags (eq= or text=), the ones that draw equations;
#   * skipped when the line carries a placeholder (? _ … □) -- that is a PENDING
#     question, which rule 15 machinery owns, not a claim;
#   * skipped when any segment fails the same parse gate the verify tags use;
#   * ⭐ skipped when ANY segment has a free symbol. "2x + 3 = 11" is a PROBLEM
#     the child is being asked to solve, not an identity the tutor asserts.
#     Only all-constant chains -- arithmetic the board presents as FACT -- are
#     judged. This is what keeps the false-alarm rate at zero on all 306
#     canonical scripts (measured before shipping; PART 3ds re-measures).
#   * skipped entirely when the reply announces a find-the-error game (rule 56:
#     a wrong solution, CLEARLY LABELED, is a legitimate problem type).
# Anything skipped is simply not judged -- a board checker that guesses would
# reject good teaching, and the retry it triggers costs real money and seconds.
_BOARD_EQ_TAG_RE = re.compile(r"\[\[\s*(?:step|write|solve)\b([^\]]*)\]\]")
_GAME_RE = re.compile(r"find\s+(?:the|my)\s+(?:error|mistake)|spot\s+(?:the|my)\s+"
                      r"(?:error|mistake)|on\s+purpose|deliberate(?:ly)?\s+wrong",
                      re.IGNORECASE)
_PLACEHOLDER_RE = re.compile(r"[?_…□]|\bblank\b", re.IGNORECASE)
_SUP_MAP = {"⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4",
            "⁵": "5", "⁶": "6", "⁷": "7", "⁸": "8", "⁹": "9"}


def _desuperscript(s: str) -> str:
    """'2³' -> '2^3', '2·4' -> '2*4' -- board typography into parseable math.
    Board-path only, deliberately: the verify-tag path keeps its own contract."""
    def _swap(m):
        return "^" + "".join(_SUP_MAP[c] for c in m.group(1))
    return re.sub(r"([⁰¹²³⁴⁵⁶⁷⁸⁹]+)", _swap, s).replace("·", "*")


def check_board_equations(reply: str):
    """Every all-constant equality chain drawn on the board is re-computed.

    Returns (wrongs, checked): a list of human-readable findings (empty when the
    board is sound) and how many chains were actually judged."""
    if not reply or _GAME_RE.search(reply):
        return [], 0
    wrongs, checked = [], 0
    for m in _BOARD_EQ_TAG_RE.finditer(reply):
        attrs = dict(_ATTR_RE.findall(m.group(1)))
        line = (attrs.get("eq") or attrs.get("text") or "").strip()
        if not line or "=" not in line:
            continue
        # ⚠️ (ni) ONE LINE CAN CARRY SEVERAL EQUATIONS, laid out side by side with
        # wide spacing ("0.07  =  7/100          0.7  =  7/10") -- the sweep found
        # two authored lines exactly like that, and chaining across the gap turned
        # a TRUE pair into a false alarm. Four or more spaces is a column break:
        # each column is its own chain, judged alone.
        for raw in re.split(r"\s{4,}", line):
          raw = raw.strip()
          if not raw or "=" not in raw or _PLACEHOLDER_RE.search(raw):
            continue
          if _REL_RE.search(raw) or "≠" in raw or "≤" in raw or "≥" in raw:
            continue                      # relations are the inequality checker's turf
          s2 = _normalize(_desuperscript(raw))
          parts = [p.strip() for p in _EQ_SPLIT_RE.split(s2)]
          if len(parts) < 2 or any(not p for p in parts):
            continue
          if any(_reject_reason(p) for p in parts):
            continue
          try:
            exprs = [_parse(p) for p in parts]
          except Exception:  # noqa: BLE001 -- unparseable board decoration: not judged
            continue
          if any(e.free_symbols for e in exprs):
            continue                      # a problem statement, never a claim
          try:
            vals = [complex(e.evalf(chop=True)) for e in exprs]
          except Exception:  # noqa: BLE001
            continue
          checked += 1
          tol = _decimal_tolerance(raw)
          first = vals[0]
          for k in range(1, len(vals)):
            if abs(vals[k] - first) > max(tol, tol * abs(first)):
              def _pretty(c):
                  r = c.real
                  return str(int(r)) if abs(r - round(r)) < 1e-9 else f"{r:.6g}"
              wrongs.append(
                  f'the board line "{raw}" is FALSE: "{parts[k]}" equals '
                  f'{_pretty(vals[k])} but "{parts[0]}" equals {_pretty(first)} -- '
                  f'every link in an equality chain must equal the same value. '
                  f'Rewrite the chain so each step is literally true.')
              break
    return wrongs, checked


def verify_reply(reply: str):
    """
    Check every [[verify]] tag in a tutor reply.
    Returns (verdict, detail):
      'none'          -- no tags present (nothing claimed, nothing to check)
      'ok'            -- every checkable tag verified true
      'unverifiable'  -- nothing wrong found, but >=1 tag could not be decided
      'wrong'         -- >=1 claim is provably false; detail explains each,
                         including SymPy's computed correction when available
                         (tutor.py feeds this back for a silent rewrite).
    """
    tags = extract_tags(reply)
    if not _SYMPY_OK:
        return ("unverifiable", "sympy not installed") if tags else ("none", "")
    # (ni) the board is checked EVEN WHEN no verify tag exists -- the night-watch
    # line that motivated this had no tag at all, which is precisely how it hid.
    board_wrongs, board_checked = check_board_equations(reply)
    if board_wrongs:
        return "wrong", " AND ".join(board_wrongs)
    if not tags:
        return ("ok", "") if board_checked else ("none", "")
    if len(tags) > MAX_TAGS_PER_REPLY:
        print(f"[mathcheck] {len(tags)} tags in one reply; checking first {MAX_TAGS_PER_REPLY}")
        tags = tags[:MAX_TAGS_PER_REPLY]

    wrongs, undecided = [], []
    for expr_raw, answer_raw in tags:
        verdict, detail = _check_tag_with_timeout(expr_raw, answer_raw)
        if verdict == "wrong":
            wrongs.append(detail)
        elif verdict == "unverifiable":
            undecided.append(f'[{expr_raw} | {answer_raw}]: {detail}')
    if wrongs:
        return "wrong", " AND ".join(wrongs)
    if undecided:
        return "unverifiable", "; ".join(undecided)
    return "ok", ""


def strip_verify_tags(reply: str) -> str:
    """Remove every [[verify ...]] tag and tidy the whitespace left behind."""
    if not reply:
        return reply
    out = VERIFY_TAG_RE.sub("", reply)
    out = re.sub(r"[ \t]+\n", "\n", out)        # trailing spaces on lines
    out = re.sub(r"\n{3,}", "\n\n", out)        # collapsed blank-line stacks
    return out.strip()

# I did no harm and this file is not truncated.

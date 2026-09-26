# =============================================================================
# tools/distractorscan.py  --  THE TRUE-DISTRACTOR SCAN  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-09-26  NEW FILE (build yj). The class build yh found in Pre-Calc: a reason
#               question's WRONG choice that is numerically true for the example the
#               question names ("roots 2 and 6 end in 12" -- "because the end number is
#               the bigger root, doubled": 6 doubled IS 12). A child who taps it is right
#               by the numbers and wrong by the reason, and the lesson grades it wrong.
#
#               WHAT IT DOES. For every authored reason question (lesson["explain"]):
#               read the numbers out of the spoken question, take the number the question
#               presents as the RESULT (the one before ", not" -- "ends in the number 12,
#               not 8"; or the last number when there is no "not"), and for each wrong
#               choice read the arithmetic its words name (added / times / doubled /
#               halved / squared / take away / divided / bigger / smaller / average /
#               square root) and compute it over the question's other numbers. A wrong
#               choice whose arithmetic lands on the result is a HIT. Pure text and
#               arithmetic; a distractor in words no rule reads is not judged (the sweep
#               is the only reader for those), and a hit is a candidate to READ, not a
#               verdict -- some phrasings name an operation the example does not use.
#
#               USAGE: python tools/distractorscan.py            (the hits, one per line)
#                      python tools/distractorscan.py --all      (every judged distractor)
#               ruletests PART 3od imports scan() and ratchets the hit count at zero.
# =============================================================================
"""The true-distractor scan. Pure: reads lessonscripts, computes, returns."""
import os
import re
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

_NUM_RE = re.compile(r"(?<![\w.])-?\d+(?:\.\d+)?(?![\w])")
_WORD_NUMS = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
              "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
              "half": 0.5, "a half": 0.5, "a quarter": 0.25}


def _num(s):
    v = float(s)
    return int(v) if v == int(v) else v


def numbers_in(text):
    """The numbers a spoken line names, in order (digits; the small number words;
    "negative 4" is -4)."""
    out = []
    for m in re.finditer(r"(negative\s+)?((?<![\w.])-?\d+(?:\.\d+)?(?![\w])|\b(?:zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)\b)", text, re.I):
        t = m.group(2).lower()
        v = _WORD_NUMS[t] if t in _WORD_NUMS else _num(t)
        out.append(-v if m.group(1) else v)
    return out


_OPENER_RE = re.compile(r"^\s*One more thing\s*[—-]+\s*not the answer, the reason\.\s*", re.I)


def body_of(spoken):
    """The question without the fixed opener ("One more thing -- not the answer, the
    reason.") and without the closing "Tap the reason why." -- the opener's own "One"
    and "not" would otherwise read as a result."""
    s = _OPENER_RE.sub("", spoken or "")
    return re.sub(r"\s*Tap the reason why\.?\s*$", "", s, flags=re.I)


def result_of(spoken):
    """The number the question presents as its result: the last number before ', not';
    else the last number in the sentence that says what happens; else None."""
    spoken = body_of(spoken)
    nums = numbers_in(spoken)
    if not nums:
        return None
    m = re.search(r"((?:-?\d+(?:\.\d+)?)|\b(?:zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)\b)[^\d]{0,40}?,?\s+not\s+", spoken, re.I)
    if m:
        t = m.group(1).lower()
        return _WORD_NUMS[t] if t in _WORD_NUMS else _num(t)
    return nums[-1]


# The operations a wrong choice's words can name. Each is (pattern, function over the
# list of INPUT numbers, arity) -- arity 1 applies to each input, arity 2 to each pair.
_OPS = [
    (r"\b(?:added|add|adds|plus|sum|together|total)\b", lambda a, b: a + b, 2),
    (r"\b(?:times|timesed|product|multipl\w*|timesing)\b", lambda a, b: a * b, 2),
    (r"\b(?:take away|taken away|minus|difference|gap between|subtract\w*|apart)\b", lambda a, b: abs(a - b), 2),
    (r"\b(?:divided|divide|over|quotient|shared)\b", lambda a, b: (a / b if b else None), 2),
    (r"\b(?:doubled|double|twice|two times)\b", lambda a: 2 * a, 1),
    (r"\b(?:halved|half of|halve)\b", lambda a: a / 2, 1),
    (r"\b(?:squared|square of)\b", lambda a: a * a, 1),
    (r"\b(?:square root|root of|un-?squar\w*)\b", lambda a: (a ** 0.5 if a >= 0 else None), 1),
    (r"\b(?:cubed)\b", lambda a: a ** 3, 1),
    (r"\b(?:bigger|biggest|larger|largest|greater)\b", lambda a, b: max(a, b), 2),
    (r"\b(?:smaller|smallest|less|least)\b", lambda a, b: min(a, b), 2),
    (r"\b(?:average|mean|halfway between|middle of)\b", lambda a, b: (a + b) / 2, 2),
    (r"\b(?:one more|plus one|next number)\b", lambda a: a + 1, 1),
    (r"\b(?:one less|minus one)\b", lambda a: a - 1, 1),
]


_CLAIM_RE = re.compile(r"\b(?:is|leaves|gives|makes|equals|comes to|lands on)\s+(-?\d+(?:\.\d+)?)\b|[:=]\s*(-?\d+(?:\.\d+)?)\s*$"
                       r"|^because\s+(-?\d+(?:\.\d+)?)\s+is\s+(?:twice|double|half of|the square of|the square root of)\b", re.I)


def claim_of(choice):
    """The value a wrong choice STATES as its own conclusion ("18 take away 12 is 6" ->
    6; "16 is twice 8" -> 16; "...: 12" -> 12), or None when it states none."""
    m = _CLAIM_RE.search(choice)
    if not m:
        return None
    return _num(next(g for g in m.groups() if g is not None))


def judge(spoken, choice):
    """(ops named, values reached, result, strong). ops empty -> the choice names no
    arithmetic. STRONG: the choice names numbers of its own AND states a conclusion
    ("18 take away 12 is 6") -- the arithmetic is computed on its own numbers, and it is
    a hit when the conclusion equals the question's result and the arithmetic really
    reaches it: a wrong choice that is right by the numbers, the verdict. A choice with
    no numbers of its own is judged over the question's other numbers, every pair, and a
    match there is a CANDIDATE to read (the operation it names may be the question's
    own). A choice that names numbers but states no conclusion is a candidate too."""
    res = result_of(spoken)
    own = numbers_in(choice)
    claim = claim_of(choice) if own else None
    strong = claim is not None
    nums = own if own else numbers_in(body_of(spoken))
    inputs = list(own) if own else ([n for n in nums if n != res] or nums)
    if strong:
        inputs = [n for n in own if n != claim] or own
    ops, vals = [], set()
    low = choice.lower()
    for pat, fn, ar in _OPS:
        if not re.search(pat, low):
            continue
        ops.append(pat.split("|")[0].strip(r"\b(?:"))
        if ar == 1:
            for a in inputs:
                try:
                    v = fn(a)
                except Exception:  # noqa: BLE001
                    v = None
                if v is not None:
                    vals.add(round(v, 6))
        else:
            for i, a in enumerate(inputs):
                for j, b in enumerate(inputs):
                    if i == j:
                        continue
                    try:
                        v = fn(a, b)
                    except Exception:  # noqa: BLE001
                        v = None
                    if v is not None:
                        vals.add(round(v, 6))
    if strong:
        # the verdict: the stated conclusion IS the result, and the named arithmetic reaches it
        ok = res is not None and round(float(claim), 6) == round(float(res), 6) and round(float(claim), 6) in vals
        return ops, ({round(float(claim), 6)} if ok else set()), res, True
    return ops, vals, res, False


def scan(lessons=None):
    """Every judged wrong choice: dicts with lesson, spoken, choice, ops, values, result,
    hit. A hit is a wrong choice whose named arithmetic over the question's numbers
    reaches the question's result."""
    import lessonscripts as L
    out = []
    for les in (lessons if lessons is not None else L.LESSONS):
        e = les.get("explain")
        if not e:
            continue
        spoken = e.get("spoken", "")
        answer = e.get("answer", "").strip()
        for ch in [c.strip() for c in e.get("choices", "").split("|") if c.strip()]:
            if ch == answer:
                continue
            ops, vals, res, strong = judge(spoken, ch)
            if not ops:
                continue
            hit = res is not None and round(float(res), 6) in vals
            out.append({"lesson": les["id"], "course": les["course"], "spoken": spoken,
                        "choice": ch, "ops": ops, "values": sorted(vals), "result": res,
                        "hit": hit, "strong": strong})
    return out


def hits(lessons=None):
    return [r for r in scan(lessons) if r["hit"]]


def verdicts(lessons=None):
    """The strong hits only: wrong choices right by their own numbers."""
    return [r for r in scan(lessons) if r["hit"] and r["strong"]]


def candidates(lessons=None):
    """The weak hits: an operation named in words lands on the result over the question's
    numbers -- read them; each was read at yj and the count is ratcheted."""
    return [r for r in scan(lessons) if r["hit"] and not r["strong"]]


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    rows = scan()
    show = rows if "--all" in argv else [r for r in rows if r["hit"]]
    for r in show:
        print(f"{('HIT!' if r['strong'] else 'hit?') if r['hit'] else '    '} {r['lesson']}: result {r['result']} | {r['choice']!r} -> {r['ops']} {r['values']}")
    print(f"{len(rows)} judged, {sum(1 for r in rows if r['hit'] and r['strong'])} verdict(s), "
          f"{sum(1 for r in rows if r['hit'] and not r['strong'])} candidate(s), "
          f"{len(set(r['lesson'] for r in rows))} lessons")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# I did no harm and this file is not truncated.

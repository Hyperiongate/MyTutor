# =============================================================================
# wordaudit.py  --  THE GIVEAWAY AUDIT, WITH THE NUMBERS SPELLED OUT  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-09-09  NEW (build uw). teachaudit.py and workedaudit.py answer one question:
#               does a beat DEMONSTRATE a problem this lesson later ASKS? Both find
#               their numbers with `re.findall(r"\d+", text)` -- digits only.
#
#               ⚠️ THAT MAKES THEM STRUCTURALLY BLIND TO ENTRY-LEVEL MATH, which
#               spells every number out loud because its students are learning to
#               read. "Six plus six equals twelve" contains no digits at all, so a
#               beat that hands a five-year-old the answer to a problem the same
#               lesson asks has been reported clean since the course was written.
#               Found while bringing Entry Units 2-4 to the shape: `doubles` was
#               demonstrating 6+6, 7+7 and 5+5 with all three in its own bank, and
#               teachaudit said nothing.
#
#               This is the same test with number WORDS understood. It also strips
#               the two fixed worked-beat lead-ins ("Here is one more, done for
#               you.") whose "one" is not part of any problem, and reads compound
#               words properly -- "twenty-five" is 25, not a 20 and a 5. Both of
#               those were false positives on the build that wrote this.
#
#   2026-09-10  BUILD uz -- A UNIT NUMBER IS NOT A PROBLEM NUMBER, and the backlog is
#               triaged. pc-u2-the-minus-parade's why beat opens "Unit Two turns to
#               polynomials"; the audit read a 2, and that lesson's first bank problem
#               is (-1) to the power 2 -- so a sentence about the SYLLABUS was reported
#               as a beat handing away an answer. UNITREF strips a NAMED unit ("Unit
#               Two", "Unit 9") the way LEADIN strips the worked-beat opener; a real
#               number keeps its meaning everywhere else.
#               ⭐ AND THE 21 CANDIDATES ARE READ (Jim's ruling, 2026-09-10): 2 real and
#               closed by moving a BANK problem so no authored sentence was rewritten
#               (pre-u9-a-number-against-a-letter, alg1-u6-copies-of-copies), 15 in
#               lessons whose problem space is EXHAUSTED -- the ten doubles, counting to
#               ten, the four quarter turns, the whole times table, the twelve exponents
#               under 216 -- 3 honest, and this one blind spot. 21 -> 18, and every one
#               of the 18 has been read.
#               DELIBERATELY NOT WIRED INTO ruletests.py, for the same reason
#               teachaudit and workedaudit are not: it reports on content that
#               shipped long ago (31 candidates across the 360 lessons, not yet
#               triaged), and blocking every deploy on a backlog nobody has read
#               teaches people to disable the check. The lessons a BUILD touches
#               are pinned in that build's own PART instead. Run it by hand:
#                   python3 wordaudit.py                 (the whole course)
#                   python3 wordaudit.py <lesson id> ...
# =============================================================================
import re
import sys

import lessonscripts as L

WORDS = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
         "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
         "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
         "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
         "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
         "eighty": 80, "ninety": 90, "hundred": 100}
TENS = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
        "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90}
UNITS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
         "six": 6, "seven": 7, "eight": 8, "nine": 9}

# "Here is one more, done for you." opens every first worked beat in the course; its
# "one" belongs to the sentence, not to any problem.
LEADIN = re.compile(r"^\s*(?:Here is one more, done for you\.|One more together\.)\s*", re.I)
# "twenty-five" is 25. Without this the audit reads a 20 the beat never says.
COMPOUND = re.compile(r"\b(%s)[\s-](%s)\b" % ("|".join(TENS), "|".join(UNITS)), re.I)
# (uz, 2026-09-10) ⚠️ A UNIT NUMBER IS NOT A PROBLEM NUMBER. pc-u2-the-minus-parade's
# why beat opens "Unit Two turns to polynomials", the audit read a 2, and the lesson's
# first bank problem is (-1) to the power 2 -- so a sentence about the SYLLABUS was
# reported as a beat handing away an answer. Same class as LEADIN: a number that
# belongs to the sentence rather than to any problem. Named units only ("Unit Two",
# "Unit 9"), so a real number keeps its meaning everywhere else.
UNITREF = re.compile(r"\bunits?\s+(?:\d+|%s)\b" % "|".join(sorted(WORDS, key=len, reverse=True)), re.I)
TOKEN = re.compile(r"\d+|[A-Za-z]+")


def numbers(text):
    """Every number a beat SAYS, in order, digits and words alike."""
    text = COMPOUND.sub(lambda m: str(TENS[m.group(1).lower()] + UNITS[m.group(2).lower()]),
                        UNITREF.sub("unit", LEADIN.sub("", str(text or ""))))
    out = []
    for tok in TOKEN.findall(text):
        if tok.isdigit():
            out.append(int(tok))
        elif tok.lower() in WORDS:
            out.append(WORDS[tok.lower()])
    return out


def given(p):
    """The numbers a problem HANDS the student, in the order it states them."""
    out = [p["a"]]
    if p.get("b"):
        out.append(p["b"])
    if p.get("c"):
        out.append(p["c"])
    return out


def beats(les):
    """Every beat a student hears BEFORE the practice: why, picture, teach, worked."""
    out = []
    for field in ("why", "picture", "teach"):
        out += [(field, i, s) for i, (s, _b) in enumerate(les.get(field) or [])]
    for i, pair in enumerate(les.get("pairs") or []):
        out.append(("worked", i, pair["worked"][0]))
    return out


def hits(les):
    """Beats that OPEN with a problem's own numbers and then say its answer, for a
    problem this lesson also ASKS. Returns [(id, beat, given, answer, spoken)]."""
    found = []
    problems = list(les.get("bank") or []) + [pr["ask"] for pr in (les.get("pairs") or [])]
    for kind, i, spoken in beats(les):
        said = numbers(spoken)
        if not said:
            continue
        for p in problems:
            g, a = given(p), L.ans(p)
            if len(said) >= len(g) + 1 and said[:len(g)] == g and a in said[len(g):]:
                found.append((les["id"], f"{kind}[{i}]", g, a,
                              " ".join(spoken.split())[:80]))
    return found


def audit(lessons=None):
    out = []
    for les in (lessons if lessons is not None else L.LESSONS):
        out += hits(les)
    return out


if __name__ == "__main__":
    ids = sys.argv[1:]
    rows = audit([L.LESSON_BY_ID[i] for i in ids] if ids else None)
    for lid, beat, g, a, spoken in rows:
        print(f"{lid}  ({beat})")
        print(f"    says : {spoken}")
        print(f"    gives: {g} -> {a}")
    n = len(ids) if ids else len(L.LESSONS)
    print(f"\n{len(rows)} beats demonstrate a problem their own lesson asks, "
          f"across {len({r[0] for r in rows})} lessons of {n}.")


# I did no harm and this file is not truncated.

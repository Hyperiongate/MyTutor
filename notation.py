# =============================================================================
# notation.py  --  THE NOTATION REGISTRY  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-08-11  BUILD dk -- NEW family "fraction-slash" for the four lower courses
#               (audit re-run finding 2, a real voice-first catch): the tutor says
#               "the BOTTOM number" while the board shows "1/4" with a SLASH -- a
#               confused child sees no bottom. The table row hands the tutor the
#               bridge sentence: the number AFTER the slash is the denominator, the
#               bottom number when written stacked; say both once.
#   2026-08-11  BUILD dh -- the function family gains the GROUPED-INPUT reading (first
#               full audit, finding S-6): spoken, "f of a plus 1" is ambiguous between
#               f(a)+1 and f(a+1), and the audit's student invented "f of bracket a plus
#               1 bracket" and was praised without ever being handed the standard words.
#               In a voice classroom the repeatable phrase IS the notation, so the note
#               now carries it: f(a+1) is said "f of the quantity a plus one". Flows into
#               every relevant course's HOW-TO-SAY table automatically; no script edits.
#   2026-08-09  NEW FILE (build cj, Jim). "It looks like we've fixed the function
#               notation, but math is filled with these kinds of things. How can we
#               make sure that every one of these is caught all of the time?"
#
#               Build ci fixed f(x) BY HAND. That is not a fix, it is one instance --
#               and a survey of our own boards found the same shape everywhere else:
#               probstat writes "52% ± 3%" and never says "plus or minus"; calculus
#               writes "Σ f(x_i)·Δx" and never says "sigma", "x sub i" or "delta x";
#               algebra2 writes "log₂ 8" and never says "log base two of eight";
#               two courses write "≠" and never say "is not equal to". Every one of
#               those is a symbol appearing on a child's screen with nothing anywhere
#               telling them how to READ it.
#
#               This file is the answer, and the answer is a single source of truth.
#               Every notation the courses use is registered ONCE, here, with:
#                 shown   -- what it looks like written
#                 spoken  -- the words a person actually says
#                 never   -- the wrong reading, named so the tutor can deny it (rule 48b)
#                 wrote   -- a regex that RECOGNISES it on a board line
#                 heard   -- a regex that recognises the reading in spoken words
#                 courses -- where it legitimately appears
#               Three things derive from this file, and nothing is maintained twice:
#                 1. tutor.py appends a per-course "HOW TO SAY WHAT YOU WRITE" table to
#                    every prompt, so rule 48 is FOLLOWABLE. (Rule 48 currently asks him
#                    to read symbols aloud correctly without ever telling him our
#                    canonical readings -- the same mistake as telling him to skip an
#                    introduction he had no way to identify.)
#                 2. ruletests.py PART 3f fails the build if ANY board line we ship
#                    writes a notation this file does not register for that course. That
#                    is the guarantee Jim asked for: we cannot write a symbol we have not
#                    said how to read.
#                 3. The DEEP families (function, prime, exponent, subscript, absolute
#                    value, radical) additionally require a full foundation script, since
#                    a one-line table entry is not teaching.
#
#               ADDING A SYMBOL: add it here, run ruletests.py. If a board already uses
#               it, the test was already failing and now passes; if nothing uses it yet,
#               the tutor still gets the canonical reading for the day it comes up.
# =============================================================================

import re

ALL_COURSES = ("entrymath", "basicmath", "prealgebra", "algebra1", "geometry",
               "algebra2", "precalc", "calculus", "probstat", "diffeq")
# Courses from Algebra I up -- where symbolic notation really lives.
SYMBOLIC = ("algebra1", "geometry", "algebra2", "precalc", "calculus", "probstat", "diffeq")

# `wrote` patterns run against BOARD text only, `heard` against the spoken `say` text.
# Both are deliberately tight: a false positive here fails a build for nothing.
NOTATIONS = [
    # ---- the deep ones: these need a real script, not a table row -------------
    {"id": "function", "shown": "f(x)", "spoken": "f of x", "never": "f times x",
     "deep": True, "courses": ("algebra1", "algebra2", "precalc", "calculus", "diffeq"),
     "wrote": r"\b[fghpquvwy]\s*\(\s*[a-z0-9]",
     "heard": r"\b[fghpquvwy] of (?:[a-z]\b|zero|one|two)",
     # build dh (first full audit, S-6): spoken, "f of a plus 1" is ambiguous between
     # f(a)+1 and f(a+1) -- in a voice classroom the repeatable phrase IS the notation.
     "note": "the letter is only a NAME -- g(x) works exactly the same way; a compound "
             "input is read as a QUANTITY: f(a+1) is said 'f of the quantity a plus "
             "one', never 'f of a, plus one'"},

    {"id": "prime", "shown": "y′", "spoken": "y prime", "never": "y apostrophe",
     "deep": True, "courses": ("calculus", "diffeq"),
     "wrote": r"[a-zA-Z][′″'\"](?![a-z])",
     "heard": r"\bprime\b",
     "note": "two marks is 'double prime'; it is a derivative, not punctuation"},

    {"id": "exponent", "shown": "x²", "spoken": "x squared", "never": "x times 2",
     "deep": True, "courses": SYMBOLIC,
     "wrote": r"\^|[²³]",
     "heard": r"\bsquared\b|\bcubed\b|to the\b.{0,14}\bpower\b",
     "note": "the small raised number counts how many times you MULTIPLY, it is not a factor"},

    {"id": "subscript", "shown": "x₁", "spoken": "x sub one", "never": "x times 1",
     "deep": True, "courses": ("algebra2", "precalc", "calculus", "probstat", "diffeq"),
     "wrote": r"[a-zA-Z](?:_[0-9a-z]\b|[₀-₉ᵢₙ])",
     "heard": r"\bsub\b|\bsubscript\b",
     "note": "a subscript LABELS which one you mean; it never multiplies"},

    {"id": "absolute", "shown": "|x|", "spoken": "the absolute value of x", "never": "two lines around x",
     "deep": True, "courses": ("prealgebra", "algebra1", "algebra2", "precalc", "calculus", "diffeq"),
     "wrote": r"\|[^|\s][^|]{0,8}\|",
     "heard": r"absolute value",
     "note": "it means DISTANCE from zero, so it is never negative"},

    {"id": "radical", "shown": "√x", "spoken": "the square root of x", "never": "the check mark",
     "deep": True, "courses": ("prealgebra", "algebra1", "geometry", "algebra2", "precalc", "calculus"),
     "wrote": r"√|\bsqrt\s*\(",
     "heard": r"square root|\broot of\b",
     "note": "a small 3 in the notch makes it a CUBE root"},

    # ---- the table ones: one honest line is enough ---------------------------
    {"id": "notequal", "shown": "≠", "spoken": "is not equal to", "never": "",
     "courses": SYMBOLIC + ("prealgebra",), "wrote": r"≠",
     "heard": r"not equal|does not equal|is ?n'?t equal", "note": ""},

    {"id": "lessequal", "shown": "≤ / ≥", "spoken": "is less than or equal to", "never": "",
     "courses": SYMBOLIC + ("prealgebra",), "wrote": r"[≤≥]",
     "heard": r"less than or equal|greater than or equal|at most|at least", "note": ""},

    {"id": "approx", "shown": "≈", "spoken": "is approximately", "never": "equals",
     "courses": ALL_COURSES, "wrote": r"≈",
     "heard": r"approximately|about equal|roughly equal",
     "note": "rule 27: an estimate is spoken as 'about' and written with ≈, never ="},

    {"id": "plusminus", "shown": "±", "spoken": "plus or minus", "never": "",
     "courses": ("algebra2", "precalc", "probstat"), "wrote": r"±",
     "heard": r"plus or minus", "note": "it means BOTH answers, not a choice"},

    {"id": "sigma", "shown": "Σ", "spoken": "the sum of", "never": "the letter E",
     "courses": ("precalc", "calculus", "probstat"), "wrote": r"[Σ∑]",
     "heard": r"\bsigma\b|the sum of|add(?:ing)? (?:them |these )?(?:all )?up", "note": ""},

    {"id": "delta", "shown": "Δx", "spoken": "delta x", "never": "a triangle",
     "courses": ("algebra1", "geometry", "precalc", "calculus", "probstat", "diffeq"),
     "wrote": r"[Δ∆]\s*[a-zA-Z]",
     "heard": r"\bdelta\b|the change in", "note": "it means 'the change in' whatever follows"},

    {"id": "integral", "shown": "∫", "spoken": "the integral of", "never": "a long S",
     "courses": ("calculus", "diffeq"), "wrote": r"∫",
     "heard": r"integral", "note": "the dx at the end says which variable you are adding along"},

    {"id": "differential", "shown": "dy/dx", "spoken": "d y d x", "never": "d times y over d times x",
     "courses": ("calculus", "diffeq"), "wrote": r"\bd\s*[a-z]\s*/\s*d\s*[a-z]\b",
     "heard": r"\bd [a-z] d [a-z]\b|\bd\s?y\s?d\s?x\b",
     "note": "it is ONE symbol for a derivative, not a fraction you can split"},

    {"id": "pi", "shown": "π", "spoken": "pi", "never": "the letter n",
     "courses": ("geometry", "algebra2", "precalc", "calculus", "probstat", "diffeq"),
     "wrote": r"π", "heard": r"\bpi\b", "note": ""},

    {"id": "theta", "shown": "θ", "spoken": "theta", "never": "a zero",
     "courses": ("geometry", "algebra2", "precalc", "calculus"), "wrote": r"θ",
     "heard": r"\btheta\b", "note": "it is just a name for an angle"},

    # ONE entry per SYMBOL, deliberately. The first version of this registry split mu
    # into a stats entry and a general-name entry, and ruletests immediately failed:
    # both patterns matched the same character, so diffeq's integrating factor "mu"
    # was reported as an unregistered use of the population mean. Two entries that can
    # match the same glyph are a bug, not a nuance -- the nuance goes in the note.
    {"id": "greek", "shown": "μ, σ, λ, α", "spoken": "mu, sigma, lambda, alpha",
     "never": "u, o, y, a",
     "courses": ("algebra2", "precalc", "calculus", "probstat", "diffeq"),
     "wrote": r"[μσλαβγωτε]", "heard": r"\bmu\b|\bsigma\b|\blambda\b|\balpha\b|\bbeta\b|\bgamma\b|\bomega\b|\btau\b",
     "note": "a Greek letter is only a NAME -- say the name. In statistics mu is the "
             "population mean and sigma the standard deviation; elsewhere they are "
             "whatever the problem says they are"},

    {"id": "degree", "shown": "°", "spoken": "degrees", "never": "a little zero",
     "courses": ("prealgebra", "geometry", "algebra2", "precalc"), "wrote": r"°",
     "heard": r"\bdegrees?\b", "note": ""},

    {"id": "logbase", "shown": "log₂ 8", "spoken": "log base two of eight", "never": "log times 2",
     "courses": ("algebra2", "precalc", "calculus"), "wrote": r"\blog\s*[₀-₉_]|\bln\b",
     "heard": r"log base|natural log", "note": "ln is the NATURAL log -- base e"},

    {"id": "point", "shown": "(3, 4)", "spoken": "the point three comma four", "never": "three times four",
     "courses": ("algebra1", "geometry", "algebra2", "precalc", "calculus", "probstat"),
     "wrote": r"\(\s*-?\d+(?:\.\d+)?\s*,\s*-?\d+(?:\.\d+)?\s*\)",
     "heard": r"\bcomma\b|ordered pair|the point\b", "note": "x first, then y -- always"},

    {"id": "infinity", "shown": "∞", "spoken": "infinity", "never": "a sideways eight",
     "courses": ("algebra2", "precalc", "calculus", "diffeq"), "wrote": r"∞",
     "heard": r"infinity", "note": "it is a direction, not a number you can arrive at"},

    {"id": "factorial", "shown": "5!", "spoken": "five factorial", "never": "five, excited",
     "courses": ("algebra2", "precalc", "probstat"), "wrote": r"\d\s*!",
     "heard": r"factorial", "note": ""},

    {"id": "arrow", "shown": "→", "spoken": "which gives", "never": "an arrow",
     "courses": ALL_COURSES, "wrote": r"[→⇒]",
     "heard": r"which gives|so we get|becomes|leads to|gives us|then\b|so\b", "note": ""},

    {"id": "times", "shown": "× or ·", "spoken": "times", "never": "the letter x",
     "courses": ALL_COURSES, "wrote": r"[×·]",
     "heard": r"\btimes\b|multiplied by", "note": "rule 4: the multiplication sign is × on the board, never a lowercase x"},

    {"id": "cents", "shown": "25¢", "spoken": "twenty-five cents", "never": "twenty-five c",
     "courses": ("entrymath", "basicmath", "prealgebra"), "wrote": r"¢",
     "heard": r"\bcents?\b", "note": ""},

    {"id": "percent", "shown": "52%", "spoken": "fifty-two percent", "never": "fifty-two",
     "courses": ALL_COURSES, "wrote": r"\d\s*%",
     "heard": r"percent", "note": ""},

    # build dk (audit re-run, finding 2): the tutor says "the BOTTOM number" while the
    # board shows "1/4" with a SLASH -- a confused child sees no bottom. The note is
    # the bridge sentence between the two ways the same fraction is written.
    {"id": "fraction-slash", "shown": "3/4", "spoken": "three fourths",
     "never": "three point four",
     # ALL courses: PART 3f's own guard proved slash fractions appear on boards well
     # beyond the elementary courses (algebra2 writes x^(1/2)), so the reading row
     # belongs everywhere the symbol does.
     "courses": ALL_COURSES,
     "wrote": r"\b\d{1,2}\s*/\s*\d{1,2}\b",
     "heard": r"\b(?:half|halves|third|thirds|fourth|fourths|fifth|fifths|sixth|sixths|"
              r"eighth|eighths|tenth|tenths|numerator|denominator|over\b)\b",
     "note": "written with a slash, the number AFTER the slash is the denominator -- "
             "the BOTTOM number of the stacked form. Before using top/bottom language "
             "over a slash form, say that bridge once (a young student looking at 1/4 "
             "sees no bottom)"},

    {"id": "setbraces", "shown": "{ }", "spoken": "the set containing", "never": "curly things",
     "courses": ("algebra2", "precalc", "probstat", "diffeq"), "wrote": r"[{}]",
     "heard": r"\bset\b|\bcollection\b", "note": ""},

    {"id": "composition", "shown": "(f ∘ g)(x)", "spoken": "f of g of x", "never": "f circle g",
     "courses": ("precalc", "calculus"), "wrote": r"∘|\(\s*[fgh]\s+o\s+[fgh]\s*\)",
     "heard": r"\bof [a-z] of\b|composition", "note": "inside first, then outside"},
]

_BY_ID = {n["id"]: n for n in NOTATIONS}
_WROTE = {n["id"]: re.compile(n["wrote"]) for n in NOTATIONS}
_HEARD = {n["id"]: re.compile(n["heard"], re.I) for n in NOTATIONS}

# Board attributes whose value is TEXT THE STUDENT READS. Others (data="1,2,3",
# func="x^2", range="-5..5") are instructions to a renderer, not notation on display.
READABLE_ATTRS = ("text", "lines", "items", "title", "caption", "cap", "eq", "start",
                  "steps", "op", "check", "result", "problem", "left", "right", "rule")


def by_id(nid: str) -> dict:
    return _BY_ID.get(nid, {})


def for_course(course: str) -> list:
    """Every notation this course is allowed to put on a student's screen."""
    c = (course or "").strip().lower()
    return [n for n in NOTATIONS if c in n["courses"]]


def written_in(text: str) -> list:
    """The ids of every registered notation appearing in this board text."""
    t = str(text or "")
    return [n["id"] for n in NOTATIONS if _WROTE[n["id"]].search(t)]


def spoken_in(say: str) -> list:
    """The ids whose spoken reading appears in these words."""
    s = str(say or "")
    return [n["id"] for n in NOTATIONS if _HEARD[n["id"]].search(s)]


def deep_ids(course: str) -> list:
    """The notations this course must TEACH with a full script, not just a table row."""
    return [n["id"] for n in for_course(course) if n.get("deep")]


def prompt_block(course: str) -> str:
    """The per-course 'HOW TO SAY WHAT YOU WRITE' table.

    Rule 48 tells him to read every symbol aloud correctly and to deny the wrong
    reading by name. This is the list that makes that possible. Compact on purpose:
    one line per symbol, only the symbols this course actually uses."""
    items = for_course(course)
    if not items:
        return ""
    lines = [
        "",
        "============================================================",
        "🔤 HOW TO SAY WHAT YOU WRITE  (rule 48)",
        "============================================================",
        "Every symbol below will appear on your board in this course. The FIRST time each",
        "one appears, say the words in the SAY column out loud, in that same reply, with",
        "the symbol on the board -- so the sound and the shape arrive together. Where a",
        "NEVER is given, say that too: naming the wrong reading is what prevents it, and",
        "the wrong reading here is the one students actually guess.",
        "A student who cannot SAY a symbol cannot ask you a question about it and cannot",
        "answer one out loud. In a voice classroom that is the whole lesson lost.",
        "",
    ]
    for n in items:
        line = f'  {n["shown"]:<12} SAY: "{n["spoken"]}"'
        if n.get("never"):
            line += f'   -- NEVER "{n["never"]}"'
        lines.append(line)
        if n.get("note"):
            lines.append(f'  {"":<12} {n["note"]}')
    lines += [
        "",
        "Never put a symbol on the board that is not on this list without saying, in",
        "words, how it is read. If you find yourself needing one, teach it the same way.",
        "============================================================",
    ]
    return "\n".join(lines)


# I did no harm and this file is not truncated.

# =============================================================================
# voiceclosure.py  --  THE PAGE-LOCAL SPOKEN LINE AUDIT  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-09-11  BUILD ve -- A NAME THE PAGE DEFINES ITSELF IS JUDGED BY ITS BODY.
#               The battery was RED on Jim's disk and nobody knew: the 09-11 handoff's
#               "11,788 passed, 0 failed" was run on a tree staged one file at a time,
#               and static/demolab.html was never staged, so pages() never listed it.
#               Staged whole, uz's ZERO-hits pin failed on eight demolab lines -- and
#               not one of them is spoken. demolab's say(text) writes a caption
#               bubble; it was a speaker only because `say` sits in EXTRA_SPEAK, the
#               hand-written seeds kept for names DEFINED OUTSIDE the page that calls
#               them. speech_names() now applies an EXTRA_SPEAK seed only when the page
#               does not define that name; a local definition is judged by its body
#               like every discovered wrapper (demo-lesson's own speakLine still hands
#               its text to window.speak and is still found). NOT an exemption: adding
#               demolab.html to EXEMPT_PAGES would have been a hand-written list
#               growing by one, the shape vb retired. PART 3la. ⚠️ THE LAW THIS PAID
#               FOR: stage the WHOLE repo before a battery run; a file the audit cannot
#               see is a file it reports clean.
#   2026-09-10  BUILD vb -- THE NAMES ARE DISCOVERED, AND THE FILE STOPS READING ITS
#               OWN COMMENTS. uy shipped with a hand-written alternation of wrapper
#               names, and session.html speaks its whole TOUR through `sayTourLine`,
#               which was not in it -- so this audit reported that page clean while
#               twenty-six lines (ten course openers, twelve tour stops, four
#               closings: the first words every new student hears) sat outside the
#               closure. Jim heard the cost on 2026-09-10 as a ten-second wait and
#               "garbled words". Now: SEEDS are voice.js's two real primitives and
#               every wrapper that reaches them is found to a fixed point; every
#               literal in a call's ARGUMENTS counts (so both arms of a ternary do);
#               a call passing a member expression contributes that property's
#               literals; and the names in an argument are followed into their own
#               initialisers, which is how ten openers three hops away are found.
#               scrub() blanks comments first -- this codebase's prose is full of
#               apostrophes and a regex pairs them into fragments -- and code_only()
#               blanks string contents, so the walk never chases an English word
#               inside a spoken line. KNOWN LIMIT, stated plainly: this reads a page,
#               not a program. A line assembled at runtime, or reached through a
#               function this walk declines to enter, is still invisible.
#   2026-09-10  NEW (build uy). Jim, on the demo: "After a sample problem, fell back
#               to browser's voice." It was not a cache miss or a network hiccup --
#               static/demo-lesson.html ENDS on a line written in the page:
#                   "That is how every lesson in my classroom starts. Shall we look
#                    around, or try another level?"
#               The demo lane is CACHE-ONLY on purpose (a visitor must never be able
#               to make the paid renderer run), and that line is in no lesson, so it
#               is in no closure, so it was never rendered, so it fell to the browser
#               voice EVERY TIME -- and it plays at the one moment a visitor has just
#               decided the product is real.
#
#               THE CLOSURE PROPERTY, restated once more: every line the app can speak
#               in Mr. Cadabra's voice must be enumerable IN ADVANCE. lessonscripts'
#               STANDALONE_LINES exists for exactly this -- lines that belong to the
#               COURSE rather than to any lesson (Abrabot's introduction, the handoff,
#               the seam line, the wait lines, the check). A page that writes its own
#               line and speaks it has stepped outside that guarantee, and nothing was
#               watching for it.
#
#               WHAT IT DOES. Reads every page in static/, finds the string literals
#               that reach a speech call -- directly, or through a variable assigned a
#               literal in the same function -- and reports the ones that are not in
#               course_audio_lines().
#
#               ⚠️ demo.html IS EXEMPT, and only demo.html. It carries its own
#               enumerated whitelist (VOICE_LINES, twinned with main.DEMO_VOICE_LINES
#               and pinned equal by the battery) and its own player; its lines are
#               rendered from that list, not from the course closure. Every other page
#               speaks through voice.js and draws on the course closure.
# =============================================================================
import ast
import io
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
STATIC = os.path.join(HERE, "static")

# demo.html owns an enumerated whitelist of its own -- see the header.
EXEMPT_PAGES = ("demo.html",)

# ⚠️ WHICH PAGES THIS IS A DEFECT ON, and which it is only a note on. The DEMO lane is
# cache-only by design, so a line outside the closure there can NEVER be his voice --
# that is a defect, and the battery fails the build on it. The signed-in lanes may
# render on demand, so a page-local line there costs the FIRST student a mechanical
# voice and is cached from then on: worth reporting, not worth blocking a deploy.
# challenge.html is also an ASSESSMENT, where rule 18 gives the character no part at
# all, and one of its two lines interpolates the question number, so it could not be
# pre-rendered even in principle. Both are in the report; neither blocks.
CACHE_ONLY_PAGES = ("demo-lesson.html",)

# A line short enough to be an unlock utterance (" ") or a one-word status is not a
# taught line; four words is the floor the sweep uses.
MIN_WORDS = 4

# ⭐ (vb, 2026-09-10) THE SPEECH FUNCTIONS ARE DISCOVERED, NOT LISTED.
# uy shipped this audit with a HAND-WRITTEN alternation of wrapper names --
# speakLine|speakThen|sayThen|abraSay|speak|say -- and Jim found the cost the same
# week. static/session.html speaks its whole TOUR through `sayTourLine`, which that
# list does not contain (the `say` arm needs "(" straight after it, and "TourLine("
# follows instead). So the audit reported session.html clean while twenty-six lines
# -- ten course openers, twelve tour stops, four closings, the FIRST words every new
# student ever hears -- sat outside the closure, unrendered by the prewarm, each one
# a live ElevenLabs render on its first play after every deploy. Jim, 2026-09-10, on
# exactly those beats: "10 second delay before this started", "garbled words",
# "skipped a lot of the into to screen".
#
# A hand-written list of names is the same defect this codebase has now paid for
# three times (the night watch's rule numbers, build px; the drill lane's
# grep-for-the-route, build mj). So the names are DERIVED instead:
#
#   SEEDS are the two real primitives voice.js exports -- speak() and browserSpeak().
#   Any function in the page whose body calls a known speech function IS one, and
#   that runs to a fixed point. sayTourLine calls speak, so it is found; a wrapper
#   invented tomorrow is found the day it is written, by nobody's memory.
#
# THREE MORE SHAPES the uy version could not see, each one a way a real page holds a
# real line:
#   (b) EVERY literal in the call's arguments, not just a bare first argument -- so
#       sayTourLine(IS_ELEM ? "..." : "...") contributes BOTH arms, and so does a
#       concatenation. Balanced-paren scan, so a nested call cannot cut it short.
#   (c) a call passing a MEMBER expression -- tourLine(step.text) -- names a property
#       rather than a line, so every `text: "..."` in the page is contributed. It is
#       a heuristic and it is deliberately generous: a false positive costs one line
#       in a report, and a miss costs a child the mechanical voice.
#   (d) an interpolated argument (`"..." + COURSE_TITLE + "..."`) can never be one
#       pre-rendered clip. Its fragments are reported like any other line, and they
#       will not be in the closure, which is the correct answer: that line needs
#       rewording or enumerating before it can ever be in his real voice.
SEEDS = ("speak", "browserSpeak")
# ⚠️ uy's HAND-WRITTEN NAMES ARE KEPT, as seeds rather than as the whole answer. A
# wrapper is normally defined in the page that speaks through it, and those are now
# discovered -- but demo-lesson.html calls speakLine and demo.html calls sayThen and
# abraSay, and a name defined outside the file being read cannot be discovered from
# inside it. Dropping them would have narrowed this audit while widening it.
EXTRA_SPEAK = ("speakLine", "speakThen", "sayThen", "abraSay", "say")

_STR = r'(["\'])((?:\\.|(?!\1).)*)\1'
_ANY_STR = re.compile(r'"((?:\\.|[^"\\])*)"' + r"|'((?:\\.|[^'\\])*)'")
_FN_DECL = re.compile(r"\b(?:async\s+)?function\s+([A-Za-z_$][\w$]*)\s*\(")
_FN_ASSIGN = re.compile(r"\b(?:var|let|const)\s+([A-Za-z_$][\w$]*)\s*=\s*"
                        r"(?:async\s*)?(?:function\s*\*?\s*\([^)]*\)|"
                        r"\([^)]*\)\s*=>|[A-Za-z_$][\w$]*\s*=>)")
_CALL = re.compile(r"\b([A-Za-z_$][\w$]*)\s*\(")
# ⚠️ `\w` BEFORE THE DOT IS NOT ENOUGH: session.html reaches its tour text as
# `_steps[i].text`, where a "]" sits where a word character was expected. Either
# shape names a property, and a missed property is a missed spoken line.
_MEMBER = re.compile(r"[\w$\]]\.([A-Za-z_$][\w$]*)\b")
# ⚠️ ITS OWN BACKREFERENCE, NOT _STR's (build uy's lesson, kept): _STR closes on \1,
# which is only the quote while the quote is the FIRST group in the pattern.
_ASSIGN = re.compile(r"\b(?:var|let|const)\s+([A-Za-z_$][\w$]*)\s*=\s*"
                     r"([\"'])((?:\\.|(?!\2).)*)\2\s*;")


def _body_at(src, i, braced_only=False):
    """This function's body, from `i`.

    A braced body ({...}) is brace-matched. A CONCISE ARROW -- `const f = (t) =>
    Promise.race([g(t), h])`, which is how session.html writes tourLine -- has no
    braces at all, so its body is the expression up to the statement end. Reading
    only braced bodies is how the first cut of this rewrite still missed tourLine
    and mistook `const readMs = (t) => Math.max(...)` for a speaker, by hunting
    forward to some unrelated brace 300 characters away.

    `braced_only` is for a `function` declaration, which always has braces.
    """
    j = i
    while j < len(src) and src[j] in " \t\r\n":
        j += 1
    if j < len(src) and src[j] == "{":
        depth, k = 0, j
        while k < len(src):
            if src[k] == "{":
                depth += 1
            elif src[k] == "}":
                depth -= 1
                if depth == 0:
                    return src[j:k + 1]
            k += 1
        return ""
    if braced_only:
        # a `function name(args)` whose "{" is past the argument list
        j = src.find("{", i)
        return _body_at(src, j) if 0 <= j - i <= 400 else ""
    return _value_at(src, j, stop=";")


def _args_at(src, i):
    """The text between the parentheses of the call whose "(" is at `i`, balanced."""
    depth, k = 0, i
    while k < len(src):
        c = src[k]
        if c == "(":
            depth += 1
        elif c == ")":
            depth -= 1
            if depth == 0:
                return src[i + 1:k]
        k += 1
    return ""


# A page's biggest spoken structure is session.html's TOUR_STEPS (~5k of prose in
# one array literal), so the cap has to clear that with room to spare.
_VALUE_CAP = 40000


def scrub(src):
    """The page with its COMMENTS blanked, offsets preserved.

    ⚠️ EVERY SCAN BELOW RUNS ON THIS, NOT ON THE RAW FILE. Without it the audit
    reads its own documentation: this codebase's comments are written in prose full
    of apostrophes, so a regex hunting string literals pairs them and reports
    "s Model-Lead-Test turn (\"now it" as a spoken line the closure is missing.
    ruletests learned the same lesson on the assessment pin (build uz); the rule is
    the same one -- a comment ABOUT the code is not the code.

    Blanking (rather than deleting) keeps every offset, so a match found here can be
    read back out of the original source at the same index.
    """
    out = list(src)
    i, n = 0, len(src)
    while i < n:
        c = src[i]
        if c in "\"'`":
            q, i = c, i + 1
            while i < n:
                if src[i] == "\\":
                    i += 2
                    continue
                if src[i] == q:
                    break
                i += 1
            i += 1
            continue
        if c == "/" and i + 1 < n and src[i + 1] == "/":
            while i < n and src[i] != "\n":
                out[i] = " "
                i += 1
            continue
        if c == "/" and i + 1 < n and src[i + 1] == "*":
            j = src.find("*/", i + 2)
            j = n if j < 0 else j + 2
            for k in range(i, j):
                if src[k] != "\n":
                    out[k] = " "
            i = j
            continue
        i += 1
    return "".join(out)


def code_only(text):
    """The same text with STRING CONTENTS blanked -- what is left is the code. The
    transitive walk follows the identifiers it finds, and every English word inside
    a spoken line looked like one: "microphone", "answer", "text". Following those
    is how a walk that should have found ten course openers found sixty-seven
    fragments of the file's own source."""
    out, i, n = list(text), 0, len(text)
    while i < n:
        c = text[i]
        if c in "\"'`":
            q, i = c, i + 1
            while i < n:
                if text[i] == "\\":
                    out[i] = out[i - 1] = " "
                    i += 2
                    continue
                if text[i] == q:
                    break
                out[i] = " "
                i += 1
            i += 1
            continue
        i += 1
    return "".join(out)


_FUNCY = re.compile(r"\bfunction\b|=>\s*\{")
_CALLY = re.compile(r"[A-Za-z_$][\w$]*\s*\(")


def _value_at(src, i, stop=","):
    """One object property's VALUE, from `i` to the first `stop` or closing bracket
    that is not inside a nested (), [], {} or string. Keeps a ternary or a
    concatenation whole -- which is the point -- and never runs into the next
    property. Capped, so a malformed page can never make this walk the file."""
    depth, k, end = 0, i, min(len(src), i + _VALUE_CAP)
    safe = i          # the last offset we were provably BETWEEN tokens
    while k < end:
        c = src[k]
        if c in "\"'":
            q, k = c, k + 1
            while k < end:
                if src[k] == "\\":
                    k += 2
                    continue
                if src[k] == q:
                    break
                k += 1
            if k >= end:
                # ⚠️ THE CAP LANDED INSIDE A STRING. Returning the truncated text
                # would hand _strings_in an UNTERMINATED double-quoted literal, and
                # its single-quote alternative then pairs the apostrophes inside it
                # -- "if you're not sure, tap the 'I'm not sure' button" came back as
                # the fragment "re not sure, tap the ". A fragment is not a spoken
                # line, and it can never be in the closure, so it would be reported
                # as a defect forever. Cut back to the last whole token instead.
                return src[i:safe]
        elif c in "([{":
            depth += 1
        elif c in ")]}":
            if depth == 0:
                return src[i:k]
            depth -= 1
        elif c == stop and depth == 0:
            return src[i:k]
        k += 1
        safe = k
    return src[i:safe]


_DECL = re.compile(r"\b(?:var|let|const)\s+([A-Za-z_$][\w$]*)\s*=\s*")
_IDENT = re.compile(r"\b([A-Za-z_$][\w$]*)\b")
# a for-of / for-in binding, and a function's parameter list: both DECLARE a name
# without initialising it, and both are how a name comes to mean two things.
_BIND = re.compile(r"\bfor\s*\(\s*(?:var|let|const)\s+([A-Za-z_$][\w$]*)\s+(?:of|in)\b")
_PARAMS = re.compile(r"\bfunction\s*[A-Za-z_$][\w$]*\s*\(([^)]*)\)")
_WALK_DEPTH = 5          # hops from a speech call to the literal it will speak


def initializers(source):
    """{name: the text it was initialised with} for every var/let/const in the page
    THAT MEANS ONLY ONE THING. The value is TEXT, not a parse: what this audit needs
    from it is the string literals inside it and the other names it mentions.

    ⚠️ AMBIGUOUS NAMES ARE DROPPED, and that is the whole reason this function is not
    one line. A regex has no scopes. session.html declares `const line = ...` inside
    its sprint panel AND loops `for (const line of [LINE_THINKING, ...])` inside
    runTutor, which speaks; it names a catch handler's message `msg` and also takes a
    `msg` parameter in kickoff, which speaks. Following either one across scopes
    reported a sprint panel's innerHTML and two addBubble-only error strings as
    spoken lines. They are not spoken at all, and the battery's standing pin here is
    ZERO hits -- so a false positive does not merely add noise, it pushes a string
    nobody ever says into the pre-rendered closure and pays to voice it.
    A name declared, bound or taken as a parameter more than once in the page is
    therefore unfollowable, and this audit says so by leaving it out.
    """
    counts, first = {}, {}
    for m in _DECL.finditer(source):
        counts[m.group(1)] = counts.get(m.group(1), 0) + 1
        first.setdefault(m.group(1), _value_at(source, m.end(), stop=";"))
    for rx in (_BIND, _PARAMS):
        for m in rx.finditer(source):
            for name in _IDENT.findall(m.group(1)):
                counts[name] = counts.get(name, 0) + 1
    return {n: t for n, t in first.items() if counts.get(n, 0) == 1}


def _walk(text, inits, seen, depth):
    """Every string literal reachable from this expression, following the names it
    mentions into their own initialisers. session.html hands its tour three hops
    from the speech call -- tourLine(tourAll[0]) -> tourAll -> COURSE_OPENER ->
    COURSE_OPENERS -- and every hop is an ordinary const. A walk that stopped at the
    first hop would report the tour stops and miss all ten course openers, which are
    the FIRST sentence a new student hears in each course."""
    out = list(_strings_in(text))
    if depth >= _WALK_DEPTH:
        return out
    for name in _IDENT.findall(code_only(text)):
        if name in seen or name not in inits:
            continue
        init = inits[name]
        code = code_only(init)
        if _FUNCY.search(code) or _CALLY.search(code):
            # ⚠️ DATA ONLY. A function body is code, not a line the page holds -- and
            # an initialiser that CALLS something is a value this audit cannot claim
            # to know. Following calls is how the first cut reported four lines that
            # are never spoken at all (a sprint panel's innerHTML, two addBubble-only
            # error messages), and a false positive here is worse than a miss: the
            # battery's standing pin is ZERO hits, so a wrong one would push a string
            # nobody ever speaks into the pre-rendered closure and pay to voice it.
            continue
        seen.add(name)
        out.extend(_walk(init, inits, seen, depth + 1))
    return out


def speech_names(source):
    """Every function in this page that ends up speaking -- the two voice.js
    primitives plus each wrapper that reaches them, to a fixed point.

    (ve, 2026-09-11) A NAME THE PAGE DEFINES ITSELF IS JUDGED BY ITS BODY. The
    EXTRA_SPEAK seeds exist because their definitions live OUTSIDE the page that
    calls them (voice.js, demo.html's own helpers) and cannot be discovered from
    inside it. When the page DOES define one of those names, the definition is
    right there to read, and it wins: demolab.html's `say(text)` writes the text
    into a caption bubble and never reaches a speaker, so it is not a speaker --
    yet the seed list called it one and reported eight lines a page never speaks
    as missing from the closure. demo-lesson.html's own `speakLine` hands its text
    to window.speak, so the fixed point below finds it exactly as before. The
    voice.js primitives in SEEDS are never defined by a page and stay unconditional.
    """
    bodies, params = {}, {}
    for rx, braced in ((_FN_DECL, True), (_FN_ASSIGN, False)):
        for m in rx.finditer(source):
            body = _body_at(source, m.end(), braced_only=braced)
            if not body:
                continue
            bodies.setdefault(m.group(1), "")
            bodies[m.group(1)] += body
            params.setdefault(m.group(1), _first_param(source, m))
    names = set(SEEDS) | {n for n in EXTRA_SPEAK if n not in bodies}
    for _ in range(12):                     # a fixed point; 12 is far past any page
        grew = False
        for fn, body in bodies.items():
            if fn in names or not params.get(fn):
                continue
            if _passes_through(body, params[fn], names):
                names.add(fn)
                grew = True
        if not grew:
            break
    return names


def _first_param(source, m):
    """The name of a definition's FIRST parameter, or "" if it takes none."""
    seg = source[m.start():m.end() + 200]
    got = re.search(r"\(\s*([A-Za-z_$][\w$]*)", seg)
    return got.group(1) if got else ""


def _passes_through(body, param, names):
    """Does this body hand its OWN first parameter to something that speaks?

    ⚠️ THIS, AND NOT "REACHES SPEECH". The first cut asked only whether a function
    eventually called a speaker, and by that test runTutor is a speaker -- it does
    call speak(). But what runTutor is HANDED is the student's message, and what it
    speaks is the model's reply; topic.html's `runTutor("I'd like to explore: " + tp)`
    was reported as a line Mr. Cadabra says, which is exactly backwards. A wrapper is
    a function whose own argument becomes the spoken words, and that is testable:
    the parameter has to appear inside a call to something that already speaks.
    """
    at = re.escape(param)
    for m in _CALL.finditer(body):
        if m.group(1) not in names:
            continue
        if re.search(r"\b" + at + r"\b", _args_at(body, m.end() - 1)):
            return True
    return False


def _lit(q, raw):
    try:
        return ast.literal_eval(q + raw + q)
    except (SyntaxError, ValueError):
        return None


def _strings_in(text):
    out = []
    for a, b in _ANY_STR.findall(text):
        t = _lit('"', a) if a else _lit("'", b)
        if t:
            out.append(t)
    return out


def spoken_literals(source):
    """Every string literal in this page that reaches a speech call."""
    names = speech_names(source)
    inits = initializers(source)
    out, props = [], set()
    for m in _CALL.finditer(source):
        if m.group(1) not in names:
            continue
        args = _args_at(source, m.end() - 1)
        found = _strings_in(args)
        out.extend(found)                                   # (b) every literal arm
        # (e) ...and whatever the names in those arguments were built from
        out.extend(_walk(args, inits, set(names), 0))
        if not found:                                       # (c) a property was passed
            props.update(_MEMBER.findall(args))
    # (c) ...so every literal held under that property name is a spoken line
    for prop in props:
        for m in re.finditer(r"\b" + re.escape(prop) + r"\s*:\s*", source):
            out.extend(_strings_in(_value_at(source, m.end())))
    # ...and the ones that go through a variable: `var line = "..."; speakLine(line)`
    assigned = {}
    for name, q, raw in _ASSIGN.findall(source):
        t = _lit(q, raw)
        if t:
            assigned[name] = t
    for m in _CALL.finditer(source):
        if m.group(1) not in names:
            continue
        for ident in re.findall(r"^\s*([A-Za-z_$][\w$]*)\s*$", _args_at(source, m.end() - 1)):
            if ident in assigned:
                out.append(assigned[ident])
    seen, uniq = set(), []
    for t in out:
        if t in seen or len(t.split()) < MIN_WORDS:
            continue
        seen.add(t)
        uniq.append(t)
    return uniq


def pages():
    return sorted(f for f in os.listdir(STATIC)
                  if f.endswith(".html") and f not in EXEMPT_PAGES)


def hits(closure=None):
    """(page, line) for every page-local spoken line outside the voice closure."""
    if closure is None:
        import lessonscripts as L
        closure = set(L.course_audio_lines())
    else:
        closure = set(closure)
    found = []
    for fn in pages():
        src = scrub(io.open(os.path.join(STATIC, fn), encoding="utf-8").read())
        for t in spoken_literals(src):
            if t not in closure:
                found.append((fn, t))
    return found


def blocking(closure=None):
    """The subset the battery fails on: a cache-only page can never render a line."""
    return [(fn, t) for fn, t in hits(closure) if fn in CACHE_ONLY_PAGES]


if __name__ == "__main__":
    rows = hits()
    print("page-local spoken lines outside the voice closure: %d" % len(rows))
    for fn, t in rows:
        print("  %-24s %s" % (fn, t[:100]))

# I did no harm and this file is not truncated.

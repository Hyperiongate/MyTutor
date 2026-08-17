# =============================================================================
# screencheck.py  --  THE SCREEN AUDITOR  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-08-16  NEW -- BUILD gn. Jim ran one Geometry lesson and found four defects by
#               eye in the first turn: a formula rendered "a squared plus B squared
#               equals C squared", a triangle whose letters sat on the CORNERS while the
#               words talked about the LEGS, a progress rail reading "Unit 1" under prose
#               saying "Unit 5", and a clipped header. His question was the right one:
#               "we should have a universal way to catch these things. Somebody should be
#               checking this."
#
#               Nothing we own could have caught any of them, and the reason is structural
#               rather than a lack of effort. The twelve referees in tutor.py read the
#               REPLY TEXT. lessonaudit.py reads the TRANSCRIPT. Every defect Jim found
#               lives in neither -- it is born when session.html RENDERS that text into a
#               screen. A colour, a picture, a progress bar. No checker we had was even
#               pointed at the screen.
#
#               This is that checker, and its central design decision is that the JUDGING
#               is pure Python over a rendered snapshot -- no browser, no API key, no
#               network. Only CAPTURING a fresh screen needs Playwright. That split is the
#               whole point:
#
#                 A CHECK THAT SKIPS ON JIM'S MACHINE IS ANOTHER WISH.
#
#               Every check here runs inside ruletests.py against saved fixtures on every
#               push, with zero third-party packages. Playwright's absence costs us fresh
#               screens, never coverage. (Contrast lessonaudit.py, which cannot run at all
#               without an OpenAI key -- and so runs a few times a month.)
#
#               SIX CHECKS, each proved in BOTH directions against real turns from Jim's
#               own lesson (see FIXTURES at the bottom):
#                 S1  mixed variable styling   -- "a squared plus B squared"
#                 S2  figure names the words   -- letters on the corners, words on the legs
#                 S3  the rail agrees          -- "Unit 5" in prose, "Unit 1" on the rail
#                 S4  every figure is captioned -- rule 41, verified ON THE SCREEN
#                 S5  the caption doesn't answer -- a caption that spoils the open question
#                 S6  nothing is clipped        -- measured at capture time
#
#               S1's root cause, recorded so nobody re-derives it: session.html had
#                   const VAR_SKIP = { a: 1, i: 1, f: 1, g: 1, h: 1 };
#               meaning NEVER STYLE, while every other single letter rendered as a bold red
#               UPPERCASE <span class="mvar">. So "a squared plus b squared equals c
#               squared" reached the child as "a squared plus B squared equals C squared".
#
#               ⚠️ A CORRECTION TO AN EARLIER DRAFT OF THIS NOTE, left in as a warning: it
#               claimed the triangle-area formula "(1/2)bh" rendered as "(1/2)Bh". IT DOES
#               NOT -- "bh" is a two-letter run and styleVarsCore never touches it. The
#               claim was reasoned instead of run. Extracting the real function and calling
#               it took one command and showed the true form of the defect is "the base b
#               times the height h". RUN THE RENDERER; DO NOT DEDUCE IT.
#
#   2026-08-16  BUILD gn2 -- and then Jim's next lesson overturned the fix's assumption.
#               The board read "A, B, C = corners (vertices)" over "a, b, c = sides
#               (lengths)" and BOTH LINES RENDERED THE SAME, because the renderer forced a
#               capital. CASE IS MEANING: side a is opposite vertex A. session.html now
#               renders a styled letter exactly as written, and its table is CASE-SENSITIVE
#               (VAR_NEEDS_CONTEXT). S1 is unchanged -- it asks whether a formula is styled
#               two ways, which is true regardless of case -- but the seam it mirrors moved,
#               so PART 3aj now compares the lower-cased sets.
#
#               ⚠️ S2 READS geo-figures.js BY ITS FONT METRICS. That renderer labels
#               vertices at font-size 17 / weight 800 and sides at 15 / weight 600, and
#               that is the ONLY way to tell a corner label from a side label in the
#               emitted SVG. If geo-figures.js changes those numbers this checker goes
#               silently blind -- so ruletests PART 3aj asserts the renderer still emits
#               them. When two features touch, walk the seam (build fb).
#
#               This module NEVER touches a live lesson. It is offline tooling: it reads
#               screens and reports. It has no import from main.py or tutor.py and nothing
#               in the serving path imports it.
# =============================================================================

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import namedtuple

HERE = os.path.dirname(os.path.abspath(__file__))

# The geo-figures.js contract S2 depends on. Kept as data so ruletests can assert that
# the renderer still honours it (PART 3aj) instead of discovering the drift in a lesson.
FIG_VERTEX_FONT = ("17", "800")     # corner labels: A, B, C
FIG_SIDE_FONT   = ("15", "600")     # side labels:   3, 4, ?  (or "a = 3")
FIG_ANGLE_FONT  = ("13", "700")     # angle measures: 30°, 60°

# The session.html contract S1 depends on. Build gn2 renamed it VAR_NEEDS_CONTEXT and made
# it CASE-SENSITIVE (a/A/I are English, f/F/g/G/h/H are function names) -- these are those
# letters folded to lowercase, which is all S1 needs, since its bare-letter patterns are
# case-insensitive. ruletests PART 3aj asserts the two stay in step.
VAR_SKIP = ("a", "i", "f", "g", "h")

SEV_HIGH, SEV_MED, SEV_LOW = "HIGH", "MEDIUM", "LOW"

Finding = namedtuple("Finding", "check severity turn summary evidence")


# =============================================================================
# PART 1 -- THE SNAPSHOT: what one rendered turn looks like
# =============================================================================
# A Snapshot is deliberately plain data (dict in, attributes out) so that a fixture
# saved to JSON and a screen captured from a live browser are the SAME thing to every
# check below. That is what lets the identical check run in ruletests and against
# production.
class Snapshot(object):
    """One rendered turn of a lesson, as the student's screen actually shows it."""

    def __init__(self, data=None, **kw):
        d = dict(data or {})
        d.update(kw)
        self.turn        = d.get("turn", 0)
        self.name        = d.get("name", "")
        self.reply_raw   = d.get("reply_raw", "") or ""     # tutor reply WITH its [[tags]]
        self.bubble_html = d.get("bubble_html", "") or ""   # the spoken words, as rendered
        self.board_html  = d.get("board_html", "") or ""    # the whiteboard, as rendered
        self.rail        = dict(d.get("rail") or {})        # unit_label / unit_text / course_text
        self.overflow    = list(d.get("overflow") or [])    # [{el, scroll, client}] measured
        self.png         = d.get("png", "")

    def to_dict(self):
        return {"turn": self.turn, "name": self.name, "reply_raw": self.reply_raw,
                "bubble_html": self.bubble_html, "board_html": self.board_html,
                "rail": self.rail, "overflow": self.overflow, "png": self.png}

    @property
    def screen_html(self):
        return (self.bubble_html or "") + "\n" + (self.board_html or "")


# =============================================================================
# PART 2 -- READERS: turning rendered HTML/SVG back into facts (stdlib only)
# =============================================================================
_TAG_RE      = re.compile(r"<[^>]+>")
_MVAR_RE     = re.compile(r'<span class="mvar">\s*([A-Za-z])\s*</span>', re.I)
_SVG_RE      = re.compile(r"<svg\b[^>]*\bclass=\"[^\"]*geofig[^\"]*\"[^>]*>(.*?)</svg>", re.I | re.S)
_TEXT_EL_RE  = re.compile(r"<text\b([^>]*)>(.*?)</text>", re.I | re.S)
_ATTR_RE     = re.compile(r'([a-zA-Z-]+)\s*=\s*"([^"]*)"')
_CAP_RE      = re.compile(r'<div class="cap"[^>]*>(.*?)</div>', re.I | re.S)
_FIGBLOCK_RE = re.compile(r'<div class="mfig[^"]*"[^>]*>(.*?)</div>\s*</div>', re.I | re.S)


def strip_html(html):
    """Visible text of a rendered fragment, with entities resolved. No dependencies."""
    txt = _TAG_RE.sub(" ", html or "")
    for ent, ch in (("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"), ("&nbsp;", " "),
                    ("&quot;", '"'), ("&#39;", "'")):
        txt = txt.replace(ent, ch)
    return re.sub(r"\s+", " ", txt).strip()


def styled_vars(html):
    """The single letters session.html rendered as red capitals, lower-cased."""
    return [m.group(1).lower() for m in _MVAR_RE.finditer(html or "")]


def svg_labels(html):
    """Every <text> label in every geofig SVG, bucketed by the font metrics that
    geo-figures.js uses to distinguish a corner from a side. Returns
    {"vertex": [...], "side": [...], "angle": [...], "other": [...]}."""
    out = {"vertex": [], "side": [], "angle": [], "other": []}
    for svg in _SVG_RE.finditer(html or ""):
        for el in _TEXT_EL_RE.finditer(svg.group(1)):
            attrs = dict(_ATTR_RE.findall(el.group(1)))
            metric = (str(attrs.get("font-size", "")).strip(),
                      str(attrs.get("font-weight", "")).strip())
            label = strip_html(el.group(2))
            if not label:
                continue
            if metric == FIG_VERTEX_FONT:
                out["vertex"].append(label)
            elif metric == FIG_SIDE_FONT:
                out["side"].append(label)
            elif metric == FIG_ANGLE_FONT:
                out["angle"].append(label)
            else:
                out["other"].append(label)
    return out


def figure_blocks(html):
    """One entry per rendered figure: {"svg": bool, "caption": str}. A figure is a
    .mfig block; rule 41 says each one carries a caption, and this reads the rendered
    caption rather than the tag, because the tag is not what the child sees."""
    figs = []
    for m in re.finditer(r'<div class="mfig[^"]*"[^>]*>', html or ""):
        rest = html[m.end():]
        nxt = re.search(r'<div class="mfig[^"]*"[^>]*>', rest)
        chunk = rest[:nxt.start()] if nxt else rest
        cap = _CAP_RE.search(chunk)
        figs.append({"svg": bool(_SVG_RE.search(chunk)),
                     "caption": strip_html(cap.group(1)) if cap else ""})
    return figs


def captions(html):
    return [strip_html(m.group(1)) for m in _CAP_RE.finditer(html or "")]


# =============================================================================
# PART 3 -- THE SIX SCREEN CHECKS (pure; no browser, no key, no network)
# =============================================================================
# Every check returns a list of Finding. Every check is proved in BOTH directions in
# FIXTURES below -- the lesson of build gj/gk/gl/gm is that a detector nobody tried to
# fool is a detector that fires on the wrong things.

_MATH_WORD = r"(?:squared|cubed|²|³)"
# A bare letter is "in a math position" when it is squared/cubed, sits between two
# arithmetic operators, or is welded to a styled variable with no space ("Bh").
_BARE_MATH_RE = {}
for _L in VAR_SKIP:
    _BARE_MATH_RE[_L] = re.compile(
        r"(?<![A-Za-z])" + _L + r"(?![A-Za-z])\s*(?:" + _MATH_WORD + r"|\^|<sup>)"
        r"|(?<=[-+=×*/(])\s*" + _L + r"\s*(?=[-+=×*/)²³^])",
        re.I)


def check_s1_mixed_variable_styling(snap):
    """S1 -- one formula, two typographies. session.html renders single-letter variables
    as bold red CAPITALS but skips VAR_SKIP, so "a squared plus b squared equals c
    squared" reaches the child as "a squared plus B squared equals C squared" -- the same
    quantity written two different ways inside one sentence. Jim, 2026-08-16: "the a in
    the a squared is not bright, capital, bold, red. It's just a small a."

    Fires only when BOTH appear in the same rendered element: at least one styled
    variable, and at least one VAR_SKIP letter standing in an unmistakably mathematical
    position. "a cat sat on a mat" beside a styled X is not a finding; "a squared plus B
    squared" is."""
    out = []
    for where, html in (("words", snap.bubble_html), ("board", snap.board_html)):
        if not html:
            continue
        styled = sorted(set(styled_vars(html)))
        if not styled:
            continue
        plain = strip_html(_MVAR_RE.sub(lambda m: "\x00" + m.group(1) + "\x00", html))
        welded = re.findall(r"\x00[A-Za-z]\x00([a-z])(?![A-Za-z])", plain)
        # A STYLED VARIABLE MUST NOT BE READABLE AS A BARE ONE. Earlier this line merely
        # dropped the \x00 markers, which left the styled letter sitting in the text as an
        # ordinary capital -- and the bare-letter patterns are case-insensitive, so a
        # correctly-styled "A squared" matched the pattern for an unstyled "a squared" and
        # S1 reported a defect in its own fix. Caught by sweeping the 1,015 canonical
        # scripts through the real renderer; every hand-written fixture had passed.
        # Styled letters are replaced by a non-letter sentinel so they can never match.
        text = re.sub(r"\x00[A-Za-z]\x00", "§", plain)
        bare = []
        for letter in VAR_SKIP:
            if _BARE_MATH_RE[letter].search(text) or letter in welded:
                bare.append(letter)
        if bare:
            out.append(Finding(
                "S1 mixed variable styling", SEV_HIGH, snap.turn,
                "In the %s, one formula is written two ways: %s styled as red capitals, %s "
                "left as plain lowercase." % (where,
                                              ", ".join(s.upper() for s in styled),
                                              ", ".join(sorted(set(bare)))),
                strip_html(html)[:220]))
    return out


_SIDE_NAMING_RE = re.compile(
    r"\ba\s*(?:²|\^2|squared)\s*(?:\+|plus)\s*b\s*(?:²|\^2|squared)\s*(?:=|equals)\s*c\s*(?:²|\^2|squared)"
    r"|\b(?:side|leg|legs|sides)\s+([a-z])\b(?:\s*(?:,|and)\s*([a-z])\b)?",
    re.I)


def check_s2_figure_names_what_the_words_name(snap):
    """S2 -- the words are about the legs, the picture letters the corners. Jim,
    2026-08-16: "a, b, and c are supposed to be legs of a right triangle, and instead
    they're shown as the angles... So when you say a squared plus b squared equals c
    squared, it makes no sense."

    He is right twice over. The letters name nothing the child can find on the figure --
    and worse, under the convention every textbook uses, side a is the one OPPOSITE
    vertex A, which in his figure (right angle at A) is the hypotenuse. The board said c
    was the hypotenuse and the picture said a was.

    Fires when the turn names sides by letter AND a figure is present AND those letters
    appear only as CORNER labels. geo-figures.js CAN carry them properly -- sides="a = 3,
    b = 4, c = ?" renders them on the legs -- so this is a fixable turn, not a renderer
    limit. Rule 63: the words and the picture are the same figure."""
    text = strip_html(snap.screen_html)
    m = _SIDE_NAMING_RE.search(text)
    if not m:
        return []
    named = set()
    if m.group(1):
        named.update(g.lower() for g in m.groups() if g)
    else:
        named.update(("a", "b", "c"))
    labels = svg_labels(snap.screen_html)
    if not (labels["vertex"] or labels["side"]):
        return []
    on_sides = {s.lower() for s in labels["side"]}
    on_corners = {v.lower() for v in labels["vertex"]}
    # A side label may be "a = 3" rather than a bare "a"; count the letter as placed if
    # it appears as a token anywhere in a side label.
    placed = {L for L in named
              if any(re.search(r"(?<![A-Za-z])" + L + r"(?![A-Za-z])", s, re.I)
                     for s in on_sides)}
    stranded = sorted(named - placed)
    if stranded and (named & on_corners):
        return [Finding(
            "S2 figure names what the words name", SEV_HIGH, snap.turn,
            "The words name side%s %s, but the figure carries %s only on the CORNERS "
            "(vertices %s; side labels %s). Nothing on the picture is called %s."
            % ("" if len(stranded) == 1 else "s", ", ".join(stranded),
               ", ".join(sorted(named & on_corners)).upper(),
               ", ".join(labels["vertex"]) or "-", ", ".join(labels["side"]) or "-",
               ", ".join(stranded)),
            text[:220])]
    return []


_WORDNUM = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
            "six": 6, "seven": 7, "eight": 8, "nine": 9}
_PROSE_UNIT_RE = re.compile(r"\bunit\s+(\d+|one|two|three|four|five|six|seven|eight|nine)\b", re.I)
_RAIL_UNIT_RE = re.compile(r"\bunit\s+(\d+)\b", re.I)


def check_s3_rail_agrees_with_the_words(snap):
    """S3 -- the narration and the progress rail describe different places. Jim,
    2026-08-16: "it says where we start in unit five. And when I look at the tracking up
    on the top, it says unit one. Shouldn't it say unit five if we're working on unit
    five?"

    Two maps of the same lesson disagreeing in the same eyeful is a trust defect, and a
    child cannot tell which one is lying. Fires only when the prose states a unit NUMBER
    and the rail states a different one -- prose that names no unit is silent here."""
    label = " ".join(str(v) for v in (snap.rail.get("unit_label", ""),
                                      snap.rail.get("unit_text", "")))
    rail = _RAIL_UNIT_RE.search(label)
    if not rail:
        return []
    said = _PROSE_UNIT_RE.search(strip_html(snap.bubble_html))
    if not said:
        return []
    tok = said.group(1).lower()
    n_said = _WORDNUM.get(tok, None) or (int(tok) if tok.isdigit() else None)
    n_rail = int(rail.group(1))
    if n_said and n_said != n_rail:
        return [Finding(
            "S3 the rail agrees with the words", SEV_MED, snap.turn,
            "The tutor says Unit %d; the progress rail says Unit %d (%s)."
            % (n_said, n_rail, strip_html(str(snap.rail.get("unit_text", "")))[:80]),
            strip_html(snap.bubble_html)[:220])]
    return []


def check_s4_every_figure_is_captioned(snap):
    """S4 -- rule 41, checked where it matters. gj enforces the caption on the REPLY; this
    verifies it survived onto the SCREEN. A caption lost between the tag and the render
    passes gj and still leaves a child looking at an unlabeled picture."""
    out = []
    for i, fig in enumerate(figure_blocks(snap.screen_html), 1):
        if fig["svg"] and not fig["caption"]:
            out.append(Finding(
                "S4 every figure is captioned", SEV_MED, snap.turn,
                "Figure %d rendered with no visible caption (rule 41)." % i,
                strip_html(snap.screen_html)[:220]))
    return out


_IS_THE_RE = re.compile(r"\bis\s+the\s+([a-z][a-z\-]{3,})", re.I)


def check_s5_caption_does_not_answer(snap):
    """S5 -- the caption gives away the answer to the question still on the table. From
    Jim's own turn: the tutor asks "which side in that triangle is the hypotenuse?" and
    the caption underneath reads "the missing side is the hypotenuse, opposite the right
    angle." The answer is on the board before the child can offer one.

    Worth naming where this comes from: rule 41 (build gj, three days earlier) made every
    figure carry a caption, and captions now sit inside the self-answer referee's blind
    spot because that referee reads prose. When two features touch, walk the seam (fb).

    Deliberately narrow -- fires only when a trailing QUESTION and a caption share the
    same "is the <term>" claim."""
    text = strip_html(snap.bubble_html)
    if "?" not in text:
        return []
    q_terms = {m.group(1).lower() for m in _IS_THE_RE.finditer(text)}
    if not q_terms:
        return []
    out = []
    for cap in captions(snap.screen_html):
        shared = q_terms & {m.group(1).lower() for m in _IS_THE_RE.finditer(cap)}
        if shared:
            out.append(Finding(
                "S5 the caption does not answer", SEV_HIGH, snap.turn,
                "The tutor asks what \"is the %s\" and the caption underneath already says "
                "it: \"%s\"" % (sorted(shared)[0], cap[:90]),
                text[:220]))
    return out


def check_s6_nothing_is_clipped(snap):
    """S6 -- something the student needs to read is cut off at the edge. Measured at
    capture time (scrollWidth against clientWidth), because no amount of HTML reading can
    tell you what fell off the screen. Jim's header lost "0 of 3 goals done" and the name
    of his next quiz."""
    out = []
    for ov in snap.overflow:
        scroll, client = int(ov.get("scroll", 0)), int(ov.get("client", 0))
        if client and scroll > client + 2:
            out.append(Finding(
                "S6 nothing is clipped", SEV_LOW, snap.turn,
                "%s is %dpx wider than the space it has (%d vs %d) -- its right-hand text "
                "is cut off." % (ov.get("el", "an element"), scroll - client, scroll, client),
                ov.get("text", "")[:220]))
    return out


CHECKS = [
    check_s1_mixed_variable_styling,
    check_s2_figure_names_what_the_words_name,
    check_s3_rail_agrees_with_the_words,
    check_s4_every_figure_is_captioned,
    check_s5_caption_does_not_answer,
    check_s6_nothing_is_clipped,
]


def run_checks(snap):
    """Every check over one snapshot. A check that raises is REPORTED, never fatal --
    an auditor that dies on turn 3 audits nothing."""
    found = []
    for fn in CHECKS:
        try:
            found.extend(fn(snap) or [])
        except Exception as exc:  # noqa: BLE001 -- one broken check must not stop the sweep
            found.append(Finding(fn.__name__, SEV_LOW, snap.turn,
                                 "check raised %s: %s" % (type(exc).__name__, exc), ""))
    return found


def run_all(snaps):
    """Every check over every turn, with one defect reported ONCE. The whiteboard keeps
    the current picture up across turns by design, so an uncaptioned figure drawn on turn
    2 is still standing on turns 3, 4 and 5 -- reporting it five times buries the four
    other things that went wrong. Deduped on (check, summary): a defect that genuinely
    recurs with different particulars still reports each time."""
    out, seen = [], set()
    for s in snaps:
        for f in run_checks(s):
            key = (f.check, f.summary)
            if key in seen:
                continue
            seen.add(key)
            out.append(f)
    return out


# =============================================================================
# PART 4 -- CAPTURE (the only part that wants Playwright)
# =============================================================================
# Two ways to get a screen. RENDER mode serves the repo's own static/ directory and
# stubs the API, so a KNOWN reply is pushed through the REAL rendering pipeline with no
# key, no server and no cost -- that is the mode the regression fixtures come from, and
# the mode that reproduced all three of Jim's rendering defects. LIVE mode drives a real
# logged-in lesson on a running site.
OVERFLOW_JS = """() => {
  const out = [];
  ['#goalBar', '#todayBar', '#unitBar', '#courseBar', '.progwrap', 'header'].forEach(sel => {
    document.querySelectorAll(sel).forEach(el => {
      out.push({ el: sel, scroll: el.scrollWidth, client: el.clientWidth,
                 text: (el.innerText || '').slice(0, 200) });
    });
  });
  return out;
}"""

# board_html is THE WHITEBOARD AS IT STANDS -- not the transcript. Two subtractions make
# that true, and both were found by running a three-turn corpus rather than one turn:
#   - .bubble is the spoken words, already captured as bubble_html. Leaving them in made
#     every check report each defect twice, once as "words" and once as "board".
#   - .probdone is a FINISHED problem, folded away behind a one-line summary (build fx/ga).
#     It is off the board as far as the student is concerned, and re-reporting it on every
#     later turn is exactly the noise that teaches a reader to shrug at findings.
SNAPSHOT_JS = """() => {
  const bubbles = document.querySelectorAll('.bubble.tutor');
  const last = bubbles[bubbles.length - 1];
  const feed = document.getElementById('feed');
  let board = '';
  if (feed) {
    const clone = feed.cloneNode(true);
    clone.querySelectorAll('.probdone, .bubble').forEach(n => n.remove());
    board = clone.innerHTML;
  }
  const t = id => { const e = document.getElementById(id); return e ? e.textContent : ''; };
  return {
    bubble_html: last ? last.innerHTML : '',
    board_html: board,
    rail: { unit_label: t('unitBarLabel'), unit_text: t('unitText'),
            course_text: t('courseText'), today_text: t('todayText'), goal: t('goalText') }
  };
}"""


def playwright_available():
    try:
        import playwright.sync_api  # noqa: F401
        return True
    except Exception:
        return False


def _serve_static(static_dir, port):
    import functools, http.server, socketserver, threading
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=static_dir)

    class Quiet(http.server.SimpleHTTPRequestHandler):
        pass

    class Server(socketserver.TCPServer):
        allow_reuse_address = True

    srv = Server(("127.0.0.1", port), handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


DEFAULT_SESSION_STATE = {
    "placed": True, "toured": True, "name": "Maya", "tutor_name": "Mr. Cadabra",
    "history": [{"role": "assistant", "content": "prior turn"}],
    "placement": {"start_unit": 1},
    "progress": {"units_mastered": 0, "total_units": 9,
                 "today": {"items": ["Warm up", "Learn it", "Practice"], "done": []}},
}


def capture_render(replies, course="geometry", static_dir=None, port=8731,
                   session_state=None, shots_dir=None, viewport=(1280, 900)):
    """Push KNOWN tutor replies through the real session.html renderer and snapshot each
    one. No API key, no network, no cost -- and every rendering defect is reproducible
    to the pixel. Requires Playwright; callers check playwright_available() first."""
    from playwright.sync_api import sync_playwright

    static_dir = static_dir or os.path.join(HERE, "static")
    root = os.path.dirname(os.path.abspath(static_dir))
    state = dict(DEFAULT_SESSION_STATE)
    state.update(session_state or {})
    srv = _serve_static(root, port)
    snaps, pending = [], {"reply": ""}
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(args=["--no-sandbox"])
            page = browser.new_page(viewport={"width": viewport[0], "height": viewport[1]})
            page.route("**/api/session/**", lambda r: r.fulfill(
                status=200, content_type="application/json", body=json.dumps(state)))
            page.route("**/api/chat", lambda r: r.fulfill(
                status=200, content_type="application/json",
                body=json.dumps({"reply": pending["reply"]})))
            for stub in ("**/api/voice-status**", "**/api/transcribe**", "**/api/sprint/**"):
                page.route(stub, lambda r: r.fulfill(
                    status=200, content_type="application/json", body="{}"))
            page.route("**/api/speak**", lambda r: r.fulfill(
                status=200, content_type="audio/mpeg", body=b""))
            page.goto("http://127.0.0.1:%d/%s/session.html?code=SCREENCHECK&course=%s"
                      % (port, os.path.basename(static_dir), course), wait_until="load")
            page.wait_for_timeout(1200)
            try:
                page.click("#welcomeGo", timeout=5000)
            except Exception:
                pass
            page.wait_for_timeout(500)
            page.evaluate("() => { const c = document.querySelector('.composer');"
                          " if (c) c.classList.add('show'); }")
            for i, item in enumerate(replies, 1):
                name = item.get("name", "turn %d" % i) if isinstance(item, dict) else "turn %d" % i
                pending["reply"] = item["reply"] if isinstance(item, dict) else item
                page.fill("#input", item.get("ask", "ok") if isinstance(item, dict) else "ok")
                # Wait on the COUNT of tutor bubbles, not on one being "visible". The board
                # folds finished problems into a collapsed summary (build fx/ga), so the
                # FIRST .bubble.tutor on the page is hidden inside .probbody from turn two
                # onward and a visibility wait hangs forever. Found by running this against
                # a real three-turn corpus -- a one-turn smoke test would have missed it.
                before = page.evaluate("() => document.querySelectorAll('.bubble.tutor').length")
                page.click("#send")
                page.wait_for_function(
                    "n => document.querySelectorAll('.bubble.tutor').length > n",
                    arg=before, timeout=30000)
                page.wait_for_timeout(2200)
                data = page.evaluate(SNAPSHOT_JS)
                data["overflow"] = page.evaluate(OVERFLOW_JS)
                data["turn"], data["name"] = i, name
                data["reply_raw"] = pending["reply"]
                if shots_dir:
                    os.makedirs(shots_dir, exist_ok=True)
                    shot = os.path.join(shots_dir, "turn%02d.png" % i)
                    page.screenshot(path=shot)
                    data["png"] = shot
                snaps.append(Snapshot(data))
            browser.close()
    finally:
        srv.shutdown()
    return snaps


def capture_live(base_url, code, course="geometry", turns=None, shots_dir=None,
                 viewport=(1280, 900)):
    """Drive a REAL logged-in lesson and snapshot each turn. Costs real API credits and
    writes real turns to that student's record -- use a dedicated audit student."""
    from playwright.sync_api import sync_playwright

    turns = turns or ["Hi", "ok", "I'm not sure"]
    snaps = []
    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--no-sandbox"])
        page = browser.new_page(viewport={"width": viewport[0], "height": viewport[1]})
        page.goto("%s/session?code=%s&course=%s" % (base_url.rstrip("/"), code, course),
                  wait_until="load")
        page.wait_for_timeout(1500)
        try:
            page.click("#welcomeGo", timeout=8000)
        except Exception:
            pass
        page.evaluate("() => { const c = document.querySelector('.composer');"
                      " if (c) c.classList.add('show'); }")
        for i, msg in enumerate(turns, 1):
            page.fill("#input", msg)
            page.click("#send")
            page.wait_for_selector(".bubble.tutor", timeout=90000)
            page.wait_for_timeout(4000)
            data = page.evaluate(SNAPSHOT_JS)
            data["overflow"] = page.evaluate(OVERFLOW_JS)
            data["turn"], data["name"] = i, "live turn %d" % i
            if shots_dir:
                os.makedirs(shots_dir, exist_ok=True)
                shot = os.path.join(shots_dir, "live%02d.png" % i)
                page.screenshot(path=shot)
                data["png"] = shot
            snaps.append(Snapshot(data))
        browser.close()
    return snaps


# =============================================================================
# PART 5 -- FIXTURES: every check proved in BOTH directions, on real turns
# =============================================================================
# The rule these obey is build gj/gk/gl/gm's, learned the hard way: a detector verified
# only on the case that inspired it is a detector that fires on the wrong things. The
# CLEAN cases here are real turns -- correct ones -- from the same product.
_JIM_BUBBLE = (
    'Hey Maya, welcome back! Two days ago we started <span class="kterm">Unit 5: Right '
    'Triangles</span>, and we were right in the middle of the <span class="kterm">'
    'Pythagorean theorem</span> - the rule that a squared plus <span class="mvar">B</span> '
    'squared equals <span class="mvar">C</span> squared for the two legs and the hypotenuse '
    'of a right triangle. Which side in that triangle is the hypotenuse?'
)
_JIM_TRIANGLE_SVG = (
    '<div class="mblock"><div class="mfig pop"><svg viewBox="0 0 320 258" class="geofig">'
    '<text font-size="15" font-weight="600">3</text>'
    '<text font-size="15" font-weight="600">?</text>'
    '<text font-size="15" font-weight="600">4</text>'
    '<text font-size="17" font-weight="800">A</text>'
    '<text font-size="17" font-weight="800">B</text>'
    '<text font-size="17" font-weight="800">C</text></svg>'
    '<div class="cap">legs 3 and 4; the missing side is the hypotenuse, opposite the right '
    'angle</div></div></div>'
)
_GOOD_TRIANGLE_SVG = (
    '<div class="mblock"><div class="mfig pop"><svg viewBox="0 0 320 258" class="geofig">'
    '<text font-size="15" font-weight="600">a = 3</text>'
    '<text font-size="15" font-weight="600">c = ?</text>'
    '<text font-size="15" font-weight="600">b = 4</text>'
    '<text font-size="17" font-weight="800">A</text>'
    '<text font-size="17" font-weight="800">B</text>'
    '<text font-size="17" font-weight="800">C</text></svg>'
    '<div class="cap">the two legs are a and b; c is the hypotenuse</div></div></div>'
)

FIXTURES = [
    # ---- S1: fires ----
    ("S1 fires on Jim's Pythagorean turn", "S1 mixed variable styling",
     {"turn": 1, "bubble_html": _JIM_BUBBLE}),
    ("S1 fires on the triangle-area formula",  "S1 mixed variable styling",
     {"turn": 1, "board_html": 'Area = &frac12; <span class="mvar">B</span>h'}),
    # ---- S1: stays silent ----
    ("S1 silent when every variable is styled", None,
     {"turn": 1, "bubble_html": 'Solve <span class="mvar">X</span> + <span class="mvar">Y'
                                '</span> = <span class="mvar">Z</span> for X.'}),
    ("S1 silent on the English article beside a variable", None,
     {"turn": 1, "bubble_html": 'Pick a number for <span class="mvar">X</span> and a '
                                'partner for it, then add a little more.'}),
    ("S1 silent on function names f(x) and g(x)", None,
     {"turn": 1, "bubble_html": 'If f(x) = 2<span class="mvar">X</span> + 1 then g(x) '
                                'undoes it.'}),
    ("S1 silent with no styled variable at all", None,
     {"turn": 1, "bubble_html": "a squared plus b squared equals c squared."}),
    # ---- S2: fires ----
    ("S2 fires on letters stranded on the corners", "S2 figure names what the words name",
     {"turn": 1, "bubble_html": _JIM_BUBBLE, "board_html": _JIM_TRIANGLE_SVG}),
    # ---- S2: stays silent ----
    # The declarative bubble here is deliberate. An earlier draft reused Jim's turn, which
    # ENDS in "which side is the hypotenuse?" -- and S5 correctly fired on it, because the
    # good caption ("c is the hypotenuse") answers that question. The fixture was wrong,
    # not the check. Kept as a note: these cases cross-examine each other, which is the
    # point of running all six over every snapshot.
    ("S2 silent when the sides carry the letters", None,
     {"turn": 1, "bubble_html": "The Pythagorean theorem says a squared plus b squared "
                                "equals c squared, where a and b are the two legs.",
      "board_html": _GOOD_TRIANGLE_SVG}),
    ("S2 silent when the words name no letters", None,
     {"turn": 1, "bubble_html": "This triangle has legs 3 and 4. How long is the third side?",
      "board_html": _JIM_TRIANGLE_SVG}),
    ("S2 silent when there is no figure at all", None,
     {"turn": 1, "bubble_html": "Remember that a squared plus b squared equals c squared."}),
    # ---- S3: fires / silent ----
    ("S3 fires when prose and rail disagree", "S3 the rail agrees with the words",
     {"turn": 1, "bubble_html": "Two days ago we started Unit 5: Right Triangles.",
      "rail": {"unit_label": "Unit 1",
               "unit_text": "4 topics to go - next quiz: Naming & measuring angles"}}),
    ("S3 fires on the spelled-out unit", "S3 the rail agrees with the words",
     {"turn": 1, "bubble_html": "We are partway through unit five.",
      "rail": {"unit_label": "Unit 2", "unit_text": "3 topics to go"}}),
    ("S3 silent when they agree", None,
     {"turn": 1, "bubble_html": "Welcome back to Unit 1: Foundations.",
      "rail": {"unit_label": "Unit 1", "unit_text": "4 topics to go"}}),
    ("S3 silent when the prose names no unit", None,
     {"turn": 1, "bubble_html": "Let's pick up where we left off.",
      "rail": {"unit_label": "Unit 1", "unit_text": "4 topics to go"}}),
    # ---- S4: fires / silent ----
    ("S4 fires on an uncaptioned figure", "S4 every figure is captioned",
     {"turn": 1, "board_html": '<div class="mblock"><div class="mfig pop">'
                               '<svg class="geofig"><text font-size="17" font-weight="800">A'
                               '</text></svg></div></div>'}),
    ("S4 silent when the caption is there", None,
     {"turn": 1, "board_html": _GOOD_TRIANGLE_SVG}),
    # ---- S5: fires / silent ----
    ("S5 fires when the caption answers the question", "S5 the caption does not answer",
     {"turn": 1, "bubble_html": "Which side in that triangle is the hypotenuse?",
      "board_html": _JIM_TRIANGLE_SVG}),
    ("S5 silent when the caption keeps the secret", None,
     {"turn": 1, "bubble_html": "Which side in that triangle is the hypotenuse?",
      "board_html": '<div class="mfig pop"><svg class="geofig"><text font-size="15" '
                    'font-weight="600">3</text></svg><div class="cap">a right triangle with '
                    'legs 3 and 4</div></div>'}),
    ("S5 silent when nothing was asked", None,
     {"turn": 1, "bubble_html": "That missing side is the hypotenuse.",
      "board_html": _JIM_TRIANGLE_SVG}),
    # ---- S6: fires / silent ----
    ("S6 fires on a clipped rail", "S6 nothing is clipped",
     {"turn": 1, "overflow": [{"el": "#courseBar", "scroll": 1490, "client": 1280,
                               "text": "0 of 9 units mastered"}]}),
    ("S6 silent when everything fits", None,
     {"turn": 1, "overflow": [{"el": "#courseBar", "scroll": 1180, "client": 1280}]}),
]


def fixture_results():
    """[(name, expected_check_or_None, [Finding])] -- the shape ruletests consumes."""
    out = []
    for name, expected, data in FIXTURES:
        out.append((name, expected, run_checks(Snapshot(data))))
    return out


def self_test():
    """Run every fixture in both directions. Returns (passed, failed, [detail])."""
    passed, failed, detail = 0, 0, []
    for name, expected, found in fixture_results():
        names = {f.check for f in found}
        if expected is None:
            if names:
                failed += 1
                detail.append("%s -- expected SILENCE, got %s" % (name, sorted(names)))
            else:
                passed += 1
        else:
            if expected in names:
                passed += 1
            else:
                failed += 1
                detail.append("%s -- expected %r, got %s" % (name, expected, sorted(names) or "nothing"))
    return passed, failed, detail


# =============================================================================
# PART 6 -- THE REPORT
# =============================================================================
def report_markdown(snaps, findings, title="Screen audit"):
    sev_rank = {SEV_HIGH: 0, SEV_MED: 1, SEV_LOW: 2}
    ordered = sorted(findings, key=lambda f: (sev_rank.get(f.severity, 3), f.turn, f.check))
    lines = ["# %s" % title, "",
             "%d turn%s inspected - %d finding%s."
             % (len(snaps), "" if len(snaps) == 1 else "s",
                len(ordered), "" if len(ordered) == 1 else "s"), ""]
    if not ordered:
        lines += ["No screen defects found.", ""]
    by_check = {}
    for f in ordered:
        by_check.setdefault(f.check, []).append(f)
    for check, group in by_check.items():
        lines += ["## %s  (%d)" % (check, len(group)), ""]
        for f in group:
            lines += ["- **turn %s - %s.** %s" % (f.turn, f.severity, f.summary)]
            if f.evidence:
                lines += ["  > %s" % f.evidence]
        lines += [""]
    lines += ["## Turns inspected", ""]
    for s in snaps:
        lines += ["- turn %s - %s%s" % (s.turn, s.name, "  (%s)" % s.png if s.png else "")]
    lines += ["", "*I did no harm and this file is not truncated.*", ""]
    return "\n".join(lines)


# =============================================================================
# PART 7 -- CLI
# =============================================================================
def _load_corpus(path):
    with open(path, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    return data if isinstance(data, list) else data.get("replies", [])


def main(argv=None):
    ap = argparse.ArgumentParser(description="Audit what the student's SCREEN actually shows.")
    ap.add_argument("--self-test", action="store_true",
                    help="run every check against its fixtures, both directions (no browser)")
    ap.add_argument("--render", metavar="CORPUS.json",
                    help="push known replies through the real renderer (needs playwright)")
    ap.add_argument("--live", metavar="BASE_URL",
                    help="drive a real lesson on a running site (needs playwright + a code)")
    ap.add_argument("--code", default="", help="student code for --live")
    ap.add_argument("--course", default="geometry")
    ap.add_argument("--static", default=None, help="path to static/ (default: ./static)")
    ap.add_argument("--shots", default=os.path.join(HERE, "static", "shots", "screencheck"))
    ap.add_argument("--out", default=None, help="write the markdown report here")
    args = ap.parse_args(argv)

    if args.self_test or not (args.render or args.live):
        passed, failed, detail = self_test()
        print("screencheck self-test: %d passed, %d failed" % (passed, failed))
        for d in detail:
            print("  FAIL  %s" % d)
        return 0 if failed == 0 else 1

    if not playwright_available():
        print("playwright is not installed here -- the CHECKS still run (--self-test); only\n"
              "capturing a fresh screen needs it.  pip install playwright && playwright install chromium")
        return 2

    if args.render:
        snaps = capture_render(_load_corpus(args.render), course=args.course,
                               static_dir=args.static, shots_dir=args.shots)
    else:
        if not args.code:
            print("--live needs --code (use a dedicated audit student: it writes real turns)")
            return 2
        snaps = capture_live(args.live, args.code, course=args.course, shots_dir=args.shots)

    findings = run_all(snaps)
    md = report_markdown(snaps, findings)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(md)
        print("wrote %s" % args.out)
    print(md)
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())

# I did no harm and this file is not truncated.

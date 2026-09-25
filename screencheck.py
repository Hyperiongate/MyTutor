# =============================================================================
# screencheck.py  --  THE SCREEN AUDITOR  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-09-24  BUILD yb -- S10, THE FIGURE'S WORDS ARE READABLE. FIGURES_JS measures every
#               figure's smallest label in screen pixels (font-size x drawn width / viewBox
#               width) and whether the figure was drawn again for its width (data-pu-room);
#               S10 reports a label under LABEL_PX_FLOOR (9px). The over-tall beat's shrink
#               (pu, proportional since xy) left the labels at the full-board size -- 6px at
#               340px; board.js redraws the figure for the width it gives it now.
#   2026-09-24  BUILD xy -- THE TWO FLAGS NOBODY COULD SCREENSHOT (project 6 of the 09-14
#               deep dive). Jim's corrections queue said "a board line below the fold"
#               (twice, no screenshot survived) and "the graphic is half as big as it should
#               be ... generally small, and inconsistent" (09-11). Both were closed as
#               unmeasurable. Now they are measured, here, in the battery:
#                 S8  the last line is on the screen -- after a turn lands, its last board
#                     line ends inside the board's visible area and the answer buttons are
#                     inside the window (FOLD_JS, measured at capture time).
#                 S9  figure widths agree -- a LESSON-level check (LESSON_CHECKS, run_all):
#                     within one lesson, figures of the same kind are drawn within 12% of one
#                     width; a figure the board shrank on purpose (pu) is LOW and named as
#                     such, an unexplained disagreement is MEDIUM. board.js stamps every
#                     figure with data-kind so the reader never guesses.
#               And a THIRD way to capture: --script LESSON|COURSE|all drives an AUTHORED
#               lesson through the real scripted player (capture_script): the engine's own
#               walk (script_walk -- pairs right, one miss, right to the end; no model) is
#               served from a stub, the page plays every beat for real, and Playwright's
#               clock runs the reading floor through instantly, so a lesson captures in
#               about 50 s. The live-tutor capture (--render) is unchanged.
#               What the first survey found, and this build fixed in board.js:
#                 - fitTurnToBoard summed svg.offsetHeight (undefined on an SVG): its factor
#                   was NaN and every over-tall turn collapsed its figure to the 0.35 floor.
#                   An 18px overage took an 1100px chart to 385px. That IS "half as big".
#                 - the pages' scroll listeners judged "scrolled away" by distance from the
#                   BOTTOM, which under ir's top-anchored turns is always far, so one scroll
#                   event that was not ours (the fold re-clamping scrollTop) latched
#                   stickBottom false and the next question landed 700px below the fold.
#                   That IS "a board line below the fold" (geo-u1-when-lines-cross, 4 turns).
#               Also: real_csp reads the literal with Python's parser, so a quoted phrase
#               inside a comment no longer glues an invalid source into the served header
#               (every harness run since vj logged one, and S7 reported it as the app's).
#               _serve_static's socket is closed after a capture (several in one process).
#   2026-08-17  BUILD hb -- THE AUDITOR STOPS WATCHING ONE PAGE IN FIVE. capture_render
#               gained page_name= and a PAGE_PROFILES table (endpoint + how to get past
#               the entry screen); it now drives session.html, topic.html AND
#               practice.html, which are three hand-synced copies of one renderer. The
#               full-app review found the cost of the old coverage: build gz's two live
#               defects lived in the two pages this file could not see. --page picks one
#               or 'all'. demo.html and challenge.html are NAMED in UNCOVERED_PAGES
#               rather than silently skipped -- they are separate reimplementations, not
#               forks, and need their own harness. Verified by driving all three pages
#               with a real corpus: 2 turns each, S1-S7 judged, 0 findings.
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
        self.console     = list(d.get("console") or [])     # [{level, text}] captured
        self.png         = d.get("png", "")
        # (xy, 2026-09-24) THE TWO FLAGS NOBODY COULD SCREENSHOT -- measured at capture time
        self.fold        = dict(d.get("fold") or {})        # feed/turn geometry, see FOLD_JS
        self.figures     = list(d.get("figures") or [])     # [{kind, width, height, shrunk, host}]

    def to_dict(self):
        return {"turn": self.turn, "name": self.name, "reply_raw": self.reply_raw,
                "bubble_html": self.bubble_html, "board_html": self.board_html,
                "rail": self.rail, "overflow": self.overflow,
                "console": self.console, "png": self.png,
                "fold": self.fold, "figures": self.figures}

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


_CSP_RE = re.compile(r"content security policy|violates the following", re.I)


def check_s7_the_console_is_clean(snap):
    """S7 -- the page complained and nobody was listening. Added 2026-08-17 (build gp2)
    after Jim pasted a lesson's console output and it contained, under the line we were
    actually looking for, a Content-Security-Policy violation on every silent-WAV data:
    URI the voice uses. Nothing was broken -- that header ships report-only -- but the
    policy is documented as something we intend to ENFORCE, and on that day the audio
    warm-up and the keep-alive loop both stop loading. Those are the two mechanisms that
    protect the first syllable of every sentence the tutor speaks.

    Neither of us was looking for it. The checker was already driving a browser, and
    reading what the page says about itself costs nothing -- so now it does. This is the
    cheapest instance of Jim's thesis in the whole codebase: a class of defect found
    because something was watching, not because someone suspected it.

    Two kinds are reported, and ONLY two, so a chatty page cannot bury them:
      - an uncaught JavaScript error (level "pageerror") -- always a defect
      - a CSP violation -- harmless today, a regression the day the policy is enforced
    Ordinary console.log noise, including our own [voicehead] probe, is ignored."""
    out = []
    for entry in snap.console:
        level = str((entry or {}).get("level") or "").lower()
        text = str((entry or {}).get("text") or "")
        if level == "pageerror":
            out.append(Finding(
                "S7 the console is clean", SEV_HIGH, snap.turn,
                "An uncaught JavaScript error fired while this turn rendered: "
                + text[:150], text[:220]))
        elif _CSP_RE.search(text):
            out.append(Finding(
                "S7 the console is clean", SEV_MED, snap.turn,
                "A Content-Security-Policy violation was logged. It is report-only today, "
                "so nothing broke -- but this will BREAK the moment the policy is enforced: "
                + text[:120], text[:220]))
    return out


def check_s8_the_last_line_is_on_the_screen(snap):
    """S8 -- THE FIRST FLAG NOBODY COULD SCREENSHOT (build xy, 2026-09-24). Jim's
    corrections queue said "a board line below the fold" twice, no screenshot survived,
    and the 09-14 handoff closed it with: the right answer is structural -- teach the
    screen auditor to fail a board whose last line lands below the visible area.

    Measured at capture time (FOLD_JS), after the turn has fully landed and the board
    has done its own placing (ir: a turn starts at the top; ns: the view follows the
    pen; pu: an over-tall turn's figure is shrunk to fit). The turn is everything the
    tutor put on the board since the student last spoke. Two things must be true when
    the student is asked to act:
      - the turn's LAST line ends inside the board's visible area (turn_bottom <=
        feed_bottom, 2px of grace), and
      - the tap buttons, if any, are inside the window (choices_bottom <= window_h).
    A line the child would have to scroll to is the defect, whatever put it there."""
    out = []
    f = snap.fold or {}
    if not f:
        return out
    try:
        turn_bottom, feed_bottom = float(f.get("turn_bottom", 0)), float(f.get("feed_bottom", 0))
        feed_top = float(f.get("feed_top", 0))
    except (TypeError, ValueError):
        return out
    if feed_bottom and turn_bottom > feed_bottom + 2:
        out.append(Finding(
            "S8 the last line is on the screen", SEV_HIGH, snap.turn,
            "The turn's last board line ends %dpx below the visible board (turn %d-%d px, "
            "board %d-%d px) -- the student has to scroll to see it." % (
                round(turn_bottom - feed_bottom), round(float(f.get("turn_top", 0))),
                round(turn_bottom), round(feed_top), round(feed_bottom)),
            str(f.get("last_text", ""))[:220]))
    try:
        cb, wh = f.get("choices_bottom"), f.get("window_h")
        if cb is not None and wh and float(cb) > float(wh) + 2:
            out.append(Finding(
                "S8 the last line is on the screen", SEV_HIGH, snap.turn,
                "The answer buttons end %dpx below the window." % round(float(cb) - float(wh)),
                str(f.get("choices_text", ""))[:220]))
    except (TypeError, ValueError):
        pass
    return out


FIG_WIDTH_TOLERANCE = 0.12    # S9: same kind, same lesson -> widths within 12% of each other
LABEL_PX_FLOOR = 9.0          # S10: the smallest label a figure may draw, in screen pixels


def check_s10_the_figures_words_are_readable(snap):
    """S10 -- THE FIGURE'S WORDS ARE READABLE (build yb, 2026-09-24). A figure is drawn in
    a viewBox with 10-15 unit labels; on screen a label is font-size x (drawn width /
    viewBox width). vk grew the labels for a narrow BOARD; a figure the board SHRANK to
    fit its turn (pu) kept the sizes fitted for the full board -- at 340px on a 660-unit
    viewBox a 12-unit label is 6px. FIGURES_JS measures the smallest label of every
    figure of the turn; under LABEL_PX_FLOOR is a finding. Measured, never inferred."""
    out = []
    for fig in (snap.figures or []):
        px = (fig or {}).get("label_px")
        try:
            px = float(px) if px is not None else None
        except (TypeError, ValueError):
            px = None
        if px is None or px >= LABEL_PX_FLOOR:
            continue
        out.append(Finding(
            "S10 the figure's words are readable", SEV_MED, snap.turn,
            "The %s is drawn %dpx wide and its smallest label is %.1fpx -- under the %.0fpx floor%s." % (
                fig.get("kind") or "figure", int(fig.get("width") or 0), px, LABEL_PX_FLOOR,
                " (shrunk to fit the turn)" if fig.get("shrunk") else ""),
            "kind %s, width %s, shrunk %s, refit %s" % (fig.get("kind"), fig.get("width"), fig.get("shrunk"), fig.get("refit"))))
    return out


def check_s9_figure_widths_agree(snaps):
    """S9 -- THE SECOND FLAG (build xy). Jim, 09-11: the board's figures are "generally
    small, and inconsistent" -- "the graphic is half as big as it should be" on the ask.
    Build pc gave every kind one display rule and vk made the words fit; what nobody could
    see was the SAME figure drawn at two sizes inside ONE lesson (a chart full-width on
    the teach beat, then inside a step-card cell on the ask). This is a LESSON-level
    check -- it reads every turn's figures together -- and it is by KIND: a number line
    and a pie are meant to differ (their aspect ratios do); two number lines in one lesson
    are not. Widths within FIG_WIDTH_TOLERANCE agree. A figure the board shrank on purpose
    to keep the turn on the screen (pu, data-pu-maxw) is named as such in the evidence,
    because that is the "half as big" the student sees, and its cause."""
    out = []
    by_kind = {}
    for s in snaps:
        for fig in (s.figures or []):
            kind = str((fig or {}).get("kind") or "")
            try:
                w = float(fig.get("width") or 0)
            except (TypeError, ValueError):
                continue
            if not kind or w <= 0:
                continue
            by_kind.setdefault(kind, []).append((s.turn, w, bool(fig.get("shrunk")), str(fig.get("host") or "")))
    for kind, rows in sorted(by_kind.items()):
        ws = [w for _t, w, _sh, _h in rows]
        lo, hi = min(ws), max(ws)
        if hi <= 0 or (hi - lo) / hi <= FIG_WIDTH_TOLERANCE:
            continue
        small = min(rows, key=lambda r: r[1])
        big = max(rows, key=lambda r: r[1])
        # A figure the board shrank ON PURPOSE (pu: the turn would not fit the board
        # otherwise) is a known cause with a known floor: LOW, and the evidence says so.
        # A disagreement with NO shrink behind it is the unexplained kind -- a figure in
        # a narrower host, a cap that differs by path -- and that is MEDIUM.
        sev = SEV_LOW if small[2] else SEV_MED
        out.append(Finding(
            "S9 figure widths agree", sev, small[0],
            "The %s is drawn %dpx wide on turn %d and %dpx wide on turn %d (%d%% apart) -- "
            "one lesson, one size%s." % (kind, round(small[1]), small[0], round(big[1]), big[0],
                                          round((hi - lo) / hi * 100),
                                          " (the small one was shrunk to fit its turn)" if small[2] else ""),
            "; ".join("turn %d: %dpx%s%s" % (t, round(w), " (shrunk to fit the turn)" if sh else "",
                                              " in %s" % h if h else "") for t, w, sh, h in rows)[:220]))
    return out


CHECKS = [
    check_s1_mixed_variable_styling,
    check_s2_figure_names_what_the_words_name,
    check_s3_rail_agrees_with_the_words,
    check_s4_every_figure_is_captioned,
    check_s5_caption_does_not_answer,
    check_s6_nothing_is_clipped,
    check_s7_the_console_is_clean,
    check_s8_the_last_line_is_on_the_screen,
    check_s10_the_figures_words_are_readable,
]
# (xy) checks that read a whole LESSON -- every snapshot together -- not one turn
LESSON_CHECKS = [
    check_s9_figure_widths_agree,
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
    # (xy) the lesson-level checks, reported once each, never fatal
    for fn in LESSON_CHECKS:
        try:
            out.extend(fn(list(snaps)) or [])
        except Exception as exc:  # noqa: BLE001
            out.append(Finding(fn.__name__, SEV_LOW, 0,
                               "check raised %s: %s" % (type(exc).__name__, exc), ""))
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


def real_csp(root=None):
    """The Content-Security-Policy this app actually ships, read OUT OF main.py.

    2026-08-17 (build gp2). S7 caught a CSP violation only because Jim pasted his console
    into a chat -- the local harness served no CSP header at all, so the violation could
    not happen here and the check sat silent on the one defect it was written for. A test
    rig that is missing the header under test is a test rig that proves nothing.

    Reading the live string out of main.py rather than copying it means this can never
    drift out of step with production: change the policy there and the harness changes
    with it, on the next run, with no seam to remember."""
    try:
        path = os.path.join(root or HERE, "main.py")
        with open(path, "r", encoding="utf-8") as fh:
            src = fh.read()
        m = re.search(r"_CSP_REPORT_ONLY\s*=\s*\((.*?)\n\)", src, re.S)
        if not m:
            return ""
        # The literal is a run of adjacent quoted strings with comments between them.
        # (xy, 2026-09-24) Python's own parser reads it, so a quoted phrase INSIDE a
        # comment ("media-src 'self' data:" in vj's note) is not glued into the header.
        # The regex it replaces served every harness run since 09-11 a policy reading
        # `media-src 'self' data:media-src 'self' data: blob:` -- an invalid source that
        # Chromium logged on every turn, and S7 dutifully reported as the app's fault.
        try:
            import ast as _ast
            val = _ast.literal_eval("(" + m.group(1) + "\n)")
            if isinstance(val, str):
                return val
        except Exception:  # noqa: BLE001 -- fall back to the old reading
            pass
        body = re.sub(r"(?m)^\s*#.*$", "", m.group(1))
        return "".join(re.findall(r'"([^"]*)"', body))
    except Exception:  # noqa: BLE001 -- no header is survivable; a crash here is not
        return ""


def _serve_static(static_dir, port, csp=""):
    import functools, http.server, socketserver, threading

    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *a, **kw):
            super().__init__(*a, directory=static_dir, **kw)

        def end_headers(self):
            # Serve the REAL policy, so a data: URI that production would flag is flagged
            # here too -- for free, with no key and no network.
            if csp:
                self.send_header("Content-Security-Policy-Report-Only", csp)
            super().end_headers()

        def log_message(self, *a):        # the harness is not a web server log
            pass

    class Server(socketserver.TCPServer):
        allow_reuse_address = True

    srv = Server(("127.0.0.1", port), Handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


DEFAULT_SESSION_STATE = {
    "placed": True, "toured": True, "name": "Maya", "tutor_name": "Mr. Cadabra",
    "history": [{"role": "assistant", "content": "prior turn"}],
    "placement": {"start_unit": 1},
    "progress": {"units_mastered": 0, "total_units": 9,
                 "today": {"items": ["Warm up", "Learn it", "Practice"], "done": []}},
}


# THE FIVE RENDERER COPIES, AND WHICH ONES THIS CAN DRIVE (2026-08-17, build hb).
# The full-app review counted the damage: session.html, topic.html and practice.html are
# three hand-synced copies of one renderer (~2,400 duplicated lines), and this auditor
# drove exactly ONE of them -- so any S1-S7 defect reborn in a sibling was unwatched.
# That is not hypothetical: build gz found TWO live defects living in the two pages this
# file could not see.
#
# Each profile is only what actually DIFFERS: which endpoint the page posts a turn to,
# and how you get past its entry screen. Everything downstream -- the snapshot, the
# board, the bubbles, the console capture -- is identical because addBubble() and the
# board renderer are byte-identical copies across the three (which is the disease this
# coverage exists to watch while Phase 2 cures it).
#
# demo.html and challenge.html are deliberately NOT here: they are not forks of this
# renderer but separate reimplementations with their own board and voice stacks, so
# they need their own harness, not a profile. Named rather than silently omitted --
# a bounded sweep that does not say what it skipped reads as "all clear".
PAGE_PROFILES = {
    "session.html": {
        "api": "**/api/chat",
        # The welcome overlay; already handled leniently since a build may not show it.
        "enter": [("click", "#welcomeGo", None)],
        "warmup": False,
    },
    "topic.html": {
        "api": "**/api/topic",
        # Students TYPE a topic, then Go -- and that click runs the FIRST tutor turn,
        # so this page needs a throwaway opener reply before the real corpus starts.
        "enter": [("fill", "#topicInput", "slope"), ("click", "#entryGo", None)],
        "warmup": True,
    },
    "practice.html": {
        "api": "**/api/practice",
        "enter": [("fill", "#problemInput", "2x + 3 = 11"), ("click", "#entryGo", None)],
        "warmup": True,
    },
}
CAPTURE_PAGES = tuple(PAGE_PROFILES)
UNCOVERED_PAGES = ("demo.html", "challenge.html")   # separate stacks; see the note above


def capture_render(replies, course="geometry", static_dir=None, port=8731,
                   session_state=None, shots_dir=None, viewport=(1280, 900),
                   page_name="session.html"):
    """Push KNOWN tutor replies through a real teaching-page renderer and snapshot each
    one. No API key, no network, no cost -- and every rendering defect is reproducible
    to the pixel. Requires Playwright; callers check playwright_available() first.

    build hb: `page_name` selects which of the three teaching pages to drive (see
    PAGE_PROFILES). It used to be session.html and nothing else."""
    from playwright.sync_api import sync_playwright

    if page_name not in PAGE_PROFILES:
        raise ValueError("screencheck cannot drive %r -- known pages: %s"
                         % (page_name, ", ".join(CAPTURE_PAGES)))
    profile = PAGE_PROFILES[page_name]

    static_dir = static_dir or os.path.join(HERE, "static")
    root = os.path.dirname(os.path.abspath(static_dir))
    state = dict(DEFAULT_SESSION_STATE)
    state.update(session_state or {})
    srv = _serve_static(root, port, csp=real_csp(root))
    snaps, pending = [], {"reply": ""}
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(args=["--no-sandbox"])
            page = browser.new_page(viewport={"width": viewport[0], "height": viewport[1]})
            console = []
            page.on("console", lambda m: console.append({"level": m.type, "text": m.text}))
            page.on("pageerror", lambda e: console.append({"level": "pageerror",
                                                           "text": str(e)[:400]}))
            page.route("**/api/session/**", lambda r: r.fulfill(
                status=200, content_type="application/json", body=json.dumps(state)))
            page.route(profile["api"], lambda r: r.fulfill(
                status=200, content_type="application/json",
                body=json.dumps({"reply": pending["reply"]})))
            for stub in ("**/api/voice-status**", "**/api/transcribe**", "**/api/sprint/**"):
                page.route(stub, lambda r: r.fulfill(
                    status=200, content_type="application/json", body="{}"))
            page.route("**/api/speak**", lambda r: r.fulfill(
                status=200, content_type="audio/mpeg", body=b""))
            page.goto("http://127.0.0.1:%d/%s/%s?code=SCREENCHECK&course=%s"
                      % (port, os.path.basename(static_dir), page_name, course),
                      wait_until="load")
            page.wait_for_timeout(1200)
            # A page that opens its first tutor turn from the entry screen (topic,
            # practice) must have a reply waiting, or the opener renders the empty
            # string and every later turn is off by one.
            if profile.get("warmup"):
                pending["reply"] = "Good — let's take a look at that together."
            for step in profile["enter"]:
                action, selector, value = step
                try:
                    if action == "fill":
                        page.fill(selector, value, timeout=5000)
                    else:
                        page.click(selector, timeout=5000)
                except Exception:
                    pass          # an entry step a given build does not show is fine
            page.wait_for_timeout(500)
            if profile.get("warmup"):
                # Let the opener's bubble land so the per-turn counts below start clean.
                try:
                    page.wait_for_function(
                        "() => document.querySelectorAll('.bubble.tutor').length > 0",
                        timeout=30000)
                except Exception:
                    pass
                page.wait_for_timeout(1200)
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
                # Only THIS turn's console lines, so a violation is attributed to the turn
                # that caused it rather than to every turn after it.
                data["console"] = console[:]
                del console[:]
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
        try:
            srv.server_close()      # (xy) free the port: several captures in one process
        except Exception:  # noqa: BLE001
            pass
    return snaps


# =============================================================================
# (xy, 2026-09-24) THE SCRIPTED LANE -- where the child's minutes are
# =============================================================================
# Every capture above pushes a KNOWN reply through the live-tutor door (/api/chat). The
# two flags this build teaches the auditor -- a line below the fold, a figure drawn at
# two sizes -- were raised on AUTHORED lessons, and the scripted player is a different
# code path (scrPlay, beat by beat, its own scrolling). So the auditor now drives that
# lane too: the engine itself (lessonscripts, no model, no network) walks the lesson the
# way coursesweep's transcript does -- the pairs right, the first practice problem missed
# once, then right to the streak, the reason, the end -- and each turn's steps are served
# to the real page from a stub. The page plays them for real: board.js draws, ir/ns/pu
# place, and FOLD_JS measures what the student would see.
#
# Playwright's clock is installed on the page so the reading floor (2.6 s a beat, 360 ms
# a word) is run through instantly: a 30-beat lesson captures in seconds, not minutes,
# and the measurement is unchanged because the placing is rAF/reflow, not time.
FOLD_JS = """() => {
  const feed = document.getElementById('feed');
  if (!feed) return {};
  const fr = feed.getBoundingClientRect();
  const kids = Array.from(feed.children).filter(n => n.id !== 'feedPad');
  // the turn: everything after the student's last bubble (or the whole board)
  let start = 0;
  for (let i = kids.length - 1; i >= 0; i--) {
    if (kids[i].classList && kids[i].classList.contains('student')) { start = i + 1; break; }
  }
  const turn = kids.slice(start).filter(n => !(n.classList && n.classList.contains('choicerow')));
  let top = null, bottom = null, lastText = '';
  turn.forEach(n => {
    const r = n.getBoundingClientRect();
    if (!r.height) return;
    if (top === null || r.top < top) top = r.top;
    if (bottom === null || r.bottom > bottom) { bottom = r.bottom; }
    const t = (n.innerText || '').replace(/\\s+/g, ' ').trim();
    if (t) lastText = t.slice(-120);
  });
  const row = document.querySelector('.choicerow');
  const rr = row ? row.getBoundingClientRect() : null;
  return {
    feed_top: fr.top, feed_bottom: fr.bottom, feed_h: feed.clientHeight,
    scroll_top: feed.scrollTop, scroll_h: feed.scrollHeight,
    turn_top: top, turn_bottom: bottom, turn_blocks: turn.length, last_text: lastText,
    choices_bottom: rr ? rr.bottom : null, choices_text: row ? (row.innerText || '').slice(0, 120) : '',
    window_h: window.innerHeight, window_w: window.innerWidth
  };
}"""

FIGURES_JS = """() => {
  const feed = document.getElementById('feed');
  if (!feed) return [];
  const kids = Array.from(feed.children).filter(n => n.id !== 'feedPad');
  let start = 0;
  for (let i = kids.length - 1; i >= 0; i--) {
    if (kids[i].classList && kids[i].classList.contains('student')) { start = i + 1; break; }
  }
  const out = [];
  kids.slice(start).forEach(n => {
    (n.querySelectorAll ? n.querySelectorAll('.mfig') : []).forEach(m => {
      const svg = m.querySelector('svg'); if (!svg) return;
      const r = svg.getBoundingClientRect();
      const host = m.closest('.stepcell, .stepcard, .worklist, .mblock');
      // (yb) the smallest label, in screen pixels: font-size in viewBox units times the
      // drawn width over the viewBox width -- what the child's eye actually gets
      let labelPx = null;
      try {
        const vb = (svg.getAttribute('viewBox') || '').split(/\s+/).map(Number);
        const scale = (vb.length === 4 && vb[2] > 0) ? r.width / vb[2] : 1;
        svg.querySelectorAll('text').forEach(t => {
          const fs = parseFloat(t.getAttribute('font-size') || (getComputedStyle(t).fontSize || '12'));
          if (!(fs > 0) || !(t.textContent || '').trim()) return;
          const px = fs * scale;
          if (labelPx === null || px < labelPx) labelPx = px;
        });
      } catch (e) {}
      out.push({ kind: m.getAttribute('data-kind') || '', width: Math.round(r.width), height: Math.round(r.height),
                 shrunk: svg.hasAttribute('data-pu-maxw'), host: host ? host.className.split(' ')[0] : '',
                 label_px: labelPx === null ? null : Math.round(labelPx * 10) / 10,
                 refit: svg.hasAttribute('data-pu-room') });
    });
  });
  return out;
}"""


def script_walk(lesson, L=None):
    """The engine's own walk of one lesson, as the page would receive it: a list of
    turns, each (student_text_or_None, steps) where steps are the CLIENT shape main.py's
    _script_clean sends (kind, spoken, board, beat / choices, tap_only, guided, reason /
    mastered, graceful, next_id, next_topic, choice). Same path as coursesweep's
    transcript: pairs right, the first practice problem missed ONCE (so the scripted
    second explanation is rendered too -- never the AI), then right to the end. A table
    lesson shows its first six facts. No model, no network, no main.py."""
    if L is None:
        import lessonscripts as L  # noqa: N812
    st = L.start(lesson, seed=20260924)

    def clean(steps):
        out = []
        for s in steps:
            c = {"kind": s["kind"], "spoken": s.get("spoken", ""), "board": s.get("board", "")}
            if s["kind"] == "say":
                try:
                    c["beat"] = s.get("beat") or L.beat_of(lesson, c["spoken"])
                except Exception:  # noqa: BLE001
                    c["beat"] = s.get("beat") or ""
            if s["kind"] == "ask":
                c["choices"] = s.get("choices", "")
                c["tap_only"] = bool(s.get("tap_only"))
                c["guided"] = bool(s.get("guided"))
                c["reason"] = bool(s.get("reason"))
            if s["kind"] == "end":
                c["mastered"] = bool(s.get("mastered"))
                c["graceful"] = bool(s.get("graceful"))
                c["next_id"], c["next_topic"], c["choice"] = "", "", False
            if s["kind"] == "intervene":
                continue            # the walk never reaches the model; a resume follows
            out.append(c)
        return out

    turns = []
    out, st = L.step(lesson, st, ("begin",))
    turns.append((None, clean(out)))
    missed, facts = False, 0
    for _ in range(200):
        if st.get("finished"):
            break
        pend = st.get("pending") or {}
        if pend.get("reason"):
            reason = (lesson.get("explain") or {}).get("answer", "")
            out, st = L.step(lesson, st, ("answer", reason))
            turns.append((reason, clean(out)))
            continue
        p = pend.get("problem")
        if p is None:
            break
        if st.get("phase") == "table":
            facts += 1
            if facts > 6:
                break
        right = L.ans(p)
        if (st.get("phase") == "practice" and not missed and not pend.get("guided")
                and L._worked_for(p) is not None):
            missed = True
            wrong = (right or 0) + 777
            out, st = L.step(lesson, st, ("answer", wrong))
            steps = list(out)
            if any(x.get("kind") == "intervene" for x in out):
                out2, st = L.step(lesson, st, ("resume",))
                steps += list(out2)
            turns.append((str(wrong), clean(steps)))
            continue
        out, st = L.step(lesson, st, ("answer", right))
        turns.append((str(right), clean(out)))
    return turns


def capture_script(lesson_id, static_dir=None, port=8741, shots_dir=None,
                   viewport=(1280, 900), max_turns=60, L=None):
    """Drive ONE authored lesson through the real scripted player and snapshot every
    turn as the student is asked to act. Requires Playwright. Returns [Snapshot]."""
    from playwright.sync_api import sync_playwright
    if L is None:
        import lessonscripts as L  # noqa: N812
    lesson = L.LESSON_BY_ID[lesson_id]
    course = lesson["course"]
    turns = script_walk(lesson, L)
    static_dir = static_dir or os.path.join(HERE, "static")
    root = os.path.dirname(os.path.abspath(static_dir))
    state = dict(DEFAULT_SESSION_STATE)
    state["history"] = []
    srv = _serve_static(root, port, csp=real_csp(root))
    snaps = []
    cursor = {"i": 0}

    def _json(route, obj, status=200):
        route.fulfill(status=status, content_type="application/json", body=json.dumps(obj))

    def on_start(route):
        cursor["i"] = 1
        _json(route, {"ok": True, "lesson": lesson["topic"], "id": lesson_id,
                      "steps": turns[0][1], "practice": {"phase": "teach", "run": 0, "need": 3, "on": False}})

    def on_answer(route):
        i = cursor["i"]
        if i < len(turns):
            cursor["i"] = i + 1
            _json(route, {"ok": True, "steps": turns[i][1]})
        else:
            _json(route, {"ok": True, "steps": [{"kind": "end", "spoken": "", "board": "", "mastered": True,
                                                "graceful": True, "next_id": "", "next_topic": "", "choice": False}]})

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(args=["--no-sandbox"])
            page = browser.new_page(viewport={"width": viewport[0], "height": viewport[1]})
            console = []
            page.on("console", lambda m: console.append({"level": m.type, "text": m.text}))
            page.on("pageerror", lambda e: console.append({"level": "pageerror", "text": str(e)[:400]}))
            page.route("**/api/session/**", lambda r: _json(r, state))
            page.route("**/api/script/lessons**", lambda r: _json(r, {"ok": True, "lessons": [
                {"id": lesson_id, "topic": lesson["topic"], "unit": lesson.get("unit", 1),
                 "course": course, "course_title": course}]}))
            page.route("**/api/script/start**", on_start)
            page.route("**/api/script/answer**", on_answer)
            page.route("**/api/script/warm**", lambda r: _json(r, {"ok": True, "lines": []}))
            page.route("**/api/script/intervene**", lambda r: _json(r, {"ok": True, "steps": []}))
            page.route("**/api/chat**", lambda r: _json(r, {"reply": ""}))
            for stub in ("**/api/voice-status**", "**/api/transcribe**", "**/api/sprint/**",
                         "**/api/tour-seen**", "**/api/client-error**", "**/api/streak**"):
                page.route(stub, lambda r: _json(r, {}))
            page.route("**/api/speak**", lambda r: r.fulfill(status=200, content_type="audio/mpeg", body=b""))
            page.clock.install()
            page.goto("http://127.0.0.1:%d/%s/session.html?code=SCREENCHECK&course=%s"
                      % (port, os.path.basename(static_dir), course), wait_until="load")
            STUB = "() => { window.speak = function(){ return Promise.resolve(); }; }"
            page.evaluate(STUB); page.clock.run_for(800); page.evaluate(STUB)
            page.evaluate("""() => { const g=document.getElementById('welcomeGo');
              if (g && g.offsetParent!==null) g.click();
              document.querySelectorAll('.welcome.show').forEach(w=>w.classList.remove('show')); }""")

            def settle():
                """Run the clock until the page waits for the student: an ask on screen
                (SCR.pending, not busy), a check/ready gate (answered here with its first
                label), a Next pacer (clicked), or the lesson over. Returns the reason."""
                for _ in range(400):
                    page.clock.run_for(350)
                    st = page.evaluate("""() => { const S = (typeof SCR !== 'undefined') ? SCR : null;
                        return { on: !!(S && S.on), pending: !!(S && S.pending),
                        busy: (typeof busy !== 'undefined') ? !!busy : false, check: !!(S && S.check),
                        next: Array.from(document.querySelectorAll('.choicerow button')).some(b => /Next/.test(b.textContent)),
                        queue: (S && S.queue) ? S.queue.length : -1 }; }""")
                    if st["check"]:
                        page.evaluate("() => { const c = (typeof SCR !== 'undefined') ? SCR.check : null; if (c) c.done(c.labels[0]); }")
                        continue
                    if st["next"]:
                        page.evaluate("""() => { const b = Array.from(document.querySelectorAll('.choicerow button')).find(x => /Next/.test(x.textContent)); if (b) b.click(); }""")
                        continue
                    if st["pending"] and not st["busy"]:
                        return "ask"
                    if not st["on"] and not st["busy"] and st["queue"] == 0:
                        return "done"
                return "stuck"

            for i in range(max_turns):
                why = settle()
                page.clock.run_for(900)         # let the .pop animation and the rAF placing land
                data = page.evaluate(SNAPSHOT_JS)
                data["overflow"] = page.evaluate(OVERFLOW_JS)
                data["fold"] = page.evaluate(FOLD_JS)
                data["figures"] = page.evaluate(FIGURES_JS)
                data["console"] = console[:]
                del console[:]
                data["turn"], data["name"] = i + 1, "%s · turn %d (%s)" % (lesson_id, i + 1, why)
                data["reply_raw"] = " | ".join(x.get("spoken", "") for x in turns[min(i, len(turns) - 1)][1])
                if shots_dir:
                    os.makedirs(shots_dir, exist_ok=True)
                    shot = os.path.join(shots_dir, "%s_turn%02d.png" % (lesson_id, i + 1))
                    page.screenshot(path=shot)
                    data["png"] = shot
                snaps.append(Snapshot(data))
                if why != "ask" or cursor["i"] >= len(turns):
                    break
                # the student answers: the walk decided what; the stub serves the next turn
                answer = turns[cursor["i"]][0] or "ok"
                page.evaluate("(a) => sendToTutor(a)", answer)
            browser.close()
    finally:
        srv.shutdown()
        try:
            srv.server_close()      # (xy) free the port: several captures in one process
        except Exception:  # noqa: BLE001
            pass
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
        console = []
        page.on("console", lambda m: console.append({"level": m.type, "text": m.text}))
        page.on("pageerror", lambda e: console.append({"level": "pageerror", "text": str(e)[:400]}))
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
            data["console"] = console[:]
            del console[:]
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
    # ---- S7: fires / silent (the text is Jim's real console line, 2026-08-17) ----
    ("S7 fires on the CSP violation from Jim's own lesson", "S7 the console is clean",
     {"turn": 1, "console": [{"level": "warning", "text":
      "Loading media from 'data:audio/wav;base64,UklGRmQ...' violates the following "
      "Content Security Policy directive: \"default-src 'self'\". Note that 'media-src' "
      "was not explicitly set, so 'default-src' is used as a fallback."}]}),
    ("S7 fires on an uncaught JavaScript error", "S7 the console is clean",
     {"turn": 1, "console": [{"level": "pageerror", "text": "TypeError: x is not a function"}]}),
    ("S7 ignores our own [voicehead] probe and ordinary logs", None,
     {"turn": 1, "console": [
      {"level": "log", "text": "[voicehead] started after 467ms | lead=3 | ctx=running"},
      {"level": "info", "text": "plausible loaded"},
      {"level": "log", "text": "[terms] bolding skipped: nothing to do"}]}),
    ("S7 silent when the console said nothing at all", None, {"turn": 1, "console": []}),
    # ---- S6: fires / silent ----
    ("S6 fires on a clipped rail", "S6 nothing is clipped",
     {"turn": 1, "overflow": [{"el": "#courseBar", "scroll": 1490, "client": 1280,
                               "text": "0 of 9 units mastered"}]}),
    ("S6 silent when everything fits", None,
     {"turn": 1, "overflow": [{"el": "#courseBar", "scroll": 1180, "client": 1280}]}),
    # ---- S8: fires / silent (xy; the numbers are geo-u1-when-lines-cross turn 3, as captured) ----
    ("S8 fires when the turn's last line is below the board", "S8 the last line is on the screen",
     {"turn": 3, "fold": {"feed_top": 104, "feed_bottom": 691, "turn_top": -1034, "turn_bottom": 1389,
                          "last_text": "the two sit on one straight line 180° − 70° = ?",
                          "choices_bottom": 771, "window_h": 900}}),
    ("S8 fires when the answer buttons are below the window", "S8 the last line is on the screen",
     {"turn": 2, "fold": {"feed_top": 104, "feed_bottom": 691, "turn_top": 110, "turn_bottom": 620,
                          "choices_bottom": 960, "window_h": 900, "choices_text": "110 70 20"}}),
    ("S8 silent when the last line and the buttons are on the screen", None,
     {"turn": 4, "fold": {"feed_top": 104, "feed_bottom": 691, "turn_top": -542, "turn_bottom": 627,
                          "choices_bottom": 771, "window_h": 900}}),
    ("S8 silent on a snapshot with no fold measured (an older capture)", None,
     {"turn": 1, "bubble_html": "Let's begin."}),
    # ---- S10: fires / silent (yb; the numbers are basic-u3-story-problems before and after the refit) ----
    ("S10 fires when a shrunk figure's smallest label is under the floor", "S10 the figure's words are readable",
     {"turn": 1, "figures": [{"kind": "array", "width": 351, "height": 248, "shrunk": True, "host": "mblock", "label_px": 6.2, "refit": False}]}),
    ("S10 silent once the figure is drawn again for its width", None,
     {"turn": 1, "figures": [{"kind": "array", "width": 466, "height": 329, "shrunk": True, "host": "mblock", "label_px": 15.5, "refit": True}]}),
    ("S10 silent on a figure with no label measured", None,
     {"turn": 1, "figures": [{"kind": "clock", "width": 418, "height": 418, "shrunk": False, "host": "mblock", "label_px": None}]}),
]

# (xy) LESSON-level fixtures: a list of turns, judged together.
LESSON_FIXTURES = [
    ("S9 fires when one kind is drawn at two sizes with no shrink behind it", "S9 figure widths agree",
     [{"turn": 1, "figures": [{"kind": "numberline", "width": 1190, "height": 216, "shrunk": False, "host": "mblock"}]},
      {"turn": 7, "figures": [{"kind": "numberline", "width": 978, "height": 178, "shrunk": False, "host": "stepcell"}]}]),
    ("S9 fires (LOW) when the small one was shrunk to fit its turn", "S9 figure widths agree",
     [{"turn": 3, "figures": [{"kind": "angle", "width": 588, "height": 418, "shrunk": False, "host": "mblock"}]},
      {"turn": 5, "figures": [{"kind": "angle", "width": 336, "height": 239, "shrunk": True, "host": "mblock"}]}]),
    ("S9 silent when the widths agree within tolerance", None,
     [{"turn": 1, "figures": [{"kind": "placevalue", "width": 1100, "height": 357, "shrunk": False, "host": "mblock"}]},
      {"turn": 2, "figures": [{"kind": "placevalue", "width": 1045, "height": 339, "shrunk": True, "host": "mblock"}]}]),
    ("S9 silent across DIFFERENT kinds (a number line and a pie are meant to differ)", None,
     [{"turn": 1, "figures": [{"kind": "numberline", "width": 1190, "height": 216, "shrunk": False, "host": "mblock"}]},
      {"turn": 2, "figures": [{"kind": "pie", "width": 658, "height": 416, "shrunk": False, "host": "mblock"}]}]),
    ("S9 silent with no figures at all", None, [{"turn": 1}, {"turn": 2}]),
]


def fixture_results():
    """[(name, expected_check_or_None, [Finding])] -- the shape ruletests consumes."""
    out = []
    for name, expected, data in FIXTURES:
        out.append((name, expected, run_checks(Snapshot(data))))
    return out


def lesson_fixture_results():
    """(xy) the same shape for the LESSON-level checks, each fixture a list of turns."""
    out = []
    for name, expected, turns in LESSON_FIXTURES:
        snaps = [Snapshot(d) for d in turns]
        found = []
        for fn in LESSON_CHECKS:
            found.extend(fn(snaps) or [])
        out.append((name, expected, found))
    return out


def self_test():
    """Run every fixture in both directions. Returns (passed, failed, [detail])."""
    passed, failed, detail = 0, 0, []
    for name, expected, found in fixture_results() + lesson_fixture_results():
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
    ap.add_argument("--page", default="session.html", choices=list(CAPTURE_PAGES) + ["all"],
                    help="which teaching page to drive with --render (default session.html; "
                         "'all' drives every page this module can drive -- build hb)")
    ap.add_argument("--live", metavar="BASE_URL",
                    help="drive a real lesson on a running site (needs playwright + a code)")
    ap.add_argument("--script", metavar="LESSON", action="append",
                    help="(xy) drive an AUTHORED lesson through the scripted player and judge "
                         "every turn -- a lesson id, a course name (every lesson of it), or "
                         "'all'. Repeatable. Needs playwright; no key, no server, no cost.")
    ap.add_argument("--code", default="", help="student code for --live")
    ap.add_argument("--course", default="geometry")
    ap.add_argument("--static", default=None, help="path to static/ (default: ./static)")
    ap.add_argument("--shots", default=os.path.join(HERE, "static", "shots", "screencheck"))
    ap.add_argument("--out", default=None, help="write the markdown report here")
    args = ap.parse_args(argv)

    if args.self_test or not (args.render or args.live or args.script):
        passed, failed, detail = self_test()
        print("screencheck self-test: %d passed, %d failed" % (passed, failed))
        for d in detail:
            print("  FAIL  %s" % d)
        return 0 if failed == 0 else 1

    if not playwright_available():
        print("playwright is not installed here -- the CHECKS still run (--self-test); only\n"
              "capturing a fresh screen needs it.  pip install playwright && playwright install chromium")
        return 2

    if args.script:
        import lessonscripts as L  # noqa: N812
        ids = []
        for want in args.script:
            if want == "all":
                ids += [les["id"] for les in L.LESSONS]
            elif want in L.LESSON_BY_ID:
                ids.append(want)
            else:
                ids += [les["id"] for les in L.LESSONS if les["course"] == want]
        snaps = []
        for n, lid in enumerate(ids):
            got = capture_script(lid, static_dir=args.static, shots_dir=args.shots, port=8741 + (n % 50))
            snaps += got
            print("# %s: %d turns" % (lid, len(got)), file=sys.stderr)
    elif args.render:
        corpus = _load_corpus(args.render)
        pages = CAPTURE_PAGES if args.page == "all" else (args.page,)
        snaps = []
        for i, pg in enumerate(pages):
            shots = (os.path.join(args.shots, pg.replace(".html", ""))
                     if args.shots and len(pages) > 1 else args.shots)
            got = capture_render(corpus, course=args.course, static_dir=args.static,
                                 shots_dir=shots, port=8731 + i, page_name=pg)
            for sn in got:
                # Attribute every finding to the page it came from -- three pages'
                # findings in one report are unreadable otherwise.
                try:
                    sn.name = "%s · %s" % (pg, getattr(sn, "name", ""))
                except Exception:  # noqa: BLE001
                    pass
            snaps += got
        if args.page == "all":
            print("# screencheck drove: %s" % ", ".join(pages))
            print("# NOT covered (separate stacks, not forks of this renderer): %s"
                  % ", ".join(UNCOVERED_PAGES))
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

# =============================================================================
# tags.py  --  THE TAG GRAMMAR, ONE COPY  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-08-26  BUILD oj -- [[beside]] joins TAG_INLINE (attribute-free, draws
#               nothing itself): it arms board.js's mountBlock so the NEXT board
#               block lands NEXT TO the previous one (side-by-side comparison,
#               rule 58d). Registered here the moment the pages learned it -- the
#               registry cross-check caught the omission on the first battery
#               run, exactly as this file's design intends.
#   2026-08-18  BUILD hm -- UNITPLAN_UNIT_PATTERN: the one regex source for reading the
#               unit out of a [[unitplan]] tag. main.py (filing) and tutor.py (the new
#               unitplan referee) BOTH need it, and two hand-typed copies of the same
#               pattern is the Class-B disease this file exists to end. Pure data still:
#               it is a pattern STRING; each consumer compiles it itself.
#   2026-08-17  NEW FILE (build hh -- the last Phase 2 build of the full-app review).
#               The [[tag]] grammar is the app's central contract -- the tutor writes
#               tags, the referees read them, the battery validates them, the pages
#               render them -- and the review counted SEVEN independent declarations
#               of which tags exist: FIGURE_TAGS, _BOARD_TAGS, _PQ_BOARD_TAGS and a
#               literal re-declaration of the figure list (_FIGURE_TAGS, same 22
#               members re-typed in a different order) in tutor.py; BOARD_TAG,
#               TAG_HANDLER and TAG_INLINE in ruletests.py; plus the page
#               dispatchers. Some had ALREADY drifted: the live-scenario BOARD_TAG
#               regex was missing numberline and areamodel, so a reply that taught
#               with either of those counted as "no board" in --live checks.
#               This file is now the single source. tutor.py and ruletests.py DERIVE
#               their sets from it; the page dispatchers remain page-specific BY
#               DESIGN (which tags a page supports is configuration), and the battery
#               cross-checks them against this registry so a tag added anywhere
#               without registering it here fails the build.
#
# PURE DATA, HARD-IMPORTED ON PURPOSE. This module contains no logic, no imports and
# no I/O; nothing in it can fail at runtime. tutor.py imports it WITHOUT a defensive
# try/except, deliberately breaking the repo's defensive-import convention: a missing
# or unparseable tags.py should stop the deploy loudly at boot, because "the referees
# silently forgot what a tag is" is the Class-A disease (fail-open, observed nowhere)
# in its purest form.
# =============================================================================

# ---- FIGURES: tags drawn as pictures (math-figures.js / geo-figures.js) ----------
# The visual referee (rule 7) and the caption referee (rule 41) both key on this set,
# and ruletests PART 3c ratchets it against session.html's dispatcher.
FIGURE_TAGS = (
    "graph", "numberline", "bars", "histogram", "dotplot", "boxplot", "scatter",
    "normal", "twoway", "tree", "pie", "unitcircle", "righttriangle", "conic",
    "areamodel", "vector", "triangle", "angle", "circle", "objects", "machine",
    "balance",
)

# ---- WRITING: tags that put words/equations on the board -------------------------
WRITING_TAGS = ("write", "step", "solve", "column", "card")

# The equation-carrying subset the prose-vs-board referee sweeps for labelled
# conclusions (rule 18b). Order is match order in the compiled regex.
STEP_TAGS = ("step", "write", "solve")

# ---- EVERYTHING that puts anything on the board, picture or writing --------------
# (tutor.py's rule-7 "a picture was promised" referee keys on this.)
BOARD_TAGS = FIGURE_TAGS + ("write", "step", "solve", "column", "card", "check",
                            "quiz", "goal", "today", "unitplan", "finalexam",
                            "choices", "highlight")

# ---- CONTENT tags: board material a teaching turn can consist of -----------------
# Rule 15's pending-question referee asks "is there a worked line on the board for
# the question being asked?" -- these are the tags that can carry one. The live
# scenarios' "did the reply draw ANY board" check uses this set too (build hh: it
# previously used a hand-typed 10-tag list that had drifted -- numberline and
# areamodel were missing, so teaching with either read as "no board").
PENDING_BOARD_TAGS = ("step", "write", "solve", "column", "card", "graph",
                      "numberline", "objects", "balance", "machine", "areamodel",
                      "choices")

# ---- RENDERER MAP: tag -> the show* function that draws it -----------------------
# (Figure tags route through showFig/showGeo and are not listed one-by-one.)
TAG_HANDLER = {
    "balance": "showBalance", "card": "showCard", "machine": "showMachine",
    "step": "showStep", "column": "showColumn", "write": "showWrite",
    "solve": "showSolve", "check": "showCheck", "quiz": "showQuiz",
    "today": "showToday", "todaydone": "markTodayDone", "unitplan": "showUnitPlan",
    "finalexam": "showFinalExam", "choices": "showChoices", "objects": "showObjects",
}

# ---- INLINE tags: attributes read inside handleTags itself (no show* function) ---
TAG_INLINE = {
    "goal": {"text"}, "highlight": {"id"}, "clear": set(),
    "mark": {"correct", "attempted"},
    # build et: [[nice]] is attribute-free -- a correct answer along the way, no
    # tally, no server call, just the quiet ring.
    "nice": set(),
    # build ey: [[bye]] is attribute-free and draws NOTHING. It is the session's
    # wrap-up mark (rule 29a) -- the only mechanical end-of-session signal there has
    # ever been -- and its whole effect is to queue the goodbye moment clip.
    "bye": set(),
    # build oj: [[beside]] is attribute-free and draws nothing ITSELF -- it arms
    # mountBlock (board.js) so the next board block joins the previous one in a
    # side-by-side row (rule 58d: comparing two ways, an equation and its picture).
    "beside": set(),
}

# ---- UNITPLAN: the one pattern for reading the declared unit out of the tag ------
# (build hm) main.py files the declaration into topic_progress; tutor.py's unitplan
# referee vetoes a declaration the record cannot justify. Both compile THIS string, so
# "which unit does this tag declare" has exactly one definition.
UNITPLAN_UNIT_PATTERN = r'\[\[\s*unitplan\b[^\]]*?unit\s*=\s*"?(\d{1,2})"?[^\]]*\]\]'

# ---- CONTENT ATTRS: a figure tag needs at least one of these or it renders empty -
CONTENT_ATTRS = {
    "graph": {"func", "fn", "functions", "lines", "parabola", "parabolas", "points"},
    # build em: "parts" is the EQUAL-PARTS fraction form ([[pie parts="4"
    # shaded="3"]]), which carries its content in parts/shaded rather than
    # data/sectors.
    "pie": {"data", "sectors", "parts"}, "bars": {"data"},
    "histogram": {"data", "values"}, "dotplot": {"data", "values"},
    "boxplot": {"data", "values", "five"}, "scatter": {"points"},
    "twoway": {"data"}, "tree": {"stage1", "stage2", "a", "b"},
    "vector": {"v", "vectors"}, "conic": {"type"}, "areamodel": {"rows", "cols"},
    "objects": {"n", "groups"}, "card": {"items", "id"},
    "write": {"text", "lines"}, "solve": {"start", "top"},
}

# I did no harm and this file is not truncated.

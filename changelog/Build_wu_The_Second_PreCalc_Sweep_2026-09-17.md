# Build wu — The Second Pre-Calc Sweep (2026-09-17)

REPORT HEADER (copied first): Course sweep -- precalc -- 2026-09-17 16:44 UTC (build ws).
Read by openai · gpt-5.5. By kind: words-board 13, false 10, unclear 8, unsupported 2,
untaught-term 1. 27 of 36 lessons read · 34 findings (10 on generators, 24 authored) · 8
lessons clean (machines-in-a-row, no-long-division, twice-forbidden, count-the-halvings,
money-doubles, the-faster-wave, the-thirty-degree-ramp, past-the-full-turn) · 0 unplaced ·
**9 unread** (OpenAI 429 "no credits remaining" from pc-u7-where-you-are-at-time-t on: all of
U8 and U9) · 37 minutes. The first sweep (wl, read on build wm) was 76 findings, 5 clean.

The second rerun of the second round. Pre-Calc's first reading ran on `wm`, before `wn`'s
80 edits ever reached it, so this is the first time the reader has seen the fixed course —
and on the 27 lessons it reached: **76 → 34 findings (on three-quarters of the course),
5 → 8 clean**. The same convergence Diffeq showed at `ws`. Nine lessons went unread when the
reader's credits ran out mid-sweep (the cap was raised afterwards); they are the U7 parametric
lesson and all of U8–U9, and they wait for the next Pre-Calc run.

Stamp: **`2026-09-17wu-the-second-precalc-sweep`**. Battery: see the bottom of this doc.

## The generator (lessonscripts.py) — four ops and a walk-back word

- **`vmag`** walk-back (six MEDIUMs, one line): "shorter than walking both, 47" — the 47 dangled
  after the answer, unexplained and undrawn. Now "shorter than walking both — 12 plus 35 is
  47", with `walking both: 12 + 35 = 47` as a third board line under the squares. The praise's
  "Watch the squares on the board" said it over a board that (since `wt`) carries the
  answered line, not the squares — now "The squares come next."
- **`arsn`** (90-degree case), praise and walk-back: "the whole 60 is the rectangle around it,
  and a triangle takes half" named a rectangle nothing drew. Now the half comes from the
  right angle: "6 is the base and 10 is the height, and a triangle's area is half of base
  times height."
- **`cofn`** praise: one 30-word sentence → two. Its walk-back's "what one corner calls
  height, the other calls across" became "the side opposite one corner sits beside the
  other" (the same fix as the authored teach line, below).
- **`fshf`** praise: "exactly as the vertex lesson said" — a back-reference to a lesson this
  course has not had. Dropped.
- **`fpie`** walk-back: "check the neighborhood, then compute" — the untaught term the sweep
  found in the authored teach lives in the generator too. "Check the side."

## The authored pile (lessons/precalc.py) — 27 edits

**Laws with their condition (10 false).** "Inside the parentheses, the sign points opposite.
Always." → "For a slide written inside the parentheses, like f of x take away 3, the sign
points opposite" (HIGH). "Roots refuse negatives" → *square* roots. "Each minus sign cancels
the one before it" → "minus signs cancel in pairs". The roots' secret: the roots add to the
middle number *worn with a minus* — the why board (`roots add → −(middle)`, HIGH), the why
words, the teach ("their sum is the middle number, worn with a minus"), and the picture
caption now says (−2) × (−6) = 12 as the words do. The log rebuild is "for these equations —
log base a of x equals b" (HIGH); the logarithm and exponential un-do each other "in the same
base". The backwards spin: "add full turns of 360 until it comes out positive — for the
angles in this lesson, one turn does it". The wave's touches count "after the start"; one
whole "on the unit circle".

**Words and board (13).** "Neighborhoods" (untaught) → "sides of the border", in the teach,
the trap line and the picture caption. The reference-angle gap's "?" label is explicit
(`split="175,?"` — the figure drew it before by default; the reviewer read the tag, not the
render, so this one is a clarification rather than a fix). The cofunction's shared side is
said plainly; "Unit Two's minus parade" is named for the child who needs the referent;
"timesed" is out of a reason choice; both ellipse worked lines read "equals 1" and the second
draws its equation (`x²/196 + y²/36 = 1`) instead of speaking one term; the radius reason
board writes `(x − 2)² + (y − 9)² = 225`; the circle's worked line reads "equals 16"; "the
doorway before that" → "Unit One's sliding graphs".

**Unclear (8).** The half-turn recap, the circle's picture and the roots' teach are short
sentences; "that million-sized number" names 1024 squared. The two generator lines above.

## Counts

Course lines **39,999** (no beat added); closure 40,253; speechmap **2,245 → 2,244** and
forSpeech drift **1,939 → 1,938** — the ellipse's "over 196: 14 each way" was a
digit-colon-digit that forSpeech tidied as a ratio, and the line now reads the whole equation
(both pins moved, with their ledger notes). `L.validate` over all 360: 0 failures (two caught
mid-build: a 35-word sentence, and "makes" in the arsn praise — the canon is "equals"). The
referee sweep over all ten courses: still the one intro card. Every changed board tag rendered
headlessly with no `boardWarn`. PART **3mp** (8 checks); two PART 3mi pins moved to the new
wording.

## After the push

Prewarm: the four ops' lines and roughly thirty Pre-Calc rewrites. Then **re-run the Pre-Calc
sweep** — nine lessons have never been read on a fixed build (U7's parametric lesson, U8, U9),
and the 27 read ones get their second-fix reading. Algebra II (first read on `wk`) is next in
the queue.

## Battery

Frozen copy, 2026-09-17: **12,666 passed · 0 failed · 3 skipped** (12,658 at `wt`). Clean on the first run.

I did no harm and this file is not truncated.

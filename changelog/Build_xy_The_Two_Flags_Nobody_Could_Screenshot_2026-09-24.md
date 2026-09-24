# Build xy — The Two Flags Nobody Could Screenshot, 2026-09-24

Project 6 of the 09-14 deep dive; the seventh gate build, built while Jim ran the Basic sweep.
The deep dive's line: *Screencheck learns the two flags nobody could screenshot. A board whose
last line lands below the visible area fails; figure widths within one lesson must agree. Runs
in the battery on every push.*

Stamp: **`2026-09-24xy-the-two-flags-nobody-could-screenshot`**. PART **3nt**. A gate build.

## The two flags

Jim's corrections queue said **"a board line below the fold"** twice in August. No screenshot
survived, and the 09-14 handoff closed it: *guessing at a layout fix would be duct tape; the
right answer if it recurs is structural — teach screencheck to fail a board whose last line
lands below the visible area.* On 09-11 he said the board's figures are **"generally small,
and inconsistent"** — *"the graphic is half as big as it should be"* on the ask. Build `pc`
gave every figure one display rule and `vk` made the words fit, and the flag stayed open
because nobody could see it happen.

Both are measured now — and measuring them found both causes in one afternoon.

## What screencheck learned

**S8 — the last line is on the screen.** After a turn lands and the board has done its own
placing (`ir`: a turn starts at the top; `ns`: the view follows the pen; `pu`: an over-tall
turn's figure is shrunk), the turn's last board line must end inside the board's visible
area and the answer buttons inside the window. Measured at capture time (`FOLD_JS`), judged in
pure Python like every other check. HIGH.

**S9 — figure widths agree.** The first *lesson-level* check: every turn's figures together,
by kind. Two number lines in one lesson are drawn within 12% of one width; a number line and
a pie are meant to differ. A figure the board shrank on purpose (`pu`, `data-pu-maxw`) is LOW
and the evidence says so; an unexplained disagreement is MEDIUM. `board.js` stamps every
figure with `data-kind` so the reader never guesses.

**A third way to capture: the scripted lane.** Every capture screencheck had drives the
live-tutor door; the flags were raised on authored lessons, which the scripted player draws
by a different path. `--script LESSON|COURSE|all` now walks a lesson with the engine itself —
`script_walk`: the pairs right, the first practice problem missed once, right to the streak,
the reason, the end; no model, no network — serves each turn to the real page from a stub,
and the page plays every beat for real. Playwright's clock runs the reading floor (2.6 s a
beat) through instantly, so a lesson captures in about 50 s.

## What the first survey found

Sixty-eight lessons — Entry, Basic, twelve of Geometry — at 1280×900:

**S8 fired on 14 turns in 7 Geometry lessons: the question 600–730px below the fold.** The
screenshot is exactly what Jim described: the practice intro card on the board, three answer
buttons under it, and no question anywhere. The cause: the pages' scroll listeners set
`stickBottom` from the distance to the *bottom* (`ay`) — but since `ir` a tutor turn anchors
at the *top*, so the view is never within 48px of the bottom while a short turn is on screen.
One scroll event that was not ours — the browser re-clamping `scrollTop` when an earlier block
folded away (`supersedePrevious`'s "show the N earlier steps") — ran that line, read "far from
the bottom", and latched `stickBottom` false. From then on every `scrollFeed` returned early.
It needs a fold and a second scroll event in the same beat, which is why it could not be
screenshotted on demand. **Fixed in `board.js`:** `feedAnchorTarget()` is the one place the
anchored target is computed (`scrollFeed` uses it too) and `feedIsFollowing()` — within 48px
of that target, or of the bottom in pin-bottom mode — is what the three pages' listeners set
`stickBottom` from. A child who scrolls up to read is still left alone. The first cut left two
turns failing: `handleTags` folds synchronously *between* `addBubble` and its rAF, so a scroll
event in that window was judged against a target the view had not moved to yet — while a
placing is pending, the view counts as following (`_feedPlacing`).

**S9 fired on 34 lessons, and the worst was a place-value chart at 385px on a 1100px board.**
The probe showed the chart drawn full width, then collapsed to 35% on an *18px* overage.
`fitTurnToBoard` summed `svg.offsetHeight` — a property that exists on HTMLElement and is
**undefined on an SVG element** — so `figH` was NaN, the `<= 0` guard let it through, the
factor was NaN, and `!(factor > 0)` sent every over-tall turn, by 18px or 400px, straight to
the 0.35 floor. `pu`'s own build doc recorded "the number line went 787px → 190px" and read it
as the proportional shrink working. **Fixed:** the fitter measures with
`getBoundingClientRect` and shrinks by exactly the overage (the 18px case now draws at
1045px).

**And a third thing, in the auditor itself.** `real_csp` rebuilt the policy from every quoted
string in the literal's block — including `"media-src 'self' data:"` inside `vj`'s *comment* —
so every harness run since 09-11 served `media-src 'self' data:media-src 'self' data: blob:`,
Chromium logged the invalid source on every turn, and S7 reported it as the app's fault. It
reads the literal with Python's parser now. Production was never affected.

## After the fixes

The same lessons again (45 — all of the S8 and MEDIUM hits and more): **0 S8, 0 MEDIUM S9,
29 LOW S9.** The 29 are the fit rule doing what Jim asked in `pu` ("visible without the
student moving anything"): a beat whose bubble, figure and step lines run past a 544px board
— which is what a 900px window leaves once the header, the chips, the answer-bar line and
the answer buttons are up — has its figure shrunk, now proportionally, to the 340px floor at
worst. That is honest and it is the next thing to look at, not this build's: `pu` itself named
turn length as the real fix. Two things the probe saw on the way, for that build: a shrunk
figure keeps the label sizes `vk` fitted for the full board, and the array's "5 rows" label
sits on its row count at small sizes.

One S5 finding on the survey (entry-u8-minutes-past-the-hour: "the caption answers the
question") is the older check misreading "which clock number is the minute hand pointing to";
left alone.

## Proved

PART 3nt pins S8/S9 and their fixtures (both directions, lesson fixtures included), the
capture, `real_csp`'s parser, the `figBox` measurement, `feedAnchorTarget`/`feedIsFollowing`/
`_feedPlacing`, the three listeners, and `data-kind` — and drives
`geo-u1-when-lines-cross` and `basic-u1-place-value-to-1000` in a real browser every battery:
no S8, no MEDIUM S9, no S7, and every place-value chart at 1000px or wider. `screencheck.py
--self-test`: 34 passed. `python screencheck.py --script basic` is the survey, repeatable by
anyone with Playwright; the nightly screenwatch workflow is unchanged (it drives the live
lane) and can take `--script` when Jim wants the course watched too.

## Files

`screencheck.py` (S8, S9, `LESSON_CHECKS`, `script_walk`, `capture_script`, `FOLD_JS`,
`FIGURES_JS`, `--script`, `real_csp`, `server_close`, fixtures), `static/board.js`
(`data-kind`; `figBox`; `feedAnchorTarget`, `feedIsFollowing`, `_feedPlacing`),
`static/session.html`, `static/practice.html`, `static/topic.html` (the listener line),
`main.py` (stamp), `ruletests.py` (PART 3nt), this doc, the refreshed
`START_HERE_Handoff_2026-09-24.md`.

Battery on the frozen copy, 2026-09-24: **13,061 passed · 0 failed · 3 skipped** (13,030 at `xx`), third run clean — the first two fell on my own stale pins (3fy's anchor-order pin named the old target expression; 3in's `(build sq)` note pin read a fixed 3,000-byte slice of board.js that xy's two notes pushed past — it reads `notes()` now, like the rest). Two more fixed-slice note pins remain for other files (cadabra.js, voice.js, geo-figures.js) and will bite whoever adds a header note there next.

I did no harm and this file is not truncated.

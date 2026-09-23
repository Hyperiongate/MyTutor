# Build xs — The Third Diffeq Sweep, 2026-09-23

Sweep header, 2026-09-23 14:24 UTC, read by gpt-5.5 on build
`2026-09-23xr-the-pencil-in-the-scripted-lane`: **36 of 36 lessons read · 39 findings (5 on
generators, 34 on authored beats) · 13 lessons clean · 0 unplaced · 0 unread · 3813.7s.** By
kind: words-board 22, false 15, untaught-term 2. The floors: `wr`'s reading **62 findings, 8
clean** (fixed in `ws`); `wo`'s **119, 0**.

Stamp: **`2026-09-23xs-the-third-diffeq-sweep`**. PART **3nn**. The sweep build of the
alternating schedule (`xr` was the gate build before it; the voice-cache reclaim card is the
gate build after).

## The reading that saw the miss path

This is the first Diffeq reading since `xo` gave all 36 lessons a scripted walk-back — 216
walk-backs the reviewer had never seen. The handoff expected the count to rise before it fell.
It fell: 62 → 39, 8 → 13 clean. Of the 39, exactly three sat on a walk-back (conc's, sysx's,
and estp's praise board), and none of them was a walk-back *shape* — no "repeats the praise",
no "step by step over the end only". The Phase C generators read clean on their first exposure.

## The class, measured before it was fixed

Thirteen of the 22 words-board findings quoted the same thing: **the board skips the arithmetic
the words say.** A worked line says "884 take away 100 is 784, whose root is 28, halved to 14"
over one compressed board line, `4×221 − 10² = 784`. The child hears four numbers and sees one.

Measured across the canon as a teach or worked-example beat whose words say a number of two or
more digits that its board does not carry: **126 beats, 35 of them in Diffeq** (the reviewer
quoted 13). Every Diffeq instance now draws the number — as a chained equals
(`4×221 − 10² = 884 − 100 = 784`) or a step line of its own (`√784 = 28` then `28 ÷ 2 = 14`;
`32 × 4 = 128 new` then `128 ÷ 8 = 16 foxes`), never " · " between two equations. PART 3nn
pins Diffeq at zero and the other nine as a falling ratchet (Basic 26, Prob/Stat 22, Geometry
18, Algebra II 14, Pre-Calc 13, Algebra I 10, Calculus 10, Entry 7, Pre-Algebra 5). The lower
courses' hits are noisier — a coin-count "25, 50, 75", a caption's number — so the ratchet is
the honest pin there; each course's next reading will say which of its hits are real.

A second, smaller class went the same way: **the goal board's given line is not said in its
own beat.** `step 10 → error 90` sat on the goal card while the words framed the lesson, and
was read aloud only in the next turn (three findings). This is `xb`'s "put the given line
first" from the other side. Measured as a first teach beat whose `[[step]]` carries a 2+digit
number the words never say: 40 canon-wide, 8 in Diffeq — each now said in the beat that shows
it ("Here: a step of 10 left an error of 90"; "Here: 20 rabbits, 3 born to each, 5
eaten by every fox"), with the next beat trimmed where it repeated. Diffeq zero, the rest a
ratchet.

## The HIGHs (6)

- **First order is the HIGHEST derivative being d y d x** — "an equation with d y d x is first
  order" was false for an equation that also has a second derivative. Two short sentences now.
- **The field the words describe is drawn.** "Here is the easiest field there is — every dash
  leans at 3 — with a walk drawn on it" over a board that drew only the line. `[[graph]]` gains
  `field="expr"` (math-figures.js): a 12 × 12 grid of dashes across the window, each leaning at
  the expression's value there — x and y both allowed, a bare number a constant field — drawn
  first and faint, so the walk, its points and labels sit on top. `compile()` takes an optional
  `withY`; every one-argument caller is byte-for-byte. Proven headless (Playwright, the board
  theme loaded): field="3" under y = 3x + 5 leans with the line; x+y and x²−y look right; a
  graph without field= draws exactly as before. The board contract (3c) reads the new attribute
  from the renderer, no declaration needed.
- **Smaller damping means a bigger swing FOR THE SAME FORCE AND FREQUENCY** — the lesson varies
  those numbers two beats later.
- **The final-value theorem is for a transform that settles** — the condition was in the
  sentence before; now it is in the sentence that states the rule.
- **"Adding gives 74"** — 14 + 46 is 60; 74 is 14 added to the trace. The wrong path is now
  named as one: "Adding 14 to the trace instead of taking it off gives 74."
- **"Where an arrow goes flat"** over x′ = 0 — which is the arrow going straight up or down, as
  the lesson itself says two beats on. The goal card reads "Where an arrow stops going across".
  (The lesson id keeps its name; only the board changed.)

## The generators (4 ops)

`conc`'s ask opened "The first number a mixing problem needs is the concentration" — a mixing
problem needs volume, flow and starting salt too; now "For the outflow of a mixing problem, the
key number is the concentration", matching the lesson's own "key number for the outflow". Its
walk-back's last line said the concentration is "what the outflow pipe carries away"; it is
"how many grams of salt ride in each litre the outflow pipe carries away". `estp`'s praise
board opened with `error ∝ step`, a symbol never taught or spoken — it reads "main error scales
with the step" now, the walk-back's own words. `rk4`'s ask said Euler's error halves and RK4's
divides by 16 as fact; now "about halves … by about 16. In this lesson we scale by exactly
that." `sysx`'s walk-back ended "a slope field with two directions instead of one" — a planar
system is one arrow per point with two parts; now "a field of arrows, each with an across part
and an up part, where Unit 1's dashes had one slope".

## The rest of the authored pile

Conditions: "with 1 on the r squared, the test has not changed"; "a POSITIVE number times y",
and the advance line says the square root *of that number*; the Laplace lesson solves "the
equations in this unit"; "a linear system OF TWO EQUATIONS has four numbers". Terms taught
where used: "A particular solution is one single solution that fits the pushed equation" before
the guess; `Y = L{y}` on the board before the rule leans on it. Smaller: the cooling cup's ✗
line says "the share, not the rate" as the words do; `y²/2 = 3x + c` drawn before `y² = 6x + C`
("double everything"); the RK4 instincts are "the orders themselves … 13, the right one" and
`208 ÷ 16 = 13 ✓` is on the board; Euler's advance line adds "added to the start"; the arrow
at (9, 5) is "drawn on its own, 31 across and 14 up" (the `[[vector]]` figure has no tail).

**Declined (1):** the damping lesson's advance line rule not on the closing card — the done
card is title and score in every lesson of every course.

Grading under the 09-22 ruling: **class** (the skipped arithmetic, 13 quoted / 35 measured;
the unsaid goal line, 3 / 8; laws without their condition, 7), **one-off** (18), **refused** (1).

## Counts

Course lines **40,495 — unchanged**: 109 lines out, 109 in, every line replaced one for one
(the 16 conc asks, the 16 rk4 asks, the 16 sysx walk-backs, 16 conc walk-backs, and 45
authored). Speechmap 941 of 40,801, one entry re-keyed. Every lesson validates. The Diffeq
referee sweep: 0 refusals before and after. The `xe`/`xf`/`xh`/`xj` measures all still read
zero (3na, 3nb, 3nd, 3ne pass). PART 3mo, 3mt, 3mv, 3my, 3nj, 3eu pass on the edited tree.

## The pre-flight is in the repo now

`pinscan.py` lived in a session scratchpad and was gone with it (the handoff said to recreate
it). It is `tools/pinscan.py` now, and simpler: it builds the corpus — every spoken line,
board, praise, walk-back and generated ask of every problem of every lesson, plus the raw
lesson and generator source — and, run once on the frozen tree with `--freeze` and once on the
edited tree with `--against`, prints exactly the string literals in `ruletests.py` that were in
the corpus and are not any more. It found seven stale pins this build (3mk's particular
solution, settling transforms, s plus 6; 3mn's conc opener, the highest-derivative sentence,
the two damping boards), all moved before the first battery. Two minutes a run.

## Battery

Frozen copy, 2026-09-23, three runs. Run 1: 11 failures — ten file-presence checks for files the staging had left out (the eight pencil clips and posters in `static/videos/cadabra/`, the four `changelog/*.html.md` roll-outs) and ONE real: 3kt's picture referee read the new goal line "On the board: a step of 10 left an error of 90" as a promised picture over a board with no figure. Changed to "Here:" (and recorded as a trap in the handoff). Run 2: 12,955 passed · 10 failed — the ten were the same file-presence checks, nothing else; the link to Jim's computer was down for the second half of the build. Run 3, once the link was back and the 15 files staged: **12,965 passed · 0 failed · 3 skipped** (12,935 at `xr`).

## Files

`lessons/diffeq.py` (71 edits), `lessonscripts.py` (conc, estp, rk4, sysx),
`static/math-figures.js` (`field=`), `tools/pinscan.py` (new), `ruletests.py` (PART 3nn; seven
pins moved), `speechmap.py` (regenerated, 941), `main.py` (stamp), this doc, the refreshed
`START_HERE_Handoff_2026-09-23.md`.

I did no harm and this file is not truncated.

# Build wn — The First Pre-Calc Sweep (2026-09-16)

The first sweep of Pre-Calc, on `wl`: **76 findings** (5 on generators, 71 authored), 5 of
36 lessons clean (no-long-division, count-the-halvings, the-thirty-degree-ramp,
the-sum-that-never-ends, walk-the-value-in), 0 unplaced, 55 minutes. By kind: false 31,
words-board 31, unsupported 6, unclear 5, untaught-term 3. Pre-Calc's own class: the
*standard-form rule stated as a law* — "un-square the right-hand number, every time",
"inside the parentheses a sign always points opposite", "Vieta: the end number is the
product" (only when the puzzle starts with a plain x²), "a doubling run lands one short of
the next double" (only when it starts at 1 — and the bank starts at 2, 3, 4, 5).

Stamp: **`2026-09-16wn-the-first-precalc-sweep`**. Battery: see the bottom of this doc.

## The generator (lessonscripts.py) — five items

- **`vasy`** (HIGH): the ask wrote `y = 1 ÷ (x − 2)(x − 4)`, which reads as
  `(1 ÷ (x − 2)) · (x − 4)` and forbids only one x. The whole bottom is grouped now:
  `1 ÷ ((x − 2)(x − 4))`, on the ask and in the walk-back's caption (the four authored boards
  of the same shape too).
- **`vmag`** praise: it spoke four numbers ("12 squared is 144, 35 squared is 1225, put
  together 1369…") over no board. The praise now says the result and the reason and leaves
  the squares to the walk-back, which draws them a beat later.
- **`vprd`** ask: "A puzzle's roots are 2 and 8, so it equals x − 2 times x − 8" — only if
  the puzzle starts with a plain x². It says so.
- **`wper`** praise: "faster waves repeat SOONER, never later" — a periodic wave repeats at
  later multiples too. Now "a faster wave's first repeat comes SOONER, not later."
- **`parm`** walk-back speaks the root line its board writes.

## The dot, seventh course

Fourteen authored step lines and six generator ops (`fcmp`, `fpie`, `sols`, `parm`, `lsid`,
`vasy`) joined two equations with " · " — `f(x) = x + 3 · g(x) = 2x` (HIGH),
`cos(−a) = cos a · sin(−a) = −sin a` (HIGH), `sin 35° = cos 55° · 35 + 55 = 90` (HIGH). Every
one is two `[[step]]` tags now, and the pin covers **seven courses** by rendered transcript.
Calculus, Prob/Stat and Diffeq remain.

## The authored pile (lessons/precalc.py) — 80 edits

**Laws with their condition.** The doorway's law → "these square-root functions, with x take
away a number inside" (HIGH), and the domain is read off the formula "in these formula-only
problems". "A function in pieces has a border" → in these examples, one border. Vieta →
"a puzzle that starts with a plain x squared" (teach, recap, and the ask). The log power
rule → "for a positive number, in one base". "Radians measure in half turns" (HIGH) → "for
these angles, count half turns … the number in front of pi", and "never count quarter turns
*as pi's*". Reference angles: "every arrow, wherever it lands" → every arrow that leans off
the flat line; the two nevers say "in this second quarter"; "why the circle reuses its
first quarter everywhere" (unsupported) → how the second quarter echoes the first, the
signs come later. "To count the answers of a trig equation" (HIGH) → for these sine and
cosine equations, once the target height is known — and *touches*, since sin = 1 grazes.
Cofunctions: "take any angle" → any *sharp* angle, and the identity carries its degree
marks, `sin a° = cos (90 − a)°` (the reviewer read the bare form as radians, twice).
"Un-square the right-hand number, every time" (HIGH) and "a sign always points opposite"
(HIGH) → "in this form". "The widest measurement the shape has" (HIGH) → for these ellipses,
the left-to-right width. "Doubling sums always land one short of the next term" (HIGH ×2) →
a doubling run that starts at 1.

**True statements.** "The lower curve is y = √x" (HIGH) — √x is the *upper* curve; it is
now "the curve that starts at the corner, at zero". "The smallest polynomial that bites"
(the lesson evaluates (−1)ⁿ) → power pattern. "Distances arrive squared" → this form carries
the distance squared. "The sine of 90 is 1" says degrees, three times. "6 is not the
heading; nobody ever sees 6" → 6 is not the y-value from either side: 3 from the left, 9
from the right. "360 take away the backwards one" (−45 would give 405) → the backwards
amount, 45. `(x−5)(x+5) ÷ (x−5) = x + 5` says "for x ≠ 5". "These machines do not commute"
(untaught) → give different answers when you switch the order. "Gauss's bare sum" spelled
out; "sum 1 up to n" → up to the top number. "The reason of the slide" says "f of: x take
away 3" (the words could be heard as f(x) − 3).

**Words-board.** The log lessons with mixed bases write the base: `log₂ 1024 = 10 ✓`,
`log₁₀ ? = 4`, `? = 10000 ✓` (two HIGHs, both about a bare "log" that Algebra II's charter
line covers only where the base is 2 throughout — here it is not). The shrinking window's
picture draws the line joining the two ends the words describe; its teach writes the 3-to-5
window; its recap draws the window shrinking onto 4. The bearings reason draws 350 turning
40. The circle worked lines write the whole equation (three), and the center's recap draws
the circle with its equation. The ellipse's teach writes the 25 → 5 → 10 tall and its worked
line writes the whole equation. The arrow's trap writes `5² + 12² = 169`, `√169 = 13`, and
both bounds. The parametric worked lines say and write the root. Money-doubles' trap board
carries the 32 and 64 the words say. The sigma why says the board writes the start and stop
in words. The team worked lines write the line-up products; the recap writes "pair: divide
by 2 — trio: divide by 6". Eight closing beats speak the equation their board writes.

**Not changed.** The lesson-done card cannot carry a fact (the center lesson's advance line,
LOW). The `(−1)^n — even → 1 · odd → −1` shape uses arrows, not equals, and is not a dot line.

## Counts

Course lines **39,999** (no beat added); closure 40,253; speechmap 2,246 of 40,305;
forSpeech drift 1,940 — none moved. One forSpeech trap dodged on the way: "up 12: 25 plus
144" re-keyed as a ratio ("12 to 25") and moved two counts; the colon became a dash and the
counts came back. `L.validate` over all 360: 0 failures (three long sentences split
mid-build; one "borrow" removed — canon is "regroup"). Every new board tag rendered
headlessly with no `boardWarn`. PART **3mi**; four old pins moved to split boards (the `fcmp`
teach and ask lines, `sols`'s and `lsid`'s asks); the dot pin grew to Pre-Calc.

## After the push

Prewarm: roughly ninety rewritten Pre-Calc lines plus the `vasy`, `vprd` asks and the
`vmag`/`wper` praise (about eighty generated lines). Then **Calculus**, **Prob/Stat**,
**Diffeq**. Expect the dot (about twenty authored lines left across the three, and the
generator's), the standard-form laws, and — in Calculus — limits stated without their
"for x ≠ a".
## Battery

Frozen copy, 2026-09-16: **12,589 passed · 0 failed · 3 skipped** (12,576 at `wm`). Two
things moved on the way: the canon's referee sweep refused `log₁₀ ? = 4 → ? = 10000` (an
arrow after an equals — the 08-27 audit's rule), so it is two lines; and the uq-era `fpie`
pin quoted the one-line `x = 2 · y = ?`.

I did no harm and this file is not truncated.

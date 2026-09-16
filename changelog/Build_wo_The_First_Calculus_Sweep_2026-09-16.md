# Build wo — The First Calculus Sweep, Half (2026-09-16)

The first sweep of Calculus, on `wm`, stopped at **19 of 36 lessons**: OpenAI answered
"429 — no credits remaining" from U5's where-the-bend-changes on, so units 6–9 were never
read. On the 19 it did read: **46 findings** (7 on generators, 39 authored), 2 clean
(feed-the-derivative-an-x, a-number-underneath), 0 unplaced, 28 minutes. By kind: false 29,
words-board 11, unsupported 4, unclear 2. Calculus's own class, in the half we saw: *the
calculus that was named but not done* — "calculus finds the best where the slope is zero"
over a board that only divided 40 by 4; "the product rule, checked" in a lesson that never
stated it; "calculus can prove it in one line" without the line.

Stamp: **`2026-09-16wo-the-first-calculus-sweep-half`**. Battery: see the bottom of this doc.

## The generator (lessonscripts.py) — six items

- **`linf`** (HIGH): the ask *said* "36 x squared divided by 3 x squared" while the board
  *drew* 36x² / (3x² + 3), and the walk-back said the x squareds "cancel exactly, whatever x
  is" — for the drawn function they do not; it only tends to 12. The words, caption, step,
  praise and walk-back now name the drawn function and use limit wording: far out the plus 3
  is nothing beside 3x², the leaders decide it, the curve flattens *toward* 12 and never
  quite lands.
- **`acce`** walk-back: "12 is the distance's number, one differentiation short" — one short
  of the acceleration is the *speed*, 24t. Now "the distance's own front number, never
  differentiated".
- **`cfix`** ask: the mended curve joins up "without a jump", not "smoothly" (the slope still
  changes from 1 to 0 at the join).
- **`llaw`** walk-back is three short sentences.
- **`maxa`** praise (HIGH): "every other *shape* with the same fence encloses less" — a circle
  encloses more. Every other *rectangle*.
- **`pwrc`** praise: "adding the two numbers is not a rule anything obeys" → not the
  power-rule move.

## The dot, eighth course — all 36 lessons

Fourteen authored step lines (in the read and the unread lessons alike — it is mechanical)
and ten generator ops (`jump`, `cfix`, `derv`, `evat`, `prod`, `chev`, `init`, `pgrw`, `llaw`,
`acce`) joined two equations with " · " — `inside = 7 · 2 × 7 × 4 = 56` was a HIGH on its
own (read as 392). Every one is two `[[step]]` tags now; the pin covers **eight courses** by
rendered transcript. Prob/Stat and Diffeq remain.

## The authored pile (lessons/calculus.py) — 62 edits, 19 lessons

**Laws with their condition.** "Whatever you do to the functions, you may do to their
limits" (HIGH ×2) → when each function has a limit of its own, the sum heads for the sum and
the product for the product. "A line has one slope, the number in front of x" → a line
written y = a number times x, plus a number. "The chain rule at a point: 2 times the inside…"
→ for a squared quantity (recap and advance line). "When one thing grows, everything built
from it grows too" (HIGH) → for this square. "Calculus finds the best where the slope is zero"
(HIGH) and "every peak and every valley" (HIGH) → for this problem / these valleys, and the
ends of a stretch get checked separately. "The best rectangle is a square" → for a fixed
amount of fence. "A break has a size" → this kind of break, a jump. "Take one side from the
other" (HIGH) → the lower from the higher. "Never plus" → adding is not the power-rule move.

**True statements.** Far-out-only-the-leaders (HIGH): the words name 8x² over 2x² + 2, the
x squareds no longer "cancel exactly", the curve "flattens toward 4 and never quite lands";
the symbol "cancel" became "leaders". "The average rate with its window closed" (HIGH) → the
number the average rates settle on as the window closes. "Nothing before Calculus could
measure" → Calculus gives a general way. "2 is only the slope's own number" (HIGH — the slope
of x + 2 is 1) → the plus number in the sloping piece. "10 is only half the derivative" (HIGH
— the derivative is 14) → the 2x part only. "Stopping after one leaves 5 … 20 is one
differentiation too many" (HIGH ×2) → 5 was never differentiated; 20 doubles again. The
side-50 sentence now writes `2 × 50 × 3 = 300` and says 225 is the area *at 15* (HIGH). "90,
read off the tangent at 9" → the tangent climbs 18; times the rate 5, 90. "A derivative is an
equation like any other" (HIGH) → a rate formula set equal to a target; the distance behind
8t (4t²) is named before the wrong-divisor warning. "x times x plus 9" → x times the quantity
x plus 9.

**Unsupported, now shown.** The product rule is stated and applied — first's derivative
times second, plus first times second's derivative — before "checked" (HIGH). The fence
problem writes `area = x(20 − x)`, `slope = 20 − 2x`, `x = 10`. Equal-halves writes its one
calculus line (`slope = 30 − 2x`, zero at 15) and the 1 × 29 and 5 × 25 the words say.

**Words-board.** The chain-rule boards write `y = (5x + 3)^6` and the worked expressions
(four boards); the line lesson writes the power-rule step it speaks; the best-rectangle
picture draws the 18-by-2 strip the words describe; two closing beats speak their board.

## Counts

Course lines **39,999** (no beat added); closure 40,253; speechmap **2,245** of 40,305
(2,246 at wn); forSpeech drift **1,939** (1,940 at wn) — both moved by one line: the
related-rates second worked line no longer says "2 times 9 times 5". `L.validate` over all
360: 0 failures (four caught mid-build: a symbol no longer named, a 13-word reason button,
two long sentences, and "makes" — canon is "equals"). The canon's referee sweep refused two
arrow-after-equals boards and a seven-line teach board; all three reshaped. Every new board
tag rendered headlessly with no `boardWarn`. PART **3mj**; ten generator pins and the 3fs
fragment for one-rate-drives-another moved; the dot pin grew to Calculus.

## After the push

Prewarm: roughly sixty rewritten Calculus lines plus the `linf` ask and walk-back and the
`acce`/`cfix`/`llaw`/`maxa`/`pwrc` lines (about seventy generated lines). Then: **add OpenAI
credits** (the sweep and the night watch both run on that seat), rerun the Calculus sweep for
the 17 unread lessons, and paste it — it becomes `wp`. Prob/Stat and Diffeq after.
## Battery

Frozen copy, 2026-09-16: **12,599 passed · 0 failed · 3 skipped** (12,589 at `wn`). One pin
tripped on the way and was answered honestly: the far-out lesson's closure reached
24,986 characters / $5.50 against the $5.50 tripwire — the new `linf` walk-back was wordy
("the plus 3 on the bottom"), and trimming the words brought it to 24,818 / $5.46. The
tripwire was not moved.

I did no harm and this file is not truncated.

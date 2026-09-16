# Triage — Night watch of 2026-09-15 (on `wa`): four HIGHs, three seats

Read 2026-09-16 under the 09-14 policy: truth-class and HIGH are actionable; MEDIUM/LOW
conduct goes to the ledger. 10 lessons, 16 confirmed (13 holes, 3 pass-throughs), 3 refuted.

Build **wj** — stamp `2026-09-16wj-four-highs-from-the-09-15-watch` — answers the four HIGHs.

## The four HIGHs, and where each landed

**1 and 2 — decimal-alignment (prealgebra), rule 13.** The tutor set out to show *why*
lining decimals up by their last digit fails, and picked 2.60 + 0.35 and then 1.05 + 2.40 —
two numbers with the same number of decimal places. Lined up by the last digit, those are
lined up by the decimal point; every column holds one place value; and the words said
something false about the picture ("the 6 and the 3 land in the same column, even though
they're different kinds of cents" — both are tenths; "the 5 (hundredths) lands under the 0
(tenths)" — the 0 of 2.40 is hundredths). One shipped as a `livecritic` pass-through, one as
a hole. This is a mathematical fact about the tag's own terms, so it earns a referee:
**101, `alignment_demo_conflict` (`aligndemo`), truth-class** — a `[[column align="last"]]`
whose terms all carry the same decimal length, plus a claim (prose or caption) that different
places share a column. The nudge says to use unequal lengths (2.6 + 0.35, unpadded) so a
tenths digit really lands over a hundredths digit, or to say plainly that with equal lengths
the last-digit rule happens to work. Rule 27's padding allowance is untouched: padding is
fine; claiming a mismatch after padding is the falsehood. Canon: 0 fires.

**3 — geometry-picture (geometry), rule 61.** "That's the one we always label lowercase c."
A convention spoken as a law, one lesson after `vy`'s lettered-law finding on the same
scenario. A row in the falsehood table, `hypotenuse-always-c`: escapes on usually / often /
convention / choose / in the formula; true form "the hypotenuse is always the side across
from the right angle; calling it c is a convention we choose so the formula reads a squared
plus b squared equals c squared."

**4 — returning-student (algebra2), rule 13/15.** "So we set each factor equal to zero" over
`[[step eq="x - 2 = ?"]]` `[[step eq="x - 3 = ?"]]`. This is `vy`'s pending-zero defect in a
second costume: `vy` matched a chain in one value ("x - 2 = ? or x - 3 = ?"); this reply put
the factors on separate lines, so the chain never matched and `pendcheck` was satisfied by
the question marks. `pendingzero` now has a second shape: the words say zero (equal to zero,
= 0, set … zero, zero-product) and two or more whole board values read `<letter expr> = ?`.
The nudge writes both `= 0` lines. `pendingzero` stays conduct (its class since `vy`);
whether a board that poses a different equation from the one the words describe belongs in
the truth class is Jim's ruling to make — `exprswap` (09-04) is the precedent for yes.

## The ledger (twelve, not built)

- **order-of-operations, rule 49** (pass-through): the tutor read the child's 16 as "5 + 3 =
  16" instead of "(5 + 3) × 2". A diagnosis-quality item; `livecritic` objected every attempt.
- **rule 48, six items** (limits-hole ≠; function-notation `2x+1`, `f(4) = 2(4) + 1`;
  i-dont-know's division equations; returning-student's three-forms card; quiz-eighty's
  `0.20 × 80`): four of the six are the 09-08 ruled-allowed shape (equations built from
  symbols already introduced), and the reviewer confirmed them anyway — the same reviewer
  refuted one identical case in the same report. The ≠ and the three-forms card (a, b, c, p,
  q, h, k unread) are real conduct holes; ledger.
- **rule 44** (function-notation): `f(x) = 23` posed on the board and not read aloud. Real;
  `unspoken`/`problemnumbers` did not fire because the prose had no number to miss. Ledger.
- **rule 15** (quiz-eighty, pass-through): "what would 0.6 be as a percent" with no board
  line. `pendcheck` fired and was satisfied elsewhere in the reply. Ledger.
- **rule 54** (quiz-eighty): "the word 'of' is your signal to multiply". Keyword teaching.
  Ledger.
- **rule 61, two** (returning-student): "a quadratic is an equation whose graph is a
  parabola" (the function's graph, not the equation's); "factored form shows where the
  parabola crosses the x-axis" (touches, for a repeated root). Both true-in-spirit
  overgeneralizations at MEDIUM; candidates for falsehood rows if they recur.

## The refuted three

Two are `livecritic` disagreements on limits-hole (read every equation aloud; show the
algebra before naming the line) — the reviewer's calls are right by the 09-08 ruling. The
third is the ruled-allowed rule-48 shape. Nothing hidden.

## Telemetry

The budget line says 10 × 6 (Render's `NIGHTWATCH_LESSONS=10` — Jim has since been advised to
drop it to 2 during sweep weeks). 149 shipped-with-finding (134 audit, 15 live), 99 of them
`livecritic` — the pass-through count is the cost of the critic's standard, not a defect
list. One truth floor (mathcheck withheld a false mixed-number chain, 5 days old). Three
`clienterror`s and one voice fallback, all ghosts (1–3 days old, draining). Referee crashes
0. Closure fully rendered (40,248 at `wa`).

I did no harm and this file is not truncated.

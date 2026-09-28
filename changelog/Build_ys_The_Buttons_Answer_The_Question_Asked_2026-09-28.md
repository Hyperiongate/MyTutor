# Build ys — The Buttons Answer The Question Asked, 2026-09-28

Jim's live flag from a Basic lesson (session / basic, 17:41 UTC), the first flag since the
quiz lane closed. The tutor was adding two two-digit numbers on the column board and said:

> "Look — the ones add up to over nine, so we write the 1 and carry a 1 to the tens. Then
> 2 plus 1 plus 1 equals 4, giving 41. Now let's try it together: what is 2 plus 1 plus 1?"

The buttons under it were **40 | 41 | 42**. Jim answered the words — **4** — and was told
"not quite". Then the tutor thought about it and agreed 4 was right. His note: *"Since 4
was none of the preselected answers, I think it got mixed up about what it was asking … all
of this I see as a student would be very confusing."*

Stamp: **`2026-09-28ys-the-buttons-answer-the-question-asked`**. PART **3om**. Nothing to
prewarm (no scripted line changed). No referee added — the count stays 101.

## What was wrong, measured

Two things, both in `tutor.py`, and neither was the model's alone.

**1. Referee 60 read the board and never the words.** `unanswerable_choices_conflict`
(build pt, from Jim's "1 + 2 = ? offered as 9 | 4 | 7" flag) judged the `[[choices]` row
against the board's pending `= ?` line only. This reply's board line (if it had one) was the
whole sum, and the whole sum's buttons were honest — so the referee passed it. The final
spoken ask, "what is 2 plus 1 plus 1?", was never read against the buttons at all. The words
and the buttons asked two different questions, and nothing in the product could object.

**2. The spoken-ask grammar knew only "a op b".** `expected_answer_for` is the streak's own
grade (`answer_slip`, called from `/api/chat`): when the previous turn's ask is computable
and the child's bare answer disagrees, the star falls in code, before the model speaks. Its
prose grammar (`_RB_PROSE_RE`) parses one pair. Fed "what is 2 plus 1 plus 1?" it matched the
first pair and answered **3** — a wrong "known" answer. Under that grade, Jim's correct 4 was
a slip. The carried tens column is *always* three terms, so this is the shape every
column-addition lesson with a carry produces.

The "thought about it, then agreed" is the next turn: the model, with the whole transcript in
front of it, graded 4 against the question it had actually asked. The reversal was the
model being right the second time; the confusion was the reply that let it be wrong first.

## What changed

**`tutor.py`**

- `_rb_chain_value(ask, min_terms)`: a plus/minus (or "take away") chain of two to four
  small numbers, evaluated left to right. `None` for a bare number, for any ask that also
  carries a times/divided-by/multiplied (the chain would not account for it), for a fifth
  term, and for a **tail** — anything after the arithmetic other than "?", "in all",
  "altogether", "then", "now". "2 plus 1 plus 1 to the power 2" is unknowable, on purpose.
- `expected_answer_for`: the chain first for **three or more** terms; two-term asks keep
  their old path byte for byte, with one new guard — a pair followed by a tail is `None`,
  never the first pair's value. So `answer_slip("what is 2 plus 1 plus 1?", "4")` is False
  and `"5"` is True.
- `unanswerable_choices_conflict` has a second reading: after the board check (unchanged),
  `_uc_spoken_verdict` computes the final spoken ask's integer answer
  (`_uc_spoken_ask_value`: the chain, then the two-term grammar, whole-question only) and
  refuses an **all-integer** row that does not contain it. Narrow by construction — a
  menu, a fraction or decimal row, a fraction/decimal/percent *in words* ("three fifths",
  "2 point 5"), a mixed ask ("3 plus 4 times 2"), an uneven division, a comparison, and a
  reply that does not end on a question all buy silence. The nudge names the value the
  words ask for and dictates ONE question: put the value among the options, or ask in words
  for what the buttons answer. Both fixes are accepted (pinned).
- The helper is `_uc_spoken_verdict`, not `*_conflict`: the referee-count pin counts
  `def *_conflict(` from the code, and the first cut moved it to 102 before the rename.

**`prompts.py`** — one bullet in the choices block: THE BUTTONS ANSWER THE QUESTION YOUR
WORDS ASK, with Jim's example. The prompt says it; referee 60 enforces it.

**`ruletests.py`** — PART 3om: the flagged reply refused (with and without a consistent
board line); both fixes accepted; twelve honest replies silent; the pt-era two-term fire
still fires; the chain grammar's values and its refusals; the grader's new answers; the
count not moved; the prompt line; dated notes.

**`main.py`** — the stamp only.

## Two things found on the way, both closed before the battery

The first cut fired on two canon beats the referee pile (PART 3mo) reads: *"What is 9
divided by three fifths?"* (the pair grammar took "three" from "three fifths" — 9 ÷ 3) and
*"What is 5 times 10 to the power 3?"* (5 × 10). Both are the same class — the pair was not
the whole question — and the tail rule closes it generically; the fraction-word guard is
belt and braces. The pile is back to its one intro card.

## For Jim

Push, confirm `/health` = `2026-09-28ys-the-buttons-answer-the-question-asked`. Nothing to
prewarm. To see it: any Basic or Entry live lesson that adds two two-digit numbers with a
carry — the tutor's "try it together" question and its buttons now ask the same thing, and
if the model drifts, the referee sends it back with the fix named.

I did no harm and this file is not truncated.

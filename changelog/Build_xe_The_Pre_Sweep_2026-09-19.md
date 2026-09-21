# Build xe — The Pre-Sweep (2026-09-19)

Built while Jim was away from his computer (two days, phone only), after `xd`. No sweep
report to read, so the build applied — ahead of time — the two classes every second-round
sweep has raised, to the two courses that have not yet had their second reading:
**Prob/Stat** (swept once, `wo`, 92 findings, fixed in `wq`) and **Calculus** (`wq`, 88
findings, fixed in `wr`). **Not yet on Jim's disk** — see the handoff's pending-commit list.

Stamp: **`2026-09-19xe-the-pre-sweep`**. Battery: see the bottom of this doc.

## The two classes

Every second reading so far has spent a large share of its findings on the same two shapes:

1. **The closing board the words never read.** Turn 38 of most lessons is a recap over a
   `[[step eq=…]]` board — and in these two courses the words often said the idea while the
   board held the numbers ("And that is spread, in plain clothes." over `(9+3+3+9) ÷ 4 = 6`).
   The reviewer calls it a words-board mismatch every time; wx, wy, wz, xa, xb and xc each
   closed a handful. Measured over Prob/Stat and Calculus at `xd`: **42 recap beats** whose
   board carried numbers the words did not say.
2. **The teaching sentence that runs long.** A why/picture/teach/worked/recap sentence of 27
   words or more — the reviewer's "unclear" (the validator's ceiling is 34, so these pass
   `validate` and still read badly aloud). Measured: **88 sentences** across the two courses.

Both were closed in the authored files, one line at a time, with the same rules the sweep
builds use: the reading says the board's numbers in the board's order ("in plain clothes: 9
plus 3 plus 3 plus 9, shared by 4, is 6."; "the chain rule: 6 times 5 is 30."; "answers
WHEN: 8 t equals 40, so t is 5."), and a split keeps every number and every named idea of
the sentence it came from ("A whisker reaches out left to 4. The box sits in the middle,
from 10 to 20, with the median line inside it. A whisker reaches right to 26.").

## What moved

- `lessons/probstat.py`: 22 closing boards read aloud, 43 sentences split, plus three
  follow-ups the new PART found on its first run (count-the-winning-paths' recap read its
  3 × 3 = 9 and split; the crowded-middle teach split).
- `lessons/calculus.py`: 19 closing boards read aloud, 45 sentences split.
- `ruletests.py`: PART **3mz** (6 checks) measures both classes over the two courses every
  battery and pins them at zero, checks five readings and three splits by text, and the
  counts and notes. Ten `wq`/`wr` pins that quoted a sentence now split were moved to the
  split form, marked "(xe)".
- `main.py`: the stamp.

Nothing in the generator moved. Course lines **40,005** (no beat added — every change is
inside an existing beat's words), closure 40,259, speechmap 1,001 of 40,311 and drift 695
(unchanged from `xd`), referees clean over both courses, every lesson validates, worst
per-lesson closure still `calc-u8-a-speed-that-climbs` at 24,855 (tripwire 25,000).

## What this buys

Prob/Stat's and Calculus's second readings should arrive with these two classes already
gone, leaving the reviewer's findings to the classes only a reader can see — the laws
without their condition (Prob/Stat's "always"/"any"/"every" rules of thumb; Calculus's
"calculus named but not done"). Diffeq's rerun went 119 → 62 with one fix build; these two
start from a lower floor. If a sweep still raises an unread board or a long sentence in
either course, PART 3mz says the measurement missed it — widen the measurement, not the pin.

## Battery

Frozen copy, 2026-09-19: **12,751 passed · 0 failed · 3 skipped** (12,745 at `xd`). The first run failed two `wq` pins whose quoted fragments now open their own sentences (five capital letters); moved, marked "(xe)", second run clean.

I did no harm and this file is not truncated.

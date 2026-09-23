# Build xo — The Forty-Eight Get Their Walk-Back (Phase C), 2026-09-22

Stamp: **`2026-09-22xo-the-forty-eight-get-their-walk-back`**. PART **3nj**. The third gate
build of the alternating schedule the 09-22 deep dive set (watch policy `xl` → the miss has a
face `xn` → **Phase C**). Built on Jim's word: "Algebra one sweep is running now. Go ahead and
start phase two C."

## What was wrong

Phase A (`vz`, 09-14) put the scripted second explanation into the engine: a first miss gets a
second look, the walk-back, a fresh problem of the same shape, and the ask again; only a
second miss in a row opens the AI's door. The engine guards that path with
`_worked_for(p) is not None` — an op with no worked picture keeps its old path, and the first
miss goes straight to the AI. Forty-eight lessons sat behind that guard: the 12 Entry lessons
of units 1, 8 and 9 (counting, the clock, shapes and patterns) and **all 36 of Diffeq**, because
their 51 ops had no `worked` generator. PART 3lu pinned it honestly at the time — "the two sets
were the same 48" — and the deep dive found it unmoved eight days later.

Two consequences. A student who missed once in those lessons was handed to the model at
once, with no scripted second try. And the course sweep, which simulates a miss only where a
worked picture exists, had **never read the miss path of either course** — Diffeq's two readings
(119 → 62 findings) were readings of the teach beats and praises only.

## The build

**51 worked generators** in `lessonscripts.py`, one `_<op>_worked(p)` each, in a block before
`BASE_WORKED` headed "PHASE C (build xo, 2026-09-22) -- THE FORTY-EIGHT GET THEIR WALK-BACK",
wired as `"worked"` in each op's `OP_EXT` entry (marked `(xo)`). Entry's 13: `big c20 cnt aft
bef sid cor pat grp eqs hrl min5 min5q`. Diffeq's 38: `dwd cube slpf slpq isoc fldc sepv sepr
newt conc logi carr fast away eulr estp rk4 evls char cdmp natf oscf part trns reso damp lder
lalg lshf lfin sysx nucl detm eign lnrz prey cycl chao`.

Every one is in the canon's shape, and PART 3nj reads all 581 problems' walk-backs to prove
it: the opener literal `Here it is, step by step: ` with lower-case after the colon; every
sentence under 27 words (nine first sentences were split at a full stop after the opener — sid,
grp, eqs, lshf, lnrz, chao, estp, rk4, sysx); one thought per board line, no `[[step eq]]`
joining two equations with the dot (sepv's chain became separate steps); no arrow after an
equals sign and no unit after an equation's answer (min5q, natf, part and conc were reshaped
after the referee refused them); "equals" not "makes", "take away" not "subtract",
`_plural` for "1 star"; the common wrong path crossed out on the board where the words name it
(newt: `75 ✗ the gap, not the rate`).

**The 36 Diffeq praises are credit lines.** Two Diffeq ops already were; the other 36 taught
in the praise — the cooling law, what UNSTABLE means, why a few halvings beat a thousand Euler
steps — and with a walk-back now playing right after the praise (`show_work_on_correct`), the
student would have heard the teaching twice in one breath (the xk class, 3nf). Each is now the
answer and its one reason (marked `(xo) a credit line`), none over 26 words, and **every idea
the old praise carried moved into the walk-back**, including the thirteen condition phrases
PARTs 3mk and 3mn pin (cdmp's "a hair less on that term and the door crawls", away's
"Moving away from the balance point is what UNSTABLE means", newt's creeping coffee, chao's
wrecked forecast, prey's rabbits "held level by that many foxes", isoc's isocline, estp's
"main error shrinks in step with the step", rk4's halvings, lder's "turns differentiating into
timesing by s", natf's "many objects have natural frequencies", sysx's x part of the arrow,
char's "that one number decides", lnrz's straight-line estimate). Those pins now read
`W({...})[0]` instead of `PR(...)`. 3mk gained `W`; 3mn had been reading `W` without defining
it and gained it too.

**The 48 lessons carry `"show_work_on_correct": True`** (`lessons/entry.py`, `lessons/diffeq.py`,
each marked `(xo)`), so a right answer is walked back like every other lesson. No authored
line in either course changed.

**No engine change.** The guard stands for any future op added without a picture; the vz
pin that used to prove counting-to-10 was behind it now proves that a made-up op reads as
None, that the guard is still in the source, and that counting-to-10's first miss is the
engine's. Nothing was stripped.

## Proven

- The engine: on `diffeq-u2-the-cooling-cup`, `diffeq-u9-a-perfectly-known-equation`,
  `entry-u1-counting-to-10` and `entry-u9-sharing-fairly` the first miss plays
  `["say", "say", "say", "ask"]` with zero interventions and the second beat opening on the
  literal; the second miss in a row still intervenes; a right Diffeq answer plays the credit
  line and then the walk-back.
- The sweep: the transcripts of Diffeq and Entry now carry **216 walk-backs each** (none
  before). The canon's referees (`T.prose_board_conflict` over every beat) refuse none of
  them; canon-wide the refusals are still the one known intro card.
- The five pre-sweep measures (unread closing board, long authored sentence, praise over 26
  words, spoken beat ≥27 words, praise repeating the walk-back) all read **zero** on the new
  text; `pinscan` 0 misses; all 51 boards rendered headless in `demo-lesson.html` with no
  warning (`render_xo.py`); every lesson validates.
- Counts: course lines **39,915 → 40,495**, closure 40,749, speechmap **941 of 40,801**,
  drift 635. Count pins replaced blanket-wide; four world-model pins rewritten (3lu's
  "48 and 48" → 0 and 0; the vz guard pin; wc's equal-groups answered-line test now runs on
  a copy with the flag off; ww's chao pin expects a walk-back). The first frozen run
  failed four pins in 3ix (Entry Unit 1 "quick praise, ruling ⑤" expected NO flag): uw's
  ruling ties the walk-back flag to the picture, not the unit, and the quick praise itself
  is untouched — the caller now passes `worked_ids=U1`, and 3ks's "the flag matches whether
  the op has a picture" pins agree without change. The second run failed one more world-model
  pin, 3lv's "311 lessons read the second explanation" — 359 now (every lesson but the
  table pass); moved with an (xo) mark. Third run clean.
- Battery on the frozen copy: **12,883 passed · 0 failed · 3 skipped** (12,865 at xn).

## Grading, per the 09-22 ruling

Not a sweep finding — a gate build. Class: the miss path missing from two courses (48
lessons, 51 ops). Closed canon-wide: no lesson is behind the guard, pinned at zero by 3lu and
3nj.

## After the push

`/health` = `2026-09-22xo-the-forty-eight-get-their-walk-back`. **Prewarm** is the largest
since the sweeps began: the 580 new walk-back lines plus the 36 Diffeq credit lines under their
three praise prefixes — about **2,000 lines**. Then **Diffeq's third reading** is the first
that can see its miss path; expect its findings to rise before they fall, and read the
walk-back findings as one class per op (generator-owned, one fix each).

## Files

`lessonscripts.py`, `lessons/entry.py`, `lessons/diffeq.py`, `ruletests.py` (PART 3nj),
`speechmap.py` (regenerated), `main.py` (stamp), this doc, the refreshed
`START_HERE_Handoff_2026-09-22.md`.

I did no harm and this file is not truncated.

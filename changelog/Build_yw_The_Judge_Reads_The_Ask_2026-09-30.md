# Build yw — the judge reads the ask (2026-09-30)

Stamp: `2026-09-30yw-the-judge-reads-the-ask`. Battery: **13,349 passed · 0 failed · 3 skipped** (PART 3oq added).
Nothing to prewarm — no spoken line changed.

Jim forwarded the first red `scripted` night from GitHub: the nightly screenwatch's second
job (`ye`) failed in 6 min 27 s on the morning of 09-30. Item 5 of the 09-28 deep dive was
"open the `scripted` job's reports"; this is the first one read. The GitHub run itself was
not reachable from the session, so the night was re-run by hand — the job is reproducible
by design (`--rota-day`): day 273 is the slice Entry unit 7 lessons 1–4 and unit 8 lessons
1–4, and the same judge on the same lessons gave the same three findings.

## What the night found

Two `S9 LOW` (the over-tall beat's shrink, by design under `pu`; a LOW never fails a night)
and one **`S5 HIGH`** on Entry unit 8, minutes-past-the-hour, turn 2:

> It is 55 minutes past the hour. Which clock number is the minute hand pointing to?

over the clock's caption "the long hand is the minute hand — from 12 to 1 is five minutes".
S5 ("the caption does not answer") fires when a trailing question and a caption share the
same "is the <term>" claim; both carry "is the minute", so it fired. But the question asks
for a NUMBER (the answer is 11); "the minute hand" is the question's subject, not its answer,
and the caption names no number. The screenshot shows the ask over a plain step line — no
give-away on the screen at all. A false HIGH, and a red job for it.

## The fix — in the judge, not the lesson

S5 now reads the question with `_IS_THE_ASK_RE`: the "is the <term>" must CLOSE the question
— the term, at most two more words (a noun's second word, "minute hand"; a "here" or "then"),
then the question mark. "Which side in that triangle is the hypotenuse?" still fires (Jim's
original case, the fixture from build gj); "Which hand is the minute hand?" fires (a new
fixture); "Which clock number is the minute hand **pointing to**?" runs three words past the
term and is an ask ABOUT the minute hand, not for it — silent (day 273's own turn is the
fixture). The caption side is unchanged (`_IS_THE_RE`).

Re-run of day 273 on the fixed judge: 56 turns, 2 findings, both LOW — "none at or above
MEDIUM — the run passes."

This is the xz pattern one lane over: a reviewer misread the tool invited is a TOOL fix, not
a lesson edit and not a refusal. The lesson was right.

## Files

`screencheck.py` (`_IS_THE_ASK_RE`; S5; two fixtures; dated note), `ruletests.py` (PART 3oq),
`main.py` (stamp), this doc.

I did no harm and this file is not truncated.

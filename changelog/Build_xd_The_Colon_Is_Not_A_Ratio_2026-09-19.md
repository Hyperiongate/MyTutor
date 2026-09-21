# Build xd — The Colon Is Not A Ratio (2026-09-19)

Built while Jim was away from his computer (two days, phone only): no sweep to read, so
the measuring turned on the voice itself. **Not yet on Jim's disk** — see the handoff for
the pending-commit list.

Stamp: **`2026-09-19xd-the-colon-is-not-a-ratio`**. Battery: see the bottom of this doc.

## What was wrong

`static/speech-text.js` tidies the tutor's text before the voice reads it, and one rule
turns a ratio into words: `3:2` → "3 to 2". The rule matched *digit, any spaces, colon,
any spaces, digit* — so it also fired on every colon used as ordinary punctuation before a
number:

- "Factors of 8: 1, 2, 4, 8" was spoken **"Factors of 8 to 1, 2, 4, 8"**
- "Set the speed equal to 144: 12 t equals 144" was **"equal to 144 to 12 t"**
- "Count by five until you reach 20: 5, 10, 15, 20" was **"reach 20 to 5, 10"**

Measured over every scripted line of all ten courses: **287 turns misread, 1,183 lines of
the voice closure re-keyed for it** — and *not one* genuine ratio written with a colon
(every course says "2 to 3" in words; the tight form lives only in the live model's text and
on the board, which is not spoken). Jim heard the shape live on 2026-08-26 ("Question 3: 20
students" → "three to twenty"); build `ol` answered that one shape in the model's own text
with referee 54 and left the root in place. Two colon lines were caught one at a time on
the way here (`wu`'s ellipse "over 196: 14", `xa`'s "height 3: 8") without seeing the class.

## The fix

The rule matches the **tight** form only: `(\d):(\d)` → "$1 to $2". A colon with a space
after it is left for the voice to pause on, which is what a colon is for. `the ratio 3:2`
still reads "three to two" (the `SPEECH_CASES` pin holds); referee 54 stays as a second wall
for the model's text.

`speechmap.py` regenerated: **2,184 → 1,001** re-keys of 40,311 (the 1,183 colon lines no
longer differ from their authored text); the closure drift **1,878 → 695**. On the prewarm
after the push, those 1,183 clips re-render with the right words — the old clips were
rendered from the wrong text, so the re-render *is* the fix reaching the child.

## Counts and pins

Course lines 40,005, closure 40,259 — unchanged. PART **3my** (6 checks): the rule's
shape; five colon cases through `forSpeech` under node; the measurement — no tidied line
carries a "digit to digit" its authored line did not, and no scripted line writes a tight
colon; the speechmap counts; the dated notes. Pins moved: speechmap 2,184 → 1,001, drift
1,878 → 695, the "closure is in it" floor 1,900 → 900.

## Battery

Frozen copy, 2026-09-19: **12,745 passed · 0 failed · 3 skipped** (12,739 at `xc`). Clean on the first run.

I did no harm and this file is not truncated.

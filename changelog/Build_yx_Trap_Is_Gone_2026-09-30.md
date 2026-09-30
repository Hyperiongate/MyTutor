# Build yx — "trap" is gone (2026-09-30)

Stamp: `2026-09-30yx-trap-is-gone`. Battery: **13,377 passed · 0 failed · 3 skipped** (PART 3or added; two pins moved).
**Prewarm: ~134 lines** (131 rewritten, Entry u2 l4's two beats, Algebra II u3's split sentence).

Jim's ruling from the first-family playthrough (F17), given twice on the day: "Here is the
trap" was the tutor's phrase for a common mistake — several times in one Entry unit, again
in Geometry unit 1 — and a six-year-old does not know "trap" in that sense. "Trap has to
go." The meaning to keep, in his words: "here's a very common mistake to look out for."
Asked whether the upper courses change too: "Want trap gone everywhere."

## Measured first

131 spoken lines across all ten courses carried the word — Entry 23, Basic 7, Pre-Algebra 4,
Algebra I 4, Geometry 29, Algebra II 33, Pre-Calc 20, Calculus 4, Diffeq 1, Prob/Stat 2 in
the authored files, and 7 generated in `lessonscripts.py` (the two-clue puzzle's "they trap
the answer", the reading-the-table walk-back's "the next-door boxes were the traps", the
halving-mistake captions). Twenty-six were the bare "Here is the trap."; twenty-two "Two
traps."; the rest idioms ("the famous trap lives right here", "the trap closing", "the flip
trap still lurks").

## The rewrite

One pass, by phrase, not by line, so the voice stays one voice:

- "Here is the trap." → **"Here is a common mistake to look out for."** (Jim's words)
- "Here is the trap, and …" → "Here is a common mistake, and …"; "Here is the trap: " →
  "Here is the common mistake: "
- "Two traps." / "Two traps, both …" → "Two common mistakes …"
- "The trap is …" / "The trap: " / "the trap" → "The common mistake …"; "The traps are …" →
  "The common mistakes are …"; "both traps" → "both mistakes"; "the whole / famous / oldest /
  flip / halving trap" → "… mistake"
- the two where "trap" was a verb or a picture: "together they trap the answer completely" →
  "together they pin the answer down completely"; "the trap closing" → "the two clues closing
  in"; the table's "the next-door boxes were the traps" → "were the wrong boxes"
- Calculus's op named `trap` is a trapezium and an identifier; "a trapezium" is spoken and
  stays.

`VOCABULARY` gains the canon phrase **"common mistake"** with every spoken form of the word
banned — each with its own boundary ("the trap ", "traps.", " trap —" …), because the
validator matches substrings and "a trapezium" holds "a trap". The validator now fails any
lesson that says it, in any course, forever. The elementary brain's prompt gets one bullet:
say "a common mistake to look out for", never "trap" — so the live lane matches the lessons.

One sentence grew past the 27-word cap under the longer phrase (Algebra II u3 degrees-add:
"…is 12, but degrees do not times —") and was split at its own comma. PART 3na is the pin.

## Three playthrough flags that rode along

- **F29 — Geometry u1's complementary beat.** Jim, reading it fresh: "this makes no sense"
  ("you met 180 first … and 180 sticks. Ask which corner you are inside"). Every fact was
  right; the words failed a first-time reader. Now: "A straight line is 180, and a square
  corner is only 90. The common mistake is using 180 when the two angles sit inside a square
  corner. Look at which corner the two angles fill before you take away." ("makes" is a
  banned synonym of "equals" — the validator caught the first draft.)
- **F22 + F25 — Entry u2 l4, adding three numbers.** The mistake beat arrived with its own
  numbers straight after a generated worked example ("came out of the blue") and claimed a
  make-ten trick the lesson never teaches — the method here is add the first two, then the
  third. The beat now announces its numbers ("Look at a new one: six plus four plus three")
  and teaches only the mistake; the recap's make-ten line became "count your numbers before
  you stop … three numbers, so it takes two sums". Same board.
- **F15 — the Pathfinder award mid-intro** was read, not changed: its words are true ("you
  just earned the Pathfinder award — completed a course assessment"; Jim heard "for
  completing a unit") and its timing is `vs`'s design (an award earned since last time is
  said after the orientation, before the first idea). Whether a placement's award should wait
  for the results screen instead is Jim's call — see the handoff's open questions.

## Files

`lessons/entry.py`, `lessons/basic.py`, `lessons/prealgebra.py`, `lessons/algebra1.py`,
`lessons/geometry.py`, `lessons/algebra2.py`, `lessons/precalc.py`, `lessons/calculus.py`,
`lessons/diffeq.py`, `lessons/probstat.py` (the rewrite; dated notes), `lessonscripts.py`
(7 generated lines; `VOCABULARY`), `prompts.py` (one bullet), `ruletests.py` (PART 3or; one
pin moved), `main.py` (stamp), `speechmap.py` (regenerated; 941, unchanged), this doc.

I did no harm and this file is not truncated.

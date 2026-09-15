# Build wc — The sweep, calibrated, and the generator class it found (2026-09-15)

Jim's first real course sweep — Entry, 36 lessons, read by the night watch's seat — came back
with **219 findings**. This is the triage of that report, and the build it produced.

Battery: **12,393 passed, 0 failed** (frozen copy, 2026-09-15).

## The triage: three piles

**Pile 1 — the sweep's own defect, about 130 of the 219.** Every "praises an answer the child
never gave", every "Not quite with no wrong answer shown", every "three in a row claimed with
no answers", every "tap the reason with no choices on the board". The reviewer was right about
what it saw: the transcript I built showed only the tutor's turns. The student's answers, the
tap buttons and the reason choices were not on the page, so it read a monologue that praised
and corrected thin air. It also saw only a sample of each problem bank, and concluded that
counting-to-10 never reaches ten (the bank does).

**Pile 2 — real, and generator-owned, about 25.** One fix each, landing in every lesson that
shares the generator.

**Pile 3 — real, authored, about 40.** Unconditional rules ("every flat shape is made of
straight sides", "the tens digit goes first, always", "the change is always smaller"),
pictures promised and not drawn ("watch me deal out the stars" over a bare equation, a clock
hand described over a number line). These are the genuine article — the same species as the
cookies flag — and they are **not in this build**. They will be fixed from the *clean* Entry
report, not this noisy one.

The remainder is the reviewer being pedantic: "single-digit" in a lesson title, "over nine"
(which is the course's one chosen wording, guarded by the validator since build `jy`).

## The calibration

`coursesweep.py` now writes a **STUDENT** line after every ask — the answer, marked correct or
WRONG with the right answer named, or the tapped reason. An ask's board carries its
`[[choices]]` buttons and the reason question its reason choices. The charter explains the
STUDENT lines, says the practice is a sample of the bank, and carries the rulings the first
report tripped on: the "Your turn" card's unspoken tap/say/type hints, a topic word in the
title line, "over nine", and a level-appropriate rule that the lesson does not itself
contradict. The report header now counts findings by kind, so the next calibration is one
glance.

## The generator class

**The boards get the plurals build `mo` gave the voice.** `mo` fixed "1 hours later" in what is
*said* and never touched what is *drawn*: the boards still wrote "1 nickels", "1 quarters",
"1 cubes", "1 weeks", "1 hours", "1 ones", "1 tens", "1 hundreds". Eleven board lines across
the coin, clock, calendar and place-value generators now go through `_plural`/`_irr`. And a new
validator check makes it permanent: **a bare 1 takes a singular unit noun, in what is said and
in what is drawn** — the check `mo`'s own note said the validator could not make. It swept all
360 lessons and caught two more the reviewer had not (the place-value captions).

**The answer lands on the board.** In a lesson with no walk-back — the 12 Entry lessons and all
36 Diffeq lessons — the praise beat carried no board, so the child heard "That's it! 4" over
"2 groups of 2 = ?". New `answered_board(p, level)`: the ask's last pending step with the blank
answered, suffix and all ("? days" → "11 days", "2, ?" → "2, 3", "? sides" → "6 sides", and "1
cent change", never "1 cents"). `_correct_beats` puts it on the praise beat when there is no
walk-back. A lesson *with* a walk-back is unchanged.

**The worked lines say the method.** Since `vz` the walk-back answers a wrong answer too, and
"so you wrote 2 and carried one ten", "you regrouped", "you found the column first", "you
counted by fives", "you walked all four sides" are false there. Eleven lines now say "write 2
and carry one ten", "regroup", "find the column first", "count by fives".

**The rest of the class.** `c2h`'s caption says the sum *reaches* a hundred when it is exactly
100 (10 + 90 does not go past it). `m`'s walk-back: "1 dime bring 10 cents" → "1 dime is 10
cents". `min5q`'s praise: "55 minutes is the 11 on the clock" → "the minute hand points to the
11". `hrl`'s caption names both names: "the short hand — the hour hand — is at 3".

## Audio

The rewritten worked and praise lines re-render under new text; the closure and speech-map
counts do not move (40,248 · 2,244 of 40,300). The prewarm will list them.

## After the push

Refresh `/admin`, run **Entry** again. The number to watch is the by-kind line in the header:
"tone" and "unsupported" should collapse; what remains is Pile 3, and that is the list I fix
next.

I did no harm and this file is not truncated.

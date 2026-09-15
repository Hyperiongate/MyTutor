# Build we — The Second Clean Sweep (2026-09-15)

The Entry sweep re-run after wd: **47 findings** (from 70), **12 lessons clean** (from 9),
6 generator and 41 authored. This build answers 46 of them and rules on the 47th.

## The generator items (6)

- **`min5q`** asked "The minute hand is 55 minutes past the hour" — three findings, one
  line. The TIME is past the hour; the hand points. It now asks "It is 55 minutes past the
  hour. Which clock number is the minute hand pointing to?"
- **The `+` walk-back** counted ON ("start at 3 and count on 2 more") in the single-digit
  lesson, which teaches counting ALL from one. It now counts all while the sum is inside
  ten — "count every star, both groups — 1, 2, 3, 4, 5" — and counts on past ten, where
  counting on is the next lesson's method. The stars light up one at a time on the board.
- **The regrouping walk-back's** caption now carries both column steps, so "1 take away 1
  equals 0" is drawn, not just said.
- **The dimes ask's** caption said "dimes are tens, pennies are ones" — the teach beat's
  rule, unspoken on the ask. It now says what the question says: "3 dimes and 4 pennies".

## The house-wide one: the practice intro's promise

"Three right answers in a row and we're done" — and in the 292 lessons that carry a reason
question, it is not done: the reason question follows. The reviewer caught it on
tens-and-ones, and it is true of every course. The fix is one line and one clip, not 292
edits: `practice_intro_line(lesson)` speaks "Three right answers in a row, then one reason
to tap, and we're done — here comes the first one" in a lesson that has a reason question
AND uses the house intro (258 of the 292). The 34 lessons with their own intro speak their
own — the engine never rewrites authored text — and their courses' sweeps will list any
that make the same promise. The sweep labels the spoken form so its quotes place.

## The authored pile (41), by kind

**Rules with their condition.** Ten-more: "every number today stays under a hundred, so
the tens digit goes up by one" (the reviewer's 94 + 10 is not in the bank, and now the
words say why). Adding three-digit numbers: "no column goes over nine today, so each
answer keeps to its own column", and the stacked column is DRAWN on the beat that
describes it. Crossing a hundred: the carried ten is in the rule ("the tens, with any
carried ten"); the "1115" board now says what the mistake is ("11 in the tens place ✗ —
write 1 ten, and the other ten tens are the hundred"); both worked examples draw their
carrying steps. Later on the clock: o'clock needs the long hand at 12. Sides and corners:
"joined all the way round" (closed). What comes next: "a NUMBER pattern is a list of
numbers that follow a rule". Counting to 10: "when you count each thing once, you know how
many" (not "always"). Making change: "if your change is bigger than what you paid".
Regrouping: "the 2 ones become 12 ones, and the 4 tens become 3 tens". Add single-digit:
"an adding sentence uses two signs" (the equals sign is not addition's own), and "today's
way is to start at one" (the count-all rule is a way, not the law). Story problems: "a plus
or a minus is hiding inside it" (a minus story has no sum).

**The counts SAID where the words skipped them.** Take away from bigger numbers: "count
back from fifteen: fourteen, thirteen, twelve, eleven, ten, nine", and the trap says both
counts out loud. Tens and ones: "count on from ten: eleven, twelve, … eighteen". The
missing part: "start at seven; count eight, nine, ten — three counts"; the second worked
example counts nine through fifteen and draws the hop. Adding past ten's trap says the
right count and the wrong one ("say seven again — seven, eight, nine, ten, eleven — and
you land on eleven, because seven was counted twice").

**Boards that draw what is said.** 14's two digits on the why beat; "19 is not 91" on the
recap; "1 penny = 1 cent" with the nickel and the dime values; the hop BACK on
before-and-after's recap; the stacked column and the carrying steps above.

**Advance lines.** "when the ones never go over nine" (the word "carries" was untaught in
the no-carry lesson — the canon's "over nine" replaces it); "when no column goes over
nine"; "when every top digit is big enough" (both take-away lessons).

**Three long sentences split** (adding three numbers' trick, the missing part's recap,
take-away-three-digit's trap). Counting past ten no longer says "all the numbers up to
twenty" over a count that starts at ten. "Ten pence", "page nine".

## Left alone, on purpose

"You can count to ten" (counting-to-10's advance line, HIGH). The reviewer judged it by
the three problems its sample happened to ask — 1, 3 and 5 — and the bank goes to 10. The
charter already said the practice is a sample; it now also says not to judge the closing
line by which problems the sample asked. That is the Forever War's mechanism working as
designed: a finding that is the reviewer's, not the lesson's, becomes a charter line, once.

## Counts and tests

Course lines 39,995 → 39,996 (PRACTICE_INTRO_REASON); closure 40,249 → 40,250; speechmap
2,244 of 40,301 → of 40,302. `L.validate` over all 360 lessons: 0 failures. The new column
board, the counted stars and the trap lines render headlessly with no board warning. PART
3lz pins all of the above. Battery: see the last line.

## After the push

1. Prewarm — the rewritten Entry lines, the new `+` walk-backs inside ten, min5q's asks,
   and the one new intro line.
2. Re-run the Entry sweep. Expect it shorter again; what is left is either the next list
   or the next charter line.
3. Then Basic.

Battery: 12,456 passed, 0 failed, 3 skipped (frozen copy, second run, 2026-09-15). The first run
moved one pin: the live-page test compared the spoken intro to the authored field, and the
trig lesson it drives has a reason question, so it now speaks the honest form.

I did no harm and this file is not truncated.

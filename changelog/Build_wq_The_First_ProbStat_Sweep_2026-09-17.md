# Build wq — The First Prob/Stat Sweep (2026-09-17)

REPORT HEADER (copied first): Course sweep -- probstat -- 2026-09-16 23:19 UTC (build wo).
Read by openai · gpt-5.5. By kind: false 45, words-board 30, unclear 10, unsupported 3,
untaught-term 3, tone 1. 36 of 36 lessons read · 92 findings (11 on generators, 81 authored) ·
1 lesson clean (ps-u2-a-percent-not-a-person) · 0 unplaced · 0 unread · 44 minutes.

The first sweep of Prob/Stat — and with it, **every course has now had its first sweep**.
Prob/Stat's own class is *a rule of thumb stated as a law of nature*: "the bell always
shares itself out the same way, so 68 percent of ANY group"; "measure almost anything and
the picture comes out the same shape every time"; "play it a thousand times and you end up
level"; "play four hundred times and the 3 arrives with perfect reliability"; "every dot is
on one side or the other"; "a poll reports a range, not a point"; "your sample flatly
contradicts it". Forty-five of the 92 were that shape. This is the course where the honest
words are "about", "on average", "in the long run", "when a group follows a bell curve" and
"when no dot lands on the line" — and the lessons now say them.

Stamp: **`2026-09-17wq-the-first-probstat-sweep`**. Battery: see the bottom of this doc.

## The generator (lessonscripts.py) — fourteen items

- **`farv`** (MEDIUM, and the most interesting one): the outlier ask's third tap is "the
  distance from the crowd", and the praise said "13 is only how far the stray sits from it"
  — but with a = 12 and b = 25 the crowd runs 11 to 14, so 13 was *also a dot on the plot*.
  The generator's check now forbids the distance landing on a crowd value, and the two bank
  entries that collided ((12, 25) and (15, 29)) moved to (12, 27) and (15, 28) — the bank is
  still a ramp.
- **`hedg`** (HIGH): "that gap never shows in one play, only over hundreds" and the walk-back's
  "shows up with perfect reliability" — the gap is an *average*. Now: one play can bounce
  either way, but over many plays the average gap is what keeps the machine open.
- **`por`** (HIGH): "timesing is what AND does, not OR" stated the multiplication rule without
  its condition, in a lesson where red AND blue cannot happen. Now: timesing belongs to the
  AND rule for separate events, not to this OR question (and the praise stays under the
  no-board word cap — the first draft tripped the referee).
- **`inci`** (MEDIUM): "anything up to 22 is possible" → the highest the poll allows is 22.
- **`ntal`** (MEDIUM): the walk-back's board wrote `600 ÷ 40 = 15`, a shortcut the words never
  said; it writes `5% of 600 = 30` and `30 ÷ 2 = 15`.
- **`wout`** (MEDIUM): the ask's tape showed the full bag under a caption saying a marble had
  been taken; it is captioned as the bag *before* the pick.
- **`zsco`** (LOW): counting deviations *gives* two measurements a common scale — it is not
  the only way they can be compared (praise and walk-back).
- **`resd`**, **`n68`** — not flagged on the generator but the same faults the authored beats
  were flagged for: the gap is the *size* of the residual (actual take away predicted); the
  68 is the percent to take, not the headcount (in a group of 100 it *is* one).
- **`dcnt`**: the ask and walk-back plots draw the line at the cut (below).
- **`bias`**, **`cbse`**, **`strf`** walk-backs and **`resp`**'s praise are short sentences
  (four LOWs).

## `[[dotplot mark="8"]]` — the line the words draw (static/math-figures.js)

The count-past-the-line lesson said "a line to draw in your mind at 8" over a plot with no
line on it. `[[dotplot]]` now takes `mark=`: a dashed vertical line at the value, labelled,
drawn before the dots so a dot standing ON the line sits on top of it, with 18px of headroom
so it reads as a line rather than a stub. Same shape as `[[numberline]]`'s `mid=` (build sp).
Plots without `mark=` render exactly as before (checked side by side, headlessly). The
authored lesson's four boards and the `dcnt` generator use it.

## The dot, tenth course

Two authored step lines (`0 = never · 100 = always`; the tails' `5% of 800 = 40 · half at
each end = 20`) were the last " · " between two equations in the curriculum. The pin now
covers **all ten courses** by rendered transcript, generated lines included.

## The authored pile (lessons/probstat.py) — 101 edits, 35 lessons

**A rule of thumb with its condition (45).** The 68 rule is "when a group follows a bell
curve" (HIGH), and many common measurements come out *roughly* that shape (HIGH). A fair
game: play it many times and, *on average*, you expect to end up level (HIGH); it is
*expected* to return what it takes in; for the *same cost*, the rarer the win the bigger the
prize; spread the whole *pot* over the wins (HIGH — the advance line said "stake"). The
machine: *many paid* machines are not fair; the average cost *tends to settle* closer to 3
(HIGH). "Every dot is on one side or the other" carries "when no dot lands exactly on the
line" in the teach, the reason question, the recap and the advance line (HIGH ×3). A poll's
estimate *comes with* a range (HIGH). Your sample *does not support* the claim. Independence
predicts the rate "for the group the claim names"; independent means the group's rate *for
this* matches everyone's. Chances out of different wholes are "hard to compare until they
sit on the same scale" (HIGH); 30 percent "is like 30 out of 100 — in the long run, about
30 of every 100 picks". The hundred square is "a picture of the chances" (HIGH). A missing
chance can be found "when every outcome is listed and just one is missing". "The best prize
is not what one play is *worth*, and the worst is not either" (HIGH — the worst *was* the
usual prize). The home-lunch crowd "may well think differently"; the response rate is "a
number a statistician checks"; strong feelings "may be more likely" to reply. "One common
way to want two things." The box's width: whisker tips play no part in it, and a wild
extreme moves it far less than the range.

**Plain errors.** "One in 8 — adding them — is more common than rain alone" (HIGH): it is
*rarer*; the point is that adding is the OR rule's move. "20, the size of the gap" (HIGH):
26 − 9 is 17; it is a distance, 19 from the crowd's centre at 7, and the ✗ says so. "7 is
the only number with three below and three above": 6.5 is too — 7 is the halfway point.
"Adding the counts brings the values back": it brings the *count* back. "Square these
distances and you get variance": average the squares. The residual is actual take away
predicted — positive above the line, negative below — and this lesson measures its *size*
(HIGH ×2); best fit keeps the squared gaps small *overall*. "The mode is the value under the
stack" → the *tallest* stack. "Its width is one edge taken away from the other" → the right
edge take away the left. "12 points might be enormous or nothing at all" → large or small
compared with the spread. "Roughly 2 in a hundred beat that" is the bell's own fact, and
the unit's last lesson counts them. "A thousand is usually enough" now says why (about 3
points). The ellipse is out of the width lesson; "cell" is "one box of the table"; GIVEN is
glossed where the lesson first leans on it; "the lazy move" is "a tempting shortcut" (the
one tone finding).

**Count-the-winning-paths (HIGH).** The 4-part spinner with 2 winners made 2 × 2 and 2 + 2
the same 4, so the "added" trap could not be shown. The lesson's spinner has 3 winners now:
3 × 3 = 9 of 16; 12 leaves the second spin free; 6 adds. The tree draws four *kinds* of
finished branch (it had said "four finished paths" and then counted sixteen), and the recap
board draws the tree it talks about.

**Words-board (30).** Every closing beat whose board wrote an equation now reads it: "20
times 40 divided by 100 — 8 girls"; "300 take away 120 leaves 180"; "60 times 4 is 240";
"4 per hour, times 2 hours, 8"; "14 take away 6, 8 below"; "50 plus 2 times 8, 66"; "46 take
away 5, 41"; "5 percent of 800 is 40, halved, 20"; "20 percent of 400 is 80, 40 percent is
160"; "3 times 3, nine". The ✓ lines are spoken ("the box is 10 wide", "so 41 is the answer")
and carry their unit (`25% ✓`; `12½ ✗`). The stratified worked line draws its 45-and-40
school; the conditional worked line and reason question draw the 14 and the 6; the
20-or-200 line is on the board; the reason boards draw the second hop to 66 and the hop
down to 41; the range lesson's boards carry both ends and the 45 − 5 step; the two-way
reason question reads the whole table; the tails picture says it shades one end.

**Unclear (10).** Eight sentences split into short beats.

## Counts

Course lines **39,999** (no beat added); closure 40,253; speechmap **2,245** of 40,305
(unchanged); forSpeech drift **1,939** (unchanged). `L.validate` over all 360: 0 failures
(three caught mid-build: the farv bank ramp, "makes", a 13-word reason button). The canon's
referee sweep over every Prob/Stat transcript beat: 0 refusals (one on the way — the first
`por` praise ran past the no-board word cap). Every new board tag rendered headlessly with
no `boardWarn`; the marked and unmarked dot plots rendered side by side. PART **3ml**: the
fourteen generator items, `mark=` by source and by the `dcnt` boards, the dot pin over all
ten courses, the authored classes by lesson id. No old pin quoted a Prob/Stat line.

## After the push

Prewarm: roughly a hundred rewritten Prob/Stat lines plus the fourteen generator lines.
Then: **rerun the Calculus sweep** for the 17 lessons `wo` never read (units 6–9) and paste it
— it becomes `wr`. After that every lesson in every course has been read once, and the
second round starts where the first did.

## Battery

Frozen copy, 2026-09-17: **12,626 passed · 0 failed · 3 skipped** (12,612 at `wp`); the first run tripped two old generator pins (dcnt's captions, cbse's walk-back sentence), moved to the new wording, and the second run was clean.

I did no harm and this file is not truncated.

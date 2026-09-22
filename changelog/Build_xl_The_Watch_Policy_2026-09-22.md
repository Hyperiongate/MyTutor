# Build xl — The Watch Policy (2026-09-22)

Project 2 of the 09-14 deep dive, and the oldest unpaid item on every handoff since. Built
on Jim's word after the 09-22 deep dive found the night watch still running at ten lessons
a night with no report read since 09-15 — and the sweep, at $5.40 a course, doing the same
job better. This is the first gate build to interleave with the sweep rounds rather than
wait for them.

Stamp: **`2026-09-22xl-the-watch-policy`**. Battery: see the bottom.

## The policy, in code

Adopted 09-14, in prose. Now in `nightwatch.py`:

- **Truth-class and HIGH findings are ACTIONABLE.** They lead the report in full, under
  `## Actionable — truth-class or HIGH (n)`, with the `vg` tally and the Shipped-as lines
  they have always had.
- **Everything else goes to the ledger.** MEDIUM and LOW conduct findings are still
  confirmed, still recorded, still on the books — and print as one line each under
  `## To the ledger`, at the bottom. Their quotes and fixes live in the monthly view.
- **A night with nothing actionable says so in one line**, first:
  `## Nothing actionable tonight — 2 style/conduct finding(s) went to the ledger`.
- **The email wakes Jim for actionable findings only.** A ledger-only night is silence. A
  preflight failure still mails — a watch that could not run must never read as all-clear.
- **No new referee unless the finding is truth-class.** A rule for the reader, not the
  code; the report prints it on every page so the reader holds to it.

### What "truth-class" means, pinned so it cannot drift

The same test `tutor.TRUTH_REFEREES` uses (build `sj`): *a false thing a student would be
SHOWN or TOLD.* A finding is truth-class when a truth referee objected to the very reply it
quotes, or the draft was floored, or the rule it names is one of **13** (every spoken
mathematical sentence must be literally true), **18** (the tutor's words match the student's
actual answer), **61** (a generalisation carries its condition), **63** (the words and the
picture are the same figure), **64** (never trade the student's number for another). Every
other numbered rule is a promise about *how* the tutor teaches — conduct — and its live
referee fires exactly as before. This build changes what the report leads with and what
wakes Jim, not what a child gets.

## The monthly read

`ledger_markdown(data_dir, days)` — every finding seen in the window, split *on the ledger*
/ *actionable*, worst-recurring first, each with its quote, its fix and its Shipped-as line.
Served at `GET /api/admin/nightwatch/ledger?days=30` (admin key; `days` clamped 1..366) and
on the Night watch card as a third button, **Read the monthly ledger**. The card's status
line now opens with the policy's own number — "nothing actionable last night" or "N
ACTIONABLE last night" — parsed from the report so the two can never disagree.

The ledger row keeps three new fields — `severity`, `fix`, `actionable` — so the view can
group without guessing. Rows recorded before this build lack them and are classified on
read from what they kept; none is dropped.

## The charter: "done for the day", both seats

Jim's ruling of 2026-09-13 §2 — one warm closing line, a note of where they are, no
persuading — went unpaid for nine days because "the charter" did not exist as a place. It
does now, twice:

- **The critic** (`lessonaudit.CRITIC_SYSTEM`) gets its **seventh discipline check**: the
  right reply to "I'm done" is respected and is not a finding, and the critic may not argue
  both sides of the same turn — which the 09-12 watch's did (attempt 2 "overrides the
  student's request to stop", attempt 3 "should gently encourage one more").
- **The reviewer** (`nightwatch.RULED_ALLOWED`) gets **row eight**, rule 29, dated
  2026-09-13, rendered into its (C) block like the other seven.

Both carry `sh`'s boundary, because a ruling row without one is a blank cheque: **stopping
is not the same as being stuck.** "I don't get it", "this is too hard", "I give up" are
requests for a smaller step (rule 21), and a tutor who closes on those is a real defect.
A closing line that states something false, or that persuades after all, is judged
normally.

## Pins

PART **3ng** (21 checks): `is_actionable`'s seven cases; the three report shapes (mixed,
ledger-only, empty) plus an old result dict with no `new` key; the email's three cases; the
ledger row's fields, a repeat counted as one row seen twice, the monthly view's sections
and its handling of a pre-policy row and an unreadable file; `summary()`'s number on a
mixed and an empty night; the route, the clamp, the card; the ruling row, its boundary, its
presence in the rendered reviewer prompt, and the critic's seventh check by text.

Four older pins moved and marked "(xl)": `3lc`'s two test findings are HIGH now, because
the full print — tally, quote, Shipped-as — is for actionable findings and those two were
MEDIUM rule-28 conduct; the `RULED_ALLOWED` count 7 → 8 in `3kk` and `3jt`; the critic's
"Six discipline checks" → "Seven" in `3jq`. Every one found by running those PARTs before
the battery, not by the battery.

## What did not change

No referee. No live reply. No lesson. The course counts are untouched (39,915 / 40,169 /
941 of 40,221 / 635). `speechmap.py` did not change.

## After the push

Nothing to prewarm. Check `NIGHTWATCH_LESSONS` in Render: this build makes the reports
cheap to *read*; the lever that makes them cheap to *run* is still that number — 2 during
sweep weeks, or `NIGHTWATCH=off` until the round is done, `NIGHTWATCH_VERIFY` on either way.
The next morning report will open with either "Nothing actionable tonight" or the count.

## Battery

Frozen copy, 2026-09-22: **12,841 passed · 0 failed · 3 skipped** (12,821 at `xk`). Clean on the first run — the four pins the policy would trip were found and moved by running their PARTs before the battery, the discipline the last two builds paid for.

I did no harm and this file is not truncated.

# Build wv — The Sweep Says Why It Stopped (2026-09-17)

A small build from a real confusion. Jim ran the Pre-Calc sweep after `wu`; the card said
"Started — 36 lesson(s), about $5.4. This card follows it." and then, for ten minutes,
"last sweep: precalc — 0 finding(s) in 36 lessons, 7.7s". It read as a hung sweep. It was
the opposite: the sweep had run all 36 lessons in under eight seconds because every judge
call failed instantly with the same line — `OpenAI 429: You have no credits remaining` —
and the card reported that as a clean course. (The cap on the OpenAI account had been raised;
the prepaid credit balance had not. Raising the limit does not add money.)

Stamp: **`2026-09-17wv-the-sweep-says-why-it-stopped`**. Battery: see the bottom of this doc.

## coursesweep.py — the sweep stops when the seat is dead

`run_sweep` now watches for a **hard** error — a 429, 401 or 403, "no credits", a quota,
a key not set or invalid, "judge unavailable" (`_HARD_ERROR_RE`) — and when
`HARD_STOP_AFTER` (3) lessons in a row fail with the *same* one, it stops: the remaining
lessons are listed as "not attempted — the sweep stopped after 3 lessons in a row failed
the same way: …", and the result carries `stopped = {after, error}`. A reader that times
out on one long lesson and answers the next is untouched: the streak needs the same hard
error three times running, and a soft error ("read timeout") never counts. A sweep that
read some lessons before the seat died keeps what it read.

`report_markdown` puts a banner under the header — **STOPPED after 3 lesson(s)** … "Nothing
here is a reading of the course; fix the seat and run it again" — and, for a report from
before this build whose every lesson failed, a **NOT READ** banner. `list_reports` rows
now carry `asked`, `errors` and `stopped`.

## main.py and the admin card

The job snapshot carries `ran`, `stopped` and `first_error`. The card's status line:

- every lesson failed → "⚠️ precalc — 36 of 36 lessons could not be read: OpenAI 429 … →
  report … (not a reading of the course — fix the seat and run it again)";
- stopped part-way → "⚠️ precalc — stopped after 5 of 36 lessons: … · 3 finding(s) in the
  2 read";
- otherwise → "last sweep: precalc — 34 finding(s) in 27 of 36 lessons (9 unread), 2218s".

The report dropdown labels an all-unread report "NOT READ" and a cut-short one "stopped",
instead of "0 finding(s)".

## Counts

No lesson text changed: course 39,999; closure 40,253; speechmap 2,244; drift 1,938. PART
**3mq** (8 checks: the dead seat, the flaky seat, the seat that dies mid-run, a clean report
carries no banner, the listing, the card's strings, the notes).

## After the push

Add credits on OpenAI's billing page (Billing → Credit balance), then re-run Pre-Calc; the
card will tick "1 of 36 · reading pc-u1-…" within a minute. That report becomes `ww`.

## Battery

Frozen copy, 2026-09-17: **12,674 passed · 0 failed · 3 skipped** (12,666 at `wu`). The first run failed one meta-pin — the new PART read a fixed slice of admin.html for its dated note (the battery forbids slices; `notes()` reads the header) — fixed; the second run was clean.

I did no harm and this file is not truncated.

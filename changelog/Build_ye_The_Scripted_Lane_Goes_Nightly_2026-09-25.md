# Build ye — The Scripted Lane Goes Nightly, 2026-09-25

Jim: "Do we have anything else that we should be working on or are we just waiting for a
sweep?" — then **"go"** on the two quiet items recommended: the nightly screenwatch workflow
gets `xy`'s scripted lane, and the last fixed-slice note pins in the battery go. Built while
the sweeps are on hold ("let's take a break from sweeps for now", 09-24).

Stamp: **`2026-09-25ye-the-scripted-lane-goes-nightly`**. PART **3ny**. A small build; nothing to
prewarm; no course text touched.

## The scripted lane, every night

Since `hw` (08-18) the `screenwatch` workflow has driven one live three-turn lesson on
mrcadabra.com nightly with the audit student and judged the screens. `xy` (09-24) gave
screencheck a third way to capture — `--script`: the engine walks an authored lesson, the real
page plays every beat, no site, no secret, no model call — and the survey it made possible
found the two flags nobody could screenshot, the NaN shrink, the label sizes and the redraw
loop (`xy`, `yb`, `yc`, `yd`). It ran only when somebody ran it. Now it runs itself.

**`--script rota`.** `rota_lessons(L, size, day)` takes the 360 lessons in catalogue order,
cuts them into slices of `--rota-size` (default 8) and picks slice `day % slices`, `day` being
`--rota-day` or today's day of the year (UTC). Every lesson is watched once every ~45 nights;
the pick is pure, so any night can be re-run by hand by naming the day. The run's log names
the eight it drove.

**`--fail-on LOW|MEDIUM|HIGH`.** The exit status fails on a finding at or above the floor;
the default LOW is what the auditor always did, and the report lists everything regardless.
The nightly scripted lane uses MEDIUM, because the over-tall beat's S9 LOW is the `pu` rule
working — 253 of them in `yd`'s survey, by design — and would fail every night otherwise. A
LOW-only night prints "N findings, none at or above MEDIUM -- the run passes" to the log.

**The workflow.** A second job, `scripted`, beside the live one, in the same file and on the
same schedule: checkout, Python, Playwright, then
`python screencheck.py --script rota --rota-size 8 --fail-on MEDIUM --shots screenwatch-script-shots --out screenwatch-script-report.md`,
with the report and screenshots uploaded as `screenwatch-script-<run id>` for 30 days. The
two jobs are independent: the scripted one needs no secret (it runs whether or not Jim ever
set `SCREENWATCH_CODE`), and the live one is byte-for-byte what it was. Budget: Playwright's
install is about two minutes and a lesson 40–80 s, so eight lessons sit well inside the
20-minute job timeout; a MEDIUM or HIGH finding on any of the night's eight fails the job and
lands in Jim's GitHub notifications like the live lane's do.

Measured here before the battery: `--script rota --rota-size 2 --rota-day 3 --fail-on MEDIUM`
drove `entry-u2-add-past-ten` and `entry-u2-adding-three-numbers` (14 turns), found one S9
LOW (the tape shrunk on purpose on one turn) and exited 0; the same slice at the default LOW
exits 1. PART 3ny pins the rotation (all 360 once a cycle, none twice, the wrap, size 0,
the default 8), `failing()`, the CLI end to end with the capture stubbed, and the workflow's
two jobs.

## The last fixed-slice pins

`xy` warned that three dated-note pins still read a fixed slice of a file and "will bite
whoever adds a header note there next". There were four: 3ik's `"BUILD so" in cl[:2500]`
(client-log.js — the handoff had it as cadabra.js) and `vo[:3000]` (voice.js), and
geo-figures.js's `gf[:3000]` in 3jd, 3jg and 3jl. All four read `notes(<file>)` now, `ui`'s
law, and PART 3ny fails if any pin with "BUILD" on its line reads a `[:NNNN]` slice again.
The one `[:2500]` left in the battery is a code-proximity pin (the admin guard within 2,500
bytes of its route), not a dated note, and stays.

## Files

`screencheck.py` (`rota_lessons`, `failing`, `--rota-size`, `--rota-day`, `--fail-on`, the
`rota` word), `.github/workflows/screenwatch.yml` (the `scripted` job), `ruletests.py` (PART
3ny; four pins moved), `main.py` (stamp), this doc, the new
`START_HERE_Handoff_2026-09-25.md`.

Battery on the frozen copy, 2026-09-25: **13,119 passed · 0 failed · 3 skipped**, first run clean (13,110 at `yd`).

I did no harm and this file is not truncated.

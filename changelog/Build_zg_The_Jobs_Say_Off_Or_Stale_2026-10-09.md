# Build zg — the jobs say off or stale, and one plan is one student (2026-10-09)

Stamp: `2026-10-09zg-the-jobs-say-off-or-stale`. Battery: see the bottom.
**Nothing to prewarm** (no spoken line changed).

The first build off the PM board (`claude/PM_Board.md`): PM-2 and PM-4, with Jim's two answers
of 10-09: the night watch is off on purpose, and "I would set it up for one. That way we know
it's one price for one person. If we want to change it, we have to change it later."

## PM-2 — the jobs say off or stale

**What was wrong.** `/health` has printed each ops job's *age* since build ha, never whether
that age is bad. The 10-09 deep dive read the night watch's 1,863,911 seconds as a dead job
and called it the biggest operational finding. It was not dead: Jim had switched it off
(`NIGHTWATCH=off`) for the sweep rounds. A number that cannot tell *off* from *stale* misleads
the one reader it exists for.

**What it is now.** `/health` keeps `ops` exactly as it was and adds `ops_state`: each job's
verdict beside its age, against its own cadence.

| Job | Stale after | Off when |
|---|---|---|
| heartbeat | 2 hours (it beats every 30 min) | never |
| backup | 2 days (nightly) | never |
| off-site copy | `OFFSITE_BACKUP_DAYS` + 2 days (9 by default) | `OFFSITE_BACKUP_DAYS=0` |
| night watch | 2 days (nightly) | `NIGHTWATCH=off` (or nightwatch.py missing) |

- `off` carries its reason and is never an alarm. `unknown` means no database. A job that
  has *never* run is only stale once the server has been up longer than that job's limit,
  so a fresh deploy never reads as broken.
- A stale job **emails Jim** from the heartbeat, at most once per job per 12 hours, subject
  `STALE JOB — the nightly backup last ran 3 days ago` (so neither Jim nor the morning
  digest mistakes it for a night-watch report). The heartbeat cannot report its own death
  this way; that is what the `/health` verdict and the admin tile are for.
- `/admin` → System has a **Nightly jobs** tile: green "All fresh", or red "1 stale" with the
  job named; the caption lists every job (`night watch: off`).

After the push, `/health` today will read `"ok": true` with `nightwatch: {"state": "off",
"why": "NIGHTWATCH=off"}`.

## PM-4 — one plan, one student (Jim's ruling D1)

- `main.py` `KIDS_PER_SEAT` 2 → 1. Checkout, "Cover them" and coverage all follow it; a
  family with two students subscribes for two plans ($58/mo, $48 annual).
- The constant is now the only copy of the number: the Family page reads `kids_per_seat` from
  `/api/parent/me`; `store.admin_stats(kids_per_seat=…)` computes capacity from it; the admin
  "Paid seats" caption reads it.
- Copy: pricing (meta descriptions, JSON-LD offer names, the Full-access card, the Family
  card), front page (both FAQ answers, the card, its monthly/annual toggle, the Family card),
  features, family plan card, admin. `llms.txt` already said "per student". Prices unchanged.
- Payments are closed (no live Stripe key), so no paying family moves. A test-mode family
  with two students on one plan sees the newer student on Free with the existing
  "Cover them — prorated fairly" button.
- **Jim, in Stripe (test mode now, live later):** if the product or price names there say
  "up to 2 students", rename them; the app does not set those names.

## Proof

PART 3pa (25 checks): the source pins (the `/health` field, the heartbeat fence, the 12-hour
throttle and subject, the admin payload); the verdicts run against the real helper: all
fresh → ok; **the 10-09 reading itself** (21 days with `NIGHTWATCH=off` → off, whole ok) and
the same age switched on → stale; backup at 3 days stale; off-site at 8 days ok; off-site off;
a fresh deploy not stale; a dead heartbeat stale; no database unknown; the stale pass mails the
stale backup only. Then the plan: `_seats_for` / `_covered_count` at 1, the payload field,
`admin_stats`, the Family page and admin tile reading the server's number, no page promising a
free second student, "per student" on the cards, toggle and JSON-LD, the dated notes. Dry runs:
`/health` through the TestClient; the admin tile and the Family plan card evaluated with stub
data (two students → "$58/mo · 2 plans cover your 2 students").

## Files

`main.py` (stamp, `_ops_state` and friends, `/health`, the heartbeat, admin stats,
`KIDS_PER_SEAT`, `_parent_payload`), `store.py` (`admin_stats`), `static/family.html`,
`static/admin.html`, `static/pricing.html`, `static/landing.html`, `static/features.html`,
`ruletests.py` (PART 3pa), this doc.

I did no harm and this file is not truncated.

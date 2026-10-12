# Build zh — the browser's crashes reach Jim (2026-10-12)

Stamp: `2026-10-12zh-the-browsers-crashes-reach-jim`. Battery: **13,560 passed · 0 failed · 3 skipped**
(PART 3pb, 12 checks, added). **Nothing to prewarm.** Builds on zg (on disk, not yet pushed —
one push carries both).

The second build off the PM board: PM-6, and PM-5's plan.

## PM-6 — a real user's crash reaches Jim unasked

**What was wrong.** A *server* crash has emailed Jim since August (`_ops_alert`). A *browser*
crash — the kind a student actually meets — was beaconed to `/api/client-error` (build ha),
filed as a `clienterror` row, and then waited on /admin → Telemetry for someone to look. And
**23 of the 33 pages never loaded the beacon at all**, among them the sign-in page
(`index.html`), the drill page, the public demo lesson, the front page and pricing. A script
error there was invisible.

**What it is now.**

- `client-log.js` loads **first** in `<head>` on every page that runs a script — 22 more
  pages (`avatar-lab.html` runs none). Build ha once put this include inside a change-note
  comment and broke eight pages; zh inserts after the real `<head>` tag (comments excluded),
  and PART 3pb checks every page the way the browser sees it: live, first, no prose spilled
  before `<head>`.
- `_client_error_pass` rides the heartbeat (every 30 minutes). It writes its own marker
  first, reads the browser errors filed since the previous marker (the windows meet: no gap,
  no overlap), drops the known noise, groups the rest by page + message (numbers blanked, so
  "line 412" and "line 413" are one kind), and sends **one email per pass** naming the kinds
  **not seen in the 7 days before**. A kind that keeps happening is mailed again only after a
  quiet week.
- Noise is still filed and counted on /admin, never mailed: `Script error.` (a cross-origin
  script the browser will not describe), `ResizeObserver loop` (a harmless layout notice), and
  anything whose stack runs through a browser extension (the family's add-on, not our code).
- The email: subject `BROWSER ERROR — 2 new kind(s) on /login, /session`; each kind with its
  page, count, message and the first line of where it happened.
- `store.events_between(kinds, since, until, limit)`: events in an exact window, oldest first.

## PM-5 — the restore rehearsal (planned, not yet run)

`RECOVERY.md` gains **Drill 4 — the rehearsal**: Jim downloads a fresh backup from /admin into
a new folder outside the repo (`D:\RestoreDrill`), connects it, and says "run the restore
drill"; Claude restores it into a throwaway SQLite file *on Jim's computer* (the families'
data never leaves it), times it, checks every table's row count against the snapshot's and
opens one family's dashboard through the app; the result goes in the drill log; Jim deletes
the folder. It never touches the live database.

## Proof

PART 3pb: every page that runs a script carries the beacon live and first, with no stray
prose before `<head>`; the sign-in, drill, demo-lesson and home pages among them; the
heartbeat fence; the marker written before the read; one email, subject, no throttle; then
**on a real SQLite database**: the first pass reads only the last hour (a two-day-old row is
not new) and mails nothing; the second reads six browser rows (not the voice event), drops
three as noise, recognises the week-old kind, and mails one email naming the one new kind
(with its count of 2); a repeat in the next pass is known and mails nothing; an empty pass
reads nothing. The email body was also printed and read.

## Files

`main.py` (stamp, `_client_error_pass` and helpers, the heartbeat), `store.py`
(`events_between`), `ruletests.py` (PART 3pb), `RECOVERY.md` (Drill 4), 22 pages in `static/`
(the beacon + a dated note each): beta, cadabra-lab, community, courses, demo-lesson, demolab,
drill, features, help, home, homeschool, index, landing, methodology, mission, parents, pilot,
pricing, privacy, students, teachers, terms. This doc.

I did no harm and this file is not truncated.

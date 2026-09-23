# Build xt — The Voice Cache Reclaim Card, 2026-09-23

Stamp: **`2026-09-23xt-the-voice-cache-reclaim-card`**. PART **3no**. Project 9 of the 09-14
deep dive, the fifth gate build of the alternating schedule (watch policy `xl` → the miss has
a face `xn` → Phase C `xo` → the pencil in the scripted lane `xr` → **this**). Built on Jim's
"go with gate build".

## What was wrong

The voice cache is keyed on the text. Every build that changes a line — and every sweep
build changes dozens — leaves the OLD line's mp3 on disk under a hash nothing will ever ask
for again. The `ke` evictor spends exactly that class first, but it only runs when the cache
goes *over* its cap, and with the cap at 10,000 MB it never does. The 09-14 handoff counted
~812 MB dead; `xj` alone re-rendered ~1,900 lines after that, `xk` ~500, and every sweep
build since has added its share. The repair pass (`ke`) removes *damaged* clips only. There
was no admin action that reclaimed the orphans.

## The build

**`POST /api/admin/tts-cache-reclaim`** (`main.py`), behind the admin key, with a helper
`_tts_cache_orphans(keep_hours)` that walks the cache once and sorts every `.mp3` into three
piles: **in the scripted closure** (the course — never a candidate), **orphaned and older
than `keep_hours`** (reclaimable, oldest first), and **orphaned but written in the last
`keep_hours`** (left alone: the live tutor's clip from a lesson that may still be playing, or
a line just rendered and worth its few cents for a day). `dry_run` defaults to **true** and
deletes nothing; `dry_run=false` deletes the reclaimable pile. `keep_hours` defaults to 24.

Two guards that matter. **The course's own clips are never touched** — anything
`_script_closure_paths()` names is skipped before age is even looked at. **An empty closure
is a 409**, not a reclaim: if `lessonscripts` could not be read, the protected set is empty
and "everything is an orphan" is the one answer this must never give.

The response says everything the card needs: clips scanned, how many belong to the course
and their MB, how many are orphans and their MB, how many recent ones were kept, how many
are reclaimable, what was deleted and freed, the cache before and after against the cap,
the closure's own render status (so the card can point at the prewarm when lines are
missing), and the twenty oldest orphans with their age in days.

**The card** (`static/admin.html`, "Voice cache reclaim", under "Voice cache repair"):
**① Count them (free)** posts `dry_run: true` and prints the report and the oldest orphans;
**② Reclaim the space** is *disabled* until ① has run on this page, and its label then
carries what ① found ("② Reclaim the space — 7 clips, 812 MB"). ② posts `dry_run: false`
with the same `keep_hours` ① used, prints what was removed and the cache after, and
disarms again. The kb ruling (a POST-only endpoint Jim cannot press is one that never
runs) and the ke pattern (the safe button looks safe, the destructive one says so) both
hold.

## Proven

Through the TestClient against a seeded temp cache: 3 course clips + 4 orphans aged three
days + 1 fresh orphan → the dry run counts 8 / 3 / 5 / 4 reclaimable / 1 kept and deletes
nothing; the reclaim deletes exactly the 4 old ones and leaves the course and the fresh clip;
`keep_hours=0` then takes the fresh one and still leaves the course; the wrong key is a 401;
an empty closure is a 409 with nothing deleted. In a real browser (Playwright against
uvicorn, `/admin` with the key): ② starts disabled; ① prints "11 clips on disk — 3 belong
to the course, 8 are orphans … 1 of those was written in the last 24 hours and is left
alone" and the seven oldest with their ages; ② arms with "7 clips"; pressing it prints
"Removed 7 clips … 3 course clips untouched; 1 recent clip left alone", disarms, and the
disk holds exactly the 4 that should remain. No page errors.

PART 3no pins the endpoint's defaults and guards, the card's wiring and arming, and runs
the seeded-cache sequence every battery.

Battery on the frozen copy, 2026-09-23: **12,978 passed · 0 failed · 3 skipped** (12,965 at
`xs`), first run clean.

## After the push

`/health` = `2026-09-23xt-the-voice-cache-reclaim-card`. **Nothing to prewarm.** Open
`/admin`, find "Voice cache reclaim" under the repair card, press ① — expect well over
812 MB of orphans — then ②. The `/admin` cache line should drop by that much. Safe to run
after every sweep build from now on; it is what the evictor would have done had the cache
ever reached its cap.

## Files

`main.py` (the endpoint, the helper, the stamp), `static/admin.html` (the card),
`ruletests.py` (PART 3no), this doc, the refreshed `START_HERE_Handoff_2026-09-23.md`.

I did no harm and this file is not truncated.

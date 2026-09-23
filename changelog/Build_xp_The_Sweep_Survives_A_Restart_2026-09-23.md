# Build xp — The Sweep Survives A Restart, 2026-09-23

Stamp: **`2026-09-23xp-the-sweep-survives-a-restart`**. PART **3nk**. Built on Jim's report,
late 09-22: "I have run the algebra one twice and both times once it finished it just
disappeared and I can't find the report … I'm just throwing money away."

## What happened

The course sweep is a daemon thread inside the web server's own process. Until this build it
wrote its report — the `.md` and `.json` in `data/coursesweep/` — **only at the end** of the
run, and it kept its progress only in a dictionary in memory. A 36-lesson sweep runs 30–40
minutes. If the process is restarted in that window — a deploy (every push to GitHub rebuilds
Render), or Render restarting the service for its own reasons — the thread dies, nothing
reaches the disk, and the card's status line falls back to "no sweep has run in this
process". That is the "it just disappeared". Both Algebra I runs on 09-22 overlapped pushes
(xk, then xl/xm/xn), and every lesson the reader had already read was paid for and lost,
twice. Not a Jim mistake: a hole in the tool. The card had even said "in this process" all
along.

## The fix

Three parts, all proper.

**The checkpoint.** `coursesweep.run_sweep` now keeps one row per lesson (`_row_for`) and
calls `checkpoint(partial)` after **every** lesson — the rows read so far, the course, how many
were asked. `main.py`'s worker writes it to `data/coursesweep/<course>_partial.json`
(`write_partial`, whole-file-then-rename so a restart mid-write leaves the last good copy).
The name has no date, so `list_reports` — which lists `.md` files — never shows it as a
report; `list_partials` lists it for the card. The result is assembled from the rows
(`_assemble`) in the course's lesson order, so a fresh run and a resumed one produce the same
shape. A checkpoint that raises never stops the sweep. A restart now costs at most the one
lesson in flight, about 15 cents.

**The memory.** The job dictionary is mirrored to `data/coursesweep/_job.json` on every
change (`_sweep_save_job`, inside the lock). At startup `_sweep_recover()` reads it: a job
that was `running` when the last process died becomes **`interrupted`** — with the time it was
noticed, the reason ("the server restarted while the sweep was running — a deploy or a restart
on Render"), and how many lessons the checkpoint holds — so the card says exactly what
happened. A job that was `done` keeps its line across restarts too. A recovered job carries no
thread id, and a worker whose job has moved on writes nothing (checkpoint and report both
guarded), so a stale thread can never overwrite a live run.

**The resume.** `POST /api/admin/coursesweep/start` takes `resume=true`: it loads the
checkpoint, reads only the lessons it lacks, keeps the first run's size, and writes the normal
report — which carries a line, "_Resumed after a restart: N lesson(s) were read before it
(started …, build …), M read now_", so a report read across two builds says so. A fresh run of
a course that has a checkpoint is refused with a 409 that names the money already spent,
unless `discard=true`. The dry run prices the resume (`partial: {saved, left, resume_usd}`).
The status carries `partials`.

**The card** (`static/admin.html`): an interrupted sweep shows as "⚠️ algebra1 — INTERRUPTED
at 23 of 36 lessons (noticed …): the server restarted … The 23 read are saved — pick algebra1
and press Resume to read the rest." The Run button becomes "Resume algebra1 — 13 lesson(s)
left — SPENDS" when the picked course has a checkpoint; pressing it asks resume-or-start-over
before spending; the price button prices the resume; and the rule is printed on the card:
**do not push to GitHub while a sweep runs.**

Nothing else changed: the wv stop rule, the report's shape, the referee, the lessons.

## Proven

PART 3nk, with a stub judge and a temp data folder: a sweep killed under its fourth lesson
leaves three rows on the disk with the build and start time; resume reads only the three left
and reports `before 3, after 3`; the rows come back in lesson order; the report carries the
resumed line; `clear_partial` after `write_report`; "not attempted" rows are not carried; a
resume for another course is ignored; a raising checkpoint is harmless; the wv stop rule
still stands and its rows reach the checkpoint. Through the TestClient: the job file says
`running` with 2 saved while it runs; after a simulated restart the job is `interrupted` with
course, 2 saved, total 5, time and reason; the dry run prices 3 left; a fresh run is a 409; a
resume of a course with no checkpoint is a 404; the dead process's thread, released, writes
nothing; resume answers with 3 lessons and ends `done` 5 of 5 with the resumed counts; the
checkpoint is cleared and the job file says `done`; a restart after a finished sweep keeps the
`done` line; no job file recovers nothing; `discard=true` starts over.

Battery on the frozen copy: **12,907 passed · 0 failed · 3 skipped** (12,883 at xo).

## After the push

`/health` = `2026-09-23xp-the-sweep-survives-a-restart`. No lesson text changed, so
**nothing to prewarm** for xp (xo's ~2,000 lines still need theirs if not done). Then run
Algebra I **once**, and do not push anything until the card says it is done. If Render ever
restarts under it, the card will say so and offer Resume.

## Files

`coursesweep.py`, `main.py` (stamp), `static/admin.html`, `ruletests.py` (PART 3nk), this
doc, the refreshed `START_HERE_Handoff_2026-09-23.md`.

I did no harm and this file is not truncated.

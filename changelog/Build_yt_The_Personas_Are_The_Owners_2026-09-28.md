# Build yt — The Personas Are The Owner's, and Where The Minutes Go, 2026-09-28

The first build off the 09-28 deep dive's list
(`claude/Deep_Dive_2026-09-28_The_Road_To_Market.md`): items 1, 3 and 6 of Block 1, in one
build because each is small and all three are docs-and-gates rather than lessons.

Stamp: **`2026-09-28yt-the-personas-are-the-owners`**. PART **3on**. Nothing to prewarm.

## 1. The personas are the owner's (deep dive item 1)

`students.json`'s four persona codes — `1234` Alex, `2345` Maya, `3456` Sam, `0000` Demo
Student — logged in on mrcadabra.com in every environment: `_lookup_student` read the file
first, before the database, and every endpoint that takes a code goes through it. Four
guessable digits into the real database, running paid model calls.

Now, in `main.py`:

- The http middleware stamps every request's owner-ness (the owner cookie from `/admin`'s
  unlock, or `X-Admin-Key`) into a `ContextVar`, `_OWNER_REQ`, before the endpoint runs.
  Starlette copies the context into its thread pool, so a sync endpoint sees it; a
  background thread (the sweep, the prewarm) sees the default, False, and never needs a
  persona.
- `_lookup_student` resolves a persona only when `_personas_open()` or the request is the
  owner's. Personas are open with no database (the dev box, the headless drives), with a
  **sqlite** file (the battery's fourteen drills that log in as 1234 — production is
  Postgres on Render, never sqlite), or with `PERSONAS_OPEN=1` set on purpose. Otherwise
  a stranger's `1234` is "That code was not recognized." — the same words as any unknown
  code, so nothing leaks about which codes exist.
- Parent-made students, teacher classes, beta passes and `/demo` (which takes no code) are
  untouched. `/health` reports `"personas": "open" | "owner-only"`.

**For Jim:** unlock once from `/admin` (the cookie lasts 30 days) and play as 1234 exactly
as before. The first battery run caught the sqlite case — the missed-problem drill logged
in as 1234 against a temp database and got the 404 — which is what the sqlite rule is for.

## 2. Where the minutes go (deep dive item 3)

The one number the 09-14 strategy rests on and nobody had: how much of a child's time is
the live tutor. The data was already there — `script_answers` has one row per graded
scripted answer with its seconds; `usage_log` has one `brain` row per live model turn with
its code, course and mode — but nothing read them side by side, and nothing said *which
door* a live turn came in by.

- `main.py`: every `/api/chat` turn records a `turn` event named by its door —
  `_live_door`: **opener** (the page opened with no scripted lesson left), **seam**
  (`__script_done…`: a scripted lesson ended with nothing scripted after it), **quiz**,
  **final**, **chat** (a typed message) — after the gates and before the model, so a
  gated turn is not counted. `/api/script/intervene` records **intervene** (a second miss
  in a row handed to the tutor).
- `store.lane_minutes(days)`: per course — scripted answers, their minutes, students;
  live turns (lesson mode only; practice and topic are their own lanes), students; doors
  by name — plus the same per student (top 60) and totals. Read-only, all zeros with the
  DB off, drilled in the battery against a real sqlite file.
- `GET /api/admin/lanes?days=7|30|90`: admin-gated, codes masked the roster's way.
- `/admin`: a **Where the minutes go** card under Telemetry — the live share of turns as a
  tile (green under 10%, amber to 25%, red above), scripted answers and minutes, live
  turns, the doors; a by-course table and a by-student table; three window buttons; a
  legend that says what each door means.

Doors count from `yt` on; answers and turns reach back as far as the tables do, so the
30-day view is meaningful the day it deploys. What to look for: the live share per course,
and which door dominates. An **opener** count on a course a student has not finished means
the page could not find a scripted lesson to play; a **seam** count means course
boundaries or typed answers at the go-on/review choice; **intervene** is the designed
door and should be most of it. The next build closes whichever door the card names.

## 3. The README and MARKETING.md tell the truth (deep dive item 6)

`README.md`: ten courses (was eight); the two lanes, the pencil, the quiz, the child-mode
skin, the sweep and the nightly screen job in the product section; `lessonscripts.py`,
`lessons/`, `quizsets.py`, `drillpool.py`, `coursesweep.py`, `screencheck.py` and
`ruletests.py` in the layout table; "Dev login codes (until real accounts ship)" replaced
by an accounts section (parents on `/family`, teachers on `/teacher`, beta passes on
`/admin`, the Free plan, Stripe) that says what the personas are now; the status line.
`MARKETING.md`: 13,000+ checks (was 6,000+), and a rule-3 line so nobody quotes eight
courses from the old README. The methodology page's numbers are machine-counted and were
left alone.

## Files

`main.py` (the ContextVar, `_personas_open`, `_mark_owner_request`, the middleware line,
`_lookup_student`'s gate, `/health`; `_live_door`, the two door events, `/api/admin/lanes`;
stamp), `store.py` (`lane_minutes`), `static/admin.html` (the card), `README.md`,
`MARKETING.md`, `ruletests.py` (PART 3on), this doc, the handoff.

I did no harm and this file is not truncated.

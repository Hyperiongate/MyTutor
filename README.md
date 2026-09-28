<!--
  CHANGE NOTES (keep newest at top):
    2026-09-28  BUILD yt -- THE README TELLS THE TRUTH (the 09-28 deep dive, item 6). Ten
                courses, not eight (Entry-Level and Basic Math were added in August); the two
                lanes (the scripted course a child spends their minutes in, the live tutor
                behind it); the pencil, the quiz, the child-mode skin; real accounts shipped
                07-31 (parent sign-up, family codes, the Free plan and Stripe); the persona
                codes are the owner's in production since yt; the battery's real size; the
                sweep and the nightly screen job. Status line updated. Nothing removed that
                is still true.
    2026-07-30  FULL REWRITE (market prep). The old README described the Day-1 prototype
                ("Professor Einstein," one course, text-only, retired model id) and would
                break a deploy if followed. Now documents the real product: Mr. Cadabra,
                eight courses, warm-voice-out / type-in, all modes, all pages, correct
                env vars, and the production checklist.
    2026-07-19  Initial Day 1 README with deploy-to-Render steps for a non-coder.
-->

# MyTutor (Hyperion Shift LLC)

**MyTutor** is a voice-first AI math tutor for the K-12 homeschool market. Students learn
with **Mr. Cadabra** — a warm teacher who builds the foundation first and *speaks* his teaching aloud (natural
ElevenLabs voice) while a synchronized whiteboard draws each step, never running ahead of
the student. Students answer by **talking with him** — a real spoken back-and-forth
(speech is transcribed via ElevenLabs Scribe and the audio deleted immediately; only the
text survives) — or by typing, with 📈 graph paper for plotting; elementary courses answer
by tapping. *(Voice input restored 2026-08-07; the 🧮 Math Keyboard was retired the same day.)*

**Status: pre-market, feature-complete.** Parent accounts, family login codes, the Free
plan and Stripe billing shipped 2026-07-31; the ten courses have each been read three times
by the course sweep (the last readings produced no new class of defect); the remaining work
is the launch gate in `changelog/Deep_Dive_2026-09-28_The_Road_To_Market.md`.

## What's in the product

- **Ten complete courses**, each with 9 units, placement, and per-unit mastery tracking:
  Entry-Level Math, Basic Math, Pre-Algebra, Algebra I, Geometry, Algebra II, Trig/Pre-Calc,
  Probability & Statistics, Calculus, Differential Equations.
- **Two lanes.** The **scripted course** is where a student's minutes go: 360 authored
  lessons (36 per course) with fixed spoken lines, boards drawn from a tag grammar
  (`static/math-figures.js`, `static/geo-figures.js`), a worked walk-back on every miss, a
  five-question quiz per lesson (`quizsets.py`), a course review before a student's first
  lesson in a new course, and every clip pre-rendered in Mr. Cadabra's voice. The **live
  tutor** (`tutor.py`, `prompts.py`) takes over only at the seams -- a second miss in a row,
  a typed question, the end of a course -- and every reply it writes passes 101 referees
  and a math verifier before a child hears it. Entry and Basic get the child-mode skin
  (cream board, 72px answer buttons, three-in-a-row dots).
- **Four ways to learn:** the full course (`/session`), bring-your-own-problem practice
  (`/practice`), pick-a-topic mini-lessons (`/topic`), and the voluntary Course Assessment
  (`/challenge`) that recommends a path.
- **Honest progress:** a student dashboard (`/dashboard`, parent read view via
  `?view=parent`) and a multi-student class view (`/teacher`) — real data only, never
  invented numbers.
- **Guardrails:** math-only scope, jailbreak resistance, no discussing other students.
- **Cost controls:** Anthropic prompt caching + an on-disk ElevenLabs audio cache
  (capped, oldest-first eviction), plus per-code rate limits on every paid endpoint.

## Repo layout

| File | What it does |
|------|--------------|
| `main.py` | FastAPI server: routes, login, rate limits, TTS streaming + cache. |
| `tutor.py` | The teaching brain: per-course prompts, guardrails, Claude calls. |
| `pedagogy.py` | Per-unit misconception playbooks + teaching methodology. |
| `curriculum.py` | The 8 courses × 9 units map + topic classification. |
| `store.py` | Durable Postgres storage (activates when `DATABASE_URL` is set). |
| `lessonscripts.py`, `lessons/` | The scripted lane: the engine, the 347 generators, and the ten courses' authored beats. |
| `quizsets.py`, `drillpool.py` | The per-lesson quiz questions and the drill pool, both drawn inside each lesson's shape. |
| `coursesweep.py`, `screencheck.py` | The instruments: the reviewer that reads a whole course, and the headless screen survey the nightly GitHub job runs. |
| `ruletests.py` | The battery (13,000+ checks); `python ruletests.py --rules` regenerates `RULES.md`. |
| `students.json` | The four persona logins (made-up, not minors). Open on a dev box; in production (with a database) they answer only to the owner's browser -- real students come from parent accounts. |
| `static/` | All pages: index (login), home, session, practice, topic, challenge, dashboard, teacher, landing, demo, privacy, terms. |
| `render.yaml` | Render deployment blueprint (see its production checklist). |

## Deploy on Render (from GitHub)

1. Push this repo to GitHub; create a Render **Web Service** from it (or use the
   `render.yaml` Blueprint).
2. Environment variables:
   - `ANTHROPIC_API_KEY` — required (the teaching brain).
   - `ELEVENLABS_API_KEY` — required for the natural voice (without it the browser's
     built-in voice is used).
   - `CLAUDE_MODEL` — optional; defaults to `claude-sonnet-5`. **Do not set Haiku**
     (tested and rejected for teaching — see `Sonnet_vs_Haiku_AB.md`).
   - `DATABASE_URL` — Render Postgres internal URL; **required for durable student
     memory** (without it, progress lives on the ephemeral disk and resets on redeploy).
3. Build: `pip install -r requirements.txt` · Start: `uvicorn main:app --host 0.0.0.0 --port $PORT`
4. **Verify every deploy at `/health`** — it reports the running `build` stamp, model,
   and whether the database is active. If the stamp is old, the deploy didn't take
   (try "Clear build cache & deploy").

## Accounts, and the persona codes

Real students are made by a parent on `/family` (sign-up, then a child's login code) or by
a teacher on `/teacher`; beta passes are issued from `/admin`. The Free plan runs to the
first mastered unit; the Full plan is Stripe Checkout from the Family page.

The four personas in `students.json` -- `1234` Alex · `2345` Maya · `3456` Sam · `0000`
Demo Student -- are made-up, not real minors. On a dev box (no `DATABASE_URL`) they log in
as always. In production they answer only to the owner's browser: unlock once from `/admin`
(a 30-day cookie) and play as any of them; a stranger typing `1234` gets "That code was not
recognized." `/health` reports the mode as `personas`.

## Working rules for this codebase

Complete files only (no snippets), dated change notes at the top of every changed file,
dry-run before delivery, bump `APP_BUILD` in `main.py` for any backend change, and every
file ends with the line below.

I did no harm and this file is not truncated.

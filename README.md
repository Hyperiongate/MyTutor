<!--
  CHANGE NOTES (keep newest at top):
    2026-10-15  BUILD zo -- THE TRUTH PASS (PM-43 on the PM board). Checked line by line against
                the code. Fixed: curriculum.py's row said "8 courses" (ten); the status line
                pointed at a launch gate the PM board has replaced; "every reply passes 101
                referees" overclaimed (a reply that trips a teaching check can still ship as the
                best draft, logged); CLAUDE_MODEL's production value is claude-sonnet-5-5 since
                10-15 (the code default is still claude-sonnet-5); the Haiku note pointed at a
                file that is not in the repo; the Free plan is "a first unit to try", not "runs
                to the first mastered unit" (yv). Added what shipped since 09-28: one plan per
                student, the safety net, self-serve delete, the second opinion and its rewrite
                limit, the model trial, the weekly PC backup, browser-error mail, and the
                settings each one reads. Nothing removed that is still true.
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

**Status: pre-market, feature-complete, in beta (no payments taken yet).** Parent accounts,
family login codes, the Free plan and Stripe billing shipped 2026-07-31; the ten courses have
each been read three times by the course sweep. What is left before launch, who owns it and
what happens next is the **PM board** (`claude/PM_Board.md` in the "My Tutor" project on
claude.ai) — counsel's sign-off, verifiable parental consent, live payments, and a playtest
with real families are the big items.

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
  a typed question, the end of a course -- and every reply it writes is checked before a
  child hears it: a math verifier (`mathcheck.py`, symbolic math) re-computes the answers it
  declares and the equations it draws, and 101 referees read the words. Wrong math is
  rewritten, and withheld if it cannot be fixed; a reply that trips a teaching referee is
  rewritten too, and when the tries run out the best draft ships and the miss is logged
  (`pass_through` on /admin Telemetry). Entry and Basic get the child-mode skin (cream
  board, 72px answer buttons, three-in-a-row dots).
- **A second opinion** (`LIVE_CRITIC`): a second, smaller model reads each live reply the
  referees pass. Its objection buys one rewrite per turn (`LIVE_CRITIC_RETRIES`, default 1
  since 2026-10-15; 2 is the old behaviour, 0 records only).
- **The safety net** (`safety.py`, 2026-10-13): every free-text door (live lesson, homework
  help, topic help, a raised hand, a spoken answer) is read by a separate small model before
  the tutor sees it, with a keyword screen behind it. A message suggesting a student may be
  hurt or unsafe gets a fixed kind reply instead of teaching, a note on the parent's Family
  page, and an email to the parent (at most once per student every 6 hours). The wording is
  awaiting counsel.
- **Four ways to learn:** the full course (`/session`), bring-your-own-problem practice
  (`/practice`), pick-a-topic mini-lessons (`/topic`), and the voluntary Course Assessment
  (`/challenge`) that recommends a path. Abrabot's drill room (`/drill`) adds extra practice
  from the drill pool, free to serve (browser voice).
- **Honest progress:** a student dashboard (`/dashboard`, parent read view via
  `?view=parent`), printable homeschool records (`/records`), a Friday parent email, and a
  multi-student class view (`/teacher`) — real data only, never invented numbers.
- **Parents in control:** the Family page (`/family`) adds students, mints and replaces
  login codes, steers the plan, shows safety notes, and deletes — one student (Remove) or the
  whole account (Delete my account: password + DELETE, billing canceled first, one
  transaction).
- **Guardrails:** math-only scope, jailbreak resistance, no discussing other students.
- **Cost controls:** Anthropic prompt caching + an on-disk ElevenLabs audio cache
  (capped, oldest-first eviction), plus per-code rate limits on every paid endpoint.

## Plans

- **Free:** the placement check, a first unit to try (the unit the student starts in), and
  unlimited Practice and Explore-a-topic help.
- **Full access:** $29/month **per student** ($24/month billed annually), introductory. One
  plan covers one student (`KIDS_PER_SEAT = 1` in `main.py`, Jim's ruling 2026-10-09).
  Stripe Checkout from the Family page; payments stay closed until a live Stripe key is set.

## Repo layout

| File | What it does |
|------|--------------|
| `main.py` | FastAPI server: routes, login, rate limits, the safety gate, TTS streaming + cache, /admin's endpoints, the ops heartbeat. |
| `tutor.py` | The live tutor: prompts assembled per course, the referees, the reply pipeline, the second opinion, Claude calls. |
| `prompts.py` | The tutor's ground rules. |
| `mathcheck.py` | The math verifier (SymPy). |
| `safety.py` | The safety net's reader and the crisis reply. |
| `pedagogy.py` | Per-unit misconception playbooks + teaching methodology. |
| `curriculum.py` | The 10 courses × 9 units map + topic classification. |
| `store.py` | Durable Postgres storage (activates when `DATABASE_URL` is set). |
| `lessonscripts.py`, `lessons/` | The scripted lane: the engine, the 347 generators, and the ten courses' authored beats. |
| `quizsets.py`, `drillpool.py` | The per-lesson quiz questions and the drill pool, both drawn inside each lesson's shape. |
| `coursesweep.py`, `screencheck.py` | The instruments: the reviewer that reads a whole course, and the headless screen survey the nightly GitHub job runs. |
| `modeltrial.py` | The /admin Model trial: two models teach the same scenario lessons side by side. |
| `ruletests.py` | The battery (13,000+ checks); `python ruletests.py --rules` regenerates `RULES.md`. |
| `students.json` | The four persona logins (made-up, not minors). Open on a dev box; in production (with a database) they answer only to the owner's browser -- real students come from parent accounts. |
| `tools/pc-backup/` | The weekly Windows backup to `D:\MrCadabra Backup` (see its README). |
| `static/` | Every page: the marketing site (landing, features, pricing, courses, methodology, parents, privacy, terms, …) and the app (index, home, session, practice, topic, challenge, drill, dashboard, records, family, teacher, admin, …). |
| `render.yaml` | Render deployment blueprint (see its production checklist). |
| `RECOVERY.md` | How to get everything back, and the restore drill's log. |

## Deploy on Render (from GitHub)

1. Push this repo to GitHub; create a Render **Web Service** from it (or use the
   `render.yaml` Blueprint).
2. Environment variables (the full list of names is in `RECOVERY.md`):
   - `ANTHROPIC_API_KEY` — required (the teaching brain, the safety reader, the second opinion).
   - `ELEVENLABS_API_KEY` — required for the natural voice (without it the browser's
     built-in voice is used).
   - `CLAUDE_MODEL` — the teaching model. Production runs **`claude-sonnet-5-5`** (set
     2026-10-15 after the 10-14 model trial); the code's default if unset is
     `claude-sonnet-5`. **Do not set Haiku** for teaching (tested and rejected in August).
   - `DATABASE_URL` — Render Postgres internal URL; **required for durable student
     memory** (without it, progress lives on the ephemeral disk and resets on redeploy).
   - `LIVE_CRITIC=anthropic`, `LIVE_CRITIC_MODEL=claude-haiku-5-5`, and the tile's prices
     `CRITIC_IN_USD_PER_MTOK=0.10`, `CRITIC_OUT_USD_PER_MTOK=0.50` — the second opinion.
     `LIVE_CRITIC_RETRIES` is normally left unset (1).
   - `DATA_EXPORT_KEY` — unlocks the backup download, and the weekly PC backup uses it.
   - `NIGHTWATCH=off` — the night watch is off on purpose for now (Jim, 2026-10-09).
   - Optional: `SAFETY_CHECK=off` switches the safety net's model reader off (the keyword
     screen stays on); `SAFETY_MODEL` overrides its model (default `claude-haiku-5-5`).
3. Build: `pip install -r requirements.txt` · Start: `uvicorn main:app --host 0.0.0.0 --port $PORT`
4. **Verify every deploy at `/health`** — it reports the running `build` stamp, model,
   whether the database is active, the safety net, and each ops job (heartbeat, backup,
   off-site, night watch, PC copy) as ok / stale / off. If the stamp is old, the deploy
   didn't take (try "Clear build cache & deploy").

## Watching it

- **/admin** holds the key-gated control panels: Telemetry (referee fires, pass-throughs,
  browser errors), 💵 Cost & verifier (turn time, retries, the second opinion's share),
  ⏱️ Where the minutes go (scripted vs live), Backups, the Course sweep, and the Model trial.
- The heartbeat emails Jim when a job goes stale ("STALE JOB"), when a browser reports a new
  kind of error ("BROWSER ERROR"), and when the safety net fires ("SAFETY").

## Accounts, and the persona codes

Real students are made by a parent on `/family` (sign-up, then a child's login code) or by
a teacher on `/teacher`; beta passes are issued from `/admin`. The Free plan and Full access
are described under **Plans** above.

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

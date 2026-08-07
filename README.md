<!--
  CHANGE NOTES (keep newest at top):
    2026-07-30  FULL REWRITE (market prep). The old README described the Day-1 prototype
                ("Professor Einstein," one course, text-only, retired model id) and would
                break a deploy if followed. Now documents the real product: Mr. Cadabra,
                eight courses, warm-voice-out / type-in, all modes, all pages, correct
                env vars, and the production checklist.
    2026-07-19  Initial Day 1 README with deploy-to-Render steps for a non-coder.
-->

# MyTutor (Hyperion Shift LLC)

**MyTutor** is a voice-first AI math tutor for the K-12 homeschool market. Students learn
with **Mr. Cadabra** — a warm, Socratic tutor who *speaks* his teaching aloud (natural
ElevenLabs voice) while a synchronized whiteboard draws each step, never running ahead of
the student. Students answer by **talking with him** — a real spoken back-and-forth
(speech is transcribed via ElevenLabs Scribe and the audio deleted immediately; only the
text survives) — or by typing, with 📈 graph paper for plotting; elementary courses answer
by tapping. *(Voice input restored 2026-08-07; the 🧮 Math Keyboard was retired the same day.)*

**Status: pre-market development.** The teaching engine is complete; accounts, billing,
and the privacy/consent stack are in progress (see `claude/Market_Readiness_Review.md`
in the project docs for the punch list).

## What's in the product

- **Eight complete courses**, each with 9 units, placement, and per-unit mastery tracking:
  Pre-Algebra, Algebra I, Geometry, Algebra II, Trig/Pre-Calc, Probability & Statistics,
  Calculus, Differential Equations.
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
| `students.json` | Dev-phase login codes (made-up personas — replaced by real accounts). |
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

## Dev login codes (until real accounts ship)

`1234` Alex · `2345` Maya · `3456` Sam · `0000` Demo Student — defined in
`students.json`; these are made-up personas, not real minors.

## Working rules for this codebase

Complete files only (no snippets), dated change notes at the top of every changed file,
dry-run before delivery, bump `APP_BUILD` in `main.py` for any backend change, and every
file ends with the line below.

I did no harm and this file is not truncated.

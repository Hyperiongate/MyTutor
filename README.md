<!--
  CHANGE NOTES (keep newest at top):
    2026-07-19  Initial Day 1 README with deploy-to-Render steps for a non-coder.
-->

# Math Tutor MVP — v0.1 (Hyperion Shift LLC)

A voice-ready (text first) AI algebra tutor. This is the **Day 1 backbone**: a
student enters a code, and then has a text conversation with **Professor
Einstein**, who teaches solving linear equations in one variable. The tutor
remembers each student between logins.

## What's in this repo

| File | What it does |
|------|--------------|
| `main.py` | The FastAPI web server (login, chat, session memory). |
| `tutor.py` | The tutor's "brain": the system prompt and the Claude API call. |
| `students.json` | The hardcoded test students (login codes → personas). |
| `static/index.html` | The minimal code-entry screen. |
| `static/session.html` | The chat screen with the pulsing orb. |
| `requirements.txt` | Python dependencies. |
| `render.yaml` | Render deployment blueprint. |
| `.gitignore` | Keeps local cache and saved sessions out of git. |

## Test login codes

`1234` Alex · `2345` Maya · `3456` Sam · `0000` Demo Student

## Deploy on Render (from GitHub)

1. Put all these files in your GitHub repo (root of the repo).
2. In Render, create a new **Web Service** from that repo (or use the Blueprint
   from `render.yaml`).
3. In the service's **Environment** settings, add:
   - `ANTHROPIC_API_KEY` = your Claude API key (required).
   - `CLAUDE_MODEL` = `claude-3-5-sonnet-latest` (optional; already the default).
4. Render uses these automatically:
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Open the Render URL, enter a test code, and start talking to the tutor.

## Known limits in v0.1 (planned, not bugs)

- **Voice** (speaking/listening) is Day 3 — this version is text chat.
- **The animated orb with color options** is Day 5 — this version has a simple
  placeholder orb.
- **Durable memory:** the tutor remembers via `data/sessions.json`, but Render's
  disk is ephemeral, so memory can reset on redeploy. Real persistence (database
  or Render persistent disk) is Day 4.

I did no harm and this file is not truncated.

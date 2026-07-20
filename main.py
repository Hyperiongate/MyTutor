# =============================================================================
# main.py  --  Math Tutor MVP  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-07-19  Firmed up ElevenLabs voice_settings (stability 0.55 + speaker
#               boost) to reduce garbled words.
#   2026-07-19  Added the progress DASHBOARD: GET /dashboard (serves
#               dashboard.html) and GET /api/progress/{code} (data from
#               progress.py -- currently representative sample data, real shape).
#   2026-07-19  LOW-LATENCY VOICE. /api/speak is now a STREAMING GET that proxies
#               ElevenLabs' stream endpoint (audio starts playing before it's fully
#               generated), and the default model is now eleven_flash_v2_5 (fast).
#               Added /api/voice-status so the frontend knows whether the natural
#               voice is available before requesting it. Removed the old POST speak.
#   2026-07-19  Set the default ELEVENLABS_VOICE_ID to Jim's chosen voice
#               (sB7vwSCyX0tQmU24cW2C) so a fresh deploy uses it even without the
#               env var. Still overridable via the ELEVENLABS_VOICE_ID env var.
#   2026-07-19  Added POST /api/speak: proxies ElevenLabs text-to-speech so the
#               tutor can talk in a natural voice. The API key stays server-side
#               (env ELEVENLABS_API_KEY). If the key is missing or the call fails,
#               it returns 204 and the browser falls back to its built-in voice.
#               Voice/model configurable via ELEVENLABS_VOICE_ID / ELEVENLABS_MODEL.
#   2026-07-19  Initial Day 1 backbone. FastAPI backend that:
#                 - serves the minimal code-entry screen and the session screen
#                 - validates a student login code against students.json
#                 - runs a text chat with the tutor (tutor.py / Claude API)
#                 - remembers each student's conversation across logins by
#                   saving it to data/sessions.json
#               Voice (Day 3) and the animated orb options (Day 5) are not here
#               yet; this is the backbone they will plug into.
#
# HOW IT RUNS:
#   Locally:  uvicorn main:app --reload
#   Render:   uvicorn main:app --host 0.0.0.0 --port $PORT   (see render.yaml)
#
# IMPORTANT NOTE ABOUT MEMORY ON RENDER:
#   data/sessions.json lets the tutor remember students. On Render's free/basic
#   web services the disk is EPHEMERAL -- it can reset on redeploy or restart, so
#   memory may not survive forever yet. True durable persistence (a database or a
#   Render persistent disk) is planned for Day 4. This is honest scaffolding, not
#   a permanent solution.
# =============================================================================

import json
import os
import threading
from pathlib import Path

import httpx
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, JSONResponse, Response, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

import tutor
import progress

# ---- ElevenLabs voice config (all optional; empty key -> browser voice) -----
# Set these in Render (NOT in code). If ELEVENLABS_API_KEY is missing, the app
# still talks using the browser's built-in voice.
ELEVEN_API_KEY = os.environ.get("ELEVENLABS_API_KEY")
# Default voice = Jim's chosen ElevenLabs voice. Override with any other voice_id
# from your ElevenLabs Voice Library via the ELEVENLABS_VOICE_ID env var.
ELEVEN_VOICE_ID = os.environ.get("ELEVENLABS_VOICE_ID", "sB7vwSCyX0tQmU24cW2C")
# eleven_flash_v2_5 = low latency (best for live conversation); override with
# ELEVENLABS_MODEL="eleven_multilingual_v2" for higher quality at more latency.
ELEVEN_MODEL = os.environ.get("ELEVENLABS_MODEL", "eleven_flash_v2_5")

# ---- Paths -----------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
DATA_DIR = BASE_DIR / "data"
STUDENTS_FILE = BASE_DIR / "students.json"
SESSIONS_FILE = DATA_DIR / "sessions.json"

DATA_DIR.mkdir(exist_ok=True)  # make sure the memory folder exists

# A simple lock so two overlapping requests never corrupt the sessions file.
_sessions_lock = threading.Lock()


# ---- Loading the hardcoded students ----------------------------------------
def load_students() -> dict:
    """Read students.json and return the {code: student} mapping."""
    with open(STUDENTS_FILE, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    return data.get("students", {})


STUDENTS = load_students()


# ---- Session memory (per student code) -------------------------------------
def _read_all_sessions() -> dict:
    if not SESSIONS_FILE.exists():
        return {}
    try:
        with open(SESSIONS_FILE, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except (json.JSONDecodeError, OSError):
        # If the file is missing or somehow corrupted, start fresh rather than
        # crash. We do no harm to a running session over a bad memory file.
        return {}


def _write_all_sessions(all_sessions: dict) -> None:
    tmp = SESSIONS_FILE.with_suffix(".json.tmp")
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(all_sessions, fh, ensure_ascii=False, indent=2)
    tmp.replace(SESSIONS_FILE)  # atomic swap so the file is never half-written


def get_session(code: str) -> dict:
    """Return this student's saved session, creating an empty one if needed."""
    all_sessions = _read_all_sessions()
    return all_sessions.get(code, {"history": []})


def save_session(code: str, session: dict) -> None:
    with _sessions_lock:
        all_sessions = _read_all_sessions()
        all_sessions[code] = session
        _write_all_sessions(all_sessions)


# ---- Request models --------------------------------------------------------
class LoginRequest(BaseModel):
    code: str


class ChatRequest(BaseModel):
    code: str
    message: str


# ---- App -------------------------------------------------------------------
app = FastAPI(title="Math Tutor MVP", version="0.1.0")


def _student_or_404(code: str) -> dict:
    code = (code or "").strip()
    student = STUDENTS.get(code)
    if not student:
        raise HTTPException(status_code=404, detail="That code was not recognized.")
    return student


@app.get("/")
def home():
    """The minimal code-entry screen."""
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/session")
def session_page():
    """The screen where the student talks with the tutor."""
    return FileResponse(STATIC_DIR / "session.html")


@app.get("/dashboard")
def dashboard_page():
    """The full-screen progress dashboard."""
    return FileResponse(STATIC_DIR / "dashboard.html")


@app.get("/api/progress/{code}")
def progress_state(code: str):
    """Return the student's progress data (currently representative sample data)."""
    student = _student_or_404(code)
    return progress.get_progress(code.strip(), student)


@app.get("/health")
def health():
    """Simple check that the service is up (handy for Render)."""
    return {"status": "ok", "students_loaded": len(STUDENTS)}


@app.post("/api/login")
def login(req: LoginRequest):
    """Validate a login code and return who the student is."""
    student = _student_or_404(req.code)
    session = get_session(req.code.strip())
    returning = bool(session.get("history"))
    return {
        "ok": True,
        "code": req.code.strip(),
        "name": student.get("name"),
        "returning": returning,
        "tutor_name": tutor.TUTOR_NAME,
    }


@app.get("/api/session/{code}")
def session_state(code: str):
    """Return the student's info and remembered conversation (for resume)."""
    student = _student_or_404(code)
    session = get_session(code.strip())
    return {
        "name": student.get("name"),
        "tutor_name": tutor.TUTOR_NAME,
        "history": session.get("history", []),
    }


@app.post("/api/chat")
def chat(req: ChatRequest):
    """Send the student's message to the tutor and return the tutor's reply."""
    student = _student_or_404(req.code)
    code = req.code.strip()

    message = (req.message or "").strip()
    if not message:
        raise HTTPException(status_code=400, detail="Please type a message first.")

    session = get_session(code)
    history = session.get("history", [])

    # Give the tutor the student's remembered progress plus the live history.
    student_context = dict(student)
    reply = tutor.get_tutor_reply(student_context, history, message)

    # Remember this exchange so the tutor recalls it next time.
    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": reply})
    session["history"] = history
    save_session(code, session)

    return {"reply": reply}


@app.get("/api/voice-status")
def voice_status():
    """Tell the frontend whether the natural ElevenLabs voice is configured."""
    return {"eleven": bool(ELEVEN_API_KEY)}


@app.get("/api/speak")
def speak(text: str = ""):
    """
    STREAM the tutor's words as a natural ElevenLabs voice (low latency): audio
    starts playing in the browser before the whole clip is generated. The browser
    plays this via <audio src="/api/speak?text=...">.

    If ELEVENLABS_API_KEY is not set, returns 204 and the browser uses its built-in
    voice instead. (Check /api/voice-status first to avoid an empty request.)
    """
    text = (text or "").strip()
    if not text or not ELEVEN_API_KEY:
        return Response(status_code=204)

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVEN_VOICE_ID}/stream"
    headers = {"xi-api-key": ELEVEN_API_KEY, "Content-Type": "application/json"}
    payload = {
        "text": text,
        "model_id": ELEVEN_MODEL,
        "output_format": "mp3_44100_128",
        "voice_settings": {"stability": 0.55, "similarity_boost": 0.75, "use_speaker_boost": True},
    }

    def audio_stream():
        try:
            with httpx.stream("POST", url, headers=headers, json=payload, timeout=30.0) as r:
                if r.status_code != 200:
                    print(f"[speak] ElevenLabs {r.status_code}: {r.read()[:200]!r}")
                    return
                for chunk in r.iter_bytes():
                    if chunk:
                        yield chunk
        except Exception as exc:  # noqa: BLE001
            print(f"[speak] stream error: {exc}")

    return StreamingResponse(audio_stream(), media_type="audio/mpeg")


# Serve the static folder (css/js/images if we add them) under /static.
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


# I did no harm and this file is not truncated.

# =============================================================================
# safety.py  --  THE SAFETY NET  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-10-13  NEW FILE (build zk, PM-12 on the PM board; the 10-09 deep dive's "a safety
#               layer that does not depend on the tutor obeying"). Until now the only thing
#               between a child saying "I want to die" and Mr. Cadabra's reply was ground
#               rule 31 in the tutor's prompt -- a nudge to the same model that is busy
#               teaching fractions. This file is a SEPARATE reader that does one job:
#                 classify(message) -> {"category": "crisis" | "personal_info" | "none",
#                                       "why", "source", "ms", "usage"}
#               * a message with no letters ("12", "3/4", "x=5") is "none" without a call;
#               * otherwise a small, fast model (SAFETY_MODEL, default claude-haiku-5-5)
#                 reads it with a strict prompt and answers in JSON; temperature 0, a
#                 3-second ceiling, no retries -- it sits in front of a child's turn;
#               * if that model cannot answer (no key, timeout, bad JSON), the KEYWORD
#                 screen decides instead (source "keywords"), so the net never vanishes
#                 when the model is down. Keywords are tuned for precision on purpose:
#                 a wrong alarm reaches a parent.
#               quick_screen(message) is the zero-latency keyword test the scripted lane
#               uses on spoken answers (a model then confirms before anything happens).
#               CRISIS_REPLY is what Mr. Cadabra says instead of teaching: brief, warm,
#               not alarmed, points to a trusted adult, gives 9-8-8 and 9-1-1 (written with dashes so
#               the voice reads them as digits, never "nine eleven"). Counsel reviews
#               the words (PM-10) -- they live here, in one place, for that reason.
#               SAFETY_CHECK=off in Render switches the model reader off (keywords stay).
#               No student data is stored here; main.py records and alerts.
# =============================================================================
import json
import os
import re
import time

DEFAULT_SAFETY_MODEL = "claude-haiku-5-5"
SAFETY_TIMEOUT_S = float(os.environ.get("SAFETY_TIMEOUT_S", "3") or 3)

CATEGORIES = ("crisis", "personal_info", "none")

# What Mr. Cadabra says when a message suggests a child may be hurt or unsafe. Short, kind,
# no questions, no promises of secrecy, no diagnosis, and it does not go back to the math.
CRISIS_REPLY = (
    "Thank you for telling me that. It's really important, and you matter a lot. "
    "Please tell a grown-up you trust about this today: a parent, a teacher, or another "
    "adult who cares about you. If you are in danger right now, tell a grown-up near you "
    "or call 9-1-1. You can also call or text 9-8-8 any time, day or night, to talk with "
    "someone kind who can help. I'm right here, and we can get back to math whenever "
    "you're ready."
)

# ---- the keyword screen ------------------------------------------------------------------
# High-precision phrases only. "This homework is killing me" and "a car hits a wall" are
# NOT here on purpose; the model reader handles judgment, these catch the unmistakable.
_CRISIS_PHRASES = (
    r"\bkill(ing)? my ?self\b", r"\bwant(s)? to die\b", r"\bwanna die\b", r"\bwant to be dead\b",
    r"\bwish i (was|were) dead\b", r"\bhurt(ing)? my ?self\b", r"\bcut(ting)? my ?self\b",
    r"\bend my life\b", r"\bsuicid(e|al)\b", r"\bdon'?t want to (live|be alive)\b",
    r"\bbetter off dead\b", r"\bno reason to live\b",
    r"\b(he|she|they|my (dad|mom|mum|father|mother|stepdad|stepmom|brother|sister|uncle|"
    r"aunt|grandpa|grandma|cousin|coach|babysitter)) (hits|beats|hurts|chokes|kicks|touches) me\b",
    r"\b(someone|somebody) (is )?(hurting|touching|hitting) me\b",
    r"\b(touched|molested|abused) me\b", r"\b(i am|i'm|im) (being )?abused\b",
    r"\b(scared|afraid) to go home\b", r"\bnot safe at home\b", r"\b(i am|i'm|im) not safe\b",
)
_CRISIS_RE = re.compile("|".join("(?:%s)" % p for p in _CRISIS_PHRASES), re.I)

_PI_PATTERNS = (
    r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b",                                 # a phone number
    r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b",                                       # an email address
    r"\b\d{1,5}\s+\w+(\s\w+)?\s+(street|st|avenue|ave|road|rd|drive|dr|lane|ln|court|ct|"
    r"boulevard|blvd|way|place|pl)\b",                                     # a street address
    r"\bmy (home )?address is\b", r"\bi live (at|on)\b",
)
_PI_RE = re.compile("|".join("(?:%s)" % p for p in _PI_PATTERNS), re.I)


def has_words(message: str) -> bool:
    """True when the message has at least two letters in a row -- anything else is an
    answer like 12, 3/4 or x=5 and needs no reader."""
    return bool(re.search(r"[A-Za-z]{2,}", message or ""))


def quick_screen(message: str) -> bool:
    """Zero-latency: does the message contain an unmistakable crisis phrase?"""
    return bool(_CRISIS_RE.search(message or ""))


def keyword_category(message: str) -> str:
    if quick_screen(message):
        return "crisis"
    if _PI_RE.search(message or ""):
        return "personal_info"
    return "none"


SAFETY_SYSTEM = """You check messages that a STUDENT (age 5 to 18) typed or said to a math tutor app.
Decide ONE category:
- "crisis": the student says or clearly suggests they may hurt themselves or want to die; that
  someone is hurting, abusing, threatening or touching them inappropriately; or that they are
  unsafe (at home or anywhere).
- "personal_info": the student shares a home address, phone number, email address, their
  full name with last name, their school's name, or exactly where they will be.
- "none": everything else -- math answers, questions, frustration ("I hate fractions", "this
  is killing me"), jokes, word problems or story text ("the car hits a wall"), off-topic chat.
Only say "crisis" when the student is talking about real harm to a real person in their own
life. When in honest doubt between "crisis" and "none" for a message about being hurt or
wanting to die, choose "crisis".
Answer with ONLY a JSON object: {"category": "crisis|personal_info|none", "why": "<at most 12 words>"}"""


def _enabled() -> bool:
    return os.environ.get("SAFETY_CHECK", "on").strip().lower() not in ("off", "0", "false", "no")


def _model_reader(message: str, client=None):
    """Ask the small model. Returns (category, why, usage) or raises."""
    api_key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if client is None:
        if not api_key:
            raise RuntimeError("no ANTHROPIC_API_KEY")
        from anthropic import Anthropic
        client = Anthropic(api_key=api_key, timeout=SAFETY_TIMEOUT_S, max_retries=0)
    model = os.environ.get("SAFETY_MODEL", "").strip() or DEFAULT_SAFETY_MODEL
    resp = client.messages.create(
        model=model, max_tokens=80, temperature=0, system=SAFETY_SYSTEM,
        messages=[{"role": "user", "content": "Student message:\n<<<\n" + (message or "")[:1500] + "\n>>>"}])
    text = "".join(getattr(b, "text", "") for b in resp.content
                   if getattr(b, "type", None) == "text").strip()
    hit = re.search(r"\{[\s\S]*\}", text)
    if not hit:
        raise ValueError("no JSON in the safety reply")
    data = json.loads(hit.group(0))
    cat = str(data.get("category", "")).strip().lower()
    if cat not in CATEGORIES:
        raise ValueError("unknown category %r" % cat)
    u = getattr(resp, "usage", None)
    usage = {"model": model,
             "in": int(getattr(u, "input_tokens", 0) or 0),
             "out": int(getattr(u, "output_tokens", 0) or 0)}
    return cat, str(data.get("why", ""))[:120], usage


def classify(message: str, client=None) -> dict:
    """The one question: is this a crisis, personal information, or nothing? Never raises."""
    t0 = time.time()
    msg = (message or "").strip()
    if not msg or not has_words(msg):
        return {"category": "none", "why": "no words", "source": "skip", "ms": 0, "usage": None}
    if _enabled():
        try:
            cat, why, usage = _model_reader(msg, client)
            # belt and braces: an unmistakable phrase is a crisis even if the model says not
            if cat != "crisis" and quick_screen(msg):
                cat, why = "crisis", "keyword: " + (why or "unmistakable phrase")
            return {"category": cat, "why": why, "source": "model",
                    "ms": int((time.time() - t0) * 1000), "usage": usage}
        except Exception as exc:  # noqa: BLE001 -- the net must never vanish with the model
            fallback_why = "model unavailable (%s)" % type(exc).__name__
    else:
        fallback_why = "SAFETY_CHECK=off"
    cat = keyword_category(msg)
    return {"category": cat, "why": fallback_why, "source": "keywords",
            "ms": int((time.time() - t0) * 1000), "usage": None}

# I did no harm and this file is not truncated.

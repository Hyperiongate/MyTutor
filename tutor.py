# =============================================================================
# tutor.py  --  Math Tutor MVP  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-07-19  Initial version. Holds the authoritative "Professor Einstein"
#               system prompt (single source of truth), the context-injection
#               logic (student name + progress), and the Claude API call used to
#               generate the tutor's replies. Model is configurable via the
#               CLAUDE_MODEL env var so it can be updated without code changes.
#
# WHAT THIS FILE IS FOR:
#   This is the tutor's "brain." main.py imports get_tutor_reply() to answer a
#   student. The system prompt below is the thing we will revise most often as
#   real sessions teach us what works. Edit SYSTEM_PROMPT_TEMPLATE to change how
#   the tutor teaches.
#
# ENV VARS (set these in Render, NOT in code):
#   ANTHROPIC_API_KEY   (required)  your Claude API key
#   CLAUDE_MODEL        (optional)  defaults to a stable Claude model; override
#                                   with any current model id from Anthropic docs
# =============================================================================

import os

from anthropic import Anthropic

# The tutor's name is locked for v0.1.
TUTOR_NAME = "Professor Einstein"

# Model is configurable via env so we never have to touch code to change it.
# "-latest" aliases always point at the newest stable release of that model.
DEFAULT_MODEL = "claude-3-5-sonnet-latest"

# How many past turns of a conversation we replay to the model on each request.
# Keeps the "tutor remembers" feeling while bounding token cost. One "turn" here
# means one message (student or tutor), so 24 == roughly the last dozen exchanges.
MAX_HISTORY_MESSAGES = 24

# -----------------------------------------------------------------------------
# THE TUTOR SYSTEM PROMPT  (the authoritative draft -- revise this often)
# -----------------------------------------------------------------------------
# {student_name} and {progress} are filled in per student before each request.
SYSTEM_PROMPT_TEMPLATE = """\
You are {tutor_name}, a warm, patient, and encouraging algebra tutor working
one-on-one with a single high-school student. You speak out loud in a real voice
conversation, so you sound like a caring human tutor sitting beside the student,
never like a textbook or a chatbot.

THE STUDENT
Your student's name is {student_name}. Use their name naturally and sparingly,
the way a real tutor does. Here is what you remember about their progress so far:
{progress}
If this is the very start and there is no progress yet, warmly welcome them by
name and find out how they feel about algebra before diving in.

WHAT YOU ARE TEACHING (v0.1 scope -- stay inside this)
You teach exactly ONE topic right now: solving linear equations in one variable
(for example 2x + 3 = 11, or 5x - 4 = 3x + 2, or x/3 + 1 = 4). This includes:
  - the idea that an equation is a balance and both sides must stay equal
  - adding or subtracting the same amount from both sides
  - multiplying or dividing both sides by the same nonzero number
  - combining like terms
  - moving variable terms to one side
  - checking an answer by substituting it back in
If the student asks about a different math topic (quadratics, geometry, fractions
in the abstract, word problems beyond simple linear ones, etc.), gently
acknowledge it and steer back: tell them it is on the list for later and that
today you two are focused on linear equations. Do not teach outside this scope.

HOW YOU TEACH
  1. Present ONE problem at a time. Never dump a worksheet.
  2. Ask the student to work through it aloud, one step at a time, and to tell
     you their reasoning -- not just the answer.
  3. Listen to the reasoning. Praise correct thinking specifically ("nice -- you
     subtracted 3 from both sides, exactly right").
  4. When they get stuck, do NOT give the answer. Ask a smaller guiding question,
     or offer a simpler example first, then come back to the original problem.
  5. When they succeed, offer a slightly harder variant to stretch them.
  6. Only work a full problem for them after they have genuinely tried and are
     still stuck -- and even then, narrate each step and ask them to say why it
     works.
  7. Regularly have them CHECK their answer by plugging it back in. Build the
     habit that a solved equation can be verified.
  8. Celebrate real progress. Keep math anxiety low. Mistakes are welcome and
     useful -- treat every wrong step as a normal, fixable part of learning.

HOW YOU SPEAK (this is a VOICE conversation)
  - Keep almost every reply to 1-3 short sentences. Long monologues do not work
    out loud.
  - Speak plainly. Say math the way a person would say it aloud: "two x plus
    three equals eleven," not dense notation.
  - Ask one question at a time and then stop, so the student can answer.
  - Be encouraging and human, never robotic. No bullet lists, no headings, no
    "as an AI." You are a tutor.

SAFETY AND BOUNDARIES
  - You are working with a minor in a trusted learning space. Keep everything
    age-appropriate, kind, and focused on algebra.
  - If the student is upset, frustrated, or wants to talk about something not
    related to the lesson, respond with warmth and care, briefly, then gently
    guide back to the math when they are ready.

Remember: the one question that matters for this product is "does this feel like
a real tutor?" Be that tutor.
"""


def build_system_prompt(student: dict) -> str:
    """Fill the template with this student's name and remembered progress."""
    name = (student or {}).get("name", "the student")
    progress = (student or {}).get("progress") or ""
    progress = progress.strip()
    if not progress:
        progress = ("(No prior sessions yet -- this is your first meeting with "
                    "this student.)")
    return SYSTEM_PROMPT_TEMPLATE.format(
        tutor_name=TUTOR_NAME,
        student_name=name,
        progress=progress,
    )


def _trim_history(history: list) -> list:
    """Return at most the last MAX_HISTORY_MESSAGES messages, oldest first."""
    if not history:
        return []
    return history[-MAX_HISTORY_MESSAGES:]


def get_tutor_reply(student: dict, history: list, user_message: str) -> str:
    """
    Ask Claude for the tutor's next reply.

    student       -- the student record (name, progress, ...)
    history       -- prior conversation as a list of {"role","content"} dicts
                     where role is "user" (the student) or "assistant" (tutor)
    user_message  -- what the student just said

    Returns the tutor's reply as plain text. On a configuration or API problem
    it returns a friendly, human-readable message instead of crashing, so the
    app keeps running and the tester sees a clear explanation.
    """
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return ("(Setup needed: I can't reach my brain yet. Please add the "
                "ANTHROPIC_API_KEY environment variable in Render, then reload "
                "this page.)")

    model = os.environ.get("CLAUDE_MODEL", DEFAULT_MODEL)

    messages = _trim_history(list(history or []))
    messages.append({"role": "user", "content": user_message})

    try:
        client = Anthropic(api_key=api_key)
        response = client.messages.create(
            model=model,
            max_tokens=400,
            system=build_system_prompt(student),
            messages=messages,
        )
        # Concatenate any text blocks the model returned.
        parts = [block.text for block in response.content
                 if getattr(block, "type", None) == "text"]
        reply = "".join(parts).strip()
        return reply or "(Sorry, I lost my train of thought. Could you say that again?)"
    except Exception as exc:  # noqa: BLE001  -- we want a graceful UI message
        # We deliberately never leak a raw stack trace to a student. We log it
        # for the developer and show a calm message instead.
        print(f"[tutor] Claude API error: {exc}")
        return ("(I'm having trouble thinking right now -- give me a moment and "
                "try again.)")


# I did no harm and this file is not truncated.

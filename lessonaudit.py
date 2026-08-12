# =============================================================================
# lessonaudit.py  --  THE OFFLINE LESSON AUDITOR  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-08-11  BUILD dh -- three lessons from adjudicating the first FULL-CAST run
#               (Audit_Findings_2026-08-11.md):
#               (1) SCENARIOS CAN SEED A PROGRESS RECORD. The final-exam-locked finding
#               (E-1) could not be adjudicated because the audit student was a bare
#               {"progress": "Working in unit 9."} -- no mastery state, and this harness
#               calls tutor.get_tutor_reply directly, so main.py's real server-side
#               final-exam gate never runs here. The scenario now seeds an explicit
#               mastery picture (which units are mastered, which are checked-but-open and
#               at what best score), so the critic can legitimately mark whether the
#               tutor names the open units. NOTE, recorded so nobody re-litigates it:
#               the SERVER gate (_final_gate_message, build cu) is out of this harness's
#               reach by design and is proven by its own end-to-end test in that build.
#               (2) THE CRITIC LEARNS THE BOARD'S CASE CONVENTION (discipline check 4).
#               It flagged "x^2 - 3X - 10" as inconsistent notation -- but the student's
#               board renders EVERY single-letter variable as a red CAPITAL regardless of
#               the case in the tag (session.html styleVars), so tag-level case mixing is
#               invisible to the student. Findings about it are noise.
#               (3) THE CRITIC LEARNS OUR DECIDED DESIGNS (discipline check 5). Three of
#               its findings re-litigated the sanctioned rule-39(d) check-in wording, and
#               one re-litigated rule 50's student agency. Decided designs are not
#               findings; the checks name both so the next run spends its attention on
#               real defects.
#   2026-08-10  BUILD dc -- COUNT THE STUMBLES. The first full audit's most important
#               finding was made by a human reading the transcripts, not by the critic:
#               four graceful-failure turns in ten lessons. A critic marking content
#               reads straight past absence. Fallback turns are now detected by string
#               (FALLBACK_MARKERS), retried once, counted per lesson and in the summary,
#               and injected as a code-made reliability finding the marker cannot argue
#               away. The critic prompt gained three discipline checks from its own
#               false positives (the removable-discontinuity graph it called wrong, the
#               board line it called missing while quoting it).
#   2026-08-10  BUILD db -- ROOM TO THINK. Jim's probe marked gpt-5.1 unusable on a
#               5-token budget: a reasoning model had spent the whole budget thinking.
#               "Output limit reached" is proof of access, not absence of it. Retry once
#               with a roomy budget (4x or +3000) when the API says the output limit was
#               hit -- and likewise for the quiet variant, a 200 whose message is empty
#               with finish_reason "length". Without this, running the audit on gpt-5.5
#               would have killed every 120-token student turn.
#   2026-08-10  BUILD da -- probe_models(). Jim asked how to tell whether a new key can
#               use gpt-5.5. There is no way to tell by looking, so this asks the key: one
#               tiny call per candidate, strongest first, overridable via
#               OPENAI_PROBE_MODELS. The verification case is named with its remedy
#               because OpenAI gates the GPT-5 family behind organisation verification and
#               a bare 403 tells nobody what to do next. dry_run() now runs the probe, so
#               the /admin pricing button answers the question in one click.
#   2026-08-10  BUILD cz -- FIXES FROM THE FIRST REAL RUN. It failed, and usefully.
#               * max_tokens -> negotiated token parameter (newer models want
#                 max_completion_tokens). Ask the API, do not guess from the name.
#               * NEW preflight(): one tiny call proves key + model + parameter BEFORE any
#                 lesson. The failing run cost 89.9 seconds and two live tutor calls to
#                 learn a parameter name; it should cost a second.
#               * default model gpt-5.5 -> gpt-4.1, which his key actually reaches.
#               * the model list is offered only on a genuine model error, not on any
#                 message containing the word "model".
#               * the summary tells the truth: a run where nothing was marked no longer
#                 reads as "0 findings", which is what a clean audit reads as.
#   2026-08-10  BUILD cw -- NEW FILE. Jim: "I need to build some sort of
#               effectiveness/reality check so we don't keep having these problems."
#
# WHAT THIS IS, AND WHY IT IS NOT IN THE LIVE PATH
# -----------------------------------------------------------------------------
# Two things check quality today, and there is a gap between them.
#   * ruletests.py checks the CODE and the WORDS OF THE PROMPT. It can prove a rule is
#     in there and that a board tag will draw. It cannot judge teaching.
#   * Jim, reading lessons one at a time. He found the f(x) gap, the hole with no cause,
#     and a mastery bar nobody could clear. He is the only thing looking at the actual
#     teaching, and that does not scale past him.
#
# This closes that gap. It runs real lessons and has an INDEPENDENT model mark them.
#
# Jim asked whether we should instead review every live reply with a second model before
# posting it. We decided against it, and the reason is worth keeping: every defect found
# so far was a MISSING SPECIFICATION, not a bad day. f(x) was never taught because no
# script existed. The hole had no cause because no rule required one. The mastery bar was
# unreachable because nobody multiplied 90% by five questions. A live reviewer catches
# things like that SOMETIMES and lets them through next Tuesday; a rule plus a test closes
# them forever, for free. Live review would also double per-turn cost and put a pause in
# front of a voice tutor, which is the product.
#
# HOW IT WORKS
# -----------------------------------------------------------------------------
#   1. OpenAI PLAYS THE STUDENT from a persona ("you are eight, you are stuck on
#      fractions, answer in one short sentence"). Deliberately not a hand-written script:
#      a scripted student only ever walks the paths we thought of, and the bugs live in
#      the paths we did not.
#   2. Claude is the TUTOR, through tutor.get_tutor_reply -- the real prompt, the real
#      rules, the real board tags. Nothing is mocked.
#   3. OpenAI then CRITIQUES the finished transcript against the generated rule index, as
#      a picky mathematics teacher: what was asserted with no reason, what symbol was
#      written but never read aloud, which rule number does this break.
#   4. It writes a report. A HUMAN reads it and turns real findings into a rule and a
#      test. NOTHING here edits the teaching. A critic can be wrong, and a wrong critic
#      quietly sanding down good teaching is the exact failure we are trying to avoid.
#
# A DIFFERENT VENDOR ON PURPOSE. Claude checking Claude agrees with itself. Independent
# training means independent blind spots, which is the whole point of a second opinion.
#
# RUNNING IT
# -----------------------------------------------------------------------------
#   Locally:  python lessonaudit.py --dry-run          # cost estimate, spends nothing
#             python lessonaudit.py --limit 2          # two scenarios
#             python lessonaudit.py                    # the whole cast
#   On Render (this is how Jim runs it -- the keys live there, and only there):
#             POST /api/admin/lesson-audit {key, dry_run:true}
#             POST /api/admin/lesson-audit {key, limit:2, offset:0}
#
# ⚠️ KEYS. Read from the environment, never printed, never returned, never logged. The
# only thing this file ever says about a key is whether one is present.
# ⚠️ MODEL NAMES MOVE. OPENAI_AUDIT_MODEL sets it. If the configured model is rejected,
# this asks the API which models the account actually has and names them in the error,
# so a stale default is a one-line fix and never a mystery.
# =============================================================================
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import tutor  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))

OPENAI_URL = "https://api.openai.com/v1/chat/completions"
OPENAI_MODELS_URL = "https://api.openai.com/v1/models"
# Overridable because model names move faster than this file will. A wrong default is not
# a silent failure here: see _openai(), which asks the account what it has.
# 2026-08-10 (build cz): default changed gpt-5.5 -> gpt-4.1 after Jim's first live run
# listed what his key can actually reach. Picking a default from a press release rather
# than from the account is how the first run burned 90 seconds to say "no".
AUDIT_MODEL = os.environ.get("OPENAI_AUDIT_MODEL", "gpt-4.1")
TURNS = int(os.environ.get("AUDIT_TURNS", "8"))          # student turns per lesson

# ESTIMATES ONLY, for the dry run -- published prices change and these are not read from
# anywhere authoritative. The dry run says so out loud. The real number is on the two
# billing dashboards after a run.
EST_CLAUDE_PER_TURN = 0.03      # a lesson turn, mostly cached prompt
EST_OPENAI_PER_1K = 0.004       # blended in/out, the student turns and the critique


# =============================================================================
# THE CAST. Each one exists to expose a class of failure we have actually been bitten by
# -- the note says which, so nobody deletes a scenario without knowing what it guarded.
# =============================================================================
SCENARIOS = [
    dict(id="fractions-lost", course="basic", unit=2,
         exposes="rule 36-38 foundation-first, rule 39 turn length and failable check-ins, "
                 "rule 44 read the problem aloud. A confused young child is where a tutor "
                 "most easily talks too long and asks a question that cannot fail.",
         persona="You are 8 years old and you are stuck on fractions. You are polite but "
                 "you get lost easily. Answer in ONE short sentence, the way a child "
                 "speaks. If you do not follow something, say so plainly. Sometimes say "
                 "'yes' when you have not really understood -- children do that. Never "
                 "explain that you are an AI.",
         opening="I have to do fractions for homework and I don't get it"),
    dict(id="order-of-operations", course="prealgebra", unit=1,
         exposes="rule 49 (a wrong answer is the output of a RULE), rules 20-22. The "
                 "student runs left to right; if the tutor just corrects the number, the "
                 "broken rule survives and fires again next week.",
         persona="You are 12. You are confident and quick. You evaluate arithmetic strictly "
                 "left to right and you are sure that is correct. Answer in one short "
                 "sentence. Do not volunteer that you are making an error. If corrected, "
                 "push back once before you consider it. Never say you are an AI.",
         opening="3 + 2 x 4 is 20 right"),
    dict(id="limits-hole", course="calculus", unit=1,
         exposes="rule 51 (a feature on the board must belong to the function) and rule 1. "
                 "This is Jim's own catch: a hole asserted on y = x^2, which has no hole, "
                 "and an approach narrated as though the curve stopped at the point.",
         persona="You are a bright student meeting limits for the first time. You ask "
                 "precise, slightly sceptical questions when something is asserted without "
                 "a reason. One or two sentences. Never say you are an AI.",
         opening="can you explain what a limit is"),
    dict(id="function-notation", course="algebra1", unit=3,
         exposes="rule 48 (teach them how to SAY the symbol) and rule 14. The exact gap "
                 "Jim hit live: f(x) written on the board, never read aloud, then g(x).",
         persona="You are 13, meeting function notation for the first time. You read "
                 "symbols out loud incorrectly when you guess. One or two sentences. Never "
                 "say you are an AI.",
         opening="my book has f(x) in it and I don't know what that means"),
    dict(id="decimal-alignment", course="prealgebra", unit=5,
         exposes="the misconception catalogue and the board referees: a wrong answer must "
                 "never be adopted in words, and every computation asked must be on the "
                 "board with a '?' line (rules 15, 18).",
         persona="You are 12 and you line decimals up by their last digit instead of the "
                 "decimal point. You are willing but you make that same mistake "
                 "consistently. One short sentence. Never say you are an AI.",
         opening="whats 3.5 + 0.47"),
    dict(id="quiz-eighty", course="prealgebra", unit=4,
         exposes="rule 45 (the tally is arithmetic), rule 47 (no cold quizzes), rule 50 "
                 "(an unfinished unit is your job). A student who scores 8/10 has passed "
                 "nothing and must be offered review and a retake, warmly.",
         persona="You are 12. You want to take the unit quiz right now and get it over "
                 "with. You will get most questions right and miss one or two. Answer with "
                 "just your answer, briefly. Never say you are an AI.",
         opening="can I take the unit quiz on percents now"),
    dict(id="i-dont-know", course="basic", unit=3,
         exposes="rules 23-27 (the escalating ladder) and rule 39(e). A student who says "
                 "'I don't know' twice is where a tutor either gives the answer away or "
                 "repeats itself louder.",
         persona="You are 9. You say 'I don't know' a lot, and you mean it. You will "
                 "engage if something concrete is put in front of you. Very short answers. "
                 "Never say you are an AI.",
         opening="I don't know how to do any of this"),
    dict(id="geometry-picture", course="geometry", unit=4,
         exposes="rules 1, 2, 7, 8 and rule 41 (every picture carries a caption naming "
                 "what to NOTICE). Geometry is where a tutor most often describes a figure "
                 "it never drew.",
         persona="You are 14 working on triangles. You ask to SEE things ('can you show "
                 "me?'). One or two sentences. Never say you are an AI.",
         opening="I need to find the missing side of a right triangle"),
    dict(id="final-exam-locked", course="prealgebra", unit=9,
         exposes="the Final Exam gate (build cu) and rule 50. The student is short of "
                 "mastery and must be told WHICH units, and offered the retake -- not just "
                 "'you have mastered 3 of 9'. The progress seed below IS the test: units "
                 "4 and 7 are open at named best scores, so a correct reply names BOTH, "
                 "offers review and retake, and says the record keeps their best score.",
         # build dh (E-1): this harness bypasses main.py's server-side gate by design,
         # so the scenario must carry the mastery picture the real path would load.
         progress=("Working in unit 9. Units mastered: 1, 2, 3, 5, 6, 8. "
                   "Checked but not yet mastered: Unit 4 (Fractions, best score 85%), "
                   "Unit 7 (Percents, best score 80%). Unit 9 in progress, no quiz yet. "
                   "The Final Exam stays locked until every unit is mastered."),
         persona="You are 13 and impatient. You want to take the final exam now. You "
                 "answer briefly and you push back when told to wait. Never say you are "
                 "an AI.",
         opening="I want to take the final exam"),
    dict(id="returning-student", course="algebra2", unit=2,
         exposes="the opener rules, foundation memory (rule 40: ASK, do not replay) and "
                 "rule 42 (never compare this student to anyone else).",
         persona="You are 15, coming back after a week away. You half-remember the last "
                 "topic. Short answers. Never say you are an AI.",
         opening="I'm back, what were we doing again"),
]

CRITIC_SYSTEM = """\
You are a mathematics teacher with twenty years in a classroom, reviewing a transcript
from an AI tutor before it is used with real children. You are respected because you are
specific and because you do not pad your reviews with praise.

You will be given the tutor's RULE INDEX and one lesson transcript.

Report only things that are ACTUALLY WRONG in this transcript. In particular hunt for:
  * anything ASSERTED WITHOUT A REASON -- a feature on a graph the function does not
    have, a step that appears with no justification, a claim a knowledgeable student
    would answer with "says who?"
  * MATHEMATICS THAT IS WRONG, imprecise, or true only by accident
  * a symbol WRITTEN but never SAID out loud, or said in a way a student could not repeat
  * a question the student cannot answer wrongly ("does that make sense?" alone)
  * a wrong answer CORRECTED but the student's broken rule left intact
  * a picture referred to in words that does not appear as a board tag
  * anything a bright student would find confusing, and why

Board tags look like [[step eq="..."]] or [[graph ...]]. Treat a tag as the thing being
drawn on the board. The student cannot see anything that is not in a tag.

Do NOT report: tone, warmth, length, formatting, or anything you merely think could be
phrased better. Do NOT invent rule numbers. If the transcript is clean, say so - a clean
report is a useful result and you will not be thought lazy for returning one.

Three discipline checks, added after your predecessor's first marking run (each cost a
human time to reject):
1. BEFORE you flag, re-read the surrounding turns. A claim that was derived or justified
   EARLIER in the transcript is not an unjustified assertion. (Example from that run: a
   graph of y = x+2 with a hole at x = 2 was flagged as a false feature -- but the
   transcript had just cancelled (x^2-4)/(x-2) to x+2 with x != 2, and the line-with-a-
   point-removed IS the standard, correct graph of that rational function.)
2. BEFORE you flag a missing board line or missing spoken words, SEARCH the reply for
   them. If your suggested fix already appears in the transcript, you have no finding.
3. Mathematics that is correct under standard conventions is never a finding, however
   surprising it looks.
4. THE BOARD'S CASE CONVENTION: the student's screen renders every single-letter
   variable as a red CAPITAL letter, whatever the case inside the tag -- so
   "x^2 - 3X - 10" displays perfectly consistently. Case mixing inside a tag is
   invisible to the student and is NOT a finding.
5. DECIDED DESIGNS ARE NOT FINDINGS. Two you will be tempted by: (a) the check-in
   "...or should I show it a different way?" is REQUIRED wording (the rules ban the
   bare "does that make sense?" and mandate exactly this escape-hatch form -- flag only
   the bare form asked alone); (b) a student MAY choose to move past an unfinished unit
   once the tutor has raised it -- rule 50 preserves that agency on purpose; flag only a
   tutor who never raised it at all. And an OFFER ("Want to try one more, or move on?")
   is an invitation, not an understanding check, and needs no pending board line.

Return STRICT JSON only, no prose around it:
{"findings":[{"severity":"high|medium|low","rule":<number or null>,
  "what":"<one sentence: what is wrong>",
  "quote":"<the exact words from the transcript that are wrong>",
  "why":"<why it misleads a student>",
  "fix":"<the concrete change you would make>"}],
 "verdict":"<one sentence overall>"}
severity high = a student would learn something false or be unable to follow.
"""


# =============================================================================
# OPENAI TRANSPORT
# =============================================================================
# Which token-limit parameter this model wants. The newer models reject "max_tokens" and
# require "max_completion_tokens"; the older ones are the other way round. We do not guess
# from the model NAME -- names change and guessing is how you ship a break. We try one,
# and if the API tells us it wanted the other we switch and remember for the rest of the
# run. Learned from Jim's first real run, which failed on exactly this after spending 90
# seconds and two live tutor calls first.
_TOKEN_PARAM = "max_completion_tokens"


def _openai(messages, max_tokens=900, want_json=False, model=None, _retry=True):
    """One OpenAI chat call. Returns (text, error). Never raises, never logs the key."""
    global _TOKEN_PARAM
    import httpx
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not key:
        return None, ("no OPENAI_API_KEY in the environment. On Render: add it to the "
                      "service's Environment tab; it is never sent anywhere else.")
    body = {"model": model or AUDIT_MODEL, "messages": messages,
            _TOKEN_PARAM: max_tokens}
    if want_json:
        body["response_format"] = {"type": "json_object"}
    try:
        r = httpx.post(OPENAI_URL, json=body, timeout=120.0,
                       headers={"Authorization": f"Bearer {key}"})
    except Exception as exc:  # noqa: BLE001
        return None, f"could not reach OpenAI: {exc}"
    if r.status_code == 200:
        try:
            choice = r.json()["choices"][0]
            content = choice["message"]["content"]
            # A reasoning model can also fail QUIETLY: 200, finish_reason "length", and
            # an empty message, because the whole budget went to thinking. An empty
            # student turn would end the lesson early and look like the student left.
            if (_retry and not (content or "").strip()
                    and (choice.get("finish_reason") == "length")):
                roomy = max(max_tokens * 4, max_tokens + 3000)
                print(f"[audit] empty message with finish_reason=length; "
                      f"retrying with {roomy} tokens")
                return _openai(messages, roomy, want_json, model, _retry=False)
            return content, None
        except Exception as exc:  # noqa: BLE001
            return None, f"unexpected OpenAI response shape: {exc}"
    detail = ""
    code = ""
    try:
        err = (r.json().get("error") or {})
        detail = err.get("message", "")
        code = (err.get("code") or "") + " " + (err.get("param") or "")
    except Exception:  # noqa: BLE001
        detail = (r.text or "")[:200]
    low = detail.lower()

    # THE TOKEN-PARAMETER SWAP. The API names the parameter it wanted; take it at its word.
    if _retry and r.status_code == 400 and "max_tokens" in low and "max_completion_tokens" in low:
        _TOKEN_PARAM = ("max_completion_tokens" if "'max_tokens' is not supported" in low
                        else "max_tokens")
        print(f"[audit] switching token parameter to {_TOKEN_PARAM} and retrying")
        return _openai(messages, max_tokens, want_json, model, _retry=False)

    # THE REASONING BUDGET (2026-08-10, build db, found by Jim's second probe). A
    # reasoning-family model spends tokens THINKING before it writes a word, and that
    # spending counts against max_completion_tokens -- so a tiny budget comes back as
    # "Could not finish the message because max_tokens or model output limit was
    # reached", which LOOKS like no-access and is actually proof of access (the request
    # was accepted, billed, and answered -- with thinking). Jim's probe called gpt-5.1
    # unusable for exactly this reason, on a 5-token budget. Same philosophy as the
    # parameter swap: the API told us what was wrong, so take it at its word and retry
    # once with room to think. Never guessed from the model name.
    if (_retry and r.status_code == 400
            and "output limit was reached" in low):
        roomy = max(max_tokens * 4, max_tokens + 3000)
        print(f"[audit] model spent the budget reasoning; retrying with {roomy} tokens")
        return _openai(messages, roomy, want_json, model, _retry=False)

    # Only a genuine MODEL problem earns the model list. The first version appended it to
    # anything containing the word "model", which is how a parameter error came back
    # wearing a costume -- true information, wrong diagnosis, and Jim had to read past it.
    if (r.status_code in (400, 404)
            and ("model_not_found" in code or "does not exist" in low
                 or "do not have access" in low or "invalid model" in low)):
        names = _openai_model_names(key)
        if names:
            detail += ("  |  models available on this account: " + ", ".join(names[:25])
                       + ".  Set OPENAI_AUDIT_MODEL to one of these.")
    return None, f"OpenAI {r.status_code}: {detail}"


# The models worth asking about, strongest first. This is a PROBE LIST, not a promise --
# the only authority on what a key can reach is the key itself, which is why we ask it.
PROBE_MODELS = [m.strip() for m in os.environ.get(
    "OPENAI_PROBE_MODELS",
    "gpt-5.5,gpt-5.1,gpt-5,gpt-4.1,gpt-4o,gpt-4o-mini").split(",") if m.strip()]


def probe_models(candidates=None):
    """Ask the KEY which models it can actually use, one tiny call each.

    2026-08-10 (build da). Jim, holding a new key: "how can I tell if it's for chat five
    point five?" There is no way to tell by looking -- a key carries no model list, and a
    key's access is a property of the ORGANISATION (and, for project keys, of the
    project's model permissions). The only honest answer is to try it, cheaply.

    Returns a list of {model, ok, why} in the order asked. Costs a fraction of a cent per
    model and about a second each. Never raises."""
    out = []
    for name in (candidates or PROBE_MODELS):
        text, err = _openai([{"role": "user", "content": "Reply with: ok"}],
                            max_tokens=5, model=name)
        if not err:
            out.append({"model": name, "ok": True, "why": "usable with this key"})
            continue
        low = (err or "").lower()
        # OpenAI is explicit about this one and it has a specific remedy, so say the
        # remedy rather than making somebody paste an error into a search box.
        if "must be verified" in low or "verify" in low:
            why = ("this model needs ORGANISATION VERIFICATION -- OpenAI platform "
                   "Settings > General > Verify Organisation (photo ID + a live selfie). "
                   "Access switches on about 15 minutes after approval.")
        elif "does not exist" in low or "do not have access" in low or "model_not_found" in low:
            why = "not available to this key"
        else:
            why = err
        out.append({"model": name, "ok": False, "why": why})
    return out


def preflight():
    """Prove the OpenAI side works BEFORE any lesson runs. One tiny call, a fraction of a
    cent, about a second.

    Jim's first real run spent 89.9 seconds and two live tutor calls before failing on a
    parameter name. Everything that can be wrong here -- missing key, wrong model name,
    wrong token parameter, no network -- is knowable in one cheap round trip, and finding
    out cheaply is the difference between a typo and a wasted afternoon.
    Returns (ok, message)."""
    text, err = _openai([{"role": "user", "content": "Reply with the single word: ready"}],
                        max_tokens=5)
    if err:
        return False, err
    return True, f"OpenAI reachable · model {AUDIT_MODEL} · token parameter {_TOKEN_PARAM}"


def _openai_model_names(key):
    """The chat-capable model ids this account can actually use. Best effort."""
    import httpx
    try:
        r = httpx.get(OPENAI_MODELS_URL, timeout=30.0,
                      headers={"Authorization": f"Bearer {key}"})
        if r.status_code != 200:
            return []
        ids = [m.get("id", "") for m in (r.json().get("data") or [])]
        return sorted(i for i in ids if i.startswith(("gpt", "o1", "o3", "o4")))
    except Exception:  # noqa: BLE001
        return []


# =============================================================================
# RUNNING ONE LESSON
# =============================================================================
def _rules_text():
    """The generated rule index. RULES.md if it is present (it is committed), otherwise
    regenerate from the prompt so the critic is never marking against a stale list."""
    path = os.path.join(HERE, "RULES.md")
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read()
    except OSError:
        try:
            import ruletests
            return ruletests.rules_markdown()      # same generator, if it is exposed
        except Exception:  # noqa: BLE001
            return "(rule index unavailable -- judge on mathematics and clarity alone)"


def _student_turn(sc, transcript):
    """OpenAI, in character, says the next student thing."""
    recent = transcript[-8:]
    convo = "\n".join(f"{'TUTOR' if r == 'assistant' else 'YOU'}: {t}" for r, t in recent)
    msgs = [{"role": "system", "content": sc["persona"] +
             "\n\nYou are in a maths lesson. Reply with ONLY what you would say next -- no "
             "stage directions, no quotation marks, no explanation."},
            {"role": "user", "content": f"The lesson so far:\n\n{convo}\n\nWhat do you say next?"}]
    text, err = _openai(msgs, max_tokens=120)
    if err:
        return None, err
    return (text or "").strip().strip('"'), None


# The tutor's own graceful-failure apologies. get_tutor_reply never raises to a
# student; it returns one of these instead -- "lost my train of thought" when the model
# came back EMPTY after retries, "having trouble thinking" when the API call itself
# failed (rate limit, overload, network). In a real classroom each one is a turn the
# student watches the tutor stumble.
# 2026-08-10 (build dc): Jim's first full audit had FOUR of these across ten lessons --
# one scenario opened with two in a row -- and the CRITIC read straight past every one,
# because a critic marking mathematics does not think to mark absence. Counting them is
# code's job. Frequency is the finding: one is weather, four in ten lessons is a rate.
FALLBACK_MARKERS = ("lost my train of thought", "having trouble thinking right now")


def _is_fallback(reply: str) -> bool:
    low = (reply or "").lower()
    return any(m in low for m in FALLBACK_MARKERS)


def run_scenario(sc, turns=TURNS):
    """Play one lesson. Returns (transcript, error, fallbacks). Transcript is
    [(role, text), ...]; fallbacks counts tutor turns that came back as an apology."""
    # build dh: a scenario may seed a full progress record (mastery state, open units,
    # best scores) -- the harness calls the tutor directly, so anything main.py would
    # normally load onto the student must arrive through the scenario itself.
    student = {"name": "Audit Student", "code": "AUDIT",
               "progress": sc.get("progress") or f"Working in unit {sc.get('unit', 1)}."}
    transcript = [("user", sc["opening"])]
    history = []
    fallbacks = 0
    for i in range(turns):
        try:
            reply = tutor.get_tutor_reply(dict(student), list(history), transcript[-1][1],
                                          course=sc["course"], code="AUDIT")
            if _is_fallback(reply):
                # Count it, then retry ONCE -- an audit lesson derailed by a transient
                # API hiccup marks nothing, and a real student would simply repeat
                # themselves, which is exactly what this does.
                fallbacks += 1
                time.sleep(2)
                retry = tutor.get_tutor_reply(dict(student), list(history),
                                              transcript[-1][1],
                                              course=sc["course"], code="AUDIT")
                if not _is_fallback(retry):
                    reply = retry
                else:
                    fallbacks += 1
        except Exception as exc:  # noqa: BLE001
            return transcript, f"tutor call failed on turn {i + 1}: {exc}", fallbacks
        transcript.append(("assistant", reply))
        history.append({"role": "user", "content": transcript[-2][1]})
        history.append({"role": "assistant", "content": reply})
        if i == turns - 1:
            break
        say, err = _student_turn(sc, transcript)
        if err:
            return transcript, err, fallbacks
        if not say:
            break
        transcript.append(("user", say))
    return transcript, None, fallbacks


def critique(sc, transcript):
    """Mark one transcript. Returns (findings_dict, error)."""
    body = "\n\n".join(f"{'TUTOR' if r == 'assistant' else 'STUDENT'}: {t}"
                       for r, t in transcript)
    msgs = [{"role": "system", "content": CRITIC_SYSTEM},
            {"role": "user", "content":
                f"THE TUTOR'S RULE INDEX:\n\n{_rules_text()[:60000]}\n\n"
                f"=====\n\nTRANSCRIPT (course: {sc['course']}, this scenario exists to "
                f"expose: {sc['exposes']}):\n\n{body}"}]
    text, err = _openai(msgs, max_tokens=2000, want_json=True)
    if err:
        return None, err
    try:
        return json.loads(text), None
    except Exception:  # noqa: BLE001
        start, end = (text or "").find("{"), (text or "").rfind("}")
        if start >= 0 and end > start:
            try:
                return json.loads(text[start:end + 1]), None
            except Exception:  # noqa: BLE001
                pass
        return None, f"critic did not return JSON: {(text or '')[:200]}"


# =============================================================================
# THE RUN
# =============================================================================
def dry_run(limit=None, offset=0, turns=TURNS, probe=True):
    """Price the job, and prove the key -- without teaching a single lesson.

    2026-08-10 (build da): this used to be pure arithmetic and could therefore tell you a
    price for a job that could not run at all. It now also ASKS THE KEY which models it
    can reach, which is the question a person actually has when they paste in a new one.
    Not free any more, but a fraction of a cent -- and honest about that."""
    picked = SCENARIOS[offset:offset + limit] if limit else SCENARIOS[offset:]
    claude = len(picked) * turns * EST_CLAUDE_PER_TURN
    # per scenario: (turns-1) student turns, each small, plus one big critique
    openai_k = len(picked) * (((turns - 1) * 1.2) + 22)
    return {
        "ok": True, "dry_run": True,
        "scenarios": [{"id": s["id"], "course": s["course"], "exposes": s["exposes"]}
                      for s in picked],
        "turns_each": turns,
        "have_openai_key": bool(os.environ.get("OPENAI_API_KEY")),
        "have_anthropic_key": bool(os.environ.get("ANTHROPIC_API_KEY")),
        "model": AUDIT_MODEL,
        "estimated_cost_usd": round(claude + openai_k * EST_OPENAI_PER_1K, 2),
        "estimate_note": ("ESTIMATE ONLY -- built from assumed per-token prices, not read "
                          "from either vendor. Read the real figure off the two billing "
                          "dashboards after the first run and correct the constants at "
                          "the top of lessonaudit.py."),
        "models": (probe_models() if (probe and os.environ.get("OPENAI_API_KEY", "").strip())
                   else []),
        "token_parameter": _TOKEN_PARAM,
    }


def audit(limit=None, offset=0, turns=TURNS):
    """Run the batch and mark it. Returns a plain dict -- no printing, so the endpoint
    and the command line can both use it."""
    picked = SCENARIOS[offset:offset + limit] if limit else SCENARIOS[offset:]
    started = time.time()
    # FAIL FAST AND CHEAP. One tiny call proves the key, the model and the token parameter
    # before a single lesson is taught. Jim's first run spent 89.9 seconds and two live
    # tutor calls to discover a parameter name.
    ok, note = preflight()
    if not ok:
        return {"ok": False, "dry_run": False, "model": AUDIT_MODEL,
                "scenarios_run": 0, "findings": 0, "high": 0, "did_not_complete": 0,
                "seconds": round(time.time() - started, 1), "results": [],
                "preflight_error": note,
                "summary": f"Nothing was run. The OpenAI side failed its preflight: {note}"}
    results = []
    for sc in picked:
        t0 = time.time()
        transcript, err, fallbacks = run_scenario(sc, turns)
        row = {"id": sc["id"], "course": sc["course"], "exposes": sc["exposes"],
               "turns": len(transcript), "seconds": round(time.time() - t0, 1),
               "fallbacks": fallbacks,
               "transcript": [{"who": r, "text": t} for r, t in transcript]}
        if err:
            row["error"] = err
            results.append(row)
            continue
        marked, cerr = critique(sc, transcript)
        if cerr:
            row["error"] = cerr
        else:
            row["verdict"] = marked.get("verdict", "")
            row["findings"] = marked.get("findings", []) or []
        # THE FINDING THE CRITIC CANNOT MAKE: reliability. Injected by CODE, at a fixed
        # severity, so it can never be argued away by a generous marker.
        if fallbacks:
            row.setdefault("findings", []).append({
                "severity": "high" if fallbacks >= 2 else "medium",
                "rule": None,
                "what": f"the tutor stumbled {fallbacks} time(s) -- turns came back as "
                        f"the graceful-failure apology instead of teaching",
                "quote": "(Sorry, I lost my train of thought. Could you say that again?)",
                "why": "a real student watches the tutor fail and repeats themselves; "
                       "'lost my train of thought' means the model returned EMPTY, "
                       "'having trouble thinking' means the API call itself failed -- "
                       "check the Render logs from this run's timestamps for the cause",
                "fix": "read the [tutor] error lines in the Render logs; if these are "
                       "rate limits from back-to-back audit lessons they will not affect "
                       "single students, but if they appear in live traffic too, that is "
                       "a product problem",
            })
        results.append(row)
    high = sum(1 for r in results for f in (r.get("findings") or [])
               if (f.get("severity") or "").lower() == "high")
    total = sum(len(r.get("findings") or []) for r in results)
    # ⚠️ HONESTY IN THE HEADLINE. The first version reported "2 scenarios · 0 findings"
    # for a run in which BOTH scenarios died before a single word was marked. Zero
    # findings and zero lessons marked are opposite results and must never read the same.
    stumbles = sum(r.get("fallbacks", 0) for r in results)
    failed = sum(1 for r in results if r.get("error"))
    marked = len(results) - failed
    if marked == 0 and failed:
        summary = (f"NOTHING WAS MARKED. All {failed} lesson(s) failed to complete -- see "
                   f"the reason on each below. This is not a clean audit.")
    elif failed:
        summary = (f"{marked} lesson(s) marked, {total} finding(s) ({high} serious). "
                   f"⚠️ {failed} lesson(s) did NOT complete, so this audit is partial.")
    else:
        summary = f"{marked} lesson(s) marked, {total} finding(s) ({high} serious)."
    if stumbles:
        summary += (f" The tutor stumbled {stumbles} time(s) across the batch "
                    f"(graceful-failure turns -- see the reliability finding).")
    return {"ok": True, "dry_run": False, "model": AUDIT_MODEL,
            "scenarios_run": len(results), "lessons_marked": marked,
            "did_not_complete": failed, "findings": total, "high": high,
            "tutor_stumbles": stumbles,
            "seconds": round(time.time() - started, 1), "summary": summary,
            "results": results}


def report_markdown(run):
    """The human-readable report. Findings first -- the transcripts are evidence, and
    nobody reads evidence they have not been given a reason to read."""
    from datetime import datetime, timezone
    when = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    fails = run.get("did_not_complete", 0)
    out = [f"# Lesson audit — {when}", "",
           f"_Model: {run.get('model')} · {run.get('lessons_marked', run.get('scenarios_run'))} "
           f"lesson(s) marked · {run.get('findings')} findings ({run.get('high')} high)"
           + (f" · ⚠️ {fails} DID NOT COMPLETE" if fails else "")
           + f" · {run.get('seconds')}s_", "",
           f"**{run.get('summary', '')}**", "",]
    if run.get("preflight_error"):
        out += [f"> The OpenAI side never answered, so no lesson was taught: "
                f"`{run['preflight_error']}`", ""]
    out += [
           "Nothing here has been acted on. A finding is an OPINION from an independent "
           "model; read the quoted words yourself before changing anything. A real one "
           "becomes a rule AND a test in the same commit.", ""]
    for r in run.get("results", []):
        out.append(f"## {r['id']}  ·  {r['course']}")
        out.append(f"_Guards: {r['exposes']}_")
        if r.get("error"):
            out += ["", f"**Did not complete:** {r['error']}", ""]
            continue
        out += ["", f"**Verdict:** {r.get('verdict', '')}", ""]
        fs = r.get("findings") or []
        if not fs:
            out += ["No findings.", ""]
        for f in fs:
            sev = (f.get("severity") or "?").upper()
            rule = f" · rule {f['rule']}" if f.get("rule") else ""
            out += [f"### {sev}{rule} — {f.get('what', '')}",
                    f"> {f.get('quote', '')}", "",
                    f"**Why it misleads:** {f.get('why', '')}", "",
                    f"**Suggested fix:** {f.get('fix', '')}", ""]
        out += ["<details><summary>transcript</summary>", ""]
        for line in r.get("transcript", []):
            who = "**Mr. Cadabra:**" if line["who"] == "assistant" else "**Student:**"
            out.append(f"{who} {line['text']}")
            out.append("")
        out += ["</details>", ""]
    out.append("I did no harm and this file is not truncated.")
    return "\n".join(out)


def main():
    args = sys.argv[1:]

    def opt(name, default=None):
        if name in args:
            i = args.index(name)
            if i + 1 < len(args):
                return args[i + 1]
        return default

    limit = int(opt("--limit", 0)) or None
    offset = int(opt("--offset", 0))
    turns = int(opt("--turns", TURNS))
    if "--dry-run" in args:
        d = dry_run(limit, offset, turns)
        print(f"\nLESSON AUDIT — DRY RUN (nothing is spent)\n")
        print(f"  model             {d['model']}")
        print(f"  OPENAI_API_KEY    {'present' if d['have_openai_key'] else 'MISSING'}")
        print(f"  ANTHROPIC_API_KEY {'present' if d['have_anthropic_key'] else 'MISSING'}")
        print(f"  scenarios         {len(d['scenarios'])} × {d['turns_each']} turns")
        for s in d["scenarios"]:
            print(f"    - {s['id']:<20} {s['course']}")
        if d.get("models"):
            print("\n  what this key can actually reach:")
            for m in d["models"]:
                print(f"    {'YES' if m['ok'] else 'no '}  {m['model']:<12} {m['why'][:80]}")
        print(f"\n  estimated cost    ${d['estimated_cost_usd']}")
        print(f"  {d['estimate_note']}\n")
        return 0
    run = audit(limit, offset, turns)
    md = report_markdown(run)
    path = os.path.join(HERE, "lesson_audit_report.md")
    try:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(md)
        print(f"\nwrote {path}")
    except OSError as exc:
        print(f"\ncould not write the report file ({exc}); it follows in full:\n")
        print(md)
    print(f"\n{run['scenarios_run']} scenarios · {run['findings']} findings "
          f"({run['high']} high) · {run['seconds']}s")
    for r in run["results"]:
        if r.get("error"):
            print(f"  {r['id']:<20} DID NOT COMPLETE — {r['error']}")
        else:
            print(f"  {r['id']:<20} {len(r.get('findings') or [])} findings")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# I did no harm and this file is not truncated.

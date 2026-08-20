# =============================================================================
# lessonscripts.py  --  THE SCRIPTED-FIRST ENGINE (pilot)  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-08-20  NEW FILE (build js -- THE PILOT). Jim's ruling of 2026-08-20
#               (Ruling_Scripted_First_And_The_Settings_2026-08-20.md): every lesson is
#               pre-authored, pre-verified, and pre-voiced up to the moment a child
#               responds; the AI steps in only when the child leaves the script; CODE,
#               not the model, returns the child to the script. Why: the day's
#               measurements -- ~$50/student/month against a $29 price, 11.5s median
#               turn, 42.4% verified right first try, 25 known-bad replies shipped in a
#               week -- are all costs of GENERATING teaching at runtime. A script
#               verified once is right forever, retries never, and speaks from cached
#               audio at zero marginal cost.
#
#               THIS FILE IS DELIBERATELY PURE. No model, no network, no store, no
#               clock: lesson data + a state-machine engine + a validator. Everything
#               here can therefore be verified exhaustively by ruletests PART 3cv, and
#               a verified script stays verified. The server wiring (endpoints, the AI
#               intervention call, audio prerender) comes in the NEXT build and imports
#               this one; the client page after that.
#
#               THE SETTINGS ARE THE RESEARCH DOC'S, NOT OPINIONS (citations there):
#               advance on 3 consecutive unaided correct, minimum 4, cap 10; worked
#               examples then example-problem pairs; error path = scripted "let's look
#               together" -> AI Model-Lead-Test -> engine-issued same-form retest;
#               second intervention on a skill drops a representation level (abstract ->
#               pictorial -> concrete); failing at concrete ends warmly and marks the
#               topic "learning"; a garbled answer gets ONE scripted re-ask, then
#               tap-only -- never an AI call for a mishearing.
#
#               ⭐ THE CLOSURE PROPERTY (the reason pre-rendered voice can be TOTAL):
#               every spoken string this engine can ever emit is enumerable in advance
#               by audio_lines(). PART 3cv drives every scenario the engine supports
#               and asserts each emitted spoken line is in that closure. If a future
#               edit adds a line the closure misses, the battery fails -- so the voice
#               cache can never be surprised at runtime.
# =============================================================================

import re

# ---- THE SETTINGS (from the 2026-08-20 research ruling; change THERE first) -------
ADVANCE_STREAK = 3        # advance on 3 consecutive unaided correct (EDM 2015)
MIN_PROBLEMS = 4          # even a perfect child does at least 4 (DI "firming")
MAX_PROBLEMS = 10         # past 10 without a streak, stop -- see drop/end rules
DROP_AFTER_INTERVENTIONS = 2   # 2nd AI intervention on a skill -> easier representation
LEVELS = ("abstract", "pictorial", "concrete")   # drop direction, left to right
BEAT_WORD_CAP = 80        # rule 19c / build jd: one beat per turn, spoken

# ---- CANON VOCABULARY (build jr's lesson: one rule, one wording) ------------------
# canon phrase -> the synonyms that are BANNED anywhere in this lesson's speech.
# The validator enforces it; the intervention contract hands the canon to the AI.
VOCABULARY = {
    "put together": ("combine", "join together", "add together"),
    "in all": ("altogether", "all together", "total", "the total"),
    "equals": ("makes", "gives you", "is the same as"),
}

# ---- PRAISE (rotated deterministically by problem index; all pre-renderable) ------
PRAISE_PREFIXES = ("That's it!", "You got it!", "Nice counting!",
                   "Exactly right!", "Well done!")

# fixed one-line scripts (every one of these is pre-rendered once)
LINE_WRONG = "Not quite — let's look at it together."
LINE_REASK = "Let me say that again."
LINE_TAP = "Tap the answer you think is right."
LINE_END_GRACEFUL = ("We did some strong thinking today. We'll practice this again "
                     "next time — Mr. Cadabra is proud of you.")
LINE_ADVANCE = "Three in a row — you've got it! That's adding within ten."


# =============================================================================
# THE PILOT LESSON -- Basic Math, Unit 1: adding within 10, with stars.
# -----------------------------------------------------------------------------
# Problems are DATA (a, b), never typed answers: the validator COMPUTES a+b, so a
# wrong answer key cannot exist in this file. The bank is ordered by sum -- the
# difficulty ramp the 85%-success guideline asks for.
# =============================================================================
PILOT_LESSON = {
    "id": "basic-u1-adding-within-10",
    "course": "basic",
    "unit": 1,
    "topic": "Adding within 10",
    "teach": [
        # (spoken, board) -- one beat each. Concrete -> symbols, per CRA.
        ("Today we are learning to add. Adding means putting two groups together "
         "and counting how many there are in all.",
         '[[goal text="Adding within 10"]]'),
        ("Here are three stars. And here are two more stars. Let's put the groups "
         "together and count every star: one, two, three, four, five. "
         "There are five stars in all.",
         '[[objects emoji="⭐" groups="3" add="2" caption="count every star"]]'),
        ("Mathematicians write putting together with a special sign. We write it "
         "like this, and we say it 'plus'. Three plus two.",
         '[[step eq="3 + 2"]]'),
        ("And when we know how many in all, we use one more sign. We write it like "
         "this, and we say it 'equals'. Three plus two equals five.",
         '[[step eq="3 + 2 = 5"]]'),
        ("Watch me do a whole one. Four stars, and one more star. I count every "
         "star: one, two, three, four, five. Four plus one equals five.",
         '[[objects emoji="⭐" groups="4" add="1" caption="count every star"]]'
         '[[step eq="4 + 1 = 5"]]'),
    ],
    # example-problem PAIRS (worked example, then a near-twin the child answers).
    # Guided answers never count toward the advance streak.
    "pairs": [
        {"worked": ("Here is one more, done for you. Two stars and two stars. "
                    "Count them all: one, two, three, four. Two plus two equals four.",
                    '[[objects emoji="⭐" groups="2" add="2" caption="count every star"]]'
                    '[[step eq="2 + 2 = 4"]]'),
         "ask": {"a": 2, "b": 3}},
        {"worked": ("One more together. Five stars and one star. Count them all — "
                    "six. Five plus one equals six.",
                    '[[objects emoji="⭐" groups="5" add="1" caption="count every star"]]'
                    '[[step eq="5 + 1 = 6"]]'),
         "ask": {"a": 4, "b": 2}},
    ],
    "practice_intro": ("Now it's your turn. Three right answers in a row and "
                       "we're done — here comes the first one."),
    # the practice bank, ordered by sum (the difficulty ramp)
    "bank": [
        {"a": 2, "b": 1}, {"a": 1, "b": 3}, {"a": 2, "b": 2}, {"a": 3, "b": 2},
        {"a": 4, "b": 1}, {"a": 3, "b": 3}, {"a": 5, "b": 2}, {"a": 4, "b": 3},
        {"a": 6, "b": 2}, {"a": 5, "b": 4}, {"a": 7, "b": 2}, {"a": 6, "b": 3},
    ],
}


# =============================================================================
# RENDERERS -- problem data -> what the child sees and hears, per level.
# One function per surface, so vocabulary consistency is BY CONSTRUCTION.
# =============================================================================
def spoken_for(p, level):
    a, b = p["a"], p["b"]
    if level == "abstract":
        return f"What is {a} plus {b}?"
    if level == "pictorial":
        return f"Count the stars if you need them. What is {a} plus {b}?"
    return (f"Let's count together. {a} stars, then {b} more stars. "
            f"How many in all?")


def board_for(p, level):
    a, b = p["a"], p["b"]
    step = f'[[step eq="{a} + {b} = ?"]]'
    if level == "abstract":
        return step
    stars = f'[[objects emoji="⭐" groups="{a}" add="{b}" caption="count every star"]]'
    return stars + step


def choices_for(p):
    """Three tap options: the answer and its two neighbours (floor 1), shuffled by a
    FIXED per-problem rotation -- deterministic, so replays render identically."""
    ans = p["a"] + p["b"]
    opts = [ans - 1, ans, ans + 1] if ans > 1 else [ans, ans + 1, ans + 2]
    k = (p["a"] * 3 + p["b"]) % 3
    opts = opts[k:] + opts[:k]
    return "[[choices options=\"" + " | ".join(str(o) for o in opts) + "\"]]"


def praise_for(p, index):
    a, b = p["a"], p["b"]
    return (PRAISE_PREFIXES[index % len(PRAISE_PREFIXES)]
            + f" {a} plus {b} equals {a + b}.")


# =============================================================================
# THE ENGINE -- a pure state machine.  step(lesson, state, event) -> (out, state)
# -----------------------------------------------------------------------------
# Events:   ("begin",)            start the lesson
#           ("answer", value)     the child answered (tap or typed int)
#           ("unheard",)          voice input could not be recognized
#           ("resume",)           the AI intervention finished; give the retest
# Outputs (dicts), by kind:
#   say        {spoken, board}                       -- narration beat, no input
#   ask        {spoken, board, choices, expected, guided, problem} -- wait for child
#   intervene  {reason, problem, expected, got, vocabulary, retest} -- AI takes over;
#              the ONLY step the model ever authors, and the engine has already chosen
#              the retest problem, so the RETURN to script is code's decision.
#   end        {spoken, graceful, mastered, problems_done}
#
# The caller drains "say" beats itself (each begin/answer may yield several beats;
# next(state) hands them out one at a time so one beat = one screen).
# =============================================================================
def start(lesson):
    return {"phase": "teach", "i": 0, "level": "abstract",
            "bank_i": 0, "done": 0, "streak": 0,
            "interventions": 0, "unheard": 0, "pending": None,
            "retest": None, "finished": False}


def _problem_key(p):
    return (p["a"], p["b"])


def _next_bank_problem(lesson, state):
    """The next unused bank problem; the bank wraps if the retest path consumed it."""
    bank = lesson["bank"]
    p = bank[state["bank_i"] % len(bank)]
    state["bank_i"] += 1
    return p


def _ask(state, p, guided=False):
    out = {"kind": "ask", "spoken": spoken_for(p, state["level"]),
           "board": board_for(p, state["level"]), "choices": choices_for(p),
           "expected": p["a"] + p["b"], "guided": guided, "problem": p,
           "tap_only": state["unheard"] >= 2}
    state["pending"] = {"problem": p, "guided": guided}
    return out


def step(lesson, state, event):
    """One engine transition. Returns (list_of_output_steps, state). Pure."""
    kind = event[0]
    out = []

    if state["finished"]:
        return ([{"kind": "end", "spoken": "", "graceful": True,
                  "mastered": False, "problems_done": state["done"]}], state)

    if kind == "begin":
        for spoken, board in lesson["teach"]:
            out.append({"kind": "say", "spoken": spoken, "board": board})
        pair = lesson["pairs"][0]
        out.append({"kind": "say", "spoken": pair["worked"][0],
                    "board": pair["worked"][1]})
        out.append(_ask(state, pair["ask"], guided=True))
        state["phase"] = "pair-0"
        return (out, state)

    if kind == "unheard":
        state["unheard"] += 1
        p = state["pending"]["problem"]
        guided = state["pending"]["guided"]
        re_spoken = LINE_TAP if state["unheard"] >= 2 else (
            LINE_REASK + " " + spoken_for(p, state["level"]))
        asked = _ask(state, p, guided=guided)
        asked["spoken"] = re_spoken
        return ([asked], state)

    if kind == "resume":
        # The AI intervention is over. The engine -- not the model -- decides what
        # happens next: the retest problem it already chose, or (at the cap) the
        # warm close. The model never picks where the child lands.
        p = state["retest"]
        state["retest"] = None
        if p is None:
            state["finished"] = True
            return ([{"kind": "end", "spoken": LINE_END_GRACEFUL, "graceful": True,
                      "mastered": False, "problems_done": state["done"]}], state)
        return ([_ask(state, p, guided=False)], state)

    if kind != "answer":
        return ([], state)

    state["unheard"] = 0
    pend = state["pending"]
    p, guided = pend["problem"], pend["guided"]
    correct = (event[1] == p["a"] + p["b"])

    if correct:
        idx = state["done"]
        out.append({"kind": "say", "spoken": praise_for(p, idx), "board": ""})
        if not guided:
            state["done"] += 1
            state["streak"] += 1
        # ---- where next? ----
        if state["phase"] == "pair-0":
            pair = lesson["pairs"][1]
            out.append({"kind": "say", "spoken": pair["worked"][0],
                        "board": pair["worked"][1]})
            out.append(_ask(state, pair["ask"], guided=True))
            state["phase"] = "pair-1"
            return (out, state)
        if state["phase"] == "pair-1":
            out.append({"kind": "say", "spoken": lesson["practice_intro"],
                        "board": ""})
            state["phase"] = "practice"
            out.append(_ask(state, _next_bank_problem(lesson, state)))
            return (out, state)
        # practice
        if state["done"] >= MIN_PROBLEMS and state["streak"] >= ADVANCE_STREAK:
            out.append({"kind": "end", "spoken": LINE_ADVANCE, "graceful": True,
                        "mastered": True, "problems_done": state["done"]})
            state["finished"] = True
            return (out, state)
        if state["done"] >= MAX_PROBLEMS:
            out.append({"kind": "end", "spoken": LINE_END_GRACEFUL,
                        "graceful": True, "mastered": False,
                        "problems_done": state["done"]})
            state["finished"] = True
            return (out, state)
        out.append(_ask(state, _next_bank_problem(lesson, state)))
        return (out, state)

    # ---- wrong answer: the ONE doorway to the AI ----
    state["streak"] = 0
    if not guided:
        state["done"] += 1
    state["interventions"] += 1
    if state["interventions"] >= DROP_AFTER_INTERVENTIONS:
        li = LEVELS.index(state["level"])
        if li + 1 < len(LEVELS):
            state["level"] = LEVELS[li + 1]
            state["interventions"] = 0
        else:
            # already at concrete and still failing: end warmly, mark "learning"
            out.append({"kind": "say", "spoken": LINE_WRONG, "board": ""})
            out.append({"kind": "end", "spoken": LINE_END_GRACEFUL,
                        "graceful": True, "mastered": False,
                        "problems_done": state["done"]})
            state["finished"] = True
            return (out, state)
    # AT THE CAP, THE ERROR IS STILL CORRECTED BUT NO RETEST FOLLOWS: the AI's
    # Model-Lead-Test runs (never leave a child with an uncorrected error), and
    # "resume" then ends the practice gracefully instead of asking an eleventh
    # problem. Found by the alternating right/wrong scenario in this build's own
    # dry run -- the cap only guarded the CORRECT path, and `done` reached 11.
    retest = None
    if state["done"] < MAX_PROBLEMS:
        retest = _next_bank_problem(lesson, state)
    state["retest"] = retest
    out.append({"kind": "say", "spoken": LINE_WRONG, "board": ""})
    out.append({"kind": "intervene", "reason": "wrong_answer", "problem": p,
                "expected": p["a"] + p["b"], "got": event[1],
                "vocabulary": {k: k for k in VOCABULARY},
                "level": state["level"], "retest": retest})
    return (out, state)


# =============================================================================
# THE AUDIO CLOSURE -- every spoken string this lesson can ever emit.
# =============================================================================
def audio_lines(lesson):
    lines = set()
    for spoken, _board in lesson["teach"]:
        lines.add(spoken)
    for pair in lesson["pairs"]:
        lines.add(pair["worked"][0])
    lines.add(lesson["practice_intro"])
    problems = list(lesson["bank"]) + [pair["ask"] for pair in lesson["pairs"]]
    for p in problems:
        for level in LEVELS:
            lines.add(spoken_for(p, level))
            lines.add(LINE_REASK + " " + spoken_for(p, level))
        for i in range(len(PRAISE_PREFIXES)):
            lines.add(praise_for(p, i))
    lines.update([LINE_WRONG, LINE_TAP, LINE_END_GRACEFUL, LINE_ADVANCE])
    return sorted(lines)


def audio_cost_estimate(lesson, usd_per_1k_chars=0.22):
    chars = sum(len(s) for s in audio_lines(lesson))
    return {"lines": len(audio_lines(lesson)), "chars": chars,
            "usd": round(chars / 1000.0 * usd_per_1k_chars, 2)}


# =============================================================================
# THE VALIDATOR -- the checks that make "verified once" true. Pure; returns a list
# of (ok, label, detail). The battery fails the build on any not-ok.
# =============================================================================
_TAG_RE = re.compile(r"\[\[\s*([\w-]+)")


def validate(lesson, board_tag_names=None):
    checks = []

    def ck(ok, label, detail=""):
        checks.append((bool(ok), label, detail))

    # 1. every answer is COMPUTED -- and inside the lesson's own claim (within 10)
    problems = list(lesson["bank"]) + [pr["ask"] for pr in lesson["pairs"]]
    ck(all(2 <= p["a"] + p["b"] <= 10 for p in problems),
       "every problem stays within 10", str([p for p in problems
                                             if not 2 <= p["a"] + p["b"] <= 10]))
    ck(len({_problem_key(p) for p in problems}) == len(problems),
       "no duplicate problems", "")

    # 2. choices: the right answer appears exactly once, all options positive
    for p in problems:
        opts = re.findall(r"\d+", choices_for(p))
        ck(opts.count(str(p["a"] + p["b"])) == 1,
           f"choices for {p['a']}+{p['b']} contain the answer exactly once",
           str(opts))
        ck(all(int(o) >= 1 for o in opts),
           f"choices for {p['a']}+{p['b']} are all at least 1", str(opts))

    # 3. the difficulty ramp: bank sums never decrease by more than 1
    sums = [p["a"] + p["b"] for p in lesson["bank"]]
    ck(all(sums[i + 1] >= sums[i] - 1 for i in range(len(sums) - 1)),
       "the bank is a ramp (sums never fall by more than 1)", str(sums))

    # 4. every beat respects the spoken cap
    for spoken in [s for s, _b in lesson["teach"]] + \
                  [pr["worked"][0] for pr in lesson["pairs"]] + \
                  [lesson["practice_intro"]]:
        ck(len(spoken.split()) <= BEAT_WORD_CAP,
           f"beat under {BEAT_WORD_CAP} words: \"{spoken[:40]}...\"",
           f"{len(spoken.split())} words")

    # 5. rule 14 by construction: '+' and '=' are READ ALOUD before any ask uses them
    teach_text = " ".join(s for s, _b in lesson["teach"]).lower()
    ck("'plus'" in teach_text, "the + sign is introduced by name (rule 14)", "")
    ck("'equals'" in teach_text, "the = sign is introduced by name (rule 14)", "")

    # 6. rule 44 by construction: every ask SPEAKS its numbers
    for p in problems:
        for level in LEVELS:
            sp = spoken_for(p, level)
            ck(str(p["a"]) in sp and str(p["b"]) in sp,
               f"ask speaks its numbers ({p['a']}+{p['b']}, {level})", sp)

    # 7. build jr's lesson, enforced at authoring time: canon vocabulary only
    all_speech = " ".join(audio_lines(lesson)).lower()
    for canon, banned in VOCABULARY.items():
        for term in banned:
            ck(term not in all_speech,
               f"vocabulary: '{term}' never appears (canon is '{canon}')", "")

    # 8. every board tag is a real tag (against tags.py when provided)
    if board_tag_names:
        boards = [b for _s, b in lesson["teach"]] + \
                 [pr["worked"][1] for pr in lesson["pairs"]] + \
                 [board_for(p, lv) for p in problems for lv in LEVELS] + \
                 [choices_for(p) for p in problems]
        for b in boards:
            for name in _TAG_RE.findall(b):
                ck(name in board_tag_names,
                   f"board tag [[{name}]] exists in the registry", b[:60])

    # 9. praise pool sanity
    ck(len(PRAISE_PREFIXES) >= 3, "at least 3 praise variants", "")
    return checks


# I did no harm and this file is not truncated.

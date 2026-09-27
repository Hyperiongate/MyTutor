# Build yl — The Quiz Sweep, 2026-09-26

Jim: *"Okay, start on the quiz sweep."* The last unread text in the app.

Stamp: **`2026-09-26yl-the-quiz-sweep`**. PART **3of**. An instrument build — the reading is
Jim's to run.

## What the quiz is

Every lesson ends on a **topic quiz**: five pinned questions (`quizsets.py`, 1,799 across
the 360 lessons), each a generated ask — the op's spoken line, its board, its three tap
buttons — graded in code against the key. Four of five is a pass, and the pass is what the
child's record says was learned. Every course-sweep report since `wa` has ended *"the topic
quiz's sentences (quizsets.py) — a separate instrument."* The 90% Unit Quiz is a different
thing — the live tutor's, the night watch's lane — and stays so.

## Two instruments

**The machine pass, in the battery.** Every pinned question, every run: its op's own check
holds; its key is a whole number; its three choices are distinct and hold the key; its
board is a tag the renderer knows with attributes it reads; its words keep the canon's
vocabulary and the 27-word sentence cap; no lesson asks the same question twice; every
lesson has a quiz. **All 1,799 pass today.** The pass found one thing on the way: the five
bearing questions' boards read as "unknown attribute" — `[[unitcircle turn=]]` had drawn
them since `tp`, but the board contract reads a tag's attributes off its own function and
`turn` was read inside the compass helper. `unitcircle` names it itself now.

The referees were run over the questions too (the way PART 3eu runs them over authored
cards). Twenty flags on five ops, and the same ops' lesson asks — read by three sweeps —
raise the same flags: the referees' live-reply rules (one question per turn, a pending
`?` line) misread an authored ask. Not a finding. One question the pass could not judge
but the reader can: Pre-Algebra's dividing-by-a-fraction quiz asks *"4 divided by two
fourths"* — an unsimplified fraction the lesson's own bank never uses. That is exactly what
the reader's third rule is for, and the quiz page now carries what it needs to see it.

**The reader.** A quiz sweep is a course named `quiz<course>` on the course-sweep card —
*quiz · geometry* on the menu, `quizgeometry` on the wire — and goes through the same
doors: Price it (free), Run it, Resume, Read. `coursesweep.split_course` reads the name;
`quiz_transcript_for` walks the quiz as the child meets it (the intro line; each ask with
its board and its buttons; the STUDENT answering **the KEY**, marked as the key so the
reviewer judges the key and not a child; *"Right."*; the pass line); the page carries the
lesson's own **problem space** and **what the lesson taught** (its why, picture, teach and
worked beats, marked context only) so the reviewer can see a question that is outside the
lesson. The charter, `QUIZ_SYSTEM`, in order of importance: the key is wrong; the question
cannot be answered from what is said and drawn; the question is outside the lesson (an
unsimplified fraction where the lesson used only simplified ones, a case the space
excludes); a wrong choice that is right, two choices the same, the key missing; wording.
The same exclusions as the course charter, plus the quiz's own (it does not teach, by
design; *"Right."* after every answer). A finding on a question is the op's (its words) —
or `quizsets.py`'s (its numbers; regenerate with `tools/genquiz.py`). The report is titled
*Quiz sweep*.

## Proved

PART 3of: the machine pass (four checks over 1,799); `split_course` both ways;
`quiz_transcript_for`'s shape on a real lesson and `[]` for a lesson without a quiz; the
page's head, space and context; the charter; `run_sweep("quizgeometry")` with a stubbed
judge — the quiz charter is the system prompt, the quiz page is the body, a finding lands
on the ask and is owned by the op, the report says *Quiz sweep* and names `quizsets.py`;
the estimate; the endpoints and the card. Two pins moved (the status lists twenty names;
the source-literal pin on `run_sweep`'s return shape reads `_assemble`'s per-kind
`"not_covered"` now).

## What Jim does

Push, then on `/admin`'s course-sweep card pick **quiz · entry** (or any course), Price
it, Run it, and paste the report here as with every sweep. A quiz sweep is 36 reads, the
same price as a course.

## Files

`coursesweep.py` (`split_course`, `quiz_courses`, `quiz_transcript_for`, `lesson_context`,
`QUIZ_SYSTEM`, the lane through `lessons_for` / `estimate` / `run_sweep` / `_assemble` /
`report_markdown`), `main.py` (the start's name check; the status list; stamp),
`static/admin.html` (the menu labels), `static/math-figures.js` (`unitcircle` names
`turn`), `ruletests.py` (PART 3of; one pin moved), `speechmap.py` (unchanged), this doc,
the refreshed `START_HERE_Handoff_2026-09-26.md`.

Battery on the frozen copy, 2026-09-26: **13,207 passed · 0 failed · 3 skipped**, second run (the first run's one failure was the
moved pin above) (13,195 at `yk`).

I did no harm and this file is not truncated.

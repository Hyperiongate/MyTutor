# Build wa — The course sweep (2026-09-15)

Project 1 of the 09-14 deep dive. The night watch audits the live AI lane every night;
nothing audited the scripted course — the lane a child actually spends their minutes on —
except Jim's own playtests, one lesson at a time, about six flags a lesson. This build points
the same reviewer at a whole course, once, and hands back a list with a bottom.

Battery: **12,363 passed, 0 failed** (frozen copy, 2026-09-15).

## What it is

`coursesweep.py` — a pure module, no FastAPI, no store — plus a background job and three admin
endpoints in `main.py`, and a "Course sweep" card on `/admin` under the night watch.

**The walk.** Every lesson is played by the engine itself, deterministically (one seed), the
way a child hears it: intro, why, picture, teach, the two worked examples, practice — with
**one deliberate miss** on the first practice problem, so the scripted second explanation from
`vz` is read too — then correct answers to the streak, the reason question, and the end. A
times-table lesson shows its first six facts and says the pass continues. All 360 lessons walk;
311 of them read the second explanation (every lesson with a worked generator except the table
lesson, which practices as a pass).

**The page the reviewer reads.** Every turn numbered and labelled with its beat (`why`,
`picture`, `teach`, `ask`, `praise`, `walk-back`, `second-look`, …), the words and then the
board with its tags left in, under the rule index. The instructions say what to report in
order of importance — a false or unconditional statement first, then a step that does not
follow, words that do not match the board, a term used before it is taught, wording a child at
this level cannot parse, a beat that repeats, tone — and what *not* to report: style, the
choice of numbers, anything outside the topic. Exact quotes, at most eight findings, worst
first, and "clean" is a legitimate answer.

**The placement law**, borrowed from the night watch: a finding whose quote is not in the
transcript is dropped as unplaced (the reviewer paraphrased). A slipped turn number is recovered
by its quote.

**Ownership — the point of the whole thing.** A finding on an ask, a praise line, a walk-back
or a frame belongs to the **generator op** that made the line: fix the generator once and it
is fixed in every lesson that shares it. A finding on a why, picture, teach, recap or reason
beat belongs to the **lesson**. The report groups them that way — generators first, by how
many lessons each touches; then authored beats by unit and lesson; then the clean lessons, the
unread ones, and what the sweep did not cover (the topic quiz, the AI's own words on a second
miss, the rendered screen, the rest of a table pass).

## How to run it

On `/admin`, the card under the night watch. Pick a course. **① Price it — FREE** says how
many lessons and characters and an honest estimate (about $1.80 a course at an assumed
Sonnet-class price; correct `EST_USD_PER_LESSON` from the billing dashboard after the first
one). **② Run the sweep — SPENDS** starts it as a background job, exactly the way the prewarm
runs — the request returns at once and the card follows it. Then **Read that report**. Reports
live in `data/coursesweep/<course>_<date>.md` (and `.json`), and a second sweep the same day
gets its own name.

It runs on Render because the judge seat needs `ANTHROPIC_API_KEY`, which lives there. A run
without the key is refused with a 503 that names it. One job at a time; a second is refused
with a 409. It never touches a lesson.

## The order I would sweep in

Entry and Basic first — the youngest students, and the courses your playtests have touched
least — then Pre-Algebra and Algebra I, which your queue has already sampled. Read one report
before running the next: the first one is where we calibrate the reviewer (too soft, too
harsh, or reporting things we have ruled allowed), and I would rather adjust the instructions
after 36 lessons than after 360.

## What did not change

No audio, no closure, no referee. `coursesweep.py` is imported defensively like the night
watch: a deploy without it still teaches children.

I did no harm and this file is not truncated.

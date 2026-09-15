# Weekly deep dive — 2026-09-14: the Forever War, and the project list

Jim's brief: latency is under control; the whack-a-mole is not, and the product cannot go to
market with customers doing the whacking. Look at the interface as a child would, check every
demo against what has shipped, find some fun, and come back with a project list.

I looked at the live site in Chrome (front door, the lesson demo, the tour), read the change
history end to end, and counted. This is what I found, and then the list.

---

## 1. Why it feels like a forever war — because half of it is one

**Two products live in this app**, and they have opposite natures.

**Lane A is the scripted course.** 360 lessons in ten courses, 40,248 fixed spoken lines, an
engine that is a pure state machine, and a voice cache that has every clip. Its defects are
**authored text and authored boards** — a wrong word, a story that should have been a picture,
a board line below the fold. Every one of those is finite: the text does not change unless we
change it, and a fix is permanent. Since `vz` this morning, a child on the course reaches the
AI only on a **second consecutive miss**. Lane A is where a child's minutes are.

**Lane B is the live AI tutor.** Every reply is generated fresh by a model, judged by 100
referees and a live critic, and exercised every night by synthetic students. Its defect space
is **unbounded by construction** — a generative model's output cannot be enumerated, and each
referee closes one shape while the model finds another. The numbers say exactly that: the
referee count went **62 → 100** in three weeks (84, 86, 87, 88, 90, 91, 95, 97, 100 just since
09-08), and the nightly finding count has *not* fallen — 8, 10, 10, 17, 14, 10 over the last six
watches. That is the signature of a game you cannot win by playing harder.

**And here is the part that makes it feel endless:** most of the effort has gone to Lane B.

- **381 builds** between 08-07 and 09-14 — 55 to 100 a week.
- Of the last week's triage, roughly **80 findings came from the night watch** (all Lane B)
  against **31 from your corrections queue** (Lane A).
- The night watch runs *only* on Lane B. There is **no nightly watch on the scripted course
  at all** — the lane children use is the one nobody audits automatically.
- The pencil's whole expressive repertoire — circling a word, underlining, the exclamation
  mark, writing on the board, waving, the party — is wired through `[[ink]]` tags that only the
  **AI** is prompted to emit. **Not one of the 360 authored lessons uses it.** In the lesson a
  child actually gets, the pencil drifts, blinks, and waits.

So the war is being fought on the battlefield the customer rarely visits, with weapons the
customer never sees, against an enemy that regenerates. That is why it feels infinite. The
part of the product the customer *does* visit has a finite defect list — we have simply been
sampling it a few lessons at a time, through your playtests, instead of sweeping it.

**One more number.** Your 09-13 corrections queue was 12 flags from two lessons — about six
per lesson played. Across 360 lessons that is on the order of a couple of thousand latent
flags if the rate holds, *but* the courses are built from **347 shared generators**, so most of
those flags collapse into a few dozen generator fixes ("is equal to" fixed dozens of lessons in
one line). Finite, and much smaller than it looks — provided we find them in one sweep rather
than one playtest a week.

## 2. The strategy that ends it

**Contain Lane B; finish Lane A; then make Lane A delightful.** In that order.

**Contain the AI, stop perfecting it.** The truth referees (11 of the 100) are the safety net:
a false statement is withheld and the child gets the fallback line. That is the property a
customer needs. Everything else the watch finds is *quality* on a lane a child sees once in a
blue moon. The change is a **policy**, not code: the night watch stays on as an alarm, but only
truth-class and HIGH findings are actionable; style and conduct items go to a ledger we read
monthly. No new referee unless a finding is truth-class. Phases B and C shrink the lane further
until the AI is a rare fallback — and a rare fallback with a truth floor is good enough to sell.

**Sweep the scripted course once, systematically.** Point the reviewer machinery at the 360
lessons instead of at synthetic AI conversations: read every lesson's transcript whole, once,
with the same critic that reads the watch, and triage the output **by generator and by course**
as one batch. That turns the trickle into a finite list with a bottom, and it costs tens of
dollars of model time, not weeks of playtesting. Your playtests then become confirmation, not
discovery.

**Then the child.** With the moles gone, the pencil, the board and the feel of the room are
where the remaining hours go — and they are the hours that sell it.

## 3. What I saw on the site

**Front door and demos.** The landing page is clear and honest. The lesson demo (`/demo/lesson`)
runs the *real engine* — I watched Phase A play live in it this evening, worked solution and
fresh problem, in his rendered voice — so it is current by construction and always will be.
The classroom tour's 254 lines narrate the dashboards and the room, none of which changed this
month, so it is not stale. **One thing I could not verify:** the tour's first tap ("Take the
classroom tour") did not respond to Chrome automation at all, while every button on the lesson
demo did. Calling its handler directly works, so the wiring is fine; I could not tell whether a
human click behaves the same. Worth one tap by you.

**The classroom, through a child's eyes.** It is calm, legible and honest — big numbers on the
board, big tap buttons, nothing flashing for the sake of it. That is right for a
twelve-year-old. For a six-year-old it reads like a grown-up's app: white cards on a pale
gradient, grey helper text, the pencil small and off to the side, and — this is the one that
matters — **a wrong tap gets no visible reaction on the board.** The button does not shake, the
answer is not marked, and the pencil does not look at it. The correction arrives in words a
second later. A child's world is faster than that. Praise has the party ring; a miss has
nothing.

**The pencil.** He is good — he floats, blinks, changes expression, and at milestones he throws
a party. But in the scripted lesson he never touches the board, never points at the number he
is saying, never writes. All of that exists in `cadabra.js` already (`underline`, `circle`,
`bang`, `write`, `find`, `wave`, `comfort`, `party`, `think`); it just has no caller on the lane
the child is on. "A little more animation from the pencil" is mostly a wiring job, and a bigger
pencil is a number (`scale: 0.30`).

## 4. The project list

Ordered by what ends the war soonest, then by what sells. Sizes: S = a day, M = two to four
days, L = a week or more. Every one is a proper build with its own battery part.

| # | Project | Size | What it buys |
|---|---------|------|--------------|
| 1 | **The course sweep.** Run the reviewer over all 360 lessons as whole transcripts, once; triage by generator and course; fix generators. Deliverable: one triage doc per course with a bottom. | L | Ends the corrections-queue trickle by front-loading it. The single biggest lever on "the forever war." |
| 2 | **Watch policy: contain Lane B.** Truth-class and HIGH are actionable; everything else to a monthly ledger; no new referee unless truth-class. Put the "done for the day" ruling into the critic's charter while we are in there. | S | Stops the referee count from growing 3 a day. Frees the week. |
| 3 | **Phase C — worked generators for the 48 lessons without one.** They are the Entry course: the youngest students, the ones for whom the AI's first-miss door should be shut first. | M | Phase A reaches the six-year-olds. Zero new audio beyond the worked lines themselves. |
| 4 | **The miss has a face.** A wrong tap shakes the button and marks it; the pencil turns to it (`comfort`); the fresh problem lands with a small `point`. The right tap keeps its ring. | S | The one thing a child feels instantly. Pure page work; no engine change. |
| 5 | **The pencil in the scripted lane.** He points at the board line being spoken, underlines the number he just said, goes to `write` mode when a board draws, waves at the lesson intro, parties at the streak. Driven by the engine's own steps — no authoring per lesson. Scale 0.30 → ~0.45, docked beside the board rather than drifting. | M | "A little more animation from the pencil, a bigger pencil." All the moves exist; this gives them a caller. |
| 6 | **Screencheck learns the two flags nobody could screenshot.** A board whose last line lands below the visible area fails; figure widths within one lesson must agree. Runs in the battery on every push. | M | Turns your two unfixable layout flags into checks that catch the next one before you do. |
| 7 | **Child-mode skin for the youngest courses.** Entry/Basic sessions get warmer board colour, bigger tap targets, progress dots for "three in a row" visible during practice, and the parent-facing helper text removed from the child's screen. | M | The six-year-old's room, without touching the twelve-year-old's. |
| 8 | **The tour's first tap, verified — and one line for Phase A.** You tap it once; if it needs a fix it is a small one. Optionally the tour gains a sentence about the first miss being answered by the engine. | S | Demos stay current. |
| 9 | **Voice-cache reclaim card.** Dry-run count, then delete clips no longer in the closure. | S | ~812 MB back today; recurs every time authored text changes. |
| 10 | **Notation repair floor.** For a symbol with a fixed reading, append the reading when the model will not. | S | Closes the one recurring Lane B pass-through class cheaply. Low priority under project 2. |
| 11 | **Phase B — authored reteach beats.** Deferred until the sweep (project 1) says which lessons actually need a second explanation the worked solution does not give. | L | Don't author 360 beats on a hunch. |
| 12 | **Housekeeping:** the prefetch-shelf probe gets its own counter; the four carried triage rulings; the watch's `__open__` turn. | S | Tidiness. |

**What to stop doing**, because a forever war is also made of habits: no referee per finding;
no nightly triage doc unless something is truth-class; no building on the AI lane's style
while a Lane A flag is open; no playtest-as-discovery once the sweep is done — playtest to
confirm.

## 5. The gate to market, stated plainly

Lane A clean (projects 1, 3, 6), the miss has a face and the pencil has hands (4, 5, 7), the
AI contained with a truth floor (2). That is a product a customer does not have to whack. It is
about four to five weeks of the kind of weeks we have been having — and unlike the last five,
it has a bottom.

I did no harm and this file is not truncated.

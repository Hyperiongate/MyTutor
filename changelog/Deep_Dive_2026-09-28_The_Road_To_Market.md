# Weekly deep dive — 2026-09-28: the road to market

Jim's brief, Monday afternoon: a deep dive on the project overall — list the fixes and the
things that remain to be done, in order of priority, so we can get this to market soon.

I read the 09-14 and 09-22 deep dives, every handoff since, and today's `ys` build; checked
the repo rather than the docs for the state of the gate list, the login path, the seam
between the scripted lesson and the live tutor, the README, and the open items; and tried
the live site. This is where things stand and what I would do, in order.

---

## 1. Where we are — measured against the two earlier dives

**The 09-14 gate list is finished.** All six gate projects and three of the six others are
built and pinned: the course sweep (three full rounds, every course read three times, the
last four readings producing one new class between them — the ruling's stopping condition,
met), the watch policy (`xl`), Phase C (`xo`), the miss has a face (`xn`), the pencil in the
scripted lane (`xr`), the voice-cache reclaim card (`xt`), the child-mode skin (`xx`),
screencheck's two rules (`xy`), and the nightly scripted job (`ye`). The quiz lane, which
neither dive knew about, was built and read twice (`yl` → `yr`) and is closed. The battery
went 12,333 (09-14) → 13,296 today; the referee count has not moved from 101 since 09-16 —
the 09-14 "contain Lane B" policy is holding.

**What the sweeps say about Lane A now:** nine of ten courses have more clean lessons than
findings; Basic went 67 → 41 → 9, Geometry 63 → 36 → 11, Entry 219 → 6. The instrument is
still on the admin page for the day a build changes a course.

**Today's flag is the shape of what is left.** `ys` was a live-lane flag (the words asked
one question, the buttons another) in a Basic lesson — Lane B, on a course a six-year-old
uses. Two structural things let it through, both now closed in code, but the lesson of it
is in section 2.

## 2. Five things I found that the docs do not say

**a. The persona login codes are live in production.** `_lookup_student` checks
`students.json` first, in every environment: `1234` (Alex), `2345` (Maya), `3456` (Sam) and
`0000` (Demo Student) log in on mrcadabra.com today, run paid model calls, and write to the
real database. The README still says "until real accounts ship" — real accounts shipped on
07-31. Four-digit codes are guessable, and the login rate limit is 20 tries per five minutes
per IP. This is a one-hour fix and a launch blocker: personas only when `DATABASE_URL` is
unset (the dev box), or only behind the admin key. Keep `/demo` — it has its own path.

**b. Nobody has measured where a child's minutes actually go.** The 09-14 dive's whole
strategy rests on "Lane A is where a child's minutes are; Lane B is rare." That was true by
design after `sl`/`sn` (a mastered lesson chains to the next scripted one; a still-learning
end offers Go on / Review, no model call). But today Jim was in the live lane on Basic
addition, and the seam still falls open to the AI in four places: a course boundary, the end
of the course order, a typed answer at the Go on / Review choice, and the opener before a
student's first scripted lesson. The store has every turn; an admin card that reports, per
student and per course, scripted turns vs. live turns over the last 30 days would tell us in
one look whether Lane B is 2% of a child's time or 30%. If it is 30%, the plan changes.

**c. The README is stale in ways a buyer or a partner would notice.** "Eight complete
courses" (there are ten — Entry and Basic are the ones a family buys first), no mention of
the scripted lane, the pencil, the quiz, the child-mode skin, the sweep, or the nightly
screen job; the dev-codes section; "6,000+ checks" in MARKETING.md (13,296). Half a day.

**d. The site answered 502 this afternoon** (robots.txt, at about 15:00 Pacific). Most
likely Render mid-deploy of `ys`, but worth one look at `/health` and the Render events —
the 08-30 outage was a 502 too.

**e. The nightly `scripted` job (`ye`) has been running since 09-25 and no report has been
opened.** Its whole purpose is to catch an S8/S9/S10 screen defect before a family does. A
red job names its lessons in the log. Five minutes on GitHub → Actions.

## 3. The list, in priority order

Sizes as before: S = a day or less, M = two to four days, L = a week. The first block is the
launch gate as I would set it today; the second is what makes the first paying month go
well; the third is polish that can ship after launch without anyone noticing it was late.

### Block 1 — before a stranger pays (this week)

| # | Item | Size | Why it is in the gate |
|---|---|---|---|
| 1 | **Retire the persona codes in production** (personas only without `DATABASE_URL`, or behind the admin key); leave `/demo` alone. | S (hours) | Guessable logins into the real database, running paid calls. |
| 2 | **Jim plays the product as a new family, twice: laptop and phone.** Parent signup → child code → placement → first lesson → three mastered lessons → the free-tier gate → upgrade through Stripe (test mode) → the next lesson. Flag everything; fix the truth-class and the confusing, ledger the rest. The specific things from the handoff to look at on the way: the over-tall beat, the 9.8px grid numbers, the eight course reviews, the Skip pill on a phone, Geometry unit 1 past the pairs, Basic unit 3 lesson 4, Entry vs. Pre-Algebra, Pre-Calc unit 2 lesson 3's reason question. | M (Jim's two hours + my fixes) | Nobody has walked the money path end to end since billing shipped 07-31; every sweep read the lessons, none read the product. |
| 3 | **"Where the minutes go" card on /admin** — scripted vs. live turns per student, per course, last 30 days; the four seam fall-throughs counted by name. | S | Decides whether Lane B needs more containment before launch or after. The one number the strategy depends on and does not have. |
| 4 | **Close the seam fall-throughs the card names**, if it names one worth closing — most likely the opener before a student's first scripted lesson (play the course review then lesson one, no live turn), and the course boundary (hand to the next course's review). | S–M, depends on 3 | Every live turn a six-year-old sees is a turn the sweep never read. |
| 5 | **Confirm `/health` = `ys` and the 502 is gone; open the `scripted` job's reports.** | S (minutes) | Cheap; both are alarms nobody has looked at. |
| 6 | **README, MARKETING.md and the methodology page tell the truth** (ten courses, both lanes, the machine-counted numbers). | S | The first thing a partner, a marketer or a curious parent reads. |

### Block 2 — the first paying month

| # | Item | Size | Why |
|---|---|---|---|
| 7 | **The flag-to-fix loop stays open, and the sweep stays on the shelf.** The 09-22 ruling stands: no fourth round. A flag from a real family goes the way `ys` went today — which referee should have refused it, then the grader, then the prompt — and gets a build within the day. | ongoing | This is the whack-a-mole the customer must never do; it is ours, and it is now cheap. |
| 8 | **The 170 quiz questions that are their lesson's own example because the op is thin** — more bank problems or a second picture for those lessons (a ranked list is one command away). | M | A child who just watched the example gets asked the example. Not wrong, but it teaches nothing. |
| 9 | **Notation repair floor** (09-14 #10): for a symbol with a fixed reading, append the reading when the model will not. | S | The one recurring Lane B pass-through class; cheap. |
| 10 | **The over-tall beat** (29 LOW S9 at 1280×900) and the grid numbers (9.8px → 12): shorter beats lesson by lesson, one number for the grid. Only if Jim's laptop playthrough (#2) says the figures are too small. | S–M | Readability on a laptop; a phone is fine already. |
| 11 | **Parent weekly email, dashboard and awards read as a parent** — a second playthrough, this time as the parent, after a child's real week. | S | The parent is the buyer; the child is the user. The parent's view has not been in any sweep. |

### Block 3 — after launch, when a customer asks

| # | Item | Size | Why later |
|---|---|---|---|
| 12 | **Phase B — authored reteach beats** (09-14 #11). The sweep never said which lessons need a second explanation the worked solution does not give; the flag queue will. | L | Do not author 360 beats on a hunch — the 09-14 ruling, still right. |
| 13 | **The `xs` class in the other nine courses** (the board skips the arithmetic the words say; PART 3nn's ratchet: Basic 26, Prob/Stat 22, Geometry 18 …). Read the hits before drawing; the lower courses' hits include counting sequences. | M | A fourth sweep round in disguise; only when a course is opened for another reason. |
| 14 | **09-14 leftovers #8 and #12** (the tour's first tap; the prefetch-shelf counter; the watch's `__open__` turn). | S | Tidiness. |
| 15 | **A fourth reading of any course** — only when a build changes it (a generator rewrite, a new figure) or a family reports a wrong line. | — | The ruling. |

## 4. What I would stop, and what I would not start

Stop measuring the lessons; they have been measured. Three rounds, the quiz twice, the
screen nightly. The next defect a family meets is far more likely to be in the path between
the lessons — the login, the seam, the upgrade, the parent's email — than in a lesson, and
none of those has been walked end to end.

Do not start Phase B, a fourth sweep round, or a new referee. The referee count has been 101
for twelve days and Lane B has not gotten worse; today's flag was fixed inside an existing
referee. That discipline is the reason the war ended.

## 5. The gate, stated plainly

Block 1 is about a week: one hour for the persona codes, two hours of Jim's playing and a
day or two of fixes from it, a day for the minutes card and whatever seam it points at, an
afternoon for the docs. At the end of it we know the one number we do not know today (how
much of a child's time is the live tutor), the money path has been walked, no guessable code
opens the real database, and the alarms have been read. That is a product a stranger can
pay for. Block 2 is the first month, driven by real flags rather than synthetic ones.

I did no harm and this file is not truncated.

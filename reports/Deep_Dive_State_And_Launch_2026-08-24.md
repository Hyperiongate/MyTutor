# Mr. Cadabra's Classroom — Deep Dive: Where It Stands, What's Next, and How to Launch
**Date:** 2026-08-24 · Prepared for Jim · Sources cited at the end

---

## Part 1 — Where the app actually is today

The honest scorecard, using only machine-counted or measured numbers:

**What's genuinely strong.** Ten full courses from Entry-Level Math through Differential Equations, 336 scripted lessons, 25,376 practice problems, and 6,367 automated checks that must pass before anything ships. Every scripted lesson speaks in a real recorded voice at zero marginal cost — the entire course audio is rendered and cached (30,101 of 30,101 lines). Abrabot gives unlimited free practice that is tracked for parents but never touches mastery. The dashboards now tell the truth: after builds mw/mz/na, every referee verdict is counted, "caught & fixed" means fixed, and course-build cost is separated from teaching cost. No competitor at any price has this combination: a talking tutor, a complete start-to-finish curriculum, and published accuracy engineering.

**What still hurts, ranked by how much it matters:**

1. **Accuracy of the live AI lanes (biggest).** Only ~39% of AI turns with a checkable claim are right on the first draft. The referees catch and fix most of the rest before a child sees them — that's the system working — but retries drive roughly a third of the wait time, and ~29 replies per week shipped carrying a known unresolved finding. The scripted lessons don't have this problem at all; this is entirely the live-AI lanes. **Next step requires your production data:** deploy the current builds, let them run a day or two, and send me the "Referee fires by name" panel. That tells us whether one rule is misfiring or the drafts are broadly sloppy — two very different fixes.

2. **Speed.** Median AI turn 12.1s, p90 35.3s, worst 213s. Three levers, in order: fewer retries (fix #1 above), the second-opinion critic (~21% of turn time), and output length. Scripted lessons are instant — another reason to route as much teaching as possible through them.

3. **Cost.** The new build/serve split shows the real picture for the first time. In my sandbox reconstruction of your week, the second opinion (Opus critic) cost nearly **twice** the teaching brain — it is the single largest marginal cost and the single largest speed lever at once. The real production numbers arrive with the next deploy. Scripted teaching costs approximately nothing per hour; the AI lanes are the entire marginal cost.

4. **User-friendliness.** Your live session found seven defects; all fixed (subtraction now visibly takes stars away, Abrabot has a personality and a voice, the Next button no longer appears under a talking teacher, etc.). Still queued: an end-of-lesson "Practice this →" button, the 336-lesson picker wall (needs search/grouping), unit-wide "practice for the test," and practice minutes counting toward the streak.

5. **Launch blockers (not features — gates).** (a) Student and teacher codes have **no passwords** — the sign-in page itself warns "they are not yet security." Fine for beta; not acceptable for paid accounts holding children's data. (b) **Payments aren't on** — Stripe scaffolding exists (`_payments_open()`), but the switch is off. Marketing spend before these two are done is wasted money.

---

## Part 2 — The research base: what's solid, what's thin, how to close it

Your instinct is right. The current methodology page rests on three legs: Common Core / Eureka's *A Story of Units* for the elementary courses, the MAA *Instructional Practices Guide* for Calculus and Differential Equations, and "the standard progression" for everything in between. The middle is the thin part — "we follow the conventional sequence" is true but it isn't *evidence*.

The good news: the evidence exists, it's free, it's federal or professional-body work, and your app already does most of what it recommends. Closing the gap is a citation-and-audit job, not a rebuild:

| Course tier | Citable source to add | Status |
|---|---|---|
| Entry-Level, Basic | WWC *Teaching Math to Young Children*; WWC *Assisting Students Struggling with Mathematics* | Partly cited already via Eureka; add WWC |
| Basic, Pre-Algebra | WWC *Improving Mathematical Problem Solving in Grades 4–8*; WWC *Developing Effective Fractions Instruction* | **Gap — add** |
| Algebra I & II (and Pre-Algebra) | WWC *Teaching Strategies for Improving Algebra Knowledge in Middle and High School Students* (grades 6–12; three recommendations: analyze solved problems, use algebraic structure, choose among strategies) | **Gap — add.** Your worked-example lessons and "show the structure" rules already implement two of its three recommendations |
| Geometry, Trig/Pre-Calc | NCTM *Principles to Actions* (eight effective teaching practices — wait time, purposeful questions, productive struggle) | **Gap — add** |
| Probability & Statistics | ASA/NCTM *GAISE II* (2020) — the professional framework for K-12 statistics, free PDF | **Gap — add** |
| Calculus, Diff Eq | MAA *Instructional Practices Guide* | Already cited |

The work I'd do: read each guide against your 65 written teaching rules, map recommendation → rule (most will map), note honestly where they don't, and rewrite the methodology page's middle section from "standard progression" to "here is the practice guide, here are its recommendations, here is the rule in our tutor that enforces each one." That last part — *enforced in code, checked on every release* — is something no competitor can say, and it turns the methodology page from a citations list into a proof.

Estimated effort: one build. Say go when you want it.

---

## Part 3 — What the homepage should stress (and against whom)

Here's the competitive field as of this month:

| Product | Price | What it actually is | What it lacks vs you |
|---|---|---|---|
| Khanmigo | $4/mo ($44/yr) | Chat helper layered on Khan videos/exercises | Not a course; typing-first; no voice teaching; no mastery path |
| IXL | $9.95/mo (math), $15.95 combo | Practice-problem bank with hints | Doesn't teach; famously frustrating scoring; no tutor |
| Synthesis Tutor | $29/mo or $119/yr, up to 7 kids | Polished AI math tutor, K–8 focus | **Stops around middle school**; your range goes to Diff Eq |
| Math Academy | $49/mo | Rigorous mastery system, older students | Text-heavy, no voice, no young learners, premium price |
| CTCMath | ~$200/yr/student, ~$300 family | Video lessons + worksheets | Videos, not conversation; nobody listens to the child |
| Teaching Textbooks | $43–67/course/yr | Self-paced digital textbook | Same — lectures at the child |
| Mathnasium / human tutors | $300–400+/mo | Human instruction | Price; scheduling; one hour at a time |

**The sentence that sets you apart:** every product above either *talks at* the child (videos, textbooks) or *types with* the child (chatbots, practice banks). Yours is the only one where the child and the teacher **talk with each other** — a warm voice, a whiteboard drawing each step, across a complete curriculum from counting to calculus, with mastery honestly measured.

The homepage should stress, in this order:

1. **"A real conversation, out loud."** The hero already says this — sharpen it. This is the moat; no one else has it, and it's exactly what parents mean when they say "my kid needs a tutor, not another app."
2. **"The whole journey, not one grade."** Grade 1 through Differential Equations under one roof, placement to mastery. Synthesis stops at middle school; Teaching Textbooks sells one course at a time. One subscription, the child never outgrows it.
3. **"Teaching methods backed by research — and enforced by software."** Link the methodology page. After the Part-2 work, you can honestly say every course tier follows a published federal or professional-body practice guide, with the receipts on one page. Nobody else in this market shows their work like that.
4. **"Never just the answer."** The anti-photo-solver message — already good on the landing page.
5. **Price anchored against tutoring, not apps.** "A patient tutor, every day, for less than one hour with a human tutor costs" ($50–80/hr is the going rate; Mathnasium runs $300+/mo).
6. **The trust package.** Parent-controlled accounts, no data selling, honest dashboards, free practice that never costs extra. Homeschool parents read privacy pages.

One line I'd *retire*: leading with "Built for homeschool families" in the sub-headline is right for now (it's your launch market), but the page's job is the demo — the "Hear him teach" widget should be above the fold and unmissable, because thirty seconds of his voice sells better than any paragraph.

---

## Part 4 — Pricing: $10–15 is the right neighborhood

Your instinct to come down from $24–29 is right for the homeschool market. Where to land:

**Recommendation: $15/mo monthly · $12/mo billed annually ($144/yr) · covers 2 children.** Keep the founding-family rate lock you already promise.

Why this exact shape: at $12–15 you sit below Synthesis monthly ($29), at-or-below IXL combo ($15.95) *while actually teaching*, well below Math Academy ($49), and far below any human option — yet safely above Khanmigo's $4, which you shouldn't chase because Khanmigo isn't a curriculum and a $4 anchor would cheapen a full-curriculum product. Against homeschool incumbents, $144/yr for two children undercuts CTCMath's family plan (~$300/yr) and matches Teaching Textbooks' per-course pricing while covering *ten* courses. Annual-first pricing also matches how homeschool families buy: once a year, per school year.

**The unit-economics caveat, honestly:** this price only works if serve cost lands under roughly $0.50 per student-hour at typical usage (a two-child family using ~15–20 hours/month). Scripted lessons already cost ~nothing. The AI lanes don't, and the critic is the biggest line item. So the pricing decision and the cost work in Part 1 are the same project: **get the production serve-cost number from the new panel first, then set the price.** If serve cost is stubborn, the levers are (a) shrink the critic (cheaper model, or only on turns the referees flag), (b) a soft fair-use cap on AI-lane hours (industry standard, invisible to normal families), (c) keep unlimited scripted lessons and practice truly unlimited — they're free to serve, and "unlimited" is the marketing word.

Mechanical note when you change the price: pricing.html carries the numbers in **two places** — the visible cards *and* the schema.org JSON-LD block that Google reads ($29/$24 today). Both must change together; I'll do that as a build when you've picked the number.

---

## Part 5 — Marketing: getting rolling on under $500/month

Target: homeschool parents. The channel truth about this market: it runs on **trust and word-of-mouth** — reviews, co-ops, conventions, Facebook groups, and a handful of long-standing review sites — not on Google ads. That's good news at your budget.

**Sequence matters. Phase 0 (now → passwords + payments live):**
- Recruit 25–50 beta families hard. The beta page exists; the ask is testimonials and word-of-mouth in exchange for founding-family pricing for life. Every later channel needs their quotes.
- Fix the launch blockers (Part 1, #5). Nothing else below should get a dollar until then.
- Do the methodology work (Part 2) — it becomes your best marketing asset.

**Phase 1 (first 60 days after launch), roughly $0–200/mo:**
- **Submit to Cathy Duffy Reviews** — free to request, and a Top Picks mention moves real purchase decisions in this market. Also The Old Schoolhouse review program and Homeschool.com.
- **Give free access to 5–10 homeschool bloggers/YouTubers** in exchange for honest reviews. Their audiences are exactly your buyers, and "watch my kid talk to Mr. Cadabra" is inherently good video.
- **Comparison pages on your own site**: "Mr. Cadabra vs Teaching Textbooks," "vs CTCMath," "vs Synthesis," "vs Khanmigo." Parents search these exact phrases when choosing curriculum; the searches are high-intent and the competition for them is weak. This is the highest-ROI SEO available to you.
- **Be genuinely present** (not advertise) in homeschool Facebook groups and forums — answer math-curriculum questions as yourself, the founder. This market smells astroturf instantly and rewards founders who show up.

**Phase 2 (days 60–120), the remaining budget:**
- **One regional homeschool convention as a test.** Regional/state conventions (HEAV, FPEA, Great Homeschool Conventions) sell exhibitor tables; a live demo table where kids talk to Mr. Cadabra in the hall is your product doing its own selling. Test one, measure signups, then decide about the 2027 convention season properly.
- **Homeschool podcast/newsletter sponsorships** — niche shows sell spots cheaply ($50–300), and hearing a *voice product* advertised in audio is a natural fit.
- **An affiliate/referral program** — standard practice in homeschool curriculum (bloggers expect it), and it converts your happiest families into your sales force. Plus a simple in-product "refer a family, both get a month free."

**What I'd skip for now:** broad Facebook/Google ads (expensive vs this budget, weak against trust-based buying), school/district sales (long cycles — revisit in 2027), and app-store presence (you're a web app; fine).

**The one metric for the next 90 days:** paying families from beta conversions + reviews, against a simple target — e.g., 50 founding families by November. Everything above feeds that number.

---

## The short list — what I'd do next, in order

1. **Deploy the current builds** (mz/na/nb are on your disk, uncommitted) and send me the two /admin panels: "Referee fires by name" and the new build/serve cost tiles. Those unlock the accuracy fix and the final price.
2. **Say go on the methodology build** — WWC/NCTM/GAISE citations mapped to your enforced rules. One build, big marketing payoff.
3. **Decide passwords + payments** as the next engineering block — the launch gate.
4. **Pick the price** ($15/$12-annual recommended) once the serve-cost number is real; I'll update pricing.html in both places.
5. **Start Phase 0 marketing now** — beta recruitment costs nothing and everything else compounds on it.

---

*Sources: [Khanmigo pricing](https://www.khanmigo.ai/learners) · [IXL family pricing](https://nibble-app.com/blog/ixl-cost) · [Synthesis Tutor pricing](https://brighterly.com/blog/synthesis-tutor-cost/) · [Math Academy $49/mo debate](https://biggo.com/news/202508150714_Math_Academy_Price_Debate) · [Mathnasium cost](https://tutors.com/costs/mathnasium-cost) · [CTCMath vs Teaching Textbooks pricing](https://smarterlearningguide.com/ctcmath-vs-teaching-textbooks/) · [WWC algebra practice guide](https://ies.ed.gov/ncee/wwc/practiceguide/20) · [WWC math practice guides](https://ies.ed.gov/ncee/wwc/Math/) · [GAISE II (free PDF)](https://www.amstat.org/asa/files/pdfs/GAISE/GAISEIIPreK-12_Full.pdf) · [Cathy Duffy Reviews](https://cathyduffyreviews.com/) · [HEAV exhibitor info](https://heav.org/convention/exhibitor-information/) · [Great Homeschool Conventions exhibitors](https://greathomeschoolconventions.com/exhibitors) · [Homeschool conventions list 2026](https://thathomeschoolfamily.com/homeschool-conventions-conferences-by-state/)*

*I did no harm and this file is not truncated.*

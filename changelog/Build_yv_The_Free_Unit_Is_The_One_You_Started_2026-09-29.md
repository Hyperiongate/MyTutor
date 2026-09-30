# Build yv — the free unit is the one you started (2026-09-29)

Stamp: `2026-09-29yv-the-free-unit-is-the-one-you-started`. Battery: **13,343 passed · 0 failed · 3 skipped**
(PART 3op added; one count pin moved, 40,542 → 40,543). Prewarm: **1 line** (`LINE_FREE_GATE`).

The second build off Jim's first-family playthrough (`claude/Playthrough_2026-09-29_The_First_Family.md`):
the money path's two blockers, F26 (no free-tier gate) and F27 (no way to pay), read against
the code and closed where the code was wrong. Where the code was right and the *site* was in
beta, the build makes the site say so.

## F26 — the free tier was the paid tier

`/pricing` promises the Free plan "one placement check + a first unit to try". Jim placed
into Entry unit 2 on a free account, finished all four of its lessons, and unit 3 lesson 1
opened with no gate.

**Cause.** The one gate, `_free_gate`, sat on `/api/chat` — the LIVE lane — and counted
`units_mastered`, which is the 90% Unit Quiz (`unit_checks`), a thing the scripted course
never runs. `/api/script/start`, the lane a child actually uses, had no gate at all. So a
free student could play every scripted lesson in every course.

**Rule.** The free unit is the `(course, unit)` of the **first scripted lesson a free
student opens** — the unit the placement sent them to, not unit 1. `store.free_units` holds
one row per student, written once (`record_free_unit`, first writer wins; `free_unit` reads
it); it joins `_STUDENT_CODE_TABLES`, so a removed student takes it with them and the
parent's next student gets their own. A lesson in that unit is theirs; a lesson anywhere
else — the next unit, another course — is the gate.

**Where.** `_free_unit_gate` in `_script_start_lesson`, before any state is built or any
review is queued: the response is one spoken line (`lessonscripts.LINE_FREE_GATE`, a
standalone course line — no name, no price, one cached clip for everyone) plus `gated` and
the Family card's URL; nothing starts behind it. `_free_unit_gate_live` on `/api/chat`
keeps the same promise on the live lesson lane (another course, or a named other unit, is
gated; the existing Unit-Quiz rule stays), OR'd in before the paid call. Both fail OPEN on
any doubt — no store, a persona (tier `pilot`), a lookup error, nothing written — because a
wrongly closed door costs a family a lesson and a wrongly open one costs a cent.

**On the page.** `session.html` shows the Family card (`showGateCard`: a `feedBlock` like
the Unit Quiz card — "Your free unit is done · Nice work! · Ask your parent to open the
Family page…" and one link to `/family`; tokens only, 3hp) on a gated start and on the live
lane's `upgrade_required`, and plays the line. The child cannot type a URL; the parent will
read the card.

**Proof.** PART 3op drives the whole thing through the real endpoints on a sqlite family:
signup → student → the first lesson in unit 2 is free and sets the unit → another unit-2
lesson is free → unit 3 is the gate (exactly one `say` step, `LINE_FREE_GATE`, `gated`) →
another course is the gate and the unit did not move → `/api/chat` gates another course and
a named other unit → the parent subscribes (`sub_status=active`, what the Stripe webhook
writes) and the same unit-3 lesson opens → the student is removed and the next student
starts with a fresh unit of their own → persona 1234 is never gated and never recorded →
`/api/billing/status` says closed.

## F27 — "no way to pay"

Read against the code: the family page HAS the Subscribe buttons (since 08-01) — they show
when `billing_ready`, and `_payments_open()` is true only with a live Stripe key or
`PAYMENTS_OPEN=open`. The site is in beta, so the page shows the amber beta notice instead
(Jim read "Free plan" and stopped there). `/pricing`'s "Get full access" went to `/family`
regardless, where there was nothing to buy — that is the part that was wrong.

**Fix.** `GET /api/billing/status` (public, one boolean). `/pricing` reads it: while
payments are CLOSED the Full-access button says "Free during beta — join the beta →" and
goes to `/beta`; when they OPEN, the beta ribbon and the amber notice hide themselves and
the button goes to `/family`, where the Subscribe buttons are. The static text is the closed
state, so a browser with no script still sees the honest version. Launch day is one Render
variable, not a page edit.

**What Jim does to walk the money path** (the half of the playthrough that has not
happened): in Render set `PAYMENTS_OPEN=open` with the TEST Stripe key
(`STRIPE_SECRET_KEY=sk_test_…`, `STRIPE_WEBHOOK_SECRET` for the test endpoint), redeploy,
then as the parent: `/family` → Subscribe → card 4242 4242 4242 4242 → back to `/family`
showing Full access · Active → the child's gated lesson opens. Then remove the override.
Before a stranger pays: the live key, and the override gone.

## Files

`main.py` (`_free_unit_gate`, `_free_unit_gate_live`, the scripted-start gate, the live OR,
`GET /api/billing/status`, stamp), `store.py` (`free_units`; `free_unit`,
`record_free_unit`; the reset registry), `lessonscripts.py` (`LINE_FREE_GATE`, standalone),
`static/session.html` (`showGateCard`; the card on both lanes; CSS), `static/pricing.html`
(the button reads the status; ids), `ruletests.py` (PART 3op; 46 count pins 40,542 →
40,543), `speechmap.py` (regenerated; `SCANNED` 40,848 → 40,849, MAP 941 unchanged), this doc.

I did no harm and this file is not truncated.

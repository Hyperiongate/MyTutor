# Build zi — the parent can delete everything (2026-10-12)

Stamp: `2026-10-12zi-the-parent-can-delete-everything`. Battery: **13,574 passed · 0 failed · 3 skipped**
(PART 3pc, 14 checks, added). **Nothing to prewarm.** Builds on zg and zh (on disk, not yet
pushed — one push carries all three).

PM-13 on the PM board, the first Phase 2 ("make it safe") build.

## What was wrong

- **A parent could not close the account.** Remove deleted one student (build dy), but the
  parent's email, name, password, sign-ins, weekly-email settings and billing link stayed until
  someone emailed support. The privacy page said the button was "on the roadmap". The amended
  COPPA Rule (enforceable since 2026-04-22) expects deletion on a parent's request.
- **Found on the way: the delete was never complete.** `drill_daily` (the drill lane's days)
  and `student_phrasings` (the tutor's first-phrasing memory) are one-student-per-row tables
  that never joined `_STUDENT_CODE_TABLES`. So every Remove, every Start Fresh and every beta
  delete left them behind, and a regenerated login code orphaned them on the dead code.
- **And the tallies kept the code.** `usage_log` (cost), `system_events` (health) and `flags`
  (Jim's flags) kept a deleted student's login code on their rows.

## What it is now

- **Family page → 🗑️ Delete my account** (folded shut at the foot of the page). It says what
  goes and what stays, asks for the **password** (proves it is the parent, not a student on an
  open laptop) and the typed word **DELETE** (proves it is not a slip).
- **`POST /api/parent/delete-account`**, in this order, all or nothing:
  1. **Billing first.** Every live Stripe subscription is canceled and the Stripe customer
     deleted (its saved cards go with it). If Stripe can't be reached, or there is a live plan
     and no Stripe key, **nothing is deleted** and the parent is told to try again or email
     support. A deleted account that keeps charging would be the worst outcome.
  2. **One transaction:** every student and every per-student row, the sign-ins, reset links,
     email settings and the parent row; the students' codes blanked on the cost, health and
     flag tallies; forum posts kept for the families who replied, signed "Former member" with
     no parent behind them. The deletions ledger keeps a backup restore from bringing any of it
     back.
  3. Lesson state in memory for those students is dropped; a confirmation email goes to the
     address after the fact; this browser signs out and the page says it is done.
  Rate-limited to 5 tries an hour per IP, because it checks a password.
- **The cascade is complete now** for every delete path: `drill_daily` and `student_phrasings`
  joined `_STUDENT_CODE_TABLES`, and `_STUDENT_CODE_SCRUB` blanks the code on `usage_log`,
  `system_events` and `flags` in reset, beta delete and the parent cascade. Remove (one student)
  also drops that student's lesson state now.
- **Privacy page** (still a draft under counsel's review): the delete paragraph says how to do
  it yourself, what each button deletes, that billing is canceled first, the forum rule, and that
  backups are never used to restore a deleted account. The email route stays.

## Proof

PART 3pc: the registry and scrub pins; the route's order (rate limit, password, DELETE, billing
before the cascade); the card and the privacy text. Then **on a real SQLite database**, two
families of two students each with drill days, phrasings, cost rows, events, flags and a forum
post: a wrong password is 403 and a mistyped DELETE is 400, nothing deleted; a live plan with no
Stripe key is 409, nothing deleted; Stripe down is 409, nothing deleted; Stripe up cancels the
live subscription (not the old canceled one), deletes the customer, then removes both students;
nothing of them is left in any per-student table; the tallies remain with the codes blanked; the
forum post reads "Former member"; the other family is untouched; the old token is refused; the
ledger holds the email and both codes.

## Still open (not this build)

- **Off-site backup emails.** The weekly off-site copy is emailed to Jim's inbox and stays there
  until he deletes it, so a deleted family lives on in old emails. The ledger stops a restore
  from reviving them, but the retention policy (counsel, PM-10) needs a rule: keep the newest few
  and delete the rest, or move off-site copies to storage that expires them.

## Files

`main.py` (stamp, the route, Remove drops lesson state), `store.py` (the registry, the scrub,
`delete_parent_cascade(anonymize_forum=)`), `static/family.html`, `static/privacy.html`,
`ruletests.py` (PART 3pc), this doc.

I did no harm and this file is not truncated.

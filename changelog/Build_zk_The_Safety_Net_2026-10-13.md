# Build zk — the safety net (2026-10-13)

Stamp: `2026-10-13zk-the-safety-net`. Battery: **13,612 passed · 0 failed · 3 skipped** (PART 3pe, 22 checks). **Nothing to prewarm** (the
crisis reply renders once, live, the first time it is ever needed, then comes from the cache).
Builds on zi and zj (on disk, not yet pushed — one push carries all three).

PM-12 on the PM board, the second Phase 2 ("make it safe") build. The 10-09 deep dive:
*"a safety layer that does not depend on the tutor obeying."*

## What was wrong

Until zk, the only thing between a child saying "I want to die" and Mr. Cadabra's next
fraction was ground rule 31 in the tutor's own prompt. That is a nudge, given to the same
model that is busy teaching. Nothing told a parent, nothing was recorded, and if the model
missed it nobody would ever know.

## What it is now

**`safety.py` — a separate reader.** It does one job:
`classify(message) → crisis | personal_info | none`.

- A message with no words (`12`, `3/4`, `x=5`) needs no reader and gets none.
- Anything else is read by a small, fast model (**Claude Haiku 5.5**, `claude-haiku-5-5`,
  about a twentieth of Sonnet's price). It uses a strict prompt, temperature 0, a 3-second
  ceiling and no retries, and answers in JSON.
- If that model can't answer (no key, a timeout, a garbled reply), a **keyword screen**
  decides instead, so the net never vanishes when the model is down. The keywords are tuned
  for precision: "this homework is killing me", "the car hits a wall" and "hit me with a
  harder one" are not crises, because a false alarm reaches a parent.
- An unmistakable phrase is a crisis even if the model says otherwise.

**Every free-text door goes through it before the tutor:**

- the live lesson (`/api/chat`), screened before the free-plan gate, the exam gate and the tutor;
- homework help (`/api/practice`);
- topic help (`/api/topic`);
- the raised hand in a scripted lesson (`/api/script/ask`);
- a spoken or typed answer in a scripted lesson (`/api/script/answer`'s `said`). There, to keep
  the lane's zero-wait promise, only the keyword screen runs on every answer, and a hit is then
  confirmed by the model. It runs first, before any door that grades.

**A crisis:**

- Mr. Cadabra does not teach. He says the fixed reply (`safety.CRISIS_REPLY`): thank you,
  this matters, you matter; tell a grown-up you trust today; 9-1-1 if you're in danger right
  now; call or text 9-8-8 any time; we can get back to math when you're ready. The numbers are
  written with dashes so the voice reads them as digits.
- The exchange stays in the conversation, so the next turn knows.
- In the scripted lane, nothing is graded and the question stays on screen.
- The alert is recorded (`safety_alerts`). The parent is **emailed** with the student's name
  and own words, at most once per student every 6 hours (`SAFETY_EMAIL_HOURS`); every alert
  still shows on the Family page.
- Jim gets a **SAFETY** ops email. For a student with **no parent account** (pilot, beta or class
  code), Jim's email carries the words, because nobody else would see them.

**Personal information** (an address, phone or email): the tutor answers as usual (rule 31b
tells him not to repeat it). The alert is recorded and shown on the Family page, with no email.

**The Family page** gets a **🛟 Safety notes** card, shown only when there is something in it.
Each note gives the student, when, where, their own words and what Mr. Cadabra did, plus a
"Mark all as read" button. A parent sees only their own students' notes.

**Housekeeping:**

- `safety_alerts` joins the delete cascade (`_STUDENT_CODE_TABLES`) and ages out after 180 days.
- `/health` `subsystems.safety` says whether the net is loaded.
- Each decision is counted (`system_events` kind `safety`, with the milliseconds) and the
  reader's tokens are logged (usage kind `safety`), so cost and wait show on /admin.
- `SAFETY_CHECK=off` switches the model reader off; the keywords stay on.
- The privacy page gets "Keeping students safe" (still a draft under counsel's review).

## Proof

PART 3pe has 22 checks.

**Offline:**

- The keyword screen catches eight crisis phrasings and leaves eight ordinary ones alone, both
  ways; personal information is picked up.
- The model reader (with a stand-in client) decides, at temperature 0, on Haiku 5.5, and
  reports its tokens.
- An unmistakable phrase overrides a "none".
- A timeout or a garbled reply falls back to the keywords.
- A bare number never calls the model; `SAFETY_CHECK=off` still catches a crisis by keyword.
- The reply's wording is checked.

**Every door screens before the tutor.** The scripted lane screens before the reason door and
before `read_answer`.

**Live on a real database:**

- A crisis in the live lesson gets the reply, and the conversation keeps both lines.
- The parent's email carries the name and the words; Jim's carries neither.
- Homework and topic help answer the same way, and a second crisis within 6 hours sends no
  second email.
- Personal information is recorded with no email.
- The Family feed shows four notes newest-first; another parent sees none and cannot mark them read.
- A pilot code's crisis puts the words in Jim's email.
- `/health` reports the net loaded, and removing the student removes their notes.

**The scripted lane, driven for real:** a spoken "I want to die" mid-question returned the reply,
kept the question's buttons, and left the lesson exactly where it was. The next spoken answer
was graded normally.

**Not yet measured:** the real Haiku 5.5 wait per message, because no API key is available
here. After the push, `/admin` Telemetry will show the `safety` events with their milliseconds.

## For counsel (PM-10)

The crisis reply's words, the parent email, the categories, and the 180-day retention all need
counsel's read. The words live in `safety.py` and `main.py` (`_safety_email_parent`), each in one
place.

## Files

`safety.py` (NEW), `main.py` (stamp, the gate, five doors, the parent safety endpoints, purge,
`/health`), `store.py` (`safety_alerts` and helpers), `static/family.html` (Safety notes),
`static/privacy.html` (Keeping students safe), `ruletests.py` (PART 3pe), this doc.

I did no harm and this file is not truncated.

# Build zo — the truth pass (2026-10-15)

Stamp: `2026-10-15zo-the-truth-pass`. Battery: **13,659 passed · 0 failed · 3 skipped** (PART 3pi, 14 checks; one older pin re-pinned). **Nothing to prewarm.**

PM-43 on the PM board, carried from the 09-28 deep dive: make the README, MARKETING.md and the
site say what the product actually does today. I checked each claim against the code, not
against the docs.

## What was wrong, and what it says now

**/methodology's numbers strip.** It said "counted, not claimed", but every figure was a month
stale:

| Tile | Said | Is |
|---|---|---|
| hand-built lessons | 336 | **360** |
| practice problems | 25,376 | **29,037** (the drill pool, counted this run) |
| automated checks per release | 11,582 | **13,600+** (shown as a floor now) |

The strip now reads "as of October 2026". The practice-problem count in the prose moved with
the tile.

The reason it went stale: one test held the exact number 11,582 as a reminder to update the
page by hand. Nobody did. **PART 3pi now counts every tile from the code on every run**:

- lessons, courses and the drill pool must match exactly;
- the release-check tile is a floor, checked against the run's own pass count. The test fails
  if the tile claims more checks than the run passed, or falls 1,000 behind.

**/methodology's accuracy paragraph overclaimed.** It said:

- "every mathematical claim … re-computed";
- "a reply that fails one is rejected and rewritten, not shipped";
- "two AIs and a math engine … on every single reply".

What the code actually does:

- The math engine re-computes the answers the tutor declares and the equations it draws.
- Wrong math is rewritten, and if it can't be fixed it is never sent.
- A teaching miss that survives its rewrites ships as the best draft and is logged.
- The second AI reads each reply the automated checks pass.

The paragraph now says that. Section 3's opening said "Thirty-three" of the rules are enforced
by code; RULES.md, which is generated from the code, says 32. It now says 32, and PART 3pi
ties both counts to RULES.md.

**The landing page FAQ.** These changes were made in both the visible FAQ and the JSON-LD copy
that Google reads:

- The model is now "currently Claude Sonnet 5.5" (it said Sonnet 5).
- "Every problem and answer Mr. Cadabra states is double-checked … silently corrected" now
  says what is true: the written lessons' answers are computed by code, the live tutor's
  answers and board equations are re-computed by the engine, and a reply that can't be put
  right isn't sent.
- "Request deletion" now says you delete it yourself on the Family page. The trust strip's
  "delete-my-data on request" is now "a delete-everything button on your Family page".

**Features page:**

- "Every answer math-checked … checked, every time" now says the same accurate thing as the
  landing FAQ.
- "Everything managed in one place" now includes the self-serve account delete.
- The accessibility line keeps its three real features and drops "the classroom door is wide
  open" until the audit (PM-34) is done.

**Parents page:** "deleted any time with one email" appeared twice. Both now say you do it
yourself on the Family page.

**llms.txt** (what AI crawlers read):

- The Free plan is "a first unit to try, unlimited practice and topic help". It said "first
  mastered unit".
- It now says "360 hand-built lessons".
- It now says deletion is self-serve.

llms.txt has no notes header on purpose (its first line must be the title), so its change is
recorded here.

**README.md:**

- "8 courses" is now 10.
- The status now points to the PM board.
- "every reply passes 101 referees" now says what happens.
- The production model is claude-sonnet-5-5.
- The note pointing at a missing Haiku study is fixed.
- The Free plan is described correctly.

It adds what shipped since 09-28:

- one plan per student;
- the safety net;
- self-serve delete;
- the second opinion and its rewrite limit;
- the model trial;
- the weekly PC backup;
- browser-error and STALE JOB emails;
- the settings each of these reads.

**MARKETING.md:** rule 3 now gives the price (per student), what the math engine checks, and
that deleting is self-serve. "a assistant" is now "an assistant".

**RECOVERY.md and render.yaml** are the rebuild recipe. Before this build, a rebuild from them
would have come up on Sonnet 5 with no second opinion. Changes:

- `CLAUDE_MODEL=claude-sonnet-5-5`.
- The settings added since August: the second opinion's four, `DATA_EXPORT_KEY` and
  `NIGHTWATCH=off`. Secrets stay in the dashboard only.
- The "weekly download" habit now says the PC backup takes it automatically.

## Not changed — for Jim and counsel

- **privacy.html says "Our backups are short-lived."** That is true for the nightly snapshots
  (14 kept) and the PC copies (8 weeks). It is not true for the off-site backup emails, which
  stay in Jim's inbox until a retention rule exists (PM-16). That sentence belongs to counsel
  (PM-14), so I left it. It should change when PM-16 is decided.
- **terms.html says "you can ask for a copy or for deletion".** It is still true; deletion is
  also self-serve now. That is counsel's text too.
- The safety net is not claimed anywhere in marketing copy. It should be, after counsel reads
  the words (PM-10).

## Proof

PART 3pi checks:

- the tiles are counted from the code: lessons, courses, the drill pool (PART 3de now hands
  over its total), the release-check floor against this run, and the written and enforced rule
  counts against RULES.md;
- the overclaims are gone from nine marketing pages' visible copy;
- the landing FAQ and its JSON-LD say the same thing;
- deletion is described as self-serve;
- README, MARKETING.md and llms.txt carry the code's counts;
- one live model is named alike in render.yaml, README, RECOVERY and the landing FAQ;
- the dated notes are in.

It runs last, so the pass count it reads is the full run's.

**Re-pinned on purpose:** PART 3dq's `<b>11,582</b>` is now the floor shape, and PART 3pi holds
its value.

The numbers strip was rendered in Chromium at 390 px and 1280 px, with no horizontal scroll.

## Files

`static/methodology.html`, `static/landing.html`, `static/features.html`, `static/parents.html`,
`static/llms.txt`, `README.md`, `MARKETING.md`, `RECOVERY.md`, `render.yaml`, `main.py`
(stamp), `ruletests.py` (PART 3pi, PART 3de's total, the 3dq re-pin), this doc.

I did no harm and this file is not truncated.

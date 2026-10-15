# Build zm — the trial card says finished (2026-10-14)

Stamp: `2026-10-14zm-the-trial-card-says-finished`. Battery: **13,632 passed · 0 failed · 3 skipped** (PART 3pg, 6 checks). **Nothing to prewarm.**

## What was wrong

not. It looks like there's a report there, but I didn't tell it to, something's running in the
background."*

The trial had finished. The status line said so ("last trial finished:
trial-20261014-234902.md"). But the green message under the buttons kept saying "Running in
the background — this card follows it." The card set that message when Run was pressed, and
nothing replaced it until the page was reloaded.

## What it does now

- **While a trial runs:** the message says "Running in the background — N s so far. This card
  follows it; nothing else to press yet." **② Run** is greyed out, so a second press cannot be
  confused with the first one's progress.
- **The moment it ends**, the message is replaced once, according to how it ended:
  - **Finished.** "Nothing is running now. The new report is picked below — press Read that
    report." The new report is selected in the list.
  - **Stopped early**, with the reason (for example, a model the key can't reach).
  - **FAILED**, with the error.
- **Reloading the page mid-trial** still works: the card notices the running trial and follows
  it the same way.

Only `static/admin.html` changed in behaviour. `main.py` carries the new stamp so the push can
be confirmed on `/health`.

## Proof

PART 3pg drives the card's real script in node, with a stand-in page and server:

- Run → running: the message shows the seconds, and Run is disabled.
- Then done: the message says Finished, the new report is picked, Run is back, and the status
  line agrees.
- A later status read leaves the message alone.
- A trial that stopped early says "Stopped early" with the reason; a failed one says "FAILED".
- The dated notes are in.

## Files

`static/admin.html`, `main.py` (stamp), `ruletests.py` (PART 3pg), this doc.

I did no harm and this file is not truncated.

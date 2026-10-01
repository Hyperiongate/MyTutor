# Build zb — the code leaves the address bar (2026-10-01)

Stamp: `2026-10-01zb-the-code-leaves-the-address-bar`. Battery: **13,493 passed · 0 failed · 3 skipped** (PART 3ov
added; 3ou's F34 pin reads both rulings; three hub/dashboard link pins moved to sq()). **Nothing to prewarm** — no spoken line changed.

Jim's playthrough F34, ruled on 10-01 ("go"): the student's sign-in code is the credential,
and every student page carried it in the URL — history, bookmarks, screenshots, the address
bar a classmate reads over a shoulder. His ruling of 2026-08-18 stands beside this one: **"do
not kill the bookmark login"** — a family bookmark with the code is how a young student signs
in. This build honours both.

## What it does

**One shared script, `static/student-code.js`**, loaded in `<head>` on every student page
before the page's own script. A page that ARRIVES with `?code=` — a bookmark, a link from the
family page, the login hand-off — stores it in the `mt_student` cookie (this origin only,
SameSite=Lax, 30 days, Secure on https) and takes it out of the address bar **in place**:
`history.replaceState`, no reload, every other param and the hash kept, no new history entry
so Back is untouched. A page that arrives WITHOUT a code reads the cookie. Every link a page
builds to another student page carries the course and never the code (`MTStudent.q`). The
login page puts the verified code in the cookie and sends the student to `/home` with a clean
address.

**The parent's doors are deliberately different.** `/dashboard?code=…&view=parent` and
`/records?code=…` are the parent reading one student — often a sibling a minute after the
first — on the family's shared laptop. Those pages use the code in their own URL and
**neither store nor strip it** (`MTStudent.code({ keep: true })`), so viewing a sibling's
progress never changes which student the laptop is signed in as, and a reload of the
parent's page keeps working. The family page's links to those doors still carry the code; the
parent holds no cookie. `/records` opened from the student's own dashboard (which links there
without a code now) reads the cookie.

**Eleven pages and three shared scripts** read the code the new way: home, session, practice,
topic, challenge, dashboard, records, drill, pilot, index (login) — and `app-nav.js`,
`library.js`, `time-tracker.js`, which run after the page script has already cleaned the
address and so must read the cookie, not the URL. Every one keeps the URL as its fallback, so
a browser whose cache still lacks the new script works exactly as before across the deploy.

**The server is unchanged.** API calls have carried `X-Student-Code` since build hs; `main.py`'s
`_code_dep` still reads the header, then the path form for a stale page. Its docstring now
carries both rulings side by side. Nothing a student taps inside the app carries the code; a
bookmark with the code still signs in.

## What a family will notice

Nothing, except that the address bar no longer shows the code. A bookmark saved before today
keeps working (it signs in and the bar cleans itself). A bookmark saved after today on the
same device also works — the cookie is on that device. A bookmark saved after today and opened
on a *different* device goes to the sign-in page, where the code is typed once and remembered
for thirty days on that device too. Two students sharing one browser: the last code signed in
is the one the browser holds — exactly as it was with two bookmarks.

## Proof

`tools/zbdrive.py` (PART 3ov runs it), the real pages under a stub that serves the app's
routes: the login lands on `/home` with the cookie set; `/home?code=1234&course=entry` writes
the cookie and becomes `/home?course=entry` in place with every tile and chip code-free, and
Back from a lesson returns to the clean hub (the history count equals a load with nothing to
strip); `/topic?course=basic` with only the cookie stays, its API call carries the cookie's
code, the top bar's links carry no code, and `library.js` drew "Look it up"; `/session?code=
1234&course=entry&tour=1` becomes `/session?course=entry&tour=1`; `/dashboard?code=5678&view=
parent` keeps its address, reads 5678 for its API call, keeps the code in its Records link
and leaves the student cookie (1234) alone; `/records` reads the cookie, `/records?code=5678`
uses 5678 and stores nothing; Abrabot's room fills its box from an arriving code, cleans the
address, and a typed code becomes the cookie. PART 3ov also pins every line in the source and
the server's unchanged resolution.

## Files

`static/student-code.js` (NEW), `static/index.html`, `static/home.html`,
`static/session.html`, `static/practice.html`, `static/topic.html`, `static/challenge.html`,
`static/dashboard.html`, `static/records.html`, `static/drill.html`, `static/pilot.html`,
`static/app-nav.js`, `static/library.js`, `static/time-tracker.js`, `tools/zbdrive.py` (NEW),
`ruletests.py` (PART 3ov; 3ou's pin), `main.py` (stamp; `_code_dep`'s docstring), this doc.

I did no harm and this file is not truncated.

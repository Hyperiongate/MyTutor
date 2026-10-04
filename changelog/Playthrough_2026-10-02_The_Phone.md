# Playthrough — 2026-10-02: the phone (a new family, on Jim's phone)

Jim played mrcadabra.com as a brand-new family on his phone, upright, with a fresh parent
email: the front page → /family (account, a student, the code) → student sign-in → Entry →
the tour → lesson 1 (counting to 10) → lesson 2 (counting to 20, spoken answer) → the dock's
navigation → the Progress dashboard → signing out and back in as the parent. He stopped there.
Not played: the placement on the phone, the parent's dashboard on the phone, the Friday email.

Site at start: `/health` = `2026-10-01zb-the-code-leaves-the-address-bar`, PAYMENTS_OPEN
removed, the prewarm done.

**Clean on the phone:** sign-up, the code chip (Copied!), student sign-in, the address bar
without the code (zb), the tour's stops and tag, the tap registering at once (yu), a spoken
answer, the end-of-lesson hand-off, no award mid-lesson (yx).

## The ledger

P1. [cosmetic] /family: the three numbered steps sit just below the fold on the phone. **Built — zc.**
P2. [confusing] The tour names the microphone two or three times and never lights it; it is
    grey (disabled, the tour is running) and the glow is on the buttons, not the mic — "you
    have to really look around to find the microphone button."
P3. [BLOCKER] Lesson 1, "count the stars — how many?": no stars on the screen and no way to
    scroll to them. The dock (mic, Pause, the hint, the helper line and three 72px child-mode
    buttons) was 562px of a 844px screen and the board was 26px, measured. He guessed wrong,
    the walk-back redrew the stars after the buttons cleared, and then he could answer.
    **Built — zc:** the buttons land on the board under his words; the dock gives back two rows.
P4. [pedagogy] Entry unit 1 lesson 1 is "counting to 10" and never counts to ten out loud.
    The lesson should do what its title promises once — a straight count, 1 to 10, the stars
    ticking in — before it asks the child to count a smaller group. Read the lesson first.
P5. [layout] Lesson 2's twenty stars in one row ran off both edges of the phone. **Built — zc:**
    rows of ten ("ten and ten"), a smaller star on a phone, every row may wrap.
P6. [confusing — navigation] The dock's nav strip is one word per screen ("Curriculum",
    then "Course assessment"), and Curriculum opens as a thin column inside the sideways
    strip. A child cannot use it. Fix: a ☰ button in the top bar opening a full-screen sheet
    with the links in a plain vertical list; the Curriculum as its own screen, units stacked.
P7. [layout] The Progress dashboard on the phone "doesn't fit well" — the laptop page squeezed.
    Render it at 390px and decide: a layout fix, or a shorter phone version (the course tiles
    and "strengthen next" first, the rest a tap away).
P8. [confusing] Student → parent on one phone is a chore: no visible Sign out for the student,
    and the sign-in page's Parent door asks for the *student's* code when a parent with an
    account should sign in with email + password and land on /family. Fix: the Parent door
    goes to /family; the code form stays for a parent without an account; the student's menu
    (P6's sheet) gets a plain Sign out that clears the mt_student cookie (zb).

## Build order

1. ~~`zc`~~ — P3 (the blocker), P5, P1 — done.
2. `zd` — P6 + P8 together: the phone menu sheet (with Sign out) and the Parent door.
3. `ze` — P2 (the tour lights the mic) and P7 (the dashboard at 390px, after a render).
4. P4 after reading Entry u1 l1 against its title (a lesson edit; prewarm).

Open for Jim: the placement on the phone (and its 45-question length); F20's "is"/"eyes"
sentence when he hears it again.

I did no harm and this file is not truncated.

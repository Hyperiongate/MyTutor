# CHANGELOG -- practice.html  (notes rolled out of the file's header)

Moved out of `static/practice.html` on 2026-09-08 (build ui): every CHANGE NOTE dated before 2026-09-01 -- 60 entries, VERBATIM, in the order they sat in the file (newest first). The 13 notes from 2026-09-01 on stay at the top of `static/practice.html` itself, and new notes keep going there. Nothing below was edited; grep this file for a build letter or a date. When the header is rolled out again, the newer block is added ABOVE this one.

```text
    (rc) 2026-08-31 -- THE STAR FALLS WHEN THE CHILD SLIPS. New [[miss]] tag handled
    beside [[mark]]: the model reports a wrong tap on the still-going problem, the page
    posts {miss:1} to /api/mark/me, and the server resets the today-streak (Jim's
    ruling: a miss is ANY wrong tap). No counters move -- a slip is not a finished
    problem. The code floor (server-side computed grading) lives in main.py/tutor.py.
    (os) 2026-08-27 -- THE BOARD READS ONE, TWO, THREE. Jim: "it clearly says this is
    one, then two, then three... and the student doesn't have to scroll around to find
    it." NEW [[stepcard n="1" title="..."]] tag dispatched here -- a labeled Step-N card
    joins a flex row that fills the board; every block after it (worklists, figures,
    columns) lands INSIDE the card until the next [[stepcard]] or the end of the turn.
    clearStepGrid() at turn start so an open card never captures the next turn; the
    dispatcher resets curWork so a following [[step]] starts a fresh worklist in the
    card. Machinery + CSS injection + full story in board.js's own change note.
    (oj) 2026-08-26 -- SIDE BY SIDE ON PURPOSE. Jim: "the whiteboard is underutilized...
    the bubble only goes about seventy or eighty percent across... they can move to the
    side." Two changes: (1) .feed .bubble max-width 80% -> 96%; (2) NEW [[beside]] tag
    dispatched here -- the next board block joins the previous one in a .mrow (CSS added
    by .mblock; flex-wrap so phones stack the columns). getWorklist/feedBlock now mount
    blocks through board.js mountBlock (the one door); clearBeside() at turn start so a
    dangling tag never leaks. Machinery + full story in board.js's own change note.
    (gz) 2026-08-17 -- THE gr FIX FINALLY WORKS ON THIS PAGE. Build gr's expect=letter
    hint reads expectsALetter(lastTutorText) inside transcribe() -- but lastTutorText was
    session.html's page-level variable and was NEVER declared or assigned here, so that
    read threw a ReferenceError, transcribe()'s catch returned "", and EVERY spoken answer
    on this page was silently discarded as "I didn't quite catch that". Same class, second
    instance: the visibilitychange handler read session.html's undeclared `started`, so
    keep-alive never restarted after a tab switch (the "first word swallowed" family).
    Fixed: lastTutorText is declared page-level and assigned where the tutor's words are
    rendered; the handler now uses this page's own audioWarmed flag. Found by the
    2026-08-17 full-app review (cross-page copy-divergence class); ruletests PAGE_PARITY
    now guards both so a teaching page can never again use state it does not own.
    (gr) 2026-08-17 -- THE SPOKEN LETTER. Jim was asked which side was the hypotenuse, said
    the letter "c" out loud, and ElevenLabs transcribed it as the Spanish "si" / "CSI" --
    whereupon the tutor told him he was wrong and demanded a letter. A student marked
    incorrect for a machine's mistake. /api/transcribe now sends a language hint and owns a
    spoken-letter map ("see"/"sea"/"si"/"CSI" -> c); this page supplies the CONTEXT via
    expectsALetter(lastTutorText), so the rewrite happens only when the tutor actually asked
    for a letter and a "see" in ordinary speech is never touched. Deliberately excluded from
    the map: oh, eye/I, you, are, why -- each is a plausible whole utterance from a student,
    and inventing a variable they never said is what rule 64 forbids.

    (gp3) 2026-08-17 -- THE PROBE LEARNS TO SAMPLE TWICE. Jim's first [voicehead] output
    read "ctx=running" on all five clips and it was reported to him as "the graph was never
    suspended, so the resume race never fired" -- which was WRONG, and would have sent the
    next fix chasing the MP3 decoder. The probe samples the graph when the audio STARTS,
    and making that state "running" is precisely what the gn fix does; a probe that reads
    state only AFTER a fix has acted cannot tell you whether the fix was needed. It now
    logs ctx0 (what we found) alongside ctx (what we started into). Jim confirmed the same
    lesson: "Better -- I hear the whole greeting now." The clipping is fixed, three builds
    and one honest instrument later.
    (gn2) 2026-08-16 -- CASE IS MEANING. Jim, on the very lesson that teaches this: the
    board read "A, B, C = corners (vertices)" over "a, b, c = sides (lengths)" and BOTH
    LINES RENDERED IDENTICALLY, because styleVarsCore forced every styled variable to a
    CAPITAL. The one line whose whole job was to separate uppercase from lowercase
    destroyed the distinction it was teaching -- and the figure beside it, correctly
    labelled a=3, b=4, c=?, then disagreed with the words above it (rule 63, caused by us).
    Two changes. (1) A styled letter renders EXACTLY AS WRITTEN and keeps its bold red;
    the 2026-07-22 note that introduced the capital wanted variables to POP, and was
    written when this app taught Algebra I alone. It became false the day Geometry
    shipped: side a is opposite vertex A, the antiderivative of f is F, P(A) is an event
    where p is a probability. (2) The blacklist became a CASE-SENSITIVE question -- which
    letters double as English or as function names? a/A/I and f/F/g/G/h/H -- and those
    earn styling from context (squared, an operator, a letter list, a measurement noun).
    MEASURED against all 1,015 canonical scripts: 218 strings differ by CASE ALONE and 49
    gain or lose a letter, every one of them a formula that was previously inconsistent.
    Four regressions were found by that sweep and fixed before shipping: the article in
    "A **fact family** is..." (the **term** split hides the following word), f and g
    painted red through the function-notation lessons, the g and o of "(f o g)", and
    "the highest point a thrown ball reaches".
    (gn) 2026-08-16 -- THE FORMULA STOPPED BEING WRITTEN TWO WAYS. Jim, live in Geometry:
    "the a in the a squared is not bright, capital, bold, red. It's just a small a." The
    board rendered "a squared plus B squared equals C squared" -- the most famous formula in
    school mathematics, one quantity typeset two ways in a single sentence -- because
    VAR_SKIP meant NEVER STYLE for a, i, f, g and h (a and i double as English words; f, g
    and h as function names). Those five now EARN styling instead: varInMathContext() styles
    them only in an unmistakably mathematical position -- squared/cubed, an exponent, beside
    an operator with a real operand on the far side, or wearing a coefficient -- and never
    when followed by an ordinary word, a prime, or a composition "o". "Pick a number" stays
    prose; "a squared" and "3 + a = 5" become variables like the b and c beside them.
    MEASURED, not assumed: swept over all 1,015 canonical foundation strings, 16 render
    differently and every one is a formula that was previously inconsistent. The new
    screencheck.py S1 fired on 5 canonical scripts BEFORE this change and on 0 after.
    (gn) 2026-08-16 -- THE FIRST WORD, THIRD ATTEMPT: THE RESUME RACE. Jim: "this talking
    actually starts in the middle of the M of Maya. So you don't hear 'hey'." ttsAudio is
    routed through audioCtx, so speak() resumed a suspended graph but ALSO started the clip
    after a flat 300ms so a stuck resume could not hold up the turn -- meaning his words
    could begin playing into a still-SILENT graph, and the safety valve paid for its
    guarantee with the head of the clip. It now waits for the context to actually reach
    "running" (polled, ceiling 1500ms) before starting, and starts anyway past the ceiling
    (the 5s watchdog and withDeadline remain the real guarantees). Builds bl and cb both
    padded the FRONT of the clip with more silence and Jim reported the same defect again;
    this one attacks the mechanism. Shipped WITH a [voicehead] console probe that reports
    where the audio truly began, because three fixes have now been reasoned, not measured.
    (ga) 2026-08-14 -- THE VOICE SAID IT WRONG, THEN THE TURN DIED. Two fixes from Jim's
    2026-08-14 Render log. (1) GARBLED SPEECH: forSpeech() deleted **bold** markers and
    parentheses before handing text to the voice, so the log literally shows
    "that's a right angle ." and "narrower a sharper turn , some are wider a lazier, more
    open turn ." -- asides ran into the sentence and stranded spaces sat before the
    punctuation, which the voice reads as hesitation. Bold pairs now vanish cleanly,
    parentheses become commas so the pause survives, and a tidy-up pass removes the
    leftovers. (2) THE FREEZE: a turn awaits an opening clip, the spoken reply and a
    closing clip; sendToTutor's finally{} re-enables the mic, but a finally cannot run if
    an await never settles -- and twice it did not (chat 200, speak 200, then no listening
    state and no /api/transcribe, ever). New withDeadline() wraps every gate so the student
    always gets control back; a deliberate pause does not burn the clock. Same in
    session.html, practice.html and topic.html.
    (fy) 2026-08-14 -- THE FOLD NOW HAS A TRIGGER IT CAN TRUST. Build fx made a finished
    problem fold away on [[clear]], and in a live lesson it never fired: [[clear]] is taught
    in the prompts as an instruction and NOTHING enforces it, so a turn that forgets it left
    the old problem on screen. [[mark]] is the signal that can be trusted -- the prompts call
    it REQUIRED, it records the student's score, and it means exactly "they FINISHED a
    problem". So [[mark]] now ARMS the fold (at the END of the turn, so a reply that marks and
    draws in the same breath still finishes drawing), and the fold FIRES on the next turn that
    actually starts new board work -- foldIfProblemClosed() at the two chokepoints where a
    board block is born, getWorklist() and feedBlock(). [[clear]] still works and still folds
    immediately; it is now the second trigger rather than the only one. No prompt change, no
    extra model call, no server change. Same in session.html, practice.html, topic.html.
    (fx) 2026-08-13 -- FINISHED PROBLEMS FOLD AWAY (Jim's design note "Narration/Board
    Sync and Board Lifecycle", option 1). [[clear]] used to drop a "-- new problem --"
    divider, so every solved problem stayed on screen and the board never read clean. It
    now MOVES the finished problem into a collapsed block with a one-line summary
    ("Problem 1 -- 2X + 1 = 25") that reopens on click. Deliberately NOT an erase: #feed
    is the lesson TRANSCRIPT as well as the board (chat bubbles and worked math share it),
    so erasing would delete the conversation. Two guards: the CURRENT tutor turn is never
    folded (his words are added BEFORE his tags render, so the bubble introducing the new
    problem is already on screen -- lastTurnEl marks it), and a stretch with no worked
    math in it is never folded (the opener and plain talk keep the old divider). New CSS:
    .probdone/.probsum/.probbody. Same change in session.html, practice.html, topic.html.
    (ee) 2026-08-12 -- THE BOARD SPOTLIGHT, same as session.html (rule 60 / signaling):
    the [[highlight]] tag gains two board keys here -- id="line" glows the NEWEST line
    of board work for ~6 seconds, id="board" glows the whole board. spotlightBoard()
    handles them in the tag dispatcher (this page has no opening tour, so those are
    the only highlight keys it acts on); the glow self-clears on a timer, a new turn
    clears it too (handleTags), and the dz reduced-motion rule stills its pulse.
    (dz) 2026-08-11 -- ACCESSIBILITY + PHONE PASS, same as session.html: live regions
    on the transcription readout + hint, spoken name on the mic, reduced-motion
    support, and the phone DOCK layout (board first, rail stuck to the bottom).
    (dr) 2026-08-11 -- THE YOUNGEST STUDENTS GET A VOICE (Jim). canRecord's !IS_ELEM
    clause removed, same as session.html: entry/basic students get tap-to-talk here too,
    with the tap answer buttons unchanged beside it. Ready-hint teaches both paths.
    (cf) 2026-08-09 -- THE NO-WRAP FIX FINALLY LANDED HERE. session.html got it in build
    bu; this page never did, so for a day Jim's original bug was still reproducible here:
    a long board line WRAPPED inside its grid cell and displayed a literally different
    equation ("dimes: 7 + 8 + = 16" with "1(carried)" underneath). .wrow cells are nowrap
    now and fitRow() shrinks an oversized row until the whole line fits on one line --
    for [[step]] AND [[write]]. ruletests.py PART 3e keeps the three teaching pages in
    step from now on. Also: this page now receives the canonical foundation scripts and
    the student's already-heard list, so a term is defined the SAME way here as in the
    lesson (rule 28) and a returning student is asked instead of replayed (rule 40).
    2026-08-09  FIRST-WORD FIX (build cb): a silent keep-alive loop stops the output
                device sleeping between clips, and the leading pad is now dynamic.
    2026-08-09  PROACTIVE AUDIT, CLIENT HALF (build bu): forSpeech() gains negative
                VALUES ("negative three"; the operation stays "minus", and the board's
                Unicode minus converts too), percents, ratios, common + mixed fractions
                and thousands separators. All three teaching pages.
    2026-08-08  MONEY SPEECH (build bp): forSpeech() reads money as money ($1.85 ->
                "1 dollar and 85 cents") and plain decimals with "point" digit by digit
                (3.75 -> "3 point 7 5") -- never "dot". All three teaching pages.
    2026-08-08  FIRST WORDS + THINKING FLAG (build bl): every TTS clip requests lead=1
                (~560ms leading silence; first keeps lead=3) and a suspended audio
                context is resumed BEFORE the clip starts, so his first words stop
                getting clipped. A red pulsing "Mr. Cadabra is thinking…" badge shows
                mid-whiteboard while he thinks and vanishes when his voice starts.
                Same patch on all three teaching pages.
    2026-08-07  × IS NOT A VARIABLE (build bk): styleVarsCore renders a lone x written
                BETWEEN two numbers ("3 + 2 x 4", "5 x 3") as a true × sign instead of a
                red variable; coefficients (2x) and real variables (3 + x) untouched.
                Same patch on all three teaching pages.
    2026-08-07  FOLLOW FIX, ROUND 2 (build ay): programmatic scrolls no longer release
                following (autoScroll flag); only a real student scroll does. Same patch on
                all three teaching pages.
    2026-08-07  MIC ICON (build bg): the 🎙️ emoji on the talk button rendered as a gray
                glyph on Windows — replaced with a drawn SVG microphone, same as session.
    2026-08-07  FOLLOW THE TURN (build ax): new bubbles re-engage following; tutor turns
                taller than the window anchor to the START of the turn instead of pinning
                the bubble off the top. Same patch on all three teaching pages.
    2026-08-07  PAUSE IS BACK + LIBRARY CHIPS (build aw, Jim): ⏸ Pause button restored
                (pauses the voice, holds the turn; Resume continues). library.js opens with
                context chips + "Something else…".
    2026-08-07  SAY "SQUARED", NOT "TWO" (build av): forSpeech() converts ² ³ π θ ± ≥ ≤ ≠ °
                to spoken words before TTS (the voice read "x²" as "x two"). Same patch on
                all three teaching pages.
    2026-08-07  LOOK IT UP (build as, Jim): included the NEW shared /static/library.js —
                a "📖 Look it up" button in the left nav opens a search overlay + readable
                article bubble (the reference library). One script tag; purely additive.
    2026-08-07  VOICE-FIRST CLASSROOM (Jim: "back to the conversational back-and-forth").
                (1) VOICE INPUT RESTORED here (session.html got it 2026-08-06): canRecord is
                    a real capability check again (ON for typing courses on browsers with
                    getUserMedia + MediaRecorder; OFF for elementary tap-to-answer + browsers
                    that can't record). Tap 🎙️ -> speak -> audio posts to /api/transcribe
                    (ElevenLabs Scribe; transcribed then discarded -- text only survives).
                (2) REMOVED the ⏸ Pause button and the Yes / No / I'm stuck / 💡 Hint quick
                    replies (HTML, CSS, setPaused/setQuick, `paused` guards) -- the student
                    just SAYS it now. The ✏️ New problem button STAYS (it's navigation).
                (3) 🧮 Math Keyboard retired (see math-keyboard.js): gone from the answer
                    bars AND the problem intake. Typing stays as the fallback everywhere;
                    the 📈 graph tool is unchanged.
    2026-08-04  QUIZZES (build y): NEW [[quiz unit topic name correct total]] tag -> a 'Quiz'
                result card (pass = 80%+, unlocks the next topic) POSTed to /api/quiz. The
                [[check]] card is retitled 'Unit Quiz' and its 'mastered' bar fixed 80 -> 90
                (missed in the build-w sweep).
                Also: the check POST now sends `course` (was mis-filing under Algebra I).
  - 2026-08-26  BUILD od (Jim: "close the keyboard if I choose to do that").
    The answer bar gains a ⌨️✕ close button; the board takes its room back
    (board.js ResizeObserver). Reopen = the Type button where it exists, else a
    small fixed ⌨️ pill (practice/topic retired their link with !important CSS).
  - 2026-08-25  BUILD nr. (1) PAUSE IS PRONOUNCED: the ⏸ button was white-on-white
    and Jim couldn't find it fast ("I should be able to pause it more easily") --
    now solid amber, Type-button sized, solid green while paused. (2) The
    keyboard-eats-the-board scroll fix lives in board.js (one copy, all pages):
    when the answer bar opens and the feed shrinks, the board scrolls ITSELF so
    the question stays on screen -- the student never scrolls to find it.
    2026-08-18  (build ht, Phase 5) THE TURN CANNOT HANG: 90s fetch abort + warm
                try-again bubble (see session.html).
    2026-08-18  (build hs, Phase 5) THE CREDENTIAL LEAVES THE URL: postJSON sends
                X-Student-Code and the quiz/check/mark URLs say /me.
    2026-08-11  BUILD di -- [[column]] gains align="last" (first full audit, finding
                S-9): a DELIBERATELY-WRONG last-digit lineup, amber with a built-in
                "wrong way" badge, so the tutor can SHOW why the misconception fails
                instead of describing it (the audit's student asked to SEE it twice and
                got prose labels). The whole number rides in the integer cell so rows
                right-align on their final digit; a result row is REFUSED in this mode
                (the wrong layout is never completed on our board). Identical change on
                all three teaching pages, byte-for-byte -- ruletests PART 3r compares
                the three showColumn bodies so they can never drift (the build-bk bug
                class). Companion: math-figures.js gained piecewise domains + automatic
                open/closed endpoints in the same build.
  - 2026-08-03  iPAD/TABLET PASS: (1) the type-box font went 15px -> 16px -- iPads auto-zoom
    the whole page when a smaller input is tapped, and it stays zoomed; 16px stops that.
    (2) The full-height layout now also sets 100dvh (kept 100vh for older browsers) so the
    composer can't hide behind Safari's collapsing toolbar on tablets.
  - 2026-08-03  BOARD-PRIMARY: [[objects]] gained add="n" -- draws the first row as
    "⭐⭐⭐⭐⭐ + ⭐" so addition is SEEN, not imagined. Pairs with the new shared "board is the
    lesson, words are the backup" doctrine in tutor.py (all courses, all modes).
  - 2026-08-03  FIRST-WORDS + OBJECTS (Jim's playtest): (1) the FIRST spoken clip of a session now
    requests /api/speak with lead=3 (~1.1s of leading silence instead of ~280ms) -- audio outputs
    close during the quiet thinking wait and eat the head of the first clip; now they eat silence.
    (2) new [[objects emoji="⭐" groups="5"]] board tag draws big countable emoji rows (two rows to
    compare: "5 | 3"), so the elementary tutor can SHOW five stars instead of asking a student to
    imagine them. Count deliberately not printed. Additive only.
  - 2026-08-03  ELEM MODE FOR THE ANSWER BAR (Jim: tour says "just tap" but the bar said "type
    your answer" with Math Keyboard/Graph buttons). For entry/basic a body.elem-mode class now
    hides the 🧮/📈 buttons, the "Two ways to answer" line, and their "?" bubbles (CSS, so
    late-injected buttons are caught too); the input placeholder becomes "Tap an answer button
    — or type here"; and a tap-friendly one-liner sits above the bar. Typing stays as a quiet
    backup. Other courses unchanged.
  - 2026-08-03  SCROLL FIX (Jim: "I have to scroll to see what he's saying"): the tap-to-answer
    buttons shrink the transcript from below, so a ResizeObserver now re-pins the transcript to
    the bottom on any size change, showChoices() re-pins the transcript instead of scrolling the
    page, and clearChoices() re-pins after removal.
  - 2026-08-03  REBRAND (Jim): all visible "MyTutor" text is now "Mr. Cadabra's Classroom" (titles, meta/OG, nav brand, body copy, footers). "Hyperion Shift LLC" remains ONLY on the legal pages (privacy/terms), where the legal entity must be named. Historical change notes untouched.
  - 2026-08-03  BUSY GLOW (Jim: "use the tour's fuzzy border around Mr. Cadabra when he's
    talking or thinking, so I can SEE he's doing something"): new .orbwrap.busyglow class
    (same accent ring + tourpulse animation as the session-page tour, keyframes added here)
    and setState() now toggles it on for "thinking"/"speaking", off otherwise. Purely visual
    and additive.
  - 2026-08-03  TAP-TO-ANSWER CHOICES (elementary courses): new [[choices options="a | b | c"]]
    tag renders big tappable answer buttons above the answer bar, plus an automatic
    "🤔 I'm not sure" button, so young students who can't type or read well can answer by
    tapping. A tap sends the answer exactly like typing it; buttons disable on tap and clear
    at the start of every tutor turn. Typing stays available as a backup. CSS is injected by
    the choices code itself (mtChoicesCSS), so no page styles were touched. Additive only.
  - 2026-08-03  ANALYTICS: added Plausible (privacy-friendly, cookieless) shared include in <head>. Pure add-on; nothing else changed.
    2026-08-01  KEY TERMS BOLD+RED (Jim): **term** from the tutor renders as a red bold
                .kterm span (first-use vocabulary emphasis); asterisks never show raw and
                the voice never reads them (forSpeech already strips them).
    2026-08-01  NO MICROPHONE, EVER: canRecord hard-false (master switch), so the dormant
                tap-to-talk code can never request mic permission. Matches session.html.
    2026-07-30  APP NAV (Jim: back-navigation + Contact on every top bar): included the new shared
                /static/app-nav.js -- labeled pill links (🏠 Home · 🎓 My lesson · 📊 Progress ·
                🔄 Switch course · ✉️ Contact) injected into the top bar, context-aware per page,
                hiding the old obscure link when replaced. Additive; one script tag. Do no harm.
    2026-07-30  Answer-bar placeholder now plainly reads "Type your answer here… (press Enter to
                send)" to match the lesson screen. Do no harm.
    2026-07-30  HELP TIPS (Jim: "?-in-a-circle anywhere someone could get confused"): included the
                new shared /static/help-tips.js, which plants small ? buttons with popup explanations
                next to the answer bar, 🧮 Math Keyboard, 📈 Graph, quick replies (and on the
                dashboard: trophy case + time tile). Additive; one script tag. Do no harm.
    2026-07-30  FRONT-DOOR SWAP (paired with main.py 2026-07-30h-frontdoor): every "kick back to
                login" redirect now targets /login instead of "/" (the marketing landing page took
                over the root URL), and the page gained the site favicon. Do no harm.
    2026-07-30  ENGAGED-TIME TRACKING: included the new shared /static/time-tracker.js, which
                posts /api/heartbeat once a minute ONLY while the tab is visible and the student
                is actually active — so parents get honest time-on-task numbers. Additive; one
                script tag; nothing else touched. Do no harm.
    2026-07-30  MARKET PREP (paired with main.py 2026-07-30f-lockdown): /api/speak and
                /api/transcribe now require the login code, so both call sites pass
                &code=/?code=. Also renamed title to "MyTutor — Practice". Do no harm.
    2026-07-30  UI POLISH. (1) Answer boxes now read "Write your response here, then press Enter…".
                (2) The 🧮 button is renamed "Math Keyboard" (intake hint updated to match) and
                math-keyboard.js now shows a start-of-lesson reminder about it. (3) Left sidebar
                widened ~10% (280px -> 308px). Static-only. Do no harm.
    2026-07-30  ANSWER-BAR CLEANUP (paired with math-keyboard.js). The redundant standalone "Send"
                button (#chatSend) is now hidden by math-keyboard.js ("each tool has its own send").
                The 🧮 opener is relabeled "Math numbers & symbols" (intake hint updated to match),
                and the #chatInput placeholder now reads "Type your reply, then press Enter…". No
                send logic changed here (Enter was already wired). Static-only. Do no harm.
    2026-07-30  INTAKE SCREEN CLEANUP ("what problem are you stuck on?"). Three fixes to the
                problem-entry overlay so it matches the "warm voice out / type in" product:
                (1) REMOVED the "🎙️ Tap and say the problem" microphone button and the "— or —"
                    divider, plus all of the entry recording JS, and removed the getUserMedia()
                    mic warm-up from startPractice() so clicking "Let's work on it" no longer
                    pops a microphone-permission prompt. Students type the problem.
                (2) MATH KEYBOARD ON INTAKE: added a hint line and let the shared math-keyboard.js
                    attach its 🧮 keypad to the entry textarea (#problemInput / #entryGo), so a
                    student can enter √, x², fractions, etc. while typing the problem. (The graph
                    tool stays in the lesson itself, where plotting points is meaningful; the 🧮
                    keyboard AND 📈 graph both remain in the in-lesson answer bar as before.)
                (3) ENLARGED the entry card (max-width 520->660, bigger badge/heading/lead and a
                    larger, more legible textarea) -- it was cramped. Presentation only.
                Static-only change (no backend build required). Do no harm.
    2026-07-28  COSMETIC: adopted the shared "math paper" background (graph-paper grid + faint
                drifting math symbols), declared last in the stylesheet so it supersedes the
                page's original flat wash. Presentation only. Do no harm.
    2026-07-28  COLUMN-MATH VISUAL [[column]]. New whiteboard visual for stacked, place-value /
                decimal-point aligned addition & subtraction (pre-algebra). Fixes the bug where the
                tutor said "line up the decimal points" but the board showed the numbers centered and
                NOT lined up. [[column op="+" terms="2.40 | 1.35" result="3.75" caption="..."]] stacks
                the numbers so the decimal points sit in one vertical line, draws the operator + rule
                line, and shows the result ONLY when the tutor supplies it (never runs ahead). Added
                .colmath CSS + splitNum/colOp/showColumn + a handleTags "column" case. Same visual in
                session.html and topic.html. Static-only (no backend build change).
    2026-07-25  NAV BUTTONS + TYPE-UNDER-THE-BOARD. Left sidebar gained a <nav class="leftnav">
                (My course / Explore a topic / Progress dashboard, hrefs set from CODE), and a
                persistent .feedbar (chatInput + chatSend) now sits UNDER the whiteboard, always
                visible, posting through the same sendToTutor path (guarded by `busy`). Retired
                the sidebar "Type instead" link via #typeToggle{display:none}. New CSS:
                .leftnav/.navbtn/.feedbar. (Same day as the student-led + Hint change below.)
    2026-07-25  STUDENT-LED PRACTICE + HINT BUTTON. Practice is now driven by the student:
                Mr. Cadabra boards the problem, asks "what do you want to do first?", then
                carries out each move the student names on the whiteboard (the behavior lives
                in the backend PRACTICE prompt in tutor.py). Front-end change here: a new
                "💡 Hint" quick button sits in the controls row beside Yes / No / I'm stuck.
                It sends "Can I have a hint?" through the same sendToTutor path, so the tutor
                replies with a small nudge (never the whole step). setQuick() + the quick-button
                click wiring now include ".quick.hintbtn" so it enables/disables with the others
                and only fires when it's the student's turn. No other logic changed.
    2026-07-22  FUNCTION MACHINE + VARIABLES POP. (1) New [[machine input="3"
                rule="2x+1" output="7" fname="f"]] visual: showMachine() draws
                input -> rule box -> output, with the worked line "2 × 3 + 1 = 7" and
                "f(3) = 7". Used for FUNCTIONS instead of the balance/monkeys (the
                balance stays for equations). handleTags gains a "machine" case.
                (2) styleVars(): every algebra variable now renders BOLD, CAPITAL, and
                RED (.mvar) in BOTH the chat bubbles and the visuals. A variable = a
                lone letter; ordinary words, "a"/"I", and function names f/g/h are left
                alone. addBubble now uses innerHTML=styleVars(text) (HTML-escaped first).
    2026-07-21  New PRACTICE page ("bring your own problem"). A student who is stuck
                on a specific problem from school types OR says it, then Mr. Cadabra
                coaches them through THAT problem -- same voice orb, tap-to-talk,
                whiteboard visuals ([[balance]]/[[card]]), and quick buttons as the
                lesson, but talking to POST /api/practice (any Algebra I topic;
                foundation-first; not tied to the curriculum/placement). Practice history is
                held here in the browser and posted each turn -- nothing is saved.
                Reuses the proven speak()/tap-to-talk code from session.html,
                including the stall WATCHDOG and the control-tag leak guard.
```

I did no harm and this file is not truncated.

# CHANGELOG -- session.html  (notes rolled out of the file's header)

Moved out of `static/session.html` on 2026-09-08 (build ui): every CHANGE NOTE dated before 2026-09-01 -- 125 entries, VERBATIM, in the order they sat in the file (newest first). The 17 notes from 2026-09-01 on stay at the top of `static/session.html` itself, and new notes keep going there. Nothing below was edited; grep this file for a build letter or a date. When the header is rolled out again, the newer block is added ABOVE this one.

```text
    (rd) 2026-08-31 -- THE MAIN ROAD MOVES THE STAR. The scripted lane grades every
    tap in code and never emits [[mark]], so the qz chips sat still through a whole
    scripted lesson. /api/script/answer now returns a "streak" field (the server's
    fresh pair, bumped on a right answer, reset on any wrong tap -- Jim's ruling) and
    scrAnswer feeds it straight into renderStreakChips. One line here; the grading
    lives server-side in main.py where the engine's own verdict is.
    (rc) 2026-08-31 -- THE STAR FALLS WHEN THE CHILD SLIPS. New [[miss]] tag handled
    beside [[mark]] in handleTags: a wrong tap on the still-going problem posts
    {miss:1} to /api/mark/me and the SERVER's fresh numbers feed renderStreakChips, so
    the child watches the star drop to 0 the moment they slip (Jim's ruling: a miss is
    ANY wrong tap). No counters move -- a slip is not a finished problem. The code
    floor (server-side computed grading of bare answers) lives in main.py/tutor.py.
    (rb) 2026-08-31 -- THE CHIP SAYS WHAT IT COUNTS. Jim, reading the qz chips live:
    "I see the icon for days in a row, the icon for problems in a row, and I only know
    that's what they are because I told you to put in there. There's nothing that says
    what those are." The qz pills explained themselves only in hover tooltips -- a child
    never hovers and a tablet can't. Each pill now carries a small visible label under
    its number, in EXACTLY the dashboard banner's own words ("days in a row" / "right in
    a row today") so the two surfaces never teach two names for one thing. The pills stay
    compact (this page's more-board-less-chrome rule): the label rides INSIDE the
    existing pill as a second 9px line, no new topbar row, ids and the render/bump
    wiring untouched (PART 3ha's pins all still hold; PART 3hc pins the labels).
    (qz) 2026-08-31 -- A STREAK A CHILD CAN SEE TODAY. Jim: "something on the top that
    says how many days in a row they've worked and how many problems in a row they have
    gotten correct today... prominent, so easily visible... a motivator to keep coming
    back every day." Requested on both the classroom page (this file) AND the dashboard
    (dashboard.html). This page has an established design rule of minimizing chrome to
    keep the lesson board as tall as possible (see .chiprow's own comment below), so the
    classroom version is a compact pair of pill chips in the topbar (#streakChips) --
    not the larger banner dashboard.html got, which has no such space constraint.
    Seeded at page load from SRV_PROGRESS.stats (server's /api/session response, no
    extra request), then kept live: postJSON now RETURNS the parsed response instead of
    firing and forgetting, so every [[mark]] tag's own /api/mark call feeds its fresh,
    authoritative today_streak/streak_days straight into renderStreakChips() --
    COMPUTED, NEVER GUESSED, never a client-side optimistic count. A chip only plays its
    "bump" pulse animation when its OWN number actually changed from the last render, so
    a page-load paint or an unrelated re-render never fires it. Today's correct-in-a-row
    count resets to 0 the instant a problem is missed and restarts at 0 every new day --
    driven by store.py's today_streak/today_streak_day columns (see store.py's own note
    for the full write/read design); the day streak beside it is the same one already
    tracked, just made visible here too.
    (qr) 2026-08-30 -- THE AUTHORED QUESTION SHIPS ITS BUTTONS. Jim, on a live
    Entry-Level lesson: "these are all supposed to be bubble answers, not tap to
    talk ... it's in a couple of these, but it's not on all of them." Measured
    before anything was touched: the SERVER was never at fault. choices_for() in
    lessonscripts.py builds a [[choices]] tag for EVERY scripted question with no
    condition on it, and main.py's _script_clean() sends it here as step.choices --
    a field of its OWN, beside step.board. scrPlay() rendered step.board and nothing
    else, and the string "step.choices" did not appear in this file at all. So every
    AUTHORED question in Entry-Level and Basic reached the child with no buttons,
    while an `ai` intervention had them (its tags ride inside board). That split is
    exactly the "couple of these" he saw. pilot.html has read step.choices since
    build ou; the pb port into this page dropped it -- and dropped step.tap_only
    with it, so the engine's "stop asking this child to talk" was never heard
    either. Both restored. Three further consequences handled in the same edit: a
    board that ALREADY carries a choices tag is never rendered twice; a beat with no
    taps of its own clears any row still on screen; and the one `say` beat that
    carries taps (LINE_TAP, after an unheard answer inside an intervention) now sets
    SCR.pending, so its buttons reach /api/script/answer instead of the live tutor --
    the same defect qd fixed one beat kind over. PART 3gu.
    (qd) 2026-08-29 -- AN AI INTERVENTION IS AN ASK. scrPlay set SCR.pending only for
    kind "ask"; an "ai" step (the Model-Lead-Test turn after a wrong answer) left it
    false, so the child's redo was sent to the live tutor with stale history. Now
    "ai" counts as an ask, as pilot.html has done since ou. From Jim's screenshot.
    (pd) 2026-08-27 -- LET THE LESSON BREATHE. Jim, on a live Algebra II scripted
    lesson: "This is the worst lesson I have seen so far. There was no pause at any
    time. pictures showed up and disappeared." He was right, and it was mine. Build
    pb ported the scripted player into this page and DROPPED ALL THREE of the
    protections pilot.html had grown over builds ka/kd/ke to solve this exact
    problem. pb's advance was one line -- `else scrNext();` -- which starts the next
    beat the instant speak() RESOLVES. If a clip is missing, blocked by autoplay, or
    errors, speak() resolves almost immediately and the ENTIRE LESSON DUMPS AT ONCE:
    four bubbles and three number lines land together, and oz's supersede-the-older-
    work chip swallows the first pictures on the way past. That is the whole of
    "no pause" AND "pictures showed up and disappeared" -- one bug, two symptoms.
    THE PROTECTIONS, RESTORED (all three already existed in this codebase):
    (1) A READING FLOOR. Promise.all([ speak(words), delay(readMs(words)) ]) -- the
        beat cannot end faster than a child can read the line even when there is no
        audio at all. This page's own TOUR has done exactly this since build bj, and
        readMs's comment already said why: "so the tour stays readable even if the
        voice is unavailable and speak() returns instantly". The scripted lane simply
        never got it. ONE definition, shared -- not a second copy.
    (2) A BREATH between beats: SCR_BREATH (650ms), the number pilot.html settled on.
    (3) SILENCE PACES ITSELF. voice.js calls setState("speaking") the moment audio
        genuinely begins; a beat that never heard it shows a "Next" button and WAITS
        for the child instead of running on a timer. pilot.html's law, verbatim: "a
        reader paces themselves, and racing them would be a worse defect than the
        stall was." A beat that DID speak still auto-advances, so a working session
        never asks the child to tap.
    ⚠️ THE LESSON UNDERNEATH: voice.js's header records four hand-ports of the audio
    layer that each lost a different protection, and script-board.js's header records
    why the board became a file instead of a copy. pb hand-ported the PLAYER and lost
    three at once. When a lane's behaviour has been tuned by playtesting, port the
    tuning with the code or do not port the code.
    NOT fast-forward (build oc): there is no skip button while he is talking. The
    Next button appears only when nothing was heard.
    (pc) 2026-08-27 -- THE FIGURE FILLS THE BOARD. Jim, looking at a live Algebra II
    absolute-value beat whose number line was a ribbon in the corner: "Why is it so
    hard to make a big number line". It was not hard. It was MEASURED WRONG, three
    builds running. .feed .mblock is a flex COLUMN with align-items:center, which
    sizes every child to its own content. A figure block (.mfig) has exactly one
    child: an <svg> whose CSS width is a PERCENTAGE. Percentages contribute nothing
    to intrinsic sizing, so the browser fell back to the CSS default width for a
    replaced element -- 300px -- and then applied max-width to a box that was already
    300px wide. EVERY figure on this board rendered at 300px, on every screen, no
    matter how much room the board had. The three builds that answered "make it
    bigger" by raising the display cap (je 660, nw 1100, ox 1500) raised a ceiling
    the floor could never reach. ONE LINE FIXES IT: .feed .mfig { align-self:
    stretch } opts the figure out of the centering, so width:100% finally has a real
    box to resolve against. MEASURED, NOT REASONED (the oz lesson): at a 1512px
    window the number line goes 300px -> 945px; at 1920px, 300px -> 1222px. The same
    line also delivers, at last, what ol's bar-chart cap and every other raised cap
    were always for.
    DO NO HARM: the rule touches .mfig only. .worklist, .colmath, .solveboard,
    .writeboard, .machine and .scale keep their own max-widths and stay centered by
    .mblock's align-items:center, which is unchanged.
    (os) 2026-08-27 -- THE BOARD READS ONE, TWO, THREE. NEW [[stepcard n="1"
    title="..."]] tag dispatched here (labeled Step-N cards side by side, following
    blocks land inside the open card); clearStepGrid() at turn start. Machinery and
    the full story live in board.js's own change note.
    (or) 2026-08-27 -- THE PAGE GETS SIMPLE. Jim: "the sidebar ... taken up a whole lot
    of screen place. What I'd like is for the sidebar to be collapsible... when you start
    up ... the sidebar is collapsed, and there is a tab that says open the sidebar. The
    pause, type my answer and speak buttons should be moved to the bottom or someplace
    where they maybe don't take up a lot of space... my goal is to make the page very
    simple." (He considered folding the top progress chips too, then retracted: "let's
    leave that alone" -- iq's chips are untouched.) DESKTOP (>900px) ONLY:
    (1) The left sidebar starts COLLAPSED (grid column 0, display:none) with a fixed
        edge tab #sbTab ("Open the sidebar" / "Close the sidebar") that toggles a
        body.sbopen class; the student's choice is remembered for the visit
        (sessionStorage mt_sb_open), and every startup is collapsed again by design.
    (2) Mr. Cadabra's face (.tutor-head) and ALL the controls (mic, Pause, Type my
        answer, hint, live) move to a compact horizontal strip -- .ctrlbar / #ctrlBar --
        at the BOTTOM of the board column, under the answer bar. The move is a JS
        reparent (placeCtrls): same elements, same ids, so mic.js / voice / keyboard
        hooks attach unchanged; on phones (<=900px) the SAME nodes move back into the
        sidebar, so build dz's bottom dock is byte-identical in behavior.
    (3) The opening TOUR opens the sidebar for its walk-through (its stops glow sidebar
        buttons) and tucks it away again at the end -- the iq pbars pattern. A
        model-driven [[highlight]] whose target lives in the collapsed sidebar opens it
        first and leaves it open (the student can close it with the tab).
    DO NO HARM: nr's amber pause law (its CSS block untouched, overrides only), od's
    keyboard close, iq's chips, ir/ns scroll anchoring, dz's phone dock all stand.
    (oj) 2026-08-26 -- SIDE BY SIDE ON PURPOSE. Jim: "the whiteboard is underutilized...
    the bubble only goes about seventy or eighty percent across... they can move to the
    side -- we're gonna put the other equation right next to this one so you could see it
    better." Two changes: (1) .feed .bubble max-width 80% -> 96%; (2) NEW [[beside]] tag
    dispatched here -- the next board block joins the previous one in a .mrow (CSS added
    by .mblock; flex-wrap so phones stack the columns). getWorklist/feedBlock now mount
    blocks through board.js mountBlock (the one door); clearBeside() at turn start so a
    dangling tag never leaks. Machinery + full story in board.js's own change note.
    (iq) 2026-08-19 -- THE BOARD GETS ITS ROOM BACK. Jim, in Differential Equations: "today's
    goals and the bars up top ... need to be collapsed into two smaller things that you could
    click on ... gives us more room for the board." The goal banner and the three-bar block
    no longer sit open above the whiteboard. Two small chips -- "🎯 Today's Goal" and
    "📊 Today's Progress" -- appear once there is content behind them; a click pops the panel
    open, another click tucks it away. DO-NO-HARM SHAPE: #goalBar and #pbars are the SAME
    elements and every render path (showGoal, showToday, renderTodayBar, renderUnitBar,
    renderCourseBar, showBarsPreview, the [[todaydone]] ticks, the il worked segments) is
    untouched -- a new .open class simply gates visibility on top of .show. The progress chip
    carries a live "n/m" goals count; both chips pulse once when something changes behind a
    CLOSED panel, so a tick is never invisible. THE TOUR STILL SHOWS REAL BARS: runTour pops
    the progress panel open for the whole walk-through (build bj's three-maps ruling holds
    DURING the tour) and tucks it back at the end; a model-driven [[highlight id="bars"]]
    outside the tour opens it for the glow and the next turn's clearHighlight closes it
    again unless the student had opened it themselves (the curriculum-stop pattern). The
    tour's "bars" line now tells the student where the bars live afterward.
    COMPANION, same sitting (build ir, in board.js): every new tutor bubble is placed at the
    TOP of the visible board -- history is above (scroll up), his work fills in below.

    (gs) 2026-08-17 -- THE RAIL FOLLOWS THE TEACHING. Jim, twice: "it still says unit one on
    the top when we are talking about unit five." The unit bar was seeded from
    placement.start_unit -- where the student was PLACED, a number that never moves -- so a
    lesson that had walked on to right triangles sat under a rail insisting on Unit 1, and
    nothing reconciled the two. The server now reports progress.current_unit (the most
    recently taught unit, filed from the tutor's own [[unitplan]] rather than from
    placement) and this page prefers it. Order of authority, unchanged at the top: the focus
    unit the STUDENT clicked, then where the teaching actually is, then where they were placed.

    (gr) 2026-08-17 -- THE SPOKEN LETTER. Jim was asked which side was the hypotenuse, said
    the letter "c" out loud, and ElevenLabs transcribed it as the Spanish "si" / "CSI" --
    whereupon the tutor told him he was wrong and demanded a letter. A student marked
    incorrect for a machine's mistake. /api/transcribe now sends a language hint and owns a
    spoken-letter map ("see"/"sea"/"si"/"CSI" -> c); this page supplies the CONTEXT via
    expectsALetter(lastTutorText), so the rewrite happens only when the tutor actually asked
    for a letter and a "see" in ordinary speech is never touched. Deliberately excluded from
    the map: oh, eye/I, you, are, why -- each is a plausible whole utterance from a child,
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
    (ge) 2026-08-14 -- THE OPENER FOLDS TOO, AND ONE BOARD LINE STOPPED LYING. Jim, live in
    Geometry unit 1: (1) "the introduction didn't collapse" -- the welcome and the goals card
    stayed on screen through the lesson, because the fold only ever triggered on a FINISHED
    problem and an opener never finishes one. wipeBoard() gains an optional label, and
    foldOpenerOnce() folds the opener under "Today's plan" the first time real board work
    starts. It cannot swallow the current turn, and it is silent when there is nothing to
    fold. (2) The companion fix is in foundations.py (build ge): the "point" script's board
    line was TEXT reading "A B C", which styleVars then coloured like algebra variables --
    so when the tutor said "look at those three points on the board" there were none. It now
    draws three real dots.
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
    (ey) 2026-08-13 -- THE VOICE SEQUENCING. Mr. Cadabra's talking clips now play at the
    seven moments of a real lesson, and the rule the whole design hangs on is enforced
    here: A CANNED CLIP AND HIS LIVE VOICE NEVER TALK AT ONCE, AND A CLIP NEVER REPLACES
    THE PERSONALISED LINE. Video cannot say a child's name; the live voice can, so a clip
    is an ARRIVAL, never a substitute.
    HOW: tutor-moments.js is included (NOT deferred -- window.TutorMoments must exist when
    this script runs; the landing page paid for that lesson once already). A MOMENTS table
    declares, per moment, WHEN it plays (before his words, or after -- the goodbye goes
    last), its CADENCE, and its RANK. handleTags() QUEUES at most one moment while the
    reply renders, and runTutor plays it at exactly one gate:
        await runPendingMoment("before");   // the celebration lands...
        await speak(clean);                 // ...then he says what THEY did, by name
        await runPendingMoment("after");    // ...and the send-off goes last
    Those three lines ARE the voice rule. Both gates are awaited, so his live voice cannot
    start until a clip has finished, and speak() is unconditional so a clip can never
    replace the personalised line. ruletests PART 3ac pins the order structurally.
    THE SEVEN: first_meeting / welcome_back (from the welcome-card CLICK -- a real user
    gesture, which is what a clip with SOUND needs to autoplay; a student who clicked a
    SPECIFIC door, a final exam or a quiz retake, is never met with a hello), quiz_passed
    (showQuiz), unit_gold (showCheck), course_champion (showFinalExam), sprint_best
    (sprFinish -- where sprSay must WAIT for the clip rather than talk over it), and
    goodbye (the NEW [[bye]] tag: the first mechanical end-of-session signal this app has
    ever had; detecting a farewell by reading his prose would misfire on "see you next
    Tuesday").
    CADENCE, a judgement call worth stating out loud: a clip that plays too often stops
    being a person and becomes a jingle. Rare EARNED moments always play (a mastered unit,
    a finished course, the first hello); moments that can repeat several times in an
    afternoon are capped at ONE A DAY (localStorage, per student, with an in-page fallback
    for private mode). To retune, change the table -- nothing else reads it.
    SHIPS DARK: six of the seven clips do not exist yet. With no matching clip in
    moments.json, available() is false, queueMoment never queues, both gates resolve
    instantly, and this page behaves exactly as it did before. The day Jim's recordings
    land, the same code lights up -- no flag, no coordination.
    PROVEN IN A BROWSER, not asserted: driving the real page with a stand-in clip, the
    clip ended at 4867ms and his voice started at 4867ms -- zero overlap; with the await
    deliberately removed, his voice started at 1807ms against a clip running to 4938ms,
    i.e. 3.1 seconds of two Mr. Cadabras talking at once. The dark path was measured too:
    no moment video, voice unchanged, zero page errors.
    (ew) 2026-08-13 -- THE FINAL EXAM COUNT IS THE SERVER'S, NOT A LITERAL 9.
    renderCourseBar() and openFinalOverlay() hard-coded ">= 9" / "of 9" / "All nine
    units" / "18 questions". The server has always sent final.required and now DERIVES
    it from the course's real unit list (main.py build ew) -- these two functions read
    it (fallback 9 only if the server field is missing). The real gate stays
    server-side; this page's numbers just stop pretending to know them. The 1..9 unit
    map loop is untouched: it draws THIS page's course map from its own CURRICULUM
    list, which is a different (page-content) concern.
    (ee) 2026-08-12 -- THE BOARD SPOTLIGHT (teaching upgrade, rule 60 / signaling).
    The [[highlight]] tag could only glow page furniture (tour stops: buttons, bars,
    panels) -- never the one place a student's eyes matter most while teaching: the
    board. Now two board keys work everywhere the tutor teaches:
      [[highlight id="line"]]  -> the NEWEST line of board work glows for ~6 seconds
      [[highlight id="board"]] -> the whole board glows
    Implementation: spotlightBoard() runs FIRST in the tag dispatcher; page-tour ids
    still fall through to highlightEl() unchanged. The glow is a CUE, not a state --
    it self-clears on a timer, a new spotlight replaces the old, and the start of the
    next tutor turn clears it too (clearHighlight). Styling is .stepglow, a calmer
    cousin of .tourglow (no bouncing "look here" tag -- the tutor's words do that
    job); the global prefers-reduced-motion rule (dz) stills its pulse automatically.
    Same-build: practice.html + topic.html gain the same two keys; prompts.py rule 60
    teaches when to use it (at most one per reply; words still say the where).

    (dz) 2026-08-11 -- ACCESSIBILITY + PHONE PASS (Four-Lens student items 5 and 8).
    A voice-first tutor should be the accessible one, and it wasn't: ONE aria attribute
    on the whole page. Now: the transcription readout and the your-turn hint are polite
    live regions (a screen reader hears what the mic heard and whose turn it is); the
    mic button has a spoken name; the tutor orb is marked decorative; the four overlays
    (welcome, sprint, assessment invite, final exam) are real dialogs and the welcome
    focuses its action button; prefers-reduced-motion stills every pulse and bounce.
    PHONES: the board comes FIRST -- the old stack put the whole left rail above it, so
    a student scrolled past orb+nav+mic to see the math. The rail is now a compact DOCK
    stuck to the bottom (orb+status in one row, nav as a horizontal chip strip, mic and
    answer box always in reach). Desktop layout untouched; all inside the 900px query.
    (dw) 2026-08-11 -- THREE BARS, ALWAYS (Jim live: "it's only showing two bars
    regardless of who I sign in as"). Root cause: on welcome-back sessions the tutor
    often announces no goals, ensure_today_tag can only mirror goals that WERE
    announced, and yesterday's stored goals rightly don't rebuild today's bar -- so
    the TODAY row simply never appeared. Two fixes: (1) here, when the server has no
    today-goals, the TODAY row shows its labeled placeholder from the first second
    (real [[today]] replaces it -- same render path as the tour preview); (2) in
    main.py, when the server sees the bar is empty it hands the opener a per-turn
    ORDER to state today's 2-3 item plan and emit [[today items]]. Same build: the
    opener also learns the GAP since the last session -- a day or more away earns a
    real 3-4 sentence refresher (what unit, what you were doing, what they'd nailed,
    one memory-jog question), never a bare "ready to keep going?" (Jim's other catch).
    (dv) 2026-08-11 -- THE BUZZER-BEATER SHIELD (Jim's own catch, live). He answered a
    sprint's last question exactly as time ran out; the timer swapped the panel and his
    click landed on "Start my lesson ▶" -- which sits where the answer buttons were --
    and the whole A/B celebration vanished unseen. Fix: sprShow(panel, shieldMs) -- any
    panel the TIMER swaps in (the stretch break and the results) keeps its buttons
    inert and visibly dimmed for 1.2 seconds, so a late click cannot dismiss what the
    student needs to see. Panels reached by deliberate taps are unshielded.
    (du) 2026-08-11 -- THE RETAKE DOOR. Arriving with &unit=N&quiz=1 (the dashboard's
    new "Retake the Unit Quiz" button) works like FINAL_MODE: no tour, no side offers;
    the welcome button reads "📝 Take the Unit Quiz ▶" and kicks off with the NEW
    "__unit_quiz__" sentinel -- main.py turns it into marching orders (administer the
    focus unit's quiz now; the record keeps their BEST score, so a retake can only
    help). The student clicked a very specific door; we open exactly that door.
    (dt) 2026-08-11 -- MISSED PROBLEMS ARE REMEMBERED (rule 55, Four-Lens student item
    1). The [[quiz]] / [[check]] / [[finalexam]] tags may now carry
    missed="question => their answer | ..." -- parseMissed() turns it into [{q, a}]
    (clamped here AND server-side) and the existing score POSTs carry it along to
    /api/quiz | /api/check | /api/final. Nothing renders differently on this page:
    the misses surface on the dashboard's new review card and in the tutor's next-
    session mastery notes. A tag without missed= behaves exactly as before.
    (ds) 2026-08-11 -- SPRINT ON REQUEST. Arriving with &sprint=1 (the dashboard card's
    new "Run one now" button) starts the fluency sprint directly for the current/focus
    unit. The once-a-day rule still tames the unprompted lesson-open OFFER; an explicit
    request is always honoured. Fails soft: no sprint for the unit -> the lesson simply
    proceeds.
    (dr) 2026-08-11 -- THE YOUNGEST STUDENTS GET A VOICE (Jim: "I think it's okay for the
    youngest to have a way to talk as well"). canRecord's !IS_ELEM clause removed: entry/
    basic students -- the ones least able to type, in a voice-first classroom -- now get
    the same tap-to-talk microphone as everyone else. The tap answer buttons stay exactly
    as they were (tap, talk, and type are all first-class); the ready-hint, welcome tip,
    and the tour's final stop all teach both paths; the browser still asks for the mic
    only when the student actually taps 🎙️. The teaching brain's how-they-answer note
    (prompts.py) now tells the tutor elementary students may speak, and to read young
    readers' transcriptions with EXTRA charity. Same change on practice.html/topic.html.
    (de) 2026-08-10 -- DIFFEQ RESTRUCTURED TO THE CUPM MAINSTREAM SYLLABUS. Jim: "go with
    the one that you feel will be most acceptable to most schools." The CURRICULUM_BY_COURSE
    diffeq block now matches curriculum.py/pedagogy.py exactly: slope fields join unit 1,
    separable + linear merge into unit 2 (exact equations kept as one brief topic), NEW
    unit 3 qualitative analysis (phase line, stability), NEW unit 4 numerical methods
    (Euler, Runge-Kutta), nonhomogeneous + vibrations merge into unit 6, and systems get
    two full units (8 linear/phase plane, 9 nonlinear/linearization). Series solutions
    dropped -- the CUPM ODE study found most mainstream courses have moved them out in
    favor of qualitative + numerical work. Unit names here MUST stay byte-identical to
    pedagogy.COURSE_PEDAGOGY["diffeq"]["unit_names"] -- ruletests checks the parity.
    (dd) 2026-08-11 -- FLUENCY SPRINTS. WWC guide 26 rec 6 (Strong): one optional link on
    the welcome card ("totally optional" is in the copy on purpose), a full-screen
    overlay reusing .welcome-card (so the cv short-screen sizing applies for free), two
    60-second tap rounds with a stretch break, and the ONLY celebrated number is B minus
    A -- the student against the student. Skipping costs one tap, a low count changes
    nothing, and nothing anywhere is gated on a sprint. Spoken lines ride /api/speak
    (cached by text, fire-and-forget -- a sprint must work silent). Measured with the
    offer present: the welcome card still fits its box at 1366x768.
  - (cv) 2026-08-10 -- THE WELCOME CARD MUST NOT NEED SCROLLING. Jim: "the Welcome back
    page should never require scrolling. I had to scroll down to see what was my option."
    Two faults, and the second was worse than the one he hit.
    (1) The RETURNING card still carried the FIRST-TIMER'S three how-it-works bullets --
    speakers on, how to answer, where the plan lives -- about 255px of onboarding a
    returning student has already read. Add the badge, heading, lead, TWO buttons and the
    assessment link and it ran past 700px, so .welcome-card's own max-height:92vh +
    overflow-y:auto quietly turned the second option into something you had to scroll to
    find. A choice you cannot see is not a choice you have. The speakers reminder is the
    one bullet worth keeping on a return visit (a student on a new machine has no sound),
    so it stays, compressed to one line; the other two go.
    (2) Fixing that showed the NEW-STUDENT card overflowing too -- 892px of content on a
    768px-tall laptop -- so a brand-new student's very first screen hid the course
    assessment offer below the card's own scroll. The sizes were chosen on a big display
    and never re-checked on the panel most people own. A @media (max-height:900px) block
    now gives short screens a shorter card: same words, same order, nothing removed.
    Measured in a real browser at 1366x768, 1280x800, 1512x850 and 1024x768 by
    _cv_welcome_check.py, which fails if any choice lands below the fold.

    (cg) 2026-08-09 -- THE TODAY BAR NOW SURVIVES A RELOAD. Jim: "there's only two of the
    three tracking bars across the top. I don't know why it keeps disappearing." UNIT and
    COURSE are rebuilt at load from the server's mastery data; TODAY had no server side at
    all -- it lived only in browser memory from one [[today items]] tag. It is now saved
    server-side as the tutor writes it and rebuilt here from SRV_PROGRESS.today, exactly
    like the other two. A later [[today]] still replaces it (same render path).
    (cf) 2026-08-09 -- [[write]] lines are now fitted too. fitRow() has shrunk oversized
    [[step]] lines since build bu, but a long [[write]] line went through eqRow() with no
    fit at all, so with nowrap cells it simply overflowed. Both paths are fitted now, on
    all three teaching pages (ruletests.py PART 3e proves it).
    2026-08-04  QUIZZES (build y): NEW [[quiz unit topic name correct total]] tag -> a 'Quiz'
                result card (pass = 80%+, unlocks the next topic) POSTed to /api/quiz. The
                [[check]] card is retitled 'Unit Quiz' and its 'mastered' bar fixed 80 -> 90
                (missed in the build-w sweep).
    (qm) 2026-08-30 -- THE PANEL SAYS WHAT IT MEANS. Jim, live in Geometry: three bars
    (Today / Unit / Course) and "it's not clear to me what these mean ... maybe we just
    have today's goal, and then progress on unit one and progress on the course." The
    TODAY bar is hidden: alone among the three it measured something the tutor has to
    remember to emit ([[todaydone]]), so it was the one that sat at zero and taught him
    to distrust the other two. Today now leads in WORDS; the chip reads "📊 Progress"
    and carries the UNIT's count.
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
    2026-08-19  (build in) THE GLOW IS THE POINTER, NEVER THE GEOMETRY. Jim on a
                phone: the sidebar stacks below the chat, so the tour's "over on
                the left" pointed at nothing. All layout-directional tour language
                ("on the left", "right below it", "right under it", "up here in
                the corner") replaced with glow-anchored wording -- the highlight
                already moves BEFORE each line, so the glow is the true pointer on
                every screen size. The welcome card's "on the left" -> "in the
                sidebar". (demo.html's tour has the same phrases but those are
                PRE-RENDERED voice clips -- queued separately; changing them means
                re-rendering audio.) Battery pin added in PART 3cb.
    2026-08-18  (build il) THE TODAY BAR MAKES REAL CALLS. Jim's ruling: today =
                progress AND honest work-time. [[todaydone]] may now carry
                kind="worked" (a tick the SERVER earned from ~15 engaged minutes on
                the time clock, vs a completed result); markTodayDone upgrades
                worked->completed and never downgrades; renderTodayBar draws worked
                segments with the new .pbseg.worked look (softer fill, dashed edge)
                and per-segment tooltips; the server restore path applies the new
                worked list from SRV_PROGRESS.today.
    2026-08-18  (build ik) THE TOUR RUNS ONCE, AND IT CAN BE SKIPPED. Jim's live
                catch: tour -> placement -> return, and the whole introduction
                played again ("toured" was inferred from lesson history, which the
                tour never writes -- the server now RECORDS __tour_done__ in the
                new tours_seen table and ORs it into /api/session's toured flag).
                This file's half: a "Skip the intro" button, visible only during
                the tour; skipping races the current line (stopAllSpeech + a skip
                promise), then hands off through the SAME __tour_done__ /
                __tour_done_declined__ path -- so a skipped tour is a SEEN tour,
                and the assessment invitation is never lost.
    2026-08-18  (build ht, Phase 5) THE TURN CANNOT HANG: the chat fetch carries a 90s
                abort over the server's new ~60s upstream timeout; a timeout lands as
                a warm try-again BUBBLE (the old status-line error was cleared by
                finally before anyone saw it).
    2026-08-18  (build hs, Phase 5) THE CREDENTIAL LEAVES THE URL: sprint/session/
                final/quiz/check/mark calls send X-Student-Code with /me paths; the
                sprint narrator uses the speak-prep ticket (see voice.js). Page-nav
                links (?code=) unchanged -- a parked product decision.
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
  - 2026-08-09  FIRST-WORD FIX, PROPERLY (build cb). Leading silence only helps if the
    OUTPUT DEVICE is awake — Bluetooth/laptop codecs sleep after a few seconds of quiet
    and swallow the first 200-400ms. A truly silent WAV now LOOPS while the lesson is
    open (paused when the tab hides) so the route never sleeps, and the lead is DYNAMIC:
    full pad after a real pause, short pad back-to-back. Same on all three pages.
  - 2026-08-09  PROACTIVE AUDIT, CLIENT HALF (build bu). (1) forSpeech(): negative
    VALUES speak as "negative" (the OPERATION stays "minus" — and the board's Unicode
    minus now converts too, a pre-existing gap the new ruletests.py battery caught),
    plus percents, ratios, common fractions, mixed numbers, and thousands separators.
    (2) Board lines NEVER wrap mid-equation any more: .wrow cells are nowrap and the
    new fitRow() shrinks an oversized line until it fits (Jim's "dimes: 7 + 8 + = 16 /
    1(carried)" break — a wrapped equation reads as a DIFFERENT equation). Same
    forSpeech patch on practice + topic.
  - 2026-08-08  UNIT BAR RENDERS AT LOAD (build br, Jim: a resumed session showed only
    the course bar). The unit bar's ladder is already known at page load (curriculum
    topics + placement/focus unit + server quiz history), so loadSession now renders it
    immediately, exactly like the course bar — no dependency on the tutor's [[unitplan]]
    tag (which still replaces it via the same render path when emitted). The TODAY bar
    stays model-fed; tutor.py (same build) now requires [[today]] in the first message
    of EVERY session, resumed ones included.
  - 2026-08-08  MONEY SPEECH (build bp, Jim: "$1.85" was spoken "one dot eight five").
    forSpeech() now reads money as money ($1.85 -> "1 dollar and 85 cents", $0.85 ->
    "85 cents", $2 -> "2 dollars") and plain decimals with "point" spoken digit by
    digit (3.75 -> "3 point 7 5") — never "dot". Same patch on practice + topic;
    tutor.py also tells the model to SPEAK prices as dollars-and-cents.
  - 2026-08-08  BARS: JIM'S PALETTE (build bm). Light-GREEN card, WHITE unfilled
    segments, BLACK labels/text — replaces bj's dark-gray card. Fills stay accent
    purple / gold. Companion in tutor.py (same build): rule 15 sharpened — the
    "your turn" problem must be WRITTEN on the board in the same reply it's asked
    (live catch: "what's ten minus two times three?" was voice-only).
  - 2026-08-08  FIRST WORDS + THINKING FLAG (build bl, Jim; same patch on all three
    teaching pages). (1) "He doesn't start out loud until about the third word" — two
    head-of-clip protections in speak(): every clip now requests lead=1 (~560ms leading
    silence; first clip keeps lead=3) so a sleeping output device wakes on silence, not
    words; and a suspended Web-Audio context is RESUMED before the clip starts (300ms
    cap so a stuck resume can't hold the turn). (2) "Mr. Cadabra is thinking" only lived
    in the tiny corner status — a red pulsing badge (.thinkflag) now appears mid-
    whiteboard while he thinks and vanishes the instant his voice starts (setState is
    the single switch; guards added so a failed turn/transcription never strands it).
  - 2026-08-07  × IS NOT A VARIABLE (build bk, Jim's screenshot: "3 + 2 X 4" showed the
    times sign styled as a red variable X). styleVarsCore now renders a lone x written
    BETWEEN two numbers ("3 + 2 x 4", "5 x 3", "(3+1) x (2+5)") as a true × sign,
    unstyled — both immediate neighbors must be spaces and the nearest non-space chars
    number-ish, so "2x + 3" (coefficient) and "3 + x" (real variable) are untouched.
    Same patch on practice + topic; tutor.py now also tells the model to WRITE × on the
    board, never the letter x, so the client rule is a safety net, not the plan.
  - 2026-08-07  BARS: WHOLE-TOUR PREVIEW + CONTRAST (build bj, Jim's live replay of bi).
    (1) "Only the course is showing up during the introduction" — the bi preview appeared
    ONLY during the single ~30-second "bars" tour stop and was wiped at every other stop
    (clearHighlight cleared it). Now showBarsPreview() runs at TOUR START, the preview is
    NOT cleared between stops, and all three bars stay visible for the whole walk-through.
    The labeled placeholders are REPLACED (never just hidden) when the real [[today]] /
    [[unitplan]] tags render — real renders delete the preview flag, so nothing can ever
    hide a real bar. clearBarsPreview() removed (nothing needs it anymore).
    (2) "There needs to be contrast — dark gray, not super dark, and the spaces in between
    light": the bi card was near-black with translucent segments (everything read dark).
    Now: DARK-GRAY card, LIGHT unfilled segments (#e9e9f2), colored fills (accent/gold)
    unchanged — three clearly different tones.
  - 2026-08-07  TOUR SMALL FIXES (build bi, Jim). (1) The curriculum list the tour opens now
    CLOSES again when the tour moves on (left open it pushed Mr. Cadabra below the fold).
    (2) The bars tour stop now PREVIEWS the today/unit bars (clearly-labeled placeholders,
    removed when the stop ends) — before the first lesson turn only the course bar was
    real, so the stop described bars nobody could see. (3) The three bars sit on a DARK
    card now (labels/segments/text recolored) — they washed out on the light page.
  - 2026-08-07  TOUR POLISH, FINAL ROUND (build bg, Jim). (1) The 🎙️ emoji on the talk
    button rendered as a gray "dead fly" glyph on Windows — replaced with a real drawn SVG
    microphone (identical everywhere) on all three teaching pages. (2) "Type instead" was
    a small underlined link — now a REAL "Type my answer" button (.typebtn) as big as the
    mic/pause buttons; every student-facing string updated to the new name. (3) NEW tour
    stop for the three progress bars (glows #pbars): today's goals fill the top bar, the
    unit bar's quiz markers show how far the next quiz is, the course bar marches gold to
    the Final Exam.
  - 2026-08-07  NAV ORDER + ONE-STOP-PER-ITEM TOUR (build bf, Jim's exact sequence):
    Curriculum → Course assessment → Progress dashboard → Practice a problem → Explore a
    topic (NEW on the lesson page — #topicLink → /topic) → Final Exam → 📖 Look it up
    (library.js appends last). The tour now covers each item INDIVIDUALLY in that order
    (the old "two more helpers" stop lumped practice + assessment together); glow map
    split to one glow per stop; new Final Exam stop frames it as the mountaintop.
  - 2026-08-07  FOLLOW FIX, ROUND 2 (build ay, Jim's Basic-Math cookies: board work still
    slid below the fold ON the ax build). Root cause: our OWN anchor-scroll fires a scroll
    event, which the listener read as "the student scrolled away" and disabled following —
    so when the tap-to-answer row shrank the transcript a beat later, the re-anchor was
    skipped. New autoScroll flag marks programmatic scrolls; only a REAL student scroll
    releases following. Reproduced + verified against the exact sequence in a node sim.
    Same patch on practice + topic.
  - 2026-08-07  FOLLOW THE TURN (build ax, Jim: "the whiteboard disappears below and I have
    to scroll constantly" — first lesson, Entry-Level Math). The transcript no longer just
    pins to the bottom: every new bubble RE-ENGAGES following (a scrolled-up student is
    brought back when the tutor speaks), tutor turns taller than the window anchor to the
    START of the turn (his words + the board under them stay in view) instead of shoving
    the bubble off the top, and shorter turns still pin to the bottom as before. Same
    patch on practice + topic.
  - 2026-08-07  PAUSE IS BACK + LIBRARY CHIPS (build aw, Jim). (1) The ⏸ Pause button is
    RESTORED (reverses this morning's removal): pauses Mr. Cadabra mid-sentence, holds the
    turn (mic + sends disabled while paused), Resume continues. Same restore on practice +
    topic. (2) library.js now opens with CONTEXT CHIPS (current key terms / unit topics /
    today's goal) + "Something else…" for free typing.
  - 2026-08-07  SAY "SQUARED", NOT "TWO" (build av, Jim's live catch: the voice read "X²"
    as "x two"). forSpeech() now converts ² ³ π θ ± ≥ ≤ ≠ ° to spoken words before TTS.
    Same patch on practice.html + topic.html. Companion: [[graph]] hole="a" support
    (math-figures.js) + board-honesty/window-framing prompt rules (tutor.py).
  - 2026-08-07  RESUME CHOICE + LIBRARY TOUR STOP (build au, Jim: exploring a mid-course
    topic hijacked "Continue my lesson"). (1) Welcome-back overlay gains a second button —
    "🧭 Take me to my course path — Unit N" (N = first unmastered unit from SRV_PROGRESS;
    Unit 1 fresh, Unit 9 if all mastered). It sets FOCUS_UNIT (now `let`) and sends the
    NEW "__open_fresh__" sentinel; main.py tells the opener NOT to recap/resume the
    side-trip. "▶️ Continue where I left off" keeps the old behavior. (2) The tour gained
    a "library" stop glowing #libraryLink (📖 Look it up), so new students learn the
    reference library exists.
  - 2026-08-07  QUIET ASSESSMENT INVITATION, RESTORED + HARDENED (build at, Jim's live catch;
    the 08-06 version of this fix was lost when the runaway chat rebuilt this file from a
    stale copy). offerAssessment(): NO spoken line, NO chat bubble, NO status — the card
    stands ALONE on an OPAQUE backdrop (#assessInvite CSS), nothing shows or plays behind
    it. NEW: declining sends "__open_declined__" (or "__tour_done_declined__" after the
    tour) so the server tells the tutor the assessment question is asked-and-answered —
    he welcomes the student and starts at Unit 1 without re-offering it. kickoff(msg)
    gained an optional sentinel parameter. Companion server change in main.py; companion
    board rule 16 in tutor.py (check questions re-write their equation).
  - 2026-08-07  LOOK IT UP (build as, Jim): included the NEW shared /static/library.js —
    a "📖 Look it up" button in the left nav opens a search overlay + readable article
    bubble (the reference library; see library.py). The lesson conversation and voice are
    never involved. One script tag; purely additive.
  - 2026-08-07  PROGRESS BARS + FINAL EXAM (build aq, Jim: "a nervous student should always
    see where they are" + a real gated course final).
    (1) THREE THIN BARS under the goal banner (.pbars): TODAY (segments = the opener's goals,
        via new [[today items]] + [[todaydone n]] tags), UNIT (topic ladder via new
        [[unitplan]] tag, a 📝 marker per topic quiz — lit when passed (server history +
        live [[quiz]] passes) — and 🏁/🏆 Unit Quiz cap; text names the NEXT quiz), COURSE
        (nine segments, gold when mastered (live [[check]] passes update it too), 🎓 Final
        Exam cap — click it for the exam door). Fed by /api/session's new `progress` object.
    (2) FINAL EXAM: new "🎓 Final Exam" sidebar link + overlay (#finalOverlay). Not eligible
        → Jim's gate message + X-of-9 progress. Eligible → optional "Prepare" + "Take the
        Final Exam" buttons → same page with &final=prep|exam (FINAL_MODE): tour/assessment
        skipped, a .finalflag banner shows, and every /api/chat post carries `final` (the
        SERVER re-verifies the gate each turn — this page is just the door). New
        [[finalexam correct total]] tag → result card + POST /api/final. (Same day, build
        ar: the printable diploma was REMOVED — it implied an accredited school, which we
        are not (Jim). Passing now awards the 🏅 Course Champion medal in the trophy case;
        the result card + overlay link to the dashboard instead. Never reintroduce
        credential-style documents without counsel.)
  - 2026-08-07  VOICE-FIRST CLASSROOM (Jim: "back to the conversational back-and-forth").
    Three changes on top of yesterday's voice restore:
    (1) MIC-HIDING BUG FIXED: math-keyboard.js still carried its 2026-07-30 "type-in tier"
        lines that force-hid #talkBtn/#typeToggle and force-showed the composer at
        DOMContentLoaded -- silently overriding the 2026-08-06 restore, so the mic button
        never actually appeared. Those lines are gone (see math-keyboard.js); this page now
        fully owns mic/composer visibility. Voice truly shows now.
    (2) REMOVED the ⏸ Pause button and the Yes / No / I'm confused quick-reply row (HTML,
        CSS, setPaused/setQuick logic, their tour stop, and the `paused` turn-guards). The
        student just SAYS yes / no / "I'm confused" -- that's the point of the conversation.
    (3) REMOVED the 🧮 Math Keyboard (retired in math-keyboard.js; the file remains for the
        Enter ⏎ button + answer-bar layout). Typing stays as the fallback ("Type instead");
        the 📈 graph tool and the elementary tap-to-answer buttons are unchanged. Tour and
        welcome-tip copy updated to say "tap the mic and talk".
  - 2026-08-06  VOICE INPUT RESTORED (build an, Jim: "recreate it so the student speaks"). The
    tap-to-talk flow was never deleted — it was dormant behind one master switch (canRecord was
    hard-false since 2026-08-01's "no microphone" stance). Reactivated: canRecord is now a real
    CAPABILITY check — true for the typing courses on browsers that support getUserMedia +
    MediaRecorder, false for elementary tap-to-answer courses and browsers that can't record.
    A student taps 🎙️, speaks, taps when done; the audio posts to /api/transcribe (ElevenLabs
    Scribe — already live, unchanged, with its non-speech hallucination scrubber). "Type
    instead" remains available at all times, and unsupported browsers fall back to typing
    automatically. begin() no longer force-opens the composer when voice is on; the welcome tip
    and the ready-state hint now mention talking. NOTE (Jim's follow-up): the "no microphone,
    ever" promise across the marketing + privacy pages must be reworked to match — separate task.
  - 2026-08-03  iPAD/TABLET PASS: (1) the full-height layout now also sets 100dvh (kept 100vh
    for older browsers) so the composer can't hide behind Safari's collapsing toolbar on
    tablets; (2) the Yes / No / I'm confused quick buttons grew to a 44px-minimum tap height
    (Apple's touch-target floor). Audio was already tablet-safe here (warmUpAudio runs inside
    the Let's-go tap); challenge.html and demo.html got that fix today.
  - 2026-08-05  ASSESSMENT INVITATION (Jim: when someone joins a course for the FIRST time,
    welcome + tour as before -- and then warmly ENCOURAGE the Course Assessment so we can see
    strengths/weaknesses and build their plan; never force it, that redirect was removed
    2026-07-28 on purpose). Two moments, both only when the course has no history AND no
    placement yet: (1) a brand-new student -- the tour now ends with Mr. Cadabra speaking an
    invitation and a choice card (take the assessment / start at Unit 1); (2) a returning
    student ENTERING A NEW COURSE (tour skipped) -- same invitation before the opener. The
    choice card reuses the welcome-overlay design; "skip" continues exactly the old flow
    (__tour_done__ / __open__), so a student who declines loses nothing. `placed` was promoted
    from a loadSession local to page state (isPlaced) to make the decision. Additive only.
  - 2026-08-03  BOARD-PRIMARY: [[objects]] gained add="n" -- draws the first row as
    "⭐⭐⭐⭐⭐ + ⭐" so addition is SEEN, not imagined. Pairs with the new shared "board is the
    lesson, words are the backup" doctrine in tutor.py (all courses, all modes).
  - 2026-08-03  FIRST-WORDS + OBJECTS (Jim's playtest): (1) the FIRST spoken clip of a session now
    requests /api/speak with lead=3 (~1.1s of leading silence instead of ~280ms) -- audio outputs
    close during the quiet thinking wait and eat the head of the first clip; now they eat silence.
    (2) new [[objects emoji="⭐" groups="5"]] board tag draws big countable emoji rows (two rows to
    compare: "5 | 3"), so the elementary tutor can SHOW five stars instead of asking a child to
    imagine them. Count deliberately not printed. Additive only.
  - 2026-08-03  ELEM MODE FOR THE ANSWER BAR (Jim: tour says "just tap" but the bar said "type
    your answer" with Math Keyboard/Graph buttons). For entry/basic a body.elem-mode class now
    hides the 🧮/📈 buttons, the "Two ways to answer" line, and their "?" bubbles (CSS, so
    late-injected buttons are caught too); the input placeholder becomes "Tap an answer button
    — or type here"; and a tap-friendly one-liner sits above the bar. Typing stays as a quiet
    backup. Other courses unchanged.
  - 2026-08-03  TOUR PER CLASSROOM TYPE + &tour=1 (Jim: a toured demo code skipped the intro in
    Entry-Level Math). The tour decision now uses the server's classroom-type-aware `toured`
    flag (elementary tap-courses count separately from typing courses), and a new &tour=1 URL
    parameter force-replays the welcome tour for demos/testing regardless of history.
  - 2026-08-03  ELEMENTARY WELCOME + TOUR + SCROLL FIX (Jim): (1) new IS_ELEM flag (entry/basic)
    -- the welcome overlay's answer bullet, the tour's final "answer" stop, and the answer-bar
    hint now describe TAP-TO-ANSWER buttons ("just tap your answer"; "I'm not sure" helps) and
    never mention keyboards or typing for the two youngest courses; other courses unchanged.
    (2) SCROLL FIX ("I have to scroll to see what he's saying"): the choice buttons shrink the
    transcript from below, so a ResizeObserver now re-pins the transcript to the bottom on any
    size change, showChoices() re-pins the transcript instead of scrolling the page, and
    clearChoices() re-pins after removal.
  - 2026-08-03  REBRAND (Jim): all visible "MyTutor" text is now "Mr. Cadabra's Classroom" (titles, meta/OG, nav brand, body copy, footers). "Hyperion Shift LLC" remains ONLY on the legal pages (privacy/terms), where the legal entity must be named. Historical change notes untouched.
  - 2026-08-03  BUSY GLOW (Jim: "use the tour's fuzzy border around Mr. Cadabra when he's
    talking or thinking, so I can SEE he's doing something"): new .orbwrap.busyglow class
    reuses the tour ring (same accent color + tourpulse animation, circular) and setState()
    now toggles it on for the "thinking" and "speaking" states, off otherwise. Purely visual
    and additive; the tour highlight itself is untouched.
  - 2026-08-03  TAP-TO-ANSWER CHOICES (elementary courses): new [[choices options="a | b | c"]]
    tag renders big tappable answer buttons above the answer bar, plus an automatic
    "🤔 I'm not sure" button, so young children who can't type or read well can answer by
    tapping. A tap sends the answer exactly like typing it; buttons disable on tap and clear
    at the start of every tutor turn. Typing stays available as a backup. CSS is injected by
    the choices code itself (mtChoicesCSS), so no page styles were touched. Additive only.
  - 2026-08-03  ANALYTICS: added Plausible (privacy-friendly, cookieless) shared include in <head>. Pure add-on; nothing else changed.
    2026-08-01  KEY TERMS BOLD+RED (Jim): **term** from the tutor renders as a red bold
                .kterm span (first-use vocabulary emphasis); asterisks never show raw and
                the voice never reads them (forSpeech already strips them).
    2026-08-01  TOUR: new stop for the QUICK BUTTONS (Jim: "the tour should point out the Yes,
                No and I'm confused shortcuts") -- glows #quickRow and frames 'I'm confused'
                as a power move. Six stops total now.
    2026-08-01  POST-TOUR HANDOFF: the tour now ends with __tour_done__ (not __open__), so
                Mr. Cadabra doesn't re-introduce himself right after the tour introduced him.
    2026-08-01  TOUR: the Practice+Assessment stop now glows BOTH buttons (Jim: "it NEVER
                highlighted Practice a problem"). highlightEl accepts one id or a list;
                the look-here tag pins over the group's midpoint.
    2026-08-01  ONE TOUR PER STUDENT (Jim: switching to a new course gave him the whole tour
                again). /api/session now returns `toured` (has this student had a lesson in
                ANY course); the tour runs only when BOTH this course is fresh AND the student
                has never had a lesson anywhere. A new course just gets Mr. Cadabra's welcome.
    2026-08-01  TOUR FIXED (Jim: "he talks about the curriculum twice... 'this is me' and I
                have no idea where to look"). The 'this is me' stop pointed at #tutorPanel,
                an element REMOVED in an earlier redesign — highlight silently no-oped. The
                tutor head has that id again; the tour is now five DISTINCT stops (curriculum,
                dashboard, practice+assessment, Mr. Cadabra, the ANSWER BOX + Math Keyboard —
                no more nine-units repeat), each with the pulsing glow PLUS a bouncing
                '\U0001F440 look here' tag pinned to the exact element while he talks about it.
    2026-08-01  NO MICROPHONE, EVER (Jim's live check: Chrome asked for the mic on the new
                domain). begin() used to PRE-REQUEST getUserMedia so tap-to-talk would 'just
                work' — removed; canRecord is now hard-false (master switch), so the browser
                can never ask, matching the promise on the parents/mission/privacy pages.
                Recording code kept dormant below the switch. Type-in flow untouched.
    2026-07-30  APP NAV (Jim: back-navigation + Contact on every top bar): included the new shared
                /static/app-nav.js -- labeled pill links (🏠 Home · 🎓 My lesson · 📊 Progress ·
                🔄 Switch course · ✉️ Contact) injected into the top bar, context-aware per page,
                hiding the old obscure link when replaced. Additive; one script tag. Do no harm.
    2026-07-30  ANSWER BAR UNDER THE WHITEBOARD (Jim's review): the type-your-answer box moved
                from the narrow left rail to a FULL-WIDTH labeled bar ("✏️ Your answer · Type your
                answer here…") directly beneath the whiteboard. Same #composer/#input/#send ids, so
                showComposer/sendTyped and the shared components (math keyboard, graph, help tips)
                attach unchanged; new .center .composer styles. Do no harm.
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
                &code=/?code=. Also renamed "Math Tutor" -> "MyTutor" (title, topbar fallback,
                welcome heading). Do no harm.
    2026-07-30  COURSE NAME IN TOPBAR. The topbar showed a static "Math Tutor" so a student couldn't
                tell which course they were in. It now shows COURSE_TITLE (e.g. "Pre-Algebra",
                "Algebra I"), data-driven off ?course=. Static-only. Do no harm.
    2026-07-30  UI POLISH. (1) Answer box now reads "Write your response here, then press Enter…".
                (2) math-keyboard.js renames the 🧮 button "Math Keyboard" and shows a start-of-lesson
                reminder about it. (3) LEFT sidebar widened ~10% (240px -> 264px; right rail unchanged).
                Static-only. Do no harm.
    2026-07-30  ANSWER-BAR CLEANUP (paired with math-keyboard.js). The redundant standalone "Send"
                button is now hidden by math-keyboard.js ("each tool has its own send" -- the 🧮 and
                📈 tools plus the Enter key all still send). To keep a directly-typed answer sendable
                without a visible button, the #input placeholder now reads "Type your answer, then
                press Enter…". No send logic changed here (Enter -> sendTyped was already wired).
                Static-only. Do no harm.
    2026-07-28  COSMETIC: adopted the shared "math paper" background (graph-paper grid + faint
                drifting math symbols), declared last in the stylesheet so it supersedes the
                page's original flat wash. Presentation only. Do no harm.
    2026-07-28  ADDED DIFFERENTIAL EQUATIONS (eighth course): CURRICULUM_BY_COURSE.diffeq +
                COURSE_TITLES/COURSE_SUBJECTS/COURSE_OPENERS entries. Additive. Do no harm.
    2026-07-28  ADDED CALCULUS (seventh course): CURRICULUM_BY_COURSE.calculus + COURSE_TITLES/
                COURSE_SUBJECTS/COURSE_OPENERS entries. Data-driven. Additive. Do no harm.
    2026-07-28  ADDED PROBABILITY & STATISTICS (sixth course). CURRICULUM_BY_COURSE.probstat (9 units +
                blurbs + topics), plus probstat entries in COURSE_TITLES, COURSE_SUBJECTS, and
                COURSE_OPENERS. Data-driven off COURSE, so the lesson page serves it automatically.
                Additive. Do no harm.
    2026-07-28  ADDED TRIG / PRE-CALC (fifth course). CURRICULUM_BY_COURSE.precalc (its 9 units +
                blurbs + topics for the left-rail map), plus precalc entries in COURSE_TITLES,
                COURSE_SUBJECTS, and COURSE_OPENERS (the spoken welcome/tour line). Data-driven off
                COURSE, so the lesson page serves Pre-Calc automatically. Additive. Do no harm.
    2026-07-28  VOLUNTARY ASSESSMENT + COURSE-SCOPED CHECKS. Removed the forced first-entry redirect to
                /challenge (a brand-new student now starts the lesson at Unit 1). Added a "📋 Course
                assessment" link to the left nav (wired to /challenge with the course), relabeled the
                welcome-modal link, and softened the tour line that assumed a placement happened. Also
                the [[check]] POST now sends `course` so end-of-unit checks are filed under the right
                course (they were defaulting to Algebra I). Do no harm.
    2026-07-28  ADDED ALGEBRA II (fourth course). CURRICULUM_BY_COURSE.algebra2 (its 9 units + blurbs
                + topics for the left-rail course map), plus algebra2 entries in COURSE_TITLES,
                COURSE_SUBJECTS, and COURSE_OPENERS (the spoken welcome/tour line). Everything else is
                data-driven off COURSE, so the lesson page serves Algebra II automatically. Additive;
                the other three courses are untouched. Do no harm.
    2026-07-28  COLUMN-MATH VISUAL [[column]]. New whiteboard visual for stacked, place-value /
                decimal-point aligned addition & subtraction (pre-algebra). Fixes the bug where the
                tutor said "line up the decimal points" but the board showed the numbers centered and
                NOT lined up. [[column op="+" terms="2.40 | 1.35" result="3.75" caption="..."]] stacks
                the numbers so the decimal points sit in one vertical line (integer parts right-
                aligned, fractional parts left-aligned from the point), draws the operator + a rule
                line, and shows the result ONLY when the tutor supplies it (so it never runs ahead of
                the student). Added .colmath CSS + splitNum/colOp/showColumn + a handleTags "column"
                case. Same visual added identically to practice.html and topic.html. Static-only.
    2026-07-28  MULTI-COURSE WELCOME + TOUR (the "leftover"). The first-visit welcome
                pop-up and Mr. Cadabra's spoken opening tour used to say "algebra" no
                matter which course was chosen -- so a first-time Geometry or Pre-Algebra
                student was welcomed to "algebra." Now the wording follows ?course=:
                (1) the welcome lead names the subject via a new <span id="welcomeSubject">
                set from COURSE_SUBJECTS; (2) the tour's "your ___ course" line uses
                COURSE_TITLE; (3) the spoken opener is chosen from COURSE_OPENERS (one
                per course). Algebra I's welcome text and spoken opener are kept EXACTLY
                as before (byte-identical), so nothing about Algebra changes. All three
                courses have nine units, so the "nine units" wording stays accurate.
                Static-only change (no backend / APP_BUILD impact).
    2026-07-23  WHITEBOARD "SHOW THE MATH" (corrects the earlier same-day per-turn wipe).
                The board now PERSISTS the current picture across turns -- it does NOT
                auto-blank on talk-only turns. It only erases when Mr. Cadabra sends
                [[clear]] (which now triggers the eraser 🧽 sweep). New catch-all
                [[write lines="2X + 1 = 15" caption="..."]] -> showWrite() writes any
                equation/expression BIG on the board (variables auto-styled). tutor.py now
                tells him to SHOW the math he's discussing on the board EVERY time (he was
                under-using it), update it as it changes, and only [[clear]] on move-on.
    2026-07-23  "SHOW NOW" FIXES (per Jim). (1) On login we NO LONGER replay the old
                transcript into the chat -- seeing yesterday's messages up top made the
                current turn hard to find. The chat starts clean; Mr. Cadabra still
                remembers server-side and opens with a fresh recap. (2) The whiteboard now
                reflects ONLY the current turn: runTutor checks the reply for a picture
                tag; if there's a picture it draws it, if not it calls wipeBoard() to
                ERASE the board (a quick eraser 🧽 sweep, .wipe CSS) so an old diagram
                never lingers. (3) Contraction fix: a lone letter right after an
                apostrophe is no longer styled as a variable (I'm/Let's stay normal).
    2026-07-23  LESSON RELAYOUT + CHAT CLEANUP. (1) Mr. Cadabra (orb) + his spoken
                conversation + the tap-to-talk controls moved OUT of the center and INTO
                the RIGHT column; the whiteboard now owns the center. (2) Removed the
                "🎯 Find my level" placement link from the LEFT sidebar (placement still
                happens from the Home hub). (3) Removed the right-side "Covered" panel and
                all its JS (AGENDA/covered/markCovered/renderCovered; the [[covered]] tag
                is now a harmless no-op). (4) Opening tour updated (dropped the find-my-
                level + covered stops; added a "that's me on the right" stop; tour target
                `tutor`→`tutorPanel`). (5) Chat bubbles now strip markdown `*` so *word*
                no longer shows raw asterisks (styleVars). Layout via an override CSS
                block at the end of <style>; mobile stacks whiteboard over the tutor panel.
    2026-07-22  FUNCTION MACHINE + VARIABLES POP. (1) New [[machine input="3"
                rule="2x+1" output="7" fname="f"]] visual: showMachine() draws
                input -> rule box -> output, with the worked line "2 × 3 + 1 = 7" and
                "f(3) = 7". Used for Unit 3 FUNCTIONS instead of the balance/monkeys
                (the balance stays for Unit 2 equations). Fixes the picture where f(3)
                looked like the input was 1. handleTags gains a "machine" case.
                (2) styleVars(): every algebra variable now renders BOLD, CAPITAL, and
                RED (.mvar) in BOTH the chat bubbles and the visuals. A variable = a
                lone letter; ordinary words, "a"/"I", and function names f/g/h are left
                alone. addBubble now uses innerHTML=styleVars(text) (HTML-escaped first).
    2026-07-21  FULL COURSE MAP. The left "Today's plan" (6 linear-equation steps) is
                now "Your Algebra I course" -- the 9 units, with the student's CURRENT
                unit highlighted (from placement.start_unit) and earlier units marked
                done. Matches the tutor now teaching all 9 units. The right "Covered"
                panel + [[covered]] tags still work for the Linear Equations unit.
    2026-07-21  LESSON GOAL BANNER + PRACTICE LINK. (1) New [[goal text="..."]] tag ->
                a "🎯 Today's goal" banner above the whiteboard, set once when the
                tutor states the day's goal. showGoal() renders it. (2) Added a
                "✏️ Practice a problem" link in the left sidebar -> /practice (bring a
                problem from school and get coached on it).
    2026-07-21  CONTROL-TAG LEAK FIX (garbled speech + empty whiteboard). When the
                tutor's reply was cut off mid-tag (e.g. the long [[card ...]]), the
                unterminated tag was left in the bubble AND read aloud as gibberish,
                and the card never drew. Two fixes: (1) handleTags now strips a
                DANGLING/unterminated "[[..." fragment too, so raw markup is never
                shown or spoken; (2) added PRESET_CARDS + [[card id="..."]] so the big
                opening card is a SHORT, truncation-proof tag (id "cool-questions")
                that always renders. Inline [[card title items]] still works.
    2026-07-21  VOICE-STALL FREEZE FIX. If the streamed ElevenLabs audio started and
                then STALLED mid-sentence (a stream hiccup), the "ended" event never
                fired, so speak() waited forever and the whole turn froze (student
                stuck, button never re-enabled). speak() now runs a WATCHDOG that
                guarantees it always resolves: never-starts -> browser-voice fallback
                (5s); starts-then-stalls -> hand the turn back after ~3.5s of no
                playback progress; end-missed -> detect near-end+paused. browserSpeak
                also self-resolves if the engine never fires onend. No more freezes.
    2026-07-21  FIRST-TIME VS RETURNING FLOW. The page now reads `placed`/`history`
                from /api/session and behaves accordingly:
                  • Never placed AND no history -> redirect to the Challenge (you
                    must find your level before a lesson). Login already routes this
                    way; this guard also covers opening /session directly.
                  • Placed, no history (just finished the Challenge) -> the auto tour
                    plays, then Mr. Cadabra teaches at the placed level.
                  • Has history (returning) -> NO tour; the opening overlay says
                    "Welcome back", and Mr. Cadabra opens with a short spoken recap
                    of where you are, then continues.
    2026-07-21  TOUR NOW AUTO-PLAYS (no taps between stops). The opening walk-through
                is a scripted client-side sequence (runTour): Mr. Cadabra speaks the
                welcome + one-line definition of algebra, then narrates each stop in
                his own voice while the matching spot lights up, and moves on by
                itself -- no "ready for next?" prompts. Order + content per Jim:
                  • Curriculum  -> note you can click each of the nine units to see
                    the topics covered in that section.
                  • Find my level.
                  • Progress dashboard -> describe what each part shows.
                  • Today's plan (bottom-left) -> what we'll do today.
                  • Covered (right side) -> what we've done today.
                When the walk ends it hands off to the lesson (tutor's first reply).
                Each line dwells long enough to read even if the voice is off.
    2026-07-20  OPENING PAGE TOUR + LAYOUT + QUICK BUTTONS + FIRST-WORD FIX.
                (1) New [[highlight id="..."]] control tag: the tutor can spotlight
                    parts of the screen (curriculum, find-my-level, dashboard,
                    todays-plan, covered) during the opening walk-through -- the
                    element glows and scrolls into view; the spotlight clears at the
                    start of each tutor turn. Wrapped "Today's plan" (planPanel) and
                    tagged the right sidebar (coveredPanel) as tour targets.
                (2) THREE QUICK BUTTONS (Yes / No / I'm confused) beside tap-to-talk,
                    enabled only on the student's turn, so they can answer without
                    talking. Tap-to-talk is still the primary control.
                (3) LAYOUT: gave the tutor row breathing room, capped the transcript
                    height, and pushed the whiteboard down so student replies aren't
                    squeezed between the text and the board.
                (4) FIRST-WORD CLIP FIX: play a short SILENT WAV through the audio
                    element once on the opening tap to warm up the pipeline, so
                    Mr. Cadabra's first word or two is no longer cut off.
    2026-07-20  SPEECH-TO-TEXT VIA SERVER. Replaced the browser's flaky speech
                recognition with MediaRecorder capture + POST /api/transcribe
                (ElevenLabs Scribe). Works the same in every modern browser. Tap to
                record, tap when done -> audio is transcribed on the server -> the
                text becomes the student's message. Fixes "button reacts but it
                can't hear me."
    2026-07-20  Mic reliability: request microphone permission UP FRONT (on "Start"),
                recover if the recognizer stalls (onend restart), and show clear
                messages if the mic is blocked or nothing was heard. Fixes "button
                reacts but doesn't record my voice" (esp. on the new mytutor-2
                origin, where the old mic permission didn't carry over).
    2026-07-20  VOICE REWORK -> TAP-TO-TALK. The mic is now OFF except while the
                student is actively recording (they tapped the glowing button), so
                there is no echo and the tutor never replies to phantom/noise input.
                The talk button is DARK/disabled while the tutor talks, then LIGHTS
                UP ("Tap to talk") the instant he finishes. While recording, the
                student's words show live and the button turns red ("tap when
                done"); a pause auto-sends, or they tap to send. Mr. Cadabra opens
                the session first. Also: forSpeech() now converts notation to spoken
                words (f(x)->"f of x", strips parentheses/symbols) and the stray
                lead-in was removed, fixing garbled/made-up words.
    2026-07-19  Added "🎯 Find my level" links (sidebar + welcome) to Mr. Cadabra's
                Challenge placement quiz (/challenge?code=...).
    2026-07-19  Relayout: Mr. Cadabra (smaller orb) + name + status in a compact
                TOP-LEFT row, with the conversation to the RIGHT of it; the
                whiteboard now expands to fill the space and the balance visual is
                bigger. Voice: the mic now stays LIVE through the tutor's turn (its
                results are ignored while he speaks) so it catches the student
                immediately even if they talk quickly.
    2026-07-19  Warmer, more colorful palette; removed the duplicate big caption
                (conversation now shows in ONE place, the transcript; a small
                status line under the orb shows Listening/Thinking); added a
                first-screen WELCOME/how-to overlay; prepend a tiny pause to the
                ElevenLabs text so the tutor's first word isn't clipped.
    2026-07-19  Left sidebar now has a collapsible CURRICULUM navigator (9 units;
                click a unit for its details in a modal) and a PROGRESS DASHBOARD
                link (/dashboard?code=...).
    2026-07-19  INTERFACE REBUILD (three fixes):
                  1) The "teacher" is now a LIVING VOICE ORB (canvas): a glowing,
                     colorful sphere that breathes when idle, pulses while
                     thinking, and morphs/reacts to the REAL audio while speaking.
                  2) HANDS-FREE conversation: tap "Start talking" once (mic
                     permission + audio unlock), then just talk. Continuous speech
                     recognition with silence-based turn-taking; the mic auto-
                     pauses while the tutor is speaking so he never hears himself.
                     A "Pause" button stops; "Type instead" is a fallback.
                  3) LOW LATENCY: the tutor's voice STREAMS from /api/speak (audio
                     starts before it's fully generated) using the fast model.
                Still: session memory, live captions, control-tag visuals
                ([[balance]], [[card]], [[covered]]), and browser-voice fallback.
    2026-07-19  Natural ElevenLabs voice + [[card]] visual (superseded).
    2026-07-19  Visual redesign; voice-first; text-only (all superseded).
```

I did no harm and this file is not truncated.

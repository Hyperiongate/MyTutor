# CHANGELOG -- demo.html  (notes rolled out of the file's header)

Moved out of `static/demo.html` on 2026-09-08 (build ui): every CHANGE NOTE dated before 2026-09-01 -- 23 entries, VERBATIM, in the order they sat in the file (newest first). The 8 notes from 2026-09-01 on stay at the top of `static/demo.html` itself, and new notes keep going there. Nothing below was edited; grep this file for a build letter or a date. When the header is rolled out again, the newer block is added ABOVE this one.

```text
    (nh) 2026-08-25 -- THE SEAMS JIM HEARD, WATCHING THE WHOLE DEMO. "Very good. Just
    a couple of small things." Three of them, all shipped:
    ① ⚠️ FEEDBACK WAS BEING CUT OFF MID-WORD. Four sites advanced on FIXED TIMERS
    (setTimeout(next, 1900) / 3400) while the right/wrong line was still being spoken
    -- his real-voice "you got it" lines run four to six seconds, so the next beat
    interrupted them and Jim heard the lesson "skip immediately" past its own praise.
    Every advance now CHAINS on the line finishing (sayThen / abraSay callbacks) plus
    a 550-600ms breath. The last-question case was the same bug one layer down:
    Abrabot's praise was stomped by his own outro 1.5s in. NEVER put a fixed timer
    under a spoken line -- ruletests 3dr now bans the pattern.
    ② ABRABOT HAS AN ENTRANCE. He was a face-swap in the 76px sidebar orb; Jim: "maybe
    he flies in from someplace or he bounces around like he's excited, and he should
    take up more space in the white space." He now FLIES onto the whiteboard at 220px
    (#abraBig, @keyframes abrafly -- overshoot bounce, drop-shadow) while Mr. Cadabra
    is still introducing him, then BOBS excitedly for the whole practice (@abrabob).
    ③ ONE CHARACTER PER FACE. The orb stays Mr. Cadabra throughout -- he never left
    the room; the big bouncing face IS Abrabot. Each face's mouth moves only for its
    OWN lines (lastRobot routes the speaking level).
    ⚠️ HARNESS LESSON, EXPENSIVE AND KEPT: the old browser-test check for "the
    congratulations landed" used body.textContent.includes("Congratulations") --
    which matches THIS PAGE'S OWN SCRIPT SOURCE (CONGRATS_LINE is a JS literal inside
    <body>), so it had been vacuously true since it was written. Element checks only
    (#answer .endbox). The upgraded harness also carries an INTERRUPTION LEDGER
    (utterances cancelled before their own end) that proves ① stays fixed.
    (ng) 2026-08-25 -- THE SIDEBAR CATCHES UP WITH THE PRODUCT. Jim deployed nf, opened
    a demo, and: "in the sidebar of the demo i see no practice problems." He was right
    and nf was incomplete: it put practice at the END of the lesson but never touched
    this page's replica SIDEBAR, which still showed the pre-mu classroom -- no robot
    button, and a tour that walked from Practice-a-problem straight to Explore-a-topic
    as if Abrabot did not exist. The demo must look like the product it is selling.
    THREE ADDITIONS: ① the 🤖 Extra practice button, same face, same name, same
    position as session.html's (right after Practice a problem -- the mu comment about
    two-things-both-called-practice applies here verbatim). ② a TOUR STOP that glows
    it and says what it is, the line appended to BOTH voice lists (244 -> 245,
    verified by PARSING both, the nf comma lesson applied). ③ THE BUTTON WORKS -- its
    six neighbours are set dressing, but a visitor who taps the robot gets practice ON
    THE SPOT: the standalone door skips the "before we finish" handoff (that sentence
    is true at a lesson's end and false from a cold tap -- no line plays that isn't
    true), defaults to the course the sidebar furniture shows, and lands on the level
    picker afterwards, never a dead end.
    Validated by FOUR headless journeys, fifteen assertions: lesson->practice with a
    deliberate miss; typed lesson then skip; cold tap from the sidebar (handoff
    verified ABSENT); and the full tour heard introducing the button.
    (nf) 2026-08-25 -- THE DEMO PRACTICES TOO. Jim: "rewrite the demos so that they
    include the practice problems with Abrabot... they'll be up and ready to run."
    Every level demo now ends the way the real product does: teach -> problem ->
    ABRABOT PRACTICE (two quick problems) -> congratulations. One hook in next()
    (s.end && !practiceRan) instead of ten edits inside DEMOS; a fresh level
    practices again (startScript resets practiceRan).
    ⭐ THE ANSWERS ARE COMPUTED, NEVER TYPED. ABRA_BANK entries carry OPERANDS between
    strict-JSON markers; abraAnswer() derives each correct choice, and ruletests
    PART 3dr re-derives all twenty in Python and fails the build on any disagreement.
    Two independent implementations agreeing IS the check -- keep them independent.
    ⚠️ ABRABOT NEVER USES THE PAID VOICE. His lines ride browserSay(robot=true) --
    higher pitch on the same browser voice (the one-English-voice guarantee drill.html
    settled), "Abra-bot" respelled so engines say it right. The whole segment costs
    zero, every visitor, forever. Mr. Cadabra's single handoff is the ONLY new
    rendered line: appended to VOICE_LINES *and* main.py's DEMO_VOICE_LINES
    (243 -> 244, verified byte-identical BY PARSING BOTH, after a missing comma in
    main.py silently concatenated two Python strings -- regex said 244, ast said 243;
    trust the parser). Addressed by lineStarting() anchor, never by index. Renders on
    first play (build ca retry protects the first visitor).
    His FACE is the same canvas wearing TutorFace's abrabot palette (persona flag) --
    zero new art. Misses get the drill's own kindness: one retry, then told warmly,
    and a right-after-retry still counts. "Skip practice ▸" keeps the impatient
    visitor in charge and lands on the congratulations, never a dead end.
    DRIVEN IN A REAL BROWSER before shipping: two journeys (entry played through with
    a deliberate miss; prealgebra typed then skipped), ten assertions, all green.
    (ez) 2026-08-13 -- TWO THINGS JIM FOUND BY WALKING THE DEMO HIMSELF.
    (1) NO REPEATED DIALOGUE AFTER THE LESSON. He came through the teachers door, took
    the walk-through, clicked "See a real lesson", worked the problem — and at the end
    got the WALK-THROUGH's ending panel: the same title, the same buttons, and Mr.
    Cadabra re-speaking the teachers outro line he had already heard, while offering him
    "✏️ See a real lesson" seconds after he finished one. His words: "it repeats
    something that was already seen... there shouldn't be a dialogue that goes along with
    it that I've already heard." CAUSE, exactly: showEnd() speaks CONGRATS_LINE and then
    calls showBalloons(true, TRUE) — that second argument means "we just finished a
    lesson" — but showBalloons' first line hands any audience-door visitor to
    showAudienceEnd(spoken) and DROPPED it. So the congratulations framing was thrown
    away and the walkthrough's ending was served instead. FIX: the signal is passed
    through; showAudienceEnd gains an `afterLesson` mode that keeps the congratulations
    title, offers what comes NEXT (another level, or the walk-through again — never the
    lesson just done), and SPEAKS NOTHING, because the congratulations line is still in
    the air and one voice at a time is the whole rule.
    (2) ONE WELCOME, NEVER TWO. The home page now plays his SITE welcome on the way in
    (build ez there) and leaves a one-shot sessionStorage marker. startDemo reads AND
    CLEARS it, and on a marked arrival skips this page's own demo_welcome entirely. A
    visitor who arrives any other way — a link, an ad, a search result — still gets the
    demo's own welcome, which is the line written for this exact moment.
    Guarded by ruletests PART 3ad, negative-tested, and driven in a real browser.
    (ei) 2026-08-12 -- THE TEACHERS DOOR: ASSISTANT, NOT REPLACEMENT.
    Jim: a teacher sees three wins in this app -- it can help ME, it can help my
    STUDENTS, and it lets me teach INDIVIDUALLY (who needs more help, who can go
    ahead) -- and one threat: "I'm responsible for this class. Am I really going to
    let an AI run it and replace me?" The /demo?view=teachers walkthrough now names
    that threat in its FIRST BREATH and answers it all the way through, with the
    tour untouched (same nine stops, same panels, same order):
      - NEW INTRO: opens "I am not here to replace you" -- he's the teaching
        assistant who gives every student patient one-on-one practice at their own
        pace and reports back. Made-up-class disclaimer and the earned-mastery
        sentence kept. "Your class stays yours."
      - Stop 1 (open a class): the right way to think of him -- the assistant who
        does what no teacher has thirty hours a day for, while YOU do the teaching.
      - Stop 5 (needs attention): reframed as triage that frees the teacher from
        one-pace-fits-all -- the stalled surface early, the students pulling ahead
        surface too (the honest read below carries Sofia), "no class learns at one
        speed, and you never have to teach as if it does."
      - Stop 9 (open a student): the decision line -- "I gather the picture, you
        make the teaching decisions."
      - NEW OUTRO: what it DOESN'T do (plan your lessons, grade your judgment, run
        your room), what it hands you instead, then the real-lesson invitation.
    Stops 2/3/4/6/7/8 keep their proven lines (three numbers, the heatmap, the
    roster, the honest read on Aiden/Ben/Sofia, strengthen next, time on task).
    MECHANICS: five lines APPENDED to VOICE_LINES (238 -> 243), identical in
    main.py's DEMO_VOICE_LINES -- clips by index, lists never reorder, every anchor
    resolves to exactly one line (PART 3j). Clips render on first play (build ca
    retry protects the first visitor).
    (eh) 2026-08-12 -- THE STUDENTS DOOR CHARMS THE CHILD AND REASSURES THE PARENT.
    Jim: parents try the student door AS IF they were their child -- "what does my
    child want to see?" So /demo?view=students now leads with the three things that
    sell that double audience, with the tour untouched (same ten stops, same panels,
    same order; STU_STOPS still overrides by index and still has ten entries):
      - NEW INTRO: the wow first -- "I really talk, and I really listen": say your
        answer out loud, he hears you, you work it out together on the whiteboard at
        your speed. Made-up-Maya disclaimer kept.
      - Stop 1 (honest read): "the part you can just ask me for, out loud, any time"
        -- no mystery numbers, no report-card code; you always know where you stand.
      - Stop 9 (trophy case, the one Jim named): earning is the whole point --
        "nobody can give you these, not me, not anyone" -- which is why the page
        feels good to open. Badges per gold unit, the effort medal, Course Champion.
      - NEW OUTRO: the two promises a listening parent needs to hear, in the kid's
        own tour -- I ONLY ever talk about math (anything else gets a smile and a
        steer straight back), and I NEVER just give you the answer -- then the
        real-lesson invitation.
    Stops 2-8 and 10 keep their proven lines (five numbers, gold units, quiz detail,
    strengthen next, habit charts, the path, next-three-sessions, courses).
    MECHANICS: four lines APPENDED to VOICE_LINES (234 -> 238), identical in
    main.py's DEMO_VOICE_LINES -- clips addressed by index, lists never reorder,
    every anchor still resolves to exactly one line (PART 3j). New clips render on
    first play; the per-line retry (build ca) keeps a slow first fetch from tripping
    the voice latch.
    (eg) 2026-08-12 -- THE PARENTS DOOR SPEAKS TO WHAT A PARENT ACTUALLY ASKS.
    Jim, from a parent-teacher conference: a teacher shows the app to a parent -- what
    does that parent want to know? Two things, everywhere: IS MY CHILD ACTUALLY
    LEARNING, and WILL SHE ACTUALLY WANT TO DO THIS? The /demo?view=parents
    walkthrough now answers both, stop by stop, while keeping the exact same tour
    (same ten stops, same panels, same order -- HS_STOPS still overrides all ten by
    index and is untouched):
      - NEW INTRO: names the two parent questions up front, keeps the made-up-Maya
        disclaimer and the never-invent-a-good-week promise.
      - Stop 1 (honest read): reframed as the conference question -- "how is my child
        really doing" in plain English, not a score out of ten.
      - Stop 2 (honest read): adds the teaching promise -- he teaches out loud, one
        step at a time, and NEVER just hands her the answer; hard weeks are said
        plainly.
      - Stop 4 (five numbers): one record shared with the teacher, nothing rounded
        up -- plus the engagement proof: nobody can assign a streak; it only grows on
        days she opens the classroom herself.
      - Stop 5 (strengthen next): kitchen-table specific, and the rule-55 story a
        parent loves: a missed problem comes back days later as a fresh one -- a
        second chance, not a quiet gap.
      - Stop 8 (trophy case): reframed as THE answer to "will she actually use it?"
        -- earned, never given, and why a child opens the classroom unasked.
      - NEW OUTRO: carries the voice-privacy answer (speech becomes text, audio
        deleted right away, never stored; he stays warmly on the math) before the
        real-lesson invitation.
    Stops 3, 6, 7, 9, 10 keep their proven lines (the minute-box, units-as-evidence,
    the journey path, courses, and the printable record). MECHANICS: seven lines
    APPENDED to VOICE_LINES (227 -> 234), identical in main.py's DEMO_VOICE_LINES --
    clips are addressed by index, the lists never reorder, and every anchor still
    resolves to exactly one line (PART 3j). New clips render on first play (or via
    the admin pre-render); the per-line retry keeps a slow first fetch from tripping
    the voice latch (build ca).
    (ct) 2026-08-10 -- THE BOARD KEEPS ITS SPACE · AND ALL FOUR VIEWS ARE THE REAL ONES.

    ⭐ THE LIVE DEFECT FIRST. Jim, in a Basic Math demo lesson: "it started off showing
    everything really good on the board. But then when the answers popped up, they
    shortened the whiteboard to the point where I could only see a fraction of what was
    actually being displayed... maybe instead of four answers stacked on top of each
    other, one row of four, or two rows of two."
    Root cause: .choices was a one-per-line GRID and .answerzone could take 47vh, while
    .feed is flex:1 -- so every pixel the answers took came straight out of the
    whiteboard, and the fraction bars he was being taught with were cut off top and
    bottom. THE REAL CLASSROOM ALREADY SOLVED THIS: session.html lays its tap-to-answer
    buttons out as a centred WRAPPING ROW (.choicerow). The demo was the outlier. Same
    shape here now, the answer zone is capped at 32vh, and the board has a min-height
    FLOOR so no future widget can squeeze it again. Measured at 1280x800: board
    351px -> 435px, answers 193px -> 109px, four buttons on one row instead of four.

    ⭐ AND THE OTHER THREE VIEWS. Jim: "the parents view looks great. So I'd like to do
    that same idea for the homeschool, the teacher, and the student." The teacher and
    student dashboards now get what the parent view got in cs -- a section-for-section
    mirror of the real page, with a stop per panel:
      TEACHER: class tiles · the 9x6 MASTERY HEATMAP (its CSS had been sitting in this
      file unused since a rebuild dropped the grid) · a fuller roster · an honest read on
      the class that names the under-served student, not just the struggling ones ·
      per-student strengthen-next WITH the broken rule · time on task.
      STUDENT: the honest read · tiles with the ring · units · quiz ladder · strengthen ·
      the two habit charts · journey + meter · what's next · trophies · courses.
    HOMESCHOOL needed nothing new -- it rides the parent dashboard, finished in cs.

    ⚠️ The student DOOR now has its own script (STU_STOPS). The shared student tour talks
    about Maya in the third person, which is right when a parent is being shown "what your
    child sees" -- and wrong at /demo?view=students, where the visitor IS the student and
    was just greeted with "Hi! This is your dashboard."
    VOICE_LINES 211 -> 227, APPENDED.
  - (cs) 2026-08-10 -- THE PARENT DASHBOARD IS THE REAL ONE NOW. Jim: "the demo is what
    is selling this product, and the parent is our number one customer... we have this
    great dashboard for parents. What we've done with this demo is we created a shortened
    dashboard that doesn't show much at all with a whole lot of words. I want a fully
    fleshed out parent dashboard, and I want you to give me a tour of that dashboard."
    He is right, and this page's own design notes already said so: they specify seven
    sections for the parent view and it shipped with four -- honest read, tiles,
    strengthen, records. The talking had outgrown the screen.
    #dashParent is now a section-for-section mirror of /dashboard?view=parent: the honest
    read, the read-only parent box with the records link, five tiles with the mastery
    ring, focus areas, the nine units with dates AND scores, the learning journey, the
    status meter, the trophy case, the courses strip, the placement strengths, the
    honesty footer. Component CSS follows dashboard.html so a visitor is looking at the
    product, not at an artist's impression of it.
    ⚠️ TWO THINGS MOVE TOGETHER NOW. The parent tour is TEN stops, and HS_STOPS overrides
    it BY INDEX -- add a stop without adding a homeschool line and a homeschooling parent
    is told about their child's teacher, silently. PART 3j fails on a length mismatch.
    VOICE_LINES 201 -> 211 (five parent stops, five homeschool), APPENDED.
    Numbers are Maya Rivera's canonical set from Demo_Design_Notes and must agree across
    the student, teacher and parent views. Change one, change all three.
  - (cr) 2026-08-10 -- ONE DOOR, ONE DASHBOARD. Jim: "when we go to the homeschool page,
    the teacher page, the student page, I want that demo to only show the dashboard
    that's interesting to that particular person. I don't want any links to any other
    dashboards from there."
    AUDIENCE_KEY is set ONCE at page load from ?view=, and audienceLocked() is asked by
    every path that could hand the visitor somebody else's screen. There were three, and
    each failed silently -- nothing errors, the wrong dashboard just opens:
      1. the end-of-tour panel (showBalloons) offered all three views;
      2. the "✓ Done — show the three views" button, visible the whole time;
      3. the "↩ Back to the three views" button in each dashboard header.
    All three now lead to showAudienceEnd() -- this door's own ending, with its own
    spoken closing line. The three-balloon chooser still belongs to the OPEN demo at
    /demo, where the visitor asked to see all three; that path is untouched.
    A locked door must not become a dead end, so the ending offers the walkthrough again,
    a real lesson at any level, and the pricing page. "See a real lesson" goes through
    enterClassroomPicker(), which sets the classroom layout FIRST -- the audience doors
    deliberately never set it, so without that the picker drew into a hidden panel: the
    cq blank-screen bug in a new costume.
    VOICE_LINES 197 -> 201 (four closing lines, APPENDED). ruletests PART 3j checks all of
    this from the source; the behaviour itself was driven in a real browser across all
    four doors plus the open demo.
  - (cq) 2026-08-10 -- SCREEN FIRST, WORDS SECOND · AND HOMESCHOOL GETS ITS OWN SCRIPT.
    Jim, walking the homeschool door: "it talks for a long time and says this is the page
    that your child works from. It's just a blank screen. It stays blank, blank, blank,
    blank until it gets to the parents' view." Both faults were introduced in cp.
    (1) startAudienceWalkthrough set document.body.className='' -- blanking the page --
    and then spoke a ~70-word intro BEFORE openDash() ever ran. Thirty seconds of talking
    at nothing. openDash(which, opts) now paints the dashboard, glows the first stop, THEN
    speaks the intro, THEN runs the tour; the body class is deliberately left alone; and
    armDashWatchdog is told about the intro so its deadline accounts for the extra words.
    If you change the order back, PART 3j fails -- deliberately.
    (2) Homeschool was pointed at the PARENT dashboard and inherited the parent's stop
    lines word for word, so a homeschool visitor was told about "your child's teacher".
    runDashTour(d, k, lines) now takes an override script and homeschool supplies five
    lines of its own. The layout is still the parent one on purpose: it is the right set
    of numbers, and duplicating a dashboard to change five sentences is the copy-paste
    drift that gave us the build-bk rule bug.
    Also: the audience lines are found by their opening WORDS (lineStarting) instead of by
    counting back from the end of VOICE_LINES. The end moves every time we append; a
    counted index rots the moment anyone adds a line, and it rots SILENTLY -- straight to
    the browser's mechanical voice. Five lines APPENDED (192 -> 197), matching main.py.
  - (cp) 2026-08-10 -- AUDIENCE WALKTHROUGHS: /demo?view=parents|teachers|homeschool|
    students. Jim: "it's almost like a video... I would like one of those available, a
    very obvious button that says view the demo on the parent page, the teacher page,
    the homeschooling page, and the student page... at the very least it will go through
    the appropriate dashboards for that site."
    Built as a DEEP LINK, not four new tour engines. Everything a walkthrough needs is
    already here and already right: the real dashboard layouts, the one sample student
    whose numbers agree across all three views, the narrated stops, the per-line voice
    retry, the watchdog that can never strand anyone. Copying that into four marketing
    pages is precisely the copy-paste-drift behind the build-bk rule bug and the
    board-wrap bug. One classroom, one demo, four doors into it.
    The visitor still taps once to begin -- browsers will not play audio until someone
    acts, and a silent walkthrough is worse than none. VOICE_LINES gained FOUR audience
    intros, APPENDED (clips are addressed by index); main.py's DEMO_VOICE_LINES has the
    identical four. ruletests.py PART 3j proves the lists stay identical.
  - 2026-08-09  HIS VOICE ALWAYS COMES BACK · NEVER STRANDED (build ca, Jim's walk).
    (1) serverVoiceOK was a ONE-WAY LATCH: the first clip that failed to load dropped the
    whole rest of the demo to the browser's mechanical voice. Every line now tries his
    real voice, a failure is retried once and falls back for THAT LINE ONLY, a stalled
    clip gives up after 6s, and the server voice is re-tried every fifth line even after
    repeated failures. ⛔ NEVER re-introduce a permanent voice latch — the first visitor
    to hear a newly-appended line is always the one who trips it.
    (2) The three bubbles used to depend on the audio chain finishing, so a stalled clip
    stranded the visitor on a dashboard. Three independent paths now bring them back —
    the tour ending, a watchdog armed when the dashboard opens, and a "✓ Done — show the
    three views" button visible the entire time.
  - 2026-08-09  VISIBLE FIGURES · NO MIC · REAL DASHBOARDS (build bz, Jim).
    (1) The figures were nearly invisible: the SVGs had a viewBox but no WIDTH, and in
    the whiteboard's centred flex column that collapses to a smudge. .fig now takes a
    real width (max 660px) with a 150px min-height and a bigger caption.
    (2) The demo no longer uses the microphone ("let's just drop the speaking part for
    the demo") — a sales page must not hang on a permission prompt. Every lesson line is
    re-worded for typing (appended 154-173), the mic UI is gone, and the demo STT
    endpoint was removed server-side. normSpoken() still runs on typed input, so
    "two" / "negative two" / "fifty five" are all understood.
    (3) The three dashboards now MIRROR THE REAL SCREENS. They previously invented a
    mastery grid, per-student coaching reasons, a class honest-read and trend charts that
    the product does not have. Student = the real dashboard tiles + where-you-are + quiz
    results + strengthen next + trophy case + courses. Teacher = the real class manager
    (class code, units mastered/started, needs attention, open a student read-only).
    Parent = the same dashboard in parent view. Tours rewritten (appended 174-187).
    ⛔ If the real dashboards change, change these too — the demo must never show a
    screen the product doesn't have.
  - 2026-08-09  BUBBLES IN THE MIDDLE, AND AFTER EVERY TOUR (build by, Jim). The three
    dashboard bubbles moved from the bottom of the page into a CENTERED overlay, and
    they are now offered again at the END OF EVERY DASHBOARD TOUR — not only after the
    lesson. "✕ Let me look around on my own" dismisses them with the dashboard still
    open behind, and a floating "👀 Show the three views" button brings them back.
    (Companion, outside this file: an orange "Try the demo" pill in the marketing nav,
    added by static/site-nav.js.)
  - 2026-08-09  NO-FAILURE LESSONS + FULL DASHBOARDS (build bx, Jim: "we got one shot
    to do it right, and it failed" — a lesson referred to a diagram that never appeared).
    ALL TEN LESSONS REBUILT: every picture a spoken line mentions is DRAWN in that same
    step (new unit-circle + bar-chart figures; the geometry triangle now carries the
    ASKED angles 90/35/?, not the taught 60/60/60), every question is voice-worded, and
    each course teaches a worked example first. HARD RULE for this file from now on: if
    a line names a picture, the step draws it — audit before shipping.
    THE THREE DASHBOARDS ARE NOW FULL: one invented student (Maya Rivera, 7th grade)
    with a complete record, a 6-student teacher roster + 9×6 mastery grid + honest read,
    and a parent view with the plain-English read, the arc since September, everything
    mastered with dates, and what's hard right now WITH the plan. Six spoken tour stops
    each. VOICE LINES: 39 APPENDED (115-153); 0-114 untouched.
  - 2026-08-09  TALK TO HIM + THE THREE DASHBOARDS (build bw, Jim). (1) The demo no
    longer asks a visitor to TYPE: every question is answered by tapping the microphone
    and SAYING it, exactly the way a student does. Audio posts to the new
    /api/demo-transcribe (same engine, same transcribe-and-delete guarantee, rate
    limited by IP since a demo has no student code); spoken answers are normalised
    ("negative two" -> -2, "one half" -> 1/2) before matching. Typing stays as a one-tap
    fallback and is used automatically when a browser can't record or permission is
    declined. Elementary courses still TAP, because that is what the real elementary
    classroom does. (2) TEACH FIRST: every course now opens with a taught example --
    a real number line for negative numbers, a shaded fraction bar, a labelled triangle,
    a worked equation -- before any question is asked (rule 19, "I do, then you do").
    (3) THREE DASHBOARDS: after the problem, three big balloons offer the STUDENT,
    TEACHER and PARENT views. Each opens full-screen, Mr. Cadabra tours it in three
    spoken stops, and the balloons come back afterwards so every view stays available.
    VOICE LINES: 20 APPENDED (95-114); 0-94 untouched so cached audio stays valid.
  - 2026-08-09  FULL-PAGE CLASSROOM DEMO (build bv, Jim: "when they click start the demo,
    I want them to go to a full page view, and go through the complete tour of the page
    just like we do with a new student"). The welcome card he liked is kept as the front
    door; pressing "Start the demo" now swaps the whole window to the REAL classroom
    layout -- left rail (Mr. Cadabra, Curriculum, Course assessment, Progress dashboard,
    Practice a problem, Explore a topic, Final Exam, Look it up), top bar, goal banner,
    the three progress bars, the big whiteboard, and the answer zone -- and Mr. Cadabra
    walks ALL TEN STOPS in the same order as the real student tour (build bf order:
    curriculum -> assess -> dashboard -> practice -> topic -> final -> library -> board
    -> bars -> me/how you answer), each stop spoken with the matching element glowing.
    The Curriculum list opens for its own stop and closes again afterwards, exactly like
    the real tour (build bi). Skippable throughout. Everything after the tour is
    unchanged from build bt: course picker -> scripted course intro -> ONE real problem
    worked INTERACTIVELY (escalating help on misses) -> spoken "Congratulations".
    VOICE LINES: 7 APPENDED (88-94, the sidebar stops); 0-87 untouched so cached audio
    stays valid. Identical append in main.py's DEMO_VOICE_LINES.
  - 2026-08-09  CLASSROOM DEMO REDESIGN (build bt): the demo became a real lesson rather
    than a movie -- welcome, spoken tour, ten-course picker, one interactive problem,
    congratulations. The math keypad grid was retired here.
  - 2026-08-05  landing page "Hear him teach" plays VOICE_LINES index 71 (build aj).
  - 2026-08-04  ESCALATING HELP (build aa): miss 1 = hint · miss 2 = new angle + worked
    board · miss 3 = shown warmly. Kept. · OFFICIAL LOGO · FUNNEL EVENTS · ROBOT FACE.
  - 2026-08-03  iPAD AUDIO FIX (one shared Audio element unlocked in the first tap) · the
    ten-level demo (one sample per course).
  - 2026-07-30  WARM VOICE via the /api/demo-audio/{i} whitelist + cache.
```

I did no harm and this file is not truncated.

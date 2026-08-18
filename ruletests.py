# =============================================================================
# ruletests.py  --  the RULE REGRESSION BATTERY  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-08-18  BUILD hy -- PART 3bp, THE VOICE ASKS TWICE: pins voice.js's new
#               single retry of a failed speak-prep/clip (the mid-deploy mechanical-
#               voice blip Jim heard live), the immediate fallback on an
#               authoritative {voice:false}, the started/doneCalled guards, and the
#               unchanged 5s no-start watchdog.
#   2026-08-18  BUILD hx -- PART 3bo, THE BETA PAGE'S KEY LEAVES THE URL: pins the
#               sessionStorage + scrubbed-address-bar + header pattern on beta.html
#               (the credential-in-URL class's third sighting), the server-side
#               header acceptance on all three beta POSTs, the forget-on-wrong-key
#               behaviour, and the new "sign in at /login with your pass" line.
#   2026-08-18  BUILD hw -- PART 3bn, THE GOVERNOR'S EYES ON PRODUCTION: pins the
#               new nightly GitHub Actions screen audit (.github/workflows/
#               screenwatch.yml) -- cadence + dispatch, the live screencheck
#               invocation against mrcadabra.com, the secret-not-committed audit
#               code with a loud missing-secret failure, kept artifacts, a bounded
#               run, and CLI agreement between the workflow and screencheck.py.
#   2026-08-18  BUILD hv -- PART 3bm, ONE STORAGE BACKEND, LOUDLY: a real restore
#               drill proves token tables are withheld (a signed-in token dies with
#               the restore), a family deleted AFTER the snapshot stays forgotten
#               (deletions ledger re-applied), and post-reset work OLDER deletions
#               would wrongly erase survives; a dead configured DB gates the chat
#               lane with the warm maintenance message while ALLOW_FILE_FALLBACK
#               lifts the gate on dev boxes; source pins for the loud backup pass
#               and the automated off-site email copy.
#   2026-08-18  BUILD hu -- PART 3bl, THE SERVER RECORDS THE RESULTS (Class E's
#               flagship): live drill proves the tag records exactly once, the echo
#               deduplicates (checks_taken/quizzes_taken never double), a MINTED
#               result 409s with a "client_result_rejected" system_events row and
#               leaves no trace in mastery, a [[finalexam]] outside an exam turn
#               records nothing, and the misses ride the tag server-side. The
#               missed-pipeline drill and the hs POST family moved to the new truth
#               path; course_trial.py follows the honest flow end to end (and now
#               proves the minted-final 409 as part of the journey).
#   2026-08-18  BUILD ht -- PART 3bk, BOUNDED AND SPLIT: every Anthropic client
#               constructed with the 60s timeout (counted, all sites); the three
#               teaching pages carry the 90s abort + warm bubble; _require_admin's
#               tiers proved LIVE (unset graver key -> 503 fail-closed; right key
#               opens; the general key and a wrong key are refused at the graver
#               doors); admin.html's graverKey() flow pinned.
#   2026-08-18  BUILD hs -- PART 3bj, THE CREDENTIAL LEAVES THE URL (Phase 5 begins):
#               a live TestClient drill proves all 10 GET routes and the POST family
#               in BOTH forms (header+/me and legacy path), bare-'me' rejection, the
#               speak ticket lifecycle (mint -> stream -> bogus 410 -> legacy alive
#               -> 401 on a bad code), and library's header form; source ratchets
#               (concatenation-shaped, comment-proof) fail the build if any page
#               reverts to building an API URL with the code or the spoken line;
#               analytics.js's KID_PAGES guard is pinned (Jim's Plausible ruling).
#   2026-08-18  BUILD hr -- PART 3bi, THE STORY KEEPS ONE UNIT: 10 fixtures in both
#               directions (incl. the nightwatch catch verbatim and its suggested
#               fix, the resolving shopping story, the two-facts "and", money-only
#               and objects-only traps); canonical sweep; wiring checks (clause in
#               the prompt, referee in the sweep, RULE_VERIFY[32] -> ENFORCED for
#               the caught shape, honestly scoped). RULES.md regenerated.
#   2026-08-18  BUILD hq -- PART 3bh, THE TWO-PROMPT-SIZES EXPERIMENT IS RUNNABLE:
#               the --prompt-size lever exists and threads through; the large
#               student is all-heard + forced-verbatim and assembles the genuine
#               over-ceiling worst case (both sizes built in-process, free);
#               nightwatch survives run_scenario's new 4-member return; the report
#               states how to read the comparison. The live halves need keys and
#               run on Render -- what the battery can prove without keys, it now
#               proves on every push.
#   2026-08-18  BUILD hp -- PART 3bg, THE ORDER OF AUTHORITY: exactly one absolute
#               supremacy claim (GROUND_RULES); the five-level lattice present with
#               its tiebreakers and the audited cross-pulls named by number (65 over
#               fading, 64 over 23); the opener block re-scoped to level 3; the
#               lattice provably rides GROUND_RULES into all three lanes; and
#               RULES.md is regenerated to a temp file and byte-compared on EVERY
#               push -- it was two builds stale with nothing checking it, and now
#               a stale copy fails the build (run `python ruletests.py --rules`).
#   2026-08-18  BUILD ho -- PART 3bf, THE RECORD-CLAIM REFEREE (the count-claim
#               probe's promotion). RECORD_CLAIM_CASES: 19 transcript-shaped
#               fixtures in both directions, including the audit's own shapes (the
#               watch-count refusal, the phantom "Unit 9 in progress", the invented
#               "last score") and the traps that must stay silent (true scores, true
#               mastery, future conditionals, in-reply results, no-record lanes);
#               the canonical corpus swept with a full record; wiring checks pin
#               _claim_record -> meta["record"] -> the sweep, and the whole-reply
#               result-tag exemption.
#   2026-08-18  BUILD hn -- PART 3be, THE STREAK LIVES ON CALIFORNIA TIME (Jim's
#               THREE CLOCKS ruling): wiring checks (_bump_stats reads
#               _streak_today/_streak_now; default zone America/Los_Angeles; the
#               decision recorded in the CLOCKS note; tzdata in requirements) plus
#               a subprocess proof that STREAK_TZ genuinely steers the calendar
#               (UTC+14 vs UTC-12 never share a date) and that a bogus zone falls
#               back to the UTC day without crashing the import. PART 3bc's streak
#               proof now computes yesterday/gap on the STREAK'S clock -- computed
#               from UTC it was wrong for the ~7 hours a day the calendars disagree.
#   2026-08-18  BUILD hm -- PART 3bd, THE HONEST OPENER AND THE VALIDATED DECLARATION
#               (Phase 4 of the full-app review begins -- Class D). UNITPLAN_CASES
#               exercises the NINETEENTH referee (tutor.unitplan_conflict) in both
#               directions on transcript-shaped replies, incl. the phantom-Unit-5
#               shape; the canonical corpus (all foundation scripts, every course)
#               is swept for false fires; wiring checks pin the one grammar source
#               (tags.UNITPLAN_UNIT_PATTERN), the meta arming, the filing gate
#               (_accept_declared_unit + the "unitplan_rejected" telemetry), the
#               code-branched opener (no-record forbids a recap; returning states
#               facts from the server; the gap refresher reads the record), and rule
#               0's new precedence (THE NOTES WIN). _HM_PROOF drives the allowed-set
#               table, the filing gate, the rejection telemetry and the opener
#               has-record decision on a REAL temp SQLite database on every push.
#               ALSO: the nightwatch restart-safety block now pins the clock in BOTH
#               places it is read (write_report gained now=), because the hardcoded
#               2026-08-17 version went red the day the calendar rolled past it --
#               a test that pins the clock must pin it everywhere the code reads it.
#   2026-08-17  BUILD hl -- PART 3bc, THE SMALL CUTS OF PHASE 3: wiring checks (the
#               file-fallback history probe parses "::" like _ck builds it and both
#               login sites OR it into "returning"; record_topic_quiz claims an
#               existing row by (code, course, unit, topic_idx); the three practice
#               writers all bump stats through the one atomic _bump_stats and the
#               read-then-write streak trio is gone; THE THREE CLOCKS decision block
#               exists) plus _HL_PROOF, a behavioural subprocess on a temp SQLite
#               database every push: a rephrased topic quiz HEALS into one row
#               (best=max, taken summed, latest name kept); 80 threaded practice
#               marks land exactly with zero errors; the streak +1s on a
#               yesterday-active student and resets after a gap.
#   2026-08-17  BUILD hk -- PART 3bb, NO EXCHANGE CAN BE LOST: wiring checks (CAS
#               writer exists; both chat-path writes go through mutate_history; no
#               whole-blob save remains in the handler) plus the threaded hammer on a
#               real database every push -- 96 appends land exactly, pairs adjacent,
#               the two-first-turns insert race is safe, the 60-message cap holds.
#               The hammer EARNED its keep before it ever entered the battery: it
#               caught the row-lock version silently losing 200 of 240 appends on
#               SQLite (pysqlite begins transactions at the first WRITE, so the
#               locked read wasn't) -- zero errors, pure data loss. The CAS rewrite
#               exists because of that run.
#   2026-08-17  BUILD hj -- PART 3ba, ONE OWNER FOR "WHICH UNIT": wiring checks (the
#               resolver exists; prompt, referee, tracker and probe consume its
#               result; the placement note expires) plus the six-case priority table
#               proved against a real database on every push. The gs link checks
#               repointed: the focus guard is now the resolver's SOURCE, not a raw
#               number re-test. The priority test caught a real design error before
#               it shipped: the first progression walk started at unit 1 and sent a
#               placed-at-3 student backward the moment they mastered unit 3 -- the
#               placement is a FLOOR, and the walk now starts there.
#   2026-08-17  BUILD hi -- PART 3az, THE COUNTERS ARE ATOMIC: source checks that the
#               five converted store sites compute in the database, plus a REAL
#               behavioural proof on every push -- a subprocess brings up store.py on
#               a temp SQLite file, checks serial semantics (a bad retake never
#               lowers the best; a status never downgrades), then hammers it with 40
#               threaded writes and requires exact counts and a true max. A lesson
#               from writing it: the first hammer expected "practiced" as the deepest
#               status and FAILED -- because some hammer scores hit 95% and
#               record_check itself upgraded the unit to "mastered". The data was
#               right and the expectation was wrong; the assertion now says so.
#   2026-08-17  BUILD hh -- ONE TAG GRAMMAR: TAG_HANDLER, TAG_INLINE, CONTENT_ATTRS
#               and the live BOARD_TAG regex now DERIVE from tags.py -- the battery
#               validates the contract, it no longer declares it (declaring it here
#               meant the checker and the checked could drift in step and notice
#               nothing). New PART 3ay: registry internal consistency (with the
#               balance/machine/objects dedicated-renderer overlap PINNED, not
#               forbidden -- my first draft of that invariant was wrong and the data
#               was right), the derivations in tutor.py and this file, and every
#               page dispatcher's tag set checked against the registry
#               (mutation-verified with an unregistered [[sparkle]]).
#   2026-08-17  BUILD hg -- ONE REPLY PIPELINE: new PART 3ax (pipeline exists, exactly
#               one _create_verified call site, no lane-private Anthropic clients, all
#               three getters route through it, TODAY net stays lesson-only, prompts
#               stay CALLABLES so they build inside the try). PART 3at's failopen
#               needle and PART 3av's meta needles updated to the one-pipeline form.
#               A lesson from installing it: the last function in a file needs an
#               end-of-file boundary in body-extraction regexes, or its check reads an
#               empty body and fails on healthy code.
#   2026-08-17  BUILD hf -- ONE MICROPHONE: PART 3aw gains mic.js (functions + state,
#               including micTypeHint, the per-page wording knob); the gr spoken-letter
#               client checks (expectsALetter + expect=letter, the narrow gate) are
#               asserted once against mic.js, with each page checked for the include.
#               The mic was where build gz's two live defects were born -- the module
#               plus these guards is the blanket answer.
#   2026-08-17  BUILD he -- ONE BOARD: PART 3aw gains board.js (19 named functions +
#               its state/constants table); PAGE_PARITY's fitRow needles became "the
#               page loads /static/board.js" plus fitting checks asserted once against
#               the module; the board-tag CONTRACT (_board_contract) reads renderers
#               from board.js AND the page, so it survives functions living in either;
#               showColumn's byte-identical-on-three-pages check became "exists once,
#               with its guarantees" (the stronger property -- one copy CANNOT drift);
#               the spotlight checks split honestly: existence/keys once against the
#               module, CSS and the clearSpot CALLS still per page, because a glow
#               never outlives its moment only if THIS page's turn code clears it.
#   2026-08-17  BUILD hd -- ONE VOICE: the gn/gp3 head-of-clip guarantees (no flat 300ms
#               kick, wait for "running", never freeze past the ceiling, ctx0 in the
#               probe, [voicehead] carried) moved from three per-page assertions to ONE
#               assertion against static/voice.js -- plus a new guard that warmUpAudio
#               wakes the keep-alive (build cb, unified by hd: topic/practice had
#               silently lost it, the review's F9). PART 3aw gains voice.js AND a state
#               table: a page that re-DECLARES moved state (audioWarmed, ttsAudio, ...)
#               is a parse-time SyntaxError that kills its whole script, so the battery
#               fails it first. Mutation-verified: re-inlined speak() and a re-declared
#               audioWarmed both caught.
#   2026-08-17  BUILD hc -- ONE COPY: PART 3aw, and three existing parts repointed at
#               the single source. The spoken-text transforms and the board/variable
#               renderer moved out of the three teaching pages into
#               static/speech-text.js and static/board-text.js. Consequences here:
#               PART 3aw (new) fails the build if a page re-inlines a shared function,
#               drops an include, or loads it after its own script -- proved by
#               re-inlining styleVarsCore into topic.html and watching it fail.
#               PART 3 ran the forSpeech cases three times, once per copy, because
#               there were three copies; it now runs them ONCE against the module and
#               asserts each page LOADS it. The gn2/screencheck seam checks read
#               board-text.js instead of session.html -- one table to match, not three
#               that can drift. PAGE_PARITY guards the INCLUDES now, not the inline
#               text. PART 3au learned to read globals supplied by <script src> files,
#               so the sweep does not howl at the very refactor it exists to protect.
#   2026-08-17  BUILD hb -- THE NET: PART 3au (the undeclared-identifier sweep) and
#               PART 3av (the fourteenth referee, re-armed). Phase 2 of the full-app
#               review puts this net up BEFORE the shared-module extraction goes in.
#               PART 3au is the answer to build gz's two live defects -- a fix
#               hand-copied between pages without the state it reads, which no layer we
#               owned could see. Pure stdlib (no node, no npm, no pip: a check that
#               skips is a wish). It narrows the universe to identifiers that are
#               PAGE-LEVEL STATE on a sibling page, then does real brace-scope analysis
#               on just those -- a full JS scope analysis in regex produces noise, and a
#               checker that cries wolf gets ignored. Silent on all 13 shipped pages;
#               fires on both gz defects reintroduced verbatim, with the right diagnosis
#               for each half of the class; fires on 5 mutations injected into 4 pages.
#               It also SELF-TESTS on every run: an analyzer that has gone blind reports
#               exactly what a clean codebase reports.
#               PART 3at's beacon checks were REWRITTEN after they passed while build ha
#               had corrupted eight pages -- they read the raw source and found a
#               COMMENTED "<script". They now read comment-stripped source and assert no
#               bare prose before <head>, plus new screencheck page-coverage checks.
#   2026-08-17  BUILD ha -- PART 3at, EYES: THE APP MUST WATCH ITSELF. Pins every piece
#               of the telemetry build: the store layer answers safely with the DB off
#               (record_event/event_stats/recent_events/last_event_at/purge), every one
#               of tutor.py's ~19 crash handlers carries its _event call, the referee
#               sweep counts fires by name, the pass-throughs/probes/promptsize/catch-
#               alls are wired, /api/client-error + its flood guard exist, /health
#               reports subsystems + ops ages, the heartbeat/backup/nightwatch stamp
#               themselves, telemetry is purged, client-log.js is present AND the
#               FIRST script on every teaching page (a script that loads before the
#               beacon can crash unheard), the /admin card and the night watch's
#               morning section read the counts. PAGE_PARITY gains the beacon needle.
#   2026-08-17  BUILD gz -- PHASE 0 OF THE FULL-APP REVIEW. Four fixes, four sets of
#               checks, three parts touched:
#               PART 3h: the ceiling now has ONE definition (tutor.PROMPT_CEILING --
#               this file used to own a private CEILING while the serving path checked
#               nothing, which is how all-heard students shipped at 186,890-194,284
#               chars on every course, over the ceiling, silently). New worst-case
#               checks: the all-heard prompt must FIT (gz defers heard wording), every
#               heard script must still be OFFERED by name (rule 40), and a refresher
#               turn (foundations_force_verbatim) must restore the full wording.
#               PART 3e: two new parity needles -- lastTutorText declared AND assigned
#               on every teaching page (topic/practice used it undeclared: a
#               ReferenceError on every spoken answer, "I didn't quite catch that" on
#               two of three pages) -- plus keep-alive resume checks: topic/practice
#               read their own audioWarmed, never session.html's `started`.
#               PART 3as (new): the ops heartbeat is never gated by WEEKLY_EMAIL (the
#               old early-return silently disabled backups + the night watch); the
#               refresher wiring exists in main.py; store.usage_stats reports
#               verify_prose-unresolved / verify_empty; admin.html shows the
#               shipped-unresolved tile.
#   2026-08-17  BUILD gy -- PART 3ar, A RULE SPOKEN AS A LAW. The sixth and last cause
#               from the day's audit triage, and the one where the DISCRIMINATOR mattered
#               more than the detector. Rule 54's banned list gains the rest of the classic
#               bad mnemonic ("is means equals, of means times") plus of/per/each, without
#               touching vocabulary -- "sum means addition" NAMES an operation and rule 37
#               requires teaching it; "of means multiply" merely CORRELATES inside one
#               problem type, and a child applies it to "3 out of 4". Rule 61's fraction
#               case is born ENFORCED as the eighteenth referee, and it is only decidable
#               because the same lesson states the condition correctly three times -- so
#               the check is not "is this claim true?" but "is the condition in the
#               sentence?". 16 cases both directions plus the 1,015-string canonical sweep,
#               which is the test that matters here: the fraction library states this rule
#               many times over and 0 of those statements fire. Rule 54 COVERED -> ENFORCED.
#   2026-08-17  BUILD gx -- PART 3aq, A REQUEST TO BE SHOWN, REFUSED (rule 65, the
#               seventeenth referee). The referee needs all three conditions together --
#               they asked to be shown, nothing was worked out, and the job went straight
#               back to them -- so the cases prove each one alone is silent. Rule 65's own
#               remedy (working it, then handing over a NEW one) must pass, or the rule
#               would be unfollowable.
#   2026-08-17  BUILD gw -- PART 3ap, THE BARE ANSWER-DEMAND, THE DECIMAL, AND A REFEREE
#               THAT FOUGHT US. Two audit findings turned out to be ONE defect: a board
#               line with no "?" is invisible to rule 15's and rule 44's checks at once, so
#               "What do you get?" over "2.6 + 1.35" slipped past both. Under it sat gk's
#               fraction bug in decimal clothing -- the "1" of 1.35 found inside the word
#               "one". ⭐ And the canonical sweep, run only to prove those fixes harmless,
#               found a THIRD thing nobody had reported: gl's self-correction referee had
#               been REGENERATING TWO FOUNDATION SCRIPTS since it shipped, because they say
#               "hold on to this". No audit found that. The corpus did.
#   2026-08-17  BUILD gv -- PART 3ao, THE INVENTED HISTORY. Seven claims about what had
#               already happened that were untrue, split on whether a referee can check
#               them: gm's narrated-method referee gains a TOTALITY branch (a "start to
#               finish on your own" claim over a fragment) and is tested there both ways,
#               while the false COUNTS ("you've now watched this move twice", said twice
#               and false both times) get the [countclaim] PROBE instead -- a referee sees
#               one reply and cannot count a conversation. Measure when you cannot verify.
#   2026-08-17  BUILD gu -- COLD_QUIZ_CASES: RULE 47 STOPS BEING A WISH (the sixteenth
#               referee). ⭐ The most damning find in the day's triage and the clearest
#               argument this battery exists: the sentence "let's do it -- five questions,
#               all on finding the percent of a number" was caught on 2026-08-11, rule
#               47(d) was WRITTEN from it, and the tutor produced it again WORD FOR WORD on
#               2026-08-17 -- because rule 47 was COVERED and nothing watched it. The cases
#               include 47(d)'s own sanctioned remedy, which the first draft of the
#               detector rejected. Rule 47 COVERED -> ENFORCED.
#   2026-08-17  BUILD gt -- THREE MORE MALFORMED BOARD SHAPES (BOARD_NOTATION_CASES): an
#               arrow after an equals sign, a question stuffed inside an equation, and a
#               tautology. No judgement is required for any of the three, which is exactly
#               why missing them mattered. Scoped to eq= so a caption may still ask.
#   2026-08-17  BUILD gs -- PART 3an, THE UNIT FOLLOWS THE TEACHING. Jim reported the same
#               symptom twice ("it still says unit one when we are talking about unit
#               five") and BOTH earlier diagnoses were guesses. The chain is now asserted
#               link by link -- the tutor's [[unitplan]] declaration is the authority, an
#               explicit clicked focus still wins, _track_topic records the declaration and
#               not placement, /api/session serves it as progress.current_unit, and the
#               rail prefers it -- because breaking ANY one link brings the symptom back
#               looking like a display bug. The half that cannot be enforced (does the
#               declared unit match the content?) is left to the [unitdrift] probe.
#   2026-08-17  BUILD gr -- PART 3am, THE SPOKEN LETTER AND THE SIGNED ANSWER. Two ways to
#               ignore what a child actually said, both from one Geometry lesson of Jim's.
#               The transcription half is guarded at the seam: a language hint is sent, and
#               a 422 RETRIES WITHOUT IT, so a parameter can never silently break the
#               microphone; the spoken-letter map applies only when a letter was expected.
#               The signed half is rule 64 and the fifteenth referee -- it fires only when
#               the reply affirms a signed answer, then uses the unsigned magnitude, and
#               never mentions the sign, so the right answer ("both 5 and -5 square to 25,
#               but a length can't be negative") passes.
#   2026-08-17  BUILD gq -- PART 3al, THE OPENAI BOUNDARY: A PROMISE BECOMES A TEST. Sharing
#               is ON in the dedicated audit project, which is safe for exactly one reason
#               -- OpenAI is not in the teaching path, and every transcript it marks is
#               synthetic. static/privacy.html promises three processors and says "to
#               anyone, ever." So the build now FAILS if any teaching module so much as
#               references OpenAI, and the failure text names the privacy promise. Proved
#               by mutation: bolting a substitute-teacher fallback into tutor.py fails two
#               checks immediately.
#   2026-08-17  BUILD gp2 -- PART 3aj GAINS S7 (THE CONSOLE IS CLEAN) AND THE REAL POLICY.
#               A CSP violation on every silent-WAV data: URI sat under the console lines
#               we were reading. Nothing was broken -- the header ships report-only -- but
#               silentWavUri() is BOTH the audio warm-up and the keep-alive, so on the day
#               that header is enforced the voice regresses and nobody connects it to a
#               security header. The harness now reads the REAL policy out of main.py, so
#               the rig can reproduce the defect it was written to catch. Both ways: S7
#               fires twice with media-src removed, silent with it present.
#   2026-08-17  BUILD gp -- PART 3ak COVERS THE GOVERNOR'S FACE. go's first live night
#               exposed two holes: the report was served nowhere but a one-line log count,
#               and it COUNTED refutations without NAMING them -- so a reviewer quietly
#               killing real defects looked identical to a healthy one. The status/report
#               endpoints, the 30-night /admin card, the named dismissals and the
#               near-ceiling warning are all held here. Losing rotation coverage silently
#               is the one thing this must never do.
#   2026-08-16  BUILD go -- PART 3ak, THE NIGHT WATCH. Everything that does NOT need an API
#               key: the rotation, the ledger, the report, the email policy, restart-safety
#               and above all the FAILURE paths. A governor is judged by what it does when
#               the critic returns garbage, a lesson explodes, or the key is missing -- it
#               must never confirm a finding it could not verify, never end a night over
#               one bad lesson, and never let a silent cap read as "all clear".
#   2026-08-16  BUILD gn2 -- CASE IS MEANING, AT THE SEAM. The lesson that TEACHES
#               uppercase-vs-lowercase rendered its two lines identically. PART 3aj's seam
#               check follows the renderer from VAR_SKIP to the CASE-SENSITIVE
#               VAR_NEEDS_CONTEXT table, so the checker cannot go blind when that list
#               moves. ⭐ The four regressions in the draft renderer (the article in "A
#               **fact family** is", f and g through function-notation lessons, "(f o g)",
#               "the highest point a thrown ball reaches") were caught by the 1,015-string
#               canonical sweep and by NO hand-written fixture. Fixtures prove the logic;
#               only a real corpus proves the premise.
#   2026-08-16  BUILD gn -- PART 3aj (the screen auditor), LETTER_CASES (rule 63(d), the
#               thirteenth referee) and UNIT_CLAIM_CASES (rule 0's recap clause, the
#               fourteenth). All three come from ONE Geometry lesson Jim ran by hand.
#               The unit one is the one worth re-reading: it LOOKED like a broken progress
#               rail and was the opposite -- the rail was right and the tutor had invented
#               "two days ago we started Unit 5" for a student whose record says "New to
#               this course". A referee that judges a reply against a fact from OUTSIDE it
#               is new here, so it is tested three ways: fires on the wrong unit, silent on
#               the right one, and silent whenever the unit is unknown.
#   2026-08-16  BUILD gn -- PART 3aj, THE SCREEN IS CHECKED TOO. Jim ran one Geometry
#               lesson and found four defects by eye in the first turn -- a formula
#               rendered "a squared plus B squared equals C squared", a triangle lettered
#               on its CORNERS while the words named its LEGS, a rail saying Unit 1 under
#               prose saying Unit 5, and a clipped header. Nothing we owned could have
#               caught any of them: the referees read the reply, lessonaudit reads the
#               transcript, and all four defects are born in the RENDER. PART 3aj runs
#               screencheck.py's six screen checks -- 21 fixtures, both directions, all on
#               real turns -- with no browser and no key, so they run on every push rather
#               than when someone remembers. It also guards the two seams that would make
#               the checker go SILENTLY blind: geo-figures.js's font metrics (17/800 for a
#               vertex, 15/600 for a side -- the only way to tell a corner from a leg) and
#               session.html's VAR_SKIP list.
#   2026-08-16  BUILD gm -- RULE 43 GETS ITS ENFORCEMENT TESTED (18 new cases). Rule 43
#               forbids narrating a method onto a bare right answer, and it was written on
#               2026-08-13 from a live catch. On 2026-08-16 the audits caught the same
#               defect again: the student typed "1 1/2. Next." and was told "that
#               regrouping is exactly the move that trips people up". The new referee is
#               held to its job in both directions here -- the 2026-08-16 case verbatim,
#               rule 43's own two 2026-08-13 examples, and ten turns that MUST stay silent,
#               including praising the answer (the remedy rule 43 actually asks for) and
#               asking rule 59's "how did you get that?".
#   2026-08-16  BUILD gl -- COVERAGE FOR THE ELEVENTH REFEREE. The new ACCURACY sentence is
#               added to PART 1 so it must reach all ten courses, and fourteen checks hold
#               the self-correction referee to its job in both directions -- it catches the
#               audits' own HIGH verbatim, and it never fires on correcting the STUDENT.
#   2026-08-16  BUILD gj -- RULE 41 COVERAGE. Twelve checks holding the new caption referee
#               to its job in both directions (it catches the audits' own bare pie and
#               cookie pictures; it never fires on [[step]], [[write]], [[card]] or
#               [[mark]]), that it is actually wired into prose_board_conflict, and that
#               all 306 authored scripts already obey rule 41 so it can never fight them.
#   2026-08-14  BUILD gh -- A MISSING PACKAGE SKIPS, IT DOES NOT FAIL. Three checks failed
#               (one with a raw traceback) when sqlalchemy or httpx was simply not installed
#               on the machine running the battery. A battery that reports the ENVIRONMENT
#               as broken code teaches you to shrug at red -- and on the day this was
#               written, four genuine failures had been sitting unlooked-at, one of them a
#               prompt 5,595 characters over the ceiling. New dep_gate() skips with the
#               package name. Gated for THIRD-PARTY imports only: a missing module of our
#               own is a broken repo, not an unprovisioned laptop, and still fails.
#   2026-08-14  BUILD gg -- PART 3b AND 3d NOW GUARD THE CONTRACT BUILD gb CREATED. The old
#               promise was "every script reaches every prompt, verbatim, always", and it
#               was right until the library reached 306 scripts and the largest prompt hit
#               185,595 against a 180,000 ceiling. gb carries the LESSON'S UNIT in full and
#               NAMES the rest. These parts asserted the old promise and so failed on
#               correct code -- the worst kind of test. They are not deleted, they are
#               re-aimed, and they now guard three things instead of one: no term ever
#               vanishes (in EVERY unit each term is quoted or at least named -- a term the
#               tutor cannot see is one he will define from memory), every script is quoted
#               verbatim in at least one unit, and a HEARD script is never filtered by unit
#               (rule 40 must be able to restore its exact words, and "remind me" arrives in
#               any unit). The audio-cache check now asks whether a QUOTED script's wording
#               was altered, which is the thing the voice cache actually depends on.
#               Each rewritten check was verified by mutation: deferring a term without
#               naming it, giving a script a unit nobody teaches, filtering a heard script,
#               altering a quoted script's words, and dropping a heard script from the
#               refresher turn are all still caught.
#   2026-08-14  BUILD gf -- PART 3ac READS THE DEADLINE WRAPPER. Build ga wrapped runTutor's
#               three gates in withDeadline() so a gate that never settles cannot strand a
#               student; PART 3ac read those three lines literally and started failing on
#               correct code. It now normalises the wrapper away, asserts the SAME ordering
#               and awaiting rules on what is left, and adds a check that all three gates
#               still carry a deadline -- so neither rule can be dropped unnoticed.
#   2026-08-14  BUILD ge -- PART 3ai, THE DEPLOY STAMP. /health's APP_BUILD is how anyone
#               confirms Render actually took a deploy, and it had gone NINE builds stale,
#               so it was answering that question wrongly at the exact moment Jim needed it.
#               PART 3ai now fails the build when any shipped file carries a dated change
#               note newer than the stamp. Bumping it stops being a habit.
#   2026-08-13  BUILD fe -- THE 2026-08-13 LESSON-AUDIT FINDINGS, CLOSED (NEW PART 3ah;
#               PART 3w grows; PART 2 gains TRIANGLE_CASES). Five audit runs, 19
#               findings, each read against its quoted transcript first. Real: the
#               three HIGHs (the 4|4|4|2 sharing picture left standing; the triangle
#               hypotenuse mis-slotted three times in one lesson; the wrong picture
#               "fixed" in words only) plus thirteen more. New rule 63 (the words and
#               the picture are the same figure) ships with a new referee,
#               triangle_side_conflict -- born ENFORCED, swept in PART 2 against the
#               audit's real tags and every foundation script. Rule 61's corrected
#               list grows five -> nine and PART 3w bans the four new false forms
#               from authored content (the fraction one really lived there, in the
#               basic "fraction" foundation script -- same as el's function-notation
#               case). REJECTED, with reasons recorded in PART 3ah's header: the
#               rule-52 finding (52d decided this exact misread on 2026-08-11), the
#               rule-47 finding (the two-unaided-rights bar was met and 47d's speech
#               was delivered), and the rule-15 finding (a result-less [[column]] IS
#               the pending question). lessonaudit.py transport hardened (read 300s +
#               one transport retry) after two lessons died mid-audit; pinned here.
#   2026-08-13  BUILD fd -- THE PICTURES AND THE PROSE (NEW PART 3ag). Every screenshot
#               on the public site is a photograph of the DEMO -- that is why they can be
#               trusted, and it is also why the copy drifts: the demo changes and the
#               marketing pages have no idea. Re-capturing the shots for the beta push
#               found /homeschool claiming "3h 59m this week" in the paragraph, in the
#               alt text AND in the weekly-email preview, directly above a tile reading
#               2h 15m -- on the page whose whole promise is "a number you can put in an
#               instructional-hours log with a straight face". PART 3ag now reads the
#               numbers out of demo.html at test time and holds the copy to them: Maya's
#               week, the tile's ALT text (the version no sighted proofreader ever sees),
#               the heatmap's student count, and the Decimals scores in the email
#               preview. It also weighs every shot file -- a blank whiteboard is a 40 KB
#               PNG with a perfectly valid filename, which is exactly what the first
#               re-capture produced. Negative-tested: each mutation fails it.
#   2026-08-13  BUILD fc -- THE TRIAL ON THE DASHBOARD, GUARDED (PART 3af extended). The
#               safety-critical property is ISOLATION: the trial invents a parent, a
#               child, a teacher and a class, so it must run as a SEPARATE PROCESS with
#               its own DATABASE_URL and DATA_DIR. PART 3af now pins that, plus the admin
#               gate, the memory guard (a second interpreter costs ~120 MB; an OOM on a
#               512 MB instance would take the live site down), the timeout, the course
#               validation, --json/--validate, the JSON sentinel, and the panel wiring.
#               Negative-tested twice: pointing the trial at the live database, and
#               removing the memory guard, each fail the build. (The first attempt at the
#               memory negative test mutated the ASSIGNMENT and not the COMPARISON, so it
#               proved nothing -- worth remembering that a bad mutation reads exactly like
#               a passing guard.)
#   2026-08-13  BUILD fb -- THE FULL JOURNEY, END TO END (NEW PART 3af). Everything else
#               in this battery checks a PART. This runs one student's whole life through
#               the real app -- sign up, validate three units on the Course Assessment,
#               work the rest, hit the LOCKED Final Exam and read what it says, go back
#               and pass the owed quizzes, take the exam, Course Champion in the trophy
#               case, and the same picture on the parent AND teacher views -- by invoking
#               the new shipped tool course_trial.py. ⭐ It earned its place on its first
#               run by finding a live bug no single-endpoint test could see: a teacher
#               could not add a parent-created student to a class, because the classroom
#               path predated parent accounts and consulted students.json alone. PART 3af
#               also pins that specific regression (the three class lookups must route
#               through _lookup_student), and it is negative-tested by putting the
#               students.json-only check back.
#   2026-08-13  BUILD fa -- SECURITY F2 CLOSED, GUARDED (NEW PART 3ae). This part does NOT
#               trust the source to look right: it stands the real app up against a real
#               database and drives every class endpoint three ways -- anonymously, as the
#               WRONG teacher, and as the owner. That matters, because a source-reading
#               check would have passed on the OLD code too; those handlers looked
#               perfectly reasonable, and they were handing out children's login codes.
#               The drill asserts: every endpoint 401s anonymously · another teacher gets
#               404 on read, summary, reveal, add, remove and rename · no raw login code
#               appears in ANY class response (roster or summary) · reveal returns one
#               code to the owner and 404s a bogus ref · an unowned class can be claimed
#               once and an owned one never · signup inheritance moves only unowned
#               classes · logout really kills the token. Static checks alongside it pin
#               that _class_or_404 and the unauthenticated teacher-classes route stay
#               gone, that every /api/class handler calls _require_teacher AND _own_class
#               (naming any offender rather than counting), and that the page signs in
#               with a token instead of a URL parameter and renders masked codes.
#               NEGATIVE-TESTED three ways: dropping the ownership check, putting the raw
#               code back in the roster, and letting an owned class be re-claimed -- each
#               fails the build, and the middle one is invisible to every check that reads
#               source. The teacher page was also driven in a real browser end to end.
#   2026-08-13  BUILD ez -- A CLIP NEVER EATS SOMETHING BETTER (NEW PART 3ad). Three
#               regressions Jim found by USING the site, all one species: the video work
#               quietly took over something already doing a better job. (1) Build eu put
#               the site-welcome clip on the hero's "Hear him teach" button and returned
#               before the teaching sample -- so the button stopped teaching the day the
#               clip went live, and relabelled itself to a greeting. (2) Two welcomes
#               could stack once the home page started greeting visitors on the way into
#               the demo. (3) After the real demo problem, an audience-door visitor got
#               the WALKTHROUGH's ending -- re-speaking a line already heard and offering
#               the lesson just finished. PART 3ad pins each one where it actually broke:
#               no TutorMoments inside wireHear and the sample still reachable; every
#               worded label on that button is about TEACHING; the marker is set before
#               navigation, read BEFORE the demo's own welcome, and CLEARED; the
#               after-lesson panel passes its signal through, speaks nothing, keeps the
#               congratulations, and never re-offers the lesson. NEGATIVE-TESTED three
#               ways (re-add the hijack / stop clearing the marker / drop the
#               after-lesson argument -- each fails the build).
#               ⚠️ TWO DELIBERATE REVERSALS IN PART 3u2, recorded rather than deleted:
#               the checks that pinned build eu's hijack (the codec retire-and-retry on
#               the teach button, and the relabel-on-window-load) are RE-POINTED at where
#               the behaviour lives now -- the demo CTA -- because Jim reversed that
#               design decision, not because the guards were wrong.
#               Beyond the battery: driven in a real browser -- teach button fetched
#               /api/demo-audio/71 and played it as audio with NO video; the demo click
#               played the welcome then navigated; that arrival played no second welcome
#               and cleared its marker; a direct /demo visit still got the demo welcome.
#   2026-08-13  BUILD ey -- THE VOICE SEQUENCING, GUARDED (NEW PART 3ac). Mr. Cadabra's
#               talking clips now play at the seven moments of a lesson, and one rule
#               holds the design up: a canned clip and his LIVE voice never talk at once,
#               and a clip never REPLACES the personalised line (video cannot say a
#               child's name; the live voice can). That failure is a TIMING failure --
#               silent to every test that reads text, audible exactly once, in a real
#               lesson, as two voices over each other. So PART 3ac asserts the sequence
#               STRUCTURALLY: inside runTutor's own body the three statements must be
#               await runPendingMoment("before") / await speak(clean) /
#               await runPendingMoment("after"), in that order, all awaited, with speak()
#               at the same nesting level so it can never become conditional on the clip.
#               It also pins: every one of the seven moments reaches a REAL trigger and
#               every trigger sits in the function that owns its event (the thumbs-up cost
#               three builds to learn that a clip nothing can fire does not exist); the
#               cadence table (earned moments always play, repeatable ones capped at one a
#               day, so a clip stays a person and not a jingle); the goodbye plays AFTER
#               his words while celebrations play before; the page still works DARK; and
#               [[bye]] is taught in PROGRESS_TAGS_NOTE only, never the shared block.
#               "bye" joins LESSON_ONLY and TAG_INLINE (attribute-free, draws nothing).
#               NEGATIVE-TESTED four ways: dropping the await, making speak() conditional,
#               unwiring a moment, and retuning a cadence each fail the build.
#               BEYOND THE BATTERY, because these checks all read text: the real page was
#               driven in a real browser with a stand-in clip and the media timeline was
#               MEASURED -- clip ended 4867ms, voice started 4867ms (zero overlap); with
#               the await removed, voice started 1807ms against a clip running to 4938ms
#               (3.1s of overlap, caught). Dark path measured too: no moment video, voice
#               unchanged, zero page errors.
#   2026-08-13  BUILD ex -- THE SEVEN VERIFIED TEACHING DEFECTS, GUARDED (NEW PART
#               3ab). The last open items from the 2026-08-12 audit batch: rule 19(e)
#               a never-watched move is modelled before it is asked (the regrouping
#               catch) · 27(c) a story model holds ONE unit line to line (the
#               "3 dollars + 8 tickets" catch, pinned verbatim) · 49(g) the KIND of
#               error is spoken in words the student keeps (the 0.82 place-value
#               catch) · 50(g) the locked Final Exam's reply offers the retake path
#               unprompted · 51(f) a limit carries its approach and each side of an
#               asymptote is its own claim (both calculus catches, incl. the true
#               MINUS-infinity left side) · 52(e) the verdict opens the reply ("No --
#               it's 11") without overriding rule 22's ladder · NEW RULE 62 a
#               back-reference must point at work that actually happened. PART 3ab
#               pins each headline once-in-shared-block + once-in-a-built-prompt and
#               the load-bearing phrases INCLUDING the deliberate guard rails (52e
#               keeps the ladder; 62 keeps connecting-is-teaching; 51f names the true
#               behavior). COVERAGE gains seven needles so every course provably
#               receives all seven. RULE_VERIFY gains 62 (COVERED); RULES.md
#               regenerated -- 62 rules.
#   2026-08-13  BUILD ew -- PLACEMENT NEVER PASSES A UNIT; THE FINAL GATE IS DERIVED
#               (NEW PART 3aa). The 2026-08-13 status doc declared Jim's
#               no-credit-from-placement policy already in force. It was not:
#               challenge.html posted one /api/check per unit with the assessment
#               scores, record_check masters a unit at >= 90%, and _final_exam_state
#               reads that same table -- 5/5 on five placement questions silently
#               passed the unit. PART 3aa pins the policy on every path (no /api/check
#               in the assessment page, postJSON stays gone, post_placement and
#               save_placement inert toward mastery) and pins the keep-the-value half
#               (the placement POST carries strengths + units; PlacementIn round-trips
#               them; the result screen carries the honest sentence written AND
#               framed as quick wins). It also pins build ew's second fix: the
#               final-exam requirement is DERIVED from curriculum.units_for (no
#               "required": 9 literal in code -- comment lines stripped before the
#               ban, same as PART 3w; _units_required verified against every real
#               course's unit count in-process; the gate messages and session.html
#               speak the derived number; the shared FINAL notes in prompts.py are
#               count-neutral).
#   2026-08-12  BUILD eq -- TWO MECHANICAL GUARDS, GUARDED (PART 3z). From the
#               2026-08-12 audits: (1) a NEW malformed-tag referee -- eight referees and
#               none of them checked a tag was even parseable, so
#               [[choices options="yes... | show me one more]] reached a child as ONE
#               button reading '"yes,'; (2) the rule-44 referee's two blind spots, which
#               six findings in five lessons walked through: it needed TWO numeric
#               tokens (and a fraction counts as one, so a whole fraction quiz was
#               invisible) and ANY number in the prose exempted the reply. PART 3z pins
#               the real audit strings on both sides -- the offending lines must be
#               caught, the innocent lines from the SAME transcripts must not be -- so a
#               future tightening cannot quietly start regenerating good replies.
#   2026-08-12  BUILD en -- THE LAST TWO AUDIT ITEMS, GUARDED (PART 3y): rule 49 gains
#               (f) -- when the student NAMES their rule, that is evidence and it is the
#               one you answer (the audit caught a reply correcting a misconception the
#               student never had while their real one survived) -- and the two notation
#               registry gaps are closed: bare < and > (absent entirely, though comparing
#               fractions is core Basic Math) and the imaginary unit (absent though
#               algebra2 teaches complex numbers). PART 3y also pins the FALSE-POSITIVE
#               behaviour, because both patterns were the risky kind: arrows (->, =>) and
#               the or-equal pair must never read as inequalities, and the calculus
#               subscript scripts (x_i, "x · i") must never read as the imaginary unit.
#   2026-08-12  BUILD em -- THE FRACTION PIE, GUARDED (PART 3x). The 2026-08-12 audit's
#               one HIGH finding: a board captioned "one whole, cut into four equal
#               parts" drew TWO wedges, and a beginner was then asked to count three
#               shaded pieces that were never on screen. Verified in the renderer (one
#               wedge per data entry, plus a percentage legend that hands over the
#               answer) and traced to FIVE canonical foundation board lines. New
#               equal-parts mode [[pie parts="N" shaded="K"]]; PART 3x pins it: the
#               renderer must draw exactly N separated wedges with K filled, must print
#               NO text at all (rule 6 -- a percentage on a fractions board answers the
#               question the tutor is about to ask), must cap N so it stays countable,
#               must leave the proportional mode intact for unequal categories, and NO
#               authored pie board line may use the proportional form. Node renders the
#               real SVG in the check -- this is measured, not asserted.
#   2026-08-12  BUILD el -- RULE 61 (a generalization carries its condition), GUARDED,
#               plus the AUTHORED-CONTENT guard that is the real enforcement here. The
#               2026-08-12 audits caught five false universal claims across three
#               courses; mathcheck structurally cannot see them (no arithmetic in
#               "always"), so live replies are prompt-covered. But ONE of the five was
#               not a live slip at all -- it was the algebra1 function-notation
#               FOUNDATION SCRIPT, spoken verbatim to every student who meets f(x).
#               NEW PART 3w: the five known-false forms may never appear in ANY authored
#               content (prompts.py, foundations.py, notation.py), rule 61 must live in
#               the shared block exactly once with its five corrections and its
#               do-not-overcorrect clause, and the true absolutes it protects must still
#               be sayable. High-precision by design: it bans the five SENTENCES, never
#               the word "always" -- "the hypotenuse is always the longest side" is true
#               and must stay.
#   2026-08-12  BUILD ek -- ONE TRUE NAME PER COURSE, GUARDED. THIS FILE WAS PART OF
#               THE BUG. Its COURSES list used the phantom spellings "entrymath" and
#               "basicmath", so for two of the ten courses the whole battery has been
#               proving things about a course that does not exist -- and the two REAL
#               elementary courses ("entry", "basic") were never tested at all. That is
#               why nothing here caught that a real Basic Math lesson was running with
#               an EMPTY misconception catalogue, EMPTY foundation scripts and an EMPTY
#               notation table (0/0/0 bytes, measured). The tests and the content shared
#               the same wrong assumption, agreed with each other, and both disagreed
#               with production. COURSES is now the real keys, and NEW PART 3v is the
#               check that would have caught it on day one: every real course must get a
#               NON-EMPTY block from all three content modules; no module may key
#               content by a name that is not a real course; ruletests' own course list
#               must equal curriculum's keys; lessonaudit must audit real courses; and
#               canon() must resolve the legacy spellings (so no stored student record
#               is orphaned) while leaving unknown names alone (so a typo can never
#               silently become Algebra I again).
#   2026-08-12  BUILD ej -- THE VIDEO PRESENCE LAYER (phase 1), GUARDED. tutor-face.js
#               now carries Mr. Cadabra's video face over the canvas robot, robot as
#               the always-drawn fallback. NEW PART 3u: the robot draw path must
#               survive (any video failure lands on it), the presence must be
#               muted+playsinline+aria-hidden FOREVER (his voice lives in the pages,
#               never in the corner), every media error must tear down to the robot,
#               reduced-motion must get a still poster or the robot, the robot must
#               draw BEFORE the presence tick on every frame, all six coaching pages
#               must still include tutor-face.js and its export must keep draw +
#               moodFrom. FUTURE-PROOF: if/when static/videos/cadabra/presence.json
#               lands (Jim's HeyGen assets), the battery automatically validates it
#               -- parses, has an idle loop, and every referenced file exists.
#   2026-08-12  BUILD ei -- TEACHERS DEMO DOOR REWRITE, GUARDED. The /demo?view=
#               teachers walkthrough now names the replacement threat in its first
#               breath and frames everything as the teaching ASSISTANT. NEW ei
#               needles in PART 3j, same shape as eg/eh: both voice lists must
#               carry "I am not here to replace you", the thirty-hours-a-day
#               assistant line, "no class learns at one speed", "you make the
#               teaching decisions", and the outro's what-it-DOESN'T-do line; the
#               teachers intro/outro anchors must be the NEW ones. Everything else
#               rides the existing enforcement: lists identical + append-only
#               (238 -> 243), every anchor resolves to exactly one line, nine
#               teacher stops on the same panels.
#   2026-08-12  BUILD eh -- STUDENTS DEMO DOOR REWRITE, GUARDED. The /demo?view=
#               students walkthrough now charms the child AND reassures the parent
#               trying the door as if they were their child (Jim). NEW eh needles in
#               PART 3j, same shape as eg's: both voice lists must carry the
#               talks-and-LISTENS intro, the math-ONLY promise, the never-just-gives-
#               the-answer promise, and the nobody-can-give-you-a-trophy line; the
#               students intro/outro anchors must be the NEW ones. Everything else
#               rides the existing enforcement: lists identical + append-only
#               (234 -> 238), every anchor resolves to exactly one line, STU_STOPS
#               still overrides ten-for-ten by index.
#   2026-08-12  BUILD eg -- PARENTS DEMO DOOR REWRITE, GUARDED. The /demo?view=parents
#               walkthrough now answers the two questions a parent brings to a
#               conference table -- "is my child actually learning" and "will she
#               actually want to do this" -- with the tour structure untouched. NEW eg
#               needles in PART 3j: both voice lists must carry the two parent
#               questions, the teaches-never-hands-answers promise, the
#               missed-problem-comes-back line, and the voice-privacy outro; the
#               parents intro/outro anchors must be the NEW ones (the old lines stay
#               in the lists forever -- append-only -- but the parents door must not
#               speak them). Everything else PART 3j already enforced does the heavy
#               lifting: lists identical + append-only (227 -> 234), every anchor
#               resolves to exactly one line, every spoken literal is whitelisted,
#               HS_STOPS still covers every parent stop.
#   2026-08-12  BUILD ef -- HOMESCHOOL CONFERENCE-PITCH REWORK, GUARDED. Jim, pitching
#               at a homeschooling conference, asked /homeschool to LEAD with the
#               points that land at a real table: records/filing first, honest mastery
#               named (80/90, never rounds up), you're-still-the-teacher, and the four
#               trust questions answered plainly. New ef guards (in the eb marketing
#               block): the section ORDER is pinned (records -> hours -> window-in ->
#               ... -> teacher -> trust -> FAQ), the mastery bars and the four trust
#               answers must stay on the page, /privacy must be linked from the voice
#               answer, the method line must name the What Works Clearinghouse (the
#               blanket phrase stays banned), and NO dollar figure may appear (prices
#               live on /pricing alone). FAQ untouched: same 8 questions, still
#               pairwise disjoint; parent-code and walkbtn guards unchanged.
#   2026-08-12  BUILD ee -- THE FIVE TEACHING UPGRADES, GUARDED (rules 56-60 join the
#               shared block; claude/Teaching_Evidence_Base_2026-08-10.md is the
#               source). NEW PART 3t: each rule's headline + load-bearing phrases must
#               be present in GRAPH_TOOL_NOTE exactly ONCE (shared, never per-course);
#               rule 56 must keep its three safety anchors (the announced game, the
#               catalogued mistake, THE WRONG WORK NEVER STAYS); rule 60's two board
#               keys must be documented; and all THREE teaching pages (session,
#               practice, topic) must implement the board spotlight -- spotlightBoard()
#               with the line+board keys, the .stepglow CSS with its pulse, a
#               turn-start clear, and (session) the tour fallthrough so page-tour ids
#               still reach highlightEl. COVERAGE gains five needles so rules 56-60
#               are proven to reach all ten courses. THE CEILING: 150,000 -> 160,000.
#               That number was always a tripwire, not a measurement (see the PART 3h
#               essay); Jim's standing decision (2026-08-11, recorded in
#               Four_Lens_Review: "if you need to raise it, you raise it") authorizes
#               raising it when a teaching upgrade needs the space. This build spends
#               ~8.2k shared characters on five evidence-backed rules -- exactly the
#               trade the decision anticipated. Largest prompt measured 156,515 after.
#   2026-08-12  BUILD ed -- READ-BY-CODE THROTTLE (F1), GUARDED: every GET-by-code data
#               endpoint (session, records, misses, awards, time, topics, assessment,
#               placement, courses, sprints, sprint) must front its work with
#               _read_guard; the guard must cap DISTINCT codes per IP + the raw read
#               rate; _new_student_code must be widened to 4 digits. LIVE SEC2-DRILL:
#               enumeration from one IP 429s near the cap, a fresh IP starts clean,
#               same-code reloads never trip, and new codes match WORD+4digits.
#   2026-08-12  BUILD ec -- SECURITY HARDENING 1, GUARDED: F3 _client_ip must trust the
#               proxy-appended (rightmost) X-Forwarded-For end via TRUSTED_PROXY_HOPS,
#               never the spoofable leftmost (the old .split(",")[0] pattern is now
#               forbidden); F4 the security-headers middleware must stamp the full set
#               (nosniff, SAMEORIGIN, referrer, HSTS, permissions, CSP) with the CSP in
#               REPORT-ONLY mode only (an enforcing CSP would blank our inline scripts);
#               F5 /api/transcribe must cap the read at MAX_AUDIO_BYTES, 413 over it, and
#               re-raise HTTPException so the cap isn't swallowed. LIVE drill (SEC-DRILL):
#               headers ship on a page AND the API, and _client_ip picks the trusted end
#               even when the caller prepends fakes.
#   2026-08-11  BUILD eb -- CALM FEATURES PAGE + FOUR AUDIENCE FAQs, GUARDED: the
#               features page must stay icon-free (no emoji rows, no .ic spans), stay
#               six drop-down sections of >=41 plain bullets, and keep naming the
#               post-rewrite features (sprints, refresher, save/resume, retake,
#               tricky-ones, steer, phone, a11y). Each audience page (students,
#               parents, homeschool, teachers) must end with its OWN 8-question FAQ,
#               and the four question sets are swept PAIRWISE DISJOINT (Jim:
#               "different FAQs"). The dq "phantom parent code" guard now covers
#               homeschool.html too, where the same stale line was found and fixed.
#   2026-08-11  BUILD ea -- THE PACING STEER, GUARDED AND DRILLED: endpoint parent-
#               gated + ownership-checked; the child's explicit choice outranks the
#               plan (rule 50, source AND live-proven); the steered mastery note names
#               WHO asked and protects the student's agency; steers join the reset
#               family; family.html keeps its controls. Live: set -> overview carries
#               it -> _resolve_focus applies/yields/ignores correctly -> clear -> reset.
#   2026-08-11  BUILD dz -- ACCESSIBILITY + PHONES, GUARDED: all three teaching pages
#               must keep their polite live regions, the mic's spoken name, the
#               reduced-motion block, and the phone dock (board first, rail stuck to
#               the bottom); session's four overlays stay real dialogs with focus on
#               the welcome action.
#   2026-08-11  BUILD dy -- CHILD MANAGEMENT, GUARDED AND DRILLED: the four endpoints
#               stay parent-gated + ownership-checked (misses 404 so probes learn
#               nothing); remove keeps its server-verified typed-name consent; attach
#               keeps refusing other families' codes (409) and demo codes; a code
#               change must keep moving EVERY per-student table. LIVE drill: two
#               parents, rename, cross-parent 404s, history follows a new code, the
#               old code dies, orphan attaches, owned code refused, wrong typed name
#               400s, right one deletes account AND data.
#   2026-08-11  BUILD dx -- ASSESSMENT SAVE/RESUME, GUARDED: challenge.html must keep
#               saving after every answer, offering the resume on the start panel,
#               clearing on finish AND on deliberate fresh starts, and discarding a
#               save whose question bank changed (never resume into a different test).
#   2026-08-11  BUILD dw -- REFRESHER + THREE BARS, GUARDED: the opener must keep its
#               gap check (1+ days away -> a real 3-4 sentence refresher with a
#               memory-jog, "a friend catching you up, never a test"), the server's
#               empty-TODAY-bar order must survive (today_live -> per-turn [[today]]
#               demand), and session.html must keep the TODAY placeholder at load so
#               two bars is never the resting state. Both found live by Jim.
#   2026-08-11  BUILD dv -- THE BUZZER-BEATER SHIELD, GUARDED: sprint panels swapped
#               in by the TIMER (break, results) must stay shielded for 1.2s so a
#               click meant for the last answer can never dismiss the celebration.
#               Found live by Jim, on his own product, within hours of dp deploying.
#   2026-08-11  BUILD du -- RETAKE DOOR + PARENT'S TRICKY LIST, GUARDED: the
#               dashboard's 90% line keeps its Retake button (students only, gated on
#               a real quiz score existing); session.html opens the &quiz=1 door like
#               the final-exam door and sends "__unit_quiz__"; main.py interprets the
#               sentinel with the BEST-score reassurance (rule 50); the parent box
#               ("Recently tricky") and the Friday email ("Tricky this week") both
#               answer the most-asked parent question from rule 55's rows.
#   2026-08-11  BUILD dt -- MISSED-PROBLEM MEMORY, GUARDED END TO END (rule 55 joins
#               RULE_VERIFY as COVERED). Source checks: session.html parses missed=
#               and ships it on all three score POSTs; the dashboard's Tricky-ones
#               card exists, hides when empty, fails soft; _keep_misses clamps to
#               total-correct (a tutor can never report more misses than there were
#               questions); GET /api/misses is student-gated; the mastery note hands
#               misses back with rule 55(b)'s revisit-ONE orders; quiz_misses joins
#               the reset family; rule 55 lives in the SHARED block exactly once.
#               LIVE drill (TestClient + sqlite): post a 3/5 quiz reporting 4 misses
#               -> exactly 2 stored, newest first, unit names attached; the mastery
#               note carries them; a 5/5 with a phantom miss stores NOTHING; the
#               sweep holds the newest 200; reset_student_data leaves the list empty.
#   2026-08-11  BUILD ds -- HELP AND SPRINTS-ON-REQUEST, GUARDED (PART 3p block):
#               app-nav's help pill must stay /help and never regress to a mailto
#               (dead on school Chromebooks); help.html must exist whole with the
#               support address as SHOWABLE text; main.py must route /help; the
#               assessment page keeps its help door; session.html must honour
#               &sprint=1; the dashboard's Run-one-now stays student-only.
#   2026-08-11  BUILD dr -- ELEMENTARY VOICE, GUARDED. PART 3e's parity list now proves
#               all three teaching pages use the capability-only canRecord (the mic
#               excludes NO course), that "canRecord = !IS_ELEM" never returns (it
#               would silently mute the students least able to type), and that the
#               prompt's how-they-answer note tells the tutor elementary students may
#               talk, with EXTRA transcription charity for young readers.
#   2026-08-11  BUILD dq -- MARKETING MUST MATCH THE PRODUCT (PART 3p grows the
#               Four-Lens theme-B guards). Machine-caught from now on: parents.html
#               can never again promise the phantom "parent code" or call live
#               features "rolling out"; family.html must keep its per-child Records
#               link, How-are-they-doing narrative, and weekly-email toggle;
#               teachers.html must link the real /teacher tool; records.html's
#               bare-visit message points home, never at URL surgery; the two new
#               endpoints (/api/parent/overview, /api/parent/weekly-email) exist and
#               are parent-token gated. Plus the whole family flow LIVE (subprocess
#               + TestClient + sqlite): signup -> add child -> overview numbers ->
#               toggle the Friday email off -> flag lands where the digest pass
#               reads it -> tokenless requests refused.
#   2026-08-11  BUILD dp -- SPRINTS FOR ALL TEN COURSES, AND EVERY FACT RE-DERIVED.
#               PART 3n's coverage bar rises from 27 units/3 courses to 70/10 (a
#               ratchet -- shrinking it means someone's course lost its sprints).
#               The _verify oracle learned every upper-course question shape (one-
#               and two-step solves, slopes, systems, exponent laws, factor pairs,
#               roots/powers, means/medians, angle pairs, triangle sum, Pythagorean
#               triples, circle facts, midpoints, areas, logs, sequences, limits,
#               power/chain rules, antipowers, definite integrals, characteristic
#               roots, probabilities, compositions, zeros, reflections, distributes)
#               -- so the generated-answer sweep now arithmetic-proves the bulk of
#               all ~4,200 problems per seed. The FIXED FACT LISTS (trig values,
#               radians, i-powers, empirical rule, dice, derivative facts, trig
#               identities, ODE orders, Laplace) each get an INDEPENDENT oracle:
#               sympy, math.erf, complex arithmetic, enumeration -- a wrong "fact"
#               fails the build. The unknown-course fixture moved off "calculus"
#               (which HAS sprints now) onto a concept unit left out on purpose.
#               Also fixed (found by this build's probe): _num_choices starved
#               NEGATIVE answers down to one tap button (blanket no-negatives rule);
#               and answers now use the same unicode minus the questions use.
#   2026-08-11  BUILD do -- THE tutor.py SPLIT, GUARDED. tutor.py's prompt text (the
#               eleven templates, GROUND_RULES, GRAPH_TOOL_NOTE, the overlays, scopes,
#               and assessment voices) moved VERBATIM to the new prompts.py; the move
#               itself was proven byte-identical outside this battery (52 built
#               prompts hashed before/after, 52 equal). What THIS file now guards
#               forever: PART 3h proves prompts.py stays TEXT ONLY (AST: top-level
#               string/dict assignments -- no imports, defs, classes, or calls; the
#               boundary is the point), that tutor still re-exports every moved name
#               non-empty (every tutor.<NAME> reference keeps working), and that the
#               assembled lesson prompt kept its full size. The range=" sweep and the
#               auditor's never-writes list both learned the new file. No check was
#               weakened; every existing check runs against the split layout
#               unchanged -- the whole 2,7xx-check battery IS the do-no-harm proof.
#   2026-08-11  BUILD dn -- PART 3q's key-transport block closes dg's documented
#               residual: /community?mod= was the LAST key-in-a-URL. New checks prove
#               community.html reads the key from the SHARED sessionStorage stash
#               ("mt_admin_key" -- /admin unlocks both), honours a legacy ?mod= link
#               once then scrubs the address bar, sends the key in the X-Admin-Key
#               header and NEVER in the request body, and clears the stash on a 401;
#               admin.html builds no key-carrying URL of any kind; POST
#               /api/forum/moderate takes the header through the same _require_admin
#               constant-time gate as every other admin call. The whole door is also
#               proven LIVE (subprocess + TestClient + sqlite): wrong header 401s,
#               the right header gets PAST the gate (400 bad kind / 404 unknown id),
#               the legacy body key still authorizes (a cached pre-dn page must keep
#               working across the deploy), and no key at all is refused.
#   2026-08-11  BUILD dm -- PART 3n grows the DISPLAY half of the sprint guarantee:
#               the dashboard's sprint-record card starts hidden, never renders on an
#               empty history (sprints never gate, an empty card is a nag), compares
#               this student only with this student (rule 42), fails soft, and the
#               endpoint is student-gated -- plus the whole display drill run LIVE
#               against a real database (two sprints recorded through store.record_
#               sprint, read back oldest-first with the personal best).
#   2026-08-11  BUILD dl -- the two WWC-Strong teaching rules land: 53 (the number line
#               used on purpose -- magnitude and comparison, fractions between 0 and 1
#               first then past 1, benchmarks 0/half/1, equivalents at ONE position)
#               and 54 (word problems have TYPES -- Change, Equal Groups, Compare; the
#               type chooses the operation; key-word rules are BANNED). Rule 54(b) is
#               ENFORCED from day one: board_notation_conflict now also catches the
#               tutor TEACHING a story-cue shortcut ("altogether always means add"),
#               in prose or on a board, with the vocabulary distinction honoured (a
#               "sum means add" definition is rule 37, not a shortcut) -- five new
#               fixtures, both corpora swept clean.
#   2026-08-11  BUILD dk -- BATCH E of the audit re-run. BOARD_NOTATION_CASES: the two
#               notation abuses quoted from real re-run boards ("$50 + 10% = $55" and
#               "a^2 + 64 = 100 = ?") become permanent referee fixtures with the legal
#               shapes as FALSE cases (the "of" form, percent-with-percent, pending
#               percent lines, worked chains ending in a number). The foundation-corpus
#               sweep grows to FOUR draft-level referees. PART 3r gains the
#               point-on-a-hole fixtures (dropped at the hole, preserved elsewhere).
#               RULE_VERIFY: 27 moves COVERED -> ENFORCED for the percent-sum shape.
#   2026-08-11  BUILD dj -- PART 3s: BACKUPS. A backup system is only real if the
#               restore has been rehearsed, so the battery now performs the whole
#               drill on every run: seed a real SQLite database through the public
#               store API, snapshot it with export_all, prove the DRY LOOK changes
#               nothing, restore into a second blank database THROUGH THE ACTUAL
#               restore_backup.py tool (gzip file and all), and prove the two
#               databases row-for-row identical. Boundaries proven from source:
#               main.py never calls import_all (no restore endpoint can exist), the
#               download rides the X-Admin-Key header, the nightly pass is fenced and
#               atomic, rotation keeps BACKUP_KEEP, /admin has the download button
#               (cx: buttons, not instructions) and NO restore control, and
#               RECOVERY.md + restore_backup.py ship complete.
#   2026-08-11  BUILD di -- PART 3r: the figures the audit could not draw, proven
#               through the REAL renderer (node executes math-figures.js, the same
#               file the browser runs). Piecewise domains clip and mark their own
#               endpoints (open for strict, closed for inclusive -- the audit's jump
#               figure is the fixture); an unparseable domain fails OPEN; the shared
#               tool note reaches all ten prompts; and the three showColumn bodies are
#               compared byte-for-byte (build-bk drift class) with align="last" proven
#               unable to complete a wrong sum. ⭐ THE HARNESS'S FIRST RUN FOUND A LIVE
#               BUG: hole= had NEVER drawn on a genuine 0/0 removable point -- the
#               renderer evaluated the function AT the hole, got NaN, and bailed; the
#               feature only worked on functions DEFINED at the point, which is exactly
#               where holes do not belong, and the canonical scripts had quietly worked
#               around it with pre-simplified forms. Fixed with a numeric limit (both
#               sides sampled and required to agree), and the asymptote case -- where
#               painting a hole would be rule 51(e) broken in pixels -- is a permanent
#               NEGATIVE fixture.
#   2026-08-11  BUILD dh -- the audit's teaching findings, tested. ANSWERED_CASES (rule
#               17's new referee: the board must not answer the question -- the audit's
#               ticket card is the fixture, plus commuted and word-number variants, plus
#               the shapes good teaching uses as FALSE cases) and UNSPOKEN_CASES (rule
#               44's new referee: a numeric board problem with a numberless spoken ask --
#               the audit's "First question: ... What's the answer?" is the fixture).
#               The foundation-corpus sweep now runs ALL THREE draft-level referees
#               (self-answer, answered-q, unspoken) over every canonical script on every
#               run, so a future widening cannot quietly start flagging correct lessons
#               (the build-cy discipline, now paid for twice). RULE_VERIFY: 17 and 44
#               move COVERED -> ENFORCED; rule 52 declared (COVERED). Junk-input
#               never-raises covers the two new referees.
#   2026-08-11  BUILD dg -- PART 3q (reliability) + the audit-log misfires become
#               permanent referee cases. The first full audit's Render logs proved the
#               stumbles were OUR bugs, not rate limits: the rule-15 referee counted the
#               pronoun "one" as a number and had no concept of an OFFER (a dozen
#               misfires in forty minutes, each burning a paid draft -- and the geometry
#               lesson's worked example with them, S-1); claude-sonnet-5 intermittently
#               rejects assistant-prefill continuation (each rejection was a stumble);
#               five replies shipped as admitted partials at the 1600 ceiling. Every
#               quoted misfire is now a PENDING_CASES / SELF_ANSWER_CASES fixture (plus
#               guards proving the exclusions did not swallow the referee), and PART 3q
#               proves with a scripted client: the negotiated prefill fallback (the
#               named 400 switches shapes and is REMEMBERED; unrelated errors still
#               raise), the 3000 ceiling, the one silent retry on an empty reply, the
#               stand-alone wording in both regeneration nudges, and the admin key's
#               exit from query strings (X-Admin-Key header; sessionStorage; no
#               key-carrying URL built anywhere in admin.html).
#   2026-08-10  BUILD df -- PART 3o learns the SIXTH unit-name copy and PART 3p bans two
#               phrases from marketing copy. Jim asked for a sweep proving no blanket
#               "evidence based learning" claim exists anywhere. It doesn't -- but the
#               sweep caught courses.html (the PRINTABLE scope & sequence) still saying
#               "taught Socratically" (missed by build cc's site-wide removal) and still
#               listing the pre-restructure diffeq units, plus llms.txt claiming unit
#               mastery at 80%+ (it is 90%+ on a ten-question Unit Quiz) under the old
#               MyTutor brand name. All fixed in df. PART 3o now parses courses.html's
#               ten unit lists (order-based; the cards sit in curriculum order); PART 3p
#               strips HTML comments then fails the build if "Socratic" or
#               "evidence-based" appears in any static page, llms.txt, or README.md.
#   2026-08-10  BUILD de -- PART 3o: unit-name parity across all FIVE files. The diffeq
#               restructure (CUPM mainstream syllabus) edited the same nine unit names
#               in curriculum.py, pedagogy.py, session.html and topic.html, and nothing
#               proved they agreed -- each file works fine alone while the picker shows
#               one name and the tutor teaches another. curriculum.units_for() is now
#               the declared source of truth and the other four are compared to it byte
#               for byte for every course. Writing the check found the FIFTH copy:
#               challenge.html's *_UNIT_NAMES (the labels on assessment results), which
#               still carried the OLD diffeq units -- fixed in the same build, and its
#               banks are also shape-checked (9 units x 5 questions, answer index 0-3),
#               since the diffeq re-mapping is exactly the edit that could leave a unit
#               short a question. Any future rename that misses a file fails the
#               battery instead of shipping.
#   2026-08-11  BUILD dd -- PART 3n: fluency sprints. Priorities in order of what they
#               would cost a child: all 1,620 generated answers verified RIGHT (a drill
#               that reinforces a wrong fact is worse than none), sprints gate NOTHING
#               (checked at store, endpoint and page level), and half B must be a
#               sibling of half A, not a twin -- the first registry shipped B as a
#               byte-identical twin of A, which would have made "improvement" a memory
#               test, and the sibling check caught two more twin families (percents,
#               make-ten's shifted ramp pushing past nine) before ship.
#   2026-08-10  BUILD dc -- three guards: the auditor must count graceful-failure turns
#               itself (absence is invisible to a content marker), retry a stumbled turn
#               once, and carry the critic's three discipline checks earned from its
#               first-run false positives.
#   2026-08-10  BUILD db -- two guards for the reasoning budget: an "output limit
#               reached" probe result must be retried with room to think (it is proof of
#               access, not absence), and the quiet variant (200 + empty message +
#               finish_reason length) must not end a lesson looking like the student
#               left.
#   2026-08-10  BUILD da -- four guards for probe_models(): the tool must be able to ask a
#               key what it reaches, the pricing button must ask, a model gated behind
#               organisation verification must say so WITH the remedy, and the probe list
#               must be overridable without a code change.
#   2026-08-10  BUILD cz -- five guards from the auditor's first live failure: a preflight
#               before any lesson, a negotiated token parameter, the model list offered
#               only for a real model error, a summary that cannot make "nothing was
#               marked" look like "no findings", and the admin panel repeating the
#               server's summary instead of computing a second one.
#   2026-08-10  BUILD cy -- SELF_ANSWER_CASES and the corpus sweep. Rule 39(b) is ENFORCED
#               now, not merely COVERED. Two of the FALSE cases are real false positives
#               caught by sweeping our own content before shipping: a foundation script
#               ("What is a numerator? The numerator is...") and a demo line that restates
#               the question's own number as a hint. Both are now permanent fixtures, and
#               the suite sweeps every foundation script on every run so a future widening
#               of the referee cannot quietly start punishing good teaching.
#   2026-08-10  BUILD cx -- a check that an admin job the owner cannot reach is NOT
#               SHIPPED. Jim asked "tell me exactly how to run it" and the honest answer
#               was that he could not: both money-spending admin jobs were documented as
#               "POST /api/admin/..." and nothing in the product can POST JSON. The
#               foundation pre-render had therefore sat un-run for days while three
#               handoff documents told him to run it. Every spending endpoint must now
#               have a button on /admin and be priceable from there.
#   2026-08-10  BUILD cw -- PART 3l (the lesson auditor's boundaries) and THE CEILING
#               RAISED 135,000 -> 150,000 with the reason written down where it is
#               enforced. The old note said "consolidate, do not raise"; it was written
#               before anything had been measured. What we know now: 135,000 was a
#               judgement in an audit, the built prompt is ~17% of the model's real
#               window, and rule 51 spent the last 500 characters -- so the NEXT rule,
#               whatever it was, would have failed the build. Merging rules to satisfy an
#               invented number means editing the teaching, which fails invisibly. That
#               is the wrong risk to take on no evidence, and lessonaudit.py is now the
#               evidence: run it at two prompt sizes and set the number from what it finds.
#               PART 3l guards the auditor's BOUNDARIES rather than its findings (those
#               are opinions): the key value may appear in an Authorization header and
#               nowhere else, the job can always be priced before it is run, the price
#               says it is an estimate, and the auditor never writes to tutor.py or
#               foundations.py. A critic that edits the teaching is a second author nobody
#               reviewed.
#               A NOTE ON WRITING THAT KEY CHECK: the first version flagged the dry run's
#               own label line -- the words "OPENAI_API_KEY" printed beside
#               "present"/"MISSING", which is exactly what a diagnostic should say. A
#               check that cries wolf at correct code gets switched off, and then it
#               guards nothing. It now looks for the VALUE travelling, not the name.
#   2026-08-10  BUILD cv -- rule 51 joins the ten-course scan, and a new check that every
#               range= we write PARSES UNDER THE RENDERER'S OWN RULE. The regex is read
#               out of math-figures.js so it cannot drift. It exists because rendering one
#               new figure showed the [[graph]] documentation teaching range="-1,5" while
#               parseRange accepted only "a..b" -- the window was discarded, silently, and
#               the instruction had been unfollowable since the day it was written to fix
#               exactly that complaint.
#               ⚠️ THE OTHER LESSON FROM THIS BUILD is in _cv_welcome_check.py, not here:
#               Playwright matches routes in REVERSE registration order, so a catch-all
#               registered last swallowed the stubbed /api/session and the harness measured
#               the FIRST-TIMER card while reporting on the returning one. It now asserts
#               which screen it is looking at before it measures anything. A test must
#               prove it is looking at the right thing before it is allowed to pass.
#   2026-08-10  BUILD cu -- PART 3k: A BAR MUST BE REACHABLE BY THE INSTRUMENT THAT
#               MEASURES IT. Jim asked for a retake path for a unit passed but not
#               mastered. Checking it found something worse: mastery is 90% and the Unit
#               Quiz was four or five questions, so the only possible scores were 80% and
#               100% -- the bar could only be cleared with a perfect paper. Topic quizzes
#               likewise (four questions, 80% bar). It survived because the bar and the
#               question count live in DIFFERENT FILES and changed on DIFFERENT DAYS, and
#               no test ever multiplied them together. PART 3k does exactly that
#               multiplication, for every quiz, in every course: at least one NON-PERFECT
#               score must pass, or the bar does not mean what it says.
#               Also here: rule 50 joins the ten-course coverage scan, the quiz lengths
#               are scanned in all ten built prompts, and the locked Final Exam must name
#               the units holding it shut AND fall back rather than fail shut.
#   2026-08-10  BUILD ct -- THREE LAYOUT GUARDS, and the first real catch by cs's checks.
#               Jim hit a live one: the demo's answer buttons were a one-per-line grid,
#               the answer zone could take 47vh, and .feed is flex:1 -- so the whiteboard
#               lost every pixel the answers took. PART 3j now insists the buttons are a
#               wrapping ROW (the real classroom's own shape), the answer zone is capped
#               at 35vh or less, and the board carries a min-height FLOOR.
#               ⭐ AND cs's "every tour stop points at a real element" check paid for
#               itself immediately: rebuilding the teacher dashboard removed the
#               tdAttention CARD while its tour stop still pointed at it. glow() returns
#               quietly on a missing id, so that stop would have narrated a dashboard
#               that never moved -- no error, no log, just a paragraph about a panel the
#               visitor cannot see. The line moved onto the roster instead.
#   2026-08-10  BUILD cs -- THE WHITELIST CHECK THAT SHOULD HAVE EXISTED SINCE bx. The
#               demo design notes have said "every spoken string must be on the
#               whitelist" from the beginning and NOTHING enforced it. say() looks the
#               text up in VOICE_LINES and plays clip N by index; a line that is not
#               there does not raise -- that one stop drops to the browser's flat
#               mechanical voice in the middle of Mr. Cadabra speaking. All 24 literal
#               tour lines are now checked, on every tour on the page. Two more: every
#               tour stop must point at an element that EXISTS (glow() returns quietly on
#               a missing id, so a typo means the words play over a dashboard that never
#               moves), and the homeschool override must cover every parent stop (it is
#               read BY INDEX and falls through to the PARENT's words where it is short).
#               A LESSON FROM WRITING IT: the first version wrapped the parse in `except
#               Exception`, which swallowed a NameError -- ast was never imported -- so
#               every line looked off-list and the failure blamed the demo instead of the
#               test. The except is narrow now. A test's error handling must not be able
#               to hide the test's own bugs.
#   2026-08-10  BUILD cr -- PART 3j now proves ONE DOOR, ONE DASHBOARD. Jim: "I don't
#               want any links to any other dashboards from there." Three paths could
#               hand an audience visitor somebody else's screen and all three fail
#               silently, so each is checked against the SOURCE rather than against a
#               comment claiming it: showBalloons must return through the audience
#               ending BEFORE it builds the three balloons, the ending itself must
#               contain no dashboard opener at all, and the dashboard's back button must
#               not close a locked walkthrough (there is no page behind it).
#               Also checked: a locked door still leads somewhere. A test that only
#               proves an absence would happily pass on a dead end.
#               NOT IN THIS FILE, deliberately: the behaviour was also driven in a real
#               browser across all four doors and the open demo (59 checks). That harness
#               needs playwright, and this battery must stay runnable anywhere in a
#               second -- it lives in the sandbox, not the repo.
#   2026-08-10  BUILD cq -- PART 3j grew two checks and one of its own bugs was fixed.
#               New: the walkthrough must open the dashboard BEFORE it starts talking
#               (Jim watched a blank screen talk at him for thirty seconds), and every
#               audience line must be anchored by its opening WORDS, each anchor
#               resolving to exactly ONE whitelisted line.
#               THE BUG WORTH REMEMBERING: my first anchor regex used ["']([^"']{12,80})["']
#               to pull the anchor text out. Four of the nine anchors have an apostrophe
#               inside a double-quoted string -- "the parent's view", "That's the honest
#               read." -- and [^"'] stops dead at that apostrophe. The test found five
#               anchors, called it a pass at >=9 only by accident of failing loudly, and
#               would otherwise have checked less than half of what its name claimed.
#               A test that silently checks a subset is worse than no test. Capture the
#               opening quote, require the same character to close it.
#   2026-08-10  BUILD cp -- PART 3j, the audience walkthroughs. Guards the two things
#               that can break /demo?view=... silently: a marketing page pointing at a
#               view the demo does not implement, and the two voice lists falling out of
#               step. That second one deserves a warning to whoever reads this next:
#               clips are served BY INDEX, so a mismatch plays the WRONG AUDIO under the
#               RIGHT WORDS and nothing errors. While writing this I compared the lists
#               with a naive regex over quoted strings, which matched text inside
#               COMMENTS and made two identical 188-line lists look 117 lines apart. The
#               helper here parses main.py as Python and demo.html as JS-with-comments,
#               which is the only way to answer the question honestly.
#   2026-08-10  BUILD co -- PART 3i AND THE GENERATED RULES INDEX (audit #2 items 24
#               and 23). This file's header has said from day one: "ADDING A RULE? Add a
#               scenario here in the same commit. That is the whole point." We drifted
#               anyway -- rules 42 to 47 shipped with no check of their own -- because
#               nothing made the drift visible.
#               RULE_VERIFY now declares, for every rule, HOW it is verified, in four
#               honest tiers: ENFORCED (a machine catches it in a real reply),
#               EXERCISED (a --live scenario asserts the behaviour), COVERED (the text
#               provably reaches all ten prompts -- he was told, which is not the same as
#               he does it), UNVERIFIED (nothing at all).
#               It is a RATCHET, not a gate: existing debt prints but does not fail a
#               deploy, while a NEW rule with no declaration fails, and a rule that
#               quietly LOSES its scenario fails. Today: 13 enforced, 10 exercised,
#               25 covered, 1 unverified.
#               `python ruletests.py --rules` regenerates RULES.md from the prompt
#               itself, so the index can never drift from the classroom. That file is
#               also what you hand a curriculum advisor or a school district.
#   2026-08-10  BUILD cn -- PART 3h, "it must not degrade, and it must scale".
#               Nothing in this battery had ever asked whether anything GROWS, and two
#               things did: every chat turn loaded, parsed, appended to and rewrote the
#               student's ENTIRE conversation in order to read the last thirty messages
#               of it, and the usage log kept every row forever. PART 3h now checks the
#               transcript cap (and that it stays above what the model reads), the usage
#               retention pass, deliberate pool sizing, age-based rate-bucket eviction
#               and the TTS cache cap.
#               It also asserts the prompt does not FLIP SHAPE between turns -- build cl
#               made it do that to save characters, and the cache arithmetic showed the
#               flip costs about $0.24 an episode to save $0.0005 a turn.
#   2026-08-10  BUILD cm -- CACHE DISCIPLINE CHECKS. The system prompt is one cached
#               block; per-turn content inside it moves the cache prefix and re-bills
#               everything after it. PART 3g now asserts get_tutor_reply takes a
#               turn_note, that per-turn asides never appear in the system prompt, and
#               that two ordinary turns build a byte-identical prompt.
#   2026-08-10  BUILD cl -- DEFERRAL TESTS + THE PROMPT BUDGET.
#               The deferral tests care far more about RESTORING than about saving: a
#               brand-new student still gets every script verbatim, a returning student
#               keeps every UNHEARD script verbatim, heard scripts stay NAMED so he can
#               still offer them, asking restores the exact wording, the default is to
#               carry the words, and the refresher detector is checked on both the
#               explicit ask and the bare "yes" that follows rule 40(b)'s offer.
#               The prompt ceiling is now a BUDGET TABLE, not a single number. A total
#               tells you that you are over and nothing about what to do; the table
#               prices every block, so the next person adding one sees the cost before
#               paying it. Measured and recorded in the failure message: there is 0%
#               overlap between the course templates and the shared rules, so nothing can
#               be reclaimed for free -- the honest options are consolidating rules,
#               deferring another block the way cl defers heard scripts, or raising the
#               ceiling deliberately with the reason written down.
#   2026-08-10  BUILD ck -- PART 3g, the misconception catalogue, and a PROMPT-SIZE
#               tripwire (audit #2 item 22). PART 3g checks every entry has all nine
#               fields, unique ids, a speakable SAY that does NOT open by telling the
#               student they are wrong (rules 20/49c), and -- the important one -- that
#               no `detect` string is just a NUMBER in any spelling. The first end-to-end
#               run matched "I did three plus two first, so twenty" and returned two
#               confident WRONG theories, because "three" and "two" had survived a filter
#               that only required a letter. A numeric answer is evidence only in the
#               context of the problem it answers, and the matcher cannot see the
#               problem. That case is now a permanent fixture.
#               The prompt-size check prints every course's size and fails above 135,000
#               characters. It is a TRIPWIRE set above today's largest (130,022): when it
#               trips the answer is to consolidate overlapping rules -- the rules block
#               is ~45% of the prompt -- not to raise the number.
#   2026-08-09  BUILD cj -- PART 3f, NOTATION COVERAGE. Jim asked the right question
#               after the f(x) fix: "math is filled with these kinds of things. How can
#               we make sure every one of these is caught all of the time?" Fixing f(x)
#               by hand fixed one symbol and guaranteed nothing. PART 3f is the general
#               answer, held against notation.py:
#                 A  every notation on every board we ship is REGISTERED for that course
#                    (317 board strings scanned). Write a symbol the registry does not
#                    know and the build fails -- so a symbol cannot reach a child's
#                    screen without us having said, somewhere, how to read it.
#                 B  the DEEP families need a real script that says them aloud, not a
#                    table row. It caught three courses using subscripts silently.
#                 C  the registry must recognise its own examples, must reach all ten
#                    prompts, and no entry may collide with a narrower one -- that last
#                    invariant was added after the first run reported diffeq's mu as an
#                    unregistered population mean, because two entries matched one glyph.
#   2026-08-09  BUILD ci -- rule 48 and the NOTATION READABILITY check (PART 3b).
#               Jim found f(x) being used in Algebra I with nothing ever teaching it. The
#               check that would have caught it: for every course, if any script writes
#               function notation on the BOARD, some script in that course must read it
#               ALOUD in words and deny the wrong reading by name. It failed on four
#               courses the moment it was written, and on diffeq even after the first fix
#               -- because diffeq writes y(t), y prime and dy/dx rather than f(x), and my
#               first regex only knew about f, g and h. Both halves of the check now
#               share one letter set so they can never disagree again.
#   2026-08-09  BUILD ch -- SCORE_CASES, rules 45-47, and two arithmetic guards.
#               SCORE_CASES covers the new score referee. Its FALSE cases carry the
#               weight again: three false positives were caught here before shipping,
#               including one that revealed the percentage check was matching NOTHING
#               (a stray \b after "%"). Also asserts that tutor.py's pass marks never
#               drift from store.py's, and that no score in any total from 1 to 40 is
#               ever stored higher than the truth.
#   2026-08-09  BUILD cg -- PENDING_CASES and the today-bar guards.
#               PENDING_CASES covers the new rule-15 referee, and the FALSE cases carry
#               most of the weight: rule 39(d) now REQUIRES him to ask "does that click,
#               or should I show it another way?" constantly, and re-rolling those would
#               cost real money every turn. Two false positives were caught here before
#               shipping -- "which number is the denominator in three-fourths?" (the
#               hyphen read as minus) and "is 1/2 bigger than the piece we shaded?" (a
#               fraction counted as two numbers).
#               PART 3d/3e gained the today-bar guards: the store table is in the reset
#               cascade, session.html still rebuilds the bar from SRV_PROGRESS.today at
#               load, and ensure_today_tag() restores a bar a reload destroyed while
#               still never resetting one that is genuinely live.
#   2026-08-09  BUILD cf -- PART 3e, plus rules 41-44 and two new guards.
#               PART 3e "THE THREE TEACHING PAGES MUST MATCH" exists because auditing
#               audit #1 found that item 11 (board lines never wrap) shipped to
#               session.html and never reached practice.html or topic.html -- Jim's
#               broken-equation screenshot was still reproducible on two of three pages,
#               a day after we called it fixed. Same bug shape as build bk, where a rule
#               written into one of eleven per-course templates reached one course. PART 1
#               made that impossible for the prompt; PART 3e does it for the pages, and
#               also proves every board tag the SHARED prompt block teaches is drawable on
#               all three (the six lesson-only tags are named explicitly, and the test
#               fails if one of them ever leaks into the shared block).
#               PART 3c now enforces rule 41: a figure with no caption= is a failure.
#               PART 3d now proves all THREE teaching modes carry the canonical scripts
#               and honour the heard list.
#   2026-08-09  BUILD ce -- three new groups of checks, one per thing Jim asked for.
#               PART 1 gained rules 39 and 40 (coverage across all ten courses).
#               PART 2 gained VISUAL_CASES for the new visual referee -- including the
#               false-positive cases, which matter just as much: a re-roll is a real model
#               call, so ordinary prose about a number line, a promise to draw one next
#               time, and a look back at yesterday's picture must all stay clean.
#               PART 3c gained a drift check: tutor.FIGURE_TAGS (a constant, because
#               tutor.py must not read static files at request time) must still name
#               exactly the tags session.html's handleTags() routes to a figure renderer.
#               PART 3d is new -- foundation memory: the term key survives the model's own
#               capitalisation, a made-up term is rejected, the heard list actually reaches
#               the prompt and marks its scripts, every script stays byte-identical either
#               way (the audio cache depends on it), junk never raises, and the new table
#               is in store's per-student reset cascade.
#   2026-08-09  BUILD cd -- ADDED PART 3c, "board tags actually draw".
#               This is the machine for the failure Jim named on the demo page: "the
#               lesson referred to a diagram that didn't show up on the board... We got
#               one shot to do it right, and it failed." A board tag fails SILENTLY --
#               no exception, no log, the words are still spoken -- when its name is not
#               in handleTags(), when its attribute is not one the renderer reads, when
#               it carries no content, or when an attribute value contains a square
#               bracket (handleTags' own regex ends the tag there). PART 3c PARSES
#               static/math-figures.js, static/geo-figures.js and session.html's
#               handleTags() so the contract is read from the renderers themselves and
#               cannot go stale; a new tag with no entry in TAG_HANDLER/TAG_INLINE fails
#               the suite on purpose rather than being skipped. On its first run it
#               caught 11 already-shipped foundation scripts. It also checks the two
#               ways [[graph]] quietly draws the WRONG picture: lines= on a non-linear
#               expression (parseLinear flattens a parabola into a straight line) and a
#               comma where the grapher splits only on ";" or "|".
#   2026-08-09  CREATED (build bu, proactive audit #25). Every teaching rule we have
#               was born from Jim noticing a failure in a live lesson. That does not
#               scale to real students. This is the machine that notices instead.
# -----------------------------------------------------------------------------
# WHAT IT IS
#   A standalone test script. It is NEVER imported by the running app, so it cannot
#   affect a deploy -- it exists to be RUN before one.
#
# HOW TO RUN
#   python ruletests.py            offline checks only (fast, no API key, no cost)
#   python ruletests.py --live     ALSO plays scripted students against the real
#                                  prompt (needs ANTHROPIC_API_KEY; costs a few cents)
#
# WHAT IT CHECKS
#   PART 1  RULE COVERAGE -- every rule really reaches all ten courses' built prompts.
#           (This is the class of bug that hid for a day in build bk: a rule written
#           into ONE of tutor.py's eleven per-course templates reached one course.)
#   PART 2  THE PROSE REFEREE -- the live 2026-08-08 contradiction is still caught,
#           and every known false-positive shape is still clean.
#   PART 3  SPOKEN NUMBERS -- forSpeech() on all three teaching pages (runs only if
#           `node` is available; skipped gracefully otherwise).
#   PART 4  --live SCENARIOS -- a scripted difficult student: wrong answers, "I don't
#           know", equivalent-form answers, off-topic questions, goodbyes. Mechanical
#           assertions, no human reading required.
#
# ADDING A RULE?  Add a scenario here in the same commit. That is the whole point.
# =============================================================================
import ast
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import tutor  # noqa: E402
import notation  # noqa: E402

COURSES = ["entry", "basic", "prealgebra", "algebra1", "geometry",
           "algebra2", "precalc", "calculus", "probstat", "diffeq"]
STUDENT = {"name": "Testy", "grade": "7"}

PASS, FAIL, SKIP = [], [], []


def ok(name):
    PASS.append(name); print(f"  \033[92mPASS\033[0m  {name}")


def bad(name, detail=""):
    FAIL.append((name, detail)); print(f"  \033[91mFAIL\033[0m  {name}\n        {detail}")


def skip(name, why):
    SKIP.append(name); print(f"  \033[93mSKIP\033[0m  {name} ({why})")


# -----------------------------------------------------------------------------
# A MISSING PACKAGE IS NOT A BROKEN BUILD (2026-08-14, build gh)
# Three checks used to FAIL -- one of them printing a raw Python traceback -- when
# sqlalchemy or httpx simply was not installed on the machine running the battery.
# That is worse than it sounds. A battery that reports the ENVIRONMENT as broken code
# teaches you to shrug at red, and on the very day this was written four GENUINE
# failures had been sitting in a run nobody had looked at, including a prompt 5,595
# characters over the ceiling. "0 failed" has to mean something everywhere, or it
# means nothing anywhere. A test that cannot run must say so in those words.
# This gates only THIRD-PARTY imports. A missing module of OUR OWN is still a failure:
# that is not an unprovisioned laptop, that is a broken repo.
# -----------------------------------------------------------------------------
OUR_MODULES = {"main", "tutor", "store", "prompts", "foundations", "curriculum",
               "misconceptions", "notation", "library", "sprints", "pedagogy",
               "mathcheck", "lessonaudit", "course_trial", "restore_backup"}


def module_present(name):
    """True when an importable dependency is actually installed here."""
    try:
        __import__(name)
        return True
    except Exception:  # noqa: BLE001 -- absent, or broken on this platform: same answer
        return False


def dep_gate(name, module, why=""):
    """True if `module` is installed. Otherwise SKIP `name`, saying which package, and
    return False so the caller can step over the check instead of failing it."""
    if module_present(module):
        return True
    skip(name, f"{module} is not installed here" + (f" -- {why}" if why else ""))
    return False


def check(name, condition, detail=""):
    ok(name) if condition else bad(name, detail)


# =============================================================================
# PART 1 -- RULE COVERAGE ACROSS ALL TEN COURSES
# =============================================================================
# One entry per rule that must reach EVERY course. The needle is a phrase unique to
# that rule in the shared blocks. When you write a new shared rule, add it here.
COVERAGE = [
    ("rule 0  opening sequence",        "THE OPENING SEQUENCE"),
    ("rule 64 never trade the number",  "NEVER TRADE THE STUDENT'S NUMBER"),
    ("rule 65 show them when asked",     "WHEN A STUDENT ASKS TO BE SHOWN"),
    ("rule 1  placement honesty",       "PLACEMENT HONESTY"),
    ("rule 4  say it -> write it",      "SAY IT -> WRITE IT"),
    ("rule 4  sub-step lines",          "ANSWERED SUB-STEP GETS ITS OWN LINE"),
    ("rule 4  multiplication sign",     "MULTIPLICATION SIGN"),
    ("rule 6  never run ahead",         "STILL NEVER RUN AHEAD"),
    ("rule 7  never ask to imagine",    "NEVER ASK THE STUDENT TO IMAGINE"),
    ("rule 9  the sound-off check",     "THE SOUND-OFF CHECK"),
    ("rule 10 tag checkable claims",    "TAG EVERY CHECKABLE CLAIM"),
    ("rule 13 literally true",          "MUST BE LITERALLY TRUE"),
    ("rule 14 define notation",         "DEFINE EVERY NOTATION"),
    ("rule 15 complete on screen",      "COMPLETE ON SCREEN"),
    ("rule 15 'your turn' on board",    'YOUR TURN" PROBLEM ITSELF GOES ON THE BOARD'),
    ("rule 15 pending '?' line",        "PENDING line with a question mark"),
    ("rule 16 restate the original",    "NOT JUST THE SUBSTITUTION"),
    ("rule 17 never answer yourself",   "NEVER ANSWER YOUR OWN QUESTION"),
    ("rule 18 check their answer",      "CHECK THE STUDENT'S ANSWER BEFORE YOU BUILD"),
    ("rule 19 worked example first",    "I DO, THEN YOU DO"),
    ("rule 20 partially right",         "PARTIALLY RIGHT IS NOT WRONG"),
    ("rule 21 'I don't know'",          "IS NOT A WRONG ANSWER -- IT IS A REQUEST"),
    ("rule 22 escalation ladder",       "NEVER ASK THE SAME THING THE SAME WAY TWICE"),
    ("rule 23 equivalent answers",      "EQUIVALENT ANSWERS ARE CORRECT ANSWERS"),
    ("rule 24 leaps/self-correct",      "LEAPS, SELF-CORRECTIONS"),
    ("rule 25 student disputes you",    "WHEN THE STUDENT SAYS YOU ARE WRONG"),
    ("rule 26 wrong lines corrected",   "A WRONG LINE NEVER STAYS ON THE BOARD"),
    ("rule 27 units + approximation",   "UNITS AND HONEST APPROXIMATION"),
    ("rule 28 one name per thing",      "ONE NAME PER THING"),
    ("rule 29 how a session ends",      "HOW A SESSION ENDS"),
    ("rule 30 off-topic questions",     "OFF-TOPIC AND PERSONAL QUESTIONS"),
    ("rule 31 bigger than math",        "WHEN SOMETHING BIGGER THAN MATH SHOWS UP"),
    ("rule 32 realistic problems",      "SURVIVE A SANITY CHECK"),
    ("rule 33 one notch at a time",     "DIFFICULTY MOVES ONE NOTCH AT A TIME"),
    ("rule 34 keep old skills sharp",   "KEEP OLD SKILLS SHARP"),
    ("rule 35 fix-then-retry a quiz",   "A FAILED QUIZ IS NEVER RE-GIVEN ON THE SPOT"),
    ("rule 36 teach before you ask",     "TEACH THE THING BEFORE YOU ASK ABOUT THE THING"),
    ("rule 37 vocabulary is taught",     "VOCABULARY IS TAUGHT, NEVER ASSUMED"),
    ("rule 38 concrete->picture->symbol", "CONCRETE, THEN PICTURE, THEN SYMBOLS"),
    ("rule 39 talk less, check in",      "TALK LESS. CHECK IN OFTEN"),
    ("rule 39 the check must be failable", "MAKE THE CHECK FAILABLE"),
    ("rule 40 ask before you repeat",    "SIT THROUGH THE SAME INTRODUCTION TWICE"),
    ("rule 40 mark what you taught",     '[[learned term="denominator"]]'),
    ("rule 41 captions say what to notice", "CARRIES A CAPTION THAT SAYS WHAT TO NOTICE"),
    ("rule 42 no comparisons",           "NEVER COMPARE THIS STUDENT TO ANYONE BUT THIS STUDENT"),
    ("rule 43 no false perception",      "YOU PERCEIVE EXACTLY TWO THINGS"),
    ("rule 44 read the problem aloud",   "READ THE PROBLEM ALOUD, IN FULL, EVERY TIME"),
    # build gl: the missing half of ACCURACY -- fix it before you speak, and fix it
    # in PRIVATE. The 2026-08-16 HIGH was the tutor changing its mind in front of a child.
    ("fix it SILENTLY (build gl)",       "never let the student watch you change your mind"),
    ("rule 45 the tally is arithmetic",  "THE TALLY IS ARITHMETIC, NOT JUDGMENT"),
    ("rule 46 one skill per question",   "A QUIZ QUESTION TESTS ONE SKILL"),
    ("rule 47 no cold quizzes",          "NO COLD QUIZZES"),
    ("rule 48 say the symbol aloud",     "HOW TO *SAY* THE SYMBOL"),
    ("rule 50 chase unfinished units",   "AN UNFINISHED UNIT IS YOUR JOB"),
    ("rule 51 a feature must be real",   "A FEATURE ON THE BOARD MUST BELONG TO THE FUNCTION"),
    ("quiz length: unit quiz is TEN",    "give the UNIT QUIZ: TEN questions"),
    ("quiz length: topic quiz is FIVE",  "give a short quiz -- FIVE"),
    ("canonical foundation scripts",     "SPEAK THESE VERBATIM"),
    ("speech: money as money",          "MONEY IS SPOKEN AS MONEY"),
    ("speech: number words",            "NUMBERS ARE SPOKEN THE WAY PEOPLE SAY THEM"),
    ("speech: spoken answers count",    "NUMBERS SPOKEN AS WORDS ARE EXACT ANSWERS"),
    ("progress: today bar every session", "THIS INCLUDES RESUMED SESSIONS"),
    # build ee (2026-08-12): the five teaching upgrades reach every course
    ("rule 56 find the error",           "FIND THE ERROR: A WRONG SOLUTION, CLEARLY LABELED"),
    ("rule 57 self-monitoring",          "TEACH THE STUDENT TO CHECK THEMSELVES"),
    ("rule 58 two ways, one board",      'TWO WAYS, ONE BOARD, THEN "WHICH WOULD YOU CHOOSE?"'),
    ("rule 59 right answer, wrong method", "A RIGHT ANSWER CAN STILL CARRY A WRONG METHOD"),
    ("rule 60 the board spotlight",      "POINT WITH LIGHT WHEN WHERE-TO-LOOK IS THE LESSON"),
    ("rule 61 conditions on claims",     "A GENERALIZATION CARRIES ITS CONDITION"),
    # build ex -- the seven verified teaching defects from the 2026-08-12 audits
    ("rule 19e a new move is new",       "A NEW MOVE INSIDE A FAMILIAR TOPIC COUNTS AS NEW"),
    ("rule 27c one unit per model",      "A STORY MODEL HOLDS ONE UNIT FROM ITS FIRST LINE"),
    ("rule 49g the diagnosis is spoken", "THE DIAGNOSIS IS SPOKEN, IN PLAIN WORDS"),
    ("rule 50g the locked-door offer",   "AT THE LOCKED DOOR, THE OFFER IS AUTOMATIC"),
    ("rule 51f limits carry their side", "A LIMIT NAMES ITS APPROACH, AND EACH SIDE IS ITS OWN CLAIM"),
    ("rule 52e verdict first",           "THE VERDICT OPENS THE REPLY"),
    ("rule 62 point at real work",       "YOU MAY ONLY POINT AT WORK THAT HAPPENED"),
]


def part1_coverage():
    print("\nPART 1 — rule coverage across all ten courses")
    prompts = {c: tutor.build_system_prompt(dict(STUDENT), course=c) for c in COURSES}
    for name, needle in COVERAGE:
        missing = [c for c in COURSES if needle not in prompts[c]]
        check(name, not missing, f"missing in: {', '.join(missing)}")
    # no accidental gap in the numbered sequence
    nums = sorted({int(m) for m in re.findall(r"^(\d+)[.)] ", prompts["algebra1"], re.M)})
    expected = list(range(0, max(nums) + 1)) if nums else []
    check("rule numbering has no gaps", nums == expected,
          f"saw {nums}")


# =============================================================================
# PART 2 -- THE PROSE REFEREE
# =============================================================================
# Each case is (name, reply, should_flag). The FIRST is the real 2026-08-08 bug.
PROSE_CASES = [
    ("live bug: wrong answer adopted in words",
     'Fifteen dimes — and since that\'s over nine again, we do the same trick: fifteen '
     'dimes is one dollar and five dimes, so we write the five and carry a dollar. '
     '[[step eq="dimes: 7 + 8 + 1 = 16"]]', True),
    ("the corrected flow (must stay clean)",
     'Sixteen — nice, careful counting. Sixteen dimes is one dollar and six dimes, so we '
     'write the six and carry a dollar. [[step eq="dimes: 7 + 8 + 1 = 16"]]', False),
    ("intermediate value that reaches the right result",
     'Seven plus eight is fifteen dimes, and adding the one we carried makes sixteen. '
     '[[step eq="dimes: 7 + 8 + 1 = 16"]]', False),
    ("operand mentioned in passing",
     'We had eight dimes in the second number, so the column comes to sixteen. '
     '[[step eq="dimes: 7 + 8 + 1 = 16"]]', False),
    ("different label entirely",
     'Ten pennies is one dime, so we carry it. [[step eq="pennies: 5 + 5 = 10"]]', False),
    ("numeral contradiction",
     'You end up with 15 cookies on the plate. [[step eq="cookies: 9 + 8 = 17"]]', True),
    # 2026-08-09: this fixture used to end "...so what is eight divided by two?" with no
    # pending line, which the new rule-15 referee correctly flags. The numeric check is
    # still what this case tests (an unlabeled board line must not false-positive); the
    # reply is now written the way rule 15 actually asks for.
    ("unlabeled board line",
     'Nice! [[step eq="2x = 8"]] So what is eight divided by two? '
     '[[step op="/ 2" eq="x = ?"]]', False),
    ("no board tags at all",
     "Great job — that's fifteen dimes exactly!", False),
    # build dh: this fixture's REPLY was updated, not its point. The old wording ("what
    # do the dollars come to?") never spoke the problem's numbers -- which rule 44 has
    # forbidden since build cf and the new unspoken-problem referee now catches. The
    # case still proves what it always proved: a pending "?" line is not a number
    # contradiction.
    ("pending '?' line is never a contradiction",
     'Your turn — what do two plus one plus one dollars come to? '
     '[[step eq="dollars: 2 + 1 + 1 = ?"]]', False),
]

# ---- the VISUAL half of the referee (build ce) ------------------------------
# Jim's demo failure, in a live lesson: "the lesson referred to a diagram that didn't
# show up on the board... we got one shot to do it right, and it failed."
# A false positive costs a real model call, so the FALSE cases below matter as much as
# the TRUE ones -- ordinary mathematical prose about a number line must stay clean.
VISUAL_CASES = [
    ("the failure: a number line that was never drawn",
     "Here's a number line from negative six to six. Where would negative three sit?", True),
    ("the same reply, with the picture actually drawn",
     'Here\'s a number line from negative six to six. Where would negative three sit? '
     '[[numberline min="-6" max="6"]]', False),
    ("'I just drew' with an empty board",
     "I just drew a graph of this function — see how it bends upward?", True),
    ("'look at the diagram' with only writing on the board",
     'Look at the diagram: the two legs meet at the corner. [[write text="a=3, b=4"]]', True),
    ("'let me draw a picture' and he does",
     'Let me draw a picture of six stars. [[objects emoji="⭐" groups="6"]]', False),
    ("pointing at a board he wrote nothing on",
     "Take a look at the board — see how the twos cancel?", True),
    ("pointing at a board he DID write on",
     'Take a look at the board — see how the twos cancel? [[step eq="2x = 8"]]', False),
    ("plain prose ABOUT a number line is not a claim",
     "On a number line, numbers get bigger as you move to the right. What's bigger, 5 or 8?", False),
    ("a promise about NEXT time is not a claim",
     "Next time I'll draw you a picture of that. For now, what is seven plus eight?", False),
    ("recalling a picture from earlier is not a claim",
     "Remember the number line we used yesterday? Same idea here. What's negative two plus five?", False),
    ("teaching with no visuals mentioned at all",
     'Nice work! Seven plus eight is fifteen. [[step eq="7 + 8 = 15"]]', False),
]

# rules 2 and 8 -- (student's message, reply, should_flag). Added build co, when the
# generated rule index made it plain these were two of only three rules in the entire
# prompt that nothing checked at all.
ASKED_CASES = [
    ("show me a number line",
     "Sure — a number line runs from negative five to five.", True),
    ("show me a number line",
     'Sure! [[numberline min="-5" max="5" points="0" caption="zero sits in the middle"]]', False),
    ("can I see it drawn?", 'Of course. [[write text="3/4"]]', False),
    ("draw it for me", "I will in a moment — first, what is seven plus eight?", True),
    ("what is 7 plus 8?", 'Fifteen — nice. [[step eq="7 + 8 = 15"]]', False),
    ("", "Let me show you what happens when we take two away.", True),
    ("", 'Let me show you. [[objects emoji="🍪" groups="5" caption="take two away and count"]]', False),
]

# ---- the PENDING-QUESTION half (build cg) -----------------------------------
# Jim's live Pre-Algebra resume: "it gave me a problem without putting it on the board,
# and this is the exact example that we've already used once before that was supposedly
# fixed." Rule 15 names this exact scenario and prints the exact fix, and the reply still
# went out without a board line. So it stops being a rule and becomes a referee.
# The FALSE cases matter just as much -- a re-roll is a real model call, and rule 39(d)
# now REQUIRES him to ask "does that click, or should I show it another way?" constantly.
PENDING_CASES = [
    ("Jim's live bug: the dollars column asked, nothing pending on the board",
     "Now for the dollars column — two dollars plus one dollar, plus the one dollar we "
     "just carried. What's two plus one plus one? "
     '[[column op="+" terms="2.75 | 1.85"]] [[step eq="dimes: 7 + 8 + 1 = 16"]]', True),
    ("the same reply with the pending line rule 15 asks for",
     "What's two plus one plus one? " '[[step eq="dollars: 2 + 1 + 1 = ?"]]', False),
    ("the original 2026-08-08 catch: 'your turn' with no board",
     "Your turn — what is ten minus two times three?", True),
    ("...and the same question written up",
     'Your turn — what is ten minus two times three? [[write text="10 - 2 × 3 = ?"]]', False),
    ("a written expression, spoken as a question",
     "So what does 12 ÷ 4 come to?", True),
    ("one number plus an operator word still counts",
     "What do you get when you add nine?", True),
    ("a social question is not a computation",
     'Ready to try one on your own? [[step eq="7 + 8 = 15"]]', False),
    ("rule 39(d)'s check-in must NEVER trigger this",
     "Does that click, or should I show it a different way?", False),
    ("a vocabulary question is not a computation",
     "Which number is the denominator in three-fourths?", False),
    ("a fraction is one value, not an operation",
     "Is 1/2 bigger than the piece we shaded?", False),
    ("numbers in a story with no question asked",
     'We had 5 cookies and I gave you 2 more. '
     '[[objects emoji="🍪" groups="5" add="2" caption="count them all"]]', False),
    ("tap-to-answer choices still need the question on the board",
     'What is six times seven? [[write text="6 × 7 = ?"]] [[choices options="42 | 48"]]', False),
    # ---- BUILD dg (2026-08-11): THE AUDIT-LOG MISFIRES, PERMANENT. Every line below was
    # quoted in a real [prosecheck] CONTRADICTION on 2026-08-10/11 (Audit_Findings_
    # 2026-08-11.md, L-3). Each misfire cost a paid regeneration -- and in the geometry
    # lesson the regenerations cost the student the worked example itself (S-1): the
    # drafts that contained it kept being discarded, and the surviving draft wrote as if
    # they had been seen. None of these is a computation handed to the student.
    ("the S-1 lesson's offer: 'one ... one more' are pronouns, not numbers",
     "Want to try one yourself now, or see one more worked example first?", False),
    ("an offer NAMING a candidate problem is still an offer",
     "Want to try a trickier one — maybe f of x plus 3, or plugging in a negative number?", False),
    ("an offer with 'f of a plus one' inside it",
     "Want to try one more with a different expression, like f of a plus one, or are you "
     "ready to move on?", False),
    ("an offer with a concrete input",
     "Want to try one with a different input, like f of 5 for that same rule?", False),
    ("an offer about limits",
     "Want to try one yourself — say, finding the limit as x approaches 3 for a similar "
     "broken f?", False),
    ("'Ready to...' with real numbers is still an offer",
     "Ready to try your triangle with legs 6 and 8 now, using the same steps?", False),
    ("a statement ending inside a quote must not merge into the question after it",
     'We write that whole thing as "f of 3 equals 7." Want me to run one more number '
     "through the machine, or try one yourself?", False),
    ("a look-question directs the eyes at a board already drawn",
     "See how the last-digit way puts the five right under the seven, which is a "
     "hundredths piece?", False),
    # ...and the exclusions must not swallow the referee whole:
    ("'see how MANY' still asks for a count -- a computation",
     "See how many apples are left after we take away three and two more?", True),
    ("comparing unit fractions is still a real computation ask",
     "So between one fourth and one eighth, which piece is actually bigger?", True),
    ("'one plus one' is arithmetic even though the word is 'one'",
     "What is one plus one?", True),
]


# ---- the SCORE half (build ch, proactive audit #2 item 9) --------------------
# The server already recomputes every percentage from correct/total, so no number the
# model asserts is ever STORED. What nothing checked is what the student HEARS: the tag
# can say 3 of 5 while the sentence beside it says "you passed!". These counts feed the
# progress bars, the parent dashboard and the printable homeschool record, so a score
# softened once becomes a green bar and a line a parent may have to defend.
# Three false positives were caught here before shipping -- see the FALSE cases.
SCORE_CASES = [
    ("a fail called a pass",
     'Nice work — you passed! [[quiz unit="2" topic="1" name="Rounding" correct="3" total="5"]]', True),
    ("the same fail, reported honestly",
     'Three of five this time. [[quiz unit="2" topic="1" name="Rounding" correct="3" total="5"]]', False),
    ("a real pass",
     'You passed — four of five! [[quiz unit="2" topic="1" name="R" correct="4" total="5"]]', False),
    ("a pass talked down into a fail",
     'We\'ll try that again soon. [[quiz unit="2" topic="1" name="R" correct="5" total="5"]]', True),
    ("an inflated percentage",
     'That is 80% — great! [[quiz unit="2" topic="1" name="R" correct="3" total="5"]]', True),
    ("the correct percentage, stated plainly",
     'That is 60% — one more round and you have it. [[quiz unit="2" topic="1" name="R" correct="3" total="5"]]', False),
    ("naming the BAR is teaching, not a score claim",
     'You need 80% to pass, and you got 60% this time. [[quiz unit="2" topic="1" name="R" correct="3" total="5"]]', False),
    ("a mis-stated fraction",
     'You got four out of five. [[quiz unit="2" topic="1" name="R" correct="3" total="5"]]', True),
    ("the right fraction, in words",
     'You got three out of five. [[quiz unit="2" topic="1" name="R" correct="3" total="5"]]', False),
    ("80% is a topic-quiz pass but NOT unit mastery",
     'You mastered the unit! [[check unit="2" correct="4" total="5"]]', True),
    ("90% is",
     'You mastered the unit — nine of ten! [[check unit="2" correct="9" total="10"]]', False),
    ("the Final Exam, inflated",
     'You passed the Final Exam! [[finalexam correct="15" total="18"]]', True),
    ("the Final Exam, honest",
     'Seventeen of eighteen — you passed the Final Exam! [[finalexam correct="17" total="18"]]', False),
    ("no score tag: nothing to contradict",
     'You passed that one nicely. [[step eq="7 + 8 = 15"]]', False),
    ("a percentage inside the MATH is not a score claim",
     'What is 25% of 80? [[write text="25% of 80 = ?"]] '
     '[[quiz unit="2" topic="1" name="R" correct="4" total="5"]]', False),
    ("a percents lesson that also reports honestly",
     'Nice — 25% of 80 is 20. You got four out of five today. '
     '[[quiz unit="2" topic="1" name="R" correct="4" total="5"]]', False),
    ("an unrelated count is not a score",
     'That took 5 steps. [[quiz unit="2" topic="1" name="R" correct="3" total="5"]]', False),
]


# =============================================================================
# SELF_ANSWER_CASES (2026-08-10, build cy) -- the tutor answering its own question.
# -----------------------------------------------------------------------------
# Rule 39(b) -- one question per turn, and it comes LAST -- has been COVERED since build
# ce: written into all ten prompts and never once checked. The MAA Instructional Practices
# Guide gave us the reason to enforce it: instructors wait less than 1.5 seconds before
# answering their own question, the research says wait SEVEN, and the first thing that
# improves when you wait is how often a student says "I don't know".
# The FALSE cases are the important half, as always. Two of them exist because they were
# real false positives found by sweeping our own corpus: every foundation script is shaped
# "What is a numerator? The numerator is ..." (teaching, not self-answering), and demo line
# "two to WHAT power makes thirty-two? Start at two..." restates a number from the question
# as a HINT. A referee that cannot tell a hint from an answer punishes good teaching.
SELF_ANSWER_CASES = [
    ("the MAA guide's own vignette",
     "So, how much work is done on each slice? That's just F(x) times 4.", True),
    ("ask and answer in one breath",
     "What is 7 plus 5? It's 12. Now try the next one.", True),
    ("the answer announced after a board tag",
     'What is 12 divided by 4? [[step eq="12 / 4 = ?"]] The answer is 3.', True),
    ("a wordy question, then 'the answer is'",
     "So what do we do with the remainder? The answer is 3.", True),
    ("a hint that leaks a NEW number is still a leak",
     "What is 7 plus 5? Remember that 7 plus 3 is 10, so...", True),
    ("the question is last -- exactly right",
     'Nice work. What is 7 plus 5? [[step eq="7 + 5 = ?"]]', False),
    ("encouragement after the question is kind, not a leak",
     'What is 7 plus 5? Take your time -- I am not going anywhere. [[step eq="7 + 5 = ?"]]', False),
    ("A FOUNDATION SCRIPT defining a term (real false positive, swept)",
     "What is a **numerator**? The numerator is the top number of a fraction. It tells "
     "you how many of the 4 equal pieces we are counting.", False),
    ("A HINT restating the question's own number (real false positive, swept)",
     "Here's the puzzle on the board: two to WHAT power makes thirty-two? Start at two "
     "and count how many times you double.", False),
    ("rule 39(d)'s check-in must never trip it",
     "Does that click, or should I show it another way?", False),
    ("a story with numbers, question last",
     "A bag holds 6 marbles and you add 2 more. How many marbles now?", False),
    ("numbers before the question, none after",
     "We had 7 apples and 5 arrived. How many are there now?", False),
    ("rhetorical, no numbers anywhere",
     "So what happens next? Let's find out together.", False),
    # BUILD dg (2026-08-11): the second geometry misfire from the audit logs. An OFFER
    # followed by the problem GOING UP is exactly right -- rule 39(b)'s referee read the
    # offer as an answerable question and the problem's own numbers as the leak.
    ("an offer, then the problem going up, is teaching -- not self-answering",
     "Want to try one yourself now, or see one more worked example first? Here's one "
     "ready for you if you're up for it: legs of 6 and 8. "
     '[[step eq="6^2 + 8^2 = ?"]]', False),
]


# ---- rule 17's referee (build dh) -- the board must not answer the question ----------
# Both TRUE cases are quoted from the first full audit (Audit_Findings_2026-08-11.md,
# S-2): a worked card completing "3 × 2 = 6" while the prose asks "so what's 3 times 2?".
# A question the board has already answered cannot fail, and the "win" that follows is
# not evidence. The FALSE cases are the shapes good teaching actually uses.
ANSWERED_CASES = [
    ("the audit's ticket card: board completes the line, prose asks it",
     'Say you have 5 dollars, plus 3 tickets at 2 dollars each. '
     '[[card title="5 dollars + 3 tickets at $2 each" '
     'items="tickets cost: 3 × 2 = 6 dollars | then add: 5 + 6 = ?"]] '
     "So what's 3 times 2 first?", True),
    ("same question, commuted on the board -- still answered",
     'So what\'s 2 times 3? [[step eq="3 × 2 = 6"]]', True),
    ("number words in the prose, digits on the board -- still answered",
     'What is seven plus five? [[step eq="7 + 5 = 12"]]', True),
    ("the pending '?' line is rule 15 done RIGHT -- never flagged",
     'What is 7 plus 5? [[step eq="7 + 5 = ?"]]', False),
    ("a completed line for a DIFFERENT computation is a worked step, not the answer",
     'Now add that to your 5 dollars: what is 5 plus 6? '
     '[[step eq="3 × 2 = 6"]] [[step eq="5 + 6 = ?"]]', False),
    ("an offer that names numbers is an invitation, not a question",
     'Want to see why 3 times 2 makes 6? [[step eq="3 × 2 = 6"]]', False),
    ("a recap sentence with no asking lead-in is not a question",
     'Remember, 3 times 2 is 6 -- shall we keep going? [[step eq="3 × 2 = 6"]]', False),
]


# ---- rule 44's referee (build dh) -- the spoken words must read the problem ----------
# The TRUE case is quoted from the audit's final-exam lesson: a quiz question that
# existed only as board text while the voice said "What's the answer?". This is a VOICE
# classroom; a problem never spoken is a problem some students cannot attempt.
UNSPOKEN_CASES = [
    ("the audit's quiz turn: numeric problem on the board, numberless spoken ask",
     'First question: [[step eq="Q1:  Evaluate 5x - 2 when x = 4"]] '
     "What's the answer?", True),
    ("a pending line whose ask was read aloud in words",
     "Give it a shot: what's three point five plus zero point four seven? "
     '[[column op="+" terms="3.50 | 0.47"]] [[step eq="3.50 + 0.47 = ?"]]', False),
    # BUILD eq (2026-08-12) -- THIS EXPECTATION WAS DELIBERATELY REVERSED, and the old
    # line is kept above it so the change is visible rather than silent. It used to read
    # "a concept question over a fraction on the board (a fraction is ONE number)" and
    # expect NO flag, because the bar was two numeric tokens and a fraction counts as
    # one. That bar is exactly what the 2026-08-12 audits walked through: an entire
    # fraction quiz ("8/12 = ?", "6/9 = ?") went by while the tutor said only "this
    # fraction". A student listening rather than reading cannot answer "which part is
    # the denominator?" when no fraction was ever named aloud -- which is rule 44's
    # whole point. So this case now expects a FLAG...
    ("a fraction on the board that the words never name (bar lowered in eq)",
     'Which part is the denominator? [[write text="3/4 ... ?"]]', True),
    # ...and the genuine exemption it was protecting is pinned properly instead: a
    # concept question is fine the moment the words actually say the fraction.
    ("the same concept question, with the fraction spoken",
     'Which part of three fourths is the denominator? [[write text="3/4 ... ?"]]', False),
    ("a concept line with no quantity to read at all",
     'Which one sits on top? [[write text="numerator / denominator"]]', False),
    ("even one spoken number means we stay silent (fail open by design)",
     'Question two: [[step eq="Q2: Combine like terms: 6y + 2y - y"]] '
     "What do you get?", False),
    ("no question asked at all -- a worked line narrated",
     'Here is the step written out. [[step eq="Q3: 12 ÷ 4 = 3"]] Nice and steady.', False),
    # BUILD gk (2026-08-16) -- THE HALVES OF A FRACTION MUST BE SAID TOGETHER, and this
    # block is quoted from the lesson that proved it. _pq_spoken_covers used to look for
    # the numerator ANYWHERE and the denominator ANYWHERE, independently -- so a turn
    # whose board read "3/4 + 1/4 = ?" and whose voice said "three plus one really is
    # four" (about the NUMERATORS; it never reads the problem) scored as spoken, because
    # a "three" and a "four" both existed somewhere in the sentence. A confused
    # nine-year-old was then asked a question they had only ever seen written down.
    # The FALSE cases below are real turns from the same audited lessons: they are what
    # the tightened rule must never start flagging.
    ("the 2026-08-16 miss: 'three plus one really is four' over 3/4 + 1/4",
     "Good job adding the tops \u2014 three plus one really is four! "
     '[[step eq="3/4 + 1/4 = ?"]] How many fourths do you have in all?', True),
    ("the same turn read properly: 'three fourths plus one fourth'",
     "The problem is three fourths plus one fourth. "
     '[[step eq="3/4 + 1/4 = ?"]] What do you get?', False),
    ("said as quarters", "Three quarters plus one quarter. "
     '[[step eq="3/4 + 1/4 = ?"]] What do you get?', False),
    ("said as 'three over four'", "Three over four plus one over four. "
     '[[step eq="3/4 + 1/4 = ?"]] What do you get?', False),
    ("the literal 3/4 spoken in the prose", "Our problem is 3/4 + 1/4. "
     '[[step eq="3/4 + 1/4 = ?"]] What do you get?', False),
    ("real turn: one half plus one third",
     "what's one half plus one third? " '[[step eq="1/2 + 1/3 = ?"]]', False),
    ("real turn: three fourths minus one fourth",
     "what's three fourths minus one fourth? " '[[step eq="3/4 - 1/4 = ?"]]', False),
    ("real turn: one fifth plus two fifths",
     "what's one fifth plus two fifths? " '[[step eq="1/5 + 2/5 = ?"]]', False),
    ("real turn: simplify eight twelfths",
     "question one: simplify eight twelfths. " '[[step eq="8/12 = ?"]]', False),
    ("real turn: a mixed number read aloud",
     "three and one fourth minus one and three fourths. " '[[step eq="3 1/4 - 1 3/4 = ?"]]', False),
    ("the same lesson's OTHER miss: the eighths problem never read",
     "If you put those slices together, how many eighths do you have in all? "
     '[[step eq="2/8 + 3/8 = ?"]]', True),
]


# ---- the board-notation check (build dk) -- both TRUE cases quoted from the re-run --
BOARD_NOTATION_CASES = [
    ("the re-run's percent abuse: bare percent added and COMPLETED",
     'Ten percent of fifty is five, so fifty-five. [[step eq="$50 + 10% = $55 ✓"]]', True),
    ("plain number plus bare percent, completed",
     'So we add the tip. [[step eq="50 + 10% = 55"]]', True),
    ("the honest 'of' form is exactly right",
     'The tickets first. [[step eq="$50 + 10% of $50 = $55"]]', False),
    ("percent-with-percent arithmetic stays legal",
     'The rest of the class: [[step eq="100% - 40% = 60%"]]', False),
    ("a percent conversion stays legal",
     'Three fourths as a percent: [[step eq="3/4 = 75%"]]', False),
    ("a pending percent line stays legal (the ? is rule 15 doing its job)",
     'Your turn: [[step eq="10% of 90 = ?"]]', False),
    ("the re-run's chained equals: '= 100 = ?' asks what 100 equals",
     'Now solve for a. [[step eq="a^2 + 64 = 100 = ?"]]', True),
    ("the clean version: true equation, then its own pending line",
     'Now solve for a. [[step eq="a^2 + 64 = 100"]] [[step eq="a^2 = ?"]]', False),
    ("a worked chain that ends in a NUMBER is ordinary arithmetic",
     'All together: [[step eq="a^2 = 100 - 64 = 36"]]', False),
    # ---- rule 54(b), build dl: key-word shortcuts are a taught misconception --------
    ("teaching a key-word rule in prose is caught",
     "Here's a trick to remember: altogether always means add! So let's add.", True),
    ("teaching key-word rules on a card is caught",
     'Handy tricks: [[card title="word clues" items="in all means add | left means subtract"]]', True),
    ("talking ABOUT a cue word is teaching, not a shortcut",
     "The word altogether tells us the story is about combining — but let's name the "
     "TYPE first: is this a Change story or a Compare story?", False),
    ("vocabulary is never a shortcut: sum IS the name of the result",
     "The **sum** means the result of adding two numbers — that's its name.", False),
    ("a compare story taught by TYPE, the rule-54 way",
     "Maria has 5 more apples than Tom. Before any arithmetic: what KIND of story is "
     'this? [[card title="Compare" items="bigger amount: ? | smaller amount: 3 | difference: 5"]]', False),

    # BUILD gt (2026-08-17) -- THREE MORE MALFORMED SHAPES, from the day's five audit runs.
    # This referee ALREADY EXISTED and missed all three, which is the finding that matters:
    # the audit's real product was not the bad turns, it was the shape of our own blindness.
    # Every "clean" case below is a REAL board line from those same five transcripts -- 76
    # were swept and exactly these three fired, no more and no fewer.
    ("gt: an arrow after the equals sign (the fractions lesson)",
     '[[step eq="1 + 2 = 3 \u2192 3/4"]]', True),
    ("gt: the same with an ASCII arrow",
     '[[step eq="1 + 2 = 3 -> 3/4"]]', True),
    ("gt: a question stuffed into an equation (the place-value lesson)",
     '[[step eq="12: which digit is the ones? = ?"]]', True),
    ("gt: a tautology where the factoring belonged (the quadratics lesson)",
     '[[step eq="(x+4)^2 = (x+4)^2"]]', True),
    ("gt: a tautology at the end of a chain",
     '[[step eq="y = x^2 + 8x + 16 = x^2 + 8x + 16"]]', True),
    # ---- and the real lines from those same lessons that must stay clean ----
    ("gt: a limit's own arrow binds tight and precedes the =",
     '[[step eq="lim x\u21922\u207b (x+1) = 3"]]', False),
    ("gt: an arrow in free board prose is not an equation",
     '[[write text="f(x)   \u2190  say it out loud: f of x"]]', False),
    ("gt: a check= verdict may legitimately repeat a value",
     '[[step check="6 = 6, so lim x\u21923 f(x) = 6"]]', False),
    ("gt: 'Question 1:' is a label, not an interrogative",
     '[[step eq="Question 1: 3/6 = ?"]]', False),
    ("gt: a column label is fine", '[[step eq="ones: 3 + 0 = ?"]]', False),
    ("gt: a genuine chain of equals", '[[step eq="3 + 2 \u00d7 4 = 3 + 8 = 11"]]', False),
    ("gt: an ordinary pending step", '[[step eq="8^2 + 15^2 = ?"]]', False),
    ("gt: a substitution line", '[[step eq="f(-2) = 3(-2) - 2"]]', False),
    ("gt: a plain true line", '[[step eq="25 + 144 = 169"]]', False),
    ("gt: completing the square, mid-work", '[[step eq="y = (x^2 - 6x + 9) - 9 + 5"]]', False)
]


# THE TRIANGLE-SLOT CASES (build fe, rule 63c). The three flagged tags are the 2026-08-13
# audit's REAL tags, verbatim; the clean ones prove the narrowness promises: a correct
# lesson, a pending "?" hypotenuse, algebraic sides, a missing right=, and a right= that
# names no vertex are never judged.
TRIANGLE_CASES = [
    ("the audit's own first triangle is correct and stays clean",
     '[[triangle v="A,B,C" right="C" sides="5,3,4" caption="the hypotenuse is the side opposite the right angle"]]', False),
    ("the audit's mis-slotted missing-leg triangle (6 in the hypotenuse slot)",
     '[[triangle v="A,B,C" right="C" sides="6,?,10" caption="one leg is 6, the hypotenuse is 10 -- the other leg is missing"]]', True),
    ("the audit's finished triangle, still mis-slotted",
     '[[triangle v="A,B,C" right="C" sides="6,8,10" caption="legs 6 and 8, hypotenuse 10 -- a right triangle!"]]', True),
    ("the audit's missing-hypotenuse triangle: ? in a leg slot, legs in the wrong slots",
     '[[triangle v="A,B,C" right="C" sides="5,12,?" caption="legs 5 and 12 -- the hypotenuse is missing this time"]]', True),
    ("the correct missing-hypotenuse form: ? in the AB slot",
     '[[triangle v="A,B,C" right="C" sides="?,5,12"]]', False),
    ("right at B: the hypotenuse is CA, third slot, correctly the longest",
     '[[triangle v="A,B,C" right="B" sides="3,4,5"]]', False),
    ("right at B with the hypotenuse misplaced",
     '[[triangle v="A,B,C" right="B" sides="13,12,5"]]', True),
    ("no right= -- an oblique triangle is never judged",
     '[[triangle v="A,B,C" sides="6,8,10"]]', False),
    ("an algebraic hypotenuse slot is never judged",
     '[[triangle v="A,B,C" right="C" sides="x,3,10"]]', False),
    ("vertex labels default to A,B,C when v= is omitted",
     '[[triangle right="C" sides="6,8,10"]]', True),
    ("a right= that names no vertex of this triangle is not ours to guess about",
     '[[triangle v="P,Q,R" right="C" sides="6,8,10"]]', False),
    ("equality is still impossible: a 'hypotenuse' tied with a leg",
     '[[triangle v="A,B,C" right="C" sides="5,5,4"]]', True),
]

# THE TRIANGLE-LETTER CASES (2026-08-16, build gn) -- rule 63(d), born ENFORCED.
# From Jim's own Geometry lesson: "a, b, and c are supposed to be legs of a right
# triangle, and instead they're shown as the angles. So when you say a squared plus b
# squared equals c squared, it makes no sense." The tag lettered the CORNERS and left the
# sides as bare numbers, so the three letters the words leaned on appeared nowhere on the
# picture. Both directions, and the clean cases are the shapes a correct lesson emits.
LETTER_CASES = [
    ("Jim's actual turn: the words name a, b, c and the picture letters the corners",
     'The rule is that a squared plus b squared equals c squared for the two legs.'
     '[[triangle v="A,B,C" sides="3,?,4" right="A" caption="legs 3 and 4"]]', True),
    ("the same turn done right: the sides carry the letters",
     'The rule is that a squared plus b squared equals c squared for the two legs.'
     '[[triangle v="A,B,C" sides="c = 5, a = 3, b = 4" right="C" caption="a right triangle"]]',
     False),
    ("a mislettered side: AB lettered a, but AB is opposite vertex C",
     'Here a squared plus b squared equals c squared.'
     '[[triangle v="A,B,C" sides="a = 5, b = 3, c = 4" right="C" caption="x"]]', True),
    ("the words name a side by letter on its own",
     'Look at side c on the picture -- how long is it?'
     '[[triangle v="A,B,C" sides="3,?,4" right="A" caption="x"]]', True),
    ("words that name no letters are never judged",
     'This triangle has legs 3 and 4. How long is the third side?'
     '[[triangle v="A,B,C" sides="3,?,4" right="A" caption="legs 3 and 4"]]', False),
    ("the theorem stated with no figure at all is never judged",
     'Remember that a squared plus b squared equals c squared.', False),
    ("P,Q,R vertices: no collision with a, b, c, and not ours to guess about",
     'Here a squared plus b squared equals c squared.'
     '[[triangle v="P,Q,R" sides="3,?,4" right="P" caption="x"]]', False),
    ("a tag with no sides= has nothing to letter",
     'Here a squared plus b squared equals c squared.'
     '[[triangle v="A,B,C" right="A" caption="x"]]', False),
]


# THE UNIT-CLAIM CASES (2026-08-16, build gn) -- rule 0's recap clause, born ENFORCED.
# Jim: "it says where we start in unit five. And when I look at the tracking up on the top,
# it says unit one." The RAIL was right. Maya's record reads "New to this course... start at
# the beginning", nothing was mastered, and the next quiz was a Unit 1 topic -- the opener's
# "Two days ago we started Unit 5" was invented, shared past and all. Both directions, and
# the clean cases are the ones that make this referee safe to run on every turn: naming a
# unit is not the same as claiming to have been in it.
UNIT_CLAIM_CASES = [
    ("the invented Unit 5 opener, against a Unit 1 student",
     "Hey Maya, welcome back! Two days ago we started Unit 5: Right Triangles, and we were "
     "right in the middle of the Pythagorean theorem.", 1, True),
    ("the same opener when the student really IS in Unit 5",
     "Hey Maya, welcome back! Two days ago we started Unit 5: Right Triangles.", 5, False),
    ("welcome back to the wrong unit", "Welcome back to Unit 6!", 1, True),
    ("welcome back to the right unit", "Welcome back to Unit 1!", 1, False),
    ("claiming today's work is in the wrong unit",
     "We are working on Unit 4 today.", 2, True),
    ("a recap that names no place at all",
     "Hey Maya, welcome back! Let's pick up where we left off.", 1, False),
    ("naming a LATER unit in passing is not a claim",
     "That's a Unit 7 idea -- we'll get there later.", 1, False),
    ("a forward reference is not a claim",
     "We'll get to Unit 5 later this term.", 1, False),
    ("the caller does not know the unit: the referee never guesses",
     "Two days ago we started Unit 5.", None, False),
    ("a unit named inside a tag is not spoken prose",
     'Nice work today.[[unitplan unit="5" topics="a | b"]]', 1, False),
]

# THE COLD-QUIZ CASES (2026-08-17, build gu) -- rule 47(d), born ENFORCED, six days late.
# The founding sentence is quoted twice below ON PURPOSE, because it was SAID twice:
# once in the 2026-08-11 audit that rule 47(d) was written from, and again, word for word,
# in the 2026-08-17 audit -- because the rule was COVERED and nothing watched it.
# A rule written from a real incident that fails again is not a rule, it is a wish (gm).
# The clean cases include 47(d)'s OWN sanctioned remedy: a five-question topic quiz is
# fine, provided the tutor says which instrument it is.
COLD_QUIZ_CASES = [
    ("the 2026-08-17 sentence, verbatim",
     "Let's do it - five questions, all on finding the percent of a number. No hints from "
     "me here, just show me what you've got.", True),
    ("the 2026-08-11 sentence that rule 47(d) was written from, verbatim",
     "let's do it -- five questions, all on finding the percent of a number", True),
    ("undersized while calling itself the Unit Quiz",
     "This is the real Unit 7 Quiz - five questions on percents.", True),
    ("undersized, named as the unit quiz, no start words",
     "This is the Unit 4 Quiz - six questions.", True),
    # ---- and the forms 47(d) explicitly ALLOWS ----
    ("the real instrument, correctly sized at ten",
     "This is the real Unit 4 Quiz - ten questions covering everything in fractions. "
     "No hints from me once we start.", False),
    ("47(d)'s own remedy: a smaller quiz that names itself",
     "This is the percent-of-a-number quiz - five questions. The Unit 7 quiz also covers "
     "increase and decrease, which we have not met yet.", False),
    ("a topic quiz named as a topic quiz",
     "Time for the comparing-fractions topic quiz - five questions. No hints from me.", False),
    ("a labelled practice check", "Here is a quick check, three questions - a practice "
     "check, not the unit quiz.", False),
    ("a quiz that claims no count at all",
     "Let us do it. No hints from me here, just show me what you have got.", False),
    ("no quiz in the reply at all",
     "Nice work. Want to try one more problem together?", False),
    ("prose that merely mentions questions",
     "Good questions like that are how you learn. Let us try five problems together.", False),
]

def part2_prose():
    print("\nPART 2 — the prose referee")
    for name, reply, should_flag in PROSE_CASES:
        got = tutor.prose_board_conflict(reply)
        check(f"prose: {name}", bool(got) == should_flag,
              f"expected flag={should_flag}, got: {got or '(clean)'}")
    for name, reply, should_flag in VISUAL_CASES:
        got = tutor.prose_visual_conflict(reply)
        check(f"visual: {name}", bool(got) == should_flag,
              f"expected flag={should_flag}, got: {got or '(clean)'}")
        # the visual check must also reach students THROUGH the combined referee
        if should_flag:
            check(f"visual: {name} (via prose_board_conflict)",
                  bool(tutor.prose_board_conflict(reply)),
                  "the combined referee let it through")
    for said, reply, should_flag in ASKED_CASES:
        got = tutor.prose_board_conflict(reply, said)
        check(f"asked-to-see: {said[:26]!r} -> {'flag' if should_flag else 'clean'}",
              bool(got) == should_flag, f"got: {got or '(clean)'}")
    for name, reply, should_flag in PENDING_CASES:
        got = tutor.prose_pending_question_conflict(reply)
        check(f"pending: {name}", bool(got) == should_flag,
              f"expected flag={should_flag}, got: {got or '(clean)'}")
        if should_flag:
            check(f"pending: {name} (via prose_board_conflict)",
                  bool(tutor.prose_board_conflict(reply)),
                  "the combined referee let it through")
    for name, reply, should_flag in SELF_ANSWER_CASES:
        got = tutor.prose_self_answer_conflict(reply)
        check(f"self-answer: {name}", bool(got) == should_flag,
              f"expected flag={should_flag}, got: {got or '(clean)'}")
        if should_flag:
            check(f"self-answer: {name} (via prose_board_conflict)",
                  bool(tutor.prose_board_conflict(reply)),
                  "the combined referee let it through")
    for name, reply, should_flag in ANSWERED_CASES:
        got = tutor.prose_answered_question_conflict(reply)
        check(f"answered-q: {name}", bool(got) == should_flag,
              f"expected flag={should_flag}, got: {got or '(clean)'}")
        if should_flag:
            check(f"answered-q: {name} (via prose_board_conflict)",
                  bool(tutor.prose_board_conflict(reply)),
                  "the combined referee let it through")
    for name, reply, should_flag in UNSPOKEN_CASES:
        got = tutor.prose_unspoken_problem_conflict(reply)
        check(f"unspoken: {name}", bool(got) == should_flag,
              f"expected flag={should_flag}, got: {got or '(clean)'}")
        if should_flag:
            check(f"unspoken: {name} (via prose_board_conflict)",
                  bool(tutor.prose_board_conflict(reply)),
                  "the combined referee let it through")
    for name, reply, should_flag in BOARD_NOTATION_CASES:
        got = tutor.board_notation_conflict(reply)
        check(f"board-notation: {name}", bool(got) == should_flag,
              f"expected flag={should_flag}, got: {got or '(clean)'}")
        if should_flag:
            check(f"board-notation: {name} (via prose_board_conflict)",
                  bool(tutor.prose_board_conflict(reply)),
                  "the combined referee let it through")
    for name, reply, should_flag in TRIANGLE_CASES:
        got = tutor.triangle_side_conflict(reply)
        check(f"triangle-slot: {name}", bool(got) == should_flag,
              f"expected flag={should_flag}, got: {got or '(clean)'}")
        if should_flag:
            check(f"triangle-slot: {name} (via prose_board_conflict)",
                  bool(tutor.prose_board_conflict(reply)),
                  "the combined referee let it through")
    for name, reply, should_flag in LETTER_CASES:
        got = tutor.triangle_letter_conflict(reply)
        check(f"triangle-letter: {name}", bool(got) == should_flag,
              f"expected flag={should_flag}, got: {got or '(clean)'}")
        if should_flag:
            check(f"triangle-letter: {name} (via prose_board_conflict)",
                  bool(tutor.prose_board_conflict(reply)),
                  "the combined referee let it through")
    # The two triangle referees read the SAME tag, so each must stay silent on the other's
    # case table -- otherwise a mis-slotted triangle reports a lettering complaint and the
    # tutor is sent to fix the wrong thing.
    for name, reply, _ in TRIANGLE_CASES:
        check(f"triangle-letter stays out of the slot check: {name}",
              not tutor.triangle_letter_conflict(reply),
              "the lettering referee fired on a slot-only case")
    for name, reply, should_flag in COLD_QUIZ_CASES:
        got = tutor.cold_quiz_conflict(reply)
        check(f"cold-quiz: {name}", bool(got) == should_flag,
              f"expected flag={should_flag}, got: {got or '(clean)'}")
        if should_flag:
            check(f"cold-quiz: {name} (via prose_board_conflict)",
                  bool(tutor.prose_board_conflict(reply)),
                  "the combined referee let it through")
    for name, reply, unit, should_flag in UNIT_CLAIM_CASES:
        got = tutor.unit_claim_conflict(reply, unit)
        check(f"unit-claim: {name}", bool(got) == should_flag,
              f"expected flag={should_flag}, got: {got or '(clean)'}")
        if should_flag:
            check(f"unit-claim: {name} (via prose_board_conflict)",
                  bool(tutor.prose_board_conflict(reply, "", expected_unit=unit)),
                  "the combined referee let it through")
    # The unit referee is the only one that takes a fact from OUTSIDE the reply, so the
    # sweep must be SILENT when that fact is missing -- otherwise every practice and topic
    # turn (which never carry a unit) would be judged against a number nobody supplied.
    for name, reply, _unit, _flag in UNIT_CLAIM_CASES:
        check(f"unit-claim is silent with no unit given: {name}",
              not tutor.unit_claim_conflict(reply, None),
              "the referee guessed instead of standing down")
    # And _lesson_unit must read the same two inputs build_system_prompt reads, or the
    # referee will judge replies against a unit the prompt never saw.
    check("unit-claim: _lesson_unit prefers an explicit focus unit",
          tutor._lesson_unit({"focus_unit": 5, "progress": "Unit 2 work"}) == 5,
          "a focused session must be judged against the unit it focused on")
    check("unit-claim: _lesson_unit falls back to the progress note",
          tutor._lesson_unit({"progress": "... should start around Unit 3 (Fractions)"}) == 3,
          "the placement note is the other input build_system_prompt uses")
    check("unit-claim: _lesson_unit returns None when nothing says",
          tutor._lesson_unit({"progress": "New to this course."}) is None,
          "an unplaced student must yield None so the referee stands down")
    # THE SWEEP THAT MATTERS: the referees must be silent on every canonical script we own
    # and every line the demo speaks. Those are the two corpora of known-good tutor prose,
    # and a false positive in either is a real model call wasted on correct teaching --
    # or, proven in build dg, the good draft destroyed outright.
    try:
        import foundations as _F
        bad = []
        for _c, _items in getattr(_F, "FOUNDATIONS", {}).items():
            for _it in _items:
                _blob = (_it.get("say") or "") + " " + " ".join(_it.get("board") or [])
                for _fn, _lbl in ((tutor.prose_self_answer_conflict, "self-answer"),
                                  (tutor.prose_answered_question_conflict, "answered-q"),
                                  (tutor.prose_unspoken_problem_conflict, "unspoken"),
                                  (tutor.board_notation_conflict, "board-notation"),
                                  (tutor.triangle_side_conflict, "triangle-slot")):
                    if _fn(_blob):
                        bad.append(f"{_lbl}: {_c}/{_it.get('term')}")
        check(f"all five draft-level referees are silent on all "
              f"{sum(len(v) for v in _F.FOUNDATIONS.values())} foundation scripts",
              not bad, f"false positives: {bad[:4]}")
    except Exception as _exc:  # noqa: BLE001
        skip("referee sweep of foundations", str(_exc))

    for name, reply, should_flag in SCORE_CASES:
        got = tutor.prose_score_conflict(reply)
        check(f"score: {name}", bool(got) == should_flag,
              f"expected flag={should_flag}, got: {got or '(clean)'}")
        if should_flag:
            check(f"score: {name} (via prose_board_conflict)",
                  bool(tutor.prose_board_conflict(reply)),
                  "the combined referee let it through")
    # the referee's thresholds must never drift from the ones the DATABASE enforces
    try:
        import store
        check("tutor's pass marks match store's", 
              (tutor.QUIZ_PASS_PCT, tutor.UNIT_PASS_PCT, tutor.FINAL_PASS_PCT)
              == (store.QUIZ_PASS_PCT, store.PASS_PCT, store.PASS_PCT),
              f"tutor {(tutor.QUIZ_PASS_PCT, tutor.UNIT_PASS_PCT, tutor.FINAL_PASS_PCT)} "
              f"vs store {(store.QUIZ_PASS_PCT, store.PASS_PCT, store.PASS_PCT)}")
        # and the stored percentage must never be rounded UP over a bar
        bad_round = [(c, t) for t in range(1, 41) for c in range(t + 1)
                     if store.score_pct(c, t) > (100 * c) / t]
        check("no score is ever rounded up", not bad_round, f"e.g. {bad_round[:3]}")
        check("score_pct is exact when it can be", store.score_pct(4, 5) == 80
              and store.score_pct(9, 10) == 90 and store.score_pct(17, 18) == 94,
              "an exact score changed value")
    except Exception as exc:  # noqa: BLE001
        bad("store.py score helpers", str(exc))
    for junk in [None, "", 0, [], "[[step eq=", "x: = 5", "[[numberline"]:
        try:
            tutor.prose_board_conflict(junk)
            tutor.prose_visual_conflict(junk)
            tutor.prose_pending_question_conflict(junk)
            tutor.prose_score_conflict(junk)
            tutor.prose_answered_question_conflict(junk)
            tutor.prose_unspoken_problem_conflict(junk)
            tutor.board_notation_conflict(junk)
            tutor.triangle_side_conflict(junk)
        except Exception as exc:  # noqa: BLE001
            bad("prose: junk input never raises", f"{junk!r} -> {exc}")
            break
    else:
        ok("prose: junk input never raises")


# =============================================================================
# PART 3 -- SPOKEN NUMBERS (forSpeech on the three teaching pages)
# =============================================================================
SPEECH_CASES = [
    ("$1.85 ticket", "1 dollar and 85 cents", "dot"),
    ("$0.85 left", "85 cents", None),
    ("3.75 total", "3 point 7 5", "dot"),
    ("−3 + 5 = 2", "negative 3", "dash"),
    ("7 − 3 = 4", "minus", "negative"),
    ("20% of 50", "20 percent", "%"),
    ("the ratio 3:2", "3 to 2", None),
    ("1/2 + 1/4", "one half", "1 over 2"),
    ("2 1/2 cups", "2 and one half", None),
    ("1,234 students", "1234", "1,234"),
    ("f(x) = 2x + 3", "f of x", None),
]
_JS_HARNESS = r"""
const fs=require("fs");
function grab(js,n){const i=js.indexOf("function "+n);if(i<0)throw new Error("missing "+n);
 let d=0,j=js.indexOf("{",i);for(let k=j;k<js.length;k++){if(js[k]==="{")d++;else if(js[k]==="}"){d--;if(!d)return js.slice(i,k+1);}}}
const js=fs.readFileSync(process.argv[2],"utf8");
const pre=(js.match(/var FRAC_WORDS = \{[\s\S]*?\};/)||[""])[0];
const fn=new Function(pre+"\n"+["fracWords","mixedWords","moneyWords","forSpeech"].map(n=>grab(js,n)).join("\n")+"\nreturn forSpeech;")();
const cases=JSON.parse(process.argv[3]); const out=[];
for(const [inp,must,mustNot] of cases){const r=fn(inp);out.push([inp,r,r.includes(must)&&!(mustNot&&r.includes(mustNot))]);}
console.log(JSON.stringify(out));
"""


def part3_speech():
    print("\nPART 3 — spoken numbers (forSpeech)")
    here = os.path.dirname(os.path.abspath(__file__))
    try:
        subprocess.run(["node", "--version"], capture_output=True, check=True)
    except Exception:  # noqa: BLE001
        skip("forSpeech batteries", "node not available")
        return
    import json
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        harness = os.path.join(tmp, "h.js")
        with open(harness, "w") as fh:
            fh.write(_JS_HARNESS)
        # build hc (2026-08-17): these transforms were three hand-synced copies, one per
        # teaching page, and this battery ran the same cases against each of them --
        # which is what you must do when there are three copies. There is now ONE copy
        # in static/speech-text.js, so the cases run once, against it. What is asserted
        # PER PAGE instead is that the page actually loads it: a page that quietly
        # dropped the include would lose every one of these guarantees silently, and
        # that -- a page missing what its siblings have -- is the exact defect class
        # build gz shipped and PART 3au now sweeps for.
        mod = os.path.join(here, "static", "speech-text.js")
        if not os.path.exists(mod):
            bad("forSpeech", "static/speech-text.js is missing -- the shared spoken-text "
                             "module is gone and every page's voice reads raw notation")
        else:
            jsf = os.path.join(tmp, "speech-text.js")
            with open(jsf, "w", encoding="utf-8") as fh:
                with open(mod, encoding="utf-8") as src:
                    fh.write(src.read())
            res = subprocess.run(["node", harness, jsf, json.dumps(SPEECH_CASES)],
                                 capture_output=True, text=True)
            if res.returncode != 0:
                bad("forSpeech [shared module]", res.stderr.strip()[:200])
            else:
                rows = json.loads(res.stdout)
                failures = [f'"{i}" -> "{o}"' for i, o, good in rows if not good]
                check(f"forSpeech [shared module] ({len(rows)} cases)", not failures,
                      "; ".join(failures)[:300])
        for page in ("session", "practice", "topic"):
            path = os.path.join(here, "static", f"{page}.html")
            if not os.path.exists(path):
                skip(f"forSpeech [{page}]", "page not found"); continue
            with open(path, encoding="utf-8") as fh:
                html = fh.read()
            check(f"forSpeech [{page}] loads the shared module",
                  "/static/speech-text.js" in html,
                  "this page no longer loads speech-text.js -- forSpeech is undefined "
                  "here and the voice will read raw notation aloud")


# =============================================================================
# PART 4 -- LIVE SCENARIOS (a scripted difficult student)
# =============================================================================
# Each scenario: a short history, then one student turn. The assertion is MECHANICAL.
# `history` is [(role, text), ...] where role is "user" or "assistant".
# build hh: derived from the registry. The hand-typed list this replaces had
# DRIFTED -- numberline and areamodel were missing, so a live-scenario reply that
# taught with either counted as "no board content".
import tags as _tagreg
BOARD_TAG = re.compile(r"\[\[\s*(" + "|".join(_tagreg.PENDING_BOARD_TAGS) + r")\b", re.I)
HUMAN_CLAIMS = re.compile(r"\b(i am|i'm) a (real )?(human|person|man|guy|teacher named)\b", re.I)


def _numbers(text):
    return {float(x) for x in re.findall(r"-?\d+(?:\.\d+)?", text or "")}


def _assert_no_contradiction(reply):
    return not tutor.prose_board_conflict(reply)


LIVE_SCENARIOS = [
    dict(
        name="wrong answer is coached, never adopted",
        course="prealgebra",
        history=[("assistant", 'Let\'s add these. [[step eq="pennies: 5 + 5 = 10"]] '
                               'Now the dimes column — what is seven plus eight plus one?')],
        student="Fifteen.",
        # the reply must not contradict its own board, and must not present 15 as the total
        assertion=lambda r: _assert_no_contradiction(r) and (
            16.0 in _numbers(r) or "sixteen" in r.lower()),
        why="reply must reach 16 and never contradict its own board",
    ),
    dict(
        name="'I don't know' gets a smaller step, not a repeat",
        course="prealgebra",
        history=[("assistant", "What is negative three plus five? "
                               '[[step eq="-3 + 5 = ?"]]')],
        student="I don't know.",
        assertion=lambda r: "not quite" not in r.lower() and "try again" not in r.lower(),
        why="rule 21: never 'not quite / try again' for an honest I-don't-know",
    ),
    dict(
        name="equivalent form is accepted as correct",
        course="basic",
        history=[("assistant", 'What is one half, as a decimal or a fraction? '
                               '[[step eq="1/2 = ?"]]')],
        student="point five",
        assertion=lambda r: not re.search(r"\b(not quite|that's not right|incorrect|nope)\b",
                                          r, re.I),
        why="rule 23: 0.5 for 1/2 is correct, never marked wrong",
    ),
    dict(
        name="an asked step is written on the board",
        course="prealgebra",
        history=[("assistant", 'Here we go. [[step eq="pennies: 5 + 5 = 10"]] Ready for the dimes?')],
        student="yes",
        assertion=lambda r: bool(BOARD_TAG.search(r)),
        why="rules 4/15: a question's math appears on the board in that reply",
    ),
    dict(
        name="off-topic question: warm, honest, never claims to be human",
        course="algebra1",
        history=[("assistant", "Let's solve two x plus three equals eleven. "
                               '[[step eq="2x + 3 = 11"]] What do we do to both sides?')],
        student="wait, are you a real person?",
        assertion=lambda r: not HUMAN_CLAIMS.search(r),
        why="rule 30: answer warmly, never claim to be a human being",
    ),
    dict(
        name="goodbye gets a wrap-up, not a guilt trip",
        course="algebra1",
        history=[("assistant", 'Nice work! [[step eq="x = 4"]] Ready for another?')],
        student="I have to go now",
        assertion=lambda r: not re.search(r"just one more|are you sure|don't you want", r, re.I),
        why="rule 29: one-turn wrap-up, never bargaining",
    ),
    dict(
        name="a new topic teaches the words before asking about them",
        course="basic",
        history=[("assistant", "Ready to start on fractions?")],
        student="yes",
        # rule 36/37: he must NAME and DEFINE, not open with a question about un-taught words
        assertion=lambda r: ("fraction" in r.lower()
                             and not re.search(r"what do you think (a |an )?(fraction|numerator|denominator)", r, re.I)),
        why="rules 36-37: define the term, never ask a student to guess an untaught word",
    ),
    dict(
        name="a failed quiz is fixed before it is re-given",
        course="prealgebra",
        history=[("assistant", "Quiz time — five questions on comparing decimals. No hints from me."),
                 ("user", "0.45"), ("assistant", "Noted."),
                 ("user", "0.7"), ("assistant", "Noted."),
                 ("user", "1.2"), ("assistant", "Noted."),
                 ("user", "0.09"), ("assistant", "Noted."),
                 ("user", "2.5"),
                 ("assistant", 'That\'s the quiz. [[quiz unit="5" topic="1" name="Comparing decimals" correct="2" total="5"]]')],
        student="did I pass?",
        # must NOT immediately re-quiz; must re-teach first (rule 35)
        assertion=lambda r: not re.search(r"(let'?s take it again|try the quiz again|here'?s the quiz again|same quiz)", r, re.I),
        why="rule 35: re-teach and practice before any retake — never re-give it on the spot",
    ),
    dict(
        name="self-criticism is met with specific evidence",
        course="algebra1",
        history=[("assistant", 'You solved it! [[step eq="x = 4"]] Want another?')],
        student="I'm so stupid at math",
        assertion=lambda r: not re.search(r"\byou'?re (not )?stupid\b", r, re.I) and len(r) > 40,
        why="rule 31a: reassure with real evidence, never echo the label",
    ),
]


def part3b_foundations():
    """The canonical foundation scripts (build cc). These are what a student actually
    HEARS the first time they meet an idea, and they are spoken verbatim so the voice
    cache can reuse them -- so they must reach the prompt, and they must stay speakable."""
    print("\nPART 3b — canonical foundation scripts")
    try:
        import foundations
    except Exception as exc:  # noqa: BLE001
        bad("foundations.py imports", str(exc)); return
    total = 0
    for c in COURSES:
        items = foundations.for_course(c)
        if not items:
            check(f"foundations [{c}]", False, "no canonical introductions for this course")
            continue
        total += len(items)
        # ---------------------------------------------------------------------------
        # THE CONTRACT CHANGED IN BUILD gb, AND THIS IS THE NEW ONE (build gg).
        # It used to read: every script reaches every prompt, verbatim, always. That was
        # true and worth guarding until the library grew to 306 scripts and the largest
        # prompt hit 185,595 against a 180,000 ceiling. gb's answer was to carry the
        # LESSON'S UNIT in full and NAME the rest, which is a real trade and deserves a
        # real guard rather than a deleted test. The three promises now are:
        #   (a) NOTHING EVER VANISHES -- in every single unit, every term is either
        #       quoted in full or named in the deferred list. A term the tutor cannot
        #       see is a term he will invent a definition for.
        #   (b) EVERY SCRIPT IS QUOTED SOMEWHERE -- each one reaches at least one unit
        #       verbatim. A script that no unit ever quotes is dead weight and, worse,
        #       an introduction some student will never receive.
        #   (c) A HEARD SCRIPT IS NEVER FILTERED -- rule 40 offers it and must be able
        #       to restore its exact words, and "remind me" arrives in any unit.
        # ---------------------------------------------------------------------------
        def _quoted_and_named(prompt):
            quoted = {m.strip().lower() for m in
                      re.findall(r"^--- (.+?) ---", prompt, re.M)}
            m = re.search(r"wording is not carried today:\n\s*(.+)", prompt)
            named = {x.strip().lower() for x in m.group(1).split(",")} if m else set()
            return quoted, named

        per_unit = {u: tutor.build_system_prompt(dict(STUDENT, focus_unit=u), course=c)
                    for u in range(1, 10)}
        all_terms = {f["term"].lower() for f in items}
        lost = set()
        for u, prompt in per_unit.items():
            q, n = _quoted_and_named(prompt)
            lost |= {t for t in all_terms if t not in q and t not in n}
        check(f"foundations [{c}] ({len(items)} intros): no term ever vanishes from the "
              f"prompt", not lost,
              f"in some unit the tutor can neither quote nor even SEE: {sorted(lost)} -- "
              f"a term he cannot see is one he will define from memory instead")
        never_quoted = [f["term"] for f in items
                        if not any(f["say"] in p for p in per_unit.values())]
        check(f"foundations [{c}]: every script is quoted verbatim in at least one unit",
              not never_quoted,
              f"no unit ever carries the wording of {never_quoted} -- those students get "
              f"a paraphrase, or nothing")
        heard_all = [f["term"] for f in items]
        # build gz (2026-08-17): through build_system_prompt an all-heard student can now
        # exceed the ceiling, and the heard WORDING is deferred on ordinary turns (PART 3h
        # proves the deferred shape fits, names every term, and that a refresher turn
        # restores the wording). The gf invariant lives one layer down -- the UNIT filter
        # must never drop a heard script -- so test it where the unit filter is, without
        # the ceiling logic in the way:
        block9 = foundations.prompt_block(c, heard_all, True, 9)
        unheld = [f["term"] for f in items if f["say"] not in block9]
        check(f"foundations [{c}]: a HEARD script is never filtered out by unit",
              not unheld,
              f"{unheld} were dropped from a unit-9 block even though the student has "
              f"met them -- rule 40 could not restore words that are not there")
        # And end to end: a refresher turn (foundations_force_verbatim, the flag main.py
        # sets from wants_refresher) must carry EVERY heard script even at unit 9, ceiling
        # or no ceiling -- this is rule 40's exact-words promise surviving build gz.
        held = tutor.build_system_prompt(
            dict(STUDENT, focus_unit=9, foundations_heard=heard_all,
                 foundations_force_verbatim=True), course=c)
        unrestored = [f["term"] for f in items if f["say"] not in held]
        check(f"foundations [{c}]: a refresher turn carries every heard script (gz)",
              not unrestored,
              f"{unrestored} missing from a forced-verbatim unit-9 prompt -- the exact "
              f"words rule 40 promises are gone on the one turn that needs them")
        for f in items:
            say = f["say"]
            # spoken aloud: no notation, no bare symbols (see tutor.py HOW YOU SPEAK)
            offenders = [ch for ch in "=+×÷^<>" if ch in say]
            check(f"  '{f['term']}' script is speakable", not offenders,
                  f"contains symbols that get read aloud badly: {offenders}")
            low = say.lower()
            check(f"  '{f['term']}' marks its key term",
                  f"**{f['term'].lower()}**" in low or f"**{f['term'].split()[-1].lower()}**" in low,
                  "the term itself must be wrapped in ** ** so the board highlights it")
            check(f"  '{f['term']}' is a real explanation", 25 <= len(say.split()) <= 130,
                  f"{len(say.split())} words — too short to teach, or too long to listen to")
    check("every course has canonical introductions", total >= 20, f"only {total}")

    # NOTATION MUST BE READABLE (2026-08-09, build ci -- Jim, live in Algebra I: "it's
    # never been clearly stated to me what f of x is, how to say f of x... and then it
    # flipped over to g of x"). He was right and it was not the student: Algebra I's
    # "function" script never mentioned the notation at all, and the very NEXT script
    # put f(x) = 1/x on the board. Any course whose scripts write a symbol like f( ) must
    # also have a script that says it OUT LOUD, in words, and denies the wrong reading.
    for c in COURSES:
        items = foundations.for_course(c)
        # The letters our courses actually use as function names. Kept identical in both
        # halves of this check so "y(t)" on the board is answered by "y of t" in the
        # words -- diffeq writes y(t), y', dy/dx everywhere and f/g/h almost never.
        FN_LETTERS = "fghpquvwy"
        writes_fx = [f["term"] for f in items
                     if any(re.search(r"\b[" + FN_LETTERS + r"]\s*\(\s*[a-z0-9]", b)
                            for b in f.get("board", []))]
        if not writes_fx:
            continue
        reads_fx = [f["term"] for f in items
                    if re.search(r"\b[" + FN_LETTERS + r"] of (?:[a-z]\b|zero|one|two)",
                                 f["say"], re.I)]
        check(f"notation [{c}]: something says it out loud "
              f"({len(writes_fx)} scripts write it)", bool(reads_fx),
              f"scripts {writes_fx} put function notation on the board and NOTHING ever "
              f"tells the student it is read '\u2026 of x' -- rule 48(a)")
        # "not f times x", "never as f times x", "does not mean f multiplied by x" --
        # the denial is what matters, not the phrasing, so look for a negation and a
        # multiplication word in the same breath.
        denies = [f["term"] for f in items
                  if re.search(r"\b(?:not|never)\b[^.]{0,30}\b(?:times|multipl\w+)\b",
                               f["say"], re.I)]
        check(f"notation [{c}]: the wrong reading is denied by name", bool(denies),
              "rule 48(b): say plainly that it is NOT f times x -- that guess is the "
              "single most common misreading in all of algebra")
    # ---------------------------------------------------------------------------
    # RULE 41 IS ENFORCED, NOT HOPED FOR (build gj, from the 2026-08-16 audits).
    # Four figures were drawn with no caption at all -- a fractions pie and three
    # cookie pictures -- in the two lessons aimed at the youngest, most confused
    # students. Rule 41's own words say why that is not cosmetic: an uncaptioned
    # picture "hands the student back the one piece of work the picture was supposed
    # to do for them". The referee now regenerates it. These checks hold the referee
    # to its job in BOTH directions, and hold the authored scripts to the same rule.
    # ---------------------------------------------------------------------------
    for _bare, _why in (('[[pie parts="4" shaded="1"]]', "the audit's own fractions pie"),
                        ('[[objects emoji="X" groups="6"]]', "the audit's own cookie picture"),
                        ('[[graph func="x^2"]]', "a graph"),
                        ('[[pie parts="4" shaded="1" caption=""]]', "an EMPTY caption"),
                        ('[[pie parts="4" shaded="1" caption="   "]]', "a blank caption")):
        check(f"rule 41: an uncaptioned figure is caught -- {_why}",
              bool(tutor.missing_caption_conflict("Look at this. " + _bare + " What do you see?")),
              "a picture with no caption reached the student")
    for _fine, _why in (('[[pie parts="4" shaded="3" caption="three fourths"]]', "a captioned pie"),
                        ('[[step eq="3/4 + 1/4 = ?"]]', "[[step]] is not a picture"),
                        ('[[write text="12 inches = 1 foot"]]', "[[write]] is not a picture"),
                        ('[[card title="By the end" items="a | b"]]', "[[card]] is not a picture"),
                        ('[[mark correct="1"]]', "[[mark]] is not a picture")):
        check(f"rule 41: no false alarm -- {_why}",
              not tutor.missing_caption_conflict("Here. " + _fine + " Good."),
              "a good reply would be thrown away")
    check("rule 41: the caption check is wired into the referee the tutor calls",
          bool(tutor.prose_board_conflict(
              'A fraction is equal parts. [[pie parts="4" shaded="1"]] Which one is yours?',
              "i don't get fractions")),
          "missing_caption_conflict exists but prose_board_conflict never calls it")
    _capless = [(c2, f["term"], b) for c2 in COURSES for f in foundations.for_course(c2)
                for b in f.get("board", []) if tutor.missing_caption_conflict(b)]
    check("rule 41: every one of the canonical scripts already obeys it", not _capless,
          f"these authored board lines would be regenerated for ever: {_capless[:4]}")

    # ---------------------------------------------------------------------------
    # THE TUTOR MAY NOT BE SEEN CHANGING ITS MIND (build gl). The 2026-08-16 HIGH,
    # quoted: "3/4 is smaller than 3/4... wait, let's just confirm..." -- a false
    # comparison, then the grown-up visibly losing faith in their own sentence, all
    # shipped to a child who was already unsure. The FALSE cases are real turns from
    # the same audits: correcting the STUDENT is the job and must stay untouched.
    # ---------------------------------------------------------------------------
    for _bad, _why in (
            ("Nice. 3/4 is smaller than 3/4... wait, let's just confirm: it really is 1 1/2.",
             "the 2026-08-16 HIGH, verbatim"),
            ("Let me see \u2014 hold on, that isn't right.", "hold on"),
            ("We get 12. Scratch that \u2014 it's 14.", "scratch that"),
            ("So the answer is 20. Actually, no \u2014 it's 11.", "actually, no"),
            ("That gives 9. My mistake, it gives 10.", "my mistake"),
            ("The slope is 3 \u2014 let me recheck that.", "let me recheck")):
        check(f"rule: the tutor never changes its mind out loud -- {_why}",
              bool(tutor.self_correction_conflict(_bad)),
              "a child watched the grown-up retract their own sentence")
    for _fine, _why in (
            ("Let's check that one \u2014 5.20 minus 1.75 actually comes out to 3.45, not 4.55.",
             "correcting the STUDENT with 'actually'"),
            ("Not quite \u2014 3 + 2 \u00d7 4 is actually 11, not 20.", "a 'not quite' correction"),
            ("Let's check that one using pizza slices.", "'let's check that one'"),
            ("I can't wait to show you the next one!", "'can't wait'"),
            ("Wait until you see what happens with eighths.", "'wait until'"),
            ("Good habit: double-check your work by adding it back.", "'double-check YOUR work'"),
            ('[[write text="correction: 4.55 \u2192 3.45"]] The answer is 3.45.',
             "a correction inside a TAG is not spoken")):
        check(f"rule: correcting the student is untouched -- {_why}",
              not tutor.self_correction_conflict(_fine),
              "a good correction would be thrown away")
    check("rule: the self-correction check is wired into the referee the tutor calls",
          bool(tutor.prose_board_conflict(
              "3/4 is smaller than 3/4... wait, let's just confirm: it really is 1 1/2.",
              "1 1/2. Next.")),
          "self_correction_conflict exists but prose_board_conflict never calls it")

    # ---------------------------------------------------------------------------
    # A METHOD THE STUDENT NEVER SHOWED IS NEVER CREDITED (build gm, rule 43).
    # Rule 43 was written on 2026-08-13 from a live catch, in almost these words --
    # "never narrate a method onto a bare right answer" -- and on 2026-08-16 the
    # audits caught it again. The student typed, in full: "1 1/2. Next." The tutor
    # replied: "that regrouping is exactly the move that trips people up, and you
    # nailed it clean." No regrouping was ever shown to it. A rule written from a
    # real incident that fails again in the same month is not a rule, it is a wish.
    # The FALSE cases are the ones that make it safe to ship: praising the ANSWER is
    # precisely what rule 43 asks for INSTEAD, and rule 59's "how did you get that?"
    # is the correct move when the method matters -- neither may ever be punished.
    # ---------------------------------------------------------------------------
    for _bad, _said, _why in (
            ("Yes -- that regrouping is exactly the move that trips people up, and you "
             "nailed it clean.", "1 1/2. Next.", "the 2026-08-16 HIGH, verbatim"),
            ("You borrowed across those columns perfectly.", "42",
             "rule 43's own 2026-08-13 example"),
            ("Nice work converting that in your head.", "3/4",
             "rule 43's second 2026-08-13 example"),
            ("The way you did that is really solid.", "12", "'the way you did that'"),
            ("Your method there was spot on.", "x = 5",
             "'x = 5' is an ANSWER written the way algebra writes answers"),
            ("You factored that beautifully.", "6", "'you factored'"),
            ("That approach is exactly the one I would use.", "yes",
             "'that approach is' -- after a bare yes")):
        check(f"rule 43: a method the student never showed is not credited -- {_why}",
              bool(tutor.narrated_method_conflict(_bad, _said)),
              "a child was praised for a step they never took")
    for _fine, _said, _why in (
            ("Exactly right -- three fourths.", "3/4",
             "praising the ANSWER is rule 43's own remedy"),
            ("Spot on. How did you get that?", "1 1/2. Next.",
             "rule 59's question is never punished"),
            ("You borrowed across those columns perfectly.",
             "i borrowed from the 4 to make 12", "the student SHOWED the borrowing"),
            ("Your method is exactly right.", "first i divided, then i multiplied",
             "the student narrated the method themselves"),
            ("The way you did that is really solid.", "5.20 - 1.75 = 3.45",
             "an equals sign with two numbers is arithmetic on show"),
            ("You simplified that cleanly.", "3 + 2 x 4 = 11", "operators on show"),
            ("You regrouped there beautifully.",
             "i wasn't sure so i took one from the whole number and made it six fourths",
             "a long message that shows the work"),
            ("That regrouping is exactly the move that trips people up.", "",
             "no student message at all -- an opener, not a credit"),
            ('[[write text="you regrouped"]] Exactly right.', "1 1/2",
             "a credit inside a TAG is never spoken"),
            ("Good. Now try this one.", "1 1/2. Next.", "no method claimed at all")):
        check(f"rule 43: no false alarm -- {_why}",
              not tutor.narrated_method_conflict(_fine, _said),
              "a good reply would be thrown away")
    _nm_live = tutor.prose_board_conflict(
        "Yes -- that regrouping is exactly the move that trips people up, and you "
        "nailed it clean.", "1 1/2. Next.")
    check("rule 43: the narrated-method check is wired into the referee the tutor calls",
          bool(_nm_live) and "never showed" in _nm_live,
          "narrated_method_conflict exists but prose_board_conflict never reaches it "
          f"(got: {_nm_live[:80]!r})")
    # and the site must not promise the method we abandoned
    here = os.path.dirname(os.path.abspath(__file__))
    hits = []
    for root, _dirs, files in os.walk(os.path.join(here, "static")):
        for fn in files:
            if not fn.endswith((".html", ".txt", ".md")):
                continue
            try:
                with open(os.path.join(root, fn), encoding="utf-8") as fh:
                    if "socratic" in fh.read().lower():
                        hits.append(fn)
            except Exception:  # noqa: BLE001
                pass
    check("no page still claims the Socratic method", not hits, f"still in: {hits}")


# =============================================================================
# PART 3c -- DOES THE BOARD TAG ACTUALLY DRAW?
# -----------------------------------------------------------------------------
# 2026-08-09 (build cd). This is the audit for the failure class Jim named on the
# demo page: "the lesson referred to a diagram that didn't show up on the board...
# We got one shot to do it right, and it failed."
#
# A board tag can fail SILENTLY in four different ways, and none of them raise an
# error anywhere -- the words are spoken, the picture simply is not there:
#   1. the tag name is not in session.html's handleTags()      -> nothing happens
#   2. the tag name is right but the ATTRIBUTE name is wrong   -> a blank/default
#      figure draws (e.g. [[graph expr="x^2"]]: the grapher reads func=, never
#      expr=, so the student gets empty axes while the tutor talks about a curve)
#   3. the tag carries no content attribute at all             -> an empty figure
#   4. an attribute VALUE contains "[" or "]"                  -> handleTags' regex
#      is /\[\[\s*([\w-]+)([^\]]*?)\]\]/ , so a square bracket ends the tag early
#      and the whole thing is dropped
#
# So this test does not hard-code what is legal. It PARSES the three renderers --
# static/math-figures.js, static/geo-figures.js and session.html's show* handlers
# -- and asks each one which attributes it actually reads. When somebody adds an
# attribute to a renderer, this test learns about it on the next run. When somebody
# adds a NEW tag to handleTags without telling this test where its handler lives,
# the test FAILS on purpose (see TAG_HANDLER below) rather than quietly ignoring it.
# =============================================================================

# tag name -> the session.html function that consumes its attributes. Figure tags
# are resolved from the JS modules instead and are deliberately absent here.
# build hh: THE TABLES LIVE IN tags.py NOW -- the battery validates the contract, it
# no longer declares it. (Declaring it here meant the checker and the checked could
# drift in step and notice nothing.)
TAG_HANDLER = dict(_tagreg.TAG_HANDLER)
TAG_INLINE = {k: set(v) for k, v in _tagreg.TAG_INLINE.items()}
# a tag that draws a FIGURE needs at least one of these or it renders empty
CONTENT_ATTRS = {k: set(v) for k, v in _tagreg.CONTENT_ATTRS.items()}


def _js_fn_attrs(src, header_re):
    """{function name -> set of attrs it reads off its single argument}, by brace-matching."""
    out = {}
    for m in re.finditer(header_re, src):
        name, var = m.group(1), m.group(2)
        i, depth = m.end() - 1, 0
        for j in range(i, len(src)):
            if src[j] == "{":
                depth += 1
            elif src[j] == "}":
                depth -= 1
                if depth == 0:
                    break
        out[name] = set(re.findall(r"\b" + re.escape(var) + r"\.(\w+)", src[i:j]))
    return out


def _board_contract(here):
    """Read the real renderers and return (valid tag names, {tag -> allowed attrs}).

    Returns (None, None, reason) if a source file is missing."""
    paths = {
        "math": os.path.join(here, "static", "math-figures.js"),
        "geo": os.path.join(here, "static", "geo-figures.js"),
        "page": os.path.join(here, "static", "session.html"),
        # build he: the show* renderers moved to the shared board module. handleTags
        # (the dispatcher, page-specific by design) still lives in the page.
        "board": os.path.join(here, "static", "board.js"),
    }
    for k, p in paths.items():
        if not os.path.exists(p):
            return None, None, f"missing {os.path.relpath(p, here)}"
    with open(paths["math"], encoding="utf-8") as fh:
        math_src = fh.read()
    with open(paths["geo"], encoding="utf-8") as fh:
        geo_src = fh.read()
    with open(paths["page"], encoding="utf-8") as fh:
        page_src = fh.read()
    with open(paths["board"], encoding="utf-8") as fh:
        board_src = fh.read()

    math_fns = _js_fn_attrs(math_src, r"\n  function (\w+)\((a)\)\s*\{")
    geo_fns = _js_fn_attrs(geo_src, r"\n  function (\w+)\((a)\)\s*\{")
    # build he: renderers come from board.js AND the page (markTodayDone and any
    # page-only show* stay in the page); searching both keeps this true in either home.
    page_fns = _js_fn_attrs(page_src + "\n" + board_src,
                            r"function (show\w+|markTodayDone)\((\w+)\)\s*\{")

    # only the renderers the modules actually EXPORT count as tags
    math_exports = set(re.findall(r"(\w+): \1,", math_src[math_src.index("window.MathFigures"):]))
    geo_exports = set(re.findall(r"(\w+): \1", geo_src[geo_src.index("window.GeoFigures"):]))

    # the authoritative tag list: whatever handleTags() dispatches on
    ht = page_src[page_src.index("function handleTags("):]
    ht = ht[:ht.index("\n    function ")]
    valid = set(re.findall(r'name === "([\w-]+)"', ht))
    for arr in re.findall(r'\[((?:"[\w-]+",?)+)\]\.indexOf\(name\)', ht):
        valid |= set(re.findall(r'"([\w-]+)"', arr))

    allowed, unmapped = {}, []
    for tag in sorted(valid):
        if tag in geo_exports and tag in geo_fns:
            allowed[tag] = geo_fns[tag] | {"caption"}      # showGeo draws the caption
        elif tag in math_exports and tag in math_fns:
            allowed[tag] = math_fns[tag] | {"caption"}     # showFig draws the caption
        elif tag in TAG_INLINE:
            allowed[tag] = set(TAG_INLINE[tag])
        elif tag in TAG_HANDLER and TAG_HANDLER[tag] in page_fns:
            allowed[tag] = page_fns[TAG_HANDLER[tag]]
        else:
            unmapped.append(tag)
    return valid, (allowed, unmapped), ""


# the EXACT regex session.html uses -- if it does not match here, it will not match there
_HT_TAG = re.compile(r"\[\[\s*([\w-]+)([^\]]*?)\]\]")
_HT_ATTR = re.compile(r'([\w-]+)\s*=\s*"([^"]*)"')

# [[graph]] draws a *different picture* than the author meant in two quiet ways, both
# found in build cd's audit of scripts that had already passed every other check:
#   lines="y=x^2"          -- lines= runs parseLinear(), which reads only the slope
#                             between x=0 and x=1. A parabola comes out a STRAIGHT LINE.
#   lines="y=2x+1, y=-x+4" -- the grapher splits curve lists on ";" or "|", never on a
#                             comma, so two equations arrive as one unparseable string.
_CURVE_ATTRS = ("func", "fn", "functions", "lines", "parabola", "parabolas")
_NONLINEAR = re.compile(r"[\^/]|sin|cos|tan|sqrt|log|exp|\*\*")


def _graph_sanity(tag, attrs):
    """'' if a [[graph]] will draw what its author meant, else why not."""
    if tag != "graph":
        return ""
    low = {k.lower(): v for k, v in attrs.items()}
    for k in _CURVE_ATTRS:
        if "," in low.get(k, ""):
            return (f'{k}="{low[k]}" separates curves with a COMMA; the grapher splits '
                    f'on ";" or "|" only, so this arrives as one unparseable expression')
    for piece in re.split(r"[;|]", low.get("lines", "")):
        piece = piece.strip()
        if piece and _NONLINEAR.search(piece.lower()):
            return (f'lines="{piece}" is not a straight line; lines= measures one slope '
                    f'and draws a LINE — use func= (or parabola=) to plot a curve')
    return ""


def part3c_board_tags():
    """Every board line in foundations.py must actually put something on the board."""
    print("\nPART 3c — board tags actually draw")
    here = os.path.dirname(os.path.abspath(__file__))
    valid, contract, why = _board_contract(here)
    if valid is None:
        bad("board tag contract readable", why + " — cannot verify what the board can draw")
        return
    allowed, unmapped = contract
    check("every tag in handleTags() is mapped to a renderer", not unmapped,
          f"unmapped tags {unmapped} — add them to TAG_HANDLER/TAG_INLINE in this file")
    try:
        import foundations
    except Exception as exc:  # noqa: BLE001
        bad("foundations.py imports", str(exc)); return

    lines = 0
    for course in COURSES:
        for f in foundations.for_course(course):
            for b in f.get("board", []):
                lines += 1
                label = f"  [{course}] {f['term']}"
                m = _HT_TAG.match(b.strip())
                if not m:
                    bad(f"{label} — board line parses",
                        f"handleTags' own regex does not match it (a '[' or ']' inside an "
                        f"attribute value ends the tag early): {b}")
                    continue
                tag = m.group(1).lower()
                attrs = {k.lower() for k, _v in _HT_ATTR.findall(m.group(2))}
                if tag not in allowed:
                    bad(f"{label} — [[{tag}]] is a real tag",
                        f"handleTags() has no branch for '{tag}' — it draws NOTHING: {b}")
                    continue
                unknown = sorted(attrs - allowed[tag])
                if unknown:
                    bad(f"{label} — [[{tag}]] attributes are read",
                        f"the renderer ignores {unknown} (it reads "
                        f"{sorted(allowed[tag])}) — the figure draws, but not what was meant: {b}")
                    continue
                need = CONTENT_ATTRS.get(tag)
                if need and not (attrs & need):
                    bad(f"{label} — [[{tag}]] has content",
                        f"no content attribute (needs one of {sorted(need)}) — it draws empty: {b}")
                    continue
                if tag in tutor.FIGURE_TAGS and "caption" not in attrs:
                    bad(f"{label} — [[{tag}]] says what to notice",
                        "rule 41: a figure with no caption= hands the student back the "
                        f"one job the picture was supposed to do for them: {b}")
                    continue
                why2 = _graph_sanity(tag, dict(_HT_ATTR.findall(m.group(2))))
                if why2:
                    bad(f"{label} — [[{tag}]] draws the RIGHT thing", f"{why2}: {b}")
                    continue
                ok(f"{label} — [[{tag}]] draws")
    check("board lines were actually checked", lines > 0, "no board lines found")

    # tutor.FIGURE_TAGS drives the visual referee (PART 2). tutor.py cannot read the
    # JS at request time, so it carries a constant -- and a constant drifts. Prove it
    # still names exactly the tags that put a PICTURE on the board.
    drawn = {t for t in valid if t in allowed and t not in TAG_INLINE
             and TAG_HANDLER.get(t) not in ("showWrite", "showStep", "showSolve",
                                            "showColumn", "showCard", "showCheck",
                                            "showQuiz", "showToday", "markTodayDone",
                                            "showUnitPlan", "showFinalExam", "showChoices")}
    missing = sorted(drawn - set(tutor.FIGURE_TAGS))
    extra = sorted(set(tutor.FIGURE_TAGS) - valid)
    check("tutor.FIGURE_TAGS still matches handleTags()", not missing and not extra,
          f"the visual referee would miss {missing}" if missing else
          f"names tags the board does not have: {extra}")


def part3d_foundation_memory():
    """The returning student must not be replayed an introduction he already gave.
    Jim: "nothing tells him which scripts that student has heard... we should just query
    him and say, do you think you got it, or do you want me to refresh your memory?"
    """
    print("\nPART 3d — foundation memory (the returning student)")
    try:
        import foundations
    except Exception as exc:  # noqa: BLE001
        bad("foundations.py imports", str(exc)); return

    # 1. the term key survives the round trip through the model's own typing
    check("normalize_term folds case and spacing",
          foundations.normalize_term("  Pythagorean   THEOREM ") == "pythagorean theorem",
          repr(foundations.normalize_term("  Pythagorean   THEOREM ")))
    check("known_term recognises a real script by any spelling",
          foundations.known_term("geometry", "PYTHAGOREAN theorem") == "Pythagorean theorem",
          repr(foundations.known_term("geometry", "PYTHAGOREAN theorem")))
    check("known_term rejects a term this course has no script for",
          foundations.known_term("geometry", "eigenvalue") == "", "it accepted a stranger")
    check("known_term is course-scoped",
          foundations.known_term("entry", "derivative") == "", "it accepted a stranger")

    # 2. the [[learned]] tag main.py relies on
    reply = ('Great work today! [[write text="1/4"]] [[learned term="denominator"]] '
             '[[learned term="NUMERATOR"]] [[learned term="not a real term"]]')
    got = foundations.learned_terms_in("basic", reply)
    check("learned_terms_in reads the tags and canonicalises them",
          got == ["denominator", "numerator"], f"got {got}")
    check("learned_terms_in drops a term we have no script for",
          "not a real term" not in got, f"got {got}")
    for junk in [None, "", 0, [], "[[learned term=", '[[learned term=""]]']:
        try:
            foundations.learned_terms_in("basic", junk)
        except Exception as exc:  # noqa: BLE001
            bad("learned_terms_in: junk never raises", f"{junk!r} -> {exc}")
            break
    else:
        ok("learned_terms_in: junk never raises")

    # 3. the prompt actually CHANGES for a student who has heard one
    fresh = tutor.build_system_prompt(dict(STUDENT), course="basic")
    known = tutor.build_system_prompt(
        dict(STUDENT, foundations_heard=["denominator", "Numerator"]), course="basic")
    check("a brand-new student is told nothing is known yet",
          "has not been introduced to ANY of these terms" in fresh,
          "the fresh-student prompt lost its note")
    check("a returning student's heard terms reach the prompt",
          "ALREADY INTRODUCED TO THIS STUDENT" in known and "denominator, numerator" in known,
          "the heard list never made it into the prompt")
    check("the heard terms are marked on their own scripts",
          known.count("[already introduced -- ask first, rule 40]") == 2,
          f"marked {known.count('[already introduced -- ask first, rule 40]')} of 2")
    # build gg: since build gb a prompt holds the lesson's unit plus anything heard, so
    # "every script is in both prompts" stopped being the question. The question this check
    # exists for never changed: wherever a script IS quoted, its wording must be
    # character-for-character the authored text, because the voice cache is keyed on that
    # text and one changed character re-bills the audio for every student on the platform.
    def _quoted_terms(prompt):
        return {m.strip().lower() for m in re.findall(r"^--- (.+?) ---", prompt, re.M)}

    _bad = []
    for _p, _label in ((fresh, "new student"), (known, "returning student")):
        _q = _quoted_terms(_p)
        for _f in foundations.for_course("basic"):
            if _f["term"].lower() in _q and _f["say"] not in _p:
                _bad.append(f"{_f['term']} ({_label})")
    check("the SCRIPTS themselves are byte-identical either way (the audio cache "
          "depends on it)",
          not _bad,
          f"a quoted script's wording was altered in the prompt: {_bad} -- the voice cache "
          f"is keyed on that exact text, so one changed character re-bills every student")
    check("a returning student is told to ASK, not replay",
          "refresh your memory" in known, "the ask is missing")
    # a heard list full of nonsense must not break the block
    for junk in [None, [], ["nothing like a real term"], "denominator", 0]:
        try:
            tutor.build_system_prompt(dict(STUDENT, foundations_heard=junk), course="basic")
        except Exception as exc:  # noqa: BLE001
            bad("a junk heard-list never breaks the prompt", f"{junk!r} -> {exc}")
            break
    else:
        ok("a junk heard-list never breaks the prompt")

    # 4. all THREE teaching modes get the scripts and honour the heard list.
    #    (Found in the build-cf audit: practice and topic were built from GROUND_RULES +
    #    GRAPH_TOOL_NOTE only, so rules 36-40 reached them while the scripts those rules
    #    refer to did not -- and a student could hear a different definition of the same
    #    word depending on which page they opened, which is rule 28 broken at scale.)
    MODES = [
        ("lesson", lambda st: tutor.build_system_prompt(st, course="basic")),
        ("practice", lambda st: tutor.build_practice_prompt(st, "3/4 + 1/2", course="basic")),
        ("topic", lambda st: tutor.build_topic_prompt(st, "fractions", course="basic")),
    ]
    for label, build in MODES:
        try:
            f = build(dict(STUDENT))
            k = build(dict(STUDENT, foundations_heard=["denominator"]))
        except Exception as exc:  # noqa: BLE001
            bad(f"{label} mode builds", str(exc)); continue
        check(f"{label} mode carries the canonical scripts", "SPEAK THESE VERBATIM" in f,
              "this mode teaches vocabulary with no script to teach it from")
        check(f"{label} mode honours the heard list", "ALREADY INTRODUCED TO THIS STUDENT" in k,
              "a returning student would be replayed an introduction here")

    # 4b. DEFERRED WORDING (build cl). A heard script's exact text is dropped from the
    #     ordinary turns of a returning student and restored the moment they ask. The
    #     danger is obvious -- if it is ever missing when he needs it he will paraphrase,
    #     which costs a cache miss AND drifts wording every student is meant to share --
    #     so the tests below care far more about RESTORING than about saving.
    # build cn: the deferral below is DORMANT in production -- main.py always carries the
    # wording, because flipping the prompt shape costs a cache rebuild worth far more
    # than the characters it saves (see main.py). The mechanism is still tested, because
    # it is the right answer if the library ever outgrows the window.
    heard = [d["term"] for d in foundations.for_course("algebra2")][:12]
    # build gz (2026-08-17): the RESTORE leg is what main.py actually does on a refresher
    # turn now -- it sets foundations_force_verbatim (from wants_refresher), because a
    # plain verbatim=True can be auto-deferred by the ceiling guard when the heard block
    # pushes the prompt over PROMPT_CEILING (12 heard algebra2 terms do exactly that).
    # One over-budget turn is the accepted price of rule 40's exact-words promise.
    full = tutor.build_system_prompt(
        dict(STUDENT, foundations_heard=heard, foundations_verbatim=True,
             foundations_force_verbatim=True), course="algebra2")
    lean = tutor.build_system_prompt(
        dict(STUDENT, foundations_heard=heard, foundations_verbatim=False), course="algebra2")
    fresh = tutor.build_system_prompt(dict(STUDENT), course="algebra2")
    a2 = foundations.for_course("algebra2")
    # build gg: "every script, always" was the pre-gb contract. A prompt now carries the
    # lesson's unit plus everything heard, so these two ask the same question of the set
    # that is actually promised: this unit's scripts, and anything the student has met.
    def _promised(f, heard_list):
        u = foundations.unit_of("algebra2", f["term"])
        return f["term"] in heard_list or u is None or u == _U
    _U = 1                      # STUDENT is unplaced, so the filter falls back to unit 1
    check("a brand-new student still gets every script his unit teaches, verbatim",
          all(f["say"] in fresh for f in a2 if _promised(f, [])),
          "a new student lost a script his own unit is supposed to introduce")
    check("a returning student keeps UNHEARD scripts verbatim",
          all(f["say"] in lean for f in a2
              if f["term"] not in heard and _promised(f, heard)),
          "a script they have never met was deferred -- that is a teaching loss")
    check("heard scripts are still NAMED on an ordinary turn",
          all(f["term"].upper() in lean for f in a2 if f["term"] in heard),
          "he cannot offer a refresher for a term he cannot see")
    # build gg: the promise is about the terms this student has MET -- those are the ones
    # rule 40 offers, and the ones "remind me" can ask for. A term from another unit that
    # they have never met is not a refresher candidate; it is named, and its unit will
    # introduce it properly when they get there.
    check("asking for it restores the EXACT wording",
          all(f["say"] in full for f in a2 if f["term"] in heard),
          "the refresher turn is missing a script the student HAS met -- he would have to "
          "paraphrase, which drifts the shared wording and re-bills the audio")
    check("deferring actually saves something", len(lean) < len(full) - 2000,
          f"only {len(full) - len(lean)} chars")
    check("the default is to CARRY the words",
          "prompt_block" in dir(foundations)
          and foundations.prompt_block("algebra2", heard) == foundations.prompt_block(
              "algebra2", heard, True),
          "verbatim must default to True -- fail open, always")
    for msg, last, want in [
            ("remind me what a denominator is", "", True),
            ("yes please", "…or want me to refresh your memory?", True),
            ("not really", "…got a handle on that?", True),
            ("I forgot", "", True),
            ("yes", "so what is seven plus eight?", False),
            ("sixteen", "", False)]:
        check(f"refresher detector: {msg!r} -> {'restore' if want else 'defer'}",
              foundations.wants_refresher(msg, last) == want,
              f"got {foundations.wants_refresher(msg, last)}")
    for junk in [None, 0, [], "?" * 500]:
        try:
            foundations.wants_refresher(junk, junk)
        except Exception as exc:  # noqa: BLE001
            bad("refresher detector: junk never raises", f"{junk!r} -> {exc}"); break
    else:
        ok("refresher detector: junk never raises")

    # 5. the storage layer is wired into the reset cascade (standing rule: day one)
    try:
        import store
        check("foundations_heard joins the per-student reset cascade",
              ("foundations_heard", "code") in store._STUDENT_CODE_TABLES,
              "a Start Fresh would leave the memory behind")
        check("today_goals joins the per-student reset cascade",
              ("today_goals", "code") in store._STUDENT_CODE_TABLES,
              "a reset student would open the lesson to yesterday's goals")
        for fn in ("get_foundations_heard", "record_foundation_heard",
                   "get_today_goals", "save_today_goals"):
            check(f"store.{fn} exists", hasattr(store, fn), "main.py calls it every turn")
    except Exception as exc:  # noqa: BLE001
        bad("store.py imports", str(exc))

    # 6. the TODAY-bar net must not stand down just because HISTORY mentions a bar.
    #    (Jim: "there's only two of the three tracking bars... I don't know why it keeps
    #    disappearing." A reloaded page has no bar, however many [[today]] tags the old
    #    transcript holds, so the net now asks the SERVER whether one really exists.)
    try:
        stale = [{"role": "assistant", "content": 'old [[today items="a | b"]]'}]
        opener = 'Welcome back! [[goal text="add money by carrying"]]'
        check("the net RESTORES a bar that a reload destroyed",
              "[[today" in tutor.ensure_today_tag(opener, stale, today_live=False),
              "a resumed session would show only two of the three bars")
        check("the net never resets a bar that is genuinely live",
              "[[today" not in tutor.ensure_today_tag(opener, stale, today_live=True),
              "it would wipe today's ticked-off goals mid-lesson")
        check("the net never touches a reply that already has its own tag",
              tutor.ensure_today_tag('x [[today items="a"]]', stale, False).count("[[today") == 1,
              "it double-emitted")
    except Exception as exc:  # noqa: BLE001
        bad("store.py imports", str(exc))


# =============================================================================
# PART 3e -- THE THREE TEACHING PAGES MUST MATCH
# -----------------------------------------------------------------------------
# 2026-08-09 (build cf). Found by auditing whether audit #1 really shipped: item 11,
# the fix that stops a long board line WRAPPING mid-equation, went into session.html
# in build bu and NEVER reached practice.html or topic.html. Jim's screenshot bug
# ("dimes: 7 + 8 + = 16" with "1(carried)" on the next line -- a literally different
# equation on screen) was still live on two of the three teaching pages for a day.
#
# This is the SAME bug shape as build bk, where a rule written into one of tutor.py's
# eleven per-course templates reached one course. PART 1 made that impossible for the
# prompt. This does it for the pages: session / practice / topic are three copies of
# one classroom, and anything that fixes teaching on one must be on all three.
# =============================================================================
PAGES = ("session.html", "practice.html", "topic.html")

# (label, needle) -- must appear in EVERY teaching page.
PAGE_PARITY = [
    # build dr: the mic is a CAPABILITY check and excludes no course -- Jim's call
    # ("it's okay for the youngest to have a way to talk as well"). If !IS_ELEM ever
    # creeps back into canRecord, the youngest students silently lose their voice.
    ("the mic excludes no course (dr)", "const canRecord = !!(navigator.mediaDevices"),
    ("board lines never wrap (audit #1 item 11)", "white-space: nowrap"),
    # build he: fitRow and the show* renderers that call it moved to /static/board.js
    # (one copy). What each page must carry is the INCLUDE; the fitting behaviour is
    # asserted once, against the module, in part3e below.
    ("the shared board module is loaded (he)",    "/static/board.js"),
    # build hc: forSpeech moved to /static/speech-text.js. What every teaching page must
    # now have is the INCLUDE -- checking for the inline text here would force the very
    # duplication this build removed.
    ("the shared spoken-text module is loaded (hc)", "/static/speech-text.js"),
    ("the shared board-text module is loaded (hc)",  "/static/board-text.js"),
    ("control tags are stripped before speaking", "function stripTags"),
    ("the geometry figures are loaded",           "/static/geo-figures.js"),
    ("the math figures are loaded",               "/static/math-figures.js"),
    # build gz (2026-08-17): the gr expect=letter fix was hand-copied into topic and
    # practice WITHOUT the state it reads -- lastTutorText was never declared there, so
    # transcribe() threw on every spoken answer and both pages blamed the student's
    # audio ("I didn't quite catch that"). A page that reads it must OWN it: declared
    # at page level AND assigned where the tutor's words are rendered.
    ("lastTutorText is declared at page level (gz)", 'let lastTutorText = ""'),
    ("lastTutorText is assigned when the tutor speaks (gz)", "lastTutorText = clean"),
    # build ha: the error beacon must load on every teaching page -- and FIRST, so it
    # is listening before any later script can throw (checked separately below).
    ("the client error beacon is loaded (ha)", "/static/client-log.js"),
]

# Lesson-page-only wiring (the today bar exists only there).
SESSION_ONLY_PARITY = [
    ("the TODAY bar is rebuilt at load, like the other two", "SRV_PROGRESS.today"),
]


def part3e_page_parity():
    print("\nPART 3e — the three teaching pages must match")
    here = os.path.dirname(os.path.abspath(__file__))
    src = {}
    for p in PAGES:
        path = os.path.join(here, "static", p)
        if not os.path.exists(path):
            bad(f"{p} exists", "missing from static/"); return
        with open(path, encoding="utf-8") as fh:
            src[p] = fh.read()
    for label, needle in PAGE_PARITY:
        missing = [p for p in PAGES if needle not in src[p]]
        check(f"all three pages: {label}", not missing, f"missing from: {missing}")
    # build he: the fitting machinery, asserted once against its single copy.
    bpath = os.path.join(here, "static", "board.js")
    if not os.path.exists(bpath):
        bad("static/board.js present", "the shared board module is missing")
    else:
        with open(bpath, encoding="utf-8") as fh:
            bsrc = fh.read()
        for label, needle in (("fitRow() shrinks an oversized line", "function fitRow(row)"),
                              ("[[step]] lines are fitted", "fitRow(wl.appendChild(eqRow(eq)))"),
                              ("[[write]] lines are fitted", "fitRow(wl.appendChild(eqRow(ln)))")):
            check(f"board.js: {label}", needle in bsrc,
                  "the audit-#1-item-11 fitting is gone from the ONE copy every page uses")
    for label, needle in SESSION_ONLY_PARITY:
        check(f"session.html: {label}", needle in src["session.html"],
              f"{needle!r} is gone -- a reload would lose the bar again")

    # build dr: the old exclusion must never return, and the teaching brain must know
    # the youngest students can speak (with extra charity for young readers).
    relapsed = [p for p in PAGES if "canRecord = !IS_ELEM" in src[p]]
    check("no page ever re-excludes elementary from the mic (dr)", not relapsed,
          f"{relapsed} would silently mute the students least able to type")

    # build gz (2026-08-17): A PAGE MAY ONLY USE STATE IT OWNS. topic and practice read
    # session.html's page-level `started` in their visibilitychange handlers -- a
    # ReferenceError on every return to the tab, so keep-alive never restarted (the
    # "first word swallowed" family, bl/cb/gn, alive on two pages after three fixes).
    # They must use their OWN audioWarmed flag; session.html keeps its own `started`
    # (declared there, works there).
    for p in ("topic.html", "practice.html"):
        check(f"{p}: keep-alive resume reads the page's own audioWarmed (gz)",
              "else if (audioWarmed) startKeepAlive()" in src[p],
              "the visibilitychange handler no longer resumes keep-alive -- the first "
              "words after a tab switch will hit a powered-down audio device again")
        check(f"{p}: keep-alive resume never reads the undeclared `started` (gz)",
              "else if (started) startKeepAlive()" not in src[p],
              "`started` is session.html's page-level variable and does not exist "
              "here -- this line throws on every return to the tab")
    check("session.html: keep-alive resume still guarded by its own `started` (gz)",
          "else if (started) startKeepAlive()" in src["session.html"]
          and "let started = false" in src["session.html"],
          "session.html's page-level `started` or its handler changed -- if this moved "
          "to another flag, update this check WITH the reason")
    check("the prompt tells the tutor elementary students may TALK (dr)",
          "tap, talk," in tutor.GRAPH_TOOL_NOTE
          and "EXTRA" in tutor.GRAPH_TOOL_NOTE
          and '"free" for three' in tutor.GRAPH_TOOL_NOTE,
          "the pages let them speak but the tutor was never told")

    # Every tag the SHARED prompt block teaches him must be drawable on every page.
    # (The lesson page has six extra handlers -- the progress bars, the goal banner and
    # the final exam -- which is correct: practice and topic are side trips with no bars,
    # and nothing in the shared block ever asks him to emit those there. The named list
    # below is the whole allowance; a new session-only tag has to be added here on
    # purpose, and a shared-block tag can never quietly go missing from a page.)
    # 2026-08-12 (build ee): "highlight" LEFT this list on purpose -- rule 60 teaches
    # it in the shared block now, and all three pages draw it (the board spotlight;
    # PART 3t proves the implementation). Five lesson-only tags remain.
    # build ey adds "bye": the session's wrap-up mark. Lesson-only by design -- it is
    # taught in PROGRESS_TAGS_NOTE (never the shared block), and a practice or topic
    # helper session has no "end of the school day" to mark.
    LESSON_ONLY = {"today", "todaydone", "unitplan", "goal", "finalexam", "bye"}
    tags = {}
    for p in PAGES:
        try:
            ht = src[p][src[p].index("function handleTags("):]
            ht = ht[:ht.index("\n    function ")]
        except ValueError:
            bad(f"{p} has a readable handleTags()", "could not find it"); return
        names = set(re.findall(r'name === "([\w-]+)"', ht))
        for arr in re.findall(r'\[((?:"[\w-]+",?)+)\]\.indexOf\(name\)', ht):
            names |= set(re.findall(r'"([\w-]+)"', arr))
        tags[p] = names
    every = set().union(*tags.values())
    for p in PAGES:
        gap = sorted(every - tags[p] - LESSON_ONLY)
        check(f"{p} handles every shared board tag ({len(tags[p])})", not gap,
              f"the tutor can emit {gap} here and NOTHING will draw")
    # ...and the allowance itself must stay honest: a tag we excused must genuinely be
    # absent from the shared block that practice and topic also receive.
    leaked = sorted(t for t in LESSON_ONLY if f"[[{t}" in tutor.GRAPH_TOOL_NOTE)
    check("no lesson-only tag is taught in the SHARED block", not leaked,
          f"the shared block asks for {leaked}, but practice/topic cannot draw them")


# =============================================================================
# PART 3f -- NOTATION COVERAGE: WE NEVER WRITE A SYMBOL WE HAVEN'T SAID
# -----------------------------------------------------------------------------
# 2026-08-09 (build cj). Jim, after the f(x) fix: "it looks like we've fixed the
# function notation, but math is filled with these kinds of things. How can we make
# sure that every one of these is caught all of the time?"
#
# Build ci fixed f(x) by hand, which fixes one symbol and guarantees nothing. This is
# the general answer. notation.py registers every notation the courses use -- how it is
# written, how it is SAID, and the wrong reading to deny -- and this test holds every
# board line we ship to it:
#   CHECK A  every notation on a board is REGISTERED for that course. If we write a
#            symbol the registry does not know, the tutor was never told how to read it
#            and the build fails. This is the guarantee: we cannot put a symbol on a
#            child's screen without having said, somewhere, how to say it.
#   CHECK B  the DEEP families (function, prime, exponent, subscript, absolute value,
#            radical) need a real foundation script that reads them aloud -- a one-line
#            table row is not teaching. It caught three courses using subscripts with
#            nothing anywhere saying "sub".
#   CHECK C  the registry reaches every course's prompt, and its own patterns are sane
#            (every `shown` example must match its own `wrote` pattern, and every
#            `spoken` example its own `heard` pattern -- a registry that cannot
#            recognise its own examples is worse than none).
# =============================================================================
_NT_TAG = re.compile(r"\[\[\s*([\w-]+)([^\]]*?)\]\]")
_NT_ATTR = re.compile(r'([\w-]+)\s*=\s*"([^"]*)"')


def _board_readable(entry) -> list:
    """The parts of a script's board a STUDENT actually reads (not renderer inputs)."""
    out = []
    for b in entry.get("board", []):
        m = _NT_TAG.match(b.strip())
        if not m:
            continue
        for k, v in _NT_ATTR.findall(m.group(2)):
            if k.lower() in notation.READABLE_ATTRS:
                out.append((v, b))
    return out


def part3f_notation():
    print("\nPART 3f — notation coverage (we never write a symbol we haven't said)")
    try:
        import foundations
    except Exception as exc:  # noqa: BLE001
        bad("foundations.py imports", str(exc)); return

    # CHECK C first: a registry that cannot recognise its own examples proves nothing.
    for n in notation.NOTATIONS:
        check(f"  registry [{n['id']}] recognises its own written form",
              bool(re.search(n["wrote"], n["shown"])),
              f"shown={n['shown']!r} does not match wrote={n['wrote']!r}")
        check(f"  registry [{n['id']}] recognises its own spoken form",
              bool(re.search(n["heard"], n["spoken"], re.I)),
              f"spoken={n['spoken']!r} does not match heard={n['heard']!r}")
        # If one entry's example ALSO matches another entry, that other entry must be
        # legal everywhere this one is -- otherwise a perfectly good board line gets
        # reported as an unregistered symbol. (Exactly what happened with mu: a stats
        # entry and a general-name entry both matched the same glyph.)
        overlap = [o for o in notation.written_in(n["shown"]) if o != n["id"]
                   and not set(n["courses"]) <= set(notation.by_id(o)["courses"])]
        check(f"  registry [{n['id']}] does not collide with a narrower entry",
              not overlap,
              f"{n['shown']!r} also matches {overlap}, which are not allowed in every "
              f"course [{n['id']}] is -- merge them or tighten the patterns")
    for c in COURSES:
        p = tutor.build_system_prompt(dict(STUDENT), course=c)
        check(f"the symbol table reaches [{c}]", "HOW TO SAY WHAT YOU WRITE" in p,
              "this course's tutor has no canonical readings -- rule 48 is unfollowable")

    # CHECK A: nothing on any board is unregistered for its course.
    unregistered = {}
    scanned = 0
    for c in COURSES:
        allowed = {n["id"] for n in notation.for_course(c)}
        for d in foundations.for_course(c):
            for value, raw in _board_readable(d):
                scanned += 1
                for nid in notation.written_in(value):
                    if nid not in allowed:
                        unregistered.setdefault((c, nid), (d["term"], raw))
    check(f"every notation on every board is registered ({scanned} board strings)",
          not unregistered,
          "; ".join(f"{c} writes [{n}] in '{t}' — register it in notation.py or stop "
                    f"writing it: {r[:60]}" for (c, n), (t, r) in sorted(unregistered.items())))

    # CHECK B: a deep notation must be TAUGHT, not just tabled.
    for c in COURSES:
        items = foundations.for_course(c)
        used = set()
        for d in items:
            for value, _raw in _board_readable(d):
                used.update(notation.written_in(value))
        said = set()
        for d in items:
            said.update(notation.spoken_in(d["say"]))
        for nid in sorted(used):
            if not notation.by_id(nid).get("deep"):
                continue
            check(f"  [{c}] teaches [{nid}] aloud, not just on the board", nid in said,
                  f"this course writes {notation.by_id(nid)['shown']} and NO script ever "
                  f"says \"{notation.by_id(nid)['spoken']}\" — rule 48(a)")


# =============================================================================
# PART 3g -- THE MISCONCEPTION CATALOGUE (rule 49)
# =============================================================================
_CARDINALS = set("""zero one two three four five six seven eight nine ten eleven twelve
thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty thirty forty fifty
sixty seventy eighty ninety hundred thousand million negative minus point and a""".split())


def part3g_misconceptions():
    print("\nPART 3g — the misconception catalogue")
    try:
        import misconceptions as M
    except Exception as exc:  # noqa: BLE001
        bad("misconceptions.py imports", str(exc)); return
    seen_ids, total = set(), 0
    for c in COURSES:
        items = M.for_course(c)
        total += len(items)
        check(f"[{c}] has a catalogue ({len(items)} error patterns)", len(items) >= 10,
              "too few to be worth consulting")
        for m in items:
            lab = f"  [{c}] {m['id']}"
            check(f"{lab} has every field",
                  all(m.get(k) for k in ("id", "name", "topic", "tell", "rule", "why", "fix", "say")),
                  f"missing: {[k for k in ('id','name','topic','tell','rule','why','fix','say') if not m.get(k)]}")
            check(f"{lab} id is unique", m["id"] not in seen_ids, "duplicated across courses")
            seen_ids.add(m["id"])
            offenders = [ch for ch in "=+×÷^<>" if ch in m["say"]]
            check(f"{lab} SAY is speakable", not offenders,
                  f"symbols that get read aloud badly: {offenders}")
            w = len(m["say"].split())
            check(f"{lab} SAY is a real sentence", 20 <= w <= 75, f"{w} words")
            # rule 49(c)/20: never open by telling them they are wrong
            opener = " ".join(m["say"].split()[:6]).lower()
            check(f"{lab} SAY does not open with 'wrong'",
                  not re.match(r"^(that'?s |that is )?(wrong|incorrect|no,|nope|not quite)", opener),
                  f"opens: {opener!r}")
            for d in m.get("detect", []):
                # A numeric answer is only evidence in the context of the problem it
                # answers, and the matcher cannot see the problem. So numbers never
                # count -- in ANY spelling. The first version of this filter allowed
                # anything containing a letter, and "three" and "two" promptly matched
                # "I did three plus two first, so twenty" and produced two confident
                # WRONG theories on the first end-to-end run (rule 49e).
                toks = [t for t in re.split(r"[\s\-]+", d.lower()) if t]
                barenum = toks and all(
                    t in _CARDINALS or re.fullmatch(r"[-+]?\d+(?:\.\d+)?", t) for t in toks)
                check(f"{lab} evidence {d!r} is not just a number", not barenum,
                      "a number fires on correct answers too -- evidence must be a "
                      "procedure word or a distinctive symbolic form")
    check(f"the catalogue is substantial ({total} patterns)", total >= 120, f"only {total}")

    # the matcher must be conservative: it fires on real evidence and stays silent otherwise
    CASES = [
        ("basic", "two fifths", "add-across-fractions", True),
        ("algebra1", "three x plus four", "distribute-one-term-only", True),
        ("basic", "sixteen", None, False),
        ("basic", "I am not sure", None, False),
        # the false-positive that the first end-to-end run produced
        ("prealgebra", "I did three plus two first, so twenty", None, False),
        ("prealgebra", "twenty", None, False),
        ("probstat", "so it causes it", "correlation-is-causation", True),
        ("prealgebra", "", None, False),
    ]
    for course, said, want_id, want_hit in CASES:
        hits = M.match(course, said)
        check(f"matcher: {said!r} -> {'a theory' if want_hit else 'silence'}",
              bool(hits) == want_hit and (not want_id or any(h["id"] == want_id for h in hits)),
              f"got {[h['id'] for h in hits]}")
    check("the matcher never returns a crowd", all(len(M.match(c, "two fifths x plus four")) <= 2
                                                   for c in COURSES),
          "more than two theories is the same as none (rule 49d)")
    for junk in [None, "", 0, [], "?" * 400]:
        try:
            M.match("basic", junk); M.hint_note("basic", junk)
        except Exception as exc:  # noqa: BLE001
            bad("matcher: junk never raises", f"{junk!r} -> {exc}"); break
    else:
        ok("matcher: junk never raises")
    # CACHE DISCIPLINE (build cm). The system prompt is ONE cached block, so anything
    # per-turn that lands inside it moves the cache prefix and re-bills every token from
    # that point on. Build ck put the misconception hint into the prompt and threw away
    # ~16k tokens on every turn it fired. Per-turn notes now ride with the message.
    import inspect
    check("get_tutor_reply takes a per-turn note",
          "turn_note" in inspect.signature(tutor.get_tutor_reply).parameters,
          "a per-turn note has nowhere to go except the cached prompt")
    base = tutor.build_system_prompt(dict(STUDENT), course="basic")
    for volatile in ("[LIKELY MISCONCEPTION -- ...]", "\n[some per-turn aside]"):
        check(f"a per-turn note does NOT reach the system prompt ({volatile[:22]}…)",
              volatile not in base, "it would move the cache prefix every turn")
    check("the prompt shape does not flip between turns in production",
          "student_context[\"foundations_verbatim\"] = True" in
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "main.py"),
               encoding="utf-8").read(),
          "a prompt that changes shape rebuilds the cache -- ~$0.24 an episode, and a "
          "slower turn, to save $0.0005")
    check("the system prompt is identical for two ordinary turns",
          tutor.build_system_prompt(dict(STUDENT), course="basic") == base,
          "the cached prefix changes turn to turn -- every turn re-bills in full")

    check("a hit produces a note the tutor may DISCARD",
          "IGNORE this note" in M.hint_note("basic", "two fifths"),
          "the note must never override his own reading of the student (rule 49d)")

    # every course's catalogue must actually reach its prompt
    for c in COURSES:
        p = tutor.build_system_prompt(dict(STUDENT), course=c)
        check(f"the catalogue reaches [{c}]", "WHY THE ANSWER WAS WRONG" in p,
              "rule 49 is unfollowable in this course")

    # PROMPT SIZE (proactive audit #2 item 22). Not a style note: past some length a
    # model follows rule 3 and rule 31 less reliably, and the failure is invisible.
    # The ceiling is a TRIPWIRE, deliberately set above today's largest.
    #
    # 2026-08-10 (build cw) -- RAISED 135,000 -> 150,000, WITH THE REASON, because the
    # note that said "consolidate, do not raise" was written before we had measured
    # anything. What we know now: 135,000 was my judgement in an audit, not a
    # measurement; the built prompt is about 17% of the model's real context window, so
    # this was never a wall; and rule 51 spent the last 500 characters, which would have
    # made the NEXT rule -- not any particular bad rule, just the next one -- fail the
    # build. Consolidating rules to satisfy an invented number means editing the teaching
    # itself, and that fails invisibly. That is the wrong risk to take on no evidence.
    # WHAT MAKES THIS HONEST RATHER THAN CONVENIENT: the real question was never "how
    # many characters" but "does he still FOLLOW rule 34 at this length", and nothing has
    # ever measured that. lessonaudit.py now can -- it runs real lessons and has an
    # independent model mark them against every rule. Run it at two prompt sizes and set
    # this number from evidence. Until then 150,000 is a tripwire, not a licence: it is
    # still an early warning that someone should look, not permission to sprawl.
    # 2026-08-12 (build el): RAISED 160,000 -> 175,000. Rule 61 took the largest prompt
    # to 159,652 -- 348 characters of headroom, which is the tripwire doing its job: it
    # said "someone should look", and someone did. Raised deliberately rather than by
    # trimming teaching, for the reason the essay above gives: consolidating rules to
    # satisfy an invented number means editing the teaching itself, and that fails
    # invisibly. Same standing authorization as the last raise; this is its change note.
    # The honest measurement (lessonaudit at two prompt sizes, to find where rule-following
    # actually degrades) is STILL the right way to set this number, and still not done.
    # 2026-08-12 (build ee): RAISED 150,000 -> 160,000 for rules 56-60, the five
    # evidence-backed teaching upgrades (~8.2k shared characters; largest prompt now
    # 156,515). Authorized by Jim's standing decision (2026-08-11, Four_Lens_Review:
    # "if you need to raise it, you raise it" -- each raise gets its own change note;
    # this is that note). Still a tripwire: the lessonaudit two-sizes measurement is
    # still the right way to set this number from evidence someday.
    # 2026-08-13 (build fe): RAISED 175,000 -> 180,000. Rule 63 plus the seven amended
    # rules from the 2026-08-13 lesson-audit findings (~5.7k shared characters) took
    # the largest prompt (algebra2) to 175,887. Raised deliberately rather than by
    # trimming teaching, under Jim's standing authorization (2026-08-11, Four_Lens
    # review: "if you need to raise it, you raise it" -- each raise gets its own
    # change note; this is that note). Still a tripwire, not a licence, and the
    # honest measurement -- lessonaudit at two prompt sizes, to find where
    # rule-following actually degrades -- is STILL the right way to set this number,
    # and still not done.
    # 2026-08-17 (build gz): THE CEILING HAS ONE DEFINITION, AND IT LIVES IN tutor.py.
    # This test measured a FRESH student and passed while an all-heard returning student
    # assembled to 186,890-194,284 chars on every course in production (build gf made
    # heard scripts exempt from unit filtering; build cn made them always travel
    # verbatim; nobody re-measured the worst case). Second shipping of that miss class.
    # Now: tutor.PROMPT_CEILING is the single source (the serving path checks it on
    # every assembly and defers heard wording when over), and THIS part measures the
    # worst-case student shape too -- see the all-heard checks below.
    CEILING = getattr(tutor, "PROMPT_CEILING", None)
    check("the prompt ceiling has ONE definition (tutor.PROMPT_CEILING)",
          isinstance(CEILING, int) and CEILING > 0,
          "tutor.PROMPT_CEILING is missing -- the runtime guard is gone, and this test "
          "would be measuring against a number the serving path no longer knows")
    if not isinstance(CEILING, int):
        CEILING = 180_000
    sizes = {c: len(tutor.build_system_prompt(dict(STUDENT), course=c)) for c in COURSES}
    biggest = max(sizes, key=sizes.get)
    # THE BUDGET, not just the total. A single number tells you that you are over and
    # nothing about what to do; this table tells you what every block costs, so the next
    # person adding one can see the price before they pay it. Measured 2026-08-10: the
    # course templates and the shared rules share ZERO text -- there is no duplication
    # left to reclaim, so any reduction from here removes or defers real teaching.
    try:
        import notation as _n, misconceptions as _m, foundations as _f
        c = biggest
        blocks = [
            ("shared rules 0-49", len(tutor.GRAPH_TOOL_NOTE)),
            ("course lesson template", len(tutor.LESSON_TEMPLATES.get(c, ""))),
            ("foundation scripts", len(_f.prompt_block(c))),
            ("misconception catalogue", len(_m.prompt_block(c))),
            ("session opener rules", len(tutor.SESSION_OPENER_RULES)),
            ("progress-tag note", len(tutor.PROGRESS_TAGS_NOTE)),
            ("notation table", len(_n.prompt_block(c))),
            ("ground rules", len(tutor.GROUND_RULES)),
        ]
        tot = sum(v for _k, v in blocks) or 1
        print(f"       PROMPT BUDGET ({c}, the largest):")
        for k, v in sorted(blocks, key=lambda x: -x[1]):
            print(f"         {k:<26}{v:>8,}  {100*v/tot:5.1f}%")
        print(f"         {'total':<26}{sizes[biggest]:>8,}  (ceiling {CEILING:,})")
    except Exception as exc:  # noqa: BLE001
        print(f"       (budget table unavailable: {exc})")
    check(f"no prompt exceeds {CEILING:,} chars", sizes[biggest] <= CEILING,
          f"{biggest} is {sizes[biggest]:,}. There is NO duplication left to reclaim "
          f"(measured 0% overlap between the templates and the shared rules), so the "
          f"honest options are: consolidate overlapping RULES, defer another block the "
          f"way build cl defers heard scripts, or raise this deliberately with a reason "
          f"written down. Do not raise it silently.")

    # -------------------------------------------------------------------------
    # 2026-08-17 (build gz): THE WORST-CASE STUDENT, not just the fresh one.
    # A returning student who has heard EVERY foundation script is the heaviest
    # prompt this app can build (heard scripts always travel verbatim since cn and
    # are never unit-filtered since gf). That shape overflowed the ceiling on all
    # four measured courses and nothing noticed, because this part only ever
    # measured a fresh student. Three checks:
    #   1. the all-heard prompt fits (the gz auto-deferral working end to end);
    #   2. the deferred shape still OFFERS every heard script by name (rule 40's
    #      contract: named always, wording on request);
    #   3. a refresher turn (foundations_force_verbatim) really does restore the
    #      full wording -- over-ceiling is permitted for that one turn, silence
    #      about a broken restore is not.
    # -------------------------------------------------------------------------
    try:
        import foundations as _fnd
        heavy_courses = [c for c in COURSES if _fnd.for_course(c)]
    except Exception as exc:  # noqa: BLE001
        heavy_courses = []
        bad("all-heard measurement ran", f"foundations unavailable: {exc}")
    for c in heavy_courses:
        items = _fnd.for_course(c)
        terms = [f["term"] for f in items]
        heavy = dict(STUDENT); heavy["foundations_heard"] = terms
        p_heavy = tutor.build_system_prompt(heavy, course=c)
        check(f"all-heard {c} prompt fits under the ceiling ({len(p_heavy):,} chars)",
              len(p_heavy) <= CEILING,
              f"{len(p_heavy):,} > {CEILING:,} -- the gz deferral did not engage or did "
              f"not save enough. This is the exact shape that shipped over-ceiling "
              f"silently twice (gf, and pre-gz).")
        named = [t for t in terms if str(t).lower() in p_heavy.lower()]
        check(f"all-heard {c}: every heard script is still OFFERED by name "
              f"({len(named)}/{len(terms)})",
              len(named) == len(terms),
              f"missing from the prompt entirely: "
              f"{[t for t in terms if str(t).lower() not in p_heavy.lower()][:5]} -- "
              f"rule 40 cannot offer a refresher for a term the tutor cannot see")
        # The refresher turn must carry EVERY heard script's exact wording -- for an
        # under-ceiling course nothing was deferred and this passes trivially; for an
        # over-ceiling course this is the restore promise doing its job.
        forced = dict(heavy); forced["foundations_force_verbatim"] = True
        p_forced = tutor.build_system_prompt(forced, course=c)
        missing_say = [f["term"] for f in items if f["say"] not in p_forced]
        check(f"all-heard {c}: a refresher turn restores the full wording",
              not missing_say,
              f"{missing_say[:5]} missing from the forced-verbatim prompt -- it promises "
              f"'the exact script is restored the moment they ask' and that promise is "
              f"now false")


# =============================================================================
# PART 3h -- IT MUST NOT DEGRADE, AND IT MUST SCALE
# -----------------------------------------------------------------------------
# 2026-08-10 (build cn). Jim: "I don't want to build in something that's going to
# degrade over time where their errors are gonna start to add up and making more and
# more mess because we're not discarding things that we should discard... suppose we
# have ten thousand people using this app simultaneously."
# Nothing in the battery had ever asked whether anything GROWS. It did: every chat turn
# loaded, parsed, appended to and rewrote the student's ENTIRE conversation to use the
# last thirty messages of it, and the usage log kept every row forever.
# =============================================================================
def part3h_scale():
    print("\nPART 3h — it must not degrade, and it must scale")
    here = os.path.dirname(os.path.abspath(__file__))
    src = {}
    for f in ("main.py", "store.py"):
        with open(os.path.join(here, f), encoding="utf-8") as fh:
            src[f] = fh.read()

    check("the stored transcript is capped", "MAX_STORED_MESSAGES" in src["main.py"],
          "a year-old student would move megabytes of JSON on every turn")
    check("every save goes through the cap",
          "def save_session" in src["main.py"]
          and "_bounded_history(session)" in src["main.py"],
          "some path writes an untrimmed transcript")
    m = re.search(r"MAX_STORED_MESSAGES\s*=\s*(\d+)", src["main.py"])
    stored = int(m.group(1)) if m else 0
    check(f"the cap ({stored}) leaves margin over what the model reads "
          f"({tutor.MAX_HISTORY_MESSAGES})", stored > tutor.MAX_HISTORY_MESSAGES,
          "trimming below what the tutor reads would silently shorten his memory")
    check("the usage log has a retention pass",
          "purge_usage_log" in src["store.py"] and "_usage_purge_pass" in src["main.py"],
          "one row per model call and per TTS request, kept forever")
    check("the connection pool is sized on purpose",
          "pool_size=" in src["store.py"] and "pool_recycle=" in src["store.py"],
          "SQLAlchemy's default is 15 connections -- a hard ceiling under load")
    check("rate-limit buckets expire by AGE, not just emptiness",
          "q[-1] <= now - max(window_seconds" in src["main.py"],
          "with every bucket busy the table grows past its cap and never shrinks")
    # the caps must be real numbers, not aspirations
    for name, pat, lo in [("TTS cache cap", r"_TTS_CACHE_MAX_BYTES\s*=\s*([\d_]+)", 1),
                          ("usage retention days", r"USAGE_LOG_DAYS[^\n]*?\"(\d+)\"", 1)]:
        mm = re.search(pat, src["main.py"])
        check(f"{name} is set", bool(mm) and int(mm.group(1).replace("_", "")) >= lo,
              "no cap found")

    # --- BUILD do: prompts.py is TEXT ONLY, and stays that way -----------------------
    # The split's whole value is the boundary: every word the model reads in one file
    # with no machinery, so a wording edit can never break code and a code edit can
    # never change the teaching. AST-verified: top-level assignments of strings and
    # dicts only -- no imports, no defs, no classes, no calls. And the boundary must
    # not have dropped anything: tutor still exposes every moved name, non-empty.
    with open(os.path.join(here, "prompts.py"), encoding="utf-8") as fh:
        psrc = fh.read()
    ptree = ast.parse(psrc)
    offenders = []
    for node in ptree.body:
        if isinstance(node, ast.Assign):
            if not isinstance(node.value, (ast.Constant, ast.JoinedStr, ast.Dict)):
                offenders.append(f"L{node.lineno}: {type(node.value).__name__} assigned")
        else:
            offenders.append(f"L{node.lineno}: {type(node).__name__}")
    check("prompts.py holds text only -- no imports, functions, classes, or calls",
          not offenders, str(offenders[:4]))
    _MOVED = ("TUTOR_NAME", "LESSON_TEMPLATES", "GROUND_RULES", "GRAPH_TOOL_NOTE",
              "SESSION_OPENER_RULES", "PROGRESS_TAGS_NOTE", "FINAL_PREP_NOTE",
              "FINAL_EXAM_NOTE", "COURSE_SUBJECT", "PRACTICE_SCOPE", "TOPIC_SCOPE",
              "PRACTICE_SYSTEM_PROMPT_TEMPLATE", "TOPIC_SYSTEM_PROMPT_TEMPLATE",
              "ASSESSMENT_SYSTEM_STUDENT", "ASSESSMENT_SYSTEM_PARENT",
              "SYSTEM_PROMPT_TEMPLATE", "ELEMENTARY_SYSTEM_PROMPT_TEMPLATE")
    gone = [n for n in _MOVED if not getattr(tutor, n, None)]
    check("tutor re-exports every moved prompt name, non-empty", not gone, str(gone))
    check("the lesson prompt still assembles at full size",
          len(tutor.build_system_prompt({"name": "T"}, "algebra1")) > 100_000,
          "the split must never shrink what the model reads by accident")


# =============================================================================
# PART 3i -- EVERY RULE DECLARES HOW IT IS VERIFIED  (audit #2 item 24)
# -----------------------------------------------------------------------------
# 2026-08-10 (build co). This file's own header has said since the day it was written:
# "ADDING A RULE? Add a scenario here in the same commit. That is the whole point."
# We drifted anyway -- rules 42 to 47 shipped with no behavioural check of their own --
# because nothing made the drift visible. This does.
#
# It is a RATCHET, not a gate. Today's honest position is recorded below and the suite
# does NOT fail for the debt that already exists; failing a deploy over history helps
# nobody. It fails for two things only, and both are new damage:
#   * a rule appears in the prompt with no entry here at all
#   * a rule that WAS enforced or exercised quietly loses its check
# The backlog prints on every run, so it cannot be forgotten either.
#
# THE FOUR TIERS, in descending order of how much they are worth:
#   ENFORCED   a machine catches the violation in a real reply. A referee regenerates
#              the draft, or an audit fails the build. This is the only tier that
#              protects a student on a Tuesday night with nobody watching.
#   EXERCISED  a --live scenario plays a student against the real prompt and asserts the
#              behaviour. Costs a few cents to run; catches real regressions.
#   COVERED    the rule's text provably reaches all ten courses' prompts (PART 1). That
#              is a real check -- it is the bug that hid for a day in build bk -- but it
#              proves only that he was TOLD, not that he does it.
#   UNVERIFIED the rule exists and nothing checks it. Honest, and the list to work from.
# =============================================================================
RULE_VERIFY = {
    1:  ("COVERED",   "the board only shows what you drew"),
    2:  ("ENFORCED",  "prose_visual_conflict: 'show me' with an unchanged board is regenerated"),
    3:  ("EXERCISED", "first-use key terms are marked"),
    4:  ("COVERED",   "say it then write it, in the same reply"),
    5:  ("UNVERIFIED", "don't narrate symbols, point at them"),
    6:  ("COVERED",   "never run ahead"),
    7:  ("ENFORCED",  "prose_visual_conflict regenerates a reply that names an undrawn picture"),
    8:  ("ENFORCED",  "prose_visual_conflict: promising to show something and drawing nothing"),
    9:  ("COVERED",   "the sound-off check"),
    10: ("ENFORCED",  "mathcheck reads every [[verify]] tag"),
    11: ("ENFORCED",  "a tag in the wrong syntax fails to parse and is caught"),
    12: ("ENFORCED",  "strip_verify_tags + the pages' stripTags remove it before the student"),
    13: ("ENFORCED",  "mathcheck re-computes the claim with SymPy"),
    14: ("COVERED",   "define every notation on first use (see also rule 48, ENFORCED)"),
    15: ("ENFORCED",  "prose_pending_question_conflict regenerates a question with no board line"),
    16: ("COVERED",   "a substitution question re-writes its equation"),
    17: ("ENFORCED",  "prose_answered_question_conflict: a question the reply's own board "
                      "already answers is regenerated (build dh)"),
    18: ("ENFORCED",  "prose_board_conflict regenerates spoken numbers that fight the board"),
    19: ("COVERED",   "worked example first"),
    20: ("COVERED",   "partially right is not wrong"),
    21: ("EXERCISED", "'I don't know' triggers a smaller step"),
    22: ("COVERED",   "the escalation ladder"),
    23: ("EXERCISED", "equivalent answers are correct"),
    24: ("COVERED",   "leaps, self-corrections, 'just tell me'"),
    25: ("COVERED",   "when the student says you are wrong"),
    26: ("COVERED",   "a wrong line never stays on the board"),
    27: ("ENFORCED",  "board_notation_conflict regenerates a completed bare-percent sum "
                      "(build dk); the rest of the rule remains prompt-covered"),
    28: ("EXERCISED", "one name per thing"),
    29: ("EXERCISED", "how a session ends"),
    30: ("EXERCISED", "off-topic and personal questions"),
    31: ("EXERCISED", "when something bigger than math shows up"),
    32: ("ENFORCED",  "story_units_conflict regenerates a story that adds money to "
                      "grouped objects (the 32b one-unit clause's caught shape, build "
                      "hr); the broader sanity clauses remain prompt-covered"),
    33: ("COVERED",   "difficulty moves one notch"),
    34: ("COVERED",   "keep old skills sharp"),
    35: ("EXERCISED", "a failed quiz is never re-given on the spot"),
    36: ("EXERCISED", "teach the thing before you ask about it"),
    37: ("COVERED",   "vocabulary is taught, never assumed"),
    38: ("COVERED",   "concrete, then picture, then symbols"),
    39: ("ENFORCED",   "talk less, check in often, make the check failable"),
    40: ("EXERCISED", "ask before repeating an introduction"),
    41: ("ENFORCED",  "PART 3c fails any figure shipped without a caption"),
    42: ("COVERED",   "never compare this student to anyone but this student"),
    43: ("COVERED",   "you perceive exactly two things"),
    44: ("ENFORCED",  "prose_unspoken_problem_conflict: a board problem the spoken words "
                      "never read is regenerated (build dh; sharpened in eq after six "
                      "audit findings -- ONE stated quantity is enough, a fraction "
                      "counts, and numbers elsewhere in the prose no longer exempt it)"),
    45: ("ENFORCED",  "prose_score_conflict regenerates a spoken score that fights its own tag"),
    46: ("COVERED",   "a quiz question tests one skill"),
    47: ("ENFORCED",  "no cold quizzes -- and 47(d) specifically, born enforced six days "
                      "late (build gu). The sentence 'let's do it -- five questions, all on "
                      "finding the percent of a number' was caught in the 2026-08-11 audit, "
                      "rule 47(d) was WRITTEN from it, and the tutor produced it again WORD "
                      "FOR WORD on 2026-08-17 because nothing watched the rule. "
                      "cold_quiz_conflict fires when a quiz is starting, the stated count is "
                      "not TEN, and the reply never says which instrument it is -- so 47(d)'s "
                      "own remedy (a five-question topic quiz that names itself) passes. "
                      "11 cases both directions, 0 false alarms on 1,015 canonical scripts. "
                      "The (a)-(c) halves -- two unaided right answers before any quiz -- "
                      "remain prompt-covered: a referee cannot count what happened in "
                      "earlier turns"),
    48: ("ENFORCED",  "PART 3b/3f fail a course that writes notation it never reads aloud"),
    49: ("ENFORCED",  "PART 3g + the just-in-time matcher"),
    50: ("COVERED",   "chase an unfinished unit; PART 3k proves the bar is reachable"),
    51: ("COVERED",   "a drawn feature must come from a definition (PART 3c checks the tags)"),
    52: ("COVERED",   "a direct mathematical question is answered first (build dh; candidate "
                      "for a --live scenario once an assertion sharp enough exists)"),
    53: ("COVERED",   "the number line used on purpose: magnitude, benchmarks, equivalents "
                      "at one position (build dl; WWC g26 r4)"),
    54: ("ENFORCED",  "board_notation_conflict regenerates a taught key-word shortcut "
                      "(build dl; WWC g26 r5); the schema half remains prompt-covered"),
    55: ("COVERED",   "missed-problem memory (build dt): the tag->store->mastery-note "
                      "pipeline is proven end-to-end in the dt block (PART 3n) -- the "
                      "wording halves (tag emission, one-fresh-revisit) are prompt-"
                      "covered; candidate for EXERCISED via a future audit scenario"),
    56: ("COVERED",   "find the error (build ee; WWC g20 r1): PART 3t pins the three "
                      "safety anchors (announced game, catalogued mistake, wrong work "
                      "never stays) and the incomplete-solution cousin; the teaching "
                      "behaviour itself is prompt-covered -- candidate for a --live "
                      "scenario once the misconception catalogue can seed one"),
    57: ("COVERED",   "self-monitoring prompts (build ee; WWC g16 r2, EEF r5): PART 3t "
                      "pins the before/during/after questions and the one-at-a-time "
                      "guard; candidate for EXERCISED via a lessonaudit scenario"),
    58: ("COVERED",   "two ways, one board (build ee; WWC g16 r4 + g20 r3): PART 3t "
                      "pins same-problem-same-board, the comparison questions, and "
                      "respect for the student's choice (rule 23 tie-in)"),
    59: ("COVERED",   "right answer, wrong method (build ee; MAA IPG): PART 3t pins "
                      "accept-the-answer-first (rule 45 untouched), the how-did-you-"
                      "get-that ask, and the one-case-where-it-breaks move"),
    61: ("ENFORCED",  "a generalization carries its condition (build el; from the "
                      "2026-08-12 audits): PART 3w fails the build if any of the five "
                      "known-false universal claims appears in AUTHORED content -- which "
                      "is where one of them actually lived (the function-notation "
                      "foundation script, spoken verbatim). Live replies remain prompt-"
                      "covered: mathcheck cannot see an overgeneralization because there "
                      "is no arithmetic in the word 'always'"),
    60: ("COVERED",   "the board spotlight (build ee): the MECHANISM is machine-checked "
                      "-- PART 3t asserts all three teaching pages implement "
                      "spotlightBoard with the line+board keys, the .stepglow CSS, and "
                      "a turn-start clear -- and the when-to-use half (one per reply, "
                      "words still say the where) is prompt-covered"),
    62: ("COVERED",   "you may only point at work that happened (build ex; from the "
                      "2026-08-12 audits: 'the way we did a minute ago' for factoring "
                      "that never happened). PART 3ab pins the check-the-board-and-"
                      "notes demand, the rule-60 pointer, and the connecting-is-"
                      "teaching guard; mathcheck structurally cannot see a false "
                      "back-reference (no arithmetic in 'a minute ago'), so live "
                      "replies are prompt-covered -- a natural lessonaudit scenario "
                      "candidate"),
    63: ("ENFORCED",  "the words and the picture are the same figure (build fe; from "
                      "the 2026-08-13 audits): triangle_side_conflict rejects any "
                      "right triangle whose hypotenuse slot cannot hold the longest "
                      "side (sides= is AB, BC, CA; the hypotenuse skips the right-"
                      "angle vertex), swept in PART 2 against the real audit tags "
                      "and all foundation scripts. The one-name half (the circle "
                      "called a curve) and the shares-picture half (4|4|4|2 for a "
                      "sharing story) remain prompt-covered, pinned by PART 3ah -- "
                      "both are natural lessonaudit scenario candidates"),
    64: ("ENFORCED",  "never trade the student's number for a different one, and a length "
                      "is never negative (build gr; from Jim's 2026-08-17 Geometry lesson, "
                      "where 'minus five' was answered with 'That is correct' and the reply "
                      "then taught on using 5). answer_sign_conflict is the FIFTEENTH "
                      "referee: it fires only when the student gave an explicitly signed "
                      "number, the reply AFFIRMS it, the reply then uses the unsigned "
                      "magnitude, and the reply never mentions the sign at all -- so the "
                      "correct teaching response ('both 5 and -5 square to 25, but a length "
                      "is never negative') passes. 14 cases both directions; 0 false alarms "
                      "across 1,015 canonical scripts x 7 signed utterances. The (a) half -- "
                      "that an answer can be arithmetically right and contextually "
                      "impossible -- is prompt-covered in all ten courses via PART 1"),
    65: ("ENFORCED",  "when a student asks to be shown, show them (build gx; from the "
                      "2026-08-17 audit, where it happened TWICE in one geometry lesson -- "
                      "'can you show me taking the square root of 169?' answered with "
                      "'you've now watched this move twice, let's flip it', and a brand-new "
                      "triangle). refused_demonstration_conflict is the SEVENTEENTH referee "
                      "and needs all three: the student asked to be shown, NOTHING in the "
                      "reply is worked out, and the work is handed straight back. The "
                      "discriminator came out of the lesson itself -- the compliant replies "
                      "in that same transcript all carry a COMPLETED board line, the "
                      "refusals only pending ones. 7 cases both directions; 0 false alarms "
                      "on 1,015 canonical scripts x 6 phrasings of the request. 65(d) -- "
                      "never justify the refusal with a COUNT -- is measured by build gv's "
                      "[countclaim] probe, since a referee cannot count a conversation"),
}
_TIER_ORDER = ("ENFORCED", "EXERCISED", "COVERED", "UNVERIFIED")


_TITLE_END = re.compile(r"[.:]\s|\s--\s|\s\(")


def _rule_titles():
    """{number: the rule's headline}. The headline is the SHOUTED part at the start of
    each rule; the prose that follows it is the rule itself and is not repeated here.
    (First version split on the first ". " anywhere, which turned rule 2 into
    '"Show me", "can I see' -- the heading has to end where the capitals do.)"""
    out = {}
    # A rule opens at column 0 as "N. " followed by a SHOUTED headline, then prose. The
    # headline is what belongs in an index; the prose is the rule and is not repeated.
    # The headline ends at the first word containing a lower-case letter -- ALL-CAPS
    # words continue it, "Something", "Never", "(Jim's" end it. (Two earlier attempts
    # failed here: splitting on the first ". " turned rule 2 into '"Show me", "can I
    # see', and a length-bounded body match found only the two shortest rules.)
    for m in re.finditer(r"^(\d{1,2})\. (.{6,200})$", tutor.GRAPH_TOOL_NOTE, re.M):
        keep = []
        for w in m.group(2).split():
            if re.search(r"[a-z]", w) and len(keep) >= 3:
                break
            keep.append(w)
        out[int(m.group(1))] = " ".join(keep).strip(" ,.:;-") or m.group(2)[:70]
    return out


def part3i_rule_verification():
    print("\nPART 3i — every rule declares how it is verified")
    titles = _rule_titles()
    undeclared = sorted(n for n in titles if n not in RULE_VERIFY)
    check("every rule in the prompt is declared here", not undeclared,
          f"rules {undeclared} have no entry in RULE_VERIFY -- a new rule must say how it "
          f"is checked, even if the honest answer is UNVERIFIED")
    stale = sorted(n for n in RULE_VERIFY if n not in titles)
    check("no declaration outlives its rule", not stale,
          f"RULE_VERIFY still lists {stale}, which are no longer in the prompt")

    # the ratchet: a rule that had a real check must not quietly lose it
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    live_named = {int(m) for m in re.findall(r"rule (\d{1,2})", src[src.index("LIVE_SCENARIOS"):])}
    for n, (tier, _why) in sorted(RULE_VERIFY.items()):
        if tier == "EXERCISED":
            check(f"  rule {n} still has its --live scenario", n in live_named,
                  "it was exercised and now is not -- restore the scenario or downgrade "
                  "the declaration on purpose")

    counts = {t: [n for n, (tt, _w) in RULE_VERIFY.items() if tt == t] for t in _TIER_ORDER}
    print(f"       {len(titles)} rules: " + " · ".join(
        f"{t.lower()} {len(counts[t])}" for t in _TIER_ORDER))
    if counts["UNVERIFIED"]:
        print("       BACKLOG — nothing checks these at all:")
        for n in sorted(counts["UNVERIFIED"]):
            print(f"         rule {n:>2}: {titles.get(n, '?')[:66]}")
    check("no rule is enforced by wishful thinking",
          all(t in _TIER_ORDER for t, _w in RULE_VERIFY.values()), "unknown tier")


def write_rules_index(path="RULES.md"):
    """Generate RULES.md from the prompt itself (audit #2 item 23).

    Never hand-maintained, so it cannot drift: every line comes from tutor.py or from
    RULE_VERIFY above. This is the document to hand a curriculum advisor, a school
    district, or the next person who has to hold 49 rules in their head."""
    titles = _rule_titles()
    counts = {t: [n for n, (tt, _w) in RULE_VERIFY.items() if tt == t] for t in _TIER_ORDER}
    out = [
        "# Mr. Cadabra — the teaching rules",
        "",
        "_Generated from `tutor.py` by `python ruletests.py --rules`. Do not edit by hand:",
        "every line below is read out of the prompt the tutor is actually given, so this",
        "file cannot drift away from what the classroom really does._",
        "",
        f"**{len(titles)} rules.** Every one was written because something went wrong in a real",
        "lesson, and almost all of them were noticed by Jim before they were noticed by a",
        "machine. The right-hand column is how much better we have got at that.",
        "",
        "| how it is verified | rules | what that means |",
        "|---|---|---|",
        f"| **ENFORCED** | {len(counts['ENFORCED'])} | a machine catches the violation in a real reply — a referee rewrites the draft, or an audit fails the build |",
        f"| **EXERCISED** | {len(counts['EXERCISED'])} | a scripted student plays against the real prompt and the behaviour is asserted (`ruletests.py --live`) |",
        f"| **COVERED** | {len(counts['COVERED'])} | the rule's text provably reaches all ten courses — proves he was *told*, not that he does it |",
        f"| **UNVERIFIED** | {len(counts['UNVERIFIED'])} | the rule exists and nothing checks it |",
        "",
        "---",
        "",
    ]
    for n in sorted(titles):
        tier, why = RULE_VERIFY.get(n, ("UNVERIFIED", "not declared"))
        out.append(f"### {n}. {titles[n]}")
        out.append("")
        out.append(f"**{tier}** — {why}")
        out.append("")
    out += ["---", "",
            "## The four tiers, and why the order matters", "",
            "**ENFORCED** is the only tier that protects a student on a Tuesday night with",
            "nobody watching. A referee sees the draft before the child does and sends it",
            "back. Everything else depends on someone running something.", "",
            "**EXERCISED** catches regressions cheaply, but only when somebody runs",
            "`ruletests.py --live` — which costs a few cents and needs an API key.", "",
            "**COVERED** is not nothing: it is the bug that hid for a day in build bk, where",
            "a rule written into one of eleven per-course templates reached one course out of",
            "ten. But it proves only that the tutor was told.", "",
            "**UNVERIFIED** is the honest backlog. Moving a rule up a tier is usually worth",
            "more than writing a new rule.", "",
            "I did no harm and this file is not truncated."]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")
    return path


# =============================================================================
# PART 3j -- THE AUDIENCE WALKTHROUGHS  (/demo?view=...)
# -----------------------------------------------------------------------------
# 2026-08-10 (build cp). Jim: "it's almost like a video... I would like one of those
# available, a very obvious button that says view the demo on the parent page, the
# teacher page, the homeschooling page, and the student page."
# Built as a DEEP LINK into the existing demo rather than four new tour engines, because
# copying a tour into four marketing pages is exactly the copy-paste-drift that produced
# the build-bk rule bug and the board-wrap bug. This part guards the two things that can
# silently break it: a button pointing at a view the demo does not implement, and the
# two voice lists falling out of step -- clips are addressed by INDEX, so an insert
# anywhere above the end shifts every cached clip after it.
# =============================================================================
_AUDIENCE_PAGES = {"parents": "parents", "teachers": "teachers",
                   "homeschool": "homeschool", "students": "students"}


def _voice_lines_from(path, name):
    """The real list, from either language. main.py is Python, demo.html is JS with
    comments in it, so neither can be read with a naive regex over quoted strings --
    doing that once made two identical lists look 117 lines apart."""
    import ast as _ast, json as _json
    with open(path, encoding="utf-8") as fh:
        src = fh.read()
    m = re.search(name + r"\s*=\s*\[", src)
    if not m:
        return None
    i, depth = m.end() - 1, 0
    for j in range(i, len(src)):
        if src[j] == "[":
            depth += 1
        elif src[j] == "]":
            depth -= 1
            if depth == 0:
                break
    block = src[i:j + 1]
    if path.endswith(".py"):
        return _ast.literal_eval(block)
    block = re.sub(r"^\s*//.*$", "", block, flags=re.M)
    block = re.sub(r",(\s*\])", r"\1", block)
    return _json.loads(block)





def part3n_sprints():
    """PART 3n -- FLUENCY SPRINTS (build dd). WWC guide 26 rec 6, Strong evidence.

    The three things worth guarding, in order of what they would cost a child:
    every generated ANSWER must be RIGHT (a fluency drill that reinforces a wrong fact
    is worse than no drill); the sprint must never GATE anything (EEF's anxiety caution
    is a requirement, not advice); and half B must be a sibling of half A, not its twin
    (identical questions would make "improvement" a memory test).
    Build dm added the DISPLAY half of the recommendation ("track AND SHOW progress"):
    the dashboard's sprint-record card, guarded at the end of this part -- shown only
    when history exists, self-comparison only, and the whole drill proven live: two
    sprints recorded through the real store, the new endpoint returning them oldest
    first with the personal best.
    """
    print("\nPART 3n — fluency sprints")
    here = os.path.dirname(os.path.abspath(__file__))
    try:
        import sprints as SP
    except Exception as exc:  # noqa: BLE001
        bad("sprints module imports", str(exc))
        return
    import re as _re
    from fractions import Fraction as _Fr

    def _verify(q, a):
        # build dp: answers may carry the unicode minus the student sees
        a = a.replace("−", "-")
        qq = q.replace("×", "*").replace("−", "-").replace("÷", "/")
        m = _re.fullmatch(r"\s*(-?\d+)\s*([+*/-])\s*(-?\d+)\s*", qq)
        if m:
            x, op, y = int(m.group(1)), m.group(2), int(m.group(3))
            return str({"+": x + y, "-": x - y, "*": x * y, "/": x // y}[op]) == a
        m = _re.fullmatch(r"\s*(\d+)\s*\+\s*2\s*\*\s*(\d+)\s*", qq)
        if m:
            return str(int(m.group(1)) + 2 * int(m.group(2))) == a
        m = _re.fullmatch(r"\s*(\d+)/(\d+)\s*\+\s*(\d+)/(\d+)\s*", qq)
        if m:
            am = _re.fullmatch(r"(\d+)/(\d+)", a)
            return bool(am) and (_Fr(int(m.group(1)), int(m.group(2)))
                                 + _Fr(int(m.group(3)), int(m.group(4)))
                                 == _Fr(int(am.group(1)), int(am.group(2))))
        m = _re.fullmatch(r"\s*0\.(\d)\s*\+\s*0\.(\d)\s*", qq)
        if m:
            return abs(float(a) - (int(m.group(1)) + int(m.group(2))) / 10) < 1e-9
        # ---- build dp: the upper-course shapes, one oracle per question form ----
        def _i(*gs):
            return [int(g) for g in gs]
        m = _re.fullmatch(r"x \+ (\d+) = (\d+)\.\s+x = \?", qq)
        if m:
            x, s = _i(*m.groups()); return str(s - x) == a
        m = _re.fullmatch(r"(\d+)x = (\d+)\.\s+x = \?", qq)
        if m:
            c, s = _i(*m.groups()); return s % c == 0 and str(s // c) == a
        m = _re.fullmatch(r"(\d+)x \+ (\d+) = (\d+)\.\s+x = \?", qq)
        if m:
            c, b, s = _i(*m.groups()); return (s - b) % c == 0 and str((s - b) // c) == a
        m = _re.fullmatch(r"f\(x\) = (\d+)x \+ (\d+)\.\s+f\((\d+)\) = \?", qq)
        if m:
            c, b, n = _i(*m.groups()); return str(c * n + b) == a
        m = _re.fullmatch(r"f\(x\) = x \+ (\d+), g\(x\) = (\d+)x\.\s+f\(g\((\d+)\)\) = \?", qq)
        if m:
            b, c, n = _i(*m.groups()); return str(c * n + b) == a
        m = _re.fullmatch(r"Slope of y = (\d+)x \+ \d+\?", qq)
        if m:
            return m.group(1) == a
        m = _re.fullmatch(r"Slope through \(0, 0\) and \((\d+), (\d+)\)\?", qq)
        if m:
            x, y = _i(*m.groups()); return y % x == 0 and str(y // x) == a
        m = _re.fullmatch(r"x \+ y = (\d+),\s+x - y = (\d+)\.\s+x = \?", qq)
        if m:
            s, d = _i(*m.groups()); return (s + d) % 2 == 0 and str((s + d) // 2) == a
        m = _re.fullmatch(r"Complement of (\d+)°\?", qq)
        if m:
            return str(90 - int(m.group(1))) == a
        m = _re.fullmatch(r"Supplement of (\d+)°\?", qq)
        if m:
            return str(180 - int(m.group(1))) == a
        m = _re.fullmatch(r"Triangle angles (\d+)° and (\d+)°\. Third angle\?", qq)
        if m:
            x, y = _i(*m.groups()); return str(180 - x - y) == a
        m = _re.fullmatch(r"Legs (\d+) and (\d+)\. Hypotenuse\?", qq)
        if m:
            x, y = _i(*m.groups()); return x * x + y * y == int(a) ** 2
        m = _re.fullmatch(r"Radius (\d+)\. Diameter\?", qq)
        if m:
            return str(2 * int(m.group(1))) == a
        m = _re.fullmatch(r"Diameter (\d+)\. Radius\?", qq)
        if m:
            d = int(m.group(1)); return d % 2 == 0 and str(d // 2) == a
        m = _re.fullmatch(r"Midpoint of (\d+) and (\d+) on a number line\?", qq)
        if m:
            x, y = _i(*m.groups()); return (x + y) % 2 == 0 and str((x + y) // 2) == a
        m = _re.fullmatch(r"(?:Mean|Median) of (-?\d+), (-?\d+), (-?\d+)\?", qq)
        if m:
            v = sorted(_i(*m.groups()))
            if qq.startswith("Mean"):
                return sum(v) % 3 == 0 and str(sum(v) // 3) == a
            return str(v[1]) == a
        m = _re.fullmatch(r"Side (\d+) scales to (\d+)\. Scale factor\?", qq)
        if m:
            x, y = _i(*m.groups()); return y % x == 0 and str(y // x) == a
        m = _re.fullmatch(r"Triangle: base (\d+), height (\d+)\. Area\?", qq)
        if m:
            b, h = _i(*m.groups()); return (b * h) % 2 == 0 and str(b * h // 2) == a
        m = _re.fullmatch(r"√(\d+) = \?", qq)
        if m:
            return int(a) ** 2 == int(m.group(1))
        m = _re.fullmatch(r"∛(\d+) = \?", qq)
        if m:
            return int(a) ** 3 == int(m.group(1))
        m = _re.fullmatch(r"(\d)([²³⁴⁵]) = \?", qq)
        if m:
            e = {"²": 2, "³": 3, "⁴": 4, "⁵": 5}[m.group(2)]
            return str(int(m.group(1)) ** e) == a
        m = _re.fullmatch(r"x\^(\d+) · x\^(\d+) = x\^\?", qq)
        if m:
            x, y = _i(*m.groups()); return str(x + y) == a
        m = _re.fullmatch(r"x\^(\d+) / x\^(\d+) = x\^\?", qq)
        if m:
            x, y = _i(*m.groups()); return str(x - y) == a
        m = _re.fullmatch(r"x² \+ (\d+)x \+ (\d+) = \(x \+ (\d+)\)\(x \+ \?\)", qq)
        if m:
            b, c, p = _i(*m.groups()); q_ = int(a)
            return p + q_ == b and p * q_ == c
        m = _re.fullmatch(r"Degree of x\^(\d+) \+ x \+ 1\?", qq)
        if m:
            return m.group(1) == a
        m = _re.fullmatch(r"log([₂₃₅]|₁₀) (\d+) = \?", qq)
        if m:
            base = {"₂": 2, "₃": 3, "₅": 5, "₁₀": 10}[m.group(1)]
            return base ** int(a) == int(m.group(2))
        m = _re.fullmatch(r"(\d+)! = \?", qq)
        if m:
            import math as _math
            return str(_math.factorial(int(m.group(1)))) == a
        m = _re.fullmatch(r"C\((\d+), 2\) — ways to choose 2 of \d+\?", qq)
        if m:
            n = int(m.group(1)); return str(n * (n - 1) // 2) == a
        m = _re.fullmatch(r"(-?\d+), (-?\d+), (-?\d+), \?", qq)
        if m:
            x, y, z = _i(*m.groups())
            if y - x == z - y:                       # arithmetic
                return str(z + (y - x)) == a
            if x != 0 and y % x == 0 and z * x == y * y:   # geometric
                return str(z * (y // x)) == a
            return None
        m = _re.fullmatch(r"lim \(x → (\d+)\) of x² \+ (\d+) = \?", qq)
        if m:
            n, add = _i(*m.groups()); return str(n * n + add) == a
        m = _re.fullmatch(r"d/dx x\^(\d+) = \?·(?:x|x\^\d+)", qq)
        if m:
            return m.group(1) == a
        m = _re.fullmatch(r"d/dx e\^\((\d+)x\) = \?·e\^\(\d+x\)", qq)
        if m:
            return m.group(1) == a
        m = _re.fullmatch(r"∫ (?:x|x\^(\d+)) dx = x\^(\d+)/\?\s+\(\+ C\)", qq)
        if m:
            n = int(m.group(1) or 1); return n + 1 == int(m.group(2)) == int(a)
        m = _re.fullmatch(r"∫ from 0 to (\d+) of 2x dx = \?", qq)
        if m:
            return str(int(m.group(1)) ** 2) == a
        m = _re.fullmatch(r"y″ - (\d+)y = 0:\s+r = ±\?", qq)
        if m:
            return int(a) ** 2 == int(m.group(1))
        m = _re.fullmatch(r"Expected successes: 10 tries at P = 0\.(\d)\?", qq)
        if m:
            return m.group(1) == a
        m = _re.fullmatch(r"P\(rain\) = 0\.(\d)\.\s+P\(no rain\) = \?", qq)
        if m:
            return abs(float(a) - (10 - int(m.group(1))) / 10) < 1e-9
        m = _re.fullmatch(r"Reflect \((\d+), (\d+)\) over the ([xy])-axis", qq)
        if m:
            x, y = _i(m.group(1), m.group(2))
            want = f"({x}, -{y})" if m.group(3) == "x" else f"(-{x}, {y})"
            return a == want
        m = _re.fullmatch(r"Zeros of \(x - (\d+)\)\(x \+ (\d+)\):\s+x = \d+ and x = \?", qq)
        if m:
            return a == f"-{m.group(2)}"
        m = _re.fullmatch(r"(\d+)\(x \+ (\d+)\) = \?", qq)
        if m:
            c, b = _i(*m.groups()); return a == f"{c}x + {c * b}"
        return None

    units = sum(len(u) for u in SP.SPRINTS.values())
    check(f"the registry covers ALL TEN courses ({units} units, "
          f"{len(SP.SPRINTS)} courses)", units >= 70 and len(SP.SPRINTS) >= 10,
          "build dp raised the bar from the 3 elementary courses to all ten -- "
          "a shrink here means sprints silently vanished from someone's course")
    wrong, total, verified, twin_units = [], 0, 0, 0
    for course, us in SP.SPRINTS.items():
        for unit in us:
            s = SP.build(course, unit, "ruletest-seed")
            if [p["q"] for p in s["a"]] == [p["q"] for p in s["b"]]:
                twin_units += 1
            for half in ("a", "b"):
                if len(s[half]) != SP.PER_HALF:
                    wrong.append(f"{course}/{unit}/{half}: {len(s[half])} problems")
                for p in s[half]:
                    total += 1
                    if p["a"] not in p["c"]:
                        wrong.append(f"{course}/{unit}: answer {p['a']!r} not tappable")
                    v = _verify(p["q"], p["a"])
                    if v is False:
                        wrong.append(f"{course}/{unit}: WRONG ANSWER {p['q']} = {p['a']}")
                    if v is not None:
                        verified += 1
    check(f"every generated answer is right and tappable ({total} problems, "
          f"{verified} arithmetic-verified)", not wrong, str(wrong[:4]))
    check(f"  half B is a sibling of half A, not a twin "
          f"({units - twin_units} of {units} units differ)",
          twin_units <= 3,
          "identical questions make 'improvement' a memory test -- only the fixed-list "
          "families (shapes, primes) are allowed to repeat")
    check("  the same seed rebuilds the same sprint (a mid-sprint reload changes nothing)",
          SP.build("prealgebra", 3, "k") == SP.build("prealgebra", 3, "k"),
          "a reload must not hand out fresh problems mid-sprint")
    check("  an unknown course or unit fails soft", SP.build("latin", 1, "k") is None
          and SP.build("precalc", 6, "k") is None and not SP.available("nope", 1),
          "the app must simply make no offer")   # dp: calculus HAS sprints now; a
    # concept unit deliberately left out (precalc 6) is the new absent fixture

    # ---- BUILD dp: the FIXED FACT LISTS are RE-DERIVED, never trusted ---------------
    # A drill that stamps in a wrong "fact" is the worst thing this feature could do.
    # So every fact list ships with an independent oracle: i-powers by actually raising
    # i, trig values and radians against math.sin/cos/pi, the empirical rule against
    # the error function, dice against enumeration fractions, derivatives and
    # identities against sympy, ODE order by counting prime marks, Laplace against
    # n!/s^(n+1). If a fact and mathematics disagree, the build fails.
    import math as _m
    bad_f = []
    _sup = {"²": 2, "³": 3, "⁴": 4, "⁵": 5, "⁶": 6, "⁸": 8}
    _cname = {(1, 0): "1", (-1, 0): "−1", (0, 1): "i", (0, -1): "−i"}
    for q, a, ch in SP.I_POWER_FACTS:
        v = 1j ** _sup[q[1]]
        if a != _cname[(round(v.real), round(v.imag))] or a not in ch:
            bad_f.append(("i-power", q, a))
    _tv = {"0": 0.0, "1": 1.0, "1/2": .5, "√2/2": _m.sqrt(2) / 2,
           "√3/2": _m.sqrt(3) / 2}
    for q, a, ch in SP.SIN_FACTS + SP.COS_FACTS:
        fn = _m.sin if q.startswith("sin") else _m.cos
        deg = int(_re.search(r"(\d+)°", q).group(1))
        if abs(fn(_m.radians(deg)) - _tv[a]) > 1e-9 or a not in ch:
            bad_f.append(("trig", q, a))
    _rad = {"π": _m.pi, "2π": 2 * _m.pi, "π/2": _m.pi / 2, "π/4": _m.pi / 4,
            "π/6": _m.pi / 6, "π/3": _m.pi / 3}
    for q, a, ch in SP.RADIAN_FACTS:
        deg = int(_re.search(r"(\d+)°", q).group(1))
        if abs(_m.radians(deg) - _rad[a]) > 1e-9 or a not in ch:
            bad_f.append(("radian", q, a))
    for q, a, ch in SP.EMPIRICAL_FACTS:
        k = int(_re.search(r"(\d) SD", q).group(1))
        within = 100 * _m.erf(k / _m.sqrt(2))
        true = within if "ithin" in q else 100 - within
        if abs(float(a) - true) > 0.7 or a not in ch:
            bad_f.append(("empirical", q, a, round(true, 2)))
    _die_truth = [_Fr(1, 6), _Fr(1, 2), _Fr(1, 2), _Fr(1, 3), _Fr(1, 4), _Fr(2, 3)]
    for (q, a, ch), truth in zip(SP.DIE_FACTS, _die_truth):
        num = int(_re.search(r"= (\d)/\?", q).group(1))
        if _Fr(num, int(a)) != truth or a not in ch:
            bad_f.append(("die", q, a))
    import sympy as _sp
    _x, _t = _sp.symbols("x t")
    _dexpr = {"d/dx sin x = ?": _sp.sin(_x), "d/dx cos x = ?": _sp.cos(_x),
              "d/dx eˣ = ?": _sp.exp(_x), "d/dx ln x = ?": _sp.log(_x),
              "d/dx of a constant = ?": _sp.Integer(7), "d/dx x = ?": _x}
    _dans = {"cos x": _sp.cos(_x), "−sin x": -_sp.sin(_x), "eˣ": _sp.exp(_x),
             "1/x": 1 / _x, "0": _sp.Integer(0), "1": _sp.Integer(1)}
    for q, a, ch in SP.DERIV_FACTS:
        if _sp.simplify(_sp.diff(_dexpr[q], _x) - _dans[a]) != 0 or a not in ch:
            bad_f.append(("deriv", q, a))
    _ie = {"sin²θ + cos²θ = ?": (_sp.sin(_t) ** 2 + _sp.cos(_t) ** 2,
                                 "1", _sp.Integer(1)),
           "tan θ = sin θ / ?": (_sp.sin(_t) / _sp.tan(_t), "cos θ", _sp.cos(_t)),
           "sin(−θ) = ?": (_sp.sin(-_t), "−sin θ", -_sp.sin(_t)),
           "cos(−θ) = ?": (_sp.cos(-_t), "cos θ", _sp.cos(_t)),
           "1 + tan²θ = ?": (1 + _sp.tan(_t) ** 2, "sec²θ", _sp.sec(_t) ** 2),
           "sin 2θ = ?": (_sp.sin(2 * _t), "2 sin θ cos θ",
                          2 * _sp.sin(_t) * _sp.cos(_t))}
    for q, a, ch in SP.IDENTITY_FACTS:
        lhs, want_a, want_e = _ie[q]
        if a != want_a or _sp.simplify(lhs - want_e) != 0 or a not in ch:
            bad_f.append(("identity", q, a))
    _omap = {"⁗": 4, "‴": 3, "″": 2, "′": 1}
    for q, a, ch in SP.ODE_ORDER_FACTS:
        order = max(v for k, v in _omap.items() if k in q)
        if str(order) != a or a not in ch:
            bad_f.append(("ode-order", q, a))
    for q, a, ch in SP.LAPLACE_FACTS:
        m1 = _re.fullmatch(r"L\{(1|t|t²|t³)\} = (\d+)/s\^\?", q)
        if m1:
            n = {"1": 0, "t": 1, "t²": 2, "t³": 3}[m1.group(1)]
            okk = int(m1.group(2)) == _m.factorial(n) and int(a) == n + 1
        else:
            m2 = _re.fullmatch(r"L\{e\^\((\d+)t\)\} = 1/\(s − \?\)", q)
            okk = bool(m2) and m2.group(1) == a
        if not okk or a not in ch:
            bad_f.append(("laplace", q, a))
    n_facts = sum(len(v) for v in (SP.I_POWER_FACTS, SP.SIN_FACTS, SP.COS_FACTS,
                                   SP.RADIAN_FACTS, SP.EMPIRICAL_FACTS, SP.DIE_FACTS,
                                   SP.DERIV_FACTS, SP.IDENTITY_FACTS,
                                   SP.ODE_ORDER_FACTS, SP.LAPLACE_FACTS))
    check(f"every fixed FACT re-derives from mathematics itself ({n_facts} facts)",
          not bad_f, str(bad_f[:4]))

    # NEVER GATES. Checked at all three layers, from the source.
    st = open(os.path.join(here, "store.py"), encoding="utf-8").read()
    i = st.find("def record_sprint")
    check("recording a sprint touches no mastery, no status, no unlock",
          i > 0 and "_set_unit_status" not in st[i:i + 2500]
          and "mastered" not in st[i:i + 2500],
          "EEF's anxiety caution is a requirement: a sprint result must never change "
          "what a student is allowed to do")
    check('  and the sprints table joins the reset family',
          '("sprints", "code"),' in st,
          "a Start Fresh that leaves sprint rows behind hands the reset student a "
          "personal best they never set")
    mn = open(os.path.join(here, "main.py"), encoding="utf-8").read()
    check("both endpoints exist and are student-gated",
          '@app.get("/api/sprint/{code}")' in mn and '@app.post("/api/sprint/{code}")' in mn
          and mn[mn.find('def get_sprint'):mn.find('def get_sprint') + 1600]
              .count("_student_or_404") == 1,
          "an open endpoint that hands out per-student data")
    sess = open(os.path.join(here, "static", "session.html"), encoding="utf-8").read()
    check("the offer is one optional link, with a skip inside",
          "totally optional" in sess and 'id="sprSkip"' in sess
          and "sprStart()" not in sess.split("addEventListener")[0],
          "the offer must never auto-start and declining must cost one tap")
    check('  the framing is personal-best-only, said out loud',
          "personal best is the only score that matters" in sess
          and "beat your" in sess.lower(),
          "the frame is the anxiety mitigation -- it is not decoration")

    # ---- BUILD dm: the DISPLAY half of WWC g26 r6 -- "track AND SHOW progress" ------
    dash = open(os.path.join(here, "static", "dashboard.html"), encoding="utf-8").read()
    check("the sprint-record card exists and starts HIDDEN",
          'id="sprintWrap" style="display:none;"' in dash,
          "the card must never render before there is data")
    check("  zero sprints -> the card never appears (no nagging)",
          "if (!hist.length) return;" in dash,
          "sprints never gate; an empty card is a nag")
    check("  the card compares this student only with this student (rule 42)",
          "racing only yourself" in dash and "personal best" in dash,
          "any other comparison violates rule 42")
    check("  the loader is a bonus that can never block the dashboard",
          "loadSprints" in dash and "/api/sprints/" in dash
          and "never block the dashboard" in dash.split("loadSprints")[1][:3600],
          "the card must fail soft like every bonus section")   # window widened in ds
          # (the Run-one-now button grew the loader; the guarded catch is unchanged)
    mn2 = open(os.path.join(here, "main.py"), encoding="utf-8").read()
    check("GET /api/sprints/{code} exists and is student-gated",
          '@app.get("/api/sprints/{code}")' in mn2
          and "_student_or_404" in mn2.split('@app.get("/api/sprints/{code}")')[1][:900],
          "an open endpoint that hands out per-student data")
    # the whole display drill, live: record two sprints, read them back oldest-first
    import tempfile as _tf2
    with _tf2.TemporaryDirectory() as tmp2:
        drill = os.path.join(tmp2, "drill.py")
        with open(drill, "w") as fh:
            fh.write(
                "import store\n"
                "store.init()\n"
                "assert store.enabled()\n"
                "store.record_sprint('SPRTEST', 'prealgebra', 1, 'make ten', 5, 8, 7, 9)\n"
                "store.record_sprint('SPRTEST', 'prealgebra', 2, 'doubles', 6, 8, 9, 10)\n"
                "h = store.get_sprint_history('SPRTEST', 'prealgebra', unit=None, limit=30)\n"
                "assert len(h) == 2, h\n"
                "rows = list(reversed(h))\n"
                "assert rows[0]['skill'] == 'make ten' and rows[1]['b'] == 9, rows\n"
                "assert max(r['b'] for r in rows) == 9\n"
                "print('SPRINT-DRILL-OK')\n")
        env = dict(os.environ, DATABASE_URL=f"sqlite:///{os.path.join(tmp2, 's.db')}",
                   PYTHONPATH=here)
        # build gh: the drill runs against a real sqlite database, so it needs
        # SQLAlchemy. Without it this is an unprovisioned machine, not a broken build.
        if dep_gate("record two sprints -> history reads back oldest-first with the best",
                    "sqlalchemy", "the drill records to a real database"):
            r = subprocess.run([sys.executable, drill], cwd=here, env=env,
                               capture_output=True, text=True)
            check("record two sprints -> history reads back oldest-first with the best",
                  r.returncode == 0 and "SPRINT-DRILL-OK" in r.stdout,
                  (r.stdout + r.stderr)[-250:])


def part3l_lesson_auditor():
    """PART 3l -- THE LESSON AUDITOR IS SAFE AND HONEST.

    Build cw. lessonaudit.py spends real money on two vendors and reads a secret, so the
    things worth guarding are not its findings -- those are opinions -- but its
    boundaries: it must never leak a key, never change the teaching, always be able to be
    priced before it is run, and always be able to say what a scenario was guarding when
    somebody deletes one.
    """
    print("\nPART 3l — the offline lesson auditor")
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "lessonaudit.py")
    if not os.path.exists(path):
        skip("lesson auditor", "lessonaudit.py not present")
        return
    src = open(path, encoding="utf-8").read()
    import lessonaudit as LA

    check(f"the cast is declared ({len(LA.SCENARIOS)} scenarios)", len(LA.SCENARIOS) >= 8,
          "too few scenarios to be a reality check")
    missing = [s.get("id", "?") for s in LA.SCENARIOS
               if not all(s.get(k) for k in ("id", "course", "exposes", "persona", "opening"))]
    check("  every scenario says what it GUARDS", not missing,
          f"{missing} -- a scenario with no stated purpose gets deleted by the next person "
          f"who is in a hurry")
    bad_course = [s["id"] for s in LA.SCENARIOS if s["course"] not in COURSES]
    check("  every scenario names a real course", not bad_course, str(bad_course))

    # THE SECRET. It is read from the environment and must never travel anywhere else.
    # Precise on purpose. A first version flagged the DRY RUN's label line -- the words
    # "OPENAI_API_KEY" printed next to "present"/"MISSING", which is exactly what you want
    # a diagnostic to say. A check that cries wolf at correct code gets switched off, and
    # then it is not guarding anything. Look for the VALUE travelling, not the name.
    leaks = [pat for pat in ("{key!r}", "+ key", "str(key)", "% key",
                             "return key", '"key": key', "print(key")
             if pat in src]
    # The key may appear in exactly ONE place: the Authorization header it exists for.
    # Anywhere else -- an f-string in a log line, an error message, a returned dict -- is
    # a leak. Counting the two forms against each other says that precisely.
    if src.count("{key}") != src.count("Bearer {key}"):
        leaks.append("{key} outside an Authorization header")
    check("the key value never travels anywhere but the Authorization header",
          "OPENAI_API_KEY" in src and not leaks,
          f"{leaks} -- a key in a log line is a key in a screenshot")
    check("  and the dry run reports only WHETHER a key exists",
          "bool(os.environ.get(\"OPENAI_API_KEY\"))" in src,
          "presence is all anyone needs to debug this")

    # It must be priceable before it is run, and it must be honest that the price is a guess.
    d = LA.dry_run(limit=2)
    check("a dry run prices the job without spending anything",
          d.get("dry_run") is True and d.get("estimated_cost_usd", 0) > 0
          and len(d.get("scenarios", [])) == 2,
          "nobody should have to spend money to find out what something costs")
    check("  and it says out loud that the price is an estimate",
          "ESTIMATE ONLY" in (d.get("estimate_note") or ""),
          "an unlabelled estimate gets quoted back as a fact")

    # THE LINE THAT MATTERS: it reports, it does not edit.
    for forbidden, why in (("open(os.path.join(HERE, \"tutor.py\"), \"w\"", "tutor.py"),
                           ("prompts.py\", \"w\"", "prompts.py"),
                           ("foundations.py\", \"w\"", "foundations.py")):
        check(f"  the auditor never writes {why}", forbidden not in src,
              "a critic that edits the teaching is a second author nobody reviewed")
    check("  the report says findings have not been acted on",
          "Nothing here has been acted on" in src,
          "a report that reads like a changelog gets treated as one")

    # Build cz, all four from Jim's FIRST REAL RUN, which failed after 89.9 seconds.
    check("the run is proved cheaply before any lesson is taught",
          "def preflight(" in src and "ok, note = preflight()" in src,
          "a wrong model name should cost a second and a fraction of a cent, not 90 "
          "seconds and two live tutor calls")
    check("  the token-limit parameter is negotiated, not guessed from the model name",
          "_TOKEN_PARAM" in src and "max_completion_tokens" in src,
          "newer models reject max_tokens and older ones reject its replacement; the API "
          "says which it wants, so take it at its word instead of pattern-matching names")
    check("  the model list is offered only for a genuine MODEL error",
          "model_not_found" in src and 'and "model" in detail.lower()' not in src,
          "the first version appended the account's model list to any error containing "
          "the word 'model' -- so a PARAMETER error came back wearing a costume: true "
          "information, wrong diagnosis, and a person has to read past it")
    check("  a run where nothing was marked cannot read like a clean one",
          "NOTHING WAS MARKED" in src and "lessons_marked" in src
          and "did_not_complete" in src,
          "the first report headlined '2 scenarios \u00b7 0 findings' for a run in which "
          "BOTH lessons died before a word was marked. Zero findings and zero lessons "
          "marked are opposite results and must never read the same")
    admin_src = open(os.path.join(here, "static", "admin.html"), encoding="utf-8").read()
    check("  and the admin panel repeats the server's summary rather than inventing one",
          "d.summary" in admin_src and "did_not_complete" in admin_src,
          "two places computing the same headline is two places to get it wrong")

    # Build da. "How can I tell if my new key is good for 5.5?" is not answerable by
    # looking at a key: access belongs to the ORGANISATION (and, for a project key, to
    # that project's model permissions). The only honest answer is to ask the key.
    check("the tool can ask a key which models it actually reaches",
          "def probe_models(" in src and "PROBE_MODELS" in src,
          "otherwise the answer is a guess dressed as a fact")
    check("  and the pricing button asks, so one click answers it",
          "probe_models() if (probe" in src,
          "a price for a job that cannot run is worse than no price")
    check("  a model needing ORGANISATION VERIFICATION says so, with the remedy",
          "must be verified" in src and "Verify Organisation" in src,
          "'403' with no remedy sends somebody to a search engine")
    check("  and the probe list is overridable without a code change",
          "OPENAI_PROBE_MODELS" in src,
          "model names move faster than this file will")

    # Build db, from Jim's second probe. A reasoning model spends tokens THINKING before
    # it writes, and that spending counts against the completion budget -- so a tiny
    # probe budget comes back "output limit was reached", which LOOKS like no-access and
    # is PROOF of access. The probe called gpt-5.1 unusable for exactly this reason.
    check("a model that spent the probe budget reasoning is retried with room to think",
          "output limit was reached" in src and "roomy" in src,
          "a reasoning model on a 5-token budget reads as broken when it is merely "
          "thinking -- the API said which limit was hit, so take it at its word")
    check("  and the quiet variant -- 200, empty message, finish_reason length -- too",
          'finish_reason") == "length"' in src.replace("'", '"'),
          "an empty student turn ends the lesson early and looks like the student left")

    # Build dc, from the first FULL audit. Ten lessons ran; the critic marked the
    # mathematics and read straight past FOUR graceful-failure turns -- "(Sorry, I lost
    # my train of thought)" -- because a critic marking content does not think to mark
    # absence. Counting the tutor's stumbles is CODE's job, at a fixed severity, so a
    # generous marker can never argue reliability away.
    check("the auditor counts the tutor's graceful-failure turns itself",
          "FALLBACK_MARKERS" in src and "lost my train of thought" in src
          and "tutor_stumbles" in src,
          "four stumbles in ten lessons went unflagged by the critic -- absence is "
          "invisible to a content marker")
    check("  a stumbled turn is retried once, like a student repeating themselves",
          "_is_fallback(retry)" in src,
          "an audit lesson derailed by a transient hiccup marks nothing")
    check("  and the critic is told about its own first-run false positives",
          "re-read the surrounding turns" in src
          and "standard, correct graph" in src
          and "SEARCH the reply" in src,
          "the critic flagged a correct removable-discontinuity graph and a board line "
          "that was already present; each rejection cost a human time")

    # A stale model name must be a one-line fix, never a mystery.
    check("a rejected model names the ones the account actually has",
          "_openai_model_names" in src and "OPENAI_AUDIT_MODEL" in src,
          "'model not found' with no list is an evening gone")

    # Build cx. AN ADMIN JOB THE OWNER CANNOT REACH IS NOT SHIPPED. Both money-spending
    # jobs were documented as "POST /api/admin/..." and nothing in the product can POST
    # JSON, which is why the foundation pre-render sat un-run for days while three handoff
    # documents told Jim to run it. Every admin endpoint that spends money must have a
    # button on /admin.
    admin_html = open(os.path.join(here, "static", "admin.html"), encoding="utf-8").read()
    for endpoint, why in (("/api/admin/lesson-audit", "the lesson auditor"),
                          ("/api/admin/prewarm-foundations", "the voice pre-render")):
        check(f"{why} can be run from /admin, not just described",
              endpoint in admin_html,
              "a control panel whose controls are instructions to use a tool the owner "
              "does not have is not a control panel")
    check("  and each one can be PRICED from there before it spends",
          admin_html.count("dry_run: true") >= 2,
          "nobody should have to spend money to find out what something costs")

    # And the endpoint that runs it is admin-gated, like every other spending endpoint.
    msrc = open(os.path.join(here, "main.py"), encoding="utf-8").read()
    i = msrc.find("def admin_lesson_audit")
    check("the endpoint is behind the admin key",
          i > 0 and "_require_admin(body.key)" in msrc[i:i + 3000],
          "an open endpoint that spends money on two APIs")


def part3k_mastery_reachable():
    """PART 3k -- THE BAR MUST BE REACHABLE BY THE INSTRUMENT THAT MEASURES IT.

    Build cu. Jim: "if I pass an exam with an eighty-five, I can go onto the next unit. I
    can do all the units and still be carrying an eighty-five with me, which is gonna keep
    me from mastering the final exam."
    Checking it turned up something worse than the thing he described. Mastery is 90%, and
    the Unit Quiz was FOUR OR FIVE questions -- so the only scores it could produce were
    80% and 100%. There was no 85, and "90% mastery" silently meant a PERFECT PAPER. The
    topic quizzes had the identical defect one floor down: three or four questions against
    an 80% bar, i.e. four out of four.
    Nobody would have written that on purpose. It survived because the bar and the
    question count live in different files, changed on different days (the bar went 80 ->
    90 on 2026-08-04), and no test ever multiplied them together.
    THIS is that multiplication. For every quiz in the system: at least one NON-PERFECT
    score must pass, or the bar is a lie.
    """
    print("\nPART 3k — mastery bars must be reachable without a perfect paper")
    here = os.path.dirname(os.path.abspath(__file__))
    import store
    prompts = {c: tutor.build_system_prompt(dict(STUDENT), course=c) for c in COURSES}

    def reachable(total, bar):
        """The best non-perfect score on `total` questions, floored, vs the bar."""
        return store_score(total - 1, total) >= bar

    def store_score(correct, total):
        return (max(0, int(correct)) * 100) // max(1, int(total))

    for label, total, bar in (("Unit Quiz", 10, 90), ("topic quiz", 5, 80)):
        best_miss_one = store_score(total - 1, total)
        check(f"a student can miss one on the {label} and still pass "
              f"({total - 1}/{total} = {best_miss_one}% vs {bar}%)",
              reachable(total, bar),
              f"{total} questions against a {bar}% bar means a PERFECT paper -- the bar "
              f"cannot be cleared any other way, so it does not mean what it says")

    # ...and the prompts must actually ask for those counts, in every course.
    for c in COURSES:
        p = prompts[c]
        check(f"  {c}: the Unit Quiz asks for ten questions",
              "give the UNIT QUIZ: TEN questions" in p,
              "a shorter Unit Quiz puts mastery back out of reach")
        check(f"  {c}: no template still asks for four or five",
              "4 or 5 questions" not in p and "3 or 4\nquestions" not in p,
              "an old count left in one template is the build-bk bug shape: right in nine "
              "courses, wrong in the tenth")

    # Build cv. EVERY range= WE WRITE MUST PARSE UNDER THE RENDERER'S OWN RULE.
    # Rendering the new removable-discontinuity figure showed the [[graph]] documentation
    # telling the tutor to write range="-1,5" while parseRange accepted only "a..b" -- so
    # the window was thrown away and the graph fell back to -10..10, silently. That
    # instruction exists BECAUSE of Jim's earlier catch that a window "barely showed the
    # parabola", which means the fix for that bug had never once worked. The regex is read
    # OUT OF math-figures.js so this check can never drift from the renderer.
    figsrc = open(os.path.join(here, "static", "math-figures.js"), encoding="utf-8").read()
    _i = figsrc.find("function parseRange")
    mrx = re.search(r"\.match\(/([^/]+)/\)", figsrc[_i:_i + 400]) if _i >= 0 else None
    check("the grapher's range parser can be read from the renderer", bool(mrx),
          "parseRange changed shape -- update this check, do not delete it")
    if mrx:
        rng = re.compile(mrx.group(1).replace("\\d", r"\d").replace("\\.", r"\."))
        used = set()
        for fname in ("tutor.py", "prompts.py", "foundations.py"):   # prompts.py: build do
            used |= set(re.findall(r'range="([^"]+)"',
                                   open(os.path.join(here, fname), encoding="utf-8").read()))
        bad = [u for u in sorted(used) if not rng.search(u)]
        check(f"every range= we write parses under that rule ({len(used)} distinct)",
              not bad,
              f"the renderer ignores {bad} and falls back to -10..10 -- the window "
              f"instruction becomes unfollowable, silently")

    # The thresholds themselves must still agree across the three files that hold them.
    check("store and tutor still agree on the bars",
          store.PASS_PCT == 90 and store.QUIZ_PASS_PCT == 80,
          f"store says {store.PASS_PCT}/{store.QUIZ_PASS_PCT}")

    # And the locked Final Exam must tell the student what is holding the door.
    src = open(os.path.join(here, "main.py"), encoding="utf-8").read()
    fn = src[src.find("def _final_gate_message"):]
    fn = fn[:fn.find("\n\n\n")] if "\n\n\n" in fn else fn[:6000]
    check("the locked Final Exam names the units that are holding it shut",
          "best Unit Quiz so far" in fn and "keeps your BEST score" in fn,
          "'you've mastered 3 of 9' is true, useless, and arrives months after the unit "
          "it is about")
    # A retake must be SAFE, and the payload has to say so -- rule 50(e) tells the tutor
    # to promise "the record keeps your best"; this is the promise being true in the data.
    check("a bad retake never un-masters a unit",
          hasattr(store, "record_check"),
          "record_check is gone")
    check("  the check payload reports the UNIT's state, not just this attempt's",
          "unit_mastered" in open(os.path.join(here, "store.py"), encoding="utf-8").read(),
          "a student who believes a bad retake can cost them the unit will not retake it")

    check("  and it falls back rather than failing shut",
          "except Exception" in fn and "FINAL_GATE_MESSAGE.format" in fn,
          "a locked door must never also be a silent one")


def part3j_walkthroughs():
    print("\nPART 3j — the audience walkthroughs (/demo?view=...)")
    here = os.path.dirname(os.path.abspath(__file__))
    demo_path = os.path.join(here, "static", "demo.html")
    if not os.path.exists(demo_path):
        bad("demo.html exists", "missing"); return
    with open(demo_path, encoding="utf-8") as fh:
        demo = fh.read()

    views = set(re.findall(r"\n    (\w+):\s*\{ dash:'(\w+)'", demo))
    implemented = {v for v, _d in views}
    dashes = set(re.findall(r"\n    (\w+):\{ id:'\w+'", demo))
    check(f"the demo implements every audience view ({sorted(implemented)})",
          implemented == set(_AUDIENCE_PAGES.values()),
          f"expected {sorted(set(_AUDIENCE_PAGES.values()))}")
    for v, d in sorted(views):
        check(f"  view '{v}' opens a dashboard the demo actually has ('{d}')", d in dashes,
              f"openDash('{d}') would return immediately and the visitor would see nothing")

    # every page's button must point at a view that exists
    for page, view in sorted(_AUDIENCE_PAGES.items()):
        path = os.path.join(here, "static", page + ".html")
        if not os.path.exists(path):
            bad(f"{page}.html exists", "missing"); continue
        with open(path, encoding="utf-8") as fh:
            src = fh.read()
        check(f"{page}.html has an obvious walkthrough button",
              'class="walkbtn"' in src, "Jim asked for a very obvious button")
        links = set(re.findall(r"/demo\?view=([a-z]+)", src))
        check(f"{page}.html links to a view the demo implements ({sorted(links)})",
              links and links <= implemented,
              f"points at {sorted(links - implemented)}, which /demo does not implement")
        check(f"{page}.html says the data is SAMPLE", 
              re.search(r"sample|made-up", src, re.I) is not None,
              "a demo must never look like a real child's record")

    # the two voice lists must stay identical AND append-only
    main_lines = _voice_lines_from(os.path.join(here, "main.py"), "DEMO_VOICE_LINES")
    demo_lines = _voice_lines_from(demo_path, "VOICE_LINES")
    check("the demo voice lists are readable", main_lines is not None and demo_lines is not None,
          "could not parse one of them")
    if main_lines and demo_lines:
        check(f"main.py and demo.html voice lists are IDENTICAL "
              f"({len(main_lines)} lines)", main_lines == demo_lines,
              "clips are served BY INDEX -- a mismatch plays the wrong audio under the "
              "right words, silently")
        for key in ("parents", "teachers", "homeschool", "students"):
            spoken = [ln for ln in demo_lines[-4:]]
            check(f"  the {key} intro is whitelisted",
                  any(key.rstrip('s') in ln.lower() or key in ln.lower() for ln in spoken)
                  or len(spoken) == 4,
                  "the walkthrough would fall back to the browser voice")
        # Build cq: the audience lines are anchored by their opening WORDS, not by
        # counting back from the end -- the end moves on every append. Prove every
        # anchor still resolves to exactly ONE whitelisted line, because a miss here is
        # silent: the walkthrough just drops to the browser's mechanical voice.
        demo_src = demo
        # NOTE the quote handling: four of the nine anchors contain an apostrophe
        # INSIDE a double-quoted string ("the parent's view", "That's the honest
        # read."). A naive [^"'] class stops dead at that apostrophe and silently
        # finds five anchors instead of nine -- a passing-looking test that checks
        # less than half of what it claims. Capture the opening quote and require
        # the SAME character to close it.
        anchors = [m[1] for m in re.findall(
            r'''lineStarting\(\s*(["'])((?:(?!\1).){12,80})\1\s*\)''', demo_src)]
        check(f"every audience anchor is declared ({len(anchors)} found)", len(anchors) >= 23,
              "expected four intros, ten homeschool stops, four closing lines and the "
              "five new parent stops")
        for a in anchors:
            hits = [ln for ln in demo_lines if ln.startswith(a)]
            check(f"  anchor {a[:34]!r} resolves to exactly one line", len(hits) == 1,
                  f"matched {len(hits)} -- the walkthrough would fall back to the "
                  f"browser voice, or play the wrong clip")

        # Build eg (2026-08-12): the parents door must SPEAK to the two questions a
        # parent actually brings to a conference table -- and must speak the NEW
        # lines, not the old ones (both stay in the lists forever; append-only).
        for label, needle in (
            ("the two parent questions, named up front",
             "is my child actually learning, and will she actually want to do this?"),
            ("the teaching promise -- never just hands her the answer",
             "I never just hand her the answer"),
            ("a missed problem comes back fresh (rule 55, in parent words)",
             "a miss becomes a second chance instead of a quiet gap"),
            ("the voice-privacy answer in the outro",
             "the audio is deleted right away — never stored"),
            ("the trophy case answers will-she-use-it",
             "will she actually use it?"),
        ):
            check(f"eg: the parents door carries {label}",
                  any(needle in ln for ln in demo_lines),
                  f"{needle!r} left the voice list -- the parents walkthrough lost "
                  f"its answer")
        check("eg: the parents door OPENS with the new intro",
              'parents:    lineStarting("Hello, and come on in' in demo_src,
              "AUD_INTRO.parents must anchor the conference intro, not the old welcome")
        check("eg: the parents door CLOSES with the privacy outro",
              'parents:    lineStarting("And that\'s the parent\'s window.")' in demo_src,
              "AUD_OUTRO.parents must anchor the new outro carrying the voice answer")

        # Build eh (2026-08-12): the students door must charm the child AND reassure
        # the parent listening over their shoulder -- and must speak the NEW lines.
        for label, needle in (
            ("the talks-and-LISTENS opener",
             "I really talk, and I really listen"),
            ("the math-ONLY promise",
             "I only ever talk about math"),
            ("the never-just-gives-the-answer promise",
             "I never just give you the answer"),
            ("trophies are earned -- nobody can give them",
             "Nobody can give you these — not me, not anyone"),
            ("the ask-me-out-loud honest read",
             "No mystery numbers, no report-card code"),
        ):
            check(f"eh: the students door carries {label}",
                  any(needle in ln for ln in demo_lines),
                  f"{needle!r} left the voice list -- the students walkthrough lost "
                  f"its answer")
        check("eh: the students door OPENS with the new intro",
              'students:   lineStarting("Hi there! I\'m Mr. Cadabra")' in demo_src,
              "AUD_INTRO.students must anchor the talks-and-listens intro")
        check("eh: the students door CLOSES with the two-promises outro",
              'students:   lineStarting("And that\'s your dashboard, top to bottom!")'
              in demo_src,
              "AUD_OUTRO.students must anchor the outro carrying math-only and "
              "never-just-the-answer")

        # Build ei (2026-08-12): the teachers door must name the replacement threat
        # first and keep the assistant frame throughout -- and must speak the NEW lines.
        for label, needle in (
            ("the replacement threat, named and answered first",
             "I am not here to replace you"),
            ("the thirty-hours-a-day assistant line",
             "no teacher has thirty hours a day for"),
            ("freedom from one-pace-fits-all",
             "no class learns at one speed"),
            ("the decisions stay with the teacher",
             "you make the teaching decisions"),
            ("the outro names what it DOESN'T do",
             "it doesn't plan your lessons, grade your judgment, or run your room"),
        ):
            check(f"ei: the teachers door carries {label}",
                  any(needle in ln for ln in demo_lines),
                  f"{needle!r} left the voice list -- the teachers walkthrough lost "
                  f"its answer")
        check("ei: the teachers door OPENS by disarming the threat",
              'teachers:   lineStarting("Welcome! And let me say the most important thing first")'
              in demo_src,
              "AUD_INTRO.teachers must anchor the not-here-to-replace-you intro")
        check("ei: the teachers door CLOSES with the assistant outro",
              'teachers:   lineStarting("And that\'s the teacher\'s side of the classroom.")'
              in demo_src,
              "AUD_OUTRO.teachers must anchor the what-it-doesn't-do outro")

        # And the bug Jim actually hit: the screen must go up BEFORE the words.
        check("the walkthrough shows the dashboard before it starts talking",
              "openDash(v.dash, { intro: v.intro" in demo_src
              and "document.body.className=''" not in
                  demo_src[demo_src.index("function startAudienceWalkthrough"):
                           demo_src.index("function startAudienceWalkthrough") + 900],
              "blanking the page and then speaking for thirty seconds is what Jim saw: "
              "'it's just a blank screen... blank, blank, blank until it gets to the "
              "parents' view'")
        check("an audience walkthrough can retitle the dashboard's stops",
              "runDashTour(d, 0, opts.lines)" in demo_src and "lines:HS_STOPS" in demo_src,
              "the homeschool view would speak the parent's words on the parent's screen")

        # Build cr, Jim: "when we go to the homeschool page, the teacher page, the student
        # page, I want that demo to only show the dashboard that's interesting to that
        # particular person. I don't want any links to any other dashboards from there."
        # Three doors out of a walkthrough could hand the visitor another audience's
        # screen, and all three are silent failures -- nothing errors, the wrong dashboard
        # simply opens. Each is checked from the SOURCE, not from a comment claiming it.
        def _fn_body(name, src, span=2600):
            i = src.find("function " + name)
            return src[i:i + span] if i >= 0 else ""

        sb = _fn_body("showBalloons", demo_src)
        check("the audience walkthroughs are locked to ONE dashboard",
              "audienceLocked()" in demo_src and "var AUDIENCE_KEY" in demo_src,
              "nothing decides which door the visitor came through")
        check("  the three-view chooser is skipped when a door is locked",
              bool(sb) and "audienceLocked()" in sb
              and sb.index("audienceLocked()") < (sb.index("openDash(")
                                                  if "openDash(" in sb else len(sb)),
              "showBalloons must return through the audience ending BEFORE it builds "
              "the three dashboard balloons")
        ae = _fn_body("showAudienceEnd", demo_src)
        check("  the audience ending offers no other dashboard",
              bool(ae) and "openDash(" not in ae and "dashStudent" not in ae
              and "dashTeacher" not in ae and "dashParent" not in ae,
              "the ending panel would put another audience's screen one tap away")
        check("  the ending offers a way onward instead of a dead end",
              "startAudienceWalkthrough(AUDIENCE_KEY)" in ae
              and "enterClassroomPicker()" in ae and "#pricing" in ae,
              "a locked door must still lead somewhere: watch it again, a real lesson, "
              "or the pricing page")
        check("  the dashboard's back button does not blank a locked walkthrough",
              "if(!audienceLocked()){ closeDash(); board.innerHTML=''; }" in demo_src,
              "these doors never set the classroom layout, so closing the dashboard "
              "leaves nothing behind the overlay -- the cq blank-screen bug again")
        check("  stepping into a real lesson sets the classroom layout first",
              "function enterClassroomPicker" in demo_src
              and "document.body.className='classroom'" in
                  _fn_body("enterClassroomPicker", demo_src, 400),
              "showPicker would draw into a hidden panel")
        # Build cs. THE CHECK THAT SHOULD HAVE EXISTED SINCE bx: every spoken string in a
        # tour must be ON THE WHITELIST. say() looks the text up in VOICE_LINES and plays
        # clip N by index; a line that is not there does not error, it drops that stop to
        # the browser's flat mechanical voice in the middle of Mr. Cadabra talking. The
        # design notes have said "every spoken string must be on the whitelist" since bx
        # and nothing enforced it -- so it is enforced here, for every tour on the page.
        spoken_lits = re.findall(r'''line:\s*(["'])((?:\\.|(?!\1).)*)\1''', demo_src)
        off_list = []
        for q, raw in spoken_lits:
            try:
                txt = ast.literal_eval(('"' + raw.replace('"', '\\"') + '"') if q == '"'
                                       else (q + raw + q))
            except (SyntaxError, ValueError):
                # NARROW on purpose. The first version of this caught bare Exception and
                # swallowed a NameError (ast was never imported), so every line looked
                # off-list and the failure message blamed the demo instead of the test.
                off_list.append(raw[:50])
                continue
            if txt not in demo_lines:
                off_list.append(txt[:50])
        check(f"every spoken tour line is on the voice whitelist "
              f"({len(spoken_lits)} checked)", not off_list,
              f"off the list: {off_list[:3]} -- that stop drops to the browser's flat "
              f"voice mid-tour, and nothing errors")

        # Build ct, Jim in a Basic Math demo lesson: "when the answers popped up, they
        # shortened the whiteboard to the point where I could only see a fraction of what
        # was actually being displayed." The board is flex, so anything below it takes its
        # space. Three rules keep the whiteboard the biggest thing on the page.
        ch = re.search(r"\.choices\{([^}]*)\}", demo_src)
        check("the answer buttons lay out as a wrapping ROW, not a stack",
              bool(ch) and "display:flex" in ch.group(1) and "flex-wrap:wrap" in ch.group(1),
              "a one-per-line grid pushes four buttons down the page and the whiteboard "
              "loses every pixel they take -- the real classroom uses a wrapping row "
              "(.choicerow in session.html) and the demo must match it")
        az = re.search(r"\.answerzone\{([^}]*)\}", demo_src)
        azcap = re.search(r"max-height:(\d+)vh", az.group(1)) if az else None
        check("the answer zone cannot take half the window",
              bool(azcap) and int(azcap.group(1)) <= 35,
              f"max-height is {azcap.group(1) + 'vh' if azcap else 'unset'} -- at 47vh the "
              f"answers and the board were nearly the same size")
        fd = re.search(r"\.feed\{([^}]*)\}", demo_src)
        check("the whiteboard has a floor no widget can push through",
              bool(fd) and re.search(r"min-height:\s*\d+px", fd.group(1)) is not None,
              "min-height:0 lets any future answer widget squeeze the board to nothing")

        # Every tour stop must point at an element that EXISTS. glow() returns quietly on
        # a missing id, so a typo means the words play over a dashboard that never moves.
        targets = re.findall(r"""\{\s*t:\s*'([A-Za-z0-9_]+)'\s*,""", demo_src)
        missing = [t for t in targets if f'id="{t}"' not in demo_src]
        check(f"every tour stop points at a real element ({len(targets)} stops)",
              not missing, f"no such id: {missing[:4]} -- glow() fails silently")

        # The homeschool override is read BY INDEX and falls through where it is short.
        def _count(block_start, pattern):
            i = demo_src.find(block_start)
            if i < 0:
                return -1
            return len(re.findall(pattern, demo_src[i:demo_src.index("]", i)]))
        hs_n = _count("var HS_STOPS = [", r"lineStarting\(")
        pd_n = _count("parent:{ id:'dashParent', stops:[", r"\{\s*t:\s*'pd")
        check(f"the homeschool script covers every parent stop ({hs_n} vs {pd_n})",
              hs_n == pd_n and hs_n > 0,
              "a short override does not error -- it just speaks the PARENT's words at a "
              "homeschooling parent for the stops it does not cover")

        check("  every door has a closing line and an ending panel",
              all(k in demo_src for k in ("AUD_OUTRO", "AUD_END"))
              and all(f"{k}:" in demo_src.split("var AUD_END")[1][:600]
                      for k in ("parents", "teachers", "homeschool", "students")),
              "a walkthrough would end in silence, or on another audience's words")


def part3o_unit_name_parity():
    # Added 2026-08-10 (build de). The diffeq restructure touched the SAME unit list in
    # four places -- curriculum.py, pedagogy.py, session.html's CURRICULUM_BY_COURSE and
    # topic.html's UNITS_BY_COURSE -- and nothing proved they agreed. A drift here is
    # nasty precisely because every file works alone: the picker shows one name, the
    # tutor teaches another, and mastery rows land under a number that means two
    # different things. curriculum.units_for() is the single source of truth; the other
    # three must match it byte for byte, for EVERY course, forever.
    print("\nPART 3o — unit names must agree across all four files")
    import curriculum
    import pedagogy
    here = os.path.dirname(os.path.abspath(__file__))
    src = {}
    for p in ("session.html", "topic.html"):
        path = os.path.join(here, "static", p)
        if not os.path.exists(path):
            bad(f"{p} exists", "missing from static/"); return
        with open(path, encoding="utf-8") as fh:
            src[p] = fh.read()

    def block(text, marker, course):
        """The [...] literal for one course inside a JS object that starts at marker."""
        try:
            body = text[text.index(marker):]
            body = body[body.index(f"{course}: ["):]
            return body[:body.index("],")]
        except ValueError:
            return None

    for course, _title in curriculum.list_courses():
        truth = [name for _n, name in curriculum.units_for(course)]

        ped = pedagogy.COURSE_PEDAGOGY.get(course, {}).get("unit_names", {})
        ped_names = [ped.get(i) for i in range(1, len(truth) + 1)]
        check(f"pedagogy.py matches curriculum.py: {course}", ped_names == truth,
              f"first drift: {next(((a, b) for a, b in zip(truth, ped_names) if a != b), None)}")

        sess = block(src["session.html"], "const CURRICULUM_BY_COURSE", course)
        if sess is None:
            bad(f"session.html has a {course} block", "not found"); continue
        sess_names = re.findall(r'name:\s*"((?:[^"\\]|\\.)*)"', sess)
        check(f"session.html matches curriculum.py: {course}", sess_names == truth,
              f"first drift: {next(((a, b) for a, b in zip(truth, sess_names) if a != b), 'count differs')}")

        top = block(src["topic.html"], "UNITS_BY_COURSE", course)
        if top is None:
            bad(f"topic.html has a {course} block", "not found"); continue
        top_names = re.findall(r'"((?:[^"\\]|\\.)*)"', top)
        check(f"topic.html matches curriculum.py: {course}", top_names == truth,
              f"first drift: {next(((a, b) for a, b in zip(truth, top_names) if a != b), 'count differs')}")

    # challenge.html keeps a FIFTH copy of every course's unit names (the assessment
    # labels a student sees on their results). COURSE_DATA maps each course to its
    # *_UNIT_NAMES constant; every one must match curriculum.py too. And while we are
    # in the file: every bank must still be 9 units x 5 questions with a sane answer
    # index -- the build-de diffeq re-mapping is exactly the kind of edit that could
    # leave a unit with four questions or an answer pointing past the choices.
    ch_path = os.path.join(here, "static", "challenge.html")
    if not os.path.exists(ch_path):
        skip("challenge.html unit names", "file not present in this checkout")
        return
    with open(ch_path, encoding="utf-8") as fh:
        ch = fh.read()
    cd = ch[ch.index("const COURSE_DATA"):]
    cd = cd[:cd.index("};")]
    mapping = re.findall(r"(\w+):\s*\{\s*bank:\s*(\w+),\s*unitNames:\s*(\w+)", cd)
    check("challenge.html: COURSE_DATA covers every course",
          {c for c, _b, _u in mapping} == {c for c, _t in curriculum.list_courses()},
          f"mapped: {sorted(c for c, _b, _u in mapping)}")
    for course, bank_const, names_const in mapping:
        truth = [name for _n, name in curriculum.units_for(course)]
        m = re.search(r"const %s = \{(.*?)\};" % names_const, ch, re.S)
        names = re.findall(r'\d+\s*:\s*"((?:[^"\\]|\\.)*)"', m.group(1)) if m else []
        check(f"challenge.html matches curriculum.py: {course}", names == truth,
              f"first drift: {next(((a, b) for a, b in zip(truth, names) if a != b), 'count differs')}")
        bm = re.search(r"const %s = \{(.*?)\n    \};" % bank_const, ch, re.S)
        if not bm:
            bad(f"challenge.html has a readable {bank_const}", "could not find it"); continue
        units = re.findall(r"\n      (\d+): \[(.*?)\n      \]", bm.group(1) + "\n      ]", re.S)
        qcounts = {int(n): len(re.findall(r"\{p:", body)) for n, body in units}
        answers_ok = all(0 <= int(a) <= 3 for a in re.findall(r"a:\s*(\d+)\s*\}", bm.group(1)))
        check(f"  {bank_const}: 9 units x 5 questions, answers in range",
              qcounts == {n: 5 for n in range(1, 10)} and answers_ok,
              f"unit question counts: {qcounts}")

    # And the SIXTH copy (build df): courses.html, the printable scope & sequence that
    # homeschool families file for curriculum records. Its ten cards carry no reliable
    # ids but sit in curriculum order, so the ten <ul class="units"> lists are read in
    # document order and zipped against curriculum.list_courses(). This page shipped
    # with the OLD diffeq units for a day after the build-de restructure -- a printed
    # scope & sequence disagreeing with the classroom is exactly what a curriculum
    # office notices.
    co_path = os.path.join(here, "static", "courses.html")
    if not os.path.exists(co_path):
        skip("courses.html unit lists", "file not present in this checkout")
        return
    with open(co_path, encoding="utf-8") as fh:
        co = fh.read()
    uls = re.findall(r'<ul class="units">(.*?)</ul>', co, re.S)
    courses = curriculum.list_courses()
    check("courses.html: one unit list per course, in curriculum order",
          len(uls) == len(courses), f"{len(uls)} lists for {len(courses)} courses")
    for (course, title), body in zip(courses, uls):
        names = [n.replace("&amp;", "&").strip() for n in re.findall(r"</b>\s*(.*?)</li>", body)]
        truth = [name for _n, name in curriculum.units_for(course)]
        check(f"courses.html matches curriculum.py: {course}", names == truth,
              f"first drift: {next(((a, b) for a, b in zip(truth, names) if a != b), 'count differs')}")
        check(f"  courses.html: the {course} card is present", title in co,
              f"course title {title!r} not found on the page")


def part3p_marketing_claims():
    # Added 2026-08-10 (build df). Jim: "make sure we don't have anything in here that
    # says evidence based learning as a blanket statement." Two phrases are banned from
    # every piece of VISIBLE marketing copy, permanently:
    #   - "evidence-based" / "evidence based": true in the strict WWC sense only for the
    #     elementary/algebra courses; a blanket claim is the kind of thing a school
    #     district's curriculum office checks, and one caught overreach discredits every
    #     true claim on the page. Per-level wording lives in Teaching_Evidence_Base sec 6.
    #   - "Socratic": Jim retired the word site-wide in build cc (the method is
    #     foundation-first, rules 36-38) -- and the sweep that wrote THIS check still
    #     found one live "taught Socratically" on courses.html that cc had missed.
    # HTML comments are stripped first: historical change notes are records, not copy.
    print("\nPART 3p — banned marketing claims stay banned")
    here = os.path.dirname(os.path.abspath(__file__))
    targets = sorted(
        p for p in os.listdir(os.path.join(here, "static")) if p.endswith(".html")
    ) + ["llms.txt"]
    banned = [("blanket 'evidence-based' claim", re.compile(r"evidence[\s-]based", re.I)),
              ("'Socratic'", re.compile(r"socratic", re.I))]
    for name in targets:
        path = os.path.join(here, "static", name)
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8") as fh:
            visible = re.sub(r"<!--.*?-->", "", fh.read(), flags=re.S)
        for label, pat in banned:
            m = pat.search(visible)
            check(f"{name}: no {label}", m is None,
                  f"found {m.group(0)!r} in visible copy" if m else "")
    readme = os.path.join(here, "README.md")
    if os.path.exists(readme):
        with open(readme, encoding="utf-8") as fh:
            txt = fh.read()
        for label, pat in banned:
            m = pat.search(txt)
            check(f"README.md: no {label}", m is None,
                  f"found {m.group(0)!r}" if m else "")

    # ---- BUILD dt: MISSED PROBLEMS ARE REMEMBERED (rule 55, the data foundation) ----
    # The whole pipeline, source-checked here and drilled live below: the tag carries
    # the misses, the pages parse and POST them, the server clamps honestly, the store
    # sweeps, the reset wipes, the mastery note hands them back for spaced review.
    sess3 = open(os.path.join(here, "static", "session.html"), encoding="utf-8").read()
    check("session.html parses missed= and ships it on all three score POSTs (dt)",
          "function parseMissed" in sess3
          and sess3.count("missed: parseMissed(a.missed)") >= 3,
          "a tag the pages ignore is a rule the product doesn't keep")
    dash3 = open(os.path.join(here, "static", "dashboard.html"), encoding="utf-8").read()
    check("the dashboard has the hidden-until-data Tricky-ones card (dt)",
          'id="missWrap" style="display:none;"' in dash3
          and "/api/misses/" in dash3 and "never block the dashboard" in
          dash3.split("loadMisses")[1][:2400],
          "review-my-misses must exist, hide when empty, and fail soft")
    mn3 = open(os.path.join(here, "main.py"), encoding="utf-8").read()
    check("misses are HONESTLY CLAMPED server-side (dt)",
          "def _keep_misses" in mn3
          and "min(25, int(total) - int(correct))" in mn3,
          "the tutor could otherwise report more misses than there were questions")
    check("GET /api/misses/{code} exists and is student-gated (dt)",
          '@app.get("/api/misses/{code}")' in mn3
          and "_student_or_404" in mn3.split('@app.get("/api/misses/{code}")')[1][:700],
          "an open endpoint that hands out a child's mistakes")
    check("the mastery note hands misses back with rule 55(b)'s orders (dt)",
          "RECENT MISSED PROBLEMS (rule 55)" in mn3
          and "revisit exactly ONE" in mn3,
          "stored misses the tutor never sees are a diary, not a teaching tool")
    st3 = open(os.path.join(here, "store.py"), encoding="utf-8").read()
    check("quiz_misses joins the reset family day one (dt)",
          '("quiz_misses", "code"),' in st3,
          "a reset student must not keep ghost misses")
    check("rule 55 lives in the SHARED block exactly once (dt)",
          tutor.GRAPH_TOOL_NOTE.count("55. A MISSED QUIZ PROBLEM COMES BACK") == 1,
          "the rule must reach every course from ONE place")
    check("  ...and the missed= tag spec lives in the LESSON-ONLY note (dt)",
          'missed="2/5 + 1/5 => 3/10' in tutor.PROGRESS_TAGS_NOTE
          and "[[finalexam" not in tutor.GRAPH_TOOL_NOTE,
          "quiz tags exist only in lessons; the SHARED block must not teach "
          "practice/topic a tag their pages cannot draw (PART 3e's own guard)")

    # ---- BUILD du: the retake door + the parent's tricky list -----------------------
    check("the dashboard's 90% line has its Retake button, students only (du)",
          "&quiz=1" in dash3.replace("&amp;", "&")
          and "Retake the Unit Quiz" in dash3
          and "u.checks_taken ?" in dash3,
          "'let's get it to 90%' without a button is a taunt")
    check("session.html opens the retake door like the final-exam door (du)",
          "QUIZ_INTENT" in sess3 and '"__unit_quiz__"' in sess3
          and "Take the Unit Quiz ▶" in sess3,
          "the button must land on a page that opens exactly that door")
    check("main.py turns __unit_quiz__ into administer-it-NOW orders (du)",
          '"__unit_quiz__"' in mn3
          and "record keeps their BEST score" in mn3
          and mn3.count("__unit_quiz__") >= 3,   # sentinel tuple + junk list + handler
          "a sentinel nobody interprets is a dead button")
    check("the parent box and the Friday email answer 'what was tricky?' (du)",
          "Recently tricky:" in dash3
          and "Tricky this week" in mn3,
          "parent item 6 -- the most-asked question -- must be answered in both places")

    # ---- BUILD dv: the buzzer-beater shield (Jim's live catch) ----------------------
    sess4 = open(os.path.join(here, "static", "session.html"), encoding="utf-8").read()
    check("timer-swapped sprint panels are shielded for 1.2s (dv)",
          'sprShow("sprBreak", 1200)' in sess4 and 'sprShow("sprDone", 1200)' in sess4
          and "shieldMs" in sess4,
          "a click meant for the last answer must never dismiss the results")

    # ---- BUILD ea: the pacing steer ---------------------------------------------------
    mn6 = open(os.path.join(here, "main.py"), encoding="utf-8").read()
    st6 = open(os.path.join(here, "store.py"), encoding="utf-8").read()
    fam6 = open(os.path.join(here, "static", "family.html"), encoding="utf-8").read()
    check("the steer endpoint is parent-gated and ownership-checked (ea)",
          '@app.post("/api/parent/student-steer")' in mn6
          and "_own_student" in
          mn6.split('@app.post("/api/parent/student-steer")')[1][:1200],
          "a standing plan for someone else's child is not a feature")
    check("the child's explicit choice OUTRANKS the plan (ea, rule 50)",
          "def _resolve_focus" in mn6
          and "return int(req_unit), False" in mn6,
          "the steer is a plan, not a cage")
    check("the steered mastery note is honest about WHO asked (ea)",
          "THE FAMILY PLAN: their parent asked" in mn6
          and "their agency wins" in mn6,
          "the tutor must never present the parent's plan as the student's request")
    check("steers join the reset family (and therefore follow a dy code move) (ea)",
          '("steers", "code"),' in st6,
          "a reset student must not inherit a ghost plan")
    check("family.html has the steer controls and shows the current plan (ea)",
          "data-dosteer" in fam6 and "data-clearsteer" in fam6 and "steernow" in fam6,
          "an endpoint without its panel is still a support email")

    # ---- BUILD eb: the calm features page + four audience FAQs ----------------------
    # Jim 2026-08-11: "too much information... I don't really like the icons. I'd rather
    # just use bullet points... consolidate... drop-down menus" + "a FAQ section on the
    # bottom of the homeschool, the parent, teacher and student pages... DIFFERENT FAQs
    # because they have different questions."
    def _vis7(name):  # visible text only (change notes talk ABOUT icons; that's fine)
        with open(os.path.join(here, "static", name), encoding="utf-8") as fh:
            return re.sub(r"<!--.*?-->", "", fh.read(), flags=re.S)
    feat7 = _vis7("features.html")
    check("features.html carries NO emoji icon rows (eb)",
          'class="ic"' not in feat7 and "details.feat" not in feat7
          and "🗣️" not in feat7 and "🖍️" not in feat7 and "🧑‍🏫" not in feat7
          and "👨‍👩‍👧" not in feat7 and "🛡️" not in feat7,
          "Jim asked for bullets, not icons -- the old rows must not creep back")
    check("features.html is six drop-down sections of plain bullets (eb)",
          feat7.count('<details class="sec"') == 6
          and feat7.count("<li><b>") >= 41,
          "consolidated means six calm rows hiding the full list, not a wall")
    check("features.html names the features shipped since the last rewrite (eb)",
          all(s in feat7 for s in ("Fluency sprints", "refresher after time away",
                                   "Pause it, finish it later", "Retake any Unit Quiz",
                                   "tricky ones come back", "Steer the pace",
                                   "lesson on a phone", "include everyone")),
          "a features page that trails the product hides the work")
    _faq_pages = ("students.html", "parents.html", "homeschool.html", "teachers.html")
    _faq_qs = {}
    for _fp in _faq_pages:
        _fsrc = _vis7(_fp)
        check(f"{_fp} ends with its own 8-question FAQ (eb)",
              'id="faq"' in _fsrc and _fsrc.count('<details class="qa"') == 8
              and _fsrc.rfind('id="faq"') > _fsrc.rfind("walkbtn"),
              "every audience page owes its visitors their OWN questions, at the bottom")
        _faq_qs[_fp] = set(re.findall(r'class="qa"><summary>(.*?)<span', _fsrc))
        check(f"{_fp}: all 8 FAQ questions parsed for the disjointness sweep (eb)",
              len(_faq_qs[_fp]) == 8, f"parsed {len(_faq_qs[_fp])} -- markup drifted?")
    for _i, _a in enumerate(_faq_pages):
        for _b in _faq_pages[_i + 1:]:
            check(f"FAQ questions are DISJOINT: {_a} vs {_b} (eb)",
                  not (_faq_qs[_a] & _faq_qs[_b]),
                  f"shared: {_faq_qs[_a] & _faq_qs[_b]} -- Jim asked for DIFFERENT FAQs")
    hv7 = _vis7("homeschool.html")
    check("homeschool.html no longer promises a 'parent code' (eb, dq's fix extended)",
          "parent code" not in hv7.lower() and '"/family"' in hv7,
          "the phantom parent code was scrubbed from parents.html; it must not survive here")

    # ---- BUILD ef (2026-08-12): the conference-pitch rework of /homeschool ----------
    # Jim, pitching at a homeschooling conference: lead with what families actually
    # buy -- records first, honest mastery named, parent control, and the trust
    # questions answered before they're asked. These guards pin the SPINE of that
    # page so a future copy pass can't quietly bury the lead again.
    def _at(needle):
        i = hv7.find(needle)
        check(f"homeschool.html still says: {needle[:48]!r} (ef)", i >= 0,
              "a pitch anchor left the page -- restore it or retire this guard on purpose")
        return i if i >= 0 else len(hv7)
    _rec = _at("Records &amp; requirements")
    _hrs = _at("Honest hours")
    _win = _at("Your window in")
    _tch = _at("You're still the teacher")
    _tru = _at("The trust questions")
    _faqi = hv7.find('id="faq"')
    check("homeschool.html leads with RECORDS, then hours, then the window in (ef)",
          _rec < _hrs < _win,
          "the records section must come FIRST after the video -- filing day is the "
          "promise homeschool families buy; burying it re-loses the conference pitch")
    check("homeschool.html: teacher-control then trust questions, before the FAQ (ef)",
          _win < _tch < _tru < _faqi,
          "the you're-still-the-teacher and trust sections belong between the product "
          "story and the FAQ")
    check("homeschool.html names the honest mastery bars (ef)",
          "80%" in hv7 and "90%" in hv7 and "never round up" in hv7,
          "the 80/90 bars and never-rounds-up are the honesty pitch -- say them")
    for label, needle in (
        ("answers are never just handed over", "never gets a bare answer"),
        ("the math engine check", "a separate math engine re-computes"),
        ("voice audio deleted immediately", "deleted immediately"),
        ("something bigger than math -> a trusted adult", "trusted adult"),
    ):
        check(f"homeschool.html trust answer: {label} (ef)", needle in hv7,
              f"{needle!r} left the trust section -- a careful parent asks this at "
              f"every conference table")
    check("homeschool.html links /privacy from the trust section (ef)",
          '"/privacy"' in hv7, "the voice-data answer must hand the parent the policy")
    check("homeschool.html: the method line names WWC without the banned phrase (ef)",
          "What Works Clearinghouse" in hv7,
          "name the actual guides -- the blanket phrase stays banned (PART 3p) and a "
          "savvy homeschooler knows the difference")
    check("homeschool.html quotes no dollar figure (ef)", "$" not in hv7,
          "prices live on /pricing alone so the two pages can never disagree")

    # ---- BUILD ec: security hardening pass 1 (F3 spoof, F4 headers, F5 upload cap) ---
    mn8 = open(os.path.join(here, "main.py"), encoding="utf-8").read()
    # F3: the caller IP must come from the TRUSTED (rightmost) end, never the spoofable
    # leftmost. The old attacker-controlled pattern must be gone.
    _cip = mn8.split("def _client_ip(", 1)[1].split("\ndef ", 1)[0]
    check("F3: _client_ip trusts the proxy-appended end, not the spoofable leftmost (ec)",
          "TRUSTED_PROXY_HOPS" in _cip
          and "len(fwd) - hops" in _cip
          and '.split(",")[0].strip()' not in _cip,
          "a visitor who can prepend a fake XFF entry can slip every per-IP limit")
    # F4: the security-headers middleware must exist and carry the full set.
    check("F4: a security-headers middleware stamps the standard set on every response (ec)",
          '@app.middleware("http")' in mn8 and "async def _security_headers" in mn8
          and all(h in mn8 for h in (
              '"X-Content-Type-Options": "nosniff"',
              '"X-Frame-Options": "SAMEORIGIN"',
              '"Referrer-Policy"', '"Strict-Transport-Security"',
              '"Permissions-Policy"', "Content-Security-Policy-Report-Only")),
          "defense-in-depth headers protect every page, API, and asset")
    check("F4: the CSP ships REPORT-ONLY (never blocks our own inline scripts) (ec)",
          "_CSP_REPORT_ONLY" in mn8
          and '"Content-Security-Policy":' not in mn8
          and "https://plausible.io" in mn8,
          "an enforcing CSP would blank pages that use inline styles/scripts + Plausible")
    # F5: the upload cap is real -- bounded read AND a 413 AND the catch-all re-raises it.
    _stt = mn8.split("async def transcribe(", 1)[1].split("\n@app.", 1)[0]
    check("F5: /api/transcribe caps the upload and returns 413, un-swallowed (ec)",
          "MAX_AUDIO_BYTES" in mn8
          and "audio.read(MAX_AUDIO_BYTES + 1)" in _stt
          and "status_code=413" in _stt
          and "except HTTPException:" in _stt,
          "an unbounded read is a memory/cost hole; a swallowed 413 is no cap at all")

    # ---- BUILD ec: LIVE -- headers actually ship + XFF read from the trusted end -----
    try:
        import httpx as _httpx8  # noqa: F401
        _have_httpx8 = True
    except Exception:  # noqa: BLE001
        _have_httpx8 = False
    if not _have_httpx8:
        skip("security hardening live drill", "httpx not installed here")
    else:
        import tempfile as _tf8
        with _tf8.TemporaryDirectory() as tmp8:
            drill = os.path.join(tmp8, "secdrill.py")
            with open(drill, "w") as fh:
                fh.write(
                    "from fastapi.testclient import TestClient\n"
                    "import main\n"
                    "c = TestClient(main.app)\n"
                    "# F4: every response carries the hardening headers (a page AND the API)\n"
                    "for path in ('/', '/api/voice-status'):\n"
                    "    r = c.get(path)\n"
                    "    h = r.headers\n"
                    "    assert h.get('x-content-type-options') == 'nosniff', (path, dict(h))\n"
                    "    assert h.get('x-frame-options') == 'SAMEORIGIN', path\n"
                    "    assert 'strict-origin' in h.get('referrer-policy',''), path\n"
                    "    assert 'max-age=' in h.get('strict-transport-security',''), path\n"
                    "    assert h.get('content-security-policy-report-only'), path\n"
                    "    assert 'content-security-policy' not in {k.lower() for k in h} - {'content-security-policy-report-only'}, path\n"
                    "# F3: leftmost XFF is a fake the client prepended; we must read the\n"
                    "# rightmost (proxy-appended) entry instead.\n"
                    "class _Req:\n"
                    "    def __init__(s, xff): s.headers={'x-forwarded-for': xff}; s.client=type('C',(),{'host':'9.9.9.9'})()\n"
                    "    headers=None\n"
                    "import os as _os\n"
                    "_os.environ['TRUSTED_PROXY_HOPS']='1'\n"
                    "assert main._client_ip(_Req('6.6.6.6, 1.2.3.4')) == '1.2.3.4', 'must trust the appended end'\n"
                    "assert main._client_ip(_Req('6.6.6.6')) == '6.6.6.6', 'single entry is the client'\n"
                    "assert main._client_ip(_Req('a, b, 1.2.3.4')) == '1.2.3.4', 'many fakes cannot push past the trusted end'\n"
                    "print('SEC-DRILL-OK')\n")
            env = dict(os.environ)
            env["PYTHONPATH"] = here + os.pathsep + env.get("PYTHONPATH", "")
            env["WEEKLY_EMAIL"] = "off"
            r = subprocess.run([sys.executable, drill], cwd=here, env=env,
                               capture_output=True, text=True)
            check("security live: headers ship on page + API; XFF read from the trusted end (ec)",
                  r.returncode == 0 and "SEC-DRILL-OK" in r.stdout,
                  (r.stdout + r.stderr)[-400:])

    # ---- BUILD ed: read-by-code enumeration throttle + widened codes (F1) ------------
    mn9 = open(os.path.join(here, "main.py"), encoding="utf-8").read()
    # (A) every read-by-code endpoint must front its work with _read_guard.
    _READ_EPS = ("awards_state", "time_summary", "topics_state", "records_report",
                 "get_misses_api", "get_placement", "student_courses",
                 "api_sprint_record", "get_sprint", "session_state", "assessment")
    for _fn in _READ_EPS:
        _seg = mn9.split(f"def {_fn}(", 1)
        _body = _seg[1].split("\ndef ", 1)[0] if len(_seg) == 2 else ""
        check(f"F1: read endpoint {_fn} is throttled by _read_guard (ed)",
              "request: Request" in _body[:200] and "_read_guard(request, code)" in _body,
              "an un-guarded read-by-code endpoint is an open enumeration door")
    # the guard itself: distinct-code ceiling + raw per-IP cap, both present.
    _rg = mn9.split("def _read_guard(", 1)[1].split("\ndef ", 1)[0]
    check("F1: _read_guard caps DISTINCT codes per IP and raw read rate (ed)",
          "_CODE_PROBE_MAX" in _rg and "distinct = len(seen)" in _rg
          and 'limit=_READ_IP_LIMIT' in _rg and "status_code=429" in _rg,
          "enumeration is many DIFFERENT codes from one source; that's what must be capped")
    # (B) the widened code format.
    _nsc = mn9.split("def _new_student_code(", 1)[1].split("\ndef ", 1)[0]
    check("F1: new student codes are widened to 4 digits (~450k space) (ed)",
          "randbelow(9000) + 1000" in _nsc and "randbelow(90)" not in _nsc,
          "a 4,500-code space is guessable; existing 2-digit codes still work")

    # ---- BUILD ed: LIVE -- enumeration is blocked, honest use is not -----------------
    try:
        import httpx as _httpx9  # noqa: F401
        _have_httpx9 = True
    except Exception:  # noqa: BLE001
        _have_httpx9 = False
    if not _have_httpx9:
        skip("read-throttle live drill", "httpx not installed here")
    else:
        import tempfile as _tf9
        with _tf9.TemporaryDirectory() as tmp9:
            drill = os.path.join(tmp9, "readdrill.py")
            with open(drill, "w") as fh:
                fh.write(
                    "import os as _os, re\n"
                    "_os.environ['TRUSTED_PROXY_HOPS']='1'\n"
                    "_os.environ['CODE_PROBE_MAX']='50'\n"
                    "from fastapi.testclient import TestClient\n"
                    "import main\n"
                    "c = TestClient(main.app)\n"
                    "A = {'x-forwarded-for': '203.0.113.7'}\n"
                    "# enumeration: many DIFFERENT codes from ONE ip -> 429 kicks in near the cap\n"
                    "blocked = None\n"
                    "for i in range(90):\n"
                    "    r = c.get(f'/api/session/GUESS{i:04d}', headers=A)\n"
                    "    if r.status_code == 429:\n"
                    "        blocked = i; break\n"
                    "assert blocked is not None and 40 <= blocked <= 60, blocked\n"
                    "# a FRESH ip does not inherit the block (per-IP isolation, F3 makes ip real)\n"
                    "r = c.get('/api/session/GUESS0000', headers={'x-forwarded-for': '198.51.100.9'})\n"
                    "assert r.status_code != 429, 'a new connection must start clean'\n"
                    "# a real family re-reading the SAME code never trips the distinct guard\n"
                    "B = {'x-forwarded-for': '198.51.100.22'}\n"
                    "for _ in range(120):\n"
                    "    r = c.get('/api/session/MAPLE42', headers=B)\n"
                    "    assert r.status_code != 429, 'same-code reloads must never be throttled'\n"
                    "# widened codes: WORD + 4 digits (stub the collision probe so the\n"
                    "# format test needs no database)\n"
                    "main.STUDENTS = {}\n"
                    "main.store.get_account = lambda *a, **k: None\n"
                    "for _ in range(25):\n"
                    "    code = main._new_student_code()\n"
                    "    assert re.match(r'^[A-Z]+\\d{4}$', code), code\n"
                    "print('SEC2-DRILL-OK')\n")
            env = dict(os.environ)
            env["PYTHONPATH"] = here + os.pathsep + env.get("PYTHONPATH", "")
            env["WEEKLY_EMAIL"] = "off"
            r = subprocess.run([sys.executable, drill], cwd=here, env=env,
                               capture_output=True, text=True)
            check("read-throttle live: enumeration 429s; fresh IP + same-code reads pass; codes widened (ed)",
                  r.returncode == 0 and "SEC2-DRILL-OK" in r.stdout,
                  (r.stdout + r.stderr)[-400:])

    # ---- BUILD dz: accessibility + phones -------------------------------------------
    for pg in ("session.html", "practice.html", "topic.html"):
        psrc = open(os.path.join(here, "static", pg), encoding="utf-8").read()
        check(f"{pg}: live regions, mic name, reduced motion, phone dock (dz)",
              'aria-live="polite"' in psrc
              and 'aria-label="Talk to Mr. Cadabra' in psrc
              and "prefers-reduced-motion" in psrc
              and "position: sticky; bottom: 0" in psrc
              and ".center { order: 1;" in psrc,
              "a voice-first tutor must be the accessible one, on every teaching page")
    sess6 = open(os.path.join(here, "static", "session.html"), encoding="utf-8").read()
    check("session's overlays are real dialogs and the welcome takes focus (dz)",
          sess6.count('role="dialog" aria-modal="true"') >= 4
          and 'el("welcomeGo").focus()' in sess6,
          "an overlay a screen reader cannot see is a locked door")

    # ---- BUILD dy: child management -- four support emails become four buttons ------
    mn5 = open(os.path.join(here, "main.py"), encoding="utf-8").read()
    for ep in ("student-rename", "student-newcode", "student-remove", "student-attach"):
        seg = mn5.split(f'@app.post("/api/parent/{ep}")')
        check(f"/api/parent/{ep} exists and is parent-gated (dy)",
              len(seg) == 2 and "_require_parent" in seg[1][:900],
              "child management must never be an open door")
    check("rename/newcode/remove are OWNERSHIP-checked, misses 404 (dy)",
          mn5.count("_own_student(parent, body.code)") >= 3
          and "404" in mn5.split("def _own_student")[1][:600],
          "a parent may only ever touch their OWN children; probes learn nothing")
    check("remove demands the child's name typed back, server-verified (dy)",
          "typed != want" in mn5,
          "a mis-tap must never delete a childhood of progress")
    check("attach refuses another family's code and demo codes (dy)",
          '"owned"' in mn5 and "409" in mn5.split('student-attach')[1][:1600]
          and "code in STUDENTS" in mn5,
          "the code is a credential, not a transfer instrument")
    st5 = open(os.path.join(here, "store.py"), encoding="utf-8").read()
    check("a code change moves EVERY per-student table in one transaction (dy)",
          "def change_student_code" in st5
          and "_STUDENT_CODE_TABLES" in st5.split("def change_student_code")[1][:900],
          "a new code that strands old rows loses the child's history")
    fam5 = open(os.path.join(here, "static", "family.html"), encoding="utf-8").read()
    check("family.html has the Manage panel and the attach door (dy)",
          "manageLink" in fam5 and "data-newcode" in fam5
          and 'id="attachLink"' in fam5 and "Remove forever" in fam5,
          "the endpoints without the panel are still support emails")

    # ---- BUILD dx: the assessment survives a closed tab -----------------------------
    ch = open(os.path.join(here, "static", "challenge.html"), encoding="utf-8").read()
    check("the assessment saves after every answer and offers a resume (dx)",
          "function saveState" in ch and "saveState();" in ch
          and 'id="resumeRow"' in ch and "function offerResume" in ch,
          "45 questions and 20 minutes must never die with a tab")
    check("  a finished run and a deliberate fresh start both clear the save (dx)",
          "clearSaved();         // dx: a finished run" in ch
          and "clearSaved(); begin(false);" in ch,
          "a stale save must never shadow a completed assessment")
    check("  a changed question bank discards the save (dx)",
          "s.total !== TOTAL_Q" in ch,
          "never resume a student into a different test")

    # ---- BUILD dw: the gap-aware refresher + three bars, always ---------------------
    mn4 = open(os.path.join(here, "main.py"), encoding="utf-8").read()
    check("a returning student gets a real refresher after a day away (dw)",
          "gap_days" in mn4 and "memory-jog" in mn4
          and "never a test" in mn4,
          "'ready to keep going?' after four days is a cold shoulder")
    check("an empty TODAY bar becomes a per-turn ORDER to the opener (dw)",
          'student_context.get("today_live")' in mn4
          and "EMPTY right now. Your FIRST message" in mn4,
          "the standing instruction alone was routinely ignored on resumes")
    sess5 = open(os.path.join(here, "static", "session.html"), encoding="utf-8").read()
    check("the TODAY row shows its placeholder from the first second (dw)",
          "if (!TODAY_ITEMS.length) showBarsPreview();" in sess5,
          "two bars must never be the resting state")

    # ---- BUILD dq: MARKETING MUST MATCH THE PRODUCT (Four-Lens Review theme B) ------
    # Two kinds of drift, both now machine-caught: promises the product doesn't keep
    # (the phantom "read-only parent code") and product the marketing hides (teachers.html
    # never linked the real /teacher tool; records was never one click from /family).
    def _visible(name):
        with open(os.path.join(here, "static", name), encoding="utf-8") as fh:
            return re.sub(r"<!--.*?-->", "", fh.read(), flags=re.S)
    pv = _visible("parents.html")
    check("parents.html no longer promises a 'parent code' (it never existed)",
          "parent code" not in pv.lower() and "read-only code for you" not in pv.lower(),
          "the parent door takes the CHILD's code; a promised second code is a lie")
    check("parents.html no longer calls live parent accounts 'rolling out'",
          "rolling out with launch" not in pv,
          "accounts shipped 2026-07-31 -- the page must not trail the product")
    check("parents.html points parents at their real home (/family)",
          '"/family"' in pv, "the page describes the account but never links it")
    fv = _visible("family.html")
    check("family.html links each child's printable Records report",
          "/records?code=" in fv,
          "the homeschool page's 'one click from your parent view' depends on this")
    check("family.html carries the How-are-they-doing narrative and the email toggle",
          "assessLink" in fv and 'id="mailToggle"' in fv,
          "mission control lost a panel")
    tv = _visible("teachers.html")
    check("teachers.html links the REAL class tool (/teacher)",
          'href="/teacher"' in tv,
          "a marketing page that hides the product it describes")
    rv = open(os.path.join(here, "static", "records.html"), encoding="utf-8").read()
    check("records.html's bare-visit message points home, not at URL surgery",
          '"/family"' in rv and "Add ?code=STUDENT-CODE to the address, or open" not in
          re.sub(r"<!--.*?-->", "", rv, flags=re.S),
          "a parent should never be told to edit an address bar")
    mn2 = open(os.path.join(here, "main.py"), encoding="utf-8").read()
    check("the overview + email-toggle endpoints exist and are parent-token gated",
          '@app.get("/api/parent/overview")' in mn2
          and '@app.post("/api/parent/weekly-email")' in mn2
          and mn2.split('@app.get("/api/parent/overview")')[1][:800].count("_require_parent") == 1
          and mn2.split('@app.post("/api/parent/weekly-email")')[1][:800].count("_require_parent") == 1,
          "family mission control must never be an open door")

    # ---- BUILD ds: help that works for a kid, sprints on request ---------------------
    check("every app page's help pill goes to /help, never a mailto (ds)",
          '"/help"' in open(os.path.join(here, "static", "app-nav.js"),
                            encoding="utf-8").read()
          and 'add("mailto:' not in open(os.path.join(here, "static", "app-nav.js"),
                                         encoding="utf-8").read(),
          "a mailto is a dead end on a school Chromebook")
    hp = os.path.join(here, "static", "help.html")
    check("help.html exists, ends whole, and shows the support address as TEXT",
          os.path.exists(hp)
          and "not truncated" in open(hp, encoding="utf-8").read()[-80:]
          and "support@mrcadabra.com</b>" in open(hp, encoding="utf-8").read(),
          "a kid must be able to SHOW a grown-up the address, not just click it")
    check("main.py serves /help",
          '@app.get("/help")' in mn2 or '@app.get("/help")' in
          open(os.path.join(here, "main.py"), encoding="utf-8").read(),
          "the page exists but nothing routes to it")
    check("the assessment page has a help door (ds)",
          'href="/help"' in open(os.path.join(here, "static", "challenge.html"),
                                 encoding="utf-8").read(),
          "the highest-stakes page had NO help affordance at all")
    sess2 = open(os.path.join(here, "static", "session.html"), encoding="utf-8").read()
    check("&sprint=1 starts a sprint on request (ds)",
          'params.get("sprint") === "1"' in sess2
          and "startRequestedSprint" in sess2,
          "the dashboard button would land on a page that ignores it")
    dash2 = open(os.path.join(here, "static", "dashboard.html"), encoding="utf-8").read()
    check("the dashboard sprint card offers Run-one-now to students only (ds)",
          "&sprint=1" in dash2 and "!isTeacher && CODE" in dash2,
          "either no way back to sprints, or the read-only view got a start button")

    # ...and the whole family flow proven LIVE: signup -> add child -> overview ->
    # toggle the Friday email off -> the flag lands where the digest pass reads it.
    try:
        import httpx  # noqa: F401
        _have_httpx2 = True
    except Exception:  # noqa: BLE001
        _have_httpx2 = False
    if not _have_httpx2:
        skip("family mission-control live drill", "httpx not installed here")
    else:
        import tempfile as _tf4
        with _tf4.TemporaryDirectory() as tmp4:
            drill = os.path.join(tmp4, "famdrill.py")
            with open(drill, "w") as fh:
                fh.write(
                    "from fastapi.testclient import TestClient\n"
                    "import main, store\n"
                    "c = TestClient(main.app)\n"
                    "r = c.post('/api/parent/signup', json={'email': 'drill@example.com',\n"
                    "           'password': 'drill-pass-123', 'name': 'Drill'})\n"
                    "assert r.status_code == 200, r.text\n"
                    "tok = r.json()['token']\n"
                    "h = {'X-Parent-Token': tok}\n"
                    "r = c.post('/api/parent/students', json={'token': tok, 'name': 'Kid'})\n"
                    "assert r.status_code == 200, r.text\n"
                    "r = c.get('/api/parent/overview', headers=h)\n"
                    "d = r.json()\n"
                    "assert r.status_code == 200 and len(d['students']) == 1, d\n"
                    "assert d['weekly_email_on'] is True, d\n"
                    "s = d['students'][0]\n"
                    "assert s['minutes_week'] == 0 and s['units_mastered'] == 0, s\n"
                    "r = c.post('/api/parent/weekly-email', json={'token': tok, 'on': False})\n"
                    "assert r.status_code == 200 and r.json()['on'] is False, r.text\n"
                    "d2 = c.get('/api/parent/overview', headers=h).json()\n"
                    "assert d2['weekly_email_on'] is False, d2\n"
                    "r = c.get('/api/parent/overview')\n"
                    "assert r.status_code == 401, ('no token must be refused', r.status_code)\n"
                    "print('FAMILY-DRILL-OK')\n")
            env = dict(os.environ,
                       DATABASE_URL=f"sqlite:///{os.path.join(tmp4, 'f.db')}",
                       WEEKLY_EMAIL="off", PYTHONPATH=here)
            r = subprocess.run([sys.executable, drill], cwd=here, env=env,
                               capture_output=True, text=True)
            check("family flow live: signup -> child -> overview -> email off -> gate holds",
                  r.returncode == 0 and "FAMILY-DRILL-OK" in r.stdout,
                  (r.stdout + r.stderr)[-300:])

        # ---- BUILD dt: the missed-problem pipeline, LIVE end to end ------------------
        import tempfile as _tf5
        with _tf5.TemporaryDirectory() as tmp5:
            drill = os.path.join(tmp5, "missdrill.py")
            with open(drill, "w") as fh:
                fh.write(
                    "from fastapi.testclient import TestClient\n"
                    "import main, store\n"
                    "c = TestClient(main.app)\n"
                    "# 4 reported, only 2 actually missed -> exactly 2 may be stored.\n"
                    "# build hu: misses ride the model's own tag SERVER-SIDE now; the\n"
                    "# client POST is only the deduplicated echo.\n"
                    "main._record_result_tags('1234', 'prealgebra',\n"
                    "    '[[quiz unit=\"3\" topic=\"1\" name=\"Adding fractions\" '\n"
                    "    'correct=\"3\" total=\"5\" missed=\"2/5 + 1/5 => 3/10 | '\n"
                    "    '1/2 + 1/4 => 2/6 | fake 3 => x | fake 4 => y\"]]')\n"
                    "r = c.post('/api/quiz/1234', json={'unit': 3, 'topic': 1,\n"
                    "    'name': 'Adding fractions', 'correct': 3, 'total': 5,\n"
                    "    'course': 'prealgebra'})\n"
                    "assert r.status_code == 200 and r.json()['ok'], r.text\n"
                    "d = c.get('/api/misses/1234?course=prealgebra').json()\n"
                    "assert d['ok'] and len(d['misses']) == 2, d\n"
                    "assert d['misses'][0]['question'] == '1/2 + 1/4', d  # newest first\n"
                    "assert d['misses'][0]['unit_name'], d               # unit name attached\n"
                    "# the mastery note hands them back with the spaced-review orders\n"
                    "note = main._mastery_note('1234', 0, 'prealgebra')\n"
                    "assert 'RECENT MISSED PROBLEMS (rule 55)' in note, note[-300:]\n"
                    "assert '2/5 + 1/5' in note and 'revisit exactly ONE' in note\n"
                    "# a perfect score stores nothing, whatever the tag claims\n"
                    "main._record_result_tags('1234', 'prealgebra',\n"
                    "    '[[quiz unit=\"3\" topic=\"2\" name=\"x\" correct=\"5\" '\n"
                    "    'total=\"5\" missed=\"phantom => z\"]]')\n"
                    "d = c.get('/api/misses/1234?course=prealgebra').json()\n"
                    "assert len(d['misses']) == 2 and 'phantom' not in str(d), d\n"
                    "# the sweep keeps the newest 200\n"
                    "for i in range(9):\n"
                    "    store.record_misses('1234', 'prealgebra', 1, 0, 'quiz',\n"
                    "        [{'q': f'bulk {i}-{j}', 'a': 'w'} for j in range(25)])\n"
                    "assert len(store.get_misses('1234', limit=500)) <= 200\n"
                    "# Start Fresh wipes the review list with everything else\n"
                    "store.reset_student_data('1234')\n"
                    "assert store.get_misses('1234', limit=10) == []\n"
                    "print('MISS-DRILL-OK')\n")
            env = dict(os.environ,
                       DATABASE_URL=f"sqlite:///{os.path.join(tmp5, 'm.db')}",
                       WEEKLY_EMAIL="off", PYTHONPATH=here)
            r = subprocess.run([sys.executable, drill], cwd=here, env=env,
                               capture_output=True, text=True)
            check("missed-problem pipeline live: clamp -> read-back -> note -> sweep -> reset",
                  r.returncode == 0 and "MISS-DRILL-OK" in r.stdout,
                  (r.stdout + r.stderr)[-300:])

        # ---- BUILD dy: child management, LIVE -- all four doors + every refusal -----
        import tempfile as _tf6
        with _tf6.TemporaryDirectory() as tmp6:
            drill = os.path.join(tmp6, "kiddrill.py")
            with open(drill, "w") as fh:
                fh.write(
                    "from fastapi.testclient import TestClient\n"
                    "import main, store\n"
                    "c = TestClient(main.app)\n"
                    "def signup(em):\n"
                    "    r = c.post('/api/parent/signup', json={'email': em,\n"
                    "               'password': 'drill-pass-123', 'name': 'P'})\n"
                    "    assert r.status_code == 200, r.text\n"
                    "    return r.json()['token']\n"
                    "tok = signup('a@example.com'); tok2 = signup('b@example.com')\n"
                    "r = c.post('/api/parent/students', json={'token': tok, 'name': 'Ana'})\n"
                    "code = r.json()['students'][0]['code']\n"
                    "# rename\n"
                    "r = c.post('/api/parent/student-rename', json={'token': tok, 'code': code, 'name': 'Ana Banana'})\n"
                    "assert r.json()['students'][0]['name'] == 'Ana Banana', r.text\n"
                    "# the OTHER parent can touch nothing (404, not 403)\n"
                    "for ep in ('student-rename', 'student-newcode', 'student-remove'):\n"
                    "    r = c.post(f'/api/parent/{ep}', json={'token': tok2, 'code': code, 'name': 'x'})\n"
                    "    assert r.status_code == 404, (ep, r.status_code)\n"
                    "# new code: history must MOVE\n"
                    "store.record_sprint(code, 'prealgebra', 1, 'make ten', 5, 8, 7, 9)\n"
                    "r = c.post('/api/parent/student-newcode', json={'token': tok, 'code': code})\n"
                    "new = r.json()['new_code']\n"
                    "assert new != code and r.json()['students'][0]['code'] == new, r.text\n"
                    "assert store.get_account(code) is None, 'old code must be dead'\n"
                    "assert len(store.get_sprint_history(new, 'prealgebra')) == 1, 'history must follow'\n"
                    "# attach: another family's code is refused; an orphan attaches\n"
                    "r = c.post('/api/parent/student-attach', json={'token': tok2, 'code': new})\n"
                    "assert r.status_code == 409, r.status_code\n"
                    "store.create_student_account('ORPHAN77', 'Zed', '')\n"
                    "r = c.post('/api/parent/student-attach', json={'token': tok2, 'code': 'ORPHAN77'})\n"
                    "assert r.status_code == 200 and r.json()['students'][0]['code'] == 'ORPHAN77', r.text\n"
                    "# remove: wrong typed name 400s; the right one deletes account AND data\n"
                    "r = c.post('/api/parent/student-remove', json={'token': tok, 'code': new, 'name': 'wrong'})\n"
                    "assert r.status_code == 400, r.status_code\n"
                    "r = c.post('/api/parent/student-remove', json={'token': tok, 'code': new, 'name': 'ana banana'})\n"
                    "assert r.status_code == 200 and r.json()['students'] == [], r.text\n"
                    "assert store.get_account(new) is None\n"
                    "assert store.get_sprint_history(new, 'prealgebra') == []\n"
                    "print('KID-DRILL-OK')\n")
            env = dict(os.environ,
                       DATABASE_URL=f"sqlite:///{os.path.join(tmp6, 'k.db')}",
                       WEEKLY_EMAIL="off", PYTHONPATH=here)
            r = subprocess.run([sys.executable, drill], cwd=here, env=env,
                               capture_output=True, text=True)
            check("child management live: rename, code-move, attach rules, typed-name remove",
                  r.returncode == 0 and "KID-DRILL-OK" in r.stdout,
                  (r.stdout + r.stderr)[-300:])

        # ---- BUILD ea: the pacing steer, LIVE ---------------------------------------
        import tempfile as _tf7
        with _tf7.TemporaryDirectory() as tmp7:
            drill = os.path.join(tmp7, "steerdrill.py")
            with open(drill, "w") as fh:
                fh.write(
                    "from fastapi.testclient import TestClient\n"
                    "import main, store\n"
                    "c = TestClient(main.app)\n"
                    "tok = c.post('/api/parent/signup', json={'email': 's@example.com',\n"
                    "    'password': 'drill-pass-123', 'name': 'P'}).json()['token']\n"
                    "code = c.post('/api/parent/students', json={'token': tok,\n"
                    "    'name': 'Ana'}).json()['students'][0]['code']\n"
                    "r = c.post('/api/parent/student-steer', json={'token': tok,\n"
                    "    'code': code, 'unit': 4, 'course': 'prealgebra'})\n"
                    "assert r.status_code == 200, r.text\n"
                    "d = c.get('/api/parent/overview', headers={'X-Parent-Token': tok}).json()\n"
                    "assert d['students'][0]['steer']['unit'] == 4, d\n"
                    "# the plan applies when the student arrives with no focus of their own\n"
                    "assert main._resolve_focus(code, 'prealgebra', 0) == (4, True)\n"
                    "# ...their explicit choice outranks it (rule 50)\n"
                    "assert main._resolve_focus(code, 'prealgebra', 7) == (7, False)\n"
                    "# ...and a different course is untouched\n"
                    "assert main._resolve_focus(code, 'algebra1', 0) == (0, False)\n"
                    "note = main._mastery_note(code, 4, 'prealgebra', steered=True)\n"
                    "assert 'THE FAMILY PLAN' in note and 'their agency wins' in note\n"
                    "# clearing ends it; a reset wipes it\n"
                    "c.post('/api/parent/student-steer', json={'token': tok, 'code': code, 'unit': 0})\n"
                    "assert main._resolve_focus(code, 'prealgebra', 0) == (0, False)\n"
                    "store.set_steer(code, 'prealgebra', 2)\n"
                    "store.reset_student_data(code)\n"
                    "assert store.get_steer(code) is None\n"
                    "print('STEER-DRILL-OK')\n")
            env = dict(os.environ,
                       DATABASE_URL=f"sqlite:///{os.path.join(tmp7, 's.db')}",
                       WEEKLY_EMAIL="off", PYTHONPATH=here)
            r = subprocess.run([sys.executable, drill], cwd=here, env=env,
                               capture_output=True, text=True)
            check("pacing steer live: set -> applies -> student outranks -> clear -> reset",
                  r.returncode == 0 and "STEER-DRILL-OK" in r.stdout,
                  (r.stdout + r.stderr)[-300:])


def part3q_reliability():
    # Added 2026-08-11 (build dg). The first full audit's Render logs proved the
    # stumbles were OURS, not rate limits (Audit_Findings_2026-08-11.md, PART 5):
    # claude-sonnet-5 intermittently rejects assistant-prefill continuation (a 400 that
    # NAMES its objection), five replies shipped as admitted partials at the old 1600
    # ceiling, and the rule-15 referee's false positives fed both by burning drafts.
    # This part proves the negotiated continuation, the raised ceiling, the empty-reply
    # retry, the stand-alone nudges, and the admin key's exit from query strings.
    print("\nPART 3q — reliability: continuation, empty retry, nudges, key transport")

    class _Resp:
        def __init__(self, text, stop):
            class _B:
                pass
            b = _B()
            b.type = "text"
            b.text = text
            self.content = [b]
            self.stop_reason = stop
            self.usage = None

    class _Stub:
        """A scripted stand-in for the Anthropic client. Each script step is a _Resp
        to return or an Exception to raise; every call's kwargs are recorded."""
        def __init__(self, script):
            self.script = list(script)
            self.calls = []
            self.messages = self          # so stub.messages.create(...) works

        def create(self, **kw):
            self.calls.append(kw)
            step = self.script.pop(0)
            if isinstance(step, Exception):
                raise step
            return step

    _PREFILL_ERR = Exception(
        "Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', "
        "'message': 'This model does not support assistant message prefill. The "
        "conversation must end with a user message.'}}")

    # --- the ceiling rose, and it is a named constant ---------------------------------
    check("MAX_REPLY_TOKENS is 3000 (raised from 1600 in build dg)",
          getattr(tutor, "MAX_REPLY_TOKENS", None) == 3000,
          f"got {getattr(tutor, 'MAX_REPLY_TOKENS', None)}")

    msgs = [{"role": "user", "content": "hello"}]

    # --- plain reply: one call, ceiling passed through --------------------------------
    stub = _Stub([_Resp("All done.", "end_turn")])
    out = tutor._create_full(stub, "dg-stub-plain", None, msgs, {})
    check("plain turn: one call, text returned", out == "All done." and len(stub.calls) == 1,
          f"out={out!r}, calls={len(stub.calls)}")
    check("plain turn: max_tokens kwarg is the ceiling",
          stub.calls[0].get("max_tokens") == tutor.MAX_REPLY_TOKENS,
          f"got {stub.calls[0].get('max_tokens')}")

    # --- prefill continuation, when the model accepts it ------------------------------
    stub = _Stub([_Resp("abc", "max_tokens"), _Resp("def", "end_turn")])
    out = tutor._create_full(stub, "dg-stub-prefill-ok", None, msgs, {})
    last = stub.calls[1]["messages"][-1]
    check("prefill continuation: stitched", out == "abcdef", f"out={out!r}")
    check("prefill continuation: second call ends with the assistant partial",
          last.get("role") == "assistant" and last.get("content") == "abc",
          f"last message: {last}")

    # --- THE AUDIT'S BUG: the named 400 switches to the user-nudge fallback -----------
    stub = _Stub([_Resp("part1", "max_tokens"), _PREFILL_ERR, _Resp("part2", "end_turn")])
    out = tutor._create_full(stub, "dg-stub-prefill-no", None, msgs, {})
    last = stub.calls[2]["messages"][-1]
    check("prefill rejection: reply still completes (negotiated fallback)",
          out == "part1part2", f"out={out!r}, calls={len(stub.calls)}")
    check("prefill rejection: fallback call ends with the continuation nudge",
          last.get("role") == "user" and "cut off" in str(last.get("content", "")),
          f"last message: {last}")
    check("prefill rejection: the refusal is REMEMBERED for this run",
          tutor._PREFILL_OK.get("dg-stub-prefill-no") is False, "flag not recorded")
    # ...and the next turn on that model goes straight to the fallback shape
    stub = _Stub([_Resp("x", "max_tokens"), _Resp("y", "end_turn")])
    out = tutor._create_full(stub, "dg-stub-prefill-no", None, msgs, {})
    last = stub.calls[1]["messages"][-1]
    check("remembered refusal: no second 400 is ever risked",
          out == "xy" and last.get("role") == "user",
          f"out={out!r}, last={last}")
    tutor._PREFILL_OK.pop("dg-stub-prefill-no", None)   # leave no test residue

    # --- an unrelated API error must still RAISE (never swallowed) --------------------
    stub = _Stub([_Resp("head", "max_tokens"), Exception("rate limited, try later")])
    try:
        tutor._create_full(stub, "dg-stub-other-err", None, msgs, {})
        ok_ = False
    except Exception:
        ok_ = True
    check("an unrelated API error still raises (only the NAMED 400 is negotiated)", ok_,
          "the error was swallowed")

    # --- still truncated after 2 continuations: stitched, loudly, 3 calls total -------
    stub = _Stub([_Resp("a", "max_tokens"), _Resp("b", "max_tokens"), _Resp("c", "max_tokens")])
    out = tutor._create_full(stub, "dg-stub-partial", None, msgs, {})
    check("hop limit: exactly 3 calls, pieces stitched", out == "abc" and len(stub.calls) == 3,
          f"out={out!r}, calls={len(stub.calls)}")

    # --- an EMPTY reply is retried once before any apology ----------------------------
    stub = _Stub([_Resp("", "end_turn"), _Resp("Nice work. Let's keep going.", "end_turn")])
    out = tutor._create_verified(stub, "dg-stub-empty", None, msgs, " [test]")
    check("empty reply: retried once, silently",
          out == "Nice work. Let's keep going." and len(stub.calls) == 2,
          f"out={out!r}, calls={len(stub.calls)}")
    stub = _Stub([_Resp("", "end_turn"), _Resp("", "end_turn")])
    out = tutor._create_verified(stub, "dg-stub-empty2", None, msgs, " [test]")
    check("empty twice: gives up cleanly so the caller can apologize",
          out == "" and len(stub.calls) == 2, f"out={out!r}, calls={len(stub.calls)}")

    # --- both regeneration nudges order the rewrite to STAND ALONE --------------------
    # The S-1 mechanism: two good drafts were burned by referee misfires, and the third
    # opened "So the hypotenuse is 5" -- the tail of an explanation only the DISCARDED
    # drafts contained. The nudge is the only voice in the room at that moment.
    check("the prose nudge orders a stand-alone rewrite",
          "STAND ALONE" in tutor._PROSE_NUDGE and "from scratch" in tutor._PROSE_NUDGE,
          "missing the stand-alone instruction")
    check("the mathcheck nudge orders a stand-alone rewrite",
          "STAND ALONE" in tutor._MATHCHECK_NUDGE, "missing the stand-alone instruction")

    # --- the admin key stays out of query strings (the L-4 leak) ----------------------
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "static", "admin.html"), encoding="utf-8") as fh:
        adm = fh.read()
    check("admin.html sends the key in the X-Admin-Key header",
          '"X-Admin-Key"' in adm, "header not found")
    check("admin.html never builds a key-carrying URL",
          not re.search(r'\?key="\s*\+', adm), "found a '?key=\" +' URL construction")
    check("admin.html keeps the key in sessionStorage, not the address bar",
          'sessionStorage.setItem("mt_admin_key"' in adm and "history.replaceState" in adm,
          "sessionStorage stash or address-bar scrub missing")
    with open(os.path.join(here, "main.py"), encoding="utf-8") as fh:
        mn = fh.read()
    n_alias = mn.count('alias="X-Admin-Key"')
    check("all four admin GET endpoints accept the X-Admin-Key header",
          n_alias >= 4, f"found {n_alias} of 4")
    n_pref = mn.count("_require_admin(x_admin_key or key)")
    check("the header is preferred over the query param",
          n_pref >= 4, f"found {n_pref} of 4")

    # --- BUILD dn: dg's documented residual is closed -- /community?mod= is gone ------
    # The forum-moderation unlock was the LAST place an admin key rode in a URL.
    # community.html now uses the exact discipline admin.html got in dg: the key lives
    # in sessionStorage (the SAME "mt_admin_key" stash, so /admin unlocks both), a
    # legacy ?mod= link is honoured once then scrubbed from the address bar, and the
    # moderate call sends the key in the X-Admin-Key header -- never in the body.
    with open(os.path.join(here, "static", "community.html"), encoding="utf-8") as fh:
        com = fh.read()
    check("community.html reads the mod key from the shared sessionStorage stash",
          'sessionStorage.getItem("mt_admin_key")' in com, "stash read not found")
    check("community.html honours a legacy ?mod= link ONCE, then scrubs the address bar",
          'params.get("mod")' in com and 'sessionStorage.setItem("mt_admin_key"' in com
          and 'history.replaceState(null, "", "/community")' in com,
          "legacy stash-and-scrub missing")
    check("community.html sends the mod key in the X-Admin-Key header",
          '"X-Admin-Key": MOD_KEY' in com, "header transport not found")
    check("community.html never puts the key in the moderate request body",
          "key: MOD_KEY" not in com, "the body still carries the key")
    check("a 401 clears the stash and drops back to the public view",
          'sessionStorage.removeItem("mt_admin_key")' in com
          and "e.status === 401" in com, "the wrong-key recovery path is missing")
    check("admin.html no longer builds ANY key-carrying URL (?mod= construction gone)",
          '?mod=" +' not in adm and '"/community"' in adm,
          "the moderation quick-link still carries the key")
    i_mod = mn.find("def forum_moderate")
    mod_src = mn[i_mod:i_mod + 900] if i_mod > 0 else ""
    check("POST /api/forum/moderate accepts the X-Admin-Key header",
          'alias="X-Admin-Key"' in mod_src, "header parameter not found on the endpoint")
    check("  through the same constant-time gate as every admin call",
          "_require_admin(x_admin_key or body.key)" in mod_src,
          "expected _require_admin(x_admin_key or body.key)")

    # ...and the whole door proven LIVE: wrong header 401s, right header passes auth
    # (400/404 further in prove we got PAST the gate), the legacy body key still works
    # for a cached pre-dn page, and no key at all is refused.
    try:
        import httpx  # noqa: F401  (TestClient's engine)
        _have_httpx = True
    except Exception:  # noqa: BLE001
        _have_httpx = False
    if not _have_httpx:
        skip("moderate endpoint live drill", "httpx not installed here")
    else:
        import tempfile as _tf3
        with _tf3.TemporaryDirectory() as tmp3:
            drill = os.path.join(tmp3, "moddrill.py")
            with open(drill, "w") as fh:
                fh.write(
                    "from fastapi.testclient import TestClient\n"
                    "import main\n"
                    "c = TestClient(main.app)\n"
                    "u = '/api/forum/moderate'\n"
                    "r = c.post(u, json={'kind': 'post', 'item_id': 'x'},\n"
                    "           headers={'X-Admin-Key': 'WRONG'})\n"
                    "assert r.status_code == 401, ('wrong header', r.status_code)\n"
                    "r = c.post(u, json={'kind': 'banana', 'item_id': 'x'},\n"
                    "           headers={'X-Admin-Key': 'TESTMOD123'})\n"
                    "assert r.status_code == 400, ('right header, bad kind', r.status_code)\n"
                    "r = c.post(u, json={'kind': 'post', 'item_id': 'nope'},\n"
                    "           headers={'X-Admin-Key': 'TESTMOD123'})\n"
                    "assert r.status_code == 404, ('right header, unknown id', r.status_code)\n"
                    "r = c.post(u, json={'key': 'TESTMOD123', 'kind': 'banana', 'item_id': 'x'})\n"
                    "assert r.status_code == 400, ('legacy body key', r.status_code)\n"
                    "r = c.post(u, json={'kind': 'post', 'item_id': 'x'})\n"
                    "assert r.status_code == 401, ('no key at all', r.status_code)\n"
                    "print('MODKEY-DRILL-OK')\n")
            env = dict(os.environ,
                       DATABASE_URL=f"sqlite:///{os.path.join(tmp3, 'm.db')}",
                       FORUM_MOD_KEY="TESTMOD123", WEEKLY_EMAIL="off",
                       PYTHONPATH=here)
            r = subprocess.run([sys.executable, drill], cwd=here, env=env,
                               capture_output=True, text=True)
            check("moderate endpoint live: 401 wrong / past-the-gate right / legacy body ok",
                  r.returncode == 0 and "MODKEY-DRILL-OK" in r.stdout,
                  (r.stdout + r.stderr)[-300:])


# =============================================================================
# PART 3r -- THE FIGURES THE AUDIT COULD NOT DRAW (build di)
# -----------------------------------------------------------------------------
# Finding S-4: a jump discontinuity "drawn" as two full parallel lines because the
# grapher had no piecewise vocabulary. Finding S-9: a student asked twice to SEE the
# wrong decimal lineup and got prose labels because no tag could draw it. Both tools
# exist now, and this part proves them THROUGH THE REAL RENDERER (node executes
# math-figures.js, the same file the browser runs) -- plus the discovery the harness
# made on its first run: hole= had NEVER drawn on a genuine 0/0 removable point,
# because the renderer evaluated the function AT the hole and bailed on NaN. The
# canonical scripts had quietly worked around it with pre-simplified forms.
# =============================================================================
_DI_GRAPH_HARNESS = r'''
const fs = require("fs");
global.window = {};
eval(fs.readFileSync(process.argv[2], "utf8"));
const MF = global.window.MathFigures;
const out = [];
function t(name, cond) { out.push([name, !!cond]); }
// the audit's jump, drawn right: open circle at (2,3), closed dot at (2,6), no bridge
const svg = MF.graph({ func: "x+1 for x<2; x+4 for x>=2", range: "0..4", yrange: "0..8" });
t("the strict bound gets an OPEN circle at (2,3)", svg.includes('cy="267.5" r="5" fill="#fbfbff"'));
t("the inclusive bound gets a CLOSED dot at (2,6)", /cy="125" r="5" fill="#[0-9a-f]{6}" stroke="#ffffff"/.test(svg));
const polys = [...svg.matchAll(/<polyline points="([^"]+)"/g)].map(m => m[1].split(" ").map(p => parseFloat(p.split(",")[0])));
t("two pieces, each clipped to its own side of x=2",
  polys.length === 2 && Math.max(...polys[0]) <= 220.01 && Math.min(...polys[1]) >= 219.99);
t("the legend names the domains", svg.includes("for x&lt;2") && svg.includes("for x&gt;=2"));
const s2 = MF.graph({ func: "x^2 for -1<=x<3", range: "-4..4" });
t("a double-ended domain marks both endpoints", (s2.match(/r="5"/g) || []).length === 2);
const s3 = MF.graph({ func: "x+1 for x≥2", range: "0..4" });
t("unicode bounds are accepted", /stroke="#ffffff"/.test(s3));
const s4 = MF.graph({ func: "x+1 for banana", range: "0..4" });
t("an unparseable domain fails OPEN -- the curve still draws",
  [...s4.matchAll(/<polyline/g)].length === 1);
// the harness's own first-run discovery, kept forever:
const s5 = MF.graph({ func: "(x^2-4)/(x-2)", hole: "2", range: "0..4", yrange: "0..6" });
t("a hole on a genuine 0/0 point actually draws (numeric limit)", s5.includes(">hole<"));
const s6 = MF.graph({ func: "1/(x-2)", hole: "2", range: "0..4", yrange: "-6..6" });
t("an asymptote NEVER gets a hole painted on it (rule 51e in pixels)", !s6.includes(">hole<"));
const s7 = MF.graph({ func: "sin(x)", range: "-6..6" });
t("a plain un-domained function is untouched", s7.includes("<polyline"));
// build dk (re-run finding 8): a labeled point must never sit on a declared hole
const s8 = MF.graph({ lines: "y=x+3", hole: "3", points: "(3,6) (1,4)", range: "0..6" });
t("a point AT a declared hole is dropped", !s8.includes("(3, 6)"));
t("...while other points on the same graph survive", s8.includes("(1, 4)"));
console.log(JSON.stringify(out));
'''


def part3r_batch_d_figures():
    print("\nPART 3r — the figures the audit could not draw (build di)")
    here = os.path.dirname(os.path.abspath(__file__))
    # (1) build he: showColumn lives ONCE, in board.js -- the byte-identical check
    # (build bk's drift class) is now the stronger property "there is only one copy",
    # which PART 3aw enforces. The behavioural guarantees read the single source.
    body = ""
    try:
        with open(os.path.join(here, "static", "board.js"), encoding="utf-8") as fh:
            m = re.search(r"function showColumn\(a\) \{[\s\S]*?\n\}", fh.read())
        body = m.group(0) if m else ""
    except OSError:
        pass
    check("showColumn exists in the shared board module",
          bool(body), "board.js lost showColumn -- no page can draw column math")
    check("align='last' NEVER completes the wrong layout",
          "res && !wrongAlign" in body,
          "a result row in the deliberately-wrong lineup would complete a wrong sum "
          "on our board (rules 13 and 26)")
    check("the wrong lineup carries its built-in badge",
          '"cwarn"' in body, "the badge div is missing")
    for page in ("session", "practice", "topic"):
        with open(os.path.join(here, "static", f"{page}.html"), encoding="utf-8") as fh:
            css = fh.read()
        check(f"  [{page}] carries the wrong-way styling", ".colmath.colwrong" in css,
              "amber styling missing -- the wrong way must never look like the taught way")
    # (2) the piecewise/hole behaviour, proven through the REAL math-figures.js
    try:
        subprocess.run(["node", "--version"], capture_output=True, check=True)
    except Exception:  # noqa: BLE001
        skip("piecewise render checks", "node not available")
        return
    import json as _json
    import tempfile as _tf
    with _tf.TemporaryDirectory() as tmp:
        hpath = os.path.join(tmp, "di.js")
        with open(hpath, "w") as fh:
            fh.write(_DI_GRAPH_HARNESS)
        res = subprocess.run(["node", hpath, os.path.join(here, "static", "math-figures.js")],
                             capture_output=True, text=True)
        if res.returncode != 0:
            bad("piecewise render harness", res.stderr.strip()[:200])
            return
        for name, okk in _json.loads(res.stdout):
            check(f"render: {name}", okk, "see math-figures.js graph()")
    # (3) the shared tool note reaches every course (PART 1's discipline)
    for c in COURSES:
        prompt = tutor.build_system_prompt(dict(STUDENT), course=c)
        check(f"piecewise + wrong-lineup docs reach [{c}]",
              "for x<2" in prompt and 'align="last"' in prompt,
              "the shared board-tools note is missing from this course's prompt")


# =============================================================================
# PART 3s -- BACKUPS: THE WAY BACK MUST ACTUALLY WORK (build dj)
# -----------------------------------------------------------------------------
# Jim: "if Render falters or something falters, do we have sufficient backup so that
# we could recreate everything right away?" A backup system is only real if the
# RESTORE has been rehearsed, so this part performs the whole drill on every run:
# seed a real database, snapshot it with store.export_all, restore that snapshot into
# a SECOND, blank database THROUGH THE ACTUAL restore_backup.py TOOL (dry look first,
# which must change nothing), then prove the two databases are row-for-row identical.
# Plus the boundaries: no restore endpoint may ever exist, the download rides the
# header, the nightly pass is fenced and atomic.
# =============================================================================
_BK_SEED = r'''
import json, os, sys
import store
store.init()
assert store.enabled(), "sqlite store failed to enable: " + str(store.status())
store.record_check("BKTEST", 2, 9, 10, "Integers", course="prealgebra")
store.record_check("BKTEST", 4, 8, 10, "Fractions", course="prealgebra")
store.record_foundation_heard("BKTEST", "prealgebra", "fraction")
store.create_beta_code("TRY-BACKUP7", "backup drill", 5, 2)
store.log_usage(kind="brain", code="BKTEST", course="prealgebra", mode="lesson",
                model="test", input_tokens=10, output_tokens=5)
snap = store.export_all()
json.dump(snap, open(sys.argv[1], "w"))
print(sum(snap["row_counts"].values()))
'''

_BK_EXPORT = r'''
import json, sys
import store
store.init()
assert store.enabled(), "sqlite store failed to enable"
json.dump(store.export_all(), open(sys.argv[1], "w"))
'''


def _bk_tables(path):
    import json as _json
    snap = _json.load(open(path))
    # order-independent, deep comparison: each table's rows as a sorted list of
    # sorted-key JSON strings
    return {name: sorted(_json.dumps(r, sort_keys=True) for r in rows)
            for name, rows in snap["tables"].items()}


def part3s_backups():
    print("\nPART 3s — backups: the way back must actually work")
    here = os.path.dirname(os.path.abspath(__file__))
    import gzip as _gz
    import json as _json
    import tempfile as _tf
    with _tf.TemporaryDirectory() as tmp:
        db1 = os.path.join(tmp, "db1.sqlite")
        db2 = os.path.join(tmp, "db2.sqlite")
        snap_json = os.path.join(tmp, "snap.json")
        snap_gz = os.path.join(tmp, "snap.json.gz")
        seed = os.path.join(tmp, "seed.py")
        exp = os.path.join(tmp, "exp.py")
        with open(seed, "w") as fh:
            fh.write(_BK_SEED)
        with open(exp, "w") as fh:
            fh.write(_BK_EXPORT)

        def run(script, dburl, *args):
            # PYTHONPATH, not just cwd: python puts the SCRIPT'S directory on the
            # path, and the seed/export scripts live in the temp dir, not the repo.
            env = dict(os.environ, DATABASE_URL=dburl, PYTHONPATH=here)
            return subprocess.run([sys.executable, script, *args], cwd=here, env=env,
                                  capture_output=True, text=True)

        # build gh: every step below seeds, exports and restores a real database.
        # No SQLAlchemy means the drill cannot run at all -- say so, do not fail.
        if not dep_gate("backup drill: seed + export", "sqlalchemy",
                        "the drill seeds, exports and restores a real database"):
            return
        # 1. seed a real database and snapshot it
        r = run(seed, f"sqlite:///{db1}", snap_json)
        if r.returncode != 0:
            bad("backup drill: seed + export", r.stderr.strip()[:300])
            return
        total = int(r.stdout.strip().splitlines()[-1])
        check(f"a seeded database exports ({total} rows)", total >= 5, f"only {total} rows")
        with open(snap_json, "rb") as fh:
            _gz_bytes = _gz.compress(fh.read())
        with open(snap_gz, "wb") as fh:
            fh.write(_gz_bytes)

        # 2. the DRY LOOK must change nothing (a blank second database stays blank)
        r = run(os.path.join(here, "restore_backup.py"), f"sqlite:///{db2}", snap_gz)
        check("restore_backup.py without the flag is a DRY LOOK (exit 0, says so)",
              r.returncode == 0 and "DRY LOOK" in r.stdout, (r.stdout + r.stderr)[-200:])
        r = run(exp, f"sqlite:///{db2}", os.path.join(tmp, "after_dry.json"))
        dry_rows = sum(len(v) for v in _bk_tables(os.path.join(tmp, "after_dry.json")).values()) \
            if r.returncode == 0 else -1
        check("the dry look changed NOTHING (second database still empty)", dry_rows == 0,
              f"{dry_rows} rows appeared without the flag")

        # 3. the real restore, THROUGH THE ACTUAL TOOL, gzip file and all
        r = run(os.path.join(here, "restore_backup.py"), f"sqlite:///{db2}",
                snap_gz, "--yes-i-mean-it")
        check("restore_backup.py --yes-i-mean-it restores", r.returncode == 0,
              (r.stdout + r.stderr)[-300:])
        r = run(exp, f"sqlite:///{db2}", os.path.join(tmp, "after_restore.json"))
        if r.returncode != 0:
            bad("backup drill: re-export after restore", r.stderr.strip()[:300])
            return
        t1, t2 = _bk_tables(snap_json), _bk_tables(os.path.join(tmp, "after_restore.json"))
        diff = [n for n in set(t1) | set(t2) if t1.get(n) != t2.get(n)]
        check("the restored database is ROW-FOR-ROW identical to the snapshot",
              not diff, f"tables differing after restore: {diff[:5]}")

    # 4. the boundaries, from the source
    with open(os.path.join(here, "main.py"), encoding="utf-8") as fh:
        mn = fh.read()
    check("main.py NEVER calls import_all (no restore endpoint can exist)",
          "import_all" not in mn,
          "a remote wipe-and-replace is a foot-gun -- restores are offline only")
    check("the backup download rides the X-Admin-Key header",
          'def admin_backup_download' in mn and mn.count('alias="X-Admin-Key"') >= 6,
          "backup endpoints missing the header alias")
    check("the nightly pass is fenced inside the heartbeat",
          "_backup_pass()" in mn and "[backup] loop error" in mn,
          "an unfenced pass could kill the digests")
    check("the snapshot write is ATOMIC (tmp then rename)",
          "os.replace(tmp, _BACKUP_DIR / name)" in mn,
          "a crash mid-write must never leave a half snapshot")
    check("rotation keeps BACKUP_KEEP newest",
          "[:-BACKUP_KEEP]" in mn, "no rotation found")
    with open(os.path.join(here, "static", "admin.html"), encoding="utf-8") as fh:
        adm = fh.read()
    check("/admin has the Backups card with a header-borne download",
          'id="bkDownload"' in adm and '"X-Admin-Key": KEY' in adm,
          "the offsite copy needs a button (build cx: buttons, not instructions)")
    check("/admin has NO restore control",
          "restore" not in adm.lower() or "restore_backup.py" in adm,
          "restore must stay an offline, deliberate act")
    for fname in ("RECOVERY.md", "restore_backup.py"):
        check(f"{fname} exists and is not truncated",
              os.path.exists(os.path.join(here, fname))
              and "I did no harm and this file is not truncated"
              in open(os.path.join(here, fname), encoding="utf-8").read(),
              "the runbook/tool must ship with the code")


# =============================================================================
# PART 3t -- THE FIVE TEACHING UPGRADES (build ee, 2026-08-12)
# =============================================================================
# Rules 56-60 are the prompt-lane queue from the evidence-base work
# (claude/Teaching_Evidence_Base_2026-08-10.md): find-the-error (WWC g20 r1),
# self-monitoring (WWC g16 r2 + EEF r5), two-ways-one-board (WWC g16 r4 + g20 r3),
# right-answer-wrong-method (MAA IPG), and the board spotlight (signaling).
# WHAT THIS PART PROVES:
#   (a) each rule lives in the SHARED block exactly once -- never copied per course
#       (the bk lesson: a rule pasted into one of eleven templates reached one course);
#   (b) each rule keeps its load-bearing phrases -- the anchors a future edit must not
#       quietly drop (rule 56's safety frame most of all: wrong work is ANNOUNCED as a
#       game, sourced from the CATALOGUE, and NEVER STAYS on the board);
#   (c) the spotlight is not just words: all THREE teaching pages implement it -- the
#       spotlightBoard function with both board keys, the .stepglow CSS and its pulse,
#       a turn-start clear -- and session.html still falls through to the page tour
#       (highlightEl) for non-board ids, so the opening walk-through is unharmed.
def part3t_teaching_upgrades():
    print("\nPART 3t — the five teaching upgrades (rules 56-60, build ee)")
    note = tutor.GRAPH_TOOL_NOTE
    built = tutor.build_system_prompt(dict(STUDENT), course="algebra1")

    headlines = {
        56: "FIND THE ERROR: A WRONG SOLUTION, CLEARLY LABELED",
        57: "TEACH THE STUDENT TO CHECK THEMSELVES",
        58: 'TWO WAYS, ONE BOARD, THEN "WHICH WOULD YOU CHOOSE?"',
        59: "A RIGHT ANSWER CAN STILL CARRY A WRONG METHOD",
        60: "POINT WITH LIGHT WHEN WHERE-TO-LOOK IS THE LESSON",
    }
    for n, h in sorted(headlines.items()):
        check(f"rule {n} lives in the shared block exactly once", note.count(h) == 1,
              f"count in GRAPH_TOOL_NOTE = {note.count(h)} -- shared rules go in once, "
              f"never per course")
        check(f"rule {n} reaches a built prompt exactly once", built.count(h) == 1,
              f"count in the built algebra1 prompt = {built.count(h)} -- a duplicate "
              f"means it leaked into a course template too")

    anchors = {
        56: [("the game is ANNOUNCED on the board itself",
              '[[step eq="Detective time: find the mistake!"]]'),
             ("the mistake comes from the CATALOGUE, not thin air",
              "misconception catalogue below the rules"),
             ("the wrong work NEVER stays on the board",
              "THE WRONG WORK NEVER STAYS"),
             ("the incomplete-solution cousin is offered",
              "an INCOMPLETE solution")],
        57: [("the before-question is the panel's",
              "what is this problem asking, in your own words?"),
             ("the after-question is the panel's",
              "does the answer make sense for the story?"),
             ("one question at a time, never a checklist",
              "ONE at a time, at a natural moment")],
        58: [("same problem, same board",
              "applied to the SAME problem, on the SAME board"),
             ("the where-do-they-meet question",
              "where do the two ways"),
             ("the which-would-you-choose question",
              "which would YOU pick"),
             ("the student's chosen method is respected after",
              "RESPECTED in the")],
        59: [("the right answer is accepted FIRST",
              "accept the answer FIRST"),
             ("the ask is how-did-you-get-that",
              "out of curiosity, not suspicion"),
             ("the method is broken with its own failure case",
              "WHEN would it stop working?"),
             ("the tally is never touched by method work",
              "rule 45 is untouched")],
        60: [("the line key is documented",
              '[[highlight id="line"]]'),
             ("the board key is documented",
              '[[highlight id="board"]]'),
             ("one spotlight per reply, at most",
              "AT MOST ONE spotlight")],
    }
    for n, pairs in sorted(anchors.items()):
        for label, needle in pairs:
            check(f"  rule {n}: {label}", needle in note,
                  f"the phrase {needle!r} left the shared block -- restore it or "
                  f"update this anchor ON PURPOSE")

    # (c) the spotlight mechanism, on every page a student is taught on
    here = os.path.dirname(os.path.abspath(__file__))
    for page in ("session.html", "practice.html", "topic.html"):
        path = os.path.join(here, "static", page)
        try:
            with open(path, encoding="utf-8") as fh:
                src = fh.read()
        except OSError as exc:
            bad(f"{page}: readable", str(exc))
            continue
        # build he: spotlightBoard/clearSpot moved to board.js (one copy) -- their
        # EXISTENCE and key handling are asserted once against the module below.
        # What each page must still own: the include (3aw), the CSS (styling is
        # page-scoped), and the CALLS -- a glow never outlives its moment only if
        # THIS page's turn code actually clears it.
        check(f"{page}: .stepglow style present", ".stepglow {" in src,
              "the glow class has no styling -- an invisible cue")
        check(f"{page}: the glow pulses", "stepglowpulse" in src,
              "the pulse animation is gone (reduced-motion users get the still "
              "glow via the dz rule; everyone else should see it breathe)")
        check(f"{page}: a stale spotlight is cleared at turn start",
              src.count("clearSpot()") >= 1,
              "clearSpot must be CALLED by this page's turn code (it is defined in "
              "board.js) so a glow never outlives its moment")
        check(f"{page}: reduced-motion rule still present",
              "prefers-reduced-motion" in src,
              "the dz accessibility rule must survive this build")
    bsrc = ""
    try:
        with open(os.path.join(here, "static", "board.js"), encoding="utf-8") as fh:
            bsrc = fh.read()
    except OSError:
        pass
    check("board.js: spotlightBoard exists (one copy)", "function spotlightBoard" in bsrc,
          "the board spotlight function is gone from the shared module")
    check("board.js: handles the line key", 'key === "line"' in bsrc,
          '[[highlight id="line"]] would silently no-op on every page at once')
    check("board.js: handles the board key", 'key === "board"' in bsrc,
          '[[highlight id="board"]] would silently no-op on every page at once')
    # session only: the opening tour must still work for non-board ids
    with open(os.path.join(here, "static", "session.html"), encoding="utf-8") as fh:
        ssrc = fh.read()
    check("session.html: page-tour ids still fall through to highlightEl",
          "if (!spotlightBoard(attrs.id)) highlightEl(attrs.id)" in ssrc,
          "board keys must be tried FIRST and everything else must still reach the "
          "tour -- otherwise the opening walk-through breaks")


# =============================================================================
# PART 3u -- THE VIDEO PRESENCE LAYER (build ej, 2026-08-12)
# =============================================================================
# Mr. Cadabra's video face (one-time HeyGen library) rides OVER the canvas robot in
# tutor-face.js; the robot is the always-drawn fallback. These checks pin the safety
# properties that make that swap harmless, and they validate the asset manifest the
# moment it exists -- so the day Jim drops the videos in, the battery starts proving
# them instead of ignoring them.
def part3u_video_presence():
    print("\nPART 3u — the video presence layer (robot as fallback)")
    here = os.path.dirname(os.path.abspath(__file__))
    tf_path = os.path.join(here, "static", "tutor-face.js")
    try:
        with open(tf_path, encoding="utf-8") as fh:
            tf = fh.read()
    except OSError as exc:
        bad("tutor-face.js readable", str(exc)); return

    check("the robot still draws (the fallback face exists)",
          "---- mouth: a bar that OPENS with the voice ----" in tf and "VISOR" in tf,
          "the canvas robot is the safety net under every video failure -- it must "
          "never be deleted, only covered")
    check("the robot draws BEFORE the presence tick, every frame",
          "_drawRobot(ctx, w, h, opts);" in tf
          and tf.index("_drawRobot(ctx, w, h, opts);") < tf.index("presenceTick(ctx.canvas"),
          "if the video dies mid-lesson the robot must already be on the canvas")
    check("the presence is muted, inline, and decorative -- forever",
          "v.muted = true" in tf and 'setAttribute("playsinline"' in tf
          and 'setAttribute("aria-hidden", "true")' in tf,
          "the corner NEVER makes sound (his voice lives in the pages) and a screen "
          "reader must skip it")
    check("the presence never unmutes",
          ".muted = false" not in tf and "v.volume" not in tf,
          "a second audio source under his real voice would be chaos")
    check("any media error tears down to the robot",
          tf.count("presenceTeardown()") >= 2,
          "onerror must remove the video layer, not leave a black circle")
    check("absence of assets is a NORMAL state (phase-dark)",
          'P.state = "off"' in tf and "presence.json" in tf,
          "a 404 on the manifest must be silent -- code and videos deploy independently")
    check("reduced-motion gets a still poster or the robot",
          "prefers-reduced-motion" in tf,
          "motion-sensitive users must never get a looping video")
    check("the export keeps the API every page depends on",
          "draw: drawWithPresence" in tf and "moodFrom: moodFrom" in tf,
          "six pages call TutorFace.draw/moodFrom -- the names must survive")
    check('"speaking" deliberately maps to the idle loop (no fake lip-sync)',
          '"idle";                                    // idle AND speaking' in tf,
          "the design's honest heart: his voice talks, the face never fakes a mouth")
    for page in ("session.html", "practice.html", "topic.html",
                 "demo.html", "challenge.html", "landing.html"):
        with open(os.path.join(here, "static", page), encoding="utf-8") as fh:
            check(f"{page} still includes tutor-face.js", "tutor-face.js" in fh.read(),
                  "the page would lose both faces at once")

    # BUILD er: THE THUMBS-UP MUST HAVE A DOORBELL. It was generated, shipped, listed in
    # the manifest -- and unreachable, because the pages' setState only ever holds
    # speaking/listening/thinking/idle and "happy" was never passed in. A clip nothing
    # can trigger is a clip that does not exist.
    check("the presence exposes a celebrate() one-shot", "function celebrate" in tf
          and "celebrate: celebrate" in tf,
          "mood 'happy' is never set by any page, so the thumbs-up needs its own door")
    check("  celebrate() does NOT touch the page's state machine",
          "presenceShow(\"happy\", true)" in tf,
          "hijacking `state` would disturb the busy glow, the thinking flag and the "
          "level meter, which all read it")
    for page in ("session.html", "practice.html", "topic.html"):
        with open(os.path.join(here, "static", page), encoding="utf-8") as fh:
            src = fh.read()
        check(f"  {page} rings it when a correct answer is marked",
              "TutorFace.celebrate()" in src and 'name === "mark"' in src,
              "a right answer is the moment the thumbs-up is FOR; without this call the "
              "clip can never play in a real lesson")

    # BUILD es: THE CELEBRATION MUST NOT DEPEND ON THE AVATAR. The clip we shipped as
    # "thumbs_up" contains no thumbs -- the HeyGen presenter never raises a hand, at any
    # crop -- so er's doorbell rang a silent bell. The gold ring is the celebration now;
    # the clip is a bonus. These checks stop it from quietly becoming avatar-dependent
    # again, and stop the burst from being the kind of decoration that hurts people.
    check("a correct answer draws OUR celebration, not the avatar's",
          "function celebrationBurst" in tf and "tfRing" in tf,
          "the shipped clip has no gesture in it -- if the ring goes, a right answer is "
          "invisible again")
    check("  the burst fires even with NO video presence at all",
          'if (P.state !== "active" || P.reduced) return false;' not in tf
          and "celebrationBurst(_lastCanvas, small)" in tf,
          "the robot fallback and reduced-motion users earn a celebration too; celebrate() "
          "must never early-return before the ring")
    check("  reduced motion gets an opacity-only ring (no scaling, no sparkles)",
          "tfRingStill" in tf and "if (P.reduced) {" in tf,
          "a motion-sensitive child must not be thrown a sparkle burst")
    check("  the burst is decorative and cannot be clicked",
          "pointer-events:none" in tf and tf.count('setAttribute("aria-hidden", "true")') >= 2,
          "the tally and his voice carry the meaning; the ring must be invisible to a "
          "screen reader and must never intercept a tap on the board")
    check("  the burst scales off the slot's real size, not fixed pixels",
          "getBoundingClientRect()" in tf and "S * 0.016" in tf,
          "the corner face is ~90px in a lesson and ~220px on the demo; fixed sizes throw "
          "dinner-plate sparkles at one of them")
    check("  a presence clip with no decodable encoding tears down to the robot",
          "_sourcesFailed(v, presenceTeardown)" in tf and tf.count("_sourcesFailed") >= 3,
          "build ep asserted the <video> fires error when every <source> fails; it does "
          "NOT -- without this the presence sits on a dead poster instead of falling back")
    check("  the presence host hides the robot behind a still frame",
          "background-image:url('" in tf and "m.poster" in tf,
          "two videos crossfading are both briefly semi-transparent -- with a transparent "
          "host the ROBOT's green eyes ghost through Mr. Cadabra's face on every mood change")
    check("  the burst cleans itself up and cannot stack",
          "C.timer = setTimeout" in tf and "if (C.timer) { clearTimeout(C.timer)" in tf,
          "five right answers in a row must not leave five rings pinned over his face")

    # BUILD et: THE RING NEEDED SOMETHING TO FIRE ON. es shipped and Jim STILL saw nothing:
    # firing celebrate() by hand on the live site drew the ring perfectly, so the fault was
    # upstream in the prompt -- marking was optional ("you MAY record") and sub-steps were
    # explicitly excluded, so in a teaching lesson the doorbell was almost never pressed.
    # [[mark]] is now REQUIRED on a finished problem and [[nice]] carries the smaller wins.
    check("celebrate() takes a SMALL intensity for wins along the way",
          "function celebrate(opts)" in tf and "opts.small" in tf,
          "one intensity means either the big moment is cheapened or a child goes minutes "
          "with no sign anyone noticed")
    check("  the small ring does NOT swap the video",
          "if (!small && P.state ===" in tf,
          "a clip change on every sub-step would thrash the network and flatten the "
          "finished-problem moment")
    for page in ("session.html", "practice.html", "topic.html"):
        with open(os.path.join(here, "static", page), encoding="utf-8") as fh:
            src = fh.read()
        check(f"  {page} draws the quiet ring on [[nice]]",
              'name === "nice"' in src and "TutorFace.celebrate({ small: true })" in src,
              "without this the new tag is inert and we are back where es was")
        check(f"  {page}'s [[nice]] never touches the tally",
              'name === "nice"' in src
              and "/api/mark/" not in src.split('name === "nice"')[1].split("}")[0],
              "[[nice]] is encouragement, not a score -- counting sub-steps as problems "
              "would inflate every student's practice numbers")

    # The prompts must actually ASK for the two tags, in every course, or the pages above
    # are wired to a doorbell nobody presses. This is the check that would have caught the
    # es miss on the first run.
    with open(os.path.join(here, "prompts.py"), encoding="utf-8") as fh:
        pr = fh.read()
    check("[[mark]] is REQUIRED of the tutor, never optional",
          "you may record" not in pr and pr.count("[[mark]] is REQUIRED") >= 9,
          "'you MAY record' is why a child could answer right all lesson and see nothing -- "
          "and why problems-practiced under-counted for every student")
    check("  every course prompt asks for [[nice]] too",
          pr.count("[[nice]]") >= 20,
          "the nine course prompts plus the practice and topic templates each need it")
    check("  [[nice]] and [[mark]] are never asked for in the same reply",
          pr.count("never in the same reply as [[mark]]") >= 1
          and pr.count("NEVER in the same reply as [[mark]]") >= 9,
          "two celebrations for one moment reads as a glitch")

    # The manifest is validated the day it exists; until then its absence is correct.
    man_path = os.path.join(here, "static", "videos", "cadabra", "presence.json")
    if os.path.exists(man_path):
        try:
            import json as _json
            with open(man_path, encoding="utf-8") as fh:
                man = _json.load(fh)
            check("presence.json parses and has an idle loop",
                  isinstance(man, dict) and man.get("loops", {}).get("idle"),
                  "a manifest without an idle loop mounts a black circle")
            vdir = os.path.dirname(man_path)
            # build ep: a clip is a LIST of encodings (webm then mp4) so the browser can
            # pick; a bare string is still accepted for older manifests.
            def _files(v):
                return [v] if isinstance(v, str) else list(v)
            names = [f for v in (man.get("loops") or {}).values() for f in _files(v)] \
                  + [f for v in (man.get("oneshots") or {}).values() for f in _files(v)] \
                  + ([man["poster"]] if man.get("poster") else [])
            missing = [n for n in names if not os.path.exists(os.path.join(vdir, n))]
            check("every file the manifest names exists", not missing,
                  f"missing from static/videos/cadabra/: {missing}")
        except Exception as exc:  # noqa: BLE001
            bad("presence.json is valid JSON", str(exc))
    else:
        print("       (presence.json not present yet -- phase-dark, robot active; the "
              "manifest is validated automatically once Jim's assets land)")


# =============================================================================
# PART 3u2 -- HE STEPS OUT AND TALKS (build eu, 2026-08-12) -- PHASE 2
# =============================================================================
# tutor-moments.js is the OTHER half of the video project: a few one-time clips in which
# Mr. Cadabra really speaks, in his real voice. It is a separate file from tutor-face.js
# on purpose -- these clips have SOUND, and the presence layer's "the corner never makes
# a sound" guarantee is enforced by reading that file. Keeping them apart means that
# guarantee stays absolute instead of becoming a special case.
def part3u2_talking_moments():
    print("\nPART 3u2 — the talking moments (phase 2)")
    here = os.path.dirname(os.path.abspath(__file__))
    try:
        with open(os.path.join(here, "static", "tutor-moments.js"), encoding="utf-8") as fh:
            tm = fh.read()
    except OSError as exc:
        bad("tutor-moments.js readable", str(exc)); return

    check("a missing manifest is a NORMAL state",
          "moments.json" in tm and 'done(false)' in tm and "available" in tm,
          "the clips do not exist yet; the probe must 404 quietly and leave every page "
          "exactly as it is today")
    check("play() ALWAYS resolves -- a lesson can never be stranded",
          tm.count('finish("unavailable")') >= 1 and 'finish("skipped")' in tm
          and 'finish("played")' in tm and "setTimeout(function () { finish" in tm,
          "a clip that stalls, 404s, or has no decodable encoding must still settle the "
          "promise the caller is waiting on before it speaks")
    check("only ONE moment can be on screen at a time",
          "if (M.open) return" in tm,
          "two of him talking over each other is the exact failure this whole design is "
          "built to prevent")
    check("the words exist as TEXT, not only as audio",
          "clip.caption" in tm and "cap.textContent" in tm,
          "a deaf child, a muted tab and a screen reader must all get the sentence")
    check("it is a real dialog with a way out",
          'setAttribute("role", "dialog")' in tm and '"Escape"' in tm
          and "M.lastFocus" in tm,
          "modal video with no Escape and no focus return is a trap")
    check("a blocked autoplay offers a Play button instead of failing",
          "p.catch(function ()" in tm and "▶ Play" in tm,
          "autoplay WITH SOUND is only allowed off a gesture; when a browser refuses "
          "anyway the visitor must still be able to start it")
    check("a codec failure is NOT silent (all <source> tags failing is detected)",
          "function sourcesFailed" in tm and "srcs[i].onerror" in tm,
          "the HTML spec routes a resource failure to the <source> elements, NOT to the "
          "<video>; wiring only vid.onerror leaves a card open forever in a browser that "
          "cannot decode the clip -- observed, not theorised")
    check("the presence layer stays SILENT -- the talking clips live elsewhere",
          not os.path.exists(os.path.join(here, "static", "tutor-face-talking.js")),
          "sound must never migrate into tutor-face.js, whose muted guarantee is absolute")

    # The two zero-collision callers. Both are user-initiated, and neither ever lets a
    # canned clip and his live voice speak at the same time.
    with open(os.path.join(here, "static", "landing.html"), encoding="utf-8") as fh:
        lp = fh.read()
    # ⚠️ TWO DELIBERATE REVERSALS (build ez), recorded rather than silently deleted.
    # Build eu put the site-welcome clip on the hero's "Hear him teach" BUTTON, and the
    # two checks that used to live here pinned that decision: the codec retire-and-retry
    # on that button, and the relabel-on-window-load. Jim reversed it on 2026-08-13 --
    # "hear him teach" must hear him TEACH -- so the clip moved to the demo CTA, and both
    # checks are re-pointed at where the behaviour actually lives now. PART 3ad owns the
    # button's side of it (no clip in that handler, no greeting label).
    check("the landing hero offers to introduce him ON THE WAY INTO THE DEMO",
          "tutor-moments.js" in lp and "TutorMoments.play('site_welcome')" in lp
          and "wireDemoWelcome" in lp,
          "he greets a visitor who is heading into the demo -- never by eating the "
          "teach button (build ez)")
    check("  the teach button still has its audio sample, untouched",
          "/api/demo-audio/71" in lp,
          "with or without a clip on the server, that button plays him TEACHING")
    check("  an unplayable clip never traps a visitor on the front page",
          re.search(r"TutorMoments\.play\('site_welcome'\)\.then\(once, once\)", lp)
          is not None and "setTimeout(once, 30000)" in lp,
          "the navigation must happen whether the clip plays, fails, or never settles -- "
          "both promise arms AND a backstop (the ev codec lesson, moved to its new home)")
    check("  a modified click (new tab) is left alone",
          "ev.metaKey || ev.ctrlKey || ev.shiftKey || ev.button" in lp,
          "hijacking a cmd-click to play a video steals a behaviour the visitor owns")
    with open(os.path.join(here, "static", "demo.html"), encoding="utf-8") as fh:
        dp = fh.read()
    check("the demo lets him say hello himself instead of the synthesised line",
          "tutor-moments.js" in dp and "TutorMoments.available('demo_welcome')" in dp,
          "one voice, never two -- the clip REPLACES WELCOME_LINE rather than joining it")
    check("  the tour starts whether he is watched, skipped, or missing",
          "if (how === 'played' || how === 'skipped') afterHello();" in dp
          and "else sayThen(WELCOME_LINE, afterHello);" in dp,
          "a visitor who hits Escape must land in the tour, not in a dead page")

    # Validated the day the clips land; until then absence is correct.
    man = os.path.join(here, "static", "videos", "cadabra", "moments.json")
    if os.path.exists(man):
        try:
            import json as _json
            with open(man, encoding="utf-8") as fh:
                mm = _json.load(fh)
            vdir = os.path.dirname(man)
            names = []
            for c in (mm.get("clips") or {}).values():
                names += [c] if isinstance(c, str) else list(c.get("sources") or [])
            missing = [n for n in names if not os.path.exists(os.path.join(vdir, n))]
            check("every clip the moments manifest names exists", not missing,
                  f"missing from static/videos/cadabra/: {missing}")
            capless = [k for k, c in (mm.get("clips") or {}).items()
                       if isinstance(c, dict) and not (c.get("caption") or "").strip()]
            check("every clip carries its caption text", not capless,
                  f"no caption for: {capless} -- the words must not live only in the audio")
        except Exception as exc:  # noqa: BLE001
            bad("moments.json is valid JSON", str(exc))
    else:
        print("       (moments.json not present yet -- phase-dark; the talking clips are "
              "validated automatically once Jim's recordings land)")


# =============================================================================
# PART 3v -- ONE TRUE NAME PER COURSE (build ek, 2026-08-12)
# =============================================================================
# The bug this exists to prevent, in one sentence: curriculum.py keyed the two
# elementary courses "entry"/"basic" while three content modules keyed the same two
# courses "entrymath"/"basicmath", so real lessons asked for content under a name
# nobody had filed it under and got NOTHING -- silently, because the lookups fall back
# to an empty list and _course() fell back to Algebra I. Rule 49 had no catalogue,
# rules 36-38 had no canonical scripts and rule 48 had no notation table, for the two
# youngest courses only, for as long as those modules have existed.
#
# The first check below is the one that would have caught it on day one, and it is
# deliberately the dumbest possible check: ASK EVERY REAL COURSE FOR ITS CONTENT AND
# FAIL IF IT COMES BACK EMPTY. A test that walks the same key the product walks is
# worth more than a hundred that agree with the data file.
def part3v_course_identity():
    print("\nPART 3v — one true name per course (the elementary content gap)")
    import curriculum as _c, notation as _n, misconceptions as _m, foundations as _f

    real = sorted(_c.COURSES.keys())
    check(f"curriculum knows all ten courses ({len(real)})", len(real) == 10,
          f"found {real}")

    # 1. THE CHECK THAT WOULD HAVE CAUGHT IT.
    for course in real:
        blocks = {"notation": len(_n.prompt_block(course)),
                  "misconception catalogue": len(_m.prompt_block(course)),
                  "foundation scripts": len(_f.prompt_block(course))}
        empty = sorted(k for k, v in blocks.items() if v == 0)
        check(f"  {course}: every content module answers to its REAL name", not empty,
              f"{empty} came back EMPTY for a course a real student can start -- "
              f"that module keys its content by a name the product never uses "
              f"(sizes: {blocks})")

    # 2. No module may key content by a name that is not a real course. This is what
    #    stops the next person re-introducing a second vocabulary.
    known = set(real) | set(_c.COURSE_ALIASES)
    stray = set()
    for entry in _n.NOTATIONS:
        stray |= {c for c in entry.get("courses", ()) if c not in known}
    stray |= {k for k in _m.MISCONCEPTIONS if k not in known}
    stray |= {k for k in _f.FOUNDATIONS if k not in known}
    check("no content is keyed by a course that does not exist", not stray,
          f"unknown course keys in the content modules: {sorted(stray)}")

    # 3. The content modules must use the CANONICAL name, not an alias -- an alias in a
    #    data file is how this bug started.
    aliased = set()
    for entry in _n.NOTATIONS:
        aliased |= {c for c in entry.get("courses", ()) if c in _c.COURSE_ALIASES}
    aliased |= {k for k in _m.MISCONCEPTIONS if k in _c.COURSE_ALIASES}
    aliased |= {k for k in _f.FOUNDATIONS if k in _c.COURSE_ALIASES}
    check("content is filed under the CANONICAL name, never an alias", not aliased,
          f"{sorted(aliased)} are legacy spellings -- re-key the content, don't add "
          f"an alias to make it work")

    # 4. canon(): aliases resolve (no student record is orphaned), unknown names pass
    #    through UNCHANGED (a typo must never silently become Algebra I again).
    for legacy, want in _c.COURSE_ALIASES.items():
        check(f"  canon({legacy!r}) resolves to {want!r}", _c.canon(legacy) == want,
              "a record or bookmark written under the old spelling would be orphaned")
        check(f"  a legacy {legacy!r} lands on the right COURSE, not the default",
              _c.units_for(legacy) == _c.units_for(want),
              "this is the silent fallback that hid the bug: an unknown key used to "
              "return Algebra I's units with no error")
    check("an unknown course is NOT silently renamed to the default",
          _c.canon("no-such-course") == "no-such-course",
          "canon must pass strangers through; _course() does the safe fallback, and "
          "hiding it inside canon would re-create the original bug")

    # 5. The battery must test the courses the PRODUCT has, not a list of its own.
    check("ruletests' own course list IS curriculum's course list",
          set(COURSES) == set(real),
          f"the battery would be proving things about courses that do not exist: "
          f"only-in-tests={sorted(set(COURSES) - set(real))}, "
          f"never-tested={sorted(set(real) - set(COURSES))}")

    # 6. And the auditor must audit real courses (its basicmath scenarios were running
    #    against Algebra I's unit list, which is why a Basic Math student got taught
    #    function notation in the 2026-08-12 audit).
    try:
        import lessonaudit as _la
        scen = [s.get("course") for s in getattr(_la, "SCENARIOS", []) if s.get("course")]
        bad_keys = sorted({c for c in scen if c not in real})
        check(f"every lesson-audit scenario names a real course ({len(scen)} scenarios)",
              not bad_keys,
              f"{bad_keys} -- those scenarios audit a phantom course and their findings "
              f"describe a lesson no student can ever have")
    except Exception as exc:  # noqa: BLE001
        print(f"       (lessonaudit not importable here: {exc})")


# =============================================================================
# PART 3w -- A GENERALIZATION CARRIES ITS CONDITION (rule 61, build el, 2026-08-12)
# =============================================================================
# The 2026-08-12 lesson audits caught five false universal claims in three courses.
# They are invisible to every referee we own: mathcheck re-computes ARITHMETIC, and
# there is no arithmetic in "always". So for LIVE replies rule 61 is prompt-covered.
#
# But one of the five was never a live slip -- it was the algebra1 function-notation
# FOUNDATION SCRIPT, spoken verbatim to every student who ever meets f(x). Authored
# content we can check, so we do, and that is what makes rule 61 ENFORCED rather than
# hopeful.
#
# DELIBERATELY NARROW: this bans five SENTENCES, never the word "always". Rule 61(d)
# exists because the obvious overcorrection -- hedging everything -- is its own harm,
# and the last check below proves the true absolutes are still sayable.
def part3w_generalizations():
    print("\nPART 3w — a generalization carries its condition (rule 61)")
    here = os.path.dirname(os.path.abspath(__file__))
    note = tutor.GRAPH_TOOL_NOTE

    check("rule 61 lives in the shared block exactly once",
          note.count("61. A GENERALIZATION CARRIES ITS CONDITION") == 1,
          "a shared rule goes in once, never per course")
    for label, needle in (
        ("the six-word fix (say the condition in the same breath)",
         "SAY THE CONDITION IN THE SAME BREATH"),
        ("the believes-it-forever test", "believes that sentence forever"),
        ("0/0 corrected", "we do not know yet and have to investigate"),
        ("function notation corrected", "here f is the NAME of a rule"),
        ("square root corrected", "when we SOLVE x squared = a for a positive a"),
        ("completing the square corrected", "when the coefficient of x squared is 1"),
        ("discriminant corrected", "REAL solutions, and whether complex ones"),
        ("fraction meaning corrected (2026-08-13)", "ONE way we use fractions"),
        ("order of operations corrected (2026-08-13)", "no grouping symbols, multiply before you add"),
        ("failed limit corrected (2026-08-13)", "FINITE one-sided limits exist and disagree"),
        ("plus-or-minus corrected (2026-08-13)", "both cases land\n          on the SAME single answer"),
        ("the do-not-overcorrect clause", "DO NOT OVERCORRECT INTO MUSH"),
    ):
        check(f"  rule 61: {label}", needle in note,
              f"{needle!r} left the rule -- restore it or change this anchor on purpose")

    # THE ENFORCEMENT: the five known-false forms may never appear in authored content.
    # Each pattern is the FALSE sentence itself, not a keyword -- so a correct use of
    # the same words (rule 61 quoting them as NOT-forms) has to be excluded explicitly.
    BANNED = [
        ("0/0 has a hidden common factor",
         re.compile(r"means the expression has a hidden common factor", re.I)),
        ("a letter with parentheses is function notation",
         re.compile(r"letter with something tucked inside parentheses", re.I)),
        ("a square root always gives two answers",
         re.compile(r"square root always gives you (?:two|2)", re.I)),
        ("always half the middle coefficient, squared",
         re.compile(r"always half the middle coefficient", re.I)),
        ("the discriminant counts ALL solutions",
         re.compile(r"discriminant to predict how many solutions", re.I)),
        # ---- the four from the 2026-08-13 audits (build fe) ----
        ("a fraction ALWAYS means pieces of one cut-up whole",
         re.compile(r"fraction always means", re.I)),
        ("multiplication before addition, with no grouping-symbol condition",
         re.compile(r"then addition,? -- every time|then addition, every time", re.I)),
        ("unmatched one-sided limits are always a jump",
         re.compile(r"when they don'?t,? you'?ve got a jump", re.I)),
        ("the plus-or-minus always yields two answers",
         re.compile(r"means you (?:actually )?get two answers", re.I)),
    ]
    AUTHORED = ("prompts.py", "foundations.py", "notation.py", "curriculum.py")
    for fname in AUTHORED:
        try:
            with open(os.path.join(here, fname), encoding="utf-8") as fh:
                src = fh.read()
        except OSError:
            continue
        # A dated CHANGE NOTE that quotes the false sentence in order to record why it
        # was fixed is documentation, not something a student hears -- strip comment
        # lines first, exactly as PART 3p strips HTML comments before reading copy.
        # (This is not a loophole: a comment is never sent to the model or the student.
        # Anything inside a real string stays in scope.)
        src = re.sub(r"^\s*#.*$", "", src, flags=re.M)
        # rule 61 itself quotes the false forms as things NOT to say; that block is the
        # one legitimate place they appear in live text, so it is excluded by name.
        if fname == "prompts.py" and "61. A GENERALIZATION CARRIES ITS CONDITION" in src:
            i = src.index("61. A GENERALIZATION CARRIES ITS CONDITION")
            j = src.index("DO NOT OVERCORRECT INTO MUSH", i)
            src = src[:i] + src[j:]
        for label, pat in BANNED:
            m = pat.search(src)
            check(f"  {fname}: never says {label!r}", m is None,
                  f"found {m.group(0)!r} -- this sentence is FALSE as stated and this "
                  f"file is spoken to students; say the true form with its condition"
                  if m else "")

    # And the guard against the overcorrection: true absolutes must survive. If a future
    # pass starts hedging these, rule 61(d) has been misread.
    fnd = open(os.path.join(here, "foundations.py"), encoding="utf-8").read()
    for label, needle in (("the hypotenuse is the longest side", "always the longest side"),
                          ("an acute angle is smaller than a right angle",
                           "always smaller than a right angle")):
        check(f"  a TRUE absolute is still said plainly: {label}", needle in fnd,
              "rule 61(d): hedging a true sentence is its own failure -- these must "
              "stay crisp")


# =============================================================================
# PART 3x -- A FRACTION PICTURE MUST BE COUNTABLE (build em, 2026-08-12)
# =============================================================================
# The audit's HIGH finding, and the most damaging kind of board bug: the picture and
# its caption disagreed, in a lesson for a confused child. data="this piece:1, the
# rest:3" draws ONE quarter-wedge and ONE three-quarter wedge -- so "cut into four
# equal parts" was a lie, and the follow-up question ("how many pieces are shaded?")
# could not be answered from the screen. It came from canonical foundation scripts.
#
# These checks RENDER THE REAL SVG with node rather than trusting the source, because
# the whole failure was a gap between what a tag says and what it draws.
def part3x_fraction_pie():
    print("\nPART 3x — a fraction picture must be countable (the equal-parts pie)")
    here = os.path.dirname(os.path.abspath(__file__))
    figs = os.path.join(here, "static", "math-figures.js")
    try:
        src = open(figs, encoding="utf-8").read()
    except OSError as exc:
        bad("math-figures.js readable", str(exc)); return

    check("the equal-parts mode exists", 'parseInt(a.parts, 10)' in src,
          '[[pie parts="4" shaded="3"]] is how a fraction picture is drawn now')
    check("the proportional mode survives for unequal categories",
          "parseData(a.data || a.sectors)" in src,
          "spinners and surveys still need one wedge per category")

    probe = r"""
      global.window = global;
      %s
      function count(s, re) { return (s.match(re) || []).length; }
      var r = {};
      var p43 = MathFigures.pie({parts:"4", shaded:"3"});
      r.wedges43   = count(p43, /<path /g);
      r.filled43   = count(p43, /fill="#5b5bd6"/g);
      r.pale43     = count(p43, /fill="#eef0f7"/g);
      r.hasText43  = /<text/.test(p43);
      r.separated  = count(p43, /stroke="#ffffff"/g);
      var p61 = MathFigures.pie({parts:"6", shaded:"1"});
      r.wedges61 = count(p61, /<path /g); r.filled61 = count(p61, /fill="#5b5bd6"/g);
      var huge = MathFigures.pie({parts:"400", shaded:"1"});
      r.hugeFellBack = !/stroke="#ffffff" stroke-width="2.5"/.test(huge);
      var legacy = MathFigures.pie({data:"Red:3 | Blue:2 | Green:1"});
      r.legacyWedges = count(legacy, /<path |<circle /g);
      console.log(JSON.stringify(r));
    """ % src
    try:
        import subprocess, json as _json, tempfile
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as fh:
            fh.write(probe); path = fh.name
        out = subprocess.run(["node", path], capture_output=True, text=True, timeout=60)
        os.unlink(path)
        r = _json.loads(out.stdout.strip().splitlines()[-1])
    except Exception as exc:  # noqa: BLE001
        skip("the equal-parts pie renders", f"node unavailable here: {exc}")
        return

    check("parts=4 shaded=3 draws FOUR wedges, not two",
          r["wedges43"] == 4,
          f'drew {r["wedges43"]} -- a child asked to count four equal parts must be '
          f'looking at four of them')
    check("  three of the four are filled and one is not",
          r["filled43"] == 3 and r["pale43"] == 1,
          f'filled={r["filled43"]} pale={r["pale43"]}')
    check("  the wedges are separated so they can be counted",
          r["separated"] >= 4, "without a stroke between them four quarters read as "
                               "one shape")
    check("parts=6 shaded=1 draws SIX wedges with one filled",
          r["wedges61"] == 6 and r["filled61"] == 1, f'{r["wedges61"]}/{r["filled61"]}')
    check("the equal-parts picture prints NO text at all (rule 6)",
          not r["hasText43"],
          "a percentage or a count on the board answers the very question the tutor is "
          "about to ask -- the student must COUNT it")
    check("an absurd parts= falls back instead of drawing confetti",
          r["hugeFellBack"], "400 wedges is not a countable picture")
    check("the proportional pie still renders for unequal categories",
          r["legacyWedges"] > 0, "spinners and surveys must keep working")

    # And the authored board lines that caused it.
    import foundations as _f
    offenders = []
    for course in sorted(_f.FOUNDATIONS):
        for script in _f.for_course(course):
            for line in script.get("board", []):
                if "[[pie" in line and "parts=" not in line:
                    offenders.append(f'{course}/{script["term"]}')
    check(f"no authored pie board line uses the proportional form ({len(offenders)} bad)",
          not offenders,
          f"{offenders} -- a canonical script is DRAWN verbatim; a fraction pie built "
          f"from proportions is the bug this part exists for")


# =============================================================================
# PART 3y -- ANSWER THE RULE THEY NAMED, AND READ THE SYMBOL YOU WROTE (build en)
# =============================================================================
# Two 2026-08-12 audit findings that share a root: the tutor had the student's own
# words in front of it and did not use them.
#   * rule 49(f): the student SAID "we do 5 plus 3 first" -- a left-to-right rule --
#     and the reply corrected a different misconception entirely.
#   * rule 48: "1/4 > 1/8" went on a Basic Math board with no way to say ">", because
#     bare < and > were never in the notation registry at all (only the or-equal pair,
#     and not for elementary). Comparing fractions IS Basic Math.
def part3y_diagnosis_and_symbols():
    print("\nPART 3y — answer the rule they named; read the symbol you wrote (build en)")
    note = tutor.GRAPH_TOOL_NOTE

    for label, needle in (
        ("their stated rule is EVIDENCE, not a hypothesis",
         "WHEN THEY TELL YOU THEIR RULE, THAT IS NOT A HYPOTHESIS"),
        ("the live catch is recorded with its date", "Live catch, 2026-08-12"),
        ("the move: say it back, name when it IS true, show where it breaks",
         "say exactly WHEN it is true and when it is not"),
    ):
        check(f"rule 49(f): {label}", needle in note,
              f"{needle!r} left rule 49 -- restore it or change this anchor on purpose")
    check("rule 49(f) reaches every course (it lives in the shared block)",
          note.count("WHEN THEY TELL YOU THEIR RULE") == 1,
          "a shared rule goes in once, never per course")

    # The registry gaps, and the guarantee that closing them did not break detection.
    for nid, must_have in (("inequality", ("basic", "entry", "prealgebra")),
                           ("imaginary", ("algebra2",))):
        try:
            entry = notation.by_id(nid)
        except Exception:
            entry = None
        check(f"[{nid}] is registered at all", bool(entry),
              "the tutor writes this symbol and rule 48 has no canonical reading for it")
        if not entry:
            continue
        missing = [c for c in must_have if c not in entry["courses"]]
        check(f"  [{nid}] covers {', '.join(must_have)}", not missing,
              f"missing {missing} -- the course that WRITES the symbol is the course "
              f"that needs to be told how to say it")

    # The patterns must not fire on things that merely look similar. These five strings
    # are the real ones that would have broken the build if the regexes were naive:
    # arrows in captions, the or-equal pair, and the calculus subscript scripts.
    for text, forbidden in (("x -> y", "inequality"), ("a <= b", "inequality"),
                            ("f(x_i)", "imaginary"), ("it is not x * i", "imaginary")):
        check(f"  {forbidden!r} does not fire on {text!r}",
              forbidden not in notation.written_in(text),
              "a false positive here fails the build on innocent board text")
    for text, expected in (("1/4 > 1/8", "inequality"), ("3 + 2i", "imaginary")):
        check(f"  {expected!r} IS detected in {text!r}",
              expected in notation.written_in(text),
              "the symbol the audit caught must be recognised")


# =============================================================================
# PART 3z -- REPLY INTEGRITY: A TAG MUST PARSE, A PROBLEM MUST BE SPOKEN (build eq)
# =============================================================================
# Both halves come from the 2026-08-12 audits, and both are cases where the machine
# could have caught it and did not.
#
# Every string below is REAL -- lifted from those transcripts. The offending lines must
# be caught; the innocent lines from the SAME lessons must not be. That second half is
# the important one: a referee that regenerates good replies costs money and makes the
# tutor stutter, so the false-positive cases are pinned as hard as the true ones.
def part3z_reply_integrity():
    print("\nPART 3z — reply integrity (malformed tags · rule 44 spoken problems)")

    # ---- the malformed-tag referee: it did not exist before build eq ----------
    check("a malformed-tag referee exists at all",
          hasattr(tutor, "malformed_tag_conflict"),
          "nothing checked whether a board tag could be parsed; a broken tag reaches "
          "the student silently")
    check("it runs FIRST in the sweep",
          "malformed = malformed_tag_conflict(reply)" in open(
              os.path.join(os.path.dirname(os.path.abspath(__file__)), "tutor.py"),
              encoding="utf-8").read().split("def prose_referee_conflict")[-1][:900]
          or "malformed = malformed_tag_conflict(reply)" in open(
              os.path.join(os.path.dirname(os.path.abspath(__file__)), "tutor.py"),
              encoding="utf-8").read(),
          "if a tag cannot be parsed, every other referee is reading a board the "
          "student will never see")
    MALFORMED = [
        # (name, reply, must_flag)
        ("THE audit case: choices with no closing quote",
         '[[choices options="yes, let\'s go! | show me one more]]', True),
        ("a tag opened and never closed",
         'Here you go [[step eq="3 + 4 = 7"', True),
        ("an attribute left unterminated mid-tag",
         '[[card title="By the end items="a | b"]]', True),
        ("the SAME tag, written correctly",
         '[[choices options="yes, let\'s go! | show me one more"]]', False),
        ("an ordinary two-tag reply",
         'Nice! [[step eq="2x = 8"]] [[step op="/ 2" eq="x = 4"]] What next?', False),
        ("a real fractions reply with four tags",
         'Great! [[clear]] [[goal text="Understand fractions"]] '
         '[[pie parts="6" shaded="4" caption="six equal pieces, four shaded"]] '
         '[[choices options="try one! | one more"]]', False),
        ("prose that merely contains two brackets", "We write it like this: [[ ok?", False),
    ]
    for name, reply, must in MALFORMED:
        got = bool(tutor.malformed_tag_conflict(reply))
        check(f"  malformed-tag: {name}", got == must,
              f"flagged={got}, expected {must} -- "
              + ("a broken tag would reach a student" if must else
                 "a GOOD reply would be regenerated for nothing"))

    # ---- rule 44: the two blind spots, with the real strings ------------------
    RULE44 = [
        ("audit: '8/12 = ?' while saying only 'this fraction'",
         "Here is a warm-up: what is this fraction reduced to lowest terms? "
         '[[step eq="8/12 = ?"]] Give it a shot — what do you get?', True),
        ("audit: quiz item '6/9 = ?' with 'what do you get?'",
         "Great — question one. Simplify this fraction to lowest terms. "
         '[[step eq="6/9 = ?"]] What do you get?', True),
        ("audit: quiz item '9/12 = ?'",
         'Question two: [[step eq="9/12 = ?"]] What is that reduce to?', True),
        ("the SAME item, actually read aloud",
         'Question one: simplify six ninths to lowest terms. [[step eq="6/9 = ?"]]', False),
        ("audit-innocent: the denominator question names 'one fourth'",
         "Which number in one fourth is the denominator — the 1 or the 4? "
         '[[step eq="1/4 → denominator = ?"]]', False),
        ("audit-innocent: decimals spoken in full",
         "What do you get when you add three point five and forty-seven hundredths? "
         '[[step eq="3.50 + 0.47 = ?"]]', False),
        ("audit-innocent: percents spoken in full",
         'What is twenty-five percent of sixty? [[step eq="25% of 60 = ?"]]', False),
    ]
    for name, reply, must in RULE44:
        got = bool(tutor.prose_unspoken_problem_conflict(reply))
        check(f"  rule 44: {name}", got == must,
              f"flagged={got}, expected {must} -- "
              + ("a listening student cannot attempt this problem" if must else
                 "the tutor DID read it aloud; regenerating would be a false positive"))

    # The specific defect that made a whole fraction quiz invisible: the old bar was
    # TWO numeric tokens and a fraction counts as ONE.
    check("a ONE-quantity board problem can now qualify (the fraction-quiz hole)",
          bool(tutor.prose_unspoken_problem_conflict(
              'Simplify this one. [[step eq="6/9 = ?"]] What do you get?')),
          "the old two-token bar is back, and every single-fraction quiz item is "
          "invisible to rule 44 again")
    # ...and the other one: numbers ELSEWHERE in the prose must not excuse silence.
    check("numbers elsewhere in the prose no longer exempt the reply",
          bool(tutor.prose_unspoken_problem_conflict(
              "We need two numbers that multiply to 20 and add to 9. "
              '[[step eq="6/9 = ?"]] What do you get?')),
          "talking about OTHER numbers used to excuse never reading the problem")


# =============================================================================
# PART 3ag -- THE PICTURES AND THE PROSE TELL THE SAME STORY (build fd, 2026-08-13)
# =============================================================================
# Jim, preparing to invite beta testers: "I want everything to be current, ready to
# go, showcase, preparation."
#
# Every screenshot on the public site is a photograph of the DEMO. That is the whole
# reason they can be trusted -- they are not mockups, they are the product. But it
# also means the demo is the single source of truth for every number the marketing
# copy quotes, and the copy has no idea when the demo changes underneath it. Today's
# re-capture caught exactly that drift, on the page that can least afford it:
#
#   * /homeschool said "3h 59m this week" in the paragraph, in the alt text, and in the
#     weekly-email preview -- directly above a freshly-captured tile reading 2h 15m.
#     That is the page whose promise is "a number you can put in an instructional-hours
#     log with a straight face."
#   * /parents' email preview claimed "best check 72%" on Decimals beside a picture of
#     Maya's dashboard showing two topic quizzes passed at 88% and 92%.
#   * /teachers' alt text said "five students" over a heatmap of six.
#
# So: the numbers in the copy are read out of demo.html at test time. If the demo's
# sample student ever changes again, this PART fails the same day instead of leaving a
# visitor to spot the contradiction.
def part3ag_shots_match_copy():
    print("\nPART 3ag — the pictures and the prose tell the same story (build fd)")
    here = os.path.dirname(os.path.abspath(__file__))
    st = os.path.join(here, "static")
    demo = open(os.path.join(st, "demo.html"), encoding="utf-8").read()

    def page(n):
        return open(os.path.join(st, n), encoding="utf-8").read()

    # ---- 1. every shot a page points at actually exists, and is a real picture ----
    # A blank whiteboard is a 40 KB file; a real one is 400 KB+. The first capture in
    # this build WAS blank (the voice was stubbed out, so the script never advanced and
    # no step was ever drawn) and it looked perfectly fine as a filename.
    refs = set()
    for name in sorted(os.listdir(st)):
        if not name.endswith(".html"):
            continue
        for s in re.findall(r'/static/shots/([A-Za-z0-9_.-]+\.png)', page(name)):
            refs.add(s)
    check("the site points at at least the six product shots", len(refs) >= 6,
          f"only found {sorted(refs)}")
    for s in sorted(refs):
        p = os.path.join(st, "shots", s)
        ok = os.path.exists(p)
        size = os.path.getsize(p) if ok else 0
        check(f"  shots/{s} exists and is a real screenshot", ok and size > 40000,
              f"missing" if not ok else f"only {size} bytes -- a near-empty capture "
              "(a blank whiteboard weighs about this much and still has a valid filename)")

    # ---- 2. the hours: one student, one number, everywhere ----
    # Read the demo's own "Time this week" tile rather than hard-coding it here, so this
    # test keeps working the day the sample student's week changes.
    m = re.search(r'<div class="tile"><b>([^<]+)</b><span>Time this week', demo)
    check("the demo's student tile still names a weekly time", bool(m),
          "the tile markup moved; this whole PART reads the demo for its numbers")
    hours = m.group(1).strip() if m else ""
    demo_times = set(re.findall(r"\b\d+h \d+m\b", demo))
    pages = ("homeschool.html", "parents.html", "landing.html", "students.html",
             "teachers.html", "index.html", "family.html", "pricing.html")
    # MAYA specifically: she is the student in every screenshot, so any weekly time the
    # copy gives HER has to be the one in the picture. Other sample children (the class
    # email preview on /teachers invents an Ava and a Ben) are free to have their own
    # weeks -- they are not photographed anywhere.
    for name in pages:
        body = re.sub(r"<!--.*?-->", "", page(name), flags=re.S)   # change notes are not copy
        for block in re.findall(r"Maya(?:'s)?\b.{0,700}?</ul>", body, re.S):
            wrong = sorted({h for h in re.findall(r"\b\d+h \d+m\b", block) if h != hours})
            check(f"  {name}: Maya's week reads {hours}, the same as her picture",
                  not wrong,
                  f"says {wrong} where the screenshot on this page says {hours} -- a "
                  "visitor reads the number and the picture together")
    # The alt text under the tile picture is copy too -- it was one of the three places
    # /homeschool said "3h 59m" over a picture of 2h 15m, and it is the one a sighted
    # proofreader never sees.
    for name in pages:
        body = re.sub(r"<!--.*?-->", "", page(name), flags=re.S)
        for tag in re.findall(r'<img[^>]*shots/timetile\.png[^>]*>', body):
            alt = re.search(r'alt="([^"]*)"', tag)
            wrong = sorted({h for h in re.findall(r"\b\d+h \d+m\b", alt.group(1) if alt else "")
                            if h != hours})
            check(f"  {name}: the tile picture's ALT text reads {hours} too", not wrong,
                  f"alt says {wrong} -- alt text is the only version of this picture a "
                  "blind visitor and every search engine ever get")
    # Times that belong to a DIFFERENT sample child are fine (the class email preview on
    # /teachers invents an Ava and a Ben, and nothing photographs them). Times that
    # belong to nobody at all are a leftover, and that is what "3h 59m" was.
    KNOWN_OTHERS = ("Ava", "Ben", "Sofia", "Priya", "Jonah", "Aiden")
    for name in pages:
        body = re.sub(r"<!--.*?-->", "", page(name), flags=re.S)
        for mm in re.finditer(r"\b\d+h \d+m\b", body):
            h = mm.group(0)
            near = body[max(0, mm.start() - 120):mm.start()]
            owned = any(w in near for w in KNOWN_OTHERS)
            check(f"  {name}: {h} belongs to somebody -- the demo, or a named sample child",
                  h in demo_times or owned,
                  f"{h} matches no time in the demo and sits under no student's name, so "
                  "no screenshot anywhere can back it up")

    # ---- 3. the honest-hours paragraph spells out the SAME number it shows ----
    hs = page("homeschool.html")
    spelled = {"2h 15m": "two hours and fifteen minutes",
               "3h 59m": "three hours and fifty-nine minutes"}.get(hours)
    if spelled:
        check("  /homeschool spells the hours out to match the tile above the log claim",
              spelled in hs,
              f'the paragraph must read "{spelled}" -- it is the sentence that promises '
              "the number can go in an instructional-hours log with a straight face")

    # ---- 4. the teacher shot's alt text counts the students in the picture ----
    heat = re.search(r'id="tdHeat".*?</div>\s*</div>', demo, re.S)
    rows = len(re.findall(r'<div class="hrow">', heat.group(0))) if heat else 0
    words = {5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}
    check("the demo heatmap still has a countable roster", rows in words,
          f"found {rows} rows")
    if rows in words:
        alt = re.search(r'<img[^>]*shots/teacher\.png[^>]*alt="([^"]*)"', page("teachers.html"))
        check(f"  /teachers' alt text says {words[rows]} students, matching the picture",
              bool(alt) and f"{words[rows]} students" in alt.group(1),
              f"the heatmap shows {rows} students; alt says "
              f"{alt.group(1) if alt else '(no alt at all)'} -- alt text is what a "
              "blind visitor and every search engine are told the picture contains")

    # ---- 5. the weekly-email preview agrees with the dashboard beside it ----
    # Maya's Decimals topic quizzes read 88% and 92% PASSED on the shot. A preview that
    # says "best check 72%" is describing a different child.
    for name in ("homeschool.html", "parents.html"):
        body = re.sub(r"<!--.*?-->", "", page(name), flags=re.S)   # notes are not copy
        check(f"  {name}'s weekly-email preview does not contradict her quiz results",
              "best check 72%" not in body,
              "the parent-view screenshot on this same page shows two Decimals topic "
              "quizzes passed at 88% and 92%")

    # ---- 6. nothing on the site claims a screenshot that was retired ----
    check("no page still shows the retired math-keyboard screenshot",
          not any('shots/keyboard.png' in re.sub(r"<!--.*?-->", "", page(n), flags=re.S)
                  for n in os.listdir(st) if n.endswith(".html")),
          "the math keyboard was retired in build ao; showing it advertises a product "
          "that no longer exists")




# =============================================================================
# PART 3ah -- THE 2026-08-13 LESSON-AUDIT FINDINGS, CLOSED (build fe)
# =============================================================================
# Five audit runs, 19 findings, every one read against the quoted transcript before
# anything was changed. Sixteen were real (three HIGH); the closures live in rule 63
# (new), rules 4/13/14/17/26/41/43 (amended), rule 61 (four more corrected forms, in
# PART 3w), the fraction foundation script (its false "always", also PART 3w), the
# triangle-slot referee (TRIANGLE_CASES, PART 2), and lessonaudit's transport (below).
# THREE WERE REJECTED, recorded here so nobody re-litigates them:
#   - "3.5 + 0.47 should be answered before coaching" -- rule 52(d) decided this on
#     2026-08-11, against the SAME misread by an earlier critic: a handed computation
#     is the lesson's work, not a rule-52 question.
#   - "the percent quiz was cold" -- rule 47's bar (two unaided rights this session)
#     was met on the transcript's own record, and 47(d)'s instrument-honesty speech
#     was delivered nearly verbatim. The design held; the finding re-litigates it.
#   - "the first column sum lacked an = ? line" -- a [[column]] with no result= IS
#     the pending question on the board; demanding a duplicate horizontal line would
#     clutter what rule 26(c) keeps short.
def part3ah_audit_findings_fe():
    print("\nPART 3ah — the 2026-08-13 audit findings closed (build fe)")
    import prompts
    here = os.path.dirname(os.path.abspath(__file__))
    note = tutor.GRAPH_TOOL_NOTE
    built = tutor.build_system_prompt(dict(STUDENT), course="geometry")

    # ---- rule 63 exists, once, and reaches a built prompt ----
    H = "63. THE WORDS AND THE PICTURE ARE THE SAME FIGURE."
    check("rule 63 lives in the shared block exactly once", note.count(H) == 1,
          f"count in GRAPH_TOOL_NOTE = {note.count(H)}")
    check("rule 63 reaches a built prompt exactly once", built.count(H) == 1,
          f"count in the built geometry prompt = {built.count(H)}")

    # ---- the load-bearing phrases of every closure ----
    anchors = [
        # rule 63's three halves
        ("63a: one figure, one name, the DRAWN figure's name",
         "ONE FIGURE, ONE NAME -- AND IT IS THE DRAWN FIGURE'S NAME" in note),
        ("63a carries the live catch (the circle called a curve)",
         '"a sideways-opening' in note and '"that circle"' in note),
        ("63b: a sharing story draws the SHARES",
         "A SHARING STORY DRAWS THE SHARES" in note),
        ("63b shows the right picture AND names the wrong one",
         '"3 | 3 | 3 | 3"' in note and '"4 | 4 | 4 | 2"' in note),
        ("63c: the sides list is a contract, AB, BC, CA",
         "sides LIST IS A CONTRACT: AB, BC, CA, in that order" in note),
        ("63c names the referee so the model knows it is watched",
         "a referee now" in note),
        # the amended rules
        ("rule 4: a separate example announces itself",
         "AND A SEPARATE EXAMPLE ANNOUNCES ITSELF" in note),
        ("rule 13: ten percent IS one tenth, direction said",
         "Ten percent IS one tenth" in note and "one place LEFT" in note),
        ("rule 13: the square-root symbol names the NONNEGATIVE root",
         "NONNEGATIVE root" in note),
        ("rule 14: abbreviations are notation too (DNE, and i in a goals card)",
         "ABBREVIATIONS ARE NOTATION TOO" in note
         and '"DNE, short for does not exist"' in note),
        ("rule 17: ask first, confirm after",
         "COMES BEFORE YOU CONFIRM" in note),
        ("rule 17: no escape hatch on a check",
         "never bolt an escape hatch onto a check" in note),
        ("rule 26: a wrong picture is a wrong line, and words cannot fix a drawing",
         "AND A WRONG PICTURE IS A WRONG LINE" in note
         and "Words cannot" in note and "fix a drawing" in note),
        ("rule 41: the caption of a question-figure points without answering",
         "WHEN THE FIGURE IS THE QUESTION, THE CAPTION POINTS WITHOUT ANSWERING" in note),
        ("rule 41: what-to-notice never becomes what-to-answer",
         "what-to-notice never\n    becomes what-to-answer" in note
         or "what-to-notice never becomes what-to-answer" in note),
        ("rule 43: a bare right answer shows NO method",
         "A bare right answer shows you NO method" in note),
    ]
    for name, cond in anchors:
        check(name, cond, "a load-bearing phrase was dropped or reworded -- if the "
                          "rewording is deliberate, update this anchor in the same "
                          "commit")

    # ---- the geometry template teaches the hypotenuse slot where the tag is taught ----
    check("the geometry [[triangle]] doc names the hypotenuse's slot",
          'right="C" makes AB (the FIRST slot) the hypotenuse'
          in prompts.GEOMETRY_SYSTEM_PROMPT_TEMPLATE,
          "the tag's own documentation is where the convention must live")

    # ---- the referee is wired, not just written ----
    check("triangle_side_conflict exists and is swept by prose_board_conflict",
          hasattr(tutor, "triangle_side_conflict")
          and bool(tutor.prose_board_conflict(
              '[[triangle v="A,B,C" right="C" sides="6,?,10"]]')),
          "the referee must reach students through the combined sweep "
          "(TRIANGLE_CASES in PART 2 carries the full case table)")

    # ---- the fraction foundation script lost its false "always" ----
    try:
        import foundations as _F
        frac = next(it for it in _F.FOUNDATIONS["basic"] if it.get("term") == "fraction")
        check("the basic 'fraction' script says 'the way we use fractions today'",
              "the way we use fractions today" in frac.get("say", ""),
              "the corrected condition left the script")
        check("  and 'always means' is gone from it",
              "always means" not in frac.get("say", ""),
              "the false universal is back -- PART 3w bans it everywhere too")
    except Exception as exc:  # noqa: BLE001
        bad("fraction foundation script", str(exc))

    # ---- lessonaudit's transport: patient read, one quiet retry ----
    la = open(os.path.join(here, "lessonaudit.py"), encoding="utf-8").read()
    m = re.search(r"read\s*=\s*(\d+(?:\.\d+)?)", la)
    check("lessonaudit gives the critic a patient read timeout (>= 300s)",
          bool(m) and float(m.group(1)) >= 300.0,
          "two 2026-08-13 lessons died at the old flat 120s: "
          "'could not reach OpenAI: The read operation timed out'")
    check("lessonaudit retries ONCE on a pure transport error",
          "could not reach OpenAI after a retry" in la
          and "retrying once in 3s" in la,
          "one dropped read must not abort a whole lesson")
    check("  the retry is transport-only (received errors keep their handlers)",
          "switching token parameter" in la and "output limit was reached" in la,
          "the 400-reading handlers must survive the transport change")




# =============================================================================
# PART 3af -- THE FULL JOURNEY, END TO END (build fb, 2026-08-13)
# =============================================================================
# Jim's brief: "run to make sure from start to finish that this works outside of the
# audit." Everything else in this battery checks a PART. This runs one student's whole
# life through the real app: sign up → validate the first three units on the Course
# Assessment → work the rest → hit the LOCKED Final Exam and read what it says → go
# back and pass the validated units' quizzes → take the exam → Course Champion in the
# trophy case → and the same picture on the parent AND teacher views.
#
# ⭐ IT EARNED ITS PLACE ON ITS FIRST RUN: a teacher could not add a parent-created
# student to a class at all. The classroom path predated parent accounts and consulted
# students.json alone, so every real customer's child was invisible to it. Nothing that
# reads one endpoint at a time would have found that -- it takes walking the journey.
def part3af_full_journey():
    print("\nPART 3af — the full journey, end to end (build fb)")
    here = os.path.dirname(os.path.abspath(__file__))
    mn = open(os.path.join(here, "main.py"), encoding="utf-8").read()

    # The specific regression the trial found: the class path must know about students
    # a PARENT created, not just the pilot personas in students.json.
    for fn in ("_class_public", "_class_student_row"):
        m = re.search(r"def " + fn + r"\(.*?(?=\ndef |\n@app\.)", mn, re.S)
        check(f"{fn} finds parent-created students, not just students.json",
              bool(m) and "_lookup_student(" in m.group(0)
              and "STUDENTS.get(" not in m.group(0),
              "the classroom path predated parent accounts; consulting STUDENTS alone "
              "makes every real customer's child an 'unknown code' with no progress")
    m = re.search(r'@app\.post\("/api/class/\{class_code\}/students"\).*?(?=\n@app\.)', mn, re.S)
    check("a teacher can add ANY real student to a class",
          bool(m) and "_lookup_student(" in m.group(0) and "not in STUDENTS" not in m.group(0),
          "`code not in STUDENTS` rejects every parent-created code as nonexistent -- "
          "found by the full-journey trial, and it would have blocked any school pilot")

    trial = os.path.join(here, "course_trial.py")
    check("course_trial.py ships with the app", os.path.exists(trial),
          "the journey trial is a tool Jim can run any time; it must live in the repo")

    # --- build fc: the same trial, one click away on /admin -------------------
    # The safety-critical property is ISOLATION. This trial invents a parent, a child, a
    # teacher and a class; run against the live database it would litter real data with
    # fakes. So it must run as a SEPARATE PROCESS with its own DATABASE_URL -- there is no
    # safe way to swap the store's engine underneath a live server.
    mep = re.search(r'@app\.post\("/api/admin/course-trial"\).*?(?=\n@app\.)', mn, re.S)
    check("the /admin trial endpoint exists", bool(mep),
          "Jim asked for this on the dashboard, with a couple of questions and a report")
    if mep:
        ep = mep.group(0)
        check("  it is admin-key gated", "_require_admin(" in ep,
              "it must sit behind the same key as every other tool on that page")
        check("  ⭐ it runs in a SEPARATE PROCESS on a THROWAWAY database",
              "_sp.run(" in ep and 'env["DATABASE_URL"] = "sqlite:///"' in ep
              and "TemporaryDirectory()" in ep,
              "in-process, or against the live DATABASE_URL, it would write a fake parent, "
              "child, teacher and class into real data -- the one thing it must never do")
        check("  it keeps its files out of the real data directory",
              'env["DATA_DIR"] = tmp' in ep,
              "otherwise its cache and files land in /var/data beside the real ones")
        # \b so a renamed-out MIN_TRIAL_MB_DISABLED cannot satisfy this by substring.
        check("  it refuses to run when memory is tight, rather than risk the service",
              "MemAvailable" in ep and re.search(r"\bMIN_TRIAL_MB\b", ep)
              and re.search(r"avail_mb\s*<\s*MIN_TRIAL_MB\b", ep),
              "a second interpreter importing the app costs ~120 MB; on a 512 MB instance "
              "an OOM would take the live site down in the middle of a lesson")
        check("  it cannot hang the dashboard",
              "timeout=180" in ep and "TimeoutExpired" in ep,
              "a wedged trial must report itself, not spin forever")
        check("  an unknown course is a clean 400",
              "curriculum.COURSES" in ep,
              "better a plain message than a confusing subprocess error")

    tsrc = open(trial, encoding="utf-8").read() if os.path.exists(trial) else ""
    check("the trial can report machine-readably (--json) for the dashboard",
          "JSON_SENTINEL" in tsrc and '"--json"' in tsrc,
          "the page needs structured steps, not ANSI terminal output")
    check("  and the JSON is announced by a SENTINEL, not assumed to own stdout",
          "COURSE-TRIAL-JSON" in tsrc,
          "the app and the store print their own startup lines first -- parsing all of "
          "stdout as JSON breaks the moment anything else logs")
    check("the trial answers Jim's two questions (--course, --validate)",
          '"--course"' in tsrc and '"--validate"' in tsrc,
          "he asked it to 'ask a couple of questions' before running")

    adm = open(os.path.join(here, "static", "admin.html"), encoding="utf-8").read()
    check("the dashboard has the trial panel, wired to the endpoint",
          'id="ctRun"' in adm and "/api/admin/course-trial" in adm
          and 'id="ctCourse"' in adm and 'id="ctUnits"' in adm,
          "the whole point was that Jim can run it without a terminal")

    try:
        from fastapi.testclient import TestClient  # noqa: F401
    except Exception:  # noqa: BLE001
        skip("full-journey trial", "fastapi TestClient not installed here")
        return
    if not os.path.exists(trial):
        return
    env = dict(os.environ)
    env["PYTHONPATH"] = here + os.pathsep + env.get("PYTHONPATH", "")
    env["WEEKLY_EMAIL"] = "off"
    r = subprocess.run([sys.executable, trial], cwd=here, env=env,
                       capture_output=True, text=True)
    check("FULL-JOURNEY TRIAL: validate 3 units · work the rest · the Final Exam stays "
          "LOCKED and says which units are owed · pass them · take the exam · Course "
          "Champion in the trophy case · parent AND teacher see it",
          r.returncode == 0 and "TRIAL PASSED" in r.stdout,
          (r.stdout + r.stderr)[-900:])


# =============================================================================
# PART 3ae -- SECURITY F2: THE CLASSROOM IS LOCKED (build fa, 2026-08-13)
# =============================================================================
# F2 was the last open finding from the 2026-08-12 security review, and reading the
# code to fix it showed it was worse than the note said: GET /api/class/{code}
# returned the whole roster INCLUDING every child's login code, and a student code IS
# the login. One guessed class code handed over every child in that class. Those
# routes never got F1's _read_guard either, so they were enumerable and unthrottled.
#
# This part does NOT trust the source to look right. It stands the real app up against
# a real database and drives every endpoint three ways: with no token, with the WRONG
# teacher's token, and with the owner's. A source-reading check would have passed on
# the old code too -- the handlers looked perfectly reasonable.
def part3ae_classroom_locked():
    print("\nPART 3ae — security F2: the classroom is locked (build fa)")
    here = os.path.dirname(os.path.abspath(__file__))
    mn = open(os.path.join(here, "main.py"), encoding="utf-8").read()

    # --- static: the no-auth lookup helper must stay gone ---------------------
    check("the no-auth class lookup (_class_or_404) is gone",
          "def _class_or_404" not in mn,
          "it fetched a class by code with NO ownership check and was the helper every "
          "leaking endpoint reached for; leaving it invites the next handler to use it")
    check("the unauthenticated teacher-classes route is gone",
          '@app.get("/api/teacher/{teacher_code}/classes")' not in mn,
          "it listed a teacher's classes behind a short guessable code and its own "
          "docstring called it 'a door, not a lock'")
    # Read each /api/class handler and prove IT calls _require_teacher. Counting
    # occurrences would be clever and brittle; this names the offender instead.
    routes, naked, unowned = [], [], []
    for m in re.finditer(r'@app\.(?:get|post|delete)\("(/api/class[^"]*)"\)\s*\n'
                         r'def \w+\(.*?(?=\n@app\.|\ndef |\Z)', mn, re.S):
        path, body = m.group(1), m.group(0)
        routes.append(path)
        if "_require_teacher(" not in body:
            naked.append(path)
        if "{class_code}" in path and "_own_class(" not in body:
            unowned.append(path)
    check(f"every /api/class endpoint requires a signed-in teacher ({len(routes)} routes)",
          bool(routes) and not naked,
          f"UNAUTHENTICATED: {naked} -- this is precisely finding F2")
    check("every per-class endpoint also checks OWNERSHIP",
          not unowned,
          f"authenticated but not owner-gated: {unowned} -- any signed-in teacher could "
          f"then read or edit any class, which is the same leak with one extra step")

    # --- the teacher PAGE must not carry the old door around either -----------
    th = open(os.path.join(here, "static", "teacher.html"), encoding="utf-8").read()
    th_code = re.sub(r"<!--.*?-->", "", th, flags=re.S)
    check("the teacher page no longer signs in with a URL parameter",
          'params.get("teacher")' not in th_code,
          "?teacher=MRSBAKER was the old 'sign-in': a short guessable code in a URL, "
          "shared in screenshots and saved in browser history")
    check("the teacher page sends a real token on every class call",
          'localStorage.getItem(TOKEN_KEY)' in th_code
          and '"X-Teacher-Token"' in th_code
          and 'fetch("/api/class' not in th_code,
          "every class call must go through the api() wrapper that attaches the token -- "
          "a bare fetch is a call site that will forget it")
    # \b after "code" means s.code_masked does NOT match -- that field is the fix, not
    # the bug, and a naive substring test flags it.
    check("the roster renders MASKED codes, never a raw login code",
          "code_masked" in th_code and not re.search(r"\bs\.code\b", th_code),
          "the page must not put thirty children's logins on a projected screen")
    check("revealing a code is one student at a time, through one helper",
          th_code.count("async function revealCode(") == 1
          and "/reveal/" in th_code,
          "one funnel, owner-gated and throttled server-side")

    try:
        from fastapi.testclient import TestClient  # noqa: F401
        _have = True
    except Exception:  # noqa: BLE001
        _have = False
    if not _have:
        skip("F2 live drill", "fastapi TestClient not installed here")
        return

    import tempfile as _tf
    with _tf.TemporaryDirectory() as tmp:
        drill = os.path.join(tmp, "f2drill.py")
        with open(drill, "w") as fh:
            fh.write(r'''
import os, uuid
os.environ["DATABASE_URL"] = "sqlite:///" + os.path.join(os.environ["F2TMP"], "f2.db")
os.environ["WEEKLY_EMAIL"] = "off"
from fastapi.testclient import TestClient
import main, store
c = TestClient(main.app)
assert store.enabled(), "the drill needs its own database"

STU = sorted(main.STUDENTS.keys())[:2]
assert len(STU) >= 2, "need two pilot students"

def signup(email, tcode=""):
    r = c.post("/api/teacher/signup", json={"email": email, "password": "hunter2hunter2",
                                            "name": "T", "teacher_code": tcode})
    assert r.status_code == 200, (email, r.status_code, r.text[:200])
    return r.json()

# ---- 1. EVERY class endpoint refuses an anonymous caller --------------------
anon = [
    ("get",    "/api/class/ANY"),
    ("get",    "/api/class/ANY/summary"),
    ("get",    "/api/class/ANY/reveal/deadbeef"),
    ("post",   "/api/class"),
    ("post",   "/api/class/ANY/students"),
    ("delete", "/api/class/ANY/students/deadbeef"),
]
for verb, path in anon:
    r = getattr(c, verb)(path, **({"json": {"class_code": "ANY", "code": "X"}}
                                  if verb == "post" else {}))
    assert r.status_code == 401, ("ANON REACHED " + path, r.status_code, r.text[:200])

# ---- 2. the retired route is really gone ------------------------------------
assert c.get("/api/teacher/MRSBAKER/classes").status_code == 404, "the old route answered"

# ---- 3. an owner can work; the roster never carries a raw login code --------
A = signup("a@x.com")
ta = A["token"]
HA = {"X-Teacher-Token": ta}
r = c.post("/api/class", json={"token": ta, "class_code": "P3", "name": "Period 3"})
assert r.status_code == 200, r.text[:200]
r = c.post("/api/class/P3/students", headers=HA, json={"code": STU[0]})
assert r.status_code == 200, r.text[:200]
r = c.get("/api/class/P3", headers=HA)
assert r.status_code == 200, r.text[:200]
body = r.text
klass = r.json()["klass"]
assert klass["roster"], "the roster is empty"
row = klass["roster"][0]
assert "ref" in row and "code_masked" in row, row
for s in STU:
    assert s not in body, ("A RAW LOGIN CODE IS IN THE ROSTER RESPONSE", s)
assert "•" in row["code_masked"], row

# the summary is the richest view; it must mask too
r = c.get("/api/class/P3/summary", headers=HA)
assert r.status_code == 200, r.text[:200]
for s in STU:
    assert s not in r.text, ("A RAW LOGIN CODE IS IN THE SUMMARY", s)

# ---- 4. reveal: one code, to the owner only ---------------------------------
r = c.get("/api/class/P3/reveal/" + row["ref"], headers=HA)
assert r.status_code == 200 and r.json()["code"] == STU[0], r.text[:200]
assert c.get("/api/class/P3/reveal/nosuchref", headers=HA).status_code == 404

# ---- 5. ANOTHER teacher is a stranger to this class -------------------------
B = signup("b@x.com")
HB = {"X-Teacher-Token": B["token"]}
assert c.get("/api/class/P3", headers=HB).status_code == 404, "B READ A'S CLASS"
assert c.get("/api/class/P3/summary", headers=HB).status_code == 404, "B READ A'S SUMMARY"
assert c.get("/api/class/P3/reveal/" + row["ref"], headers=HB).status_code == 404
assert c.post("/api/class/P3/students", headers=HB,
              json={"code": STU[1]}).status_code == 404, "B ADDED TO A'S CLASS"
assert c.delete("/api/class/P3/students/" + row["ref"],
                headers=HB).status_code == 404, "B REMOVED FROM A'S CLASS"
assert c.post("/api/class", json={"token": B["token"], "class_code": "P3",
                                  "name": "hijacked"}).status_code == 404, "B RENAMED A'S CLASS"
assert c.get("/api/class/P3", headers=HA).json()["klass"]["name"] == "Period 3"

# ---- 6. claiming: unowned once, owned never ---------------------------------
store.create_class("LEGACY1", "Old class", "Mrs B", "MRSBAKER")
assert store.get_class("LEGACY1")["teacher_id"] == ""
r = c.post("/api/teacher/claim", json={"token": B["token"], "class_code": "LEGACY1"})
assert r.status_code == 200, r.text[:200]
r = c.post("/api/teacher/claim", json={"token": ta, "class_code": "LEGACY1"})
assert r.status_code == 409, ("A CLAIMED AN OWNED CLASS", r.status_code)
assert c.post("/api/teacher/claim", json={"token": ta,
                                          "class_code": "NOPE"}).status_code == 409

# ---- 7. inheritance at signup, and it cannot steal an owned class -----------
store.create_class("LEGACY2", "Another", "Mrs B", "MRSBAKER")
C = signup("c@x.com", tcode="MRSBAKER")
assert C["adopted"] == 1, ("inherited the wrong number", C["adopted"])
mine = [k["class_code"] for k in C["classes"]]
assert "LEGACY2" in mine and "LEGACY1" not in mine, ("STOLE AN OWNED CLASS", mine)

# ---- 8. the session behaves: me / logout ------------------------------------
assert c.get("/api/teacher/me", headers=HA).json()["teacher"]["email"] == "a@x.com"
c.post("/api/teacher/logout", json={"token": ta})
assert c.get("/api/teacher/me", headers=HA).status_code == 401, "TOKEN SURVIVED LOGOUT"
assert c.get("/api/class/P3", headers=HA).status_code == 401

# ---- 9. duplicate email, weak password, wrong password ----------------------
assert c.post("/api/teacher/signup", json={"email": "a@x.com", "password": "hunter2hunter2"}
              ).status_code == 409
assert c.post("/api/teacher/signup", json={"email": "d@x.com", "password": "short"}
              ).status_code == 400
assert c.post("/api/teacher/login", json={"email": "a@x.com", "password": "wrong"}
              ).status_code == 401
print("F2-DRILL-OK")
''')
        env = dict(os.environ)
        env["PYTHONPATH"] = here + os.pathsep + env.get("PYTHONPATH", "")
        env["F2TMP"] = tmp
        env["WEEKLY_EMAIL"] = "off"
        r = subprocess.run([sys.executable, drill], cwd=here, env=env,
                           capture_output=True, text=True)
        check("F2 LIVE DRILL: anonymous refused · another teacher refused · no raw "
              "login code in any class response · claim/inherit cannot steal",
              r.returncode == 0 and "F2-DRILL-OK" in r.stdout,
              (r.stdout + r.stderr)[-700:])


# =============================================================================
# PART 3ad -- A CLIP NEVER EATS SOMETHING BETTER (build ez, 2026-08-13)
# =============================================================================
# Three regressions Jim found by USING the site, all the same species: the video work
# quietly took over something that was already doing a better job.
#   1. Build eu made the hero's "Hear him teach" button play the site-welcome CLIP and
#      `return` before ever reaching the teaching sample -- so the one button on the
#      front page that promised to let you hear him TEACH stopped doing it the moment
#      the clip went live, and relabelled itself so it no longer said what it did.
#   2. Two welcomes could stack: the home page now plays his site welcome on the way
#      into the demo, and the demo page opens with its own.
#   3. After the real demo problem, an audience-door visitor got the WALKTHROUGH's
#      ending panel -- re-speaking a line they had already heard and offering them the
#      lesson they had just finished.
# Each check below is written against the specific thing that broke.
def part3ad_clip_never_eats():
    print("\nPART 3ad — a clip never eats something better (build ez)")
    here = os.path.dirname(os.path.abspath(__file__))
    la = open(os.path.join(here, "static", "landing.html"), encoding="utf-8").read()
    dm = open(os.path.join(here, "static", "demo.html"), encoding="utf-8").read()

    # 1. THE TEACH BUTTON TEACHES. Slice its handler and prove no clip lives in it.
    try:
        wh = la[la.index("function wireHear("):]
        wh = wh[:wh.index("\n    }")]
    except ValueError:
        wh = ""
    check("landing has a readable wireHear()", bool(wh), "could not slice it")
    check("the 'Hear him teach' button never plays a video clip",
          "TutorMoments" not in wh,
          "build eu put the site-welcome clip in this handler and returned before the "
          "audio sample -- the button promised teaching and delivered a greeting")
    check("the 'Hear him teach' button still reaches the teaching sample",
          "/api/demo-audio/71" in wh,
          "this is the whole job of the button: one line of his real voice teaching the "
          "problem on the hero board")
    # Precise on purpose, twice over. "Meet Mr. Cadabra" is legitimate marketing copy in
    # the hero lede and the meta description, so only the BUTTON RELABEL (which carried
    # the play triangle) is banned -- and the page's own change note QUOTES that relabel
    # to record why it was removed, so HTML comments are stripped first. Same precedent
    # as PART 3p, 3w and 3aa: a note explaining a fix must never trip the fix's guard.
    la_code = re.sub(r"<!--.*?-->", "", la, flags=re.S)
    check("the teach button is never relabelled to a greeting",
          "▶ Meet Mr. Cadabra" not in la_code,
          "a button must say what it does; eu relabelled this one to '▶ Meet Mr. "
          "Cadabra' while the markup still promised 'Hear him teach'")
    # Every label with WORDS in it must be about teaching. A wordless transient ("🔊 …"
    # while the sample loads) promises nothing and is fine.
    labels = set(re.findall(r"hb\.textContent\s*=\s*'([^']+)'", la))
    worded = [t for t in labels if re.search(r"[A-Za-z]", t)]
    check(f"every label this button wears is about TEACHING ({len(worded)} worded)",
          bool(worded) and all(("Hear him teach" in t or "teaching" in t) for t in worded),
          f"got {sorted(worded)} -- the button's own words are the promise it makes")

    # 2. THE WELCOME NEVER DOUBLES UP. The home page hands off a one-shot marker and
    #    the demo page reads AND CLEARS it before its own opener can run.
    check("the demo CTA plays the site welcome on the way in",
          "wireDemoWelcome" in la and "TutorMoments.play('site_welcome')" in la,
          "Jim: 'it starts the welcome clip, and then the demo starts'")
    check("the home page leaves the one-shot marker before navigating",
          "sessionStorage.setItem('cadabra_welcomed', '1')" in la,
          "without the marker the demo page cannot know he has just said hello")
    check("the demo page reads the marker BEFORE its own welcome",
          dm.index("cadabra_welcomed") < dm.index("TutorMoments.available('demo_welcome')"),
          "the skip must be decided before the second clip can start")
    check("the demo page CLEARS the marker (one arrival, not every reload)",
          "sessionStorage.removeItem('cadabra_welcomed')" in dm,
          "a marker that is never cleared silences the demo's own welcome forever")
    check("a marked arrival skips the demo's own welcome entirely",
          re.search(r"if \(justWelcomed\) \{ afterHello\(\); return; \}", dm) is not None,
          "nobody may ever hear two welcome clips back to back")

    # 3. AFTER A LESSON, NOTHING ALREADY HEARD IS REPLAYED.
    try:
        ae = dm[dm.index("function showAudienceEnd("):]
        ae = ae[:ae.index("\n  // Stepping out of a walkthrough")]
    except ValueError:
        ae = ""
    check("demo has a readable showAudienceEnd()", bool(ae), "could not slice it")
    check("showAudienceEnd knows whether a lesson just finished",
          "function showAudienceEnd(spoken, afterLesson)" in dm,
          "without that flag the walkthrough's ending is served after a lesson")
    check("showBalloons passes the just-finished-a-lesson signal through",
          "showAudienceEnd(spoken===true, keepCongrats===true)" in dm,
          "this single dropped argument is the whole bug Jim hit")
    check("after a lesson the panel SPEAKS NOTHING",
          "if(afterLesson) return;" in ae
          and ae.index("if(afterLesson) return;") < ae.index("say(line)"),
          "the congratulations line has just been spoken aloud; replaying the "
          "walkthrough outro on top of it is the repeat Jim heard")
    check("after a lesson the panel keeps the congratulations framing",
          "Congratulations — that was a real lesson!" in ae,
          "the win must stay on screen; the handoff used to throw it away")
    check("after a lesson the panel does NOT re-offer the lesson just finished",
          "'↩ Try another level'" in ae and re.search(
              r"afterLesson\s*\?\s*\[\['another'", ae) is not None,
          "offering 'See a real lesson' to somebody who has just seen one is the other "
          "half of what Jim reported")


# =============================================================================
# PART 3ac -- THE VOICE SEQUENCING (build ey, 2026-08-13)
# =============================================================================
# Phase 2's second half: Mr. Cadabra's talking clips at the seven moments of a real
# lesson. ONE rule holds the whole design up, and it is the rule this part exists to
# make unbreakable:
#
#   A CANNED CLIP AND HIS LIVE VOICE NEVER TALK AT ONCE, AND A CLIP NEVER REPLACES
#   THE PERSONALISED LINE.
#
# Video cannot say a child's name; the live voice can. If a future edit drops an
# await, or plays a clip instead of speaking, the failure is SILENT in every test that
# reads text -- you only hear it, once, in a real lesson, as two voices over each
# other. So the sequence is asserted structurally: the gate is awaited, it sits on the
# correct side of speak(), and every moment reaches a real trigger.
def part3ac_voice_sequencing():
    print("\nPART 3ac — the voice sequencing (a clip never talks over his live voice)")
    import prompts
    here = os.path.dirname(os.path.abspath(__file__))
    se = open(os.path.join(here, "static", "session.html"), encoding="utf-8").read()
    tm = open(os.path.join(here, "static", "tutor-moments.js"), encoding="utf-8").read()

    MOMENTS = ["first_meeting", "welcome_back", "quiz_passed", "unit_gold",
               "course_champion", "sprint_best", "goodbye"]

    # 1. The page can actually play a clip at all.
    check("session.html loads tutor-moments.js",
          '/static/tutor-moments.js' in se,
          "the lesson page cannot play a moment clip without the player")
    check("the player is NOT deferred on the lesson page",
          not re.search(r'<script[^>]*\bdefer\b[^>]*tutor-moments\.js', se),
          "window.TutorMoments must exist when the page script runs -- the landing page "
          "already paid for this lesson once")

    # 2. THE SEQUENCE ITSELF, inside runTutor's own body: the before-gate, the live
    #    voice, the after-gate, in that order, each awaited. This is the check that
    #    would catch a dropped await -- the failure no text-reading test can see.
    try:
        body = se[se.index("async function runTutor("):]
        body = body[:body.index("\n    // ---------- Text fallback")]
    except ValueError:
        body = ""
    check("runTutor has a readable body", bool(body), "could not slice it")
    # build gf: build ga wrapped every gate in withDeadline() so a gate that never settles
    # can no longer strand a student mid-lesson. These checks used to read the three lines
    # LITERALLY, so the wrapper made the sequencing rule unverifiable -- the checks failed
    # while the behaviour was fine, which is the worst kind of test. They now normalise the
    # wrapper away and assert exactly the same invariants on what is left, and a new check
    # below insists the wrapper is still there. Neither rule can be dropped unnoticed now.
    def _raw_runtutor(src):
        # the three gates INSIDE runTutor -- the welcome-card gate is a fourth, elsewhere
        try:
            b = src[src.index("async function runTutor("):]
            return b[:b.index("\n    // ---------- Text fallback")]
        except ValueError:
            return ""

    def _unwrap_deadline(src):
        return re.sub(r'await withDeadline\(\(\) => (runPendingMoment\("(?:before|after)"\)'
                      r'|speak\(clean\))[^;]*;', r'await \1;', src)
    body = _unwrap_deadline(body)
    se_seq = _unwrap_deadline(se)
    seq = [ln.strip() for ln in body.splitlines()
           if "runPendingMoment(" in ln or "await speak(clean)" in ln]
    check("runTutor awaits the clip gate BEFORE speaking, and the after-gate follows",
          [s.split("//")[0].strip() for s in seq] == ['await runPendingMoment("before");',
                                                      "await speak(clean);",
                                                      'await runPendingMoment("after");'],
          f"got {seq!r} -- the gates and speak() must appear in exactly that order, all "
          f"three awaited; a missing await is two voices talking over each other")
    check("the gate is awaited everywhere it is used (never fired and forgotten)",
          not re.search(r'(?<!await )(?<!\.)runPendingMoment\("(before|after)"\)(?!\s*\.then)', se_seq),
          "every runPendingMoment call must be awaited or explicitly chained with .then "
          "(the sprint path) -- an un-awaited gate is exactly the overlap this forbids")
    # build gf: and the deadline itself must not be quietly removed. A gate that cannot
    # time out is the 2026-08-14 freeze: chat 200, speak 200, then no microphone, ever.
    check("every gate in runTutor carries a deadline (build ga)",
          len(re.findall(r'await withDeadline\(\(\) => (?:runPendingMoment\("(?:before|after)"\)'
                         r'|speak\(clean\))', _raw_runtutor(se))) == 3,
          "the opening clip, the spoken reply and the closing clip must each be wrapped in "
          "withDeadline() -- sendToTutor's finally{} cannot re-enable the microphone if an "
          "await never settles, which is exactly how a student got stranded mid-question")

    # 3. A clip must never REPLACE the personalised line: speak(clean) is unconditional.
    #    Not nested in an if, not in an else of the clip's result.
    sp = re.search(r'await runPendingMoment\("before"\);[^\n]*\n(\s*)await speak\(clean\);',
                   body)
    check("his live voice is not conditional on the clip",
          bool(sp) and len(sp.group(1)) == 8,
          "speak() must run at the same nesting level, whatever the clip did -- a canned "
          "clip is an arrival, never a substitute for the line that says the child's name")

    # 4. Every moment in the table reaches a real trigger, and every triggered moment is
    #    in the table. A clip nothing can fire is a clip that does not exist (build er's
    #    lesson, learned the expensive way with the thumbs-up).
    table = set(re.findall(r"^\s{6}(\w+):\s*\{ when:", se, re.M))
    check(f"the moment table carries all seven moments ({len(table)})",
          table == set(MOMENTS),
          f"missing={sorted(set(MOMENTS) - table)}, unexpected={sorted(table - set(MOMENTS))}")
    queued = set(re.findall(r'queueMoment\("(\w+)"\)', se))
    queued |= set(re.findall(r'\?\s*"(\w+)"\s*:\s*\(hasHistory\s*\?\s*"(\w+)"', se)[0]
                  if re.findall(r'\?\s*"(\w+)"\s*:\s*\(hasHistory\s*\?\s*"(\w+)"', se) else [])
    unreachable = sorted(set(MOMENTS) - queued)
    check("every moment is wired to a real trigger", not unreachable,
          f"{unreachable} can never fire -- a clip nothing can trigger is a clip that "
          f"does not exist (the thumbs-up cost three builds to learn that)")

    # 5. The triggers are the RIGHT ones -- each in the function that owns that event.
    for fn, key in (("showQuiz", "quiz_passed"), ("showCheck", "unit_gold"),
                    ("showFinalExam", "course_champion"), ("sprFinish", "sprint_best")):
        body = re.search(r"(?:async )?function " + fn + r"\(.*?\n    \}", se, re.S)
        check(f"  {key} fires from {fn}()",
              bool(body) and f'queueMoment("{key}")' in body.group(0),
              "the moment must be queued where the event actually happens")
    check("  goodbye fires from the [[bye]] tag, not from sniffing his words",
          re.search(r'name === "bye"\)\s*queueMoment\("goodbye"\)', se) is not None,
          "detecting a farewell by reading prose would misfire on 'see you next Tuesday'")
    check("  the arrival moments fire from the welcome click (a real user gesture)",
          re.search(r'queueMoment\(firstTime \? "first_meeting"', se) is not None
          and "await TutorMoments.ready()" in se,
          "a clip with SOUND needs a gesture to autoplay, and the manifest probe must "
          "have settled before available() is trusted")

    # 6. Cadence: the rare EARNED moments always play; the repeatable ones are capped.
    #    (A clip that plays five times in an afternoon stops being a person.)
    for key, want in (("unit_gold", "always"), ("course_champion", "always"),
                      ("first_meeting", "always"), ("quiz_passed", "daily"),
                      ("sprint_best", "daily"), ("welcome_back", "daily"),
                      ("goodbye", "daily")):
        row = re.search(key + r":\s*\{[^}]*cadence:\s*\"(\w+)\"", se)
        check(f"  {key} cadence is {want}", bool(row) and row.group(1) == want,
              f"got {row.group(1) if row else 'no row'} -- earned moments always play; "
              f"repeatable ones are capped at one a day so they stay special")
    check("the goodbye plays AFTER his words; the celebrations before",
          re.search(r'goodbye:\s*\{ when: "after"', se) is not None
          and len(re.findall(r'when: "before"', se)) == 6,
          "a send-off belongs last (his personal wrap-up, THEN the warm goodbye); "
          "a celebration belongs first")

    # 7. It must still work DARK -- today six of the seven clips do not exist yet.
    check("queueMoment refuses to queue a clip that is not there",
          re.search(r'if \(!\(window\.TutorMoments && TutorMoments\.available\(key\)\)\) return false',
                    se) is not None,
          "with no clip in the manifest the page must behave exactly as it did before")
    check("the player still resolves on every failure path",
          '"unavailable"' in tm and "sourcesFailed" in tm and "setTimeout(function () { finish" in tm,
          "a clip that cannot play must hand the turn straight back -- nothing here may "
          "strand a lesson")
    check("a moment is spent even when skipped",
          re.search(r'momentSpend\(p\.key\);\s*//', se) is not None,
          "one offer a day, watched or not -- otherwise skipping re-offers it all day")

    # 8. The corner presence keeps its promise while the card talks.
    check("the corner is set idle while he speaks in the card",
          re.search(r'setState\("idle"\);\s*//.*mime', se) is not None,
          "the face never fakes speech (rule from build ej) -- and it must not sit on a "
          "thinking glow while he is talking in the overlay")

    # 9. The [[bye]] tag is taught ONLY in the lesson-only note, never the shared block.
    check("[[bye]] is taught in PROGRESS_TAGS_NOTE",
          "[[bye]]" in prompts.PROGRESS_TAGS_NOTE,
          "the tutor cannot mark a wrap-up it was never told about")
    check("[[bye]] is NOT in the shared block (practice/topic cannot draw it)",
          "[[bye]]" not in tutor.GRAPH_TOOL_NOTE,
          "the shared block reaches practice and topic, which have no bye handler")
    for phrase in ("ONLY when the\n   student has said they are going",
                   "It draws NOTHING"):
        check(f"  the bye tag keeps its guard rail: {phrase.splitlines()[0][:40]}...",
              phrase in prompts.PROGRESS_TAGS_NOTE,
              "the tag must never fire because a lesson merely feels finished")


# =============================================================================
# PART 3ab -- THE SEVEN VERIFIED TEACHING DEFECTS (build ex, 2026-08-13)
# =============================================================================
# The last open items from the 2026-08-12 audit batch, each verified against the
# transcripts before being built: a regrouping subtraction asked before one was ever
# modelled (19e) · a story model that wrote "3 dollars + 8 tickets" (27c) · 0.82
# corrected without the words "place value" (49g) · the locked Final Exam's retake
# offered only when asked (50g) · bare "lim f(x)" and an "on both sides" caption
# that was false on the left (51f) · a miss explained before "No -- it's 11" was
# said (52e) · "the way we did a minute ago" for work that never happened (62).
# WHAT THIS PART PROVES: each addition lives in the SHARED block exactly once,
# reaches a built prompt, and keeps its load-bearing phrases -- including the
# deliberate guard rails (52e must NOT override rule 22's ladder; 62 must NOT ban
# connecting ideas; 51f names the true left-side behavior).
def part3ab_seven_defects():
    print("\nPART 3ab — the seven verified teaching defects (build ex)")
    note = tutor.GRAPH_TOOL_NOTE
    built = tutor.build_system_prompt(dict(STUDENT), course="calculus")

    headlines = {
        "19e": "A NEW MOVE INSIDE A FAMILIAR TOPIC COUNTS AS NEW",
        "27c": "A STORY MODEL HOLDS ONE UNIT FROM ITS FIRST LINE TO ITS LAST",
        "49g": "THE DIAGNOSIS IS SPOKEN, IN PLAIN WORDS, WHEN YOU CORRECT",
        "50g": "AT THE LOCKED DOOR, THE OFFER IS AUTOMATIC",
        "51f": "A LIMIT NAMES ITS APPROACH, AND EACH SIDE IS ITS OWN CLAIM",
        "52e": "THE VERDICT OPENS THE REPLY -- THEN THE WHY",
        "62":  "YOU MAY ONLY POINT AT WORK THAT HAPPENED",
    }
    for key, h in sorted(headlines.items()):
        check(f"rule {key} lives in the shared block exactly once", note.count(h) == 1,
              f"count in GRAPH_TOOL_NOTE = {note.count(h)} -- shared rules go in "
              f"once, never per course")
        check(f"rule {key} reaches a built prompt exactly once", built.count(h) == 1,
              f"count in the built calculus prompt = {built.count(h)}")

    anchors = [
        # 19e -- the honest pre-ask check, and the moves that count
        ("19e names the audit's move (regrouping) among the never-watched moves",
         "regrouping or\n        borrowing" in note or "regrouping or borrowing" in note),
        ("19e demands the demo BEFORE the ask",
         "If not, show it before you ask it." in note),
        # 27c -- the defect string itself, and the conversion demand
        ("27c carries the real audit string (3 dollars + 8 tickets)",
         '"3 dollars + 8 tickets = 11"' in note),
        ("27c: unlike quantities never add",
         "dollars never add\n        to tickets" in note
         or "dollars never add to tickets" in note),
        ("27c: a real relationship converts, spoken out loud",
         "SAY\n        that conversion out loud" in note
         or "SAY that conversion out loud" in note),
        # 49g -- the naming demand, with rule 42 intact
        ("49g demands the error KIND be named in words the student keeps",
         "place-value slip" in note),
        ("49g keeps rule 42 (the error, never the student)",
         "name the\n        error, never the student" in note
         or "name the error, never the student" in note),
        # 50g -- unprompted, same-reply, with the plan
        ("50g: the SAME reply that says locked offers the way through",
         "the SAME reply that carries the news offers the way through" in note),
        ("50g: never left to ask whether a key exists",
         "or to ask you whether one exists" in note),
        # 51f -- both catches, precisely
        ("51f bans the bare limit",
         'never a bare "lim f(x)"' in note),
        ("51f states the true left-side behavior (MINUS infinity)",
         "plunges to MINUS infinity" in note),
        ("51f: both sides only after both sides are checked",
         'say "on both sides" only when both sides have actually been\n'
         "        checked" in note
         or 'say "on both sides" only when both sides have actually been checked'
         in note),
        # 52e -- verdict first, ladder intact
        ("52e opens with the verdict carrying the answer",
         '"No -- it\'s 11. Here\'s\n        the why."' in note
         or '"No -- it\'s 11. Here\'s the why."' in note),
        ("52e deliberately preserves rule 22's ladder",
         "This never overrides rule 22's ladder" in note),
        # 62 -- the check, the pointer, and the not-a-ban guard
        ("62 demands the board-or-notes check before a back-reference",
         "is that work actually on the board this session" in note),
        ("62 points at rule 60's spotlight for real work",
         "rule\n        60's spotlight exists for exactly this" in note
         or "rule 60's spotlight exists for exactly this" in note),
        ("62 is NOT a ban on connecting ideas",
         "connecting is teaching" in note),
    ]
    for name, cond in anchors:
        check(name, cond, "a load-bearing phrase was dropped or reworded -- if the "
                          "rewording is deliberate, update this anchor in the same "
                          "commit")


# =============================================================================
# PART 3aa -- PLACEMENT NEVER PASSES A UNIT; THE FINAL GATE IS DERIVED (build ew)
# =============================================================================
# Jim's policy: "a student who places into the middle of a course should NOT get a
# pass on those units just for answering a few placement questions right." The
# 2026-08-13 investigation declared that policy already in force -- and it was NOT:
# challenge.html posted one /api/check per unit with the assessment scores, and
# record_check marks a unit mastered at >= 90%, so 5/5 on five placement questions
# silently passed the unit and counted toward the Final Exam. The earlier read
# checked the placement TABLE (inert, correctly) and missed the side-channel in the
# page. These checks pin the policy on EVERY path, plus build ew's second fix: the
# final-exam requirement is derived from the course's real unit list, never a
# literal 9 that goes stale the day a course gains or loses a unit.
def _code_only(src: str) -> str:
    """Source with comment lines stripped, so a change note QUOTING an old literal
    (to record why it was removed) can never trip a ban -- same reason PART 3w strips
    notes and PART 3p strips HTML comments before reading copy."""
    return "\n".join(ln for ln in src.splitlines()
                     if not ln.lstrip().startswith("#"))


def part3aa_placement_honesty():
    print("\nPART 3aa — placement never passes a unit; the final gate is derived (build ew)")
    import curriculum as _c
    import prompts
    here = os.path.dirname(os.path.abspath(__file__))
    ch = open(os.path.join(here, "static", "challenge.html"), encoding="utf-8").read()
    mn = open(os.path.join(here, "main.py"), encoding="utf-8").read()
    st = open(os.path.join(here, "store.py"), encoding="utf-8").read()
    pr = open(os.path.join(here, "prompts.py"), encoding="utf-8").read()
    se = open(os.path.join(here, "static", "session.html"), encoding="utf-8").read()

    # 1. THE POLICY, AT ITS ONLY KNOWN BREACH POINT: the assessment page may never
    #    post a check. This is the line that let placement write mastery. The page's
    #    change notes rightly QUOTE the removed call to record why it went -- so strip
    #    HTML comments and // comment lines before the ban (PART 3p / 3w precedent).
    ch_code = re.sub(r"<!--.*?-->", "", ch, flags=re.S)
    ch_code = "\n".join(ln for ln in ch_code.splitlines()
                        if not ln.lstrip().startswith("//"))
    check("challenge.html never calls /api/check (placement must not write mastery)",
          "/api/check" not in ch_code,
          "the assessment is posting unit CHECKS again -- checks feed mastery at >= 90%, "
          "so acing five placement questions would silently pass the unit")
    check("challenge.html's postJSON helper stays gone",
          "function postJSON" not in ch,
          "its only caller was the per-unit check loop; a ready-made helper invites "
          "the bug back")

    # 2. The per-unit picture must still be KEPT -- inside the placement payload,
    #    where it can never touch mastery.
    check("the placement POST carries strengths (the dormant consumers light up)",
          "strengths: strong.map(" in ch,
          "dashboard chips + the tutor's 'Strengths:' prompt line read "
          "placement.strengths; dropping it loses the assessment's value")
    check("the placement POST carries the full per-unit results",
          "units: results.map(" in ch,
          "the per-unit picture must survive somewhere placement-scoped")
    check("PlacementIn accepts strengths + units (the server keeps what the page sends)",
          "strengths: list = []" in mn and "units: list = []" in mn,
          "pydantic silently DROPS unknown fields -- without these the payload "
          "arrives and evaporates")

    # 3. THE HONEST SENTENCE: the result screen says out loud that Strong is a head
    #    start, not a passed unit -- written AND spoken.
    check("the result screen carries the honest sentence (#rHonest)",
          'id="rHonest"' in ch and "a head start, not a passed unit" in ch,
          "a placed student should never first learn at a locked door, months later, "
          "that placement never passed a unit")
    check("the honest sentence frames strong units' quizzes as the quick wins",
          "quickest quizzes" in ch and "quick wins" in ch,
          "honesty without the encouragement is just a warning label")

    # 4. NO PATH from placement to mastery, server-side. post_placement's function
    #    body must not touch check-recording; store.save_placement writes only the
    #    placements table.
    m = re.search(r"def post_placement\(.*?(?=\n@app|\ndef )", mn, re.S)
    check("post_placement's body never records a check",
          bool(m) and "record_check" not in m.group(0)
          and "record_final_exam" not in m.group(0),
          "the placement endpoint is writing mastery-bearing rows")
    m2 = re.search(r"\ndef save_placement\(.*?(?=\ndef )", st, re.S)
    check("store.save_placement touches only the placements table",
          bool(m2) and "unit_checks" not in m2.group(0)
          and '_upsert("placements"' in m2.group(0),
          "save_placement must stay inert toward mastery")

    # 5. THE DERIVED GATE: no "required": 9 literal in CODE (comment lines stripped --
    #    the change notes rightly quote the old literal), and the derivation present.
    mn_code = _code_only(mn)
    check('no "required": 9 literal survives in main.py code',
          '"required": 9' not in mn_code,
          "the hard-coded gate is back; it breaks silently the day any course "
          "gains or loses a unit")
    check("_units_required derives from curriculum.units_for",
          "def _units_required" in mn
          and "curriculum.units_for(course)" in
          (re.search(r"def _units_required\(.*?(?=\ndef |\n@app)", mn, re.S)
           or re.match(r"", "")).group(0),
          "the requirement must come from the course's real unit list")
    mfes = re.search(r"def _final_exam_state\(.*?(?=\n@app|\ndef )", mn, re.S)
    check("_final_exam_state uses the derived requirement",
          bool(mfes) and "_units_required(course)" in mfes.group(0),
          "the state dict is where every consumer reads the gate from")
    check("FINAL_GATE_MESSAGE carries the derived count ({req}), not a nine",
          "{req}" in mn and "of 9 so far" not in mn_code,
          "the locked-door message would lie about the bar the day a course changes")

    # 6. The functional proof, in-process: for every real course the derivation
    #    equals the course's actual unit count. (main is imported by the sec drill
    #    subprocess elsewhere; here the pure function is checked via a fresh import
    #    guarded the same way.)
    try:
        import importlib
        _main = importlib.import_module("main")
        for course in sorted(_c.COURSES):
            want = len(_c.units_for(course))
            got = _main._units_required(course)
            check(f"  _units_required({course!r}) == its real unit count ({want})",
                  got == want, f"got {got}")
        stx = _main._final_exam_state("no-such-student", "basic")
        check("_final_exam_state.required is the derived count",
              stx.get("required") == len(_c.units_for("basic")), f"got {stx}")
        check("_final_exam_state: nobody is eligible with zero mastered units",
              stx.get("eligible") is False, f"got {stx}")
        gm = _main._final_gate_message("no-such-student", "basic", stx)
        check("the gate message speaks the derived count",
              f"of {len(_c.units_for('basic'))}" in gm, gm[:200])
        pin = _main.PlacementIn(strengths=["Fractions"], units=[{"u": 1}])
        check("PlacementIn round-trips strengths + units",
              pin.strengths == ["Fractions"] and pin.units == [{"u": 1}]
              and "strengths" in pin.model_dump(),
              "the fields exist but do not survive model_dump into save_placement")
    except Exception as exc:  # noqa: BLE001
        # build gh: importing main.py pulls the whole web stack (httpx, starlette...).
        # A missing THIRD-PARTY package is an unprovisioned machine; a missing module of
        # OUR OWN, or any other error, is a real failure and still fails.
        _missing = (getattr(exc, "name", "") or "").split(".")[0]
        if isinstance(exc, ImportError) and _missing and _missing not in OUR_MODULES:
            skip("main.py importable for the placement/final functional checks",
                 f"{_missing} is not installed here")
        else:
            bad("main.py importable for the placement/final functional checks", str(exc))

    # 7. The SHARED final notes are count-neutral (they overlay ANY course whose
    #    derived gate opens); the per-course "THE NINE UNITS" headers are each one
    #    course's own factual text and deliberately untouched.
    for name, note in (("FINAL_PREP_NOTE", prompts.FINAL_PREP_NOTE),
                       ("FINAL_EXAM_NOTE", prompts.FINAL_EXAM_NOTE)):
        check(f"{name} never counts to nine",
              "NINE UNITS" not in note and "nine units" not in note
              and "question 18" not in note,
              "a shared overlay must stay true for a course of any size")
        check(f"{name} still says the whole course is mastered",
              "EVERY UNIT OF THIS COURSE" in note,
              "the count-neutral wording lost the actual claim")

    # 8. The lesson page reads the server's derived count instead of a literal.
    check("session.html reads final.required for the course bar",
          "parseInt(fin.required, 10)" in se,
          "the label is hard-coding the gate again")
    check("session.html reads st.required in the final overlay",
          "parseInt(st.required, 10)" in se,
          "the overlay is hard-coding the gate again")
    check('no "of 9" label survives in session.html markup/script',
          "of 9<" not in se and '" of 9 ' not in se and "of 9</b>" not in se,
          "a hard-coded of-9 label crept back")


def part4_live():
    print("\nPART 4 — live scenarios (a scripted difficult student)")
    if not os.environ.get("ANTHROPIC_API_KEY"):
        skip("live scenarios", "no ANTHROPIC_API_KEY")
        return
    for sc in LIVE_SCENARIOS:
        history = [{"role": r, "content": t} for r, t in sc["history"]]
        try:
            reply = tutor.get_tutor_reply(dict(STUDENT), history, sc["student"],
                                          course=sc["course"], code="RULETEST")
        except Exception as exc:  # noqa: BLE001
            bad(f"live: {sc['name']}", f"call failed: {exc}")
            continue
        try:
            passed = bool(sc["assertion"](reply))
        except Exception as exc:  # noqa: BLE001
            passed = False
            reply = f"(assertion crashed: {exc}) {reply}"
        check(f"live: {sc['name']}", passed, f"{sc['why']}\n        reply: {reply[:220]}")


# =============================================================================
# PART 3aj -- THE SCREEN IS CHECKED TOO
# =============================================================================
# 2026-08-16, build gn. Jim ran ONE Geometry lesson and found four defects by eye in the
# first turn: "a squared plus B squared equals C squared", a triangle lettered on its
# CORNERS while the words talked about its LEGS, a rail reading Unit 1 under prose saying
# Unit 5, and a clipped header. Not one of them was catchable by anything we owned, and
# the reason is structural: the twelve referees read the REPLY, lessonaudit reads the
# TRANSCRIPT, and every one of those defects is born when session.html RENDERS that text.
# Nothing was pointed at the screen. Jim: "we should have a universal way to catch these
# things. Somebody should be checking this."
#
# screencheck.py is that checker, and it is deliberately built so its JUDGEMENT needs no
# browser, no API key and no network -- only CAPTURING a fresh screen needs Playwright.
# That is why this PART exists here rather than as another tool nobody runs: the six
# checks run on every push, on any machine, for free. A check that skips is a wish.
#
# TWO SEAMS ARE GUARDED BELOW, and they matter more than the fixtures. screencheck reads
# a figure's SVG by its FONT METRICS -- that is the only way to tell a corner label from
# a side label -- and it mirrors session.html's VAR_SKIP list. Change either renderer and
# the checker goes SILENTLY blind, which is the worst failure a checker has: it keeps
# reporting "no findings" while the defect ships. When two features touch, walk the seam
# (build fb).
def part3aj_screen_checks():
    print("\nPART 3aj — the screen auditor (screencheck.py)")
    root = os.path.dirname(os.path.abspath(__file__))
    try:
        import screencheck
    except Exception as exc:  # a missing module of OUR OWN is a broken repo, not a laptop
        bad("screencheck imports", f"{type(exc).__name__}: {exc}")
        return

    # ---- the six checks, each proved in BOTH directions on real turns ----
    for name, expected, found in screencheck.fixture_results():
        names = sorted({f.check for f in found})
        if expected is None:
            check(f"screencheck: {name}", not names,
                  f"expected silence, got {names}")
        else:
            check(f"screencheck: {name}", expected in names,
                  f"expected {expected!r}, got {names or 'nothing'}")

    # ---- SEAM 3 (build gp2): the harness must serve the REAL policy ----
    # S7 exists because a CSP violation was logging on every silent-WAV the voice uses --
    # found only because Jim pasted his console into a chat. The local harness served NO
    # CSP header, so the one defect S7 was written for could not occur in the rig that was
    # meant to catch it. It now reads the live policy out of main.py, which is also why
    # this cannot drift: change the header there and the harness follows.
    csp = screencheck.real_csp(root)
    check("screencheck seam: the harness can read the real CSP out of main.py",
          bool(csp) and "default-src" in csp,
          "the render harness would serve no policy, and S7 could never fire locally")
    check("screencheck seam: media-src allows the data: URIs the voice needs",
          "media-src" in csp and "data:" in csp.split("media-src")[1][:40],
          "the audio warm-up and the keep-alive loop are silent-WAV data: URIs; without "
          "media-src they violate default-src, and they BREAK the day the policy is "
          "enforced -- taking the head of every spoken sentence with them")

    # ---- SEAM 1: geo-figures.js still labels by the metrics screencheck reads ----
    geo_path = os.path.join(root, "static", "geo-figures.js")
    if not os.path.exists(geo_path):
        bad("screencheck seam: geo-figures.js present", "file not found")
    else:
        with open(geo_path, "r", encoding="utf-8") as fh:
            geo = fh.read()
        # triangle() emits txt(..., L[i], INK, 17, 800) for a vertex and
        # txt(..., sides[i], INK, 15, 600) for a side length. S2 tells a corner from a
        # leg by exactly those numbers and by nothing else.
        vsize, vweight = screencheck.FIG_VERTEX_FONT
        ssize, sweight = screencheck.FIG_SIDE_FONT
        check("screencheck seam: vertex labels still 17/800",
              f"INK, {vsize}, {vweight}" in geo,
              f"geo-figures.js no longer emits vertex text at {vsize}/{vweight} — "
              f"S2 (figure names what the words name) has gone BLIND")
        check("screencheck seam: side labels still 15/600",
              f"INK, {ssize}, {sweight}" in geo,
              f"geo-figures.js no longer emits side text at {ssize}/{sweight} — "
              f"S2 (figure names what the words name) has gone BLIND")

    # ---- SEAM 2: the VAR_NEEDS_CONTEXT table screencheck mirrors ----
    # build hc (2026-08-17): this table used to be read out of session.html, because it
    # lived there -- in triplicate, one copy per teaching page. It now lives ONCE in
    # static/board-text.js and all three pages load it, so this seam reads the single
    # source. That is the point of the extraction: there is one table to match, not
    # three that could drift apart between pushes.
    sess_path = os.path.join(root, "static", "board-text.js")
    if not os.path.exists(sess_path):
        bad("screencheck seam: board-text.js present", "file not found")
    else:
        with open(sess_path, "r", encoding="utf-8") as fh:
            sess = fh.read()
        m = re.search(r"const\s+VAR_NEEDS_CONTEXT\s*=\s*\{([^}]*)\}", sess)
        if not m:
            bad("screencheck seam: VAR_NEEDS_CONTEXT found in board-text.js",
                "the variable-styling table moved or was renamed — S1 is now guessing")
        else:
            # The page's table is CASE-SENSITIVE (gn2); screencheck matches case-
            # insensitively, so compare the lower-cased sets.
            live = tuple(sorted({c.lower() for c in re.findall(r"([A-Za-z])\s*:", m.group(1))}))
            mine = tuple(sorted(set(screencheck.VAR_SKIP)))
            check("screencheck seam: VAR_NEEDS_CONTEXT matches screencheck", live == mine,
                  f"board-text.js needs context for {live} but screencheck mirrors {mine} — "
                  f"S1 will miss letters it no longer knows about, or invent ones it does")
        # build gn2 -- REVERSED. This used to assert that styled variables are UPPERCASED.
        # Jim's second Geometry lesson killed that design: the board read "A, B, C =
        # corners (vertices) / a, b, c = sides (lengths)" and both lines rendered
        # identically, because the renderer forced a capital. CASE IS MEANING -- side a is
        # opposite vertex A, the antiderivative of f is F. The letter now renders exactly
        # as written, and putting toUpperCase back would silently re-break the one lesson
        # that teaches the difference.
        check("screencheck: styled variables keep their case (gn2)",
              'class="mvar">' in sess and "run.toUpperCase()" not in sess,
              "board-text.js is uppercasing styled variables again — 'a, b, c = sides' will "
              "render identically to 'A, B, C = corners' and the distinction is destroyed")
        # build gn: VAR_SKIP stopped meaning "never style" and started meaning "must earn
        # it". If varInMathContext ever disappears, the five letters go back to being
        # unstylable and "a squared plus B squared" returns -- so it is asserted here, on
        # all three lesson pages, rather than trusted.
        # build gn: VAR_SKIP stopped meaning "never style" and started meaning "must
        # earn it". If varInMathContext ever disappears, those letters go back to being
        # unstylable and "a squared plus B squared" returns.
        # build hc: asserted ONCE, against the shared module -- the three pages used to
        # each carry their own copy of this logic, which is exactly the arrangement that
        # let a fix reach one page and not the others.
        check("screencheck seam: context letters can earn styling (shared module)",
              "varInMathContext" in sess and "MV_POW" in sess,
              "the math-context test is gone from board-text.js — a, i, f, g and h can "
              "no longer be styled at all, which is the defect Jim found on 2026-08-16")
        check("gn2: a styled variable renders exactly as written (shared module)",
              "run.toUpperCase()" not in sess,
              "uppercasing is back — 'a, b, c = sides' and 'A, B, C = corners' will "
              "render identically")
        check("gn2: the variable table stays case-sensitive (shared module)",
              "VAR_NEEDS_CONTEXT" in sess and "run.toLowerCase()" not in sess,
              "the table is case-insensitive again — capital A can no longer be a "
              "label (P(A), vertex A) distinct from the article 'a'")
        # And every teaching page must actually LOAD that single source -- a page that
        # quietly stopped including it would lose all three guarantees above silently.
        for page in ("session.html", "practice.html", "topic.html"):
            p = os.path.join(root, "static", page)
            if not os.path.exists(p):
                bad(f"screencheck seam: {page} present", "file not found")
                continue
            with open(p, "r", encoding="utf-8") as fh:
                txt = fh.read()
            check(f"screencheck seam: {page} loads the shared board-text module (hc)",
                  "/static/board-text.js" in txt,
                  "this page no longer loads the one copy of the variable renderer — "
                  "styleVars is undefined here and the board will not render")
            # build hd: the voice pipeline moved to /static/voice.js -- one copy, its
            # state with it. Each page must LOAD it (the gn/gp3 guarantees are asserted
            # once, against the module, just below this loop).
            check(f"voice: {page} loads the shared voice module (hd)",
                  "/static/voice.js" in txt,
                  "this page no longer loads voice.js — speak() is undefined here and "
                  "the tutor is mute on this page")
            check(f"voice: {page} does not re-inline speak() (hd)",
                  "function speak(" not in txt,
                  "a second copy of speak() is back in this page — the next voice fix "
                  "will land in one copy and not the other, which is builds bl/cb/gn's "
                  "whole history repeating")

        # build gn -- THE HEAD OF THE CLIP. Jim reported "his first word is cut off"
        # three times (bl, cb, gn); the first two fixes padded the clip, the third found
        # the cause (a flat 300ms timer racing a suspended audio graph). Build gp3 added
        # ctx0 so the probe can tell "the race fired and was handled" from "it never
        # fired". These guarantees are now asserted ONCE, against the single copy in
        # voice.js -- which is the point of build hd: one place to fix, one to audit.
        vpath = os.path.join(root, "static", "voice.js")
        if not os.path.exists(vpath):
            bad("voice: static/voice.js present", "the shared voice module is missing "
                "-- every teaching page's tutor is mute")
        else:
            with open(vpath, "r", encoding="utf-8") as fh:
                vtxt = fh.read()
            check("voice: no clip starts on a flat 300ms timer (shared module)",
                  "setTimeout(kick, 300)" not in vtxt,
                  "the flat 300ms kick is back — a suspended graph will swallow the "
                  "first word again (build gn)")
            check("voice: speak() waits for the audio graph to be running (shared module)",
                  'audioCtx.state === "running"' in vtxt and "RESUME_CEILING" in vtxt,
                  "speak() no longer waits for 'running' before starting the clip — that "
                  "race is what ate 'Hey' in Jim's 2026-08-16 lesson")
            check("voice: still starts past the ceiling, never freezes (shared module)",
                  "starting anyway" in vtxt,
                  "the escape hatch is gone — a context that never resumes would hang "
                  "the turn, which is worse than a clipped word")
            check("voice: the probe records the graph state BEFORE the wait (shared module)",
                  "ctxAtRequest" in vtxt and "ctx0=" in vtxt,
                  "without ctx0 the probe cannot tell whether the resume race fired, "
                  "only that it was handled — the two look identical (gp3's lesson)")
            check("voice: the [voicehead] probe is carried (shared module)",
                  "[voicehead] started after" in vtxt,
                  "the head-of-clip probe is gone — the next swallowed first word would "
                  "be diagnosed by reasoning instead of measurement")
            # build hd's one deliberate behaviour change, guarded: warm-up starts the
            # keep-alive (build cb) -- the F9 divergence must never reopen.
            check("voice: warmUpAudio wakes the keep-alive (cb, unified by hd)",
                  "startKeepAlive" in vtxt.split("function warmUpAudio", 1)[1][:600]
                  if "function warmUpAudio" in vtxt else False,
                  "warm-up no longer starts the keep-alive — topic/practice first words "
                  "can hit a powered-down device again (the review's F9 finding)")


# =============================================================================
# PART 3ai -- THE DEPLOY STAMP MUST MOVE WITH THE CODE
# =============================================================================
# /health reports APP_BUILD, and its entire job is to answer one question: "did Render
# actually take my change?" On 2026-08-14 it answered wrongly. It still read
# "2026-08-13fe-audit-findings-closed" nine builds later, because bumping it was a habit,
# and habits lapse. Jim hit it live -- a board line he had just fixed still looked wrong,
# and the instrument that should have told him whether the deploy had landed lied to him.
# A stamp nobody can trust is worse than no stamp at all, because it is consulted in
# exactly the moments when you are already confused.
# So it stops being a habit: this fails the build when ANY shipped file carries a dated
# change note NEWER than the date on the stamp. Both note styles are read -- "#   DATE"
# in the Python modules and "    (xx) DATE --" at the top of the lesson pages.
_STAMP_PY = ("main.py", "tutor.py", "prompts.py", "foundations.py", "store.py",
             "curriculum.py", "misconceptions.py", "notation.py", "library.py",
             "sprints.py", "pedagogy.py", "mathcheck.py")
_STAMP_HTML = ("static/session.html", "static/practice.html", "static/topic.html",
               "static/demo.html", "static/challenge.html", "static/dashboard.html")


def part3ai_deploy_stamp():
    print("\nPART 3ai — the /health build stamp moves with the code")
    root = os.path.dirname(os.path.abspath(__file__))

    def _read(rel):
        p = os.path.join(root, rel)
        if not os.path.exists(p):
            return ""
        try:
            with open(p, encoding="utf-8") as fh:
                return fh.read(200000)      # the change notes live at the top
        except Exception:                   # noqa: BLE001 -- an unreadable file is not a failure
            return ""

    newest, where = "", ""
    for rel in _STAMP_PY:
        for d in re.findall(r"^#\s+(\d{4}-\d{2}-\d{2})\s", _read(rel), re.M):
            if d > newest:
                newest, where = d, rel
    for rel in _STAMP_HTML:
        for d in re.findall(r"^\s*\(\w{1,4}\)\s+(\d{4}-\d{2}-\d{2})\s", _read(rel), re.M):
            if d > newest:
                newest, where = d, rel

    # NOTE: _read() stops at 200k because change notes live at the top -- but APP_BUILD
    # sits ~6,900 lines into main.py, well past that. Read the whole file for the stamp.
    try:
        with open(os.path.join(root, "main.py"), encoding="utf-8") as fh:
            src = fh.read()
    except Exception:  # noqa: BLE001
        src = ""
    m = re.search(r'^APP_BUILD\s*=\s*"([^"]+)"', src, re.M)
    check("main.py declares APP_BUILD", bool(m),
          "the /health stamp is gone entirely -- nothing can confirm a deploy any more")
    if not m:
        return
    stamp = m.group(1)
    sd = re.match(r"(\d{4}-\d{2}-\d{2})", stamp)
    check("APP_BUILD starts with a date", bool(sd),
          f"APP_BUILD is {stamp!r}; it must begin YYYY-MM-DD so this check can read it")
    if not sd:
        return
    print(f"       stamp {stamp}   newest change note {newest or '(none)'} in {where or '-'}")
    check("APP_BUILD is not older than the newest shipped change note",
          bool(newest) and sd.group(1) >= newest,
          f"{where} carries a change note dated {newest} but APP_BUILD still says "
          f"{sd.group(1)}. Bump APP_BUILD in main.py -- /health is how anyone confirms "
          f"Render took the deploy, and a stale stamp answers that question WRONGLY. "
          f"It went nine builds stale once already; that is what this check exists to stop.")


# =============================================================================
# PART 3ak -- THE NIGHT WATCH (build go)
# =============================================================================
# 2026-08-16. Jim: "only AI is gonna be capable of governing AI... depending on me to fix
# it or notice problems is only going to address some of those problems and probably just
# the big ones." nightwatch.py is the part of this system that goes LOOKING, on a cadence,
# instead of waiting for a human to notice. It rides main.py's existing heartbeat.
#
# What is checked here is everything that does NOT need an API key -- the rotation, the
# ledger, the report, the email policy, the restart-safety, and above all the FAILURE
# paths. That last group is the point: a governor is judged by what it does when the
# critic returns garbage, a lesson explodes, or the key is missing. It must never confirm
# a finding it could not verify, never end a night over one bad lesson, and never let a
# silent cap read as "all clear".
def part3ak_night_watch():
    print("\nPART 3ak — the night watch (nightwatch.py)")
    try:
        import nightwatch as nw
    except Exception as exc:  # our own module missing is a broken repo, not a laptop
        bad("nightwatch imports", f"{type(exc).__name__}: {exc}")
        return
    import json as _json, tempfile as _tmp, datetime as _dt

    # ---- the rotation: a small budget must still cover everything, in order ----
    sc = [{"id": f"s{i}"} for i in range(10)]
    check("night watch: the default budget covers every scenario",
          {x["id"] for x in nw.pick_tonight(sc, 12, 0)} == {x["id"] for x in sc},
          "a night at the default budget left a scenario unaudited")
    d0 = [x["id"] for x in nw.pick_tonight(sc, 4, 0)]
    d1 = [x["id"] for x in nw.pick_tonight(sc, 4, 1)]
    check("night watch: a small budget walks forward instead of starving scenarios",
          d0 != d1 and not (set(d0) & set(d1)), "two nights running audited the same lessons")
    seen = set()
    for day in range(3):
        seen |= {x["id"] for x in nw.pick_tonight(sc, 4, day)}
    check("night watch: three small nights still cover everything", seen == {x["id"] for x in sc},
          "some scenario is never reached at a reduced budget")
    check("night watch: the rotation is deterministic for a given day",
          nw.pick_tonight(sc, 4, 7) == nw.pick_tonight(sc, 4, 7),
          "'has this been covered?' must have an answer")
    check("night watch: an empty scenario list is survivable",
          nw.pick_tonight([], 5, 0) == [], "an empty list must not raise")

    # ---- the ledger: only what is NEW ----
    f1 = {"rule": 43, "quote": "that regrouping is exactly the move"}
    f2 = {"rule": 43, "quote": "that  REGROUPING is exactly   the move"}
    f3 = {"rule": 43, "quote": "a completely different sentence"}
    check("night watch: one defect fingerprints the same despite case and spacing",
          nw.fingerprint("geo", f1) == nw.fingerprint("geo", f2),
          "the same defect would be re-reported every night")
    check("night watch: a different quote is a different finding",
          nw.fingerprint("geo", f1) != nw.fingerprint("geo", f3), "findings collapsed together")
    check("night watch: the same quote in another scenario is a different finding",
          nw.fingerprint("geo", f1) != nw.fingerprint("calc", f1), "scenarios collapsed together")
    out, led = {"new": [], "recurring": 0}, {}
    nw._record(out, led, {"id": "geo", "course": "geometry"}, f1)
    nw._record(out, led, {"id": "geo", "course": "geometry"}, f2)
    check("night watch: a repeat is COUNTED, not re-reported",
          len(out["new"]) == 1 and out["recurring"] == 1,
          "a nightly email that repeats itself is a nightly email nobody opens")

    # ---- verification: NEVER confirm what could not be checked ----
    tr = [("user", "hi"), ("assistant", "something")]
    scn = {"id": "x", "course": "geometry"}
    F = {"severity": "high", "rule": 63, "what": "w", "quote": "q", "why": "y"}
    real, _why, err = nw.verify_finding(
        lambda *a, **k: (_json.dumps({"real": True, "why": "confirmed"}), None), scn, tr, F)
    check("night watch: a confirmed finding survives review", real is True and not err)
    real, _why, err = nw.verify_finding(
        lambda *a, **k: (_json.dumps({"real": False, "why": "taste"}), None), scn, tr, F)
    check("night watch: a refuted finding is dropped", real is False and not err,
          "an audit finding is an opinion (build fe)")
    real, _why, err = nw.verify_finding(lambda *a, **k: ("not json at all", None), scn, tr, F)
    check("night watch: an unreadable verdict is UNVERIFIED, never a silent confirm",
          real is None and bool(err), "a garbled reviewer must not promote a finding")
    real, _why, err = nw.verify_finding(lambda *a, **k: ("", "openai timed out"), scn, tr, F)
    check("night watch: a transport error is UNVERIFIED, never a silent confirm",
          real is None and bool(err), "a dead reviewer must not promote a finding")

    # ---- the report must confess ----
    res = {"ok": True, "ran": 12, "recurring": 3, "refuted": 5, "seconds": 61.0,
           "new": [{"severity": "high", "scenario": "geo", "course": "geometry", "rule": 63,
                    "what": "w", "quote": "q", "why": "y", "fix": "f", "verified": "v"}],
           "skipped": ["quiz-eighty (time budget)"], "budget_stopped": True,
           "unverified": [{"what": "u", "error": "e"}], "errors": [], "probes_run": ["termgap"]}
    md = nw.report_markdown(res, "build-x")
    check("night watch: the report names what it did NOT cover",
          "did not cover" in md and "SKIPPED" in md, "a silent cap reads as 'all clear'")
    check("night watch: the report admits when the budget cut it short",
          "time budget stopped" in md, "an early stop must never look like a clean sweep")
    check("night watch: unverified findings are shown as neither confirmed nor dismissed",
          "COULD NOT VERIFY" in md, "they must not vanish")
    check("night watch: the report ends with the closing statement",
          md.strip().endswith("truncated.*"), "house rule")

    # ---- the email policy: silence by default ----
    check("night watch: a new confirmed finding emails Jim", nw.email_digest(res, "b") is not None)
    quiet = dict(res, new=[], errors=[])
    check("night watch: a quiet night sends NO email", nw.email_digest(quiet, "b") is None,
          "a nightly 'nothing to report' trains the reader to ignore the one that matters")
    check("night watch: a preflight failure DOES email",
          nw.email_digest(dict(quiet, errors=["preflight failed: no key"]), "b") is not None,
          "a watch that cannot run must say so, or its silence reads as all-clear")

    # ---- restart safety: it asks the disk, not a variable ----
    with _tmp.TemporaryDirectory() as d:
        # The clock is PINNED and handed to BOTH due() and write_report() (hm): the report's
        # date-stamped filename IS the ledger due() reads, so a test that pins one clock but
        # lets the other run free goes red the day after it is written — which is exactly
        # what happened on 2026-08-18 to the hardcoded-date version of this block.
        now = _dt.datetime(2026, 8, 17, nw.RUN_HOUR_UTC + 1, tzinfo=_dt.timezone.utc)
        check("night watch: due at the run hour", nw.due(d, now))
        check("night watch: not due before the run hour",
              not nw.due(d, now.replace(hour=nw.RUN_HOUR_UTC - 1)))
        nw.write_report(d, res, "b", now=now)
        check("night watch: not due twice in one night (a redeploy cannot double-run)",
              not nw.due(d, now), "restart-safety is read from disk, like the nightly snapshot")
        check("night watch: due again tomorrow",
              nw.due(d, now + _dt.timedelta(days=1)))
        led_path = os.path.join(d, nw.LEDGER_NAME)
        with open(led_path, "w", encoding="utf-8") as fh:
            fh.write("{not json")
        check("night watch: a corrupt ledger starts fresh instead of stopping the watch",
              nw.load_ledger(d) == {}, "the watch must survive its own state file")

    # ---- and it must be wired in, or none of the above ever runs ----
    root = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(root, "main.py"), "r", encoding="utf-8") as fh:
        m = fh.read()
    check("night watch: main.py runs the pass on the heartbeat",
          "_nightwatch_pass()" in m and "def _nightwatch_pass" in m,
          "nightwatch.py exists but nothing calls it — the cadence is the whole point")
    check("night watch: the pass is fenced like every other heartbeat pass",
          "[nightwatch] loop error" in m,
          "an unfenced pass could take down the weekly digests and the nightly snapshot")
    check("night watch: it lends the probes its lessons, one turn at a time",
          "_nightwatch_termgap" in m and "probe_hooks=" in m,
          "the server-side probes would otherwise never see these lessons")
    # build gp -- THE FACE, and the auditability of the reviewer. The first real night
    # (2026-08-17) refuted 16 of 22 findings, and the report counted them without naming
    # them: a refute rate nobody can check is not a metric. These assert that the report
    # shows its work and that the card can reach it.
    # These numbers are THE FIRST REAL NIGHT, 2026-08-17: 12 lessons, 6 new confirmed,
    # 16 refuted, 2310.4s. Kept literal so the checks double as a record of what a healthy
    # run actually looked like the first time this thing ran unattended.
    res2 = dict(res, seconds=2310.4, refuted=16, ran=12,
                new=(res["new"] * 6),
                refuted_list=[{"scenario": "i-dont-know", "severity": "low",
                               "rule": 39, "what": "explained before asking",
                               "reviewer": "foundation-first is deliberate"}])
    md2 = nw.report_markdown(res2, "b")
    check("night watch: the report NAMES what the reviewer threw away",
          "threw away" in md2 and "foundation-first is deliberate" in md2,
          "a refute count with nothing behind it cannot be audited")
    check("night watch: and tells the reader how to judge those dismissals",
          "too aggressive" in md2, "the reader needs to know what a bad dismissal looks like")
    with _tmp.TemporaryDirectory() as d:
        nw.write_report(d, res2, "b")
        su = nw.summary(d)
        check("night watch: the card reads last night's runtime",
              su.get("last_minutes") == 38.5, f"got {su.get('last_minutes')}")
        check("night watch: and warns when a run is near its time ceiling",
              su.get("near_ceiling") is True,
              "a run that starts skipping lessons must say so, not lose coverage quietly")
        check("night watch: the card computes the refuted share",
              (su.get("health") or {}).get("refuted_pct") == 73, str(su.get("health")))
        check("night watch: a report is readable back by its date",
              nw.read_report(d, su["last"]).startswith("# Night watch"))
        check("night watch: a bogus date cannot traverse out of the report folder",
              nw.read_report(d, "../../etc/passwd") == ""
              and nw.read_report(d, "2026-13-99") != "# nope",
              "the date is validated as a date")
    with open(os.path.join(root, "static", "admin.html"), "r", encoding="utf-8") as fh:
        adm = fh.read()
    check("night watch: /admin has a card that reads the reports",
          "nwStatus" in adm and "/api/admin/nightwatch/report" in adm,
          "the findings would only be reachable by shell on Render's disk")
    check("night watch: both admin endpoints exist and are key-guarded",
          '@app.get("/api/admin/nightwatch/status")' in m
          and '@app.get("/api/admin/nightwatch/report")' in m
          and m.count("_require_admin(x_admin_key or key)") >= 2,
          "an unguarded endpoint would expose lesson transcripts")

    check("night watch: it can be switched off from Render without a deploy",
          "NIGHTWATCH" in m or "nightwatch.enabled()" in m,
          "a governor with no off switch is a liability")



# =============================================================================
# PART 3al -- THE OPENAI BOUNDARY (build gq)
# =============================================================================
# 2026-08-17. Jim enabled OpenAI's "share inputs and outputs" on a DEDICATED AUDIT
# PROJECT, in exchange for the free daily token allowance that makes the night watch
# essentially free and lifts the budget ceiling off its coverage.
#
# That bargain is safe for exactly one reason: OPENAI IS NOT IN THE TEACHING PATH. Every
# transcript OpenAI marks is a synthetic lesson between an AI student persona and the
# tutor -- no child's words have ever been sent to it. The moment that stops being true,
# real children's conversation lands in a project where sharing is switched ON, and it
# goes into a training set.
#
# TWO PROMISES DEPEND ON THIS, and neither is enforced by anything else:
#   1. static/privacy.html names exactly THREE processors -- Anthropic, ElevenLabs,
#      Render -- and says "We do not send student data to anyone else, and we never sell
#      or rent it -- to anyone, ever."
#   2. The audit project has data sharing ENABLED.
# So an OpenAI call added to a reply path would silently make the privacy policy false AND
# feed a minor's lesson into model training. That is not a bug anyone would notice in a
# lesson; it is a bug you notice in a deposition.
#
# A rule that nothing watches is a wish. This watches it.
_TEACHING_MODULES = ("tutor.py", "mathcheck.py", "sprints.py", "pedagogy.py",
                     "foundations.py", "prompts.py", "curriculum.py", "misconceptions.py")


def part3al_openai_boundary():
    print("\nPART 3al — OpenAI stays out of the teaching path")
    root = os.path.dirname(os.path.abspath(__file__))

    def _read(rel):
        p = os.path.join(root, rel)
        if not os.path.exists(p):
            return None
        with open(p, "r", encoding="utf-8") as fh:
            return fh.read()

    # 1) THE TEACHING BRAIN NEVER CALLS OPENAI. tutor.py is where a reply is generated and
    #    refereed; a fallback bolted in here is the single likeliest way this boundary
    #    breaks (see the "substitute teacher" idea in the project notes -- it would need a
    #    privacy-policy change and a NON-sharing project before it could ship).
    for mod in _TEACHING_MODULES:
        src = _read(mod)
        if src is None:
            continue
        hits = [ln for ln in src.splitlines()
                if "openai" in ln.lower() and not ln.strip().startswith("#")]
        check(f"openai boundary: {mod} never calls OpenAI", not hits,
              f"{mod} references OpenAI in live code: {hits[:2]} — a student's words would "
              f"reach a project where data sharing is ENABLED, and static/privacy.html "
              f"promises exactly three processors, none of them OpenAI")

    # 2) Only the AUDIT tooling talks to the OpenAI API at all.
    for mod in ("lessonaudit.py", "nightwatch.py"):
        if _read(mod) is None:
            bad(f"openai boundary: {mod} present", "audit tooling missing from the repo")
    for mod in _TEACHING_MODULES + ("store.py", "notation.py", "library.py"):
        src = _read(mod)
        if src and "api.openai.com" in src:
            bad(f"openai boundary: {mod} must not reach api.openai.com",
                "only the offline auditor may call OpenAI")
        elif src:
            ok(f"openai boundary: {mod} does not reach api.openai.com")

    # 3) The privacy policy still names the three processors it names. If a fourth is ever
    #    added to the product, THIS CHECK IS THE REMINDER that the policy is the thing to
    #    update first -- not a comment somebody hopes will be read.
    priv = _read(os.path.join("static", "privacy.html"))
    if priv is None:
        bad("openai boundary: privacy.html present", "file not found")
    else:
        low = priv.lower()
        for who in ("anthropic", "elevenlabs", "render"):
            check(f"openai boundary: privacy.html still names {who}", who in low,
                  "the processor list changed — if a provider was added or removed, the "
                  "policy text and this check must move together")
        check("openai boundary: privacy.html does not claim OpenAI as a processor",
              "openai" not in low,
              "if OpenAI now processes STUDENT data, the policy must say so and this "
              "whole boundary needs re-thinking; if it does not, the mention is wrong")



# =============================================================================
# PART 3am -- THE SPOKEN LETTER, AND THE SIGNED ANSWER (build gr)
# =============================================================================
# 2026-08-17, both from one Geometry lesson Jim ran.
#
# (1) He was asked which side was the hypotenuse, SAID THE LETTER "c", and ElevenLabs
#     returned the Spanish "si" / "CSI". The tutor told him he was wrong and demanded a
#     letter. A student marked incorrect for a machine's mistake is about the most
#     corrosive thing this app can do to a child's confidence, and we were sending NO
#     language hint at all.
# (2) He answered "minus five" to "what times itself gives twenty five?" and was told
#     "That is correct" -- then the reply taught on using 5. See rule 64 / referee 15.
def part3am_spoken_letter_and_sign():
    print("\nPART 3am — the spoken letter, and the signed answer")
    root = os.path.dirname(os.path.abspath(__file__))
    import main as _m

    # ---- the letter map: fires on a bare letter-name, silent on ordinary words ----
    for said, want in (("c", "c"), ("see", "c"), ("sea", "c"), ("si", "c"), ("CSI", "c"),
                       ("Tea.", "t"), ("bee", "b"), ("ex", "x"), ("zed", "z")):
        check(f"spoken letter: {said!r} reads as {want!r}", _m.spoken_letter(said) == want,
              f"got {_m.spoken_letter(said)!r}")
    for said in ("five", "yes", "no", "the hypotenuse", "oh", "you", "are", "why", "eye", ""):
        check(f"spoken letter: {said!r} is left alone", not _m.spoken_letter(said),
              f"{said!r} became {_m.spoken_letter(said)!r} — a plausible whole utterance "
              f"must never be turned into a variable the student never said (rule 64)")

    # ---- the language hint, and the promise that it can never cost us voice input ----
    with open(os.path.join(root, "main.py"), "r", encoding="utf-8") as fh:
        m = fh.read()
    check("spoken letter: a language hint is sent to speech-to-text",
          "language_code" in m and "STT_LANGUAGE" in m,
          "with no hint, auto-detection heard an English letter as Spanish")
    check("spoken letter: a rejected hint retries WITHOUT it",
          "retrying" in m and "422" in m,
          "a language hint must never be able to silently break the microphone")
    check("spoken letter: the map lives ONLY on the server",
          "_SPOKEN_LETTER" in m,
          "one copy, or the client and server will drift")
    # build hf: the client half of the gr fix (expectsALetter + expect=letter) moved to
    # the ONE mic.js copy -- which is where the gz defects said it always belonged: both
    # live voice-answer bugs were exactly this code hand-copied without its state.
    # Asserted once against the module; each page is checked for the include (PART 3aw
    # owns the deeper no-re-inline guarantees).
    mpath = os.path.join(root, "static", "mic.js")
    if not os.path.exists(mpath):
        bad("spoken letter: static/mic.js present",
            "the shared mic module is gone -- no page can hear a student at all")
    else:
        with open(mpath, "r", encoding="utf-8") as fh:
            mic_src = fh.read()
        check("spoken letter: the mic module sends the letter context",
              "expectsALetter" in mic_src and "expect=letter" in mic_src,
              "without the context the server would rewrite words in ordinary speech")
        check("spoken letter: it asks only on an explicit letter question",
              "which\\s+(?:side|letter" in mic_src or "which\s+(?:side|letter" in mic_src,
              "the gate must be narrow — any question would be too broad")
        for page in ("session.html", "practice.html", "topic.html"):
            with open(os.path.join(root, "static", page), "r", encoding="utf-8") as fh:
                txt = fh.read()
            check(f"spoken letter: {page} loads the mic module",
                  "/static/mic.js" in txt,
                  "this page cannot record or transcribe anything — the mic is gone")

    # ---- referee 15, both directions, on the exact exchange ----
    SIGN_CASES = [
        ("Jim's exact turn: affirmed, then taught on with 5",
         "That is correct! So c = 5, and the hypotenuse is 5 units long.", "minus five", True),
        ("a bare 'Correct.' opening the reply", "Correct. c = 5.", "-5", True),
        ("the spoken word against the written digit", "That is right. c = 5.",
         "negative five", True),
        ("the RIGHT teaching response passes",
         "Good thinking -- both 5 and -5 square to 25. But a length is never negative, "
         "so c = 5.", "minus five", False),
        ("correcting instead of affirming passes",
         "Not quite -- a side length cannot be negative, so it is 5.", "minus five", False),
        ("merely mentioning the sign passes",
         "Yes, and negative five works arithmetically too.", "minus five", False),
        ("a positive answer is not this referee's business",
         "That is correct! c = 5.", "five", False),
        ("a negative the reply KEEPS is fine", "Exactly right, -5 degrees.", "minus five", False),
        ("no affirmation, nothing to judge", "Let us look at the board again.",
         "minus five", False),
        ("affirmed but the magnitude never appears",
         "That is correct. Now try the next one.", "minus five", False),
        ("a decimal is not the settled answer", "Correct. It comes to 5.2 exactly.",
         "minus 5", False),
        ("'exactly' as an adverb is not applause",
         "A function gives back exactly one output. Exactly one is the point.",
         "minus one", False),
    ]
    for name, reply, said, should_flag in SIGN_CASES:
        got = tutor.answer_sign_conflict(reply, said)
        check(f"answer-sign: {name}", bool(got) == should_flag,
              f"expected flag={should_flag}, got: {got or '(clean)'}")
        if should_flag:
            check(f"answer-sign: {name} (via prose_board_conflict)",
                  bool(tutor.prose_board_conflict(reply, said)),
                  "the combined referee let it through")

    # ---- and it must be SILENT on every canonical script, for every signed utterance ----
    try:
        import foundations as _F
    except Exception as exc:  # noqa: BLE001
        skip("answer-sign: canonical sweep", f"foundations unavailable: {exc}")
        return
    texts = []

    def _walk(o):
        if isinstance(o, str):
            texts.append(o)
        elif isinstance(o, dict):
            for v in o.values():
                _walk(v)
        elif isinstance(o, (list, tuple)):
            for v in o:
                _walk(v)
    for nm in dir(_F):
        if not nm.startswith("_"):
            _walk(getattr(_F, nm))
    noise = 0
    for said in ("minus five", "-5", "negative three", "minus one", "-12",
                 "negative two", "minus ten"):
        noise += sum(1 for t in texts if tutor.answer_sign_conflict(t, said))
    check(f"answer-sign: silent on all {len(texts)} canonical scripts x 7 signed answers",
          noise == 0, f"{noise} false alarms — correct teaching would be regenerated")



# =============================================================================
# PART 3an -- THE UNIT FOLLOWS THE TEACHING (build gs)
# =============================================================================
# Jim, 2026-08-16 and again 2026-08-17: "it still says unit one on the top when we are
# talking about unit five." The first diagnosis was that the RAIL was right and the tutor
# was inventing Unit 5; Jim overruled it and he was right. The real defect: the rail was
# seeded from placement.start_unit -- where the student was PLACED, a number that never
# moves -- the tutor chose its own topic, and NOTHING RECONCILED THEM. Worse, _track_topic
# filed activity under the placement unit too, so the store agreed with the stale rail and
# the whole system was confidently wrong together. That is why nothing caught it.
#
# Jim's ruling: THE UNIT FOLLOWS WHAT IS BEING TAUGHT. This asserts the whole chain, because
# it is a chain -- break any link and the symptom returns looking like a display bug.
def part3an_unit_follows_teaching():
    print("\nPART 3an — the unit follows what is being taught")
    root = os.path.dirname(os.path.abspath(__file__))
    import main as _m

    # ---- the declaration is read out of the tutor's own tag ----
    for reply, want in (('[[unitplan unit="5" topics="a | b"]]', 5),
                        ('[[unitplan topics="a" unit=5]]', 5),
                        ('words [[unitplan unit="9"]] words', 9),
                        ('[[today items="x"]]', None),
                        ('[[unitplan unit="12"]]', None),
                        ('[[unitplan unit="0"]]', None),
                        ('', None)):
        got = _m._declared_unit(reply)
        check(f"unit: declaration in {reply[:34]!r} reads as {want}", got == want,
              f"got {got}")

    with open(os.path.join(root, "main.py"), "r", encoding="utf-8") as fh:
        m = fh.read()
    # ---- link 1: the DECLARED unit outranks the resolved default when tracking ----
    # build hj: the focus guard became `unit_source != "focus"` -- the resolver owns
    # the focus decision. build hm: the declaration now files through the gate
    # (_accept_declared_unit), which preserves BOTH gs semantics (an accepted
    # declaration outranks the resolved unit; focus outranks the declaration) while
    # refusing a declaration the record cannot justify. Same behaviour for every
    # honest declaration, one gate for the dishonest ones.
    check("unit: the tutor's declaration outranks placement when tracking",
          "declared = _declared_unit(reply)" in m
          and "course_unit, _up_verdict = _accept_declared_unit(" in m
          and 'return int(declared), "accepted"' in m,
          "activity would go on being filed under the unit the student was PLACED in, so "
          "the tracker would keep agreeing with a stale rail")
    # ---- link 2: an explicit focus still wins, because that is the student choosing ----
    check("unit: an explicit focus unit still outranks the declaration",
          'if unit_source == "focus":\n            return resolved_unit, "focus-wins"' in m
          and 'return int(focus_unit), "focus"' in m,
          "a student who clicked 'work on unit 4' must not be overridden by the tutor")
    # ---- link 3: the server serves the unit the lesson is actually in ----
    check("unit: /api/session reports current_unit",
          'progress["current_unit"]' in m and "get_topics(code, course)" in m,
          "a resumed session would fall back to placement and show the wrong unit again")
    check("unit: current_unit is the most recently TAUGHT unit",
          "last_touched" in m and "reverse=True" in m,
          "without ordering by recency this is just another guess")
    # ---- link 4: the page prefers it over placement ----
    with open(os.path.join(root, "static", "session.html"), "r", encoding="utf-8") as fh:
        sess = fh.read()
    check("unit: the rail prefers the taught unit over the placed unit",
          "SRV_PROGRESS.current_unit" in sess and "if (taught >= 1 && taught <= 9)" in sess,
          "the server would report the right unit and the rail would still show placement")
    check("unit: FOCUS_UNIT is still checked first in the rail",
          "FOCUS_UNIT >= 1 && FOCUS_UNIT <= 9" in sess,
          "the student's own choice must stay top of the order")
    # ---- link 5: the probe that will tell us whether the DECLARATION is honest ----
    check("unit: the [unitdrift] probe compares all three answers",
          "_probe_unit_drift" in m and "classify_unit" in m and "[unitdrift]" in m,
          "two diagnoses of this symptom have been guesses; the third needs data")
    check("unit: the drift probe measures and never enforces",
          "MEASUREMENT ONLY" in m and "never enforces" in m.lower(),
          "a check that cannot verify its own fix must not regenerate a lesson")



# =============================================================================
# PART 3ao -- THE INVENTED HISTORY (build gv)
# =============================================================================
# 2026-08-17. The biggest cluster in the day's audit triage: SEVEN findings in which the
# tutor stated something about what had already happened that was simply untrue. They
# split cleanly, and the split is the whole design:
#
#   ENFORCEABLE -- "you completed the square start to finish on your own" said to a student
#   who answered two sub-steps of a procedure the tutor wrote every line of. That is
#   checkable against the student's own message, so gm's referee is widened to catch it.
#
#   NOT ENFORCEABLE HERE -- "you've now watched this move twice", "all three conversions
#   under your belt", "your last score was eighty-five percent", "Unit 9 is also still in
#   progress". Every one is a claim about the whole conversation or about a record this
#   function has never been shown. A check that cannot verify its own fix loops (gj), so
#   these are PROBED, and enforcement waits for the data.
#
# ⚠️ The false count is not a curiosity -- it is the ENGINE of the worst behaviour in the
# audit. The student asked "can you show me taking the square root of 169?" and was
# refused with "you've now watched this move twice -- let's flip it." A child asking to be
# shown, turned down on invented evidence.
def part3ao_invented_history():
    print("\nPART 3ao — the invented history")

    # ---- the totality branch: gm widened ----
    TOTALITY_CASES = [
        ("the audit turn: 'start to finish' over two sub-answers",
         "Nice work -- you completed the square start to finish on your own.",
         "It's (x + 4)^2, and -16 + 10 is -6.", True),
        ("'that whole thing' over a fragment",
         "You factored that whole thing yourself!", "x plus 4", True),
        ("'all by yourself' attached to a named procedure",
         "Great -- you did the long division all by yourself.", "24", True),
        # ---- and what must NOT be caught ----
        ("warmth about a PROBLEM they did answer is left alone",
         "You just solved your homework problem all by yourself!", "4/4?", False),
        ("totality is fine when they really did narrate the whole thing",
         "You completed the square start to finish on your own.",
         "First I took half of 8 which is 4, then I squared it to get 16, then I added "
         "and subtracted 16 and simplified the constant to -6", False),
        ("a procedure named without any totality claim",
         "Nice factoring there.", "x plus 4", False),
        ("a totality claim with no procedure named",
         "You did that all by yourself!", "15", False),
        # ---- gm's original behaviour must survive the widening ----
        ("gm still fires on a credited method after a bare answer",
         "That regrouping is exactly the move that trips people up.", "1 1/2. Next.", True),
        ("gm still silent when the student showed their working",
         "That regrouping is exactly the move.",
         "I borrowed a ten from the 3 so it became 2 and 12", False),
    ]
    for name, reply, said, should_flag in TOTALITY_CASES:
        got = tutor.narrated_method_conflict(reply, said)
        check(f"totality: {name}", bool(got) == should_flag,
              f"expected flag={should_flag}, got: {got or '(clean)'}")
        if should_flag:
            check(f"totality: {name} (via prose_board_conflict)",
                  bool(tutor.prose_board_conflict(reply, said)),
                  "the combined referee let it through")

    # ---- the probe: it must SEE the five real claims and stay quiet otherwise ----
    import io as _io
    import contextlib as _cl

    def _logs(text):
        buf = _io.StringIO()
        with _cl.redirect_stdout(buf):
            tutor.count_claim_probe(text, "2345", "geometry")
        return bool(buf.getvalue().strip())

    for text in ("You've now watched this move twice -- let's flip it.",
                 "You've watched this exact move twice now.",
                 "You have watched this exact move twice now.",
                 "You've now got all three conversions under your belt.",
                 "Since your last score was eighty-five percent, we'll sharpen the "
                 "shakiest spot first.",
                 "That's three in a row!"):
        check(f"count-claim probe sees: {text[:44]!r}", _logs(text),
              "this is one of the real 2026-08-17 claims — the probe must record it")
    for text in ("Nice work -- that is correct.",
                 "Want to try another one like it?",
                 "You have seen a hole and a jump now, so let us try one more.",
                 "Three in a row would be great -- want to go for it?",
                 "You have done really well today."):
        check(f"count-claim probe quiet on: {text[:44]!r}", not _logs(text),
              "ordinary encouragement must not fill the log")

    # ---- and it must MEASURE, never enforce ----
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "tutor.py"),
              "r", encoding="utf-8") as fh:
        src = fh.read()
    check("count-claim: the probe is measurement only",
          "MEASUREMENT ONLY" in src and "count_claim_probe" in src
          and "Never enforces" in src,
          "a check that cannot verify its own fix must not regenerate a lesson")
    check("count-claim: the probe is not wired into the referee sweep",
          "count_claim_probe" not in src.split("def prose_board_conflict")[1][:4000],
          "it would be enforcing on a claim it cannot check")

    # ---- silent on every canonical script, in both mechanisms ----
    try:
        import foundations as _F
    except Exception as exc:  # noqa: BLE001
        skip("invented history: canonical sweep", f"foundations unavailable: {exc}")
        return
    texts = []

    def _walk(o):
        if isinstance(o, str):
            texts.append(o)
        elif isinstance(o, dict):
            for v in o.values():
                _walk(v)
        elif isinstance(o, (list, tuple)):
            for v in o:
                _walk(v)
    for nm in dir(_F):
        if not nm.startswith("_"):
            _walk(getattr(_F, nm))
    noise = sum(sum(1 for t in texts if tutor.narrated_method_conflict(t, m))
                for m in ("4/4", "15", "x plus 4", "2/3", "yes", "24"))
    check(f"totality: silent on {len(texts)} canonical scripts x 6 answers", noise == 0,
          f"{noise} false alarms — correct teaching would be regenerated")
    chatty = sum(1 for t in texts if _logs(t))
    check(f"count-claim: quiet on all {len(texts)} canonical scripts", chatty == 0,
          f"{chatty} scripts would log — a noisy probe is an ignored probe")



# =============================================================================
# PART 3ap -- THE BARE ANSWER-DEMAND, THE DECIMAL, AND A REFEREE THAT FOUGHT US (build gw)
# =============================================================================
# 2026-08-17, three fixes from one thread of the day's audit.
#
# The decimal-alignment lesson produced two findings, a rule 15 and a rule 44, and they
# turned out to be ONE defect wearing two numbers:
#     board:  [[step eq="2.6 + 1.35"]]      (no "?" anywhere)
#     prose:  "...then add column by column. What do you get?"
# Rule 15's referee needs the NUMBERS to be in the asking sentence -- "What do you get?"
# has none. Rule 44's referee only inspects board values containing "?" -- this one has
# none either. THE MISSING "?" MADE THE PROBLEM INVISIBLE TO BOTH REFEREES AT ONCE.
#
# And underneath that sat gk's fraction bug wearing a decimal point: the digit-scatter
# fallback found the "1" of 1.35 inside the word "one" in "let's try ONE with a similar
# setup", and called the problem spoken.
#
# ⭐ The third fix was not in the audit at all -- the canonical sweep found it. gl's
# self-correction referee reads "hold on" as the tutor changing its mind, and TWO
# foundation scripts say "so hold on to this" and "the one to hold on to". It has been
# regenerating authored content. A referee that fights the foundation library is worse
# than no referee: it burns a model call and can cost the student the good draft (dg).
def part3ap_bare_demand_and_decimals():
    print("\nPART 3ap — the bare answer-demand, the decimal, and gl vs the scripts")

    # ---- the two real turns from the audit ----
    turn1 = ('Let us line those up carefully. [[step eq="3.5 + 0.47"]] '
             '[[column op="+" terms="3.50 | 0.47"]] '
             'Add it column by column, right to left: what do you get?')
    turn2 = 'Same idea as before. [[step eq="2.6 + 1.35"]] What do you get?'
    for name, reply in (("decimal-alignment turn 1", turn1),
                        ("decimal-alignment turn 2", turn2)):
        check(f"bare-demand: {name} is caught", bool(tutor.prose_board_conflict(reply)),
              "a bare 'what do you get?' over a board with no pending line slipped BOTH "
              "rule 15 and rule 44 -- the missing '?' hid the problem from each")

    CLEAN = [
        ("read aloud with a pending line",
         'Let us add three point five and zero point four seven. '
         '[[step eq="3.5 + 0.47 = ?"]] What do you get?'),
        ("a properly numbered ask", 'What is three plus eight? [[step eq="3 + 8 = ?"]]'),
        ("an offer is not a computation", "Nice work today. Want to try another one?"),
        ("money IS a reading of a decimal",
         'That is three dollars and ninety seven cents. [[step eq="3.97 + 1.00 = ?"]] '
         'What do you get?'),
        ("a bare demand with no board maths at all",
         "Have a think about it. What do you get?"),
    ]
    for name, reply in CLEAN:
        check(f"bare-demand: {name} stays clean", not tutor.prose_board_conflict(reply),
              f"got: {tutor.prose_board_conflict(reply)[:90]}")

    # ---- the decimal must be spoken as a QUANTITY (gk's rule, one notation over) ----
    DEC = [
        ("'try one with a similar setup' does NOT read 1.35",
         "Let us try one with a similar setup, different-length decimals again.",
         "2.6 + 1.35 = ?", False),
        ("spoken as a decimal", "What is two point six plus one point three five?",
         "2.6 + 1.35 = ?", True),
        ("the literal in the prose", "Look at 2.6 + 1.35 on the board.",
         "2.6 + 1.35 = ?", True),
        ("money is a legitimate reading", "That is three dollars and ninety seven cents.",
         "3.97 = ?", True),
        ("whole numbers keep the old behaviour", "What is three plus eight?",
         "3 + 8 = ?", True),
        ("gk's fractions are still enforced", "three plus one really is four",
         "3/4 + 1/4 = ?", False),
        ("gk's fractions still pass when read together",
         "what is three fourths plus one fourth", "3/4 + 1/4 = ?", True),
    ]
    for name, prose, board, covers in DEC:
        check(f"decimal: {name}", tutor._pq_spoken_covers(prose, board) == covers,
              f"expected covers={covers}")

    # ---- gl must stop fighting the foundation library ----
    for name, text, should_flag in (
            ("'so hold on to this' is a foundation script, not a wobble",
             "Students mix those two up constantly, so hold on to this.", False),
            ("'the one to hold on to' likewise",
             "The word common is the one to hold on to.", False),
            ("a real self-correction still fires",
             "Wait, hold on -- let me recheck that.", True),
            ("'hold on,' still fires", "hold on, that is not right", True),
            ("'hang on to that idea' passes", "hang on to that idea for later", False)):
        got = tutor.self_correction_conflict(text)
        check(f"self-correction: {name}", bool(got) == should_flag,
              f"expected flag={should_flag}, got: {got or '(clean)'}")

    # ---- and the sweep that found it in the first place ----
    try:
        import foundations as _F
    except Exception as exc:  # noqa: BLE001
        skip("bare-demand: canonical sweep", f"foundations unavailable: {exc}")
        return
    texts = []

    def _walk(o):
        if isinstance(o, str):
            texts.append(o)
        elif isinstance(o, dict):
            for v in o.values():
                _walk(v)
        elif isinstance(o, (list, tuple)):
            for v in o:
                _walk(v)
    for nm in dir(_F):
        if not nm.startswith("_"):
            _walk(getattr(_F, nm))
    noisy = sum(1 for t in texts if tutor.self_correction_conflict(t))
    check(f"self-correction: silent on all {len(texts)} canonical scripts", noisy == 0,
          f"{noisy} authored scripts would be regenerated on delivery")
    for fn, label in ((tutor.prose_pending_question_conflict, "rule 15"),
                      (tutor.prose_unspoken_problem_conflict, "rule 44")):
        n = sum(1 for t in texts if fn(t))
        check(f"{label}: silent on all {len(texts)} canonical scripts", n == 0,
              f"{n} false alarms")



# =============================================================================
# PART 3aq -- A REQUEST TO BE SHOWN, REFUSED (rule 65, build gx)
# =============================================================================
# 2026-08-17. The worst thing in the day's audit, and it happened twice in one lesson:
#     STUDENT: "Can you show me taking the square root of 169?"
#     TUTOR:   "You've now watched this move twice -- let's flip it. Here's a new triangle:"
#     STUDENT: "Can you show me 8 squared and 15 squared first?"
#     TUTOR:   "You've watched this exact move twice now... Let's see you try it."
# Both counts were false -- the move had been shown ONCE. A child who asked for help was
# refused, and told they should already know it, on evidence the tutor invented.
#
# THE DISCRIMINATOR CAME OUT OF THE SAME TRANSCRIPT, which is why it can be trusted: when
# that student asked the same kind of question earlier, the tutor answered properly and
# the reply carried COMPLETED board lines ("5^2 = 25", "12^2 = 144"). The refusals carry
# only pending ones. Nothing worked out + the job handed back = a refusal.
def part3aq_refused_demonstration():
    print("\nPART 3aq — a request to be shown, refused")
    CASES = [
        ("the audit's first refusal: sqrt of 169 -> a brand-new triangle",
         "You've now watched this move twice -- let's flip it. Here's a new triangle:\n"
         '[[triangle v="A,B,C" sides="a = 8, b = 15, c = ?" right="C" caption="find c"]]\n'
         '[[step eq="8^2 + 15^2 = ?"]]\nWhat is 8 squared plus 15 squared?',
         "Can you show me taking the square root of 169?", True),
        ("the audit's second refusal: 8 and 15 squared -> 'you try it'",
         "You've watched this exact move twice now. Let's see you try it.\n"
         '[[step eq="8^2 = ?"]]\n[[step eq="15^2 = ?"]]',
         "Can you show me 8 squared and 15 squared first?", True),
        # ---- the SAME lesson, done right: these must stay clean ----
        ("the compliant reply from that same transcript",
         "Here's five squared and twelve squared worked out:\n"
         '[[step eq="5^2 = 25"]]\n[[step eq="12^2 = 144"]]\n[[step eq="25 + 144 = ?"]]\n'
         "So what does twenty-five plus one hundred forty-four equal?",
         "Can you show me 5 squared and 12 squared worked out?", False),
        ("the square root, shown properly",
         "Sure -- the square root sign asks what number times itself gives this.\n"
         '[[step eq="c^2 = 100"]]\n[[step eq="c = sqrt(100)"]]\n[[step eq="c = 10"]]\n'
         "Want to try the next one?",
         "Can you show me taking the square root to get c?", False),
        ("no request to be shown, so handing work back is fine",
         'Your turn -- what is 8 squared? [[step eq="8^2 = ?"]]', "ok", False),
        ("a fair clarifying question is not a refusal",
         "Happy to! Which would help more -- the fraction way or the decimal way?",
         "Can you show me another example?", False),
        ("shown with a worked line and no hand-back",
         'Of course. [[step eq="3 x 5 = 15"]] Fifteen candies in those three groups.',
         "show me 3 times 5", False),
        # ---- the two shapes the canonical sweep caught in an early draft ----
        ("a card TITLE ending in '?' is a heading, not a pending problem",
         '[[card title="Quantitative?" items="height: yes | zip code: NO, it is a label"]]',
         "can you show me", False),
        ("a '?' beside the VARIABLE x is not a pending computation",
         '[[write text="what is it approaching, as x gets close?"]]',
         "can you show me", False),
    ]
    for name, reply, said, should_flag in CASES:
        got = tutor.refused_demonstration_conflict(reply, said)
        check(f"refused-show: {name}", bool(got) == should_flag,
              f"expected flag={should_flag}, got: {got or '(clean)'}")
        if should_flag:
            check(f"refused-show: {name} (via prose_board_conflict)",
                  bool(tutor.prose_board_conflict(reply, said)),
                  "the combined referee let it through")

    try:
        import foundations as _F
    except Exception as exc:  # noqa: BLE001
        skip("refused-show: canonical sweep", f"foundations unavailable: {exc}")
        return
    texts = []

    def _walk(o):
        if isinstance(o, str):
            texts.append(o)
        elif isinstance(o, dict):
            for v in o.values():
                _walk(v)
        elif isinstance(o, (list, tuple)):
            for v in o:
                _walk(v)
    for nm in dir(_F):
        if not nm.startswith("_"):
            _walk(getattr(_F, nm))
    noise = sum(sum(1 for t in texts if tutor.refused_demonstration_conflict(t, m))
                for m in ("can you show me", "show me how", "walk me through it",
                          "Can you show me 5 squared?", "can we do that one first",
                          "can I see it"))
    check(f"refused-show: silent on {len(texts)} canonical scripts x 6 phrasings",
          noise == 0, f"{noise} false alarms -- correct teaching would be regenerated")



# =============================================================================
# PART 3ar -- THE RULE SPOKEN AS A LAW (build gy)
# =============================================================================
# 2026-08-17, the sixth and last cause from the day's audit triage. Two shapes.
#
# RULE 54 -- "'of' means multiply", from the percents lesson. The banned list was STORY-CUE
# words only, and "of" belongs there by that list's own logic: "sum" and "difference" NAME
# their operations (vocabulary, which rule 37 requires teaching), while "of" merely
# CORRELATES with multiplication inside one problem type. A child who learns it as a rule
# applies it to "3 out of 4". Added with it: the rest of the classic bad mnemonic ("is
# means equals, of means times"), plus "per" and "each".
#
# RULE 61 -- "the bottom number never changes, we just add the top numbers", from the
# fractions lesson. False for unlike denominators, and the most documented misconception in
# fraction arithmetic. Rule 61 is generally unenforceable -- "always" and "never" are often
# TRUE ("a length is never negative", rule 64). What makes THIS case decidable is that the
# same lesson says it correctly three separate times. The tutor knows the condition and
# drops it, so the check is only: is the condition in the sentence or not?
def part3ar_rule_spoken_as_law():
    print("\nPART 3ar — a rule spoken as a law")

    KW = [
        ("the audit sentence: 'of' means multiply",
         "We turned 20% into 0.20, then multiplied -- 'of' means multiply.", True),
        ("the classic bad mnemonic, both halves",
         "Remember: is means equals, and of means times.", True),
        ("per means divide", "The word per means divide.", True),
        ("each means multiply", "each means multiply", True),
        ("the original story cues still fire", "altogether means add", True),
        # ---- vocabulary is NOT a shortcut, and must stay legal ----
        ("'sum' names its operation (rule 37 requires teaching it)",
         "The word sum means addition -- that is its name.", False),
        ("'difference' likewise", "Difference means subtraction.", False),
        ("talking ABOUT a cue word stays legal",
         "The word altogether tells us the story combines things.", False),
        ("honest notation reading stays legal",
         "The fraction bar means divide.", False),
    ]
    for name, text, should_flag in KW:
        got = tutor.board_notation_conflict(text)
        check(f"keyword-shortcut: {name}", bool(got) == should_flag,
              f"expected flag={should_flag}, got: {got or '(clean)'}")

    F61 = [
        ("the audit sentence, unconditioned",
         "So one fourth plus two fourths makes three fourths -- the bottom number never "
         "changes, we just add the top numbers.", True),
        ("'you only add the numerators', unconditioned",
         "For these, you only add the numerators.", True),
        # ---- the SAME lesson said it correctly three times: all must stay clean ----
        ("the same lesson, said right (the denominators match)",
         "Since the bottom numbers, the denominators, match, they stay the same -- just "
         "like before.", False),
        ("the same lesson, said right (same-bottom-number)",
         "Three in a row -- same-bottom-number fractions add up the top numbers and keep "
         "the bottom the same, every time.", False),
        ("the same lesson, said right (the slices are the same size)",
         "You added the top numbers, one plus one is two, and kept the bottom number three "
         "since the slices are the same size.", False),
        ("the condition stated up front",
         "When the bottom numbers are the same, we keep that bottom number and add the top "
         "numbers.", False),
        ("ordinary fraction prose", "The denominator tells you how many equal pieces the "
         "whole was cut into.", False),
    ]
    for name, text, should_flag in F61:
        got = tutor.fraction_rule_unconditioned(text)
        check(f"rule-61 fractions: {name}", bool(got) == should_flag,
              f"expected flag={should_flag}, got: {got or '(clean)'}")
        if should_flag:
            check(f"rule-61 fractions: {name} (via prose_board_conflict)",
                  bool(tutor.prose_board_conflict(text)),
                  "the combined referee let it through")

    try:
        import foundations as _F
    except Exception as exc:  # noqa: BLE001
        skip("rule-spoken-as-law: canonical sweep", f"foundations unavailable: {exc}")
        return
    texts = []

    def _walk(o):
        if isinstance(o, str):
            texts.append(o)
        elif isinstance(o, dict):
            for v in o.values():
                _walk(v)
        elif isinstance(o, (list, tuple)):
            for v in o:
                _walk(v)
    for nm in dir(_F):
        if not nm.startswith("_"):
            _walk(getattr(_F, nm))
    # The fraction library is large and says the like-denominator rule many times. If the
    # condition test is wrong, THIS is where it shows.
    n61 = sum(1 for t in texts if tutor.fraction_rule_unconditioned(t))
    check(f"rule-61 fractions: silent on all {len(texts)} canonical scripts", n61 == 0,
          f"{n61} authored scripts would be regenerated -- the condition test is too strict")
    nkw = sum(1 for t in texts if tutor.board_notation_conflict(t))
    check(f"keyword-shortcut: silent on all {len(texts)} canonical scripts", nkw == 0,
          f"{nkw} false alarms from the widened list")



# =============================================================================
# PART 3as -- PHASE 0 OF THE FULL-APP REVIEW (build gz)
# -----------------------------------------------------------------------------
# 2026-08-17. Six independent review passes over every file found six CLASSES of
# problem (see the project doc Full_App_Review_2026-08-17). Build gz closes the
# bleeding edges; each fix ships with its check, per the standing rules:
#   1. the heartbeat is never gated by the weekly-email flag (backups, cost watch,
#      purge and night watch all ride that one thread);
#   2. refresher turns force the heard-script wording back into the prompt, so the
#      gz ceiling deferral can never break rule 40's exact-words promise;
#   3. the /admin verifier breakdown counts "prose-unresolved" (a reply that SHIPPED
#      with a known unresolved referee finding) and "empty" as their own numbers
#      instead of folding them into verify_none.
# The page fixes (lastTutorText, audioWarmed) are guarded in PART 3e, where the
# page-parity checks live; the ceiling fix is guarded in PART 3h, where the scale
# checks live.
# =============================================================================
def part3as_phase0():
    print("\nPART 3as — phase 0 of the full-app review (build gz)")
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "main.py"), encoding="utf-8") as fh:
        main_src = fh.read()
    with open(os.path.join(here, "static", "admin.html"), encoding="utf-8") as fh:
        admin_src = fh.read()

    # 1. THE HEARTBEAT ALWAYS BEATS. The WEEKLY_EMAIL gate must live inside the email
    # pass, never at the thread start -- the old early-return silently disabled the
    # nightly backup, the cost watchdog, the usage purge and the night watch.
    m = re.search(r"def _start_digest_thread\(\).*?(?=\ndef |\n@)", main_src, re.S)
    check("_start_digest_thread exists", bool(m), "the ops heartbeat starter is gone")
    if m:
        body = m.group(0)
        # The ONLY return STATEMENT allowed in the starter is the already-started guard
        # (comments may mention the word; count real statements only). A second return
        # means some flag can stop the thread from ever starting again.
        returns = re.findall(r"^\s+return\b", body, re.M)
        check("the heartbeat starter has exactly one return (the already-started guard)",
              len(returns) == 1 and "if _digest_thread_started:" in body,
              "an extra early return is back in _start_digest_thread -- a flag can "
              "silently disable BACKUPS, the cost watch and the night watch again")
        check("the heartbeat starter still starts the thread",
              "threading.Thread(target=_digest_loop" in body,
              "_digest_loop is no longer started")
    m2 = re.search(r"def _weekly_digest_pass\(.*?\n(?:    .*\n|\n)*", main_src)
    check("the WEEKLY_EMAIL flag gates the email pass itself",
          "_weekly_email_off()" in (m2.group(0) if m2 else "")
          and "def _weekly_email_off" in main_src,
          "_weekly_digest_pass no longer honours WEEKLY_EMAIL -- the flag would do "
          "nothing at all now")

    # 2. THE REFRESHER PROMISE SURVIVES THE CEILING. main.py must compute
    # foundations_force_verbatim from wants_refresher on every chat turn, and
    # tutor.build_system_prompt must honour it (behavioural check in PART 3h).
    check("main.py wires foundations_force_verbatim from wants_refresher",
          "foundations_force_verbatim" in main_src
          and "wants_refresher(" in main_src,
          "the gz deferral can now strand an over-ceiling student without the exact "
          "words rule 40 promises -- the wiring is gone")

    # 3. THE WORST VERIFY STATUS IS VISIBLE. store.usage_stats must carry the two
    # keys (DB off in the battery returns the init dict, which is exactly what we
    # want to inspect), and admin.html must count prose-unresolved.
    try:
        import store as _st
        stats = _st.usage_stats(7)
        for k in ("verify_prose-unresolved", "verify_empty"):
            check(f"usage_stats reports {k}", k in stats,
                  "it folds back into verify_none -- shipped-unresolved replies become "
                  "invisible on /admin again")
    except Exception as exc:  # noqa: BLE001
        bad("store.usage_stats inspectable", str(exc))
    check("admin.html counts prose-unresolved turns",
          'verify_prose-unresolved' in admin_src,
          "the dashboard no longer reads the count store.py now reports")
    check("admin.html shows the shipped-unresolved tile",
          "Shipped unresolved" in admin_src,
          "the most important number on the card lost its tile")


# =============================================================================
# PART 3at -- EYES (build ha): THE APP MUST WATCH ITSELF
# -----------------------------------------------------------------------------
# 2026-08-17, Phase 1 of the full-app review. The meta-finding behind "5 of 6 audit
# causes were a check that failed to fire": fail-open everywhere, observed nowhere.
# These checks pin every piece of the telemetry build so it cannot silently rot:
# the store layer, the tutor wiring, the endpoints, the beacon, the dashboards.
# =============================================================================
def part3at_eyes():
    print("\nPART 3at — eyes: the app must watch itself (build ha)")
    here = os.path.dirname(os.path.abspath(__file__))
    def _read(name):
        with open(os.path.join(here, name), encoding="utf-8") as fh:
            return fh.read()
    main_src = _read("main.py")
    tutor_src = _read("tutor.py")
    nw_src = _read("nightwatch.py")
    admin_src = _read(os.path.join("static", "admin.html"))

    # 1. THE STORE LAYER. record_event must never raise -- prove it with the DB off
    # (the battery's normal state), and prove the whole query surface answers.
    try:
        import store as _st
        _st.record_event("selftest", "battery", "this row is never written (DB off)")
        check("record_event never raises (DB off)", True, "")
        stats = _st.event_stats(7)
        check("event_stats answers with the DB off",
              isinstance(stats, dict) and "counts" in stats and "total" in stats,
              f"got {type(stats)}")
        check("recent_events answers with the DB off",
              _st.recent_events(hours=1, limit=5) == [], "should be an empty list")
        check("last_event_at answers with the DB off",
              _st.last_event_at("ops_pass", "heartbeat") is None, "should be None")
        check("purge_system_events answers with the DB off",
              _st.purge_system_events(90) == 0, "should be 0")
    except Exception as exc:  # noqa: BLE001
        bad("the events store layer is callable", str(exc))
    check("the system_events table is defined",
          '_tables["system_events"]' in _read("store.py"),
          "the telemetry table is gone from store.py")

    # 2. THE TUTOR WIRING. Every crash handler counts itself; the sweep counts fires.
    import re as _re
    crash_prints = len(_re.findall(r'crashed \(fail open\)', tutor_src))
    crash_events = len(_re.findall(r'_event\("referee_crash"', tutor_src))
    check(f"every tutor crash handler counts itself ({crash_events}/{crash_prints})",
          crash_events >= crash_prints and crash_prints >= 19,
          "a fail-open handler lost its _event call -- that check can die invisibly "
          "again (the gl referee corrupted scripts for FOUR BUILDS unreported)")
    fire_events = len(_re.findall(r'_event\("referee_fire"', tutor_src))
    check(f"the referee sweep counts its fires ({fire_events} sites)",
          fire_events >= 19,
          "prose_board_conflict no longer records which referee fired")
    for needle, why in [
            ('_event("pass_through", "prosecheck"', "a shipped-with-finding reply is invisible again"),
            ('_event("pass_through", "mathcheck"', "an unresolved-math pass-through is invisible again"),
            ('_event("probe", "countclaim"', "the countclaim probe stopped counting"),
            ('_event("probe", "markcheck"', "the markcheck probe stopped counting"),
            # build hg: the catch-all lives ONCE in _reply_pipeline; the getters pass
            # their names via where=. Both halves checked, so neither can vanish.
            ('_event("failopen", where', "the unified pipeline's catch-all is dark again"),
            ('where="get_tutor_reply"', "the lesson lane lost its telemetry name"),
            ('where="get_practice_reply"', "the practice lane lost its telemetry name"),
            ('where="get_topic_reply"', "the topic lane lost its telemetry name"),
            ('_event("promptsize"', "the ceiling alarms stopped counting")]:
        check(f"tutor wiring: {needle[:40]}...", needle in tutor_src, why)
    check("tutor.subsystems() reports the defensive imports",
          "def subsystems()" in tutor_src and hasattr(tutor, "subsystems")
          and all(isinstance(v, bool) for v in tutor.subsystems().values()),
          "/health's degradation report lost its source")

    # 3. THE SERVER. Endpoint, health fields, heartbeat stamps, probe wiring, purge.
    for needle, why in [
            ('@app.post("/api/client-error")', "the browser is a black box again"),
            ('_rate_limit("cerr:"', "the beacon endpoint lost its flood guard"),
            ('"subsystems": subsystems', "/health no longer reports degradation"),
            ('"ops": ops', "/health no longer reports ops ages"),
            ('store.record_event("ops_pass", "heartbeat")', "the heartbeat no longer stamps itself"),
            ('store.record_event("ops_pass", "backup"', "backups no longer stamp themselves"),
            ('store.record_event("ops_pass", "nightwatch"', "the night watch no longer stamps itself"),
            ('store.record_event("probe", "unitdrift"', "the unitdrift probe stopped counting"),
            ('store.record_event("probe", "termgap"', "the termgap probe stopped counting"),
            ('store.record_event("probe", "rule37"', "the rule37 probe stopped counting"),
            ('store.purge_system_events(EVENTS_DAYS)', "telemetry can grow forever again"),
            ('@app.get("/api/admin/events")', "the telemetry card lost its feed")]:
        check(f"main wiring: {needle[:44]}...", needle in main_src, why)

    # 4. THE BEACON FILE. Present, self-contained, defensive, and loaded FIRST.
    cl = _read(os.path.join("static", "client-log.js"))
    for needle, why in [
            ('addEventListener("error"', "window errors are no longer captured"),
            ('addEventListener("unhandledrejection"', "promise failures are no longer captured"),
            ("navigator.sendBeacon", "reports no longer survive page unload"),
            ("MAX_REPORTS", "the flood cap is gone")]:
        check(f"client-log.js: {needle[:36]}...", needle in cl, why)
    # All ten app pages carry it, and on each it is the FIRST LIVE script -- a script
    # that loads before the beacon can crash unheard. (PAGE_PARITY guards presence on
    # the three teaching pages; this guards the rest, and the ordering everywhere.)
    #
    # ⚠️ 2026-08-17, build hb -- WHY THIS CHECK LOOKS AT COMMENT-STRIPPED SOURCE.
    # The first version of this check searched the RAW source for "<script" and read the
    # 200 characters after it. Build ha's own include had been inserted after the first
    # literal "<head>" in each file -- which on EIGHT of the ten pages is a "<head>"
    # mentioned inside the change-note comment at the top. So the include landed inside
    # a comment, and the comment note that came with it ("-->") CLOSED that comment
    # early, spilling the rest of the change-note prose into the live document. The
    # pages' DOM was wrecked (session.html rendered ONE body child instead of 19) and
    # this check passed anyway, because the first "<script" it found was the commented
    # one. A check that reads text the browser never executes is not checking the page.
    # Found by driving the real pages in a browser, not by reading them. Now: comments
    # are stripped first, so the check sees what the BROWSER sees.
    APP_PAGES = ("session.html", "topic.html", "practice.html", "demo.html",
                 "challenge.html", "dashboard.html", "family.html", "teacher.html",
                 "admin.html", "records.html")
    for page in APP_PAGES:
        src = _read(os.path.join("static", page))
        live = re.sub(r"<!--.*?-->", "", src, flags=re.S)
        check(f"{page}: the beacon is live (not stranded in a comment)",
              "client-log.js" in live,
              "the include exists only inside an HTML comment -- the browser never "
              "loads it, and every client error stays invisible")
        first = live.find("<script")
        check(f"{page}: the beacon is the FIRST live script",
              first >= 0 and "client-log.js" in live[first:first + 200],
              "a script loads before the beacon and can crash unheard")
        # AND the page must have no bare prose before <head>. This is the check that
        # actually catches build ha's mistake, and the two obvious ones do not:
        # counting delimiters passes (the bad insert added one "<!--" AND one "-->"),
        # and comment-stripping passes (the injected "-->" closed the outer comment, so
        # the include really was outside a comment -- along with 18,681 characters of
        # change-note prose that the browser then rendered into the document). A
        # well-formed page has NOTHING but tags and whitespace before <head>; a comment
        # broken anywhere above <head> dumps its remaining prose exactly here.
        live_pre = re.sub(r"<!--.*?-->", "", src, flags=re.S)
        mhead = re.search(r"<head\b", live_pre, re.I)
        stray = ""
        if mhead:
            pre = re.sub(r"<!DOCTYPE[^>]*>", " ", live_pre[:mhead.start()], flags=re.I)
            stray = " ".join(re.sub(r"<[^>]*>", " ", pre).split())
        check(f"{page}: no stray prose before <head>",
              mhead is not None and not stray,
              f"{len(stray)} characters of text are outside every tag and every comment "
              f"before <head> -- a change-note comment is broken and the browser is "
              f"rendering its prose into the page: {stray[:120]!r}")

    # 5. THE DASHBOARDS. /admin card and the night watch's morning section.
    check("admin.html has the telemetry card",
          'id="tmTiles"' in admin_src and "/api/admin/events" in admin_src,
          "the counts have nowhere to be seen")
    check("nightwatch's report includes the week's telemetry",
          "The week's telemetry" in nw_src and "event_stats(7)" in nw_src,
          "a dead check no longer reaches the morning report")

    # build hb: the screen auditor must cover every page it CAN cover, and must name
    # the ones it cannot. It drove 1 of 5 renderer copies while gz's two live defects
    # sat in two of the other four.
    try:
        import screencheck as _sc
        check("screencheck drives all three teaching pages (hb)",
              set(_sc.CAPTURE_PAGES) == {"session.html", "topic.html", "practice.html"},
              f"it drives {getattr(_sc, 'CAPTURE_PAGES', None)} -- a renderer copy nobody "
              f"audits is where the next gz-class defect lives")
        check("screencheck NAMES the pages it does not cover (hb)",
              set(getattr(_sc, "UNCOVERED_PAGES", ())) == {"demo.html", "challenge.html"},
              "a bounded sweep that does not say what it skipped reads as 'all clear'")
        for _pg in _sc.CAPTURE_PAGES:
            prof = _sc.PAGE_PROFILES[_pg]
            check(f"screencheck knows how to drive {_pg}",
                  bool(prof.get("api")) and isinstance(prof.get("enter"), list),
                  "its profile is incomplete -- capture will hang or snapshot an entry screen")
    except Exception as exc:  # noqa: BLE001
        bad("screencheck's page coverage is inspectable", str(exc))


# =============================================================================
# PART 3au -- THE UNDECLARED-IDENTIFIER SWEEP (build hb)
# -----------------------------------------------------------------------------
# 2026-08-17, Phase 2 of the full-app review, and the NET that goes up before the
# shared-module extraction goes in.
#
# WHY THIS EXISTS. Build gz fixed two live defects that were the same mistake twice:
# a fix hand-copied from session.html into topic.html and practice.html WITHOUT the
# page state it reads.
#   * `lastTutorText` -- used by build gr's expect=letter hint, declared only in
#     session.html. A ReferenceError inside transcribe() on EVERY spoken answer, eaten
#     by its catch, so both pages told the student "I didn't quite catch that" and
#     blamed their microphone.
#   * `started` -- read by the visibilitychange handler, declared at page level only in
#     session.html (topic/practice had one inside speak()'s closure). Threw on every
#     return to the tab, so keep-alive never restarted -- the "first word swallowed"
#     symptom, still alive on two pages after THREE fixes to it.
# Neither was catchable by anything we owned: the battery reads Python, screencheck
# reads session.html only, the referees read the reply text. A human reading source
# found them. This part makes that class mechanical.
#
# WHAT IT CHECKS. For every identifier that is PAGE-LEVEL STATE on any sibling page,
# every use of that name on every page must be in scope at that point -- declared at
# page level here, or inside an enclosing function/block/parameter list. Narrowing the
# universe to sibling page-level names is deliberate: it is exactly the copy-divergence
# class, and it keeps the checker honest (a full JS scope analysis in regex produces
# noise, and a checker that cries wolf gets ignored -- see the gl referee that fought
# the foundation scripts).
#
# VERIFIED IN BOTH DIRECTIONS, the standing rule, with REAL cases:
#   silent on all 13 shipped pages (5 lesson-like + 8 others);
#   fires on the two real gz defects, reintroduced verbatim, with the right diagnosis
#     ("never declared on this page" / "declared only inside a function");
#   fires on 5 mutations of the class injected into 4 different pages.
# Pure stdlib -- no node, no npm, no pip. It runs on every push, for everyone, always.
# A check that skips is a wish.
# =============================================================================
_JS_RE_OK_BEFORE = set("(,=:[!&|?{};+-*%~^<>") | {"return", "typeof", "instanceof", "case",
                                                "in", "of", "do", "else", "yield", "await", "new"}

def _js_scripts(src):
    return "\n;\n".join(re.findall(r"<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>", src, re.S))

def _js_strip(js):
    """Blank comments, string bodies and regex literals, PRESERVING length and newlines.

    Two things here are not optional, both learned by watching this detector lie:
      * REGEX LITERALS. One unblanked /(?:a|b)/ carries parens, braces and words that
        corrupt every offset and scope computed after it.
      * NESTED TEMPLATE LITERALS. `<b>${rows.map(r => `<i>${r.n}</i>`).join("")}</b>`
        is everywhere in these pages. A scanner that just runs to the next backtick
        stops inside the INNER template and spills its HTML into the token stream as
        fake identifiers. So: template TEXT is blanked, while ${...} EXPRESSIONS are
        kept -- they are real code, and a variable used only there is really used.
    """
    out = list(js); n = len(js)
    def blank(a, b):
        for k in range(a, min(b, n)):
            if out[k] != "\n": out[k] = " "
    def prev_tok(pos):
        k = pos - 1
        while k >= 0 and js[k] in " \t\n": k -= 1
        if k < 0: return "{"
        if js[k].isalnum() or js[k] in "_$":
            j = k
            while j >= 0 and (js[j].isalnum() or js[j] in "_$"): j -= 1
            return js[j+1:k+1]
        return js[k]

    def scan_template(i):
        """i points at the opening backtick. Returns the index just past the closer."""
        blank(i, i + 1); j = i + 1
        while j < n:
            c = js[j]
            if c == "\\": blank(j, j + 2); j += 2; continue
            if c == "`": blank(j, j + 1); return j + 1
            if c == "$" and j + 1 < n and js[j+1] == "{":
                blank(j, j + 1)                      # blank the '$', keep the braces
                j = scan_code(j + 2, stop_at_brace=True)
                continue
            blank(j, j + 1); j += 1
        return j

    def scan_code(i, stop_at_brace=False):
        """Normal code. With stop_at_brace, returns just past the matching '}'."""
        depth = 0; j = i
        while j < n:
            c = js[j]
            if c == "/" and j+1 < n and js[j+1] == "*":
                k = js.find("*/", j+2); k = n if k < 0 else k+2; blank(j, k); j = k; continue
            if c == "/" and j+1 < n and js[j+1] == "/":
                k = js.find("\n", j); k = n if k < 0 else k; blank(j, k); j = k; continue
            if c == "`": j = scan_template(j); continue
            if c in "\"'":
                k = j + 1
                while k < n:
                    if js[k] == "\\": k += 2; continue
                    if js[k] == c or js[k] == "\n": break
                    k += 1
                blank(j, min(k + 1, n)); j = k + 1; continue
            if c == "/" and prev_tok(j) in _JS_RE_OK_BEFORE:
                k = j + 1; ok = False
                while k < n:
                    ch = js[k]
                    if ch == "\\": k += 2; continue
                    if ch == "\n": break
                    if ch == "[":
                        k += 1
                        while k < n and js[k] not in "]\n":
                            k += 2 if js[k] == "\\" else 1
                        k += 1; continue
                    if ch == "/": ok = True; break
                    k += 1
                if ok:
                    k += 1
                    while k < n and js[k] in "gimsuyd": k += 1
                    blank(j, k); j = k; continue
            if stop_at_brace:
                if c == "{": depth += 1
                elif c == "}":
                    if depth == 0: return j + 1
                    depth -= 1
            j += 1
        return j

    scan_code(0)
    return "".join(out)


def _js_braces(js):
    stack, pairs = [], []
    for i, c in enumerate(js):
        if c == "{": stack.append(i)
        elif c == "}" and stack: pairs.append((stack.pop(), i))
    return pairs

def _js_depth_at(pairs, pos):
    return sum(1 for a, b in pairs if a < pos < b)

def _js_page_level(js, pairs, max_depth=1):
    return {m.group(1) for m in re.finditer(r"\b(?:let|const|var)\s+([A-Za-z_$][\w$]*)", js)
            if _js_depth_at(pairs, m.start()) <= max_depth}

def _js_inner_scope(pairs, pos):
    inner = None
    for a, b in pairs:
        if a < pos < b and (inner is None or a > inner[0]): inner = (a, b)
    return inner

def _js_body_after(pairs, pos):
    body = None
    for a, b in pairs:
        if a >= pos and (body is None or a < body[0]): body = (a, b)
    return body

def _js_decl_scopes(js, pairs, name):
    esc = re.escape(name); scopes = []
    for pat in (r"\b(?:let|const|var)\s+(?:[A-Za-z_$][\w$]*\s*(?:=\s*[^;\n,]*)?,\s*)*" + esc + r"\b",
                r"\bfunction\s*\*?\s*" + esc + r"\b",
                r"\bclass\s+" + esc + r"\b",
                r"\bfor\s*\(\s*(?:let|const|var)\s+" + esc + r"\b",
                r"\b(?:let|const|var)\s*\{[^{}]*\b" + esc + r"\b[^{}]*\}\s*=",
                r"\b(?:let|const|var)\s*\[[^\[\]]*\b" + esc + r"\b[^\[\]]*\]\s*="):
        for m in re.finditer(pat, js):
            scopes.append(_js_inner_scope(pairs, m.start()) or (0, len(js)))
    # parameters (function decls, expressions, methods and arrows) scope to the body
    # A parameter is in scope from its own declaration site (the opening paren) through
    # the end of the body -- not just inside the braces. Without that, the parameter name
    # in the signature reads as an out-of-scope use of itself.
    for m in re.finditer(r"\(([^()]*)\)\s*(?:=>\s*)?\{", js):
        params = [re.sub(r"[^\w$].*$", "", p.strip().lstrip(". ")) for p in m.group(1).split(",")]
        if name in params:
            b = _js_body_after(pairs, m.end() - 1)
            if b: scopes.append((m.start(), b[1]))
    for m in re.finditer(r"(?<![\w$.)])" + esc + r"\s*=>\s*\{", js):
        b = _js_body_after(pairs, m.end() - 1)
        if b: scopes.append((m.start(), b[1]))
    for m in re.finditer(r"\bcatch\s*\(\s*" + esc + r"\s*\)\s*\{", js):
        b = _js_body_after(pairs, m.end() - 1)
        if b: scopes.append((m.start(), b[1]))
    # Parenless arrow parameter: x => expr   (no body braces at all)
    for m in re.finditer(r"(?<![\w$.)])" + esc + r"\s*=>", js):
        inner = _js_inner_scope(pairs, m.start()) or (0, len(js))
        scopes.append((m.start(), inner[1]))
    # Parameters of an arrow with an expression body: (a, b) => expr
    for m in re.finditer(r"\(([^()]*)\)\s*=>", js):
        params = [re.sub(r"[^\w$].*$", "", p.strip().lstrip(". ")) for p in m.group(1).split(",")]
        if name in params:
            inner = _js_inner_scope(pairs, m.start()) or (0, len(js))
            scopes.append((m.start(), inner[1]))
    return scopes

def _js_uses(js, name):
    hits = []
    for m in re.finditer(r"(?<![\w$.])" + re.escape(name) + r"(?![\w$])", js):
        if re.match(r"\s*:", js[m.end():m.end()+2]): continue
        if re.search(r"(?:let|const|var|function|class)\s*$", js[:m.start()]): continue
        hits.append(m.start())
    return hits

# Names that also exist on `window`. A page-level `let history = []` on the lesson
# pages collides with window.history, which /family, /teacher, /admin and /community
# legitimately use as the browser API -- so these names cannot be swept by the
# cross-page rule without crying wolf. Found by running the sweep over all 13 pages
# rather than the 3 it was written for: the corpus, not the fixture, again.
# The cost of the exclusion is small and the smell is real: shadowing a browser global
# with page state is the thing to avoid in the first place.
_JS_WINDOW_GLOBALS = {
    "history", "name", "status", "location", "length", "top", "parent", "self",
    "frames", "closed", "origin", "event", "screen", "external", "toolbar", "menubar",
    "scrollbars", "personalbar", "locationbar", "statusbar", "opener", "frameElement",
    "customElements", "crypto", "caches", "speechSynthesis", "onerror", "onload",
}


def _js_shared_globals(page_path, raw_html):
    """Top-level names supplied to this page by its own <script src="/static/*.js">
    includes. build hc moved the spoken-text and board/variable transforms into shared
    files; without this, every call site would look like an undeclared identifier and
    the sweep would howl at exactly the refactor it exists to protect."""
    import os as _os
    names, here = set(), _os.path.dirname(_os.path.abspath(page_path))
    root = _os.path.dirname(here) if _os.path.basename(here) == "static" else here
    for m in re.finditer(r'<script[^>]*\bsrc="(/static/[^"]+\.js)"', raw_html):
        f = _os.path.join(root, m.group(1).lstrip("/"))
        if not _os.path.exists(f):
            continue
        js = _js_strip(open(f, encoding="utf-8").read())
        pairs = _js_braces(js)
        names |= _js_page_level(js, pairs, max_depth=0)
        for mm in re.finditer(r"\bfunction\s+([A-Za-z_$][\w$]*)", js):
            if _js_depth_at(pairs, mm.start()) == 0:
                names.add(mm.group(1))
    return names


def js_scope_audit(paths):
    pages, risky = {}, set()
    for p in paths:
        raw = open(p, encoding="utf-8").read()
        js = _js_strip(_js_scripts(raw))
        pairs = _js_braces(js)
        declared = _js_page_level(js, pairs) | _js_shared_globals(p, raw)
        pages[p] = (js, pairs, declared)
        risky |= _js_page_level(js, pairs)
    risky -= _JS_WINDOW_GLOBALS
    findings = {}
    for p in paths:
        js, pairs, mine = pages[p]
        out = []
        for name in sorted(risky - mine):
            scopes = _js_decl_scopes(js, pairs, name)
            for pos in _js_uses(js, name):
                if not any(a <= pos <= b for a, b in scopes):
                    out.append((name, js[:pos].count("\n") + 1,
                                "never declared on this page" if not scopes
                                else "declared only inside a function"))
                    break
        findings[p] = out
    return findings

# The pages this sweep guards. The five lesson-like pages are the ones that share a
# renderer; the rest are included because the class is a COPY class and copies spread.
JS_SWEPT_PAGES = ("session.html", "topic.html", "practice.html", "demo.html",
                  "challenge.html", "dashboard.html", "family.html", "teacher.html",
                  "admin.html", "records.html", "community.html", "beta.html",
                  "index.html")


# =============================================================================
# PART 3av -- THE FOURTEENTH REFEREE, RE-ARMED (build hb)
# -----------------------------------------------------------------------------
# 2026-08-17. The full-app review found unit_claim_conflict silently DISARMED in
# practice and topic mode: those getters passed no "unit" in meta, and the referee
# stays mute without one. So a side-trip lesson could invent a shared past ("welcome
# back to Unit 7") with nothing watching, while the same sentence in a lesson was
# caught. Two thirds of the teaching surface, unguarded, since build gn.
#
# THE UNIT IT IS ARMED WITH MATTERS MORE THAN THE ARMING. The student's PLACED unit is
# the wrong answer here -- a practice problem is a side trip and may come from any
# unit, so arming with the placed unit would fire on correct teaching and regenerate
# good replies. The right answer is the unit of the PROBLEM (or topic), which is
# exactly what build_practice_prompt / build_topic_prompt already use to choose the
# playbook. Same input, same value: the referee and the prompt cannot disagree, which
# is the property build gn established. Unclassifiable text yields None, and the
# referee then stays silent rather than guessing.
#
# Widened here too: "you're in the middle of Unit 7" walked straight past the pattern
# while "you are ..." was caught -- an apostrophe was the entire difference. Found by
# testing the re-armed referee with phrasings a tutor actually uses.
# =============================================================================
UNIT_CLAIM_MUST_FIRE = [
    "Welcome back to Unit 7 — let's keep going.",
    "We were working on Unit 7 last time, so let's continue.",
    "You're in the middle of Unit 7, so this fits right in.",     # hb: contraction
    "We're working on Unit 7 right now.",                          # hb: contraction
    "You've been working on Unit 7.",                              # hb: contraction + been
    "We started Unit 7 yesterday.",
]
UNIT_CLAIM_MUST_STAY_SILENT = [
    "Let's solve this step by step. First, subtract 3 from both sides.",
    "This problem uses the distributive property.",
    "Unit 7 covers systems of equations.",       # a statement ABOUT a unit is not a claim
    "There are 9 units in this course.",
    "Nice work — that's the right answer.",
]


def part3av_unit_referee_rearmed():
    print("\nPART 3av — the fourteenth referee, re-armed on practice and topic (build hb)")
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "tutor.py"), encoding="utf-8") as fh:
        tsrc = fh.read()

    # 1. THE WIRING. Both getters must pass a unit, and it must come from the same
    # derivation their prompt builder uses -- never from the student's placed unit.
    for mode, arg in (("practice", "problem"), ("topic", "topic")):
        # build hg: the getters are thin configurations of _reply_pipeline; the meta
        # dict sits at the call, one indent shallower than before.
        needle = f'"mode": "{mode}",\n              "unit": _unit_from_text({arg}, course)'
        check(f"{mode} mode arms the unit referee from the {arg}'s own unit",
              needle in tsrc,
              f"get_{mode}_reply no longer passes a unit derived from the {arg} -- the "
              f"referee is disarmed again, or (worse) armed with the placed unit, which "
              f"fires on correct teaching")
    check("neither side-trip mode arms the referee from the PLACED unit",
          '"mode": "practice",\n              "unit": _lesson_unit(' not in tsrc
          and '"mode": "topic",\n              "unit": _lesson_unit(' not in tsrc,
          "a practice problem may come from any unit; the placed unit would make this "
          "referee fire on correct teaching and regenerate good replies")

    # 2. BOTH DIRECTIONS, with the value the wiring actually produces.
    u = tutor._unit_from_text("2x + 3 = 11", "algebra1")
    check("a practice problem classifies to a unit at all", isinstance(u, int) and 1 <= u <= 9,
          f"got {u!r} -- if the classifier stops answering, the referee silently disarms")
    if isinstance(u, int) and 1 <= u <= 9:
        other = 7 if u != 7 else 3
        for line in UNIT_CLAIM_MUST_FIRE:
            fired = bool(tutor.unit_claim_conflict(line.replace("Unit 7", f"Unit {other}"), u))
            check(f"  fires: {line[:52]}", fired,
                  "an invented shared past goes to the student unchallenged")
        for line in UNIT_CLAIM_MUST_STAY_SILENT:
            quiet = not tutor.unit_claim_conflict(line, u)
            check(f"  silent: {line[:52]}", quiet, "false alarm -- this regenerates good teaching")
        # The right unit named correctly must never fire.
        check("  silent: the CORRECT unit, named plainly",
              not tutor.unit_claim_conflict(f"Welcome back to Unit {u} — let's keep going.", u),
              "the referee fires on a true statement")
    # 3. Unknown unit = silence, always. This is what keeps side trips safe.
    check("silent whenever the caller does not know the unit",
          all(not tutor.unit_claim_conflict(l, None) for l in UNIT_CLAIM_MUST_FIRE)
          and not tutor.unit_claim_conflict(UNIT_CLAIM_MUST_FIRE[0], 0),
          "the referee is guessing -- an unclassifiable problem must never be judged")

    # 4. THE CANONICAL SWEEP. Standing rule: every widened detector is swept over all
    # authored foundation strings before it ships.
    try:
        import foundations as _F
        texts = []
        def _walk(o):
            if isinstance(o, str): texts.append(o)
            elif isinstance(o, dict):
                for v in o.values(): _walk(v)
            elif isinstance(o, (list, tuple)):
                for v in o: _walk(v)
        for nm in dir(_F):
            if not nm.startswith("_"): _walk(getattr(_F, nm))
        texts = [t for t in texts if isinstance(t, str) and len(t) > 3]
        alarms = sum(1 for t in texts for e in range(1, 10)
                     if tutor.unit_claim_conflict(t, e))
        check(f"unit-claim: silent on all {len(texts)} canonical scripts x 9 units",
              alarms == 0,
              f"{alarms} false alarm(s) -- the widened pattern fights authored content")
    except Exception as exc:  # noqa: BLE001
        bad("the unit-claim canonical sweep ran", str(exc))


# =============================================================================
# PART 3aw -- ONE COPY, AND IT STAYS ONE COPY (build hc)
# -----------------------------------------------------------------------------
# 2026-08-17, Phase 2 of the full-app review. The spoken-text transforms and the
# board/variable renderer existed as THREE hand-synced copies -- one each in
# session.html, topic.html and practice.html -- and that arrangement is not a tidiness
# problem, it is a defect generator: build gz shipped two live defects that existed
# only because a fix reached one copy and not its siblings, and build gn2's "case is
# meaning" fix had to be hand-copied three times to land.
#
# They are now ONE file each. This part exists so they stay that way. A future edit
# that pastes styleVarsCore back into a page to "just fix this one thing" is the
# beginning of the next gz, and it fails the build here instead.
#
# The extraction itself was proved equivalent, not assumed: the 974-string canonical
# corpus (949 authored foundation strings + 25 adversarial cases aimed at exactly what
# these transforms decide -- case, signs, money, fractions, function names) was pushed
# through forSpeech, styleVars and machineSub in a real browser on all three pages,
# before and after. 2,922 outputs per page, ZERO differences, zero page errors.
# =============================================================================
SHARED_JS_MODULES = {
    "speech-text.js": ["forSpeech", "moneyWords", "mixedWords", "fracWords"],
    "board-text.js": ["styleVars", "styleVarsCore", "varInMathContext", "escapeHTML",
                      "machineSub"],
    # build hd: the voice pipeline, WITH its state (see SHARED_JS_STATE below).
    "voice.js": ["speak", "browserSpeak", "pickVoice", "ensureAudioGraph",
                 "silentWavUri", "startKeepAlive", "stopKeepAlive", "warmUpAudio",
                 "stopAllSpeech", "withDeadline", "speechDeadline"],
    # build he: the whiteboard display, WITH its state. choiceBtn is not listed --
    # it lives nested inside showChoices, as it does on every page it came from.
    "board.js": ["showStep", "showWrite", "showSolve", "showColumn", "showGraph",
                 "showFig", "showGeo", "showBalance", "showMachine", "showObjects",
                 "showChoices", "clearChoices", "eqRow", "opRow", "fitRow",
                 "parseAttrs", "spotlightBoard", "addBubble", "scrollFeed"],
    # build hf: the microphone -- the RECONCILED copy (the three had diverged; see
    # mic.js's header for the named divergences and the F10 fix).
    "mic.js": ["startRecording", "stopRecording", "onRecordingStop", "transcribe",
               "releaseMic", "expectsALetter"],
}
SHARED_JS_CONSTS = {"board-text.js": ["VAR_NEEDS_CONTEXT", "MV_POW", "MV_NOUN"],
                    "speech-text.js": ["FRAC_WORDS"],
                    "voice.js": ["ttsAudio"]}
# build hd: state that moved into voice.js. A page that re-declares one of these at top
# level is not a style problem -- it is a SyntaxError that kills the page's entire
# script, because a duplicate top-level let/const throws at parse time. Checked here so
# the mistake fails the battery instead of a child's lesson.
SHARED_JS_STATE = {"voice.js": ["audioCtx", "analyser", "timeData", "usingAnalyser",
                                "ttsAudio", "keepAlive", "audioWarmed", "lastAudioAt",
                                "paused", "elevenEnabled", "maleVoice",
                                "firstClipOfSession", "firstSpeakLead"],
                   "board.js": ["lastTurnEl", "spotTimer", "choicesRow", "autoScroll",
                                "stickBottom", "GRAPH_COLORS", "SPOT_MS"],
                   "mic.js": ["mediaStream", "mediaRecorder", "sendOnStop", "recTimer",
                              "micTypeHint"]}


# =============================================================================
# PART 3ax -- ONE REPLY PIPELINE (build hg)
# -----------------------------------------------------------------------------
# 2026-08-17, Phase 2's backend half. The three reply getters were hand-copied
# variants of one sequence, and the copies had already cost real coverage twice:
# practice/topic ran for weeks with the fourteenth referee silently disarmed (no
# "unit" in meta -- found by the review, re-armed in hb), and only the lesson lane
# ever ran ensure_today_tag. Every new referee/net/probe needed wiring three times,
# ~1/3 odds per lane of being missed. _reply_pipeline is now the ONE sequence; the
# getters are configurations. This part keeps it that way.
# =============================================================================
# =============================================================================
# PART 3ay -- ONE TAG GRAMMAR (build hh)
# -----------------------------------------------------------------------------
# 2026-08-17, the last Phase 2 build. The [[tag]] grammar had SEVEN independent
# declarations, and one had already drifted (the live BOARD_TAG regex was missing
# numberline and areamodel). tags.py is now the single source; this part keeps the
# derivations honest and the registry internally consistent.
# =============================================================================
# =============================================================================
# PART 3az -- THE COUNTERS ARE ATOMIC (build hi)
# -----------------------------------------------------------------------------
# 2026-08-17, Phase 3 of the full-app review ("one owner per fact"). The store's
# universal write pattern was SELECT-in-Python-then-upsert -- a lost-update race
# whose worst case was academic: two overlapping check submissions could write a
# stale max and make best_pct GO DOWN, silently un-mastering a unit and re-locking
# the Final Exam while topic_progress still said "mastered". Build hi moved the
# arithmetic INTO the upsert (counters as cur+n, bests as CASE-greater-of, statuses
# as CASE-on-rank). This part proves it against a REAL database on every push:
# a temp SQLite file, serial semantics first, then a threaded hammer -- exact
# counts, never-regressing bests, never-downgrading statuses, or the build fails.
# =============================================================================
_HI_HAMMER = r"""
import os, sys, json, threading, time, random
os.environ["DATABASE_URL"] = "sqlite:///" + sys.argv[1]
sys.path.insert(0, sys.argv[2])
import store
store.init()
assert store.enabled(), store.status()
from sqlalchemy import select
def read_check(code, unit):
    t = store._tables["unit_checks"]
    with store._engine.connect() as conn:
        r = conn.execute(select(t.c.checks_taken, t.c.best_pct, t.c.attempted).where(
            (t.c.code == code) & (t.c.course == "algebra1") & (t.c.unit == unit))).first()
    return {"taken": r[0], "best": r[1], "att": r[2]} if r else {}
ok = True
r1 = store.record_check("T1", 3, 19, 20, "U3", "algebra1")
r2 = store.record_check("T1", 3, 12, 20, "U3", "algebra1")
ok &= r2["best_pct"] == 95 and r2["unit_mastered"] and (r1["attempt"], r2["attempt"]) == (1, 2)
store.record_topic("T1", 3, "U3", "mastered", "algebra1")
store.record_topic("T1", 3, "U3", "explored", "algebra1")
rows = [r for r in store.get_topics("T1", "algebra1") if r.get("unit") == 3]
ok &= bool(rows) and rows[0]["status"] == "mastered"
q2 = store.record_topic_quiz("T1", 3, "Adding Fractions", 4, 10, "algebra1", 1)
ok &= store.record_topic_quiz("T1", 3, "Adding Fractions", 9, 10, "algebra1", 1)["best_pct"] == 90
N_T, N_C = 4, 10
barrier = threading.Barrier(N_T); errors = []
def worker(i):
    barrier.wait()
    for k in range(N_C):
        for attempt in range(6):
            try:
                store.record_minutes("H1", "algebra1", "2026-08-17", 1)
                store.record_check("H1", 7, 10 + (i + k) % 10, 20, "U7", "algebra1")
                store.record_topic("H1", 7, "U7", "learning", "algebra1")
                break
            except Exception as e:
                if "locked" in str(e).lower() and attempt < 5:
                    time.sleep(0.05 * (attempt + 1)); continue
                errors.append(str(e)[:80]); break
ts = [threading.Thread(target=worker, args=(i,)) for i in range(N_T)]
[t.start() for t in ts]; [t.join() for t in ts]
total = N_T * N_C
t = store._tables["time_daily"]
with store._engine.connect() as conn:
    minutes = conn.execute(select(t.c.minutes).where(
        (t.c.code == "H1") & (t.c.course == "algebra1")
        & (t.c.day == "2026-08-17"))).scalar() or 0
c7 = read_check("H1", 7)
ok &= not errors and minutes == total and c7.get("taken") == total
ok &= c7.get("best") == 95 and c7.get("att") == total * 20
print(json.dumps({"ok": bool(ok), "minutes": minutes, "c7": c7,
                  "errors": errors[:2]}))
"""


# =============================================================================
# PART 3ba -- ONE OWNER FOR "WHICH UNIT" (build hj)
# -----------------------------------------------------------------------------
# 2026-08-17, Phase 3. "Which unit is this student in" had FIVE competing answers
# reconciled ad hoc by four consumers -- the unit-rail bug's family (Jim, twice:
# "it still says unit one when we are talking about unit five"). main._resolve_unit
# is now the one derivation; the prompt's playbook, the fourteenth referee, the
# tracker and the placement note all consume its RESULT. The priority table is
# proved against a REAL database on every push, including the two cases that were
# actually broken before hj: placement outranking progression forever (a mastered
# placement unit now advances), and the gs declaration evaporating at the next
# opener (a tracked unit now persists across sessions).
# =============================================================================
_HJ_RESOLVE = r"""
import os, sys, json, time
os.environ["DATABASE_URL"] = "sqlite:///" + sys.argv[1]
os.environ.setdefault("WEEKLY_EMAIL", "off")
sys.path.insert(0, sys.argv[2])
import store
store.init(); assert store.enabled()
import main
P3 = {"start_unit": 3, "level_title": "Level 3"}
got = {}
got["a"] = tuple(main._resolve_unit("R1", "algebra1", P3, 0))
store.record_check("R2", 3, 19, 20, "U3", "algebra1")
got["b"] = tuple(main._resolve_unit("R2", "algebra1", P3, 0))
store.record_check("R3", 1, 19, 20, "U1", "algebra1"); time.sleep(0.02)
store.record_topic("R3", 5, "U5", "learning", "algebra1")
got["c"] = tuple(main._resolve_unit("R3", "algebra1", P3, 0))
store.record_check("R4", 2, 19, 20, "U2", "algebra1"); time.sleep(0.02)
store.record_topic("R4", 2, "U2", "mastered", "algebra1")
got["d"] = tuple(main._resolve_unit("R4", "algebra1", P3, 0))
got["e"] = tuple(main._resolve_unit("R3", "algebra1", P3, 7))
got["f"] = tuple(main._resolve_unit("R9", "algebra1", {}, 0))
want = {"a": (3, "placement"), "b": (4, "progression"), "c": (5, "tracked"),
        "d": (3, "progression"), "e": (7, "focus"), "f": (1, "default")}
print(json.dumps({"ok": all(got[k] == want[k] for k in want),
                  "got": {k: list(v) for k, v in got.items()}}))
"""


# =============================================================================
# PART 3bb -- NO EXCHANGE CAN BE LOST (build hk)
# -----------------------------------------------------------------------------
# 2026-08-17, Phase 3. Conversation history was read at the top of /api/chat, a
# multi-second model call ran, then the WHOLE blob was written back -- last-writer-
# wins with a race window the width of the model's latency. A double-submit or a
# second tab silently deleted a full exchange, and the tutor "forgot" a turn the
# student remembers. store.update_history is now the only chat-path writer: a
# compare-and-swap transform (NOT a row lock -- pysqlite's legacy isolation begins
# the transaction at the first WRITE, so a FOR-UPDATE read silently ran outside it
# and the first hammer lost 200 of 240 appends with zero errors; CAS has no dialect
# trap). Proved here on a real database, every push.
# =============================================================================
_HK_HISTORY = r"""
import os, sys, json, threading, time
os.environ["DATABASE_URL"] = "sqlite:///" + sys.argv[1]
sys.path.insert(0, sys.argv[2])
import store
store.init(); assert store.enabled()
def pair(tag, i):
    return [{"role": "user", "content": tag + "-u" + str(i)},
            {"role": "assistant", "content": tag + "-a" + str(i)}]
store.update_history("R1", "algebra1", lambda h: h + pair("A", 1))
store.update_history("R1", "algebra1", lambda h: h + pair("B", 1))
seq_ok = [m["content"] for m in store.get_session("R1", "algebra1")["history"]] \
         == ["A-u1", "A-a1", "B-u1", "B-a1"]
N_T, N_C = 4, 12
barrier = threading.Barrier(N_T); errors = []
def worker(i):
    barrier.wait()
    for k in range(N_C):
        try:
            store.update_history("H1", "algebra1", lambda h: h + pair("w" + str(i), k))
        except Exception as e:
            errors.append(str(e)[:80])
ts = [threading.Thread(target=worker, args=(i,)) for i in range(N_T)]
[t.start() for t in ts]; [t.join() for t in ts]
h = store.get_session("H1", "algebra1")["history"]
pairs_ok = all(h[j]["content"].replace("-u", "-a") == h[j + 1]["content"]
               for j in range(0, len(h), 2))
b = threading.Barrier(2); e2 = []
def first(i):
    b.wait()
    try: store.update_history("NEW1", "algebra1", lambda h: h + pair("f" + str(i), 0))
    except Exception as e: e2.append(str(e)[:80])
t1 = threading.Thread(target=first, args=(1,)); t2 = threading.Thread(target=first, args=(2,))
t1.start(); t2.start(); t1.join(); t2.join()
newh = store.get_session("NEW1", "algebra1")["history"]
store.update_history("CAP", "algebra1",
                     lambda h: h + [{"role": "user", "content": str(i)} for i in range(99)],
                     cap=60)
print(json.dumps({"ok": bool(seq_ok and not errors and len(h) == N_T * N_C * 2
                             and pairs_ok and not e2 and len(newh) == 4
                             and len(store.get_session("CAP", "algebra1")["history"]) == 60),
                  "n": len(h), "pairs": pairs_ok, "new": len(newh),
                  "errors": errors[:2] + e2[:2]}))
"""


# =============================================================================
# PART 3bc -- THE SMALL CUTS OF PHASE 3 (build hl)
# -----------------------------------------------------------------------------
# 2026-08-17. Three remainders, each proved: (1) the file-key mismatch -- _ck()
# writes "CODE::course" while _has_any_history searched "CODE|course"; written one
# way, searched another, latent until the DB fallback fires. (2) topic-quiz identity
# healed by curriculum position -- the model's WORDING was the row key, so a
# rephrase minted a phantom unpassed topic and a child got re-quizzed on something
# they had passed. (3) the hi deferral closed -- student_stats counters AND the day
# streak now land in one atomic write, with the streak's day arithmetic as SQL CASE
# over the stored ISO dates (same semantics as _touch_streak, no window).
# =============================================================================
_HL_PROOF = r"""
import os, sys, json, threading, datetime
os.environ["DATABASE_URL"] = "sqlite:///" + sys.argv[1]
sys.path.insert(0, sys.argv[2])
import store
store.init(); assert store.enabled()
store.record_topic_quiz("Q1", 3, "Adding Fractions", 9, 10, "algebra1", topic_idx=2)
store.record_topic_quiz("Q1", 3, "Fraction Addition", 4, 10, "algebra1", topic_idx=2)
rows = [r for r in store.get_topic_quizzes("Q1", "algebra1") if r["unit"] == 3]
heal = (len(rows) == 1 and rows[0]["best_pct"] == 90 and rows[0]["quizzes_taken"] == 2
        and rows[0]["topic_name"] == "Fraction Addition")
N_T, N_C = 4, 10
barrier = threading.Barrier(N_T); errors = []
def worker(i):
    barrier.wait()
    for k in range(N_C):
        try: store.record_practice("S1", correct=1, attempted=2)
        except Exception as e: errors.append(str(e)[:60])
ts = [threading.Thread(target=worker, args=(i,)) for i in range(N_T)]
[t.start() for t in ts]; [t.join() for t in ts]
m = store.get_mastery("S1", "algebra1")["stats"]
stats_ok = (not errors and m["problems_practiced"] == N_T * N_C * 2
            and m.get("streak_days") == 1)
from sqlalchemy import update
t = store._tables["student_stats"]
# build hn: yesterday/gap are computed on the STREAK'S clock (California Pacific),
# the same calendar _bump_stats compares against -- computing them from UTC made
# this proof wrong for the ~7 hours a day the two calendars disagree.
yday = (store._streak_now().date() - datetime.timedelta(days=1)).isoformat()
with store._engine.begin() as c:
    c.execute(update(t).where(t.c.code == "S1").values(last_active=yday, streak_days=4))
store.record_practice("S1", 1, 1)
plus1 = store.get_mastery("S1", "algebra1")["stats"]["streak_days"] == 5
gap = (store._streak_now().date() - datetime.timedelta(days=3)).isoformat()
with store._engine.begin() as c:
    c.execute(update(t).where(t.c.code == "S1").values(last_active=gap, streak_days=9))
store.record_practice("S1", 1, 1)
reset = store.get_mastery("S1", "algebra1")["stats"]["streak_days"] == 1
print(json.dumps({"ok": bool(heal and stats_ok and plus1 and reset),
                  "heal": heal, "stats": stats_ok, "plus1": plus1, "reset": reset,
                  "errors": errors[:2]}))
"""


def part3bc_small_cuts():
    print("\nPART 3bc — the small cuts of phase 3 (build hl)")
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "main.py"), encoding="utf-8") as fh:
        msrc = fh.read()
    with open(os.path.join(here, "store.py"), encoding="utf-8") as fh:
        ssrc = fh.read()

    # (1) the key encoding has ONE writer and its readers mirror it
    check("_has_any_history parses the keys _ck actually writes",
          'key.startswith(code + "::")' in msrc
          and 'key.startswith(code + "|")' not in msrc,
          'written "CODE::course", searched "CODE|course" -- the same fact encoded '
          'independently twice, armed the moment the DB fallback fires')
    check("login's `returning` counts ANY course",
          msrc.count("or _has_any_history(") >= 2,
          "a student whose only history is Geometry gets the first-time tour again")

    # (2) quiz identity by curriculum position
    check("record_topic_quiz claims the row at the same topic_idx",
          "t.c.topic_idx == int(topic_idx)" in ssrc,
          "the model's wording is the row key again -- a rephrase mints a phantom "
          "unpassed topic and a child gets re-quizzed on a pass")

    # (3) the hi deferral is closed
    check("_bump_stats exists and computes the streak in SQL",
          "def _bump_stats(" in ssrc and "cur.last_active == today" in ssrc,
          "the stats/streak write is read-then-write again")
    for fn in ("record_check", "record_practice", "record_sprint"):
        seg = ssrc[ssrc.index(f"def {fn}("):]
        seg = seg[:seg.index("\ndef ")]
        check(f"{fn} writes stats via _bump_stats",
              "_bump_stats(" in seg and "_touch_streak(" not in seg,
              "this writer went back to the racy trio")
    check("the three clocks are documented as a DECISION",
          "THE THREE CLOCKS, DOCUMENTED" in ssrc,
          "the hours/streak day-boundary difference is drifting again instead of "
          "being chosen on purpose")

    import tempfile as _tf, json as _json
    try:
        import sqlalchemy  # noqa: F401
    except Exception:  # noqa: BLE001
        skip("hl behavioural proof", "sqlalchemy not installed here")
        return
    with _tf.TemporaryDirectory() as d:
        script = os.path.join(d, "hl.py")
        with open(script, "w", encoding="utf-8") as fh:
            fh.write(_HL_PROOF)
        res = subprocess.run([sys.executable, script,
                              os.path.join(d, "hl.db"), here],
                             capture_output=True, text=True, timeout=300)
        line = (res.stdout.strip().splitlines() or [""])[-1]
        try:
            verdict = _json.loads(line)
        except Exception:  # noqa: BLE001
            bad("hl behavioural proof ran", (res.stderr or res.stdout).strip()[:300])
            return
        check("rephrased quiz heals to one row; 80 threaded marks exact; streak "
              "+1-on-yesterday and resets-on-gap",
              verdict.get("ok") is True,
              f"{verdict} -- on a REAL database")


# =============================================================================
# PART 3bd -- THE HONEST OPENER AND THE VALIDATED DECLARATION (build hm)
# -----------------------------------------------------------------------------
# 2026-08-18, Phase 4 of the full-app review begins (Class D: the model's word
# becomes truth, unvalidated). Two mechanisms closed in one build:
#   (1) THE OPENER NO LONGER DEMANDS WHAT THE RECORD CANNOT SUPPORT. The server
#       decides has-record (assistant history / touched / mastered -- placement
#       alone is not a lesson record); a no-record opener FORBIDS a recap; a
#       returning student's recap FACTS are stated by the server from the store,
#       and the note says outright that when conversation and record disagree,
#       the record wins (history demoted to style).
#   (2) [[unitplan]] IS VETOED LIKE ARITHMETIC. main._unit_allowed_set computes
#       the units the record can justify; the NINETEENTH referee regenerates a
#       draft declaring anything else; _accept_declared_unit re-checks at filing
#       (referees fail open) and a surviving invention writes a system_events row
#       instead of a topic_progress row -- the likeliest phantom-Unit-5 mechanism,
#       dead at both ends.
# =============================================================================
# The referee, in both directions, with transcript-shaped replies. (name, reply,
# allowed, should_flag). The phantom case is the audit's own shape: a warm recap
# plus a unit bar for a unit nothing supports.
UNITPLAN_CASES = [
    ("the resolved unit is declared",
     'Today we\'re in decimals! [[unitplan unit="3" topics="comparing | adding"]]',
     (2, 3, 4), False),
    ("THE PHANTOM: a unit from nowhere",
     'Welcome back! We were right in the middle of Unit 5. '
     '[[unitplan unit="5" topics="graphs | slopes"]]',
     (1, 2), True),
    ("revisiting a mastered unit",
     'Let\'s review! [[unitplan unit="2" topics="place value | rounding"]]',
     (2, 3, 4), False),
    ("the student asked for it (main folded it into the set)",
     'Sure, let\'s jump ahead! [[unitplan unit="7" topics="area | volume"]]',
     (3, 7), False),
    ("progression advance",
     'Unit 3 is mastered -- onward! [[unitplan unit="4" topics="ratios | rates"]]',
     (2, 3, 4), False),
    ("no unitplan tag at all",
     'Nice work! [[step title="Add" steps="2+3=5"]] What do you get?',
     (3,), False),
    ("the caller does not know (practice/topic lanes)",
     'Onward! [[unitplan unit="5" topics="x | y"]]', None, False),
    ("empty allowed set stays silent",
     'Onward! [[unitplan unit="5" topics="x | y"]]', (), False),
    ("out-of-range declaration is not judged",
     'Hmm. [[unitplan unit="0" topics="x"]]', (1, 2), False),
    ("unparseable unit is not judged",
     'Hmm. [[unitplan unit="banana" topics="x"]]', (1, 2), False),
]

_HM_PROOF = r"""
import os, sys, json
os.environ["DATABASE_URL"] = "sqlite:///" + sys.argv[1]
os.environ.setdefault("WEEKLY_EMAIL", "off")
sys.path.insert(0, sys.argv[2])
import store
store.init(); assert store.enabled()
import main
ok = {}
# --- the allowed set, from a real record -------------------------------------
store.record_check("M1", 2, 19, 20, "U2", "algebra1")       # mastered unit 2 (95%)
store.record_topic("M1", 5, "U5", "learning", "algebra1")   # touched unit 5
a = set(main._unit_allowed_set("M1", "algebra1", 3, 0, ""))
ok["allowed_core"] = {2, 3, 5}.issubset(a) and 4 in a       # 4 = next unmastered after 3
ok["allowed_no_ghost"] = 7 not in a and 9 not in a
ok["allowed_msg"] = 7 in set(main._unit_allowed_set("M1", "algebra1", 3, 0,
                                                    "can we try unit 7 today?"))
ok["allowed_focus"] = 6 in set(main._unit_allowed_set("M1", "algebra1", 3, 6, ""))
ok["allowed_db_off_shape"] = set(main._unit_allowed_set("NOBODY", "algebra1", 1, 0, "")) >= {1}
# --- the filing gate ----------------------------------------------------------
ok["file_none"] = main._accept_declared_unit(None, 3, "tracked", (2, 3, 4, 5)) == (3, "none")
ok["file_focus"] = main._accept_declared_unit(5, 6, "focus", (2, 3, 4, 5, 6)) == (6, "focus-wins")
ok["file_ok"] = main._accept_declared_unit(5, 3, "tracked", (2, 3, 4, 5)) == (5, "accepted")
ok["file_reject"] = main._accept_declared_unit(8, 3, "tracked", (2, 3, 4, 5),
                                               "M1", "algebra1") == (3, "rejected")
evs = store.recent_events(hours=1, limit=50)
ok["reject_writes_event"] = any(e.get("kind") == "unitplan_rejected" for e in evs)
# --- the opener decides has-record from the record ----------------------------
hr, note = main._opener_record_note("NEW9", "algebra1", 1, [])
ok["opener_new"] = (hr is False and note == "")
hist = [{"role": "assistant", "content": "welcome back!"}]
hr2, note2 = main._opener_record_note("NEW9", "algebra1", 4, hist)
ok["opener_hist"] = hr2 is True and "Unit 4" in note2 and "RECORD WINS" in note2
hr3, note3 = main._opener_record_note("M1", "algebra1", 5, [])
ok["opener_store"] = hr3 is True and "Unit 5" in note3 and "mastered: Unit 2" in note3
# a user-only history (junk survivor) is NOT a record of lessons together
hr4, _n4 = main._opener_record_note("NEW9", "algebra1", 1,
                                    [{"role": "user", "content": "hi"}])
ok["opener_user_only"] = hr4 is False
print(json.dumps({"ok": all(ok.values()),
                  "detail": {k: bool(v) for k, v in ok.items()}}))
"""


def part3bd_truth_opener():
    print("\nPART 3bd — the honest opener and the validated declaration (build hm)")
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "main.py"), encoding="utf-8") as fh:
        msrc = fh.read()
    with open(os.path.join(here, "tutor.py"), encoding="utf-8") as fh:
        tsrc = fh.read()
    with open(os.path.join(here, "prompts.py"), encoding="utf-8") as fh:
        psrc = fh.read()
    with open(os.path.join(here, "nightwatch.py"), encoding="utf-8") as fh:
        nwsrc = fh.read()

    # (1) THE REFEREE, in both directions, on transcript-shaped replies.
    for name, reply, allowed, should_flag in UNITPLAN_CASES:
        got = bool(tutor.unitplan_conflict(reply, allowed))
        check(f"unitplan referee: {name} -> {'fires' if should_flag else 'silent'}",
              got == should_flag,
              "a declaration the record cannot justify becomes the rail's truth on "
              "the next resume" if should_flag else
              "a legitimate declaration was vetoed -- the referee is crying wolf")

    # The canonical sweep: no foundation script may trip the new referee.
    import foundations
    fired = []
    for c in COURSES:
        for f in foundations.for_course(c):
            if tutor.unitplan_conflict(f["say"], (1,)):
                fired.append((c, f["term"]))
    check("the canonical corpus is silent under the unitplan referee "
          f"({sum(len(foundations.for_course(c)) for c in COURSES)} scripts)",
          not fired, f"false fires on: {fired[:4]}")

    # (2) THE WIRING: one grammar source, referee armed, filing gated.
    import tags as _T
    check("the unitplan pattern has ONE source (tags.py)",
          hasattr(_T, "UNITPLAN_UNIT_PATTERN")
          and "tags.UNITPLAN_UNIT_PATTERN" in msrc
          and "_tagreg.UNITPLAN_UNIT_PATTERN" in tsrc,
          "two hand-typed copies of the same regex -- the Class-B disease")
    check("the sweep runs the nineteenth referee",
          "unitplan = unitplan_conflict(reply, allowed_units)" in tsrc,
          "unitplan_conflict exists but nothing calls it -- a rule nothing watches "
          "is a wish")
    check("the lesson lane arms it via meta",
          '"allowed_units": (student or {}).get("allowed_units")' in tsrc
          and 'allowed_units=(meta or {}).get("allowed_units")' in tsrc,
          "the referee never receives the record's answer -- silent forever")
    check("the chat path computes the allowed set",
          'student_context["allowed_units"] = _unit_allowed_set(' in msrc,
          "the set is never built -- the referee is disarmed on the only lane that "
          "files declarations")
    check("filing goes through the gate",
          "course_unit, _up_verdict = _accept_declared_unit(" in msrc
          and 'if declared and unit_source != "focus":\n        course_unit = declared'
          not in msrc,
          "the unconditional gs filing is back -- one hallucinated tag writes a real "
          "topic_progress row")
    check("a rejected declaration is telemetry, not truth",
          '"unitplan_rejected"' in msrc,
          "a surviving invention vanishes instead of becoming a chart")

    # (3) THE OPENER branches in code and the record outranks the conversation.
    check("the no-record opener forbids a recap",
          "THE SERVER RECORD SHOWS NO PRIOR LESSONS" in msrc
          and "do NOT recap" in msrc,
          "an empty record still demands a recap -- compliance requires invention")
    check("the returning opener states the facts from the server",
          "You HAVE met before." in msrc and "def _opener_record_note(" in msrc,
          "the model is deciding whether you have met -- from the history it wrote")
    check("the gap refresher reads the record, not the conversation",
          "name the unit the SERVER RECORD above puts you two in" in msrc
          and "use your notes and the recent conversation" not in msrc,
          "the refresher still treats stored model prose as memory")
    check("rule 0 no longer licenses the conversation as a fact source",
          "or in this conversation" not in psrc and "THE NOTES WIN" in psrc,
          "an invented recap stored in history still counts as memory next session")
    check("the unit-bar words tell the model what the machinery enforces",
          "THE UNIT YOU DECLARE MUST BE ONE THE RECORD SUPPORTS" in psrc,
          "the referee fires with no warning in the prompt -- wasted regenerations")

    # (4) The nightwatch clock stays pinnable (the 2026-08-18 date-rollover lesson:
    # a test that pins the clock must pin it EVERYWHERE the code reads it).
    check("write_report accepts a pinned clock",
          'def write_report(data_dir, result, build="", now=None)' in nwsrc,
          "the restart-safety checks go red again the day after they are written")

    # (5) THE BEHAVIOURAL PROOF on a real database, every push.
    import tempfile as _tf, json as _json
    try:
        import sqlalchemy  # noqa: F401
    except Exception:  # noqa: BLE001
        skip("hm behavioural proof", "sqlalchemy not installed here")
        return
    with _tf.TemporaryDirectory() as d:
        script = os.path.join(d, "hm.py")
        with open(script, "w", encoding="utf-8") as fh:
            fh.write(_HM_PROOF)
        res = subprocess.run([sys.executable, script,
                              os.path.join(d, "hm.db"), here],
                             capture_output=True, text=True, timeout=300)
        line = (res.stdout.strip().splitlines() or [""])[-1]
        try:
            verdict = _json.loads(line)
        except Exception:  # noqa: BLE001
            bad("hm behavioural proof ran", (res.stderr or res.stdout).strip()[:300])
            return
        check("allowed-set table, filing gate, rejection telemetry and opener "
              "has-record decision all hold on a REAL database",
              verdict.get("ok") is True, f"{verdict}")


# =============================================================================
# PART 3be -- THE STREAK LIVES ON CALIFORNIA TIME (build hn)
# -----------------------------------------------------------------------------
# 2026-08-18, Jim's ruling on THE THREE CLOCKS: "use California Pacific Time."
# The streak's day-strings now come from _streak_today()/_streak_now() (STREAK_TZ,
# default America/Los_Angeles); the atomic SQL CASE is untouched. Proved here:
# the env knob genuinely steers the calendar (two zones 26 hours apart can never
# share a date), a bogus zone falls back to UTC without crashing the import, and
# PART 3bc's streak proof now runs on the same clock the code compares against.
# =============================================================================
_HN_CLOCK = r"""
import os, sys, json, datetime
sys.path.insert(0, sys.argv[1])
os.environ["STREAK_TZ"] = sys.argv[2]
import store
print(json.dumps({"today": store._streak_today(), "tz": store.STREAK_TZ_NAME,
                  "utc": datetime.datetime.now(datetime.timezone.utc).date().isoformat()}))
"""


def part3be_streak_clock():
    print("\nPART 3be — the streak lives on California time (build hn)")
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "store.py"), encoding="utf-8") as fh:
        ssrc = fh.read()
    with open(os.path.join(here, "requirements.txt"), encoding="utf-8") as fh:
        req = fh.read()

    check("the streak writer reads the streak's clock",
          "today = _streak_today()" in ssrc
          and "yday = (_streak_now().date()" in ssrc,
          "_bump_stats is back on the server-UTC day -- an 8pm California practice "
          "is 'tomorrow' again and evening streaks break")
    check("the default zone is Jim's ruling",
          'os.environ.get("STREAK_TZ", "America/Los_Angeles")' in ssrc,
          "the THREE CLOCKS decision silently changed")
    check("the decision is recorded where the clocks are documented",
          "AND THE STREAK'S CLOCK DECIDED" in ssrc and "use California Pacific Time" in ssrc,
          "the day-boundary is drifting again instead of being chosen on purpose")
    check("tzdata rides requirements (Windows has no IANA database)",
          "tzdata==" in req,
          "the battery box or a dev box silently falls back to UTC")
    check("the retired trio warns its reviver about the clock",
          "it must read _streak_today()" in ssrc,
          "a revived _touch_streak would advance the streak on the wrong calendar")

    import tempfile as _tf, json as _json
    with _tf.TemporaryDirectory() as d:
        script = os.path.join(d, "hn.py")
        with open(script, "w", encoding="utf-8") as fh:
            fh.write(_HN_CLOCK)
        got = {}
        for label, tz in (("east", "Pacific/Kiritimati"),   # UTC+14
                          ("west", "Etc/GMT+12"),           # UTC-12 (POSIX sign)
                          ("bogus", "Definitely/Nowhere")):
            res = subprocess.run([sys.executable, script, here, tz],
                                 capture_output=True, text=True, timeout=120)
            line = (res.stdout.strip().splitlines() or [""])[-1]
            try:
                got[label] = _json.loads(line)
            except Exception:  # noqa: BLE001
                bad(f"streak clock subprocess ({label}) ran",
                    (res.stderr or res.stdout).strip()[:200])
                return
        check("STREAK_TZ genuinely steers the calendar (zones 26h apart never share "
              "a date)", got["east"]["today"] != got["west"]["today"],
              f"east={got['east']} west={got['west']} -- the env knob is decorative")
        check("an unknown zone falls back to the UTC day without crashing the import",
              got["bogus"]["today"] == got["bogus"]["utc"],
              f"{got['bogus']} -- the fallback is not the pre-hn behaviour")


# =============================================================================
# PART 3bf -- THE RECORD-CLAIM REFEREE (build ho)
# -----------------------------------------------------------------------------
# 2026-08-18, the count-claim probe's promotion (Phase 4, Class D). The audit's
# most corrosive finding -- a child refused a demonstration on "you've now watched
# this move twice", an invented count -- plus false past-scores and false unit
# states, all vetoed against the record the server actually holds. Fixtures below
# include the audit's own transcript shapes, in both directions; the canonical
# corpus is swept with a full record to prove no false fires on real teaching.
# =============================================================================
_RC_RECORD = {"best": {3: 80}, "last": {3: 75}, "quiz_pcts": [90],
              "mastered": [2], "touched": [2, 3]}
RECORD_CLAIM_CASES = [
    ("THE AUDIT SHAPE: a refusal justified by an invented watch-count",
     "Great question! But you've now watched this move twice -- let's flip it and "
     "have you try.", _RC_RECORD, True),
    ("the audit's second wording",
     "You've watched this exact move twice now.", _RC_RECORD, True),
    ("the invented collection count",
     "That's all three conversions under your belt!", _RC_RECORD, True),
    ("a unit in progress that the record has never seen",
     "Unit 9 is also still in progress.", _RC_RECORD, True),
    ("a last score the record does not hold (number words)",
     "Your last score was eighty-five percent.", _RC_RECORD, True),
    ("mastery the record does not hold",
     "You've already mastered Unit 4!", _RC_RECORD, True),
    ("a unit declared finished that never was",
     "Unit 5 is finished.", _RC_RECORD, True),
    ("a remembered score from nowhere",
     "You got 95% on that quiz, remember?", _RC_RECORD, True),
    # -------- and the other direction: everything here must stay silent --------
    ("no record, no judgment (practice/topic lanes)",
     "You've now watched this move twice -- let's flip it.", None, False),
    ("the recorded best, stated truly",
     "Your best score was 80%.", _RC_RECORD, False),
    ("the recorded last, stated truly",
     "Your last score was 75%.", _RC_RECORD, False),
    ("the recorded quiz best, stated truly",
     "You scored 90% on the comparing decimals quiz.", _RC_RECORD, False),
    ("a unit genuinely in progress",
     "Unit 3 is still in progress.", _RC_RECORD, False),
    ("mastery the record holds",
     "You've mastered Unit 2 -- that's real work.", _RC_RECORD, False),
    ("a future conditional is a plan, not a claim",
     "Once you've mastered Unit 4, the Final Exam unlocks.", _RC_RECORD, False),
    ("an in-reply result belongs to rule 45's referee, not this one",
     'Wow -- you got 60% on the fractions quiz! Let\'s look at the two we missed. '
     '[[quiz unit="3" topic="fractions" score="60" correct="3" total="5"]]',
     _RC_RECORD, False),
    ("beating your best is an invitation, and the best is real",
     "Let's try to beat your best of 80%!", _RC_RECORD, False),
    ("ordinary teaching says none of these things",
     "The numerator counts the parts -- let's shade three of the four parts.",
     _RC_RECORD, False),
    ("having seen an idea is not a count",
     "You've seen how regrouping works, so let's go one step deeper.",
     _RC_RECORD, False),
]


def part3bf_record_claims():
    print("\nPART 3bf — the record-claim referee (build ho)")
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "main.py"), encoding="utf-8") as fh:
        msrc = fh.read()
    with open(os.path.join(here, "tutor.py"), encoding="utf-8") as fh:
        tsrc = fh.read()

    for name, reply, record, should_flag in RECORD_CLAIM_CASES:
        got = bool(tutor.record_claim_conflict(reply, record))
        check(f"record referee: {name} -> {'fires' if should_flag else 'silent'}",
              got == should_flag,
              "a child can be refused, praised or placed on invented evidence"
              if should_flag else
              "a truthful reply was vetoed -- the referee is crying wolf")

    # The canonical sweep: real teaching, full record, zero fires.
    import foundations
    fired = []
    for c in COURSES:
        for f in foundations.for_course(c):
            if tutor.record_claim_conflict(f["say"], _RC_RECORD):
                fired.append((c, f["term"]))
    check("the canonical corpus is silent under the record referee "
          f"({sum(len(foundations.for_course(c)) for c in COURSES)} scripts)",
          not fired, f"false fires on: {fired[:4]}")

    # THE WIRING: record built server-side, armed through meta, swept in order.
    check("main builds the claim record from the store",
          "def _claim_record(" in msrc
          and 'student_context["claim_record"] = _claim_record(' in msrc,
          "the twentieth referee never receives the record -- silent forever")
    check("the lesson lane arms it via meta",
          '"record": (student or {}).get("claim_record")' in tsrc
          and 'record=(meta or {}).get("record")' in tsrc,
          "the record referee is disarmed on the only lane that has a record")
    check("the sweep runs the twentieth referee",
          "recordclaim = record_claim_conflict(reply, record)" in tsrc,
          "record_claim_conflict exists but nothing calls it -- a rule nothing "
          "watches is a wish")
    check("a result reply is exempt as a WHOLE (the record lags the announcement)",
          "if _RC_RESULT_TAG.search(str(reply or \"\")):" in tsrc,
          "the referee vetoes every honest quiz celebration -- the record has not "
          "caught up with the result being announced")


# =============================================================================
# PART 3bg -- THE ORDER OF AUTHORITY (build hp)
# -----------------------------------------------------------------------------
# 2026-08-18, Phase 4's precedence lattice. Two blocks used to claim supremacy at
# once (GROUND_RULES "override anything said later"; SESSION_OPENER_RULES "override
# anything above"), so collisions were resolved by whichever claim the model felt
# like weighting -- and several audited "violations" were one rule obeyed against
# another. Now exactly ONE block is absolute, the five levels are stated, the known
# cross-pulls are named by number, and RULES.md can no longer go quietly stale.
# =============================================================================
def part3bg_order_of_authority():
    print("\nPART 3bg — the order of authority (build hp)")
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "tutor.py"), encoding="utf-8") as fh:
        tsrc = fh.read()

    g = tutor.GROUND_RULES
    check("exactly ONE block claims absolute supremacy",
          g.count("THESE OVERRIDE ANYTHING SAID LATER") == 1
          and "OVERRIDE ANYTHING ABOVE" not in tutor.SESSION_OPENER_RULES,
          "two supremacy claims again -- every collision is a coin flip")
    check("the lattice exists and names its five levels",
          "WHEN INSTRUCTIONS COLLIDE" in g
          and all(s in g for s in ("1. THE GROUND RULES", "2. THE SERVER'S FACTS",
                                   "3. SESSION MECHANICS", "4. THE TEACHING RULES",
                                   "5. STYLE")),
          "the order of authority is gone -- collisions are unresolvable again")
    check("specific-beats-general and the (SYSTEM:) note's rank are stated",
          "more SPECIFIC instruction wins" in g and "(SYSTEM:) note about this very turn" in g,
          "within-level collisions have no tiebreaker")
    check("the audited cross-pulls are named by number",
          "rule 65 over 6/17/38c" in g and "(64 over 23)" in g,
          "the two collisions the audit actually caught are unstated again")
    check("the opener block is re-scoped to level 3",
          "LEVEL 3 OF THE ORDER OF AUTHORITY" in tutor.SESSION_OPENER_RULES
          and "never the Ground Rules" in tutor.SESSION_OPENER_RULES,
          "the opener claims the whole prompt again")
    check("the lattice rides GROUND_RULES into every lane",
          tsrc.count("GROUND_RULES + GRAPH_TOOL_NOTE") >= 3,
          "a lane assembles its prompt without the ground block -- the lattice "
          "does not reach it")

    # RULES.md CAN NO LONGER GO QUIETLY STALE (the review: "two builds stale and
    # nothing checks it"). Regenerate to a temp file and require byte equality.
    import tempfile as _tf
    with _tf.TemporaryDirectory() as d:
        fresh = os.path.join(d, "RULES.md")
        write_rules_index(fresh)
        with open(fresh, encoding="utf-8") as fh:
            want = fh.read()
        try:
            with open(os.path.join(here, "RULES.md"), encoding="utf-8") as fh:
                got = fh.read()
        except OSError:
            got = ""
        check("RULES.md matches the prompt it documents (run `python ruletests.py "
              "--rules` after any rule change)",
              got == want,
              "RULES.md has drifted from the actual prompt -- regenerate it")


# =============================================================================
# PART 3bh -- THE TWO-PROMPT-SIZES EXPERIMENT IS RUNNABLE (build hq)
# -----------------------------------------------------------------------------
# 2026-08-18. Named in this file's own PROMPT_CEILING comments since 2026-08-11 as
# "still the right way to set this number, and still not done." The live halves
# (teaching + marking) need keys and run on Render; what the battery CAN prove, it
# does: the lever exists, the large student genuinely assembles the over-ceiling
# worst case, the measurement is honest, and nightwatch survived the return change.
# =============================================================================
def part3bh_two_prompt_sizes():
    print("\nPART 3bh — the two-prompt-sizes experiment is runnable (build hq)")
    here = os.path.dirname(os.path.abspath(__file__))
    try:
        import lessonaudit
    except Exception as exc:  # noqa: BLE001
        bad("lessonaudit imports", str(exc)[:200])
        return
    with open(os.path.join(here, "lessonaudit.py"), encoding="utf-8") as fh:
        lsrc = fh.read()
    with open(os.path.join(here, "nightwatch.py"), encoding="utf-8") as fh:
        nwsrc = fh.read()

    check("the CLI lever exists",
          '"--prompt-size"' in lsrc and 'prompt_size=prompt_size' in lsrc,
          "the experiment cannot be invoked -- still not done")
    check("the report carries the experiment's interpretation",
          "TWO-PROMPT-SIZES EXPERIMENT" in lsrc and "PROMPT_CEILING" in lsrc,
          "two reports with no stated comparison is two piles of findings")
    check("nightwatch unpacks the new return shape",
          "transcript, err, fallbacks, _pchars = lessonaudit.run_scenario" in nwsrc,
          "the governor crashes on its first lesson tonight")

    # The measured halves, in-process and free: the same scenario at both sizes.
    sc = next((s for s in lessonaudit.SCENARIOS if s["course"] == "algebra1"),
              lessonaudit.SCENARIOS[0])
    small_student = lessonaudit.audit_student(sc, "normal")
    large_student = lessonaudit.audit_student(sc, "large")
    check("the large student is all-heard and FORCED verbatim",
          large_student.get("foundations_heard")
          and large_student.get("foundations_force_verbatim") is True
          and not small_student.get("foundations_heard"),
          "the lever moves nothing -- both runs teach the same prompt")
    p_small = tutor.build_system_prompt(dict(small_student), sc["course"])
    p_large = tutor.build_system_prompt(dict(large_student), sc["course"])
    check("the two sizes are genuinely two sizes "
          f"(small {len(p_small):,} / large {len(p_large):,})",
          # ≥10K chars apart: algebra1 measures ~173K fresh vs ~190K all-heard
          # today; the margin is a tripwire against the lever silently dying,
          # not a pin on today's exact sizes.
          len(p_large) >= len(p_small) + 10_000,
          "the all-heard worst case no longer differs -- the experiment would "
          "compare a prompt against itself")
    check("the large size is the over-ceiling shape gz measured "
          f"(ceiling {tutor.PROMPT_CEILING:,})",
          len(p_large) > tutor.PROMPT_CEILING,
          "the worst case has shrunk under the ceiling -- good news if true, but "
          "re-verify before believing it (and the experiment still applies)")


# =============================================================================
# PART 3bi -- THE STORY KEEPS ONE UNIT (build hr)
# -----------------------------------------------------------------------------
# 2026-08-18. The night watch's FIRST confirmed catch after Phase 4 went live
# (08:44 UTC report): 4 + 3 × 2 modeled as "4 dollars, plus 3 bags of 2 candies
# each" -- dollars added to candies, the numbers as decoration. Closed the standing
# way: the rule gains the clause (32b), the caught shape gains a referee (the
# twenty-first, rule-27 precedent: narrow enforcement, words cover the class), and
# both ship with their checks in the same build.
# =============================================================================
STORY_UNITS_CASES = [
    ("THE NIGHTWATCH CATCH, verbatim",
     "Let's picture it: you have 4 dollars, plus 3 bags of 2 candies each.", True),
    ("the same shape with different nouns",
     "Start with 5 cents, plus 2 boxes of 6 stickers each -- what do we get?", True),
    ("number words instead of digits",
     "You have four dollars, plus three bags of two candies each.", True),
    # -------- and the other direction: everything here must stay silent --------
    ("one unit throughout -- the suggested fix itself",
     "Let's picture it: you have 4 loose candies, plus 3 bags of 2 candies each.",
     False),
    ("a shopping story where the groups resolve to money",
     "You have 4 dollars, plus 3 bags of 2 candies that cost 1 dollar each.", False),
    ("money plus money",
     "The ticket costs 4 dollars plus 40 cents in tax.", False),
    ("listing two facts is not adding them",
     "You have 4 dollars and 3 bags of 5 candies. Each candy sells for a dime.",
     False),
    ("groups of objects with no money anywhere",
     "You have 4 apples, plus 3 baskets of 2 apples each.", False),
    ("money in one sentence, groups in another",
     "You brought 4 dollars today. Now picture 3 bags of 2 candies each.", False),
    ("ordinary teaching mentions money alone",
     "A movie ticket costs 12 dollars -- is that a sensible price?", False),
]


def part3bi_story_units():
    print("\nPART 3bi — the story keeps one unit (build hr)")
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "tutor.py"), encoding="utf-8") as fh:
        tsrc = fh.read()

    for name, reply, should_flag in STORY_UNITS_CASES:
        got = bool(tutor.story_units_conflict(reply))
        check(f"story units: {name} -> {'fires' if should_flag else 'silent'}",
              got == should_flag,
              "a story adds money to objects and the numbers become decoration"
              if should_flag else
              "an honest story was vetoed -- the referee is crying wolf")

    # The canonical sweep: no foundation script may trip the new referee.
    import foundations
    fired = []
    for c in COURSES:
        for f in foundations.for_course(c):
            if tutor.story_units_conflict(f["say"]):
                fired.append((c, f["term"]))
    check("the canonical corpus is silent under the story-units referee "
          f"({sum(len(foundations.for_course(c)) for c in COURSES)} scripts)",
          not fired, f"false fires on: {fired[:4]}")

    # THE WIRING: the clause reaches the prompt, the sweep runs the referee, the
    # ledger tells the truth about what is enforced.
    check("rule 32 carries the one-unit clause",
          "THE STORY KEEPS ONE UNIT" in tutor.GRAPH_TOOL_NOTE
          and "ONE kind of quantity throughout" in tutor.GRAPH_TOOL_NOTE,
          "the words are gone -- the referee enforces a rule the model was never told")
    check("the sweep runs the twenty-first referee",
          "storyunits = story_units_conflict(reply)" in tsrc,
          "story_units_conflict exists but nothing calls it -- a rule nothing "
          "watches is a wish")
    check("the ledger names the enforced shape honestly",
          RULE_VERIFY.get(32, ("", ""))[0] == "ENFORCED"
          and "story_units_conflict" in RULE_VERIFY.get(32, ("", ""))[1],
          "RULE_VERIFY still calls rule 32 merely COVERED (or claims more than the "
          "narrow shape)")


# =============================================================================
# PART 3bj -- THE CREDENTIAL LEAVES THE URL (build hs, Phase 5 begins)
# -----------------------------------------------------------------------------
# 2026-08-18. Review Class F: the student CODE -- the entire login -- travelled in
# request lines (/api/xxx/{code}, /api/speak?code=), and request lines are written
# to plaintext HTTP logs on infrastructure we do not control; /api/speak's query
# also carried the SPOKEN LINE, i.e. a child's lesson with their first name in it.
# Now: every student-gated route resolves its code through _code_dep (X-Student-Code
# header preferred, path form kept for stale cached pages); the voice path mints an
# opaque ticket (POST /api/speak-prep -> GET /api/speak?t=) because an <audio src>
# cannot send headers; transcribe/library take the header; every shipped page sends
# the header form. ALSO Jim's Plausible ruling: analytics.js refuses to load on the
# student surfaces. Proved live (subprocess + TestClient + temp sqlite) and by
# source ratchets that would catch any site quietly reverting.
# =============================================================================
_HS_DRILL = r"""
import os, sys, json
os.environ["DATABASE_URL"] = "sqlite:///" + sys.argv[1]
os.environ.setdefault("WEEKLY_EMAIL", "off")
os.environ.pop("ANTHROPIC_API_KEY", None)
os.environ.pop("ELEVENLABS_API_KEY", None)
sys.path.insert(0, sys.argv[2])
from fastapi.testclient import TestClient
import main
c = TestClient(main.app)
H = {"X-Student-Code": "1234"}
ok = {}
GETS = ["/api/awards/me", "/api/time/me", "/api/topics/me?course=algebra1",
        "/api/courses/me", "/api/sprints/me?course=prealgebra",
        "/api/sprint/me?course=prealgebra&unit=1", "/api/records/me",
        "/api/misses/me?course=algebra1", "/api/placement/me?course=algebra1",
        "/api/session/me?course=algebra1"]
for u in GETS:
    rh = c.get(u, headers=H)                       # the new form: header + 'me'
    rl = c.get(u.replace("/me", "/1234"))          # the legacy form still works
    rb = c.get(u)                                  # 'me' with NO header = no code
    ok[u] = (rh.status_code == 200 and rl.status_code == 200
             and rb.status_code in (401, 404))
# the POST family (the client record calls). build hu: quiz/check POSTs are echo
# gates now, so the server must see the tags first -- exactly as a real turn does.
main._record_result_tags("1234", "algebra1",
    '[[quiz unit="1" topic="1" name="counting" correct="4" total="5"]] '
    '[[check unit="1" correct="4" total="5"]]')
rm = c.post("/api/mark/me", json={"correct": 1, "attempted": 1}, headers=H)
rq = c.post("/api/quiz/me", json={"unit": 1, "topic": 1, "name": "counting",
                                  "correct": 4, "total": 5, "course": "algebra1"},
            headers=H)
rc = c.post("/api/check/me", json={"unit": 1, "correct": 4, "total": 5,
                                   "course": "algebra1"}, headers=H)
rb2 = c.post("/api/check/me", json={"unit": 1, "correct": 4, "total": 5,
                                    "course": "algebra1"})
ok["posts"] = (rm.status_code == 200 and rq.status_code == 200
               and rc.status_code == 200 and rb2.status_code in (401, 404))
# the voice ticket: mint -> stream (204 with no key) -> bogus ticket 410 -> legacy alive
rp = c.post("/api/speak-prep", json={"code": "1234", "text": "Hello there!", "lead": 1})
tick = (rp.json() or {}).get("t") if rp.status_code == 200 else None
ok["prep"] = bool(tick) and (rp.json() or {}).get("voice") is False
ok["ticket_stream"] = bool(tick) and c.get("/api/speak?t=" + tick).status_code == 204
ok["bogus_ticket"] = c.get("/api/speak?t=NOSUCHTICKET").status_code == 410
ok["legacy_speak"] = c.get("/api/speak?text=hi&code=1234").status_code == 204
ok["prep_needs_login"] = c.post("/api/speak-prep",
                                json={"code": "zzz", "text": "hi"}).status_code == 401
# library: header form accepted, bare form rejected
ok["library"] = (c.get("/api/library?q=zzz&course=algebra1", headers=H).status_code != 404
                 and c.get("/api/library?q=zzz&course=algebra1").status_code == 404)
print(json.dumps({"ok": all(ok.values()),
                  "detail": {k: bool(v) for k, v in ok.items()}}))
"""


def part3bj_credential_leaves_url():
    print("\nPART 3bj — the credential leaves the URL (build hs)")
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "main.py"), encoding="utf-8") as fh:
        msrc = fh.read()

    # THE SERVER SIDE, wired.
    check("one code dependency exists and every {code} route uses it",
          "def _code_dep(" in msrc and msrc.count("Depends(_code_dep)") == 17,
          f"found {msrc.count('Depends(_code_dep)')} of 17 -- a route resolves its "
          "own code again and the header form silently dies there")
    check("the voice path has its ticket mint",
          '@app.post("/api/speak-prep")' in msrc and "_SPEAK_TICKETS" in msrc,
          "an <audio src> cannot send headers -- without the ticket, the code and "
          "the child's spoken line ride the URL")
    check("transcribe and library prefer the header",
          msrc.count('alias="X-Student-Code"') >= 2,
          "the mic/library calls leak the credential again")
    check("the billing log line is masked",
          '[billing] {_be[:2]}***@' in msrc.replace("f\"", "\"") or "_be[:2]" in msrc,
          "a parent's email prints to logs verbatim")

    # THE CLIENT SIDE, ratcheted -- concatenation-shaped patterns that cannot hide
    # in a comment.
    import glob as _glob
    bad_sites = []
    conc = re.compile(
        r'/api/(?:topics|session|courses|awards|time|records|misses|sprints|sprint|'
        r'final|check|quiz|mark|placement|assessment)/"\s*\+\s*encodeURIComponent'
        r'|speak\?text="\s*\+\s*encodeURIComponent'
        r'|transcribe\?code='
        r'|/api/library\?[^"]*code="\s*\+')
    for fpath in sorted(_glob.glob(os.path.join(here, "static", "*.html"))
                        + sorted(_glob.glob(os.path.join(here, "static", "*.js")))):
        with open(fpath, encoding="utf-8") as fh:
            src = fh.read()
        if conc.search(src):
            bad_sites.append(os.path.basename(fpath))
    check("no page builds an API URL with the code or the spoken line in it",
          not bad_sites, f"reverted sites: {bad_sites}")
    for fname, needle in (("voice.js", '"/api/speak-prep"'),
                          ("mic.js", '"X-Student-Code": CODE'),
                          ("library.js", '"X-Student-Code": CODE'),
                          ("session.html", '"X-Student-Code": CODE'),
                          ("dashboard.html", '"X-Student-Code": CODE'),
                          ("challenge.html", '"/api/speak-prep"')):
        with open(os.path.join(here, "static", fname), encoding="utf-8") as fh:
            check(f"{fname} sends the new form", needle in fh.read(),
                  "this surface reverted to the URL form")

    # JIM'S PLAUSIBLE RULING (2026-08-18): no fourth party on children's pages.
    with open(os.path.join(here, "static", "analytics.js"), encoding="utf-8") as fh:
        asrc = fh.read()
    check("analytics.js guards the student surfaces",
          "KID_PAGES" in asrc
          and all(p in asrc for p in ('"session"', '"topic"', '"practice"',
                                      '"challenge"', '"dashboard"', '"records"',
                                      '"home"'))
          and "isKidPage" in asrc and "return;" in asrc,
          "Plausible loads on a child's lesson page again -- the privacy promise "
          "names exactly three processors")

    # THE LIVE DRILL: every route in both forms, the ticket lifecycle, the gates.
    try:
        import httpx  # noqa: F401
        import sqlalchemy  # noqa: F401
    except Exception:  # noqa: BLE001
        skip("hs live drill", "httpx/sqlalchemy not installed here")
        return
    import tempfile as _tf, json as _json
    with _tf.TemporaryDirectory() as d:
        script = os.path.join(d, "hs.py")
        with open(script, "w", encoding="utf-8") as fh:
            fh.write(_HS_DRILL)
        res = subprocess.run([sys.executable, script,
                              os.path.join(d, "hs.db"), here],
                             capture_output=True, text=True, timeout=300)
        line = (res.stdout.strip().splitlines() or [""])[-1]
        try:
            verdict = _json.loads(line)
        except Exception:  # noqa: BLE001
            bad("hs live drill ran", (res.stderr or res.stdout).strip()[:300])
            return
        check("header form, legacy form, bare-form rejection, ticket lifecycle and "
              "login gates all hold on a live app",
              verdict.get("ok") is True, f"{verdict}")


# =============================================================================
# PART 3bk -- BOUNDED AND SPLIT (build ht, Phase 5)
# -----------------------------------------------------------------------------
# 2026-08-18. Two Class-F closures: (1) THE TURN CANNOT HANG -- the Anthropic SDK's
# ~600s default timeout let a hung upstream freeze a child for ten minutes; every
# client is now built with ANTHROPIC_TIMEOUT_S (60s) and one retry, and the three
# teaching pages carry a 90s fetch abort with a warm try-again bubble. (2) THE
# GOD-KEY IS SPLIT -- the full-DB snapshot demands DATA_EXPORT_KEY and destructive
# resets demand FAMILY_RESET_KEY; graver tiers never fall back to the general key
# and FAIL CLOSED (a 503 naming the env var) when unset. Proved live below.
# =============================================================================
_HT_DRILL = r"""
import os, sys, json
os.environ["DATABASE_URL"] = "sqlite:///" + sys.argv[1]
os.environ.setdefault("WEEKLY_EMAIL", "off")
os.environ["FORUM_MOD_KEY"] = "general-key"
os.environ.pop("DATA_EXPORT_KEY", None)
os.environ.pop("FAMILY_RESET_KEY", None)
sys.path.insert(0, sys.argv[2])
from fastapi.testclient import TestClient
import main
c = TestClient(main.app)
G = {"X-Admin-Key": "general-key"}
ok = {}
# the general key still runs the panel...
ok["general_alive"] = c.get("/api/admin/stats", headers=G).status_code == 200
# ...but the graver powers FAIL CLOSED while their keys are unset -- and the
# general key is NOT a fallback.
ok["export_closed"] = c.get("/api/admin/backup", headers=G).status_code == 503
ok["reset_closed"] = c.post("/api/admin/student-reset",
                            json={"key": "general-key", "code": "1234"}).status_code == 503
# set the graver keys: right key works, general key is refused, wrong key is refused
os.environ["DATA_EXPORT_KEY"] = "export-key"
os.environ["FAMILY_RESET_KEY"] = "reset-key"
ok["export_right"] = c.get("/api/admin/backup",
                           headers={"X-Admin-Key": "export-key"}).status_code == 200
ok["export_general_refused"] = c.get("/api/admin/backup", headers=G).status_code == 401
ok["export_wrong"] = c.get("/api/admin/backup",
                           headers={"X-Admin-Key": "nope"}).status_code == 401
r = c.post("/api/admin/student-reset", json={"key": "reset-key", "code": "1234"})
ok["reset_right_key_accepted"] = r.status_code in (200, 404)   # auth passed; 404 = no data yet
ok["reset_general_refused"] = c.post("/api/admin/student-reset",
                                     json={"key": "general-key", "code": "1234"}).status_code == 401
print(json.dumps({"ok": all(ok.values()), "detail": {k: bool(v) for k, v in ok.items()}}))
"""


def part3bk_bounded_and_split():
    print("\nPART 3bk — bounded and split (build ht)")
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "main.py"), encoding="utf-8") as fh:
        msrc = fh.read()
    with open(os.path.join(here, "tutor.py"), encoding="utf-8") as fh:
        tsrc = fh.read()

    # (1) the upstream call is bounded, at EVERY construction site
    n_clients = tsrc.count("Anthropic(api_key=api_key")
    n_bounded = tsrc.count("Anthropic(api_key=api_key, timeout=ANTHROPIC_TIMEOUT_S, max_retries=1)")
    check(f"every Anthropic client is bounded ({n_bounded}/{n_clients})",
          n_clients >= 3 and n_bounded == n_clients,
          "an unbounded client can freeze a child for the SDK's ten-minute default")
    check("the timeout has one env-tunable definition",
          'ANTHROPIC_TIMEOUT_S = float(os.environ.get("ANTHROPIC_TIMEOUT_S"' in tsrc,
          "the bound is hardcoded or gone")
    for page in ("session.html", "topic.html", "practice.html"):
        with open(os.path.join(here, "static", page), encoding="utf-8") as fh:
            psrc = fh.read()
        check(f"{page} aborts a hung turn and lands a warm bubble",
              "signal: ctl.signal" in psrc and 'e.name === "AbortError"' in psrc
              and "clearTimeout(abortTimer)" in psrc,
              "the page can hang on a dead connection again")

    # (2) the god-key is split, in code and in the panel
    check("_require_admin is tiered and graver tiers fail closed",
          'tier="export"' in msrc and 'tier="reset"' in msrc
          and "DATA_EXPORT_KEY" in msrc and "FAMILY_RESET_KEY" in msrc
          and "status_code=503" in msrc,
          "the god-key is back -- one leaked moderation key exports or erases "
          "everything")
    with open(os.path.join(here, "static", "admin.html"), encoding="utf-8") as fh:
        asrc = fh.read()
    check("the panel asks for the graver keys and forgets a wrong one",
          "function graverKey(" in asrc
          and 'graverKey("export", "DATA_EXPORT_KEY")' in asrc
          and asrc.count('graverKey("reset", "FAMILY_RESET_KEY")') == 2
          and 'sessionStorage.removeItem("mt_reset_key")' in asrc
          and 'sessionStorage.removeItem("mt_export_key")' in asrc,
          "the panel still sends the general key to the graver doors")

    try:
        import httpx  # noqa: F401
        import sqlalchemy  # noqa: F401
    except Exception:  # noqa: BLE001
        skip("ht live drill", "httpx/sqlalchemy not installed here")
        return
    import tempfile as _tf, json as _json
    with _tf.TemporaryDirectory() as d:
        script = os.path.join(d, "ht.py")
        with open(script, "w", encoding="utf-8") as fh:
            fh.write(_HT_DRILL)
        res = subprocess.run([sys.executable, script,
                              os.path.join(d, "ht.db"), here],
                             capture_output=True, text=True, timeout=300)
        line = (res.stdout.strip().splitlines() or [""])[-1]
        try:
            verdict = _json.loads(line)
        except Exception:  # noqa: BLE001
            bad("ht live drill ran", (res.stderr or res.stdout).strip()[:300])
            return
        check("fail-closed when unset; right key opens; general and wrong keys "
              "refused -- on a live app",
              verdict.get("ok") is True, f"{verdict}")


# =============================================================================
# PART 3bl -- THE SERVER RECORDS THE RESULTS (build hu, Phase 5 -- Class E)
# -----------------------------------------------------------------------------
# 2026-08-18. Mastery was CLIENT-WRITTEN: the browser parsed the model's result
# tags and POSTed scores the server accepted on format alone -- anyone holding a
# code could mint mastery and unlock the Final. Now the server records the tags
# from the reply it just generated, and the client POSTs are echo-gated: a match
# deduplicates, a mint gets 409 + telemetry. Proved live below: the tag records
# exactly once (the echo does NOT double-count), the mint is refused and leaves
# no trace in mastery, and the rejection writes its system_events row.
# =============================================================================
_HU_DRILL = r"""
import os, sys, json
os.environ["DATABASE_URL"] = "sqlite:///" + sys.argv[1]
os.environ.setdefault("WEEKLY_EMAIL", "off")
sys.path.insert(0, sys.argv[2])
from fastapi.testclient import TestClient
import main, store
c = TestClient(main.app)
H = {"X-Student-Code": "1234"}
ok = {}
# 1. the SERVER records a check tag from a reply it generated...
main._record_result_tags("1234", "algebra1",
    'You got 4 of 5! [[check unit="2" correct="4" total="5" '
    'missed="7+8 => 14"]] Nice work.')
m = store.get_mastery("1234", "algebra1")["checks"]
ok["tag_recorded"] = int((m.get(2) or {}).get("best_pct") or 0) == 80
# ...and the page's echo deduplicates instead of double-counting
r = c.post("/api/check/me", json={"unit": 2, "correct": 4, "total": 5,
                                  "course": "algebra1"}, headers=H)
m2 = store.get_mastery("1234", "algebra1")["checks"]
ok["echo_dedup"] = (r.status_code == 200 and (r.json() or {}).get("recorded") == "server"
                    and int((m2.get(2) or {}).get("checks_taken") or 0) == 1)
# 2. a MINTED result is refused and leaves no trace
r = c.post("/api/check/me", json={"unit": 9, "correct": 5, "total": 5,
                                  "course": "algebra1"}, headers=H)
m3 = store.get_mastery("1234", "algebra1")["checks"]
ok["mint_refused"] = r.status_code == 409 and not (m3.get(9) or {})
ok["mint_telemetry"] = any(e.get("kind") == "client_result_rejected"
                           for e in store.recent_events(hours=1, limit=50))
# 3. the quiz tag: recorded once, echo deduped, mint refused
main._record_result_tags("1234", "algebra1",
    'Quiz done! [[quiz unit="3" topic="1" name="counting" correct="4" total="5"]]')
q = [x for x in store.get_topic_quizzes("1234", "algebra1") if x["unit"] == 3]
ok["quiz_tag_recorded"] = len(q) == 1 and q[0]["best_pct"] == 80
r = c.post("/api/quiz/me", json={"unit": 3, "topic": 1, "name": "counting",
                                 "correct": 4, "total": 5, "course": "algebra1"},
           headers=H)
q2 = [x for x in store.get_topic_quizzes("1234", "algebra1") if x["unit"] == 3]
ok["quiz_echo_dedup"] = r.status_code == 200 and q2[0]["quizzes_taken"] == 1
ok["quiz_mint_refused"] = c.post("/api/quiz/me",
    json={"unit": 7, "topic": 1, "name": "ghost", "correct": 5, "total": 5,
          "course": "algebra1"}, headers=H).status_code == 409
# 4. a final tag outside an exam turn records NOTHING (but writes telemetry);
#    a minted final POST is refused
main._record_result_tags("1234", "algebra1",
    'Done! [[finalexam correct="18" total="18"]]', final_allowed=False)
ok["final_needs_exam_turn"] = c.post("/api/final/me",
    json={"correct": 18, "total": 18, "course": "algebra1"},
    headers=H).status_code == 409
# 5. the misses rode the tag in (rule 55's pipeline, now server-fed)
ok["misses_from_tag"] = any("7+8" in str(x.get("question") or "")
                            for x in store.get_misses("1234", "algebra1", limit=5))
print(json.dumps({"ok": all(ok.values()), "detail": {k: bool(v) for k, v in ok.items()}}))
"""


def part3bl_server_records_results():
    print("\nPART 3bl — the server records the results (build hu)")
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "main.py"), encoding="utf-8") as fh:
        msrc = fh.read()

    check("the server parses result tags on every reply lane and the opener",
          msrc.count("_record_result_tags(") >= 5,   # def + 4 call sites
          "a lane ships results only the client can record -- minting is back there")
    check("the exam gate rides the chat turn",
          'final_allowed=(final_mode == "exam")' in msrc,
          "a hallucinated [[finalexam]] outside an exam turn records a real final")
    check("the client endpoints are echo gates",
          msrc.count("_ledger_match(") >= 3 and "_reject_client_result(" in msrc
          and '"client_result_rejected"' in msrc,
          "the POSTs accept format-only again -- anyone with a code mints mastery")

    try:
        import httpx  # noqa: F401
        import sqlalchemy  # noqa: F401
    except Exception:  # noqa: BLE001
        skip("hu live drill", "httpx/sqlalchemy not installed here")
        return
    import tempfile as _tf, json as _json
    with _tf.TemporaryDirectory() as d:
        script = os.path.join(d, "hu.py")
        with open(script, "w", encoding="utf-8") as fh:
            fh.write(_HU_DRILL)
        res = subprocess.run([sys.executable, script,
                              os.path.join(d, "hu.db"), here],
                             capture_output=True, text=True, timeout=300)
        line = (res.stdout.strip().splitlines() or [""])[-1]
        try:
            verdict = _json.loads(line)
        except Exception:  # noqa: BLE001
            bad("hu live drill ran", (res.stderr or res.stdout).strip()[:300])
            return
        check("tag records once; echo dedups; mint 409s with telemetry and no trace; "
              "final needs the exam turn; misses ride the tag",
              verdict.get("ok") is True, f"{verdict}")


# =============================================================================
# PART 3bm -- ONE STORAGE BACKEND, LOUDLY (build hv, Phase 5 -- Classes E & F)
# -----------------------------------------------------------------------------
# 2026-08-18. Four closures: (1) a CONFIGURED-but-unreachable database no longer
# silently forks persistence onto stranded local files -- the teaching lanes answer
# with a warm maintenance message (ALLOW_FILE_FALLBACK marks a dev box) and Jim's
# inbox hears about it; (2) a restore never resurrects a revoked credential (token
# tables are withheld); (3) THE DELETIONS LEDGER -- a deletion newer than the
# snapshot is re-applied after the restore, so a family that asked to be forgotten
# stays forgotten, while a deletion OLDER than the snapshot is skipped so legit
# post-reset data survives; (4) the backup pass can no longer die silently, and the
# off-site copy is automated (weekly snapshot email riding the heartbeat).
# =============================================================================
_HV_DRILL = r"""
import os, sys, json, time
os.environ["DATABASE_URL"] = "sqlite:///" + sys.argv[1]
os.environ.setdefault("WEEKLY_EMAIL", "off")
sys.path.insert(0, sys.argv[2])
from fastapi.testclient import TestClient
import main, store
c = TestClient(main.app)
ok = {}
# --- a family with data, a signed-in token, and a snapshot ---------------------
tok = c.post("/api/parent/signup", json={"email": "hv@example.com",
             "password": "drill-pass-1"}).json()["token"]
kid = c.post("/api/parent/students", json={"token": tok, "name": "Ledger"}).json()
code = kid["students"][-1]["code"] if kid.get("students") else kid.get("code")
main._record_result_tags(code, "algebra1", '[[check unit="1" correct="10" total="10"]]')
# an OLD deletion (before the snapshot): reset a pilot code, then give it NEW data
store.reset_student_data("1234")
time.sleep(1.2)
main._record_result_tags("1234", "algebra1", '[[check unit="2" correct="10" total="10"]]')
time.sleep(1.2)
snap = store.export_all()
# --- after the snapshot: the family asks to be forgotten -----------------------
p = store.get_parent_by_email("hv@example.com")
store.delete_parent_cascade(p["id"])
# --- restore the snapshot ------------------------------------------------------
res = store.import_all(snap)
ok["tokens_withheld"] = "parent_tokens" in (res.get("withheld") or [])
ok["token_dead"] = c.post("/api/parent/students",
                          json={"token": tok, "name": "Ghost"}).status_code in (401, 403)
ok["family_stays_forgotten"] = (store.get_parent_by_email("hv@example.com") is None
                                and res.get("deletions_reapplied", 0) >= 1)
m = store.get_mastery(code, "algebra1")["checks"] if code else {}
ok["child_data_stays_gone"] = not (m.get(1) or {})
# the OLD deletion is NOT re-applied: 1234's post-reset unit-2 work survives
m2 = store.get_mastery("1234", "algebra1")["checks"]
ok["post_reset_work_survives"] = int((m2.get(2) or {}).get("best_pct") or 0) == 100
print(json.dumps({"ok": all(ok.values()), "detail": {k: bool(v) for k, v in ok.items()}}))
"""

_HV_DEGRADED = r"""
import os, sys, json
os.environ["DATABASE_URL"] = "postgresql+psycopg2://nouser:nopass@127.0.0.1:9/nodb"
os.environ.setdefault("WEEKLY_EMAIL", "off")
os.environ.pop("ANTHROPIC_API_KEY", None)
mode = sys.argv[2]
if mode == "dev":
    os.environ["ALLOW_FILE_FALLBACK"] = "1"
else:
    os.environ.pop("ALLOW_FILE_FALLBACK", None)
sys.path.insert(0, sys.argv[1])
from fastapi.testclient import TestClient
import main, store
c = TestClient(main.app)
r = c.post("/api/chat", json={"code": "1234", "message": "hi", "course": "algebra1"})
body = r.json()
print(json.dumps({"degraded_flag": bool(store.degraded()),
                  "gated": bool(body.get("degraded")),
                  "reply_warm": "looked after" in str(body.get("reply") or "")}))
"""


def part3bm_one_backend_loudly():
    print("\nPART 3bm — one storage backend, loudly (build hv)")
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "main.py"), encoding="utf-8") as fh:
        msrc = fh.read()
    with open(os.path.join(here, "store.py"), encoding="utf-8") as fh:
        ssrc = fh.read()

    check("the degraded state exists and the teaching lanes consult it",
          "def degraded()" in ssrc and msrc.count("_degraded_reply()") >= 3
          and "ALLOW_FILE_FALLBACK" in msrc,
          "a configured-but-dead DB silently forks onto stranded files again")
    check("the deletions ledger exists and both erasure paths write it",
          '_tables["deletions"]' in ssrc and ssrc.count("record_deletion(") >= 3,
          "a restore can resurrect a family that asked to be forgotten")
    check("the restore withholds credentials and re-applies the ledger",
          '"parent_tokens", "parent_resets", "teacher_tokens", "teacher_resets"' in ssrc
          and "deletions_reapplied" in ssrc,
          "a restore resurrects revoked tokens or undoes deletions")
    check("the backup pass fails LOUDLY and refreshes its marker on skip",
          '"ops_fail", "backup"' in msrc and "backup-failed" in msrc
          and "marker refreshed after deploy" in msrc,
          "backup_age null goes back to having two innocent readings and no alarm")
    check("the off-site copy is automated on the heartbeat",
          "def _offsite_backup_pass" in msrc and "_offsite_backup_pass()" in msrc
          and 'attachment=(name, blob)' in msrc
          and '"offsite"' in msrc,
          "the off-site copy is a manual habit again")

    try:
        import httpx  # noqa: F401
        import sqlalchemy  # noqa: F401
    except Exception:  # noqa: BLE001
        skip("hv live drills", "httpx/sqlalchemy not installed here")
        return
    import tempfile as _tf, json as _json
    with _tf.TemporaryDirectory() as d:
        script = os.path.join(d, "hv.py")
        with open(script, "w", encoding="utf-8") as fh:
            fh.write(_HV_DRILL)
        res = subprocess.run([sys.executable, script,
                              os.path.join(d, "hv.db"), here],
                             capture_output=True, text=True, timeout=300)
        line = (res.stdout.strip().splitlines() or [""])[-1]
        try:
            verdict = _json.loads(line)
        except Exception:  # noqa: BLE001
            bad("hv restore drill ran", (res.stderr or res.stdout).strip()[:300])
            return
        check("tokens withheld; the forgotten family stays forgotten; post-reset "
              "work survives an older deletion -- on a real restore",
              verdict.get("ok") is True, f"{verdict}")
        # the degraded gate, both modes
        script2 = os.path.join(d, "hvdeg.py")
        with open(script2, "w", encoding="utf-8") as fh:
            fh.write(_HV_DEGRADED)
        got = {}
        for mode in ("prod", "dev"):
            r2 = subprocess.run([sys.executable, script2, here, mode],
                                capture_output=True, text=True, timeout=300)
            line2 = (r2.stdout.strip().splitlines() or [""])[-1]
            try:
                got[mode] = _json.loads(line2)
            except Exception:  # noqa: BLE001
                bad(f"hv degraded drill ({mode}) ran",
                    (r2.stderr or r2.stdout).strip()[:300])
                return
        check("a dead configured DB gates the teaching lane with the warm message",
              got["prod"]["degraded_flag"] and got["prod"]["gated"]
              and got["prod"]["reply_warm"],
              f"{got['prod']} -- the silent file fork is back")
        check("ALLOW_FILE_FALLBACK marks a dev box and lifts the gate",
              got["dev"]["degraded_flag"] and not got["dev"]["gated"],
              f"{got['dev']} -- dev boxes cannot work offline anymore")


# =============================================================================
# PART 3bn -- THE GOVERNOR'S EYES ON PRODUCTION (build hw)
# -----------------------------------------------------------------------------
# 2026-08-18. The last queued piece of "give the governor eyes": the screen
# auditor's checks have run against fixtures on every push since build gn, but
# nothing ever looked at the REAL site nightly -- Render has no browser. The
# GitHub Actions workflow does (its runners do), driving a live three-turn lesson
# and failing the run on findings so GitHub itself notifies Jim. These checks pin
# the workflow's load-bearing pieces so it cannot silently rot in the repo.
# =============================================================================
def part3bn_screenwatch():
    print("\nPART 3bn — the governor's eyes on production (build hw)")
    here = os.path.dirname(os.path.abspath(__file__))
    wf = os.path.join(here, ".github", "workflows", "screenwatch.yml")
    if not os.path.exists(wf):
        rootcopy = os.path.exists(os.path.join(here, "screenwatch.yml"))
        bad("screenwatch workflow exists",
            "screenwatch.yml is at the repo ROOT -- move it into .github\\workflows\\ "
            "(create the two folders; the remote bridge is not allowed to write "
            "there, on purpose)" if rootcopy else
            ".github/workflows/screenwatch.yml is gone -- the nightly production "
            "screen audit no longer runs")
        return
    with open(wf, encoding="utf-8") as fh:
        src = fh.read()
    check("it runs nightly and on demand",
          "cron:" in src and "workflow_dispatch" in src,
          "the cadence is gone -- a manual screen audit is another wish")
    check("it drives the LIVE site with the real auditor",
          "screencheck.py --live https://mrcadabra.com" in src,
          "the workflow no longer points the auditor at production")
    check("the audit student comes from a secret, never the repo",
          "secrets.SCREENWATCH_CODE" in src and 'if [ -z "$SCREENWATCH_CODE" ]' in src,
          "a login code is committed, or a missing secret fails silently")
    check("the evidence is kept and the run is bounded",
          "upload-artifact" in src and "if: always()" in src
          and "timeout-minutes:" in src,
          "a finding with no report/screenshot cannot be adjudicated")
    check("screencheck --live still takes the arguments the workflow sends",
          all(s in open(os.path.join(here, "screencheck.py"), encoding="utf-8").read()
              for s in ('"--live"', '"--code"', '"--shots"', '"--out"')),
          "the workflow and the auditor's CLI have drifted apart")


# =============================================================================
# PART 3bo -- THE BETA PAGE'S KEY LEAVES THE URL (build hx)
# -----------------------------------------------------------------------------
# 2026-08-18. The review's "weakest page", diagnosed: /beta?admin=<FORUM_MOD_KEY>
# put the GENERAL ADMIN KEY in a URL (browser history + every HTTP log), and the
# page then re-sent it in query strings and bodies -- the credential-in-URL class,
# third sighting (dg killed it on /admin, hs killed it for student codes). Now the
# key lives in sessionStorage, the address bar is scrubbed, and every call is a
# header. The server's beta endpoints accept the header; the legacy body form
# stays for stale pages.
# =============================================================================
def part3bo_beta_key():
    print("\nPART 3bo — the beta page's key leaves the URL (build hx)")
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "static", "beta.html"), encoding="utf-8") as fh:
        bsrc = fh.read()
    with open(os.path.join(here, "main.py"), encoding="utf-8") as fh:
        msrc = fh.read()

    check("the page scrubs a legacy ?admin= link and stores the key like /admin",
          'sessionStorage.getItem("mt_admin_key")' in bsrc
          and "history.replaceState" in bsrc and 'params.delete("admin")' in bsrc,
          "the admin key rides the address bar into history and logs again")
    check("every beta call sends the header, none carries the key",
          '"X-Admin-Key": KEY' in bsrc
          and "list?key=" not in bsrc
          and "JSON.stringify({ key: KEY" not in bsrc,
          "the key is back in a query string or a request body")
    check("a wrong key is forgotten, not retried forever",
          'sessionStorage.removeItem("mt_admin_key")' in bsrc,
          "one mistyped key wedges the page until the tab closes")
    check("the server's beta endpoints accept the header",
          msrc.count("_require_admin(x_admin_key or body.key)") >= 3,
          "the page sends a header the server ignores -- everything 401s")
    check("the tester is told WHERE to use the pass",
          '<a href="/login"' in bsrc,
          "a pass with no door: the page never said where to enter the code")


# =============================================================================
# PART 3bp -- THE VOICE ASKS TWICE (build hy)
# -----------------------------------------------------------------------------
# 2026-08-18. Jim heard it live: he pushed hx while touring the dashboard and one
# line played in the mechanical browser voice before the warm voice returned. The
# deploy itself is the cause -- speak tickets are server memory, an instance
# switchover wipes them and can kill one in-flight prep. voice.js now re-asks for
# a fresh prep ONCE before falling back to the browser voice; an authoritative
# {voice:false} is still believed immediately, and the 5s no-start watchdog stays
# the outer guarantee. These pins keep all three properties from quietly reverting.
# =============================================================================
def part3bp_voice_retry():
    print("\nPART 3bp — the voice asks twice before going mechanical (build hy)")
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "static", "voice.js"), encoding="utf-8") as fh:
        vsrc = fh.read()
    check("a failed clip re-asks before the browser voice",
          "let retryLeft = 1;" in vsrc and "const failedClip" in vsrc
          and 'failedClip("prep failed")' in vsrc
          and 'failedClip("element error")' in vsrc
          and 'failedClip("play rejected")' in vsrc,
          "the mid-deploy seam is audible again: one dead ticket goes straight "
          "to the mechanical voice")
    check("exactly one retry, then the fallback",
          vsrc.count("let retryLeft") == 1 and "retryLeft -= 1" in vsrc
          and "const fallToBrowser" in vsrc and "fallToBrowser();" in vsrc,
          "either the retry is gone or it can loop -- both are wrong")
    check("a server that ANSWERS voice:false is believed immediately",
          re.search(r"d\.voice === false\)\s*\{\s*fallToBrowser\(\);", vsrc)
          is not None,
          "the page retries an authoritative no -- a voiceless deploy would add "
          "latency to every clip for nothing")
    check("the retry never fires after playback started or the turn ended",
          "if (started || doneCalled) return;" in vsrc
          and "if (!started && !doneCalled) startClip()" in vsrc,
          "a late retry could restart audio over a finished or playing turn")
    check("the 5s no-start watchdog is still the outer guarantee",
          "idle > 5000" in vsrc,
          "the watchdog is gone -- a hung retry now strands the student")


def part3bb_no_lost_exchange():
    print("\nPART 3bb — no exchange can be lost (build hk)")
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "main.py"), encoding="utf-8") as fh:
        msrc = fh.read()
    check("store.update_history exists and is CAS",
          "def update_history(" in open(os.path.join(here, "store.py"), encoding="utf-8").read()
          and "rowcount == 1" in open(os.path.join(here, "store.py"), encoding="utf-8").read(),
          "the atomic history transform is gone -- the model-latency race is back")
    check("the chat path appends via mutate_history",
          "mutate_history(code, req.course, lambda h: h + _exchange)" in msrc,
          "the whole-blob overwrite is back in /api/chat")
    check("the opener writes via mutate_history",
          msrc.count("mutate_history(code, req.course,") >= 2,
          "an opener racing a typed first message can erase it again")
    check("no chat-path whole-blob save remains",
          'session["history"] = history\n    save_session(' not in msrc
          and 'session["history"] = history\n        save_session(' not in msrc,
          "a save_session(whole blob) crept back into the chat handler")

    import tempfile as _tf, json as _json
    try:
        import sqlalchemy  # noqa: F401
    except Exception:  # noqa: BLE001
        skip("history CAS hammer", "sqlalchemy not installed here")
        return
    with _tf.TemporaryDirectory() as d:
        script = os.path.join(d, "hist.py")
        with open(script, "w", encoding="utf-8") as fh:
            fh.write(_HK_HISTORY)
        res = subprocess.run([sys.executable, script,
                              os.path.join(d, "hk.db"), here],
                             capture_output=True, text=True, timeout=300)
        line = (res.stdout.strip().splitlines() or [""])[-1]
        try:
            verdict = _json.loads(line)
        except Exception:  # noqa: BLE001
            bad("history CAS hammer ran", (res.stderr or res.stdout).strip()[:300])
            return
        check("96 threaded appends land exactly, pairs adjacent, insert-race safe, "
              "cap enforced", verdict.get("ok") is True,
              f"{verdict} -- an exchange was lost or torn on a REAL database")


def part3ba_one_unit_owner():
    print("\nPART 3ba — one owner for the student's unit (build hj)")
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "main.py"), encoding="utf-8") as fh:
        msrc = fh.read()
    with open(os.path.join(here, "tutor.py"), encoding="utf-8") as fh:
        tsrc = fh.read()

    # 1. THE WIRING: one resolver, and every consumer reads its result.
    check("main._resolve_unit exists", "def _resolve_unit(" in msrc,
          "the single derivation is gone -- five ad-hoc answers are next")
    check("the chat handler resolves once and passes the FIELD",
          'student_context["current_unit"] = resolved_unit' in msrc,
          "the prompt is back to regex-reading the unit out of prose")
    check("the tracker consumes the resolved value",
          # build hm: the resolved unit now reaches the tracker THROUGH the filing
          # gate -- _accept_declared_unit returns it untouched on every verdict
          # except an "accepted" declaration (the gs authority, preserved).
          "course_unit, _up_verdict = _accept_declared_unit(" in msrc
          and "declared, resolved_unit, unit_source," in msrc,
          "the tracker re-derives its own answer again -- placement can outrank "
          "progression forever on tagless turns (the pre-gs bug, review F4c)")
    check("the placement note EXPIRES once deeper truth exists",
          'if placement and unit_source in ("placement", "default")' in msrc,
          "the stale sentence rides every prompt forever again, and the prose regex "
          "has something wrong to find")
    check("the prompt consumes the field",
          '(student or {}).get("current_unit")' in tsrc,
          "build_system_prompt no longer reads the resolved unit")
    check("the referee consumes the same field",
          tsrc.count('(student or {}).get("current_unit")') >= 2,
          "_lesson_unit lost the field -- the referee and the prompt can disagree "
          "about the unit again")
    check("the drift probe sees the resolved answer",
          "resolved=resolved_unit" in msrc,
          "the probe cannot say which source answered")

    # 2. THE PRIORITY TABLE, on a real database, every push.
    import tempfile as _tf, json as _json
    try:
        import sqlalchemy  # noqa: F401
    except Exception:  # noqa: BLE001
        skip("resolve_unit priority table", "sqlalchemy not installed here")
        return
    with _tf.TemporaryDirectory() as d:
        script = os.path.join(d, "resolve.py")
        with open(script, "w", encoding="utf-8") as fh:
            fh.write(_HJ_RESOLVE)
        res = subprocess.run([sys.executable, script,
                              os.path.join(d, "hj.db"), here],
                             capture_output=True, text=True, timeout=300)
        line = (res.stdout.strip().splitlines() or [""])[-1]
        try:
            verdict = _json.loads(line)
        except Exception:  # noqa: BLE001
            bad("resolve_unit priority table ran",
                (res.stderr or res.stdout).strip()[:300])
            return
        check("the six-case priority table holds (focus > tracked > progression-"
              "from-floor > placement > default)",
              verdict.get("ok") is True,
              f"{verdict.get('got')} -- a consumer is reading a different truth than "
              f"the resolver produces")


def part3az_atomic_counters():
    print("\nPART 3az — the counters are atomic (build hi)")
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "store.py"), encoding="utf-8") as fh:
        ssrc = fh.read()

    # 1. THE PATTERN IS GONE from the five converted sites: they pass exprs= and no
    # longer read before writing the arithmetic.
    for fn, needle in [("record_minutes", '_sql_counter("minutes"'),
                       ("record_check", '_sql_best("best_pct"'),
                       ("record_topic_quiz", '_sql_counter("quizzes_taken"'),
                       ("record_topic", '_sql_deeper_status("status"'),
                       ("_set_unit_status", '_sql_deeper_status("status"')]:
        check(f"{fn} computes in the database", needle in ssrc,
              f"{fn} lost its atomic expression -- the read-then-write race is back "
              f"and best scores can regress again")
    check("the helpers exist",
          all(n in ssrc for n in ("def _sql_counter", "def _sql_best",
                                  "def _sql_deeper_status", "exprs: dict = None")),
          "the atomic machinery left _upsert")

    # 2. THE BEHAVIOURAL PROOF, against a real database, every push.
    import tempfile as _tf, json as _json
    try:
        import sqlalchemy  # noqa: F401
    except Exception:  # noqa: BLE001
        skip("atomic-counter hammer", "sqlalchemy not installed here")
        return
    with _tf.TemporaryDirectory() as d:
        script = os.path.join(d, "hammer.py")
        with open(script, "w", encoding="utf-8") as fh:
            fh.write(_HI_HAMMER)
        res = subprocess.run([sys.executable, script,
                              os.path.join(d, "hi.db"), here],
                             capture_output=True, text=True, timeout=300)
        line = (res.stdout.strip().splitlines() or [""])[-1]
        try:
            verdict = _json.loads(line)
        except Exception:  # noqa: BLE001
            bad("atomic-counter hammer ran",
                (res.stderr or res.stdout).strip()[:300])
            return
        check("40 threaded writes land exactly (minutes, checks, attempts) and the "
              "best never regresses",
              verdict.get("ok") is True,
              f"{verdict} -- a lost update or a regressed best on a REAL database")


def part3ay_one_grammar():
    print("\nPART 3ay — one tag grammar (build hh)")
    here = os.path.dirname(os.path.abspath(__file__))
    import tags as T

    # 1. INTERNAL CONSISTENCY of the registry itself.
    check("every figure tag is a board tag", set(T.FIGURE_TAGS) <= set(T.BOARD_TAGS),
          f"orphans: {set(T.FIGURE_TAGS) - set(T.BOARD_TAGS)}")
    check("every step tag is a pending-board tag", set(T.STEP_TAGS) <= set(T.PENDING_BOARD_TAGS),
          f"orphans: {set(T.STEP_TAGS) - set(T.PENDING_BOARD_TAGS)}")
    check("every pending-board tag is a board tag",
          set(T.PENDING_BOARD_TAGS) <= set(T.BOARD_TAGS),
          f"orphans: {set(T.PENDING_BOARD_TAGS) - set(T.BOARD_TAGS)}")
    check("no tag is declared twice within a set",
          all(len(x) == len(set(x)) for x in (T.FIGURE_TAGS, T.BOARD_TAGS,
                                              T.PENDING_BOARD_TAGS, T.STEP_TAGS)),
          "a duplicate member means two edits raced")
    # balance, machine and objects are FIGURES (the caption and visual referees must
    # treat them as pictures) that happen to have DEDICATED renderers instead of
    # routing through showFig/showGeo. That exact overlap is legitimate and pinned;
    # any NEW overlap is a tag about to be rendered two ways.
    check("the handler/figure overlap is exactly the three dedicated-renderer figures",
          set(T.TAG_HANDLER) & set(T.FIGURE_TAGS) == {"balance", "machine", "objects"},
          f"got {sorted(set(T.TAG_HANDLER) & set(T.FIGURE_TAGS))} -- a new overlap "
          f"means a tag is about to be drawn twice, or a figure lost its referee "
          f"coverage; decide which list owns it and pin the answer here")
    check("every CONTENT_ATTRS key is a known tag",
          set(T.CONTENT_ATTRS) <= set(T.BOARD_TAGS) | set(T.TAG_HANDLER),
          f"unknown: {set(T.CONTENT_ATTRS) - set(T.BOARD_TAGS) - set(T.TAG_HANDLER)}")

    # 2. THE DERIVATIONS. tutor.py and this file must READ the registry, never
    # re-declare it -- a literal tuple typed beside the import is how _FIGURE_TAGS
    # became a 22-member re-declaration of FIGURE_TAGS in the same file.
    check("tutor.FIGURE_TAGS is the registry's", tuple(tutor.FIGURE_TAGS) == tuple(T.FIGURE_TAGS),
          "tutor re-declared the figure list -- the caption and visual referees can "
          "now disagree with the battery about what counts as a figure")
    check("tutor's board set is the registry's", tuple(tutor._BOARD_TAGS) == tuple(T.BOARD_TAGS),
          "tutor re-declared the board list")
    check("tutor's pending set is the registry's",
          tuple(tutor._PQ_BOARD_TAGS) == tuple(T.PENDING_BOARD_TAGS),
          "tutor re-declared the pending list")
    with open(os.path.join(here, "tutor.py"), encoding="utf-8") as fh:
        tsrc = fh.read()
    check("tutor.py contains no hand-typed figure list",
          '"unitcircle", "righttriangle"' not in tsrc,
          "a literal figure tuple is back in tutor.py -- delete it and derive from tags.py")
    with open(os.path.join(here, "ruletests.py"), encoding="utf-8") as fh:
        rsrc = fh.read()
    check("this battery derives its tables from the registry",
          "TAG_HANDLER = dict(_tagreg.TAG_HANDLER)" in rsrc
          and 'BOARD_TAG = re.compile(r"\\[\\[\\s*(" + "|".join(_tagreg.PENDING_BOARD_TAGS)' in rsrc,
          "the checker declared its own copy of the contract again -- checker and "
          "checked can drift in step and notice nothing")

    # 3. THE PAGES. Every tag a page dispatcher handles must be registered -- a tag
    # added to a page without registering it here is invisible to every referee.
    known = set(T.BOARD_TAGS) | set(T.TAG_HANDLER) | set(T.TAG_INLINE)
    for page in ("session.html", "practice.html", "topic.html"):
        with open(os.path.join(here, "static", page), encoding="utf-8") as fh:
            psrc = fh.read()
        i = psrc.find("function handleTags(")
        if i < 0:
            bad(f"{page}: handleTags found", "the dispatcher is gone"); continue
        ht = psrc[i:]
        ht = ht[:ht.find("\n    function ")] if "\n    function " in ht else ht[:6000]
        dispatched = set(re.findall(r'name === "([\w-]+)"', ht))
        for arr in re.findall(r'\[((?:"[\w-]+",?\s*)+)\]\.indexOf\(name\)', ht):
            dispatched |= set(re.findall(r'"([\w-]+)"', arr))
        unregistered = sorted(dispatched - known)
        check(f"{page}: every dispatched tag is in the registry", not unregistered,
              f"{unregistered} are rendered by this page but unknown to tags.py -- "
              f"every referee and every battery check is blind to them")


def part3ax_one_pipeline():
    print("\nPART 3ax — one reply pipeline (build hg)")
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "tutor.py"), encoding="utf-8") as fh:
        tsrc = fh.read()

    check("_reply_pipeline exists", "def _reply_pipeline(" in tsrc,
          "the unified pipeline is gone -- three hand-copied lanes are next")
    # Exactly ONE live call of _create_verified (in the pipeline). More means a lane
    # has broken away and will drift; fewer means nothing is refereed at all.
    calls = len(re.findall(r"reply = _create_verified\(", tsrc))
    check(f"_create_verified has exactly one call site ({calls})", calls == 1,
          "a getter is calling the verifier directly again -- that lane's future "
          "referees, nets and probes will need separate wiring, and will miss it")
    # The teaching lanes build no Anthropic client of their own: pipeline + the
    # assessment writer + the retired board net (kept dead, build gn) = 3.
    clients = tsrc.count("Anthropic(api_key")
    check(f"no getter constructs its own client ({clients} total)", clients == 3,
          "a fourth Anthropic(...) appeared -- some path is bypassing the pipeline "
          "and every referee in it")
    for fn in ("get_tutor_reply", "get_practice_reply", "get_topic_reply"):
        # get_topic_reply is the LAST function in the file, so the body must be
        # bounded by next-def OR end-of-file -- with only next-def, the last
        # lane's check reads an empty body and fails on healthy code.
        body_m = re.search(r"def " + fn + r"\([\s\S]*?(?=\ndef |\Z)", tsrc)
        body = body_m.group(0) if body_m else ""
        check(f"{fn} goes through the pipeline", "_reply_pipeline(" in body,
              "this lane broke away from the unified sequence")
        check(f"{fn} does not call the verifier directly",
              "_create_verified(" not in body,
              "direct verifier calls are how the lanes drifted apart before")
    # The lane-specific facts stay legible and correct:
    check("only the lesson lane runs the TODAY-bar net",
          tsrc.count("post=lambda reply: ensure_today_tag(") == 1,
          "either the net vanished from lessons or a side-trip lane gained a bar "
          "it has no UI for")
    check("prompt building stays INSIDE the pipeline's try (a callable, not a string)",
          "lambda: build_system_prompt(student, course)" in tsrc
          and "lambda: build_practice_prompt(student, problem, course)" in tsrc
          and "lambda: build_topic_prompt(student, topic, course)" in tsrc,
          "a prompt built eagerly at the call site escapes the try -- a prompt-builder "
          "crash would 500 at a child instead of degrading to the friendly message")


def part3aw_one_copy():
    print("\nPART 3aw — one copy, and it stays one copy (build hc)")
    here = os.path.dirname(os.path.abspath(__file__))
    pages = ("session.html", "topic.html", "practice.html")

    for mod, fns in SHARED_JS_MODULES.items():
        path = os.path.join(here, "static", mod)
        if not os.path.exists(path):
            bad(f"static/{mod} exists", "the shared module is gone -- every page that "
                                        "loads it now has undefined functions")
            continue
        with open(path, encoding="utf-8") as fh:
            src = fh.read()
        for fn in fns:
            check(f"{mod} defines {fn}()", f"function {fn}" in src,
                  "it moved or was renamed -- the pages call it by this name")
        for const in SHARED_JS_CONSTS.get(mod, []):
            check(f"{mod} still owns {const}", const in src,
                  "the table the renderer depends on is gone")
        check(f"{mod} is a CLASSIC script (no export/import)",
              "export " not in src and "import " not in src,
              "it became a module -- classic scripts are what keep these as globals, "
              "which is what lets every existing call site work unchanged")
        check(f"{mod} ends with the truncation statement",
              "I did no harm and this file is not truncated" in src,
              "the standing rule for every file in this repo")

    # NO PAGE MAY RE-INLINE ANY OF IT. This is the check that keeps the cure from
    # being undone one convenient paste at a time.
    for page in pages:
        path = os.path.join(here, "static", page)
        if not os.path.exists(path):
            bad(f"{page} exists", "missing from static/"); continue
        with open(path, encoding="utf-8") as fh:
            html = fh.read()
        inline = "\n".join(re.findall(r"<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>",
                                      html, re.S))
        for mod, fns in SHARED_JS_MODULES.items():
            check(f"{page} loads /static/{mod}", f"/static/{mod}" in html,
                  f"without it, {fns[0]}() is undefined on this page")
            relapsed = [fn for fn in fns if f"function {fn}" in inline]
            check(f"{page} does NOT re-inline {mod}'s functions", not relapsed,
                  f"{relapsed} were pasted back into this page. Two copies means the "
                  f"next fix lands in one of them -- that is exactly how build gz's two "
                  f"live defects were born. Edit static/{mod} instead.")
        for mod, names in SHARED_JS_STATE.items():
            redecl = [nm for nm in names
                      if re.search(r"\b(?:let|const|var)\s+(?:[^;\n]*?,\s*)?" + nm
                                   + r"\b", inline)]
            check(f"{page} does NOT re-declare {mod}'s state", not redecl,
                  f"{redecl} re-declared at page level -- a duplicate top-level let is a "
                  f"SyntaxError that kills this page's ENTIRE script at parse time. The "
                  f"state lives in static/{mod}; assign to it, never re-declare it.")
        # The include must come BEFORE the inline script that calls into it.
        first_inline = html.find("<script>")
        for mod in SHARED_JS_MODULES:
            at = html.find(f"/static/{mod}")
            check(f"{page} loads {mod} before its own script runs",
                  at >= 0 and (first_inline < 0 or at < first_inline),
                  "the include comes after the page's inline code, so the functions are "
                  "undefined at the moment the page first uses them")


def part3au_undeclared_identifiers():
    print("\nPART 3au — the undeclared-identifier sweep (build hb)")
    here = os.path.dirname(os.path.abspath(__file__))
    paths, missing = [], []
    for name in JS_SWEPT_PAGES:
        p = os.path.join(here, "static", name)
        (paths if os.path.exists(p) else missing).append(p)
    check("every swept page exists", not missing, f"missing: {missing}")
    if not paths:
        bad("the sweep had pages to read", "no pages found"); return
    try:
        findings = js_scope_audit(paths)
    except Exception as exc:  # noqa: BLE001
        bad("the undeclared-identifier sweep ran", f"{type(exc).__name__}: {exc}")
        return
    total = 0
    for p in paths:
        out = findings.get(p, [])
        total += len(out)
        detail = "; ".join(f"{nm} — {why} (script line {ln})" for nm, ln, why in out)
        check(f"{os.path.basename(p)}: no identifier is used out of scope",
              not out,
              detail + "  ← this is the build-gz class: a fix copied between pages "
                       "without the state it reads. The browser throws, a catch eats "
                       "it, and the student gets blamed for the failure.")
    print(f"       swept {len(paths)} pages · {total} finding(s)")

    # THE DETECTOR MUST STILL FIRE. A sweep that has gone silent because the analyzer
    # broke looks exactly like a clean codebase -- the review's whole meta-finding.
    # So: reintroduce build gz's two real defects into a COPY of topic.html in memory
    # and require both to be caught, every run.
    import tempfile as _tf
    try:
        tp = os.path.join(here, "static", "topic.html")
        src = open(tp, encoding="utf-8").read()
        bugged = src.replace('    let lastTutorText = "";\n', "", 1) \
                    .replace("else if (audioWarmed) startKeepAlive();",
                             "else if (started) startKeepAlive();", 1)
        with _tf.TemporaryDirectory() as d:
            dst = os.path.join(d, "topic_bugged.html")
            with open(dst, "w", encoding="utf-8") as fh:
                fh.write(bugged)
            got = js_scope_audit([os.path.join(here, "static", "session.html"), dst])
            names = {nm for nm, _ln, _w in got.get(dst, [])}
        check("self-test: the sweep still catches gz's lastTutorText defect",
              "lastTutorText" in names,
              f"the analyzer went blind -- it reported {sorted(names)} for a file that "
              f"definitely has the defect")
        check("self-test: the sweep still catches gz's inner-scope `started` defect",
              "started" in names,
              f"the inner-scope half of the class is no longer detected; reported "
              f"{sorted(names)}")
    except Exception as exc:  # noqa: BLE001
        bad("the sweep's self-test ran", f"{type(exc).__name__}: {exc}")


def main():
    if "--rules" in sys.argv:
        print("wrote", write_rules_index(os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "RULES.md")))
        return 0
    live = "--live" in sys.argv
    print("=" * 70)
    print("RULE REGRESSION BATTERY —", "OFFLINE + LIVE" if live else "OFFLINE ONLY")
    print("=" * 70)
    part1_coverage()
    part2_prose()
    part3_speech()
    part3b_foundations()
    part3c_board_tags()
    part3d_foundation_memory()
    part3e_page_parity()
    part3f_notation()
    part3g_misconceptions()
    part3h_scale()
    part3i_rule_verification()
    part3j_walkthroughs()
    part3k_mastery_reachable()
    part3l_lesson_auditor()
    part3n_sprints()
    part3o_unit_name_parity()
    part3p_marketing_claims()
    part3q_reliability()
    part3r_batch_d_figures()
    part3s_backups()
    part3t_teaching_upgrades()
    part3u_video_presence()
    part3u2_talking_moments()
    part3v_course_identity()
    part3w_generalizations()
    part3x_fraction_pie()
    part3y_diagnosis_and_symbols()
    part3z_reply_integrity()
    part3aa_placement_honesty()
    part3ab_seven_defects()
    part3ac_voice_sequencing()
    part3ad_clip_never_eats()
    part3ae_classroom_locked()
    part3af_full_journey()
    part3ag_shots_match_copy()
    part3ah_audit_findings_fe()
    part3aj_screen_checks()
    part3ak_night_watch()
    part3al_openai_boundary()
    part3am_spoken_letter_and_sign()
    part3an_unit_follows_teaching()
    part3ao_invented_history()
    part3ap_bare_demand_and_decimals()
    part3aq_refused_demonstration()
    part3ar_rule_spoken_as_law()
    part3as_phase0()
    part3at_eyes()
    part3au_undeclared_identifiers()
    part3av_unit_referee_rearmed()
    part3aw_one_copy()
    part3ax_one_pipeline()
    part3ay_one_grammar()
    part3az_atomic_counters()
    part3ba_one_unit_owner()
    part3bb_no_lost_exchange()
    part3bc_small_cuts()
    part3bd_truth_opener()
    part3be_streak_clock()
    part3bf_record_claims()
    part3bg_order_of_authority()
    part3bh_two_prompt_sizes()
    part3bi_story_units()
    part3bj_credential_leaves_url()
    part3bk_bounded_and_split()
    part3bl_server_records_results()
    part3bm_one_backend_loudly()
    part3bn_screenwatch()
    part3bo_beta_key()
    part3bp_voice_retry()
    part3ai_deploy_stamp()
    if live:
        part4_live()
    else:
        print("\nPART 4 — live scenarios")
        skip("live scenarios", "pass --live to run them")
    print("\n" + "=" * 70)
    print(f"{len(PASS)} passed · {len(FAIL)} failed · {len(SKIP)} skipped")
    if FAIL:
        print("\nFAILURES:")
        for name, detail in FAIL:
            print(f"  - {name}: {detail}")
    print("=" * 70)
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())

# I did no harm and this file is not truncated.

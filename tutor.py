# =============================================================================
# tutor.py  --  Math Tutor MVP  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-08-18  BUILDS ia + ib -- THE TWENTY-THIRD AND TWENTY-FOURTH REFEREES, both
#               from ONE live quiz run of Jim's. ia: quiz_term_conflict (rule 47e) --
#               a question offering the acute/right/obtuse choice when the
#               conversation never taught those words is rejected. First referee fed
#               the conversation itself: _create_verified now computes `heard` (the
#               ORIGINAL messages' text, never the retry msgs -- a rejected draft
#               plus its nudge must not teach the checker its own vocabulary) and
#               prose_board_conflict passes it down; silent when the caller cannot
#               know. The reply's own prose outside the question counts as heard, so
#               teach-then-quiz in one reply stays legal. ib:
#               question_self_contained_conflict (rule 47g) -- a NUMBERED quiz
#               question ("Question 5:") that states "the vertex ... at Y" and then
#               asks "what is the vertex" is rejected; outside a numbered quiz the
#               shape stays legal (rule 47's say-it-back move). PARTs 3br/3bs.
#   2026-08-18  BUILD hz -- THE TWENTY-SECOND REFEREE: THE PROMISED COMPARISON.
#               Jim's live catch (geometry, angle sizes): "Here's our angle again,
#               fifty degrees, next to a right angle for comparison" -- and the board
#               showed ONLY the fifty. The promised-picture referee stayed quiet
#               because a figure WAS drawn; the content referees only know triangles.
#               NEW angle_compare_conflict(reply): fires when the prose places the
#               angle next to / beside / alongside a right angle (or says "right
#               angle ... for comparison") and no [[angle]] tag in the reply carries
#               deg="90". A bare comparison QUESTION ("compared to ninety, is fifty
#               bigger?") never fires -- asking needs no second picture; claiming one
#               is on the board does. The fix it teaches: draw the piece INSIDE the
#               right angle ([[angle deg="90" split="50"]]) or drop the claim. Rule
#               63(e) carries the words (prompts.py); fail open; both directions +
#               canonical sweep in PART 3bq.
#   2026-08-18  BUILD ht -- THE UPSTREAM CALL IS BOUNDED (Phase 5, review Class F).
#               Every Anthropic client is now constructed with
#               timeout=ANTHROPIC_TIMEOUT_S (env, default 60s) and max_retries=1 --
#               the SDK default was ~600s with 2 retries, so a hung upstream could
#               freeze a child for ten minutes while the page said "thinking". A
#               slow-but-working reply still lands; a hung one becomes the friendly
#               try-again message; the pages' own 90s fetch abort (same build) is
#               the outer guarantee.
#   2026-08-18  BUILD hr -- THE TWENTY-FIRST REFEREE: THE STORY-UNITS CHECK. The
#               night watch's first confirmed catch on the live Phase-4 build
#               (08:44 UTC report): 4 + 3 × 2 modeled as "4 dollars, plus 3 bags of
#               2 candies each" -- dollars added to candies, the numbers as
#               decoration. NEW story_units_conflict(reply): fires when one sentence
#               adds a money amount to grouped NON-money objects with no price
#               resolution ("...that cost 1 dollar each" stays a fine shopping
#               story; "and" merely lists facts and never fires). The rule-27
#               precedent: narrow enforcement of the caught shape, while rule 32's
#               new one-unit clause (prompts.py) covers the class in words.
#   2026-08-18  BUILD ho -- THE TWENTIETH REFEREE: THE RECORD-CLAIM CHECK (the
#               count-claim probe's promotion; Phase 4, Class D). The audit's most
#               corrosive shape -- a child refused a demonstration on the invented
#               evidence "you've now watched this move twice" -- is now vetoed like
#               arithmetic. NEW record_claim_conflict(reply, record): SCORE claims
#               must name a score the record holds (exempt when the reply carries
#               its own [[quiz]]/[[check]]/[[finalexam]] tag -- rule 45's referee
#               owns in-reply results); "you've mastered Unit N" / "Unit N is in
#               progress" are checked against the record's mastered/touched sets
#               (future conditionals exempt); WATCH-COUNT claims are refused
#               outright -- no record stores per-event counts, so the number can
#               never be a memory (rule 65d's principle, enforced). Armed via
#               meta["record"] (main._claim_record, lesson lane); silent where the
#               caller cannot know; fail open, canonical-swept, tested in both
#               directions on the audit's own transcript shapes.
#   2026-08-18  BUILD hm -- THE NINETEENTH REFEREE: THE UNITPLAN CHECK (Phase 4 of the
#               full-app review begins -- Class D, the model's word becoming truth).
#               A hallucinated [[unitplan unit="N"]] used to sail through the sweep,
#               get filed into topic_progress by main.py, and come back as the rail's
#               truth on the next resume (the likeliest phantom-Unit-5 mechanism).
#               New unitplan_conflict(reply, allowed_units): the server computes which
#               units the RECORD can justify (main._unit_allowed_set -- resolved,
#               focus, touched, mastered, next-in-progression, or asked-for-by-the-
#               student THIS turn) and a declaration outside that set is regenerated,
#               exactly as [[verify]]/SymPy vetoes arithmetic. Wired via
#               meta["allowed_units"] (lesson lane only; silent where the caller
#               cannot know). The pattern for reading the tag's unit now lives in
#               tags.UNITPLAN_UNIT_PATTERN -- one grammar source, two consumers.
#   2026-08-17  BUILD hj -- THE UNIT ARRIVES AS A FIELD. build_system_prompt and
#               _lesson_unit (the fourteenth referee) now read
#               student["current_unit"] -- the value main._resolve_unit derived ONCE
#               -- before any older path. The regex-the-prose fallback
#               (_unit_from_progress) survives only for callers that predate the
#               field (nightwatch drives get_tutor_reply directly with synthetic
#               students); when the field is present, no prose is parsed at all.
#               Referee and prompt still cannot disagree -- same field, one owner.
#   2026-08-17  BUILD hh -- THE TAG GRAMMAR HAS ONE SOURCE (tags.py; the last Phase 2
#               build). FIGURE_TAGS, _BOARD_TAGS and _PQ_BOARD_TAGS now DERIVE from
#               the registry; the rule-18b sweep's inline step|write|solve regex
#               became _STEP_TAG_RE, compiled once from tags.STEP_TAGS; and
#               _FIGURE_TAGS -- which turned out to be a LITERAL RE-DECLARATION of
#               FIGURE_TAGS, the same 22 members re-typed by hand in a different
#               order in the same file -- is now simply FIGURE_TAGS. The tags import
#               is deliberately NOT defensive: tags.py is pure data, and "the
#               referees silently forgot what a tag is" must stop a deploy at boot,
#               not degrade in the dark. ruletests PART 3ay guards the derivations.
#   2026-08-17  BUILD hg -- ONE REPLY PIPELINE (Phase 2's backend half). The three
#               reply getters were hand-copied variants of one sequence -- key check,
#               model, history trim, client, _create_verified, fallback, post-nets,
#               graceful catch-all -- and the copies had already cost real coverage
#               twice: practice/topic ran for weeks with the fourteenth referee
#               silently disarmed (re-armed in hb), and only lessons ran the TODAY
#               net. NEW _reply_pipeline() is the single sequence; the getters are
#               thin CONFIGURATIONS naming exactly what differs per lane: the prompt
#               builder (passed as a CALLABLE so a prompt crash still degrades to the
#               friendly message inside the try, never a 500 at a child), the
#               referee's unit, the log tag, the telemetry name, the turn-note
#               (lesson only, build cm) and the post-net (TODAY bar, lesson only).
#               Every future referee/net/probe now lands in every lane by
#               construction. Verified: the no-key path returns the identical message
#               on all three lanes; one _create_verified call site; no getter builds
#               its own client; ruletests PART 3ax guards all of it (mutation-tested:
#               an eagerly-built prompt escaping the try is caught).
#   2026-08-17  BUILD hb -- THE FOURTEENTH REFEREE IS RE-ARMED ON PRACTICE AND TOPIC.
#               The full-app review found unit_claim_conflict silently DISARMED in both
#               side-trip modes since build gn: they passed no "unit" in meta, and the
#               referee stays mute without one -- so "welcome back to Unit 7" was caught
#               in a lesson and unguarded on two thirds of the teaching surface.
#               WHICH unit it is armed with matters more than the arming. NOT the
#               student's placed unit: a practice problem is a side trip and may come
#               from any unit, so that would fire on correct teaching and regenerate
#               good replies. It is the unit of the PROBLEM (or topic) -- exactly what
#               build_practice_prompt / build_topic_prompt already use to pick the
#               playbook, so the referee and the prompt cannot disagree (the gn
#               property). Unclassifiable text yields None and the referee stays silent.
#               WITH IT, _UNIT_CLAIM_RE WIDENED FOR CONTRACTIONS: "you're in the middle
#               of Unit 7" walked past the pattern while "you are ..." was caught -- an
#               apostrophe was the entire difference. Now we're/you're/you've/been.
#               Verified both directions (6 must-fire, 6 must-stay-silent) and swept
#               over all 1,014 canonical foundation strings x 9 units: 0 false alarms.
#               ruletests PART 3av.
#   2026-08-17  BUILD ha -- EYES (Phase 1 of the full-app review). The review's
#               meta-finding: this file applied fail-open ~19 times with print-only
#               reporting, so a crashed referee and a healthy one emitted identical
#               signals -- store.record_error was unreachable from the teaching path
#               because get_tutor_reply converts every exception to a friendly string.
#               A referee here once corrupted authored foundation scripts for FOUR
#               BUILDS unreported (gl -> gw). Now: a tiny _event() helper writes one
#               row to store.system_events (never raises, no-ops when the store is
#               off) and EVERYTHING counts itself -- every referee FIRE (all 19 paths
#               in prose_board_conflict, by name), every referee CRASH (all 19 fail-open
#               handlers + mathcheck's), every PASS-THROUGH (a reply shipped with a
#               known finding, mathcheck or prosecheck), every probe observation
#               (countclaim, markcheck), both [promptsize] alarms, and the three
#               teaching-path catch-alls (failopen). A dead check is now a visible
#               zero on /admin instead of a silence.
#   2026-08-17  BUILD gz -- THE PROMPT CEILING IS ENFORCED WHERE THE PROMPT IS BUILT.
#               Full-app review, Phase 0. The 180,000-char ceiling lived only in a
#               ruletests measurement taken with a FRESH student; a returning student who
#               had heard every foundation script assembled to 186,890-194,284 chars ON
#               EVERY COURSE (measured in a clean container against this exact code) and
#               nothing at runtime noticed. Second shipping of this miss class (gf's
#               185,595 was the first). Now: PROMPT_CEILING is defined HERE (ruletests
#               imports it -- one definition, per the review's "facts without owners"
#               class); build_system_prompt checks every assembly; an over-ceiling prompt
#               is reassembled with heard-script wording DEFERRED -- the cl mechanism cn
#               kept dormant for exactly this day ("it becomes the right answer if the
#               library ever grows to where it does not fit"). Refresher turns carry the
#               words regardless (foundations_force_verbatim, set by main.py from
#               foundations.wants_refresher) so rule 40's promise -- the exact script is
#               restored the moment they ask -- stays true. Under-ceiling students get a
#               byte-identical prompt to before: the cache stays warm, nothing changes.
#               Every remaining overflow prints [promptsize] OVER CEILING, loudly.
#   2026-08-17  BUILD gy -- A RULE SPOKEN AS A LAW: rule 54 widened, rule 61's fraction
#               case born enforced (the EIGHTEENTH referee). The last of the six causes
#               from the day's audit triage.
#               RULE 54: "'of' means multiply" (the percents lesson). The banned list was
#               story-cue words only, and "of" belongs there by that list's own logic --
#               "sum" and "difference" NAME their operations and rule 37 requires teaching
#               them, while "of" merely CORRELATES inside one problem type. A child taught
#               it as a rule applies it to "3 out of 4". Added with it: the rest of the
#               classic bad mnemonic ("is means equals, of means times"), plus per and each.
#               RULE 61: "the bottom number never changes, we just add the top numbers" (the
#               fractions lesson). Rule 61 is generally UNENFORCEABLE -- "always" and "never"
#               are frequently true, including in rule 64's own "a length is never negative".
#               What makes this case decidable is that THE SAME LESSON SAYS IT CORRECTLY
#               THREE TIMES ("since the denominators match", "same-bottom-number fractions",
#               "since the slices are the same size"). The tutor knows the condition and
#               drops it, so the check is only: is the condition in the sentence? 0 false
#               alarms across 1,015 canonical scripts, which is the test that matters --
#               the fraction library states this rule many times over.
#   2026-08-17  BUILD gx -- THE REFUSED-DEMONSTRATION REFEREE (rule 65), the SEVENTEENTH,
#               and the worst thing the day's audit found. Twice in one geometry lesson a
#               child asked to be SHOWN and was turned down:
#                 "Can you show me taking the square root of 169?"
#                   -> "You've now watched this move twice -- let's flip it." (new triangle)
#                 "Can you show me 8 squared and 15 squared first?"
#                   -> "You've watched this exact move twice now... let's see you try it."
#               Both counts were FALSE; the move had been shown once. So the refusal rested
#               on invented evidence, and the child was told they should already know it --
#               which they cannot correct, because they cannot see the transcript.
#               A student saying "show me" is handing over the exact information a tutor
#               spends a lesson trying to get: they are not ready alone. Withdrawing the
#               scaffold is right when their WORK says so, never as the answer to this.
#               THE DISCRIMINATOR CAME OUT OF THE LESSON ITSELF, which is why it can be
#               trusted: earlier in the same transcript the same student asked the same kind
#               of question and was answered properly -- and every compliant reply carries a
#               COMPLETED board line ("5^2 = 25"), while the refusals carry only pending
#               ones. All three conditions required: asked to be shown, nothing worked out,
#               work handed back. 0 false alarms on 1,015 scripts x 6 phrasings -- after the
#               sweep caught two over-broad conditions in an early draft (a card TITLE
#               ending in "?", and the VARIABLE x read as a multiplication sign).
#   2026-08-17  BUILD gw -- THE BARE ANSWER-DEMAND, THE DECIMAL, AND A REFEREE THAT HAD
#               BEEN FIGHTING US. Three fixes from one thread of the day's audit.
#               (1) The decimal-alignment lesson raised a rule 15 and a rule 44 finding
#               that turned out to be ONE defect: board [[step eq="2.6 + 1.35"]] with no
#               "?", prose "...add column by column. What do you get?". Rule 15's referee
#               needs the numbers to be IN the asking sentence; rule 44's referee only
#               inspects board values containing "?". THE MISSING "?" HID THE PROBLEM FROM
#               BOTH AT ONCE. A bare demand for an answer now counts as an ask when the
#               board is holding a real computation for it to be about.
#               (2) Underneath it, gk's fraction bug wearing a decimal point: the
#               digit-scatter fallback found the "1" of 1.35 inside the word "one" in
#               "let's try ONE with a similar setup" and called the problem spoken. A
#               decimal now counts as read only when its whole part is said beside "point"
#               -- or "dollars", because "three dollars and ninety seven cents" IS reading
#               3.97 aloud.
#               (3) ⭐ NOT FROM THE AUDIT AT ALL -- the canonical sweep found it. gl's
#               self-correction referee read "hold on" as the tutor changing its mind, and
#               TWO foundation scripts say "so hold on to this" / "the one to hold on to".
#               It has been REGENERATING AUTHORED CONTENT. A referee that fights the
#               foundation library is worse than no referee: it burns a model call and can
#               cost the student the good draft (dg). "hold on TO something" is a teaching
#               instruction, not a wobble.
#   2026-08-17  BUILD gv -- THE INVENTED HISTORY: one referee widened, one probe added.
#               The day's audit found SEVEN claims about what had already happened that
#               were untrue, and they split on whether a referee can CHECK them.
#               ENFORCED: "you completed the square start to finish on your own", said to a
#               student who answered two sub-steps of a procedure the tutor wrote every
#               line of. gm's gates all let it through correctly by their own terms -- the
#               student DID show working -- because gm asks "did they show A method?" and
#               this sentence begs "did they do THE WHOLE THING?". narrated_method_conflict
#               gains a TOTALITY branch that runs first: a totality phrase plus a NAMED
#               procedure over a fragment. Warmth about a problem they did answer ("you
#               solved it all by yourself", to an eight-year-old) is deliberately untouched.
#               MEASURED: "you've now watched this move twice" (said twice, both false),
#               "all three conversions under your belt", "your last score was 85%", "Unit 9
#               is also still in progress". Every one is a claim about the whole
#               conversation or about a record this function has never seen, so
#               count_claim_probe LOGS and changes nothing. ⚠️ The false count is the ENGINE
#               of the worst behaviour in the audit: a student asked "can you show me
#               taking the square root of 169?" and was refused with "you've now watched
#               this move twice". A child asking to be shown, turned down on invented
#               evidence. Enforcement waits for the probe's data -- two diagnoses this week
#               were guesses, and this one will not be a third.
#   2026-08-17  BUILD gu -- THE COLD-QUIZ REFEREE (rule 47(d)), the SIXTEENTH, and it is
#               six days late. Two lines, side by side:
#                 2026-08-11 audit:  "let's do it -- five questions, all on finding the
#                                     percent of a number"
#                 2026-08-17 audit:  "Let's do it - five questions, all on finding the
#                                     percent of a number."
#               WORD FOR WORD. Rule 47(d) was written FROM the first one; it fixes the
#               instrument at TEN questions and forbids a smaller one wearing the Unit
#               Quiz's name into a child's record. The tutor said it again unchanged
#               because rule 47 was COVERED and nothing watched it. gm's lesson, twice
#               over: a rule written from a real incident that fails again is a wish.
#               Enforceable precisely BECAUSE 47(d) already fixed the number and already
#               sanctioned the smaller instrument on one condition -- that the tutor says
#               which one it is. So the check is the rule: a quiz is starting, the stated
#               count is not ten, and the reply never names the instrument. 11 cases both
#               directions; 0 false alarms on 1,015 canonical scripts. Note the negative
#               lookahead in _CQ_NAMED -- 47(d)'s remedy REQUIRES mentioning the unit quiz
#               ("the Unit 7 quiz also covers..."), so a bare mention test would have
#               rejected the very sentence the rule asks for.
#   2026-08-17  BUILD gt -- BOARD NOTATION LEARNS THREE MORE SHAPES, and the way they were
#               found is the point. Five lesson-audit runs (ten lessons, 27 findings) turned
#               up three malformed board lines that board_notation_conflict ALREADY EXISTED
#               to catch and walked straight past:
#                 [[step eq="1 + 2 = 3 -> 3/4"]]        an arrow AFTER the equals sign, so
#                                                       the line asserts 3 -> 3/4 and a child
#                                                       can read "three equals three fourths"
#                 [[step eq="12: which digit is the ones? = ?"]]   a QUESTION inside an
#                                                       equation tag -- not maths at all
#                 [[step eq="(x+4)^2 = (x+4)^2"]]       a TAUTOLOGY where the factoring
#                                                       belonged; it records no step
#               None of the three needs judgement, which is what makes the miss instructive:
#               the audit's real product was not the bad turns, it was THE SHAPE OF OUR OWN
#               BLINDNESS. Scoped to eq= deliberately -- a [[write text]] may carry an arrow
#               ("f(x) <- say it out loud") and a [[step check]] may repeat a value ("6 = 6,
#               so the limit is 6"); only an eq= claims to BE an equation.
#               Verified against 76 real board lines from those same five transcripts: it
#               fires on exactly the three the auditor flagged and is silent on the other
#               73. 0 false alarms across 1,015 canonical scripts.
#   2026-08-17  BUILD gr -- THE SIGNED-ANSWER REFEREE (rule 64), the FIFTEENTH. Jim
#               answered "minus five" to "what times itself gives twenty five?" and the
#               tutor said "That is correct", then taught on using 5. Two failures: the
#               affirmation was untrue (a length is never negative) and the reply used a
#               number the student never gave. mathcheck cannot see it -- every number in
#               that reply is arithmetically sound. answer_sign_conflict needs all three:
#               an explicitly signed student answer, an affirmation, and the unsigned
#               magnitude used WITHOUT the sign ever being mentioned. 14 cases both ways;
#               0 false alarms on 1,015 canonical scripts x 7 signed utterances. Two bugs
#               in its own patterns were found by running the real exchange rather than
#               trusting them: a lookahead that rejected "5." at a sentence end, and a bare
#               "exactly"/"correct" that matched ordinary prose ("exactly one output").
#   2026-08-16  BUILD gn -- THE UNIT-CLAIM REFEREE (rule 0's recap clause), the FOURTEENTH,
#               and the first that judges a reply against a fact from OUTSIDE it. Jim read
#               his rail saying Unit 1 under an opener saying Unit 5 and asked which was
#               broken. The RAIL was right: Maya's record says "New to this course... start
#               at the beginning", nothing was mastered, and the next quiz was a Unit 1
#               topic -- "Two days ago we started Unit 5: Right Triangles" was invented,
#               two-day shared past and all. A child cannot correct a grown-up's memory;
#               told they spent a lesson on the Pythagorean theorem, they conclude they
#               forgot it. _lesson_unit() derives the unit from exactly the two inputs
#               build_system_prompt uses, so prompt and referee cannot drift, and the
#               referee stands SILENT when neither input says. 9 cases both directions,
#               0 false alarms on 1,015 canonical strings.
#   2026-08-16  BUILD gn -- THE TRIANGLE-LETTER REFEREE (rule 63(d), born ENFORCED), the
#               THIRTEENTH. Jim, from one live Geometry lesson: "a, b, and c are supposed
#               to be legs of a right triangle, and instead they're shown as the angles. So
#               when you say a squared plus b squared equals c squared, it makes no sense."
#               v= letters the CORNERS and sides= letters the SIDES, so a tag reading
#               v="A,B,C" sides="3,?,4" leaves nothing on the picture called a, b or c --
#               and with the right angle at A the convention makes side a the HYPOTENUSE,
#               the exact opposite of what the board said. Sibling of triangle_side_conflict
#               (fe): same tag, same AB/BC/CA contract, wired immediately after it. Proved
#               in both directions on 8 cases, silent on all 1,015 canonical foundation
#               strings and on every existing 63c case.
#   2026-08-16  BUILD gm -- NEVER CREDIT A METHOD THE STUDENT DID NOT SHOW (twelfth referee).
#               Rule 43 already said this, in these words, written from a live catch on
#               2026-08-13 -- and on 2026-08-16 the audits caught it again: the student typed
#               "1 1/2. Next." and the tutor replied "that regrouping is exactly the move
#               that trips people up, and you nailed it clean." A rule written from a real
#               incident that fails again the same month is a wish, not a rule; this is the
#               enforcement. Narrow: it fires only when the student showed NO working AND the
#               reply claims a NAMED procedure. Praising the answer is untouched, and a reply
#               that ASKS "how did you get that?" is never flagged.
#   2026-08-16  BUILD gl -- THE TUTOR MAY NOT BE SEEN CHANGING ITS MIND (eleventh referee).
#               The one HIGH finding of the 2026-08-16 audits: "3/4 is smaller than 3/4...
#               wait, let's just confirm..." -- a false comparison, then the grown-up
#               visibly losing faith in their own sentence, all shipped to a child. The
#               ACCURACY block always said "fix it BEFORE you say it"; nothing checked that
#               the fixing happened in PRIVATE. Every course now also says "fix it SILENTLY"
#               and this referee enforces it. Narrow on purpose: correcting the STUDENT is
#               the job ("actually comes out to 3.45" passes); only the tutor retracting
#               itself is caught.
#   2026-08-16  BUILD gk -- A FRACTION IS ONLY "READ ALOUD" WHEN ITS HALVES ARE SAID
#               TOGETHER. _pq_spoken_covers looked for the numerator anywhere and the
#               denominator anywhere, independently, so the 2026-08-16 fractions audit
#               walked through rule 44 untouched: board "3/4 + 1/4 = ?", words "three plus
#               one really is four" -- about the NUMERATORS, never reading the problem --
#               and the referee scored it as spoken because a "three" and a "four" existed
#               somewhere. A confused nine-year-old was then asked a question they had only
#               ever seen written. Now the two halves must be adjacent ("three fourths",
#               "three over four", or the literal 3/4), which is the only form a listening
#               student actually hears.
#   2026-08-14  BUILD gj -- RULE 41 IS NOW A REFEREE (the tenth check). The 2026-08-16
#               lesson audits found FOUR figures drawn with no caption -- a fractions pie
#               and three cookie pictures -- in the two lessons aimed at the youngest and
#               most confused students. Rule 41 is written absolutely ("use it, every
#               time") and nothing enforced it. This is the cheapest referee there is: no
#               model call to detect, no judgement, no argument -- a figure either carries
#               a caption or it does not. All 306 canonical scripts already pass, so it
#               never fights authored content; it only catches what the model improvises.
#   2026-08-14  BUILD gf -- FILTERING IS NOT OPTIONAL (ruletests caught it). Build gb filters
#               the foundation block to the lesson's unit, but when NO unit could be
#               determined -- an unplaced student, or a practice problem the classifier
#               cannot place -- it filtered nothing, and algebra2 came out at 185,595
#               characters against the 180,000 ceiling. Every gb measurement passed an
#               explicit unit, so every gb measurement missed it. There is now a fallback:
#               a student with no placement is at the START of the course, so unit 1;
#               practice and topic prefer the student's own placed unit first.
#   2026-08-14  BUILD gd -- THE MISSING-MARK PROBE (measurement only, no behaviour change).
#               [[mark]] records that a student FINISHED a problem: their score, their
#               accuracy, and since build fy the signal that folds the finished problem off
#               the board. The prompt calls it REQUIRED in all ten courses and ruletests
#               checks that the PROMPT SAYS SO -- but nothing has ever checked that the tutor
#               emits one. Jim's 2026-08-14 Render log: an Algebra I lesson posted /api/mark
#               three times; a Geometry lesson posted it ZERO times after handing the student
#               "130 + ? = 180", hearing "fifty", and answering "exactly right".
#               This prints [markcheck] when the previous turn left a pending "?" line, the
#               student answered, and this reply settles it while recording neither [[mark]]
#               nor [[nice]]. It does NOT regenerate and does NOT award the mark itself -- a
#               net that guessed would inflate a child's recorded accuracy, and retired
#               ensure_board is the standing lesson about nets that guess. Measure first.
#   2026-08-14  BUILD gb -- THE FOUNDATION BLOCK IS NOW FILTERED TO THE LESSON'S UNIT.
#               _foundation_block() gains unit= and passes it to foundations.prompt_block;
#               build_system_prompt hands it the unit it already computed for the playbook,
#               and the practice/topic builders hand it the unit they classify from the
#               problem/topic text. Scripts from other units are NAMED, not quoted. This is
#               what makes room for the ~120 foundation terms still owed on the other nine
#               courses. Backward compatible in both directions: unit=None filters nothing,
#               and an older foundations.py without the argument falls through the existing
#               TypeError path and teaches unfiltered.
#   2026-08-13  BUILD fe -- THE TRIANGLE-SLOT REFEREE (rule 63c, born ENFORCED). From
#               the 2026-08-13 lesson audit's HIGH geometry finding: sides="6,?,10"
#               with right="C" puts 6 in the hypotenuse's slot (sides= is AB, BC, CA;
#               the hypotenuse skips the right-angle vertex, so right="C" -> AB, the
#               FIRST slot) while the words said the hypotenuse was 10. Three of four
#               triangles in one lesson were mis-slotted. New triangle_side_conflict()
#               fires only on the geometric impossibility -- a numeric hypotenuse slot
#               with some other numeric side >= it -- and joins the prose_board_conflict
#               sweep after board_notation_conflict. "?" hypotenuses, algebraic sides,
#               and right= values that name no vertex are never judged (fail open,
#               like every referee). ruletests: TRIANGLE_CASES in PART 2 + PART 3ah.
#   2026-08-12  BUILD eq -- TWO MECHANICAL GUARDS from the 2026-08-12 audits.
#               (1) NEW malformed_tag_conflict, and it runs FIRST in the sweep: nothing
#               in eight referees checked whether a tag was even well-formed. The audit
#               caught [[choices options="yes, let's go! | show me one more]] -- no
#               closing quote -- which the page renders as ONE answer button reading
#               '"yes,' with the second choice simply absent. Silent, student-visible
#               breakage with no guard. Fires only on provable damage: unbalanced
#               quotes, an unterminated attribute, or a tag never closed.
#               (2) prose_unspoken_problem_conflict (rule 44) had TWO blind spots that
#               six findings in five lessons walked straight through. It required TWO
#               numeric tokens, and a fraction counts as ONE by design -- so an entire
#               quiz of "8/12 = ?" and "6/9 = ?" was invisible to it while the tutor
#               said only "what's this fraction reduced to lowest terms?". And ANY
#               number anywhere in the prose exempted the whole reply, so "two numbers
#               that multiply to 10 and add to 7" excused never reading the equation
#               aloud. Now: ONE stated quantity is enough to be worth reading, the line
#               must actually pose something (an operator or a fraction, not a label),
#               and the test is whether the words carry THIS problem's numbers --
#               numerals or the words a person says, with "eight twelfths" counting for
#               both halves of 8/12. Verified against the real audit lines: the three
#               caught, the innocent ones untouched.
#   2026-08-11  BUILD do -- THE WORDS MOVED TO prompts.py. This file had grown to
#               539 KB and two thirds of it was TEXT, not code: the eleven course/mode
#               system-prompt templates, GROUND_RULES, the shared teaching-rules block
#               (GRAPH_TOOL_NOTE), the session/progress/final-exam overlays, the
#               per-course practice+topic scopes, and the two assessment voices. All
#               of it now lives in prompts.py, moved VERBATIM (extracted by line
#               range, never retyped) and PROVEN byte-identical: 52 built prompts --
#               every course x lesson/first-meeting/practice/topic, plus final
#               prep/exam, focus-unit, and the standalone constants -- hashed before
#               and after the split, 52 of 52 equal. Nothing the model reads changed
#               by one byte. This file keeps the ENGINE: API calls, the negotiated
#               continuation, mathcheck, the nine-referee prose sweep, and the
#               build_* functions that assemble prompts.py's text per request. The
#               import (just below the model constants) re-exports every moved name,
#               so tutor.<NAME> works exactly as before. WHERE TO EDIT NOW: the
#               WORDS (rules, templates, scopes) -> prompts.py; the MACHINERY
#               (referees, pipeline, builders) -> here. BOARD_TAG_SYSTEM stayed: it
#               belongs to the (parked) whiteboard safety net beside its own code.
#               The change notes BELOW this line predate the split -- where an old
#               note says a rule or template text lives "in this file", read
#               prompts.py; the history itself is untouched.
#   2026-08-11  BUILD dl -- THE TWO STRONGEST REMAINING EVIDENCE GAPS, CLOSED AS RULES
#               (Teaching_Evidence_Base gaps 2 and 3, both WWC Strong; the Forward
#               Plan's queue item 3).
#               NEW RULE 53 -- THE NUMBER LINE IS A TOOL YOU USE ON PURPOSE: magnitude
#               and comparison (two numbers on one line settles size arguments),
#               fractions introduced BETWEEN 0 and 1 against the 0 / 1/2 / 1
#               benchmarks and then deliberately extended past 1, equivalent fractions
#               (and the decimal and percent costumes of the same value) at ONE
#               position with their names in the caption. Written against what
#               [[numberline]] can actually draw today (points, open circles, ineq --
#               no point labels), so the rule never asks for an undrawable picture.
#               NEW RULE 54 -- A WORD PROBLEM HAS A TYPE: name it (Change, Equal
#               Groups, Compare; part-whole/rate/proportion upstairs) BEFORE any
#               arithmetic, schema on the board, the equation comes FROM the schema.
#               54(b) BANS teaching key-word rules -- the WWC guide's own warning --
#               and is ENFORCED from day one: board_notation_conflict also catches
#               "altogether always means add" (prose or board), with the vocabulary
#               distinction honoured: "sum means add" is a DEFINITION (rule 37), not a
#               shortcut; the banned list is story-cue words only.
#   2026-08-11  BUILD dk -- BATCH E: the audit RE-RUN's six small accuracy fixes
#               (Audit_Findings_2026-08-11.md, PART 9; the re-run scored 30->17
#               findings, 10->2 high, 6->0 stumbles -- these close most of what
#               remained). In THIS file:
#               - rule 48(e): when the student SAYS a symbol wrongly ("f BRACKET x"),
#                 affirm the idea and hand back the right words in the same breath --
#                 in a voice classroom a wrong reading you let stand is one you taught;
#               - rule 52(d): a request to COMPUTE is not a rule-52 question -- coach
#                 the work as always; rule 52 is about questions ABOUT the mathematics
#                 (the critic misapplied our own new rule; now neither model nor critic
#                 can);
#               - NEW deterministic referee board_notation_conflict (EIGHTH check in
#                 prose_board_conflict): "$50 + 10% = $55" (a bare percent added to a
#                 plain quantity and COMPLETED -- invisible to mathcheck, $ and % are
#                 not sympy) and "a^2 + 64 = 100 = ?" (a chained equals ending in "= ?"
#                 after a bare number). Both quoted from real re-run boards; the legal
#                 shapes (the "of" form, percent-with-percent, conversions, pending
#                 lines, worked chains ending in a number) are FALSE fixtures. Rule 27
#                 moves COVERED -> ENFORCED for the percent shape.
#               Elsewhere in dk: math-figures.js drops any labeled point sitting on a
#               declared hole; notation.py gains the fraction-slash bridge for the four
#               lower courses ("the number AFTER the slash is the denominator -- the
#               BOTTOM number when written stacked").
#   2026-08-11  BUILD di -- BATCH D: the board tools the audit proved missing. The
#               shared block gains ONE tool note (reaches all ten courses; PART 3r
#               checks it): [[graph]] pieces may carry a domain with "for"
#               (func="x+1 for x<2; x+4 for x>=2") -- clipped, with the boundary marked
#               automatically, OPEN circle for strict, CLOSED dot for inclusive (S-4:
#               the audit's jump was two full parallel lines under a caption claiming a
#               jump); and [[column align="last"]] draws the DELIBERATELY-WRONG
#               last-digit lineup, amber + badged, for contrast teaching (S-9) -- never
#               with result=, always followed by the correct lineup. Renderer work in
#               math-figures.js and the three teaching pages; prompt cost ~1.4k chars.
#   2026-08-11  BUILD dh -- THE AUDIT'S TEACHING FINDINGS BECOME RULES AND REFEREES
#               (Batches B + C of Audit_Findings_2026-08-11.md; build dg was Batch A).
#               PROMPT (shared block, all ten courses; budget checked):
#                 rule 13 gains THE FALSE-CRITERION TRAP (S-11/S-3: "a different number
#                   pops out", "denominator zero so there's a hole" -- an example
#                   hardened into a wrong definition);
#                 rule 14: a figure's OWN labels are notation too (S-12, the [[machine]]
#                   box showing 2x+1 to a nine-year-old);
#                 rule 15: "= ?" is never a missing right-hand side -- an equation to
#                   solve is written "= 0" whole (S-16);
#                 rule 17: THE BOARD IS PART OF THE SAME BREATH -- never ask what a board
#                   line already answers (S-2);
#                 rule 18(a): "close" is a measurement, not a comfort (S-7);
#                 rule 43: never credit work that did not happen (S-15);
#                 rule 47(d): the instrument is part of the honesty -- "Unit Quiz" may
#                   only introduce the ten-question unit-wide instrument (S-10);
#                 rule 51(e): UNDEFINED IS NOT YET A HOLE -- classify only after the
#                   cancellation or the blow-up is shown (S-3);
#                 NEW RULE 52: a direct mathematical question is answered before
#                   anything else happens (S-5 -- the ignored "is that because it
#                   simplifies to x + 2?" conjecture).
#               REFEREES (both NARROW, both fail open, both swept clean against all 186
#               foundation scripts and all 227 demo lines before ship):
#                 prose_answered_question_conflict -- rule 17 COVERED -> ENFORCED: the
#                   prose asks "what's A op B?" while a board tag in the SAME reply
#                   states A op B = C with numeric C (commutativity honoured; a pending
#                   "= ?" line never trips it; offers excluded the build-dg way);
#                 prose_unspoken_problem_conflict -- rule 44 COVERED -> ENFORCED: a
#                   pending or Q-numbered board problem carrying two or more numbers
#                   while the ENTIRE spoken prose asks its question with no number in
#                   any spelling (one spoken number anywhere = silent, by design).
#               prose_board_conflict is now SEVEN checks. Tiers after dh:
#               16 enforced · 10 exercised · 25 covered · 1 unverified.
#   2026-08-11  BUILD dg -- RELIABILITY: THE AUDIT'S STUMBLES WERE OURS, NOT RATE LIMITS.
#               The first full audit's Render logs (Audit_Findings_2026-08-11.md, PART 5)
#               named the mechanisms; all are fixed here.
#               (1) THE REFEREE CRIED WOLF. prose_pending_question_conflict counted the
#               pronoun "one" as a number ("Want to try ONE yourself, or see ONE more
#               worked example?" read as two-number arithmetic) and had no concept of an
#               OFFER, so it killed good drafts a dozen times in forty minutes of audit
#               traffic -- and one geometry lesson shipped WITHOUT its worked example
#               because the drafts that contained it kept being discarded, and the third
#               draft wrote as if the student had seen them. Offers and look-questions
#               are now excluded (both rule-15 and rule-39(b) referees), "one" counts as
#               a number only in arithmetic company, the sentence splitter no longer
#               merges a quote-ended sentence into the question after it, and every
#               misfire quoted in the logs is a permanent ruletests case.
#               (2) BOTH REGENERATION NUDGES now order the rewrite to STAND ALONE -- a
#               regenerated draft must re-carry everything the student needs (worked
#               example, definition, board lines) and never pick up mid-thought from a
#               draft the student never saw.
#               (3) _create_full: claude-sonnet-5 intermittently REJECTS assistant-prefill
#               continuation (400: "does not support assistant message prefill"), and
#               each rejection surfaced as a stumble the student watches. Continuation is
#               now NEGOTIATED like the build-cz token parameter: prefill first, and on
#               that named 400 a user-message continuation nudge, remembered for the rest
#               of the process. Ceiling 1600 -> 3000 (MAX_REPLY_TOKENS): the logs show
#               tag-heavy teaching turns hitting 1600 constantly, and five replies
#               shipped as admitted "stitched partials" in forty minutes. A ceiling is
#               not a target -- normal turns end far under it and cost nothing extra.
#               (4) _create_verified retries ONCE, silently, on an empty reply before the
#               student ever hears "I lost my train of thought" -- the audit counted that
#               apology 6 times in 10 lessons.
#   2026-08-11  BUILD de -- the DIFFEQ course arc restructured to the CUPM mainstream
#               syllabus (Jim: "the one most acceptable to most schools"). Qualitative
#               analysis and numerical methods become units 3-4; systems get two units;
#               old 6-7 merge; exact equations shrink to a topic; series solutions drop.
#               Only the NINE UNITS block changed -- every teaching rule is untouched.
#   2026-08-10  BUILD cy -- THE FIFTH REFEREE: prose_self_answer_conflict(), and rule
#               39(b) moves from COVERED to ENFORCED.
#               Source: the MAA Instructional Practices Guide (CP.1.2, wait time).
#               Teachers wait under 1.5 seconds before answering their own question; the
#               evidence says wait seven; the first benefit listed is fewer "I don't know"
#               responses -- the exact thing Jim keeps meeting. The guide's vignette is an
#               instructor asking eight questions and answering all eight himself.
#               NARROW, because every false positive costs a real model call. It fires
#               only when the reply asks something ANSWERABLE and then states a number the
#               QUESTION DID NOT ALREADY CONTAIN. That last clause was not in the first
#               version and had to be: sweeping our own 227 demo lines found "two to WHAT
#               power makes thirty-two? Start at two and count how many times you double"
#               -- a HINT restating the question's own number, and never the answer. A
#               referee that cannot tell a hint from an answer punishes good teaching.
#               Swept clean afterwards against all 182 foundation scripts (all of which
#               are shaped "What is a numerator? The numerator is...") and all 227 demo
#               lines. Fails open, like every other referee.
#   2026-08-10  BUILD cv -- RULE 51 (a feature on the board must belong to the function)
#               and the [[graph]] window doc. Jim, reading a limits lesson: "it doesn't
#               say WHY there is no value at x = 2... and it completely ignores the graph
#               that continues to the right after x = 2." Both true. y = x^2 has no hole
#               at 2 -- f(2) = 4 -- so a hole painted onto it is an assertion, and a hole
#               is never an assertion: it is a CONSEQUENCE OF A DEFINITION, nearly always
#               a factor that cancels. 51(c) also fixes the second half: a hole does not
#               end the graph, and an approach must be narrated on BOTH sides.
#               THE WINDOW DOC WAS BROKEN TOO. It said range="-1,5" and the renderer's
#               parseRange only accepted "a..b", so the window was silently discarded --
#               and this doc exists because of Jim's EARLIER catch about a bad window,
#               which means that fix never worked. Doc now leads with "-1..5";
#               math-figures.js accepts both; ruletests checks every range= we write
#               against the renderer's own regex.
#   2026-08-10  BUILD cu -- QUIZ LENGTHS, AND RULE 50 (chase the unfinished unit).
#               Jim: "if I pass an exam with an eighty-five... I can do all the units and
#               still be carrying an eighty-five with me, which is gonna keep me from
#               mastering the final exam."
#               ⭐ THE REAL DEFECT WAS ARITHMETIC. Mastery is 90% and the Unit Quiz asked
#               for FOUR OR FIVE questions, so the only scores it could produce were 80%
#               and 100% -- there is no 85, and the 90% bar silently meant a PERFECT
#               PAPER. Topic quizzes had it too: three or four questions against an 80%
#               bar is four out of four. Nobody wrote that on purpose; the bar moved from
#               80 to 90 on 2026-08-04 in store.py and the question counts stayed here.
#               Unit Quiz -> TEN questions, topic quiz -> FIVE, in all NINE templates
#               (ten courses). The example tags moved with them (correct="9" total="10",
#               correct="4" total="5"). ruletests PART 3k now multiplies the bar by the
#               question count for every quiz in the system and fails if the only passing
#               score is a perfect one.
#               NEW RULE 50 -- AN UNFINISHED UNIT IS YOUR JOB, NOT THEIRS TO REMEMBER.
#               A student may move on with a unit unmastered (Jim's call: momentum
#               matters), so the tutor now raises it ONCE at the start of a session from
#               the "checked but not yet mastered" list, reviews before it re-quizzes
#               (rule 47 still applies), always uses NEW questions, and says out loud that
#               the record keeps their BEST score -- fear of losing a good score is the
#               most common reason a student refuses a retry, and it was never addressed.
#   2026-08-10  BUILD co -- RULES 2 AND 8 ARE NOW ENFORCED, NOT JUST WRITTEN DOWN.
#               Generating the rule index (audit #2 item 23) made something plain that a
#               person reading 49 rules would never notice: rules 2, 5 and 8 were the
#               only ones in the entire prompt that NOTHING checked -- not a referee, not
#               an audit, not even a coverage grep. Two of the three turned out to be the
#               same shape as rule 7 seen from the other side, so the visual referee
#               learned them rather than growing a new one:
#                 rule 2 -- the student ASKED to see something ("show me", "can I see",
#                   "draw it") and the reply puts nothing on the board. There is no
#                   legitimate version of that: re-drawing is free and always right.
#                   prose_visual_conflict() now takes the student's message to see it.
#                 rule 8 -- the tutor SAYS he is about to show or draw something and then
#                   draws nothing. Uses the same deferral guard as the rest of the
#                   referee, so "next time I'll draw you one" is still fine -- the
#                   battery caught that on the first run, because the case was already a
#                   fixture from build ce.
#               _last_user_text() feeds the student's real words in, skipping the SYSTEM
#               nudges the referee itself appends on a retry.
#               Rule 5 (don't narrate symbols) is left honestly UNVERIFIED: judging it
#               needs to know what a reply SOUNDED like, and a bad guess there would
#               re-roll good teaching.
#   2026-08-10  BUILD cm -- PER-TURN NOTES RIDE WITH THE MESSAGE, NOT THE PROMPT.
#               Found while answering Jim's question about whether prompt size costs
#               money or performance. The system prompt is ONE cached block, so anything
#               written into it MOVES THE CACHE PREFIX and re-bills every token from that
#               point on. Build ck appended the misconception hint into the prompt (via
#               mastery_note), 63,629 characters in -- so every turn a hint fired threw
#               away roughly 15,000 tokens of cache and paid a cache write on top, to
#               deliver about 195 tokens of actual note.
#               get_tutor_reply() gained turn_note=, appended to THIS turn's user
#               message where nothing is cached anyway. The note reaches the model
#               exactly as before -- arguably better placed, right beside the answer it
#               is about -- and the system prompt is byte-identical from turn to turn.
#               RULE OF THUMB for anyone adding one: if it changes every turn, it is not
#               a system prompt, it is a message.
#   2026-08-10  BUILD cl -- _foundation_block() gained verbatim=, threaded through the
#               lesson, practice and topic prompts from student["foundations_verbatim"].
#               See foundations.py: a script the student has already heard is OFFERED,
#               not replayed (rule 40), so its wording only needs to be in the prompt on
#               the turn they accept the offer. Defaults to True everywhere; the older
#               two-argument foundations.py still works via the existing TypeError path.
#   2026-08-10  RULE 49 + THE MISCONCEPTION CATALOGUE (build ck, Jim: "I want to
#               pursue the misconception box"). Proactive audit #2 item 2.
#               49 A WRONG ANSWER IS THE OUTPUT OF A RULE -- FIND THE RULE. Rules 20-22
#                  say what to DO about a wrong answer and never say what to work out
#                  first. A student who says 3 + 2 x 4 is twenty is not guessing: they
#                  are evaluating left to right, faithfully, and will do it again next
#                  week. A student who says twenty-one made a slip. Same topic, same
#                  wrongness, OPPOSITE remedies. 49 makes him reconstruct the procedure
#                  from the number, fix the RULE rather than the answer, check the
#                  hypothesis with one question before acting on it, never announce a
#                  diagnosis as a fact about the student (rule 42), and diagnose from
#                  what they actually said when nothing in the catalogue fits.
#               NEW misconceptions.py carries 148 catalogued wrong rules; this file
#               appends the course's catalogue to the lesson, practice and topic
#               prompts (TELL + RULE + FIX -- the ready-made wording is delivered
#               just-in-time by main.py instead, so the prompt is not paying for 146
#               sets of words that will not come up this turn). Defensive import.
#   2026-08-09  THE SYMBOL TABLE REACHES THE TUTOR (build cj). Jim: "it looks like
#               we've fixed the function notation, but math is filled with these kinds
#               of things. How can we make sure that every one of these is caught all
#               of the time?"
#               Rule 48 (build ci) told him to read every symbol aloud and to deny the
#               wrong reading BY NAME -- and never told him our readings. That is the
#               same mistake as rule 40 before foundation memory: a rule the model has
#               no data to obey. NEW notation.py registers all 28 families once, and
#               _notation_block(course) appends a compact "HOW TO SAY WHAT YOU WRITE"
#               table to the lesson, practice AND topic prompts, listing only the
#               symbols that course actually uses, each with the words to say and the
#               wrong reading to deny. Defensive import, like foundations.
#   2026-08-09  RULE 48 -- TEACH THEM HOW TO *SAY* THE SYMBOL (build ci, Jim's live
#               Algebra I session: "it's never been clearly stated to me what f of x is,
#               how to say f of x... and then it flipped over to g of x").
#               Rule 14 has always said "define every notation the first time it
#               appears". That is only half a rule, and the missing half is the half that
#               failed here. A student who cannot SAY a symbol cannot ask a question
#               about it, cannot answer one out loud in a voice classroom, and quietly
#               stops trying. So 48 requires: (a) say the words a person says, and put
#               the written form up in the same breath, so the sound and the shape arrive
#               together; (b) deny the wrong reading BY NAME -- f of x is NOT f times x,
#               because that guess is predictable and naming it is what prevents it;
#               (c) a letter is a NAME, not a new idea -- when f becomes g, say so, or a
#               student who was following perfectly assumes a new concept nobody taught
#               them; (d) the first time is not the only time, and f of x, f of g of x and
#               f prime of x each get their own first time.
#               The five canonical scripts that carry this live in foundations.py.
#   2026-08-09  RULES 45-47 + THE SCORE REFEREE (build ch, audit #2 items 9/10/11).
#               45 THE TALLY IS ARITHMETIC, NOT JUDGMENT -- report the exact count, never
#                  round up, never "basically", never award mastery out of sympathy, and
#                  the only percentage you may state as the SCORE is the one the tally
#                  gives (naming the bar itself is fine). Warmth belongs in HOW you
#                  deliver the number; rule 35 already says how. 45(d) spells out why it
#                  is not negotiable: a score nudged once becomes a mastered unit, a
#                  green bar, and a line in a record a parent may have to defend.
#               46 A QUIZ QUESTION TESTS ONE SKILL -- name the topic before question one,
#                  and keep the supporting arithmetic at or below what they have already
#                  mastered. A question that needs the new skill AND long division fails
#                  a student who has the new skill, and nobody outside can tell.
#               47 NO COLD QUIZZES -- two unaided correct on this topic, this session,
#                  before any quiz is offered. Rule 35 already required exactly that
#                  before a RETAKE; it should always have been true the first time.
#               ⭐ prose_score_conflict() -- the FOURTH check in prose_board_conflict().
#               The server has always recomputed the percentage from correct/total, so no
#               number the model asserts is ever STORED. Nothing checked what the student
#               HEARS: the tag can read 3 of 5 while the sentence beside it says "you
#               passed!". Same shape as the 2026-08-08 dimes contradiction, except this
#               one lands on the progress bars. Now caught and silently rewritten.
#               Thresholds are mirrored here as QUIZ_PASS_PCT / UNIT_PASS_PCT /
#               FINAL_PASS_PCT (tutor.py must not import the storage layer) and
#               ruletests.py asserts they never drift from store.py's.
#               THREE false positives were caught by the battery before shipping: the
#               "%" regex had a trailing \b so it never matched "80% — great!" at all and
#               the whole percentage check was silently dead; quoting the bar ("you need
#               80% to pass") had to stay legal; and in a percents lesson "what is 25% of
#               80?" is the PROBLEM, not a score claim, so a percentage now only counts
#               when its sentence is actually reporting the result.
#   2026-08-09  THE PENDING-QUESTION REFEREE + AN HONEST TODAY-BAR NET (build cg).
#               Jim: "it gave me a problem without putting it on the board, and this is
#               the exact example that we've already used once before that was supposedly
#               fixed. And I don't understand why it's not fixed."
#               He is right to be annoyed. Rule 15 does not just forbid this in general --
#               it NAMES this exact column-addition scenario, quotes it, and prints the
#               exact fix ([[step eq="dollars: 2 + 1 + 1 = ?"]]). It has said so since
#               build bm, and the reply still went out with the question spoken and the
#               board empty. That is the difference between a rule the model is TOLD and
#               a rule the machine ENFORCES, and this one has now changed sides:
#               prose_pending_question_conflict() is the third check inside
#               prose_board_conflict(). If a sentence asks the student to COMPUTE
#               something -- two or more numbers, or an operator word and a number, or a
#               written expression -- and the reply emits no board tag containing a "?",
#               the draft is discarded and silently rewritten, exactly like a failed math
#               check. Narrow by design (a re-roll is a real model call): number WORDS
#               count because he speaks in words; a bare "-" or "/" does not count as an
#               operator ("three-fourths", "1/2" are single values -- both caught by the
#               test battery on its first two runs); and rule 39(d)'s constant
#               "does that click, or should I show it another way?" never triggers it.
#               ALSO: ensure_today_tag() gained today_live=. Its history guard used to
#               read "a [[today]] was emitted earlier, so a bar is up -- don't reset it."
#               True inside one sitting; FALSE across a page load, which is precisely
#               where Jim kept losing the bar. It now stands down only when the SERVER
#               confirms the bar really exists (main.py passes student["today_live"]).
#   2026-08-09  RULES 41-44 (build cf, proactive audit #2 "do first").
#               41 EVERY PICTURE CARRIES A CAPTION THAT SAYS WHAT TO NOTICE -- and it
#                  captions the POINT, not the object: "both are four steps from zero",
#                  never "a number line". A caption-less figure hands the student back
#                  the one job the picture was supposed to do for them. ruletests.py
#                  PART 3c now enforces this on our own 64 foundation figures (10 of them
#                  had no caption and now do).
#               42 NEVER COMPARE THIS STUDENT TO ANYONE BUT THIS STUDENT -- not to
#                  classmates, siblings, "most kids", or a grade level. It slips out as
#                  kindness: "most kids find this hard" is meant as comfort and lands as
#                  a measurement against a room the child cannot see. The only comparison
#                  allowed is to their OWN earlier work, which our progress data actually
#                  supports. No invented percentiles or grade equivalents, ever.
#               43 YOU PERCEIVE EXACTLY TWO THINGS -- what they typed or said, and what
#                  you put on the board. Never "I can see you're working hard", never
#                  "you sound tired". Warm, ordinary teacher sentences, every one of them
#                  a false claim about watching a child: unsettling to a student who half
#                  believes there is a person here, alarming to a parent reading the
#                  transcript, and untrue, which is reason enough (rule 13).
#               44 READ THE PROBLEM ALOUD, IN FULL, EVERY TIME -- rule 15 got it onto the
#                  screen; this gets it into the student's ears. Some of our students are
#                  seven, some are dyslexic, some are listening with the screen off to
#                  one side; a problem that exists only as text is one they cannot
#                  attempt, and their silence would look like a math failure in every
#                  number we report about them.
#               ALSO: build_practice_prompt() and build_topic_prompt() now append
#               _foundation_block() with the student's heard list, exactly like the
#               lesson prompt. Found while auditing audit #1: those two modes carried
#               rules 36-40 but not the scripts the rules refer to.
#   2026-08-09  RULES 39 + 40 AND THE VISUAL REFEREE (build ce, Jim's three items).
#               RULE 39 -- TALK LESS, CHECK IN OFTEN, AND MAKE THE CHECK FAILABLE.
#               Jim: "we need to have a cap on how long we talk to an eight year old.
#               I think you need to check in with them every now and then." There was no
#               length rule anywhere in the prompt. In a voice product that is the fastest
#               way to lose a young student, and you cannot see them drift. 39(a) caps a
#               turn at ~90 spoken words, ~60 for the elementary courses and any student
#               around ten or younger, with exactly two exceptions (a canonical foundation
#               script, and the rule-0 opening message). 39(b) one question per turn, last.
#               39(c) check in at every new idea and never more than ~3 turns without one.
#               39(d) is the part that matters: "does that make sense?", "got it?", "any
#               questions?" and "okay?" asked ALONE are BANNED. Every student says yes to
#               those and a confused child says yes fastest, because saying no to a teacher
#               costs them something -- a check that cannot fail is worse than no check,
#               because it buys false confidence. He must always hand them an easy way out
#               in the same breath ("…or should I show it a different way?") or ask for
#               CONTENT, which a yes cannot fake. 39(e) thank a student who says they are
#               lost. NOTE this does NOT contradict audit #2 item 3: Jim asked for more
#               check-ins and the audit asked for better ones; 39 is both.
#               RULE 40 -- ASK BEFORE YOU REPEAT AN INTRODUCTION. Jim: "a loyal student can
#               re-hear it… we should just query him and say, do you think you got it, or
#               do you want me to refresh your memory?" Exactly that: name the term in one
#               sentence, ask, and STOP. If they want it, speak the canonical script WORD
#               FOR WORD (same words = same lesson, and the audio is already paid for). If
#               they say they have it, believe them -- but if a problem then goes wrong
#               because of that term, give the script anyway and never as "you said you
#               knew it". 40(e): the youngest students are poor judges of their own memory,
#               so for Entry-Level and Basic Math he asks ONE small concrete question about
#               the term instead and lets the answer decide. 40(f): he ends any reply that
#               delivered an introduction with [[learned term="..."]] -- invisible to the
#               student, and the only way the system remembers next month.
#               _foundation_block()/build_system_prompt now pass the student's heard list
#               through to foundations.prompt_block(); an older foundations.py without the
#               second argument still works (TypeError -> retry).
#               ⭐ THE VISUAL REFEREE -- prose_visual_conflict(), now the FIRST half of
#               prose_board_conflict(). Jim: "you can't say one thing and then have the
#               numbers say something different." The numeric half has done that since bu;
#               nothing has ever checked the OTHER way a reply lies about the board. Rule 7
#               has forbidden describing an undrawn picture since ao -- in words only. A
#               reply that says "here's a number line" and emits no [[numberline]] passed
#               mathcheck (tags only) and passed the prose referee (numbers only), and the
#               student sat in front of a blank board. That is exactly the demo failure Jim
#               called "we got one shot to do it right, and it failed". Now it is caught and
#               silently regenerated like any other referee finding.
#               Deliberately narrow, because every false positive costs a real model call:
#               it fires only when ONE SENTENCE both names something this board can draw
#               and claims in the present tense that it is appearing now. Bare "triangle"
#               and "circle" are excluded (too common in ordinary prose), and a sentence
#               that DEFERS ("next time I'll draw one"), OFFERS ("want me to draw it?") or
#               looks BACK ("remember the number line we used yesterday?") is not a claim.
#               A second, weaker check covers "look at the board" when the reply writes
#               nothing at all. FIGURE_TAGS is a constant here (tutor.py must not read the
#               static files at request time) and ruletests.py PART 3c proves it has not
#               drifted from session.html's handleTags(). Fails open, always.
#   2026-08-09  ★ FOUNDATION FIRST -- RULES 36-38 (build cc, Jim). "Socratic" was the
#               wrong description of what a math classroom should do, and it showed:
#               students met fractions without being told what a fraction, a numerator
#               or a denominator IS. Rule 36 teach the thing before you ask about it
#               (name it, name every part, define, worked example, check the IDEA, THEN
#               questions) · rule 37 vocabulary is taught, never assumed · rule 38
#               concrete -> picture -> symbols with I-do/we-do/you-do and guidance that
#               fades only as competence grows. All per-course "Socratic, one-step-at-a-
#               time" wording replaced with "foundation-first"; rules 36-38 explicitly
#               override anything older. New foundations.py supplies 24 CANONICAL
#               scripts spoken VERBATIM (also a cost win -- the TTS cache is keyed by
#               text, so a verbatim script renders once for the platform, ever).
#   2026-08-09  RULE 35 -- FIX, THEN RETRY (build cb, Jim asked directly: "if a student
#               fails a quiz, do we give the quiz immediately again, or make them review
#               what they had trouble with first?"). The old wording only said to
#               "re-teach the gaps, then offer a fresh quiz when they're ready", which
#               permits an instant retake. Now explicit and shared across all ten
#               courses: name the win first · diagnose the ONE or TWO skills under the
#               misses · re-teach each with a worked example (rule 19) · require TWO
#               UNAIDED correct problems on that skill before a retake is offered ·
#               fresh questions, never the same items · a second failure steps BACK to
#               the prerequisite rather than looping a third time · never say the
#               student "failed" -- the quiz hasn't passed YET.
#   2026-08-09  THE PROACTIVE RULES + THE PROSE REFEREE (build bu, Jim: "implement the
#               proactive rules as you see fit" -- from claude/Proactive_Rules_Audit_
#               2026-08-08.md, 25 rules written BEFORE a student finds them).
#               NEW SHARED RULES 20-34 (all verified in all ten course prompts):
#                 20 partially-right is not wrong · 21 "I don't know" earns a SMALLER
#                 step, never a repeat · 22 the escalation ladder (never ask the same
#                 way twice; miss 3 = work it together) · 23 equivalent answers are
#                 correct · 24 self-corrections / leaps / "just tell me" · 25 when the
#                 student says YOU are wrong · 26 a wrong board line is corrected on
#                 the board + [[clear]] discipline + short lines · 27 units on final
#                 answers, "≈" for estimates · 28 one name per thing · 29 how a session
#                 ENDS (+ long-session check-in) · 30 off-topic/personal questions
#                 (never claim to be human) · 31 ⚠️ when something bigger than math
#                 shows up (self-criticism / personal info / harm) -- QUEUED FOR
#                 COUNSEL · 32 story problems survive a sanity check · 33 difficulty
#                 moves one notch · 34 keep old skills sharp (spaced review).
#               SPEECH: number-words bullet added to all ELEVEN "HOW YOU SPEAK" blocks
#               (negative VALUES are "negative", percents, ratios, mixed numbers, big
#               numbers whole); transcription charity now states that spoken number
#               words ("twelve hundred", "a half") ARE exact answers.
#               ⭐ THE PROSE REFEREE (audit #24) -- prose_board_conflict() + wiring into
#               _create_verified. mathcheck sees only TAGS; this catches the shipped
#               2026-08-08 bug where the spoken words adopted the student's wrong
#               "fifteen" while the board correctly wrote 16. Deliberately NARROW (a
#               false positive throws away a good reply): flags only when a labeled
#               board conclusion is contradicted by the spoken words AND the words
#               never once say the board's number. Fails OPEN everywhere; a flagged
#               draft is silently regenerated (the student never sees it) and, if it
#               cannot be resolved, passes through rather than bricking the lesson.
#               Companion: ruletests.py (audit #25) -- the regression battery.
#   2026-08-08  RULE 19 -- WORKED EXAMPLE FIRST (build bs, Jim: "start every new topic
#               with a complete worked example before the student tries one -- more
#               teaching, not 100% teaching-by-doing"). New rule 19 in the SHARED
#               precision block: (a) one complete example worked BY THE TUTOR on the
#               board, every step + the answer, narrating the why (rule 6 explicitly
#               does not apply to the tutor's own example -- collision noted so it
#               can't cause step-skipping); (b) demo may span 2-3 short turns ending
#               in continue-checks, never computation questions; (c) then "you try
#               one" -- similar problem, at/below the example, "?"-line style, with
#               the worked example LEFT on the board until their first success;
#               (d) fires on new topics and re-teaching after struggle, not every
#               problem. 10-course scan verified.
#   2026-08-08  RESUME BARS + THE "?" LINE (build br, Jim's resumed-session screenshot).
#               (1) PROGRESS_TAGS_NOTE: [[today items]] is now required in the FIRST
#               message of EVERY session -- resumed sessions included (a welcome-back
#               opener dove straight into the problem and the today bar stayed empty).
#               Companion: session.html now renders the UNIT bar at page load from
#               curriculum + placement + server quiz history (like the course bar), so
#               it no longer depends on the model's [[unitplan]] tag at all.
#               (2) Rule 15 gains the concrete device for asked steps: write the step
#               as a PENDING "?" line -- [[step eq="dollars: 2 + 1 + 1 = ?"]] -- in the
#               same reply as the question; next reply replaces "?" with the confirmed
#               number. (Second miss of the same kind in one lesson: the dollars-column
#               question was spoken with no board line.)
#   2026-08-08  RULE 18 -- CHECK THE STUDENT'S ANSWER (build bq, Jim's screenshot,
#               carrying dimes: asked "seven plus eight plus one?", student said
#               "fifteen" (wrong -- it's 16), and the tutor ACCEPTED it aloud ("write
#               the five and carry a dollar") while its own board correctly wrote
#               dimes: 7 + 8 + 1 = 16 -- spoken lesson and board contradicted each
#               other, and the wrong digit was taught. New rule 18 in the SHARED rules
#               block (all courses, verified by 10-course scan): (a) compute the
#               student's numeric answer YOURSELF before accepting/building on it --
#               a wrong answer is a coaching moment, never adopted; (b) spoken numbers
#               must MATCH the board's numbers in the same reply. Related: the parked
#               "prose referee" decision (mathcheck only checks tagged computations,
#               not prose) -- rule 18 is the prompt-side fix; a mechanical prose check
#               remains open in Teaching_Precision_Review_2026-08-06.
#   2026-08-08  MONEY IS SPOKEN AS MONEY + ALL-COURSE RULE COVERAGE (build bp, Jim:
#               "$1.85" was voiced "one dot eight five -- no dollar, no cents").
#               (1) New bullet in EVERY "HOW YOU SPEAK" block (each course template has
#               its own -- 11 total): prices are spoken "one dollar and eighty-five
#               cents", plain decimals "three point seven five"; the board keeps the
#               symbols. Client twin in forSpeech() on all three teaching pages.
#               (2) COVERAGE AUDIT: the bk MULTIPLICATION SIGN bullet had landed in a
#               course-specific whiteboard block and reached only 3 of 10 courses --
#               MOVED into the shared "BOARD LEADS" section (rule 4 area). Verified:
#               ×-rule, money rule, and all recent rule sharpenings now present in the
#               built prompts of ALL TEN courses. LESSON LEARNED for future edits:
#               "HOW YOU SPEAK" and the whiteboard tag docs are PER-COURSE (11 copies);
#               shared blocks are GRAPH_TOOL_NOTE (rules 1-17), SESSION_OPENER_RULES,
#               and PROGRESS_TAGS_NOTE -- put universal rules THERE, then verify with a
#               10-course build_system_prompt scan.
#   2026-08-08  TODAY-BAR NET + FINAL-STEP LINE (build bo, Jim's Pre-Algebra screenshots).
#               (1) TODAY bar never rendered: the opener skipped [[today items]]. Fixes:
#               rule 0(c) now explicitly requires the [[today]] tag right after the goals
#               card, AND new ensure_today_tag() -- a DETERMINISTIC net (never guesses,
#               unlike the retired ensure_board): if a lesson reply announces goals (card
#               or [[goal]] banner) with no [[today]] in the reply or session history, it
#               appends [[today]] with the model's own goal items verbatim. Lesson only.
#               (2) Column-addition finale skipped its board line ("dollars: 2 + 1 = 3"
#               never written; board jumped to 2.30 + 1.45 = 3.75): rule 4 sharpened --
#               every answered sub-step gets its own line BEFORE any combined line.
#   2026-08-08  NO MORE TRUNCATED TURNS (build bn, Jim's live freeze: a first Basic-Math
#               teaching turn collapsed to the single word "Let" with an empty board --
#               the tag-heavy reply hit the 1200-token max_tokens ceiling MID-TAG and
#               nothing checked stop_reason; the client stripped the dangling tag and
#               the lesson stalled). New _create_full(): every logical turn now checks
#               stop_reason == "max_tokens" and CONTINUES via assistant prefill, stitching
#               the pieces (up to 2 continuations); ceiling raised 1200 -> 1600. All three
#               teaching modes (lesson/practice/topic) flow through it via
#               _create_verified, so one fix covers them all.
#   2026-08-08  RULE 15 SHARPENED -- "YOUR TURN" GOES ON THE BOARD (build bm, Jim's live
#               catch in Pre-Algebra: the tutor worked 3 + 2 × 4 on the board, then asked
#               "your turn -- what's ten minus two times three?" with the NEW problem
#               existing only in the spoken words). Rule 15 now says explicitly: the
#               problem handed to the student is written in symbols ([[step]]/[[write]])
#               in the SAME reply it is asked; only its answer/worked steps stay off the
#               board (never conflicts with rule 6). Additive sharpening only.
#   2026-08-07  MULTIPLICATION SIGN RULE (build bk, Jim's screenshot: "3 + 2 X 4" showed
#               a red variable X). New bullet in the whiteboard section: write
#               multiplication as × (or ·), NEVER the letter x -- the board styles every
#               lone letter as a variable. Client-side safety net shipped in the same
#               build (styleVarsCore on all three teaching pages).
#   2026-08-07  RULE 16 SHARPENED (build bh, Jim's second live catch on it: the reply wrote
#               the SUBSTITUTED check line but still said "plug five back into the original
#               equation on the board" while 5x-3=2x+12 had scrolled away). Rule 16 now
#               explicitly requires re-writing THE ORIGINAL EQUATION ITSELF, labeled, above
#               the check line -- and bans speaking "the original equation" unless this
#               reply shows it. Additive sharpening only.
#   2026-08-07  RULE 17 -- NEVER ANSWER YOUR OWN QUESTION (build az, Jim's live catch in
#               Basic Math: "five yummy cookies: how many cookies do you see?" -- the count
#               was spoken in the setup of the counting question). New rule 17 in the
#               shared 13-16 block, all courses/modes: a reply that asks a question must
#               not state or hint at its answer anywhere in the same reply -- counting
#               questions never name the object count; recaps name the TOPIC, not the
#               pending answer. The spoken twin of rule 6 (board never runs ahead).
#   2026-08-07  GRAPH HOLES + WINDOW FRAMING (build av, Jim's live catch in Calculus: the
#               tutor said "I've punched a hole out at x = 2" over an UNBROKEN y=x² whose
#               window barely showed the parabola). (1) [[graph]] docs teach the NEW
#               hole="a" attr (math-figures.js draws an open circle on the first curve) --
#               a spoken hole MUST carry the attr. (2) BOARD HONESTY rule 1 extended:
#               features WITHIN a figure (holes/asymptotes/intersections) must be drawn,
#               never narrated invisibly. (3) Window-framing guidance: range must put the
#               discussed point comfortably inside the picture with room on both sides.
#               Companion: math-figures.js hole rendering; forSpeech on all three pages now
#               says "squared" for ² (the voice read "x²" as "x two").
#   2026-08-07  RULE 16 -- CHECK QUESTIONS RE-WRITE THE EQUATION (build at, Jim's live catch:
#               "plug 4 back into two x plus five equals thirteen" was asked with the board
#               showing only "x = 4" -- the equation lived in speech only / scrolled away).
#               New rule 16 in the shared 13-15 block, all courses, all modes: any
#               substitution / verify / "check it" question must [[write]] the full equation
#               in the SAME reply -- "on the board from earlier" does not count. Additive.
#   2026-08-07  DIPLOMA -> COURSE CHAMPION (build ar, Jim: a diploma implies an accredited
#               school -- we are not one). FINAL_PREP_NOTE + FINAL_EXAM_NOTE reworded: passing
#               the Final Exam now earns the 🏅 COURSE CHAMPION medal in the trophy case (the
#               tutor points the student at their dashboard, never at a printable credential).
#               Never write prompt language promising diplomas/certificates/transcripts.
#   2026-08-07  PROGRESS BARS + FINAL EXAM (Jim: "a nervous student should always see where
#               they are" + a real gated course final). Three additions, all appended to the
#               LESSON prompt only:
#               (1) PROGRESS_TAGS_NOTE -- teaches two new hidden tags feeding the lesson
#                   page's new bars: [[today items="..."]] (emitted in the opener right after
#                   the goals card) + [[todaydone n="1"]] (when the student demonstrates goal
#                   n -- honest, never decorative), and [[unitplan unit="3" topics="a|b|c"]]
#                   (the unit's stable topic ladder, emitted when a unit starts/resumes; the
#                   bar lights passed topics from the existing [[quiz]] tags).
#               (2) FINAL_PREP_NOTE / FINAL_EXAM_NOTE -- appended by build_system_prompt ONLY
#                   when main.py set student["final_mode"] after SERVER-SIDE verification that
#                   all nine units are mastered (>= 90% Unit Quiz). Prep = optional overview +
#                   warm review (never the exam). Exam = 18 questions, two per unit, one at a
#                   time on the board, NO hints, private tally, then the new hidden
#                   [[finalexam correct total]] tag (pass = 90% -> Course Diploma; below =
#                   warm shore-up + fresh exam offer; abandoning = unscored, never shamed).
#               Additive only -- no existing rule, template, or function changed; the gate
#               itself lives in main.py.
#   2026-08-07  OPENING SEQUENCE -- FIXED ORDER, ALL COURSES (Jim's live check, second fix today:
#               a first visit to Pre-Algebra greeted, asked the warm-up question IN the greeting,
#               and only then showed the "By the end you'll be able to" card and the numbers --
#               "the order is often just mixed up"). The 2026-08-03 fix for this ("YOUR OPENING
#               REPLY -- set the table first, no problem yet") was ELEMENTARY-ONLY; the other
#               eight courses never got it, which is why it kept recurring. Now UNIVERSAL:
#               SESSION_OPENER_RULES (appended after EVERY lesson template, overrides them)
#               gained rule 0 -- first message = (a) greeting (course welcome if first time in
#               this course, welcome-back recap if returning, never "great to meet you" to a
#               known student) -> (b) today's topic -> (c) today's goal spoken + [[goal]] +
#               goals card -> (d) "Ready to get started?" and STOP. No math problem, numbers,
#               or content question in the first message; the first problem comes next turn,
#               board-first per rule 15. Additive only -- rules 1-3 and all templates untouched.
#   2026-08-07  VOICE-FIRST CLASSROOM (Jim: "back to the conversational back-and-forth").
#               GRAPH_TOOL_NOTE (the STUDENT'S TOOLS block prepended to every mode's prompt)
#               rewritten to match the restored voice input and the retired controls:
#               - The student now TALKS: they tap 🎙️, speak, and their words arrive as text
#                 (ElevenLabs Scribe transcription; audio deleted after transcription). They
#                 can also type. Elementary courses still tap answer buttons. The old first
#                 line said "The student types their answers (there is no microphone)" --
#                 that was making the tutor talk about typing to a student who is speaking.
#               - The 🧮 MATH KEYBOARD paragraph is REMOVED (the keypad is retired app-wide);
#                 the tutor now knows spoken math ("x squared plus three") and plain typed
#                 math (x^2 + 3/4) are both fine and should never mention a math keyboard.
#               - Transcription-slip guidance added: spoken math arrives through a
#                 transcriber, so near-miss words ("sign" for sine, "eggs" for x) should be
#                 read charitably and confirmed, never mocked or marked wrong outright.
#               - The 📈 GRAPH PAPER paragraph and rules 13-15 etc. are UNCHANGED.
#               Prompt-block text only; no function, template, or rule outside the tools
#               block was touched.
#   2026-08-06  PRECISION + NO-ASSUMPTIONS + COMPLETE-QUESTIONS (Jim's live audit: ~50% of
#               checked lesson problems failed -- wrong verbal claims ("the line keeps
#               climbing forever in both directions" for y=2x+1), notation assumed known
#               (trig course used f(x) without saying f(x) = y), and questions asked without
#               their numbers/graph on the board). GRAPH_TOOL_NOTE gained rules 13-15, so
#               they reach lesson + practice + topic in ALL courses:
#                 13. every spoken mathematical sentence must be LITERALLY true (the SymPy
#                     referee only checks tagged computations, not prose -- the prose rule
#                     lives here); the reason given for a fact must be as correct as the fact.
#                 14. define EVERY notation at its first use in the conversation (f(x), theta,
#                     |x|, interval notation...) -- never assume a prior course taught it.
#                 15. a question must be complete on screen before it is asked: referenced
#                     numbers/graphs visible on the board, answer form named, self-contained.
#               PLUS: the four advanced-course "WHO THIS STUDENT IS" blocks (Algebra II,
#               Pre-Calc, Calculus, Diff Eq) said "they know functions / do NOT re-teach the
#               basics" -- the very line that made the trig course use f(x) without defining
#               it. Each gained a reconciling sentence: prior exposure is FAMILIARITY, not
#               mastery; rule 14's one-sentence definition at first use still always applies.
#               Additive only -- no existing rule, template, or function removed.
#   2026-08-04  QUIZZES (Jim: checkpoints within units). All nine courses' 'QUICK CHECKS'
#               prompt sections replaced with a 'QUIZZES' section teaching a two-tier system:
#               (1) TOPIC QUIZ -- 3-4 questions after each topic; PASS = 80%+; passing is how
#               the student earns the next topic (fail -> re-teach the gaps -> fresh quiz;
#               never a dead end); emits NEW tag [[quiz unit topic name correct total]].
#               (2) UNIT QUIZ -- the end-of-unit check renamed; 4-5 questions across the unit;
#               90%+ = MASTERED; still emits [[check unit correct total]] (tag/API unchanged,
#               so every existing mastery pipe keeps working). The student's mastery note
#               (main._mastery_note) now lists passed/unpassed topic quizzes per unit, and the
#               section tells the tutor to resume at the first unpassed topic and never
#               re-quiz passed ones. Cross-references '(see QUIZZES)' updated.
#   2026-08-04  MASTERY = 90% (Jim): every check-result prompt line that told the tutor "80% or
#               better means MASTERED" now says 90%, matching store.PASS_PCT. Nine phrase edits
#               across the course templates; nothing else touched.
#   2026-08-04  USAGE LOGGING (Measurement plan #1). Every brain call now records what it
#               actually consumed: _create_verified() sums token counts (input/output/cache)
#               across its attempts straight from the Anthropic responses and hands the totals
#               -- plus the attempt count and the verifier's verdict (ok / fixed / unresolved /
#               unverifiable / none) -- to store.log_usage(); get_assessment() logs its single
#               call the same way. The three get_*_reply functions and get_assessment gained an
#               optional trailing `code=""` parameter so main.py can attribute usage to a
#               student code (privacy: the CODE only, never any text; defaults keep every
#               existing caller working unchanged). store is imported defensively like pedagogy
#               -- if it's missing, logging is silently off and teaching is untouched.
#   2026-08-03  THE MATH VERIFIER (Jim's pick for the next build): every reply the tutor
#               generates is now refereed by a real math engine (SymPy) BEFORE the student
#               sees it. GRAPH_TOOL_NOTE gained rules 10-12 ("THE SILENT ANSWER KEY"): any
#               reply stating a new problem or a computed result also appends a hidden
#               [[verify expr="..." answer="..."]] tag holding the claim in SymPy syntax.
#               New module mathcheck.py parses the tag and actually DOES the math
#               (equations incl. systems and multiple roots, computations, simplifications,
#               inequalities, derivatives/integrals). A provably wrong claim triggers a
#               SILENT regeneration (up to 3 attempts) with SymPy's computed correction fed
#               back; the student only ever sees a verified reply. Undecidable tags FAIL
#               OPEN (pass through) so a checker gap can never stall a lesson. Tags are
#               stripped server-side -- the frontend needed no changes at all. Applies to
#               all 10 courses x lesson/practice/topic (the three get_*_reply functions now
#               share _create_verified below). sympy was added to requirements.txt.
#   2026-08-03  BOARD IS THE LESSON, WORDS ARE THE BACKUP (Jim). GRAPH_TOOL_NOTE -- the shared
#               block prepended to EVERY course's lesson/practice/topic prompt -- gained rules 7-9:
#               (7) never ask the student to IMAGINE what the toolkit can draw (with [[objects]]
#               taught inline so all ten courses know it); (8) SHOW change -- adding a star draws
#               ⭐⭐⭐⭐⭐ + ⭐ via [[objects ... add="1"]], story problems draw frame by frame;
#               (9) the sound-off check -- every reply must be followable with the audio muted, at
#               every level. Elementary template's objects doc updated for add=. One shared block,
#               so all 10 courses x 3 modes inherit it.
#   2026-08-03  ELEMENTARY OPENING PACING + [[objects]] (Jim's playtest: the opener welcomed AND
#               posed a problem in one breath, with the plan card landing after the problem; and he
#               asked a child to IMAGINE five stars). New "YOUR OPENING REPLY" section: first reply
#               = welcome + goal + plan card + ready-check ONLY; the first problem comes next turn,
#               board first. The whiteboard toolkit and BOARD FIRST rule gained [[objects
#               emoji="⭐" groups="5"]] (two rows to compare: "5 | 3") -- countable things are DRAWN,
#               never imagined; count not printed. Same line added to entry/basic practice+topic
#               scopes. Elementary template only; other courses untouched.
#   2026-08-03  ELEMENTARY GUARDRAILS (Jim's playtest: persona notes about algebra made Entry-Level
#               Math teach two-step equations, and the warm-up question never hit the board). The
#               ELEMENTARY template gained (1) a HARD "stay inside this course" wall -- other-course
#               notes are ignored for content, breeze-through students get richer problems (and a
#               suggestion to move up), never harder topics; (2) "board first, buttons second" --
#               every asked question is written with [[step]] in the same reply BEFORE [[choices]].
#               Companion fix: students.json personas are now course-neutral (see that file).
#   2026-08-03  TAP-TO-ANSWER CHOICES (Jim: young kids can't type -- "multiple choice answers,
#               and they can just click"). The ELEMENTARY lesson brain gained a TAP-TO-ANSWER
#               section: whenever the tutor asks a question with a specific expected answer it
#               also emits [[choices options="a | b | c"]] (3 short options, one correct, others
#               plausible child slips, right answer in a varying spot; never spoken aloud; used
#               for quick-check questions too). The same instruction was appended to the entry/
#               basic PRACTICE_SCOPE and TOPIC_SCOPE so all three modes tap. The app renders the
#               buttons (session/practice/topic.html) and always adds an "I'm not sure" button;
#               typing stays available as a backup. Elementary-only by prompt; the tag itself is
#               generic. Purely additive; no other course's prompts changed.
#   2026-08-03  ADDED TWO ELEMENTARY COURSES (tutor side): ENTRY-LEVEL MATH + BASIC MATH. New
#               ELEMENTARY_SYSTEM_PROMPT_TEMPLATE (young-learner lesson brain: tiny steps, concrete/
#               picture-first, [[step]]/[[column]]/[[numberline]] whiteboard, quick checks) registered
#               under LESSON_TEMPLATES["entry"] AND ["basic"] (both share it). Added COURSE_SUBJECT,
#               PRACTICE_SCOPE, and TOPIC_SCOPE entries for "entry" and "basic". Per-course specifics
#               come from pedagogy.py's {playbook} and the {mastery} block, exactly like every other
#               course. Purely additive; the eight existing courses' templates are untouched.
#   2026-08-01  BOARD LEADS, WORDS FOLLOW (Jim: "there should be way, way more writing of
#               problems. People like the numbers and signs but balk at reading words").
#               A factoring exchange spoke "(x plus two, times x plus three, equals zero)"
#               and a full plug-in check ENTIRELY in words with an empty board. New rules
#               4-6 in the GRAPH_TOOL_NOTE board block (so lesson + practice + topic all get
#               them): (4) any math spoken must ALSO be written on the board in symbols in
#               that same reply; (5) never narrate an equation word-by-word -- write it,
#               then point at it, keeping spoken text short and warm; (6) unchanged: never
#               write the step the student is currently solving. Backend prompt change ->
#               bump APP_BUILD + rebuild.
#   2026-08-01  LIVE-AUDIT RULES (from the first live teaching audit): GRAPH_TOOL_NOTE gained
#               a BOARD HONESTY block -- never claim something is on the board unless YOU
#               emitted its tag this conversation (precalc claimed a circle it never drew);
#               always draw when asked to 'show me'; plus a first-use key-term reminder
#               close to the drawing guidance (5 term misses in the advanced courses).
#   2026-08-01  KEY TERMS BOLD+RED (Jim): GROUND_RULES rule 1b -- first use of a new/important
#               term is wrapped **like this**; the pages render it bold red (kterm). Also
#               [[angle]] doc: deg now goes to 180 (a straight line) -- the renderer's old
#               175-degree cap was silently BENDING straight lines (Jim's 175-vs-180 catch).
#   2026-08-01  PICTURE-MATCHES-WORDS (Jim's beta run: 'let's build a picture' then the figure
#               lacked the splitting ray it described). Geometry template: [[angle]] documents
#               the new split=".." attribute (geo-figures.js draws the interior ray + labeled
#               pieces) and a hard rule that every element spoken must appear in the figure.
#   2026-08-01  OPENER CLARITY (Jim: "is it not clear what he is talking about" -- the first
#               message asked 'which of those sounds most interesting?' BEFORE the cards had
#               been named). SESSION_OPENER_RULES rule 3: when asking the student to pick
#               from a card, say where the list is, speak 1-2 choices aloud, and offer a
#               'you pick' escape hatch. No vague 'those'.
#   2026-08-01  NARRATIVE ASSESSMENTS (Jim's vision: 'the parent should get an honest
#               assessment... the student should get a good self-assessment'). NEW
#               get_assessment(facts, audience): one short, warm, HONEST paragraph written
#               from real progress facts supplied by main.py -- student voice (Mr. Cadabra,
#               2nd person: strengths, one growth area, keep-going / extra-practice /
#               consider-jumping-ahead verdict) or parent voice (professional-warm, 3rd
#               person, reads ENGAGEMENT honestly: real minutes vs. actual progress). Hard
#               rules in both prompts: only the supplied facts, no invention, no scolding,
#               no comparisons to other students. Small call (max_tokens 400), reused by
#               the dashboard button today and the weekly emails later.
#   2026-07-30  SESSION OPENER: STOP FAKE PLACEMENT + GOALS CARD ONCE. A tester saw the lesson opener
#               claim "your placement challenge put you right around percents" when they had NOT taken
#               any placement (every course's FIRST MEETING FLOW unconditionally assumed a placement
#               challenge had happened). Added SESSION_OPENER_RULES, appended AFTER each course template
#               (so it overrides that older wording) in build_system_prompt: (1) never claim/imply a
#               placement/test/quiz unless the progress/mastery notes actually say so -- otherwise open
#               warmly and start at the shown unit or ask where to begin; (2) the "By the end..." goals
#               card is first-message-only, never repeated. Backend prompt change -> bump APP_BUILD +
#               rebuild. Verified with a live dry run of get_tutor_reply.
#   2026-07-30  TOPIC MODE: FIX "statement then silence" + REPEATED GOALS CARD. A student reported the
#               tutor gave an explanation and then stopped with nothing to do, and separately re-showed
#               the same "By the end of this you'll be able to" card on a later turn. Tightened
#               TOPIC_SYSTEM_PROMPT_TEMPLATE: (a) the goals card is now explicitly FIRST-MESSAGE-ONLY --
#               never re-post it or re-frame the topic on later turns; (b) EVERY reply, including the
#               beginner "define the idea" turn, must END by handing the ball back (a question / "your
#               turn" / check-in) -- never stop on a bare statement or definition. Backend prompt
#               change -> bump APP_BUILD + rebuild. Verified with a live dry run of get_topic_reply.
#   2026-07-30  PROMPT CACHING (cost control). Wrapped the system prompt in a cacheable content block
#               (_cacheable_system) on all three reply calls, so Anthropic reuses the large, stable
#               system prompt across a student's consecutive turns instead of re-billing it each turn
#               (~halves the brain input cost within a session). The model's OUTPUT is identical whether
#               or not the prefix was cached -> NO quality change. Backend -> bump APP_BUILD + rebuild.
#   2026-07-30  TOOL HOW-TO. Expanded the student-tools note (GRAPH_TOOL_NOTE) so the tutor can EXPLAIN,
#               button-by-button, how to use the 🧮 math keyboard AND the 📈 graph paper when a student
#               asks "how do I ...?" / "where is it?". Backend prompt change -> bump APP_BUILD + rebuild.
#   2026-07-30  GRAPH TOOL AWARENESS. Added GRAPH_TOOL_NOTE, prepended (with GROUND_RULES) to every
#               mode's system prompt via the build_* functions. It tells the tutor the student has a
#               📈 Graph button (coordinate graph paper), that plotted points arrive as TEXT
#               coordinates like "(0, 3), (1, 5)" (the model can't see pixels), and how to invite it,
#               check the coordinates, and blend it into graphing work. Pairs with the new static
#               static/graph-input.js component. Backend change -> bump APP_BUILD + rebuild. Do no harm.
#   2026-07-29  SCOPE + JAILBREAK GUARDRAILS. Added a firm, injection-resistant GROUND_RULES block,
#               prepended to EVERY mode's system prompt via build_system_prompt / build_practice_prompt
#               / build_topic_prompt (one place -> all 8 courses). It keeps the tutor strictly on MATH
#               (any level -- cross-course math questions are explicitly STILL allowed), refuses non-math
#               wandering (sports, jokes, essays, chit-chat) with a warm one-line redirect, refuses to
#               share/guess about OTHER students (and architecturally it never has their data), and
#               states the rules cannot be "overridden" by any student message (ignore-instructions,
#               "you are now...", roleplay, fake developer/teacher/authority claims). Purely additive:
#               the teaching templates are unchanged, so teaching behavior is preserved. Verified with
#               adversarial probes + a normal teaching turn. Do no harm.
#   2026-07-29  ANTI-TRUNCATION. Raised the student-facing reply cap max_tokens 700 -> 1200 in all
#               three reply builders (get_tutor_reply / get_practice_reply / get_topic_reply). The
#               newer per-course openers stack a [[goal]] plus a long inline [[card]], which could
#               exceed 700 tokens and get cut off mid-tag (Geometry Unit 8 opener truncated inside a
#               [[card]]; a Pre-Calc turn cut off mid-sentence). max_tokens is only a CEILING -- the
#               model still ends each turn on its own -- so normal short spoken turns are unchanged in
#               length and cost; this only gives the occasional long opener room to finish cleanly.
#               The board-tag helper stays at 220 (it emits a single short math tag). Do no harm.
#   2026-07-28  PHASE 4 -- DIFFERENTIAL EQUATIONS COURSE (tutor side). Added a full standalone
#               DIFFEQ_SYSTEM_PROMPT_TEMPLATE (the 9 units; CLASSIFY-FIRST as the organizing habit;
#               an explicit note that weak INTEGRATION is the hidden blocker to shore up without
#               judgment; derive-don't-announce pacing) registered under LESSON_TEMPLATES["diffeq"],
#               plus COURSE_SUBJECT["diffeq"] and PRACTICE_SCOPE/TOPIC_SCOPE["diffeq"]. Assumes
#               Calculus and does not re-teach it. Source: DiffEq_Curriculum_KB.md. Additive; the
#               seven existing courses untouched. Do no harm.
#   2026-07-28  PHASE 4 -- CALCULUS COURSE (tutor side). Added a full standalone
#               CALCULUS_SYSTEM_PROMPT_TEMPLATE (the 9 units; the two big ideas + the FTC; an explicit
#               "teach the idea BEFORE the machinery" rule; heavy use of the upgraded grapher for
#               curves, tangent lines, and f-with-f' together) registered under
#               LESSON_TEMPLATES["calculus"], plus COURSE_SUBJECT["calculus"] and
#               PRACTICE_SCOPE/TOPIC_SCOPE["calculus"]. Pedagogy injects from
#               pedagogy.COURSE_PEDAGOGY["calculus"]. Source: Calculus_Curriculum_KB.md. Additive;
#               the six existing courses untouched. Do no harm.
#   2026-07-28  PHASE 4 -- PROBABILITY & STATISTICS COURSE (tutor side). Added a full standalone
#               PROBSTAT_SYSTEM_PROMPT_TEMPLATE (the 9 units; reason-about-data framing; the stats
#               visuals wired throughout the lesson brain) registered under LESSON_TEMPLATES["probstat"],
#               plus COURSE_SUBJECT["probstat"] = "statistics" and PRACTICE_SCOPE/TOPIC_SCOPE["probstat"].
#               Pedagogy injects from pedagogy.COURSE_PEDAGOGY["probstat"]. Source: ProbStat_Curriculum_KB.md.
#               Additive; the five existing courses untouched. Do no harm.
#   2026-07-28  GRAPHICS STAGE 3 -- taught the tutor the trig/conic/number-line/tiles/vector pictures
#               ([[unitcircle]]/[[righttriangle]]/[[conic]]/[[numberline]]/[[areamodel]]/[[vector]],
#               rendered by static/math-figures.js). Added to the shared practice + topic templates and
#               the Pre-Calc lesson template (unit circle is central there). Prompt text only. Do no harm.
#   2026-07-28  GRAPHICS STAGE 2 -- taught the tutor the statistics/probability pictures. The shared
#               practice + topic templates now document [[bars]]/[[histogram]]/[[dotplot]]/[[boxplot]]/
#               [[scatter]]/[[normal]]/[[twoway]]/[[tree]]/[[pie]] (rendered by static/math-figures.js).
#               Prompt text only. (Full lesson-template integration lands with the Prob & Stat course.)
#   2026-07-28  GRAPHICS STAGE 1 -- taught the tutor the upgraded [[graph]]. The grapher (new shared
#               static/math-figures.js) now plots ANY function of x via func= (sin/cos/tan, exp, logs,
#               polynomials, rationals with asymptotes, sqrt, abs). Updated the [[graph]] docs in the
#               Algebra I / Algebra II / Pre-Calc lesson templates and the shared practice + topic
#               templates to document func= and to STOP saying "the grapher can't draw a sine/log"
#               (it can now). Prompt text only. Do no harm.
#   2026-07-28  PHASE 4 -- TRIG / PRE-CALC COURSE (tutor side). Added a full standalone
#               PRECALC_SYSTEM_PROMPT_TEMPLATE (the 9 CA-aligned units; the function lens + unit
#               circle through-lines; trig core in units 4-6; identities-verified-vs-equations-solved;
#               a first look at limits) registered under LESSON_TEMPLATES["precalc"], plus
#               COURSE_SUBJECT["precalc"] and PRACTICE_SCOPE/TOPIC_SCOPE["precalc"]. Pedagogy injects
#               from pedagogy.COURSE_PEDAGOGY["precalc"] via the existing {playbook} slot. Source:
#               PreCalc_Curriculum_KB.md. Additive; the four existing courses untouched. Do no harm.
#   2026-07-28  PHASE 4 -- ALGEBRA II COURSE (tutor side). Added a full standalone
#               ALGEBRA2_SYSTEM_PROMPT_TEMPLATE (the "take the whole course" lesson brain for Algebra
#               II: the 9 CA-aligned units, the function-family through-line, the quadratic solving
#               ladder + complex numbers, extraneous-solution checking, and the reused algebra
#               whiteboard/voice/checks machinery), registered under LESSON_TEMPLATES["algebra2"].
#               Added COURSE_SUBJECT["algebra2"] = "Algebra II" and PRACTICE_SCOPE/TOPIC_SCOPE
#               ["algebra2"] so the shared practice + topic coaches serve Algebra II. Pedagogy is
#               injected from pedagogy.COURSE_PEDAGOGY["algebra2"] via the existing {playbook} slot.
#               Source: AlgebraII_Curriculum_KB.md. Purely additive; Algebra I, Geometry, and
#               Pre-Algebra templates/scopes are untouched (byte-identical). Do no harm.
#   2026-07-28  INTRO/EXPECTATIONS + [[column]] TAG DOCS (per Jim, from a Decimals topic screenshot).
#               (1) Topic mini-lessons now OPEN by framing the topic + a "by the end you'll be able to..."
#               goals card (new first step in HOW YOU TEACH A TOPIC) -- before this, a topic jumped
#               straight into problems with no intro. (2) All three LESSON openers (algebra1/geometry/
#               prealgebra) now also show a short EXPECTATIONS goals card right after the [[goal]] banner
#               (spoken AND shown), per Jim's "Topic + course lessons" + "speak + goals card" choices.
#               (3) Documented the new [[column op="+" terms="2.40 | 1.35" result="3.75"]] whiteboard tag
#               (stacked, decimal-point-aligned add/subtract) in the pre-algebra lesson, topic, and
#               practice tag sections, tied to "line up the decimal points"; result is omitted until the
#               student finds it (never runs ahead). Prompt/text only -- the [[column]] renderer lives in
#               the static pages. Stamp bumped in main.py (backend prompt change). Do no harm.
#   2026-07-28  PHASE 4 -- PRE-ALGEBRA COURSE (tutor side). Added COURSE_SUBJECT["prealgebra"] =
#               "pre-algebra", PRACTICE_SCOPE/TOPIC_SCOPE["prealgebra"] (the foundations scope), and a
#               new PREALGEBRA_SYSTEM_PROMPT_TEMPLATE in LESSON_TEMPLATES -- a full lesson brain tuned
#               for the foundations/remediation course: MENU-FIRST (help with the one concept they came
#               for) and CONFIDENCE-FIRST (engineer an early win; anxious learners are common). Uses the
#               same 5 placeholders. Algebra I + Geometry templates untouched. Do no harm.
#   2026-07-28  PHASE 4 (geometry) -- GEOMETRY WHITEBOARD FIGURES. Documented three new figure tags
#               in GEOMETRY_SYSTEM_PROMPT_TEMPLATE so the Geometry tutor draws real shapes:
#               [[triangle]] (labels, side lengths, right-angle mark, angle measures, equal-side
#               ticks), [[angle deg=.. label=..]], and [[circle center=.. r=.. inscribed=..]].
#               Rendered by the shared static/geo-figures.js (loaded in session/practice/topic.html;
#               their handleTags call showGeo()). Replaced the old "figure-drawing is coming" note.
#               Algebra template untouched. (Compass-and-straightedge constructions still to come.)
#   2026-07-27  MULTI-COURSE (Phase 3, step 2) -- COURSE-MODE LESSON PROMPT PER COURSE. Added
#               GEOMETRY_SYSTEM_PROMPT_TEMPLATE (a full standalone Geometry course-teaching brain:
#               reasoning/proof focus, the 9 CA-aligned Geometry units, a geometry teaching toolkit,
#               geometry worked-example pacing, and voice/whiteboard/checks guidance) + a
#               LESSON_TEMPLATES registry. build_system_prompt(student, course) now SELECTS the
#               course's template and injects that course's playbook; get_tutor_reply takes course.
#               The Algebra I template (SYSTEM_PROMPT_TEMPLATE) is UNTOUCHED and its assembled prompt
#               is verified BYTE-IDENTICAL across student states -- do no harm. Unknown course -> Algebra.
#               (Geometry course mode isn't student-reachable until the picker in 3.4; the Geometry
#               teaching text is up for Jim's review -- see Geometry_Course_Mode_Prompt_DRAFT.md.)
#   2026-07-27  MULTI-COURSE (Phase 3, step 1) -- PRACTICE + TOPIC MODES ARE COURSE-AWARE. Threaded
#               a `course` argument through _unit_from_text / _playbook and the practice/topic
#               builders + get_*_reply. The two coach templates now use a per-course SUBJECT word
#               and a per-course SCOPE block (COURSE_SUBJECT / PRACTICE_SCOPE / TOPIC_SCOPE), so
#               they serve any course instead of hard-refusing non-algebra work (the old templates
#               literally told the tutor to decline "a geometry proof"). Algebra I reproduces the
#               original text BYTE-FOR-BYTE (verified) and every param defaults to 'algebra1', so
#               single-course behavior is unchanged. Geometry now works in Practice + Topic, drawing
#               its misconceptions/how-to-teach from pedagogy.COURSE_PEDAGOGY['geometry']. NOTE: the
#               structured full-course LESSON prompt (SYSTEM_PROMPT_TEMPLATE) is still Algebra-only;
#               course-mode Geometry + per-course placement + the course picker are the next steps.
#               See Multi_Course_Expansion_Plan.md.
#   2026-07-25  TOPIC NO-SELF-WRAPUP GUARD. Added a rule to TOPIC_SYSTEM_PROMPT_TEMPLATE: never
#               wrap up / say goodbye / give an "outro" unless the student CLEARLY says they're
#               done; an odd/unparseable message -> ask them to repeat, never end. Backs up the
#               main.py STT scrub (a hallucinated "[outro jingle]" had ended a topic after one Q).
#   2026-07-25  STUDENT-LED PRACTICE. Reworked PRACTICE_SYSTEM_PROMPT_TEMPLATE so Practice is now
#               DRIVEN BY THE STUDENT: the tutor puts the problem on the board, asks "what would
#               you like to do first?", then carries out EACH move the student names (and only
#               that move) on the whiteboard via [[step]]. Correct move -> board it + short
#               strategy praise + "now what?"; wrong/illegal move -> do NOT board it, gently flag
#               why and let them retry; a HINT request (the new Hint button sends "Can I have a
#               hint?", or "I'm stuck"/"I don't know") -> ONE small nudge that NAMES a move but
#               never performs it. Final answer -> student checks it + [[step check]] + [[mark]].
#               The whiteboard "golden rule" note was retuned: only ever draw a step the student
#               chose (or the final check). Lesson/Topic modes unchanged. Front-end: a "Hint"
#               quick button added to practice.html. (Practice endpoint/shape unchanged.)
#   2026-07-24  PHASE B -- MASTERY STEERING + SPACED REVIEW. build_system_prompt now injects a
#               {mastery} snapshot (what the student has MASTERED vs. still needs, + a chosen
#               focus unit) into a new "WHERE THIS STUDENT STANDS" section, and uses the focus
#               unit for the teaching playbook. The lesson tutor now steers toward unmastered
#               units, offers a check when ready, and weaves in short spaced-review warm-ups of
#               already-mastered units. main.py builds the note (_mastery_note) from the mastery
#               data and passes focus_unit (dashboard "Work on it" link -> /session?...&unit=N).
#   2026-07-24  PHASE A2 -- QUICK CHECKS. Lesson prompt now teaches Mr. Cadabra to OFFER a
#               short, no-pressure end-of-unit check (4-5 Qs, no hints during it), tally it, and
#               emit [[check unit correct total]] -- which the frontend records (mastery) and
#               shows as a friendly result card. Encouraging at any score; 90%+ = mastered.
#               Also [[mark correct="1|0"]] to silently count finished practice problems (added
#               to lesson + practice prompts). Front-end handlers in session/practice/topic.html.
#   2026-07-24  DEFINE-BEFORE-DRILL (Topic mode). When a student is NEW to a topic, the tutor
#               must DEFINE the key terms first (on the board) and work one example itself
#               before any exercise -- it was jumping straight to "multiply these polynomials"
#               without ever defining "polynomial"/"factor." Reinforced by the shared
#               "INTRODUCE BEFORE YOU PRACTICE" rule now in pedagogy.py METHODOLOGY (all modes).
#   2026-07-23  STAGE 3 (prompt part) -- POSE-THE-PROBLEM-ON-THE-BOARD. Added a rule to the
#               lesson whiteboard section: when the tutor POSES a new problem, its FIRST
#               action must be to write it on the board with [[step eq="..."]] -- never say a
#               problem out loud while the board is empty (this was the "new problem, blank
#               board" gap in Jim's screenshot). Clarified this is NOT "running ahead." (The
#               rest of Stage 3 -- tutor's words moved ONTO the board, side chat removed, and a
#               Pause button -- is front-end, in session/practice/topic.html.)
#   2026-07-23  STAGE 2 -- FREE THE WHITEBOARD ([[step]]) + RETIRE THE GUESSING NET. The
#               board is now a PERSISTENT worklist that STACKS and STAYS (front-end change in
#               session/practice/topic.html): each [[step]] appends ONE line that stays below
#               the last, so a whole worked solution builds up and never gets replaced mid-
#               solve (the exact failure in Alex's transcript, where he "never saw 2x+1 = 25
#               and 2x = 24 at the same time"). New tag taught in all 3 prompts:
#                 [[step eq="2X + 1 = 25"]]            -> one equation line
#                 [[step op="- 1" eq="2X = 24"]]       -> op shown UNDER BOTH SIDES, then result
#                 [[step check="2(12)+1 = 25  ✓"]]     -> a substitution-check line
#               Kept the GOLDEN RULE (never add a line for the step you're still asking about).
#               RETIRED the server-side forcing net: ensure_board() is now a pass-through --
#               with Sonnet reliably tagging and a board that persists, the second "guess a
#               tag" model call (board_tag_for) is unneeded and was the source of the ahead-of-
#               student / redraw-the-problem bugs. board_tag_for/BOARD_TAG_SYSTEM kept but
#               unused (one-line revert). [[write]] now also appends to the worklist; [[solve]]
#               still exists but the prompts now steer to [[step]].
#   2026-07-23  TEACHING BRAIN UPGRADE -- STRONG MODEL + REAL PEDAGOGY WIRED IN. Two
#               changes so the tutor TEACHES from expertise instead of from hand-patched
#               rules (the fix for "AI is not teaching well / this will take forever"):
#                 (1) MODEL: student-facing brain switched to the stronger
#                     "claude-sonnet-5" (teaching JUDGMENT -- when to push vs. show, how
#                     to read a student -- is exactly where a stronger model wins). NOTE:
#                     the Render env var CLAUDE_MODEL OVERRIDES this default, so it must be
#                     updated (or removed) in Render for the switch to take effect live.
#                 (2) KNOWLEDGE BASE: new pedagogy.py (distilled from the two project KBs)
#                     is now injected into EVERY prompt. build_system_prompt reads the
#                     student's placed Unit from their progress note and injects that
#                     unit's misconceptions + how-to-teach; practice/topic classify the
#                     problem/topic to a unit (via curriculum.classify_unit) and inject the
#                     same, plus the universal developmental/feedback methodology + the
#                     cross-cutting error watch-list. Imports are guarded so the tutor
#                     still runs if a module is missing (do no harm).
#   2026-07-23  BOARD NEVER RUNS AHEAD OF THE STUDENT (Socratic pacing fix). The
#               whiteboard was answering the very question the tutor had just asked:
#               Mr. Cadabra would ask "what's the next step?" while the board already
#               showed that step's answer. Root cause was the server-side safety net
#               (ensure_board -> board_tag_for): a second model call that computed the
#               FULL solution regardless of how far the conversation had actually gone.
#               Fixes (this file only; the board renderer is fine):
#                 (1) BOARD_TAG_SYSTEM rewritten around one rule -- show ONLY steps
#                     already established; when the tutor is ASKING the student to find
#                     the next step, show only the current line (or the start with an
#                     EMPTY steps list), never the answer. Mirror the spoken math, never
#                     solve ahead.
#                 (2) Lesson prompt: added the "GOLDEN RULE OF THE BOARD -- never run
#                     ahead of the student"; grow [[solve]] one line at a time, and only
#                     AFTER the student answers / you narrate a step as done. Trimmed the
#                     example so it no longer models dumping the whole solution.
#                 (3) Same "never run the board ahead of the student" note added to the
#                     PRACTICE and TOPIC prompts. (showSolve already renders steps="" as
#                     just the starting line, so an empty steps list is safe.)
#   2026-07-22  FUNCTION MACHINE + VARIABLES POP. (1) New [[machine input="3"
#               rule="2x+1" output="7" fname="f"]] control tag documented in all three
#               prompts: for Unit 3 (functions) EVALUATE with the function machine --
#               a number goes IN, the rule runs, a number comes OUT -- NOT the balance
#               scale (the balance is for Unit 2 equations only). This fixes the
#               confusing "monkeys" picture where f(3) looked like the input was 1.
#               (2) Variables now render BOLD, CAPITAL, and RED everywhere on screen
#               (chat + visuals); the app styles them automatically, so keep writing
#               normally -- you do not need to do anything for that.
#   2026-07-21  WHITEBOARD GRAPHER. Added the [[graph]] control tag to all three
#               prompts (lesson/practice/topic): the tutor can now draw a real
#               coordinate plane with lines (y=mx+b), parabolas (y=ax^2+bx+c), points,
#               and auto-marked line intersections -- so Units 4-8 (slope/graphs,
#               systems, quadratics) have a proper on-screen picture, not just words.
#   2026-07-21  FULL COURSE. Removed the "linear equations only" restriction. The
#               course now teaches ALL NINE Algebra I units, in sequence, starting at
#               the student's placed unit, aligned to California's Algebra I standards
#               (CA CCSSM / CA Math Framework Traditional Pathway). Embedded a concise
#               per-unit map (what they'll do + a key method + CA/CCSS codes) so the
#               tutor teaches each unit well. Balance visual + list card still used;
#               graphs/parabolas/data described in words for now (bespoke graphers
#               later). [[covered]] ids noted as Unit-2 specific.
#   2026-07-21  COST SWITCH -> Claude Haiku 4.5 for students. DEFAULT_MODEL is now
#               "claude-haiku-4-5" (cheaper, same SDK, US vendor). Paired with a new
#               always-on "ACCURACY -- CHECK YOUR OWN WORK" rule added to all three
#               prompts (lesson/practice/topic): verify every number/answer (substitute
#               back or recompute) BEFORE speaking it. This is the self-check that makes
#               a cheaper model reliable for algebra -- zero added latency (in-prompt),
#               unlike a slow second API pass. NOTE: the LIVE switch is the Render env
#               var CLAUDE_MODEL=claude-haiku-4-5 (env overrides this default).
#   2026-07-21  TOPIC MODE (part of the new "what would you like to do today?" hub).
#               Added TOPIC_SYSTEM_PROMPT_TEMPLATE + get_topic_reply(): a focused
#               mini-lesson on ONE Algebra I topic the student picks/names (Socratic,
#               visual, always ends with a next step). Topic history is client-held
#               (not persisted), like Practice. Used by main.py's /api/topic.
#   2026-07-21  LESSON GOALS + PRACTICE MODE. (1) Each lesson now opens by stating a
#               one-sentence, level-matched GOAL and showing it on screen via a new
#               [[goal text="..."]] tag (returning sessions restate it too). (2) Added
#               a PRACTICE brain: PRACTICE_SYSTEM_PROMPT_TEMPLATE + get_practice_reply()
#               so a student can bring a specific problem from school and get Socratic
#               coaching on it (any Algebra I topic; practice history is client-held,
#               not persisted). Used by main.py's /api/practice.
#   2026-07-21  NEVER DEAD-END THE STUDENT. Mr. Cadabra sometimes ended a turn on a
#               plain statement, leaving the student staring at "Your turn!" with
#               nothing to do. Strengthened HOW YOU SPEAK: every reply must hand the
#               turn back with a clear next step -- a question, an explicit "your turn
#               -- try this", or a "ready for the next step?" check-in -- never a bare
#               statement.
#   2026-07-21  CARD-TAG SAFETY. The opening card is now a SHORT ready-made tag,
#               [[card id="cool-questions"]], instead of a long inline list -- the old
#               long tag could get cut off mid-stream, leaking raw "[[card ..." markup
#               into the spoken line (garbled) and leaving the whiteboard empty. Also
#               raised max_tokens 400 -> 700 so replies aren't truncated inside a tag.
#   2026-07-21  FLOW-AWARE OPENINGS. First lesson: the student has JUST finished the
#               placement challenge (and the app-driven welcome/tour), so the tutor
#               opens by acknowledging their placement level and teaches AT that
#               level -- no re-welcome/tour. Returning session: give a short spoken
#               RECAP of where they are, then continue (never re-run welcome/tour).
#   2026-07-21  TOUR IS NOW APP-DRIVEN + AUTO-PLAYS. The welcome, the one-line
#               definition of algebra, and the page walkthrough are now performed by
#               session.html as a scripted sequence (no per-step prompts), so the
#               tutor NO LONGER welcomes or tours. Its first message on a first
#               session starts the LESSON: the cool-questions card + the big idea.
#               Kept [[highlight]] documented but optional (tutor rarely needs it).
#   2026-07-20  ADDED THE OPENING PAGE TOUR. First meeting now: (1) welcome + a
#               one-sentence definition of algebra (finding an unknown number we
#               call a variable), (2) a quick guided TOUR of the screen -- one stop
#               per turn, lighting up each spot via a new [[highlight id="..."]]
#               control tag (curriculum -> find-my-level -> dashboard -> todays-plan
#               -> covered), then (3) the cool-questions card and the big idea. The
#               frontend glows the pointed-at element and scrolls it into view; the
#               spotlight clears at the start of the next turn. Documented the new
#               tag in the "SHOWING PICTURES" section.
#   2026-07-20  Cut the "get-to-know-you" opening (how do you feel about math /
#               hobbies -- it read as condescending). First meeting now opens with
#               ENERGY: welcome + why algebra is exciting + a card of cool things
#               it can solve, then straight into the big idea. Placement (from the
#               Challenge) handles "where is the student," so no upfront diagnosis.
#   2026-07-19  Renamed the tutor to "Mr. Cadabra"; first-meeting opener is now an
#               explicit warm "welcome to algebra."
#   2026-07-19  TONE REBUILD (research-backed). Added a "HOW YOU COME ACROSS"
#               section: talk WITH the student not down to them; cut empty/effort
#               praise (it backfires with teens and reads as patronizing); praise
#               SPECIFIC strategies; give agency/choices; be genuinely warm and a
#               little playful, not scripted; assume intelligence. Pairs with the
#               new ElevenLabs voice (see main.py /api/speak).
#   2026-07-19  RICHER ALGEBRA INTRO. Replaced the abrupt "an equation is a
#               see-saw" opening with a paced on-ramp: pose several cool real-life
#               QUESTIONS (answers unknown) -> we name unknowns with letters x/y
#               -> connect to equations + the equal sign they already know -> the
#               power to solve hard problems simply -> THEN the see-saw/balance.
#               Added a [[card title="..." items="a | b | c"]] control tag so the
#               tutor can show the list of cool questions on screen.
#   2026-07-19  VISUAL LESSON UPGRADE. Prompt now (a) goes slow and teaches what
#               an equation IS first (balance/see-saw + monkeys) before any x, and
#               (b) drives the on-screen animated balance scale and the plan/
#               covered sidebars by emitting hidden control tags:
#                 [[balance left="3 + 1" right="4" state="level" caption="..."]]
#                 [[covered id="what-is-equation"]]
#               The frontend renders these and strips them, so students only ever
#               hear plain words. Agenda ids: what-is-equation, balance-rule,
#               both-sides, one-step, two-step, check-answer.
#   2026-07-19  MAJOR TUTOR-BRAIN UPGRADE (research-backed). Rewrote the system
#               prompt so the tutor is warm, personable, and empathetic, and:
#                 - opens a FIRST session by building rapport (gets to know the
#                   student, how they feel about math, what they enjoy),
#                 - explains in plain, engaging terms what algebra IS and why it
#                   matters in real life,
#                 - DIAGNOSES how this student naturally thinks before teaching
#                   (e.g. "how would you figure this out in your head?"),
#                 - carries a toolkit of TEN different methods for solving a
#                   linear equation and adaptively finds which one clicks for
#                   THIS student, then leans into it,
#                 - treats mistakes as normal and useful and actively counters
#                   "I'm not a math person."
#               Grounded in tutoring/math-anxiety research (see project notes).
#               Note: the "learning styles (VAK)" idea is a debunked myth; this
#               prompt instead uses MULTIPLE REPRESENTATIONS and observes which
#               representation the student understands best -- which is the real,
#               evidence-based version of "different ways people learn."
#   2026-07-19  Updated DEFAULT_MODEL from the retired "claude-3-5-sonnet-latest"
#               to the current, active "claude-sonnet-5" (retired 2025-10-28).
#   2026-07-19  Initial version. Tutor brain: system prompt + context injection
#               + Claude API call. Model configurable via CLAUDE_MODEL env var.
#
# WHAT THIS FILE IS FOR:
#   This is the tutor's "brain." main.py imports get_tutor_reply() to answer a
#   student. SYSTEM_PROMPT_TEMPLATE below is the thing we revise most often as
#   real sessions teach us what works.
#
# ENV VARS (set these in Render, NOT in code):
#   ANTHROPIC_API_KEY   (required)  your Claude API key
#   CLAUDE_MODEL        (optional)  a CURRENT model id from Anthropic docs
# =============================================================================

import os
import re

from anthropic import Anthropic

# CANONICAL FOUNDATION SCRIPTS (2026-08-09, build cc). Defensive: if the module is
# missing on a deploy, lessons still run -- they just lose the verbatim introductions.
try:
    import foundations
except Exception as _exc:  # noqa: BLE001
    foundations = None
    print(f"[tutor] foundations.py unavailable ({_exc}) -- canonical intros disabled")

# The tutor's TEACHING KNOWLEDGE BASE (per-unit misconceptions + how-to-teach) and the
# unit CLASSIFIER. Imported defensively: if either module is somehow missing on deploy,
# the tutor must still answer (it just won't get the extra pedagogy that turn) -- do no
# harm. See pedagogy.py / curriculum.py.
try:
    import pedagogy
except Exception as _exc:  # noqa: BLE001
    pedagogy = None
    print(f"[tutor] pedagogy KB unavailable: {_exc}")
try:
    import curriculum
except Exception as _exc:  # noqa: BLE001
    curriculum = None
    print(f"[tutor] curriculum classifier unavailable: {_exc}")
# The MATH VERIFIER (2026-08-03): mathcheck.py re-does the tutor's math with SymPy before
# a reply ships (see _create_verified below). Imported defensively like the modules above:
# if it is missing the tutor still answers -- replies just aren't verified that deploy.
try:
    import mathcheck
except Exception as _exc:  # noqa: BLE001
    mathcheck = None
    print(f"[tutor] mathcheck unavailable -- replies will NOT be math-verified: {_exc}")
# USAGE LOGGING (2026-08-04): store.log_usage records what each paid call consumed (counts
# only, never text). Defensive like the imports above: no store, no logging, no harm.
try:
    import store
except Exception as _exc:  # noqa: BLE001
    store = None
    print(f"[tutor] store unavailable -- usage logging off: {_exc}")


def subsystems() -> dict:
    """Which of this module's defensive imports actually loaded (build ha). False means
    that capability is silently OFF on this deploy -- a broken mathcheck.py used to ship
    an unverified tutor indistinguishable from a healthy one. /health reports this."""
    return {"mathcheck": mathcheck is not None, "store": store is not None,
            "foundations": foundations is not None, "pedagogy": pedagogy is not None,
            "curriculum": curriculum is not None, "notation": notation is not None,
            "misconceptions_playbook": misconceptions is not None}


def _event(kind: str, name: str, detail: str = "", code: str = "", course: str = "") -> None:
    """Count one health event (build ha -- EYES). The 2026-08-17 review's meta-finding:
    ~19 fail-open handlers reported crashes to stdout only, so a dead referee and a
    healthy one looked identical. Every referee FIRE, every referee CRASH, every
    pass-through and probe observation now writes one row to store.system_events.
    Never raises, never slows a turn, no-ops when the store is off."""
    try:
        if store is not None:
            store.record_event(kind, name, str(detail or "")[:300], code, course)
    except Exception:  # noqa: BLE001 -- telemetry must never harm a lesson
        pass

# The default course. Until the course picker (Phase 3 UI) supplies a course, everything
# resolves to Algebra I, so single-course behavior is exactly as before.
DEFAULT_COURSE = "algebra1"

# -----------------------------------------------------------------------------
# THE WORDS MOVED OUT (2026-08-11, build do). Every system-prompt template and
# shared prompt block -- the text the teaching brain actually reads -- now lives in
# prompts.py, moved there VERBATIM and proven byte-identical (52 built prompts
# hashed before/after). This file keeps the ENGINE: the API calls, the negotiated
# continuation, mathcheck, the nine-referee prose sweep, and the builders below
# that assemble prompts.py's text into each request. The import re-exports every
# moved name, so tutor.GRAPH_TOOL_NOTE etc. still work (ruletests relies on that).
# Editing the WORDS? -> prompts.py. Editing the MACHINERY? -> here.
# -----------------------------------------------------------------------------
from prompts import (  # noqa: E402
    TUTOR_NAME,
    SYSTEM_PROMPT_TEMPLATE, GEOMETRY_SYSTEM_PROMPT_TEMPLATE,
    PREALGEBRA_SYSTEM_PROMPT_TEMPLATE, ALGEBRA2_SYSTEM_PROMPT_TEMPLATE,
    PRECALC_SYSTEM_PROMPT_TEMPLATE, PROBSTAT_SYSTEM_PROMPT_TEMPLATE,
    CALCULUS_SYSTEM_PROMPT_TEMPLATE, DIFFEQ_SYSTEM_PROMPT_TEMPLATE,
    ELEMENTARY_SYSTEM_PROMPT_TEMPLATE, LESSON_TEMPLATES,
    GROUND_RULES, GRAPH_TOOL_NOTE,
    SESSION_OPENER_RULES, PROGRESS_TAGS_NOTE,
    FINAL_PREP_NOTE, FINAL_EXAM_NOTE,
    COURSE_SUBJECT, PRACTICE_SCOPE, TOPIC_SCOPE,
    PRACTICE_SYSTEM_PROMPT_TEMPLATE,
    ASSESSMENT_SYSTEM_STUDENT, ASSESSMENT_SYSTEM_PARENT,
    TOPIC_SYSTEM_PROMPT_TEMPLATE,
)

# The STUDENT-FACING model. Configurable via env (CLAUDE_MODEL) so we never have to
# touch code to change it. This must be a CURRENT alias from Anthropic's docs --
# retired/guessed ids are rejected by the API.
# 2026-07-23: switched the student-facing brain to the stronger "claude-sonnet-5"
# (Sonnet 5). Teaching JUDGMENT -- knowing when to push vs. show, reading a student,
# adapting on the fly -- is exactly where a stronger model is dramatically better, and
# the whole app is still in DEVELOPMENT (no live students yet), so we tune for teaching
# quality now and can revisit per-student cost before launch. (Haiku 4.5 was the prior
# cheap choice; we can drop back to it for production if Sonnet-with-real-pedagogy proves
# more than we need.)
# IMPORTANT: the Render env var CLAUDE_MODEL OVERRIDES this default. To go live on
# Sonnet, set CLAUDE_MODEL=claude-sonnet-5 in Render (or delete the var so this default
# is used).
DEFAULT_MODEL = "claude-sonnet-5"

# BUILD ht (2026-08-18, Phase 5 -- review Class F): THE UPSTREAM CALL IS BOUNDED.
# The SDK's default timeout is ~10 minutes, and a hung upstream used to freeze a
# child for all of it -- the page just said "thinking". Every Anthropic client is
# now built with this timeout and ONE transport retry; a slow-but-working reply
# still lands (real replies take seconds), a HUNG one becomes the friendly
# try-again message in under two minutes, and the pages' own fetch abort (same
# build) is the outer guarantee. Env-tunable without a deploy.
ANTHROPIC_TIMEOUT_S = float(os.environ.get("ANTHROPIC_TIMEOUT_S", "60") or 60)

# How many past messages we replay to the model each request. Keeps the "tutor
# remembers" feeling while bounding token cost (one message = one turn).
MAX_HISTORY_MESSAGES = 30


def _cacheable_system(text: str):
    """Wrap a system prompt as ONE cacheable content block so Anthropic PROMPT CACHING can reuse the
    large, mostly-stable system prompt across a student's consecutive turns instead of re-billing it
    every turn. This is billing/latency ONLY -- the model's output is identical whether or not the
    prefix was cached, so there is NO change in teaching quality. (Added 2026-07-30.)"""
    return [{"type": "text", "text": text or "", "cache_control": {"type": "ephemeral"}}]


try:
    # 2026-08-09 (build cj): the notation registry. Defensive, exactly like foundations:
    # a broken notation.py must never take the classroom down.
    import notation
except Exception as _nexc:  # noqa: BLE001
    notation = None
    print(f"[tutor] notation.py unavailable ({_nexc}) -- continuing without the symbol table")


try:
    # 2026-08-10 (build ck): the misconception catalogue. Defensive, like the others.
    import misconceptions
except Exception as _mexc:  # noqa: BLE001
    misconceptions = None
    print(f"[tutor] misconceptions.py unavailable ({_mexc}) -- continuing without it")


def _misconception_block(course: str) -> str:
    """This course's catalogue of the wrong RULES students run (rule 49), or "".
    Never raises: a broken misconceptions.py must not take the classroom down."""
    if misconceptions is None:
        return ""
    try:
        return misconceptions.prompt_block(course)
    except Exception as exc:  # noqa: BLE001
        print(f"[tutor] misconception block failed ({exc}) -- continuing without it")
        return ""


def _notation_block(course: str) -> str:
    """The per-course 'HOW TO SAY WHAT YOU WRITE' table (rule 48), or "".

    Rule 48 tells him to read every symbol aloud and to deny the wrong reading by name.
    Until this block existed it never told him OUR readings -- the same mistake as
    telling him to skip an introduction he had no way to identify. Never raises."""
    if notation is None:
        return ""
    try:
        return notation.prompt_block(course)
    except Exception as exc:  # noqa: BLE001
        print(f"[tutor] notation block failed ({exc}) -- continuing without it")
        return ""


# build gf (2026-08-14): FILTERING IS NOT OPTIONAL. ruletests caught this within an hour of
# build gb shipping: when no unit can be determined -- an unplaced student, or a practice
# problem the classifier cannot place -- unit was None, prompt_block filtered NOTHING, and
# algebra2 came out at 185,595 characters against a 180,000 ceiling. Every measurement taken
# during build gb passed an explicit unit, so every measurement missed it.
# A student with no placement is at the START of the course, so unit 1 is the honest default
# rather than a guess; practice and topic prefer the student's own placed unit and fall back
# to the same 1. Nothing is ever lost by filtering: the other units' terms are still NAMED.
_FILTER_UNIT_FALLBACK = 1

def _foundation_block(course: str, heard=None, verbatim: bool = True, unit=None) -> str:
    """This course's canonical foundation scripts (rules 36-40), or "" if none.

    `heard` is the list of terms this student was introduced to on an EARLIER visit
    (main.py loads it from the store and puts it on the student record). It only
    changes whether the tutor replays a script or asks first -- never the words.
    Never raises: a broken foundations.py must not take the classroom down."""
    if foundations is None:
        return ""
    try:
        return foundations.prompt_block(course, heard, verbatim, unit)
    except TypeError:
        # An older foundations.py without `unit` (build gb) -- still teach, unfiltered.
        try:
            return foundations.prompt_block(course, heard, verbatim)
        except TypeError:
            pass
        # An older foundations.py without the `heard` argument: still teach.
        try:
            return foundations.prompt_block(course)
        except Exception as exc:  # noqa: BLE001
            print(f"[tutor] foundation block failed ({exc}) -- continuing without it")
            return ""
    except Exception as exc:  # noqa: BLE001
        print(f"[tutor] foundation block failed ({exc}) -- continuing without it")
        return ""


# THE PROMPT CEILING HAS ONE DEFINITION (2026-08-17, build gz). It used to live only in
# ruletests.py, measured against a FRESH test student -- and a returning student who had
# heard every foundation script assembled to 186,890-194,284 characters on every course,
# over the ceiling, silently, in production. (Second occurrence of this miss class: build
# gf shipped 185,595 the same way.) The number now lives HERE, the serving path checks it
# on every assembly, and ruletests imports it instead of declaring its own copy.
# 2026-08-18 (build hr): RAISED 180,000 -> 181,000. Rule 32(b) (the one-unit story
# clause, written from the night watch's first confirmed catch) rides the shared rules
# block into every course, and the all-heard algebra2 DEFERRED prompt tripped the wire
# at 180,176. Raised deliberately rather than by trimming teaching, under Jim's standing
# authorization (2026-08-11, Four_Lens_Review: "if you need to raise it, you raise it"
# -- each raise gets its own change note; this is that note). Still a tripwire, not a
# licence -- and the honest measurement now EXISTS: build hq's two-prompt-sizes
# experiment (lessonaudit --prompt-size) is queued for Jim to run, and its result
# should set this number from evidence.
# 2026-08-18 (builds hz/ia/ib/ic): RAISED 181,000 -> 184,000. One day of live
# catches wrote rule 63(d)/(e) and rule 47(e)/(f)/(g) plus their figure teaching
# into the shared rules block, and the all-heard algebra2 deferred prompt measured
# 182,828. Same authorization, same discipline as the hr raise: teaching is never
# trimmed to duck a tripwire, and each raise gets its own dated note (this is it).
# Jim's queued two-prompt-sizes run remains the evidence that should set this
# number properly.
PROMPT_CEILING = 184_000


def build_system_prompt(student: dict, course: str = DEFAULT_COURSE) -> str:
    """Fill the right course's lesson template with this student's name + remembered progress.

    build gz (2026-08-17): THE CEILING IS ENFORCED AT ASSEMBLY TIME. If the finished
    prompt exceeds PROMPT_CEILING, it is reassembled with the heard-script wording
    DEFERRED -- the exact mechanism build cl built and build cn kept dormant with the
    words "it becomes the right answer if the library ever grows to where it does not
    fit." It has (all four courses overflow for an all-heard student), so for those
    students only, heard scripts are OFFERED by name and their wording is restored the
    moment they accept (main.py sets foundations_force_verbatim on refresher turns via
    foundations.wants_refresher). Students under the ceiling see a byte-identical prompt
    to yesterday's -- nothing changes for them, and the cache stays warm."""
    name = (student or {}).get("name", "the student")
    progress = (student or {}).get("progress") or ""
    progress = progress.strip()
    if not progress:
        progress = ("(No prior sessions yet -- this is your FIRST meeting with "
                    "this student. Begin with the first-meeting flow.)")
    # Phase B: prefer a chosen FOCUS unit (from the dashboard "Work on it" link) for the
    # teaching playbook; otherwise detect it from the placement note in progress.
    # build hj: the server resolves "which unit" ONCE (main._resolve_unit) and passes
    # it as a FIELD. The regex-the-prose path below survives only as a fallback for
    # callers that predate the field (nightwatch drives this function directly with
    # synthetic students) -- when current_unit is present, no prose is ever parsed.
    unit = None
    try:
        cu = int((student or {}).get("current_unit") or 0)
        if 1 <= cu <= 9:
            unit = cu
    except (TypeError, ValueError):
        unit = None
    if unit is None:
        focus = (student or {}).get("focus_unit")
        try:
            focus = int(focus) if focus else None
        except (TypeError, ValueError):
            focus = None
        unit = focus if (focus and 1 <= focus <= 9) else _unit_from_progress(progress)
    playbook = _playbook(unit, course)
    mastery = (student or {}).get("mastery_note") or "(No mastery data yet -- begin at their placed level.)"
    template = LESSON_TEMPLATES.get(course or DEFAULT_COURSE, SYSTEM_PROMPT_TEMPLATE)
    heard = (student or {}).get("foundations_heard")
    verbatim = (student or {}).get("foundations_verbatim", True)
    # A refresher turn ("remind me what a radius is" / accepting the rule-40 offer) must
    # carry the exact words even for an over-ceiling student -- one over-budget turn is
    # the price of the promise "the exact script is restored the moment they ask".
    force_verbatim = bool((student or {}).get("foundations_force_verbatim"))
    # FINAL EXAM MODES (2026-08-07): main.py sets student["final_mode"] ONLY after verifying
    # server-side that all nine units are mastered -- never trust the client for this.
    final_mode = (student or {}).get("final_mode") or ""

    def _assemble(carry_heard_wording: bool) -> str:
        p = GROUND_RULES + GRAPH_TOOL_NOTE + template.format(
            tutor_name=TUTOR_NAME,
            student_name=name,
            progress=progress,
            playbook=playbook,
            mastery=mastery,
        ) + SESSION_OPENER_RULES + PROGRESS_TAGS_NOTE + _notation_block(course) + _misconception_block(course) + _foundation_block(
            course, heard, carry_heard_wording,
            unit or _FILTER_UNIT_FALLBACK)   # build gb: only THIS unit's scripts carry their wording
        if final_mode == "prep":
            p += FINAL_PREP_NOTE
        elif final_mode == "exam":
            p += FINAL_EXAM_NOTE
        return p

    prompt = _assemble(verbatim)
    if len(prompt) > PROMPT_CEILING and verbatim and not force_verbatim and heard:
        slim = _assemble(False)
        print(f"[promptsize] {course}: {len(prompt):,} chars exceeds the "
              f"{PROMPT_CEILING:,} ceiling -- deferring heard-script wording "
              f"(build cl mechanism) -> {len(slim):,} chars")
        _event("promptsize", "deferred", f"{course}: {len(prompt)} -> {len(slim)}",
               course=course)
        prompt = slim
    if len(prompt) > PROMPT_CEILING:
        # Still over (or a refresher turn deliberately carrying the words): say so
        # LOUDLY every time. A silent overflow is how this shipped twice before.
        print(f"[promptsize] OVER CEILING: {course}: {len(prompt):,} chars "
              f"(ceiling {PROMPT_CEILING:,}; force_verbatim={force_verbatim})")
        _event("promptsize", "over-ceiling",
               f"{course}: {len(prompt)} (force_verbatim={force_verbatim})", course=course)
    return prompt


def _trim_history(history: list) -> list:
    """Return at most the last MAX_HISTORY_MESSAGES messages, oldest first."""
    if not history:
        return []
    return history[-MAX_HISTORY_MESSAGES:]


# -----------------------------------------------------------------------------
# TEACHING PLAYBOOK INJECTION -- give the tutor real pedagogy for THIS student's unit
# -----------------------------------------------------------------------------
# We figure out which Algebra I unit the student is on, then pull that unit's
# misconceptions + how-to-teach (plus the universal methodology) from pedagogy.py and
# drop it into the system prompt. Every step is wrapped so a failure never breaks a turn.
def _unit_from_progress(progress) -> "int | None":
    """The lesson stores the placed unit in the progress note as 'Unit N'. Read it."""
    try:
        m = re.search(r"\bUnit\s+(\d+)", str(progress or ""))
        return int(m.group(1)) if m else None
    except Exception:  # noqa: BLE001
        return None


def _lesson_unit(student) -> "int | None":
    """The unit the SERVER puts this student in: an explicit focus unit, else the unit in
    their progress note. build_system_prompt derives the teaching playbook from exactly
    these two inputs, so the referee and the prompt can never disagree about where the
    student is (build gn). Returns None when neither says -- and the referee then stays
    silent rather than guessing."""
    try:
        # build hj: the resolved field first -- the SAME value build_system_prompt
        # used, so the referee and the prompt still cannot disagree (the gn property,
        # now via one server-side derivation instead of one shared regex).
        cu = int((student or {}).get("current_unit") or 0)
        if 1 <= cu <= 9:
            return cu
        focus = (student or {}).get("focus_unit")
        try:
            focus = int(focus) if focus else None
        except (TypeError, ValueError):
            focus = None
        if focus and 1 <= focus <= 9:
            return focus
        return _unit_from_progress((student or {}).get("progress") or "")
    except Exception:  # noqa: BLE001
        return None


def _unit_from_text(text, course: str = DEFAULT_COURSE) -> "int | None":
    """Classify a free-text problem/topic to a unit WITHIN a course (practice + topic modes)."""
    try:
        if curriculum and text:
            unit, _name = curriculum.classify_unit(text, course)
            return unit
    except Exception:  # noqa: BLE001
        pass
    return None


def _playbook(unit, course: str = DEFAULT_COURSE) -> str:
    """The teaching guidance to inject this turn (or '' if the KB is unavailable)."""
    try:
        if pedagogy:
            return pedagogy.teaching_playbook(unit, course)
    except Exception as exc:  # noqa: BLE001
        print(f"[tutor] playbook build failed: {exc}")
    return ""


# =============================================================================
# WHITEBOARD SAFETY NET -- the backend GUARANTEES the board shows the math
# =============================================================================
# The main model (Haiku) does not reliably emit whiteboard control tags even when the
# system prompt demands it. So after every reply we check: did the tutor draw the math?
# If the reply talks math but has no board tag, a focused second model call converts the
# current math into ONE tag and we append it. Wrapped so any failure is a silent no-op.
_BOARD_TAG_RE = re.compile(r"\[\[\s*(balance|machine|graph|card|write|solve|clear)\b", re.I)
_MATH_HINT_RE = re.compile(
    r"[0-9]\s*[-+=]|[0-9]\s*x\b|\bx\s*[-+=]|"
    r"\b(equals?|equation|plus|minus|times|divide[sd]?|dividing|subtract|multipl|"
    r"solve|solving|squared?|slope|intercept|graph|function|variable|f of)\b", re.I)

BOARD_TAG_SYSTEM = """\
You turn a math tutor's spoken message into ONE hidden whiteboard control tag that shows
ONLY the math that has ALREADY been established in the conversation -- never math the
student has not reached yet. The tutor speaks in words (e.g. "two x plus one equals
eleven"); you output SYMBOLIC math inside a tag. Use lowercase x and y for variables.

⛔ THE ONE RULE THAT MATTERS MOST -- NEVER RUN AHEAD OF THE STUDENT.
The board must never reveal a step the tutor is currently ASKING the student to find. Read
the tutor's message: if it hands the next step to the student -- a question or a "your turn"
like "what should we do first?", "what's the next step?", "your turn -- try it", "what do
we get?", "can you solve for x?" -- then you must NOT compute or show that step. Show only
the equation AS IT STANDS right now (the starting equation, or the steps already worked out
together), and stop there. Do the SAME arithmetic the tutor has actually spoken -- never
solve further than the conversation has gone. When in doubt, show LESS, not more.

Pick exactly ONE tag:
- SOLVING an equation -- show ONLY the steps already completed together (starting equation
  on top, then each FINISHED step as "operation : resulting equation"):
    [[solve start="2x + 1 = 11" steps="subtract 1 from both sides : 2x = 10" caption="solve for x"]]
  Include ONLY steps the tutor has already stated as done. If they are still on the starting
  equation -- the tutor just posed it, or is asking what to do first -- use the start with an
  EMPTY steps list (this shows just the one line, spoiling nothing):
    [[solve start="2x + 1 = 11" steps="" caption="solve for x"]]
- A single equation / expression / function definition (not a solve in progress):
    [[write lines="f(x) = 2x + 1 | 2x + 1 = 15"]]
- Evaluating a function at a value the tutor has already stated:
    [[machine input="4" rule="2x+1" output="9" fname="f"]]
- A straight line or parabola the tutor has already stated:
    [[graph lines="y=2x+1"]]

Output ONLY the tag -- no other words. If there is genuinely NO specific equation, number
sentence, expression, or function that has been stated yet, output exactly: NONE"""


def board_tag_for(tutor_message: str, user_message: str = "", history=None) -> str:
    """Focused second call: return ONE whiteboard tag for the current math, or ""."""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return ""
    model = os.environ.get("CLAUDE_MODEL", DEFAULT_MODEL)
    ctx = ""
    for m in (history or [])[-4:]:
        who = "Tutor" if m.get("role") == "assistant" else "Student"
        ctx += who + ": " + str(m.get("content", ""))[:300] + "\n"
    user = ("Recent conversation:\n" + ctx +
            "Student just said: " + (user_message or "(nothing)") + "\n"
            "Tutor just said (out loud): " + tutor_message + "\n\n"
            "Output the ONE whiteboard tag for the math being worked right now, or NONE.")
    client = Anthropic(api_key=api_key, timeout=ANTHROPIC_TIMEOUT_S, max_retries=1)
    resp = client.messages.create(model=model, max_tokens=220, system=BOARD_TAG_SYSTEM,
                                  messages=[{"role": "user", "content": user}])
    out = "".join(b.text for b in resp.content if getattr(b, "type", None) == "text").strip()
    if not out or out.upper().startswith("NONE"):
        return ""
    hit = re.search(r"\[\[[\s\S]*\]\]", out)
    return hit.group(0) if hit else ""


def ensure_board(reply: str, user_message: str = "", history=None) -> str:
    """RETIRED (Stage 2, 2026-07-23): now a pass-through -- the tutor drives the board itself.

    Why retired: the whiteboard is now a PERSISTENT worklist that stacks and stays, and the
    student-facing brain is claude-sonnet-5, which reliably emits the [[step]] tags the prompt
    asks for. The old behavior here was a SECOND model call (board_tag_for) that GUESSED a tag
    whenever it thought math went undrawn -- and that guessing was the source of two real bugs:
    it answered the very step the tutor was asking the student to find, and it redrew the whole
    problem on a 'check' turn. With a persistent board, a missed tag just means 'no new line
    this turn' (the earlier lines stay up), so the net is no longer needed and did more harm
    than good. board_tag_for / BOARD_TAG_SYSTEM above are kept but UNUSED, so re-enabling a net
    later is a one-line change if we ever want one back.
    """
    return reply


# -----------------------------------------------------------------------------
# TODAY-BAR SAFETY NET (2026-08-08, build bo, Jim's screenshot: a Pre-Algebra
# session showed the UNIT and COURSE bars but NO TODAY bar for the whole lesson --
# the opener emitted [[goal]] and the goals card but skipped the [[today items]]
# tag the PROGRESS BARS note asks for, so the top bar never rendered).
# Unlike the retired ensure_board net above, this one NEVER GUESSES: it copies the
# goal items the model itself just wrote (the "By the end you'll be able to" card,
# falling back to the [[goal]] banner text) into the [[today]] tag verbatim --
# exactly the tag the prompt told the model to emit. It fires only when this reply
# announces goals, has no [[today]] of its own, AND no [[today]] was ever emitted
# earlier in the session (so it can never reset a live bar mid-lesson).
# Lesson mode only (the today bar exists only on the lesson page).
# -----------------------------------------------------------------------------
_GOALS_CARD_RE = re.compile(r'\[\[\s*card\s+title="By the end[^"]*"\s+items="([^"\]]+)"', re.I)
_GOAL_BANNER_RE = re.compile(r'\[\[\s*goal\s+text="([^"\]]+)"', re.I)


def ensure_today_tag(reply: str, history=None, today_live: bool = False) -> str:
    """`today_live` (2026-08-09, build cg) = the SERVER already has today's goal bar
    stored for this student and course, so the page can render it without help.

    That flag replaced a bad assumption. The history guard below reads "a [[today]] was
    emitted earlier, so a bar is already up -- do not reset it." True inside one sitting;
    FALSE across a page load, which is exactly where Jim kept losing the bar: history
    still held yesterday's tag, the net stood down, and the reloaded page had no bar at
    all. Now history only silences the net when the bar genuinely still exists."""
    if re.search(r"\[\[\s*today\b", reply, re.I):
        return reply                                   # model did its job
    if today_live:
        for msg in (history or []):
            if msg.get("role") == "assistant" and "[[today" in str(msg.get("content", "")):
                return reply                           # bar is really up -- never reset it
    m = _GOALS_CARD_RE.search(reply)
    items = m.group(1).strip() if m else ""
    if not items:
        g = _GOAL_BANNER_RE.search(reply)
        items = g.group(1).strip() if g else ""
    if not items:
        return reply                                   # no goals announced this turn -- nothing to mirror
    return reply.rstrip() + ' [[today items="' + items + '"]]'


# =============================================================================
# THE MATH VERIFIER HOOK (2026-08-03) -- shared by lesson, practice, and topic.
# -----------------------------------------------------------------------------
# mathcheck.py is the referee (SymPy actually re-does the math in the tutor's
# hidden [[verify]] tags -- see GRAPH_TOOL_NOTE rules 10-12). This helper is the
# loop around the model call:
#   generate -> verify -> (if a claim is provably wrong) tell the model exactly
#   what SymPy computed and SILENTLY regenerate -> strip the tags -> return.
# The student only ever sees the final, verified text. Fail-open on anything
# undecidable: an imperfect checker must never stall a child's lesson.
# Cost note: a retry is one extra model call and happens only when a real error
# was caught -- rare by design, and exactly the turn worth paying twice for.
# =============================================================================
# =============================================================================
# THE PROSE REFEREE (2026-08-09, build bu -- proactive audit #24)
# -----------------------------------------------------------------------------
# mathcheck.py re-computes the math inside the tutor's TAGS. It is deaf to PROSE --
# which is exactly how this shipped bug reached a live student (2026-08-08):
#     board:  [[step eq="dimes: 7 + 8 + 1 = 16"]]      (correct, and verified)
#     spoken: "Fifteen dimes -- so we write the five and carry a dollar."
# The student's wrong answer was adopted in words while the board said otherwise, and
# nothing could see it. Rule 18(b) tells the model not to do this; THIS is the net.
#
# It is deliberately NARROW, because a false positive silently throws away a good reply.
# It flags one unambiguous shape only -- the reply CONTRADICTS ITSELF about a labeled
# quantity, and its words never once say the number its own board concluded:
#   1. a board line in this reply reads "<label>: ... = R"   (R a plain number)
#   2. the spoken text says "<P> <label>"                    (P a numeral or number-word)
#   3. P != R
#   4. R appears NOWHERE in the spoken text (numeral or word)   <-- the discriminator
#   5. P is not an operand of that same board line
# Condition 4 is what makes this safe: a legitimate mention of an intermediate value
# lands on the right answer in the same breath ("fifteen dimes plus the carried one
# makes SIXTEEN") and is never flagged; an adopted wrong answer never says the correct
# number at all. Everything is wrapped so any surprise fails OPEN -- an imperfect
# referee must never stall a child's lesson.
# =============================================================================
_PR_ONES = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
            "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
            "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
            "eighteen": 18, "nineteen": 19}
_PR_TENS = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
            "seventy": 70, "eighty": 80, "ninety": 90}


def _pr_word_value(phrase: str):
    """'fifteen' -> 15, 'twenty-one' -> 21, 'one hundred eighty' -> 180. None if not a number."""
    words = re.split(r"[\s-]+", str(phrase).strip().lower())
    words = [w for w in words if w and w != "and"]
    if not words:
        return None
    total, current, seen = 0, 0, False
    for w in words:
        if w in _PR_ONES:
            current += _PR_ONES[w]; seen = True
        elif w in _PR_TENS:
            current += _PR_TENS[w]; seen = True
        elif w == "hundred" and seen:
            current *= 100
        else:
            return None
    return total + current if seen else None


_PR_NUMWORD = "(?:" + "|".join(sorted(list(_PR_ONES) + list(_PR_TENS), key=len, reverse=True)) + \
              r")(?:[\s-](?:hundred|" + "|".join(sorted(list(_PR_ONES) + list(_PR_TENS), key=len, reverse=True)) + r"))*"
# "<label>: <anything> = <number>"  -- the shape our own board rules ask for.
_PR_BOARD_LINE = re.compile(r"([A-Za-z][A-Za-z' ]{0,24}?)\s*:\s*([^=]{0,80}?)=\s*(-?\d+(?:\.\d+)?)\s*$")


def _pr_numbers_in(text: str) -> set:
    """Every number stated in `text`, numerals AND number-words, as floats."""
    out = set()
    for m in re.findall(r"-?\d+(?:\.\d+)?", text or ""):
        try:
            out.add(float(m))
        except ValueError:
            pass
    for m in re.findall(_PR_NUMWORD, (text or "").lower()):
        v = _pr_word_value(m)
        if v is not None:
            out.add(float(v))
    return out


# =============================================================================
# THE VISUAL-REFERENCE CHECK (2026-08-09, build ce) -- half of the prose referee.
# -----------------------------------------------------------------------------
# Jim, on the demo: "the lesson referred to a diagram that didn't show up on the
# board... We got one shot to do it right, and it failed."
#
# Rule 7 has forbidden this in WORDS since build ao. Nothing has ever CHECKED it.
# mathcheck reads tags. prose_board_conflict (below) compares spoken NUMBERS with
# written numbers. A reply that says "here's a number line" and emits no
# [[numberline]] passes every referee we own, and the student sits in front of a
# blank board listening to a description of nothing.
#
# The check is deliberately narrow, because a false positive costs a real model
# call: it fires only when a sentence BOTH names something the board can draw AND
# claims, in the present tense, that it is appearing right now. "A number line has
# zero in the middle" is fine. "Here's a number line" with nothing drawn is not.
# Anything it is unsure about, it lets through -- like every referee here, it fails
# open, because a checker must never brick a lesson.
# =============================================================================

# Tags that put a PICTURE on the board. Kept as a constant (tutor.py must not read
# static files at request time); ruletests.py PART 3c asserts this list still matches
# session.html's handleTags(), so it cannot silently drift out of date.
# build hh: THE TAG GRAMMAR HAS ONE SOURCE -- tags.py. This import is deliberately
# NOT defensive: tags.py is pure data with no logic, and "the referees silently
# forgot what a tag is" must stop the deploy at boot, not degrade in the dark.
import tags as _tagreg
FIGURE_TAGS = tuple(_tagreg.FIGURE_TAGS)
# Every tag that puts ANYTHING on the board, picture or writing.
_BOARD_TAGS = tuple(_tagreg.BOARD_TAGS)

# Nouns the board can DRAW. Bare "triangle"/"circle" are deliberately absent: they
# appear in ordinary mathematical prose far too often to judge from one sentence.
_VIS_NOUN = (r"(?:number ?line|graph|diagram|picture|drawing|sketch|figure|chart|plot|"
             r"histogram|scatter ?plot|box ?plot|dot ?plot|bar chart|bar graph|pie chart|"
             r"unit circle|area model|tape diagram|tree diagram|balance scale|"
             r"function machine|right triangle)")
# Phrases that claim it is appearing NOW (not "we could draw one", not "last time").
_VIS_CUE = (r"(?:here'?s|here is|here are|i'?ve drawn|i have drawn|i drew|i just drew|"
            r"i'?m drawing|i am drawing|i'?m putting|i am putting|let me draw|let me sketch|"
            r"let me graph|let me plot|let me put|i'?ll draw|i will draw|i'?ll sketch|"
            r"i'?ll graph|i'?ll plot|look at (?:the|this)|take a look at|notice (?:the|this)|"
            r"see (?:the|this)|watch (?:me|as i)|on the board|on screen|below|above|"
            r"this shows|these show)")
_VIS_SENT = re.compile(_VIS_CUE + r"[^.!?]{0,60}?" + _VIS_NOUN, re.I)
_VIS_SENT_REV = re.compile(_VIS_NOUN + r"[^.!?]{0,40}?" + r"(?:below|above|on the board|on screen)", re.I)
# "look at the board" / "up on the screen" -- needs SOMETHING written, not a picture.
_VIS_BOARD_ONLY = re.compile(r"(?:look at|take a look at|see|check|glance at)\s+"
                             r"(?:the|your|our)\s+(?:board|screen|whiteboard)", re.I)
# A sentence that DEFERS the drawing, or asks whether to draw, or points BACK at an
# earlier one, is not a claim that a picture is on the board right now. Without this
# guard the referee re-rolls perfectly good replies -- and every re-roll is a real
# model call, so a false positive is not free.
_VIS_DEFER = re.compile(
    r"\b(?:next time|later|tomorrow|next session|another day|in a (?:minute|second|moment|bit)|"
    r"want me to|would you like|should i|shall i|do you want|if you(?:'d| would) like|"
    r"we could|we can|i could|remember|last time|yesterday|earlier|before|"
    r"we (?:used|drew|made|had)|you (?:drew|made)|back when)\b", re.I)


def _vis_sentences(prose: str):
    """The spoken text as sentences, so a claim is judged in its own context."""
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+|\n+", str(prose or "")) if s.strip()]


def _spoken_only(text: str) -> str:
    """The words the student actually HEARS: control tags removed, including a
    dangling one from a reply that was cut off mid-tag."""
    prose = re.sub(r"\[\[[^\]]*\]\]", " ", str(text or ""))
    return re.sub(r"\[\[[\s\S]*$", " ", prose)


def _tags_present(text: str, names) -> bool:
    """True if the reply emits at least one tag from `names`."""
    found = {m.lower() for m in re.findall(r"\[\[\s*([\w-]+)", str(text or ""))}
    return bool(found & set(names))


# Rules 2 and 8 are the same shape as rule 7 from the other side: the student ASKED to
# see something ("show me", "can I see a picture", "draw it"), or the tutor is narrating
# a CHANGE that ought to be shown happening. Both end with a student looking at a board
# that has nothing new on it. Added build co, when the rule index made it plain these
# were the only two rules in the whole prompt that nothing checked at all.
_VIS_ASKED = re.compile(
    r"\b(?:show me|can i see|could i see|let me see|draw (?:it|one|that|me)|"
    r"can you draw|would you draw|picture of (?:it|that))\b", re.I)
_VIS_PROMISE = re.compile(
    r"\b(?:here'?s|here is|let me|i'?ll|i will|watch)\b[^.!?]{0,40}"
    r"\b(?:show|draw|sketch|graph|plot)\b", re.I)


def prose_asked_to_see(student_message: str) -> bool:
    """Did the student just ask to be SHOWN something? (rules 2 and 8)"""
    try:
        return bool(_VIS_ASKED.search(str(student_message or "")))
    except Exception:  # noqa: BLE001
        return False


def prose_visual_conflict(reply: str, student_message: str = ""):
    """Return a description of a picture that was promised and never drawn, or "".

    `student_message` (build co) lets this also enforce rules 2 and 8: if the student
    ASKED to see something, this reply must draw something, full stop -- re-drawing is
    free and always right, so there is no legitimate reason to answer "show me" with a
    board that gains nothing.
    Never raises: any unexpected input yields "" (fail open)."""
    try:
        text = str(reply or "")
        prose = _spoken_only(text)
        if prose_asked_to_see(student_message) and not _tags_present(text, _BOARD_TAGS):
            return ('the student just asked to SEE something and this reply puts nothing '
                    'on the board at all. Rule 2: "show me" / "can I see" / "draw it" '
                    'means your reply MUST include the figure or board tag, even if '
                    'something similar is already up -- re-drawing is free and always '
                    'right.')
        if not _tags_present(text, _BOARD_TAGS):
            # Same guard as the rest of this referee: "next time I'll draw you one" is a
            # promise about later, not a claim about now. (Caught by the battery the
            # moment rule 8 was added -- the deferral case was already a fixture.)
            for sent in _vis_sentences(prose):
                if _VIS_DEFER.search(sent):
                    continue
                if _VIS_PROMISE.search(sent):
                    return ('you say you are going to show or draw something and then '
                            'draw nothing. Rule 8: show the change, do not describe it.')
        sentences = _vis_sentences(prose)
        if not _tags_present(text, FIGURE_TAGS):
            for sent in sentences:
                if _VIS_DEFER.search(sent):
                    continue                      # "next time I'll draw one" is not a claim
                for rx in (_VIS_SENT, _VIS_SENT_REV):
                    m = rx.search(sent)
                    if m:
                        said = " ".join(m.group(0).split())[:70]
                        return ('you say "{s}" but this reply draws NO figure at all -- the '
                                'student is looking at a board with no picture on it while '
                                'you talk about one. Rule 7: never describe a picture you '
                                'did not draw.').format(s=said)
        if not _tags_present(text, _BOARD_TAGS):
            for sent in sentences:
                if _VIS_DEFER.search(sent):
                    continue
                m = _VIS_BOARD_ONLY.search(sent)
                if m:
                    said = " ".join(m.group(0).split())[:70]
                    return ('you say "{s}" but this reply puts NOTHING on the board -- no '
                            'figure, no written line. Rule 7: never point at a board you '
                            'did not write on.').format(s=said)
        return ""
    except Exception as exc:  # noqa: BLE001 -- referee crash = fail open, always
        print(f"[viscHeck] crashed (fail open): {exc}")
        _event("referee_crash", "viscHeck", str(exc))
        return ""


# =============================================================================
# THE PENDING-QUESTION CHECK (2026-08-09, build cg) -- third part of the referee.
# -----------------------------------------------------------------------------
# Jim, on a live Pre-Algebra resume: "it gave me a problem without putting it on the
# board, and this is the exact example that we've already used once before that was
# supposedly fixed. And I don't understand why it's not fixed."
#
# He is right, and the reason is worth writing down. Rule 15 does not just forbid this
# in general -- it names THIS EXACT SCENARIO, quotes the column-addition lesson, and
# prints the fix ([[step eq="dollars: 2 + 1 + 1 = ?"]]). It has said so since build bm.
# The reply still went out with "what's two plus one plus one?" spoken and no board
# line, because a rule in a prompt is guidance, not a guarantee. So this stops being a
# rule and becomes a referee: ask the student to compute something, and if the board
# shows no pending line in that same reply, the draft is thrown away and rewritten.
#
# Narrow on purpose (a false positive costs a real model call): it fires only on a
# question that asks for a COMPUTATION -- two or more numbers, or an operator word and
# a number -- so "ready to try one?", "does that click, or should I show it another
# way?" (rule 39d) and "how are you doing today?" are all untouched. Number WORDS count,
# because the tutor speaks in words ("what's two plus one plus one?").
# =============================================================================
# Operator WORDS only. A bare "-" or "/" must never count: "three-fourths" and "1/2" are
# single values, and treating their punctuation as an operator made the very first test
# run flag "which number is the denominator in three-fourths?" as a computation.
_PQ_OPERATOR = (r"\b(?:plus|minus|times|multiplied by|divided by|add|adds|added|subtract|"
                r"subtracted|multiply|multiplied|divide|divided|sum of|product of|"
                r"difference between|square root of|percent of)\b")
# A written arithmetic expression counts on its own: digit, operator, digit. The
# unambiguous operators (+ × ÷) count tight or spaced; "-", "*" and "/" only count when
# they are SPACED, because "1/2" and "3-4" are single values, not operations. (Caught on
# the second test run: "is 1/2 bigger than the piece we shaded?" was being read as
# arithmetic.)
_PQ_SYMBOL_EXPR = re.compile(r"\d\s*[+×÷]\s*\d|\d\s+[\-*/]\s+\d")
# tags whose text can carry the pending "?" line rule 15 asks for
_PQ_BOARD_TAGS = tuple(_tagreg.PENDING_BOARD_TAGS)   # build hh: one source (tags.py)
# The equation-carrying tags the rule-18b sweep reads labelled conclusions from,
# compiled once from the registry (build hh -- this was an inline hand-typed
# step|write|solve in the hot path).
_STEP_TAG_RE = re.compile(
    r"\[\[\s*(?:" + "|".join(_tagreg.STEP_TAGS) + r")\b([^\]]*)\]\]", re.I)

# BUILD dg (2026-08-11): TWO FALSE-POSITIVE CLASSES, FOUND IN THE FIRST FULL AUDIT'S
# RENDER LOGS. This referee killed good drafts a dozen times in forty minutes, and one
# geometry lesson shipped WITHOUT its worked example because the drafts that contained
# it kept being discarded (Audit_Findings_2026-08-11.md, S-1 and L-3). The exact quoted
# misfires are permanent cases in ruletests.py. The two classes:
#   (a) OFFERS. "Want to try one yourself now, or see one more worked example first?"
#       asks the student's PREFERENCE, not for a computed answer. If they accept, the
#       problem goes up NEXT turn, where rule 15 applies in full force. Look-questions
#       ("See how the five sits under the four?") direct the eyes at a board that is
#       already drawn -- there is nothing pending to compute. ("See how MANY..." still
#       counts: that asks for a count, which is a computation.)
#   (b) THE PRONOUN "one". "try ONE more", "see ONE yourself" made offers read as
#       two-number arithmetic. "one" now counts as a number only in arithmetic company:
#       beside an operator word, a fraction word, or "more/less than".
_PQ_OFFER = re.compile(
    r"^(?:(?:and|so|now|or|okay|ok|alright|great|nice|perfect)[,\s]+)*"
    r"(?:do you want|want to|want me to|want another|want more|wanna|"
    r"would you (?:like|rather|prefer)|are you ready|ready to|ready for|"
    r"shall we|should we|how about|care to|up for|feel like|what do you say|"
    r"(?:do you|can you)?\s*see (?:how|that|why|where|it)(?!\s+(?:many|much|few|long))|"
    r"notice (?:how|that|the)(?!\s+(?:many|much))|look at)\b", re.I)


def _pq_is_offer(sentence: str) -> bool:
    """True when a question asks the student's PREFERENCE or directs their eyes --
    an invitation or a look-question, never a computation handed to them. Offers need
    no pending board line: the problem itself arrives on the turn the student accepts."""
    return bool(_PQ_OFFER.match(str(sentence or "").strip()))


# "one" in arithmetic company -- the only "one" that counts as a number (build dg).
_PQ_ONE_ARITH = re.compile(
    r"\b(?:plus|minus|times|add|adds|added|subtract|multiplied|divided|of)\s+one\b"
    r"|\bone\s+(?:plus|minus|times|divided|multiplied|more\s+than|less\s+than|"
    r"hundred|thousand|half|halves|third|thirds|fourth|fourths|fifth|fifths|"
    r"sixth|sixths|seventh|sevenths|eighth|eighths|ninth|ninths|tenth|tenths)\b", re.I)

# A sentence-splitter that sees a sentence ending INSIDE a closing quote. The old split
# key ((?<=[.!?])\s+) stopped dead at «...goes in." Want me to...» -- the period hides
# before the quote mark, the two sentences merged, and a statement full of numbers
# inherited the next sentence's "?" (the third false-positive class in the audit logs).
_PQ_SENT_SPLIT = re.compile(r"(?<=[.!?])\s+|(?<=[.!?][\"'”’])\s+|\n+")


def _pq_numeric_tokens(sentence: str) -> int:
    """How many numbers a sentence states, numerals and number-words alike.

    A written fraction ("1/2", "3/4") is ONE number, not two -- counting its halves
    separately made "is 1/2 bigger than the piece we shaded?" look like arithmetic.
    And "one" only counts in arithmetic company (build dg) -- as a bare pronoun
    ("try one more", "see one yourself") it is not a number at all."""
    low = re.sub(r"\d+\s*/\s*\d+", " ½ ", sentence.lower())
    n = len(re.findall(r"\d+(?:\.\d+)?", low)) + low.count("½")
    words = sorted([w for w in list(_PR_ONES) + list(_PR_TENS) if w != "one"],
                   key=len, reverse=True)
    n += len(re.findall(r"\b(?:" + "|".join(words) + r")\b", low))
    n += len(_PQ_ONE_ARITH.findall(low))
    return n


# build gw: a demand for AN ANSWER, with no numbers in it. Deliberately not "what do you
# think?" or "does that make sense?" -- those are invitations, not computations.
_PQ_BARE_DEMAND = re.compile(
    r"\bwhat (?:do|did) you get\b|\bwhat'?s the (?:answer|total|sum|result)\b|"
    r"\bwhat does (?:that|it) (?:come to|equal|make)\b|\bhow much (?:is )?(?:that|it)\b|"
    r"\bwhat'?s it come to\b|\bwhat do you get when you\b", re.I)


def prose_pending_question_conflict(reply: str):
    """Return a description of a computation asked with nothing on the board, or "".
    Never raises: any unexpected input yields "" (fail open)."""
    try:
        text = str(reply or "")
        prose = _spoken_only(text)
        asks = []
        for sent in _PQ_SENT_SPLIT.split(prose):
            sent = sent.strip()
            if not sent.endswith("?"):
                continue
            if _pq_is_offer(sent):
                continue          # an invitation, not a computation (build dg)
            nums = _pq_numeric_tokens(sent)
            if (nums >= 2
                    or (nums >= 1 and re.search(_PQ_OPERATOR, sent, re.I))
                    or _PQ_SYMBOL_EXPR.search(sent)):
                asks.append(sent)
        # BUILD gw (2026-08-17) -- THE BARE ANSWER-DEMAND, which walked past everything
        # above. From the day's decimal-alignment audit, twice:
        #     board:  [[step eq="2.6 + 1.35"]]        (no "?" anywhere)
        #     prose:  "...then add column by column. What do you get?"
        # Every gate above needs the NUMBERS to be in the asking sentence -- two of them,
        # or one with an operator. "What do you get?" has none, so `asks` came back empty
        # and rule 15 never looked. And because the board line carries no "?" either, rule
        # 44's referee skipped it too: THE MISSING "?" MADE THE PROBLEM INVISIBLE TO BOTH.
        # That is why the audit's rule-15 and rule-44 findings here are one defect wearing
        # two numbers.
        # So: a bare demand for an answer counts as an ask, PROVIDED the board is holding a
        # real computation for it to be about. Narrow on both sides -- the phrase must be an
        # answer-demand ("what do you get", not "what do you think"), and the board must
        # carry an operator with a number.
        if not asks and _PQ_BARE_DEMAND.search(prose):
            for tag in re.findall(r"\[\[\s*(?:" + "|".join(_PQ_BOARD_TAGS) + r")\b([^\]]*)\]\]",
                                  text, re.I):
                for val in re.findall(r'"([^"]*)"', tag):
                    if re.search(r"[+\-\u2212\u00d7x*/\u00f7]", val) and re.search(r"\d", val):
                        asks.append(_PQ_BARE_DEMAND.search(prose).group(0))
                        break
                if asks:
                    break
        if not asks:
            return ""
        # Does the board carry a PENDING line -- a "?" standing in for the unknown?
        for tag in re.findall(r"\[\[\s*(" + "|".join(_PQ_BOARD_TAGS) + r")\b([^\]]*)\]\]",
                              text, re.I):
            if "?" in tag[1]:
                return ""
        asked = " ".join(asks[-1].split())[:90]
        return ('you ask the student to work out "{q}" but this reply puts no pending line '
                'on the board -- nothing with a "?" in it. Rule 15: the problem you hand '
                'them goes UP, in symbols, in the same reply you ask it, written as a '
                'pending line like [[step eq="dollars: 2 + 1 + 1 = ?"]]. The "?" keeps the '
                'question complete on the board without running ahead of them '
                '(rule 6).').format(q=asked)
    except Exception as exc:  # noqa: BLE001 -- referee crash = fail open, always
        print(f"[pendcheck] crashed (fail open): {exc}")
        _event("referee_crash", "pendcheck", str(exc))
        return ""


# =============================================================================
# THE SELF-ANSWER CHECK (2026-08-10, build cy) -- fifth part of the referee.
# -----------------------------------------------------------------------------
# WAIT TIME, and why this is not a new rule but an old one finally enforced.
#
# From the MAA Instructional Practices Guide (CP.1.2), which Jim put in the tutor folder:
# instructors wait on average LESS THAN 1.5 SECONDS before answering their own question
# or asking another; the research says wait at least SEVEN, and that an average above
# three seconds is the threshold at which the discourse actually changes (Fuller et al.
# 1985; Tobin 1987). The first benefit the guide lists for waiting is "a decrease in the
# number of 'I don't know' responses" -- which is the exact thing Jim keeps meeting.
#
# The guide's vignette is a calculus instructor asking eight questions in a row and
# answering EVERY ONE of them himself a second later. We cannot rush our students -- they
# type or speak whenever they like -- but we can rush OURSELVES, in exactly that way: ask
# a question and then supply the answer in the same reply. The student never gets the
# seven seconds because the answer was already on the screen.
#
# RULE 39(b) ALREADY FORBIDS THIS: one question per turn, and it comes LAST. It has been
# COVERED since build ce -- written into all ten prompts and never checked. Moving a rule
# up a tier is worth more than writing a new one, so this enforces 39(b) rather than
# adding rule 52 (and it costs no prompt budget, which at 134,476 characters matters).
#
# NARROW ON PURPOSE, because every false positive costs a real model call. It fires only
# when BOTH halves are true:
#   1. the reply asks something ANSWERABLE -- the same test rule 15's referee uses, so a
#      rhetorical "so what happens next?" is not a question for these purposes; and
#   2. after that question, the reply keeps talking AND states a NUMBER.
# "What is 7 plus 5? Take your time." is clean -- no number after the question.
# "What is 7 plus 5? It's 12." is not.
# A question that is genuinely last is clean, which is the behaviour we want.
_SA_TRAILING_NUM = re.compile(r"\d")
# A second way in, for questions that carry no numbers of their own ("how much work is
# done on each slice?" -- the guide's own vignette). Widening the QUESTION test would have
# caught our foundation scripts, which are all shaped "What is a numerator? The numerator
# is ..." -- teaching, not self-answering. So the widening goes on the TAIL instead:
# nobody announces a definition with "the answer is". Both halves still required.
_SA_ANSWER_MARKER = re.compile(
    r"\b(?:the answer is|that'?s just|that is just|it'?s just|which is just|"
    r"so the answer|comes out to|works out to|equals)\b", re.I)


def _sa_number_tokens(text: str) -> set:
    """The number tokens a sentence states, numerals and number-words alike, as a SET --
    so the tail can be compared against the question and a restated number recognised as
    a hint rather than an answer."""
    low = str(text or "").lower()
    out = set(re.findall(r"\d+(?:\.\d+)?", low))
    words = sorted(list(_PR_ONES) + list(_PR_TENS), key=len, reverse=True)
    out |= set(re.findall(r"\b(?:" + "|".join(words) + r")\b", low))
    return out


def prose_self_answer_conflict(reply: str):
    """Return a description of the tutor answering its own question, or "".
    Never raises: any unexpected input yields "" (fail open)."""
    try:
        text = str(reply or "")
        prose = _spoken_only(text)
        sentences = [x.strip() for x in _PQ_SENT_SPLIT.split(prose) if x.strip()]
        last_ask = -1
        asked = ""
        for i, sent in enumerate(sentences):
            if not sent.endswith("?"):
                continue
            if _pq_is_offer(sent):
                continue          # an invitation, not a question he can self-answer (dg)
            nums = _pq_numeric_tokens(sent)
            rest = " ".join(sentences[i + 1:])
            if (nums >= 2
                    or (nums >= 1 and re.search(_PQ_OPERATOR, sent, re.I))
                    or _PQ_SYMBOL_EXPR.search(sent)
                    or _SA_ANSWER_MARKER.search(rest)):
                last_ask, asked = i, sent
        if last_ask < 0:
            return ""
        tail = " ".join(sentences[last_ask + 1:]).strip()
        if not tail:
            return ""                      # the question is last -- exactly right
        # Words of encouragement after a question are fine and often kind. Stating a
        # number gives the answer away -- but ONLY a number the question did not already
        # contain. Caught on the sweep of our own 227 demo lines: "two to WHAT power makes
        # thirty-two? Start at two and count how many times you double" restates "two"
        # from the question as a HINT and never says five. A hint is not an answer, and a
        # referee that cannot tell them apart would punish good teaching.
        asked_nums = _sa_number_tokens(asked)
        novel = [t for t in _sa_number_tokens(tail) if t not in asked_nums]
        if not novel:
            return ""
        return ('you ask "{q}" and then keep talking, and what follows states a number -- '
                '"{t}". Rule 39(b): ONE question per turn and it comes LAST. The research '
                'behind it is blunt: teachers wait about a second and a half before '
                'answering their own question, the evidence says wait seven, and the first '
                'thing that improves when you wait is how often a student says "I don\'t '
                'know". Ask, then stop. Their answer is the next turn\'s job, and if they '
                'are stuck, rule 24 gives you the whole ladder -- on the NEXT turn.'
                ).format(q=" ".join(asked.split())[:70], t=" ".join(tail.split())[:60])
    except Exception as exc:  # noqa: BLE001 -- referee crash = fail open, always
        print(f"[selfanswer] crashed (fail open): {exc}")
        _event("referee_crash", "selfanswer", str(exc))
        return ""


# =============================================================================
# THE BOARD-NOTATION CHECK (2026-08-11, build dk) -- deterministic, no model call.
# -----------------------------------------------------------------------------
# Two abuses of notation the audit RE-RUN shipped to real boards, each teaching a
# broken rule in writing, and neither visible to mathcheck ($ and % are not sympy):
#   1. "$50 + 10% = $55" -- a bare percent ADDED to a plain quantity, COMPLETED. The
#      missing idea is "10% OF $50" (rules 13/27). Percent-with-percent arithmetic
#      ("100% - 40% = 60%") stays legal: the pattern requires a plain first operand.
#   2. "a^2 + 64 = 100 = ?" -- a chain of equals signs ending in "= ?" straight after
#      a bare number: "100 = ?" asks what one hundred equals (rule 15's "?" is a value
#      to compute, never a dangling continuation).
# Deterministic and NARROW: a legitimate pending line ("50 - 25% = ?"), a percent
# conversion ("3/4 = 75%"), and the "of" form all pass untouched. Swept against every
# canonical script before ship, like every referee since cy.
_BN_PCT = re.compile(
    r"(?:\$\s*)?\d+(?:\.\d+)?\s*[+\-−]\s*\d+(?:\.\d+)?\s*%\s*=\s*\$?\s*\d")
_BN_CHAIN = re.compile(r"=\s*-?\d+(?:\.\d+)?\s*=\s*\?")
# BUILD dl -- rule 54(b)'s referee: the tutor TEACHING a key-word-to-operation rule.
# The WWC guide names this as a habit tutors install by accident, and it is exactly
# the kind of confident, friendly sentence a model produces ("remember: 'altogether'
# always means add!"). Narrow: it requires the quoted-word/means/operation SHAPE, so
# talking ABOUT a key word ("the word 'altogether' tells us the story combines
# things") stays legal, and so does honest notation reading ("the fraction bar means
# divide"). Fails open like every referee.
# The banned list is STORY-CUE words only. "Sum means add" and "difference means
# subtract" are VOCABULARY -- those words are the operations' names, and rule 37
# requires teaching them. The trap the guide warns about is narrative cue words that
# merely CORRELATE with an operation ("altogether", "left", "more") being taught as if
# they decided it.
# BUILD gy (2026-08-17): "of" JOINS THE LIST, and it belongs there by this list's own
# logic. From the day's audit, in the percents lesson: "We turned 20% into 0.20, then
# multiplied -- 'of' means multiply." That is not vocabulary the way "sum" and "difference"
# are (those words NAME their operations, and rule 37 requires teaching them). "of" merely
# CORRELATES with multiplication inside one problem type, and a student who learns it as a
# rule applies it to "3 out of 4" and "what fraction of the class", mechanically and wrong.
# Added with it: the rest of the classic bad mnemonic -- "is means equals, of means times",
# plus "per" and "each", which correlate with division and multiplication respectively and
# decide neither.
_KW_SHORTCUT = re.compile(
    r"\b(?:altogether|all together|in all|in total|left(?:\s+over)?|remain(?:s|ing)?|"
    r"fewer|more|of|per|each|and|is)\b[\"'”’)]?\s*"
    r"(?:always\s+|usually\s+|just\s+)?means?\s+(?:you\s+|to\s+|we\s+)?"
    r"(?:add(?:ing|ition)?|plus|subtract(?:ing|ion)?|minus|take\s+away|"
    r"multipl(?:y|ying|ication)|times|divid(?:e|ing)|division|equals?)\b", re.I)

# BUILD gy -- RULE 61, THE FRACTION CASE. From the same audit, the fractions lesson:
#     "So one fourth plus two fourths makes three fourths -- the bottom number never
#      changes, we just add the top numbers."
# For unlike denominators the bottom number DOES change, so as spoken that is a false
# sentence, and it is the single most-documented misconception in fraction arithmetic.
# What makes this enforceable where rule 61 generally is not: THE SAME LESSON SAYS IT
# CORRECTLY THREE TIMES -- "Since the bottom numbers, the denominators, match...",
# "same-bottom-number fractions...", "kept the bottom number three since the slices are
# the same size". The tutor knows the condition and drops it. So the check is simply:
# is the condition in the sentence or not?
_R61_FRAC_CLAIM = re.compile(
    r"\b(?:the\s+)?(?:bottom(?:\s+number)?|denominator)s?\b[^.!?]{0,40}?"
    r"\b(?:never\s+chang|does\s*n[o']?t\s+chang|always\s+stays?|stays?\s+the\s+same|"
    r"doesn'?t\s+move)\w*"
    r"|\bjust\s+add\s+(?:up\s+)?the\s+top(?:\s+numbers?)?\b"
    r"|\byou\s+(?:only\s+)?add\s+the\s+(?:top|numerator)s?\b", re.I)
_R61_FRAC_CONDITION = re.compile(
    r"\bsame\b|\bmatch(?:es|ing)?\b|\balike\b|\bequal\b|\blike\s+denominator|"
    r"\bwhen\s+the\s+bottom|\bif\s+the\s+bottom|\bboth\s+.{0,20}\bfourths?\b|"
    r"\bsame[- ]size\b|\bsame[- ]bottom", re.I)


def fraction_rule_unconditioned(reply: str):
    """Return a description of the like-denominator rule spoken as a universal law, or "".
    Never raises: any unexpected input yields "" (fail open)."""
    try:
        prose = _spoken_only(str(reply or ""))
        for sent in re.split(r"(?<=[.!?])\s+", prose):
            m = _R61_FRAC_CLAIM.search(sent)
            if not m:
                continue
            if _R61_FRAC_CONDITION.search(sent):
                continue                   # the condition is right there: correct teaching
            return ('you say "{q}" with no condition attached. For fractions with DIFFERENT '
                    "bottom numbers that sentence is false -- the denominator changes, and a "
                    "child who believes it forever will add thirds to fourths by adding the "
                    "tops. Rule 61: say the whole true sentence, and the condition costs six "
                    'words -- "when the bottom numbers are the SAME, keep that bottom number '
                    'and add the top numbers."').format(
                        q=" ".join(sent[max(0, m.start() - 20):m.end() + 20].split())[:70])
        return ""
    except Exception as exc:  # noqa: BLE001 -- referee crash = fail open, always
        print(f"[frac61] crashed (fail open): {exc}")
        _event("referee_crash", "frac61", str(exc))
        return ""


def board_notation_conflict(reply: str):
    """Return a description of a malformed board line, or "". Never raises: any
    unexpected input yields "" (fail open)."""
    try:
        text = str(reply or "")
        for tag in re.findall(r"\[\[[^\]]*\]\]", text):
            for val in re.findall(r'"([^"]*)"', tag):
                if _BN_PCT.search(val):
                    v = " ".join(val.split())[:60]
                    return ('the board completes "{v}" -- a bare percent ADDED to a '
                            "plain quantity. Rule 27: a percent is not an amount; the "
                            'missing idea is "of". Write "$50 + 10% of $50 = $55", or '
                            'convert first ("10% of $50 = $5" then "$50 + $5 = $55") -- '
                            "never complete the malformed form.").format(v=v)
                if _BN_CHAIN.search(val):
                    v = " ".join(val.split())[:60]
                    return ('the board writes "{v}" -- a chain of equals signs ending '
                            'in "= ?" right after a bare number, which asks what that '
                            'number equals. Rule 15: the "?" marks a value to COMPUTE. '
                            'Write the true equation alone ("a^2 + 64 = 100"), then the '
                            'pending step as its own line ("a^2 = ?").').format(v=v)
        # build gt (2026-08-17), from the day's lesson audit: THREE MORE WAYS A BOARD LINE
        # CAN BE MALFORMED, all found in one sweep and all decidable without judgement.
        # This referee already existed and missed every one of them, which is the finding
        # that matters -- the audit's real product was not the bad turns, it was the shape
        # of our own blindness.
        # SCOPED TO eq= ON PURPOSE. A [[write text=...]] is free-form board prose and may
        # legitimately carry an arrow ("f(x) <- say it out loud"), and a [[step check=...]]
        # is a verdict that may legitimately repeat a value ("6 = 6, so the limit is 6").
        # An eq= claims to be an EQUATION, and these three shapes are not equations.
        for tag in re.findall(r"\[\[[^\]]*\]\]", text):
            for val in re.findall(r'\beq\s*=\s*"([^"]*)"', tag):
                v = " ".join(val.split())
                short = v[:60]
                # (1) AN ARROW AFTER AN EQUALS SIGN. From the fractions lesson:
                #     [[step eq="1 + 2 = 3 -> 3/4"]] -- as written this asserts 3 -> 3/4,
                #     and a child may simply read "three equals three fourths".
                #     A limit's own arrow ("lim x->2") is NOT this: it binds tight to its
                #     variable and comes BEFORE the equals sign, so both are required --
                #     whitespace on each side of the arrow, and an "=" earlier in the line.
                am = re.search(r"=\s.*?\s(\u2192|\u21d2|->|=>)\s", v)
                if am:
                    return ('the board writes "{v}" -- an arrow after an equals sign. As '
                            "written that line claims the value BEFORE the arrow equals "
                            "the thing after it, so a student can read it as \"3 equals "
                            "three fourths\". Rule 15: one line, one true statement. Split "
                            "it into the two steps you actually mean, each of which is true "
                            "on its own.").format(v=short)
                # (2) A QUESTION STUFFED INTO AN EQUATION. From the place-value lesson:
                #     [[step eq="12: which digit is the ones? = ?"]] -- not an equation at
                #     all. ("Question 1: 3/6 = ?" is a LABEL, not an interrogative, and
                #     stays clean.)
                qm = re.search(r"\b(which|what|how many|how much|why|who|where)\b", v, re.I)
                if qm and "?" in v:
                    return ('the board writes "{v}" -- a QUESTION inside an equation tag. '
                            "That is not a mathematical statement, and the student is left "
                            "reading a sentence where a computation should be. Rule 4: ask "
                            "the question in your WORDS, and put the thing to be computed "
                            'on the board as an equation with a pending "?" -- or use a '
                            "card if it is genuinely a text prompt.").format(v=short)
                # (3) A TAUTOLOGY. From the quadratics lesson:
                #     [[step eq="(x+4)^2 = (x+4)^2"]] where the FACTORING belonged.
                #     A line that says a thing equals itself records no step and teaches
                #     nothing; adjacent sides are compared so "A = B = B" is caught too.
                parts = [" ".join(x.split()) for x in v.split("=")]
                for a, b in zip(parts, parts[1:]):
                    if a and a == b:
                        return ('the board writes "{v}" -- a line that says something '
                                "equals ITSELF. It records no step: whatever move the "
                                "student just made, this does not show it. Write the real "
                                "relationship instead (the expression on one side, what it "
                                "became on the other).").format(v=short)

        # rule 54(b), build dl: teaching a key-word-to-operation shortcut, in prose or
        # on the board. The words that get banned are story CUES only (see above).
        m = _KW_SHORTCUT.search(_spoken_only(text))
        if not m:
            for tag in re.findall(r"\[\[[^\]]*\]\]", text):
                for val in re.findall(r'"([^"]*)"', tag):
                    m = _KW_SHORTCUT.search(val)
                    if m:
                        break
                if m:
                    break
        if m:
            return ('you teach "{q}" -- a key-word rule. Rule 54(b): key words do NOT '
                    "reliably signal operations, and a key-word rule installs a "
                    "misconception with your authority behind it. Name the problem's "
                    "TYPE instead (Change, Equal Groups, Compare) and let the type "
                    "choose the operation. Words describe the story; the schema decides "
                    "the arithmetic.").format(q=" ".join(m.group(0).split())[:60])
        return ""
    except Exception as exc:  # noqa: BLE001 -- referee crash = fail open, always
        print(f"[boardnote] crashed (fail open): {exc}")
        _event("referee_crash", "boardnote", str(exc))
        return ""


# =============================================================================
# THE TRIANGLE-SLOT CHECK (2026-08-13, build fe) -- rule 63(c) is born ENFORCED.
# -----------------------------------------------------------------------------
# The 2026-08-13 lesson audit (geometry-picture, HIGH): a lesson said "one leg is 6,
# the hypotenuse is 10" while its tag read sides="6,?,10" right="C" -- and sides= is
# AB, BC, CA by contract (geo-figures.js draws it exactly so), so with the right angle
# at C the FIRST slot is the hypotenuse. The drawn hypotenuse said 6; every spoken
# sentence said 10. Three of that lesson's four triangles were mis-slotted, which is
# the worst kind of board bug: the words and the picture each perfectly plausible,
# and a student who believes both learns that labels are decoration.
# NARROW, like every referee: it fires ONLY when a [[triangle]] tag carries BOTH
# right= (naming one of its vertices) and sides=, the hypotenuse slot holds a NUMBER,
# and some other slot holds a number >= it -- a geometric impossibility, never a
# style call. A pending "?" hypotenuse is always clean; algebraic side lengths are
# never judged; a right= that names no vertex is not ours to guess about.
_TRI_TAG = re.compile(r"\[\[\s*triangle\b([^\]]*)\]\]", re.I)
_TRI_ATTR = re.compile(r'([A-Za-z_]\w*)\s*=\s*"([^"]*)"')


def triangle_side_conflict(reply: str):
    """Return a description of a right-triangle tag whose hypotenuse slot holds a
    side that cannot be the hypotenuse, or "". Never raises: any unexpected input
    yields "" (fail open)."""
    try:
        text = str(reply or "")
        for m in _TRI_TAG.finditer(text):
            attrs = {k.lower(): v for k, v in _TRI_ATTR.findall(m.group(1))}
            right = (attrs.get("right") or "").strip()
            sides_raw = (attrs.get("sides") or "").strip()
            if not right or not sides_raw:
                continue
            v = [s.strip() for s in (attrs.get("v") or "A,B,C").split(",")]
            sides = [s.strip() for s in sides_raw.split(",")]
            if len(v) != 3 or len(sides) != 3:
                continue
            try:
                ridx = [x.upper() for x in v].index(right.upper())
            except ValueError:
                continue          # right= names no vertex of this triangle: not ours
            # slots are AB, BC, CA; the hypotenuse is the side that SKIPS the right-
            # angle vertex: right at A -> BC (slot 1), at B -> CA (2), at C -> AB (0).
            hyp = {0: 1, 1: 2, 2: 0}[ridx]

            def _num(s):
                try:
                    return float(s)
                except ValueError:
                    return None

            hv = _num(sides[hyp])
            if hv is None:
                continue          # a pending "?" (or algebraic) hypotenuse is fine
            offenders = [sides[i] for i in range(3) if i != hyp
                         and _num(sides[i]) is not None and _num(sides[i]) >= hv]
            if offenders:
                pair = v[hyp].upper() + v[(hyp + 1) % 3].upper()
                return ("your [[triangle]] tag has the right angle at {r}, which makes "
                        "{p} the hypotenuse -- the sides list is AB, BC, CA in that "
                        "order -- but the {p} slot holds {h}, while another side is "
                        "{o}. The hypotenuse is always the strictly longest side, so "
                        "this drawing contradicts itself. Rule 63(c): put the "
                        "hypotenuse's length (or its pending \"?\") in the {p} slot "
                        "and the legs in theirs.").format(
                            r=right.upper(), p=pair,
                            h=sides[hyp], o=offenders[0])
        return ""
    except Exception as exc:  # noqa: BLE001 -- referee crash = fail open, always
        print(f"[triangleslot] crashed (fail open): {exc}")
        _event("referee_crash", "triangleslot", str(exc))
        return ""


# =============================================================================
# THE REFUSED-DEMONSTRATION CHECK (2026-08-17, build gx) -- rule 65, the SEVENTEENTH.
# -----------------------------------------------------------------------------
# The worst thing in the 2026-08-17 audit, and it happened twice in one lesson:
#
#   STUDENT: "Can you show me taking the square root of 169?"
#   TUTOR:   "You've now watched this move twice -- let's flip it. Here's a new triangle:"
#
#   STUDENT: "Can you show me 8 squared and 15 squared first?"
#   TUTOR:   "You've watched this exact move twice now... Let's see you try it."
#            [[step eq="8^2 = ?"]] [[step eq="15^2 = ?"]]
#
# Both counts were FALSE -- the move had been shown once. So a child who asked for help
# was refused, and told they should already know it, on evidence the tutor invented.
# (The false count itself is build gv's probe; this referee is about the refusal.)
#
# A student saying "show me" is handing over the exact information a tutor spends a whole
# lesson trying to get: they are not ready to do it alone. Withdrawing the scaffold is
# right when their WORK says so. It is never right as the answer to this question.
#
# THE DISCRIMINATOR CAME OUT OF THE LESSON ITSELF. Earlier in the same transcript the same
# student asked the same kind of question and was answered properly:
#     "Here's five squared and twelve squared worked out:"
#     [[step eq="5^2 = 25"]]  [[step eq="12^2 = 144"]]
# The compliant replies contain a COMPLETED line. The refusals contain only PENDING ones.
# So: they asked to be shown, nothing in the reply is worked out, and the work is handed
# straight back. All three, or it does not fire.
_RD_ASKS = re.compile(
    r"\b(?:can|could|will|would) you (?:please )?(?:show|walk|do|work)\b"
    r"|\bshow me\b|\bwalk me through\b|\bcan (?:you|we) do (?:that|this|it|the)\b"
    r"|\bdo (?:that|this|it) one first\b|\bcan i see\b", re.I)
# A line that is WORKED OUT: an "=" followed by something that is not a bare "?".
_RD_COMPLETED = re.compile(r"=\s*(?!\s*\?)[^\s=?][^=?]*$")
_RD_HANDS_BACK = re.compile(
    r"\byour turn\b|\bgive it a (?:shot|go|try)\b|\blet'?s see you try\b|\byou try\b|"
    r"\blet'?s flip it\b|\bsee if you can\b|\bhave a go\b|\bwhat do you get\b|"
    r"\byou'?ve got this\b|\bshow me what you\b", re.I)


def refused_demonstration_conflict(reply: str, student_message: str = ""):
    """Return a description of a reply that refused a request to be shown, or "".
    Never raises: any unexpected input yields "" (fail open)."""
    try:
        said = " ".join(str(student_message or "").split())
        if not said or not _RD_ASKS.search(said):
            return ""
        text = str(reply or "")
        # Did anything actually get WORKED OUT on the board?
        for tag in re.findall(r"\[\[[^\]]*\]\]", text):
            for val in re.findall(r'"([^"]*)"', tag):
                v = " ".join(val.split())
                if "=" in v and _RD_COMPLETED.search(v):
                    return ""              # something was shown -- that is the job done
        prose = _spoken_only(text)
        # A PENDING COMPUTATION, not merely a question mark. An early version treated any
        # "?" in any tag as "the work was handed back", and the canonical sweep caught it
        # firing on card TITLES -- [[card title="Quantitative?"]], [[write text="what is it
        # approaching, as x gets close?"]]. A title that ends in a question mark is a
        # heading, not a problem waiting for the student.
        # NOTE the operator class deliberately omits a bare "x": it is the multiplication
        # sign AND the commonest variable in the app, and including it made
        # [[write text="what is it approaching, as x gets close?"]] look like a pending
        # computation. The true multiplication sign is here.
        pending = any(("?" in val and re.search(r"[=+\-\u2212\u00d7*/\u00f7^]", val))
                      for tag in re.findall(r"\[\[[^\]]*\]\]", text)
                      for val in re.findall(r'"([^"]*)"', tag))
        if not (pending or _RD_HANDS_BACK.search(prose)):
            return ""                      # not a hand-back; may be a fair clarification
        return ('the student asked to be SHOWN -- "{s}" -- and this reply works nothing out '
                "and hands the job straight back to them. Rule 65: a request to be shown is "
                "not a negotiation, it is the student telling you in the plainest words they "
                "have that they are not ready to do it alone. Show the thing they asked for, "
                "in full, with the value on the board -- then offer them the next one. "
                "Fading the scaffold is right when their WORK says so, never as the answer "
                'to "please show me".').format(s=said[:60])
    except Exception as exc:  # noqa: BLE001 -- referee crash = fail open, always
        print(f"[refusedshow] crashed (fail open): {exc}")
        _event("referee_crash", "refusedshow", str(exc))
        return ""


# =============================================================================
# THE COUNT-CLAIM PROBE (2026-08-17, build gv) -- MEASUREMENT ONLY, on purpose.
# -----------------------------------------------------------------------------
# The day's audit turned up five claims about what has ALREADY HAPPENED that were simply
# untrue, and they are the engine of a worse behaviour:
#
#   "You've now watched this move twice"        -- it was shown ONCE
#   "You've watched this exact move twice now"  -- same false count, same lesson
#   "all three conversions under your belt"     -- two were practised, one was watched
#   "Unit 9 is also still in progress"          -- not in the student's record at all
#   "your last score was eighty-five percent"   -- only a BEST score ever existed
#
# In the geometry lesson the false count was the JUSTIFICATION: the student asked "can you
# show me taking the square root of 169?" and was refused with "you've now watched this
# move twice -- let's flip it". A child asking to be shown was turned down on invented
# evidence. That is the most corrosive thing in the whole audit.
#
# AND IT IS NOT ENFORCEABLE HERE, WHICH IS WHY THIS IS A PROBE. A referee sees one reply
# and the student's last message; "twice" is a claim about the whole conversation, and
# "the shakiest spot" is a claim about a record this function has never been shown. A
# check that cannot verify its own fix is a check that loops (gj's lesson). So it counts
# and logs, and enforcement waits for the data to say which shapes are worth catching.
#
# The honest thing to record: I already know the fix I would reach for -- pass the history
# in and count. I am not doing it on a guess. Two diagnoses this week were guesses.
_CC_CLAIM = re.compile(
    # "you've" and "you have" both, and up to four words in between -- the two real
    # examples were "You've now watched this move twice" and "You've watched this exact
    # move twice now", which differ in exactly those two ways.
    r"\byou(?:'ve|\s+have)\s+(?:now\s+)?(?:watched|seen|done|had)\b(?:\s+\S+){0,4}\s+"
    r"(?:twice|three\s+times|four\s+times|\d+\s+times)\b"
    r"|\b(?:that'?s|thats) (?:two|three|four|\d+) in a row\b"
    r"|\ball (?:two|three|four|\d+) \w{3,20} under your belt\b"
    r"|\byou'?ve (?:now )?got all (?:two|three|four|\d+)\b"
    r"|\byour last score was\b"
    r"|\b(?:the|your) (?:shakiest|weakest) (?:spot|skill|area)\b",
    re.I)


def count_claim_probe(reply: str, code: str = "", course: str = "") -> None:
    """LOG a claim about what has already happened. Never enforces, never raises."""
    try:
        prose = _spoken_only(str(reply or ""))
        for m in _CC_CLAIM.finditer(prose):
            claim = " ".join(prose[max(0, m.start() - 30):m.end() + 30].split())
            print(f"[countclaim] code={str(code)[:3]}*** course={course} -- the reply "
                  f"asserts something about the past that nothing here can check: "
                  f"...{claim}...")
            _event("probe", "countclaim", claim, code, course)
    except Exception as exc:  # noqa: BLE001 -- a probe must never affect a lesson
        print(f"[countclaim] probe failed (ignored): {exc}")


# =============================================================================
# THE COLD-QUIZ CHECK (2026-08-17, build gu) -- rule 47(d), the SIXTEENTH referee.
# -----------------------------------------------------------------------------
# Read these two lines next to each other.
#
#   2026-08-11, the first full audit:   "let's do it -- five questions, all on finding
#                                        the percent of a number"
#   2026-08-17, six days later:         "Let's do it - five questions, all on finding
#                                        the percent of a number."
#
# WORD FOR WORD. Rule 47(d) was WRITTEN from the first one. It says in as many words that
# "Unit Quiz" may only introduce the real thing -- ten questions across the unit's topics
# -- and that a smaller instrument must never wear the bigger one's name into a child's
# record. The tutor produced the offending sentence again, unchanged, because rule 47 was
# COVERED and nothing watched it.
#
# This is gm's lesson for the second time: A RULE WRITTEN FROM A REAL INCIDENT THAT FAILS
# AGAIN IS NOT A RULE, IT IS A WISH. Rule 47 stops being a wish here.
#
# What makes it enforceable is that 47(d) already fixed the number -- TEN -- and already
# sanctioned the smaller instrument on one condition: that the tutor SAYS which instrument
# it is ("this is the percent-of-a-number quiz; the Unit 7 quiz also covers increase and
# decrease, which we haven't met yet"). So the check IS the rule:
#
#   a quiz is STARTING, with a stated count that is not ten, and the reply never says
#   which instrument this is.
#
# A ten-question unit quiz passes. A five-question topic quiz that NAMES itself passes --
# that is 47(d)'s own remedy. Only the unnamed, undersized one fires.
_CQ_START = re.compile(
    r"\bno hints from me\b|\bjust show me what you'?ve got\b|\bhere'?s (?:your )?(?:the )?first "
    r"question\b|\bquestion (?:one|1)\b|\blet'?s do it\b.{0,80}\bquestions?\b|"
    r"\bstarting (?:the|your) quiz\b", re.I)
_CQ_COUNT = re.compile(
    r"\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|\d{1,2})\s+questions?\b",
    re.I)
# The reply says WHICH instrument this is -- 47(d)'s sanctioned form.
# NOTE the negative lookahead. 47(d)'s remedy REQUIRES mentioning the unit quiz -- "the
# Unit 7 quiz also covers increase and decrease, which we haven't met yet" -- so a bare
# "mentions the unit quiz" test would reject the very sentence the rule asks for. What is
# forbidden is CLAIMING to be it: "this is the real Unit 7 Quiz" while handing over five
# questions. So "this is the <thing> quiz" counts as naming a smaller instrument only when
# <thing> is not a unit.
_CQ_NAMED = re.compile(
    r"\btopic quiz\b|\bnot the unit quiz\b|\bthis is the (?!.{0,20}\bunit\b).{0,40}quiz\b|"
    r"\bunit \d+ quiz also covers\b|\bpractice check\b|\bwarm[- ]?up quiz\b|"
    r"\bquick check\b|\bnot the real\b", re.I)
_CQ_UNITNAME = re.compile(r"\b(?:the )?(?:real )?unit(?: \d+)? quiz\b", re.I)
_CQ_WORDNUM = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
               "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12}


def cold_quiz_conflict(reply: str):
    """Return a description of an undersized quiz wearing the Unit Quiz's clothes, or "".
    Never raises: any unexpected input yields "" (fail open)."""
    try:
        text = str(reply or "")
        prose = re.sub(r"\[\[[^\]]*\]\]", " ", text)
        starting = bool(_CQ_START.search(prose))
        names_unit_quiz = bool(_CQ_UNITNAME.search(prose))
        if not (starting or names_unit_quiz):
            return ""
        m = _CQ_COUNT.search(prose)
        if not m:
            return ""                      # no count claimed -- nothing to measure
        tok = m.group(1).lower()
        count = _CQ_WORDNUM.get(tok) or (int(tok) if tok.isdigit() else None)
        if count is None or count == 10:
            return ""                      # the real instrument, correctly sized
        if _CQ_NAMED.search(prose):
            return ""                      # a smaller quiz that SAYS what it is: allowed
        return ("you are starting a quiz of {n} question{s} without saying which instrument "
                "it is. Rule 47(d): the words \"Unit Quiz\" may only introduce the real "
                "thing -- TEN questions across the whole unit's topics -- and a smaller "
                "instrument must never wear the bigger one's name into a child's record. "
                "This exact sentence was caught on 2026-08-11 and the rule was written from "
                "it. Either give the real ten-question unit quiz, or name what this actually "
                "is: \"this is the <topic> quiz -- the Unit N quiz also covers <the rest>, "
                "which we haven't met yet.\"").format(n=count, s="" if count == 1 else "s")
    except Exception as exc:  # noqa: BLE001 -- referee crash = fail open, always
        print(f"[coldquiz] crashed (fail open): {exc}")
        _event("referee_crash", "coldquiz", str(exc))
        return ""


# =============================================================================
# THE SILENTLY-CHANGED-ANSWER CHECK (2026-08-17, build gr) -- the FIFTEENTH referee.
# -----------------------------------------------------------------------------
# Jim, live in Geometry, 2026-08-17, with the exact exchange:
#
#   TUTOR:   3 squared plus 4 squared is 25, so c squared must be 25.
#            What times itself gives you twenty five?
#   JIM:     minus five
#   TUTOR:   That is correct.       ...and then carried on as though he had said 5.
#
# TWO errors in one reply, and the second is the worse one.
#
# (1) "That is correct" is FALSE. (-5)(-5) = 25 is sound arithmetic, but c is the length of
#     a side. A length is never negative. The tutor affirmed something untrue.
# (2) IT THEN USED A NUMBER THE STUDENT NEVER SAID. It silently swapped -5 for 5 and taught
#     on. The student is left believing their answer was accepted as given -- and a child who
#     is told "correct" and then watches a different number appear learns that the sign is
#     decoration, which is the exact misconception this lesson exists to prevent.
#
# Error (2) is the general defect and the one worth enforcing: A REPLY MAY NOT AFFIRM AN
# ANSWER AND THEN WORK FROM A DIFFERENT ONE. It is the mirror of rule 43 (never credit a
# method the student did not show) one level down: never credit a NUMBER they did not give.
# mathcheck cannot catch it, because every number in the reply is arithmetically true.
#
# NARROW -- three conditions, all required:
#   (a) the student's message carries an explicitly SIGNED number ("minus five", "-5")
#   (b) the reply AFFIRMS ("that is correct", "exactly right", "yes")
#   (c) the reply then treats the unsigned value as the answer AND NEVER MENTIONS THE SIGN
# The third clause is what keeps the correct teaching response clean: "both 5 and -5 square
# to 25, but a length can't be negative, so c = 5" affirms, uses 5, and ADDRESSES the sign --
# and must pass, because that is the reply we want.
# AFFIRMATION, and it has to be an affirmation OF AN ANSWER. An early draft accepted a bare
# "exactly" and a bare "correct" anywhere in the reply, and it fired on FOUR canonical
# scripts -- "terms with exactly the same letter part", "worth twenty five cents". Ordinary
# prose is full of both words. So the loose ones must OPEN a sentence (which is how a tutor
# actually affirms: "Correct. c = 5."), while the unambiguous phrases may appear anywhere.
_SC_AFFIRM = re.compile(
    r"\b(?:that'?s (?:right|correct|it)|that is (?:right|correct)|exactly right|"
    r"you'?ve got it|you got it|well done|nice work|spot on|bang on)\b"
    # ...and a sentence-opening affirmation must STAND ALONE. "Exactly one output" is an
    # adverb, not applause -- it fired on the function script until the lookahead was added.
    r"|(?:^|[.!?\u2014]\s*|--\s*)(?:correct|exactly|perfect|yes|yep|right)"
    r"(?=\s*[.,!;:\u2014]|\s*$)",
    re.I)
# The student said a negative: "-5", "minus five", "negative five".
_SC_STUDENT_NEG = re.compile(
    r"(?:(?:^|\s)-\s*(\d+(?:\.\d+)?))|"
    r"\b(?:minus|negative)\s+(\d+(?:\.\d+)?|" + _PR_NUMWORD + r")\b", re.I)
# The reply talks about the sign at all -- any of these means it did NOT ignore it.
_SC_ADDRESSES_SIGN = re.compile(
    r"\bnegative\b|\bminus\b|\bpositive\b|\bboth\b|\bsign\b|\btwo (?:answers|roots|values)\b|"
    r"\bcan'?t be\b|\bcannot be\b|\bnever negative\b|\blength\b.{0,24}\bpositive\b|"
    r"-\s*\d", re.I)


def answer_sign_conflict(reply: str, student_message: str = ""):
    """Return a description of a reply that affirmed a signed answer and then worked from
    the unsigned one without ever mentioning the sign, or "". Never raises (fail open)."""
    try:
        said = str(student_message or "")
        m = _SC_STUDENT_NEG.search(said)
        if not m:
            return ""
        magnitude = next((g for g in m.groups() if g), "")
        if not magnitude:
            return ""
        text = str(reply or "")
        prose = re.sub(r"\[\[[^\]]*\]\]", " ", text)
        if not _SC_AFFIRM.search(prose):
            return ""                    # it did not affirm -- correcting is the job
        if _SC_ADDRESSES_SIGN.search(text):
            return ""                    # it engaged with the sign: exactly what we want
        # Does the reply use the UNSIGNED value as the settled answer? The student may have
        # SAID a word ("minus five") while the board WRITES a digit ("c = 5"), which is the
        # founding case -- so both forms are searched. Two bugs lived here and both were
        # found by running the real exchange rather than trusting the pattern:
        #   - the old lookahead (?![\d.]) rejected "5." at the end of a sentence, so the
        #     plainest possible reply ("Correct. c = 5.") slipped straight through;
        #   - "five" was never mapped to "5", so the spoken form never matched the written.
        mag = str(magnitude).lower()
        forms = set()
        digits = mag if mag.replace(".", "").isdigit() else ""
        if digits:
            forms.add(digits)
            for w, n in list(_PR_ONES.items()) + list(_PR_TENS.items()):
                if str(n) == digits:
                    forms.add(w)
        else:
            n = _PR_ONES.get(mag, _PR_TENS.get(mag))
            forms.add(mag)
            if n is not None:
                forms.add(str(n))
        pattern = "|".join(re.escape(f) for f in sorted(forms, key=len, reverse=True))
        # (?!\.?\d) allows "5." (a sentence ending) while still refusing "5.2" (a decimal).
        if re.search(r"(?<![\d.-])(?:" + pattern + r")(?!\.?\d)", text, re.I):
            return ("the student answered a NEGATIVE number ({neg}) and your reply says it is "
                    "correct, then goes on using {pos} -- a number they never gave. Two things "
                    "are wrong: {neg} times itself does give the right product, but it cannot "
                    "be a length, so \"correct\" is untrue; and swapping their number for a "
                    "different one without saying so teaches them the sign is decoration. "
                    "Say what is true of BOTH values, then say why the context rules one out "
                    "-- e.g. \"both {pos} and {neg} square to it, but a length is never "
                    "negative, so it is {pos}.\"").format(neg="-" + str(magnitude),
                                                           pos=str(magnitude))
        return ""
    except Exception as exc:  # noqa: BLE001 -- referee crash = fail open, always
        print(f"[answersign] crashed (fail open): {exc}")
        _event("referee_crash", "answersign", str(exc))
        return ""


# =============================================================================
# THE UNIT-CLAIM CHECK (2026-08-16, build gn) -- rule 0's recap clause, born ENFORCED.
# -----------------------------------------------------------------------------
# Jim, live in Geometry: "it says where we start in unit five. And when I look at the
# tracking up on the top, it says unit one. Shouldn't it say unit five if we're working
# on unit five?"
#
# The rail was RIGHT and the tutor was wrong, which is the opposite of how it looked.
# Maya's record reads "New to this course... start at the beginning of this course";
# there was no placement past Unit 1, nothing mastered, and the next quiz on the rail was
# a Unit 1 topic. Nothing anywhere said Unit 5. The opener -- "Two days ago we started
# Unit 5: Right Triangles, and we were right in the middle of the Pythagorean theorem" --
# was INVENTED, complete with a shared past two days deep.
#
# That is worse than a mismatched progress bar. A child cannot correct a grown-up's
# memory: told they spent a lesson on the Pythagorean theorem, they conclude they have
# forgotten it. And the transcript tells their parent something that never happened --
# the same defect rule 43 closed in gm, one level up.
#
# NARROW. It fires only when the reply CLAIMS the student is (or was) working in a unit,
# and that number differs from the unit the server put them in. Reference in passing is
# untouched -- "that's a Unit 7 idea", "we'll get to Unit 5 later" -- because naming a
# unit is not the same as claiming to have been in it. Silent when the caller does not
# know the unit, which is the honest default: this referee never guesses.
# build hb (2026-08-17): CONTRACTIONS COUNT. Re-arming this referee on practice and
# topic mode meant testing it with the phrasings a tutor actually uses, and "you're in
# the middle of Unit 7" walked straight past it while "you are in the middle of Unit 7"
# was caught -- the apostrophe was the whole difference. Widened to accept we're/you're
# (and we've/you've). Swept over all 1,015 canonical foundation strings: 0 false alarms.
_UNIT_CLAIM_RE = re.compile(
    r"\b(?:we|you)(?:'re|'ve)?\s+(?:were|are|have been|has been|been|was)?\s*(?:just\s+)?"
    r"(?:started|starting|working on|in the middle of|partway through|part way through|"
    r"picking up|carrying on|continuing|left off (?:in|on)|up to|in)\s+"
    r"(?:the\s+)?(?:middle\s+of\s+)?(?:the\s+)?unit\s+(\d+)"
    r"|\bwelcome back to\s+unit\s+(\d+)"
    r"|\bwe\s+started\s+unit\s+(\d+)",
    re.I)


def unit_claim_conflict(reply: str, expected_unit=None):
    """Return a description of a reply that claims a unit the student is not in, or "".
    Never raises: any unexpected input yields "" (fail open)."""
    try:
        try:
            expected = int(expected_unit or 0)
        except (TypeError, ValueError):
            return ""
        if not (1 <= expected <= 9):
            return ""          # the caller does not know -- never guess
        prose = re.sub(r"\[\[[^\]]*\]\]", " ", str(reply or ""))
        for m in _UNIT_CLAIM_RE.finditer(prose):
            claimed_raw = next((g for g in m.groups() if g), None)
            if not claimed_raw:
                continue
            claimed = int(claimed_raw)
            if claimed != expected:
                return ("your reply tells the student they are (or were) working in Unit "
                        "{c}, but this student's notes put them in Unit {e}. Nothing you "
                        "were given says Unit {c}. Rule 0: a recap is a memory, not a "
                        "guess -- never invent a shared past. Welcome them back without "
                        "naming a place, or name Unit {e}.").format(c=claimed, e=expected)
        return ""
    except Exception as exc:  # noqa: BLE001 -- referee crash = fail open, always
        print(f"[unitclaim] crashed (fail open): {exc}")
        _event("referee_crash", "unitclaim", str(exc))
        return ""


# =============================================================================
# THE UNITPLAN CHECK (2026-08-18, build hm) -- the NINETEENTH referee, Phase 4's first.
# -----------------------------------------------------------------------------
# The full-app review's Class D, in its purest form: a single hallucinated
# [[unitplan unit="5"]] writes a real topic_progress row (main.py files the declaration
# -- Jim's 2026-08-17 ruling, THE UNIT FOLLOWS THE TEACHING), and that row becomes the
# rail's current unit on the next resume. The model's word became durable truth with no
# validation anywhere -- the likeliest mechanism of the phantom-Unit-5 mystery.
#
# The fix is the [[verify]] pattern extended to unit identity: the SERVER holds the
# record, so the server says which units a declaration could honestly name. main.py
# computes that set per turn (_unit_allowed_set: the resolved unit, the focus unit,
# every unit the record shows touched or mastered, the next unmastered unit after the
# resolved one -- a legitimate mid-session advance -- plus any unit the student's OWN
# message just asked for). A declaration outside the set is a memory the record does
# not hold: the draft is regenerated, and the student never sees it. main.py keeps a
# belt-and-suspenders re-check at filing time (fail-open pass-throughs exist), so a
# surviving invention still cannot become a topic_progress row.
#
# SILENT when the caller passes no allowed set (practice/topic lanes, nightwatch's
# synthetic students, an unresolvable store) -- a referee that cannot know must not
# guess (the gn property). Fail open on any crash, like every referee.
_UNITPLAN_RE = re.compile(_tagreg.UNITPLAN_UNIT_PATTERN, re.I)


def unitplan_conflict(reply: str, allowed_units=None):
    """Return a description of a [[unitplan]] declaring a unit the record cannot
    justify, or "". Silent when allowed_units is empty/None. Never raises."""
    try:
        allowed = set()
        for u in (allowed_units or ()):
            try:
                u = int(u)
            except (TypeError, ValueError):
                continue
            if 1 <= u <= 9:
                allowed.add(u)
        if not allowed:
            return ""          # the caller does not know -- never guess
        for m in _UNITPLAN_RE.finditer(str(reply or "")):
            try:
                declared = int(m.group(1))
            except (TypeError, ValueError):
                continue
            if not (1 <= declared <= 9):
                continue
            if declared not in allowed:
                return ("your [[unitplan]] tag declares Unit {c}, but nothing in this "
                        "student's record supports being in Unit {c} -- not their "
                        "resolved unit, not a unit they have touched or mastered, not "
                        "the next unit in their progression, and they did not ask for "
                        "it. The unit bar you draw becomes this student's RECORDED "
                        "progress. Rule 0: a recap is a memory, not a guess. Teach and "
                        "declare the unit the record puts them in (their notes name "
                        "it), or the unit the student themselves just asked for."
                        ).format(c=declared)
        return ""
    except Exception as exc:  # noqa: BLE001 -- referee crash = fail open, always
        print(f"[unitplanref] crashed (fail open): {exc}")
        _event("referee_crash", "unitplanref", str(exc))
        return ""


# =============================================================================
# THE STORY-UNITS CHECK (2026-08-18, build hr) -- the TWENTY-FIRST referee.
# -----------------------------------------------------------------------------
# The night watch's FIRST confirmed catch on the Phase-4 build (2026-08-18 08:44 UTC
# report, order-of-operations, prealgebra): the tutor modeled 4 + 3 × 2 as
#
#   "Let's picture it: you have 4 dollars, plus 3 bags of 2 candies each."
#
# A child cannot put dollars and candies in one pile, so the addition in the story is
# not the addition in the expression -- the numbers become decoration (rule 32's new
# one-unit clause, written from this catch).
#
# NARROW, the rule-27 precedent (enforce the caught shape; the words cover the class):
# fires only when ONE SENTENCE contains (a) a money amount, (b) an additive joiner
# immediately before a count of grouped NON-money objects ("plus 3 bags of 2
# candies"), and (c) no sign that the groups resolve to money ("...that cost 2
# dollars each" is a fine shopping story -- everything becomes money). Judged per
# sentence on the SPOKEN prose only. Fail open, canonical-swept, both directions.
_SU_MONEY = re.compile(
    r"(?:\$\s*\d|\b(?:\d+|" + _PR_NUMWORD + r")\s+(?:dollars?|cents?|bucks?)\b)", re.I)
# The joiner is "plus"/"add" ONLY -- "and" merely lists two facts ("you have 4
# dollars and 3 bags of candy; each candy sells for a dime" is a fine story whose
# money resolution lives in the NEXT sentence), and a referee that fires on it
# would veto honest shopping problems. Narrow means narrow.
_SU_OBJ_GROUP = re.compile(
    r"\b(?:plus|add(?:s|ed|ing)?)\s+(?:\d+|" + _PR_NUMWORD + r")\s+"
    r"(?:bags?|boxes?|groups?|packs?|piles?|stacks?|rows?|baskets?|sets?|trays?)\s+of\s+"
    r"(?:\d+|" + _PR_NUMWORD + r")\s+(?!dollars?\b|cents?\b|bucks?\b)([a-z]+)", re.I)
_SU_RESOLVES = re.compile(
    r"\b(?:cost|costs|costing|worth|pay|pays|paid|spend|spends|spent|price|priced|at|for)\b"
    r"[^.!?]{0,24}?(?:\$|\bdollars?\b|\bcents?\b|\bbucks?\b)"
    r"|(?:\$|\bdollars?\b|\bcents?\b|\bbucks?\b)\s*(?:each|apiece|per)\b", re.I)


def story_units_conflict(reply: str):
    """Return a description of a story that adds money to grouped objects, or "".
    Never raises: any unexpected input yields "" (fail open)."""
    try:
        prose = _spoken_only(str(reply or ""))
        for sent in _vis_sentences(prose):
            m = _SU_OBJ_GROUP.search(sent)
            if not m:
                continue
            if not _SU_MONEY.search(sent):
                continue
            if _SU_RESOLVES.search(sent):
                continue          # the groups become money -- a fine shopping story
            thing = m.group(1)
            return ('your story adds a MONEY amount to "{t}" -- two kinds of thing '
                    "that cannot go in one pile, so the addition in the story is not "
                    "the addition in the expression and the numbers become "
                    "decoration. Rule 32(b): a story that models an expression keeps "
                    "ONE kind of quantity throughout. Retell it with a single unit "
                    '(all {t}, or all money), e.g. "you have 4 loose candies, plus '
                    '3 bags of 2 candies each."').format(t=thing[:24])
        return ""
    except Exception as exc:  # noqa: BLE001 -- referee crash = fail open, always
        print(f"[storyunits] crashed (fail open): {exc}")
        _event("referee_crash", "storyunits", str(exc))
        return ""


# =============================================================================
# THE PROMISED-COMPARISON CHECK (2026-08-18, build hz) -- the TWENTY-SECOND referee.
# -----------------------------------------------------------------------------
# Jim's live catch, geometry: "Here's our angle again, fifty degrees, next to a
# right angle for comparison" -- spoken over a board holding ONLY the fifty-degree
# angle. Every existing watcher was honestly blind to it: the promised-picture
# referee stays quiet because a figure WAS drawn; the two figure-content referees
# only read [[triangle]] tags; the screen auditor judges layout, not claims. The
# prompt's "YOUR PICTURE MUST MATCH YOUR WORDS" was a wish (a rule that nothing
# watches is a wish), so the caught shape becomes a referee, narrow on purpose
# like rule 27's and hr's precedents:
#
#   FIRES when a sentence puts the angle NEXT TO / BESIDE / ALONGSIDE / SIDE BY
#   SIDE WITH a right angle (or claims "right angle ... for comparison") and no
#   [[angle]] tag in the reply carries deg="90". The board draws ONE figure per
#   tag, so the only honest ways to keep that sentence are [[angle deg="90"
#   split="50"]] (the piece drawn INSIDE the right angle -- the better teaching
#   picture anyway) or a plain 90-degree angle.
#
#   NEVER fires on the comparison QUESTION alone ("compared to a right angle of
#   ninety degrees, is fifty bigger, smaller, or about the same?") -- asking a
#   student to compare against a remembered right angle needs no second picture;
#   only CLAIMING one is on the board does. Deferrals ("next time I'll draw them
#   side by side") ride the same _VIS_DEFER exemption as the promised-picture
#   referee. Fail open, like every referee.
# =============================================================================
_AC_RIGHT = r"(?:right\s+angle|ninety[-\s]?degree(?:s)?(?:\s+angle)?|90\s*(?:°|degrees?)(?:\s+angle)?)"
_AC_JUXTA = re.compile(
    r"\b(?:next\s+to|beside|alongside|side\s+by\s+side\s+with|on\s+top\s+of)\s+"
    r"(?:a|the|our|this|that)?\s*" + _AC_RIGHT, re.I)
_AC_FORCOMP = re.compile(_AC_RIGHT + r"(?:\s+\S+){0,3}?\s+for\s+(?:a\s+|the\s+)?comparison\b", re.I)
_AC_ANGLE_TAG = re.compile(r"\[\[\s*angle\b([^\]]*)\]\]", re.I)
_AC_DEG = re.compile(r'\bdeg\s*=\s*"?\s*(\d{1,3})', re.I)


def angle_compare_conflict(reply: str):
    """Return a description of a spoken right-angle comparison the reply's own
    figure does not show, or "". Never raises: any unexpected input yields ""
    (fail open)."""
    try:
        text = str(reply or "")
        prose = _spoken_only(text)
        claimed = ""
        for sent in _vis_sentences(prose):
            if _VIS_DEFER.search(sent):
                continue                    # "next time I'll draw them side by side"
            m = _AC_JUXTA.search(sent) or _AC_FORCOMP.search(sent)
            if m:
                claimed = " ".join(m.group(0).split())[:70]
                break
        if not claimed:
            return ""
        for attrs in _AC_ANGLE_TAG.findall(text):
            dm = _AC_DEG.search(attrs)
            if dm and dm.group(1) == "90":
                return ""                   # a right angle IS drawn (alone or holding the split piece)
        return ('you say "{c}" but no right angle is anywhere in this reply\'s '
                "figure -- the student is told to compare against a picture that is "
                "not there. Rule 63(e): a comparison you SPEAK is a comparison you "
                "DRAW. The board draws one figure per tag, so draw the piece INSIDE "
                'the right angle -- [[angle deg="90" split="50"]] shows fifty '
                "degrees sitting inside ninety with forty left over -- or drop the "
                "claim and just ask the comparison question, which needs no second "
                "picture.").format(c=claimed)
    except Exception as exc:  # noqa: BLE001 -- referee crash = fail open, always
        print(f"[anglecompare] crashed (fail open): {exc}")
        _event("referee_crash", "anglecompare", str(exc))
        return ""


# =============================================================================
# THE QUIZ-TERM CHECK (2026-08-18, build ia) -- the TWENTY-THIRD referee.
# -----------------------------------------------------------------------------
# Jim's live quiz run, catch #1 of four: quiz question one was "is one hundred ten
# degrees acute, right, or obtuse?" -- and the student's only honest answer was
# "I don't know. We haven't covered that." Worse, the tutor then ADMITTED it ("I
# hadn't taught it yet"), restarted the quiz, and asked the SAME untaught choice
# again. The term-gap probe (build gi) could only log the miss after the student
# was hit; nothing could stop the question going out, because "what was taught"
# lives in the conversation history and no referee could see it.
#
# Now one can. _create_verified computes `heard` -- the lowercased text of the
# turn's ORIGINAL messages (both sides of the conversation as the model saw it,
# NOT including retry nudges, which would let a rejected draft teach the checker
# its own vocabulary) -- and hands it down the sweep. Rule 47(e) carries the words.
#
# NARROW, per the rule-27/hr/hz precedents -- the caught shape only:
#   FIRES on a QUESTION sentence offering the acute/obtuse classification choice
#   ("is this angle acute, right, or obtuse?") when an offered term was never
#   heard: "acute"/"obtuse" as words, the "right" option as "right angle" (bare
#   "right" is ordinary prose). The reply's OWN prose outside the question counts
#   as heard -- a reply that teaches the terms and then asks is doing its job, and
#   defining a term inside a LATER lesson stays legal.
#   SILENT when the caller passes no history (battery fixtures, nightwatch panels,
#   direct calls) -- a referee that cannot know must not guess.
# =============================================================================
_QT_CHOICE_TERMS = re.compile(r"\b(acute|obtuse)\b", re.I)


def quiz_term_conflict(reply: str, heard=None):
    """Return a description of a quiz choice built on terms the conversation never
    taught, or "". Silent when `heard` is None. Never raises (fail open)."""
    try:
        if heard is None:
            return ""
        text = str(reply or "")
        prose = _spoken_only(text)
        for sent in _vis_sentences(prose):
            if "?" not in sent:
                continue                    # teaching sentences may list the terms freely
            terms = {t.lower() for t in _QT_CHOICE_TERMS.findall(sent)}
            if not ({"acute", "obtuse"} <= terms):
                continue                    # not the classification-choice shape
            if re.search(r"\bright\b", sent, re.I):
                terms.add("right")
            base = (str(heard) + " " + prose.replace(sent, " ")).lower()
            missing = []
            for t in sorted(terms):
                needle = "right angle" if t == "right" else t
                if needle not in base:
                    missing.append(needle)
            if missing:
                miss = ", ".join('"' + m + '"' for m in missing)
                return ("your quiz question offers the choice acute / right / obtuse, "
                        "but this conversation has never said {m} -- the student's only "
                        "honest answer is \"we haven't covered that\", and that miss "
                        "lands on their record. Rule 47(e): THE QUIZ ASKS ONLY WHAT WAS "
                        "TAUGHT. Stop the quiz, teach the missing idea in its own turn "
                        "(with the pictures -- an [[angle]] under ninety, at ninety, "
                        "over ninety), get two unaided rights, and only then quiz it."
                        ).format(m=miss)
        return ""
    except Exception as exc:  # noqa: BLE001 -- referee crash = fail open, always
        print(f"[quizterm] crashed (fail open): {exc}")
        _event("referee_crash", "quizterm", str(exc))
        return ""


# =============================================================================
# THE SELF-CONTAINED QUESTION CHECK (2026-08-18, build ib) -- the TWENTY-FOURTH.
# -----------------------------------------------------------------------------
# Jim's live quiz run, catch #4: "Here's angle X Y Z with the vertex at Y. What is
# the vertex of this angle -- the middle letter, where the two rays meet?" The
# question states its own answer and then asks it. Neither sibling could see it:
# the self-answer referee (rule 39b) looks for an answer AFTER the question, and
# the board-answers-it referee (rule 17) reads tags, not prose. Rule 47(g) carries
# the words.
#
# NARROW -- the caught shape, in a QUIZ only: the reply is a numbered quiz question
# ("Question 3:" and kin), it states "the vertex ... at <letter>", and it then asks
# "what is the vertex". OUTSIDE a quiz this exact shape is often good teaching --
# rule 47's own say-it-back move ("the vertex is at Y -- say it back: what's the
# vertex?") must stay legal -- which is why the Question-N marker is required.
# =============================================================================
_QSC_QUIZ = re.compile(r"\bquestion\s+(?:one|two|three|four|five|\d+)\s*[:.,]", re.I)
_QSC_STATE = re.compile(r"\bvertex\s+(?:is\s+)?at\s+([A-Za-z])\b", re.I)
_QSC_ASK = re.compile(r"\bwhat(?:'s|\s+is)\s+the\s+vertex\b", re.I)


def question_self_contained_conflict(reply: str):
    """Return a description of a quiz question that states its own answer, or "".
    Never raises: any unexpected input yields "" (fail open)."""
    try:
        prose = _spoken_only(str(reply or ""))
        if not _QSC_QUIZ.search(prose):
            return ""                      # not a numbered quiz question
        stated = _QSC_STATE.search(prose)
        if not (stated and _QSC_ASK.search(prose)):
            return ""
        return ('your quiz question says the vertex is at {v} and then asks "what is '
                "the vertex?\" -- the answer is inside the question, so a right answer "
                "proves nothing and the tally becomes fiction. Rule 47(g): THE QUESTION "
                "MUST NOT CONTAIN ITS ANSWER. Say the figure's NAME and let the picture "
                "and caption carry it -- \"here's angle X Y Z -- what is the vertex?\" "
                "is the same question with the answer left for the student."
                ).format(v=stated.group(1).upper())
    except Exception as exc:  # noqa: BLE001 -- referee crash = fail open, always
        print(f"[selfquiz] crashed (fail open): {exc}")
        _event("referee_crash", "selfquiz", str(exc))
        return ""


# =============================================================================
# THE RECORD-CLAIM CHECK (2026-08-18, build ho) -- the TWENTIETH referee.
# -----------------------------------------------------------------------------
# The count-claim probe's promotion (build gv measured; Phase 4 enforces). The audit's
# most corrosive finding: a child asked "can you show me taking the square root of
# 169?" and was REFUSED on invented evidence -- "you've now watched this move twice."
# The probe logged five such claims about the past in one day's audit: false watch
# counts, "all three conversions under your belt", "Unit 9 is also still in
# progress" (not in the record at all), "your last score was eighty-five percent"
# (only a BEST ever existed).
#
# The [[verify]] pattern, extended to the past: the SERVER holds the record
# (main._claim_record hands this referee a compact copy), so claims the record can
# check are checked, and counts the record CANNOT hold are refused outright:
#
#   SCORE claims  ("your last/best score was N%", "you got N% on the ... quiz")
#       -> N must be a score the record actually holds (unit checks' best/last,
#          topic-quiz bests). EXEMPT when the reply itself carries a [[quiz]]/
#          [[check]]/[[finalexam]] tag: an in-reply result is rule 45's referee's
#          job (prose_score_conflict), not a claim about the past.
#   UNIT-STATE claims ("you've mastered Unit N", "Unit N is still in progress")
#       -> checked against the record's mastered/touched sets. Future conditionals
#          ("once you've mastered Unit 4...") are exempt.
#   WATCH-COUNT claims ("you've watched this move twice", "all three ... under
#       your belt") -> ALWAYS refused: the record stores no per-event counts, so
#       no such number can ever be a memory -- and rule 65(d) already bans
#       justifying a refusal with a count. The regeneration nudge tells the model
#       to make its point without the invented number.
#
# SILENT when the caller passes no record (practice/topic lanes, nightwatch's
# synthetic students, the DB off) -- a referee that cannot know must not guess.
# Fail open on any crash, like every referee.
_RC_NUM = r"(\d{1,3}|" + _PR_NUMWORD + r")\s*(?:%|percent)"
_RC_SCORE_PATTERNS = (
    ("last", re.compile(r"\byour\s+(?:last|previous)\s+(?:quiz\s+|check\s+|test\s+)?score\s+(?:was|is)\s+" + _RC_NUM, re.I)),
    ("best", re.compile(r"\byour\s+(?:personal\s+)?best(?:\s+score)?\s+(?:was|is|of)\s+" + _RC_NUM, re.I)),
    ("got",  re.compile(r"\byou\s+(?:got|scored|earned)\s+" + _RC_NUM + r"\s+on\s+(?:the|your|that|it)\b", re.I)),
)
_RC_MASTERED_YOU = re.compile(r"\byou(?:'ve|\s+have)\s+(?:already\s+)?mastered\s+unit\s+(\d)\b", re.I)
_RC_MASTERED_UNIT = re.compile(r"\bunit\s+(\d)\s+is\s+(?:already\s+)?(?:mastered|complete|finished)\b", re.I)
_RC_INPROGRESS = re.compile(
    r"\bunit\s+(\d)\s+is\s+(?:(?:also|still)\s+){0,2}in\s+progress\b", re.I)
_RC_FUTURE = re.compile(r"\b(?:once|when|after|if|until)\s*$", re.I)
_RC_WATCHED = re.compile(
    r"\byou(?:'ve|\s+have)\s+(?:now\s+|already\s+|just\s+)?(?:watched|seen)\b(?:\s+\S+){0,4}?\s+"
    r"(?:once|twice|(?:two|three|four|five|\d+)\s+times)\b"
    r"|\ball\s+(?:two|three|four|five|\d+)\s+\w{3,20}\s+under\s+your\s+belt\b", re.I)
_RC_RESULT_TAG = re.compile(r"\[\[\s*(?:quiz|check|finalexam)\b", re.I)


def _rc_value(raw) -> "float | None":
    """'85' -> 85.0, 'eighty-five' -> 85.0, junk -> None."""
    s = str(raw or "").strip()
    if re.match(r"^\d{1,3}$", s):
        return float(s)
    v = _pr_word_value(s)
    return float(v) if v is not None else None


def record_claim_conflict(reply: str, record=None):
    """Return a description of a claim about the past that the student's record
    cannot support, or "". Silent when `record` is None. Never raises."""
    try:
        if not isinstance(record, dict):
            return ""          # the caller does not know -- never guess
        # A reply announcing a RESULT ([[quiz]]/[[check]]/[[finalexam]]) is exempt
        # from the WHOLE sweep: the new result is not yet in the record (recording
        # follows the reply), and the in-reply numbers are rule 45's referee's job.
        if _RC_RESULT_TAG.search(str(reply or "")):
            return ""
        prose = _spoken_only(str(reply or ""))
        # WATCH COUNTS: no record anywhere stores these -- the number is always invented.
        m = _RC_WATCHED.search(prose)
        if m:
            said = " ".join(m.group(0).split())
            return ('your reply tells the student "{s}" -- a COUNT of past events. '
                    "Nothing in this student's record stores how many times anything "
                    "was watched, seen or collected, so that number cannot be a "
                    "memory; and rule 65(d) forbids justifying anything to a student "
                    "with a count. Make your point without the invented number -- "
                    '"we\'ve worked on this before" is honest; "twice" is not.'
                    ).format(s=said[:80])
        # UNIT-STATE claims, against the record's own sets.
        mastered = {int(u) for u in (record.get("mastered") or ())}
        touched = {int(u) for u in (record.get("touched") or ())} | mastered
        for pat in (_RC_MASTERED_YOU, _RC_MASTERED_UNIT):
            for m in pat.finditer(prose):
                if _RC_FUTURE.search(prose[max(0, m.start() - 12):m.start()]):
                    continue               # "once you've mastered Unit 4..." is a plan
                u = int(m.group(1))
                if u not in mastered:
                    return ("your reply says Unit {u} is mastered, but the record "
                            "shows {have}. Rule 0: a recap is a memory, not a guess "
                            "-- praise what the record actually holds, or say "
                            "nothing about mastery.").format(
                                u=u, have=("mastered units " + ", ".join(
                                    str(x) for x in sorted(mastered))
                                    if mastered else "NO mastered units yet"))
        for m in _RC_INPROGRESS.finditer(prose):
            u = int(m.group(1))
            if u not in touched:
                return ("your reply says Unit {u} is in progress, but this student's "
                        "record shows no work in Unit {u} at all{have}. Rule 0: never "
                        "invent a shared past -- speak only of units the record "
                        "shows.").format(
                            u=u, have=(" (their record shows units " + ", ".join(
                                str(x) for x in sorted(touched)) + ")"
                                if touched else ""))
        # SCORE claims, against every percentage the record actually holds.
        known_last = {float(v) for v in (record.get("last") or {}).values()}
        known_best = {float(v) for v in (record.get("best") or {}).values()}
        known_quiz = {float(v) for v in (record.get("quiz_pcts") or ())}
        known_by_kind = {
            "last": known_last | known_best | known_quiz,
            "best": known_best | known_quiz,
            "got":  known_last | known_best | known_quiz,
        }
        any_known = known_last | known_best | known_quiz
        for kind, pat in _RC_SCORE_PATTERNS:
            for m in pat.finditer(prose):
                val = _rc_value(m.group(1))
                if val is None:
                    continue
                if val not in known_by_kind[kind]:
                    return ("your reply tells the student a past score of "
                            "{v:.0f}%, but the record holds {have}. Rule 45's "
                            "principle reaches the past too: a number you SAY "
                            "about their record must BE in their record. State "
                            "a recorded score, or encourage them without "
                            "inventing one.").format(
                                v=val, have=("these scores: " + ", ".join(
                                    f"{int(x)}%" for x in sorted(any_known))
                                    if any_known else "NO recorded scores yet"))
        return ""
    except Exception as exc:  # noqa: BLE001 -- referee crash = fail open, always
        print(f"[recordclaim] crashed (fail open): {exc}")
        _event("referee_crash", "recordclaim", str(exc))
        return ""


# =============================================================================
# THE TRIANGLE-LETTER CHECK (2026-08-16, build gn) -- rule 63(d), born ENFORCED.
# -----------------------------------------------------------------------------
# Jim ran one Geometry lesson and read the first turn out loud: "a, b, and c are supposed
# to be legs of a right triangle, and instead they're shown as the angles. So when you say
# a squared plus b squared equals c squared, it makes no sense. The most popular theorem
# in all of math is wrong."
#
# The tag was [[triangle v="A,B,C" sides="3,?,4" right="A"]]. v= letters the CORNERS and
# sides= letters the SIDES, so the picture had A, B, C on its vertices, 3/?/4 on its legs,
# and nothing at all called a, b or c -- while the words leaned on exactly those three
# letters. Worse than absent: under the convention every textbook uses, side a is the one
# OPPOSITE vertex A, which in that figure (right angle at A) is the HYPOTENUSE. The board
# said c was the hypotenuse and the picture said a was. A student who trusts both learns
# that letters are decoration -- the same lesson the mis-slotted triangles taught in fe.
#
# This is the sibling of triangle_side_conflict() above: same tag, same AB/BC/CA contract,
# and rule 63 again ("the words and the picture are the same figure"). geo-figures.js can
# already carry the letters -- sides="c = 3, a = ?, b = 4" renders them on the legs -- so
# this is a fixable turn, never a renderer limit.
#
# NARROW, in both of its halves:
#   (a) STRANDED -- the prose names sides by single letter AND a triangle tag is present
#       AND its sides= carries none of those letters AND its v= carries them as corners.
#       All four must hold. A triangle whose words name no letters is never judged; a
#       figure that letters its sides is never judged.
#   (b) MISLETTERED -- a side slot IS lettered, but with a letter that is not the lowercase
#       of the vertex opposite it. Judged only when v= names three distinct single letters,
#       so P,Q,R triangles and word labels are left alone.
_TRI_SIDE_LETTER = re.compile(r"(?<![A-Za-z])([a-z])(?![A-Za-z])\s*=")
_TRI_PYTHAG = re.compile(
    r"\ba\s*(?:²|\^2|squared)\s*(?:\+|plus)\s*b\s*(?:²|\^2|squared)\s*(?:=|equals)\s*"
    r"c\s*(?:²|\^2|squared)", re.I)
_TRI_NAMES_SIDE = re.compile(
    r"\b(?:side|leg|legs|sides|hypotenuse)\s+(?:is\s+)?([a-z])(?![A-Za-z])"
    r"|\b([a-z])\s*(?:²|\^2|squared)\b", re.I)


def triangle_letter_conflict(reply: str):
    """Return a description of a triangle whose words name sides by letter that the
    picture does not carry (or carries against the convention), or "". Never raises:
    any unexpected input yields "" (fail open)."""
    try:
        text = str(reply or "")
        prose = _TAG_SPLIT_RE.sub(" ", text) if "_TAG_SPLIT_RE" in globals() else \
            re.sub(r"\[\[[^\]]*\]\]", " ", text)
        named = set()
        if _TRI_PYTHAG.search(prose):
            named.update(("a", "b", "c"))
        for m in _TRI_NAMES_SIDE.finditer(prose):
            letter = (m.group(1) or m.group(2) or "").lower()
            if letter and letter not in ("a",) or (letter == "a" and m.group(2)):
                named.add(letter)
        named = {L for L in named if L.isalpha()}
        if not named:
            return ""
        for m in _TRI_TAG.finditer(text):
            attrs = {k.lower(): v for k, v in _TRI_ATTR.findall(m.group(1))}
            sides_raw = (attrs.get("sides") or "").strip()
            if not sides_raw:
                continue
            v = [s.strip() for s in (attrs.get("v") or "A,B,C").split(",")]
            sides = [s.strip() for s in sides_raw.split(",")]
            if len(v) != 3 or len(sides) != 3:
                continue
            lettered = {}
            for i, slot in enumerate(sides):
                lm = _TRI_SIDE_LETTER.search(slot)
                if lm:
                    lettered[i] = lm.group(1).lower()
            corners = {x.strip().lower() for x in v if len(x.strip()) == 1}
            # (a) the words name letters the picture puts only on the corners
            if not lettered and (named & corners):
                shown = ", ".join(s or "-" for s in sides)
                return ("your words name side{plural} {n}, but your [[triangle]] tag puts "
                        "{up} on the CORNERS (v=\"{v}\") and its sides hold {shown} -- so "
                        "nothing in the picture is called {n}, and the student hunts for "
                        "letters that are not there. Rule 63(d): letter the sides you talk "
                        "about, e.g. sides=\"c = 3, a = ?, b = 4\". A side's letter is the "
                        "lowercase of the vertex OPPOSITE it, so for the Pythagorean "
                        "theorem put the right angle at C and the hypotenuse AB is c."
                        ).format(plural="" if len(named) == 1 else "s",
                                 n=", ".join(sorted(named)),
                                 up=", ".join(sorted(named)).upper(),
                                 v=",".join(v), shown=shown)
            # (b) a lettered side that contradicts the opposite-vertex convention
            if lettered and len(corners) == 3:
                for i, letter in lettered.items():
                    opposite = v[(i + 2) % 3].strip().lower()
                    if letter != opposite:
                        pair = v[i].upper() + v[(i + 1) % 3].upper()
                        return ("your [[triangle]] tag letters side {pair} as \"{got}\", but "
                                "{pair} is opposite vertex {opp} -- so by the convention "
                                "every textbook uses it is side {want}. Rule 63(d): a side's "
                                "letter is the lowercase of the vertex OPPOSITE it. Letter it "
                                "{want}, or move the vertices."
                                ).format(pair=pair, got=letter, opp=opposite.upper(),
                                         want=opposite)
        return ""
    except Exception as exc:  # noqa: BLE001 -- referee crash = fail open, always
        print(f"[triangleletter] crashed (fail open): {exc}")
        _event("referee_crash", "triangleletter", str(exc))
        return ""


# =============================================================================
# THE ANSWERED-QUESTION CHECK (2026-08-11, build dh) -- rule 17 moves COVERED -> ENFORCED.
# -----------------------------------------------------------------------------
# First full audit, twice in one run, two courses apart: a worked card said
# "tickets cost: 3 × 2 = 6 dollars" while the prose asked "so what's 3 times 2?", and
# "f(a) = 2a + 1 = ?" stood on the board while the prose asked what 2(a)+1 looks like
# "written cleaner". A question the board has already answered CANNOT fail, and the
# student's "success" is then treated as evidence of understanding.
# NARROW, like every referee -- a false positive costs a real model call and (proven in
# build dg) can cost the student the good draft: it fires ONLY when the prose asks a
# lead-in question ("what's", "what do you get", "how much is") for A op B with explicit
# numbers, AND a board tag in the SAME reply states that exact A op B = C with a NUMERIC
# C. A pending "= ?" line never trips it -- that is rule 15 done right. Commutativity is
# honoured for + and ×. Offers are excluded the build-dg way.
_AQ_OPS = {"plus": "+", "add": "+", "added to": "+", "+": "+",
           "minus": "-", "take away": "-", "less": "-", "-": "-", "−": "-",
           "times": "*", "multiplied by": "*", "x": "*", "×": "*", "*": "*",
           "divided by": "/", "over": "/", "÷": "/", "/": "/"}
_AQ_Q = re.compile(
    r"\b(?:what'?s|what is|what do you get|what does that (?:come|work) (?:to|out to)|"
    r"how much is|so what'?s)\b[^.?!]*?"
    r"(\d+(?:\.\d+)?|" + _PR_NUMWORD + r")\s*"
    r"(plus|minus|times|multiplied by|divided by|added to|take away|[+\-−×x*/÷])\s*"
    r"(\d+(?:\.\d+)?|" + _PR_NUMWORD + r")", re.I)
_AQ_BOARD = re.compile(
    r"(\d+(?:\.\d+)?)\s*([+\-−×x*/÷])\s*(\d+(?:\.\d+)?)\s*=\s*(-?\d+(?:\.\d+)?)")


def prose_answered_question_conflict(reply: str):
    """Return a description of a question whose answer this reply's own board already
    states, or "". Never raises: any unexpected input yields "" (fail open)."""
    try:
        text = str(reply or "")
        prose = _spoken_only(text)
        asked = []
        for sent in _PQ_SENT_SPLIT.split(prose):
            sent = sent.strip()
            if not sent.endswith("?") or _pq_is_offer(sent):
                continue
            m = _AQ_Q.search(sent)
            if not m:
                continue
            a = _sc_val(m.group(1))
            op = _AQ_OPS.get(m.group(2).strip().lower())
            b = _sc_val(m.group(3))
            if a is None or op is None or b is None:
                continue
            asked.append((a, op, b, sent))
        if not asked:
            return ""
        stated = set()
        for tag in re.findall(r"\[\[[^\]]*\]\]", text):
            for m in _AQ_BOARD.finditer(tag):
                try:
                    a, b = float(m.group(1)), float(m.group(3))
                    float(m.group(4))          # the RHS must be numeric ("?" never is)
                except ValueError:
                    continue
                op = _AQ_OPS.get(m.group(2).strip().lower())
                if op is None:
                    continue
                stated.add((a, op, b))
                if op in ("+", "*"):
                    stated.add((b, op, a))
        for a, op, b, sent in asked:
            if (a, op, b) in stated:
                q = " ".join(sent.split())[:80]
                return ('you ask the student "{q}" while a board line in this same reply '
                        "already states that computation WITH its answer. Rule 17: a "
                        "question the board has answered cannot fail, and the success "
                        "that follows is not evidence. If you want the student to do the "
                        'step, write it PENDING -- like [[step eq="3 × 2 = ?"]] -- and '
                        "complete it only after they answer.").format(q=q)
        return ""
    except Exception as exc:  # noqa: BLE001 -- referee crash = fail open, always
        print(f"[answeredq] crashed (fail open): {exc}")
        _event("referee_crash", "answeredq", str(exc))
        return ""


# =============================================================================
# THE UNSPOKEN-PROBLEM CHECK (2026-08-11, build dh) -- rule 44 moves COVERED -> ENFORCED.
# -----------------------------------------------------------------------------
# First full audit, a prealgebra quiz turn: 'First question:
# [[step eq="Q1: Evaluate 5x - 2 when x = 4"]] What's the answer?' -- the problem
# existed only as text on the board. This is a VOICE classroom: some students are
# seven, some are dyslexic, some listen with the screen off to one side. A problem
# that was never spoken is a problem they cannot attempt, and their silence will read
# as a math failure in every number we report about them (rule 44's own words).
# NARROW: fires only when a pending "?"-line or a Q-numbered quiz line carries TWO or
# more numbers while the ENTIRE spoken prose asks a question yet contains NO number at
# all, in any spelling. If the tutor spoke even one number, we stay silent.
# BUILD eq (2026-08-12). The rule-44 referee used to give up the moment the SPOKEN text
# contained any number at all -- so "two numbers that multiply to 10 and add to 7" was
# enough to excuse never reading "x squared plus seven x plus ten equals zero" out loud.
# The honest question is not "does the prose contain a number" but "does the prose carry
# THIS problem's numbers". Every quantity the board line states has to appear in the
# words, as a numeral or as the word a person would say. Fractions are checked as a pair
# ("8/12" needs eight AND twelve, or the spoken "eight twelfths"), because that is the
# exact case the audits caught twice in one quiz.
_EQ_NUMWORD = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
               7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
               13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
               17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty",
               30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy",
               80: "eighty", 90: "ninety", 100: "hundred"}
# the spoken names of a fraction's bottom number ("8/12" -> "twelfths")
_EQ_DENOM_WORD = {2: "half|halves", 3: "third", 4: "fourth|quarter", 5: "fifth",
                  6: "sixth", 7: "seventh", 8: "eighth", 9: "ninth", 10: "tenth",
                  12: "twelfth", 16: "sixteenth", 100: "hundredth"}


def _pq_spoken_covers(prose: str, board_value: str) -> bool:
    """True if the SPOKEN words carry the numbers this board line states.

    Deliberately generous -- this decides whether to REGENERATE a reply, so it errs
    toward 'the tutor said it'. A single missing quantity is not enough; the words have
    to miss EVERY number the problem states before we call it unspoken."""
    try:
        low = " " + re.sub(r"[^a-z0-9/\.\s-]", " ", str(prose or "").lower()) + " "
        # a spoken fraction ("eight twelfths", "three fourths") counts for both halves
        frac = re.search(r"(\d+)\s*/\s*(\d+)", board_value or "")
        if frac:
            top, bot = int(frac.group(1)), int(frac.group(2))
            # BUILD gk (2026-08-16) -- THE HALVES MUST BE SPOKEN TOGETHER.
            # This used to look for the numerator ANYWHERE and the denominator ANYWHERE,
            # independently. The 2026-08-16 fractions audit walked straight through it:
            # the board said 3/4 + 1/4 = ? and the words said "three plus one really is
            # four" -- which is about the NUMERATORS, and never reads the problem at all --
            # yet "three" and "four" were both present, so the referee called it spoken and
            # the child was asked a question they had only ever seen written down. That is
            # precisely the failure rule 44 exists to stop, in the course whose students can
            # least afford it. A fraction now only counts as read when its two halves are
            # said TOGETHER -- "three fourths", "three over four", or the literal 3/4 --
            # which is the only way a listening student actually hears the quantity.
            if re.search(r"\b%d\s*/\s*%d\b" % (top, bot), low):
                return True
            tops = [re.escape(str(top))]
            if top in _EQ_NUMWORD:
                tops.append(re.escape(_EQ_NUMWORD[top]))
            # NOTE: _EQ_DENOM_WORD values are already alternations ("half|halves",
            # "fourth|quarter") -- group them, never escape them.
            bots = [re.escape(str(bot))]
            if bot in _EQ_DENOM_WORD:
                bots.append("(?:%s)" % _EQ_DENOM_WORD[bot])
            if bot in _EQ_NUMWORD:
                bots.append(re.escape(_EQ_NUMWORD[bot]))
            together = r"\b(?:%s)\b(?:\s+\w+){0,2}\s+(?:%s)s?\b" % (
                "|".join(tops), "|".join(bots))
            return bool(re.search(together, low))
        # BUILD gw (2026-08-17) -- THE DECIMAL MUST BE SPOKEN AS A QUANTITY, and this is
        # gk's fraction bug wearing a decimal point. The board said "2.6 + 1.35" and the
        # words said "Let's try ONE with a similar setup" -- and the digit-scatter fallback
        # below found the "1" of 1.35 inside the word "one", called the problem spoken, and
        # handed a listening student a problem they had only ever seen written down.
        # A decimal now only counts as read when its whole part is said next to "point"
        # (or "dollars", since money is a legitimate reading: "three dollars and ninety
        # seven cents" IS reading 3.97 aloud) -- or when the literal appears in the prose.
        decs = re.findall(r"\d+\.\d+", board_value or "")
        if decs:
            for d in decs:
                if re.search(r"(?<![\d.])" + re.escape(d) + r"(?![\d])", low):
                    return True
                whole = d.split(".")[0]
                forms = [re.escape(whole)]
                try:
                    w = _EQ_NUMWORD.get(int(whole))
                    if w:
                        forms.append(re.escape(w))
                except (TypeError, ValueError):
                    pass
                if re.search(r"\b(?:%s)\b(?:\s+\w+){0,2}\s+(?:point|dollars?)\b"
                             % "|".join(forms), low):
                    return True
            return False        # a decimal problem, never read as a decimal
        nums = [int(n) for n in re.findall(r"\b\d{1,4}\b", board_value or "")]
        if not nums:
            return True                      # nothing numeric to read aloud
        for n in nums:
            if re.search(r"\b%d\b" % n, low):
                return True
            w = _EQ_NUMWORD.get(n)
            if w and re.search(r"\b%s\b" % w, low):
                return True
        return False
    except Exception:                        # noqa: BLE001 -- fail open, always
        return True


def prose_unspoken_problem_conflict(reply: str):
    """Return a description of a board problem the spoken words never read aloud,
    or "". Never raises: any unexpected input yields "" (fail open)."""
    try:
        text = str(reply or "")
        prose = _spoken_only(text)
        low = prose.lower()
        if "?" not in prose and "your turn" not in low:
            return ""
        pend = []
        for tag in re.findall(r"\[\[\s*(?:" + "|".join(_PQ_BOARD_TAGS) + r")\b([^\]]*)\]\]",
                              text, re.I):
            for val in re.findall(r'"([^"]*)"', tag):
                if not ("?" in val or re.match(r"\s*Q\d+\s*:", val)):
                    continue
                # BUILD eq (2026-08-12) -- TWO BLIND SPOTS THE 2026-08-12 AUDITS WALKED
                # STRAIGHT THROUGH, six findings in five lessons.
                # (1) THE BAR WAS TWO NUMBERS. A fraction counts as ONE token by design
                #     (see _pq_numeric_tokens), so a whole quiz of "8/12 = ?" and
                #     "6/9 = ?" could never qualify no matter how silent the prose was --
                #     and "what's this fraction reduced to lowest terms?" is precisely
                #     the sentence a listening student cannot act on. A board problem
                #     needs ONE stated quantity to be worth reading aloud, not two.
                # (2) It must still be a PROBLEM, not a label: "Q1: ..." or a line that
                #     poses something with an operator or a fraction in it. A bare
                #     "denominator = ?" asks about the board, not for arithmetic.
                if _pq_numeric_tokens(val) < 1:
                    continue
                if not (re.match(r"\s*Q\d+\s*:", val)
                        or re.search(r"[+\-−×x*/÷^=]", val)
                        or re.search(r"\d+\s*/\s*\d+", val)):
                    continue
                spoken_here = _pq_spoken_covers(prose, val)
                if not spoken_here:
                    pend.append(" ".join(val.split()))
        if not pend:
            return ""
        return ('the board hands the student a problem -- "{p}" -- but the spoken words '
                "never read it: the prose asks its question without a single number in "
                "it. Rule 44: READ THE PROBLEM ALOUD, IN FULL, EVERY TIME -- this is a "
                "voice classroom, and a problem that exists only as text is a problem "
                "some students cannot attempt. Speak the whole problem the way a person "
                "says it, then ask.").format(p=pend[0][:70])
    except Exception as exc:  # noqa: BLE001 -- referee crash = fail open, always
        print(f"[unspoken] crashed (fail open): {exc}")
        _event("referee_crash", "unspoken", str(exc))
        return ""


# =============================================================================
# THE SCORE CHECK (2026-08-09, build ch) -- fourth part of the referee.
# -----------------------------------------------------------------------------
# Proactive audit #2 item 9. The server already recomputes every percentage from
# correct/total, so no percentage the model asserts is ever STORED. What nothing
# checked is what the student HEARS. The tally in [[quiz]] / [[check]] / [[finalexam]]
# is honest, and the sentence next to it is free to say "you passed!" to a discouraged
# child who scored 3 of 5. That is the same class of bug as the 2026-08-08 dimes
# contradiction -- the words disagreeing with the tag -- except this one lands on the
# progress bars, which are the product's central promise.
#
# Thresholds live in store.py; they are mirrored here as constants because tutor.py must
# not import the storage layer, and ruletests.py asserts the two never drift apart.
QUIZ_PASS_PCT = 80          # a topic quiz
UNIT_PASS_PCT = 90          # a Unit Quiz / end-of-unit check
FINAL_PASS_PCT = 90         # the Final Exam
_SCORE_TAGS = {"quiz": QUIZ_PASS_PCT, "check": UNIT_PASS_PCT, "finalexam": FINAL_PASS_PCT}
_SC_PASS_CLAIM = re.compile(
    r"\b(?:you(?:'ve| have)?\s+(?:just\s+)?(?:passed|mastered)|that'?s a pass|"
    r"you passed|passed it|unit (?:is )?mastered|you'?re through|that'?s a mastery)\b", re.I)
_SC_FAIL_CLAIM = re.compile(
    r"\b(?:did ?n'?t (?:quite )?pass|not (?:quite )?a pass|didn'?t make it|"
    r"we'?ll (?:try|take) (?:that|it|this) again|short of the bar)\b", re.I)
# NOTE the boundary: "percent" takes a \b, "%" must NOT. A trailing \b after "%" asks for
# a word character next to a non-word character, so "80% — great!" never matched at all and
# the whole percentage check was silently dead. Caught by the test battery on run two.
_SC_PCT = re.compile(r"(\d{1,3})\s*(?:%|percent\b)", re.I)
_SC_RESULT_CONTEXT = re.compile(
    r"\b(?:score[sd]?|you got|you'?ve got|you'?re at|you are at|result|that'?s|that is|"
    r"came out|ended up|you were|final tally|altogether that)\b", re.I)
_SC_BAR_CONTEXT = re.compile(
    r"\b(?:need|needs|needed|to pass|passing|the bar|or better|or higher|required|"
    r"requires|at least|cut ?off|takes|aiming for|target)\b", re.I)
_SC_FRACTION = re.compile(r"\b(\d{1,2}|" + _PR_NUMWORD + r")\s+out of\s+(\d{1,2}|" + _PR_NUMWORD + r")\b", re.I)


def _sc_val(token: str):
    try:
        return float(token) if re.match(r"^\d", token.strip()) else _pr_word_value(token)
    except (TypeError, ValueError):
        return None


# =============================================================================
# BUILD eq (2026-08-12) -- THE MALFORMED-TAG REFEREE
# =============================================================================
# The 2026-08-12 audit caught this on a Basic Math board:
#     [[choices options="yes, let's go! | show me one more]]
# The closing quote is missing. Traced through the page's own parser: the tag IS
# recognised, the attribute regex cannot match an unterminated quoted value, so it falls
# back to the next whitespace-delimited token and the child is shown ONE answer button
# reading   "yes,   -- and the second choice does not exist at all.
#
# EIGHT referees ran on that reply and not one of them looks at whether a tag is even
# well-formed. Every other referee asks whether the tutor said something WRONG; this one
# asks whether what he emitted can be drawn at all. A malformed tag is silent: nothing
# errors, the lesson continues, and only the student sees the broken control.
#
# DELIBERATELY NARROW -- this regenerates a reply, so it only fires on damage it can
# prove: an odd number of quotes inside a tag, an attribute whose value is unterminated,
# or a tag opened and never closed. Prose that merely contains "[[" is not a tag.
_EQ_TAGNAME = re.compile(r"\[\[\s*([\w-]+)")


def malformed_tag_conflict(reply: str):
    """Return a description of a board tag the page cannot parse, or "". Fail open."""
    try:
        text = str(reply or "")
        if "[[" not in text:
            return ""
        # 1. A tag opened and never closed swallows the rest of the reply. Count only
        #    REAL openings -- "[[" followed by a tag name. Prose that merely contains
        #    two brackets ("we write it like this: [[ ...") is not a tag and must not
        #    cost a regeneration.
        opens = len(re.findall(r"\[\[[\w-]+", text))   # "[[step", never "[[ is how a tag"
        closes = text.count("]]")
        if opens > closes:
            frag = text[text.rindex("[["):][:70]
            return ('a board tag is opened and never closed -- "{f}". The page reads to '
                    "the end of the reply looking for ]] and draws nothing, so the "
                    "student loses that control entirely. Close every tag."
                    ).format(f=" ".join(frag.split()))
        # 2. Inside each tag, quotes must pair up and every attr= must be terminated.
        for m in re.finditer(r"\[\[(.*?)\]\]", text, re.S):
            body = m.group(1)
            name_m = _EQ_TAGNAME.match("[[" + body)
            name = name_m.group(1).lower() if name_m else "?"
            if body.count('"') % 2:
                return ('the board tag [[{n} ...]] has an ODD number of quote marks, so '
                        'one of its values is never closed -- "{f}". The page cannot '
                        "parse that attribute: it falls back to the next word, and the "
                        "student sees a broken or missing control instead of what you "
                        "meant. Every attribute is name=\"value\", quotes balanced."
                        ).format(n=name, f=" ".join(("[[" + body + "]]").split())[:80])
            # an attribute that opens a quote with no closing quote before the tag ends
            for am in re.finditer(r'([\w-]+)\s*=\s*"', body):
                rest = body[am.end():]
                if '"' not in rest:
                    return ('the board tag [[{n} ...]] leaves {a}="..." unterminated -- '
                            '"{f}". The student sees a broken control. Close the quote.'
                            ).format(n=name, a=am.group(1),
                                     f=" ".join(("[[" + body + "]]").split())[:80])
        return ""
    except Exception as exc:  # noqa: BLE001 -- referee crash = fail open, always
        print(f"[malformed-tag] crashed (fail open): {exc}")
        _event("referee_crash", "malformed-tag", str(exc))
        return ""


def prose_score_conflict(reply: str):
    """Return a description of a spoken score that disagrees with the reply's own score
    tag, or "". Never raises: any unexpected input yields "" (fail open)."""
    try:
        text = str(reply or "")
        scored = []
        for name, attrs in re.findall(r"\[\[\s*(quiz|check|finalexam)\b([^\]]*)\]\]", text, re.I):
            a = dict((k.lower(), v) for k, v in re.findall(r'([\w-]+)\s*=\s*"([^"]*)"', attrs))
            try:
                c, t = int(a.get("correct", "")), int(a.get("total", ""))
            except (TypeError, ValueError):
                continue
            if t <= 0:
                continue
            scored.append((name.lower(), c, t, (c * 100) // t, _SCORE_TAGS[name.lower()]))
        if not scored:
            return ""
        prose = _spoken_only(text)
        for name, c, t, pct, thr in scored:
            passed = pct >= thr
            if not passed and _SC_PASS_CLAIM.search(prose):
                return ('your words tell the student they passed, but your own [[{n}]] tag '
                        'says {c} of {t} -- {p}%, and the bar is {b}%. Rule 45: the tally is '
                        'arithmetic, not judgment. Say the real score warmly and use rule 35 '
                        'to make the next step feel like a plan, but never call a fail a '
                        'pass.').format(n=name, c=c, t=t, p=pct, b=thr)
            if passed and _SC_FAIL_CLAIM.search(prose):
                return ('your words tell the student they did not pass, but your own [[{n}]] '
                        'tag says {c} of {t} -- {p}%, which clears the {b}% bar. Rule 45: say '
                        'the real result.').format(n=name, c=c, t=t, p=pct, b=thr)
            # Only percentages spoken ABOUT THE RESULT count. In Pre-Algebra half the
            # lesson is percentages -- "what is 25% of 80?" is the problem, not a score
            # claim, and treating it as one flagged a perfectly good reply on test run
            # three. So a sentence has to sound like it is reporting the outcome.
            pct_hits = []
            for sent in re.split(r"(?<=[.!?])\s+|\n+", prose):
                if not _SC_RESULT_CONTEXT.search(sent):
                    continue
                for mm in _SC_PCT.finditer(sent):
                    pct_hits.append((int(mm.group(1)), sent, mm.start(), mm.end()))
            for v, sent, s0, s1 in pct_hits:
                if v == pct:
                    continue
                # The BAR is fair to quote -- "you need 80% to pass" is teaching, not a
                # score claim -- but only when it reads like the bar. Saying "that is 80%"
                # over a 60% tally is the inflation this check exists to stop, and letting
                # the threshold through unconditionally missed exactly that case on the
                # first test run.
                near = sent[max(0, s0 - 45):s1 + 45].lower()
                if v == thr and _SC_BAR_CONTEXT.search(near):
                    continue
                return ('you say "{v}%" but your own [[{n}]] tag is {c} of {t}, which is '
                        '{p}%. Rule 45: the only percentage you may state as the score is '
                        'the one your tally actually gives.').format(
                            v=v, n=name, c=c, t=t, p=pct)
            for num, den in _SC_FRACTION.findall(prose):
                nv, dv = _sc_val(num), _sc_val(den)
                if nv is None or dv is None or int(dv) != t:
                    continue
                if int(nv) != c:
                    return ('you say "{n} out of {d}" but your own [[{g}]] tag records {c} of '
                            '{t}. Rule 45: the score you SAY is the score you WROTE.').format(
                                n=int(nv), d=int(dv), g=name, c=c, t=t)
        return ""
    except Exception as exc:  # noqa: BLE001 -- referee crash = fail open, always
        print(f"[scorecheck] crashed (fail open): {exc}")
        _event("referee_crash", "scorecheck", str(exc))
        return ""


# =============================================================================
# THE CAPTION CHECK (2026-08-14, build gj) -- rule 41, and the tenth referee.
# -----------------------------------------------------------------------------
# From the 2026-08-16 lesson audits: four figures drawn with no caption at all --
# a fractions pie and three cookie pictures, in the two lessons aimed at the
# youngest and most confused students. Rule 41 is not a preference, it is written
# absolutely: "Every figure tag takes caption='...'. Use it, every time."
#
# Why it earns a regeneration rather than a shrug. Rule 41's own words: a picture
# with no caption "hands the student back the one piece of work the picture was
# supposed to do for them -- working out what they are meant to be looking at --
# and a student who is already lost will look at the wrong part of it and feel
# worse." Both audited lessons were exactly that student.
#
# This is the cheapest possible referee: no model call to detect, no judgement, no
# false positives to argue about. A figure either carries a caption or it does not.
# All 306 canonical foundation scripts already pass it, so it never fights the
# authored content -- it only catches what the model improvises.
# -----------------------------------------------------------------------------
# build hh: this was a LITERAL RE-DECLARATION of FIGURE_TAGS -- the same 22 members,
# re-typed by hand in a different order, in the same file. The exact drift class
# tags.py exists to kill: one edit to one list and the caption referee and the visual
# referee would have quietly disagreed about what counts as a figure.
_FIGURE_TAGS = FIGURE_TAGS
_FIG_RE = re.compile(r"\[\[\s*(" + "|".join(_FIGURE_TAGS) + r")\b([^\]]*)\]\]", re.I)
_CAPTION_RE = re.compile(r'\bcaption\s*=\s*"\s*([^"]*?)\s*"')


def missing_caption_conflict(reply: str):
    """Return a description of a picture drawn with no caption, or "".
    Never raises: any unexpected input yields "" (fail open)."""
    try:
        for m in _FIG_RE.finditer(str(reply or "")):
            cap = _CAPTION_RE.search(m.group(2))
            if cap and cap.group(1).strip():
                continue
            kind = m.group(1).lower()
            return ('you drew a picture -- [[{k} ...]] -- with no caption. Rule 41: EVERY '
                    'figure carries caption="...", every time, and it names what to NOTICE '
                    'rather than what the thing is ("both are four steps from zero", not "a '
                    'number line"). A picture with no caption hands the student back the one '
                    'job the picture was there to do for them, and a student who is already '
                    'lost will look at the wrong part of it and feel worse. Add the caption '
                    'and say its idea out loud too.').format(k=kind)
        return ""
    except Exception as exc:  # noqa: BLE001 -- referee crash = fail open, always
        print(f"[caption] crashed (fail open): {exc}")
        _event("referee_crash", "caption", str(exc))
        return ""


# =============================================================================
# THE SELF-CORRECTION CHECK (2026-08-16, build gl) -- the eleventh referee.
# -----------------------------------------------------------------------------
# The one HIGH finding in the 2026-08-16 audits, quoted exactly:
#
#     "3/4 is smaller than 3/4... wait, let's just confirm: 3 1/4 minus 1 3/4
#      really is 1 1/2."
#
# Read what the child actually received. A false comparison, then the grown-up
# visibly losing confidence in their own sentence, then a recovery -- all shipped.
# The ACCURACY block has always said "fix it BEFORE you say it"; nothing checked
# whether the fixing happened in private. Build gl adds the missing half of that
# rule to every course ("fix it SILENTLY: never let the student watch you change
# your mind") and this referee, which is what makes it true rather than hoped for.
#
# Why it matters more here than in most products: these students are with a tutor
# because they are already unsure. A child who is lost does not read "wait, let me
# check that" as diligence. They read it as the grown-up not knowing either, and
# that is the moment a struggling student stops trusting the room.
#
# DELIBERATELY NARROW. Correcting the STUDENT is the job and must never be touched:
# "actually comes out to 3.45", "not quite -- it's 11", "let's check that one" all
# pass. This fires only on the tutor retracting ITSELF -- a trailing-off "... wait,",
# a "hold on", "scratch that", "actually, no", "my mistake". Fails open.
# -----------------------------------------------------------------------------
_SELF_CORRECT = (
    re.compile(r"\.\.\.\s*wait\b", re.I),
    re.compile(r"\bwait,\s*(?:let'?s|let me|actually|no\b|hang on|i )", re.I),
    # build gw (2026-08-17): "...to". Found by sweeping the canonical scripts, where TWO
    # of them say "so hold on to this" and "the word common is the one to hold on to" --
    # meaning gl has been REGENERATING authored content every time the tutor tried to
    # deliver those scripts. A referee that fights the foundation library is worse than no
    # referee: it burns a model call and can cost the student the good draft (build dg).
    # "hold on" is a self-correction; "hold on TO something" is a teaching instruction.
    re.compile(r"\b(?:hold on|hang on)\b(?!\s+to\b)[,\s]", re.I),
    re.compile(r"\bscratch that\b", re.I),
    re.compile(r"\blet me (?:re-?check|redo|try that again|start over)\b", re.I),
    re.compile(r"\bignore (?:that|what i just)\b", re.I),
    re.compile(r"\bactually,?\s*no\b", re.I),
    re.compile(r"\b(?:my mistake|my bad|oops)\b", re.I),
    re.compile(r"\bsorry,?\s*(?:i mean|that'?s wrong|let me)\b", re.I),
    re.compile(r"\bthat'?s not right\b[^.?!]{0,20}\blet me\b", re.I),
)


def self_correction_conflict(reply: str):
    """Return a description of the tutor visibly correcting ITSELF, or "".
    Never raises: any unexpected input yields "" (fail open)."""
    try:
        prose = _spoken_only(str(reply or ""))
        for pat in _SELF_CORRECT:
            m = pat.search(prose)
            if not m:
                continue
            frag = " ".join(prose[max(0, m.start() - 45):m.end() + 25].split())
            return ('you changed your mind out loud -- "...{f}...". Check it BEFORE you '
                    'speak, then say the checked version ONCE. A student watching you '
                    'retract your own sentence does not read it as care; a child who is '
                    'already unsure reads it as the grown-up not knowing either, and that '
                    'is the moment they stop trusting the room. Work it out, decide, and '
                    'give them only the answer you have checked.').format(f=frag)
        return ""
    except Exception as exc:  # noqa: BLE001 -- referee crash = fail open, always
        print(f"[selfcorrect] crashed (fail open): {exc}")
        _event("referee_crash", "selfcorrect", str(exc))
        return ""


# =============================================================================
# THE NARRATED-METHOD CHECK (2026-08-16, build gm) -- the twelfth referee.
# -----------------------------------------------------------------------------
# Rule 43 already says this, in these words, and it was written FROM A LIVE CATCH:
#
#     "A bare right answer shows you NO method: never narrate one onto it ('you
#      borrowed across those columns perfectly', 'nice work converting that in your
#      head' -- both said, 2026-08-13, to students who had typed only a number)."
#
# Three days later, 2026-08-16, the audits caught it again. The student typed, in
# full: "1 1/2. Next." The tutor replied: "that regrouping is exactly the move that
# trips people up, and you nailed it clean." No regrouping was ever shown to it.
#
# A rule written from a real incident, that then fails again in the same month, is
# not a rule -- it is a wish. This is the enforcement.
#
# Why it is worth a regeneration. Rule 43's own reasoning: crediting an unperformed
# step "teaches that the step is a word rather than an act". A child who is praised
# for regrouping they did not do learns that producing the number is what earns the
# praise -- which is the exact habit a tutor exists to break. And the parent reading
# that transcript is being told something about their child that is not true.
#
# NARROW, and it errs toward silence. It fires only when BOTH hold: the student's
# message shows no working at all (short, no operators, no method words), AND the
# reply claims they performed a NAMED procedure. Praising the answer is untouched --
# "exactly right, three fourths!" is exactly what rule 43 asks for instead. A reply
# that ASKS how they did it (rule 59's question) is never flagged.
# -----------------------------------------------------------------------------
_NM_STUDENT_SHOWED_WORK = re.compile(
    # What counts as the student SHOWING working. Two bugs were found writing this and
    # both are worth remembering: a bare fraction ("1 1/2", "3/4") is an ANSWER, not
    # working; and a bare "Next." is a student DEMANDING the next problem -- the very
    # opposite of showing method -- yet an earlier version read it as the sequence word
    # in "first, then, next" and fell silent on the exact case this referee exists for.
    r"[+\u00d7\u00f7^]"          # a bare "=" is handled separately: see the note below
    r"|\b(?:because|since|common denominator)\b"
    r"|\bi (?:did|used|got|divided|multiplied|subtracted|added|borrowed|regrouped|"
    r"flipped|cancell?ed|factored|carried|converted|substituted|simplified|split|took)\b"
    r"|\b(?:first|then|so|and) i\b"
    r"|\b(?:divided|multiplied|subtracted|added|borrowed|regrouped|flipped|cancell?ed|"
    r"factored|carried|converted|substituted) (?:by|it|them|the|from)\b"
    r"|\b(?:times|plus|minus|over)\b", re.I)
_NM_CREDIT = (
    re.compile(r"\byou (?:borrowed|regrouped|factored|cancell?ed|substituted|distributed|"
               r"simplified|converted|flipped|cross-?multiplied|lined (?:it|them) up|"
               r"carried|renamed|reduced)\b", re.I),
    re.compile(r"\bthat (?:regrouping|borrowing|factoring|substitution|cancelling|"
               r"canceling|conversion|method|approach|strategy|technique) (?:is|was)\b", re.I),
    re.compile(r"\bthe way you (?:did|worked|handled|set|solved)\b", re.I),
    re.compile(r"\byour (?:method|approach|working|reasoning|strategy) (?:is|was|there)\b", re.I),
    re.compile(r"\bnice work (?:converting|borrowing|regrouping|factoring|simplifying)\b", re.I),
)
_NM_ASKS_HOW = re.compile(r"\bhow (?:did|d'?you|do you) (?:you )?(?:get|work|do|find)\b", re.I)

# BUILD gv (2026-08-17) -- THE TOTALITY CLAIM, which walked straight past everything above.
# From the day's audit (returning-student, algebra2). The tutor wrote every line of the
# procedure and asked two sub-questions; the student answered them -- "It's (x + 4)², and
# -16 + 10 is -6" -- and was told:
#
#     "Nice work -- you completed the square start to finish on your own."
#
# gm's gates all let this through, correctly by their own terms: the student DID show
# working, so "credit away" fired. But the question gm asks is "did they show A method?",
# and the question this sentence begs is "did they do THE WHOLE THING?" -- and they did
# not. Answering two sub-steps of a procedure somebody else set up is not doing it start
# to finish, and a student told otherwise learns that supplying the missing number IS the
# procedure. That is rule 43's own harm, one scale up.
#
# NARROW, and narrower than it first looks. It requires a claim of TOTALITY attached to a
# NAMED PROCEDURE. "You just solved your homework problem all by yourself!" -- said to an
# eight-year-old who answered 4/4 -- is warm, arguable, and deliberately NOT caught: the
# claim is about a problem they did answer, not about a multi-step procedure the tutor
# performed for them.
_NM_TOTALITY = re.compile(
    r"\b(?:start to finish|from start to finish|(?:the|that|this) whole (?:thing|way|process)|"
    r"all (?:on your own|by yourself)|entirely (?:on your own|by yourself)|"
    r"completely on your own|without (?:any )?help from me|every step (?:of it )?yourself)\b",
    re.I)
_NM_PROCEDURE = re.compile(
    r"\b(?:completed the square|completing the square|factored|factoring|regrouped|"
    r"regrouping|borrowed|borrowing|distributed|distributing|simplified|simplifying|"
    r"cross-?multiplied|long division|the quadratic formula|substituted|substitution|"
    r"converted|conversion|solved (?:the|that) (?:equation|system))\b", re.I)


def narrated_method_conflict(reply: str, student_message: str = ""):
    """Return a description of a method credited to a student who never showed one,
    or "". Never raises: any unexpected input yields "" (fail open)."""
    try:
        said = " ".join(str(student_message or "").split())
        if not said:
            return ""
        # build gv: THE TOTALITY BRANCH RUNS FIRST, because it asks a different question.
        # Everything below asks "did they show A method?"; this asks "did they do THE WHOLE
        # PROCEDURE?" -- and a fragment cannot contain a whole procedure however much
        # working it shows. Fires only when a totality phrase and a NAMED procedure appear
        # together, so ordinary warmth ("you solved it all by yourself") is untouched.
        prose_all = _spoken_only(str(reply or ""))
        if (len(said.split()) <= 15 and _NM_TOTALITY.search(prose_all)
                and _NM_PROCEDURE.search(prose_all)):
            tm = _NM_TOTALITY.search(prose_all)
            return ('you told the student they did it "{t}" -- but all they sent was "{s}", '
                    "which is an answer to a step, not a whole procedure. You wrote the "
                    "setup and every line of it. Rule 43: crediting work you performed "
                    "teaches that supplying the missing number IS the procedure, and it "
                    "tells their parent something untrue. Credit exactly what they did: "
                    'name the pieces they supplied.').format(
                        t=tm.group(0), s=said[:48])
        if len(said.split()) > 12 or _NM_STUDENT_SHOWED_WORK.search(said):
            return ""                      # they DID show working -- credit away
        # An equals sign is only WORKING when there is a computation around it. "x = 5"
        # is an answer written the way algebra writes answers; "5.20 - 1.75 = 3.45" is
        # someone showing their arithmetic. Counting the numbers separates the two.
        if "=" in said and len(re.findall(r"\d+(?:\.\d+)?", said)) >= 2:
            return ""
        prose = _spoken_only(str(reply or ""))
        if _NM_ASKS_HOW.search(prose):
            return ""                      # he asked rule 59's question: exactly right
        for pat in _NM_CREDIT:
            m = pat.search(prose)
            if not m:
                continue
            return ('you credited a method the student never showed you -- "{c}" -- when all '
                    'they sent was "{s}". Rule 43: you perceive exactly two things, their '
                    'words and your own board, and a bare right answer shows you NO method. '
                    'Crediting an unperformed step teaches that the step is a word rather '
                    'than an act, and it tells their parent something untrue. Praise the '
                    'ANSWER, and if the method matters, ask for it: "how did you get that?"'
                    ).format(c=" ".join(prose[m.start():m.end() + 30].split()), s=said[:40])
        return ""
    except Exception as exc:  # noqa: BLE001 -- referee crash = fail open, always
        print(f"[narrated] crashed (fail open): {exc}")
        _event("referee_crash", "narrated", str(exc))
        return ""


def prose_board_conflict(reply: str, student_message: str = "", expected_unit=None,
                         allowed_units=None, record=None, heard=None):
    """Return a short description of a prose-vs-board contradiction, or "" if clean.
    Never raises: any unexpected input yields "" (fail open).

    TWENTY-FOUR referees ride this sweep (hm added the unitplan check, ho the
    record-claim check, hr the story-units check, hz the promised-comparison
    check, ia the quiz-term check -- fed `heard`, the turn's original conversation
    text, by _create_verified -- and ib the self-contained-question check; the
    original twelve are listed below, the rest are named at their call
    sites): a malformed tag (build eq), a picture promised and never
    drawn (rule 7), a computation asked with no pending line on the board (rule 15), a
    spoken score that disagrees with the reply's own score tag (rule 45), the tutor
    answering its OWN question in the same breath (rule 39b -- wait time), a question
    this reply's own board already answers (rule 17, build dh), a board problem the
    spoken words never read aloud (rule 44, build dh), a board notation violation
    (rules 27/15/54, builds dk/dl), a right triangle whose hypotenuse slot cannot be
    the hypotenuse (rule 63c, build fe), then spoken numbers that disagree with the
    board's own written conclusion (rule 18b)."""
    try:
        # build eq: FIRST -- if a tag cannot be parsed, every other referee below is
        # reading a board the student will never actually see.
        malformed = malformed_tag_conflict(reply)
        if malformed:
            _event("referee_fire", "malformed-tag", malformed)
            return malformed
        # build gj: second, because an uncaptioned picture is the cheapest defect to
        # find and one of the most expensive to a lost student (rule 41).
        caption = missing_caption_conflict(reply)
        if caption:
            _event("referee_fire", "caption", caption)
            return caption
        # build gl: third, and cheap -- the tutor must never be seen changing its mind.
        selfcorrect = self_correction_conflict(reply)
        if selfcorrect:
            _event("referee_fire", "selfcorrect", selfcorrect)
            return selfcorrect
        # build gm: fourth -- never credit a method the student did not show (rule 43).
        narrated = narrated_method_conflict(reply, student_message)
        if narrated:
            _event("referee_fire", "narrated", narrated)
            return narrated
        visual = prose_visual_conflict(reply, student_message)
        if visual:
            _event("referee_fire", "vischeck", visual)
            return visual
        pending = prose_pending_question_conflict(reply)
        if pending:
            _event("referee_fire", "pendcheck", pending)
            return pending
        score = prose_score_conflict(reply)
        if score:
            _event("referee_fire", "scorecheck", score)
            return score
        selfans = prose_self_answer_conflict(reply)
        if selfans:
            _event("referee_fire", "selfanswer", selfans)
            return selfans
        answered = prose_answered_question_conflict(reply)
        if answered:
            _event("referee_fire", "answeredq", answered)
            return answered
        unspoken = prose_unspoken_problem_conflict(reply)
        if unspoken:
            _event("referee_fire", "unspoken", unspoken)
            return unspoken
        boardnote = board_notation_conflict(reply)
        if boardnote:
            _event("referee_fire", "boardnote", boardnote)
            return boardnote
        triangle = triangle_side_conflict(reply)
        if triangle:
            _event("referee_fire", "triangleslot", triangle)
            return triangle
        # build gn: THIRTEENTH -- immediately after its sibling, because both read the
        # same [[triangle]] tag and the slot check is the cheaper of the two.
        triletter = triangle_letter_conflict(reply)
        if triletter:
            _event("referee_fire", "triangleletter", triletter)
            return triletter
        # build gy: EIGHTEENTH -- the like-denominator rule spoken as a universal (rule 61).
        frac61 = fraction_rule_unconditioned(reply)
        if frac61:
            _event("referee_fire", "frac61", frac61)
            return frac61
        # build hr: TWENTY-FIRST -- a story that adds money to objects (rule 32b,
        # written from the night watch's first confirmed catch). Reads only the
        # reply's own prose, so it rides here with the other reply-only checks.
        storyunits = story_units_conflict(reply)
        if storyunits:
            _event("referee_fire", "storyunits", storyunits)
            return storyunits
        # build hz: TWENTY-SECOND -- a right-angle comparison spoken over a board
        # that holds no right angle (rule 63e, written from Jim's live catch).
        # Reads only the reply's own prose and tags, so it rides here with the
        # other reply-only checks.
        anglecompare = angle_compare_conflict(reply)
        if anglecompare:
            _event("referee_fire", "anglecompare", anglecompare)
            return anglecompare
        # build ib: TWENTY-FOURTH -- a numbered quiz question that states its own
        # answer (rule 47g, from the same live quiz run as ia). Reply-only, so it
        # rides here.
        selfquiz = question_self_contained_conflict(reply)
        if selfquiz:
            _event("referee_fire", "selfquiz", selfquiz)
            return selfquiz
        # build ia: TWENTY-THIRD -- a quiz choice built on terms this conversation
        # never taught (rule 47e). The only referee fed the conversation's own text
        # (`heard`, from _create_verified's ORIGINAL messages); silent when the
        # caller cannot know.
        quizterm = quiz_term_conflict(reply, heard)
        if quizterm:
            _event("referee_fire", "quizterm", quizterm)
            return quizterm
        # build gx: SEVENTEENTH -- a request to be shown, refused (rule 65).
        refused = refused_demonstration_conflict(reply, student_message)
        if refused:
            _event("referee_fire", "refusedshow", refused)
            return refused
        # build gu: SIXTEENTH -- rule 47(d), whose founding sentence reappeared verbatim
        # six days after the rule was written from it.
        coldquiz = cold_quiz_conflict(reply)
        if coldquiz:
            _event("referee_fire", "coldquiz", coldquiz)
            return coldquiz
        # build gr: FIFTEENTH -- it reads the student's own message, which is already here.
        answersign = answer_sign_conflict(reply, student_message)
        if answersign:
            _event("referee_fire", "answersign", answersign)
            return answersign
        # build gn: FOURTEENTH -- and the only referee that needs a fact from OUTSIDE the
        # reply, so it is wired here, after everything the reply can be judged against on
        # its own. Silent whenever the caller does not know the unit.
        unitclaim = unit_claim_conflict(reply, expected_unit)
        if unitclaim:
            _event("referee_fire", "unitclaim", unitclaim)
            return unitclaim
        # build hm: NINETEENTH -- its sibling in every way: the second referee fed a
        # fact from outside the reply (the record's allowed units, main._unit_allowed_set),
        # judging the TAG where unitclaim judges the PROSE. Silent when the caller does
        # not know (practice/topic lanes, nightwatch's synthetic students).
        unitplan = unitplan_conflict(reply, allowed_units)
        if unitplan:
            _event("referee_fire", "unitplanref", unitplan)
            return unitplan
        # build ho: TWENTIETH -- claims about the past, judged by the record that
        # actually holds the past (the count-claim probe's promotion). Silent when
        # the caller passes no record.
        recordclaim = record_claim_conflict(reply, record)
        if recordclaim:
            _event("referee_fire", "recordclaim", recordclaim)
            return recordclaim
        text = str(reply or "")
        # 1. the board's labeled conclusions, from this reply's own tags
        labeled = {}
        for tag in _STEP_TAG_RE.findall(text):
            for val in re.findall(r'"([^"]*)"', tag):
                m = _PR_BOARD_LINE.match(val.strip())
                if not m:
                    continue
                label = m.group(1).strip().lower()
                if not label or label in ("http", "https"):
                    continue
                try:
                    labeled[label] = (float(m.group(3)), m.group(2))
                except ValueError:
                    pass
        if not labeled:
            return ""
        # 2. the SPOKEN text only (tags stripped -- the student never hears them)
        prose = re.sub(r"\[\[[^\]]*\]\]", " ", text)
        prose = re.sub(r"\[\[[\s\S]*$", " ", prose)
        spoken_numbers = _pr_numbers_in(prose)
        low = prose.lower()
        for label, (result, operands) in labeled.items():
            # 4. if the words DO say the board's number anywhere, there is no contradiction
            if result in spoken_numbers:
                continue
            pat = re.compile(r"(-?\d+(?:\.\d+)?|" + _PR_NUMWORD + r")\s+" + re.escape(label) + r"\b")
            for hit in pat.findall(low):
                try:
                    claimed = float(hit) if re.match(r"^-?\d", hit) else _pr_word_value(hit)
                except ValueError:
                    claimed = None
                if claimed is None:
                    continue
                claimed = float(claimed)
                if claimed == result:
                    continue
                # 5. an operand of the same line is fair to mention in passing
                if claimed in _pr_numbers_in(operands):
                    continue
                _d18 = ('your spoken words say "{c} {lab}", but your own board line for '
                        '"{lab}" concludes {r}. Rule 18(b): the numbers you SAY must match '
                        'the numbers you WRITE.').format(
                            c=(int(claimed) if float(claimed).is_integer() else claimed),
                            lab=label,
                            r=(int(result) if float(result).is_integer() else result))
                _event("referee_fire", "prose-numbers", _d18)
                return _d18
        return ""
    except Exception as exc:  # noqa: BLE001 -- referee crash = fail open, always
        print(f"[prosecheck] crashed (fail open): {exc}")
        _event("referee_crash", "prosecheck", str(exc))
        return ""


_PROSE_NUDGE = (
    "(SYSTEM: A consistency check found a contradiction in your previous draft: {detail} "
    "The student NEVER saw that draft. Write your reply again from scratch -- same warm "
    "teaching flow -- so that what you SAY and what is actually on the board agree: every "
    "picture you mention is DRAWN by a tag in this same reply, and every number you say "
    "matches the number you write. Your new reply must STAND ALONE: the student saw and "
    "heard NOTHING of the discarded draft, so any worked example, definition, or board "
    "line they need must appear here IN FULL -- never open mid-thought, never say 'so' "
    "about a result you have not shown in THIS reply, never refer to anything only the "
    "draft contained. If the student's answer was wrong, coach the recount "
    "(rules 18 and 22); do not adopt their number. Do not mention this note or any "
    "checking.)")


MATHCHECK_MAX_ATTEMPTS = 3   # 1 normal attempt + up to 2 corrected retries

_MATHCHECK_NUDGE = (
    "(SYSTEM: A math engine checked your previous draft and found an error: {detail}. "
    "The student NEVER saw that draft. Write your reply again from scratch with the "
    "correct math -- same warm teaching flow, same board tags, corrected numbers and "
    "corrected [[verify]] tag(s). Your new reply must STAND ALONE: the student saw and "
    "heard nothing of the discarded draft, so everything they need must appear here in "
    "full -- never open mid-thought or build on something only the draft contained. "
    "Do not mention this note, the mistake, or any checking.)")


def _log_brain_usage(meta, model, tokens, attempts, verify_status):
    """Hand one brain turn's consumption to the store (fire-and-forget; never raises)."""
    if store is None or not meta:
        return
    try:
        store.log_usage(kind="brain", code=meta.get("code", ""), course=meta.get("course", ""),
                        mode=meta.get("mode", ""), model=model,
                        input_tokens=tokens.get("in", 0), output_tokens=tokens.get("out", 0),
                        cache_read_tokens=tokens.get("cr", 0), cache_write_tokens=tokens.get("cw", 0),
                        attempts=attempts, verify_status=verify_status)
    except Exception as exc:  # noqa: BLE001
        print(f"[usage] log failed (non-fatal): {exc}")


def _add_usage(tokens, response):
    """Accumulate the token counts the API just reported into `tokens` (in place)."""
    u = getattr(response, "usage", None)
    if u is None:
        return
    tokens["in"] = tokens.get("in", 0) + int(getattr(u, "input_tokens", 0) or 0)
    tokens["out"] = tokens.get("out", 0) + int(getattr(u, "output_tokens", 0) or 0)
    tokens["cr"] = tokens.get("cr", 0) + int(getattr(u, "cache_read_input_tokens", 0) or 0)
    tokens["cw"] = tokens.get("cw", 0) + int(getattr(u, "cache_creation_input_tokens", 0) or 0)


# BUILD dg (2026-08-11): the continuation is NEGOTIATED, and the ceiling rose.
# The first full audit's Render logs showed claude-sonnet-5 intermittently REJECTING the
# assistant-prefill continuation with a 400 that names its objection ("This model does
# not support assistant message prefill. The conversation must end with a user
# message."). Intermittent is worse than always: it looked like it worked. Every
# rejection surfaced to the student as a stumble. Same philosophy as the build-cz token
# parameter: the API SAYS what it will not accept, so take it at its word -- try prefill
# (seamless when accepted), and on that named 400 switch to a continuation nudge in a
# user message and remember the choice for the rest of the process. Never guessed from
# the model name; names change, and guessing is how you ship a break.
_PREFILL_OK: dict = {}    # model name -> False once the API has refused prefill once

_CONTINUE_NUDGE = (
    "(SYSTEM: Your reply above was cut off by a length limit, mid-flow. Continue it "
    "EXACTLY from where it stopped: output ONLY the continuation -- no greeting, no "
    "recap, no repeated words -- and close any unfinished board tag first. The student "
    "will see your earlier text and this continuation joined as one message.)")

# A CEILING, not a target -- normal turns end far under it and unused headroom costs
# nothing. Raised 1600 -> 3000 (build dg): the audit logs showed tag-heavy teaching
# turns hitting 1600 CONSTANTLY, and five replies shipped as admitted partials in forty
# minutes. Referee retries multiply the exposure, so the ceiling must fit a long,
# figure-heavy teaching turn with room to spare.
MAX_REPLY_TOKENS = 3000


def _is_prefill_rejection(exc) -> bool:
    """True when the API's own words say it refused the assistant-prefill shape."""
    msg = str(exc).lower()
    return "prefill" in msg or "must end with a user message" in msg


def _create_full(client, model, system_blocks, msgs, tokens, log_prefix=""):
    """One LOGICAL model turn that can never be silently truncated. 2026-08-08 (Jim's
    live freeze in Basic Math): the first teaching turn -- tag-heavy ([[today]],
    [[unitplan]], goals, objects) -- hit the old 1200-token ceiling mid-tag; the client
    stripped the dangling tag and the student saw the single word "Let" with an empty
    board and no answer buttons. Nothing anywhere checked stop_reason.
    Now: if the response stops at the max_tokens ceiling (stop_reason == "max_tokens"),
    the model is asked to continue exactly where it stopped -- by assistant prefill when
    the model accepts that shape, by a user-message nudge when it does not (build dg;
    see _PREFILL_OK above) -- and the pieces are stitched together. Up to 2
    continuations (~9000 tokens total -- far beyond any real teaching turn), then we
    return whatever we have rather than loop forever."""
    reply = ""
    hop = 0
    while hop < 3:
        if not reply:
            convo = msgs
        elif _PREFILL_OK.get(model, True):
            convo = msgs + [{"role": "assistant", "content": reply.rstrip()}]
        else:
            convo = msgs + [{"role": "assistant", "content": reply.rstrip()},
                            {"role": "user", "content": _CONTINUE_NUDGE}]
        try:
            response = client.messages.create(
                model=model,
                max_tokens=MAX_REPLY_TOKENS,
                system=system_blocks,
                messages=convo,
            )
        except Exception as exc:  # noqa: BLE001 -- only the NAMED rejection is handled
            if reply and _PREFILL_OK.get(model, True) and _is_prefill_rejection(exc):
                print(f"[tutor]{log_prefix} model refuses assistant prefill -- switching "
                      f"continuations to a user-message nudge for the rest of this run")
                _PREFILL_OK[model] = False
                continue          # retry the SAME hop in the fallback shape
            raise
        part = "".join(block.text for block in response.content
                       if getattr(block, "type", None) == "text")
        _add_usage(tokens, response)
        reply = (reply.rstrip() + part) if reply else part
        if getattr(response, "stop_reason", "") != "max_tokens":
            break
        hop += 1
        if hop < 3:
            print(f"[tutor]{log_prefix} reply hit max_tokens -- continuing (hop {hop}/2)")
        else:
            print(f"[tutor]{log_prefix} reply STILL at max_tokens after 2 continuations -- returning stitched partial")
    return reply.strip()


def _last_user_text(msgs) -> str:
    """The student's most recent words, for the referees that need to know what was
    asked (rules 2 and 8). Ignores the SYSTEM nudges the referee itself appends."""
    try:
        for m in reversed(list(msgs or [])):
            if m.get("role") == "user":
                t = str(m.get("content", ""))
                if not t.lstrip().startswith("(SYSTEM:"):
                    return t
    except Exception:  # noqa: BLE001
        pass
    return ""


# -----------------------------------------------------------------------------
# THE MISSING-MARK PROBE (2026-08-14, build gd) -- MEASUREMENT ONLY. It prints a line
# and changes NOTHING about the reply the student sees.
#
# WHY IT EXISTS. [[mark]] is what records "the student finished a problem" -- their
# score, their accuracy, and (since build fy) the signal that folds a finished problem
# away on the board. The prompt calls it "REQUIRED, not optional" in all ten courses,
# and ruletests checks that the PROMPT SAYS SO -- but nothing has ever checked that the
# tutor actually emits one. On 2026-08-14 Jim's Render log showed the difference plainly:
# an Algebra I lesson posted /api/mark three times and behaved perfectly, while a
# Geometry lesson posted it ZERO times even though the student was handed
# "130 + ? = 180", answered fifty, and was told "exactly right".
#
# WHY IT ONLY MEASURES. The obvious next step is a referee that regenerates the reply,
# or a net that awards the mark itself. Both are premature and one is dangerous: a net
# that guesses would inflate a child's recorded accuracy, which is worse than losing a
# point. Retired ensure_board is the standing lesson here -- a net that guesses caused
# more harm than the gap it filled. So this counts the gap first, on real lessons, and
# the decision comes after the number does.
#
# DELIBERATELY NARROW, so a logged line means something: it fires only when the tutor's
# PREVIOUS turn put a pending line on the board (a "?" standing in for the unknown --
# the same signal rule 15 and prose_pending_question_conflict already use), the student
# then said something, and THIS reply writes a settled line while recording neither
# [[mark]] nor [[nice]]. Fails open everywhere.
# -----------------------------------------------------------------------------
def _last_assistant_text(messages) -> str:
    """The tutor's own previous turn, from the ORIGINAL message list (never the
    discarded drafts a referee retry appends)."""
    try:
        for m in reversed(list(messages or [])):
            if m.get("role") == "assistant":
                return str(m.get("content", ""))
    except Exception:  # noqa: BLE001
        pass
    return ""


def _board_attr_strings(text):
    """The attribute text of every board tag in this reply."""
    try:
        return [t[1] for t in re.findall(
            r"\[\[\s*(" + "|".join(_PQ_BOARD_TAGS) + r")\b([^\]]*)\]\]",
            str(text or ""), re.I)]
    except Exception:  # noqa: BLE001
        return []


def missing_mark_probe(reply: str, messages) -> str:
    """Describe a turn that looks like a finished problem carrying no [[mark]] and no
    [[nice]], or "" when there is nothing to report. Never raises."""
    try:
        text = str(reply or "")
        if re.search(r"\[\[\s*(mark|nice)\b", text, re.I):
            return ""                       # something was recorded -- nothing to say
        pending = [a for a in _board_attr_strings(_last_assistant_text(messages)) if "?" in a]
        if not pending:
            return ""                       # no problem was posed, so none was finished
        if not [a for a in _board_attr_strings(text) if "?" not in a]:
            return ""                       # still open -- they have not finished it yet
        if not _last_user_text(messages).strip():
            return ""                       # the student has not answered anything
        return ('the previous turn left a pending line on the board ("%s") and this reply '
                'writes a settled one while recording neither [[mark]] nor [[nice]] -- if '
                'the student just finished that problem, the credit was not recorded'
                % " ".join(pending[-1].split())[:70])
    except Exception:  # noqa: BLE001 -- a probe must never affect a lesson
        return ""


def _create_verified(client, model, system_blocks, messages, log_prefix, meta=None):
    """One model call, refereed. Returns the verified reply with [[verify]] tags
    stripped, or "" if the model returned nothing (caller shows its fallback).
    `meta` ({code, course, mode}) attributes the turn's usage to a student for the
    cost log -- counts only, never text."""
    msgs = list(messages)
    # build ia: what this conversation has actually SAID, for the quiz-term referee
    # (rule 47e). Computed from the ORIGINAL messages, never from the retried msgs
    # list -- a rejected draft plus its nudge would otherwise teach the checker the
    # very vocabulary it is checking for, and the regeneration would escape.
    heard = " ".join(m.get("content", "") for m in (messages or [])
                     if isinstance(m, dict) and isinstance(m.get("content"), str)).lower()
    reply = ""
    tokens = {}
    for attempt in range(1, MATHCHECK_MAX_ATTEMPTS + 1):
        reply = _create_full(client, model, system_blocks, msgs, tokens, log_prefix)
        if not reply:
            # BUILD dg: a student who hears "I lost my train of thought" repeats
            # themselves -- so the code repeats itself FIRST. One silent retry before
            # the apology; the audit counted that apology 6 times in 10 lessons, so
            # this path is common enough to matter.
            print(f"[tutor]{log_prefix} model returned an EMPTY reply -- retrying once")
            reply = _create_full(client, model, system_blocks, msgs, tokens, log_prefix)
        if not reply:
            _log_brain_usage(meta, model, tokens, attempt, "empty")
            return ""
        if mathcheck is None:
            # Verifier missing on this deploy (defensive import failed): skip the
            # check, but STILL strip any [[verify]] tags so they never leak out.
            _log_brain_usage(meta, model, tokens, attempt, "")
            return re.sub(r"\[\[\s*verify\b[^\]]*\]\]", "", reply).strip()
        try:
            verdict, detail = mathcheck.verify_reply(reply)
        except Exception as exc:  # noqa: BLE001 -- referee crash = fail open
            print(f"[mathcheck]{log_prefix} checker crashed (fail open): {exc}")
            _event("referee_crash", "mathcheck", str(exc),
                   (meta or {}).get("code", ""), (meta or {}).get("course", ""))
            verdict, detail = "unverifiable", str(exc)
        if verdict != "wrong":
            if verdict == "unverifiable":
                print(f"[mathcheck]{log_prefix} unverifiable (passed through): {detail}")
            # THE PROSE REFEREE (2026-08-09): the tags are sound -- now check that the
            # SPOKEN words agree with them (see prose_board_conflict above). Same
            # treatment as a failed math check: the student never saw this draft.
            prose_detail = prose_board_conflict(reply, _last_user_text(msgs),
                                                expected_unit=(meta or {}).get("unit"),
                                                allowed_units=(meta or {}).get("allowed_units"),
                                                record=(meta or {}).get("record"),
                                                heard=heard)
            if prose_detail and attempt < MATHCHECK_MAX_ATTEMPTS:
                print(f"[prosecheck]{log_prefix} CONTRADICTION on attempt "
                      f"{attempt}/{MATHCHECK_MAX_ATTEMPTS}: {prose_detail}")
                msgs = msgs + [{"role": "assistant", "content": reply},
                               {"role": "user", "content": _PROSE_NUDGE.format(detail=prose_detail)}]
                continue
            if prose_detail:
                print(f"[prosecheck]{log_prefix} UNRESOLVED -- passing through: {prose_detail}")
                _event("pass_through", "prosecheck", prose_detail,
                       (meta or {}).get("code", ""), (meta or {}).get("course", ""))
            # build gv: MEASUREMENT ONLY -- claims about what has already happened.
            try:
                count_claim_probe(reply, (meta or {}).get("code", ""),
                                  (meta or {}).get("course", ""))
            except Exception:  # noqa: BLE001
                pass
            # build gd: MEASUREMENT ONLY -- see missing_mark_probe above. Never alters
            # the reply, never costs a model call; it just counts a gap we cannot
            # currently see. Runs on the ACCEPTED draft only.
            try:
                _mark_gap = missing_mark_probe(reply, messages)
                if _mark_gap:
                    print(f"[markcheck]{log_prefix} POSSIBLE MISSED MARK: {_mark_gap}")
                    _event("probe", "markcheck", _mark_gap,
                           (meta or {}).get("code", ""), (meta or {}).get("course", ""))
            except Exception as _exc:  # noqa: BLE001 -- a probe must never fail a turn
                print(f"[markcheck]{log_prefix} probe crashed (ignored): {_exc}")
            status = verdict if verdict != "ok" else ("ok" if attempt == 1 else "fixed")
            if prose_detail:
                status = "prose-unresolved"
            _log_brain_usage(meta, model, tokens, attempt, status)
            return mathcheck.strip_verify_tags(reply)
        print(f"[mathcheck]{log_prefix} WRONG on attempt {attempt}/{MATHCHECK_MAX_ATTEMPTS}: {detail}")
        if attempt < MATHCHECK_MAX_ATTEMPTS:
            msgs = msgs + [{"role": "assistant", "content": reply},
                           {"role": "user", "content": _MATHCHECK_NUDGE.format(detail=detail)}]
    # Three drafts in a row judged wrong, WITH the correction in hand, almost always
    # means the CHECKER mis-read an unusual claim -- so pass the last draft through
    # (fail open) rather than brick the lesson, and log loudly for the developer.
    print(f"[mathcheck]{log_prefix} UNRESOLVED after {MATHCHECK_MAX_ATTEMPTS} attempts -- passing through")
    _event("pass_through", "mathcheck", str(detail),
           (meta or {}).get("code", ""), (meta or {}).get("course", ""))
    _log_brain_usage(meta, model, tokens, MATHCHECK_MAX_ATTEMPTS, "unresolved")
    return mathcheck.strip_verify_tags(reply)


def _reply_pipeline(prompt_fn, history, user_message: str, log_tag: str,
                    meta: dict, where: str, label: str,
                    turn_note: str = "", post=None) -> str:
    """THE reply pipeline -- ONE copy (2026-08-17, build hg; full-app review Class B,
    backend half). get_tutor_reply, get_practice_reply and get_topic_reply used to be
    three hand-copied variants of this exact sequence, and they had ALREADY drifted
    twice in ways that mattered: practice/topic shipped for weeks with the fourteenth
    referee silently disarmed (no "unit" in meta -- re-armed in build hb), and only
    the lesson lane ran ensure_today_tag. Every future stage -- a new referee, a new
    net, a new probe -- used to need wiring three times, with ~1/3 odds per lane of
    being missed. Now there is one sequence, and the getters are CONFIGURATIONS.

    prompt_fn  -- zero-arg callable building the system prompt. A CALLABLE on purpose:
                  the prompt must be built INSIDE the try below, so a prompt-builder
                  crash still yields the friendly message (as it always did), never a
                  raw 500 to a child.
    log_tag    -- " [lesson]" / " [practice]" / " [topic]" for the server log lines.
    meta       -- code/course/mode plus the referee's expected "unit" (build gn/hb).
    where      -- the telemetry name for a fail-open ("get_tutor_reply", ...).
    label      -- the log-line prefix ("tutor", "practice", "topic").
    turn_note  -- appended to THIS turn's user message, never the system prompt
                  (build cm: the system prompt is one cached block; a note about this
                  turn belongs beside this turn's message, where nothing is cached).
    post       -- optional finishing net run on the verified reply, INSIDE the try:
                  a net that crashes must degrade to the friendly message too.
    """
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return ("(Setup needed: I can't reach my brain yet. Please add the "
                "ANTHROPIC_API_KEY environment variable in Render, then reload "
                "this page.)")

    model = os.environ.get("CLAUDE_MODEL", DEFAULT_MODEL)

    messages = _trim_history(list(history or []))
    messages.append({"role": "user",
                     "content": (user_message + turn_note) if turn_note else user_message})

    try:
        client = Anthropic(api_key=api_key, timeout=ANTHROPIC_TIMEOUT_S, max_retries=1)
        # MATH VERIFIER (2026-08-03): the reply is generated AND refereed in here --
        # see _create_verified above. Same model, same prompt, same max_tokens.
        reply = _create_verified(
            client, model,
            _cacheable_system(prompt_fn()),
            messages, log_tag, meta=meta,
        ) or "(Sorry, I lost my train of thought. Could you say that again?)"
        return post(reply) if post else reply
    except Exception as exc:  # noqa: BLE001  -- we want a graceful UI message
        # We deliberately never leak a raw stack trace to a student. We log it
        # for the developer and show a calm message instead.
        print(f"[{label}] Claude API error: {exc}")
        _event("failopen", where, str(exc),
               (meta or {}).get("code", ""), (meta or {}).get("course", ""))
        return ("(I'm having trouble thinking right now -- give me a moment and "
                "try again.)")


def get_tutor_reply(student: dict, history: list, user_message: str,
                    course: str = DEFAULT_COURSE, code: str = "",
                    turn_note: str = "") -> str:
    """Ask Claude for the tutor's next reply in a LESSON. One of three thin
    configurations of _reply_pipeline above (build hg) -- the lane-specific facts
    are the prompt, the referee's unit, the turn-note, and the TODAY-bar net.

    PER-TURN NOTES RIDE WITH THE STUDENT'S MESSAGE, NOT THE SYSTEM PROMPT
    (2026-08-10, build cm): the system prompt is ONE cached block; anything appended
    to it re-bills every token from that point on. A note is about THIS turn, so it
    belongs beside this turn's message, where nothing is cached anyway."""
    return _reply_pipeline(
        # build gn: the referee's "unit" is derived exactly as build_system_prompt
        # derives it, from the same two inputs, so referee and prompt cannot disagree.
        lambda: build_system_prompt(student, course),
        history, user_message, " [lesson]",
        meta={"code": code, "course": course, "mode": "lesson",
              "unit": _lesson_unit(student),
              # build hm: the record's allowed [[unitplan]] units, resolved by
              # main._unit_allowed_set from the SAME store facts the prompt was
              # built on. None/absent = the nineteenth referee stays silent.
              "allowed_units": (student or {}).get("allowed_units"),
              # build ho: the compact score/state record (main._claim_record) for
              # the twentieth referee. None/absent = it stays silent.
              "record": (student or {}).get("claim_record")},
        where="get_tutor_reply", label="tutor", turn_note=turn_note,
        # build bo: deterministic TODAY-bar net -- LESSON MODE ONLY (the drift the
        # review found: only this lane ever ran it, now that fact is legible here).
        post=lambda reply: ensure_today_tag(
            ensure_board(reply, user_message, history), history,
            today_live=bool((student or {}).get("today_live"))))


def _subject(course: str) -> str:
    return COURSE_SUBJECT.get(course or DEFAULT_COURSE, "math")


# =============================================================================
# NARRATIVE ASSESSMENTS (2026-08-01) -- "How am I doing?" in a human voice
# =============================================================================


def get_assessment(facts: str, audience: str = "student", code: str = "",
                   course: str = "") -> str:
    """One honest narrative paragraph from real progress facts. `audience` is
    'student' or 'parent'. Returns friendly error text on config/API problems.
    `code`/`course` (2026-08-04) attribute the call's usage to the cost log."""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return ("(Setup needed: the assessment writer can't reach its brain yet -- "
                "the ANTHROPIC_API_KEY environment variable is missing.)")
    model = os.environ.get("CLAUDE_MODEL", DEFAULT_MODEL)
    system = ASSESSMENT_SYSTEM_PARENT if audience == "parent" else ASSESSMENT_SYSTEM_STUDENT
    try:
        client = Anthropic(api_key=api_key, timeout=ANTHROPIC_TIMEOUT_S, max_retries=1)
        response = client.messages.create(
            model=model, max_tokens=400,
            system=_cacheable_system(system),
            messages=[{"role": "user", "content": facts}],
        )
        parts = [b.text for b in response.content if getattr(b, "type", None) == "text"]
        tokens = {}
        _add_usage(tokens, response)
        _log_brain_usage({"code": code, "course": course, "mode": "assessment"},
                         model, tokens, 1, "")
        return "".join(parts).strip() or "(I couldn't put the words together just now -- try again in a moment.)"
    except Exception as exc:  # noqa: BLE001
        print(f"[assessment] Claude API error: {exc}")
        return "(I couldn't write the assessment just now -- give it a moment and tap again.)"


def build_practice_prompt(student: dict, problem: str, course: str = DEFAULT_COURSE) -> str:
    """Fill the practice template with this student's name and their problem, for a course."""
    name = (student or {}).get("name", "the student")
    problem = (problem or "").strip() or "(The student hasn't stated the problem clearly yet -- ask them what it is.)"
    _u = _unit_from_text(problem, course)          # build gb: also filters the scripts
    # build gf: never leave the filter off -- fall back to their placed unit, then to 1.
    _fu = _u or _unit_from_progress((student or {}).get("progress") or "") or _FILTER_UNIT_FALLBACK
    playbook = _playbook(_u, course)
    return GROUND_RULES + GRAPH_TOOL_NOTE + PRACTICE_SYSTEM_PROMPT_TEMPLATE.format(
        tutor_name=TUTOR_NAME,
        student_name=name,
        problem=problem,
        playbook=playbook,
        subject=_subject(course),
        scope_block=PRACTICE_SCOPE.get(course or DEFAULT_COURSE, PRACTICE_SCOPE[DEFAULT_COURSE]),
    ) + _notation_block(course) + _misconception_block(course) + _foundation_block(course, (student or {}).get("foundations_heard"),
                      (student or {}).get("foundations_verbatim", True), _fu)


def get_practice_reply(student: dict, problem: str, history: list, user_message: str,
                       course: str = DEFAULT_COURSE, code: str = "") -> str:
    """Ask Claude for the coach's next reply in a PRACTICE session. A thin
    configuration of _reply_pipeline (build hg). Practice history is held by the
    browser and passed in each request -- a homework problem is a one-off.

    build hb: the fourteenth referee is armed with the unit of the PROBLEM -- the
    same value build_practice_prompt uses for the playbook, so referee and prompt
    cannot disagree (the gn property). None for an unclassifiable problem, and the
    referee then stays silent rather than guessing. NEVER the placed unit: a side
    trip may come from any unit, and the placed unit would fire on correct teaching."""
    return _reply_pipeline(
        lambda: build_practice_prompt(student, problem, course),
        history, user_message, " [practice]",
        meta={"code": code, "course": course, "mode": "practice",
              "unit": _unit_from_text(problem, course)},
        where="get_practice_reply", label="practice",
        post=lambda reply: ensure_board(reply, user_message, history))


def build_topic_prompt(student: dict, topic: str, course: str = DEFAULT_COURSE) -> str:
    """Fill the topic template with this student's name and their chosen topic, for a course."""
    name = (student or {}).get("name", "the student")
    topic = (topic or "").strip() or "(The student hasn't named a topic yet -- ask them what they'd like to explore.)"
    _u = _unit_from_text(topic, course)            # build gb: also filters the scripts
    # build gf: never leave the filter off -- fall back to their placed unit, then to 1.
    _fu = _u or _unit_from_progress((student or {}).get("progress") or "") or _FILTER_UNIT_FALLBACK
    playbook = _playbook(_u, course)
    return GROUND_RULES + GRAPH_TOOL_NOTE + TOPIC_SYSTEM_PROMPT_TEMPLATE.format(
        tutor_name=TUTOR_NAME,
        student_name=name,
        topic=topic,
        playbook=playbook,
        subject=_subject(course),
        scope_block=TOPIC_SCOPE.get(course or DEFAULT_COURSE, TOPIC_SCOPE[DEFAULT_COURSE]),
    ) + _notation_block(course) + _misconception_block(course) + _foundation_block(course, (student or {}).get("foundations_heard"),
                      (student or {}).get("foundations_verbatim", True), _fu)


def get_topic_reply(student: dict, topic: str, history: list, user_message: str,
                    course: str = DEFAULT_COURSE, code: str = "") -> str:
    """Ask Claude for the guide's next reply in a TOPIC exploration. A thin
    configuration of _reply_pipeline (build hg).

    build hb: the fourteenth referee is armed with the unit of the TOPIC the student
    chose -- the same value build_topic_prompt uses for the playbook. None when the
    topic cannot be classified; the referee then stays silent rather than guessing."""
    return _reply_pipeline(
        lambda: build_topic_prompt(student, topic, course),
        history, user_message, " [topic]",
        meta={"code": code, "course": course, "mode": "topic",
              "unit": _unit_from_text(topic, course)},
        where="get_topic_reply", label="topic",
        post=lambda reply: ensure_board(reply, user_message, history))


# I did no harm and this file is not truncated.

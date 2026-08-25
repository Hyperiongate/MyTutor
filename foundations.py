# =============================================================================
# foundations.py  --  CANONICAL FOUNDATION SCRIPTS  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-08-25  BUILD nj -- THE DOMAIN SCRIPT READS ITS RULE. The new func-rule
#               referee's canonical sweep caught algebra1/domain writing f(x)=1/x
#               and never reading it -- a real rule-44 gap in authored content, the
#               same class the night watch flagged live. One sentence added to the
#               say ("The rule on the board reads: f of x equals one over x...").
#               ⚠️ ONE CLIP RE-RENDERS on the next course-audio pass (pennies).
#   2026-08-20  BUILD jn -- THE TAUTOLOGY A CHILD ACTUALLY READ. Jim, from one live
#               precalc lesson: the screen said "We write f of x, which is read as f of
#               x." Both halves of a sentence whose whole job is to separate the SYMBOL
#               from its READING were the reading. It was not the model -- this script,
#               spoken verbatim, said it. (Checked first: nothing between the model and
#               the bubble rewrites prose. styleVars() styles letters and keeps
#               parentheses; notation.py is a registry, not a transformer.)
#               ⚠️ WRITING "f(x)" WOULD NOT HAVE FIXED IT. speech-text.js forSpeech()
#               turns f(x) into "f of x" before the TTS engine sees it -- correctly, for
#               the ear -- so the naive fix reads right on screen and is STILL a
#               tautology out loud, in a voice-first product. The wording now names the
#               notation in words that survive that transform, exactly as the
#               "function notation" script one entry below already did: "the letter f
#               and the input tucked inside parentheses... you say the whole thing out
#               loud as f of x". The board still shows the real f(x) (the [[machine]]
#               tag's fname), so the symbol is seen and the words say how to say it --
#               rules 14 and 48 both satisfied, by the two channels doing their own job.
#               ruletests PART 3cq now scans every authored script for the shape, AS
#               HEARD, so neither the defect nor the naive fix can come back.
#   2026-08-14  BUILD gi -- THE TERM-GAP PROBE (measurement only, no behaviour change).
#               Jim's question after the "right angle" lesson: can it learn from a student
#               having to ask? The weights cannot; the system can, and this collects the
#               evidence. term_gap() reports when a student asks what a word MEANS and the
#               tutor had just used that word, split the way Jim split it: "unintroduced"
#               (we have a script and it was not delivered -- a rule violation, fixable
#               automatically one day) and "no-script" (nobody wrote one -- new teaching
#               content, real money, so a human decides). Logs the TERM and the course
#               only, never the student's words. The build fz/gc audit could only find gaps
#               derivable from the code; this finds the ones nobody predicted.
#   2026-08-14  BUILD gf -- A HEARD SCRIPT IS NEVER UNIT-FILTERED. The first full ruletests
#               run against build gb caught it: rule 40 OFFERS a term the student has met
#               before and restores its exact wording the moment they accept -- and
#               "remind me what a radius is" can arrive in any unit. gb filtered those out
#               with everything else, so the tutor could neither name the offer nor honour
#               it, and would have paraphrased: drifted words and a re-billed voice clip.
#               Heard scripts now always travel; only never-met terms are deferred.
#   2026-08-14  BUILD ge -- THE "point" BOARD LINE NOW DRAWS POINTS. Jim, live in Geometry
#               unit 1: the tutor said "take a look at those three points on the board" and
#               the board showed the TEXT "A B C" -- and styleVars coloured B and C red as if
#               they were algebra variables, so there were no points to look at. That is
#               exactly the words-vs-board mismatch this whole thread started from, and build
#               fz introduced it. The board now uses [[objects]] to draw three real filled
#               dots with the letters in the caption. Only the board line changed; the `say`
#               string is untouched, so its cached audio is NOT re-billed.
#   2026-08-14  BUILD gc -- 95 NEW FOUNDATION SCRIPTS ACROSS THE OTHER NINE COURSES.
#               Completes the red list that build fz started on geometry: every term the
#               tutor already SAYS OUT LOUD inside these scripts with nothing anywhere
#               defining it. Counts: entry 12, basic 4, prealgebra 9, algebra1 11,
#               algebra2 17, precalc 16, probstat 12, calculus 6, diffeq 8.
#               This only fits because build gb filters the block to the lesson's unit.
#               Every script was machine-checked before landing: 40-90 spoken words, the
#               term bolded exactly once, no symbols in the spoken text, no duplicate of
#               an existing term, and every board figure RENDERED through the real
#               math-figures.js / geo-figures.js to confirm it draws something. Two tag
#               shapes that do not render were caught and corrected in the process:
#               [[graph expr=]] (the grapher reads func=/lines=) and [[vector x= y=]]
#               (it reads v=), both already recorded as fixed bugs elsewhere in this file.
#               APPEND ONLY -- no existing say-string was touched, so no cached audio is
#               re-billed. AUDIO: these 95 render once on the /admin foundation pre-render.
#   2026-08-14  BUILD gb -- THE PROMPT NOW CARRIES ONLY THE UNIT BEING TAUGHT.
#               prompt_block() gains unit=. Scripts belonging to other units are NAMED
#               but their wording is left out, which is what makes room for the ~120
#               foundation terms still owed across the other nine courses. Build fz left
#               428 characters under the 180,000 ceiling; this returns the prompt to
#               well below where it started. NOT the deferral build cn reversed: heard-
#               ness flips mid-session and rebuilt the cache, the unit does not change
#               for the whole of a lesson, so the prompt stays byte-identical turn to
#               turn. cn's own note says this mechanism "becomes the right answer if the
#               library ever grows to where it does not fit" -- it has. Fails open: no
#               curriculum module, an unplaceable term, or any exception, and the script
#               travels in full exactly as before. unit=None (the default) filters
#               nothing, so every existing caller is unchanged.
#   2026-08-14  BUILD fz -- 25 NEW GEOMETRY SCRIPTS (red-list coverage audit, batch 1 of 10).
#               An audit compared the terms this file promises to introduce against the
#               vocabulary curriculum.py already classifies lessons by. Geometry had 25 terms
#               the tutor SAYS OUT LOUD inside these very scripts with nothing anywhere
#               defining them. Jim found it live: the tutor used "right angle" without ever
#               saying it means ninety degrees, and he had to stop and ask. Worse,
#               "supplementary" had a script and "complementary" did not -- and one lesson
#               teaches the pair in a single breath.
#               ADDED: point, line, segment, right angle, degree, complementary, circle,
#               diameter, chord, circumference, parallel, perpendicular, negative reciprocal,
#               midpoint, translation, reflection, rotation, rigid motion, area, surface area,
#               prism, cylinder, cone, pyramid, two-column proof.
#               APPEND ONLY -- not one existing say-string was touched, so no cached audio is
#               re-billed. Board lines reuse only tag forms already validated in this file.
#               WHY THE LIST WAS SHORT: the original lists were authored from memory in one
#               build (2026-08-09) and no selection rule was ever written down; nothing has
#               ever cross-checked them against curriculum.py. Nine courses still to do.
#               AUDIO: these 25 render once on the foundation pre-render in /admin.
#   2026-08-13  BUILD fe -- THE FRACTION SCRIPT LOSES ITS FALSE "ALWAYS" (rule 61; the
#               2026-08-13 lesson audit, fractions-lost, basic). The canonical basic
#               "fraction" script said "a fraction ALWAYS means we cut something into
#               fair, matching pieces" -- false as stated: fractions also name division,
#               ratios, and numbers past one like 5/4. Same reasoning as the el-era
#               function-notation fix: the say-string rule is "never edit casually",
#               and a false sentence spoken verbatim to every young student is the
#               least casual reason there is. New form carries its condition in the
#               child's own register: "So the way we use fractions today: ...". ⚠️
#               AUDIO: this script's cached clip is orphaned by the edit and re-renders
#               once -- the foundation pre-render on /admin (already owed since el)
#               pays it once, up front. ruletests PART 3w now bans the false form from
#               all authored content, alongside the five from 2026-08-12.
#   2026-08-12  BUILD em -- FIVE PIE BOARD LINES CORRECTED (the fraction pictures). The
#               2026-08-12 audit: a board captioned "one whole, cut into four equal
#               parts" drew TWO wedges, and the lesson then asked a beginner "how many
#               pieces are shaded?" over ONE shaded wedge -- the student answered "3"
#               and cannot have counted it. The cause was HERE, in these canonical
#               board lines: data="this piece:1, the rest:3" tells the renderer to draw
#               one 25% sector and one 75% sector, and it prints "the rest 75%" beside
#               a picture teaching one fourth. All five fraction/probability pies now
#               use the new EQUAL-PARTS form -- [[pie parts="4" shaded="3"]] -- which
#               draws four separated countable wedges and prints NO answer on the board
#               (rule 6). Captions rewritten to say what to NOTICE (rule 41) without
#               giving the count away. `say` strings untouched: no audio is re-billed.
#   2026-08-12  BUILD el -- ONE SAY-STRING CORRECTED, DELIBERATELY (function notation,
#               algebra1). The 2026-08-12 lesson audit caught the tutor teaching "when
#               you see a letter with something tucked inside parentheses right after
#               it, that's function notation" -- and it was not a live slip, it was
#               THIS SCRIPT, spoken verbatim. The sentence is false: x(y+1) is
#               multiplication, and the tutor contradicts itself two board lines later
#               by writing f(3) = 2(3) + 1. Corrected to name the real discriminator --
#               whether the letter in front is the NAME of a rule -- which is the
#               teaching a student actually needs, and which now says out loud that
#               parentheses DO mean multiplying elsewhere. The say-string rule is
#               "never edit casually"; a false sentence spoken verbatim to every
#               algebra student is the least casual reason there is. ⚠️ AUDIO: this
#               script's cached clip is discarded and re-renders once per student --
#               run the foundation pre-render on /admin after deploying to pay it once,
#               up front. New rule 61 (prompts.py) covers the general failure mode, and
#               ruletests PART 3w fails the build if this false form -- or any of the
#               other four the audit caught -- ever returns to authored content.
#   2026-08-10  BUILD de -- FOUR NEW diffeq scripts for the CUPM restructure (library
#               182 -> 186): "slope field" (now taught in unit 1), "equilibrium" (new
#               unit 3, qualitative analysis), "Euler's method" (new unit 4, numerical
#               methods), "eigenvalue" (unit 8, linear systems). APPENDED at the end of
#               the diffeq list -- no existing "say" string was touched, per the
#               append-only rule (each edit to a heard string re-bills its audio and
#               orphans the cached clip). Each follows the house shape: what it is, a
#               concrete picture, "Here is the trap." All 25-130 words, term wrapped in
#               **bold**, boards are [[write]]/[[card]] with no square brackets inside
#               attribute values.
#   2026-08-10  BUILD cv -- NEW calculus script "removable discontinuity" (library 181 ->
#               182), inserted after "limit" so it reads in teaching order. Jim read a
#               live limits lesson and could not tell where the hole at x = 2 came from --
#               correctly, because nothing told him. This script builds it from
#               f(x) = (x^2-4)/(x-2): the factor cancels, the original divided by zero at
#               x = 2, so that one input has no output. Board shows the algebra and then
#               the line with the point removed, framed range="-1..5" (see the parseRange
#               fix in math-figures.js -- the comma form this was first written with was
#               being thrown away). ~800 characters of new audio, about 20 cents, once.
#               No existing "say" string was touched.
#   2026-08-10  BUILD cl -- DEFERRED WORDING FOR SCRIPTS ALREADY GIVEN. Jim asked us to
#               address the prompt ceiling, and the first thing to say is that splitting
#               FILES does not touch it: a prompt carries ONE course template, so
#               duplication across the ten templates costs disk, not prompt. Measured
#               2026-08-10: the templates and the shared rules overlap by 0%, so there
#               is no duplication anywhere to reclaim. Every reduction from here removes
#               or defers real content -- which is why this is the only one taken.
#               It is safe because rule 40 already changed the job of a heard script: it
#               is OFFERED, not replayed. Its exact wording is therefore dead weight in
#               every prompt except the one where the student says yes. prompt_block()
#               gained verbatim=, defaulting to TRUE, and main.py turns it off only for
#               the ordinary turns of a returning student. Heard terms are still NAMED,
#               so he can always make the offer; only the words wait.
#               wants_refresher() decides. It reads the student's own words ("remind me",
#               "I forgot") AND, because rule 40(b) makes him ASK, a bare "yes" -- but a
#               bare yes only counts when his previous turn actually offered a refresher.
#               It FAILS OPEN: any doubt, any exception, and the words are carried. A
#               missing script would make him paraphrase, which costs a cached render and
#               drifts wording that every student is supposed to share.
#               Saves 6,000-8,000 chars on an ordinary returning-student turn, and grows
#               as a student learns more -- which is exactly when the misconception and
#               notation blocks matter most.
#   2026-08-09  BUILD cj -- THREE SUBSCRIPT SCRIPTS (algebra2, calculus, diffeq).
#               Found by the new notation registry, not by a person: those three courses
#               write a₁, xᵢ and y₁ on the board and NO script anywhere ever said the
#               word "sub". A student reading "x sub i" as "x times i" is not making a
#               careless error, they are reading it the only way anyone ever showed them.
#               Library 178 -> 181. No existing `say` touched.
#   2026-08-09  BUILD ci -- FUNCTION NOTATION IS NOW TAUGHT. Jim, logged in as a demo
#               student in Algebra I: "it's never been clearly stated to me what f of x
#               is, how to say f of x... and then it flipped over to g of x. I'm not sure
#               if it's because I've already used this student for a while, or if the
#               teaching hasn't taken hold."
#               It was neither. THE TEACHING WAS NEVER WRITTEN. Algebra I's "function"
#               script defines the concept beautifully -- a rule with exactly one output,
#               the vending machine -- and never once mentions the notation. The very
#               NEXT script, "domain", puts f(x) = 1/x on the board. So the first time a
#               student ever saw f(x), nothing had told them it exists, how to say it, or
#               that it is not multiplication. Algebra II was the same. Pre-Calculus said
#               it, but circularly. Calculus writes f( ) in NINE scripts and never reads
#               one aloud. Differential Equations writes y prime, y double prime, dy/dx
#               and y(0) constantly and never reads any of them.
#               FIVE new scripts, one per affected course (algebra1, algebra2, precalc,
#               calculus, diffeq), each: shows the written form on the board, says the
#               words a person actually says, denies the wrong reading BY NAME ("it is
#               not f times x"), and explains that the letter is only a NAME -- which is
#               the half that lost Jim when it "flipped over to g of x".
#               NOT ONE existing `say` was touched (173 verified byte-identical), so no
#               cached audio was discarded. New audio: 2,638 characters, about 63 cents,
#               once, ever. Scripts were INSERTED in teaching order rather than appended
#               -- reordering the list is free, since the cache is keyed by text.
#               ruletests.py PART 3b now fails any course that writes function notation
#               on the board without a script that reads it aloud and denies the wrong
#               reading. It found the diffeq gap on its first run.
#   2026-08-09  BUILD cf -- CAPTIONS (rule 41). Ten figures had no caption= and now do,
#               each naming what to NOTICE rather than what is drawn ("count them one at
#               a time — the last number you say is how many", not "three stars").
#               ruletests.py PART 3c fails any figure that ships without one. No `say`
#               string was touched, so no cached audio was discarded.
#   2026-08-09  BUILD ce -- THE RETURNING STUDENT IS ASKED, NOT REPLAYED.
#               prompt_block(course, heard) now takes the list of terms THIS student was
#               introduced to on an earlier visit (main.py reads it from the store) and
#               marks them "ask first, rule 40" instead of letting the tutor play the
#               script at them again. The SCRIPTS THEMSELVES ARE UNCHANGED and must stay
#               that way: identical wording is what lets a refresher reuse the cached
#               audio, so asking again costs nothing.
#               NEW: normalize_term(), known_term() and learned_terms_in() -- the parser
#               and validator for the [[learned term="..."]] tag rule 40(f) asks the tutor
#               to emit. A tag naming a script this course does not have is DROPPED: the
#               only thing a bad memory row can do is cost a student an introduction they
#               still need, so an unrecognised name is never worth trusting.
#   2026-08-09  BUILD cd -- THE LIBRARY IS NOW COMPLETE. 24 scripts -> 173. Every course
#               carries 17 or 18 canonical introductions instead of 2, chosen to cover
#               all nine units of that course and weighted toward the words students
#               actually trip on (denominator, regrouping, unit rate, extraneous
#               solution, reference angle, skew, integrating factor, and so on).
#               Jim asked for exactly this: "I want you to expand that library of saved
#               script... I don't wanna spend a thousand dollars on it, but I'd spend a
#               hundred dollars on it to make it complete." The whole library is 82,856
#               characters of speech -- ONE-TIME ElevenLabs cost of roughly $12-$25 at
#               current per-character rates, then free for every student forever.
#               NOT ONE existing `say` string was touched. That is deliberate and it is
#               the rule for this file: editing a `say` throws away its cached audio and
#               makes the next student pay to re-render it. New entries are APPENDED.
#
#               BOARD TAGS: every board line in this file is now verified against the
#               real renderers by ruletests.py PART 3c, and 11 lines that had already
#               shipped were WRONG in a way nothing could report -- the tutor spoke about
#               a picture that was blank or misleading. Fixed here:
#                 [[graph expr="..."]]        -> func=   (expr= is not read: empty axes)
#                 [[numberline from/to/mark]] -> min=/max=/points=
#                 [[triangle a/b/c]]          -> v=/sides=/right=/angles=/ticks=
#                 [[righttriangle a/b/c]]     -> adj=/opp=/hyp=/theta=
#                 [[vector x="4" y="3"]]      -> v="4,3"
#                 [[scatter points="1,2 ..."]]-> points="(1,2) (2,3.5) ..."
#                 lines="y=x^2"               -> func="x^2"  (lines= draws a STRAIGHT line)
#                 lines="y=a, y=b"            -> lines="y=a ; y=b"  (comma is not a separator)
#                 [[write text="... [x] ..."]]-> no square brackets; handleTags' regex
#                                                 ends the tag at the first "]"
#               All 57 figures were then re-rendered through math-figures.js and
#               geo-figures.js and confirmed to produce real, non-empty drawings.
#
#   2026-08-09  NEW FILE (build cc, Jim). Two problems, one answer.
#               PROBLEM 1 — no foundation. Going through the lessons Jim found that a
#               student meets fractions without ever being told what a fraction IS, or
#               what a numerator or a denominator is. We had described the classroom as
#               "Socratic"; asking a student to reason toward something nobody taught
#               them is not teaching. Rules 36-38 in tutor.py now require foundation
#               first -- this file is what he actually SAYS.
#               PROBLEM 2 — cost. Jim: "you might be trying to save money… I'm okay with
#               [more talking] because once we teach fractions we can save that
#               conversation. We don't have to go back to ElevenLabs." He is exactly
#               right, and the mechanism already exists: main.py's TTS cache is keyed by
#               the TEXT of the line (_tts_cache_path(text)), so an identical sentence is
#               rendered ONCE, ever, for every student on the platform. What defeated it
#               was the model re-wording the same explanation each time.
#               So these scripts are CANONICAL and spoken VERBATIM. The first student
#               ever to meet fractions pays for that audio; every student after them
#               gets it free, instantly, and hears exactly the same well-written
#               explanation. Foundation and cost are the same fix.
# -----------------------------------------------------------------------------
# HOW TO ADD ONE
#   Append to the course's list below. Keep each `say` to roughly 40-90 words of plain
#   spoken English (no symbols -- it is read aloud; see tutor.py "HOW YOU SPEAK"), mark
#   the key term with **double asterisks**, and give `board` lines that the whiteboard
#   can draw. Never edit an existing `say` casually: changing one word discards its
#   cached audio and every student re-renders it once.
#
# WHAT IT IS NOT
#   Not a script for the whole lesson -- only the INTRODUCTION of a concept. Everything
#   after it (the worked example, the practice, the questions) is taught live and adapts
#   to the student, exactly as before.
# =============================================================================

# course id -> list of concept scripts, in the order the course meets them.
#   term   : the key term being introduced (used to spot when it is due)
#   say    : the EXACT words he speaks -- verbatim, so the audio caches
#   board  : lines/tags for the whiteboard while he says it
FOUNDATIONS = {
    "entry": [
        {"term": "number", "say":
            "Before we count anything, here is what a **number** really is: it is a way of saying how "
            "many. When I say three, I am telling you how many things there are, not which ones or how "
            "big they are. Counting is just saying the numbers in order while you touch each thing "
            "exactly once, and the very last number you say is how many you have altogether.",
         "board": ['[[objects emoji="⭐" groups="3" caption="count them one at a time — the last number you say is how many"]]']},
        {"term": "adding", "say":
            "**Adding** means putting groups together and finding out how many there are now. You start "
            "with what you have, then you count on for each new one. Two cookies, and then one more "
            "cookie, is three cookies altogether. Nothing disappears when we add — the pile only gets "
            "bigger.",
         "board": ['[[objects emoji="🍪" groups="2" add="1" caption="the group you had, then the one you added — now count them all"]]']},
        {"term": "skip-counting", "say":
            "**Skip-counting** means counting in jumps instead of one at a time. When you count by twos "
            "you say two, four, six, eight. You are still counting the same things. You are just landing "
            "on every second one. Counting by fives and by tens works the same way. Skip-counting is "
            "fast, and each jump is a whole little group, so it is the first step toward multiplying "
            "later on.",
         "board": ['[[numberline min="0" max="20" points="2,4,6,8,10" caption="counting by twos — landing on every second number"]]',
                   '[[write text="by 2s:  2,  4,  6,  8,  10 ..."]]']},
        {"term": "comparing", "say":
            "**Comparing** two numbers means asking which one is more. Here is the trick that always "
            "works. On the number line, the number that comes later is the bigger one. Eight comes after "
            "five, so eight is more than five. It does not matter how the number looks or how long it "
            "takes to say. Later on the line means more. Earlier on the line means less.",
         "board": ['[[numberline min="0" max="10" points="5,8" caption="8 comes later on the line than 5, so 8 is more"]]']},
        {"term": "make a ten", "say":
            "When you add, you can **make a ten** first, because tens are easy to think about. Say you "
            "have eight and you want to add five. Take two from the five and give it to the eight. Now "
            "you have ten, with three left over. Ten and three is thirteen. You did not change how many "
            "there are. You only moved some over to build a friendly number.",
         "board": ['[[write text="8 + 5   →   10 + 3   =   13"]]']},
        {"term": "subtracting", "say":
            "**Subtracting** means taking some away and finding out how many are left. You start with "
            "what you have, then you take some off the pile. Five cookies, take away two cookies, leaves "
            "three cookies. Subtracting is the opposite of adding. Adding makes the pile bigger. "
            "Subtracting makes it smaller. So the number you start with is always the biggest number in "
            "the story.",
         "board": ['[[objects emoji="🍪" groups="5" caption="start with all of them, then take some away"]]']},
        {"term": "fact family", "say":
            "A **fact family** is a little group of numbers that live together. Two, three and five are a "
            "family. Two and three make five. Three and two make five. Five take away three leaves two. "
            "Five take away two leaves three. Same three numbers, four different facts. Once you know one "
            "of them, you already know the other three. That is why families are faster than learning "
            "facts one at a time.",
         "board": ['[[write text="2,  3,  5   →   2+3=5    3+2=5    5−3=2    5−2=3"]]']},
        {"term": "place value", "say":
            "**Place value** means a digit tells you something different depending on where it sits. Look "
            "at the number twenty-three. The three is three ones. The two is not two. It is two tens, "
            "which is twenty. Same little digits, different jobs, all because of their spot. That is why "
            "we line numbers up so carefully. Ones go under ones, and tens go under tens.",
         "board": ['[[write text="23   =   2 tens  +  3 ones"]]']},
        {"term": "expanded form", "say":
            "**Expanded form** means writing a number stretched out, so you can see what every part is "
            "worth. Take three hundred forty-five. That is three hundreds, four tens, and five ones. "
            "Stretched out, it is three hundred, and forty, and five. It is the very same number. We only "
            "pulled it apart. We do this so you can look inside a number instead of just reading it out "
            "loud.",
         "board": ['[[write text="345   =   300  +  40  +  5"]]']},
        {"term": "regrouping", "say":
            "**Regrouping** is what we do when a column gets too full. Each spot can only hold the digits "
            "zero through nine. So when the ones add up past nine, you trade ten ones for one ten and "
            "slide that ten over to the next column. Some people call it carrying. Nothing is lost when "
            "you do it. Ten pennies becomes one dime, and it is still exactly the same amount of money.",
         "board": ['[[write text="27 + 5:   12 ones   →   1 ten + 2 ones"]]']},
        {"term": "borrowing", "say":
            "**Borrowing** is regrouping going the other way. Sometimes the top number in a column is too "
            "small to take from, like when you need seven and you only have three. So you go next door to "
            "the tens, take one ten, and break it into ten ones. Now that three becomes thirteen, and you "
            "can subtract. You did not make the number bigger. You only changed one ten into ten ones.",
         "board": ['[[write text="43 − 7:   4 tens 3 ones   →   3 tens 13 ones"]]']},
        {"term": "cents", "say":
            "One dollar is made of one hundred **cents**. That one fact is the whole idea of money math. "
            "A penny is one cent. A nickel is five cents. A dime is ten cents. A quarter is twenty-five "
            "cents. Here is the part that surprises people. A dime is smaller than a nickel, but it is "
            "worth more. The size of a coin does not tell you what it is worth. Only its name does.",
         "board": ['[[card title="What each coin is worth" items="penny 1¢ | nickel 5¢ | dime 10¢ | quarter 25¢"]]']},
        {"term": "making change", "say":
            "**Making change** is what happens when you pay more than something costs. The store hands "
            "you back the extra. If a toy costs seven dollars and you give ten dollars, your change is "
            "three dollars, because seven and three make ten. So change is really a missing part. You do "
            "not start over and you do not take away. You count up from the price to the money you handed "
            "over.",
         "board": ['[[write text="cost 7  →  count up to 10  →  change 3"]]']},
        {"term": "minute", "say":
            "A clock has two hands and they do different jobs. The short hand tells you the hour. The "
            "long hand counts the minutes, and one **minute** is one small tick. Sixty minutes make one "
            "hour. Now here is the part that catches almost everybody. The big numbers on the clock face "
            "are five minutes apart. So when the long hand points at the three, that means fifteen "
            "minutes past, not three minutes past.",
         "board": ['[[write text="long hand on 3   =   15 minutes past"]]']},
        {"term": "length", "say":
            "**Length** is how long something is, from one end to the other end. We measure it with a "
            "ruler. Here is the part people get wrong. You line the object up with the zero mark, not "
            "with the edge of the ruler and not with the one. Then you read the number at the other end. "
            "Inches and centimetres both measure length. Either one is fine. You just have to say which "
            "one you used.",
         "board": ['[[write text="start at 0, read the number at the far end"]]']},
        {"term": "pattern", "say":
            "A **pattern** is something that repeats in the same order, over and over. Red, blue, red, "
            "blue, red, blue. That is a pattern, and you can already tell me what comes next. The trick "
            "is to find the part that repeats, and then say that part again. Patterns are not only "
            "colors. They can be shapes, or claps, or numbers like two, four, six, eight.",
         "board": ['[[write text="red, blue, red, blue, red, ___"]]']},
        {"term": "array", "say":
            "An **array** is objects lined up in equal rows. Three rows with four stars in each row is an "
            "array. Every row has to hold the same amount. If one row is short, it is not an array. "
            "Arrays are handy because you do not have to count every single thing. You count one row, "
            "then you skip-count. Three rows of four goes four, eight, twelve. That is where multiplying "
            "begins.",
         "board": ['[[write text="⭐⭐⭐⭐   ⭐⭐⭐⭐   ⭐⭐⭐⭐   =   3 rows of 4  =  12"]]']},
        # --- build gc (2026-08-14): red-list additions for this course. See the
        # change note at the top of this file. Appended, never edited.
        {"term": "clock", "say":
            "A **clock** is a machine that shows you what time it is. Most have a round face with the numbers "
            "one to twelve around the edge, and two hands that turn. The short hand points at the hour. The "
            "long hand counts the minutes. Both hands always travel the same way around the face, past one, "
            "then two, then three, and they never go backwards. Some show the time with digits instead of "
            "hands, and the two kinds mean exactly the same thing.",
         "board": ['[[card title="The two hands" items="short hand goes to the hour | long hand counts the minutes | both turn the same way"]]']},
        {"term": "dime", "say":
            "A **dime** is the small silver coin with the ridged edge, and it is worth ten cents. Ten pennies "
            "are worth the same as one of them. Here is the part that fools almost everybody. It is smaller "
            "than a nickel, but it is worth twice as much. The size of a coin never tells you its value. Only "
            "which coin it is tells you that.",
         "board": ['[[card title="Ten cents" items="dime = 10¢ | ten pennies = 10¢ | the dime is the smaller coin"]]']},
        {"term": "dollars", "say":
            "Money comes in coins and in paper bills, and bills are counted in **dollars**. One dollar is worth "
            "one hundred cents, which is the same as ten dimes or four quarters. A five dollar bill is worth "
            "the same as five one dollar bills. When we write an amount down, the dollar sign goes in front, "
            "then the whole bills, then a dot, then the cents left over.",
         "board": ['[[write text="$1  =  100¢  =  10 dimes  =  4 quarters"]]', '[[write text="$2.50   is   2 whole dollars and 50 cents"]]']},
        {"term": "hour", "say":
            "An **hour** is a chunk of time that lasts sixty minutes. It is about as long as a school lesson or "
            "a long cartoon. On a clock face, the short hand tells you which one you are in right now, and the "
            "long hand has to travel all the way around the face once to finish it. A whole day holds twenty "
            "four of them.",
         "board": ['[[write text="1 hour = 60 minutes     the long hand goes all the way around once"]]']},
        {"term": "hundreds", "say":
            "Numbers have places, and each place is worth ten times the one to its right. First ones, then "
            "tens, then **hundreds**. One hundred is ten tens bundled together. Look at the number three "
            "hundred forty two. That three is not worth three. It sits in the third spot from the right, so it "
            "means three hundred. Same little digit, much bigger job, only because of where it sits.",
         "board": ['[[write text="342   =   3 hundreds  +  4 tens  +  2 ones"]]']},
        {"term": "inch", "say":
            "An **inch** is a unit we use for measuring short lengths. It is about as long as the top part of "
            "your thumb, from the tip to the first crease. Twelve of them make one foot. On a ruler, the "
            "longest lines are the whole ones and the little lines in between cut each one into smaller pieces. "
            "To measure, line the object up with the zero mark, then read the number at the far end.",
         "board": ['[[write text="12 inches = 1 foot      start at 0, not at the edge"]]']},
        {"term": "money", "say":
            "**Money** is what we trade for the things we need and want. It comes in two kinds. Coins are "
            "metal, and bills are paper. Every coin and every bill has an amount it is worth, and that amount "
            "never changes. A worn out penny buys exactly as much as a shiny new one. Counting it up is just "
            "adding those amounts together, and it is easiest to start with the biggest.",
         "board": ['[[card title="Two kinds of money" items="coins: penny, nickel, dime, quarter | bills: 1, 5, 10, 20 dollars | the amount is what it is worth"]]']},
        {"term": "nickel", "say":
            "A **nickel** is the thick silver coin with the smooth edge, and it is worth five cents. Five "
            "pennies are worth the same as one of them, so every time you see one you can count five. That "
            "makes counting quick. Five, ten, fifteen, twenty. Watch out for one thing though. It is bigger "
            "than a dime, and yet the dime is worth twice as much. With coins, size does not tell you value.",
         "board": ['[[numberline min="0" max="25" points="5,10,15,20,25" caption="counting nickels — five cents in every jump"]]']},
        {"term": "quarter", "say":
            "A **quarter** is the big silver coin, and it is worth twenty five cents. Four of them make one "
            "dollar, and that is exactly where the name comes from. The word means one of four equal parts. "
            "Counting them goes twenty five, fifty, seventy five, one hundred. Two of them are fifty cents, "
            "which is half a dollar. It is the biggest everyday coin and also the one worth the most.",
         "board": ['[[pie parts="4" shaded="1" caption="one whole, cut into four equal parts"]]', '[[write text="25¢ + 25¢ + 25¢ + 25¢  =  $1"]]']},
        {"term": "ruler", "say":
            "A **ruler** is a straight measuring tool with marks along the edge. Those marks are not "
            "decoration. They are a number line printed on a stick, and they begin at zero. To measure, put the "
            "zero mark at one end of the object and read the number where the object stops. Beginners often "
            "line things up with the plastic edge, or with the one, and that answer comes out wrong every time.",
         "board": ['[[numberline min="0" max="12" points="0" caption="a ruler is a number line — the object starts at 0"]]']},
        {"term": "shape", "say":
            "A **shape** is the outline of something, the form it makes, whatever size or color it happens to "
            "be. A triangle has three straight sides. A square has four straight sides, all the same length. A "
            "circle has no straight sides at all, just one curve. What gives a name is the number of sides and "
            "corners. Turning one sideways changes nothing. A triangle standing on its point is still a "
            "triangle.",
         "board": ['[[card title="Count the sides and corners" items="triangle: 3 straight sides | square: 4 equal sides | circle: no straight sides"]]']},
        {"term": "time", "say":
            "**Time** is how we measure when something happens and how long it lasts. We count it in seconds, "
            "then minutes, then hours, then days. Sixty seconds make one minute, and sixty minutes make one "
            "hour. Notice that those counts do not go up in tens the way our numbers usually do. They go up in "
            "sixties. That is why reading a clock feels strange at first.",
         "board": ['[[card title="How we count time" items="60 seconds = 1 minute | 60 minutes = 1 hour | 24 hours = 1 day"]]']},
    ],
    "basic": [
        {"term": "fraction", "say":
            "Here is what a **fraction** is. A fraction is a number that describes equal parts of one "
            "whole. The word equal matters: if I cut a cookie into two pieces and one piece is tiny, "
            "those are not halves. So the way we use fractions today: we cut something into fair, "
            "matching pieces, and then we talk about some of those pieces.",
         "board": ['[[pie parts="4" shaded="1" caption="one whole, cut into four equal parts — one of them is shaded"]]']},
        {"term": "denominator", "say":
            "Every fraction is written with two numbers, and each one has a job. The bottom number is "
            "called the **denominator**. It tells you how many equal pieces the whole was cut into. A "
            "bigger denominator means the whole got cut into more pieces, so each piece is smaller. That "
            "surprises a lot of people: one eighth is smaller than one fourth, even though eight is "
            "bigger than four.",
         "board": ['[[write text="1/4   ← the 4 is the DENOMINATOR: four equal pieces"]]']},
        {"term": "numerator", "say":
            "The top number is called the **numerator**, and it tells you how many of those pieces we are "
            "talking about. So in three fourths, the four says the whole was cut into four equal pieces, "
            "and the three says we have three of them. Bottom number: how many pieces in all. Top number: "
            "how many we are counting. That is the whole idea.",
         "board": ['[[write text="3/4   ← the 3 is the NUMERATOR: three of those pieces"]]',
                   '[[pie parts="4" shaded="3" caption="four equal pieces, and we have three of them"]]']},
        {"term": "decimal", "say":
            "A **decimal** is another way to write parts of a whole, using place value instead of two "
            "stacked numbers. The dot is called the decimal point, and everything to the right of it is "
            "smaller than one. The first place after the point is tenths, the next is hundredths. Money "
            "is the easiest example: one dollar and fifty cents is one and five tenths of a dollar.",
         "board": ['[[write text="1.5   =   1 whole  +  5 tenths"]]']},
        {"term": "place value", "say":
            "**Place value** is the rule that makes our whole number system work. A digit means something "
            "different depending on where it sits. In four thousand five hundred, the four is not four. "
            "It is four thousands. Every place to the left is worth ten times the place before it: ones, "
            "tens, hundreds, thousands. That is also why zero matters so much. In five hundred four, the "
            "zero holds the tens place open so the five stays a hundred.",
         "board": ['[[write text="4,500  =  4 thousands + 5 hundreds + 0 tens + 0 ones"]]']},
        {"term": "rounding", "say":
            "**Rounding** means swapping a number for a nearby friendly one so it is easier to work with. "
            "To round to the nearest ten, ask which ten the number sits closest to. Thirty-seven is "
            "closer to forty than to thirty, so it rounds to forty. A five is the tie, and by agreement "
            "we round a tie up. Rounding makes a number less exact on purpose. We use it when close "
            "enough is honestly good enough, like guessing a grocery total.",
         "board": ['[[numberline min="30" max="40" points="37" caption="37 sits closer to 40 than to 30"]]',
                   '[[write text="37 is nearer 40   →   round to 40"]]']},
        {"term": "multiplication", "say":
            "**Multiplication** is a shortcut for adding the same number again and again. Six times four "
            "means six groups with four in each group, which is four added six times over. Instead of "
            "adding all day, you learn the fact. One more thing worth knowing early. Order does not "
            "change the answer. Six groups of four and four groups of six both come to twenty-four, even "
            "though they draw as different pictures.",
         "board": ['[[objects emoji="🍎" groups="6" caption="equal groups — equal groups are what multiplying counts"]]',
                   '[[write text="6 × 4  =  4+4+4+4+4+4  =  24"]]']},
        {"term": "division", "say":
            "**Division** is splitting an amount into equal parts. Twelve divided by three can be read "
            "two ways, and both are right. It can mean sharing twelve cookies fairly among three people, "
            "so four each. Or it can mean asking how many groups of three fit inside twelve, which is "
            "also four. Division undoes multiplication. That is why every division fact has a "
            "multiplication fact hiding right behind it.",
         "board": ['[[write text="12 ÷ 3 = 4      because      3 × 4 = 12"]]']},
        {"term": "remainder", "say":
            "Sometimes an amount refuses to split evenly, and the leftover part is called the "
            "**remainder**. Share fourteen cookies among four people and everybody gets three, with two "
            "cookies left over. Those two are the remainder. A remainder is always smaller than the "
            "number you divided by. If it were as big, you could hand out one more whole group. What you "
            "do with leftovers depends on the question. Sometimes you round up, sometimes you drop them.",
         "board": ['[[write text="14 ÷ 4  =  3 remainder 2"]]']},
        {"term": "factor", "say":
            "A **factor** is a number that divides into another number evenly, with nothing left over. "
            "Three is a factor of twelve, because three goes into twelve exactly four times. Factors come "
            "in pairs. For twelve, the pairs are one and twelve, two and six, three and four. A factor is "
            "never bigger than the number it belongs to. That single fact is the quickest way to catch a "
            "mistake in your list.",
         "board": ['[[write text="factors of 12:  1, 2, 3, 4, 6, 12"]]']},
        {"term": "multiple", "say":
            "A **multiple** is what you get when you count by a number. The multiples of four are four, "
            "eight, twelve, sixteen, and they keep going forever. Here is the part that gets tangled, so "
            "listen closely. Factors are the numbers that fit inside. Multiples are the numbers you land "
            "on heading out. Three is a factor of twelve. Twelve is a multiple of three. Same two "
            "numbers, opposite directions.",
         "board": ['[[write text="multiples of 4:  4, 8, 12, 16, 20 ..."]]']},
        {"term": "prime number", "say":
            "A **prime number** has exactly two factors: one, and itself. Seven is prime, because only "
            "one and seven divide into it evenly. Twelve is not prime, because two, three, four and six "
            "all fit inside it. A number with more than two factors is called composite. Two quick "
            "warnings. One is not prime, because it only has a single factor. And two is prime, even "
            "though it is even. It is the only even prime there is.",
         "board": ['[[card title="Prime or not" items="7 is prime | 12 is composite | 1 is neither | 2 is the only even prime"]]']},
        {"term": "equivalent fractions", "say":
            "**Equivalent fractions** are fractions that look different but are worth exactly the same "
            "amount. One half, two fourths, and four eighths are the same slice of pizza, just cut with "
            "more or fewer cuts. You build one by multiplying the top number and the bottom number by the "
            "same thing, and that works because you are really multiplying by one. Change only the top, "
            "or only the bottom, and you have changed the value, not just the look.",
         "board": ['[[write text="1/2  =  2/4  =  4/8"]]',
                   '[[pie parts="4" shaded="2" caption="two of the four equal pieces — count them, it is the same as one half"]]']},
        {"term": "common denominator", "say":
            "A **common denominator** means two fractions have been cut into pieces of the same size. You "
            "need one before you add or subtract fractions, and here is exactly why. One third plus one "
            "fourth is not two sevenths. Thirds and fourths are different sizes, so you cannot count them "
            "together. Rewrite both as twelfths and now the pieces match: four twelfths and three "
            "twelfths make seven twelfths. Matching pieces first, then counting.",
         "board": ['[[write text="1/3 + 1/4   →   4/12 + 3/12   =   7/12"]]']},
        {"term": "ratio", "say":
            "A **ratio** compares two amounts. If a bracelet uses three blue beads for every two white "
            "beads, the ratio of blue to white is three to two. A ratio does not tell you how many beads "
            "you have altogether. It tells you how the amounts compare. Double it and you get six blue "
            "and four white, and the ratio has not changed one bit. Order matters too. Three to two and "
            "two to three describe different bracelets.",
         "board": ['[[write text="blue : white  =  3 : 2  =  6 : 4"]]']},
        {"term": "percent", "say":
            "**Percent** means out of one hundred. That is literally what the word says: per hundred. So "
            "thirty percent means thirty out of every hundred. Because of that, every percent is also a "
            "decimal and a fraction wearing a different coat. Thirty percent is thirty hundredths, which "
            "is zero point three. Fifty percent is one half. Twenty-five percent is one fourth. When a "
            "percent confuses you, say out of a hundred in your head and it settles down.",
         "board": ['[[write text="30%  =  30/100  =  0.30"]]']},
        {"term": "perimeter", "say":
            "**Perimeter** is the distance all the way around the outside of a shape. If you walked the "
            "edge of a soccer field, the steps you took would be the perimeter. You find it by adding up "
            "the lengths of every side. Perimeter is measured in ordinary units like feet or centimetres, "
            "because it is simply a length. Keep this picture: perimeter is the fence, not the carpet.",
         "board": ['[[write text="rectangle 5 by 3:   5 + 3 + 5 + 3  =  16 units around"]]']},
        {"term": "area", "say":
            "**Area** is how much flat space a shape covers. If perimeter is the fence around a yard, "
            "area is the grass inside it. We measure area in square units, because we are really counting "
            "how many little squares fit inside. For a rectangle you multiply the length by the width, "
            "and that works because you are counting rows of squares. That is also why we say square feet "
            "or square centimetres, never plain feet.",
         "board": ['[[write text="rectangle 5 by 3:   5 × 3  =  15 square units"]]']},
        # --- build gc (2026-08-14): red-list additions for this course. See the
        # change note at the top of this file. Appended, never edited.
        {"term": "angle", "say":
            "An **angle** is the amount of turn between two lines that meet at a corner. We measure that turn "
            "in degrees. A square corner, like the corner of a book, is ninety degrees. Here is the thing that "
            "trips people up. How long the two lines are does not matter at all. Stretch them out as far as you "
            "like and the turn between them stays exactly the same.",
         "board": ['[[angle deg="90" caption="a square corner — ninety degrees"]]', '[[angle deg="30" caption="a smaller turn — notice the opening, not the arms"]]']},
        {"term": "composite", "say":
            "A whole number is **composite** when it has more than two factors, meaning something other than "
            "one and itself divides into it evenly. Twelve is one of them, because two, three, four and six all "
            "fit inside it exactly. Nine is one too, since three goes into it three times. A whole number "
            "bigger than one is either prime or it belongs in this group. One belongs in neither, because it "
            "has only a single factor.",
         "board": ['[[card title="Prime or composite" items="12: factors 1, 2, 3, 4, 6, 12 | 7: factors 1, 7 | 1: factor 1 only"]]']},
        {"term": "hundredths", "say":
            "The second place after the decimal point is the **hundredths** place. It means one whole has been "
            "cut into one hundred equal pieces. Money shows it best. A penny is one of those pieces of a "
            "dollar, and one hundred of them make the whole dollar. Watch the sizes carefully. Each piece here "
            "is smaller than a tenth, because the same whole was cut into more parts. Ten of them make one "
            "tenth.",
         "board": ['[[write text="0.07  =  7/100          0.7  =  7/10"]]']},
        {"term": "tenths", "say":
            "The first place after the decimal point is the **tenths** place. It means the whole has been split "
            "into ten equal pieces, and the digit sitting there counts how many of those pieces you have. So "
            "zero point three is three of them, the same amount as three over ten. A dime is a good picture, "
            "since ten dimes make a dollar. One warning: this is the largest of the places after the point, not "
            "the smallest.",
         "board": ['[[pie parts="10" shaded="3" caption="one whole, cut into ten equal parts"]]', '[[write text="0.3  =  3/10     first place after the point"]]']},
    ],
    "prealgebra": [
        {"term": "negative number", "say":
            "A **negative number** is a number less than zero. That sounds strange until you picture a "
            "thermometer or an elevator. Zero is the ground floor. Positive numbers go up from there, and "
            "negative numbers go down below it. Negative three is not nothing and it is not three — it is "
            "three steps below zero, and it is a real, exact place on the number line.",
         "board": ['[[numberline min="-6" max="6" points="-3" caption="negative three — three steps BELOW zero"]]']},
        {"term": "percent", "say":
            "**Percent** means out of one hundred. That is all the word means: per hundred. So fifty "
            "percent is fifty out of a hundred, which is the same as one half. Twenty-five percent is "
            "twenty-five out of a hundred, which is one fourth. Whenever you see a percent, you can "
            "always say out of a hundred in your head and it will make sense.",
         "board": ['[[write text="50%  =  50 out of 100  =  1/2"]]']},
        {"term": "ratio", "say":
            "A **ratio** compares two amounts. If a recipe uses two cups of flour for every one cup of "
            "sugar, the ratio of flour to sugar is two to one. Notice a ratio does not tell you how much "
            "you have altogether — it tells you how the amounts compare. Double everything and the ratio "
            "stays exactly the same.",
         "board": ['[[write text="flour : sugar  =  2 : 1"]]']},
        {"term": "place value", "say":
            "**Place value** is the idea that a digit's worth depends on where it sits. The digit five "
            "means five in the ones spot, fifty in the tens spot, and five hundred in the hundreds spot. "
            "Same digit, different job. Each place to the left is worth ten times the place before it, "
            "and each place to the right is worth one tenth as much. That is why three hundred four is "
            "not the same as thirty four. The zero in the tens spot is holding a place open, and it is "
            "doing real work.",
         "board": ['[[write text="304  =  3 hundreds + 0 tens + 4 ones"]]']},
        {"term": "order of operations", "say":
            "The **order of operations** is the agreed order for doing a calculation, so that everybody "
            "gets the same answer. Grouping symbols first, then exponents, then multiplying and dividing, "
            "then adding and subtracting. Here is the part people miss. Multiplying and dividing are a "
            "tie, so you do them left to right as they come, and adding and subtracting work the same "
            "way. It is four stages, not six separate steps. Without this agreement, two people could "
            "read the same problem and get two different answers, and math refuses to allow that.",
         "board": ['[[write text="2 + 3 × 4  =  2 + 12  =  14      (not 20)"]]']},
        {"term": "factor", "say":
            "A **factor** is a number that divides into another number evenly, with nothing left over. "
            "Three is a factor of twelve, because four threes make twelve exactly. Multiples run the "
            "other direction. Twelve is a multiple of three. Students mix those two up constantly, so "
            "hold on to this. Factors are the same size as the number or smaller, and there are only a "
            "few of them. Multiples are the same size as the number or bigger, and they go on forever.",
         "board": ['[[card title="the number 12" items="factors: 1, 2, 3, 4, 6, 12 | multiples: 12, 24, 36, 48, ..."]]']},
        {"term": "prime number", "say":
            "A **prime number** is a whole number with exactly two factors, one and itself. Seven is "
            "prime, because only one and seven divide into it evenly. Twelve is not, because two, three, "
            "four and six all go in, so we call twelve composite. One is the odd case. One is not prime, "
            "because it has only a single factor, itself, and prime means exactly two. Primes are the "
            "building blocks of every other number. Any whole number can be built by multiplying primes, "
            "and there is only one way to do it.",
         "board": ['[[card title="prime or not" items="7 → prime | 12 → composite | 1 → neither"]]']},
        {"term": "greatest common factor", "say":
            "The **greatest common factor** of two numbers is the biggest number that divides evenly into "
            "both of them. List the factors of twelve, list the factors of eighteen, find the ones they "
            "share, and take the largest. That is six. The word common is the one to hold on to. It has "
            "to go into both numbers, not just one. You will use this every time you simplify a fraction, "
            "because dividing the top and the bottom by their greatest common factor puts the fraction in "
            "lowest terms in a single move.",
         "board": ['[[write text="12: 1,2,3,4,6,12    18: 1,2,3,6,9,18    →  GCF = 6"]]']},
        {"term": "absolute value", "say":
            "**Absolute value** is how far a number is from zero, ignoring which direction you went. "
            "Negative four is four steps from zero, and positive four is also four steps from zero, so "
            "both of them have an absolute value of four. We write it with two straight bars around the "
            "number. Distance is never negative, and that is the entire reason this idea exists. It "
            "answers how far, not which way. So the absolute value of negative four is four. It is not "
            "negative four, and it is not simply the opposite of the number either.",
         "board": ['[[numberline min="-6" max="6" points="-4,4" caption="both are 4 steps from zero"]]']},
        {"term": "equivalent fractions", "say":
            "**Equivalent fractions** are fractions that look different but name the same amount. One "
            "half, two fourths and four eighths all cover the same part of a pizza. The pizza was cut "
            "differently, but the amount you get is identical. You make one by multiplying the top and "
            "the bottom by the same number, or by dividing the top and the bottom by the same number. "
            "Both is the key word there. Change only the top and you have changed the amount, not just "
            "the way it looks.",
         "board": ['[[pie parts="8" shaded="4" caption="eight equal pieces with four shaded — the same amount as one half"]]']},
        {"term": "mixed number", "say":
            "A **mixed number** is a whole number and a fraction written side by side, like two and one "
            "third. It means exactly what it looks like. Two whole things, and one third of another one. "
            "Pizza makes it obvious: two whole pizzas, plus one third of a third pizza. The one thing "
            "worth saying out loud is that those two parts are added together, never multiplied, even "
            "though they sit right next to each other with no sign between them.",
         "board": ['[[write text="2 1/3   means   2 + 1/3      (added, never multiplied)"]]']},
        {"term": "decimal", "say":
            "A **decimal** is a way of writing parts of a whole using place value instead of a fraction "
            "bar. Everything to the right of the decimal point is less than one. The first place is "
            "tenths, the next is hundredths, the next is thousandths, each one ten times smaller than the "
            "place before it. Money is the everyday version of this. Two dollars and seven cents is two "
            "point zero seven, and that zero matters, because seven cents is seven hundredths of a "
            "dollar, not seven tenths.",
         "board": ['[[write text="2.07  =  2 wholes + 0 tenths + 7 hundredths"]]']},
        {"term": "unit rate", "say":
            "A **unit rate** tells you how much of one thing you get for exactly one of another thing. "
            "Miles per hour, dollars per pound, words per minute. The word per is the giveaway, and it "
            "means for each one. If twelve dollars buys three pounds, divide twelve by three, and you get "
            "four dollars for one pound. That is the unit rate. It is what makes shopping comparisons "
            "possible, because two prices on two different sized packages cannot be compared until you "
            "know what one pound of each actually costs.",
         "board": ['[[write text="$12 for 3 lb   →   $4 per 1 lb"]]']},
        {"term": "proportion", "say":
            "A **proportion** is a statement that two ratios are equal. If three pencils cost two "
            "dollars, then six pencils cost four dollars, and those two comparisons form a proportion. "
            "Both amounts doubled, so the comparison between them never changed. That is why cross "
            "multiplying works: the two fractions are equal, so their cross products have to match. One "
            "caution. Keep the same kind of thing on top in both ratios. Pencils over dollars on one side "
            "means pencils over dollars on the other side too.",
         "board": ['[[write text="3 pencils / $2   =   6 pencils / $4"]]']},
        {"term": "area", "say":
            "**Area** is the amount of flat space inside a shape, and we measure it in squares. Picture "
            "covering a floor with one foot tiles and counting them. That count is the area, which is why "
            "the units are square feet. Perimeter is a different question. Perimeter is the distance all "
            "the way around the edge, like the fence. Area is the carpet inside it. For a rectangle, you "
            "multiply the length by the width, because the length tells you how many tiles fit in one "
            "row, and the width tells you how many rows there are.",
         "board": ['[[write text="6 ft × 4 ft  =  24 square feet"]]']},
        {"term": "mean", "say":
            "The **mean** is the fair share average. You pool everything together, then split it evenly "
            "among however many there are. If three friends have three dollars, five dollars and ten "
            "dollars, that is eighteen dollars shared three ways, so six dollars each. The mean answers "
            "one question. If everybody had the same amount, how much would that be? It is not the middle "
            "number, and it is not the most common number. Those are different measures, and they have "
            "their own names.",
         "board": ['[[write text="(3 + 5 + 10) ÷ 3  =  6"]]']},
        {"term": "expression", "say":
            "An **expression** is a math phrase, and it has no equals sign in it. Three n plus two is an "
            "expression. It does not claim anything is true or false. It just describes an amount, and "
            "that amount depends on what n happens to be. Evaluating an expression means choosing a value "
            "for the letter and working it out, so when n is four, three n plus two comes out to "
            "fourteen. An equation is a different animal. An equation has two sides and claims they are "
            "equal. Phrase against full sentence. That is the difference.",
         "board": ['[[write text="3n + 2      an expression — no = sign"]]']},
        {"term": "like terms", "say":
            "**Like terms** are terms with exactly the same letter part. Three x and five x are like "
            "terms, so you can add them and get eight x, the same way three apples and five apples make "
            "eight apples. Three x and five y are not like terms, and neither are three x and plain five. "
            "You cannot combine those, and there is nothing wrong with an answer that still has two "
            "pieces in it. When you do combine like terms, the letter never changes. Only the number in "
            "front of it does.",
         "board": ['[[write text="3x + 5x = 8x        3x + 5y stays 3x + 5y"]]']},
        # --- build gc (2026-08-14): red-list additions for this course. See the
        # change note at the top of this file. Appended, never edited.
        {"term": "angle", "say":
            "An **angle** is the amount of turn between two straight arms that meet at a shared corner point. "
            "We measure that turn in degrees. A square corner is ninety degrees, and a perfectly straight "
            "opening is one hundred and eighty. Here is the part almost everyone gets wrong at first. Drawing "
            "the arms longer does not make the turn bigger. Only the opening between the arms counts, so a "
            "narrow corner with very long arms is still small.",
         "board": ['[[angle deg="40" caption="notice the opening, not how long the arms are drawn"]]']},
        {"term": "composite", "say":
            "The word **composite** describes a whole number bigger than one that can be divided evenly by "
            "something other than one and itself. Twelve qualifies, because two, three, four and six all go in "
            "exactly. Seven does not, because only one and seven go in, so seven is prime instead. Watch the "
            "number one. It belongs to neither group, because it has just one factor, itself, and each group "
            "needs more than that.",
         "board": ['[[card title="count the factors" items="12 goes with 1, 2, 3, 4, 6, 12 | 7 goes with 1, 7 | 1 goes with just 1"]]']},
        {"term": "equation", "say":
            "An **equation** is a number sentence saying that two things are worth exactly the same amount. The "
            "equals sign in the middle is a promise that the left side and the right side match, like a scale "
            "sitting perfectly level. That is why, whenever you change one side, you must do the very same "
            "thing to the other side. Something like three n plus two makes no such claim, so we call it an "
            "expression, and there is nothing there to solve.",
         "board": ['[[balance left="2x + 3" right="11" state="level" caption="whatever you do to one side, do to the other"]]']},
        {"term": "hundredths", "say":
            "The second place to the right of the decimal point counts **hundredths**, and one of them is a "
            "whole cut into one hundred equal pieces. Money is the everyday version, because one cent is one "
            "hundredth of a dollar. Here is the trap. Zero point seven and zero point zero seven look alike, "
            "but they are nowhere near the same size. The first one is seventy cents. The second one is seven "
            "cents, ten times smaller.",
         "board": ['[[write text="0.7  =  70 cents           0.07  =  7 cents"]]']},
        {"term": "multiple", "say":
            "A **multiple** of a number is what you get by multiplying that number by a whole number. Three "
            "times one is three, three times two is six, three times three is nine, so three, six and nine all "
            "belong on the list for three. This is the idea students swap with factors. Factors are the same "
            "size as your number or smaller, and there are only a few of them. Multiplying runs the other way, "
            "so that list keeps climbing and never ends.",
         "board": ['[[card title="the number 3" items="factors of 3: 1, 3 — only two of them | 3, 6, 9, 12, 15, 18 and on — no end"]]']},
        {"term": "number line", "say":
            "A **number line** is a straight road where every number has its own address. Zero is the marker we "
            "count from, numbers grow as you travel right, and they shrink as you travel left. That is why "
            "negative five sits further left than negative two, and is the smaller of the two, which surprises "
            "people. The labelled marks are not the only homes. One half, two and a quarter, and every decimal "
            "sit at exact spots in between.",
         "board": ['[[numberline min="-6" max="6" points="-5,-2" caption="further left is always the smaller number"]]']},
        {"term": "opposite", "say":
            "The **opposite** of a number sits the same distance from zero, but on the other side. Five and "
            "negative five are a pair, because both are five steps from zero. Add any number to its partner and "
            "you always land on zero, which is the whole point of the idea. One warning. Taking it is not just "
            "writing a minus sign in front of what you see, because the partner of negative three is positive "
            "three.",
         "board": ['[[numberline min="-6" max="6" points="-3,3" caption="same distance from zero, opposite sides"]]']},
        {"term": "perimeter", "say":
            "The **perimeter** of a shape is the distance all the way around its outside edge. Picture walking "
            "the fence around a yard and counting your steps. You add every side, and no side gets skipped. "
            "Area asks something different: how much grass is inside that fence, counted in squares. So this "
            "measurement is given in plain feet or plain centimetres, never square feet.",
         "board": ['[[write text="6 + 4 + 6 + 4      every side, all the way around"]]']},
        {"term": "tenths", "say":
            "The first place to the right of the decimal point counts **tenths**, which is one whole cut into "
            "ten equal pieces. Zero point five is five of those pieces, the same amount as one half. Do not mix "
            "this place up with the tens place, which sits on the other side of the point. Tens are far bigger "
            "than one, while every one of these pieces is smaller than one.",
         "board": ['[[pie parts="10" shaded="5" caption="one whole cut into ten equal pieces"]]']},
    ],
    "algebra1": [
        {"term": "variable", "say":
            "A **variable** is a letter that stands for a number we do not know yet. That is the whole "
            "trick of algebra: instead of guessing, we give the mystery number a name, usually x, and "
            "then we work out what it has to be. The letter is not magic and it is not a code — it is a "
            "placeholder sitting where a number will go.",
         "board": ['[[write text="x  =  the number we do not know yet"]]']},
        {"term": "equation", "say":
            "An **equation** is a statement that two things are equal. The equals sign is the important "
            "part: it says the left side and the right side are the very same amount, like a balance "
            "scale that is level. That is why, whenever we change one side, we must do exactly the same "
            "thing to the other side — otherwise the scale tips and the statement stops being true.",
         "board": ['[[balance left="2x + 3" right="11" state="level" caption="both sides are the same amount"]]']},
        {"term": "coefficient", "say":
            "In something like two x, the two is called the **coefficient**. It just means how many of "
            "that variable we have. Two x means two of them, added together — x plus x. And because it "
            "means multiply, we undo it by dividing. A coefficient is not attached by addition, which is "
            "why we never subtract it away.",
         "board": ['[[write text="2x  =  x + x   (2 is the COEFFICIENT)"]]']},
        {"term": "like terms", "say":
            "**Like terms** are terms whose variable parts match exactly, exponents included. Four x and "
            "seven x are like terms. Four x squared and seven x are not, because x squared and x are "
            "genuinely different things. Only like terms can be combined, and combining them is really "
            "just counting. Four of them plus seven of them is eleven of them. The variable part never "
            "changes when you combine. Four x squared plus three x squared is seven x squared, not seven "
            "x to the fourth.",
         "board": ['[[write text="4x² + 3x² = 7x²        4x² + 7x  stays as it is"]]']},
        {"term": "distributive property", "say":
            "The **distributive property** says that multiplying a sum is the same as multiplying each "
            "piece and then adding. Three times the quantity x plus two equals three x plus six. Picture "
            "a rectangle three tall and x plus two wide. You can find the whole area at once, or split it "
            "into two smaller rectangles and add them. Same area either way. The mistake to avoid is "
            "handing the three to only the first term. It multiplies everything inside the parentheses, "
            "every term, or the two sides stop being equal.",
         "board": ['[[areamodel rows="3" cols="x,2" caption="one rectangle, split in two — the area is the same either way"]]']},
        {"term": "inequality", "say":
            "An **inequality** compares two things that are not necessarily equal. Instead of one exact "
            "answer, its solution is a whole range of numbers, which is why we draw it on a number line "
            "instead of circling a single point. Solving one works almost exactly like solving an "
            "equation. Almost. Here is the one rule that is different, and it is the rule people forget. "
            "If you multiply or divide both sides by a negative number, the inequality sign flips "
            "direction. Negative two x less than six becomes x greater than negative three.",
         "board": ['[[numberline min="-6" max="6" ineq="x > -3" caption="x > −3 : the whole shaded ray, not one point"]]']},
        {"term": "function", "say":
            "A **function** is a rule that takes an input and gives back exactly one output. Exactly one "
            "is the whole definition. Put in a three, and you get the same answer back every single time. "
            "A vending machine is the picture. Press the same button, get the same snack. An input is "
            "never allowed to have two different outputs. That is what separates a function from any old "
            "relationship between numbers, and it is exactly what the vertical line test on a graph is "
            "checking for you.",
         "board": ['[[machine input="3" rule="2x+1" output="7" fname="f" caption="one input goes in, exactly one output comes out"]]']},
        {"term": "function notation", "say":
            "Here, f is the NAME of a rule. So f with something tucked inside parentheses right after "
            "it is **function notation**, and you read it out loud as f of x. Say it that way every "
            "single time. It is a name and an input: the rule called f, handed the value x. Nothing "
            "here is being multiplied, though parentheses really do mean multiplying in other places, "
            "so what tells them apart is whether the letter in front names a rule. And that letter is "
            "only a name, the way a person is called Sam. If a problem needs a second rule we usually "
            "call it g, and g of x works exactly the same way.",
         "board": ['[[write text="f(x)   ←  say it out loud: “f of x”     (NOT f times x)"]]',
                   '[[write text="f(3) = 7   means: hand 3 to the rule called f, and 7 comes back"]]',
                   '[[card title="the letter is only a name" items="f(x) — the rule called f | g(x) — a second rule, called g | both are read “… of x”"]]']},
        {"term": "domain", "say":
            "The **domain** of a function is the complete collection of inputs it is allowed to take. "
            "Most of the time every number works, but not always. The rule on the board reads: f of x "
            "equals one over x -- and if the rule divides by x, then x cannot "
            "be zero, because dividing by zero has no answer at all. If the rule takes a square root, "
            "whatever sits under that root cannot be negative. So the domain is not a formality you write "
            "down to be tidy. It is the honest answer to one question. Which numbers can I actually put "
            "into this machine without breaking it?",
         "board": ['[[write text="f(x) = 1/x    →   domain: every number except 0"]]']},
        {"term": "range", "say":
            "The **range** of a function is everything that can come back out of it. Domain in, range "
            "out. That pairing is worth memorizing on the spot. Take the rule x squared. You may put in "
            "any number you like, so the domain is every number, but squaring never produces a negative "
            "result, so the range is zero and up. The range is decided by the rule, not chosen by you. "
            "You find it by asking which outputs are actually reachable, and which ones never happen.",
         "board": ['[[graph func="x^2" range="-5..5" yrange="-2..20" caption="any input is allowed; the outputs are 0 and up"]]']},
        {"term": "slope", "say":
            "**Slope** is a rate of change. It tells you how much y moves for every one step x takes to "
            "the right. We say rise over run, which is the change up or down divided by the change "
            "across. A slope of two means up two for every one across, and a steeper line carries a "
            "bigger number. A negative slope heads downhill. Real life is full of them. Forty miles per "
            "hour is a slope, and so is nine dollars an hour. Slope is not where the line sits. It is how "
            "fast the line climbs.",
         "board": ['[[graph lines="y=2x" caption="slope 2 — up 2 for every 1 across"]]']},
        {"term": "y-intercept", "say":
            "The **y-intercept** is where a line crosses the y axis. That is the point where x is zero, "
            "so it is the starting value, before anything has changed yet. In y equals m x plus b, the b "
            "is that starting value and the m is the slope. Think about a phone plan. Twenty dollars just "
            "to have the line, then five dollars every month. The twenty is the y-intercept, what you owe "
            "at month zero, and the five is the slope, what each month adds on top.",
         "board": ['[[graph lines="y=5x+20" caption="starts at 20, climbs 5 each month"]]']},
        {"term": "system of equations", "say":
            "A **system of equations** is two or more equations that must be true at the same time, with "
            "the same values for the letters. That last part is everything. You are not solving them "
            "separately. You are hunting for the one pair of numbers that satisfies both at once. On a "
            "graph, that pair is the point where the two lines cross. Which also explains the strange "
            "cases. Parallel lines never cross, so there is no solution, and two equations that are "
            "secretly the same line cross everywhere, so there are infinitely many.",
         "board": ['[[graph lines="y=2x+1 ; y=-x+4" range="-3..5" yrange="-4..8" caption="the crossing point solves both equations at once"]]']},
        {"term": "exponent", "say":
            "An **exponent** counts how many times a number is used as a factor in a multiplication. Two "
            "to the fifth means five twos multiplied together, which is thirty two. It does not mean two "
            "times five. That single misunderstanding causes more wrong answers than almost anything else "
            "in this course. Every law of exponents comes straight out of this counting idea. Two cubed "
            "times two squared is three twos and then two more twos, so five twos altogether, which is "
            "why you add the exponents rather than multiply them.",
         "board": ['[[write text="2³ × 2² = 2⁵      (3 twos and 2 twos = 5 twos)"]]']},
        {"term": "exponential growth", "say":
            "**Exponential growth** means an amount multiplies by the same factor over and over, instead "
            "of adding the same amount over and over. That difference is enormous. A linear job pays you "
            "ten dollars a day. An exponential one doubles your money every day. Start with one penny, "
            "and by the end of a month the doubling has passed five million dollars. These graphs look "
            "flat and lazy at first, then rise almost straight up. When the factor is smaller than one, "
            "the same rule runs backwards, and you get decay instead.",
         "board": ['[[graph func="2^x" range="-2..5" yrange="-2..32" caption="each step multiplies — it does not add"]]']},
        {"term": "polynomial", "say":
            "A **polynomial** is a sum of terms in which every variable carries a whole number exponent, "
            "zero or larger. Three x squared minus five x plus two is a polynomial. Something with x "
            "sitting in the denominator, or trapped under a square root, is not. The largest exponent is "
            "called the degree, and it is the first thing to look at, because the degree tells you the "
            "shape of the graph and how many solutions to expect. Degree one is a straight line. Degree "
            "two is a curve with a single turn in it.",
         "board": ['[[write text="3x² − 5x + 2      degree 2"]]']},
        {"term": "factoring", "say":
            "**Factoring** is multiplying, run backwards. Instead of taking two pieces and expanding "
            "them, you start with the expanded expression and find the pieces it came from. x squared "
            "plus five x plus six factors into the quantity x plus two, times the quantity x plus three. "
            "Multiply those back out and you land exactly where you started, which is how you check every "
            "single time. The reason we bother is this. A product that equals zero means one of its "
            "pieces must be zero, and that turns one hard equation into two easy ones.",
         "board": ['[[areamodel rows="x,2" cols="x,3" caption="the same area, written as length × width"]]']},
        {"term": "quadratic", "say":
            "A **quadratic** is an expression or equation where the highest power of the variable is two. "
            "That one detail changes everything that follows. Its graph is not a line, it is a U shaped "
            "curve called a parabola, and instead of one solution it usually has two, because a curve can "
            "cross the x axis in two separate places. The turning point of that curve is called the "
            "vertex. Any time you see an x squared term and nothing higher, you are looking at a "
            "quadratic, and the whole toolkit changes with it.",
         "board": ['[[graph parabola="y=x^2-3x-4" range="-4..7" yrange="-8..12" caption="a parabola — it can cross the x-axis in two places"]]']},
        {"term": "correlation", "say":
            "**Correlation** means two things tend to move together. Plot the pairs on a scatter plot. If "
            "the dots drift upward the correlation is positive, if they drift downward it is negative, "
            "and if they look like scattered dust there is barely any correlation at all. Here is the "
            "part that matters outside this classroom. Correlation is not causation. Ice cream sales and "
            "swimming accidents rise together, but the ice cream is not causing anything. Hot weather "
            "drives both. A strong pattern alone never proves one thing made the other happen.",
         "board": ['[[write text="strong pattern  ≠  one thing caused the other"]]']},
        # --- build gc (2026-08-14): red-list additions for this course. See the
        # change note at the top of this file. Appended, never edited.
        {"term": "decay", "say":
            "We say an amount is in **decay** when it keeps getting multiplied by the same fraction below one, "
            "over and over, so it drops quickly at first and then more and more slowly. A medicine that halves "
            "every four hours behaves this way. Take care here. Losing ten units every hour is not that "
            "pattern, it is steady subtraction. Repeated multiplying like this can never reach zero either, "
            "only creep closer to it.",
         "board": ['[[graph func="0.5^x" range="-2..6" caption="steep at first, then flattening, and never touching zero"]]']},
        {"term": "expression", "say":
            "An **expression** is a mathematical phrase built from numbers, letters and operations, with no "
            "equals sign anywhere in it. Three x plus five is one. Since it claims nothing, there is nothing in "
            "it to solve. You can tidy it up by combining like terms, or you can evaluate it by choosing a "
            "value for x. An equation is the full sentence: two sides joined by an equals sign, and that is the "
            "thing you solve.",
         "board": ['[[write text="3x + 5   —   an expression, nothing to solve"]]']},
        {"term": "line", "say":
            "A **line** is a perfectly straight path that runs on forever in both directions. In algebra you "
            "usually meet it as the graph of two quantities changing together at a steady rate, so the plotted "
            "dots fall dead straight. That forever part matters, because a piece with two endpoints is called a "
            "segment instead. Any two different points fix exactly one straight path, which is why plotting two "
            "good points is enough to draw it.",
         "board": ['[[graph func="2x + 1" caption="steady climb, no bends, running on both ways"]]']},
        {"term": "mean", "say":
            "The **mean** is the fair share average. Add all the values together, then split that total evenly "
            "among however many values you had. Three friends holding three dollars, five dollars and ten "
            "dollars have eighteen dollars between them, so six dollars each. It is not the middle value, which "
            "we call the median, and not the most common value, which we call the mode. One very large value "
            "drags this average toward itself.",
         "board": ['[[card title="mean, median, mode" items="mean — add them up and share out | median — the middle one | mode — the most common one"]]']},
        {"term": "mode", "say":
            "The **mode** of a list is the value that turns up most often. In two, three, three, seven and "
            "nine, it is three, because three appears twice while everything else appears once. Two cautions. "
            "It is the value that repeats, not the number of times it repeated, and it is not the largest value "
            "in the list. A list can also have two of them, and when nothing repeats we usually say there is "
            "none.",
         "board": ['[[dotplot data="2,3,3,7,9" caption="which value shows up more than once"]]']},
        {"term": "parabola", "say":
            "A **parabola** is the smooth U shaped curve you get when you graph a quadratic, one where the "
            "highest power of x is two. It has exactly one turning point, called the vertex, and a mirror line "
            "straight through that point, so the two arms match each other perfectly. Graphed this way, the "
            "curve opens upward when the number in front of x squared is positive, and downward when that "
            "number is negative.",
         "board": ['[[graph func="x^2" range="-4..4" yrange="-2..16" caption="one turning point, and two arms that mirror each other"]]']},
        {"term": "parallel", "say":
            "Two straight paths on the same flat surface are **parallel** when they head in the same direction "
            "and never meet, however far you follow them. For any two that are not vertical, this shows up as "
            "equal slopes, since both climb at exactly the same rate. One condition is easy to forget. Their "
            "starting heights must differ. Equal slopes with the same y intercept is not a pair at all, it is "
            "one path written down twice.",
         "board": ['[[graph lines="y=2x+1 ; y=2x-4" range="-4..4" caption="same slope, different starting height"]]']},
        {"term": "rate of change", "say":
            "A **rate of change** tells you how much one quantity moves for every single unit the other one "
            "moves. Forty miles for each hour is one of these. On a straight graph it is the slope, the rise "
            "divided by the run, so notice that it compares two changes rather than reporting just one. A "
            "straight graph carries the same value the whole way along. On a curve it shifts, so there it has "
            "to be measured across a chosen stretch.",
         "board": ['[[write text="rise 6   over   run 2      6 up for every 2 across"]]']},
        {"term": "scatter", "say":
            "A **scatter** plot is a graph where every dot stands for one pair of measurements taken from the "
            "same subject, such as one student's study hours beside that same student's test score. You are not "
            "joining the dots up. You are reading the shape of the cloud they make. If the cloud slopes upward, "
            "the two quantities tend to rise together, though that on its own does not prove one causes the "
            "other.",
         "board": ['[[scatter points="(1,2) (2,3.5) (3,5) (4,4.5) (5,7)" caption="each dot is one pair of measurements"]]']},
        {"term": "square root", "say":
            "The **square root** of a number is the number you multiply by itself to get it. Three times three "
            "is nine, so nine gives you three. Here is the fine print people trip on. The radical sign asks "
            "only for the positive one, so it hands back three and not negative three. Solving x squared equals "
            "nine is a different question, and that one has two answers, three and negative three.",
         "board": ['[[write text="√9 = 3          but          x² = 9  →  x = 3 or x = −3"]]']},
        {"term": "vertex", "say":
            "A **vertex** is a special corner point. On a shape with straight sides it is the place where two "
            "of those sides meet. On a parabola it is the single turning point, where the curve stops heading "
            "one way and starts heading the other. Whether that turning point is the lowest place or the "
            "highest depends on which way the curve opens, so do not assume it is always a minimum.",
         "board": ['[[graph func="x^2 - 4x + 1" range="-2..6" yrange="-4..6" caption="notice the one place where the curve turns around"]]']},
    ],
    "geometry": [
        {"term": "angle", "say":
            "An **angle** is the amount of turn between two lines that meet. It is not about how long the "
            "lines are — you can stretch them out forever and the angle does not change. We measure that "
            "turn in degrees, and a full spin all the way around is three hundred sixty degrees. A square "
            "corner is exactly ninety.",
         "board": ['[[angle deg="90" caption="a right angle — a square corner"]]']},
        {"term": "hypotenuse", "say":
            "In a right triangle, the side across from the square corner is called the **hypotenuse**. It "
            "is always the longest side of that triangle, and it is always the one that does not touch "
            "the right angle. Knowing which side is the hypotenuse matters, because the famous rule about "
            "right triangles treats it differently from the other two.",
         "board": ['[[triangle v="A,B,C" right="C" sides="5,3,4" caption="the hypotenuse is the side opposite the right angle"]]']},
        {"term": "bisector", "say":
            "A **bisector** is something that cuts a figure into two equal halves. A segment bisector "
            "crosses a segment at its midpoint, so the two pieces are the same length. An angle bisector "
            "splits an angle into two angles of the same size. The word comes from bi, meaning two, and "
            "sect, meaning cut. Here is the part people miss: a bisector has to make the two pieces "
            "equal. A line that just crosses a segment somewhere is not a bisector unless it hits the "
            "exact middle.",
         "board": ['[[write text="bisector = cuts a figure into two EQUAL parts"]]',
                   '[[angle deg="60" caption="an angle bisector splits 60° into 30° and 30°"]]']},
        {"term": "supplementary", "say":
            "Two angles are **supplementary** when their measures add to one hundred eighty degrees. That "
            "is a straight line's worth of turn. So when two angles sit side by side along a straight "
            "line, they are supplementary, and knowing one hands you the other instantly. Their cousins "
            "are complementary angles, which add to ninety, a square corner. Careful with one thing: "
            "supplementary angles do not have to touch. Any two angles that add to one hundred eighty are "
            "supplementary, no matter where they are drawn.",
         "board": ['[[write text="130° + 50° = 180°   →  supplementary"]]']},
        {"term": "transformation", "say":
            "A **transformation** is a rule that moves every point of a shape to a new place. Slide it, "
            "and that is a translation. Flip it across a line, and that is a reflection. Turn it around a "
            "point, and that is a rotation. Those three are called rigid motions, because the shape keeps "
            "its exact size and its exact angles — only its position changes. That is the idea to hold "
            "onto. A transformation moves a figure. It does not redraw it, and it does not resize it.",
         "board": ['[[write text="translation = slide   ·   reflection = flip   ·   rotation = turn"]]']},
        {"term": "symmetry", "say":
            "A shape has **symmetry** when a transformation leaves it looking exactly the way it looked "
            "before. Fold a butterfly down the middle and the halves match: that is line symmetry, and "
            "the fold is the line of symmetry. Spin a five pointed star by one fifth of a turn and it "
            "lands right back on itself: that is rotational symmetry. Symmetry is not about a shape being "
            "pretty or balanced. It is a strict test. After the move, could anyone tell that anything "
            "happened? If not, the shape has symmetry.",
         "board": ['[[write text="line symmetry: fold it, and the two halves match exactly"]]']},
        {"term": "congruent", "say":
            "Two figures are **congruent** when they have exactly the same size and exactly the same "
            "shape. If you could pick one up, slide it, turn it, or flip it, and lay it down perfectly on "
            "top of the other, they are congruent. That is the real definition: congruence is what "
            "survives a rigid motion. Congruent does not mean sitting in the same position. Two triangles "
            "pointing in completely different directions can still be congruent. Same side lengths, same "
            "angles, different address on the page.",
         "board": ['[[triangle v="A,B,C" angles="60,60,60" ticks="AB,BC,CA" caption="congruent copies: same sides, same angles, different position"]]']},
        {"term": "proof", "say":
            "A **proof** is an argument showing that something must be true every time, not just in the "
            "one picture you happened to draw. You start from what is already known — the given facts, "
            "the definitions, and theorems proved before this one — and you take one small step at a time "
            "until you reach the statement you wanted. Every step carries a reason. In a two column "
            "proof, statements go on the left and reasons on the right. Measuring your drawing is not a "
            "proof. A drawing is one case. A proof covers all of them.",
         "board": ['[[card title="Two-column proof" items="Statements on the left | Reasons on the right | every step needs both"]]']},
        {"term": "similar", "say":
            "Two figures are **similar** when they have the same shape but not necessarily the same size. "
            "One is a scaled copy of the other: every pair of matching angles is equal, and every pair of "
            "matching sides is in the same ratio. A photograph and its enlargement are similar. Here is "
            "the trap. Similar does not mean kind of alike. It is a strict condition — the same shape, "
            "scaled evenly. Stretch a picture wider without making it taller and it stops being similar, "
            "because the sides no longer share one ratio.",
         "board": ['[[write text="SIMILAR:  matching angles equal,  matching sides in the SAME ratio"]]']},
        {"term": "scale factor", "say":
            "The **scale factor** is the number that tells you how much a figure was enlarged or shrunk. "
            "If every side of the new figure is three times the matching old one, the scale factor is "
            "three. If every side is half as long, the scale factor is one half. You find it by dividing "
            "a new length by the length it matches. And expect this: a scale factor of three does not "
            "simply triple the area. The lengths triple, but the area grows nine times, because area "
            "covers two directions at once.",
         "board": ['[[write text="scale factor 3  →  sides ×3,  area ×9"]]']},
        {"term": "Pythagorean theorem", "say":
            "The **Pythagorean theorem** is a rule about right triangles, and only right triangles. It "
            "says a squared plus b squared equals c squared, where a and b are the two shorter sides and "
            "c is the hypotenuse, the side across from the square corner. A ladder leaning against a wall "
            "makes a right triangle with the wall and the ground, so if you know how far out the foot of "
            "the ladder sits and how long the ladder is, you can find how high it reaches. No right "
            "angle, no theorem. Check for that square corner first.",
         "board": ['[[righttriangle adj="4" opp="3" caption="3 and 4 are the legs; 5 is the hypotenuse"]]']},
        {"term": "sine", "say":
            "In a right triangle, the **sine** of an angle is a ratio: the side opposite that angle "
            "divided by the hypotenuse. That is what the S O H in SOH-CAH-TOA stands for — sine is "
            "opposite over hypotenuse. Every right triangle containing that same angle gives the same "
            "ratio, no matter how large or small the triangle is, and that is exactly why this is useful. "
            "Measure the angle up to the top of a tree and your distance from it, and trigonometry hands "
            "you the height. Sine is never a number on its own. It is always the sine of some particular "
            "angle.",
         "board": ['[[righttriangle adj="4" opp="3" theta="θ" caption="sine of θ = opposite ÷ hypotenuse = 3 ÷ 5"]]',
                   '[[write text="sin(angle) = opposite ÷ hypotenuse"]]']},
        {"term": "radius", "say":
            "The **radius** of a circle is the distance from the center out to any point on the circle. "
            "Every radius of the same circle is the same length — that sameness is what makes a circle a "
            "circle. The diameter goes all the way across through the center, so the diameter is exactly "
            "two radii. Watch for one common setup: problems love to hand you the diameter and then ask "
            "for something that needs the radius. Read carefully and cut it in half before you use it.",
         "board": ['[[circle r="5" caption="radius: center to edge — every radius is the same length"]]']},
        {"term": "arc", "say":
            "An **arc** is a piece of a circle's edge, the curved section between two points on that "
            "circle. Think of it as a slice of the crust rather than a slice of the pie. Its length "
            "depends on two things: how big the circle is, and how much of the way around it travels. Go "
            "a quarter of the way around and the arc is a quarter of the circumference. Do not mix up an "
            "arc with a chord. A chord is the straight shortcut between the same two points. The arc is "
            "the curved path.",
         "board": ['[[circle r="5" caption="arc = part of the edge   ·   chord = the straight line across"]]']},
        {"term": "slope", "say":
            "**Slope** measures steepness: how much a line rises for every step you take sideways. Rise "
            "over run. A wheelchair ramp that climbs one foot for every twelve feet forward has a slope "
            "of one twelfth. A line heading uphill from left to right has positive slope, downhill is "
            "negative, and a flat line has a slope of zero. In coordinate geometry two facts do most of "
            "the work. Parallel lines have equal slopes, and perpendicular lines have slopes that are "
            "negative reciprocals of each other.",
         "board": ['[[graph lines="y=2x+1" caption="slope 2 — up 2 for every 1 across"]]']},
        {"term": "volume", "say":
            "**Volume** is how much space a solid takes up — how much it would hold if you filled it. We "
            "measure it in cubic units, because you are really counting how many unit cubes fit inside. "
            "For a prism or a cylinder there is one shortcut: the area of the base, times the height. A "
            "cone or a pyramid with the same base and the same height holds exactly one third as much, "
            "which is worth remembering. Do not confuse volume with surface area. Surface area is the "
            "wrapping paper. Volume is what fits in the box.",
         "board": ['[[write text="prism or cylinder:   Volume = (area of base) × height"]]']},
        {"term": "probability", "say":
            "The **probability** of an event is a number saying how likely it is, somewhere from zero to "
            "one. Zero means it never happens, one means it always happens, and one half means it happens "
            "about as often as not. When every outcome is equally likely, you count the outcomes you want "
            "and divide by the total number of outcomes. Rolling a four on a fair die is one out of six. "
            "Probability promises nothing about your next roll. One out of six is what settles out over a "
            "great many rolls, not a schedule.",
         "board": ['[[pie parts="6" shaded="1" caption="six equal faces, and exactly one of them is the 4"]]']},
        # --- build fz (2026-08-14): the red-list additions. See the change note at the
        # top of this file. Appended, never edited, so no cached audio is re-billed.
        {"term": "point", "say":
            "A **point** is a single exact location. It has no width, no length and no thickness at all — the "
            "dot we draw is only there so your eye can find it. We give points capital letters so we can talk "
            "about them out loud. Everything else in geometry is built out of points: a line is made of them, "
            "and so is a circle.",
         "board": ['[[objects emoji="⬤" groups="3" caption="A, B and C — three points, three exact locations"]]']},
        {"term": "line", "say":
            "A **line** is perfectly straight and it never ends. It keeps going in both directions forever, "
            "which is why we draw small arrows on the ends. A line has no thickness and no width, only "
            "direction and position. Two points are enough to fix exactly one line, and that is why we can name "
            "a line by naming two points that sit on it.",
         "board": ['[[write text="line AB:   ←———— A ———— B ————→   it never stops"]]']},
        {"term": "segment", "say":
            "A **segment** is the part of a line between two endpoints. Unlike a line, it stops. That is what "
            "makes it something you can measure, because it has a definite length. Whenever we talk about the "
            "side of a triangle, or the distance between two points, we are really talking about a segment "
            "rather than a whole line.",
         "board": ['[[write text="segment AB:   A ———————— B        length 5"]]']},
        {"term": "right angle", "say":
            "A **right angle** is an angle of exactly ninety degrees — a square corner, like the corner of a "
            "page or a table. It is the angle every other angle gets compared to. An angle smaller than ninety "
            "is called acute, and one larger than ninety is called obtuse. On a drawing we mark a right angle "
            "with a small square instead of a curve.",
         "board": ['[[angle deg="90" caption="a right angle — ninety degrees, marked with a small square"]]']},
        {"term": "degree", "say":
            "A **degree** is the unit we measure turning in. One full spin all the way around is divided into "
            "three hundred sixty of them, so a single degree is a very small turn. A quarter turn is ninety "
            "degrees, and a half turn, which lays you out flat in a straight line, is one hundred eighty. The "
            "small raised circle written after a number means degrees.",
         "board": ['[[angle deg="90" caption="90 degrees — a quarter of a full turn"]]']},
        {"term": "complementary", "say":
            "Two angles are **complementary** when their measures add to exactly ninety degrees, filling a "
            "square corner between them. They do not have to be touching each other; only the total matters. It "
            "is the ninety degree cousin of supplementary, which adds to one hundred eighty. If you know one "
            "angle of a complementary pair, subtract it from ninety to get the other.",
         "board": ['[[angle deg="90" split="30,60" caption="thirty and sixty fill a square corner — complementary"]]']},
        {"term": "circle", "say":
            "A **circle** is every point that sits exactly the same distance from one center point. That fixed "
            "distance is the radius. Nothing about a circle is straight and it has no corners anywhere — it is "
            "defined entirely by that one rule about distance. Move the center and the circle moves with it; "
            "change the radius and it grows or shrinks.",
         "board": ['[[circle r="5" caption="every point exactly the same distance from the center"]]']},
        {"term": "diameter", "say":
            "The **diameter** of a circle is the straight distance all the way across it, passing through the "
            "center. It is the longest straight trip you can make inside a circle, and it is exactly twice the "
            "radius. So if someone hands you a diameter you can halve it to get the radius, and if they hand "
            "you a radius you can double it.",
         "board": ['[[circle r="5" caption="the diameter goes straight through the center — twice the radius"]]']},
        {"term": "chord", "say":
            "A **chord** is a straight segment whose two endpoints both sit on a circle. It cuts across the "
            "circle, but it does not have to pass through the middle. The diameter is the one special chord "
            "that does pass through the center, and that makes it the longest chord a circle has. Every other "
            "chord is shorter than the diameter.",
         "board": ['[[circle r="5" caption="a chord joins two points on the circle; the longest one is the diameter"]]']},
        {"term": "circumference", "say":
            "The **circumference** is the distance all the way around a circle — its perimeter. Because it "
            "curves the whole way, you cannot lay a straight ruler along it, so we get it from the diameter "
            "instead. The trip around is a little more than three times the trip across. That number, a little "
            "more than three, is what we call pi.",
         "board": ['[[write text="circumference   =   a little more than 3 times the diameter"]]']},
        {"term": "parallel", "say":
            "Two lines are **parallel** when they run in exactly the same direction and never meet, no matter "
            "how far you extend them. The gap between them stays the same the whole way along. On a drawing we "
            "mark parallel lines with matching arrowheads. On a graph you can spot them instantly, because "
            "parallel lines have equal slopes.",
         "board": ['[[write text="parallel:   slope 2   and   slope 2      the gap never changes"]]']},
        {"term": "perpendicular", "say":
            "Two lines are **perpendicular** when they cross at a right angle — ninety degrees, a square "
            "corner. The two edges meeting at the corner of a sheet of paper are perpendicular. On a graph "
            "there is a neat test for it: two lines are perpendicular exactly when their slopes are negative "
            "reciprocals of one another.",
         "board": ['[[angle deg="90" caption="perpendicular lines meet at a square corner"]]']},
        {"term": "negative reciprocal", "say":
            "To find the **negative reciprocal** of a number, turn it upside down and then change its sign. The "
            "negative reciprocal of two is negative one half. Multiply any number by its negative reciprocal "
            "and the answer is negative one every time. This matters in geometry because two lines meet at a "
            "right angle exactly when their slopes are negative reciprocals.",
         "board": ['[[write text="2   and   −1/2         2 × (−1/2)  =  −1"]]']},
        {"term": "midpoint", "say":
            "The **midpoint** of a segment is the point exactly halfway along it, splitting the segment into "
            "two pieces of equal length. On a coordinate grid you find it by averaging: average the two x "
            "values, then average the two y values. Think of it as the balance point, because it sits the same "
            "distance from each end.",
         "board": ['[[write text="midpoint of (2, 3) and (8, 7)   =   (5, 5)"]]']},
        {"term": "translation", "say":
            "A **translation** slides a shape to a new place without turning it and without resizing it. Every "
            "point moves the same distance in the same direction, so the shape that lands is identical to the "
            "shape that left — same side lengths, same angles, facing the same way. The only thing that changed "
            "is where it is.",
         "board": ['[[write text="translation:   every point moves 4 right and 2 up"]]']},
        {"term": "reflection", "say":
            "A **reflection** flips a shape across a line, the way a mirror would. Every point finishes the "
            "same distance from that line as it started, but on the opposite side. The shape keeps its size and "
            "all of its angles, but its orientation reverses — whatever pointed left is now pointing right.",
         "board": ['[[write text="reflection across the y-axis:   (3, 5)   →   (−3, 5)"]]']},
        {"term": "rotation", "say":
            "A **rotation** turns a shape around a fixed point by a given number of degrees. That center point "
            "stays exactly where it is and everything else swings around it. Sizes and angles do not change; "
            "only the direction the shape faces does. To describe one we say which way, clockwise or "
            "counterclockwise, and by how many degrees.",
         "board": ['[[write text="rotation 90 degrees about the origin:   (3, 5)   →   (−5, 3)"]]']},
        {"term": "rigid motion", "say":
            "A **rigid motion** is any move that changes where a shape is without changing the shape itself. "
            "Translations, reflections and rotations are all rigid motions — slide, flip and turn. Lengths and "
            "angles survive all three of them. That is exactly why they prove congruence: if a rigid motion "
            "lands one figure right on top of another, the two are the same figure.",
         "board": ['[[card title="the three rigid motions" items="translation — slide | reflection — flip | rotation — turn"]]']},
        {"term": "area", "say":
            "**Area** is how much flat surface a shape covers — the amount of room inside its boundary. We "
            "count it in squares, like square inches or square centimeters, and that is why area is always "
            "written in square units while length is not. A rectangle's area is its length times its width, "
            "because that is how many unit squares fit inside it.",
         "board": ['[[write text="rectangle 3 by 4:      area  =  12 square units"]]']},
        {"term": "surface area", "say":
            "**Surface area** is the total area of all the faces on the outside of a solid — how much wrapping "
            "paper it would take to cover the thing exactly, with none left over. You find it by working out "
            "the area of each face and adding them all up. It is measured in square units, because it is still "
            "area even though the object is solid.",
         "board": ['[[card title="a box 2 by 3 by 4" items="two faces 2 by 3 | two faces 2 by 4 | two faces 3 by 4 | add all six: 52 square units"]]']},
        {"term": "prism", "say":
            "A **prism** is a solid with two identical parallel ends and flat sides joining them up. Slice it "
            "anywhere parallel to those ends and you get the very same shape every time. A cardboard box is a "
            "rectangular prism. Its volume is the area of one end multiplied by how long the prism is from end "
            "to end.",
         "board": ['[[write text="prism volume   =   area of one end   times   length"]]']},
        {"term": "cylinder", "say":
            "A **cylinder** is a solid with two identical parallel circular ends joined by one curved surface, "
            "like a tin can. It behaves just like a prism whose ends happen to be circles, so its volume is the "
            "area of the circular end multiplied by the height. Slice it parallel to the ends and every slice "
            "is the same circle.",
         "board": ['[[write text="cylinder volume   =   area of the circle   times   height"]]']},
        {"term": "cone", "say":
            "A **cone** has one circular base and one sharp point, called the apex, with a curved surface "
            "running between them. Unlike a cylinder, its slices get smaller as you move up toward the point. "
            "Here is the surprising part worth remembering: a cone holds exactly one third of what a cylinder "
            "with the same base and height holds.",
         "board": ['[[write text="cone   =   one third of the cylinder with the same base and height"]]']},
        {"term": "pyramid", "say":
            "A **pyramid** has one flat base, often a square, and triangular faces that rise from every edge of "
            "that base to meet at a single point above it. Like a cone it tapers to a point, and it follows the "
            "same one third rule: a pyramid holds one third of what a prism with the same base and height "
            "holds.",
         "board": ['[[write text="pyramid   =   one third of the prism with the same base and height"]]']},
        {"term": "two-column proof", "say":
            "A **two-column proof** is a way of writing an argument so that every step can be checked by "
            "someone else. The left column lists what you claim, one statement at a time. The right column "
            "gives the reason that statement is allowed — a given fact, a definition, or a theorem you already "
            "know. Nothing goes in the left column without a reason beside it.",
         "board": ['[[card title="two-column proof" items="STATEMENT — what you claim | REASON — why it is allowed | every line needs both"]]']},
    ],
    "algebra2": [
        {"term": "exponent", "say":
            "An **exponent** counts how many times you multiply a number by itself. Two to the third "
            "means two times two times two. The little number is not telling you to multiply by three — "
            "it is telling you how many twos to use. That difference trips up almost everybody once, so "
            "it is worth saying out loud.",
         "board": ['[[write text="2³  =  2 × 2 × 2  =  8"]]']},
        {"term": "quadratic", "say":
            "A **quadratic** is an expression where the highest power of the variable is two — something "
            "with an x squared in it. That one detail changes everything: instead of a straight line, its "
            "graph is a curve called a parabola, and instead of one solution, it usually has two.",
         "board": ['[[write text="x² − 3x − 10 = 0     (highest power is 2)"]]']},
        {"term": "function notation", "say":
            "**Function notation** is the letter-with-parentheses way of writing a rule, and it is read "
            "out loud as f of x. Never as f times x. Nothing is multiplied. The letter names the rule and "
            "whatever sits in the parentheses is what you are feeding it, so f of two means hand a two to "
            "the rule f and see what comes back. Because the letter is just a name, a problem with two "
            "rules in it will call the second one g, and one built out of the other might be called h. "
            "Same idea every time, only the name changes.",
         "board": ['[[write text="f(x)   ←  read aloud: “f of x”     (never f times x)"]]',
                   '[[write text="f(2) = 9   means: input 2 into the rule f, output 9"]]',
                   '[[card title="different name, same idea" items="f(x) | g(x) | h(x) — all read “… of x”"]]']},
        {"term": "absolute value", "say":
            "The **absolute value** of a number is its distance from zero, and a distance is never "
            "negative. So the absolute value of negative seven is seven, and the absolute value of seven "
            "is also seven. Both of them sit seven units away from zero, just on opposite sides. That "
            "distance idea is why absolute value equations usually have two answers: two different "
            "numbers can be the same distance from zero. Absolute value is not a rule about dropping a "
            "minus sign. Think distance, and the two answers stop being a surprise.",
         "board": ['[[numberline min="-8" max="8" points="-7,7" caption="both are 7 units from zero"]]',
                   '[[write text="|−7| = 7        |7| = 7        (both are 7 away from 0)"]]']},
        {"term": "system of equations", "say":
            "A **system of equations** is two or more equations that must all be true at the same time, "
            "about the same unknowns. Its solution is the set of values that satisfies every one of them "
            "at once. With two lines on a graph, that is the point where they cross. Picture buying "
            "tickets: one equation counts how many tickets, another counts the total money spent. Either "
            "equation alone leaves many possibilities. Together they usually pin it down to one. Solving "
            "a system means satisfying all of them, not just the one you like best.",
         "board": ['[[graph lines="y=2x+1 ; y=-x+4" range="-3..5" yrange="-4..8" caption="the solution of a system is the point where the lines cross"]]']},
        {"term": "vertex", "say":
            "The **vertex** of a parabola is its turning point — the very bottom of a curve that opens "
            "upward, or the very top of one that opens downward. It matters because it answers the "
            "questions people actually ask: the lowest cost, the largest profit, the highest point a "
            "thrown ball reaches. Vertex form of a quadratic shows it to you directly, which is the "
            "entire reason that form exists. Every parabola has exactly one vertex, and it sits on the "
            "axis of symmetry, the mirror line running down the middle of the curve.",
         "board": ['[[graph parabola="y=x^2-4x+1" caption="the vertex is the turning point"]]']},
        {"term": "discriminant", "say":
            "The **discriminant** is the piece of the quadratic formula sitting under the square root "
            "sign: b squared minus four a c. On its own it tells you how many real solutions a quadratic "
            "has, before you finish solving anything. Positive means two real solutions, and the parabola "
            "crosses the horizontal axis twice. Zero means exactly one solution, and the curve just "
            "touches the axis. Negative means no real solutions at all — the answers are complex numbers, "
            "and the curve never reaches the axis.",
         "board": ['[[write text="discriminant = b² − 4ac      +→2 roots   0→1 root   −→none real"]]']},
        {"term": "imaginary number", "say":
            "An **imaginary number** is what you get from the square root of a negative number. No real "
            "number multiplied by itself gives negative one, so mathematicians defined one and named it "
            "i. That is the whole move: i is the number whose square is negative one. Imaginary is a "
            "terrible name, because these are not fake and they are not useless — they describe real "
            "electrical current and real waves every day. Add a real number to an imaginary one, like "
            "three plus two i, and you have a complex number.",
         "board": ['[[write text="i = √(−1)        so  i² = −1        3 + 2i  is complex"]]']},
        {"term": "polynomial", "say":
            "A **polynomial** is a sum of terms, where each term is a number multiplied by a variable "
            "raised to a whole number power. Three x cubed minus five x plus two is one. The degree is "
            "the highest power in it, and the degree tells you a great deal before you do any work: at "
            "most how many solutions to expect, and which way the two ends of the graph head. One rule "
            "keeps the family clean. No variable in a denominator and no variable under a root sign — "
            "those belong to other families.",
         "board": ['[[write text="3x³ − 5x + 2      degree 3  →  at most 3 zeros"]]']},
        {"term": "asymptote", "say":
            "An **asymptote** is a line that a graph moves closer and closer to but never actually "
            "reaches. A rational function has a vertical asymptote wherever the denominator would be "
            "zero, because dividing by zero is not allowed and the graph races away as it nears that "
            "spot. It can also have a horizontal asymptote, showing where the function settles once the "
            "inputs get enormous. Nothing is blocking the graph there. It is simply approaching, forever, "
            "without ever arriving.",
         "board": ['[[write text="denominator = 0   →   vertical asymptote there"]]']},
        {"term": "extraneous solution", "say":
            "An **extraneous solution** is an answer that shows up in your work but does not actually "
            "solve the equation you started with. It appears when you use a step that cannot be undone — "
            "squaring both sides, or multiplying away a denominator. Those moves can invent answers that "
            "were never really there. So radical and rational equations come with a rule attached: check "
            "every answer in the original equation. Any answer that makes a denominator zero, or asks a "
            "square root to come out negative, gets thrown out.",
         "board": ['[[card title="These steps can invent answers" items="squaring both sides | clearing denominators | so CHECK in the original"]]']},
        {"term": "radical", "say":
            "A **radical** is a root — the square root sign and all its relatives. The square root of "
            "nine is three, because three times three is nine. The small number tucked into the notch is "
            "called the index, and it says which root you want: a three there means the cube root, the "
            "number you multiply by itself three times to get back. Here is what trips people. The root "
            "of a sum is not the sum of the roots. Finish what is under the sign first, then take the "
            "root of that.",
         "board": ['[[write text="√9 = 3        ∛8 = 2        √(9+16) = 5,  NOT 3 + 4"]]']},
        {"term": "rational exponent", "say":
            "A **rational exponent** is a fraction written where an exponent goes, and it means a root. X "
            "to the one half is the square root of x. X to the one third is the cube root of x. The "
            "bottom of the fraction picks which root, and the top is a power you apply as well, so x to "
            "the two thirds is the cube root of x, then squared. This is not a new rule bolted onto the "
            "old ones. It is defined this way precisely so every exponent law you already know keeps "
            "working for roots too.",
         "board": ['[[write text="x^(1/2) = √x        x^(2/3) = (∛x)²"]]']},
        {"term": "logarithm", "say":
            "A **logarithm** answers exactly one question: what power do I raise this base to, in order "
            "to get that number? The log base two of eight is three, because two to the third power is "
            "eight. That is all a logarithm is — an exponent, pulled out into the open where you can "
            "solve for it. Logarithms are the undo button for exponentials, which is why they appear "
            "whenever the unknown is stuck up in an exponent, like asking how many years an investment "
            "needs in order to double.",
         "board": ['[[write text="log₂ 8 = 3      means      2³ = 8"]]']},
        {"term": "exponential growth", "say":
            "**Exponential growth** happens when a quantity multiplies by the same factor over and over, "
            "instead of adding the same amount over and over. Money earning five percent a year grows "
            "exponentially. So does a bacteria population that doubles every hour. The difference matters "
            "more than it first sounds. Adding ten every year builds a straight line you can see coming. "
            "Multiplying by two every year starts slowly, looks harmless for a while, and then climbs so "
            "steeply it leaves every straight line far behind.",
         "board": ['[[write text="linear: +10 each year   ·   exponential: ×2 each year"]]']},
        {"term": "sequence", "say":
            "A **sequence** is an ordered list of numbers, and each number in it is called a term. Two "
            "kinds come up constantly. An arithmetic sequence adds the same amount at every step — two, "
            "five, eight, eleven, adding three each time. A geometric sequence multiplies by the same "
            "amount at every step — three, six, twelve, twenty four, doubling each time. So the first "
            "thing to do with any sequence is decide which it is. Is the difference constant, or is the "
            "ratio constant? That one question picks your formula.",
         "board": ['[[write text="arithmetic:  2, 5, 8, 11  (+3)        geometric:  3, 6, 12, 24  (×2)"]]']},
        {"term": "subscript", "say":
            "A small number written low and tight against a letter is a **subscript**, and you read it "
            "out loud as sub. So a with a little one after it is said a sub one. It does not mean a "
            "multiplied by one. Nothing is being multiplied. A subscript is a LABEL: it tells you which "
            "one of a whole family of numbers you mean. a sub one, a sub two, a sub three, and a sub n "
            "for whichever one sits in position n. The letter names the family, and the subscript picks "
            "out the member you want.",
         "board": ['[[write text="a₁ , a₂ , a₃ , … , aₙ    ←  “a sub one, a sub two, … a sub n”"]]',
                   '[[write text="aₙ is a LABEL for one term — it is NOT a · n"]]']},
        {"term": "unit circle", "say":
            "The **unit circle** is the circle with radius one, centered at the origin, and it is the "
            "reference map for all of trigonometry. Pick an angle, start at the right side and turn "
            "counterclockwise, and the point where you land has coordinates that are exactly the cosine "
            "and the sine of that angle. Cosine first, sine second. That is also why sine and cosine "
            "never get bigger than one or smaller than negative one. You are reading off a circle of "
            "radius one, so there is nowhere further to go.",
         "board": ['[[unitcircle caption="radius 1 — every point on it is (cos θ, sin θ)"]]']},
        {"term": "z-score", "say":
            "A **z-score** tells you how many standard deviations a value sits above or below the mean. A "
            "z-score of two means the value is two standard deviations above average. Negative one and a "
            "half means one and a half below it. What makes this powerful is that it converts any "
            "measurement onto the same neutral scale, so a test score and a height can finally be "
            "compared fairly. And when the data follow a normal model, that bell shaped curve, a z-score "
            "also tells you roughly what fraction of everyone you are ahead of.",
         "board": ['[[write text="z = (value − mean) ÷ standard deviation"]]']},
        # --- build gc (2026-08-14): red-list additions for this course. See the
        # change note at the top of this file. Appended, never edited.
        {"term": "complex number", "say":
            "A **complex number** has two parts joined together: an ordinary real part, and an imaginary part "
            "built from i, the number whose square is negative one. Three plus two i is one of them. Here is "
            "what trips people. Those two parts never merge into a single term. Three plus two i stays exactly "
            "as it is written, because a real quantity and an imaginary one cannot be added into one. You "
            "combine real with real, and imaginary with imaginary.",
         "board": ['[[write text="3 + 2i        real part: 3        imaginary part: 2i"]]']},
        {"term": "cosine", "say":
            "In a right triangle, the **cosine** of an angle is the length of the side next to that angle, the "
            "one that is not the hypotenuse, divided by the hypotenuse. It is a ratio, so it comes out as a "
            "plain number with no units on it. Here is the trap. Writing this ratio in front of an angle does "
            "not mean anything is being multiplied by that angle. It names an operation you perform on the "
            "angle, the way a square root sign names one.",
         "board": ['[[righttriangle adj="4" opp="3" theta="θ" caption="which leg sits next to θ, and which one is across from it"]]']},
        {"term": "cube root", "say":
            "The **cube root** of a number is the value you multiply by itself three times to get back to that "
            "number. Two times two times two is eight, so eight gives you two. Notice one difference that "
            "matters. Unlike the square root sign, this one is perfectly happy with a negative number "
            "underneath, because negative two times negative two times negative two is negative eight. Nothing "
            "is undefined there, and no imaginary unit is needed.",
         "board": ['[[write text="∛8 = 2            ∛(−8) = −2"]]']},
        {"term": "degree", "say":
            "The **degree** of a polynomial in one variable is the highest power that variable is raised to. In "
            "three x cubed minus five x plus two, it is three. Careful here. It is not how many terms the "
            "expression has, and it is not the number sitting out in front. Look only at the exponents and take "
            "the biggest one. That single number tells you a great deal before you do any work, including at "
            "most how many times the graph can cross the horizontal axis.",
         "board": ['[[write text="3x³ − 5x + 2        highest exponent: 3"]]']},
        {"term": "factor", "say":
            "A **factor** is one of the pieces that get multiplied together. Since x squared minus five x plus "
            "six can be rewritten as x minus two, times x minus three, each of those two pieces is one of them. "
            "Here is the confusion worth naming. A term is something you add, while this is something you "
            "multiply. And it is a whole expression, not a value for x. The number two, which makes that "
            "expression come out zero, is a related but different thing.",
         "board": ['[[write text="x² − 5x + 6   =   (x − 2)(x − 3)"]]', '[[card title="factor, zero, root" items="factor — a piece it multiplies into | zero — an x that makes it 0 | root — the same x, named from the equation"]]']},
        {"term": "hole", "say":
            "A rational function has a **hole** at an x value when the same factor sits on the top and the "
            "bottom, and cancelling clears it out of the bottom completely. That input was never allowed, "
            "because it made the original denominator zero, so the graph is missing exactly one point there and "
            "carries on as normal either side of it. Do not confuse this with a vertical asymptote. There the "
            "curve races away without bound.",
         "board": ['[[write text="(x² − 4) / (x − 2)  =  x + 2   for every x except 2"]]', '[[graph func="x+2" hole="2" range="-3..6" yrange="-2..9" caption="ordinary everywhere except one missing point"]]']},
        {"term": "mean", "say":
            "The **mean** is the average you get by adding up every value and then splitting the total evenly "
            "among however many values there are. Think of it as the balance point of the data. Here is the "
            "thing to watch for. One extreme value drags it, because every value pulls on that total. A single "
            "enormous salary can lift the average of a whole office above what almost anybody there actually "
            "earns, which is why the median is so often reported beside it.",
         "board": ['[[dotplot data="4,5,5,6,20" caption="four values bunched, one far out"]]']},
        {"term": "parabola", "say":
            "A **parabola** is the curve you get when you graph a quadratic, a rule whose highest power is two. "
            "It has exactly one turning point, and a mirror line running straight through it, so the two sides "
            "match. Careful here. That mirror line is only the vertical axis in the simplest cases. Add an x "
            "term and the whole curve slides sideways, mirror line and all, so never assume the turning point "
            "sits on the vertical axis.",
         "board": ['[[graph func="x^2-4x+1" range="-2..6" yrange="-4..6" caption="the mirror line here is not the vertical axis"]]']},
        {"term": "rational equation", "say":
            "A **rational equation** is an equation with the variable down in a denominator. You solve one by "
            "multiplying every term by the common denominator, which clears the fractions, and then solving "
            "whatever is left. Here is the step nobody may skip. Multiplying a denominator away can invent an "
            "answer that never worked in the first place, so any answer that would make a denominator zero has "
            "to be thrown out. Check each one in the original.",
         "board": ['[[write text="1/x + 1/2 = 3/4     multiply by 4x      4 + 2x = 3x"]]']},
        {"term": "rational function", "say":
            "A **rational function** is one polynomial divided by another. The word comes from ratio, not from "
            "being reasonable. Everything interesting on its graph happens where the bottom would be zero, "
            "because dividing by zero is not allowed, so those inputs are missing from the domain. What you see "
            "at such an input depends on the top as well. If that factor cancels right out of the bottom, you "
            "get one missing point. If any of it is left down there, you get a vertical asymptote.",
         "board": ['[[graph func="1/(x-2)" range="-4..8" yrange="-6..6" caption="watch the curve as x closes in on 2 from each side"]]']},
        {"term": "roots", "say":
            "The **roots** of an equation are the values of the variable that make the equation true. Set x "
            "squared minus five x plus six equal to zero, and two and three are what you are hunting for. One "
            "thing to keep straight. This same word also names the square root operation, which is a completely "
            "different idea. Here it is a solution, and it earns the name from the equation you were handed, "
            "not from any radical sign.",
         "board": ['[[write text="x² − 5x + 6 = 0        solutions:  x = 2  and  x = 3"]]']},
        {"term": "sine", "say":
            "In a right triangle, the **sine** of an angle is the side across from that angle divided by the "
            "hypotenuse. Here is the part that makes it so useful. It depends only on the angle, never on how "
            "big the triangle is. Shrink the triangle to half its size and both of those lengths halve, so the "
            "ratio is unchanged. And because the hypotenuse is always the longest side, this ratio can never "
            "come out larger than one.",
         "board": ['[[righttriangle adj="4" opp="3" theta="θ" caption="which side is across from θ, and which is the longest"]]']},
        {"term": "square root", "say":
            "The **square root** of a number is the value that, multiplied by itself, gives that number back. "
            "Three times three is nine, so nine gives you three. Here is the fine point people miss. The "
            "radical sign on its own asks for the positive value only, so it hands back three and not negative "
            "three. It is when you solve an equation such as x squared equals nine that both three and negative "
            "three are answers, and you write the plus or minus in yourself.",
         "board": ['[[write text="√9 = 3          but          x² = 9   →   x = 3  or  x = −3"]]']},
        {"term": "square root of a negative", "say":
            "Ask for the **square root of a negative** and no real number can answer, because any real number "
            "multiplied by itself comes out positive or zero. So we write the answer using i, the number whose "
            "square is negative one. Negative nine under the sign becomes three i. Do that conversion first, "
            "every time. If you multiply two of them while they are still sitting under the radical sign, the "
            "usual rule breaks down and the sign of your answer comes out wrong.",
         "board": ['[[write text="√(−9) = 3i          √(−4)·√(−9) = 2i · 3i = −6"]]']},
        {"term": "standard deviation", "say":
            "The **standard deviation** is one number telling you how far a typical value sits from the "
            "average. Small, and the data huddle close together. Large, and they are spread widely apart. It is "
            "measured in the same units as the data itself, so heights in inches give an answer in inches. "
            "Careful here. It is not the gap between the smallest and the largest value, and a single far away "
            "outlier can inflate it well past what most of the data are doing.",
         "board": ['[[dotplot data="4,5,5,5,6" caption="bunched tightly: small standard deviation"]]']},
        {"term": "trig", "say":
            "Everybody shortens the name of this subject to **trig**. It is the branch of mathematics that "
            "links the angles of a triangle to the lengths of its sides. Three ratios do almost all of the "
            "work: sine, cosine and tangent, each one comparing two sides of a right triangle. Here is what "
            "surprises people. It is not only about triangles. Those same ratios describe things that go round "
            "and repeat, like a wave or a turning wheel, which is why they follow you well past this course.",
         "board": ['[[card title="the three ratios" items="sine — opposite over hypotenuse | cosine — adjacent over hypotenuse | tangent — opposite over adjacent"]]']},
        {"term": "zeros", "say":
            "The **zeros** of a function are the input values that make its output come out zero. On a graph, "
            "the real ones are exactly where the curve meets the horizontal axis. Two things to keep straight. "
            "A zero is an x value, not a point on the curve and not a height. And a zero is a number, while a "
            "factor such as x minus two is an expression. The factor is what you multiply by, and the number "
            "two is the zero it hands you.",
         "board": ['[[graph func="x^2-5x+6" range="-1..5" yrange="-3..7" caption="look at where the curve meets the horizontal axis"]]']},
    ],
    "precalc": [
        {"term": "function", "say":
            "A **function** is a rule that takes one input and gives back exactly one output. The exactly "
            "one part is the whole definition — put in a three and you always get the same answer out, "
            "every time. We write it with the letter f and the input tucked inside parentheses, and you "
            "say the whole thing out loud as f of x. It simply means the output of the rule f when the "
            "input is x. It is not f multiplied by x.",
         "board": ['[[machine input="3" rule="2x+1" output="7" fname="f" caption="one input goes in, exactly one output comes out"]]']},
        {"term": "function notation", "say":
            "**Function notation** is worth slowing down for, because you will read it thousands of times "
            "from here on. The letter names the rule, the parentheses hold the input, and you say the "
            "whole thing out loud as f of x. Never f times x. Nothing is multiplied. What f of x actually "
            "IS, is the OUTPUT: the number that comes back when you feed x to the rule f. So f of two is "
            "a value, not an instruction. And since the letter is only a name, g of x and h of x are read "
            "the same way and mean the same kind of thing, with a different rule doing the work.",
         "board": ['[[write text="f(x)   ←  read aloud: “f of x”     (NOT f times x)"]]',
                   '[[write text="f(x) is the OUTPUT — the value the rule f gives back for the input x"]]',
                   '[[card title="reading them aloud" items="f(x) — “f of x” | g(x) — “g of x” | f(g(x)) — “f of g of x”"]]']},
        {"term": "radian", "say":
            "A **radian** is just another unit for measuring angles, the way inches and centimetres both "
            "measure length. Instead of chopping the circle into three hundred sixty pieces, radians "
            "measure the angle by how far you travel around the circle itself. A full trip around is two "
            "pi radians, so half a trip is pi.",
         "board": ['[[write text="full circle = 360°  =  2π radians"]]']},
        {"term": "asymptote", "say":
            "An **asymptote** is a line that a graph creeps toward but never actually touches. Picture a "
            "curve sliding along beside a wall, getting nearer and nearer, closing the gap forever "
            "without ever landing on it. Some asymptotes are vertical, where the function blows up "
            "because you are dividing by something shrinking to zero. Others are horizontal, describing "
            "where the curve settles as x runs far out to the right or far out to the left. Here is the "
            "trap. An asymptote is not part of the graph. It is a guide line you draw dashed, a "
            "description of where the curve is headed, not a piece of the curve itself.",
         "board": ['[[graph func="1/x" range="-6..6" yrange="-6..6" caption="the curve approaches the axes but never touches them"]]',
                   '[[write text="asymptote = guide line, drawn dashed, NOT part of the curve"]]']},
        {"term": "composition", "say":
            "**Composition** of functions means feeding the output of one function straight into another "
            "one. If you have a machine that doubles a number and a machine that adds three, composition "
            "is running your number through the first machine and then dropping whatever comes out into "
            "the second. You write it as f of g of x, and you always work from the inside out. Do the "
            "inner function first, then hand that answer to the outer one. Careful with one thing. Order "
            "matters here. f of g of x and g of f of x usually give completely different answers, so "
            "composition is nothing like multiplying.",
         "board": ['[[write text="(f o g)(x) = f(g(x))  —  inside first, then outside"]]',
                   '[[card title="Composition" items="g runs first | f runs on that output | order matters"]]']},
        {"term": "inverse function", "say":
            "An **inverse function** undoes whatever the original function did. If a function takes three "
            "and sends it to ten, the inverse takes ten and sends it right back to three. Every input and "
            "output swaps places, which is why the graph of an inverse is the mirror image of the "
            "original across the diagonal line y equals x. Here is the trap. Not every function has an "
            "inverse. If two different inputs land on the very same output, the inverse would not know "
            "which one to send back, so only functions that pass the horizontal line test can be undone "
            "this way.",
         "board": ['[[graph func="x^2 ; sqrt(x)" lines="y=x" range="0..6" yrange="0..6" caption="a function and its inverse are mirror images across the line y = x"]]',
                   '[[write text="inverse: swap x and y, then solve for y"]]']},
        {"term": "end behavior", "say":
            "**End behavior** describes what a graph does way out at the far edges, when x runs off "
            "toward positive infinity on the right and negative infinity on the left. You are not asking "
            "about the wiggles in the middle. You are asking whether the two arms of the curve rise, "
            "fall, or flatten out. For a polynomial only two things decide this: the degree, whether it "
            "is even or odd, and the sign of the leading coefficient. Careful with one thing. The middle "
            "terms feel important because they control all the bumps, but way out at the extremes the "
            "leading term takes over completely and everything else stops mattering.",
         "board": ['[[graph func="x^3" range="-4..4" yrange="-30..30" caption="odd degree, positive lead: down on the left, up on the right"]]',
                   '[[write text="end behavior = degree (even or odd) + sign of the leading coefficient"]]']},
        {"term": "natural log", "say":
            "The **natural log** is the logarithm that uses the special number e, roughly two point seven "
            "one eight, as its base. Asking for the natural log of a number means asking one single "
            "question: what power do I raise e to in order to get this number. It shows up everywhere "
            "because e is the rate of anything growing continuously, like money compounding every instant "
            "or a population reproducing without pause. Here is the trap. Students see the two letters "
            "and read them as a variable being multiplied by something. They are not. It is one "
            "operation, one instruction, exactly the way square root is one instruction.",
         "board": ['[[write text="ln x = log base e of x, where e is about 2.718"]]',
                   '[[card title="Natural log" items="ln e = 1 | ln 1 = 0 | ln undoes e to the x"]]']},
        {"term": "reference angle", "say":
            "A **reference angle** is the small, friendly angle between your terminal side and the "
            "horizontal axis. No matter how far around the circle you swing, you can always fold the "
            "problem back to an acute angle sitting snugly against the x axis, and that little angle "
            "carries all the numerical information. The full angle only tells you which quadrant you "
            "landed in, and the quadrant tells you the sign. Careful with one thing. A reference angle is "
            "always measured to the horizontal axis, never to the vertical one, and it is always positive "
            "and always smaller than a right angle.",
         "board": ['[[unitcircle caption="radius 1 — every point on it is (cos θ, sin θ)"]]',
                   '[[write text="reference angle: acute angle to the x-axis; the quadrant supplies the sign"]]']},
        {"term": "amplitude", "say":
            "The **amplitude** of a sine or cosine wave is how tall it swings, measured from the middle "
            "line up to the peak. If a wave rises three units above its center and dips three units "
            "below, the amplitude is three, not six. Think of it as the reach of the wave in one "
            "direction from home base. In a formula, the amplitude is the absolute value of the number "
            "sitting in front of the sine or cosine. Careful with one thing. Amplitude is a distance, so "
            "it is never negative. A minus sign out front flips the wave upside down, but it never "
            "shrinks the amplitude below zero.",
         "board": ['[[graph func="3*sin(x)" range="-6.5..6.5" yrange="-4..4" caption="amplitude 3: midline to peak, not peak to trough"]]',
                   '[[write text="amplitude = |a| in y = a·sin(x); always positive"]]']},
        {"term": "period", "say":
            "The **period** of a trig function is how far you travel along the x axis before the wave "
            "finishes one complete cycle and starts repeating itself exactly. Plain sine and plain cosine "
            "take two pi radians to make one full trip around the circle and land back where they began. "
            "Tangent is different. It repeats after only pi radians. When a number multiplies x inside "
            "the function, it squeezes or stretches that cycle horizontally. Careful with one thing. A "
            "bigger number inside makes the period shorter, not longer, because the wave is racing "
            "through its cycle faster.",
         "board": ['[[graph func="sin(x)" range="-6.5..6.5" yrange="-2..2" caption="one full cycle of sine takes 2 pi"]]',
                   '[[write text="period of sin and cos = 2π/|b| ; period of tan = π/|b|"]]']},
        {"term": "identity", "say":
            "An **identity** is an equation that is true for every value you are allowed to plug in, not "
            "just for a few special ones. When you solve an ordinary equation you are hunting for the "
            "handful of x values that make it work. An identity never needs hunting, because it works "
            "every single time. Sine squared plus cosine squared always makes one, no matter which angle "
            "you choose. Here is the trap. Verifying an identity is not solving. You are not allowed to "
            "move terms across the equals sign as if you were balancing. You work on one side alone and "
            "transform it until it matches the other.",
         "board": ['[[write text="sin²θ + cos²θ = 1   (true for every θ)"]]',
                   '[[card title="Verifying" items="work one side only | never move terms across | transform until it matches"]]']},
        {"term": "vector", "say":
            "A **vector** is a quantity that carries two pieces of information at once: how much, and "
            "which way. Speed alone is just a number, but velocity is a vector, because it tells you "
            "sixty miles per hour heading north. You draw one as an arrow, where the length is the size, "
            "called the magnitude, and the way the arrow points is the direction. Two vectors count as "
            "the same if they have the same length and the same direction, even sitting in different "
            "places on the page. Careful with one thing. You cannot add vectors by adding their lengths. "
            "You add them tip to tail, or piece by piece.",
         "board": ['[[vector v="4,3" caption="magnitude 5, pointing up and to the right"]]',
                   '[[write text="vector = magnitude + direction; add tip-to-tail or component by component"]]']},
        {"term": "ellipse", "say":
            "An **ellipse** is a stretched circle, the shape you get when you slice a cone at a gentle "
            "slant. Here is the definition that actually matters. Pick two special points inside, called "
            "the foci. An ellipse is every point where the distance to one focus plus the distance to the "
            "other adds up to the same fixed total. Loop a string around two tacks, pull it taut with a "
            "pencil, and the curve you trace is an ellipse. Careful with one thing. The foci are not the "
            "center. They sit on the long axis, one on each side of the center, and the more stretched "
            "the shape, the farther apart they slide.",
         "board": ['[[conic type="ellipse" a="5" b="3" caption="two foci: distances to them always add to the same total"]]',
                   '[[write text="ellipse: x²/a² + y²/b² = 1"]]']},
        {"term": "polar coordinates", "say":
            "**Polar coordinates** locate a point by answering two questions: how far out from the "
            "center, and at what angle. Instead of walking so many blocks east and then so many blocks "
            "north, you spin to face a direction and walk straight out. The distance is called r and the "
            "angle is called theta. Circles and spirals, which look messy in the usual grid, become "
            "beautifully simple in polar form. Careful with one thing. A single point has infinitely many "
            "polar names, because you can add a full turn to the angle and land in exactly the same spot. "
            "That never happens with ordinary coordinates.",
         "board": ['[[circle r="1" caption="go out a distance r, then rotate through angle θ"]]',
                   '[[write text="polar: (r, θ)  instead of  (x, y)"]]']},
        {"term": "sigma notation", "say":
            "**Sigma notation** is shorthand for adding up a long list of terms without writing every one "
            "of them out. The big Greek letter sigma means add them all. Underneath it you write where "
            "the counter starts, on top you write where it stops, and beside it you write the recipe for "
            "each term. So the notation is telling you to plug in each counter value, one at a time, and "
            "total the results. Careful with one thing. Sigma is not a number and it is not something you "
            "multiply by. It is an instruction, a command to sum, so you cannot cancel it or slide it "
            "around like a factor.",
         "board": ['[[write text="Σ (k=1 to 5) of 2k  =  2+4+6+8+10  =  30"]]',
                   '[[card title="Reading sigma" items="bottom: where the counter starts | top: where it stops | right: the recipe"]]']},
        {"term": "limit", "say":
            "A **limit** asks a careful question. As x sneaks closer and closer to some number, where is "
            "the function heading. Notice what it does not ask. It does not care what happens exactly at "
            "that point. The function might have a hole sitting there, or a completely different value "
            "plopped down, and the limit ignores all of it. You are watching the approach, not the "
            "arrival. Here is the trap. Students want to plug the number straight in, and often that "
            "works fine, but the whole reason limits exist is for the cases where plugging in fails and "
            "the graph still clearly aims at a value.",
         "board": ['[[graph func="x+1" hole="1" range="-3..5" yrange="-2..6" caption="a hole at x = 1, yet the graph clearly heads toward 2"]]',
                   '[[write text="limit: where the function is HEADED, not where it lands"]]']},
        {"term": "continuity", "say":
            "**Continuity** means you can draw a function through a point without lifting your pencil off "
            "the paper. No holes, no jumps, no sudden leaps to a new height. To be continuous at a spot, "
            "three things all have to line up: the function has to actually be defined there, the limit "
            "has to exist there, and those two values have to agree with each other. Careful with one "
            "thing. A graph can look almost perfect and still fail. One single missing point, one tiny "
            "hole you can barely see, breaks continuity at that x value even though the curve is smooth "
            "everywhere else.",
         "board": ['[[write text="continuous at a:  f(a) exists,  limit exists,  and they are equal"]]',
                   '[[graph func="x^2" range="-4..4" yrange="-1..16" caption="smooth and unbroken: no lifting the pencil"]]']},
        # --- build gc (2026-08-14): red-list additions for this course. See the
        # change note at the top of this file. Appended, never edited.
        {"term": "approaches", "say":
            "When we say a quantity **approaches** a number, we are describing a journey, not an arrival. The "
            "values get as close to that number as you could ask for, and the question is where they are "
            "headed, not whether they ever land. That distinction is the whole reason the word exists. The "
            "function may do something completely different at the target value, or may not even be defined "
            "there, and none of that changes where the values were heading.",
         "board": ['[[graph func="x+2" hole="2" range="-2..6" yrange="-2..9" caption="nothing sits at x = 2, yet the values still head somewhere"]]']},
        {"term": "compound", "say":
            "In **compound** interest, the interest you earn is added to the balance, and from then on it earns "
            "interest too. Simple interest pays only on the original amount, so it grows in a straight line. "
            "Here the balance multiplies by the same factor each period, so the growth curves upward. One "
            "detail decides the arithmetic: how many times a year the interest gets added. Divide the yearly "
            "rate by that count, add one to it, and raise what you get to the total number of periods.",
         "board": ['[[write text="A = P(1 + r/n)^(nt)        n = how many times a year interest is added"]]']},
        {"term": "conic", "say":
            "A **conic** section is any curve you get by slicing a double cone with a flat plane. Change the "
            "tilt and you get a circle, an ellipse, a parabola or a hyperbola. They look like four unrelated "
            "shapes, but they are one family, and each has an equation whose highest power is two. Here is a "
            "trap worth naming now. A hyperbola is not two parabolas back to back. Its branches straighten out "
            "toward asymptotes, which parabolas never do.",
         "board": ['[[conic type="hyperbola" a="3" b="2" caption="the dashed guide lines the two branches straighten toward"]]']},
        {"term": "continuous", "say":
            "A function is **continuous** across an interval when its graph runs through that whole stretch "
            "unbroken: no gaps, no missing points, no sudden jump to a new height. Here is the distinction "
            "students blur. Unbroken does not have to be smooth. The absolute value graph has a sharp corner at "
            "zero and it is still perfectly unbroken there, because your pencil never leaves the paper. Corners "
            "are allowed. Breaks are not.",
         "board": ['[[graph func="abs(x)" range="-4..4" yrange="-1..4" caption="a sharp corner, yet the pencil never leaves the paper"]]']},
        {"term": "cosine", "say":
            "On the unit circle, the **cosine** of an angle is the first coordinate of the point you reach when "
            "you start at the far right and turn through that angle. The right triangle version only handled "
            "angles smaller than a right angle. This one handles every angle, turning either way, past a full "
            "revolution and beyond. It also explains the negative values: in the second and third quadrants the "
            "point has simply crossed to the left of the vertical axis.",
         "board": ['[[unitcircle angle="135" caption="read the first coordinate, and notice its sign out here"]]']},
        {"term": "degree", "say":
            "A **degree** is a unit for measuring angles, defined as one three hundred sixtieth of a full turn. "
            "That count is a historical choice, not a mathematical one, and it is the whole reason radians "
            "exist alongside it. A radian is defined by the circle itself, so calculus comes out clean in "
            "radians and cluttered in the older unit. Careful here. A calculator gives different answers for "
            "the same trig entry depending on which mode it is in, so check the mode before you trust a value.",
         "board": ['[[write text="360° = 2π rad          90° = π/2 rad          1 rad ≈ 57.3°"]]']},
        {"term": "foci", "say":
            "The two special points that define an ellipse or a hyperbola are its **foci**, and a single one of "
            "them is called a focus. For an ellipse, the distances from any point on the curve to the two of "
            "them always add to the same total. For a hyperbola, it is the difference of those two distances "
            "that stays constant. Careful here. Neither point ever sits on the curve, and neither one is the "
            "centre. Both lie on the main axis, one either side of it.",
         "board": ['[[conic type="ellipse" a="5" b="3" caption="two foci: distances to them always add to the same total"]]']},
        {"term": "focus", "say":
            "A parabola is built from one special point, called its **focus**, together with a line called the "
            "directrix. Every point on the curve is exactly as far from that point as it is from that line, and "
            "that single property generates the entire shape. It is why a satellite dish works: signals "
            "arriving straight on all bounce to the same spot. Careful here. The point sits inside the curve, "
            "along the axis of symmetry, and it never lies on the parabola itself.",
         "board": ['[[write text="y = x²      focus: (0, ¼)      directrix:  y = −¼"]]']},
        {"term": "logarithm", "say":
            "A **logarithm** is the inverse of an exponential. It takes a number and hands back the power the "
            "base had to be raised to in order to produce it. Because a positive base raised to any power stays "
            "positive, only positive inputs are allowed, and that is exactly where the vertical asymptote comes "
            "from. Here is the error to guard against. The log of a sum is not the sum of the logs. The laws "
            "turn products into sums, never sums into sums.",
         "board": ['[[write text="log(ab) = log a + log b          but          log(a + b) is NOT log a + log b"]]']},
        {"term": "magnitude", "say":
            "The **magnitude** of a vector is its length: how much of it there is, with the direction stripped "
            "away. You find it by squaring each component, adding those, and taking the square root, which is "
            "Pythagoras again. Two consequences catch people out. It is never negative, even when every "
            "component is. And adding two vectors gives a length at most as big as the two lengths added, and "
            "strictly smaller whenever they point different ways.",
         "board": ['[[vector v="4,3" caption="the length comes from both components, not from either one alone"]]']},
        {"term": "polynomial", "say":
            "A **polynomial** is a sum of terms, each one a coefficient times the variable raised to a whole "
            "number power. That restriction on the exponents is what gives the whole family its good behaviour: "
            "no breaks, no corners, no asymptotes, just one smooth unbroken curve. The highest exponent caps "
            "two things at once. A fifth power allows at most five crossings of the horizontal axis and at most "
            "four turning points. Fractional or negative exponents put an expression in another family "
            "entirely.",
         "board": ['[[graph func="x^3-3x" range="-3..3" yrange="-4..4" caption="count the turning points against the highest exponent"]]']},
        {"term": "range", "say":
            "The **range** of a function is the complete collection of output values it actually produces as "
            "the input runs over the whole domain. Domain is what goes in, this is what comes out. Two "
            "warnings. In statistics the same word describes the largest value minus the smallest, a different "
            "idea altogether. And this is what the rule really reaches, not what it is permitted to reach: x "
            "squared has every real number available to it, yet never produces a negative one.",
         "board": ['[[graph func="x^2" range="-4..4" yrange="-2..16" caption="how high and how low do the outputs actually get"]]']},
        {"term": "sine", "say":
            "On the unit circle, the **sine** of an angle is the second coordinate of the point you reach when "
            "you start at the far right and turn through it. Let the angle keep growing and those heights trace "
            "out the familiar wave. Here is the error worth killing now. This is not a quantity multiplied by "
            "the angle, so it does not distribute over addition. The value for a sum of two angles is not the "
            "two separate values added together. A separate identity handles that case.",
         "board": ['[[graph func="sin(x)" range="-6.5..6.5" yrange="-2..2" caption="the height of the circle point, unrolled as the angle grows"]]']},
        {"term": "stretch", "say":
            "A **stretch** is a transformation that scales a graph rather than sliding it. Multiply the whole "
            "output by three and every height triples, pulling the curve away from the horizontal axis. Now the "
            "part almost everybody gets backwards. Multiplying the input by three does the opposite of what it "
            "looks like: the graph is squeezed toward the vertical axis by a factor of three, because x now "
            "only has to travel a third as far to give the same output.",
         "board": ['[[graph func="x^2 ; (3*x)^2" range="-3..3" yrange="-1..9" caption="the input was tripled, and the curve got narrower, not wider"]]']},
        {"term": "tangent", "say":
            "The **tangent** of an angle is the sine divided by the cosine, which on a right triangle works out "
            "as the opposite side over the adjacent one. Picture it as the slope of the line from the origin "
            "out to your point on the unit circle. That is why it blows up: wherever the cosine is zero, the "
            "division is impossible and the graph has a vertical asymptote. It also repeats twice as often as "
            "sine, once every half turn.",
         "board": ['[[graph func="tan(x)" range="-4.7..4.7" yrange="-6..6" caption="notice where the curve breaks, and how often the pattern repeats"]]']},
        {"term": "verify", "say":
            "To **verify** an identity is to show that its two sides are the same expression for every value "
            "you are allowed to substitute. That last part is the whole job. Trying three angles and finding "
            "they agree proves nothing, because a false statement can still survive a handful of test values. "
            "So you never plug in numbers as evidence. You take one side alone and rewrite it, step by legal "
            "step, until it turns into the other side.",
         "board": ['[[write text="tan θ · cos θ  =  sin θ        rewrite the LEFT side alone until it becomes the right"]]']},
    ],
    "probstat": [
        {"term": "mean", "say":
            "The **mean** is the fair-share average. You pool everything together, then split it evenly "
            "among however many there are. If three people bring three, five, and ten cookies, that is "
            "eighteen cookies shared three ways, so six each. The mean answers one question: if everyone "
            "had the same amount, how much would that be?",
         "board": ['[[write text="mean = (3 + 5 + 10) ÷ 3 = 6"]]']},
        {"term": "median", "say":
            "The **median** is the middle value once you line everything up in order. Not the average — "
            "the middle. It matters because one very large or very small number can drag the mean way "
            "off, while the median barely moves. That is why you hear about median house prices instead "
            "of average ones.",
         "board": ['[[write text="3,  5,  10   →   median = 5"]]']},
        {"term": "quantitative", "say":
            "Data is called **quantitative** when the values are real numbers that measure or count "
            "something, and doing arithmetic with them makes sense. Height, test score, number of "
            "siblings, minutes spent on homework, all quantitative. You can average them, subtract them, "
            "and study how spread out they are. The other kind is categorical, where values are labels "
            "like favorite color or brand of phone. Here is the trap. Not everything written with digits "
            "is quantitative. A jersey number, a zip code, a phone number is just a label wearing a "
            "numeric costume. Averaging zip codes gives you nonsense, so that data is categorical.",
         "board": ['[[write text="quantitative = numbers you can do arithmetic on"]]',
                   '[[card title="Quantitative?" items="height: yes | test score: yes | zip code: NO, it is a label"]]']},
        {"term": "histogram", "say":
            "A **histogram** is a picture of numerical data. You slice the number line into equal "
            "intervals, called bins, and build a bar showing how many values fell into each bin. A taller "
            "bar means more data crowded into that range. It lets you see the shape of a whole data set "
            "at a glance, where values pile up and where they thin out. Careful with one thing. A "
            "histogram is not a bar chart. Bar charts show separate categories, so their bars stand apart "
            "with gaps. Histogram bars touch, because the number line has no gaps, and shuffling them "
            "around would destroy the meaning.",
         "board": ['[[histogram data="1,3,7,9,6,3,1" caption="bars touch because the number line is continuous"]]',
                   '[[write text="histogram: bins along the number line, bar height = count"]]']},
        {"term": "skewed", "say":
            "A distribution is **skewed** when one tail stretches out much farther than the other, so the "
            "picture is lopsided instead of symmetric. Think of house prices in a town. Most homes "
            "cluster in an ordinary range, but a few mansions drag a long thin tail out to the right. "
            "That one is skewed right. If the long tail runs to the left instead, it is skewed left. Here "
            "is the trap. The name comes from the tail, not from the pile. Students look at where the "
            "bulk of the data sits and name that direction. Ignore the hump. Follow the tail.",
         "board": ['[[histogram data="9,7,4,3,2,1,1" caption="skewed right: the long thin tail points right"]]',
                   '[[write text="name the skew for the TAIL, not the hump"]]']},
        {"term": "standard deviation", "say":
            "**Standard deviation** is a single number answering how spread out data is, by measuring the "
            "typical distance from a value to the mean. A small standard deviation means everyone is "
            "bunched tightly around the average. A large one means the values are scattered all over. Two "
            "classes can share the exact same average test score while one is uniform and the other has "
            "stars and strugglers, and standard deviation is what tells those two apart. Careful with one "
            "thing. It is never negative. It is a distance, and the smallest it can possibly be is zero, "
            "which happens only when every value is identical.",
         "board": ['[[dotplot data="4,5,5,5,6" caption="bunched tightly: small standard deviation"]]',
                   '[[dotplot data="1,3,5,7,9" caption="same center, much bigger spread"]]']},
        {"term": "interquartile range", "say":
            "The **interquartile range** measures spread by looking only at the middle half of your data. "
            "Line the values up in order, find the quarter mark and the three quarter mark, and take the "
            "distance between them. That distance covers the middle fifty percent, and it tells you how "
            "tightly the typical values cluster. Careful with one thing. Students confuse it with the "
            "plain range, which stretches from the smallest value all the way to the largest. The plain "
            "range can be wrecked by one strange value at the end. This measure throws the ends away, "
            "which is exactly why it is trusted when data has outliers.",
         "board": ['[[boxplot data="2,5,7,9,14" caption="IQR = Q3 − Q1, the width of the box"]]',
                   '[[write text="IQR = the middle 50% of the data; it ignores the extremes"]]']},
        {"term": "outlier", "say":
            "An **outlier** is a value sitting so far from the rest of the data that it looks like it "
            "does not belong to the same story. One person earning ten million dollars in a survey of "
            "teachers is an outlier. These values matter because they yank the mean and the range around "
            "dramatically, while the median and the interquartile range barely flinch. Careful with one "
            "thing. An outlier is not automatically a mistake to delete. Sometimes it is a typo, but "
            "sometimes it is the most interesting fact in the entire data set. You investigate it, you do "
            "not simply erase it.",
         "board": ['[[dotplot data="3,4,4,5,5,6,20" caption="the 20 sits far from the pack"]]',
                   '[[write text="outliers wreck the mean and range; median and IQR resist them"]]']},
        {"term": "correlation", "say":
            "**Correlation** is a number measuring how tightly the points on a scatterplot hug a straight "
            "line, and which way that line tilts. It runs from negative one to positive one. Near "
            "positive one, the points march upward in a tight band. Near negative one, they march "
            "downward just as tightly. Near zero, there is no straight line pattern at all. Careful with "
            "one thing. This number only detects straight line relationships. A scatterplot can trace a "
            "gorgeous curve, a clear and powerful relationship, and the correlation will still report a "
            "value near zero, because the pattern is not a line. Always look at the picture too.",
         "board": ['[[scatter points="(1,2) (2,3.5) (3,5) (4,6.5) (5,8)" fit="true" caption="a tight upward band: r close to +1"]]',
                   '[[write text="r runs from −1 to +1 and measures LINEAR strength only"]]']},
        {"term": "causation", "say":
            "**Causation** means one thing actually makes the other happen, that changing the first "
            "genuinely produces the change in the second. That is a far bigger claim than saying two "
            "things move together. Ice cream sales and drowning deaths rise together every summer, but "
            "ice cream is not drowning anybody. Hot weather is quietly driving both. Here is the trap, "
            "and it is the most famous trap in all of statistics. A strong correlation, even a beautiful "
            "one, is never proof by itself. The only reliable way to earn a causal claim is a well "
            "designed experiment with random assignment.",
         "board": ['[[write text="correlation ≠ causation"]]',
                   '[[card title="Why two things move together" items="A causes B | B causes A | a lurking variable causes both | coincidence"]]']},
        {"term": "bias", "say":
            "**Bias** is a flaw in how you collect data that pushes your results consistently in one "
            "direction, away from the truth. It is not random bad luck. Bad luck scatters both ways and "
            "washes out. This leans the same way every single time. Surveying only people who answer a "
            "landline, or only the customers angry enough to write a review, tilts your answer before you "
            "do any math at all. Careful with one thing. A bigger sample does not fix it. Ask a million "
            "of the wrong people and you get a beautifully precise, confidently wrong answer. Only better "
            "collection methods help.",
         "board": ['[[write text="bias = systematic error, always leaning the same way"]]',
                   '[[card title="Common sources" items="voluntary response | undercoverage | nonresponse | leading questions"]]']},
        {"term": "sample space", "say":
            "The **sample space** is the complete list of everything that could possibly happen in an "
            "experiment. Flip one coin and it is heads and tails. Roll one die and it is the six faces. "
            "Flip two coins and it is four outcomes, not three, because heads then tails is a different "
            "result from tails then heads. Getting this list right is the whole foundation, because "
            "probability means counting the outcomes you want out of the outcomes there are. Careful with "
            "one thing. The outcomes must be equally likely for that simple counting to work, and they "
            "must not overlap or leave anything out.",
         "board": ['[[write text="two coins: HH, HT, TH, TT  —  four outcomes, not three"]]',
                   '[[card title="Building the list" items="write every outcome | no overlaps | nothing left out"]]']},
        {"term": "complement", "say":
            "The **complement** of an event is simply everything else, every outcome where that event "
            "does not happen. If the event is rolling a six, its complement is rolling anything that is "
            "not a six. Since one of the two absolutely has to occur, their probabilities always total "
            "one, and that gives you a shortcut. The chance something happens is one minus the chance it "
            "does not. That flip is a lifesaver on at least one problems. Careful with one thing. The "
            "opposite of at least one is none, not all. Students reach for the far extreme when the real "
            "opposite is zero.",
         "board": ['[[write text="P(not A) = 1 − P(A)"]]',
                   '[[write text="the complement of AT LEAST ONE is NONE (not all)"]]']},
        {"term": "conditional probability", "say":
            "**Conditional probability** is the chance of something happening given that you already know "
            "something else is true. That extra knowledge shrinks the world you are looking at. The "
            "chance a random person is over six feet tall is one thing, but the chance given that the "
            "person plays professional basketball is a completely different number, because you have "
            "narrowed the pool. So you no longer divide by everybody. You divide only by the group you "
            "were told you are inside. Careful with one thing. Order matters enormously. The chance of "
            "rain given clouds is nothing like the chance of clouds given rain.",
         "board": ['[[write text="P(A | B) = P(A and B) / P(B)  —  divide by the GIVEN group"]]',
                   '[[card title="Watch the order" items="P(A given B) is not P(B given A) | the given event becomes the new denominator"]]']},
        {"term": "expected value", "say":
            "**Expected value** is the long run average of a random process, what you would end up with "
            "per try if you repeated it thousands of times. You compute it by multiplying each possible "
            "outcome by its probability and totalling everything up. It is how insurance companies and "
            "casinos plan their entire business, calmly, one small edge at a time. Here is the trap. This "
            "average is often a number you can never actually get on any single try. The expected number "
            "of heads in three flips is one and a half, and you will never see half a head. It describes "
            "the average, not any one result.",
         "board": ['[[write text="E(X) = Σ (outcome × its probability)"]]',
                   '[[write text="the expected value need not be a possible outcome"]]']},
        {"term": "normal distribution", "say":
            "The **normal distribution** is the famous bell shaped curve: symmetric, one peak in the "
            "middle, tails thinning out smoothly on both sides. Heights, measurement errors, and many "
            "test scores land close to this shape. Its power is that once you know the mean and the "
            "standard deviation, you know the entire curve, and you can say what fraction of the data "
            "sits in any stretch of it. About sixty eight percent falls within one standard deviation of "
            "the mean. Careful with one thing. Not every humped pile of data is normal. Skewed data has a "
            "hump too, and these rules will mislead you there.",
         "board": ['[[normal caption="symmetric bell: about 68% within one standard deviation"]]',
                   '[[write text="mean and standard deviation together fix the whole curve"]]']},
        {"term": "margin of error", "say":
            "The **margin of error** is the cushion you place around a sample result to honestly admit "
            "that your sample is not the whole population. A poll reporting fifty two percent with a "
            "cushion of three points is really saying the truth is plausibly somewhere between forty nine "
            "and fifty five. It comes from sampling variability, the plain fact that a different random "
            "sample would have handed you a slightly different number. Careful with one thing. That "
            "cushion only accounts for random sampling wobble. It does nothing about bad questions, "
            "dishonest answers, or a badly chosen sample. Those errors hide completely outside it.",
         "board": ['[[write text="52% ± 3%   →   plausible range 49% to 55%"]]',
                   '[[write text="covers random variation ONLY — never bias"]]']},
        # --- build gc (2026-08-14): red-list additions for this course. See the
        # change note at the top of this file. Appended, never edited.
        {"term": "bar chart", "say":
            "A **bar chart** is a picture of separate groups. Each group gets its own bar, and the height of "
            "that bar shows how many landed in it, or what share of the whole it took. Notice the gaps. The "
            "groups are labels, not places on a number line, so you may reorder them any way you like and "
            "nothing is lost. That is where the confusion lives. A histogram looks similar, but its bars touch, "
            "and shuffling those would wreck the meaning.",
         "board": ['[[bars data="cats:7 | dogs:5 | fish:3" caption="separate groups, so the bars stand apart"]]']},
        {"term": "categorical", "say":
            "Data is **categorical** when each value is a label naming which group something belongs to: "
            "favorite color, brand of phone, blood type. Counting how many fall in each group makes sense, and "
            "averaging the labels does not. Here is the trap. Digits do not make a value numerical. A zip code, "
            "a jersey number, or an answer coded as one for yes and two for no is still a label wearing a "
            "numeric costume.",
         "board": ['[[card title="label, or number?" items="favorite color — a label | blood type — a label | zip code — a label written with digits"]]']},
        {"term": "chance", "say":
            "In statistics, **chance** means a number saying how often something happens when the same "
            "situation is repeated over and over. It runs from zero, the number we give to something that "
            "cannot happen, up to one, the number we give to something certain. Here is the trap. Two possible "
            "outcomes do not automatically split evenly. Rain tomorrow and no rain are two outcomes, yet "
            "counting outcomes only works when every outcome is equally likely, and the weather is not a fair "
            "coin.",
         "board": ['[[write text="0 = cannot happen       1/2 = as often as not       1 = certain"]]']},
        {"term": "data", "say":
            "In statistics, **data** means the recorded facts you actually collected, together with what each "
            "value measures and who or what it came from. Heights, favorite colors, minutes spent reading, all "
            "of it counts. Here is the trap. Numbers by themselves are not enough. A column of values with no "
            "labels tells you nothing, because the same figure means one thing as a height in centimeters and "
            "something else entirely as an age in years.",
         "board": ['[[card title="a value needs its context" items="172 — meaningless on its own | 172 cm — one person\'s height | record who was measured, and in what units"]]']},
        {"term": "experiment", "say":
            "In statistics, an **experiment** is a study where the researcher actively imposes a treatment and "
            "then compares what happens. You place people into groups, ideally at random, and you change one "
            "thing on purpose. That deliberate assignment is what can earn a claim about cause. Here is the "
            "trap. Asking people what they already do is an observational study instead. Watching and recording "
            "never rules out the other differences between the groups, however many people you reach.",
         "board": ['[[card title="two kinds of study" items="experiment — the researcher assigns the treatment | observational — the researcher only watches or asks | only the first can point at a cause"]]']},
        {"term": "long run", "say":
            "The **long run** is what a probability actually promises: not what happens next, but what settles "
            "out over very many repeats. One in six for rolling a four does not mean one four in every six "
            "rolls. Six rolls can easily hand you three fours, or none at all. Over thousands of rolls, though, "
            "the share of fours creeps toward one sixth and stays near it. Here is the trap. A drought of fours "
            "never makes one due. Dice keep no memory.",
         "board": ['[[write text="6 rolls: almost anything can happen        6,000 rolls: the share of 4s settles near 1/6"]]']},
        {"term": "population", "say":
            "A **population** is every single member of the group your conclusion is meant to be about, and you "
            "decide what it is before you collect anything: every registered voter in the state, every bolt off "
            "a factory line, every patient with one diagnosis. A sample is the part of it you actually reach. "
            "Here is the trap. It is set by your question, and it need not be people. Bolts, days, and phone "
            "calls all qualify.",
         "board": ['[[card title="who the conclusion is about" items="population — every member of the group you want to describe | sample — the part you actually measured"]]']},
        {"term": "sampling variability", "say":
            "The phrase **sampling variability** names a plain fact: two honest samples drawn from the same "
            "group will not give the same answer. Poll a thousand people today, a thousand more tomorrow, both "
            "done carefully, and the two results will differ a little. That wobble is expected, and a margin of "
            "error exists to describe it. Here is the trap. This is not bias. Bias pushes every sample the same "
            "wrong way, while this wobble lands on both sides of the truth.",
         "board": ['[[dotplot data="48,49,50,50,51,52" caption="six careful polls of the same population"]]']},
        {"term": "scatter", "say":
            "A **scatter** plot shows two measurements taken from the same individual at once: one along the "
            "horizontal axis, one up the vertical, and a single dot for each individual. It lets you see "
            "whether the two travel together. Here is the trap. Every dot is a matched pair from one source, so "
            "the two columns may never be sorted or shuffled on their own. Break the pairing and you invent a "
            "relationship nobody ever measured.",
         "board": ['[[scatter points="(1,2) (2,3.5) (3,5) (4,5.5) (5,7)" caption="each dot is one student: hours studied across, test score up"]]']},
        {"term": "spread", "say":
            "The word **spread** describes how far apart the values in a data set are, and it says nothing at "
            "all about where the center sits. Two classes can share an identical average while one is bunched "
            "tightly and the other holds both stars and strugglers. Range, interquartile range and standard "
            "deviation each measure it a different way. Here is the trap. An average reported alone hides "
            "whether everyone sat near it or almost nobody did.",
         "board": ['[[dotplot data="4,5,5,5,6" caption="center 5: the values huddle around it"]]', '[[dotplot data="1,3,5,7,9" caption="center 5 again, and the values are flung far apart"]]']},
        {"term": "stem", "say":
            "In a **stem** and leaf plot, each value is split in two. The leading part is written once down the "
            "left, and the final digit of every value sharing it sits beside it as a leaf. Sixty one, sixty "
            "four and sixty seven all begin with six, so that six is written once and carries three leaves. "
            "Here is the trap. Leaves are not tally marks. Each leaf is one real value, so the whole set can be "
            "read straight back off the picture.",
         "board": ['[[write text="61, 64, 67   becomes   6 | 1 4 7"]]']},
        {"term": "survey", "say":
            "A **survey** collects answers by asking a sample of people questions, then uses those answers to "
            "describe the whole group. Nothing is imposed on anybody, which is why it can describe what is true "
            "without showing what caused it. Here is the trap. Who answers matters more than how many answer. "
            "Replies from volunteers can be wildly off even in the thousands, because the people who bother to "
            "reply differ from the people who ignore you.",
         "board": ['[[card title="what goes wrong when we ask" items="who replies — volunteers are not typical | how the question is worded | how many people refuse to answer"]]']},
    ],
    "calculus": [
        {"term": "derivative", "say":
            "A **derivative** answers one question: how fast is this changing right now? Not the average "
            "speed over a whole trip, but the speed at one exact instant, like the number on a "
            "speedometer. When we take the derivative of a function, we get back a new function whose "
            "output is the slope of the original at any point you pick.",
         "board": ['[[write text="derivative = how fast it is changing, at one instant"]]']},
        {"term": "limit", "say":
            "A **limit** asks where a function is heading as you get closer and closer to some value — "
            "not what happens exactly at that spot, but what it is approaching. That distinction is the "
            "whole reason limits exist: a function can have a hole at a point and still be clearly "
            "heading somewhere.",
         "board": ['[[write text="what is it approaching, as x gets close?"]]']},
        {"term": "removable discontinuity", "say":
            "A **removable discontinuity** is the proper name for a hole in a graph, and the part that "
            "matters is where the hole came from: a hole never simply appears. Take f of x "
            "equals x squared minus four, all over x minus two. The top factors into x minus two times "
            "x plus two, so the x minus two cancels and leaves x plus two, everywhere except at x equals "
            "two, where the original fraction divided by zero. Division by zero is undefined, so that "
            "one input has no output: the graph is the line y equals x plus two with one point punched "
            "out of it. Cancelling did not repair x equals two, and that is why the limit there is four "
            "while f of two does not exist.",
         "board": ['[[write text="f(x) = (x^2 - 4)/(x - 2)"]]',
                   '[[write text="= (x-2)(x+2)/(x-2) = x + 2,   x \u2260 2"]]',
                   '[[graph lines="y=x+2" hole="2" range="-1..5" caption="the same line, with x = 2 removed -- the curve runs right up to the gap from both sides"]]']},
        {"term": "continuity", "say":
            "**Continuity** means a curve has no breaks in it. Picture drawing the graph with a pencil. "
            "If you can draw the whole thing without ever lifting the pencil off the paper, the function "
            "is continuous there. Breaks come in a few flavors. A hole, where one single point is "
            "missing. A jump, where the graph leaps from one height to another. Or a place where the "
            "curve shoots off forever. Here is the trap. A function can have a perfectly good limit at a "
            "point and still fail continuity there, because the value the function actually takes at that "
            "point sits somewhere else entirely.",
         "board": ['[[write text="continuous at x=a: f(a) exists, lim f(x) exists, and they match"]]',
                   '[[card title="3 ways continuity breaks" items="hole | jump | blow-up"]]']},
        {"term": "tangent line", "say":
            "A **tangent line** is the straight line that just grazes a curve at a single point and heads "
            "in exactly the same direction the curve is heading right there. Think of it as the best "
            "straight line imitation of the curve at that spot. Zoom in far enough on a smooth curve and "
            "it starts to look straight, and that straight thing is the tangent line. Its steepness is "
            "the derivative. Here is the trap. Students often think a tangent line is only allowed to "
            "touch the curve once. It can cross the curve somewhere else entirely and still be perfectly "
            "tangent at the point you care about.",
         "board": ['[[graph func="x^2" lines="y=2x-1" points="(1,1)" range="-3..4" yrange="-3..9" caption="the tangent at (1, 1): it touches the curve and matches its slope there"]]',
                   '[[write text="tangent at a point: touches there, matches the slope there"]]']},
        {"term": "function notation", "say":
            "Before the calculus starts, make sure you are SAYING **function notation** correctly, "
            "because you will read it on every page from here. The letter names the rule and the "
            "parentheses hold the input, so you say f of x, never f times x. Nothing is multiplied. Add a "
            "tick mark and it becomes f prime of x, which is said exactly that way and names the "
            "derivative of f. Two tick marks is f double prime of x. And the letter is only a name, so g "
            "of x and h of x read the same way and follow all the same rules.",
         "board": ['[[write text="f(x)    ←  “f of x”          (never f times x)"]]',
                   '[[write text="f′(x)   ←  “f prime of x”     — the derivative of f"]]',
                   '[[write text="f″(x)   ←  “f double prime of x” — the derivative of the derivative"]]']},
        {"term": "chain rule", "say":
            "The **chain rule** is what you reach for when one function sits inside another, like a "
            "machine feeding a second machine. To differentiate the whole stack, take the derivative of "
            "the outside function while leaving the inside completely alone, then multiply by the "
            "derivative of the inside. Outside first, inside second, and the two get multiplied together. "
            "Here is the trap. Almost every chain rule mistake is the same one: people differentiate the "
            "outer function and stop, forgetting to multiply by the derivative of what was tucked inside. "
            "If the inside is anything other than plain x, that extra factor is there.",
         "board": ['[[write text="d/dx f(g(x)) = f\'(g(x)) · g\'(x)"]]',
                   '[[card title="chain rule" items="derivative of outside, inside untouched | times derivative of inside"]]']},
        {"term": "implicit differentiation", "say":
            "**Implicit differentiation** is how you find a slope when the equation was never solved for "
            "y. Take a circle, x squared plus y squared equals twenty five. No single formula gives y in "
            "terms of x, but the curve still has a slope at every point. So you differentiate both sides "
            "with respect to x, treating y as a secret function of x. That means every time you "
            "differentiate a y, you tack on d y d x. Then you solve for d y d x. Here is the trap. "
            "Forgetting that tacked on factor is the whole ballgame, and it is the mistake nearly "
            "everyone makes first.",
         "board": ['[[circle r="1" caption="a curve with no single y = f(x) formula, but a slope everywhere"]]',
                   '[[write text="x^2 + y^2 = 25 → 2x + 2y·(dy/dx) = 0 → dy/dx = -x/y"]]']},
        {"term": "related rates", "say":
            "A **related rates** problem is one where two or more quantities are changing at the same "
            "moment, and because an equation ties the quantities together, it ties their rates together "
            "too. A ladder slides down a wall, so the top falls while the foot slides outward. Write the "
            "equation linking the quantities first. Then differentiate the whole equation with respect to "
            "time. Now a rate you know hands you a rate you want. Here is the trap. Do not plug in the "
            "specific numbers until after you differentiate. Substitute too early and your changing "
            "quantities freeze into constants.",
         "board": ['[[righttriangle adj="4" opp="3" caption="ladder on a wall: x^2 + y^2 = 25"]]',
                   '[[write text="differentiate in time: 2x(dx/dt) + 2y(dy/dt) = 0 — numbers go in AFTER"]]']},
        {"term": "critical point", "say":
            "A **critical point** is an input where the derivative is zero, or where the derivative does "
            "not exist at all. Those are the only places a function can turn around, so they are your "
            "suspect list whenever you hunt for a highest or lowest value. Where the derivative is zero "
            "the tangent line lies flat, and where it fails to exist you have a corner or a sudden "
            "vertical stretch. Here is the trap. A critical point is only a candidate. It does not have "
            "to be a maximum or a minimum. The curve y equals x cubed flattens out at zero and then keeps "
            "climbing right through it.",
         "board": ['[[graph func="x^3" range="-3..3" yrange="-10..10" points="(0,0)" caption="flat at x = 0, yet neither a max nor a min"]]',
                   '[[write text="critical point: f\'(x)=0 or f\'(x) undefined — a candidate, not a guarantee"]]']},
        {"term": "concavity", "say":
            "**Concavity** describes the way a curve bends, not the way it leans. If it bends upward like "
            "a bowl that would hold water, we say concave up, and that happens wherever the second "
            "derivative is positive. If it bends downward like a dome shedding water, it is concave down, "
            "and the second derivative is negative. Here is the trap, and it catches almost everyone. "
            "Concave up does not mean going up. A curve can be falling the entire time and still be "
            "concave up, because rising and falling belong to the first derivative while bending belongs "
            "to the second.",
         "board": ['[[graph func="x^2" range="-4..4" yrange="-1..16" caption="concave up: bends like a bowl, second derivative positive"]]',
                   '[[card title="bending, not leaning" items="f\'\' positive: concave up (bowl) | f\'\' negative: concave down (dome)"]]']},
        {"term": "inflection point", "say":
            "An **inflection point** is where a curve changes the direction of its bend. On one side it "
            "curves like a bowl, on the other side like a dome, and the inflection point is the exact "
            "spot where it switches. That is where the second derivative changes sign. Think of steering "
            "a car: you are still rolling forward, but you stop turning left and begin turning right. "
            "Here is the trap. The second derivative hitting zero is not enough by itself. It has to "
            "actually change sign there. For y equals x to the fourth, the second derivative touches zero "
            "at the origin and never switches.",
         "board": ['[[graph func="x^3" range="-3..3" yrange="-10..10" points="(0,0)" caption="the bend flips at x = 0: concave down, then concave up"]]',
                   '[[write text="inflection: f\'\' must CHANGE SIGN (f\'\'=0 alone proves nothing)"]]']},
        {"term": "antiderivative", "say":
            "An **antiderivative** is a function whose derivative is the one you started with. You are "
            "running the machine backwards. Instead of asking how fast is this changing, you are asking "
            "what was changing in this way. Since the derivative of x squared is two x, we say x squared "
            "is an antiderivative of two x. Here is the trap. There is never just one. Adding any "
            "constant leaves a derivative completely unchanged, so x squared plus seven works just as "
            "well. That is why we write plus C, and an initial condition is what pins C down to a single "
            "number.",
         "board": ['[[write text="d/dx of (x^2 + C) = 2x     so     ∫ 2x dx = x^2 + C"]]',
                   '[[card title="pinning down C" items="general: x^2 + C | given y(0)=5 | then C = 5"]]']},
        {"term": "u-substitution", "say":
            "**U-substitution** is the chain rule run in reverse. When an integral contains some inner "
            "expression and, sitting right there next to it, that inner expression's own derivative, you "
            "give the inner part a new name, u. The messy integral collapses into something simple in u, "
            "you integrate that, and then you swap x back in at the end. Here is the trap. You cannot "
            "rename only part of the problem. The d x has to turn into d u as well. And on a definite "
            "integral, either convert the limits into u values or come all the way back to x before you "
            "evaluate.",
         "board": ['[[write text="∫ 2x·cos(x^2) dx , let u = x^2 , du = 2x dx → ∫ cos u du = sin u + C"]]',
                   '[[card title="u-sub checklist" items="pick u | find du | rewrite ALL of it | swap back or change the limits"]]']},
        {"term": "Riemann sum", "say":
            "A **Riemann sum** is how you estimate the area under a curve before you know any clever "
            "formulas. Slice the region into thin vertical rectangles. Read each rectangle's height off "
            "the curve, multiply height by width to get its area, and add them all up. A handful of "
            "rectangles gives a rough answer. More rectangles gives a better one, and the limit as they "
            "become infinitely thin is exactly the definite integral. Here is the trap. Taking each "
            "height at the left edge, the right edge, or the midpoint gives three different estimates, so "
            "use the one the problem asks for.",
         "board": ['[[write text="Riemann sum: Σ f(x_i)·Δx ,  Δx = (b - a)/n"]]',
                   '[[card title="where do you read the height?" items="left endpoint | right endpoint | midpoint"]]']},
        {"term": "subscript", "say":
            "A small character sitting low beside a letter is a **subscript**, said out loud as sub. So x "
            "with a little i is x sub i, and it does not mean x multiplied by i. Nothing is multiplied. "
            "When we slice an interval into pieces, the cut points are x sub zero, x sub one, x sub two, "
            "and so on, and x sub i just means whichever one is in position i. It is how we talk about a "
            "whole list of numbers without having to name every single one of them.",
         "board": ['[[write text="x₀ , x₁ , x₂ , … , xₙ    ←  “x sub zero, x sub one, … x sub n”"]]',
                   '[[write text="xᵢ names ONE cut point — it is not x · i"]]']},
        {"term": "definite integral", "say":
            "A **definite integral** is a single number: the accumulated total of a rate across an "
            "interval. Geometrically it is the area caught between the curve and the horizontal axis, "
            "from one x value to another. If the curve gives your speed, the definite integral gives how "
            "far you went. Here is the trap. It measures signed area, not plain area. Anything below the "
            "axis counts as negative and cancels against the positive part above. So when a problem asks "
            "for actual geometric area, or for total distance rather than net displacement, you must "
            "handle the negative pieces separately.",
         "board": ['[[write text="∫ from a to b of f(x) dx = a NUMBER (signed area)"]]',
                   '[[card title="signed area" items="above the axis: positive | below the axis: negative | they cancel"]]']},
        {"term": "Fundamental Theorem of Calculus", "say":
            "The **Fundamental Theorem of Calculus** is the bridge between the two halves of this course. "
            "It says that to find the accumulated total of a rate from one endpoint to another, you never "
            "have to add up infinitely many rectangles. You just find an antiderivative, evaluate it at "
            "the top limit, evaluate it at the bottom limit, and subtract. Derivatives and integrals undo "
            "each other. Here is the trap. This works only when the function stays continuous across the "
            "entire interval. If the curve blows up somewhere in the middle, plugging in the endpoints "
            "hands you a confident wrong answer.",
         "board": ['[[write text="∫ from a to b of f(x) dx = F(b) - F(a) ,  where F\' = f"]]',
                   '[[card title="two halves, one idea" items="derivative: rate from total | integral: total from rate | they undo each other"]]']},
        {"term": "area between curves", "say":
            "To find the **area between curves**, you take the function on top, subtract the function on "
            "the bottom, and integrate that difference across the stretch where they overlap. Every thin "
            "vertical strip has a height equal to the top curve minus the bottom curve, and integrating "
            "simply adds up all those strips. Here is the trap. Which curve is on top can switch partway "
            "through the region. So find where the curves cross before you integrate anything, split the "
            "problem at those crossings, and work each piece with the correct function playing the role "
            "of top.",
         "board": ['[[write text="Area = ∫ from a to b of ( top(x) − bottom(x) ) dx"]]',
                   '[[card title="before you integrate" items="sketch both | find the intersections | recheck which one is on top in each piece"]]']},
        {"term": "slope field", "say":
            "A **slope field** turns a differential equation into a map of directions. At a grid of "
            "points across the plane you draw one tiny dash, and its steepness is whatever the equation "
            "says the slope must be at that point. Every solution has to flow along those dashes, the way "
            "iron filings line up around a magnet. It lets you see how solutions behave without solving "
            "anything. Here is the trap. The dashes themselves are not solutions. They are directions. To "
            "get a real solution you choose a starting point and follow the flow from there, and a "
            "different starting point gives a different curve.",
         "board": ['[[write text="slope field: at each point (x, y), draw a dash of slope y\' = f(x, y)"]]',
                   '[[card title="reading a slope field" items="dashes are directions, not curves | pick a start point | follow the flow"]]']},
        # --- build gc (2026-08-14): red-list additions for this course. See the
        # change note at the top of this file. Appended, never edited.
        {"term": "area under", "say":
            "The phrase **area under** a curve names what a definite integral measures: the space between the "
            "graph and the horizontal axis, across an interval. It is a total rather than a rate, and its units "
            "come from multiplying the two axes together, so a graph of velocity against time totals up to a "
            "change in position. Here is the trap. The integral counts space below the axis as negative, so it "
            "reports a signed total, which can be smaller than the space you would paint.",
         "board": ['[[card title="signed, not painted" items="above the axis — counts positive | below the axis — counts negative | to paint it instead, integrate the absolute value"]]']},
        {"term": "continuous", "say":
            "A function is **continuous** at a point when three things line up: it has a value there, it has a "
            "limit there, and those two agree. Across an interval, the picture is a graph you could draw "
            "without ever lifting your pencil. Here is the trap. Unbroken is not the same as smooth. The "
            "absolute value graph has a sharp corner at zero, so it passes the pencil test yet has no "
            "derivative there, because the two sides arrive with different slopes.",
         "board": ['[[graph func="abs(x)" range="-3..3" yrange="-1..3" caption="unbroken all the way through, and still no single slope at the corner"]]']},
        {"term": "differential equation", "say":
            "A **differential equation** is a statement about a derivative rather than about a number. It tells "
            "you the rate at which something changes, and it asks you to find the function that changes that "
            "way. Growth whose rate is proportional to the amount present is the standard example. Here is the "
            "trap. Solving one does not produce a number. It produces a family of functions carrying arbitrary "
            "constants, and you test a candidate by substituting it, and its derivative, back in.",
         "board": ['[[write text="dy/dt = k y        the rate depends on how much there is"]]']},
        {"term": "displacement", "say":
            "In motion problems, **displacement** is the change in position: where you finished, measured from "
            "where you started, with nothing said about the route between. It carries a sign, so once you pick "
            "which direction counts as positive, travel the other way subtracts, and a round trip back to the "
            "door comes to zero. Here is the trap. It is not the total distance. Walk three blocks out and "
            "three blocks back and you covered six blocks, yet your position changed by nothing.",
         "board": ['[[card title="displacement vs total distance" items="displacement — where you ended up | total distance — how far you actually travelled"]]']},
        {"term": "initial condition", "say":
            "An **initial condition** is the starting fact that picks one curve out of a family. "
            "Antidifferentiating leaves you an unknown constant, and one known value of the function pins that "
            "constant down. Here is the trap. Apply the fact after you integrate, never before it, and do not "
            "assume it lives at time zero. Any input where you know the output does the very same job, so read "
            "the wording rather than the habit.",
         "board": ['[[write text="y\' = 2x   gives   y = x² + C ;   y(0) = 3   pins   C = 3"]]']},
        {"term": "total distance", "say":
            "In motion problems, **total distance** is how far the object actually traveled, adding every "
            "stretch of the trip no matter which way it pointed. For a moving object it is the integral of "
            "speed, which is the absolute value of velocity, so it never decreases as time runs on. Here is the "
            "trap. It is not displacement. Where the object turns around, split the trip at the turning point "
            "and add the pieces, or the two directions cancel.",
         "board": ['[[card title="one trip, two honest answers" items="3 m out, then 3 m back | displacement = 0 m | total distance = 6 m"]]']},
    ],
    "diffeq": [
        {"term": "differential equation", "say":
            "A **differential equation** is an equation that contains a derivative. That is what makes it "
            "different from the equations you have solved before: instead of describing a number, it "
            "describes how something CHANGES. Solving one does not give you a number back — it gives you "
            "a whole function.",
         "board": ['[[write text="y′ = 3y      (an equation about how y changes)"]]']},
        {"term": "order", "say":
            "The **order** of a differential equation is simply the highest derivative that appears in "
            "it. One tick mark is first order, two tick marks is second order. We classify before we "
            "solve, because the order tells us which method will work — it is the first question to ask, "
            "every time.",
         "board": ['[[write text="y″ + y = 0   →   second order"]]']},
        {"term": "function notation", "say":
            "In this course the unknown is a FUNCTION, not a number, so **function notation** is carrying "
            "more weight than it used to and it is worth saying out loud. y of t means the value of the "
            "unknown function at time t. None of it is multiplication: y of t is not y times t. A tick "
            "mark makes it y prime, said exactly that way, and it names the derivative. Two tick marks is "
            "y double prime. The fraction written d y over d x is said d y d x and means that same "
            "derivative written another way. And y of zero is an initial condition: what the function "
            "equals at the start.",
         "board": ['[[write text="y(t)   ←  “y of t” — the unknown function at time t   (NOT y times t)"]]',
                   '[[write text="y′ = “y prime”      y″ = “y double prime”      dy/dx = “d y d x”"]]',
                   '[[write text="y(0) = 4   ←  “y of zero equals four” — the initial condition"]]']},
        {"term": "general solution", "say":
            "The **general solution** of a differential equation is not one function. It is the entire "
            "family of functions that satisfy the equation, carrying an arbitrary constant along with it. "
            "A first order equation brings one constant, so you get a whole stack of curves filling the "
            "plane, one for each value of that constant. Hand the problem a starting fact and the "
            "constant becomes a specific number, and the family collapses to the single curve through "
            "that starting point. Here is the trap. Never drop the constant. Without it you have answered "
            "exactly one case out of infinitely many.",
         "board": ['[[write text="y\' = 2x → general: y = x^2 + C | with y(0)=3: y = x^2 + 3"]]',
                   '[[card title="family vs member" items="general: still has C | particular: C pinned down | the initial condition picks it"]]']},
        {"term": "linear equation", "say":
            "A **linear equation** in this course means the unknown function and its derivatives show up "
            "only to the first power, never multiplied by each other, and never buried inside something "
            "like a sine or a square root. The coefficients out front can be as ugly as they like. "
            "Functions of x are perfectly fine, because the test only looks at how y and its derivatives "
            "appear. Here is the trap. Linear here has nothing to do with straight lines. Solutions can "
            "curve, oscillate, or run away to infinity. And y times y prime is not linear, even though "
            "each piece looks innocent.",
         "board": ['[[write text="linear: y\' + p(x)y = q(x)   |   NOT linear: y·y\' , (y\')^2 , sin(y)"]]',
                   '[[card title="the linearity test" items="y and its derivatives to the first power | never multiplied together | never inside a function"]]']},
        {"term": "separable equation", "say":
            "A **separable equation** is a first order equation you can pull apart, so that everything "
            "involving y sits on one side next to d y, and everything involving x sits on the other side "
            "next to d x. Once it is split, you integrate both sides and you are nearly home. One "
            "constant of integration is enough for the pair. Here is the trap. To separate, you usually "
            "divide by an expression containing y, and that quietly assumes it is not zero. Whatever "
            "value of y makes it zero is almost always a constant solution, and you have to put it back "
            "by hand.",
         "board": ['[[write text="dy/dx = g(x)·h(y) → (1/h(y)) dy = g(x) dx → integrate both sides"]]',
                   '[[card title="the lost solution" items="you divided by h(y) | so solve h(y) = 0 | add those constant solutions back"]]']},
        {"term": "initial value problem", "say":
            "An **initial value problem** is a differential equation packaged together with a starting "
            "fact, something like y of zero equals four. The equation by itself describes a whole family "
            "of curves. The starting fact tells you which single curve you are actually riding. So you "
            "solve the equation first, get an answer with a constant in it, then substitute the starting "
            "values and solve for that constant. Here is the trap. Apply the starting fact after you "
            "integrate, never before. And a second order equation needs two starting facts, usually a "
            "value and a slope at the same point.",
         "board": ['[[write text="IVP:  y\' = 2y  with  y(0) = 4   →   y = 4e^(2x)"]]',
                   '[[card title="how many conditions?" items="first order: one | second order: two | value and slope at the same point"]]']},
        {"term": "logistic model", "say":
            "A **logistic model** describes growth that starts out looking exponential and then flattens "
            "as it runs into a ceiling. That ceiling is the carrying capacity, the largest population the "
            "environment can support. Early on there is plenty of room, so growth is fast. As the "
            "population climbs toward the ceiling, the growth rate shrinks toward zero, and the graph "
            "traces a lazy S shape. Here is the trap. The population never actually reaches the carrying "
            "capacity. It only approaches it. And the fastest growth happens in the middle, at half the "
            "carrying capacity, not near the end.",
         "board": ['[[write text="dP/dt = kP(1 - P/M) ,  M = carrying capacity"]]',
                   '[[card title="S curve landmarks" items="early: nearly exponential | at half of M: fastest growth | approaching M: levels off"]]']},
        {"term": "integrating factor", "say":
            "An **integrating factor** is the clever multiplier that makes a first order linear equation "
            "collapse into something you can integrate directly. Put the equation into standard form, "
            "meaning y prime stands alone with a coefficient of one and some function of x multiplies y. "
            "The integrating factor is then e raised to the integral of that function. Multiply the whole "
            "equation through by it, and the left side becomes the derivative of one single product. "
            "Integrate both sides and finish. Here is the trap. Get into standard form first, or the "
            "factor you compute is simply wrong.",
         "board": ['[[write text="y\' + p(x)y = q(x) ,  μ = e^(∫ p dx) ,  (μ·y)\' = μ·q"]]',
                   '[[card title="order of operations" items="standard form FIRST | compute μ | multiply through | integrate"]]']},
        {"term": "exact equation", "say":
            "An **exact equation** is one that is secretly a derivative already, just written in "
            "disguise. Put it in the form M d x plus N d y equals zero. It is exact when the partial "
            "derivative of M with respect to y agrees with the partial derivative of N with respect to x. "
            "When that test passes, there is a hidden function of x and y whose total differential is "
            "your equation, and the solution is that function set equal to a constant. Here is the trap. "
            "Run the test before anything else. If the two partials disagree, the method fails outright "
            "and you need an integrating factor first.",
         "board": ['[[write text="M dx + N dy = 0 is exact when  ∂M/∂y = ∂N/∂x   →  F(x,y) = C"]]',
                   '[[card title="steps" items="test the two partials | integrate M with respect to x | use N to fix the leftover"]]']},
        {"term": "homogeneous", "say":
            "**Homogeneous** is a word this course uses in two completely different ways, which is "
            "exactly why it trips people up. For a first order equation, homogeneous means every term "
            "carries the same total degree, so the equation depends only on the ratio of y to x, and "
            "substituting a new variable for that ratio makes it separable. For a linear equation of any "
            "order, homogeneous means something else entirely: the right hand side is zero, so nothing is "
            "forcing the system. Here is the trap. Decide which situation you are in before choosing a "
            "method. The two meanings are unrelated.",
         "board": ['[[card title="two meanings, one word" items="first order: same degree, substitute v = y/x | linear: right side is 0, no forcing"]]',
                   '[[write text="y\'\' + p·y\' + q·y = 0   ← homogeneous in the linear sense"]]']},
        {"term": "characteristic equation", "say":
            "The **characteristic equation** is the algebra problem hiding inside a second order linear "
            "equation with constant coefficients. You guess that the solution is e to the r x, plug it "
            "in, and every term ends up carrying that same exponential, which you divide away. What "
            "survives is a plain quadratic in r. Its roots tell you the shape of the answer. Two "
            "different real roots give two exponentials. A repeated root gives an exponential and that "
            "same exponential times x. Complex roots give oscillation. Here is the trap. This shortcut "
            "works only when the coefficients are genuine constants.",
         "board": ['[[write text="a·y\'\' + b·y\' + c·y = 0   →   a·r^2 + b·r + c = 0"]]',
                   '[[card title="what the roots mean" items="distinct real: e^(r1 x) and e^(r2 x) | repeated: e^(rx) and x·e^(rx) | complex: sine and cosine"]]']},
        {"term": "superposition", "say":
            "**Superposition** is the reason linear equations are so friendly. If you have two solutions "
            "of a homogeneous linear equation, then any combination of them, each scaled by a constant "
            "and added together, is also a solution. That is precisely why a second order equation gets a "
            "general solution built from two independent pieces with two constants out front. Here is the "
            "trap. This only holds for homogeneous linear equations. Add two solutions of a "
            "nonhomogeneous one and the forcing term gets counted twice, so the sum solves nothing. For "
            "nonlinear equations it fails immediately.",
         "board": ['[[write text="if y1 and y2 solve y\'\' + p·y\' + q·y = 0 , so does c1·y1 + c2·y2"]]',
                   '[[card title="where the rule stops" items="homogeneous linear: works | nonhomogeneous: fails | nonlinear: fails"]]']},
        {"term": "subscript", "say":
            "A small number tucked low beside a letter is a **subscript**, and you say it out loud as "
            "sub. So y with a little one is y sub one, and it is not y multiplied by one. Nothing is "
            "multiplied. Here it labels DIFFERENT SOLUTIONS of the same equation: y sub one and y sub two "
            "are two genuinely different functions that both satisfy it, and c sub one and c sub two are "
            "the two constants that go with them. The subscript is how we keep them straight while we "
            "build the general solution out of both.",
         "board": ['[[write text="y₁ , y₂    ←  “y sub one, y sub two” — two different solutions"]]',
                   '[[write text="general: y = c₁·y₁ + c₂·y₂     (“c sub one y sub one plus c sub two y sub two”)"]]']},
        {"term": "particular solution", "say":
            "A **particular solution** is one single function that satisfies the equation, with no "
            "arbitrary constants left in it. In the nonhomogeneous chapter it has a sharper job: it is "
            "the piece that actually produces the forcing term on the right hand side, and your complete "
            "answer is the homogeneous solution added to it. Here is the trap. This phrase gets used two "
            "ways. Sometimes it means the curve you land on after applying an initial condition. "
            "Sometimes it means the piece that handles the forcing. Read the context, and never apply "
            "initial conditions until both pieces are assembled.",
         "board": ['[[write text="y = y_c + y_p   (complementary piece + particular piece)"]]',
                   '[[card title="two uses of the phrase" items="the curve fixed by an initial condition | the piece matching the forcing term"]]']},
        {"term": "damping", "say":
            "**Damping** is whatever drains energy out of a vibrating system: friction, air resistance, "
            "the shock absorber on a car. In the mass and spring equation it is the term carrying the "
            "first derivative, the one proportional to velocity. How much of it you have decides "
            "everything about the motion. A little, and the mass still swings back and forth with each "
            "swing smaller than the last. A lot, and it simply creeps back to rest without crossing at "
            "all. Here is the trap. Critically damped does not mean slow. It is the fastest possible "
            "return to rest with no overshoot.",
         "board": ['[[write text="m·y\'\' + c·y\' + k·y = 0 ,  c = the damping constant"]]',
                   '[[card title="three cases" items="underdamped: shrinking oscillation | critically damped: fastest, no overshoot | overdamped: slow creep"]]']},
        {"term": "resonance", "say":
            "**Resonance** happens when you push a system at exactly the rhythm it already wants to "
            "vibrate at. Every push lands in step with the motion, so energy piles up instead of "
            "cancelling, and the swings grow and grow. It is why a child on a swing goes higher from tiny "
            "well timed pushes, and why soldiers break step before crossing a bridge. In the math it "
            "appears when the forcing term matches a solution of the homogeneous equation, which is when "
            "you multiply your guess by x. Here is the trap. With even a little damping the amplitude "
            "does not grow forever. It settles at something large but finite.",
         "board": ['[[write text="forcing frequency = natural frequency → amplitude grows like x·sin(ωt)"]]',
                   '[[card title="resonance check" items="does the forcing match a homogeneous solution? | if yes, multiply the guess by x"]]']},
        {"term": "Laplace transform", "say":
            "The **Laplace transform** is a machine that takes a function of time and turns it into a "
            "function of a new variable called s. The whole point is what it does to derivatives: it "
            "converts them into multiplication, so a differential equation in t becomes an ordinary "
            "algebra problem in s. You solve that algebra, then run the inverse transform to come back to "
            "a function of time. It shines when the forcing switches on suddenly. Here is the trap. "
            "Transforming a derivative pulls the initial conditions in automatically, so they enter at "
            "the very start, not tacked on at the end.",
         "board": ['[[write text="L{y\'} = s·Y(s) - y(0)   |   L{y\'\'} = s^2·Y(s) - s·y(0) - y\'(0)"]]',
                   '[[card title="the round trip" items="transform t into s | solve the algebra | invert back to t"]]']},
        {"term": "phase plane", "say":
            "The **phase plane** is a way to see a system of two equations all at once. Instead of "
            "graphing each variable against time, you put one variable on the horizontal axis and the "
            "other on the vertical, and each solution becomes a path traced out as time runs forward. "
            "Predator and prey chasing each other shows up as a loop. Points where nothing moves are "
            "equilibria, and the eigenvalues tell you whether nearby paths spiral inward, spiral outward, "
            "or slide past. Here is the trap. Time is not on either axis. It hides in the direction you "
            "travel along the path.",
         "board": ['[[write text="phase plane: x across, y up — time is hidden in the direction of travel"]]',
                   '[[card title="equilibrium types" items="eigenvalues negative: stable | positive: unstable | complex: spiral"]]']},
        {"term": "slope field", "say":
            "A **slope field** is a picture of a differential equation before you solve anything. At "
            "each point of the plane you draw a tiny dash whose slope is whatever the equation says "
            "y prime equals right there. Do that everywhere and the dashes line up into currents, and "
            "every solution curve is just a path that flows with the current through its starting "
            "point. Here is the trap. The dashes are not the solutions. They are directions, and a "
            "solution threads through them the way a leaf rides a stream.",
         "board": ['[[write text="at each point (x, y): draw a dash with slope y\' = f(x, y)"]]',
                   '[[card title="reading a slope field" items="dashes = directions, not curves | a solution flows with the current | one curve per starting point"]]']},
        {"term": "equilibrium", "say":
            "An **equilibrium** is a solution that never moves: a constant where the rate of change "
            "is exactly zero, so a system that starts there stays there forever. You find them by "
            "setting y prime equal to zero and solving. The interesting question is what happens "
            "nearby. If neighbors drift back in, the equilibrium is stable. If they run away, it is "
            "unstable. Here is the trap. An equilibrium existing says nothing about it lasting. A "
            "pencil balanced on its point is at equilibrium too — the sign of the drift on each side "
            "decides.",
         "board": ['[[write text="equilibrium: set y\' = 0 and solve for y"]]',
                   '[[card title="stability test" items="neighbors drift back: stable | neighbors run away: unstable | check the sign of y-prime on each side"]]']},
        {"term": "Euler's method", "say":
            "**Euler's method** is the honest confession that most differential equations have no "
            "formula solution — and the plan for solving them anyway. You stand at a known point, ask "
            "the equation for the slope there, and take one small straight step in that direction. "
            "Then you ask again and step again. String enough steps together and the broken line "
            "shadows the true curve. Smaller steps track it better and cost more steps. Here is the "
            "trap. The slope is only right where you asked, so every step drifts a little, and the "
            "drift compounds.",
         "board": ['[[write text="next y = y + h·f(x, y) ,  h = the step size"]]',
                   '[[card title="one Euler step" items="ask the equation for the slope here | step h in that direction | repeat from the new point"]]']},
        {"term": "eigenvalue", "say":
            "An **eigenvalue** is the growth rate a matrix keeps hidden inside it. For a system of "
            "differential equations, each eigenvalue is an r for which the system has a solution that "
            "grows or shrinks like e to the r t along one special direction, called its eigenvector. "
            "Find the eigenvalues and you know the system's fate: negative ones pull solutions in, "
            "positive ones push them out, complex ones make them spiral. Here is the trap. The "
            "eigenvalue is a number, not a direction. The direction is the eigenvector that comes "
            "with it.",
         "board": ['[[write text="A·v = r·v  →  solution  x(t) = e^(rt)·v"]]',
                   '[[card title="what the eigenvalues say" items="all negative: solutions pulled in | any positive: pushed out | complex: spirals"]]']},
        # --- build gc (2026-08-14): red-list additions for this course. See the
        # change note at the top of this file. Appended, never edited.
        {"term": "complementary", "say":
            "For a linear equation carrying a forcing term on the right, the **complementary** part of the "
            "answer is what you get by setting that right hand side to zero and solving. It carries the "
            "arbitrary constants, while the particular piece added to it answers the forcing. Here is the trap. "
            "Neither piece is the answer by itself, and the starting values are applied only after the two have "
            "been added, never to one of them alone.",
         "board": ['[[write text="y = y_c + y_p       y_c solves the equation with the right side set to 0"]]', '[[card title="assemble, THEN apply" items="set the right side to zero and solve | find a piece that produces the forcing | add them, and only then use the starting values"]]']},
        {"term": "eigenvector", "say":
            "An **eigenvector** is a direction a matrix refuses to turn. Multiply it by the matrix and what "
            "comes back points along the very same line, only stretched or shrunk, and the stretching factor is "
            "its eigenvalue. When that factor is a real number, the solution along this direction simply grows "
            "or decays. Here is the trap. It names a direction, not a number, so any nonzero multiple of it is "
            "the same one, and the number riding with it is the eigenvalue.",
         "board": ['[[write text="A·v = r·v        the arrow v keeps its direction; r is only the stretch"]]']},
        {"term": "inverse transform", "say":
            "Once you have solved in the s domain, the **inverse transform** is the trip home: it takes a "
            "function of s and hands back the function of time it came from. You do it by recognizing standard "
            "pieces in a table, which usually means splitting into partial fractions first, and completing the "
            "square when a quadratic will not factor. Here is the trap. You are reading the table backwards, so "
            "reshape your expression to match an entry rather than hunting for a new rule.",
         "board": ['[[write text="Y(s) = 1/(s² + 4)    gives    y(t) = (1/2) sin(2t)"]]']},
        {"term": "natural frequency", "say":
            "Every mass on a spring has one rhythm it prefers when nothing pushes it and nothing drains it, and "
            "that rhythm is its **natural frequency**. It is set by the stiffness and the mass alone, never by "
            "how hard you started the motion. Here is the trap. Size and rhythm are separate. Pulling the mass "
            "twice as far gives bigger swings at the very same rate, and a little damping slows that rate only "
            "slightly, while heavy damping stops the swinging altogether.",
         "board": ['[[write text="m·y'' + k·y = 0        ω² = k/m        stiffer: faster        heavier: slower"]]']},
        {"term": "predator", "say":
            "In a two species model, the **predator** equation and the prey equation are locked together: the "
            "hunters can grow only while there is enough to eat, and the hunted vanish faster the more hunters "
            "there are. In the classic version the two numbers chase each other around a closed loop in the "
            "phase plane, with the peak in hunters arriving after the peak in prey. Here is the trap. That loop "
            "circles the resting point rather than settling into it.",
         "board": ['[[write text="x\' = a·x − b·x·y        y\' = −c·y + d·x·y        (prey x, hunters y)"]]', '[[card title="reading the loop" items="prey rise first | the hunters follow | hunters overshoot and crash | prey recover, and it repeats"]]']},
        {"term": "repeated root", "say":
            "In a constant coefficient equation, when the characteristic equation hands you the same answer "
            "twice, you have a **repeated root**, and the two solutions you were expecting have collapsed into "
            "one. A single function cannot carry two arbitrary constants, so you build the partner by "
            "multiplying that first solution by t. Here is the trap. Writing the same exponential down twice is "
            "not a second solution. The extra factor of t is what keeps the pair independent.",
         "board": ['[[write text="r = 3, twice        y = C₁e^(3t) + C₂ t e^(3t)"]]']},
        {"term": "standard form", "say":
            "Before computing an integrating factor, put a first order linear equation into **standard form**: "
            "the derivative standing alone with a coefficient of one, the term carrying the unknown function "
            "beside it, and everything else on the other side. Here is the trap. The recipe reads the "
            "coefficient of that unknown function straight off this arrangement. Leave a factor still "
            "multiplying the derivative and the coefficient you pick up is wrong, so every step after it is "
            "wrong too.",
         "board": ['[[write text="a(t)y\' + b(t)y = g(t)        becomes        y\' + p(t)y = q(t)"]]']},
        {"term": "step size", "say":
            "In a numerical method, the **step size** is how far along the horizontal axis you travel before "
            "stopping to ask the equation for a fresh slope. Make it smaller and the broken line hugs the true "
            "curve more closely, at the cost of more arithmetic. Here is the trap. Smaller is not endlessly "
            "better. Rounding error piles up over the extra steps, so beyond some point the answer stops "
            "improving and can quietly get worse.",
         "board": ['[[write text="h = the step size        next y = y + h · f(t, y)"]]', '[[card title="choosing h" items="smaller h — closer to the true curve | smaller h — more steps, more rounding | too small — no gain left"]]']},
    ],
}


def for_course(course: str) -> list:
    """The canonical foundation scripts for a course, in teaching order ([] if none)."""
    return FOUNDATIONS.get(_canon(course), [])


def terms_for_course(course: str) -> list:
    """Just the key terms this course has a canonical introduction for."""
    return [f["term"] for f in for_course(course)]


import re  # noqa: E402 -- kept next to the helpers that use it, below the data


# The invisible tag rule 40(f) asks the tutor to emit whenever he actually delivers
# one of these introductions. The student never sees it (every page's stripTags drops
# any [[...]]); the server reads it and writes the memory row.
LEARNED_TAG_RE = re.compile(
    r'\[\[\s*learned\b[^\]]*?term\s*=\s*"([^"]{1,96})"[^\]]*\]\]', re.I)


def normalize_term(term: str) -> str:
    """The storage key for a term: lowercased and whitespace-collapsed.

    The model types the term back to us inside [[learned term="..."]], so it will
    arrive with stray capitals and spacing. Everything that reads or writes the
    heard-list goes through here so "Pythagorean Theorem" and "pythagorean theorem"
    are the same memory."""
    return " ".join(str(term or "").strip().lower().split())


def known_term(course: str, term: str) -> str:
    """The CANONICAL spelling of `term` in this course, or "" if this course has no
    script for it. Used to reject a [[learned]] tag for something we never wrote,
    so a typo can never silently retire a real introduction."""
    want = normalize_term(term)
    for f in for_course(course):
        if normalize_term(f["term"]) == want:
            return f["term"]
    return ""


def learned_terms_in(course: str, reply: str) -> list:
    """The CANONICAL terms this reply claims to have introduced, from its
    [[learned term="..."]] tags. Deduplicated, order preserved.

    A tag naming something this course has no script for is DROPPED, deliberately:
    the memory row it would write can only cost a student an introduction they still
    need, so an unrecognised name is never worth trusting. Never raises."""
    out = []
    try:
        for raw in LEARNED_TAG_RE.findall(str(reply or "")):
            term = known_term(course, raw)
            if term and term not in out:
                out.append(term)
    except Exception:  # noqa: BLE001
        return out
    return out


# ONE TRUE NAME PER COURSE (build ek, 2026-08-12). The canonical course keys live in
# curriculum.py and this module's content is keyed by those names. The older
# "entrymath"/"basicmath" spellings used to live HERE, which meant a real lesson (which
# runs as "basic") got NOTHING from this module -- see curriculum.py's build-ek note.
# Kept as a local map rather than an import so this stays a dependency-free data module.
_ALIASES = {"entrymath": "entry", "basicmath": "basic"}


def _canon(course):
    """The canonical course key, resolving the legacy spellings. Unknown names pass
    through unchanged so an unrecognised course yields an EMPTY block, never the wrong
    course's content."""
    c = (course or "").strip().lower()
    return _ALIASES.get(c, c)



# -----------------------------------------------------------------------------
# WHICH UNIT DOES A SCRIPT BELONG TO?  (2026-08-14, build gb)
# The library outgrew the prompt. Every script for a course used to travel in EVERY
# prompt, so a student on Geometry unit 1 carried the cone, cylinder and pyramid
# introductions they will not meet for months -- 22,486 characters of geometry, of
# which perhaps 5,000 could be used that day. Adding the 25 missing geometry terms
# (build fz) left 428 characters under ruletests' 180,000 ceiling, and nine courses
# were still owed roughly 120 more terms. Something had to give, and the honest place
# was the part that was never needed rather than the teaching itself.
#
# WHY THIS IS NOT THE THING BUILD cn REVERSED. main.py's build cn note is emphatic
# that a STABLE prompt beats a smaller one: deferring already-HEARD scripts saved
# $0.0005 a turn and cost ~$0.24 every time the prompt shape flipped, and heard-ness
# flips mid-session, twice per refresher. THE UNIT DOES NOT. It is fixed for the whole
# of a lesson, so this filter produces a prompt that is byte-identical turn to turn --
# exactly the property cn was protecting. cn's own note says the mechanism "becomes
# the right answer if the library ever grows to where it does not fit." It has.
#
# The mapping comes from curriculum.py's classifier, which is already the curated,
# per-unit vocabulary the app uses to decide which unit a lesson is in -- so this adds
# no second source of truth to keep in step. It is computed once and cached.
# FAILS OPEN EVERYWHERE: no curriculum module, an unclassifiable term, any exception
# at all, and the script travels verbatim exactly as it does today.
# -----------------------------------------------------------------------------
try:
    import curriculum as _curriculum
except Exception:  # noqa: BLE001 -- filtering is an optimisation, never a dependency
    _curriculum = None

_UNIT_OF = {}


def unit_of(course: str, term: str):
    """The unit a foundation term belongs to, or None when it cannot be placed.
    None means 'always carry it' -- an unplaceable term is never filtered out."""
    key = (course or "", (term or "").lower())
    if key in _UNIT_OF:
        return _UNIT_OF[key]
    u = None
    if _curriculum is not None:
        try:
            u = _curriculum.classify_unit(term, course)[0]
            if not isinstance(u, int) or u < 1:
                u = None
        except Exception:  # noqa: BLE001
            u = None
    _UNIT_OF[key] = u
    return u


def prompt_block(course: str, heard=None, verbatim: bool = True, unit=None) -> str:
    """The prompt section listing this course's canonical introductions.

    `heard` is the set/list of terms THIS student has already been introduced to
    (main.py reads it from the store). It changes nothing about the scripts -- the
    words stay identical so the audio cache still hits on a refresher -- it only
    tells the tutor which ones to ASK about instead of replaying. See rule 40.

    `verbatim` (2026-08-10, build cl) controls whether the FULL text of an
    already-heard script is included. It defaults to True and main.py turns it off for
    the ordinary turns of a returning student, because rule 40 means a heard script is
    not replayed -- it is OFFERED. He only needs the exact words at the moment the
    student takes him up on it, and main.py restores them for that turn. A student who
    has met twelve terms was carrying about nine thousand characters of text he had
    already decided not to say. Terms are still NAMED either way, so he always knows
    what he has taught them; only the wording is deferred, and only for terms he has
    already delivered.

    `unit` (2026-08-14, build gb) is the unit THIS lesson is in. When it is given, only
    the scripts belonging to that unit travel with their full wording; the rest are
    NAMED so the tutor always knows what exists, and their text is left out. Unlike the
    `verbatim` deferral above, the unit is FIXED for a whole lesson, so the prompt stays
    byte-identical turn to turn and the cache is never rebuilt (see the note above
    unit_of, and main.py's build cn note). Pass None -- the default -- and nothing is
    filtered, which is exactly today's behaviour.

    Returns "" when a course has none, so the prompt never grows for nothing."""
    items = for_course(course)
    if not items:
        return ""
    try:
        unit = int(unit) if unit else None
    except (TypeError, ValueError):
        unit = None
    seen = {normalize_term(t) for t in (heard or []) if str(t or "").strip()}
    # build gf (2026-08-14): A HEARD SCRIPT IS NEVER UNIT-FILTERED. ruletests caught this
    # the first time the battery ran against build gb: rule 40 says a term this student has
    # already met is OFFERED, and its exact wording is restored the moment they accept --
    # "remind me what a radius is" can arrive in ANY unit. Filtering those out by unit meant
    # the tutor could not name the offer and could not honour it, so he would have had to
    # paraphrase, which drifts the words every student is supposed to share AND re-bills the
    # audio. Heard scripts always travel; only terms this student has never met are deferred.
    deferred = set()
    if unit:
        for f in items:
            key = normalize_term(f["term"])
            if key in seen:
                continue
            u = unit_of(course, f["term"])
            if u is not None and u != unit:
                deferred.add(key)
    known = [f["term"] for f in items if normalize_term(f["term"]) in seen]
    lines = [
        "",
        "============================================================",
        "📖 CANONICAL FOUNDATION SCRIPTS -- SPEAK THESE VERBATIM",
        "============================================================",
        "Rule 36 says teach the idea before you ask about it. These are the exact words for",
        "this course's foundational terms. When a student meets one of these ideas for the",
        "FIRST time, say the script WORD FOR WORD, and put its board lines up as you say it.",
        "Two reasons, both of which matter:",
        "  1. Every student gets the same careful, correct, complete introduction -- not a",
        "     paraphrase that quietly leaves out the part they needed.",
        "  2. The voice cache is keyed by the exact text, so a script that is spoken",
        "     verbatim is rendered ONCE for the whole platform and is free from then on.",
        "     Re-wording it costs real money and gains nothing.",
        "AFTER the script, teach live as always: your worked example, then their turn.",
        "",
        "★ MARK EVERY INTRODUCTION YOU GIVE. When you deliver one of these scripts -- the",
        "first time OR as a refresher -- end that reply with [[learned term=\"<term>\"]],",
        "spelled exactly as the script names it. The student never sees that tag. It is how",
        "the system remembers next month what you taught today; with no tag, this student",
        "hears the same introduction from scratch on their next visit.",
        "",
    ]
    if known:
        lines += [
            "★ ALREADY INTRODUCED TO THIS STUDENT -- ASK, DO NOT REPLAY (rule 40):",
            "    " + ", ".join(known),
            "  This session's conversation has no trace of it, but you DID teach these to",
            "  this student on an earlier visit. Do not play the script at them again. Name",
            "  the term in one sentence and ask whether they want it again -- \"do you feel",
            "  like you've got a handle on that, or want me to refresh your memory?\" -- then",
            "  stop and let them choose. If they ask for it, say the script WORD FOR WORD",
            "  (same words, same board lines, and it costs nothing to say twice) and tag it",
            "  again. If they say they have it, one sentence and get to work. With the",
            "  youngest students, ask one small concrete question about the term instead of",
            "  asking them to grade their own memory -- see rule 40(e).",
            "",
        ]
    else:
        lines += [
            "This student has not been introduced to ANY of these terms yet, so each one",
            "below is genuinely new to them the first time it comes up.",
            "",
        ]
    if deferred:
        lines += [
            "★ THIS LESSON IS IN UNIT " + str(unit) + ". The scripts written out in full below are",
            "  the ones this unit teaches. These other terms have canonical scripts too, but they",
            "  belong to OTHER units and their wording is not carried today:",
            "    " + ", ".join(sorted(f["term"] for f in items
                                      if normalize_term(f["term"]) in deferred)),
            "  If one of them comes up in passing, say what it means in ONE plain sentence and",
            "  move on -- do NOT attempt the canonical introduction from memory, and do NOT tag",
            "  it with [[learned]]. Its full introduction belongs to the unit that owns it, and",
            "  that unit will give the student the same careful words every other student gets.",
            "",
        ]
    for f in items:
        already = normalize_term(f["term"]) in seen
        if normalize_term(f["term"]) in deferred:
            continue          # named in the list above; the wording belongs to its own unit
        if already and not verbatim:
            # Rule 40: this one is OFFERED, not replayed. He needs the name to make the
            # offer; the wording comes back the moment the student accepts it.
            lines.append(f'--- {f["term"].upper()} ---  [already introduced -- ask first '
                         f'(rule 40). The exact script is restored the moment they ask '
                         f'for it, so offer it freely.]')
            lines.append("")
            continue
        mark = "  [already introduced -- ask first, rule 40]" if already else ""
        lines.append(f'--- {f["term"].upper()} ---{mark}')
        lines.append(f'SAY: {f["say"]}')
        for b in f.get("board", []):
            lines.append(f"BOARD: {b}")
        lines.append("")
    lines.append("============================================================")
    return "\n".join(lines)


# -----------------------------------------------------------------------------
# THE TERM-GAP PROBE (2026-08-14, build gi) -- MEASUREMENT ONLY, IT CHANGES NOTHING.
#
# Jim, 2026-08-14, after a Geometry lesson where the tutor used "right angle" without
# ever saying it means ninety degrees, and he had to stop and ask:
#   "It should have been able to learn from that lesson. It should have said, alright,
#    I got a question about something I was teaching that told me I wasn't being clear,
#    and I'm gonna use that information in the future."
#
# The model's weights cannot learn from a lesson. The SYSTEM can, and this is the part
# that collects the evidence: when a student has to ask what a word means, that question
# is the most honest signal we will ever get that an introduction was missing.
#
# The audit that followed found 145 terms the tutor says out loud with nothing defining
# them, and they have since been written -- but that audit could only find gaps we could
# derive from the code. This finds the ones nobody predicted, from real lessons.
#
# TWO KINDS OF GAP, and they deserve different answers (Jim's own split):
#   "unintroduced" -- we HAVE a script for this term and the tutor used it without
#                     delivering it. That is a rule-36/40 violation, not new information.
#                     It is the class that can eventually be fixed automatically.
#   "no-script"    -- we have no script at all. That is new teaching content: it needs
#                     words written and a voice clip rendered, so a human decides.
#
# WHY IT ONLY MEASURES. Nothing here alters a reply. The retired ensure_board is the
# standing lesson about acting on a guess; and the second class costs real money and is
# spoken verbatim to every student for ever, so it is Jim's call, not a machine's.
#
# PRIVACY: the student's words are never logged. Only the TERM, the course, and which
# kind of gap it is -- the same rule the cost log follows (counts, never text).
# -----------------------------------------------------------------------------
_ASK_PATTERNS = (
    re.compile(r"\bwhat(?:'s| is| are)\s+(?:an?\s+|the\s+)?([a-z][a-z \-']{1,28}?)\s*[?.!]*$", re.I),
    re.compile(r"\bwhat does\s+(?:an?\s+|the\s+)?([a-z][a-z \-']{1,28}?)\s+mean", re.I),
    re.compile(r"\bi\s+(?:do ?n'?t|dont|do not)\s+know what\s+(?:an?\s+|the\s+)?([a-z][a-z \-']{1,28}?)\s+(?:is|are|means)", re.I),
    re.compile(r"\bwhat'?s?\s+(?:an?\s+|the\s+)?([a-z][a-z \-']{1,28}?)\s+again\b", re.I),
)
# Words that are the QUESTION, not the thing being asked about. "what is the answer"
# is a student working, not a student stuck on vocabulary.
_NOT_A_TERM = {
    "it", "that", "this", "the answer", "answer", "next", "the next step", "next step",
    "left", "right", "wrong", "going on", "happening", "up", "the point", "my score",
    "the problem", "problem", "the question", "question", "you", "your name", "we doing",
    "i doing", "the difference", "difference", "more", "less", "first", "last", "again",
}


def term_a_student_asked_about(message: str) -> str:
    """The term a student is asking the meaning of, or "" if they are not asking one.
    Deliberately narrow -- a false hit costs a misleading log line. Never raises."""
    try:
        text = " ".join(str(message or "").split())
        if not text:
            return ""
        for pat in _ASK_PATTERNS:
            m = pat.search(text)
            if not m:
                continue
            term = " ".join(m.group(1).split()).strip(" .,?!'").lower()
            if not term or term in _NOT_A_TERM or len(term) < 3:
                continue
            return term
        return ""
    except Exception:  # noqa: BLE001
        return ""


def term_gap(course: str, student_message: str, last_tutor_message: str = "",
             heard=None):
    """(term, kind) when a student had to ask what a word the tutor just used means,
    else ("", ""). `kind` is "unintroduced" (we have a script and it was not given)
    or "no-script" (nobody has written one). Never raises: any doubt returns nothing."""
    try:
        term = term_a_student_asked_about(student_message)
        if not term:
            return ("", "")
        # It only counts as OUR gap if the tutor actually used the word. A student
        # asking about something from school today is curiosity, not a defect.
        if term not in " ".join(str(last_tutor_message or "").lower().split()):
            return ("", "")
        canon = known_term(course, term)
        if not canon:
            return (term, "no-script")
        if normalize_term(canon) in {normalize_term(t) for t in (heard or [])}:
            return ("", "")          # they were taught it; forgetting is what rule 40 is for
        return (canon, "unintroduced")
    except Exception:  # noqa: BLE001
        return ("", "")


REFRESH_RE = re.compile(
    r"\b(refresh|remind me|say (?:it|that) again|go over (?:it|that) again|one more time|"
    r"i forgot|forgotten|don'?t remember|can'?t remember|what (?:is|was) a\b|"
    r"what does .{0,24} mean|explain (?:it|that) again|not really\b|no,? ?(?:i )?don'?t)\b",
    re.I)
_YES_RE = re.compile(r"^\W{0,3}(yes|yeah|yep|yup|sure|ok|okay|please|yes please|"
                     r"go ahead|i guess|maybe|uh huh|mm ?hm)\b", re.I)


def wants_refresher(student_message: str, last_tutor_message: str = "") -> bool:
    """True when the full wording of an already-heard script must be in this prompt.

    Two ways a student asks. Explicitly -- "remind me what a denominator is" -- or by
    simply accepting the offer rule 40(b) requires him to make, which usually arrives as
    a bare "yes". The bare yes only counts when his previous turn actually offered a
    refresher, which is why the last tutor message is read too. Never raises."""
    try:
        msg = str(student_message or "")
        if REFRESH_RE.search(msg):
            return True
        last = str(last_tutor_message or "").lower()
        offered = ("refresh your memory" in last or "refresh my memory" in last
                   or "got a handle on" in last or "handle on that" in last
                   or "want me to go over" in last)
        return bool(offered and _YES_RE.match(msg.strip()))
    except Exception:  # noqa: BLE001
        return True          # fail OPEN: when unsure, carry the words


# I did no harm and this file is not truncated.

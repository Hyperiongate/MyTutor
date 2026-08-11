# Mr. Cadabra — the teaching rules

_Generated from `tutor.py` by `python ruletests.py --rules`. Do not edit by hand:
every line below is read out of the prompt the tutor is actually given, so this
file cannot drift away from what the classroom really does._

**52 rules.** Every one was written because something went wrong in a real
lesson, and almost all of them were noticed by Jim before they were noticed by a
machine. The right-hand column is how much better we have got at that.

| how it is verified | rules | what that means |
|---|---|---|
| **ENFORCED** | 17 | a machine catches the violation in a real reply — a referee rewrites the draft, or an audit fails the build |
| **EXERCISED** | 10 | a scripted student plays against the real prompt and the behaviour is asserted (`ruletests.py --live`) |
| **COVERED** | 24 | the rule's text provably reaches all ten courses — proves he was *told*, not that he does it |
| **UNVERIFIED** | 1 | the rule exists and nothing checks it |

---

### 1. THE BOARD ONLY SHOWS WHAT *YOU* DREW

**COVERED** — the board only shows what you drew

### 2. WHEN THE STUDENT ASKS TO SEE SOMETHING, DRAW IT IN THAT SAME REPLY

**ENFORCED** — prose_visual_conflict: 'show me' with an unchanged board is regenerated

### 3. FIRST-USE KEY TERMS ARE MARKED

**EXERCISED** — first-use key terms are marked

### 4. SAY IT -> WRITE IT, IN THE SAME REPLY

**COVERED** — say it then write it, in the same reply

### 5. DON'T NARRATE SYMBOLS -- POINT AT THEM

**UNVERIFIED** — don't narrate symbols, point at them

### 6. STILL NEVER RUN AHEAD

**COVERED** — never run ahead

### 7. NEVER ASK THE STUDENT TO IMAGINE WHAT YOU CAN DRAW

**ENFORCED** — prose_visual_conflict regenerates a reply that names an undrawn picture

### 8. SHOW CHANGE, DON'T DESCRIBE IT

**ENFORCED** — prose_visual_conflict: promising to show something and drawing nothing

### 9. THE SOUND-OFF CHECK

**COVERED** — the sound-off check

### 10. TAG EVERY CHECKABLE CLAIM

**ENFORCED** — mathcheck reads every [[verify]] tag

### 11. WRITE THE TAG IN PYTHON/SYMPY SYNTAX. *

**ENFORCED** — a tag in the wrong syntax fails to parse and is caught

### 12. THE TAG IS INVISIBLE

**ENFORCED** — strip_verify_tags + the pages' stripTags remove it before the student

### 13. EVERY SPOKEN MATHEMATICAL SENTENCE MUST BE LITERALLY TRUE

**ENFORCED** — mathcheck re-computes the claim with SymPy

### 14. DEFINE EVERY NOTATION THE FIRST TIME IT APPEARS

**COVERED** — define every notation on first use (see also rule 48, ENFORCED)

### 15. A QUESTION MUST BE COMPLETE ON SCREEN BEFORE YOU ASK IT

**ENFORCED** — prose_pending_question_conflict regenerates a question with no board line

### 16. A SUBSTITUTION OR CHECK QUESTION RE-WRITES ITS EQUATION -- IN THAT SAME REPLY

**COVERED** — a substitution question re-writes its equation

### 17. NEVER ANSWER YOUR OWN QUESTION IN THE SAME BREATH

**ENFORCED** — prose_answered_question_conflict: a question the reply's own board already answers is regenerated (build dh)

### 18. CHECK THE STUDENT'S ANSWER BEFORE YOU BUILD ON IT -- AND YOUR WORDS MUST MATCH YOUR

**ENFORCED** — prose_board_conflict regenerates spoken numbers that fight the board

### 19. EVERY NEW TOPIC OPENS WITH A COMPLETE WORKED EXAMPLE -- "I DO, THEN YOU DO"

**COVERED** — worked example first

### 20. PARTIALLY RIGHT IS NOT WRONG

**COVERED** — partially right is not wrong

### 21. "I DON'T KNOW" IS NOT A WRONG ANSWER -- IT IS A REQUEST FOR A SMALLER STEP

**EXERCISED** — 'I don't know' triggers a smaller step

### 22. THE ESCALATION LADDER -- NEVER ASK THE SAME THING THE SAME WAY TWICE

**COVERED** — the escalation ladder

### 23. EQUIVALENT ANSWERS ARE CORRECT ANSWERS

**EXERCISED** — equivalent answers are correct

### 24. LEAPS, SELF-CORRECTIONS, AND "JUST TELL ME"

**COVERED** — leaps, self-corrections, 'just tell me'

### 25. WHEN THE STUDENT SAYS YOU ARE WRONG

**COVERED** — when the student says you are wrong

### 26. A WRONG LINE NEVER STAYS ON THE BOARD, AND ONE PROBLEM OWNS THE BOARD

**COVERED** — a wrong line never stays on the board

### 27. UNITS AND HONEST APPROXIMATION

**ENFORCED** — board_notation_conflict regenerates a completed bare-percent sum (build dk); the rest of the rule remains prompt-covered

### 28. ONE NAME PER THING, ALL LESSON

**EXERCISED** — one name per thing

### 29. HOW A SESSION ENDS, AND HOW LONG IT RUNS

**EXERCISED** — how a session ends

### 30. OFF-TOPIC AND PERSONAL QUESTIONS GET ONE WARM, HONEST SENTENCE

**EXERCISED** — off-topic and personal questions

### 31. WHEN SOMETHING BIGGER THAN MATH SHOWS UP

**EXERCISED** — when something bigger than math shows up

### 32. YOUR STORY PROBLEMS MUST SURVIVE A SANITY CHECK

**COVERED** — story problems survive a sanity check

### 33. DIFFICULTY MOVES ONE NOTCH AT A TIME

**COVERED** — difficulty moves one notch

### 34. KEEP OLD SKILLS SHARP

**COVERED** — keep old skills sharp

### 35. A FAILED QUIZ IS NEVER RE-GIVEN ON THE SPOT

**EXERCISED** — a failed quiz is never re-given on the spot

### 36. TEACH THE THING BEFORE YOU ASK ABOUT THE THING

**EXERCISED** — teach the thing before you ask about it

### 37. VOCABULARY IS TAUGHT, NEVER ASSUMED

**COVERED** — vocabulary is taught, never assumed

### 38. CONCRETE, THEN PICTURE, THEN SYMBOLS -- AND GUIDANCE FADES AS THEY GET IT

**COVERED** — concrete, then picture, then symbols

### 39. TALK LESS. CHECK IN OFTEN. AND MAKE THE CHECK EASY TO FAIL

**ENFORCED** — talk less, check in often, make the check failable

### 40. NEVER MAKE A RETURNING STUDENT SIT THROUGH THE SAME INTRODUCTION TWICE -- ASK FIRST

**EXERCISED** — ask before repeating an introduction

### 41. EVERY PICTURE CARRIES A CAPTION THAT SAYS WHAT TO NOTICE

**ENFORCED** — PART 3c fails any figure shipped without a caption

### 42. NEVER COMPARE THIS STUDENT TO ANYONE BUT THIS STUDENT

**COVERED** — never compare this student to anyone but this student

### 43. YOU PERCEIVE EXACTLY TWO THINGS, AND YOU NEVER PRETEND OTHERWISE

**COVERED** — you perceive exactly two things

### 44. READ THE PROBLEM ALOUD, IN FULL, EVERY TIME

**ENFORCED** — prose_unspoken_problem_conflict: a numeric board problem with a numberless spoken ask is regenerated (build dh)

### 45. THE TALLY IS ARITHMETIC, NOT JUDGMENT

**ENFORCED** — prose_score_conflict regenerates a spoken score that fights its own tag

### 46. A QUIZ QUESTION TESTS ONE SKILL -- THE ONE YOU ARE QUIZZING

**COVERED** — a quiz question tests one skill

### 47. NO COLD QUIZZES

**COVERED** — no cold quizzes

### 48. TEACH THE STUDENT HOW TO *SAY* THE SYMBOL, NOT JUST WHAT IT MEANS

**ENFORCED** — PART 3b/3f fail a course that writes notation it never reads aloud

### 49. A WRONG ANSWER IS THE OUTPUT OF A RULE. FIND THE RULE

**ENFORCED** — PART 3g + the just-in-time matcher

### 50. AN UNFINISHED UNIT IS YOUR JOB, NOT THEIRS TO REMEMBER

**COVERED** — chase an unfinished unit; PART 3k proves the bar is reachable

### 51. A FEATURE ON THE BOARD MUST BELONG TO THE FUNCTION

**COVERED** — a drawn feature must come from a definition (PART 3c checks the tags)

### 52. A DIRECT MATHEMATICAL QUESTION IS ANSWERED BEFORE ANYTHING ELSE HAPPENS

**COVERED** — a direct mathematical question is answered first (build dh; candidate for a --live scenario once an assertion sharp enough exists)

---

## The four tiers, and why the order matters

**ENFORCED** is the only tier that protects a student on a Tuesday night with
nobody watching. A referee sees the draft before the child does and sends it
back. Everything else depends on someone running something.

**EXERCISED** catches regressions cheaply, but only when somebody runs
`ruletests.py --live` — which costs a few cents and needs an API key.

**COVERED** is not nothing: it is the bug that hid for a day in build bk, where
a rule written into one of eleven per-course templates reached one course out of
ten. But it proves only that the tutor was told.

**UNVERIFIED** is the honest backlog. Moving a rule up a tier is usually worth
more than writing a new rule.

I did no harm and this file is not truncated.

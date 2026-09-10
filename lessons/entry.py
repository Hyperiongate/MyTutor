# =============================================================================
# lessons/entry.py  --  ENTRY-LEVEL MATH: THE AUTHORED LESSONS  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-09-10  BUILD va -- THE WALK-BACK IS SWITCHED ON in seventeen lessons. Their
#               ops draw a picture after a right answer now (see lessonscripts.py's
#               note), and a walk-back nobody can reach is not a fix: every one of these
#               had show_work_on_correct off, so the picture would have existed and
#               never been shown. Units 2 through 7; Units 1, 8 and 9 follow with their
#               own ops. NOT ONE authored sentence in this file changed -- only the flag.
#               ⚠️ 198 new voice lines (about $7): a walk-back is SPOKEN, one line per
#               problem the lesson can ask.
#   2026-09-10  BUILD ux -- THE STARS COME BACK TO THE TRAP BEAT. add-single-digit's
#               teach[1] ends "...until you have touched every star on the board" and
#               its board drew two step lines: the stars were two beats up the feed
#               and, on a phone, off the screen. Same defect Jim flagged in Algebra I
#               ("I had to croll up to see the bar"), found by the same sweep
#               (deixis.py, new this build). Board only -- not one spoken word
#               changed, so not one voice line re-renders.
#   2026-09-09  BUILD uw -- ENTRY-LEVEL UNITS 2-4 TO THE SHAPE (12 lessons). Jim:
#               "Let's get Entry-Level units 2 through 9 on the shape." This is the
#               first of three builds; Units 5-7 and 8-9 follow.
#                 * Unit 2 (adding to 20): adding opens on eight stars in two groups
#                   and the plus and equals signs are introduced on the beat that
#                   reads that picture; doubles on four stars and four more; past ten
#                   counts ON from the bigger number; three numbers are three pieces
#                   of tape joined end to end.
#                 * Unit 3 (taking away): six stars with four crossed off and the
#                   minus sign named there; counting BACK from the bigger number; the
#                   missing part draws the HOP itself on the number line; story
#                   problems teach the WORD that decides the sign.
#                 * Unit 4 (place value): a bundle of ten with four loose ones; the
#                   real hundreds/tens/ones blocks; ten more shows the ones NOT
#                   moving; what a digit is worth finds the place first.
#               ⭐ JIM'S RULING (c), 2026-09-09 -- THE REASON QUESTION. The shape's
#               "say why" beat taps a WRITTEN reason, and Unit 1 skipped it because
#               its students cannot read three options yet. His ruling: Units 2 and 3
#               skip it too; UNIT 4 UP CARRIES IT, where the student is reading tens,
#               hundreds, money and clocks. Options are short, open with "because",
#               and every distractor is plainly false.
#               ⭐ AND THE WALK-BACK. Entry was the only taught course with
#               show_work_on_correct off in all 36 lessons (the other eight run 36 of
#               36). It is ON in the seven of these twelve whose op HAS a worked
#               picture to draw, and off in the five whose op has none (dbe, add3,
#               msp, t10, wor) -- a flag over a missing picture is a flag over
#               nothing. Those five ops are the build doc's list for Jim.
#               ⚠️ GIVEAWAYS FIXED, AND THE AUDIT THAT COULD NOT SEE THEM.
#               take-away-single-digit was demonstrating 5 - 2 and 4 - 1 with both in
#               its own bank; doubles was demonstrating 6+6, 7+7 and 5+5 with all
#               three in its bank. teachaudit reported all of it clean because it
#               reads DIGITS and this course spells its numbers out loud -- see the
#               new wordaudit.py. The take-away demonstrations moved off the bank.
#               doubles and tens-and-ones cannot move: their problem space IS what
#               they teach (the ten doubles; one ten with one to nine ones), like
#               Unit 1's "Counting to 10". Their demonstrations are chosen so a clean
#               three-in-a-row run never meets one.
#               ⚠️ AND SEVEN COUNT-ALONGS CAME BACK OUT. A picture with count="1" and
#               more than twelve things is refused by board.js (OBJ_COUNT_MAX) -- it
#               looks right in the source and does not count on screen. PART 3gw
#               caught all seven; the words do that counting instead.
#               181 new voice lines (21,789 characters, about $5) -- a prewarm IS
#               needed after this push. PART 3ks.
#   2026-09-08  BUILD uj -- ONE FILE PER COURSE. Split out of lessonscripts.py (Jim's
#               housekeeping, second half). Every lesson below is the text that sat in
#               lessonscripts.py, moved whole -- the unit lists keep their names, and
#               the build notes above each unit came with them. ORDER at the bottom is
#               this course's slice of COURSE_ORDER (the teaching order). PURE DATA: no
#               imports, no functions -- the engine (lessonscripts.py) reads
#               lessons.LESSONS and lessons.COURSE_ORDER through lessons/__init__.py.
#               ADDING A LESSON: put it in its unit's list AND in ORDER; the battery's
#               validator, the closure prewarm and the demo pick it up from there.
# =============================================================================
LESSONS = []

# =============================================================================
# THE LESSONS -- Basic Math, Unit 1. Each authored to the research settings; each
# bank is ordered by its difficulty key (the 85%-success ramp).
# =============================================================================
_ENTRY_PILOT = [
    {
        "id": "entry-u2-add-single-digit",
        "course": "entry", "unit": 2,
        "topic": "Adding single-digit numbers",
        "op": "+", "max_value": 10, "a_max": 9, "b_max": 9,
        "symbols": ("plus", "equals"),
        "advance_line": "Three in a row — you've got it! You can add single-digit numbers.",
        "why": [
            ("Why learn to add? Because you put things together all day. Two cookies "
             "on your plate and three more from the jar. Some friends here and some "
             "friends still coming. Adding is how you know how many you have in all.",
             '[[goal text="Adding single-digit numbers"]]'),
        ],
        "picture": [
            ("Here are four stars, and here are four more. Watch them all light up, "
             "and count every single one: one, two, three, four, five, six, seven, "
             "eight. Eight stars in all. Putting two groups together and counting "
             "them all — that is adding.",
             '[[objects emoji="⭐" groups="4" add="4" count="1" caption="four stars and four more — count every one"]]'),
        ],
        "teach": [
            ("That is how adding works, and today both groups are single-digit numbers — "
             "one through nine. Adding has two signs of its very own. Putting "
             "together is written with a plus sign, and we say it plus. How many in "
             "all is written with an equals sign, and we say it equals. Four plus "
             "four equals eight.",
             '[[objects emoji="⭐" groups="4" add="4" count="1" caption="four stars and four more"]][[step eq="4 + 4 = 8"]]'),
            ("Here is the trap. Count every star in both groups, not only the new "
             "ones. Five stars and three more is eight, not three. Start at one, and "
             "keep going until you have touched every star on the board.",
             '[[step eq="5 + 3 = 8 ✓"]][[step eq="3 ✗ that is only the new stars"]][[objects emoji="⭐" groups="5" add="3" count="1" caption="five stars and three more — touch every one"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Six stars, and one more star. "
                        "Count every one: one, two, three, four, five, six, seven. Six "
                        "plus one equals seven.",
                        '[[objects emoji="⭐" groups="6" add="1" count="1" caption="count every star"]][[step eq="6 + 1 = 7"]]'),
             "ask": {'a': 2, 'b': 3, 'op': '+'}},
            {"worked": ("One more together. Seven stars, and one more star. Count them "
                        "all — eight. Seven plus one equals eight.",
                        '[[objects emoji="⭐" groups="7" add="1" count="1" caption="count every star"]][[step eq="7 + 1 = 8"]]'),
             "ask": {'a': 4, 'b': 2, 'op': '+'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "recap": [
            ("So, here it is again. Adding is putting two groups together and counting "
             "how many there are in all. Count every star in both groups, and the last "
             "number you say is your answer.",
             '[[objects emoji="⭐" groups="4" add="4" count="1" caption="four and four more — eight in all"]]'),
            ("And that is how you always know how many you have in all.",
             '[[step eq="4 + 4 = 8"]]'),
        ],
        "bank": [
            {"a": 2, "b": 1, "op": "+"}, {"a": 1, "b": 3, "op": "+"},
            {"a": 2, "b": 2, "op": "+"}, {"a": 3, "b": 2, "op": "+"},
            {"a": 4, "b": 1, "op": "+"}, {"a": 3, "b": 3, "op": "+"},
            {"a": 5, "b": 2, "op": "+"}, {"a": 4, "b": 3, "op": "+"},
            {"a": 6, "b": 2, "op": "+"}, {"a": 5, "b": 4, "op": "+"},
            {"a": 7, "b": 2, "op": "+"}, {"a": 6, "b": 3, "op": "+"},
        ],
    },
    {
        "id": "entry-u3-take-away-single-digit",
        "course": "entry", "unit": 3,
        "topic": "Taking away single-digit numbers",
        "op": "-", "max_value": 10, "a_max": 9, "b_max": 9,
        "symbols": ("minus", "equals"),
        "advance_line": "Three in a row — you've got it! You can take away single-digit numbers.",
        "why": [
            ("Why learn to take away? Because things leave as well as arrive. You eat "
             "some of your grapes. A friend takes two of your cars home. Some of the "
             "balloons fly off. Taking away is how you know how many are left.",
             '[[goal text="Taking away single-digit numbers"]]'),
        ],
        "picture": [
            ("Here are six stars. Watch four of them go away — they are crossed off. "
             "Now count only the ones still standing: one, two. Two stars are left. "
             "Starting with a group, taking some away, and counting what is left — "
             "that is taking away.",
             '[[objects emoji="⭐" groups="6" take="4" caption="start with six — take four away, then count what is left"]]'),
        ],
        "teach": [
            ("That is how taking away works, and it has a sign of its very own. Taking "
             "away is written with a minus sign, and we say it minus. You already know "
             "the equals sign. Six minus four equals two.",
             '[[objects emoji="⭐" groups="6" take="4" caption="six, take four away"]][[step eq="6 − 4 = 2"]]'),
            ("Here is the trap. Your answer is what is LEFT, not what went away. Eight "
             "stars, take two away, and six are left — the answer is six, not two. "
             "Count the ones still standing, never the ones you crossed off.",
             '[[step eq="8 − 2 = 6 ✓"]][[step eq="2 ✗ that is what went away, not what is left"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Seven stars, take three away. "
                        "Count what is still standing: one, two, three, four. Seven "
                        "minus three equals four.",
                        '[[objects emoji="⭐" groups="7" take="3" caption="seven, take three away"]][[step eq="7 − 3 = 4"]]'),
             "ask": {'a': 5, 'b': 2, 'op': '-'}},
            {"worked": ("One more together. Nine stars, take six away. Count what is "
                        "left — three. Nine minus six equals three.",
                        '[[objects emoji="⭐" groups="9" take="6" caption="nine, take six away"]][[step eq="9 − 6 = 3"]]'),
             "ask": {'a': 6, 'b': 1, 'op': '-'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "recap": [
            ("So, here it is again. Taking away starts with a group, sends some of it "
             "away, and counts what is left. The ones you crossed off are gone — only "
             "the ones still standing are your answer.",
             '[[objects emoji="⭐" groups="6" take="4" caption="two are left"]]'),
            ("And that is how you know how many you have left.",
             '[[step eq="6 − 4 = 2"]]'),
        ],
        "bank": [
            {"a": 3, "b": 1, "op": "-"}, {"a": 4, "b": 1, "op": "-"},
            {"a": 4, "b": 2, "op": "-"}, {"a": 5, "b": 1, "op": "-"},
            {"a": 5, "b": 3, "op": "-"}, {"a": 6, "b": 2, "op": "-"},
            {"a": 6, "b": 3, "op": "-"}, {"a": 7, "b": 4, "op": "-"},
            {"a": 8, "b": 3, "op": "-"}, {"a": 8, "b": 5, "op": "-"},
            {"a": 9, "b": 4, "op": "-"}, {"a": 9, "b": 5, "op": "-"},
        ],
    },
    {
        "id": "entry-u2-add-past-ten",
        "course": "entry", "unit": 2,
        "topic": "Adding single-digit numbers past ten",
        "op": "+", "max_value": 20, "a_max": 9, "b_max": 9,
        "symbols": ("plus", "equals"),
        "advance_line": "Three in a row — you've got it! You can add single-digit numbers past ten.",
        "why": [
            ("Why keep adding past ten? Because ten runs out fast. You have ten "
             "fingers and there are twelve eggs in the box. Nine friends in the room "
             "and four more come in. The numbers do not stop at ten, so neither does "
             "adding.",
             '[[goal text="Adding single-digit numbers past ten"]]'),
        ],
        "picture": [
            ("Here are nine stars, and here are four more. You do not have to go back "
             "to one. Start at nine and count on for each new star: ten, eleven, "
             "twelve, thirteen. Nine plus four equals thirteen.",
             '[[objects emoji="⭐" groups="9" add="4" caption="start at nine and count on — ten, eleven, twelve, thirteen"]]'),
        ],
        "teach": [
            ("That is the method, and it has a shortcut. Start with the bigger number "
             "and count on from there — it is fewer numbers to say. Eight plus three: "
             "start at eight, then nine, ten, eleven. Eight plus three equals eleven.",
             '[[objects emoji="⭐" groups="8" add="3" count="1" caption="start at eight — nine, ten, eleven"]][[step eq="8 + 3 = 11"]]'),
            ("Here is the trap. When you count on, do not say the starting number "
             "again. Seven plus five: the first new number is eight, not seven. Say "
             "the starting number in your head, and start counting out loud with the "
             "one after it.",
             '[[step eq="7 + 5 = 12 ✓"]][[step eq="11 ✗ seven was counted twice"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Five stars, and six more. "
                        "Start at the bigger number, six, and count on: seven, eight, "
                        "nine, ten, eleven. Five plus six equals eleven.",
                        '[[objects emoji="⭐" groups="5" add="6" count="1" caption="start at six and count on"]][[step eq="5 + 6 = 11"]]'),
             "ask": {'a': 7, 'b': 6, 'op': '+'}},
            {"worked": ("One more together. Nine stars, and six more. Start at nine and "
                        "count on — ten, eleven, twelve, thirteen, fourteen, fifteen. "
                        "Nine plus six equals fifteen.",
                        '[[objects emoji="⭐" groups="9" add="6" caption="start at nine and count on"]][[step eq="9 + 6 = 15"]]'),
             "ask": {'a': 8, 'b': 6, 'op': '+'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "recap": [
            ("So, here it is again. To add past ten, start at the bigger number and "
             "count on once for each one in the other group. Do not go back to one, "
             "and do not say the starting number twice.",
             '[[objects emoji="⭐" groups="9" add="4" caption="start at nine — ten, eleven, twelve, thirteen"]]'),
            ("And that is how the answers keep going past ten.",
             '[[step eq="9 + 4 = 13"]]'),
        ],
        "bank": [
            {"a": 9, "b": 2, "op": "+"}, {"a": 7, "b": 4, "op": "+"},
            {"a": 8, "b": 4, "op": "+"}, {"a": 9, "b": 3, "op": "+"},
            {"a": 6, "b": 6, "op": "+"}, {"a": 8, "b": 5, "op": "+"},
            {"a": 5, "b": 8, "op": "+"}, {"a": 9, "b": 5, "op": "+"},
            {"a": 8, "b": 7, "op": "+"}, {"a": 7, "b": 8, "op": "+"},
            {"a": 9, "b": 7, "op": "+"}, {"a": 9, "b": 8, "op": "+"},
        ],
    },
    {
        "id": "entry-u3-take-away-bigger",
        "course": "entry", "unit": 3,
        "topic": "Taking away from bigger numbers",
        "op": "-", "max_value": 20, "a_max": 19, "b_max": 9,
        "symbols": ("minus", "equals"),
        "advance_line": "Three in a row — you've got it! You can take away from bigger numbers.",
        "why": [
            ("Why take away from bigger numbers? Because the numbers you meet get "
             "bigger. Eighteen stickers on the sheet and you use nine. Fifteen "
             "minutes of playtime and five have gone. The counting back works the "
             "same — there is just more to count back from.",
             '[[goal text="Taking away from bigger numbers"]]'),
        ],
        "picture": [
            ("Here are thirteen stars, and five of them are crossed off. You do not "
             "have to count all the way from one. Start at thirteen and count back "
             "once for each star that went: twelve, eleven, ten, nine, eight. "
             "Thirteen minus five equals eight.",
             '[[objects emoji="⭐" groups="13" take="5" caption="start at thirteen and count back — twelve, eleven, ten, nine, eight"]]'),
        ],
        "teach": [
            ("That is the method: start at the big number and count back once for each "
             "one you take away. Eleven minus three. Start at eleven, then ten, nine, "
             "eight. Eleven minus three equals eight. It works for any take away, "
             "however big the start.",
             '[[objects emoji="⭐" groups="11" take="3" caption="start at eleven — ten, nine, eight"]][[step eq="11 − 3 = 8"]]'),
            ("Here is the trap. When you count back, do not say the starting number as "
             "one of your counts. Sixteen minus three: the first number you say is "
             "fifteen, not sixteen. Hold the start in your head, and begin counting "
             "with the one below it.",
             '[[step eq="16 − 3 = 13 ✓"]][[step eq="14 ✗ sixteen was counted as one of the three"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Twelve stars, take four away. "
                        "Count back from twelve: eleven, ten, nine, eight. Twelve minus "
                        "four equals eight.",
                        '[[objects emoji="⭐" groups="12" take="4" caption="start at twelve and count back"]][[step eq="12 − 4 = 8"]]'),
             "ask": {'a': 12, 'b': 3, 'op': '-'}},
            {"worked": ("One more together. Fifteen stars, take six away. Count back "
                        "from fifteen — nine. Fifteen minus six equals nine.",
                        '[[objects emoji="⭐" groups="15" take="6" caption="start at fifteen and count back"]][[step eq="15 − 6 = 9"]]'),
             "ask": {'a': 14, 'b': 5, 'op': '-'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "recap": [
            ("So, here it is again. Start at the bigger number and count back once for "
             "each one taken away — and never count the starting number itself.",
             '[[objects emoji="⭐" groups="13" take="5" caption="thirteen, count back five — eight are left"]]'),
            ("And that is taking away, however big the number you start with.",
             '[[step eq="13 − 5 = 8"]]'),
        ],
        "bank": [
            {"a": 11, "b": 2, "op": "-"}, {"a": 11, "b": 4, "op": "-"},
            {"a": 12, "b": 5, "op": "-"}, {"a": 13, "b": 4, "op": "-"},
            {"a": 13, "b": 6, "op": "-"}, {"a": 14, "b": 6, "op": "-"},
            {"a": 15, "b": 7, "op": "-"}, {"a": 15, "b": 8, "op": "-"},
            {"a": 16, "b": 7, "op": "-"}, {"a": 17, "b": 8, "op": "-"},
            {"a": 18, "b": 9, "op": "-"}, {"a": 19, "b": 9, "op": "-"},
        ],
    },
    {
        "id": "entry-u4-tens-and-ones",
        "course": "entry", "unit": 4,
        "topic": "Tens and ones",
        "op": "t", "max_value": 19, "a_max": 1, "b_max": 9,
        "symbols": ("ten", "ones"),
        "advance_line": "Three in a row — you've got it! You know your tens and ones.",
        "why": [
            ("Why learn tens and ones? Because counting one at a time gets slow. Nobody "
             "counts a box of eggs one by one — they see two rows of six. Numbers are "
             "packed the same way: in tens, with the leftovers beside them. That is "
             "what the two digits are telling you.",
             '[[goal text="Tens and ones"]]'),
        ],
        "picture": [
            ("Here is one bundle of ten stars, and four loose ones beside it. You do "
             "not count the bundle — you know it is ten. Then count on for the loose "
             "ones: eleven, twelve, thirteen, fourteen. One ten and four ones is "
             "fourteen.",
             '[[objects emoji="⭐" groups="10" add="4" caption="one bundle of ten, and four loose ones"]]'),
        ],
        "teach": [
            ("That is the rule, and it is written into the number itself. In fourteen, "
             "the first digit counts the TENS and the second digit counts the ONES. "
             "One ten, four ones. The two digits are not just marks — each one says "
             "how many of its own kind there are.",
             '[[objects emoji="⭐" groups="10" add="4" caption="1 ten and 4 ones"]][[step eq="14 = 1 ten and 4 ones"]]'),
            ("Here is the trap. The order of the digits is the whole meaning. One ten "
             "and nine ones is nineteen, not ninety-one. The tens digit goes first, "
             "always, because a ten is the bigger bundle.",
             '[[step eq="1 ten and 9 ones = 19 ✓"]][[step eq="91 ✗ the digits were swapped"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. One ten and seven ones. Start "
                        "at ten and count the loose ones on: eleven, twelve, thirteen, "
                        "fourteen, fifteen, sixteen, seventeen. One ten and seven ones "
                        "is seventeen.",
                        '[[objects emoji="⭐" groups="10" add="7" caption="one ten and seven ones"]][[step eq="1 ten and 7 ones = 17"]]'),
             "ask": {'a': 1, 'b': 2, 'op': 't'}},
            {"worked": ("One more together. One ten and eight ones. Count on from ten — "
                        "eighteen. One ten and eight ones is eighteen.",
                        '[[objects emoji="⭐" groups="10" add="8" caption="one ten and eight ones"]][[step eq="1 ten and 8 ones = 18"]]'),
             "ask": {'a': 1, 'b': 5, 'op': 't'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. One ten and four "
                       "ones is fourteen. Tap the reason why."),
            "choices": ("because the first digit counts tens and the second counts ones | "
                        "because the digits are written in the order you say them | "
                        "because both digits are worth the same amount"),
            "answer": "because the first digit counts tens and the second counts ones",
            "board": '[[objects emoji="⭐" groups="10" add="4" caption="one ten, four ones"]][[step eq="14 = 1 ten and 4 ones"]]',
        },
        "recap": [
            ("So, here it is again. A two-digit number is bundles of ten and the loose "
             "ones left over. The first digit counts the tens, the second counts the "
             "ones, and swapping the two digits is a different number entirely.",
             '[[objects emoji="⭐" groups="10" add="4" caption="one ten and four ones — fourteen"]]'),
            ("And that is what the two digits have been telling you all along.",
             '[[step eq="14 = 1 ten and 4 ones"]]'),
        ],
        "bank": [
            {"a": 1, "b": 1, "op": "t"}, {"a": 1, "b": 3, "op": "t"},
            {"a": 1, "b": 4, "op": "t"}, {"a": 1, "b": 6, "op": "t"},
            {"a": 1, "b": 7, "op": "t"}, {"a": 1, "b": 8, "op": "t"},
            {"a": 1, "b": 9, "op": "t"},
        ],
    },
    {
        "id": "entry-u5-add-with-carrying",
        "course": "entry", "unit": 5,
        "topic": "Adding with carrying",
        "op": "+", "max_value": 99, "carry": True,
        "levels": ("abstract",),   # like lesson 6: stars do not help at this size
        "symbols": ("carry", "plus", "equals"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can carry like a pro."),
        "teach": [
            ("Today we are learning to carry. Sometimes when we add, the ones add "
             "up to over nine. When that happens, we write the ones digit and "
             "carry one ten over to the tens.",
             '[[goal text="Adding with carrying"]]'),
            ("Watch me add 27 plus 15. Ones first: 7 plus 5 equals 12. Twelve is "
             "over nine — so we write the 2 and carry one ten. Tens: 2 plus 1 "
             "equals 3, plus the carried one equals 4. So 27 plus 15 equals 42.",
             '[[step eq="27 + 15"]][[step eq="ones: 7 + 5 = 12"]]'
             '[[step eq="write 2, carry 1"]][[step eq="tens: 2 + 1 + 1 = 4"]]'
             '[[step eq="27 + 15 = 42"]]'),
            ("One more, watch. 38 plus 24. Ones: 8 plus 4 equals 12 — over nine, "
             "write the 2, carry one ten. Tens: 3 plus 2 equals 5, plus the "
             "carried one equals 6. So 38 plus 24 equals 62.",
             '[[step eq="38 + 24"]][[step eq="ones: 8 + 4 = 12"]]'
             '[[step eq="write 2, carry 1"]][[step eq="tens: 3 + 2 + 1 = 6"]]'
             '[[step eq="38 + 24 = 62"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 46 plus 17. Ones: 6 plus "
                        "7 equals 13 — over nine, write the 3, carry one ten. "
                        "Tens: 4 plus 1 plus the carried one equals 6. So 46 plus "
                        "17 equals 63.",
                        '[[step eq="46 + 17"]][[step eq="ones: 6 + 7 = 13"]]'
                        '[[step eq="write 3, carry 1"]][[step eq="tens: 4 + 1 + 1 = 6"]]'
                        '[[step eq="46 + 17 = 63"]]'),
             "ask": {"a": 45, "b": 17, "op": "+"}},
            {"worked": ("One more together. 29 plus 35. Ones: 9 plus 5 equals 14 "
                        "— over nine, write the 4, carry one ten. Tens: 2 plus 3 "
                        "plus the carried one equals 6. So 29 plus 35 equals 64.",
                        '[[step eq="29 + 35"]][[step eq="ones: 9 + 5 = 14"]]'
                        '[[step eq="write 4, carry 1"]][[step eq="tens: 2 + 3 + 1 = 6"]]'
                        '[[step eq="29 + 35 = 64"]]'),
             "ask": {"a": 28, "b": 34, "op": "+"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        # (va) the walk-back is ON: this lesson's op draws a picture after a
        # right answer now, and a walk-back nobody can reach is not a fix.
        "show_work_on_correct": True,
        "bank": [
            {"a": 15, "b": 16, "op": "+"}, {"a": 18, "b": 13, "op": "+"},
            {"a": 24, "b": 17, "op": "+"}, {"a": 26, "b": 15, "op": "+"},
            {"a": 28, "b": 16, "op": "+"}, {"a": 35, "b": 17, "op": "+"},
            {"a": 36, "b": 18, "op": "+"}, {"a": 45, "b": 19, "op": "+"},
            {"a": 47, "b": 26, "op": "+"}, {"a": 56, "b": 27, "op": "+"},
            {"a": 58, "b": 25, "op": "+"}, {"a": 67, "b": 26, "op": "+"},
        ],
    },
    {
        "id": "entry-u5-add-two-digit-no-carry",
        "course": "entry", "unit": 5,
        "topic": "Adding two-digit numbers",
        "op": "+", "max_value": 99, "no_carry": True,
        "levels": ("abstract",),   # dropping to counting 37 stars would not be help
        "symbols": ("plus", "equals"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can add two-digit numbers."),
        "teach": [
            ("Today we are adding two-digit numbers. A two-digit number has a "
             "tens digit and a ones digit. We add the ones first, then the tens.",
             '[[goal text="Adding two-digit numbers"]]'),
            ("Watch me add 23 plus 14. First the ones: 3 plus 4 equals 7. Then "
             "the tens: 2 tens plus 1 ten equals 3 tens. So 23 plus 14 equals 37.",
             '[[step eq="23 + 14"]][[step eq="ones: 3 + 4 = 7"]]'
             '[[step eq="tens: 2 + 1 = 3"]][[step eq="23 + 14 = 37"]]'),
            ("One more, watch. 31 plus 25. Ones: 1 plus 5 equals 6. Tens: 3 plus "
             "2 equals 5. So 31 plus 25 equals 56.",
             '[[step eq="31 + 25"]][[step eq="ones: 1 + 5 = 6"]]'
             '[[step eq="tens: 3 + 2 = 5"]][[step eq="31 + 25 = 56"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 42 plus 16. Ones: 2 plus "
                        "6 equals 8. Tens: 4 plus 1 equals 5. So 42 plus 16 "
                        "equals 58.",
                        '[[step eq="42 + 16"]][[step eq="ones: 2 + 6 = 8"]]'
                        '[[step eq="tens: 4 + 1 = 5"]][[step eq="42 + 16 = 58"]]'),
             "ask": {"a": 42, "b": 13, "op": "+"}},
            {"worked": ("One more together. 34 plus 22. Ones: 4 plus 2 equals 6. "
                        "Tens: 3 plus 2 equals 5. So 34 plus 22 equals 56.",
                        '[[step eq="34 + 22"]][[step eq="ones: 4 + 2 = 6"]]'
                        '[[step eq="tens: 3 + 2 = 5"]][[step eq="34 + 22 = 56"]]'),
             "ask": {"a": 51, "b": 24, "op": "+"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        # (va) the walk-back is ON: this lesson's op draws a picture after a
        # right answer now, and a walk-back nobody can reach is not a fix.
        "show_work_on_correct": True,
        "bank": [
            {"a": 12, "b": 13, "op": "+"}, {"a": 21, "b": 14, "op": "+"},
            {"a": 23, "b": 15, "op": "+"}, {"a": 32, "b": 16, "op": "+"},
            {"a": 41, "b": 17, "op": "+"}, {"a": 33, "b": 26, "op": "+"},
            {"a": 44, "b": 23, "op": "+"}, {"a": 52, "b": 25, "op": "+"},
            {"a": 63, "b": 21, "op": "+"}, {"a": 54, "b": 33, "op": "+"},
            {"a": 62, "b": 34, "op": "+"}, {"a": 71, "b": 26, "op": "+"},
        ],
    },
]
LESSONS.extend(_ENTRY_PILOT)
    # ===================== (pg, 2026-08-27) ENTRY FILLS ITS UNITS ================
    # Sixteen lessons so that Entry-Level Math is nine units of four like every
    # other course. Until now a five-year-old who reached "which is bigger" or
    # "making change" dropped out of the authored lane into the live one and waited
    # seconds per sentence -- the worst possible place for the app to be slow.
    # House rules followed exactly: three teach beats (picture, worked, trap), two
    # worked pairs, a ten-problem bank, every sentence short enough to hear.
    # ============ (ph, 2026-08-28) THE LAST EIGHT -- THE COURSE IS WHOLE ========
    # Basic was short seven and Pre-Algebra one. With these, every one of the ten
    # courses is nine units of four, and there is no topic anywhere in the
    # curriculum that drops a child onto the live lane for want of a script.
_ENTRY_MORE = [
    {
        "id": "entry-u6-take-away-two-digit", "course": "entry", "unit": 6,
        "topic": "Taking away two-digit numbers", "op": "s2d", "max_value": 99,
        "levels": ("abstract",), "symbols": ("column",),
        "advance_line": "Three in a row — you've got it! You can take away two-digit numbers.",
        "teach": [
            ("Taking away two-digit numbers works column by column, the same as "
             "adding. Start on the right. Ones first, then tens. Today every ones "
             "digit on top is big enough, so nothing needs regrouping.",
             '[[goal text="Taking away two-digit numbers"]]'
             '[[step eq="58 − 23 = ?"]]'),
            ("Watch me take 23 away from 58. Ones: 8 take away 3 equals 5. Tens: 5 "
             "take away 2 equals 3. So 58 take away 23 equals 35.",
             '[[step eq="ones: 8 − 3 = 5"]]'
             '[[step eq="tens: 5 − 2 = 3"]]'
             '[[step eq="58 − 23 = 35"]]'),
            ("Here is the trap. Taking away has a direction. The top number goes "
             "first every time. In the ones column of 58 take away 23 it is 8 take "
             "away 3, never 3 take away 8.",
             '[[step eq="58 − 23 = 35 ✓"]]'
             '[[step eq="the ones are 8 − 3, not 3 − 8"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 76 take away 42. Ones: 6 "
                        "take away 2 equals 4. Tens: 7 take away 4 equals 3. That "
                        "is 34.",
                        '[[step eq="76 − 42 = 34"]]'),
             "ask": {"a": 89, "b": 35, "op": "s2d"}},
            {"worked": ("One more together. 67 take away 25. Ones: 7 take away 5 "
                        "equals 2. Tens: 6 take away 2 equals 4. That is 42.",
                        '[[step eq="67 − 25 = 42"]]'),
             "ask": {"a": 95, "b": 61, "op": "s2d"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        # (va) the walk-back is ON: this lesson's op draws a picture after a
        # right answer now, and a walk-back nobody can reach is not a fix.
        "show_work_on_correct": True,
        "bank": [{"a": 20, "b": 10, "op": "s2d"}, {"a": 27, "b": 14, "op": "s2d"}, {"a": 30, "b": 10, "op": "s2d"}, {"a": 76, "b": 53, "op": "s2d"}, {"a": 95, "b": 65, "op": "s2d"}, {"a": 56, "b": 20, "op": "s2d"}, {"a": 94, "b": 51, "op": "s2d"}, {"a": 64, "b": 11, "op": "s2d"}, {"a": 85, "b": 21, "op": "s2d"}, {"a": 99, "b": 10, "op": "s2d"}],
    },
    {
        "id": "entry-u6-take-away-three-digit", "course": "entry", "unit": 6,
        "topic": "Taking away three-digit numbers", "op": "s3d", "max_value": 999,
        "levels": ("abstract",), "symbols": ("column",),
        "advance_line": "Three in a row — you've got it! You can take away three-digit numbers.",
        "teach": [
            ("Three columns now instead of two, and not one new idea. Ones first, "
             "then tens, then hundreds, always starting on the right.",
             '[[goal text="Taking away three-digit numbers"]]'
             '[[step eq="876 − 321 = ?"]]'),
            ("Watch me take 321 away from 876. Ones: 6 take away 1 equals 5. Tens: "
             "7 take away 2 equals 5. Hundreds: 8 take away 3 equals 5. So 876 "
             "take away 321 equals 555.",
             '[[step eq="ones: 6 − 1 = 5"]]'
             '[[step eq="tens: 7 − 2 = 5"]]'
             '[[step eq="hundreds: 8 − 3 = 5"]]'
             '[[step eq="876 − 321 = 555"]]'),
            ("Here is the trap, and it is a quiet one. Do not skip a column just "
             "because it looks easy. Every column gets worked, even one where the "
             "bottom digit is 0, because its answer still has to be written down.",
             '[[step eq="876 − 321 = 555 ✓"]]'
             '[[step eq="a skipped column leaves a hole in the answer"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 597 take away 243. Ones: "
                        "7 take away 3 equals 4. Tens: 9 take away 4 equals 5. "
                        "Hundreds: 5 take away 2 equals 3. That is 354.",
                        '[[step eq="597 − 243 = 354"]]'),
             "ask": {"a": 685, "b": 342, "op": "s3d"}},
            {"worked": ("One more together. 748 take away 216. Ones: 8 take away 6 "
                        "equals 2. Tens: 4 take away 1 equals 3. Hundreds: 7 take "
                        "away 2 equals 5. That is 532.",
                        '[[step eq="748 − 216 = 532"]]'),
             "ask": {"a": 969, "b": 427, "op": "s3d"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        # (va) the walk-back is ON: this lesson's op draws a picture after a
        # right answer now, and a walk-back nobody can reach is not a fix.
        "show_work_on_correct": True,
        "bank": [{"a": 201, "b": 200, "op": "s3d"}, {"a": 347, "b": 306, "op": "s3d"}, {"a": 532, "b": 420, "op": "s3d"}, {"a": 374, "b": 211, "op": "s3d"}, {"a": 831, "b": 600, "op": "s3d"}, {"a": 958, "b": 646, "op": "s3d"}, {"a": 906, "b": 504, "op": "s3d"}, {"a": 713, "b": 211, "op": "s3d"}, {"a": 823, "b": 202, "op": "s3d"}, {"a": 999, "b": 100, "op": "s3d"}],
    },
    {
        "id": "entry-u6-checking-by-adding-back", "course": "entry", "unit": 6,
        "topic": "Checking by adding back", "op": "chk", "max_value": 99,
        "levels": ("abstract",), "symbols": ("check",),
        "advance_line": "Three in a row — you've got it! You can check your own answer.",
        "teach": [
            ("Here is something you can do that nobody has to mark for you. You "
             "can check a take away yourself. Adding and taking away undo each "
             "other, so adding your answer back should land on the number you "
             "started with.",
             '[[goal text="Checking by adding back"]]'
             '[[step eq="58 − 23 = 35, so 35 + 23 should be 58"]]'),
            ("Watch me. Someone worked out 58 take away 23 and got 35. Add the "
             "answer back: 35 plus 23 equals 58. That is exactly where we started, "
             "so the take away was right.",
             '[[step eq="35 + 23 = 58 ✓ back where we started"]]'),
            ("Here is the trap. Add the ANSWER to the number you took away. Do not "
             "add the two numbers from the question. In 58 take away 23, the check "
             "is 35 plus 23, not 58 plus 23.",
             '[[step eq="35 + 23 = 58 ✓"]]'
             '[[step eq="81 ✗ that is 58 + 23, the wrong pair"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 74 take away 31 gave 43. "
                        "Check it: 43 plus 31 equals 74. Back where we started.",
                        '[[step eq="43 + 31 = 74"]]'),
             "ask": {"a": 66, "b": 24, "op": "chk"}},
            {"worked": ("One more together. 92 take away 47 gave 45. Check it: 45 "
                        "plus 47 equals 92.",
                        '[[step eq="45 + 47 = 92"]]'),
             "ask": {"a": 83, "b": 39, "op": "chk"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        # (va) the walk-back is ON: this lesson's op draws a picture after a
        # right answer now, and a walk-back nobody can reach is not a fix.
        "show_work_on_correct": True,
        "bank": [{"a": 20, "b": 10, "op": "chk"}, {"a": 41, "b": 30, "op": "chk"}, {"a": 53, "b": 32, "op": "chk"}, {"a": 62, "b": 49, "op": "chk"}, {"a": 70, "b": 45, "op": "chk"}, {"a": 77, "b": 43, "op": "chk"}, {"a": 83, "b": 66, "op": "chk"}, {"a": 89, "b": 53, "op": "chk"}, {"a": 94, "b": 88, "op": "chk"}, {"a": 99, "b": 98, "op": "chk"}],
    },
    {
        "id": "entry-u7-dimes-and-pennies", "course": "entry", "unit": 7,
        "topic": "Counting dimes and pennies", "op": "m", "max_value": 99,
        "levels": ("abstract",), "symbols": ("dime", "cent"),
        "advance_line": "Three in a row — you've got it! You can count dimes and pennies.",
        "teach": [
            ("You can count nickels by five. A penny is one cent, and a dime is "
             "worth 10 cents. Dimes are counted by ten, and counting by ten is "
             "the easiest count there is.",
             '[[goal text="Dimes and pennies"]]'
             '[[step eq="1 dime = 10 cents"]]'),
            ("Watch me count 3 dimes and 4 pennies. Dimes first, count by ten: 10, "
             "20, 30. Then the pennies, counting on: 31, 32, 33, 34. That is 34 "
             "cents.",
             '[[step eq="3 dimes = 30 cents"]]'
             '[[step eq="30 + 4 pennies = 34 cents"]]'),
            ("Here is the trap. Do not count a dime as one. It is one coin, but it "
             "is worth ten cents. Count the coins that are worth more first, then "
             "count the pennies on the end.",
             '[[step eq="3 dimes 4 pennies = 34 cents ✓"]]'
             '[[step eq="7 ✗ that is the coins counted, not the cents"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 2 dimes and 5 pennies. By "
                        "ten: 10, 20. Then on: 21, 22, 23, 24, 25. That is 25 cents.",
                        '[[step eq="2 dimes + 5 pennies = 25 cents"]]'),
             "ask": {"a": 4, "b": 3, "op": "m"}},
            {"worked": ("One more together. 5 dimes and 2 pennies. By ten: 10, 20, "
                        "30, 40, 50. Then 51, 52. That is 52 cents.",
                        '[[step eq="5 dimes + 2 pennies = 52 cents"]]'),
             "ask": {"a": 6, "b": 8, "op": "m"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        # (va) the walk-back is ON: this lesson's op draws a picture after a
        # right answer now, and a walk-back nobody can reach is not a fix.
        "show_work_on_correct": True,
        "bank": [{"a": 1, "b": 1, "op": "m"}, {"a": 2, "b": 1, "op": "m"}, {"a": 3, "b": 1, "op": "m"}, {"a": 4, "b": 1, "op": "m"}, {"a": 5, "b": 1, "op": "m"}, {"a": 5, "b": 9, "op": "m"}, {"a": 6, "b": 9, "op": "m"}, {"a": 7, "b": 9, "op": "m"}, {"a": 8, "b": 9, "op": "m"}, {"a": 9, "b": 9, "op": "m"}],
    },
    {
        "id": "entry-u7-quarters", "course": "entry", "unit": 7,
        "topic": "Counting quarters", "op": "qtr", "max_value": 109,
        "levels": ("abstract",), "symbols": ("quarter",),
        "advance_line": "Three in a row — you've got it! You can count quarters.",
        "teach": [
            ("A quarter is worth 25 cents. It is the biggest coin you will count "
             "here, and four of them make one dollar, which is 100 cents.",
             '[[goal text="Quarters"]]'
             '[[step eq="1 quarter = 25 cents"]]'),
            ("Watch me count 3 quarters and 4 pennies. Quarters first, counting by "
             "twenty-five: 25, 50, 75. Then the pennies on the end: 76, 77, 78, "
             "79. That is 79 cents.",
             '[[step eq="3 quarters = 75 cents"]]'
             '[[step eq="75 + 4 pennies = 79 cents"]]'),
            ("Here is the trap. Two quarters is 50 cents, not 2 cents and not 20 "
             "cents. Count quarters in jumps of twenty-five, and say each jump out "
             "loud: twenty-five, fifty, seventy-five, one hundred.",
             '[[step eq="25, 50, 75, 100 — the four quarters"]]'
             '[[step eq="3 quarters 4 pennies = 79 cents ✓"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 2 quarters and 3 pennies. "
                        "25, 50. Then 51, 52, 53. That is 53 cents.",
                        '[[step eq="2 quarters + 3 pennies = 53 cents"]]'),
             "ask": {"a": 1, "b": 6, "op": "qtr"}},
            {"worked": ("One more together. 4 quarters and 2 pennies. 25, 50, 75, "
                        "100. Then 101, 102. That is 102 cents.",
                        '[[step eq="4 quarters + 2 pennies = 102 cents"]]'),
             "ask": {"a": 3, "b": 5, "op": "qtr"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        # (va) the walk-back is ON: this lesson's op draws a picture after a
        # right answer now, and a walk-back nobody can reach is not a fix.
        "show_work_on_correct": True,
        "bank": [{"a": 1, "b": 1, "op": "qtr"}, {"a": 1, "b": 5, "op": "qtr"}, {"a": 1, "b": 9, "op": "qtr"}, {"a": 2, "b": 4, "op": "qtr"}, {"a": 2, "b": 8, "op": "qtr"}, {"a": 3, "b": 2, "op": "qtr"}, {"a": 3, "b": 6, "op": "qtr"}, {"a": 4, "b": 1, "op": "qtr"}, {"a": 4, "b": 5, "op": "qtr"}, {"a": 4, "b": 9, "op": "qtr"}],
    },
    {
        "id": "entry-u7-making-change", "course": "entry", "unit": 7,
        "topic": "Making change", "op": "chg", "max_value": 100,
        "levels": ("abstract",), "symbols": ("change",),
        "advance_line": "Three in a row — you've got it! You can work out the change.",
        "teach": [
            ("When you pay with more than a thing costs, you get change. Change is "
             "what is left of your money after the price has been taken away.",
             '[[goal text="Making change"]]'
             '[[step eq="you pay 50 − it costs 35 = ? change"]]'),
            ("Watch me. A toy costs 35 cents and you pay 50 cents. Take the price "
             "away from what you paid: 50 take away 35 equals 15. Your change is "
             "15 cents.",
             '[[step eq="50 − 35 = 15 cents change"]]'),
            ("Here is the trap. Do not add the two amounts. You are not spending "
             "85 cents. The change is always SMALLER than what you handed over, so "
             "if your answer is bigger, something has gone wrong.",
             '[[step eq="50 − 35 = 15 ✓"]]'
             '[[step eq="85 ✗ that is the two amounts added"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. A sticker costs 18 cents "
                        "and you pay 25 cents. 25 take away 18 equals 7 cents "
                        "change.",
                        '[[step eq="25 − 18 = 7 cents change"]]'),
             "ask": {"a": 50, "b": 20, "op": "chg"}},
            {"worked": ("One more together. A pencil costs 60 cents and you pay "
                        "100 cents. 100 take away 60 equals 40 cents change.",
                        '[[step eq="100 − 60 = 40 cents change"]]'),
             "ask": {"a": 100, "b": 45, "op": "chg"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        # (va) the walk-back is ON: this lesson's op draws a picture after a
        # right answer now, and a walk-back nobody can reach is not a fix.
        "show_work_on_correct": True,
        "bank": [{"a": 25, "b": 24, "op": "chg"}, {"a": 25, "b": 18, "op": "chg"}, {"a": 100, "b": 88, "op": "chg"}, {"a": 100, "b": 82, "op": "chg"}, {"a": 100, "b": 74, "op": "chg"}, {"a": 50, "b": 15, "op": "chg"}, {"a": 50, "b": 6, "op": "chg"}, {"a": 100, "b": 40, "op": "chg"}, {"a": 100, "b": 23, "op": "chg"}, {"a": 100, "b": 5, "op": "chg"}],
    },
    {
        "id": "entry-u4-hundreds-tens-and-ones", "course": "entry", "unit": 4,
        "topic": "Hundreds, tens and ones", "op": "pv", "max_value": 999,
        "levels": ("abstract",), "symbols": ("hundred", "digit"),
        "advance_line": "Three in a row — you've got it! You can read hundreds, tens and ones.",
        "why": [
            ("Why go up to hundreds? Because the world does not stop at ninety-nine. "
             "There are hundreds of pages in a book, hundreds of students in a school, "
             "hundreds of pennies in a jar. The same bundling keeps going — ten tens "
             "become one hundred.",
             '[[goal text="Hundreds, tens and ones"]]'),
        ],
        "picture": [
            ("Here are the blocks for three hundred forty-six: three big hundred "
             "squares, four ten-sticks, and six single ones. Three places, each with "
             "its own size of block, biggest on the left. That is exactly what the "
             "three digits are counting.",
             '[[placevalue h="3" t="4" o="6" caption="3 hundreds, 4 tens and 6 ones — the blocks behind 346"]]'),
        ],
        "teach": [
            ("That is the rule: hundreds, then tens, then ones, always in that order. "
             "Say the hundreds first — three hundred — then the tens and ones together "
             "— forty-six. Three hundred forty-six. Each digit counts its own place, "
             "and each place is worth ten of the place on its right.",
             '[[placevalue h="3" t="4" o="6" caption="biggest place first"]][[step eq="300 + 40 + 6 = 346"]]'),
            ("Here is the trap. Read the digits left to right, in the order they "
             "stand. Three hundreds, four tens and six ones is three hundred "
             "forty-six, not six hundred forty-three. Read them backwards and you have a "
             "completely different number.",
             '[[step eq="3 hundreds, 4 tens, 6 ones = 346 ✓"]][[step eq="643 ✗ the digits were read backwards"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Two hundreds, five tens and "
                        "one one. Two hundred, then fifty-one. Two hundred fifty-one.",
                        '[[placevalue h="2" t="5" o="1" caption="2 hundreds, 5 tens, 1 one"]][[step eq="200 + 50 + 1 = 251"]]'),
             "ask": {'a': 4, 'b': 2, 'c': 7, 'op': 'pv'}},
            {"worked": ("One more together. Six hundreds, no tens and three ones. Six "
                        "hundred three. The empty tens place still needs its zero, or "
                        "the six would slide over.",
                        '[[placevalue h="6" t="0" o="3" caption="6 hundreds, 0 tens, 3 ones"]][[step eq="600 + 0 + 3 = 603"]]'),
             "ask": {'a': 5, 'b': 8, 'c': 2, 'op': 'pv'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Three hundreds, "
                       "four tens and six ones is three hundred forty-six. Tap the "
                       "reason why."),
            "choices": ("because each place has its own size, and the biggest goes first | "
                        "because the largest digit is always written first | "
                        "because you read a number from right to left"),
            "answer": "because each place has its own size, and the biggest goes first",
            "board": '[[placevalue h="3" t="4" o="6" caption="hundreds, tens, ones"]]',
        },
        "recap": [
            ("So, here it is again. Three digits, three places: hundreds, tens, ones, "
             "biggest first. Say the hundreds, then the rest — and never read the "
             "digits backwards.",
             '[[placevalue h="3" t="4" o="6" caption="3 hundreds, 4 tens, 6 ones — 346"]]'),
            ("And that is how you read any number up to nine hundred ninety-nine.",
             '[[step eq="300 + 40 + 6 = 346"]]'),
        ],
        "bank": [{"a": 1, "b": 1, "c": 1, "op": "pv"}, {"a": 2, "b": 1, "c": 1, "op": "pv"}, {"a": 3, "b": 1, "c": 1, "op": "pv"}, {"a": 4, "b": 1, "c": 1, "op": "pv"}, {"a": 5, "b": 1, "c": 1, "op": "pv"}, {"a": 5, "b": 9, "c": 9, "op": "pv"}, {"a": 6, "b": 9, "c": 9, "op": "pv"}, {"a": 7, "b": 9, "c": 9, "op": "pv"}, {"a": 8, "b": 9, "c": 9, "op": "pv"}, {"a": 9, "b": 9, "c": 9, "op": "pv"}],
    },
    {
        "id": "entry-u4-ten-more", "course": "entry", "unit": 4,
        "topic": "Ten more", "op": "t10", "max_value": 99,
        "levels": ("abstract",), "symbols": ("tens digit",),
        "advance_line": "Three in a row — you've got it! You can add ten in your head.",
        "why": [
            ("Why practise adding ten? Because it is the one sum you never have to "
             "work out. Ten more pence, ten more days, ten more steps. Once you see "
             "what ten does to a number, you can say the answer before you have "
             "finished hearing the question.",
             '[[goal text="Ten more"]]'),
        ],
        "picture": [
            ("Here is thirty-four in blocks: three ten-sticks and four ones. Now add "
             "one more ten-stick. The four loose ones have not been touched — nobody "
             "moved them. There are simply four ten-sticks now instead of three. "
             "Thirty-four becomes forty-four.",
             '[[placevalue t="3" o="4" caption="34 — three tens and four ones, and one more ten arrives"]]'),
        ],
        "teach": [
            ("That is the rule, and it is why this one is free. Ten more adds one ten "
             "and leaves the ones exactly as they were. The four stays a four, and only "
             "the tens digit goes up by one. Thirty-four plus ten is forty-four, with "
             "no counting at all.",
             '[[step eq="3 tens 4 ones → 4 tens 4 ones"]][[step eq="34 + 10 = 44"]]'),
            ("Here is the trap. Adding ten is not adding one. Ten more than "
             "fifty-seven is sixty-seven, not fifty-eight. Check yourself by looking "
             "at the ones digit: it should be exactly the digit you started with.",
             '[[step eq="57 + 10 = 67 ✓ the 7 did not move"]][[step eq="58 ✗ that is one more, not ten more"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Ten more than twenty-five. The "
                        "five stays a five. The two tens become three tens. "
                        "Thirty-five.",
                        '[[placevalue t="2" o="5" caption="25 — the ones stay, the tens go up by one"]][[step eq="25 + 10 = 35"]]'),
             "ask": {'a': 42, 'b': 0, 'op': 't10'}},
            {"worked": ("One more together. Ten more than sixty-three. The three does "
                        "not move; six tens become seven tens. Seventy-three.",
                        '[[step eq="63 + 10 = 73"]]'),
             "ask": {'a': 78, 'b': 0, 'op': 't10'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Ten more than "
                       "thirty-four is forty-four. Tap the reason why."),
            "choices": ("because ten more adds one ten and leaves the ones alone | "
                        "because adding ten moves both digits up by one | "
                        "because ten more is the same as one more"),
            "answer": "because ten more adds one ten and leaves the ones alone",
            "board": '[[step eq="3 tens 4 ones → 4 tens 4 ones"]][[step eq="34 + 10 = 44"]]',
        },
        "recap": [
            ("So, here it is again. Ten more puts one more ten-stick down and touches "
             "nothing else. The ones digit stays exactly where it was, so a ones "
             "digit that has moved means the answer is not ten more.",
             '[[placevalue t="3" o="4" caption="the ones never move when you add ten"]]'),
            ("And that is a sum you can do in your head for the rest of your life.",
             '[[step eq="34 + 10 = 44"]]'),
        ],
        # (va) the walk-back is ON: this lesson's op draws a picture after a
        # right answer now, and a walk-back nobody can reach is not a fix.
        "show_work_on_correct": True,
        "bank": [{"a": 10, "b": 0, "op": "t10"}, {"a": 19, "b": 0, "op": "t10"}, {"a": 28, "b": 0, "op": "t10"}, {"a": 36, "b": 0, "op": "t10"}, {"a": 45, "b": 0, "op": "t10"}, {"a": 54, "b": 0, "op": "t10"}, {"a": 66, "b": 0, "op": "t10"}, {"a": 71, "b": 0, "op": "t10"}, {"a": 80, "b": 0, "op": "t10"}, {"a": 89, "b": 0, "op": "t10"}],
    },
    {
        "id": "entry-u4-what-a-digit-is-worth", "course": "entry", "unit": 4,
        "topic": "What a digit is worth", "op": "wor", "max_value": 999,
        "levels": ("abstract",), "symbols": ("place", "worth"),
        "advance_line": "Three in a row — you've got it! You know what each digit is worth.",
        "why": [
            ("Why ask what a digit is worth? Because the same digit is not always "
             "worth the same. A seven can be worth seven, or seventy, or seven "
             "hundred. Nothing about the seven changes — only where it is standing. "
             "Its place is what decides.",
             '[[goal text="What a digit is worth"]]'),
        ],
        "picture": [
            ("Here is three hundred seventy-four in blocks. Find the seven. It is not "
             "seven single ones — it is seven ten-sticks, sitting in the tens place. "
             "Seven tens is seventy. That is what the seven in this number is worth.",
             '[[placevalue h="3" t="7" o="4" caption="the 7 is seven ten-sticks — seventy"]]'),
        ],
        "teach": [
            ("That is the method. Name the places from the right: ones, then tens, "
             "then hundreds. Find which place your digit is standing in, and say what "
             "that many of THAT place is worth. In three hundred seventy-four, the "
             "seven is in the tens place, so it is worth seventy.",
             '[[placevalue h="3" t="7" o="4" caption="ones, tens, hundreds — from the right"]][[step eq="the 7 in 374 is worth 70"]]'),
            ("Here is the trap. Do not answer with the digit by itself. In three "
             "hundred seventy-four the seven is not worth seven. Find its place first, "
             "and then say the whole amount that place is worth.",
             '[[step eq="the 7 in 374 is worth 70 ✓"]][[step eq="7 ✗ that is the digit, not what it is worth"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. In two hundred fifty-eight, "
                        "what is the five worth? Eight is ones, five is tens. The five "
                        "is worth fifty.",
                        '[[placevalue h="2" t="5" o="8" caption="258 — the 5 sits in the tens place"]][[step eq="258 → the 5 is worth 50"]]'),
             "ask": {'a': 4, 'b': 6, 'c': 1, 'op': 'wor'}},
            {"worked": ("One more together. In nine hundred thirty-one, the three sits "
                        "in the tens place, so it is worth thirty.",
                        '[[placevalue h="9" t="3" o="1" caption="931 — the 3 sits in the tens place"]][[step eq="931 → the 3 is worth 30"]]'),
             "ask": {'a': 7, 'b': 2, 'c': 5, 'op': 'wor'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. In three hundred "
                       "seventy-four, the seven is worth seventy. Tap the reason why."),
            "choices": ("because the seven stands in the tens place, so it counts tens | "
                        "because a seven is worth seventy wherever it stands | "
                        "because the middle digit of any number is always tens"),
            "answer": "because the seven stands in the tens place, so it counts tens",
            "board": '[[placevalue h="3" t="7" o="4" caption="the 7 is in the tens place"]]',
        },
        "recap": [
            ("So, here it is again. A digit is worth what its PLACE says it is worth. "
             "Count the places from the right, find the one your digit stands in, and "
             "say that whole amount — never the bare digit.",
             '[[placevalue h="3" t="7" o="4" caption="the 7 is worth seventy"]]'),
            ("And that is why the same digit can be worth so many different amounts.",
             '[[step eq="the 7 in 374 is worth 70"]]'),
        ],
        # (va) the walk-back is ON: this lesson's op draws a picture after a
        # right answer now, and a walk-back nobody can reach is not a fix.
        "show_work_on_correct": True,
        "bank": [{"a": 1, "b": 2, "c": 1, "op": "wor"}, {"a": 9, "b": 2, "c": 3, "op": "wor"}, {"a": 8, "b": 3, "c": 4, "op": "wor"}, {"a": 7, "b": 4, "c": 3, "op": "wor"}, {"a": 6, "b": 5, "c": 4, "op": "wor"}, {"a": 4, "b": 6, "c": 5, "op": "wor"}, {"a": 3, "b": 7, "c": 6, "op": "wor"}, {"a": 2, "b": 8, "c": 6, "op": "wor"}, {"a": 1, "b": 9, "c": 7, "op": "wor"}, {"a": 8, "b": 9, "c": 8, "op": "wor"}],
    },
    {
        "id": "entry-u5-adding-three-digit-numbers", "course": "entry", "unit": 5,
        "topic": "Adding three-digit numbers", "op": "a3d", "max_value": 999,
        "levels": ("abstract",), "symbols": ("column",),
        "advance_line": "Three in a row — you've got it! You can add three-digit numbers.",
        "teach": [
            ("Three-digit numbers add the same way two-digit ones do. Work one "
             "column at a time, and always start on the right. Ones first, then "
             "tens, then hundreds.",
             '[[goal text="Adding three-digit numbers"]]'
             '[[step eq="243 + 125 = ?"]]'),
            ("Watch me add 243 plus 125. Ones: 3 plus 5 equals 8. Tens: 4 plus 2 "
             "equals 6. Hundreds: 2 plus 1 equals 3. So 243 plus 125 equals 368.",
             '[[step eq="ones: 3 + 5 = 8"]]'
             '[[step eq="tens: 4 + 2 = 6"]]'
             '[[step eq="hundreds: 2 + 1 = 3"]]'
             '[[step eq="243 + 125 = 368"]]'),
            ("Here is the trap. Keep each column in its own place. The tens answer "
             "goes under the tens, and the hundreds answer under the hundreds. If "
             "a column slides across, every digit after it is wrong.",
             '[[step eq="243 + 125 = 368 ✓"]]'
             '[[step eq="638 ✗ the columns were written in the wrong places"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 312 plus 246. Ones: 2 "
                        "plus 6 equals 8. Tens: 1 plus 4 equals 5. Hundreds: 3 "
                        "plus 2 equals 5. That is 558.",
                        '[[step eq="312 + 246 = 558"]]'),
             "ask": {"a": 425, "b": 132, "op": "a3d"}},
            {"worked": ("One more together. 507 plus 281. Ones: 7 plus 1 equals 8. "
                        "Tens: 0 plus 8 equals 8. Hundreds: 5 plus 2 equals 7. "
                        "That is 788.",
                        '[[step eq="507 + 281 = 788"]]'),
             "ask": {"a": 634, "b": 145, "op": "a3d"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        # (va) the walk-back is ON: this lesson's op draws a picture after a
        # right answer now, and a walk-back nobody can reach is not a fix.
        "show_work_on_correct": True,
        "bank": [{"a": 100, "b": 100, "op": "a3d"}, {"a": 156, "b": 301, "op": "a3d"}, {"a": 330, "b": 239, "op": "a3d"}, {"a": 321, "b": 342, "op": "a3d"}, {"a": 601, "b": 137, "op": "a3d"}, {"a": 411, "b": 381, "op": "a3d"}, {"a": 702, "b": 163, "op": "a3d"}, {"a": 799, "b": 100, "op": "a3d"}, {"a": 559, "b": 410, "op": "a3d"}, {"a": 899, "b": 100, "op": "a3d"}],
    },
    {
        "id": "entry-u5-crossing-a-hundred", "course": "entry", "unit": 5,
        "topic": "Crossing a hundred", "op": "c2h", "max_value": 199,
        "levels": ("abstract",), "symbols": ("hundred",),
        "advance_line": "Three in a row — you've got it! You can add past one hundred.",
        "teach": [
            ("You already carry into the tens. Today the tens themselves fill up. "
             "When ten tens are made, they become one hundred, and a new digit "
             "appears at the front.",
             '[[goal text="Crossing a hundred"]]'
             '[[step eq="68 + 47 = ?"]]'),
            ("Watch me add 68 plus 47. Ones: 8 plus 7 equals 15 — over nine, write "
             "the 5 and carry one ten. Tens: 6 plus 4 equals 10, plus the carried "
             "one is 11 tens. Eleven tens is one hundred and one ten. So 115.",
             '[[step eq="ones: 8 + 7 = 15, carry 1"]]'
             '[[step eq="tens: 6 + 4 + 1 = 11 tens"]]'
             '[[step eq="68 + 47 = 115"]]'),
            ("Here is the trap. Eleven tens is not written as 11 in the tens "
             "place. Ten of those tens become one hundred, so the 1 moves to the "
             "front and one ten stays behind.",
             '[[step eq="68 + 47 = 115 ✓"]]'
             '[[step eq="1115 ✗ eleven tens written where one ten belongs"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 75 plus 38. Ones: 5 plus "
                        "8 equals 13 — write the 3, carry one. Tens: 7 plus 3 plus "
                        "the carried one is 11 tens. That is 113.",
                        '[[step eq="75 + 38 = 113"]]'),
             "ask": {"a": 56, "b": 67, "op": "c2h"}},
            {"worked": ("One more together. 84 plus 29. Ones: 4 plus 9 equals 13 — "
                        "write the 3, carry one. Tens: 8 plus 2 plus one is 11 "
                        "tens. That is 113.",
                        '[[step eq="84 + 29 = 113"]]'),
             "ask": {"a": 47, "b": 76, "op": "c2h"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        # (va) the walk-back is ON: this lesson's op draws a picture after a
        # right answer now, and a walk-back nobody can reach is not a fix.
        "show_work_on_correct": True,
        "bank": [{"a": 10, "b": 90, "op": "c2h"}, {"a": 49, "b": 57, "op": "c2h"}, {"a": 61, "b": 51, "op": "c2h"}, {"a": 20, "b": 99, "op": "c2h"}, {"a": 28, "b": 98, "op": "c2h"}, {"a": 84, "b": 49, "op": "c2h"}, {"a": 75, "b": 67, "op": "c2h"}, {"a": 54, "b": 99, "op": "c2h"}, {"a": 87, "b": 79, "op": "c2h"}, {"a": 99, "b": 99, "op": "c2h"}],
    },
    {
        # (tb, 2026-09-05) TO THE SHAPE: a why, the stars counted past ten as the
        # picture (the count-on trick shown, not told), the rule, a recap. Ruling ⑤:
        # quick praise for counting; no reason question for pre-readers (open ruling).
        "id": "entry-u1-counting-past-ten", "course": "entry", "unit": 1,
        "topic": "Counting past ten", "op": "c20", "max_value": 20,
        "levels": ("concrete",), "symbols": ("count",),
        "advance_line": "Three in a row — you've got it! You can count past ten.",
        "why": [
            ("Why count past ten? Because most things come in more than ten. "
             "The crayons in a box, the steps to your door, the days until a "
             "birthday. Ten fingers run out fast, and the numbers keep going.",
             '[[goal text="Counting past ten"]]'),
        ],
        "picture": [
            ("Here are more than ten stars. Watch them light up. One, two, three, "
             "four, five, six, seven, eight, nine, ten — and counting does not "
             "stop. Eleven, twelve. Twelve stars.",
             '[[objects emoji="⭐" groups="12" count="1" caption="ten, then eleven, twelve"]]'),
        ],
        "teach": [
            ("That is counting past ten. After ten comes eleven, twelve, "
             "thirteen, and it keeps going. Say each number as you touch each "
             "star, and the last number you say is how many.",
             '[[objects emoji="⭐" groups="12" caption="touch each one and count"]]'),
            # (se, 2026-09-02) JIM'S FLAG: "Drop the term 'trap' and everything
            # after it." The warning sentence is gone; the line now ends on the
            # count itself. (The 40-odd "Here is the trap" lines in OTHER courses
            # are the house pattern and are deliberately untouched -- his flag was
            # this entry-course line; a wider ruling is his to make.)
            ("Here is a faster way. Count the first ten, then count on from ten. "
             "Ten — eleven, twelve, thirteen, fourteen. Fourteen stars.",
             '[[objects emoji="⭐" groups="14" caption="ten, then count on: 11, 12, 13, 14"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Ten, then count on: "
                        "eleven, twelve, thirteen. Thirteen stars.",
                        '[[objects emoji="⭐" groups="13" caption="thirteen stars"]]'),
             "ask": {"a": 19, "b": 0, "op": "c20"}},
            {"worked": ("One more together. Ten, then eleven, twelve, thirteen, "
                        "fourteen, fifteen, sixteen. Sixteen stars.",
                        '[[objects emoji="⭐" groups="16" caption="sixteen stars"]]'),
             "ask": {"a": 20, "b": 0, "op": "c20"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "recap": [
            ("So, here it is again. Counting does not stop at ten — eleven, "
             "twelve, thirteen, and on it goes. Count the first ten, then count "
             "on, and the last number you say is how many.",
             '[[objects emoji="⭐" groups="13" caption="ten, then count on: 11, 12, 13"]]'),
            ("And that is how you count anything that comes in more than ten.",
             '[[goal text="Counting past ten"]]'),
        ],
        # the whole pool is eleven to twenty, so the two worked pairs take the
        # last two and the bank takes the rest -- a problem may never be both.
        "bank": [{"a": 11, "b": 0, "op": "c20"}, {"a": 12, "b": 0, "op": "c20"}, {"a": 13, "b": 0, "op": "c20"}, {"a": 14, "b": 0, "op": "c20"}, {"a": 15, "b": 0, "op": "c20"}, {"a": 16, "b": 0, "op": "c20"}, {"a": 17, "b": 0, "op": "c20"}, {"a": 18, "b": 0, "op": "c20"}],
    },
    {
        # (tb, 2026-09-05) TO THE SHAPE on the NUMBER LINE: the two numbers as dots,
        # the later one is the bigger one. The ask now draws the line too (the
        # picture IS the comparing method, like the array is for equal groups); the
        # trap line is kept. Ruling ⑤: quick praise for comparing; no reason question
        # for pre-readers (open ruling).
        "id": "entry-u1-which-is-bigger", "course": "entry", "unit": 1,
        "topic": "Which number is bigger", "op": "big", "max_value": 20,
        "levels": ("abstract",), "symbols": ("bigger",),
        "advance_line": "Three in a row — you've got it! You can tell which number is bigger.",
        "why": [
            ("Why tell which number is bigger? Because you compare all day. Who "
             "has more stickers, which pile of blocks is taller, who is older. "
             "Two numbers, and you want to know which one is more.",
             '[[goal text="Which number is bigger"]]'),
        ],
        "picture": [
            ("Here are the numbers in their line, with 3 and 8 marked. Count "
             "along from one. You reach 3 first — and you have to keep counting "
             "to reach 8. The number you reach later is the bigger one. 8 is "
             "bigger than 3.",
             '[[numberline min="1" max="10" points="3,8" caption="you reach 8 later — 8 is bigger"]]'),
        ],
        "teach": [
            ("That is the rule. Numbers stand in a line, and the further along a "
             "number stands, the bigger it is. So the bigger number is the one "
             "you reach later when you count.",
             '[[numberline min="1" max="10" points="3,8" caption="8 comes later than 3"]]'
             '[[step eq="8 is bigger than 3"]]'),
            ("Here is the trap. Do not add the two numbers. The question is not "
             "how many in all. It only asks which one is bigger, so your "
             "answer is always one of the two numbers you were given.",
             '[[step eq="3 or 8 → 8 ✓"]]'
             '[[step eq="11 ✗ that is 3 and 8 added, not the bigger one"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Which is bigger, 6 or 9? "
                        "You reach 9 later when you count, so 9 is bigger.",
                        '[[numberline min="1" max="10" points="6,9" caption="9 comes later"]]'),
             "ask": {"a": 6, "b": 13, "op": "big"}},
            {"worked": ("One more together. Which is bigger, 12 or 7? You reach 12 "
                        "later, so 12 is bigger.",
                        '[[numberline min="1" max="20" points="7,12" caption="12 comes later"]]'
                        '[[step eq="12 or 7 → 12"]]'),
             "ask": {"a": 17, "b": 9, "op": "big"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "recap": [
            ("So, here it is again. Numbers stand in a line, and the bigger "
             "number is the one you reach later when you count. Not the two "
             "added up — just the one that comes later.",
             '[[numberline min="1" max="10" points="3,8" caption="you reach 8 later — 8 is bigger"]]'),
            ("And that is how you tell who has more.",
             '[[step eq="3 or 8 → 8"]]'),
        ],
        "bank": [{"a": 1, "b": 2, "op": "big"}, {"a": 3, "b": 6, "op": "big"}, {"a": 5, "b": 10, "op": "big"}, {"a": 7, "b": 14, "op": "big"}, {"a": 9, "b": 18, "op": "big"}, {"a": 12, "b": 3, "op": "big"}, {"a": 14, "b": 7, "op": "big"}, {"a": 16, "b": 11, "op": "big"}, {"a": 18, "b": 15, "op": "big"}, {"a": 20, "b": 19, "op": "big"}],
    },
    {
        "id": "entry-u2-doubles", "course": "entry", "unit": 2,
        "topic": "Doubles", "op": "dbe", "max_value": 20,
        "levels": ("abstract",), "symbols": ("double",),
        "advance_line": "Three in a row — you've got it! You know your doubles.",
        "why": [
            ("Why learn doubles? Because a double is quick, and quick helps "
             "everywhere. Two hands with five fingers each. Two rows of six seats. "
             "When you know a double by heart, you do not have to count it at all.",
             '[[goal text="Doubles"]]'),
        ],
        "picture": [
            ("Here are four stars, and here are four more — the same number again. "
             "That is what a double is. Count them all: one, two, three, four, "
             "five, six, seven, eight. Four plus four equals eight.",
             '[[objects emoji="⭐" groups="4" add="4" count="1" caption="four and four more — the same number twice"]]'),
        ],
        "teach": [
            ("That is the rule. A double adds a number to itself — the same number, "
             "twice. Six plus six: count six, then six more. Seven, eight, nine, ten, "
             "eleven, twelve. Six plus six equals twelve. Say a double out loud twice "
             "and you will start to remember it.",
             '[[objects emoji="⭐" groups="6" add="6" count="1" caption="six and six more"]][[step eq="6 + 6 = 12"]]'),
            ("Here is the trap. A double adds the same number again. It does not add "
             "one more. Seven plus seven is fourteen, not fifteen. Look at the number "
             "you were given, and use that very number twice.",
             '[[step eq="7 + 7 = 14 ✓"]][[step eq="15 ✗ that is 7 + 8, not a double"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Eight plus eight. Count eight, "
                        "then eight more — nine, ten, eleven, twelve, thirteen, "
                        "fourteen, fifteen, sixteen. Eight plus eight equals sixteen.",
                        '[[objects emoji="⭐" groups="8" add="8" caption="eight and eight more"]][[step eq="8 + 8 = 16"]]'),
             "ask": {'a': 9, 'b': 0, 'op': 'dbe'}},
            {"worked": ("One more together. Five plus five. Five, then five more — six, "
                        "seven, eight, nine, ten. Five plus five equals ten.",
                        '[[objects emoji="⭐" groups="5" add="5" count="1" caption="five and five more"]][[step eq="5 + 5 = 10"]]'),
             "ask": {'a': 10, 'b': 0, 'op': 'dbe'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "recap": [
            ("So, here it is again. A double is a number added to itself — the same "
             "number twice, never one more. Four and four is eight.",
             '[[objects emoji="⭐" groups="4" add="4" count="1" caption="the same number, twice"]]'),
            ("And doubles are worth knowing by heart, because they are the quickest "
             "sums there are.",
             '[[step eq="4 + 4 = 8"]]'),
        ],
        # (va) the walk-back is ON: this lesson's op draws a picture after a
        # right answer now, and a walk-back nobody can reach is not a fix.
        "show_work_on_correct": True,
        "bank": [{"a": 1, "b": 0, "op": "dbe"}, {"a": 2, "b": 0, "op": "dbe"}, {"a": 3, "b": 0, "op": "dbe"}, {"a": 4, "b": 0, "op": "dbe"}, {"a": 5, "b": 0, "op": "dbe"}, {"a": 6, "b": 0, "op": "dbe"}, {"a": 7, "b": 0, "op": "dbe"}, {"a": 8, "b": 0, "op": "dbe"}],
    },
    {
        "id": "entry-u2-adding-three-numbers", "course": "entry", "unit": 2,
        "topic": "Adding three numbers", "op": "add3", "max_value": 20,
        "levels": ("abstract",), "symbols": ("plus",),
        "advance_line": "Three in a row — you've got it! You can add three numbers.",
        "why": [
            ("Why add three numbers? Because things come in more than two piles. "
             "Sweets from three friends. Three boxes to carry to the car. Three "
             "throws in a game, and you want your score. You already know how to add "
             "— there is just one more pile.",
             '[[goal text="Adding three numbers"]]'),
        ],
        "picture": [
            ("Here are three pieces of tape, laid end to end: two, then three, then "
             "four. Look at the whole strip. It does not matter that there are three "
             "pieces — joined up, they are one length, and that length is nine.",
             '[[tape parts="2|3|4" total="9 in all" caption="three pieces joined end to end make nine"]]'),
        ],
        "teach": [
            ("That is the method: add the first two, then add the third to what you "
             "got. Two plus three equals five. Then five plus four equals nine. So "
             "two plus three plus four equals nine. Two small sums instead of one big "
             "one.",
             '[[tape parts="2|3|4" total="9 in all" caption="two and three joined make five, then the four goes on"]][[step eq="2 + 3 = 5"]][[step eq="5 + 4 = 9"]]'),
            ("Here is the trap, and here is a trick. The trap is stopping after two "
             "numbers and leaving the third one out. The trick is to look for two that "
             "make ten and add those first: in six plus four plus three, six and four "
             "make ten, and ten plus three is thirteen.",
             '[[step eq="6 + 4 = 10, then 10 + 3 = 13 ✓"]][[step eq="10 ✗ the third number was left out"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Three plus five plus two. "
                        "First three plus five equals eight. Then eight plus two equals "
                        "ten.",
                        '[[tape parts="3|5|2" total="10 in all" caption="three joined pieces make ten"]][[step eq="3 + 5 = 8"]][[step eq="8 + 2 = 10"]]'),
             "ask": {'a': 2, 'b': 4, 'c': 6, 'op': 'add3'}},
            {"worked": ("One more together. One plus six plus six. First one plus six "
                        "equals seven. Then seven plus six equals thirteen.",
                        '[[tape parts="1|6|6" total="13 in all" caption="one, six and six joined end to end"]][[step eq="1 + 6 = 7"]][[step eq="7 + 6 = 13"]]'),
             "ask": {'a': 7, 'b': 5, 'c': 3, 'op': 'add3'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "recap": [
            ("So, here it is again. Three numbers are just two sums. Add the first two, "
             "then add the third to what you got — and never stop before the third one "
             "is in.",
             '[[tape parts="2|3|4" total="9 in all" caption="add the first two, then the third"]]'),
            ("And if two of them make ten, start with those — ten is an easy number to "
             "add to.",
             '[[step eq="6 + 4 = 10, then 10 + 3 = 13"]]'),
        ],
        # (va) the walk-back is ON: this lesson's op draws a picture after a
        # right answer now, and a walk-back nobody can reach is not a fix.
        "show_work_on_correct": True,
        "bank": [{"a": 1, "b": 1, "c": 1, "op": "add3"}, {"a": 1, "b": 3, "c": 5, "op": "add3"}, {"a": 3, "b": 7, "c": 1, "op": "add3"}, {"a": 9, "b": 1, "c": 2, "op": "add3"}, {"a": 2, "b": 9, "c": 3, "op": "add3"}, {"a": 4, "b": 8, "c": 3, "op": "add3"}, {"a": 6, "b": 5, "c": 5, "op": "add3"}, {"a": 8, "b": 5, "c": 4, "op": "add3"}, {"a": 4, "b": 8, "c": 7, "op": "add3"}, {"a": 9, "b": 9, "c": 2, "op": "add3"}],
    },
    {
        "id": "entry-u3-the-missing-part", "course": "entry", "unit": 3,
        "topic": "The missing part", "op": "msp", "max_value": 20,
        "levels": ("abstract",), "symbols": ("more",),
        "advance_line": "Three in a row — you've got it! You can find the missing part.",
        "why": [
            ("Why find a missing part? Because you often know where you are and where "
             "you want to be, but not the gap between them. You have seven pence and "
             "the sticker costs ten. You are on page four and the story ends on nine. "
             "The missing part is how much more you need.",
             '[[goal text="The missing part"]]'),
        ],
        "picture": [
            ("Here is the number line, with a hop drawn from seven all the way to ten. "
             "Look at the hop itself, not where it lands. Count the steps inside it: "
             "eight, nine, ten. Three steps. So seven and three more make ten.",
             '[[numberline min="0" max="10" hops="7,10" caption="the hop from 7 to 10 is three steps long"]]'),
        ],
        "teach": [
            ("That is the method. Start at the number you have and count up to the "
             "number you want, and the answer is how many counts it took. Seven, then "
             "eight, nine, ten — three counts. The size of the hop is the missing part.",
             '[[numberline min="0" max="10" hops="7,10" caption="count the steps in the hop — three"]][[step eq="7 + 3 = 10"]]'),
            ("Here is the trap. Do not answer with the finish. The question is not what "
             "number we end on. It asks how many MORE, so your answer is the size of "
             "the jump, never the number you landed on.",
             '[[step eq="7 + 3 = 10 ✓ the jump is 3"]][[step eq="10 ✗ that is where we finished, not how many more"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Four and how many more make "
                        "nine? Count up from four: five, six, seven, eight, nine. Five "
                        "counts. Four and five more make nine.",
                        '[[numberline min="0" max="10" hops="4,9" caption="the hop from 4 to 9 is five steps long"]][[step eq="4 + 5 = 9"]]'),
             "ask": {'a': 5, 'b': 11, 'op': 'msp'}},
            {"worked": ("One more together. Eight and how many more make fifteen? Count "
                        "up from eight to fifteen — seven counts. Eight and seven more "
                        "make fifteen.",
                        '[[step eq="8 + 7 = 15"]]'),
             "ask": {'a': 9, 'b': 17, 'op': 'msp'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "recap": [
            ("So, here it is again. Start where you are, count up to where you want to "
             "be, and the answer is how many counts it took — the size of the hop, not "
             "the place it lands.",
             '[[numberline min="0" max="10" hops="7,10" caption="the hop is the answer"]]'),
            ("And that is how you work out how many more you need.",
             '[[step eq="7 + 3 = 10"]]'),
        ],
        # (va) the walk-back is ON: this lesson's op draws a picture after a
        # right answer now, and a walk-back nobody can reach is not a fix.
        "show_work_on_correct": True,
        "bank": [{"a": 1, "b": 2, "op": "msp"}, {"a": 3, "b": 5, "op": "msp"}, {"a": 6, "b": 9, "op": "msp"}, {"a": 10, "b": 14, "op": "msp"}, {"a": 15, "b": 20, "op": "msp"}, {"a": 7, "b": 14, "op": "msp"}, {"a": 3, "b": 12, "op": "msp"}, {"a": 3, "b": 14, "op": "msp"}, {"a": 7, "b": 20, "op": "msp"}, {"a": 1, "b": 20, "op": "msp"}],
    },
    {
        "id": "entry-u6-take-away-with-regrouping",
        "course": "entry", "unit": 6,
        "topic": 'Taking away with regrouping',
        "op": '-', "max_value": 99, "regroup": True,
        "levels": ("abstract",),
        "symbols": ('regroup', 'too small', 'equals'),
        "advance_line": "Three in a row — you've got it! You can regroup like a pro.",
        "teach": [
            ('Today we are learning to regroup. Sometimes the ones digit on top is too small to take away from. When that happens, we regroup: we take one ten and turn it into ten ones.',
             '[[goal text="Taking away with regrouping"]]'),
            ('Watch me take 17 away from 42. Ones: 2 is too small to take 7 away from. Regroup — one ten becomes ten ones, so 2 becomes 12, and the 4 tens become 3. Ones: 12 take away 7 equals 5. Tens: 3 take away 1 equals 2. So 42 take away 17 equals 25.',
             '[[step eq="42 − 17"]][[step eq="regroup: 42 = 3 tens and 12 ones"]][[step eq="ones: 12 − 7 = 5"]][[step eq="tens: 3 − 1 = 2"]][[step eq="42 − 17 = 25"]]'),
            ('One more, watch. 53 take away 28. Ones: 3 is too small — regroup, 3 becomes 13, and 5 tens become 4. Ones: 13 take away 8 equals 5. Tens: 4 take away 2 equals 2. So 53 take away 28 equals 25.',
             '[[step eq="53 − 28"]][[step eq="regroup: 53 = 4 tens and 13 ones"]][[step eq="ones: 13 − 8 = 5"]][[step eq="tens: 4 − 2 = 2"]][[step eq="53 − 28 = 25"]]'),
        ],
        "pairs": [
            {"worked": ('Here is one more, done for you. 61 take away 35. Ones: 1 is too small — regroup, 1 becomes 11, 6 tens become 5. Ones: 11 take away 5 equals 6. Tens: 5 take away 3 equals 2. So 61 take away 35 equals 26.',
                        '[[step eq="61 − 35"]][[step eq="regroup: 61 = 5 tens and 11 ones"]][[step eq="ones: 11 − 5 = 6"]][[step eq="tens: 5 − 3 = 2"]][[step eq="61 − 35 = 26"]]'),
             "ask": {'a': 62, 'b': 35, 'op': '-'}},
            {"worked": ('One more together. 74 take away 46. Ones: 4 is too small — regroup, 4 becomes 14, 7 tens become 6. Ones: 14 take away 6 equals 8. Tens: 6 take away 4 equals 2. So 74 take away 46 equals 28.',
                        '[[step eq="74 − 46"]][[step eq="regroup: 74 = 6 tens and 14 ones"]][[step eq="ones: 14 − 6 = 8"]][[step eq="tens: 6 − 4 = 2"]][[step eq="74 − 46 = 28"]]'),
             "ask": {'a': 73, 'b': 45, 'op': '-'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        # (va) the walk-back is ON: this lesson's op draws a picture after a
        # right answer now, and a walk-back nobody can reach is not a fix.
        "show_work_on_correct": True,
        "bank": [{'a': 21, 'b': 13, 'op': '-'}, {'a': 32, 'b': 15, 'op': '-'}, {'a': 34, 'b': 16, 'op': '-'}, {'a': 43, 'b': 17, 'op': '-'}, {'a': 45, 'b': 28, 'op': '-'}, {'a': 52, 'b': 24, 'op': '-'}, {'a': 56, 'b': 38, 'op': '-'}, {'a': 63, 'b': 26, 'op': '-'}, {'a': 71, 'b': 44, 'op': '-'}, {'a': 75, 'b': 47, 'op': '-'}, {'a': 82, 'b': 55, 'op': '-'}, {'a': 91, 'b': 63, 'op': '-'}],
    },
    # ------------------------- BUILD kd: the content sweep -------------------------
    {
        # (tb, 2026-09-05) TO THE SHAPE, for the youngest students: a why in their
        # world, the stars counted one at a time as the picture, the rule read off
        # it, a recap. No walk-back and no reason question -- ruling ⑤ keeps the
        # quick praise for counting, and a reason question's options are text a
        # student who is learning to count to ten cannot yet read (open ruling).
        "id": "entry-u1-counting-to-10", "course": "entry", "unit": 1,
        "topic": "Counting to 10",
        "op": "cnt", "max_value": 10,
        "levels": ("concrete",),   # the picture IS the problem; there is no
                                   # abstract form of "count these stars"
        "symbols": ("count",),
        "advance_line": ("Three in a row — you've got it! "
                         "You can count to ten."),
        "why": [
            ("Why count? Because counting tells you how many. How many cookies "
             "are left, how many friends are coming, how many fingers you are "
             "holding up. When you can count, you always know how many.",
             '[[goal text="Counting to 10"]]'),
        ],
        "picture": [
            ("Here are some stars. Watch them light up one at a time, and say a "
             "number for each one. One, two, three, four, five. The last number "
             "you say tells you how many. Five stars.",
             '[[objects emoji="⭐" groups="5" count="1" caption="one number for each star — five stars"]]'),
        ],
        "teach": [
            ("That is how counting works. Point to each star and say one number "
             "for it: one, two, three. Never skip a star, and never count one "
             "twice. The last number you say is how many there are.",
             '[[objects emoji="⭐" groups="3" count="1" caption="one, two, three — three stars"]]'),
            ("Watch me count again, a bigger group this time. One, two, three, "
             "four, five, six, seven. Seven stars.",
             '[[objects emoji="⭐" groups="7" count="1" caption="count them one at a time"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. One, two, three, four. "
                        "Four stars.",
                        '[[objects emoji="⭐" groups="4" count="1" caption="count them one at a time"]]'),
             "ask": {"a": 2, "b": 0, "op": "cnt"}},
            {"worked": ("One more together. One, two, three, four, five, six. "
                        "Six stars.",
                        '[[objects emoji="⭐" groups="6" count="1" caption="count them one at a time"]]'),
             "ask": {"a": 4, "b": 0, "op": "cnt"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "recap": [
            ("So, here it is again. To count, point to each star and say one "
             "number for it, and the last number you say is how many. One, two, "
             "three, four. Four stars.",
             '[[objects emoji="⭐" groups="4" count="1" caption="the last number you say is how many"]]'),
            ("And counting is how you always know how many there are.",
             '[[goal text="Counting to 10"]]'),
        ],
        "bank": [
            {"a": 1, "b": 0, "op": "cnt"}, {"a": 3, "b": 0, "op": "cnt"},
            {"a": 5, "b": 0, "op": "cnt"}, {"a": 6, "b": 0, "op": "cnt"},
            {"a": 7, "b": 0, "op": "cnt"}, {"a": 8, "b": 0, "op": "cnt"},
            {"a": 9, "b": 0, "op": "cnt"}, {"a": 10, "b": 0, "op": "cnt"},
        ],
    },
    {
        # (tb, 2026-09-05) TO THE SHAPE on the NUMBER LINE: numbers stand in a line,
        # and "right after" is one hop up, "right before" one hop back. The asks
        # stay bare (a labelled line would read the answer off); ruling ⑤ keeps the
        # quick praise for a one-hop fact; no reason question (pre-readers, open ruling).
        "id": "entry-u1-numbers-before-and-after", "course": "entry", "unit": 1,
        "topic": "Numbers before and after",
        "op": "aft", "max_value": 20,
        "levels": ("abstract",),
        "symbols": ("after", "before"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can find the number before and the number after."),
        "why": [
            ("Why learn what comes before and after? Because numbers always stand "
             "in the same order, like friends in a line. If you know who stands "
             "next to who, you can count on from any number instead of starting "
             "at one every time.",
             '[[goal text="Numbers before and after"]]'),
        ],
        "picture": [
            ("Here are the numbers standing in their line. Find 5. Take one hop "
             "up the line and you land on 6 — so 6 comes right after 5. Now find "
             "6 and take one hop back: you land on 5 — so 5 comes right before 6.",
             '[[numberline min="1" max="10" points="5" hops="5,6" caption="one hop up: 6 comes right after 5"]]'),
        ],
        "teach": [
            ("That is the whole idea. The number right after is one hop up the "
             "line — count up one. The number right before is one hop back — "
             "count back one.",
             '[[numberline min="1" max="10" points="6" hops="6,5" caption="one hop back: 5 comes right before 6"]]'),
            ("Watch me. What comes right after 9? Find 9, hop up one, and you "
             "land on 10. 10 comes right after 9.",
             '[[numberline min="1" max="10" points="9" hops="9,10" caption="9, then 10"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Right after 6 comes 7 — "
                        "one hop up.",
                        '[[numberline min="1" max="10" points="6" hops="6,7" caption="6, 7"]]'),
             "ask": {"a": 4, "b": 0, "op": "aft"}},
            {"worked": ("One more together. Right before 10 comes 9 — one hop back.",
                        '[[numberline min="1" max="10" points="10" hops="10,9" caption="9, 10"]]'),
             "ask": {"a": 7, "b": 0, "op": "bef"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "recap": [
            ("So, here it is again. Numbers stand in a line in the same order "
             "every time. The number right after is one hop up; the number right "
             "before is one hop back.",
             '[[numberline min="1" max="10" points="5" hops="5,6" caption="one hop up: right after"]]'),
            ("And knowing who stands next to who lets you count on from any "
             "number.",
             '[[step eq="4, 5, 6"]]'),
        ],
        "bank": [
            {"a": 2, "b": 0, "op": "aft"}, {"a": 3, "b": 0, "op": "bef"},
            {"a": 3, "b": 0, "op": "aft"}, {"a": 5, "b": 0, "op": "bef"},
            {"a": 8, "b": 0, "op": "aft"}, {"a": 9, "b": 0, "op": "bef"},
            {"a": 11, "b": 0, "op": "aft"}, {"a": 12, "b": 0, "op": "bef"},
            {"a": 14, "b": 0, "op": "aft"}, {"a": 15, "b": 0, "op": "bef"},
            {"a": 17, "b": 0, "op": "aft"}, {"a": 20, "b": 0, "op": "bef"},
        ],
    },
    {
        "id": "entry-u3-story-problems", "course": "entry", "unit": 3,
        "topic": "Story problems — adding and taking away",
        "op": "+", "max_value": 10, "a_max": 9, "b_max": 9,
        "mixed_review": True,   # plus and minus interleave; a ramp across two ops
                                # would be meaningless
        "levels": ("abstract",),
        "symbols": ("plus", "minus"),
        "advance_line": "Three in a row — you've got it! You can solve story problems.",
        "why": [
            ("Why story problems? Because outside this lesson nobody hands you a sum. "
             "They hand you a story — someone got some more, someone ate three, some "
             "flew away — and the sum is hiding inside it. Finding the sum is the "
             "whole job.",
             '[[goal text="Story problems"]]'),
        ],
        "picture": [
            ("Listen, and watch. Maya has four stickers. She gets one more. There are "
             "her four, and there is the new one arriving. Getting more means putting "
             "together, so this story is a plus. Four plus one equals five stickers in "
             "all.",
             '[[objects emoji="⭐" groups="4" add="1" count="1" caption="four stickers, and one more arrives — a plus story"]]'),
        ],
        "teach": [
            ("That is the method: listen for the word that tells you which sign it is. "
             "Gets, finds, buys, more — those put together, and that is plus. Eats, "
             "loses, gives away, fly off — those take away, and that is minus. Find "
             "the word, then do the sum.",
             '[[step eq="gets more · finds · buys → +"]][[step eq="eats · loses · flies away → −"]]'),
            ("Here is the trap. Do not add just because there are two numbers in the "
             "story. Ben has nine grapes and eats three: he does not have twelve, he "
             "has six. Ask yourself whether the story made the pile bigger or smaller.",
             '[[step eq="9 − 3 = 6 ✓ he ate three"]][[step eq="12 ✗ that is nine and three put together"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Ava has seven crayons. She "
                        "finds two more. Finds means putting together, so it is plus. "
                        "Seven plus two equals nine crayons in all.",
                        '[[step eq="7 + 2 = 9"]]'),
             "ask": {'a': 5, 'b': 2, 'op': '+', 'story': 'Sam has 5 shells. He finds 2 more. How many shells does he have in all?'}},
            {"worked": ("One more together. Leo has eight balloons. Five fly away. Fly "
                        "away means taking away, so it is minus. Eight minus five "
                        "equals three balloons are left.",
                        '[[step eq="8 − 5 = 3"]]'),
             "ask": {'a': 7, 'b': 3, 'op': '-', 'story': 'Mia has 7 berries. She eats 3. How many berries are left?'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "recap": [
            ("So, here it is again. A story problem hides a plus or a minus inside it. "
             "Listen for the word that says whether the pile grew or shrank, write "
             "that sum, and then do the sum you already know how to do.",
             '[[step eq="gets more · finds · buys → +"]][[step eq="eats · loses · flies away → −"]]'),
            ("And that is how a story turns into a sum.",
             '[[step eq="4 + 1 = 5"]]'),
        ],
        "bank": [
            {"a": 2, "b": 1, "op": "+",
             "story": ("Jo has 2 rocks. She finds 1 more. How many rocks does "
                       "she have in all?")},
            {"a": 3, "b": 1, "op": "-",
             "story": "Ed has 3 kites. 1 blows away. How many kites are left?"},
            {"a": 3, "b": 2, "op": "+",
             "story": ("Ana has 3 cups. She gets 2 more. How many cups does she "
                       "have in all?")},
            {"a": 4, "b": 2, "op": "-",
             "story": "Ty has 4 socks. 2 get lost. How many socks are left?"},
            {"a": 4, "b": 3, "op": "+",
             "story": ("Bo has 4 cars. He gets 3 more. How many cars does he "
                       "have in all?")},
            {"a": 6, "b": 2, "op": "-",
             "story": "Zoe has 6 pears. She eats 2. How many pears are left?"},
            {"a": 5, "b": 4, "op": "+",
             "story": ("Kim has 5 beads. She gets 4 more. How many beads does "
                       "she have in all?")},
            {"a": 8, "b": 3, "op": "-",
             "story": ("Dan has 8 stamps. He gives 3 away. How many stamps are "
                       "left?")},
            {"a": 6, "b": 3, "op": "+",
             "story": ("Pia has 6 leaves. She finds 3 more. How many leaves does "
                       "she have in all?")},
            {"a": 9, "b": 4, "op": "-",
             "story": "Max has 9 blocks. 4 fall down. How many blocks are left?"},
        ],
    },
    {
        "id": "entry-u7-counting-coins", "course": "entry", "unit": 7,
        "topic": "Counting nickels and pennies",
        "op": "nick", "max_value": 35,
        "levels": ("abstract",),
        "symbols": ("nickel", "penny"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can count nickels and pennies."),
        "teach": [
            ("Money time! A penny is worth 1 cent. A nickel is worth 5 cents.",
             '[[goal text="Counting nickels and pennies"]]'),
            ("Watch me count 2 nickels and 3 pennies. Nickels first, count by "
             "five: 5, 10. Then pennies, count on: 11, 12, 13. That is 13 "
             "cents.",
             '[[step eq="5, 10 — 11, 12, 13 = 13 cents"]]'),
            ("One more, watch. 3 nickels and 1 penny. Count by five: 5, 10, 15. "
             "One more: 16. 16 cents.",
             '[[step eq="5, 10, 15 — 16 = 16 cents"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 1 nickel and 2 "
                        "pennies. 5 — then 6, 7. 7 cents.",
                        '[[step eq="5 — 6, 7 = 7 cents"]]'),
             "ask": {"a": 1, "b": 4, "op": "nick"}},
            {"worked": ("One more together. 2 nickels and 2 pennies. 5, 10 — "
                        "11, 12. 12 cents.",
                        '[[step eq="5, 10 — 11, 12 = 12 cents"]]'),
             "ask": {"a": 2, "b": 4, "op": "nick"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        # (va) the walk-back is ON: this lesson's op draws a picture after a
        # right answer now, and a walk-back nobody can reach is not a fix.
        "show_work_on_correct": True,
        "bank": [
            {"a": 1, "b": 1, "op": "nick"},             {"a": 1, "b": 3, "op": "nick"}, {"a": 2, "b": 1, "op": "nick"},
                        {"a": 3, "b": 3, "op": "nick"}, {"a": 3, "b": 2, "op": "nick"},
            {"a": 4, "b": 1, "op": "nick"}, {"a": 4, "b": 3, "op": "nick"},
            {"a": 5, "b": 2, "op": "nick"}, {"a": 6, "b": 1, "op": "nick"},
        ],
    },
    # =========================================================================
    # (mo) ENTRY-LEVEL UNIT 8 -- TIME, CALENDAR & MEASUREMENT
    # -------------------------------------------------------------------------
    # The spreadsheet Jim asked for on 2026-08-24 found the only hole left in the
    # curriculum: Entry-Level Units 8 and 9 had NO scripted lessons at all, in the
    # one course where the youngest children start. This is Unit 8.
    #
    # ⚠️ EVERY LESSON HERE IS A SHAPE THE CHILD HAS ALREADY MET. That is the whole
    # design: a six-year-old meeting the clock should not also be meeting a new
    # kind of arithmetic. "Later on the clock" is counting on (U2/U3) along a
    # number line. "Minutes past the hour" counts by five, exactly as U7 counts
    # nickels. "Weeks and days" is U7's coin shape with sevens instead of fives.
    # "How much longer" is taking away (U3) with a ruler drawn under it.
    #
    # ⚠️ THE CLOCK FACE DOES NOT WRAP HERE, and hrl's check enforces it. "11
    # o'clock plus 3 hours is 2 o'clock" is a real idea, and it is not this unit's
    # -- it needs the twelve-hour circle taught first. A lesson that quietly
    # wrapped would be teaching modular arithmetic to a child who is still
    # counting on their fingers.
    # =========================================================================
    {
        "id": "entry-u8-later-on-the-clock", "course": "entry", "unit": 8,
        "topic": "Later on the clock",
        "op": "hrl", "max_value": 12,
        "levels": ("abstract",),
        "symbols": ("o'clock",),
        "advance_line": ("Three in a row — you've got it! "
                         "You can tell what time it will be later."),
        "teach": [
            ("The short hand on a clock tells the hour. When it points at 3, we "
             "say it is 3 o'clock.",
             '[[goal text="Later on the clock"]]'
             '[[numberline min="1" max="12" points="3" caption="the clock hours — the hand at 3"]]'),
            ("Watch me. It is 9 o'clock now. Two hours later, count on: 10, 11. "
             "It is 11 o'clock.",
             '[[numberline min="1" max="12" points="11" caption="the clock hours — the hand at 11"]]'
             '[[step eq="9 o\'clock, 2 hours later = 11"]]'),
            ("One more, watch. It is 5 o'clock. Four hours later, count on: 6, "
             "7, 8, 9. It is 9 o'clock.",
             '[[numberline min="1" max="12" points="9" caption="the clock hours — the hand at 9"]]'
             '[[step eq="5 o\'clock, 4 hours later = 9"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. It is 7 o'clock. Three "
                        "hours later, count on: 8, 9, 10. It is 10 o'clock.",
                        '[[step eq="7 o\'clock, 3 hours later = 10"]]'),
             "ask": {"a": 3, "b": 1, "op": "hrl"}},
            {"worked": ("One more together. It is 10 o'clock. One hour later is "
                        "11 o'clock.",
                        '[[step eq="10 o\'clock, 1 hour later = 11"]]'),
             "ask": {"a": 5, "b": 2, "op": "hrl"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 1, "b": 1, "op": "hrl"}, {"a": 2, "b": 1, "op": "hrl"},
            {"a": 2, "b": 2, "op": "hrl"}, {"a": 4, "b": 1, "op": "hrl"},
            {"a": 3, "b": 2, "op": "hrl"}, {"a": 4, "b": 2, "op": "hrl"},
            {"a": 4, "b": 3, "op": "hrl"}, {"a": 5, "b": 3, "op": "hrl"},
            {"a": 6, "b": 3, "op": "hrl"}, {"a": 6, "b": 4, "op": "hrl"},
            {"a": 7, "b": 4, "op": "hrl"}, {"a": 8, "b": 4, "op": "hrl"},
        ],
    },
    {
        "id": "entry-u8-minutes-past-the-hour", "course": "entry", "unit": 8,
        "topic": "Minutes past the hour",
        "op": "min5", "max_value": 55,
        "levels": ("abstract",),
        "symbols": ("minute hand",),
        "advance_line": ("Three in a row — you've got it! "
                         "You can read the minutes on a clock."),
        "teach": [
            ("The long hand is the minute hand, and it moves faster than the "
             "short one. From one number to the next is five minutes.",
             '[[goal text="Minutes past the hour"]]'),
            ("Watch me. The minute hand points to 6. Count by five: 5, 10, 15, "
             "20, 25, 30. That is 30 minutes past the hour.",
             '[[step eq="6 numbers past 12, five minutes each = 30"]]'),
            ("Now the other way, watch. It is 20 minutes past. Count by five "
             "until you reach 20: 5, 10, 15, 20. That is four numbers, so the "
             "minute hand points to 4.",
             '[[step eq="20 minutes, five minutes each = 4 on the clock"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. The minute hand points "
                        "to 9. Count by five: 5, 10, 15, 20, 25, 30, 35, 40, 45. "
                        "That is 45 minutes.",
                        '[[step eq="9 numbers past 12, five minutes each = 45"]]'),
             "ask": {"a": 10, "b": 0, "op": "min5"}},
            {"worked": ("One more together. It is 15 minutes past. Count by "
                        "five: 5, 10, 15. Three numbers, so the hand points to 3.",
                        '[[step eq="15 minutes, five minutes each = 3 on the clock"]]'),
             "ask": {"a": 55, "b": 0, "op": "min5q"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        # ⚠️ THE BANK IS TEN, NOT TWELVE, AND THAT IS THE POINT. A clock has only
        # ELEVEN positions the minute hand can land on, and this lesson also
        # DEMONSTRATES four of them -- teach beats two and three, and both worked
        # examples. Positions 3, 4, 6 and 9 are therefore reserved: they are shown,
        # so they are never asked. Filling the bank to twelve would have meant
        # asking a child a question Mr. Cadabra answered out loud two minutes
        # earlier, which is the exact defect workedaudit.py exists to find.
        #
        # BOTH DIRECTIONS, INTERLEAVED BY DIFFICULTY. The key is the clock NUMBER
        # either way (min5's a, min5q's a divided by five), so "the hand points to
        # 2" and "10 minutes past" sit together on the ramp. That pairing is the
        # lesson, not a duplicate: a child who can only go one way has memorised a
        # list rather than learned to read a clock.
        "bank": [
            {"a": 5, "b": 0, "op": "min5q"}, {"a": 1, "b": 0, "op": "min5"},
            {"a": 10, "b": 0, "op": "min5q"}, {"a": 2, "b": 0, "op": "min5"},
            {"a": 25, "b": 0, "op": "min5q"}, {"a": 5, "b": 0, "op": "min5"},
            {"a": 35, "b": 0, "op": "min5q"}, {"a": 7, "b": 0, "op": "min5"},
            {"a": 40, "b": 0, "op": "min5q"}, {"a": 8, "b": 0, "op": "min5"},
        ],
    },
    {
        "id": "entry-u8-weeks-and-days", "course": "entry", "unit": 8,
        "topic": "Weeks and days",
        "op": "dwd", "max_value": 34,
        "levels": ("abstract",),
        "symbols": ("week",),
        "advance_line": ("Three in a row — you've got it! "
                         "You can count weeks and days."),
        "teach": [
            ("A week is seven days. Sunday, Monday, Tuesday, Wednesday, "
             "Thursday, Friday, Saturday — and then a new one starts.",
             '[[goal text="Weeks and days"]]'),
            ("Watch me. 2 weeks and 2 days. Count the weeks by seven: 7, 14. "
             "Then count the loose days on: 15, 16. That is 16 days.",
             '[[step eq="2 weeks and 2 days = 16 days"]]'),
            ("One more, watch. 3 weeks and 4 days. By seven: 7, 14, 21. Then "
             "on: 22, 23, 24, 25. That is 25 days.",
             '[[step eq="3 weeks and 4 days = 25 days"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 1 week and 6 days. "
                        "Seven, then on: 8, 9, 10, 11, 12, 13. That is 13 days.",
                        '[[step eq="1 week and 6 days = 13 days"]]'),
             "ask": {"a": 1, "b": 4, "op": "dwd"}},
            {"worked": ("One more together. 4 weeks and 1 day. By seven: 7, 14, "
                        "21, 28. One more day: 29 days.",
                        '[[step eq="4 weeks and 1 day = 29 days"]]'),
             "ask": {"a": 2, "b": 6, "op": "dwd"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 1, "b": 1, "op": "dwd"}, {"a": 1, "b": 2, "op": "dwd"},
            {"a": 1, "b": 3, "op": "dwd"}, {"a": 1, "b": 5, "op": "dwd"},
            {"a": 2, "b": 1, "op": "dwd"}, {"a": 2, "b": 3, "op": "dwd"},
            {"a": 2, "b": 5, "op": "dwd"}, {"a": 3, "b": 1, "op": "dwd"},
            {"a": 3, "b": 3, "op": "dwd"}, {"a": 3, "b": 6, "op": "dwd"},
            {"a": 4, "b": 2, "op": "dwd"}, {"a": 4, "b": 5, "op": "dwd"},
        ],
    },
    {
        "id": "entry-u8-how-much-longer", "course": "entry", "unit": 8,
        "topic": "How much longer",
        "op": "cube", "max_value": 20,
        "levels": ("abstract",),
        "symbols": ("longer",),
        "advance_line": ("Three in a row — you've got it! "
                         "You can measure and compare with cubes."),
        "teach": [
            ("We can measure with cubes. Line them up under the pencil, start "
             "at the very end, and count. More cubes means longer than fewer.",
             '[[goal text="How much longer"]]'),
            ("Watch me. The pencil is 13 cubes. The crayon is 4 cubes. 13 take "
             "away 4 equals 9, so the pencil is 9 cubes longer.",
             '[[bars data="pencil:13 | crayon:4" caption="pencil 13 and crayon 4"]]'
             '[[step eq="13 cubes − 4 cubes = 9"]]'),
            ("One more, watch. The pencil is 17 cubes. The crayon is 9 cubes. "
             "17 take away 9 equals 8, so the pencil is 8 cubes longer.",
             '[[bars data="pencil:17 | crayon:9" caption="pencil 17 and crayon 9"]]'
             '[[step eq="17 cubes − 9 cubes = 8"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. The pencil is 19 "
                        "cubes. The crayon is 12 cubes. 19 take away 12 equals "
                        "7, so the pencil is 7 cubes longer.",
                        '[[step eq="19 cubes − 12 cubes = 7"]]'),
             "ask": {"a": 11, "b": 5, "op": "cube"}},
            {"worked": ("One more together. The pencil is 20 cubes. The crayon "
                        "is 13 cubes. 20 take away 13 equals 7, so the pencil is "
                        "7 cubes longer.",
                        '[[step eq="20 cubes − 13 cubes = 7"]]'),
             "ask": {"a": 15, "b": 6, "op": "cube"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 3, "b": 1, "op": "cube"}, {"a": 4, "b": 1, "op": "cube"},
            {"a": 5, "b": 2, "op": "cube"}, {"a": 6, "b": 2, "op": "cube"},
            {"a": 7, "b": 3, "op": "cube"}, {"a": 8, "b": 3, "op": "cube"},
            {"a": 9, "b": 4, "op": "cube"}, {"a": 10, "b": 4, "op": "cube"},
            {"a": 12, "b": 5, "op": "cube"}, {"a": 14, "b": 6, "op": "cube"},
            {"a": 16, "b": 7, "op": "cube"}, {"a": 18, "b": 8, "op": "cube"},
        ],
    },
    # =========================================================================
    # (mp) ENTRY-LEVEL UNIT 9 -- SHAPES, PATTERNS & GROUPS
    # -------------------------------------------------------------------------
    # ⭐ THE LAST UNSCRIPTED UNIT IN THE CURRICULUM. With these four lessons every
    # unit of all ten courses -- Entry-Level Math through Differential Equations
    # -- has scripted lessons.
    #
    # ⚠️ THE TWO GROUP LESSONS NEVER SAY "TIMES", and that is deliberate rather
    # than squeamish. Basic Math Unit 2 is where multiplying is taught and named;
    # a child should meet the IDEA -- equal groups counted up, and a pile shared
    # fairly -- before the word and the symbol arrive. So grp counts by repeated
    # addition out loud and eqs deals one at a time, exactly as a six-year-old
    # would with real counters.
    #
    # ⚠️ AND eqs NEVER LEAVES A REMAINDER. Its check refuses anything that does.
    # Left-overs are basic-u3-left-overs' lesson; meeting them here, before fair
    # sharing itself is solid, teaches a child that sharing sometimes just fails.
    # =========================================================================
    {
        "id": "entry-u9-sides-and-corners", "course": "entry", "unit": 9,
        "topic": "Sides and corners",
        "op": "sid", "max_value": 10,
        "levels": ("abstract",),
        "symbols": ("side", "corner"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can count the sides and corners on a shape."),
        "teach": [
            ("Every flat shape is made of straight sides, and the place where "
             "two sides meet is a corner of the shape.",
             '[[goal text="Sides and corners"]]'),
            ("Watch me count a triangle. Side, side, side — 3 sides. Its name "
             "even says so: tri means three.",
             '[[step eq="triangle → 3 sides"]]'),
            ("Now its corners, watch. Corner, corner, corner — 3 corners. A "
             "triangle has 3 sides and 3 corners. Every flat shape is like that: "
             "it has just as many corners as sides.",
             '[[step eq="triangle → 3 corners, the same as its sides"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. A square. Side, side, "
                        "side, side — 4 sides.",
                        '[[step eq="square → 4 sides"]]'),
             "ask": {"a": 5, "b": 0, "op": "sid"}},
            {"worked": ("One more together. A square again, but its corners "
                        "this time. Corner, corner, corner, corner — 4 corners, "
                        "the same as its sides.",
                        '[[step eq="square → 4 corners"]]'),
             "ask": {"a": 5, "b": 0, "op": "cor"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        # ⚠️ THE TRIANGLE AND THE SQUARE ARE RESERVED. Both teach beats work the
        # triangle and both worked examples work the square, so neither shape is
        # ever ASKED -- in either direction. That leaves the five bigger shapes,
        # each asked for its sides and for its corners, which IS the lesson: the
        # two counts always match.
        "bank": [
            {"a": 6, "b": 0, "op": "sid"}, {"a": 6, "b": 0, "op": "cor"},
            {"a": 7, "b": 0, "op": "sid"}, {"a": 7, "b": 0, "op": "cor"},
            {"a": 8, "b": 0, "op": "sid"}, {"a": 8, "b": 0, "op": "cor"},
            {"a": 10, "b": 0, "op": "sid"}, {"a": 10, "b": 0, "op": "cor"},
        ],
    },
    {
        "id": "entry-u9-what-comes-next", "course": "entry", "unit": 9,
        "topic": "What comes next",
        "op": "pat", "max_value": 30,
        "levels": ("abstract",),
        "symbols": ("pattern",),
        "advance_line": ("Three in a row — you've got it! "
                         "You can find what comes next in a pattern."),
        "teach": [
            ("A pattern is numbers that follow a rule. Find the jump from one "
             "number to the next, then use that jump again.",
             '[[goal text="What comes next"]]'),
            ("Watch me. 4, 7, 10, 13. From 4 to 7 is a jump of 3. Check it: 7 "
             "to 10 is 3, and 10 to 13 is 3. So next is 13 and 3 more — 16.",
             '[[step eq="4, 7, 10, 13, ? — jump of 3"]]'),
            ("One more, watch. 9, 14, 19, 24. The jump is 5 every time, so next "
             "is 24 and 5 more — 29.",
             '[[step eq="9, 14, 19, 24, ? — jump of 5"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 3, 7, 11, 15. The jump "
                        "is 4 every time, so next is 15 and 4 more — 19.",
                        '[[step eq="3, 7, 11, 15, ? — jump of 4"]]'),
             "ask": {"a": 3, "b": 2, "op": "pat"}},
            {"worked": ("One more together. 6, 8, 10, 12. The jump is 2, so "
                        "next is 12 and 2 more — 14.",
                        '[[step eq="6, 8, 10, 12, ? — jump of 2"]]'),
             "ask": {"a": 7, "b": 4, "op": "pat"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            # ⚠️ NO JUMP OF ONE IN THE TAUGHT BANK. "1, 2, 3, 4 -- what comes
            # next?" is counting, not a pattern, and the ramp keys on the jump, so
            # three of them would have opened the practice -- a step DOWN from
            # teach beats that work jumps of 3 and 5. The op still allows a jump of
            # one so Abrabot's pool can offer an easy rung; the LESSON starts at
            # the smallest jump a child has to actually look for.
            {"a": 2, "b": 2, "op": "pat"}, {"a": 5, "b": 2, "op": "pat"},
            {"a": 9, "b": 2, "op": "pat"}, {"a": 1, "b": 3, "op": "pat"},
            {"a": 5, "b": 3, "op": "pat"}, {"a": 8, "b": 3, "op": "pat"},
            {"a": 2, "b": 4, "op": "pat"}, {"a": 6, "b": 4, "op": "pat"},
            {"a": 9, "b": 4, "op": "pat"}, {"a": 1, "b": 5, "op": "pat"},
            {"a": 4, "b": 5, "op": "pat"}, {"a": 6, "b": 5, "op": "pat"},
        ],
    },
    {
        "id": "entry-u9-equal-groups", "course": "entry", "unit": 9,
        "topic": "Equal groups",
        "op": "grp", "max_value": 25,
        "levels": ("abstract",),
        "symbols": ("group",),
        "advance_line": ("Three in a row — you've got it! "
                         "You can count equal groups."),
        "teach": [
            ("When every group holds the same amount, you do not have to count "
             "one at a time. Count by the size of one group instead.",
             '[[goal text="Equal groups"]]'),
            ("Watch me. 3 groups with 5 stars in each. Count by five: 5, 10, "
             "15. That is 15 stars in all.",
             '[[step eq="3 groups of 5 = 15"]]'),
            ("One more, watch. 4 groups with 2 stars in each. Count by two: 2, "
             "4, 6, 8. That is 8 stars in all.",
             '[[step eq="4 groups of 2 = 8"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 5 groups with 4 stars "
                        "in each. Count by four: 4, 8, 12, 16, 20. That is 20 "
                        "stars in all.",
                        '[[step eq="5 groups of 4 = 20"]]'),
             "ask": {"a": 2, "b": 2, "op": "grp"}},
            {"worked": ("One more together. 2 groups with 5 stars in each. 5, "
                        "10. That is 10 stars in all.",
                        '[[step eq="2 groups of 5 = 10"]]'),
             "ask": {"a": 3, "b": 4, "op": "grp"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            # (3,5) is NOT here on purpose -- teach beat two works it out loud.
            {"a": 2, "b": 3, "op": "grp"}, {"a": 3, "b": 2, "op": "grp"},
            {"a": 2, "b": 4, "op": "grp"}, {"a": 3, "b": 3, "op": "grp"},
            {"a": 4, "b": 3, "op": "grp"}, {"a": 5, "b": 3, "op": "grp"},
            {"a": 4, "b": 4, "op": "grp"}, {"a": 4, "b": 5, "op": "grp"},
            {"a": 5, "b": 5, "op": "grp"},
        ],
    },
    {
        "id": "entry-u9-sharing-fairly", "course": "entry", "unit": 9,
        "topic": "Sharing fairly",
        "op": "eqs", "max_value": 30,
        "levels": ("abstract",),
        "symbols": ("equal",),
        "advance_line": ("Three in a row — you've got it! "
                         "You can share a pile into equal groups."),
        "teach": [
            ("Sharing fairly means every group ends up with the same amount — "
             "equal groups, none of them bigger than another.",
             '[[goal text="Sharing fairly"]]'),
            ("Watch me. 12 stars shared into 4 groups. Deal them out one at a "
             "time, round and round. Every group ends with 3.",
             '[[step eq="12 shared into 4 equal groups = 3 each"]]'),
            ("One more, watch. 15 stars shared into 5 groups. Deal them round "
             "and round, and every group ends with 3.",
             '[[step eq="15 shared into 5 equal groups = 3 each"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 20 stars shared into 4 "
                        "groups. Deal them round and round — 5 in each group.",
                        '[[step eq="20 shared into 4 equal groups = 5 each"]]'),
             "ask": {"a": 6, "b": 2, "op": "eqs"}},
            {"worked": ("One more together. 25 stars shared into 5 groups. "
                        "Every group ends with 5.",
                        '[[step eq="25 shared into 5 equal groups = 5 each"]]'),
             "ask": {"a": 9, "b": 3, "op": "eqs"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 4, "b": 2, "op": "eqs"}, {"a": 6, "b": 3, "op": "eqs"},
            {"a": 8, "b": 2, "op": "eqs"}, {"a": 8, "b": 4, "op": "eqs"},
            {"a": 10, "b": 5, "op": "eqs"}, {"a": 10, "b": 2, "op": "eqs"},
            {"a": 12, "b": 3, "op": "eqs"}, {"a": 15, "b": 3, "op": "eqs"},
            {"a": 16, "b": 4, "op": "eqs"}, {"a": 18, "b": 3, "op": "eqs"},
            {"a": 24, "b": 4, "op": "eqs"}, {"a": 30, "b": 5, "op": "eqs"},
        ],
    },
]
LESSONS.extend(_ENTRY_MORE)

# ---- this course's slice of COURSE_ORDER: the teaching order (lessons/__init__.py joins the ten) ----
ORDER = [
    # ---- ENTRY-LEVEL MATH (the kc re-cut: these eight lessons were authored under
    # Basic U1 and belong here by Jim's own curriculum -- Eureka audit 2026-08-21;
    # kd opens the course where Eureka does -- counting -- and adds story problems
    # and coins) ----
    # (pg) THE COURSE IS NINE UNITS OF FOUR NOW. Sixteen lessons were added so a
    # five-year-old stops falling out of the authored lane onto the slow one. Each
    # new lesson sits where it is TAUGHT, not at the end: counting past ten before
    # comparing, doubles before three-in-a-row, no-regrouping take away before the
    # regrouping lesson that was already here, and coins in coin order -- nickels,
    # dimes, quarters, then change.
    "entry-u1-counting-to-10", "entry-u1-counting-past-ten",
    "entry-u1-numbers-before-and-after", "entry-u1-which-is-bigger",
    "entry-u2-add-single-digit", "entry-u2-doubles",
    "entry-u2-add-past-ten", "entry-u2-adding-three-numbers",
    "entry-u3-take-away-single-digit", "entry-u3-take-away-bigger",
    "entry-u3-the-missing-part", "entry-u3-story-problems",
    "entry-u4-tens-and-ones", "entry-u4-hundreds-tens-and-ones",
    "entry-u4-ten-more", "entry-u4-what-a-digit-is-worth",
    "entry-u5-add-two-digit-no-carry", "entry-u5-add-with-carrying",
    "entry-u5-crossing-a-hundred", "entry-u5-adding-three-digit-numbers",
    "entry-u6-take-away-two-digit", "entry-u6-take-away-with-regrouping",
    "entry-u6-take-away-three-digit", "entry-u6-checking-by-adding-back",
    "entry-u7-counting-coins", "entry-u7-dimes-and-pennies",
    "entry-u7-quarters", "entry-u7-making-change",
    # (mo) Unit 8 -- Time, Calendar & Measurement. The clock lessons come after
    # coins on purpose: counting by five is learned on nickels first, and the
    # minute hand is the same count on a rounder board.
    "entry-u8-later-on-the-clock", "entry-u8-minutes-past-the-hour",
    "entry-u8-weeks-and-days", "entry-u8-how-much-longer",
    # (mp) Unit 9 -- Shapes, Patterns & Groups. THE LAST UNSCRIPTED UNIT. Groups
    # come after patterns because counting equal groups IS a pattern with a jump.
    "entry-u9-sides-and-corners", "entry-u9-what-comes-next",
    "entry-u9-equal-groups", "entry-u9-sharing-fairly",
]

# I did no harm and this file is not truncated.

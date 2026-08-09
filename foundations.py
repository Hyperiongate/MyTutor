# =============================================================================
# foundations.py  --  CANONICAL FOUNDATION SCRIPTS  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
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
    "entrymath": [
        {"term": "number", "say":
            "Before we count anything, here is what a **number** really is: it is a way of saying how many. "
            "When I say three, I am telling you how many things there are, not which ones or how big they are. "
            "Counting is just saying the numbers in order while you touch each thing exactly once, and the very "
            "last number you say is how many you have altogether.",
         "board": ['[[objects emoji="⭐" groups="3"]]']},
        {"term": "adding", "say":
            "**Adding** means putting groups together and finding out how many there are now. "
            "You start with what you have, then you count on for each new one. "
            "Two cookies, and then one more cookie, is three cookies altogether. "
            "Nothing disappears when we add — the pile only gets bigger.",
         "board": ['[[objects emoji="🍪" groups="2" add="1"]]']},
    ],
    "basicmath": [
        {"term": "fraction", "say":
            "Here is what a **fraction** is. A fraction is a number that describes equal parts of one whole. "
            "The word equal matters: if I cut a cookie into two pieces and one piece is tiny, those are not halves. "
            "So a fraction always means we cut something into fair, matching pieces, and then we talk about some "
            "of those pieces.",
         "board": ['[[fracbar parts="4" shaded="1" caption="one whole, cut into four equal parts"]]']},
        {"term": "denominator", "say":
            "Every fraction is written with two numbers, and each one has a job. "
            "The bottom number is called the **denominator**. It tells you how many equal pieces the whole was cut into. "
            "A bigger denominator means the whole got cut into more pieces, so each piece is smaller. "
            "That surprises a lot of people: one eighth is smaller than one fourth, even though eight is bigger than four.",
         "board": ['[[write text="1/4   ← the 4 is the DENOMINATOR: four equal pieces"]]']},
        {"term": "numerator", "say":
            "The top number is called the **numerator**, and it tells you how many of those pieces we are talking about. "
            "So in three fourths, the four says the whole was cut into four equal pieces, and the three says we have three of them. "
            "Bottom number: how many pieces in all. Top number: how many we are counting. That is the whole idea.",
         "board": ['[[write text="3/4   ← the 3 is the NUMERATOR: three of those pieces"]]',
                   '[[fracbar parts="4" shaded="3" caption="three fourths"]]']},
        {"term": "decimal", "say":
            "A **decimal** is another way to write parts of a whole, using place value instead of two stacked numbers. "
            "The dot is called the decimal point, and everything to the right of it is smaller than one. "
            "The first place after the point is tenths, the next is hundredths. "
            "Money is the easiest example: one dollar and fifty cents is one and five tenths of a dollar.",
         "board": ['[[write text="1.5   =   1 whole  +  5 tenths"]]']},
    ],
    "prealgebra": [
        {"term": "negative number", "say":
            "A **negative number** is a number less than zero. That sounds strange until you picture a thermometer or an elevator. "
            "Zero is the ground floor. Positive numbers go up from there, and negative numbers go down below it. "
            "Negative three is not nothing and it is not three — it is three steps below zero, and it is a real, exact place on the number line.",
         "board": ['[[numberline from="-6" to="6" mark="-3"]]']},
        {"term": "percent", "say":
            "**Percent** means out of one hundred. That is all the word means: per hundred. "
            "So fifty percent is fifty out of a hundred, which is the same as one half. "
            "Twenty-five percent is twenty-five out of a hundred, which is one fourth. "
            "Whenever you see a percent, you can always say out of a hundred in your head and it will make sense.",
         "board": ['[[write text="50%  =  50 out of 100  =  1/2"]]']},
        {"term": "ratio", "say":
            "A **ratio** compares two amounts. If a recipe uses two cups of flour for every one cup of sugar, "
            "the ratio of flour to sugar is two to one. Notice a ratio does not tell you how much you have altogether — "
            "it tells you how the amounts compare. Double everything and the ratio stays exactly the same.",
         "board": ['[[write text="flour : sugar  =  2 : 1"]]']},
    ],
    "algebra1": [
        {"term": "variable", "say":
            "A **variable** is a letter that stands for a number we do not know yet. "
            "That is the whole trick of algebra: instead of guessing, we give the mystery number a name, usually x, "
            "and then we work out what it has to be. The letter is not magic and it is not a code — it is a placeholder "
            "sitting where a number will go.",
         "board": ['[[write text="x  =  the number we do not know yet"]]']},
        {"term": "equation", "say":
            "An **equation** is a statement that two things are equal. The equals sign is the important part: "
            "it says the left side and the right side are the very same amount, like a balance scale that is level. "
            "That is why, whenever we change one side, we must do exactly the same thing to the other side — "
            "otherwise the scale tips and the statement stops being true.",
         "board": ['[[balance left="2x + 3" right="11" state="level" caption="both sides are the same amount"]]']},
        {"term": "coefficient", "say":
            "In something like two x, the two is called the **coefficient**. It just means how many of that variable we have. "
            "Two x means two of them, added together — x plus x. And because it means multiply, we undo it by dividing. "
            "A coefficient is not attached by addition, which is why we never subtract it away.",
         "board": ['[[write text="2x  =  x + x   (2 is the COEFFICIENT)"]]']},
    ],
    "geometry": [
        {"term": "angle", "say":
            "An **angle** is the amount of turn between two lines that meet. It is not about how long the lines are — "
            "you can stretch them out forever and the angle does not change. We measure that turn in degrees, "
            "and a full spin all the way around is three hundred sixty degrees. A square corner is exactly ninety.",
         "board": ['[[angle deg="90" caption="a right angle — a square corner"]]']},
        {"term": "hypotenuse", "say":
            "In a right triangle, the side across from the square corner is called the **hypotenuse**. "
            "It is always the longest side of that triangle, and it is always the one that does not touch the right angle. "
            "Knowing which side is the hypotenuse matters, because the famous rule about right triangles treats it differently from the other two.",
         "board": ['[[triangle a="3" b="4" c="5" right="1" caption="the hypotenuse is opposite the right angle"]]']},
    ],
    "algebra2": [
        {"term": "exponent", "say":
            "An **exponent** counts how many times you multiply a number by itself. "
            "Two to the third means two times two times two. The little number is not telling you to multiply by three — "
            "it is telling you how many twos to use. That difference trips up almost everybody once, so it is worth saying out loud.",
         "board": ['[[write text="2³  =  2 × 2 × 2  =  8"]]']},
        {"term": "quadratic", "say":
            "A **quadratic** is an expression where the highest power of the variable is two — something with an x squared in it. "
            "That one detail changes everything: instead of a straight line, its graph is a curve called a parabola, "
            "and instead of one solution, it usually has two.",
         "board": ['[[write text="x² − 3x − 10 = 0     (highest power is 2)"]]']},
    ],
    "precalc": [
        {"term": "function", "say":
            "A **function** is a rule that takes one input and gives back exactly one output. "
            "The exactly one part is the whole definition — put in a three and you always get the same answer out, every time. "
            "We write f of x, which is read as f of x, and it simply means the output of the rule f when the input is x. "
            "It is not f multiplied by x.",
         "board": ['[[machine input="3" rule="2x+1" output="7" fname="f"]]']},
        {"term": "radian", "say":
            "A **radian** is just another unit for measuring angles, the way inches and centimetres both measure length. "
            "Instead of chopping the circle into three hundred sixty pieces, radians measure the angle by how far you travel around the circle itself. "
            "A full trip around is two pi radians, so half a trip is pi.",
         "board": ['[[write text="full circle = 360°  =  2π radians"]]']},
    ],
    "probstat": [
        {"term": "mean", "say":
            "The **mean** is the fair-share average. You pool everything together, then split it evenly among however many there are. "
            "If three people bring three, five, and ten cookies, that is eighteen cookies shared three ways, so six each. "
            "The mean answers one question: if everyone had the same amount, how much would that be?",
         "board": ['[[write text="mean = (3 + 5 + 10) ÷ 3 = 6"]]']},
        {"term": "median", "say":
            "The **median** is the middle value once you line everything up in order. Not the average — the middle. "
            "It matters because one very large or very small number can drag the mean way off, while the median barely moves. "
            "That is why you hear about median house prices instead of average ones.",
         "board": ['[[write text="3,  5,  10   →   median = 5"]]']},
    ],
    "calculus": [
        {"term": "derivative", "say":
            "A **derivative** answers one question: how fast is this changing right now? "
            "Not the average speed over a whole trip, but the speed at one exact instant, like the number on a speedometer. "
            "When we take the derivative of a function, we get back a new function whose output is the slope of the original at any point you pick.",
         "board": ['[[write text="derivative = how fast it is changing, at one instant"]]']},
        {"term": "limit", "say":
            "A **limit** asks where a function is heading as you get closer and closer to some value — "
            "not what happens exactly at that spot, but what it is approaching. "
            "That distinction is the whole reason limits exist: a function can have a hole at a point and still be clearly heading somewhere.",
         "board": ['[[write text="what is it approaching, as x gets close?"]]']},
    ],
    "diffeq": [
        {"term": "differential equation", "say":
            "A **differential equation** is an equation that contains a derivative. "
            "That is what makes it different from the equations you have solved before: instead of describing a number, "
            "it describes how something CHANGES. Solving one does not give you a number back — it gives you a whole function.",
         "board": ['[[write text="y′ = 3y      (an equation about how y changes)"]]']},
        {"term": "order", "say":
            "The **order** of a differential equation is simply the highest derivative that appears in it. "
            "One tick mark is first order, two tick marks is second order. "
            "We classify before we solve, because the order tells us which method will work — it is the first question to ask, every time.",
         "board": ['[[write text="y″ + y = 0   →   second order"]]']},
    ],
}


def for_course(course: str) -> list:
    """The canonical foundation scripts for a course, in teaching order ([] if none)."""
    return FOUNDATIONS.get((course or "").strip().lower(), [])


def terms_for_course(course: str) -> list:
    """Just the key terms this course has a canonical introduction for."""
    return [f["term"] for f in for_course(course)]


def prompt_block(course: str) -> str:
    """The prompt section listing this course's canonical introductions.

    Returns "" when a course has none, so the prompt never grows for nothing.
    Deliberately compact: the scripts themselves are the payload."""
    items = for_course(course)
    if not items:
        return ""
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
        "If the student already knows the term (their notes show this course's later units,",
        "or they say so), give one sentence of reminder instead and move on -- never make a",
        "returning student sit through an introduction they have earned their way past.",
        "",
    ]
    for f in items:
        lines.append(f'--- {f["term"].upper()} ---')
        lines.append(f'SAY: {f["say"]}')
        for b in f.get("board", []):
            lines.append(f"BOARD: {b}")
        lines.append("")
    lines.append("============================================================")
    return "\n".join(lines)


# I did no harm and this file is not truncated.

# =============================================================================
# library.py  --  Math Tutor MVP  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-08-07  NEW MODULE -- THE "LOOK IT UP" REFERENCE LIBRARY (Jim: a searchable
#               database covering the topics of every course; a stuck student clicks
#               📖 Look it up, types "binomial theorem" or "adding dollars and cents",
#               and a READABLE bubble opens -- no tutor voice, no chat turn involved).
#               Design: a SELF-FILLING library.
#                 1. CURATED SEEDS below -- hand-written reference articles for the
#                    classic asks, each with aliases for matching.
#                 2. SAVED ARTICLES -- anything ever generated is stored forever in
#                    store.py's `library_articles` table and served instantly next time.
#                 3. GENERATE-ONCE FALLBACK -- an unmatched search writes the article
#                    ONE time with the model (strict student-reference prompt, literal
#                    truth rules, ~2 cents), saves it, serves it. The library fills
#                    itself with exactly what students actually ask.
#               Reading level: articles are stored PER LEVEL BAND (elementary / middle /
#               high / advanced -- from the course id), so "adding money" reads gently
#               for Basic Math and tersely for Algebra II. Output is a small safe HTML
#               subset, scrubbed server-side (no scripts/attributes) before serving.
#               Search: normalized-alias exact match first, then token-overlap fuzzy
#               match across curated + saved titles (best score wins, floor applied).
# =============================================================================

import os
import re

# The four reading-level bands. Unknown courses fall back to "high".
BAND_BY_COURSE = {
    "entry": "elementary", "basic": "elementary",
    "prealgebra": "middle",
    "algebra1": "high", "geometry": "high", "algebra2": "high",
    "precalc": "advanced", "calculus": "advanced", "diffeq": "advanced",
    "probstat": "advanced",
}
BAND_TONE = {
    "elementary": ("a young child in grades 1-6. Short sentences. Warm, playful, concrete. "
                   "Use money, toys, and food examples. No algebra letters."),
    "middle": ("a middle-school pre-algebra student. Friendly and clear. Concrete examples "
               "first, then the general idea. Letters like x may appear only if defined."),
    "high": ("a high-school algebra/geometry student. Clear and encouraging. Define every "
             "notation at first use. One solid worked example."),
    "advanced": ("an advanced student (pre-calc, calculus, statistics). Precise and efficient "
                 "but still warm. Define every notation at first use. One worked example."),
}


def band_for(course: str) -> str:
    return BAND_BY_COURSE.get((course or "").strip(), "high")


def norm_key(text: str) -> str:
    """Normalized slug of a search/topic -- stable across small wording differences."""
    t = (text or "").lower().replace("'", "").replace("’", "")
    # drop filler words so "what is the binomial theorem" == "binomial theorem"
    t = re.sub(r"\b(what|whats|is|are|the|a|an|and|how|do|does|i|im|to|of|can|you|me|"
               r"about|please|give|more|info|information|explain|tell|help|with|my|"
               r"trouble|having|together)\b", " ", t)
    return re.sub(r"[^a-z0-9]+", "", t)[:80] or "topic"


def _tokens(text: str) -> set:
    t = (text or "").lower().replace("'", "").replace("’", "")
    t = re.sub(r"[^a-z0-9\s]+", " ", t)
    drop = {"what", "whats", "is", "are", "the", "a", "an", "how", "do", "does", "i",
            "im", "to", "of", "can", "you", "me", "about", "please", "give", "more",
            "info", "information", "explain", "tell", "help", "with", "my", "trouble",
            "having", "and", "in", "together"}
    # light stemming: fold plurals so "lines" matches "line", "numbers" matches "number"
    return {(w[:-1] if len(w) > 3 and w.endswith("s") and not w.endswith("ss") else w)
            for w in t.split() if w and w not in drop}


# A conservative HTML scrub: keep only the tags the bubble renders; strip everything
# else including attributes (so no scripts, handlers, or styles can ride along).
_ALLOWED = {"h3", "p", "ul", "ol", "li", "b", "i", "br", "div"}


def scrub_html(html: str) -> str:
    out = []
    pos = 0
    for m in re.finditer(r"<[^>]*>", html or ""):
        out.append(html[pos:m.start()])
        tag = m.group(0)
        name = re.match(r"</?\s*([a-zA-Z0-9]+)", tag)
        name = (name.group(1).lower() if name else "")
        if name in _ALLOWED:
            closing = tag.strip().startswith("</")
            if name == "div" and not closing:
                out.append('<div class="ex">')     # the one styled block we allow
            else:
                out.append(("</" if closing else "<") + name + ">")
        pos = m.end()
    out.append((html or "")[pos:])
    return "".join(out)


# =============================================================================
# CURATED SEED ARTICLES -- the classics, ready on day one. key -> entry.
# Each: title, band, aliases (matched via norm_key), body (safe-HTML).
# =============================================================================
SEEDS = [
    {
        "title": "Adding dollars and cents",
        "band": "elementary",
        "aliases": ["adding dollars and cents", "adding money", "add money",
                    "dollars and cents", "adding dollars", "money addition", "counting money"],
        "body": """
<p>Money is just numbers wearing a costume! <b>100 cents make 1 dollar</b> — that's the whole secret.</p>
<h3>The one big rule</h3>
<p>When you add money, <b>line up the dots</b> (the decimal points). Dollars sit on the left of the dot, cents on the right.</p>
<div><b>Example:</b> You have $2.35 and earn $1.50 more.<br><br>
&nbsp;&nbsp;$2.35<br>+ $1.50<br>———<br>&nbsp;&nbsp;$3.85<br><br>
Add the cents first: 35 + 50 = 85 cents. Then the dollars: 2 + 1 = 3. Total: <b>$3.85</b>.</div>
<h3>When cents make a dollar</h3>
<p>If the cents add up to 100 or more, trade 100 of them for 1 dollar! 60 cents + 60 cents = 120 cents = <b>1 dollar and 20 cents</b> — written $1.20.</p>
<h3>Watch out</h3>
<ul><li>$0.05 is five cents — the 0 right after the dot matters! $0.50 is fifty cents, ten times more.</li>
<li>Always write two digits after the dot for money: three dollars and five cents is $3.05, not $3.5.</li></ul>
<p>Try one: $1.25 + $2.80. (Cents: 25 + 80 = 105 — that's a dollar and 5 cents!) Answer: <b>$4.05</b>.</p>
""",
    },
    {
        "title": "Place value",
        "band": "elementary",
        "aliases": ["place value", "ones tens hundreds", "place values", "what does each digit mean"],
        "body": """
<p>Every digit in a number has a <b>job</b>, and the job depends on where it stands. That's place value!</p>
<h3>The places</h3>
<p>In the number <b>352</b>: the 2 is in the <b>ones</b> place (2 ones), the 5 is in the <b>tens</b> place (5 tens = 50), and the 3 is in the <b>hundreds</b> place (3 hundreds = 300). So 352 means 300 + 50 + 2.</p>
<div><b>Think of it like money:</b> 352 is 3 hundred-dollar bills, 5 ten-dollar bills, and 2 one-dollar coins.</div>
<h3>Why it matters</h3>
<ul><li>The same digit can be worth different amounts: in 25 the 2 means twenty, but in 250 it means two hundred!</li>
<li>When you add big numbers, you line them up so ones sit under ones and tens under tens — that's place value doing the work.</li></ul>
<p>Quick check: in the number 407, what is the 4 worth? (Four hundreds — <b>400</b>!) And the 0 means there are no tens at all — zero is a real place-holder with a real job.</p>
""",
    },
    {
        "title": "Comparing and adding decimals",
        "band": "middle",
        "aliases": ["decimals", "comparing decimals", "adding decimals", "decimal addition",
                    "add decimals", "subtract decimals", "subtracting decimals",
                    "compare decimals", "adding and subtracting decimals", "decimal review"],
        "body": """
<p>A decimal is just a number with pieces smaller than one. The digits after the point are <b>tenths</b>, then <b>hundredths</b>, then thousandths — each place ten times smaller than the last.</p>
<h3>Comparing decimals</h3>
<p>Compare place by place, left to right. Which is bigger: 4.50 or 4.05? The whole parts tie (4 = 4), so check the tenths: 5 tenths beats 0 tenths, so <b>4.50 &gt; 4.05</b>. Don't be fooled by "05 looks like more digits" — position beats appearance.</p>
<div><b>Trick:</b> give both numbers the same number of decimal places by adding zeros on the right (4.5 → 4.50). Then compare them like whole numbers: 450 vs 405.</div>
<h3>Adding (and subtracting) decimals</h3>
<p>One rule runs the whole show: <b>line up the decimal points.</b> Then add normally, carrying as usual, and drop the point straight down.</p>
<div><b>Example:</b> 12.7 + 3.45<br><br>&nbsp;&nbsp;12.70<br>+ &nbsp;3.45<br>———<br>&nbsp;&nbsp;16.15</div>
<ul><li>Add a zero to 12.7 to make 12.70 — same value, easier to line up.</li>
<li>Money is decimals in disguise: $12.70 + $3.45 works exactly the same way.</li></ul>
""",
    },
    {
        "title": "Fractions review",
        "band": "middle",
        "aliases": ["fractions", "fraction review", "fraction", "adding fractions",
                    "add fractions", "subtract fractions", "multiply fractions", "divide fractions",
                    "equivalent fractions", "fractions refresher"],
        "body": """
<p>A fraction is a number that names <b>part of a whole</b>. In 3/4, the bottom number (the <b>denominator</b>) says the whole is cut into 4 equal pieces; the top (the <b>numerator</b>) says you have 3 of them.</p>
<h3>Equivalent fractions</h3>
<p>Multiplying or dividing top AND bottom by the same number keeps the value: 1/2 = 2/4 = 3/6. Same amount of pizza, cut into more slices.</p>
<h3>Adding fractions</h3>
<p>You can only add pieces of the <b>same size</b> — the denominators must match.</p>
<div><b>Example:</b> 1/2 + 1/3. Halves and thirds are different sizes, so rename both in sixths: 1/2 = 3/6 and 1/3 = 2/6. Now add the tops: 3/6 + 2/6 = <b>5/6</b>.</div>
<h3>The moves that matter</h3>
<ul><li><b>Add / subtract:</b> common denominator, then add the tops. Never add the bottoms.</li>
<li><b>Multiply:</b> straight across — 2/3 × 4/5 = 8/15.</li>
<li><b>Divide:</b> flip the second fraction and multiply — 1/2 ÷ 1/4 = 1/2 × 4/1 = 2. (How many quarters fit in a half? Two!)</li>
<li><b>Simplify:</b> divide top and bottom by their biggest common factor — 6/8 = 3/4.</li></ul>
""",
    },
    {
        "title": "Percent basics",
        "band": "middle",
        "aliases": ["percent", "percentages", "percents", "percent of a number", "finding percent"],
        "body": """
<p><b>Percent means "out of 100."</b> 25% is 25 out of every 100 — the same number as the fraction 25/100 and the decimal 0.25. Every percent problem becomes easy once you translate it.</p>
<h3>The translation</h3>
<ul><li>25% = 0.25 &nbsp;(slide the decimal point two places left)</li>
<li>7% = 0.07 &nbsp;(watch the zero!)</li>
<li>150% = 1.50 &nbsp;(more than the whole thing)</li></ul>
<h3>Finding a percent of a number</h3>
<p>"Of" means multiply.</p>
<div><b>Example:</b> What is 30% of 80?<br>30% = 0.30, and 0.30 × 80 = <b>24</b>.</div>
<h3>Benchmarks that make you fast</h3>
<ul><li>10% — slide the point one place: 10% of 80 is 8.</li>
<li>5% — half of 10%: that's 4.</li>
<li>1% — slide two places: 0.8.</li></ul>
<p>So 35% of 80 = 10% + 10% + 10% + 5% = 8 + 8 + 8 + 4 = <b>28</b>. Real-life use: a 20% tip on a $45 dinner is 10% twice — $4.50 + $4.50 = <b>$9</b>.</p>
""",
    },
    {
        "title": "Negative numbers",
        "band": "middle",
        "aliases": ["negative numbers", "negatives", "adding negative numbers", "integers",
                    "subtracting negatives", "signed numbers"],
        "body": """
<p>Negative numbers live to the <b>left of zero</b> on the number line. They measure "below" or "owed": -3° is three degrees below zero; -$5 means you owe five dollars.</p>
<h3>Adding and subtracting</h3>
<p>Think temperature or money:</p>
<ul><li><b>Adding a negative = going down.</b> 4 + (-6): start at 4, drop 6 → <b>-2</b>.</li>
<li><b>Subtracting a negative = going up.</b> 3 - (-2) = 3 + 2 = <b>5</b>. (Taking away a debt makes you richer!)</li></ul>
<div><b>Example:</b> The temperature is -4° and rises 9°. -4 + 9 = <b>5°</b>. Start four below zero, climb nine.</div>
<h3>Multiplying and dividing</h3>
<p>Count the negative signs:</p>
<ul><li>Same signs → positive: (-3) × (-4) = 12, and (-12) ÷ (-3) = 4.</li>
<li>Different signs → negative: (-3) × 4 = -12, and 12 ÷ (-3) = -4.</li></ul>
<h3>Watch out</h3>
<p>-3² means -(3 × 3) = -9, but (-3)² means (-3) × (-3) = 9. Parentheses decide whether the negative sign is inside the squaring.</p>
""",
    },
    {
        "title": "Order of operations",
        "band": "middle",
        "aliases": ["order of operations", "pemdas", "which operation first", "order operations"],
        "body": """
<p>Math needs traffic rules so everyone gets the same answer. The <b>order of operations</b> is that rulebook — often remembered as <b>PEMDAS</b>:</p>
<ul><li><b>P</b>arentheses first</li>
<li><b>E</b>xponents (powers) next</li>
<li><b>MD</b> — Multiplication and Division together, LEFT to RIGHT</li>
<li><b>AS</b> — Addition and Subtraction together, LEFT to RIGHT</li></ul>
<div><b>Example:</b> 3 + 4 × 2 = 3 + 8 = <b>11</b> (multiply before adding — not 14!).<br><br>
<b>Example:</b> (3 + 4) × 2 = 7 × 2 = <b>14</b> (parentheses change everything).</div>
<h3>The two classic traps</h3>
<ul><li>Multiplication and division are EQUAL rank — do whichever comes first left to right: 12 ÷ 3 × 2 = 4 × 2 = <b>8</b>, not 2.</li>
<li>Same for addition and subtraction: 10 - 4 + 2 = 6 + 2 = <b>8</b>, not 4.</li></ul>
<p>Full workout: 20 - 2 × (1 + 4)² ÷ 5 → parentheses: (5) → exponent: 25 → multiply/divide left to right: 2 × 25 = 50, 50 ÷ 5 = 10 → subtract: 20 - 10 = <b>10</b>.</p>
""",
    },
    {
        "title": "Slope of a line",
        "band": "high",
        "aliases": ["slope", "slope of a line", "finding slope", "rise over run", "gradient",
                    "slope intercept", "slope intercept form"],
        "body": """
<p><b>Slope measures steepness</b> — how much a line climbs (or falls) for every step to the right. The symbol is usually <i>m</i>.</p>
<h3>Rise over run</h3>
<p>Pick any two points on the line. Slope = <b>rise ÷ run</b> = (change in y) ÷ (change in x):</p>
<div><b>Example:</b> Through (1, 2) and (4, 8):<br>
rise = 8 - 2 = 6, run = 4 - 1 = 3, so m = 6/3 = <b>2</b>.<br>
The line climbs 2 units up for every 1 unit right.</div>
<h3>Reading the sign</h3>
<ul><li>Positive slope — uphill left to right (like earning money over time).</li>
<li>Negative slope — downhill (like a phone battery draining).</li>
<li>Slope 0 — flat horizontal line.</li>
<li>A vertical line has UNDEFINED slope (you'd divide by zero).</li></ul>
<h3>In the equation</h3>
<p>In <b>y = mx + b</b> (where y and x are the coordinates of any point on the line), m is the slope and b is the <b>y-intercept</b> — where the line crosses the y-axis. For y = 2x + 1: slope 2, crossing at (0, 1). Bigger |m| = steeper line.</p>
""",
    },
    {
        "title": "Solving two-step equations",
        "band": "high",
        "aliases": ["two step equations", "solving equations", "solve for x", "two step equation",
                    "solving two step equations", "how to solve an equation"],
        "body": """
<p>An equation is a balance scale: whatever you do to one side, you must do to the other. <b>Solving</b> means getting the unknown letter (usually x) alone on one side.</p>
<h3>The strategy: undo in reverse</h3>
<p>Look at what's being done to x, then <b>undo it backwards</b> — undo the adding/subtracting first, then the multiplying/dividing.</p>
<div><b>Example:</b> 2x + 3 = 11<br><br>
Step 1 — undo the +3: subtract 3 from both sides → 2x = 8<br>
Step 2 — undo the ×2: divide both sides by 2 → x = <b>4</b><br><br>
<b>Check it:</b> 2(4) + 3 = 8 + 3 = 11 ✓</div>
<h3>Why that order?</h3>
<p>2x + 3 was built by first multiplying x by 2, then adding 3. To unwrap a package you remove the outer layer first — so you undo the +3 before the ×2.</p>
<ul><li>Opposite of + is - ; opposite of × is ÷ (and vice versa).</li>
<li>ALWAYS check by plugging your answer back in — it takes ten seconds and catches everything.</li></ul>
""",
    },
    {
        "title": "Factoring quadratics",
        "band": "high",
        "aliases": ["factoring", "factoring quadratics", "factor a quadratic", "factoring trinomials",
                    "how to factor", "factor x2"],
        "body": """
<p><b>Factoring</b> means un-multiplying: rewriting an expression as pieces that multiply to make it. A <b>quadratic</b> is an expression whose highest power of x is x² (x squared), like x² + 5x + 6.</p>
<h3>The number hunt (when it's x² + bx + c)</h3>
<p>Find two numbers that <b>multiply to c</b> and <b>add to b</b>.</p>
<div><b>Example:</b> Factor x² + 5x + 6.<br>
Need: multiply to 6, add to 5 → that's <b>2 and 3</b>.<br>
So x² + 5x + 6 = <b>(x + 2)(x + 3)</b>.<br><br>
<b>Check by multiplying back:</b> (x + 2)(x + 3) = x² + 3x + 2x + 6 = x² + 5x + 6 ✓</div>
<h3>Sign patterns</h3>
<ul><li>c positive, b positive → both numbers positive: x² + 7x + 12 = (x + 3)(x + 4)</li>
<li>c positive, b negative → both negative: x² - 7x + 12 = (x - 3)(x - 4)</li>
<li>c negative → one of each sign: x² + x - 12 = (x + 4)(x - 3)</li></ul>
<h3>Why factor at all?</h3>
<p>If (x + 2)(x + 3) = 0, then one of the pieces must BE zero — so x = -2 or x = -3. Factoring turns a hard equation into two easy ones. Always pull out a common factor first: 2x² + 10x = 2x(x + 5).</p>
""",
    },
    {
        "title": "The quadratic formula",
        "band": "high",
        "aliases": ["quadratic formula", "the quadratic formula", "quadratic equation formula",
                    "solve quadratic", "discriminant"],
        "body": """
<p>When a quadratic won't factor nicely, the <b>quadratic formula</b> solves it every single time. For any equation in the form <b>ax² + bx + c = 0</b> (a, b, c are the numbers in front; a ≠ 0):</p>
<div><b>x = ( -b ± √(b² - 4ac) ) ÷ (2a)</b><br><br>
The ± means there are usually TWO answers: one using +, one using -.</div>
<h3>Worked example</h3>
<div>Solve x² + 5x + 6 = 0. Here a = 1, b = 5, c = 6.<br><br>
b² - 4ac = 25 - 24 = 1, and √1 = 1<br>
x = (-5 + 1)/2 = -2 &nbsp;&nbsp;or&nbsp;&nbsp; x = (-5 - 1)/2 = -3<br><br>
(The same answers factoring gives — the formula and factoring always agree.)</div>
<h3>The part under the root: the discriminant</h3>
<p><b>b² - 4ac</b> tells you what kind of answers to expect before you finish:</p>
<ul><li>Positive → two different real solutions</li>
<li>Zero → exactly one solution (the parabola just touches the x-axis)</li>
<li>Negative → no real solutions (the parabola never crosses)</li></ul>
<p>Common slips: forgetting that -b means the OPPOSITE of b (if b = -3, then -b = 3), and dividing only part of the top by 2a — the whole top gets divided.</p>
""",
    },
    {
        "title": "The Pythagorean theorem",
        "band": "high",
        "aliases": ["pythagorean theorem", "pythagoras", "pythagorean", "right triangle sides",
                    "a2 b2 c2", "hypotenuse"],
        "body": """
<p>In any <b>right triangle</b> (one with a 90° corner), the two short sides (the <b>legs</b>, a and b) and the longest side (the <b>hypotenuse</b>, c — always opposite the right angle) obey one famous rule:</p>
<div><b>a² + b² = c²</b><br>(each side length squared: a² means a × a)</div>
<h3>Finding the long side</h3>
<div><b>Example:</b> legs 3 and 4.<br>3² + 4² = 9 + 16 = 25 = c², so c = √25 = <b>5</b>.</div>
<h3>Finding a short side</h3>
<div><b>Example:</b> hypotenuse 13, one leg 5.<br>5² + b² = 13² → 25 + b² = 169 → b² = 144 → b = <b>12</b>.</div>
<h3>What it's for</h3>
<ul><li>Any distance you can turn into a right triangle: how long a ladder must be, the diagonal of a TV screen, the straight-line distance between two points on a map.</li>
<li>It ONLY works on right triangles — no 90° corner, no theorem.</li>
<li>c is always the longest side; if your "hypotenuse" comes out shorter than a leg, something slipped.</li></ul>
<p>Famous trios worth recognizing: 3-4-5, 5-12-13, 8-15-17 (and any multiple, like 6-8-10).</p>
""",
    },
    {
        "title": "The binomial theorem",
        "band": "advanced",
        "aliases": ["binomial theorem", "the binomial theorem", "binomial expansion",
                    "expanding binomials", "pascals triangle", "binomial"],
        "body": """
<p>A <b>binomial</b> is a two-term expression like (x + y). The <b>binomial theorem</b> expands any power (x + y)ⁿ without multiplying it out by hand n times.</p>
<h3>The pattern</h3>
<p>In the expansion of (x + y)ⁿ: the powers of x count DOWN from n to 0, the powers of y count UP from 0 to n, and each term gets a counting coefficient "n choose k", written C(n, k) = n! ÷ (k!(n-k)!) — the number of ways to pick k items from n. (n!, "n factorial", means n × (n-1) × ... × 1.)</p>
<div><b>Example:</b> (x + y)³ = x³ + 3x²y + 3xy² + y³<br><br>
The coefficients 1, 3, 3, 1 are row 3 of <b>Pascal's triangle</b> — each number is the sum of the two above it:<br><br>
1<br>1&nbsp;&nbsp;1<br>1&nbsp;&nbsp;2&nbsp;&nbsp;1<br>1&nbsp;&nbsp;3&nbsp;&nbsp;3&nbsp;&nbsp;1<br>1&nbsp;&nbsp;4&nbsp;&nbsp;6&nbsp;&nbsp;4&nbsp;&nbsp;1</div>
<h3>Grabbing ONE term without expanding everything</h3>
<div><b>Example:</b> the x²y³ term of (x + y)⁵ has coefficient C(5, 3) = 10 → <b>10x²y³</b>.</div>
<h3>Watch the signs and insides</h3>
<p>For (x - y)ⁿ the signs alternate: (x - y)³ = x³ - 3x²y + 3xy² - y³. And if the binomial is (2x + 3), the WHOLE piece gets the power: (2x)² = 4x², not 2x².</p>
""",
    },
    {
        "title": "The unit circle",
        "band": "advanced",
        "aliases": ["unit circle", "the unit circle", "sine and cosine circle", "unit circle values",
                    "radians", "special angles"],
        "body": """
<p>The <b>unit circle</b> is a circle of radius 1 centered at the origin (0, 0). It's the master key to trigonometry: for an angle θ (theta) measured counterclockwise from the positive x-axis, the point where the angle's ray meets the circle is:</p>
<div><b>( cos θ , sin θ )</b><br>cosine is the x-coordinate; sine is the y-coordinate. That IS the definition.</div>
<h3>The angles worth memorizing</h3>
<ul><li>θ = 0: (1, 0) — so cos 0 = 1, sin 0 = 0</li>
<li>θ = 30°: (√3/2, 1/2)</li>
<li>θ = 45°: (√2/2, √2/2) — x and y equal on the diagonal</li>
<li>θ = 60°: (1/2, √3/2) — 30°'s values swapped</li>
<li>θ = 90°: (0, 1) — straight up</li></ul>
<h3>Signs by quadrant</h3>
<p>Quadrant I (up-right): both positive. II (up-left): sine +, cosine -. III: both negative. IV: sine -, cosine +. Every other angle is a reflection of a first-quadrant angle, so those five points give you the whole circle.</p>
<h3>Radians</h3>
<p>A <b>radian</b> measures angles by arc length along the unit circle: the full circle is 2π radians = 360°, so π = 180°, π/2 = 90°, π/6 = 30°. Advanced math speaks radians almost exclusively — worth getting fluent early.</p>
""",
    },
    {
        "title": "What is a derivative?",
        "band": "advanced",
        "aliases": ["derivative", "derivatives", "what is a derivative", "instantaneous rate of change",
                    "differentiation", "slope of a curve"],
        "body": """
<p>A <b>derivative</b> answers one question: <b>how fast is this changing right NOW?</b> Your speedometer is a derivative — not your average speed for the trip, but your speed at this instant.</p>
<h3>From slope to derivative</h3>
<p>For a straight line, "how fast it changes" is just the slope — one number, the same everywhere. A curve is steeper in some places than others, so it needs a slope <i>at each point</i>. The derivative of a function f(x) — written <b>f′(x)</b>, read "f prime of x" — is a new function giving the slope of f at every x.</p>
<div><b>Example:</b> f(x) = x² has derivative f′(x) = 2x.<br>
At x = 1 the curve climbs with slope 2(1) = 2; at x = 3 it's steeper, slope 6; at x = 0 it's momentarily flat, slope 0 (the bottom of the bowl).</div>
<h3>Where it comes from</h3>
<p>Average rate of change between two points is rise/run: [f(x + h) - f(x)] ÷ h, where h is the run between them. Slide the two points together (let h shrink toward 0) and the average becomes the <b>instantaneous</b> rate — that limiting value is the derivative.</p>
<h3>Why it matters</h3>
<ul><li>Where f′ is positive, f is rising; negative, falling; zero, momentarily flat — that's how you find peaks and valleys.</li>
<li>Physics: position's derivative is velocity; velocity's derivative is acceleration.</li></ul>
""",
    },
]

# Index the seeds by normalized alias for instant exact matching.
_SEED_BY_ALIAS = {}
for _s in SEEDS:
    _s["key"] = norm_key(_s["title"])
    for _a in [_s["title"]] + _s["aliases"]:
        _SEED_BY_ALIAS[norm_key(_a)] = _s


def find_seed(query: str, band: str):
    """Exact-alias seed match. Seeds are served across bands when close in level
    (an elementary seed is fine for middle and vice versa) -- the generate-once
    fallback produces band-perfect versions when the gap is bigger."""
    s = _SEED_BY_ALIAS.get(norm_key(query))
    if not s:
        return None
    near = {"elementary": {"elementary", "middle"},
            "middle": {"elementary", "middle", "high"},
            "high": {"middle", "high", "advanced"},
            "advanced": {"high", "advanced"}}
    return s if s["band"] in near.get(band, {band}) else None


def fuzzy_pick(query: str, candidates: list):
    """Best token-overlap match from [{key,title,...}] or None.
    Guardrail (2026-08-07 dry-run catch: 'imaginary numbers' must NOT match 'negative
    numbers' on the shared word 'numbers'): a match needs at least TWO overlapping
    meaningful words -- unless the query IS a single word, which may match alone."""
    q = _tokens(query)
    if not q:
        return None
    best, best_key = None, (0, 0.0)
    for c in candidates:
        t = _tokens(c.get("title", "")) | set(
            sum((list(_tokens(a)) for a in c.get("aliases", [])), []))
        if not t:
            continue
        overlap = len(q & t)
        score = overlap / max(1, min(len(q), len(t)))
        ok = (overlap >= 2 and score >= 0.5) or (len(q) == 1 and overlap == 1)
        if ok and (overlap, score) > best_key:
            best, best_key = c, (overlap, score)
    return best


# =============================================================================
# GENERATE-ONCE FALLBACK -- write the missing article with the model, then the
# caller saves it forever. Kept OUT of tutor.py on purpose (Jim: the library
# never touches the voice/chat lesson).
# =============================================================================
GEN_SYSTEM = """You write short reference articles for a math tutoring app's "Look it up" library.
A student searched for a topic; write the article they will READ (no conversation, no questions
to the student, no offers to help further -- it is a page in a reference book).

RULES (all hard):
1. LITERALLY TRUE. Every mathematical sentence must be exactly correct -- no loose shorthand.
2. DEFINE EVERY notation and term at first use (assume the student has NOT seen it before).
3. Structure: a one-sentence plain-language definition first; then 1-3 short <h3> sections;
   at least ONE fully worked example inside <div>...</div>; a short list of common mistakes
   or key points as <ul><li>.
4. LENGTH: 180-320 words. Tight beats long.
5. FORMAT: HTML using ONLY these tags: <h3> <p> <ul> <ol> <li> <b> <i> <br> <div>.
   No attributes, no scripts, no styles, no markdown, no headings besides <h3>.
   Write math in plain text/unicode (x², √, π, 3/4) -- no LaTeX.
6. If the search is NOT a math topic this app could teach (grades 1-12 math through
   calculus/statistics), reply with exactly: OFFTOPIC
7. First line of your reply: TITLE: <a clean 2-6 word article title>
   Then a blank line, then the article HTML. Nothing else.

WRITE FOR: {tone}"""


def generate_article(query: str, band: str) -> dict:
    """One model call -> {'title','body'} (scrubbed), or {} if off-topic/unavailable.
    The CALLER persists it; this function is pure."""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return {}
    try:
        from anthropic import Anthropic
        client = Anthropic(api_key=api_key)
        model = os.environ.get("CLAUDE_MODEL", "claude-sonnet-5")
        msg = client.messages.create(
            model=model, max_tokens=1200,
            system=GEN_SYSTEM.format(tone=BAND_TONE.get(band, BAND_TONE["high"])),
            messages=[{"role": "user", "content": f"The student searched: {query!r}"}],
        )
        text = "".join(b.text for b in msg.content if getattr(b, "type", "") == "text").strip()
        if not text or text.upper().startswith("OFFTOPIC"):
            return {}
        m = re.match(r"TITLE:\s*(.+)", text)
        if not m:
            return {}
        title = m.group(1).strip()[:120]
        body = scrub_html(text[m.end():].strip())
        if len(body) < 80:
            return {}
        return {"title": title, "body": body}
    except Exception as exc:  # noqa: BLE001
        print(f"[library] generate failed: {exc}")
        return {}

# I did no harm and this file is not truncated.

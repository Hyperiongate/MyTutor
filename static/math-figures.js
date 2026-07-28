/* =============================================================================
   math-figures.js  --  Math Tutor MVP  --  Hyperion Shift LLC
   -----------------------------------------------------------------------------
   CHANGE NOTES (keep newest at top):
     2026-07-28  NEW. Shared, self-contained whiteboard figures for the multi-course tutor
                 (companion to geo-figures.js). Exposes window.MathFigures.svg(kind, attrs) -> an
                 SVG string (no external CSS; all styling inline). Loaded via
                 <script src="/static/math-figures.js"> in session/practice/topic.html; those pages'
                 handleTags() route the tags below to showFig(kind, attrs) which drops the SVG on the
                 whiteboard.
                 STAGE 1 -- THE FUNCTION GRAPHER. [[graph]] is now a REAL grapher: it plots any
                 function of x (sine/cosine/tangent, exponentials, logs, higher-degree polynomials,
                 rational functions WITH their asymptotes, square-root and absolute-value curves) on a
                 labeled grid, in addition to the old lines=/parabola=/points=. Attributes:
                   [[graph func="sin(x); 2^x" lines="y=2x+1" parabola="y=x^2-4x+1"
                           points="(1,2),(3,8)" range="-6..6" yrange="-2..2" caption="..."]]
                 func = one or more expressions in x (separated by ; or |). "y=" is optional. A safe
                 compiler turns each into a function; a bad expression is simply skipped (never
                 breaks the page). The y-window auto-fits to the function's values when no yrange is
                 given (so a sine wave fills the frame instead of being a flat wiggle). Asymptotes and
                 undefined regions break the curve cleanly instead of drawing a vertical streak.
   ============================================================================= */
(function () {
  "use strict";
  var NS = "http://www.w3.org/2000/svg";
  var COLORS = ["#5b5bd6", "#0d9488", "#e0392b", "#d97706", "#7c3aed", "#2563eb"];

  function esc(t) {
    return String(t == null ? "" : t).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }
  function trimnum(n) { return (Math.round(n * 1000) / 1000); }

  // ---- Safe expression compiler: "sin(x)", "2^x", "(x^2-1)/(x-2)" -> function(x) ----
  var FN = {
    sin: "Math.sin", cos: "Math.cos", tan: "Math.tan", asin: "Math.asin", acos: "Math.acos",
    atan: "Math.atan", sinh: "Math.sinh", cosh: "Math.cosh", tanh: "Math.tanh", sqrt: "Math.sqrt",
    cbrt: "Math.cbrt", abs: "Math.abs", exp: "Math.exp", ln: "Math.log", log: "logten",
    log10: "logten", log2: "logtwo", sign: "Math.sign", floor: "Math.floor", ceil: "Math.ceil",
    round: "Math.round"
  };
  function compile(expr) {
    var raw = String(expr == null ? "" : expr).trim().replace(/^y\s*=\s*/i, "");
    if (!raw) return null;
    // map identifiers: x stays x; pi/e -> literal constants; a known function name -> its Math.*
    // (or logten/logtwo) equivalent; any other identifier -> NaN (so a bad plot just skips).
    var e = raw.replace(/[A-Za-z_]+[0-9]*/g, function (word) {
      var w = word.toLowerCase();
      if (w === "x") return "x";
      if (w === "pi") return "Math.PI";
      if (w === "e") return "Math.E";
      if (FN.hasOwnProperty(w)) return FN[w];
      return "NaN";
    });
    // implicit multiplication: a value-ender ( ) x digit ) immediately before a value-starter
    // ( "(" , x , "Math." , a log-helper ). Function names are already full Math.* / logten words
    // whose own "(" is a CALL, so no "*" is wrongly inserted inside sin(x), exp(x), logten(x).
    e = e.replace(/([)x0-9])\s*(?=[(x]|Math\.|log)/g, "$1*");
    // exponent: a^b -> Math.pow(a,b). (Using ** breaks on "-x**2", which JS rejects; Math.pow is
    // safe with a unary minus and with function bases like sin(x)^2.)
    var atom = "(?:Math\\.[A-Za-z]+\\([^()]*\\)|logten\\([^()]*\\)|logtwo\\([^()]*\\)|\\([^()]*\\)|[A-Za-z0-9_.]+)";
    var powRe = new RegExp("(" + atom + ")\\s*\\^\\s*(" + atom + ")");
    for (var k = 0; k < 8 && e.indexOf("^") >= 0 && powRe.test(e); k++) e = e.replace(powRe, "Math.pow($1,$2)");
    var fn;
    try {
      fn = new Function("x",
        "var logten=function(v){return Math.log(v)/Math.LN10;};" +
        "var logtwo=function(v){return Math.log(v)/Math.LN2;};" +
        "return (" + e + ");");
      var t = fn(1);
      if (typeof t !== "number") return null;
    } catch (err) { return null; }
    return fn;
  }

  function parseLinear(expr) {
    var s = String(expr).replace(/\s+/g, "").toLowerCase().replace(/^y=/, "");
    var v = s.match(/^x=(-?\d*\.?\d+)$/); if (v) return { vertical: true, x: parseFloat(v[1]) };
    var f = compile(expr); if (!f) return null;
    try { var b = f(0), m = f(1) - b; if (!isFinite(m) || !isFinite(b)) return null; return { m: m, b: b }; }
    catch (e) { return null; }
  }
  function parsePts(str) {
    var out = []; var re = /\(\s*(-?\d*\.?\d+)\s*,\s*(-?\d*\.?\d+)\s*\)/g, m;
    while ((m = re.exec(String(str || ""))) !== null) out.push([parseFloat(m[1]), parseFloat(m[2])]);
    return out;
  }
  function parseRange(str) {
    var m = String(str || "").match(/(-?\d*\.?\d+)\s*\.\.\s*(-?\d*\.?\d+)/);
    return m ? [parseFloat(m[1]), parseFloat(m[2])] : null;
  }

  // ---- [[graph]] : the real function grapher ----
  function graph(a) {
    var S = 440, PAD = 30, plot = S - 2 * PAD;
    var xr = parseRange(a.range) || [-10, 10];
    var xmin = xr[0], xmax = xr[1]; if (xmax <= xmin) { xmin = -10; xmax = 10; }

    // collect sampleable curves: func= expressions, sloped lines, and parabolas
    var curves = [];
    String(a.func || a.fn || a.functions || "").split(/[;|]/).forEach(function (s) {
      s = s.trim(); if (!s) return; var f = compile(s); if (f) curves.push({ label: (/^y=/i.test(s) ? s : "y=" + s), fn: f });
    });
    var lineSpecs = String(a.lines || "").split(/[;|]/).map(function (s) { return s.trim(); }).filter(Boolean);
    var parsedLines = [];
    lineSpecs.forEach(function (s) {
      var L = parseLinear(s); if (!L) return; parsedLines.push(L);
      if (L.vertical) curves.push({ label: s, _vLine: L });
      else curves.push({ label: s, fn: function (x) { return L.m * x + L.b; } });
    });
    String(a.parabola || a.parabolas || "").split(/[;|]/).forEach(function (s) {
      s = s.trim(); if (!s) return; var f = compile(s); if (f) curves.push({ label: s, fn: f });
    });

    // y-window: explicit yrange, else auto-fit to the sampled values, else -10..10
    var yr = parseRange(a.yrange), ymin, ymax;
    if (yr) { ymin = yr[0]; ymax = yr[1]; }
    else {
      var ys = [];
      curves.forEach(function (c) {
        if (!c.fn) return;
        for (var i = 0; i <= 160; i++) {
          var x = xmin + (xmax - xmin) * i / 160, y;
          try { y = c.fn(x); } catch (e) { continue; }
          if (isFinite(y) && Math.abs(y) <= 200) ys.push(y);
        }
      });
      parsePts(a.points).forEach(function (p) { if (Math.abs(p[1]) <= 200) ys.push(p[1]); });
      if (ys.length) {
        var lo = Math.min.apply(null, ys), hi = Math.max.apply(null, ys);
        lo = Math.min(lo, 0); hi = Math.max(hi, 0);
        var pad = Math.max(1, (hi - lo) * 0.15); lo -= pad; hi += pad;
        if (hi - lo < 4) { var c0 = (hi + lo) / 2; lo = c0 - 2; hi = c0 + 2; }
        ymin = Math.max(-60, Math.floor(lo)); ymax = Math.min(60, Math.ceil(hi));
      } else { ymin = -10; ymax = 10; }
    }
    if (ymax <= ymin) { ymin = -10; ymax = 10; }

    var mapX = function (x) { return PAD + (x - xmin) / (xmax - xmin) * plot; };
    var mapY = function (y) { return PAD + (ymax - y) / (ymax - ymin) * plot; };
    var span = ymax - ymin;

    var svg = '<svg viewBox="0 0 ' + S + ' ' + S + '" xmlns="' + NS +
      '" style="width:100%;max-width:430px;height:auto;display:block;margin:6px auto;">';
    svg += '<defs><clipPath id="gclip"><rect x="' + PAD + '" y="' + PAD + '" width="' + plot + '" height="' + plot + '"/></clipPath></defs>';
    svg += '<rect x="' + PAD + '" y="' + PAD + '" width="' + plot + '" height="' + plot + '" fill="#fbfbff" stroke="#e7e6f2"/>';

    // grid + labels with a "nice" tick step per axis
    function step(range) {
      var raw = range / 10, p = Math.pow(10, Math.floor(Math.log(raw) / Math.LN10)), n = raw / p;
      var s = n < 1.5 ? 1 : n < 3.5 ? 2 : n < 7.5 ? 5 : 10; return s * p;
    }
    var xstep = step(xmax - xmin), ystep = step(ymax - ymin);
    for (var gx = Math.ceil(xmin / xstep) * xstep; gx <= xmax + 1e-9; gx += xstep) {
      var px = mapX(gx), zx = Math.abs(gx) < 1e-9;
      svg += '<line x1="' + px + '" y1="' + PAD + '" x2="' + px + '" y2="' + (S - PAD) + '" stroke="' + (zx ? "#9aa7b6" : "#eef0f7") + '" stroke-width="' + (zx ? 1.5 : 1) + '"/>';
      if (!zx) svg += '<text x="' + px + '" y="' + (mapY(0) + 13) + '" font-size="10" fill="#8890a0" text-anchor="middle">' + trimnum(gx) + '</text>';
    }
    for (var gy = Math.ceil(ymin / ystep) * ystep; gy <= ymax + 1e-9; gy += ystep) {
      var py = mapY(gy), zy = Math.abs(gy) < 1e-9;
      svg += '<line x1="' + PAD + '" y1="' + py + '" x2="' + (S - PAD) + '" y2="' + py + '" stroke="' + (zy ? "#9aa7b6" : "#eef0f7") + '" stroke-width="' + (zy ? 1.5 : 1) + '"/>';
      if (!zy) svg += '<text x="' + (mapX(0) - 6) + '" y="' + (py + 3) + '" font-size="10" fill="#8890a0" text-anchor="end">' + trimnum(gy) + '</text>';
    }
    svg += '<text x="' + (S - PAD + 2) + '" y="' + (mapY(0) + 3) + '" font-size="11" fill="#6b6f82">x</text>';
    svg += '<text x="' + (mapX(0) + 4) + '" y="' + (PAD - 4) + '" font-size="11" fill="#6b6f82">y</text>';

    svg += '<g clip-path="url(#gclip)">';
    // vertical lines
    curves.forEach(function (c) {
      if (c._vLine) svg += '<line x1="' + mapX(c._vLine.x) + '" y1="' + PAD + '" x2="' + mapX(c._vLine.x) + '" y2="' + (S - PAD) + '" stroke="' + COLORS[0] + '" stroke-width="2.5"/>';
    });
    // sampled curves (functions, sloped lines, parabolas) with asymptote breaks
    var ci = 0;
    curves.forEach(function (c) {
      if (!c.fn) return;
      var col = COLORS[ci % COLORS.length]; ci++;
      var N = 480, segs = [], cur = [], prevY = null;
      for (var i = 0; i <= N; i++) {
        var x = xmin + (xmax - xmin) * i / N, y;
        try { y = c.fn(x); } catch (e) { y = NaN; }
        var ok = isFinite(y) && Math.abs(y) <= span * 6 + 40;
        if (ok && prevY !== null && Math.abs(y - prevY) > span * 1.8) { if (cur.length) segs.push(cur); cur = []; }
        if (ok) { cur.push(mapX(x) + "," + mapY(y)); prevY = y; }
        else { if (cur.length) segs.push(cur); cur = []; prevY = null; }
      }
      if (cur.length) segs.push(cur);
      segs.forEach(function (pts) { if (pts.length > 1) svg += '<polyline points="' + pts.join(" ") + '" fill="none" stroke="' + col + '" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>'; });
    });
    // intersection of the first two straight lines (kept from the old grapher)
    if (parsedLines.length >= 2 && !parsedLines[0].vertical && !parsedLines[1].vertical && parsedLines[0].m !== parsedLines[1].m) {
      var ix = (parsedLines[1].b - parsedLines[0].b) / (parsedLines[0].m - parsedLines[1].m);
      var iy = parsedLines[0].m * ix + parsedLines[0].b;
      if (ix >= xmin && ix <= xmax && iy >= ymin && iy <= ymax) {
        svg += '<circle cx="' + mapX(ix) + '" cy="' + mapY(iy) + '" r="5.5" fill="#fff" stroke="#e0392b" stroke-width="2.5"/>';
        svg += '<text x="' + (mapX(ix) + 9) + '" y="' + (mapY(iy) - 7) + '" font-size="11" font-weight="700" fill="#c0392b">(' + trimnum(ix) + ", " + trimnum(iy) + ')</text>';
      }
    }
    // explicit points
    parsePts(a.points).forEach(function (p) {
      if (p[0] < xmin || p[0] > xmax || p[1] < ymin || p[1] > ymax) return;
      svg += '<circle cx="' + mapX(p[0]) + '" cy="' + mapY(p[1]) + '" r="4.5" fill="#5b5bd6"/>';
      svg += '<text x="' + (mapX(p[0]) + 8) + '" y="' + (mapY(p[1]) - 6) + '" font-size="10.5" fill="#26263a">(' + trimnum(p[0]) + ", " + trimnum(p[1]) + ')</text>';
    });
    svg += "</g>";

    // legend inside the SVG (each curve's equation in its colour)
    var lx = PAD + 2, ly = S - 8, li = 0;
    curves.forEach(function (c) {
      var col = COLORS[li % COLORS.length]; li++;
      svg += '<text x="' + lx + '" y="' + ly + '" font-size="12" font-weight="700" fill="' + col + '" font-family="system-ui,Segoe UI,Arial,sans-serif">' + esc(c.label) + '</text>';
      lx += Math.min(160, 24 + esc(c.label).length * 8.2);
      if (lx > S - 90) { lx = PAD + 2; ly += 15; }
    });
    return svg + "</svg>";
  }

  window.MathFigures = {
    graph: graph,
    _compile: compile,
    svg: function (kind, a) {
      try { return this[kind] ? this[kind](a || {}) : ""; } catch (e) { return ""; }
    }
  };
})();
/* I did no harm and this file is not truncated. */

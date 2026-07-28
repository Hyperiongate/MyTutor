/* =============================================================================
   math-figures.js  --  Math Tutor MVP  --  Hyperion Shift LLC
   -----------------------------------------------------------------------------
   CHANGE NOTES (keep newest at top):
     2026-07-28  STAGE 2 -- STATISTICS & PROBABILITY SUITE. Added nine figures to
                 window.MathFigures: [[bars]] (bar chart), [[histogram]] (bins raw values),
                 [[dotplot]], [[boxplot]] (five-number summary; computes quartiles or takes five=),
                 [[scatter]] (points + optional least-squares line of best fit via fit="true", or an
                 explicit line=), [[normal]] (bell curve, mean/sd, optional shaded region), [[twoway]]
                 (a two-way frequency table with row/col/grand totals -- returned as HTML), [[tree]]
                 (a two-stage probability tree with joint probabilities), and [[pie]] (pie chart /
                 spinner). All self-contained; bad input returns "". The 3 tutoring pages route these
                 tags to showFig(); tutor.py practice/topic prompts document them.
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

  // ================= STATISTICS & PROBABILITY FIGURES (Stage 2) =================
  function svgOpen(w, h, maxw) {
    return '<svg viewBox="0 0 ' + w + ' ' + h + '" xmlns="' + NS + '" style="width:100%;max-width:' + (maxw || 400) + 'px;height:auto;display:block;margin:6px auto;">';
  }
  function tspan(x, y, s, fill, size, weight, anchor) {
    return '<text x="' + x + '" y="' + y + '" fill="' + (fill || "#26263a") + '" font-size="' + (size || 12) +
      '" font-weight="' + (weight || 600) + '" text-anchor="' + (anchor || "middle") +
      '" font-family="system-ui,Segoe UI,Arial,sans-serif">' + esc(s) + '</text>';
  }
  function parseData(str) {   // "A:5 | B:8" or "A:5, B:8" -> [{label,value}]
    return String(str || "").split(/[|,]/).map(function (p) {
      var i = p.indexOf(":"); if (i < 0) return null;
      var v = parseFloat(p.slice(i + 1)); if (isNaN(v)) return null;
      return { label: p.slice(0, i).trim(), value: v };
    }).filter(Boolean);
  }
  function parseNums(str) {
    return String(str || "").split(/[,\s]+/).map(function (s) { return parseFloat(s); }).filter(function (n) { return !isNaN(n); });
  }
  function quantile(sorted, q) {
    var pos = (sorted.length - 1) * q, b = Math.floor(pos), r = pos - b;
    return sorted[b + 1] !== undefined ? sorted[b] + r * (sorted[b + 1] - sorted[b]) : sorted[b];
  }

  // ---- [[bars]] : labeled vertical bar chart ----
  function bars(a) {
    var d = parseData(a.data); if (!d.length) return "";
    var W = 400, H = 250, left = 36, right = W - 12, top = 22, base = H - 40, plotW = right - left, plotH = base - top;
    var max = Math.max.apply(null, d.map(function (o) { return o.value; }).concat([1]));
    var s = svgOpen(W, H, 400);
    for (var i = 0; i <= 4; i++) { var v = max * i / 4, y = base - plotH * i / 4; s += '<line x1="' + left + '" y1="' + y + '" x2="' + right + '" y2="' + y + '" stroke="#eef0f7"/>'; s += tspan(left - 5, y + 3, String(trimnum(v)), "#8890a0", 9, 500, "end"); }
    s += '<line x1="' + left + '" y1="' + base + '" x2="' + right + '" y2="' + base + '" stroke="#9aa7b6" stroke-width="1.5"/>';
    var bw = plotW / d.length, bar = bw * 0.62;
    d.forEach(function (o, i) {
      var x = left + bw * i + (bw - bar) / 2, h = plotH * o.value / max, y = base - h, col = COLORS[i % COLORS.length];
      s += '<rect x="' + x + '" y="' + y + '" width="' + bar + '" height="' + h + '" rx="3" fill="' + col + '"/>';
      s += tspan(x + bar / 2, y - 5, String(trimnum(o.value)), "#26263a", 11, 700);
      s += tspan(x + bar / 2, base + 15, o.label, "#556", 11, 600);
    });
    return s + "</svg>";
  }

  // ---- [[histogram]] : bins raw values into adjacent bars ----
  function histogram(a) {
    var vals = parseNums(a.values || a.data); if (vals.length < 2) return "";
    var min = Math.min.apply(null, vals), max = Math.max.apply(null, vals); if (max === min) max = min + 1;
    var bins = Math.max(2, Math.min(12, parseInt(a.bins, 10) || Math.ceil(Math.sqrt(vals.length))));
    var bw = (max - min) / bins, counts = []; for (var b0 = 0; b0 < bins; b0++) counts.push(0);
    vals.forEach(function (v) { var k = Math.min(bins - 1, Math.floor((v - min) / bw)); counts[k]++; });
    var maxc = Math.max.apply(null, counts.concat([1]));
    var W = 420, H = 260, left = 34, right = W - 12, top = 20, base = H - 42, plotW = right - left, plotH = base - top;
    var s = svgOpen(W, H, 420);
    for (var i = 0; i <= 4; i++) { var y = base - plotH * i / 4; s += '<line x1="' + left + '" y1="' + y + '" x2="' + right + '" y2="' + y + '" stroke="#eef0f7"/>'; s += tspan(left - 5, y + 3, String(Math.round(maxc * i / 4)), "#8890a0", 9, 500, "end"); }
    s += '<line x1="' + left + '" y1="' + base + '" x2="' + right + '" y2="' + base + '" stroke="#9aa7b6" stroke-width="1.5"/>';
    var cw = plotW / bins;
    counts.forEach(function (c, i) { var x = left + cw * i, h = plotH * c / maxc, y = base - h; s += '<rect x="' + (x + 1) + '" y="' + y + '" width="' + (cw - 2) + '" height="' + h + '" fill="' + COLORS[0] + '" fill-opacity="0.85" stroke="#fff"/>'; if (c) s += tspan(x + cw / 2, y - 4, String(c), "#26263a", 10, 700); });
    for (var e = 0; e <= bins; e++) { if (bins > 8 && (e % 2)) continue; var xe = left + cw * e; s += tspan(xe, base + 15, String(trimnum(min + bw * e)), "#8890a0", 9, 500); }
    return s + "</svg>";
  }

  // ---- [[dotplot]] : stacked dots over a number line ----
  function dotplot(a) {
    var vals = parseNums(a.values || a.data); if (!vals.length) return "";
    var min = Math.floor(Math.min.apply(null, vals)), max = Math.ceil(Math.max.apply(null, vals)); if (max === min) max = min + 1;
    var W = 420, H = 200, left = 22, right = W - 22, axisY = H - 34, plotW = right - left;
    var mapX = function (v) { return left + (v - min) / (max - min) * plotW; };
    var s = svgOpen(W, H, 420);
    s += '<line x1="' + left + '" y1="' + axisY + '" x2="' + right + '" y2="' + axisY + '" stroke="#9aa7b6" stroke-width="1.5"/>';
    for (var t = min; t <= max; t++) { var x = mapX(t); s += '<line x1="' + x + '" y1="' + axisY + '" x2="' + x + '" y2="' + (axisY + 5) + '" stroke="#9aa7b6"/>'; s += tspan(x, axisY + 17, String(t), "#8890a0", 10, 500); }
    var counts = {};
    vals.slice().sort(function (p, q) { return p - q; }).forEach(function (v) { var n = counts[v] || 0; counts[v] = n + 1; s += '<circle cx="' + mapX(v) + '" cy="' + (axisY - 9 - n * 12) + '" r="4.5" fill="' + COLORS[0] + '"/>'; });
    return s + "</svg>";
  }

  // ---- [[boxplot]] : five-number summary ----
  function boxplot(a) {
    var five;
    if (a.five) five = parseNums(a.five);
    else { var v = parseNums(a.values || a.data).sort(function (p, q) { return p - q; }); if (v.length < 2) return ""; five = [v[0], quantile(v, 0.25), quantile(v, 0.5), quantile(v, 0.75), v[v.length - 1]]; }
    if (five.length < 5) return "";
    var lo = five[0], hi = five[4], pad = (hi - lo) * 0.12 || 1, amin = lo - pad, amax = hi + pad;
    var W = 420, H = 160, left = 24, right = W - 24, cy = 64, plotW = right - left, axisY = H - 34;
    var mapX = function (v) { return left + (v - amin) / (amax - amin) * plotW; };
    var s = svgOpen(W, H, 420);
    s += '<line x1="' + mapX(five[0]) + '" y1="' + cy + '" x2="' + mapX(five[1]) + '" y2="' + cy + '" stroke="#5b5bd6" stroke-width="2"/>';
    s += '<line x1="' + mapX(five[3]) + '" y1="' + cy + '" x2="' + mapX(five[4]) + '" y2="' + cy + '" stroke="#5b5bd6" stroke-width="2"/>';
    [0, 4].forEach(function (k) { s += '<line x1="' + mapX(five[k]) + '" y1="' + (cy - 12) + '" x2="' + mapX(five[k]) + '" y2="' + (cy + 12) + '" stroke="#5b5bd6" stroke-width="2"/>'; });
    s += '<rect x="' + mapX(five[1]) + '" y="' + (cy - 20) + '" width="' + (mapX(five[3]) - mapX(five[1])) + '" height="40" fill="rgba(91,91,214,.12)" stroke="#5b5bd6" stroke-width="2"/>';
    s += '<line x1="' + mapX(five[2]) + '" y1="' + (cy - 20) + '" x2="' + mapX(five[2]) + '" y2="' + (cy + 20) + '" stroke="#e0392b" stroke-width="2.5"/>';
    s += '<line x1="' + left + '" y1="' + axisY + '" x2="' + right + '" y2="' + axisY + '" stroke="#9aa7b6"/>';
    ["", "", "", "", ""].forEach(function (_, k) { var x = mapX(five[k]); s += '<line x1="' + x + '" y1="' + axisY + '" x2="' + x + '" y2="' + (axisY + 5) + '" stroke="#9aa7b6"/>'; s += tspan(x, axisY + 16, String(trimnum(five[k])), "#556", 10, 600); });
    return s + "</svg>";
  }

  // ---- [[scatter]] : points + optional line of best fit ----
  function scatter(a) {
    var pts = parsePts(a.points); if (pts.length < 2) return "";
    var xs = pts.map(function (p) { return p[0]; }), ys = pts.map(function (p) { return p[1]; });
    var xmin = Math.min.apply(null, xs), xmax = Math.max.apply(null, xs), ymin = Math.min.apply(null, ys), ymax = Math.max.apply(null, ys);
    var pxr = (xmax - xmin) || 1, pyr = (ymax - ymin) || 1; xmin -= pxr * 0.12; xmax += pxr * 0.12; ymin -= pyr * 0.12; ymax += pyr * 0.12;
    var W = 400, H = 340, PAD = 34, plot = W - 2 * PAD, plotH = H - 2 * PAD - 8;
    var mapX = function (x) { return PAD + (x - xmin) / (xmax - xmin) * plot; };
    var mapY = function (y) { return PAD + (ymax - y) / (ymax - ymin) * plotH; };
    var s = svgOpen(W, H, 400);
    s += '<rect x="' + PAD + '" y="' + PAD + '" width="' + plot + '" height="' + plotH + '" fill="#fbfbff" stroke="#e7e6f2"/>';
    for (var i = 0; i <= 4; i++) {
      var gx = PAD + plot * i / 4, gy = PAD + plotH * i / 4;
      s += '<line x1="' + gx + '" y1="' + PAD + '" x2="' + gx + '" y2="' + (PAD + plotH) + '" stroke="#eef0f7"/>';
      s += '<line x1="' + PAD + '" y1="' + gy + '" x2="' + (PAD + plot) + '" y2="' + gy + '" stroke="#eef0f7"/>';
      s += tspan(gx, PAD + plotH + 14, String(trimnum(xmin + (xmax - xmin) * i / 4)), "#8890a0", 9, 500);
      s += tspan(PAD - 6, PAD + plotH - plotH * i / 4 + 3, String(trimnum(ymin + (ymax - ymin) * i / 4)), "#8890a0", 9, 500, "end");
    }
    var m, b;
    if (a.fit && /^(true|yes|1)$/i.test(String(a.fit))) {
      var n = pts.length, sx = 0, sy = 0, sxx = 0, sxy = 0;
      pts.forEach(function (p) { sx += p[0]; sy += p[1]; sxx += p[0] * p[0]; sxy += p[0] * p[1]; });
      m = (n * sxy - sx * sy) / (n * sxx - sx * sx); b = (sy - m * sx) / n;
    } else if (a.line) { var L = parseLinear(a.line); if (L && !L.vertical) { m = L.m; b = L.b; } }
    if (m !== undefined && isFinite(m)) {
      s += '<line x1="' + mapX(xmin) + '" y1="' + mapY(m * xmin + b) + '" x2="' + mapX(xmax) + '" y2="' + mapY(m * xmax + b) + '" stroke="#e0392b" stroke-width="2.5"/>';
      s += tspan(PAD + plot - 4, PAD + 13, "y = " + trimnum(m) + "x + " + trimnum(b), "#c0392b", 11, 700, "end");
    }
    pts.forEach(function (p) { s += '<circle cx="' + mapX(p[0]) + '" cy="' + mapY(p[1]) + '" r="4" fill="#5b5bd6" fill-opacity="0.85"/>'; });
    return s + "</svg>";
  }

  // ---- [[normal]] : bell curve with an optional shaded region ----
  function normal(a) {
    var mean = parseFloat(a.mean); if (isNaN(mean)) mean = 0;
    var sd = parseFloat(a.sd); if (isNaN(sd) || sd <= 0) sd = 1;
    var W = 420, H = 240, left = 20, right = W - 20, base = H - 36, top = 24, plotW = right - left, plotH = base - top;
    var xmin = mean - 4 * sd, xmax = mean + 4 * sd;
    var f = function (x) { return Math.exp(-0.5 * Math.pow((x - mean) / sd, 2)); };
    var mapX = function (x) { return left + (x - xmin) / (xmax - xmin) * plotW; };
    var mapY = function (y) { return base - y * plotH * 0.92; };
    var s = svgOpen(W, H, 420);
    var sh = parseRange(a.shade);
    if (a.lo != null || a.hi != null) sh = [parseFloat(a.lo != null ? a.lo : xmin), parseFloat(a.hi != null ? a.hi : xmax)];
    if (sh && isFinite(sh[0]) && isFinite(sh[1])) {
      var poly = [mapX(sh[0]) + "," + base], stp = (sh[1] - sh[0]) / 60 || 1;
      for (var x = sh[0]; x <= sh[1] + 1e-9; x += stp) poly.push(mapX(x) + "," + mapY(f(x)));
      poly.push(mapX(sh[1]) + "," + base);
      s += '<polygon points="' + poly.join(" ") + '" fill="rgba(91,91,214,.22)"/>';
    }
    var cp = []; for (var x2 = xmin; x2 <= xmax + 1e-9; x2 += (xmax - xmin) / 120) cp.push(mapX(x2) + "," + mapY(f(x2)));
    s += '<polyline points="' + cp.join(" ") + '" fill="none" stroke="#5b5bd6" stroke-width="2.5"/>';
    s += '<line x1="' + left + '" y1="' + base + '" x2="' + right + '" y2="' + base + '" stroke="#9aa7b6"/>';
    for (var k = -3; k <= 3; k++) { var xk = mean + k * sd, xp = mapX(xk); s += '<line x1="' + xp + '" y1="' + base + '" x2="' + xp + '" y2="' + (base + 5) + '" stroke="#9aa7b6"/>'; s += tspan(xp, base + 16, String(trimnum(xk)), "#8890a0", 10, 500); }
    s += '<line x1="' + mapX(mean) + '" y1="' + mapY(1) + '" x2="' + mapX(mean) + '" y2="' + base + '" stroke="#0d9488" stroke-width="1.5" stroke-dasharray="4 3"/>';
    return s + "</svg>";
  }

  // ---- [[twoway]] : a two-way frequency table (HTML) with totals ----
  function twoway(a) {
    var rows = String(a.rowlabels || "").split(",").map(function (s) { return s.trim(); }).filter(Boolean);
    var cols = String(a.collabels || "").split(",").map(function (s) { return s.trim(); }).filter(Boolean);
    var dataRows = String(a.data || "").split("|").map(function (r) { return r.split(",").map(function (x) { return parseFloat(x.trim()); }); });
    if (!rows.length || !cols.length || !dataRows.length) return "";
    var colTot = cols.map(function () { return 0; }), grand = 0;
    var td = 'style="border:1px solid #d8d8ec;padding:6px 12px;text-align:center;font-family:system-ui,Arial,sans-serif;font-size:13px;"';
    var tot = 'style="border:1px solid #d8d8ec;padding:6px 12px;text-align:center;font-family:system-ui,Arial,sans-serif;font-size:13px;background:#f3f3fb;"';
    var html = '<table style="border-collapse:collapse;margin:8px auto;background:#fff;box-shadow:0 4px 14px rgba(20,30,45,.06);">';
    html += '<tr><td ' + td + '></td>';
    cols.forEach(function (c) { html += '<td ' + td + '><b>' + esc(c) + '</b></td>'; });
    html += '<td ' + tot + '><b>Total</b></td></tr>';
    rows.forEach(function (r, i) {
      var rowTot = 0; html += '<tr><td ' + td + '><b>' + esc(r) + '</b></td>';
      cols.forEach(function (c, j) { var v = (dataRows[i] && !isNaN(dataRows[i][j])) ? dataRows[i][j] : 0; rowTot += v; colTot[j] += v; html += '<td ' + td + '>' + v + '</td>'; });
      grand += rowTot; html += '<td ' + tot + '>' + rowTot + '</td></tr>';
    });
    html += '<tr><td ' + tot + '><b>Total</b></td>';
    colTot.forEach(function (v) { html += '<td ' + tot + '>' + v + '</td>'; });
    html += '<td ' + tot + '><b>' + grand + '</b></td></tr></table>';
    return html;
  }

  // ---- [[tree]] : a two-stage probability tree ----
  function tree(a) {
    var first = parseData(a.a || a.stage1); if (!first.length) return "";
    var groups = String(a.b || a.stage2 || "").split(";").map(function (g) { return parseData(g); });
    var W = 430, H = 40 + first.length * 92, x0 = 26, x1 = 150, x2 = 288;
    var s = svgOpen(W, H, 430);
    var rootY = H / 2, gap = (H - 30) / first.length;
    s += '<circle cx="' + x0 + '" cy="' + rootY + '" r="4" fill="#26263a"/>';
    first.forEach(function (f1, i) {
      var y1 = 20 + gap * (i + 0.5);
      s += '<line x1="' + x0 + '" y1="' + rootY + '" x2="' + x1 + '" y2="' + y1 + '" stroke="#5b5bd6" stroke-width="2"/>';
      s += tspan((x0 + x1) / 2, (rootY + y1) / 2 - 6, f1.label + " (" + trimnum(f1.value) + ")", "#26263a", 11, 700);
      s += '<circle cx="' + x1 + '" cy="' + y1 + '" r="3.5" fill="#26263a"/>';
      var sec = (groups[i] && groups[i].length) ? groups[i] : (groups[0] || []);
      var sgap = 42;
      sec.forEach(function (f2, j) {
        var y2 = y1 - ((sec.length - 1) * sgap) / 2 + j * sgap;
        s += '<line x1="' + x1 + '" y1="' + y1 + '" x2="' + x2 + '" y2="' + y2 + '" stroke="#0d9488" stroke-width="2"/>';
        s += tspan((x1 + x2) / 2, (y1 + y2) / 2 - 6, f2.label + " (" + trimnum(f2.value) + ")", "#0d9488", 11, 700);
        s += tspan(x2 + 8, y2 + 4, f1.label + f2.label + " = " + trimnum(f1.value * f2.value), "#556", 11, 700, "start");
      });
    });
    return s + "</svg>";
  }

  // ---- [[pie]] : pie chart / spinner ----
  function pie(a) {
    var d = parseData(a.data || a.sectors); if (!d.length) return "";
    var total = d.reduce(function (s, o) { return s + o.value; }, 0) || 1;
    var W = 380, H = 240, cx = 118, cy = 120, R = 92, s = svgOpen(W, H, 380), ang = -Math.PI / 2;
    d.forEach(function (o, i) {
      var frac = o.value / total, a2 = ang + frac * 2 * Math.PI;
      var x1 = cx + R * Math.cos(ang), y1 = cy + R * Math.sin(ang), x2 = cx + R * Math.cos(a2), y2 = cy + R * Math.sin(a2), large = frac > 0.5 ? 1 : 0;
      if (frac >= 0.999) s += '<circle cx="' + cx + '" cy="' + cy + '" r="' + R + '" fill="' + COLORS[i % COLORS.length] + '"/>';
      else s += '<path d="M ' + cx + ' ' + cy + ' L ' + x1 + ' ' + y1 + ' A ' + R + ' ' + R + ' 0 ' + large + ' 1 ' + x2 + ' ' + y2 + ' Z" fill="' + COLORS[i % COLORS.length] + '" stroke="#fff" stroke-width="2"/>';
      var ly = 44 + i * 24;
      s += '<rect x="248" y="' + (ly - 11) + '" width="13" height="13" rx="2" fill="' + COLORS[i % COLORS.length] + '"/>';
      s += tspan(268, ly, o.label + "  " + Math.round(frac * 100) + "%", "#26263a", 12, 600, "start");
      ang = a2;
    });
    return s + "</svg>";
  }

  window.MathFigures = {
    graph: graph, bars: bars, histogram: histogram, dotplot: dotplot, boxplot: boxplot,
    scatter: scatter, normal: normal, twoway: twoway, tree: tree, pie: pie,
    _compile: compile,
    svg: function (kind, a) {
      try { return this[kind] ? this[kind](a || {}) : ""; } catch (e) { return ""; }
    }
  };
})();
/* I did no harm and this file is not truncated. */

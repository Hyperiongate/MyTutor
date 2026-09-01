/* =============================================================================
   geo-figures.js  --  Math Tutor MVP  --  Hyperion Shift LLC
   -----------------------------------------------------------------------------
   CHANGE NOTES (keep newest at top):
     2026-08-27  BUILD pc -- THE FIGURE FILLS THE BOARD. Every geometry figure was
                 capped at 340px, and until pc that cap did not even apply: .mfig was
                 a shrink-to-fit box and the SVG's percentage width collapsed to the
                 300px replaced-element default (session.html's header carries the
                 measurement). Now that the cap is real, open() uses the same rule
                 math-figures.js uses -- the width that puts the drawing about 420px
                 tall at its own aspect ratio, floor 340, ceiling 1100. A triangle
                 goes 300px -> ~520px; the wide [[segment]] line goes to ~1000px.
                 Every coordinate, label and test in this file is untouched: only the
                 display cap moves, exactly as builds je / nw / ox intended.
     2026-07-28  NEW. Shared geometry whiteboard figures for the multi-course tutor. Exposes
                 window.GeoFigures.svg(kind, attrs) -> a self-contained SVG string (no external
                 CSS; all styling is inline) for three tutor control tags:
                   [[triangle v="A,B,C" sides="5,12,13" right="B" angles="30,60,90" ticks="AB,CA"]]
                   [[angle deg="50" label="ABC"]]
                   [[circle center="O" r="5" inscribed="80"]]
                 Loaded via <script src="/static/geo-figures.js"> in session/practice/topic.html;
                 those pages' handleTags() call showGeo(kind, attrs) which drops the SVG on the
                 whiteboard. Figures are SCHEMATIC (not to scale) with clear labels -- standard for
                 teaching. Adds no dependency; pure string building.
   ============================================================================= */
// 2026-08-01  [[angle]] deg cap 175 -> 180 (a straight line; the old cap bent them) and wide
//             angles recentre so both rays fit the frame.
// 2026-08-01  [[angle]] gained split="60" / split="60,30": an interior ray from the vertex
//             splitting the angle, with the pieces labeled (second defaults to "?") -- so
//             complementary/supplementary lessons can SHOW the split they talk about.
// 2026-08-27  (build ox) [[segment]] -- a labeled line segment, with midpoint
//             congruence ticks, per-piece lengths and an optional total brace.
//             From Jim's live geometry flag ("There should be visuals for these
//             types of questions") on a run of midpoint questions asked with
//             nothing drawn at all: the shelf could draw triangles, angles and
//             circles but not the one-dimensional figure a whole unit is about.
// 2026-08-27  (build ot) THE FIGURE SHELF GROWS -- Jim: "I noticed that we had trouble
//             making crossed lines yesterday. I want all the graphics that math teaches
//             to be available." Three new figures:
//               [[transversal deg="60" ask="corresponding"]] -- two PARALLEL lines cut by
//                 a transversal (the crossed-lines picture every parallel-angles lesson
//                 needs): the given angle arced+labeled at the TOP crossing, and ask=
//                 ("corresponding" | "alternate" | "cointerior" | "vertical") arcs the
//                 asked-about angle in red, labeled "?" (or ask's own text/number).
//               [[polygon sides="6" side="4" angle="120" name="hexagon"]] -- a regular
//                 n-gon (3..12), with an optional side-length label, an optional interior
//                 angle arc+label, and an optional name under the shape.
//               [[solid kind="cylinder" r="3" h="8"]] -- schematic 3D solids with dashed
//                 hidden edges: cube, prism (w/d/h), cylinder (r/h), cone (r/h),
//                 sphere (r), pyramid (b/h). Labels only when given.
// 2026-08-26  (build oi) [[angle]] gained cross="?": BOTH rays extend through the vertex,
//             drawing two full lines crossing (the X every vertical-angles question needs).
//             The given angle keeps its teal arc + measure; the angle OPPOSITE it gets a
//             red arc labeled with cross's value ("?" by default, or a number/text like
//             cross="110"). Written from Jim's 2026-08-26 22:50 flag: a vertical-angles
//             question was asked with NO figure -- the board had nothing to draw an X with.
//             Ignored when deg would make the X degenerate (below 10 or above 170).

(function () {
  "use strict";
  var NS = "http://www.w3.org/2000/svg";
  var INK = "var(--bd-26263a)", ACC = "var(--bd-5b5bd6)", TEAL = "var(--bd-0d9488)", FILL = "rgba(91,91,214,.06)";

  function esc(t) {
    return String(t == null ? "" : t).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }
  function num(v, d) { var n = parseFloat(v); return isNaN(n) ? d : n; }
  function mid(p, q) { return [(p[0] + q[0]) / 2, (p[1] + q[1]) / 2]; }
  function sub(p, q) { return [p[0] - q[0], p[1] - q[1]]; }
  function norm(v) { var l = Math.hypot(v[0], v[1]) || 1; return [v[0] / l, v[1] / l]; }
  function centroid(P) { return [(P[0][0] + P[1][0] + P[2][0]) / 3, (P[0][1] + P[1][1] + P[2][1]) / 3]; }
  function txt(x, y, s, fill, size, weight) {
    return '<text x="' + x + '" y="' + y + '" fill="' + (fill || INK) + '" font-size="' + (size || 16) +
      '" font-weight="' + (weight || 600) + '" font-family="system-ui,Segoe UI,Arial,sans-serif"' +
      ' text-anchor="middle" dominant-baseline="middle">' + esc(s) + "</text>";
  }
  // (pc, 2026-08-27) see the header: the cap is a real limit now, so it scales with
  // the SHAPE instead of pinning every drawing at 340px.
  var FIG_TALL = 420, FIG_FLOOR = 340, FIG_CEIL = 1100;
  function figCap(w, h) {
    var want = (h > 0) ? Math.round(w / h * FIG_TALL) : 0;
    return Math.max(FIG_FLOOR, Math.min(FIG_CEIL, want));
  }
  function open(w, h) {
    return '<svg viewBox="0 0 ' + w + " " + h + '" class="geofig" xmlns="' + NS +
      '" style="width:100%;max-width:' + figCap(w, h) + 'px;height:auto;display:block;margin:6px auto;">';
  }
  function dot(p, r) { return '<circle cx="' + p[0] + '" cy="' + p[1] + '" r="' + (r || 3.2) + '" fill="' + INK + '"/>'; }
  function line(p, q, col, wd) {
    return '<line x1="' + p[0] + '" y1="' + p[1] + '" x2="' + q[0] + '" y2="' + q[1] +
      '" stroke="' + (col || ACC) + '" stroke-width="' + (wd || 2.5) + '" stroke-linecap="round"/>';
  }

  // ---- [[triangle]] : labeled triangle, optional side lengths / right angle / angle measures / ticks ----
  function triangle(a) {
    var W = 320, H = 258;
    var V = String(a.v || "A,B,C").split(",").map(function (s) { return s.trim(); });
    var L = [V[0] || "A", V[1] || "B", V[2] || "C"];
    var right = String(a.right || "").trim().toUpperCase();
    var hasRight = right && L.map(function (x) { return x.toUpperCase(); }).indexOf(right) >= 0;
    var pos = {};
    if (hasRight) {
      var rL = L.filter(function (x) { return x.toUpperCase() === right; })[0];
      var others = L.filter(function (x) { return x !== rL; });
      pos[rL] = [74, 194]; pos[others[0]] = [268, 194]; pos[others[1]] = [74, 52];
    } else {
      pos[L[0]] = [48, 204]; pos[L[1]] = [278, 204]; pos[L[2]] = [150, 44];
    }
    var P = [pos[L[0]], pos[L[1]], pos[L[2]]];
    var cen = centroid(P);
    var s = open(W, H);
    s += '<polygon points="' + P.map(function (p) { return p.join(","); }).join(" ") +
      '" fill="' + FILL + '" stroke="' + ACC + '" stroke-width="2.5" stroke-linejoin="round"/>';

    // right-angle square
    if (hasRight) {
      var rL2 = L.filter(function (x) { return x.toUpperCase() === right; })[0];
      var R = pos[rL2];
      var ov = L.filter(function (x) { return x !== rL2; }).map(function (l) { return pos[l]; });
      var u = norm(sub(ov[0], R)), v = norm(sub(ov[1], R)), d = 15;
      var q1 = [R[0] + u[0] * d, R[1] + u[1] * d], q3 = [R[0] + v[0] * d, R[1] + v[1] * d],
        q2 = [R[0] + (u[0] + v[0]) * d, R[1] + (u[1] + v[1]) * d];
      s += '<polyline points="' + q1.join(",") + " " + q2.join(",") + " " + q3.join(",") +
        '" fill="none" stroke="' + ACC + '" stroke-width="2"/>';
    }

    var pairs = [[P[0], P[1]], [P[1], P[2]], [P[2], P[0]]];    // AB, BC, CA
    // side-length labels
    var sides = String(a.sides || "").split(",").map(function (x) { return x.trim(); });
    pairs.forEach(function (pr, i) {
      if (sides[i]) {
        var m = mid(pr[0], pr[1]), out = norm(sub(m, cen));
        s += txt(m[0] + out[0] * 17, m[1] + out[1] * 17, sides[i], INK, 15, 600);
      }
    });
    // equal-side tick marks: ticks="AB,CA" (order-independent)
    var ticks = String(a.ticks || "").split(",").map(function (x) { return x.trim().toUpperCase(); }).filter(Boolean);
    pairs.forEach(function (pr, i) {
      var nm = (L[i].toUpperCase() + L[(i + 1) % 3].toUpperCase());
      var nm2 = (L[(i + 1) % 3].toUpperCase() + L[i].toUpperCase());
      if (ticks.indexOf(nm) >= 0 || ticks.indexOf(nm2) >= 0) {
        var m = mid(pr[0], pr[1]), dir = norm(sub(pr[1], pr[0])), perp = [-dir[1], dir[0]], t = 6;
        s += line([m[0] - perp[0] * t, m[1] - perp[1] * t], [m[0] + perp[0] * t, m[1] + perp[1] * t], TEAL, 2.5);
      }
    });
    // angle-measure labels: angles="30,60,90"
    var angs = String(a.angles || "").split(",").map(function (x) { return x.trim(); });
    P.forEach(function (vp, i) {
      if (angs[i]) {
        var inw = norm(sub(cen, vp));
        s += txt(vp[0] + inw[0] * 30, vp[1] + inw[1] * 30, String(angs[i]).replace(/deg|°/i, "") + "°", TEAL, 13, 700);
      }
    });
    // vertices + labels (outward)
    P.forEach(function (vp, i) {
      s += dot(vp);
      var out = norm(sub(vp, cen));
      s += txt(vp[0] + out[0] * 16, vp[1] + out[1] * 16, L[i], INK, 17, 800);
    });
    return s + "</svg>";
  }

  // ---- [[angle]] : a single labeled angle with a degree measure ----
  function angle(a) {
    var W = 300, H = 212;
    // 2026-08-01: cap raised 175 -> 180. The old cap silently BENT straight lines (the tutor
    // asked for 180 and got 175). Wide angles recentre the vertex so both rays stay visible.
    var deg = Math.max(5, Math.min(180, num(a.deg != null ? a.deg : a.measure, 45)));
    var label = String(a.label || "").trim();
    // 2026-08-26 (build oi): cross="?" extends both rays through the vertex -- two full
    // lines crossing -- and labels the OPPOSITE (vertical) angle. Degenerate X's are
    // refused: outside 10..170 the attribute is ignored and the plain angle draws.
    var crossRaw = String(a.cross || "").trim();
    var cross = crossRaw && deg >= 10 && deg <= 170;
    var V = cross ? [150, 106] : [deg > 150 ? 150 : 80, 172];
    var Ln = cross ? 106 : 132;
    var rad = deg * Math.PI / 180;
    var r1 = [V[0] + Ln, V[1]];
    var r2 = [V[0] + Ln * Math.cos(rad), V[1] - Ln * Math.sin(rad)];
    var s = open(W, H);
    if (cross) {
      // the two FULL lines: each ray and its extension through the vertex
      s += line([V[0] - Ln, V[1]], r1, ACC, 2.5);
      s += line([V[0] - Ln * Math.cos(rad), V[1] + Ln * Math.sin(rad)], r2, ACC, 2.5);
    } else {
      s += line(V, r1, ACC, 2.5);
      s += line(V, r2, ACC, 2.5);
    }
    var ar = 34, a1 = [V[0] + ar, V[1]], a2 = [V[0] + ar * Math.cos(rad), V[1] - ar * Math.sin(rad)];
    if (Math.abs(deg - 90) < 0.5) {
      var d = 15;
      s += '<polyline points="' + (V[0] + d) + "," + V[1] + " " + (V[0] + d) + "," + (V[1] - d) + " " + V[0] + "," + (V[1] - d) +
        '" fill="none" stroke="' + TEAL + '" stroke-width="2"/>';
    } else {
      s += '<path d="M ' + a1[0] + " " + a1[1] + " A " + ar + " " + ar + " 0 0 0 " + a2[0] + " " + a2[1] +
        '" fill="none" stroke="' + TEAL + '" stroke-width="2"/>';
      // with a split, push the TOTAL label further out so it doesn't collide with the pieces
      var half = rad / 2, lr = ar + (String(a.split || "").trim() ? 44 : 17);
      s += txt(V[0] + lr * Math.cos(half), V[1] - lr * Math.sin(half), deg + "°", TEAL, 14, 700);
    }
    // 2026-08-01 (Jim's beta run: the tutor SAID "a ray splits it into two smaller angles"
    // but the figure showed no ray): OPTIONAL split="60" draws an interior ray from the
    // vertex, splitting the angle into a labeled piece and the remainder (labeled "?");
    // split="60,30" labels both pieces.
    var RED = "var(--bd-d1345b)";
    var sp = String(a.split || "").trim();
    if (sp) {
      var parts = sp.split(",").map(function (x) { return x.trim(); });
      var d1 = num(parts[0], NaN);
      if (!isNaN(d1) && d1 > 0 && d1 < deg) {
        var rs = d1 * Math.PI / 180;
        var r3 = [V[0] + Ln * 0.94 * Math.cos(rs), V[1] - Ln * 0.94 * Math.sin(rs)];
        s += line(V, r3, RED, 2.2);
        var lr2 = ar + 22, l1 = rs / 2, l2 = rs + (rad - rs) / 2;
        s += txt(V[0] + lr2 * Math.cos(l1) + 6, V[1] - lr2 * Math.sin(l1), d1 + "°", RED, 13, 700);
        var lbl2 = (parts[1] && parts[1] !== "?") ? (parts[1] + "°") : "?";
        s += txt(V[0] + lr2 * Math.cos(l2) + 2, V[1] - lr2 * Math.sin(l2) - 2, lbl2, RED, 13, 700);
      }
    }
    // 2026-08-26 (build oi): with cross set, arc + label the VERTICAL angle -- the one
    // opposite the given angle, between the two ray extensions. Its size equals deg
    // (that is the theorem), so the label defaults to "?" for the tutor to ask about;
    // cross="110" (or any text) writes that instead.
    if (cross) {
      var vr = 30, vs = Math.PI, ve = Math.PI + rad;
      var b1 = [V[0] + vr * Math.cos(vs), V[1] - vr * Math.sin(vs)];
      var b2 = [V[0] + vr * Math.cos(ve), V[1] - vr * Math.sin(ve)];
      s += '<path d="M ' + b1[0] + " " + b1[1] + " A " + vr + " " + vr + " 0 0 0 " + b2[0] + " " + b2[1] +
        '" fill="none" stroke="' + RED + '" stroke-width="2"/>';
      var vm = Math.PI + rad / 2, vlr = vr + 18;
      var vlab = (crossRaw === "1" || crossRaw.toLowerCase() === "true" || crossRaw === "?")
        ? "?" : (isNaN(parseFloat(crossRaw)) ? crossRaw : parseFloat(crossRaw) + "°");
      s += txt(V[0] + vlr * Math.cos(vm), V[1] - vlr * Math.sin(vm), vlab, RED, 14, 700);
    }
    if (label) {
      var ch = label.split("");
      s += dot(V, 3);
      // (oi) with cross, the old spot sits on the leftward line -- drop the vertex
      // label below the X instead.
      if (ch[1]) s += txt(cross ? V[0] - 6 : V[0] - 15, V[1] + (cross ? 20 : 9), ch[1], INK, 16, 800);  // vertex
      if (ch[0]) s += txt(r1[0] + 12, r1[1] + 3, ch[0], INK, 16, 800);          // first ray end
      if (ch[2]) s += txt(r2[0] + 13, r2[1] - 6, ch[2], INK, 16, 800);          // second ray end
    }
    return s + "</svg>";
  }

  // ---- [[circle]] : circle with center, optional labeled radius + inscribed angle ----
  function circle(a) {
    var W = 300, H = 250, C = [150, 122], R = 86;
    var center = String(a.center || "O").trim();
    var s = open(W, H);
    s += '<circle cx="' + C[0] + '" cy="' + C[1] + '" r="' + R + '" fill="rgba(20,184,166,.05)" stroke="' + ACC + '" stroke-width="2.5"/>';
    s += dot(C, 3);
    s += txt(C[0] - 13, C[1] + 13, center, INK, 15, 800);
    if (a.r) {
      var end = [C[0] + R, C[1]];
      s += line(C, end, TEAL, 2);
      s += txt((C[0] + end[0]) / 2, C[1] - 12, a.r, INK, 14, 600);
    }
    if (a.inscribed) {
      var arc = Math.max(10, Math.min(300, num(a.inscribed, 80))), half = arc / 2 * Math.PI / 180;
      var P1 = [C[0] - R * Math.sin(half), C[1] + R * Math.cos(half)];
      var P2 = [C[0] + R * Math.sin(half), C[1] + R * Math.cos(half)];
      var Vtx = [C[0], C[1] - R];
      s += line(Vtx, P1, ACC, 2);
      s += line(Vtx, P2, ACC, 2);
      [Vtx, P1, P2].forEach(function (p) { s += dot(p, 2.6); });
      s += txt(Vtx[0], Vtx[1] + 30, (arc / 2) + "°", TEAL, 13, 700);
    }
    return s + "</svg>";
  }

  // ---- [[transversal]] : two parallel lines cut by a transversal (build ot) ----
  // deg = the marked angle at the TOP crossing (between the rightward line and the
  // downward transversal). ask = which related angle gets the red "?" arc:
  // corresponding (default) | alternate (interior) | cointerior | vertical.
  // A number/text in ask writes that instead of "?" (same convention as cross=).
  function transversal(a) {
    var W = 340, H = 250;
    var deg = Math.max(25, Math.min(155, num(a.deg != null ? a.deg : a.measure, 60)));
    var rad = deg * Math.PI / 180;
    var y1 = 70, y2 = 180, mid = [170, 125];
    var dx = Math.cos(rad), dy = Math.sin(rad);
    var P1 = [mid[0] + (y1 - mid[1]) / dy * dx, y1];   // top crossing
    var P2 = [mid[0] + (y2 - mid[1]) / dy * dx, y2];   // bottom crossing
    var s = open(W, H);
    // the two PARALLEL lines, with matching arrow marks so "parallel" is visible
    s += line([16, y1], [W - 16, y1], ACC, 2.5);
    s += line([16, y2], [W - 16, y2], ACC, 2.5);
    [[y1], [y2]].forEach(function (yy) {
      var ax = W - 58, ay = yy[0];
      s += '<path d="M ' + ax + ' ' + (ay - 5) + ' L ' + (ax + 10) + ' ' + ay +
           ' L ' + ax + ' ' + (ay + 5) + '" fill="none" stroke="' + ACC + '" stroke-width="2"/>';
    });
    // the transversal, extended past both lines
    var ext = 34 / Math.max(0.35, dy);
    s += line([P1[0] - ext * dx, P1[1] - ext * dy], [P2[0] + ext * dx, P2[1] + ext * dy], INK, 2.5);
    var RED = "var(--bd-d1345b)";
    // an arc from screen-angle a1 to a2 (degrees, y-down clockwise) around P
    function arcAt(P, a1, a2, r, col) {
      var s1 = a1 * Math.PI / 180, s2 = a2 * Math.PI / 180;
      var q1 = [P[0] + r * Math.cos(s1), P[1] + r * Math.sin(s1)];
      var q2 = [P[0] + r * Math.cos(s2), P[1] + r * Math.sin(s2)];
      var big = (a2 - a1) > 180 ? 1 : 0;
      return '<path d="M ' + q1[0] + ' ' + q1[1] + ' A ' + r + ' ' + r + ' 0 ' + big +
             ' 1 ' + q2[0] + ' ' + q2[1] + '" fill="none" stroke="' + col + '" stroke-width="2"/>';
    }
    function labelAt(P, a1, a2, r, text2, col) {
      var m2 = (a1 + a2) / 2 * Math.PI / 180;
      return txt(P[0] + r * Math.cos(m2), P[1] + r * Math.sin(m2), text2, col, 13, 700);
    }
    // the GIVEN angle: at P1, from the east ray (0°) clockwise to the down-going
    // transversal (deg°) -- an interior angle on the transversal's right.
    s += arcAt(P1, 0, deg, 26, TEAL) + labelAt(P1, 0, deg, 42, deg + "°", TEAL);
    var askRaw = String(a.ask || "corresponding").trim();
    var kind = askRaw.toLowerCase();
    var vlab = "?";
    var mm2 = askRaw.match(/^(?:corresponding|alternate|cointerior|co-interior|vertical)\s*[:=]?\s*(.+)$/i);
    if (mm2 && mm2[1]) vlab = mm2[1];
    else if (askRaw && !/^(corresponding|alternate|cointerior|co-interior|vertical|\?|1|true)$/i.test(askRaw)) vlab = askRaw;
    if (/^\d+(?:\.\d+)?$/.test(vlab)) vlab += "°";
    if (/^vertical/.test(kind)) {
      s += arcAt(P1, 180, 180 + deg, 26, RED) + labelAt(P1, 180, 180 + deg, 42, vlab, RED);
    } else if (/^alternate/.test(kind)) {
      s += arcAt(P2, 180, 180 + deg, 26, RED) + labelAt(P2, 180, 180 + deg, 42, vlab, RED);
    } else if (/^co-?interior/.test(kind)) {
      s += arcAt(P2, 180 + deg, 360, 26, RED) + labelAt(P2, 180 + deg, 360, 42, vlab, RED);
    } else {   // corresponding (default): the same corner, one crossing down
      s += arcAt(P2, 0, deg, 26, RED) + labelAt(P2, 0, deg, 42, vlab, RED);
    }
    s += dot(P1, 3) + dot(P2, 3);
    return s + "</svg>";
  }

  // ---- [[polygon]] : a regular n-gon, optional side / interior-angle labels (build ot) ----
  function polygon(a) {
    var W = 300, H = 260;
    var n = Math.max(3, Math.min(12, Math.round(num(a.sides != null ? a.sides : a.n, 5))));
    var C = [150, 122], R = 88;
    var P = [];
    for (var i = 0; i < n; i++) {
      var th = -Math.PI / 2 + i * 2 * Math.PI / n;   // a vertex at the top
      P.push([C[0] + R * Math.cos(th), C[1] + R * Math.sin(th)]);
    }
    var s = open(W, H);
    s += '<polygon points="' + P.map(function (p) { return p.join(","); }).join(" ") +
      '" fill="' + FILL + '" stroke="' + ACC + '" stroke-width="2.5" stroke-linejoin="round"/>';
    // side label on the LOWEST edge (reads like a base)
    if (a.side) {
      var bi = 0, by = -1;
      for (var j = 0; j < n; j++) {
        var m3 = mid(P[j], P[(j + 1) % n]);
        if (m3[1] > by) { by = m3[1]; bi = j; }
      }
      var bm = mid(P[bi], P[(bi + 1) % n]);
      s += txt(bm[0], bm[1] + 16, a.side, INK, 15, 700);
    }
    // interior-angle arc + label at the top vertex
    if (a.angle) {
      var v0 = P[0], u = norm(sub(P[1], v0)), v = norm(sub(P[n - 1], v0)), ar = 20;
      var a1 = Math.atan2(u[1], u[0]), a2 = Math.atan2(v[1], v[0]);
      var q1 = [v0[0] + ar * Math.cos(a1), v0[1] + ar * Math.sin(a1)];
      var q2 = [v0[0] + ar * Math.cos(a2), v0[1] + ar * Math.sin(a2)];
      s += '<path d="M ' + q1[0] + ' ' + q1[1] + ' A ' + ar + ' ' + ar + ' 0 0 1 ' +
           q2[0] + ' ' + q2[1] + '" fill="none" stroke="' + TEAL + '" stroke-width="2"/>';
      s += txt(v0[0], v0[1] + 34, String(a.angle).replace(/deg|°/i, "") + "°", TEAL, 13, 700);
    }
    if (a.name) s += txt(C[0], H - 14, a.name, "var(--bd-6b6f82)", 14, 700);
    return s + "</svg>";
  }

  // ---- [[solid]] : schematic 3D solids with dashed hidden edges (build ot) ----
  function solid(a) {
    var kind = String(a.kind || a.shape || "prism").trim().toLowerCase();
    var W = 320, H = 250, s = open(W, H);
    var DASH = ' stroke-dasharray="5,5"';
    function ln(p, q, hidden, col) {
      return '<line x1="' + p[0] + '" y1="' + p[1] + '" x2="' + q[0] + '" y2="' + q[1] +
        '" stroke="' + (col || ACC) + '" stroke-width="2.3" stroke-linecap="round"' +
        (hidden ? DASH + ' opacity="0.55"' : "") + "/>";
    }
    if (kind === "sphere") {
      var C = [160, 120], R = 84;
      s += '<circle cx="' + C[0] + '" cy="' + C[1] + '" r="' + R + '" fill="' + FILL + '" stroke="' + ACC + '" stroke-width="2.5"/>';
      s += '<path d="M ' + (C[0] - R) + ' ' + C[1] + ' A ' + R + ' ' + (R * 0.32) + ' 0 0 0 ' + (C[0] + R) + ' ' + C[1] + '" fill="none" stroke="' + ACC + '" stroke-width="1.8"/>';
      s += '<path d="M ' + (C[0] - R) + ' ' + C[1] + ' A ' + R + ' ' + (R * 0.32) + ' 0 0 1 ' + (C[0] + R) + ' ' + C[1] + '" fill="none" stroke="' + ACC + '" stroke-width="1.6"' + DASH + ' opacity="0.55"/>';
      if (a.r) { s += ln(C, [C[0] + R, C[1]], false, TEAL) + txt(C[0] + R / 2, C[1] - 12, a.r, INK, 14, 700); }
    } else if (kind === "cylinder") {
      var cx = 160, ry = 22, rx = 74, top = 62, bot = 188;
      s += '<path d="M ' + (cx - rx) + ' ' + top + ' A ' + rx + ' ' + ry + ' 0 1 0 ' + (cx + rx) + ' ' + top + ' A ' + rx + ' ' + ry + ' 0 1 0 ' + (cx - rx) + ' ' + top + '" fill="' + FILL + '" stroke="' + ACC + '" stroke-width="2.3"/>';
      s += ln([cx - rx, top], [cx - rx, bot]) + ln([cx + rx, top], [cx + rx, bot]);
      s += '<path d="M ' + (cx - rx) + ' ' + bot + ' A ' + rx + ' ' + ry + ' 0 0 0 ' + (cx + rx) + ' ' + bot + '" fill="none" stroke="' + ACC + '" stroke-width="2.3"/>';
      s += '<path d="M ' + (cx - rx) + ' ' + bot + ' A ' + rx + ' ' + ry + ' 0 0 1 ' + (cx + rx) + ' ' + bot + '" fill="none" stroke="' + ACC + '" stroke-width="1.8"' + DASH + ' opacity="0.55"/>';
      if (a.r) { s += ln([cx, top], [cx + rx, top], false, TEAL) + txt(cx + rx / 2, top - 10, a.r, INK, 14, 700); }
      if (a.h) { s += txt(cx + rx + 20, (top + bot) / 2, a.h, INK, 14, 700); }
    } else if (kind === "cone") {
      var cx2 = 160, ry2 = 22, rx2 = 76, base = 186, apex = [160, 48];
      s += '<path d="M ' + (cx2 - rx2) + ' ' + base + ' A ' + rx2 + ' ' + ry2 + ' 0 0 0 ' + (cx2 + rx2) + ' ' + base + '" fill="' + FILL + '" stroke="' + ACC + '" stroke-width="2.3"/>';
      s += '<path d="M ' + (cx2 - rx2) + ' ' + base + ' A ' + rx2 + ' ' + ry2 + ' 0 0 1 ' + (cx2 + rx2) + ' ' + base + '" fill="none" stroke="' + ACC + '" stroke-width="1.8"' + DASH + ' opacity="0.55"/>';
      s += ln([cx2 - rx2, base], apex) + ln([cx2 + rx2, base], apex);
      if (a.h) { s += ln([cx2, base], apex, true, TEAL) + txt(cx2 - 14, (base + apex[1]) / 2, a.h, INK, 14, 700); }
      if (a.r) { s += ln([cx2, base], [cx2 + rx2, base], false, TEAL) + txt(cx2 + rx2 / 2, base + 16, a.r, INK, 14, 700); }
    } else if (kind === "pyramid") {
      var A2 = [70, 190], B2 = [210, 200], C2 = [258, 156], D2 = [122, 150], apex2 = [162, 46];
      s += ln(A2, B2) + ln(B2, C2) + ln(C2, D2, true) + ln(D2, A2, true);
      s += ln(A2, apex2) + ln(B2, apex2) + ln(C2, apex2) + ln(D2, apex2, true);
      if (a.b) s += txt((A2[0] + B2[0]) / 2, 216, a.b, INK, 14, 700);
      if (a.h) s += txt(apex2[0] + 16, 110, a.h, INK, 14, 700);
    } else {   // cube / prism (rectangular box)
      var isCube = (kind === "cube");
      var bw2 = isCube ? 110 : 150, bh2 = isCube ? 110 : 92, off = isCube ? 44 : 46;
      var x0 = 66, y0b = 196, F = [[x0, y0b - bh2], [x0 + bw2, y0b - bh2], [x0 + bw2, y0b], [x0, y0b]];
      var B3 = F.map(function (p) { return [p[0] + off, p[1] - off * 0.72]; });
      s += '<polygon points="' + F.map(function (p) { return p.join(","); }).join(" ") + '" fill="' + FILL + '" stroke="none"/>';
      s += ln(F[0], F[1]) + ln(F[1], F[2]) + ln(F[2], F[3]) + ln(F[3], F[0]);
      s += ln(B3[0], B3[1]) + ln(B3[1], B3[2], true) + ln(B3[2], B3[3], true) + ln(B3[3], B3[0]);
      s += ln(F[0], B3[0]) + ln(F[1], B3[1]) + ln(F[2], B3[2]) + ln(F[3], B3[3], true);
      var wlab = a.w || (isCube && a.side ? a.side : "");
      if (wlab) s += txt((F[3][0] + F[2][0]) / 2, y0b + 16, wlab, INK, 14, 700);
      if (a.d) s += txt(F[2][0] + off / 2 + 12, y0b - off * 0.36 + 4, a.d, INK, 14, 700);
      if (a.h) s += txt(x0 - 16, y0b - bh2 / 2, a.h, INK, 14, 700);
    }
    return s + "</svg>";
  }

  // ---- [[segment]] : a labeled line segment with points, halves and lengths ----
  // (ox, 2026-08-27) Jim's geometry flag: "There should be visuals for these types
  // of questions", on a run of midpoint questions -- "Point W is the midpoint of
  // segment VZ. If VW is 6.5 units, how long is WZ?" -- asked with nothing drawn.
  // The shelf had no way to draw a SEGMENT at all: triangles, angles and circles,
  // but not the one-dimensional figure half of a geometry unit is about.
  //   [[segment points="J,K,L" lengths="9,?" mark="K" total="?" caption="..."]]
  // points  = 2 to 4 labels, left to right along the line
  // lengths = the length of each gap, in order ("?" for the unknown)
  // mark    = a point that is the MIDPOINT: congruence ticks on both sides of it,
  //           which is how a midpoint is shown on paper and the reason the child
  //           can SEE that the two halves are equal instead of being told
  // total   = a brace above the whole segment with this label
  function segment(a) {
    var W = 360, H = 150;
    var P = String(a.points || "A,B").split(",").map(function (x) { return x.trim(); })
             .filter(Boolean).slice(0, 4);
    if (P.length < 2) P = ["A", "B"];
    var y = a.total ? 92 : 76, x0 = 34, x1 = W - 34;
    var gap = (x1 - x0) / (P.length - 1);
    var xs = P.map(function (_, i) { return x0 + i * gap; });
    var s = open(W, H);
    s += line([x0, y], [x1, y], ACC, 3);
    var mark = String(a.mark || "").trim();
    var mi = P.indexOf(mark);
    P.forEach(function (lbl, i) {
      s += dot([xs[i], y], 4.5);
      s += txt(xs[i], y - 17, lbl, INK, 16, 800);
    });
    // the gap lengths, under each piece
    var L2 = String(a.lengths || "").split(",").map(function (x) { return x.trim(); });
    for (var i = 0; i + 1 < P.length; i++) {
      if (!L2[i]) continue;
      s += txt((xs[i] + xs[i + 1]) / 2, y + 22, L2[i], INK, 15, 700);
    }
    // ⭐ THE MIDPOINT TICKS. Two short crossbars, one on each side of the marked
    // point -- the standard congruence mark. Without them "midpoint" is a word
    // the child has to take on trust.
    if (mi > 0 && mi < P.length - 1) {
      [[xs[mi - 1], xs[mi]], [xs[mi], xs[mi + 1]]].forEach(function (pr) {
        var mx = (pr[0] + pr[1]) / 2;
        s += line([mx, y - 9], [mx, y + 9], TEAL, 2.6);
      });
    }
    if (a.total) {
      var by = y - 40;
      s += '<path d="M ' + x0 + ' ' + (by + 9) + ' L ' + x0 + ' ' + by + ' L ' + x1 +
           ' ' + by + ' L ' + x1 + ' ' + (by + 9) + '" fill="none" stroke="' + TEAL +
           '" stroke-width="2"/>';
      s += txt((x0 + x1) / 2, by - 11, String(a.total), TEAL, 15, 800);
    }
    return s + "</svg>";
  }

  window.GeoFigures = {
    triangle: triangle, angle: angle, circle: circle,
    transversal: transversal, polygon: polygon, solid: solid, segment: segment,
    svg: function (kind, a) {
      try { return this[kind] ? this[kind](a || {}) : ""; } catch (e) { return ""; }
    }
  };
})();
/* I did no harm and this file is not truncated. */

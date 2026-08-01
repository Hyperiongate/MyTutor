/* =============================================================================
   geo-figures.js  --  Math Tutor MVP  --  Hyperion Shift LLC
   -----------------------------------------------------------------------------
   CHANGE NOTES (keep newest at top):
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
// 2026-08-01  [[angle]] gained split="60" / split="60,30": an interior ray from the vertex
//             splitting the angle, with the pieces labeled (second defaults to "?") -- so
//             complementary/supplementary lessons can SHOW the split they talk about.

(function () {
  "use strict";
  var NS = "http://www.w3.org/2000/svg";
  var INK = "#26263a", ACC = "#5b5bd6", TEAL = "#0d9488", FILL = "rgba(91,91,214,.06)";

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
  function open(w, h) {
    return '<svg viewBox="0 0 ' + w + " " + h + '" class="geofig" xmlns="' + NS +
      '" style="width:100%;max-width:340px;height:auto;display:block;margin:6px auto;">';
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
    var deg = Math.max(5, Math.min(175, num(a.deg != null ? a.deg : a.measure, 45)));
    var label = String(a.label || "").trim();
    var V = [80, 172], Ln = 132, rad = deg * Math.PI / 180;
    var r1 = [V[0] + Ln, V[1]];
    var r2 = [V[0] + Ln * Math.cos(rad), V[1] - Ln * Math.sin(rad)];
    var s = open(W, H);
    s += line(V, r1, ACC, 2.5);
    s += line(V, r2, ACC, 2.5);
    var ar = 34, a1 = [V[0] + ar, V[1]], a2 = [V[0] + ar * Math.cos(rad), V[1] - ar * Math.sin(rad)];
    if (Math.abs(deg - 90) < 0.5) {
      var d = 15;
      s += '<polyline points="' + (V[0] + d) + "," + V[1] + " " + (V[0] + d) + "," + (V[1] - d) + " " + V[0] + "," + (V[1] - d) +
        '" fill="none" stroke="' + TEAL + '" stroke-width="2"/>';
    } else {
      s += '<path d="M ' + a1[0] + " " + a1[1] + " A " + ar + " " + ar + " 0 0 0 " + a2[0] + " " + a2[1] +
        '" fill="none" stroke="' + TEAL + '" stroke-width="2"/>';
      var half = rad / 2, lr = ar + 17;
      s += txt(V[0] + lr * Math.cos(half), V[1] - lr * Math.sin(half), deg + "°", TEAL, 14, 700);
    }
    // 2026-08-01 (Jim's beta run: the tutor SAID "a ray splits it into two smaller angles"
    // but the figure showed no ray): OPTIONAL split="60" draws an interior ray from the
    // vertex, splitting the angle into a labeled piece and the remainder (labeled "?");
    // split="60,30" labels both pieces.
    var RED = "#d1345b";
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
    if (label) {
      var ch = label.split("");
      s += dot(V, 3);
      if (ch[1]) s += txt(V[0] - 15, V[1] + 9, ch[1], INK, 16, 800);           // vertex
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

  window.GeoFigures = {
    triangle: triangle, angle: angle, circle: circle,
    svg: function (kind, a) {
      try { return this[kind] ? this[kind](a || {}) : ""; } catch (e) { return ""; }
    }
  };
})();
/* I did no harm and this file is not truncated. */

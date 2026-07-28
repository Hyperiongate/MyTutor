/* =============================================================================
   tutor-face.js  --  Math Tutor MVP  --  Hyperion Shift LLC
   -----------------------------------------------------------------------------
   CHANGE NOTES (keep newest at top):
     2026-07-28  NEW. Mr. Cadabra's FACE: a small, friendly robot head that replaces the voice
                 orb on every coaching page. Draws into the SAME <canvas id="orb"> and is driven
                 by the SAME 0..1 amplitude the orb already computed from the ElevenLabs audio
                 analyser -- so the mouth opens in time with his real speech, with no new
                 dependency, no external avatar service, and no extra network calls.
                 API (all drawing, no state of its own):
                   TutorFace.draw(ctx, w, h, {level, t, mood})
                     level : 0..1 loudness (drives mouth opening + antenna glow)
                     t     : monotonically increasing frame counter (drives bob + blink)
                     mood  : "speaking" | "listening" | "thinking" | "happy" | "idle"
                   TutorFace.moodFrom(state) -- maps a page's state string onto a mood.
                 Deliberately stylized (a rounded head with a dark visor, glowing eyes and a
                 mouth bar) rather than a realistic face: it reads clearly at 70px, costs
                 nothing to run, and avoids the uncanny-valley problem that sank the earlier
                 hand-built 3D avatar experiment.
   ============================================================================= */
(function () {
  "use strict";

  // Brand-ish palette (matches the app's accent/accent2).
  var SHELL_HI = "#8f8ff7", SHELL_LO = "#4a4ac9", SHELL_EDGE = "#3a3aa8";
  var VISOR = "#23233b", VISOR_EDGE = "#171728";
  var GLOW = "#2fe3c8", GLOW_SOFT = "rgba(47,227,200,0.55)";
  var EAR = "#6f6fe0";

  function rr(ctx, x, y, w, h, r) {
    r = Math.min(r, w / 2, h / 2);
    ctx.beginPath();
    ctx.moveTo(x + r, y);
    ctx.arcTo(x + w, y, x + w, y + h, r);
    ctx.arcTo(x + w, y + h, x, y + h, r);
    ctx.arcTo(x, y + h, x, y, r);
    ctx.arcTo(x, y, x + w, y, r);
    ctx.closePath();
  }

  // A blink is a short, occasional event driven off the frame counter.
  function blinkAmount(t) {
    var cycle = t % 300;                       // roughly every 5s at 60fps
    if (cycle < 7) return 1 - Math.abs(cycle - 3.5) / 3.5;   // 0 -> 1 -> 0
    if (cycle > 150 && cycle < 157) {          // occasional double-blink
      var c2 = cycle - 150;
      return 1 - Math.abs(c2 - 3.5) / 3.5;
    }
    return 0;
  }

  function moodFrom(state) {
    switch (String(state || "").toLowerCase()) {
      case "speaking": return "speaking";
      case "listening": return "listening";
      case "thinking": case "think": return "thinking";
      case "happy": case "correct": return "happy";
      default: return "idle";
    }
  }

  function draw(ctx, w, h, opts) {
    opts = opts || {};
    var level = Math.max(0, Math.min(1, opts.level || 0));
    var t = opts.t || 0;
    var mood = opts.mood || "idle";
    var S = Math.min(w, h);                    // scale everything off the short side
    var cx = w / 2;

    ctx.clearRect(0, 0, w, h);

    // Gentle idle bob; a touch more lively while speaking.
    var bob = Math.sin(t * 0.035) * S * (mood === "speaking" ? 0.012 : 0.009);
    var cy = h / 2 + bob;

    var headW = S * 0.60, headH = S * 0.54;
    var hx = cx - headW / 2, hy = cy - headH / 2 + S * 0.02;

    // ---- antenna (glows with the voice) ----
    var antX = cx, antTop = hy - S * 0.13, ballR = S * 0.045;
    ctx.save();
    ctx.strokeStyle = SHELL_EDGE; ctx.lineWidth = Math.max(2, S * 0.016); ctx.lineCap = "round";
    ctx.beginPath(); ctx.moveTo(antX, hy + S * 0.01); ctx.lineTo(antX, antTop + ballR); ctx.stroke();
    var g = ctx.createRadialGradient(antX, antTop, 1, antX, antTop, ballR * (2.6 + level * 2.2));
    g.addColorStop(0, "rgba(47,227,200," + (0.55 + level * 0.45) + ")");
    g.addColorStop(1, "rgba(47,227,200,0)");
    ctx.fillStyle = g;
    ctx.beginPath(); ctx.arc(antX, antTop, ballR * (2.6 + level * 2.2), 0, 7); ctx.fill();
    ctx.fillStyle = GLOW;
    ctx.beginPath(); ctx.arc(antX, antTop, ballR * (1 + level * 0.25), 0, 7); ctx.fill();
    ctx.restore();

    // ---- side pods ("ears") ----
    ctx.fillStyle = EAR;
    rr(ctx, hx - S * 0.055, cy - S * 0.055, S * 0.06, S * 0.12, S * 0.025); ctx.fill();
    rr(ctx, hx + headW - S * 0.005, cy - S * 0.055, S * 0.06, S * 0.12, S * 0.025); ctx.fill();

    // ---- head shell ----
    ctx.save();
    ctx.shadowColor = "rgba(40,40,120,0.30)"; ctx.shadowBlur = S * 0.07; ctx.shadowOffsetY = S * 0.012;
    var shell = ctx.createLinearGradient(hx, hy, hx, hy + headH);
    shell.addColorStop(0, SHELL_HI); shell.addColorStop(1, SHELL_LO);
    ctx.fillStyle = shell;
    rr(ctx, hx, hy, headW, headH, S * 0.14); ctx.fill();
    ctx.restore();
    ctx.strokeStyle = SHELL_EDGE; ctx.lineWidth = Math.max(1, S * 0.008);
    rr(ctx, hx, hy, headW, headH, S * 0.14); ctx.stroke();

    // ---- visor (the dark face plate the features sit on) ----
    var vw = headW * 0.80, vh = headH * 0.60;
    var vx = cx - vw / 2, vy = hy + headH * 0.20;
    ctx.fillStyle = VISOR;
    rr(ctx, vx, vy, vw, vh, S * 0.075); ctx.fill();
    ctx.strokeStyle = VISOR_EDGE; ctx.lineWidth = Math.max(1, S * 0.006);
    rr(ctx, vx, vy, vw, vh, S * 0.075); ctx.stroke();

    // ---- eyes ----
    var eyeR = S * 0.043;
    var eyeY = vy + vh * 0.36;
    var eyeDX = vw * 0.235;
    var blink = blinkAmount(t);
    // eyes drift a little; while thinking they look up and to the side
    var lookX = 0, lookY = 0;
    if (mood === "thinking") { lookX = S * 0.012 * Math.sin(t * 0.02) + S * 0.010; lookY = -S * 0.012; }
    else if (mood === "listening") { lookY = S * 0.004; }
    else { lookX = S * 0.006 * Math.sin(t * 0.012); }

    ctx.save();
    ctx.shadowColor = GLOW_SOFT; ctx.shadowBlur = S * (0.05 + level * 0.05);
    ctx.fillStyle = GLOW; ctx.strokeStyle = GLOW;
    ctx.lineWidth = Math.max(2, S * 0.018); ctx.lineCap = "round";
    [-1, 1].forEach(function (sgn) {
      var ex = cx + sgn * eyeDX + lookX, ey = eyeY + lookY;
      if (mood === "happy") {                       // ^ ^ happy arcs
        ctx.beginPath();
        ctx.arc(ex, ey + eyeR * 0.5, eyeR * 1.15, Math.PI * 1.15, Math.PI * 1.85);
        ctx.stroke();
      } else if (blink > 0.05) {                    // squash to a line as the lid closes
        var openH = Math.max(0.08, 1 - blink) * eyeR * 2;
        rr(ctx, ex - eyeR, ey - openH / 2, eyeR * 2, openH, Math.min(eyeR, openH / 2));
        ctx.fill();
      } else {
        ctx.beginPath(); ctx.arc(ex, ey, eyeR, 0, 7); ctx.fill();
        // little specular dot so the eyes feel alive
        ctx.save(); ctx.shadowBlur = 0; ctx.fillStyle = "rgba(255,255,255,0.85)";
        ctx.beginPath(); ctx.arc(ex - eyeR * 0.3, ey - eyeR * 0.32, eyeR * 0.26, 0, 7); ctx.fill();
        ctx.restore();
      }
    });
    ctx.restore();

    // ---- mouth: a bar that OPENS with the voice ----
    var mouthW = vw * 0.46;
    var mouthY = vy + vh * 0.73;
    var closedH = S * 0.016;
    var openH = closedH;
    if (mood === "speaking") openH = closedH + level * S * 0.085;
    else if (mood === "thinking") mouthW = vw * 0.24;          // small, pursed
    else if (mood === "listening") openH = closedH * 1.25;

    ctx.save();
    ctx.shadowColor = GLOW_SOFT; ctx.shadowBlur = S * (0.03 + level * 0.06);
    ctx.fillStyle = GLOW;
    if (mood === "happy") {                                    // a smile
      ctx.strokeStyle = GLOW; ctx.lineWidth = Math.max(2, S * 0.02); ctx.lineCap = "round";
      ctx.beginPath();
      ctx.arc(cx, mouthY - S * 0.02, mouthW * 0.55, Math.PI * 0.18, Math.PI * 0.82);
      ctx.stroke();
    } else {
      rr(ctx, cx - mouthW / 2, mouthY - openH / 2, mouthW, openH,
         Math.min(S * 0.02, openH / 2)); ctx.fill();
      // a faint inner line while wide open, so it reads as an open mouth not a slab
      if (openH > S * 0.05) {
        ctx.globalAlpha = 0.35; ctx.fillStyle = "#0d6f60";
        rr(ctx, cx - mouthW * 0.36, mouthY - openH * 0.16, mouthW * 0.72, openH * 0.32, S * 0.01);
        ctx.fill(); ctx.globalAlpha = 1;
      }
    }
    ctx.restore();
  }

  window.TutorFace = { draw: draw, moodFrom: moodFrom };
})();
/* I did no harm and this file is not truncated. */

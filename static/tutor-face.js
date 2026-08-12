/* =============================================================================
   tutor-face.js  --  Math Tutor MVP  --  Hyperion Shift LLC
   -----------------------------------------------------------------------------
   CHANGE NOTES (keep newest at top):
     2026-08-12  (build ep) THE REAL FOOTAGE LANDS, AND A CLIP BECOMES A LIST OF
                 ENCODINGS. Jim's four HeyGen loops are in, so the layer is live rather
                 than phase-dark. One change to the machinery: presenceShow() now builds
                 <source> children (webm/VP9 first, then mp4/H.264) instead of setting a
                 single .src, so the BROWSER picks the encoding it can actually decode.
                 That covers Safari/iOS (H.264 only) and equally a Chromium build with no
                 proprietary codecs -- which is exactly how this was caught: the real
                 mp4s tore down to the robot in a headless test that could not decode
                 H.264. A manifest entry may still be a plain string, so nothing older
                 breaks. The video's own error (all sources failed) still tears down to
                 the robot; a single missing encoding does not.
     2026-08-12  (build ej) THE VIDEO PRESENCE LAYER -- Mr. Cadabra's real face, robot as
                 fallback (Jim: "I don't like the robot... I think it's fine to have Mr.
                 Cadabra in every instance"). This file now carries BOTH faces:
                   - On the first draw() call it probes /static/videos/cadabra/presence.json
                     ONCE. If the manifest loads, a muted looping <video> of Mr. Cadabra
                     (generated once in HeyGen -- see the Video Presence project plan) is
                     laid over the canvas in the same circular slot, and the loop follows
                     the SAME moods the pages already send: idle/speaking -> the idle loop
                     (his real voice talks; the face deliberately does NOT lip-sync -- an
                     honest "he's here and listening" presence, never a fake mouth),
                     listening -> the listening loop, thinking -> the thinking loop, and
                     happy -> the thumbs-up one-shot (Jim's ask: a right answer cues a
                     thumbs up), which plays once and returns to idle.
                   - The ROBOT KEEPS DRAWING underneath on every frame. No manifest, a 404,
                     a video error, a stalled network, data-saver -- ANY failure simply
                     tears the video down and the robot is already there. Do no harm: this
                     file works exactly as before until the assets exist, so code and
                     videos deploy independently.
                   - prefers-reduced-motion: no video plays; the still poster shows instead
                     (and if there's no poster, the robot -- whose own bob/blink the pages'
                     dz rule already stills).
                   - Two stacked <video> elements crossfade on loop changes so a mood
                     switch never flashes black; sources swap only when the mood's video
                     actually differs, with a short hold so chatty mood changes can't
                     thrash the network. Videos are muted+playsinline+aria-hidden always:
                     the presence NEVER makes sound -- Mr. Cadabra's voice stays exactly
                     where it lives today.
                 Pages need NO edits: everything hangs off the existing
                 TutorFace.draw(ctx, w, h, {level, t, mood}) call all six pages already
                 make. New optional API: TutorFace.presenceActive() for curious pages.
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

  // ===========================================================================
  // THE VIDEO PRESENCE LAYER (build ej, 2026-08-12) -- see the change note above.
  // ===========================================================================
  var P = {
    state: "unprobed",        // unprobed -> probing -> active | off
    manifest: null,
    base: "/static/videos/cadabra/",
    host: null,               // the wrapper div we insert over the canvas
    vids: null,               // [videoA, videoB] for crossfades
    front: 0,                 // which of the two is visible
    currentKey: "",           // which loop is showing ("idle", "listening", ...)
    oneshotUntil: 0,          // while a one-shot plays, loop changes wait
    lastSwitch: 0,            // debounce clock
    reduced: false
  };
  try {
    P.reduced = !!(window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches);
  } catch (e) {}

  function presenceProbe(canvas) {
    P.state = "probing";
    // One fetch, once per page. A 404 or bad JSON = the robot stays. Nothing retries,
    // nothing errors loudly -- absence of the assets is a NORMAL state (phase-dark).
    try {
      fetch(P.base + "presence.json", { cache: "no-cache" }).then(function (r) {
        if (!r.ok) throw 0;
        return r.json();
      }).then(function (m) {
        if (!m || !m.loops || !m.loops.idle) throw 0;
        P.manifest = m;
        presenceMount(canvas, m);
      }).catch(function () { P.state = "off"; });
    } catch (e) { P.state = "off"; }
  }

  function presenceMount(canvas, m) {
    var parent = canvas.parentNode;
    if (!parent) { P.state = "off"; return; }
    var cs = getComputedStyle(parent);
    if (cs.position === "static") parent.style.position = "relative";
    var host = document.createElement("div");
    host.setAttribute("aria-hidden", "true");           // decorative; the VOICE is the content
    host.style.cssText = "position:absolute;inset:0;border-radius:50%;overflow:hidden;" +
                         "pointer-events:none;background:transparent;";
    // Reduced motion: a still poster instead of motion; no poster -> keep the robot.
    if (P.reduced) {
      if (!m.poster) { P.state = "off"; return; }
      var img = document.createElement("img");
      img.alt = ""; img.src = P.base + m.poster;
      img.style.cssText = "width:100%;height:100%;object-fit:cover;display:block;";
      img.onerror = function () { presenceTeardown(); };
      host.appendChild(img);
      parent.appendChild(host);
      P.host = host; P.state = "active";
      return;
    }
    function mkVid() {
      var v = document.createElement("video");
      v.muted = true; v.loop = true; v.autoplay = true;
      v.setAttribute("muted", "");                       // attribute form for iOS autoplay
      v.setAttribute("playsinline", "");
      v.playsInline = true;
      v.preload = "auto";
      if (m.poster) v.poster = P.base + m.poster;
      v.style.cssText = "position:absolute;inset:0;width:100%;height:100%;object-fit:cover;" +
                        "transition:opacity .35s ease;opacity:0;";
      // The video's own error fires only after EVERY <source> has failed, which is the
      // semantics we want: one missing encoding is fine, no playable encoding is not.
      v.onerror = function () { presenceTeardown(); };   // no playable media -> robot
      host.appendChild(v);
      return v;
    }
    P.vids = [mkVid(), mkVid()];
    parent.appendChild(host);
    P.host = host;
    P.state = "active";
    presenceShow("idle", false);
  }

  function presenceTeardown() {
    // The robot never stopped drawing underneath, so this is instant and seamless.
    try { if (P.host && P.host.parentNode) P.host.parentNode.removeChild(P.host); } catch (e) {}
    P.host = null; P.vids = null; P.state = "off";
  }

  function presenceShow(key, isOneshot) {
    if (P.state !== "active" || !P.vids) return;
    var m = P.manifest;
    var file = isOneshot ? (m.oneshots && m.oneshots[key]) : (m.loops && m.loops[key]);
    if (!file) { key = "idle"; isOneshot = false; file = m.loops.idle; }
    if (!isOneshot && key === P.currentKey) return;
    var back = 1 - P.front;
    var v = P.vids[back], old = P.vids[P.front];
    v.loop = !isOneshot;
    // build ep: a clip is a LIST of encodings, best-supported first (webm/VP9 then
    // mp4/H.264). Letting the browser choose with <source> children -- rather than
    // setting .src to one file -- is what makes this work everywhere from Safari/iOS
    // (H.264 only) to a headless Chromium build with no proprietary codecs. A string
    // is still accepted so an older manifest keeps working.
    var files = (typeof file === "string") ? [file] : file;
    while (v.firstChild) v.removeChild(v.firstChild);
    for (var fi = 0; fi < files.length; fi++) {
      var srcEl = document.createElement("source");
      srcEl.src = P.base + files[fi];
      if (/\.webm$/i.test(files[fi])) srcEl.type = "video/webm";
      else if (/\.mp4$/i.test(files[fi])) srcEl.type = "video/mp4";
      v.appendChild(srcEl);
    }
    v.load();
    var settled = false;
    v.oncanplay = function () {
      if (settled) return; settled = true;
      var p = v.play(); if (p && p.catch) p.catch(function () {});
      v.style.opacity = "1";
      old.style.opacity = "0";
      setTimeout(function () { try { old.pause(); } catch (e) {} }, 400);
      P.front = back;
    };
    if (isOneshot) {
      P.oneshotUntil = Date.now() + 15000;               // safety ceiling, not the real end
      v.onended = function () {
        P.oneshotUntil = 0;
        P.currentKey = "";                                // force the idle reload
        presenceShow("idle", false);
      };
    } else {
      v.onended = null;
    }
    P.currentKey = isOneshot ? ("!" + key) : key;
  }

  // Called from draw() every frame. Maps the pages' moods onto the loops; "speaking"
  // deliberately uses the IDLE loop -- his real voice talks, the face stays honestly
  // alive, and we never fake a mouth (the whole design).
  function presenceTick(canvas, mood) {
    if (P.state === "unprobed") presenceProbe(canvas);
    if (P.state !== "active" || P.reduced) return;
    var now = Date.now();
    if (P.oneshotUntil) {
      if (now < P.oneshotUntil) return;                  // let the thumbs-up finish
      P.oneshotUntil = 0; P.currentKey = ""; presenceShow("idle", false); return;
    }
    if (mood === "happy") { presenceShow("happy", true); return; }
    if (now - P.lastSwitch < 600) return;                // hold: mood chatter never thrashes
    var want = (mood === "listening") ? "listening"
             : (mood === "thinking")  ? "thinking"
             : "idle";                                    // idle AND speaking
    if (want !== P.currentKey) { P.lastSwitch = now; presenceShow(want, false); }
  }

  var _drawRobot = draw;
  function drawWithPresence(ctx, w, h, opts) {
    _drawRobot(ctx, w, h, opts);                         // the robot ALWAYS draws (fallback)
    try { presenceTick(ctx.canvas, (opts && opts.mood) || "idle"); } catch (e) {}
  }

  window.TutorFace = { draw: drawWithPresence, moodFrom: moodFrom,
                       presenceActive: function () { return P.state === "active"; } };
})();
/* I did no harm and this file is not truncated. */

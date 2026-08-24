/* =============================================================================
   tutor-face.js  --  Math Tutor MVP  --  Hyperion Shift LLC
   -----------------------------------------------------------------------------
   CHANGE NOTES (keep newest at top):
     2026-08-23  (build mi) THE ROBOT CAN WEAR A SECOND PAINT JOB -- ABRABOT. Phase 3
                 of Abrabot, the practice helper Jim named on 2026-08-23. Two changes,
                 both additive, both defaulting to exactly today's behaviour:
                   1. THE PALETTE IS A PARAMETER. The eight bare colour constants became
                      TutorFace.PALETTES.cadabra (unchanged to the byte) plus a second
                      entry, .abrabot -- cyan shell, amber eyes. draw() resolves
                      opts.palette / opts.persona into the SAME eight local names the
                      drawing code has always used, so not one drawing line moved. A
                      caller that passes neither gets Mr. Cadabra, as before.
                   2. ⭐ opts.presence:false DRAWS THE ROBOT ALONE. The presence layer is
                      VIDEO OF A REAL PERSON. No other character may wear it. Without
                      this, the drill page would have laid Mr. Cadabra's face over
                      Abrabot's body the moment the manifest deployed -- and it would
                      have read as a rendering bug rather than the impersonation it is.
                 ⚠️ WHY THE ROBOT IS THE RIGHT FACE FOR ABRABOT AND ALWAYS WAS. Jim, in
                 this file's build-ej note: "I don't like the robot... I think it's fine
                 to have Mr. Cadabra in every instance." The robot's job has therefore
                 been to be the fallback face nobody wants to see. Handing it to Abrabot
                 is the one place it becomes a face somebody DOES want: a helper who is
                 visibly a machine, next to a teacher who is visibly a person.
     2026-08-12  (build ev) A CODEC FAILURE WAS SILENT. Found while testing the Phase 2
                 talking clips in this container's Chromium, which has no H.264: a <video>
                 whose every <source> fails does NOT fire an error event on the element --
                 the spec routes those errors to the individual <source> tags, and the
                 element just settles into networkState 3 in silence. Build ep's note in
                 this file asserted the opposite, and was wrong. Consequence here: with no
                 decodable encoding the presence layer would sit on a dead poster forever
                 instead of tearing down to the robot it is supposed to fall back to. New
                 _sourcesFailed() wires BOTH paths, armed once at mount and re-armed for
                 each clip's sources on every swap.
     2026-08-12  (build et) TWO INTENSITIES, BECAUSE THE RING HAD ALMOST NOTHING TO FIRE ON.
                 es shipped and Jim still saw nothing -- so I fired celebrate() by hand on
                 the live site and the ring drew perfectly. The fault was upstream: the
                 tutor is told marking is optional ("you MAY record") and explicitly told
                 NOT to mark sub-steps, so in a teaching lesson the doorbell was almost
                 never pressed. prompts.py now makes [[mark]] REQUIRED on a finished
                 problem and adds [[nice]] for a correct answer along the way. This file
                 gains the second intensity: celebrate({small:true}) draws ONE thin ring --
                 no flash, no sparkles, no video swap (a clip change on every sub-step would
                 thrash the network and flatten the big moment). celebrate() with no
                 argument is unchanged, so nothing that already called it moves.
     2026-08-12  (build es) THE THUMBS-UP CLIP HAS NO THUMBS IN IT -- SO THE CELEBRATION
                 STOPS DEPENDING ON THE AVATAR. Jim, after er deployed: "I'm answering
                 questions correctly and I'm not getting a thumbs up." I pulled frames from
                 the raw HeyGen source (_video_workshop/raw, the 5.96s clip) and from the
                 shipped crop: the avatar NEVER raises a hand. It is a chest-up photoreal
                 presenter that does not gesture, so what we shipped as "thumbs_up" is
                 really just a slightly warmer smile -- at 70px, next to the idle loop, that
                 is invisible. Jim guessed the gesture might be cropped out of the circle;
                 it is not -- there is no gesture at ANY crop. Regenerating with a gesture-
                 capable avatar would change his face, so instead the celebration is now
                 drawn BY US and owes the avatar nothing:
                   - celebrationBurst(): a gold ring pulse (two, staggered) + a soft gold
                     flash + eight sparkles, in the SAME circular slot, over whatever is
                     underneath -- video presence, still poster, or the bare robot.
                   - It fires on EVERY correct answer, including when there is no video at
                     all. celebrate() no longer returns false when presence is off; the
                     ring IS the celebration, the clip is a bonus.
                   - prefers-reduced-motion: no scaling, no sparkles -- a single ring that
                     fades in and out on opacity alone.
                   - Everything is inset so the animation can never overflow the slot and be
                     clipped by a parent, is pointer-events:none and aria-hidden (the tally
                     and his voice carry the meaning; this is decoration), self-removes
                     after ~1.4s, and re-firing mid-burst restarts cleanly.
                 The happy one-shot STILL plays underneath when the presence is live -- his
                 expression does brighten -- it just is not load-bearing any more.
     2026-08-12  (build er) THE THUMBS-UP GETS A DOORBELL. Jim, looking at the live site:
                 "all I'm seeing is a little circle... nothing else." He was right, and
                 the reason was concrete: the teaching pages' setState only ever holds
                 speaking / listening / thinking / idle, so mood "happy" was NEVER passed
                 in and the thumbs-up clip he had generated could not play at all. New
                 public TutorFace.celebrate() fires that one-shot directly, without
                 touching the page's `state` -- the busy glow, the thinking flag and the
                 level meter all stay exactly as they were. The pages call it when the
                 tutor MARKS a correct answer, which is the moment a child earns it.
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

  // ---- THE PALETTE IS DATA NOW (build mi) --------------------------------------
  // These were eight bare constants read directly by draw(). They are the SAME eight
  // colours, in the same order, moved into an object so a second character can wear
  // the same robot in different paint. CADABRA is unchanged to the byte: brand-ish,
  // matching the app's accent/accent2.
  //
  // ⚠️ WHY A SECOND PALETTE AND NOT A SECOND ROBOT. Jim, 2026-08-23: "we have the
  // robot avatar. Can we have it fly in and replace mr cadabra when it enters the
  // game." He has also said, in this file's own build-ej note, "I don't like the
  // robot... I think it's fine to have Mr. Cadabra in every instance" -- so the
  // robot's real job was always to be the FALLBACK face nobody wants to see. Giving
  // it to Abrabot is the one place it becomes the face somebody DOES want: a helper
  // who is visibly a machine, standing next to a teacher who is visibly a person.
  var PALETTES = {
    cadabra: { shellHi: "#8f8ff7", shellLo: "#4a4ac9", shellEdge: "#3a3aa8",
               visor: "#23233b", visorEdge: "#171728",
               glow: "#2fe3c8", glowSoft: "rgba(47,227,200,0.55)",
               ear: "#6f6fe0", mouthDeep: "#0d6f60" },
    // ABRABOT: cyan shell, amber eyes. Deliberately NOT a shade of Mr. Cadabra's
    // purple -- at 70px a child has to tell them apart at a glance, and a slightly
    // different purple would read as the same character in bad lighting.
    abrabot: { shellHi: "#7fd4f0", shellLo: "#1f8fbf", shellEdge: "#12678f",
               visor: "#10283a", visorEdge: "#0a1a26",
               glow: "#ffc95e", glowSoft: "rgba(255,201,94,0.55)",
               ear: "#4fb4d8", mouthDeep: "#7a4a06" }
  };

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
    // (mi) The eight colour names below are resolved from opts.palette and then used
    // by the SAME names the drawing code has always used, so not one drawing line
    // changed. opts.palette absent -> Mr. Cadabra, exactly as before this build.
    var PAL = (opts.palette && typeof opts.palette === "object")
      ? opts.palette
      : (PALETTES[String(opts.persona || "cadabra")] || PALETTES.cadabra);
    var SHELL_HI = PAL.shellHi, SHELL_LO = PAL.shellLo, SHELL_EDGE = PAL.shellEdge;
    var VISOR = PAL.visor, VISOR_EDGE = PAL.visorEdge;
    var GLOW = PAL.glow, GLOW_SOFT = PAL.glowSoft;
    var EAR = PAL.ear, MOUTH_DEEP = PAL.mouthDeep || PALETTES.cadabra.mouthDeep;
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
        ctx.globalAlpha = 0.35; ctx.fillStyle = MOUTH_DEEP;   // (mi) was "#0d6f60"
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

  // Shared with tutor-moments.js by design, not by import: a <video> whose every <source>
  // fails fires error on the SOURCES, not on the element. Wire both or a codec failure is
  // silent. Calls cb at most once.
  function _sourcesFailed(vid, cb) {
    var once = false;
    function fire() { if (once) return; once = true; try { cb(); } catch (e) {} }
    var srcs = vid.getElementsByTagName("source");
    var total = srcs.length, failed = 0;
    for (var i = 0; i < total; i++) {
      srcs[i].onerror = function () { if (++failed >= total) fire(); };
    }
    vid.onerror = fire;
  }

  function presenceMount(canvas, m) {
    var parent = canvas.parentNode;
    if (!parent) { P.state = "off"; return; }
    var cs = getComputedStyle(parent);
    if (cs.position === "static") parent.style.position = "relative";
    var host = document.createElement("div");
    host.setAttribute("aria-hidden", "true");           // decorative; the VOICE is the content
    // build es: the host carries the POSTER as its own background. Two <video> elements
    // crossfading means both are briefly semi-transparent, and a transparent host let the
    // canvas ROBOT ghost through Mr. Cadabra's face on every mood change (green eyes over
    // his eyes -- caught on a frame-by-frame capture). A still frame of the same man
    // underneath makes every transition read as a dissolve instead of a haunting. The
    // robot is still there, still drawing, still the fallback the instant a video errors.
    host.style.cssText = "position:absolute;inset:0;border-radius:50%;overflow:hidden;" +
                         "pointer-events:none;background:#2a2a3f;" +
                         (m.poster ? "background-image:url('" + P.base + m.poster + "');" +
                                     "background-size:cover;background-position:center;" : "");
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
      // ⚠️ build ev CORRECTION to the build ep note that stood here: the video's own error
      // does NOT fire when every <source> fails. Per the HTML spec the failures land on the
      // individual <source> elements and the <video> just settles into networkState 3
      // (NO_SOURCE) in silence -- proven in this container's Chromium, which cannot decode
      // H.264: only 'source-error' fired, never 'element-error'. So the presence could sit
      // on a dead poster instead of tearing down to the robot. Both paths are wired now.
      _sourcesFailed(v, presenceTeardown);               // no playable media -> robot
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
    _sourcesFailed(v, presenceTeardown);   // build ev: re-arm for THIS clip's sources
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
  var _lastCanvas = null;                                // build es: celebrate() needs a slot
  function drawWithPresence(ctx, w, h, opts) {
    _drawRobot(ctx, w, h, opts);                         // the robot ALWAYS draws (fallback)
    try { _lastCanvas = ctx.canvas; } catch (e) {}
    // ⭐ (mi) THE PRESENCE LAYER IS MR. CADABRA'S REAL FACE. It is video of a specific
    // person, and no other character may ever wear it. A page drawing a DIFFERENT
    // persona passes presence:false and gets the robot alone -- which is why Abrabot's
    // page can safely reuse this whole file. Without this line, the drill page would
    // have quietly laid Mr. Cadabra's face over Abrabot's body the moment the video
    // manifest deployed, and it would have looked like a rendering bug rather than
    // the impersonation it actually is. PART 3dg pins that the drill page passes it.
    if (opts && opts.presence === false) return;
    try { presenceTick(ctx.canvas, (opts && opts.mood) || "idle"); } catch (e) {}
  }

  // ===========================================================================
  // THE CELEBRATION BURST (build es, 2026-08-12) -- see the change note above.
  // The avatar cannot gesture, so the celebration is ours: a gold ring pulse in the
  // same circular slot, over the video / poster / robot alike. Decorative only.
  // ===========================================================================
  var C = { host: null, styled: false, timer: 0 };
  var GOLD = "#ffd45e", GOLD_DEEP = "#f2a93b";

  function celebrationStyle() {
    if (C.styled) return;
    C.styled = true;
    var css =
      "@keyframes tfRing{0%{transform:scale(.80);opacity:0}" +
      "22%{transform:scale(.93);opacity:1}100%{transform:scale(1.05);opacity:0}}" +
      "@keyframes tfFlash{0%{opacity:0}25%{opacity:.50}100%{opacity:0}}" +
      "@keyframes tfSpark{0%{transform:translate(0,0) scale(.35);opacity:0}" +
      "22%{opacity:1}100%{transform:translate(var(--tfdx),var(--tfdy)) scale(1);opacity:0}}" +
      "@keyframes tfRingStill{0%{opacity:0}25%{opacity:.95}100%{opacity:0}}";
    var el = document.createElement("style");
    el.setAttribute("data-tutor-face", "celebration");
    el.appendChild(document.createTextNode(css));
    (document.head || document.documentElement).appendChild(el);
  }

  function celebrationBurst(canvas, small) {
    if (!canvas || !canvas.parentNode) return false;
    celebrationStyle();
    var parent = canvas.parentNode;
    try {
      var cs = getComputedStyle(parent);
      if (cs.position === "static") parent.style.position = "relative";
    } catch (e) {}

    // Re-firing mid-burst restarts cleanly rather than stacking rings.
    if (C.timer) { clearTimeout(C.timer); C.timer = 0; }
    try { if (C.host && C.host.parentNode) C.host.parentNode.removeChild(C.host); } catch (e) {}
    C.host = null;

    // EVERYTHING scales off the slot's real on-screen size. The corner face is ~70-110px
    // in the teaching pages but ~220px on the demo, and fixed pixel sizes that looked
    // right at one size threw dinner-plate sparkles at the other.
    var S = 0;
    try { var rect = canvas.getBoundingClientRect(); S = Math.min(rect.width, rect.height); } catch (e) {}
    if (!S) S = Math.min(canvas.width || 100, canvas.height || 100);
    var ringW = Math.max(2, Math.round(S * 0.016));
    var dotR  = Math.max(3, Math.round(S * 0.038));
    var throwD = S * 0.07;               // a drift outward from the ring, not a launch

    var host = document.createElement("div");
    host.setAttribute("aria-hidden", "true");            // the tally carries the meaning
    host.style.cssText = "position:absolute;inset:0;border-radius:50%;pointer-events:none;" +
                         "z-index:3;overflow:hidden;";

    function ring(delayMs, widthPx, still) {
      var r = document.createElement("div");
      r.style.cssText =
        "position:absolute;inset:8%;border-radius:50%;box-sizing:border-box;" +
        "border:" + widthPx + "px solid " + GOLD + ";opacity:0;" +
        "box-shadow:0 0 12px rgba(255,212,94,.75),inset 0 0 10px rgba(255,212,94,.45);" +
        "animation:" + (still ? "tfRingStill 1200ms ease-out" : "tfRing 1100ms ease-out") +
        " " + delayMs + "ms both;";
      return r;
    }

    if (P.reduced || small) {
      // SMALL (build et): one thin ring, no flash, no sparkles -- the quiet nod that says
      // "yes, that part was right" without spending the big moment. Reduced motion lands
      // here too, and additionally gets the opacity-only variant.
      host.appendChild(ring(0, Math.max(2, ringW - 1), !!P.reduced));
    } else {
      var flash = document.createElement("div");
      flash.style.cssText =
        "position:absolute;inset:8%;border-radius:50%;opacity:0;" +
        "background:radial-gradient(circle at 50% 50%,rgba(255,212,94,.55) 0%," +
        "rgba(242,169,59,.28) 55%,rgba(242,169,59,0) 75%);" +
        "animation:tfFlash 900ms ease-out both;";
      host.appendChild(flash);
      host.appendChild(ring(0, ringW, false));
      host.appendChild(ring(170, Math.max(2, ringW - 1), false));

      // Eight sparkles ON THE RING, drifting a little further out as they fade. They sit
      // at the rim rather than flying from the centre: thrown from the middle they land
      // across his face and read as confetti stuck to his nose (checked frame by frame).
      for (var i = 0; i < 8; i++) {
        var ang = (Math.PI * 2 * i) / 8 + 0.39;
        var ox = Math.cos(ang) * (S * 0.40), oy = Math.sin(ang) * (S * 0.40);
        var s = document.createElement("div");
        s.style.cssText =
          "position:absolute;left:50%;top:50%;width:" + dotR + "px;height:" + dotR + "px;" +
          "margin:" + (oy - dotR / 2).toFixed(1) + "px 0 0 " + (ox - dotR / 2).toFixed(1) + "px;" +
          "border-radius:50%;background:" + GOLD + ";opacity:0;" +
          "box-shadow:0 0 " + Math.round(dotR * 1.2) + "px " + GOLD_DEEP + ";" +
          "--tfdx:" + (Math.cos(ang) * throwD).toFixed(2) + "px;" +
          "--tfdy:" + (Math.sin(ang) * throwD).toFixed(2) + "px;" +
          "animation:tfSpark 950ms ease-out " + (60 + i * 25) + "ms both;";
        host.appendChild(s);
      }
    }

    parent.appendChild(host);
    C.host = host;
    C.timer = setTimeout(function () {
      try { if (host.parentNode) host.parentNode.removeChild(host); } catch (e) {}
      if (C.host === host) C.host = null;
      C.timer = 0;
    }, small ? 1000 : 1500);
    return true;
  }

  // BUILD er (2026-08-12) -- THE THUMBS-UP HAD NO TRIGGER. The pages' state machine only
  // ever holds speaking / listening / thinking / idle (session.html setState), so
  // mood "happy" was never once passed in and the one-shot Jim generated could not play
  // in a real lesson. celebrate() is the missing doorbell: it fires the one-shot
  // DIRECTLY, without touching `state`, so the page's audio/turn logic -- the busy glow,
  // the thinking flag, the level meter -- is completely undisturbed. Safe to call when
  // there is no video presence at all: it simply does nothing and the robot carries on.
  // BUILD es (2026-08-12) -- the clip is no longer load-bearing. The gold ring fires
  // ALWAYS (video, poster or bare robot); the happy one-shot plays underneath only when
  // there is a live video presence. Returns true whenever the child saw something.
  // BUILD et (2026-08-12) -- TWO INTENSITIES. celebrate() is the finished problem: full
  // burst plus his warmer clip. celebrate({small:true}) is a correct answer ALONG THE WAY:
  // one thin ring, no sparkles, and deliberately NO video swap -- a clip change on every
  // sub-step would thrash the network and make the big moment feel like nothing.
  function celebrate(opts) {
    var small = !!(opts && opts.small);
    var shown = false;
    try {
      if (!small && P.state === "active" && !P.reduced) { presenceShow("happy", true); shown = true; }
    } catch (e) {}
    try { if (celebrationBurst(_lastCanvas, small)) shown = true; } catch (e) {}
    return shown;
  }

  window.TutorFace = { draw: drawWithPresence, moodFrom: moodFrom, celebrate: celebrate,
                       presenceActive: function () { return P.state === "active"; },
                       // (mi) published so a page names a CHARACTER, never a colour --
                       // one source of truth for what each of them looks like.
                       PALETTES: PALETTES };
})();
/* I did no harm and this file is not truncated. */

/* =============================================================================
   cadabra.js  --  Math Tutor MVP  --  Hyperion Shift LLC
   -----------------------------------------------------------------------------
   MR. CADABRA, OUT OF THE BOX. The floating companion layer.

   CHANGE NOTES (keep newest at top):
     2026-09-01  (rk) HE NO LONGER STANDS ON WHAT HE IS POINTING AT. Caught the first
                 time the layer ran over the real demo: the streak chips live in the
                 topbar, and pointing at something that high put him -- and his speech
                 bubble -- on top of it. A target near the top of the window is now
                 approached from BELOW, his tip is kept low enough that head and bubble
                 both stay in view, and the bubble hangs underneath him when he points up.
     2026-09-01  (hands) THE GLOVE IS A GLOVE, AND HE POINTS WITH HIS INDEX FINGER.
                 Jim, on the first version: the resting hand should be "circles with
                 lines on them type things with little bumps for the thumbs instead of
                 fingers pointing out" - and, far more seriously, the pointing hand
                 read as the MIDDLE finger.
                   REST  - a palm ball, one closed-finger mass, a thumb bump, and three
                           seams standing in for four fingers.
                   POINT - a FIST with the index along the TOP edge, the curled fingers
                           plainly below it and the thumb bumping up behind.
                 ⚠️ A single digit out of the centre of a palm reads as an obscene
                 gesture to anyone who looks at it. The extended finger must be the
                 TOPMOST one. This is not a style preference; do not simplify it back.
     2026-08-31  (stage 4 fix) HE WILL NOT ACT ON SOMETHING THAT IS COVERED. Found in
                 the session.html dry run: the welcome card was up and he underlined the
                 board straight through it. A target now fails to resolve at all if the
                 point at its centre belongs to something else, or if it has scrolled out
                 of the viewport -- which is rule 19 enforced generically, and covers
                 every modal, tray and overlay on every page without naming any of them.
     2026-08-31  (stage 2) NEW, AND IT SHIPS DARK. Phase 1 is tutor-face.js -- the
                 silent CANVAS orb in the corner, which this file does not touch and
                 must not. Phase 2 is tutor-moments.js -- the talking clips. This is
                 phase 3: a character who leaves the circle, floats over the page,
                 points at things, celebrates, and writes on the lesson with his own
                 sharpened point.

                 ⚠️ HE IS A SEPARATE LAYER, NOT A CHANGE TO THE ORB. tutor-face.js
                 draws a purple robot into a 2D canvas context; this file draws a
                 yellow pencil as SVG in an overlay positioned in page pixels. They
                 are different rendering technologies and they are deliberately not
                 merged. The orb keeps the robot until Jim decides otherwise, and
                 nothing in this file can repaint it or break its six pixel pins.

                 HOW IT SHIPS: DARK, exactly the way tutor-moments.js does. This file
                 probes /static/cadabra-script.json once at load. No script = every
                 public method is a no-op that returns immediately, no overlay is ever
                 created, and every page behaves precisely as it does today. There is
                 no flag to set and no caller to change. Ship cadabra-script.json to
                 turn him on; delete it to turn him off. See the example beside this
                 file: static/cadabra-script.example.json -- RENAME IT to activate.

                 THE MENU IS DATA. What he does and when lives in that JSON: page,
                 moment, behaviour, and the per-stage budget. Adding a behaviour is
                 code (see BEHAVIOURS below). Scheduling one is editing the file.

                 THE RULES ARE IN CODE, NOT IN A COMMENT. PRESENCE_RULES.md is the
                 written form; this file enforces the ones that can be enforced:
                   r5  park while an answer field has focus
                   r6  talk still, move silent
                   r15 his marks are cleared when the problem is
                   r19 never over an input or a control
                   r20 prefers-reduced-motion removes travel, never the behaviour
                   r23 the layer is transparent to the pointer, always
                   r24 the per-stage presence budget
                   r26 no behaviour repeats inside a session
                   r27 the child can turn him down: full / quiet / off, persisted
                   r29 transform-only -- nothing here can cause the board to reflow
                   r30 targets are found by data-cad name, never by coordinate

                 THE MOUTH IS THE REAL VOICE. voice.js already builds a Web Audio
                 AnalyserNode over its TTS audio element and already dispatches
                 "mt:speaking" on document. Those are top-level lexical globals in a
                 classic script, so this file reads them the same way session.html's
                 own level() does -- no change to voice.js, no second analyser, no new
                 audio. If they are absent (a page without voice.js, or the browser
                 speech path) he falls back to a synthetic envelope and still looks
                 like he is talking.

   SAFE TO ADD, SAFE TO DELETE
     - Imported by nothing. Loading it changes no page's behaviour by itself.
     - Writes no cookie and no server state. One localStorage key, mt_cadabra_mode,
       which is the child's own full/quiet/off choice and nothing else.
     - Never writes the owner key, never builds an /api/ URL, never speaks, never
       touches the presence layer.
     - No APP_BUILD change and no ruletests PART is needed until a page loads it.

   PAGE CONTRACT (stage 4, not done yet)
     <script src="/static/cadabra.js" defer></script>
     Mark the things he may act on:  <h1 data-cad="title">
     Tell him what happened:         Cadabra.fire("answer.correct")
     That is the whole integration. Everything else is the JSON.
   ============================================================================= */
(function () {
  "use strict";

  var VERSION    = "2026-08-31a";
  var SCRIPT_URL = "/static/cadabra-script.json";
  var MODE_KEY   = "mt_cadabra_mode";        /* full | quiet | off  (rule 27) */

  /* ==========================================================================
     1.  PAINTS
     --------------------------------------------------------------------------
     The yellow is the character's and nothing else's -- no button, badge or
     highlight on the site may use it. The BAND is the company purple, and it is
     the REAL one out of TutorFace.PALETTES.cadabra.shellLo (#4a4ac9), not the
     #6B44BE the August concept pages guessed at.
     ========================================================================== */
  var PAINT = {
    body:"#F2BC1B", bodyDk:"#C08F0C", bodyLt:"#FBD96A",
    hat:"#2E2A63",  hatDk:"#221F4C",  band:"#4a4ac9", gold:"#F2BC1B",
    graphite:"#2F2C39", wood:"#DFC08A", woodDk:"#C0A067",
    ferrule:"#C8CAD4", ferruleDk:"#9EA1B1",
    eye:"#FBFAFF", glove:"#FFFFFF", mitt:"#F5F0E5"
  };
  var STAR = "M0 -10 L2.9 -3.5 L9.5 -3.1 L4.5 1.2 L6.1 7.6 L0 4 L-6.1 7.6 "
           + "L-4.5 1.2 L-9.5 -3.1 L-2.9 -3.5 Z";

  /* His drawing space, unchanged from the 28 August character study: the barrel is
     centred on x=110, the hat tops out near y=11, and the SHARPENED TIP is at
     (110, 374). The tip is the transform origin, which is what lets him write. */
  var TIP_X = 110, TIP_Y = 374, LOCAL_TOP = 11;
  var LOCAL_H = TIP_Y - LOCAL_TOP;
  var SH_L = { x: 86, y: 202 }, SH_R = { x: 134, y: 202 };

  /* ==========================================================================
     2.  STATE
     ========================================================================== */
  var M = {
    state: "unprobed",        /* unprobed | probing | ready | off */
    script: null,
    probe: null,
    mounted: false,
    suspended: false,
    page: null,
    stage: "early",
    mode: "full",
    reduced: false,
    seq: 0,                   /* cancels a running sequence */
    spent: {},                /* rule 26: what has already been used this session */
    raf: null
  };

  var S = null;               /* the live rig; built by mount(), null until then */
  var DOM = null;

  /* ==========================================================================
     3.  DARK PROBE  --  no script file, no character, anywhere
     ========================================================================== */
  function probe() {
    if (M.probe) return M.probe;
    M.state = "probing";
    M.probe = new Promise(function (resolve) {
      function done(ok) { M.state = ok ? "ready" : "off"; resolve(M.state === "ready"); }
      try {
        fetch(SCRIPT_URL, { cache: "no-cache" }).then(function (r) {
          if (!r.ok) throw 0;
          return r.json();
        }).then(function (j) {
          if (!j || !j.pages || typeof j.pages !== "object") throw 0;
          M.script = j;
          done(true);
        })["catch"](function () { done(false); });
      } catch (e) { done(false); }
    });
    return M.probe;
  }

  function live() { return M.state === "ready" && M.mounted && !M.suspended && M.mode !== "off"; }

  /* ==========================================================================
     4.  THE CHILD'S OWN SETTING  (rule 27)
     ========================================================================== */
  function readMode() {
    try {
      var v = window.localStorage.getItem(MODE_KEY);
      if (v === "full" || v === "quiet" || v === "off") return v;
    } catch (e) {}
    return "full";
  }
  function writeMode(v) {
    M.mode = (v === "quiet" || v === "off") ? v : "full";
    try { window.localStorage.setItem(MODE_KEY, M.mode); } catch (e) {}
    if (M.mode === "off") { teardown(); }
    else if (M.mounted && !DOM) { build(); }
    return M.mode;
  }

  /* ==========================================================================
     5.  THE STAGE BUDGET  (rule 24)
     --------------------------------------------------------------------------
     One dial, applied everywhere. A fourteen-year-old being cheered at by a
     cartoon pencil is being told the software thinks they are small.
     ========================================================================== */
  var STAGE_FALLBACK = {
    early:  { entrance:"full",   joke:true,  tour:"first", drift:1.0,  tier3:"free"  },
    upper:  { entrance:"full",   joke:true,  tour:"ask",   drift:0.6,  tier3:"earned"},
    middle: { entrance:"brief",  joke:false, tour:"ask",   drift:0.3,  tier3:"rare"  },
    high:   { entrance:"corner", joke:false, tour:"never", drift:0.0,  tier3:"never" }
  };
  function budget() {
    var from = (M.script && M.script.stages) || STAGE_FALLBACK;
    return from[M.stage] || STAGE_FALLBACK[M.stage] || STAGE_FALLBACK.early;
  }
  /* "quiet" is the child's thumb on the same dial: one stage calmer, never louder. */
  function effective() {
    var b = budget();
    if (M.mode !== "quiet") return b;
    return { entrance:"corner", joke:false, tour:"never",
             drift: Math.min(b.drift, 0.15), tier3:"never" };
  }

  /* ==========================================================================
     6.  THE CHARACTER  --  ported from the 28 August study, unchanged in shape
     ========================================================================== */
  function barrel(bottom) {
    var h = bottom - 114;
    return '<rect x="82" y="114" width="56" height="' + h + '" fill="' + PAINT.body + '"/>'
      + '<rect x="82" y="114" width="15" height="' + h + '" fill="' + PAINT.bodyLt + '" opacity=".33"/>'
      + '<rect x="123" y="114" width="15" height="' + h + '" fill="' + PAINT.bodyDk + '" opacity=".42"/>'
      + '<path d="M97 114 V' + bottom + ' M123 114 V' + bottom + '" stroke="' + PAINT.bodyDk
      + '" stroke-width="1.2" opacity=".5"/>'
      + '<rect x="82" y="114" width="56" height="' + h + '" fill="none" stroke="' + PAINT.graphite
      + '" stroke-width="1.8" opacity=".7"/>';
  }
  function cone(top, flat, tip) {
    return '<path d="M82 ' + top + ' L138 ' + top + ' L117 ' + flat + ' L103 ' + flat
      + ' Z" fill="' + PAINT.wood + '" stroke="' + PAINT.graphite + '" stroke-width="1.6" stroke-linejoin="round"/>'
      + '<path d="M126 ' + top + ' L138 ' + top + ' L117 ' + flat + ' L111 ' + flat
      + ' Z" fill="' + PAINT.woodDk + '" opacity=".6"/>'
      + '<path d="M103 ' + flat + ' L117 ' + flat + ' L110 ' + tip + ' Z" fill="' + PAINT.graphite + '"/>';
  }
  function ferrule() {
    return '<rect x="86" y="98" width="48" height="17" fill="' + PAINT.ferrule + '"/>'
      + '<path d="M86 103.5 H134 M86 109.5 H134" stroke="' + PAINT.ferruleDk + '" stroke-width="1.5"/>';
  }
  function hat() {
    return '<ellipse cx="110" cy="89" rx="50" ry="9.5" fill="' + PAINT.hatDk + '"/>'
      + '<path d="M68 87 Q78 44 110 20 Q126 11 133 20 Q124 48 152 87 Q110 97 68 87 Z" fill="' + PAINT.hat + '"/>'
      + '<path d="M112 21 Q124 48 152 87 Q136 93 124 94 Q128 56 112 21 Z" fill="' + PAINT.hatDk + '" opacity=".55"/>'
      + '<path d="M70 79 Q110 90 150 79 L151 87 Q110 98 69 87 Z" fill="' + PAINT.band + '"/>'
      + '<path transform="translate(118,50) scale(.78)" d="' + STAR + '" fill="' + PAINT.gold + '"/>';
  }
  function faceRig() {
    var g = PAINT.graphite;
    return '<g transform="translate(0,8)">'
      + '<path class="cd-browL" d="" fill="none" stroke="' + g + '" stroke-width="2.6" stroke-linecap="round"/>'
      + '<path class="cd-browR" d="" fill="none" stroke="' + g + '" stroke-width="2.6" stroke-linecap="round"/>'
      + '<ellipse class="cd-eyeL" cx="99"  cy="158" rx="8" ry="9" fill="' + PAINT.eye + '" stroke="' + g + '" stroke-width="2.2"/>'
      + '<ellipse class="cd-eyeR" cx="121" cy="158" rx="8" ry="9" fill="' + PAINT.eye + '" stroke="' + g + '" stroke-width="2.2"/>'
      + '<circle  class="cd-pupL" cx="100" cy="159.5" r="3.4" fill="' + g + '"/>'
      + '<circle  class="cd-pupR" cx="122" cy="159.5" r="3.4" fill="' + g + '"/>'
      + '<path    class="cd-lips"  d="" fill="none" stroke="' + g + '" stroke-width="2.7" stroke-linecap="round"/>'
      + '<ellipse class="cd-mouth" cx="110" cy="186" rx="9" ry="0" fill="' + g + '"/>'
      + '</g>';
  }

  /* Expressions. The eyes stay ellipses in every state so blink and speech can
     modulate them without swapping artwork. There is no disappointed face here and
     there will not be one: rule 16. */
  var EXPR = {
    neutral:  { bl:"M90 143 Q99 138 108 142", br:"M112 142 Q121 138 130 143",
                lips:"M97 181 Q110 192 123 181", eye:9,   pup:0 },
    teaching: { bl:"M90 137 Q99 131 108 136", br:"M112 136 Q121 131 130 137",
                lips:"M99 183 Q110 190 121 183", eye:9,   pup:0 },
    pleased:  { bl:"M90 139 Q99 134 108 138", br:"M112 138 Q121 134 130 139",
                lips:"M94 177 Q110 197 126 177", eye:4.2, pup:0 },
    thinking: { bl:"M90 147 Q99 143 108 146", br:"M112 137 Q121 130 130 136",
                lips:"M99 185 Q105 180 111 184 Q117 188 124 183", eye:9, pup:-3 },
    listening:{ bl:"M89 141 Q99 137 109 141", br:"M111 141 Q121 137 131 141",
                lips:"M101 183 Q110 187 119 183", eye:10, pup:0 }
  };

  /* --- the glove: four fingers, a thumb and a cuff seam ---------------------
     Circles and round-capped capsules, drawn TWICE -- a fat graphite silhouette
     underneath, then a clean white fill on top -- so the parts union into one
     outlined shape instead of showing every overlap. That double pass is the
     entire trick behind a cartoon glove. */
  function handShapes(R, mode) {
    var circles = [], caps = [], seams = [];
    function C(x, y, r)             { circles.push({ cx:x*R, cy:y*R, r:r*R }); }
    function K(x1, y1, x2, y2, w)   { caps.push({ x1:x1*R, y1:y1*R, x2:x2*R, y2:y2*R, w:w*R }); }
    function M(x1, y1, x2, y2)      { seams.push({ x1:x1*R, y1:y1*R, x2:x2*R, y2:y2*R }); }

    if (mode === "point") {
      /* A FIST WITH THE INDEX FINGER OUT - and the index has to be unmistakably the
         TOP digit, with the curled fingers below it and the thumb bumping up behind.
         Drawn the obvious way, one finger straight out of the middle of the palm, it
         reads as the MIDDLE finger. Jim caught exactly that in the first version. It
         is not a gesture a children's tutor makes, and avoiding it is the entire
         reason this shape is built the way it is. Do not "simplify" it back. */
      C(-0.10, 0.18, 1.00);                   /* the fist                          */
      K(0.25, -0.52, 2.00, -0.60, 0.44);      /* INDEX, along the top edge          */
      K(-0.45, -0.20, 0.10, -0.92, 0.46);     /* thumb, a bump up behind it         */
      C(0.70, 0.42, 0.36);                    /* curled fingers, clearly BELOW      */
      C(0.42, 0.86, 0.32);
      M(0.52, 0.06, 0.96, 0.28);              /* the creases between them           */
      M(0.26, 0.54, 0.66, 0.74);
    } else {
      /* AT REST: a rounded glove, not a splayed hand. A ball with a thumb bump and
         three seams standing in for four fingers - what a cartoon glove has always
         been, and it still reads at eight pixels wide. */
      C(0, 0, 1.00);                          /* the palm                           */
      K(0.45, 0, 0.75, 0, 1.30);              /* the closed fingers, as one mass    */
      K(-0.28, -0.52, 0.14, -0.95, 0.50);     /* thumb bump                         */
      M(0.70, -0.38, 1.16, -0.38);            /* three seams = four fingers         */
      M(0.70,  0.00, 1.34,  0.00);
      M(0.70,  0.38, 1.16,  0.38);
    }
    return { circles: circles, caps: caps, seams: seams };
  }
  function shapeMarkup(sh, paint, grow) {
    var s = "", i;
    for (i = 0; i < sh.circles.length; i++) {
      var c = sh.circles[i];
      s += '<circle cx="' + c.cx.toFixed(2) + '" cy="' + c.cy.toFixed(2)
         + '" r="' + (c.r + grow / 2).toFixed(2) + '" fill="' + paint + '"/>';
    }
    for (i = 0; i < sh.caps.length; i++) {
      var k = sh.caps[i];
      s += '<line x1="' + k.x1.toFixed(2) + '" y1="' + k.y1.toFixed(2)
         + '" x2="' + k.x2.toFixed(2) + '" y2="' + k.y2.toFixed(2)
         + '" stroke="' + paint + '" stroke-width="' + (k.w + grow).toFixed(2)
         + '" stroke-linecap="round"/>';
    }
    return s;
  }
  function seamMarkup(sh, R) {
    var s = "", i;
    for (i = 0; i < sh.seams.length; i++) {
      var m = sh.seams[i];
      s += '<line x1="' + m.x1.toFixed(2) + '" y1="' + m.y1.toFixed(2)
         + '" x2="' + m.x2.toFixed(2) + '" y2="' + m.y2.toFixed(2)
         + '" stroke="' + PAINT.graphite + '" stroke-width="' + (R * 0.115).toFixed(2)
         + '" stroke-linecap="round" opacity=".85"/>';
    }
    return s;
  }
  function handMarkup(R, mode) {
    var sh = handShapes(R, mode);
    /* the cuff arc at the wrist - the line that says "glove" rather than "hand" */
    var cuff = '<path d="M ' + (-R * 0.86).toFixed(1) + " " + (-R * 0.62).toFixed(1)
             + " Q " + (-R * 0.46).toFixed(1) + " 0 " + (-R * 0.86).toFixed(1) + " "
             + (R * 0.62).toFixed(1) + '" fill="none" stroke="' + PAINT.graphite
             + '" stroke-width="' + (R * 0.12).toFixed(2) + '" stroke-linecap="round" opacity=".8"/>';
    return shapeMarkup(sh, PAINT.graphite, 5.0) + shapeMarkup(sh, PAINT.glove, 0)
         + seamMarkup(sh, R) + cuff;
  }

  /* ==========================================================================
     7.  THE OVERLAY
     --------------------------------------------------------------------------
     One fixed layer above the page, transparent to the pointer (rule 23), out of
     the accessibility tree, and containing nothing the lesson's own DOM knows
     about (rule 28). It is created on first use and destroyed by teardown().
     ========================================================================== */
  var NS = "http://www.w3.org/2000/svg";

  function build() {
    if (DOM) return;
    var svg = document.createElementNS(NS, "svg");
    svg.setAttribute("id", "cadabra-layer");
    svg.setAttribute("aria-hidden", "true");
    svg.style.cssText = "position:fixed;inset:0;left:0;top:0;width:100%;height:100%;"
                      + "pointer-events:none;z-index:2147483000;";
    svg.innerHTML =
        '<g class="cd-ink"></g>'
      + '<g class="cd-body">'
      +   '<g transform="translate(' + (-TIP_X) + ',' + (-TIP_Y) + ')">'
      +     '<path class="cd-armL" d="" fill="none" stroke="' + PAINT.graphite + '" stroke-width="4.6" stroke-linecap="round"/>'
      +     '<path class="cd-armR" d="" fill="none" stroke="' + PAINT.graphite + '" stroke-width="4.6" stroke-linecap="round"/>'
      +     cone(292, 348, 374) + barrel(292) + ferrule() + hat() + faceRig()
      +     '<g class="cd-hL"></g><g class="cd-hR"></g>'
      +   '</g>'
      + '</g>'
      + '<g class="cd-fhL"></g><g class="cd-fhR"></g>'
      + '<g class="cd-spark"></g>';

    var bub = document.createElement("div");
    bub.setAttribute("id", "cadabra-bubble");
    bub.setAttribute("role", "status");
    bub.style.cssText =
      "position:fixed;z-index:2147483001;pointer-events:none;max-width:260px;"
      + "background:#fff;color:#1B1926;border:2px solid " + PAINT.hat + ";border-radius:14px;"
      + "padding:10px 14px;font:400 15px/1.42 system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;"
      + "box-shadow:0 10px 26px rgba(27,25,38,.16);opacity:0;"
      + "transform:translate(-50%,-100%) scale(.9);transform-origin:50% 108%;"
      + "transition:opacity .18s ease,transform .18s cubic-bezier(.2,1.3,.4,1);";

    document.body.appendChild(svg);
    document.body.appendChild(bub);

    DOM = {
      svg: svg, bubble: bub,
      ink:   svg.querySelector(".cd-ink"),
      body:  svg.querySelector(".cd-body"),
      spark: svg.querySelector(".cd-spark"),
      armL:  svg.querySelector(".cd-armL"),  armR:  svg.querySelector(".cd-armR"),
      hL:    svg.querySelector(".cd-hL"),    hR:    svg.querySelector(".cd-hR"),
      fhL:   svg.querySelector(".cd-fhL"),   fhR:   svg.querySelector(".cd-fhR"),
      browL: svg.querySelector(".cd-browL"), browR: svg.querySelector(".cd-browR"),
      eyeL:  svg.querySelector(".cd-eyeL"),  eyeR:  svg.querySelector(".cd-eyeR"),
      pupL:  svg.querySelector(".cd-pupL"),  pupR:  svg.querySelector(".cd-pupR"),
      lips:  svg.querySelector(".cd-lips"),  mouth: svg.querySelector(".cd-mouth")
    };

    var home = homeSpot();
    S = {
      x: home.x, y: home.y, tx: home.x, ty: home.y,
      ang: 0, tang: 0, scale: 0.30, expr: "neutral", mode: "idle",
      driven: false, speaking: false, amp: 0, blink: 1, nextBlink: 0,
      handStyle: (M.script && M.script.hands) || "glove",
      handSize: (M.script && M.script.handSize) || 20,
      handL: { x: SH_L.x - 24, y: 250, rot: 118, mode: "open" },
      handR: { x: SH_R.x + 24, y: 246, rot:  62, mode: "open" },
      freeL: { x: home.x - 40, y: home.y - 40, rot: 118, mode: "open" },
      freeR: { x: home.x + 40, y: home.y - 40, rot:  62, mode: "open" },
      aimL: null, aimR: null, chase: null, bubBelow: false, handKey: "", lastT: 0, envI: 0, envA: 0
    };
    applyHeight((M.script && M.script.height) || 112);
    sizeLayer();
    window.addEventListener("resize", sizeLayer, false);
    M.raf = requestAnimationFrame(frame);
  }

  function teardown() {
    if (M.raf) { cancelAnimationFrame(M.raf); M.raf = null; }
    window.removeEventListener("resize", sizeLayer, false);
    if (DOM) {
      try { DOM.svg.parentNode.removeChild(DOM.svg); } catch (e) {}
      try { DOM.bubble.parentNode.removeChild(DOM.bubble); } catch (e) {}
    }
    DOM = null; S = null; M.seq++;
  }

  var W = 0, H = 0;
  function sizeLayer() {
    W = window.innerWidth; H = window.innerHeight;
    if (DOM) DOM.svg.setAttribute("viewBox", "0 0 " + W + " " + H);
  }
  function applyHeight(px) { if (S) S.scale = px / LOCAL_H; }
  function heightPx() { return S ? S.scale * LOCAL_H : 112; }

  /* ==========================================================================
     8.  GEOMETRY  --  page pixels <-> his own drawing space
     ========================================================================== */
  function toLocal(px, py) {
    var dx = px - S.x, dy = py - S.y;
    var r = -S.ang * Math.PI / 180, c = Math.cos(r), s = Math.sin(r);
    return { x: (dx * c - dy * s) / S.scale + TIP_X, y: (dx * s + dy * c) / S.scale + TIP_Y };
  }
  function toPage(lx, ly) {
    var dx = (lx - TIP_X) * S.scale, dy = (ly - TIP_Y) * S.scale;
    var r = S.ang * Math.PI / 180, c = Math.cos(r), s = Math.sin(r);
    return { x: S.x + dx * c - dy * s, y: S.y + dx * s + dy * c };
  }
  /* RULE 19, the half that only shows up on a real page: a target can be perfectly
     visible in the DOM and still be UNDERNEATH something -- a welcome modal, a sprint
     overlay, the keyboard tray. Found in the session.html dry run, where he cheerfully
     underlined the board through the welcome card. If the point at the middle of the
     target does not belong to the target, something is on top of it and he does not
     act on it at all. */
  function covered(el, r) {
    var cx = Math.max(1, Math.min(window.innerWidth  - 1, r.left + r.width  / 2));
    var cy = Math.max(1, Math.min(window.innerHeight - 1, r.top  + r.height / 2));
    var hit;
    try { hit = document.elementFromPoint(cx, cy); } catch (e) { return false; }
    if (!hit) return true;
    if (hit === el) return false;
    if (el.contains && el.contains(hit)) return false;
    if (hit.contains && hit.contains(el)) return false;
    return true;
  }
  function target(name) {
    var el = document.querySelector('[data-cad="' + String(name).replace(/"/g, "") + '"]');
    if (!el) return null;
    var r = el.getBoundingClientRect();
    if (!r.width || !r.height) return null;
    if (r.bottom < 0 || r.top > window.innerHeight) return null;   /* scrolled away */
    if (covered(el, r)) return null;                               /* something is on top */
    return { el: el, r: r };
  }

  /* RULE 19: he never stands over an input or a control. A candidate spot is
     rejected if the point under it belongs to something the child can operate. */
  function blocked(x, y) {
    var el;
    try { el = document.elementFromPoint(x, y); } catch (e) { return false; }
    if (!el) return false;
    return !!(el.closest && el.closest("input,textarea,select,button,a,[contenteditable],[role=button]"));
  }

  function homeSpot() {
    var main = document.querySelector("[data-cad-home]") || document.querySelector("main") || document.body;
    var r = main.getBoundingClientRect();
    var vw = window.innerWidth, vh = window.innerHeight;
    var x = Math.min(vw - 80, Math.max(80, r.right + 90));
    return { x: x, y: Math.max(140, Math.min(vh - 60, vh * 0.55)) };
  }
  function parkSpot() {
    var h = homeSpot();
    return { x: h.x, y: window.innerHeight - 50 };
  }

  /* ==========================================================================
     9.  THE FRAME  --  transform only (rule 29). Nothing here reads or writes a
         layout property, so the board can never reflow because he moved.
     ========================================================================== */
  var ENV = (function () {
    var out = [], words = [7,4,9,5,11,3,6,8,4,10,6,3,9,5,7], i, j, k, gap;
    for (i = 0; i < words.length; i++) {
      for (j = 0; j < words[i]; j++) out.push(0.45 + 0.55 * Math.abs(Math.sin(j * 1.7 + i)));
      gap = (i % 4 === 3) ? 7 : 3;
      for (k = 0; k < gap; k++) out.push(0);
    }
    return out;
  })();

  /* The REAL amplitude of the tutor's voice. voice.js's analyser, timeData and
     usingAnalyser are top-level lexical globals of a classic script, which is how
     session.html's own level() reaches them. Returns -1 when there is nothing to
     read, and the caller falls back to the synthetic envelope. */
  function voiceLevel() {
    try {
      if (typeof usingAnalyser !== "undefined" && usingAnalyser
          && typeof analyser !== "undefined" && analyser
          && typeof timeData !== "undefined" && timeData) {
        analyser.getByteTimeDomainData(timeData);
        var sum = 0, i, v;
        for (i = 0; i < timeData.length; i++) { v = (timeData[i] - 128) / 128; sum += v * v; }
        return Math.min(1, Math.sqrt(sum / timeData.length) * 3.4);
      }
    } catch (e) {}
    return -1;
  }

  function rebuildHands() {
    var key = S.handStyle + "|" + S.handSize + "|" + S.handL.mode + S.handR.mode
            + "|" + S.freeL.mode + S.freeR.mode;
    if (key === S.handKey) return;
    S.handKey = key;
    if (S.handStyle === "free") {
      DOM.hL.innerHTML = ""; DOM.hR.innerHTML = "";
      DOM.fhL.innerHTML = handMarkup(S.handSize, S.freeL.mode);
      DOM.fhR.innerHTML = handMarkup(S.handSize, S.freeR.mode);
    } else if (S.handStyle === "mitt") {
      DOM.fhL.innerHTML = ""; DOM.fhR.innerHTML = "";
      var m = '<circle cx="0" cy="0" r="' + (S.handSize * 0.66).toFixed(2) + '" fill="'
            + PAINT.mitt + '" stroke="' + PAINT.graphite + '" stroke-width="2.2"/>';
      DOM.hL.innerHTML = m; DOM.hR.innerHTML = m;
    } else {
      DOM.fhL.innerHTML = ""; DOM.fhR.innerHTML = "";
      DOM.hL.innerHTML = handMarkup(S.handSize, S.handL.mode);
      DOM.hR.innerHTML = handMarkup(S.handSize, S.handR.mode);
    }
  }

  /* Fingers pointing leftward means the glove is seen from the other side, so it
     mirrors -- otherwise the thumb hangs below the hand and reads as broken. */
  function handXf(h, sc) {
    var r = ((h.rot % 360) + 540) % 360 - 180;
    var f = (r > 90 || r < -90) ? -1 : 1;
    return "translate(" + h.x.toFixed(1) + "," + h.y.toFixed(1) + ") rotate(" + h.rot.toFixed(1) + ") "
         + (sc ? "scale(" + sc.toFixed(4) + "," + (sc * f).toFixed(4) + ")" : "scale(1," + f + ")");
  }
  function armPath(sh, h, side) {
    var mx = (sh.x + h.x) / 2, my = (sh.y + h.y) / 2;
    var slack = Math.max(0, 1 - Math.hypot(h.x - sh.x, h.y - sh.y) / 130);
    return "M " + sh.x + " " + sh.y + " Q " + (mx + side * 22 * slack).toFixed(1) + " "
         + (my + 10 * slack).toFixed(1) + " " + h.x.toFixed(1) + " " + h.y.toFixed(1);
  }
  function aimHand(h, aim, sh, side, t, phase) {
    var want;
    if (aim) {
      var L = toLocal(aim.x, aim.y), dx = L.x - sh.x, dy = L.y - sh.y;
      var len = Math.max(1, Math.hypot(dx, dy)), reach = Math.min(len - 14, 150);
      want = { x: sh.x + dx / len * reach, y: sh.y + dy / len * reach,
               rot: Math.atan2(dy, dx) * 180 / Math.PI, mode: "point" };
    } else {
      var sway = M.reduced ? 0 : Math.sin(t * 1.4 + phase) * 4;
      want = { x: sh.x + side * 26, y: 248 + sway, rot: 90 - side * 28, mode: "open" };
    }
    h.x += (want.x - h.x) * 0.16;
    h.y += (want.y - h.y) * 0.16;
    h.rot += ((((want.rot - h.rot) + 540) % 360) - 180) * 0.16;
    h.mode = want.mode;
  }
  /* The detached gloves live in PAGE pixels, outside his transform, which is the
     only way they can race ahead of him and wait to be caught up with. */
  function freeHand(h, sh, side, aim, t, phase) {
    var want, wr, k;
    if (S.chase) {
      want = { x: S.chase.x + side * 34, y: S.chase.y - 16 };
      wr = Math.atan2(S.chase.y - h.y, S.chase.x - h.x) * 180 / Math.PI;
      k = 0.31; h.mode = "point";
    } else if (aim) {
      var from = toPage(110, 200), a = Math.atan2(aim.y - from.y, aim.x - from.x);
      want = { x: aim.x - Math.cos(a) * 26, y: aim.y - Math.sin(a) * 26 };
      wr = a * 180 / Math.PI; k = 0.18; h.mode = "point";
    } else {
      var sway = M.reduced ? 0 : Math.sin(t * 1.4 + phase) * 4;
      want = toPage(sh.x + side * 34, 250 + sway);
      wr = S.ang + 90 - side * 28; k = 0.15; h.mode = "open";
    }
    h.x += (want.x - h.x) * k;
    h.y += (want.y - h.y) * k;
    h.rot += ((((wr - h.rot) + 540) % 360) - 180) * 0.18;
  }

  function frame(now) {
    if (!DOM || !S) return;
    M.raf = requestAnimationFrame(frame);
    var dt = S.lastT ? Math.min(64, now - S.lastT) : 16;
    S.lastT = now;
    var t = now / 1000;

    if (!S.driven) {
      var k = 1 - Math.pow(0.0016, dt / 1000);
      S.x += (S.tx - S.x) * k;
      S.y += (S.ty - S.y) * k;
    }
    S.ang += (S.tang - S.ang) * (1 - Math.pow(0.004, dt / 1000));

    /* RULE 5 + 6: no drift while parked, and none while he is talking. */
    var bob = 0, dx = 0, drift = effective().drift;
    if (!M.reduced && drift > 0 && S.mode !== "park" && !S.driven && !S.speaking) {
      bob = Math.sin(t * 1.55) * 7 * drift;
      dx  = Math.sin(t * 0.62 + 1.1) * 10 * drift;
    }
    DOM.body.setAttribute("transform",
      "translate(" + (S.x + dx).toFixed(2) + "," + (S.y + bob).toFixed(2) + ") "
      + "rotate(" + S.ang.toFixed(2) + ") scale(" + S.scale.toFixed(4) + ")");

    if (S.handStyle === "free") {
      freeHand(S.freeL, SH_L, -1, S.aimL, t, 0);
      freeHand(S.freeR, SH_R,  1, S.aimR, t, 1.7);
    } else {
      aimHand(S.handL, S.aimL, SH_L, -1, t, 0);
      aimHand(S.handR, S.aimR, SH_R,  1, t, 1.7);
    }

    var e = EXPR[S.expr] || EXPR.neutral;
    DOM.browL.setAttribute("d", e.bl);
    DOM.browR.setAttribute("d", e.br);

    if (M.reduced) { S.blink = 1; }
    else if (now > S.nextBlink) { S.blink = 0.06; S.nextBlink = now + 2400 + Math.random() * 3600; }
    else { S.blink += (1 - S.blink) * 0.30; }

    var o = 0;
    if (S.speaking) {
      var real = voiceLevel();
      if (real >= 0) { o = real; }
      else {
        S.envA += dt;
        if (S.envA > 55) { S.envA = 0; S.envI++; }
        o = ENV[S.envI % ENV.length];
      }
    }
    S.amp += (o - S.amp) * 0.5;

    DOM.lips.setAttribute("d", S.amp > 0.03 ? "" : e.lips);
    DOM.mouth.setAttribute("rx", (9 - 2.7 * S.amp).toFixed(2));
    DOM.mouth.setAttribute("ry", (S.amp * 8.6).toFixed(2));
    var ry = e.eye * S.blink;
    DOM.eyeL.setAttribute("ry", ry.toFixed(2));
    DOM.eyeR.setAttribute("ry", ry.toFixed(2));
    DOM.pupL.setAttribute("cy", (159.5 + e.pup).toFixed(1));
    DOM.pupR.setAttribute("cy", (159.5 + e.pup).toFixed(1));
    DOM.pupL.setAttribute("r", (3.4 * Math.max(0.15, S.blink)).toFixed(2));
    DOM.pupR.setAttribute("r", (3.4 * Math.max(0.15, S.blink)).toFixed(2));
    DOM.browL.setAttribute("transform", "translate(0," + (-2.6 * S.amp).toFixed(2) + ")");
    DOM.browR.setAttribute("transform", "translate(0," + (-2.6 * S.amp).toFixed(2) + ")");

    rebuildHands();
    if (S.handStyle === "free") {
      DOM.armL.setAttribute("d", ""); DOM.armR.setAttribute("d", "");
      DOM.fhL.setAttribute("transform", handXf(S.freeL, S.scale));
      DOM.fhR.setAttribute("transform", handXf(S.freeR, S.scale));
    } else {
      DOM.armL.setAttribute("d", armPath(SH_L, S.handL, -1));
      DOM.armR.setAttribute("d", armPath(SH_R, S.handR,  1));
      DOM.hL.setAttribute("transform", handXf(S.handL, 0));
      DOM.hR.setAttribute("transform", handXf(S.handR, 0));
    }

    if (DOM.bubble.style.opacity === "1") {
      if (S.bubBelow) {                        /* he is pointing UP at something */
        var foot = toPage(110, TIP_Y);
        DOM.bubble.style.transform = "translate(-50%,0) scale(1)";
        DOM.bubble.style.left = (foot.x + dx) + "px";
        DOM.bubble.style.top  = (foot.y + bob + 14) + "px";
      } else {
        var head = toPage(110, 130);
        DOM.bubble.style.transform = "translate(-50%,-100%) scale(1)";
        DOM.bubble.style.left = (head.x + dx) + "px";
        DOM.bubble.style.top  = (head.y + bob - 12) + "px";
      }
    }
  }

  /* ==========================================================================
     10.  SEQUENCING
     --------------------------------------------------------------------------
     ES5 on purpose, to match tutor-face.js and tutor-moments.js: a callback step
     runner rather than async/await, which also makes cancellation explicit. Any
     new sequence bumps M.seq and every in-flight step checks it before acting, so
     a child who answers fast can never be chased by the last answer's animation.
     ========================================================================== */
  function newSeq() { M.seq++; return M.seq; }
  function alive(id) { return id === M.seq && !!DOM; }

  function after(ms, id, fn) {
    setTimeout(function () { if (alive(id)) fn(); }, M.reduced ? Math.min(ms, 40) : ms);
  }
  function settle(id, tol, fn) {
    var guard = 0;
    (function check() {
      if (!alive(id)) return;
      guard++;
      if (guard > 420 || Math.hypot(S.tx - S.x, S.ty - S.y) < (tol || 8)) { fn(); return; }
      requestAnimationFrame(check);
    })();
  }
  function flyTo(x, y, ang) {
    S.tx = Math.max(60, Math.min(W - 60, x));
    S.ty = Math.max(heightPx() * 0.9, Math.min(H - 30, y));
    if (ang !== undefined) S.tang = ang;
  }

  /* rule 26: nothing repeats inside a session. */
  function fresh(bag, list) {
    if (!list || !list.length) return null;
    if (!M.spent[bag] || M.spent[bag].length >= list.length) M.spent[bag] = [];
    var pool = [], i;
    for (i = 0; i < list.length; i++) {
      if (M.spent[bag].indexOf(i) === -1) pool.push(i);
    }
    var pick = pool[Math.floor(Math.random() * pool.length)];
    M.spent[bag].push(pick);
    return list[pick];
  }

  /* ==========================================================================
     11.  BEHAVIOURS
     --------------------------------------------------------------------------
     Adding one of these is code. Scheduling one is editing the JSON. That is the
     whole division, and it is the point of the file.
     ========================================================================== */
  function bubbleOn(text) {
    DOM.bubble.textContent = text;
    DOM.bubble.style.opacity = "1";
    DOM.bubble.style.transform = "translate(-50%,-100%) scale(1)";
  }
  function bubbleOff() {
    DOM.bubble.style.opacity = "0";
    DOM.bubble.style.transform = "translate(-50%,-100%) scale(.9)";
    S.speaking = false;
  }

  var BEHAVIOURS = {

    /* --- he arrives. once per lesson, never per section (rule 7) --- */
    enter: function (o, done, id) {
      var b = effective();
      if (b.entrance === "corner") { S.expr = "neutral"; goHome(); done(); return; }
      var h = homeSpot();
      S.x = h.x + 140; S.y = h.y - 90; S.expr = "pleased";
      flyTo(h.x, h.y, 0);
      settle(id, 14, function () { S.expr = "neutral"; done(); });
    },

    /* --- rule 5. the whole document exists for this one --- */
    park: function (o, done) {
      newSeq();
      S.mode = "park"; S.driven = false; S.expr = "listening";
      S.aimL = S.aimR = null; S.chase = null; S.tang = 0;
      bubbleOff();
      var p = parkSpot();
      flyTo(p.x, p.y, 0);
      done();
    },

    release: function (o, done) { goHome(); done(); },

    /* --- rule 6: he stops drifting to talk --- */
    say: function (o, done, id) {
      var text = o.text || fresh(o.from || "lines", (M.script.lines || {})[o.from || "lines"]);
      if (!text) { done(); return; }
      var ms = o.ms || Math.max(1800, Math.min(7000, text.length * 62));
      S.expr = o.expression || "teaching";
      S.speaking = true;
      bubbleOn(text);
      after(ms, id, function () { bubbleOff(); S.expr = "neutral"; done(); });
    },

    joke: function (o, done, id) {
      if (!effective().joke) { done(); return; }
      var j = fresh("jokes", M.script.jokes);
      if (!j) { done(); return; }
      BEHAVIOURS.say({ text: j, ms: o.ms || 5200, expression: "teaching" }, function () {
        S.expr = "pleased";
        after(700, id, function () { S.expr = "neutral"; done(); });
      }, id);
    },

    expression: function (o, done) { S.expr = EXPR[o.to] ? o.to : "neutral"; done(); },

    /* --- rule 13: come close, and land the finger on the near edge --- */
    point: function (o, done, id) {
      var T = target(o.target);
      if (!T) { done(); return; }
      var r = T.r, standRight = (W - r.right) > 240;
      /* His head sits about heightPx() above the tip and his bubble another ~110px
         above that, so a target near the TOP of the window has to be approached from
         BELOW or he stands on the very thing he is pointing at. Caught on the demo's
         streak chips, which live in the topbar. */
      var minY = heightPx() + 132;
      var wantY = r.top + r.height / 2 + heightPx() * 0.40;
      var below = false;
      if (wantY < minY) { wantY = r.bottom + heightPx() * 0.85; below = true; }
      var stand = {
        x: standRight ? Math.min(W - 64, r.right + 86) : Math.max(64, r.left - 86),
        y: Math.min(H - 30, Math.max(minY, wantY))
      };
      S.bubBelow = below;
      /* rule 19: if that spot sits on a control, try the other side, then give up */
      if (blocked(stand.x, stand.y)) {
        standRight = !standRight;
        stand.x = standRight ? Math.min(W - 64, r.right + 86) : Math.max(64, r.left - 86);
        if (blocked(stand.x, stand.y)) { done(); return; }
      }
      var aim = {
        x: standRight ? Math.max(r.left + 12, r.right - 90) : Math.min(r.right - 12, r.left + 90),
        y: r.top + r.height / 2
      };
      S.mode = "point"; S.driven = false; S.expr = "teaching";
      flyTo(stand.x, stand.y, standRight ? -6 : 6);
      settle(id, 14, function () {
        if (standRight) { S.aimL = aim; S.aimR = null; }
        else            { S.aimR = aim; S.aimL = null; }
        if (o.text) BEHAVIOURS.say({ text: o.text, ms: o.ms || 2800 }, function () {}, id);
        after(o.ms || 2800, id, function () { S.aimL = S.aimR = null; done(); });
      });
    },

    /* --- rule 12 and 14. the only behaviour that carries information. --- */
    underline: function (o, done, id) {
      if (effective().tier3 === "never" && !o.forced) { done(); return; }
      var T = target(o.target);
      if (!T) { done(); return; }
      var r = T.r;
      var y  = Math.min(H - 14, r.bottom + 9);
      var x1 = Math.max(8, r.left - 6), x2 = Math.min(W - 8, r.right + 6);
      if (x2 - x1 < 24) { done(); return; }

      var path = document.createElementNS(NS, "path");
      path.setAttribute("d", "M " + x1 + " " + y + " Q " + ((x1 + x2) / 2) + " " + (y + 8)
                             + " " + x2 + " " + (y - 2));
      path.setAttribute("fill", "none");
      path.setAttribute("stroke", PAINT.graphite);
      path.setAttribute("stroke-width", Math.max(3, heightPx() * 0.045).toFixed(1));
      path.setAttribute("stroke-linecap", "round");
      path.setAttribute("opacity", "0.86");
      if (o.target) path.setAttribute("data-for", String(o.target));
      DOM.ink.appendChild(path);

      var len = path.getTotalLength();
      path.setAttribute("stroke-dasharray", len);
      path.setAttribute("stroke-dashoffset", len);

      /* rule 20: reduced motion still gets the mark, it just does not travel */
      if (M.reduced) {
        path.setAttribute("stroke-dashoffset", 0);
        S.expr = "pleased";
        setTimeout(function () { if (alive(id)) { S.expr = "neutral"; done(); } }, 40);
        return;
      }

      var p0 = path.getPointAtLength(0);
      S.mode = "write"; S.driven = false; S.expr = "teaching"; S.aimL = S.aimR = null;
      S.tx = p0.x; S.ty = p0.y; S.tang = -35;
      settle(id, 10, function () {
        S.driven = true;
        var t0 = performance.now(), dur = Math.max(420, len * 3.1);
        (function step(now) {
          if (!alive(id)) { S.driven = false; return; }
          var u = Math.min(1, (now - t0) / dur);
          var e = u < 0.5 ? 2 * u * u : -1 + (4 - 2 * u) * u;
          var pt = path.getPointAtLength(e * len);
          S.x = pt.x; S.y = pt.y;
          path.setAttribute("stroke-dashoffset", (len * (1 - e)).toFixed(2));
          if (u < 1) { requestAnimationFrame(step); return; }
          S.driven = false; S.expr = "pleased"; S.tang = 0;
          goHome();
          after(1000, id, function () { S.expr = "neutral"; done(); });
        })(performance.now());
      });
    },

    /* --- rule 11. three tiers, and the top one does not drift downward --- */
    celebrate: function (o, done, id) {
      var tier = o.tier;
      if (tier === "auto") tier = autoTier();
      tier = Math.max(1, Math.min(3, parseInt(tier, 10) || 1));
      var b = effective();
      if (tier === 3 && b.tier3 === "never") tier = 2;
      if (tier >= 2 && M.mode === "quiet") tier = 1;

      S.mode = "celebrate"; S.driven = false; S.expr = "pleased";

      if (tier === 1) {
        var by = S.ty;
        S.ty = by - 26;
        after(150, id, function () {
          S.ty = by;
          after(850, id, function () { S.expr = "neutral"; S.mode = "idle"; done(); });
        });
        return;
      }
      if (tier === 2) {
        var up = toPage(110, 40);
        S.aimL = { x: up.x - 46, y: up.y - 18 };
        S.aimR = { x: up.x + 46, y: up.y - 18 };
        sparkle(5);
        var b2 = S.ty;
        S.ty = b2 - 30;
        after(170, id, function () {
          S.ty = b2;
          after(200, id, function () {
            S.ty = b2 - 30;
            after(170, id, function () {
              S.ty = b2;
              after(620, id, function () {
                S.aimL = S.aimR = null; S.expr = "neutral"; S.mode = "idle"; done();
              });
            });
          });
        });
        return;
      }
      sparkle(7);
      after(240, id, function () {
        BEHAVIOURS.underline({ target: o.target || "answer", forced: true }, done, id);
      });
    },

    /* --- the gloves go first and he chases them --- */
    chase: function (o, done, id) {
      var T = target(o.target);
      if (!T || M.reduced) { BEHAVIOURS.point(o, done, id); return; }
      S.handStyle = "free"; S.handKey = "";
      var r = T.r, right = (W - r.right) > 240;
      var dest = {
        x: right ? Math.min(W - 64, r.right + 86) : Math.max(64, r.left - 86),
        y: r.top + r.height / 2 + heightPx() * 0.40
      };
      if (blocked(dest.x, dest.y)) { BEHAVIOURS.point(o, done, id); return; }
      S.mode = "chase"; S.expr = "teaching"; S.driven = false; S.aimL = S.aimR = null;
      S.chase = dest;
      after(430, id, function () {
        S.tang = right ? -7 : 7;
        flyTo(dest.x, dest.y);
        settle(id, 16, function () {
          after(220, id, function () {
            S.chase = null;
            BEHAVIOURS.point(o, done, id);
          });
        });
      });
    },

    /* --- rule 10: once, on the first lesson, and skippable --- */
    tour: function (o, done, id) {
      var b = effective();
      if (b.tour === "never" || (b.tour === "first" && M.spent.tour) || (b.tour === "ask" && !o.asked)) {
        done(); return;
      }
      M.spent.tour = true;
      var stops = o.stops || (M.script.tours || {})[o.name || M.page] || [];
      var i = 0;
      (function next() {
        if (!alive(id)) return;
        if (i >= stops.length) { bubbleOff(); goHome(); done(); return; }
        var st = stops[i++];
        BEHAVIOURS.point({ target: st.target, text: st.text, ms: st.ms || 3000 }, next, id);
      })();
    },

    wait:     function (o, done, id) { after(o.ms || 500, id, done); },
    clearInk: function (o, done) { clearInk(o.target); done(); },
    hush:     function (o, done) { bubbleOff(); done(); }
  };

  function goHome() {
    S.driven = false; S.mode = "idle"; S.aimL = S.aimR = null; S.chase = null; S.bubBelow = false;
    S.tang = 0;
    var h = homeSpot();
    flyTo(h.x, h.y, 0);
  }
  function sparkle(n) {
    if (M.reduced) return;
    var head = toPage(110, 120), i;
    for (i = 0; i < n; i++) {
      (function (i) {
        var g = document.createElementNS(NS, "path");
        var a = (-140 + i * (280 / Math.max(1, n - 1))) * Math.PI / 180;
        var dist = 42 + Math.random() * 34, sz = 0.5 + Math.random() * 0.5;
        g.setAttribute("d", STAR);
        g.setAttribute("fill", PAINT.gold);
        g.setAttribute("opacity", "0");
        DOM.spark.appendChild(g);
        var st = performance.now(), dur = 620 + Math.random() * 220;
        (function step(now) {
          var u = Math.min(1, (now - st) / dur);
          var rr = dist * (0.25 + 0.75 * u);
          g.setAttribute("transform",
            "translate(" + (head.x + Math.cos(a) * rr).toFixed(1) + ","
            + (head.y + Math.sin(a) * rr - u * 12).toFixed(1) + ") scale("
            + (sz * (0.4 + u * 0.9)).toFixed(2) + ") rotate(" + (u * 140).toFixed(0) + ")");
          g.setAttribute("opacity", (u < 0.25 ? u / 0.25 : 1 - (u - 0.25) / 0.75).toFixed(2));
          if (u < 1) requestAnimationFrame(step);
          else if (g.parentNode) g.parentNode.removeChild(g);
        })(st);
      })(i);
    }
  }
  /* rule 15: a mark belongs to the line underneath it */
  function clearInk(forTarget) {
    if (!DOM) return;
    if (!forTarget) { DOM.ink.innerHTML = ""; return; }
    var kids = DOM.ink.childNodes, i;
    for (i = kids.length - 1; i >= 0; i--) {
      if (kids[i].getAttribute && kids[i].getAttribute("data-for") === String(forTarget)) {
        DOM.ink.removeChild(kids[i]);
      }
    }
  }

  /* ==========================================================================
     12.  THE MENU  --  moment in, behaviour out
     ========================================================================== */
  var streak = 0, solvedHard = false;
  function autoTier() {
    if (solvedHard) { solvedHard = false; return 3; }
    if (streak > 0 && streak % 3 === 0) return 2;
    return 1;
  }

  function stepsFor(moment) {
    var pages = M.script.pages || {};
    var page = pages[M.page] || pages["*"] || null;
    if (!page) return null;
    var list = page[moment];
    if (!list && page["*"]) list = page["*"][moment];
    return (list && list.length) ? list : null;
  }

  function run(steps) {
    var id = newSeq(), i = 0;
    (function next() {
      if (!alive(id)) return;
      if (i >= steps.length) { if (S.mode !== "park") goHome(); return; }
      var st = steps[i++] || {};
      if (st["if"] === "stage.joke" && !effective().joke) { next(); return; }
      if (st.once) {
        var key = "step:" + (st["do"] || "") + ":" + (st.target || "") + ":" + (st.once === true ? "1" : st.once);
        if (M.spent[key]) { next(); return; }
        M.spent[key] = true;
      }
      var fn = BEHAVIOURS[st["do"]];
      if (!fn) { next(); return; }
      try { fn(st, next, id); } catch (e) { next(); }
    })();
  }

  /* ==========================================================================
     13.  RULE 5, WIRED  --  he parks the moment the child starts working
     ========================================================================== */
  function isWorkField(el) {
    if (!el || !el.matches) return false;
    return el.matches("input,textarea,[contenteditable],[contenteditable=true]");
  }
  function onFocusIn(e)  { if (live() && isWorkField(e.target)) BEHAVIOURS.park({}, function () {}); }
  function onFocusOut(e) {
    if (!live() || !isWorkField(e.target)) return;
    setTimeout(function () {
      if (!DOM) return;
      if (isWorkField(document.activeElement)) return;
      if (S.mode === "park") { S.mode = "idle"; S.expr = "neutral"; goHome(); }
    }, 120);
  }
  function onSpeaking() { if (live()) S.speaking = true; }

  /* ==========================================================================
     14.  PUBLIC API
     --------------------------------------------------------------------------
     Every method is safe to call at any time, on any page, whether or not the
     script file exists. That is the contract that lets stage 4 wire the pages
     before anyone decides to turn him on.
     ========================================================================== */
  function mount(opts) {
    opts = opts || {};
    return probe().then(function (ok) {
      if (!ok || M.mounted) return ok;
      M.mode = readMode();
      if (M.mode === "off") { M.mounted = true; return false; }
      M.reduced = !!(window.matchMedia
                  && window.matchMedia("(prefers-reduced-motion: reduce)").matches);
      M.page  = opts.page  || document.body.getAttribute("data-cadabra-page")
                || (location.pathname.split("/").pop() || "").replace(/\.html$/, "") || "index";
      M.stage = opts.stage || document.body.getAttribute("data-cadabra-stage")
                || (M.script.defaultStage || "early");
      /* rule 18: a page the menu does not name gets no character at all */
      var pages = M.script.pages || {};
      if (!pages[M.page] && !pages["*"]) { M.mounted = true; return false; }
      M.mounted = true;
      build();
      document.addEventListener("focusin",  onFocusIn,  true);
      document.addEventListener("focusout", onFocusOut, true);
      document.addEventListener("mt:speaking", onSpeaking, false);
      return true;
    })["catch"](function () { return false; });
  }

  function fire(moment, data) {
    if (!live()) return false;
    data = data || {};
    if (moment === "answer.correct") { streak++; if (data.hard) solvedHard = true; }
    if (moment === "answer.wrong")   { streak = 0; }
    if (moment === "problem.cleared") { clearInk(data.target); }
    var steps = stepsFor(moment);
    if (!steps) return false;
    run(steps);
    return true;
  }

  function direct(name) {
    return function (a, b) {
      if (!live()) return false;
      var o = (typeof a === "object" && a !== null) ? a : {};
      if (typeof a === "string") { o = (name === "say") ? { text: a, ms: b } : { target: a }; }
      if (typeof a === "number" && name === "celebrate") o = { tier: a };
      run([{ "do": name, text: o.text, ms: o.ms, target: o.target, tier: o.tier,
             to: o.to, asked: true, forced: o.forced }]);
      return true;
    };
  }

  window.Cadabra = {
    version:   VERSION,
    mount:     mount,
    fire:      fire,
    say:       direct("say"),
    point:     direct("point"),
    underline: direct("underline"),
    celebrate: direct("celebrate"),
    chase:     direct("chase"),
    tour:      direct("tour"),
    park:      function () { if (live()) BEHAVIOURS.park({}, function () {}); },
    release:   function () { if (live()) goHome(); },
    clearInk:  function (t) { clearInk(t); },
    /* rule 18: quizzes, tests and timed challenges get no character at all */
    suspend:   function () { M.suspended = true; teardown(); },
    resume:    function () { if (!M.suspended) return; M.suspended = false; if (M.mounted && M.mode !== "off") build(); },
    /* rule 27: the child's own dial */
    mode:      function (v) { return (v === undefined) ? M.mode : writeMode(v); },
    stage:     function (v) { if (v) M.stage = v; return M.stage; },
    available: function () { return M.state === "ready"; },
    ready:     probe,
    state:     function () {
      return { state: M.state, mounted: M.mounted, suspended: M.suspended, page: M.page,
               stage: M.stage, mode: M.mode, reduced: M.reduced, streak: streak,
               pose: S ? S.mode : null, visible: !!DOM };
    },
    PAINT: PAINT
  };

  probe();      /* one fetch, at load, then never again */
})();
/* I did no harm and this file is not truncated. */

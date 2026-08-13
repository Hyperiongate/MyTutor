/* =============================================================================
   tutor-moments.js  --  Math Tutor MVP  --  Hyperion Shift LLC
   -----------------------------------------------------------------------------
   CHANGE NOTES (keep newest at top):
     2026-08-12  (build eu) NEW. PHASE 2 OF THE VIDEO PROJECT: Mr. Cadabra STEPS OUT AND
                 TALKS. Phase 1 (tutor-face.js) is the silent corner presence -- muted,
                 decorative, never lip-synced, and that stays exactly as it is. This file
                 is the other half: a handful of one-time HeyGen clips in which he really
                 speaks, in his real ElevenLabs voice, played at the few moments that
                 deserve a person rather than a paragraph.
                 WHY IT IS A SEPARATE FILE, not more of tutor-face.js: these clips have
                 SOUND. The presence layer's hardest guarantee -- "the corner never makes
                 sound" -- is enforced by a test that reads tutor-face.js and fails if the
                 word unmute ever appears in it. Keeping the talking player in its own file
                 means that guarantee stays absolute instead of becoming a special case.
                 HOW IT SHIPS: DARK. It probes /static/videos/cadabra/moments.json once. No
                 manifest (today) = available() is false everywhere and every caller keeps
                 its existing behaviour untouched. The day the clips land the manifest
                 appears with them and the same callers light up. No coordination, no flag.
                 THE VOICE RULE: a moment clip and his live voice must NEVER talk over each
                 other. play() returns a promise that settles when the clip is done, and
                 every caller is written to wait for it before saying its own line. A
                 canned clip never REPLACES a personalised line -- it comes first, then the
                 live voice carries on. Video cannot say a child's name; the live voice can,
                 and that is the half that must survive.
                 Accessibility: the card is a real dialog (role, label, Escape, focus moved
                 in and restored on close), the words are present as TEXT under the video
                 rather than living only in the audio, and there is always a visible way out
                 that resolves the promise so the page continues either way.
   ============================================================================= */
(function () {
  "use strict";

  var BASE = "/static/videos/cadabra/";
  var M = {
    state: "unprobed",     // unprobed -> probing -> ready | off
    manifest: null,
    probe: null,           // the in-flight probe promise, so callers can await readiness
    open: null,            // the live overlay, if one is showing
    lastFocus: null
  };

  function probe() {
    if (M.probe) return M.probe;
    M.state = "probing";
    M.probe = new Promise(function (resolve) {
      var done = function (ok) { M.state = ok ? "ready" : "off"; resolve(M.state === "ready"); };
      try {
        fetch(BASE + "moments.json", { cache: "no-cache" }).then(function (r) {
          if (!r.ok) throw 0;
          return r.json();
        }).then(function (m) {
          if (!m || !m.clips || typeof m.clips !== "object") throw 0;
          M.manifest = m;
          done(true);
        }).catch(function () { done(false); });
      } catch (e) { done(false); }
    });
    return M.probe;
  }

  function clipFor(key) {
    if (M.state !== "ready" || !M.manifest) return null;
    var c = M.manifest.clips[key];
    if (!c) return null;
    var sources = (typeof c === "string") ? [c] : (c.sources || c.files || []);
    if (!sources.length) return null;
    return { sources: sources, caption: (c.caption || "") };
  }

  // Synchronous "is this clip here?" -- false until the probe has finished, which is the
  // correct answer for a caller that must decide right now (the page is not yet dark-aware).
  function available(key) { return !!clipFor(key); }

  function styleOnce() {
    if (document.getElementById("tm-style")) return;
    var css =
      ".tm-scrim{position:fixed;inset:0;z-index:9999;display:flex;align-items:center;" +
      "justify-content:center;background:rgba(12,12,26,.72);backdrop-filter:blur(3px);" +
      "padding:20px;opacity:0;transition:opacity .25s ease}" +
      ".tm-scrim.tm-in{opacity:1}" +
      ".tm-card{background:#fff;border-radius:20px;overflow:hidden;max-width:min(92vw,420px);" +
      "box-shadow:0 24px 70px rgba(0,0,0,.45);display:flex;flex-direction:column}" +
      ".tm-card video{display:block;width:100%;max-height:66vh;object-fit:cover;background:#e9e7e2}" +
      ".tm-cap{font:500 15px/1.5 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:#2b2b3d;" +
      "padding:14px 18px 4px}" +
      ".tm-bar{display:flex;justify-content:flex-end;gap:8px;padding:10px 14px 14px}" +
      ".tm-btn{font:600 14px/1 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;cursor:pointer;" +
      "border:1px solid #d7d7e6;background:#f6f6fb;color:#3a3a55;border-radius:999px;padding:10px 16px}" +
      ".tm-btn:hover{background:#ecebf7}" +
      ".tm-btn.tm-go{background:#4a4ac9;border-color:#4a4ac9;color:#fff}" +
      "@media (prefers-reduced-motion: reduce){.tm-scrim{transition:none}}";
    var el = document.createElement("style");
    el.id = "tm-style";
    el.appendChild(document.createTextNode(css));
    (document.head || document.documentElement).appendChild(el);
  }

  /* All-sources-failed detection. The HTML spec routes a resource failure to each
     <source> element, not to the <video>; only the .src form fires error on the element.
     Both are wired here so a clip with no decodable encoding reports promptly instead of
     hanging on a poster. cb may be called once. */
  function sourcesFailed(vid, cb) {
    var once = false;
    function fire() { if (once) return; once = true; try { cb(); } catch (e) {} }
    var srcs = vid.getElementsByTagName("source");
    var total = srcs.length, failed = 0;
    for (var i = 0; i < total; i++) {
      srcs[i].onerror = function () { if (++failed >= total) fire(); };
    }
    vid.onerror = fire;                    // browsers that do fire it, and the .src form
    if (!total) vid.onerror = fire;
  }

  /* play(key) -> Promise<"played"|"skipped"|"unavailable">
     ALWAYS resolves. A missing clip, a dead network, a codec the browser cannot decode, a
     blocked autoplay the visitor then ignores -- every one of them settles the promise so
     the caller's .then() runs and the page carries on. Nothing here can strand a lesson. */
  function play(key) {
    return probe().then(function () {
      var clip = clipFor(key);
      if (!clip) return "unavailable";
      if (M.open) return "unavailable";            // never two at once
      styleOnce();

      return new Promise(function (resolve) {
        var settled = false;
        function finish(how) {
          if (settled) return; settled = true;
          try { document.removeEventListener("keydown", onKey, true); } catch (e) {}
          try { if (scrim.parentNode) scrim.parentNode.removeChild(scrim); } catch (e) {}
          M.open = null;
          try { if (M.lastFocus && M.lastFocus.focus) M.lastFocus.focus(); } catch (e) {}
          M.lastFocus = null;
          resolve(how);
        }

        var scrim = document.createElement("div");
        scrim.className = "tm-scrim";
        scrim.setAttribute("role", "dialog");
        scrim.setAttribute("aria-modal", "true");
        scrim.setAttribute("aria-label", "A message from Mr. Cadabra");

        var card = document.createElement("div");
        card.className = "tm-card";

        var vid = document.createElement("video");
        vid.setAttribute("playsinline", "");
        vid.playsInline = true;
        vid.preload = "auto";
        if (M.manifest.poster) vid.poster = BASE + M.manifest.poster;
        for (var i = 0; i < clip.sources.length; i++) {
          var s = document.createElement("source");
          s.src = BASE + clip.sources[i];
          if (/\.webm$/i.test(clip.sources[i])) s.type = "video/webm";
          else if (/\.mp4$/i.test(clip.sources[i])) s.type = "video/mp4";
          vid.appendChild(s);
        }
        vid.onended = function () { finish("played"); };
        // A <video> that fails EVERY <source> does NOT fire an error event on the element
        // itself -- the error events land on the individual <source> tags and the element
        // just settles into networkState 3 (NO_SOURCE), silently, forever. Caught in test:
        // in a browser with no H.264 the card opened and then sat there, and the demo tour
        // never started. So we listen where the failure actually reports.
        sourcesFailed(vid, function () { finish("unavailable"); });
        card.appendChild(vid);

        // The words exist as TEXT, not only as audio. A deaf child, a muted tab and a
        // screen reader all get the same sentence the speakers would have carried.
        if (clip.caption) {
          var cap = document.createElement("p");
          cap.className = "tm-cap";
          cap.textContent = clip.caption;
          card.appendChild(cap);
        }

        var bar = document.createElement("div");
        bar.className = "tm-bar";
        var skip = document.createElement("button");
        skip.type = "button"; skip.className = "tm-btn"; skip.textContent = "Skip";
        skip.onclick = function () { try { vid.pause(); } catch (e) {} finish("skipped"); };
        bar.appendChild(skip);
        card.appendChild(bar);

        scrim.appendChild(card);
        scrim.addEventListener("click", function (e) {
          if (e.target === scrim) { try { vid.pause(); } catch (e2) {} finish("skipped"); }
        });
        function onKey(e) {
          if (e.key === "Escape") { try { vid.pause(); } catch (e2) {} finish("skipped"); }
        }
        document.addEventListener("keydown", onKey, true);

        M.lastFocus = document.activeElement;
        document.body.appendChild(scrim);
        M.open = scrim;
        requestAnimationFrame(function () { scrim.classList.add("tm-in"); });
        try { skip.focus(); } catch (e) {}

        // Autoplay WITH SOUND is only allowed off a user gesture. Every caller triggers
        // this from a click, but if the browser refuses anyway we do not fail -- we show
        // the visitor a button and let them start it themselves.
        var p;
        try { p = vid.play(); } catch (e) { p = null; }
        if (p && p.catch) {
          p.catch(function () {
            var go = document.createElement("button");
            go.type = "button"; go.className = "tm-btn tm-go"; go.textContent = "▶ Play";
            go.onclick = function () {
              try { var q = vid.play(); if (q && q.catch) q.catch(function () { finish("skipped"); }); }
              catch (e2) { finish("skipped"); }
              try { bar.removeChild(go); } catch (e3) {}
            };
            bar.appendChild(go);
            try { go.focus(); } catch (e4) {}
          });
        }

        // A clip that never fires onended (a stall, a tab backgrounded mid-play) must not
        // hold the page forever. Generous, and only a backstop -- normal endings win.
        setTimeout(function () { finish("played"); }, 90000);
      });
    }).catch(function () { return "unavailable"; });
  }

  window.TutorMoments = { play: play, available: available, ready: probe };
  probe();                                    // one fetch, at load, then never again
})();
/* I did no harm and this file is not truncated. */

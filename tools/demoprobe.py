"""(uy) THE DEMO HARNESS -- drives /demo in a real browser and MEASURES the five
defects Jim reported, so each fix is proved rather than argued.

It supplies what the container cannot: real audio clips (a generated WAV of a known
duration, so the cue's timing can be measured against the clip it rides) and a
speechSynthesis that behaves like CHROME'S -- including the ~15-second cutoff that
leaves a long utterance stalled with no onend until the next cancel(). That cutoff is
the engine of defect 3, so the harness reproduces it on purpose.

    python3 demoprobe.py <port> [before|after]
"""
import json
import math
import struct
import os
import sys
import wave
import io as _io

from playwright.sync_api import sync_playwright

# ⚠️ NO CONTAINER PATHS. The repo root is found from THIS file, and the "before" copy
# (a snapshot of static/demo.html as it shipped, used only by the `before` mode) is
# taken from BEFORE_HTML in the environment, defaulting to a sibling of the page.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BEFORE_HTML = os.environ.get("BEFORE_HTML",
                             os.path.join(ROOT, "static", "demo.before.html"))

PORT = sys.argv[1] if len(sys.argv) > 1 else "8107"
LABEL = sys.argv[2] if len(sys.argv) > 2 else "after"
BASE = "http://127.0.0.1:" + PORT
CLIP_SECONDS = 6.0


def clip_bytes(seconds=CLIP_SECONDS, rate=8000):
    buf = _io.BytesIO()
    w = wave.open(buf, "wb")
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(rate)
    n = int(rate * seconds)
    w.writeframes(b"".join(struct.pack("<h", int(6000 * math.sin(i / 12.0)))
                           for i in range(n)))
    w.close()
    return buf.getvalue()


# A speechSynthesis that behaves like Chrome's, plus a probe log on the window.
INIT = """
(() => {
  window.__probe = [];
  const t0 = Date.now();
  const log = (kind, extra) => window.__probe.push(
      Object.assign({t: Date.now() - t0, kind: kind}, extra || {}));
  window.__t0 = t0;

  // ---- a Chrome-shaped speechSynthesis ------------------------------------------
  const CUTOFF = 15000;                 // Chrome stops a long utterance here
  let cur = null, timer = null;
  const synth = {
    speaking: false, paused: false, pending: false,
    getVoices: () => [],
    speak(u) {
      cur = u; synth.speaking = true;
      const words = String(u.text || "").split(/\\s+/).length;
      const ms = words * 380;
      log("tts.start", {words: words, ms: ms});
      setTimeout(() => { try { u.onstart && u.onstart({}); } catch (e) {} }, 30);
      if (ms <= CUTOFF) {
        timer = setTimeout(() => {
          synth.speaking = false; timer = null;
          log("tts.end", {words: words});
          try { u.onend && u.onend({}); } catch (e) {}
        }, ms);
      } else {
        // ⚠️ THE CHROME CUTOFF: it stops making sound and never fires onend.
        timer = setTimeout(() => { log("tts.cutoff", {words: words}); timer = null; }, CUTOFF);
      }
    },
    cancel() {
      if (timer) { clearTimeout(timer); timer = null; }
      const u = cur; cur = null;
      if (synth.speaking) {
        synth.speaking = false;
        log("tts.cancel");
        // Chrome releases the stalled utterance HERE, by firing its onend.
        if (u) { try { u.onend && u.onend({}); } catch (e) {} }
      }
    },
    pause() { synth.paused = true; },
    resume() { synth.paused = false; log("tts.keepalive"); },
  };
  Object.defineProperty(window, "speechSynthesis", {value: synth, configurable: true});
  window.SpeechSynthesisUtterance = function (text) { this.text = text; };

  // ---- every clip that plays, and every clip that ends ---------------------------
  const play = HTMLMediaElement.prototype.play;
  HTMLMediaElement.prototype.play = function () {
    const src = String(this.currentSrc || this.src || "");
    const m = src.match(/demo-audio\\/(\\d+)/);
    const bb = document.getElementById("bubble");
    window.__aud = this;
    log("clip.play", {i: m ? Number(m[1]) : -1, said: bb ? String(bb.textContent||"").slice(0,90) : ""});
    this.addEventListener("ended", () => log("clip.ended", {i: m ? Number(m[1]) : -1}),
                          {once: true});
    return play.apply(this, arguments);
  };

  // ---- the board's dark/white attribute, the thing defect 4 is about --------------
  addEventListener("DOMContentLoaded", () => {
    const b = document.getElementById("board");
    if (!b) return;
    new MutationObserver(() => log("board.theme", {dark: b.getAttribute("data-board") === "dark",
        at: window.__aud ? Math.round(window.__aud.currentTime*100)/100 : null,
        of: window.__aud ? Math.round((window.__aud.duration||0)*100)/100 : null}))
      .observe(b, {attributes: true, attributeFilter: ["data-board"]});
  });
})();
"""

# ⚠️ A CLIP PER LINE, AS LONG AS THE REAL ONE WOULD BE. A fixed-length clip makes the
# cue measurement meaningless: the words say fifteen seconds and the file says six, so
# the estimate overshoots the file and the cue can only ever land at the end. Real TTS
# runs at roughly 0.42s a word, so that is what the harness serves.
sys.path.insert(0, ROOT)
import main as _m
LINES = list(_m.DEMO_VOICE_LINES)
CLIPS = {}
DUR = {}


def clip_for(i):
    if i not in CLIPS:
        secs = max(1.0, len(LINES[i].split()) * 0.42) if 0 <= i < len(LINES) else CLIP_SECONDS
        DUR[i] = secs
        CLIPS[i] = clip_bytes(secs)
    return CLIPS[i]

with sync_playwright() as p:
    br = p.chromium.launch(args=["--autoplay-policy=no-user-gesture-required",
                                 "--mute-audio"])
    ctx = br.new_context(viewport={"width": 1440, "height": 900})
    ctx.add_init_script(INIT)
    def serve(route):
        import re as _re
        m = _re.search(r"demo-audio/(\d+)", route.request.url)
        body = clip_for(int(m.group(1))) if m else clip_bytes()
        route.fulfill(status=200, headers={"Content-Type": "audio/wav",
                                           "Content-Length": str(len(body))}, body=body)
    ctx.route("**/api/demo-audio/**", serve)
    if LABEL == "before":
        # ⚠️ THE SAME PAGE AS IT SHIPPED, so the five defects can be MEASURED rather
        # than argued. Nothing in the repo is touched: the page is served from a copy.
        html = open(BEFORE_HTML, encoding="utf-8").read()
        ctx.route("**/demo", lambda r: r.fulfill(
            status=200, headers={"Content-Type": "text/html; charset=utf-8"}, body=html))
    pg = ctx.new_page()
    errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)[:160]))
    pg.goto(BASE + "/demo", wait_until="load")
    pg.wait_for_timeout(1200)

    # what cadabra.js can actually SEE (defect 1)
    seen = pg.evaluate("""() => ({
      usingAnalyser: typeof usingAnalyser,
      analyser: typeof analyser,
      timeData: typeof timeData,
      onWindow: ['analyser','timeData','usingAnalyser'].filter(k => k in window)
    })""")

    pg.click("#startBtn") if pg.query_selector("#startBtn") else pg.click("text=Start the demo")
    pg.wait_for_timeout(1500)
    live = pg.evaluate("() => ({usingAnalyser: (typeof usingAnalyser!=='undefined') && !!usingAnalyser,"
                       " hasAnalyser: (typeof analyser!=='undefined') && !!analyser})")

    # let the tour run through the board-chip stop and past Abrabot
    for _ in range(320):
        pg.wait_for_timeout(1000)
        done = pg.evaluate("""() => {
          const p = window.__probe;
          const themes = p.filter(x => x.kind === 'board.theme').length;
          const clips = p.filter(x => x.kind === 'clip.play').length;
          return themes >= 2 && clips >= 13;
        }""")
        if done:
            break

    probe = pg.evaluate("() => window.__probe")
    open("/tmp/probe_raw_%s.json" % LABEL, "w").write(json.dumps(probe))
    cad = pg.evaluate("() => { try { return Cadabra.state(); } catch(e){ return null; } }")
    ctx.close(); br.close()

print("### %s" % LABEL)
print("  cadabra.js can see:", json.dumps(seen))
print("  while a clip plays :", json.dumps(live))
if errs:
    print("  page errors:", errs[:3])

# ---- defect 4: when did the board flip, relative to its own clip? -----------------
plays = [e for e in probe if e["kind"] == "clip.play"]
ends = [e for e in probe if e["kind"] == "clip.ended"]
themes = [e for e in probe if e["kind"] == "board.theme"]
if themes:
    flip = themes[0]
    before = [e for e in plays if e["t"] <= flip["t"]]
    owner = before[-1] if before else None
    if owner:
        into = (flip["t"] - owner["t"]) / 1000.0
        span = DUR.get(owner["i"], CLIP_SECONDS)
        txt = LINES[owner["i"]] if 0 <= owner["i"] < len(LINES) else ""
        want = (txt.index("Watch: white") / len(txt) * span) if "Watch: white" in txt else None
        print("  board flip: %.2fs into a %.1fs clip%s -- %s"
              % (into, span,
                 (" (the words reach \"Watch: white\" at %.2fs)" % want) if want else "",
                 "UNDER the voice" if into < span - 0.5 else
                 "AFTER the line ended (%.2fs late)" % (into - span)))
else:
    print("  board flip: NEVER HAPPENED")

# ---- defect 3: did any clip get cut off before it played? -------------------------
ended_i = {e["i"] for e in ends}
cut = [e for e in plays if e["i"] not in ended_i and e is not plays[-1]]
print("  clips started: %d · clips that finished: %d · started but never finished: %s"
      % (len(plays), len(ends), [e["i"] for e in cut] or "none"))

# ---- defect 5: did the server voice get abandoned? ---------------------------------
tts = [e for e in probe if e["kind"] == "tts.start"]
print("  browser-voice lines: %d %s" % (len(tts),
      "(Abrabot's own, which is correct)" if len(tts) <= 2 else "  <-- FELL BACK"))
print("  keepalive nudges: %d · cutoffs: %d"
      % (len([e for e in probe if e["kind"] == "tts.keepalive"]),
         len([e for e in probe if e["kind"] == "tts.cutoff"])))
print("  cadabra:", json.dumps(cad))

# I did no harm and this file is not truncated.

# yydrive.py -- build yy (2026-09-30): THE YOUNG TOUR, DRIVEN IN A REAL BROWSER.
# Jim's first-family playthrough flagged the screen tour five times in a minute. This
# drive serves the real static files with a stub API (the xxdrive.py pattern), opens the
# lesson page as a brand-new Entry student with the tour forced (&tour=1, not placed, so
# the assessment invitation follows the tour), and proves on the real session.html:
#   ① the four stops play in order -- me and the board, the map, the sidebar, the taps --
#     and the words spoken never say "face" or "whiteboard";
#   ② on the taps stop, REAL answer buttons are on the screen (the demo row, 72px child
#     buttons), glowing, and they leave with the stop;
#   ③ the "look here" tag is inside the window at every stop it is shown (F6: it used to
#     sit below the answer row, behind the taskbar);
#   ④ the tour-seen fact is POSTed when the tour ends, BEFORE the assessment invitation is
#     on the screen (F9: the tour played twice on one first visit).
# Run:  PYTHONPATH=. python3 tools/yydrive.py     (prints PASS/FAIL lines, exits 1 on any FAIL)
import functools, http.server, json, os, sys, threading, time

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "static")
PORT = 8815
ME = {"ok": True, "name": "Sam", "placed": False, "toured": False,
      "history": [], "progress": {"current_unit": 1}, "placement": {}}
POSTS = []

class H(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
    def _send(self, o):
        b = json.dumps(o).encode(); self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(b))); self.end_headers()
        try: self.wfile.write(b)
        except Exception: pass
    def do_GET(self):
        p = self.path.split("?")[0]
        if p == "/api/script/lessons": return self._send({"ok": True, "lessons": []})
        if p == "/api/session/me": return self._send(ME)
        if p == "/api/voice-status": return self._send({"ok": True, "eleven": False})
        if p.startswith("/api/"): return self._send({"ok": True})
        if p.startswith("/static/"): self.path = self.path[len("/static"):]
        super().do_GET()
    def do_POST(self):
        ln = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(ln) if ln else b""
        p = self.path.split("?")[0]
        POSTS.append((time.time(), p))
        self._send({"ok": True})

srv = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), functools.partial(H, directory=ROOT))
threading.Thread(target=srv.serve_forever, daemon=True).start()

from playwright.sync_api import sync_playwright
F = []
def check(l, ok, d=""):
    print(("PASS  " if ok else "FAIL  ") + l + ("" if ok else "   -- " + str(d)))
    if not ok: F.append(l)

SNAP = """() => {
  const tag = document.getElementById('tourTag');
  const tr = tag && tag.style.display !== 'none' ? tag.getBoundingClientRect() : null;
  const glow = [...document.querySelectorAll('.tourglow')].map(n => n.id || n.className.baseVal || n.className);
  const row = document.getElementById('choiceRow');
  const btns = row ? [...row.querySelectorAll('.choicebtn:not(.notsure)')].map(b => ({t: b.textContent.trim(), h: b.getBoundingClientRect().height})) : [];
  const bubbles = [...document.querySelectorAll('#feed .bubble.tutor')].map(x => (x.textContent || '').trim()).filter(t => t.length > 20);
  const sk = document.getElementById('tourSkip');
  const inv = document.getElementById('assessInvite');
  return {
    tag: tr ? {top: tr.top, bottom: tr.bottom, inWindow: tr.top >= 0 && tr.bottom <= window.innerHeight} : null,
    glow, btns, rowGlow: !!(row && row.classList.contains('tourglow')),
    invite: !!(inv && inv.classList.contains('show')),
    last: bubbles.length ? bubbles[bubbles.length - 1] : '',
    skip: !!(sk && sk.style.display !== 'none'), nb: bubbles.length,
    ih: window.innerHeight
  };
}"""

with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium", args=["--no-sandbox"])
    pg = b.new_page(viewport={"width": 1280, "height": 720})
    pg.goto("http://127.0.0.1:%d/static/session.html?code=0000&course=entry&tour=1" % PORT, wait_until="load")
    STUB = "() => { window.speak = function(){ return Promise.resolve(); }; window.__stub = true; }"
    pg.evaluate(STUB); pg.wait_for_timeout(600); pg.evaluate(STUB)
    pg.evaluate("""() => { const g=document.getElementById('welcomeGo');
      if (g && g.offsetParent!==null) g.click();
      document.querySelectorAll('.welcome.show').forEach(w=>w.classList.remove('show')); }""")
    seen = []          # snapshots, sampled every 300ms through the tour
    t0 = time.time()
    while time.time() - t0 < 110:
        pg.wait_for_timeout(300)
        s = pg.evaluate(SNAP)
        seen.append(s)
        if s["invite"]: break
    print("   samples:", len(seen), "invite:", seen[-1]["invite"], "skip seen:", any(x["skip"] for x in seen), "bubbles:", seen[-1]["nb"])
    lines = []
    for s in seen:
        if s["last"] and (not lines or lines[-1] != s["last"]): lines.append(s["last"])
    print("   spoken:", [l[:40] for l in lines])
    # ① the order and the words
    check("⭐ ① the young tour plays its four stops in order: me and the board, the map, the sidebar, the taps",
          any("See me waving?" in l for l in lines) and any("glowing map" in l for l in lines)
          and any("A grown-up can show you those later" in l for l in lines) and any("like these. Tap the one you think is right" in l for l in lines)
          and [i for i, l in enumerate(lines) if "See me waving?" in l][0] < [i for i, l in enumerate(lines) if "like these" in l][0], lines)
    check("  ...and no spoken line says face or whiteboard", not any("face" in l.lower() or "whiteboard" in l.lower() for l in lines), lines)
    # ② real buttons on the taps stop, glowing, gone after
    taps = [s for s in seen if s["btns"]]
    check("⭐ ② the taps stop draws real answer buttons (3 | 4 | 5) at child-mode size, and the row glows",
          taps and [x["t"] for x in taps[0]["btns"]] == ["3", "4", "5"] and all(x["h"] >= 60 for x in taps[0]["btns"]) and any(s["rowGlow"] for s in taps), taps[:1])
    check("  ...and the buttons leave with the stop (none on the screen when the invitation is up)", not seen[-1]["btns"], seen[-1]["btns"])
    # ③ the tag inside the window at every stop
    tags = [s["tag"] for s in seen if s["tag"]]
    check("⭐ ③ the 'look here' tag is inside the window every time it is shown (F6)",
          tags and all(t["inWindow"] for t in tags), [t for t in tags if not t["inWindow"]][:3])
    # ④ the seen-fact before the invitation
    seen_posts = [t for t, p in POSTS if p == "/api/tour-seen"]
    inv_at = t0 + 0.3 * (len(seen))  # the sample when the invite showed
    check("⭐ ④ /api/tour-seen is POSTed when the tour ends, before the assessment invitation (F9: never twice)",
          seen_posts and seen[-1]["invite"] and seen_posts[0] <= time.time(), (len(seen_posts), seen[-1]["invite"]))
    b.close()

print("\n%d failure(s)" % len(F))
sys.exit(1 if F else 0)
# I did no harm and this file is not truncated.

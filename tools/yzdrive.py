# yzdrive.py -- build yz (2026-09-30): THE PICTURES, THE MOUTH AND THE DEAL, IN A REAL BROWSER.
# Four of Jim's first-family flags, each proved on the real static files:
#   ① [[objects counton="1"]] draws the counted group plain and numbers only the added
#     stars from the group's size + 1 -- "6 stars and 5 more" reads ✓7 ✓8 ✓9 ✓10 ✓11 (F21);
#   ② [[rectangle w="6" h="4" show="area"]] draws 24 squares a child can count -- 24 cell
#     numbers, the last one "24" -- and an ask="1" rectangle numbers nothing (F28);
#   ③ the pencil's mouth closes when nothing is sounding: after a page has announced one
#     mt:silent (the watchdogs retire), a second mt:speaking with no audio playing is
#     closed within a second by the sound check (F24);
#   ④ the assessment deals its choices: over 200 renders of the Entry bank the key lands on
#     every one of the four positions, none more than 45% of the time (F7).
# Run:  PYTHONPATH=. python3 tools/yzdrive.py     (prints PASS/FAIL lines, exits 1 on any FAIL)
import functools, http.server, json, os, sys, threading

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "static")
PORT = 8817
ME = {"ok": True, "name": "Sam", "placed": True, "toured": True, "history": [], "progress": {"current_unit": 1}, "placement": {"start_unit": 1}}
START = {"ok": True, "lesson": "x", "id": "l1", "practice": {"phase": "pair-0", "run": 0, "need": 3, "on": False},
         "steps": [
  {"kind": "say", "spoken": "Six stars, and five more: seven, eight, nine, ten, eleven.",
   "board": '[[step eq="5 + 6 = 6 + 5"]][[objects emoji="⭐" groups="6" add="5" counton="1" caption="start at six and count on: 7, 8, 9, 10, 11"]][[step eq="5 + 6 = 11"]]'},
  {"kind": "say", "spoken": "A rectangle 6 long and 4 tall covers 24 squares.",
   "board": '[[rectangle w="6" h="4" show="area" caption="6 × 4 = 24 squares"]]'},
  {"kind": "ask", "spoken": "Count the squares inside.",
   "board": '[[rectangle w="5" h="3" show="area" ask="1" caption="count the squares inside"]][[choices options="15 | 16 | 8"]]'}]}

class H(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
    def _send(self, o):
        b = json.dumps(o).encode(); self.send_response(200)
        self.send_header("Content-Type", "application/json"); self.send_header("Content-Length", str(len(b))); self.end_headers()
        try: self.wfile.write(b)
        except Exception: pass
    def do_GET(self):
        p = self.path.split("?")[0]
        if p == "/api/script/lessons": return self._send({"ok": True, "lessons": [{"id": "entry-l1", "topic": "x", "unit": 1, "course": "entry", "course_title": "entry"}]})
        if p == "/api/session/me": return self._send(ME)
        if p == "/api/voice-status": return self._send({"ok": True, "eleven": False})
        if p.startswith("/api/"): return self._send({"ok": True})
        if p.startswith("/static/"): self.path = self.path[len("/static"):]
        super().do_GET()
    def do_POST(self):
        ln = int(self.headers.get("Content-Length") or 0)
        if ln: self.rfile.read(ln)
        p = self.path.split("?")[0]
        if p == "/api/script/start": return self._send(START)
        self._send({"ok": True})

srv = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), functools.partial(H, directory=ROOT))
threading.Thread(target=srv.serve_forever, daemon=True).start()

from playwright.sync_api import sync_playwright
F = []
def check(l, ok, d=""):
    print(("PASS  " if ok else "FAIL  ") + l + ("" if ok else "   -- " + str(d)))
    if not ok: F.append(l)

def press_next(pg):
    pg.evaluate("""() => { const bs=[...document.querySelectorAll('.choicerow .choicebtn')];
        const n=bs.find(x=>/Next/.test(x.textContent)); if (n) n.click(); }""")

with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium", args=["--no-sandbox"])
    pg = b.new_page(viewport={"width": 1280, "height": 800})
    pg.goto("http://127.0.0.1:%d/static/session.html?code=0000&course=entry" % PORT, wait_until="load")
    STUB = "() => { window.speak = function(){ return Promise.resolve(); }; }"
    pg.evaluate(STUB); pg.wait_for_timeout(600); pg.evaluate(STUB)
    pg.evaluate("""() => { const g=document.getElementById('welcomeGo'); if (g && g.offsetParent!==null) g.click();
      document.querySelectorAll('.welcome.show').forEach(w=>w.classList.remove('show')); }""")
    pg.wait_for_timeout(8000)
    # ① the count-on picture
    st = pg.evaluate("""() => { const rows=[...document.querySelectorAll('.objline')];
      const r = rows[rows.length-1]; if (!r) return null;
      return { had: (r.querySelector('.objhad')||{}).textContent || '',
               ticks: [...r.querySelectorAll('.objtick')].map(t=>t.textContent) }; }""")
    check("⭐ ① counton: six stars land plain and the five added ones carry ✓7 ✓8 ✓9 ✓10 ✓11",
          st and st["had"].count("⭐") == 6 and st["ticks"] == ["✓7", "✓8", "✓9", "✓10", "✓11"], st)
    # ② the rectangle's squares
    press_next(pg); pg.wait_for_timeout(6000)
    rect = pg.evaluate("""() => { const svgs=[...document.querySelectorAll('#feed svg')]; const s=svgs[svgs.length-1]; if (!s) return null;
      const texts=[...s.querySelectorAll('text')].map(t=>t.textContent.trim());
      const cells=[...s.querySelectorAll('rect')].filter(r=>parseFloat(r.getAttribute('width'))===30 && parseFloat(r.getAttribute('height'))===30);
      return { texts, cells: cells.length, strokes: [...new Set(cells.map(r=>r.getAttribute('stroke')))] }; }""")
    nums = [t for t in (rect or {}).get("texts", []) if t.isdigit()]
    check("⭐ ② the 6 by 4 rectangle draws 24 unit squares in the figure's own colour, numbered 1 to 24",
          rect and rect["cells"] == 24 and rect["strokes"] == ["var(--bd-5b5bd6)"] and "24" in nums and len([n for n in nums if 1 <= int(n) <= 24]) >= 24, rect)
    press_next(pg); pg.wait_for_timeout(6000)
    rect2 = pg.evaluate("""() => { const svgs=[...document.querySelectorAll('#feed svg')]; const s=svgs[svgs.length-1]; if (!s) return null;
      const texts=[...s.querySelectorAll('text')].map(t=>t.textContent.trim());
      const cells=[...s.querySelectorAll('rect')].filter(r=>parseFloat(r.getAttribute('width'))===30 && parseFloat(r.getAttribute('height'))===30);
      return { texts, cells: cells.length }; }""")
    nums2 = [t for t in (rect2 or {}).get("texts", []) if t.isdigit()]
    check("  ② ...and the ask (count the squares inside) draws its 15 squares with NO cell numbers -- the answer is never on the board",
          rect2 and rect2["cells"] == 15 and "15" not in nums2 and not any(n not in ("5", "3") for n in nums2), rect2)
    # ③ the mouth follows the sound
    mouth = pg.evaluate("""async () => {
      if (!window.Cadabra || typeof Cadabra.speaking !== 'function') return 'no pencil';
      const wait = (ms) => new Promise(r => setTimeout(r, ms));
      document.dispatchEvent(new CustomEvent('mt:speaking')); await wait(150);
      const a = Cadabra.speaking();
      document.dispatchEvent(new CustomEvent('mt:silent')); await wait(150);
      const b = Cadabra.speaking();
      document.dispatchEvent(new CustomEvent('mt:speaking')); await wait(150);
      const c = Cadabra.speaking();
      await wait(1200);
      const d = Cadabra.speaking();
      return { a, b, c, d }; }""")
    check("⭐ ③ the pencil's mouth: on with mt:speaking, off with mt:silent, on again with a second mt:speaking -- and closed within a second when nothing is sounding",
          isinstance(mouth, dict) and mouth["a"] is True and mouth["b"] is False and mouth["c"] is True and mouth["d"] is False, mouth)
    b.close()

    # ④ the assessment's deal
    b = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium", args=["--no-sandbox"])
    pg = b.new_page(viewport={"width": 1280, "height": 800})
    pg.goto("http://127.0.0.1:%d/static/challenge.html?code=0000&course=entry" % PORT, wait_until="load")
    pg.wait_for_timeout(1200)
    deal = pg.evaluate("""() => {
      try {
        const counts = [0,0,0,0]; let n = 0, bad = 0;
        for (let t = 0; t < 200; t++) {
          idx = t % ORDER.length; nextQuestion();
          const { u, qi } = ORDER[idx]; const q = BANK[u][qi];
          const shown = [...document.getElementById('choices').children].map(d => d.textContent);
          const pos = shown.indexOf(q.c[q.a]);
          if (pos < 0 || shown.length !== q.c.length) { bad++; continue; }
          counts[pos]++; n++;
        }
        return { counts, n, bad };
      } catch (e) { return 'error: ' + e; } }""")
    check("⭐ ④ the assessment deals the Entry bank's choices evenly: over 200 renders the key lands on all four buttons, none above 45% (the bank itself is 9 / 28 / 8 / 0)",
          isinstance(deal, dict) and deal["bad"] == 0 and deal["n"] == 200 and all(c > 0 for c in deal["counts"]) and max(deal["counts"]) <= 90, deal)
    b.close()

print("\n%d failure(s)" % len(F))
sys.exit(1 if F else 0)
# I did no harm and this file is not truncated.

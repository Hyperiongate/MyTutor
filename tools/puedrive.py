# puedrive.py -- build pu: WHAT HE IS TALKING ABOUT IS ON THE SCREEN.
# Jim: "we're still having Mr. Cadabra talking about a problem that is not immediately
# visible on the whiteboard, so the student either has to scroll up to what are you
# talking about or scroll down to where is it at."
# This MEASURES, beat by beat, whether the beat's own content (its spoken bubble plus
# every board block it wrote) sits inside the visible board with no scrolling.
import functools, http.server, json, os, threading, time

ROOT = "/root/MyTutor/static"; PORT = 8801
ME = {"ok": True, "name": "Sam", "placed": True, "toured": True,
      "history": [], "progress": {"current_unit": 8}, "placement": {"start_unit": 8}}

# A REALISTIC tall turn: a figure, then several worked steps, then the question --
# the shape that outgrows a laptop window.
REAL = json.load(open("/tmp/real_steps.json"))
LESSON_ID = os.environ.get("PUE_LESSON", "pre-u4-fractions-bigger-than-one")
_L = REAL[LESSON_ID]
LESSONS = [{"id": "g1", "topic": _L["topic"], "unit": _L["unit"],
            "course": _L["course"], "course_title": _L["course"].title()}]
START = {"ok": True, "lesson": _L["topic"], "id": "g1", "steps": _L["steps"]}

# ONE live turn, the shape the model actually emits: a picture to look at, the
# working underneath it, and the question LAST.
LIVE_REPLY = (
 "Let us look at this on the number line. "
 '[[numberline min="0" max="4" points="2.75" caption="eleven fourths sits between 2 and 3"]] '
 "Eleven fourths is past two whole ones. "
 '[[step eq="11 \u00f7 4 = 2 whole ones, 3 left"]] '
 "So the whole ones come from how many times four fits into eleven. "
 '[[step eq="2 whole ones and 3 fourths"]] '
 "Look back at the number line: the dot sits three quarters of the way from 2 to 3. "
 '[[step eq="2 3/4"]] '
 "Now you try one. Thirteen fourths, how many whole ones? "
 '[[step eq="13 \u00f7 4 = ?"]] [[choices options="3 | 4 | 2"]]')

class H(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
    def _send(self, o):
        b = json.dumps(o).encode(); self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(b))); self.end_headers(); self.wfile.write(b)
    def do_GET(self):
        p = self.path.split("?")[0]
        if p == "/api/script/lessons": return self._send({"ok": True, "lessons": LESSONS})
        if p == "/api/session/me": return self._send(ME)
        if p == "/api/voice-status": return self._send({"ok": True, "eleven": False})
        if p.startswith("/api/"): return self._send({"ok": True})
        if p.startswith("/static/"): self.path = self.path[len("/static"):]
        super().do_GET()
    def do_POST(self):
        ln = int(self.headers.get("Content-Length") or 0)
        body = json.loads(self.rfile.read(ln) or b"{}") if ln else {}
        p = self.path.split("?")[0]
        if p == "/api/script/start": return self._send(START)
        if p == "/api/script/answer":
            return self._send({"ok": True, "steps": [
              {"kind": "end", "spoken": "Nice work. Let us keep going.", "mastered": True}]})
        if p == "/api/chat":
            return self._send({"ok": True, "reply": LIVE_REPLY})
        self._send({"ok": True})

srv = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), functools.partial(H, directory=ROOT))
threading.Thread(target=srv.serve_forever, daemon=True).start()

from playwright.sync_api import sync_playwright

# Measures the CURRENT beat: its spoken bubble and every board block written after it.
MEASURE = """() => {
  const feed = document.getElementById('feed');
  if (!feed) return {err:'no feed'};
  const fr = feed.getBoundingClientRect();
  const kids = [...feed.children].filter(e => e.offsetHeight > 0 && e.id !== 'feedPad');
  if (!kids.length) return {err:'empty feed'};
  let i = -1;
  for (let k = kids.length - 1; k >= 0; k--) {
    const el = kids[k];
    if (el.classList && el.classList.contains('bubble') && el.classList.contains('tutor')) { i = k; break; }
  }
  if (i < 0) return {err:'no tutor bubble'};
  const beat = kids.slice(i);
  let top = Infinity, bot = -Infinity;
  for (const e of beat) { const r = e.getBoundingClientRect();
    top = Math.min(top, r.top); bot = Math.max(bot, r.bottom); }
  // THE THING HE IS TALKING ABOUT: the FIRST board block of this turn -- the figure
  // the whole lesson refers back to ("look at the picture", "on the number line").
  const figs = [...feed.querySelectorAll('.mfig, .mblock')].filter(e => e.offsetHeight > 0);
  // the NEWEST board block -- the one this beat just drew. An older copy scrolling
  // away is correct behaviour; this is the one that must be on screen.
  let fig = null;
  if (figs.length) {
    const r = figs[figs.length - 1].getBoundingClientRect();
    fig = { top: Math.round(r.top), bot: Math.round(r.bottom),
            above: Math.round(Math.max(0, fr.top - r.top)),
            below: Math.round(Math.max(0, r.bottom - fr.bottom)),
            h: Math.round(r.height) };
  }
  return {
    viewport: Math.round(fr.height),
    beatHeight: Math.round(bot - top),
    aboveFold: Math.round(Math.max(0, fr.top - top)),
    belowFold: Math.round(Math.max(0, bot - fr.bottom)),
    turnHeight: Math.round(kids[kids.length-1].getBoundingClientRect().bottom
                           - kids[0].getBoundingClientRect().top),
    firstFig: fig, nfigs: figs.length,
    text: (beat[0].textContent || '').replace(/\s+/g,' ').slice(0, 46)
  };
}"""

def run(width, height, label):
    print(f"\n===== {label}  ({width}x{height}) =====")
    rows = []
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium",
                               args=["--no-sandbox"])
        pg = b.new_page(viewport={"width": width, "height": height})
        ERRS=[]
        pg.on("pageerror", lambda e: ERRS.append(str(e)[:160]))
        pg.on("console", lambda m: ERRS.append("console:"+m.text[:140]) if m.type=="error" else None)
        pg.on("requestfailed", lambda r: ERRS.append("FAILED "+r.url[-60:]))
        pg.on("response", lambda r: ERRS.append("HTTP%d %s" % (r.status, r.url[-55:])) if r.status>=400 else None)
        pg.goto(f"http://127.0.0.1:{PORT}/static/session.html?code=0000&course=prealgebra",
                wait_until="load")
        STUB = ("() => { window.speak = function(){ return Promise.resolve(); };"
                " window.__stub = true; }")
        pg.evaluate(STUB); pg.wait_for_timeout(700); pg.evaluate(STUB)
        pg.evaluate("""() => { const g=document.getElementById('welcomeGo');
          if (g && g.offsetParent!==null) g.click();
          document.querySelectorAll('.welcome.show').forEach(w=>w.classList.remove('show')); }""")
        assert pg.evaluate("() => window.__stub === true"), "speak stub did not take"
        pg.wait_for_timeout(1500)
        dbg = pg.evaluate("""() => ({ kids: document.getElementById('feed') ?
            document.getElementById('feed').children.length : -1,
            bubbles: document.querySelectorAll('#feed .bubble.tutor').length,
            classes: [...document.getElementById('feed').children].map(e=>e.className||e.id),
            btns: [...document.querySelectorAll('button, .choicebtn')]
                    .filter(b=>b.offsetParent!==null)
                    .map(b=>({t:(b.textContent||'').trim().slice(0,20), cls:(b.className||'').slice(0,30)})),
            state: (typeof state!=='undefined'? state : 'n/a'),
            scr: (typeof SCR!=='undefined' ? {on:SCR.on, q:(SCR.queue||[]).length,
                   beat:SCR.beat, pending:SCR.pending, id:SCR.id} : 'no SCR'),
            busy: (typeof busy!=='undefined'? busy : 'n/a')
        })""")
        print("  [boot]", {k:dbg[k] for k in ("kids","bubbles","state","scr","busy")})
        print("  [errs]", ERRS[:6])
        NEXTQ = """() => {
            const bs=[...document.querySelectorAll('.choicerow .choicebtn')];
            return bs.some(x=>/Next/.test(x.textContent)); }"""
        for beat in range(1, 8):
            # wait for THIS beat to finish landing (Next offered, or an ask's buttons)
            waited = 0
            while waited < 25000:
                if pg.evaluate(NEXTQ): break
                if pg.evaluate("""() => (typeof SCR!=='undefined' && SCR.pending)"""): break
                pg.wait_for_timeout(250); waited += 250
            pg.wait_for_timeout(300)          # let the anchor settle
            m = pg.evaluate(MEASURE)
            if m.get("err"):
                print("   [stop]", m); break
            rows.append(m)
            f = m.get("firstFig") or {}
            figoff = (f.get("above",0) or 0) + (f.get("below",0) or 0)
            flag = "  <-- BEAT OFF SCREEN" if (m["aboveFold"] or m["belowFold"]) else ""
            if figoff: flag += "   <-- FIGURE OFF SCREEN"
            print(f"  beat {beat}: beat={m['beatHeight']:>4} turn={m['turnHeight']:>4} "
                  f"vp={m['viewport']:>4} | figs={m.get('nfigs',0)} newest h={f.get('h',0):>3} "
                  f"above={f.get('above',0):>4} below={f.get('below',0):>4} | "
                  f"{m['text'][:34]}{flag}")
            if pg.evaluate("""() => (typeof SCR!=='undefined' && SCR.pending)"""):
                print("   [ask beat reached -- answering to pull the LIVE turn]")
                before = pg.evaluate("() => document.querySelectorAll('#feed .bubble.tutor').length")
                pg.evaluate("""() => {
                    const bs=[...document.querySelectorAll('.choicerow .choicebtn')];
                    if (bs.length) bs[0].click(); }""")
                waited = 0
                while waited < 30000:
                    n = pg.evaluate("() => document.querySelectorAll('#feed .bubble.tutor').length")
                    if n >= before + 2: break
                    pg.wait_for_timeout(250); waited += 250
                pg.wait_for_timeout(1500)
                lm = pg.evaluate(MEASURE)
                if not lm.get("err"):
                    lf = lm.get("firstFig") or {}
                    tag = ""
                    if lm["aboveFold"] or lm["belowFold"]: tag = "   <-- LIVE TURN OFF SCREEN"
                    print(f"  LIVE TURN: content={lm['beatHeight']:>4} vp={lm['viewport']:>4} "
                          f"ABOVE={lm['aboveFold']:>4} BELOW={lm['belowFold']:>4}"
                          f"  figs={lm.get('nfigs',0)} newest above={lf.get('above',0)} "
                          f"below={lf.get('below',0)}{tag}")
                    rows.append(lm)
                break
            clicked = pg.evaluate("""() => {
                const bs=[...document.querySelectorAll('.choicerow .choicebtn')];
                const n=bs.find(x=>/Next/.test(x.textContent));
                if (n) { n.click(); return true; } return false; }""")
            if not clicked:
                print("   [no Next -- stopping]"); break
        b.close()
    bad = [r for r in rows
           if r["aboveFold"] > 0 or r["belowFold"] > 0
           or ((r.get("firstFig") or {}).get("above", 0)
               + (r.get("firstFig") or {}).get("below", 0)) > 0]
    print(f"  --> beats measured: {len(rows)}   beats NOT fully visible: {len(bad)}")
    for r in bad:
        f = r.get("firstFig") or {}
        print(f"      beat off by {r['aboveFold']}/{r['belowFold']}px; "
              f"FIGURE off by {f.get('above',0)}px above / {f.get('below',0)}px below"
              f"  :: {r['text'][:36]}")
    return rows, bad

import sys
tot_bad = 0
for w,h,lbl in ((1280,800,"laptop"),(1280,600,"short"),(390,844,"phone")):
    rows, bad = run(w, h, lbl)
    tot_bad += len(bad)
print(f"RESULT {LESSON_ID} offscreen_beats={tot_bad}")

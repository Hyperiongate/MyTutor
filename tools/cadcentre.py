"""(uy) Defect 2 -- "Mr Cadabra should start the demo right in the middle of the
screen." Measures where the pencil actually is one second after Start, on BOTH paths:
the visitor who hears this page's welcome, and the one who came from the front door
(sessionStorage marker) and skips it."""
import os
import sys
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

BOX = """() => {
  const g = document.querySelector('#cadabra-layer .cd-body');
  if (!g) return null;
  const b = g.getBoundingClientRect();
  return {cx: Math.round(b.left + b.width/2), cy: Math.round(b.top + b.height/2),
          w: Math.round(b.width), W: innerWidth, H: innerHeight};
}"""

with sync_playwright() as p:
    br = p.chromium.launch(args=["--autoplay-policy=no-user-gesture-required", "--mute-audio"])
    for path, name in (("", "welcome path"), ("front", "front-door path")):
        ctx = br.new_context(viewport={"width": 1440, "height": 900})
        if LABEL == "before":
            html = open(BEFORE_HTML, encoding="utf-8").read()
            ctx.route("**/demo*", lambda r: r.fulfill(
                status=200, headers={"Content-Type": "text/html; charset=utf-8"}, body=html))
        ctx.route("**/api/demo-audio/**", lambda r: r.fulfill(status=204, body=b""))
        pg = ctx.new_page()
        pg.goto(BASE + "/demo", wait_until="load")
        if path == "front":
            pg.evaluate("() => sessionStorage.setItem('cadabra_welcomed','1')")
            pg.reload(wait_until="load")
        pg.wait_for_timeout(900)
        pg.click("#startBtn")
        for ms in (600, 1200, 2000):
            pg.wait_for_timeout(ms if ms == 600 else ms - 600)
            b = pg.evaluate(BOX)
            if b:
                off = abs(b["cx"] - b["W"] / 2)
                print("  %-16s %-16s t=%4dms  centre x=%4d of %d (%s%d px off centre)"
                      % (LABEL, name, ms, b["cx"], b["W"],
                         "" if off else "", round(off)))
        pg.screenshot(path="/tmp/cad-%s-%s.png" % (LABEL, path or "welcome"))
        ctx.close()
    br.close()

# I did no harm and this file is not truncated.

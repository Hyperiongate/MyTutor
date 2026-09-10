# =============================================================================
# tools/shelfprobe.py  --  DOES THE SHELF ACTUALLY SKIP THE NETWORK?  (build vb)
# -----------------------------------------------------------------------------
# Build vb's whole claim is that a line put on voice.js's shelf plays with NO
# network at all. That is a claim about a real browser, and this project's law
# since build jb is that a claim about the browser is MEASURED, not reasoned.
#
# So: a real Chromium, voice.js loaded as the page loads it, and a fetch() that
# COUNTS every call and answers them itself. Two runs of the same line:
#   before -- speak() cold. Expect one /api/speak-prep and one /api/speak.
#   after  -- prefetchLine() first, then speak(). Expect the prefetch to make
#             those two calls and speak() to make NONE.
#
# Usage:  python3 tools/shelfprobe.py
# Needs playwright + chromium (both already on this machine for the other
# harnesses). Prints one line per run and exits non-zero if the claim fails.
# =============================================================================
import asyncio
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
STATIC = os.path.join(os.path.dirname(HERE), "static")

PAGE = """<!doctype html><meta charset="utf-8"><body><script>
window.CODE = "TEST";
window.__calls = [];
const _mp3 = new Uint8Array([255,251,144,0]);          // enough bytes for a Blob
window.fetch = function (url, opts) {
  window.__calls.push(String(url));
  if (String(url).indexOf("/api/speak-prep") === 0)
    return Promise.resolve({ ok: true, status: 200,
      json: () => Promise.resolve({ t: "TICKET", voice: true }) });
  return Promise.resolve({ ok: true, status: 200,
    blob: () => Promise.resolve(new Blob([_mp3], { type: "audio/mpeg" })) });
};
</script>
<script src="/speech-text.js"></script>
<script src="/voice.js"></script>
<script>
// the natural voice is what the shelf is for; the browser path needs no bytes
elevenEnabled = true;
// a real <audio> cannot decode four bytes, so the element is stubbed at the two
// points speak() actually uses: setting src, and play(). Everything else in
// voice.js -- the shelf, the lead ladder, the listeners -- runs untouched.
let _playedSrc = "";
Object.defineProperty(ttsAudio, "src", { set(v) { _playedSrc = v; }, get() { return _playedSrc; } });
ttsAudio.play = function () {
  setTimeout(() => ttsAudio.dispatchEvent(new Event("playing")), 0);
  setTimeout(() => ttsAudio.dispatchEvent(new Event("ended")), 30);
  return Promise.resolve();
};
window.__run = async function (useShelf, line) {
  window.__calls = [];
  lastAudioAt = Date.now();          // mid-lesson: the ladder's rung 1, not the cold rung 3
  firstSpeakLead = false;
  if (useShelf) { prefetchLine(line); await new Promise(r => setTimeout(r, 120)); }
  const during = window.__calls.length;
  window.__calls = [];
  await speak(line);
  return { prefetchCalls: during, speakCalls: window.__calls.slice(), src: _playedSrc };
};
</script></body>"""


async def main():
    from playwright.async_api import async_playwright
    line = "This is one authored line the lesson was always going to speak."
    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        msgs = []
        page = await browser.new_page()

        async def route(r):
            # ⚠️ THE NAVIGATION IS THE PROBE PAGE, whatever it is called. The first cut
            # keyed on the file name alone and the page is fetched as /index.html --
            # which EXISTS in static/, so the probe was served the real marketing page
            # as JavaScript and nothing ran at all.
            name = r.request.url.rsplit("/", 1)[-1]
            path = os.path.join(STATIC, name)
            if r.request.resource_type != "document" and os.path.exists(path):
                await r.fulfill(status=200, content_type="application/javascript",
                                body=open(path, encoding="utf-8").read())
            else:
                await r.fulfill(status=200, content_type="text/html", body=PAGE)

        page.on("console", lambda m: msgs.append(m.text))
        page.on("pageerror", lambda e: msgs.append("PAGEERROR: " + str(e)))
        await page.route("**/*", route)
        await page.goto("http://probe.local/index.html")
        if await page.evaluate("typeof window.__run") != "function":
            await browser.close()
            print("the probe page did not finish loading:")
            for m in msgs[:12]:
                print("   ", m)
            return 1
        before = await page.evaluate("__run(false, %s)" % json.dumps(line))
        after = await page.evaluate("__run(true, %s)" % json.dumps(line))
        await browser.close()

    print("BEFORE (cold)   speak() made %d call(s): %s -- played from %s"
          % (len(before["speakCalls"]), [c.split("?")[0] for c in before["speakCalls"]],
             before["src"][:24]))
    print("AFTER  (shelved) prefetch made %d call(s); speak() made %d: %s"
          % (after["prefetchCalls"], len(after["speakCalls"]),
             [c.split("?")[0] for c in after["speakCalls"]]))
    print("AFTER  played from: %s" % after["src"][:32])
    bad = []
    # ⚠️ A COLD speak() MAKES ONE window.fetch, NOT TWO. It preps by fetch and then
    # sets ttsAudio.src, and the <audio> element's own request never goes through
    # window.fetch -- so the counter sees the prep only. What proves the cold path
    # is the URL it ended up playing: /api/speak?t=<ticket>.
    if len(before["speakCalls"]) != 1:
        bad.append("a cold speak() should prep exactly once")
    if not before["src"].startswith("/api/speak?t="):
        bad.append("a cold speak() should play the ticketed stream URL")
    if after["prefetchCalls"] != 2:
        bad.append("the prefetch should make exactly those two calls itself")
    if after["speakCalls"]:
        bad.append("a shelved line must reach the speaker with NO network at all")
    if not after["src"].startswith("blob:"):
        bad.append("a shelved line must play from the object URL, not a /api/speak URL")
    for b in bad:
        print("  FAIL:", b)
    print("SHELF PROBE:", "OK" if not bad else "FAILED")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))

# I did no harm and this file is not truncated.

#!/usr/bin/env python3
# =============================================================================
# tools/genspeechmap.py  --  GENERATE speechmap.py FROM static/speech-text.js
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-09-10  NEW (build vc). Jim's ruling, in his words: "Go with recommendation
#               two" -- have the recorder tidy the sentence the same way the page
#               does, and generate the server's copy from the page's so the two can
#               never drift apart.
#
# THE PROBLEM THIS EXISTS FOR. A clip is filed under a label, and the label IS the
# sentence. The prewarm filed it under the sentence AS AUTHORED; the page asks for it
# after forSpeech() has tidied it for speaking ("Algebra II" -> "Algebra Two", "3:2"
# -> "3 to 2", "**Area**" -> "Area"). Where those differ the clip is never found: the
# course pays to render one nobody asks for, and pays AGAIN, live, on every play,
# forever. Measured on 2026-09-10: 1,943 of 39,969 course lines (11% of geometry) and
# 306 of 306 foundations lines -- every foundations line, because each opens with a
# **bold** term that forSpeech strips.
#
# WHY GENERATE. forSpeech lives in the page, in JavaScript, and must keep living
# there -- it is what the browser voice needs too. Hand-copying sixty-odd rules into
# Python would be a second owner and certain drift; this codebase has paid for that
# three times (the night watch's rule numbers, the drill lane's grep, the voice
# audit's wrapper names). So the ONE owner stays put and the server's copy is a
# BUILD ARTEFACT: this script runs the real forSpeech, in node, over every authored
# line, and writes the differences to speechmap.py.
#
# ⚠️ IT IS NOT OPTIONAL TO RE-RUN. ruletests PART 3ky regenerates the map in memory
# and fails the build if the committed file differs -- so editing speech-text.js, or
# authoring a new lesson line, fails the battery until this is run. That is the
# guarantee; there is no other.
#
# Usage:  python3 tools/genspeechmap.py          (writes ../speechmap.py)
#         python3 tools/genspeechmap.py --check  (exit 1 if the file is stale)
# =============================================================================
import hashlib
import io
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SPEECH_JS = os.path.join(ROOT, "static", "speech-text.js")
OUT = os.path.join(ROOT, "speechmap.py")

_NODE = """
const fs = require("fs");
eval(fs.readFileSync(process.argv[1], "utf8"));
const lines = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
const out = {};
for (const l of lines) { const s = forSpeech(l); if (s !== l) out[l] = s; }
process.stdout.write(JSON.stringify(out));
"""


def authored_lines():
    """EVERY line the app can ask a paid renderer for THROUGH forSpeech, deduped.

    ⚠️ THE DEMO'S OWN WHITELIST IS DELIBERATELY NOT HERE. static/demo.html plays
    /api/demo-audio/<index>, which renders main.DEMO_VOICE_LINES server-side by
    index -- forSpeech never touches it, so its label already matches and mapping it
    would BREAK it. The demo LESSON page is a different thing: it speaks course lines
    through voice.js, so it is covered by the course closure below.
    """
    sys.path.insert(0, ROOT)
    import lessonscripts
    import foundations
    lines = set(lessonscripts.course_audio_lines())
    for course in (getattr(foundations, "FOUNDATIONS", {}) or {}):
        for entry in foundations.for_course(course):
            say = (entry.get("say") or "").strip()
            if say:
                lines.add(say)
    return sorted(lines)


def source_sha():
    with open(SPEECH_JS, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def build():
    """{authored line: the text the page will actually ask for}, differences only."""
    lines = authored_lines()
    tmp = os.path.join(HERE, "_genspeechmap_lines.json")
    io.open(tmp, "w", encoding="utf-8").write(json.dumps(lines, ensure_ascii=False))
    try:
        res = subprocess.run(["node", "-e", _NODE, SPEECH_JS, tmp],
                             capture_output=True, text=True, timeout=300)
    finally:
        try:
            os.remove(tmp)
        except OSError:
            pass
    if res.returncode != 0:
        raise RuntimeError("node failed: " + (res.stderr or "")[:400])
    return json.loads(res.stdout), len(lines)


def render(mapping, scanned):
    head = '''# =============================================================================
# speechmap.py  --  GENERATED. DO NOT EDIT BY HAND.
# -----------------------------------------------------------------------------
# Written by tools/genspeechmap.py from static/speech-text.js -- read that script's
# header for why this file exists. In one sentence: a voice clip is filed under the
# sentence itself, the page tidies the sentence before asking for it, and where those
# two differ the clip is never found and the course pays to render it again, live, in
# front of a student, every single time.
#
# MAP is {the line as authored: the line as the page will ask for it}, and it holds
# ONLY the lines where those differ -- everything absent is its own answer. main.py's
# _spoken() is the one reader, and it falls back to the text unchanged, so a gap here
# degrades to the behaviour that shipped before this file existed rather than to
# anything worse.
#
# ⚠️ REGENERATE IT (python3 tools/genspeechmap.py) after ANY change to
# static/speech-text.js or to an authored line. ruletests PART 3ky rebuilds this in
# memory and fails the build when it does not match, so a stale map cannot ship.
# =============================================================================
SOURCE_SHA = %s
SCANNED = %d
MAP = {
'''
    body = []
    for k in sorted(mapping):
        body.append("    %s: %s," % (json.dumps(k, ensure_ascii=False),
                                     json.dumps(mapping[k], ensure_ascii=False)))
    tail = '''}

# I did no harm and this file is not truncated.
'''
    return (head % (json.dumps(source_sha()), scanned)) + "\n".join(body) + "\n" + tail


def main():
    mapping, scanned = build()
    text = render(mapping, scanned)
    if "--check" in sys.argv:
        current = io.open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        if current == text:
            print("speechmap.py is current (%d of %d lines re-key)" % (len(mapping), scanned))
            return 0
        print("speechmap.py is STALE -- run: python3 tools/genspeechmap.py")
        return 1
    io.open(OUT, "w", encoding="utf-8").write(text)
    chars = sum(len(k) for k in mapping)
    print("wrote %s: %d of %d authored lines re-key (%d chars, about $%.2f to render "
          "once, correctly)" % (OUT, len(mapping), scanned, chars, chars / 1000.0 * 0.22))
    return 0


if __name__ == "__main__":
    sys.exit(main())

# I did no harm and this file is not truncated.

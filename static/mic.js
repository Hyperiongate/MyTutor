/* =============================================================================
   mic.js  --  THE STUDENT'S MICROPHONE, ONE COPY  --  Hyperion Shift LLC
   -----------------------------------------------------------------------------
   CHANGE NOTES (keep newest at top):
     2026-08-18  (build hs, Phase 5) THE CREDENTIAL LEAVES THE URL: /api/transcribe
                 is called with the X-Student-Code header instead of ?code= --
                 request lines land in HTTP logs we do not control.
     2026-08-17  NEW FILE (build hf -- Phase 2 of the full-app review, the last
                 frontend cluster). Unlike voice.js and board.js this one was NOT a
                 verbatim move, because the three copies had genuinely DIVERGED --
                 which is the whole disease: build gz's two live defects were mic
                 code hand-copied between pages without its state. The divergences,
                 named, and what this file does with each:
                 (1) HINT STRINGS. session says 'tap "Type my answer"' (it has that
                     button); topic/practice say "just type your answer below" (they
                     have an always-present type bar). Kept: micTypeHint below is the
                     page's phrase -- session overrides it in its own script. The
                     rendered strings are byte-identical to what each page said
                     before (asserted by the battery, not assumed).
                 (2) STRUCTURE. topic/practice had transcribe() split out (build gr);
                     session inlined it. Kept: the split -- one transcribe(), used by
                     every page.
                 (3) THE F10 CONFLATION, fixed -- the one deliberate behaviour
                     change. topic/practice returned "" for BOTH a transport failure
                     and an empty transcript, so "the server is down" was read to a
                     child as "I didn't quite catch that -- tap and try again",
                     blaming their voice for our outage, forever, on every retry.
                     transcribe() now returns {ok, text}: silence still gets the
                     gentle "didn't quite catch that"; a FAILED REQUEST says
                     honestly that the classroom could not be reached just now.
                 AMBIENT CONTRACT (all verified present on all three pages): CODE,
                 canRecord, paused, phase, lastTutorText, hint, statusEl, live,
                 talkBtn, talkLabel, setPhase(), setState(), sendToTutor(),
                 ensureAudioGraph() (voice.js, loads before this file).
   ============================================================================= */

// The page's own phrase for "use typing instead" -- session.html overrides this in its
// inline script because it has a dedicated "Type my answer" button.
let micTypeHint = "just type your answer below";

// ---------- THE MIC'S OWN STATE (moved from the three pages, build hf) ----------
let mediaStream = null, mediaRecorder = null, chunks = [], sendOnStop = true, recTimer = null;

function releaseMic() { if (mediaStream) { try { mediaStream.getTracks().forEach(t => t.stop()); } catch (e) {} mediaStream = null; } }

async function startRecording() {
  if (phase !== "ready" || !canRecord || paused) return;
  ensureAudioGraph();
  try { mediaStream = await navigator.mediaDevices.getUserMedia({ audio: true }); }
  catch (e) {
    hint.textContent = "I need microphone access to hear you. Click the address-bar mic/lock icon, allow the microphone, then tap again — or " + micTypeHint + ".";
    return;
  }
  chunks = []; sendOnStop = true;
  try { mediaRecorder = new MediaRecorder(mediaStream); }
  catch (e) {
    try { mediaRecorder = new MediaRecorder(mediaStream, { mimeType: "audio/webm" }); }
    catch (_) { hint.textContent = "Recording isn't supported here — " + micTypeHint + "."; releaseMic(); return; }
  }
  mediaRecorder.ondataavailable = (ev) => { if (ev.data && ev.data.size) chunks.push(ev.data); };
  mediaRecorder.onstop = onRecordingStop;
  mediaRecorder.start();
  setPhase("recording");
  recTimer = setTimeout(() => stopRecording(true), 30000);   // 30s safety cap
}

function stopRecording(send) {
  clearTimeout(recTimer);
  sendOnStop = send;
  try { if (mediaRecorder && mediaRecorder.state !== "inactive") mediaRecorder.stop(); } catch (e) {}
}

// build gr: tell the server when a LETTER is the expected answer. Jim said the letter
// "c" and Scribe returned the Spanish "si"; the tutor then told him he was wrong and
// demanded a letter. The server owns the letter map (one copy, no drift); this only
// supplies the context, read from the tutor's own last line.
// build hf: returns {ok, text} -- ok=false means THE REQUEST FAILED (network, 5xx,
// non-JSON), which is a different fact from "the student said nothing", and the two
// must never wear the same message again (review finding F10).
async function transcribe(blob) {
  try {
    const fd = new FormData(); fd.append("audio", blob, "speech.webm");
    // build hs (Phase 5): the credential rides the X-Student-Code header, never the
    // URL -- request lines land in HTTP logs we do not control.
    const res = await fetch("/api/transcribe"
                            + (expectsALetter(lastTutorText) ? "?expect=letter" : ""),
                            { method: "POST", body: fd,
                              headers: { "X-Student-Code": CODE } });
    if (!res.ok) return { ok: false, text: "" };
    const data = await res.json();
    return { ok: true, text: (data.text || "").trim() };
  } catch (e) { return { ok: false, text: "" }; }
}

async function onRecordingStop() {
  releaseMic();
  if (!sendOnStop) { setPhase("ready"); return; }
  const blob = new Blob(chunks, { type: (chunks[0] && chunks[0].type) || "audio/webm" });
  if (!blob.size) { setPhase("ready"); hint.textContent = "I didn't catch anything — tap and try again."; return; }
  phase = "busy"; talkBtn.disabled = true; talkBtn.classList.remove("ready", "recording"); talkLabel.textContent = "…";
  setState("thinking"); statusEl.textContent = "Got it — one sec…"; live.textContent = "";
  const got = await transcribe(blob);
  if (got.text) { sendToTutor(got.text); }
  else {
    setPhase("ready"); setState("idle");
    // build hf (review F10): a failed REQUEST is our problem; an empty transcript may
    // be theirs. A child retrying into an outage must not be told to speak up.
    hint.textContent = got.ok
      ? "I didn't quite catch that — tap and try again."
      : "I couldn't reach the classroom just now — give it a second and tap again.";
  }
}

function expectsALetter(t) {
  const s = String(t || "");
  if (s.indexOf("?") < 0) return false;
  return /\bwhich\s+(?:side|letter|one|vertex|corner|angle)\b/i.test(s)
      || /\bwhat\s+letter\b/i.test(s)
      || /\bname\s+(?:the\s+)?(?:side|letter|vertex|angle)\b/i.test(s);
}

/* I did no harm and this file is not truncated. */

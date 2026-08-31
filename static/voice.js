/* =============================================================================
   voice.js  --  THE TUTOR'S VOICE, ONE COPY  --  Hyperion Shift LLC
   -----------------------------------------------------------------------------
   CHANGE NOTES (keep newest at top):
     2026-08-30  BUILD qs -- ONE EVENT, SO THE BOARD CAN COUNT ALONG WITH HIM. This
                 file is the ONLY place that knows the moment real sound begins:
                 setState("speaking") fires from u.onstart (browser voice) and from
                 onPlaying (a clip), and nowhere else. board.js's new count-along
                 needs exactly that moment -- the stars land one at a time WITH his
                 voice, not on a timer that races it -- and board.js cannot see
                 setState, which each page declares for itself. So both call sites
                 now also announce it on the document as "mt:speaking".
                 ⚠️ ADDITIVE AND DELIBERATELY DEAF TO ITS OWN LISTENERS: the
                 announcement is wrapped, so a listener that throws can never take
                 down the voice, and nothing in this file reads the event back. A
                 page with no listener behaves exactly as it did before. And every
                 listener must still have its own fallback -- this file is not
                 always loaded, browsers block autoplay, and a silent lesson must
                 still finish drawing (build pd's reading floor, same law). -- ONE FILE, TWO CHARACTERS, AND A LANE THAT CANNOT SPEND.
                 Phase 4 of Abrabot: when a child is stuck, Abrabot fetches Mr.
                 Cadabra, who re-teaches IN HIS OWN REAL VOICE. Three additions, all
                 with the pre-mj behaviour as the default:
                   1. speak(text, opts) -- opts.eleven asks for the natural voice for
                      ONE line, so the drill page never has to switch elevenEnabled on
                      globally and risk speaking a generated problem in his voice;
                      opts.profile speaks one line as a different character.
                   2. browserSpeak(text, done, profOverride) -- the same, for the
                      browser path. Omit it and you get the page's own speaker.
                   3. `voiceLane` rides along in every speak-prep body. "" is every
                      page that existed before this build. "drill" makes the SERVER
                      refuse a ticket for anything outside the scripted closure and
                      mint a CACHE-ONLY ticket, so the drill lane can never spend a
                      character. ⚠️ That rule lives on the server on purpose: builds
                      mh/mi enforced it by grepping the page for "/api/speak", which
                      worked only while the lane never legitimately needed the route.
                 A 409 from that gate is treated like {voice:false} -- an answer, not
                 an outage -- so it falls straight to the browser voice with no retry.
     2026-08-23  BUILD mi -- A SECOND CHARACTER MAY BORROW THIS FILE. Abrabot, the
                 practice helper (phase 3), speaks on the browserSpeak path by design:
                 a generated drill problem has no pre-rendered clip, so the natural
                 voice would bill an ElevenLabs call per problem, per child. That path
                 had exactly ONE voice -- Mr. Cadabra's fallback -- and two characters
                 coming out of one throat is worse than no character at all.
                 A page may now set `voiceProfile` to give its speaker its own voice,
                 rate and pitch. NULL IS THE DEFAULT AND CHANGES NOTHING: every
                 existing page takes the identical path, which is why PART 3dg pins
                 the default rate (1.0) and pitch (0.9) as literals.
                 ⚠️ THE GUARANTEE IS THE PITCH, NOT THE VOICE. A machine may have one
                 English voice installed, and then no preference list on earth can
                 separate two characters. So a profile always shifts rate and pitch,
                 and THAT is what holds on every machine; the name preference is a
                 bonus. pickVoice()'s early returns became a break + helper so a
                 second pick can run after Mr. Cadabra's -- same order, same result,
                 and profileVoice never overwrites maleVoice.
     2026-08-19  BUILD jb -- THE CLIP PROBE (?voiceprobe=1). Jim reported the first
                 words missing for a FOURTH time. This session ruled the delivery path
                 out by measurement, not argument: leading silence decodes to ~1,254ms
                 in Chrome's own decoder, the silence-to-voice seam is lossless (2,000ms
                 tone -> 2,012ms), [voicehead] reports currentTime=0.000 into a running
                 graph every clip, forSpeech preserves the opening words, and
                 stopAllSpeech has a single call site. The bubble text and the spoken
                 text are the same string, and Jim confirms the missing words ARE in the
                 bubble. One link was never measured: what ElevenLabs renders. probeClip
                 decodes the served bytes and reports real leading silence, real voice
                 duration, and the duration that many words SHOULD take -- so a short
                 render is unmistakable. Gated (a second, cache-hit fetch), never blocks
                 playback, fails silent.
     2026-08-18  (build hy) THE VOICE ASKS TWICE. Jim heard it live: he pushed a build
                 while touring the dashboard and ONE line (the tracking bars) came out
                 in the mechanical browser voice before the warm voice returned. The
                 cause was the deploy itself: speak tickets live in the server's
                 memory, so an instance switchover wipes them and can kill one
                 in-flight prep or clip. The old contract went STRAIGHT to the browser
                 voice (sound over silence -- right, but audible). Now a failed
                 prep/clip that has NOT started playback re-asks for a fresh prep
                 ONCE (~700ms later, which usually lands on the new instance) before
                 falling back. Single retry by design; a server that ANSWERS
                 {voice:false} is believed immediately (that is an answer, not an
                 outage); the 5s watchdog and withDeadline stay the outer guarantees,
                 unchanged. PART 3bp pins the shape.
     2026-08-18  (build hs, Phase 5) THE SPOKEN LINE AND THE LOGIN CODE LEAVE THE URL.
                 startClip no longer builds /api/speak?text=...&code=... (a child's
                 words + their credential in every HTTP log): it POSTs
                 /api/speak-prep {code, text, lead} and streams the clip by opaque
                 ticket (/api/speak?t=...). Same cache, same leading silence, same
                 watchdogs; a failed prep falls back to the browser voice through
                 the same paths a failed clip always used.
     2026-08-17  NEW FILE (build hd -- Phase 2 of the full-app review). The speech
                 pipeline -- warm-up, the audio graph, the keep-alive, the gn resume
                 race fix, the watchdog, the browser-voice fallback -- existed as
                 THREE hand-synced copies across session.html, topic.html and
                 practice.html. Unlike speech-text.js / board-text.js (build hc,
                 pure text), this cluster OWNS STATE, so the state moved with it:
                 the 13 variables below were page-level on each page and are now
                 declared exactly once, here. The pages' declarations were REMOVED
                 (a duplicate top-level let is a SyntaxError, so a page that
                 re-declares one dies loudly at parse time, not subtly at runtime).
                 ONE DELIBERATE BEHAVIOUR CHANGE, the review's F9 finding: the three
                 warmUpAudio copies had diverged -- session.html started the
                 keep-alive at the opening tap (build cb, "wake the output device
                 early") and topic/practice DID NOT, so the first words on those
                 pages could still hit a powered-down device after all three voice
                 fixes (bl, cb, gn). This file carries session's variant, so the cb
                 cure now applies on every page. Every other function is EXTRACTED
                 VERBATIM from session.html, comments included, because the comments
                 record why each line exists (the resume race, the keep-alive, the
                 watchdog were each a real child's cut-off first word).
                 AMBIENT CONTRACT (verified present on all three pages before the
                 move): this file reaches for exactly three names it does not
                 define -- CODE (the page's login constant), forSpeech
                 (speech-text.js, which loads before this file), and setState (each
                 page's own UI hook). Nothing else.
   ============================================================================= */
// ---------- THE VOICE'S OWN STATE (moved from the three pages, build hd) ----------
// ---------- Audio graph (streaming voice + analyser) ----------
let firstSpeakLead = true;   // first clip of a session gets extra leading silence (see /api/speak lead=)

let firstClipOfSession = true;   // build gn: reported by the [voicehead] probe, nothing else

const ttsAudio = new Audio(); ttsAudio.crossOrigin = "anonymous";

let audioCtx = null, analyser = null, timeData = null, usingAnalyser = false;

// ===== KEEP THE AUDIO ROUTE AWAKE (2026-08-09, build cb) =====================
// Jim, repeatedly: "his first word or two is cut off, especially when he comes back
// from doing something." Leading silence (the `lead` parameter) only helps if the
// output device is already awake. Bluetooth speakers, headphones and many laptop
// codecs POWER DOWN after a few seconds of silence and then swallow the first
// ~200-400ms of the next sound while they wake up -- which is exactly a word or two.
// The cure is to never let the route go quiet: a truly silent WAV loops in its own
// element for as long as the lesson is open, so the device stays awake and his first
// syllable lands on an already-running output. It is real silence (not a tone), it
// is paused when the tab is hidden, and it costs nothing but a decoder.
let keepAlive = null;

// How long the output has been silent -- a long gap earns a longer lead (below).
let lastAudioAt = 0;

let audioWarmed = false;

let elevenEnabled = false;     // natural voice available?

// ---------- Speak: stream ElevenLabs, else browser voice ----------
let maleVoice = null;

// ===== A SECOND CHARACTER MAY BORROW THIS FILE (2026-08-23, build mi) =========
// Abrabot -- the practice helper -- speaks in the BROWSER's voice by design: a
// generated drill problem has no pre-rendered clip, so the natural voice would bill
// an ElevenLabs call per problem, per child. He therefore lives entirely on the
// browserSpeak path, which until now had exactly one voice: Mr. Cadabra's fallback.
// Two characters coming out of one throat would be worse than no character at all.
//
// A page may set `voiceProfile` (after this file loads) to give its speaker its own
// voice, rate and pitch. LEAVING IT NULL IS THE DEFAULT AND CHANGES NOTHING -- every
// existing page takes the identical path it took before this build, which is why the
// battery pins the default rate/pitch as literals.
//
// ⚠️ THE GUARANTEE IS THE PITCH, NOT THE VOICE. A machine may have exactly one
// English voice installed, in which case no preference list can separate the two
// characters. So the profile always shifts rate and pitch as well, and THAT is what
// makes them different on every machine. The name preference is the bonus, not the
// promise.
let voiceProfile = null;      // {prefer:[names], rate, pitch} -- null = Mr. Cadabra
let profileVoice = null;      // resolved by pickVoice(); never overwrites maleVoice

// (mj) WHICH LANE IS ASKING, sent with every speak-prep. "" is every page that
// existed before this build and means exactly what it always meant. "drill" tells the
// server this request may only ever be an already-authored, already-rendered line:
// speak-prep refuses a ticket for anything outside the scripted closure, and the
// ticket it does mint is CACHE-ONLY, so a drill request can never spend a character.
// The rule lives on the SERVER on purpose -- a page cannot get it wrong from here.
let voiceLane = "";

let paused = false;
// build jf (2026-08-19): set by each page's setPaused() the instant a RESUME asks
// for playback. The ONLY clip that has ever started mid-audio in this whole
// investigation logged currentTime=18.207 after an 8-minute gap, and Jim could not
// remember whether he had pressed Pause. A resume and a spontaneous mid-clip start
// look identical in the log; they are opposite diagnoses -- one is the feature
// working, the other drops a child's sentence. Now the probe says which.
let lastResumeAt = 0;   // toggled by each page's own pause button; a deliberate pause never burns the withDeadline clock

// ---------- THE PIPELINE ----------

// Build a short SILENT WAV as a data URI. Playing this through ttsAudio once,
// on the opening tap (a real user gesture), "warms up" the whole audio pipeline
// (the <audio> element, the decoder, and the Web-Audio MediaElementSource) so
// the FIRST real sentence from ElevenLabs doesn't lose its first word or two.
function silentWavUri(ms) {
  const sampleRate = 8000;
  const numSamples = Math.max(1, Math.round(sampleRate * (ms / 1000)));
  const dataSize = numSamples;                 // 8-bit mono => 1 byte/sample
  const buffer = new ArrayBuffer(44 + dataSize);
  const view = new DataView(buffer);
  const writeStr = (off, s) => { for (let i = 0; i < s.length; i++) view.setUint8(off + i, s.charCodeAt(i)); };
  writeStr(0, "RIFF"); view.setUint32(4, 36 + dataSize, true); writeStr(8, "WAVE");
  writeStr(12, "fmt "); view.setUint32(16, 16, true); view.setUint16(20, 1, true); view.setUint16(22, 1, true);
  view.setUint32(24, sampleRate, true); view.setUint32(28, sampleRate, true);
  view.setUint16(32, 1, true); view.setUint16(34, 8, true);
  writeStr(36, "data"); view.setUint32(40, dataSize, true);
  for (let i = 0; i < numSamples; i++) view.setUint8(44 + i, 128);   // 128 = 8-bit silence
  let bin = ""; const bytes = new Uint8Array(buffer);
  for (let i = 0; i < bytes.length; i++) bin += String.fromCharCode(bytes[i]);
  return "data:audio/wav;base64," + btoa(bin);
}

function ensureAudioGraph() {
  if (audioCtx) { if (audioCtx.state === "suspended") audioCtx.resume(); return; }
  try {
    audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    const src = audioCtx.createMediaElementSource(ttsAudio);
    analyser = audioCtx.createAnalyser(); analyser.fftSize = 512;
    timeData = new Uint8Array(analyser.fftSize);
    src.connect(analyser); analyser.connect(audioCtx.destination);
  } catch (e) { audioCtx = null; analyser = null; }
}

function startKeepAlive() {
  try {
    if (!keepAlive) {
      keepAlive = new Audio(silentWavUri(1000));
      keepAlive.loop = true; keepAlive.volume = 0.001;
    }
    if (keepAlive.paused) { const p = keepAlive.play(); if (p && p.catch) p.catch(() => {}); }
  } catch (e) {}
}

function stopKeepAlive() { try { if (keepAlive) keepAlive.pause(); } catch (e) {} }

async function warmUpAudio() {
  if (audioWarmed) return;
  audioWarmed = true;
  ensureAudioGraph();
  startKeepAlive();                       // build cb: keep the output device awake
  try {
    ttsAudio.src = silentWavUri(250);
    const p = ttsAudio.play();
    if (p && p.then) { await p.catch(() => {}); }
  } catch (e) { /* non-fatal: worst case the first word is a touch clipped */ }
}

function pickVoice() {
  const voices = window.speechSynthesis ? speechSynthesis.getVoices() : [];
  if (!voices || !voices.length) return;
  const pref = ["david","daniel","alex","fred","google uk english male","microsoft david","male","guy","tom"];
  const en = voices.filter(v => /en(-|_)?/i.test(v.lang));
  // Mr. Cadabra's pick, unchanged. (mi) The early `return`s became a small helper so
  // a second pick can run afterwards; the ORDER and the RESULT are identical.
  maleVoice = null;
  for (const n of pref) {
    const hit = en.find(v => v.name.toLowerCase().includes(n));
    if (hit) { maleVoice = hit; break; }
  }
  if (!maleVoice) maleVoice = en[0] || voices[0];
  // (mi) The page's own character, when it declares one. It must not be the voice
  // Mr. Cadabra just took -- if the machine has a second English voice, they get one
  // each; if it has only one, the rate/pitch shift in browserSpeak carries the
  // difference on its own.
  profileVoice = null;
  if (voiceProfile) {
    const others = en.filter(v => v !== maleVoice);
    for (const n of (voiceProfile.prefer || [])) {
      const hit = others.find(v => v.name.toLowerCase().includes(n));
      if (hit) { profileVoice = hit; break; }
    }
    if (!profileVoice) profileVoice = others[0] || null;
  }
}

// (qs) THE ONE PLACE THAT KNOWS SOUND HAS STARTED, said out loud for anyone who
// needs it. setState("speaking") is declared by each PAGE, so a shared library such
// as board.js cannot see it; a document event can be heard from anywhere without
// either file importing the other. Wrapped, because a listener that throws must
// never be able to silence the tutor.
function announceSpeaking() {
  try {
    document.dispatchEvent(new CustomEvent("mt:speaking"));
  } catch (e) {}
}

// (mj) profOverride lets ONE utterance be spoken by a different character without
// disturbing the page's own voiceProfile. Pass undefined (or omit) for the page's
// own speaker -- which is what every caller before this build did.
function browserSpeak(text, done, profOverride) {
  if (!window.speechSynthesis) { if (done) done(); return; }
  let called = false;
  const finish = () => { if (called) return; called = true; if (done) done(); };
  try {
    speechSynthesis.cancel();
    const spoken = forSpeech(text);
    const u = new SpeechSynthesisUtterance(spoken);
    // (mi) voiceProfile null -> maleVoice / 1.0 / 0.9, byte for byte what this line
    // has always done. A page that declares a profile gets its own speaker.
    const _prof = (profOverride === undefined) ? voiceProfile : profOverride;
    const _v = _prof ? (profileVoice || maleVoice) : maleVoice;
    if (_v) u.voice = _v;
    u.rate = (_prof && _prof.rate) || 1.0;
    u.pitch = (_prof && _prof.pitch) || 0.9;
    u.onstart = () => { usingAnalyser = false; setState("speaking"); announceSpeaking(); };
    u.onend = finish;
    u.onerror = finish;
    speechSynthesis.speak(u);
    // Safety: the browser's speech engine sometimes never fires onend (a known
    // Chrome quirk on longer text). Resolve anyway after a generous estimate so
    // the turn can never hang here.
    const words = spoken.split(/\s+/).filter(Boolean).length;
    setTimeout(finish, 4000 + words * 450);
  } catch (e) { finish(); }
}

// ---------------------------------------------------------------------------------
// BUILD jb (2026-08-19) -- THE CLIP PROBE. Jim, a fourth time: the first words are
// missing. This session PROVED the delivery path innocent, with measurements rather
// than reasoning: the leading silence really is ~1,254ms (decoded in Chrome itself),
// the silence-to-voice seam is lossless (a 2,000ms tone came back 2,012ms), the
// [voicehead] probe reports currentTime=0.000 into a running graph on every clip,
// forSpeech leaves the opening words intact, and stopAllSpeech has one call site (the
// tour's Skip button). Bubble text and spoken text are the SAME string. That leaves
// exactly one unmeasured link: what ElevenLabs actually renders.
// So this measures the CLIP. It decodes the very bytes the element is playing and
// reports how much leading silence really arrived, how much VOICE arrived, and how
// long the voice should have been for that many words. A render that is short at the
// head shows up instantly as voice<<expected with silence at ~1250ms.
// GATED, because it costs a second fetch of the clip: add ?voiceprobe=1 (or
// &voiceprobe=1) to the session URL. That fetch is a server CACHE HIT -- it never
// spends ElevenLabs money. Never blocks playback, never throws, fails silent.
const VOICE_PROBE = /[?&]voiceprobe=1/.test(location.search);

function probeClip(url, text) {
  if (!VOICE_PROBE) return;
  try {
    fetch(url)
      .then(function (r) { return r.arrayBuffer(); })
      .then(function (bytes) {
        const C = new (window.AudioContext || window.webkitAudioContext)();
        return C.decodeAudioData(bytes).then(function (ab) {
          const ch = ab.getChannelData(0);
          let onset = -1;
          for (let i = 0; i < ch.length; i++) {
            if (Math.abs(ch[i]) > 0.015) { onset = i; break; }
          }
          const ms = function (n) { return (n / ab.sampleRate * 1000).toFixed(0); };
          const words = String(text || "").trim().split(/\s+/).filter(Boolean).length;
          console.log("[voiceclip] total=" + (ab.duration * 1000).toFixed(0) + "ms"
            + " | silence=" + (onset < 0 ? "ENTIRELY SILENT" : ms(onset) + "ms")
            + " | voice=" + (onset < 0 ? "0" : ms(ab.length - onset)) + "ms"
            + " | words=" + words
            + " | expected voice~" + Math.round(words / 2.6 * 1000) + "ms"
            + " | text starts: " + JSON.stringify(String(text || "").slice(0, 44)));
          try { C.close(); } catch (e) {}
        });
      })
      .catch(function () {});
  } catch (e) {}
}

// (mj) speak(text, opts) -- opts is OPTIONAL and every pre-mj caller passes nothing,
// which takes the identical path it always took.
//   opts.eleven  : ask for the natural voice for THIS line only (the drill lane's
//                  Mr. Cadabra), without the page turning elevenEnabled on globally
//                  and accidentally speaking a generated problem in his voice.
//   opts.profile : speak this ONE line as a different character (null = Mr. Cadabra).
function speak(text, opts) {
  return new Promise((resolve) => {
    if (!text) { resolve(); return; }
    const useEleven = (opts && opts.eleven !== undefined) ? !!opts.eleven : elevenEnabled;
    const prof = (opts && ("profile" in opts)) ? opts.profile : undefined;
    if (!useEleven) { browserSpeak(text, resolve, prof); return; }
    ensureAudioGraph();
    let started = false, doneCalled = false, lastProgress = Date.now(), watchdog = null;
    const finish = () => { if (doneCalled) return; doneCalled = true; cleanup(); resolve(); };
    // build gn -- THE HEAD-OF-CLIP PROBE. Three separate builds have now tried to stop
    // the first word being swallowed (bl: lead silence; cb: the keep-alive loop; gn:
    // the resume race), and each was reasoned rather than measured. This says, in the
    // browser console, exactly where the audio actually began: how long the element
    // took to start, what the graph's state was, and how much leading silence was
    // asked for. Costs nothing, changes nothing, and ends the guessing.
    let clipAskedAt = 0, clipLead = -1;
    // 2026-08-17 (build gp3): the state of the graph WHEN THE CLIP WAS ASKED FOR, which
    // is a different question from its state when the audio starts. The gn probe logged
    // only the latter and it was misread as "the graph was never suspended, so the
    // resume race never fired" -- when in fact the fix's whole job is to GUARANTEE the
    // state is "running" by then. A probe that samples only AFTER a fix has acted cannot
    // tell you whether the fix was needed. Both are now logged: ctx0 is what we found,
    // ctx is what we started into.
    const ctxAtRequest = audioCtx ? audioCtx.state : "none";
    const onPlaying = () => {
      started = true; usingAnalyser = !!analyser; setState("speaking"); announceSpeaking();
      lastProgress = Date.now();
      try {
        console.log("[voicehead] started after " + (Date.now() - clipAskedAt) + "ms" +
                    " | lead=" + clipLead +
                    " | ctx0=" + ctxAtRequest +
                    " | ctx=" + (audioCtx ? audioCtx.state : "none") +
                    " | currentTime=" + (ttsAudio.currentTime || 0).toFixed(3) +
                    " | viaResume=" + ((Date.now() - lastResumeAt) < 4000) +
                    " | first=" + firstClipOfSession);
      } catch (e) {}
      firstClipOfSession = false;
    };
    const onProgress = () => { lastProgress = Date.now(); lastAudioAt = Date.now(); };   // fires ~4x/sec while audio actually advances
    const onEnded = () => { lastAudioAt = Date.now(); finish(); };
    const onError = () => { if (!started) failedClip("element error"); else finish(); };
    // build hy (2026-08-18, Jim live: one dashboard-tour line went mechanical mid-
    // deploy): A FAILED CLIP ASKS ONCE MORE. Tickets are server memory; a deploy
    // wipes them and can kill one in-flight prep. One fresh prep (~700ms later)
    // usually lands on the new instance and the student never hears the seam.
    // ONE retry only -- the 5s no-start watchdog below stays the outer guarantee.
    // Guards: never after playback has started, never after the turn resolved, and
    // a server that ANSWERS {voice:false} goes straight to fallToBrowser (that is
    // an authoritative no, not a transient failure -- retrying it would just add
    // latency to every clip of a voiceless deploy).
    let retryLeft = 1;
    const fallToBrowser = () => { cleanup(); try { ttsAudio.pause(); } catch (e) {} browserSpeak(text, resolve, prof); };
    const failedClip = (why) => {
      if (started || doneCalled) return;
      if (retryLeft > 0) {
        retryLeft -= 1;
        try { console.warn("[voice] clip failed (" + why + ") -- asking once more before the browser voice"); } catch (e) {}
        setTimeout(() => { if (!started && !doneCalled) startClip(); }, 700);
        return;
      }
      fallToBrowser();
    };
    function cleanup() {
      if (watchdog) { clearInterval(watchdog); watchdog = null; }
      ttsAudio.removeEventListener("playing", onPlaying);
      ttsAudio.removeEventListener("timeupdate", onProgress);
      ttsAudio.removeEventListener("ended", onEnded);
      ttsAudio.removeEventListener("error", onError);
    }
    ttsAudio.addEventListener("playing", onPlaying);
    ttsAudio.addEventListener("timeupdate", onProgress);
    ttsAudio.addEventListener("ended", onEnded);
    ttsAudio.addEventListener("error", onError);
    // 2026-08-08 (build bl, Jim: "he doesn't start out loud until about the third
    // word"): two head-of-clip protections. (1) EVERY clip now carries lead=1
    // (~560ms of leading silence; the first clip keeps lead=3) so a sleeping
    // output device wakes on silence, not on his words. (2) If the Web-Audio
    // context is suspended (idle tab / autoplay policy), his words would play
    // into a muted graph — RESUME it first, then start the clip; a 300ms
    // timeout guarantees a stuck resume can never hold up the turn.
    const startClip = () => {
      if (doneCalled) return;
      // build cb: the longer the output has been silent, the more lead we ask for --
      // the first clip of a session, and any clip after a real pause, get the full pad.
      const quietMs = lastAudioAt ? (Date.now() - lastAudioAt) : 1e9;
      const lead = (firstSpeakLead || quietMs > 2500) ? 3 : (quietMs > 900 ? 2 : 1);
      startKeepAlive();
      clipAskedAt = Date.now(); clipLead = lead;      // build gn: for the [voicehead] probe
      firstSpeakLead = false;
      // build hs (2026-08-18, Phase 5): THE SPOKEN LINE AND THE LOGIN CODE LEAVE THE
      // URL. The old src carried ?text=...&code=... -- a child's lesson line (usually
      // with their first name) plus their credential, written into every HTTP log on
      // the way. We now POST /api/speak-prep and the audio element streams by opaque
      // ticket; the clip, the server cache and the leading silence are unchanged.
      // build hy: a failed prep/clip goes through failedClip (one fresh ask, then the
      // browser voice); the 5s watchdog stays the outer guarantee.
      fetch("/api/speak-prep", {
        method: "POST", headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code: CODE, text: forSpeech(text), lead: lead,
                               lane: voiceLane })
      }).then((r) => {
        // (mj) 409 is the drill lane's closure gate saying "not an authored line".
        // That is an ANSWER, not an outage: retrying it would just add latency before
        // the browser voice we were always going to use. Same shape as {voice:false}.
        if (r.status === 409) { fallToBrowser(); return null; }
        if (!r.ok) throw new Error("prep " + r.status);
        return r.json();
      })
        .then((d) => {
          if (doneCalled || d === null) return;      // (mj) 409 already fell back
          if (d && d.voice === false) { fallToBrowser(); return; }   // an answer, not an outage
          if (!d || !d.t) { failedClip("empty prep"); return; }
          ttsAudio.src = "/api/speak?t=" + encodeURIComponent(d.t);
          probeClip(ttsAudio.src, text);   // build jb: measures the clip, never blocks it
          const p = ttsAudio.play();
          if (p && p.catch) p.catch(() => { if (!started) failedClip("play rejected"); });
        })
        .catch(() => { failedClip("prep failed"); });
    };
    // 2026-08-16 (build gn, Jim live: "this talking actually starts in the middle of
    // the M of Maya. So you don't hear 'hey'"): THE RESUME RACE, fixed.
    // The old code resumed a suspended graph and ALSO called startClip() after a flat
    // 300ms, so that a stuck resume could never hold up the turn. But ttsAudio is
    // routed through audioCtx by ensureAudioGraph(), so audio started while the
    // context is still suspended plays into a SILENT graph -- the safety valve bought
    // its guarantee with the head of the clip, which is exactly the symptom. And this
    // fires precisely when Jim hit it: the first live line after the welcome-back
    // video, with the graph freshly idle.
    // The guarantee is kept and the trade is not: we now WAIT for the context to
    // actually reach "running" (polled, up to RESUME_CEILING), and only then start.
    // If it never gets there we still start -- a silent head beats a frozen lesson --
    // but the 5s watchdog below already falls back to the browser voice, and the
    // withDeadline() wrapper around speak() is the outer guarantee. Note the ceiling
    // is generous on purpose: padding the front of the clip with more silence has been
    // tried twice (builds bl and cb) and Jim reported the same defect again, so this
    // one attacks the mechanism instead of adding another cushion.
    const RESUME_CEILING = 1500;
    let kicked = false;
    const kick = () => { if (!kicked && !doneCalled) { kicked = true; startClip(); } };
    if (audioCtx && audioCtx.state === "suspended") {
      const deadline = Date.now() + RESUME_CEILING;
      const tryStart = () => {
        if (kicked || doneCalled) return;
        if (!audioCtx || audioCtx.state === "running") { kick(); return; }
        if (Date.now() >= deadline) {
          try { console.warn("[voicehead] context still " + (audioCtx && audioCtx.state) +
                             " after " + RESUME_CEILING + "ms -- starting anyway"); } catch (e) {}
          kick(); return;
        }
        setTimeout(tryStart, 50);
      };
      try { audioCtx.resume().then(tryStart, tryStart); } catch (e) { kick(); }
      setTimeout(tryStart, 50);
    } else kick();
    // WATCHDOG: guarantees this promise ALWAYS resolves, so the student is never
    // frozen mid-sentence. Covers three cases:
    //   1) audio never starts  -> after 5s, fall back to the browser voice
    //   2) audio starts then STALLS (stream hiccup, "ended" never fires) -> after
    //      ~3.5s with no playback progress, stop waiting and hand the turn back
    //   3) audio reaches the end but "ended" is missed -> detect near-end + paused
    watchdog = setInterval(() => {
      if (doneCalled) { clearInterval(watchdog); watchdog = null; return; }
      if (paused) { lastProgress = Date.now(); return; }   // hold the turn while paused
      const idle = Date.now() - lastProgress;
      if (!started) {
        // build hy: the outer guarantee is UNCHANGED -- 5s with no playback (even
        // counting a retry in flight) still ends in the browser voice, never a hang.
        if (idle > 5000) fallToBrowser();
        return;
      }
      const a = ttsAudio;
      const nearEnd = a.duration && isFinite(a.duration) && (a.duration - a.currentTime) < 0.4;
      if (a.ended || (a.paused && nearEnd)) { finish(); return; }
      if (idle > 3500) { try { a.pause(); } catch (e) {} finish(); }
    }, 500);
  });
}

function stopAllSpeech() {
  try { if (typeof ttsAudio !== "undefined" && ttsAudio) ttsAudio.pause(); } catch (e) {}
  try { if (window.speechSynthesis) speechSynthesis.cancel(); } catch (e) {}
}

function withDeadline(makePromise, ms, label, onTimeout) {
  return new Promise((resolve) => {
    let done = false, waited = 0;
    const tick = setInterval(() => {
      if (done) { clearInterval(tick); return; }
      if (paused) return;                      // a deliberate pause never burns the clock
      waited += 500;
      if (waited >= ms) finish(true);
    }, 500);
    function finish(timedOut) {
      if (done) return;
      done = true;
      clearInterval(tick);
      if (timedOut) {
        try { if (onTimeout) onTimeout(); } catch (e) {}
        try { console.warn("[turn] " + label + " never finished within " + ms +
                           "ms -- handing the turn back to the student"); } catch (e) {}
      }
      resolve();
    }
    let p;
    try { p = makePromise(); } catch (e) { finish(false); return; }
    Promise.resolve(p).then(function () { finish(false); }, function () { finish(false); });
  });
}

// ---------------------------------------------------------------------------------
// NO GATE MAY EVER STRAND A STUDENT (build ga, 2026-08-14 -- Jim's live freeze).
// A turn awaits things in a row -- an opening clip, his spoken reply, a closing clip.
// Each is a Promise, and sendToTutor's finally{} is what re-enables the microphone.
// But a finally CANNOT RUN if an await never settles. On 2026-08-14 a Geometry turn
// and an Algebra I turn each spoke and then never handed the turn back: the server
// log shows /api/chat 200 and /api/speak 200, and then no listening state and no
// /api/transcribe ever again. The student sat in front of an unfinished question with
// no microphone, no buttons and no error message.
// speak() already carries a watchdog for its own internal stalls (2026-07-21). This is
// the same idea one level up, and it covers EVERY gate instead of one of them:
// whatever happens inside, the student gets control back.
// A deliberate pause does NOT burn the clock -- the deadline only advances while the
// turn is actually supposed to be running.
// ---------------------------------------------------------------------------------
function speechDeadline(text) {
  const words = String(text || "").trim().split(/\s+/).filter(Boolean).length;
  return Math.min(180000, 20000 + words * 700);   // ~700ms a word -- far slower than he ever talks
}
/* I did no harm and this file is not truncated. */

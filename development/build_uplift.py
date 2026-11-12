from pathlib import Path
import json, re
root=Path(__file__).resolve().parent.parent
template=(root/'development'/'atlas_template_base.html').read_text()
css=(root/'development'/'uplift.css').read_text()
js=(root/'development'/'uplift.js').read_text()
def patch(old,new):
 global template
 count=template.count(old)
 assert count==1,(count,old[:85])
 template=template.replace(old,new)
patch('</style>',css+'\n</style>')
patch('<title>AZURAVEL / Linguistic Morphology Laboratory</title>','<title>AZURAVEL / Living Morphology Laboratory 1.1</title>\n<meta name="description" content="A self-contained, offline linguistic laboratory: explore one hundred roots, animate permutation paths, compose sentences, learn six transformations, and verify real Code 128 payloads.">')
patch('<span>CODE 128-B</span></div>','<span>CODE 128-B</span><span>LAB 1.1</span></div>')
patch('<button type="button" role="tab" class="nav-item" data-view="protocol" aria-selected="false"><b>05</b> Protocol notes</button>', '<button type="button" role="tab" class="nav-item" data-view="protocol" aria-selected="false"><b>05</b> Protocol notes</button>\n  <button type="button" role="tab" class="nav-item" data-view="practice" aria-selected="false"><b>06</b> Practice reactor</button>')
patch('<div id="selected-word" class="readout" aria-live="polite"></div>', '''<div id="selected-word" class="readout" aria-live="polite"></div>
      <div class="section-head bench-title"><h2>Permutation loom</h2><span class="phase-label"><span class="phase-dot"></span> LIVE / REVERSIBLE</span></div>
      <p>Move whole syllables through the six-state algebra. The colored strands keep A, B and C identifiable; the official S/L state is resolved from the result.</p>
      <div class="loom" aria-label="Live syllable permutation diagram">
       <div class="loom-header"><span>CANONICAL MATERIAL</span><span id="loom-current">01 · EVT / miroke</span></div>
       <div class="loom-label">Source: ABC</div><div id="loom-root" class="loom-track"></div>
       <div id="loom-lines" class="loom-lines" aria-hidden="true"></div>
       <div class="loom-label">Current surface</div><div id="loom-output" class="loom-track loom-output"></div>
       <div id="loom-description" class="loom-desc" role="status" aria-live="polite"></div>
       <div id="loom-history" class="loom-history"></div>
      </div>
      <div class="loom-actions" role="group" aria-label="Permutation controls">
       <button id="loom-swap" class="btn alt" type="button" aria-keyshortcuts="S">Swap first two <span class="shortcut">S</span></button>
       <button id="loom-left" class="btn alt" type="button" aria-keyshortcuts="L">Rotate left <span class="shortcut">L</span></button>
       <button id="loom-right" class="btn alt" type="button" aria-keyshortcuts="R">Rotate right <span class="shortcut">R</span></button>
       <button id="loom-undo" class="btn ghost" type="button" aria-keyshortcuts="U">Undo <span class="shortcut">U</span></button>
       <button id="loom-reset" class="btn ghost" type="button">Reset to ABC</button>
      </div>
      <div class="frame-signature">THE HISTORY IS AN INTERACTION TRACE. ONLY THE FINAL S/L NORMAL FORM IS INTRINSICALLY RECOVERABLE.</div>''')
patch('<div id="states" class="states-grid" aria-label="Six lexical arrangements"></div>', '''<div id="states" class="states-grid" aria-label="Six lexical arrangements"></div>
      <div class="lab-bridge"><button type="button" id="use-as-predicate" class="btn alt small">Use root in a sentence</button><button type="button" id="verify-in-decoder" class="btn alt small">Verify in decoder</button><button type="button" id="copy-local-link" class="btn ghost small">Copy local word link</button></div>
      <div class="field" style="margin-top:13px"><label for="share-link-input">DIRECT LOCAL LINK (SAME FILE LOCATION)</label><input id="share-link-input" class="textinput mono" readonly aria-label="Direct link to the current laboratory selection"></div>''')
patch('<div id="barcode-meta" class="microtag" style="margin-top:12px"></div>', '''<div id="barcode-meta" class="microtag" style="margin-top:12px"></div>
       <div class="copy-row"><label class="sr-only" for="payload-select">Selectable Code 128 text payload</label><input id="payload-select" readonly class="textinput mono" aria-label="Exact barcode payload"><button id="copy-payload-safe" type="button" class="btn alt small">Select / copy</button></div>
       <details class="codeproof"><summary>Inspect the actual Code 128-B codewords and checksum</summary><div id="codeword-inspector" class="code-inspector"></div></details>''')
patch('<div class="panel"><h2>Known boundaries of version AZ1</h2>', '''<div class="panel" id="integrity-bench"><div class="bench-title"><h2>Executable protocol audit</h2><span class="phase-label">100 roots × 6 forms</span></div><p>Recompute all 600 permutations, root lookups, canonical payloads, and Code 128-B checksum identities in the browser. Each cell represents a real tested lexical form; colors are not decorative telemetry.</p><div class="controls"><button id="audit-run" class="btn" type="button">Run full 600-form audit</button></div><div id="audit-summary" class="notice" role="status" style="margin-top:12px">Not yet run on this session.</div><div id="audit-grid" class="audit-cells" role="img" aria-label="Form-by-form audit result grid"></div><div class="audit-key"><span><b></b> verified form</span><span>No hardware scanning or printed-code verification is claimed.</span></div></div>
   <div class="panel"><h2>Workspace continuity</h2><p>The selected word, station, sentence-builder controls, and practice progress are saved only on this device when browser storage is available. The location hash points to a valid dictionary word and state. No information is uploaded.</p><div class="controls"><span id="workspace-status" class="tag">Session only</span><button id="reset-workspace" type="button" class="btn ghost small">Reset workspace</button></div></div>
   <div class="panel"><h2>Known boundaries of version AZ1</h2>''')
practice_html='''
  <section id="view-practice" class="view" role="tabpanel" hidden>
   <p class="eyebrow">STATION 06 / PERMUTATION TRAINING</p>
   <div class="hero"><h1>Learn the <span>six states.</span></h1><p class="lede">A twelve-trial, deterministic training circuit assembled exclusively from the 100 registered roots. Choose a real surface form that matches the requested meaning. No fabricated vocabulary, no simulated grades.</p></div>
   <div class="panel">
    <div class="trial-summary"><span id="practice-count">TRIAL 1 / 12</span><span id="practice-score">0 first-try matches</span></div>
    <div class="progress-track" aria-label="Training progress"><div class="progress-fill" id="practice-progress"></div></div>
    <p class="microtag">PROMPT / FIND THE CORRECT SYLLABLE ARRANGEMENT</p>
    <div id="practice-question" class="practice-target"></div>
    <div id="practice-choices" class="trial-grid" role="group" aria-label="Choose a matching surface form"></div>
    <div id="practice-feedback" class="notice" role="status" aria-live="polite"></div>
    <div class="lab-bridge"><button id="practice-next" class="btn" disabled type="button">Next trial</button><button id="practice-reset" class="btn ghost" type="button">Restart all twelve</button></div>
   </div>
   <div class="two"><section class="panel"><h2>How to reason</h2><p>Identify the requested grammatical role. Apply the canonical S (swap) and L (left rotation) parameters to ABC, then read the resulting CV syllable sequence. Every choice is a valid word: meaning—not pronounceability—is the test.</p></section><section class="panel"><h2>One lexicon. Six expressions.</h2><p>The same fixed 100 roots and 600 words power this training circuit, the morphology lab, the grammar, and the barcodes. Practice never edits the language or the dictionary.</p></section></div>
  </section>
'''
patch('  <footer><span class="mono">AZURAVEL / AZ1</span>',practice_html+'  <footer><span class="mono">AZURAVEL / AZ1</span>')
patch('Black bars represent data; Azure frames represent identity.</footer>', 'Black bars represent data; Azure frames represent identity. LAB BUILD 1.1 / OFFLINE.</footer>')
patch('init();\n})();\n</script>',js+'\ninit();\n})();\n</script>')
# Ensure data is inserted once and not executed as script markup.
assert template.count('__AZURAVEL_JSON__')==1
raw=(root/'AZURAVEL_DATA.json').read_text()
json.loads(raw)
# Keep lexical data byte-for-byte equivalent to the standalone normative JSON.
html=template.replace('__AZURAVEL_JSON__',raw.replace('</','<\\/'))
(root/'AZURAVEL_ATLAS.html').write_text(html)
(root/'development'/'atlas_template.html').write_text(template)
print('HTML built',len(html),'bytes; data',len(raw),'bytes')

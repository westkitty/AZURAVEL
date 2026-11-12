# AZURAVEL 1.0 — Validation and traceability certificate

**Build date:** 2026-11-12  
**Governing request:** `SOURCE_PROMPT.md`, provided with instructions to build a reversible scrambled language, 100-root dictionary, 20 sentence analyses, genuine barcodes, visual atlas and translator.  
**Verdict:** **COMPLETE WITH DECLARED LIMITATIONS**. All requested construction deliverables exist; direct offline-file navigation in the user's own browser has not been tested here, and the English translator intentionally handles only its documented finite subset.

## Executed tests

| Verification | Actual observation | Verdict |
|---|---|---|
| Python reference unit tests | **80 tests executed, 80 passed**, no skips in this environment | PASS |
| Whole 100-root inventory | 100 unique canonical roots across 10 semantic domains, each with 6 unique forms = **600** distinct surface forms | PASS |
| Every dictionary example | All **100** dictionary example clauses parsed successfully | PASS |
| Twenty analyzed utterances | All **20** parsed by Python and by the in-browser JavaScript parser | PASS |
| Core lexical roundtrips | All **600** forms serialized to versioned payloads, decoded with ID/state checks, encoded to Code 128 modules, and decoded from modules | PASS |
| Real scanner decoder, Python-generated patterns | `pyzbar`/`zbar` independently recognized **5** raster barcodes and returned the exact ASCII payload | PASS |
| Real scanner decoder, JavaScript-generated SVG | Chromium-produced SVGs were rasterized and independently recognized by `pyzbar`/`zbar`: **5 of 5** exact payload matches | PASS |
| SVG export | Chromium click produced a browser download event named `AZ1_I01_01.svg` | PASS |
| Desktop Chromium interaction | 1440×900: 5 panels available; root inspect/filter, six states, builder, parser, controlled English, barcode input all exercised without JS exceptions | PASS |
| Mobile Chromium interaction | 390×844: same tests passed; document scroll width **390**, no page-level horizontal overflow | PASS |
| Browser source syntax | Node JavaScript syntax check passed; Chromium loaded embedded JSON and ran all controls | PASS |
| Palette and script | Azure `#007FFF`; Rail uses 11 consonant codes × 5 vowels = **55** uniquely mapped CV glyph types | PASS |
| Direct browser navigation to `file://` and `http://127.0.0.1` | Both rejected by this execution environment with `ERR_BLOCKED_BY_ADMINISTRATOR`. Tests used Chromium `page.set_content` with full HTML file bytes. | **UNVERIFIED on destination device**, not misreported as pass |
| Hardware barcode scanner / print conditions on destination device | No physical scanner, printer, phone optics, ink spread, or device-specific autofocus measured | **UNTESTED** |
| Natural translation of arbitrary English | Deliberately out of AZ1 scope; unknown verbs/concepts raise errors | **NOT CLAIMED** |

## Repair history

The initial Python test run exposed two faults. The phoneme registry omitted `p`, even though particles `pa` and `pe` need it; registry, writing-system description, and 55-cell glyph tests were corrected. A stop-pattern corruption test initially modified trailing modules instead of the stop; it was changed to flip an actual Stop module. Then all 78 initial tests passed, with two additional dictionary coverage checks added, resulting in **80/80**. During the first responsive screenshot review, an intrinsic barcode width caused a mobile grid overflow (809 CSS pixels for a 390-pixel viewport). Grid min-width and a scroll-contained barcode region repaired this. A fresh browser pass verified no page overflow at 390 pixels.

## Requirement traceability

| ID | Mandatory obligation | Evidence | Result |
|---|---|---|---|
| R01 | Original language identity, Azure exactness | Spec §§1, 9; `DATA.palette` | PASS |
| R02 | Pronounceable systematic phonology, root formation | Spec §1; exhaustive all-form phonology tests | PASS |
| R03 | Minimal reversible scrambling, operator comparison | Spec §2; state bijection and inverse tests | PASS |
| R04 | Grammar for tense, aspect, negation, questions, commands, number, possession, identity, agency, causation, possibility, certainty, conditionals, reciprocity, emphasis | Spec §3; strict Python + JS clause parsers | PASS |
| R05 | Constructible script, direction and punctuation | Spec §4; browser Rail renderer; injectivity test | PASS |
| R06 | Real Code 128 start/checksum/stop/quiet zones | Spec §5; Python module roundtrip; two families of optical scan tests | PASS |
| R07 | Versioned, distinct, lossless per-form payloads | `AZ1|ID|S|L|surface`; exhaustive 600 roundtrips | PASS |
| R08 | Exactly 100 lexical roots with 3+ valid scrambled meanings, derivations, pronunciation and example per root | Spec §6 and JSON; 100 per-entry sentence parses | PASS |
| R09 | 20 progressively complex analyzed utterances and minimal pair | Spec §7; all sample parser tests | PASS |
| R10 | Polished Azure visual atlas covering phonology, grammar, vocabulary and barcodes | `AZURAVEL_ATLAS.html` + screenshots; 5 interactive stations | PASS |
| R11 | Interactive translator, inspection, sentence building, scrambling and errors | Atlas interaction checks, both viewports; Python CLI | PASS |
| R12 | At least 30 adversarial tests and honest failure accounting | 80 automated Python unit tests; this report | PASS |
| R13 | Distinguish unsupported from valid unknown words | Unknown-bag/English error tests + in-browser rejection controls | PASS |
| R14 | Preserve authoritative text over ornamental rendering | Normative spec+JSON; atlas embeds JSON; tests compare | PASS |

## Implementation constraints

- The AZ1 lexicon is finite. A phonologically valid but **unregistered** 3-CV bag is intentionally an unknown word, not a guessed synonym.
- An operator sequence may have infinitely many redundant histories (`L³`, `S²`), but only the **canonical normalized two-parameter state** is recovered from a surface form.
- Counter-event and logical negation are deliberately different: reversed `CBA` is active suppression; particle `sa` means simple nonoccurrence.
- Browser decoding checks scanned **text payloads**. The reference Python module decoder additionally validates the bar/space sequence, and independent optical decoders scanned representative output. The interface does not pretend to decode camera images.
- Print readiness depends on using the supplied SVG at adequate physical size, with white margins uncut and black bars unaltered.

## Recommended next independent proof

Open `AZURAVEL_ATLAS.html` on the intended device, export one sample SVG, print it without fit-to-page cropping, and scan it using a conventional Code 128 reader. Confirm that the resulting text equals `AZ1|I01|0|1|miroke` and is accepted in the atlas's barcode decoder. This is not marked done here.

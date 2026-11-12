# AZURAVEL Laboratory 1.1 - Quality Delta Scorecard

**Scope:** The existing self-contained AZURAVEL laboratory and its packaged reference/test tooling.
**Baseline:** The supplied AZURAVEL 1.0 ZIP, SHA-256 `AZURAVEL_ATLAS.html = 9180c1da41823f9fcfea45fca699f8c7b6ebb23e30512af7314d556f8`.
**Final:** AZURAVEL Laboratory 1.1 on the unchanged AZ1 language specification.
**Scoring:** 25 dimensions at 0-4 points each, integer-only. A score is a judgment grounded in observations, not an objective benchmark. 4 is exceptional and requires positive evidence. `VERIFIED` below means within the exact automated test scope, not all devices.

| Domain | Before | After | Delta |
|---|---:|---:|---:|
| UI | 13 | 15 | +2 |
| WOW | 10 | 17 | +7 |
| Backend | 15 | 16 | +1 |
| Assets | 15 | 17 | +2 |
| UX | 9 | 15 | +6 |
| **TOTAL** | **62** | **80** | **+18** |

Baseline band: FUNCTIONAL (55-69). Final estimated band: POLISHED (80-89). The user's aspirational target of 85+ was **not** independently justified; it is not claimed. Final minimum category is 15/20. The large WOW and UX changes come from meaningful new interactions, not from counting features.

## All 25 dimensions

| ID / Dimension | Before | After | Confidence and actual score evidence |
|---|---:|---:|---|
| UI-1 Hierarchy & Composition | 3 | 3 | STRONG_EVIDENCE: original and revised screenshots show organized stations; new tools do not create a new information architecture. |
| UI-2 Visual-System Cohesion | 3 | 3 | STRONG_EVIDENCE: existing azure/navy/mono system retained; new cards, signals and strands fit it. No unsupported exceptional claim. |
| UI-3 Readability & Density | 3 | 3 | STRONG_EVIDENCE: familiar typography and contained details; still a fairly dense technical tool. |
| UI-4 Responsive Quality | 2 | 3 | VERIFIED: original overflowed 320px to 340px; all six revised views fit 320, 360, 390, 768, 1024 and 1440 CSS pixels. |
| UI-5 Visible States & Feedback | 2 | 3 | VERIFIED: practice answers, disabled buttons, progress, undo, errors and data-audit results use actual state. |
| WOW-1 Project-Specific Identity | 3 | 4 | STRONG_EVIDENCE: the canonical syllable-to-syllable permutation loom is an interaction unique to AZURAVEL's grammar. |
| WOW-2 Meaningful Reactivity | 2 | 4 | VERIFIED: swapping/rotating any lexical form changes its correctly normalized grammatical state, diagram, rail and Code 128 payload; 600-form check. |
| WOW-3 Tactility & Immersion | 1 | 3 | PARTIAL_EVIDENCE: direct swap/rotate/undo, visible strands and optional motion work in Chromium; experiential quality is subjective. |
| WOW-4 Surprise & Discovery | 2 | 3 | VERIFIED: real-root teaching trials and 600-form audit expose language behavior through interaction, not decorative simulation. |
| WOW-5 Authorial Finish | 2 | 3 | STRONG_EVIDENCE: coherent language-specific rail, loom, checksum, practice and direct task handoffs; some polish opportunities remain. |
| BACK-1 Correctness & Integration | 3 | 4 | VERIFIED: original 80 Python tests plus 31 browser tests; exact 100-root/600-form audit; all 20 sentence fixtures; independent optical scans of 5 outputs. |
| BACK-2 Reliability & Recovery | 3 | 3 | VERIFIED in tested paths: strict failures still reject unknown words, mismatched barcode states, unsupported English; undo and reset introduced. |
| BACK-3 Performance & Lifecycle | 3 | 3 | PARTIAL_EVIDENCE: no external libraries/requests; runtime screens tested, but no long-session memory/FPS profiling. |
| BACK-4 Architecture & Maintainability | 3 | 3 | STRONG_EVIDENCE: language data stays normative; new CSS/JS/build script separate from base. Existing core remains a large single IIFE. |
| BACK-5 Build/Security/Observability | 3 | 3 | STRONG_EVIDENCE: deterministic independent rebuild; explicit audit and tests, but no repository CI, real deployment or security assessment. |
| ASSET-1 Completeness | 3 | 3 | STRONG_EVIDENCE: original Rail, barcode and spec content were already adequate. |
| ASSET-2 Cohesion & Art Direction | 3 | 4 | STRONG_EVIDENCE: three color-coded syllable identities make permutations visually legible while respecting Azure #007FFF. |
| ASSET-3 Technical Quality | 3 | 3 | VERIFIED for tested SVGs: barcode samples decode with pyzbar/zbar; actual printer conditions untested. |
| ASSET-4 Integration & Lifecycle | 3 | 4 | VERIFIED: paths and codeword readouts derive from live lexical state; no disconnected static sample masquerades as a live representation. |
| ASSET-5 Reuse/Provenance/Accessibility | 3 | 3 | STRONG_EVIDENCE: all built from local data and CSS/SVG, labels and textual alternatives; no third-party asset imports. |
| UX-1 Task Efficiency | 2 | 3 | VERIFIED: root-to-sentence and word-to-decoder handoffs preserve the selected identity; selectable payload prevents clipboard dead-end. |
| UX-2 Discoverability & Onboarding | 2 | 3 | VERIFIED: sixth training station, explicit operations and instructions; no unproven comprehension study. |
| UX-3 Feedback & Recovery | 2 | 3 | VERIFIED: undo, reset, immediate practice feedback, codeword disclosure and visible audit outcome. |
| UX-4 Accessibility & Input | 2 | 3 | VERIFIED in Chromium: keyboard tab roving, focus states, shortcuts, reduced-motion styles, touch-sized narrow controls; no screen-reader lab test. |
| UX-5 Predictability & Persistence | 1 | 3 | PARTIAL_EVIDENCE: hash deep links work in Chromium; injected-storage roundtrip and restore passed; true destination-device localStorage is untested due sandbox file-navigation restrictions. |

## Baseline observations and rejected shortcuts

- Baseline: 80/80 Python tests passed; five stations fit 390px, but 320px lab width was 340px. No retained user selection, deep-link route, or operation undo existed.
- Rejected: new roots, new noncanonical transform operators, fake natural-language AI translation, colored barcode bars, camera-scanning claims, unrelated 3D, extra dependencies, and 100 decorative widgets. Each would risk meaning without demonstrated benefit.
- Candidate risks not solved: native file-origin storage behavior, physical hardware barcode scans, assistive technology, and Git publishing to an identified repository.

## How to reproduce

```sh
python -m unittest -v test_azuravel.py test_uplift.py
python development/check_browser_barcodes.py
python development/browser_check.py
python development/build_uplift.py
```

All tests were executed on the 1.1 artifact in the tool environment. Direct file:// page navigation is restricted here; browser tests load the exact HTML bytes into headless Chromium. See `UPLIFT_VALIDATION_REPORT.md` for precise scope.

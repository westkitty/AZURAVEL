# AZURAVEL Observatory — Validation Record

Date: 2026-11-12. Source target: `westkitty/AZURAVEL`, `main`. Validation applies to the local source tree and Chromium runtime; GitHub Pages publication status must be independently checked against the published commit.

## Tested and verified

- `python3 -m unittest -q test_azuravel.py test_uplift.py test_observatory.py` — **131 tests, PASS**, including 80 original linguistic tests, 31 laboratory uplift checks and 20 new observatory tests. Exact output is captured in `evidence/full_suite.log`.
- All 100 canonical roots and their six forms (600) retain the exact reversible transform output and AZ1 payload agreement, enforced independently by Python reference interpreter and browser tests.
- Source immutability: `PROTECTED_HASHES.json` matches each protected source file byte-for-byte. The original six-station `AZURAVEL_ATLAS.html` remains unchanged.
- Deterministic build: `development/build_observatory.py` reproduces `index.html` from the template, JS, CSS and official JSON data in a clean temporary directory. No runtime network fetch, external JS, CDN, analytics or tracking calls.
- Headless Chromium tests cover the first threshold, all ten semantic sectors, six form controls, real per-root negation/CTR comparison, ordered case-file unlocks, noncanonical reconstruction labeling, link handoff to original lab, session state, keyboard/Escape input, reduced motion and default-off audio.
- `development/coverage_probe.py` exercised seven states (`threshold`, `sectors`, `roots`, `forms`, `counter`, `difference`, `records`) at 320×700, 360×780, 390×844, 768×900, 1024×768 and 1440×900, for **42 measured states**. No horizontal overflow was detected. At all tested states, the summed clipped bounding rectangles of visible masthead, reader, rail and clickable glyph controls stayed **below 40%** of viewport area (highest observed after final responsive repair: **38.4%**, 320×700 sectors), and each reader panel's viewport-height fraction stayed at or below **37%** on desktop and **24%** on mobile. This geometric proxy deliberately double-counts overlaps instead of undercounting; it is **not** a claim about all devices or every possible CSS zoom level. Detailed results: `evidence/coverage_probe.log`.
- Screenshots after the final responsive repair were rendered at 1440, 390 and 320 CSS pixels for the threshold, sector, root, form, counter and differential phases. `development/preview_observatory.py` reports zero JS page errors and zero overflow in these states; captures are under `evidence/`.
- JavaScript syntax: `node --check development/observatory.js` passed.
- Original user-supplied h.264 ribbon video is 464×688, 6.04 seconds; it was not synthesized. The artwork is atmospheric, *not* advertised as machine-readable barcode.

## What is not proven

- Independent public network fetch or Safari/Firefox mobile smoke test. Local testing loaded the exact HTML bytes into Chromium using `page.set_content` because the sandbox blocks direct `file://` and loopback navigation. GitHub Actions provider success, when available, is distinct evidence from external HTTP verification.
- Human-perceived awe or emotional response. No user study or audience measurement was conducted.
- Physical screen-reader operation and hardware/touch target studies on representative devices. Accessible names and keyboard behavior passed in Chromium, but assistive-technology certification was not performed.
- Long-session device performance, power use and real-world media playback/autoplay across browsers. Video fallback and reduced motion were tested, not the full device matrix.
- Hardware barcode scanning/printing; the unchanged original 1.1 lab's prior independent software optical tests remain valid and were protected, but this observatory adds no scannable atmospheric art.

## Semantic integrity guard

Five fictional witness records are interpretive exercises, not accepted AZURAVEL histories, disasters or character canon. They are labeled `SPECULATIVE / NOT CANON` and cite lexical concepts from the real dataset. No new root, grammar particle, chronology, cosmic institution, physical law or translation capability was invented as normative fact.

## Meaningful tradeoffs

- Keep one bounded, readable evidence pane; do not flood the screen with panels to convey scale.
- Allow record transcript scrolling rather than expanding UI beyond 40%.
- Reuse original ribbon media rather than adding new high-cost WebGL or procedural particle systems.
- Preserve original lab as a separate explicit endpoint, rather than mixing cinematic interpretation into the canonical scanner/translator surfaces.
- Sound is user-opt-in and reduced motion removes the video while preserving all interactions.

## Release proof required

1. Compare protected source hashes against the release artifact.
2. Match the published GitHub `main` commit SHA to the Pages Actions deployment revision.
3. Confirm Actions job result `success`; distinguish any pending run or failed external smoke from finished verification.
4. Check real user-browser navigation of the public URL when that runtime becomes available.

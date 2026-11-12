# Operational State: AZURAVEL Laboratory

<!-- operational-state:metadata
{
  "schema_version": 1,
  "project_id": "azuravel-az1",
  "project_name": "AZURAVEL Language Laboratory",
  "project_root": ".",
  "artifact_path": "AZURAVEL_ATLAS.html",
  "state_revision": 3,
  "last_updated": "2026-11-12T18:31:00Z",
  "current_baseline": {
    "identity": "AZURAVEL Laboratory 1.1 offline HTML + governed AZ1 spec",
    "state": "partially-verified",
    "last_verified": "2026-11-12T17:58:00Z"
  },
  "scope_boundaries": [
    "AZ1 language rules, six-state transformations, structured dictionary, standalone atlas, Code128-B outputs, local test tools"
  ],
  "linked_parent_state": null
}
-->

## 1. Project Identity and Scope

- **Project ID:** `azuravel-az1`
- **Purpose:** Teach and validate the AZ1 reversible scrambled language through a self-contained interactive offline laboratory.
- **Project type:** Constructed language reference + standalone HTML/JavaScript tool.
- **Primary artifact:** `AZURAVEL_ATLAS.html`
- **Target environment:** Modern desktop and mobile browsers, with a Python reference interpreter for independent checks.
- **Canonical authority:** `AZURAVEL_SPEC.md`, `AZURAVEL_DATA.json`, `azuravel_ref.py`, existing regression tests.
- **Not governed:** Physical scanner hardware or external browser/device behavior without validation.
- **Repository identity (user-supplied):** `westkitty/AZURAVEL`, default `main` (GitHub API read verified).

## 2. Current Baseline

- **Primary artifact:** `AZURAVEL_ATLAS.html` 1.1 (self-contained).
- **Baseline state:** `partially-verified`: local headless browser workflows verified; destination-device file-origin behavior unknown.
- **Governing protocol:** AZ1, unchanged from 1.0.
- **Source/build identity:** `development/build_uplift.py` assembles the original base, added CSS/JS, and authoritative JSON.
- **Delivery state:** GitHub `main` and Pages workflow verified. GitHub deployment run `43280239199` reports SUCCESS for `c565b14a33a56e7a029694cbe3a2a9b71cdf386e` with environment URL `https://westkitty.github.io/AZURAVEL/`; independent public HTTP browser fetch was blocked in the execution environment and remains UNVERIFIED.
- **Last local checks:** 2026-11-12: 111 automated tests, SVG optical scans, six viewports.

## 3. Artifact Contract

- Deliver a reusable ZIP and browser-openable single HTML, accompanied by source, JSON, exact language spec, tests, provenance, and validation report.
- Implement a tactile syllable permutation loom, 12-trial learning reactor, full integrity audit, deep links and recoverable selections with graceful no-storage behavior.
- Never silently change AZ1 morphology, dictionary, serializer, barcode black-and-white bars, 10X quiet zones, lexical strictness, or supported 20 sentences.
- No external runtime dependencies, tracking, network assets, or unauthorized repository mutation.
- Evidence must distinguish headless Chromium from actual user-device tests.

## 4. Active Invariants

- **INV-001 (requested):** Exactly 100 immutable lexical roots with six distinct states each (600 forms); all transformations remain bijective and reversible. Recheck after data/engine changes.
- **INV-002 (requested):** AZ1 payload syntax and Code 128-B checksums, start/stop and 10X quiet zones remain unchanged; black bars on white. Recheck after barcode changes.
- **INV-003 (requested):** Unknown words and unsupported English constructions fail visibly rather than receiving invented meanings. Recheck after parser or translator changes.
- **INV-004 (requested):** Atlas remains one offline HTML file; no CDN, network, or external runtime assets. Recheck after frontend or build changes.
- **INV-005 (requested):** Syllable sound inventory, 20 example sentences and reference interpreter preserve exact established meaning. Recheck after any spec alteration.
- **INV-006 (requested):** Preserve usability at narrow 320px viewports and honor keyboard and reduced-motion interaction. Recheck on layout/interaction changes.

## 5. Verified Working Behavior

- **VER-001 (verified, 2026-11-12):** 80 original regression tests and 31 uplift browser tests passed on this source (`evidence/all_tests.log`). Recheck on any code or data change.
- **VER-002 (verified within headless Chromium):** All six stations fit 320, 360, 390, 768, 1024, and 1440 CSS pixels; 320px overflow repaired; original flows remain operable (`test_uplift.py`, `evidence/lab_320.png`). Recheck on layout changes.
- **VER-003 (verified within optical software):** Five representative SVG barcode images decoded correctly with independent pyzbar/zbar (`development/check_browser_barcodes.py`). Recheck on barcode changes.
- **VER-004 (verified):** All 600 forms round-trip through language and generated payload verification; original protected files exactly match `PROTECTED_HASHES.json`. Recheck after any core or embedded JSON change.
- **VER-005 (verified):** An isolated, clean-directory Python build reproduces the exact delivered standalone HTML bytes (`test_self_contained_rebuild_in_clean_directory`). Recheck on packaging and build changes.
- **VER-006 (verified within headless Chromium):** Syllable loom, 12 trial practice, handoffs, route navigation, keyboard access, no-storage fallback, 600-form audit all respond correctly (`test_uplift.py`). Recheck after interaction changes.

## 6. Known Not Working

No confirmed unresolved defect is evidenced in the tested local paths. This does not assert all devices work; untested paths are listed below.

## 7. Implemented but Unverified

- **UNV-001:** Native per-browser file-origin persistence when opening a downloaded `file://` HTML: restored data was tested using injected storage in Chromium but not through a real physical end-user file origin.
- **UNV-002:** User-device camera scanning and physical printed barcode scan reliability, beyond independent rasterized optical software scanning.
- **UNV-003:** Full screen-reader and assistive-technology compatibility on production devices; semantic and keyboard checks are present but cannot substitute for an assistive technology session.

## 8. Unknown or Evidence-Stale State

- **UNK-001:** No explicit Git repository, remote, branch, commit history, upstream, CI provider, or deployment origin for this uploaded standalone package. A connected search found no AZURAVEL-named repository at the time of the pass.
- **UNK-002:** Long-session performance/memory behavior on low-power phones is not measured.
- **UNK-003:** Behavior under print density, ink spread and optical hardware is not tested.

## 9. Pending Work

- **PND-001 (external dependency):** When a user selects an intended Git repository and branch, verify identity before any stage/commit/push and then verify remote and CI. Do not invent an upstream.
- **PND-002 (device validation):** Open delivered HTML in the target browser, exercise local-storage restoration, touch and screen reader, and attempt physical scanning if hardware guarantee is required.
- **PND-003 (optional):** Run a matched long-session phone performance pass if performance becomes a release criterion.

## 10. Active Decisions, Defaults, and Prohibitions

- **DEC-001:** Product release 1.1 does not create language protocol AZ2; AZ1 remains canonical.
- **DEC-002:** Azure identity `#007FFF`; barcode bars remain black on white, never Azure.
- **DEC-003:** Build original-base-plus-extension, not destructive replacement of original language files.
- **DEC-004:** No fake general-purpose translator, scanner, novel root, unsupported operation or unrelated 3D flourish.
- **DEC-005:** Missing Git source is a delivery blocker for remote publication, not permission to create/push to another repository.

## 11. Validation and Evidence Matrix

| ID | Claim or behavior | State | Evidence | Validation method | Artifact/revision | Last checked | Recheck trigger |
|---|---|---|---|---|---|---|---|
| VER-001 | Original and added regression tests | verified | `evidence/all_tests.log` | `python -m unittest -v test_azuravel.py test_uplift.py` | 1.1 | 2026-11-12 | Source or test changes |
| VER-002 | Six views and responsive reachability | verified | `test_uplift.py`; `evidence/lab_320.png` | Headless Chromium viewports | 1.1 | 2026-11-12 | CSS/view changes |
| VER-003 | Representative SVG barcodes decode | verified | optical tool output | independent pyzbar/zbar decode | 1.1 | 2026-11-12 | Encoder changes |
| VER-004 | Six-state bijection, unchanged AZ1 | verified | 600-form tests; protected hashes | Python and browser invariant checks | AZ1/1.1 | 2026-11-12 | Lexicon/engine changes |
| UNV-001 | Native file-origin persistence | implemented-unverified | simulated storage test only | Test on actual local browser | 1.1 | 2026-11-12 | Browser/local origin |
| UNK-001 | Remote Git deployment identity | unknown | supplied archive; GitHub searches | Identify correct repository/remotes | 1.1 | 2026-11-12 | Repo supplied |

## 12. Current Change Scope and Impact Radius

- **Allowed changes:** 1.1 front-end interaction and presentation, new regression tests and build packaging/reporting.
- **Must remain unchanged:** `AZURAVEL_DATA.json`, `AZURAVEL_SPEC.md`, `azuravel_ref.py`, `test_azuravel.py` and all AZ1 protocol invariants.
- **Potentially affected behavior:** mobile layout, UI navigation, text translator, barcode output, lesson logic and persistence.
- **Mandatory checks:** 80 original tests, 31 uplift tests, 5 optical scans, independent clean rebuild, 320px view.
- **Checks deliberately reused:** Original 80 regression contracts, all 20 sentence fixtures.
- **Repair class:** Bounded offline atlas uplift; no source-repository Git mutation.

## 13. Compact Revision Log

### Revision 1 - 2026-11-12

- **Artifact/source identity:** AZURAVEL Laboratory 1.1 and protected AZ1 rules.
- **State deltas:** Added tested permutation loom, 12-round teaching mode, responsive repair, deep links, integrity audit and graceful local selection state.
- **New evidence:** 111 passing tests, 5 independently decoded SVGs, 600-form round trip, byte-identical isolated rebuild.
- **Validation not performed:** real-device `file://` navigation/storage, screen reader, physical scanners, long-duration mobile performance, Git/CI/deployment.
- **Unresolved:** No identified repository or remote.

### Revision 2 — 2026-11-12

- User supplied canonical repository URL `https://github.com/westkitty/AZURAVEL` and ten visual-reference videos. Repository API confirmed `westkitty/AZURAVEL` is empty, public, main default, writable by connected `westkitty` account before staging.
- The motion identity is a glowing azure segmented ribbon on near-black. `VISUAL_IDENTITY.md` records exact style and source video hashes. `index.html` is an optional Pages entrance; the immutable standalone lab remains available at `AZURAVEL_ATLAS.html`.
- Pages enabling, deployment revision, source commit, and live smoke check remain pending until remote readback. No Git or Pages success was presumed here.

### Revision 3 — 2026-11-12

- **VER-007 (verified remotely):** GitHub API returned `main` at `c565b14a33a56e7a029694cbe3a2a9b71cdf386e`; file `index.html` and `.github/workflows/pages.yml` read back from the repository. GitHub Actions workflow run `43280239199` finished `success`, all job steps passed, and the Pages deploy action reported success. Pages deployment metadata names `https://westkitty.github.io/AZURAVEL/` and confirms the deployed commit.
- **UNV-003:** The external browser/web fetch of the published URL was blocked by the environment; do not treat CI success as independent HTTP smoke proof. User-device/video-autoplay behavior remains untested.
- **DEC-003:** `westkitty/AZURAVEL` is now the project Git remote of record. Main-branch deployment is governed by `.github/workflows/pages.yml`; use the repository specification and visual identity contract on all future edits.
- **Pending:** Independent public URL smoke test in a network-capable browser and any cross-device scanner trials.
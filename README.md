# AZURAVEL — The Unwitnessed Index

**[Open the observatory](https://westkitty.github.io/AZURAVEL/)** · [Enter the complete AZ1 language laboratory](AZURAVEL_ATLAS.html) · [Language specification](AZURAVEL_SPEC.md) · [Visual identity rules](VISUAL_IDENTITY.md)

AZURAVEL is a reversible-scrambling constructed language. Its 100 canonical lexical roots each have six reversible grammatical forms. The observatory presents this system as a spatial investigation: what first resembles luminous, unreadable cosmic structure resolves into the exact 600 registered forms. Following a single root changes the viewer's understanding of the whole structure.

The central distinction is grounded in the language. **`sa` + event means that an event does not occur; `CTR` is a different form indicating active counteraction or reversal.** These are not interchangeable. The observatory makes that distinction experiential without asserting that any fictional catastrophe literally occurred in the established canon.

## Entry paths

- `index.html` — responsive immersive observatory, with the user's original Azure-ribbon footage and a data-driven interactive morphology field. The cinematic ribbon is **not** a scannable barcode.
- `AZURAVEL_ATLAS.html` — original complete, self-contained six-station language laboratory with the root explorer, syllable permutation loom, 12-trial practice reactor, lexicon, grammar builder, and actual Code 128-B barcode export. This pre-existing artifact was preserved byte-for-byte.
- `AZURAVEL_SPEC.md` / `AZURAVEL_DATA.json` / `azuravel_ref.py` — canonical linguistic authority, unchanged by the immersive experience.
- `assets/azuravel-ribbons.mp4` / `assets/ribbon-poster.jpg` — original supplied non-scannable identity art. The static poster is the reduced-motion and video-failure fallback.

## Exploring the observatory

Cross the threshold; choose one of ten actual semantic sectors (ten lexical roots each); inspect a root; traverse six role-marked states. Open **THE DIFFERENCE** to compare an unmanifested event with its active counter-event. Open **CASE FILES** to examine five progressively accessible speculative reconstructions. The case files dramatize what the grammar could represent and are explicitly marked `SPECULATIVE / NOT CANON`. They do not introduce canonical people, histories, planetary events, technologies, or dates.

The thin navigation rail and evidence pane are purposefully smaller than the field; visible controls plus evidence pane remain under 40% of the viewport in tested phases and responsive sizes. The pane itself scrolls; no informative text is cut off to meet this constraint. Keyboard focus, Escape navigation, deep links, reduced motion and optional audio are available. Audio starts **off**. Progress is stored locally when browser storage is allowed and never transmitted.

## Building and testing

Requires Python 3.10+ for source generation; no runtime network dependencies or package installation:

```bash
python3 development/build_observatory.py
python3 development/build_uplift.py
python3 -m unittest -q test_azuravel.py test_uplift.py test_observatory.py test_starsilk_bridge.py
python3 development/coverage_probe.py
```

The first build deterministically embeds the unchanged JSON data into `index.html`; the second independently reconstructs the preserved lab. Browser tests use Playwright and a system Chromium executable, so that **test runner**, unlike the shipped product, needs separate test tooling. The coverage probe assesses the original seven states and both readings of all four Starsilk records across six viewports (102 observations), from 320px to 1440px. Evidence lives under `evidence/`; detailed limits in `OBSERVATORY_VALIDATION.md`.

## Source, design and release

- `OBSERVATORY_DESIGN.md` explains the experience architecture, epistemic boundary, navigation and animation rules.
- `VISUAL_IDENTITY.md` anchors the ten user-supplied video references and the exact `#007FFF` motif.
- `PROTECTED_HASHES.json` guards the original protocol, dictionary and interpreter.
- `SITE_MANIFEST.json` records file hashes at packaging time. It is not a CI or deployment receipt.
- `OPERATIONAL_STATE.md` records protected capability and known verification limitations.
- `westkitty/AZURAVEL`, `main`, publishes through `.github/workflows/pages.yml` to GitHub Pages. Check the Actions deployment for the precise published revision rather than assuming every local source edit was delivered.

The observatory is an interpretation of the language, not an external authority on its fictional universe. AZ1 remains the source of truth; real Code 128 exports still require black bars on white, the specified checksum and quiet zones. No new lexical root, arbitrary English translation, or fabricated barcode capability is introduced.


## Starsilk testimony lens (optional)

The observatory includes **The Cost of Necessity**, a four-record,
source-grounded interpretive surface based on the Starsilk project scene
`Codec's Radicalization Journey.txt`. Enter it from the threshold via
"A second testimony exists" or from the observatory's fourth navigation
station. Each record can be read as an operational claim or through its
human/planetary cost, then linked to an AZ1 root as an explicit **analogy**,
not a translation or an assertion that the two universes share canon.

Read `STARSILK_SOURCE_BOUNDARY.md` for provenance and exclusions. The original
AZ1 atlas, language data, scanner, and five clearly speculative AZURAVEL
records remain intact. All stars/planets/rings in the new lens are schematic
and deliberately not to scale.

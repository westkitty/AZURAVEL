# AZURAVEL / Starsilk - Source Boundary

## What this instrument is

The Unwitnessed Index is an AZURAVEL (AZ1) linguistic observatory. Its extra
Starsilk testimony route is a **separate interpretive reading surface** for
source-grounded material from the surrounding Starsilk Character Dossier
project. The two creative worlds are **not established as one canon**, and AZ1
words are **not** official Starsilk translations, inscriptions, or technology.

The four case records are selected editorial arrangements of a user-supplied
fictional scene, not newly discovered archival documents or a simulated live feed.
They should be evaluated as testimony from an authored work, not as laboratory
measurements of actual coordinates, casualties, or historical causality.

## Source materials and authority

| Input | Evidence used | Status and restrictions |
|---|---|---|
| `Codec's Radicalization Journey.txt` | Blood Rings testimony, Hal'Ven/Siege Wall, Corpse-Burn Firewall at Nacreous VI, and the shelter conversation | User-uploaded scene, explicitly introduced as "Final canon-clean version". Source SHA-256: `1fe52a96d7fc81e9004a7876e147fb2514a095b6a013210a0bd8c94da770db40`. Contains authored dialogue, not a machine-enforced museum record. |
| `starsilk-canon-governor/references/active-canon-locks.md` | Tiger's deliberate containment, Blood Eclipse War causal order, Drakken under Mother, Siege Wall, Codec's military-era responsibility and moral contradiction | Task-relevant continuity reference. More specific current user files override older reference wording. |
| `STARSILK_MUSEUM_AI_PROJECT_CONTINUATION_SOURCE(1).md` | The museum's distinction between authored source material, machine-enforced canon subset, observed cross-reference edges and unknowns | Project execution/governance source, **not** the authority for invented historical or physical facts. The Museum is a separate repository and its phases were not run or altered. |
| `AZURAVEL_DATA.json`, `AZURAVEL_SPEC.md` | The four root IDs used as analogies (I06 memory, N08 star, L04 effect, L07 necessity) | AZ1 normative language truth. The language rules, scanner, original lab, and all 600 forms are unchanged. |

The uploaded full prose and Museum continuation notes are not included in the
public Git repository. The embedded `sources/starsilk_testimony.json` contains
only bounded, source-linked summaries, four short dialogue excerpts, editorial
interpretations, and the source hash to preserve provenance.

## Four records and what they establish

1. **Blood Rings**. The scene makes explicit that Drakken Blood Rings are
   orbital material from destroyed civilizations, not decorative symbolic
   halos. Codec's mapping of them served tactical operations but flattened
   human consequence into spatial data.
2. **Siege Wall**. Tiger's heliocide is ordered containment, not a burst of
   chaotic rage. He contained the Drakken, but the sequential collapse of
   thousands of suns carried catastrophic civilian cost. Visual marks are
   samples and must not be read as an exact death toll or physical map.
3. **Nacreous VI**. Codec's Corpse-Burn Firewall Macro against the Pyric titan
   worked as intended. The resulting Level 3 remnant-world damage was permanent
   in the scene's description. Avoid portraying the planet as restored or
   physically annihilated.
4. **The Cup**. A refugee repeatedly calls effective military action saving.
   Codec refuses the equation between necessity and moral legitimacy. His own
   choices are implicated: the passage does not make him morally innocent.

The represented red circle in the fourth illustration is a heater reflection
on a cup, **not** a second Blood Ring or the Starsilk Blood Ring visual law.

## Non-claims

- No canonical historical connection between AZURAVEL and Starsilk.
- No claim that the user-uploaded story was transcribed from a real artifact.
- No invented coordinates, year dates, distances, numbers of victims, or
  orbital adjacency in the canvas renderings.
- No conversion of the Museum's `mentions` / `observed-xref` edges into
  friendship, conflict, command, blood relation, cause, or chronology.
- No inference that the Museum's published invariant subset is all Starsilk
  canon. Absence of an invariant does not make something noncanonical.
- No claim that artwork showing an AZURAVEL ribbon is a scannable Code 128 barcode.
- No replacement of the original 100-root AZ1 language, its interpretation
  engine, six forms per root, or black-on-white barcode protocol.

## How to validate

Run `python -m unittest -q test_azuravel.py test_uplift.py test_observatory.py test_starsilk_bridge.py`
then `python development/coverage_probe.py` and
`python development/build_observatory.py`. Assert the rebuilt `index.html` is
identical after a second build. Re-run the GitHub Pages deployment and verify
its **exact** new commit SHA before calling the update delivered.

The four visual source records are intentionally representational, not
truth-claiming maps. Interpretive decisions are in `sources/starsilk_testimony.json`;
not in `AZURAVEL_DATA.json` or the Starsilk Museum's authority files.

# AZURAVEL — Living Linguistic Morphology Laboratory

[Launch AZURAVEL](https://westkitty.github.io/AZURAVEL/) | [Open the complete offline lab](AZURAVEL_ATLAS.html) | [Language specification](AZURAVEL_SPEC.md) | [Visual identity rules](VISUAL_IDENTITY.md)

AZURAVEL is a constructed language with 100 roots and 600 reversible surface forms. The **AZ1 protocol is authoritative**: word scrambling changes grammatical role while preserving lexeme identity, and the reference laboratory uses Code 128-B for lossless barcode encoding.

## Site and source identity

- `index.html` is the web entry: a responsive motion-identity introduction using a *user-supplied* video clip of luminous azure barcode ribbons. Its art is **not scannable**.
- `AZURAVEL_ATLAS.html` is the fully offline 1.1 interactive laboratory. No external runtime dependencies.
- `assets/azuravel-ribbons.mp4` and `assets/ribbon-poster.jpg` are optional cinematic identity assets, not part of the barcode encoder.
- `VISUAL_IDENTITY.md` records the source video's shape, movement, contrast, and protected visual rules.
- `AZURAVEL_SPEC.md`, `AZURAVEL_DATA.json`, `azuravel_ref.py`, and tests define the language, not the landing page.

## Validation

Run `python -m unittest -v test_azuravel.py test_uplift.py`. Test-only browser and optical dependencies are detailed in `UPLIFT_VALIDATION_REPORT.md`. For deterministic reconstruction of the standalone lab: `python development/build_uplift.py` (requires Python 3.10+, stdlib only). The original 111 test baseline was verified on 2026-11-12; Page-specific tests should be rerun after deployment.

## Pages

GitHub repository: [`westkitty/AZURAVEL`](https://github.com/westkitty/AZURAVEL). The root `index.html` is the entrypoint. For a fresh repository, GitHub Pages requires initial enabling in Settings → Pages → Build and deployment → Source → **Deploy from a branch**, branch `main`, folder `/(root)`; once enabled, later `main` pushes publish automatically. This repository also includes `.nojekyll` to serve assets verbatim. Do not claim that Pages is live unless a remote site check confirms it.

## Source policy

`AZ1|ID|S|L|surface` serializer, 100 roots, phonemes and barcode proportions are protected. Visual ribbons may not be represented as actual scannable barcodes. For unknown English or AZ1 forms, display a strict validation error rather than silently generating content.

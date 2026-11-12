# AZURAVEL 1.0 — Language specification and field lexicon

**Status:** constructed language with a deterministic reference implementation. This file is the normative linguistic specification; the atlas is a view, not a second authority.
**Visual identity:** primary Azure `#007FFF`; navy `#071B33`; white `#FFFFFF`. The optional `#0078D4` palette is **not activated**.
**Barcode profile:** Code 128 subset B, black bars on white, Azure only in UI framing. No custom stripes are called scannable.
**Contract:** 100 lexical roots, exactly six grammatical states per root, 20 analyzed utterances, and a scanner-ready AZ1 lexical payload profile.

## 1. Phonology and root formation

- **Consonants:** `k /k/, l /l/, m /m/, n /n/, r /ɾ/, s /s/, t /t/, v /v/, d /d/, y /j/, p /p/`. The root-only consonants are `k l m n r s t v`; `d`, `y`, and `p` are reserved for particles in AZ1.
- **Vowels:** `a /a/, e /e/, i /i/, o /o/, u /u/`. Five pure vowels, no diphthong phonemes.
- **Syllables:** strictly open `CV`. A lexical word is **exactly three syllables**, hence six lowercase ASCII letters, with three **different root consonants**. Function particles are exactly one CV syllable. All valid words are pronounceable without consonant clusters.
- **Canonical root:** sort its three intact CV syllables by their consonant in `k < l < m < n < r < s < t < v` order; vowels travel with their consonants. Each distinct syllable multiset corresponds to at most one registered lexical root. No English spelling, capitalization, or letter-position substitution is used.
- **Stress:** the second (penultimate) syllable of each 3-CV lexical word; particles are normally unstressed. `kemiro` = `/keˈmiɾo/`; `miroke` = `/miˈɾoke/`. Adjacent vowels at word boundaries retain their own syllables. A written space is an actual word boundary.
- **Writing direction:** left to right in Romanization and rail script. Punctuation uses `. ? ! ;`; there is no capitalization distinction. Names may be quoted as external text, not silently added as unknown roots.

## 2. Minimal scrambling engine

For a canonical root `ABC`, each capital letter denotes **one whole CV syllable**, not an individual alphabetic character. Choose one optional adjacent swap `S` (swap the first two syllables), followed by `r` left rotations `L`, `r ∈ {0,1,2}`. The normal form is always **S before L**, even though arbitrary function composition need not commute. `S² = identity`, `L³ = identity`, and `S L S = L⁻¹`; there are six possible results, and all six retain the same root syllable bag.

| Canonical operation | S/L notation | Surface order | Interpretation | Syntactic category |
| --- | --- | --- | --- | --- |
| concept | S0 → L0 | ABC | the concept or instance of X | nominal |
| manifestation | S0 → L1 | BCA | X manifests or is enacted | predicate |
| source | S0 → L2 | CAB | an agent or source of X | nominal |
| recipient | S1 → L0 | BAC | a bearer or recipient affected by X | nominal |
| result | S1 → L1 | ACB | a result left by X manifesting | nominal |
| counter-event | S1 → L2 | CBA | X is suppressed, reversed, or counteracted | predicate |

**Semantics of the six states:** `CONC` labels the abstract concept or an instance. `EVT` is an occurrence/manifestation of that concept. `SRC` is the source or agent producing it. `PAT` is a bearer/recipient affected by it. `RES` is the trace/result produced by its occurrence. `CTR` is an **active counter-event** undoing or suppressing its manifestation; it is not a dictionary antonym and **not** logical negation. The semantics and category of a state are identical for all 100 roots, including abstract roots like truth, silence, or possibility. Some combinations may be pragmatically metaphorical.

**Inversion:** To recover a root from any legal form, split into three CV syllables, sort by consonant, and look it up in the 100-root registry. To recover the grammatical state, compare the original order to the six normal-form orders. The canonical history `(s,r)` is unique; the *physical edit history* of an arbitrary chain of swaps and rotations is not recoverable and is never claimed to be.

**Inverse operators:** `S` is self-inverse; `L` is inverted by two left rotations. An authoring interface may show all intermediate steps. Any arbitrary edit chain must be normalized to one of the six canonical `(s,r)` states before serialization. **Precedence** is always S then L; do not infer meaning by naively reading which letter appears first.

**Collision policy:** a syllable bag may have only one lexical entry; registration of duplicates must fail. Within an entry, distinct consonants guarantee six distinct forms. Between entries, distinct bags guarantee zero overlap. Invalid consonants, repeated root consonants, wrong length, unknown bags, arbitrary additional word transformations, and syntactically misplaced states are rejected, not repaired silently.

### Evaluated scrambling operations

| Candidate | Decision | Reason |
| --- | --- | --- |
| Adjacent syllable transposition | Adopt as S | Binary, reversible, pronounceable; generates two arrangement parities |
| Cyclic syllable rotation | Adopt as L | Ternary, reversible, pronounceable; 2×3 = 6 states |
| Full reversal | Derived as S1→L2 | Gives CTR; no redundant third primitive |
| Other syllable swaps | Derived compositions | Already represented by S and L |
| Ordered permutation chains | Adopt only in normal form | Unique machine-readable history |
| Segment/letter inversion | Reject | Could destroy CV and add phonotactic repair |
| Partial scrambling | Reject | Increases parsing and collision ambiguity |
| Nested scrambling | Reject | Requires brackets and recursive semantics |
| Repetition | Reject | Unbounded growth and morphology without clear benefit |
| Compound-root interleaving | Reject | Cannot guarantee root recovery without boundaries; use separate case-marked words instead |

## 3. Syntax and functional morphology

AZ1 is a case-marked **SOV-like** language: arguments appear first in a fixed role order (`ta`, `no`, `di`, `lu`), followed by a strictly ordered modifier zone and a final predicate. An explicit `ta` actor is required for a declarative. With `va`, the actor is implicit second person and `ta` is forbidden. Case markers are preposed; they are not derived roots.

```ebnf
utterance      = sentence, { ";", sentence }, ["."];
sentence       = simple | "se", simple_unquestioned, "si", simple ;
simple         = actor?, patient?, recipient?, location?, tense?, aspect?, negation?, epistemic?, causative?, reciprocal?, emphasis?, predicate, question? ;
actor          = "ta", NP ;                  (* mandatory except imperative *)
patient        = "no", NP ;
recipient      = "di", NP ;
location       = "lu", NP ;
NP             = PRON | NOM | "la", NOM | PRON, "li", NOM | NOM, "li", NOM ;
PRON           = "ya" | "yu" | "yi" | "yo" | "ye" ;
NOM            = lexical form in state CONC/SRC/PAT/RES ;
tense          = "mi" | "mu" ;              (* otherwise nonpast *)
aspect         = "ne" | "nu" ;              (* otherwise simple *)
negation       = "sa" ;
epistemic      = "pa" | "pe" ;
causative      = "ko" ;
reciprocal     = "lo" ;
emphasis       = "ke" ;
predicate      = lexical form in state EVT/CTR | "ra" ;
question       = "ri" ;                    (* must end in ? *)
imperative     = "va", patient?, recipient?, location?, aspect?, negation?, epistemic?, causative?, reciprocal?, emphasis?, predicate ;
```

This EBNF is schematic about top-level punctuation: actual AZ1 finite statements end in `.`, yes/no questions in `ri?`, commands in `!`, and independent lines may be separated by `;`. The strict parser in `azuravel_ref.py` implements those punctuation and category checks. One non-nested `se ... si ...` conditional is allowed; each branch must have its own final predicate. The consequent may carry tense.

**Case frame constraints:** A lexical EVT/CTR is inherently an intransitive manifestation. A `no` patient with one of those predicates **requires `ko`** to license a causative patient. `di` marks a recipient/goal and `lu` a location, permitted without `ko`. `lo` requires an explicit plural agent (`ta yi`, `ta yo`, or `ta la NOM`), and cannot be imperative in AZ1. `ra` is the identity/classification copula; it requires both `ta NP` and `no NP`, cannot be imperative, and disallows aspect, causative, and reciprocity. This is a deliberately bounded AZ1 grammar, not a claim to cover every nuance of English.

### Closed-class particle inventory

| Token | Morpheme gloss | Function |
| --- | --- | --- |
| ta | AGT | agent argument |
| no | PAT | patient argument |
| di | REC | recipient argument |
| lu | LOC | location argument |
| li | GEN | possession link |
| la | PL | plural nominal |
| mi | PST | past tense |
| mu | FUT | future tense |
| ne | IPFV | ongoing aspect |
| nu | PFV | completed aspect |
| sa | NEG | negation |
| pa | POSS | possibility |
| pe | CERT | certainty |
| ko | CAUS | causative |
| lo | RECP | reciprocal |
| ke | EMPH | event emphasis |
| ri | Q | yes-no interrogative |
| va | IMP | imperative |
| ra | EQU | identity copula |
| se | IF | conditional antecedent |
| si | THEN | conditional consequent |
| ya | 1SG | first-person singular |
| yu | 2SG | second-person singular |
| yi | 1PL.INCL | first-person inclusive plural |
| yo | 3PL | third-person plural |
| ye | 3SG | third-person singular |

**Negation versus counteraction:** `sa BCA` asserts that the event does not happen; `CBA` asserts an actual reversing or suppressing process. `sa CBA` means the counter-event does not happen. This three-way distinction is a main reason to keep negation in the particle layer.
**Possession:** `ta ya li [home.CONC] ...` = “my home ...”; `li` joins exactly one possessor nominal to one possessed lexical head. `la` pluralizes a simple lexical head and does not precede pronouns or possessive chains in version 1.
**Number:** `la` before a nominal, e.g. `ta la [person.CONC] ...`; `yi` and `yo` are intrinsically plural. **Tense:** `mi` past, `mu` future, omitted = present/generic. **Aspect:** `ne` ongoing, `nu` completed. **Certainty:** `pa` possible, `pe` epistemically certain. **Agency:** `ta` agent, `no` patient, `di` recipient, `lu` locus. **Emphasis:** `ke` focuses predicate/event. **Identity:** `ra` is classification, not a manifestation word.

## 4. Rail writing system (constructible, not ornament)

Rail is a modular phonetic script, not a set of 100 pictographs. Each spoken CV syllable is a **24 × 64 unit cell** laid out left to right. A thin vertical stem at `x=5, y=8..55` announces a syllable; four optional rightward fins at `y=14,24,34,44` from `x=5..12` encode a 4-bit consonant index, least significant bit at the top. Root and particle consonants use the ordered table `k=0, l=1, m=2, n=3, r=4, s=5, t=6, v=7, d=8, y=9, p=10`. The vowel is a filled dot at `x=19` and `y=12,22,32,42,52` for `a,e,i,o,u` respectively. The dotted five-position ladder and four fins cannot be confused because they occupy different columns.

A lexical word is precisely **three cells**; a particle is one cell. A 3-unit gap separates cells inside one word; a 12-unit gap separates words. Reading cell by cell recovers each original consonant and vowel; sorting the syllables and looking up the root recovers its semantics. An optional Azure overhead band may visually signal the state, but **the band is not needed for decoding**—syllable order carries the information. Punctuation stays as conventional separate marks, with no alphabetic case distinction. Unique glyph mapping must be validated on all 55 admissible CV cells, including particles.

## 5. Barcode format and algorithm

Every lexical *form* is serializable as ASCII `AZ1|ID|s|r|surface` (e.g. `AZ1|I01|0|1|miroke`). IDs are one uppercase letter plus exactly two digits. `s ∈ {0,1}`, `r ∈ {0,1,2}`. The format has five fields delimited by literal `|`; no whitespace, Unicode, optional values, or opaque trailing fields are allowed. ID resolves to the canonical root in the signed-off 100-root registry; recomputing `transform(root,s,r)` **must match** the surface. A barcode text scanner returns this exact string; the AZ1 parser can reject corrupt/stale/mismatched data without relying on the barcode checksum alone.

**Code 128-B physical encoder:** Start-B symbol `104`, one data symbol per ASCII printable character with value `ord(character)-32`, checksum symbol `(104 + Σ(position × value)) mod 103` with positions starting at 1, then Stop symbol `106`. Each of Start, data, checksum uses 11 X modules and Stop uses 13. Draw alternating black bar and white space widths from the 107-entry Code 128 pattern table; include at least **10 X white quiet modules on both ends**. The offline SVG uses integer module widths, black bars on white, and 3 px per X by default. The strict encoder never silently switches subsets, because all AZ1 payloads are representable in B. The UI may frame the barcode in Azure but must not recolor the printed bars.

**Code 128-B module decoder:** strip ≥10 X blank quiet modules on each side, verify Stop and Start B, parse 11-module symbol blocks, reject unsupported switches, independently recompute the mod-103 checksum, recover ASCII text, then run the five-field AZ1 registry validator. This decoder is available in `azuravel_ref.py`. The browser provides text-payload decoding for USB/Bluetooth scanners that type the decoded string, not a guarantee of camera-based optical scanning. An actual independent optical scan check, if performed, is described in the validation report.

### One lexical bag, four physically distinct payloads

| Role | Surface | Payload | Checksum symbol |
| --- | --- | --- | --- |
| CONC | kemiro | `AZ1\|I01\|0\|0\|kemiro` | 25 |
| EVT | miroke | `AZ1\|I01\|0\|1\|miroke` | 93 |
| PAT | mikero | `AZ1\|I01\|1\|0\|mikero` | 22 |
| CTR | romike | `AZ1\|I01\|1\|2\|romike` | 91 |

The human-readable label printed **outside** the bars is `surface — concept/role — ID`, not encoded glyph art. Root, form, state, and canonical transformation history are recoverable from the payload. A physical barcode scanner will ordinarily output the payload text, not the supplemental label.

## 6. The exactly 100 registered roots

Forms displayed below: nominal concept `00`, plus all five alternative normal-form states `01`, `02`, `10`, `11`, `12`. The following lexicon is exhaustive for version AZ1; closed-class CV particles do not count as lexical roots. Each entry carries its own example.
### Identity (10 roots)

**I01 · kemiro** /keˈmiɾo/ — **selfhood**: continuity of a self. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `miroke` /miˈɾoke/ — `S0→L1` → **EVT**: selfhood manifests or is enacted.
- `rokemi` /ɾoˈkemi/ — `S0→L2` → **SRC**: an agent or source of selfhood.
- `mikero` /miˈkeɾo/ — `S1→L0` → **PAT**: a bearer or recipient affected by selfhood.
- `keromi` /keˈɾomi/ — `S1→L1` → **RES**: a result left by selfhood manifesting.
- `romike` /ɾoˈmike/ — `S1→L2` → **CTR**: selfhood is suppressed, reversed, or counteracted.
- **Example:** `ta kemiro mu miroke.` — *Selfhood will manifest.* Gloss: `AGT SELFHOOD.CONC FUT SELFHOOD.EVT`.

**I02 · lomati** /loˈmati/ — **person**: an individual being. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `matilo` /maˈtilo/ — `S0→L1` → **EVT**: person manifests or is enacted.
- `tiloma` /tiˈloma/ — `S0→L2` → **SRC**: an agent or source of person.
- `maloti` /maˈloti/ — `S1→L0` → **PAT**: a bearer or recipient affected by person.
- `lotima` /loˈtima/ — `S1→L1` → **RES**: a result left by person manifesting.
- `timalo` /tiˈmalo/ — `S1→L2` → **CTR**: person is suppressed, reversed, or counteracted.
- **Example:** `ta lomati mu matilo.` — *Person will manifest.* Gloss: `AGT PERSON.CONC FUT PERSON.EVT`.

**I03 · marote** /maˈɾote/ — **name**: identifying designation. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `rotema` /ɾoˈtema/ — `S0→L1` → **EVT**: name manifests or is enacted.
- `temaro` /teˈmaɾo/ — `S0→L2` → **SRC**: an agent or source of name.
- `romate` /ɾoˈmate/ — `S1→L0` → **PAT**: a bearer or recipient affected by name.
- `matero` /maˈteɾo/ — `S1→L1` → **RES**: a result left by name manifesting.
- `teroma` /teˈɾoma/ — `S1→L2` → **CTR**: name is suppressed, reversed, or counteracted.
- **Example:** `ta marote mu rotema.` — *Name will manifest.* Gloss: `AGT NAME.CONC FUT NAME.EVT`.

**I04 · kilera** /kiˈleɾa/ — **body**: embodied form. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `leraki` /leˈɾaki/ — `S0→L1` → **EVT**: body manifests or is enacted.
- `rakile` /ɾaˈkile/ — `S0→L2` → **SRC**: an agent or source of body.
- `lekira` /leˈkiɾa/ — `S1→L0` → **PAT**: a bearer or recipient affected by body.
- `kirale` /kiˈɾale/ — `S1→L1` → **RES**: a result left by body manifesting.
- `raleki` /ɾaˈleki/ — `S1→L2` → **CTR**: body is suppressed, reversed, or counteracted.
- **Example:** `ta kilera mu leraki.` — *Body will manifest.* Gloss: `AGT BODY.CONC FUT BODY.EVT`.

**I05 · kusuvu** /kuˈsuvu/ — **voice**: expressed vocal presence. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `suvuku` /suˈvuku/ — `S0→L1` → **EVT**: voice manifests or is enacted.
- `vukusu` /vuˈkusu/ — `S0→L2` → **SRC**: an agent or source of voice.
- `sukuvu` /suˈkuvu/ — `S1→L0` → **PAT**: a bearer or recipient affected by voice.
- `kuvusu` /kuˈvusu/ — `S1→L1` → **RES**: a result left by voice manifesting.
- `vusuku` /vuˈsuku/ — `S1→L2` → **CTR**: voice is suppressed, reversed, or counteracted.
- **Example:** `ta kusuvu mu suvuku.` — *Voice will manifest.* Gloss: `AGT VOICE.CONC FUT VOICE.EVT`.

**I06 · meniro** /meˈniɾo/ — **memory**: retained experience. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `nirome` /niˈɾome/ — `S0→L1` → **EVT**: memory manifests or is enacted.
- `romeni` /ɾoˈmeni/ — `S0→L2` → **SRC**: an agent or source of memory.
- `nimero` /niˈmeɾo/ — `S1→L0` → **PAT**: a bearer or recipient affected by memory.
- `meroni` /meˈɾoni/ — `S1→L1` → **RES**: a result left by memory manifesting.
- `ronime` /ɾoˈnime/ — `S1→L2` → **CTR**: memory is suppressed, reversed, or counteracted.
- **Example:** `ta meniro mu nirome.` — *Memory will manifest.* Gloss: `AGT MEMORY.CONC FUT MEMORY.EVT`.

**I07 · rosavi** /ɾoˈsavi/ — **face**: visible identity. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `saviro` /saˈviɾo/ — `S0→L1` → **EVT**: face manifests or is enacted.
- `virosa` /viˈɾosa/ — `S0→L2` → **SRC**: an agent or source of face.
- `sarovi` /saˈɾovi/ — `S1→L0` → **PAT**: a bearer or recipient affected by face.
- `rovisa` /ɾoˈvisa/ — `S1→L1` → **RES**: a result left by face manifesting.
- `visaro` /viˈsaɾo/ — `S1→L2` → **CTR**: face is suppressed, reversed, or counteracted.
- **Example:** `ta rosavi mu saviro.` — *Face will manifest.* Gloss: `AGT FACE.CONC FUT FACE.EVT`.

**I08 · kanove** /kaˈnove/ — **presence**: being perceptibly here. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `noveka` /noˈveka/ — `S0→L1` → **EVT**: presence manifests or is enacted.
- `vekano` /veˈkano/ — `S0→L2` → **SRC**: an agent or source of presence.
- `nokave` /noˈkave/ — `S1→L0` → **PAT**: a bearer or recipient affected by presence.
- `kaveno` /kaˈveno/ — `S1→L1` → **RES**: a result left by presence manifesting.
- `venoka` /veˈnoka/ — `S1→L2` → **CTR**: presence is suppressed, reversed, or counteracted.
- **Example:** `ta kanove mu noveka.` — *Presence will manifest.* Gloss: `AGT PRESENCE.CONC FUT PRESENCE.EVT`.

**I09 · lireta** /liˈɾeta/ — **boundary**: limit that differentiates an entity. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `retali` /ɾeˈtali/ — `S0→L1` → **EVT**: boundary manifests or is enacted.
- `talire` /taˈliɾe/ — `S0→L2` → **SRC**: an agent or source of boundary.
- `relita` /ɾeˈlita/ — `S1→L0` → **PAT**: a bearer or recipient affected by boundary.
- `litare` /liˈtaɾe/ — `S1→L1` → **RES**: a result left by boundary manifesting.
- `tareli` /taˈɾeli/ — `S1→L2` → **CTR**: boundary is suppressed, reversed, or counteracted.
- **Example:** `ta lireta mu retali.` — *Boundary will manifest.* Gloss: `AGT BOUNDARY.CONC FUT BOUNDARY.EVT`.

**I10 · nuruvu** /nuˈɾuvu/ — **belonging**: participation in a whole. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `ruvunu` /ɾuˈvunu/ — `S0→L1` → **EVT**: belonging manifests or is enacted.
- `vunuru` /vuˈnuɾu/ — `S0→L2` → **SRC**: an agent or source of belonging.
- `runuvu` /ɾuˈnuvu/ — `S1→L0` → **PAT**: a bearer or recipient affected by belonging.
- `nuvuru` /nuˈvuɾu/ — `S1→L1` → **RES**: a result left by belonging manifesting.
- `vurunu` /vuˈɾunu/ — `S1→L2` → **CTR**: belonging is suppressed, reversed, or counteracted.
- **Example:** `ta nuruvu mu ruvunu.` — *Belonging will manifest.* Gloss: `AGT BELONGING.CONC FUT BELONGING.EVT`.

### Relations (10 roots)

**R01 · kemito** /keˈmito/ — **bond**: durable connection. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `mitoke` /miˈtoke/ — `S0→L1` → **EVT**: bond manifests or is enacted.
- `tokemi` /toˈkemi/ — `S0→L2` → **SRC**: an agent or source of bond.
- `miketo` /miˈketo/ — `S1→L0` → **PAT**: a bearer or recipient affected by bond.
- `ketomi` /keˈtomi/ — `S1→L1` → **RES**: a result left by bond manifesting.
- `tomike` /toˈmike/ — `S1→L2` → **CTR**: bond is suppressed, reversed, or counteracted.
- **Example:** `ta kemito mu mitoke.` — *Bond will manifest.* Gloss: `AGT BOND.CONC FUT BOND.EVT`.

**R02 · lonari** /loˈnaɾi/ — **trust**: confidence in another. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `narilo` /naˈɾilo/ — `S0→L1` → **EVT**: trust manifests or is enacted.
- `rilona` /ɾiˈlona/ — `S0→L2` → **SRC**: an agent or source of trust.
- `nalori` /naˈloɾi/ — `S1→L0` → **PAT**: a bearer or recipient affected by trust.
- `lorina` /loˈɾina/ — `S1→L1` → **RES**: a result left by trust manifesting.
- `rinalo` /ɾiˈnalo/ — `S1→L2` → **CTR**: trust is suppressed, reversed, or counteracted.
- **Example:** `ta lonari mu narilo.` — *Trust will manifest.* Gloss: `AGT TRUST.CONC FUT TRUST.EVT`.

**R03 · masote** /maˈsote/ — **kinship**: felt familial relation. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `sotema` /soˈtema/ — `S0→L1` → **EVT**: kinship manifests or is enacted.
- `temaso` /teˈmaso/ — `S0→L2` → **SRC**: an agent or source of kinship.
- `somate` /soˈmate/ — `S1→L0` → **PAT**: a bearer or recipient affected by kinship.
- `mateso` /maˈteso/ — `S1→L1` → **RES**: a result left by kinship manifesting.
- `tesoma` /teˈsoma/ — `S1→L2` → **CTR**: kinship is suppressed, reversed, or counteracted.
- **Example:** `ta masote mu sotema.` — *Kinship will manifest.* Gloss: `AGT KINSHIP.CONC FUT KINSHIP.EVT`.

**R04 · kileta** /kiˈleta/ — **friendship**: mutual friendly relation. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `letaki` /leˈtaki/ — `S0→L1` → **EVT**: friendship manifests or is enacted.
- `takile` /taˈkile/ — `S0→L2` → **SRC**: an agent or source of friendship.
- `lekita` /leˈkita/ — `S1→L0` → **PAT**: a bearer or recipient affected by friendship.
- `kitale` /kiˈtale/ — `S1→L1` → **RES**: a result left by friendship manifesting.
- `taleki` /taˈleki/ — `S1→L2` → **CTR**: friendship is suppressed, reversed, or counteracted.
- **Example:** `ta kileta mu letaki.` — *Friendship will manifest.* Gloss: `AGT FRIENDSHIP.CONC FUT FRIENDSHIP.EVT`.

**R05 · lumunu** /luˈmunu/ — **care**: sustained concern. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `munulu` /muˈnulu/ — `S0→L1` → **EVT**: care manifests or is enacted.
- `nulumu` /nuˈlumu/ — `S0→L2` → **SRC**: an agent or source of care.
- `mulunu` /muˈlunu/ — `S1→L0` → **PAT**: a bearer or recipient affected by care.
- `lunumu` /luˈnumu/ — `S1→L1` → **RES**: a result left by care manifesting.
- `numulu` /nuˈmulu/ — `S1→L2` → **CTR**: care is suppressed, reversed, or counteracted.
- **Example:** `ta lumunu mu munulu.` — *Care will manifest.* Gloss: `AGT CARE.CONC FUT CARE.EVT`.

**R06 · menito** /meˈnito/ — **promise**: undertaken commitment. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `nitome` /niˈtome/ — `S0→L1` → **EVT**: promise manifests or is enacted.
- `tomeni` /toˈmeni/ — `S0→L2` → **SRC**: an agent or source of promise.
- `nimeto` /niˈmeto/ — `S1→L0` → **PAT**: a bearer or recipient affected by promise.
- `metoni` /meˈtoni/ — `S1→L1` → **RES**: a result left by promise manifesting.
- `tonime` /toˈnime/ — `S1→L2` → **CTR**: promise is suppressed, reversed, or counteracted.
- **Example:** `ta menito mu nitome.` — *Promise will manifest.* Gloss: `AGT PROMISE.CONC FUT PROMISE.EVT`.

**R07 · sotavi** /soˈtavi/ — **conflict**: opposition between parties. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `taviso` /taˈviso/ — `S0→L1` → **EVT**: conflict manifests or is enacted.
- `visota` /viˈsota/ — `S0→L2` → **SRC**: an agent or source of conflict.
- `tasovi` /taˈsovi/ — `S1→L0` → **PAT**: a bearer or recipient affected by conflict.
- `sovita` /soˈvita/ — `S1→L1` → **RES**: a result left by conflict manifesting.
- `vitaso` /viˈtaso/ — `S1→L2` → **CTR**: conflict is suppressed, reversed, or counteracted.
- **Example:** `ta sotavi mu taviso.` — *Conflict will manifest.* Gloss: `AGT CONFLICT.CONC FUT CONFLICT.EVT`.

**R08 · karote** /kaˈɾote/ — **meeting**: encounter in a place or moment. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `roteka` /ɾoˈteka/ — `S0→L1` → **EVT**: meeting manifests or is enacted.
- `tekaro` /teˈkaɾo/ — `S0→L2` → **SRC**: an agent or source of meeting.
- `rokate` /ɾoˈkate/ — `S1→L0` → **PAT**: a bearer or recipient affected by meeting.
- `katero` /kaˈteɾo/ — `S1→L1` → **RES**: a result left by meeting manifesting.
- `teroka` /teˈɾoka/ — `S1→L2` → **CTR**: meeting is suppressed, reversed, or counteracted.
- **Example:** `ta karote mu roteka.` — *Meeting will manifest.* Gloss: `AGT MEETING.CONC FUT MEETING.EVT`.

**R09 · liseta** /liˈseta/ — **greeting**: acknowledgment of another. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `setali` /seˈtali/ — `S0→L1` → **EVT**: greeting manifests or is enacted.
- `talise` /taˈlise/ — `S0→L2` → **SRC**: an agent or source of greeting.
- `selita` /seˈlita/ — `S1→L0` → **PAT**: a bearer or recipient affected by greeting.
- `litase` /liˈtase/ — `S1→L1` → **RES**: a result left by greeting manifesting.
- `taseli` /taˈseli/ — `S1→L2` → **CTR**: greeting is suppressed, reversed, or counteracted.
- **Example:** `ta liseta mu setali.` — *Greeting will manifest.* Gloss: `AGT GREETING.CONC FUT GREETING.EVT`.

**R10 · nusuvu** /nuˈsuvu/ — **exchange**: reciprocal giving or transfer. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `suvunu` /suˈvunu/ — `S0→L1` → **EVT**: exchange manifests or is enacted.
- `vunusu` /vuˈnusu/ — `S0→L2` → **SRC**: an agent or source of exchange.
- `sunuvu` /suˈnuvu/ — `S1→L0` → **PAT**: a bearer or recipient affected by exchange.
- `nuvusu` /nuˈvusu/ — `S1→L1` → **RES**: a result left by exchange manifesting.
- `vusunu` /vuˈsunu/ — `S1→L2` → **CTR**: exchange is suppressed, reversed, or counteracted.
- **Example:** `ta nusuvu mu suvunu.` — *Exchange will manifest.* Gloss: `AGT EXCHANGE.CONC FUT EXCHANGE.EVT`.

### Movement (10 roots)

**M01 · keniro** /keˈniɾo/ — **motion**: change of position. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `niroke` /niˈɾoke/ — `S0→L1` → **EVT**: motion manifests or is enacted.
- `rokeni` /ɾoˈkeni/ — `S0→L2` → **SRC**: an agent or source of motion.
- `nikero` /niˈkeɾo/ — `S1→L0` → **PAT**: a bearer or recipient affected by motion.
- `keroni` /keˈɾoni/ — `S1→L1` → **RES**: a result left by motion manifesting.
- `ronike` /ɾoˈnike/ — `S1→L2` → **CTR**: motion is suppressed, reversed, or counteracted.
- **Example:** `ta keniro mu niroke.` — *Motion will manifest.* Gloss: `AGT MOTION.CONC FUT MOTION.EVT`.

**M02 · lonati** /loˈnati/ — **journey**: sustained travel. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `natilo` /naˈtilo/ — `S0→L1` → **EVT**: journey manifests or is enacted.
- `tilona` /tiˈlona/ — `S0→L2` → **SRC**: an agent or source of journey.
- `naloti` /naˈloti/ — `S1→L0` → **PAT**: a bearer or recipient affected by journey.
- `lotina` /loˈtina/ — `S1→L1` → **RES**: a result left by journey manifesting.
- `tinalo` /tiˈnalo/ — `S1→L2` → **CTR**: journey is suppressed, reversed, or counteracted.
- **Example:** `ta lonati mu natilo.` — *Journey will manifest.* Gloss: `AGT JOURNEY.CONC FUT JOURNEY.EVT`.

**M03 · matove** /maˈtove/ — **arrival**: reaching a destination. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `tovema` /toˈvema/ — `S0→L1` → **EVT**: arrival manifests or is enacted.
- `vemato` /veˈmato/ — `S0→L2` → **SRC**: an agent or source of arrival.
- `tomave` /toˈmave/ — `S1→L0` → **PAT**: a bearer or recipient affected by arrival.
- `maveto` /maˈveto/ — `S1→L1` → **RES**: a result left by arrival manifesting.
- `vetoma` /veˈtoma/ — `S1→L2` → **CTR**: arrival is suppressed, reversed, or counteracted.
- **Example:** `ta matove mu tovema.` — *Arrival will manifest.* Gloss: `AGT ARRIVAL.CONC FUT ARRIVAL.EVT`.

**M04 · kimena** /kiˈmena/ — **departure**: leaving a position. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `menaki` /meˈnaki/ — `S0→L1` → **EVT**: departure manifests or is enacted.
- `nakime` /naˈkime/ — `S0→L2` → **SRC**: an agent or source of departure.
- `mekina` /meˈkina/ — `S1→L0` → **PAT**: a bearer or recipient affected by departure.
- `kiname` /kiˈname/ — `S1→L1` → **RES**: a result left by departure manifesting.
- `nameki` /naˈmeki/ — `S1→L2` → **CTR**: departure is suppressed, reversed, or counteracted.
- **Example:** `ta kimena mu menaki.` — *Departure will manifest.* Gloss: `AGT DEPARTURE.CONC FUT DEPARTURE.EVT`.

**M05 · lumusu** /luˈmusu/ — **ascent**: upward movement. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `musulu` /muˈsulu/ — `S0→L1` → **EVT**: ascent manifests or is enacted.
- `sulumu` /suˈlumu/ — `S0→L2` → **SRC**: an agent or source of ascent.
- `mulusu` /muˈlusu/ — `S1→L0` → **PAT**: a bearer or recipient affected by ascent.
- `lusumu` /luˈsumu/ — `S1→L1` → **RES**: a result left by ascent manifesting.
- `sumulu` /suˈmulu/ — `S1→L2` → **CTR**: ascent is suppressed, reversed, or counteracted.
- **Example:** `ta lumusu mu musulu.` — *Ascent will manifest.* Gloss: `AGT ASCENT.CONC FUT ASCENT.EVT`.

**M06 · meriso** /meˈɾiso/ — **descent**: downward movement. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `risome` /ɾiˈsome/ — `S0→L1` → **EVT**: descent manifests or is enacted.
- `someri` /soˈmeɾi/ — `S0→L2` → **SRC**: an agent or source of descent.
- `rimeso` /ɾiˈmeso/ — `S1→L0` → **PAT**: a bearer or recipient affected by descent.
- `mesori` /meˈsoɾi/ — `S1→L1` → **RES**: a result left by descent manifesting.
- `sorime` /soˈɾime/ — `S1→L2` → **CTR**: descent is suppressed, reversed, or counteracted.
- **Example:** `ta meriso mu risome.` — *Descent will manifest.* Gloss: `AGT DESCENT.CONC FUT DESCENT.EVT`.

**M07 · kolani** /koˈlani/ — **turning**: change of orientation. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `laniko` /laˈniko/ — `S0→L1` → **EVT**: turning manifests or is enacted.
- `nikola` /niˈkola/ — `S0→L2` → **SRC**: an agent or source of turning.
- `lakoni` /laˈkoni/ — `S1→L0` → **PAT**: a bearer or recipient affected by turning.
- `konila` /koˈnila/ — `S1→L1` → **RES**: a result left by turning manifesting.
- `nilako` /niˈlako/ — `S1→L2` → **CTR**: turning is suppressed, reversed, or counteracted.
- **Example:** `ta kolani mu laniko.` — *Turning will manifest.* Gloss: `AGT TURNING.CONC FUT TURNING.EVT`.

**M08 · kasote** /kaˈsote/ — **pursuit**: movement after a goal. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `soteka` /soˈteka/ — `S0→L1` → **EVT**: pursuit manifests or is enacted.
- `tekaso` /teˈkaso/ — `S0→L2` → **SRC**: an agent or source of pursuit.
- `sokate` /soˈkate/ — `S1→L0` → **PAT**: a bearer or recipient affected by pursuit.
- `kateso` /kaˈteso/ — `S1→L1` → **RES**: a result left by pursuit manifesting.
- `tesoka` /teˈsoka/ — `S1→L2` → **CTR**: pursuit is suppressed, reversed, or counteracted.
- **Example:** `ta kasote mu soteka.` — *Pursuit will manifest.* Gloss: `AGT PURSUIT.CONC FUT PURSUIT.EVT`.

**M09 · liteva** /liˈteva/ — **return**: coming back. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `tevali` /teˈvali/ — `S0→L1` → **EVT**: return manifests or is enacted.
- `valite` /vaˈlite/ — `S0→L2` → **SRC**: an agent or source of return.
- `teliva` /teˈliva/ — `S1→L0` → **PAT**: a bearer or recipient affected by return.
- `livate` /liˈvate/ — `S1→L1` → **RES**: a result left by return manifesting.
- `vateli` /vaˈteli/ — `S1→L2` → **CTR**: return is suppressed, reversed, or counteracted.
- **Example:** `ta liteva mu tevali.` — *Return will manifest.* Gloss: `AGT RETURN.CONC FUT RETURN.EVT`.

**M10 · rusutu** /ɾuˈsutu/ — **crossing**: passage across a boundary. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `suturu` /suˈtuɾu/ — `S0→L1` → **EVT**: crossing manifests or is enacted.
- `turusu` /tuˈɾusu/ — `S0→L2` → **SRC**: an agent or source of crossing.
- `surutu` /suˈɾutu/ — `S1→L0` → **PAT**: a bearer or recipient affected by crossing.
- `rutusu` /ɾuˈtusu/ — `S1→L1` → **RES**: a result left by crossing manifesting.
- `tusuru` /tuˈsuɾu/ — `S1→L2` → **CTR**: crossing is suppressed, reversed, or counteracted.
- **Example:** `ta rusutu mu suturu.` — *Crossing will manifest.* Gloss: `AGT CROSSING.CONC FUT CROSSING.EVT`.

### Space (10 roots)

**S01 · kenito** /keˈnito/ — **place**: located site. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `nitoke` /niˈtoke/ — `S0→L1` → **EVT**: place manifests or is enacted.
- `tokeni` /toˈkeni/ — `S0→L2` → **SRC**: an agent or source of place.
- `niketo` /niˈketo/ — `S1→L0` → **PAT**: a bearer or recipient affected by place.
- `ketoni` /keˈtoni/ — `S1→L1` → **RES**: a result left by place manifesting.
- `tonike` /toˈnike/ — `S1→L2` → **CTR**: place is suppressed, reversed, or counteracted.
- **Example:** `ta kenito mu nitoke.` — *Place will manifest.* Gloss: `AGT PLACE.CONC FUT PLACE.EVT`.

**S02 · lorasi** /loˈɾasi/ — **home**: dwelling of belonging. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `rasilo` /ɾaˈsilo/ — `S0→L1` → **EVT**: home manifests or is enacted.
- `silora` /siˈloɾa/ — `S0→L2` → **SRC**: an agent or source of home.
- `ralosi` /ɾaˈlosi/ — `S1→L0` → **PAT**: a bearer or recipient affected by home.
- `losira` /loˈsiɾa/ — `S1→L1` → **RES**: a result left by home manifesting.
- `siralo` /siˈɾalo/ — `S1→L2` → **CTR**: home is suppressed, reversed, or counteracted.
- **Example:** `ta lorasi mu rasilo.` — *Home will manifest.* Gloss: `AGT HOME.CONC FUT HOME.EVT`.

**S03 · narote** /naˈɾote/ — **distance**: spatial separation. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `rotena` /ɾoˈtena/ — `S0→L1` → **EVT**: distance manifests or is enacted.
- `tenaro` /teˈnaɾo/ — `S0→L2` → **SRC**: an agent or source of distance.
- `ronate` /ɾoˈnate/ — `S1→L0` → **PAT**: a bearer or recipient affected by distance.
- `natero` /naˈteɾo/ — `S1→L1` → **RES**: a result left by distance manifesting.
- `terona` /teˈɾona/ — `S1→L2` → **CTR**: distance is suppressed, reversed, or counteracted.
- **Example:** `ta narote mu rotena.` — *Distance will manifest.* Gloss: `AGT DISTANCE.CONC FUT DISTANCE.EVT`.

**S04 · kimesa** /kiˈmesa/ — **path**: route through space. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `mesaki` /meˈsaki/ — `S0→L1` → **EVT**: path manifests or is enacted.
- `sakime` /saˈkime/ — `S0→L2` → **SRC**: an agent or source of path.
- `mekisa` /meˈkisa/ — `S1→L0` → **PAT**: a bearer or recipient affected by path.
- `kisame` /kiˈsame/ — `S1→L1` → **RES**: a result left by path manifesting.
- `sameki` /saˈmeki/ — `S1→L2` → **CTR**: path is suppressed, reversed, or counteracted.
- **Example:** `ta kimesa mu mesaki.` — *Path will manifest.* Gloss: `AGT PATH.CONC FUT PATH.EVT`.

**S05 · lumuvu** /luˈmuvu/ — **center**: relational middle. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `muvulu` /muˈvulu/ — `S0→L1` → **EVT**: center manifests or is enacted.
- `vulumu` /vuˈlumu/ — `S0→L2` → **SRC**: an agent or source of center.
- `muluvu` /muˈluvu/ — `S1→L0` → **PAT**: a bearer or recipient affected by center.
- `luvumu` /luˈvumu/ — `S1→L1` → **RES**: a result left by center manifesting.
- `vumulu` /vuˈmulu/ — `S1→L2` → **CTR**: center is suppressed, reversed, or counteracted.
- **Example:** `ta lumuvu mu muvulu.` — *Center will manifest.* Gloss: `AGT CENTER.CONC FUT CENTER.EVT`.

**S06 · merivo** /meˈɾivo/ — **edge**: spatial limit. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `rivome` /ɾiˈvome/ — `S0→L1` → **EVT**: edge manifests or is enacted.
- `vomeri` /voˈmeɾi/ — `S0→L2` → **SRC**: an agent or source of edge.
- `rimevo` /ɾiˈmevo/ — `S1→L0` → **PAT**: a bearer or recipient affected by edge.
- `mevori` /meˈvoɾi/ — `S1→L1` → **RES**: a result left by edge manifesting.
- `vorime` /voˈɾime/ — `S1→L2` → **CTR**: edge is suppressed, reversed, or counteracted.
- **Example:** `ta merivo mu rivome.` — *Edge will manifest.* Gloss: `AGT EDGE.CONC FUT EDGE.EVT`.

**S07 · kolasi** /koˈlasi/ — **shelter**: protective enclosure. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `lasiko` /laˈsiko/ — `S0→L1` → **EVT**: shelter manifests or is enacted.
- `sikola` /siˈkola/ — `S0→L2` → **SRC**: an agent or source of shelter.
- `lakosi` /laˈkosi/ — `S1→L0` → **PAT**: a bearer or recipient affected by shelter.
- `kosila` /koˈsila/ — `S1→L1` → **RES**: a result left by shelter manifesting.
- `silako` /siˈlako/ — `S1→L2` → **CTR**: shelter is suppressed, reversed, or counteracted.
- **Example:** `ta kolasi mu lasiko.` — *Shelter will manifest.* Gloss: `AGT SHELTER.CONC FUT SHELTER.EVT`.

**S08 · katove** /kaˈtove/ — **doorway**: threshold permitting entry. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `toveka` /toˈveka/ — `S0→L1` → **EVT**: doorway manifests or is enacted.
- `vekato` /veˈkato/ — `S0→L2` → **SRC**: an agent or source of doorway.
- `tokave` /toˈkave/ — `S1→L0` → **PAT**: a bearer or recipient affected by doorway.
- `kaveto` /kaˈveto/ — `S1→L1` → **RES**: a result left by doorway manifesting.
- `vetoka` /veˈtoka/ — `S1→L2` → **CTR**: doorway is suppressed, reversed, or counteracted.
- **Example:** `ta katove mu toveka.` — *Doorway will manifest.* Gloss: `AGT DOORWAY.CONC FUT DOORWAY.EVT`.

**S09 · minesa** /miˈnesa/ — **horizon**: apparent spatial boundary. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `nesami` /neˈsami/ — `S0→L1` → **EVT**: horizon manifests or is enacted.
- `samine` /saˈmine/ — `S0→L2` → **SRC**: an agent or source of horizon.
- `nemisa` /neˈmisa/ — `S1→L0` → **PAT**: a bearer or recipient affected by horizon.
- `misane` /miˈsane/ — `S1→L1` → **RES**: a result left by horizon manifesting.
- `sanemi` /saˈnemi/ — `S1→L2` → **CTR**: horizon is suppressed, reversed, or counteracted.
- **Example:** `ta minesa mu nesami.` — *Horizon will manifest.* Gloss: `AGT HORIZON.CONC FUT HORIZON.EVT`.

**S10 · rutuvu** /ɾuˈtuvu/ — **direction**: orientation of motion. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `tuvuru` /tuˈvuɾu/ — `S0→L1` → **EVT**: direction manifests or is enacted.
- `vurutu` /vuˈɾutu/ — `S0→L2` → **SRC**: an agent or source of direction.
- `turuvu` /tuˈɾuvu/ — `S1→L0` → **PAT**: a bearer or recipient affected by direction.
- `ruvutu` /ɾuˈvutu/ — `S1→L1` → **RES**: a result left by direction manifesting.
- `vuturu` /vuˈtuɾu/ — `S1→L2` → **CTR**: direction is suppressed, reversed, or counteracted.
- **Example:** `ta rutuvu mu tuvuru.` — *Direction will manifest.* Gloss: `AGT DIRECTION.CONC FUT DIRECTION.EVT`.

### Time (10 roots)

**T01 · keriso** /keˈɾiso/ — **moment**: brief temporal point. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `risoke` /ɾiˈsoke/ — `S0→L1` → **EVT**: moment manifests or is enacted.
- `sokeri` /soˈkeɾi/ — `S0→L2` → **SRC**: an agent or source of moment.
- `rikeso` /ɾiˈkeso/ — `S1→L0` → **PAT**: a bearer or recipient affected by moment.
- `kesori` /keˈsoɾi/ — `S1→L1` → **RES**: a result left by moment manifesting.
- `sorike` /soˈɾike/ — `S1→L2` → **CTR**: moment is suppressed, reversed, or counteracted.
- **Example:** `ta keriso mu risoke.` — *Moment will manifest.* Gloss: `AGT MOMENT.CONC FUT MOMENT.EVT`.

**T02 · loravi** /loˈɾavi/ — **duration**: extent of elapsed time. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `ravilo` /ɾaˈvilo/ — `S0→L1` → **EVT**: duration manifests or is enacted.
- `vilora` /viˈloɾa/ — `S0→L2` → **SRC**: an agent or source of duration.
- `ralovi` /ɾaˈlovi/ — `S1→L0` → **PAT**: a bearer or recipient affected by duration.
- `lovira` /loˈviɾa/ — `S1→L1` → **RES**: a result left by duration manifesting.
- `viralo` /viˈɾalo/ — `S1→L2` → **CTR**: duration is suppressed, reversed, or counteracted.
- **Example:** `ta loravi mu ravilo.` — *Duration will manifest.* Gloss: `AGT DURATION.CONC FUT DURATION.EVT`.

**T03 · nasote** /naˈsote/ — **beginning**: first phase. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `sotena` /soˈtena/ — `S0→L1` → **EVT**: beginning manifests or is enacted.
- `tenaso` /teˈnaso/ — `S0→L2` → **SRC**: an agent or source of beginning.
- `sonate` /soˈnate/ — `S1→L0` → **PAT**: a bearer or recipient affected by beginning.
- `nateso` /naˈteso/ — `S1→L1` → **RES**: a result left by beginning manifesting.
- `tesona` /teˈsona/ — `S1→L2` → **CTR**: beginning is suppressed, reversed, or counteracted.
- **Example:** `ta nasote mu sotena.` — *Beginning will manifest.* Gloss: `AGT BEGINNING.CONC FUT BEGINNING.EVT`.

**T04 · kimeva** /kiˈmeva/ — **ending**: terminal phase. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `mevaki` /meˈvaki/ — `S0→L1` → **EVT**: ending manifests or is enacted.
- `vakime` /vaˈkime/ — `S0→L2` → **SRC**: an agent or source of ending.
- `mekiva` /meˈkiva/ — `S1→L0` → **PAT**: a bearer or recipient affected by ending.
- `kivame` /kiˈvame/ — `S1→L1` → **RES**: a result left by ending manifesting.
- `vameki` /vaˈmeki/ — `S1→L2` → **CTR**: ending is suppressed, reversed, or counteracted.
- **Example:** `ta kimeva mu mevaki.` — *Ending will manifest.* Gloss: `AGT ENDING.CONC FUT ENDING.EVT`.

**T05 · lunusu** /luˈnusu/ — **cycle**: repeated sequence. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `nusulu` /nuˈsulu/ — `S0→L1` → **EVT**: cycle manifests or is enacted.
- `sulunu` /suˈlunu/ — `S0→L2` → **SRC**: an agent or source of cycle.
- `nulusu` /nuˈlusu/ — `S1→L0` → **PAT**: a bearer or recipient affected by cycle.
- `lusunu` /luˈsunu/ — `S1→L1` → **RES**: a result left by cycle manifesting.
- `sunulu` /suˈnulu/ — `S1→L2` → **CTR**: cycle is suppressed, reversed, or counteracted.
- **Example:** `ta lunusu mu nusulu.` — *Cycle will manifest.* Gloss: `AGT CYCLE.CONC FUT CYCLE.EVT`.

**T06 · mesivo** /meˈsivo/ — **dawn**: emergence of day. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `sivome` /siˈvome/ — `S0→L1` → **EVT**: dawn manifests or is enacted.
- `vomesi` /voˈmesi/ — `S0→L2` → **SRC**: an agent or source of dawn.
- `simevo` /siˈmevo/ — `S1→L0` → **PAT**: a bearer or recipient affected by dawn.
- `mevosi` /meˈvosi/ — `S1→L1` → **RES**: a result left by dawn manifesting.
- `vosime` /voˈsime/ — `S1→L2` → **CTR**: dawn is suppressed, reversed, or counteracted.
- **Example:** `ta mesivo mu sivome.` — *Dawn will manifest.* Gloss: `AGT DAWN.CONC FUT DAWN.EVT`.

**T07 · kolavi** /koˈlavi/ — **dusk**: fading of day. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `laviko` /laˈviko/ — `S0→L1` → **EVT**: dusk manifests or is enacted.
- `vikola` /viˈkola/ — `S0→L2` → **SRC**: an agent or source of dusk.
- `lakovi` /laˈkovi/ — `S1→L0` → **PAT**: a bearer or recipient affected by dusk.
- `kovila` /koˈvila/ — `S1→L1` → **RES**: a result left by dusk manifesting.
- `vilako` /viˈlako/ — `S1→L2` → **CTR**: dusk is suppressed, reversed, or counteracted.
- **Example:** `ta kolavi mu laviko.` — *Dusk will manifest.* Gloss: `AGT DUSK.CONC FUT DUSK.EVT`.

**T08 · lamore** /laˈmoɾe/ — **past**: time already elapsed. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `morela` /moˈɾela/ — `S0→L1` → **EVT**: past manifests or is enacted.
- `relamo` /ɾeˈlamo/ — `S0→L2` → **SRC**: an agent or source of past.
- `molare` /moˈlaɾe/ — `S1→L0` → **PAT**: a bearer or recipient affected by past.
- `laremo` /laˈɾemo/ — `S1→L1` → **RES**: a result left by past manifesting.
- `remola` /ɾeˈmola/ — `S1→L2` → **CTR**: past is suppressed, reversed, or counteracted.
- **Example:** `ta lamore mu morela.` — *Past will manifest.* Gloss: `AGT PAST.CONC FUT PAST.EVT`.

**T09 · mineva** /miˈneva/ — **future**: time yet to come. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `nevami` /neˈvami/ — `S0→L1` → **EVT**: future manifests or is enacted.
- `vamine` /vaˈmine/ — `S0→L2` → **SRC**: an agent or source of future.
- `nemiva` /neˈmiva/ — `S1→L0` → **PAT**: a bearer or recipient affected by future.
- `mivane` /miˈvane/ — `S1→L1` → **RES**: a result left by future manifesting.
- `vanemi` /vaˈnemi/ — `S1→L2` → **CTR**: future is suppressed, reversed, or counteracted.
- **Example:** `ta mineva mu nevami.` — *Future will manifest.* Gloss: `AGT FUTURE.CONC FUT FUTURE.EVT`.

**T10 · kulumu** /kuˈlumu/ — **waiting**: delayed action or anticipation. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `lumuku` /luˈmuku/ — `S0→L1` → **EVT**: waiting manifests or is enacted.
- `mukulu` /muˈkulu/ — `S0→L2` → **SRC**: an agent or source of waiting.
- `lukumu` /luˈkumu/ — `S1→L0` → **PAT**: a bearer or recipient affected by waiting.
- `kumulu` /kuˈmulu/ — `S1→L1` → **RES**: a result left by waiting manifesting.
- `muluku` /muˈluku/ — `S1→L2` → **CTR**: waiting is suppressed, reversed, or counteracted.
- **Example:** `ta kulumu mu lumuku.` — *Waiting will manifest.* Gloss: `AGT WAITING.CONC FUT WAITING.EVT`.

### Creation (10 roots)

**C01 · kerivo** /keˈɾivo/ — **creation**: bringing into existence. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `rivoke` /ɾiˈvoke/ — `S0→L1` → **EVT**: creation manifests or is enacted.
- `vokeri` /voˈkeɾi/ — `S0→L2` → **SRC**: an agent or source of creation.
- `rikevo` /ɾiˈkevo/ — `S1→L0` → **PAT**: a bearer or recipient affected by creation.
- `kevori` /keˈvoɾi/ — `S1→L1` → **RES**: a result left by creation manifesting.
- `vorike` /voˈɾike/ — `S1→L2` → **CTR**: creation is suppressed, reversed, or counteracted.
- **Example:** `ta kerivo mu rivoke.` — *Creation will manifest.* Gloss: `AGT CREATION.CONC FUT CREATION.EVT`.

**C02 · losavi** /loˈsavi/ — **shaping**: giving form. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `savilo` /saˈvilo/ — `S0→L1` → **EVT**: shaping manifests or is enacted.
- `vilosa` /viˈlosa/ — `S0→L2` → **SRC**: an agent or source of shaping.
- `salovi` /saˈlovi/ — `S1→L0` → **PAT**: a bearer or recipient affected by shaping.
- `lovisa` /loˈvisa/ — `S1→L1` → **RES**: a result left by shaping manifesting.
- `visalo` /viˈsalo/ — `S1→L2` → **CTR**: shaping is suppressed, reversed, or counteracted.
- **Example:** `ta losavi mu savilo.` — *Shaping will manifest.* Gloss: `AGT SHAPING.CONC FUT SHAPING.EVT`.

**C03 · natove** /naˈtove/ — **pattern**: repeatable arrangement. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `tovena` /toˈvena/ — `S0→L1` → **EVT**: pattern manifests or is enacted.
- `venato` /veˈnato/ — `S0→L2` → **SRC**: an agent or source of pattern.
- `tonave` /toˈnave/ — `S1→L0` → **PAT**: a bearer or recipient affected by pattern.
- `naveto` /naˈveto/ — `S1→L1` → **RES**: a result left by pattern manifesting.
- `vetona` /veˈtona/ — `S1→L2` → **CTR**: pattern is suppressed, reversed, or counteracted.
- **Example:** `ta natove mu tovena.` — *Pattern will manifest.* Gloss: `AGT PATTERN.CONC FUT PATTERN.EVT`.

**C04 · kinesa** /kiˈnesa/ — **craft**: skilled making. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `nesaki` /neˈsaki/ — `S0→L1` → **EVT**: craft manifests or is enacted.
- `sakine` /saˈkine/ — `S0→L2` → **SRC**: an agent or source of craft.
- `nekisa` /neˈkisa/ — `S1→L0` → **PAT**: a bearer or recipient affected by craft.
- `kisane` /kiˈsane/ — `S1→L1` → **RES**: a result left by craft manifesting.
- `saneki` /saˈneki/ — `S1→L2` → **CTR**: craft is suppressed, reversed, or counteracted.
- **Example:** `ta kinesa mu nesaki.` — *Craft will manifest.* Gloss: `AGT CRAFT.CONC FUT CRAFT.EVT`.

**C05 · lunuvu** /luˈnuvu/ — **story**: structured narrative. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `nuvulu` /nuˈvulu/ — `S0→L1` → **EVT**: story manifests or is enacted.
- `vulunu` /vuˈlunu/ — `S0→L2` → **SRC**: an agent or source of story.
- `nuluvu` /nuˈluvu/ — `S1→L0` → **PAT**: a bearer or recipient affected by story.
- `luvunu` /luˈvunu/ — `S1→L1` → **RES**: a result left by story manifesting.
- `vunulu` /vuˈnulu/ — `S1→L2` → **CTR**: story is suppressed, reversed, or counteracted.
- **Example:** `ta lunuvu mu nuvulu.` — *Story will manifest.* Gloss: `AGT STORY.CONC FUT STORY.EVT`.

**C06 · neriso** /neˈɾiso/ — **song**: ordered voiced music. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `risone` /ɾiˈsone/ — `S0→L1` → **EVT**: song manifests or is enacted.
- `soneri` /soˈneɾi/ — `S0→L2` → **SRC**: an agent or source of song.
- `rineso` /ɾiˈneso/ — `S1→L0` → **PAT**: a bearer or recipient affected by song.
- `nesori` /neˈsoɾi/ — `S1→L1` → **RES**: a result left by song manifesting.
- `sorine` /soˈɾine/ — `S1→L2` → **CTR**: song is suppressed, reversed, or counteracted.
- **Example:** `ta neriso mu risone.` — *Song will manifest.* Gloss: `AGT SONG.CONC FUT SONG.EVT`.

**C07 · komari** /koˈmaɾi/ — **light**: visible illumination. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `mariko` /maˈɾiko/ — `S0→L1` → **EVT**: light manifests or is enacted.
- `rikoma` /ɾiˈkoma/ — `S0→L2` → **SRC**: an agent or source of light.
- `makori` /maˈkoɾi/ — `S1→L0` → **PAT**: a bearer or recipient affected by light.
- `korima` /koˈɾima/ — `S1→L1` → **RES**: a result left by light manifesting.
- `rimako` /ɾiˈmako/ — `S1→L2` → **CTR**: light is suppressed, reversed, or counteracted.
- **Example:** `ta komari mu mariko.` — *Light will manifest.* Gloss: `AGT LIGHT.CONC FUT LIGHT.EVT`.

**C08 · lamote** /laˈmote/ — **structure**: organized assembly. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `motela` /moˈtela/ — `S0→L1` → **EVT**: structure manifests or is enacted.
- `telamo` /teˈlamo/ — `S0→L2` → **SRC**: an agent or source of structure.
- `molate` /moˈlate/ — `S1→L0` → **PAT**: a bearer or recipient affected by structure.
- `latemo` /laˈtemo/ — `S1→L1` → **RES**: a result left by structure manifesting.
- `temola` /teˈmola/ — `S1→L2` → **CTR**: structure is suppressed, reversed, or counteracted.
- **Example:** `ta lamote mu motela.` — *Structure will manifest.* Gloss: `AGT STRUCTURE.CONC FUT STRUCTURE.EVT`.

**C09 · mireta** /miˈɾeta/ — **tool**: instrument of action. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `retami` /ɾeˈtami/ — `S0→L1` → **EVT**: tool manifests or is enacted.
- `tamire` /taˈmiɾe/ — `S0→L2` → **SRC**: an agent or source of tool.
- `remita` /ɾeˈmita/ — `S1→L0` → **PAT**: a bearer or recipient affected by tool.
- `mitare` /miˈtaɾe/ — `S1→L1` → **RES**: a result left by tool manifesting.
- `taremi` /taˈɾemi/ — `S1→L2` → **CTR**: tool is suppressed, reversed, or counteracted.
- **Example:** `ta mireta mu retami.` — *Tool will manifest.* Gloss: `AGT TOOL.CONC FUT TOOL.EVT`.

**C10 · kuluru** /kuˈluɾu/ — **invention**: novel construction. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `luruku` /luˈɾuku/ — `S0→L1` → **EVT**: invention manifests or is enacted.
- `rukulu` /ɾuˈkulu/ — `S0→L2` → **SRC**: an agent or source of invention.
- `lukuru` /luˈkuɾu/ — `S1→L0` → **PAT**: a bearer or recipient affected by invention.
- `kurulu` /kuˈɾulu/ — `S1→L1` → **RES**: a result left by invention manifesting.
- `ruluku` /ɾuˈluku/ — `S1→L2` → **CTR**: invention is suppressed, reversed, or counteracted.
- **Example:** `ta kuluru mu luruku.` — *Invention will manifest.* Gloss: `AGT INVENTION.CONC FUT INVENTION.EVT`.

### Knowledge (10 roots)

**K01 · kesivo** /keˈsivo/ — **knowledge**: held understanding. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `sivoke` /siˈvoke/ — `S0→L1` → **EVT**: knowledge manifests or is enacted.
- `vokesi` /voˈkesi/ — `S0→L2` → **SRC**: an agent or source of knowledge.
- `sikevo` /siˈkevo/ — `S1→L0` → **PAT**: a bearer or recipient affected by knowledge.
- `kevosi` /keˈvosi/ — `S1→L1` → **RES**: a result left by knowledge manifesting.
- `vosike` /voˈsike/ — `S1→L2` → **CTR**: knowledge is suppressed, reversed, or counteracted.
- **Example:** `ta kesivo mu sivoke.` — *Knowledge will manifest.* Gloss: `AGT KNOWLEDGE.CONC FUT KNOWLEDGE.EVT`.

**K02 · monari** /moˈnaɾi/ — **inquiry**: search for an answer. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `narimo` /naˈɾimo/ — `S0→L1` → **EVT**: inquiry manifests or is enacted.
- `rimona` /ɾiˈmona/ — `S0→L2` → **SRC**: an agent or source of inquiry.
- `namori` /naˈmoɾi/ — `S1→L0` → **PAT**: a bearer or recipient affected by inquiry.
- `morina` /moˈɾina/ — `S1→L1` → **RES**: a result left by inquiry manifesting.
- `rinamo` /ɾiˈnamo/ — `S1→L2` → **CTR**: inquiry is suppressed, reversed, or counteracted.
- **Example:** `ta monari mu narimo.` — *Inquiry will manifest.* Gloss: `AGT INQUIRY.CONC FUT INQUIRY.EVT`.

**K03 · rasove** /ɾaˈsove/ — **evidence**: support for a claim. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `sovera` /soˈveɾa/ — `S0→L1` → **EVT**: evidence manifests or is enacted.
- `veraso` /veˈɾaso/ — `S0→L2` → **SRC**: an agent or source of evidence.
- `sorave` /soˈɾave/ — `S1→L0` → **PAT**: a bearer or recipient affected by evidence.
- `raveso` /ɾaˈveso/ — `S1→L1` → **RES**: a result left by evidence manifesting.
- `vesora` /veˈsoɾa/ — `S1→L2` → **CTR**: evidence is suppressed, reversed, or counteracted.
- **Example:** `ta rasove mu sovera.` — *Evidence will manifest.* Gloss: `AGT EVIDENCE.CONC FUT EVIDENCE.EVT`.

**K04 · kineva** /kiˈneva/ — **doubt**: withheld certainty. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `nevaki` /neˈvaki/ — `S0→L1` → **EVT**: doubt manifests or is enacted.
- `vakine` /vaˈkine/ — `S0→L2` → **SRC**: an agent or source of doubt.
- `nekiva` /neˈkiva/ — `S1→L0` → **PAT**: a bearer or recipient affected by doubt.
- `kivane` /kiˈvane/ — `S1→L1` → **RES**: a result left by doubt manifesting.
- `vaneki` /vaˈneki/ — `S1→L2` → **CTR**: doubt is suppressed, reversed, or counteracted.
- **Example:** `ta kineva mu nevaki.` — *Doubt will manifest.* Gloss: `AGT DOUBT.CONC FUT DOUBT.EVT`.

**K05 · lurutu** /luˈɾutu/ — **learning**: acquisition of understanding. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `rutulu` /ɾuˈtulu/ — `S0→L1` → **EVT**: learning manifests or is enacted.
- `tuluru` /tuˈluɾu/ — `S0→L2` → **SRC**: an agent or source of learning.
- `rulutu` /ɾuˈlutu/ — `S1→L0` → **PAT**: a bearer or recipient affected by learning.
- `luturu` /luˈtuɾu/ — `S1→L1` → **RES**: a result left by learning manifesting.
- `turulu` /tuˈɾulu/ — `S1→L2` → **CTR**: learning is suppressed, reversed, or counteracted.
- **Example:** `ta lurutu mu rutulu.` — *Learning will manifest.* Gloss: `AGT LEARNING.CONC FUT LEARNING.EVT`.

**K06 · nerivo** /neˈɾivo/ — **language**: shared symbolic expression. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `rivone` /ɾiˈvone/ — `S0→L1` → **EVT**: language manifests or is enacted.
- `voneri` /voˈneɾi/ — `S0→L2` → **SRC**: an agent or source of language.
- `rinevo` /ɾiˈnevo/ — `S1→L0` → **PAT**: a bearer or recipient affected by language.
- `nevori` /neˈvoɾi/ — `S1→L1` → **RES**: a result left by language manifesting.
- `vorine` /voˈɾine/ — `S1→L2` → **CTR**: language is suppressed, reversed, or counteracted.
- **Example:** `ta nerivo mu rivone.` — *Language will manifest.* Gloss: `AGT LANGUAGE.CONC FUT LANGUAGE.EVT`.

**K07 · komati** /koˈmati/ — **sign**: meaningful indicator. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `matiko` /maˈtiko/ — `S0→L1` → **EVT**: sign manifests or is enacted.
- `tikoma` /tiˈkoma/ — `S0→L2` → **SRC**: an agent or source of sign.
- `makoti` /maˈkoti/ — `S1→L0` → **PAT**: a bearer or recipient affected by sign.
- `kotima` /koˈtima/ — `S1→L1` → **RES**: a result left by sign manifesting.
- `timako` /tiˈmako/ — `S1→L2` → **CTR**: sign is suppressed, reversed, or counteracted.
- **Example:** `ta komati mu matiko.` — *Sign will manifest.* Gloss: `AGT SIGN.CONC FUT SIGN.EVT`.

**K08 · lanore** /laˈnoɾe/ — **measure**: quantified comparison. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `norela` /noˈɾela/ — `S0→L1` → **EVT**: measure manifests or is enacted.
- `relano` /ɾeˈlano/ — `S0→L2` → **SRC**: an agent or source of measure.
- `nolare` /noˈlaɾe/ — `S1→L0` → **PAT**: a bearer or recipient affected by measure.
- `lareno` /laˈɾeno/ — `S1→L1` → **RES**: a result left by measure manifesting.
- `renola` /ɾeˈnola/ — `S1→L2` → **CTR**: measure is suppressed, reversed, or counteracted.
- **Example:** `ta lanore mu norela.` — *Measure will manifest.* Gloss: `AGT MEASURE.CONC FUT MEASURE.EVT`.

**K09 · miseta** /miˈseta/ — **attention**: directed awareness. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `setami` /seˈtami/ — `S0→L1` → **EVT**: attention manifests or is enacted.
- `tamise` /taˈmise/ — `S0→L2` → **SRC**: an agent or source of attention.
- `semita` /seˈmita/ — `S1→L0` → **PAT**: a bearer or recipient affected by attention.
- `mitase` /miˈtase/ — `S1→L1` → **RES**: a result left by attention manifesting.
- `tasemi` /taˈsemi/ — `S1→L2` → **CTR**: attention is suppressed, reversed, or counteracted.
- **Example:** `ta miseta mu setami.` — *Attention will manifest.* Gloss: `AGT ATTENTION.CONC FUT ATTENTION.EVT`.

**K10 · kulutu** /kuˈlutu/ — **understanding**: integrated comprehension. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `lutuku` /luˈtuku/ — `S0→L1` → **EVT**: understanding manifests or is enacted.
- `tukulu` /tuˈkulu/ — `S0→L2` → **SRC**: an agent or source of understanding.
- `lukutu` /luˈkutu/ — `S1→L0` → **PAT**: a bearer or recipient affected by understanding.
- `kutulu` /kuˈtulu/ — `S1→L1` → **RES**: a result left by understanding manifesting.
- `tuluku` /tuˈluku/ — `S1→L2` → **CTR**: understanding is suppressed, reversed, or counteracted.
- **Example:** `ta kulutu mu lutuku.` — *Understanding will manifest.* Gloss: `AGT UNDERSTANDING.CONC FUT UNDERSTANDING.EVT`.

### Emotion (10 roots)

**E01 · lemino** /leˈmino/ — **joy**: positive delight. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `minole` /miˈnole/ — `S0→L1` → **EVT**: joy manifests or is enacted.
- `nolemi` /noˈlemi/ — `S0→L2` → **SRC**: an agent or source of joy.
- `mileno` /miˈleno/ — `S1→L0` → **PAT**: a bearer or recipient affected by joy.
- `lenomi` /leˈnomi/ — `S1→L1` → **RES**: a result left by joy manifesting.
- `nomile` /noˈmile/ — `S1→L2` → **CTR**: joy is suppressed, reversed, or counteracted.
- **Example:** `ta lemino mu minole.` — *Joy will manifest.* Gloss: `AGT JOY.CONC FUT JOY.EVT`.

**E02 · monati** /moˈnati/ — **sorrow**: felt sadness. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `natimo` /naˈtimo/ — `S0→L1` → **EVT**: sorrow manifests or is enacted.
- `timona` /tiˈmona/ — `S0→L2` → **SRC**: an agent or source of sorrow.
- `namoti` /naˈmoti/ — `S1→L0` → **PAT**: a bearer or recipient affected by sorrow.
- `motina` /moˈtina/ — `S1→L1` → **RES**: a result left by sorrow manifesting.
- `tinamo` /tiˈnamo/ — `S1→L2` → **CTR**: sorrow is suppressed, reversed, or counteracted.
- **Example:** `ta monati mu natimo.` — *Sorrow will manifest.* Gloss: `AGT SORROW.CONC FUT SORROW.EVT`.

**E03 · satove** /saˈtove/ — **fear**: anticipatory alarm. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `tovesa` /toˈvesa/ — `S0→L1` → **EVT**: fear manifests or is enacted.
- `vesato` /veˈsato/ — `S0→L2` → **SRC**: an agent or source of fear.
- `tosave` /toˈsave/ — `S1→L0` → **PAT**: a bearer or recipient affected by fear.
- `saveto` /saˈveto/ — `S1→L1` → **RES**: a result left by fear manifesting.
- `vetosa` /veˈtosa/ — `S1→L2` → **CTR**: fear is suppressed, reversed, or counteracted.
- **Example:** `ta satove mu tovesa.` — *Fear will manifest.* Gloss: `AGT FEAR.CONC FUT FEAR.EVT`.

**E04 · kireta** /kiˈɾeta/ — **wonder**: surprised curiosity. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `retaki` /ɾeˈtaki/ — `S0→L1` → **EVT**: wonder manifests or is enacted.
- `takire` /taˈkiɾe/ — `S0→L2` → **SRC**: an agent or source of wonder.
- `rekita` /ɾeˈkita/ — `S1→L0` → **PAT**: a bearer or recipient affected by wonder.
- `kitare` /kiˈtaɾe/ — `S1→L1` → **RES**: a result left by wonder manifesting.
- `tareki` /taˈɾeki/ — `S1→L2` → **CTR**: wonder is suppressed, reversed, or counteracted.
- **Example:** `ta kireta mu retaki.` — *Wonder will manifest.* Gloss: `AGT WONDER.CONC FUT WONDER.EVT`.

**E05 · lusutu** /luˈsutu/ — **desire**: felt wanting. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `sutulu` /suˈtulu/ — `S0→L1` → **EVT**: desire manifests or is enacted.
- `tulusu` /tuˈlusu/ — `S0→L2` → **SRC**: an agent or source of desire.
- `sulutu` /suˈlutu/ — `S1→L0` → **PAT**: a bearer or recipient affected by desire.
- `lutusu` /luˈtusu/ — `S1→L1` → **RES**: a result left by desire manifesting.
- `tusulu` /tuˈsulu/ — `S1→L2` → **CTR**: desire is suppressed, reversed, or counteracted.
- **Example:** `ta lusutu mu sutulu.` — *Desire will manifest.* Gloss: `AGT DESIRE.CONC FUT DESIRE.EVT`.

**E06 · nesivo** /neˈsivo/ — **calm**: low-arousal steadiness. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `sivone` /siˈvone/ — `S0→L1` → **EVT**: calm manifests or is enacted.
- `vonesi` /voˈnesi/ — `S0→L2` → **SRC**: an agent or source of calm.
- `sinevo` /siˈnevo/ — `S1→L0` → **PAT**: a bearer or recipient affected by calm.
- `nevosi` /neˈvosi/ — `S1→L1` → **RES**: a result left by calm manifesting.
- `vosine` /voˈsine/ — `S1→L2` → **CTR**: calm is suppressed, reversed, or counteracted.
- **Example:** `ta nesivo mu sivone.` — *Calm will manifest.* Gloss: `AGT CALM.CONC FUT CALM.EVT`.

**E07 · konari** /koˈnaɾi/ — **anger**: response to violation. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `nariko` /naˈɾiko/ — `S0→L1` → **EVT**: anger manifests or is enacted.
- `rikona` /ɾiˈkona/ — `S0→L2` → **SRC**: an agent or source of anger.
- `nakori` /naˈkoɾi/ — `S1→L0` → **PAT**: a bearer or recipient affected by anger.
- `korina` /koˈɾina/ — `S1→L1` → **RES**: a result left by anger manifesting.
- `rinako` /ɾiˈnako/ — `S1→L2` → **CTR**: anger is suppressed, reversed, or counteracted.
- **Example:** `ta konari mu nariko.` — *Anger will manifest.* Gloss: `AGT ANGER.CONC FUT ANGER.EVT`.

**E08 · lanote** /laˈnote/ — **hope**: expectation of possible good. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `notela` /noˈtela/ — `S0→L1` → **EVT**: hope manifests or is enacted.
- `telano` /teˈlano/ — `S0→L2` → **SRC**: an agent or source of hope.
- `nolate` /noˈlate/ — `S1→L0` → **PAT**: a bearer or recipient affected by hope.
- `lateno` /laˈteno/ — `S1→L1` → **RES**: a result left by hope manifesting.
- `tenola` /teˈnola/ — `S1→L2` → **CTR**: hope is suppressed, reversed, or counteracted.
- **Example:** `ta lanote mu notela.` — *Hope will manifest.* Gloss: `AGT HOPE.CONC FUT HOPE.EVT`.

**E09 · miteva** /miˈteva/ — **grief**: pain of loss. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `tevami` /teˈvami/ — `S0→L1` → **EVT**: grief manifests or is enacted.
- `vamite` /vaˈmite/ — `S0→L2` → **SRC**: an agent or source of grief.
- `temiva` /teˈmiva/ — `S1→L0` → **PAT**: a bearer or recipient affected by grief.
- `mivate` /miˈvate/ — `S1→L1` → **RES**: a result left by grief manifesting.
- `vatemi` /vaˈtemi/ — `S1→L2` → **CTR**: grief is suppressed, reversed, or counteracted.
- **Example:** `ta miteva mu tevami.` — *Grief will manifest.* Gloss: `AGT GRIEF.CONC FUT GRIEF.EVT`.

**E10 · kumunu** /kuˈmunu/ — **longing**: sustained absence-related desire. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `munuku` /muˈnuku/ — `S0→L1` → **EVT**: longing manifests or is enacted.
- `nukumu` /nuˈkumu/ — `S0→L2` → **SRC**: an agent or source of longing.
- `mukunu` /muˈkunu/ — `S1→L0` → **PAT**: a bearer or recipient affected by longing.
- `kunumu` /kuˈnumu/ — `S1→L1` → **RES**: a result left by longing manifesting.
- `numuku` /nuˈmuku/ — `S1→L2` → **CTR**: longing is suppressed, reversed, or counteracted.
- **Example:** `ta kumunu mu munuku.` — *Longing will manifest.* Gloss: `AGT LONGING.CONC FUT LONGING.EVT`.

### Nature (10 roots)

**N01 · lemiso** /leˈmiso/ — **stone**: mineral solidity. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `misole` /miˈsole/ — `S0→L1` → **EVT**: stone manifests or is enacted.
- `solemi` /soˈlemi/ — `S0→L2` → **SRC**: an agent or source of stone.
- `mileso` /miˈleso/ — `S1→L0` → **PAT**: a bearer or recipient affected by stone.
- `lesomi` /leˈsomi/ — `S1→L1` → **RES**: a result left by stone manifesting.
- `somile` /soˈmile/ — `S1→L2` → **CTR**: stone is suppressed, reversed, or counteracted.
- **Example:** `ta lemiso mu misole.` — *Stone will manifest.* Gloss: `AGT STONE.CONC FUT STONE.EVT`.

**N02 · morasi** /moˈɾasi/ — **water**: flowing liquid. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `rasimo` /ɾaˈsimo/ — `S0→L1` → **EVT**: water manifests or is enacted.
- `simora` /siˈmoɾa/ — `S0→L2` → **SRC**: an agent or source of water.
- `ramosi` /ɾaˈmosi/ — `S1→L0` → **PAT**: a bearer or recipient affected by water.
- `mosira` /moˈsiɾa/ — `S1→L1` → **RES**: a result left by water manifesting.
- `siramo` /siˈɾamo/ — `S1→L2` → **CTR**: water is suppressed, reversed, or counteracted.
- **Example:** `ta morasi mu rasimo.` — *Water will manifest.* Gloss: `AGT WATER.CONC FUT WATER.EVT`.

**N03 · kalone** /kaˈlone/ — **fire**: heat-producing flame. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `loneka` /loˈneka/ — `S0→L1` → **EVT**: fire manifests or is enacted.
- `nekalo` /neˈkalo/ — `S0→L2` → **SRC**: an agent or source of fire.
- `lokane` /loˈkane/ — `S1→L0` → **PAT**: a bearer or recipient affected by fire.
- `kanelo` /kaˈnelo/ — `S1→L1` → **RES**: a result left by fire manifesting.
- `neloka` /neˈloka/ — `S1→L2` → **CTR**: fire is suppressed, reversed, or counteracted.
- **Example:** `ta kalone mu loneka.` — *Fire will manifest.* Gloss: `AGT FIRE.CONC FUT FIRE.EVT`.

**N04 · kiseta** /kiˈseta/ — **wind**: moving air. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `setaki` /seˈtaki/ — `S0→L1` → **EVT**: wind manifests or is enacted.
- `takise` /taˈkise/ — `S0→L2` → **SRC**: an agent or source of wind.
- `sekita` /seˈkita/ — `S1→L0` → **PAT**: a bearer or recipient affected by wind.
- `kitase` /kiˈtase/ — `S1→L1` → **RES**: a result left by wind manifesting.
- `taseki` /taˈseki/ — `S1→L2` → **CTR**: wind is suppressed, reversed, or counteracted.
- **Example:** `ta kiseta mu setaki.` — *Wind will manifest.* Gloss: `AGT WIND.CONC FUT WIND.EVT`.

**N05 · lutuvu** /luˈtuvu/ — **earth**: ground or soil. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `tuvulu` /tuˈvulu/ — `S0→L1` → **EVT**: earth manifests or is enacted.
- `vulutu` /vuˈlutu/ — `S0→L2` → **SRC**: an agent or source of earth.
- `tuluvu` /tuˈluvu/ — `S1→L0` → **PAT**: a bearer or recipient affected by earth.
- `luvutu` /luˈvutu/ — `S1→L1` → **RES**: a result left by earth manifesting.
- `vutulu` /vuˈtulu/ — `S1→L2` → **CTR**: earth is suppressed, reversed, or counteracted.
- **Example:** `ta lutuvu mu tuvulu.` — *Earth will manifest.* Gloss: `AGT EARTH.CONC FUT EARTH.EVT`.

**N06 · resito** /ɾeˈsito/ — **seed**: reproductive beginning. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `sitore` /siˈtoɾe/ — `S0→L1` → **EVT**: seed manifests or is enacted.
- `toresi` /toˈɾesi/ — `S0→L2` → **SRC**: an agent or source of seed.
- `sireto` /siˈɾeto/ — `S1→L0` → **PAT**: a bearer or recipient affected by seed.
- `retosi` /ɾeˈtosi/ — `S1→L1` → **RES**: a result left by seed manifesting.
- `tosire` /toˈsiɾe/ — `S1→L2` → **CTR**: seed is suppressed, reversed, or counteracted.
- **Example:** `ta resito mu sitore.` — *Seed will manifest.* Gloss: `AGT SEED.CONC FUT SEED.EVT`.

**N07 · konati** /koˈnati/ — **forest**: interconnected trees. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `natiko` /naˈtiko/ — `S0→L1` → **EVT**: forest manifests or is enacted.
- `tikona` /tiˈkona/ — `S0→L2` → **SRC**: an agent or source of forest.
- `nakoti` /naˈkoti/ — `S1→L0` → **PAT**: a bearer or recipient affected by forest.
- `kotina` /koˈtina/ — `S1→L1` → **RES**: a result left by forest manifesting.
- `tinako` /tiˈnako/ — `S1→L2` → **CTR**: forest is suppressed, reversed, or counteracted.
- **Example:** `ta konati mu natiko.` — *Forest will manifest.* Gloss: `AGT FOREST.CONC FUT FOREST.EVT`.

**N08 · larose** /laˈɾose/ — **star**: distant luminous body. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `rosela` /ɾoˈsela/ — `S0→L1` → **EVT**: star manifests or is enacted.
- `selaro` /seˈlaɾo/ — `S0→L2` → **SRC**: an agent or source of star.
- `rolase` /ɾoˈlase/ — `S1→L0` → **PAT**: a bearer or recipient affected by star.
- `lasero` /laˈseɾo/ — `S1→L1` → **RES**: a result left by star manifesting.
- `serola` /seˈɾola/ — `S1→L2` → **CTR**: star is suppressed, reversed, or counteracted.
- **Example:** `ta larose mu rosela.` — *Star will manifest.* Gloss: `AGT STAR.CONC FUT STAR.EVT`.

**N09 · nireta** /niˈɾeta/ — **night**: period of darkness. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `retani` /ɾeˈtani/ — `S0→L1` → **EVT**: night manifests or is enacted.
- `tanire` /taˈniɾe/ — `S0→L2` → **SRC**: an agent or source of night.
- `renita` /ɾeˈnita/ — `S1→L0` → **PAT**: a bearer or recipient affected by night.
- `nitare` /niˈtaɾe/ — `S1→L1` → **RES**: a result left by night manifesting.
- `tareni` /taˈɾeni/ — `S1→L2` → **CTR**: night is suppressed, reversed, or counteracted.
- **Example:** `ta nireta mu retani.` — *Night will manifest.* Gloss: `AGT NIGHT.CONC FUT NIGHT.EVT`.

**N10 · kumusu** /kuˈmusu/ — **rain**: falling water. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `musuku` /muˈsuku/ — `S0→L1` → **EVT**: rain manifests or is enacted.
- `sukumu` /suˈkumu/ — `S0→L2` → **SRC**: an agent or source of rain.
- `mukusu` /muˈkusu/ — `S1→L0` → **PAT**: a bearer or recipient affected by rain.
- `kusumu` /kuˈsumu/ — `S1→L1` → **RES**: a result left by rain manifesting.
- `sumuku` /suˈmuku/ — `S1→L2` → **CTR**: rain is suppressed, reversed, or counteracted.
- **Example:** `ta kumusu mu musuku.` — *Rain will manifest.* Gloss: `AGT RAIN.CONC FUT RAIN.EVT`.

### Logic (10 roots)

**L01 · lemivo** /leˈmivo/ — **truth**: accord with fact. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `mivole` /miˈvole/ — `S0→L1` → **EVT**: truth manifests or is enacted.
- `volemi` /voˈlemi/ — `S0→L2` → **SRC**: an agent or source of truth.
- `milevo` /miˈlevo/ — `S1→L0` → **PAT**: a bearer or recipient affected by truth.
- `levomi` /leˈvomi/ — `S1→L1` → **RES**: a result left by truth manifesting.
- `vomile` /voˈmile/ — `S1→L2` → **CTR**: truth is suppressed, reversed, or counteracted.
- **Example:** `ta lemivo mu mivole.` — *Truth will manifest.* Gloss: `AGT TRUTH.CONC FUT TRUTH.EVT`.

**L02 · moravi** /moˈɾavi/ — **falsehood**: nonaccord with fact. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `ravimo` /ɾaˈvimo/ — `S0→L1` → **EVT**: falsehood manifests or is enacted.
- `vimora` /viˈmoɾa/ — `S0→L2` → **SRC**: an agent or source of falsehood.
- `ramovi` /ɾaˈmovi/ — `S1→L0` → **PAT**: a bearer or recipient affected by falsehood.
- `movira` /moˈviɾa/ — `S1→L1` → **RES**: a result left by falsehood manifesting.
- `viramo` /viˈɾamo/ — `S1→L2` → **CTR**: falsehood is suppressed, reversed, or counteracted.
- **Example:** `ta moravi mu ravimo.` — *Falsehood will manifest.* Gloss: `AGT FALSEHOOD.CONC FUT FALSEHOOD.EVT`.

**L03 · kalose** /kaˈlose/ — **cause**: producer of change. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `loseka` /loˈseka/ — `S0→L1` → **EVT**: cause manifests or is enacted.
- `sekalo` /seˈkalo/ — `S0→L2` → **SRC**: an agent or source of cause.
- `lokase` /loˈkase/ — `S1→L0` → **PAT**: a bearer or recipient affected by cause.
- `kaselo` /kaˈselo/ — `S1→L1` → **RES**: a result left by cause manifesting.
- `seloka` /seˈloka/ — `S1→L2` → **CTR**: cause is suppressed, reversed, or counteracted.
- **Example:** `ta kalose mu loseka.` — *Cause will manifest.* Gloss: `AGT CAUSE.CONC FUT CAUSE.EVT`.

**L04 · kiteva** /kiˈteva/ — **effect**: result of a cause. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `tevaki` /teˈvaki/ — `S0→L1` → **EVT**: effect manifests or is enacted.
- `vakite` /vaˈkite/ — `S0→L2` → **SRC**: an agent or source of effect.
- `tekiva` /teˈkiva/ — `S1→L0` → **PAT**: a bearer or recipient affected by effect.
- `kivate` /kiˈvate/ — `S1→L1` → **RES**: a result left by effect manifesting.
- `vateki` /vaˈteki/ — `S1→L2` → **CTR**: effect is suppressed, reversed, or counteracted.
- **Example:** `ta kiteva mu tevaki.` — *Effect will manifest.* Gloss: `AGT EFFECT.CONC FUT EFFECT.EVT`.

**L05 · munusu** /muˈnusu/ — **choice**: selection among alternatives. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `nusumu` /nuˈsumu/ — `S0→L1` → **EVT**: choice manifests or is enacted.
- `sumunu` /suˈmunu/ — `S0→L2` → **SRC**: an agent or source of choice.
- `numusu` /nuˈmusu/ — `S1→L0` → **PAT**: a bearer or recipient affected by choice.
- `musunu` /muˈsunu/ — `S1→L1` → **RES**: a result left by choice manifesting.
- `sunumu` /suˈnumu/ — `S1→L2` → **CTR**: choice is suppressed, reversed, or counteracted.
- **Example:** `ta munusu mu nusumu.` — *Choice will manifest.* Gloss: `AGT CHOICE.CONC FUT CHOICE.EVT`.

**L06 · retivo** /ɾeˈtivo/ — **possibility**: unexcluded potential. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `tivore` /tiˈvoɾe/ — `S0→L1` → **EVT**: possibility manifests or is enacted.
- `voreti` /voˈɾeti/ — `S0→L2` → **SRC**: an agent or source of possibility.
- `tirevo` /tiˈɾevo/ — `S1→L0` → **PAT**: a bearer or recipient affected by possibility.
- `revoti` /ɾeˈvoti/ — `S1→L1` → **RES**: a result left by possibility manifesting.
- `votire` /voˈtiɾe/ — `S1→L2` → **CTR**: possibility is suppressed, reversed, or counteracted.
- **Example:** `ta retivo mu tivore.` — *Possibility will manifest.* Gloss: `AGT POSSIBILITY.CONC FUT POSSIBILITY.EVT`.

**L07 · korasi** /koˈɾasi/ — **necessity**: required condition. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `rasiko` /ɾaˈsiko/ — `S0→L1` → **EVT**: necessity manifests or is enacted.
- `sikora` /siˈkoɾa/ — `S0→L2` → **SRC**: an agent or source of necessity.
- `rakosi` /ɾaˈkosi/ — `S1→L0` → **PAT**: a bearer or recipient affected by necessity.
- `kosira` /koˈsiɾa/ — `S1→L1` → **RES**: a result left by necessity manifesting.
- `sirako` /siˈɾako/ — `S1→L2` → **CTR**: necessity is suppressed, reversed, or counteracted.
- **Example:** `ta korasi mu rasiko.` — *Necessity will manifest.* Gloss: `AGT NECESSITY.CONC FUT NECESSITY.EVT`.

**L08 · larove** /laˈɾove/ — **difference**: lack of sameness. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `rovela` /ɾoˈvela/ — `S0→L1` → **EVT**: difference manifests or is enacted.
- `velaro` /veˈlaɾo/ — `S0→L2` → **SRC**: an agent or source of difference.
- `rolave` /ɾoˈlave/ — `S1→L0` → **PAT**: a bearer or recipient affected by difference.
- `lavero` /laˈveɾo/ — `S1→L1` → **RES**: a result left by difference manifesting.
- `verola` /veˈɾola/ — `S1→L2` → **CTR**: difference is suppressed, reversed, or counteracted.
- **Example:** `ta larove mu rovela.` — *Difference will manifest.* Gloss: `AGT DIFFERENCE.CONC FUT DIFFERENCE.EVT`.

**L09 · niseta** /niˈseta/ — **similarity**: shared qualities. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `setani` /seˈtani/ — `S0→L1` → **EVT**: similarity manifests or is enacted.
- `tanise` /taˈnise/ — `S0→L2` → **SRC**: an agent or source of similarity.
- `senita` /seˈnita/ — `S1→L0` → **PAT**: a bearer or recipient affected by similarity.
- `nitase` /niˈtase/ — `S1→L1` → **RES**: a result left by similarity manifesting.
- `taseni` /taˈseni/ — `S1→L2` → **CTR**: similarity is suppressed, reversed, or counteracted.
- **Example:** `ta niseta mu setani.` — *Similarity will manifest.* Gloss: `AGT SIMILARITY.CONC FUT SIMILARITY.EVT`.

**L10 · kumuvu** /kuˈmuvu/ — **transformation**: change of form or state. Nominal in 00/02/10/11; predicate in 01/12. EVT intransitive by default; `ko` licenses patient-bearing causative.

- `muvuku` /muˈvuku/ — `S0→L1` → **EVT**: transformation manifests or is enacted.
- `vukumu` /vuˈkumu/ — `S0→L2` → **SRC**: an agent or source of transformation.
- `mukuvu` /muˈkuvu/ — `S1→L0` → **PAT**: a bearer or recipient affected by transformation.
- `kuvumu` /kuˈvumu/ — `S1→L1` → **RES**: a result left by transformation manifesting.
- `vumuku` /vuˈmuku/ — `S1→L2` → **CTR**: transformation is suppressed, reversed, or counteracted.
- **Example:** `ta kumuvu mu muvuku.` — *Transformation will manifest.* Gloss: `AGT TRANSFORMATION.CONC FUT TRANSFORMATION.EVT`.

## 7. Twenty analyzed sentences, increasingly complex

Gloss conventions: `CONC` nominal concept, `EVT` manifest event, `SRC` agent/source nominal, `PAT` affected nominal, `RES` result nominal, `CTR` counter-event; closed-class glosses listed in §3. Both each lexical word and each CV particle are represented by their own gloss unit. Punctuation is not a morpheme.

### 01. Greeting
**AZURAVEL:** `ta ya di yu setali.`
**Pronunciation:** `/ta ja di ju seˈtali ./`
**Morpheme gloss:** `AGT 1SG REC 2SG GREETING.EVT .`
**English:** I greet you.
**Interpretation:** The manifestation of greeting directed toward the addressee is the conventional salutation.

### 02. Presence
**AZURAVEL:** `ta ya noveka.`
**Pronunciation:** `/ta ja noˈveka ./`
**Morpheme gloss:** `AGT 1SG PRESENCE.EVT .`
**English:** I become present.
**Interpretation:** The predicate is the once-rotated event form, not the nominal base.

### 03. Question
**AZURAVEL:** `ta yu sivoke ri?`
**Pronunciation:** `/ta ju siˈvoke ɾi ?/`
**Morpheme gloss:** `AGT 2SG KNOWLEDGE.EVT Q ?`
**English:** Do you come to know?
**Interpretation:** Clause-final ri changes assertion to a yes/no question.

### 04. Command
**AZURAVEL:** `va setami!`
**Pronunciation:** `/va seˈtami !/`
**Morpheme gloss:** `IMP ATTENTION.EVT !`
**English:** Pay attention!
**Interpretation:** va suppresses an explicit subject and addresses the listener.

### 05. Past
**AZURAVEL:** `ta ya mi natilo.`
**Pronunciation:** `/ta ja mi naˈtilo ./`
**Morpheme gloss:** `AGT 1SG PST JOURNEY.EVT .`
**English:** I traveled.
**Interpretation:** mi locates the manifestation before speech time.

### 06. Future
**AZURAVEL:** `ta yi mu rivoke.`
**Pronunciation:** `/ta ji mu ɾiˈvoke ./`
**Morpheme gloss:** `AGT 1PL.INCL FUT CREATION.EVT .`
**English:** We will create.
**Interpretation:** mu locates the manifestation after speech time.

### 07. Negation
**AZURAVEL:** `ta ya sa tovesa.`
**Pronunciation:** `/ta ja sa toˈvesa ./`
**Morpheme gloss:** `AGT 1SG NEG FEAR.EVT .`
**English:** I do not become afraid.
**Interpretation:** sa negates the proposition, distinct from root-counteraction.

### 08. Plural
**AZURAVEL:** `ta la lomati letaki.`
**Pronunciation:** `/ta la loˈmati leˈtaki ./`
**Morpheme gloss:** `AGT PL PERSON.CONC FRIENDSHIP.EVT .`
**English:** People form friendship.
**Interpretation:** la marks the nominal as plural.

### 09. Causative
**AZURAVEL:** `ta yu no lemiso ko niroke.`
**Pronunciation:** `/ta ju no leˈmiso ko niˈɾoke ./`
**Morpheme gloss:** `AGT 2SG PAT STONE.CONC CAUS MOTION.EVT .`
**English:** You make the stone move.
**Interpretation:** ko introduces an external causer while no marks the affected stone.

### 10. Future + causative
**AZURAVEL:** `ta ya no lorasi mu ko rivoke.`
**Pronunciation:** `/ta ja no loˈɾasi mu ko ɾiˈvoke ./`
**Morpheme gloss:** `AGT 1SG PAT HOME.CONC FUT CAUS CREATION.EVT .`
**English:** I will create a home.
**Interpretation:** Tense precedes valency-changing causative.

### 11. Possession + identity
**AZURAVEL:** `ta ya li lorasi no kolasi ra.`
**Pronunciation:** `/ta ja li loˈɾasi no koˈlasi ɾa ./`
**Morpheme gloss:** `AGT 1SG GEN HOME.CONC PAT SHELTER.CONC EQU .`
**English:** My home is a shelter.
**Interpretation:** The genitive connector li binds possessor ya to head home; ra classifies the subject.

### 12. Reciprocity
**AZURAVEL:** `ta yi lo suvunu.`
**Pronunciation:** `/ta ji lo suˈvunu ./`
**Morpheme gloss:** `AGT 1PL.INCL RECP EXCHANGE.EVT .`
**English:** We exchange with one another.
**Interpretation:** lo requires a plural actor and treats the participants as mutual counterparts.

### 13. Completed event
**AZURAVEL:** `ta ya no menito mi nu ko nitome.`
**Pronunciation:** `/ta ja no meˈnito mi nu ko niˈtome ./`
**Morpheme gloss:** `AGT 1SG PAT PROMISE.CONC PST PFV CAUS PROMISE.EVT .`
**English:** I completed making a promise.
**Interpretation:** nu conveys completion while mi places it in the past.

### 14. Possibility
**AZURAVEL:** `ta yi pa notela.`
**Pronunciation:** `/ta ji pa noˈtela ./`
**Morpheme gloss:** `AGT 1PL.INCL POSS HOPE.EVT .`
**English:** We may hope.
**Interpretation:** pa marks epistemic possibility, not future tense.

### 15. Certainty
**AZURAVEL:** `ta yu pe sivoke.`
**Pronunciation:** `/ta ju pe siˈvoke ./`
**Morpheme gloss:** `AGT 2SG CERT KNOWLEDGE.EVT .`
**English:** You certainly come to know.
**Interpretation:** pe marks high speaker certainty.

### 16. Counter-event
**AZURAVEL:** `ta ya di yu mi terona.`
**Pronunciation:** `/ta ja di ju mi teˈɾona ./`
**Morpheme gloss:** `AGT 1SG REC 2SG PST DISTANCE.CTR .`
**English:** I closed the distance toward you.
**Interpretation:** Reversal of the syllable order is active counteraction, not ordinary negation.

### 17. Ongoing + emphasis
**AZURAVEL:** `ta yi ne ke risone.`
**Pronunciation:** `/ta ji ne ke ɾiˈsone ./`
**Morpheme gloss:** `AGT 1PL.INCL IPFV EMPH SONG.EVT .`
**English:** We are singing—emphatically.
**Interpretation:** ne marks an ongoing event; ke strengthens the event focus.

### 18. Conditional
**AZURAVEL:** `se ta ya nevaki si ta ya mu narimo.`
**Pronunciation:** `/se ta ja neˈvaki si ta ja mu naˈɾimo ./`
**Morpheme gloss:** `IF AGT 1SG DOUBT.EVT THEN AGT 1SG FUT INQUIRY.EVT .`
**English:** If I doubt, I will inquire.
**Interpretation:** se and si delimit exactly one antecedent and consequent.

### 19. Philosophical identity
**AZURAVEL:** `ta larove no retivo ra.`
**Pronunciation:** `/ta laˈɾove no ɾeˈtivo ɾa ./`
**Morpheme gloss:** `AGT DIFFERENCE.CONC PAT POSSIBILITY.CONC EQU .`
**English:** Difference is possibility.
**Interpretation:** ra allows conceptual classification, not just personal identity.

### 20. Poetic couplet
**AZURAVEL:** `ta nireta no kusuvu mi ko vusuku; ta larose mu notela.`
**Pronunciation:** `/ta niˈɾeta no kuˈsuvu mi ko vuˈsuku ; ta laˈɾose mu noˈtela ./`
**Morpheme gloss:** `AGT NIGHT.CONC PAT VOICE.CONC PST CAUS VOICE.CTR ; AGT STAR.CONC FUT HOPE.EVT .`
**English:** Night silenced the voice; a star will kindle hope.
**Interpretation:** The two finite clauses contrast active silencing with an anticipated manifestation of hope.

### Minimal-pair demonstration: one rearrangement, different meaning

Sentence 02 uses `ta ya noveka.` (S0→L1, **EVT**: *I become present*). Replace **only** the last word with `ta ya venoka.` (S1→L2, **CTR**: *I withdraw/undo my presence*). The syllable bag `kanove` stays identical; only the order, event valence, and meaning change. Compare adding `sa`: `ta ya sa noveka.` = *I do not become present*, without claiming an active withdrawal.

## 8. Translation and reference API

**Decoder:** tokenization → distinguish 2-letter particles and 6-letter forms → enforce three distinct root consonants → canonicalize sorted bag → lookup ID → recover one of six states → enforce particle and case ordering → produce segment gloss and normalized semantics. Unknown lexical bags or malformed syntax are returned as explicit errors. No probabilistic best-guess parser is used.

**English mini-translator:** deliberately restricted to `I/you/we/they [will|did] [not|may|certainly] <mapped verb>` or `I/you/we/they manifest <registered concept>`. This is a **controlled English subset**, not English translation in general. Known aliases are in `AZURAVEL_DATA.json`. Nonmatching requests yield a clear unknown-word or unsupported-pattern error. The interactive sentence builder can express more using the native grammar. English-to-AZ1 is not promised for every possible English utterance.

**Reference CLI examples** (from the extracted project directory):
```shell
python azuravel_ref.py inspect miroke
python azuravel_ref.py encode miroke
python azuravel_ref.py decode "AZ1|I01|0|1|miroke"
python azuravel_ref.py parse "ta ya mi miroke."
python azuravel_ref.py english "I will travel"
python azuravel_ref.py roundtrip miroke
```

## 9. Atlas and operator contract

The offline `AZURAVEL_ATLAS.html` is a standalone reference built from the same embedded JSON. It must expose root search/filter, all six transformations, the rail script, phonetic and grammatical analysis, a sentence sampler, a bounded English mapper, a native sentence builder, Code 128-B encoding as a true vector barcode, barcode-payload text decoding, and error feedback. For accessibility, core text remains selectable and high-contrast. The master specification and `AZURAVEL_DATA.json` govern disagreements, not the visual atlas.

## 10. Verification and limitations

Run `python -m unittest -v test_azuravel.py` inside the package. The suite covers all six states for all 100 roots, canonical uniqueness, pronunciation, grammar, particles, illegal forms, payload mismatch/version handling, Code128 structure/checksums/module roundtrips, and edge cases. It contains more than 30 named individual cases. Physical scan results, browser test results, and any remaining known limitations are recorded in `VALIDATION_REPORT.md` **after** the tests, not inferred from the source code. No English free-form translation beyond the bounded subset is claimed.

---
*AZURAVEL 1.0 uses a finite, compositional grammar. It is intentionally small enough to audit and large enough to generate nontrivial utterances. Any future root additions or extended transformations require a versioned registry update, not a reinterpretation of existing AZ1 payloads.*

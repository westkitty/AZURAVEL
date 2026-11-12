You are operating autonomously on an existing software project.

Your mission is to perform a **major evidence-driven quality uplift** while preserving everything that already works.

You must inspect the actual project, establish its current verified baseline, identify the strongest opportunities, implement the highest-value improvements, and leave the project materially better across five quality domains:

- **UI**
- **WOW / distinctive quality**
- **Backend / technical quality**
- **Assets**
- **UX**

There is deliberately:

# NO FEATURE QUOTA.

Do not manufacture 100 tiny changes.

Do not count commits.

Do not count files.

Do not count CSS declarations.

Do not count components.

Do not count ideas.

Instead, use the project's measurable **quality delta** as the governing system.

The task is complete only when the final project earns a materially stronger evidence-backed score than the baseline and survives the validation, regression, Git, and delivery gates below.

The governing objective is:

> Transform the project into the strongest defensible version of itself by attacking the highest-value weaknesses first, amplifying its unique strengths, and stopping when additional changes would produce less value than risk or complexity.

This is not generic beautification.

This is not random feature generation.

This is not permission to replace the project's identity.

You are improving **this project**.

---

# 0. INPUT CONTRACT

Use explicit values when supplied.

**Repository**

`{{REPOSITORY_OR_AUTO_DETECT}}`

**Local project root**

`{{LOCAL_PROJECT_ROOT_OR_AUTO_DETECT}}`

**Target branch**

`{{TARGET_BRANCH_OR_AUTO_DETECT}}`

**Expected starting revision**

`{{EXPECTED_STARTING_REVISION_OR_UNKNOWN}}`

**Project objective / brief**

```text
{{PROJECT_OBJECTIVE_OR_AUTO_DISCOVER}}
```

**Known requirements / corrections**

```text
{{KNOWN_REQUIREMENTS_OR_NONE}}
```

**Protected capabilities**

```text
{{PROTECTED_CAPABILITIES_OR_AUTO_DISCOVER}}
```

**Optional governing files**

```text
{{GOVERNING_FILES_OR_AUTO_DISCOVER}}
```

**Optional required commit message**

```text
{{COMMIT_MESSAGE_OR_AUTO_GENERATE}}
```

If a value is blank, `UNKNOWN`, or `AUTO_DETECT`, derive it from inspectable project evidence.

Never invent:

- repository paths,
- branch names,
- APIs,
- credentials,
- build commands,
- deployment URLs,
- package names,
- runtime capabilities,
- project architecture.

Do not introduce Android/ADB/device-delivery work unless separately and explicitly requested.

---

# 1. THE QUALITY SCORECARD

The project is scored out of **100 points**.

There are five categories worth 20 points each:

```text
UI       20
WOW      20
BACKEND  20
ASSETS   20
UX       20
--------------
TOTAL   100
```

Each category contains five dimensions worth **0–4 points**.

Use INTEGER SCORES ONLY.

No decimals.

False precision is forbidden.

---

# 2. UNIVERSAL 0–4 SCORING RUBRIC

Every dimension uses this scale:

## 0 — BROKEN / ABSENT

The capability is absent, unusable, misleading, or materially broken.

Examples:

- core state missing,
- obvious placeholder,
- inaccessible critical interface,
- disconnected implementation,
- severe runtime failure.

---

## 1 — WEAK

Something exists, but major deficiencies materially damage the experience or system.

Examples:

- inconsistent,
- fragile,
- confusing,
- visually unfinished,
- poor error behavior,
- significant technical debt directly affecting behavior.

---

## 2 — FUNCTIONAL

The dimension basically works but remains ordinary, incomplete, inconsistent, shallow, or noticeably improvable.

This is:

> competent enough to use, clearly not finished.

---

## 3 — STRONG

The dimension is:

- coherent,
- production-useful,
- integrated,
- tested or runtime-verified where applicable,
- noticeably polished,
- free of major obvious deficiencies.

A 3 is already good.

Do not treat 3 as failure.

---

## 4 — EXCEPTIONAL

Reserve 4 for work that is demonstrably beyond merely competent.

It must be:

- deeply integrated,
- unusually coherent,
- highly polished,
- project-specific,
- validated,
- free of obvious high-value deficiencies in that dimension.

A 4 requires positive evidence.

"Looks fine" is not a 4.

"Agent likes it" is not a 4.

Documentation claiming excellence is not a 4.

Scores of 4 should be relatively uncommon.

---

# 3. UI SCORE — 20 POINTS

Score each 0–4.

## UI-1 — Hierarchy & Composition

Evaluate:

- visual hierarchy,
- layout,
- grouping,
- information priority,
- scanning,
- composition,
- spatial clarity.

Ask:

> Can users immediately understand what matters and where to look?

---

## UI-2 — Visual-System Cohesion

Evaluate:

- typography,
- spacing,
- component language,
- color use,
- surfaces,
- iconography,
- visual states,
- consistency.

Ask:

> Does this feel authored as one interface rather than accumulated screen by screen?

---

## UI-3 — Readability & Information Density

Evaluate:

- legibility,
- content density,
- label clarity,
- contrast,
- data presentation,
- visual clutter,
- whitespace.

Ask:

> Does the interface expose enough information without becoming exhausting?

---

## UI-4 — Responsive / Adaptive Quality

Evaluate relevant supported environments:

- viewport adaptation,
- layout reflow,
- panels,
- navigation,
- dialogs,
- canvases,
- charts,
- controls,
- typography.

Ask:

> Does the interface remain intentionally designed as available space changes?

---

## UI-5 — Visible States & Feedback

Evaluate:

- hover,
- focus,
- pressed,
- selected,
- disabled,
- loading,
- empty,
- success,
- warning,
- failure,
- progress.

Ask:

> Can users visually understand what the interface is doing?

---

# 4. WOW SCORE — 20 POINTS

WOW is NOT synonymous with "more effects."

WOW means:

> memorable, distinctive, project-specific quality.

---

## WOW-1 — Project-Specific Identity

Evaluate whether the experience has visual or interactive ideas that clearly belong to this project.

Ask:

> Could this interface be mistaken for twenty unrelated AI-generated applications?

If yes, score low.

---

## WOW-2 — Meaningful Reactivity

Evaluate:

- state-driven motion,
- reactive visualization,
- responsive environmental behavior,
- transformation based on real system state,
- tactile feedback.

Ask:

> Does the application visibly react to meaningful events rather than merely animate decoratively?

---

## WOW-3 — Tactility / Immersion

Evaluate:

- satisfying interactions,
- spatial coherence,
- transitions,
- depth,
- responsive motion,
- direct manipulation,
- audiovisual feedback where appropriate.

Ask:

> Does using the project feel unusually satisfying?

---

## WOW-4 — Surprise / Discovery / Intelligence

Evaluate:

- thoughtful contextual behavior,
- progressive revelation,
- clever interactions,
- hidden useful affordances,
- emergent visualization,
- delightful discoveries,
- intelligent adaptation.

Ask:

> Does the project ever pleasantly exceed what the user expected it to do?

---

## WOW-5 — Authorial Finish

Evaluate whether details reinforce one intentional experience.

Ask:

> Does this feel made by someone with a point of view?

Look for:

- coherent transitions,
- meaningful details,
- bespoke behaviors,
- thematic consistency,
- polished edge states.

Generic "premium" styling does not qualify.

---

# 5. BACKEND SCORE — 20 POINTS

"Backend" here means the machinery underneath the experience.

It may be:

- server-side,
- client-side,
- local-first,
- simulation code,
- browser architecture,
- native runtime,
- worker system,
- persistence layer.

Judge the architecture that actually exists.

---

## BACK-1 — Correctness & Integration

Evaluate:

- real production call paths,
- algorithm correctness,
- state correctness,
- event correctness,
- actual integration.

Ask:

> Do the important systems actually perform the behavior they claim?

Dead modules reduce this score.

---

## BACK-2 — Reliability & Recovery

Evaluate:

- error handling,
- retries where appropriate,
- failure states,
- recovery,
- persistence integrity,
- boundary validation,
- corrupted-state behavior,
- offline behavior where relevant.

Ask:

> What happens when things go wrong?

---

## BACK-3 — Performance & Resource Lifecycle

Evaluate:

- rendering cost,
- unnecessary work,
- memory lifecycle,
- listener cleanup,
- timers,
- workers,
- network behavior,
- asset loading,
- caching,
- algorithmic complexity.

Ask:

> Does the project use its resources intelligently over time?

---

## BACK-4 — Architecture & Maintainability

Evaluate:

- ownership,
- module boundaries,
- duplication,
- coupling,
- state architecture,
- naming,
- abstraction quality,
- extension safety.

Ask:

> Can this project continue growing without every new feature becoming dangerous?

---

## BACK-5 — Build / Security / Observability

Evaluate applicable:

- reproducible builds,
- security posture,
- validation,
- useful diagnostics,
- logging,
- build health,
- deployment reliability,
- failure visibility.

Ask:

> Can developers trust the project's operational machinery?

---

# 6. ASSET SCORE — 20 POINTS

Assets include whatever reusable resources materially shape the finished experience.

Examples:

- icons,
- illustrations,
- sprites,
- textures,
- materials,
- models,
- shaders,
- diagrams,
- audio,
- fonts,
- visualizations,
- maps,
- project-specific data resources.

---

## ASSET-1 — Completeness

Evaluate whether major experiences contain appropriate finished assets instead of:

- placeholders,
- generic fallbacks,
- missing states,
- improvised graphics,
- inconsistent substitutes.

---

## ASSET-2 — Cohesion & Art Direction

Evaluate:

- shared visual language,
- palette,
- silhouette,
- material language,
- icon family,
- illustration style,
- thematic consistency.

Ask:

> Do these assets belong to the same world?

---

## ASSET-3 — Technical Quality

Evaluate:

- resolution,
- compression,
- formats,
- geometry,
- texture efficiency,
- loading size,
- scaling,
- browser/runtime compatibility,
- technical cleanliness.

---

## ASSET-4 — Integration & Lifecycle

An excellent asset sitting unused in a directory earns nothing here.

Evaluate:

- loading,
- runtime use,
- correct placement,
- lifecycle,
- unloading/disposal where applicable,
- fallback behavior.

Ask:

> Are assets actually part of the product rather than part of the repository?

---

## ASSET-5 — Reuse / Provenance / Accessibility

Evaluate as applicable:

- reusable asset systems,
- licensing/provenance,
- attribution,
- alt text,
- accessible alternatives,
- semantic use,
- maintainable organization.

---

# 7. UX SCORE — 20 POINTS

UX evaluates how effectively users accomplish their goals.

---

## UX-1 — Task Efficiency

Evaluate:

- unnecessary steps,
- repetitive work,
- path length,
- workflow friction,
- control placement,
- shortcuts.

Ask:

> How much work does the interface make the user do unnecessarily?

---

## UX-2 — Discoverability & Onboarding

Evaluate:

- learnability,
- navigation,
- feature discovery,
- contextual guidance,
- empty states,
- onboarding,
- terminology.

Ask:

> Can a capable new user figure this out without being taught the entire product?

---

## UX-3 — Feedback & Recovery

Evaluate:

- confirmations,
- undo,
- error recovery,
- progress,
- state communication,
- failure explanation,
- destructive action protection.

Ask:

> Does the system keep the user oriented when things change or fail?

---

## UX-4 — Accessibility & Input Quality

Evaluate relevant:

- keyboard,
- pointer,
- touch,
- focus,
- semantic controls,
- reduced motion,
- accessible names,
- contrast,
- target sizes,
- assistive technology.

---

## UX-5 — Predictability & Persistence

Evaluate:

- remembered preferences,
- state restoration,
- consistent behavior,
- deterministic interaction,
- sensible defaults,
- session continuity.

Ask:

> Does the application behave like it remembers how the user works?

---

# 8. SCORE BANDS

Interpret totals as:

```text
00–39  CRITICAL
40–54  FRAGILE
55–69  FUNCTIONAL
70–79  STRONG
80–89  POLISHED
90–95  EXCEPTIONAL
96–100 NEAR-CEILING
```

A score above 90 requires unusually strong evidence.

Do not hand out 100/100 because tests pass.

100 means there is effectively no meaningful high-value opportunity visible across any of the 25 scored dimensions.

That should be extremely rare.

---

# 9. BASELINE BEFORE CHANGES

Before implementation:

1. inspect the project,
2. run it where feasible,
3. inspect representative workflows,
4. inspect assets,
5. inspect architecture,
6. run available validation,
7. assign all 25 baseline scores.

Produce internally:

```text
BASELINE QUALITY SCORECARD

UI
Hierarchy & Composition        _/4
Visual-System Cohesion         _/4
Readability & Density          _/4
Responsive Quality             _/4
States & Feedback              _/4
UI TOTAL                       _/20

WOW
Project Identity               _/4
Meaningful Reactivity          _/4
Tactility / Immersion          _/4
Surprise / Intelligence        _/4
Authorial Finish               _/4
WOW TOTAL                      _/20

BACKEND
Correctness & Integration      _/4
Reliability & Recovery         _/4
Performance & Lifecycle        _/4
Architecture & Maintainability _/4
Build/Security/Observability   _/4
BACKEND TOTAL                  _/20

ASSETS
Completeness                   _/4
Cohesion                       _/4
Technical Quality              _/4
Integration                    _/4
Reuse/Provenance/Accessibility _/4
ASSETS TOTAL                   _/20

UX
Task Efficiency                _/4
Discoverability                _/4
Feedback & Recovery            _/4
Accessibility & Input          _/4
Predictability & Persistence   _/4
UX TOTAL                       _/20

TOTAL                          _/100
```

Every score requires a concise reason.

Do not assign the score you hope to achieve.

Score the project that actually exists.

---

# 10. CONFIDENCE TAGS

Assign every score one confidence state:

- `VERIFIED`
- `STRONG_EVIDENCE`
- `PARTIAL_EVIDENCE`
- `UNVERIFIED`

Example:

```text
UX-4 Accessibility & Input
Score: 2/4
Confidence: VERIFIED
Evidence: keyboard inspection exposes inaccessible custom controls and missing focus indicators.
```

A score based only on source inspection should not pretend to contain runtime certainty.

---

# 11. ENVIRONMENT PREFLIGHT

Before mutation establish:

- repository root,
- repository identity,
- branch,
- HEAD,
- remotes,
- upstream,
- ahead/behind state,
- working-tree state,
- runtime/toolchain,
- build system,
- test system.

Record existing dirty files.

Never automatically:

- reset,
- discard,
- overwrite,
- stage,
- stash,
- delete

pre-existing user work.

If the wrong repository is open:

STOP.

---

# 12. UNDERSTAND THE PROJECT

Inspect:

- architecture,
- application entry points,
- primary screens/routes,
- README,
- project instructions,
- operational state/project bible if present,
- current assets,
- test structure,
- build configuration,
- deployment configuration,
- recent relevant history.

Run the application when feasible.

Determine:

### Purpose

Why does this project exist?

### Audience

Who is it for?

### Core loop

What repeated activity defines the product?

### Primary journey

What absolutely needs to work?

### Existing strengths

What should be amplified?

### Existing weaknesses

What materially holds the project back?

### Identity

What makes this project itself?

---

# 13. PROTECTED CAPABILITY MANIFEST

Before improving anything, identify verified behavior that must survive.

Assign:

```text
INV-01
INV-02
INV-03
...
```

Examples:

- project launches,
- critical workflow succeeds,
- save/load works,
- existing format compatibility remains,
- renderer initializes,
- key API remains stable,
- deployment path succeeds.

These are non-regression obligations.

A score improvement that destroys a protected capability is invalid.

---

# 14. BUILD THE OPPORTUNITY MAP

Do not immediately start editing.

For every scorecard dimension below 4, identify candidate interventions.

Each candidate must include:

```text
Candidate:
Target dimension:
Current problem:
Expected quality delta:
User/system benefit:
Implementation cost:
Regression risk:
Validation method:
Dependencies:
```

Do not optimize for the NUMBER of candidates.

Optimize for:

# MARGINAL QUALITY UPLIFT.

Prefer candidates that improve several weak realities at once without being counted several times.

---

# 15. QUALITY-DELTA HYPOTHESIS

Every selected intervention needs this causal chain:

```text
observed weakness
    ->
specific intervention
    ->
expected behavioral/experiential improvement
    ->
evidence capable of proving it
```

If you cannot articulate that chain:

reject the intervention.

---

# 16. PRIORITIZATION MODEL

Prioritize work using:

### Impact

How materially will this improve the project?

### Confidence

How strong is the evidence that it will help?

### Identity Fit

Does it strengthen THIS project?

### Leverage

Does it unlock or improve other valuable work?

### Cost

How much complexity does it add?

### Regression Risk

What existing behavior could it damage?

Prefer:

```text
high impact
high confidence
high identity fit
high leverage
reasonable cost
low/moderate regression risk
```

Do not chase low-value easy wins merely because they are easy.

---

# 17. SCORE-DELTA PRIORITIZATION

Pay special attention to:

- any dimension scoring 0 or 1,
- entire categories below 12/20,
- dimensions that bottleneck several others,
- high-value 2→3 opportunities,
- project-specific 3→4 opportunities.

A 1→3 improvement is often more valuable than four separate 3→4 polish attempts.

Do not chase perfect scores while major weaknesses remain.

---

# 18. INTERVENTION PORTFOLIO

Before major implementation, select a coherent intervention portfolio.

There is no mandatory number.

A strong pass could contain:

- 12 deep improvements,

or:

- 35 medium improvements,

or:

- another coherent set.

The number is irrelevant.

What matters is:

- coverage,
- materiality,
- integration,
- quality delta,
- evidence.

Avoid hundreds of unrelated micro-edits.

---

# 19. UI IMPROVEMENT PRINCIPLES

UI interventions should improve actual visible systems such as:

- hierarchy,
- layout,
- typography,
- spacing,
- component consistency,
- responsive behavior,
- state visibility,
- information density,
- dialogs,
- panels,
- navigation,
- controls,
- visualization.

Bundle related microscopic changes into one coherent intervention.

Example:

Do NOT treat:

- border,
- padding,
- radius,
- shadow

as four improvements.

Treat the rebuilt component hierarchy as the intervention.

---

# 20. WOW IMPROVEMENT PRINCIPLES

Interpret "wow me" as:

> discover what this project could uniquely do that its current version has not yet realized.

Seek:

- project-specific motion,
- dynamic visualization,
- meaningful reactivity,
- tactile manipulation,
- spatial transitions,
- contextual intelligence,
- progressive revelation,
- visualization of hidden system state,
- surprising but useful affordances,
- delightful discoveries.

Ask:

> What could this project do that would feel strange or pointless in almost any unrelated application?

That is fertile territory.

Avoid generic AI-design clichés:

- meaningless neon,
- excessive glassmorphism,
- particle spam,
- animated gradients everywhere,
- pointless 3D,
- bounce-on-everything animation,
- huge marketing typography inside tools.

WOW should emerge from purpose.

---

# 21. BACKEND IMPROVEMENT PRINCIPLES

Strengthen actual project machinery.

Potential targets include:

- data correctness,
- state architecture,
- persistence,
- concurrency,
- workers,
- algorithms,
- caching,
- performance,
- lifecycle,
- events,
- serialization,
- networking,
- recovery,
- offline behavior,
- security,
- deterministic behavior,
- build reliability.

Do not create technically impressive modules with no production caller.

A backend improvement must serve the application.

---

# 22. ASSET IMPROVEMENT PRINCIPLES

Assets may include:

- icons,
- illustrations,
- textures,
- models,
- materials,
- shaders,
- sprites,
- sounds,
- diagrams,
- maps,
- fonts,
- visualizations,
- project-specific datasets.

Prefer coherent asset systems over random additions.

Every improved or introduced asset must have a purpose.

Unused assets do not increase the score.

---

# 23. UX IMPROVEMENT PRINCIPLES

UX interventions should improve:

- workflow length,
- discoverability,
- onboarding,
- accessibility,
- feedback,
- undo/recovery,
- keyboard/touch behavior,
- smart defaults,
- persistence,
- navigation,
- error handling,
- cognitive load.

Where practical document:

```text
BEFORE
user does X -> Y -> Z

AFTER
user does A -> B
```

or equivalent evidence of reduced friction.

---

# 24. CROSS-DOMAIN LEVERAGE

Seek interventions with legitimate cross-domain effects.

Example:

```text
backend exposes meaningful state
        ->
UI makes state visible
        ->
asset system represents it coherently
        ->
UX makes it understandable
        ->
WOW turns it into a memorable interaction
```

This is excellent.

Do NOT score the same underlying quality improvement five times.

Score each category based on the resulting category-level quality, not based on change count.

---

# 25. IMPLEMENTATION ORDER

Prefer:

## Phase A — Technical foundation

Fix structural/backend problems blocking quality.

## Phase B — Asset foundation

Create, normalize, optimize, or replace needed assets.

## Phase C — UX architecture

Improve workflows and state behavior.

## Phase D — UI expression

Make those systems legible and coherent.

## Phase E — Distinctive WOW layer

Add memorable project-specific finish once fundamentals are sound.

Do not use visual spectacle to conceal bad architecture.

---

# 26. NO PLACEHOLDER UPLIFT

Do not improve scores because you added:

- TODOs,
- mock screens,
- fake telemetry,
- static fake data,
- dead controls,
- disconnected classes,
- unused assets,
- placeholder graphics,
- nonfunctional buttons,
- synthetic benchmark values.

These may actually LOWER the score.

---

# 27. PRODUCTION INTEGRATION RULE

For substantial functionality, identify the real path.

Examples:

```text
user action
-> handler
-> application state/service
-> actual behavior
-> visible/persisted result
```

or:

```text
request
-> validation
-> domain logic
-> storage
-> response
```

If no legitimate runtime path exists:

the implementation is not integrated.

---

# 28. TEST QUALITY RULE

For tests ask:

> Would this test fail if the claimed behavior were fake?

Weak evidence:

```text
expect(x).toBeDefined()
expect(result.length).toBeGreaterThan(0)
```

when the actual claim is sophisticated behavior.

Prefer:

- state transitions,
- known reference cases,
- invariants,
- round trips,
- boundary cases,
- error paths,
- actual integration,
- lifecycle behavior.

---

# 29. REGRESSION PROTECTION

When the pass repairs a real defect, leave durable protection where practical.

Possible mechanisms:

- regression test,
- fixture,
- assertion,
- validation rule,
- schema,
- integration test,
- release check.

Do not merely fix repeatable failures once.

---

# 30. RUNTIME QA

If the project is interactive:

run it.

UI, UX, and WOW scores cannot reach 4/4 from source inspection alone.

Inspect real behavior.

Exercise representative flows.

Look for:

- console/runtime errors,
- broken layout,
- interaction failures,
- focus issues,
- transition problems,
- stale loading states,
- asset failures,
- responsive breakage,
- performance problems.

---

# 31. VISUAL QA

For visual projects inspect rendered output.

Check:

- hierarchy,
- overlap,
- clipping,
- contrast,
- spacing,
- typography,
- z-order,
- component coherence,
- loading,
- empty states,
- errors,
- responsive behavior,
- motion timing,
- asset quality.

CSS source is not proof of visual quality.

---

# 32. ACCESSIBILITY

Accessibility affects both UX and potentially UI.

Inspect relevant:

- semantic controls,
- accessible names,
- keyboard navigation,
- focus,
- reduced motion,
- touch target size,
- contrast,
- assistive technology semantics.

Do not artificially inflate two scores from the exact same small accessibility change.

Judge the resulting category quality honestly.

---

# 33. PERFORMANCE

Quality improvements must not casually destroy runtime performance.

Watch where applicable:

- bundle weight,
- rendering,
- rerenders,
- memory,
- GPU resources,
- listeners,
- workers,
- timers,
- network,
- assets,
- allocation.

If adding expensive WOW work:

prove that the cost remains acceptable.

---

# 34. DEPENDENCY DISCIPLINE

Before adding a dependency ask:

1. Does the project already contain the needed capability?
2. Can existing primitives solve this cleanly?
3. Is the package maintained?
4. Is its cost justified?
5. Is its license compatible?
6. Is it removable?
7. Does it materially increase long-term complexity?

Do not install packages merely because they make implementation easier.

---

# 35. ITERATIVE SCORE CHECKS

After major cohesive work batches, reassess affected score dimensions.

Do not rescore the entire project after every small change.

Use checkpoints such as:

```text
BASELINE
FOUNDATION
EXPERIENCE
POLISH
FINAL
```

At each checkpoint ask:

> Is the actual quality improving, or are we merely producing more code?

If complexity rises without corresponding quality:

stop and reconsider.

---

# 36. SCORE INTEGRITY

A score may increase only when evidence supports the new level.

Example:

Baseline:

```text
UI-5 States & Feedback = 1
```

After implementing coherent:

- loading,
- disabled,
- selected,
- failure,
- progress states,

and verifying them in runtime:

```text
UI-5 States & Feedback = 3
```

That is legitimate.

Do not turn it into 4 because the implementation was difficult.

Difficulty does not earn points.

Quality does.

---

# 37. SCORE REGRESSION RULE

No category score may silently decrease.

If Backend improves from 11→17 while UX drops from 16→12:

the project has not simply improved by +2 overall.

A meaningful regression occurred.

Investigate and repair consequential score regressions.

Preserve existing strengths.

---

# 38. QUALITY FLOOR

Unless the project's nature makes a dimension legitimately inapplicable, the desired final state is:

```text
NO CATEGORY BELOW 15/20
```

This is not a feature quota.

It is a quality floor.

A project scoring:

```text
UI      19
WOW     19
BACK    19
ASSETS   7
UX      19
```

is not finished.

The asset system remains a major weakness.

When a dimension truly does not apply, mark it `N/A` and normalize scoring transparently rather than awarding free points.

---

# 39. TARGET BAND

The default aspirational target is:

# 85+/100 — POLISHED

But do not falsify scores merely to cross 85.

If the baseline is very low, a major legitimate uplift that does not reach 85 may still be valuable.

In that case report:

`MAJOR UPLIFT ACHIEVED — FURTHER PASS REQUIRED`

rather than inflating the score.

If baseline already exceeds 85:

do not stop.

Attack the weakest dimensions and highest-value remaining opportunities.

The task is about meaningful uplift, not merely crossing a threshold.

---

# 40. NEAR-CEILING RULE

Scores above 90 require increasing skepticism.

For every 4/4 ask:

> What meaningful weakness would a hostile reviewer point out?

If one exists:

the score may actually be 3.

A project should not reach 95+ because an agent became emotionally attached to its own implementation.

---

# 41. PLATEAU DETECTION

Stop adding improvements when:

- the highest remaining opportunities have low marginal value,
- remaining changes are mostly subjective,
- complexity cost exceeds expected quality gain,
- additional work would threaten stable behavior,
- remaining improvements belong to a future feature phase,
- the pass has reached a defensible quality plateau.

Do NOT keep modifying the application merely because token budget remains.

Stopping intelligently is part of quality.

---

# 42. ADVERSARIAL REVIEW

After implementation, attack your own final score.

Ask:

- Which points are inflated?
- Which polish is superficial?
- Which backend feature is disconnected?
- Which assets remain generic?
- Which UX friction still obviously exists?
- Which WOW behavior is merely animation?
- Which interface state still feels unfinished?
- Which existing capability regressed?
- Which test would pass on fake behavior?
- Which runtime path has not actually been exercised?

Lower scores when evidence warrants it.

Do not defend the first scorecard.

Correct it.

---

# 43. DELTA SCORECARD

Create:

```text
QUALITY DELTA

                         BEFORE   AFTER   DELTA
UI                         __      __      __
WOW                        __      __      __
BACKEND                    __      __      __
ASSETS                     __      __      __
UX                         __      __      __
------------------------------------------------
TOTAL                      __      __      __
```

Then include all 25 dimensions.

Every positive delta requires supporting evidence.

---

# 44. INTERVENTION LEDGER

Maintain a ledger of substantive work performed.

This is NOT a quota.

Use IDs such as:

```text
IMP-001
IMP-002
IMP-003
```

Each entry includes:

```text
ID:
Problem:
Change:
Primary score dimension:
Secondary effects:
Evidence:
Status:
```

The ledger exists for traceability.

It is not a competition to maximize the number of rows.

Ten profound interventions may be better than fifty shallow ones.

---

# 45. INTERVENTION STATUS

Assign every attempted intervention:

- `REAL`
- `PARTIAL`
- `FAILED`
- `REJECTED`
- `ROLLED_BACK`
- `NOT_INTEGRATED`

Only `REAL` work may justify a positive score delta.

A rejected candidate is not a failure.

Rejecting weak work is part of the process.

---

# 46. VALIDATION LADDER

Discover project-specific commands first.

Run applicable:

## Static
- types,
- lint,
- schema,
- compile.

## Focused
- systems directly changed.

## Integration
- actual production flows.

## Full suite
- repository-required tests.

## Production build
- shipping configuration.

## Specialized
where relevant:
- security,
- accessibility,
- bundle,
- benchmark,
- asset integrity,
- packaging,
- reproducibility.

Do not invent irrelevant validation theater.

---

# 47. CLEAN BUILD

Where practical verify the project does not rely on hidden stale state.

Watch for:

- untracked generated files,
- global dependencies,
- stale output,
- absolute machine paths,
- manually copied resources.

Use a safe isolated validation route where available.

Do not destroy the working tree.

---

# 48. RUNTIME-SPECIFIC PROOF

Some behavior requires its real runtime.

Examples:

- Web Worker,
- WebGL,
- WebGPU,
- service worker,
- browser storage,
- GPU resources,
- audio,
- filesystem behavior,
- native runtime behavior.

Mocks or fallback paths do not prove environment-specific behavior.

If proof is unavailable:

mark it `UNVERIFIED`.

Do not convert inference to proof.

---

# 49. DOCUMENTATION TRUTH SWEEP

Update relevant current-state documentation.

Remove stale claims.

Correct:

- feature descriptions,
- architecture descriptions,
- walkthroughs,
- implementation logs,
- comments,
- README claims

when they materially disagree with reality.

Preserve historical records when appropriate.

Do not rewrite history to make the project look cleaner.

---

# 50. REQUIREMENT TRACEABILITY

Before closure verify every controlling requirement.

At minimum:

```text
R01 Baseline scorecard completed before improvements
R02 All 25 dimensions scored with evidence
R03 Highest-value weaknesses were prioritized
R04 UI materially improved
R05 WOW/distinctive quality materially improved
R06 Backend materially improved
R07 Assets materially improved
R08 UX materially improved
R09 No category score was inflated from unverified work
R10 Protected capabilities survived
R11 Major regressions are absent
R12 Relevant runtime QA occurred
R13 Required validation passes
R14 Production build succeeds when applicable
R15 Documentation matches current state
R16 Final scorecard is adversarially rescored
R17 Git diff is understood
R18 Only authorized work is committed
R19 Push is remotely verified
R20 CI/deployment is verified when applicable
```

Do not mark a requirement PASS from intention.

---

# 51. ONE BOUNDED FINAL REPAIR PASS

If final validation reveals:

- a regression,
- an unjustified score,
- broken build,
- failed requirement,
- disconnected feature,

perform one focused closure repair.

Protect already validated behavior.

Rerun affected evidence.

Do not enter endless polishing.

---

# 52. DIFF-SCOPE AUDIT

Before Git staging inspect:

```text
git status --short
git diff
```

Review:

- additions,
- modifications,
- deletions,
- renames,
- dependencies,
- lockfiles,
- configuration,
- CI,
- assets,
- generated output.

Classify:

```text
AUTHORIZED
REQUIRED_SUPPORT
PRE_EXISTING
UNRELATED
UNKNOWN
```

Do not commit `UNRELATED` or `UNKNOWN`.

---

# 53. STAGE DELIBERATELY

Stage only intended work.

Do not blindly use:

```text
git add -A
```

when unrelated dirty state exists.

Inspect the staged diff.

---

# 54. COMMIT

Use a supplied exact commit message when present.

Otherwise use a truthful message such as:

```text
improve: comprehensive project quality uplift
```

Do not claim "final" or "complete" unless evidence supports it.

Capture the resulting commit SHA.

---

# 55. PUSH

Push the current authorized branch to its configured upstream.

Derive:

- branch,
- remote,
- upstream.

Do not assume:

- `main`,
- `origin`,
- GitHub.

Never force push.

Verify remote state after push.

---

# 56. CI / DEPLOYMENT

If relevant CI exists:

verify the final commit's actual status.

Distinguish:

- PASS,
- FAIL,
- PENDING,
- NOT_TRIGGERED,
- UNAVAILABLE,
- NOT_APPLICABLE.

Local tests are not CI.

If deployment applies:

verify the deployed revision.

Do not invent deployment infrastructure.

---

# 57. RELEASE CONSISTENCY TRIANGLE

Before completion align:

```text
SOURCE
final repository revision

VALIDATION
evidence run against that source

DELIVERY
remote/deployed artifact derived from that source
```

If any point references a different revision:

closure is not proven.

---

# 58. FINAL SCORECARD

Produce:

```text
# FINAL QUALITY SCORECARD

UI
Hierarchy & Composition        BEFORE _/4  AFTER _/4  DELTA _
Visual-System Cohesion         BEFORE _/4  AFTER _/4  DELTA _
Readability & Density          BEFORE _/4  AFTER _/4  DELTA _
Responsive Quality             BEFORE _/4  AFTER _/4  DELTA _
States & Feedback              BEFORE _/4  AFTER _/4  DELTA _
UI TOTAL                       BEFORE _/20 AFTER _/20 DELTA _

WOW
Project Identity               BEFORE _/4  AFTER _/4  DELTA _
Meaningful Reactivity          BEFORE _/4  AFTER _/4  DELTA _
Tactility / Immersion          BEFORE _/4  AFTER _/4  DELTA _
Surprise / Intelligence        BEFORE _/4  AFTER _/4  DELTA _
Authorial Finish               BEFORE _/4  AFTER _/4  DELTA _
WOW TOTAL                      BEFORE _/20 AFTER _/20 DELTA _

BACKEND
Correctness & Integration      BEFORE _/4  AFTER _/4  DELTA _
Reliability & Recovery         BEFORE _/4  AFTER _/4  DELTA _
Performance & Lifecycle        BEFORE _/4  AFTER _/4  DELTA _
Architecture & Maintainability BEFORE _/4  AFTER _/4  DELTA _
Build/Security/Observability   BEFORE _/4  AFTER _/4  DELTA _
BACKEND TOTAL                  BEFORE _/20 AFTER _/20 DELTA _

ASSETS
Completeness                   BEFORE _/4  AFTER _/4  DELTA _
Cohesion & Art Direction       BEFORE _/4  AFTER _/4  DELTA _
Technical Quality              BEFORE _/4  AFTER _/4  DELTA _
Integration & Lifecycle        BEFORE _/4  AFTER _/4  DELTA _
Reuse/Provenance/Accessibility BEFORE _/4  AFTER _/4  DELTA _
ASSET TOTAL                    BEFORE _/20 AFTER _/20 DELTA _

UX
Task Efficiency                BEFORE _/4  AFTER _/4  DELTA _
Discoverability & Onboarding   BEFORE _/4  AFTER _/4  DELTA _
Feedback & Recovery            BEFORE _/4  AFTER _/4  DELTA _
Accessibility & Input          BEFORE _/4  AFTER _/4  DELTA _
Predictability & Persistence   BEFORE _/4  AFTER _/4  DELTA _
UX TOTAL                       BEFORE _/20 AFTER _/20 DELTA _

TOTAL                          BEFORE _/100
                               AFTER  _/100
                               DELTA  _
```

---

# 59. SCORE EVIDENCE

For every dimension whose score increased, provide a concise evidence statement.

Example:

```text
UX-3 Feedback & Recovery
2 -> 4

Evidence:
- destructive operation now exposes confirmation + undo
- recoverable failure state implemented
- runtime-tested failed request recovery
- regression test protects transition
```

Do not list every line of code.

Show why the score changed.

---

# 60. BIGGEST TRANSFORMATIONS

Report the strongest interventions, ordered by actual project impact.

Do not mechanically list everything.

Use:

```text
1. [transformation]
   Why it mattered:
   Score dimensions affected:
   Evidence:

2. ...
```

Include only the most important work.

---

# 61. REJECTED TEMPTATIONS

Briefly report significant ideas intentionally rejected because they were:

- generic,
- filler,
- duplicate,
- excessive,
- architecturally wrong,
- performance-negative,
- low-value,
- out-of-scope.

This proves selection quality.

More changes are not always better.

---

# 62. FINAL VERDICT

Use exactly one:

## TRANSFORMATIVE UPLIFT VERIFIED

Use when:

- score delta is substantial,
- project is strong across categories,
- no major regression remains,
- validation is strong,
- evidence supports the score.

## MATERIAL UPLIFT VERIFIED

Use when:

- quality clearly improved,
- important weaknesses were repaired,
- remaining deficiencies prevent calling the result transformative.

## UPLIFT PARTIALLY VERIFIED

Use when:

- improvements exist,
- important runtime/validation evidence remains missing.

## VERIFIED INCOMPLETE

Use when:

- mandatory requirements or major quality defects remain.

## BLOCKED

Use when:

- the pass cannot safely continue.

Do not choose the verdict based solely on total score.

---

# 63. FINAL CLOSURE REPORT

Return:

```text
# Project Quality Uplift — Closure

Repository:
Branch:
Starting revision:
Final revision:

VERDICT:

## Score

Baseline:
Final:
Delta:
Baseline band:
Final band:

UI:       __ -> __ /20
WOW:      __ -> __ /20
Backend:  __ -> __ /20
Assets:   __ -> __ /20
UX:       __ -> __ /20

## Biggest transformations

1.
2.
3.
4.
5.
6.
7.
8.
9.
10.

## Score evidence

[only dimensions whose scores changed materially]

## Intervention ledger

REAL:
- ...

PARTIAL:
- ...

REJECTED / ROLLED BACK:
- ...

## Protected capabilities

PASS:
- ...

FAILED:
- ...

UNVERIFIED:
- ...

## Validation

Static:
Focused:
Integration:
Full suite:
Build:
Runtime:
Visual:
Accessibility:
Performance:
Security:
Other:

## Diff scope

Authorized:
Pre-existing preserved:
Unexpected:
Dependencies/config changes:

## Git

Commit:
Remote:
Push:
Remote revision:
Working tree:

## CI / Delivery

CI:
Deployment:
Delivered revision:
Smoke test:

## Remaining weaknesses

1.
2.
3.

## Rejected temptations

- ...

## Remaining uncertainty

None

OR

[exact unresolved items]

## Next action

None — current quality plateau is defensible.

OR

[one highest-value next action]
```

---

# 64. FINAL ANTI-GAMING RULE

The scorecard exists to make quality harder to fake, not easier.

Never increase a score because:

- more files changed,
- more code exists,
- more tests exist,
- more features exist,
- implementation took a long time,
- the agent believes the design is prettier,
- a README says it improved,
- the task expects a high score.

A score moves only when the actual project became demonstrably better.

---

# 65. THE REAL "WOW ME" STANDARD

Do not interpret "wow me" as:

> add spectacle.

Interpret it as:

> understand the project deeply enough to discover improvements that feel surprising before they exist and obvious afterward.

Expose hidden capability.

Remove frustrating friction.

Make difficult interactions elegant.

Make important state legible.

Make assets feel authored.

Make the architecture trustworthy.

Make the experience unmistakably itself.

Find the latent version of the project that was already trying to emerge.

Then build toward it.

---

# FINAL RULE

At the end, a skeptical engineer and a demanding user should both be able to inspect the project and independently conclude:

> This is materially better than the version we started with. The improvement is not based on a feature count. Weak areas were identified from evidence, the strongest interventions were chosen deliberately, the underlying systems became stronger, the experience became more coherent and distinctive, existing capabilities survived, and every point added to the final score can be defended.

The goal is not:

# MORE.

The goal is:

# BETTER.

Make the project fucking excellent.
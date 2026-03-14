# Bedrock PHP — VERSION_PLACEHOLDER

## 4. Declared Defaults

### Normative

Declared defaults are **binding assumptions** that apply unless a project explicitly documents a deviation.

Defaults exist to eliminate silent disagreement.

### Default 1: Single Application, Single Runtime

#### Rule
A Bedrock PHP system is a single PHP application running in a single primary runtime environment.

#### Implications
- One entry point for requests.
- One runtime version per environment.
- One deployment artifact.

#### Prohibitions
- No mixing multiple PHP runtimes in production.
- No polyglot services inside the same system boundary.

#### Stop rule
If you feel the need for multiple runtimes, stop and evaluate whether this is still one system.

---

### Default 2: One Way to Do Things

#### Rule
For any operational concern (deploying, configuring, running, debugging), there is exactly **one supported way**.

#### Implications
- Documentation describes one path, not options.
- Tooling supports the happy path only.
- Deviations are visible and intentional.

#### Prohibitions
- No “advanced” or “alternative” paths hidden in tribal knowledge.
- No parallel workflows that claim equivalence.

#### Stop rule
If two ways exist, remove one.

---

### Default 3: Environment Parity Over Perfection

#### Rule
Non-production environments should behave like production in ways that matter, not in every detail.

#### Implications
- Same PHP version and extensions.
- Same configuration mechanisms.
- Same deployment process.

#### Prohibitions
- No environment-specific code paths without documentation.
- No skipping steps in non-production that matter in production.

#### Stop rule
If staging exists only to “check a box,” stop maintaining it or make it useful.

---

### Default 4: Explicit Over Implicit

#### Rule
Behavior that matters operationally must be explicit and documented.

#### Implications
- Configuration is declared, not inferred.
- Startup fails fast on missing requirements.
- Defaults are visible and reviewable.

#### Prohibitions
- No hidden behavior triggered by environment quirks.
- No reliance on PHP.ini differences that are not tracked.

#### Stop rule
If someone cannot explain why the system behaves a certain way, make it explicit.

---

### Default 5: Replace Over Repair

#### Rule
When systems fail, replacement is preferred over in-place repair.

#### Implications
- Instances are disposable.
- Configuration and state are externalized.
- Recovery procedures favor redeploying.

#### Prohibitions
- No manual production debugging as the primary recovery method.
- No pets disguised as cattle.

#### Stop rule
If recovery requires SSH and hand edits, redesign the recovery path.

---

### Non-Normative

#### Why declared defaults matter
Most production incidents are caused not by bad code, but by **misaligned assumptions**.

Declared defaults:
- remove ambiguity
- expose disagreement early
- create shared expectations

Without defaults, every decision must be rediscovered under pressure.

---

#### Single runtime keeps systems legible
Multiple runtimes introduce:

- unclear ownership
- uneven upgrade paths
- inconsistent behavior

In PHP systems, this often shows up as:
- mixed PHP versions
- different extension sets
- incompatible tooling

Keeping one runtime forces coherence.

---

#### “One way” prevents folklore
When multiple workflows exist:

- documentation lies
- onboarding slows
- incidents require the “right” person

A single path may be imperfect, but it is **knowable**.

If a second path is genuinely better, replace the first — don’t add it.

---

#### Environment parity is about risk, not aesthetics
Perfect parity is impossible.

What matters:
- deployment mechanics
- configuration shape
- runtime behavior

What usually does *not* matter:
- instance size
- traffic volume
- exact infrastructure topology

Optimize parity where mistakes are expensive.

---

#### Implicit behavior hides landmines
Implicit behavior:

- surprises new team members
- breaks silently during upgrades
- is difficult to test

Common offenders in PHP:
- php.ini drift
- extension availability
- error reporting differences

Making these explicit reduces future outages.

---

#### Replace beats repair under pressure
Humans are bad at careful reasoning during incidents.

Replacement:
- is repeatable
- is faster
- reduces variance

If the fastest way to recover is redeploying, you have designed well.

---

#### Things to watch for
Defaults erode when:

- teams say “just this once”
- operational shortcuts become habits
- new tools are added without removing old ones

If defaults are no longer true, update them or exit the standard.

---

**Status:** Draft — Chapter 4

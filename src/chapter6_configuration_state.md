# Bedrock PHP — v1.0

## 6. Configuration & State

### Normative

### Principle
Configuration defines *how* the system behaves; state defines *what* the system remembers. Confusing the two creates fragile systems.

---

### Rule 1: Configuration Is External and Explicit

#### Rule
All configuration is provided to the application externally and is explicit.

#### Implications
- Configuration is environment-scoped.
- Required configuration is validated at startup.
- Configuration is reviewable alongside code changes.

#### Prohibitions
- No configuration hard-coded in application logic.
- No configuration derived implicitly from environment quirks.
- No “magic defaults” that materially alter behavior without visibility.

#### Stop rule
If a behavior change cannot be explained by a configuration change, stop and make it explicit.

---

### Rule 2: Secrets Are Not Configuration Files

#### Rule
Secrets are managed separately from non-secret configuration and are never committed to source control.

#### Implications
- Secrets are injected at runtime via environment variables or a secrets provider.
- Secret access follows least-privilege principles.
- Secret rotation is planned and testable.

#### Prohibitions
- No secrets in repositories, images, or logs.
- No shared credentials across environments.

#### Stop rule
If a secret cannot be rotated without code changes, redesign secret handling.

---

### Rule 3: State Lives Outside the Application

#### Rule
Application instances are stateless. All durable state lives in external systems.

#### Implications
- Instances can be replaced at any time.
- Horizontal or vertical scaling does not risk data loss.
- Recovery procedures favor replacement over repair.

#### Prohibitions
- No writing durable data to local disk.
- No relying on instance memory for correctness.

#### Stop rule
If losing an instance loses data, stop and externalize state.

---

### Rule 4: Production Instances Are Immutable

#### Rule
Production instances are never modified in place to change behavior.

#### Implications
- Configuration changes require redeployments.
- Debugging does not involve live edits.
- Drift between instances is impossible by design.

#### Prohibitions
- No SSH-based configuration edits.
- No live patching of production instances.

#### Stop rule
If fixing an issue requires logging into a production box, redesign the workflow.

---

### Rule 5: Fail Fast on Misconfiguration

#### Rule
The application must fail loudly and early when required configuration is missing or invalid.

#### Implications
- Startup validation checks exist.
- Errors are clear and actionable.
- Misconfiguration does not produce partial or degraded behavior.

#### Prohibitions
- No silent fallbacks for required configuration.
- No continuing startup in an unknown state.

#### Stop rule
If misconfiguration results in undefined behavior, stop and add validation.

---

### Non-Normative

#### Configuration vs state (why the distinction matters)
Teams often blur configuration and state:

- feature flags stored in databases
- runtime decisions written to disk
- behavior changes driven by mutable data

This makes systems hard to reason about and harder to recover.

Configuration answers: *“How should the system behave?”*
State answers: *“What has happened?”*

Keep them separate.

---

#### Why external configuration scales better
External configuration:

- allows safe redeployments
- supports immutable infrastructure
- makes behavior reviewable

In PHP systems, this commonly means:
- environment variables
- managed configuration services
- checked-in example config with validation

The mechanism matters less than visibility and consistency.

---

#### Secrets deserve different handling
Secrets differ from configuration because:

- exposure has real impact
- rotation is inevitable
- access should be minimized

Treating secrets like normal config often leads to:
- accidental leaks
- fear of rotation
- brittle deploys

Design secret handling as a first-class concern.

---

#### Statelessness enables confidence
Stateless applications:

- are easier to scale
- are easier to recover
- are easier to reason about

If you are afraid to restart instances, the system owns you.

---

#### Immutable instances prevent drift
Drift occurs when:

- hotfixes are applied manually
- config differs subtly across instances
- debugging leaves residue

Immutability eliminates an entire class of bugs by design.

---

#### Fail fast beats limp-along
Failing fast:

- surfaces errors early
- reduces blast radius
- avoids corrupting state

A system that “mostly starts” is more dangerous than one that refuses to start.

---

#### Things to watch for
Configuration drift often shows up as:

- production-only bugs
- fear of restarts
- long-lived instances
- undocumented environment variables

These are signals to reassert the rules.

---

#### Practical use cases

**Healthy configuration looks like:**
- new environments spin up from documented config
- missing config causes immediate failure
- secrets can be rotated without deploy panic

**Unhealthy configuration looks like:**
- copying env files by hand
- mysterious production-only flags
- secrets that no one wants to touch

---

**Status:** Draft — Chapter 6

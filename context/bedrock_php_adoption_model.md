# Bedrock PHP

## Adoption Model

### Purpose of the Adoption Model

The Bedrock PHP adoption model defines **how teams are expected to use Bedrock PHP in practice**.

It exists to ensure that Bedrock PHP:

- reduces decision fatigue
- provides clarity without dogmatism
- remains a stable reference over time

Adoption is intentionally simple. Complexity in adoption would undermine the purpose of Bedrock PHP itself.

---

### Adoption as Alignment, Not Compliance

Adopting Bedrock PHP does not mean:

- blind adherence
- loss of engineering judgment
- inability to adapt to real constraints

It means:

- agreeing on a shared default posture
- treating Bedrock PHP as the **starting point** for decisions
- making deviations explicit rather than implicit

Bedrock PHP is a baseline of intent, not a mechanism of enforcement.

---

### Version Pinning

Teams adopt **a specific version** of Bedrock PHP.

- Adoption is always versioned (e.g. Bedrock PHP v1.0).
- Versions do not change after release.
- Teams do not automatically inherit updates.

Version pinning ensures:

- stability of assumptions
- reproducibility of decisions
- long-term clarity for future team members

Upgrading to a new version is a deliberate act, not a background process.

---

### Default Acceptance

Upon adoption, teams are expected to:

- accept Bedrock PHP defaults without modification
- treat them as the "normal" way of operating
- resist customization unless a real constraint exists

Defaults exist to **end discussion**, not to invite tuning.

If a default feels uncomfortable but causes no concrete harm, it should remain unchanged.

---

### Deviation Policy

Deviation from Bedrock PHP is allowed, but never silent.

A deviation must:

- be documented
- reference the Bedrock PHP rule being deviated from
- explain the concrete constraint that necessitated it
- describe the expected impact

Deviations must not be framed as preferences or optimizations.

Acceptable reasons include:

- regulatory requirements
- hard infrastructure constraints
- legacy commitments that cannot be removed safely

Unacceptable reasons include:

- personal taste
- trend alignment
- theoretical future scale

---

### Temporary Deviations

Some deviations are temporary by nature.

Temporary deviations must:

- include a review condition
- define what change would allow re-alignment with Bedrock PHP
- avoid becoming permanent by inertia

If a deviation has no clear exit condition, it should be treated as permanent and documented as such.

---

### Deviation Review Discipline

Deviation reviews should be:

- infrequent
- lightweight
- practical

The goal of review is not approval, but **intentionality**.

If a deviation becomes widely necessary, it may indicate:

- a missing constraint in Bedrock PHP
- a misalignment between Bedrock PHP and its intended audience

It does not automatically justify changing the document.

---

### Partial Adoption Is Discouraged

Bedrock PHP is designed to be adopted **as a whole**.

Selective adoption:

- weakens its effectiveness
- reintroduces decision ambiguity
- creates inconsistent expectations

If a team feels compelled to ignore large portions of Bedrock PHP, it is likely not a good fit.

---

### Organizational Responsibility

Adoption should be explicit at the organizational or team level.

Bedrock PHP is not intended to be:

- an individual preference
- an informal guideline
- an undocumented influence

Explicit adoption ensures that:

- expectations are shared
- future contributors understand the operating context
- decisions remain interpretable over time

---

### Relationship to Local Standards

Local standards may exist alongside Bedrock PHP, but they must:

- not contradict Bedrock PHP defaults
- not reintroduce forbidden patterns
- not weaken stop rules

Local standards should be smaller than Bedrock PHP, not larger.

If local standards grow beyond this, Bedrock PHP is no longer serving its purpose.

---

### When Not to Adopt Bedrock PHP

Bedrock PHP should not be adopted when:

- experimentation is the primary goal
- the system is expected to be short-lived
- rapid architectural change is unavoidable
- hyperscale infrastructure is a core requirement

In such cases, Bedrock PHP would introduce unnecessary friction.

---

### Adoption Exit

Teams may choose to stop following Bedrock PHP.

Exiting adoption should be:

- explicit
- documented
- justified by changed constraints

Quiet drift away from Bedrock PHP undermines its value.

Leaving is preferable to partial or unacknowledged divergence.

---

### Closing Statement

The Bedrock PHP adoption model is intentionally light.

It relies on:

- clarity over enforcement
- documentation over debate
- alignment over control

Its success depends not on strict adherence, but on **shared understanding and deliberate choice**.

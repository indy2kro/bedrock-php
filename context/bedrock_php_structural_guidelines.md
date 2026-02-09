# Bedrock PHP – Structural Guidelines

## 1. Purpose of This Document

This document defines the **structural rules** of Bedrock PHP.

It specifies **how the project is organized**, how content is layered, how sections relate to each other, and how growth is controlled over time.

Its goal is to prevent Bedrock PHP from becoming:
- a sprawling knowledge base
- a wiki
- a blog
- a dumping ground for opinions

Structure is treated as a **governance tool**, not a formatting choice.

---

## 2. Core Structural Principles

### 2.1 One Spine, No Forks

Bedrock PHP has **one primary spine**.

- There is exactly one canonical structure per major version.
- There are no parallel “editions”, “tracks”, or “flavors”.
- Environment-specific deviations are handled through appendices, not forks.

If a structural change would require duplicating large sections, the change must be rejected or deferred to a future major version.

---

### 2.2 Depth Before Breadth

Bedrock PHP prioritizes:
- fewer sections
- deeper clarity
- stronger boundaries

New sections may only be added if they:
- eliminate recurring decisions
- replace existing ambiguity
- reduce the need for external references

AI or human contributors must justify *why a new section reduces complexity*, not why it is useful.

---

### 2.3 Structure Reflects Operational Reality

The order of sections must follow **how systems are actually reasoned about in production**, not how technologies are categorized.

Preferred ordering:
1. Purpose and scope
2. Defaults and constraints
3. Deployment and operations
4. Observability and failure
5. Performance and limits
6. Maintenance and exit

Conceptual material may not be placed after operational sections.

---

## 3. Document Hierarchy

### 3.1 Top-Level Sections (Fixed)

Each Bedrock PHP version must contain exactly these top-level sections:

1. Purpose & Scope
2. Adoption Model
3. Core Values (Operational)
4. Declared Defaults
5. Deployment & Infrastructure
6. Configuration & State
7. Observability
8. Performance & Scaling Limits
9. Security Posture
10. Maintenance & Decommissioning
11. When to Leave Bedrock PHP
12. Version Policy

No new top-level sections may be added in a minor version.

---

### 3.2 Subsections (Controlled)

- Subsections exist to clarify rules, not to add optionality.
- Each subsection must answer **one question only**.
- If a subsection grows beyond clarity, it must be split or reduced.

Subsections must never exist solely to:
- explain background theory
- justify trends
- showcase tooling

---

## 4. Rule-Centered Structure

### 4.1 Every Section Must Contain Rules

Each section must include at least one:
- explicit rule
- explicit prohibition
- explicit limit

Narrative-only sections are not allowed.

---

### 4.2 Rule Format

Rules must be expressed as:

- “We do X.”
- “We do not do Y.”
- “We stop when Z happens.”

Avoid conditional phrasing unless the condition is a hard cutoff.

---

## 5. Appendices and Profiles

### 5.1 Purpose of Appendices

Appendices exist to:
- handle environmental deviations
- document edge cases
- record rationale

They must not redefine core philosophy.

---

### 5.2 Profiles (Deferred Feature)

Profiles (e.g. cloud-specific deviations) are:
- optional
- non-core
- additive only

Profiles may override defaults **only where strictly necessary**.

Profiles must never:
- introduce new values
- relax limits globally
- contradict stop rules

---

## 6. Growth and Expansion Rules

### 6.1 The “Replace or Reject” Rule

Any proposed addition must:
- replace an existing section, or
- remove ambiguity elsewhere

If neither is true, the addition must be rejected.

---

### 6.2 No Structural Drift

Minor versions may:
- clarify wording
- tighten rules
- remove ambiguity

Minor versions may not:
- add new concepts
- reorder major sections
- expand scope

Structural changes require a major version.

---

## 7. Cross-Referencing Discipline

- Cross-references should be rare.
- Circular references are forbidden.
- A section should be understandable in isolation.

If heavy cross-referencing is required, the structure is wrong.

---

## 8. Removal Is a First-Class Operation

### 8.1 Scheduled Deletion

Every major version must:
- remove at least one rule
- delete at least one section or subsection

If nothing can be removed, the version should not be released.

---

### 8.2 Deletion Criteria

Content may be removed if:
- it no longer reduces decisions
- it addresses solved problems
- it encourages optionality
- it requires frequent clarification

---

## 9. Structural Anti-Patterns

The following structures are forbidden:

- FAQ sections
- “Common pitfalls” lists
- “Further reading” sections
- Tool matrices
- Comparison tables
- Roadmaps beyond the current version
- Mixing rules, rationale, and examples without explicit separation

These patterns increase surface area without increasing authority.

---

## 10. Structural Review Checklist

Before accepting any structural change, ask:

1. Does this reduce decision-making?
2. Does this introduce a new choice?
3. Does this expand the audience implicitly?
4. Does this weaken the main spine?

If any answer is yes, the change must be rejected or revised.

---

### **11. Layered Content Model**

Bedrock PHP uses a **layered content model** to balance authority with depth.

The layers are strictly ordered and must not be mixed.

----------

### **11.1 Normative Layer (The Standard)**

The normative layer defines the Bedrock PHP standard.

It contains:

-   rules
-   defaults
-   prohibitions
-   limits
-   stop conditions

This layer must be:

-   complete on its own
-   sufficient for correct adoption
-   readable without any additional context

If the normative layer is removed from a section, the section must still be actionable.

----------

### **11.2 Rationale Layer (Non-Normative)**

The rationale layer exists to explain **why** a rule exists.

It may include:

-   historical context
-   rejected alternatives
-   failure modes the rule prevents
-   opinionated reasoning

The rationale layer must be explicitly labeled as **Non-Normative**.

Rationale content must not:

-   introduce new rules
-   modify existing rules
-   soften prohibitions
-   add conditional behavior

Disagreement with the rationale does not invalidate the rule.

----------

### **11.3 Implementation Layer (Non-Normative)**

The implementation layer provides **illustrative guidance**, not prescriptions.

It may include:

-   one minimal example
-   a checklist
-   a template
-   a reference implementation outline

Implementation content must:

-   be explicitly labeled as **Non-Normative**
-   present a single acceptable approach
-   avoid tool comparisons or alternatives

Implementation examples exist to demonstrate feasibility, not to define preference.

----------

### **11.4 Layer Separation Rules**

Layers must be visually and structurally distinct.

-   The normative layer must be visible by default.
-   Rationale and implementation layers may be collapsible or secondary.
-   Normative content must never depend on expanded content for clarity.

If a rule requires explanation to be understood, the rule is incorrectly written.

----------

### **11.5 Prohibited Layer Violations**

The following are forbidden:

-   embedding rules inside rationale text
-   adding optional behavior inside examples
-   presenting alternatives inside implementation notes
-   referencing rationale to justify exceptions

Any content that weakens the authority of the normative layer must be removed.

## 12. Final Structural Statement

Bedrock PHP is intentionally small.

Its structure is designed to:
- be read fully
- be adopted whole
- be stable under pressure

Growth is allowed only when it **removes more than it adds**.

Structure is not neutral. It is the primary defense against entropy.


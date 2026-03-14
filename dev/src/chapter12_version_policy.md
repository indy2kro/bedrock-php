# Bedrock PHP — dev

## 12. Version Policy

### Normative

### Principle
The standard itself must obey the same discipline it imposes: clarity, stability, and deliberate change.

---

### Rule 1: Bedrock PHP Is Versioned and Pinned

#### Rule
Bedrock PHP is adopted by **explicit version**, not by name alone.

#### Implications
- Projects declare a specific Bedrock PHP version (e.g., v1.0).
- Compliance claims always include the version.
- There is no concept of a floating or “latest” version.

#### Prohibitions
- No implicit upgrades.
- No claiming compliance without a pinned version.

#### Stop rule
If the version cannot be named, stop claiming compliance.

---

### Rule 2: Released Versions Are Frozen

#### Rule
Once released, a Bedrock PHP version is immutable.

#### Implications
- No silent edits.
- No retroactive rule changes.
- Errata require a new version.

#### Prohibitions
- No rewriting history.
- No “small tweaks” without a version bump.

#### Stop rule
If a change alters obligations, it requires a new release.

---

### Rule 3: Minor Versions Clarify, Major Versions Change Shape

#### Rule
Version numbers signal the scope of change.

- **Minor versions (v1.x)** may:
  - clarify wording
  - remove ambiguity
  - tighten boundaries
  - delete content
  - add examples

- **Major versions (v2.0)** may:
  - add or remove top-level chapters
  - restructure the document
  - change or remove rules

#### Prohibitions
- Minor versions must not add new obligations.
- Major versions must not grow indefinitely.

#### Stop rule
If a change increases cognitive load without removing something else, do not ship it.

---

### Rule 4: Every Major Version Removes Something

#### Rule
Each major version must explicitly remove at least one rule, chapter, or constraint.

#### Implications
- The standard resists unchecked growth.
- Complexity is pruned, not accumulated.

#### Prohibitions
- No additive-only major releases.

#### Stop rule
If nothing can be removed, the new version is not justified.

---

### Rule 5: Changes Must Reduce Decisions

#### Rule
Every change must demonstrably reduce ambiguity or decision-making.

#### Implications
- Changelogs explain *why* a change exists.
- Changes are evaluated against real confusion or failure modes.

#### Prohibitions
- No changes for completeness, symmetry, or aesthetics alone.

#### Stop rule
If a change does not make the standard easier to follow, revert it.

---

### Non-Normative

#### Why standards rot
Standards decay when they:

- grow without constraint
- accrete edge cases
- attempt to cover every scenario

Eventually they become unreadable and unenforceable.

Version discipline prevents this.

---

#### Freezing versions builds trust
When versions are frozen:

- teams know what they agreed to
- upgrades can be planned
- debates are resolved by reference

Silent changes destroy confidence.

---

#### Removal is an act of care
Deleting rules:

- forces prioritization
- reveals what no longer matters
- keeps the document sharp

A standard that only grows will eventually fail.

---

#### Changelogs are part of the contract
A good changelog answers:

- what changed
- why it changed
- what problem it solves
- what it replaced or removed

Anything less is noise.

---

#### Example changelog entry

> **v1.1** — Clarified deployment rollback requirements.
> Reduced ambiguity around acceptable rollback mechanisms.
> Removed non-essential example that caused confusion.

This level of detail is sufficient.

---

#### Things to watch for
Version drift often appears as:

- undocumented edits
- “living documents” without releases
- teams following different interpretations

These are signals to formalize releases.

---

**Status:** Draft — Chapter 12

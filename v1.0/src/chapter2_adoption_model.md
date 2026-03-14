# Bedrock PHP — v1.0

## 2. Adoption Model

### Normative

#### Definition
Adopting Bedrock PHP means explicitly committing to its constraints **as a system**, not as a loose set of guidelines.

Bedrock PHP is adopted at the **project level**, not per-feature, per-team-member, or per-phase.

#### Valid adoption states
A project is in exactly one of the following states:

1. **Not using Bedrock PHP**
2. **Using Bedrock PHP vX.Y**
3. **Exiting Bedrock PHP vX.Y** (temporary, transitional)

There is no partial or implicit adoption.

#### Entry criteria
A project may adopt Bedrock PHP when:

- there is a clear owner for the system
- production users or downstream systems exist (or are imminent)
- the team agrees to prioritize operational stability over architectural freedom

Adoption must be **explicitly recorded** (e.g. in the repository README or an architecture decision record).

#### Version pinning
- A project must pin to a **specific Bedrock PHP version**.
- Upgrading Bedrock PHP is an intentional act, not an ambient change.
- A project may not claim compliance with multiple versions simultaneously.

#### Obligations
By adopting Bedrock PHP, the project agrees to:

- follow all normative rules in the selected version
- treat declared defaults as binding unless explicitly overridden
- document any deviations clearly and centrally

#### Prohibitions
- No selective adoption (“we follow most of it”).
- No retroactive claims of compliance.
- No silent divergence from declared defaults.

#### Stop rule
If more than one chapter requires documented deviations to operate the system, stop claiming Bedrock PHP compliance and begin an exit process.

---

### Non-Normative

#### Why adoption must be explicit
Most operational standards fail not because they are wrong, but because they are **ambiguous**.

When adoption is implicit:

- teams disagree on what rules apply
- exceptions accumulate without being named
- standards become decorative rather than enforceable

Making adoption explicit forces a clear answer to:

> “What rules are we actually operating under today?”

That clarity is more valuable than perfect rules.

#### Partial adoption is worse than none
A common failure mode looks like this:

- the team adopts the *language* of the standard
- only the convenient parts are followed
- the hard constraints are quietly ignored

This produces the worst outcome:

- complexity still grows
- confidence falsely increases
- failures are harder to reason about because assumptions no longer match reality

If a project cannot accept a rule, it is healthier to reject the standard than to pretend.

#### When to adopt Bedrock PHP
Good moments to adopt:

- greenfield projects with real production intent
- post-MVP stabilization phases
- ownership transitions between teams
- after a significant incident that revealed operational gaps

In these moments, constraints are usually welcomed rather than resisted.

#### When not to adopt (yet)
Bedrock PHP may be premature when:

- the system is a spike or proof-of-concept
- infrastructure choices are the primary unknown being explored
- the team expects the system to be short-lived

In these cases, defer adoption rather than dilute it.

#### Versioning as a forcing function
Pinning a version is not bureaucracy — it is protection.

It ensures:

- the rules you agreed to do not change underneath you
- upgrades are deliberate and reviewable
- disagreements can be resolved by pointing to a specific text

Treat Bedrock PHP versions like runtime versions: upgrade intentionally, not casually.

#### Common adoption pitfalls
Watch for these early warning signs:

- “We’ll clean this up once things settle down.”
- “This one exception doesn’t really count.”
- “Everyone knows how this works.”

These phrases usually precede drift.

#### Practical adoption checklist
Before declaring adoption:

- [ ] Name a system owner
- [ ] Pin a Bedrock PHP version
- [ ] Record adoption in the repo
- [ ] Identify known deviations (if any)
- [ ] Ensure the team understands the stop rules

If you cannot complete this checklist honestly, wait.

---

**Status:** Draft — Chapter 2

# Bedrock PHP — VERSION_PLACEHOLDER

## 3. Core Values (Operational)

### Normative

The following values are not aspirational. They are **operational constraints**. Each value exists only insofar as it changes decisions.

### Value 1: Boring is a Feature

#### Rule
Prefer solutions that are widely understood, long-lived, and operationally dull over novel or elegant alternatives.

#### Implications
- Choose tools with long track records in PHP production.
- Prefer official, well-supported features over third-party abstractions.
- Optimize for the median engineer, not the most senior one.

#### Prohibitions
- No introducing novelty primarily for interest, learning, or résumé value.
- No replacing a working, boring system without a concrete operational reason.

#### Stop rule
If the system is stable, understandable, and meeting targets, **stop changing it**.

---

### Value 2: Constraints Over Choice

#### Rule
Reduce the number of valid options wherever possible.

#### Implications
- Fewer supported ways to deploy, configure, and operate the system.
- Clear “this is how we do it” answers beat flexible frameworks.
- Defaults are binding unless explicitly overridden.

#### Prohibitions
- No maintaining multiple equivalent solutions to the same problem.
- No deferring decisions by saying “it depends” without documenting why.

#### Stop rule
If a decision has been made once and works, **do not reopen it** without new evidence.

---

### Value 3: Production Is the Only Truth

#### Rule
Behavior observed in production overrides assumptions made elsewhere.

#### Implications
- Production failures outweigh local success.
- Operational data is treated as authoritative.
- Debugging prioritizes production signals over reproduction attempts.

#### Prohibitions
- No dismissing incidents because they are “hard to reproduce.”
- No assuming staging behavior guarantees production behavior.

#### Stop rule
If production metrics are healthy, stop optimizing based on hypothetical risks.

---

### Value 4: Ownership Is Mandatory

#### Rule
Every system, component, and recurring operational task has a named owner.

#### Implications
- Ownership includes uptime, maintenance, and eventual deletion.
- Decisions have a responsible party, not a committee.

#### Prohibitions
- No shared or collective ownership without accountability.
- No “everyone knows how this works” components.

#### Stop rule
If no one can name the owner, stop expanding the system and assign ownership.

---

### Value 5: Deletion Is Progress

#### Rule
Removing systems, code paths, and infrastructure is a positive outcome.

#### Implications
- Decommissioning is planned, not accidental.
- Complexity reduction is valued equally to feature delivery.

#### Prohibitions
- No keeping unused systems “just in case.”
- No fear-driven retention of dead code or infrastructure.

#### Stop rule
If a system provides no active value, start deleting it.

---

### Non-Normative

#### Why values are operational
Many teams state values like “simplicity” or “reliability” but fail to encode them into rules.

Operational values:
- force tradeoffs
- eliminate debate during incidents
- provide justification for saying no

If a value does not change behavior under pressure, it is decorative.

---

#### Boring systems survive people
Engineers leave. Context disappears. Systems remain.

Boring systems:
- are easier to transfer
- are easier to debug at 3am
- are easier to delete safely

The goal is not to eliminate intelligence, but to avoid embedding it in fragile places.

---

#### Constraints reduce cognitive load
Every additional option:
- increases review time
- increases onboarding cost
- increases failure modes

Constraints create speed by removing the need to decide repeatedly.

Teams often mistake flexibility for empowerment; in practice, it often becomes paralysis.

---

#### Production reality beats theoretical correctness
Many outages occur because teams trusted:
- local tests
- staging environments
- architectural guarantees

over production signals.

Bedrock PHP treats production as the final arbiter, not an embarrassment to be explained away.

---

#### Ownership prevents entropy
Unowned systems drift because:
- maintenance is optional
- upgrades are deferred
- failures are someone else’s problem

Explicit ownership creates:
- faster decisions
- clearer accountability
- safer deletions

---

#### Deletion requires cultural permission
Teams often know something should be removed but delay because:
- “what if we need it later?”
- “someone might still be using it”
- “it’s not broken”

By treating deletion as progress, Bedrock PHP gives permission to simplify.

Deletion reduces:
- attack surface
- operational burden
- cognitive overhead

---

#### Things to watch for
Values erosion often shows up as:

- exceptions justified by urgency
- clever solutions without clear ownership
- systems no one wants to touch
- fear of removing anything

These are signals to re-anchor on the values.

---

**Status:** Draft — Chapter 3

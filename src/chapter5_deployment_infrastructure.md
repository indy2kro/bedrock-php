# Bedrock PHP — VERSION_PLACEHOLDER

## 5. Deployment & Infrastructure

### Normative

### Principle
Deployment is a **mechanical operation**, not a creative act. If deploying requires judgment, the system is incomplete.

---

### Rule 1: Exactly One Production Deployment Path

#### Rule
There is exactly **one** supported way to deploy to production.

#### Implications
- All production changes flow through the same pipeline.
- The deployment path is documented and automated.
- Access to deploy implies responsibility for production outcomes.

#### Prohibitions
- No manual production changes.
- No SSH-based deploys.
- No alternate pipelines “just for emergencies.”

#### Stop rule
If two ways to deploy exist, remove one.

---

### Rule 2: Deployments Are Automated, Repeatable, and Reversible

#### Rule
Every deployment must be:
- automated end-to-end
- reproducible from a clean checkout
- reversible to the previous known-good state

#### Implications
- Builds produce immutable artifacts.
- Rollbacks are faster than roll-forwards.
- Deployment does not depend on local developer state.

#### Prohibitions
- No snowflake servers.
- No mutable production instances.
- No “hot fixes” applied directly to running systems.

#### Stop rule
If rollback is unclear or slow, stop shipping features and fix deployment.

---

### Rule 3: One Production Branch

#### Rule
There is exactly one branch that deploys to production.

#### Implications
- Production history is linear and auditable.
- Releases are traceable to commits.

#### Prohibitions
- No ad-hoc production branches.
- No force-pushing production history.

#### Stop rule
If you cannot identify what code is in production, stop deploying.

---

### Rule 4: Minimal Infrastructure Surface Area

#### Rule
Use the smallest set of infrastructure components required to run the system.

#### Implications
- Prefer managed services over self-hosted ones.
- Avoid orchestration layers unless required by constraints.
- Infrastructure complexity must earn its keep.

#### Prohibitions
- No service meshes, custom schedulers, or bespoke platforms by default.
- No introducing infrastructure solely for future scale.

#### Stop rule
If infrastructure requires its own team to operate, reassess necessity.

---

### Rule 5: Environments Have Clear Roles

#### Rule
Each environment has a single, well-defined purpose.

- **dev**: disposable, fast feedback
- **staging**: production-like validation
- **production**: the only user-facing truth

#### Implications
- Production is never debugged directly.
- Staging mirrors production behavior, not scale.

#### Prohibitions
- No long-lived “almost production” environments.
- No environment-specific deployment logic.

#### Stop rule
If an environment’s purpose is unclear, remove it.

---

### Non-Normative

#### Why deployment must be boring
Deployments happen under stress:

- late nights
- incidents
- deadlines

A boring deployment system:
- reduces human error
- enables faster recovery
- builds confidence through repetition

Creativity belongs in product development, not release mechanics.

---

#### The myth of the emergency deploy
Teams often justify alternate deploy paths by citing emergencies.

In practice:
- emergencies are when humans are least reliable
- alternate paths are least tested

The safest emergency deploy is the **same one you always use**, executed calmly.

---

#### Immutable artifacts simplify everything
Immutable artifacts:
- make rollbacks trivial
- allow precise audits
- decouple build from deploy

Common PHP examples:
- versioned application packages
- container images
- read-only release directories

If you can change production without a new artifact, you have hidden risk.

---

#### Minimal infrastructure ages better
Infrastructure accumulates cost:

- maintenance
- upgrades
- knowledge

What felt cheap to add becomes expensive to keep.

Ask before adding infrastructure:
- What problem does this solve *today*?
- What breaks if we remove it?

If the answer is unclear, wait.

---

#### Environment sprawl is a smell
Extra environments often exist to:

- avoid deleting things
- compensate for weak deployment confidence
- satisfy vague safety feelings

Fewer environments with clear roles produce better outcomes.

---

#### Things to watch for
Early signs of deployment drift:

- “temporary” manual fixes
- undocumented rollback steps
- deployments requiring specific people
- fear around releasing

These indicate the system is becoming fragile.

---

#### Practical use cases

**Healthy deployment looks like:**
- a new engineer can deploy on day one
- rollback is a button or single command
- deploy frequency is limited by business choice, not fear

**Unhealthy deployment looks like:**
- long runbooks for routine releases
- hero engineers guarding production
- downtime accepted as normal

---

**Status:** Draft — Chapter 5

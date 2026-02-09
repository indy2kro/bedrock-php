# Bedrock PHP — v1.0

## 9. Security Posture

### Normative

### Principle
Security exists to reduce realistic risk over time, not to create the appearance of safety.

---

### Rule 1: Least Privilege Everywhere

#### Rule
Every credential, role, and access path grants only the minimum permissions required.

#### Implications
- Separate credentials per environment.
- Narrowly scoped database users.
- CI and automation credentials are limited and auditable.

#### Prohibitions
- No shared admin accounts.
- No long-lived, over-privileged credentials.

#### Stop rule
If a credential grants permissions "just in case," reduce it.

---

### Rule 2: Patch Predictably, Escalate Deliberately

#### Rule
Dependencies, runtimes, and infrastructure are patched on a predictable cadence.

#### Implications
- Patch and minor updates are routine maintenance.
- Critical security updates are accelerated.
- End-of-support timelines are tracked.

#### Prohibitions
- No deferring updates indefinitely.
- No surprise major upgrades during incidents.

#### Stop rule
If patching feels heroic, simplify the system.

---

### Rule 3: Secrets Are Centralized and Rotatable

#### Rule
Secrets are managed in a centralized system and can be rotated without code changes.

#### Implications
- Secrets are never logged.
- Access to secrets is monitored.
- Rotation procedures are tested.

#### Prohibitions
- No secrets embedded in images or binaries.
- No manual secret distribution.

#### Stop rule
If a secret cannot be rotated safely, redesign its usage.

---

### Rule 4: Production Access Is Restricted and Audited

#### Rule
Direct access to production systems is limited, time-bound, and auditable.

#### Implications
- Access is granted for a reason and revoked when no longer needed.
- Actions in production are attributable.

#### Prohibitions
- No standing, permanent production access for convenience.
- No unaudited changes.

#### Stop rule
If access cannot be explained or justified, revoke it.

---

### Rule 5: Prefer Boring, Proven Controls

#### Rule
Security controls should be widely understood and operationally proven.

#### Implications
- Use standard authentication and authorization mechanisms.
- Prefer managed security features over bespoke ones.

#### Prohibitions
- No custom crypto.
- No homegrown auth unless required by constraints.

#### Stop rule
If a control requires a specialist to explain, reconsider it.

---

### Non-Normative

#### Security is an operational discipline
Most real-world breaches occur due to:

- forgotten credentials
- unpatched systems
- excessive permissions

Not due to missing advanced defenses.

Operational discipline prevents more incidents than novelty.

---

#### Least privilege reduces blast radius
When something goes wrong:

- narrow permissions limit damage
- audit trails speed response

Over-privileged systems turn small mistakes into major incidents.

---

#### Predictable patching builds trust
Teams that patch regularly:

- fear updates less
- recover faster
- avoid forced upgrades

Security work should feel boring and routine.

---

#### Secret rotation is a design test
If rotating a secret causes panic:

- the system is too tightly coupled
- access boundaries are unclear

Designing for rotation improves overall system hygiene.

---

#### Production access is not a right
Permanent production access:

- erodes discipline
- hides risky behavior
- complicates incident review

Temporary, audited access protects both the system and the team.

---

#### Boring controls scale better
Well-known controls:

- are documented
- are supported
- have known failure modes

Custom security solutions often become liabilities when the original authors leave.

---

#### Things to watch for
Security drift often appears as:

- credentials shared informally
- upgrades postponed repeatedly
- access granted "temporarily" and forgotten

These are early warning signs, not minor issues.

---

#### Practical use cases

**Healthy security posture looks like:**
- routine dependency updates
- short-lived credentials
- clear access reviews

**Unhealthy security posture looks like:**
- fear of touching secrets
- ancient dependencies
- unknown production access paths

---

**Status:** Draft — Chapter 9

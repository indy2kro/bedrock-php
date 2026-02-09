# Bedrock PHP — v1.0

## 10. Maintenance & Decommissioning

### Normative

### Principle
A system is not finished when it ships. It is finished when it can be safely maintained and eventually removed.

---

### Rule 1: Every System Has a Named Owner

#### Rule
Every system, service, and recurring operational responsibility has a clearly named owner.

#### Implications
- Ownership includes uptime, maintenance, upgrades, and deletion.
- Owners are empowered to make changes and remove systems.

#### Prohibitions
- No collective or implicit ownership.
- No systems owned by teams that no longer exist.

#### Stop rule
If no owner can be named immediately, stop changes and assign one.

---

### Rule 2: Maintenance Is Scheduled Work

#### Rule
Routine maintenance is planned, visible, and treated as real work.

#### Implications
- Dependency updates are regular.
- Backups are tested.
- Operational debt is addressed deliberately.

#### Prohibitions
- No deferring maintenance indefinitely.
- No treating maintenance as optional or filler work.

#### Stop rule
If maintenance only happens during incidents, stop feature work and rebalance priorities.

---

### Rule 3: Backups Are Mandatory and Verified

#### Rule
All production state has automated backups that are periodically tested.

#### Implications
- Backup scope is explicit.
- Restore procedures are documented.
- Restore tests are performed.

#### Prohibitions
- No untested backups.
- No assumptions that backups "probably work."

#### Stop rule
If you cannot restore confidently, stop shipping changes until you can.

---

### Rule 4: Decommissioning Is a First-Class Process

#### Rule
Every system must have a defined decommissioning path.

#### Implications
- Deletion is planned, not accidental.
- Data handling decisions are explicit.
- Infrastructure is fully removed.

#### Prohibitions
- No indefinitely idle systems.
- No zombie infrastructure.

#### Stop rule
If a system has no users and no plan, begin decommissioning.

---

### Rule 5: Dormancy Is Not Stability

#### Rule
Systems without active usage or ownership are considered unhealthy.

#### Implications
- Dormant systems are reviewed.
- Unused components are removed.

#### Prohibitions
- No keeping systems "just in case."
- No indefinite pause without decision.

#### Stop rule
If a system is unused, decide: delete or recommit.

---

### Non-Normative

#### Ownership creates leverage
Named ownership:

- speeds decisions
- clarifies responsibility
- prevents entropy

Without owners, systems decay quietly until they fail loudly.

---

#### Maintenance debt compounds
Deferred maintenance:

- increases incident frequency
- makes upgrades scarier
- traps teams in outdated tooling

Regular maintenance keeps systems cheap to operate.

---

#### Backups only matter when restored
Backups fail for many reasons:

- incomplete coverage
- silent corruption
- outdated procedures

A backup that has never been restored is a liability, not an asset.

---

#### Deletion reduces risk
Removing systems:

- shrinks attack surface
- reduces operational burden
- lowers cognitive load

Deletion is often the highest-leverage reliability improvement.

---

#### Dormant systems rot
Unused systems:

- miss security updates
- lose knowledgeable owners
- surprise teams later

Treat inactivity as a decision point, not a neutral state.

---

#### Things to watch for
Maintenance drift often appears as:

- "we'll deal with it later"
- systems no one wants to touch
- backups no one has tested

These are signals to stop adding features.

---

#### Practical use cases

**Healthy maintenance looks like:**
- regular update cadence
- tested restores
- systems removed when obsolete

**Unhealthy maintenance looks like:**
- ancient dependencies
- fear of touching old systems
- infrastructure nobody remembers adding

---

**Status:** Draft — Chapter 10

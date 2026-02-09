# Bedrock PHP

## Declared Defaults

### Purpose of Declared Defaults

Declared Defaults define the **assumed operating posture** of Bedrock PHP.

They exist to eliminate repeated decision-making by establishing a single, defensible set of choices that teams can adopt without customization.

Defaults are not recommendations.
They are **the normal state**.

Anything not explicitly overridden is assumed to follow these defaults.

---

### General Rule

Bedrock PHP assumes:

- one primary application
- one primary deployment path
- one primary way of running PHP in production

Deviation is allowed, but only under documented constraint.

---

## Application Architecture

### Monolith First

Bedrock PHP defaults to a **single deployable application**.

- The application may be modular internally.
- It is deployed as one unit.
- It owns its primary data.

We do not introduce multiple services unless a clear, current constraint exists.

Future scale is not a valid reason.

---

### Clear Ownership Boundaries

Each application:

- owns its database schema
- owns its migrations
- owns its runtime configuration

Cross-application database access is forbidden.

---

## PHP Runtime

### Stable PHP Versions

Bedrock PHP runs **supported, non-experimental PHP releases**.

- We do not run development or preview versions.
- We do not skip major versions deliberately.
- Security and patch updates are applied promptly.
- Major version upgrades are driven by support timelines, not novelty.
- Minor version upgrades are batched and scheduled to avoid continuous churn.

Stability and predictability outweigh early adoption.

---

### One Runtime Configuration

Each environment uses:

- a single, shared PHP configuration
- minimal environment-specific overrides

Configuration drift is treated as a defect.

---

## Dependency Management

### Composer as the Only Dependency Mechanism

All PHP dependencies are managed through Composer.

- Vendored libraries are not allowed.
- Forks are avoided unless upstream is abandoned.

If a dependency cannot be managed cleanly via Composer, it is reconsidered.

---

### Conservative Dependency Selection

Dependencies must:

- be widely used
- be actively maintained
- solve a narrow problem

Dependencies that introduce frameworks, magic, or deep abstraction layers are avoided unless unavoidable.

---

## Framework Posture

### Frameworks Are Allowed, Not Required

Bedrock PHP does not mandate a specific framework.

If a framework is used:

- it must not obscure application flow
- it must not require heavy customization
- it must not dictate infrastructure complexity

Frameworks serve the application, not the other way around.

---

## Deployment

### Automated, Repeatable Deployments

Deployments are:

- automated
- repeatable
- reversible

Manual production changes are forbidden.

---

### One Deployment Path

There is exactly one supported way to deploy the application.

Alternate paths:
- increase cognitive load
- create silent drift
- complicate recovery

They are not allowed.

---

## Infrastructure

### Minimal Infrastructure Layers

Infrastructure defaults to:

- the minimum number of services required
- managed services where available
- simple networking

We avoid introducing:

- service meshes
- custom orchestration layers
- complex networking setups

Unless forced by current constraints.

---

### Single Primary Environment per Stage

Each stage (development, staging, production) has:

- one primary environment
- no parallel long-lived variants

Ephemeral environments are allowed only if they are disposable.

---

## Configuration and Secrets

### Explicit Configuration

Configuration is:

- explicit
- documented
- environment-scoped

Implicit defaults and hidden configuration are avoided.

---

### Centralized Secrets Management

Secrets are:

- centrally managed
- rotated deliberately
- never embedded in code

Local development may use simplified mechanisms, but production does not.

---

## Observability

### Logs First

Logging is mandatory.

- Logs are structured where possible.
- Logs are retained long enough to diagnose incidents.

Metrics and tracing are secondary.

---

### Error Visibility

Errors:

- are surfaced early
- fail loudly
- are observable without deep inspection

Silent failure is unacceptable.

---

## Performance

### Adequate Performance Targets

Performance targets are:

- defined
- conservative
- based on real usage

We do not optimize before targets are exceeded.

---

### Vertical Scaling Before Horizontal

Bedrock PHP defaults to:

- vertical scaling first
- horizontal scaling only when necessary

Complex scaling strategies require justification.

---

## Data Management

### One Primary Data Store

Each application has:

- one primary database
- a clear source of truth

Additional data stores are introduced only under clear necessity.

---

### Backups Are Mandatory

Backups:

- are automated
- are tested
- are documented

Untested backups are treated as non-existent.

---

## Security Posture

### Least Privilege by Default

Access is:

- minimal
- role-based
- reviewed periodically

Broad permissions are not acceptable defaults.

---

### Known Tradeoffs

Bedrock PHP accepts:

- slightly lower peak performance
- slower adoption of new features
- reduced architectural flexibility

In exchange for:

- simpler systems
- lower operational risk
- long-term maintainability

---

### Maintenance Hygiene

- Patch updates are applied on a predictable cadence (e.g., weekly) and accelerated for critical CVEs.
- Automated PRs are allowed, but must pass CI and have a simple rollback path.
- Major upgrades are scheduled intentionally and justified (support timelines / concrete constraint).

---

### Closing Statement

These defaults are intentionally conservative.

They exist to:

- make the common case easy
- make the uncommon case explicit
- prevent accidental complexity

Teams are expected to start here — and stay here — unless reality forces them elsewhere.


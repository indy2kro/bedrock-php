# Bedrock PHP

## Profile: AWS

**Status:** Non-Core, Derivative Artifact  
**Profile Type:** Environment  
**Profile Version:** v1.0  
**Compatible Bedrock PHP Version(s):** v1.0  
**Monetization:** Paid Profile

This profile is a **constrained interpretation** of Bedrock PHP for teams operating primarily on AWS. It does not modify the Bedrock PHP standard.

---

## 1. Scope & Assumptions

This profile applies when:

- AWS is the **single primary cloud provider**
- The system is a **single PHP application** deployed as a monolith
- The operating team size is **small to medium (≤20 engineers)**
- The organization prefers **managed services over bespoke infrastructure**

This profile does **not** apply to:

- multi-cloud active-active architectures
- organizations with dedicated platform teams
- event-driven or service-mesh-based systems

If these conditions are not met, this profile must not be used.

---

## 2. Unchanged Bedrock Defaults

The following Bedrock PHP defaults remain unchanged:

- Monolith-first application architecture
- One deployment path
- Composer as the sole dependency mechanism
- Logs-first observability
- Vertical scaling before horizontal scaling
- Explicit configuration and centralized secrets
- Conservative dependency and upgrade posture

---

## 3. Strengthened or Narrowed Rules

Under this profile:

- We limit AWS usage to **a small, fixed set of managed services**.
- We do not introduce a second compute paradigm once one is chosen.
- We do not introduce cross-account complexity unless forced by regulation.
- Infrastructure variation between environments is treated as a defect.

Defaults are intentionally narrower to prevent AWS-driven sprawl.

---

## 4. Explicit Acceptances

Under this profile, we explicitly accept:

- Higher per-unit infrastructure cost in exchange for reduced operational effort
- Vendor lock-in to AWS-managed services
- Slower access to cutting-edge infrastructure features

These tradeoffs are considered acceptable to preserve predictability and operability.

---

## 5. Explicit Rejections

Under this profile, we explicitly reject:

- Kubernetes (EKS). It introduces coordination and failure modes disproportionate to this scale.
- Multi-account application architectures. They increase cognitive load and incident complexity.
- Service meshes and custom networking overlays.
- Mixing container-based and VM-based deployment models.

These rejections are non-negotiable within this profile.

---

## 6. Stop Rules

The following conditions define **hard stops**:

- If application latency and error budgets are met, we do not add caching layers.
- If a single managed database meets capacity targets, we do not shard or replicate manually.
- If deployment time remains under agreed thresholds, we do not introduce parallel deployment paths.

Optimization stops when targets are met.

---

## 7. Applicability Exit Conditions

This profile no longer applies when:

- The organization operates **more than one primary cloud provider**
- The application requires **multiple independent production regions**
- The engineering team exceeds **20 engineers**
- Regulatory requirements mandate strict account or network isolation

Exiting this profile is expected under these conditions and does not represent failure.

---

## 8. Non-Normative Notes (Optional)

**Non-Normative:**

Teams commonly overestimate the need for AWS service breadth early. This profile exists to constrain early decisions so that AWS complexity grows only when forced by reality, not by perceived best practice.

---

## 9. Closing Statement

This profile exists to reduce AWS-specific decisions under constraint.

If following this profile introduces optionality, debate, or service proliferation, the profile has failed its purpose.


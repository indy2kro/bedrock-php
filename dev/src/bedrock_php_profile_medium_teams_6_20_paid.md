# Bedrock PHP

## Profile: Medium Teams (6–20)

**Status:** Non-Core, Derivative Artifact  
**Profile Type:** Team Size / Organizational Scale  
**Profile Version:** v1.0  
**Compatible Bedrock PHP Version(s):** v1.0  
**Monetization:** Paid Profile

This profile is a **constrained interpretation** of Bedrock PHP for organizations operating with a medium-sized engineering team. It does not modify the Bedrock PHP standard.

---

## 1. Scope & Assumptions

This profile applies when:

- The engineering team size is **between 6 and 20 engineers**
- The system is a **single primary PHP application**
- Operational responsibility is shared, but not delegated to a dedicated platform team
- The organization values **predictability over local autonomy**

This profile does **not** apply to:

- teams of 5 or fewer engineers
- organizations with dedicated SRE or platform teams
- product organizations operating multiple independent applications at equal priority

If these conditions are not met, this profile must not be used.

---

## 2. Unchanged Bedrock Defaults

The following Bedrock PHP defaults remain unchanged:

- Monolith-first application architecture
- Single primary deployment path
- One primary data store
- Composer as the only dependency mechanism
- Logs-first observability
- Explicit configuration and centralized secrets
- Conservative dependency and upgrade posture

---

## 3. Strengthened or Narrowed Rules

Under this profile:

- We limit the number of concurrently active architectural initiatives.
- We require defaults to be **documented, not tribal**.
- We do not introduce parallel ways of doing the same thing.
- We do not allow team-level customization of infrastructure or deployment paths.

Consistency is prioritized over local optimization.

---

## 4. Explicit Acceptances

Under this profile, we explicitly accept:

- Slower experimentation in exchange for shared understanding
- Reduced individual autonomy to preserve system coherence
- Occasional friction when introducing change

These tradeoffs are accepted to prevent coordination overhead from becoming systemic risk.

---

## 5. Explicit Rejections

Under this profile, we explicitly reject:

- Multiple deployment paths for different teams or services
- Team-specific infrastructure or runtime variants
- Architecture decisions made to accommodate individual preferences
- Introducing services or abstractions to reduce interpersonal coordination

These patterns scale coordination cost faster than delivery speed.

---

## 6. Stop Rules

The following conditions define **hard stops**:

- If the system can be understood end-to-end by a senior engineer within a reasonable time, we do not split it.
- If deployment and rollback are reliable, we do not add orchestration layers.
- If operational incidents are resolvable without escalation chains, we do not add process frameworks.

Optimization stops when clarity is preserved.

---

## 7. Applicability Exit Conditions

This profile no longer applies when:

- The engineering organization exceeds **20 engineers**
- Multiple applications require equal operational priority
- A dedicated platform or SRE team becomes necessary

Exiting this profile reflects organizational growth, not failure.

---

## 8. Non-Normative Notes (Optional)

**Non-Normative:**

Medium-sized teams often experience pressure to adopt “scaled” practices prematurely. This profile exists to delay that pressure until it is unavoidable, preserving simplicity for as long as possible.

---

## 9. Closing Statement

This profile exists to reduce coordination-driven decisions under growth.

If following this profile introduces parallel systems, optionality, or team-specific divergence, the profile has failed its purpose.

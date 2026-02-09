# Bedrock PHP

## Profile Template

**Status:** Non-Core, Derivative Artifact  
**Audience:** Teams operating under a specific, declared constraint  
**Monetization:** Paid (unless explicitly designated as the single free reference profile)

This template is **normative** for any AI-generated Bedrock PHP Profile.

AI must follow this structure exactly. Sections may not be reordered, merged, or omitted.

---

## 1. Profile Identity

**Profile Name:**  
**Profile Type:** Environment | Team Size | Longevity | Constraint  
**Profile Version:**  
**Compatible Bedrock PHP Version(s):**  

This profile is a **constrained interpretation** of Bedrock PHP. It does not modify the Bedrock PHP standard.

---

## 2. Scope & Assumptions

This section defines **where this profile applies**.

AI must explicitly state:

- the assumed environment or constraint
- what is considered *in scope*
- what is explicitly *out of scope*

Example:

> This profile assumes a single AWS account hosting a PHP application operated by a team of 6–12 engineers. It does not apply to multi-account federated setups or organizations with dedicated platform teams.

If assumptions cannot be stated clearly, the profile must not be generated.

---

## 3. Unchanged Bedrock Defaults

This section lists Bedrock PHP defaults that remain **fully unchanged** under this profile.

Rules:

- Defaults must be referenced, not redefined
- No commentary or justification is allowed here

Example:

- Monolith-first architecture
- Single deployment path
- Logs-first observability

---

## 4. Strengthened or Narrowed Rules

This section documents where Bedrock PHP rules become **stricter or more explicit** under this profile.

Rules:

- Only existing Bedrock PHP rules may be strengthened
- No new concepts may be introduced
- Each rule must be written declaratively

Example:

> Under this profile, we do not introduce more than one managed database service.

---

## 5. Explicit Acceptances

This section lists **explicitly accepted tradeoffs** under this profile.

Rules:

- Acceptances must acknowledge cost, risk, or limitation
- Acceptances must be narrow and concrete

Example:

> We accept higher per-unit infrastructure cost in exchange for reduced operational complexity.

---

## 6. Explicit Rejections

This section lists **explicitly rejected architectures, services, or practices**.

Rules:

- Rejections must be decisive
- Each rejection must include a brief rationale

Example:

> We do not adopt Kubernetes in this profile. It introduces coordination and failure modes disproportionate to the team size.

---

## 7. Stop Rules

This section defines **hard boundaries** that prevent scope creep.

Rules:

- Stop rules must be testable
- Each rule must define a clear stopping condition

Example:

> If request volume doubles without breaching latency targets, we do not change the architecture.

---

## 8. Applicability Exit Conditions

This section defines **when this profile no longer applies**.

Rules:

- Exit conditions must be concrete
- Exits must not be framed as failures

Example:

> This profile no longer applies once the team exceeds 20 engineers or operates more than one production region.

---

## 9. Non-Normative Notes (Optional)

This section may include:

- historical context
- common misinterpretations
- known failure modes

Rules:

- Must be explicitly labeled non-normative
- Must not introduce new rules

---

## 10. Closing Statement

This profile exists to reduce decisions under constraint.

If following this profile introduces debate, optionality, or customization pressure, the profile has failed its purpose.

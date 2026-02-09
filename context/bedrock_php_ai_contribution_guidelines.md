# Bedrock PHP – AI Contribution Guidelines

## 1. Purpose of This Document

This document defines **how AI tools are to be used** in the creation, maintenance, and evolution of **Bedrock PHP**.

Bedrock PHP is not a content project, a tutorial series, or a living blog. It is a **stable, opinionated, production-oriented reference** intended to reduce decision fatigue for small to mid-sized PHP teams running long-lived systems.

AI is used as a **force multiplier**, not an authority.

> **AI may assist with articulation, exploration, and consistency.**  
> **AI may not define standards, introduce novelty, or expand scope autonomously.**

This document exists to prevent the most common failure mode of AI-assisted projects: *accidental bloat, loss of authority, and erosion of intentional limits*.

---

## 2. Non‑Negotiable Principles

All AI-assisted output **must** adhere to the following principles.

### 2.1 Bedrock Is Finite by Design

- Bedrock PHP is released in **versioned editions** (v1.0, v1.1, v2.0, …).
- Each version is **stable and frozen** after release.
- AI must **not** suggest continuous updates, rolling changes, or evergreen expansion.

If an AI proposes:
- “Keeping this up to date”
- “Regular refreshes”
- “Adapting to new trends automatically”

👉 The suggestion must be rejected.

---

### 2.2 Authority Comes from Deliberate Choice

Bedrock PHP exists to **end debates**, not host them.

AI contributions must:
- Prefer **one clear default** over multiple options
- Avoid “it depends” unless explicitly framed as a documented exception
- Avoid listing alternatives unless the purpose is to **reject** them

AI must never present:
- comparison tables of tools
- multiple equally valid approaches
- exploratory surveys

When ambiguity exists, AI should ask for clarification rather than inventing flexibility.

---

### 2.3 Boring Is a Feature, Not a Bug

Bedrock PHP intentionally favors:
- boring technology
- predictable patterns
- conservative defaults
- known failure modes

AI output must avoid:
- novelty bias
- excitement framing
- “modern”, “cutting-edge”, or “next-generation” language

Preferred adjectives:
- stable
- predictable
- sufficient
- proven
- adequate

---

## 3. Scope Discipline

### 3.1 What Bedrock PHP Covers

AI may contribute content **only** within these domains:

- PHP runtime and versioning posture
- Application structure (monolith-first)
- Dependency discipline
- Deployment and CI/CD defaults
- Infrastructure complexity limits
- Configuration and secrets handling
- Observability before optimization
- Performance *cutoffs* and stop rules
- Maintenance, deletion, and end-of-life practices

---

### 3.2 What Bedrock PHP Explicitly Does NOT Cover

AI must not introduce content about:

- Framework comparisons
- Frontend tooling
- Career advice
- Team culture or management theory
- AI-assisted coding practices
- “Best practices” without operational context
- Hyperscale / FAANG-style infrastructure

If asked to generate such content, AI should respond:

> “This is intentionally out of scope for Bedrock PHP.”

---

## 4. Tone and Voice Rules

AI-generated text must follow these tone constraints:

- Calm
- Declarative
- Slightly stubborn
- Non-apologetic
- Non-evangelical

Avoid:
- enthusiasm
- marketing language
- calls to action
- rhetorical hype

### 4.1 Sentence Style

Prefer:
- short, direct sentences
- explicit rules
- clear boundaries

Example:
> “We do not introduce a second service unless this condition is met.”

Avoid:
> “You might consider exploring a service-based approach if your needs grow.”

---

## 5. How AI Should Handle Disagreement

When AI detects conflicting industry opinions:

1. State the Bedrock position clearly
2. Acknowledge alternatives briefly
3. Explain *why Bedrock rejects them*
4. End the discussion

Example pattern:

> “Some teams choose X. Bedrock does not. X introduces Y failure mode at this scale. We accept the tradeoff.”

No extended debate.

---

## 6. Stop Rules (Critical)

Bedrock PHP is defined as much by **where it stops** as by what it includes.

AI must actively look for opportunities to:
- introduce limits
- define thresholds
- say “do nothing”
- recommend deletion

Examples:
- “Below this traffic level, do not optimize further.”
- “If this condition is met, stop.”

If AI proposes additional layers, tools, or abstractions, it must also propose **a stopping condition**.

---

## 7. Versioning and Change Control

AI must respect the following rules:

- No changes are made to a released version
- Clarifications may be written, but only for the *next* version
- All changes must be traceable to:
  - new constraints
  - widespread misuse
  - clear operational failure

AI should not suggest updates based on:
- new tools
- community trends
- popularity shifts

---

## 8. Use of Multiple AI Tools

Different AI tools may be used for:

- drafting prose
- checking internal consistency
- identifying contradictions
- summarizing sections

However:

- **Final decisions remain human**
- AI outputs must be reviewed against this document
- Conflicts between AI outputs must be resolved manually

No AI is allowed to unilaterally merge, refactor, or expand Bedrock PHP.

---

## 9. Anti‑Patterns for AI Contributions

AI must actively avoid:

- expanding scope to be helpful
- softening rules to be inclusive
- adding examples that imply optionality
- introducing “future-proofing” language
- reframing decisions as personal preference

When in doubt, AI should err on the side of **removal**, not addition.

---

## 10. The Core Test

Every AI-assisted contribution must pass this test:

> “Would this reduce the number of decisions a tired tech lead has to make at 3am?”

If the answer is no, the content does not belong in Bedrock PHP.

---

## 11. Final Guiding Statement

Bedrock PHP is not trying to be right forever.

It is trying to be **good enough, stable enough, and clear enough** to let teams stop thinking and start shipping — and then sleep.

AI exists to help articulate that clarity, not to erode it.


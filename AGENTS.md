# AGENTS.md - Agent Guidelines for Bedrock PHP

## Overview

Bedrock PHP is an **operational standard** for building, deploying, and running PHP applications in production. It is a **documentation project** containing markdown files that define rules and guidelines for PHP operations.

This is NOT a typical PHP codebase. It contains no PHP code, no Composer dependencies, no build scripts, and no tests.

---

## Project Structure

```
bedrock-php/
├── README.md                    # Main entry point
├── src/                         # Chapter documents (chapter*.md)
├── context/                     # Supporting documentation
│   ├── bedrock_php_ai_contribution_guidelines.md
│   ├── bedrock_php_structural_guidelines.md
│   ├── bedrock_php_declared_defaults.md
│   └── ... (other context files)
├── tools/                       # AI tool integration values
│   ├── runtime-values.md
│   ├── config-values.md
│   └── ... (domain-specific values)
└── AGENTS.md                    # This file
```

---

## Build / Test / Lint Commands

This project has no build process, no tests, and no linting tools.

### Why?
- Pure markdown documentation
- No executable code
- Content is static text files

### Verification
To verify content is correct:
- Check markdown syntax validity (no special tooling needed)
- Ensure all chapters follow the structural guidelines in `context/bedrock_php_structural_guidelines.md`
- Ensure AI contributions follow `context/bedrock_php_ai_contribution_guidelines.md`

---

## Code Style Guidelines

Since this is a documentation project, "code style" refers to **markdown content style**.

### Writing Principles

1. **Be Boring and Predictable**
   - Use conservative language
   - Avoid novelty, excitement, or "modern" framing
   - Prefer: stable, predictable, sufficient, proven, adequate

2. **Be Declarative**
   - Use direct statements: "We do X." / "We do not do Y."
   - Avoid: "You might consider...", "It depends...", "Perhaps..."
   - Never present multiple equally valid options

3. **Be Calm and Non-Apologetic**
   - Avoid: enthusiasm, marketing language, calls to action
   - Never soften rules to be inclusive
   - Don't hedge or qualify unnecessarily

4. **Follow the "Stop Rules"**
   - Actively look for opportunities to introduce limits
   - Define thresholds and stopping conditions
   - Say "do nothing" when appropriate

### Document Structure

Each chapter MUST follow the layered content model:

```
## Section Title

### Normative Content (Required)
Rules, defaults, prohibitions, limits - the actual standard.
This layer must be complete and actionable on its own.

---

### Non-Normative: Rationale (Optional)
Explain WHY the rule exists.
Label clearly as "Non-Normative".
Must NOT introduce new rules or modify existing ones.

---

### Non-Normative: Implementation (Optional)
One minimal example, checklist, or template.
Label clearly as "Non-Normative".
Present ONE approach only - no alternatives.
```

### Rule Formatting

Rules must be expressed as:
- "We do X."
- "We do not do Y."
- "We stop when Z happens."

Avoid conditional phrasing unless it's a hard cutoff.

### Anti-Patterns to Avoid

- Comparison tables of tools
- Multiple equally valid approaches
- "It depends" without explicit documented exception
- Exploratory surveys or "research"
- Future-proofing language
- Adding examples that imply optionality
- Softening rules or adding caveats

### Tone Checklist

- [ ] Calm
- [ ] Declarative
- [ ] Slightly stubborn
- [ ] Non-apologetic
- [ ] Non-evangelical
- [ ] Short, direct sentences
- [ ] Explicit rules
- [ ] Clear boundaries

---

## Core Values

These values guide decisions when rules are insufficient. They are **decision-making shortcuts**, not aspirational slogans.

### The 10 Operational Values

1. **Stability Over Novelty**
   - Prefer tools with known failure modes
   - Resist upgrades without concrete operational benefit
   - Novelty is treated as a cost

2. **Predictability Over Flexibility**
   - Constrain behavior, surface problems early
   - Limit options even at the cost of adaptability
   - Predictable systems are easier to reason about under pressure

3. **Explicit Limits Over Implicit Growth**
   - Define when to stop, when to do nothing, when not to optimize
   - If a system can grow without a hard boundary, that boundary is missing

4. **Deletion Over Abstraction**
   - First response to complexity: remove, not generalize
   - Abstractions hide complexity and are difficult to remove

5. **Operational Clarity Over Theoretical Correctness**
   - Optimize for clarity during incidents, not theoretical elegance
   - Fail in obvious ways

6. **Defaults That End Discussions**
   - Defaults exist to end discussion, not invite refinement
   - If a default sparks debate, it has failed

7. **Constraints Over Coordination**
   - Encode decisions as constraints rather than processes
   - Constraints survive personnel changes

8. **Known Failure Modes Over Hidden Risk**
   - Prefer systems that fail visibly and predictably
   - Hidden risk is more dangerous than known limitation

9. **Boring by Design**
   - Boring systems are easier to staff and maintain
   - If a design decision feels exciting, it deserves extra scrutiny

10. **Longevity Over Local Optimization**
    - Optimize for systems understandable years later
    - Reject short-term gains that lock in complexity

---

## Implementation Pattern

Each section should follow this pattern:

```
1. Rules (normative, declarative)
2. One minimal example (show what "good" looks like)
3. Stop rule (when not to add more)
```

### What Each Section Should Produce

At least one of:
- A checklist
- A template
- A minimal example
- A default policy statement people can paste into docs

### The "Abstract Usefulness" Rule

Bedrock should be specific enough to implement in a day, general enough to survive 3 years.

### Anti-Patterns to Avoid

- Multiple tools presented as equals ("GitHub Actions vs GitLab vs Jenkins...")
- Long tutorials
- Matrices and comparisons
- "Choose your own adventure"

---

## Adoption Model

When contributing content, remember:

- **Version Pinning**: Teams adopt a specific version (e.g., v1.0). Versions do not change after release.
- **Deviation Policy**: Deviation from Bedrock PHP is allowed but never silent. A deviation must:
  - Be documented
  - Reference the Bedrock PHP rule being deviated from
  - Explain the concrete constraint that necessitated it
  - Not be framed as preference or optimization
- **Partial Adoption**: Discouraged. Bedrock PHP is designed to be adopted as a whole.
- **Defaults Are Normal**: Accept defaults without modification unless a real constraint exists.

---

## Key Reference Documents

Before contributing, read these:

1. **`context/bedrock_php_ai_contribution_guidelines.md`** - How AI should contribute
2. **`context/bedrock_php_structural_guidelines.md`** - Document organization rules
3. **`context/bedrock_php_declared_defaults.md`** - Default choices
4. **`context/bedrock_php_core_values_operational.md`** - Decision-making principles

---

## Versioning

- Bedrock PHP uses explicit, frozen versions (v1.0, v1.1, etc.)
- Each version is **stable and frozen** after release
- No changes to released versions
- Minor versions may only: clarify wording, tighten rules, remove ambiguity

---

## The Core Test

Every contribution must pass this test:

> "Would this reduce the number of decisions a tired tech lead has to make at 3am?"

If the answer is no, the content does not belong in Bedrock PHP.

---

## How to Handle Scope Creep

If asked to generate content outside scope, respond:

> "This is intentionally out of scope for Bedrock PHP."

Bedrock PHP explicitly does NOT cover:
- Framework comparisons
- Frontend tooling
- Career advice
- Team culture or management theory
- AI-assisted coding practices
- "Best practices" without operational context
- Hyperscale / FAANG-style infrastructure

---

## When Adding Content

Follow the "Replace or Reject" rule:
- Any proposed addition must: replace an existing section OR remove ambiguity elsewhere
- If neither is true, the addition must be rejected
- Growth is allowed only when it **removes more than it adds**

Every major version must:
- Remove at least one rule
- Delete at least one section or subsection
- If nothing can be removed, the version should not be released

---

## Final Guiding Statement

Bedrock PHP exists to let teams stop thinking and start shipping - and then sleep.

AI exists to help articulate that clarity, not to erode it.

Be boring. Be decisive. Be stable.

# Bedrock PHP — v1.0

## What This Is

Bedrock PHP is an **operational standard** for building, deploying, and running PHP applications in production.

It is intentionally restrictive.

Its goal is not to define the best possible system, but to define a **safe, boring, repeatable baseline** that:

- reduces decision fatigue
- minimizes accidental complexity
- survives team and context changes
- remains understandable months or years later

If Bedrock PHP feels limiting, that is by design.

---

## What This Is Not

Bedrock PHP does **not** define:

- application architecture patterns
- framework choice
- coding style or formatting rules
- team rituals or development process

It does not attempt to be universal or future-proof.

Bedrock PHP is a tool for a specific phase and set of constraints.

---

## How to Use This Repository

This repository is organized as a set of standalone chapters.

Each chapter contains:
- **Normative sections** (binding rules)
- **Non-normative sections** (context, examples, failure modes)

Normative rules are the contract.
Non-normative text exists to help you apply them correctly.

If there is a conflict, the normative rules win.

---

## For AI Contributors

If you are an AI agent contributing to Bedrock PHP, read `AGENTS.md` first.

---

## Adoption Rules (Read This First)

A project using Bedrock PHP must:

- explicitly adopt a specific version (e.g. v1.0)
- adopt it at the project level, not selectively
- document any deviations centrally

Partial adoption is worse than non-adoption.

If you cannot follow a rule, that is a signal — not a failure.

---

## Recommended Reading Order

If you are new to Bedrock PHP:

1. **Chapter 1 — Purpose & Scope**
2. **Chapter 2 — Adoption Model**
3. **Chapter 3 — Core Values (Operational)**
4. **Chapter 4 — Declared Defaults**

Then read the remaining chapters as needed.

---

## What Compliance Means

A project claiming compliance with Bedrock PHP v1.0:

- follows all normative rules in v1.0
- treats declared defaults as binding
- has documented deviations (if any)
- is willing to exit the standard if fit degrades

Compliance is binary, not aspirational.

---

## When Not to Use Bedrock PHP

Do not adopt Bedrock PHP if:

- infrastructure experimentation is a core goal
- the system is short-lived or exploratory
- regulatory or organizational constraints conflict with the rules
- multiple independent teams must ship autonomously from day one

In these cases, choose a different standard deliberately.

---

## Exiting Bedrock PHP

Exiting is expected for some systems.

When you exit:
- record the exit
- state the reasons
- stop claiming compliance

Standards retain value only when they are followed honestly.

---

## Versioning

This repository uses explicit, frozen versions.

- v1.0 is immutable
- changes require a new release
- major versions remove constraints as well as add them

Always reference the version you are using.

---

## Status

**Current version:** Bedrock PHP v1.0

This document is the entry point and orientation guide.

For rules, always defer to the chapter documents.

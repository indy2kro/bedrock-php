# Bedrock PHP

## Purpose & Scope

### Purpose

Bedrock PHP exists to provide a **stable, opinionated production baseline** for teams running PHP systems that are expected to live for years.

It is designed to reduce decision fatigue, prevent unnecessary complexity, and give teams a defensible default they can rely on without constant re-evaluation.

Bedrock PHP is not about doing things the *best* way.
It is about doing them a **sufficient, predictable, and repeatable way** — and then stopping.

The intended outcome of adopting Bedrock PHP is simple:

- fewer architectural debates
- fewer premature optimizations
- fewer irreversible decisions made too early
- fewer systems that need heroics to operate

If Bedrock PHP is doing its job, teams spend less time discussing infrastructure and more time shipping and maintaining software.

---

### The Problem Bedrock PHP Addresses

Most PHP teams do not fail because of poor technical skill.
They fail because:

- every decision is treated as unique
- every new tool feels justified
- nothing clearly signals when to stop
- defaults are re-litigated repeatedly

The modern ecosystem offers *too many viable options* and *too little permission to choose one and move on*.

Bedrock PHP exists to create that permission.

It does so by declaring explicit defaults, limits, and prohibitions — and accepting their tradeoffs openly.

---

### What Bedrock PHP Is

Bedrock PHP is:

- a **production-first reference**, not a tutorial
- a **normative baseline**, not a menu of choices
- a **versioned document**, not a living feed
- a **decision-ending artifact**, not a discussion starter

It assumes:

- PHP is a valid, long-lived platform
- most systems do not need exotic architecture
- operational simplicity is a competitive advantage
- stability is more valuable than novelty

---

### What Bedrock PHP Is Not

Bedrock PHP is explicitly **not**:

- a framework comparison
- a list of best practices
- a catalog of tools
- a guide to modern trends
- a hyperscale architecture reference
- a replacement for engineering judgment

It does not attempt to:

- optimize for peak performance
- showcase clever techniques
- remain continuously up to date
- accommodate every team or use case

If a topic requires frequent revision to stay relevant, it does not belong in Bedrock PHP.

---

### Scope

Bedrock PHP covers only the parts of a system that:

- repeatedly cause unnecessary debate
- tend to accumulate irreversible complexity
- materially affect long-term operability

The scope of Bedrock PHP includes:

- PHP runtime posture and upgrade strategy
- application structure defaults
- dependency discipline
- deployment and CI/CD expectations
- infrastructure complexity limits
- configuration and secrets handling
- observability before optimization
- performance cutoffs and stop rules
- maintenance, deletion, and end-of-life practices

Everything else is intentionally out of scope.

---

### Target Audience

Bedrock PHP is written for:

- tech leads responsible for systems in production
- engineering managers overseeing small to mid-sized teams
- founders and CTOs running long-lived PHP products
- senior engineers acting as technical stewards

It assumes the reader:

- has operational responsibility
- has experienced the cost of overengineering
- values predictability over novelty
- wants fewer decisions, not more options

It is not written for beginners, hobby projects, or experimentation-driven teams.

---

### Adoption Philosophy

Bedrock PHP is designed to be adopted **as a whole**.

Teams are expected to:

- treat its defaults as the starting point
- document deviations explicitly
- revisit deviations only when constraints change

Adoption does not imply perfection.
It implies **intentional alignment**.

---

### Longevity Statement

Bedrock PHP is written with the assumption that:

- most systems will outlive their original authors
- team composition will change
- context will be lost over time

Its purpose is to leave behind a clear, durable set of decisions that remain understandable long after the original reasoning has faded.

Bedrock PHP favors decisions that age well over decisions that age impressively.

---

### Closing Statement

Bedrock PHP does not promise optimal systems.

It promises systems that are:

- understandable
- operable
- difficult to accidentally ruin

Its primary goal is not to help teams move faster.
It is to help them **stop moving unnecessarily**.


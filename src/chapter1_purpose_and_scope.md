# Bedrock PHP — v1.0

## 1. Purpose & Scope

### Normative

#### Purpose
Bedrock PHP defines a **deliberately constrained way** to build, deploy, and operate PHP applications in production. Its purpose is not to maximize flexibility, expressiveness, or novelty. Its purpose is to:

- Reduce decision fatigue
- Minimize accidental complexity
- Produce systems that are understandable months later
- Enable small teams to operate production systems safely

Bedrock PHP exists to answer one question consistently:

> “What is the simplest thing that can reasonably work here?”

#### Scope
Bedrock PHP applies to:

- PHP applications that serve real users
- Systems expected to live longer than a prototype
- Teams that want **boring reliability** over architectural exploration

Bedrock PHP explicitly covers:

- deployment and infrastructure expectations
- configuration and state handling
- observability and operations
- security posture
- maintenance and end-of-life

Bedrock PHP explicitly does **not** attempt to define:

- application architecture (MVC, hexagonal, DDD, etc.)
- framework choice
- coding style or formatting rules
- team process, rituals, or org structure

Those choices are intentionally left outside the boundary.

#### Constraints
By adopting Bedrock PHP, a team agrees to:

- accept fewer options than are technically available
- prefer clarity over cleverness
- remove systems instead of extending them by default

These constraints are a feature, not a limitation.

#### Prohibitions
- Bedrock PHP must not be selectively adopted while ignoring its defaults.
- Bedrock PHP must not be used as a branding label without operational compliance.
- Bedrock PHP must not be treated as a “best practices grab bag.”

#### Stop rule
If the team finds itself repeatedly asking:

- “Can we bend this just a little?”
- “What if we add one more exception?”

Then stop and reassess adoption. Bedrock PHP is only useful when followed consistently.

---

### Non-Normative

#### Why this document exists
Most production complexity does not come from business logic. It comes from:

- unexamined defaults
- ad-hoc infrastructure decisions
- systems accreting behavior without ownership

Bedrock PHP exists to *front-load* those decisions so they are made once, deliberately, and then mostly forgotten.

This is not a philosophy document. It is an **operational contract**.

#### What Bedrock PHP is good at
Bedrock PHP shines when:

- the team is small (1–10 engineers)
- the product is evolving but not experimental infrastructure-wise
- uptime matters more than novelty
- the cost of mistakes is higher than the cost of saying “no” to complexity

Common examples:

- SaaS backends
- internal tools that accidentally became critical
- long-lived APIs
- revenue-adjacent systems

#### What Bedrock PHP is bad at
Bedrock PHP will feel painful if:

- you want to explore infrastructure as a learning goal
- the system is a research prototype
- you need per-team autonomy across many independent services
- you are required to meet heavy regulatory frameworks that mandate specific tooling

In these cases, the friction is a signal, not a bug.

#### Things to look out for
Teams often violate the *spirit* of Bedrock PHP before they violate its rules. Watch for:

- adding tools “just in case we need them later”
- parallel deployment paths creeping in
- configuration becoming implicit or tribal knowledge
- operational work being deferred because “it works for now”

These are early warning signs of drift.

#### Practical adoption advice
- Adopt Bedrock PHP **at project start** or at a clear inflection point (rewrite, ownership transfer, stability phase).
- Write down where you knowingly diverge.
- Revisit those divergences quarterly.

If the list grows, it may be time to exit.

---

**Status:** Draft — Chapter 1

## Should Bedrock include examples or implementation options?

**Yes — but only in a Bedrock way.** Otherwise it becomes abstract and useless _or_ it becomes a tool catalog.

### The Bedrock pattern: “Rules → Minimal reference example → Stop rule”

Each subsection should have:

1.  **Rules** (normative, declarative)
2.  **One minimal example** (show what “good” looks like)
3.  **Stop rule** (when not to add more)

That keeps it concrete without turning it into a menu.

### What Bedrock should NOT do

-   multiple tools presented as equals (“GitHub Actions vs GitLab vs Jenkins…”)
-   long tutorials
-   matrices and comparisons
-   “choose your own adventure”

### Implementation Notes (Non-Normative)

In each section, allow a small, boxed pattern:

- One example snippet/template
- One “common acceptable tooling” sentence max (optional)
- A reminder that tooling choice is secondary

### The “abstract usefulness” rule of thumb

Bedrock should be specific enough to implement in a day, and general enough to survive 3 years.

If a section can’t produce at least one of these, it’s too abstract:
- a checklist
- a template
- a minimal example
- a default policy statement people can paste into docs
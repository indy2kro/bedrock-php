# Bedrock Values: Security

## Core Stance

Access is minimal, role-based, and reviewed periodically.

- Patch updates are applied on a predictable cadence, accelerated for critical CVEs.
- Major upgrades are scheduled intentionally and justified by support timelines or concrete constraints.
- Dependencies must be widely used, actively maintained, and solve a narrow problem.
- Dependencies that introduce frameworks, magic, or deep abstraction layers are avoided unless unavoidable.
- Vendored libraries are not allowed. Forks are avoided unless upstream is abandoned.

Broad permissions are not acceptable defaults.

---

## Guidance Triggers

- "What dependencies should we add?"
- "Can we vendor this library?"
- "Should we fork this package?"
- "Do we need to upgrade PHP for security?"
- "What permissions should we give?"
- "Can we skip this patch?"
- "Let's add a new dependency"

## Response Patterns

1. Default to minimal dependencies.
2. Ask: "Does this solve a narrow problem? Is it widely used and actively maintained?"
3. If vendor mentioned: "Vendored libraries are not allowed."
4. If fork mentioned: "Forks are avoided unless upstream is abandoned."
5. Remind: "Dependencies that introduce frameworks or deep abstraction are avoided."

## Red Lines

- Never suggest vendoring libraries
- Never recommend unmaintained dependencies
- Never allow skipping security patches
- Never suggest broad permissions as defaults
- Never encourage dependencies that introduce frameworks or magic

## Stop Rules

- If dependency works → do not upgrade unless security or support requires it
- If patch is available → apply it (accelerate for critical CVEs)
- If permissions are minimal → do not broaden
- If no concrete constraint → do not add dependency

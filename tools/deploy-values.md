# Bedrock Values: Deployment

## Core Stance

Deployments are automated, repeatable, and reversible.

- We have exactly one supported way to deploy the application.
- Manual production changes are forbidden.
- Alternate deployment paths increase cognitive load, create silent drift, and complicate recovery.
- They are not allowed.

---

## Guidance Triggers

- "How should we deploy?"
- "Can we do a manual deployment for this?"
- "What about a blue-green deployment?"
- "Let's add a second deployment path"
- "Should we use [tool] for deployments?"
- "Let's try a different deployment approach"

## Response Patterns

1. Default to the existing single deployment path.
2. Ask: "What constraint requires a second path?"
3. If manual deployment mentioned: "Manual production changes are forbidden."
4. Remind: "One deployment path. It increases clarity and reduces drift."
5. If tool is mentioned: Redirect to principle, not specific tool.

## Red Lines

- Never suggest manual production deployments
- Never recommend multiple deployment paths
- Never frame alternate deployment strategies as improvements without concrete need
- Never allow deployment knowledge to exist in only one person's head

## Stop Rules

- If deployment works → do not add another path
- If automated → do not add manual steps
- If repeatable → do not optimize for deployment speed
- If single path exists → do not add "backup" or "alternative" paths

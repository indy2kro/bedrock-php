# Bedrock Values: Configuration

## Core Stance

Configuration is explicit, documented, and environment-scoped.

- We use environment variables for configuration.
- We manage secrets centrally, never embedded in code.
- Configuration drift is treated as a defect.
- We minimize environment-specific overrides.
- Local development may use simplified mechanisms, but production does not.

Implicit defaults and hidden configuration are avoided.

---

## Guidance Triggers

- "Where should we store config?"
- "How do we handle secrets?"
- "Can we hardcode this value?"
- "Should we use a config file?"
- "Let's use environment variables vs config files"
- "What's our config for different environments?"

## Response Patterns

1. Default to environment variables for configuration.
2. Ask: "Is this a secret? If yes, use centralized secrets management."
3. For config changes: "Document it. Make it explicit."
4. Remind: "Configuration drift is a defect."
5. If multiple environments: "One primary environment per stage. No long-lived variants."

## Red Lines

- Never suggest embedding secrets in code
- Never recommend hidden or implicit configuration
- Never allow configuration drift to go unchecked
- Never suggest different config mechanisms per environment without justification

## Stop Rules

- If config is documented → do not add more
- If secrets are centralized → do not change mechanism
- If configuration works → do not add abstraction layer
- If environment is stable → do not add environment-specific overrides

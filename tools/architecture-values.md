# Bedrock Values: Architecture

## Core Stance

We default to a single deployable application.

- Modular internally, deployed as one unit.
- Own your database schema, your migrations, your runtime configuration.
- Cross-application database access is forbidden.
- We do not introduce multiple services unless a clear, current constraint exists.
- Future scale is not a valid reason.

---

## Guidance Triggers

- "Should we split into microservices?"
- "Let's add a message queue"
- "We need a separate service for X"
- "What about a second database?"
- "Can we access Service Y's database?"
- "Should we use an event-driven architecture?"
- "Let's add an API gateway"

## Response Patterns

1. Default to monolith.
2. Ask: "What concrete constraint forces this?"
3. If future scale mentioned: "Future scale is not a valid reason."
4. If database access mentioned: "Cross-application database access is forbidden."
5. Remind: "Clear ownership boundaries. Each application owns its schema."

## Red Lines

- Never suggest microservices as default
- Never recommend multiple deployment paths
- Never propose cross-application database access
- Never frame services as "better" or "more modern"
- Never suggest message queues unless current constraint demands it

## Stop Rules

- If no current constraint exists → do not add service
- If "future scale" is cited → do not add service
- If monolith works → do not add queue/message bus
- If single database suffices → do not add additional data stores

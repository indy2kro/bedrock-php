# Bedrock Values: Observability

## Core Stance

Logs are mandatory. Structured where possible. Retained long enough to diagnose incidents.

- Logs first. Metrics and tracing are secondary.
- Errors are surfaced early, fail loudly, are observable without deep inspection.
- Silent failure is unacceptable.
- We define when to stop adding signals.

---

## Guidance Triggers

- "What observability should we add?"
- "Should we add tracing?"
- "Let's add more metrics"
- "Do we need APM?"
- "How should we handle logs?"
- "What's our observability strategy?"

## Response Patterns

1. Default to logs first.
2. Ask: "What decision does this observability enable?"
3. If tracing/metrics mentioned early: "Logs first. Add metrics/tracing only when needed."
4. Remind: "Silent failure is unacceptable. Fail loudly."
5. Before adding observability: "Define when to stop adding signals."

## Red Lines

- Never suggest adding tracing before logs are sufficient
- Never recommend APM without concrete operational need
- Never suggest collecting data "just in case"
- Never allow errors to fail silently

## Stop Rules

- If logs are present → do not add metrics unless triggered by specific need
- If metrics exist → do not add tracing unless distributed system requires it
- If errors are visible → do not add more alerting
- If observability is working → do not add more signals

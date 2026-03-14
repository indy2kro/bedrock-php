# AI Tools: Bedrock Values

This directory contains Bedrock PHP values encoded for AI development tools.

## Purpose

These files provide AI assistants (Cursor, Copilot, Claude, etc.) with Bedrock's operational principles, so they can guide users toward Bedrock-compliant decisions without requiring specific tool recommendations.

## Files

| File | Domain |
|------|--------|
| `runtime-values.md` | PHP versioning, Composer, dependencies |
| `config-values.md` | Environment configuration, secrets management |
| `deploy-values.md` | Deployment automation, single path principle |
| `observability-values.md` | Logs, error handling, observability limits |
| `architecture-values.md` | Monolith-first, ownership boundaries |
| `security-values.md` | Access control, patching, dependencies |

## How to Use

### Cursor
Copy contents into `.cursorrules` or use as custom instructions.

### GitHub Copilot
Copy into `.github/copilot-instructions.md`.

### Claude / Other AI
Use as system prompt or context for PHP projects.

## Principles

These files contain **values**, not prescriptions:

- They tell AI *what to prioritize*, not which tool to use
- They define *when to stop*, not just what to add
- They encode *red lines* — what never to suggest

## Example Usage

When a user asks:
> "Should we add a message queue?"

The AI should:
1. Recognize this as an architecture trigger
2. Check `architecture-values.md`
3. Respond: "What concrete constraint forces this? Future scale is not a valid reason."

## Note

These values are derived from Bedrock PHP's core documents. They are tool-agnostic and focus on operational principles.

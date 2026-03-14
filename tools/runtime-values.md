# Bedrock Values: Runtime

## Core Stance

We run supported, non-experimental PHP releases.

- We do not run development or preview versions.
- We do not skip major versions deliberately.
- Security and patch updates are applied promptly.
- Major version upgrades are driven by support timelines, not novelty.
- Minor version upgrades are batched and scheduled to avoid continuous churn.

Stability and predictability outweigh early adoption.

---

## Guidance Triggers

- "Should we use the latest PHP version?"
- "What PHP version should we be on?"
- "Can we try the RC/beta version?"
- "Let's skip to PHP 9.x"
- "We need to always be on the latest minor version"
- "Should we use a non-standard PHP distribution?"

## Response Patterns

1. Default to supported PHP versions only.
2. Ask: "Is there a concrete constraint requiring this version?"
3. If "latest" or "newest" is mentioned: redirect to supported versions.
4. Remind: "Stability and predictability outweigh early adoption."
5. For minor upgrades: "Batch and schedule to avoid continuous churn."

## Red Lines

- Never suggest development or preview PHP versions
- Never recommend skipping major versions
- Never frame unsupported PHP versions as acceptable
- Never encourage "always latest" minor version policy

## Stop Rules

- If PHP version is supported → do not change
- If no security issue → do not upgrade major version for novelty
- If working → do not change PHP distribution

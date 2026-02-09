# Bedrock PHP — v1.0

## 7. Observability

### Normative

### Principle
Observability exists to answer real operational questions under pressure, not to collect data for its own sake.

---

### Rule 1: Logging Is Mandatory and Actionable

#### Rule
All production systems must emit logs that are usable during incidents.

#### Implications
- Logs are centralized and searchable.
- Logs include enough context to understand failures.
- Log formats are consistent within the system.

#### Prohibitions
- No relying on local instance logs only.
- No logs that require source-code archeology to interpret.

#### Stop rule
If logs cannot explain an incident after the fact, stop and improve logging.

---

### Rule 2: Errors Are Visible and Counted

#### Rule
Unhandled errors and failures are surfaced automatically.

#### Implications
- Exceptions are captured with stack traces.
- Error rates are visible over time.
- Alerts exist for sustained or severe failures.

#### Prohibitions
- No swallowing exceptions silently.
- No relying on user reports as the primary error signal.

#### Stop rule
If users report errors before monitoring does, stop and fix visibility.

---

### Rule 3: Minimum Viable Metrics

#### Rule
The system exposes a small, intentional set of metrics tied to user impact.

#### Implications
- Metrics answer: is it slow, is it broken, is it getting worse?
- Metrics are stable over time.
- Dashboards are simple and reviewed occasionally.

#### Prohibitions
- No metric explosion.
- No dashboards without owners.

#### Stop rule
If metrics are not consulted during incidents, remove or replace them.

---

### Rule 4: Correlation Beats Volume

#### Rule
It must be possible to correlate related events across logs and errors.

#### Implications
- Request or correlation IDs exist where applicable.
- Logs reference error identifiers.
- Background jobs are traceable to triggering events when relevant.

#### Prohibitions
- No uncorrelated noise logs.
- No tracing systems that are not understood by the team.

#### Stop rule
If correlation cannot be explained to a new team member, simplify it.

---

### Rule 5: Retention Matches Reality

#### Rule
Observability data is retained long enough to investigate real incidents.

#### Implications
- Retention policies are explicit.
- Storage costs are understood and accepted.

#### Prohibitions
- No default retention without review.
- No discarding data before it can reasonably be used.

#### Stop rule
If data is routinely unavailable during investigations, increase retention.

---

### Non-Normative

#### Observability is not surveillance
Collecting everything:

- increases cost
- increases noise
- slows down understanding

Good observability focuses on **questions**, not exhaust.

---

#### Logs are the first responder
In most PHP systems:

- logs are the fastest signal
- metrics lag
- traces are optional

Well-structured logs often solve incidents without anything else.

Log entries that help under pressure usually include:
- timestamp
- request or job identifier
- error class and message
- user or account identifier (when appropriate)

---

#### Error visibility changes behavior
When errors are visible:

- teams fix them earlier
- failures feel real
- quality improves naturally

When errors are hidden:

- workarounds accumulate
- incidents repeat
- trust erodes

Visibility is a cultural lever.

---

#### Metrics should map to user pain
Useful metrics often include:

- request latency percentiles
- HTTP 5xx rates
- job failure counts

Metrics that look impressive but answer no question should be removed.

---

#### Correlation reduces guesswork
Without correlation:

- incidents become pattern-matching exercises
- teams argue about causes

Correlation does not require full distributed tracing.

Often, a simple request ID propagated through logs is enough.

---

#### Retention is a design decision
Too little retention:
- hides slow-moving failures
- prevents learning from incidents

Too much retention:
- increases cost
- encourages hoarding

Choose retention based on how long problems realistically surface.

---

#### Things to watch for
Observability drift often appears as:

- dashboards no one checks
- alerts everyone ignores
- logs no one trusts

These indicate observability theater, not observability.

---

#### Practical use cases

**Healthy observability looks like:**
- incidents start with logs, not guesswork
- alerts point to real problems
- metrics guide prioritization

**Unhealthy observability looks like:**
- silent failures discovered late
- massive dashboards during outages
- debates about what data means

---

**Status:** Draft — Chapter 7

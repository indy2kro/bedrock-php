# Bedrock PHP — VERSION_PLACEHOLDER

## 8. Performance & Scaling Limits

### Normative

### Principle
Performance work exists to meet defined targets, not to satisfy discomfort or speculation.

---

### Rule 1: Targets Before Optimization

#### Rule
Performance targets must be defined before performance work begins.

#### Implications
- Targets are measurable and time-bound.
- Targets reflect user impact, not internal preference.
- Targets are few.

#### Prohibitions
- No optimizing “because it feels slow.”
- No tuning without baseline measurements.

#### Stop rule
If targets are being met in production, stop optimizing.

---

### Rule 2: Measure in Production or Production-Like Conditions

#### Rule
Performance decisions are based on production data or realistic load tests.

#### Implications
- Local benchmarks are advisory only.
- Synthetic tests reflect real usage patterns.

#### Prohibitions
- No extrapolating from empty databases or idealized inputs.
- No assuming linear scaling.

#### Stop rule
If measurements do not reflect reality, stop and redesign measurement.

---

### Rule 3: Vertical Before Horizontal

#### Rule
Scale vertically before introducing horizontal scaling complexity.

#### Implications
- Increase instance size first.
- Simplify architecture before distributing it.
- Delay coordination costs.

#### Prohibitions
- No sharding, queues, or distributed caches without necessity.
- No premature load balancers.

#### Stop rule
If vertical scaling still meets targets, stop.

---

### Rule 4: Caching Is a Liability Until Proven Otherwise

#### Rule
Introduce caching only when a measured bottleneck exists and invalidation is understood.

#### Implications
- Cache scope is explicit.
- Cache lifetime is deliberate.
- Cache failure modes are known.

#### Prohibitions
- No caching “just in case.”
- No caches without clear invalidation strategies.

#### Stop rule
If caching does not materially improve target metrics, remove it.

---

### Rule 5: Scaling Decisions Are Reversible

#### Rule
Scaling mechanisms must be removable without rewriting the system.

#### Implications
- Scaling is additive, not foundational.
- Core logic does not depend on scale artifacts.

#### Prohibitions
- No coupling correctness to scale.
- No irreversible architectural commitments.

#### Stop rule
If a scaling change cannot be rolled back, reconsider it.

---

### Non-Normative

#### Why premature optimization hurts
Premature optimization:

- hides real bottlenecks
- increases maintenance cost
- creates fragile complexity

Many performance issues disappear with:
- better queries
- faster disks
- more memory

Before changing architecture, exhaust boring fixes.

---

#### Production latency is what users feel
Users experience:
- tail latency
- timeouts
- errors

Average performance often hides pain.

Focus on:
- p95 / p99 latency
- error rates under load

These metrics drive meaningful improvement.

---

#### Vertical scaling buys time
Vertical scaling:

- is fast to implement
- is easy to reason about
- delays distributed systems problems

Buying time is a valid strategy.

Use it to:
- learn real usage
- simplify code
- prepare deliberate changes

---

#### Caches fail in interesting ways
Caching introduces:

- stale data
- cache stampedes
- coherence problems

In PHP systems, common cache pitfalls include:
- assuming cache consistency
- overloading shared caches
- caching too close to business logic

Treat caches as optimization layers, not sources of truth.

---

#### Reversibility protects you
Irreversible scaling decisions:

- lock teams into complexity
- make future changes expensive
- turn temporary needs into permanent burden

Design scaling paths you can abandon.

---

#### Things to watch for
Performance drift often shows up as:

- architecture discussions without metrics
- caching proposals before measurements
- fear-driven scaling decisions

These are signals to slow down.

---

#### Practical use cases

**Healthy performance work looks like:**
- targets agreed before changes
- metrics guiding decisions
- improvements validated in production

**Unhealthy performance work looks like:**
- benchmarks without context
- complex diagrams for simple systems
- optimizations no one can explain later

---

**Status:** Draft — Chapter 8

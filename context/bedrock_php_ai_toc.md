## **Bedrock PHP — v1.0 Table of Contents**
### 1. Purpose & Scope
_(done)_
### 2. Adoption Model
_(done)_
### 3. Core Values (Operational)
_(done)_
### 4. Declared Defaults
_(done)_
----------
### 5. Deployment & Infrastructure
Focus:
-   how code reaches production
-   what infra is acceptable
-   what is explicitly rejected
Includes:
-   single deployment path
-   managed services preference
-   environment boundaries
-   no bespoke orchestration
----------
### 6. Configuration & State
Focus:
-   where state lives
-   how config is handled
-   what is forbidden
Includes:
-   env config rules
-   secrets handling
-   immutability expectations
-   state ownership
----------
### 7. Observability
Focus:
-   what you must see
-   what you don’t need yet
-   when to stop adding signals
Includes:
-   logs-first doctrine
-   error visibility
-   retention minimums
-   when _not_ to add tracing
----------
### 8. Performance & Scaling Limits
Focus:
-   when to optimize
-   when not to scale
-   how far vertical scaling goes
Includes:
-   explicit performance targets
-   hard “do nothing” thresholds
-   rejection of speculative scaling
----------
### 9. Security Posture
Focus:
-   baseline hygiene
-   patching rules
-   access discipline
Includes:
-   patch vs major upgrade distinction
-   dependency update cadence
-   least privilege defaults
-   known accepted risks
----------
### 10. Maintenance & Decommissioning
Focus:
-   what happens after launch
-   how systems age
-   how things are removed
Includes:
-   deletion as default
-   archive rules
-   EOL signals
-   ownership decay handling
----------
### 11. When to Leave Bedrock PHP
Focus:
-   honest exit criteria
-   no sunk-cost trap
Includes:
-   scale thresholds
-   organizational mismatch
-   compliance-driven exits
----------
### 12. Version Policy
Focus:
-   how change happens
-   how it doesn’t
Includes:
-   major vs minor versions
-   removal guarantees
-   compatibility promises
# EstateOS Compliance and Assurance Mapping

## 1. Control model

EstateOS applies four assurance layers across all frontend and backend workflows:

1. **Preventive controls** – identity, network isolation, secure SDLC, policy gates, and release constraints.
2. **Detective controls** – monitoring, anomaly detection, SIEM correlation, data quality alerts, and drift analysis.
3. **Corrective controls** – incident response, service rollback, human override, failover, and compensating controls.
4. **Evidence controls** – immutable audit packets, approvals, control attestations, and model/policy lineage.

## 2. Standards alignment

| Framework / Standard | EstateOS architecture response | Primary evidence |
| --- | --- | --- |
| ISO/IEC 27001 | ISMS, asset inventory, risk treatment, secure development, access reviews, incident management, supplier governance. | Risk register, policies, change records, access reviews, control tests. |
| ISO/IEC 27017 | Azure-specific cloud controls for tenancy, segmentation, logging, admin isolation, and customer/provider shared responsibility clarity. | Landing zone baseline, network policies, CSPM reports, privileged access records. |
| ISO/IEC 25010 | Quality requirements for usability, reliability, maintainability, security, performance efficiency, and functional suitability across the platform. | Architecture decision records, NFR scorecards, quality gates, test evidence. |
| ISO 22301 | Business continuity planning for critical APIs, asynchronous workflows, failover, backup, and manual continuity procedures. | BIA outputs, DR runbooks, failover tests, tabletop exercise records. |
| ISO 31000 | Risk governance for product, operational, cyber, model, legal, and market risks, with treatment plans and KRIs. | Risk taxonomy, treatment records, KRI dashboards, governance minutes. |

## 3. Control mapping by platform layer

| Platform layer | Key controls | Relevant standards |
| --- | --- | --- |
| Frontend/BFF | Strong authentication, consent capture, secure sessions, usability validation, accessibility, action logging. | ISO/IEC 27001, ISO/IEC 25010 |
| Router/orchestration | Intent traceability, deterministic routing policy, confidence thresholds, release gating, explanation generation. | ISO/IEC 25010, ISO 31000 |
| Expert microservices | Versioned models, scoped permissions, service isolation, evaluation metrics, contract tests. | ISO/IEC 27017, ISO/IEC 25010 |
| Event backbone | Durable delivery, retry logic, idempotency, dead-letter handling, event traceability. | ISO 22301, ISO/IEC 25010 |
| Data/evidence stores | Encryption, retention, lineage, immutable evidence, backup and recovery. | ISO/IEC 27001, ISO 22301 |
| Security operations | SIEM, posture management, vulnerability response, incident coordination. | ISO/IEC 27001, ISO/IEC 27017, ISO 31000 |

## 4. Workflow-specific controls

### 4.1 Property valuation and investment analysis
- Verify market data provenance and freshness before model use.
- Preserve comparable-set rationale and scenario assumptions in the decision packet.
- Require model risk evidence for release of pricing or ROI-driven recommendations.

### 4.2 Residency eligibility
- Version jurisdiction content and legal rules.
- Require human review for edge cases, adverse jurisdictions, or unclear source-of-funds.
- Bind recommendations to legal/evidence references and user profile completeness.

### 4.3 Insurance matching
- Enforce carrier licensing and servicing constraints.
- Retain peril and property exposure evidence with purpose limitation.
- Capture quote assumptions, exclusions, and underwriting blockers.

### 4.4 Financial risk and compliance
- Apply affordability, suitability, KYC/AML, and sanctions checks before release.
- Escalate low-confidence or high-risk cases to manual review.
- Preserve adverse or blocked outcome reasoning for downstream audit.

## 5. Audit evidence package for a single recommendation

A complete recommendation should preserve:
1. Request, correlation, and actor metadata.
2. Consent and purpose-binding state.
3. Data sources, freshness, and lineage references.
4. Experts selected, scores, and model versions.
5. Policy gates evaluated and their outcomes.
6. Final recommendation, explanation, and confidence/uncertainty.
7. Human approvals, overrides, and rationale.
8. Retention, continuity, and deletion metadata.

## 6. Operating assurance practices

- **Monthly operational review:** latency, drift, blocked-release trends, and resilience observations.
- **Quarterly assurance review:** control effectiveness, access governance, and evidence completeness.
- **Annual management review:** risk posture, standard alignment, continuity readiness, and improvement plan updates.

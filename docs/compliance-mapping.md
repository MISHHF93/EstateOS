# EstateOS Compliance and Assurance Mapping

## 1. Control model

EstateOS applies four assurance layers across all frontend and backend workflows:

1. **Preventive controls** – identity, MFA, RBAC, network isolation, secure SDLC, policy gates, and release constraints.
2. **Detective controls** – monitoring, anomaly detection, SIEM correlation, data quality alerts, screening alerts, and drift analysis.
3. **Corrective controls** – incident response, service rollback, human override, failover, and compensating controls.
4. **Evidence controls** – immutable audit packets, approvals, control attestations, model/policy lineage, and privacy processing records.

## 2. Standards alignment

| Framework / Standard | EstateOS architecture response | Primary evidence |
| --- | --- | --- |
| ISO/IEC 27001 | ISMS, asset inventory, risk treatment, secure development, access reviews, incident management, supplier governance. | Risk register, policies, change records, access reviews, control tests. |
| ISO/IEC 27017 | Azure-specific cloud controls for tenancy, segmentation, logging, admin isolation, and customer/provider shared responsibility clarity. | Landing zone baseline, network policies, CSPM reports, privileged access records. |
| ISO/IEC 27701 | Privacy information management for consent, purpose limitation, data subject rights, retention, deletion, and controller/processor accountability. | Consent receipts, RoPA, retention matrix, deletion logs, privacy impact assessments. |
| SOC 2 Type 2 | Evidence-backed control operation for security, availability, confidentiality, processing integrity, and privacy over time. | Control test results, ticket evidence, access logs, monitoring records, exception approvals. |
| ISO/IEC 25010 | Quality requirements for usability, reliability, maintainability, security, performance efficiency, and functional suitability across the platform. | Architecture decision records, NFR scorecards, quality gates, test evidence. |
| ISO/IEC 5259 | Data quality controls for market feeds, comparable sets, ranking features, freshness, provenance, and remediation. | Data quality scorecards, source lineage, freshness monitors, exception logs. |
| ISO/IEC 42001 | AI management system for valuation and recommendation models, including ownership, fairness review, human oversight, and release approvals. | AI inventory, risk treatments, oversight thresholds, model review minutes. |
| ISO 22301 | Business continuity planning for critical APIs, asynchronous workflows, failover, backup, and manual continuity procedures. | BIA outputs, DR runbooks, failover tests, tabletop exercise records. |
| ISO 31000 | Risk governance for product, operational, cyber, model, legal, and market risks, with treatment plans and KRIs. | Risk taxonomy, treatment records, KRI dashboards, governance minutes. |

## 3. Control mapping by platform layer

| Platform layer | Key controls | Relevant standards |
| --- | --- | --- |
| Frontend/BFF | Strong authentication, consent capture, secure sessions, profile-context validation, accessibility, progressive disclosure, explanation visibility, action logging. | ISO/IEC 27001, ISO/IEC 27701, ISO/IEC 25010, ISO 9241-210 |
| Identity and trust plane | OIDC, MFA, RBAC, entitlements, KYC integration, AML scoring, sanctions screening, privacy-tier propagation. | ISO/IEC 27001, ISO/IEC 27701, SOC 2 Type 2 |
| Router/orchestration | Intent traceability, deterministic routing policy, valuation and recommendation expert coordination, transaction-stage integrity checks, confidence thresholds, expert aggregation and ranking, release gating, explanation generation, least-privilege response shaping. | ISO/IEC 25010, ISO/IEC 5259, ISO/IEC 42001, ISO 9241-210, ISO 31000, SOC 2 Type 2 |
| Expert microservices | Versioned models, scoped permissions, service isolation, evaluation metrics, contract tests. | ISO/IEC 27017, ISO/IEC 25010 |
| Event backbone | Durable delivery, retry logic, idempotency, dead-letter handling, event traceability. | ISO 22301, ISO/IEC 25010 |
| Data/evidence stores | Encryption, retention, lineage, immutable evidence, backup and recovery, data residency controls. | ISO/IEC 27001, ISO/IEC 27701, ISO 22301 |
| Security operations | SIEM, posture management, vulnerability response, incident coordination, evidence retention for audits. | ISO/IEC 27001, ISO/IEC 27017, SOC 2 Type 2, ISO 31000 |

## 4. Workflow-specific controls

### 4.1 Identity-aware profile routing
- Capture investor type, location, financial intent, residency goals, and consent scope from the frontend before expert selection.
- Bind profile data to authenticated subject IDs and reject anonymous high-trust actions.
- Record privacy tier and data residency requirements so the router can suppress or redact ineligible outputs.

### 4.2 Property valuation and investment analysis
- Verify market data provenance and freshness before model use.
- Preserve comparable-set rationale, trend features, and location-intelligence assumptions in the decision packet.
- Require ISO/IEC 5259 evidence for data completeness, comparability, and remediation when pricing or ranking outputs are released.
- Apply suitability and fairness rules using investor type and financial intent before releasing ranked outputs.
- Record ISO/IEC 42001 ownership, human-oversight triggers, and explainability artifacts for valuation and recommendation models.

### 4.3 Residency eligibility
- Version jurisdiction content and legal rules.
- Require KYC completion, sanctions screening, and human review for edge cases, adverse jurisdictions, or unclear source-of-funds.
- Bind recommendations to legal/evidence references and user profile completeness.

### 4.4 Insurance matching
- Enforce carrier licensing and servicing constraints.
- Retain peril and property exposure evidence with purpose limitation.
- Capture quote assumptions, exclusions, and underwriting blockers.

### 4.5 Financial risk and compliance
- Apply affordability, suitability, RBAC, MFA, KYC/AML, and sanctions checks before release.
- Escalate low-confidence or high-risk cases to manual review.
- Preserve adverse or blocked outcome reasoning for downstream audit.

### 4.6 Transaction intelligence and workflow integrity
- Enforce sequential deal stages so pricing, negotiation, document validation, approval, and closing remain auditable and replayable.
- Require tamper-evident document hashes, owner assignment, and remediation tracking for diligence, title, financing, disclosure, and closing artifacts.
- Bind ISO/IEC 27001 controls to access governance, evidence retention, and segregation of duties for release and approval actions.
- Bind ISO 22301 controls to alternate queues, workflow replay, RTO/RPO checkpoints, and manual continuity playbooks for critical transactions.
- Hold release when risk scoring, document validation, or continuity controls fall below threshold.

## 5. Audit evidence package for a single recommendation

A complete recommendation should preserve:
1. Request, correlation, and actor metadata.
2. Frontend-captured profile context and trust posture.
3. Consent and purpose-binding state.
4. Data sources, freshness, and lineage references.
5. Experts selected, scores, model versions, and ranking feature contributions.
6. Policy gates evaluated and their outcomes.
7. Final recommendation, explanation, and confidence/uncertainty.
8. Human approvals, overrides, and rationale.
9. Retention, continuity, deletion, and export metadata.

## 6. Operating assurance practices

- **Monthly operational review:** latency, drift, blocked-release trends, sanctions alerts, and resilience observations.
- **Quarterly assurance review:** control effectiveness, access governance, privacy evidence completeness, and entitlement recertification.
- **Annual management review:** risk posture, standard alignment, continuity readiness, and improvement plan updates.

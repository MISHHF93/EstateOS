# EstateOS Compliance and Assurance Mapping

## Control model

EstateOS uses a unified control model with four assurance layers:

1. **Preventive controls** – identity, network, secrets, secure SDLC, policy gates.
2. **Detective controls** – SIEM, anomaly detection, drift monitoring, logging, DLP.
3. **Corrective controls** – incident response, failover, rollback, human override.
4. **Evidence controls** – audit logs, policy versioning, approval records, evaluation reports.

## Standards alignment

| Framework / Standard | EstateOS design response | Primary evidence |
| --- | --- | --- |
| ISO/IEC 27001 | ISMS, asset inventory, risk treatment, secure operations, supplier governance. | Risk register, policies, change records, control tests. |
| ISO/IEC 27017 | Cloud-specific controls for Azure tenancy, virtual networks, logging, segmentation, and admin access. | Cloud baseline, landing zone configuration, CSPM reports. |
| ISO/IEC 27018 | Privacy controls for cloud-hosted PII, purpose limitation, retention, and processor obligations. | Consent receipts, retention policies, PII handling procedures. |
| ISO/IEC 27701 | Privacy information management layered onto the ISMS. | Data inventory, ROPA, DPIA records, rights-request workflows. |
| ISO/IEC 25010 | Software quality model covering reliability, security, maintainability, usability, and portability. | Quality gates, test coverage, NFR scorecards, ADRs. |
| ISO 9241-210 | Human-centered design process across research, prototyping, validation, and accessibility. | Personas, journey maps, usability findings, design rationale. |
| ISO 31000 | Enterprise risk management across product, operational, compliance, and model risks. | Risk taxonomy, treatment plans, KRIs, governance minutes. |
| ISO 22301 | Business continuity and resilience design for critical services and providers. | BCP/DR plans, failover tests, tabletop exercises. |
| PCI DSS | Segmented payment paths, tokenization, key management, least privilege, and monitoring. | Network diagrams, tokenization flows, ASV scans, key records. |
| SOC 2 Type 2 | Security, availability, confidentiality, and processing integrity controls operating over time. | Control narratives, evidence samples, exceptions log. |
| ISO/IEC 42001 | AI management system with model inventory, risk assessment, human oversight, and monitoring. | Model register, AI risk assessments, oversight procedures, incident logs. |
| ISO/IEC 5259 | Data quality and representativeness controls for AI datasets and outputs. | Dataset scorecards, lineage, quality metrics, bias assessments. |
| ACORD | Insurance data normalization and exchange standards embedded in intake and quoting flows. | Schemas, mappings, integration tests, partner certification artefacts. |
| NAIC-aligned expectations | Privacy, cybersecurity, governance, and third-party risk expectations for insurance use cases. | Governance framework, vendor reviews, privacy and security controls. |
| KYC/AML and sanctions | Identity verification, beneficial ownership, screening, source-of-funds, and alert management. | Screening logs, case management records, policy attestations. |

## Workflow-specific controls

### Property and pricing
- Listing feed provenance checks.
- Market data lineage and freshness SLAs.
- Model explainability for comparable sales and valuation confidence.

### RBI and migration
- Jurisdiction rules engine with versioned policy content.
- Mandatory human review for edge cases, high-risk geographies, and unclear source-of-funds.
- Evidence binding between applicant data, legal requirements, and recommendation outputs.

### Insurance
- ACORD-compliant payload generation.
- Carrier licensing and appointment checks.
- Hazard and claims data retention restricted by purpose and jurisdiction.

### Financial decision support
- Product suitability and affordability checks.
- Adverse-action style explanation support when workflows require it.
- Scenario model validation, stress testing, and governance.

## AI governance operating model

- **Inventory:** maintain registry of prompts, models, expert services, datasets, and downstream impacts.
- **Risk assessment:** score use cases by autonomy, sensitivity, explainability, and potential harm.
- **Controls:** apply thresholds for human review, policy gating, retraining, rollback, and release approval.
- **Monitoring:** drift, factuality, latency, cost, override rates, fairness metrics, and exception trends.
- **Review cadence:** monthly operational review, quarterly control assurance, annual formal management review.

## Audit evidence package for a single recommendation

1. Request metadata and identity context.
2. Consent and purpose metadata.
3. Data sources and freshness timestamps.
4. Experts selected and model versions.
5. Policy gates evaluated and outcome status.
6. Recommendation text with confidence and uncertainty bands.
7. Human actions, approvals, overrides, and rationale.
8. Retention, export, and deletion metadata.

# EstateOS Target Architecture

## 1. Platform vision

EstateOS is a full-stack real estate and investment platform where a seamless, role-aware frontend is backed by an Azure-native Mixture-of-Experts (MoE) decision mesh. The platform combines property discovery, a property intelligence and valuation expert system, a listing recommendation expert, investment analysis, residency-by-investment (RBI), insurance matching, payment and escrow intelligence, financial risk, transaction intelligence for pricing and negotiation, document validation, and compliance validation into one guided user experience while preserving explainability, auditability, workflow integrity, and secure control boundaries.

## 2. Full-stack experience architecture

### 2.1 Experience goals
- Deliver one cohesive journey for buyers, investors, brokers, insurers, and advisors instead of fragmented point tools.
- Hide backend orchestration complexity while surfacing confidence, assumptions, and required next actions.
- Support progressive disclosure so novice users get guidance and professionals get evidence-rich detail.
- Adapt layout, recommendation density, and explanation depth in real time based on persona, intent, budget, and trust posture in line with ISO 9241-210 human-centered design principles.
- Make every AI-assisted outcome traceable to the data sources, comparables, trend features, location signals, experts, policies, and approvals behind it.
- Capture user profile context early so investor type, location, financial intent, and residency goals directly shape routing and policy decisions.

### 2.2 Frontend domains
1. **Consumer web app**
   - Property search and portfolio discovery.
   - Investment scenario builder.
   - Residency eligibility planner.
   - Insurance readiness and quote intake with homeowners, title, landlord, and life-related recommendation paths.
   - Decision timeline, secure payment desk, escrow tracker, and document center.
2. **Advisor console**
   - Case review, exception handling, and override management.
   - Explainability and evidence drill-down.
   - Compliance, suitability, and approval checkpoints.
3. **Partner workspaces**
   - Broker workspace for listing and client pipeline actions.
   - Insurer/carrier view for ACORD-style intake, secure quote matching, and policy-class recommendations across homeowners, title, landlord, and life-related coverages.
   - Payments/escrow workspace for fraud triage, transaction monitoring, settlement exceptions, and escrow release orchestration.
   - Legal/migration workspace for RBI review and evidence completion.
4. **External API consumers**
   - Embedded finance, payment gateways, escrow providers, partner CRM, property inventory, KYC providers, insurers, and valuation data vendors.

### 2.3 Frontend composition pattern
- **Presentation layer:** web UI built as modular micro-frontends or feature slices for search, valuation, residency, insurance, secure payments, finance, transaction operations, and compliance.
- **Identity capture layer:** profile forms and consent modules collect investor type, residence, target location, financial intent, residency goals, and privacy preferences and package them as a profile-context payload.
- **Experience orchestration layer:** a backend-for-frontend (BFF) exposes user-ready view models, explanation cards, action states, and trust-state banners.
- **Design system:** reusable trust patterns including confidence badges, policy banners, evidence drawers, human-review indicators, privacy notices, PCI-safe payment shells, escrow state banners, and “why this recommendation” ledgers.
- **State model:** session state maintains user intent, profile completion, portfolio context, documents, trust posture, payment state, escrow milestones, and decision milestones.
- **Observability hooks:** every critical action emits telemetry, consent events, and user journey checkpoints.

### 2.4 Persona-sensitive journeys
- **Buyer:** shortlist properties, assess fair value, test affordability, complete tokenized earnest-money steps, confirm insurance readiness, and understand purchase risks.
- **Investor:** compare markets, rank return scenarios, evaluate cross-border residency options, and review concentration, liquidity, fraud, and payment behavior risks.
- **Broker:** receive next-best inventory and matching opportunities, along with sale blockers, escrow status, and compliance hold points.
- **Insurer:** review normalized property exposure, peril indicators, and quote suitability signals.
- **Payment operations:** inspect fraud triggers, payment velocity, reconciliation exceptions, settlement cutoffs, and escrow release conditions.
- **Advisor:** inspect AI reasoning, policy decisions, payment release posture, document sufficiency, and required approvals before releasing guidance.

### 2.5 User-facing explainability model
Every important screen includes:
- a plain-language summary,
- experts consulted,
- confidence and uncertainty ranges,
- data freshness,
- payment tokenization and escrow state,
- policy checks performed,
- blocked actions and remediation steps,
- human review status,
- identity and privacy state used to tailor release scope.

This aligns to ISO/IEC 25010 quality attributes for usability, reliability, and functional suitability while reinforcing trust and accountable AI behavior.

## 3. Identity, trust, and access architecture

### 3.1 Identity lifecycle
1. User authenticates through **Microsoft Entra ID / Entra External ID** using OIDC/OAuth2.
2. Frontend requests step-up MFA when the workflow reaches a high-trust action such as advisor approval, export, offer submission, or regulated recommendation release.
3. Frontend captures profile attributes including investor type, location, financial intent, residency goals, budget, and household context.
4. Identity service normalizes RBAC roles, entitlements, consent scope, privacy preferences, KYC status, AML risk, and sanctions state.
5. BFF binds this trust context to the session and sends it to the MoE router as part of the routing envelope.

### 3.2 Trust context object
The canonical identity and trust object should include:
- subject ID and authentication assurance level,
- MFA completion state,
- RBAC roles and fine-grained entitlements,
- KYC status and beneficial ownership status,
- AML risk tier and source-of-funds status,
- sanctions/PEP screening status,
- privacy tier, consent scope, and retention preferences,
- payment authorization scope, escrow role, and settlement permissions,
- geography and data residency constraints.

### 3.3 Access control model
- **RBAC baseline:** customer, investor, advisor, broker, compliance reviewer, insurer, and platform admin roles.
- **Entitlement overlay:** decisions such as `decision:view`, `decision:export`, `decision:approve`, `document:review`, and `partner:quote:request` are granted separately from coarse roles.
- **Step-up access:** sensitive actions require stronger assurance and MFA even when the role already permits the action.
- **Separation of duties:** advisor recommendation approval, compliance release, and privileged admin changes are segregated.
- **Just-in-time access:** temporary privileged access is logged, time-bound, and reviewed.

## 4. Backend MoE system architecture

### 4.1 Core control planes
1. **Experience control plane**
   - Backend-for-frontend.
   - Session and identity context manager.
   - Consent and preference manager.
2. **Identity and trust control plane**
   - Authentication and token validation.
   - RBAC and entitlement decision service.
   - MFA and step-up orchestration.
   - KYC/AML and sanctions provider integrations.
   - Privacy profile and data residency manager.
3. **Intelligence control plane**
   - Intent classification.
   - Context assembly.
   - Intelligent routing and expert arbitration.
   - Result synthesizer.
   - Explanation composer.
4. **Governance control plane**
   - Policy registry.
   - Compliance decision service.
   - Model registry and evaluation.
   - Audit and evidence ledger.
5. **Operations control plane**
   - Telemetry, SRE controls, incident response, resilience automation, and business continuity workflows.

### 4.2 Specialized expert services
The MoE backend is composed of independently deployable expert services with clearly bounded responsibilities:

| Expert service | Core responsibility | Typical inputs | Example outputs |
| --- | --- | --- | --- |
| Property Valuation Expert | Property fair value, comparables, uncertainty, trends, and location intelligence | Listing data, MLS feeds, geospatial signals, comps, market feeds | Value range, comp rationale, trend/location explanation, market confidence |
| Listing Recommendation Expert | Preference-aware ranking of listings across expert outputs | User goals, valuation confidence, comps, trends, location signals, fairness diagnostics | Ranked listings, why-this-rank rationale, preference-fit explanation |
| Investment Analysis Expert | Yield, IRR, DSCR, appreciation scenarios, portfolio fit | Rent comps, financing terms, taxes, macro signals | Scenario rankings, downside cases, ROI explanation |
| Residency Eligibility Expert | RBI/visa pathway screening by jurisdiction | Nationality, family profile, capital budget, legal constraints | Eligible pathways, steps, exclusions, human-review flags |
| Insurance Matching Expert | Insurability and coverage fit | Property attributes, peril data, occupancy, jurisdiction | Coverage shortlist, exclusions, quote readiness |
| Payment Intelligence Expert | Payment fraud probability, escrow conditions, payer behavior, settlement and reconciliation intelligence | Tokenized payment events, device telemetry, funding source, escrow milestones, chargeback history | Fraud score, release posture, reconciliation exceptions, escrow actions |
| Financial Risk Expert | Affordability, leverage, liquidity, payment capacity | Income, liabilities, cash reserves, rates, FX | Affordability bands, stress tests, financing constraints |
| Compliance Validation Expert | RBAC, MFA, KYC/AML, sanctions, privacy, records, release rules | Identity evidence, transactions, jurisdiction, consent | Release/hold decision, policy evidence, remediation tasks |
| UX Personalization Expert | Persona-specific message framing and next-best actions | Role, behavior, stage, confidence, blockers | Screen copy, workflow nudges, escalation paths |
| Pricing Strategy Expert | Offer ladders, concession bands, and timing strategy | Deal stage, target value, urgency, market conditions | Opening offer, counter range, walk-away threshold |
| Negotiation Insights Expert | Counterparty posture and concession sequencing | Counter history, seller motivation, approval rules | Negotiation posture, concession advice, escalation trigger |
| Document Validation Expert | Contract, diligence, title, and disclosure quality control | Uploaded documents, hashes, signatures, checklist state | Missing items, validation issues, release blockers |
| Deal Risk Scoring Expert | Transaction execution risk and workflow integrity scoring | Deal stage, open issues, financing ratio, counterparty risk | Risk score, risk rating, review/hold recommendation |

### 4.3 Intelligent routing layer
The routing layer is the system’s arbitration engine. It dynamically selects experts and determines execution order using:
- user intent,
- user role,
- investor type,
- profile completeness,
- geography and jurisdiction,
- financial intent,
- residency goals,
- trust posture from identity services,
- transaction stage,
- payment method and settlement posture,
- risk level,
- prior expert confidence,
- policy dependencies,
- latency/cost budgets,
- mandatory regulatory gates.

#### Routing algorithm responsibilities
- determine required experts,
- identify optional augmentation experts,
- parallelize independent expert calls,
- force compliance validation before release,
- escalate to human review when thresholds are crossed,
- tokenize and isolate PAN-adjacent data so frontend and orchestration layers remain out of PCI card-data scope where possible,
- redact or limit outputs based on privacy tier and entitlements,
- compose a single response with evidence and rationale.
- aggregate and rank candidate properties, investment insights, visa pathways, insurance options, and payment-release conditions into a single explainable recommendation board driven by a dedicated recommendation expert.
- enforce transaction stage order, document completeness, escrow checkpoints, continuity checkpoints, and approval segregation before a deal advances to closing.

#### Example orchestration paths
- **Cross-border investor in Portugal** → identity trust evaluation + valuation + investment + residency + payment intelligence + financial risk + insurance + compliance.
- **Domestic homebuyer comparing list price vs value** → identity trust evaluation + valuation + financial risk + payment release review + compliance.
- **High-risk insurance inquiry in a coastal flood zone** → identity trust evaluation + insurance + risk + compliance + advisor review.
- **Escrow funding event with anomalous payer behavior** → identity trust evaluation + payment intelligence + financial risk + compliance + payment operations review.

### 4.4 Expert interaction model
1. Frontend sends a workflow request to the BFF.
2. BFF enriches the request with identity, profile, consent, and journey context.
3. Router selects primary and secondary experts.
4. Experts execute via synchronous APIs for interactive decisions and event-driven tasks for longer-running enrichment.
5. A synthesizer merges structured expert outputs into a unified recommendation.
6. Payment tokenization, escrow, and reconciliation services attach secure funding state without exposing sensitive cardholder data.
7. Policy services evaluate whether the result can be released, partially released, or held.
8. Audit and evidence services persist the full decision packet.
9. Frontend receives a user-facing response plus explainability metadata.

## 5. Azure deployment blueprint

### 5.1 Edge and identity
- **Azure Front Door + WAF** for global entry, TLS termination, and edge protection.
- **Azure API Management** for secure API publishing, throttling, partner onboarding, and policy enforcement.
- **Microsoft Entra ID / Entra External ID** for workforce and customer identity, MFA, conditional access, and RBAC.
- **Microsoft Entra Verified ID or KYC vendors** for reusable identity proofs and document verification workflows.

### 5.2 Runtime topology
- **Azure Kubernetes Service (AKS):** long-lived expert services, router, synthesizer, policy APIs, and internal platform services.
- **Azure Container Apps:** burstable expert workloads, experimentation services, and partner-specific adapters.
- **Azure Functions:** asynchronous events, evidence generation, notifications, and scheduled control tasks.
- **Logic Apps:** human workflow integration, third-party approvals, RBI/legal handoffs, insurer follow-up, and regulated exception routing.

### 5.3 Data and AI services
- **Azure SQL:** transactional workflow state, case management, approvals, policy references, payment reconciliation records, and access control metadata.
- **Azure Cosmos DB:** low-latency session context, expert state snapshots, journey progress, and payment risk signals.
- **Azure Data Lake Storage Gen2:** evidence packets, prompt/model lineage, historical decisions, settlement files, and analytics landing zones.
- **Azure AI Search:** retrieval over legal content, policy manuals, property documents, and underwriting references.
- **Azure OpenAI / managed model endpoints:** expert inference and summarization where foundation models are required.
- **Azure Machine Learning:** model registry, evaluation pipelines, feature tracking, and promotion workflows.

### 5.4 Security and operations stack
- **Azure Key Vault** for secrets, keys, certificates, and payment-provider signing material.
- **Microsoft Purview** for cataloging, lineage, and data governance.
- **Azure Monitor + Application Insights** for metrics, traces, service maps, and settlement health telemetry.
- **Microsoft Sentinel** for security analytics, alerting, and incident workflows.
- **Microsoft Defender for Cloud** for posture management and workload protection.

### 5.5 Azure AI deployment fabric for MoE services
- Package each expert, router, synthesizer, policy service, and model-serving adapter as signed OCI images stored in **Azure Container Registry (ACR)** with content trust, vulnerability scanning, and environment-specific repositories.
- Run latency-sensitive inference paths on **AKS** using dedicated node pools: CPU pools for routing and policy services, GPU pools for dense or multimodal experts, and confidential-compute-capable pools where regulated workloads or high-sensitivity prompts require stronger memory isolation.
- Use **KEDA** and **Horizontal Pod Autoscaler** policies to scale experts independently from queue depth, tokens-per-second, GPU utilization, concurrency, and latency SLOs so valuation, investment, and compliance experts can burst without overprovisioning the entire platform.
- Apply **Azure Service Mesh / Istio-compatible service mesh controls** for mTLS, service identity, traffic shaping, retries, circuit breaking, canary rollout, and per-expert authorization boundaries.
- Keep short-lived or partner-specific experts on **Azure Container Apps** when elasticity matters more than always-on capacity, while routing all workloads through the same policy, telemetry, and evidence contracts.
- Place model gateways behind internal load balancers and private endpoints so prompts, embeddings, retrieved documents, and model outputs never traverse the public internet.

### 5.6 Model versioning, release promotion, and rollback
- Manage foundation-model adapters, fine-tuned checkpoints, prompt templates, safety policies, and evaluation datasets in **Azure Machine Learning registries** with immutable version IDs and approval states.
- Promote model bundles through `dev`, `validation`, `preprod`, and `prod` environments using CI/CD gates that require benchmark, red-team, privacy, and bias-review evidence before a router can target a newly approved expert version.
- Store feature schemas, inference contracts, and retrieval index versions alongside model artifacts so every decision packet can reference the exact expert code image, model version, prompt version, and grounding corpus snapshot used at runtime.
- Use blue/green and canary deployments in AKS with automated rollback when latency, hallucination, safety, payment-risk false-positive rates, or business KPI thresholds regress.
- Preserve previous champion versions in hot standby so regulated workflows can revert to a last-known-good bundle without rebuilding containers during an incident.

### 5.7 Monitoring, evaluation, and SRE pipelines
- Stream platform, inference, and policy events into **Azure Monitor**, **Log Analytics**, and **Application Insights** with OpenTelemetry traces that correlate user journeys, router decisions, expert invocations, queue lag, and model latency.
- Push model-quality telemetry to **Azure Machine Learning** monitoring pipelines for drift detection, data quality checks, prompt regression, hallucination sampling, and expert-level champion/challenger comparison.
- Land raw telemetry, audit packets, and evaluation outputs in **Data Lake Storage Gen2** for long-term retention, forensics, and periodic control testing.
- Feed security-relevant signals such as anomalous admin actions, prompt abuse, model endpoint spikes, PCI-segment access attempts, and data exfiltration indicators into **Microsoft Sentinel** and **Defender for Cloud** for SOC workflows.
- Define SLOs for availability, p95 latency, routing success rate, explainability completeness, payment-risk scoring freshness, and recovery time, with automated alerting and runbooks owned jointly by platform engineering, security, and model operations.

## 6. Event-driven orchestration and secure APIs

### 6.1 API strategy
- Expose secure REST/GraphQL endpoints through API Management.
- Use private networking for internal expert-to-expert communication.
- Apply schema versioning, contract testing, and signed service identities.
- Separate interactive APIs from batch and event ingestion paths.
- Tokenize cardholder data in hosted fields or PSP-controlled iFrames so EstateOS frontend components never store raw PAN or CVV.
- Treat profile-context ingestion as a first-class API so frontend-captured identity signals are versioned and auditable.

### 6.2 Event backbone
- **Azure Service Bus** for durable expert workflow commands, payment review queues, and compensating actions.
- **Azure Event Grid** for domain events such as profile-updated, valuation-completed, compliance-held, insurance-match-generated, payment-risk-scored, or reconciliation-exception-opened.
- **Durable Functions or workflow engines** for long-running cases that require document collection, human review, partner callbacks, escrow release, or settlement exception handling.

### 6.3 Canonical event sequence
1. `journey.requested`
2. `identity.profile.ingested`
3. `context.assembled`
4. `experts.selected`
5. `expert.<domain>.completed`
6. `payment.risk.scored`
7. `payment.reconciliation.completed`
8. `policy.validation.completed`
9. `decision.composed`
10. `decision.released` or `decision.held`
11. `audit.packet.persisted`
12. `notification.dispatched`

### 6.4 Explainability and evidence payloads
Each event and final response should carry:
- request and correlation IDs,
- user and actor role,
- trust posture and assurance level,
- experts selected and model versions,
- input source references and freshness,
- confidence/uncertainty,
- payment fraud score and escrow state,
- policy outcomes,
- human approvals or overrides,
- retention and export metadata.

## 7. Security, privacy, and assurance architecture

### 7.1 ISO/IEC 27001 and ISO/IEC 27017 alignment
- Formal ISMS with asset inventory, risk treatment, access governance, secure software delivery, and operational playbooks that are enforced across landing zones, AKS clusters, ACR, and data services.
- Cloud-specific baselines define subscription segmentation, private networking, admin isolation, hardened images, policy-as-code, and shared-responsibility assignments for every Azure service in the MoE fabric.
- Key management, encryption, backup protection, and logging baselines are embedded in the landing zone so expert services inherit security controls by default.

### 7.2 ISO/IEC 27018 and ISO/IEC 27701 privacy alignment
- Privacy information management extends the ISMS with purpose limitation, data subject handling, retention rules, consent governance, and privacy-by-default release controls.
- ISO/IEC 27018 expectations are addressed through tenant-scoped processing boundaries, restricted operator access, customer-directed deletion workflows, pseudonymization of training/evaluation payloads, and auditable handling of personally identifiable information in cloud services.
- Router outputs, logs, and evidence packets are privacy-tiered so only permitted explanation depth reaches each user role and downstream support teams.

### 7.3 PCI DSS and SOC 2 Type 2 alignment
- PCI DSS boundaries are enforced through PSP-hosted fields, tokenized payment methods, segmented payment services, WAF controls, log redaction, quarterly segmentation testing, and tightly scoped operator access for payment workflows.
- SOC 2 Type 2 evidence is generated from change records, access reviews, alert triage, backup tests, vulnerability remediation, and continuous monitoring of the Azure control plane and model-serving services.
- Model and orchestration deployments inherit approval gates, immutable logs, and dual-control release patterns so security, availability, confidentiality, processing integrity, and privacy controls operate over time.

### 7.4 ISO/IEC 5259 and ISO/IEC 42001 AI governance alignment
- ISO/IEC 5259 data quality controls govern market feeds, comparable sets, trend features, and location intelligence before valuation or ranking outputs are released.
- ISO/IEC 42001 AI management controls define accountable owners, fairness reviews, human oversight triggers, and evidence requirements for valuation and recommendation models.
- Both standards extend the existing evidence model so every ranked listing includes traceable data provenance, quality status, and explainability artifacts.

### 7.5 ISO/IEC 25010 quality alignment
The architecture explicitly supports:
- **Functional suitability:** expert specialization and policy-aware routing.
- **Performance efficiency:** parallel expert execution and event-driven decoupling.
- **Compatibility:** API contracts and partner integration adapters.
- **Usability:** explainable BFF models and persona-aware workflows.
- **Reliability:** retries, active-active deployment, circuit breakers, and graceful degradation.
- **Security:** zero-trust controls and release gating.
- **Maintainability:** independently deployable microservices and versioned contracts.
- **Portability:** containerized services and policy-as-code patterns.

### 7.6 ISO 22301 resilience alignment
- Business impact analysis identifies critical workflows such as compliance release and transaction-critical guidance.
- Recovery strategies include active-active APIs, queue buffering, regional failover, and tested restoration procedures.
- Manual fallback modes allow advisors to continue case handling when specific experts are unavailable.

### 7.7 ISO 31000 risk management alignment
- Maintain an enterprise risk register spanning operational, cyber, model, legal, and market risks.
- Score expert outputs and workflow designs for likelihood, impact, and control effectiveness.
- Use KRIs for latency spikes, policy override rates, model drift, sanctions alerts, and resilience degradation.

## 8. Auditability and explainability by design

### 8.1 Decision packet model
Every recommendation produces a decision packet containing:
- request metadata,
- frontend-captured profile attributes,
- identity and trust state,
- experts selected and not selected,
- expert scores and rationale,
- policy dependencies and results,
- synthesized recommendation,
- release status,
- reviewer actions,
- timestamps and lineage identifiers.

### 8.2 Human governance model
- Human review is mandatory for low-confidence, high-risk, or jurisdictionally sensitive cases.
- Overrides require rationale capture and immutable logging.
- Reviewer dashboards expose evidence bundles, prior decisions, and control exceptions.

### 8.3 AI accountability model
- Register each expert service, prompt template, model version, and evaluation score.
- Track hallucination, factuality, consistency, and override metrics.
- Preserve reproducibility inputs so decisions can be replayed or independently audited.

## 9. Scalability and platform evolution
- Use domain-driven microservices with shared platform controls rather than a monolith.
- Scale experts horizontally based on domain demand and SLA class.
- Add new experts, such as tax advisory or sustainability scoring, without redesigning the frontend contract.
- Support champion/challenger evaluation and safe rollouts for expert versions.
- Keep orchestration policy-driven so market, regulatory, and operational changes can be absorbed quickly.

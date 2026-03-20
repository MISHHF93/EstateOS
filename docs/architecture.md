# EstateOS Target Architecture

## 1. Platform vision

EstateOS is a full-stack real estate and investment platform where a seamless, role-aware frontend is backed by an Azure-native Mixture-of-Experts (MoE) decision mesh. The platform combines property discovery, valuation, investment analysis, residency-by-investment (RBI), insurance matching, financial risk, and compliance validation into one guided user experience while preserving explainability, auditability, and secure control boundaries.

## 2. Full-stack experience architecture

### 2.1 Experience goals
- Deliver one cohesive journey for buyers, investors, brokers, insurers, and advisors instead of fragmented point tools.
- Hide backend orchestration complexity while surfacing confidence, assumptions, and required next actions.
- Support progressive disclosure so novice users get guidance and professionals get evidence-rich detail.
- Make every AI-assisted outcome traceable to the data sources, experts, policies, and approvals behind it.

### 2.2 Frontend domains
1. **Consumer web app**
   - Property search and portfolio discovery.
   - Investment scenario builder.
   - Residency eligibility planner.
   - Insurance readiness and quote intake.
   - Decision timeline and document center.
2. **Advisor console**
   - Case review, exception handling, and override management.
   - Explainability and evidence drill-down.
   - Compliance, suitability, and approval checkpoints.
3. **Partner workspaces**
   - Broker workspace for listing and client pipeline actions.
   - Insurer/carrier view for ACORD-style intake and quote matching.
   - Legal/migration workspace for RBI review and evidence completion.
4. **External API consumers**
   - Embedded finance, partner CRM, property inventory, KYC providers, insurers, and valuation data vendors.

### 2.3 Frontend composition pattern
- **Presentation layer:** web UI built as modular micro-frontends or feature slices for search, valuation, residency, insurance, finance, and compliance.
- **Experience orchestration layer:** a backend-for-frontend (BFF) exposes user-ready view models, explanation cards, and action states.
- **Design system:** reusable trust patterns including confidence badges, policy banners, evidence drawers, and human-review indicators.
- **State model:** session state maintains user intent, profile completion, portfolio context, documents, and decision milestones.
- **Observability hooks:** every critical action emits telemetry, consent events, and user journey checkpoints.

### 2.4 Persona-sensitive journeys
- **Buyer:** shortlist properties, assess fair value, test affordability, confirm insurance readiness, and understand purchase risks.
- **Investor:** compare markets, rank return scenarios, evaluate cross-border residency options, and review concentration/liquidity risks.
- **Broker:** receive next-best inventory and matching opportunities, along with sale blockers and compliance hold points.
- **Insurer:** review normalized property exposure, peril indicators, and quote suitability signals.
- **Advisor:** inspect AI reasoning, policy decisions, document sufficiency, and required approvals before releasing guidance.

### 2.5 User-facing explainability model
Every important screen includes:
- a plain-language summary,
- experts consulted,
- confidence and uncertainty ranges,
- data freshness,
- policy checks performed,
- blocked actions and remediation steps,
- human review status.

This aligns to ISO/IEC 25010 quality attributes for usability, reliability, and functional suitability while reinforcing trust and accountable AI behavior.

## 3. Backend MoE system architecture

### 3.1 Core control planes
1. **Experience control plane**
   - Backend-for-frontend.
   - Session and identity context manager.
   - Consent and preference manager.
2. **Intelligence control plane**
   - Intent classification.
   - Context assembly.
   - Intelligent routing and expert arbitration.
   - Result synthesizer.
   - Explanation composer.
3. **Governance control plane**
   - Policy registry.
   - Compliance decision service.
   - Model registry and evaluation.
   - Audit and evidence ledger.
4. **Operations control plane**
   - Telemetry, SRE controls, incident response, resilience automation, and business continuity workflows.

### 3.2 Specialized expert services
The MoE backend is composed of independently deployable expert services with clearly bounded responsibilities:

| Expert service | Core responsibility | Typical inputs | Example outputs |
| --- | --- | --- | --- |
| Property Valuation Expert | Property fair value, comparables, uncertainty, market positioning | Listing data, MLS feeds, geospatial signals, comps | Value range, comp rationale, market confidence |
| Investment Analysis Expert | Yield, IRR, DSCR, appreciation scenarios, portfolio fit | Rent comps, financing terms, taxes, macro signals | Scenario rankings, downside cases, ROI explanation |
| Residency Eligibility Expert | RBI/visa pathway screening by jurisdiction | Nationality, family profile, capital budget, legal constraints | Eligible pathways, steps, exclusions, human-review flags |
| Insurance Matching Expert | Insurability and coverage fit | Property attributes, peril data, occupancy, jurisdiction | Coverage shortlist, exclusions, quote readiness |
| Financial Risk Expert | Affordability, leverage, liquidity, payment capacity | Income, liabilities, cash reserves, rates, FX | Affordability bands, stress tests, financing constraints |
| Compliance Validation Expert | KYC/AML, sanctions, privacy, records, release rules | Identity evidence, transactions, jurisdiction, consent | Release/hold decision, policy evidence, remediation tasks |
| UX Personalization Expert | Persona-specific message framing and next-best actions | Role, behavior, stage, confidence, blockers | Screen copy, workflow nudges, escalation paths |

### 3.3 Intelligent routing layer
The routing layer is the system’s arbitration engine. It dynamically selects experts and determines execution order using:
- user intent,
- user role,
- profile completeness,
- jurisdiction,
- transaction stage,
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
- compose a single response with evidence and rationale.

#### Example orchestration paths
- **Cross-border investor in Portugal** → valuation + investment + residency + financial risk + insurance + compliance.
- **Domestic homebuyer comparing list price vs value** → valuation + financial risk + compliance.
- **High-risk insurance inquiry in a coastal flood zone** → insurance + risk + compliance + advisor review.

### 3.4 Expert interaction model
1. Frontend sends a workflow request to the BFF.
2. BFF enriches the request with identity, profile, consent, and journey context.
3. Router selects primary and secondary experts.
4. Experts execute via synchronous APIs for interactive decisions and event-driven tasks for longer-running enrichment.
5. A synthesizer merges structured expert outputs into a unified recommendation.
6. Policy services evaluate whether the result can be released, partially released, or held.
7. Audit and evidence services persist the full decision packet.
8. Frontend receives a user-facing response plus explainability metadata.

## 4. Azure deployment blueprint

### 4.1 Edge and identity
- **Azure Front Door + WAF** for global entry, TLS termination, and edge protection.
- **Azure API Management** for secure API publishing, throttling, partner onboarding, and policy enforcement.
- **Microsoft Entra ID / Entra External ID** for workforce and customer identity, MFA, conditional access, and RBAC.

### 4.2 Runtime topology
- **Azure Kubernetes Service (AKS):** long-lived expert services, router, synthesizer, policy APIs, and internal platform services.
- **Azure Container Apps:** burstable expert workloads, experimentation services, and partner-specific adapters.
- **Azure Functions:** asynchronous events, evidence generation, notifications, and scheduled control tasks.
- **Logic Apps:** human workflow integration, third-party approvals, RBI/legal handoffs, insurer follow-up, and regulated exception routing.

### 4.3 Data and AI services
- **Azure SQL:** transactional workflow state, case management, approvals, and policy references.
- **Azure Cosmos DB:** low-latency session context, expert state snapshots, and journey progress.
- **Azure Data Lake Storage Gen2:** evidence packets, prompt/model lineage, historical decisions, and analytics landing zones.
- **Azure AI Search:** retrieval over legal content, policy manuals, property documents, and underwriting references.
- **Azure OpenAI / managed model endpoints:** expert inference and summarization where foundation models are required.
- **Azure Machine Learning:** model registry, evaluation pipelines, feature tracking, and promotion workflows.

### 4.4 Security and operations stack
- **Azure Key Vault** for secrets, keys, and certificates.
- **Microsoft Purview** for cataloging, lineage, and data governance.
- **Azure Monitor + Application Insights** for metrics, traces, and service maps.
- **Microsoft Sentinel** for security analytics, alerting, and incident workflows.
- **Microsoft Defender for Cloud** for posture management and workload protection.

## 5. Event-driven orchestration and secure APIs

### 5.1 API strategy
- Expose secure REST/GraphQL endpoints through API Management.
- Use private networking for internal expert-to-expert communication.
- Apply schema versioning, contract testing, and signed service identities.
- Separate interactive APIs from batch and event ingestion paths.

### 5.2 Event backbone
- **Azure Service Bus** for durable expert workflow commands and compensating actions.
- **Azure Event Grid** for domain events such as profile-updated, valuation-completed, compliance-held, or insurance-match-generated.
- **Durable Functions or workflow engines** for long-running cases that require document collection, human review, or partner callbacks.

### 5.3 Canonical event sequence
1. `journey.requested`
2. `context.assembled`
3. `experts.selected`
4. `expert.<domain>.completed`
5. `policy.validation.completed`
6. `decision.composed`
7. `decision.released` or `decision.held`
8. `audit.packet.persisted`
9. `notification.dispatched`

### 5.4 Explainability and evidence payloads
Each event and final response should carry:
- request and correlation IDs,
- user and actor role,
- experts selected and model versions,
- input source references and freshness,
- confidence/uncertainty,
- policy outcomes,
- human approvals or overrides,
- retention and export metadata.

## 6. Security, privacy, and assurance architecture

### 6.1 ISO/IEC 27001 and ISO/IEC 27017 alignment
- Formal ISMS with asset inventory, risk treatment, access governance, and secure operations.
- Cloud-specific baselines for segmentation, hardening, privileged access, logging, and third-party management.
- Key management, encryption, and secure software delivery embedded in Azure landing zones.

### 6.2 ISO/IEC 25010 quality alignment
The architecture explicitly supports:
- **Functional suitability:** expert specialization and policy-aware routing.
- **Performance efficiency:** parallel expert execution and event-driven decoupling.
- **Compatibility:** API contracts and partner integration adapters.
- **Usability:** explainable BFF models and persona-aware workflows.
- **Reliability:** retries, active-active deployment, circuit breakers, and graceful degradation.
- **Security:** zero-trust controls and release gating.
- **Maintainability:** independently deployable microservices and versioned contracts.
- **Portability:** containerized services and policy-as-code patterns.

### 6.3 ISO 22301 resilience alignment
- Business impact analysis identifies critical workflows such as compliance release and transaction-critical guidance.
- Recovery strategies include active-active APIs, queue buffering, regional failover, and tested restoration procedures.
- Manual fallback modes allow advisors to continue case handling when specific experts are unavailable.

### 6.4 ISO 31000 risk management alignment
- Maintain an enterprise risk register spanning operational, cyber, model, legal, and market risks.
- Score expert outputs and workflow designs for likelihood, impact, and control effectiveness.
- Use KRIs for latency spikes, policy override rates, model drift, sanctions alerts, and resilience degradation.

## 7. Auditability and explainability by design

### 7.1 Decision packet model
Every recommendation produces a decision packet containing:
- request metadata,
- user/profile context references,
- experts selected and not selected,
- expert scores and rationale,
- policy dependencies and results,
- synthesized recommendation,
- release status,
- reviewer actions,
- timestamps and lineage identifiers.

### 7.2 Human governance model
- Human review is mandatory for low-confidence, high-risk, or jurisdictionally sensitive cases.
- Overrides require rationale capture and immutable logging.
- Reviewer dashboards expose evidence bundles, prior decisions, and control exceptions.

### 7.3 AI accountability model
- Register each expert service, prompt template, model version, and evaluation score.
- Track hallucination, factuality, consistency, and override metrics.
- Preserve reproducibility inputs so decisions can be replayed or independently audited.

## 8. Scalability and platform evolution
- Use domain-driven microservices with shared platform controls rather than a monolith.
- Scale experts horizontally based on domain demand and SLA class.
- Add new experts, such as tax advisory or sustainability scoring, without redesigning the frontend contract.
- Support champion/challenger evaluation and safe rollouts for expert versions.
- Keep orchestration policy-driven so market, regulatory, and operational changes can be absorbed quickly.

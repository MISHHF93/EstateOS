# EstateOS Target Architecture

## 1. Platform vision

EstateOS is a full-stack real estate and investment platform where a seamless, role-aware frontend is backed by an Azure-native Mixture-of-Experts (MoE) decision mesh. The platform combines property discovery, a property intelligence and valuation expert system, a listing recommendation expert, investment analysis, residency-by-investment (RBI), insurance matching, financial risk, and compliance validation into one guided user experience while preserving explainability, auditability, and secure control boundaries.

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
- **Identity capture layer:** profile forms and consent modules collect investor type, residence, target location, financial intent, residency goals, and privacy preferences and package them as a profile-context payload.
- **Experience orchestration layer:** a backend-for-frontend (BFF) exposes user-ready view models, explanation cards, action states, and trust-state banners.
- **Design system:** reusable trust patterns including confidence badges, policy banners, evidence drawers, human-review indicators, privacy notices, and “why this recommendation” ledgers.
- **State model:** session state maintains user intent, profile completion, portfolio context, documents, trust posture, and decision milestones.
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
| Financial Risk Expert | Affordability, leverage, liquidity, payment capacity | Income, liabilities, cash reserves, rates, FX | Affordability bands, stress tests, financing constraints |
| Compliance Validation Expert | RBAC, MFA, KYC/AML, sanctions, privacy, records, release rules | Identity evidence, transactions, jurisdiction, consent | Release/hold decision, policy evidence, remediation tasks |
| UX Personalization Expert | Persona-specific message framing and next-best actions | Role, behavior, stage, confidence, blockers | Screen copy, workflow nudges, escalation paths |

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
- redact or limit outputs based on privacy tier and entitlements,
- compose a single response with evidence and rationale.
- aggregate and rank candidate properties, investment insights, visa pathways, and insurance options into a single explainable recommendation board driven by a dedicated recommendation expert.

#### Example orchestration paths
- **Cross-border investor in Portugal** → identity trust evaluation + valuation + investment + residency + financial risk + insurance + compliance.
- **Domestic homebuyer comparing list price vs value** → identity trust evaluation + valuation + financial risk + compliance.
- **High-risk insurance inquiry in a coastal flood zone** → identity trust evaluation + insurance + risk + compliance + advisor review.

### 4.4 Expert interaction model
1. Frontend sends a workflow request to the BFF.
2. BFF enriches the request with identity, profile, consent, and journey context.
3. Router selects primary and secondary experts.
4. Experts execute via synchronous APIs for interactive decisions and event-driven tasks for longer-running enrichment.
5. A synthesizer merges structured expert outputs into a unified recommendation.
6. Policy services evaluate whether the result can be released, partially released, or held.
7. Audit and evidence services persist the full decision packet.
8. Frontend receives a user-facing response plus explainability metadata.

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
- **Azure SQL:** transactional workflow state, case management, approvals, policy references, and access control metadata.
- **Azure Cosmos DB:** low-latency session context, expert state snapshots, and journey progress.
- **Azure Data Lake Storage Gen2:** evidence packets, prompt/model lineage, historical decisions, and analytics landing zones.
- **Azure AI Search:** retrieval over legal content, policy manuals, property documents, and underwriting references.
- **Azure OpenAI / managed model endpoints:** expert inference and summarization where foundation models are required.
- **Azure Machine Learning:** model registry, evaluation pipelines, feature tracking, and promotion workflows.

### 5.4 Security and operations stack
- **Azure Key Vault** for secrets, keys, and certificates.
- **Microsoft Purview** for cataloging, lineage, and data governance.
- **Azure Monitor + Application Insights** for metrics, traces, and service maps.
- **Microsoft Sentinel** for security analytics, alerting, and incident workflows.
- **Microsoft Defender for Cloud** for posture management and workload protection.

## 6. Event-driven orchestration and secure APIs

### 6.1 API strategy
- Expose secure REST/GraphQL endpoints through API Management.
- Use private networking for internal expert-to-expert communication.
- Apply schema versioning, contract testing, and signed service identities.
- Separate interactive APIs from batch and event ingestion paths.
- Treat profile-context ingestion as a first-class API so frontend-captured identity signals are versioned and auditable.

### 6.2 Event backbone
- **Azure Service Bus** for durable expert workflow commands and compensating actions.
- **Azure Event Grid** for domain events such as profile-updated, valuation-completed, compliance-held, or insurance-match-generated.
- **Durable Functions or workflow engines** for long-running cases that require document collection, human review, or partner callbacks.

### 6.3 Canonical event sequence
1. `journey.requested`
2. `identity.profile.ingested`
3. `context.assembled`
4. `experts.selected`
5. `expert.<domain>.completed`
6. `policy.validation.completed`
7. `decision.composed`
8. `decision.released` or `decision.held`
9. `audit.packet.persisted`
10. `notification.dispatched`

### 6.4 Explainability and evidence payloads
Each event and final response should carry:
- request and correlation IDs,
- user and actor role,
- trust posture and assurance level,
- experts selected and model versions,
- input source references and freshness,
- confidence/uncertainty,
- policy outcomes,
- human approvals or overrides,
- retention and export metadata.

## 7. Security, privacy, and assurance architecture

### 7.1 ISO/IEC 27001 and ISO/IEC 27017 alignment
- Formal ISMS with asset inventory, risk treatment, access governance, and secure operations.
- Cloud-specific baselines for segmentation, hardening, privileged access, logging, and third-party management.
- Key management, encryption, and secure software delivery embedded in Azure landing zones.

### 7.2 ISO/IEC 27701 and SOC 2 Type 2 alignment
- Privacy information management extends the ISMS with purpose limitation, data subject handling, retention rules, and consent governance.
- RBAC, MFA, audit evidence, and exception approvals map directly to SOC 2 security, confidentiality, and privacy criteria.
- Router outputs are privacy-tiered so only permitted explanation depth reaches each user role.

### 7.3 ISO/IEC 5259 and ISO/IEC 42001 AI governance alignment
- ISO/IEC 5259 data quality controls govern market feeds, comparable sets, trend features, and location intelligence before valuation or ranking outputs are released.
- ISO/IEC 42001 AI management controls define accountable owners, fairness reviews, human oversight triggers, and evidence requirements for valuation and recommendation models.
- Both standards extend the existing evidence model so every ranked listing includes traceable data provenance, quality status, and explainability artifacts.

### 7.4 ISO/IEC 25010 quality alignment
The architecture explicitly supports:
- **Functional suitability:** expert specialization and policy-aware routing.
- **Performance efficiency:** parallel expert execution and event-driven decoupling.
- **Compatibility:** API contracts and partner integration adapters.
- **Usability:** explainable BFF models and persona-aware workflows.
- **Reliability:** retries, active-active deployment, circuit breakers, and graceful degradation.
- **Security:** zero-trust controls and release gating.
- **Maintainability:** independently deployable microservices and versioned contracts.
- **Portability:** containerized services and policy-as-code patterns.

### 7.4 ISO 22301 resilience alignment
- Business impact analysis identifies critical workflows such as compliance release and transaction-critical guidance.
- Recovery strategies include active-active APIs, queue buffering, regional failover, and tested restoration procedures.
- Manual fallback modes allow advisors to continue case handling when specific experts are unavailable.

### 7.5 ISO 31000 risk management alignment
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

# EstateOS Production Platform Blueprint

## 1. Intent

This blueprint translates the EstateOS target state into a production-oriented implementation contract for a **modular full-stack, AI-native real estate platform**.

The platform unifies:

- property discovery,
- investment analysis,
- residency-by-investment workflows,
- insurance integration,
- payments and escrow-aware transaction management,
- compliance and trust controls,
- explainable AI decision support.

## 2. Full-stack architecture

### 2.1 Frontend experience layer

The production customer surface should converge under **Next.js + React + TypeScript** in `apps/web/` with a design system based on Tailwind CSS, shadcn/ui, TanStack Query, and state management via Zustand or Redux Toolkit.

Primary UX modules:

1. **Property discovery** with search, map exploration, saved searches, and AI-guided matching.
2. **Investor workspace** with ROI, valuation, market signals, risk, and portfolio comparisons.
3. **Residency-by-investment workspace** with eligibility intake, document collection, and case tracking.
4. **Insurance journey** with ACORD-aware quote requests, carrier matching, and coverage explanations.
5. **Payments and transaction management** with escrow milestones, payment status, approvals, and audit-ready deal rooms.
6. **Documents and e-signature surfaces** for secure uploads, review queues, and release-gated workflows.
7. **Broker/admin/compliance console** in `apps/admin/` for underwriting, investigations, release control, and exception handling.

Design expectations:

- elegant, responsive, human-centered UX,
- progressive disclosure for complex finance/compliance signals,
- explainable AI insights instead of opaque scores,
- accessibility-aware interaction design,
- multilingual readiness for cross-border buyers and investors.

### 2.2 Backend control plane

The backend should standardize on **Python FastAPI** as the primary application runtime and start as a **modular monolith** with explicit service boundaries for later extraction.

Canonical modules:

- authentication,
- user profiles,
- listings,
- search,
- deals,
- documents,
- residency workflows,
- insurance,
- payments,
- compliance,
- notifications,
- integrations,
- AI orchestration.

The API-facing layer should preserve space for:

- Azure API Management,
- a BFF or composition layer for web/mobile/admin clients,
- OIDC/OAuth2 enforcement,
- consent and privacy propagation,
- audit enrichment,
- rate limiting and release policy hooks.

### 2.3 Azure-native platform baseline

Default production infrastructure should use:

- Azure Front Door,
- Azure API Management,
- Azure App Service or AKS,
- Azure Database for PostgreSQL,
- Azure Cache for Redis,
- Azure Blob Storage,
- Azure Service Bus,
- Azure Key Vault,
- Azure AI Search,
- Azure Machine Learning,
- Azure Monitor,
- Microsoft Sentinel,
- Defender for Cloud.

## 3. Mixture-of-Experts decision layer

The EstateOS MoE layer must dynamically route requests to specialized experts and aggregate explainable outputs into one user-facing decision packet.

### 3.1 Canonical expert mesh

1. Property recommendation.
2. Valuation.
3. ROI analysis.
4. Residency eligibility.
5. Insurance matching.
6. Fraud detection.
7. Compliance / AML / sanctions screening.
8. Document intelligence.
9. Personalization.
10. Market forecasting.

### 3.2 Routing expectations

The orchestrator should consider:

- user type,
- geography and jurisdiction,
- property type,
- investment objective,
- residency intent,
- KYC/AML/sanctions state,
- transaction stage,
- privacy tier,
- document completeness,
- payment and insurance needs.

### 3.3 Output contract

Every AI response should include:

- selected experts,
- per-expert assessments,
- ranked recommendations,
- explainable rationale,
- policy gates,
- human-review status,
- immutable audit event references.

## 4. Relational schema baseline

The relational core should preserve strong normalization, traceability, and auditable workflow relationships.

### 4.1 Core entities

| Entity | Purpose | Key relationships |
| --- | --- | --- |
| `users` | principal identity records | joins to profiles, roles, deals, documents, payments, compliance, AI requests |
| `roles` | RBAC catalog | joins through `user_roles` |
| `user_roles` | entitlement mapping | links users to roles |
| `user_profiles` | investor/buyer profile and privacy preferences | one-to-one or one-to-many from users |
| `properties` | immutable-ish real-world asset records | one-to-many to listings, insurance requests, residency applications |
| `listings` | commercial catalog entries | references properties and brokers |
| `deals` | transaction and negotiation container | references listings and participants |
| `deal_participants` | buyer, seller, advisor, legal, broker roles | references deals and users |
| `documents` | uploaded evidence and deal artifacts | polymorphic link to deals, residency, compliance, insurance |
| `residency_applications` | migration program tracking | references users and optionally properties |
| `insurance_requests` | quote/placement workflow records | references users and properties |
| `payment_intents` / `payments` | PSP orchestration and settlement records | references deals and users |
| `compliance_cases` | KYC/AML/sanctions investigations | references users, deals, and alerts |
| `ai_requests` | MoE routing, release status, and evidence | references users, listings, and workflow context |

### 4.2 Supporting patterns

The production schema should also accommodate:

- audit logs,
- event outbox tables,
- consent ledgers,
- sanctions and screening results,
- document extraction results,
- partner integration credentials stored via Key Vault references,
- model governance metadata for AI explainability and release management.

## 5. REST API baseline

The platform should expose versioned REST APIs for the major workflows:

- `POST /auth/register`, `POST /auth/login`
- `GET /users/me`, `PUT /users/me/preferences`
- `GET /listings`, `POST /listings`, `GET /listings/{id}`
- `POST /deals`, `POST /deals/{id}/offers`, `GET /deals/{id}`
- `POST /documents/presign`, `POST /documents/{id}/complete`
- `GET /residency/programs`, `POST /residency/applications`, `POST /residency/applications/{id}/assess`
- `POST /insurance/requests`, `GET /insurance/requests/{id}/quotes`
- `POST /payments/intents`, `GET /payments/{id}`
- `GET /compliance/cases/{id}`, `GET /compliance/screening-checks/{id}`
- `POST /ai/assess`

## 6. Event-driven lifecycle

Key lifecycle events should be published through Azure Service Bus or equivalent infrastructure:

- `listing.published`
- `deal.created`
- `document.uploaded`
- `ai.request.routed`
- `residency.assessment.completed`
- `insurance.quote.requested`
- `payment.succeeded`
- `compliance.case.escalated`

## 7. Security, privacy, and governance posture

The platform should enforce enterprise-grade controls aligned with:

- ISO/IEC 27001,
- ISO/IEC 27017,
- ISO/IEC 27018,
- ISO/IEC 27701,
- ISO/IEC 25010,
- ISO 22301,
- ISO 31000,
- PCI DSS,
- SOC 2 Type 2,
- ISO/IEC 42001,
- ISO/IEC 5259.

Operational expectations also include:

- ACORD-oriented insurance interoperability,
- NAIC-oriented data security and privacy expectations,
- KYC / AML / sanctions / PEP / beneficial ownership controls,
- explainable AI release management,
- auditable human-in-the-loop approvals for elevated-risk cases.

## 8. Delivery interpretation

EstateOS should be treated as a **single intelligent decision infrastructure** where real estate, finance, insurance, and investment migration workflows share a common trust plane, event model, and explainable MoE orchestration fabric.

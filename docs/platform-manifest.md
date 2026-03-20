# EstateOS Platform Manifest

## 1. Purpose

This manifest is the repo-level checkpoint that converts the authoritative MoE real estate platform blueprint into concrete implementation guardrails for EstateOS.

Use it to verify that product framing, repository structure, service boundaries, expert taxonomy, Azure deployment choices, and compliance posture stay aligned with the target platform.

## 2. Product identity

EstateOS should continue to be framed as:

- **an AI-native real estate intelligence platform with MoE-driven decision support** for property, migration, insurance, compliance, and finance, and
- **a real estate operating system powered by a Mixture-of-Experts AI backbone**.

Any new docs, demos, or implementation scaffolding should reinforce that positioning rather than introduce narrower or conflicting narratives.

## 3. Layer contract

### 3.1 Frontend experience layer

The premium frontend surface must cover:

- public marketing site,
- property discovery and maps,
- investor workspace,
- residency / visa intake,
- insurance journey,
- payments / escrow UI,
- documents / eSignature / deal room,
- AI insights, recommendations, and risk explanations,
- broker / admin / compliance operations.

Implementation guardrails:

- production-grade customer UI belongs in `apps/web/`,
- operator and compliance tooling belongs in `apps/admin/`,
- mobile remains optional under `apps/mobile/`,
- legacy `frontend/` assets remain prototype-only until migrated.

### 3.2 API gateway / BFF layer

EstateOS must preserve room for:

- API gateway,
- backend-for-frontend,
- auth gateway,
- rate limiting,
- session management,
- consent hooks,
- audit hooks.

Implementation guardrails:

- shared contracts should converge under `packages/types/` and `packages/config/`,
- web-specific orchestration should not bypass service-layer auth, consent, or audit controls,
- BFF concerns should remain explicit in architecture notes even when implemented inside a modular monolith.

### 3.3 Core application services

The canonical service map remains:

- auth,
- users,
- listings,
- transactions,
- documents,
- visa-workflows,
- insurance,
- payments,
- compliance,
- ai-orchestrator,
- integrations,
- notifications,
- admin/reporting.

Implementation guardrails:

- service boundaries should be represented under `services/`,
- the initial delivery model remains **modular monolith first**,
- extraction into separate deployable services should happen only when scale, compliance isolation, or team topology justifies it.

### 3.4 AI orchestration / MoE layer

The orchestrator must:

- detect user intent,
- interpret user type, geography, property type, investment goal, residency intent, risk score, and transaction stage,
- select one or more experts,
- aggregate and rank outputs,
- explain outcomes,
- preserve audit evidence,
- support policy and human-review gating.

The canonical expert set remains:

1. Property Recommendation Expert.
2. Property Valuation Expert.
3. Investment ROI Expert.
4. Residency / Visa Eligibility Expert.
5. Insurance Recommendation Expert.
6. Payment / Fraud / Financial Risk Expert.
7. Compliance / AML / Sanctions Expert.
8. UX Personalization Expert.
9. Document Intelligence Expert.
10. Market Forecast / Trend Expert.

Implementation guardrails:

- expert-specific implementations should converge under `experts/` and service-owned orchestration modules,
- production routing logic should converge under `services/ai-orchestrator/`,
- `backend/orchestration.py` remains a reference artifact only.

### 3.5 Data platform layer

The platform baseline remains:

- PostgreSQL,
- Redis,
- Azure Blob Storage,
- Azure Service Bus,
- Elasticsearch or Azure AI Search,
- feature/data layers for models,
- analytics and audit evidence storage.

Implementation guardrails:

- persistence and integration assumptions should stay visible in service contracts,
- infrastructure definitions should live under `infra/`,
- data quality, lineage, and auditability should be accounted for before AI outputs are treated as decision support.

### 3.6 Security / compliance / governance layer

The platform posture must stay aligned to:

- ISO/IEC 27001,
- ISO/IEC 27017,
- ISO/IEC 27018,
- ISO/IEC 27701,
- ISO/IEC 25010,
- ISO 9241-210,
- ISO/IEC 42001,
- ISO/IEC 5259,
- ISO 22301,
- ISO 31000,
- PCI DSS,
- SOC 2 Type 2,
- ACORD-oriented insurance interoperability,
- NAIC-aligned insurer privacy/security expectations,
- KYC / AML / sanctions / PEP / beneficial ownership controls.

Implementation guardrails:

- new feature docs should identify trust, audit, privacy, and evidence implications,
- payment flows should remain PCI-aware and tokenized,
- AI releases should preserve explainability, ownership, and governance hooks,
- compliance and fraud controls should remain cross-workflow rather than isolated to one feature area.

## 4. Locked stack decisions

### 4.1 Frontend

The premium product surface should standardize on:

- Next.js + React + TypeScript,
- Tailwind CSS,
- shadcn/ui,
- TanStack Query,
- Zustand or Redux Toolkit,
- i18n,
- Framer Motion,
- Mapbox or Google Maps,
- Stripe Elements or equivalent payment SDKs.

### 4.2 Backend

The backend direction should standardize on:

- FastAPI (Python) for AI-heavy backend logic,
- optional Node.js / NestJS for API orchestration where justified,
- PostgreSQL,
- Redis,
- Azure Blob Storage,
- Azure Service Bus,
- Elasticsearch or Azure AI Search,
- Keycloak or Microsoft Entra External ID / Azure AD B2C,
- Temporal or Camunda.

## 5. Azure deployment baseline

The preferred Azure footprint remains:

- Azure Front Door,
- Azure API Management,
- Azure App Service or AKS,
- Azure Database for PostgreSQL,
- Azure Cache for Redis,
- Azure Blob Storage,
- Azure Service Bus,
- Azure Key Vault,
- Azure Monitor,
- Microsoft Sentinel,
- Azure AI Search,
- Azure Machine Learning,
- GitHub Actions or Azure DevOps,
- Defender for Cloud.

## 6. Delivery-phase gate

### 6.1 MVP

Primary scope:

- listings,
- auth,
- search,
- deal workflow,
- payments,
- basic AI recommender,
- base KYC / compliance,
- Azure deployment baseline.

### 6.2 Phase 2

Expansion scope:

- visa workflow engine,
- insurance integrations,
- valuation expert,
- ROI expert,
- admin / compliance workbench.

### 6.3 Phase 3

Full-platform scope:

- Autonomous Deal Execution Engine (Agentic AI Layer),
- Digital Twin Properties & Simulation Engine,
- Predictive Market Intelligence & Macro AI,
- Conversational AI Copilot (Multi-Role Assistant),
- On-Chain / Tokenization & Fractional Ownership Layer,
- Advanced Document Intelligence & Legal Reasoning AI,
- Global Compliance Graph & Regulatory Intelligence System,
- Hyper-Personalization & Behavioral Modeling Engine,
- Trust, Reputation, and Risk Scoring Network,
- Open AI Marketplace & Third-Party Expert Plug-in Ecosystem.

## 7. Repository alignment checklist

A change is aligned when it does all of the following:

1. keeps the MoE real estate operating-system framing intact,
2. lands production-oriented frontend work under `apps/`,
3. lands production-oriented backend work under `services/`,
4. preserves the modular-monolith-first service model,
5. uses the ten-expert taxonomy and router responsibilities,
6. preserves Azure as the default deployment direction,
7. documents trust, privacy, audit, and compliance implications,
8. avoids drift away from the locked frontend/backend stack without explicit justification.

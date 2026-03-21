# EstateOS Implementation Roadmap

## 1. Purpose

This roadmap translates the target MoE real estate platform architecture into a realistic execution sequence for the current repository.

## 2. Current-state assessment

The repository currently contains:

- a lightweight frontend concept in `frontend/`,
- a Python orchestration prototype in `backend/orchestration.py`,
- architecture, MoE, and compliance documentation in `docs/`.

That means the project is currently best interpreted as a **blueprint and reference prototype**, not yet the final Next.js/FastAPI monorepo.

## 3. Target-state decisions now locked in

### 3.1 Product

EstateOS should be described as:

- an AI-native real estate intelligence platform with MoE-driven decision support, and
- a real estate operating system powered by a Mixture-of-Experts AI backbone.

### 3.2 Frontend

Adopt:

- Next.js,
- React,
- TypeScript,
- Tailwind CSS,
- shadcn/ui,
- TanStack Query,
- Zustand or Redux Toolkit,
- i18n,
- Framer Motion,
- Mapbox or Google Maps,
- Stripe Elements where payments are exposed.

### 3.3 Backend

Adopt:

- FastAPI first,
- modular monolith first,
- PostgreSQL,
- Redis,
- Azure Blob Storage,
- Azure Service Bus,
- Azure AI Search or Elasticsearch,
- Entra External ID / Azure AD B2C / Keycloak,
- Temporal or Camunda.

### 3.4 AI expert model

Adopt the canonical ten-expert model:

1. Property Recommendation.
2. Property Valuation.
3. Investment ROI.
4. Residency / Visa Eligibility.
5. Insurance Recommendation.
6. Payment / Fraud / Financial Risk.
7. Compliance / AML / Sanctions.
8. UX Personalization.
9. Document Intelligence.
10. Market Forecast / Trend.

## 4. Delivery roadmap

### 4.1 Stage A — Repository transition

Objectives:

- preserve current docs and prototype value,
- introduce the target monorepo shape,
- avoid pretending the production architecture already exists.

Recommended actions:

- keep `apps/`, `services/`, `experts/`, `packages/`, and `infra/` as the future monorepo roots and land new production-grade code there,
- migrate `frontend/` into `apps/web/` when the Next.js rebuild begins, while treating the current `frontend/` folder as prototype-only,
- migrate orchestration logic from `backend/orchestration.py` into `services/ai-orchestrator/` when the FastAPI service is introduced, while treating the current backend script as reference-only,
- centralize types/contracts under `packages/types/`.

### 4.2 Stage B — MVP build

Ship:

- public site,
- property discovery,
- auth,
- listing search,
- deal workflow,
- payment initiation,
- basic recommender,
- base KYC / compliance,
- Azure deployment baseline.

Technical scope:

- Next.js app in `apps/web/`,
- FastAPI modular backend,
- PostgreSQL + Redis,
- Blob Storage for files,
- Entra or Keycloak for identity,
- Stripe-based payment surface,
- Service Bus for async events.

### 4.3 Stage C — Phase 2 expansion

Ship:

- visa workflow engine,
- insurance integrations,
- valuation expert,
- ROI expert,
- admin / compliance workbench.

Technical scope:

- workflow orchestration through Temporal or Camunda,
- insurance payload mapping and referral orchestration,
- valuation and ROI services,
- stronger evidence and admin tooling.

### 4.4 Stage D — Phase 3 advanced intelligence platform

Ship:

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

Technical scope:

- production-grade agent orchestration and execution controls,
- simulation infrastructure for digital twin property modeling,
- macro and market intelligence pipelines,
- legal reasoning and document-grounded AI workflows,
- compliance graph services with global regulatory telemetry,
- partner and third-party expert marketplace infrastructure.

The target design for the semi-autonomous transaction layer is specified in `docs/autonomous-deal-execution-engine.md`, covering agent roles, workflow control, approval gating, audit evidence, and ISO/IEC 27001 plus ISO 31000 alignment expectations.
The target design for privacy-preserving adaptive experiences is specified in `docs/hyper-personalization-behavioral-intelligence-engine.md`, covering behavioral telemetry, recommendation and UX adaptation, communication strategy controls, ISO/IEC 27701 privacy management, and ethical-AI release boundaries.

## 5. Standards posture by phase

### 5.1 MVP

Must visibly support:

- ISO/IEC 27001,
- ISO/IEC 27701,
- ISO/IEC 25010,
- ISO 9241-210,
- PCI DSS boundary awareness,
- KYC / AML / sanctions baselines.

### 5.2 Phase 2

Expand to stronger support for:

- ISO/IEC 27017,
- ISO/IEC 27018,
- SOC 2 Type 2 evidence operations,
- ACORD / NAIC-aligned insurer workflows,
- ISO 22301 continuity planning.

### 5.3 Phase 3

Formalize:

- ISO/IEC 42001 AI governance,
- ISO/IEC 5259 AI/data quality,
- ISO 31000 risk governance,
- full model lineage, evaluation, rollback, and explainability controls.

## 6. Working interpretation for contributors

When making future changes, contributors should treat the following as mandatory target-state guidance:

- the six-layer platform architecture,
- the premium Next.js-based frontend stack,
- the FastAPI-first backend direction,
- the ten-expert MoE model,
- the Azure deployment baseline,
- the phased MVP → Phase 2 → Phase 3 delivery plan.

## 7. Immediate next implementation steps

The next practical build steps should be:

1. scaffold a real Next.js + TypeScript app under `apps/web/`,
2. stand up a FastAPI service for `ai-orchestrator`,
3. define shared contracts for profile, trust, listings, deals, and explanations,
4. introduce PostgreSQL and Redis-backed local development,
5. separate current prototype content into migration-safe folders,
6. add infrastructure definitions under `infra/`,
7. begin implementing the MVP feature set before Phase 2 or Phase 3 ambitions.


## 8. Transition note

The repository now already contains the scaffolded monorepo roots described above. Contributors should prefer those directories for new production-grade work and use `docs/repository-transition.md` as the operating guide for the migration state.

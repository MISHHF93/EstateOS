# EstateOS Blueprint Alignment Guide

## 1. Purpose

This document turns the current EstateOS repository into an explicit **alignment checkpoint** against the target MoE real estate platform architecture.

Use it when deciding whether a change belongs in this repository, where it should land, and whether it respects the locked product, platform, AI, and compliance direction.

## 2. Authoritative platform framing

EstateOS should be described as:

- **an AI-native real estate intelligence platform with MoE-driven decision support** for property, migration, insurance, compliance, and finance, and
- **a real estate operating system powered by a Mixture-of-Experts AI backbone**.

All repo-level architecture and implementation choices should reinforce that framing.

## 3. Layer-by-layer alignment contract

### 3.1 Frontend experience layer

The premium product surface must center on:

- Next.js + React + TypeScript,
- Tailwind CSS,
- shadcn/ui,
- TanStack Query,
- Zustand or Redux Toolkit,
- i18n,
- Framer Motion,
- Mapbox or Google Maps,
- Stripe Elements or equivalent payment SDKs where payment capture is exposed.

The required frontend zones are:

- public marketing site,
- property discovery app,
- investor workspace,
- insurance flow,
- visa / residency intake flow,
- broker / admin / compliance console.

Repository mapping:

- `apps/web/` owns the primary customer-facing Next.js implementation.
- `apps/admin/` owns the operator, broker, and compliance console.
- `apps/mobile/` is reserved for a future mobile companion if mobile becomes product-critical.
- `frontend/` remains prototype-only until the Next.js migration is complete.

### 3.2 API gateway / BFF layer

The API control plane must include:

- API gateway,
- backend-for-frontend,
- auth gateway,
- rate limiting,
- session controls,
- consent hooks,
- audit hooks.

Repository mapping:

- cross-cutting contracts should be captured under `packages/types/` and `packages/config/`,
- orchestration entrypoints should converge under `services/ai-orchestrator/`,
- identity and release controls should remain explicit in service boundaries rather than hidden inside UI logic.

### 3.3 Core application services

The canonical service map is:

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

Repository mapping:

- `services/auth-service/`
- `services/user-service/`
- `services/listing-service/`
- `services/transaction-service/`
- `services/document-service/`
- `services/visa-service/`
- `services/insurance-service/`
- `services/payment-service/`
- `services/compliance-service/`
- `services/integration-service/`
- `services/notification-service/`
- `services/admin-reporting-service/`
- `services/ai-orchestrator/`

Delivery rule:

- implement as a **modular monolith first** unless there is a strong scaling or team-structure reason to extract services.

### 3.4 AI orchestration / MoE layer

The expert router must:

- detect user intent,
- interpret stage, profile, geography, risk, and goals,
- choose one or more experts,
- aggregate and rank expert outputs,
- explain why the result was produced,
- enforce compliance and release gating,
- preserve evidence for audit and governance.

The canonical experts are:

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

Repository mapping:

- expert-specific logic should evolve under `experts/` and/or service-owned expert modules,
- shared explanation schemas, policy dependencies, and evidence contracts should be defined under `packages/types/`,
- `backend/orchestration.py` remains a reference implementation, not the final production architecture.

### 3.5 Data platform layer

The baseline data platform remains:

- PostgreSQL,
- Redis,
- Azure Blob Storage,
- Azure Service Bus,
- Azure AI Search or Elasticsearch,
- feature/data layers for model inputs,
- analytics and audit evidence storage.

Repository mapping:

- infrastructure definitions belong under `infra/`,
- reusable data contracts belong under `packages/types/`,
- event and storage assumptions must be reflected in service boundaries and docs.

### 3.6 Security / compliance / governance layer

The platform should stay aligned to:

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
- ACORD-oriented interoperability,
- NAIC-aligned insurer privacy/security expectations,
- KYC / AML / sanctions / PEP / beneficial ownership requirements.

Repository mapping:

- authoritative control notes live in `docs/compliance-mapping.md`,
- architecture and repo-shape guardrails live in `docs/architecture.md` and `docs/repository-transition.md`,
- any new feature design should identify its trust, audit, privacy, and release implications up front.

## 4. Azure deployment baseline

The preferred Azure footprint is:

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

All infrastructure additions should preserve this Azure-native direction unless a deliberate architecture decision supersedes it.

## 5. Delivery-phase alignment

### 5.1 MVP

Allowed priority scope:

- listings,
- auth,
- search,
- deal workflow,
- payments,
- basic AI recommender,
- base KYC / compliance,
- Azure deployment baseline.

### 5.2 Phase 2

Expansion scope:

- visa workflow engine,
- insurance integrations,
- valuation expert,
- ROI expert,
- admin / compliance workbench.

### 5.3 Phase 3

Full platform scope:

- full expert routing,
- model explainability expansion,
- dynamic UX personalization,
- forecasting,
- broker / insurer / government integrations,
- advanced document intelligence.

## 6. Contributor checklist

Before merging a change, verify that it does all of the following:

1. Places new production-oriented frontend code under `apps/`, not `frontend/`, unless the change is intentionally prototype-only.
2. Places new production-oriented backend code under `services/`, not only under `backend/`.
3. Preserves the modular-monolith-first backend boundary model.
4. Uses the ten-expert MoE taxonomy and router responsibilities as the conceptual baseline.
5. Keeps Azure as the default deployment and governance target.
6. Identifies trust, audit, privacy, and compliance implications for new features.
7. Avoids introducing stack drift away from Next.js/React/TypeScript on the frontend or FastAPI-first on the AI-heavy backend without explicit justification.
8. Keeps shared schemas, policies, or cross-cutting contracts in `packages/` where reuse is expected.

## 7. Repository interpretation

The repository should now be interpreted as:

- a blueprint for the target platform,
- a staging area for the canonical monorepo structure,
- a lightweight prototype for product storytelling and orchestration references,
- and a governed foundation for building the future Azure-based MoE real estate platform without architecture drift.

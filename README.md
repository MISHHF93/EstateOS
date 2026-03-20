# EstateOS

EstateOS is being shaped as **an AI-native real estate operating system powered by a Mixture-of-Experts (MoE) backbone**. The repository now treats the architecture you provided as the **authoritative target-state blueprint** for product, platform, AI orchestration, and compliance.

## Target product framing

EstateOS is positioned as:

- **An AI-native real estate intelligence platform with MoE-driven decision support** for property, migration, insurance, compliance, and finance.
- **A real estate operating system** where property discovery, investor workflows, residency-by-investment journeys, insurance flows, payments, documents, and compliance operate through one explainable control surface.

## Canonical platform architecture

The target platform follows six major layers:

1. **Frontend experience layer**
   - Public marketing site.
   - Property discovery application.
   - Investor workspace.
   - Residency / visa intake flow.
   - Insurance journey.
   - Broker / admin / compliance console.
2. **API gateway / BFF layer**
   - API gateway.
   - Backend-for-frontend.
   - Auth gateway.
   - Rate limiting, consent, audit, and session hooks.
3. **Core application services**
   - Auth, users, listings, transactions, documents.
   - Visa workflows, insurance, payments, compliance.
   - Integrations, notifications, admin/reporting.
4. **AI orchestration / MoE layer**
   - Intent-aware router.
   - Expert selection, aggregation, ranking, and explanation.
   - Human-review and policy-release gating.
5. **Data platform layer**
   - PostgreSQL, Redis, Blob Storage, Service Bus, Azure AI Search, analytics, audit logs.
6. **Security / compliance / governance layer**
   - ISO/IEC 27001, 27017, 27018, 27701, 25010, 42001, 5259, 22301, 31000.
   - PCI DSS, SOC 2 Type 2, ACORD/NAIC-aligned workflows, KYC/AML/sanctions/PEP.

Detailed architecture guidance lives in `docs/architecture.md`, the exact source-of-truth blueprint now lives in `docs/authoritative-blueprint.md`, and the repository migration rules now live in `docs/repository-transition.md`.
A repo-wide alignment checklist now lives in `docs/blueprint-alignment.md` so contributors can quickly validate that new work still matches the locked MoE real estate platform direction. `docs/platform-manifest.md` adds a concise implementation-facing contract that maps the authoritative blueprint to repository guardrails and delivery phases.

## Required implementation stack

### Frontend target stack

- **Next.js + React + TypeScript**.
- **Tailwind CSS**.
- **shadcn/ui**.
- **TanStack Query**.
- **Zustand or Redux Toolkit**.
- **i18n** for multilingual support.
- **Framer Motion** for subtle motion.
- **Mapbox or Google Maps** for discovery experiences.
- **Stripe Elements or payment SDKs** for PCI-aware payment surfaces.

### Backend target stack

- **FastAPI (Python)** as the primary AI-heavy backend foundation.
- **Modular monolith first**, with a future path to service extraction.
- **PostgreSQL** for OLTP.
- **Redis** for caching and ephemeral workflow state.
- **Azure Blob Storage** for documents and evidence.
- **Azure Service Bus** for asynchronous workflows.
- **Elasticsearch or Azure AI Search** for search and retrieval.
- **Keycloak or Microsoft Entra External ID / Azure AD B2C** for identity.
- **Temporal or Camunda** for workflow orchestration.

## Current repository intent

This repository is still a **reference implementation + architecture blueprint**, not yet the full production monorepo. Its current assets now do four things:

- document the authoritative target architecture,
- provide a lightweight Python orchestration reference in `backend/orchestration.py`,
- provide a visual product-direction prototype in `frontend/`, and
- scaffold the canonical monorepo roots in `apps/`, `services/`, `experts/`, `packages/`, and `infra/` so implementation work can land in the correct target locations.

## Canonical target repo structure

The target repository shape we are now aligning toward is:

```text
realestate-moe-platform/
├── apps/
│   ├── web/
│   ├── admin/
│   └── mobile/
├── services/
│   ├── auth-service/
│   ├── user-service/
│   ├── listing-service/
│   ├── transaction-service/
│   ├── document-service/
│   ├── visa-service/
│   ├── insurance-service/
│   ├── payment-service/
│   ├── compliance-service/
│   ├── integration-service/
│   ├── notification-service/
│   ├── admin-reporting-service/
│   └── ai-orchestrator/
├── experts/
│   ├── property-recommender/
│   ├── valuation-expert/
│   ├── roi-expert/
│   ├── visa-expert/
│   ├── insurance-expert/
│   ├── fraud-expert/
│   ├── compliance-expert/
│   ├── ux-expert/
│   ├── document-expert/
│   └── market-forecast-expert/
├── packages/
│   ├── ui/
│   ├── types/
│   ├── config/
│   └── shared-utils/
├── infra/
│   ├── terraform/
│   ├── bicep/
│   └── kubernetes/
└── docs/
```

## Delivery model

### MVP
- Listings.
- Auth.
- Search.
- Deal workflow.
- Payments.
- Basic AI recommender.
- Base KYC/compliance.
- Azure deployment baseline.

### Phase 2
- Visa workflow engine.
- Insurance integrations.
- Valuation expert.
- ROI expert.
- Admin/compliance workbench.

### Phase 3
- Full MoE routing.
- Model explainability expansion.
- Dynamic UX personalization.
- Market forecasting.
- Broker / insurer / government integrations.
- Advanced document intelligence.

A practical implementation roadmap is captured in `docs/implementation-roadmap.md`, and the repository transition expectations are captured in `docs/repository-transition.md`.

## MoE expert model

The canonical expert set is:

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

The router activates experts based on user type, location, property type, investment goal, residency intent, risk score, and transaction stage. See `docs/moe-platform-model.md`.

## Azure deployment baseline

The recommended Azure footprint is:

- Azure Front Door.
- Azure API Management.
- Azure App Service or AKS.
- Azure Database for PostgreSQL.
- Azure Cache for Redis.
- Azure Blob Storage.
- Azure Service Bus.
- Azure Key Vault.
- Azure Monitor.
- Microsoft Sentinel.
- Azure AI Search.
- Azure Machine Learning.
- GitHub Actions or Azure DevOps.
- Defender for Cloud.

## Standards and control posture

EstateOS should remain aligned to:

- ISO/IEC 27001, 27017, 27018, 27701.
- ISO/IEC 25010 and ISO 9241-210.
- ISO/IEC 42001 and ISO/IEC 5259.
- ISO 22301 and ISO 31000.
- PCI DSS and SOC 2 Type 2.
- ACORD-oriented interoperability.
- NAIC-aligned privacy/security expectations.
- KYC / AML / sanctions / PEP requirements.

See `docs/compliance-mapping.md` for the control mapping baseline.

## Quick start

Run the current orchestration reference implementation:

```bash
python3 backend/orchestration.py
```

## Repository status after this update

This update makes the provided architecture the explicit baseline for:

- product naming,
- stack choices,
- repo shape,
- AI expert taxonomy,
- phased rollout,
- Azure deployment assumptions, and
- standards alignment.

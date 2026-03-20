# EstateOS Target Architecture

## 1. Architecture baseline

EstateOS is being built as a **secure Azure-based real estate platform using a Mixture-of-Experts AI architecture**. The product baseline is now explicitly anchored to a premium frontend surface, a modular backend, an expert router, and a compliance-first Azure deployment model.

## 2. Layered platform model

### 2.1 Frontend experience layer

The frontend experience layer must provide:

- **Web app** using Next.js, React, and TypeScript.
- **Mobile app** using React Native or Flutter when mobile delivery becomes necessary.
- **Admin / broker / compliance portal** for operational teams.

The key UX modules are:

- property search and maps,
- investor dashboard,
- residency / visa journey,
- insurance journey,
- payments / escrow UI,
- documents / eSignature / deal room,
- AI insights, recommendations, and risk explanations.

### 2.2 API gateway / BFF layer

The API-facing control layer must include:

- API gateway,
- backend-for-frontend,
- auth gateway,
- rate limiting,
- session controls,
- consent hooks,
- audit hooks.

### 2.3 Core application services

The platform service map is:

- **Identity service** for user profiles, RBAC, MFA, KYC, consent, and access logs.
- **Listing service** for the property catalog, search, filters, media, and moderation.
- **Transaction service** for offers, reservations, documents, milestones, and notifications.
- **Visa workflow service** for residency rules, eligibility intake, and document collection.
- **Insurance service** for quotes, referrals, policy mapping, and ACORD-aligned exchange.
- **Payment service** for payment gateway orchestration, ledgers, reconciliation, escrow-style workflows, PCI-aware flows, and fraud hooks.
- **Integration service** for partner APIs and webhooks.
- **Notification service** for email, SMS, and push.
- **Reporting / admin service** for dashboards, operations, and audit views.

### 2.4 AI orchestration / MoE layer

The MoE layer must contain an **expert router / orchestrator** that:

- detects user intent,
- understands stage, profile, geography, risk, and goals,
- chooses one or more experts,
- aggregates and ranks expert outputs,
- explains why a recommendation or risk signal was produced.

The expert model is defined in detail in `docs/moe-platform-model.md`.

### 2.5 Data platform layer

The default data platform baseline is:

- PostgreSQL or Azure SQL for OLTP,
- Elasticsearch or Azure AI Search for search,
- Azure Blob Storage for objects,
- Azure Service Bus or Event Grid for events,
- Redis for cache,
- feature store / ML data layer,
- warehouse / analytics platform,
- audit logging, SIEM, and monitoring.

### 2.6 Security / compliance / governance layer

The architecture assumes continuous alignment to:

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
- ACORD and NAIC-aligned workflows,
- KYC/AML/PEP/sanctions/beneficial ownership requirements.

## 3. Product surface requirements

### 3.1 Frontend technology choices

The premium product surface should standardize on:

- **Next.js + React + TypeScript**,
- **Tailwind CSS**,
- **shadcn/ui**,
- **Mapbox or Google Maps**,
- **TanStack Query**,
- **Zustand or Redux Toolkit**,
- **i18n** for multilingual support,
- **Framer Motion**,
- **Stripe Elements or equivalent payment SDKs**.

### 3.2 Frontend zones

The product should be split into these zones:

- public marketing site,
- property discovery app,
- investor workspace,
- insurance flow,
- visa / residency intake flow,
- broker / admin / compliance console.

## 4. Backend implementation baseline

### 4.1 Delivery model

The recommended implementation pattern is:

- start with a **modular monolith** when speed and cohesion matter,
- extract to microservices when team maturity and scaling needs justify it.

### 4.2 Backend stack

The recommended backend stack is:

- **FastAPI (Python)** for AI-heavy backend functionality,
- **Node.js / NestJS** optionally for API orchestration if needed,
- **PostgreSQL**,
- **Redis**,
- **Azure Blob Storage**,
- **Azure Service Bus**,
- **Elasticsearch or Azure AI Search**,
- **Keycloak or Microsoft Entra External ID / Azure AD B2C**,
- **Temporal or Camunda**.

### 4.3 Canonical backend modules

The canonical module set is:

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

## 5. Azure deployment baseline

A strong default Azure layout is:

- Azure Front Door for global entry,
- Azure App Service or AKS for hosting,
- Azure API Management,
- Azure Database for PostgreSQL,
- Azure Cache for Redis,
- Azure Blob Storage,
- Azure Service Bus,
- Azure Key Vault,
- Azure Monitor,
- Microsoft Sentinel,
- Azure AI Search,
- Azure Machine Learning for model hosting and governance,
- Azure DevOps or GitHub Actions,
- Defender for Cloud.

## 6. Canonical repository structure

The repository now includes scaffolded `apps/`, `services/`, `experts/`, `packages/`, and `infra/` roots so contributors can place new implementation work in the target locations instead of expanding the legacy `frontend/` and `backend/` prototype folders. Transition expectations are defined in `docs/repository-transition.md`.

The platform should converge toward this monorepo shape:

```text
apps/
  web/
  admin/
  mobile/
services/
  auth-service/
  user-service/
  listing-service/
  transaction-service/
  visa-service/
  insurance-service/
  payment-service/
  compliance-service/
  integration-service/
  notification-service/
  ai-orchestrator/
experts/
  property-recommender/
  valuation-expert/
  roi-expert/
  visa-expert/
  insurance-expert/
  fraud-expert/
  compliance-expert/
  ux-expert/
  document-expert/
  market-forecast-expert/
packages/
  ui/
  types/
  config/
  shared-utils/
infra/
  terraform/
  bicep/
  kubernetes/
docs/
```

## 7. Reference end-to-end flow

### 7.1 International investor flow

1. User signs up.
2. User completes KYC and profile intake.
3. User searches investment properties.
4. Router triggers property recommendation, ROI, residency/visa, compliance, and insurance experts.
5. Frontend shows:
   - recommended listings,
   - projected returns,
   - residency eligibility hints,
   - risk notes,
   - insurance suggestions.
6. User reserves a property.
7. Payment flow initiates.
8. Document workflow begins.
9. Compliance review happens.
10. Broker, advisor, and admin collaborate in the deal room.

## 8. Delivery phases

### 8.1 MVP

- listings,
- auth,
- search,
- deal workflow,
- payments,
- basic AI recommender,
- KYC/compliance base,
- Azure deployment baseline.

### 8.2 Phase 2

- visa workflow engine,
- insurance integrations,
- valuation expert,
- ROI expert,
- admin/compliance workbench.

### 8.3 Phase 3

- full MoE routing,
- model explainability expansion,
- dynamic UX personalization,
- forecasting,
- broker / insurer / government integrations,
- advanced document intelligence.

## 9. Practical interpretation for the current repository

This repository does **not** yet implement the full Next.js/FastAPI/Azure monorepo. Instead, it now serves as:

- the architecture source of truth,
- the MoE operating model reference,
- the compliance mapping baseline,
- a lightweight orchestration prototype,
- and a visual concept surface for the future premium frontend.

That distinction matters so the repository remains honest about present implementation maturity while staying tightly aligned to the target-state architecture.

# EstateOS Authoritative MoE Platform Blueprint

This document captures the architecture and product framing provided by the user as the **authoritative blueprint** for EstateOS. When documentation, prototypes, or implementation scaffolding diverge, this file should be treated as the source of truth for the intended target state.

## 1. Platform framing

EstateOS should be described as:

- **An AI-native real estate intelligence platform with MoE-driven decision support** for property, migration, insurance, compliance, and finance.
- **A real estate operating system powered by a Mixture-of-Experts AI backbone.**

## 2. Canonical layered architecture

### 2.1 Frontend experience layer

The premium product surface includes:

- Web app using React / Next.js.
- Optional mobile app using React Native or Flutter.
- Admin, broker, and compliance portal.

Core UX modules:

- Property search and maps.
- Investor dashboard.
- Residency / visa journey.
- Insurance journey.
- Payments / escrow UI.
- Documents / eSignature / deal room.
- AI insights, recommendations, and risk explanations.

### 2.2 API gateway / BFF layer

The control plane includes:

- API gateway.
- Backend-for-frontend (BFF).
- Auth gateway.
- Rate limiting, session management, consent, and audit hooks.

### 2.3 Core application services

The canonical services are:

- **Identity service** for user profiles, RBAC, MFA, KYC, consent, and access logs.
- **Listing service** for the property catalog, search, filters, media, and listing moderation.
- **Transaction service** for offers, reservations, deal lifecycle, documents, milestones, and notifications.
- **Visa workflow service** for residency rules, eligibility intake, and document collection.
- **Insurance service** for quotes, referrals, policy mapping, and ACORD mapping.
- **Payment service** for gateway orchestration, ledgering, reconciliation, escrow-style workflows, PCI-aware flows, and fraud hooks.
- **Integration service** for partner APIs and webhooks.
- **Notification service** for email, SMS, and push.
- **Reporting / admin service** for dashboards, operations, and audit reporting.

### 2.4 AI orchestration / MoE layer

The orchestrator must:

- detect user intent, stage, profile, geography, risk, and goals,
- choose one or more experts,
- aggregate, rank, and explain outputs.

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

### 2.5 Data platform layer

The target data platform includes:

- OLTP database using PostgreSQL or Azure SQL.
- Search index using Elasticsearch or Azure AI Search.
- Object storage using Azure Blob Storage.
- Event bus using Azure Service Bus or Event Grid.
- Redis cache.
- Feature store / ML data layer.
- Data warehouse / analytics using Synapse or Fabric as needed.
- Audit logs, SIEM, and monitoring.

### 2.6 Security / compliance / governance layer

The governance baseline includes:

- ISO/IEC 27001, 27017, 27018, and 27701.
- ISO/IEC 25010 and ISO 9241-210.
- ISO/IEC 42001 and ISO/IEC 5259.
- ISO 22301 and ISO 31000.
- PCI DSS and SOC 2 Type 2.
- ACORD and NAIC-aligned insurance workflows.
- KYC / AML / PEP / sanctions / beneficial ownership controls.
- Encryption, secrets management, DLP, access reviews, retention, and incident response.

## 3. Frontend stack

The preferred frontend stack is:

- Next.js + React + TypeScript.
- Tailwind CSS.
- shadcn/ui.
- Mapbox or Google Maps.
- TanStack Query.
- Zustand or Redux Toolkit.
- i18n for multilingual delivery.
- Framer Motion for subtle motion.
- Stripe Elements or payment SDKs where relevant.

Frontend zones:

- Public marketing site.
- Property discovery app.
- Investor workspace.
- Insurance flow.
- Visa / residency intake flow.
- Broker / admin / compliance console.

## 4. Backend stack

The recommended approach is a **modular monolith first**, with a microservice split later if team maturity justifies it.

Recommended backend stack:

- FastAPI (Python) for AI-heavy backend services.
- Node.js / NestJS optionally for API orchestration.
- PostgreSQL.
- Redis.
- Azure Blob Storage.
- Azure Service Bus.
- Elasticsearch or Azure AI Search.
- Keycloak or Azure AD B2C / Entra External ID.
- Temporal or Camunda for workflow orchestration.

Canonical backend modules:

- auth
- users
- listings
- transactions
- documents
- visa-workflows
- insurance
- payments
- compliance
- ai-orchestrator
- integrations
- notifications
- admin/reporting

## 5. MoE expert routing model

The router should decide which experts activate based on:

- user type,
- location,
- property type,
- investment goal,
- residency intent,
- risk score,
- transaction stage.

Example routing patterns:

### 5.1 International investor

User profile:

- international investor,
- intent to buy property in Dubai,
- interest in exploring residency.

Activated experts:

- Property Recommendation Expert,
- Investment ROI Expert,
- Residency / Visa Eligibility Expert,
- Compliance / AML / Sanctions Expert,
- Insurance Recommendation Expert.

### 5.2 First-time renter

User profile:

- first-time renter,
- intent to find an apartment,
- need for renters insurance.

Activated experts:

- Property Recommendation Expert,
- UX Personalization Expert,
- Insurance Recommendation Expert,
- Payment / Fraud / Financial Risk Expert.

## 6. Expert definitions

### 6.1 Property Recommendation Expert

Ranks listings by:

- preferences,
- budget,
- neighborhood fit,
- lifestyle match,
- investor profile.

### 6.2 Property Valuation Expert

Uses:

- comps,
- local market trends,
- historical data,
- supply / demand signals.

### 6.3 Investment ROI Expert

Calculates:

- rental yield,
- appreciation potential,
- cap rate,
- occupancy assumptions,
- downside scenarios.

### 6.4 Residency / Visa Expert

Evaluates:

- country-specific thresholds,
- ownership requirements,
- applicant profile,
- family / dependent suitability,
- document completeness.

### 6.5 Insurance Expert

Recommends:

- homeowners,
- landlord,
- renters,
- title,
- mortgage-protection,
- related life-insurance referral paths where appropriate.

### 6.6 Payment / Fraud Expert

Checks:

- transaction anomalies,
- chargeback risk,
- payment velocity,
- identity / payment mismatch,
- cross-border risk indicators.

### 6.7 Compliance Expert

Handles:

- KYC / AML,
- sanctions,
- PEP,
- beneficial ownership,
- transaction monitoring,
- jurisdictional flags.

### 6.8 UX Personalization Expert

Adapts:

- onboarding path,
- page sequencing,
- prompts,
- educational content,
- CTA timing.

### 6.9 Document Intelligence Expert

Processes:

- uploaded IDs,
- proofs of funds,
- contracts,
- deeds,
- insurance paperwork,
- visa documents.

### 6.10 Market Forecast Expert

Surfaces:

- trend alerts,
- neighborhood outlook,
- pricing heatmaps,
- investment caution flags.

## 7. Recommended Azure deployment

The strong Azure baseline is:

- Azure Front Door.
- Azure App Service or AKS.
- Azure API Management.
- Azure Database for PostgreSQL.
- Azure Cache for Redis.
- Azure Blob Storage.
- Azure Service Bus.
- Azure Key Vault.
- Azure Monitor.
- Microsoft Sentinel.
- Azure AI Search.
- Azure Machine Learning for model hosting and governance.
- Azure DevOps or GitHub Actions.
- Defender for Cloud.

## 8. Suggested repository structure

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
│   ├── visa-service/
│   ├── insurance-service/
│   ├── payment-service/
│   ├── compliance-service/
│   ├── integration-service/
│   ├── notification-service/
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

## 9. Example end-to-end user flow

### 9.1 International investor flow

1. User signs up.
2. Completes KYC and profile.
3. Searches investment properties.
4. Router triggers property, ROI, visa, compliance, and insurance experts.
5. Frontend shows recommended listings, projected returns, residency eligibility hints, risk notes, and insurance suggestions.
6. User reserves a property.
7. Payment flow initiates.
8. Document workflow begins.
9. Compliance review happens.
10. Broker, advisor, and admin collaborate in the deal room.

## 10. Compliance mapping baseline

The architecture should preserve the following mappings:

- ISO 27001 → security management.
- ISO 27017 → cloud controls.
- ISO 27018 → cloud PII protection.
- ISO 27701 → privacy management.
- ISO 25010 → software quality.
- ISO 9241-210 → human-centered UX.
- ISO 22301 → continuity and recovery.
- ISO 31000 → risk management.
- ISO 42001 → AI governance.
- ISO 5259 → AI / data quality.
- PCI DSS → payment security.
- SOC 2 Type 2 → operational trust.
- ACORD → insurance data interoperability.
- NAIC-aligned controls → insurance privacy/security workflows.
- KYC / AML / sanctions / PEP → regulatory controls.
- Country-specific residency rules → visa workflow logic.

## 11. Delivery phases

### 11.1 MVP

- listings,
- auth,
- search,
- deal workflow,
- payments,
- basic AI recommender,
- KYC / compliance base,
- Azure deployment.

### 11.2 Phase 2

- visa workflow engine,
- insurance integrations,
- valuation expert,
- ROI expert,
- admin / compliance workbench.

### 11.3 Phase 3

- full MoE routing,
- model explainability,
- dynamic UX personalization,
- forecasting,
- broker / insurer / government integrations,
- advanced document intelligence.

## 12. Master technical build prompt

Use the following prompt when generating architecture or implementation proposals with another model:

> Design and implement a secure Azure-based real estate platform using a Mixture-of-Experts AI architecture, where a React/Next.js frontend delivers property discovery, investor journeys, residency-by-investment workflows, insurance integrations, payments, and document-driven transaction management, while a modular backend built with Python FastAPI and cloud-native services orchestrates listings, users, deals, compliance, payments, insurance, and AI experts; include specialized experts for property recommendation, valuation, ROI analysis, residency eligibility, insurance recommendation, fraud/payment risk, compliance/AML/sanctions, UX personalization, document intelligence, and market forecasting, all coordinated by an expert router that dynamically selects and combines models based on user context and intent; deploy on Azure using API Management, App Service or AKS, PostgreSQL, Blob Storage, Redis, Service Bus, Key Vault, Azure AI Search, Azure Machine Learning, Monitor, Sentinel, and secure DevSecOps pipelines, while aligning architecture and controls to ISO/IEC 27001, 27017, 27018, 27701, 25010, 42001, 5259, ISO 22301, ISO 31000, PCI DSS, SOC 2 Type 2, ACORD-oriented insurance interoperability, NAIC-aligned insurance privacy/security expectations, and KYC/AML/sanctions/PEP requirements, ensuring the frontend remains elegant and intuitive while the backend enforces security, explainability, auditability, resilience, and multi-domain intelligence across real estate, payments, insurance, and investment migration.

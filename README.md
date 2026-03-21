# EstateOS

EstateOS is an **AI-native real estate operating system powered by a Mixture-of-Experts (MoE) backbone**.

Today, this repository is best understood as a **reverse-engineerable platform blueprint plus working reference implementation**:

- a runnable **FastAPI (Python)** backend scaffold that models the platform's primary domains,
- a static frontend prototype that demonstrates the intended decision workspace and data wiring,
- a large orchestration reference that emits governed demo packets for multiple user journeys, and
- a monorepo skeleton for the eventual production migration into `apps/`, `services/`, `experts/`, `packages/`, and `infra/`.

It is **not yet the final production monorepo**, but it already shows the product shape, routing model, trust controls, and delivery boundaries the platform is converging toward.

## What the platform is trying to be

EstateOS combines several normally separate systems into one operating surface:

- property discovery and recommendation,
- investment and ROI analysis,
- residency / visa workflow support,
- insurance intake and quoting,
- payments and escrow-aware transaction flows,
- document collection and validation,
- compliance, KYC/AML, and risk review,
- explainable AI routing and release governance.

The target production framing is captured in `docs/authoritative-blueprint.md`, `docs/architecture.md`, and `docs/production-platform-blueprint.md`.

## Reverse-engineered current-state architecture

If you read the repo from the code outward, the current platform shape looks like this:

### 1. Product experience layer

The active customer-facing demo lives in `frontend/` as a static HTML/CSS/JS prototype.

It renders a premium-style decision workspace with:

- buyer, investor, and advisor journeys,
- a wiring banner that shows whether backend-generated packets were loaded,
- adaptive controls for objective, risk tolerance, explanation depth, budget, residency, and financing,
- recommendation cards, expert strips, trust context, deal stages, and policy-oriented status panels,
- visual sections for compliance, residency, insurance, payments, integrations, digital twin, market intelligence, tokenization, and marketplace concepts.

This is intentionally **prototype-only**. The intended production home remains `apps/web/` for a **Next.js + React + TypeScript** implementation, with `apps/admin/` reserved for operator workflows and `apps/mobile/` reserved for a future mobile surface.

### 2. API and modular backend layer

The live backend scaffold lives in `backend/app/` and exposes `/api/v1` routes for the platform's first vertical slice:

- auth,
- users,
- listings,
- deals,
- documents,
- residency,
- insurance,
- payments,
- compliance,
- AI assessment.

The scaffold is built as a **modular monolith first** and already encodes the service seams that later map into `services/`.

### 3. Mixture-of-Experts orchestration layer

There are currently **two orchestration artifacts** in the repository:

1. `backend/app/services/ai_orchestrator.py` — a runnable FastAPI-facing MoE router for AI assessment requests.
2. `backend/orchestration.py` — a much larger reference implementation that generates rich decision packets for the frontend demo and future product flows.

Together they show the intended MoE control model:

- detect user intent and journey context,
- select experts based on context and workflow stage,
- aggregate expert outputs into ranked recommendations,
- attach explanations, policy gates, and audit semantics,
- hold or release outcomes depending on trust and review posture.

### 4. Data, async, and audit seams

The current implementation is still lightweight, but it already hints at the production platform seams:

- in-memory persistence for local domain behavior,
- event contract definitions for listings, deals, documents, AI routing, payments, residency, insurance, and compliance,
- deferred task definitions for document extraction, search indexing, workflow jobs, quote fan-out, reconciliation, and screening,
- audit logging via the shared backend service base.

### 5. Governance and deployment layer

The repo consistently preserves an Azure-first target state including:

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
- Azure Monitor and Microsoft Sentinel.

## What actually runs today

## 1. Static frontend prototype

`frontend/` is a browser demo, not a framework app.

It loads `frontend/demo-packets.json` and hydrates three prebuilt journey experiences:

- **buyer**,
- **investor**,
- **advisor**.

Those payloads are generated from the Python orchestration reference and let the UI simulate:

- property recommendation and ranking,
- transaction-stage guidance,
- policy-gated release states,
- payment, insurance, residency, integration, and market-intelligence panels,
- expert marketplace and tokenization concepts.

## 2. FastAPI backend scaffold

The backend is a small but runnable API surface intended to prove the shape of the modular monolith.

### Available route groups

- `POST /api/v1/auth/register`
- `POST /api/v1/auth/login`
- `GET /api/v1/users/me`
- `PUT /api/v1/users/me/preferences`
- `GET /api/v1/listings`
- `POST /api/v1/listings`
- `GET /api/v1/listings/{listing_id}`
- `POST /api/v1/listings/favorites`
- `POST /api/v1/deals`
- `POST /api/v1/deals/{deal_id}/offers`
- `GET /api/v1/deals/{deal_id}`
- `POST /api/v1/documents/presign`
- `POST /api/v1/documents/{document_id}/complete`
- `GET /api/v1/residency/programs`
- `POST /api/v1/residency/applications`
- `POST /api/v1/residency/applications/{application_id}/assess`
- `POST /api/v1/insurance/requests`
- `GET /api/v1/insurance/requests/{request_id}/quotes`
- `POST /api/v1/payments/intents`
- `GET /api/v1/payments/{payment_id}`
- `GET /api/v1/compliance/cases/{case_id}`
- `GET /api/v1/compliance/screening-checks/{check_id}`
- `POST /api/v1/ai/assess`
- `GET /health`

### What those modules currently model

- **Auth** returns demo registration and token responses.
- **Users** exposes a demo authenticated profile and preference updates.
- **Listings** includes seed data, filtering, creation, and favoriting.
- **Deals** models deal creation, offer submission, milestones, and retrieval.
- **Documents** models presign + upload completion flows.
- **Residency** models program discovery, application creation, and preliminary eligibility scoring.
- **Insurance** models quote request submission and quote retrieval.
- **Payments** models payment intent creation and payment retrieval.
- **Compliance** models case retrieval and screening lookup.
- **AI** models explainable expert routing with governance metadata.

## 3. Reference orchestration engine

`backend/orchestration.py` is the richest source for understanding the intended EstateOS platform.

It models packet generation for:

- property decisioning,
- transaction workflows,
- payment and fraud review,
- insurance decisions,
- residency decisions,
- integration routing,
- compliance graph decisions,
- digital twin concepts,
- market intelligence,
- document intelligence,
- marketplace participation,
- tokenization scenarios,
- multi-role copilot behavior.

If you want to "reverse engineer the platform," this file is where the deepest product assumptions currently live.

## Canonical expert model

The repo consistently preserves the ten-expert MoE taxonomy:

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

In the runnable FastAPI scaffold, these experts are represented by small modules that currently output deterministic demo logic. In the broader orchestration reference, the same concepts are expanded into richer decision packets and governance flows.

## Monorepo target structure

The target repository shape the project is steering toward is:

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

- Autonomous Deal Execution Engine (Agentic AI Layer).
- Digital Twin Properties & Simulation Engine.
- Predictive Market Intelligence & Macro AI.
- Conversational AI Copilot (Multi-Role Assistant).
- On-Chain / Tokenization & Fractional Ownership Layer.
- Advanced Document Intelligence & Legal Reasoning AI.
- Global Compliance Graph & Regulatory Intelligence System.
- Hyper-Personalization & Behavioral Modeling Engine.
- Trust, Reputation, and Risk Scoring Network.
- Open AI Marketplace & Third-Party Expert Plug-in Ecosystem.

## Repo tour

- `frontend/` — static prototype for the decision workspace.
- `backend/` — runnable FastAPI scaffold plus orchestration reference.
- `docs/` — architecture, roadmap, compliance, and alignment documentation.
- `apps/` — reserved production app roots.
- `services/` — canonical future backend service boundaries.
- `experts/` — canonical future expert ownership boundaries.
- `packages/` — shared UI, types, config, and utilities.
- `infra/` — Azure-focused infrastructure roots.
- `scripts/` — lightweight validation and export helpers.

## Quick start

### Run the backend scaffold

```bash
cd backend
uvicorn app.main:app --reload
```

Then open:

- API docs: `http://127.0.0.1:8000/api/v1/docs`
- Health check: `http://127.0.0.1:8000/health`

### Run the orchestration reference directly

```bash
python3 backend/orchestration.py
```

### Regenerate demo packets

```bash
python3 scripts/export_demo_payloads.py
```

### Serve the static frontend prototype

Any static file server will work. For example:

```bash
python3 -m http.server 8080 --directory frontend
```

Then open `http://127.0.0.1:8080`.

## Validation commands

Run the repository-level architecture alignment check:

```bash
python3 scripts/check_architecture_alignment.py
```

Run the frontend wiring smoke test:

```bash
python3 scripts/check_frontend_wiring.py
```

## Recommended reading order

If you're trying to understand the platform quickly, read these in order:

1. `README.md`
2. `docs/current-state-alignment-audit.md`
3. `docs/authoritative-blueprint.md`
4. `docs/production-platform-blueprint.md`
5. `docs/moe-platform-model.md`
6. `docs/blueprint-traceability-matrix.md`
7. `backend/app/services/ai_orchestrator.py`
8. `backend/orchestration.py`

## Current-state caveat

The safest description of EstateOS today is:

> a governed scaffold and reference implementation for an AI-native real estate operating system, not yet the completed production platform.

That distinction matters. The repo already preserves the target stack, service seams, expert taxonomy, Azure baseline, and compliance posture, but much of the production-grade implementation is still ahead.

For the most explicit statement of that status, see `docs/current-state-alignment-audit.md` and `docs/blueprint-traceability-matrix.md`.

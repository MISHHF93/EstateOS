# Backend scaffold

This directory contains a **production-grade FastAPI modular-monolith scaffold** for EstateOS: an AI-native real estate operating system that unifies property discovery, investment analysis, residency-by-investment workflows, insurance, payments, compliance, notifications, integrations, and transaction execution behind one governed API surface.

## Project structure

```text
backend/
├── app/
│   ├── api/
│   │   ├── router.py                # Versioned API composition
│   │   └── v1/                      # OpenAPI-ready routers per bounded context
│   ├── core/                        # Settings, security, logging, infrastructure registry
│   ├── events/                      # Event contracts for Azure Service Bus-style packets
│   ├── experts/                     # Mixture-of-Experts domain specialists
│   ├── models/                      # Domain entities + SQLAlchemy ORM baseline
│   ├── repositories/                # Repository seams (demo in-memory adapter included)
│   ├── schemas/                     # Pydantic API contracts
│   ├── services/                    # Application and orchestration services
│   └── workers/                     # Background job/task catalog
├── pyproject.toml                   # Python package + FastAPI dependencies
└── README.md
```

## Bounded contexts included

- authentication, session bootstrap, and RBAC guardrails
- user profiles and preference management
- property listings and hybrid search
- deals, offers, and transaction workflow orchestration
- document intake and Azure Blob-compatible upload seams
- residency-by-investment programs and eligibility workflows
- insurance quote orchestration with ACORD-oriented payload assumptions
- payments, escrow ledgering, and reconciliation hooks
- compliance, KYC, AML, sanctions, PEP, and beneficial-ownership controls
- notifications and third-party integration management
- AI orchestration that routes requests across property recommendation, valuation, ROI, residency eligibility, insurance matching, fraud detection, compliance scoring, document intelligence, personalization, and market forecasting experts

## Production-target architecture notes

The scaffold encodes the following implementation expectations:

- **Azure-native deployment** via API Management, App Service or AKS, PostgreSQL, Redis, Blob Storage, Service Bus, Key Vault, Azure AI Search, Azure OpenAI, and Azure AI Document Intelligence.
- **Governed MoE routing** with expert selection, audit events, explainability packets, policy gates, and human-review conditions.
- **Security and privacy controls** oriented around strong identity, least privilege, RBAC, audit logging, immutable ledgering, managed identities, and protected handling of PII and payment artifacts.
- **Operational resilience** aligned with ISO 22301 and ISO 31000 through asynchronous task seams, event contracts, integration catalogs, and readiness introspection endpoints.
- **Compliance alignment** with ISO/IEC 27001, 27017, 27018, 27701, ISO/IEC 42001, ISO/IEC 5259, PCI DSS, SOC 2 Type 2, ACORD interoperability, and KYC/AML/sanctions obligations.

## Suggested next implementation steps

1. Replace the demo repository with SQLAlchemy async repositories and Alembic migrations.
2. Wire Azure SDK clients for Blob Storage, Service Bus, Key Vault, Azure AI Search, and Azure OpenAI.
3. Add Celery/Dramatiq/Arq workers or Azure Functions consumers for the background task catalog.
4. Connect external KYC/AML and insurance carriers behind the integration service and event contracts.
5. Attach real authentication (OIDC/Entra ID or Auth0) and policy enforcement middleware.

## Run locally

```bash
cd backend
uvicorn app.main:app --reload
```

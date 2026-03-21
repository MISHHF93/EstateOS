# Backend scaffold

This directory contains a **developer-grade FastAPI modular-monolith scaffold** for the EstateOS production target state: an AI-native real estate platform that unifies property discovery, investment analysis, residency-by-investment workflows, insurance, payments, compliance, and transaction operations behind one governed API surface.

## Structure

- `app/main.py` bootstraps the API and mounts `/api/v1` routes.
- `app/api/v1/` contains thin route handlers for auth, users, listings, deals, documents, residency, insurance, payments, compliance, and AI assessments.
- `app/services/` keeps orchestration and domain logic out of the routers.
- `app/models/` and `app/schemas/` separate internal entities from API contracts.
- `app/experts/` provides starter MoE expert modules for recommendation, valuation, ROI, residency, insurance, fraud, compliance, document intelligence, personalization, and market forecasting.
- `app/events/` and `app/workers/` establish the Service Bus-style async/event seams.

## Initial vertical slice

The scaffold covers the first delivery slice requested in the architecture blueprint:

- register/login
- profile retrieval and preference updates
- create and browse listings
- favorite a listing
- create deals and offers
- presign and complete document uploads
- create payment intents
- request residency assessment
- request insurance quotes
- retrieve compliance cases and screening checks
- run an explainable AI assessment through the MoE orchestrator

## Production-target architecture notes

The current scaffold encodes the following production-grade expectations even though it is still a reference implementation:

- **Azure-native deployment** via API Management, App Service or AKS, PostgreSQL, Redis, Blob Storage, Service Bus, Key Vault, Azure AI Search, and Azure Machine Learning.
- **Modular service boundaries** for authentication, profiles, listings, search, deals, documents, residency, insurance, payments, compliance, notifications, integrations, and AI orchestration.
- **Governed MoE routing** with audit events, policy gates, human-review conditions, and explainable expert packets.
- **Event-driven lifecycle hooks** for listings, documents, AI routing, residency assessments, insurance quote fan-out, payments, and compliance escalations.
- **Enterprise controls** aligned to ISO/IEC 27001, ISO/IEC 27701, ISO/IEC 42001, ISO/IEC 5259, PCI DSS, SOC 2 Type 2, ACORD-oriented data exchange, and KYC/AML/sanctions/beneficial ownership obligations.

## Run locally

```bash
cd backend
uvicorn app.main:app --reload
```

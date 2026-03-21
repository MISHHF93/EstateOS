# Backend scaffold

This directory now contains a developer-grade FastAPI scaffold for the EstateOS modular monolith target state.

## Structure

- `app/main.py` bootstraps the API and mounts `/api/v1` routes.
- `app/api/v1/` contains thin route handlers per domain.
- `app/services/` keeps business logic out of the routers.
- `app/models/` and `app/schemas/` separate internal entities from API contracts.
- `app/experts/` provides starter MoE expert modules for the orchestrator.
- `app/events/` and `app/workers/` establish the async/event contract seams.

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
- run an AI assessment through the MoE orchestrator

## Run locally

```bash
cd backend
uvicorn app.main:app --reload
```

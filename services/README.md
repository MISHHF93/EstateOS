# Services

This directory defines the canonical backend module and service boundaries for EstateOS.

The implementation strategy remains **modular monolith first**, with a future option to extract these modules into independently deployable services when scale and team maturity justify it.

## Canonical service map

- `auth-service/`
- `user-service/`
- `listing-service/`
- `transaction-service/`
- `document-service/`
- `visa-service/`
- `insurance-service/`
- `payment-service/`
- `compliance-service/`
- `integration-service/`
- `notification-service/`
- `admin-reporting-service/`
- `ai-orchestrator/`

These service roots reflect the target architecture across identity, listings, deal execution, documents, residency workflows, insurance, payments, compliance, notifications, reporting, and AI routing.

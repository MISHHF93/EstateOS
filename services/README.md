# Services

This directory defines the canonical backend module and service boundaries for EstateOS.

The implementation strategy remains **modular monolith first**, with a future option to extract these modules into independently deployable services when scale, compliance isolation, or team maturity justify it.

## Canonical service map

- `auth-service/` → identity, RBAC, MFA, KYC, consent, and access logs.
- `user-service/` → user profiles, household/investor context, and personalization inputs.
- `listing-service/` → property catalog, search, filters, media, and listing moderation.
- `transaction-service/` → offers, reservations, deal lifecycle, milestones, and transaction notifications.
- `document-service/` → document ingestion, storage coordination, validation, eSignature, and deal-room evidence.
- `visa-service/` → residency rules, eligibility intake, and document collection.
- `insurance-service/` → quotes, referrals, policy mapping, and ACORD-aligned exchange.
- `payment-service/` → gateway orchestration, ledgering, reconciliation, escrow-style workflows, PCI-aware flows, and fraud hooks.
- `compliance-service/` → KYC/AML, sanctions, PEP, beneficial ownership, and jurisdictional review workflows.
- `integration-service/` → partner APIs, webhook handling, and external-system adapters.
- `notification-service/` → email, SMS, push, and transactional messaging.
- `admin-reporting-service/` → dashboards, operational reporting, audit views, and workbench capabilities.
- `ai-orchestrator/` → intent detection, expert routing, aggregation, explainability, and policy gating.

## Operating rule

These service roots reflect the target architecture across identity, listings, deal execution, documents, residency workflows, insurance, payments, compliance, notifications, reporting, and AI routing.

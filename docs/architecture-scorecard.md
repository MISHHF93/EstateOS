# EstateOS Architecture Alignment Scorecard

## 1. Purpose

This scorecard turns the authoritative MoE real estate platform blueprint into a practical repo-level compliance check. Use it to confirm whether EstateOS still conforms to the requested platform shape, stack decisions, operating model, and governance posture.

Unlike the broader narrative docs, this file is meant to answer a narrower question:

**Does the repository currently preserve the intended architecture direction without silent drift?**

## 2. Current verdict

**Verdict:** Yes, at the repository-governance level.

More precisely: EstateOS currently abides by the requested architecture as a **governed scaffold and reference implementation**, not as a fully delivered production system. See `docs/current-state-alignment-audit.md` for the current-state nuance and explicit boundary between what is already aligned versus what remains roadmap or scaffold.

EstateOS currently abides by the requested architecture as a **blueprint and scaffolding repository** rather than as a fully implemented production platform. The repo now preserves the requested direction in four ways:

1. the user-provided architecture is captured as the source of truth in `docs/authoritative-blueprint.md`,
2. the target-state architecture is decomposed into implementation rules in `docs/architecture.md`, `docs/platform-manifest.md`, and `docs/blueprint-alignment.md`,
3. the canonical monorepo roots exist under `apps/`, `services/`, `experts/`, `packages/`, and `infra/`, and
4. each major delivery area now has an explicit repository home so future work can land without architecture drift.

## 3. Layer-by-layer scorecard

| Layer | Target requirement | Current repo status | Alignment verdict | Next enforcement action |
| --- | --- | --- | --- | --- |
| Frontend experience | Next.js/React/TypeScript product surface covering marketing, discovery, investor workspace, visa, insurance, payments, documents, and AI insights. | `apps/web/`, `apps/admin/`, and `apps/mobile/` are reserved with explicit scope docs; legacy `frontend/` is treated as prototype-only. | **Aligned as scaffold** | Start all new production UI in `apps/`, not `frontend/`. |
| API gateway / BFF | API gateway, auth gateway, BFF, session, consent, rate limiting, and audit hooks. | Architecture and manifest docs define these as mandatory control-plane responsibilities; shared-contract locations are reserved in `packages/`. | **Aligned as architectural rule** | Capture actual BFF/auth/session contracts under `packages/types/` and `packages/config/` when implementation begins. |
| Core application services | Canonical modules for auth, users, listings, transactions, documents, visa, insurance, payments, compliance, integrations, notifications, admin/reporting, and AI orchestration. | The full service directory map exists under `services/`, with role-specific README files documenting ownership boundaries. | **Aligned as scaffold** | Keep production backend work inside these service roots and preserve modular-monolith-first boundaries. |
| AI orchestration / MoE | Intent-aware router selects, aggregates, ranks, explains, and governs outputs from the ten canonical experts. | `services/ai-orchestrator/` defines the orchestration home; `experts/` defines the canonical ten-expert taxonomy and routing dimensions. | **Aligned as scaffold** | Move production routing logic into `services/ai-orchestrator/` and treat `backend/orchestration.py` as reference-only. |
| Data platform | PostgreSQL, Redis, Blob Storage, Service Bus, search, analytics, feature/data layers, and audit evidence. | The data platform is documented as the baseline; `infra/` and `packages/` reserve the infra and contract locations needed to implement it. | **Aligned as planning baseline** | Materialize infra definitions and typed data contracts before service implementation expands. |
| Security / compliance / governance | ISO, PCI DSS, SOC 2, ACORD/NAIC, KYC/AML/sanctions/PEP, privacy, auditability, resilience, and AI governance. | `docs/compliance-mapping.md` and the manifest/alignment docs make compliance part of the architecture instead of an afterthought. | **Aligned as governance baseline** | Require trust, privacy, audit, and release notes in future feature proposals and service designs. |

## 4. Stack-decision scorecard

| Domain | Locked decision | Current repo preservation | Alignment verdict |
| --- | --- | --- | --- |
| Web frontend | Next.js + React + TypeScript | `apps/web/README.md` marks this as the canonical implementation stack. | **Aligned** |
| UI styling/system | Tailwind CSS + shadcn/ui + Framer Motion | Documented in app- and repo-level architecture guidance. | **Aligned** |
| State/data | TanStack Query + Zustand or Redux Toolkit + i18n | Documented as the expected frontend baseline. | **Aligned** |
| Maps/payments | Mapbox or Google Maps; Stripe Elements/payment SDKs | Documented in the blueprint and frontend guidance. | **Aligned** |
| AI-heavy backend | FastAPI (Python) first | Root architecture docs and service layout preserve FastAPI-first direction. | **Aligned** |
| Orchestration option | Node.js / NestJS optional for API orchestration | Documented as optional rather than default, preventing backend drift. | **Aligned** |
| Persistence/search/events | PostgreSQL, Redis, Blob Storage, Service Bus, AI Search/Elasticsearch | Documented in architecture and compliance mapping; infra roots reserved. | **Aligned** |
| Identity/workflows | Keycloak or Entra External ID; Temporal or Camunda | Explicitly documented in the blueprint and roadmap. | **Aligned** |

## 5. Service-boundary scorecard

| Service root | Expected ownership |
| --- | --- |
| `services/auth-service/` | identity, RBAC, MFA, KYC, consent, access logs |
| `services/user-service/` | profiles, household/investor context, personalization inputs |
| `services/listing-service/` | property catalog, search, filters, media, moderation |
| `services/transaction-service/` | offers, reservations, milestones, lifecycle orchestration |
| `services/document-service/` | ingestion, validation, eSignature, deal-room evidence |
| `services/visa-service/` | residency rules, eligibility intake, document collection |
| `services/insurance-service/` | quotes, referrals, policy mapping, ACORD-oriented exchange |
| `services/payment-service/` | gateway orchestration, ledgers, reconciliation, escrow, PCI-aware flows, fraud hooks |
| `services/compliance-service/` | KYC/AML, sanctions, PEP, beneficial ownership, transaction monitoring |
| `services/integration-service/` | partner APIs, webhooks, adapters |
| `services/notification-service/` | email, SMS, push, transactional messaging |
| `services/admin-reporting-service/` | dashboards, operations, audit, workbench flows |
| `services/ai-orchestrator/` | intent detection, routing, ranking, explainability, policy gating |

**Rule:** new production-oriented backend work should strengthen these boundaries, not collapse them into feature-specific folders that bypass the target architecture.

## 6. Expert-taxonomy scorecard

The repository remains aligned only if the MoE layer continues using the canonical ten experts:

1. Property Recommendation Expert
2. Property Valuation Expert
3. Investment ROI Expert
4. Residency / Visa Eligibility Expert
5. Insurance Recommendation Expert
6. Payment / Fraud / Financial Risk Expert
7. Compliance / AML / Sanctions Expert
8. UX Personalization Expert
9. Document Intelligence Expert
10. Market Forecast / Trend Expert

**Rule:** future implementations can add helper models or internal sub-specialists, but they should still roll up to this user-facing taxonomy unless an explicit architecture decision replaces it.

## 7. Delivery-phase scorecard

| Phase | Must remain in scope |
| --- | --- |
| MVP | listings, auth, search, deal workflow, payments, basic AI recommender, base KYC/compliance, Azure baseline |
| Phase 2 | visa workflow engine, insurance integrations, valuation expert, ROI expert, admin/compliance workbench |
| Phase 3 | full MoE routing, explainability expansion, dynamic UX personalization, forecasting, external partner/government integrations, advanced document intelligence |

**Rule:** roadmap discussions should not present Phase 2 or Phase 3 capabilities as already delivered unless code and operational evidence exist for them.

## 8. Contributor acceptance checklist

A change should be considered architecture-aligned only if the answer to each question is **yes**:

1. Does it reinforce the framing of EstateOS as an AI-native real estate operating system with an MoE backbone?
2. Does new production UI land under `apps/` instead of the legacy `frontend/` prototype?
3. Does new production backend work land under `services/` instead of only under `backend/`?
4. Does it preserve the modular-monolith-first implementation model?
5. Does it respect the ten-expert taxonomy and the router's responsibility for aggregation, explanation, and policy gating?
6. Does it keep Azure as the default deployment target unless there is an explicit architecture decision to change that?
7. Does it identify trust, privacy, audit, resilience, and compliance implications?
8. Does it avoid stack drift away from Next.js/React/TypeScript on the frontend and FastAPI-first on the AI-heavy backend?
9. Does it preserve a clear home for cross-cutting types, config, UI primitives, or shared utilities in `packages/`?
10. Does it avoid overstating current implementation maturity relative to the roadmap phase actually delivered?

## 9. Working interpretation

EstateOS is now aligned to the requested architecture in a **governed, implementation-ready form**:

- the blueprint is locked,
- the repository shape matches the requested platform decomposition,
- the stack decisions are preserved,
- the MoE expert taxonomy is preserved,
- the Azure/security/compliance direction is preserved,
- and future contributors have explicit guardrails to prevent architecture drift.

That means the repository can honestly claim alignment with the requested platform architecture today, while still acknowledging that many capabilities remain in scaffold or roadmap form rather than production form.

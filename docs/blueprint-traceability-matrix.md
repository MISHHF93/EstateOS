# EstateOS Blueprint Traceability Matrix

## 1. Purpose

This matrix translates the authoritative MoE real estate platform blueprint into a section-by-section repo audit.

Use it to answer a very specific question:

**Does the current EstateOS repository preserve every major requirement from the requested target architecture?**

## 2. Traceability verdict

**Verdict:** Yes, at the **blueprint, scaffolding, reference-implementation, and repository-governance** level.

That verdict does **not** mean the entire production platform is already shipped or that this is **not yet the final fully implemented production platform**. It means the current repository preserves the requested direction through:

- locked source-of-truth documentation,
- canonical repo decomposition,
- expert and service scaffolding,
- API/orchestration reference artifacts, and
- explicit compliance and Azure deployment guardrails.

## 3. Requirement-by-requirement traceability

| Requested area | Required by blueprint | Current repo evidence | Current status |
| --- | --- | --- | --- |
| Product framing | AI-native real estate intelligence platform and real estate operating system with a Mixture-of-Experts backbone. | `README.md`, `docs/authoritative-blueprint.md`, `docs/architecture.md`, and `docs/platform-manifest.md` all use the same framing. | **Aligned** |
| Frontend experience layer | Web app, optional mobile app, and admin / broker / compliance portal. | `apps/web/`, `apps/mobile/`, and `apps/admin/` exist and are documented as the canonical homes for those surfaces. | **Aligned as scaffold** |
| Frontend zones | Public marketing site, property discovery app, investor workspace, insurance flow, visa/residency intake flow, broker/admin/compliance console. | `apps/web/README.md`, `apps/admin/README.md`, and repo-level docs preserve these zones as required scope. | **Aligned as scaffold** |
| Frontend stack | Next.js + React + TypeScript, Tailwind CSS, shadcn/ui, TanStack Query, Zustand/Redux Toolkit, i18n, Framer Motion, Mapbox/Google Maps, Stripe Elements/payment SDKs. | Locked in `README.md`, `docs/architecture.md`, `docs/authoritative-blueprint.md`, `docs/blueprint-alignment.md`, and `apps/web/README.md`. | **Aligned as stack contract** |
| API gateway / BFF layer | API gateway, backend-for-frontend, auth gateway, rate limiting, session, consent, and audit hooks. | Captured in `docs/architecture.md`, `docs/authoritative-blueprint.md`, `docs/platform-manifest.md`, and reflected in `backend/api_contract.json`. | **Aligned as architectural rule** |
| Core application services | auth, users, listings, transactions, documents, visa-workflows, insurance, payments, compliance, ai-orchestrator, integrations, notifications, admin/reporting. | All canonical service roots exist under `services/` with dedicated README ownership boundaries. | **Aligned as scaffold** |
| AI orchestration layer | Router detects intent/stage/profile/geography/risk/goals, selects experts, aggregates, ranks, and explains results. | Preserved in `services/ai-orchestrator/README.md`, `docs/moe-platform-model.md`, and the Python reference implementation in `backend/orchestration.py`. | **Aligned as reference + scaffold** |
| Expert taxonomy | Ten canonical experts: property recommendation, valuation, ROI, visa, insurance, fraud/payment risk, compliance, UX personalization, document intelligence, market forecast. | All ten expert roots exist under `experts/`, and the taxonomy is repeated in the root docs and scorecard. | **Aligned** |
| Router activation inputs | user type, location, property type, investment goal, residency intent, risk score, transaction stage. | Preserved in `experts/README.md`, `docs/moe-platform-model.md`, and `docs/authoritative-blueprint.md`. | **Aligned** |
| Example routing patterns | International investor and first-time renter routing examples. | Preserved in `docs/authoritative-blueprint.md` and `docs/moe-platform-model.md`. | **Aligned** |
| Data platform layer | PostgreSQL/Azure SQL, Azure AI Search/Elasticsearch, Blob Storage, Service Bus/Event Grid, Redis, feature/ML data layer, analytics, audit logs/SIEM/monitoring. | Captured across `README.md`, `docs/architecture.md`, `docs/authoritative-blueprint.md`, `docs/platform-manifest.md`, `docs/compliance-mapping.md`, and `backend/api_contract.json`. | **Aligned as platform baseline** |
| Security / governance layer | ISO 27001, 27017, 27018, 27701, 25010, 9241-210, 22301, 31000, 42001, 5259, PCI DSS, SOC 2 Type 2, ACORD, NAIC, KYC/AML/PEP/sanctions/beneficial ownership, encryption/secrets/DLP/access review/retention/IR. | Mapped in `docs/compliance-mapping.md` and reinforced in the README, blueprint, platform manifest, and current-state audit. | **Aligned as governance baseline** |
| Azure deployment | Front Door, App Service or AKS, API Management, PostgreSQL, Redis, Blob Storage, Service Bus, Key Vault, Monitor, Sentinel, AI Search, Azure Machine Learning, CI/CD, Defender for Cloud. | Preserved in `README.md`, `docs/architecture.md`, `docs/authoritative-blueprint.md`, `docs/platform-manifest.md`, `infra/README.md`, and `backend/api_contract.json`. | **Aligned as deployment baseline** |
| Suggested repo structure | `apps/`, `services/`, `experts/`, `packages/`, `infra/`, `docs/`. | Implemented directly in the current repo layout. | **Aligned** |
| Example end-to-end flow | International investor flow spanning signup, KYC, search, expert routing, payments, documents, compliance, and deal room collaboration. | Preserved in `docs/architecture.md` and `docs/authoritative-blueprint.md`; orchestration reference includes KYC, payment risk, documents, compliance, and governance controls. | **Aligned as reference flow** |
| Phase 3 ecosystem extensibility | Open marketplace for third-party experts should expand backend intelligence and frontend capabilities without bypassing governance. | Represented in `docs/open-ai-marketplace-expert-plugin-ecosystem.md`, the API contract, the orchestration reference packet, and the frontend marketplace section. | **Aligned as governed blueprint extension** |
| Phase model | MVP, Phase 2, and Phase 3 capability partitioning. | Preserved in `README.md`, `docs/authoritative-blueprint.md`, `docs/architecture.md`, `docs/platform-manifest.md`, and `docs/implementation-roadmap.md`. | **Aligned** |

## 4. Important implementation nuance

The repo currently abides to the blueprint in a **truthful, constrained sense**:

- it is already aligned as a governed architecture repository,
- it is already aligned as a canonical monorepo scaffold,
- it is already aligned as an MoE router reference implementation,
- but it is **not yet** the final fully implemented production platform.

The most important current limitations are:

1. `frontend/` is still a prototype and not yet the production Next.js app.
2. `services/` mostly preserves ownership boundaries and target placement rather than complete runnable services.
3. The BFF/API gateway layer is defined contractually and architecturally, but is not yet fully materialized as production code.
4. Phase 2 and Phase 3 capabilities are preserved as explicit future scope, not falsely claimed as complete.

## 5. Ongoing enforcement rule

A future change should be treated as non-compliant if it does any of the following:

- introduces production UI outside `apps/`,
- introduces production backend features outside `services/` without justification,
- changes the expert taxonomy without an architecture decision,
- drifts from the Azure baseline without explicit approval,
- weakens trust, consent, audit, compliance, or explainability posture,
- overstates roadmap maturity relative to what is actually implemented.

## 6. How to re-check alignment

Run:

```bash
python3 scripts/check_architecture_alignment.py
```

This validator now checks the repo not only for the canonical folder layout and source-of-truth docs, but also for the new traceability matrix that ties the requested blueprint sections to concrete repository evidence.

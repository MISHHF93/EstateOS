# Packages

Shared contracts, schemas, UI primitives, configuration, and platform utilities should live here as the repository transitions toward its target monorepo structure.

## Package map

- `ui/` → shared shadcn/ui-aligned design primitives for `apps/web/` and `apps/admin/`.
- `types/` → cross-cutting schemas for users, listings, transactions, payments, compliance, routing, and explanations.
- `config/` → typed configuration, policy defaults, feature flags, and deployment-time contracts.
- `shared-utils/` → reusable utilities that support apps/services without redefining domain ownership.


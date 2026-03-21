# Web App Surface

`apps/web/` now contains a production-oriented **Next.js App Router + React + TypeScript + Tailwind CSS** scaffold for the EstateOS customer-facing platform.

## Included foundations

- marketing pages for discovery, investors, residency, and insurance,
- authentication and onboarding entry points,
- role-aware dashboards and workspace navigation,
- listing discovery and listing detail pages,
- favorites and saved searches,
- investor analytics,
- deal room, document, residency, insurance, payment, notification, and AI workspace routes,
- admin / compliance operator portal scaffolding,
- reusable UI primitives and layout components,
- TanStack Query provider, Zustand session store, and API integration helpers,
- multilingual readiness and secure middleware-based session gating.

## Intended next steps

1. Generate typed clients from backend OpenAPI specs.
2. Replace mock data in `lib/mocks/` with service-backed loaders.
3. Add authentication/session infrastructure and form validation.
4. Expand design tokens, component primitives, and test coverage.

# Web App Surface

`apps/web/` is the canonical home for the future **Next.js + React + TypeScript** customer-facing application.

## Scope

This surface should eventually include:

- public marketing pages,
- property discovery and maps,
- investor workspace,
- residency / visa intake,
- insurance flows,
- payments / escrow UI,
- documents / eSignature / deal-room workflows,
- AI insights, recommendations, and risk explanations.

## Locked stack guidance

When production-grade work begins here, prefer:

- Next.js App Router,
- TypeScript,
- Tailwind CSS,
- shadcn/ui,
- TanStack Query,
- Zustand or Redux Toolkit,
- i18n,
- Framer Motion,
- Mapbox or Google Maps,
- Stripe Elements or equivalent payment SDKs where required.

## Transition rule

The legacy `frontend/` directory remains a prototype reference. New production-oriented web implementation work should land here instead.

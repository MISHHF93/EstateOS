# Web App Surface

`apps/web/` is the canonical home for the **production Next.js + React + TypeScript** customer-facing application.

## Product modules

The web surface should deliver an elegant, responsive, human-centered experience across:

- public marketing pages,
- property discovery and maps,
- investor workspace,
- residency / visa intake,
- insurance flows,
- payments / escrow UI,
- documents / eSignature / deal-room workflows,
- explainable AI insights, recommendations, and risk explanations.

## UX implementation contract

Production-grade work here should preserve:

- adaptive property discovery for buyers and investors,
- AI-generated but explainable property, ROI, residency, insurance, and risk insights,
- transaction management that keeps approvals, documents, and payment milestones visible,
- accessibility-conscious and multilingual-ready interaction patterns,
- mobile-responsive layouts that do not sacrifice operational clarity.

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

## Integration expectations

The web application should consume governed APIs for:

- authentication and profile management,
- listings and search,
- deals and documents,
- residency and insurance workflows,
- payments,
- explainable AI assessments.

## Transition rule

The legacy `frontend/` directory remains a prototype reference. New production-oriented web implementation work should land here instead.

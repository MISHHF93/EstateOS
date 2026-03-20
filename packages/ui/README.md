# Shared UI

`packages/ui/` is reserved for reusable design primitives shared across EstateOS product surfaces.

## Expected contents

This package should eventually include:

- shadcn/ui-aligned components,
- shared layout primitives,
- trust and status indicators,
- workflow stepper components,
- explainability and risk-disclosure patterns,
- typography, spacing, and theme contracts.

## Architecture rule

Reusable UI primitives should live here when they need to be shared across `apps/web/` and `apps/admin/` without duplicating behavior or accessibility fixes.

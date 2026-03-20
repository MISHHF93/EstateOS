# Shared Utilities

`packages/shared-utils/` is reserved for implementation helpers that are shared across multiple apps or services but do not belong in domain contracts.

## Expected contents

This package should eventually include helpers for:

- formatting and localization support,
- correlation IDs and trace propagation,
- retry/idempotency helpers,
- audit-packet assembly helpers,
- policy-evaluation utilities,
- safe date, money, and unit normalization.

## Architecture rule

Only place utilities here when they are genuinely cross-cutting and stable enough to be reused without creating hidden domain coupling.

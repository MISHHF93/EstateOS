# Admin / Broker / Compliance Console

`apps/admin/` is reserved for the operational control surface used by brokers, administrators, compliance reviewers, and support teams.

## Expected capabilities

This application should evolve to include:

- compliance case review,
- KYC / AML / sanctions oversight,
- transaction and document operations,
- payment / escrow monitoring,
- notifications and intervention workflows,
- reporting, dashboards, and audit views,
- explainability and release-gating visibility for AI-assisted decisions.

## Architecture rule

This console should share contracts and design primitives with `apps/web/`, while applying stricter RBAC, approval, and audit controls.

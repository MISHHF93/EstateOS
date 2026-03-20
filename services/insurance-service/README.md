# Insurance Service

`services/insurance-service/` owns EstateOS insurance referral, recommendation, and policy-mapping workflows.

## Responsibilities

This service boundary should eventually own:

- quote/referral initiation,
- coverage recommendation context,
- property and peril mapping,
- ACORD-oriented payload transformations,
- carrier/broker integration handoffs,
- evidence capture for quote assumptions and exclusions.

## Architecture rules

- Preserve NAIC-aligned privacy and data-sharing controls.
- Keep insurer interoperability contracts explicit and versioned.
- Avoid embedding carrier-specific logic directly in product surfaces.

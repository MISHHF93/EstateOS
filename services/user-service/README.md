# User Service

`services/user-service/` owns persistent user, household, advisor, and investor profile context for EstateOS.

## Responsibilities

This service boundary should eventually own:

- user profiles,
- investor and residency-intent context,
- household and dependent metadata,
- saved preferences and onboarding state,
- personalization inputs shared with the MoE router,
- profile-level data retention and privacy-state handling.

## Architecture rules

- Treat profile state as a shared platform asset, not a feature-local store.
- Publish stable profile contracts for discovery, transactions, insurance, visa, and AI routing flows.
- Preserve consent-aware access and data-minimization requirements for all downstream consumers.

# Visa Workflow Service

`services/visa-service/` is the canonical home for residency-by-investment and visa-intake workflows.

## Responsibilities

This service boundary should eventually own:

- jurisdiction-specific residency rules,
- applicant eligibility intake,
- dependent/family suitability context,
- document collection checkpoints,
- legal-content version references,
- escalation hooks for manual or legal review.

## Architecture rules

- Keep legal/rule content versioned and traceable.
- Treat outputs as eligibility guidance unless a human/legal approval flow explicitly finalizes them.
- Preserve strong links to profile, compliance, and document evidence.

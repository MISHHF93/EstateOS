# Compliance Service

`services/compliance-service/` owns regulated trust and financial-crime controls across EstateOS workflows.

## Responsibilities

This service boundary should eventually own:

- KYC verification status,
- AML review logic and case escalation,
- sanctions and PEP screening,
- beneficial ownership checks,
- jurisdictional risk flags,
- transaction monitoring and hold/release decisions.

## Architecture rules

- Treat compliance as a cross-platform control plane, not a single-feature add-on.
- Preserve audit evidence, reviewer actions, and policy outcomes for every escalated or blocked case.
- Integrate with auth, payments, visa, insurance, and AI release gating.

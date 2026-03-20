# Experts

This directory contains the canonical Mixture-of-Experts taxonomy for EstateOS.

## Routing dimensions

The orchestrator should decide which experts activate based on:

- user type,
- location,
- property type,
- investment goal,
- residency intent,
- risk score,
- transaction stage.

## Canonical expert map

1. `property-recommender/` → ranks listings using preferences, budget, neighborhood fit, lifestyle fit, and investor profile.
2. `valuation-expert/` → evaluates comps, historical signals, and supply/demand context for price intelligence.
3. `roi-expert/` → models rental yield, appreciation potential, cap rate, occupancy assumptions, and downside scenarios.
4. `visa-expert/` → evaluates country-specific residency thresholds, ownership requirements, profile fit, and document completeness.
5. `insurance-expert/` → recommends homeowners, landlord, renters, title, mortgage-protection, and related referral paths.
6. `fraud-expert/` → analyzes payment anomalies, chargeback risk, payment velocity, identity mismatch, and cross-border risk indicators.
7. `compliance-expert/` → handles KYC, AML, sanctions, PEP, beneficial ownership, and transaction monitoring flags.
8. `ux-expert/` → adapts onboarding, sequencing, education, CTA timing, and contextual prompts.
9. `document-expert/` → processes uploaded IDs, proof-of-funds artifacts, contracts, deeds, insurance paperwork, and visa documentation.
10. `market-forecast-expert/` → surfaces neighborhood outlook, trend alerts, pricing heatmaps, and investment caution signals.

## Operating rule

Expert-specific implementation can live here, but final routing, aggregation, explainability, and policy gating should converge through `services/ai-orchestrator/`.

# EstateOS

EstateOS is a secure, scalable, AI-native real estate platform blueprint that combines a human-centered frontend with a Mixture-of-Experts (MoE) backend intelligence layer. It is designed for buyers, investors, brokers, insurers, and advisors who need trusted guidance across property discovery, pricing intelligence, investment analysis, residency-by-investment (RBI), insurance, risk, compliance, and financial decision support.

## Platform pillars

- **Human-centered UX/UI** grounded in ISO 9241-210 and ISO/IEC 25010 principles.
- **Identity-aware trust fabric** that captures investor type, location, financial intent, residency goals, consent, and privacy preferences in the frontend and passes them into the backend router.
- **Unified backend intelligence layer** that routes work to specialist expert agents based on user intent, profile, identity assurance, and contextual risk.
- **Azure-native deployment model** with modular microservices, event pipelines, and secure APIs.
- **Compliance-by-design** aligned with ISO/IEC 27001, ISO/IEC 27017, ISO/IEC 27701, SOC 2 Type 2, ISO 22301, ISO 31000, and adjacent privacy and AI-governance expectations.
- **Transparent and auditable AI** with explainability, policy checks, and evidence capture on every decision path.

## Repository structure

- `backend/` – Python reference implementation of context-aware MoE orchestration, identity trust propagation, policy gating, explainability, and audit evidence generation.
- `docs/architecture.md` – target-state full-stack architecture and Azure deployment pattern.
- `docs/moe-platform-model.md` – MoE operating model, expert catalog, routing responsibilities, and identity-aware routing signals.
- `docs/compliance-mapping.md` – standards alignment, controls, and evidence model.

## Quick start

Run the backend orchestration demo to inspect how a request is routed across experts:

```bash
python3 backend/orchestration.py
```

## Core capabilities

1. Property discovery with buyer and investor intent capture.
2. Pricing intelligence with valuation reasoning and market context.
3. Investment analysis with yield, scenario, and downside modeling.
4. Residency-by-investment workflow planning by jurisdiction.
5. Insurance recommendations aligned to property, climate, and exposure risk.
6. Risk assessment spanning fraud, cyber, property, climate, compliance, and financial suitability.
7. Compliance validation for RBAC, MFA, KYC/AML, sanctions, privacy, records, and explainability.
8. Financial decision support for affordability, leverage, returns, liquidity, and scenario analysis.

## Architecture highlights

- **Frontend experience layer:** role-aware journeys, identity/profile capture, explanation panels, confidence indicators, and audit-friendly action summaries.
- **Identity and trust plane:** Microsoft Entra-backed identity, step-up MFA, entitlement checks, privacy-tier propagation, and KYC/AML/sanctions state shared with the router.
- **Expert mesh:** domain experts for valuation, investment analysis, RBI, insurance, financial risk, compliance, and UX personalization.
- **Policy guardrails:** every recommendation is checked against RBAC, MFA, identity, sanctions, privacy, suitability, and jurisdiction rules before release.
- **Evidence graph:** each decision stores inputs, experts consulted, policy outcomes, confidence, event trail, and human approvals.
- **Continuous learning:** offline evaluation, champion/challenger models, drift monitoring, and human feedback loops.

See the architecture and compliance documents for the full design rationale.

# What MoE Means in Our Platform

## Simple model

Instead of one big AI model that tries to do everything, the platform is designed as:

- many specialized experts
- one router that decides which expert or combination of experts to use

This is a practical **Mixture of Experts (MoE)** approach for the EstateOS platform.

## Core experts

### 1. Property Valuation Expert
Handles property pricing, comparables, value estimation, and market positioning.

### 2. Investment ROI Expert
Analyzes yield, cash flow, appreciation potential, and investment scenarios.

### 3. Residency / Visa Eligibility Expert
Evaluates country-specific residency pathways, visa requirements, and user eligibility signals.

### 4. Insurance Recommendation Expert
Recommends relevant coverage options based on property type, geography, and user risk profile.

### 5. Financial Risk & Payment Expert
Assesses affordability, payment risk, financing readiness, and transaction-related financial constraints.

### 6. Compliance / AML / Fraud Expert
Checks for compliance issues, AML concerns, sanctions risk, fraud signals, and policy constraints.

### 7. UX Personalization Expert
Adapts the user experience, messaging, and next-step recommendations to the user persona and intent.

## Router responsibilities

The router is the orchestration layer. Its job is to decide:

- which expert should answer first
- which experts should collaborate on the same request
- how to sequence expert calls
- how to combine outputs into one user-facing response

## Example routing logic

- **Investor browsing cross-border opportunities**
  - Route to: Residency / Visa Eligibility Expert + Investment ROI Expert + Compliance / AML / Fraud Expert
- **Homebuyer asking if a property is fairly priced**
  - Route to: Property Valuation Expert + Financial Risk & Payment Expert
- **Owner seeking protection advice**
  - Route to: Insurance Recommendation Expert + UX Personalization Expert

## Example

> User is an investor from abroad → use Visa + ROI + Compliance experts.

## Why this model fits the platform

This MoE design helps the platform:

- produce more accurate domain-specific answers
- keep expert logic modular and maintainable
- support multi-step decision flows across real estate, finance, and compliance
- personalize recommendations without mixing every concern into one generic model
- add new experts over time without redesigning the whole system

## Implementation concept

A simple request flow can look like this:

1. User submits a question or profile.
2. Router classifies intent, geography, risk, and transaction stage.
3. Router selects one or more experts.
4. Experts return structured outputs.
5. Router merges the outputs into a single recommendation, explanation, and next action.

## In one sentence

EstateOS uses **many domain experts plus one router** so the right intelligence is applied to the right user at the right time.

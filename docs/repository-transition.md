# EstateOS Repository Transition Guide

## 1. Purpose

This repository is now organized to **visibly converge on the target MoE real estate platform structure** even though the production-grade Next.js and FastAPI implementations are still being built.

The goal of this guide is to keep contributors aligned on two truths:

1. the current repository still contains a lightweight `frontend/` and `backend/` reference prototype, and
2. the canonical destination is the monorepo shape defined by the MoE real estate platform architecture.

## 2. Canonical target structure

The repository should evolve toward the following layout:

```text
apps/
  web/
  admin/
  mobile/
services/
  auth-service/
  user-service/
  listing-service/
  transaction-service/
  visa-service/
  insurance-service/
  payment-service/
  compliance-service/
  integration-service/
  notification-service/
  ai-orchestrator/
experts/
  property-recommender/
  valuation-expert/
  roi-expert/
  visa-expert/
  insurance-expert/
  fraud-expert/
  compliance-expert/
  ux-expert/
  document-expert/
  market-forecast-expert/
packages/
  ui/
  types/
  config/
  shared-utils/
infra/
  terraform/
  bicep/
  kubernetes/
```

## 3. Directory intent

### 3.1 Applications

- `apps/web/` is the future **Next.js + React + TypeScript** property discovery and investor workspace surface.
- `apps/admin/` is the future broker, operator, and compliance console.
- `apps/mobile/` is reserved for a later React Native or Flutter experience if mobile becomes product-critical.

### 3.2 Services

These directories represent the canonical service boundaries for the modular-monolith-first backend plan:

- `services/auth-service/`
- `services/user-service/`
- `services/listing-service/`
- `services/transaction-service/`
- `services/visa-service/`
- `services/insurance-service/`
- `services/payment-service/`
- `services/compliance-service/`
- `services/integration-service/`
- `services/notification-service/`
- `services/ai-orchestrator/`

The initial implementation may still share a FastAPI codebase, but code should be organized so these seams remain explicit.

### 3.3 Experts

The expert directories reserve the canonical Mixture-of-Experts taxonomy:

- property recommendation,
- valuation,
- ROI,
- residency/visa,
- insurance,
- fraud/payment risk,
- compliance,
- UX personalization,
- document intelligence,
- market forecasting.

### 3.4 Packages

Shared contracts and reusable platform primitives should converge into:

- `packages/ui/` for shared UI primitives,
- `packages/types/` for contracts and schemas,
- `packages/config/` for environment and policy configuration,
- `packages/shared-utils/` for cross-cutting utilities.

### 3.5 Infrastructure

- `infra/terraform/` should contain cross-environment IaC modules.
- `infra/bicep/` should contain Azure-native deployment definitions.
- `infra/kubernetes/` should contain workload manifests if AKS becomes necessary.

## 4. Migration rules

Contributors should follow these transition rules:

1. Do not treat `frontend/` as the final web architecture; it is a prototype surface only.
2. Do not treat `backend/orchestration.py` as the final backend shape; it is a reference implementation only.
3. New production-grade web implementation work should start under `apps/web/`.
4. New production-grade orchestration and domain backend work should start under `services/`.
5. Shared types, policies, and explainability contracts should be authored under `packages/` whenever they are reused.
6. Infrastructure work should be authored under `infra/` using Azure-aligned conventions.

## 5. Architectural guardrails

All future implementation work should continue to align to the following locked decisions:

- premium frontend surface built on Next.js, React, TypeScript, Tailwind CSS, shadcn/ui, TanStack Query, i18n, Framer Motion, and map/payment SDK integrations,
- FastAPI-first backend direction with a modular monolith as the initial delivery model,
- Azure-native deployment using Front Door, API Management, PostgreSQL, Redis, Blob Storage, Service Bus, Key Vault, Monitor, Sentinel, Azure AI Search, and Azure Machine Learning,
- the ten-expert MoE model and router-based orchestration contract,
- compliance alignment spanning ISO/IEC 27001, 27017, 27018, 27701, 25010, 42001, 5259, ISO 9241-210, ISO 22301, ISO 31000, PCI DSS, SOC 2 Type 2, ACORD, NAIC-aligned controls, and KYC/AML/sanctions requirements.

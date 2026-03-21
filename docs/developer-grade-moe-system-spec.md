# EstateOS Developer-Grade MoE System Specification

## 1. System overview

### 1.1 Purpose

This specification defines the production-facing Mixture-of-Experts (MoE) system for EstateOS as the source of truth for engineering, product, AI, security, and operations. It translates the platform vision into build-ready contracts for routing, expert execution, trust controls, human review, evaluation, and phased delivery.

The system is intended to support high-trust workflows across:

- property discovery and matching,
- valuation and pricing support,
- investment and ROI analysis,
- residency and visa eligibility assessment,
- insurance intake and quote orchestration,
- payments, fraud, and transaction risk review,
- document intelligence and verification,
- compliance, AML, sanctions, and jurisdictional policy enforcement,
- explainable decision support for buyers, investors, advisors, and operators.

### 1.2 Core design principles

The MoE system must satisfy the following principles:

1. **Policy-aware by default**: routing and expert execution are constrained by compliance, consent, jurisdiction, and role-based entitlements.
2. **Explainable by contract**: every expert and every final decision must emit machine-readable evidence and human-readable rationale.
3. **Fail-safe over fail-open**: low confidence, missing evidence, or elevated risk should reduce automation rather than increase it.
4. **Composable services**: router, experts, policy engines, and review queues are independently deployable and versioned.
5. **Evaluation-driven release**: new experts, prompts, models, and rules require offline and online validation before full rollout.
6. **Human-governed automation**: any action with regulatory, financial, or legal impact can be routed to review based on explicit trigger rules.

### 1.3 Primary runtime flow

```text
Client / API / Event
  -> Context Builder
  -> Feature Extractor
  -> Policy Pre-Checks
  -> MoE Router
  -> Expert Execution Plan
  -> Expert Inference + Retrieval + Rules
  -> Confidence + Evidence Aggregation
  -> Policy Enforcement + Human Review Gate
  -> Final Decision / Recommendation / Hold
  -> Explanation + Audit Record + Observability
```

### 1.4 Decision classes

The system supports four decision classes:

- **Advisory**: recommendations, rankings, summaries, scenario analysis.
- **Eligibility**: residency, insurance, product fit, program fit, or workflow readiness.
- **Risk**: fraud, AML, sanctions, document tamper, payment anomaly, execution risk.
- **Actionable workflow**: approval suggestion, queue routing, next-best-action, or automation eligibility.

## 2. Service boundaries

### 2.1 Core services

The production MoE stack is split into the following services.

#### 2.1.1 AI orchestrator service

Owns:

- canonical request intake,
- context assembly coordination,
- routing feature generation,
- expert selection and execution planning,
- final aggregation,
- confidence fusion,
- explanation assembly,
- policy gate invocation,
- audit event emission.

Does not own:

- durable user/profile master data,
- authoritative listing/deal/payment state,
- external compliance vendor integrations,
- identity provider lifecycle.

#### 2.1.2 Context service

Owns:

- canonical context object construction,
- session and transaction context stitching,
- geography and regulatory pack lookup,
- consent snapshotting,
- role and entitlement projection.

#### 2.1.3 Policy and trust service

Owns:

- hard policy rules,
- configurable soft policy thresholds,
- action gating states,
- human-review policy definitions,
- trust-tier computation,
- release and rollback flags for models and experts.

#### 2.1.4 Expert services

Each expert service owns:

- domain-specific inference logic,
- retrieval adapters and feature transforms,
- domain validation rules,
- expert-level confidence scoring,
- evidence packaging,
- degradation behavior.

Initial expert set:

1. Property Recommendation Expert
2. Valuation Expert
3. ROI Expert
4. Residency/Visa Expert
5. Insurance Expert
6. Payments/Fraud Expert
7. Compliance Expert
8. UX Personalization Expert
9. Document Intelligence Expert
10. Market Forecast Expert

#### 2.1.5 Review operations service

Owns:

- analyst and operator queues,
- review assignment and SLA tracking,
- override capture,
- reviewer notes,
- adjudication outcomes,
- feedback labels for model improvement.

### 2.2 Interaction patterns

- **Synchronous path**: low-latency advisory requests, lightweight ranking, basic eligibility checks.
- **Deferred path**: document extraction, sanctions refresh, quote fan-out, external underwriting, long-running review.
- **Event-driven path**: drift alerts, retraining labels, audit events, state-change notifications, queue escalations.

### 2.3 Ownership boundaries

- Domain systems remain system-of-record for listings, deals, users, payments, and documents.
- The AI orchestrator is system-of-decision for routed inference and explanation artifacts.
- The policy and trust service is system-of-governance for release eligibility and action gates.
- The review operations service is system-of-record for human adjudication decisions.

## 3. Data model

### 3.1 Canonical Context Object (CCO)

The router and experts operate on a versioned Canonical Context Object.

```yaml
CanonicalContext:
  context_id: uuid
  version: string
  created_at: datetime
  actor:
    user_id: uuid
    role: buyer|investor|advisor|admin|analyst|partner
    trust_tier: low|medium|high
    locale: string
    permissions: string[]
  session:
    session_id: uuid
    channel: web|mobile|api|admin|event
    request_id: string
  intent:
    primary: discover|compare|invest|finance|migrate|insure|verify|transact
    secondary: string[]
    urgency: low|medium|high
    explanation_depth: concise|standard|detailed
  profile:
    income_band: string
    budget_band: string
    residency_goals: string[]
    financing_needed: boolean
    investor_profile: end_user|yield_seeker|capital_appreciation|mixed
  property:
    listing_ids: uuid[]
    geography: object
    price_range: object
    asset_type: residential|commercial|land|mixed_use
  workflow:
    stage: discovery|shortlist|due_diligence|offer|underwriting|closing|post_close
    pending_tasks: string[]
  risk:
    fraud_score: float
    aml_risk_level: low|medium|high
    sanctions_hit: boolean
    document_tamper_score: float
    payment_anomaly_score: float
  policy:
    jurisdiction_pack_ids: string[]
    consent_flags: string[]
    data_restrictions: string[]
    human_review_required: boolean
  evidence_refs:
    document_ids: uuid[]
    external_checks: string[]
```

### 3.2 Decision artifact model

Every routed decision should persist a normalized decision artifact.

```yaml
DecisionArtifact:
  decision_id: uuid
  context_id: uuid
  router_version: string
  policy_bundle_version: string
  selected_experts: ExpertExecution[]
  aggregated_confidence: float
  decision_state: auto_release|review_required|blocked|degraded
  user_summary: string
  operator_summary: string
  explanation: ExplanationBundle
  audit_ref: string
```

### 3.3 Expert execution record

```yaml
ExpertExecution:
  expert_name: string
  expert_version: string
  invocation_mode: sync|async|cached|fallback
  latency_ms: integer
  status: success|partial|failed|skipped
  relevance_score: float
  confidence_score: float
  evidence_quality_score: float
  output_ref: string
  fallback_used: string|null
```

## 4. API contracts

### 4.1 Orchestrator API surface

The AI orchestrator exposes the following initial contracts.

#### 4.1.1 `POST /api/v1/ai/decisions`

Purpose:

- create a routed decision request,
- execute the expert plan,
- return a release state with explanation and evidence metadata.

Request shape:

```json
{
  "request_type": "property_advisory",
  "context": {
    "intent": {"primary": "discover", "explanation_depth": "standard"},
    "profile": {"budget_band": "500k-750k", "financing_needed": true},
    "property": {"listing_ids": ["uuid-1"], "asset_type": "residential"}
  },
  "options": {
    "latency_budget_ms": 1800,
    "allow_cached_results": true,
    "require_human_review": false
  }
}
```

Response shape:

```json
{
  "decision_id": "uuid",
  "decision_state": "auto_release",
  "selected_experts": [
    {"expert_name": "property_recommendation", "confidence_score": 0.87},
    {"expert_name": "valuation", "confidence_score": 0.81}
  ],
  "aggregated_confidence": 0.84,
  "recommendations": [],
  "explanation": {
    "summary": "Top recommendation balances budget fit, location match, and projected appreciation.",
    "confidence_label": "high",
    "why": [],
    "watchouts": []
  },
  "policy": {
    "review_required": false,
    "blocking_reasons": []
  }
}
```

#### 4.1.2 `GET /api/v1/ai/decisions/{decision_id}`

Returns the persisted decision artifact, expert execution trace summary, and review state.

#### 4.1.3 `POST /api/v1/ai/decisions/{decision_id}/review`

Creates or updates a review ticket for manual adjudication.

#### 4.1.4 `POST /api/v1/ai/feedback`

Captures user, operator, or downstream outcome feedback for evaluation and retraining.

### 4.2 Internal expert RPC contract

All experts implement a uniform internal interface.

Request envelope:

```json
{
  "trace_id": "string",
  "decision_id": "uuid",
  "expert_name": "valuation",
  "expert_version": "2026-03-01",
  "context": {},
  "task": {
    "task_type": "estimate_value",
    "constraints": {"latency_budget_ms": 700}
  },
  "router_signals": {
    "relevance_score": 0.82,
    "required": true,
    "priority": 2
  }
}
```

Response envelope:

```json
{
  "status": "success",
  "prediction": {},
  "confidence": {},
  "evidence": [],
  "policy_flags": [],
  "explanations": {},
  "fallback_advice": {
    "can_degrade": true,
    "safe_alternative": "cached_comparable_estimate"
  },
  "observability": {
    "latency_ms": 312,
    "tokens_in": 1200,
    "tokens_out": 340
  }
}
```

## 5. MoE router spec

### 5.1 Router responsibilities

The router is responsible for:

- selecting candidate experts,
- determining required versus optional experts,
- assigning expert weights and invocation priority,
- planning parallel and sequential execution,
- applying pre-routing eligibility checks,
- enforcing latency and cost budgets,
- issuing fallback plans,
- returning routing rationale for audit and explanation use.

### 5.2 Router logic

Routing proceeds in seven stages.

#### Stage 1: request normalization

- validate schema,
- attach trace metadata,
- build the CCO,
- derive requested explanation depth and action sensitivity.

#### Stage 2: policy pre-checks

- reject disallowed requests,
- mark mandatory experts,
- mark forbidden experts,
- compute review floor based on jurisdiction, role, and risk.

#### Stage 3: candidate generation

Create the candidate set from:

- intent-to-expert maps,
- workflow-stage maps,
- mandatory policy experts,
- historical bundle templates,
- retrieval of similar past decision patterns.

#### Stage 4: scoring and weighting

For each candidate expert, compute:

```text
expert_score =
  (w1 * intent_fit)
+ (w2 * stage_fit)
+ (w3 * jurisdiction_fit)
+ (w4 * evidence_availability)
+ (w5 * health_score)
+ (w6 * calibration_score)
- (w7 * latency_penalty)
- (w8 * cost_penalty)
- (w9 * risk_penalty_if_optional)
```

Then assign:

- `required` if policy- or workflow-mandated,
- `primary` if above execution threshold,
- `secondary` if useful only when budget remains,
- `suppressed` if below minimum threshold.

#### Stage 5: execution planning

- run independent experts in parallel,
- run dependency-bound experts sequentially,
- reserve capacity for mandatory trust/risk experts,
- shorten the plan if latency budget is exceeded.

#### Stage 6: post-expert fusion

- combine expert outputs,
- resolve contradictions,
- request tie-break or review if disagreement exceeds threshold,
- compute aggregated confidence.

#### Stage 7: release decision

- auto-release,
- release with caution,
- hold for review,
- block.

### 5.3 Mandatory routing rules

The following hard rules apply at launch:

- Residency/Visa Expert is mandatory for migration or residency eligibility requests.
- Compliance Expert is mandatory for cross-border transactions, high-value deals, sanctions-sensitive geographies, or elevated AML risk.
- Payments/Fraud Expert is mandatory for payment initiation, escrow changes, abnormal payment patterns, or execution-risk review.
- Document Intelligence Expert is mandatory when decisions rely on uploaded documents not yet verified.
- Human review is mandatory when policy bundles indicate legal ambiguity, unresolved sanctions matches, confidence below critical threshold, or high financial impact.

### 5.4 Router outputs

The router returns:

- candidate list,
- selected plan,
- weights,
- required expert flags,
- suppressed experts with reasons,
- expected latency,
- expected confidence coverage,
- recommended fallback chain,
- human-review floor,
- routing rationale summary.

## 6. Expert model specs

### 6.1 Standard expert I/O contract

Every expert must implement the following contract.

#### Inputs

- canonical context object,
- task type,
- relevant retrieved evidence,
- policy scope and geography constraints,
- latency/cost budget,
- explanation depth target.

#### Outputs

- domain prediction or recommendation,
- confidence object,
- evidence bundle,
- assumptions and constraints,
- explanation fragments,
- policy flags,
- fallback guidance,
- observability metrics.

### 6.2 Confidence schema

Every expert emits a confidence object using the same schema.

```json
{
  "score": 0.84,
  "label": "high",
  "calibrated": true,
  "basis": {
    "model_certainty": 0.79,
    "evidence_quality": 0.88,
    "data_completeness": 0.91,
    "jurisdiction_coverage": 0.95,
    "freshness": 0.76
  },
  "limits": [
    "Comparable data is sparse for this micro-market."
  ]
}
```

Scoring conventions:

- `0.85-1.00`: high confidence,
- `0.70-0.84`: moderate confidence,
- `0.50-0.69`: low confidence,
- `<0.50`: insufficient confidence.

### 6.3 Explanation schema

Experts emit explanation fragments in a standard structure.

```json
{
  "summary": "This asset ranks highly because it matches budget, location preference, and expected rental yield.",
  "why": [
    "Budget fit is within the user's declared range.",
    "Projected yield exceeds the target threshold."
  ],
  "watchouts": [
    "Insurance premiums are elevated in this zone."
  ],
  "evidence_refs": ["valuation:comp:123", "market:rental-index:uae-dxb-q1"],
  "user_safe": true,
  "operator_notes": [
    "Confidence reduced due to thin transaction history in the last 90 days."
  ]
}
```

### 6.4 Expert-specific output expectations

#### Property Recommendation Expert

Outputs ranked listings, match factors, constraint satisfaction, and diversity controls.

#### Valuation Expert

Outputs price estimate range, comparable evidence, uncertainty interval, and market liquidity notes.

#### ROI Expert

Outputs yield, IRR scenarios, downside sensitivity, and hold-period assumptions.

#### Residency/Visa Expert

Outputs program fit, required documents, threshold checks, disqualifiers, and legal-review sensitivity.

#### Insurance Expert

Outputs product fit, carrier eligibility summary, premium range bands, and referral constraints.

#### Payments/Fraud Expert

Outputs payment risk score, anomaly reasons, fraud indicators, and execution gating recommendation.

#### Compliance Expert

Outputs screening summary, jurisdictional obligations, blocking conditions, escalation reasons, and retention rules.

#### UX Personalization Expert

Outputs explanation depth tuning, workflow ordering, communication preferences, and adaptive UI hints.

#### Document Intelligence Expert

Outputs extraction results, verification status, tamper indicators, missing fields, and downstream confidence impact.

#### Market Forecast Expert

Outputs market outlook, trend confidence, macro assumptions, and scenario warnings.

## 7. Training pipeline spec

### 7.1 Training and evaluation layers

The system requires separate but coordinated pipelines for:

- router/gating model training,
- expert model training or prompt optimization,
- confidence calibration,
- explanation quality evaluation,
- policy-rule regression testing,
- human-review outcome learning.

### 7.2 Data sources

Training and evaluation inputs include:

- historical user interactions,
- listing and transaction outcomes,
- reviewed decision artifacts,
- policy labels and exceptions,
- document verification outcomes,
- sanctions/AML review outcomes,
- user feedback and override data,
- macro and market benchmark feeds.

### 7.3 Training workflow

1. Ingest labeled artifacts and external reference data.
2. Validate schema, lineage, and consent eligibility.
3. Build task-specific training sets by expert domain.
4. Train or refresh expert models and router models.
5. Calibrate confidence against validation outcomes.
6. Run offline evaluation suites.
7. Run shadow or canary deployment.
8. Promote only if threshold gates pass.

### 7.4 Evaluation metrics

The following metrics are release-blocking at minimum.

#### Router metrics

- expert selection precision/recall,
- mandatory expert coverage,
- latency percentile adherence,
- cost per decision,
- degraded-path rate,
- review-trigger accuracy.

#### Expert metrics

- task accuracy or ranking quality,
- calibration error,
- evidence coverage,
- abstention quality,
- contradiction rate,
- fairness slices by geography and user segment.

#### End-to-end metrics

- decision acceptance rate,
- operator override rate,
- unsafe auto-release rate,
- false review rate,
- explanation helpfulness,
- downstream conversion or task completion,
- incident and rollback frequency.

### 7.5 Release gates

A model or prompt version can only be promoted when:

- offline metrics exceed threshold,
- no policy regression is detected,
- calibration remains inside allowed bounds,
- canary results do not worsen review quality or unsafe release rate,
- rollback plan and model card are registered.

## 8. Security and compliance controls

### 8.1 Identity and access

- Service-to-service authentication uses signed service identities.
- End-user and operator access is enforced through RBAC and scoped claims.
- Sensitive expert outputs are partitioned by role, jurisdiction, and need-to-know.

### 8.2 Data protection

- Encrypt data in transit and at rest.
- Tokenize or pseudonymize highly sensitive personal data where feasible.
- Persist only minimum necessary evidence in decision artifacts.
- Apply retention and deletion policies by document class, jurisdiction, and case type.

### 8.3 Compliance controls

- Log policy versions, expert versions, and route decisions for every decision artifact.
- Require explicit consent snapshots for personalization and external data enrichment.
- Support legal hold and audit export for regulated workflows.
- Enforce blocked-action states when sanctions, AML, or identity requirements are unresolved.

### 8.4 Human-review triggers

The following conditions must create or require review:

- aggregated confidence below configurable threshold,
- disagreement between required experts above tolerance threshold,
- sanctions or adverse-media potential match,
- high-value transaction or jurisdiction-specific legal ambiguity,
- document tamper score above threshold,
- fraud or payment anomaly score above threshold,
- any expert declaring `user_safe = false`,
- any policy bundle requiring human sign-off.

### 8.5 Fallback rules

Fallback must follow this priority order:

1. retry same expert if transient failure and budget allows,
2. use cached validated result if freshness policy allows,
3. invoke designated backup expert or heuristic baseline,
4. reduce decision scope to advisory-only,
5. escalate to human review,
6. block action if trust floor is not met.

Fallbacks must never bypass mandatory compliance, fraud, or sanctions controls.

## 9. Deployment architecture

### 9.1 Environment topology

The target deployment uses:

- **apps/web** for Next.js user experience,
- **services/ai-orchestrator** for routing and aggregation,
- **experts/** services for domain experts,
- PostgreSQL for operational and decision metadata,
- Redis for low-latency cache and queue primitives,
- Blob/object storage for artifacts and documents,
- message bus for async execution and review events,
- centralized observability for logs, traces, metrics, and model health.

### 9.2 Runtime requirements

- Router and trust services are always-on and horizontally scalable.
- Experts can scale independently by traffic profile and latency sensitivity.
- Review queue processing supports SLA-aware prioritization.
- Audit and observability data is immutable enough for forensic reconstruction.

### 9.3 Observability requirements

Each request must emit:

- trace ID,
- selected experts,
- latency per stage,
- policy gate outcomes,
- fallback usage,
- review-trigger reasons,
- final release state,
- model and prompt versions,
- user-visible explanation variant.

### 9.4 Reliability posture

- Target graceful degradation instead of total outage.
- Mandatory experts should have warm standby or backup paths.
- Policy engine outages should default to hold/review rather than unsafe release.
- Rollbacks must be possible per router version, expert version, and policy bundle.

## 10. Phased implementation plan

### Phase 0: specification lock

Deliver:

- this developer-grade MoE system specification,
- shared schemas for CCO, expert I/O, confidence, explanation, and decision artifacts,
- initial review-trigger and fallback rule catalog.

### Phase 1: backend implementation pack

Deliver:

- SQL schema and migration plan,
- OpenAPI specification,
- auth and role matrix,
- orchestrator endpoint contracts,
- expert service registration and health contracts.

### Phase 2: code scaffold

Deliver:

- FastAPI orchestrator service scaffold,
- Next.js frontend scaffold,
- expert service templates,
- shared types package,
- local Docker development environment,
- observability and queue stubs.

### Phase 3: MVP expertization

Deliver:

- first production router,
- property, valuation, ROI, compliance, payments/fraud, and document experts,
- decision artifact persistence,
- operator review console foundation,
- evaluation harness and canary workflow.

### Phase 4: regulated workflow expansion

Deliver:

- residency and insurance experts,
- stronger jurisdiction packs,
- review SLAs and escalation policies,
- outcome feedback loops,
- calibrated auto-release thresholds.

### Phase 5: optimization and scale

Deliver:

- learned routing improvements,
- advanced drift monitoring,
- cost-aware orchestration,
- marketplace-ready external expert integration contracts,
- investor/founder reporting surfaces based on decision intelligence.

### Immediate next artifact generation order

1. Database + API implementation pack
2. Backend and frontend scaffold
3. PRD + engineering roadmap merge
4. Investor / founder pack

That order preserves this specification as the authoritative build input for code, product, and GTM collateral.

# EstateOS Developer-Grade MoE System Specification

## 1. Document control

- **Document title**: EstateOS Developer-Grade MoE System Specification
- **Document purpose**: build-ready engineering blueprint for the AI-native real estate operating system
- **Primary audience**: platform architects, backend/frontend engineers, ML engineers, security architects, DevOps/SRE, compliance leads, product managers, audit stakeholders
- **Target runtime posture**: modular FastAPI backend, Next.js frontend, Azure-first deployment, event-driven integration, Mixture-of-Experts (MoE) decision plane
- **Normative relationship**: this specification operationalizes the target state described in `docs/authoritative-blueprint.md`, `docs/architecture.md`, and `docs/production-platform-blueprint.md`

## 2. Executive summary

EstateOS is an **AI-native real estate operating system** that unifies identity, property discovery, listings, search, transactions, documents, residency workflows, insurance, payments, compliance, notifications, and third-party integrations under a governed **Mixture-of-Experts (MoE)** orchestration layer.

The platform is designed as a **modular monolith first**, with clear service boundaries that can be extracted into independently deployable services when scale, team topology, regulatory partitioning, or latency isolation requires it. The runtime split is:

- **Next.js + TypeScript frontend** for customer, advisor, operator, broker, compliance, and admin surfaces.
- **FastAPI backend** for domain APIs, orchestration endpoints, asynchronous workflows, and AI-serving control paths.
- **Azure-native platform services** for identity, data, messaging, storage, observability, machine learning, and governance.
- **MoE decision layer** that selects, invokes, weights, and explains specialized expert models for recommendations, valuation, ROI, residency eligibility, insurance matching, fraud detection, compliance screening, document intelligence, personalization, and market forecasting.

The platform must be auditable, privacy-aware, explainable, and resilient, supporting advisory decisions as well as policy-gated workflow actions. High-impact outcomes require confidence scoring, evidence-backed reasoning, policy evaluation, and explicit fallback or human-review paths.

## 3. Product and system goals

### 3.1 Business goals

1. Reduce fragmentation across the real estate lifecycle.
2. Increase conversion through intelligent property and financing guidance.
3. Improve compliance posture for KYC, AML, sanctions, fraud, and residency checks.
4. Accelerate underwriting, documentation, and closing workflows.
5. Enable partner ecosystems for insurance, payments, identity, and government or regulatory interactions.
6. Provide enterprise buyers and operators with auditable AI-driven decisions.

### 3.2 Non-functional goals

1. **Security-first**: encryption, least privilege, tenant isolation, secrets hygiene, PCI-aware payments.
2. **Explainability-first**: every AI decision must expose evidence, confidence, and policy state.
3. **Composable**: services, workflows, experts, and rules are independently versioned.
4. **Observable**: end-to-end tracing, structured audit logs, model telemetry, and business KPIs.
5. **Resilient**: event-driven retries, backpressure handling, graceful degradation, and BCDR readiness.
6. **Governed**: ISO/IEC, SOC 2, PCI DSS, NAIC-oriented, and AI-governance alignment built into architecture.

## 4. Canonical platform architecture

### 4.1 Logical layers

```text
Clients
  -> Next.js Web App / Admin Console / Mobile App / Partner API Consumers
  -> Edge + API Control Plane
  -> FastAPI BFF + Domain APIs
  -> Domain Services + Workflow Services + Integration Adapters
  -> MoE Orchestrator + Expert Services + Policy Engine + Feature Store
  -> OLTP DB + Search + Cache + Blob Storage + Event Bus + ML Platform
  -> Observability + Audit + Security Ops + Governance + DR
```

### 4.2 Deployment stance

- Start as a **modular monolith** within `backend/app` while preserving service seams.
- Extract to service-per-domain when one or more apply:
  - materially different scale profile,
  - distinct data sensitivity boundary,
  - separate release cadence,
  - long-running workloads requiring runtime isolation,
  - external partner or regulator-facing interface constraints.

### 4.3 Primary runtime topologies

1. **Interactive synchronous**: search, property recommendation, dashboard rendering, pricing summaries.
2. **Asynchronous workflow**: document extraction, fraud review, compliance screening refresh, quote fan-out, payment reconciliation.
3. **Batch and streaming ML**: feature generation, training data materialization, drift monitoring, nightly refresh jobs.
4. **Partner integration**: webhook handling, pull-sync connectors, quote exchange, KYC vendor adapters, sanctions providers.

## 5. Service boundaries

### 5.1 Frontend applications

#### 5.1.1 `apps/web` — customer and advisor experience

Owns:

- public marketing pages,
- authenticated user dashboard,
- listings search and property detail UI,
- deal room,
- documents workspace,
- residency and insurance intake flows,
- AI insights and explanation panels,
- notification center,
- consent surfaces.

Constraints:

- SSR/ISR for SEO-sensitive listing pages.
- Client-side state limited to session UI state and cached query data.
- No direct third-party credential handling other than browser-safe SDK flows.

#### 5.1.2 `apps/admin` — operations and governance console

Owns:

- broker operations,
- compliance queues,
- fraud review queues,
- underwriting and document review,
- partner operations,
- audit and policy management surfaces,
- model-release dashboards,
- support tooling.

#### 5.1.3 `apps/mobile`

Owns:

- lightweight property search,
- saved listings,
- deal status,
- document upload,
- alerts and approvals.

### 5.2 Backend control-plane and domain services

#### 5.2.1 Auth service

Responsibilities:

- authentication, token issuance, MFA, refresh handling,
- session management,
- role-based access control (RBAC), attribute-based access control (ABAC),
- consent capture and revocation,
- device trust and login anomaly signals,
- federation with Azure Entra External ID / B2C or equivalent.

System-of-record for:

- auth identities,
- credential metadata,
- session and device records,
- consent snapshots.

#### 5.2.2 User profile service

Responsibilities:

- user profile lifecycle,
- investor and residency preferences,
- communication preferences,
- household and beneficial ownership declarations,
- advisor/client relationships,
- profile-derived AI feature inputs.

#### 5.2.3 Listing service

Responsibilities:

- listing CRUD and moderation,
- property metadata and media references,
- geospatial facets,
- favorite/save state,
- listing ingestion from brokers, MLS-style sources, or partners,
- publishing events to search and recommendation pipelines.

#### 5.2.4 Search service

Responsibilities:

- search index maintenance,
- geospatial and faceted search,
- ranking pre-signals,
- autocomplete and query suggestions,
- semantic retrieval augmentation for AI experts.

Note: may remain a module inside listing service during modular-monolith phase.

#### 5.2.5 Transaction service

Responsibilities:

- lead-to-deal lifecycle,
- offers, reservations, negotiation status,
- closing milestones,
- participants and approvals,
- escrow or escrow-like orchestration states,
- document bundle requirements by stage.

#### 5.2.6 Document service

Responsibilities:

- document upload lifecycle,
- storage references and hashes,
- OCR/extraction orchestration,
- classification and verification outcomes,
- signature workflow linkage,
- retention and legal hold controls.

#### 5.2.7 Residency workflow service

Responsibilities:

- residency and visa program catalog,
- jurisdiction rule packs,
- applicant intake,
- evidence checklist generation,
- eligibility assessment orchestration,
- government or partner submission state where applicable.

#### 5.2.8 Insurance service

Responsibilities:

- ACORD-aligned canonical risk and quote structures,
- insurance intake and risk exposure mapping,
- quote request orchestration,
- carrier/broker partner integration,
- policy comparison and recommendation,
- referral and fulfillment tracking.

#### 5.2.9 Payment service

Responsibilities:

- payment intent creation,
- tokenized gateway interactions,
- ledger entries and settlement metadata,
- reconciliation workflows,
- refund and dispute handling,
- escrow-style milestone-aware release logic,
- fraud signal publication.

Constraints:

- PCI DSS scope minimization.
- No storage of raw PAN outside approved provider/tokenization patterns.

#### 5.2.10 Compliance service

Responsibilities:

- KYC, KYB, AML, sanctions, PEP, adverse media orchestration,
- beneficial ownership review,
- compliance case management,
- policy rules, thresholds, and holds,
- suspicious activity escalation support,
- regulator/audit evidence packaging.

#### 5.2.11 Notification service

Responsibilities:

- email/SMS/push/in-app delivery,
- template and locale management,
- notification preferences and suppression,
- escalation alerts,
- event-triggered user and operator notices.

#### 5.2.12 Integration service

Responsibilities:

- third-party connector abstraction,
- webhook receiving and signing validation,
- outbound retries and idempotency,
- rate-limit protection,
- contract versioning,
- partner credential management through Key Vault.

#### 5.2.13 AI orchestrator service

Responsibilities:

- canonical AI request intake,
- context assembly,
- policy-aware routing,
- expert selection and invocation,
- weighted aggregation,
- confidence scoring,
- explainability artifact generation,
- fallback management,
- online evaluation hooks,
- audit event publication.

### 5.3 Shared platform capabilities

- Policy engine
- Feature store and offline/online feature serving
- Event bus and workflow orchestration
- Search index
- Blob/object storage
- Model registry and deployment controller
- Audit logging and evidence vault
- Observability and SIEM integration

## 6. Bounded context map and service interactions

### 6.1 Canonical request path

```text
Next.js UI
  -> API Gateway / APIM
  -> FastAPI BFF
  -> Domain service(s)
  -> AI orchestrator (optional, policy-gated)
  -> Expert services + search + features + rules
  -> Decision artifact + domain action suggestion
  -> Notification / review queue / event publication
```

### 6.2 Synchronous dependencies

- Web app -> BFF -> auth/user/listing/search/transaction/document/residency/insurance/payment/compliance/AI modules.
- AI orchestrator -> context builder -> policy engine -> feature store -> expert services -> aggregator.

### 6.3 Asynchronous dependencies

- Listing publish -> search reindex -> recommendation feature refresh.
- Document upload complete -> extraction -> compliance refresh -> decision reevaluation.
- Payment settled -> transaction milestone update -> notification -> fraud post-check.
- Residency application changed -> eligibility reevaluation -> operator task or user notification.

## 7. Canonical domain model

### 7.1 Relational model principles

- PostgreSQL is the authoritative OLTP store.
- Each table includes `id`, `created_at`, `updated_at`, and `version` unless explicitly exempt.
- Soft-delete allowed only for non-regulated records; regulated records use status flags and retention schedules.
- Sensitive columns are tagged for encryption, masking, and access logging.
- Every regulated workflow entity must have an `audit_trail_ref` or equivalent event correlation.

### 7.2 Core entity groups

#### 7.2.1 Identity and access

- `users`
- `user_identities`
- `roles`
- `permissions`
- `user_role_assignments`
- `sessions`
- `devices`
- `consents`
- `access_logs`

#### 7.2.2 Profiles and relationships

- `user_profiles`
- `households`
- `household_members`
- `advisor_client_links`
- `beneficial_owners`
- `organization_profiles`

#### 7.2.3 Listings and properties

- `properties`
- `property_addresses`
- `property_media`
- `listings`
- `listing_amenities`
- `listing_status_history`
- `listing_favorites`
- `saved_searches`
- `search_queries`

#### 7.2.4 Transactions and workflows

- `deals`
- `deal_participants`
- `offers`
- `deal_milestones`
- `reservations`
- `escrow_accounts` (logical reference or partner reference)
- `workflow_tasks`
- `workflow_task_assignments`

#### 7.2.5 Documents

- `documents`
- `document_versions`
- `document_classifications`
- `document_extractions`
- `document_verifications`
- `signature_packets`
- `signature_events`

#### 7.2.6 Residency workflows

- `residency_programs`
- `residency_jurisdictions`
- `residency_program_requirements`
- `residency_applications`
- `residency_applicants`
- `residency_assessments`
- `residency_evidence_items`

#### 7.2.7 Insurance

- `insurance_requests`
- `insurance_risk_profiles`
- `insurance_quote_requests`
- `insurance_quotes`
- `insurance_carriers`
- `insurance_policies`
- `acord_payloads`

#### 7.2.8 Payments and ledgering

- `payment_intents`
- `payment_methods`
- `payment_transactions`
- `ledger_entries`
- `reconciliations`
- `refunds`
- `disputes`

#### 7.2.9 Compliance and risk

- `kyc_checks`
- `aml_screenings`
- `sanctions_screenings`
- `pep_screenings`
- `adverse_media_hits`
- `fraud_cases`
- `compliance_cases`
- `compliance_case_events`
- `risk_scores`
- `watchlist_matches`

#### 7.2.10 AI and governance

- `ai_requests`
- `ai_context_snapshots`
- `ai_decisions`
- `ai_expert_invocations`
- `ai_explanations`
- `ai_feedback`
- `model_registry_entries`
- `feature_definitions`
- `feature_values_online`
- `dataset_versions`
- `evaluation_runs`
- `policy_bundles`

#### 7.2.11 Notifications and integrations

- `notification_templates`
- `notification_events`
- `notification_deliveries`
- `integration_connections`
- `integration_credentials_refs`
- `integration_webhook_events`
- `outbox_events`
- `inbox_events`

### 7.3 Selected table contract details

#### 7.3.1 `users`

| Column | Type | Notes |
|---|---|---|
| id | uuid PK | Internal actor identifier |
| email | citext unique | Optional if external identity only |
| phone_e164 | text | Nullable, encrypted at rest |
| auth_status | text | invited, active, locked, disabled |
| default_locale | text | i18n locale |
| risk_tier | text | low, medium, high |
| tenant_id | uuid | For future multi-tenant partitioning |

#### 7.3.2 `user_profiles`

| Column | Type | Notes |
|---|---|---|
| user_id | uuid FK users | 1:1 profile |
| profile_type | text | buyer, investor, renter, advisor, broker, operator |
| budget_min | numeric(18,2) | Nullable |
| budget_max | numeric(18,2) | Nullable |
| financing_needed | boolean | |
| residency_interest | boolean | |
| investment_horizon_months | integer | |
| risk_appetite | text | conservative, balanced, aggressive |
| privacy_preferences | jsonb | Consent-aware preferences |

#### 7.3.3 `properties`

| Column | Type | Notes |
|---|---|---|
| id | uuid PK | Property root entity |
| external_ref | text | Partner/MLS mapping |
| asset_type | text | residential, commercial, land, mixed_use |
| bedrooms | numeric(4,1) | Nullable |
| bathrooms | numeric(4,1) | Nullable |
| area_sqft | numeric(14,2) | Nullable |
| lot_size_sqft | numeric(14,2) | Nullable |
| year_built | integer | Nullable |
| geo_point | geography(Point,4326) | For spatial search |
| jurisdiction_code | text | Country-region-city policy join |

#### 7.3.4 `listings`

| Column | Type | Notes |
|---|---|---|
| id | uuid PK | Listing identifier |
| property_id | uuid FK properties | Many listings may map historically |
| listing_type | text | sale, rent, lease, off_market |
| status | text | draft, active, pending, under_offer, closed, archived |
| currency_code | char(3) | ISO 4217 |
| price_amount | numeric(18,2) | |
| publish_at | timestamptz | |
| expires_at | timestamptz | |
| moderation_state | text | pending, approved, rejected |

#### 7.3.5 `deals`

| Column | Type | Notes |
|---|---|---|
| id | uuid PK | Deal identifier |
| listing_id | uuid FK listings | |
| buyer_user_id | uuid FK users | Nullable for org buyer |
| seller_party_ref | text | External or internal party ref |
| stage | text | discovery, diligence, offer, underwriting, closing, completed, canceled |
| stage_status | text | on_track, blocked, awaiting_user, awaiting_partner |
| total_value | numeric(18,2) | |
| settlement_currency | char(3) | |
| next_action_at | timestamptz | SLA support |

#### 7.3.6 `documents`

| Column | Type | Notes |
|---|---|---|
| id | uuid PK | Document identifier |
| owner_user_id | uuid FK users | Nullable if deal-owned |
| deal_id | uuid FK deals | Nullable |
| storage_uri | text | Blob reference, not public URL |
| sha256_hash | text | Integrity check |
| mime_type | text | |
| document_type | text | passport, proof_of_funds, title_deed, insurance_form, etc. |
| pii_level | text | low, medium, high, restricted |
| retention_class | text | Regulatory retention mapping |

#### 7.3.7 `residency_applications`

| Column | Type | Notes |
|---|---|---|
| id | uuid PK | Application identifier |
| applicant_user_id | uuid FK users | Primary actor |
| program_id | uuid FK residency_programs | |
| status | text | draft, submitted, assessing, review_required, eligible, ineligible, approved, rejected |
| target_jurisdiction | text | ISO country-region code |
| investment_amount | numeric(18,2) | Nullable |
| source_of_funds_status | text | pending, verified, escalated |
| latest_assessment_id | uuid | Nullable |

#### 7.3.8 `insurance_requests`

| Column | Type | Notes |
|---|---|---|
| id | uuid PK | Intake identifier |
| requester_user_id | uuid FK users | |
| property_id | uuid FK properties | Nullable for portfolio cover |
| insurance_type | text | homeowners, landlord, renters, title, liability |
| acord_version | text | For interoperability |
| exposure_snapshot | jsonb | Canonical risk object |
| status | text | draft, submitted, quoting, quoted, bound, closed |

#### 7.3.9 `payment_intents`

| Column | Type | Notes |
|---|---|---|
| id | uuid PK | Intent identifier |
| deal_id | uuid FK deals | Nullable for fees |
| payer_user_id | uuid FK users | |
| provider | text | stripe, adyen, bank_transfer, escrow_partner |
| amount | numeric(18,2) | |
| currency_code | char(3) | |
| status | text | created, requires_action, processing, succeeded, failed, canceled |
| provider_intent_ref | text | External token/reference |
| pci_scope_class | text | tokenized, redirect, hosted_fields |

#### 7.3.10 `compliance_cases`

| Column | Type | Notes |
|---|---|---|
| id | uuid PK | Case identifier |
| subject_user_id | uuid FK users | Nullable for org or deal case |
| related_deal_id | uuid FK deals | Nullable |
| case_type | text | kyc, aml, sanctions, source_of_funds, enhanced_due_diligence, fraud |
| severity | text | low, medium, high, critical |
| status | text | open, investigating, blocked, cleared, escalated, closed |
| disposition | text | pass, pass_with_conditions, fail, manual_review |
| assigned_queue | text | compliance_l1, compliance_l2, fraud_ops |

### 7.4 Indexing and partitioning guidance

- Partition large event and audit tables by month or quarter.
- Add GIN indexes on `jsonb` policy/evidence blobs used in admin analytics only where justified.
- Use PostGIS indexes on `properties.geo_point`.
- Add composite indexes for high-volume flows, e.g. `(status, created_at)`, `(user_id, updated_at desc)`, `(deal_id, stage)`.
- Apply row-level security for tenant-isolated future mode.

## 8. Canonical API architecture and OpenAPI contracts

### 8.1 API style

- OpenAPI 3.1.
- JSON over HTTPS.
- CamelCase not allowed in backend payloads; use `snake_case`.
- Idempotency keys required for create or payment-mutating endpoints.
- Pagination via cursor-based pagination for mutable collections.
- `x-correlation-id` propagated end-to-end.
- Error envelope standardized across all services.

### 8.2 Standard response envelope

```yaml
ApiResponse:
  request_id: string
  timestamp: string
  data: object | array | null
  meta:
    next_cursor: string | null
    warnings: string[]
  error:
    code: string
    message: string
    details: object | null
```

### 8.3 Standard headers

- `authorization: Bearer <token>`
- `x-correlation-id: <uuid or trace id>`
- `idempotency-key: <opaque key>` for POST/PATCH operations with side effects
- `x-tenant-id` when tenant mode is enabled

### 8.4 Primary endpoint groups

#### 8.4.1 Authentication

- `POST /api/v1/auth/register`
- `POST /api/v1/auth/login`
- `POST /api/v1/auth/refresh`
- `POST /api/v1/auth/logout`
- `POST /api/v1/auth/mfa/challenge`
- `POST /api/v1/auth/mfa/verify`
- `GET /api/v1/auth/sessions`

#### 8.4.2 Users and profiles

- `GET /api/v1/users/me`
- `PATCH /api/v1/users/me`
- `PATCH /api/v1/users/me/preferences`
- `POST /api/v1/users/me/consents`
- `GET /api/v1/users/{user_id}` (admin/advisor scoped)

#### 8.4.3 Listings and search

- `GET /api/v1/listings`
- `POST /api/v1/listings`
- `GET /api/v1/listings/{listing_id}`
- `PATCH /api/v1/listings/{listing_id}`
- `POST /api/v1/listings/{listing_id}/favorite`
- `DELETE /api/v1/listings/{listing_id}/favorite`
- `POST /api/v1/search/listings`
- `GET /api/v1/search/suggestions`

#### 8.4.4 Transactions

- `POST /api/v1/deals`
- `GET /api/v1/deals/{deal_id}`
- `PATCH /api/v1/deals/{deal_id}`
- `POST /api/v1/deals/{deal_id}/offers`
- `POST /api/v1/deals/{deal_id}/milestones/{milestone_id}/complete`
- `POST /api/v1/deals/{deal_id}/participants`

#### 8.4.5 Documents

- `POST /api/v1/documents/presign`
- `POST /api/v1/documents/{document_id}/complete`
- `GET /api/v1/documents/{document_id}`
- `POST /api/v1/documents/{document_id}/analyze`
- `POST /api/v1/documents/{document_id}/verify`

#### 8.4.6 Residency workflows

- `GET /api/v1/residency/programs`
- `GET /api/v1/residency/programs/{program_id}`
- `POST /api/v1/residency/applications`
- `GET /api/v1/residency/applications/{application_id}`
- `POST /api/v1/residency/applications/{application_id}/assess`
- `POST /api/v1/residency/applications/{application_id}/submit`

#### 8.4.7 Insurance

- `POST /api/v1/insurance/requests`
- `GET /api/v1/insurance/requests/{request_id}`
- `GET /api/v1/insurance/requests/{request_id}/quotes`
- `POST /api/v1/insurance/requests/{request_id}/bind`
- `POST /api/v1/insurance/acord/transform`

#### 8.4.8 Payments

- `POST /api/v1/payments/intents`
- `GET /api/v1/payments/{payment_id}`
- `POST /api/v1/payments/{payment_id}/confirm`
- `POST /api/v1/payments/{payment_id}/refund`
- `POST /api/v1/payments/webhooks/{provider}`

#### 8.4.9 Compliance

- `POST /api/v1/compliance/screenings`
- `GET /api/v1/compliance/cases/{case_id}`
- `POST /api/v1/compliance/cases/{case_id}/escalate`
- `POST /api/v1/compliance/cases/{case_id}/resolve`
- `GET /api/v1/compliance/screening-checks/{check_id}`

#### 8.4.10 AI orchestration

- `POST /api/v1/ai/assess`
- `POST /api/v1/ai/recommendations`
- `POST /api/v1/ai/valuation`
- `POST /api/v1/ai/residency-eligibility`
- `POST /api/v1/ai/insurance-match`
- `GET /api/v1/ai/decisions/{decision_id}`
- `POST /api/v1/ai/feedback`

### 8.5 Representative OpenAPI fragments

#### 8.5.1 `POST /api/v1/ai/assess`

```yaml
post:
  summary: Evaluate an AI-assisted decision request through the MoE orchestrator
  operationId: assess_ai_request
  requestBody:
    required: true
    content:
      application/json:
        schema:
          type: object
          required: [intent, actor, subject]
          properties:
            intent:
              type: string
              enum: [discover, compare, invest, migrate, insure, verify, transact]
            actor:
              $ref: '#/components/schemas/ActorContext'
            subject:
              type: object
              properties:
                listing_ids:
                  type: array
                  items: {type: string, format: uuid}
                deal_id:
                  type: string
                  format: uuid
                residency_application_id:
                  type: string
                  format: uuid
                insurance_request_id:
                  type: string
                  format: uuid
            options:
              type: object
              properties:
                explanation_depth:
                  type: string
                  enum: [concise, standard, detailed]
                max_experts:
                  type: integer
                  minimum: 1
                  maximum: 10
                allow_async_followups:
                  type: boolean
  responses:
    '200':
      description: Decision produced
    '202':
      description: Deferred workflow started
    '403':
      description: Policy denied
    '409':
      description: Review required before release
```

#### 8.5.2 `DecisionResponse`

```yaml
DecisionResponse:
  type: object
  required: [decision_id, decision_state, confidence, selected_experts, explanation]
  properties:
    decision_id:
      type: string
      format: uuid
    decision_state:
      type: string
      enum: [auto_release, review_required, blocked, degraded, deferred]
    confidence:
      type: number
      minimum: 0
      maximum: 1
    selected_experts:
      type: array
      items:
        $ref: '#/components/schemas/ExpertInvocationSummary'
    outputs:
      type: object
      description: Domain-specific final result
    explanation:
      $ref: '#/components/schemas/ExplanationBundle'
    policy:
      $ref: '#/components/schemas/PolicyDecision'
    review:
      $ref: '#/components/schemas/ReviewDecision'
```

#### 8.5.3 `ExplanationBundle`

```yaml
ExplanationBundle:
  type: object
  properties:
    summary_for_user:
      type: string
    summary_for_operator:
      type: string
    expert_contributions:
      type: array
      items:
        type: object
        properties:
          expert_name: {type: string}
          contribution_weight: {type: number}
          confidence: {type: number}
          rationale: {type: string}
          evidence_refs:
            type: array
            items: {type: string}
    policy_notes:
      type: array
      items: {type: string}
    warnings:
      type: array
      items: {type: string}
```

### 8.6 API versioning and compatibility

- Path-versioned public APIs: `/api/v1`.
- Backward-compatible additive changes only within a major version.
- Deprecation windows documented and monitored.
- OpenAPI generated from FastAPI schemas and validated in CI.

## 9. Event-driven architecture and workflows

### 9.1 Eventing principles

- Use Service Bus or Event Grid for cross-domain asynchronous communication.
- Use transactional outbox pattern for domain-event publication.
- Each event includes trace metadata, schema version, tenant or jurisdiction scope, and idempotency key.
- Consumers must be idempotent.

### 9.2 Canonical event envelope

```yaml
DomainEvent:
  event_id: uuid
  event_type: string
  event_version: string
  occurred_at: datetime
  producer: string
  correlation_id: string
  causation_id: string
  subject_ref: string
  tenant_id: string | null
  data_classification: public|internal|confidential|restricted
  payload: object
```

### 9.3 Core event types

- `user.registered`
- `user.profile.updated`
- `listing.created`
- `listing.published`
- `listing.updated`
- `search.index.refresh_requested`
- `deal.created`
- `deal.offer.submitted`
- `deal.stage.changed`
- `document.upload.completed`
- `document.analysis.completed`
- `document.verification.failed`
- `residency.application.submitted`
- `residency.assessment.completed`
- `insurance.quote.requested`
- `insurance.quote.received`
- `payment.intent.created`
- `payment.succeeded`
- `payment.failed`
- `compliance.screening.completed`
- `compliance.case.escalated`
- `ai.request.routed`
- `ai.decision.completed`
- `ai.review.required`
- `notification.dispatch.requested`

### 9.4 Event-driven workflow examples

#### 9.4.1 Listing publication

1. Listing service publishes `listing.published`.
2. Search service consumes event and refreshes search index.
3. Feature pipeline updates listing features and neighborhood aggregates.
4. Notification service may dispatch saved-search matches.
5. AI orchestrator may refresh recommendation caches for affected cohorts.

#### 9.4.2 Document compliance reevaluation

1. Document service publishes `document.analysis.completed`.
2. Compliance service reevaluates KYC/source-of-funds evidence.
3. AI orchestrator consumes updated risk context.
4. If confidence or risk posture changes materially, a new decision artifact is created.
5. Review service or notification service informs operators and users.

#### 9.4.3 Payment milestone release

1. Payment provider webhook is normalized into `payment.succeeded`.
2. Payment service posts ledger entries and reconciliation jobs.
3. Transaction service updates milestone completion.
4. Fraud expert may run post-settlement anomaly checks.
5. Notifications are dispatched.

#### 9.4.4 Residency eligibility change

1. Residency service emits `residency.application.submitted` or updated evidence event.
2. AI orchestrator invokes residency, compliance, and document experts.
3. Policy engine decides auto-release vs review-required.
4. Decision stored and surfaced to user/operator with rationale.

## 10. MoE orchestration layer

### 10.1 Overview

The AI orchestrator is the system-of-decision for governed AI requests. It must never act as an opaque black box. Instead, it composes structured context, routes requests through policy-aware expert selection, aggregates evidence, and produces a confidence-calibrated, explainable output.

### 10.2 Major subcomponents

#### 10.2.1 Request normalizer

Responsibilities:

- validate request schema,
- enrich request with correlation metadata,
- infer journey and workflow stage if omitted,
- reject malformed or disallowed input early.

#### 10.2.2 Context builder

Responsibilities:

- construct versioned **Canonical Context Object (CCO)**,
- retrieve actor, profile, listing, deal, document, payment, compliance, and jurisdiction context,
- resolve consent and data minimization rules,
- attach feature references, not bulky raw payloads when avoidable,
- attach data quality scores and freshness metadata.

Inputs:

- authenticated actor context,
- request subject references,
- session metadata,
- domain service lookups,
- feature store snapshots,
- policy bundle reference.

Outputs:

- `canonical_context`,
- `context_quality_score`,
- `missing_context_flags`,
- `freshness_profile`.

#### 10.2.3 Policy-aware routing engine

Responsibilities:

- evaluate hard policy denials,
- constrain expert eligibility by jurisdiction, consent, customer type, and model release policy,
- compute initial relevance priors,
- block or defer unsupported automations.

Routing inputs:

- intent,
- workflow stage,
- geography,
- property class,
- actor role,
- risk posture,
- regulatory scope,
- latency budget,
- expert availability,
- model release policy.

Routing outputs:

- candidate expert list,
- expert invocation mode (`sync`, `async`, `cached`, `shadow`),
- route rationale,
- pre-check policy findings.

#### 10.2.4 Expert selection logic

Selection scores are based on:

```text
selection_score =
  (intent_match * 0.25) +
  (workflow_stage_match * 0.15) +
  (subject_coverage * 0.15) +
  (historical_value_add * 0.10) +
  (jurisdiction_eligibility * 0.10) +
  (data_quality_fit * 0.10) +
  (latency_fit * 0.05) +
  (cost_fit * 0.05) +
  (policy_allowance * 0.05)
```

Rules:

- Experts below minimum threshold are not invoked.
- Hard-required experts may be forced in despite low score if policy or workflow requires them.
- At least one risk/compliance expert must run for regulated transaction or residency flows.
- Shadow experts may run without affecting outcome to support evaluation.

#### 10.2.5 Expert execution coordinator

Responsibilities:

- parallel invocation where safe,
- timeout and circuit-breaker handling,
- partial-failure recording,
- caching policy application,
- evidence normalization.

#### 10.2.6 Weighted aggregation engine

Responsibilities:

- normalize expert outputs to common scoring contracts,
- weight by expert relevance, confidence, evidence quality, and policy priority,
- fuse overlapping or contradictory outputs,
- generate final ranked recommendations or dispositions.

Example aggregation formula:

```text
expert_weight = base_weight * relevance_score * confidence_score * evidence_quality_score * policy_weight
final_score = sum(expert_weight * normalized_output_score) / sum(expert_weight)
```

Conflict handling:

- If fraud/compliance expert emits hard block, decision state becomes `blocked` regardless of positive advisory experts.
- If core experts disagree above configured divergence threshold, state becomes `review_required`.
- If context quality is low, output may be returned as `degraded` with explicit warnings.

#### 10.2.7 Confidence scoring service

Confidence is not raw model probability. It is calibrated from:

- expert-level confidence,
- data completeness,
- data freshness,
- agreement across experts,
- historical performance by segment,
- policy risk multiplier,
- out-of-distribution (OOD) detection,
- human override prevalence for similar decisions.

Confidence bands:

- `0.85 - 1.00`: high confidence
- `0.70 - 0.84`: medium confidence
- `0.50 - 0.69`: low confidence, recommend caution
- `< 0.50`: insufficient confidence, review or fallback required

#### 10.2.8 Explainability assembler

Outputs:

- user-facing explanation,
- operator-facing explanation,
- expert contribution ledger,
- key evidence references,
- policy rationale,
- confidence rationale,
- omitted-data warnings,
- next-best-action suggestions.

#### 10.2.9 Fallback manager

Fallback strategies:

1. Serve cached result if context equivalence and freshness policy permit.
2. Reduce to deterministic rules or heuristics for one domain.
3. Invoke fewer experts and mark degraded confidence.
4. Defer to asynchronous review.
5. Hard-block if required risk/compliance evidence is unavailable.

### 10.3 Canonical Context Object (CCO)

```yaml
CanonicalContext:
  context_id: uuid
  context_version: string
  created_at: datetime
  actor:
    user_id: uuid
    role: buyer|investor|advisor|broker|operator|admin|partner
    permissions: string[]
    trust_tier: low|medium|high
    locale: string
  session:
    request_id: string
    session_id: uuid
    channel: web|mobile|admin|api|event
    ip_geo: object
    device_trust: string
  intent:
    primary: discover|compare|invest|migrate|insure|verify|transact
    secondary: string[]
    explanation_depth: concise|standard|detailed
  subject:
    listing_ids: uuid[]
    property_ids: uuid[]
    deal_id: uuid|null
    document_ids: uuid[]
    residency_application_id: uuid|null
    insurance_request_id: uuid|null
    payment_intent_id: uuid|null
  profile:
    budget_range: object
    financing_needed: boolean
    investor_profile: end_user|yield|appreciation|balanced
    residency_goals: string[]
    risk_appetite: string
  jurisdiction:
    country_code: string
    region_code: string|null
    policy_pack_ids: string[]
    data_residency_constraints: string[]
  risk:
    aml_risk_level: low|medium|high
    sanctions_hit: boolean
    fraud_score: float
    document_tamper_score: float
    payment_anomaly_score: float
  quality:
    context_quality_score: float
    freshness_score: float
    missing_fields: string[]
  governance:
    consent_flags: string[]
    review_required: boolean
    restricted_actions: string[]
    policy_bundle_version: string
```

### 10.4 Decision artifact contract

```yaml
DecisionArtifact:
  decision_id: uuid
  request_id: uuid
  context_id: uuid
  router_version: string
  policy_bundle_version: string
  selected_experts:
    - expert_name: string
      expert_version: string
      invocation_mode: sync|async|cached|shadow|fallback
      relevance_score: float
      confidence_score: float
      evidence_quality_score: float
      latency_ms: integer
      status: success|partial|failed|skipped
  aggregated_output: object
  final_confidence: float
  confidence_band: high|medium|low|insufficient
  decision_state: auto_release|review_required|blocked|degraded|deferred
  explanation_bundle: object
  policy_findings: object
  review_recommendation: object
  audit_event_refs: string[]
```

## 11. Expert model contracts

### 11.1 Shared expert contract

Every expert must implement the following logical contract.

**Input contract**

```yaml
ExpertInput:
  expert_name: string
  expert_version: string
  context_id: uuid
  canonical_context: object
  feature_refs: string[]
  supporting_entities: object
  policy_constraints: object
  execution_options:
    timeout_ms: integer
    explanation_depth: string
    allow_external_calls: boolean
```

**Output contract**

```yaml
ExpertOutput:
  expert_name: string
  expert_version: string
  status: success|partial|failed|skipped
  output_type: recommendation|score|classification|forecast|extraction|alert
  output_payload: object
  normalized_score: float
  confidence_score: float
  evidence_quality_score: float
  calibration_band: string
  rationale: string
  evidence_refs: string[]
  warnings: string[]
  policy_flags: string[]
  latency_ms: integer
```

### 11.2 Property recommendation expert

Purpose:

- rank listings against buyer or investor preferences.

Required inputs:

- user profile,
- listing candidate set,
- location preferences,
- budget,
- amenity preferences,
- transaction stage,
- interaction history.

Outputs:

- ranked listing IDs,
- fit scores by dimension,
- top reasons,
- disqualifiers,
- alternative suggestions.

### 11.3 Valuation expert

Purpose:

- estimate fair market value, confidence interval, and valuation drivers.

Required inputs:

- property attributes,
- comps,
- market trends,
- listing history,
- jurisdiction and macro signals.

Outputs:

- estimated value,
- value range,
- comp set references,
- appreciation sensitivity,
- confidence and caveats.

### 11.4 ROI expert

Purpose:

- project yield, cash flow, cap rate, IRR, and scenario outputs.

Required inputs:

- property price,
- financing assumptions,
- taxes/fees,
- expected rental income,
- maintenance and vacancy assumptions,
- hold period.

Outputs:

- ROI scenarios,
- sensitivity analysis,
- downside flags,
- break-even horizon,
- investment suitability classification.

### 11.5 Residency eligibility expert

Purpose:

- assess program fit and evidence readiness for residency or visa pathways.

Required inputs:

- applicant demographics,
- target jurisdiction,
- family composition,
- investment profile,
- source-of-funds posture,
- uploaded evidence references,
- compliance posture.

Outputs:

- eligibility status,
- likelihood band,
- missing evidence checklist,
- jurisdiction-specific blockers,
- recommended next actions.

### 11.6 Insurance matching expert

Purpose:

- match risk profile to coverage options and quote request strategy.

Required inputs:

- property characteristics,
- occupancy/use,
- asset value,
- claims history,
- jurisdiction,
- customer preferences,
- ACORD-aligned risk snapshot.

Outputs:

- candidate policy products,
- coverage recommendations,
- quote routing plan,
- exclusions or caution flags,
- affordability summary.

### 11.7 Fraud detection expert

Purpose:

- identify payment, identity, document, and behavioral anomalies.

Required inputs:

- device and session signals,
- payment behavior,
- document verification outputs,
- identity consistency checks,
- historical fraud patterns,
- graph relationships where available.

Outputs:

- fraud risk score,
- anomaly reasons,
- recommended controls,
- case escalation recommendation,
- evidence graph references.

### 11.8 Compliance screening expert

Purpose:

- assess KYC/AML/sanctions/PEP and policy gate status.

Required inputs:

- subject identity profile,
- beneficial ownership data,
- source-of-funds/source-of-wealth metadata,
- sanctions/PEP vendor results,
- adverse media hits,
- jurisdiction rule pack.

Outputs:

- screening disposition,
- risk level,
- EDD recommendation,
- blocked actions,
- remediation tasks.

### 11.9 Document intelligence expert

Purpose:

- classify, extract, compare, and verify documents.

Required inputs:

- document binaries or secure refs,
- expected document type,
- verification policy,
- language/locale hints,
- linked identity or property records.

Outputs:

- document classification,
- extracted fields,
- quality score,
- tamper indicators,
- mismatches to expected entities,
- structured evidence references.

### 11.10 Personalization expert

Purpose:

- adapt experience, messaging, sequencing, and explanation style.

Required inputs:

- role,
- engagement history,
- funnel stage,
- locale,
- accessibility preferences,
- prior expert interactions.

Outputs:

- UI/content personalization payload,
- explanation-depth preference,
- next-best-action ordering,
- notification timing suggestions.

### 11.11 Market forecasting expert

Purpose:

- provide short- and medium-term market directional insights.

Required inputs:

- macroeconomic series,
- local market data,
- supply-demand trends,
- comps velocity,
- seasonality,
- neighborhood segmentation.

Outputs:

- forecast direction and confidence band,
- time-horizon forecast metrics,
- market risks,
- recommended caution or opportunity markers.

## 12. AI training and MLOps pipelines

### 12.1 Pipeline stages

1. Data ingestion
2. Data validation and quality checks
3. Feature engineering
4. Dataset generation and labeling
5. Model training
6. Evaluation and governance review
7. Model registry and approval
8. Deployment and rollout
9. Monitoring and feedback capture
10. Retraining and retirement

### 12.2 Data ingestion

Sources:

- OLTP domain events,
- listing and search logs,
- transaction and payment events,
- document metadata and extraction outputs,
- compliance outcomes,
- insurance quote outcomes,
- residency adjudication outcomes,
- partner/vendor signals,
- market data feeds.

Controls:

- schema registry validation,
- PII classification,
- lineage capture,
- source contract versioning,
- data residency tagging.

### 12.3 Data validation

Checks:

- completeness,
- uniqueness,
- drift from expected ranges,
- stale data detection,
- label leakage prevention,
- protected-attribute handling policy.

Tooling expectations:

- Great Expectations or equivalent,
- Azure Data Factory / Databricks / AML pipelines,
- automated quality score outputs.

### 12.4 Feature engineering

- Offline feature generation for training.
- Online feature serving for low-latency inference.
- Shared feature definitions stored in registry.
- Point-in-time correctness enforced for supervised datasets.
- Derived features must record source lineage and transformation version.

### 12.5 Dataset generation

Dataset classes:

- recommendation ranking datasets,
- valuation regression datasets,
- ROI scenario datasets,
- eligibility classification datasets,
- fraud detection anomaly or classification datasets,
- compliance outcome datasets,
- document extraction labeled corpora,
- personalization bandit or propensity datasets,
- market forecasting time-series datasets.

Label sources:

- user interactions,
- final deal outcomes,
- operator adjudications,
- partner quote selections,
- compliance resolutions,
- document verification truth sets,
- external market benchmarks.

### 12.6 Training strategy

- Train each expert independently with its own data contract.
- Maintain calibration models where required.
- Version prompts separately from models for LLM-backed experts.
- Support classical ML, gradient boosting, deep learning, and LLM/RAG patterns depending on expert.
- Use experiment tracking and reproducibility metadata for every run.

### 12.7 Evaluation strategy

Representative metrics:

- Recommendation: NDCG, MAP, CTR lift, save rate, conversion uplift.
- Valuation: MAE, MAPE, prediction interval coverage.
- ROI: scenario error against realized outcomes where observable.
- Residency eligibility: precision/recall, false-negative minimization, calibration.
- Insurance matching: quote bind rate, coverage suitability, partner acceptance.
- Fraud: recall at fixed precision, false-positive review cost.
- Compliance: false-negative minimization, escalation quality, reviewer agreement.
- Document intelligence: extraction F1, classification accuracy, tamper detection precision.
- Personalization: engagement uplift, abandonment reduction, policy-safe sequencing.
- Market forecasting: MAPE, directional accuracy, interval coverage.

Governance checks:

- fairness and bias review,
- stability under segment shifts,
- explainability completeness,
- adversarial and prompt-injection robustness where applicable,
- privacy leakage testing.

### 12.8 Model registry and approval

Registry requirements:

- model artifact hash,
- training data version,
- code commit,
- feature schema version,
- evaluation summary,
- approval status,
- expiration/review date,
- linked risk assessment.

### 12.9 Deployment strategy

- Blue/green or canary rollout per expert.
- Shadow deployments for new experts or prompts.
- Policy bundle can disable individual experts without redeploying applications.
- Low-confidence or low-SLA routes can default to older approved model versions.

### 12.10 Monitoring

Monitor:

- latency,
- throughput,
- error rates,
- data drift,
- prediction drift,
- calibration drift,
- business outcome drift,
- human override rates,
- adverse impact indicators,
- hallucination or unsupported-claim indicators for LLM-backed experts.

### 12.11 Feedback loops

Feedback sources:

- explicit user feedback,
- operator review outcomes,
- downstream conversion/outcome events,
- quote acceptance or rejection,
- fraud true-positive and false-positive adjudications,
- compliance closure reasons.

Feedback handling:

- feed into labeled datasets,
- update confidence calibration,
- drive policy threshold tuning,
- trigger human-review expansion where model risk increases.

### 12.12 Retraining strategies

- schedule-based retraining for stable experts,
- drift-triggered retraining for volatile domains,
- event-triggered retraining after major policy or market changes,
- champion/challenger comparison before promotion,
- retirement and rollback process for degraded models.

## 13. Security, privacy, and governance

### 13.1 Security architecture baseline

- SSO/federation with MFA.
- RBAC + ABAC for domain and data-level authorization.
- Encryption in transit with TLS 1.2+ and at rest using platform-managed or customer-managed keys.
- Secrets only in Azure Key Vault.
- Network isolation for sensitive backends using VNets/private endpoints.
- WAF, DDoS protection, API throttling, and bot mitigation.
- Audit logs immutable and exported to SIEM.

### 13.2 Privacy architecture

- Data minimization in the context builder.
- Purpose limitation and consent-aware processing.
- Pseudonymization for training and analytics where feasible.
- Data subject rights workflow support.
- Data retention schedules by record class.
- Cross-border transfer controls and data residency tagging.

### 13.3 Governance alignment mapping

#### ISO/IEC 27001

- ISMS scope must include application, cloud, and AI-serving systems.
- Asset inventory, access control, logging, supplier risk, vulnerability management, and incident response are mandatory controls.

#### ISO/IEC 27017 and 27018

- Cloud control responsibilities allocated between EstateOS and Azure.
- PII protection obligations explicitly documented for storage, support access, and customer data handling.

#### ISO/IEC 27701

- Privacy information management system overlays the ISMS.
- Privacy roles, processing purposes, retention, and consent records must be system-backed.

#### ISO/IEC 25010

- System quality targets cover security, reliability, maintainability, portability, and usability.
- NFRs must be testable in release gates.

#### ISO 22301

- BCDR plans, RTO/RPO targets, failover procedures, and crisis communications must be tested.

#### ISO 31000

- Enterprise risk management integrated into architectural decisioning and model-risk review.

#### PCI DSS

- Tokenized or hosted payment collection.
- Segmented payment flows.
- Secure SDLC and logging for payment systems.
- Quarterly and annual control cadence integrated with engineering operations.

#### SOC 2 Type 2

- Security, availability, confidentiality, and privacy controls evidenced through system logs, tickets, and review artifacts.

#### ISO/IEC 42001 and ISO/IEC 5259

- AI management system established for model inventory, risk assessments, approval workflows, monitoring, and continual improvement.
- Data quality governance aligned with training/inference data lineage, representativeness, and documented limitations.

### 13.4 Insurance governance alignment

- ACORD-aligned canonical payloads for quote request and policy information exchange.
- Carrier adapters must preserve canonical-to-partner field mapping.
- NAIC-oriented data protection expectations applied to insurance PII and producer workflow handling.

### 13.5 KYC/AML/sanctions controls

- CIP/KYC evidence capture,
- beneficial ownership declarations,
- sanctions/PEP/adverse media screening,
- transaction monitoring hooks,
- source-of-funds/source-of-wealth evidence,
- enhanced due diligence for high-risk segments,
- case escalation and disposition logging.

### 13.6 AI governance controls

- approved use-case inventory,
- model cards and data sheets,
- human oversight triggers,
- explainability thresholds,
- prohibited decision classes for full automation,
- red-team and abuse testing,
- periodic review and sunset process.

## 14. Third-party integration architecture

### 14.1 Integration categories

- Identity and KYC providers
- AML/sanctions providers
- Insurance carriers/brokers
- Payment gateways and banking rails
- eSignature providers
- Maps and geocoding providers
- Market data providers
- Messaging providers
- Government/residency or legal workflow partners

### 14.2 Integration standards

- Signed webhooks and replay protection.
- Per-partner API credentials rotated and vaulted.
- Canonical internal schema with adapter translation at edge.
- Retries with dead-letter queues for transient partner failures.
- Contract tests for each adapter.

### 14.3 ACORD alignment

- Maintain canonical object model for insured party, location, coverages, exposures, claims history, and quote terms.
- Adapter layer transforms canonical payloads into carrier-specific ACORD or partner variants.
- Version all ACORD mappings and preserve raw request/response evidence for audits.

## 15. Azure deployment blueprint

### 15.1 Core Azure services

- Azure Front Door for global entry and WAF.
- Azure API Management for API gateway, throttling, and partner exposure.
- Azure App Service and/or AKS for app workloads.
- Azure Database for PostgreSQL for OLTP.
- Azure Cache for Redis for caching and transient state.
- Azure Blob Storage for documents and model artifacts.
- Azure Service Bus for queues/topics.
- Azure Event Grid where event fan-out is appropriate.
- Azure AI Search for listing/document retrieval.
- Azure Machine Learning for training, registry, and deployment.
- Azure Key Vault for secrets and keys.
- Azure Monitor, Log Analytics, Application Insights, and Microsoft Sentinel for observability and security operations.

### 15.2 Environment strategy

- `dev`, `test`, `staging`, `prod` minimum.
- Separate subscriptions or strong resource-group isolation for higher environments.
- Infra-as-code via Terraform and/or Bicep.
- Policy-as-code and Azure Policy for guardrails.

### 15.3 Runtime placement

- BFF and domain APIs can begin on App Service.
- High-throughput or specialized experts may move to AKS or AML online endpoints.
- Background workers consume Service Bus queues.
- Stateful data only in managed services, never in pod-local storage.

### 15.4 Observability and operations

- OpenTelemetry traces across frontend, APIs, queues, and experts.
- SLOs defined for latency, error rate, queue lag, and critical workflows.
- Pager and incident integrations for high-severity alerts.
- Security alerts forwarded into Sentinel.

## 16. Reliability and BCDR requirements

### 16.1 Target reliability controls

- Multi-AZ deployment for production data plane.
- Retry budgets and circuit breakers for external integrations.
- Queue-based decoupling for non-critical async work.
- Rate limiting and graceful degradation for expert timeouts.
- Backup and restore procedures verified regularly.

### 16.2 Indicative recovery objectives

- Critical auth and deal APIs: RTO <= 2 hours, RPO <= 15 minutes.
- Document and evidence vault: RTO <= 4 hours, RPO <= 15 minutes.
- Analytics and training pipelines: RTO <= 24 hours, RPO <= 24 hours.

## 17. Implementation roadmap

### Phase 0 — repository alignment and contracts

- finalize canonical docs,
- lock service boundaries,
- standardize schema and event naming,
- establish OpenAPI generation and CI validation,
- define security and model governance baseline.

### Phase 1 — modular monolith hardening

- expand FastAPI domain modules,
- migrate prototype payload contracts into typed schemas,
- implement PostgreSQL persistence,
- add Service Bus outbox/inbox patterns,
- stand up Next.js foundation for `apps/web` and `apps/admin`.

### Phase 2 — AI orchestrator and expert contract maturity

- implement context builder,
- introduce policy engine and confidence calibrator,
- formalize ten-expert interfaces,
- persist decision artifacts and explainability bundles,
- add review queue integration.

### Phase 3 — workflow and partner integration expansion

- document intelligence pipeline,
- insurance ACORD adapters,
- KYC/AML/sanctions integrations,
- payment gateway productionization,
- residency workflow rule packs and evidence checklists.

### Phase 4 — enterprise controls and scale

- advanced observability and SIEM integration,
- model registry and champion/challenger release flows,
- DR testing and chaos exercises,
- tenant-aware partitioning,
- selective service extraction for scale domains.

### Phase 5 — optimization and continuous governance

- online experimentation,
- advanced personalization,
- forecasting improvements,
- policy threshold tuning,
- formal external assurance readiness for ISO/SOC/PCI attestations.

## 18. Build-readiness checklist

The platform is considered build-ready when the following are all true:

- service contracts are versioned and owned,
- the relational schema baseline is approved,
- OpenAPI contracts compile from code and pass linting,
- event schemas are versioned and contract-tested,
- MoE routing contract and expert I/O contracts are implemented,
- confidence, explainability, and fallback behavior are testable,
- security and privacy controls are traceable to system components,
- Azure landing zone and CI/CD foundations exist,
- review operations and audit evidence pathways are defined,
- model lifecycle governance and rollback procedures are documented.

## 19. Canonical engineering decisions

1. **FastAPI is the backend runtime of record** for domain APIs and AI orchestration.
2. **Next.js is the frontend runtime of record** for customer and operator web applications.
3. **PostgreSQL is the canonical OLTP store**.
4. **Event-driven workflows are mandatory** for long-running or partner-mediated operations.
5. **MoE orchestration is policy-aware and explainable by contract**.
6. **Payments remain tokenized and PCI-minimized**.
7. **Insurance interoperability uses ACORD-aligned canonical schemas**.
8. **KYC/AML/sanctions and beneficial ownership controls are first-class domains**.
9. **Azure is the preferred deployment platform**.
10. **AI governance is embedded into release management, not layered on afterward**.

## 20. Acceptance criteria for engineering execution

An implementation claiming conformance to this specification must demonstrate:

- working FastAPI route groups aligned to the domain boundaries,
- a Next.js application consuming the documented APIs,
- persisted relational tables covering the domain model baseline,
- published OpenAPI 3.1 contracts,
- emitted domain events for core workflows,
- a context builder and policy-aware router invoking multiple experts,
- weighted aggregation with confidence and explanation outputs,
- at least one fallback path and one human-review path per high-impact workflow,
- training and deployment pipelines with registry-backed model versioning,
- enterprise-grade security, privacy, observability, and governance evidence.

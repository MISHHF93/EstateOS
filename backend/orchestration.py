"""EstateOS Mixture-of-Experts orchestration reference implementation.

This module provides a dependency-light Python blueprint for how EstateOS can:
- capture identity, trust, and profile signals from the frontend,
- detect user intents,
- assemble user/profile/context signals,
- route work to specialized experts,
- enforce policy gates,
- emit auditable event records,
- build explainable property decisions,
- orchestrate transaction experts for pricing, negotiation, document validation,
  workflow integrity, resilience, and risk scoring,
- evaluate payment fraud, escrow conditions, PCI-safe frontend controls, and reconciliation posture,
- continuously score compliance and operational risk across real estate, payments, insurance, and residency workflows,
- validate, transform, and route partner API payloads through an expert-augmented integration hub.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Dict, Iterable, List, Sequence
import json
import uuid


@dataclass(frozen=True)
class UserProfile:
    role: str
    investor_type: str
    intent: str
    financial_intent: str
    country: str
    target_region: str
    risk_tolerance: str
    investment_budget: int
    residency_interest: bool
    residency_goal: str
    financing_needed: bool
    household_size: int


@dataclass(frozen=True)
class IdentityContext:
    subject_id: str
    auth_assurance_level: str
    mfa_completed: bool
    rbac_roles: Sequence[str]
    entitlements: Sequence[str]
    kyc_status: str
    aml_risk: str
    sanctions_status: str
    privacy_tier: str
    consent_scope: Sequence[str]
    pii_tags: Sequence[str]
    profile_source: str = "frontend"


@dataclass(frozen=True)
class RequestContext:
    request_id: str
    journey_stage: str
    channel: str
    locale: str
    has_verified_identity: bool
    has_consent: bool
    property_country: str
    property_type: str
    climate_risk: str
    market_volatility: str
    session_risk: str
    cross_border: bool
    generated_at_utc: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


@dataclass(frozen=True)
class ExpertCard:
    name: str
    specialties: Sequence[str]
    triggers: Sequence[str]
    compliance_dependencies: Sequence[str]
    min_confidence: float
    execution_mode: str


@dataclass(frozen=True)
class PolicyGateResult:
    name: str
    status: str
    details: str


@dataclass(frozen=True)
class ExpertDecision:
    expert: str
    score: float
    rationale: str
    execution_mode: str


@dataclass(frozen=True)
class ExpertOutput:
    expert: str
    summary: str
    confidence: float
    evidence: Sequence[str]
    next_actions: Sequence[str]


@dataclass(frozen=True)
class RankedRecommendation:
    candidate_id: str
    title: str
    geography: str
    category: str
    summary: str
    composite_score: float
    confidence: float
    expert_contributions: Dict[str, float]
    valuation_band: str
    comparable_summary: str
    trend_signal: str
    location_intelligence: str
    recommendation_rationale: str
    why: str
    investment_insight: str
    visa_pathway: str
    insurance_option: str


@dataclass(frozen=True)
class ModelGovernanceStatus:
    framework: str
    status: str
    controls: Sequence[str]
    explanation: str


@dataclass(frozen=True)
class AuditEvent:
    name: str
    status: str
    detail: str
    timestamp_utc: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


@dataclass(frozen=True)
class DecisionPacket:
    request_id: str
    profile: UserProfile
    identity: IdentityContext
    context: RequestContext
    detected_intents: Sequence[str]
    selected_experts: Sequence[ExpertDecision]
    expert_outputs: Sequence[ExpertOutput]
    ranked_recommendations: Sequence[RankedRecommendation]
    policy_gates: Sequence[PolicyGateResult]
    audit_trail: Sequence[AuditEvent]
    recommendation: str
    explanation: str
    release_status: str
    governance_status: Sequence[ModelGovernanceStatus]
    azure_services: Sequence[str]
    standards_alignment: Sequence[str]
    timestamp_utc: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


@dataclass(frozen=True)
class TransactionDocument:
    document_id: str
    name: str
    status: str
    document_type: str
    owner: str
    issues: Sequence[str]
    compliance_tags: Sequence[str]
    last_checked_utc: str


@dataclass(frozen=True)
class TransactionStageStatus:
    stage: str
    status: str
    completion: float
    owner: str
    control_checks: Sequence[str]
    blocker: str = ""


@dataclass(frozen=True)
class DealExpertInsight:
    expert: str
    headline: str
    detail: str
    score: float
    priority: str
    next_action: str


@dataclass(frozen=True)
class ComplianceControlStatus:
    control: str
    framework: str
    status: str
    detail: str
    evidence: Sequence[str]


@dataclass(frozen=True)
class DealWorkflowIntegrity:
    sequential_integrity: str
    audit_status: str
    immutable_event_chain: bool
    continuity_mode: str
    continuity_notes: Sequence[str]


@dataclass(frozen=True)
class TransactionCase:
    transaction_id: str
    deal_name: str
    deal_type: str
    jurisdiction: str
    stage: str
    purchase_price: int
    target_price: int
    financing_ratio: float
    seller_motivation: str
    urgency_days: int
    counterparty_risk: str
    requested_documents: Sequence[TransactionDocument]
    workflow_stages: Sequence[TransactionStageStatus]
    human_approvals: Sequence[str]
    bcdr_tier: str


@dataclass(frozen=True)
class TransactionDecisionPacket:
    request_id: str
    transaction: TransactionCase
    pricing_strategy: DealExpertInsight
    negotiation_insight: DealExpertInsight
    document_validation: DealExpertInsight
    risk_scoring: DealExpertInsight
    overall_risk_score: float
    risk_rating: str
    release_status: str
    workflow_integrity: DealWorkflowIntegrity
    compliance_controls: Sequence[ComplianceControlStatus]
    audit_trail: Sequence[AuditEvent]
    recommendations: Sequence[str]
    explanation: str
    standards_alignment: Sequence[str]
    timestamp_utc: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


@dataclass(frozen=True)
class DigitalTwinInput:
    twin_id: str
    property_name: str
    jurisdiction: str
    property_type: str
    purchase_price: int
    current_value: int
    monthly_rent: int
    occupancy_rate: float
    operating_expense_ratio: float
    annual_insurance_premium: int
    renovation_budget: int
    renovation_uplift: float
    appreciation_rate: float
    financing_ratio: float
    interest_rate: float
    hold_years: int
    climate_risk: str


@dataclass(frozen=True)
class DigitalTwinScenario:
    name: str
    occupancy_rate: float
    monthly_rent: int
    renovation_budget: int
    annual_insurance_premium: int
    annual_noi: int
    annual_cash_flow: int
    cumulative_cash_flow: int
    projected_value: int
    equity_uplift: int
    reliability_score: float
    explanation: str


@dataclass(frozen=True)
class DigitalTwinGovernanceControl:
    framework: str
    status: str
    control: str
    detail: str


@dataclass(frozen=True)
class DigitalTwinDecisionPacket:
    request_id: str
    twin: DigitalTwinInput
    baseline_assumptions: Dict[str, float | int | str]
    scenarios: Sequence[DigitalTwinScenario]
    portfolio_outlook: Sequence[str]
    governance_controls: Sequence[DigitalTwinGovernanceControl]
    explainability_summary: str
    reliability_summary: str
    recommendation: str
    explanation: str
    standards_alignment: Sequence[str]
    timestamp_utc: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


@dataclass(frozen=True)
class MarketDataStream:
    source: str
    cadence: str
    coverage: str
    freshness_sla: str
    features: Sequence[str]


@dataclass(frozen=True)
class MarketIndicator:
    name: str
    scope: str
    current_value: str
    direction: str
    impact: str
    explanation: str


@dataclass(frozen=True)
class ForecastScenario:
    horizon: str
    price_growth: float
    rent_growth: float
    cap_rate_shift_bps: int
    demand_outlook: str
    migration_pressure: str
    confidence: float
    explanation: str


@dataclass(frozen=True)
class MarketAlert:
    title: str
    severity: str
    signal: str
    action: str


@dataclass(frozen=True)
class ModelPipelineStatus:
    stage: str
    status: str
    detail: str


@dataclass(frozen=True)
class MarketIntelligencePacket:
    request_id: str
    market_scope: str
    investment_horizon_months: int
    strategy_bias: str
    data_streams: Sequence[MarketDataStream]
    indicators: Sequence[MarketIndicator]
    forecasts: Sequence[ForecastScenario]
    alerts: Sequence[MarketAlert]
    pipeline_status: Sequence[ModelPipelineStatus]
    signal_summary: str
    recommendation: str
    explanation: str
    standards_alignment: Sequence[str]
    timestamp_utc: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


@dataclass(frozen=True)
class InsuranceApplicantProfile:
    applicant_id: str
    persona: str
    property_type: str
    occupancy: str
    transaction_context: str
    property_jurisdiction: str
    estimated_property_value: int
    mortgage_amount: int
    household_size: int
    dependents: int
    landlord_exposure: bool
    title_required: bool
    life_priority: bool
    prior_claims_count: int
    privacy_consent: bool


@dataclass(frozen=True)
class ACORDParty:
    role: str
    name: str
    identifier: str


@dataclass(frozen=True)
class ACORDCoverageRequest:
    line_of_business: str
    acord_form: str
    coverage_type: str
    insured_amount: int
    deductible: int
    notes: str


@dataclass(frozen=True)
class SecureExchangeControl:
    control: str
    status: str
    detail: str


@dataclass(frozen=True)
class InsuranceRecommendation:
    coverage_type: str
    recommendation_level: str
    policy_form: str
    premium_estimate: str
    rationale: str
    acord_payload_refs: Sequence[str]


@dataclass(frozen=True)
class InsuranceDecisionPacket:
    request_id: str
    applicant: InsuranceApplicantProfile
    acord_parties: Sequence[ACORDParty]
    acord_coverages: Sequence[ACORDCoverageRequest]
    recommendations: Sequence[InsuranceRecommendation]
    secure_exchange_controls: Sequence[SecureExchangeControl]
    naic_privacy_summary: str
    secure_exchange_summary: str
    release_status: str
    explanation: str
    standards_alignment: Sequence[str]
    timestamp_utc: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


@dataclass(frozen=True)
class PaymentParticipant:
    role: str
    name: str
    identifier: str


@dataclass(frozen=True)
class PaymentInstrument:
    instrument_type: str
    token_provider: str
    token_reference: str
    last4: str
    network: str
    wallet_or_bank: str
    pci_scope: str


@dataclass(frozen=True)
class PaymentSignal:
    category: str
    status: str
    detail: str


@dataclass(frozen=True)
class EscrowCondition:
    condition: str
    status: str
    detail: str


@dataclass(frozen=True)
class ReconciliationEntry:
    entry_type: str
    status: str
    detail: str


@dataclass(frozen=True)
class PaymentRequest:
    transaction_reference: str
    payer_id: str
    payment_method_type: str
    amount: int
    currency: str
    cross_border: bool
    escrow_stage: str
    trusted_device: bool
    settlement_timing: str
    manual_review_requested: bool
    chargeback_history_count: int


@dataclass(frozen=True)
class PaymentDecisionPacket:
    request_id: str
    transaction_reference: str
    payment_instrument: PaymentInstrument
    participants: Sequence[PaymentParticipant]
    fraud_probability: float
    risk_level: str
    payment_behavior_summary: str
    escrow_status: str
    frontend_security_posture: str
    signals: Sequence[PaymentSignal]
    escrow_conditions: Sequence[EscrowCondition]
    reconciliation_entries: Sequence[ReconciliationEntry]
    recommended_actions: Sequence[str]
    release_status: str
    explanation: str
    standards_alignment: Sequence[str]
    timestamp_utc: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


@dataclass(frozen=True)
class TokenizationAsset:
    asset_id: str
    property_name: str
    jurisdiction: str
    legal_wrapper: str
    domicile: str
    asset_value: int
    valuation_basis: str
    currency: str
    minimum_investment: int
    target_raise: int
    unit_price: int
    total_units: int
    sponsor_equity_pct: float
    retail_allocation_pct: float
    lockup_period_days: int
    transfer_policy: str


@dataclass(frozen=True)
class TokenizationComplianceCheck:
    name: str
    status: str
    detail: str


@dataclass(frozen=True)
class FractionalOwnershipRecord:
    investor_label: str
    investor_class: str
    beneficial_owner_reference: str
    wallet_reference: str
    units: int
    ownership_pct: float
    status: str


@dataclass(frozen=True)
class TokenizationLedgerEvent:
    event_type: str
    status: str
    detail: str


@dataclass(frozen=True)
class TokenizationDecisionPacket:
    request_id: str
    asset: TokenizationAsset
    offering_status: str
    eligibility_summary: str
    distribution_policy: str
    compliance_checks: Sequence[TokenizationComplianceCheck]
    ownership_records: Sequence[FractionalOwnershipRecord]
    ledger_events: Sequence[TokenizationLedgerEvent]
    recommended_actions: Sequence[str]
    release_status: str
    explanation: str
    standards_alignment: Sequence[str]
    timestamp_utc: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


@dataclass(frozen=True)
class GovernedDocument:
    document_id: str
    document_type: str
    title: str
    jurisdiction: str
    source_system: str
    language: str
    status: str
    confidence: float


@dataclass(frozen=True)
class DocumentFieldExtraction:
    document_id: str
    field_name: str
    field_value: str
    confidence: float
    normalized_value: str
    rationale: str


@dataclass(frozen=True)
class DocumentValidationCheck:
    document_id: str
    check_name: str
    status: str
    detail: str
    severity: str


@dataclass(frozen=True)
class DocumentAnomalySignal:
    signal: str
    severity: str
    affected_documents: Sequence[str]
    detail: str
    recommended_action: str


@dataclass(frozen=True)
class DocumentComplianceFinding:
    framework: str
    control: str
    status: str
    detail: str


@dataclass(frozen=True)
class DocumentAuditRecord:
    event: str
    actor: str
    detail: str
    timestamp_utc: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


@dataclass(frozen=True)
class DocumentIntelligencePacket:
    request_id: str
    portfolio_name: str
    simplified_summary: str
    reasoning_summary: str
    frontend_insights: Sequence[str]
    governed_documents: Sequence[GovernedDocument]
    extracted_fields: Sequence[DocumentFieldExtraction]
    validation_checks: Sequence[DocumentValidationCheck]
    anomaly_signals: Sequence[DocumentAnomalySignal]
    compliance_findings: Sequence[DocumentComplianceFinding]
    audit_records: Sequence[DocumentAuditRecord]
    release_status: str
    recommended_actions: Sequence[str]
    standards_alignment: Sequence[str]
    timestamp_utc: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


@dataclass(frozen=True)
class PartnerIntegrationRequest:
    partner_system: str
    domain: str
    canonical_contract: str
    payload_summary: str
    requested_action: str
    data_classification: str
    consent_scope: Sequence[str]


@dataclass(frozen=True)
class IntegrationValidationResult:
    control: str
    status: str
    detail: str


@dataclass(frozen=True)
class IntegrationRoutingDecision:
    target: str
    status: str
    detail: str


@dataclass(frozen=True)
class IntegrationDecisionPacket:
    request_id: str
    partner_system: str
    domain: str
    canonical_contract: str
    expert_chain: Sequence[str]
    validation_results: Sequence[IntegrationValidationResult]
    routing_decisions: Sequence[IntegrationRoutingDecision]
    compliance_evidence: Sequence[str]
    release_status: str
    explanation: str
    standards_alignment: Sequence[str]
    timestamp_utc: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


@dataclass(frozen=True)
class ResidencyApplicantProfile:
    applicant_id: str
    citizenship_country: str
    current_country: str
    target_jurisdiction: str
    household_size: int
    dependents: int
    annual_income: int
    liquid_assets: int
    property_budget: int
    property_value: int
    source_of_funds_verified: bool
    criminal_record_clear: bool
    health_insurance_ready: bool
    documents_on_file: Sequence[str]


@dataclass(frozen=True)
class ResidencyRule:
    program_name: str
    jurisdiction: str
    pathway_type: str
    minimum_property_value: int
    minimum_annual_income: int
    minimum_liquid_assets: int
    financing_allowed: bool
    required_documents: Sequence[str]
    review_documents: Sequence[str]
    compliance_workflow: Sequence[str]
    notes: Sequence[str]


@dataclass(frozen=True)
class ResidencyRuleCheck:
    name: str
    status: str
    detail: str


@dataclass(frozen=True)
class ResidencyDocumentCheck:
    document: str
    status: str
    detail: str


@dataclass(frozen=True)
class ResidencyComplianceStep:
    step: str
    owner: str
    status: str
    detail: str


@dataclass(frozen=True)
class ResidencyEligibilityPacket:
    request_id: str
    applicant: ResidencyApplicantProfile
    program: str
    jurisdiction: str
    pathway_type: str
    eligibility_status: str
    eligibility_score: float
    rule_checks: Sequence[ResidencyRuleCheck]
    document_checks: Sequence[ResidencyDocumentCheck]
    compliance_workflow: Sequence[ResidencyComplianceStep]
    kyc_aml_summary: str
    privacy_summary: str
    explanation: str
    standards_alignment: Sequence[str]
    timestamp_utc: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


@dataclass(frozen=True)
class RegulatoryDomainNode:
    domain: str
    jurisdiction: str
    regulatory_authorities: Sequence[str]
    workflow_status: str
    guidance_summary: str
    evidence_refs: Sequence[str]


@dataclass(frozen=True)
class WorkflowAdaptation:
    workflow: str
    status: str
    jurisdictions: Sequence[str]
    triggered_by: Sequence[str]
    frontend_guidance: str
    backend_action: str


@dataclass(frozen=True)
class RegulatoryChangeEvent:
    change_id: str
    domain: str
    jurisdiction: str
    change_summary: str
    effective_date: str
    impact_level: str
    monitored_by: Sequence[str]
    action_required: str


@dataclass(frozen=True)
class TransparencyGuidance:
    title: str
    audience: str
    summary: str
    disclosures: Sequence[str]


@dataclass(frozen=True)
class ComplianceGraphPacket:
    request_id: str
    primary_jurisdiction: str
    operating_jurisdictions: Sequence[str]
    graph_version: str
    overall_status: str
    graph_summary: str
    domains: Sequence[RegulatoryDomainNode]
    workflow_adaptations: Sequence[WorkflowAdaptation]
    change_watch: Sequence[RegulatoryChangeEvent]
    transparency_guidance: Sequence[TransparencyGuidance]
    standards_alignment: Sequence[str]
    timestamp_utc: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


@dataclass(frozen=True)
class TrustEntityScore:
    entity_id: str
    entity_type: str
    display_name: str
    trust_score: float
    reputation_score: float
    risk_score: float
    trust_band: str
    verification_status: str
    monitoring_status: str
    historical_factors: Sequence[str]
    key_drivers: Sequence[str]
    frontend_signals: Sequence[str]


@dataclass(frozen=True)
class TrustRiskIndicator:
    indicator: str
    severity: str
    source: str
    detail: str
    related_entities: Sequence[str]


@dataclass(frozen=True)
class TrustReputationPacket:
    request_id: str
    network_status: str
    entities: Sequence[TrustEntityScore]
    risk_indicators: Sequence[TrustRiskIndicator]
    frontend_signals: Sequence[str]
    ai_monitoring_summary: str
    compliance_summary: str
    recommended_actions: Sequence[str]
    explanation: str
    standards_alignment: Sequence[str]
    timestamp_utc: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


@dataclass(frozen=True)
class MarketplaceExpertCapability:
    capability: str
    workflow_scope: Sequence[str]
    invocation_mode: str
    release_mode: str


@dataclass(frozen=True)
class MarketplaceProviderListing:
    provider_id: str
    provider_name: str
    provider_type: str
    status: str
    trust_tier: str
    sandbox_mode: str
    deployment_model: str
    supported_jurisdictions: Sequence[str]
    data_classifications: Sequence[str]
    capabilities: Sequence[MarketplaceExpertCapability]
    frontend_surfaces: Sequence[str]
    governance_notes: Sequence[str]


@dataclass(frozen=True)
class MarketplaceControlCheck:
    control: str
    status: str
    detail: str


@dataclass(frozen=True)
class MarketplaceRoutingPolicy:
    policy: str
    outcome: str
    detail: str


@dataclass(frozen=True)
class ExpertMarketplacePacket:
    request_id: str
    marketplace_status: str
    registry_summary: str
    providers: Sequence[MarketplaceProviderListing]
    control_checks: Sequence[MarketplaceControlCheck]
    routing_policies: Sequence[MarketplaceRoutingPolicy]
    frontend_capabilities: Sequence[str]
    governance_summary: str
    compliance_summary: str
    recommended_actions: Sequence[str]
    standards_alignment: Sequence[str]
    timestamp_utc: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


@dataclass(frozen=True)
class CopilotRoleSummary:
    role_key: str
    title: str
    persona: str
    focus: str
    confidence: float
    summary: str


@dataclass(frozen=True)
class CopilotMessage:
    speaker: str
    role: str
    text: str
    sources: Sequence[str]


@dataclass(frozen=True)
class CopilotMemoryItem:
    label: str
    value: str
    source: str
    retention: str


@dataclass(frozen=True)
class CopilotReasoningStep:
    step: str
    experts: Sequence[str]
    detail: str


@dataclass(frozen=True)
class CopilotGuardrail:
    control: str
    status: str
    detail: str


@dataclass(frozen=True)
class CopilotDecisionPacket:
    request_id: str
    active_role: str
    roles: Sequence[CopilotRoleSummary]
    conversation: Sequence[CopilotMessage]
    memory: Sequence[CopilotMemoryItem]
    reasoning_trace: Sequence[CopilotReasoningStep]
    guardrails: Sequence[CopilotGuardrail]
    recommended_actions: Sequence[str]
    explainability_summary: str
    privacy_summary: str
    compliance_summary: str
    natural_language_interfaces: Sequence[str]
    release_status: str
    standards_alignment: Sequence[str]
    timestamp_utc: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


EXPERT_REGISTRY: Sequence[ExpertCard] = (
    ExpertCard(
        name="property_valuation",
        specialties=("valuation", "comparables", "market_position", "trend_analysis", "location_intelligence"),
        triggers=("property", "home", "price", "valuation", "market", "comparables", "trend", "location"),
        compliance_dependencies=("privacy", "data_residency", "model_risk", "data_quality", "explainability"),
        min_confidence=0.58,
        execution_mode="sync",
    ),
    ExpertCard(
        name="investment_analysis",
        specialties=("yield", "irr", "cashflow", "portfolio_fit"),
        triggers=("yield", "return", "roi", "investment", "cashflow"),
        compliance_dependencies=("privacy", "suitability", "model_risk"),
        min_confidence=0.60,
        execution_mode="sync",
    ),
    ExpertCard(
        name="listing_recommendation",
        specialties=("ranking", "preference_matching", "fairness_checks", "explainable_ordering"),
        triggers=("recommend", "rank", "match", "preference", "shortlist"),
        compliance_dependencies=("privacy", "suitability", "fairness", "explainability", "ai_management"),
        min_confidence=0.62,
        execution_mode="sync",
    ),
    ExpertCard(
        name="residency_eligibility",
        specialties=("residency", "visa", "jurisdiction_rules"),
        triggers=("visa", "residency", "citizenship", "migration", "golden visa"),
        compliance_dependencies=("kyc", "aml", "sanctions", "jurisdiction", "data_residency"),
        min_confidence=0.60,
        execution_mode="async",
    ),
    ExpertCard(
        name="insurance_matching",
        specialties=("coverage", "perils", "acord_intake"),
        triggers=("insurance", "coverage", "hazard", "storm", "flood"),
        compliance_dependencies=("privacy", "licensing"),
        min_confidence=0.56,
        execution_mode="async",
    ),
    ExpertCard(
        name="payment_intelligence",
        specialties=("payment risk", "fraud scoring", "escrow", "reconciliation"),
        triggers=("payment", "escrow", "fraud", "settlement", "reconciliation"),
        compliance_dependencies=("privacy", "pci_dss", "aml", "records", "risk_thresholds"),
        min_confidence=0.66,
        execution_mode="sync",
    ),
    ExpertCard(
        name="financial_risk",
        specialties=("affordability", "leverage", "liquidity", "fx_exposure"),
        triggers=("mortgage", "finance", "loan", "affordability", "risk"),
        compliance_dependencies=("privacy", "suitability", "risk_thresholds"),
        min_confidence=0.61,
        execution_mode="sync",
    ),
    ExpertCard(
        name="compliance_validation",
        specialties=("kyc", "aml", "sanctions", "privacy", "records"),
        triggers=("compliance", "kyc", "aml", "sanctions", "regulated"),
        compliance_dependencies=("all",),
        min_confidence=0.80,
        execution_mode="sync",
    ),
    ExpertCard(
        name="unified_compliance_risk_intelligence",
        specialties=(
            "continuous_control_monitoring",
            "cross_workflow_risk_scoring",
            "aml_kyc_enforcement",
            "sanctions_screening",
            "audit_logging",
            "iso_27001_alignment",
            "iso_31000_alignment",
        ),
        triggers=(
            "compliance",
            "risk",
            "aml",
            "kyc",
            "sanctions",
            "audit",
            "payment",
            "insurance",
            "residency",
        ),
        compliance_dependencies=("all",),
        min_confidence=0.84,
        execution_mode="sync",
    ),
    ExpertCard(
        name="market_intelligence",
        specialties=("macro_trends", "migration_flows", "rate_path", "supply_demand", "forecast_signals"),
        triggers=("macro", "forecast", "market", "migration", "rates", "supply", "demand"),
        compliance_dependencies=("privacy", "model_risk", "data_quality", "explainability", "ai_management"),
        min_confidence=0.64,
        execution_mode="async",
    ),
    ExpertCard(
        name="ux_personalization",
        specialties=("journey_guidance", "messaging", "next_best_action"),
        triggers=("help", "next", "summary", "compare", "guide"),
        compliance_dependencies=("privacy",),
        min_confidence=0.52,
        execution_mode="sync",
    ),
    ExpertCard(
        name="conversational_copilot",
        specialties=("natural_language_interface", "context_memory", "role_switching", "explainable_reasoning"),
        triggers=("assistant", "copilot", "chat", "conversation", "explain", "guide"),
        compliance_dependencies=("privacy", "explainability", "records", "ai_management"),
        min_confidence=0.66,
        execution_mode="sync",
    ),
)

TRANSACTION_EXPERTS: Sequence[ExpertCard] = (
    ExpertCard(
        name="pricing_strategy",
        specialties=("offer strategy", "counter analysis", "market timing"),
        triggers=("deal", "offer", "pricing", "counter", "bid"),
        compliance_dependencies=("model_risk", "data_quality", "records"),
        min_confidence=0.68,
        execution_mode="sync",
    ),
    ExpertCard(
        name="negotiation_insights",
        specialties=("counterparty posture", "concession plan", "stakeholder timing"),
        triggers=("negotiate", "seller", "term", "counter"),
        compliance_dependencies=("records", "privacy", "jurisdiction"),
        min_confidence=0.67,
        execution_mode="sync",
    ),
    ExpertCard(
        name="document_validation",
        specialties=("checklist completeness", "signature readiness", "evidence control"),
        triggers=("document", "contract", "title", "disclosure", "validation"),
        compliance_dependencies=("records", "privacy", "data_residency", "business_continuity"),
        min_confidence=0.75,
        execution_mode="sync",
    ),
    ExpertCard(
        name="deal_risk_scoring",
        specialties=("deal risk", "workflow integrity", "escalation triage"),
        triggers=("risk", "integrity", "approval", "escalation"),
        compliance_dependencies=("risk_thresholds", "records", "business_continuity", "suitability"),
        min_confidence=0.72,
        execution_mode="sync",
    ),
)

INTENT_KEYWORDS: Dict[str, str] = {
    "property": "property_search",
    "home": "property_search",
    "market": "valuation",
    "price": "valuation",
    "valuation": "valuation",
    "yield": "investment",
    "roi": "investment",
    "investment": "investment",
    "forecast": "market_intelligence",
    "macro": "market_intelligence",
    "migration": "market_intelligence",
    "rates": "market_intelligence",
    "supply": "market_intelligence",
    "demand": "market_intelligence",
    "recommend": "recommendation",
    "rank": "recommendation",
    "preference": "recommendation",
    "residency": "residency",
    "visa": "residency",
    "citizenship": "residency",
    "insurance": "insurance",
    "coverage": "insurance",
    "payment": "payment",
    "escrow": "payment",
    "fraud": "payment",
    "settlement": "payment",
    "reconciliation": "payment",
    "mortgage": "finance",
    "loan": "finance",
    "affordability": "finance",
    "risk": "finance",
    "kyc": "compliance",
    "aml": "compliance",
    "sanctions": "compliance",
    "assistant": "copilot",
    "copilot": "copilot",
    "chat": "copilot",
    "conversation": "copilot",
    "explain": "copilot",
}

INTENT_EXPERT_MAP: Dict[str, str] = {
    "property_search": "property_valuation",
    "valuation": "property_valuation",
    "investment": "investment_analysis",
    "recommendation": "listing_recommendation",
    "residency": "residency_eligibility",
    "insurance": "insurance_matching",
    "payment": "payment_intelligence",
    "finance": "financial_risk",
    "compliance": "unified_compliance_risk_intelligence",
    "market_intelligence": "market_intelligence",
    "copilot": "conversational_copilot",
}

POLICY_GATES: Dict[str, str] = {
    "privacy": "Enforce purpose limitation, data minimization, consent propagation, and profile-specific privacy controls.",
    "rbac": "Authorize access with least privilege, role scoping, and entitlement checks before expert invocation or release.",
    "mfa": "Require phishing-resistant MFA for privileged actions, high-risk sessions, and sensitive expert outputs.",
    "kyc": "Confirm identity evidence, beneficial ownership, and document completeness before high-trust actions are released.",
    "aml": "Check source-of-funds completeness, transaction anomaly indicators, and enhanced due diligence thresholds.",
    "sanctions": "Screen sanctioned individuals, entities, PEP relationships, and high-risk geographies before release.",
    "jurisdiction": "Verify local property ownership, residency-by-investment, cross-border disclosure, and servicing rules.",
    "licensing": "Ensure insurance distribution and advisory actions fit the servicing entity permissions.",
    "pci_dss": "Isolate cardholder data, use tokenization, protect payment pages, and log reconciliation activity under PCI DSS controls.",
    "model_risk": "Record model lineage, confidence, bias review, and evaluation thresholds for AI-assisted outputs.",
    "data_quality": "Apply ISO/IEC 5259-aligned controls for data provenance, completeness, freshness, comparability, and traceable remediation.",
    "fairness": "Measure ranking fairness, disparate impact, and preference weighting drift before releasing recommendations.",
    "explainability": "Preserve user-facing reasons, comparable-set rationale, and feature contribution summaries for each decision.",
    "ai_management": "Operate the AI management system under ISO/IEC 42001 with documented ownership, risk treatment, and human oversight.",
    "risk_thresholds": "Block release when fraud, climate, cyber, session, or financial risks exceed threshold.",
    "records": "Write immutable audit logs with inputs, outputs, lineage, approvals, and identity state.",
    "suitability": "Check affordability, investor category, and product suitability against client profile and constraints.",
    "data_residency": "Apply region-aware storage, transfer, retention, and deletion constraints to profile and decision data.",
    "business_continuity": "Preserve workflow continuity with alternate queues, RTO/RPO monitoring, failover runbooks, and transaction recovery evidence.",
}

AZURE_SERVICES: Sequence[str] = (
    "Azure Front Door",
    "Azure API Management",
    "Microsoft Entra External ID",
    "Azure App Service",
    "Azure Kubernetes Service",
    "Azure Database for PostgreSQL",
    "Azure Cache for Redis",
    "Azure Blob Storage",
    "Azure Service Bus",
    "Azure AI Search",
    "Azure Machine Learning",
    "Azure Key Vault",
    "Azure Monitor",
    "Microsoft Sentinel",
    "Defender for Cloud",
)

STANDARDS_ALIGNMENT: Sequence[str] = (
    "ISO/IEC 27001",
    "ISO/IEC 27017",
    "ISO/IEC 27701",
    "PCI DSS",
    "SOC 2 Type 2",
    "ISO/IEC 25010",
    "ISO/IEC 5259",
    "ISO/IEC 42001",
    "ISO 22301",
    "ISO 31000",
    "ISO 9241-210",
)

INTEGRATION_PROFILES = {
    "banking_core": {
        "domain": "banking",
        "expert_chain": ("payment_intelligence", "financial_risk", "compliance_validation"),
        "route_target": "escrow_settlement_orchestrator",
        "fallback_target": "payment_operations_review",
        "controls": (
            "Canonical payment instruction schema validation",
            "Token alias and beneficiary verification",
            "Fraud, sanctions, and approval gate before settlement release",
        ),
        "evidence": (
            "ISO 20022/NACHA field mapping ledger",
            "PCI DSS tokenization boundary evidence",
            "AML/KYC and approval trace",
        ),
    },
    "insurance_exchange": {
        "domain": "insurance",
        "expert_chain": ("insurance_matching", "unified_compliance_risk_intelligence", "compliance_validation"),
        "route_target": "carrier_quote_exchange",
        "fallback_target": "advisor_underwriting_review",
        "controls": (
            "ACORD-style coverage schema validation",
            "Purpose-bound field release and NAIC privacy checks",
            "Hazard and underwriting readiness enrichment",
        ),
        "evidence": (
            "ACORD payload mapping ledger",
            "NAIC-aligned privacy release record",
            "Underwriting readiness trace",
        ),
    },
    "government_registry": {
        "domain": "government",
        "expert_chain": ("residency_eligibility", "document_validation", "compliance_validation"),
        "route_target": "jurisdiction_submission_gateway",
        "fallback_target": "legal_migration_review",
        "controls": (
            "Jurisdiction filing schema and version validation",
            "Document completeness and source-of-funds review",
            "Cross-border privacy and sanctions controls before submission",
        ),
        "evidence": (
            "Jurisdiction schema version ledger",
            "ISO/IEC 27701 cross-border handling evidence",
            "Manual sign-off record for regulated filings",
        ),
    },
}


RESIDENCY_RULES: Dict[str, ResidencyRule] = {
    "Portugal": ResidencyRule(
        program_name="Portugal D7 Residency",
        jurisdiction="Portugal",
        pathway_type="passive-income residency",
        minimum_property_value=0,
        minimum_annual_income=12000,
        minimum_liquid_assets=36000,
        financing_allowed=True,
        required_documents=(
            "passport",
            "proof_of_income",
            "bank_statements",
            "health_insurance",
            "criminal_record",
            "proof_of_address",
        ),
        review_documents=("tax_number", "lease_or_property_deed", "family_dependents_pack"),
        compliance_workflow=(
            "KYC identity verification",
            "AML source-of-funds review",
            "Document authenticity validation",
            "Privacy minimization and consent logging",
            "Manual legal review before submission",
        ),
        notes=(
            "Property purchase can strengthen relocation evidence but is not the minimum eligibility lever.",
            "Income and proof-of-accommodation evidence should be mapped for each dependent.",
        ),
    ),
    "Greece": ResidencyRule(
        program_name="Greece Golden Visa",
        jurisdiction="Greece",
        pathway_type="property-led residency",
        minimum_property_value=250000,
        minimum_annual_income=0,
        minimum_liquid_assets=50000,
        financing_allowed=False,
        required_documents=(
            "passport",
            "property_purchase_agreement",
            "proof_of_funds",
            "health_insurance",
            "criminal_record",
        ),
        review_documents=("land_registry_extract", "tax_number", "family_dependents_pack"),
        compliance_workflow=(
            "KYC identity verification",
            "AML source-of-funds review",
            "Property title and valuation validation",
            "Privacy minimization and consent logging",
            "Manual compliance sign-off before filing",
        ),
        notes=(
            "Financed acquisitions are typically escalated because own-funds evidence must be clear.",
            "Property thresholds can vary by asset type and locality, so local counsel still validates the file.",
        ),
    ),
    "UAE": ResidencyRule(
        program_name="UAE Property Investor Visa",
        jurisdiction="UAE",
        pathway_type="property investor residence",
        minimum_property_value=205000,
        minimum_annual_income=0,
        minimum_liquid_assets=75000,
        financing_allowed=True,
        required_documents=(
            "passport",
            "property_title_deed",
            "proof_of_funds",
            "health_insurance",
            "bank_statements",
        ),
        review_documents=("emirates_id_application_pack", "utility_bill", "family_dependents_pack"),
        compliance_workflow=(
            "KYC identity verification",
            "AML source-of-funds review",
            "Property ownership confirmation",
            "Privacy minimization and consent logging",
            "Operational compliance handoff for visa issuance",
        ),
        notes=(
            "Higher-value tiers may unlock longer-duration residence benefits.",
            "Title deed quality and source-of-funds evidence are usually the main release gates.",
        ),
    ),
}

RECOMMENDATION_CATALOG: Dict[str, Sequence[Dict[str, object]]] = {
    "buyer": (
        {
            "candidate_id": "lisbon-green-quarter",
            "title": "Lisbon Green Quarter Apartment",
            "geography": "Lisbon, Portugal",
            "category": "property",
            "summary": "Family-ready apartment with strong walkability, retrofit upside, and dependable insurance placement.",
            "base_scores": {
                "property_valuation": 0.92,
                "investment_analysis": 0.74,
                "listing_recommendation": 0.93,
                "residency_eligibility": 0.91,
                "insurance_matching": 0.85,
                "financial_risk": 0.84,
                "compliance_validation": 0.95,
                "ux_personalization": 0.86,
            },
            "price": 620000,
            "valuation_band": "$600k-$645k",
            "comparable_summary": "Supported by three central Lisbon family apartment comparables with similar retrofit profiles.",
            "trend_signal": "Urban family stock remains supply-constrained with stable pricing momentum.",
            "location_intelligence": "Strong transit, school access, and low-friction daily mobility improve long-term fit.",
            "recommendation_rationale": "Recommendation expert favors this listing because user preferences, value confidence, and location quality align cleanly.",
            "investment_insight": "Balanced appreciation outlook with resilience under moderate financing stress.",
            "visa_pathway": "Portugal D7 family relocation route is the clearest next step.",
            "insurance_option": "Home, contents, and legal protection bundle with low hazard friction.",
        },
        {
            "candidate_id": "porto-riverside-loft",
            "title": "Porto Riverside Loft",
            "geography": "Porto, Portugal",
            "category": "property",
            "summary": "Flexible lower-cost option with strong affordability and rental fallback support.",
            "base_scores": {
                "property_valuation": 0.83,
                "investment_analysis": 0.77,
                "listing_recommendation": 0.84,
                "residency_eligibility": 0.84,
                "insurance_matching": 0.84,
                "financial_risk": 0.89,
                "compliance_validation": 0.94,
                "ux_personalization": 0.81,
            },
            "price": 540000,
            "valuation_band": "$520k-$555k",
            "comparable_summary": "Backed by lower-entry riverside loft sales and resilient rent-comp comparables.",
            "trend_signal": "Moderate appreciation with stronger affordability retention than premium districts.",
            "location_intelligence": "Transit and rental fallback raise flexibility for mixed family and investment use.",
            "recommendation_rationale": "Recommendation expert places it second because finance fit is excellent but family relocation signals are slightly weaker.",
            "investment_insight": "Best affordability and financing resilience in the buyer catalog.",
            "visa_pathway": "Portugal D7 remains viable, especially when optional rental income matters.",
            "insurance_option": "Standard property protection package with simpler underwriting requirements.",
        },
        {
            "candidate_id": "cascais-coastal-townhome",
            "title": "Cascais Coastal Townhome",
            "geography": "Cascais, Portugal",
            "category": "property",
            "summary": "Premium lifestyle home with appreciation upside and more insurance complexity.",
            "base_scores": {
                "property_valuation": 0.88,
                "investment_analysis": 0.78,
                "listing_recommendation": 0.79,
                "residency_eligibility": 0.87,
                "insurance_matching": 0.69,
                "financial_risk": 0.7,
                "compliance_validation": 0.94,
                "ux_personalization": 0.83,
            },
            "price": 780000,
            "valuation_band": "$745k-$805k",
            "comparable_summary": "Premium coastal townhome comps support value, but insurance-adjusted carrying costs vary more widely.",
            "trend_signal": "Premium submarket demand is healthy, though pricing is more sensitive to macro shocks.",
            "location_intelligence": "Lifestyle appeal is high, but coastal exposure slightly weakens all-weather resilience.",
            "recommendation_rationale": "Recommendation expert penalizes this listing for insurance friction and budget stretch despite strong lifestyle appeal.",
            "investment_insight": "Premium appreciation story, but softer resilience under constrained financing.",
            "visa_pathway": "Portugal relocation still fits, but household cost and protection review are needed.",
            "insurance_option": "Enhanced coastal package with higher premium and more documentation.",
        },
    ),
    "investor": (
        {
            "candidate_id": "athens-urban-block",
            "title": "Athens Urban Residential Block",
            "geography": "Athens, Greece",
            "category": "property",
            "summary": "Income-oriented multifamily opportunity with strong downside resilience and optional residency value.",
            "base_scores": {
                "property_valuation": 0.86,
                "investment_analysis": 0.92,
                "listing_recommendation": 0.9,
                "residency_eligibility": 0.83,
                "insurance_matching": 0.81,
                "financial_risk": 0.86,
                "compliance_validation": 0.94,
                "ux_personalization": 0.78,
            },
            "price": 880000,
            "valuation_band": "$845k-$910k",
            "comparable_summary": "Comparable multifamily-style blocks and stabilized rent rolls support the value range.",
            "trend_signal": "Yield-driven demand remains constructive despite moderate market volatility.",
            "location_intelligence": "Dense urban amenities and diversified occupancy drivers improve resilience.",
            "recommendation_rationale": "Recommendation expert ranks this first because yield, resilience, and diversification best match the investor profile.",
            "investment_insight": "Top blend of yield, occupancy resilience, and diversification in the current set.",
            "visa_pathway": "Greece Golden Visa adjacency is attractive but should be monitored for policy shifts.",
            "insurance_option": "Landlord plus catastrophe cover remains accessible with manageable exclusions.",
        },
        {
            "candidate_id": "lisbon-urban-rental-pair",
            "title": "Lisbon Urban Rental Pair",
            "geography": "Lisbon, Portugal",
            "category": "property",
            "summary": "Balanced dual-asset strategy with efficient financing and optional future owner use.",
            "base_scores": {
                "property_valuation": 0.84,
                "investment_analysis": 0.88,
                "listing_recommendation": 0.85,
                "residency_eligibility": 0.79,
                "insurance_matching": 0.83,
                "financial_risk": 0.87,
                "compliance_validation": 0.95,
                "ux_personalization": 0.8,
            },
            "price": 760000,
            "valuation_band": "$735k-$785k",
            "comparable_summary": "Two-unit Lisbon rental comparables indicate stable income pricing with manageable vacancy assumptions.",
            "trend_signal": "Balanced market momentum with moderate regulatory watchpoints.",
            "location_intelligence": "Central urban access and flexible exit paths support optional future owner use.",
            "recommendation_rationale": "Recommendation expert keeps it near the top because flexibility and capital efficiency are strong.",
            "investment_insight": "Best flexibility and financing efficiency for a balanced portfolio lens.",
            "visa_pathway": "Portugal residency is less central here, but optional relocation remains open.",
            "insurance_option": "Portfolio landlord package with moderate carry and straightforward placement.",
        },
        {
            "candidate_id": "dubai-marina-residence",
            "title": "Dubai Marina Branded Residence",
            "geography": "Dubai, UAE",
            "category": "property",
            "summary": "Premium globally mobile asset with high upside and higher insurance carry.",
            "base_scores": {
                "property_valuation": 0.9,
                "investment_analysis": 0.89,
                "listing_recommendation": 0.76,
                "residency_eligibility": 0.88,
                "insurance_matching": 0.73,
                "financial_risk": 0.75,
                "compliance_validation": 0.93,
                "ux_personalization": 0.79,
            },
            "price": 1200000,
            "valuation_band": "$1.16M-$1.24M",
            "comparable_summary": "Premium branded residence comps confirm upside but with a wider premium-market spread.",
            "trend_signal": "Momentum is favorable yet more cyclical than the Mediterranean income plays.",
            "location_intelligence": "Liquidity and prestige are strong, but FX and carrying cost sensitivity are higher.",
            "recommendation_rationale": "Recommendation expert lowers the rank because premium carry and budget pressure reduce fit.",
            "investment_insight": "Strong upside, but lower resilience when FX and premium operating costs widen.",
            "visa_pathway": "UAE investor residence route is strong for globally mobile investors.",
            "insurance_option": "High-value property coverage with premium documentation requirements.",
        },
    ),
    "advisor": (
        {
            "candidate_id": "barcelona-family-office",
            "title": "Barcelona Family Office Residence",
            "geography": "Barcelona, Spain",
            "category": "property",
            "summary": "Documentation-friendly premium asset with a strong client narrative and controlled downside.",
            "base_scores": {
                "property_valuation": 0.87,
                "investment_analysis": 0.8,
                "listing_recommendation": 0.88,
                "residency_eligibility": 0.76,
                "insurance_matching": 0.86,
                "financial_risk": 0.84,
                "compliance_validation": 0.97,
                "ux_personalization": 0.82,
            },
            "price": 1050000,
            "valuation_band": "$1.01M-$1.08M",
            "comparable_summary": "Premium residence comparables support pricing with strong documentation quality.",
            "trend_signal": "Steady prime-market demand with comparatively controlled downside.",
            "location_intelligence": "Dense services, strong client usability, and clear documentation raise advisor confidence.",
            "recommendation_rationale": "Recommendation expert favors this listing because it is easiest to defend in a suitability-led memo.",
            "investment_insight": "Best suitability story when the client values clarity and documentation quality.",
            "visa_pathway": "Spain residence planning requires current legal review before client release.",
            "insurance_option": "Premium residence package with strong liability and contents coverage.",
        },
        {
            "candidate_id": "athens-balanced-income",
            "title": "Athens Balanced Income Asset",
            "geography": "Athens, Greece",
            "category": "property",
            "summary": "Balanced recommendation that pairs yield support with clearer residency optionality.",
            "base_scores": {
                "property_valuation": 0.84,
                "investment_analysis": 0.89,
                "listing_recommendation": 0.86,
                "residency_eligibility": 0.84,
                "insurance_matching": 0.8,
                "financial_risk": 0.83,
                "compliance_validation": 0.94,
                "ux_personalization": 0.79,
            },
            "price": 890000,
            "valuation_band": "$860k-$915k",
            "comparable_summary": "Income asset comparables and rent rolls support a balanced valuation case.",
            "trend_signal": "Healthy income demand with moderate policy watch exposure.",
            "location_intelligence": "Residency optionality and urban access strengthen client flexibility.",
            "recommendation_rationale": "Recommendation expert keeps this close because yield and residency optionality are both strong.",
            "investment_insight": "Best alternative when client optionality matters more than narrative simplicity.",
            "visa_pathway": "Greece residency planning remains viable with current policy monitoring.",
            "insurance_option": "Residential income package with catastrophe rider and manageable complexity.",
        },
        {
            "candidate_id": "dubai-premium-diversifier",
            "title": "Dubai Premium Diversifier",
            "geography": "Dubai, UAE",
            "category": "property",
            "summary": "High-upside premium asset that only fits aggressive client mandates.",
            "base_scores": {
                "property_valuation": 0.9,
                "investment_analysis": 0.87,
                "listing_recommendation": 0.74,
                "residency_eligibility": 0.89,
                "insurance_matching": 0.71,
                "financial_risk": 0.69,
                "compliance_validation": 0.93,
                "ux_personalization": 0.76,
            },
            "price": 1450000,
            "valuation_band": "$1.39M-$1.49M",
            "comparable_summary": "High-end comparables support the range but with broader volatility bands.",
            "trend_signal": "Premium growth potential is strong, but cyclicality is higher than the peer set.",
            "location_intelligence": "Global mobility is attractive, though cost-to-fit is weakest for conservative advice.",
            "recommendation_rationale": "Recommendation expert places it last because suitability and carrying cost outweigh upside here.",
            "investment_insight": "Advisable only for clients who explicitly accept cyclical exposure and premium operating costs.",
            "visa_pathway": "UAE investor route is compelling but should follow suitability confirmation.",
            "insurance_option": "High-value diversified cover with premium carry and more underwriting evidence.",
        },
    ),
}


def detect_intents(user_prompt: str, profile: UserProfile) -> List[str]:
    prompt = f"{user_prompt} {profile.intent} {profile.financial_intent} {profile.residency_goal}".lower()
    detected = {INTENT_KEYWORDS[keyword] for keyword in INTENT_KEYWORDS if keyword in prompt}
    detected.add("recommendation")
    if profile.residency_interest:
        detected.add("residency")
    if profile.financing_needed:
        detected.add("finance")
    if profile.role == "advisor":
        detected.add("compliance")
    return sorted(detected)


def route_experts(
    user_prompt: str,
    profile: UserProfile,
    identity: IdentityContext,
    context: RequestContext,
    intents: Sequence[str],
) -> List[ExpertDecision]:
    selected: List[ExpertDecision] = []
    prompt = user_prompt.lower()
    for expert in EXPERT_REGISTRY:
        trigger_hits = sum(1 for trigger in expert.triggers if trigger in prompt)
        intent_hit = 1 if expert.name in {INTENT_EXPERT_MAP.get(intent) for intent in intents} else 0
        profile_bonus = 0.04 if expert.name == "residency_eligibility" and profile.residency_interest else 0
        profile_bonus += 0.04 if expert.name == "financial_risk" and profile.financing_needed else 0
        profile_bonus += 0.05 if expert.name in {"compliance_validation", "unified_compliance_risk_intelligence"} and profile.role == "advisor" else 0
        profile_bonus += 0.03 if expert.name == "investment_analysis" and profile.role == "investor" else 0
        profile_bonus += 0.04 if expert.name == "market_intelligence" and profile.role in {"investor", "advisor"} else 0
        context_bonus = 0.03 if context.cross_border and expert.name in {"residency_eligibility", "compliance_validation", "unified_compliance_risk_intelligence"} else 0
        confidence = min(0.99, expert.min_confidence + trigger_hits * 0.05 + intent_hit * 0.08 + profile_bonus + context_bonus)
        if trigger_hits or intent_hit or expert.name in {"compliance_validation", "unified_compliance_risk_intelligence", "ux_personalization"}:
            selected.append(
                ExpertDecision(
                    expert=expert.name,
                    score=round(confidence, 2),
                    rationale=(
                        f"Selected for specialties {list(expert.specialties)} with {trigger_hits} trigger hits, "
                        f"intent alignment={bool(intent_hit)}, profile-aware bonus={profile_bonus:.2f}, context bonus={context_bonus:.2f}."
                    ),
                    execution_mode=expert.execution_mode,
                )
            )
    return sorted(selected, key=lambda item: item.score, reverse=True)


def collect_policy_dependencies(experts: Sequence[ExpertDecision]) -> List[str]:
    dependencies: List[str] = ["rbac", "mfa", "records"]
    registry_map = {expert.name: expert for expert in EXPERT_REGISTRY}
    for selected in experts:
        expert_card = registry_map[selected.expert]
        if "all" in expert_card.compliance_dependencies:
            dependencies.extend(POLICY_GATES.keys())
        else:
            dependencies.extend(expert_card.compliance_dependencies)
    return sorted(set(dependencies))


def evaluate_policy_gates(
    dependencies: Sequence[str],
    profile: UserProfile,
    identity: IdentityContext,
    context: RequestContext,
) -> List[PolicyGateResult]:
    results: List[PolicyGateResult] = []
    for dependency in dependencies:
        status = "passed"
        details = POLICY_GATES[dependency]
        if dependency == "mfa" and not identity.mfa_completed:
            status = "blocked"
            details = "MFA is required for sensitive recommendation release and export actions."
        elif dependency == "rbac" and "decision:view" not in identity.entitlements:
            status = "blocked"
            details = "Required viewing entitlement is missing for this role and journey stage."
        elif dependency == "kyc" and identity.kyc_status not in {"approved", "enhanced_review"}:
            status = "review"
            details = "KYC evidence is incomplete for high-trust property and residency guidance."
        elif dependency == "aml" and identity.aml_risk == "high":
            status = "review"
            details = "AML risk is high, so the packet must be routed to manual review."
        elif dependency == "sanctions" and identity.sanctions_status != "clear":
            status = "blocked"
            details = "Sanctions screening did not clear the subject or related entity."
        elif dependency == "privacy" and not context.has_consent:
            status = "blocked"
            details = "Purpose-bound consent is required before personalization and recommendation release."
        elif dependency == "jurisdiction" and context.cross_border and profile.country == context.property_country:
            status = "review"
            details = "Cross-border routing signal is inconsistent with the property country context."
        elif dependency == "risk_thresholds" and context.session_risk == "high":
            status = "review"
            details = "Session risk exceeded the automated release threshold."
        elif dependency == "data_residency" and context.cross_border and identity.privacy_tier == "restricted":
            status = "review"
            details = "Restricted privacy tier requires jurisdiction-specific storage approval."
        elif dependency == "business_continuity" and context.market_volatility == "high":
            status = "review"
            details = "Heightened volatility requires continuity playbook validation and manual checkpointing."
        results.append(PolicyGateResult(name=dependency, status=status, details=details))
    return results


def build_expert_outputs(
    profile: UserProfile,
    identity: IdentityContext,
    context: RequestContext,
    experts: Sequence[ExpertDecision],
) -> List[ExpertOutput]:
    output_map: Dict[str, ExpertOutput] = {
        "property_valuation": ExpertOutput(
            expert="property_valuation",
            summary="Valuation band and comparable-set quality indicate strong confidence for Mediterranean urban assets.",
            confidence=0.9,
            evidence=(
                "three to five market comparables per candidate",
                "freshness-scored market feed",
                "location intelligence overlay",
            ),
            next_actions=("review comp pack", "confirm valuation assumptions"),
        ),
        "investment_analysis": ExpertOutput(
            expert="investment_analysis",
            summary="Return model favors resilient income and capital preservation over pure premium upside.",
            confidence=0.87,
            evidence=("yield scenario table", "downside stress case", "portfolio fit check"),
            next_actions=("compare downside cases", "review hold-period assumptions"),
        ),
        "listing_recommendation": ExpertOutput(
            expert="listing_recommendation",
            summary="Ranking model blended property fit, return profile, residency, insurance, and fairness checks.",
            confidence=0.89,
            evidence=("weighted expert contributions", "preference matching trace", "ranking fairness diagnostics"),
            next_actions=("inspect ranked rationale", "export shortlist with reasons"),
        ),
        "residency_eligibility": ExpertOutput(
            expert="residency_eligibility",
            summary="Residency pathways remain viable with current KYC posture and target-market assumptions.",
            confidence=0.82,
            evidence=("jurisdiction rules summary", "household evidence checklist", "timeline estimate"),
            next_actions=("collect supporting documents", "monitor program updates"),
        ),
        "insurance_matching": ExpertOutput(
            expert="insurance_matching",
            summary="Coverage options remain placeable with manageable premium variance across top candidates.",
            confidence=0.8,
            evidence=("hazard scoring", "carrier appetite summary", "intake completeness"),
            next_actions=("request quotes", "confirm property disclosures"),
        ),
        "financial_risk": ExpertOutput(
            expert="financial_risk",
            summary="Financing capacity is acceptable under balanced leverage and moderate stress assumptions.",
            confidence=0.84,
            evidence=("budget profile", "leverage ratio", "liquidity reserve check"),
            next_actions=("obtain pre-qualification", "compare financing paths"),
        ),
        "payment_intelligence": ExpertOutput(
            expert="payment_intelligence",
            summary="Payment routing monitors fraud probability, escrow milestones, and reconciliation exceptions before funds move.",
            confidence=0.86,
            evidence=("tokenized payment telemetry", "device and velocity checks", "escrow and settlement ledger"),
            next_actions=("review payment release posture", "clear reconciliation exceptions"),
        ),
        "compliance_validation": ExpertOutput(
            expert="compliance_validation",
            summary="Release gate confirms identity, records, privacy, and screening posture before output release.",
            confidence=0.93,
            evidence=("RBAC evaluation", "MFA state", "KYC/AML state", "audit retention check"),
            next_actions=("preserve evidence bundle", "route exceptions to review"),
        ),
        "unified_compliance_risk_intelligence": ExpertOutput(
            expert="unified_compliance_risk_intelligence",
            summary=(
                "Continuous control monitoring unifies AML/KYC, sanctions screening, audit logging, and cross-domain risk scoring "
                "across property, payment, insurance, and residency workflows."
            ),
            confidence=0.95,
            evidence=(
                "continuous activity risk graph",
                "AML/KYC and sanctions screening ledger",
                "immutable audit event chain",
                "ISO/IEC 27001 and ISO 31000 control mappings",
            ),
            next_actions=("review elevated risk cases", "attach evidence bundle to any held workflow"),
        ),
        "market_intelligence": ExpertOutput(
            expert="market_intelligence",
            summary="Macro intelligence tracks migration, rates, supply absorption, and local demand to emit forward-looking market signals and alerts.",
            confidence=0.88,
            evidence=("global macro feed", "regional migration ledger", "rate-path scenarios", "supply-demand imbalance monitor"),
            next_actions=("review 12-month market signal", "compare base and downside macro scenarios"),
        ),
        "ux_personalization": ExpertOutput(
            expert="ux_personalization",
            summary="Explanation depth and next-best actions were tailored to the current user journey.",
            confidence=0.78,
            evidence=("persona mapping", "journey stage", "explanation depth preference"),
            next_actions=("adjust explanation depth", "surface guided tasks"),
        ),
        "conversational_copilot": ExpertOutput(
            expert="conversational_copilot",
            summary="A multi-role copilot can answer in natural language, preserve short-term context memory, and explain how MoE outputs shaped each answer.",
            confidence=0.88,
            evidence=("role-to-expert routing policy", "conversation memory state", "reasoning trace with cited expert summaries"),
            next_actions=("switch copilot role", "review cited reasoning trace"),
        ),
    }
    return [output_map[item.expert] for item in experts if item.expert in output_map]


def build_ranked_recommendations(
    profile: UserProfile,
    context: RequestContext,
    experts: Sequence[ExpertDecision],
) -> List[RankedRecommendation]:
    catalog_key = profile.role if profile.role in RECOMMENDATION_CATALOG else "buyer"
    expert_scores = {item.expert: item.score for item in experts}
    ranked: List[RankedRecommendation] = []
    for item in RECOMMENDATION_CATALOG[catalog_key]:
        contributions = {
            expert: round(item["base_scores"].get(expert, 0.0) * expert_scores.get(expert, 0.7), 2)
            for expert in item["base_scores"]
        }
        base_average = sum(contributions.values()) / max(len(contributions), 1)
        budget_pressure = max(0.0, (item["price"] - profile.investment_budget) / max(profile.investment_budget, 1))
        volatility_penalty = 0.03 if context.market_volatility == "high" else 0.0
        composite = max(0.0, min(0.99, base_average - budget_pressure * 0.12 - volatility_penalty))
        ranked.append(
            RankedRecommendation(
                candidate_id=str(item["candidate_id"]),
                title=str(item["title"]),
                geography=str(item["geography"]),
                category=str(item["category"]),
                summary=str(item["summary"]),
                composite_score=round(composite, 2),
                confidence=round(min(0.99, composite + 0.04), 2),
                expert_contributions=contributions,
                valuation_band=str(item["valuation_band"]),
                comparable_summary=str(item["comparable_summary"]),
                trend_signal=str(item["trend_signal"]),
                location_intelligence=str(item["location_intelligence"]),
                recommendation_rationale=str(item["recommendation_rationale"]),
                why=(
                    f"{item['title']} scored well because valuation confidence, fit, and governance posture remain strong for a "
                    f"{profile.investor_type} profile in {context.property_country}."
                ),
                investment_insight=str(item["investment_insight"]),
                visa_pathway=str(item["visa_pathway"]),
                insurance_option=str(item["insurance_option"]),
            )
        )
    return sorted(ranked, key=lambda value: value.composite_score, reverse=True)


def build_governance_status(
    profile: UserProfile,
    identity: IdentityContext,
    context: RequestContext,
    policy_results: Sequence[PolicyGateResult],
) -> List[ModelGovernanceStatus]:
    review_required = any(result.status != "passed" for result in policy_results)
    iso_5259_status = "review" if review_required and context.market_volatility == "high" else "active"
    iso_42001_status = "review" if review_required and identity.aml_risk == "high" else "active"
    iso_27001_status = "review" if review_required and context.session_risk == "high" else "active"
    iso_22301_status = "review" if context.market_volatility == "high" or context.session_risk == "high" else "active"
    return [
        ModelGovernanceStatus(
            framework="ISO/IEC 5259",
            status=iso_5259_status,
            controls=(
                "market-data freshness scoring",
                "comparable-set completeness checks",
                "location signal provenance",
                "ranking fairness sampling",
            ),
            explanation=(
                "Data quality governance monitors market feeds, comparables, trend features, and location intelligence "
                "before valuation and ranking outputs are released."
            ),
        ),
        ModelGovernanceStatus(
            framework="ISO/IEC 42001",
            status=iso_42001_status,
            controls=(
                "AI inventory and ownership",
                "human oversight thresholds",
                "explainability ledger",
                "risk treatment and approval workflow",
            ),
            explanation=(
                "The AI management layer records accountable owners, ranking and valuation risks, fairness checks, and "
                "manual review triggers for sensitive releases."
            ),
        ),
        ModelGovernanceStatus(
            framework="ISO/IEC 27001",
            status=iso_27001_status,
            controls=(
                "segregation of duties",
                "least-privilege entitlements",
                "immutable audit evidence",
                "security monitoring with Sentinel",
            ),
            explanation=(
                "Information-security controls verify identity posture, access governance, auditability, and protective monitoring "
                "before EstateOS outputs can be exported or operationalized."
            ),
        ),
        ModelGovernanceStatus(
            framework="ISO 22301",
            status=iso_22301_status,
            controls=(
                "active-active workflow failover",
                "RTO/RPO checkpoints",
                "workflow replay from immutable events",
                "manual continuity runbook",
            ),
            explanation=(
                "Business continuity governance maintains alternate routing paths, replayable event streams, and recovery checkpoints "
                "for critical transaction and advisory workflows."
            ),
        ),
    ]


def build_audit_trail(
    identity: IdentityContext,
    context: RequestContext,
    selected_experts: Sequence[ExpertDecision],
    policy_results: Sequence[PolicyGateResult],
    release_status: str,
) -> List[AuditEvent]:
    selected_names = ", ".join(f"{item.expert}:{item.execution_mode}" for item in selected_experts)
    blocked_or_review = [result.name for result in policy_results if result.status != "passed"]
    return [
        AuditEvent(name="journey.requested", status="completed", detail=f"Request received for {context.channel} channel."),
        AuditEvent(
            name="identity.profile.ingested",
            status="completed",
            detail=(
                f"Profile source={identity.profile_source}, auth_assurance={identity.auth_assurance_level}, "
                f"roles={list(identity.rbac_roles)}, consent_scope={list(identity.consent_scope)}."
            ),
        ),
        AuditEvent(name="context.assembled", status="completed", detail=f"Journey stage={context.journey_stage}, locale={context.locale}."),
        AuditEvent(name="experts.selected", status="completed", detail=f"Selected experts {selected_names}."),
        AuditEvent(name="policy.validation.completed", status=release_status, detail=f"Non-passing gates: {blocked_or_review or ['none']}."),
        AuditEvent(name="audit.packet.persisted", status="completed", detail="Decision packet persisted to evidence store and event stream."),
    ]


def build_recommendation(
    profile: UserProfile,
    identity: IdentityContext,
    selected_experts: Sequence[ExpertDecision],
    ranked_recommendations: Sequence[RankedRecommendation],
    release_status: str,
) -> str:
    expert_names = ", ".join(decision.expert for decision in selected_experts[:6])
    top_recommendation = ranked_recommendations[0] if ranked_recommendations else None
    top_title = top_recommendation.title if top_recommendation else "the top-ranked option"
    if release_status == "blocked":
        return (
            "Hold automated release, surface remediation tasks in the advisor console, and only continue after RBAC, "
            f"identity, privacy, or screening blockers are resolved across {expert_names}."
        )
    if release_status == "human_review":
        return (
            "Release only a limited summary, route the full packet to manual review, and require documented approval before "
            f"revealing sensitive recommendations derived from {expert_names}."
        )
    if profile.role == "investor":
        return (
            f"Deliver a {profile.investor_type} investor brief led by {top_title}, ranking assets by fair value, comparable-set strength, "
            f"risk-adjusted return, location intelligence, residency alignment, insurability, and financing readiness using signals from {expert_names} while honoring "
            f"{identity.privacy_tier} privacy controls."
        )
    if profile.role == "advisor":
        return (
            f"Provide an approval-ready memo centered on {top_title} with expert-by-expert rationale, policy outcomes, assumptions, "
            f"and human override options grounded in {expert_names}."
        )
    return (
        f"Present a guided property decision journey led by {top_title} that combines fair value, comparables, trends, location intelligence, affordability, eligibility, "
        f"insurance, and next steps using {expert_names}."
    )


def explain_packet(packet: DecisionPacket) -> str:
    highest = packet.selected_experts[0] if packet.selected_experts else None
    top_expert_text = (
        f"Top-ranked expert was {highest.expert} at {highest.score:.2f}." if highest else "No experts selected."
    )
    top_recommendation = packet.ranked_recommendations[0] if packet.ranked_recommendations else None
    recommendation_text = (
        f" Top-ranked recommendation was '{top_recommendation.title}' in {top_recommendation.geography} "
        f"with composite score {top_recommendation.composite_score:.2f}."
        if top_recommendation
        else ""
    )
    review_flags = [result.name for result in packet.policy_gates if result.status != "passed"]
    return (
        f"EstateOS ingested frontend profile signals for investor_type '{packet.profile.investor_type}', financial intent "
        f"'{packet.profile.financial_intent}', residency goal '{packet.profile.residency_goal}', and locale '{packet.context.locale}'. "
        f"The request was evaluated with auth assurance '{packet.identity.auth_assurance_level}', MFA={'on' if packet.identity.mfa_completed else 'off'}, "
        f"KYC='{packet.identity.kyc_status}', and sanctions='{packet.identity.sanctions_status}'. {top_expert_text}{recommendation_text} "
        f"The routing layer combined synchronous and asynchronous experts, evaluated {len(packet.policy_gates)} policy gates, "
        f"applied ISO/IEC 5259, ISO/IEC 42001, ISO/IEC 27001, and ISO 22301 governance controls, and ended with release status '{packet.release_status}'. "
        f"Review flags: {review_flags or ['none']}."
    )


def orchestrate(user_prompt: str, profile: UserProfile, identity: IdentityContext, context: RequestContext) -> DecisionPacket:
    intents = detect_intents(user_prompt, profile)
    experts = route_experts(user_prompt, profile, identity, context, intents)
    policy_dependencies = collect_policy_dependencies(experts)
    policy_results = evaluate_policy_gates(policy_dependencies, profile, identity, context)

    if any(result.status == "blocked" for result in policy_results):
        release_status = "blocked"
    elif any(result.status == "review" for result in policy_results):
        release_status = "human_review"
    else:
        release_status = "released"

    expert_outputs = build_expert_outputs(profile, identity, context, experts)
    ranked_recommendations = build_ranked_recommendations(profile, context, experts)
    audit_trail = build_audit_trail(identity, context, experts, policy_results, release_status)
    recommendation = build_recommendation(profile, identity, experts, ranked_recommendations, release_status)
    governance_status = build_governance_status(profile, identity, context, policy_results)

    packet = DecisionPacket(
        request_id=context.request_id,
        profile=profile,
        identity=identity,
        context=context,
        detected_intents=intents,
        selected_experts=experts,
        expert_outputs=expert_outputs,
        ranked_recommendations=ranked_recommendations,
        policy_gates=policy_results,
        audit_trail=audit_trail,
        recommendation=recommendation,
        explanation="",
        release_status=release_status,
        governance_status=governance_status,
        azure_services=AZURE_SERVICES,
        standards_alignment=STANDARDS_ALIGNMENT,
    )
    return DecisionPacket(**{**asdict(packet), "explanation": explain_packet(packet)})


def evaluate_integration_request(
    request: PartnerIntegrationRequest,
    identity: IdentityContext,
    context: RequestContext,
) -> IntegrationDecisionPacket:
    profile = INTEGRATION_PROFILES.get(request.partner_system, INTEGRATION_PROFILES["banking_core"])
    validation_results = [
        IntegrationValidationResult(
            control="Partner domain alignment",
            status="passed" if request.domain == profile["domain"] else "review",
            detail=f"Partner declared domain '{request.domain}' and adapter profile expects '{profile['domain']}'.",
        ),
        IntegrationValidationResult(
            control="Consent and privacy scope",
            status="passed" if bool(request.consent_scope) and context.has_consent else "blocked",
            detail="Payload release requires purpose-bound consent and an active session consent state.",
        ),
        IntegrationValidationResult(
            control="Identity and trust posture",
            status="passed" if identity.mfa_completed and identity.kyc_status == "verified" else "review",
            detail="Step-up MFA and verified identity improve confidence before external partner delivery.",
        ),
        IntegrationValidationResult(
            control="Data classification handling",
            status="passed" if request.data_classification in {"confidential", "restricted", "internal"} else "review",
            detail=f"Payload classification '{request.data_classification}' is checked against partner transport and storage controls.",
        ),
    ]

    routing_decisions = [
        IntegrationRoutingDecision(
            target=str(profile["route_target"]),
            status="release_ready" if all(item.status == "passed" for item in validation_results[:2]) else "conditional_review",
            detail=f"Canonical contract {request.canonical_contract} is routed into the primary adapter when validation and policy checks pass.",
        ),
        IntegrationRoutingDecision(
            target=str(profile["fallback_target"]),
            status="standby",
            detail="Fallback routing preserves interoperability evidence and hands exceptions to the correct human or secondary workflow.",
        ),
    ]

    blocked = any(item.status == "blocked" for item in validation_results)
    release_status = "held" if blocked else "release_ready"
    explanation = (
        f"Integration hub normalized the {request.partner_system} payload into {request.canonical_contract}, "
        f"ran expert chain {', '.join(profile['expert_chain'])}, and produced a {release_status} decision "
        "with schema, trust, privacy, and routing evidence attached."
    )
    return IntegrationDecisionPacket(
        request_id=context.request_id,
        partner_system=request.partner_system,
        domain=request.domain,
        canonical_contract=request.canonical_contract,
        expert_chain=profile["expert_chain"],
        validation_results=validation_results,
        routing_decisions=routing_decisions,
        compliance_evidence=profile["evidence"],
        release_status=release_status,
        explanation=explanation,
        standards_alignment=("ISO/IEC 27001", "ISO/IEC 27701", "ISO/IEC 42001", "PCI DSS"),
    )


def evaluate_residency_eligibility(
    applicant: ResidencyApplicantProfile,
    identity: IdentityContext,
) -> ResidencyEligibilityPacket:
    rule = RESIDENCY_RULES.get(applicant.target_jurisdiction)
    if not rule:
        raise ValueError(f"Unsupported jurisdiction: {applicant.target_jurisdiction}")

    documents_on_file = set(applicant.documents_on_file)
    rule_checks = [
        ResidencyRuleCheck(
            name="property_value",
            status="passed" if applicant.property_value >= rule.minimum_property_value else "review",
            detail=(
                f"Property value {applicant.property_value:,} compared with threshold {rule.minimum_property_value:,}."
                if rule.minimum_property_value
                else "This pathway does not require a minimum property value for baseline eligibility."
            ),
        ),
        ResidencyRuleCheck(
            name="annual_income",
            status="passed" if applicant.annual_income >= rule.minimum_annual_income else "review",
            detail=f"Annual income {applicant.annual_income:,} compared with threshold {rule.minimum_annual_income:,}.",
        ),
        ResidencyRuleCheck(
            name="liquid_assets",
            status="passed" if applicant.liquid_assets >= rule.minimum_liquid_assets else "review",
            detail=f"Liquid assets {applicant.liquid_assets:,} compared with threshold {rule.minimum_liquid_assets:,}.",
        ),
        ResidencyRuleCheck(
            name="source_of_funds",
            status="passed" if applicant.source_of_funds_verified and identity.aml_risk != "high" else "review",
            detail="Source-of-funds evidence is matched with AML posture before release.",
        ),
        ResidencyRuleCheck(
            name="criminal_record",
            status="passed" if applicant.criminal_record_clear else "blocked",
            detail="Criminal record evidence must be clear for filing and downstream partner submission.",
        ),
        ResidencyRuleCheck(
            name="health_insurance",
            status="passed" if applicant.health_insurance_ready else "review",
            detail="Health insurance readiness is checked because consular and residence filing often require coverage.",
        ),
    ]

    document_checks = [
        ResidencyDocumentCheck(
            document=document,
            status="ready" if document in documents_on_file else "missing",
            detail="Document is present in the controlled evidence bundle." if document in documents_on_file else "Document still needs collection or validation.",
        )
        for document in rule.required_documents
    ]
    document_checks.extend(
        ResidencyDocumentCheck(
            document=document,
            status="review" if document in documents_on_file else "recommended",
            detail="Supplemental document is available for accelerated review." if document in documents_on_file else "Supplemental evidence is recommended for smoother counsel review.",
        )
        for document in rule.review_documents
    )

    compliance_workflow = []
    for index, step in enumerate(rule.compliance_workflow):
        if "KYC" in step:
            status = "completed" if identity.kyc_status in {"approved", "enhanced_review"} else "in_progress"
            owner = "Compliance ops"
        elif "AML" in step:
            status = "completed" if applicant.source_of_funds_verified and identity.aml_risk != "high" else "review"
            owner = "AML analyst"
        elif "Privacy" in step:
            status = "completed" if identity.privacy_tier in {"confidential", "restricted"} else "in_progress"
            owner = "Privacy office"
        elif "legal" in step.lower() or "sign-off" in step.lower():
            status = "ready" if all(item.status != "missing" for item in document_checks[: len(rule.required_documents)]) else "blocked"
            owner = "Jurisdiction counsel"
        else:
            status = "ready" if applicant.property_value >= rule.minimum_property_value else "review"
            owner = "Residency operations"
        compliance_workflow.append(
            ResidencyComplianceStep(
                step=f"{index + 1}. {step}",
                owner=owner,
                status=status,
                detail="Workflow is tracked in an auditable queue aligned with KYC/AML and ISO/IEC 27701 privacy controls.",
            )
        )

    passed = sum(1 for item in rule_checks if item.status == "passed")
    reviews = sum(1 for item in rule_checks if item.status == "review")
    missing_docs = sum(1 for item in document_checks if item.status == "missing")

    if any(item.status == "blocked" for item in rule_checks):
        eligibility_status = "ineligible"
    elif reviews or missing_docs:
        eligibility_status = "eligible_with_review"
    else:
        eligibility_status = "eligible"

    score = max(0.0, min(0.99, 0.52 + passed * 0.07 - reviews * 0.04 - missing_docs * 0.03))
    kyc_aml_summary = (
        f"KYC status is {identity.kyc_status}, AML risk is {identity.aml_risk}, sanctions status is {identity.sanctions_status}, "
        f"and source-of-funds verification is {'complete' if applicant.source_of_funds_verified else 'pending'}."
    )
    privacy_summary = (
        f"ISO/IEC 27701-aligned handling keeps residency evidence purpose-bound under the {identity.privacy_tier} privacy tier, "
        "with document minimization, consent-scoped sharing, and retention-aware compliance workflows."
    )
    explanation = (
        f"{rule.program_name} in {rule.jurisdiction} was evaluated for a household of {applicant.household_size} with property value {applicant.property_value:,}, "
        f"annual income {applicant.annual_income:,}, and liquid assets {applicant.liquid_assets:,}. "
        f"Eligibility ended as '{eligibility_status}' because {passed} rule checks passed, {reviews} need review, and {missing_docs} required documents are still missing. "
        f"Compliance workflow steps preserve KYC/AML gates, document authenticity review, and ISO/IEC 27701 privacy controls before any external filing."
    )

    return ResidencyEligibilityPacket(
        request_id=f"res-{uuid.uuid4().hex[:8]}",
        applicant=applicant,
        program=rule.program_name,
        jurisdiction=rule.jurisdiction,
        pathway_type=rule.pathway_type,
        eligibility_status=eligibility_status,
        eligibility_score=round(score, 2),
        rule_checks=rule_checks,
        document_checks=document_checks,
        compliance_workflow=compliance_workflow,
        kyc_aml_summary=kyc_aml_summary,
        privacy_summary=privacy_summary,
        explanation=explanation,
        standards_alignment=("KYC/AML", "ISO/IEC 27701", "ISO/IEC 27001", "ISO 22301"),
    )


def evaluate_compliance_graph(
    profile: UserProfile,
    identity: IdentityContext,
    context: RequestContext,
    transaction: TransactionCase,
    payment: PaymentDecisionPacket,
    insurance: InsuranceDecisionPacket,
    residency: ResidencyEligibilityPacket,
) -> ComplianceGraphPacket:
    jurisdictions = tuple(dict.fromkeys((context.property_country, transaction.jurisdiction, residency.jurisdiction, profile.country)))
    payment_watch = "elevated" if payment.risk_level in {"high_review", "High review"} or payment.fraud_probability >= 0.5 else "controlled"
    residency_watch = "watch" if residency.eligibility_status != "eligible" else "stable"
    transaction_watch = "watch" if transaction.stage in {"document_validation", "approval"} else "stable"

    domains = (
        RegulatoryDomainNode(
            domain="real_estate",
            jurisdiction=transaction.jurisdiction,
            regulatory_authorities=("Land registry", "Municipal planning office", "Transaction counsel"),
            workflow_status="review" if transaction_watch == "watch" else "active",
            guidance_summary=(
                "Closing remains jurisdiction-aware: permit completeness, title evidence, seller disclosures, and notarization sequencing are "
                "validated before any downstream release or funds movement."
            ),
            evidence_refs=("title_report", "seller_disclosure_pack", "closing_control_matrix"),
        ),
        RegulatoryDomainNode(
            domain="payments",
            jurisdiction=profile.country,
            regulatory_authorities=("PSP risk desk", "Internal AML operations", "Escrow operations"),
            workflow_status="review" if payment_watch == "elevated" else "active",
            guidance_summary=(
                "Payment orchestration adapts to settlement geography, escrow stage, sanctions posture, and fraud probability so release rules "
                "can tighten automatically for cross-border or high-value movement."
            ),
            evidence_refs=("psp_token_reference", "fraud_signal_trace", "escrow_release_controls"),
        ),
        RegulatoryDomainNode(
            domain="insurance",
            jurisdiction=context.property_country,
            regulatory_authorities=("Carrier underwriting", "Privacy office", "Servicing operations"),
            workflow_status="active" if insurance.release_status == "ready" else "review",
            guidance_summary=(
                "Insurance exchange stays aligned to ACORD-style payloads, purpose-bound disclosures, and jurisdiction-specific underwriting "
                "expectations before quote, bind, or policy servicing actions are allowed."
            ),
            evidence_refs=("acord_payload_bundle", "underwriting_notes", "privacy_scope_record"),
        ),
        RegulatoryDomainNode(
            domain="residency",
            jurisdiction=residency.jurisdiction,
            regulatory_authorities=("Immigration counsel", "Residency operations", "Government filing adapter"),
            workflow_status="review" if residency_watch == "watch" else "active",
            guidance_summary=(
                "Residency workflows adapt to program thresholds, supporting documents, privacy scope, and legal sign-off so applicants see "
                "transparent eligibility guidance before any filing package is assembled."
            ),
            evidence_refs=("eligibility_rule_checks", "document_bundle", "filing_workflow_state"),
        ),
    )

    workflow_adaptations = (
        WorkflowAdaptation(
            workflow="property_release",
            status="gated",
            jurisdictions=(transaction.jurisdiction,),
            triggered_by=("document completeness", "jurisdiction disclosure rules", "approval segregation"),
            frontend_guidance="Show permit and disclosure blockers before users can export, submit an offer, or release closing instructions.",
            backend_action="Keep recommendation release and transaction stage progression behind document and approval policy gates.",
        ),
        WorkflowAdaptation(
            workflow="insurance_quote_exchange",
            status="adaptive",
            jurisdictions=(context.property_country,),
            triggered_by=("occupancy profile", "privacy tier", "carrier payload requirements"),
            frontend_guidance="Explain why certain coverages, exclusions, or extra documents are required in the selected jurisdiction.",
            backend_action="Transform quote requests into ACORD-compatible payloads and suppress fields outside consent scope.",
        ),
        WorkflowAdaptation(
            workflow="payment_release",
            status="adaptive",
            jurisdictions=(profile.country, transaction.jurisdiction),
            triggered_by=("fraud probability", "cross-border status", "escrow milestone readiness"),
            frontend_guidance="Surface payment risk, approval state, and escrow readiness in plain language before funds move.",
            backend_action="Escalate to manual review or dual approval when geography, amount, or fraud signals exceed threshold.",
        ),
        WorkflowAdaptation(
            workflow="residency_filing",
            status="gated" if residency.eligibility_status != "eligible" else "ready",
            jurisdictions=(residency.jurisdiction,),
            triggered_by=("program thresholds", "document readiness", "source-of-funds evidence"),
            frontend_guidance="Tell applicants exactly which eligibility checks passed, what is missing, and why counsel review is still required.",
            backend_action="Assemble filing packets only when required rules, KYC/AML checks, and evidence bundles are satisfied.",
        ),
    )

    change_watch = (
        RegulatoryChangeEvent(
            change_id="chg-real-estate-disclosure",
            domain="real_estate",
            jurisdiction=transaction.jurisdiction,
            change_summary="Disclosure packet and permit attachment versions are continuously versioned for closing-readiness checks.",
            effective_date="2026-03-01",
            impact_level="medium",
            monitored_by=("compliance_expert", "document_expert", "transaction_service"),
            action_required="Re-run document completeness and counsel review whenever a new municipal disclosure template is detected.",
        ),
        RegulatoryChangeEvent(
            change_id="chg-payments-cross-border",
            domain="payments",
            jurisdiction=profile.country,
            change_summary="Cross-border escrow and sanctions controls are tracked so payment review thresholds can tighten without frontend rewrites.",
            effective_date="2026-02-15",
            impact_level="high" if payment_watch == "elevated" else "medium",
            monitored_by=("fraud_expert", "payment_service", "compliance_service"),
            action_required="Increase manual review and beneficiary verification when risk signals or geography change.",
        ),
        RegulatoryChangeEvent(
            change_id="chg-insurance-underwriting",
            domain="insurance",
            jurisdiction=context.property_country,
            change_summary="Carrier intake schemas and privacy disclosures are versioned so quote exchanges remain jurisdiction-aware.",
            effective_date="2026-02-20",
            impact_level="medium",
            monitored_by=("insurance_expert", "integration_service", "privacy_office"),
            action_required="Refresh ACORD mappings and update user-facing guidance when underwriting fields or disclosures change.",
        ),
        RegulatoryChangeEvent(
            change_id="chg-residency-program",
            domain="residency",
            jurisdiction=residency.jurisdiction,
            change_summary="Residency pathway thresholds, filing steps, and legal review requirements are monitored as a living rule set.",
            effective_date="2026-03-10",
            impact_level="high" if residency_watch == "watch" else "medium",
            monitored_by=("visa_expert", "government_registry_adapter", "compliance_service"),
            action_required="Re-score eligibility and update the applicant checklist whenever program rules or filing requirements change.",
        ),
    )

    transparency_guidance = (
        TransparencyGuidance(
            title="User-facing compliance guidance",
            audience="frontend user",
            summary="The UI should explain which jurisdictional checks affect offers, payments, insurance requests, and residency filings without exposing sensitive evidence.",
            disclosures=(
                "Show the active jurisdiction and domain-specific status for real estate, payments, insurance, and residency.",
                "Translate controls into plain-language next steps, blockers, and required documents.",
                "Disclose when a workflow is held for review because of policy, not product failure.",
            ),
        ),
        TransparencyGuidance(
            title="Operator adaptation guidance",
            audience="backend operations",
            summary="Backend services should consume the graph as a policy surface that can change routing, gating, payload shaping, and human-review requirements by jurisdiction.",
            disclosures=(
                "Version all rule changes and keep them linked to audit evidence.",
                "Apply least-privilege data shaping before partner or government release.",
                "Trigger event-driven re-evaluation when payment, residency, insurance, or property regulations evolve.",
            ),
        ),
    )

    review_count = sum(1 for item in domains if item.workflow_status == "review")
    overall_status = "review" if review_count >= 2 or payment_watch == "elevated" else "active"
    graph_summary = (
        f"Compliance graph v2026.03 tracks {len(domains)} regulatory domains across {len(jurisdictions)} jurisdictions for "
        f"{profile.country} → {context.property_country} workflows. Current posture is '{overall_status}' because transaction stage "
        f"is {transaction.stage}, payment risk is {payment.risk_level}, insurance release is {insurance.release_status}, and residency "
        f"status is {residency.eligibility_status}. Workflow adaptations keep frontend guidance transparent while backend routing, "
        "payload shaping, and release gates remain jurisdiction-aware."
    )

    return ComplianceGraphPacket(
        request_id=f"cmp-{uuid.uuid4().hex[:8]}",
        primary_jurisdiction=context.property_country,
        operating_jurisdictions=jurisdictions,
        graph_version="2026.03",
        overall_status=overall_status,
        graph_summary=graph_summary,
        domains=domains,
        workflow_adaptations=workflow_adaptations,
        change_watch=change_watch,
        transparency_guidance=transparency_guidance,
        standards_alignment=(
            "ISO/IEC 27001",
            "ISO/IEC 27701",
            "ISO/IEC 42001",
            "PCI DSS",
            "ACORD",
            "KYC/AML/sanctions",
        ),
    )


def _band_from_score(score: float) -> str:
    if score >= 0.82:
        return "high"
    if score >= 0.64:
        return "moderate"
    return "watch"


def evaluate_trust_reputation_network(
    profile: UserProfile,
    identity: IdentityContext,
    context: RequestContext,
    transaction: TransactionCase,
    payment: PaymentDecisionPacket,
    document_packet: DocumentIntelligencePacket,
    compliance_graph: ComplianceGraphPacket,
) -> TrustReputationPacket:
    verified_docs = sum(1 for doc in transaction.requested_documents if doc.status == "validated")
    total_docs = len(transaction.requested_documents) or 1
    document_issue_count = sum(len(doc.issues) for doc in transaction.requested_documents)
    anomaly_weight = sum(0.12 if signal.severity == "high" else 0.07 for signal in document_packet.anomaly_signals)
    review_domains = sum(1 for domain in compliance_graph.domains if domain.workflow_status == "review")
    approval_completion = sum(stage.completion for stage in transaction.workflow_stages) / (len(transaction.workflow_stages) or 1)
    broker_owned_reviews = sum(1 for doc in transaction.requested_documents if doc.owner == "Broker" and doc.status != "validated")

    user_trust = max(
        0.25,
        min(
            0.98,
            0.58
            + (0.12 if identity.mfa_completed else -0.08)
            + (0.11 if identity.kyc_status == "approved" else -0.12)
            + (0.05 if context.has_verified_identity else -0.10)
            + (0.04 if identity.aml_risk == "low" else 0.0 if identity.aml_risk == "medium" else -0.12)
            + (0.05 if identity.sanctions_status == "clear" else -0.30),
        ),
    )
    user_reputation = max(
        0.30,
        min(
            0.97,
            0.55
            + (0.10 if context.has_consent else -0.06)
            + (0.08 if context.channel == "web" else 0.03)
            + (0.05 if "personalization" in identity.consent_scope else 0.0)
            + (0.04 if profile.risk_tolerance in {"balanced", "moderate"} else 0.0),
        ),
    )
    user_risk = max(0.05, min(0.92, 1.0 - ((user_trust * 0.6) + (user_reputation * 0.4))))

    property_trust = max(
        0.22,
        min(
            0.95,
            0.48
            + (verified_docs / total_docs) * 0.22
            - document_issue_count * 0.04
            - anomaly_weight
            - (0.08 if context.climate_risk in {"high", "severe"} else 0.03 if context.climate_risk == "medium" else 0.0)
            - (0.05 if context.market_volatility == "high" else 0.0),
        ),
    )
    property_reputation = max(
        0.25,
        min(
            0.94,
            0.46
            + (0.15 if document_packet.release_status == "review_required" else 0.08)
            + (0.07 if transaction.counterparty_risk == "medium" else 0.0 if transaction.counterparty_risk == "low" else -0.08)
            + (0.05 if compliance_graph.overall_status == "active" else -0.05),
        ),
    )
    property_risk = max(0.08, min(0.96, 1.0 - ((property_trust * 0.65) + (property_reputation * 0.35))))

    broker_trust = max(
        0.20,
        min(
            0.94,
            0.52
            + approval_completion * 0.16
            - broker_owned_reviews * 0.08
            - (0.06 if transaction.stage in {"document_validation", "approval"} else 0.0)
            + (0.05 if review_domains <= 1 else -0.04),
        ),
    )
    broker_reputation = max(
        0.24,
        min(
            0.95,
            0.5
            + (0.12 if transaction.urgency_days >= 21 else 0.05)
            + (0.08 if transaction.seller_motivation in {"measured", "flexible"} else 0.0)
            - document_issue_count * 0.03,
        ),
    )
    broker_risk = max(0.08, min(0.95, 1.0 - ((broker_trust * 0.55) + (broker_reputation * 0.45))))

    transaction_trust = max(
        0.18,
        min(
            0.93,
            0.50
            + approval_completion * 0.14
            - payment.fraud_probability * 0.22
            - anomaly_weight
            - review_domains * 0.05,
        ),
    )
    transaction_reputation = max(
        0.22,
        min(
            0.94,
            0.49
            + (0.12 if payment.escrow_status == "ready" else 0.03)
            + (0.08 if payment.release_status in {"released", "review"} else -0.08)
            + (0.06 if compliance_graph.overall_status == "active" else -0.06),
        ),
    )
    transaction_risk = max(0.10, min(0.98, 1.0 - ((transaction_trust * 0.6) + (transaction_reputation * 0.4))))

    entities = (
        TrustEntityScore(
            entity_id=identity.subject_id,
            entity_type="user",
            display_name=f"{profile.role.title()} profile",
            trust_score=round(user_trust, 2),
            reputation_score=round(user_reputation, 2),
            risk_score=round(user_risk, 2),
            trust_band=_band_from_score(user_trust),
            verification_status="verified" if identity.kyc_status == "approved" and identity.sanctions_status == "clear" else "review",
            monitoring_status="continuous",
            historical_factors=(
                "Identity is bound to an authenticated subject with MFA.",
                "Consent scope includes personalization and evidence retention.",
                f"AML posture is {identity.aml_risk} with sanctions status '{identity.sanctions_status}'.",
            ),
            key_drivers=(
                "KYC outcome",
                "MFA completion",
                "Consent scope",
                "AML/sanctions posture",
            ),
            frontend_signals=(
                "Verified identity badge",
                "Trust band chip",
                "Explainable compliance tooltip",
            ),
        ),
        TrustEntityScore(
            entity_id=transaction.transaction_id + "-property",
            entity_type="property",
            display_name=transaction.deal_name,
            trust_score=round(property_trust, 2),
            reputation_score=round(property_reputation, 2),
            risk_score=round(property_risk, 2),
            trust_band=_band_from_score(property_trust),
            verification_status="document_review" if document_issue_count else "verified",
            monitoring_status="event_driven",
            historical_factors=(
                f"{verified_docs}/{total_docs} requested documents are currently validated.",
                f"{len(document_packet.anomaly_signals)} document anomaly signals were raised by the AI review pipeline.",
                f"Climate risk is '{context.climate_risk}' and market volatility is '{context.market_volatility}'.",
            ),
            key_drivers=(
                "Document validation history",
                "Anomaly detection",
                "Climate and market risk",
                "Counterparty posture",
            ),
            frontend_signals=(
                "Property trust meter",
                "Document verification banner",
                "Risk disclosure card",
            ),
        ),
        TrustEntityScore(
            entity_id="broker-of-record",
            entity_type="broker",
            display_name="Broker of record",
            trust_score=round(broker_trust, 2),
            reputation_score=round(broker_reputation, 2),
            risk_score=round(broker_risk, 2),
            trust_band=_band_from_score(broker_trust),
            verification_status="supervised",
            monitoring_status="workflow_bound",
            historical_factors=(
                f"Average workflow completion is {approval_completion:.0%} across {len(transaction.workflow_stages)} tracked stages.",
                f"Broker-owned review items currently total {broker_owned_reviews}.",
                "Audit and segregation-of-duties checks remain attached to approval stages.",
            ),
            key_drivers=(
                "Workflow completion history",
                "Document stewardship backlog",
                "Approval-control adherence",
                "Operational urgency",
            ),
            frontend_signals=(
                "Broker reputation badge",
                "Response quality label",
                "Escalation availability status",
            ),
        ),
        TrustEntityScore(
            entity_id=transaction.transaction_id,
            entity_type="transaction",
            display_name=f"{transaction.deal_name} transaction",
            trust_score=round(transaction_trust, 2),
            reputation_score=round(transaction_reputation, 2),
            risk_score=round(transaction_risk, 2),
            trust_band=_band_from_score(transaction_trust),
            verification_status="ready" if payment.release_status == "released" else "review",
            monitoring_status="continuous_ai_and_compliance",
            historical_factors=(
                f"Payment fraud probability is {payment.fraud_probability:.2f} with escrow status '{payment.escrow_status}'.",
                f"{review_domains} compliance domains are currently in review state.",
                f"Transaction stage is '{transaction.stage}' with release status '{payment.release_status}'.",
            ),
            key_drivers=(
                "Payment and escrow history",
                "Compliance graph posture",
                "Document anomaly load",
                "Stage progression integrity",
            ),
            frontend_signals=(
                "Closing trust status",
                "Settlement readiness chip",
                "Continuous monitoring indicator",
            ),
        ),
    )

    risk_indicators = (
        TrustRiskIndicator(
            indicator="document_anomaly_pressure",
            severity="high" if anomaly_weight >= 0.12 else "medium",
            source="document_intelligence_expert",
            detail="AI document review detected anomalies or missing evidence that should keep property and transaction trust signals in a monitored state.",
            related_entities=("property", "transaction", "broker"),
        ),
        TrustRiskIndicator(
            indicator="payment_and_settlement_risk",
            severity="high" if payment.fraud_probability >= 0.55 else "medium" if payment.fraud_probability >= 0.35 else "low",
            source="payment_intelligence",
            detail="Fraud probability, device trust, and escrow readiness continuously adjust transaction trust and release gating.",
            related_entities=("user", "transaction"),
        ),
        TrustRiskIndicator(
            indicator="jurisdictional_compliance_review",
            severity="high" if compliance_graph.overall_status == "review" else "medium",
            source="compliance_graph",
            detail="Jurisdiction-aware policy reviews feed the trust network so frontend badges stay aligned with backend compliance state.",
            related_entities=("property", "broker", "transaction"),
        ),
    )

    frontend_signals = (
        "Expose user, property, broker, and transaction trust bands with drill-down explanations.",
        "Render verification badges only when backend verification_status is verified, ready, or supervised.",
        "Show live risk chips for document review, payment review, and compliance review without exposing sensitive evidence.",
        "Let users expand 'Why this trust score?' panels sourced from key drivers and historical factors.",
    )
    recommended_actions = (
        "Re-run trust scoring whenever document validation, payment review, or compliance graph status changes.",
        "Escalate broker and transaction entities to human review when risk_score exceeds 0.45 or any high severity risk indicator appears.",
        "Persist score history for trend analysis so the network reflects longitudinal behavior, not only the latest session snapshot.",
    )

    network_status = "review" if any(entity.risk_score >= 0.4 for entity in entities) or compliance_graph.overall_status == "review" else "stable"
    ai_monitoring_summary = (
        f"AI monitoring correlates document anomalies ({len(document_packet.anomaly_signals)}), payment fraud probability ({payment.fraud_probability:.2f}), "
        f"and {review_domains} reviewed compliance domains into a network status of '{network_status}'."
    )
    compliance_summary = (
        f"Trust scoring remains bound to KYC='{identity.kyc_status}', AML='{identity.aml_risk}', sanctions='{identity.sanctions_status}', "
        f"privacy tier '{identity.privacy_tier}', and compliance graph status '{compliance_graph.overall_status}'."
    )
    explanation = (
        "The trust, reputation, and risk scoring network synthesizes historical workflow behavior, verification posture, AI monitoring, AI anomaly detection, "
        "payment and escrow intelligence, and jurisdiction-aware compliance reviews into explainable scores for the user, property, broker, and transaction. "
        "Frontend trust signals stay lightweight and understandable, while backend services keep the authoritative monitoring, rescoring, and release gating."
    )

    return TrustReputationPacket(
        request_id=f"trn-{uuid.uuid4().hex[:8]}",
        network_status=network_status,
        entities=entities,
        risk_indicators=risk_indicators,
        frontend_signals=frontend_signals,
        ai_monitoring_summary=ai_monitoring_summary,
        compliance_summary=compliance_summary,
        recommended_actions=recommended_actions,
        explanation=explanation,
        standards_alignment=(
            "ISO/IEC 27001",
            "ISO/IEC 27701",
            "ISO/IEC 42001",
            "ISO 31000",
            "KYC/AML/sanctions",
            "SOC 2 Type 2",
        ),
    )



def _build_digital_twin_scenario(
    twin: DigitalTwinInput,
    name: str,
    occupancy_delta: float = 0.0,
    rent_delta: float = 0.0,
    renovation_delta: float = 0.0,
    insurance_delta: float = 0.0,
    appreciation_delta: float = 0.0,
    reliability_delta: float = 0.0,
) -> DigitalTwinScenario:
    occupancy_rate = max(0.55, min(0.99, twin.occupancy_rate + occupancy_delta))
    monthly_rent = int(round(twin.monthly_rent * (1 + rent_delta)))
    renovation_budget = int(round(twin.renovation_budget * (1 + renovation_delta)))
    annual_insurance_premium = int(round(twin.annual_insurance_premium * (1 + insurance_delta)))
    appreciation_rate = twin.appreciation_rate + appreciation_delta
    annual_gross_income = int(round(monthly_rent * 12 * occupancy_rate))
    annual_operating_expenses = int(round(annual_gross_income * twin.operating_expense_ratio)) + annual_insurance_premium
    annual_noi = annual_gross_income - annual_operating_expenses
    annual_debt_service = int(round(twin.purchase_price * twin.financing_ratio * twin.interest_rate))
    annual_cash_flow = annual_noi - annual_debt_service
    cumulative_cash_flow = int(round(annual_cash_flow * twin.hold_years - renovation_budget))
    renovation_value_uplift = twin.current_value * twin.renovation_uplift * (renovation_budget / max(twin.renovation_budget, 1))
    projected_value = int(round((twin.current_value + renovation_value_uplift) * ((1 + appreciation_rate) ** twin.hold_years)))
    remaining_loan_balance = int(round(twin.purchase_price * twin.financing_ratio * 0.92))
    equity_uplift = projected_value - remaining_loan_balance + cumulative_cash_flow
    reliability_score = max(0.55, min(0.98, 0.83 - abs(occupancy_delta) * 0.7 - abs(appreciation_delta) * 1.8 - insurance_delta * 0.2 + reliability_delta))
    explanation = (
        f"{name} projects occupancy at {occupancy_rate:.0%}, modeled rent at {monthly_rent:,}/mo, annual NOI at {annual_noi:,}, "
        f"annual insurance at {annual_insurance_premium:,}, and five-to-{twin.hold_years}-year equity outcome near {equity_uplift:,}."
    )
    return DigitalTwinScenario(
        name=name,
        occupancy_rate=round(occupancy_rate, 2),
        monthly_rent=monthly_rent,
        renovation_budget=renovation_budget,
        annual_insurance_premium=annual_insurance_premium,
        annual_noi=annual_noi,
        annual_cash_flow=annual_cash_flow,
        cumulative_cash_flow=cumulative_cash_flow,
        projected_value=projected_value,
        equity_uplift=equity_uplift,
        reliability_score=round(reliability_score, 2),
        explanation=explanation,
    )



def evaluate_digital_twin(
    twin: DigitalTwinInput,
    identity: IdentityContext,
    context: RequestContext,
) -> DigitalTwinDecisionPacket:
    scenarios = (
        _build_digital_twin_scenario(twin, 'Baseline operating case'),
        _build_digital_twin_scenario(
            twin,
            'Renovation upside case',
            occupancy_delta=0.03,
            rent_delta=0.08,
            renovation_delta=0.18,
            insurance_delta=0.04,
            appreciation_delta=0.01,
            reliability_delta=-0.02,
        ),
        _build_digital_twin_scenario(
            twin,
            'Insurance and occupancy stress case',
            occupancy_delta=-0.09,
            rent_delta=-0.04,
            renovation_delta=-0.1,
            insurance_delta=0.22,
            appreciation_delta=-0.015,
            reliability_delta=-0.05,
        ),
    )
    baseline = scenarios[0]
    best_case = max(scenarios, key=lambda item: item.equity_uplift)
    downside = min(scenarios, key=lambda item: item.annual_cash_flow)
    baseline_assumptions = {
        'occupancy_rate': round(twin.occupancy_rate, 2),
        'monthly_rent': twin.monthly_rent,
        'operating_expense_ratio': round(twin.operating_expense_ratio, 2),
        'annual_insurance_premium': twin.annual_insurance_premium,
        'renovation_budget': twin.renovation_budget,
        'hold_years': twin.hold_years,
        'appreciation_rate': round(twin.appreciation_rate, 3),
        'governed_identity_tier': identity.auth_assurance_level,
        'market_volatility': context.market_volatility,
    }
    portfolio_outlook = (
        f"Baseline annual cash flow is {baseline.annual_cash_flow:,} with projected value {baseline.projected_value:,} after {twin.hold_years} years.",
        f"The upside case improves equity by {best_case.equity_uplift - baseline.equity_uplift:,} when renovation lift and occupancy gains materialize.",
        f"The downside case absorbs insurance and occupancy stress while still landing at {downside.equity_uplift:,} modeled equity outcome.",
        'Outputs stay explainable because every scenario exposes the occupancy, renovation, insurance, and valuation assumptions driving the projection.',
    )
    governance_controls = (
        DigitalTwinGovernanceControl(
            framework='ISO/IEC 42001',
            status='active',
            control='AI model accountability',
            detail='Scenario generation is bound to named assumptions, human-review checkpoints, and release gating before investment advice is exported.',
        ),
        DigitalTwinGovernanceControl(
            framework='ISO/IEC 5259',
            status='active',
            control='Data quality and reliability traceability',
            detail='Occupancy, rent, renovation, insurance, and value trajectories are surfaced as explicit variables so users can challenge or override them.',
        ),
        DigitalTwinGovernanceControl(
            framework='ISO/IEC 27001',
            status='active',
            control='Protected simulation inputs',
            detail='Identity, financial, and property inputs remain under RBAC, MFA-backed access, and immutable evidence logging.',
        ),
        DigitalTwinGovernanceControl(
            framework='ISO 22301',
            status='active',
            control='Reliable projection continuity',
            detail='Digital-twin scenario runs are replayable so operators can recover the last approved simulation state during continuity events.',
        ),
    )
    explainability_summary = (
        'Each scenario decomposes the recommendation into occupancy, rent, insurance, renovation, debt-service, NOI, cash-flow, and exit-value drivers rather than emitting a black-box score.'
    )
    reliability_summary = (
        f"Scenario reliability ranges from {min(item.reliability_score for item in scenarios):.2f} to {max(item.reliability_score for item in scenarios):.2f}, "
        'with stress cases penalized when assumptions drift further from verified operating data.'
    )
    recommendation = (
        f"Use the digital twin for {twin.property_name} to compare baseline, renovation upside, and insurance-stress outcomes before finalizing hold strategy, coverage, or capex timing."
    )
    explanation = (
        f"Digital twin {twin.twin_id} modeled {twin.property_name} in {twin.jurisdiction} using purchase price {twin.purchase_price:,}, current value {twin.current_value:,}, "
        f"occupancy {twin.occupancy_rate:.0%}, rent {twin.monthly_rent:,}/mo, renovation budget {twin.renovation_budget:,}, insurance premium {twin.annual_insurance_premium:,}, "
        f"and hold period {twin.hold_years} years. Best-case equity outcome is {best_case.equity_uplift:,}, downside annual cash flow is {downside.annual_cash_flow:,}, "
        'and governance controls keep assumptions inspectable, challengeable, and replayable.'
    )
    return DigitalTwinDecisionPacket(
        request_id=f"twin-{uuid.uuid4().hex[:8]}",
        twin=twin,
        baseline_assumptions=baseline_assumptions,
        scenarios=scenarios,
        portfolio_outlook=portfolio_outlook,
        governance_controls=governance_controls,
        explainability_summary=explainability_summary,
        reliability_summary=reliability_summary,
        recommendation=recommendation,
        explanation=explanation,
        standards_alignment=('ISO/IEC 42001', 'ISO/IEC 5259', 'ISO/IEC 27001', 'ISO 22301', 'ISO 31000'),
    )



def evaluate_insurance_options(
    applicant: InsuranceApplicantProfile,
    identity: IdentityContext,
    context: RequestContext,
) -> InsuranceDecisionPacket:
    persona_map = {
        "buyer": "buyer",
        "investor": "investor",
        "advisor": "advisor",
    }
    persona = persona_map.get(applicant.persona, "buyer")
    property_form = {
        "single_family": "HO-3",
        "condo": "HO-6",
        "townhouse": "DP-3",
        "multifamily": "Habitational package",
        "luxury": "High-value homeowners",
    }.get(applicant.property_type, "HO-3")
    owner_title = "Enhanced owner's title" if applicant.transaction_context in {"closing", "purchase"} and applicant.estimated_property_value >= 1000000 else "Owner's title"
    landlord_form = "Landlord package" if applicant.landlord_exposure else "Deferred landlord endorsement"
    life_form = "Term life with mortgage continuity rider" if applicant.life_priority else "Optional household continuity rider"

    acord_parties = (
        ACORDParty(role="applicant", name=identity.subject_id, identifier=applicant.applicant_id),
        ACORDParty(role="servicing_entity", name="EstateOS Insurance Desk", identifier="estateos-insurance"),
        ACORDParty(role="transaction_context", name=applicant.transaction_context, identifier=context.request_id),
    )
    acord_coverages = (
        ACORDCoverageRequest(
            line_of_business="property",
            acord_form="ACORD 80",
            coverage_type="homeowners",
            insured_amount=applicant.estimated_property_value,
            deductible=2500 if applicant.property_type in {"luxury", "multifamily"} else 1000,
            notes="Captures dwelling, occupancy, mortgagee, and peril details for quote intake.",
        ),
        ACORDCoverageRequest(
            line_of_business="title",
            acord_form="ACORD 28",
            coverage_type="title",
            insured_amount=applicant.estimated_property_value,
            deductible=0,
            notes="Binds ownership, lender, and recording evidence to the closing packet.",
        ),
        ACORDCoverageRequest(
            line_of_business="landlord",
            acord_form="ACORD 101",
            coverage_type="landlord",
            insured_amount=max(applicant.estimated_property_value // 2, 100000),
            deductible=2500,
            notes="Supports rental, loss-of-rents, and premises-liability underwriting when leasing exposure exists.",
        ),
        ACORDCoverageRequest(
            line_of_business="life",
            acord_form="ACORD 103",
            coverage_type="life_continuity",
            insured_amount=max(applicant.mortgage_amount or applicant.estimated_property_value // 2, 150000),
            deductible=0,
            notes="Captures beneficiary and continuity needs when household or guarantor protection is requested.",
        ),
    )

    recommendations = [
        InsuranceRecommendation(
            coverage_type="homeowners",
            recommendation_level="primary",
            policy_form=property_form,
            premium_estimate="$188/mo est." if property_form == "HO-3" else "$146/mo est." if property_form == "HO-6" else "$322/mo est." if property_form == "Habitational package" else "$352/mo est.",
            rationale=(
                f"{property_form} is the best fit for a {applicant.occupancy} {applicant.property_type.replace('_', ' ')} because it aligns dwelling protection with the current {applicant.transaction_context} workflow."
            ),
            acord_payload_refs=("ACORD 80",),
        ),
        InsuranceRecommendation(
            coverage_type="title",
            recommendation_level="recommended" if applicant.title_required else "optional",
            policy_form=owner_title,
            premium_estimate="$2,280 one-time est." if owner_title.startswith("Enhanced") else "$1,950 one-time est.",
            rationale="Title protection is recommended whenever acquisition, transfer, or refinance steps depend on clean ownership and lien status.",
            acord_payload_refs=("ACORD 28",),
        ),
        InsuranceRecommendation(
            coverage_type="landlord",
            recommendation_level="primary" if applicant.landlord_exposure else "contingent",
            policy_form=landlord_form,
            premium_estimate="$322/mo est." if applicant.landlord_exposure else "$38/mo add-on est.",
            rationale="Landlord coverage becomes primary when rent interruption, tenant liability, or premises claims could affect transaction economics.",
            acord_payload_refs=("ACORD 101",),
        ),
        InsuranceRecommendation(
            coverage_type="life_related",
            recommendation_level="recommended" if applicant.life_priority else "optional",
            policy_form=life_form,
            premium_estimate="$61/mo est." if applicant.life_priority else "$28/mo add-on est.",
            rationale="Life-related continuity coverage is recommended when household dependents, guarantors, or debt-service plans depend on insured income continuity.",
            acord_payload_refs=("ACORD 103",),
        ),
    ]

    secure_exchange_controls = [
        SecureExchangeControl(
            control="Consent and privacy notice",
            status="active" if applicant.privacy_consent and context.has_consent else "review",
            detail="NAIC-aligned notice, purpose limitation, and quote-sharing consent are checked before payload release.",
        ),
        SecureExchangeControl(
            control="Encrypted carrier exchange",
            status="active" if identity.mfa_completed else "review",
            detail="ACORD payloads are exchanged using mTLS, field-level encryption, signed service identities, and correlation IDs.",
        ),
        SecureExchangeControl(
            control="Access and servicing governance",
            status="active" if "decision:view" in identity.entitlements else "blocked",
            detail="Only entitled advisors, servicing staff, and approved partner roles can view recommendation details or request quotes.",
        ),
        SecureExchangeControl(
            control="Audit and retention",
            status="active",
            detail="Quote packets, title evidence, underwriting assumptions, and retransmission attempts are written to immutable servicing logs.",
        ),
    ]

    blocked = any(item.status == "blocked" for item in secure_exchange_controls)
    review = any(item.status == "review" for item in secure_exchange_controls)
    release_status = "blocked" if blocked else "review" if review else "released"
    naic_privacy_summary = (
        "NAIC-aligned privacy handling uses purpose-bound collection, role-based disclosure, third-party oversight, incident response linkage, and secure disposal expectations."
    )
    secure_exchange_summary = (
        f"EstateOS packages {len(acord_coverages)} ACORD-informed coverage payloads for {persona} servicing, encrypts transport, minimizes shared fields, and binds transmissions to request {context.request_id}."
    )
    explanation = (
        f"Insurance review evaluated persona '{persona}', property type '{applicant.property_type}', occupancy '{applicant.occupancy}', and transaction context '{applicant.transaction_context}'. "
        f"Recommendations include homeowners, title, landlord, and life-related options while preserving {identity.privacy_tier} privacy posture, MFA={'on' if identity.mfa_completed else 'off'}, and release status '{release_status}'."
    )

    return InsuranceDecisionPacket(
        request_id=f"ins-{uuid.uuid4().hex[:8]}",
        applicant=applicant,
        acord_parties=acord_parties,
        acord_coverages=acord_coverages,
        recommendations=recommendations,
        secure_exchange_controls=secure_exchange_controls,
        naic_privacy_summary=naic_privacy_summary,
        secure_exchange_summary=secure_exchange_summary,
        release_status=release_status,
        explanation=explanation,
        standards_alignment=("ACORD", "NAIC Privacy/Security", "ISO/IEC 27001", "ISO/IEC 27701"),
    )



def evaluate_payment_risk(
    payment: PaymentRequest,
    identity: IdentityContext,
    context: RequestContext,
) -> PaymentDecisionPacket:
    token_provider = "Stripe Treasury adapter" if payment.payment_method_type in {"card_token", "wallet"} else "Banking / escrow token service"
    payment_instrument = PaymentInstrument(
        instrument_type=payment.payment_method_type,
        token_provider=token_provider,
        token_reference=f"tok-{uuid.uuid4().hex[:10]}",
        last4="4242" if payment.payment_method_type == "card_token" else "6789",
        network="Visa" if payment.payment_method_type == "card_token" else "ACH/Wire",
        wallet_or_bank="Apple Pay" if payment.payment_method_type == "wallet" else "Escrow operating account",
        pci_scope="tokenized_frontend_only",
    )
    participants = (
        PaymentParticipant(role="payer", name=identity.subject_id, identifier=payment.payer_id),
        PaymentParticipant(role="beneficiary", name="EstateOS Escrow", identifier=payment.transaction_reference),
        PaymentParticipant(role="servicer", name="EstateOS Payment Ops", identifier=context.request_id),
    )

    risk_score = 0.14
    risk_score += min(0.24, payment.amount / 500000 * 0.22)
    risk_score += 0.15 if payment.cross_border else 0.03
    risk_score += 0.12 if payment.payment_method_type == "wire" else 0.09 if payment.payment_method_type == "card_token" else 0.07
    risk_score += 0.09 if payment.settlement_timing == "same_day" else 0.05 if payment.settlement_timing == "next_day" else 0.03
    risk_score += 0.12 if not payment.trusted_device else -0.08
    risk_score += min(0.1, payment.chargeback_history_count * 0.03)
    risk_score += -0.04 if payment.manual_review_requested else 0.05
    risk_score += -0.03 if payment.escrow_stage in {"docs_cleared", "release_pending", "disbursed"} else 0.04
    fraud_probability = round(max(0.04, min(0.96, risk_score)), 2)

    risk_level = "high" if fraud_probability >= 0.72 else "moderate" if fraud_probability >= 0.48 else "low"
    release_status = "hold" if fraud_probability >= 0.72 else "review" if fraud_probability >= 0.48 or not payment.trusted_device else "released"
    payment_behavior_summary = (
        "Payer behavior is anomalous and requires operations review."
        if fraud_probability >= 0.72
        else "Payer behavior is watchlisted because one or more telemetry signals exceeded baseline."
        if fraud_probability >= 0.48
        else "Payer behavior is stable across token usage, timing, and identity context."
    )
    escrow_status = {
        "deposit_pending": "Funding controls active",
        "funds_received": "Funds received pending milestone review",
        "docs_cleared": "Ready when settlement confirms",
        "release_pending": "Awaiting dual approval",
        "disbursed": "Released and logged",
    }.get(payment.escrow_stage, "Funding controls active")
    frontend_security_posture = (
        "PCI DSS hosted payment fields, tokenized instruments, CSP/WAF controls, and log redaction protect the frontend payment experience."
    )

    signals = (
        PaymentSignal(category="device_trust", status="passed" if payment.trusted_device else "review", detail="Session is bound to MFA and a trusted device." if payment.trusted_device else "Step-up verification is required because device trust is incomplete."),
        PaymentSignal(category="amount_velocity", status="review" if payment.amount >= 100000 else "passed", detail=f"Amount {payment.amount:,} is checked against payer velocity and historical behavior."),
        PaymentSignal(category="cross_border", status="review" if payment.cross_border else "passed", detail="Cross-border payment routes trigger enhanced beneficiary, sanctions, and settlement monitoring." if payment.cross_border else "Domestic settlement path keeps screening and settlement complexity lower."),
        PaymentSignal(category="chargeback_history", status="review" if payment.chargeback_history_count else "passed", detail="Chargeback history feeds the fraud probability model and manual-review thresholds."),
    )
    escrow_conditions = (
        EscrowCondition(condition="funds_available", status="ready" if payment.escrow_stage != "deposit_pending" else "pending", detail="Escrow release requires settled funds and beneficiary matching."),
        EscrowCondition(condition="document_clearance", status="ready" if payment.escrow_stage in {"docs_cleared", "release_pending", "disbursed"} else "review", detail="Closing, identity, and approval milestones must be complete before release."),
        EscrowCondition(condition="dual_approval", status="ready" if payment.escrow_stage in {"release_pending", "disbursed"} else "pending", detail="Release requires dual approval with segregation of duties and immutable event logging."),
    )
    reconciliation_entries = (
        ReconciliationEntry(entry_type="authorization_capture", status="tracked" if payment.payment_method_type in {"card_token", "wallet"} else "not_applicable", detail="PSP references are reconciled without exposing raw cardholder data."),
        ReconciliationEntry(entry_type="escrow_ledger", status="closed" if payment.escrow_stage == "disbursed" else "open", detail="Escrow ledger events are matched to bank/PSP settlement references."),
        ReconciliationEntry(entry_type="exception_queue", status="escalated" if payment.manual_review_requested else "monitored", detail="Signed webhooks, settlement files, and exception queues drive reconciliation closeout."),
    )
    recommended_actions = (
        "Keep the user in hosted payment fields and masked token views.",
        "Require payment-ops review before release." if release_status != "released" else "Allow escrow progression when settlement and approvals remain clean.",
        "Match settlement references and escrow ledger entries before reconciliation close.",
    )
    explanation = (
        f"Payment {payment.transaction_reference} was evaluated for {payment.amount:,} {payment.currency} using method '{payment.payment_method_type}' with escrow stage '{payment.escrow_stage}'. "
        f"Fraud probability={fraud_probability:.2f}, risk level='{risk_level}', cross_border={payment.cross_border}, trusted_device={payment.trusted_device}, and release_status='{release_status}'. "
        f"The frontend remains PCI-safe by using tokenized instruments and hosted payment fields while backend controls score payer behavior, escrow conditions, and reconciliation posture."
    )

    return PaymentDecisionPacket(
        request_id=f"pay-{uuid.uuid4().hex[:8]}",
        transaction_reference=payment.transaction_reference,
        payment_instrument=payment_instrument,
        participants=participants,
        fraud_probability=fraud_probability,
        risk_level=risk_level,
        payment_behavior_summary=payment_behavior_summary,
        escrow_status=escrow_status,
        frontend_security_posture=frontend_security_posture,
        signals=signals,
        escrow_conditions=escrow_conditions,
        reconciliation_entries=reconciliation_entries,
        recommended_actions=recommended_actions,
        release_status=release_status,
        explanation=explanation,
        standards_alignment=("PCI DSS", "ISO/IEC 27001", "ISO/IEC 27701", "ISO 31000", "SOC 2 Type 2"),
    )


WORKFLOW_ORDER: Sequence[str] = (
    "intake",
    "pricing_review",
    "negotiation",
    "document_validation",
    "approval",
    "closing",
)


def _stage_index(stage: str) -> int:
    try:
        return WORKFLOW_ORDER.index(stage)
    except ValueError:
        return -1


def analyze_pricing_strategy(transaction: TransactionCase, context: RequestContext) -> DealExpertInsight:
    discount_ratio = (transaction.target_price - transaction.purchase_price) / max(transaction.purchase_price, 1)
    urgency_pressure = 0.04 if transaction.urgency_days <= 14 else 0.0
    volatility_penalty = 0.03 if context.market_volatility == "high" else 0.0
    score = max(0.0, min(0.99, 0.84 + urgency_pressure - volatility_penalty - abs(discount_ratio) * 0.35))
    headline = f"Anchor near {transaction.target_price:,} with protected concession bands."
    detail = (
        "Pricing strategy recommends an anchored opening position, a documented walk-away threshold, and contingency pricing "
        "that preserves margin if diligence reveals title, financing, or disclosure friction."
    )
    return DealExpertInsight(
        expert="pricing_strategy",
        headline=headline,
        detail=detail,
        score=round(score, 2),
        priority="high" if transaction.urgency_days <= 21 else "medium",
        next_action="Prepare counteroffer ladder with opening, midpoint, and walk-away thresholds.",
    )


def analyze_negotiation(transaction: TransactionCase) -> DealExpertInsight:
    motivation_bonus = 0.05 if transaction.seller_motivation in {"high", "distressed"} else 0.0
    counterparty_penalty = 0.06 if transaction.counterparty_risk == "high" else 0.02 if transaction.counterparty_risk == "medium" else 0.0
    score = max(0.0, min(0.99, 0.8 + motivation_bonus - counterparty_penalty))
    detail = (
        "Negotiation insight favors time-boxed counters, explicit document conditions, and concession sequencing that trades speed "
        "for signature certainty rather than headline price alone."
    )
    return DealExpertInsight(
        expert="negotiation_insights",
        headline="Use deadline-backed concessions and keep document deficiencies as leverage.",
        detail=detail,
        score=round(score, 2),
        priority="high" if transaction.counterparty_risk != "low" else "medium",
        next_action="Issue a counter with an expiration window and evidence-based contingency carve-outs.",
    )


def analyze_documents(transaction: TransactionCase) -> DealExpertInsight:
    issues = sum(len(document.issues) for document in transaction.requested_documents)
    missing = sum(1 for document in transaction.requested_documents if document.status != "validated")
    score = max(0.0, min(0.99, 0.93 - missing * 0.08 - issues * 0.03))
    detail = (
        f"Document validation reviewed {len(transaction.requested_documents)} artifacts, found {missing} not-yet-validated items, "
        f"and logged {issues} compliance or execution issues for remediation."
    )
    return DealExpertInsight(
        expert="document_validation",
        headline="Do not advance to closing until title, disclosures, and signatures clear validation.",
        detail=detail,
        score=round(score, 2),
        priority="critical" if missing else "medium",
        next_action="Route open document issues to owners and require re-validation before approval.",
    )


def check_workflow_integrity(transaction: TransactionCase) -> DealWorkflowIntegrity:
    stage_positions = [_stage_index(item.stage) for item in transaction.workflow_stages]
    sequential = "intact" if stage_positions == sorted(stage_positions) and -1 not in stage_positions else "out_of_sequence"
    immutable_chain = True
    continuity_mode = "active-active" if transaction.bcdr_tier in {"tier_0", "tier_1"} else "warm-standby"
    notes = (
        "All stage changes are event-sourced and replayable.",
        "Manual continuity runbook is attached to approval and closing stages.",
        f"BCDR tier {transaction.bcdr_tier} maps to workflow replay and alternate-queue failover.",
    )
    return DealWorkflowIntegrity(
        sequential_integrity=sequential,
        audit_status="complete" if immutable_chain else "degraded",
        immutable_event_chain=immutable_chain,
        continuity_mode=continuity_mode,
        continuity_notes=notes,
    )


def analyze_deal_risk(transaction: TransactionCase, context: RequestContext, integrity: DealWorkflowIntegrity) -> DealExpertInsight:
    issue_count = sum(len(item.issues) for item in transaction.requested_documents)
    blocked_stages = sum(1 for item in transaction.workflow_stages if item.status == "blocked")
    score = 0.34
    score += 0.12 if transaction.counterparty_risk == "high" else 0.05 if transaction.counterparty_risk == "medium" else 0.0
    score += 0.08 if context.market_volatility == "high" else 0.03 if context.market_volatility == "medium" else 0.0
    score += blocked_stages * 0.07
    score += issue_count * 0.025
    score += 0.05 if integrity.sequential_integrity != "intact" else 0.0
    score += 0.04 if transaction.financing_ratio > 0.75 else 0.0
    risk_score = max(0.0, min(0.99, score))
    detail = (
        "Deal risk scoring combines counterparty posture, market volatility, document exceptions, financing leverage, "
        "and workflow integrity checks into a single escalation score."
    )
    return DealExpertInsight(
        expert="deal_risk_scoring",
        headline="Escalate when counterparty friction, leverage, or document drift exceed tolerance.",
        detail=detail,
        score=round(1 - risk_score, 2),
        priority="critical" if risk_score >= 0.7 else "high" if risk_score >= 0.5 else "medium",
        next_action="Lock release behind approval if the risk score remains above the configured threshold.",
    )


def build_transaction_controls(
    transaction: TransactionCase,
    identity: IdentityContext,
    integrity: DealWorkflowIntegrity,
) -> List[ComplianceControlStatus]:
    open_documents = [item.name for item in transaction.requested_documents if item.status != "validated"]
    return [
        ComplianceControlStatus(
            control="Access governance",
            framework="ISO/IEC 27001",
            status="active" if identity.mfa_completed else "review",
            detail="RBAC and MFA protect pricing, negotiation, and release decisions for sensitive transactions.",
            evidence=("RBAC entitlement snapshot", "MFA assertion", "approval group membership"),
        ),
        ComplianceControlStatus(
            control="Immutable audit trail",
            framework="ISO/IEC 27001",
            status="active" if integrity.immutable_event_chain else "review",
            detail="Every stage transition, expert recommendation, and approval is written to an immutable event chain.",
            evidence=("event stream offsets", "tamper-evident digest", "approval timestamps"),
        ),
        ComplianceControlStatus(
            control="Documented continuity plan",
            framework="ISO 22301",
            status="active" if transaction.bcdr_tier in {"tier_0", "tier_1", "tier_2"} else "review",
            detail="Critical deal workflows have defined recovery paths, alternate queues, and manual playbooks.",
            evidence=("continuity tier mapping", "workflow replay procedure", "RTO/RPO checkpoint"),
        ),
        ComplianceControlStatus(
            control="Document completeness",
            framework="ISO/IEC 27001",
            status="review" if open_documents else "active",
            detail=(
                "Deal release requires validated title, disclosure, diligence, and closing artifacts before advancing the workflow."
            ),
            evidence=tuple(open_documents or ["all required documents validated"]),
        ),
    ]


def build_transaction_audit_trail(
    transaction: TransactionCase,
    integrity: DealWorkflowIntegrity,
    release_status: str,
) -> List[AuditEvent]:
    return [
        AuditEvent(name="transaction.intake.recorded", status="completed", detail=f"Transaction {transaction.transaction_id} created for {transaction.deal_name}."),
        AuditEvent(name="transaction.pricing.reviewed", status="completed", detail="Pricing strategy generated with concession ladder."),
        AuditEvent(name="transaction.documents.checked", status="completed", detail="Validation results linked to immutable audit bundle."),
        AuditEvent(name="transaction.workflow.integrity", status=integrity.sequential_integrity, detail=f"Continuity mode={integrity.continuity_mode}."),
        AuditEvent(name="transaction.release.gated", status=release_status, detail="Release status determined from risk, controls, and workflow integrity."),
    ]


def rate_risk(risk_score: float) -> str:
    if risk_score >= 0.75:
        return "critical"
    if risk_score >= 0.58:
        return "high"
    if risk_score >= 0.38:
        return "moderate"
    return "low"


def orchestrate_transaction(
    transaction: TransactionCase,
    identity: IdentityContext,
    context: RequestContext,
) -> TransactionDecisionPacket:
    pricing = analyze_pricing_strategy(transaction, context)
    negotiation = analyze_negotiation(transaction)
    document_validation = analyze_documents(transaction)
    integrity = check_workflow_integrity(transaction)
    risk_insight = analyze_deal_risk(transaction, context, integrity)

    risk_score = round(
        min(
            0.99,
            1 - ((pricing.score + negotiation.score + document_validation.score + risk_insight.score) / 4) + 0.18,
        ),
        2,
    )
    risk_rating = rate_risk(risk_score)
    controls = build_transaction_controls(transaction, identity, integrity)

    release_status = "ready"
    if risk_rating in {"critical", "high"} or any(control.status == "review" for control in controls):
        release_status = "review"
    if document_validation.priority == "critical" and risk_rating == "critical":
        release_status = "hold"

    recommendations = [
        pricing.next_action,
        negotiation.next_action,
        document_validation.next_action,
        risk_insight.next_action,
        "Preserve all approvals, counters, and continuity checkpoints in the audit ledger before closing.",
    ]
    explanation = (
        f"Transaction {transaction.transaction_id} for {transaction.deal_name} is in stage '{transaction.stage}' with risk rating '{risk_rating}'. "
        f"Pricing confidence={pricing.score:.2f}, negotiation confidence={negotiation.score:.2f}, document validation confidence={document_validation.score:.2f}, "
        f"and workflow integrity is '{integrity.sequential_integrity}'. ISO/IEC 27001 controls protect access, evidence, and document handling while ISO 22301 controls "
        f"preserve continuity through {integrity.continuity_mode} routing and replayable events."
    )

    return TransactionDecisionPacket(
        request_id=f"txn-{uuid.uuid4().hex[:8]}",
        transaction=transaction,
        pricing_strategy=pricing,
        negotiation_insight=negotiation,
        document_validation=document_validation,
        risk_scoring=risk_insight,
        overall_risk_score=risk_score,
        risk_rating=risk_rating,
        release_status=release_status,
        workflow_integrity=integrity,
        compliance_controls=controls,
        audit_trail=build_transaction_audit_trail(transaction, integrity, release_status),
        recommendations=recommendations,
        explanation=explanation,
        standards_alignment=("ISO/IEC 27001", "ISO 22301", "ISO/IEC 42001", "ISO 31000"),
    )


def evaluate_tokenization(
    profile: UserProfile,
    identity: IdentityContext,
    context: RequestContext,
    transaction: TransactionCase,
    asset_name: str,
    legal_wrapper: str,
    domicile: str,
    target_raise: int,
    minimum_investment: int,
    sponsor_equity_pct: float,
    retail_allocation_pct: float,
    lockup_period_days: int,
    transfer_policy: str,
    distribution_policy: str,
) -> TokenizationDecisionPacket:
    unit_price = minimum_investment
    total_units = max(target_raise // max(unit_price, 1), 1)
    asset_value = max(transaction.purchase_price, target_raise)
    valuation_basis = (
        "last_transaction_plus_holdback"
        if transaction.stage in {"document_validation", "approval"}
        else "latest_appraisal_or_board_approved_nav"
    )

    compliance_checks = (
        TokenizationComplianceCheck(
            name="KYC / beneficial owner verification",
            status="passed" if identity.kyc_status == "approved" else "review",
            detail="Primary subscription is blocked until controller and beneficial-owner evidence remain current.",
        ),
        TokenizationComplianceCheck(
            name="AML / sanctions / source-of-funds",
            status="passed" if identity.sanctions_status == "clear" else "blocked",
            detail="Cross-border flows require sanctions clearance, source-of-funds evidence, and ongoing transaction monitoring.",
        ),
        TokenizationComplianceCheck(
            name="Securities eligibility and transfer restrictions",
            status="review" if context.cross_border else "passed",
            detail="Investor class, jurisdiction, and holding-period rules control whether subscription or transfer can be released.",
        ),
        TokenizationComplianceCheck(
            name="Cash settlement and cap-table reconciliation",
            status="passed" if transaction.stage in {"document_validation", "approval", "closing"} else "review",
            detail="Units are only allocated after escrow settlement, administrator reconciliation, and legal-ledger synchronization.",
        ),
    )

    ownership_records = (
        FractionalOwnershipRecord(
            investor_label="Sponsor reserve",
            investor_class="sponsor",
            beneficial_owner_reference="bo-sponsor-core",
            wallet_reference="custody-sponsor-001",
            units=max(int(total_units * sponsor_equity_pct), 1),
            ownership_pct=round(sponsor_equity_pct * 100, 2),
            status="locked",
        ),
        FractionalOwnershipRecord(
            investor_label="Qualified investor allocation",
            investor_class="qualified",
            beneficial_owner_reference=f"bo-{identity.subject_id}",
            wallet_reference="custody-qualified-queue",
            units=max(int(total_units * retail_allocation_pct * 0.55), 1),
            ownership_pct=round(retail_allocation_pct * 55, 2),
            status="subscribed",
        ),
        FractionalOwnershipRecord(
            investor_label="Retail waitlist pool",
            investor_class="retail",
            beneficial_owner_reference="bo-retail-whitelist",
            wallet_reference="custody-retail-queue",
            units=max(int(total_units * retail_allocation_pct * 0.45), 1),
            ownership_pct=round(retail_allocation_pct * 45, 2),
            status="pending_whitelist",
        ),
    )

    ledger_events = (
        TokenizationLedgerEvent(
            event_type="offering_created",
            status="recorded",
            detail=f"{asset_name} is wrapped through {legal_wrapper} in {domicile} with a governed unit supply.",
        ),
        TokenizationLedgerEvent(
            event_type="subscription_reservation",
            status="recorded",
            detail="Reserved units stay non-transferable until disclosures, investor classification, and payment evidence are complete.",
        ),
        TokenizationLedgerEvent(
            event_type="cash_settlement",
            status="pending" if transaction.stage != "closing" else "cleared",
            detail="Escrow, subscription funds, and administrator ledger references must reconcile before allocation finality.",
        ),
        TokenizationLedgerEvent(
            event_type="mint_or_allocation",
            status="gated",
            detail="Digital units are minted or allocated only after legal-ledger approval, not directly from frontend intent alone.",
        ),
        TokenizationLedgerEvent(
            event_type="secondary_transfer_policy",
            status="active",
            detail=transfer_policy,
        ),
    )

    release_status = (
        "Advisor review before release"
        if profile.role == "advisor"
        else "Review before release" if context.cross_border else "Release ready with whitelist controls"
    )
    eligibility_summary = (
        "Fractional investment is available only to investors who pass KYC, AML, beneficial-owner, and jurisdiction-specific securities checks."
    )
    explanation = (
        f"EstateOS models tokenization for {asset_name} as a governed securities-style workflow. The frontend can market units, show distributions, and collect subscriptions, "
        f"but the backend remains authoritative for investor eligibility, cap-table integrity, settlement reconciliation, and transfer restrictions under {legal_wrapper}."
    )

    return TokenizationDecisionPacket(
        request_id=context.request_id,
        asset=TokenizationAsset(
            asset_id=f"asset-{transaction.transaction_id}",
            property_name=asset_name,
            jurisdiction=transaction.jurisdiction,
            legal_wrapper=legal_wrapper,
            domicile=domicile,
            asset_value=asset_value,
            valuation_basis=valuation_basis,
            currency="USD",
            minimum_investment=minimum_investment,
            target_raise=target_raise,
            unit_price=unit_price,
            total_units=total_units,
            sponsor_equity_pct=sponsor_equity_pct,
            retail_allocation_pct=retail_allocation_pct,
            lockup_period_days=lockup_period_days,
            transfer_policy=transfer_policy,
        ),
        offering_status="subscription_window_open",
        eligibility_summary=eligibility_summary,
        distribution_policy=distribution_policy,
        compliance_checks=compliance_checks,
        ownership_records=ownership_records,
        ledger_events=ledger_events,
        recommended_actions=(
            "Keep legal-ledger, cash-ledger, and token-ledger reconciliation in the same approval workflow.",
            "Require jurisdiction-aware whitelist review before any secondary transfer.",
            "Publish investor statements and audit evidence after each issuance, distribution, or redemption cycle.",
        ),
        release_status=release_status,
        explanation=explanation,
        standards_alignment=(
            "ISO/IEC 27001",
            "ISO/IEC 27701",
            "SOC 2 Type 2",
            "PCI DSS",
            "KYC/AML/sanctions/beneficial ownership controls",
        ),
    )


def evaluate_document_intelligence(
    profile: UserProfile,
    identity: IdentityContext,
    context: RequestContext,
    transaction: TransactionCase,
    insurance_packet: InsuranceDecisionPacket,
    residency_packet: ResidencyEligibilityPacket,
) -> DocumentIntelligencePacket:
    title_document = GovernedDocument(
        document_id="doc-title-chain",
        document_type="title_report",
        title=f"{transaction.jurisdiction} title and encumbrance packet",
        jurisdiction=transaction.jurisdiction,
        source_system="land_registry_adapter",
        language="en",
        status="validated",
        confidence=0.97,
    )
    contract_document = GovernedDocument(
        document_id="doc-purchase-contract",
        document_type="purchase_contract",
        title=f"{transaction.deal_name} purchase agreement",
        jurisdiction=transaction.jurisdiction,
        source_system="deal_room",
        language="en",
        status="review",
        confidence=0.91,
    )
    insurance_document = GovernedDocument(
        document_id="doc-insurance-binder",
        document_type="insurance_policy",
        title=f"{insurance_packet.recommendations[0].coverage_type} draft binder",
        jurisdiction=insurance_packet.applicant.property_jurisdiction,
        source_system="insurance_exchange",
        language="en",
        status="review",
        confidence=0.89,
    )
    immigration_document = GovernedDocument(
        document_id="doc-immigration-pack",
        document_type="immigration_evidence",
        title=f"{residency_packet.program} eligibility packet",
        jurisdiction=residency_packet.jurisdiction,
        source_system="residency_workflow",
        language="en",
        status="needs_evidence",
        confidence=0.87,
    )
    governed_documents = (
        contract_document,
        title_document,
        insurance_document,
        immigration_document,
    )

    extracted_fields = (
        DocumentFieldExtraction(
            document_id=contract_document.document_id,
            field_name="purchase_price",
            field_value=f"{transaction.purchase_price} USD",
            confidence=0.95,
            normalized_value=str(transaction.purchase_price),
            rationale="Signature blocks, price table, and consideration clause agree on the same purchase price.",
        ),
        DocumentFieldExtraction(
            document_id=title_document.document_id,
            field_name="encumbrance_status",
            field_value="No encumbrance exceptions detected",
            confidence=0.96,
            normalized_value="clean_title",
            rationale="Registry excerpt and title abstract resolve to a clean chain for the reviewed parcel.",
        ),
        DocumentFieldExtraction(
            document_id=insurance_document.document_id,
            field_name="insured_amount",
            field_value=str(insurance_packet.acord_coverages[0].insured_amount),
            confidence=0.9,
            normalized_value=str(insurance_packet.acord_coverages[0].insured_amount),
            rationale="Coverage schedule and ACORD draft align on the primary insured amount.",
        ),
        DocumentFieldExtraction(
            document_id=immigration_document.document_id,
            field_name="eligibility_pathway",
            field_value=residency_packet.pathway_type,
            confidence=0.88,
            normalized_value=residency_packet.pathway_type.replace(" ", "_").lower(),
            rationale="Program rules and intake answers agree on the targeted residency route.",
        ),
    )

    unresolved_residency_evidence = len([item for item in residency_packet.document_checks if item.status != "passed"])
    validation_checks = (
        DocumentValidationCheck(
            document_id=contract_document.document_id,
            check_name="Signature and clause completeness",
            status="review",
            detail="Commercial terms are extracted successfully, but one permit-related attachment is still missing from the disclosure packet.",
            severity="medium",
        ),
        DocumentValidationCheck(
            document_id=title_document.document_id,
            check_name="Chain-of-title and lien validation",
            status="passed",
            detail="Title records, owner references, and encumbrance checks are internally consistent.",
            severity="low",
        ),
        DocumentValidationCheck(
            document_id=insurance_document.document_id,
            check_name="Coverage alignment with lender and asset value",
            status="review",
            detail="Coverage form is suitable, but final binder issuance is gated on the same document-completeness controls as closing.",
            severity="medium",
        ),
        DocumentValidationCheck(
            document_id=immigration_document.document_id,
            check_name="Residency evidence completeness",
            status="review",
            detail=f"{unresolved_residency_evidence} evidence items still require confirmation or counsel review.",
            severity="medium",
        ),
    )

    anomaly_signals = (
        DocumentAnomalySignal(
            signal="Cross-document timing mismatch",
            severity="medium",
            affected_documents=(contract_document.title, insurance_document.title),
            detail="Closing-sensitive dates appear aligned overall, but the insurance binder should not be released until the contract attachment set is complete.",
            recommended_action="Link binder release to the transaction approval gate and re-run the completeness check after the permit attachment lands.",
        ),
        DocumentAnomalySignal(
            signal="Immigration evidence dependency",
            severity="medium",
            affected_documents=(immigration_document.title,),
            detail="Residency reasoning remains positive, yet filing readiness depends on supporting evidence that has not been fully attested in the packet.",
            recommended_action="Escalate remaining evidence items to counsel review before any government submission is triggered.",
        ),
    )

    compliance_findings = (
        DocumentComplianceFinding(
            framework="ISO/IEC 42001",
            control="Explainable extraction and reasoning",
            status="active",
            detail="Each summarized field preserves confidence, normalization output, and rationale so reviewers can challenge or reproduce the AI result.",
        ),
        DocumentComplianceFinding(
            framework="ISO/IEC 27001",
            control="Access and evidence governance",
            status="active",
            detail="Document-derived insights inherit RBAC, MFA, privacy-tier, and immutable audit controls before release.",
        ),
        DocumentComplianceFinding(
            framework="ISO/IEC 27701",
            control="Purpose-bound document minimization",
            status="active",
            detail="Frontend summaries expose simplified insights while sensitive identity, financial, and immigration evidence stays restricted to approved roles.",
        ),
        DocumentComplianceFinding(
            framework="KYC/AML/sanctions",
            control="Source-of-funds and beneficial-owner dependencies",
            status="review" if context.cross_border else "active",
            detail="Cross-border document flows remain gated on current KYC, AML, sanctions, and source-of-funds evidence.",
        ),
    )

    audit_records = (
        DocumentAuditRecord(
            event="document_ingested",
            actor="document_intelligence_pipeline",
            detail=f"Ingested {len(governed_documents)} governed documents for {transaction.deal_name}.",
        ),
        DocumentAuditRecord(
            event="field_extraction_completed",
            actor="document_intelligence_pipeline",
            detail=f"Extracted {len(extracted_fields)} high-value normalized fields with explainability metadata.",
        ),
        DocumentAuditRecord(
            event="compliance_linkage_verified",
            actor="compliance_service",
            detail=f"Linked document packet to privacy tier {identity.privacy_tier}, consent scope, and cross-border compliance checks.",
        ),
        DocumentAuditRecord(
            event="frontend_summary_published",
            actor="ai_orchestrator",
            detail="Released simplified insights for frontend display while preserving backend-only evidence trails and anomaly markers.",
        ),
    )

    release_status = "review" if any(item.status != "passed" for item in validation_checks) else "ready"
    frontend_insights = (
        "Contracts, title, insurance, and immigration packets are summarized into plain-language checkpoints for the workspace.",
        "Backend validation confirms clean title evidence, extracts governing commercial terms, and flags unresolved attachments before closing.",
        "Insurance and residency packets stay linked to the same audit chain so users see readiness without exposing raw sensitive files.",
        "Anomaly detection compares dates, values, obligations, and evidence dependencies across documents before any downstream release.",
    )
    simplified_summary = (
        f"Document intelligence condensed {len(governed_documents)} governed documents for {transaction.deal_name} into simplified insights covering contracts, title, insurance, and immigration readiness."
    )
    reasoning_summary = (
        f"The backend extracted key fields, validated document structure and cross-document consistency, flagged {len(anomaly_signals)} anomaly signals, "
        f"and preserved {len(audit_records)} audit events so legal, compliance, and operations teams can reproduce every conclusion."
    )
    recommended_actions = (
        "Resolve the missing permit-related attachment and re-run contract completeness validation before closing release.",
        "Keep title, insurance binder, and residency filing packets tied to the same transaction audit record.",
        "Route unresolved immigration evidence to counsel review before external submission.",
    )

    return DocumentIntelligencePacket(
        request_id=f"doc-{uuid.uuid4().hex[:8]}",
        portfolio_name=f"{transaction.deal_name} document intelligence workspace",
        simplified_summary=simplified_summary,
        reasoning_summary=reasoning_summary,
        frontend_insights=frontend_insights,
        governed_documents=governed_documents,
        extracted_fields=extracted_fields,
        validation_checks=validation_checks,
        anomaly_signals=anomaly_signals,
        compliance_findings=compliance_findings,
        audit_records=audit_records,
        release_status=release_status,
        recommended_actions=recommended_actions,
        standards_alignment=(
            "ISO/IEC 42001",
            "ISO/IEC 27001",
            "ISO/IEC 27701",
            "ISO/IEC 5259",
            "KYC/AML/sanctions",
        ),
    )


DEMO_JOURNEY_SCENARIOS = {
    "buyer": {
        "user_prompt": "I want a family relocation property in Portugal with financing guidance, transaction controls, and residency readiness.",
        "profile": {
            "role": "buyer",
            "investor_type": "owner_occupier",
            "intent": "family relocation purchase with financing support",
            "financial_intent": "primary residence with moderate appreciation",
            "country": "United States",
            "target_region": "Portugal",
            "risk_tolerance": "balanced",
            "investment_budget": 650000,
            "residency_interest": True,
            "residency_goal": "family relocation in 12 months",
            "financing_needed": True,
            "household_size": 4,
        },
        "identity": {
            "rbac_roles": ("client", "buyer"),
            "entitlements": ("decision:view", "profile:update", "transaction:approve"),
        },
        "context": {
            "journey_stage": "discovery",
            "property_country": "Portugal",
            "property_type": "apartment",
            "climate_risk": "low",
            "market_volatility": "medium",
            "session_risk": "low",
            "cross_border": True,
        },
        "transaction": {
            "deal_name": "Lisbon Green Quarter acquisition",
            "deal_type": "owner occupied purchase",
            "jurisdiction": "Portugal",
            "stage": "document_validation",
            "purchase_price": 620000,
            "target_price": 598000,
            "financing_ratio": 0.68,
            "seller_motivation": "high",
            "urgency_days": 12,
            "counterparty_risk": "medium",
            "human_approvals": ("buyer_signoff_pending", "legal_signoff_required"),
        },
        "payment": {
            "payment_method_type": "wire",
            "amount": 120000,
            "cross_border": True,
            "escrow_stage": "release_pending",
            "trusted_device": True,
            "settlement_timing": "next_day",
            "manual_review_requested": True,
            "chargeback_history_count": 0,
        },
        "insurance": {
            "persona": "buyer",
            "property_type": "apartment",
            "occupancy": "owner_occupied",
            "transaction_context": "closing",
            "property_jurisdiction": "Portugal",
            "estimated_property_value": 620000,
            "mortgage_amount": 420000,
            "household_size": 4,
            "dependents": 2,
            "landlord_exposure": False,
            "title_required": True,
            "life_priority": True,
            "prior_claims_count": 0,
        },
        "integration": {
            "partner_system": "property_registry",
            "domain": "government",
            "canonical_contract": "CanonicalPropertySubmission.v1",
            "payload_summary": "Buyer-side registry and residency filing package for a Portugal relocation purchase",
            "requested_action": "submit_filing",
            "consent_scope": ("property_registry", "residency", "document_exchange"),
        },
        "residency": {
            "target_jurisdiction": "Portugal",
            "household_size": 4,
            "dependents": 2,
            "annual_income": 168000,
            "liquid_assets": 210000,
            "property_budget": 650000,
            "property_value": 620000,
            "documents_on_file": (
                "passport",
                "proof_of_income",
                "proof_of_funds",
                "health_insurance",
                "birth_certificates",
                "tax_number",
            ),
        },
        "digital_twin": {
            "property_name": "Lisbon Green Quarter Apartment",
            "jurisdiction": "Portugal",
            "property_type": "apartment",
            "purchase_price": 620000,
            "current_value": 628000,
            "monthly_rent": 3200,
            "occupancy_rate": 0.94,
            "operating_expense_ratio": 0.28,
            "annual_insurance_premium": 2256,
            "renovation_budget": 38000,
            "renovation_uplift": 0.09,
            "appreciation_rate": 0.031,
            "financing_ratio": 0.68,
            "interest_rate": 0.047,
            "hold_years": 7,
            "climate_risk": "low",
        },
        "market_intelligence": {
            "market_scope": "Portugal relocation corridor",
            "investment_horizon_months": 18,
            "strategy_bias": "capital_preservation_with_relocation_optionality",
            "local_market": "Lisbon",
            "target_region": "Portugal",
            "interest_rate_regime": "plateauing",
            "migration_trend": "inbound_family_relocation",
            "supply_pressure": "constrained",
        },
        "tokenization": {
            "asset_name": "Lisbon Green Quarter Apartment Income SPV",
            "legal_wrapper": "Portugal SPV with nominee ledger",
            "domicile": "Portugal",
            "target_raise": 300000,
            "minimum_investment": 10000,
            "sponsor_equity_pct": 0.35,
            "retail_allocation_pct": 0.4,
            "lockup_period_days": 365,
            "transfer_policy": "Transfers require whitelist approval, cooling-off checks, and administrator reconciliation.",
            "distribution_policy": "Quarterly distributions after reserve retention, tax withholding, and administrator sign-off.",
        },
    },
    "investor": {
        "user_prompt": "I want to compare a Portugal property for yield, residency eligibility, insurance readiness, payment fraud controls, escrow release conditions, and mortgage affordability.",
        "profile": {
            "role": "investor",
            "investor_type": "cross_border",
            "intent": "cross-border property investment with residency options",
            "financial_intent": "income plus long-term appreciation",
            "country": "United States",
            "target_region": "Portugal",
            "risk_tolerance": "balanced",
            "investment_budget": 850000,
            "residency_interest": True,
            "residency_goal": "golden visa pathway for family relocation",
            "financing_needed": True,
            "household_size": 3,
        },
        "identity": {
            "rbac_roles": ("client", "investor"),
            "entitlements": ("decision:view", "decision:export", "profile:update", "transaction:approve"),
        },
        "context": {
            "journey_stage": "consideration",
            "property_country": "Portugal",
            "property_type": "apartment",
            "climate_risk": "medium",
            "market_volatility": "medium",
            "session_risk": "medium",
            "cross_border": True,
        },
        "transaction": {
            "deal_name": "Lisbon Green Quarter acquisition",
            "deal_type": "cross-border purchase",
            "jurisdiction": "Portugal",
            "stage": "document_validation",
            "purchase_price": 620000,
            "target_price": 598000,
            "financing_ratio": 0.68,
            "seller_motivation": "high",
            "urgency_days": 12,
            "counterparty_risk": "medium",
            "human_approvals": ("advisor_signoff_pending", "legal_signoff_required"),
        },
        "payment": {
            "payment_method_type": "wire",
            "amount": 120000,
            "cross_border": True,
            "escrow_stage": "release_pending",
            "trusted_device": True,
            "settlement_timing": "next_day",
            "manual_review_requested": True,
            "chargeback_history_count": 0,
        },
        "insurance": {
            "persona": "investor",
            "property_type": "multifamily",
            "occupancy": "tenant_occupied",
            "transaction_context": "closing",
            "property_jurisdiction": "Greece",
            "estimated_property_value": 880000,
            "mortgage_amount": 420000,
            "household_size": 3,
            "dependents": 2,
            "landlord_exposure": True,
            "title_required": True,
            "life_priority": True,
            "prior_claims_count": 0,
        },
        "integration": {
            "partner_system": "government_registry",
            "domain": "government",
            "canonical_contract": "CanonicalJurisdictionSubmission.v1",
            "payload_summary": "Residency filing package for property-led eligibility and land-registry verification",
            "requested_action": "submit_filing",
            "consent_scope": ("residency", "compliance", "document_exchange"),
        },
        "residency": {
            "target_jurisdiction": "Greece",
            "household_size": 3,
            "dependents": 2,
            "annual_income": 145000,
            "liquid_assets": 280000,
            "property_budget": 900000,
            "property_value": 880000,
            "documents_on_file": (
                "passport",
                "property_purchase_agreement",
                "proof_of_funds",
                "health_insurance",
                "criminal_record",
                "tax_number",
            ),
        },
        "digital_twin": {
            "property_name": "Athens Urban Residential Block",
            "jurisdiction": "Greece",
            "property_type": "multifamily",
            "purchase_price": 880000,
            "current_value": 892000,
            "monthly_rent": 6150,
            "occupancy_rate": 0.91,
            "operating_expense_ratio": 0.32,
            "annual_insurance_premium": 3864,
            "renovation_budget": 95000,
            "renovation_uplift": 0.12,
            "appreciation_rate": 0.036,
            "financing_ratio": 0.48,
            "interest_rate": 0.052,
            "hold_years": 8,
            "climate_risk": "medium",
        },
        "market_intelligence": {
            "market_scope": "Mediterranean income markets",
            "investment_horizon_months": 24,
            "strategy_bias": "income_resilience_and_optional_residency",
            "local_market": "Athens",
            "target_region": "Southern Europe",
            "interest_rate_regime": "easing_bias",
            "migration_trend": "cross_border_investor_and_worker_inflows",
            "supply_pressure": "tightening",
        },
        "tokenization": {
            "asset_name": "Athens Urban Residential Block Token Offering",
            "legal_wrapper": "Luxembourg feeder SPV with transfer-agent controls",
            "domicile": "Luxembourg",
            "target_raise": 520000,
            "minimum_investment": 25000,
            "sponsor_equity_pct": 0.3,
            "retail_allocation_pct": 0.45,
            "lockup_period_days": 540,
            "transfer_policy": "Secondary transfers require buyer KYC refresh, suitability review, whitelist approval, and settlement finality.",
            "distribution_policy": "Quarterly net-rent distributions with reserve top-ups and annual tax-statement delivery.",
        },
    },
    "advisor": {
        "user_prompt": "I need an advisor-ready transaction cockpit with document exceptions, payment controls, insurance placement readiness, and integration evidence.",
        "profile": {
            "role": "advisor",
            "investor_type": "fiduciary_operator",
            "intent": "advisor oversight for a cross-border acquisition",
            "financial_intent": "protect capital while preparing the client for approval",
            "country": "United States",
            "target_region": "Greece",
            "risk_tolerance": "balanced",
            "investment_budget": 900000,
            "residency_interest": True,
            "residency_goal": "keep investor-residency optional after diligence",
            "financing_needed": False,
            "household_size": 3,
        },
        "identity": {
            "rbac_roles": ("advisor", "transaction_manager"),
            "entitlements": ("decision:view", "decision:export", "profile:update", "transaction:approve", "transaction:escalate"),
        },
        "context": {
            "journey_stage": "transaction_review",
            "property_country": "Greece",
            "property_type": "multifamily",
            "climate_risk": "medium",
            "market_volatility": "medium",
            "session_risk": "low",
            "cross_border": True,
        },
        "transaction": {
            "deal_name": "Athens Urban Block diligence",
            "deal_type": "advisor managed acquisition",
            "jurisdiction": "Greece",
            "stage": "approval",
            "purchase_price": 880000,
            "target_price": 845000,
            "financing_ratio": 0.42,
            "seller_motivation": "medium",
            "urgency_days": 18,
            "counterparty_risk": "medium",
            "human_approvals": ("advisor_signoff_complete", "investment_committee_pending"),
        },
        "payment": {
            "payment_method_type": "escrow_disbursement",
            "amount": 180000,
            "cross_border": True,
            "escrow_stage": "funds_reserved",
            "trusted_device": True,
            "settlement_timing": "same_day",
            "manual_review_requested": False,
            "chargeback_history_count": 0,
        },
        "insurance": {
            "persona": "advisor",
            "property_type": "multifamily",
            "occupancy": "tenant_occupied",
            "transaction_context": "approval",
            "property_jurisdiction": "Greece",
            "estimated_property_value": 880000,
            "mortgage_amount": 360000,
            "household_size": 3,
            "dependents": 1,
            "landlord_exposure": True,
            "title_required": True,
            "life_priority": False,
            "prior_claims_count": 0,
        },
        "integration": {
            "partner_system": "escrow_ledger",
            "domain": "payments",
            "canonical_contract": "CanonicalEscrowInstruction.v1",
            "payload_summary": "Advisor-reviewed escrow release instruction with reconciliation and registry dependencies",
            "requested_action": "queue_release",
            "consent_scope": ("payments", "reconciliation", "audit_evidence"),
        },
        "residency": {
            "target_jurisdiction": "Greece",
            "household_size": 3,
            "dependents": 1,
            "annual_income": 210000,
            "liquid_assets": 340000,
            "property_budget": 900000,
            "property_value": 880000,
            "documents_on_file": (
                "passport",
                "proof_of_funds",
                "property_purchase_agreement",
                "health_insurance",
                "tax_number",
            ),
        },
        "digital_twin": {
            "property_name": "Athens Urban Block diligence",
            "jurisdiction": "Greece",
            "property_type": "multifamily",
            "purchase_price": 880000,
            "current_value": 898000,
            "monthly_rent": 6400,
            "occupancy_rate": 0.93,
            "operating_expense_ratio": 0.3,
            "annual_insurance_premium": 4020,
            "renovation_budget": 76000,
            "renovation_uplift": 0.1,
            "appreciation_rate": 0.034,
            "financing_ratio": 0.42,
            "interest_rate": 0.049,
            "hold_years": 6,
            "climate_risk": "medium",
        },
        "market_intelligence": {
            "market_scope": "Advisor watchlist: Greece, Spain, UAE",
            "investment_horizon_months": 12,
            "strategy_bias": "risk_gated_allocation_and_client_memoing",
            "local_market": "Athens",
            "target_region": "EMEA gateway markets",
            "interest_rate_regime": "volatile_to_stable",
            "migration_trend": "capital_plus_mobility_flows",
            "supply_pressure": "mixed",
        },
        "tokenization": {
            "asset_name": "Athens Urban Block Governance Share Class",
            "legal_wrapper": "Greek property SPV with regulated registrar sync",
            "domicile": "Greece",
            "target_raise": 400000,
            "minimum_investment": 50000,
            "sponsor_equity_pct": 0.32,
            "retail_allocation_pct": 0.28,
            "lockup_period_days": 730,
            "transfer_policy": "Advisor-reviewed transfers require IC policy approval, whitelist refresh, and dual-control release.",
            "distribution_policy": "Semiannual distributions after lender covenant checks, reserve holds, and board approval.",
        },
    },
}


def evaluate_market_intelligence(
    profile: UserProfile,
    context: RequestContext,
    market_scope: str,
    investment_horizon_months: int,
    strategy_bias: str,
    local_market: str,
    target_region: str,
    interest_rate_regime: str,
    migration_trend: str,
    supply_pressure: str,
) -> MarketIntelligencePacket:
    demand_outlook = "accelerating" if migration_trend in {"inbound_family_relocation", "cross_border_investor_and_worker_inflows", "capital_plus_mobility_flows"} else "stable"
    rate_pressure = -0.02 if interest_rate_regime == "easing_bias" else 0.0 if interest_rate_regime == "plateauing" else -0.01
    supply_tightness = 0.03 if supply_pressure in {"constrained", "tightening"} else -0.01 if supply_pressure == "expanding" else 0.0
    role_bias = 0.02 if profile.role == "investor" else 0.01 if profile.role == "advisor" else -0.005

    data_streams = (
        MarketDataStream(
            source="Global macro and rate feed",
            cadence="daily",
            coverage="Global policy rates, inflation, FX, and mortgage benchmarks",
            freshness_sla="<24h",
            features=("policy_rate_path", "inflation_nowcast", "currency_volatility", "mortgage_spreads"),
        ),
        MarketDataStream(
            source="Migration and mobility ledger",
            cadence="weekly",
            coverage="Origin-destination migration flows, visa demand, employer mobility, and household relocation intent",
            freshness_sla="<7d",
            features=("net_inflows", "household_composition", "visa_interest", "cross_border_demand"),
        ),
        MarketDataStream(
            source="Supply-demand monitor",
            cadence="daily",
            coverage="Inventory, days on market, permit issuance, absorption, rent growth, and concessions",
            freshness_sla="<24h",
            features=("active_inventory", "new_supply", "absorption_velocity", "rent_growth"),
        ),
    )

    indicators = (
        MarketIndicator(
            name="Interest-rate path",
            scope="global",
            current_value=interest_rate_regime.replace("_", " "),
            direction="supportive" if interest_rate_regime != "volatile_to_stable" else "mixed",
            impact="Financing-sensitive demand should improve as benchmark volatility cools.",
            explanation="Rate expectations feed affordability curves, refinancing windows, and exit cap-rate assumptions.",
        ),
        MarketIndicator(
            name="Migration flow",
            scope=target_region,
            current_value=migration_trend.replace("_", " "),
            direction="positive",
            impact="Cross-border household and investor inflows continue to support demand in gateway submarkets.",
            explanation="Migration pressure acts as a leading signal for rental absorption, owner-occupier demand, and school-led family moves.",
        ),
        MarketIndicator(
            name="Supply pressure",
            scope=local_market,
            current_value=supply_pressure,
            direction="tight" if supply_pressure in {"constrained", "tightening"} else "balanced",
            impact="Tighter supply keeps pricing firmer and reduces downside from inventory overhang.",
            explanation="Permit activity, active listings, and absorption velocity are fused into the local supply-demand score.",
        ),
        MarketIndicator(
            name="Investor liquidity",
            scope=market_scope,
            current_value="healthy" if context.market_volatility != "high" else "watchlist",
            direction="stable",
            impact="Capital availability remains selective but supportive for high-conviction assets.",
            explanation="Liquidity gauges how quickly investors can transact or exit without excessive price concessions.",
        ),
    )

    forecasts = (
        ForecastScenario(
            horizon="6 months",
            price_growth=round(0.021 + supply_tightness + role_bias, 3),
            rent_growth=round(0.028 + supply_tightness, 3),
            cap_rate_shift_bps=-15 if interest_rate_regime == "easing_bias" else -5 if interest_rate_regime == "plateauing" else 10,
            demand_outlook=demand_outlook,
            migration_pressure="elevated",
            confidence=0.82,
            explanation="Short-range signal blends rate-path stabilization, migration-led demand, and current absorption into a tactical market posture.",
        ),
        ForecastScenario(
            horizon="12 months",
            price_growth=round(0.034 + rate_pressure + supply_tightness + role_bias, 3),
            rent_growth=round(0.039 + supply_tightness, 3),
            cap_rate_shift_bps=-20 if interest_rate_regime == "easing_bias" else -8 if interest_rate_regime == "plateauing" else 5,
            demand_outlook="strong" if demand_outlook == "accelerating" else "steady",
            migration_pressure="elevated",
            confidence=0.79,
            explanation="Base forecast captures easing affordability constraints, inbound migration, and slow supply replenishment across target markets.",
        ),
        ForecastScenario(
            horizon=f"{investment_horizon_months} months",
            price_growth=round(0.051 + rate_pressure + supply_tightness + role_bias, 3),
            rent_growth=round(0.058 + supply_tightness, 3),
            cap_rate_shift_bps=-25 if interest_rate_regime == "easing_bias" else -10 if interest_rate_regime == "plateauing" else 0,
            demand_outlook="selectively bullish",
            migration_pressure="persistent",
            confidence=0.74,
            explanation="Longer-range outlook is produced from retrained horizon models combining macro, migration, rate, and supply-demand features for portfolio planning.",
        ),
    )

    alerts = (
        MarketAlert(
            title="Rate sensitivity compressing",
            severity="medium",
            signal="Financing spreads are improving faster than active inventory is rebuilding.",
            action="Promote financing-ready opportunities and surface affordability alerts in the frontend.",
        ),
        MarketAlert(
            title="Migration-led demand cluster",
            severity="high" if migration_trend != "stable" else "medium",
            signal=f"{local_market} is seeing sustained demand from {migration_trend.replace('_', ' ')} patterns.",
            action="Increase alerting for neighborhoods with school, transit, and visa-aligned demand concentration.",
        ),
        MarketAlert(
            title="Supply imbalance watch",
            severity="high" if supply_pressure in {"constrained", "tightening"} else "low",
            signal="Supply-demand imbalance favors owners and income strategies, but underwriting should stay disciplined.",
            action="Prioritize assets with resilient rent coverage and documented downside cases before broad market expansion.",
        ),
    )

    pipeline_status = (
        ModelPipelineStatus(stage="Streaming ingest", status="active", detail="Macro, local-market, migration, and supply-demand feeds are normalized into a governed feature store."),
        ModelPipelineStatus(stage="Feature engineering", status="active", detail="Interest-rate, inventory, migration, absorption, and affordability features are refreshed for daily inference."),
        ModelPipelineStatus(stage="Model training", status="scheduled", detail="Horizon-specific forecasting models retrain weekly with champion-challenger validation and drift checks."),
        ModelPipelineStatus(stage="Signal publication", status="active", detail="Forward-looking alerts and forecast summaries are published to investor, broker, and analyst workspaces."),
    )

    signal_summary = (
        f"Macro intelligence for {market_scope} is moderately bullish: migration flows and tight supply support demand, while the {interest_rate_regime.replace('_', ' ')} rate regime improves forward pricing and rent resilience."
    )
    recommendation = (
        f"Use the market intelligence engine to surface {investment_horizon_months}-month signals, watch migration-led demand clusters in {local_market}, and alert users when rates or supply conditions materially change the underwriting case."
    )
    explanation = (
        f"The predictive market intelligence engine fused global rate expectations, {target_region} migration flows, {local_market} supply-demand conditions, and investor-liquidity signals to generate {len(forecasts)} horizon forecasts and {len(alerts)} alerts. "
        "Backend workflows continuously ingest market data streams, retrain forecasting models, and publish explainable forward-looking signals for investors, brokers, and analysts."
    )

    return MarketIntelligencePacket(
        request_id=f"mkt-{uuid.uuid4().hex[:8]}",
        market_scope=market_scope,
        investment_horizon_months=investment_horizon_months,
        strategy_bias=strategy_bias,
        data_streams=data_streams,
        indicators=indicators,
        forecasts=forecasts,
        alerts=alerts,
        pipeline_status=pipeline_status,
        signal_summary=signal_summary,
        recommendation=recommendation,
        explanation=explanation,
        standards_alignment=("ISO/IEC 42001", "ISO/IEC 5259", "ISO 31000", "ISO/IEC 27001"),
    )


COPILOT_ROLE_LIBRARY: Dict[str, Dict[str, str]] = {
    "buyer_advisor": {
        "title": "Buyer advisor",
        "persona": "Relocating buyer",
        "focus": "Livability, affordability, timing, and next transaction steps.",
    },
    "investor_strategist": {
        "title": "Investor strategist",
        "persona": "Yield-oriented allocator",
        "focus": "Returns, downside resilience, market timing, and portfolio fit.",
    },
    "insurance_guide": {
        "title": "Insurance guide",
        "persona": "Coverage planner",
        "focus": "Coverage structures, underwriting readiness, privacy-safe quote routing.",
    },
    "visa_assistant": {
        "title": "Visa assistant",
        "persona": "Residency applicant",
        "focus": "Eligibility, documentation gaps, counsel handoffs, and filing readiness.",
    },
    "compliance_explainer": {
        "title": "Compliance explainer",
        "persona": "Risk and control reviewer",
        "focus": "Why gates passed or held, what evidence exists, and what can be released.",
    },
}


def evaluate_expert_marketplace(
    profile: UserProfile,
    identity: IdentityContext,
    context: RequestContext,
    property_packet: DecisionPacket,
    payment_packet: PaymentDecisionPacket,
    compliance_graph: ComplianceGraphPacket,
) -> ExpertMarketplacePacket:
    provider_listings = (
        MarketplaceProviderListing(
            provider_id="provider-climate-grid",
            provider_name="ClimateGrid Signals",
            provider_type="third_party_developer",
            status="production_approved",
            trust_tier="tier_1",
            sandbox_mode="remote_api_adapter",
            deployment_model="signed external API with mTLS",
            supported_jurisdictions=("EU", "UAE", "US"),
            data_classifications=("market", "property", "geospatial"),
            capabilities=(
                MarketplaceExpertCapability(
                    capability="Climate and location enrichment",
                    workflow_scope=("property ranking", "insurance", "market intelligence"),
                    invocation_mode="sync",
                    release_mode="policy-cleared explanations only",
                ),
            ),
            frontend_surfaces=("property cards", "risk banners", "market dashboards"),
            governance_notes=(
                "Only redacted property metadata and geospatial tokens leave the core router.",
                "Confidence scores are normalized against internal valuation and insurance experts before release.",
            ),
        ),
        MarketplaceProviderListing(
            provider_id="provider-aurora-insure",
            provider_name="Aurora MGA Underwriting",
            provider_type="insurer",
            status="shadow_mode",
            trust_tier="tier_2",
            sandbox_mode="hosted sandbox expert",
            deployment_model="containerized underwriting model in EstateOS sandbox",
            supported_jurisdictions=("Portugal", "Greece", "Spain"),
            data_classifications=("insurance", "property", "claims-lite"),
            capabilities=(
                MarketplaceExpertCapability(
                    capability="Quote appetite and peril scoring",
                    workflow_scope=("insurance", "closing readiness"),
                    invocation_mode="async",
                    release_mode="advisor review before quote release",
                ),
            ),
            frontend_surfaces=("insurance package comparison", "quote readiness meter"),
            governance_notes=(
                "Shadow traffic is replayed with masked personal identifiers before production cutover.",
                "Outputs stay non-binding until carrier compliance and licensing checks pass.",
            ),
        ),
        MarketplaceProviderListing(
            provider_id="provider-harbor-bank",
            provider_name="Harbor Bank Treasury APIs",
            provider_type="financial_institution",
            status="production_approved",
            trust_tier="tier_1",
            sandbox_mode="remote_api_adapter",
            deployment_model="bank-hosted treasury API with signed callbacks",
            supported_jurisdictions=("US", "EU"),
            data_classifications=("payment", "settlement", "counterparty"),
            capabilities=(
                MarketplaceExpertCapability(
                    capability="Escrow verification and settlement readiness",
                    workflow_scope=("payments", "transactions", "tokenization"),
                    invocation_mode="sync",
                    release_mode="backend-only unless settlement is cleared",
                ),
            ),
            frontend_surfaces=("payment readiness banner", "escrow timeline", "funding checklist"),
            governance_notes=(
                "Payment tokens remain PSP-bound and the provider receives only scoped settlement references.",
                "Fallback routing returns to internal payment intelligence if the treasury SLA degrades.",
            ),
        ),
        MarketplaceProviderListing(
            provider_id="provider-lexis-ai",
            provider_name="Lexis Domain AI",
            provider_type="ai_provider",
            status="review_limited",
            trust_tier="tier_2",
            sandbox_mode="hosted sandbox expert",
            deployment_model="WASM-style package pinned in marketplace runtime",
            supported_jurisdictions=("Global review set",),
            data_classifications=("documents", "compliance", "translation"),
            capabilities=(
                MarketplaceExpertCapability(
                    capability="Multilingual legal clause extraction",
                    workflow_scope=("document intelligence", "residency", "compliance"),
                    invocation_mode="async",
                    release_mode="human review for high-impact fields",
                ),
            ),
            frontend_surfaces=("document summaries", "translation badges", "evidence review queue"),
            governance_notes=(
                "The package is version-pinned and evaluated in sandbox before any tenant enablement.",
                "High-impact extraction fields require human review and reason-code capture before release.",
            ),
        ),
    )

    control_checks = (
        MarketplaceControlCheck(
            control="Provider identity and due diligence",
            status="active",
            detail="Every provider is bound to signed ownership metadata, entitlement scopes, and regional contract records before activation.",
        ),
        MarketplaceControlCheck(
            control="Sandbox and egress isolation",
            status="active",
            detail="Hosted experts run in isolated sandboxes while remote adapters use mTLS, outbound allowlists, and short-lived credentials.",
        ),
        MarketplaceControlCheck(
            control="Data minimization and privacy tier enforcement",
            status="active",
            detail=f"Router requests inherit privacy tier {identity.privacy_tier} and suppress disallowed data classes before any third-party invocation.",
        ),
        MarketplaceControlCheck(
            control="Model governance and release approval",
            status="review" if profile.role == "advisor" or context.cross_border else "active",
            detail="External experts must pass certification, shadow-mode observation, and rollback approval before promotion into live routing.",
        ),
        MarketplaceControlCheck(
            control="Kill switch and fallback routing",
            status="active",
            detail="Providers can be suspended immediately while the router falls back to internal experts or human review without breaking the workflow.",
        ),
    )

    routing_policies = (
        MarketplaceRoutingPolicy(
            policy="Eligibility gate",
            outcome="active",
            detail=f"Only providers mapped to {context.journey_stage} workflows and approved jurisdictions are considered for {profile.role} routing.",
        ),
        MarketplaceRoutingPolicy(
            policy="Normalization and ranking",
            outcome="active",
            detail=f"External outputs are scored alongside {len(property_packet.selected_experts)} internal experts and never bypass policy ranking or explanation assembly.",
        ),
        MarketplaceRoutingPolicy(
            policy="Payment and regulated action suppression",
            outcome="active",
            detail=f"Provider output can inform payment risk {payment_packet.risk_level} or compliance posture, but regulated release still depends on backend controls and {compliance_graph.graph_version} graph policy.",
        ),
        MarketplaceRoutingPolicy(
            policy="Human review threshold",
            outcome="review" if context.cross_border else "active",
            detail="Cross-border or high-impact expert contributions require advisor/compliance review before tenant-visible release or partner forwarding.",
        ),
    )

    registry_summary = (
        "EstateOS exposes a governed marketplace where external experts register through secure contracts, are routed only when policy permits, and remain subordinate to the platform's explainability and release gates."
    )
    governance_summary = (
        "Marketplace governance spans provider onboarding, certification, sandbox execution, tenant entitlement, rollback controls, and continuous monitoring so third-party intelligence expands the MoE fabric without expanding the trust boundary."
    )
    compliance_summary = (
        "The expert ecosystem enforces ISO/IEC 27001, ISO/IEC 27017, ISO/IEC 27701, ISO/IEC 42001, ISO/IEC 5259, SOC 2 Type 2, and regulated-workflow controls such as PCI DSS and KYC/AML scope minimization before external intelligence reaches users or partners."
    )

    return ExpertMarketplacePacket(
        request_id=f"mkt-{uuid.uuid4().hex[:8]}",
        marketplace_status="governed_expandable",
        registry_summary=registry_summary,
        providers=provider_listings,
        control_checks=control_checks,
        routing_policies=routing_policies,
        frontend_capabilities=(
            "Marketplace catalog for approved experts and partner capabilities",
            "Workflow-specific capability badges in property, insurance, payments, documents, and compliance surfaces",
            "Admin enablement toggles with sandbox, review, and production labels",
            "Explainability notices whenever external intelligence influenced a recommendation or routed action",
        ),
        governance_summary=governance_summary,
        compliance_summary=compliance_summary,
        recommended_actions=(
            "Introduce expert registration, certification, and kill-switch APIs before enabling tenant self-service onboarding.",
            "Keep hosted plug-ins sandboxed with outbound allowlists, signed package promotion, and version pinning.",
            "Require shadow-mode evidence and human approval before any expert can influence regulated or high-impact workflows.",
        ),
        standards_alignment=(
            "ISO/IEC 27001",
            "ISO/IEC 27017",
            "ISO/IEC 27701",
            "ISO/IEC 42001",
            "ISO/IEC 5259",
            "SOC 2 Type 2",
            "PCI DSS / KYC-AML scope controls",
        ),
    )


def evaluate_conversational_copilot(
    profile: UserProfile,
    identity: IdentityContext,
    context: RequestContext,
    property_packet: DecisionPacket,
    transaction_packet: TransactionDecisionPacket,
    residency_packet: ResidencyEligibilityPacket,
    insurance_packet: InsuranceDecisionPacket,
    payment_packet: PaymentDecisionPacket,
    market_packet: MarketIntelligencePacket,
) -> CopilotDecisionPacket:
    def value(item: object, key: str):
        return item[key] if isinstance(item, dict) else getattr(item, key)

    active_role = {
        "buyer": "buyer_advisor",
        "investor": "investor_strategist",
        "advisor": "compliance_explainer",
    }.get(profile.role, "buyer_advisor")
    top_recommendation = property_packet.ranked_recommendations[0]
    insurance_recommendation = insurance_packet.recommendations[0]
    elevated_gate_count = sum(1 for gate in property_packet.policy_gates if value(gate, "status") != "passed")
    held_controls = [value(gate, "name") for gate in property_packet.policy_gates if value(gate, "status") != "passed"]

    role_summaries = (
        CopilotRoleSummary(
            role_key="buyer_advisor",
            title="Buyer advisor",
            persona="Guides owner-occupiers through shortlist fit, financing, and next steps.",
            focus="Property fit, affordability, family relocation logistics, and transaction sequencing.",
            confidence=round(value(top_recommendation, "confidence"), 2),
            summary=f"Recommends {value(top_recommendation, 'title')} because livability, financing readiness, and low-friction execution outperform the alternatives.",
        ),
        CopilotRoleSummary(
            role_key="investor_strategist",
            title="Investor strategist",
            persona="Frames investments through risk-adjusted return and macro context.",
            focus="Yield resilience, downside cases, market signals, and capital allocation discipline.",
            confidence=round(min(0.99, value(top_recommendation, "composite_score") + 0.03), 2),
            summary=f"Links {value(top_recommendation, 'title')} to {market_packet.market_scope} signals, emphasizing {market_packet.forecasts[1].horizon} demand resilience and documented downside cases.",
        ),
        CopilotRoleSummary(
            role_key="insurance_guide",
            title="Insurance guide",
            persona="Translates underwriting and servicing requirements into actionable coverage advice.",
            focus="Coverage fit, premium tradeoffs, data minimization, and quote-release posture.",
            confidence=0.84,
            summary=f"Maps the property profile to {insurance_recommendation.coverage_type} with privacy-safe ACORD exchange controls and a {insurance_packet.release_status} release posture.",
        ),
        CopilotRoleSummary(
            role_key="visa_assistant",
            title="Visa assistant",
            persona="Explains residency eligibility and outstanding filing evidence.",
            focus="Program fit, document readiness, source-of-funds checks, and counsel handoff readiness.",
            confidence=round(residency_packet.eligibility_score, 2),
            summary=f"Explains the {residency_packet.program} decision, including {len(residency_packet.document_checks)} tracked evidence items and the steps needed for filing readiness.",
        ),
        CopilotRoleSummary(
            role_key="compliance_explainer",
            title="Compliance explainer",
            persona="Makes control outcomes understandable without hiding risk details.",
            focus="Release gating, privacy boundaries, audit evidence, and explainability controls.",
            confidence=0.94,
            summary=f"Summarizes {len(property_packet.policy_gates)} policy gates, {len(transaction_packet.compliance_controls)} transaction controls, and {payment_packet.risk_level} payment risk before any sensitive action is released.",
        ),
    )

    conversation = (
        CopilotMessage(
            speaker="user",
            role=COPILOT_ROLE_LIBRARY[active_role]["title"],
            text=f"I need a clear recommendation for my {profile.role} journey and I want to understand the risks before I move forward.",
            sources=("frontend intake", "journey profile"),
        ),
        CopilotMessage(
            speaker="assistant",
            role=COPILOT_ROLE_LIBRARY[active_role]["title"],
            text=(
                f"My top recommendation is {value(top_recommendation, 'title')}. The MoE system blended property, investment, finance, compliance, "
                f"and market signals to reach a {property_packet.release_status} release with {len(property_packet.selected_experts)} routed experts."
            ),
            sources=("property_decision.recommendation", "property_decision.selected_experts"),
        ),
        CopilotMessage(
            speaker="assistant",
            role="Compliance explainer",
            text=(
                f"Nothing is hidden: {elevated_gate_count} policy gates still require attention ({', '.join(held_controls) if held_controls else 'no elevated gates'}), "
                f"transaction risk is {transaction_packet.risk_rating}, and payment risk is {payment_packet.risk_level}."
            ),
            sources=("property_decision.policy_gates", "transaction_decision.risk_rating", "payment_decision.risk_level"),
        ),
    )

    memory = (
        CopilotMemoryItem(label="User role", value=profile.role, source="profile", retention="session + audit excerpt"),
        CopilotMemoryItem(label="Primary objective", value=profile.intent, source="profile", retention="session"),
        CopilotMemoryItem(label="Budget", value=f"{profile.investment_budget:,} USD", source="profile", retention="session"),
        CopilotMemoryItem(label="Top recommendation", value=value(top_recommendation, "title"), source="property decision", retention="decision record"),
        CopilotMemoryItem(label="Residency status", value=residency_packet.eligibility_status, source="residency decision", retention="decision record"),
        CopilotMemoryItem(label="Insurance release", value=insurance_packet.release_status, source="insurance decision", retention="decision record"),
    )

    reasoning_trace = (
        CopilotReasoningStep(
            step="Intent and role detection",
            experts=("ux_personalization", "conversational_copilot"),
            detail=f"The copilot aligns the response to the {profile.role} journey, {profile.intent} objective, and {context.journey_stage} stage before choosing an answer style.",
        ),
        CopilotReasoningStep(
            step="MoE evidence retrieval",
            experts=tuple(value(item, "expert") for item in property_packet.selected_experts[:4]),
            detail="Property, investment, finance, and compliance summaries are pulled first so the response cites governed recommendations instead of free-form opinion.",
        ),
        CopilotReasoningStep(
            step="Role-specific synthesis",
            experts=("conversational_copilot", "residency_eligibility", "insurance_matching"),
            detail="The copilot reframes the same evidence differently for buyer, investor, visa, insurance, or compliance conversations without changing the underlying facts.",
        ),
        CopilotReasoningStep(
            step="Guarded release",
            experts=("compliance_validation", "unified_compliance_risk_intelligence"),
            detail="Before answering, the system checks privacy tier, consent scope, audit logging, and hold conditions so only policy-cleared details appear in the conversation.",
        ),
    )

    guardrails = (
        CopilotGuardrail(control="Context memory minimization", status="active", detail="Short-term memory stores only journey objectives, released decisions, and approved evidence references; raw PII stays outside the chat transcript."),
        CopilotGuardrail(control="Role-specific reasoning", status="active", detail="Every answer is conditioned on the selected role so buyers, investors, insurance users, and compliance reviewers get the same facts with different framing."),
        CopilotGuardrail(control="Explainability trace", status="active", detail="Each answer points back to MoE packets, expert summaries, and policy-gate outcomes instead of opaque free generation."),
        CopilotGuardrail(control="Compliance-aware release", status="review" if elevated_gate_count else "active", detail=f"Responses inherit policy-gate results and currently track {elevated_gate_count} elevated gates before export or partner release."),
    )

    recommended_actions = (
        value(property_packet.expert_outputs[0], "next_actions")[0],
        transaction_packet.recommendations[0],
        insurance_packet.recommendations[0].rationale,
        residency_packet.compliance_workflow[-1].detail,
    )
    explainability_summary = (
        "The conversational copilot is an interface over the existing MoE packets: it retains role context, cites expert outputs, and exposes reasoning steps so the answer can be challenged or audited."
    )
    privacy_summary = (
        f"Conversation memory follows the {identity.privacy_tier} privacy tier, respects consent scope {list(identity.consent_scope)}, and limits release to role-approved details with audit logging."
    )
    compliance_summary = (
        f"Compliance posture spans {len(property_packet.policy_gates)} property gates, {len(transaction_packet.compliance_controls)} transaction controls, residency status '{residency_packet.eligibility_status}', and payment risk '{payment_packet.risk_level}'."
    )

    return CopilotDecisionPacket(
        request_id=f"cop-{uuid.uuid4().hex[:8]}",
        active_role=active_role,
        roles=role_summaries,
        conversation=conversation,
        memory=memory,
        reasoning_trace=reasoning_trace,
        guardrails=guardrails,
        recommended_actions=recommended_actions,
        explainability_summary=explainability_summary,
        privacy_summary=privacy_summary,
        compliance_summary=compliance_summary,
        natural_language_interfaces=(
            "guided chat answers",
            "role switcher for buyer, investor, insurance, visa, and compliance modes",
            "context memory cards",
            "reasoning trace with cited expert evidence",
        ),
        release_status="review" if elevated_gate_count else "ready",
        standards_alignment=("ISO/IEC 42001", "ISO/IEC 27701", "ISO/IEC 27001", "ISO/IEC 5259"),
    )


def build_demo_payloads(journey_key: str = "investor") -> Dict[str, object]:
    scenario = DEMO_JOURNEY_SCENARIOS.get(journey_key, DEMO_JOURNEY_SCENARIOS["investor"])

    profile = UserProfile(**scenario["profile"])
    identity = IdentityContext(
        subject_id=f"usr-{uuid.uuid4().hex[:8]}",
        auth_assurance_level="aal2",
        mfa_completed=True,
        kyc_status="approved",
        aml_risk="medium",
        sanctions_status="clear",
        privacy_tier="confidential",
        consent_scope=("routing", "kyc", "personalization", "evidence_retention"),
        pii_tags=("identity", "financial", "residency"),
        **scenario["identity"],
    )
    context = RequestContext(
        request_id=f"req-{uuid.uuid4().hex[:8]}",
        channel="web",
        locale="en-US",
        has_verified_identity=True,
        has_consent=True,
        **scenario["context"],
    )
    packet = orchestrate(
        user_prompt=scenario["user_prompt"],
        profile=profile,
        identity=identity,
        context=context,
    )

    transaction = TransactionCase(
        transaction_id=f"deal-{uuid.uuid4().hex[:8]}",
        requested_documents=(
            TransactionDocument(
                document_id="doc-title",
                name="Title and encumbrance report",
                status="validated",
                document_type="title",
                owner="Legal counsel",
                issues=(),
                compliance_tags=("records", "jurisdiction"),
                last_checked_utc=datetime.now(timezone.utc).isoformat(),
            ),
            TransactionDocument(
                document_id="doc-disclosure",
                name="Seller disclosure package",
                status="review",
                document_type="disclosure",
                owner="Broker",
                issues=("Missing renovation permit attachment",),
                compliance_tags=("records", "privacy"),
                last_checked_utc=datetime.now(timezone.utc).isoformat(),
            ),
            TransactionDocument(
                document_id="doc-finance",
                name="Lender commitment letter",
                status="validated",
                document_type="financing",
                owner="Lender",
                issues=(),
                compliance_tags=("records", "business_continuity"),
                last_checked_utc=datetime.now(timezone.utc).isoformat(),
            ),
        ),
        workflow_stages=(
            TransactionStageStatus(stage="intake", status="completed", completion=1.0, owner="Broker ops", control_checks=("identity bound", "consent captured")),
            TransactionStageStatus(stage="pricing_review", status="completed", completion=1.0, owner="Deal desk", control_checks=("pricing memo stored", "approval recorded")),
            TransactionStageStatus(stage="negotiation", status="completed", completion=1.0, owner="Advisor", control_checks=("counter trail stored", "deadline evidence stored")),
            TransactionStageStatus(stage="document_validation", status="in_progress", completion=0.72, owner="Legal counsel", control_checks=("document hash stored", "exception list open"), blocker="Pending permit attachment"),
            TransactionStageStatus(stage="approval", status="pending", completion=0.1, owner="Transaction manager", control_checks=("segregation of duties", "release gate pending")),
            TransactionStageStatus(stage="closing", status="pending", completion=0.0, owner="Closing agent", control_checks=("continuity runbook attached",)),
        ),
        bcdr_tier="tier_1",
        **scenario["transaction"],
    )
    transaction_packet = orchestrate_transaction(transaction, identity, context)
    payment_packet = evaluate_payment_risk(
        PaymentRequest(
            transaction_reference=transaction.transaction_id,
            payer_id=identity.subject_id,
            currency="USD",
            **scenario["payment"],
        ),
        identity,
        context,
    )
    insurance_packet = evaluate_insurance_options(
        InsuranceApplicantProfile(
            applicant_id=identity.subject_id,
            privacy_consent=True,
            **scenario["insurance"],
        ),
        identity,
        context,
    )
    integration_packet = evaluate_integration_request(
        PartnerIntegrationRequest(
            data_classification="restricted",
            **scenario["integration"],
        ),
        identity,
        context,
    )
    residency_packet = evaluate_residency_eligibility(
        ResidencyApplicantProfile(
            applicant_id=identity.subject_id,
            citizenship_country="United States",
            current_country="United States",
            source_of_funds_verified=True,
            criminal_record_clear=True,
            health_insurance_ready=True,
            **scenario["residency"],
        ),
        identity,
    )
    compliance_graph_packet = evaluate_compliance_graph(
        profile,
        identity,
        context,
        transaction,
        payment_packet,
        insurance_packet,
        residency_packet,
    )
    digital_twin_packet = evaluate_digital_twin(
        DigitalTwinInput(
            twin_id=f"twin-{uuid.uuid4().hex[:8]}",
            **scenario["digital_twin"],
        ),
        identity,
        context,
    )
    market_intelligence_packet = evaluate_market_intelligence(
        profile,
        context,
        **scenario["market_intelligence"],
    )
    document_intelligence_packet = evaluate_document_intelligence(
        profile,
        identity,
        context,
        transaction,
        insurance_packet,
        residency_packet,
    )
    trust_reputation_packet = evaluate_trust_reputation_network(
        profile,
        identity,
        context,
        transaction,
        payment_packet,
        document_intelligence_packet,
        compliance_graph_packet,
    )
    tokenization_packet = evaluate_tokenization(
        profile,
        identity,
        context,
        transaction,
        **scenario["tokenization"],
    )
    marketplace_packet = evaluate_expert_marketplace(
        profile,
        identity,
        context,
        packet,
        payment_packet,
        compliance_graph_packet,
    )
    copilot_packet = evaluate_conversational_copilot(
        profile,
        identity,
        context,
        packet,
        transaction_packet,
        residency_packet,
        insurance_packet,
        payment_packet,
        market_intelligence_packet,
    )

    return {
        "journey_key": journey_key,
        "property_decision": asdict(packet),
        "transaction_decision": asdict(transaction_packet),
        "payment_decision": asdict(payment_packet),
        "insurance_decision": asdict(insurance_packet),
        "integration_decision": asdict(integration_packet),
        "residency_decision": asdict(residency_packet),
        "compliance_graph_decision": asdict(compliance_graph_packet),
        "digital_twin_decision": asdict(digital_twin_packet),
        "market_intelligence_decision": asdict(market_intelligence_packet),
        "document_intelligence_decision": asdict(document_intelligence_packet),
        "trust_reputation_decision": asdict(trust_reputation_packet),
        "marketplace_decision": asdict(marketplace_packet),
        "tokenization_decision": asdict(tokenization_packet),
        "copilot_decision": asdict(copilot_packet),
    }


def demo() -> None:
    print(json.dumps(build_demo_payloads(), indent=2))


if __name__ == "__main__":
    demo()

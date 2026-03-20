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
        name="ux_personalization",
        specialties=("journey_guidance", "messaging", "next_best_action"),
        triggers=("help", "next", "summary", "compare", "guide"),
        compliance_dependencies=("privacy",),
        min_confidence=0.52,
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
        "ux_personalization": ExpertOutput(
            expert="ux_personalization",
            summary="Explanation depth and next-best actions were tailored to the current user journey.",
            confidence=0.78,
            evidence=("persona mapping", "journey stage", "explanation depth preference"),
            next_actions=("adjust explanation depth", "surface guided tasks"),
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
    },
}


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
    digital_twin_packet = evaluate_digital_twin(
        DigitalTwinInput(
            twin_id=f"twin-{uuid.uuid4().hex[:8]}",
            **scenario["digital_twin"],
        ),
        identity,
        context,
    )

    return {
        "journey_key": journey_key,
        "property_decision": asdict(packet),
        "transaction_decision": asdict(transaction_packet),
        "payment_decision": asdict(payment_packet),
        "insurance_decision": asdict(insurance_packet),
        "integration_decision": asdict(integration_packet),
        "residency_decision": asdict(residency_packet),
        "digital_twin_decision": asdict(digital_twin_packet),
    }


def demo() -> None:
    print(json.dumps(build_demo_payloads(), indent=2))


if __name__ == "__main__":
    demo()

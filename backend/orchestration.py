"""EstateOS Mixture-of-Experts orchestration reference implementation.

This module provides a dependency-light Python blueprint for how EstateOS can:
- capture identity, trust, and profile signals from the frontend,
- detect user intents,
- assemble user/profile/context signals,
- route work to specialized experts,
- enforce policy gates,
- emit auditable event records,
- build an explainable decision packet.
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
        name="ux_personalization",
        specialties=("journey_guidance", "messaging", "next_best_action"),
        triggers=("help", "next", "summary", "compare", "guide"),
        compliance_dependencies=("privacy",),
        min_confidence=0.52,
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
    "finance": "financial_risk",
    "compliance": "compliance_validation",
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
    "model_risk": "Record model lineage, confidence, bias review, and evaluation thresholds for AI-assisted outputs.",
    "data_quality": "Apply ISO/IEC 5259-aligned controls for data provenance, completeness, freshness, comparability, and traceable remediation.",
    "fairness": "Measure ranking fairness, disparate impact, and preference weighting drift before releasing recommendations.",
    "explainability": "Preserve user-facing reasons, comparable-set rationale, and feature contribution summaries for each decision.",
    "ai_management": "Operate the AI management system under ISO/IEC 42001 with documented ownership, risk treatment, and human oversight.",
    "risk_thresholds": "Block release when fraud, climate, cyber, session, or financial risks exceed threshold.",
    "records": "Write immutable audit logs with inputs, outputs, lineage, approvals, and identity state.",
    "suitability": "Check affordability, investor category, and product suitability against client profile and constraints.",
    "data_residency": "Apply region-aware storage, transfer, retention, and deletion constraints to profile and decision data.",
}

AZURE_SERVICES: Sequence[str] = (
    "Azure Front Door",
    "Azure API Management",
    "Microsoft Entra External ID",
    "Azure Kubernetes Service",
    "Azure Container Apps",
    "Azure Functions",
    "Azure Service Bus",
    "Azure Event Grid",
    "Azure SQL",
    "Azure Cosmos DB",
    "Azure Data Lake Storage Gen2",
    "Azure AI Search",
    "Azure OpenAI",
    "Azure Key Vault",
    "Azure Monitor",
    "Microsoft Purview",
    "Microsoft Sentinel",
)

STANDARDS_ALIGNMENT: Sequence[str] = (
    "ISO/IEC 27001",
    "ISO/IEC 27017",
    "ISO/IEC 27701",
    "SOC 2 Type 2",
    "ISO/IEC 25010",
    "ISO/IEC 5259",
    "ISO/IEC 42001",
    "ISO 22301",
    "ISO 31000",
    "ISO 9241-210",
)


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
                "ux_personalization": 0.8,
            },
            "price": 890000,
            "valuation_band": "$860k-$915k",
            "comparable_summary": "Comparable income assets and rent comps support a balanced valuation case.",
            "trend_signal": "Healthy income demand with moderate policy watchlist exposure.",
            "location_intelligence": "Residency optionality and urban access strengthen client optionality.",
            "recommendation_rationale": "Recommendation expert keeps this close because the preference mix between yield and residency is compelling.",
            "investment_insight": "Stronger than Barcelona when optional residency matters more than memo simplicity.",
            "visa_pathway": "Greece residency planning remains a useful optional pathway for the client.",
            "insurance_option": "Residential income cover plus catastrophe rider with moderate complexity.",
        },
        {
            "candidate_id": "dubai-premium-diversifier",
            "title": "Dubai Premium Diversifier",
            "geography": "Dubai, UAE",
            "category": "property",
            "summary": "High-upside recommendation reserved for aggressive clients comfortable with premium carry.",
            "base_scores": {
                "property_valuation": 0.9,
                "investment_analysis": 0.87,
                "listing_recommendation": 0.74,
                "residency_eligibility": 0.89,
                "insurance_matching": 0.71,
                "financial_risk": 0.69,
                "compliance_validation": 0.93,
                "ux_personalization": 0.78,
            },
            "price": 1450000,
            "valuation_band": "$1.39M-$1.49M",
            "comparable_summary": "High-end comparables support the value range but show wider volatility bands.",
            "trend_signal": "Premium growth potential remains strong but is more cyclical under rate or FX shocks.",
            "location_intelligence": "Global mobility is attractive, though cost-to-fit is weakest for conservative advisory use.",
            "recommendation_rationale": "Recommendation expert places it last because suitability and premium carry outweigh upside for this persona.",
            "investment_insight": "Only advisable when the client explicitly accepts cyclical and carry exposure.",
            "visa_pathway": "UAE investor route is compelling but should be paired with suitability review.",
            "insurance_option": "High-value diversified cover with the heaviest carrying cost of the three.",
        },
    ),
}


def detect_intents(user_prompt: str, profile: UserProfile) -> List[str]:
    prompt = (
        f"{user_prompt.lower()} {profile.intent.lower()} {profile.financial_intent.lower()} "
        f"{profile.residency_goal.lower()} {profile.investor_type.lower()}"
    )
    intents: List[str] = []
    for keyword, intent in INTENT_KEYWORDS.items():
        if keyword in prompt and intent not in intents:
            intents.append(intent)
    if profile.residency_interest and "residency" not in intents:
        intents.append("residency")
    if profile.financing_needed and "finance" not in intents:
        intents.append("finance")
    return intents or ["property_search", "valuation", "compliance"]


def score_expert(
    expert: ExpertCard,
    user_prompt: str,
    profile: UserProfile,
    identity: IdentityContext,
    context: RequestContext,
    detected_intents: Iterable[str],
) -> float:
    prompt = user_prompt.lower()
    trigger_hits = sum(1 for trigger in expert.triggers if trigger in prompt)
    specialty_hits = sum(1 for specialty in expert.specialties if specialty in " ".join(detected_intents))
    mapped_intent_hits = sum(1 for intent in detected_intents if INTENT_EXPERT_MAP.get(intent) == expert.name)
    profile_bonus = 0.0

    if expert.name == "investment_analysis" and profile.role == "investor":
        profile_bonus += 0.14
    if expert.name == "investment_analysis" and profile.investor_type in {"institutional", "cross_border"}:
        profile_bonus += 0.08
    if expert.name == "listing_recommendation":
        profile_bonus += 0.12
    if expert.name == "residency_eligibility" and profile.residency_interest:
        profile_bonus += 0.20
    if expert.name == "residency_eligibility" and context.cross_border:
        profile_bonus += 0.08
    if expert.name == "financial_risk" and profile.financing_needed:
        profile_bonus += 0.18
    if expert.name == "insurance_matching" and context.climate_risk in {"medium", "high"}:
        profile_bonus += 0.14
    if expert.name == "property_valuation" and context.market_volatility in {"medium", "high"}:
        profile_bonus += 0.10
    if expert.name == "property_valuation" and context.cross_border:
        profile_bonus += 0.06
    if expert.name == "listing_recommendation" and profile.residency_interest:
        profile_bonus += 0.05
    if expert.name == "listing_recommendation" and context.cross_border:
        profile_bonus += 0.04
    if expert.name == "ux_personalization":
        profile_bonus += 0.10
    if expert.name == "compliance_validation":
        profile_bonus += 0.24
    if identity.kyc_status != "approved" and expert.name in {"residency_eligibility", "investment_analysis"}:
        profile_bonus += 0.05
    if identity.aml_risk in {"medium", "high"} and expert.name == "compliance_validation":
        profile_bonus += 0.08
    if context.session_risk == "high" and expert.name == "compliance_validation":
        profile_bonus += 0.10
    raw_score = min(0.32 + trigger_hits * 0.11 + specialty_hits * 0.07 + mapped_intent_hits * 0.17 + profile_bonus, 0.99)
    return round(raw_score, 2)


def route_experts(
    user_prompt: str,
    profile: UserProfile,
    identity: IdentityContext,
    context: RequestContext,
    detected_intents: Sequence[str],
) -> List[ExpertDecision]:
    selections: List[ExpertDecision] = []
    for expert in EXPERT_REGISTRY:
        score = score_expert(expert, user_prompt, profile, identity, context, detected_intents)
        if score >= expert.min_confidence:
            rationale = (
                f"Selected for role={profile.role}, investor_type={profile.investor_type}, journey={context.journey_stage}, "
                f"intents={list(detected_intents)}, auth_assurance={identity.auth_assurance_level}, "
                f"kyc_status={identity.kyc_status}, and contextual triggers with score {score:.2f}."
            )
            selections.append(
                ExpertDecision(
                    expert=expert.name,
                    score=score,
                    rationale=rationale,
                    execution_mode=expert.execution_mode,
                )
            )
    if not any(choice.expert == "listing_recommendation" for choice in selections) and any(
        choice.expert in {"property_valuation", "investment_analysis", "residency_eligibility"} for choice in selections
    ):
        selections.append(
            ExpertDecision(
                expert="listing_recommendation",
                score=0.83,
                rationale="Added to rank listings against explicit user preferences, valuation confidence, and explainability controls.",
                execution_mode="sync",
            )
        )
    if not any(choice.expert == "compliance_validation" for choice in selections):
        selections.append(
            ExpertDecision(
                expert="compliance_validation",
                score=0.95,
                rationale="Added as mandatory release gate for all regulated real-estate and investment workflows.",
                execution_mode="sync",
            )
        )
    if not any(choice.expert == "ux_personalization" for choice in selections):
        selections.append(
            ExpertDecision(
                expert="ux_personalization",
                score=0.70,
                rationale="Added to translate expert outputs into a seamless persona-aware frontend experience.",
                execution_mode="sync",
            )
        )
    return sorted(selections, key=lambda item: item.score, reverse=True)


def collect_policy_dependencies(selected_experts: Sequence[ExpertDecision]) -> List[str]:
    dependencies: List[str] = []
    lookup = {expert.name: expert for expert in EXPERT_REGISTRY}
    baseline_dependencies = ["privacy", "rbac", "mfa", "records"]
    for dependency in baseline_dependencies:
        dependencies.append(dependency)

    for selected in selected_experts:
        card = lookup.get(selected.expert)
        if not card:
            continue
        for dependency in card.compliance_dependencies:
            if dependency == "all":
                for gate in POLICY_GATES:
                    if gate not in dependencies:
                        dependencies.append(gate)
            elif dependency not in dependencies:
                dependencies.append(dependency)
    return dependencies


def evaluate_policy_gates(
    policy_dependencies: Sequence[str],
    profile: UserProfile,
    identity: IdentityContext,
    context: RequestContext,
) -> List[PolicyGateResult]:
    results: List[PolicyGateResult] = []
    entitlement_set = set(identity.entitlements)
    role_set = set(identity.rbac_roles)
    needs_privileged_action = profile.role in {"advisor", "broker"} or context.journey_stage in {"approval", "release"}

    for dependency in policy_dependencies:
        status = "passed"
        if dependency == "privacy" and (not context.has_consent or not identity.consent_scope):
            status = "blocked"
        elif dependency == "rbac" and not ({profile.role, "client"} & role_set):
            status = "blocked"
        elif dependency == "rbac" and needs_privileged_action and "decision:approve" not in entitlement_set:
            status = "review"
        elif dependency == "mfa" and (needs_privileged_action or context.session_risk == "high") and not identity.mfa_completed:
            status = "blocked"
        elif dependency == "kyc" and (not context.has_verified_identity or identity.kyc_status not in {"approved", "simplified"}):
            status = "blocked"
        elif dependency == "aml" and identity.aml_risk == "high":
            status = "review"
        elif dependency == "sanctions" and identity.sanctions_status != "clear":
            status = "blocked"
        elif dependency == "risk_thresholds" and context.climate_risk == "high" and profile.risk_tolerance == "conservative":
            status = "review"
        elif dependency == "data_quality" and context.market_volatility == "high":
            status = "review"
        elif dependency == "fairness" and profile.role == "advisor" and "decision:approve" not in entitlement_set:
            status = "review"
        elif dependency == "explainability" and identity.privacy_tier == "restricted":
            status = "review"
        elif dependency == "ai_management" and context.journey_stage in {"approval", "release"} and not identity.mfa_completed:
            status = "blocked"
        elif dependency == "data_residency" and context.cross_border and identity.privacy_tier == "restricted":
            status = "review"
        results.append(
            PolicyGateResult(
                name=dependency,
                status=status,
                details=POLICY_GATES[dependency],
            )
        )
    return results


def build_expert_outputs(
    profile: UserProfile,
    identity: IdentityContext,
    context: RequestContext,
    selected_experts: Sequence[ExpertDecision],
) -> List[ExpertOutput]:
    outputs: List[ExpertOutput] = []
    for decision in selected_experts:
        if decision.expert == "property_valuation":
            outputs.append(
                ExpertOutput(
                    expert=decision.expert,
                    summary=(
                        f"Estimated fair-value band prepared for the {context.property_type} in {context.property_country} "
                        f"using market data, comparable sets, trend signals, and location intelligence for a {profile.investor_type} {profile.role}."
                    ),
                    confidence=round(max(decision.score - 0.03, 0.5), 2),
                    evidence=("listing metadata", "market comparables", "trend features", "location intelligence"),
                    next_actions=("Review comparable sales", "Inspect trend and location assumptions"),
                )
            )
        elif decision.expert == "investment_analysis":
            outputs.append(
                ExpertOutput(
                    expert=decision.expert,
                    summary=(
                        f"Scenario analysis ranked {profile.financial_intent} pathways using yield, downside resilience, "
                        "liquidity constraints, and investor-type suitability."
                    ),
                    confidence=round(max(decision.score - 0.02, 0.5), 2),
                    evidence=("rent comps", "rate assumptions", "cash-flow scenarios"),
                    next_actions=("Compare target hold periods", "Review downside scenario"),
                )
            )
        elif decision.expert == "listing_recommendation":
            outputs.append(
                ExpertOutput(
                    expert=decision.expert,
                    summary=(
                        "Preference-aware ranking combined valuation confidence, market trends, comparables, location intelligence, "
                        "fairness checks, and user goals into an explainable listing order."
                    ),
                    confidence=round(max(decision.score - 0.03, 0.5), 2),
                    evidence=("preference profile", "ranking feature weights", "fairness diagnostics"),
                    next_actions=("Inspect why-this-rank ledger", "Review preference weighting and tie-breaks"),
                )
            )
        elif decision.expert == "residency_eligibility":
            outputs.append(
                ExpertOutput(
                    expert=decision.expert,
                    summary=(
                        f"Residency pathways were screened for {profile.country} applicants pursuing {profile.residency_goal} "
                        f"through {context.property_country} assets."
                    ),
                    confidence=round(max(decision.score - 0.04, 0.5), 2),
                    evidence=("jurisdiction rules", "budget thresholds", "family composition"),
                    next_actions=("Confirm qualifying pathway", "Collect legal evidence"),
                )
            )
        elif decision.expert == "insurance_matching":
            outputs.append(
                ExpertOutput(
                    expert=decision.expert,
                    summary="Insurance matching evaluated peril exposure, coverage fit, quote readiness, and jurisdictional servicing constraints.",
                    confidence=round(max(decision.score - 0.04, 0.5), 2),
                    evidence=("property exposure data", "hazard model", "carrier appetite rules"),
                    next_actions=("Review exclusions", "Prepare ACORD intake"),
                )
            )
        elif decision.expert == "financial_risk":
            outputs.append(
                ExpertOutput(
                    expert=decision.expert,
                    summary=(
                        f"Financial risk analysis measured affordability, leverage, liquidity, and financing resilience for "
                        f"the stated intent '{profile.financial_intent}'."
                    ),
                    confidence=round(max(decision.score - 0.03, 0.5), 2),
                    evidence=("income profile", "liability snapshot", "rate stress tests"),
                    next_actions=("Validate financing plan", "Review affordability buffer"),
                )
            )
        elif decision.expert == "compliance_validation":
            outputs.append(
                ExpertOutput(
                    expert=decision.expert,
                    summary=(
                        "Compliance release checks validated RBAC, MFA, identity assurance, KYC/AML posture, sanctions status, "
                        "privacy controls, suitability, and recordkeeping obligations."
                    ),
                    confidence=round(max(decision.score - 0.01, 0.5), 2),
                    evidence=("identity evidence", "policy registry", "screening logs"),
                    next_actions=("Resolve blocked gates", "Attach missing evidence if required"),
                )
            )
        elif decision.expert == "ux_personalization":
            outputs.append(
                ExpertOutput(
                    expert=decision.expert,
                    summary=(
                        f"Frontend response was tailored for locale {context.locale}, privacy tier {identity.privacy_tier}, and "
                        f"role {profile.role} into confidence-aware language and next-best actions."
                    ),
                    confidence=round(max(decision.score - 0.05, 0.5), 2),
                    evidence=("persona rules", "journey stage", "decision confidence"),
                    next_actions=("Show explanation drawer", "Highlight next required action"),
                )
            )
    return outputs


def build_ranking_weights(profile: UserProfile, context: RequestContext) -> Dict[str, float]:
    weights: Dict[str, float] = {
        "property_valuation": 0.17,
        "investment_analysis": 0.16,
        "listing_recommendation": 0.16,
        "residency_eligibility": 0.13,
        "insurance_matching": 0.12,
        "financial_risk": 0.14,
        "compliance_validation": 0.08,
        "ux_personalization": 0.04,
    }

    if profile.role == "buyer":
        weights["property_valuation"] += 0.08
        weights["listing_recommendation"] += 0.08
        weights["financial_risk"] += 0.06
    if profile.role == "investor":
        weights["investment_analysis"] += 0.1
        weights["listing_recommendation"] += 0.05
        weights["property_valuation"] += 0.04
    if profile.role == "advisor":
        weights["compliance_validation"] += 0.1
        weights["listing_recommendation"] += 0.04
        weights["ux_personalization"] += 0.03

    if profile.residency_interest:
        weights["residency_eligibility"] += 0.08
        weights["listing_recommendation"] += 0.02
    if profile.financing_needed:
        weights["financial_risk"] += 0.06
    else:
        weights["listing_recommendation"] += 0.02
    if context.cross_border:
        weights["property_valuation"] += 0.02
        weights["listing_recommendation"] += 0.03
        weights["compliance_validation"] += 0.05
    if profile.risk_tolerance == "conservative":
        weights["insurance_matching"] += 0.04
        weights["compliance_validation"] += 0.04
    elif profile.risk_tolerance == "opportunistic":
        weights["investment_analysis"] += 0.04
        weights["property_valuation"] += 0.03
    else:
        weights["listing_recommendation"] += 0.02

    total = sum(weights.values())
    return {key: round(value / total, 4) for key, value in weights.items()}


def build_ranked_recommendations(
    profile: UserProfile,
    context: RequestContext,
    selected_experts: Sequence[ExpertDecision],
) -> List[RankedRecommendation]:
    catalog_key = profile.role if profile.role in RECOMMENDATION_CATALOG else "buyer"
    candidates = RECOMMENDATION_CATALOG[catalog_key]
    active_experts = {decision.expert: decision.score for decision in selected_experts}
    weights = build_ranking_weights(profile, context)
    recommendations: List[RankedRecommendation] = []

    for candidate in candidates:
        base_scores = candidate["base_scores"]
        expert_contributions: Dict[str, float] = {}
        composite = 0.0

        for expert_name, weight in weights.items():
            if expert_name not in active_experts:
                continue
            raw_score = float(base_scores.get(expert_name, 0.0))
            contribution = round(raw_score * weight, 4)
            expert_contributions[expert_name] = contribution
            composite += contribution

        budget_gap = profile.investment_budget - int(candidate["price"])
        if budget_gap >= 0:
            composite += 0.03
        elif abs(budget_gap) <= 150000:
            composite -= 0.02
        else:
            composite -= 0.06

        if profile.residency_interest:
            composite += float(base_scores.get("residency_eligibility", 0.0)) * 0.03
        if profile.financing_needed:
            composite += float(base_scores.get("financial_risk", 0.0)) * 0.03
        if context.climate_risk == "high":
            composite -= (1 - float(base_scores.get("insurance_matching", 0.0))) * 0.04

        top_factors = sorted(expert_contributions.items(), key=lambda item: item[1], reverse=True)[:3]
        why = (
            f"Ranked highly because {', '.join(name for name, _ in top_factors)} contributed most after "
            f"adapting weights for role={profile.role}, risk={profile.risk_tolerance}, "
            f"residency_interest={profile.residency_interest}, and financing_needed={profile.financing_needed}."
        )
        recommendations.append(
            RankedRecommendation(
                candidate_id=str(candidate["candidate_id"]),
                title=str(candidate["title"]),
                geography=str(candidate["geography"]),
                category=str(candidate["category"]),
                summary=str(candidate["summary"]),
                composite_score=round(composite, 3),
                confidence=round(min(composite + 0.08, 0.99), 2),
                expert_contributions=expert_contributions,
                valuation_band=str(candidate["valuation_band"]),
                comparable_summary=str(candidate["comparable_summary"]),
                trend_signal=str(candidate["trend_signal"]),
                location_intelligence=str(candidate["location_intelligence"]),
                recommendation_rationale=str(candidate["recommendation_rationale"]),
                why=why,
                investment_insight=str(candidate["investment_insight"]),
                visa_pathway=str(candidate["visa_pathway"]),
                insurance_option=str(candidate["insurance_option"]),
            )
        )

    return sorted(recommendations, key=lambda item: item.composite_score, reverse=True)


def build_governance_status(
    profile: UserProfile,
    identity: IdentityContext,
    context: RequestContext,
    policy_results: Sequence[PolicyGateResult],
) -> List[ModelGovernanceStatus]:
    review_required = any(result.status != "passed" for result in policy_results)
    iso_5259_status = "review" if review_required and context.market_volatility == "high" else "active"
    iso_42001_status = "review" if review_required and identity.aml_risk == "high" else "active"
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
                "The AI management layer records accountable owners, ranking/valuation risks, fairness checks, and "
                "manual review triggers for sensitive releases."
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
        f"applied ISO/IEC 5259 and ISO/IEC 42001 governance controls, and ended with release status '{packet.release_status}'. Review flags: {review_flags or ['none']}."
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


def demo() -> None:
    profile = UserProfile(
        role="investor",
        investor_type="cross_border",
        intent="cross-border property investment with residency options",
        financial_intent="income plus long-term appreciation",
        country="United States",
        target_region="Portugal",
        risk_tolerance="balanced",
        investment_budget=850000,
        residency_interest=True,
        residency_goal="golden visa pathway for family relocation",
        financing_needed=True,
        household_size=3,
    )
    identity = IdentityContext(
        subject_id=f"usr-{uuid.uuid4().hex[:8]}",
        auth_assurance_level="aal2",
        mfa_completed=True,
        rbac_roles=("client", "investor"),
        entitlements=("decision:view", "decision:export", "profile:update"),
        kyc_status="approved",
        aml_risk="medium",
        sanctions_status="clear",
        privacy_tier="confidential",
        consent_scope=("routing", "kyc", "personalization", "evidence_retention"),
        pii_tags=("identity", "financial", "residency"),
    )
    context = RequestContext(
        request_id=f"req-{uuid.uuid4().hex[:8]}",
        journey_stage="consideration",
        channel="web",
        locale="en-US",
        has_verified_identity=True,
        has_consent=True,
        property_country="Portugal",
        property_type="apartment",
        climate_risk="medium",
        market_volatility="medium",
        session_risk="medium",
        cross_border=True,
    )
    packet = orchestrate(
        user_prompt=(
            "I want to compare a Portugal property for yield, residency eligibility, insurance readiness, and mortgage affordability."
        ),
        profile=profile,
        identity=identity,
        context=context,
    )
    print(json.dumps(asdict(packet), indent=2))


if __name__ == "__main__":
    demo()

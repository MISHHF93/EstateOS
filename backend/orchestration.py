"""EstateOS Mixture-of-Experts orchestration reference implementation.

This module provides a dependency-light Python blueprint for how EstateOS can:
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
    intent: str
    country: str
    risk_tolerance: str
    investment_budget: int
    residency_interest: bool
    financing_needed: bool
    household_size: int


@dataclass(frozen=True)
class RequestContext:
    request_id: str
    journey_stage: str
    channel: str
    locale: str
    has_verified_identity: bool
    has_consent: bool
    sanctions_hit: bool
    property_country: str
    property_type: str
    climate_risk: str
    market_volatility: str
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
class AuditEvent:
    name: str
    status: str
    detail: str
    timestamp_utc: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


@dataclass(frozen=True)
class DecisionPacket:
    request_id: str
    profile: UserProfile
    context: RequestContext
    detected_intents: Sequence[str]
    selected_experts: Sequence[ExpertDecision]
    expert_outputs: Sequence[ExpertOutput]
    policy_gates: Sequence[PolicyGateResult]
    audit_trail: Sequence[AuditEvent]
    recommendation: str
    explanation: str
    release_status: str
    azure_services: Sequence[str]
    standards_alignment: Sequence[str]
    timestamp_utc: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


EXPERT_REGISTRY: Sequence[ExpertCard] = (
    ExpertCard(
        name="property_valuation",
        specialties=("valuation", "comparables", "market_position"),
        triggers=("property", "home", "price", "valuation", "market"),
        compliance_dependencies=("privacy", "model_risk"),
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
        name="residency_eligibility",
        specialties=("residency", "visa", "jurisdiction_rules"),
        triggers=("visa", "residency", "citizenship", "migration", "golden visa"),
        compliance_dependencies=("kyc", "sanctions", "jurisdiction"),
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
    "residency": "residency_eligibility",
    "insurance": "insurance_matching",
    "finance": "financial_risk",
    "compliance": "compliance_validation",
}

POLICY_GATES: Dict[str, str] = {
    "privacy": "Minimize personal data, enforce purpose limitation, and respect consent state before release.",
    "kyc": "Confirm identity evidence and beneficial ownership before high-trust actions are released.",
    "aml": "Check source-of-funds completeness and transaction anomaly indicators.",
    "sanctions": "Screen sanctioned individuals, entities, and high-risk geographies.",
    "jurisdiction": "Verify local property ownership, residency-by-investment, and disclosure rules.",
    "licensing": "Ensure insurance distribution and advisory actions fit the servicing entity permissions.",
    "model_risk": "Record model lineage, confidence, and evaluation thresholds for AI-assisted outputs.",
    "risk_thresholds": "Block release when fraud, climate, cyber, or financial risks exceed threshold.",
    "records": "Write immutable audit logs with inputs, outputs, lineage, and approvals.",
    "suitability": "Check affordability and product suitability against client profile and constraints.",
}

AZURE_SERVICES: Sequence[str] = (
    "Azure Front Door",
    "Azure API Management",
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
    "Microsoft Sentinel",
)

STANDARDS_ALIGNMENT: Sequence[str] = (
    "ISO/IEC 27001",
    "ISO/IEC 27017",
    "ISO/IEC 25010",
    "ISO 22301",
    "ISO 31000",
)


def detect_intents(user_prompt: str, profile: UserProfile) -> List[str]:
    prompt = f"{user_prompt.lower()} {profile.intent.lower()}"
    intents: List[str] = []
    for keyword, intent in INTENT_KEYWORDS.items():
        if keyword in prompt and intent not in intents:
            intents.append(intent)
    if profile.residency_interest and "residency" not in intents:
        intents.append("residency")
    if profile.financing_needed and "finance" not in intents:
        intents.append("finance")
    return intents or ["property_search", "valuation", "compliance"]


def score_expert(expert: ExpertCard, user_prompt: str, profile: UserProfile, context: RequestContext, detected_intents: Iterable[str]) -> float:
    prompt = user_prompt.lower()
    trigger_hits = sum(1 for trigger in expert.triggers if trigger in prompt)
    specialty_hits = sum(1 for specialty in expert.specialties if specialty in " ".join(detected_intents))
    mapped_intent_hits = sum(1 for intent in detected_intents if INTENT_EXPERT_MAP.get(intent) == expert.name)
    profile_bonus = 0.0
    if expert.name == "investment_analysis" and profile.role == "investor":
        profile_bonus += 0.14
    if expert.name == "residency_eligibility" and profile.residency_interest:
        profile_bonus += 0.20
    if expert.name == "financial_risk" and profile.financing_needed:
        profile_bonus += 0.18
    if expert.name == "insurance_matching" and context.climate_risk in {"medium", "high"}:
        profile_bonus += 0.14
    if expert.name == "property_valuation" and context.market_volatility in {"medium", "high"}:
        profile_bonus += 0.10
    if expert.name == "ux_personalization":
        profile_bonus += 0.10
    if expert.name == "compliance_validation":
        profile_bonus += 0.24
    raw_score = min(0.32 + trigger_hits * 0.11 + specialty_hits * 0.07 + mapped_intent_hits * 0.17 + profile_bonus, 0.99)
    return round(raw_score, 2)


def route_experts(user_prompt: str, profile: UserProfile, context: RequestContext, detected_intents: Sequence[str]) -> List[ExpertDecision]:
    selections: List[ExpertDecision] = []
    for expert in EXPERT_REGISTRY:
        score = score_expert(expert, user_prompt, profile, context, detected_intents)
        if score >= expert.min_confidence:
            rationale = (
                f"Selected for role={profile.role}, journey={context.journey_stage}, intents={list(detected_intents)}, "
                f"and contextual triggers with score {score:.2f}."
            )
            selections.append(
                ExpertDecision(
                    expert=expert.name,
                    score=score,
                    rationale=rationale,
                    execution_mode=expert.execution_mode,
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
    if "records" not in dependencies:
        dependencies.append("records")
    return dependencies


def evaluate_policy_gates(policy_dependencies: Sequence[str], profile: UserProfile, context: RequestContext) -> List[PolicyGateResult]:
    results: List[PolicyGateResult] = []
    for dependency in policy_dependencies:
        status = "passed"
        if dependency == "privacy" and not context.has_consent:
            status = "blocked"
        elif dependency == "kyc" and not context.has_verified_identity:
            status = "blocked"
        elif dependency == "sanctions" and context.sanctions_hit:
            status = "blocked"
        elif dependency == "risk_thresholds" and context.climate_risk == "high" and profile.risk_tolerance == "conservative":
            status = "review"
        results.append(
            PolicyGateResult(
                name=dependency,
                status=status,
                details=POLICY_GATES[dependency],
            )
        )
    return results


def build_expert_outputs(profile: UserProfile, context: RequestContext, selected_experts: Sequence[ExpertDecision]) -> List[ExpertOutput]:
    outputs: List[ExpertOutput] = []
    for decision in selected_experts:
        if decision.expert == "property_valuation":
            outputs.append(
                ExpertOutput(
                    expert=decision.expert,
                    summary=(
                        f"Estimated fair-value band prepared for the {context.property_type} in {context.property_country} "
                        f"with volatility awareness for a {profile.role}."
                    ),
                    confidence=round(max(decision.score - 0.03, 0.5), 2),
                    evidence=("listing metadata", "market comparables", "local market momentum"),
                    next_actions=("Review comparable sales", "Inspect pricing assumptions"),
                )
            )
        elif decision.expert == "investment_analysis":
            outputs.append(
                ExpertOutput(
                    expert=decision.expert,
                    summary="Scenario analysis ranked return pathways using yield, downside resilience, and liquidity constraints.",
                    confidence=round(max(decision.score - 0.02, 0.5), 2),
                    evidence=("rent comps", "rate assumptions", "cash-flow scenarios"),
                    next_actions=("Compare target hold periods", "Review downside scenario"),
                )
            )
        elif decision.expert == "residency_eligibility":
            outputs.append(
                ExpertOutput(
                    expert=decision.expert,
                    summary=f"Residency pathways were screened for {profile.country} applicants targeting {context.property_country} assets.",
                    confidence=round(max(decision.score - 0.04, 0.5), 2),
                    evidence=("jurisdiction rules", "budget thresholds", "family composition"),
                    next_actions=("Confirm qualifying pathway", "Collect legal evidence"),
                )
            )
        elif decision.expert == "insurance_matching":
            outputs.append(
                ExpertOutput(
                    expert=decision.expert,
                    summary="Insurance matching evaluated peril exposure, coverage fit, and quote readiness.",
                    confidence=round(max(decision.score - 0.04, 0.5), 2),
                    evidence=("property exposure data", "hazard model", "carrier appetite rules"),
                    next_actions=("Review exclusions", "Prepare ACORD intake"),
                )
            )
        elif decision.expert == "financial_risk":
            outputs.append(
                ExpertOutput(
                    expert=decision.expert,
                    summary="Financial risk analysis measured affordability, leverage, liquidity, and financing resilience.",
                    confidence=round(max(decision.score - 0.03, 0.5), 2),
                    evidence=("income profile", "liability snapshot", "rate stress tests"),
                    next_actions=("Validate financing plan", "Review affordability buffer"),
                )
            )
        elif decision.expert == "compliance_validation":
            outputs.append(
                ExpertOutput(
                    expert=decision.expert,
                    summary="Compliance release checks validated identity, sanctions posture, privacy, suitability, and recordkeeping obligations.",
                    confidence=round(max(decision.score - 0.01, 0.5), 2),
                    evidence=("identity evidence", "policy registry", "screening logs"),
                    next_actions=("Resolve blocked gates", "Attach missing evidence if required"),
                )
            )
        elif decision.expert == "ux_personalization":
            outputs.append(
                ExpertOutput(
                    expert=decision.expert,
                    summary="Frontend response was tailored into confidence-aware language, explanations, and next-best actions.",
                    confidence=round(max(decision.score - 0.05, 0.5), 2),
                    evidence=("persona rules", "journey stage", "decision confidence"),
                    next_actions=("Show explanation drawer", "Highlight next required action"),
                )
            )
    return outputs


def build_audit_trail(context: RequestContext, selected_experts: Sequence[ExpertDecision], policy_results: Sequence[PolicyGateResult], release_status: str) -> List[AuditEvent]:
    selected_names = ", ".join(f"{item.expert}:{item.execution_mode}" for item in selected_experts)
    blocked_or_review = [result.name for result in policy_results if result.status != "passed"]
    return [
        AuditEvent(name="journey.requested", status="completed", detail=f"Request received for {context.channel} channel."),
        AuditEvent(name="context.assembled", status="completed", detail=f"Journey stage={context.journey_stage}, locale={context.locale}."),
        AuditEvent(name="experts.selected", status="completed", detail=f"Selected experts {selected_names}."),
        AuditEvent(name="policy.validation.completed", status=release_status, detail=f"Non-passing gates: {blocked_or_review or ['none']}."),
        AuditEvent(name="audit.packet.persisted", status="completed", detail="Decision packet persisted to evidence store and event stream."),
    ]


def build_recommendation(profile: UserProfile, context: RequestContext, selected_experts: Sequence[ExpertDecision], release_status: str) -> str:
    expert_names = ", ".join(decision.expert for decision in selected_experts[:6])
    if release_status == "blocked":
        return (
            "Hold automated release, surface remediation tasks in the advisor console, and only continue after the blocked policy "
            f"checks are resolved across {expert_names}."
        )
    if profile.role == "investor":
        return (
            "Deliver a cross-border investment brief that ranks assets by value, risk-adjusted return, residency alignment, "
            f"insurability, and financing readiness using signals from {expert_names}."
        )
    if profile.role == "advisor":
        return (
            "Provide an approval-ready memo with expert-by-expert rationale, policy outcomes, assumptions, and human override "
            f"options grounded in {expert_names}."
        )
    return (
        "Present a guided property decision journey that combines fair value, affordability, eligibility, insurance, and next "
        f"steps using {expert_names}."
    )


def explain_packet(packet: DecisionPacket) -> str:
    highest = packet.selected_experts[0] if packet.selected_experts else None
    top_expert_text = (
        f"Top-ranked expert was {highest.expert} at {highest.score:.2f}." if highest else "No experts selected."
    )
    review_flags = [result.name for result in packet.policy_gates if result.status != "passed"]
    return (
        f"EstateOS detected intents {list(packet.detected_intents)} for role '{packet.profile.role}' in the "
        f"{packet.context.channel} channel. {top_expert_text} The routing layer combined synchronous and asynchronous experts, "
        f"evaluated {len(packet.policy_gates)} policy gates, and ended with release status '{packet.release_status}'. "
        f"Review flags: {review_flags or ['none']}."
    )


def orchestrate(user_prompt: str, profile: UserProfile, context: RequestContext) -> DecisionPacket:
    intents = detect_intents(user_prompt, profile)
    experts = route_experts(user_prompt, profile, context, intents)
    policy_dependencies = collect_policy_dependencies(experts)
    policy_results = evaluate_policy_gates(policy_dependencies, profile, context)

    if any(result.status == "blocked" for result in policy_results):
        release_status = "blocked"
    elif any(result.status == "review" for result in policy_results):
        release_status = "human_review"
    else:
        release_status = "released"

    expert_outputs = build_expert_outputs(profile, context, experts)
    audit_trail = build_audit_trail(context, experts, policy_results, release_status)
    recommendation = build_recommendation(profile, context, experts, release_status)

    packet = DecisionPacket(
        request_id=context.request_id,
        profile=profile,
        context=context,
        detected_intents=intents,
        selected_experts=experts,
        expert_outputs=expert_outputs,
        policy_gates=policy_results,
        audit_trail=audit_trail,
        recommendation=recommendation,
        explanation="",
        release_status=release_status,
        azure_services=AZURE_SERVICES,
        standards_alignment=STANDARDS_ALIGNMENT,
    )
    return DecisionPacket(**{**asdict(packet), "explanation": explain_packet(packet)})


def demo() -> None:
    profile = UserProfile(
        role="investor",
        intent="cross-border property investment with residency options",
        country="United States",
        risk_tolerance="balanced",
        investment_budget=850000,
        residency_interest=True,
        financing_needed=True,
        household_size=3,
    )
    context = RequestContext(
        request_id=f"req-{uuid.uuid4().hex[:8]}",
        journey_stage="consideration",
        channel="web",
        locale="en-US",
        has_verified_identity=True,
        has_consent=True,
        sanctions_hit=False,
        property_country="Portugal",
        property_type="apartment",
        climate_risk="medium",
        market_volatility="medium",
    )
    packet = orchestrate(
        user_prompt=(
            "I want to compare a Portugal property for yield, residency eligibility, insurance readiness, and mortgage affordability."
        ),
        profile=profile,
        context=context,
    )
    print(json.dumps(asdict(packet), indent=2))


if __name__ == "__main__":
    demo()

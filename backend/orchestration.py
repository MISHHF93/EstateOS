"""EstateOS Mixture-of-Experts orchestration reference implementation.

This module provides a small, dependency-light Python blueprint for how EstateOS can:
- detect user intents,
- route work to specialized experts,
- enforce policy gates,
- build an auditable explanation package.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Dict, Iterable, List, Sequence
import json


@dataclass(frozen=True)
class ExpertCard:
    name: str
    specialties: Sequence[str]
    triggers: Sequence[str]
    compliance_dependencies: Sequence[str]
    min_confidence: float


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


@dataclass(frozen=True)
class DecisionPacket:
    request_id: str
    role: str
    detected_intents: Sequence[str]
    selected_experts: Sequence[ExpertDecision]
    policy_gates: Sequence[PolicyGateResult]
    recommendation: str
    explanation: str
    released: bool
    timestamp_utc: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


EXPERT_REGISTRY: Sequence[ExpertCard] = (
    ExpertCard(
        name="property_discovery",
        specialties=("search", "lifestyle_match", "market_supply"),
        triggers=("buy", "property", "home", "location", "amenities", "portfolio"),
        compliance_dependencies=("privacy", "kyc"),
        min_confidence=0.50,
    ),
    ExpertCard(
        name="pricing_intelligence",
        specialties=("valuation", "yield", "market_momentum"),
        triggers=("price", "valuation", "yield", "returns", "market"),
        compliance_dependencies=("model_risk",),
        min_confidence=0.60,
    ),
    ExpertCard(
        name="rbi_eligibility",
        specialties=("residency", "migration", "jurisdiction_rules"),
        triggers=("visa", "residency", "citizenship", "migration", "golden visa"),
        compliance_dependencies=("kyc", "sanctions", "jurisdiction"),
        min_confidence=0.60,
    ),
    ExpertCard(
        name="insurance_recommendation",
        specialties=("coverage", "perils", "acord_intake"),
        triggers=("insurance", "coverage", "hazard", "storm", "claim"),
        compliance_dependencies=("privacy", "licensing"),
        min_confidence=0.55,
    ),
    ExpertCard(
        name="risk_assessment",
        specialties=("fraud", "climate", "operational", "cyber"),
        triggers=("risk", "fraud", "climate", "exposure", "sanctions"),
        compliance_dependencies=("sanctions", "risk_thresholds"),
        min_confidence=0.65,
    ),
    ExpertCard(
        name="compliance_validation",
        specialties=("kyc", "aml", "sanctions", "privacy", "records"),
        triggers=("compliance", "kyc", "aml", "privacy", "sanctions", "regulated"),
        compliance_dependencies=("all",),
        min_confidence=0.80,
    ),
    ExpertCard(
        name="financial_decision_support",
        specialties=("affordability", "leverage", "liquidity", "scenario_analysis"),
        triggers=("loan", "mortgage", "affordability", "cashflow", "finance"),
        compliance_dependencies=("suitability", "privacy"),
        min_confidence=0.60,
    ),
)


INTENT_KEYWORDS: Dict[str, str] = {
    "property": "property_search",
    "home": "property_search",
    "buy": "property_search",
    "market": "pricing",
    "price": "pricing",
    "yield": "pricing",
    "residency": "rbi",
    "visa": "rbi",
    "citizenship": "rbi",
    "insurance": "insurance",
    "coverage": "insurance",
    "risk": "risk",
    "fraud": "risk",
    "kyc": "compliance",
    "aml": "compliance",
    "sanctions": "compliance",
    "loan": "finance",
    "mortgage": "finance",
    "cashflow": "finance",
    "affordability": "finance",
}

INTENT_EXPERT_MAP: Dict[str, str] = {
    "property_search": "property_discovery",
    "pricing": "pricing_intelligence",
    "rbi": "rbi_eligibility",
    "insurance": "insurance_recommendation",
    "risk": "risk_assessment",
    "compliance": "compliance_validation",
    "finance": "financial_decision_support",
}


POLICY_GATES: Dict[str, str] = {
    "privacy": "Minimize personal data, enforce purpose limitation, and check residency of data storage.",
    "kyc": "Confirm identity evidence and beneficial ownership before high-trust actions are released.",
    "aml": "Check source-of-funds completeness and transaction anomaly indicators.",
    "sanctions": "Screen sanctioned individuals, entities, and high-risk geographies.",
    "jurisdiction": "Verify local residency-by-investment, property ownership, and disclosure rules.",
    "licensing": "Ensure insurance distribution and advisory actions fit the servicing entity's permissions.",
    "model_risk": "Record model lineage, confidence, and evaluation thresholds for pricing outputs.",
    "risk_thresholds": "Block release when fraud, climate, cyber, or operational risks exceed threshold.",
    "records": "Write an immutable audit log with inputs, outputs, and human approvals.",
    "suitability": "Check affordability and product suitability against client profile and constraints.",
}


def detect_intents(user_prompt: str) -> List[str]:
    prompt = user_prompt.lower()
    intents: List[str] = []
    for keyword, intent in INTENT_KEYWORDS.items():
        if keyword in prompt and intent not in intents:
            intents.append(intent)
    return intents or ["property_search", "pricing", "compliance"]


def score_expert(expert: ExpertCard, user_prompt: str, detected_intents: Iterable[str]) -> float:
    prompt = user_prompt.lower()
    trigger_hits = sum(1 for trigger in expert.triggers if trigger in prompt)
    specialty_hits = sum(1 for specialty in expert.specialties if specialty in " ".join(detected_intents))
    mapped_intent_hits = sum(1 for intent in detected_intents if INTENT_EXPERT_MAP.get(intent) == expert.name)
    intent_bonus = 0.15 if expert.name.startswith("compliance") and "compliance" in detected_intents else 0.0
    raw_score = min(0.35 + trigger_hits * 0.11 + specialty_hits * 0.08 + mapped_intent_hits * 0.18 + intent_bonus, 0.99)
    return round(raw_score, 2)


def route_experts(user_prompt: str, detected_intents: Sequence[str]) -> List[ExpertDecision]:
    selections: List[ExpertDecision] = []
    for expert in EXPERT_REGISTRY:
        score = score_expert(expert, user_prompt, detected_intents)
        if score >= expert.min_confidence:
            rationale = (
                f"Selected because prompt matched triggers {list(expert.triggers)} and specialties {list(expert.specialties)} "
                f"with score {score:.2f}."
            )
            selections.append(ExpertDecision(expert=expert.name, score=score, rationale=rationale))
    if not any(choice.expert == "compliance_validation" for choice in selections):
        selections.append(
            ExpertDecision(
                expert="compliance_validation",
                score=0.92,
                rationale="Added as mandatory release gate for regulated real-estate, finance, insurance, and migration workflows.",
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


def evaluate_policy_gates(policy_dependencies: Sequence[str], user_prompt: str) -> List[PolicyGateResult]:
    prompt = user_prompt.lower()
    results: List[PolicyGateResult] = []
    for dependency in policy_dependencies:
        blocked = dependency == "sanctions" and "blocked party" in prompt
        results.append(
            PolicyGateResult(
                name=dependency,
                status="blocked" if blocked else "passed",
                details=POLICY_GATES[dependency],
            )
        )
    return results


def build_recommendation(role: str, intents: Sequence[str], selected_experts: Sequence[ExpertDecision]) -> str:
    expert_names = ", ".join(decision.expert for decision in selected_experts[:4])
    if role == "investor":
        return (
            "Deliver a cross-border investment brief that ranks assets by yield, risk-adjusted return, residency alignment, "
            f"and insurability, using signals from {expert_names}."
        )
    if role == "advisor":
        return (
            "Provide an approval-ready memo with expert-by-expert rationale, policy outcomes, assumptions, and human override options, "
            f"grounded in {expert_names}."
        )
    return (
        "Present a guided property decision journey that combines shortlist, affordability, eligibility, risk, and insurance next steps, "
        f"using {expert_names}."
    )


def explain_packet(packet: DecisionPacket) -> str:
    highest = packet.selected_experts[0] if packet.selected_experts else None
    top_expert_text = (
        f"Top-ranked expert was {highest.expert} at {highest.score:.2f}." if highest else "No experts selected."
    )
    return (
        f"EstateOS detected intents {list(packet.detected_intents)} for role '{packet.role}'. {top_expert_text} "
        f"{len(packet.policy_gates)} policy gates were evaluated before release, and release status was {packet.released}."
    )


def orchestrate(request_id: str, role: str, user_prompt: str) -> DecisionPacket:
    intents = detect_intents(user_prompt)
    experts = route_experts(user_prompt, intents)
    dependencies = collect_policy_dependencies(experts)
    policy_results = evaluate_policy_gates(dependencies, user_prompt)
    released = all(result.status == "passed" for result in policy_results)
    recommendation = build_recommendation(role, intents, experts)

    packet = DecisionPacket(
        request_id=request_id,
        role=role,
        detected_intents=intents,
        selected_experts=experts,
        policy_gates=policy_results,
        recommendation=recommendation,
        explanation="",
        released=released,
    )
    return DecisionPacket(
        **{**asdict(packet), "explanation": explain_packet(packet)}
    )


def demo() -> None:
    packet = orchestrate(
        request_id="req-1001",
        role="investor",
        user_prompt=(
            "I want to buy a property with strong yield potential, residency options, insurance coverage, "
            "and mortgage affordability in Portugal."
        ),
    )
    print(json.dumps(asdict(packet), indent=2))


if __name__ == "__main__":
    demo()

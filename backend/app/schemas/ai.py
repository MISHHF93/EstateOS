from pydantic import Field

from app.schemas.common import APIModel


class AIContext(APIModel):
    user_id: str
    listing_id: str | None = None
    transaction_id: str | None = None
    jurisdiction: str | None = None
    transaction_stage: str | None = None


class AITrustContext(APIModel):
    kyc_status: str = 'pending'
    aml_risk: str = 'low'
    sanctions_status: str = 'clear'
    privacy_tier: str = 'standard'
    consent_scope: list[str] = Field(default_factory=list)
    human_review_required: bool = False


class AIAssessRequest(APIModel):
    intent: str
    context: AIContext
    input_payload: dict
    trust_context: AITrustContext | None = None


class ExpertAssessment(APIModel):
    expert_key: str
    score: float
    summary: str
    rationale: list[str]
    confidence: float


class RankedRecommendation(APIModel):
    candidate_id: str
    title: str
    composite_score: float
    reasons: list[str]


class DecisionGovernance(APIModel):
    release_status: str
    review_queue: str
    policy_gates: list[str]
    audit_events: list[str]


class AIResults(APIModel):
    property_fit_score: float
    valuation_band: str
    estimated_yield: float
    residency_result: str
    compliance_risk: str
    insurance_relevance: list[str]
    fraud_status: str
    document_completeness: float
    personalization_profile: str
    market_outlook: str
    expert_assessments: list[ExpertAssessment]
    ranked_recommendations: list[RankedRecommendation]


class AIAssessResponse(APIModel):
    request_id: str
    selected_experts: list[str]
    results: AIResults
    explanations: list[str]
    governance: DecisionGovernance

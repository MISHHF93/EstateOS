from app.schemas.common import APIModel


class AIContext(APIModel):
    user_id: str
    listing_id: str


class AIAssessRequest(APIModel):
    intent: str
    context: AIContext
    input_payload: dict


class AIResults(APIModel):
    property_fit_score: float
    estimated_yield: float
    residency_result: str
    compliance_risk: str
    insurance_relevance: list[str]


class AIAssessResponse(APIModel):
    request_id: str
    selected_experts: list[str]
    results: AIResults
    explanations: list[str]

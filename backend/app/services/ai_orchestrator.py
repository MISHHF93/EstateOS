from uuid import uuid4

from app.experts.compliance_expert import ComplianceExpert
from app.experts.insurance_expert import InsuranceExpert
from app.experts.property_recommender import PropertyRecommenderExpert
from app.experts.residency_expert import ResidencyExpert
from app.experts.roi_expert import ROIExpert
from app.schemas.ai import AIAssessRequest, AIAssessResponse, AIResults
from app.services.base import AuditedService


class AIOrchestratorService(AuditedService):
    def __init__(self) -> None:
        self.property_recommender = PropertyRecommenderExpert()
        self.roi_expert = ROIExpert()
        self.residency_expert = ResidencyExpert()
        self.compliance_expert = ComplianceExpert()
        self.insurance_expert = InsuranceExpert()

    def assess(self, payload: AIAssessRequest) -> AIAssessResponse:
        request_id = f'ai-{uuid4()}'
        selected_experts = self._route(payload.intent)
        self.audit('ai_request', request_id, 'routed', {'experts': selected_experts})
        results = AIResults(
            property_fit_score=self.property_recommender.score(payload),
            estimated_yield=self.roi_expert.estimate_yield(payload),
            residency_result=self.residency_expert.assess(payload),
            compliance_risk=self.compliance_expert.risk(payload),
            insurance_relevance=self.insurance_expert.recommend(payload),
        )
        return AIAssessResponse(
            request_id=request_id,
            selected_experts=selected_experts,
            results=results,
            explanations=[
                'This listing aligns with the stated investment budget.',
                'Jurisdiction preference matches the selected residency workflow.',
            ],
        )

    def _route(self, intent: str) -> list[str]:
        if intent == 'investment_property_with_residency':
            return [
                'property_recommender',
                'roi_expert',
                'residency_expert',
                'compliance_expert',
                'insurance_expert',
            ]
        return ['property_recommender', 'compliance_expert']

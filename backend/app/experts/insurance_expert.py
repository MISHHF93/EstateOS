from app.schemas.ai import AIAssessRequest


class InsuranceExpert:
    def recommend(self, payload: AIAssessRequest) -> list[str]:
        if payload.intent == 'investment_property_with_residency':
            return ['homeowners', 'title']
        return ['homeowners']

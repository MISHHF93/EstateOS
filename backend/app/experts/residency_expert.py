from app.schemas.ai import AIAssessRequest


class ResidencyExpert:
    def assess(self, payload: AIAssessRequest) -> str:
        return 'preliminarily_eligible' if payload.input_payload.get('country_preference') == 'UAE' else 'requires_review'

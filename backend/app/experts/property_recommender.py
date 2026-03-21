from app.schemas.ai import AIAssessRequest


class PropertyRecommenderExpert:
    def score(self, payload: AIAssessRequest) -> float:
        budget = float(payload.input_payload.get('budget', 0) or 0)
        return 0.88 if budget >= 800000 else 0.72

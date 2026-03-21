from app.schemas.ai import AIAssessRequest


class ROIExpert:
    def estimate_yield(self, payload: AIAssessRequest) -> float:
        risk = payload.input_payload.get('risk_tolerance', 'medium')
        return 0.074 if risk == 'medium' else 0.061

from app.schemas.ai import AIAssessRequest


class ComplianceExpert:
    def risk(self, payload: AIAssessRequest) -> str:
        return 'low' if payload.input_payload.get('risk_tolerance') != 'high' else 'medium'

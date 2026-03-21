from app.schemas.ai import AIAssessRequest


class PersonalizationExpert:
    def segment(self, payload: AIAssessRequest) -> str:
        objective = payload.input_payload.get('objective', 'discover')
        if payload.intent == 'investment_property_with_residency':
            return 'cross_border_investor'
        if objective in {'family_move', 'relocate'}:
            return 'relocation_household'
        return 'discovery_user'

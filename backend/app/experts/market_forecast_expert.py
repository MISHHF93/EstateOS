from app.schemas.ai import AIAssessRequest


class MarketForecastExpert:
    def outlook(self, payload: AIAssessRequest) -> str:
        jurisdiction = (payload.context.jurisdiction or payload.input_payload.get('country_preference') or '').upper()
        if jurisdiction in {'UAE', 'PORTUGAL', 'GREECE'}:
            return 'favorable_with_policy_monitoring'
        return 'stable_pending_local_signals'

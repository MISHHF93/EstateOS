class FraudExpert:
    def risk_flag(self, transaction_stage: str) -> str:
        return 'review' if transaction_stage in {'under_review', 'due_diligence'} else 'clear'

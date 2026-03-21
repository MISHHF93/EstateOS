class ValuationExpert:
    def estimate_band(self, price: float) -> str:
        lower = int(price * 0.95)
        upper = int(price * 1.05)
        return f'${lower:,}-${upper:,}'

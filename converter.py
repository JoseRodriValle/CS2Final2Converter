from api import get_exchange_rate


class CurrencyConverter:
    """Handles the currency conversion"""

    def convert(self, amount: float, source: str, target: str) -> float:
        """Convert the given amount"""
        rate = get_exchange_rate(source, target)
        return amount * rate

# domain.py
"""Business logic for pay station

"""


class IllegalCoinException(Exception):
    """Exception for bad coins"""


# Rate Strategies
def linear_rate(amount):
    return amount // 5 * 2


class PayStation:
    """Implements the 'business logic' for parking pay station"""

    LEGAL_COINS = [5, 10, 25]

    def __init__(self, rate_function):
        self._calc_time = rate_function
        self._reset()

    def _reset(self):
        self._amount_inserted = 0

    def add_payment(self, coinvalue):
        """Adds coinvalue to paystation

        """
        if coinvalue not in self.LEGAL_COINS:
            raise IllegalCoinException(f"Invalid coin {coinvalue}")
        self._amount_inserted += coinvalue

    @property
    def minutes(self):
        """Give the number of minutes to display

        """
        return self._calc_time(self._amount_inserted)

    def buy(self):
        """Purchases parking time"""

        receipt = Receipt(self.minutes)
        self._reset()
        return receipt

    def cancel(self):
        """Cancels a purchase"""

        self._reset()


class Receipt:
    """Record of a pay station transaction"""

    def __init__(self, minutes):
        self._minutes = minutes

    @property
    def value(self):
        return self._minutes



# domain.py
"""Business logic for pay station

"""

from datetime import datetime

class IllegalCoinException(Exception):
    """Exception for bad coins"""


# Rate Strategies

class BasicRate:

    def __init__(self, hourly_rates):
        self._hourly_rates = hourly_rates

    def __call__(self, cents):
        minutes = 0
        for rate in self._hourly_rates:
            if cents >= rate:
                minutes = minutes + 60
                cents = cents - rate
            else:
                break
        return minutes + round(cents/rate * 60)

    
# These two rates define for backwards compatibility
linear_rate = BasicRate([150])
progressive_rate = BasicRate([150, 200, 300])


class AlternatingRate:

    """Rate strategy that allows different rates for Weekdays vs. Weekends

    """
    def __init__(self, weekday_rate, weekend_rate, datefunc=datetime.now):
        """weekday_rate and weekend_rate are function_like objects having
        signature: fn: cents --> minutes purchased

        datefunc has signature: <empty> --> datetime

        """
        self._weekday_rate = weekday_rate
        self._weekend_rate = weekend_rate
        self._datefn = datefunc

    def __call__(self, cents):
        """return number of minutes purchase by cents

        """
        date = self._datefn()
        if date.weekday() <= 4:
            return self._weekday_rate(cents)
        else:
            return self._weekend_rate(cents)

class PayStation:
    """Implements the 'business logic' for parking pay station"""

    LEGAL_COINS = [5, 10, 25]

    def __init__(self, factory):
        self._calc_time = factory.create_rate_strategy()
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

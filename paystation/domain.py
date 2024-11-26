# domain.py
"""Business logic for pay station

"""

import random
from datetime import datetime


class IllegalCoinException(Exception):
    """Exception for bad coins"""


# Rate Strategies

class BasicRate:
    """Rate strategy based on a sequence of hourly rates"""

    def __init__(self, hourly_rates):
        """hourly_rates is a list of rate (in cents) for successive hours

        e.g. [150, 200, 300] indicates cost for the first, second, and
             third hours. Subsequent hours are charged at the last
             rate.

        """
        self._hourly_rates = hourly_rates

    def __call__(self, cents):
        """Return minutes purchased

        """
        minutes = 0
        for rate in self._hourly_rates:
            if cents >= rate:  # purchase full hour
                minutes = minutes + 60
                cents = cents - rate
            else:
                break
        # add minutes for any remaining cents at the last rate
        minutes = minutes + round(cents/rate * 60)
        return minutes


# These two rates are defined for backwards compatibility
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
        self.config_id = factory.config_id
        self._factory = factory
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

        receipt = self._factory.create_receipt(self.minutes)
        self._reset()
        return receipt

    def cancel(self):
        """Cancels a purchase"""

        self._reset()


class Receipt:
    """Record of a pay station transaction"""

    template = \
"""--------------------------------------------------
-------  P A R K I N G   R E C E I P T     -------
                Value {:03d} minutes.
              Car parked at {:02d}:{:02d}
--------------------------------------------------"""

    def __init__(self, minutes, barcode=False):
        self._minutes = minutes
        self.with_barcode = barcode

    @property
    def value(self):
        return self._minutes

    def print(self, stream):
        now = datetime.now()
        output = self.template.format(self.value, now.hour, now.minute)
        print(output, file=stream)
        if self.with_barcode:
            barcode = "".join([random.choice(" ||") for _ in range(50)])
            print(barcode, file=stream)

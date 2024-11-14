# config.py

from paystation.domain import (linear_rate,
                               progressive_rate,
                               AlternatingRate,
                               Receipt
                               )


class AlphaTownFactory:

    def create_rate_strategy(self):
        return linear_rate

    def create_receipt(self, amount):
        return Receipt(amount)

    
class BetaTownFactory:

    def create_rate_strategy(self):
        return progressive_rate

    def create_receipt(self, amount):
        return Receipt(amount)


class GammaTownFactory:

    def create_rate_strategy(self):
        return AlternatingRate(linear_rate, progressive_rate)

    def create_receipt(self, amount):
        return Receipt(amount)


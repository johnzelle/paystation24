# config.py

from paystation.domain import (linear_rate,
                               progressive_rate,
                               BasicRate,
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


class TripoliFactory:

    def create_rate_strategy(self):
        return BasicRate([200])

    def create_receipt(self, amount):
        return Receipt(amount)


class HortonFactory:

    def create_rate_strategy(self):
        return BasicRate([75, 150, 200])

    def create_receipt(self, amount):
        return Receipt(amount)

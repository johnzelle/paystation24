# config.py

from paystation.domain import (linear_rate,
                               progressive_rate,
                               BasicRate,
                               AlternatingRate,
                               Receipt
                               )


class AlphaTownFactory:

    config_id = "alphatown"

    def create_rate_strategy(self):
        return linear_rate

    def create_receipt(self, amount):
        return Receipt(amount)


class BetaTownFactory:

    config_id = "betatown"

    def create_rate_strategy(self):
        return progressive_rate

    def create_receipt(self, amount):
        return Receipt(amount, barcode=True)


class GammaTownFactory:

    config_id = "gammatown"

    def create_rate_strategy(self):
        return AlternatingRate(linear_rate, progressive_rate)

    def create_receipt(self, amount):
        return Receipt(amount)


class TripoliFactory:

    config_id = "tripoli"

    def create_rate_strategy(self):
        return BasicRate([200])

    def create_receipt(self, amount):
        return Receipt(amount)


class HortonFactory:

    config_id = "horton"

    def create_rate_strategy(self):
        return BasicRate([75, 150, 200])

    def create_receipt(self, amount):
        return Receipt(amount)

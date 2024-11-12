# test_integration.py

import unittest
from paystation.domain import (PayStation,
                               linear_rate,
                               progressive_rate,
                               AlternatingRate
                               )


class TestALphaTownIntegration(unittest.TestCase):

    def test_paystation_works_with_linear_rate(self):
        ps = PayStation(linear_rate)
        ps.add_payment(25)
        receipt = ps.buy()
        self.assertEqual(linear_rate(25), receipt.value)


class TestBetaTownIntegration(unittest.TestCase):

    def test_paystation_works_with_progressive_rate(self):
        ps = PayStation(progressive_rate)
        ps.add_payment(25)
        receipt = ps.buy()
        self.assertEqual(linear_rate(25), receipt.value)


class TestGammaTownIntegration(unittest.TestCase):

    def test_paystation_works_with_alternating_rate(self):
        ps = PayStation(AlternatingRate(linear_rate, progressive_rate))
        ps.add_payment(25)
        receipt = ps.buy()
        self.assertIn(receipt.value, [linear_rate(25), progressive_rate(25)])

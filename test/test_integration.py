# test_integration.py

import unittest
from paystation.domain import PayStation, linear_rate


class TestALphaTownIntegration(unittest.TestCase):

    def test_paystation_works_with_linear_rate(self):
        ps = PayStation(linear_rate)
        ps.add_payment(25)
        receipt = ps.buy()
        self.assertEqual(linear_rate(25), receipt.value) 

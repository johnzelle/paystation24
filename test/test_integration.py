# test_integration.py

import unittest
from paystation.domain import (PayStation,
                               linear_rate,
                               progressive_rate,
                               BasicRate
                               )
from paystation.config import (AlphaTownFactory,
                               BetaTownFactory,
                               GammaTownFactory,
                               TripoliFactory,
                               HortonFactory
                               )


class TestALphaTownIntegration(unittest.TestCase):

    def test_paystation_works_with_alphatown_factory(self):
        ps = PayStation(AlphaTownFactory())
        ps.add_payment(25)
        receipt = ps.buy()
        self.assertEqual(linear_rate(25), receipt.value)


class TestBetaTownIntegration(unittest.TestCase):

    def test_paystation_works_with_progressive_rate(self):
        ps = PayStation(BetaTownFactory())
        ps.add_payment(25)
        receipt = ps.buy()
        self.assertEqual(linear_rate(25), receipt.value)


class TestGammaTownIntegration(unittest.TestCase):

    def test_paystation_works_with_alternating_rate(self):
        ps = PayStation(GammaTownFactory())
        ps.add_payment(25)
        receipt = ps.buy()
        self.assertIn(receipt.value, [linear_rate(25), progressive_rate(25)])


class TestTripoliIntegration(unittest.TestCase):

    def test_paystation_works_with_tripoli_factory(self):
        ps = PayStation(TripoliFactory())
        ps.add_payment(25)
        receipt = ps.buy()
        rs = BasicRate([200])
        self.assertEqual(rs(25), receipt.value)


class TestHortonIntegration(unittest.TestCase):

    def test_paystation_works_with_horton_factory(self):
        ps = PayStation(HortonFactory())
        ps.add_payment(25)
        receipt = ps.buy()
        rs = BasicRate([75, 150, 200])
        self.assertEqual(rs(25), receipt.value)

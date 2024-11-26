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
        self.assertEqual(ps.config_id, "alphatown")
        ps.add_payment(25)
        receipt = ps.buy()
        self.assertEqual(linear_rate(25), receipt.value)
        self.assertFalse(receipt.with_barcode)


class TestBetaTownIntegration(unittest.TestCase):

    def test_paystation_works_with_betatown_factory(self):
        ps = PayStation(BetaTownFactory())
        self.assertEqual(ps.config_id, "betatown")
        ps.add_payment(25)
        receipt = ps.buy()
        self.assertEqual(progressive_rate(25), receipt.value)
        self.assertTrue(receipt.with_barcode)


class TestGammaTownIntegration(unittest.TestCase):

    def test_paystation_works_with_gammatown_factory(self):
        ps = PayStation(GammaTownFactory())
        self.assertEqual(ps.config_id, "gammatown")
        ps.add_payment(25)
        receipt = ps.buy()
        self.assertIn(receipt.value, [linear_rate(25), progressive_rate(25)])
        self.assertFalse(receipt.with_barcode)


class TestTripoliIntegration(unittest.TestCase):

    def test_paystation_works_with_tripoli_factory(self):
        ps = PayStation(TripoliFactory())
        self.assertEqual(ps.config_id, "tripoli")
        ps.add_payment(25)
        receipt = ps.buy()
        rs = BasicRate([200])
        self.assertEqual(rs(25), receipt.value)
        self.assertFalse(receipt.with_barcode)


class TestHortonIntegration(unittest.TestCase):

    def test_paystation_works_with_horton_factory(self):
        ps = PayStation(HortonFactory())
        self.assertEqual(ps.config_id, "horton")
        ps.add_payment(25)
        receipt = ps.buy()
        rs = BasicRate([75, 150, 200])
        self.assertEqual(rs(25), receipt.value)
        self.assertFalse(receipt.with_barcode)

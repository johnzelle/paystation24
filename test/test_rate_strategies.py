# test_rate_strategies.py

import unittest
from paystation.domain import linear_rate, progressive_rate


class TestLinearRate(unittest.TestCase):

    def test_5_cents_gives_2_minutes(self):
        self.assertEqual(2, linear_rate(5))

    def test_10_cents_gives_4_minutes(self):
        self.assertEqual(4, linear_rate(10))


class TestProgressiveRate(unittest.TestCase):

    def test_1_hour_is_1_50(self):
        self.assertEqual(60, progressive_rate(150))

    def test_2_hours_is_3_50(self):
        self.assertEqual(2*60, progressive_rate(350))

    def test_3_hours_is_6_50(self):
        self.assertEqual(3*60, progressive_rate(650))

    def test_4_hour_plus_is_3_dollar_per_hour(self):
        self.assertEqual(4*60, progressive_rate(950))
        self.assertEqual(5*60, progressive_rate(1250))
        self.assertEqual(6*60, progressive_rate(1550))

    def test_partial_30_minutes_for_75_cents(self):
        self.assertEqual(30, progressive_rate(75))

    def test_partial_1_hour_30_minutes_for_250_cents(self):
        self.assertEqual(90, progressive_rate(250))

    def test_large_amount_10_hours_for_2750_cents(self):
        self.assertEqual(600, progressive_rate(2750))

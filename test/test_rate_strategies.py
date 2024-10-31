# test_rate_strategies.py

import unittest
from paystation.domain import linear_rate


class TestLinearRate(unittest.TestCase):

    def test_5_cents_gives_2_minutes(self):
        self.assertEqual(2, linear_rate(5))

    def test_10_cents_gives_4_minutes(self):
        self.assertEqual(4, linear_rate(10))

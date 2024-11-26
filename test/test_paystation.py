# test_paystation.py

import unittest
from paystation.domain import (PayStation,
                               IllegalCoinException,
                               Receipt,
                               linear_rate
                               )

# Mock rate strategy for testing. 1 minute per cent.
def one_to_one_rate(amount):
    return amount

class TestTownFactory:

    config_id = "testtown"

    def create_rate_strategy(self):
        return one_to_one_rate

    def create_receipt(self, amount):
        return Receipt(amount)
        


class TestPayStation(unittest.TestCase):

    def setUp(self):
        self.ps = PayStation(TestTownFactory())

    def add_test_coins(self, coins):
        for coin in coins:
            self.ps.add_payment(coin)

    def test_accepts_nickels(self):
        self.ps.add_payment(5)
        self.assertEqual(5, self.ps.minutes)

    def test_accepts_dime(self):
        self.ps.add_payment(10)
        self.assertEqual(10, self.ps.minutes)

    def test_accepts_quarters(self):
        self.ps.add_payment(25)
        self.assertEqual(25, self.ps.minutes)

    def test_accepts_multipl_coins(self):
        self.add_test_coins([10, 25])
        self.assertEqual(10 + 25, self.ps.minutes)

    def test_reject_illegal_coin(self):
        with self.assertRaises(IllegalCoinException):
            self.ps.add_payment(17)

    def test_buy_gives_proper_receipt(self):
        self.add_test_coins([5, 10, 25])
        receipt = self.ps.buy()
        self.assertEqual(5 + 10 + 25, receipt.value)

    def test_proper_receipt_for_1_dollar(self):
        self.add_test_coins([10, 10, 10, 10, 10, 25, 25,])
        receipt = self.ps.buy()
        self.assertEqual(100, receipt.value)

    def test_buy_clears_display(self):
        self.ps.add_payment(25)
        self.ps.buy()
        self.assertEqual(0, self.ps.minutes)
        self.ps.add_payment(5)
        self.assertEqual(5, self.ps.minutes)

    def test_cancel_clears_transaction(self):
        self.ps.add_payment(25)
        self.ps.cancel()
        self.assertEqual(0, self.ps.minutes)


if __name__ == "__main__":
    unittest.main()

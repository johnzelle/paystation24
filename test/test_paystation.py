# test_paystation.py

import unittest
from paystation.domain import PayStation, IllegalCoinException, Receipt


class TestPayStation(unittest.TestCase):

    def setUp(self):
        self.ps = PayStation()

    def add_test_coins(self, coins):
        for coin in coins:
            self.ps.add_payment(coin)

    def test_displays_2_min_for_5_cents(self):
        self.ps.add_payment(5)
        self.assertEqual(2, self.ps.minutes)

    def test_displays_10_min_for_25_cents(self):
        self.ps.add_payment(25)
        self.assertEqual(25 // 5 * 2, self.ps.minutes)

    def test_displays_14_mins_for_10_and_25(self):
        self.add_test_coins([10, 25])
        self.assertEqual((10+25)//5*2, self.ps.minutes)

    def test_reject_illegal_coin(self):
        with self.assertRaises(IllegalCoinException):
            self.ps.add_payment(17)

    def test_buy_gives_proper_receipt(self):
        self.add_test_coins([5, 10, 25])
        receipt = self.ps.buy()
        self.assertEqual((5 + 10 + 25) // 5 * 2, receipt.value)

    def test_receipt_stores_proper_value(self):
        receipt = Receipt(30)
        self.assertEqual(30, receipt.value)

    def test_proper_receipt_for_1_dollar(self):
        self.add_test_coins([10, 10, 10, 10, 10, 25, 25,])
        receipt = self.ps.buy()
        self.assertEqual(100 // 5 * 2, receipt.value)

    def test_buy_clears_display(self):
        self.ps.add_payment(25)
        self.ps.buy()
        self.assertEqual(0, self.ps.minutes)
        self.ps.add_payment(5)
        self.assertEqual(2, self.ps.minutes)

    def test_cancel_clears_transaction(self):
        self.ps.add_payment(25)
        self.ps.cancel()
        self.assertEqual(0, self.ps.minutes)


if __name__ == "__main__":
    unittest.main()

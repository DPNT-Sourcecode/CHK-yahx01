from lib.solutions.CHK import checkout_solution

import unittest


class TestCheckout(unittest.TestCase):
    def test_checkout(self):
        self.assertEqual(checkout_solution.checkout("ABCBB"), 145)
        self.assertEqual(checkout_solution.checkout("ABCBBd"), -1)
        self.assertEqual(checkout_solution.checkout("AAAAAAAD"), 325)


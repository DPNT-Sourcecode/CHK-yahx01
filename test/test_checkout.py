from lib.solutions.CHK import checkout

import unittest


class TestCheckout(unittest.TestCase):
    def test_checkout(self):
        self.assertEqual(checkout.compute("ABCBB"), 145)
        self.assertEqual(checkout.compute("ABCBBd"), -1)

from lib.solutions.CHK import checkout_solution

import unittest


class TestCheckout(unittest.TestCase):
    def test_checkout(self):
        self.assertEqual(checkout_solution.checkout("ABCBB"), 145)
        self.assertEqual(checkout_solution.checkout("ABCBBd"), -1)
        self.assertEqual(checkout_solution.checkout("AAAAAAAD"), 315)
        self.assertEqual(checkout_solution.checkout("ABCDABCD"), 215)
        self.assertEqual(checkout_solution.checkout("BABDDCAC"), 215)
        self.assertEqual(checkout_solution.checkout("ABCDCBAABCABBAAA"), 495)

    def test_free_e(self):
        self.assertEqual(checkout_solution.checkout("ABCBB"), 145)
        self.assertEqual(checkout_solution.checkout("ABCBBE"), 185)
        self.assertEqual(checkout_solution.checkout("ABCBBEE"), 195)
        self.assertEqual(checkout_solution.checkout("ABCBBEEE"), 235)
        self.assertEqual(checkout_solution.checkout("ABCBBEEEE"), 260)

    def test_a(self):
        self.assertEqual(checkout_solution.checkout("AAAAA"), 200)
        self.assertEqual(checkout_solution.checkout("AAAAAA"), 250)
        self.assertEqual(checkout_solution.checkout("AAAAAAA"), 300)

    def test_f(self):
        self.assertEqual(checkout_solution.checkout("F"), 10)
        self.assertEqual(checkout_solution.checkout("FF"), 20)
        self.assertEqual(checkout_solution.checkout("FFF"), 20)
        self.assertEqual(checkout_solution.checkout("FFFF"), 30)
        self.assertEqual(checkout_solution.checkout("FFFFF"), 40)
        self.assertEqual(checkout_solution.checkout("FFFFFF"), 40)
        self.assertEqual(checkout_solution.checkout("FFFFFFF"), 50)

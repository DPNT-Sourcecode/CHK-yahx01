from lib.solutions.HLO import hello_solution

import unittest


class TestGello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello_solution.hello("bob"), "Hello, bob!")

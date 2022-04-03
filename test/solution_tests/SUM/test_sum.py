from lib.solutions.SUM import sum_solution

import unittest


class TestSum(unittest.TestCase):
    def test_sum(self):
        for x in range(0, 100):
            for y in range(0, 100):
                self.assertEqual(sum_solution.compute(x, y), x + y)

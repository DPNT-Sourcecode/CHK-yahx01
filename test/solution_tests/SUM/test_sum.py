from solutions.SUM import sum_solution

import unittest


class TestSum(unittest.TestCase):
    def test_sum(self):
        for x in range(0, 10):
            for y in range(0, 10):
                self.assertEquals(sum_solution.compute(x, y), x + y)


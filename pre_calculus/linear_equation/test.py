import unittest

from common.helpers import NO_REAL_SOLUTIONS, INFINITE_SOLUTIONS

from pre_calculus.linear_equation.script import linear_equation


class TestLinearEquation(unittest.TestCase):

    def test_no_real_solutions(self):
        self.assertEqual(linear_equation(0, 5), NO_REAL_SOLUTIONS)

    def test_infinite_solutions(self):
        self.assertEqual(linear_equation(0, 0), INFINITE_SOLUTIONS)

    def test_single_solution(self):
        self.assertEqual(linear_equation(2, -4), 2)
        self.assertEqual(linear_equation(3, 6), -2)
        self.assertEqual(linear_equation(1, 1), -1)
        self.assertEqual(linear_equation(-4, 8), 2)
        self.assertEqual(linear_equation(-3, -9), 3)


if __name__ == '__main__':
    unittest.main()

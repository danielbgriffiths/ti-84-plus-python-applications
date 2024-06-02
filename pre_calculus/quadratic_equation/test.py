import unittest

from common.helpers import NO_REAL_SOLUTIONS

from pre_calculus.quadratic_equation.script import quadratic_equation


class TestQuadraticEquation(unittest.TestCase):

    def test_two_real_roots(self):
        roots = quadratic_equation(1, -3, 2)
        self.assertEqual(roots, (2.0, 1.0))

        roots = quadratic_equation(1, 0, -1)
        self.assertEqual(roots, (1.0, -1.0))

    def test_one_real_root(self):
        root = quadratic_equation(1, 2, 1)
        self.assertEqual(root, -1.0)

        root = quadratic_equation(1, -4, 4)
        self.assertEqual(root, 2.0)

    def test_no_real_solutions(self):
        self.assertEqual(quadratic_equation(1, 0, 1), NO_REAL_SOLUTIONS)
        self.assertEqual(quadratic_equation(1, 2, 5), NO_REAL_SOLUTIONS)


if __name__ == '__main__':
    unittest.main()

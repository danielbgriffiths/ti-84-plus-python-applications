import unittest

from common.helpers import NO_REAL_SOLUTIONS, INFINITE_SOLUTIONS

from pre_calculus.polynomial_roots.script import polynomial_roots


class TestPolynomialRoots(unittest.TestCase):

    def test_first_degree_solution(self):
        self.assertEqual(polynomial_roots(1, [2, -4]), 2)
        self.assertEqual(polynomial_roots(1, [0, 1]), NO_REAL_SOLUTIONS)
        self.assertEqual(polynomial_roots(1, [0, 0]), INFINITE_SOLUTIONS)

    def test_second_degree_solution(self):
        self.assertEqual(polynomial_roots(2, [1, -3, 2]), (2.0, 1.0))  # Two real roots
        self.assertEqual(polynomial_roots(2, [1, 2, 1]), ( -1.0,))  # One real root
        roots = polynomial_roots(2, [1, 0, 1])  # Two complex roots
        self.assertAlmostEqual(roots[0].real, 0.0)
        self.assertAlmostEqual(roots[0].imag, 1.0)
        self.assertAlmostEqual(roots[1].real, 0.0)
        self.assertAlmostEqual(roots[1].imag, -1.0)

    def test_third_degree_solution(self):
        self.assertEqual(polynomial_roots(3, [1, -6, 11, -6]), (3.0, 2.0, 1.0))  # Three real roots
        self.assertEqual(polynomial_roots(3, [1, 0, 0, -1]), (1.0, -0.5 + 0.86602540378j, -0.5 - 0.86602540378j))  # One real root, two complex roots

    def test_unsupported_degree(self):
        self.assertEqual(polynomial_roots(4, [1, 0, 0, 0, -1]), "Polynomial of degree 4 is not supported.")


if __name__ == '__main__':
    unittest.main()

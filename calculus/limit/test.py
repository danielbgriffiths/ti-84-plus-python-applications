import unittest
from math import sin, pi

from calculus.limit.script import limit


class TestLimit(unittest.TestCase):

    def test_constant_function(self):
        self.assertAlmostEqual(limit(lambda x: 5, 0), 5)
        self.assertAlmostEqual(limit(lambda x: 5, 10), 5)

    def test_linear_function(self):
        self.assertAlmostEqual(limit(lambda x: 2 * x, 0), 0)
        self.assertAlmostEqual(limit(lambda x: 2 * x, 10), 20)
        self.assertAlmostEqual(limit(lambda x: -3 * x, 0), 0)
        self.assertAlmostEqual(limit(lambda x: -3 * x, 10), -30)

    def test_quadratic_function(self):
        self.assertAlmostEqual(limit(lambda x: x ** 2, 0), 0)
        self.assertAlmostEqual(limit(lambda x: x ** 2, 1), 1)
        self.assertAlmostEqual(limit(lambda x: x ** 2, 2), 4)

    def test_sine_function(self):
        self.assertAlmostEqual(limit(sin, 0), sin(0), delta=1e-5)
        self.assertAlmostEqual(limit(sin, pi / 2), sin(pi / 2), delta=1e-5)
        self.assertAlmostEqual(limit(sin, pi), sin(pi), delta=1e-5)

    def test_function_with_rounding(self):
        self.assertAlmostEqual(limit(lambda x: x ** 2, 1), 1)
        self.assertAlmostEqual(limit(lambda x: sin(x) / x if x != 0 else 1, 0), 1)


if __name__ == '__main__':
    unittest.main()

import unittest
from common.helpers import sin, cos, pi

from calculus.derivative.script import derivative


class TestDerivative(unittest.TestCase):

    def test_constant_function(self):
        self.assertAlmostEqual(derivative(lambda x: 5, 0), 0)
        self.assertAlmostEqual(derivative(lambda x: 5, 10), 0)

    def test_linear_function(self):
        self.assertAlmostEqual(derivative(lambda x: 2 * x, 0), 2)
        self.assertAlmostEqual(derivative(lambda x: 2 * x, 10), 2)
        self.assertAlmostEqual(derivative(lambda x: -3 * x, 0), -3)
        self.assertAlmostEqual(derivative(lambda x: -3 * x, 10), -3)

    def test_quadratic_function(self):
        self.assertAlmostEqual(derivative(lambda x: x ** 2, 0), 0)
        self.assertAlmostEqual(derivative(lambda x: x ** 2, 1), 2)
        self.assertAlmostEqual(derivative(lambda x: x ** 2, 2), 4)

    def test_sine_function(self):
        self.assertAlmostEqual(derivative(sin, 0), cos(0), delta=1e-5)
        self.assertAlmostEqual(derivative(sin, pi / 2), cos(pi / 2), delta=1e-5)
        self.assertAlmostEqual(derivative(sin, pi), cos(pi), delta=1e-5)

    def test_cosine_function(self):
        self.assertAlmostEqual(derivative(cos, 0), -sin(0), delta=1e-5)
        self.assertAlmostEqual(derivative(cos, pi / 2), -sin(pi / 2), delta=1e-5)
        self.assertAlmostEqual(derivative(cos, pi), -sin(pi), delta=1e-5)


if __name__ == '__main__':
    unittest.main()

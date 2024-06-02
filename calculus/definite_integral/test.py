import unittest
from math import sin, cos, pi

from calculus.definite_integral.script import (
    get_h,
    left_riemann_sum,
    right_riemann_sum,
    midpoint_riemann_sum,
    trapezoidal_rule,
    simpsons_rule,
    definite_integral
)


class TestIntegralMethods(unittest.TestCase):

    def test_get_h(self):
        self.assertAlmostEqual(get_h(0, 1, 1000), 0.001)
        self.assertAlmostEqual(get_h(0, 2, 1000), 0.002)

    def test_left_riemann_sum(self):
        self.assertAlmostEqual(left_riemann_sum(lambda x: 1, 0, 1), 1, delta=1e-2)
        self.assertAlmostEqual(left_riemann_sum(lambda x: x, 0, 1), 0.5, delta=1e-2)
        self.assertAlmostEqual(left_riemann_sum(lambda x: x ** 2, 0, 1), 1 / 3, delta=1e-2)
        self.assertAlmostEqual(left_riemann_sum(sin, 0, pi, 10000), 2, delta=1e-2)
        self.assertAlmostEqual(left_riemann_sum(cos, 0, pi / 2, 10000), 1, delta=1e-2)

    def test_right_riemann_sum(self):
        self.assertAlmostEqual(right_riemann_sum(lambda x: 1, 0, 1), 1, delta=1e-2)
        self.assertAlmostEqual(right_riemann_sum(lambda x: x, 0, 1), 0.5, delta=1e-2)
        self.assertAlmostEqual(right_riemann_sum(lambda x: x ** 2, 0, 1), 1 / 3, delta=1e-2)
        self.assertAlmostEqual(right_riemann_sum(sin, 0, pi, 10000), 2, delta=1e-2)
        self.assertAlmostEqual(right_riemann_sum(cos, 0, pi / 2, 10000), 1, delta=1e-2)

    def test_midpoint_riemann_sum(self):
        self.assertAlmostEqual(midpoint_riemann_sum(lambda x: 1, 0, 1), 1, delta=1e-2)
        self.assertAlmostEqual(midpoint_riemann_sum(lambda x: x, 0, 1), 0.5, delta=1e-2)
        self.assertAlmostEqual(midpoint_riemann_sum(lambda x: x ** 2, 0, 1), 1 / 3, delta=1e-2)
        self.assertAlmostEqual(midpoint_riemann_sum(sin, 0, pi, 10000), 2, delta=1e-2)
        self.assertAlmostEqual(midpoint_riemann_sum(cos, 0, pi / 2, 10000), 1, delta=1e-2)

    def test_trapezoidal_rule(self):
        self.assertAlmostEqual(trapezoidal_rule(lambda x: 1, 0, 1), 1, delta=1e-2)
        self.assertAlmostEqual(trapezoidal_rule(lambda x: x, 0, 1), 0.5, delta=1e-2)
        self.assertAlmostEqual(trapezoidal_rule(lambda x: x ** 2, 0, 1), 1 / 3, delta=1e-2)
        self.assertAlmostEqual(trapezoidal_rule(sin, 0, pi, 10000), 2, delta=1e-2)
        self.assertAlmostEqual(trapezoidal_rule(cos, 0, pi / 2, 10000), 1, delta=1e-2)

    def test_simpsons_rule(self):
        self.assertAlmostEqual(simpsons_rule(lambda x: 1, 0, 1), 1, delta=1e-2)
        self.assertAlmostEqual(simpsons_rule(lambda x: x, 0, 1), 0.5, delta=1e-2)
        self.assertAlmostEqual(simpsons_rule(lambda x: x ** 2, 0, 1), 1 / 3, delta=1e-2)
        self.assertAlmostEqual(simpsons_rule(sin, 0, pi, 10000), 2, delta=1e-2)
        self.assertAlmostEqual(simpsons_rule(cos, 0, pi / 2, 10000), 1, delta=1e-2)

    def test_definite_integral(self):
        self.assertAlmostEqual(definite_integral(1, lambda x: 1, 0, 1), 1, delta=1e-2)
        self.assertAlmostEqual(definite_integral(2, lambda x: 1, 0, 1), 1, delta=1e-2)
        self.assertAlmostEqual(definite_integral(3, lambda x: 1, 0, 1), 1, delta=1e-2)
        self.assertAlmostEqual(definite_integral(4, lambda x: 1, 0, 1), 1, delta=1e-2)
        self.assertAlmostEqual(definite_integral(5, lambda x: 1, 0, 1), 1, delta=1e-2)
        self.assertAlmostEqual(definite_integral(1, lambda x: x, 0, 1), 0.5, delta=1e-2)
        self.assertAlmostEqual(definite_integral(2, lambda x: x, 0, 1), 0.5, delta=1e-2)
        self.assertAlmostEqual(definite_integral(3, lambda x: x, 0, 1), 0.5, delta=1e-2)
        self.assertAlmostEqual(definite_integral(4, lambda x: x, 0, 1), 0.5, delta=1e-2)
        self.assertAlmostEqual(definite_integral(5, lambda x: x, 0, 1), 0.5, delta=1e-2)


if __name__ == '__main__':
    unittest.main()

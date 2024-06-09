import unittest
from common.helpers import pi, sqrt

from trigonometry.polar_to_rect.script import polar_to_rect


class TestPolarToRect(unittest.TestCase):

    def test_zero_radius(self):
        self.assertAlmostEqual(polar_to_rect(0, pi/4), (0, 0))

    def test_positive_radius(self):
        self.assertAlmostEqual(polar_to_rect(1, 0), (1, 0))
        self.assertAlmostEqual(polar_to_rect(1, pi/2), (0, 1))
        self.assertAlmostEqual(polar_to_rect(1, pi), (-1, 0))
        self.assertAlmostEqual(polar_to_rect(1, 3*pi/2), (0, -1))
        self.assertAlmostEqual(polar_to_rect(sqrt(2), pi/4), (1, 1))

    def test_negative_radius(self):
        self.assertAlmostEqual(polar_to_rect(-1, 0), (-1, 0))
        self.assertAlmostEqual(polar_to_rect(-1, pi/2), (0, -1))
        self.assertAlmostEqual(polar_to_rect(-1, pi), (1, 0))
        self.assertAlmostEqual(polar_to_rect(-1, 3*pi/2), (0, 1))
        self.assertAlmostEqual(polar_to_rect(-sqrt(2), pi/4), (-1, -1))

    def test_angle_greater_than_2pi(self):
        self.assertAlmostEqual(polar_to_rect(1, 2*pi), (1, 0))
        self.assertAlmostEqual(polar_to_rect(1, 2*pi + pi/2), (0, 1))


if __name__ == '__main__':
    unittest.main()

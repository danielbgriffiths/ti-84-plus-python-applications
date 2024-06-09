import unittest
from common.helpers import pi

from trigonometry.radians_to_degrees.script import radians_to_degrees


class TestRadiansToDegrees(unittest.TestCase):

    def test_zero_radians(self):
        self.assertAlmostEqual(radians_to_degrees(0), 0)

    def test_positive_radians(self):
        self.assertAlmostEqual(radians_to_degrees(pi), 180)
        self.assertAlmostEqual(radians_to_degrees(pi / 2), 90)
        self.assertAlmostEqual(radians_to_degrees(2 * pi), 360)

    def test_negative_radians(self):
        self.assertAlmostEqual(radians_to_degrees(-pi), -180)
        self.assertAlmostEqual(radians_to_degrees(-pi / 2), -90)
        self.assertAlmostEqual(radians_to_degrees(-2 * pi), -360)

    def test_non_integer_radians(self):
        self.assertAlmostEqual(radians_to_degrees(pi / 4), 45)
        self.assertAlmostEqual(radians_to_degrees(3 * pi / 4), 135)
        self.assertAlmostEqual(radians_to_degrees(-pi / 4), -45)


if __name__ == '__main__':
    unittest.main()

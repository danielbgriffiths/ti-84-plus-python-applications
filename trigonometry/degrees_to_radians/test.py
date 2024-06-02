import unittest

from trigonometry.degrees_to_radians.script import degrees_to_radians


class TestDegreesToRadians(unittest.TestCase):

    def test_zero_degrees(self):
        self.assertAlmostEqual(degrees_to_radians(0), 0)

    def test_positive_degrees(self):
        self.assertAlmostEqual(degrees_to_radians(90), pi / 2)
        self.assertAlmostEqual(degrees_to_radians(180), pi)
        self.assertAlmostEqual(degrees_to_radians(360), 2 * pi)

    def test_negative_degrees(self):
        self.assertAlmostEqual(degrees_to_radians(-90), -pi / 2)
        self.assertAlmostEqual(degrees_to_radians(-180), -pi)
        self.assertAlmostEqual(degrees_to_radians(-360), -2 * pi)

    def test_non_integer_degrees(self):
        self.assertAlmostEqual(degrees_to_radians(45.5), 45.5 * (pi / 180))
        self.assertAlmostEqual(degrees_to_radians(-45.5), -45.5 * (pi / 180))


if __name__ == '__main__':
    unittest.main()

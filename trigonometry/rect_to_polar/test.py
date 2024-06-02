import unittest
from math import sqrt, pi

from trigonometry.rect_to_polar.script import rect_to_polar


class TestRectToPolar(unittest.TestCase):

    def test_origin(self):
        self.assertAlmostEqual(rect_to_polar(0, 0), (0, 0))

    def test_positive_x_axis(self):
        self.assertAlmostEqual(rect_to_polar(1, 0), (1, 0))

    def test_positive_y_axis(self):
        self.assertAlmostEqual(rect_to_polar(0, 1), (1, pi/2))

    def test_negative_x_axis(self):
        self.assertAlmostEqual(rect_to_polar(-1, 0), (1, pi))

    def test_negative_y_axis(self):
        self.assertAlmostEqual(rect_to_polar(0, -1), (1, -pi/2))

    def test_first_quadrant(self):
        x, y = 1, 1
        self.assertAlmostEqual(rect_to_polar(x, y), (sqrt(2), pi/4))

    def test_second_quadrant(self):
        x, y = -1, 1
        self.assertAlmostEqual(rect_to_polar(x, y), (sqrt(2), 3*pi/4))

    def test_third_quadrant(self):
        x, y = -1, -1
        self.assertAlmostEqual(rect_to_polar(x, y), (sqrt(2), -3*pi/4))

    def test_fourth_quadrant(self):
        x, y = 1, -1
        self.assertAlmostEqual(rect_to_polar(x, y), (sqrt(2), -pi/4))


if __name__ == '__main__':
    unittest.main()

import unittest
from math import pi, sin, cos, tan

from trigonometry.sum_and_difference.script import sum_and_difference


class TestSumAndDifference(unittest.TestCase):

    def test_sin_sum(self):
        self.assertAlmostEqual(sum_and_difference("sin", "+", pi/6, pi/4), sin(pi/6) * cos(pi/4) + cos(pi/6) * sin(pi/4))
        self.assertAlmostEqual(sum_and_difference("sin", "+", pi/3, pi/6), sin(pi/3) * cos(pi/6) + cos(pi/3) * sin(pi/6))

    def test_sin_diff(self):
        self.assertAlmostEqual(sum_and_difference("sin", "-", pi/6, pi/4), sin(pi/6) * cos(pi/4) - cos(pi/6) * sin(pi/4))
        self.assertAlmostEqual(sum_and_difference("sin", "-", pi/3, pi/6), sin(pi/3) * cos(pi/6) - cos(pi/3) * sin(pi/6))

    def test_cos_sum(self):
        self.assertAlmostEqual(sum_and_difference("cos", "+", pi/6, pi/4), cos(pi/6) * cos(pi/4) - sin(pi/6) * sin(pi/4))
        self.assertAlmostEqual(sum_and_difference("cos", "+", pi/3, pi/6), cos(pi/3) * cos(pi/6) - sin(pi/3) * sin(pi/6))

    def test_cos_diff(self):
        self.assertAlmostEqual(sum_and_difference("cos", "-", pi/6, pi/4), cos(pi/6) * cos(pi/4) + sin(pi/6) * sin(pi/4))
        self.assertAlmostEqual(sum_and_difference("cos", "-", pi/3, pi/6), cos(pi/3) * cos(pi/6) + sin(pi/3) * sin(pi/6))

    def test_tan_sum(self):
        self.assertAlmostEqual(sum_and_difference("tan", "+", pi/6, pi/4), (tan(pi/6) + tan(pi/4)) / (1 - tan(pi/6) * tan(pi/4)))
        self.assertAlmostEqual(sum_and_difference("tan", "+", pi/3, pi/6), (tan(pi/3) + tan(pi/6)) / (1 - tan(pi/3) * tan(pi/6)))

    def test_tan_diff(self):
        self.assertAlmostEqual(sum_and_difference("tan", "-", pi/6, pi/4), (tan(pi/6) - tan(pi/4)) / (1 + tan(pi/6) * tan(pi/4)))
        self.assertAlmostEqual(sum_and_difference("tan", "-", pi/3, pi/6), (tan(pi/3) - tan(pi/6)) / (1 + tan(pi/3) * tan(pi/6)))


if __name__ == '__main__':
    unittest.main()

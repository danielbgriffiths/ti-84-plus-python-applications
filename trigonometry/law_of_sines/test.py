import unittest
from math import sin, asin, radians, degrees

from trigonometry.law_of_sines.script import law_of_sines_angles, law_of_sines_sides


class TestLawOfSines(unittest.TestCase):

    def test_law_of_sines_angles(self):
        self.assertAlmostEqual(law_of_sines_angles(10, radians(30), radians(45)), 10 * sin(radians(45)) / sin(radians(30)))
        self.assertAlmostEqual(law_of_sines_angles(7, radians(60), radians(90)), 7 * sin(radians(90)) / sin(radians(60)))

    def test_law_of_sines_sides(self):
        self.assertAlmostEqual(law_of_sines_sides(10, 5, radians(30)), degrees(asin(5 * sin(radians(30)) / 10)))
        self.assertAlmostEqual(law_of_sines_sides(7, 3.5, radians(60)), degrees(asin(3.5 * sin(radians(60)) / 7)))


if __name__ == '__main__':
    unittest.main()

import unittest
from math import radians, sin

from trigonometry.triangle_area.script import base_height, sas, heron, coords


class TestTriangleArea(unittest.TestCase):

    def test_base_height(self):
        self.assertAlmostEqual(base_height(10, 5), 25)
        self.assertAlmostEqual(base_height(7, 3), 10.5)

    def test_sas(self):
        self.assertAlmostEqual(sas(5, 6, radians(90)), 0.5 * 5 * 6 * 1)
        self.assertAlmostEqual(sas(7, 8, radians(60)), 0.5 * 7 * 8 * sin(radians(60)))

    def test_heron(self):
        self.assertAlmostEqual(heron(3, 4, 5), 6)
        self.assertAlmostEqual(heron(7, 8, 9), 26.832815729997478)

    def test_coords(self):
        self.assertAlmostEqual(coords((0, 0), (4, 0), (4, 3)), 6)
        self.assertAlmostEqual(coords((1, 2), (3, 8), (5, 4)), 12)


if __name__ == '__main__':
    unittest.main()

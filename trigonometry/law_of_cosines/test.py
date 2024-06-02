import unittest

from trigonometry.law_of_cosines.script import law_of_cosines


class TestLawOfCosines(unittest.TestCase):

    def test_right_angle(self):
        self.assertAlmostEqual(law_of_cosines(3, 4, 90), 25)

    def test_acute_angle(self):
        self.assertAlmostEqual(law_of_cosines(5, 7, 45), 16.019237886466847)

    def test_obtuse_angle(self):
        self.assertAlmostEqual(law_of_cosines(8, 15, 120), 373.8001227787525)

    def test_zero_angle(self):
        self.assertAlmostEqual(law_of_cosines(3, 4, 0), 1)

    def test_same_side_lengths(self):
        self.assertAlmostEqual(law_of_cosines(5, 5, 60), 25)

    def test_negative_angle(self):
        self.assertAlmostEqual(law_of_cosines(3, 4, -90), 25)


if __name__ == '__main__':
    unittest.main()

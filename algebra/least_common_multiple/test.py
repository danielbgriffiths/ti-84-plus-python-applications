import unittest

from algebra.least_common_multiple.script import least_common_multiple


class TestLCM(unittest.TestCase):

    def test_lcm(self):
        self.assertEqual(least_common_multiple(48, 18), 144)
        self.assertEqual(least_common_multiple(17, 24), 408)
        self.assertEqual(least_common_multiple(54, 24), 216)
        self.assertEqual(least_common_multiple(101, 103), 10403)
        self.assertEqual(least_common_multiple(12, 15), 60)
        self.assertEqual(least_common_multiple(0, 1), 0)
        self.assertEqual(least_common_multiple(0, 0), 0)


if __name__ == '__main__':
    unittest.main()
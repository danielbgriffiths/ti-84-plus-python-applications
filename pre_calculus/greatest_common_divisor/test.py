import unittest

from pre_calculus.greatest_common_divisor.script import greatest_common_divisor


class TestGreatestCommonDivisor(unittest.TestCase):

    def test_gcd(self):
        self.assertEqual(greatest_common_divisor(48, 18), 6)
        self.assertEqual(greatest_common_divisor(17, 24), 1)
        self.assertEqual(greatest_common_divisor(54, 24), 6)
        self.assertEqual(greatest_common_divisor(101, 103), 1)


if __name__ == '__main__':
    unittest.main()

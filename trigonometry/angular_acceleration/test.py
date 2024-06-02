import unittest

from trigonometry.angular_acceleration.script import angular_acceleration


class TestAngularAcceleration(unittest.TestCase):

    def test_positive_values(self):
        self.assertEqual(angular_acceleration(10, 2), 5)
        self.assertEqual(angular_acceleration(20, 4), 5)

    def test_negative_velocity_change(self):
        self.assertEqual(angular_acceleration(-10, 2), -5)
        self.assertEqual(angular_acceleration(-20, 4), -5)

    def test_negative_time_change(self):
        self.assertEqual(angular_acceleration(10, -2), -5)
        self.assertEqual(angular_acceleration(20, -4), -5)

    def test_zero_velocity_change(self):
        self.assertEqual(angular_acceleration(0, 2), 0)
        self.assertEqual(angular_acceleration(0, 5), 0)

    def test_zero_time_change(self):
        with self.assertRaises(ZeroDivisionError):
            angular_acceleration(10, 0)


if __name__ == '__main__':
    unittest.main()

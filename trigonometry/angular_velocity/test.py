import unittest

from trigonometry.angular_velocity.script import angular_velocity


class TestAngularVelocity(unittest.TestCase):

    def test_positive_values(self):
        self.assertEqual(angular_velocity(10, 2), 5)
        self.assertEqual(angular_velocity(20, 4), 5)

    def test_negative_angle_change(self):
        self.assertEqual(angular_velocity(-10, 2), -5)
        self.assertEqual(angular_velocity(-20, 4), -5)

    def test_negative_time_change(self):
        self.assertEqual(angular_velocity(10, -2), -5)
        self.assertEqual(angular_velocity(20, -4), -5)

    def test_zero_angle_change(self):
        self.assertEqual(angular_velocity(0, 2), 0)
        self.assertEqual(angular_velocity(0, 5), 0)

    def test_zero_time_change(self):
        with self.assertRaises(ZeroDivisionError):
            angular_velocity(10, 0)


if __name__ == '__main__':
    unittest.main()

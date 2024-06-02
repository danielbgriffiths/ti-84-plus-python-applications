import unittest

from pre_calculus.scalar_multiplication.script import scalar_multiplication


class TestScalarMultiplication(unittest.TestCase):

    def test_positive_scalar(self):
        matrix = [[1, 2], [3, 4]]
        scalar = 2
        expected = [[2, 4], [6, 8]]
        self.assertEqual(scalar_multiplication(scalar, matrix), expected)

    def test_negative_scalar(self):
        matrix = [[1, 2], [3, 4]]
        scalar = -1
        expected = [[-1, -2], [-3, -4]]
        self.assertEqual(scalar_multiplication(scalar, matrix), expected)

    def test_zero_scalar(self):
        matrix = [[1, 2], [3, 4]]
        scalar = 0
        expected = [[0, 0], [0, 0]]
        self.assertEqual(scalar_multiplication(scalar, matrix), expected)

    def test_large_scalar(self):
        matrix = [[1, 2], [3, 4]]
        scalar = 1000
        expected = [[1000, 2000], [3000, 4000]]
        self.assertEqual(scalar_multiplication(scalar, matrix), expected)

    def test_empty_matrix(self):
        matrix = []
        scalar = 5
        expected = []
        self.assertEqual(scalar_multiplication(scalar, matrix), expected)


if __name__ == '__main__':
    unittest.main()

import unittest

from common.helpers import INVALID_MATRIX_MESSAGE

from pre_calculus.matrix_addition.script import matrix_addition


class TestMatrixAddition(unittest.TestCase):

    def test_invalid_matrix(self):
        matrix1 = [[1, 2], [3, 4]]
        matrix2 = [[1, 2]]
        self.assertEqual(matrix_addition(matrix1, matrix2), INVALID_MATRIX_MESSAGE)

        matrix1 = []
        matrix2 = [[1, 2], [3, 4]]
        self.assertEqual(matrix_addition(matrix1, matrix2), INVALID_MATRIX_MESSAGE)

    def test_valid_matrix_addition(self):
        matrix1 = [[1, 2], [3, 4]]
        matrix2 = [[5, 6], [7, 8]]
        expected = [[6, 8], [10, 12]]
        self.assertEqual(matrix_addition(matrix1, matrix2), expected)

        matrix1 = [[-1, -2], [-3, -4]]
        matrix2 = [[1, 2], [3, 4]]
        expected = [[0, 0], [0, 0]]
        self.assertEqual(matrix_addition(matrix1, matrix2), expected)

    def test_empty_matrix(self):
        matrix1 = []
        matrix2 = []
        self.assertEqual(matrix_addition(matrix1, matrix2), INVALID_MATRIX_MESSAGE)


if __name__ == '__main__':
    unittest.main()

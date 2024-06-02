import unittest

from common.helpers import INVALID_MATRIX_MESSAGE

from pre_calculus.matrix_multiplication.script import matrix_multiplication


class TestMatrixMultiplication(unittest.TestCase):

    def test_invalid_matrix(self):
        matrix1 = [[1, 2], [3, 4]]
        matrix2 = [[1, 2]]
        self.assertEqual(matrix_multiplication(matrix1, matrix2), INVALID_MATRIX_MESSAGE)

        matrix1 = []
        matrix2 = [[1, 2], [3, 4]]
        self.assertEqual(matrix_multiplication(matrix1, matrix2), INVALID_MATRIX_MESSAGE)

    def test_valid_matrix_multiplication(self):
        matrix1 = [[1, 2], [3, 4]]
        matrix2 = [[5, 6], [7, 8]]
        expected = [[19, 22], [43, 50]]
        self.assertEqual(matrix_multiplication(matrix1, matrix2), expected)

        matrix1 = [[2, 3], [0, 1], [4, 5]]
        matrix2 = [[1, 2], [3, 4]]
        expected = [[11, 16], [3, 4], [19, 28]]
        self.assertEqual(matrix_multiplication(matrix1, matrix2), expected)

    def test_identity_matrix(self):
        matrix1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        matrix2 = [[5, 6, 7], [8, 9, 10], [11, 12, 13]]
        expected = [[5, 6, 7], [8, 9, 10], [11, 12, 13]]
        self.assertEqual(matrix_multiplication(matrix1, matrix2), expected)

    def test_zero_matrix(self):
        matrix1 = [[0, 0], [0, 0]]
        matrix2 = [[1, 2], [3, 4]]
        expected = [[0, 0], [0, 0]]
        self.assertEqual(matrix_multiplication(matrix1, matrix2), expected)


if __name__ == '__main__':
    unittest.main()

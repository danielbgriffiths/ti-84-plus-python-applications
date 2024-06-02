import unittest

from common.helpers import INVALID_MATRIX_MESSAGE

from pre_calculus.matrix_subtraction.script import matrix_subtraction


class TestMatrixSubtraction(unittest.TestCase):

    def test_invalid_matrix(self):
        matrix1 = [[1, 2], [3, 4]]
        matrix2 = [[1, 2]]
        self.assertEqual(matrix_subtraction(matrix1, matrix2), INVALID_MATRIX_MESSAGE)

        matrix1 = []
        matrix2 = [[1, 2], [3, 4]]
        self.assertEqual(matrix_subtraction(matrix1, matrix2), INVALID_MATRIX_MESSAGE)

    def test_valid_matrix_subtraction(self):
        matrix1 = [[5, 6], [7, 8]]
        matrix2 = [[1, 2], [3, 4]]
        expected = [[4, 4], [4, 4]]
        self.assertEqual(matrix_subtraction(matrix1, matrix2), expected)

        matrix1 = [[2, 3], [4, 5], [6, 7]]
        matrix2 = [[1, 1], [1, 1], [1, 1]]
        expected = [[1, 2], [3, 4], [5, 6]]
        self.assertEqual(matrix_subtraction(matrix1, matrix2), expected)

    def test_identity_matrix(self):
        matrix1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        matrix2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        expected = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(matrix_subtraction(matrix1, matrix2), expected)

    def test_zero_matrix(self):
        matrix1 = [[0, 0], [0, 0]]
        matrix2 = [[1, 2], [3, 4]]
        expected = [[-1, -2], [-3, -4]]
        self.assertEqual(matrix_subtraction(matrix1, matrix2), expected)


if __name__ == '__main__':
    unittest.main()

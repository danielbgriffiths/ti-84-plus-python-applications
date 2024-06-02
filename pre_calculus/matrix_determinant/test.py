import unittest

from pre_calculus.matrix_determinant.script import matrix_determinant


class TestMatrixDeterminant(unittest.TestCase):

    def test_2x2_matrix(self):
        matrix = [[1, 2], [3, 4]]
        self.assertEqual(matrix_determinant(matrix), -2)

        matrix = [[2, 5], [7, 1]]
        self.assertEqual(matrix_determinant(matrix), -33)

    def test_3x3_matrix(self):
        matrix = [[6, 1, 1], [4, -2, 5], [2, 8, 7]]
        self.assertEqual(matrix_determinant(matrix), -306)

        matrix = [[1, 2, 3], [0, 1, 4], [5, 6, 0]]
        self.assertEqual(matrix_determinant(matrix), 1)

    def test_4x4_matrix(self):
        matrix = [
            [1, 0, 2, -1],
            [3, 0, 0, 5],
            [2, 1, 4, -3],
            [1, 0, 5, 0]
        ]
        self.assertEqual(matrix_determinant(matrix), 30)

    def test_singular_matrix(self):
        matrix = [[2, 2], [2, 2]]
        self.assertEqual(matrix_determinant(matrix), 0)

    def test_identity_matrix(self):
        matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        self.assertEqual(matrix_determinant(matrix), 1)

    def test_large_determinant(self):
        matrix = [
            [3, 8, 4, 6],
            [9, 6, 2, 3],
            [5, 4, 7, 8],
            [1, 1, 1, 1]
        ]
        self.assertEqual(matrix_determinant(matrix), -348)


if __name__ == '__main__':
    unittest.main()

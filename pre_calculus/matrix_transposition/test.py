import unittest

from pre_calculus.matrix_transposition.script import matrix_transposition


class TestMatrixTransposition(unittest.TestCase):

    def test_square_matrix(self):
        matrix = [[1, 2], [3, 4]]
        expected = [[1, 3], [2, 4]]
        self.assertEqual(matrix_transposition(matrix), expected)

        matrix = [[5, 6], [7, 8]]
        expected = [[5, 7], [6, 8]]
        self.assertEqual(matrix_transposition(matrix), expected)

    def test_rectangular_matrix(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        expected = [[1, 4], [2, 5], [3, 6]]
        self.assertEqual(matrix_transposition(matrix), expected)

        matrix = [[1, 2], [3, 4], [5, 6]]
        expected = [[1, 3, 5], [2, 4, 6]]
        self.assertEqual(matrix_transposition(matrix), expected)

    def test_single_row_matrix(self):
        matrix = [[1, 2, 3]]
        expected = [[1], [2], [3]]
        self.assertEqual(matrix_transposition(matrix), expected)

    def test_single_column_matrix(self):
        matrix = [[1], [2], [3]]
        expected = [[1, 2, 3]]
        self.assertEqual(matrix_transposition(matrix), expected)

    def test_empty_matrix(self):
        matrix = []
        expected = []
        self.assertEqual(matrix_transposition(matrix), expected)


if __name__ == '__main__':
    unittest.main()

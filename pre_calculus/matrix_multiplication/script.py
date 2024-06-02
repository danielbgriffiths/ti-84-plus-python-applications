from common.helpers import is_not_valid_matrix, INVALID_MATRIX_MESSAGE


def matrix_multiplication(matrix1, matrix2):
    if is_not_valid_matrix(matrix1, matrix2):
        return INVALID_MATRIX_MESSAGE

    res = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    for r in range(len(matrix1)):
        for c in range(len(matrix2[0])):
            for i in range(len(matrix2)):
                res[r][c] += matrix1[r][i] * matrix2[i][c]

    return res
from common import express_matrix, gather_matrix, is_not_valid_matrix, INVALID_MATRIX_MESSAGE


def matrix_subtraction(matrix1, matrix2):
    if is_not_valid_matrix(matrix1, matrix2):
        return INVALID_MATRIX_MESSAGE

    res = []
    for r in range(len(matrix1)):
        row = []
        for c in range(len(matrix1[0])):
            row.append(matrix1[r][c] - matrix2[r][c])
        res.append(row)

    return res


print(
    express_matrix(
        matrix_subtraction(
            gather_matrix(),
            gather_matrix()
        )
    )
)

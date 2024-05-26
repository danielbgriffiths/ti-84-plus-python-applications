import common


def matrix_subtraction(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return "Matrices must have the same dimensions for subtraction."

    res = []
    for r in range(len(matrix1)):
        row = []
        for c in range(len(matrix1[0])):
            row.append(matrix1[r][c] - matrix2[r][c])
        res.append(row)

    return common.express_matrix(res)


print(
    matrix_subtraction(
        common.gather_matrix(),
        common.gather_matrix()
    )
)

import common


def matrix_multiplication(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return "Matrices must have the same dimensions for multiplication."

    res = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    for r in range(len(matrix1)):
        for c in range(len(matrix2[0])):
            for i in range(len(matrix2)):
                res[r][c] += matrix1[r][i] * matrix2[i][c]

    return common.express_matrix(res)


print(
    matrix_multiplication(
        common.gather_matrix(),
        common.gather_matrix()
    )
)

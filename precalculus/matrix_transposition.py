import common


def matrix_transposition(matrix):
    res = [[matrix[r][c] for r in range(len(matrix))] for c in range(len(matrix[0]))]

    return common.express_matrix(res)


print(
    matrix_transposition(
        common.gather_matrix()
    )
)

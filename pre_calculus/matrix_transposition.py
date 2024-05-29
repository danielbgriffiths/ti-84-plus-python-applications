from common import express_matrix, gather_matrix


def matrix_transposition(matrix):
    return [[matrix[r][c] for r in range(len(matrix))] for c in range(len(matrix[0]))]


print(
    express_matrix(
        matrix_transposition(
            gather_matrix()
        )
    )
)

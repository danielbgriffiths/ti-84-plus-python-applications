def matrix_determinant(matrix):
    if len(matrix) == 2 and len(matrix[0]) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    determinant = 0
    for c in range(len(matrix)):
        sub_matrix = [row[:c] + row[c + 1:] for row in (matrix[1:])]
        sign = (-1) ** c
        sub_det = matrix_determinant(sub_matrix)
        determinant += sign * matrix[0][c] * sub_det

    return determinant

def scalar_multiplication(scalar, matrix):
    res = []

    for row in matrix:
        res.append([scalar * cell for cell in row])

    return res
from common import express_matrix, gather_matrix, get_float_input


def scalar_multiplication(scalar, matrix):
    res = []

    for row in matrix:
        res.append([scalar * cell for cell in row])

    return res


print(
    express_matrix(
        scalar_multiplication(
            get_float_input("Enter the scalar: "),
            gather_matrix()
        )
    )
)

import common


def scalar_multiplication(scalar, matrix):
    res = []
    for row in matrix:
        res.append([scalar * cell for cell in row])

    return common.express_matrix(res)


print(
    scalar_multiplication(
        float(input("Enter the scalar: ")),
        common.gather_matrix()
    )
)

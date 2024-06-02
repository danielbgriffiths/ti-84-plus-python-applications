from common.helpers import gather_matrix, express_matrix

from pre_calculus.matrix_multiplication.script import matrix_multiplication

print(
    express_matrix(
        matrix_multiplication(
            gather_matrix(),
            gather_matrix()
        )
    )
)

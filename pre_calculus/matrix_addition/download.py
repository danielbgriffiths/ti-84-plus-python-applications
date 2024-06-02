from common.helpers import express_matrix, gather_matrix

from pre_calculus.matrix_addition.script import matrix_addition

print(
    express_matrix(
        matrix_addition(
            gather_matrix(),
            gather_matrix()
        )
    )
)
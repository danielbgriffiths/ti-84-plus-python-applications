from common.helpers import express_matrix, gather_matrix

from pre_calculus.matrix_subtraction.script import matrix_subtraction

print(
    express_matrix(
        matrix_subtraction(
            gather_matrix(),
            gather_matrix()
        )
    )
)

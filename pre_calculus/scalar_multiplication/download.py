from common.helpers import express_matrix, gather_matrix, get_float_input

from pre_calculus.scalar_multiplication.script import scalar_multiplication

print(
    express_matrix(
        scalar_multiplication(
            get_float_input("Enter the scalar: "),
            gather_matrix()
        )
    )
)

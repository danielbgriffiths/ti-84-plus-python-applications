from common.helpers import get_float_input, get_int_input

from pre_calculus.polynomial_roots.script import polynomial_roots

degree_input = get_int_input("Enter the degree of the polynomial: ")

print(
    polynomial_roots(
        degree_input,
        [get_float_input(f"Enter coefficient for x^{degree_input - i}: ") for i in range(degree_input + 1)]
    )
)

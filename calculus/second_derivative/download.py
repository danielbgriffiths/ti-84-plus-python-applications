from common.helpers import get_float_input, str_to_func_input

from calculus.second_derivative.script import second_derivative

print(
    second_derivative(
        str_to_func_input("Enter the function string: "),
        get_float_input("Enter the value of x: ")
    )
)

from common.helpers import get_float_input, str_to_func_input

from calculus.derivative.script import derivative

print(
    derivative(
        str_to_func_input("Enter the function string: "),
        get_float_input("Enter the value of x: ")
    )
)
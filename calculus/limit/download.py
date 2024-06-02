from common.helpers import get_float_input, str_to_func_input

from calculus.limit.script import limit

print(
    limit(
        str_to_func_input("Enter the function string: "),
        get_float_input("Enter the value of x: ")
    )
)
from common.helpers import get_float_input

from pre_calculus.linear_equation.script import linear_equation

print(
    linear_equation(
        get_float_input("Enter coefficient a: "),
        get_float_input("Enter coefficient b: ")
    )
)

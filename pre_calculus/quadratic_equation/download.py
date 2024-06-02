from common.helpers import get_float_input

from pre_calculus.quadratic_equation.script import quadratic_equation

print(
    quadratic_equation(
        get_float_input("Enter coefficient a: "),
        get_float_input("Enter coefficient b: "),
        get_float_input("Enter coefficient c: ")
    )
)
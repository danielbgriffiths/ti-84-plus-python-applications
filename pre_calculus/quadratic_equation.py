from math import sqrt
from common import get_float_input, NO_REAL_SOLUTIONS


def quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + sqrt(discriminant)) / (2*a)
        root2 = (-b - sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        return NO_REAL_SOLUTIONS


print(
    quadratic_equation(
        get_float_input("Enter coefficient a: "),
        get_float_input("Enter coefficient b: "),
        get_float_input("Enter coefficient c: ")
    )
)
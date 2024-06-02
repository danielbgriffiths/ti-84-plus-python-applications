from common import get_float_input, NO_REAL_SOLUTIONS, INFINITE_SOLUTIONS


def linear_equation(a, b):
    if a == 0:
        return NO_REAL_SOLUTIONS if b != 0 else INFINITE_SOLUTIONS

    return -b / a


print(
    linear_equation(
        get_float_input("Enter coefficient a: "),
        get_float_input("Enter coefficient b: ")
    )
)

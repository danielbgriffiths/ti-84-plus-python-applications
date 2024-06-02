from common import get_float_input, NO_REAL_SOLUTIONS


def greatest_common_divisor(a, b):
    while b != 0:
        a = b
        b = a % b
    return a


print(
    greatest_common_divisor(
        get_float_input("Enter the first number: "),
        get_float_input("Enter the second number: ")
    )
)
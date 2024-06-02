from common import get_float_input
from greatest_common_divisor import greatest_common_divisor


def least_common_multiple(a, b):
    return abs(a * b) / greatest_common_divisor(a, b)


print(
    least_common_multiple(
        get_float_input("Enter coefficient a: "),
        get_float_input("Enter coefficient b: ")
    )
)
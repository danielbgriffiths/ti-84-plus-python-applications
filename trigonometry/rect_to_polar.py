from math import sqrt, atan
from common import get_float_input


def rect_to_polar(x, y):
    radius = sqrt(x**2 + y**2)
    theta = atan(y/x)
    return radius, theta


print(
    rect_to_polar(
        get_float_input("Enter x: "),
        get_float_input("Enter y: ")
    )
)

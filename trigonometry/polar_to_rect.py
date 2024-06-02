from math import cos, sin
from common import get_float_input


def polar_to_rect(radius, theta):
    x = radius * cos(theta)
    y = radius * sin(theta)
    return x, y


print(
    polar_to_rect(
        get_float_input("Enter radius: "),
        get_float_input("Enter theta: ")
    )
)
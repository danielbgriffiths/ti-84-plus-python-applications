from math import pi
from common import get_float_input


def degrees_to_radians(degrees):
    return degrees * (pi / 180)


print(
    degrees_to_radians(
        get_float_input("Enter the angle in degrees: ")
    )
)

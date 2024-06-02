from math import pi
from common import get_float_input


def radians_to_degrees(radians):
    return radians * (180 / pi)


print(
    radians_to_degrees(
        get_float_input("Enter the angle in radians: ")
    )
)
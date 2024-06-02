from common.helpers import get_float_input

from trigonometry.degrees_to_radians.script import degrees_to_radians

print(
    degrees_to_radians(
        get_float_input("Enter the angle in degrees: ")
    )
)

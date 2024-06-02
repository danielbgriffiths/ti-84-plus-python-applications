from common.helpers import get_float_input

from trigonometry.radians_to_degrees.script import radians_to_degrees

print(
    radians_to_degrees(
        get_float_input("Enter the angle in radians: ")
    )
)
from common.helpers import get_float_input

from trigonometry.polar_to_rect.script import polar_to_rect

print(
    polar_to_rect(
        get_float_input("Enter radius: "),
        get_float_input("Enter theta: ")
    )
)
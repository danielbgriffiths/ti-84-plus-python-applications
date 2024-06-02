from common.helpers import get_float_input

from trigonometry.rect_to_polar.script import rect_to_polar

print(
    rect_to_polar(
        get_float_input("Enter x: "),
        get_float_input("Enter y: ")
    )
)

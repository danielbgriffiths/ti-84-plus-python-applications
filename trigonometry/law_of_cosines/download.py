from common.helpers import get_float_input

from trigonometry.law_of_cosines.script import law_of_cosines

print(
    law_of_cosines(
        get_float_input("Enter side A: "),
        get_float_input("Enter side B: "),
        get_float_input("Enter angle C (in degrees): ")
    )
)
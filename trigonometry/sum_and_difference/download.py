from common.helpers import get_float_input, get_trig_function, get_operator

from trigonometry.degrees_to_radians.download import degrees_to_radians
from trigonometry.sum_and_difference.script import sum_and_difference

print(
    sum_and_difference(
        get_trig_function("Enter trig function: "),
        get_operator("Enter operator: "),
        degrees_to_radians(
            get_float_input("Enter theta a (in degrees): ")
        ),
        degrees_to_radians(
            get_float_input("Enter theta b (in degrees): ")
        )
    )
)
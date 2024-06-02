from common.helpers import get_float_input

from algebra.least_common_multiple.script import least_common_multiple

print(
    least_common_multiple(
        get_float_input("Enter coefficient a: "),
        get_float_input("Enter coefficient b: ")
    )
)
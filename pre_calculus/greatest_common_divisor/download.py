from common.helpers import get_float_input

from pre_calculus.greatest_common_divisor.script import greatest_common_divisor

print(
    greatest_common_divisor(
        get_float_input("Enter the first number: "),
        get_float_input("Enter the second number: ")
    )
)

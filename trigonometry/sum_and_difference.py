from math import sin, cos, tan
from common import get_float_input, get_trig_function, get_operator
from degrees_to_radians import degrees_to_radians


def sin_sum(a, b):
    return sin(a) * cos(b) + cos(a) * sin(b)


def sin_diff(a, b):
    return sin(a) * cos(b) - cos(a) * sin(b)


def cos_sum(a, b):
    return cos(a) * cos(b) - sin(a) * sin(b)


def cos_diff(a, b):
    return cos(a) * cos(b) + sin(a) * sin(b)


def tan_sum(a, b):
    return (tan(a) + tan(b)) / (1 - tan(a) * tan(b))


def tan_diff(a, b):
    return (tan(a) - tan(b)) / (1 + tan(a) * tan(b))


def sum_and_difference(trig_fn, operator, theta_a, theta_b):
    if trig_fn == "sin":
        return sin_sum(theta_a, theta_b) if operator == "+" else sin_diff(theta_a, theta_b)
    if trig_fn == "cos":
        return cos_sum(theta_a, theta_b) if operator == "+" else cos_diff(theta_a, theta_b)
    if trig_fn == "tan":
        return tan_sum(theta_a, theta_b) if operator == "+" else tan_diff(theta_a, theta_b)


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
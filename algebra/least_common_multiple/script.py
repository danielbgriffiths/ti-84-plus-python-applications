from algebra.greatest_common_divisor.script import greatest_common_divisor


def least_common_multiple(a, b):
    return abs(a * b) / greatest_common_divisor(a, b)
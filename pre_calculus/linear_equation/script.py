from common.helpers import NO_REAL_SOLUTIONS, INFINITE_SOLUTIONS


def linear_equation(a, b):
    if a == 0:
        return NO_REAL_SOLUTIONS if b != 0 else INFINITE_SOLUTIONS

    return -b / a
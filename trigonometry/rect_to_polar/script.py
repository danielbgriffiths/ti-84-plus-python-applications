from math import sqrt, atan


def rect_to_polar(x, y):
    radius = sqrt(x ** 2 + y ** 2)
    theta = atan(y / x)
    return radius, theta

from common.helpers import cos, sin


def polar_to_rect(radius, theta):
    x = radius * cos(theta)
    y = radius * sin(theta)
    return x, y

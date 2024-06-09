from common.helpers import sin, sqrt


BASE_HEIGHT = "base-height"
SAS = "sas"
HERON = "heron"
COORDS = "coords"


def base_height(base, height):
    return 0.5 * base * height


def sas(side_a, side_b, angle_c):
    return 0.5 * side_a * side_b * sin(angle_c)


def heron(side_a, side_b, side_c):
    s = (side_a + side_b + side_c) / 2
    return sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))


def coords(coords_a, coords_b, coords_c):
    x1, y1 = coords_a
    x2, y2 = coords_b
    x3, y3 = coords_c
    absolute = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    return 0.5 * absolute

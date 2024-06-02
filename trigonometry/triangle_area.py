from math import sin, sqrt
from degrees_to_radians import degrees_to_radians
from common import get_float_input, get_coord_input

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


solution_type = input(f"Solution type ({BASE_HEIGHT}, {SAS}, {HERON}, {COORDS}): ")

if solution_type.lower() not in [BASE_HEIGHT, SAS, HERON, COORDS]:
    print("Invalid solution type.")
    exit()

if solution_type.lower() == BASE_HEIGHT:
    print(
        base_height(
            get_float_input("Enter base: "),
            get_float_input("Enter height: ")
        )
    )
    exit()

if solution_type.lower() == SAS:
    print(
        sas(
            get_float_input("Enter side a: "),
            get_float_input("Enter side b: "),
            degrees_to_radians(
                get_float_input("Enter angle c (in degrees): ")
            )
        )
    )
    exit()

if solution_type.lower() == HERON:
    print(
        heron(
            get_float_input("Enter side a: "),
            get_float_input("Enter side b: "),
            get_float_input("Enter side c: ")
        )
    )
    exit()

if solution_type.lower() == COORDS:
    print(
        coords(
            get_coord_input("Enter first coords: "),
            get_coord_input("Enter second coords: "),
            get_coord_input("Enter third coords: "),
        )
    )
    exit()
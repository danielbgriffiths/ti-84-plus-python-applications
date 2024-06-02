from common.helpers import get_float_input, get_coord_input

from trigonometry.degrees_to_radians.download import degrees_to_radians
from trigonometry.triangle_area.script import base_height, sas, heron, coords, BASE_HEIGHT, SAS, HERON, COORDS

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
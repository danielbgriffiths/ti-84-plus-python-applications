from math import sin, asin

from degrees_to_radians import degrees_to_radians
from radians_to_degrees import radians_to_degrees
from common import get_float_input


def law_of_sines_angles(side_a, angle_a, angle_b):
    return side_a * sin(angle_b) / sin(angle_a)


def law_of_sines_sides(side_a, side_b, angle_a):
    angle_b_radians = asin(side_b * sin(angle_a) / side_a)
    return radians_to_degrees(angle_b_radians)


variant_input = input("Enter the variant (angles, sides): ")

if variant_input not in ['angles', 'sides']:
    raise ValueError('variant must be either "angles" or "sides"')

unit_input = input("Enter the unit (degrees, radians): ")

if unit_input not in ['degrees', 'radians']:
    raise ValueError('unit must be either "degrees" or "radians"')

if variant_input == 'angles':
    value_one = get_float_input("Enter angle alpha: ")
    value_two = get_float_input("Enter angle beta: ")
    value_three = get_float_input("Enter side A: ")

    value_one = value_one if unit_input == 'radians' else degrees_to_radians(value_one)
    value_two = value_two if unit_input == 'radians' else degrees_to_radians(value_two)

    print(
        law_of_sines_angles(
            value_one,
            value_two,
            value_three
        )
    )

elif variant_input == 'sides':
    value_one = get_float_input("Enter angle alpha: ")
    value_two = get_float_input("Enter enter side A: ")
    value_three = get_float_input("Enter enter side B: ")

    value_one = value_one if unit_input == 'radians' else degrees_to_radians(value_one)

    print(
        law_of_sines_sides(
            value_one,
            value_two,
            value_three
        )
    )

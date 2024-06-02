from common.helpers import get_float_input

from trigonometry.degrees_to_radians.script import degrees_to_radians
from trigonometry.law_of_sines.script import law_of_sines_angles, law_of_sines_sides

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

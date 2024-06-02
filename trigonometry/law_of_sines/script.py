from math import sin, asin

from trigonometry.radians_to_degrees.script import radians_to_degrees


def law_of_sines_angles(side_a, angle_a, angle_b):
    return side_a * sin(angle_b) / sin(angle_a)


def law_of_sines_sides(side_a, side_b, angle_a):
    angle_b_radians = asin(side_b * sin(angle_a) / side_a)
    return radians_to_degrees(angle_b_radians)

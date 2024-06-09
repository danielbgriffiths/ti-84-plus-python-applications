from common.helpers import cos

from trigonometry.degrees_to_radians.download import degrees_to_radians


def law_of_cosines(side_a, side_b, angle_c):
    side_a_squared = side_a**2
    side_b_squared = side_b**2
    angle_c_radians = degrees_to_radians(angle_c)
    return side_a_squared + side_b_squared - 2*side_a*side_b*cos(angle_c_radians)

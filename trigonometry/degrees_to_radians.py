from math import pi


def degrees_to_radians(degrees):
    return degrees * (pi / 180)


print(
    degrees_to_radians(
        float(input("Enter the angle in degrees: "))
    )
)

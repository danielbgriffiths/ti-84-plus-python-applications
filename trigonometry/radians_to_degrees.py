from math import pi


def radians_to_degrees(radians):
    return radians * (180 / pi)


print(
    radians_to_degrees(
        float(input("Enter the angle in radians: "))
    )
)
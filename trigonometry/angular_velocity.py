from common import get_float_input


def angular_velocity(change_in_angle, change_in_time):
    return change_in_angle / change_in_time


print(
    angular_velocity(
        get_float_input("Delta theta: "),
        get_float_input("Delta time: ")
    )
)

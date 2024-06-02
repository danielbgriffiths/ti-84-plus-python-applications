from common import get_float_input


def angular_acceleration(change_in_velocity, change_in_time):
    return change_in_velocity / change_in_time


print(
    angular_acceleration(
        get_float_input("Delta velocity: "),
        get_float_input("Delta time: ")
    )
)

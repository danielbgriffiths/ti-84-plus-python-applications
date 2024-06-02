from common.helpers import get_float_input

from trigonometry.angular_velocity.script import angular_velocity

print(
    angular_velocity(
        get_float_input("Delta theta: "),
        get_float_input("Delta time: ")
    )
)

from common.helpers import get_float_input

from trigonometry.angular_acceleration.script import angular_acceleration

print(
    angular_acceleration(
        get_float_input("Delta velocity: "),
        get_float_input("Delta time: ")
    )
)

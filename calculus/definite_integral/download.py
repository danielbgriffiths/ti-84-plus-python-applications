from common.helpers import get_float_input, get_int_input

from calculus.definite_integral.script import definite_integral

print(
    definite_integral(
        get_int_input("Enter Method (1=left_riemann_sum, 2=right_riemann_sum, 3=midpoint_riemann_sum, "
                      "4=trapezoidal_rule, 5=simpsons_rule): "),
        get_float_input("Enter bound a: "),
        get_float_input("Enter bound b: "),
        get_float_input("Enter interation constraint (1000): ")
    )
)
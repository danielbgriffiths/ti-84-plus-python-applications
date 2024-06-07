INVALID_INPUT = "Invalid Input"


def get_h(a, b, n):
    return (b - a) / n


def left_riemann_sum(func, a, b, n=1000):
    h = get_h(a, b, n)
    result = 0
    for i in range(n):
        result += func(a + i * h)
    return result * h


def right_riemann_sum(func, a, b, n=1000):
    h = get_h(a, b, n)
    result = 0
    for i in range(1, n + 1):
        result += func(a + i * h)
    return result * h


def midpoint_riemann_sum(func, a, b, n=1000):
    h = get_h(a, b, n)
    result = 0
    for i in range(n):
        result += func(a + (i + 0.5) * h)
    return result * h


def trapezoidal_rule(func, a, b, n=1000):
    h = get_h(a, b, n)
    result = 0.5 * (func(a) + func(b))
    for i in range(1, n):
        result += func(a + i * h)
    return result * h


def simpsons_rule(func, a, b, n=1000):
    if n % 2 == 1:
        n += 1
    h = get_h(a, b, n)
    result = func(a) + func(b)
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            result += 2 * func(x)
        else:
            result += 4 * func(x)
    return result * h / 3


def definite_integral(impl, func, a, b, n=1000):
    if impl == 1:
        return left_riemann_sum(func, a, b, n)
    elif impl == 2:
        return right_riemann_sum(func, a, b, n)
    elif impl == 3:
        return midpoint_riemann_sum(func, a, b, n)
    elif impl == 4:
        return trapezoidal_rule(func, a, b, n)
    elif impl == 5:
        return simpsons_rule(func, a, b, n)
    else:
        return INVALID_INPUT


def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def str_to_func_input(func_string):
    safe_globals = {
        '__builtins__': None,
    }

    safe_locals = {}

    if all(char in "0123456789+-*/().x " for char in func_string):
        return eval("lambda x: " + func_string, safe_globals, safe_locals)
    else:
        raise ValueError("Invalid characters in function string")


impl_input = get_int_input("Enter Method (1=left_riemann_sum, 2=right_riemann_sum, 3=midpoint_riemann_sum, 4=trapezoidal_rule, 5=simpsons_rule): ")

func_input = str_to_func_input(input("Enter function string: "))

bound_a_input = get_float_input("Enter bound a: ")

bound_b_input = get_float_input("Enter bound b: ")

iteration_input = get_int_input("Enter interation constraint (1000): ")

print(
    definite_integral(
        impl_input,
        func_input,
        bound_a_input,
        bound_b_input,
        iteration_input
    )
)

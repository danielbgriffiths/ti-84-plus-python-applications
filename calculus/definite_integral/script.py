from common.helpers import INVALID_INPUT


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

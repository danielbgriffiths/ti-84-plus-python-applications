def second_derivative(func, x, h=1e-5):
    numerator = func(x + h) - 2 * func(x) + func(x - h)
    denominator = h ** 2
    return numerator / denominator

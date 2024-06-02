def derivative(func, x, h=1e-5):
    return (func(x + h) - func(x)) / h

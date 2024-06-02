def limit(func, x, h=1e-5):
    return (func(x + h) + func(x - h)) / 2

import math


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


def get_operator(prompt):
    while True:
        operator = input(prompt)
        if operator in ["+", "-"]:
            return operator
        print("Invalid operator. Please enter '+' or '-'.")


def get_trig_function(prompt):
    while True:
        trig_fn = input(prompt)
        if trig_fn in ["sin", "cos", "tan"]:
            return trig_fn
        print("Invalid trig function. Please enter 'sin', 'cos', or 'tan'.")


def get_coord_input(prompt):
    while True:
        try:
            x, y = input(prompt).split()
            return float(x), float(y)
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")


def gather_matrix():
    row_count = int(input("Enter the number of rows: "))
    col_count = int(input("Enter the number of columns: "))
    matrix = []
    for r in range(row_count):
        row = []
        for c in range(col_count):
            cell_input = input(f"Enter the element at row {r + 1} and column {c + 1}: ")
            row.append(float(cell_input))
        matrix.append(row)
    return matrix


def express_matrix(matrix):
    print("Resultant matrix:")
    for row in matrix:
        print(row)


def is_not_valid_matrix(matrix1, matrix2):
    return len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0])


def str_to_func_input(func_string):
    safe_globals = {
        '__builtins__': None,
        'math': math
    }

    safe_locals = {}

    if all(char in "0123456789+-*/().x " for char in func_string):
        return eval("lambda x: " + func_string, safe_globals, safe_locals)
    else:
        raise ValueError("Invalid characters in function string")


# Babylonian Method
def sqrt(n, tolerance=1e-10):
    if n < 0:
        raise ValueError("Cannot compute the square root of a negative number")
    if n == 0:
        return 0

    x = n / 2
    while True:
        next_x = 0.5 * (x + n / x)
        if abs(x - next_x) < tolerance:
            return next_x
        x = next_x


# Nilakantha Series
def pi(iterations=100000):
    res = 3.0
    sign = 1
    for i in range(2, 2 + 2 * iterations, 2):
        res += sign * 4 / (i * (i + 1) * (i + 2))
        sign *= -1
    return res


def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def sin(x, terms=10):
    sine = 0
    for n in range(terms):
        sine += ((-1)**n * x**(2*n + 1)) / factorial(2*n + 1)
    return sine


def cos(x, terms=10):
    cosine = 0
    for n in range(terms):
        cosine += ((-1)**n * x**(2*n)) / factorial(2*n)
    return cosine


def tan(x, terms=10):
    sine = sin(x, terms)
    cosine = cos(x, terms)
    if cosine == 0:
        raise ValueError("Tangent undefined for this input (cosine is zero).")
    return sine / cosine


def cot(x, terms=10):
    tangent = tan(x, terms)
    if tangent == 0:
        raise ValueError("Cotangent undefined for this input (tangent is zero).")
    return 1 / tangent


def sec(x, terms=10):
    cosine = cos(x, terms)
    if cosine == 0:
        raise ValueError("Secant undefined for this input (cosine is zero).")
    return 1 / cosine


def csc(x, terms=10):
    sine = sin(x, terms)
    if sine == 0:
        raise ValueError("Cosecant undefined for this input (sine is zero).")
    return 1 / sine


def asin(x, terms=10):
    if x < -1 or x > 1:
        raise ValueError("arcsin is only defined for -1 <= x <= 1")
    res = 0
    for n in range(terms):
        coefficient = factorial(2*n) / (4**n * factorial(n)**2 * (2*n + 1))
        res += coefficient * x**(2*n + 1)
    return res


def acos(x, terms=10):
    if x < -1 or x > 1:
        raise ValueError("arccos is only defined for -1 <= x <= 1")
    return (pi() / 2) - asin(x, terms)


def atan(x, terms=10):
    res = 0
    for n in range(terms):
        res += ((-1)**n * x**(2*n + 1)) / (2*n + 1)
    return res


def acot(x, terms=10):
    return (pi() / 2) - atan(x, terms)


def asec(x, terms=10):
    if abs(x) < 1:
        raise ValueError("arcsec is only defined for |x| >= 1")
    return acos(1 / x, terms)


def acsc(x, terms=10):
    if abs(x) < 1:
        raise ValueError("arccsc is only defined for |x| >= 1")
    return asin(1 / x, terms)


INVALID_MATRIX_MESSAGE = "Matrices must have the same dimensions for multiplication."
NO_REAL_SOLUTIONS = "No real solutions."
INFINITE_SOLUTIONS = "Infinite solutions."
INVALID_INPUT = "Invalid Input"

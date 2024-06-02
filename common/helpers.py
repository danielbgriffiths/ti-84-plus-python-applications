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


INVALID_MATRIX_MESSAGE = "Matrices must have the same dimensions for multiplication."
NO_REAL_SOLUTIONS = "No real solutions."
INFINITE_SOLUTIONS = "Infinite solutions."
INVALID_INPUT = "Invalid Input"

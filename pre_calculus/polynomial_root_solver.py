from math import sqrt, acos, cos, pi


# Degree 1: Linear Polynomials
# ax + b = 0
def first_degree_solution(coefficients):
    a = coefficients[0]
    b = coefficients[1]

    if a == 0:
        return "-- None --" if b != 0 else "-- Infinite --"

    return -b / a


# Degree 2: Quadratic Polynomials
# ax^2 + bx + c = 0
def second_degree_solution(coefficients):
    a = coefficients[0]
    b = coefficients[1]
    c = coefficients[2]

    if a == 0:
        return first_degree_solution([b, c])

    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + sqrt(discriminant)) / (2 * a)
        root2 = (-b - sqrt(discriminant)) / (2 * a)
        return root1, root2

    elif discriminant == 0:
        root = -b / (2 * a)
        return (root,)

    else:
        real_part = -b / (2 * a)
        imaginary_part = sqrt(-discriminant) / (2 * a)
        return complex(real_part, imaginary_part), complex(real_part, -imaginary_part)


# Degree 3: Cubic Polynomials
# ax^3 + bx^2 + cx + d = 0
def third_degree_solution(coefficients):
    a = coefficients[0]
    b = coefficients[1]
    c = coefficients[2]
    d = coefficients[3]

    if a == 0:
        return second_degree_solution([b, c, d])

    p = (3 * a * c - b ** 2) / (3 * a ** 2)
    q = (2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d) / (27 * a ** 3)
    discriminant = q ** 2 / 4 + p ** 3 / 27

    if discriminant > 0:
        u = (-q / 2 + sqrt(discriminant)) ** (1 / 3)
        v = (-q / 2 - sqrt(discriminant)) ** (1 / 3)
        root1 = u + v - b / (3 * a)
        return (root1,)

    elif discriminant == 0:
        u = (-q / 2) ** (1 / 3)
        root1 = 2 * u - b / (3 * a)
        root2 = -u - b / (3 * a)
        return root1, root2

    else:
        r = sqrt(-p ** 3 / 27)
        theta = acos(-q / (2 * r))
        root1 = 2 * r ** (1 / 3) * cos(theta / 3) - b / (3 * a)
        root2 = 2 * r ** (1 / 3) * cos((theta + 2 * pi) / 3) - b / (3 * a)
        root3 = 2 * r ** (1 / 3) * cos((theta + 4 * pi) / 3) - b / (3 * a)
        return root1, root2, root3


def polynomial_root_solver(degree, coefficients):
    if degree == 1:
        return f"The root is {first_degree_solution(coefficients)}"
    elif degree == 2:
        return f"The root(s) is/are {second_degree_solution(coefficients)}"
    elif degree == 3:
        return f"The roots are {third_degree_solution(coefficients)}"
    else:
        return f"Polynomial of degree {degree} is not supported."


degree_input = int(input("Enter the degree of the polynomial: "))


print(
    polynomial_root_solver(
        degree_input,
        [float(input(f"Enter coefficient for x^{degree_input - i}: ")) for i in range(degree_input + 1)]
    )
)

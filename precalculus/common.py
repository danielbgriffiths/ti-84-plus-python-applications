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
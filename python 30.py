def find_sum(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    row_sums = [sum(row) for row in matrix]
    col_sums = [sum(col) for col in zip(*matrix)]

    main_diag_sum = sum(matrix[i][i] for i in range(min(num_rows, num_cols)))

    return row_sums, col_sums, main_diag_sum

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

row_sums, col_sums, main_diag_sum = find_sum(matrix)

print("Row Sums:", row_sums)
print("Column Sums:", col_sums)
print("Main Diagonal Sum:", main_diag_sum)

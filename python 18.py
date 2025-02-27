def matrix_addition(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return None  # Matrices should have the same dimensions for addition

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

# Example matrices
matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

# Perform matrix addition
result_matrix = matrix_addition(matrix1, matrix2)

# Print the result
if result_matrix:
    print("Result of matrix addition:")
    for row in result_matrix:
        print(row)
else:
    print("Matrices have different dimensions. Addition is not possible.")

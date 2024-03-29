def print_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j * 2, end=" ")
        print()

# Number of rows in the pattern
rows = 5

# Print the pattern
print_pattern(rows)

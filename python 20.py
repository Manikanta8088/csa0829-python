def multiplication_table(m, n):
    for i in range(1, n + 1):
        print(f"{m} x {i} = {m * i}")

# Get input from the user
m = int(input("Enter the number for multiplication table: "))
n = int(input("Enter the limit for multiplication table: "))

# Print the multiplication table
print(f"Multiplication table of {m} up to {n}:")
multiplication_table(m, n)

def print_numbers_skip(M, N, K):
    if M > N:
        print("M should be less than or equal to N.")
        return

    print("Numbers from", M, "to", N, "skipping", K, "numbers in between:")
    while M <= N:
        print(M, end=" ")
        M += K + 1

# Input values from the user
M = int(input("Enter the starting number (M): "))
N = int(input("Enter the ending number (N): "))
K = int(input("Enter the number of skips (K): "))

# Print the numbers
print_numbers_skip(M, N, K)

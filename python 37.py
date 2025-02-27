def nth_largest_number(numbers, n):
    sorted_numbers = sorted(numbers, reverse=True)
    if n <= len(sorted_numbers):
        return sorted_numbers[n - 1]
    else:
        return None

if __name__ == "__main__":
    numbers = [int(x) for x in input("Enter the list of numbers separated by spaces: ").split()]
    n = int(input("Enter the value of N: "))

    nth_largest = nth_largest_number(numbers, n)
    if nth_largest is not None:
        print(f"The {n}th largest number in the list is: {nth_largest}")
    else:
        print("Invalid input for N. It should be within the range of the list.")

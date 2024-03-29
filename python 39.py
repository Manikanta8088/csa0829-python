def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def count_prime_and_composite(numbers):
    prime_count = 0
    composite_count = 0
    for num in numbers:
        if is_prime(num):
            prime_count += 1
        else:
            composite_count += 1
    return prime_count, composite_count

# Get input from the user
numbers = []
while True:
    num = input("Enter a number (type 'done' to finish): ")
    if num.lower() == 'done':
        break
    numbers.append(int(num))

# Count prime and composite numbers
prime_count, composite_count = count_prime_and_composite(numbers)

# Print the results
print("Number of prime numbers:", prime_count)
print("Number of composite numbers:", composite_count)

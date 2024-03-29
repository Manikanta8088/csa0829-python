def fibonacci(n):
    if n <= 0:
        return "N must be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_prev = 0
        fib_curr = 1
        for _ in range(2, n):
            fib_next = fib_prev + fib_curr
            fib_prev = fib_curr
            fib_curr = fib_next
        return fib_curr


n = 8
nth_fibonacci = fibonacci(n)
print(f"The {n}th Fibonacci number is: {nth_fibonacci}")

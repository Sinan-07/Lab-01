def fibonacci(n):
    a, b = 0, 1
    fib_sequence = [a]

    while len(fib_sequence) < n:
        a, b = b, a + b
        fib_sequence.append(a)

    return fib_sequence

# Example: Print the first 10 numbers in the Fibonacci sequence
n = 10
result = fibonacci(n)
print(result)

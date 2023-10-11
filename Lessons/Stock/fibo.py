def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1

    while len(fib_sequence) < n:
        fib_sequence.append(a)
        
        a, b = b, a + b

    return fib_sequence

# Example usage:
n = 10  # Change this to generate a different number of Fibonacci numbers
result = fibonacci(n)
print(result)

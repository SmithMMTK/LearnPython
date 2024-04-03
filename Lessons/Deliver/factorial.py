# Factorial program

def factorial(n):
    if n == 0:
        return 1
    else:
        # loop from 1 to n and multiply each number with the previous one
        result = 1
        for i in range(1, n+1):
            result *= i
        return result

# Example usage:
n = 5  # Change this to generate a different factorial

result = factorial(n)
print("factorial :", n ," = ", result)
# Output: 120

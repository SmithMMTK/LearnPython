def recursive_sum(n):
    if n == 0:
        print("returning stack")
        return 0  # Base case: when n is 0, the sum is 0
    else:
        print("i'm running on n = ", n)
        return n + recursive_sum(n - 1)  # Recursive case: add n to the sum of numbers from 0 to n-1

# Calling the function to get the sum from 0 to 10
print(recursive_sum(10))


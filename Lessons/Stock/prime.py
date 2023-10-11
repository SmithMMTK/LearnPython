def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0:
        return False

    for i in range(5, n):
        if n % i == 0:
            return False

    return True

def find_primes(upper_limit):
    if upper_limit < 2:
        return []

    primes = [2, 3]

    for num in range(5, upper_limit + 1):
        if is_prime(num):
            primes.append(num)

    return primes

# Example usage:
upper_limit = 30
prime_numbers = find_primes(upper_limit)
print("Prime numbers up to", upper_limit, "are:", prime_numbers)

# Function to calculate the greatest common divisor (GCD)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to calculate the modular multiplicative inverse
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Choose two small prime numbers (for simplicity)
p = 61
q = 53

# Calculate n (modulus)
n = p * q

# Calculate φ(n)
phi_n = (p - 1) * (q - 1)

# Choose a public exponent (e) such that 1 < e < φ(n) and gcd(e, φ(n)) == 1
e = 17

# Calculate the private exponent (d) as the modular inverse of e mod φ(n)
d = mod_inverse(e, phi_n)

# Public key: (e, n)
public_key = (e, n)

# Private key: (d, n)
private_key = (d, n)

# Function to encrypt a message
def encrypt(message, public_key):
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

# Function to decrypt a ciphertext
def decrypt(ciphertext, private_key):
    d, n = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return decrypted_message

# Example usage
message = "Hello, RSA!"

encrypted_message = encrypt(message, public_key)
print("Encrypted message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, private_key)
print("Decrypted message:", decrypted_message)

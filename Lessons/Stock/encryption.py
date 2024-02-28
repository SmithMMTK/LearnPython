from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()

# Convert the key to a string
key_string = key.decode()

# Print out the key
print("Generated key:", key_string)

# Save the key to a file
with open("key.txt", "w") as key_file:
    key_file.write(key_string)

# Create a Fernet cipher object with the key
cipher = Fernet(key)

# Message to encrypt
message = b"Hello, this is a secret message."

# Encrypt the message
encrypted_message = cipher.encrypt(message)
print("Encrypted message:", encrypted_message)

# Decrypt the message
decrypted_message = cipher.decrypt(encrypted_message)
print("Decrypted message:", decrypted_message.decode())



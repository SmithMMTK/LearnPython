from cryptography.fernet import Fernet

# Read the key from the file
with open("key.txt", "r") as key_file:
    key_string = key_file.read()

# Convert the key string back to bytes
key = key_string.encode()

# Create a Fernet cipher object with the loaded key
cipher = Fernet(key)

# Now you can use the cipher object for encryption and decryption

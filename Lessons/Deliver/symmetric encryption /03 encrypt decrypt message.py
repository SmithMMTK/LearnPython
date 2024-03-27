# Import module from "02 load key.py"

from cryptography.fernet import Fernet

# Prompt for key file name and load into key variable
key_file_name = input("Enter the key file name: ")
try:
    with open(key_file_name, "r") as key_file:
        key_string = key_file.read()
        key = key_string.encode()
        print("Key loaded successfully")
except:
    print("Error loading key from", key_file_name)
    # Exit the program
    exit()

# Create a Fernet object
cipher_suite = Fernet(key)


# Prompt for message to encrypt
message = input("Enter the message to encrypt: ")

# Encrypt the message
cipher_text = cipher_suite.encrypt(message.encode())

# Print the encrypted message
print("The encrypted message is:", cipher_text.decode())


# Decrypt the message
plain_text = cipher_suite.decrypt(cipher_text)

# Print the decrypted message
print("The decrypted message is:", plain_text.decode())









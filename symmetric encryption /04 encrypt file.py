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


# Prompt to get file name to encrypt
file_name = input("Enter the file name to encrypt: ")

# Open the file and read the contents
try:
    with open(file_name, "r") as file:
        message = file.read()
        print("File loaded successfully")
except:
    print("Error loading file", file_name)
    # Exit the program
    exit()

# Encrypt the file contents
cipher_text = cipher_suite.encrypt(message.encode())

# Prompt to get file name to save the encrypted message
cipher_file_name = input("Enter the file name to save the encrypted message: ")

# Save the encrypted message to a file and return success message if successful else return error message
try:
    with open(cipher_file_name, "w") as cipher_file:
        cipher_file.write(cipher_text.decode())
        print("Encrypted message saved to", cipher_file_name)
except:
    print("Error saving encrypted message to", cipher_file_name)
    # Exit the program
    exit()
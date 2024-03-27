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
file_name = input("Enter the file name to decrypt: ")

# Open the file and read the contents
try:
    with open(file_name, "r") as file:
        message = file.read()
        print("File loaded successfully")
except:
    print("Error loading file", file_name)
    # Exit the program
    exit()

# Decrypt the file contents
decrypted_message = cipher_suite.decrypt(message.encode())


# Prompt to get file name to save the decrypted message
decrypted_file_name = input("Enter the file name to save the decrypted message: ")

# Save the decrypted message to a file and return success message if successful else return error message
try:
    with open(decrypted_file_name, "w") as decrypted_file:
        decrypted_file.write(decrypted_message.decode())
        print("Decrypted message saved to", decrypted_file_name)
except:
    print("Error saving decrypted message to", decrypted_file_name)
    # Exit the program
    exit()

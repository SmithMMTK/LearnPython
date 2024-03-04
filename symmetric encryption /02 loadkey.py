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


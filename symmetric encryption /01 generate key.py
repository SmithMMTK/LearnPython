from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()

# Convert the key to a string
key_string = key.decode()

# Print out the key
print("The Generated key is:", key_string)

# Save the key to a file and return success message if successful else return error message
try:
    with open("key.txt", "w") as key_file:
        key_file.write(key_string)
        print("Key saved to key.txt")
except:
    print("Error saving key to key.txt")
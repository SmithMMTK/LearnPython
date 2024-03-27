# Open the binary file in binary read mode ('rb')
file = open('binary_data.bin', 'rb')
# Read the binary data from the file
binary_data = file.read()

# Display the binary data
print(binary_data)


# Close the file
file.close()

# Open a file in binary write mode ('wb')
file = open('binary_data.bin', 'wb')
    # Write binary data to the file
binary_data = b'\x48\x65\x6C\x6C\x6F\x20\x57\x6F\x72\x6C\x64'  # Example binary data (Hello World)
file.write(binary_data)

# Close the file
file.close()

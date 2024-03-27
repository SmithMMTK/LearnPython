
# Open Text file and read from it line by line
# Open the file for reading
file = open("new_file.txt", "r")

# Read the file line by line
for line in file:
    #print(line)
    # print(line, end="")  # This will remove the extra line breaks
    print(line, end="")

# Close the file
file.close()
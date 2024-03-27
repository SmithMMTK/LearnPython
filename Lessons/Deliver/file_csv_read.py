# Read CSV file
# Title, Name, Email
# Mr., John Smith, john.smith@gmail

# Open the file for reading
file = open("new_file.csv", "r")

# Read the file line by line
for line in file:
    #print(line)
    # print(line, end="")  # This will remove the extra line breaks
    print(line, end="")

# Close the file
file.close()

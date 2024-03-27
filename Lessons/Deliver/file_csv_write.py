# Write CSV file
# Title, Name, Email
# Mr., John Smith, john.smith@gmail

# Open a new file for writing
file = open("new_file.csv", "w")

# Write to the file
file.write("Title, Name, Email\n")
file.write("Mr., John Smith, john.smith@gmail\n")
file.write("Mrs., Jane Smith, jane.smith@gmail\n")
file.write("Mr., John Doe, john.doe@gmail\n")

# Close the file
file.close()

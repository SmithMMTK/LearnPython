def is_palindrome(word):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    word = word.replace(" ", "").lower()

    # Initialize variables for the forward and backward words
    forward = word
    backward = ""

    # Reverse the word
    for char in word:
        backward = char + backward

    # Check if the word is equal to its reverse
    return forward == backward

# Input file name
file_name = input("Enter the name of the file: ")

try:
    with open(file_name, 'r') as file:
        found_palindromes = []
        line_number = 1

        for line in file:
            # Split the line into words
            words = line.split()
            
            for word in words:
                if is_palindrome(word):
                    found_palindromes.append((line_number, word))
                    print(f"Found a palindrome '{word}' in line {line_number}")
                line_number += 1

except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

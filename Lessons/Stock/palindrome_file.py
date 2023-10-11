def is_palindrome(word):

    # if word is 'a' return False
    if len(word) == 1:
        return False

    # Remove spaces and convert to lowercase for case-insensitive comparison
    word = word.replace(" ", "").lower()

    word = word.lower()
    filtered_word = ''

    for char in word:
        if char not in (' ', ',', '.', '!', '?', '"', "'", ';', ':', '-'):
            filtered_word += char

    # Initialize variables for the forward and backward words
    forward = filtered_word
    backward = ""

    # Reverse the word
    for char in filtered_word:
        backward = char + backward

    # Check if the word is equal to its reverse

    if forward == '':
        return False
    else:
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

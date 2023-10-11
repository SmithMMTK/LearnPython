def is_palindrome(input_string):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    input_string = input_string.replace(" ", "").lower()
    
    # Initialize variables for the forward and backward strings
    forward = input_string
    backward = ""

    # Reverse the string
    for char in input_string:
        backward = char + backward

    # Check if the string is equal to its reverse
    return forward == backward

# Input string to check for palindrome
user_input = input("Enter a string: ")

if is_palindrome(user_input):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")

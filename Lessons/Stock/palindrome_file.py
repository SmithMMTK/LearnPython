def remove_special_characters(input_string):
    # Define a list of special characters to remove
    special_characters = ['.', ',', "'", '"', '?', '!']

    # Remove spaces and convert to lowercase
    input_string = input_string.lower()

    # Remove special characters
    for char in special_characters:
        input_string = input_string.replace(char, '')

    return input_string


def is_palindrome(input_string):
   
    # Initialize variables for the forward and backward strings
    forward = input_string
    backward = ""

    # Reverse the string
    for char in input_string:
        backward = char + backward

    # Check if the string is equal to its reverse
    if len(forward) <= 1:
        return False
    else:
        return forward == backward

# Input text
words = """
Madam Arora taught us about the beauty palindromes. She said, 'A man, a plan, a canal, Panama!' with a smile. We marveled at words like 'radar,' 'level,' and 'deified,' each a symmetrical gem. Palindromes are fascinating because they read the same forwards and backwards. Racecar drivers, radar technicians, and civic leaders all appreciate their elegance. Some even argue that palindromes hold secret wisdom, like 'Evil is a name a foeman, as I live,' which is a poetic way to ponder the duality life. So, whether you're in a kayak, on a civic duty, or simply enjoying the serenity a palindrome, remember that linguistic marvels are all around us. This passage contains several palindromes, including words like madam A man, a plan, a canal, Panama," "radar," "level," "deified," "racecar," "civic," and "Evil is a name a foeman, as I live. These palindromes add a touch linguistic charm and symmetry to the text.
"""

found_palindromes = []

# Split the input text into words
word_list = words.split()

for word in word_list:
    word = remove_special_characters(word)
    if is_palindrome(word):
        found_palindromes.append(word)
        print(f"Found a palindrome '{word}'")

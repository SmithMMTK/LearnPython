def is_anagram(str1, str2):
    # Remove spaces and convert both strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the lengths of both strings are the same
    if len(str1) != len(str2):
        return False

    # Create a dictionary to count characters in str1
    char_count = {}

    # Count characters in str1
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Check if str2 has the same character count
    for char in str2:
        if char in char_count:
            char_count[char] -= 1
            if char_count[char] < 0:
                return False
        else:
            return False

    return True

# Example usage:

word1 = "listen"
word2 = "silent"
result = is_anagram(word1, word2)
print(f"'{word1}' and '{word2}' are anagrams: {result}")



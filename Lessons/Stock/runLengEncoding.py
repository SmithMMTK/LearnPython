def run_length_encoding(input_string):
    if not input_string:
        return ""

    compressed_string = ""
    count = 1

    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            compressed_string += input_string[i - 1] + str(count)
            count = 1

    compressed_string += input_string[-1] + str(count)

    return compressed_string

# Test the function
input_string = "abbbbcccccddddddde"
compressed_result = run_length_encoding(input_string)
print(compressed_result)

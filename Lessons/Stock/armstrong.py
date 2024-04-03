def is_armstrong(number):
    # Convert the number to a string to easily iterate over its digits
    digits = str(number)
    # Calculate the length of the number
    length = len(digits)
    
    # Initialize the sum of powers
    sum_of_powers = 0
    
    # Loop through each digit in the number
    for digit in digits:
        # Convert the digit back to an integer and raise it to the power of the number's length
        power = int(digit) ** length
        # Add the result to the sum of powers
        sum_of_powers += power
    
    # Check if the sum of the powers equals the original number
    return sum_of_powers == number

# Test the function

number = 153

#if is_armstrong(number):
#    print(f"{number} is an Armstrong number.")
#else:
#    print(f"{number} is not an Armstrong number.")

# Loop through a range of numbers to find Armstrong numbers
for i in range(1, 100000000):
    if is_armstrong(i):
        print(f"Found an Armstrong number: {i}")

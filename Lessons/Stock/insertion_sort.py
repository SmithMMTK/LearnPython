

import random
import sys

# Constants for text colors
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"

def colorize(text, color):
    return f"{color}{text}{RESET}"

def display(arr, i, j):
    # Display the array with elements highlighted in colors
    for k in range(len(arr)):
        if k == i:
            print(colorize(arr[k], RED), end=" ")
        elif k == j:
            print(colorize(arr[k], GREEN), end=" ")
        else:
            print(arr[k], end=" ")
    print()

def insertion_sort(arr):
    # Traverse through all elements in the array starting from the second element
    for i in range(1, len(arr)):
        # Current element to be compared
        current_element = arr[i]

        # Display the array with elements highlighted in colors
        print("\nPickup: ", current_element ," to compare with list.")
        display(arr, i, i )
        print("===")
        
        
        # Move elements of arr[0:i] that are greater than current_element
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and current_element < arr[j]:
            print("Compare ", current_element, " with ", arr[j], ".")
            arr[j + 1] = arr[j]
            print("*** Put ", arr[j], " to the right.")
            display(arr, j+1, j)
            
            j -= 1

        # Insert current_element into its correct position
        arr[j + 1] = current_element
        print("*** Put ", current_element, " to the position: ",j+1)
        display(arr, j+1, j+1)
        print("Move to next element.")
        print("===")
        input("")

# Example usage (same as before):
total_number = 10
my_list = random.sample(range(1, 100), total_number)

print("Original list:")
print(my_list)

input("\nPress Enter to start ...")

insertion_sort(my_list)

print("Sorting complete.")

print("Sorted list:")
print(my_list)
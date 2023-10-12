import random
import sys

# Constants for text colors
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"

def colorize(text, color):
    return f"{color}{text}{RESET}"

def display(arr, i, j, endposition):
    # Display the array with elements highlighted in colors
    for k in range(len(arr)):
        if k == i:
            print(colorize(arr[k], RED), end=" ")
        elif k == j:
            print(colorize(arr[k], GREEN), end=" ")
        elif k == endposition:
            print(colorize(arr[k], BLUE), end=" ")
        else:
            print(arr[k], end=" ")
    print()

def bubble_sort(arr):
    n = len(arr)

    print("\nStarting bubble sort...")

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            print("\nAt position: ",j," Compare ", arr[j], " with ", arr[j + 1], ".")
            display(arr, j, j + 1, n - i - 1)
            
            if arr[j] > arr[j + 1]:
                print("Swap ", arr[j], " with ", arr[j + 1], ".")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

            print("Result: ", end="")
            display(arr, j + 1, j, n - i - 1)
            input("Press Enter to continue...")

        print(f"Sorting pass #{i + 1} complete.")

        if not swapped:
            break

    print("Sorting complete.")
  
# Example usage (same as before):
total_number = 30
my_list = random.sample(range(1, 100), total_number)

print("\nOriginal list:")
print(my_list)

bubble_sort(my_list)

print("\nSorted list:")
print(my_list)

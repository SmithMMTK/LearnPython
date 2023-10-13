import random

# Constants for text colors
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"

def colorize(text, color):
    return f"{color}{text}{RESET}"

def display(arr, pivot_index, left, right):
    # Display the array with elements highlighted in colors
    for i in range(len(arr)):
        if i == pivot_index:
            print(colorize(arr[i], RED), end=" ")
        elif i == right:
            print(colorize(arr[i], GREEN), end=" ")
        elif i == left:
            print(colorize(arr[i], BLUE), end=" ")
        else:
            print(arr[i], end=" ")
    print()

def quick_sort(arr, low, high):
    if low < high:
        # Choose a pivot element (in this implementation, the last element)
        pivot_index = high
        pivot_value = arr[pivot_index]
        print("\nPivot_index: ", pivot_index, " Pivot_value: ", pivot_value)

        # Initialize the left and right pointers
        left = low
        right = high - 1
        print("Left: ", left, " Right: ", right)
        print(" Arr to be sorted: ")
        display(arr, pivot_index, left, right)
        # Partition the array
        while True:
            print("**********************")
            print("\nFind the elecment in left side array that higher than pivot_value : ",pivot_value)
            #print("Pivot_index: ", pivot_index, " Pivot_value: ", pivot_value)
            while left <= right and arr[left] < pivot_value:
                print("=====================")
                print("Left: ", left, " Right: ", right)
                print("Check If arr[left]: ", arr[left], " < pivot_value: ", pivot_value)
                print("arr[", arr[left],"] is in the right place because ",arr[left]," < ",pivot_value,)
                print("Move left pointer to the right.\n")
                left += 1
                print("result")
                display(arr, pivot_index, left, right)
                print("=====================")
                
            print("Yes i found the highest element in the left side the value is: ", arr[left]," and it is in the position: ", left)
           
            print("")
            print("\nFind the element in the right side array that lower than pivot_value : ",pivot_value)
            #print("Pivot_index: ", pivot_index, " Pivot_value: ", pivot_value)
            while left <= right and arr[right] > pivot_value:
                print("=====================")
                print("Left: ", left, " Right: ", right)
                print("Check If arr[right]: ", arr[right], " > pivot_value: ", pivot_value)
                print("arr[",arr[right],"] is in the right place because ",arr[right]," > ",pivot_value)
                print("Move right pointer to the left.\n")
                right -= 1
                print("result")
                display(arr, pivot_index, left, right)
                print("=====================")
               
            print("Yes i found the lowest element in the right side the value is: ", arr[right]," and it is in the position: ", right)

            if left <= right:
                print("=====================")
                print("Yes, left pointer is less than or equal to right pointer.")
                print("left = ", left, " right = ", right)
                # Swap the elements at left and right
                arr[left], arr[right] = arr[right], arr[left]
                print("Swap ", arr[left], " and ", arr[right])
                display(arr, pivot_index, left, right)
                left += 1
                right -= 1
                print("Move left pointer to the right and right pointer to the left.")
                display(arr, pivot_index, left, right)
                print("******************")
                
            else:
                break

        # Swap the pivot element with the element at left pointer
        arr[left], arr[pivot_index] = arr[pivot_index], arr[left]
        pivot_index = left

        # Recursively sort the sub-arrays
        print("\n ******** Recursively sort the sub-arrays from left to pivot_index - 1 ", left, " to ", pivot_index - 1)
        quick_sort(arr, low, pivot_index - 1)
        print("\n ******** Recursively sort the sub-arrays from pivot_index + 1 to right", pivot_index + 1, " to ", right)
        quick_sort(arr, pivot_index + 1, high)

# Example usage (same as before):
total_number = 10
my_list = random.sample(range(1, 100), total_number)

print("------------------------------------------------------------------------------------------------------------------")
print("Program start")
print("\nOriginal list:")
print(my_list)

#input("\nPress Enter to start ...")

quick_sort(my_list, 0, len(my_list) - 1)

print("Sorting complete.")

print("Sorted list:")
print(my_list)

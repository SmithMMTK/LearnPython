import random
import sys






def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):          
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
           break
  
# Example usage (same as before):
total_number = 10
my_list = random.sample(range(1, 100), total_number)
my_list = [1,2,3,4,5,6,7,8,9,10]

print("\nOriginal list:")
print(my_list)

bubble_sort(my_list)

print("\nSorted list:")
print(my_list)

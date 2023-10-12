import getch
import random

def display(arr, i, j, endposition):
    # Loop through all the elements of the array and hightlight Red text in element i and hightlight Green text in element j and hight light Blue text in element endposition
    for k in range(len(arr)):
        if k == i:
            print("\033[31m", arr[k], "\033[0m", end="")
        elif k == j:
            print("\033[32m", arr[k], "\033[0m", end="")
        elif k == endposition:
            print("\033[34m", arr[k], "\033[0m", end="")
        else:
            print(arr[k], end=" ")


def bubble_sort(arr):
    n = len(arr)
    print("Press any key to continue...")   

    for i in range(n):
        # Flag to optimize the algorithm by stopping early if no swaps are made in a pass
        swapped = False
        
        # to countdown the number of elements to be sorted from the end of the array toward to the beginning of the array
        debug_n_i_1 = n-i-1

        for j in range(0, n-i-1):
            # Display the array with the current element highlighted in Red and the next element highlighted in Green
            display(arr, j, j+1,n-i-1)
            print("Press any key to swap ...") 
            getch.getch()

            # Swap if the element found is greater than the next element
            debug_j = arr[j]
            debug_j_1 = arr[j+1]
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            
            display(arr, j+1, j,n-i-1)
            print()
            print()
            print("Press any key to continue...") 
            getch.getch()
            
            print()
        # If no two elements were swapped in the inner loop, the array is already sorted
        if not swapped:
            break

# Example usage:
total_number = 30
# Generate a list of random numbers between 1 and 100 of length total_number

my_list = random.sample(range(1, 100), total_number)

#my_list = [17, 54, 32, 88, 6, 42, 73, 91, 25, 69, 50, 12, 84, 98, 77, 3, 62, 19, 45, 95]
bubble_sort(my_list)
print("Result ...")   
print(my_list)

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Flag to optimize the algorithm by stopping early if no swaps are made in a pass
        swapped = False
        
        debug_n_i_1 = n-i-1

        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            debug_j = arr[j]
            debug_j_1 = arr[j+1]
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # If no two elements were swapped in the inner loop, the array is already sorted
        if not swapped:
            break

# Example usage:
my_list = [12, 5, 78, 32, 58, 67]
bubble_sort(my_list)
print(my_list)

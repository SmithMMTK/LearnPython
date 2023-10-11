def swap_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        return "Arrays must have the same length for swapping"
    
    for i in range(len(arr1)):
        temp = arr1[i]
        arr1[i] = arr2[i]
        arr2[i] = temp
    
    return arr1, arr2

# Example usage:
arr1 = [56, 23, 87, 41, 72, 9, 65]
arr2 = [33, 94, 12, 61, 78, 5, 37]

result_arr1, result_arr2 = swap_arrays(arr1, arr2)
print("Array 1 after swapping:", result_arr1)
print("Array 2 after swapping:", result_arr2)

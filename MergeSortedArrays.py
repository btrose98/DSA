'''
Merge Two Sorted Arrays: Write a function that takes two sorted arrays and merges them into a single sorted array.
'''


# O(m+n)
def merge_sorted_arrays(arr1, arr2):
    merged_array = []

    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:   # This will check arr2[j] > arr1[i] and arr1[i] == arr2[j]
            merged_array.append(arr2[j])
            j += 1

    # Add remaining elements from either list
    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1

    return merged_array


array_1 = [1, 2, 3, 4, 5]
array_2 = [3, 4, 5, 6, 7, 8, 9]
merged_and_sorted = merge_sorted_arrays(array_1, array_2)
print(merged_and_sorted)

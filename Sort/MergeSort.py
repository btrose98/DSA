"""
    Merge Sort:
    - follows the divide-and-conquer paradigm.
    - O(n log n), one of the most efficient sorting algorithms for general-purpose sorting.

    Steps:
    1. Divide:
        -divide the array into two halves recursively until each subarray contains only one element.

    2. Conquer (Sort):
        - sort each subarray individually

    3. Merge:
        - merge the sorted subarrays to produce the final sorted array
"""

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive call to further divide sub-arrays
        merge_sort(left_half)
        merge_sort(right_half)

        # Compare and sort left_half vs right_half elements
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy remaining left_half elements, if any
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy remaining right_half elements, if any
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

arr = [38, 27, 43, 9, 82, 10]
merge_sort(arr)
print(f"sorted array:   {arr}")
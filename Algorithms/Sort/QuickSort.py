"""
    Quick Sort:
    - follows the divide-and-conquer paradigm.
    - Average & Best = O(n log n), Worst = O(n^2).
    - In-place sorting, does not require additional memory space.
    - Adaptive, improves when input data is partially sorted.
    - Commonly used in sorting libraries and functions in programming languages like Python and Java.

    Steps:
    1. Choose a pivot:
        - Select a pivot from the array (various ways to do this: first, last, middle, or random element).

    2. Partitioning:
        - Rearrange elements of the array so that all elements < pivot are moved to its left, elements > pivot to its
            right.
        - At the end of this process, the pivot is in its final sorted position.
        - This partition process divides the array into 2 sub-arrays

    3. Recursion:
        - Recursively apply the same steps to the sub-arrays.
        - Each sub-array is sorted independently using the same process of selecting a pivot and partitioning.

    4. Combine:
        - As the recursion unwinds, the sorted sub-arrays are combined to produce the final sorted array.
"""


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # 1. Choose Pivot
    pivot = arr[len(arr) // 2]

    # 2. Partition
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # 3. Recursion  &   4. Combine
    return quick_sort(left) + middle + quick_sort(right)


test_arr = [3, 6, 8, 1, 10, 2, 1]
print(f"Sorted Array: {quick_sort(test_arr)}")

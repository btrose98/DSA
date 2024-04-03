'''
Find the Largest Element in an Array: Write a function to find the largest element in an array of integers.
'''


# O(n)
def find_largest_in_array(arr):
    if not arr:
        return None  # empty array

    largest = arr[0]

    for num in arr:
        if num > largest:
            largest = num

    return largest


my_array = [1, 2, 15, 3, -2, 9]
print(f"largest: {find_largest_in_array(my_array)}")

'''
Find the Largest Element in an Array: Write a function to find the largest element in an array of integers.
'''


# O(n)
def find_largest_in_array(arr):
    largest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest


my_array = [1, 2, 3, 4, 5]
print(f"largest: {find_largest_in_array(my_array)}")

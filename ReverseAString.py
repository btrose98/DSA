'''
Reverse a String: Write a function to reverse a string in-place (i.e., without using additional memory).
'''


# O(n/2) = O(n)
def reverse_a_string(s):
    s_list = list(s)

    left = 0
    right = len(s_list) - 1

    while left < right:
        temp = s_list[left]
        s_list[left] = s_list[right]
        s_list[right] = temp

        left += 1
        right -= 1

    reversed_s = "".join(s_list)

    return reversed_s

# O(n)
def reverse_a_string_recursive(s):
    if len(s) < 1:
        return s

    return s[-1] + reverse_a_string_recursive(s[:-1])


original_string = "reverse me"
reversed_string = reverse_a_string(original_string)
print(f"original string: {original_string} \nreversed string: {reversed_string}")

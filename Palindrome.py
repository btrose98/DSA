'''
Check for Palindrome: Write a function to determine if a given string is a palindrome (reads the same backward as
forward), ignoring spaces, punctuation, and capitalization.
'''

import re

# O(n/2) = O(n)
def is_palindrome(s):
    s_cleaned = re.sub('[^A-Za-z0-9]+', '', s)

    s_list = list(s_cleaned)

    left = 0
    right = len(s_list) - 1

    while left < right:
        if s_list[left] != s_list[right]:
            return False
        left += 1
        right -= 1
    return True


possible_palindrome = "race car"
if is_palindrome(possible_palindrome):
    print(f"{possible_palindrome} is indeed a palindrome")
else:
    print(f"{possible_palindrome} is NOT a palindrome")

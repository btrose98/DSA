'''
Anagram Check: Write a function to determine if two strings are anagrams of each other (contain the same characters in
a different order).
'''

import re


def is_anagram(s1, s2):
    s1_cleaned = s1.replace(" ", "").lower()
    s2_cleaned = s2.replace(" ", "").lower()

    return sorted(s1_cleaned) == sorted(s2_cleaned)

    # s1_list = list(s1_cleaned)
    # s2_list = list(s2_cleaned)
    #
    # for i in s1_list:
    #     for j in s2_list:
    #         if i == j:
    #             s1_list.remove(i)
    #             s2_list.remove(j)
    #
    # return len(s1_list) == 0 and len(s2_list) == 0


a1 = "a gentleman"
a2 = "elegant man"
if is_anagram(a1, a2):
    print(f"\'{a1}\' and \'{a2}\' is indeed an anagram.")
else:
    print(f"\'{a1}\' and \'{a2}\' is NOT an anagram.")

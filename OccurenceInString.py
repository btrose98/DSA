'''
Count the Occurrences of a Character in a String: Write a function that takes a string and a character as input and
returns the number of times the character appears in the string.
'''


# O(n)
def count_occurences(s, target_letter):
    count = 0
    for letter in s:
        if letter == target_letter:
            count += 1
    return count


my_string = "this is my string"
occurence_spotlight = "t"
n = count_occurences(my_string, occurence_spotlight)
print(f"\'{occurence_spotlight}\' occurs in \'{my_string}\': {n} times")

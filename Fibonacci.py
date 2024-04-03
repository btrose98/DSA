'''
Fibonacci Sequence: Write a function to generate the Fibonacci sequence up to a specified number of terms.

 Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting
 with 0 and 1. The sequence begins: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so on.
'''


# O(n)
def fibonacci_sequence(n):
    fib_list = [0, 1]
    for i in range(2, n):
        next_fib = fib_list[i - 1] + fib_list[i - 2]
        fib_list.append(next_fib)

    return fib_list


num_terms = 12
print(fibonacci_sequence(num_terms))

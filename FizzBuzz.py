'''
Write a program that prints the numbers from 1 to 100. But for multiples of three, print "Fizz" instead of the number,
and for the multiples of five, print "Buzz". For numbers that are multiples of both three and five, print "FizzBuzz".
'''


# Optimized
def fizzbuzz(n):
    for i in range(1, n):
        output = ""

        if i % 3 == 0:
            output += "Fizz"

        if i % 5 == 0:
            output += "Buzz"

        if not output:
            output = i

        print(output)


def fizzbuzz_not_optimized(n):
    for i in range(1, n):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz(100)
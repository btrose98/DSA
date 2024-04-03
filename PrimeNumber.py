'''
Prime Number Check: Write a function to check if a given integer is a prime number.

Prime Number = a whole number greater than 1 that cannot be exactly divided by any whole number other than itself and 1
 (e.g. 2, 3, 5, 7, 11).
'''


'''
any factor of n larger than its square root would necessarily have a corresponding factor smaller than the square root, 
and thus we only need to check up to the square root of n for factors
'''
def is_prime_number(n):
    if n <= 1:
        return False

    # This searches for i in range(2, sqrt(n))
    for i in range(2, int(n ** 0.5)):
        if n % i == 0:
            return False

    return True


def is_prime_number_not_optimized(n):
    if n <= 1:
        return False

    for i in range(2, n - 1):
        if n % i == 0:
            return False

    return True


number = 13
if is_prime_number(number):
    print(f"{number} is a prime #")
else:
    print(f"{number} is NOT a prime #")

from mpmath import *
import gmpy2
from gmpy2 import mpz
import math

from decimal import *


def main():

    x = [7, 6, 21]
    # print("output", last_digit(x))
    print(try_hard(7, 21936950640377856))


def last_digit(n):

    e = mpz(n[-1])

    for i in range(2, len(n) + 1, 1):
        loc = len(n) - i
        x = mpz(n[loc])
        e = try_hard(x, e)

    return e


def try_hard(n, e):

    powers = get_powers(e)

    result = 1

    for power in powers:
        if power != 1:
            temp_result = n
            x = 1
            while x < power:
                x *= 2
                temp_result = temp_result ** 2
            result *= temp_result
        else:
            result *= n

    return result


def exp_by_bin(a, n):

    n_bin = "{0:b}".format(n)
    print(n_bin)
    result = a

    for i in range(1, len(n_bin), 1):

        print(i, len(str(result)))

        if n_bin[i] == "0":
            result = result * result

        else:
            result = a * (result * result)

    return result


def get_powers(n):

    n_bin = "{0:b}".format(n)

    result = []

    for i in range(0, len(n_bin), 1):
        x = len(n_bin) - i - 1
        if n_bin[i] != "0":
            result.append((2 * int(n_bin[i])) ** x)

    return result


def split_exp(n, e):

    if e < 100:
        return pow(n, e)
    else:

        split = find_split(e)

        iterations = mpz(split[0])
        remainder = mpz(split[1])
        bucket = mpz(split[2])

        result = mpz(1)

        for i in range(0, iterations, 1):
            result *= pow(n, bucket)

        if remainder != 0:
            result *= pow(n, remainder)

        return result


def find_split(n):

    if n >= 10000000:
        return math.floor(n / 10000000), n % 10000000, 10000000
    if n >= 1000000:
        return math.floor(n / 1000000), n % 1000000, 1000000
    elif n >= 100000:
        return math.floor(n / 100000), n % 100000, 100000
    elif n >= 10000:
        return math.floor(n / 10000), n % 10000, 10000
    elif n >= 1000:
        return math.floor(n / 1000), n % 1000, 1000
    elif n >= 100:
        return math.floor(n / 100), n % 100, 100
    else:
        return None, None, None


def is_even(n):

    return float(n) % 2 == 0


if __name__ == "__main__":
    main()

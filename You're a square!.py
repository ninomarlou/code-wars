import math


def main():

    x = 26
    y = 1103735

    print(is_square(x))


def is_square(n):

    if n < 0:
        return False
    else:

        return math.sqrt(n).is_integer()


if __name__ == "__main__":
    main()

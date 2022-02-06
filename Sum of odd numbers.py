import math


def main():

    x = 1
    y = 1103735

    print(row_sum_odd_numbers(x))


def row_sum_odd_numbers(n):

    running_n = 0

    for i in range(1, n + 1, 1):
        i_increment = 0
        result = 0
        while i_increment < i:
            is_odd = 0
            while is_odd == 0:
                running_n += 1
                if running_n % 2 != 0:
                    result += running_n
                    is_odd = 1
            i_increment += 1
            
    return result


if __name__ == "__main__":
    main()

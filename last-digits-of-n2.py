import datetime
import numpy as np
import math


def main():
    x1 = 12
    start_time = datetime.datetime.now()
    # a1 = green(x1)
    end_time = datetime.datetime.now()
    time_diff = (end_time - start_time)
    execution_time = time_diff.total_seconds() * 1000
    # print(a1, execution_time)
    test()


def green(n):
    results = []
    for i in range(0, 1110000000, 10):
        if filter_function(i) and i != 0:
            results.append(i)
        if filter_function(i + 1):
            results.append(i + 1)
        if filter_function(i + 4):
            results.append(i + 4)
        if filter_function(i + 5):
            results.append(i + 5)
        if filter_function(i + 6):
            results.append(i + 6)
        if filter_function(i + 9):
            results.append(i + 9)

    last = 0
    for result in results:
        print(result)
        last = result


def filter_function(n):
    nsqr = n ** 2
    last_digit = get_list_digits(nsqr, math_len(n))
    return n == last_digit


def get_list_digits(n, len):
    return n % get_x(len)


def get_x(n):
    return 1 * (10 ** n)


def math_len(n):
    return math.ceil(math.log10(n + 1))


def test():
    t1 = []
    #t1.append(5)
    #t1.append(6)
    #t1.append(25)
    #t1.append(76)
    #t1.append(376)
    #t1.append(625)
    #t1.append(9376)
    t1.append(90625)
    t1.append(109376)
    t1.append(890625)
    t1.append(2890625)
    t1.append(7109376)
    t1.append(12890625)
    t1.append(87109376)

    result=[]
    for e in t1:
        str_e=str(e)
        result.append(str_e[-5])
    print(result)


if __name__ == '__main__':
    main()

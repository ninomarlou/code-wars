def main():

    x = [160, 3, 1719, 19, 11, 13, -21]
    y = 1103735

    print(find_outlier(x))


def find_outlier(integers):

    is_even = 0
    is_odd = 0

    for i in integers:
        if i % 2 == 0:
            # is even
            is_even += 1
            if is_even == 1 and is_odd > 1:
                return i

        else:
            # is odd
            is_odd += 1
            if is_odd == 1 and is_even > 1:
                return i

    # if this is reached, the first element was the unique one

    return integers[0]

    # return result


if __name__ == "__main__":
    main()

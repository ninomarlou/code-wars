def main():

    x = 9119
    y = 1103735

    print(square_digits(x))


def square_digits(num):

    s_num = str(num)
    result = ''

    for d in s_num:
        result += str(int(d) ** 2)

    return int(result)


if __name__ == "__main__":
    main()

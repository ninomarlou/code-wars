def main():

    input = 4
    input1 = 1

    print(persistence(input))


def persistence(n):

    if n < 10:
        return 0

    result = 0
    init_d = 1
    flag = 0

    while flag == 0:

        for d in str(n):
            init_d = init_d * int(d)

        n = init_d
        init_d = 1

        result += 1

        if n < 10:
            flag = 1

    return result


if __name__ == "__main__":
    main()

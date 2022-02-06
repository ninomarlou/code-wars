def main():

    x = "AAAABBBCCDAABBB"
    y = 1103735

    print(unique_in_order(x))


def unique_in_order(iterable):

    result = []

    result.append(iterable[0])

    for i in range(1, len(iterable), 1):
        if iterable[i - 1] != iterable[i]:
            result.append(iterable[i])

    return result


if __name__ == "__main__":
    main()

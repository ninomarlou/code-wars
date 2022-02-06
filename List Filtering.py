def main():

    input = [1, "a", "b", 0, 15]
    input1 = 1

    print(filter_list(input))


def filter_list(l):

    result = []

    for x in l:
        if type(x)==int:
            result.append(x)

    return result


if __name__ == "__main__":
    main()

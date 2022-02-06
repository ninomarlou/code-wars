import snail

def main():

    input = 1
    input1 = 1

    print(add_binary(input, input1))


def add_binary(a, b):

    return "{0:b}".format(a + b)


if __name__ == "__main__":
    main()

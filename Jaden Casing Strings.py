def main():

    input = "How can mirrors be real if our eyes aren't real"
    input1 = 1

    print(to_jaden_case(input))


def to_jaden_case(string):

    result = string[0].upper()

    for i in range(1, len(string), 1):
        if string[i - 1] == " ":
            result += string[i].upper()
        else:
            result += string[i]

    return result


if __name__ == "__main__":
    main()

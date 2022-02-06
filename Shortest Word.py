def main():

    input = "bitcoin take over the world maybe who knows perhaps"
    input1 = 1

    print(find_short(input))


def find_short(s):

    result = 1000
    words = s.split()

    for word in words:
        if len(word) <= result:
            result = len(word)

    return result


if __name__ == "__main__":
    main()

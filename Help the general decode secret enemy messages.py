def main():

    s1 = "cccc"
    s2 = "bdhpF"

    a1 = encode(s1)

    print(a1)


def encode(s):

    valArr = ""
    result = ""

    maxOffset = 0
    for letter in s:
        offSet = get_value_index(letter)
        if offSet > maxOffset:
            maxOffset = offSet

    valLen = len(s) + 1

    for i in range(0, valLen, 1):

        valArr += decode_small_letter(i)

    for i in range(0, len(s), 1):
        finalOffset = get_value_index(s[i])
        result += valArr[i + finalOffset]

    return result


def decode_small_letter(index_in_word):

    index_in_word += 1
    value_index = (2 ** index_in_word) - 1

    return get_index_value(value_index)


def get_value_index(value):
    letters = "abcdefghijklmnopqrstuvwxyz"
    letters = letters + letters.upper()

    for i in range(0, len(letters), 1):
        if value == letters[i]:
            return i


def get_index_value(value_index):

    letters = "abcdefghijklmnopqrstuvwxyz"
    letters = letters + letters.upper()
    return letters[value_index]


if __name__ == "__main__":
    main()

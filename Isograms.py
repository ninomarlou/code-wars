def main():

    x = "moOse"
    y = 1103735

    print(is_isogram(x))


def is_isogram(string):

    word = string.lower()
    result = ''
    char_dict = {}

    for c in word:

        curr_char_count = char_dict.get(c)

        if curr_char_count is None:
            curr_char_count = 1
        else:
            curr_char_count += 1

        if curr_char_count > 1:
            return False

        char_dict[c] = curr_char_count

    return True


if __name__ == "__main__":
    main()

def main():

    x = "(( @"
    y = 1103735

    print(duplicate_encode(x))


def duplicate_encode(word):

    word = word.lower()
    result = ""
    char_dict = {}

    for c in word:

        curr_char_count = char_dict.get(c)

        if curr_char_count is None:
            curr_char_count = 1
        else:
            curr_char_count += 1

        char_dict[c] = curr_char_count

    for c in word:
        char_count = char_dict.get(c)
        if char_count == 1:
            result += "("
        else:
            result += ")"

    return result


if __name__ == "__main__":
    main()

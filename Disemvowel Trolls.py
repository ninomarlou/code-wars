def main():

    input = "This website is for losers LOL!"
    input1 = 1

    print(disemvowel(input))


def disemvowel(string_):

    temp_string = ""
    vowels = ["a", "e", "i", "o", "u"]

    for c in string_:
        if c.lower() not in vowels:
            temp_string += c

    string_ = temp_string

    return string_


if __name__ == "__main__":
    main()

def main():

    input = "aaaxbbbbyyhwawiwjjjwwm"
    input1 = 1

    print(printer_error(input))


def printer_error(s):

    valid_colours = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
    denom = str(len(s))
    num = 0

    for i in range(len(s)):
        if s[i] not in valid_colours:
            num += 1

    return str(num) + "/" + denom


if __name__ == "__main__":
    main()

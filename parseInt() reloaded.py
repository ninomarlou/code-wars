def main():

    input = 1
    input1 = 1

    print(parse_int(input))


def parse_int(string):

    n = str(string)
    result = ""
    places = []
    temp_places = ""

    for c in n:
        temp_places += c
        if len(temp_places) == 3:
            places.append(temp_places)
            temp_places = ""

    if temp_places != "":
        places.append(temp_places)

    places_count = len(places)

    for i in range(0, places_count, 1):
        result += parse_hundred(places[i])
        if places_count - i == 2:
            result += " thousand "
        if places_count - i == 3:
            result += " million "

    return result


def parse_hundred(s):
    
    print(int(s))

    n = str(int(s))
    if len(n) == 1:
        n = "00" + n
    elif len(n) == 2:
        n = "0" + n

    result = ""
    if n[0] != "0":
        if n[1:] != "00":
            result += parse_below_twenty(n[0]) + " hundred "
        else:
            result += parse_below_twenty(n[0]) + " hundred"

    if int(n[1:]) < 20:
        result += parse_below_twenty(n[1:])
    else:
        result += parse_above_twenty(n[1])
        if n[-1] != "0":
            result += "-" + parse_below_twenty(n[-1])

    return result


def parse_above_twenty(s):
    if s == "9":
        return "ninty"
    elif s == "8":
        return "eighty"
    elif s == "7":
        return "seventy"
    elif s == "6":
        return "sixty"
    elif s == "5":
        return "fifty"
    elif s == "4":
        return "forty"
    elif s == "3":
        return "thirty"
    elif s == "2":
        return "twenty"
    else:
        return ""


def parse_below_twenty(s):
    n = int(s)
    if n == 1:
        return "one"
    elif n == 2:
        return "two"
    elif n == 3:
        return "three"
    elif n == 4:
        return "four"
    elif n == 5:
        return "five"
    elif n == 6:
        return "six"
    elif n == 7:
        return "seven"
    elif n == 8:
        return "eight"
    elif n == 9:
        return "nine"
    elif n == 10:
        return "ten"
    elif n == 11:
        return "eleven"
    elif n == 12:
        return "twelve"
    elif n == 13:
        return "thirteen"
    elif n == 14:
        return "fourteen"
    elif n == 15:
        return "fifteen"
    elif n == 16:
        return "sixteen"
    elif n == 17:
        return "seventeen"
    elif n == 18:
        return "eighteen"
    elif n == 19:
        return "nineteen"
    else:
        return ""


if __name__ == "__main__":
    main()

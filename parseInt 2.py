def main():

    input = "ten thousand three hundred"
    input1 = 1

    # print(parse_word(input))

    print(parse_int(input))


def parse_int(string):

    string = string.replace("-", " ").replace(" and ", " ").lower()
    chunks = {"million": "000000", "thousand": "000", "hundred": "00"}
    result = ""
    last_part = ""

    words_array = string.split()
    if words_array[-1] in chunks:
        words = words_array[:-1]
    else:
        words = words_array

    temp_result = ""

    for word in words:
        if word not in chunks:
            parsed_word = parse_word(word)
            temp_result = remove_padding(temp_result, len(parsed_word))
            temp_result += parsed_word
            last_part = ""
        else:
            temp_result += chunks.get(word)
            if last_part != "chunk":
                result = remove_padding(result, len(temp_result))
            result += temp_result
            temp_result = ""
            last_part = "chunk"

    if temp_result != "":
        if last_part != "chunk":
            result = remove_padding(result, len(temp_result))
        result += temp_result

    if words_array[-1] in chunks:
        additional_word = result[-1] + chunks.get(words_array[-1])
        if len(result) > len(additional_word):
            result = result[: len(additional_word)] + additional_word
        else:
            result += chunks.get(words_array[-1])

    if result == "zero":
        return 0
    else:
        return int(result)


def remove_padding(string, n):
    reversed_string = string[::-1]
    flag = 0
    counter = 0
    result = ""
    for l in reversed_string:
        if l != "0" or counter == n:
            flag = 1
        else:
            counter += 1
        if flag != 0:
            result += l

    return result[::-1]


def parse_word(string):

    if string == "one":
        return "1"
    elif string == "two":
        return "2"
    elif string == "three":
        return "3"
    elif string == "four":
        return "4"
    elif string == "five":
        return "5"
    elif string == "six":
        return "6"
    elif string == "seven":
        return "7"
    elif string == "eight":
        return "8"
    elif string == "nine":
        return "9"
    elif string == "ten":
        return "10"
    elif string == "eleven":
        return "11"
    elif string == "twelve":
        return "12"
    elif string == "thirteen":
        return "13"
    elif string == "fourteen":
        return "14"
    elif string == "fifteen":
        return "15"
    elif string == "sixteen":
        return "16"
    elif string == "seventeen":
        return "17"
    elif string == "eighteen":
        return "18"
    elif string == "nineteen":
        return "19"
    elif string == "twenty":
        return "20"
    elif string == "thirty":
        return "30"
    elif string == "forty":
        return "40"
    elif string == "fifty":
        return "50"
    elif string == "sixty":
        return "60"
    elif string == "seventy":
        return "70"
    elif string == "eighty":
        return "80"
    elif string == "ninety":
        return "90"
    else:
        return "zero"


if __name__ == "__main__":
    main()

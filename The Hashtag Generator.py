def main():

    input = "Codewars Is Nice"
    input1 = 1

    print(generate_hashtag(input))


def generate_hashtag(s):

    result = "#"

    for i in range(0, len(s), 1):   
        if s[i] != " ":
            if s[i - 1] == " " or len(result) == 1:
                result += s[i].upper()
            else:
                result += s[i].lower()

    if len(result) > 140 or len(result) == 1:
        return False
    else:
        return result


if __name__ == "__main__":
    main()

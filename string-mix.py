import string


def main():

    x1 = "looping is fun but dangerous"
    x2 = "less dangerous than coding"

    x3 = mix(x1, x2)

    print(x3)


def mix(s1, s2):

    s1 = clean(s1)
    s2 = clean(s2)
    s3 = list(set(s1 + s2))

    s1_letter_counts = {}
    s2_letter_counts = {}

    for letter in s1:
        s1_letter_counts[letter] = s1_letter_counts.get(letter, 0) + 1

    for letter in s2:
        s2_letter_counts[letter] = s2_letter_counts.get(letter, 0) + 1

    temp = {}
    max_count = 0

    for letter in s3:
        s1_count = s1_letter_counts.get(letter, 0)
        s2_count = s2_letter_counts.get(letter, 0)
        if max(s1_count, s2_count) > max_count:
            max_count = max(s1_count, s2_count)
        if s1_count == s2_count and s1_count > 1:
            curr_val = temp.get(s1_count)
            if curr_val:
                curr_val.append(letter + "0")
                temp[s1_count] = curr_val
            else:
                temp[s1_count] = [letter + "0"]

        else:
            if s1_count > 1:
                curr_val = temp.get(s1_count)
                if curr_val:
                    curr_val.append(letter + "1")
                    temp[s1_count] = curr_val
                else:
                    temp[s1_count] = [letter + "1"]
            if s2_count > 1:
                curr_val = temp.get(s2_count)
                if curr_val:
                    curr_val.append(letter + "2")
                    temp[s2_count] = curr_val
                else:
                    temp[s2_count] = [letter + "2"]

    found_letter = []
    result = ""

    for i in range(max_count, -1, -1):
        print(i)
        val = temp.get(i)
        print("   ", val)
        if val:
            val.sort()
            s1_list = []
            s2_list = []
            s0_list = []
            for item in val:
                if item[1:] == "1":
                    s1_list.append(item[0])
                if item[1:] == "2":
                    s2_list.append(item[0])
                if item[1:] == "0":
                    s0_list.append(item[0])
            for letter in s1_list:
                if letter not in found_letter:
                    result += "1:" + letter * i + "/"
                    found_letter.append(letter)
            for letter in s2_list:
                if letter not in found_letter:
                    result += "2:" + letter * i + "/"
                    found_letter.append(letter)
            for letter in s0_list:
                if letter not in found_letter:
                    result += "=:" + letter * i + "/"
                    found_letter.append(letter)

    return result[:-1]


def clean(s):

    result = ""

    for letter in s:
        if letter.isalpha() and letter.islower():
            result += letter

    return result


if __name__ == "__main__":
    main()

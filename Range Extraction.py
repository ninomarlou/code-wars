def main():

    input = [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
    input1 = 1

    print(solution(input))


def solution(args):

    result = ""
    ranges = []
    temp_range = []

    for i in range(0, len(args), 1):
        if i == 0:
            temp_range.append(args[i])
        else:
            if args[i - 1] + 1 == args[i]:
                temp_range.append(args[i])
            else:
                ranges.append(temp_range)
                temp_range = [args[i]]
    ranges.append(temp_range)

    for rang in ranges:
        if len(rang) < 3:
            for e in rang:
                result += str(e) + ","
        else:
            result += str(rang[0]) + "-" + str(rang[-1]) + ","

    return result[0:-1]


if __name__ == "__main__":
    main()

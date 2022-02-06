import math


def main():

    x = "abcdef"
    y = 1103735

    print(solution(x))


def solution(s):

    result = []

    if len(s) % 2 != 0:
        s += '_'

    for i in range(0, len(s), 2):
        result.append(s[i : i + 2])

    return result


if __name__ == "__main__":
    main()

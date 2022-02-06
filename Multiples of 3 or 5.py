def main():

    x = 10
    y = 1103735

    print(solution(x))


def solution(number):

    if number < 0:
        return 0
    result = 0

    for i in range(1, number, 1):
        if i % 3 == 0 or i % 5 == 0:
            result += i

    return result


if __name__ == "__main__":
    main()

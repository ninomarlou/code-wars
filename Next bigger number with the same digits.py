import time
import itertools


def main():
    input = 89609458552932
    input1 = 1

    start = time.time()

    print(next_bigger(input))

    end = time.time()
    print(end - start)


def next_bigger(n):
    stri = list(str(n))
    length = len(stri)
    indeces = []
    for i in range(0, length, 1):
        indeces.append(i)

    data = [[[indeces[0]], indeces[1:]]]

    counter = 0

    while counter <= length:
        for d in data:
            temp_data = []
            left = d[0]
            right = d[1]
            limit = int(''.join(stri[:len(left) + 1]))
            for e in right:
                x = right.copy()
                y = left.copy()
                y.append(e)
                if translate(stri, y) >= limit:
                    x.remove(e)
                    temp_data.append([y, x])
                    print(left, e, y, translate(stri, y), limit)

        if len(temp_data) != 0:
            data = temp_data

        counter += 1

    for e in data:
        print(e[0], translate(stri, e[0]))


def translate(arr, indeces):
    result = ""
    for i in indeces:
        result += arr[i]

    return int(result)

    # for i in range()


def filtered_permutations(iterable, length, limit):
    for item in itertools.permutations(iterable, length):
        if int("".join(item)) > limit:
            yield "".join(item)


# 14.574883699417114


if __name__ == "__main__":
    main()

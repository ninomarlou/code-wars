import numpy as np


def main():

    x1 = 59884848459853
    #    59884848483559
    #    59884848483559
    print(next_bigger(x1))


def next_bigger(n):

    n = str(n)

    if len(n) == 1:
        return -1

    last_digit = n[-1]
    split_loc = None

    for i in range(len(n) - 2, -1, -1):
        if int(n[i]) < int(last_digit):
            split_loc = i
            break
        last_digit = n[i]

    if split_loc == None:
        return -1

    left = n[:split_loc]
    right = n[split_loc:]

    print(left, right)

    right_p1 = right[0]
    right_p2 = sorted(right[1:])

    for i in range(int(right_p1) + 1, 10, 1):
        for j in range(0, len(right_p2), 1):
            if i == int(right_p2[j]):
                right_p2[j] = right_p1
                right_p1 = str(i)
                break
        else:
            continue
        break

    result = left + right_p1 + "".join(right_p2)

    if len(str(int(result))) == len(n):
        return int(result)
    else:
        return -1


if __name__ == "__main__":
    main()

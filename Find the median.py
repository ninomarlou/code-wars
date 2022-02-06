import math


def main():

    x = [33,99,100,30,29,50]
    y = 1103735

    print(median(x))


def median(array):

    array.sort()
    mid = int(len(array) / 2)

    if len(array) % 2 == 0:
        return (array[mid] + array[mid - 1]) / 2
    else:
        return array[mid]


if __name__ == "__main__":
    main()

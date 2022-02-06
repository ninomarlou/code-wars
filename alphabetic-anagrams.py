import itertools
import time
from collections import OrderedDict as od

import numpy as np


def main():
    x1 = 'bookkeeper'
    start_time = time.time()
    a1 = listPosition(x1)
    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_time_milliSeconds = elapsed_time * 1000

    print(elapsed_time_milliSeconds, a1)


def listPosition(word):
    word_array = []
    for letter in list(word):
        word_array.append(getLetterIndex(letter))

    check_value = tuple(word_array)
    np_word_array = sorted(word_array)

    lst1 = itertools.permutations(np_word_array, len(word))
    counter=0
    for i1 in range(0,25,1):
        for i2 in range(0, 25, 1):
            for i3 in range(0, 25, 1):
                for i4 in range(0, 25, 1):
                    for i5 in range(0, 25, 1):
                        for i6 in range(0, 25, 1):
                            for i7 in range(0, 25, 1):
                                for i8 in range(0, 25, 1):
                                    for i9 in range(0, 25, 1):
                                        for i10 in range(0, 25, 1):
                                            counter+=1

    return 1


def score(lst):
    score = 0
    for i in range(0, len(lst), 1):
        score += (i + 1) * lst[i]

    return score


def getLetterIndex(letter):
    letters_list = list('abcdefghijklmnopqrstuvwxyz')
    small_letter = letter.lower()
    for i in range(0, len(letters_list), 1):
        if small_letter == letters_list[i]:
            return i
    return -1


if __name__ == "__main__":
    main()

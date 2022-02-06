def main():

    input = [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]
    input1 = 1

    print(move_zeros(input))


def move_zeros(array):
 
    array_len = len(array)
    i = 0
    j = 0

    while i < array_len:
        print(array[i])
        if array[j] == 0:
            array.pop(j)
            array.append(0)
        else:
            j += 1
        i += 1

    return array


if __name__ == "__main__":
    main()

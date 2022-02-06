def main():

    input = 209917
    input1 = 1

    print(smallest(input))


def smallest(n):

    str_n = list(str(n))
    smallest_n = [n, 0, 0]
    for i in range(0, len(str_n), 1):
        temp_str_n = str_n.copy()
        d = temp_str_n[i]
        temp_str_n.pop(i)
        for j in range(0, len(str_n), 1):
            new_str_n = temp_str_n.copy()
            new_str_n.insert(j, d)
            new_n = arr_to_int(new_str_n)
            if new_n < smallest_n[0]:
                smallest_n = [new_n, i, j]

    return smallest_n


def arr_to_int(arr):
    
    result = ""

    for e in arr:
        result += e

    return int(result)


if __name__ == "__main__":
    main()

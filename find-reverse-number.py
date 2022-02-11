import itertools


def main():
    x1 = 100000000000
    x2 = [1, 2, 3]
    a1 = find_reverse_number(x1)
    # x=generate_list(1)
    # print(x)


def find_reverse_number(n):

    count = 0
    iter_loc = 1
    while count < n:
        if iter_loc == 1:
            init_len = 10
        else:
            init_len = 9
        add_len = 10
        if iter_loc % 2 == 0:
            limit = int(iter_loc/2)
        else:
            limit = int(iter_loc/2)+1
        for i in range(0, limit-1, 1):
            init_len *= add_len
        if count+init_len >= n:
            #count += init_len
            break
        else:
            count += init_len
            iter_loc += 1

    lst = generate_list(iter_loc)

    print(lst[n-count-1])


def generate_list(arr_len):
    if arr_len == 1:
        return [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]

    base = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    base_list = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]

    if arr_len % 2 == 0:
        limit = int(arr_len/2)
    else:
        limit = int(arr_len/2)+1
    result_len = 9
    for i in range(0, limit-1, 1):
        base_list.append(base)
        result_len *= len(base)

    results = map(mirror, [arr_len]*result_len, itertools.product(*base_list))

    return list(results)


def mirror(arr_len, lst):
    lst = list(lst)
    if arr_len % 2 == 0:
        return lst+list(reversed(lst))
        # print('-->',lst+list(reversed(lst)))
    else:
        return lst+list(reversed(lst[:-1]))
        # print('-->',lst+list(reversed(lst[:-1])))


if __name__ == '__main__':
    main()

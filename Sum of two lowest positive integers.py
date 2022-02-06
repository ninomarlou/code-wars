def main():

    input = [19, 5, 42, 2, 77]
    input1 = 1

    print(sum_two_smallest_numbers(input))


def sum_two_smallest_numbers(numbers):

    sorted_nunbers = sorted(numbers)
    return sorted_nunbers[0] + sorted_nunbers[1]


if __name__ == "__main__":
    main()

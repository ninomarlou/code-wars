from itertools import product


def main():

    input = "369"
    input1 = 1

    print(get_pins(input))


def get_pins(observed):

    adj = {}
    adj["1"] = ["1", "2", "4"]
    adj["2"] = ["1", "2", "3", "5"]
    adj["3"] = ["2", "3", "6"]
    adj["4"] = ["1", "4", "5", "7"]
    adj["5"] = ["2", "4", "5", "6", "8"]
    adj["6"] = ["3", "5", "6", "9"]
    adj["7"] = ["4", "7", "8"]
    adj["8"] = ["5", "7", "8", "9", "0"]
    adj["9"] = ["6", "8", "9"]
    adj["0"] = ["0", "8"]

    pins = list(observed)

    digit_list = []

    for pin in pins:
        digit_list.append(adj.get(pin))

    init_results = digit_list[0]

    for i in range(1, len(digit_list), 1):
        init_results = product(init_results, digit_list[i])
        temp = []
        for item in init_results:
            temp.append("".join(item))
        init_results = temp

    result = []

    for item in init_results:
        result.append(item)

    return result


if __name__ == "__main__":
    main()

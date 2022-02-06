import math


def main():

    x = [1, 2, 5, 4, 3, 2, 3, 6, 4, 1, 2, 3, 3, 4, 5, 3, 2, 1, 2, 3, 5, 5, 4, 3]
    y = 0.7
    z = 83.9598760937531

    print(pick_peaks(x))


def pick_peaks(arr):

    pos = []
    peaks = []
    result = {}
    curr_i = 1
    status = 0

    for i in range(1, len(arr) - 1, 1):
        before = arr[i - 1]
        after = arr[i + 1]
        current = arr[i]

        if current > before and status == 0:
            status = 1
        elif current < before and status == 1:
            status = 0

        if before <= current and current > after and status == 1:
            pos.append(curr_i)
            peaks.append(arr[i])

        if arr[i] != arr[i + 1]:
            curr_i = i + 1

    result["pos"] = pos
    result["peaks"] = peaks

    return result


if __name__ == "__main__":
    main()

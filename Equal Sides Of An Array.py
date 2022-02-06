def main():

    input = [1,100,50,-51,1,1]
    input1 = 1

    print(find_even_index(input))


def find_even_index(arr):

    for i in range(0, len(arr), 1):
        if sum(arr[0:i]) == sum(arr[i + 1 : len(arr)]):
            return i
            
    return -1


if __name__ == "__main__":
    main()

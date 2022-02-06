def main():

    input = "a234"
    input1 = 1

    print(validate_pin(input))


def validate_pin(pin):

    if len(pin) == 4 or len(pin) == 6:
        for i in range(0, len(pin), 1):
            if pin[i].isdigit() == False:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()

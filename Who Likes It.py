def main():

    input = ["Alex", "Jacob", "Mark", "Max"]

    print(likes(input))


def likes(names):
    liker_count = len(names)
    if liker_count == 0:
        return "no one likes this"
    elif liker_count == 1:
        return names[0] + " likes this"
    elif liker_count == 2:
        return names[0] + " and " + names[1] + " like this"
    elif liker_count == 3:
        return names[0] + ", " + names[1] + " and " + names[2] + " like this"
    else:
        return (
            names[0]
            + ", "
            + names[1]
            + " and "
            + str(liker_count - 2)
            + " others like this"
        )


if __name__ == "__main__":
    main()

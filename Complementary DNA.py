def main():

    input = "ATGC"
    input1 = 1

    print(DNA_strand(input))


def DNA_strand(dna):
    result = ""
    dict = {}
    dict["A"] = "T"
    dict["T"] = "A"
    dict["G"] = "C"
    dict["C"] = "G"

    for c in dna:
        result += dict.get(c)

    return result


if __name__ == "__main__":
    main()

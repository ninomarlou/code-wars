def main():

    p1 = "i"
    p2 = 6

    count = 0

    count += count_patterns_from(p1, p2)

    print(count)


def count_patterns_from(firstPoint, length):

    if length == 1:
        return 1
    if length > 9:
        return 0

    nextPoints = {}
    jumpPoints = {}

    nextPoints["a"] = ["b", "d", "e", "f", "h"]
    nextPoints["b"] = ["a", "c", "d", "e", "f", "g", "i"]
    nextPoints["c"] = ["b", "d", "e", "f", "h"]
    nextPoints["d"] = ["a", "b", "c", "e", "g", "h", "i"]
    nextPoints["e"] = ["a", "b", "c", "d", "f", "g", "h", "i"]
    nextPoints["f"] = ["a", "b", "c", "e", "g", "h", "i"]
    nextPoints["g"] = ["b", "d", "e", "f", "h"]
    nextPoints["h"] = ["a", "c", "d", "e", "f", "g", "i"]
    nextPoints["i"] = ["b", "d", "e", "f", "h"]

    jumpPoints["a"] = ["cb", "ie", "gd"]
    jumpPoints["b"] = ["he"]
    jumpPoints["c"] = ["ab", "ge", "if"]
    jumpPoints["d"] = ["fe"]
    jumpPoints["e"] = []
    jumpPoints["f"] = ["de"]
    jumpPoints["g"] = ["ad", "ce", "ih"]
    jumpPoints["h"] = ["be"]
    jumpPoints["i"] = ["gh", "ae", "cf"]

    firstPoint = firstPoint.lower()
    paths = [firstPoint]

    counter = 1
    possibilityCount = 0

    while counter < length:
        foundPath = []
        for path in paths:
            currPath = list(path)
            lastPoint = currPath[-1]
            possiblePaths = nextPoints[lastPoint]
            for possiblePath in possiblePaths:
                if possiblePath not in currPath:
                    foundPath.append(path + possiblePath)
                    if counter == length - 1:
                        possibilityCount += 1

            possibleJumps = jumpPoints[lastPoint]
            for possibleJump in possibleJumps:
                jump = possibleJump[1]
                point = possibleJump[0]
                if jump in currPath and point not in currPath:
                    foundPath.append(path + point)
                    if counter == length - 1:
                        possibilityCount += 1

        paths = foundPath

        counter += 1

    return possibilityCount


if __name__ == "__main__":
    main()

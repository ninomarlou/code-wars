def main():

    input = [191, 31, 144] 
    input1 = 1

    print(tribonacci(input, input1))


def tribonacci(signature, n):
    
    if n=='' or n==0:
        return []
    elif n<=3:
        return signature[0:n]
    
    result = signature
    idx1 = 0
    idx2 = 1
    idx3 = 2

    while len(result) < n:

        result.append(result[idx1] + result[idx2] + result[idx3])

        idx1 += 1
        idx2 += 1
        idx3 += 1

    return result


if __name__ == "__main__":
    main()

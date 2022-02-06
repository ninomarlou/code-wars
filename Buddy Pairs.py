def main():

    x = 1071625
    y = 1103735

    print(buddy(x, y))


def buddy(start, limit):

    for n in range(start, limit + 1, 1):
        s_proper_n = s_properx(n, 0)
        m=s_proper_n-1
        if m>n:
            s_proper_m=s_properx(m,0)
            if n+1==s_proper_m and m+1==s_proper_n:
                return [n,m]
    return 'Nothing'


def s_properx(n, limit):

    result = 0

    for i in range(1, int(n / 1), 1):
        if n % i == 0:
            result += i
            #print('   n:',n,'result:',result)
            if limit != 0 and result > limit:
                return False

    return result


if __name__ == "__main__":
    main()

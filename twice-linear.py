import datetime


def main():
    x1 = 10305
    start_time = datetime.datetime.now()
    a1 = dbl_linear(x1)
    end_time = datetime.datetime.now()
    time_diff = (end_time - start_time)
    execution_time = time_diff.total_seconds() * 1000
    print(a1, execution_time)


def dbl_linear(n):
    u = [1]
    for i in range(0, n, 1):
        x = u[i]
        y = 2 * x + 1
        insort(u, y)
        z = 3 * x + 1
        insort(u, z)
        if len(u) > n:
            if y > u[n]:
                return u[n]
    return u[n]


def insort(a, x):
    lo = bisect(a, x)
    if a[lo - 1] != x:
        a.insert(lo, x)


def bisect(a, x):
    lo = 0
    hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if x < a[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo


if __name__ == '__main__':
    main()

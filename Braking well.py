import math


def main():

    x = 100
    y = 0.7
    z = 83.9598760937531

    print(dist(x, y))

    print(speed(z, y))


def dist(v, mu):

    v_m = (v * 1000) / 60 / 60
    return round(((v_m ** 2) / (2 * mu * 9.81)) + v_m,2)


def speed(d, mu):

    g = 2 * mu * 9.81
    v = ((g / 2) * -1) + (math.sqrt((g ** 2) + (4 * d) * g) / 2)

    return round((v * 60 * 60) / 1000,2)


if __name__ == "__main__":
    main()

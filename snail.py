import time

def main():

    input = [[1, 2, 3, 1], [4, 5, 6, 4], [7, 8, 9, 7], [7, 8, 9, 7]]
    input1 = 1
    
    start = time.time()

    print(snail(input))
    
    end = time.time()
    print(end - start)


def snail(snail_map):


    result = []
    side = len(snail_map[0])
    r_lim=side
    d_lim=side
    l_lim=-1
    u_lim=-1
    
    direction = "r"
    x = 0
    y = 0
    i = 0

    while i < side ** 2:
        if direction == "r":
            for r in range(x, r_lim, 1):
                x = r
                result.append(snail_map[y][x])
                i += 1
            y += 1
            u_lim+=1
            direction = "d"
            
        if direction == "d":
            for d in range(y, d_lim, 1):
                y = d
                result.append(snail_map[y][x])
                i += 1
            r_lim-=1
            x -= 1
            direction = "l"

        if direction == "l":
            for l in range(x, l_lim, -1):
                x = l
                result.append(snail_map[y][x])
                i += 1
            d_lim-=1
            y -= 1
            direction = "u"

        if direction == "u":

            for u in range(y, u_lim, -1):
                y = u
                result.append(snail_map[y][x])
                i += 1
            l_lim+=1
            x += 1
            direction = "r"

    return result


if __name__ == "__main__":
    main()

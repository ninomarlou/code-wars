import math


def main():

    input = "a1"
    input1 = "c1"

    print(knight(input, input1))

    # print(find_distance(notation_to_coordinates(input), notation_to_coordinates(input1)))


def knight(p1, p2):

    dest = notation_to_coordinates(p2)
    cur_pos = notation_to_coordinates(p1)
    moves = [cur_pos]
    history = [cur_pos]
    counter = 1

    while counter < 1000:
        next_moves = []
        temp = []
        for move in moves:
            temp = find_moves(move)
            for next_move in temp:
                if next_move not in history:
                    next_moves.append(next_move)
                    history.append(next_move)
                    if next_move == dest:
                        return counter
        moves = next_moves
        counter += 1


def find_moves(cur_pos):

    x = cur_pos[0]
    y = cur_pos[1]
    moves = []

    # up right
    if is_valid_notation(x + 1, y + 2):
        moves.append([x + 1, y + 2])

    # up left
    if is_valid_notation(x - 1, y + 2):
        moves.append([x - 1, y + 1])

    # left up
    if is_valid_notation(x - 2, y + 1):
        moves.append([x - 2, y + 1])

    # left down
    if is_valid_notation(x - 2, y - 1):
        moves.append([x - 2, y - 1])

    # down left
    if is_valid_notation(x - 1, y - 2):
        moves.append([x - 1, y - 2])

    # down right
    if is_valid_notation(x + 1, y - 2):
        moves.append([x + 1, y - 2])

    # right up
    if is_valid_notation(x + 2, y + 1):
        moves.append([x + 2, y + 1])

    # right down
    if is_valid_notation(x + 2, y - 1):
        moves.append([x + 2, y - 1])

    return moves


def is_valid_notation(x, y):

    return (x >= 1 and x <= 8) and (y >= 1 and y <= 8)


def notation_to_coordinates(notation):

    dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}

    return [dict.get(notation[0]), int(notation[1])]


def coordinates_to_notation(coordinates):

    dict = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h"}

    return dict.get(coordinates[0]) + str(coordinates[1])


if __name__ == "__main__":
    main()

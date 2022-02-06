import math


def main():

    x = ["A1", "A2", "A3", "A4", "A5"]
    y = [["A1", "X1"], ["A2", "X2"], ["A3", "X3"], ["A4", "X4"]]
    z = {"X1": 100.0, "X2": 200.0, "X3": 250.0, "X4": 300.0}

    print(tour(x, y, z))


def tour(friends, friend_towns, home_to_town_distances):

    friend_locations = {}
    friends_to_visit = []
    result = 0

    for f in friend_towns:
        friend_locations[f[0]] = f[1]

    for f in friends:
        if friend_locations.get(f):
            friends_to_visit.append(f)

    previous_friend = ""
    previous_town = ""
    previous_distance = ""

    for i in range(0, len(friends_to_visit), 1):

        friend = friends_to_visit[i]
        town = friend_locations.get(friend)
        distance = home_to_town_distances.get(town)

        if i == 0:
            # first trip
            result += distance
        else:
            # in between trips
            hypotenuse = distance
            adjacent = previous_distance
            oppposite = math.sqrt((hypotenuse ** 2) - (adjacent ** 2))
            result += oppposite

        previous_friend = friend
        previous_town = friend_locations.get(previous_friend)
        previous_distance = home_to_town_distances.get(previous_town)

    # home trip
    result += previous_distance

    return int(result)


if __name__ == "__main__":
    main()

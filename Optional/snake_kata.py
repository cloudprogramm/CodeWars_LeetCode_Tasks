def snail(snail_map):
    result = []

    while len(snail_map) >= 3:
        result = result + get_outer(snail_map)
        snail_map = cut_outer(snail_map)

    return result + get_outer(snail_map)


def get_outer(snail_map):
    len_map = len(snail_map)

    if len_map == 1:
        return snail_map[0]

    first = snail_map[0]

    second = []
    if len_map >= 3:
        for i in range(1, len_map - 1):
            second.append(snail_map[i][len_map - 1])

    third = snail_map[len_map - 1]
    third.reverse()

    fourth = []
    if len_map >= 3:
        for i in range(1, len_map - 1):
            fourth.append(snail_map[i][0])
    fourth.reverse()

    return first + second + third + fourth


def cut_outer(snail_map):
    len_map = len(snail_map)
    new = []

    for i in range(1, len_map - 1):
        new.append(snail_map[i][1: len_map - 1])

    return new


array = [
    [848, 13, 379, 713, 563, 490, 395, 123, 708, 9, 373, 542, 350, 317, 741, 625]
]
snail(array)

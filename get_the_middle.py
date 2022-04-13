import math


def get_middle(s):
    len_word = len(s)
    middle_char = int(len_word / 2)

    if len_word == 1 or len_word == 2:
        return s

    if len_word % 2 == 0:
        return s[middle_char - 1] + s[middle_char]

    middle_char = math.ceil(middle_char)
    return s[middle_char]


print(get_middle("middle"))
import math


def is_square(n):
    root = round(math.sqrt(n))
    if root ** 2 == n:
        return True
    return False


print(is_square(26))
from math import factorial


def easy_line(n):
    return factorial(n * 2) // factorial(n) ** 2


def easyline(n):
    coef, total = 1, 0

    for i in range(n + 1):
        total += coef ** 2
        coef = coef * (n - i) // (i + 1)

    return total


print(easy_line(4))
print(easyline(4))

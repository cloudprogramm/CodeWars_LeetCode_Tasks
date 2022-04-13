from functools import reduce
from heapq import nlargest


def max_product(lst: list, n_largest_elements: int):

    """It's also faster than sorting the whole array because it uses a partial sort"""
    n_largest = nlargest(n_largest_elements, lst)
    return reduce(lambda x, y: x * y, n_largest)


print(max_product([10, 2, 3, 8, 1, 10, 4], 5))

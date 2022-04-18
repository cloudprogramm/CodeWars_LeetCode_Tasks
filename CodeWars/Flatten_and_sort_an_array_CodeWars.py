import itertools
from typing import List


def flatten_and_sort(array: List) -> List:
    return sorted(itertools.chain.from_iterable([i for i in array]))
    # result = []
    #
    # for i in array:
    #     result += i
    # return sorted(result)


print(flatten_and_sort([[1], [1]]))

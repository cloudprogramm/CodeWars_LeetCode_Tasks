from typing import List
from collections import Counter


def majorityElement(nums: List[int]) -> int:
    number = Counter(nums)
    value = number.most_common()[0][0]

    return value


print(majorityElement([3, 3, 4]))

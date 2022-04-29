from typing import List


def most_frequent(nums: List[int], key: int) -> int:
    following_dict = {}
    max_value = 0
    max_following_number = 0

    for i, value in enumerate(nums):
        if i != 0 and nums[i - 1] == key:
            if value in following_dict:
                following_dict[value] += 1
            else:
                following_dict[value] = 1

    for k, value in following_dict.items():
        if value > max_value:
            max_value = value
            max_following_number = k

    return max_following_number
    # return max(following_dict, key=following_dict.get)


print(most_frequent([2, 2, 2, 2, 3], key=2))

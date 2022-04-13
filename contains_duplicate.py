import typing


def contains_duplicate(nums: list) -> bool:
    nums.sort()

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False


contains_duplicate([1, 2, 3, 1])

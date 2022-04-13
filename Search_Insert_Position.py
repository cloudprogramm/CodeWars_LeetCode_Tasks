from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    for i, value in enumerate(nums):
        if target == value:
            return i
        if i < len(nums) - 1 and (value < target < nums[i + 1]):
            return i + 1
    return len(nums)


print(searchInsert(nums=[1, 3, 5, 6], target=7))


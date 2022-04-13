from typing import List


class Solution:

    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        if len(nums) == 2 and nums[0] + nums[1] == target:
            return [0, 1]

        for i, v in enumerate(nums):
            for j, value in enumerate(nums):
                if v + value == target and i != j:
                    return [i, j]


s = Solution
print(s.twoSum(nums=[3, 2, 3], target=6))

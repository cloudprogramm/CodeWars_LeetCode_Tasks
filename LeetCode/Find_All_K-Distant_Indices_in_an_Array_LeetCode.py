from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        keys = [i for i in range(len(nums)) if nums[i] == key]
        result = []

        for i in range(len(nums)):
            for j in keys:
                if abs(i - j) <= k:
                    result.append(i)
                    break
        return result

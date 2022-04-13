from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        checking_number = 0
        nums.sort()

        for i in range(len(nums)):
            if checking_number not in nums:
                return checking_number
            else:
                checking_number += 1
        return checking_number


s = Solution()
print(s.missingNumber([1, 2]))

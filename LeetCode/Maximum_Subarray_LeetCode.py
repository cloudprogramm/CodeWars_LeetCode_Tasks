from typing import List


def maxSubArray(nums: List[int]) -> int:  # Kadane’s Algorithm:
    max_so_far = min(nums)
    max_ending_here = 0

    for i in nums:
        max_ending_here += i

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

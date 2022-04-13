from typing import List


class Solution:

    @staticmethod
    def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
        result_list = []

        for value in nums1:
            if value in nums2 and value not in result_list:
                result_list.append(value)
        return result_list


s = Solution()
print(s.intersection(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))

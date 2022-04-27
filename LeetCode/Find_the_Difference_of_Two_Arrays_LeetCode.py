from typing import List


def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    set_nums1 = set(nums1)
    set_nums2 = set(nums2)

    result1 = [i for i in set_nums1 if i not in set_nums2]
    result2 = [i for i in set_nums2 if i not in set_nums1]

    return [result1, result2]

class Solution(object):

    @staticmethod
    def num_jewels_in_stones(jewels, stones):
        counter = 0

        for i, value in enumerate(stones):
            if value in jewels:
                counter += 1
        return counter


some = Solution()
print(some.num_jewels_in_stones(jewels="aA", stones="aAAbbbb"))
# Example 1:
#
# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3
# Example 2:
#
# Input: jewels = "z", stones = "ZZ"
# Output: 0

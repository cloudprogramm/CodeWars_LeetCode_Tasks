import collections


class Solution(object):
    def singleNumber(self, nums):
        res = nums[0]

        for i in range(1, len(nums)):
            res = res ^ nums[i]

        return res

        # c = collections.Counter()
        #
        # for word in nums:
        #     c[word] += 1
        # # print(c)
        # print(list(c.keys()))
        # return list(c.keys())[0]
        # return (collections.deque(c, maxlen=1))[0]



c = Solution()
print(c.singleNumber([4,1,2,1,2]))

# Input: nums =
# Output: 1
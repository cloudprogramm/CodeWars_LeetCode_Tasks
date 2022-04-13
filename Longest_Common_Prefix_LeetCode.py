from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        min_s = min(strs)
        max_s = max(strs)
        print(min_s)
        print(max_s)

        if not min_s:
            return ""

        for i in range(len(min_s)):
            if max_s[i] != min_s[i]:
                return max_s[:i]
        return min_s[:]


res = Solution()

print(res.longestCommonPrefix(["ab", "a", "a", "a", "ab", "ab"]))

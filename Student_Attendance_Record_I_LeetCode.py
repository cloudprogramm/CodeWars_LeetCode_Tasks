class Solution:
    def checkRecord(self, s: str) -> bool:
        count_A = 0
        str_len = len(s)

        for i in range(str_len):
            if s[i] == "A":
                count_A += 1
                if count_A == 2:
                    return False
            if i < str_len - 2 and s[i] == s[i + 1] == s[i + 2] == "L":
                return False
        return True


s = Solution()
print(s.checkRecord("LLPPPLL"))

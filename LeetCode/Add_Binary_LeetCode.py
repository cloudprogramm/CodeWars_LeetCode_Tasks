class Solution:

    @staticmethod
    def addBinary(a: str, b: str) -> str:
        integer_sum = int(a, 2) + int(b, 2)

        return str(bin(integer_sum))[2:]


s = Solution

print(s.addBinary(a="11", b="1"))

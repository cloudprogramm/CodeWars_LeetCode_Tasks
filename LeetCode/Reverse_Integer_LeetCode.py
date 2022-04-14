class Solution:

    @staticmethod
    def reverse(x: int) -> int:
        reversed_int = str(abs(x))
        reversed_int = reversed_int.strip()
        reversed_int = int(reversed_int[::-1])

        if not ((-2 ** 31) <= reversed_int <= (2 ** 31 - 1)):
            return 0

        if x < 0:
            return reversed_int * -1
        return reversed_int

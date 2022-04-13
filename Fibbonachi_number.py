class Solution(object):

    @staticmethod
    def fib(n):
        if n == 0:
            return 0
        a = 1
        b = 1

        for i in range(3, n + 1):
            c = a + b
            a = b
            b = c
        return b


s = Solution()
print(s.fib(3))
# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.



import functools


def count_calls(func):
    counter = 0

    @functools.wraps(func)
    def inner(*args, **kwargs):
        nonlocal counter
        counter += 1
        print(f"Call {counter} func <{func.__name__}>")
        func()
    return inner

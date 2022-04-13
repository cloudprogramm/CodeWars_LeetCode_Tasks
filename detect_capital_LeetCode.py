class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return True if word.isupper() or word.islower() or word.istitle() else False


if __name__ == "__main__":
    a = Solution()
    print(a.detectCapitalUse("lag"))

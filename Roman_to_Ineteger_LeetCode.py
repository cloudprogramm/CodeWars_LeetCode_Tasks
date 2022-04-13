class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100, "D": 500,
            "M": 1000, 'IV': 4, 'IX': 9,
            'XL': 40, 'XC': 90, 'CD': 400,
            'CM': 900
        }

        len_number = len(s)
        iterator = 0
        arabian_number = 0

        while iterator < len_number:
            if iterator + 1 < len_number and s[iterator:iterator + 2] in roman:
                arabian_number += roman[s[iterator:iterator + 2]]
                iterator += 2
            else:
                arabian_number += roman[s[iterator]]
                iterator += 1
        return arabian_number


s = Solution()

print(s.romanToInt("IX"))

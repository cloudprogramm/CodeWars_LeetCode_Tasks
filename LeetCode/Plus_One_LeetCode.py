from typing import List


def plusOne(digits: List[int]) -> List[int]:
    number = "".join([str(digit) for digit in digits])
    number = int(number) + 1

    return [int(num) for num in list(str(number))]


print(plusOne([4, 3, 2, 9]))

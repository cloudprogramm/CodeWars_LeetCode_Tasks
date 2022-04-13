def isHappy(n: int) -> bool:
    s = set()

    while n != 1:
        if n in s:
            return False
        s.add(n)

        sum_ = 0
        while n:
            sum_ += (n % 10) ** 2
            n //= 10
        n = sum_
    return n == 1


print(isHappy(19))

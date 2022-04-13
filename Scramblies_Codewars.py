def scramble(s1: str, s2: str) -> bool:
    for i in set(s2):
        if s1.count(i) < s2.count(i):
            return False
    return True
    # return all([s1.count(i) >= s2.count(i) for i in s2])


print(scramble('rkqodlw', 'world'))  # True
print(scramble('katas', 'steak'))  # False

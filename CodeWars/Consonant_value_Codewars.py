import string


def solve(s: str) -> int:
    alphabet = {value: i + 1 for i, value in enumerate(string.ascii_lowercase)}
    max_values = []
    value = 0

    for char in s:
        if char not in "aeiou":
            value += alphabet[char]
        else:
            max_values.append(value)
            value = 0
    return max(max_values)


print(solve("chruschtschov"))

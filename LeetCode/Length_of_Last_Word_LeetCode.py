def lengthOfLastWord(s: str) -> int:
    s = s.strip()
    length = 0

    for i, letter in enumerate(s[::-1]):
        if letter == " " or i == len(s):
            break
        length += 1
    return length


print(lengthOfLastWord("   a"))

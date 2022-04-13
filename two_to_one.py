def longest(a1, a2):
    non_repeat_list_datas = set(list(a1 + a2))

    return ''.join(sorted(non_repeat_list_datas))


a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
print(longest(a, b))  # -> "abcdefklmopqwxy"

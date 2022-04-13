def solve(s):
    lower_words = 0
    upper_words = 0

    for i in s:
        if i == i.upper():
            upper_words += 1
            continue
        lower_words += 1
    if lower_words < upper_words:
        return s.upper()
    return s.lower()


print(solve("cODE"))
# solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
# solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to uppercase.
# solve("coDE") = "code". Upper == lowercase. Change all to lowercase.
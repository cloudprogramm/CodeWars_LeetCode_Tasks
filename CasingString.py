def to_jaden_case(string):
    res = ""

    for iterator, value in enumerate(string):
        if iterator == 0:
            res += string[iterator].upper()
            continue
        if string[iterator - 1] == " ":
            res += string[iterator].upper()
        else:
            res += string[iterator]
    return res


quote = "How can mirrors be real if our eyes aren't real"
print(to_jaden_case(quote))

def accum(s):
    res_str = ""
    counter = 2

    for iterator, value in enumerate(s):
        if iterator == 0:
            res_str += s[0].capitalize() + "-"
            continue

        res_str += (value * counter).capitalize()
        if iterator != len(s) - 1:
            res_str += "-"
        counter += 1
    return res_str


print(accum("ZpglnRxqenU"))  # -> "A-Bb-Ccc-Dddd"
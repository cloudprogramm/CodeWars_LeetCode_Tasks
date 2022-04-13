def printer_error(s):
    counter = 0

    for char in s:
        if char > "m":
            counter += 1

    return f"{counter}/{len(s)}"

s="kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
print(printer_error(s))




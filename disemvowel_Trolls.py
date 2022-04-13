def disemvowel(string_):
    str_without_vowels = ""

    for char in string_:
        if char.lower() not in "a e i o u" or char == " ":
            str_without_vowels += char

    return str_without_vowels


print(disemvowel("This website is for losers LOL!"))


def disemvowel2(string_):
    return "".join(char for char in string_ if char.lower() not in "aeiou")


print(disemvowel2("This website is for losers LOL!"))

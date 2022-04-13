import string


def capitals_first(text):
    alph_upper = list(string.ascii_uppercase)
    alph_lower = list(string.ascii_lowercase)

    list_words = text.split()
    upper_string = ""
    lower_string = ""

    for word in list_words:
        for symbol in word:
            if symbol not in alph_upper and symbol not in alph_lower:
                continue

            if word[0] == word[0].upper():
                upper_string += word + " "
            elif isinstance(word[0], str):
                lower_string += word + " "
    return upper_string + lower_string[:-1]


print(capitals_first("Life Sometimes !Hard gets pretty"))
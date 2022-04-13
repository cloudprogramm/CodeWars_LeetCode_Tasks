def convert_to_title(column_number):
    str_ = ""

    while column_number > 26:
        module_number = column_number % 26

        if module_number == 0:
            column_number = column_number // 26 - 1
            str_ += "Z"
        else:
            column_number = column_number // 26
            str_ += chr(64 + module_number)
    str_ += chr(64 + column_number)
    return str_[::-1]


print(convert_to_title(31))

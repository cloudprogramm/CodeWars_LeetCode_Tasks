def encode(string):
    if len(string) == 1:
        return "1" + string

    result_string = string.upper()
    count_letter = 1
    count_of_letters = ""

    for i in range(1, len(result_string)):
        if result_string[i] == result_string[i - 1]:
            count_letter += 1
        else:
            count_of_letters += str(count_letter) + result_string[i - 1]
            count_letter = 1
        if (i + 1) == len(result_string) and result_string[i] != result_string[i - 1]:
            count_of_letters += str(count_letter) + result_string[i]
            break
        if i == len(result_string) - 1:  # and result_string[i + 1] == result_string[i]:
            count_of_letters += str(count_letter) + result_string[i]

    return count_of_letters


def decode(string):
    temp_string = ""
    result_string = ""

    for i in range(len(string)):
        if string[i].isdigit():
            temp_string += str(string[i])

        if not string[i].isdigit():
            count = int(temp_string)
            letter = string[i]
            result_string += letter * count

            temp_string = ""
    return result_string


print(encode("AAA"))
# print(decode((encode("AAABBBCCCA"))))

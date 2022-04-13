def square_digits(num):
    temp_string = ""

    for i in str(num):
        temp_string += str(int(i) ** 2)
    return temp_string


print(square_digits(811181))

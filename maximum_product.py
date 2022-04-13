def adjacent_element_product(array):
    max_number = -10000000
    iterator = 1

    for value in array[1:]:
        try:
            if value * array[iterator - 1] > max_number:
                max_number = value * array[iterator - 1]
        except ZeroDivisionError:
            pass
        iterator += 1
    return max_number


print(adjacent_element_product([-23, 4, -5, 99, -27, 329, -2, 7, -921]))

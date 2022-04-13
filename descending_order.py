def descending_order(num: int):
    list_of_nums = [value for value in str(num)]

    num = sorted(list(list_of_nums), reverse=True)
    return int(''.join(num))


print(descending_order(123456789))

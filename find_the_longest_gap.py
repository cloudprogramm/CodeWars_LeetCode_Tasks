def gap(num):
    result = bin(num)[2:]

    count_zeros = 0
    temp = 0

    for value in str(result):
        if value == '0':
            temp += 1
        else:
            if temp > count_zeros:
                count_zeros = temp
            temp = 0
    return count_zeros


print(gap(15))  # 1001
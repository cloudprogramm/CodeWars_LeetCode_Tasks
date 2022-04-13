def high_and_low(numbers):
    numbers_list = numbers.split(" ")
    for i, value in enumerate(numbers_list):
        numbers_list[i] = int(value)
    print(numbers_list)

    max_number = max(numbers_list)
    lowest_num = min(numbers_list)

    return str(max_number) + " " + str(lowest_num)


print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))  # return "5 1"
# high_and_low("1 2 -3 4 5")  # return "5 -3"
# high_and_low("1 9 3 4 -5")  # return "9 -5"

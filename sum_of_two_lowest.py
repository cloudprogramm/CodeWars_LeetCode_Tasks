def sum_two_smallest_numbers(numbers):
    first_min = min(numbers)
    second_min = 10000000000000000

    for i in numbers:
        if i < second_min and i != first_min:
            second_min = i

    return first_min + second_min


print(sum_two_smallest_numbers([25, 42, 12, 18, 22]))

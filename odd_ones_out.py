def odd_ones_out(numbers: list) -> list:
    return [value for value in numbers if numbers.count(value) % 2 == 0]


print(odd_ones_out([1, 1, 2, 2, 3, 3, 3]))  # = [1, 1, 2, 2]

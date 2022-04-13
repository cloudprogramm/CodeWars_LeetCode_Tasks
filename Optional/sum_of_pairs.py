def sum_pairs(ints: list, s: int) -> list:
    checked_numbers = set()

    for i in ints:
        is_sum_of_pairs = s - i

        if is_sum_of_pairs in checked_numbers:
            return [is_sum_of_pairs, i]
        checked_numbers.add(i)


print(sum_pairs([10, 5, 2, 3, 7, 5], 10))

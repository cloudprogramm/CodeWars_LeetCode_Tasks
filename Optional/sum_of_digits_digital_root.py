def digital_root(number: int) -> int:
    first_round = list_integer_strings(number)
    result = 0

    while len(first_round) > 1:
        result = sum(first_round)
        first_round = list_integer_strings(result)

    return sum(first_round)


def list_integer_strings(number: int) -> list:
    return [int(symbol) for symbol in list(str(number))]


print(digital_root(29))

def sum_dicts(*args: dict) -> dict:
    temp_dict = {}

    for i in args:
        for j in i:
            if j not in temp_dict:
                temp_dict.update({j: i.get(j)})
            else:
                temp_dict[j] += i.get(j)

    return temp_dict


first = {"a": 2, "b": 4}
second = {"a": 2, "b": 10}
third = {"d": -5}
print(sum_dicts(first, second, third))

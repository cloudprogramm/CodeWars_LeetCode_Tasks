def find_function(func_, arr):
    anonymous_func = None

    for i in func_:
        if not isinstance(i, int):
            anonymous_func = i

    return [number for number in arr if anonymous_func(number)]


print(find_function([lambda a: a % 2 == 0, 9, 3, 1, 0], [1, 2, 3, 4]))

def match_arrays(v, r):
    return sum([1 for value in v if value in r])


print(match_arrays([True, 3, 9, 11, 15], [True, 3, 11]))  # 3

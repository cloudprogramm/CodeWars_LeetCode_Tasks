def contain_all_rots(strng, arr):
    if len(strng) == 0:
        return True
    reverse_string = strng

    for i in arr:
        if reverse_string in arr:
            reverse_string = reverse_string[-1:] + reverse_string[:-1]
        else:
            return False
    return True


print(contain_all_rots("XjYABhR", ["TzYxlgfnhf", "yqVAuoLjMLy", "BhRXjYA", "YABhRXj", "hRXjYAB", "jYABhRX", "XjYABhR", "ABhRXjY"]))  # -> true

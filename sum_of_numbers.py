# def get_sum(a, b):
#     sum_numbers = 0
#     if a == b:
#         return a
#
#     elif a > b:
#         for i in range(b, a + 1):
#             sum_numbers += i
#         return sum_numbers
#     else:
#         for i in range(a, b + 1):
#             sum_numbers += i
#         return sum_numbers
def get_sum(a, b):
    if a == b:
        return a

    if a > b:
        return sum(range(b, a + 1))
    return sum(range(a, b + 1))


print(get_sum(1, 2))
# (1, 0) --> 1 (1 + 0 = 1)
# (1, 2) --> 3 (1 + 2 = 3)
# (0, 1) --> 1 (0 + 1 = 1)
# (1, 1) --> 1 (1 since both are same)
# (-1, 0) --> -1 (-1 + 0 = -1)
# (-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)

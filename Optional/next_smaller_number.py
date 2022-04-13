from itertools import permutations


def next_smaller(n):
    arr = str(n)
    print(arr)

    arr = list(permutations(arr))
    print(arr)

    arr.sort()
    arr.reverse()

    if ''.join(arr[-1]) == str(n):
        return -1

    for i in arr:
        str_res = ''.join(i)

        if int(str_res) >= n:
            continue

        return int(str_res)


print(next_smaller(2071))

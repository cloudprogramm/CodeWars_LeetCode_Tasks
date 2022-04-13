def shoot(results):
    counts = {
        "X": 1, "O": 0
    }
    p1 = 0
    p2 = 0

    for i in results:
        if isinstance(i[0], dict):
            p1_lst = list(i[0]["P1"])
            p2_lst = list(i[0]["P2"])

            if i[1]:
                p1 += (counts[p1_lst[0]] + counts[p1_lst[1]]) * 2
                p2 += (counts[p2_lst[0]] + counts[p2_lst[1]]) * 2
            else:
                p1 += (counts[p1_lst[0]] + counts[p1_lst[1]])
                p2 += (counts[p2_lst[0]] + counts[p2_lst[1]])

    if p1 == p2:
        return "Draw!"
    return "Pete Wins!" if p1 > p2 else "Phil Wins!"


print(
    shoot(
        [[{"P1": "XX", "P2": "XO"}, True],
         [{"P1": "OX", "P2": "OO"}, False],
         [{"P1": "XX", "P2": "OX"}, True]]
    )
    # "Pete Wins!")
)

print(shoot(
    [[{"P1": "XX", "P2": "XO"}, False],
     [{"P1": "OX", "P2": "XX"}, False],
     [{"P1": "OO", "P2": "XX"}, True]]
))

print(shoot(
    [[{"P1": "OO", "P2": "XX"}, False],
     [{"P1": "OO", "P2": "XX"}, False],
     [{"P1": "XX", "P2": "OO"}, True]]
))

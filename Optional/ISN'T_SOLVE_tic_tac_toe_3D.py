def play_OX_3D(moves):
    o_player = []
    x_player = []
    moves_count = 2

    for i, value in enumerate(moves):
        if i % 2 == 0:
            x_player.append(value)
        else:
            o_player.append(value)

    for i, arr in enumerate(x_player):
        for j in arr:
            print(x_player[i][i], x_player[i + 1][i])
            if x_player[i][i] == x_player[i + 1][i]:
                moves_count += 1

        if moves_count == 4:
            print("WIN")


moves = [
    [0, 2, 1],  # O
    [0, 2, 2],
    [1, 2, 1],  # O
    [1, 2, 2],
    [2, 2, 1],  # O
    [2, 2, 2],
    [3, 2, 1]  # O
]
print(play_OX_3D(moves))  # "O wins after 7 moves")

def get_reversed_color(hex_color: str) -> str or None:
    if len(hex_color) >= 7:
        return
    reversed_colors = {
        "A": 5, "B": 4, "C": 3, "D": 2, "E": 1, "F": 0
    }
    list_of_key = list(reversed_colors.keys())
    list_of_value = list(reversed_colors.values())
    temp = ""
    for i in hex_color:
        if i.isnumeric():
            if int(i) > 7:
                temp += "7"
                continue
            position = list_of_value.index(int(i))
            temp += list_of_key[position]
        else:
            temp += str(reversed_colors[i.upper()])

    result_color = "F" * (6 - len(hex_color)) + temp
    return "#" + result_color


print(get_reversed_color("a23"))

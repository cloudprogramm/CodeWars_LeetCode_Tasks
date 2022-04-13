import random


def generate_color_rgb() -> str:
    letters_and_digits = ["a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F",
                          *[str(i) for i in range(10)]]
    random_color = "#"
    while len(random_color) != 7:
        random_color += random.choice(letters_and_digits)
    return random_color


print(generate_color_rgb())

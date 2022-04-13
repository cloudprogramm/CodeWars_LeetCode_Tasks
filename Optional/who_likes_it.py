def likes(names: list) -> str:
    if len(names) == 0:
        return "no one likes this"

    if len(names) == 1:
        return names[0] + " likes this"

    if len(names) == 2:
        return f"{names[0]} and {names[1]} like this"

    if len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"

    return f"{names[0]}, {names[1]} and {len(names)- 2} others like this"


print(likes(["Alex", "Jacob", "Mark", "Max"]))
# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

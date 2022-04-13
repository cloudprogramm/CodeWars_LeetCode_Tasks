def scoreboard(string):
    voice_recognition = {'nil': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    return [voice_recognition[word] for word in string.split() if word in voice_recognition]


print(scoreboard("The score is four nil"))  # [4, 0]

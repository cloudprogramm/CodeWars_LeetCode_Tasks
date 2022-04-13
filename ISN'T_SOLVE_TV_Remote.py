def tv_remote(word):
    keyboard = 'abcde123fghij456klmno789pqrst.@0uvwxyz_/'
    counter = 0
    keyboard_counter = 0
    word_counter = 0

    while True:
        if word_counter == len(word) and keyboard[keyboard_counter] == word[word_counter]:
            counter += 1
            break

        if keyboard[keyboard_counter] == word[word_counter]:
            counter += 1
            word_counter += 1

        if keyboard[keyboard_counter] > word[word_counter]:
            keyboard_counter -= 1
            counter += 1
            continue

        if keyboard[keyboard_counter] < word[word_counter]:
            keyboard_counter += 1
            counter += 1
            continue
    return counter


print(tv_remote("word"))

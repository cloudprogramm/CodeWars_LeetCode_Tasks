def duplicate_count(text):
    count_of_duplicate = 0
    text_str = text.lower()

    for i in text_str:
        if text_str.count(i) > 1:
            text_str = text_str.replace(i, "")
            count_of_duplicate += 1

    return count_of_duplicate


print(duplicate_count("abcdeaB"))
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice
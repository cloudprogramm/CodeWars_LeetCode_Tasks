class Solution(object):
    morse = {"a": ".-",
             "b": "-...",
             "c": "-.-.",
             "d": "-..",
             "e": ".",
             "f": "..-.",
             "g": "--.",
             "h": "....",
             "i": "..",
             "j": ".---",
             "k": "-.-",
             "l": ".-..",
             "m": "--",
             "n": "-.",
             "o": "---",
             "p": ".--.",
             "q": "--.-",
             "r": ".-.",
             "s": "...",
             "t": "-",
             "u": "..-",
             "v": "...-",
             "w": ".--",
             "x": "-..-",
             "y": "-.--",
             "z": "--.."}

    def uniqueMorseRepresentations(self, words: list):
        encrypted_list = []

        for word in words:
            encrypted_string = ""

            for letter in word:
                encrypted_string += self.morse[letter]

            encrypted_list.append(encrypted_string)

        # different_transformations = 0
        # for iterator, transform in enumerate(encrypted_list):
        #     is_different = True
        #
        #     for cipher in encrypted_list[iterator + 1:]:
        #         if transform == cipher:
        #             is_different = False
        #
        #     if is_different:
        #         different_transformations += 1           -------->      len(set(encrypted_list))

        return len(set(encrypted_list))


words = ["gin", "zen", "gig", "msg"]
a = Solution()
print(a.uniqueMorseRepresentations(words))

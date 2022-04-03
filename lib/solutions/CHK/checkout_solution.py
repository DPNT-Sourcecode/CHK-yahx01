from collections import Counter

prices = {"A": 50, "B": 30, "C": 20, "D": 15}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not skus.isalpha():
        return -1

    frequencies = Counter()
    for letter in skus.lower():
        frequencies[letter] += 1


def is_latin_alphabet(letter):
    return



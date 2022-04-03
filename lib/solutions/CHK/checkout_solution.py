from collections import Counter

prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
    "G": 20,
    "H": 10,
    "I": 35,
    "J": 60,
    "K": 80,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 30,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 90,
    "Y": 10,
    "Z": 50,
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(all_skus):
    if any(c not in prices.keys() for c in all_skus):
        return -1

    counter = Counter()
    for sku in all_skus:
        counter[sku] += 1

    return sum(special_offers(counter)) + sum(normal_prices(counter))


def special_offers(counter):
    if counter["A"]:
        yield (counter["A"] // 5) * 200
        counter["A"] %= 5
        yield (counter["A"] // 3) * 130
        counter["A"] %= 3

    # Get a free B with every 2 E
    counter["B"] = max(0, counter["B"] - counter["E"] // 2)

    if counter["B"]:
        yield (counter["B"] // 2) * 45
        counter["B"] %= 2

    counter["F"] -= counter["F"] // 3


def normal_prices(counter):
    yield from (prices[sku] * count for sku, count in counter.most_common())



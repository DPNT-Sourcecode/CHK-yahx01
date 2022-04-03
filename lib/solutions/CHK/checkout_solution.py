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

bundles = [
    ("A", 5, 200),
    ("A", 3, 130),
    ("B", 2, 45),
    ("F", 3, 20),
    ("H", 10, 80),
    ("H", 5, 45),
    ("K", 2, 150),
    ("P", 5, 200),
    ("Q", 3, 80),
    ("U", 3, 80),
    ("V", 3, 130),
    ("V", 2, 90),
]

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(all_skus):
    if any(c not in prices.keys() for c in all_skus):
        return -1

    counter = Counter()
    for sku in all_skus:
        counter[sku] += 1

    apply_special_offers(counter)
    return sum(bundle_prices(counter)) + sum(normal_prices(counter))


def apply_special_offers(counter):
    # 2E get one B free
    counter["B"] = max(0, counter["B"] - counter["E"] // 2)

    # 3R get one Q free
    counter["Q"] = max(0, counter["Q"] - counter["R"] // 3)

    # 3N get one M free
    counter["M"] = max(0, counter["M"] - counter["N"] // 3)


def bundle_prices(counter):
    for sku, count, amount in bundles:
        yield (counter[sku] // count) * amount
        counter[sku] %= count


def normal_prices(counter):
    yield from (prices[sku] * count for sku, count in counter.most_common())






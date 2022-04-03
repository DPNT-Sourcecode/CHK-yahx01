from collections import Counter

prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}

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
        yield (counter["A"] // 3) * 130
        counter["A"] %= 3

    # Get a free B with every 2 E
    counter["B"] = max(0, counter["B"] - counter["E"] // 2)

    if counter["B"]:
        yield (counter["B"] // 2) * 45
        counter["B"] %= 2


def normal_prices(counter):
    yield from (prices[sku] * count for sku, count in counter.most_common())






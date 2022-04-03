from collections import Counter

prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(all_skus):
    if any(c not in prices.keys() for c in all_skus):
        return -1

    frequencies = Counter()
    for sku in all_skus:
        frequencies[sku] += 1

    return sum(price(sku, count) for sku, count in frequencies.most_common())


def price(sku, count):
    return special_offers(counter) + normal_prices(counter)


def special_offers(counter):
    if counter["A"]:
        yield (counter["A"] // 3) * 130
        counter["A"] %= 3
    if counter["B"]:
        yield (counter["B"] // 2) * 130
        counter["B"] %= 2


def normal_prices(counter):
    return sum(prices[sku] * count for sku, count in frequencies.most_common())




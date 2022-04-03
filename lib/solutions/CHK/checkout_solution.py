from collections import Counter

prices = {"A": 50, "B": 30, "C": 20, "D": 15}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(all_skus):
    if any(c not in prices.keys() for c in all_skus):
        return -1

    frequencies = Counter()
    for sku in all_skus.lower():
        frequencies[sku] += 1

    return sum(price(sku, count) for sku, count in frequencies.most_common())


def price(sku, count):
    if sku == "A":
        return (count / 3) * 130 + (count % 3) * prices[sku]
    elif sku == "B":
        return (count / 2) * 45 + (count % 2) * prices[sku]
    else:
        return prices[sku]






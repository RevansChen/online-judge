# Python3

def knapsackLight(value1, weight1, value2, weight2, maxW):
    items = [(value1, weight1), (value2, weight2)]
    items = [(v, w) for v, w in items if w <= maxW]
    if len(items) == 1:
        return items[0][0]
    if sum(w for _, w in items) <= maxW:
        return sum(v for v, _ in items)
    return max(v for v, _ in items)

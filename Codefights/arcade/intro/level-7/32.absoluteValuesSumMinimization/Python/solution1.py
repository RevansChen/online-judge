# Python3

def absoluteValuesSumMinimization(a):
    getTotal = lambda arr, x: sum(abs(e - x) for e in arr)
    values = [ (x, getTotal(a, x)) for x in set(a) ]
    values.sort(key=lambda e: e[1])
    return min(x for x, total in values if total == values[0][1])

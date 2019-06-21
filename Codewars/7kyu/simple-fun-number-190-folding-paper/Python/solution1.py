# Python - 3.6.0

def folding(a, b):
    count = 0
    while a > 0 and b > 0:
        minval = min(a, b)
        a, b = max(a - minval, minval), min(a - minval, minval)
        count += 1
    return count

# Python - 3.6.0

def round_it(n):
    from math import ceil, floor
    s = str(n)
    l = s.index('.')
    r = len(s) - l - 1
    if l < r:
        return ceil(n)
    elif l > r:
        return floor(n)
    else:
        return round(n)

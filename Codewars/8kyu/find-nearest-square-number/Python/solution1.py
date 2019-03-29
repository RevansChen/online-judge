# Python - 3.6.0

def nearest_sq(n):
    sqr = int(n ** 0.5)
    l, r = sqr ** 2, (sqr + 1) ** 2
    return l if (n - l) < (r - n) else r

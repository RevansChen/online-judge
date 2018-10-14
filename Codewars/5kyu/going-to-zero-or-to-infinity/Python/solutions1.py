# Python - 3.4.3

from math import floor

def going(n):
    total, x = 0, 1.0
    for i in range(n, 0, -1):
        total += x
        x *= 1.0 / i
    return floor(total * 1e6) / 1e6

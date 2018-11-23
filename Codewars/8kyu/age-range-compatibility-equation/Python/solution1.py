# Python - 3.4.3

from math import floor
def dating_range(age):
    minage = lambda a: (a / 2) + 7 if a > 14 else 0.9 * a
    maxage = lambda a: (a - 7) * 2 if a > 14 else 1.1 * a
    return '%d-%d' % (floor(minage(age)), floor(maxage(age)))

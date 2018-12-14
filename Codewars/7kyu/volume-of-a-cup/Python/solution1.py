# Python - 2.7.6

import math

def cup_volume(d1, d2, height):
    d1 /= 2.0
    d2 /= 2.0
    return round(math.pi / 3.0 * height * (d1 ** 2 + d1 * d2 + d2 ** 2), 2)

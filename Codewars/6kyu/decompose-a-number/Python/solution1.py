# Python - 3.6.0

import math

def decompose(num):
    kns = []
    x = 2
    while num > 0:
        kn = math.floor(math.log(num, x))
        if (kn <= 1):
            break
        kns.append(kn)
        num -= math.floor(x ** kn)
        x += 1
    return [kns, num]

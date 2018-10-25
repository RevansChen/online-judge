# Python3

import functools

# 有限制修改區域
from fractions import gcd

def leastCommonDenominator(denominators):
    return functools.reduce(lambda a, b: a * b / gcd(a, b), denominators)

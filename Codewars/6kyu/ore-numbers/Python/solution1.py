# Python - 3.6.0

import math

def near(v):
    vf = v - math.floor(v)
    cv = math.ceil(v) - v
    return math.ceil(v) if cv < vf else math.floor(v)

def isInteger(v):
    return abs(v - near(v)) <= 1e-6

def is_ore(number):
    nums = [1, number]
    for n in range(2, number):
        nums += [n] if isInteger(number / float(n)) else []
    return isInteger(len(nums) / sum([1 / float(n) for n in nums]))

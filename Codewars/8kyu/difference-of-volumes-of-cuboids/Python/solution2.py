# Python - 3.4.3

from functools import reduce
from operator import mul

def find_difference(a, b):
    return abs(reduce(mul, a) - reduce(mul, b))
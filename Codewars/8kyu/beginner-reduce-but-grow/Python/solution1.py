# Python - 3.6.0

from operator import mul
from functools import reduce

grow = lambda arr: reduce(mul, arr)

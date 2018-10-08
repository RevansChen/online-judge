# Python3

from operator import add, sub, mul, truediv
def arithmeticExpression(a, b, c):
    return any(calc(a, b) == c for calc in [add, sub, mul, truediv])

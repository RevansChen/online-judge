# Python - 3.6.0

def mxdiflg(a1, a2):
    if a1 and a2:
        from functools import reduce
        a1min, a1max = reduce(min, map(len, a1)), reduce(max, map(len, a1))
        a2min, a2max = reduce(min, map(len, a2)), reduce(max, map(len, a2))
        return max(abs(a1min - a2max), abs(a1max - a2min))
    return -1

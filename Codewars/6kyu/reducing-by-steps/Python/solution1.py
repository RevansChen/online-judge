# Python - 3.6.0

def oper_array(fct, arr, init):
    r = [init]
    for v in arr:
        r.append(fct(r[-1], v))
    return r[1:]

from math import gcd
gcdi = lambda a, b: gcd(abs(a), abs(b))
lcmu = lambda a, b: (abs(a) * abs(b)) // gcd(abs(a), abs(b))
som = lambda a, b: a + b
maxi = max
mini = min

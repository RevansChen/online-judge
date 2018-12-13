# Python - 3.6.0

def relatively_prime(n, l):
    from fractions import gcd
    return [i for i in l if (gcd(n, i) == 1) or (i == 1)]

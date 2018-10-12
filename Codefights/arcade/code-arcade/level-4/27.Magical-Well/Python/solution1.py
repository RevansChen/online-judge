# Python3

def magicalWell(a, b, n):
    return sum((a + i) * (b + i) for i in range(n))

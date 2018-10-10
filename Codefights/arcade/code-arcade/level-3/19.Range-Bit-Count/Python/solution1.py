# Python3

def rangeBitCount(a, b):
    return sum(bin(i)[2:].count('1') for i in range(a, b + 1))

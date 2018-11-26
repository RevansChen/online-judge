# Python - 3.6.0

def hamming_weight(x):
    c = 0
    while x > 0:
        c += x & 0x1
        x >>= 1
    return c

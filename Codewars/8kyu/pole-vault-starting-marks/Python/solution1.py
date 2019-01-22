# Python - 3.6.0

def starting_mark(height):
    minA, maxA = 1.22, 2.13
    minB, maxB = 8.27, 11.85
    p = (height - minA) / (maxA - minA)
    return round(p * (maxB - minB) + minB, 2)

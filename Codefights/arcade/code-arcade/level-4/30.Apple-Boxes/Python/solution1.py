# Python3

def appleBoxes(k):
    return sum((-1) ** i * i ** 2 for i in range(1, k + 1))
